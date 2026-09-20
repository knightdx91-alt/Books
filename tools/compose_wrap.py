#!/usr/bin/env python3
"""
Compose a print-ready cover WRAP (back panel + spine + front panel) for any book.

    python3 tools/compose_wrap.py books/<slug> --init   # ask for the specs
    python3 tools/compose_wrap.py books/<slug>          # build the wrap
    python3 tools/compose_wrap.py books/<slug> --config delivery/cover.yaml
    python3 tools/compose_wrap.py books/<slug> --out /tmp/proof.pdf

--init takes the specs that cannot be fixed after printing -- trim, paper stock,
page count, print ISBN, front art -- confirms the resulting spine against the
operator, and writes delivery/cover.yaml with the back-cover copy left as
placeholders to edit.

Config-driven twin of tools/make_epub.py: the book supplies delivery/cover.yaml,
this supplies the geometry, typesetting and the IngramSpark compliance. Replaces
the per-book compose_wrap.py copies, which hardcoded one book's palette, pen name,
page count and art paths.

WHAT THIS DOES AND DOES NOT DO
The client/author supplies FRONT COVER ART ONLY. This builds everything else:
the back panel (blurb, author block, EAN-13), the spine (title + author, width
computed from the page count), the bleed-safe background, and the full-bleed
single-page PDF that IngramSpark wants. The front art is placed into the front
panel scale-to-fill with a CENTER CROP -- art at the wrong aspect ratio loses its
edges, so the report below prints the crop and the effective resolution.

It does NOT design a cover. It does not colour-correct, retouch or upscale art
(tools/cover_art_to_print_res.py is the separate upscaler, and it adds no detail).

OUTPUT is an RGB proof. Convert it for upload:

    bash tools/make_noicc.sh cmyk <wrap.pdf> <wrap-CMYK-noicc.pdf>
    python3 tools/check_upload_pdf.py cover  <wrap-CMYK-noicc.pdf>

THE SPINE IS THE ONE DIMENSION A REPRINT CANNOT FIX. Its width is page count x
paper factor, so the interior must be final before the cover is built, and the
paper stock must be the stock actually ordered. Only the two factors this project
has verified against accepted books ship here; anything else must be given
explicitly as paper.factor, read off IngramSpark's own spine calculator.
"""
import argparse
import atexit
import os
import sys

# Scratch images written beside the source art / output while composing. Cleared
# on every exit path, so a config error never leaves debris in a book folder.
_TMPS = []


def _cleanup_tmps():
    while _TMPS:
        try:
            os.remove(_TMPS.pop())
        except OSError:
            pass


atexit.register(_cleanup_tmps)

try:
    import yaml
except ImportError:
    sys.exit("ERROR: pyyaml not installed -- pip install -r requirements.txt")
try:
    from PIL import Image
    from reportlab.lib.units import inch
    from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT, TA_JUSTIFY
    from reportlab.lib.colors import Color, HexColor
    from reportlab.lib.styles import ParagraphStyle
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    from reportlab.pdfgen import canvas as rl_canvas
    from reportlab.platypus import Paragraph, Frame
except ImportError as exc:
    sys.exit(f"ERROR: {exc} -- pip install -r requirements.txt")

# ---------------------------------------------------------------- paper stocks
# Inches of spine per interior page. ONLY factors verified against a book this
# project has had accepted and printed. Everything else is a deliberate error:
# guessing here wastes a whole print run.
PAPER_STOCKS = {
    "white50": 0.002252,   # IngramSpark white 50#
    "cream50": 0.0025,     # IngramSpark cream 50#
}

ALIGN = {"left": TA_LEFT, "center": TA_CENTER, "centre": TA_CENTER,
         "right": TA_RIGHT, "justify": TA_JUSTIFY}

# Font search order. A fork on a bare machine still gets an embeddable serif.
FONT_DIRS = [
    "/mnt/skills/examples/canvas-design/canvas-fonts",
    "/usr/share/fonts/truetype/dejavu",
    "/usr/share/fonts/truetype/liberation",
]
FONT_SETS = [
    dict(regular="IBMPlexSerif-Regular.ttf", italic="IBMPlexSerif-Italic.ttf",
         bold="IBMPlexSerif-Bold.ttf", bolditalic="IBMPlexSerif-BoldItalic.ttf"),
    dict(regular="DejaVuSerif.ttf", italic="DejaVuSerif-Italic.ttf",
         bold="DejaVuSerif-Bold.ttf", bolditalic="DejaVuSerif-BoldItalic.ttf"),
    dict(regular="LiberationSerif-Regular.ttf", italic="LiberationSerif-Italic.ttf",
         bold="LiberationSerif-Bold.ttf", bolditalic="LiberationSerif-BoldItalic.ttf"),
]

