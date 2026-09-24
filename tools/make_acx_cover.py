#!/usr/bin/env python3
"""
Build an ACX / Audible audiobook cover from a book's existing print cover art.

    python3 tools/make_acx_cover.py books/<slug>

ACX wants a SQUARE cover; print covers are portrait (6x9 is 1:1.5). Centre-cropping
a portrait cover to square throws away the top and bottom -- which is where the
series line and the AUTHOR NAME usually live, and ACX requires the author name to
be on the cover. So this recomposes instead of cropping: it lifts the already-
rendered elements (masthead, title, rule, byline, the art's focal object) out of
the print cover and re-lays them out on a square canvas.

Lifting the rendered pixels rather than re-typesetting means the audiobook cover
carries the SAME typeface, weight, letterspacing and colour as the print and ebook
editions, with no font to identify or licence.

Requirements enforced (checked against ACX's published cover art requirements,
help.acx.com/s/article/cover-art-requirements, read 2026-09-24):

    square, 1:1                 minimum 2400 x 2400 px
    JPG / PNG / TIF             RGB (not CMYK)
    at least 72 dpi             at least 24-bit
    maximum 8 MB                title and author legible on the cover

ACX also rejects: pixelated or blurry text, Audible logos, watermarks or third-
party images, references to physical media, other retailers or websites, runtime
or pricing, barcodes and QR codes, and *book jacket designs* -- so the print WRAP
is never a valid audiobook cover. Its barcode alone would fail it twice over.

The compliance checks here are the mechanical ones. Artwork rights, and whether
the art reads at thumbnail size, are still a human call -- the build writes a
contact sheet of thumbnails to make that call an easy one.
"""
import argparse
import os
import sys

try:
    import yaml
    from PIL import Image, ImageChops, ImageDraw
except ImportError as exc:
    sys.exit(f"ERROR: {exc} -- pip install -r requirements.txt")

ACX_MIN = 2400
ACX_MAX_BYTES = 8 * 1024 * 1024
ACX_FORMATS = {"JPEG": ".jpg", "PNG": ".png", "TIFF": ".tif"}
# Sizes Audible actually serves a cover at. The smallest is the browse grid, which
# is where a title either reads or does not.
THUMBNAILS = (500, 300, 200, 100)


def hex_rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def build_background(art, cfg, size):
    """A square background from a type-free patch of the art, so the audiobook
    cover keeps the print cover's own grain rather than a flat fill."""
    bg_cfg = cfg.get("background") or {}
    patch = bg_cfg.get("patch")
    if patch:
        x0, y0, x1, y1 = patch
        bg = art.crop((x0, y0, x1, y1)).resize((size, size), Image.LANCZOS)
    else:
        bg = Image.new("RGB", (size, size), hex_rgb(bg_cfg.get("fill", "#000000")))
    # Optional vertical darkening, which is what gives the print covers their depth.
    grad = bg_cfg.get("gradient")
    if grad:
        top, bottom = hex_rgb(grad["top"]), hex_rgb(grad["bottom"])
        ramp = Image.new("RGB", (1, size))
        px = ramp.load()
        for y in range(size):
            t = y / (size - 1)
            px[0, y] = tuple(int(top[i] + (bottom[i] - top[i]) * t) for i in range(3))
        ramp = ramp.resize((size, size))
        bg = Image.blend(bg, ramp, float(grad.get("strength", 0.5)))
    return bg


