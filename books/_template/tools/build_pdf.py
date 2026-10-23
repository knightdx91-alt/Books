#!/usr/bin/env python3
"""
Build a 6x9 reading-copy PDF of this book from manuscript/chapters/chapter-N.md (per-book copy,
seeded from books/_template). The title comes from STATE.yaml (`book: title:`).

Usage: python3 tools/build_pdf.py            # every finished chapter
       python3 tools/build_pdf.py --upto 25   # chapters 1..25 only

Output: delivery/<Title>-reading-copy.pdf
Fonts: Crimson Pro (embedded). Body justified, first-line indent, no indent on a chapter's first
paragraph or after a scene break; "####" datelines centred in italics; HTML comments (scene budgets,
pass logs) are stripped. This is a reading copy, not the IngramSpark interior (no PDF/X, no CMYK pass).
"""
import argparse, glob, html, os, re
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph,
                                Spacer, PageBreak, NextPageTemplate)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def read_title():
    try:
        for line in open(os.path.join(ROOT, "STATE.yaml"), encoding="utf-8"):
            m = re.match(r'\s*title:\s*"([^"]*)"', line) or re.match(r"\s*title:\s*([^#]*?)\s*(?:#.*)?$", line)
            if m and m.group(1) and "<" not in m.group(1):
                return m.group(1)
    except OSError:
        pass
    return os.path.basename(ROOT).replace("-", " ").title()


TITLE = read_title()
OUT = os.path.join(ROOT, "delivery", re.sub(r"[^A-Za-z0-9]+", "-", TITLE).strip("-") + "-reading-copy.pdf")

FONT_DIR = "/mnt/skills/examples/canvas-design/canvas-fonts"
pdfmetrics.registerFont(TTFont("Crimson", f"{FONT_DIR}/CrimsonPro-Regular.ttf"))
pdfmetrics.registerFont(TTFont("Crimson-It", f"{FONT_DIR}/CrimsonPro-Italic.ttf"))
pdfmetrics.registerFont(TTFont("Crimson-Bd", f"{FONT_DIR}/CrimsonPro-Bold.ttf"))
pdfmetrics.registerFontFamily("Crimson", normal="Crimson", bold="Crimson-Bd",
                              italic="Crimson-It", boldItalic="Crimson-Bd")
# Keep reportlab's default Helvetica slot from pulling in an unembedded base-14 font.
pdfmetrics.registerFont(TTFont("Helvetica", f"{FONT_DIR}/CrimsonPro-Regular.ttf"))

TRIM_W, TRIM_H = 6 * inch, 9 * inch
M_SIDE, M_TOP, M_BOT = 0.75 * inch, 0.75 * inch, 0.75 * inch

body = ParagraphStyle("body", fontName="Crimson", fontSize=12, leading=16.5,
                      alignment=TA_JUSTIFY, firstLineIndent=18,
                      allowWidows=0, allowOrphans=0)
body_first = ParagraphStyle("body_first", parent=body, firstLineIndent=0)
scene = ParagraphStyle("scene", parent=body, alignment=TA_CENTER,
                       firstLineIndent=0, spaceBefore=8, spaceAfter=8)
ch_num = ParagraphStyle("ch_num", fontName="Crimson", fontSize=13, leading=18,
                        alignment=TA_CENTER, spaceAfter=6, keepWithNext=1)
ch_title = ParagraphStyle("ch_title", fontName="Crimson-Bd", fontSize=20, leading=26,
                          alignment=TA_CENTER, spaceAfter=10, keepWithNext=1)
dateline = ParagraphStyle("dateline", fontName="Crimson-It", fontSize=11.5, leading=16,
                          alignment=TA_CENTER, spaceAfter=24, keepWithNext=1)
book_title = ParagraphStyle("book_title", fontName="Crimson-Bd", fontSize=40,
                            leading=48, alignment=TA_CENTER)