DEFAULTS = {
    "trim": {"width": 6.0, "height": 9.0, "bleed": 0.125, "safe": 0.375},
    "paper": {"stock": "white50"},
    "palette": {"bg": "#0A0A0C", "primary": "#DCE2EC",
                "secondary": "#AEB8C6", "accent": "#C9A25A"},
    "front": {"trim_white_strip": False},
    "spine": {"title_size": 14, "author_size": 11, "title_offset": 1.5,
              "author_offset": 0.55, "baseline_nudge": 5,
              "title_color": "primary", "author_color": "secondary"},
    "back": {"frame_gap": 0.28, "blocks": []},
    "author_block": {"photo_size": 1.0, "gap": 0.15, "height": 1.0,
                     "name_size": 9, "bio_size": 7.5,
                     "name_color": "accent", "bio_color": "secondary"},
    "barcode": {"enabled": True, "width": 1.9, "height": 1.1,
                "pad_x": 0.13, "pad_y": 0.12},
    "output": {"dir": "delivery/cover", "revision_file": "REVISION"},
}

# Style presets so a minimal cover.yaml still typesets a sane back panel.
STYLE_DEFAULTS = {
    "font": "regular", "size": 10, "leading": 14.5, "color": "secondary",
    "align": "left", "space_before": 0, "space_after": 9,
}


def deep_merge(base, over):
    out = dict(base)
    for k, v in (over or {}).items():
        out[k] = deep_merge(base[k], v) if isinstance(v, dict) and isinstance(base.get(k), dict) else v
    return out


def register_fonts(cfg_fonts):
    """Register the four faces and return the reportlab names. Also aliases
    Helvetica: reportlab declares that base-14 slot even when unused, it is NOT
    embedded, and IngramSpark preflight fails the file for it."""
    chosen = None
    if cfg_fonts and cfg_fonts.get("dir"):
        d = cfg_fonts["dir"]
        files = {k: cfg_fonts.get(k) for k in ("regular", "italic", "bold", "bolditalic")}
        if all(files.values()) and all(os.path.exists(os.path.join(d, f)) for f in files.values()):
            chosen = (d, files)
    if chosen is None:
        for d in FONT_DIRS:
            for fs in FONT_SETS:
                if all(os.path.exists(os.path.join(d, f)) for f in fs.values()):
                    chosen = (d, fs)
                    break
            if chosen:
                break
    if chosen is None:
        sys.exit("ERROR: no usable TTF font set found. Set fonts.dir + the four "
                 f"faces in cover.yaml, or install DejaVu. Searched: {FONT_DIRS}")
    d, files = chosen
    names = {}
    for face, fname in files.items():
        name = f"Wrap-{face}"
        pdfmetrics.registerFont(TTFont(name, os.path.join(d, fname)))
        names[face] = name
    pdfmetrics.registerFont(TTFont("Helvetica", os.path.join(d, files["regular"])))
    return names, d


def color_of(value, palette):
    """A palette key ('primary') or a literal hex ('#C9A25A')."""
    if value in palette:
        value = palette[value]
    return HexColor(value)


def make_style(name, spec, fonts, palette):
    s = deep_merge(STYLE_DEFAULTS, spec)
    align = ALIGN.get(str(s["align"]).lower())
    if align is None:
        sys.exit(f"ERROR: style '{name}' has unknown align '{s['align']}'")
    face = s["font"]
    if face not in fonts:
        sys.exit(f"ERROR: style '{name}' wants font '{face}'; "
                 f"choose one of {sorted(fonts)}")
    return ParagraphStyle(name, fontName=fonts[face], fontSize=s["size"],
                          leading=s["leading"], textColor=color_of(s["color"], palette),
                          alignment=align, spaceBefore=s["space_before"],
                          spaceAfter=s["space_after"])


def isbn_digits(isbn):
    """The first 12 digits of the print ISBN -- EAN-13 recomputes the check digit.
    Called during config validation so a bad ISBN fails before anything is drawn."""
    digits = "".join(ch for ch in str(isbn) if ch.isdigit())[:12]
    if len(digits) != 12:
        sys.exit(f"ERROR: isbn '{isbn}' has {len(digits)} digits before the check "
                 "digit; an EAN-13 needs 12 (a 979-8 print ISBN, not the eBook one)")
    return digits


def render_ean13(isbn, workdir):
    """Render the print ISBN as a real EAN-13 PNG. None if python-barcode is
    missing -- the caller then draws a labelled placeholder box."""
    try:
        from barcode import EAN13
        from barcode.writer import ImageWriter
    except ImportError:
        return None
    digits = isbn_digits(isbn)
    base = os.path.join(workdir, "_ean13")
    # EAN13 recomputes the check digit from the first 12 digits.
    EAN13(digits, writer=ImageWriter()).save(
        base, options={"module_height": 12.0, "quiet_zone": 2.0,
                       "font_size": 8, "text_distance": 3.0, "dpi": 600})
    return base + ".png"