def estimate_black_level(crop):
    """Per-channel median of the crop -- i.e. its own background, since these
    elements are type and highlights on a large dark field. Subtracting it is
    what lets an element be lifted without bringing its background rectangle."""
    data = crop.resize((96, 96), Image.LANCZOS).convert("RGB").tobytes()
    return [sorted(data[c::3])[len(data) // 6] for c in range(3)]


def feather_mask(w, h, edge):
    """1.0 in the middle, ramping to 0 at the border -- so a lifted rectangle
    blends into the background instead of showing its own edges."""
    m = Image.new("L", (w, h), 255)
    if edge <= 0:
        return m
    d = ImageDraw.Draw(m)
    for i in range(edge):
        v = int(255 * (i + 1) / (edge + 1))
        d.rectangle([i, i, w - 1 - i, h - 1 - i], outline=v)
    return m


def place(canvas, art, el, size):
    """Lift one element from the art and composite it onto the square canvas."""
    x0, y0, x1, y1 = el["box"]
    crop = art.crop((x0, y0, x1, y1))
    target_w = int(el["width"])
    scale = target_w / crop.width
    target_h = max(1, int(round(crop.height * scale)))
    crop = crop.resize((target_w, target_h), Image.LANCZOS)

    x = int(el["x"]) if "x" in el else (size - target_w) // 2
    y = int(el["y"])

    region = canvas.crop((x, y, x + target_w, y + target_h))
    mode = el.get("mode", "add")
    if mode == "add":
        # The art is light-on-dark, so treat each element as EMISSION: subtract
        # the crop's own background level, then add what is left to the canvas.
        # Taking the brighter of the two instead (a plain lighten) carries the
        # crop's background across as well, and since the print art is vignetted
        # that background differs from the canvas and the rectangle shows.
        level = el.get("black_level") or estimate_black_level(crop)
        emission = ImageChops.subtract(crop, Image.new("RGB", crop.size, tuple(level)))
        merged = ImageChops.add(region, emission)
    elif mode == "lighten":
        merged = ImageChops.lighter(region, crop)
    elif mode == "replace":
        # For an element DARKER than its surroundings -- a dark focal object --
        # where subtracting the background would erase the object itself.
        merged = crop
    else:
        sys.exit(f"ERROR: element '{el.get('name','?')}' has unknown mode "
                 f"'{mode}' (add, lighten or replace).")
    mask = feather_mask(target_w, target_h, int(el.get("feather", 24)))
    canvas.paste(Image.composite(merged, region, mask), (x, y))
    return dict(name=el.get("name", "?"), x=x, y=y, w=target_w, h=target_h,
                scale=round(scale, 3), black_level=tuple(level) if mode == "add" else None)


def check_acx(path, title, author):
    """The mechanical half of ACX's cover requirements."""
    im = Image.open(path)
    n = os.path.getsize(path)
    checks = [
        ("square (1:1)", im.width == im.height, f"{im.width}x{im.height}"),
        (f"at least {ACX_MIN}x{ACX_MIN}", min(im.size) >= ACX_MIN, f"{im.width}x{im.height}"),
        ("JPG / PNG / TIF", im.format in ACX_FORMATS, str(im.format)),
        ("RGB (not CMYK)", im.mode == "RGB", im.mode),
        ("24-bit colour", im.mode == "RGB", f"{im.mode} = 24-bit"),
        ("at least 72 dpi", (im.info.get("dpi", (72, 72))[0] or 72) >= 72,
         f"{int(im.info.get('dpi', (72, 72))[0] or 72)} dpi"),
        ("8 MB or under", n <= ACX_MAX_BYTES, f"{n / 1024 / 1024:.2f} MB"),
        ("title on cover", bool(title), title or "MISSING"),
        ("author on cover", bool(author), author or "MISSING"),
    ]
    print("\nACX compliance")
    ok = True
    for label, passed, detail in checks:
        print(f"  [{'OK ' if passed else 'FAIL'}] {label:22} {detail}")
        ok = ok and passed
    return ok


def contact_sheet(src, out):
    """Audible's own display sizes, side by side. If the title or the author name
    stops reading in the small ones, the cover is not finished."""
    im = Image.open(src).convert("RGB")
    pad, gap = 24, 20
    w = pad * 2 + sum(THUMBNAILS) + gap * (len(THUMBNAILS) - 1)
    h = pad * 2 + max(THUMBNAILS)
    sheet = Image.new("RGB", (w, h), (32, 32, 36))
    x = pad
    for s in THUMBNAILS:
        sheet.paste(im.resize((s, s), Image.LANCZOS), (x, pad))
        x += s + gap
    sheet.save(out, quality=92)
    return out


def measure(art_path, threshold=60, margin=8):
    """Print the bounding box of every bright element in a piece of cover art.

    Filling in `elements` means knowing where the masthead, title, rule and
    byline actually sit in the source art. These covers are light-on-dark, so a
    row/column scan for bright pixels finds them. Feed the boxes it prints into
    acx.yaml, padded a little."""
    im = Image.open(art_path).convert("L")
    w, h = im.size
    data = im.tobytes()
    table = bytes(255 if i > threshold else 0 for i in range(256))
    bw = data.translate(table)

    print(f"{os.path.basename(art_path)}  {w}x{h}  (bright = luminance > {threshold})")

    # A bright strip along an edge is usually an export artifact, and it will
    # drag every bounding box out to the edge if it is not spotted.
    for label, cols in (("left", range(0, 3)), ("right", range(w - 3, w))):
        for x in cols:
            col = sum(bw[y * w + x] for y in range(0, h, 7)) / (255 * (h // 7 + 1))
            if col > 0.25:
                print(f"  NOTE: bright artifact on the {label} edge at x={x} "
                      f"({col * 100:.0f}% of the column). Excluded from the boxes "
                      "below; keep your crops clear of it.")

    bands, start, inb = [], 0, False
    for y in range(margin, h - margin):
        c = bw.count(255, y * w + margin, y * w + w - margin)
        if c > 3 and not inb:
            start, inb = y, True
        elif c <= 3 and inb:
            if y - start > 8:
                bands.append((start, y))
            inb = False
    if inb:
        bands.append((start, h - margin))

    print(f"  {len(bands)} bright band(s)  ->  box: [x0, y0, x1, y1]")
    for y0, y1 in bands:
        xs = [x for x in range(margin, w - margin)
              if any(bw[y * w + x] for y in range(y0, y1))]
        if not xs:
            continue
        print(f"    box: [{min(xs):5}, {y0:5}, {max(xs):5}, {y1:5}]   "
              f"w={max(xs) - min(xs):5}  h={y1 - y0:4}")
    print("\n  Small bands stacked at one x are usually a chain, a rule or the\n"
          "  segments of one element -- merge them into a single box.")


def build(book_dir, config_path=None, out_path=None):
    book_dir = os.path.abspath(book_dir)
    cfg_path = config_path or os.path.join(book_dir, "delivery", "acx.yaml")
    if not os.path.exists(cfg_path):
        sys.exit(f"ERROR: no ACX config at {cfg_path}\n"
                 "       Seed one from books/_template/delivery/acx.yaml")
    with open(cfg_path, encoding="utf-8") as fh:
        cfg = yaml.safe_load(fh) or {}

    def bookpath(p):
        return p if os.path.isabs(p) else os.path.join(book_dir, p)

    size = int(cfg.get("size", ACX_MIN))
    if size < ACX_MIN:
        sys.exit(f"ERROR: size {size} is below ACX's {ACX_MIN}x{ACX_MIN} minimum.")

    art_path = bookpath(cfg.get("source_art") or "")
    if not os.path.exists(art_path):
        sys.exit(f"ERROR: source art not found: {art_path}")
    art = Image.open(art_path).convert("RGB")

    title = (cfg.get("text") or {}).get("title")
    author = (cfg.get("text") or {}).get("author")

    canvas = build_background(art, cfg, size)
    placed = [place(canvas, art, el, size) for el in (cfg.get("elements") or [])]

    out_cfg = cfg.get("output") or {}
    fmt = str(out_cfg.get("format", "jpg")).lower()
    pil_fmt = {"jpg": "JPEG", "jpeg": "JPEG", "png": "PNG", "tif": "TIFF",
               "tiff": "TIFF"}.get(fmt)
    if pil_fmt is None:
        sys.exit(f"ERROR: output.format '{fmt}' is not one ACX accepts "
                 "(jpg, png or tif).")
    if out_path:
        out = os.path.abspath(out_path)
    else:
        name = out_cfg.get("name") or "acx-cover"
        out = os.path.join(bookpath(out_cfg.get("dir", "delivery/cover")),
                           name + ACX_FORMATS[pil_fmt])
    os.makedirs(os.path.dirname(out), exist_ok=True)

    save_kw = {"dpi": (72, 72)}
    if pil_fmt == "JPEG":
        save_kw.update(quality=int(out_cfg.get("quality", 92)),
                       subsampling=0, optimize=True)
    canvas.save(out, pil_fmt, **save_kw)

    print(f"wrote {out}")
    print(f"  canvas   {size}x{size}  from {os.path.basename(art_path)} "
          f"({art.width}x{art.height})")
    for p in placed:
        lvl = f"  black {p['black_level']}" if p.get("black_level") else ""
        print(f"  element  {p['name']:10} {p['w']:4}x{p['h']:4} at ({p['x']},{p['y']}) "
              f"scale {p['scale']}{lvl}")

    sheet = contact_sheet(out, os.path.join(os.path.dirname(out),
                                            "_acx-thumbnail-check.jpg"))
    ok = check_acx(out, title, author)
    print(f"\n  thumbnails {os.path.relpath(sheet, os.getcwd())}")
    print("             check the title and author still read at 100px "
          "-- that is the browse grid.")
    if not ok:
        sys.exit("\nERROR: the cover does not meet ACX's requirements (above).")
    return out


def main():
    ap = argparse.ArgumentParser(
        description="Build an ACX-compliant square audiobook cover.")
    ap.add_argument("book_dir", help="path to the book folder")
    ap.add_argument("--config", help="default: <book>/delivery/acx.yaml")
    ap.add_argument("--out", help="output image path")
    ap.add_argument("--measure", metavar="ART", nargs="?", const=True,
                    help="print the bounding boxes of the elements in the cover "
                         "art (defaults to the config's source_art) and exit")
    args = ap.parse_args()
    if args.measure:
        art = args.measure
        if art is True:
            cfg_path = args.config or os.path.join(os.path.abspath(args.book_dir),
                                                   "delivery", "acx.yaml")
            if not os.path.exists(cfg_path):
                sys.exit(f"ERROR: no config at {cfg_path}; pass the art path to "
                         "--measure instead.")
            with open(cfg_path, encoding="utf-8") as fh:
                art = (yaml.safe_load(fh) or {}).get("source_art")
            art = os.path.join(os.path.abspath(args.book_dir), art)
        if not os.path.exists(art):
            sys.exit(f"ERROR: art not found: {art}")
        measure(art)
        return
    build(args.book_dir, args.config, args.out)


if __name__ == "__main__":
    main()