subtitle = ParagraphStyle("subtitle", fontName="Crimson-It", fontSize=13, leading=18,
                          alignment=TA_CENTER, spaceBefore=18)
toc_head = ParagraphStyle("toc_head", parent=ch_title, spaceAfter=20)
toc_line = ParagraphStyle("toc_line", fontName="Crimson", fontSize=11.5, leading=17,
                          alignment=TA_CENTER)


def smart(text):
    t = re.sub(r'(^|[\s(\[—–-])"', "\\1“", text)
    t = t.replace('"', "”")
    t = re.sub(r"(^|[\s(\[—–-])'(?=\w)", "\\1‘", t)
    return t.replace("'", "’")


def inline(text):
    t = html.escape(smart(text), quote=False)
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
    t = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<i>\1</i>", t)
    t = re.sub(r"(?<!\w)_(?!\s)(.+?)(?<!\s)_(?!\w)", r"<i>\1</i>", t)
    return t


def footer(canvas, doc):
    canvas.saveState()
    canvas.setFont("Crimson", 10)
    canvas.drawCentredString(TRIM_W / 2, 0.45 * inch, str(doc.page))
    canvas.restoreState()


def load(path):
    text = re.sub(r"<!--.*?-->", "", open(path, encoding="utf-8").read(), flags=re.S)
    lines = text.splitlines()
    head = next(l for l in lines if l.startswith("# "))[2:].strip()
    num, _, title = head.partition(":")
    date, paras = None, []
    for l in lines:
        s = l.strip()
        if not s or s.startswith("# "):
            continue
        if s.startswith("#"):
            date = s.lstrip("#").strip()
            continue
        paras.append(s)
    return num.strip(), title.strip(), date, paras


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--upto", type=int, default=None)
    args = ap.parse_args()
    files = glob.glob(os.path.join(ROOT, "manuscript", "chapters", "chapter-*.md"))
    nums = sorted(int(m.group(1)) for f in files
                  if (m := re.fullmatch(r"chapter-(\d+)\.md", os.path.basename(f))))
    if args.upto:
        nums = [n for n in nums if n <= args.upto]
    chapters = [load(os.path.join(ROOT, "manuscript", "chapters", f"chapter-{n}.md")) for n in nums]

    story = [Spacer(1, 2.4 * inch), Paragraph(inline(TITLE), book_title),
             Paragraph(f"Reading copy · Chapters 1–{nums[-1]}", subtitle),
             NextPageTemplate("body"), PageBreak(),
             Paragraph("Contents", toc_head)]
    for num, title, _, _ in chapters:
        story.append(Paragraph(inline(f"{num}: {title}" if title else num), toc_line))
    for num, title, date, paras in chapters:
        story += [PageBreak(), Spacer(1, 1.2 * inch),
                  Paragraph(inline(num), ch_num), Paragraph(inline(title), ch_title)]
        story.append(Paragraph(inline(date), dateline) if date else Spacer(1, 20))
        first = True
        for p in paras:
            if re.fullmatch(r"(-{3,}|\*{3,}|\* \* \*)", p):
                story.append(Paragraph("*&nbsp;&nbsp;&nbsp;*&nbsp;&nbsp;&nbsp;*", scene))
                first = True
                continue
            story.append(Paragraph(inline(p), body_first if first else body))
            first = False

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    doc = BaseDocTemplate(OUT, pagesize=(TRIM_W, TRIM_H), title=TITLE,
                          leftMargin=M_SIDE, rightMargin=M_SIDE,
                          topMargin=M_TOP, bottomMargin=M_BOT)
    frame = Frame(M_SIDE, M_BOT, TRIM_W - 2 * M_SIDE, TRIM_H - M_TOP - M_BOT, id="f")
    doc.addPageTemplates([PageTemplate("front", [frame]),
                          PageTemplate("body", [frame], onPage=footer)])
    doc.build(story)
    print(f"wrote {OUT} ({doc.page} pages)")


if __name__ == "__main__":
    main()
