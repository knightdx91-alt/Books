#!/usr/bin/env python3
"""
Compose the full print cover WRAP (back + spine + front) for a Saeren book.

Layout (6x9 trim, full bleed 0.125"):
  [left bleed][ BACK 6" ][ SPINE ][ FRONT 6" ][right bleed]   x  [top/bottom bleed]

  python3 tools/compose_wrap.py book-2
  python3 tools/compose_wrap.py book-3

Spine width = interior page count x paper factor. PPI_FACTOR below is set to
IngramSpark **white 50#**, which is what the accepted Book One and Book Two
wraps were built at (Book One 294pp -> 0.660", Book Two 306pp -> 0.687").
If the stock ordered is actually cream 50#, set PPI_FACTOR = 0.0025 and rebuild
— and always re-check the final number against IngramSpark's spine calculator
before ordering, because the spine is the one dimension a reprint can't fix.

Page counts come from tools/build_pdf.py's reported TOTAL PHYSICAL PAGE COUNT;
bump PAGES here whenever the interior is re-cut at a different length.

Output: <book>/delivery/cover/Saeren-Book-<N>-FULL-WRAP-<rev>.pdf (RGB proof).
Convert to PDF/X-1a with the book's own tools/make_pdfx.sh, passing in/out paths.
"""
import os, sys
from PIL import Image
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.lib.colors import Color, HexColor
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph, Frame

SAEREN = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# --- dimensions ---
TRIM_W, TRIM_H, BLEED = 6.0, 9.0, 0.125
PPI_FACTOR = 0.002252          # IngramSpark white 50#  (cream 50# = 0.0025)
SAFE = 0.375                   # keep text this far inside the trim

# --- palette (sampled from the Book One / Book Two covers) ---
BG = HexColor("#0A0A0C")
SILVER = HexColor("#DCE2EC")
GREY = HexColor("#AEB8C6")
EMBER = HexColor("#C9A25A")

AUTHOR = "Post Peleos"
# Author photo for the back panel. Colour here (covers print CMYK); the interiors
# use the grayscale twin because they upload as DeviceGray.
AUTHOR_PHOTO = os.path.join(os.path.dirname(SAEREN), "_assets", "author-photo.jpg")
AUTHOR_BIO = ("Post Peleos writes character-driven fantasy about quiet people "
              "in loud worlds. <i>The Saeren Chronicles</i> is his debut series.")

