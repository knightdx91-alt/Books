#!/usr/bin/env python3
"""Build Sygl's PRINT interior to IngramSpark specs (one PDF for paperback AND
hardcover/case laminate — same trim, same interior).

    python3 books/sygl-book/tools/assemble_manuscript.py   # first: chapters -> full-manuscript-<rev>.md
    python3 books/sygl-book/tools/build_interior.py
    bash tools/make_noicc.sh gray <out.pdf> <out-GRAY-noicc.pdf>   # the upload copy

Everything identifying (title, author, ISBNs, trim, margins, revision) comes from
delivery/ebook.yaml — change it there once and rebuild.

Specs
  Trim       exact, from config (5 x 8 in), no bleed (text-only interior).
  Margins    MIRRORED: inside (gutter) / outside / top / bottom from config.
             Recto = odd physical page, gutter on the LEFT; verso = even, gutter RIGHT.
  Fonts      Crimson Pro (Regular / Italic / Bold), fully embedded TrueType subsets.
             reportlab's default /Helvetica resource slot is re-pointed at Crimson
             Pro so no unembedded base-14 font is ever declared.
  Colour     text in K-only black (CMYK 0/0/0/100) -> pure DeviceGray 0 after the
             make_noicc.sh gray pass.
  Body       justified, en_US hyphenation (pyphen), first-line indent; no indent on a
             chapter's first paragraph or after a scene break; widows/orphans
             disallowed; scene-break ornament kept with the following text.
  Chapters   every chapter opens on a new RECTO, sunk ~1/3 down the page; a blank
             verso is inserted where needed.
  Folios     page numbers in the footer, body numbered from 1 at Chapter One; none on
             front matter, chapter openers or blank pages. Running heads: author on
             verso, title on recto (same suppression), if print.running_heads.
  Count      total physical page count forced EVEN (trailing blank) for binding.

Two passes: pass 1 lays out the book and records which pages are chapter openers
and blanks; pass 2 lays out identically and uses that map to decorate the pages.
"""
import html, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from production_common import BOOK, load_config, manuscript_path  # noqa: E402

REPO = os.path.dirname(os.path.dirname(BOOK))
sys.path.insert(0, os.path.join(REPO, "tools"))
import make_epub  # noqa: E402  (shared manuscript parser: CHAPTER <WORD> headings)

from reportlab.lib.units import inch
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import CMYKColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph,
                                Spacer, PageBreak)

CFG = load_config()
PRN = dict(CFG["print"])
# --edition NAME: overlay print.editions.NAME (e.g. the 6x9 hardcover) on the base print block.
if "--edition" in sys.argv:
    _ed = sys.argv[sys.argv.index("--edition") + 1]
    PRN.update(CFG["print"]["editions"][_ed])
AUTHOR, TITLE = CFG["author"], CFG["title"]

K_BLACK = CMYKColor(0, 0, 0, 1)

FONT_DIR = "/mnt/skills/examples/canvas-design/canvas-fonts"
pdfmetrics.registerFont(TTFont("Crimson", f"{FONT_DIR}/CrimsonPro-Regular.ttf"))
pdfmetrics.registerFont(TTFont("Crimson-It", f"{FONT_DIR}/CrimsonPro-Italic.ttf"))
pdfmetrics.registerFont(TTFont("Crimson-Bd", f"{FONT_DIR}/CrimsonPro-Bold.ttf"))
pdfmetrics.registerFontFamily("Crimson", normal="Crimson", bold="Crimson-Bd",
                              italic="Crimson-It", boldItalic="Crimson-Bd")
# The saeren trick: reportlab declares /Helvetica in shared resources even when
# unused; re-point the name at an embeddable TTF so preflight sees no base-14 font.
pdfmetrics.registerFont(TTFont("Helvetica", f"{FONT_DIR}/CrimsonPro-Regular.ttf"))

TRIM_W, TRIM_H = PRN["trim"]["width"] * inch, PRN["trim"]["height"] * inch
M = {k: v * inch for k, v in PRN["margins"].items()}
TEXT_W = TRIM_W - M["inside"] - M["outside"]
TEXT_H = TRIM_H - M["top"] - M["bottom"]

REV = CFG["revision"]
OUT = os.path.join(BOOK, "delivery", "production", f"{PRN['out_name']}-{REV}.pdf")

# ---------------------------------------------------------------- styles
body = ParagraphStyle("body", fontName="Crimson", fontSize=11.5, leading=15,
                      alignment=TA_JUSTIFY, firstLineIndent=15, textColor=K_BLACK,
                      allowWidows=0, allowOrphans=0,
                      hyphenationLang="en_US", embeddedHyphenation=1,
                      uriWasteReduce=0.3)
body_first = ParagraphStyle("body_first", parent=body, firstLineIndent=0)
scene = ParagraphStyle("scene", parent=body, alignment=TA_CENTER, firstLineIndent=0,
                       spaceBefore=7.5, spaceAfter=7.5, keepWithNext=1,
                       hyphenationLang="")