def trim_white_strip(src, dst):
    """Crop a mostly-white bottom strip so dark art can bleed off-trim. Some
    front-cover exports carry a white band under the art."""
    im = Image.open(src).convert("RGB")
    w, h = im.size
    step = max(1, w // 100)

    def row_is_white(y):
        xs = range(0, w, step)
        return sum(1 for x in xs if sum(im.getpixel((x, y))) > 720) / len(list(xs))

    cut, y = h, h - 1
    while y > int(h * 0.85) and row_is_white(y) > 0.5:
        cut, y = y, y - 1
    if cut == h:
        return src
    im.crop((0, 0, w, cut)).save(dst)
    return dst


def draw_cover_fit(c, img_path, x, y, w, h):
    """Place the image to COVER the (x, y, w, h) rect in inches: scale-to-fill
    with a center crop. Returns (tmp_path, stats) for the report."""
    im = Image.open(img_path)
    iw, ih = im.size
    target, src = w / h, iw / ih
    if src > target:                       # wider than the panel -> crop the sides
        new_w = int(ih * target)
        box = ((iw - new_w) // 2, 0, (iw - new_w) // 2 + new_w, ih)
    else:                                  # taller -> crop top and bottom
        new_h = int(iw / target)
        box = (0, (ih - new_h) // 2, iw, (ih - new_h) // 2 + new_h)
    fit = img_path + ".fit.png"
    im.convert("RGB").crop(box).save(fit)
    cw, ch = box[2] - box[0], box[3] - box[1]
    stats = {
        "source_px": (iw, ih), "cropped_px": (cw, ch),
        "lost_w_pct": round(100 * (iw - cw) / iw, 1),
        "lost_h_pct": round(100 * (ih - ch) / ih, 1),
        "effective_ppi": round(cw / w, 1),
    }
    c.drawImage(fit, x * inch, y * inch, w * inch, h * inch, mask=None)
    return fit, stats


def require(cfg, path):
    node, parts = cfg, path.split(".")
    for p in parts:
        if not isinstance(node, dict) or p not in node or node[p] in (None, ""):
            sys.exit(f"ERROR: cover.yaml is missing required key '{path}'")
        node = node[p]
    return node


# ------------------------------------------------------------------ intake
# Common IngramSpark perfect-bound trims. NOT exhaustive, and which trims are
# available depends on binding and stock -- confirm against IngramSpark before
# ordering. Any other size goes in as a custom width x height.
TRIM_PRESETS = [
    ("5 x 8", 5.0, 8.0),
    ("5.25 x 8", 5.25, 8.0),
    ("5.5 x 8.5", 5.5, 8.5),
    ("6 x 9", 6.0, 9.0),
    ("6.14 x 9.21", 6.14, 9.21),
    ("7 x 10", 7.0, 10.0),
    ("8.5 x 11", 8.5, 11.0),
]


def ask(prompt, default=None, validate=None):
    """Prompt until the answer validates. Empty input takes the default.
    validate(raw) returns the parsed value or raises ValueError(message)."""
    suffix = f" [{default}]" if default not in (None, "") else ""
    while True:
        try:
            raw = input(f"{prompt}{suffix}: ").strip()
        except EOFError:
            if default is not None:
                raw = str(default)
                print(f"  (no input -- using {default})")
            else:
                sys.exit("\nERROR: input ended before a required answer was given.")
        if not raw:
            if default is None:
                print("  required.")
                continue
            raw = str(default)
            if not raw:          # an empty default means "optional, leave blank"
                return ""
        if validate is None:
            return raw
        try:
            return validate(raw)
        except ValueError as exc:
            print(f"  {exc}")


def ask_yes_no(prompt, default=True):
    d = "Y/n" if default else "y/N"
    while True:
        try:
            raw = input(f"{prompt} [{d}]: ").strip().lower()
        except EOFError:
            return default
        if not raw:
            return default
        if raw in ("y", "yes"):
            return True
        if raw in ("n", "no"):
            return False
        print("  answer y or n.")


def _pos_float(raw):
    v = float(raw)
    if v <= 0:
        raise ValueError("must be greater than zero.")
    return v


def sample_bg(path):
    """Sample the art's border for a back-panel/bleed background colour.

    Returns (darker, median) as hex. The DARKER reading (25th percentile per
    channel) is the suggestion: it tracks the real background on dark covers,
    where the median gets dragged up by a bright focal area. On the three
    covers this was checked against, median missed one badly (#757478 for art
    whose background is #0A0A0C) while the 25th percentile stayed close on all
    three. Neither is authoritative -- the caller offers both and takes an
    override, because a light-background cover inverts the logic."""
    im = Image.open(path).convert("RGB")
    w, h = im.size
    px = []
    for x in range(0, w, max(1, w // 60)):
        px.append(im.getpixel((x, 0)))
        px.append(im.getpixel((x, h - 1)))
    for y in range(0, h, max(1, h // 60)):
        px.append(im.getpixel((0, y)))
        px.append(im.getpixel((w - 1, y)))
    n = len(px)
    chan = [sorted(p[i] for p in px) for i in range(3)]
    hexc = lambda t: "#%02X%02X%02X" % tuple(t)
    return (hexc(tuple(c[n // 4] for c in chan)),
            hexc(tuple(c[n // 2] for c in chan)))


def init_config(book_dir, config_path=None):
    """Interactive intake: ask for the specs, then write delivery/cover.yaml."""
    book_dir = os.path.abspath(book_dir)
    if not os.path.isdir(book_dir):
        sys.exit(f"ERROR: no such book folder: {book_dir}")
    out_cfg = config_path or os.path.join(book_dir, "delivery", "cover.yaml")
    if os.path.exists(out_cfg):
        print(f"{out_cfg} already exists.")
        if not ask_yes_no("Overwrite it?", default=False):
            sys.exit("Left the existing config alone.")

    def bookpath(rel):
        return rel if os.path.isabs(rel) else os.path.join(book_dir, rel)

    print(f"\nCover specs for {os.path.basename(book_dir)}")
    print("Enter accepts the default in brackets.\n")

    # --- trim -------------------------------------------------------------
    print("Trim size:")
    for i, (label, _, _) in enumerate(TRIM_PRESETS, 1):
        print(f"  {i}) {label}\"" + ("   <- most common" if label == "6 x 9" else ""))
    print(f"  {len(TRIM_PRESETS) + 1}) other")

    def _trim_choice(raw):
        n = int(raw)
        if not 1 <= n <= len(TRIM_PRESETS) + 1:
            raise ValueError("pick a number from the list.")
        return n

    choice = ask("  choice", default=4, validate=_trim_choice)
    if choice == len(TRIM_PRESETS) + 1:
        tw = ask("  trim width (inches)", validate=_pos_float)
        th = ask("  trim height (inches)", validate=_pos_float)
    else:
        _, tw, th = TRIM_PRESETS[choice - 1]
    print(f"  -> {tw} x {th}\"\n")

    # --- paper + page count, i.e. the spine -------------------------------
    print("Paper stock -- this sets the spine width with the page count.")
    print("  1) white 50#   (0.002252\"/page)")
    print("  2) cream 50#   (0.0025\"/page)")
    print("  3) other       (factor from IngramSpark's spine calculator)")

    def _stock_choice(raw):
        n = int(raw)
        if n not in (1, 2, 3):
            raise ValueError("pick 1, 2 or 3.")
        return n

    sc = ask("  choice", default=1, validate=_stock_choice)
    stock, factor = None, None
    if sc == 1:
        stock, factor = "white50", PAPER_STOCKS["white50"]
    elif sc == 2:
        stock, factor = "cream50", PAPER_STOCKS["cream50"]
    else:
        print("  Take this off IngramSpark's spine calculator for your stock --")
        print("  the spine is the one dimension a reprint cannot fix.")
        factor = ask("  inches of spine per page", validate=_pos_float)

    def _pages(raw):
        n = int(raw)
        if n < 24:
            raise ValueError("perfect binding needs a real page count (24+).")
        return n

    print("\nPage count -- the FINAL interior's physical page count.")
    print("  Re-cut the interior later and the spine is wrong, so build the")
    print("  cover after the interior is locked.")
    pages = ask("  pages", validate=_pages)
    if pages % 2:
        print(f"  WARNING: {pages} is odd. Perfect binding needs an even page")
        print("           count -- check the interior before ordering.")

    spine = pages * factor
    full_w = 2 * tw + spine + 2 * 0.125
    full_h = th + 2 * 0.125
    print(f"\n  spine  {spine:.4f}\"  = {pages} x {factor}")
    print(f"  wrap   {full_w:.3f}\" x {full_h:.3f}\"  (with 0.125\" bleed)")
    if not ask_yes_no("  Does that spine match IngramSpark's calculator?", default=True):
        sys.exit("Stopped. Re-check the page count and stock, then run --init again.")

    # --- barcode ----------------------------------------------------------
    print("\nBarcode:")
    own_barcode = ask_yes_no("  Bake a real EAN-13 into the cover?", default=True)
    isbn = None
    if own_barcode:
        def _isbn(raw):
            digits = "".join(ch for ch in raw if ch.isdigit())[:12]
            if len(digits) != 12:
                raise ValueError(f"got {len(digits)} digits, need 12 "
                                 "(the PRINT ISBN, not the eBook one).")
            return raw.strip()
        isbn = ask("  print ISBN", validate=_isbn)
    else:
        print("  -> barcode disabled; tell IngramSpark to supply one.")

    # --- front art --------------------------------------------------------
    print("\nFront cover art:")

    def _art(raw):
        if not os.path.exists(bookpath(raw)):
            raise ValueError(f"not found: {bookpath(raw)}")
        return raw
    art = ask("  path (relative to the book folder)", validate=_art)
    art_abs = bookpath(art)
    im = Image.open(art_abs)
    iw, ih = im.size
    panel_w, panel_h = tw + 0.125, full_h
    target, src = panel_w / panel_h, iw / ih
    crop_w = int(ih * target) if src > target else iw
    ppi = crop_w / panel_w
    lost = round(100 * (iw - crop_w) / iw, 1)
    print(f"  {iw}x{ih}px -> centre-cropped to {panel_w}x{panel_h}\" "
          f"(loses {lost}% of width)")
    if ppi >= 300:
        print(f"  {ppi:.0f} ppi effective -- OK")
    else:
        print(f"  {ppi:.0f} ppi effective -- UNDER 300, will print soft.")
        print(f"  Ask for at least {int(round(300 * panel_w))}x"
              f"{int(round(300 * panel_h))}px.")
        if not ask_yes_no("  Continue anyway?", default=False):
            sys.exit("Stopped. Get higher-resolution art.")
    strip = ask_yes_no("  Does the art have a white band at the bottom to crop?",
                       default=False)

    # --- palette ----------------------------------------------------------
    print("\nBackground colour -- the back panel and any bleed gap are painted")
    print("this, so it should match the art's BACKGROUND, not its brightest area.")
    darker, median = sample_bg(art_abs)
    print(f"  sampled from the art's edges:  darker {darker}   median {median}")

    def _hex(raw):
        v = raw.strip().upper()
        if not v.startswith("#"):
            v = "#" + v
        if len(v) != 7 or any(ch not in "0123456789ABCDEF" for ch in v[1:]):
            raise ValueError("give a 6-digit hex colour, e.g. #0A0A0C.")
        return v
    bg = ask("  background colour", default=darker, validate=_hex)

    # --- text -------------------------------------------------------------
    print("\nText:")
    title = ask("  book title (as it reads on the spine)")
    author = ask("  author name (the pen name on this cover)")
    out_name = ask("  output filename (no extension)",
                   default=title.replace(" ", "-") + "-FULL-WRAP")
    bio = ask("  author bio for the back panel (blank to leave it out)",
              default="")
    photo = ""
    if ask_yes_no("  Is there an author photo?", default=False):
        photo = ask("    path (relative to the book folder)", validate=_art)

    # --- write ------------------------------------------------------------
    def y(v):
        return '"' + str(v).replace('"', '\\"') + '"'

    paper_block = (f"  stock: {stock}" if stock
                   else f"  factor: {factor}        # from IngramSpark's calculator")
    lines = [
        "# Cover wrap config -- read by tools/compose_wrap.py",
        "#",
        f"#   python3 tools/compose_wrap.py {os.path.relpath(book_dir, os.getcwd())}",
        "#",
        "# Written by --init. The specs below are the unfixable ones; the back-cover",
        "# copy is placeholder text -- edit it, then build.",
        "",
        f"pages: {pages}",
        "paper:",
        paper_block,
        "",
        (f"isbn: {y(isbn)}" if isbn else "# isbn: not used -- IngramSpark supplies the barcode"),
        "",
        "metadata:",
        f"  title: {y(title)}",
        f"  author: {y(author)}",
        "",
        "output:",
        "  dir: delivery/cover",
        f"  name: {y(out_name)}",
        "  revision_file: REVISION",
        "",
        f"trim: {{width: {tw}, height: {th}, bleed: 0.125, safe: 0.375}}",
        "",
        "palette:",
        f'  bg: "{bg}"',
        '  primary: "#DCE2EC"',
        '  secondary: "#AEB8C6"',
        '  accent: "#C9A25A"',
        "",
        "front:",
        f"  art: {y(art)}",
        f"  trim_white_strip: {str(bool(strip)).lower()}",
        "",
        "spine:",
        f"  title: {y(title.upper())}",
        f"  author: {y(author)}",
        "  title_size: 14",
        "  author_size: 11",
        "",
        "styles:",
        "  hook:    {font: bolditalic, size: 12,  leading: 16,   color: primary,   align: center, space_after: 14}",
        "  para:    {font: regular,    size: 10,  leading: 14.5, color: secondary, align: left,   space_after: 9}",
        "  closing: {font: italic,     size: 9.5, leading: 13.5, color: primary,   align: center, space_before: 6, space_after: 0}",
        "",
        "back:",
        "  frame_gap: 0.28",
        "  blocks:                       # TODO: replace with the real back-cover copy",
        '    - {style: hook, text: "One line that makes someone turn the book over."}',
        '    - {style: para, text: "The setup paragraph."}',
        '    - {style: para, text: "What goes wrong."}',
        '    - {style: closing, text: "The closing positioning line."}',
        "",
    ]
    if bio or photo:
        lines += ["author_block:"]
        if photo:
            lines += [f"  photo: {y(photo)}"]
        lines += [f"  name: {y(author.upper())}"]
        if bio:
            lines += [f"  bio: {y(bio)}"]
        lines += [""]
    lines += [("barcode: {enabled: true, width: 1.9, height: 1.1}" if isbn
               else "barcode: {enabled: false}"), ""]

    os.makedirs(os.path.dirname(out_cfg), exist_ok=True)
    with open(out_cfg, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines))

    rel = os.path.relpath(out_cfg, os.getcwd())
    print(f"\nwrote {rel}")
    print(f"  spine {spine:.4f}\"  wrap {full_w:.3f}\" x {full_h:.3f}\"")
    print("\nNext:")
    print(f"  1. edit the back.blocks copy in {rel}")
    print(f"  2. python3 tools/compose_wrap.py "
          f"{os.path.relpath(book_dir, os.getcwd())}")
    return out_cfg


def build(book_dir, config_path=None, out_path=None):
    book_dir = os.path.abspath(book_dir)
    cfg_path = config_path or os.path.join(book_dir, "delivery", "cover.yaml")
    if not os.path.exists(cfg_path):
        sys.exit(f"ERROR: no cover config at {cfg_path}\n"
                 f"       Run:  python3 tools/compose_wrap.py {book_dir} --init\n"
                 "       to be asked for the specs, or copy "
                 "books/_template/delivery/cover.yaml")
    with open(cfg_path, encoding="utf-8") as fh:
        cfg = deep_merge(DEFAULTS, yaml.safe_load(fh) or {})

    def bookpath(p):
        return p if os.path.isabs(p) else os.path.join(book_dir, p)

    # ---- geometry ----------------------------------------------------------
    trim = cfg["trim"]
    TRIM_W, TRIM_H = float(trim["width"]), float(trim["height"])
    BLEED, SAFE = float(trim["bleed"]), float(trim["safe"])
    pages = int(require(cfg, "pages"))
    paper = cfg["paper"]
    if paper.get("factor") is not None:
        factor, stock_label = float(paper["factor"]), f"custom {paper['factor']}"
    else:
        stock = str(paper.get("stock", "")).lower()
        if stock not in PAPER_STOCKS:
            sys.exit(f"ERROR: unknown paper stock '{stock}'. Verified stocks: "
                     f"{sorted(PAPER_STOCKS)}. For any other stock set "
                     "paper.factor explicitly from IngramSpark's spine calculator "
                     "-- the spine is the one dimension a reprint cannot fix.")
        factor, stock_label = PAPER_STOCKS[stock], stock
    spine = pages * factor
    full_w = 2 * TRIM_W + spine + 2 * BLEED
    full_h = TRIM_H + 2 * BLEED

    # ---- validate before drawing anything ----------------------------------
    # Everything that can be known from the config alone is checked here, so a
    # bad config fails on the config and never half-builds a wrap.
    isbn = cfg.get("isbn")
    if cfg["barcode"].get("enabled", True):
        if not isbn:
            sys.exit("ERROR: barcode is enabled but no 'isbn' is set. Use the PRINT "
                     "ISBN (not the eBook one), or set barcode.enabled: false if "
                     "IngramSpark is supplying the barcode.")
        isbn_digits(isbn)

    palette = cfg["palette"]
    fonts, font_dir = register_fonts(cfg.get("fonts"))
    styles = {n: make_style(n, s, fonts, palette)
              for n, s in (cfg.get("styles") or {}).items()}

    # ---- output path -------------------------------------------------------
    out_cfg = cfg["output"]
    if out_path:
        out = os.path.abspath(out_path)
    else:
        rev = ""
        rev_file = bookpath(out_cfg.get("revision_file") or "")
        if rev_file and os.path.exists(rev_file):
            rev = open(rev_file, encoding="utf-8").read().strip()
        name = require(cfg, "output.name") + (f"-{rev}" if rev else "")
        out = os.path.join(bookpath(out_cfg["dir"]), name + ".pdf")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    workdir = os.path.dirname(out)

    # ---- front art ---------------------------------------------------------
    front_src = bookpath(require(cfg, "front.art"))
    if not os.path.exists(front_src):
        sys.exit(f"ERROR: front art not found: {front_src}")
    if cfg["front"].get("trim_white_strip"):
        stripped = os.path.join(workdir, "_front-bleed.png")
        front_src = trim_white_strip(front_src, stripped)
        if front_src == stripped:
            _TMPS.append(stripped)

    # ---- canvas ------------------------------------------------------------
    c = rl_canvas.Canvas(out, pagesize=(full_w * inch, full_h * inch))
    meta = cfg.get("metadata") or {}
    c.setTitle(meta.get("title", "") or "")
    c.setAuthor(meta.get("author", "") or "")

    # 1) paint the whole canvas, so any bleed gap matches the art and never
    #    flashes white at the trim line
    c.setFillColor(color_of(palette["bg"], palette))
    c.rect(0, 0, full_w * inch, full_h * inch, fill=1, stroke=0)

    back_x0 = BLEED
    spine_x0 = BLEED + TRIM_W
    front_x0 = BLEED + TRIM_W + spine

    # 2) FRONT art -- front trim plus the right/top/bottom bleed
    fit, art_stats = draw_cover_fit(c, front_src, front_x0, 0.0,
                                    TRIM_W + BLEED, full_h)
    _TMPS.append(fit)

    # 3) SPINE, rotated -90 so it reads top-to-bottom on a shelved book
    sp = cfg["spine"]
    spine_cx = (spine_x0 + spine / 2) * inch
    nudge = float(sp["baseline_nudge"])
    for text, size, face, col, ypos in (
        (sp.get("title"), sp["title_size"], "bold", sp["title_color"],
         full_h / 2 + float(sp["title_offset"])),
        (sp.get("author"), sp["author_size"], "italic", sp["author_color"],
         BLEED + SAFE + float(sp["author_offset"])),
    ):
        if not text:
            continue
        c.saveState()
        c.translate(spine_cx, ypos * inch)
        c.rotate(-90)
        c.setFillColor(color_of(col, palette))
        c.setFont(fonts[face], size)
        c.drawCentredString(0, nudge, text)
        c.restoreState()

    # 4) BACK panel copy
    back_left = (back_x0 + SAFE) * inch
    back_width = (TRIM_W - 2 * SAFE) * inch
    ab = cfg["author_block"]
    bc_cfg = cfg["barcode"]
    barcode_w = float(bc_cfg["width"]) if bc_cfg.get("enabled", True) else 0.0
    barcode_h = float(bc_cfg["height"]) if bc_cfg.get("enabled", True) else 0.0
    has_author_block = bool(ab.get("name") or ab.get("bio") or ab.get("photo"))
    author_h = float(ab["height"]) if has_author_block else 0.0

    flow = []
    for i, blk in enumerate(cfg["back"]["blocks"]):
        style_name = blk.get("style")
        if style_name not in styles:
            sys.exit(f"ERROR: back.blocks[{i}] uses style '{style_name}', which is "
                     f"not defined under styles: {sorted(styles)}")
        flow.append(Paragraph(blk.get("text", ""), styles[style_name]))
    if flow:
        frame_bottom = (BLEED + SAFE + max(barcode_h, author_h)
                        + float(cfg["back"]["frame_gap"])) * inch
        frame_top = (full_h - BLEED - SAFE) * inch
        leftover = Frame(back_left, frame_bottom, back_width, frame_top - frame_bottom,
                         leftPadding=0, rightPadding=0, topPadding=0,
                         bottomPadding=0, showBoundary=0)
        leftover.addFromList(flow, c)
        if flow:
            print(f"  WARNING: {len(flow)} back-cover block(s) did not fit and were "
                  "dropped. Shorten the copy or reduce the type size.", file=sys.stderr)

    # 5) author block, bottom-left of the back panel
    if has_author_block:
        text_left, text_w = back_left, back_width - (barcode_w + 0.2) * inch
        if ab.get("photo"):
            photo = bookpath(ab["photo"])
            if os.path.exists(photo):
                ph = float(ab["photo_size"])
                px, py = back_left, (BLEED + SAFE) * inch
                c.drawImage(photo, px, py, ph * inch, ph * inch, mask=None)
                # hairline keeps the photo from floating on a dark panel
                c.setStrokeColor(color_of(palette["secondary"], palette))
                c.setLineWidth(0.5)
                c.rect(px, py, ph * inch, ph * inch, fill=0, stroke=1)
                gap = float(ab["gap"])
                text_left = px + (ph + gap) * inch
                text_w -= (ph + gap) * inch
            else:
                print(f"  WARNING: author photo not found, skipping: {photo}",
                      file=sys.stderr)
        parts = []
        if ab.get("name"):
            parts.append(Paragraph(ab["name"], make_style(
                "ab_name", {"font": "bold", "size": ab["name_size"], "leading": 12,
                            "color": ab["name_color"], "space_after": 3}, fonts, palette)))
        if ab.get("bio"):
            parts.append(Paragraph(ab["bio"], make_style(
                "ab_bio", {"font": "regular", "size": ab["bio_size"], "leading": 10.5,
                           "color": ab["bio_color"], "space_after": 0}, fonts, palette)))
        if parts:
            Frame(text_left, (BLEED + SAFE) * inch, text_w, author_h * inch,
                  leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0,
                  showBoundary=0).addFromList(parts, c)

    # 6) EAN-13, bottom-right of the back panel. No price add-on -- IngramSpark
    #    sets price per market, and a baked-in price is a reprint to change.
    if bc_cfg.get("enabled", True):
        bx = (spine_x0 - SAFE - barcode_w) * inch
        by = (BLEED + SAFE) * inch
        c.setFillColor(Color(1, 1, 1))
        c.rect(bx, by, barcode_w * inch, barcode_h * inch, fill=1, stroke=0)
        png = render_ean13(isbn, workdir)
        if png:
            pad_x, pad_y = float(bc_cfg["pad_x"]) * inch, float(bc_cfg["pad_y"]) * inch
            c.drawImage(png, bx + pad_x, by + pad_y,
                        barcode_w * inch - 2 * pad_x, barcode_h * inch - 2 * pad_y,
                        preserveAspectRatio=True, anchor="c", mask=None)
            os.remove(png)
        else:
            print("  WARNING: python-barcode not installed -- drawing a placeholder "
                  "box, NOT a scannable barcode. Do not upload this.", file=sys.stderr)
            c.setFillColor(Color(0.45, 0.45, 0.45))
            c.setFont(fonts["regular"], 7)
            c.drawCentredString(bx + barcode_w * inch / 2,
                                by + barcode_h * inch / 2 - 3, f"ISBN {isbn}")

    c.showPage()
    c.save()
    _cleanup_tmps()

    # ---- report ------------------------------------------------------------
    print(f"wrote {out}")
    print(f"  spine    {spine:.4f}\"  = {pages} pp x {factor} ({stock_label})")
    print(f"  canvas   {full_w:.3f}\" x {full_h:.3f}\"  "
          f"(trim {TRIM_W}x{TRIM_H}, bleed {BLEED}, safe {SAFE})")
    print(f"  fonts    {font_dir}")
    src_w, src_h = art_stats["source_px"]
    crop_w, crop_h = art_stats["cropped_px"]
    print(f"  art      {src_w}x{src_h}px -> crop {crop_w}x{crop_h}px "
          f"(lost {art_stats['lost_w_pct']}% w, {art_stats['lost_h_pct']}% h)")
    ppi = art_stats["effective_ppi"]
    flag = "OK" if ppi >= 300 else "UNDER 300 -- will print soft"
    print(f"  art ppi  {ppi} effective across the {TRIM_W + BLEED}\" front panel [{flag}]")
    if ppi < 300:
        need_w = int(round(300 * (TRIM_W + BLEED)))
        need_h = int(round(300 * full_h))
        print(f"           supply art at >= {need_w}x{need_h}px, or accept soft print",
              file=sys.stderr)
    if max(art_stats["lost_w_pct"], art_stats["lost_h_pct"]) > 15:
        print("           NOTE: heavy center-crop. Check nothing important "
              "(title, byline) fell off the edge.", file=sys.stderr)
    print("  next     bash tools/make_noicc.sh cmyk \\\n"
          f"             '{out}' \\\n"
          f"             '{out[:-4]}-CMYK-noicc.pdf'")
    print("           python3 tools/check_upload_pdf.py cover "
          f"'{out[:-4]}-CMYK-noicc.pdf'")
    return out


def main():
    ap = argparse.ArgumentParser(
        description="Compose a print-ready cover wrap from delivery/cover.yaml.")
    ap.add_argument("book_dir", help="path to the book folder, e.g. books/the-gift")
    ap.add_argument("--init", action="store_true",
                    help="ask for the specs (trim, stock, page count, ISBN, art) "
                         "and write the cover config")
    ap.add_argument("--config", help="cover config (default: <book>/delivery/cover.yaml)")
    ap.add_argument("--out", help="output PDF (default: from output.name + REVISION)")
    ap.add_argument("--build", action="store_true",
                    help="with --init, build the wrap straight after writing the config")
    args = ap.parse_args()
    if args.init:
        init_config(args.book_dir, args.config)
        if not args.build:
            return
    build(args.book_dir, args.config, args.out)


if __name__ == "__main__":
    main()