BOOKS = {
    "book-1": dict(
        slug="saeren-chronicles",
        out_name="Saeren-Book-One-FULL-WRAP",
        front="delivery/cover/hazel-academy-front-cover.png",
        book_line="BOOK ONE",
        title="HAZEL ACADEMY",
        spine_title="HAZEL ACADEMY",
        pages=294,                       # interior r17
        isbn="979-8-2409-9043-4",
        hook="The last ordinary morning of Viridia&#8217;s life smelled like scorched "
             "bread and her mother&#8217;s tea.",
        paras=[
            "Three days later she walks through the gates of Hazel &#8212; the most "
            "prestigious school for mages in the country &#8212; orphaned, silent, and "
            "certain of one thing: no one is ever going to see her grieve.",
            "In a world that long ago tore its magic cleanly in two &#8212; light from "
            "dark, safe from forbidden &#8212; Viridia was born <i>whole.</i> Both "
            "halves. The one thing Hazel was built to make certain could never exist. "
            "To be known is to be killed. So she makes herself small, learns in secret "
            "what she truly is, and lets in one person: Alice, the only girl at Hazel "
            "who sees the drowning underneath the quiet.",
            "Then the people who fear what this school hides decide to burn it down "
            "&#8212; and a girl who survives by disappearing must choose between the "
            "many she can save and the one she cannot bear to lose.",
        ],
        closing="A quiet, lyrical fantasy about grief, found family, and a girl who "
                "refuses to be made small &#8212; the first book of <i>The Saeren "
                "Chronicles.</i>",
    ),
    "book-2": dict(
        slug="saeren-chronicles-book-2",
        out_name="Saeren-Book-Two-FULL-WRAP",
        front="delivery/cover/the-resistance-front-cover-fractured-light.png",
        book_line="BOOK TWO",
        title="THE RESISTANCE",
        spine_title="THE RESISTANCE",
        pages=308,                       # interior r11
        isbn="979-8-2409-9382-4",
        hook="The war that burned Hazel to the ground has finally found her.",
        paras=[
            "Viridia escapes to a hidden resistance camp carrying a secret she has never said "
            "aloud: she was born <i>whole</i> &#8212; both halves of a magic her world tore in "
            "two six hundred years ago &#8212; and she alone could mend it. For everyone. All "
            "at once. Whether they consent or not.",
            "But Alice, the only person who ever truly saw her, is alive and held in the heart "
            "of the capital that wants Viridia dead. A war she cannot stop is closing in. And "
            "the grieving young leader at her side is marching toward his own end.",
            "She will try every bloodless road first. When the armies finally meet, the cost of "
            "doing the impossible will be measured in the people she loves.",
        ],
        closing="The second book of <i>The Saeren Chronicles</i> &#8212; a quiet, devastating "
                "fantasy about grief, found family, consent, and the weight of being the only "
                "one who can.",
    ),
    "book-3": dict(
        slug="saeren-chronicles-book-3",
        out_name="Saeren-Book-Three-FULL-WRAP",
        front="delivery/cover/the-weight-of-the-source-front-cover-eclipse.png",
        book_line="BOOK THREE",
        title="THE WEIGHT OF THE SOURCE",
        spine_title="THE WEIGHT OF THE SOURCE",
        pages=324,                       # interior r8
        isbn="979-8-1827-2380-0",
        hook="She put the world back together. Now she has to carry it.",
        paras=[
            "Months after the severing was mended, the old order is ash and every living soul "
            "carries both halves of the gift &#8212; and Viridia feels all of them. She is the "
            "source now: the still point a remade world turns on, and the one person who cannot "
            "put it down.",
            "Then the portals begin to open, and the things that come through do not attack. "
            "They come toward her. Whatever is loose in the world is being pulled to the source "
            "&#8212; and the source is a girl who has already spent almost everything she had.",
            "In saving her world she made the thing that will unmake it. What she does with "
            "that power &#8212; and what she refuses to become to use it &#8212; is the last "
            "question the Saeren Chronicles will ask of her.",
        ],
        closing="The conclusion of <i>The Saeren Chronicles</i> &#8212; a fantasy about power "
                "held without cruelty, the people who keep you human, and the weight of being "
                "what everyone else needs.",
    ),
}

FONT_DIR = "/mnt/skills/examples/canvas-design/canvas-fonts"
pdfmetrics.registerFont(TTFont("Plex", f"{FONT_DIR}/IBMPlexSerif-Regular.ttf"))
pdfmetrics.registerFont(TTFont("Plex-It", f"{FONT_DIR}/IBMPlexSerif-Italic.ttf"))
pdfmetrics.registerFont(TTFont("Plex-Bd", f"{FONT_DIR}/IBMPlexSerif-Bold.ttf"))
pdfmetrics.registerFont(TTFont("Plex-BdIt", f"{FONT_DIR}/IBMPlexSerif-BoldItalic.ttf"))
# reportlab declares a default base-14 Helvetica slot even when unused; that font is
# NOT embedded and fails IngramSpark preflight. Point the name at an embedded TTF.
pdfmetrics.registerFont(TTFont("Helvetica", f"{FONT_DIR}/IBMPlexSerif-Regular.ttf"))


def render_ean13(isbn, root):
    """Render the print ISBN as a real EAN-13 PNG. Returns a path, or None if
    python-barcode isn't installed (caller then falls back to a labelled box)."""
    try:
        from barcode import EAN13
        from barcode.writer import ImageWriter
    except ImportError:
        return None
    digits = "".join(ch for ch in isbn if ch.isdigit())[:12]
    base = os.path.join(root, "delivery", "cover", "_ean13")
    # EAN13 recomputes the check digit from the first 12 digits.
    EAN13(digits, writer=ImageWriter()).save(
        base, options={"module_height": 12.0, "quiet_zone": 2.0,
                       "font_size": 8, "text_distance": 3.0, "dpi": 600})
    return base + ".png"