ch_num = ParagraphStyle("ch_num", fontName="Crimson", fontSize=10.5, leading=14,
                        alignment=TA_CENTER, spaceAfter=8, textColor=K_BLACK,
                        keepWithNext=1)
ch_title = ParagraphStyle("ch_title", fontName="Crimson-It", fontSize=18, leading=23,
                          alignment=TA_CENTER, spaceAfter=30, textColor=K_BLACK,
                          keepWithNext=1)
half = ParagraphStyle("half", fontName="Crimson", fontSize=20, leading=26,
                      alignment=TA_CENTER, textColor=K_BLACK)
t_main = ParagraphStyle("t_main", fontName="Crimson-Bd", fontSize=44, leading=52,
                        alignment=TA_CENTER, textColor=K_BLACK)
t_auth = ParagraphStyle("t_auth", fontName="Crimson", fontSize=15, leading=20,
                        alignment=TA_CENTER, textColor=K_BLACK)
cp = ParagraphStyle("cp", fontName="Crimson", fontSize=8.5, leading=11.5,
                    alignment=TA_CENTER, textColor=K_BLACK, spaceAfter=5.5)


def spaced(s):
    """Letterspaced caps for display lines (chapter numbers, running heads)."""
    return "&#8202;".join(html.escape(c) if c != " " else "&#160;&#160;" for c in s.upper())


def md_inline(t):
    t = html.escape(t, quote=False)
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
    t = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<i>\1</i>", t)
    return t


# ---------------------------------------------------------------- flow control
class Blank(Spacer):
    """A page intentionally left blank (no folio, no running head)."""
    def __init__(self):
        super().__init__(1, 1)


class RectoBreak(Spacer):
    """Marker: start the next element on a new RECTO (odd) page."""
    def __init__(self):
        super().__init__(0, 0)


class BookDoc(BaseDocTemplate):
    def __init__(self, *a, **k):
        super().__init__(*a, **k)
        self.openers, self.blanks, self.body_start = set(), set(), None

    def handle_flowable(self, flowables):
        f = flowables[0]
        if isinstance(f, RectoBreak):
            flowables.pop(0)
            fresh = self._curPageFlowableCount == 0      # already on an untouched page
            nxt = self.page if fresh else self.page + 1
            ins = [] if fresh else [PageBreak()]
            if nxt % 2 == 0:                              # would land on a verso
                ins += [Blank(), PageBreak()]
            flowables[0:0] = ins
            return
        super().handle_flowable(flowables)

    def handle_pageBegin(self):
        # Mirrored margins by parity, decided here rather than by template cycling
        # (PageBreak resets the cycle): the page about to begin is self.page + 1.
        self.pageTemplate = self.pageTemplates[0 if (self.page + 1) % 2 else 1]
        super().handle_pageBegin()

    def afterFlowable(self, f):
        if isinstance(f, Blank):
            self.blanks.add(self.page)
        elif getattr(getattr(f, "style", None), "name", "") == "ch_num":
            self.openers.add(self.page)
            if self.body_start is None:
                self.body_start = self.page


def frame_for(recto):
    left = M["inside"] if recto else M["outside"]
    return Frame(left, M["bottom"], TEXT_W, TEXT_H, id="r" if recto else "v",
                 leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)


# ---------------------------------------------------------------- story
def story_for(chapters, pad):
    s = []
    # p1 recto: half-title
    s += [Spacer(1, 2.1 * inch), Paragraph(html.escape(TITLE), half), PageBreak()]
    # p2 verso: "Also by" (config also_by_print), else blank
    if CFG.get("also_by_print"):
        ab_h = ParagraphStyle("ab_h", parent=cp, fontSize=9.5, leading=13, spaceBefore=4, spaceAfter=7)
        ab_i = ParagraphStyle("ab_i", parent=cp, fontName="Crimson-It", fontSize=10.5, leading=14, spaceAfter=2)
        ab_t = ParagraphStyle("ab_t", parent=cp, fontSize=9.5, leading=13, spaceAfter=2)
        s += [Spacer(1, 1.6 * inch)]
        for b in CFG["also_by_print"]:
            if b.get("gap"): s += [Spacer(1, 0.3 * inch)]
            elif "h" in b: s += [Paragraph(spaced(b["h"]), ab_h)]
            elif "i" in b: s += [Paragraph(html.escape(b["i"]), ab_i)]
            else: s += [Paragraph(html.escape(b["t"]), ab_t)]
        s += [PageBreak()]
    else:
        s += [Blank(), PageBreak()]
    # p3 recto: title page
    s += [Spacer(1, 1.5 * inch), Paragraph(html.escape(TITLE), t_main),
          Spacer(1, 1.9 * inch), Paragraph(html.escape(AUTHOR), t_auth)]
    if CFG.get("publisher") and CFG.get("publisher") != AUTHOR:   # imprint at the foot of the title page
        s += [Spacer(1, 1.6 * inch), Paragraph(html.escape(CFG["publisher"]).upper(), cp)]
    s += [PageBreak()]
    # p4 verso: copyright, set low on the page
    pi = PRN
    lines = [
        f"Copyright &#169; {CFG['year']} {html.escape(AUTHOR)}",
        "All rights reserved.",
        "No part of this book may be reproduced in any form or by any electronic or "
        "mechanical means, including information storage and retrieval systems, "
        "without written permission from the author, except for the use of brief "
        "quotations in a book review.",
        "This is a work of fiction. Names, characters, places, and incidents are "
        "products of the author&#8217;s imagination or are used fictitiously. Any "
        "resemblance to actual persons, living or dead, events, or locales is "
        "entirely coincidental.",
        "All characters in this book are 18 years of age or older.",
        "<br/>".join(
            [f"ISBN {html.escape(pi['isbn_paperback'])} (paperback)"]
            + ([f"ISBN {html.escape(pi['isbn_hardcover'])} (hardcover)"] if pi.get("isbn_hardcover") else [])
            + [f"ISBN {html.escape(CFG['isbn_hyphen'])} (ebook)"]),
        f"First Edition {CFG['year']}",
        html.escape(CFG.get("publisher") or AUTHOR),
    ]
    s += [Spacer(1, 2.35 * inch)] + [Paragraph(l, cp) for l in lines] + [PageBreak()]

    for n, title, text in chapters:
        s += [RectoBreak(), Spacer(1, 1.55 * inch),
              Paragraph(spaced(f"Chapter {make_epub.WORDTITLE.get(n, n)}"), ch_num),
              Paragraph(md_inline(title), ch_title)]
        first = True
        for kind, content in make_epub.paras(text):
            if kind == "scene":
                s.append(Paragraph("*&#160;&#160;&#160;*&#160;&#160;&#160;*", scene))
                first = True
            else:
                s.append(Paragraph(md_inline(content), body_first if first else body))
                first = False
    if pad:
        s += [PageBreak(), Blank()]
    return s


