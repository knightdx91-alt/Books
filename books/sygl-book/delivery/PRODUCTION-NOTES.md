# Sygl — Production Notes (r1)

Status: **interior and EPUB built and checked; not upload-ready.** The 3 ISBNs, the cover art and
the hardcover template are still missing (see "Still missing" below). Pen name: **Søren Stromberg**.

## Specs (author's choices)

| | |
|---|---|
| Trim | 5 × 8 in, exact trim, no bleed (text-only interior) |
| Interior | black & white, **cream** paper (IngramSpark cream 50#) |
| Editions | paperback (perfect bound) and hardcover (case laminate), sharing **one** interior PDF, plus the EPUB |
| Page count | **392** physical pages (even): 4 front-matter pages + 388 body pages incl. blanks |
| Revision | r1 |

## Single source of truth

`delivery/ebook.yaml` holds title, author, year, revision, all three ISBNs, trim, margins and paper
stock. `tools/make_epub.py` reads its top-level keys; the book's own tools also read the `print:`
block. **To set the author name or an ISBN, edit it once there and run the build below.** The ISBNs
are still the placeholders `PRINT-ISBN-PAPERBACK`, `PRINT-ISBN-HARDCOVER` and `EBOOK-ISBN`. The
ebook ISBN is in two keys, `isbn` (package identifier) and `isbn_hyphen` (copyright page), and the
print ISBNs appear in both `print:` and the `copyright_extra` line, so fill in every one.

## Build (from the repo root)

```bash
python3 books/sygl-book/tools/assemble_manuscript.py      # chapters -> manuscript/full-manuscript-r1.md (generated, never hand-edit)
python3 books/sygl-book/tools/build_interior.py           # -> delivery/production/Sygl-5x8-interior-r1.pdf
bash tools/make_noicc.sh gray books/sygl-book/delivery/production/Sygl-5x8-interior-r1.pdf \
                              books/sygl-book/delivery/production/Sygl-5x8-interior-r1-GRAY-noicc.pdf
python3 tools/check_upload_pdf.py interior books/sygl-book/delivery/production/Sygl-5x8-interior-r1-GRAY-noicc.pdf
python3 books/sygl-book/tools/make_placeholder_cover.py   # only until real art exists
python3 tools/make_epub.py books/sygl-book                # -> delivery/ebook/Sygl.epub
```

The chapter files are read-only inputs. The assembler converts straight quotes to curly quotes and
"..." to an ellipsis character for print and ebook. The chapters themselves are not changed.

## Interior (`delivery/production/`)

| file | what it is |
|---|---|
| `Sygl-5x8-interior-r1.pdf` | the build (K-only black text, ToUnicode intact, searchable) |
| `Sygl-5x8-interior-r1-GRAY-noicc.pdf` | **the upload copy**: DeviceGray, no ICC, used for BOTH paperback and hardcover |

- 360 × 576 pt (5 × 8 in) Media/Trim box. Crimson Pro Regular, Italic and Bold are fully embedded
  TrueType subsets. No base-14 font: the `/Helvetica` slot is re-pointed, as in the Saeren builder.
- Mirrored margins: inside 0.80", outside 0.55", top 0.70", bottom 0.70". The script checked every
  page and none has text inside the gutter.
- Body: 11.5/15 pt, justified, en_US hyphenation, 15 pt first-line indent. No indent on the first
  paragraph of a chapter or after a scene break (`* * *`). Widows and orphans are disallowed, so
  some pages end a few lines short when a short paragraph moves whole. That is expected.
- All 30 chapters open on a recto (physical pages 5, 17, 29 … 385), sunk about a third of the way
  down. Blank versos are inserted where needed (18 blank pages, including a trailing pad to make the
  count even).
- Folios are centred in the footer, numbered from 1 at Chapter One. There are none on front matter,
  chapter openers or blanks. Running heads are the author on versos and the title on rectos, with
  the same suppression.
- Front matter: p1 half-title, p2 blank, p3 title page (Sygl / Søren Stromberg), p4 copyright
  (© 2026 Søren Stromberg; all rights reserved; work-of-fiction notice; "All characters in this book
  are 18 years of age or older."; paperback, hardcover and ebook ISBN lines; First Edition 2026).
  There is no TOC in print.
- `check_upload_pdf.py interior` on the GRAY-noicc file: **OK, DeviceGray, no colour profile.**
- Known limitation (PUBLISHING.md): the Ghostscript gray pass drops ToUnicode. Non-ASCII
  characters (ø, ©, curly quotes) therefore do not extract as text from the upload copy; they
  extract as "S ren". **Printing is unaffected:** the rendered upload file shows "Søren
  Stromberg", "SØREN STROMBERG", © and the curly quotes correctly. Tested in Ghostscript 10.02.1:
  neither interpreter setting keeps ToUnicode. Use the RGB build when you need searchable text.

## Spine and cover geometry

**Paperback**, cream 50#, 0.0025"/page (`tools/compose_wrap.py` PAPER_STOCKS `cream50`):

| | |
|---|---|
| spine | 392 × 0.0025 = **0.980 in** |
| full wrap (with 0.125" bleed) | 2 × 5 + 0.980 + 2 × 0.125 = **11.230 × 8.250 in** |
| each panel incl. outer bleed | 5.125 × 8.25 in. Front art at 300 ppi needs ≥ 1538 × 2475 px |

Re-check the 0.980" against IngramSpark's own spine calculator for 5 × 8 / cream / 392 pp before
building the wrap. The spine is the one dimension a reprint cannot fix. If the interior is re-cut,
the page count and therefore the spine change. Build the wrap with `python3 tools/compose_wrap.py
books/sygl-book --init` (set trim 5 × 8, stock cream50, pages 392 and the PAPERBACK ISBN). The
template `cover.yaml` defaults to 6 × 9, so the trim must be changed.

**Hardcover (case laminate):** do **not** derive it from the paperback numbers. A case wrap has
board, hinge and turn-in allowances, and its spine differs. Download the template from
IngramSpark's cover template generator, which needs the **hardcover ISBN**, trim 5 × 8, cream paper,
case laminate and 392 pages, and build the wrap onto that template. The current
`compose_wrap.py` produces paperback geometry only.

**Check before setup:** confirm that 5 × 8 is offered for *case laminate* in IngramSpark's
trim-size matrix. IngramSpark lists 5 × 8 for **jacketed** case laminate, but the size could not be
confirmed for plain case laminate. If it isn't offered, the options are jacketed case at 5 × 8 or a
different hardcover trim. A different trim needs its own interior, so the shared-interior plan
would no longer hold.

## EPUB (`delivery/ebook/Sygl.epub`)

- Built by `tools/make_epub.py books/sygl-book` from `manuscript/full-manuscript-r1.md`. It
  contains 30 chapters ("Chapter One" … "Chapter Twenty-One" … "Chapter Thirty").
- Copyright page: © 2026 Søren Stromberg, all rights reserved, fiction notice, the 18+ line, the
  paperback and hardcover ISBN lines, "First Edition 2026 · Ebook Edition", and the ebook ISBN.
- **EPUBCheck 5.3.0: 0 fatals / 0 errors / 0 warnings.** Structure: mimetype is first and stored
  uncompressed; `nav.xhtml` and `toc.ncx` are both present with 30 chapter entries each; all XML
  parses; `dc:creator` is "Søren Stromberg".
- The package identifier is currently `urn:isbn:EBOOK-ISBN`, and `make_epub.py` warns about it.
  **Rebuild after the ebook ISBN is set.**
- The cover is `delivery/cover/ebook-cover-PLACEHOLDER.jpg` (1600 × 2263, generated, marked "not
  for release"). Replace it with the real front cover JPG (RGB, ≥ 1600 px short side, ratio ~1.414),
  point `cover:` at it, and rebuild. The same JPG is the standalone ebook-listing image.

## Upload checklist (IngramSpark)

- [ ] Fill in the 3 ISBNs in `delivery/ebook.yaml`, then rerun the whole build (the page count
      should stay 392; confirm it).
- [ ] Paperback interior and hardcover interior: upload the **same** `Sygl-5x8-interior-r1-GRAY-noicc.pdf`.
      Run `check_upload_pdf.py interior` on the exact file being uploaded.
- [ ] Paperback cover: CMYK no-ICC wrap at 11.23 × 8.25 in, EAN-13 of the **paperback** ISBN, no
      price add-on; choose "my cover already includes a barcode".
- [ ] Hardcover cover: built on IngramSpark's generated case-laminate template, EAN-13 of the
      **hardcover** ISBN.
- [ ] Ebook: `Sygl.epub` carrying the **ebook** ISBN, plus the front-cover JPG. Enter the print
      page count (392) as the nominal ebook page count.
- [ ] Paper: **cream**, B&W, on both print formats. Recheck the spine in IngramSpark's calculator.
- [ ] Author field "Søren Stromberg" with the ø on every record, matching the title page and cover.
      Type the title once.
- [ ] Order a printed proof of each binding: solid black text, nothing in the gutter, spine text
      centred.
- [ ] When final, add Sygl to `BOOKS` in `tools/collect_completed.py` and run it. Note that the
      script reads a `REVISION` file; this book keeps its revision in `ebook.yaml`, so create
      `REVISION` (containing `r1`) at that point or extend the script.

## Still missing

1. **3 ISBNs:** paperback, hardcover, ebook (placeholders in config).
2. **Cover art:** front art for the ebook JPG and the paperback wrap, plus back-cover copy.
3. **Hardcover cover template** from IngramSpark (needs the hardcover ISBN and 392 pp), and
   confirmation that 5 × 8 is available as plain case laminate.
4. The closing line is marked PROVISIONAL in STATE.yaml. If the text changes, re-assemble and
   rebuild, and recheck the page count and spine.

## STALE (2026-10-22)
The 5x8 paperback interior and wrap name ISBN 979-8-1829-5940-7 as the paperback, but the author assigned that ISBN to the 6x9 hardcover in IngramSpark. Do NOT upload the 5x8 files until the paperback has its own ISBN and they are rebuilt.
