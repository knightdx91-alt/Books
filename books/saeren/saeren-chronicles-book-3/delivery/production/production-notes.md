# Book Three — Production Notes

## Revision policy (same as Books One and Two)
`REVISION` at the book root is the single source of truth for the build tag.
**Bump it BEFORE rebuilding**, then rebuild; prior builds are kept as history and
the new build carries the new tag. No manuscript/PDF update ships without a bump.

## Build pipeline
```
cd books/saeren/saeren-chronicles-book-3
python3 tools/assemble_manuscript.py       # -> manuscript/full-manuscript-<rev>.md
python3 tools/build_pdf.py                 # -> delivery/production/...-interior-<rev>.pdf  (RGB)
bash    tools/make_pdfx.sh                 # -> ...-interior-<rev>-PDFX1a.pdf  (CMYK / PDF-X-1a)
python3 ../tools/compose_wrap.py book-3    # -> delivery/cover/Saeren-Book-Three-FULL-WRAP-<rev>.pdf
bash    tools/make_pdfx.sh <wrap.pdf> <wrap-PDFX1a.pdf>
python3 ../make_epub.py book-3             # -> delivery/ebook/...epub
```

## Spec (mirrors Books One and Two)
- Trim 6" x 9"; margins side 0.75", top 0.75", bottom 0.70" (gutter-safe to ~500pp).
- IBM Plex Serif, fully embedded; body 11/15.5pt justified, 16pt indent.
- Chapter-title running heads; page numbers start at 1 on Chapter One.
- Even physical page count (auto-padded) for perfect binding.
- Body text is pure K-only black, so the CMYK pass gives clean single-plate black.

## Front-matter fields
They are constants at the top of `tools/build_pdf.py` — `ISBN`, `IMPRINT`,
`DEDICATION`, `ACKNOWLEDGMENTS`. An empty string omits that line or page rather
than printing a placeholder, so a production file never ships with `[Dedication]`
on a page. **`DEDICATION` is currently empty** (Books One and Two each have one;
Book Three was never given a line). Setting it adds a recto + blank verso, i.e.
**+2 pages**, which changes the spine — re-cut the cover if you fill it in.

## Cover wrap
`../tools/compose_wrap.py book-3` builds the full wrap from
`delivery/cover/the-weight-of-the-source-front-cover-eclipse.png`. Spine =
page count x `PPI_FACTOR`, set to IngramSpark **white 50#** (0.002252"/pp) to match
the accepted Book One and Book Two wraps. **Confirm the paper stock at upload and
re-check the spine against IngramSpark's spine calculator before ordering.**
The back-cover copy lives in `../tools/compose_wrap.py` (BOOKS["book-3"]) and is a
first pass written from STATE.yaml's premise — worth an author read before print.

## Current build
- **r8** — 20 chapters, 111,618 words, **322 pages** (even). First build since r5;
  it picks up the r6 (Act-One + finale de-tick) and r7 (aggressive tic-cap) prose.
  - `Saeren-Chronicles-Book-Three-6x9-interior-r8.pdf` — RGB review/proof copy.
  - `Saeren-Chronicles-Book-Three-6x9-interior-r8-PDFX1a.pdf` — PDF/X-1a:2001.
  - `../cover/Saeren-Book-Three-FULL-WRAP-r8.pdf` + `-PDFX1a.pdf` — spine 0.725",
    canvas 12.975" x 9.250", real EAN-13 for 979-8-1827-2380-0. First wrap this
    book has had.
  - `../ebook/Saeren-Chronicles-Book-Three-The-Weight-of-the-Source.epub` — eBook
    ISBN 979-8-1827-2381-7.
- New in r8: print ISBN 979-8-1827-2380-0 on the copyright page; imprint, bio and
  acknowledgments filled in (were `[IMPRINT]` / `[EXPANDED BIO OPTIONAL]` /
  `[Acknowledgments]`); and an **"Also by Post Peleos"** page in the front matter,
  on the verso facing the title page, listing the trilogy and — under a rule — the
  adult line as *A Bond of Scale and Silver* by **Søren Stromberg**, labelled 18+.