def build(chapters, pad=False, deco=None):
    def on_page(canvas, doc):
        canvas.saveState()
        canvas.setFont("Crimson", 9)                     # never leave Helvetica current
        p = doc.page
        if deco and p >= deco["body_start"] and p not in deco["openers"] \
                and p not in deco["blanks"]:
            recto = p % 2 == 1
            cx = (M["inside"] if recto else M["outside"]) + TEXT_W / 2
            canvas.setFillColor(K_BLACK)
            canvas.setFont("Crimson", 9.5)
            canvas.drawCentredString(cx, M["bottom"] - 0.32 * inch,
                                     str(p - deco["body_start"] + 1))
            if PRN.get("running_heads"):
                head = (TITLE if recto else AUTHOR).upper()
                cs = 1.6                                   # letterspacing, pt
                w = pdfmetrics.stringWidth(head, "Crimson", 8) + cs * (len(head) - 1)
                t = canvas.beginText(cx - w / 2, TRIM_H - M["top"] + 0.27 * inch)
                t.setFont("Crimson", 8)
                t.setCharSpace(cs)
                t.textOut(head)
                canvas.drawText(t)
        canvas.restoreState()

    doc = BookDoc(OUT, pagesize=(TRIM_W, TRIM_H), title=TITLE, author=AUTHOR,
                  subject=f"{TITLE} — print interior {REV}", creator="build_interior.py",
                  leftMargin=M["inside"], rightMargin=M["outside"],
                  topMargin=M["top"], bottomMargin=M["bottom"])
    doc.addPageTemplates([
        PageTemplate(id="recto", frames=[frame_for(True)], onPage=on_page),
        PageTemplate(id="verso", frames=[frame_for(False)], onPage=on_page),
    ])
    doc.build(story_for(chapters, pad))
    return doc


def main():
    src = manuscript_path(CFG)
    if not os.path.isfile(src):
        sys.exit(f"error: {src} not found — run tools/assemble_manuscript.py first")
    chapters = make_epub.parse(src)
    nums = [c[0] for c in chapters]
    if nums != list(range(1, len(nums) + 1)):
        sys.exit(f"error: chapter numbers not sequential: {nums}")
    os.makedirs(os.path.dirname(OUT), exist_ok=True)

    d1 = build(chapters)
    pad = d1.page % 2 == 1
    deco = dict(openers=d1.openers, blanks=d1.blanks | ({d1.page + 1} if pad else set()),
                body_start=d1.body_start)
    d2 = build(chapters, pad=pad, deco=deco)

    # Consistency checks between the passes and against the spec.
    assert d2.openers == d1.openers, "pass 2 layout drifted from pass 1"
    assert all(p % 2 == 1 for p in d2.openers), f"chapter on a verso: {sorted(d2.openers)}"
    assert d2.page % 2 == 0, "odd page count"
    assert len(d2.openers) == len(chapters)
    print(f"wrote {OUT}")
    print(f"chapters: {len(chapters)}  openers (physical, all recto): {sorted(d2.openers)}")
    print(f"blank pages: {sorted(d2.blanks)}")
    print(f"front matter: {d2.body_start - 1} pages; body numbered from physical page {d2.body_start}")
    print(f"TOTAL PHYSICAL PAGE COUNT (even): {d2.page}")


if __name__ == "__main__":
    main()