def draw_cover_fit(c, img_path, x, y, w, h):
    """Place image to COVER the (x,y,w,h) rect in inches (scale-to-fill, center-crop)."""
    im = Image.open(img_path)
    iw, ih = im.size
    target, src = w / h, iw / ih
    if src > target:                       # image wider -> crop the sides
        new_w = int(ih * target)
        box = ((iw - new_w) // 2, 0, (iw - new_w) // 2 + new_w, ih)
    else:                                  # image taller -> crop top/bottom
        new_h = int(iw / target)
        box = (0, (ih - new_h) // 2, iw, (ih - new_h) // 2 + new_h)
    fit = img_path + ".fit.png"
    im.convert("RGB").crop(box).save(fit)
    c.drawImage(fit, x * inch, y * inch, w * inch, h * inch, mask=None)
    return fit


def main(key):
    cfg = BOOKS[key]
    root = os.path.join(SAEREN, cfg["slug"])
    rev = open(os.path.join(root, "REVISION"), encoding="utf-8").read().strip()
    out = os.path.join(root, "delivery", "cover", f'{cfg["out_name"]}-{rev}.pdf')
    front_src = os.path.join(root, cfg["front"])

    spine = cfg["pages"] * PPI_FACTOR
    full_w = 2 * TRIM_W + spine + 2 * BLEED
    full_h = TRIM_H + 2 * BLEED

    c = canvas.Canvas(out, pagesize=(full_w * inch, full_h * inch))

    # 1) whole canvas dark, so any bleed/gap matches the art
    c.setFillColor(BG)
    c.rect(0, 0, full_w * inch, full_h * inch, fill=1, stroke=0)

    back_x0, spine_x0 = BLEED, BLEED + TRIM_W
    front_x0 = BLEED + TRIM_W + spine

    # 2) FRONT art — covers the front trim plus the right/top/bottom bleed
    fit = draw_cover_fit(c, front_src, front_x0, 0.0, TRIM_W + BLEED, full_h)

    # 3) SPINE text, rotated to read top-to-bottom
    spine_cx = (spine_x0 + spine / 2) * inch
    vshift = 5                                   # nudge to the spine's optical center
    c.saveState()
    c.translate(spine_cx, (full_h / 2 + 1.5) * inch)
    c.rotate(-90)
    c.setFillColor(SILVER)
    c.setFont("Plex-Bd", 14)
    c.drawCentredString(0, vshift, cfg["spine_title"])
    c.restoreState()
    c.saveState()
    c.translate(spine_cx, (BLEED + SAFE + 0.55) * inch)
    c.rotate(-90)
    c.setFillColor(GREY)
    c.setFont("Plex-It", 11)
    c.drawCentredString(0, vshift, AUTHOR)
    c.restoreState()

    # 4) BACK panel copy
    back_left = (back_x0 + SAFE) * inch
    back_width = (TRIM_W - 2 * SAFE) * inch
    series = ParagraphStyle("series", fontName="Plex", fontSize=8.5, leading=13,
                            textColor=GREY, alignment=TA_CENTER, spaceAfter=2)
    booknum = ParagraphStyle("booknum", fontName="Plex", fontSize=7.5, leading=11,
                             textColor=GREY, alignment=TA_CENTER, spaceAfter=16)
    hook = ParagraphStyle("hook", fontName="Plex-BdIt", fontSize=12, leading=16,
                          textColor=SILVER, alignment=TA_CENTER, spaceAfter=14)
    para = ParagraphStyle("para", fontName="Plex", fontSize=10, leading=14.5,
                          textColor=GREY, alignment=TA_LEFT, spaceAfter=9)
    closing = ParagraphStyle("closing", fontName="Plex-It", fontSize=9.5, leading=13.5,
                             textColor=SILVER, alignment=TA_CENTER, spaceBefore=6)

    flow = [Paragraph("THE SAEREN CHRONICLES", series),
            Paragraph(cfg["book_line"], booknum),
            Paragraph(cfg["hook"], hook)]
    flow += [Paragraph(p, para) for p in cfg["paras"]]
    flow.append(Paragraph(cfg["closing"], closing))

    barcode_h, barcode_w = 1.1, 1.9
    author_block_h = 1.0
    frame_bottom = (BLEED + SAFE + max(barcode_h, author_block_h) + 0.28) * inch
    frame_top = (full_h - BLEED - SAFE) * inch
    Frame(back_left, frame_bottom, back_width, frame_top - frame_bottom,
          leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0,
          showBoundary=0).addFromList(flow, c)

    # 5) author block, bottom-left of the back panel: photo, then name + bio
    bio = ParagraphStyle("bio", fontName="Plex", fontSize=7.5, leading=10.5,
                         textColor=GREY, alignment=TA_LEFT)
    name = ParagraphStyle("name", fontName="Plex-Bd", fontSize=9, leading=12,
                          textColor=EMBER, alignment=TA_LEFT, spaceAfter=3)
    text_left, text_w = back_left, back_width - (barcode_w + 0.2) * inch
    if os.path.exists(AUTHOR_PHOTO):
        ph = photo_h = 1.0                       # inches, square
        px, py = back_left, (BLEED + SAFE) * inch
        c.drawImage(AUTHOR_PHOTO, px, py, ph * inch, photo_h * inch, mask=None)
        # hairline keeps the photo from floating on the dark panel
        c.setStrokeColor(GREY)
        c.setLineWidth(0.5)
        c.rect(px, py, ph * inch, photo_h * inch, fill=0, stroke=1)
        text_left = px + (ph + 0.15) * inch
        text_w -= (ph + 0.15) * inch
    Frame(text_left, (BLEED + SAFE) * inch, text_w,
          author_block_h * inch, leftPadding=0, rightPadding=0, topPadding=0,
          bottomPadding=0, showBoundary=0).addFromList(
              [Paragraph(AUTHOR.upper(), name), Paragraph(AUTHOR_BIO, bio)], c)

    # 6) EAN-13 barcode (white box + quiet zone), bottom-right of the back panel.
    #    No price add-on — IngramSpark sets price per market.
    bx = (spine_x0 - SAFE - barcode_w) * inch
    by = (BLEED + SAFE) * inch
    c.setFillColor(Color(1, 1, 1))
    c.rect(bx, by, barcode_w * inch, barcode_h * inch, fill=1, stroke=0)
    bc = render_ean13(cfg["isbn"], root)
    if bc:
        pad_x, pad_y = 0.13 * inch, 0.12 * inch
        c.drawImage(bc, bx + pad_x, by + pad_y,
                    barcode_w * inch - 2 * pad_x, barcode_h * inch - 2 * pad_y,
                    preserveAspectRatio=True, anchor="c", mask=None)
        os.remove(bc)
    else:
        c.setFillColor(Color(0.45, 0.45, 0.45))
        c.setFont("Plex", 7)
        c.drawCentredString(bx + barcode_w * inch / 2, by + barcode_h * inch / 2 - 3,
                            f'ISBN {cfg["isbn"]}')

    c.showPage()
    c.save()
    try:
        os.remove(fit)
    except OSError:
        pass
    print("wrote", out)
    print(f'spine = {spine:.3f}"  full canvas = {full_w:.3f}" x {full_h:.3f}"  '
          f'({cfg["pages"]}pp, white 50#)')


if __name__ == "__main__":
    key = sys.argv[1] if len(sys.argv) > 1 else ""
    if key not in BOOKS:
        sys.exit(f"usage: compose_wrap.py {{{'|'.join(BOOKS)}}}")
    main(key)
