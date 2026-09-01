# Book Two — Production Notes

## Revision policy (same as Book One)
`book/genesis/saeren-chronicles-book-2/REVISION` is the single source of truth for
the build tag (e.g. `r1`). **Bump it BEFORE rebuilding**, then rebuild; the prior
build files (`...-r1.pdf`, `full-manuscript-r1.md`) are kept as history and the new
build carries the new tag. No manuscript/PDF update ships without a revision bump.

## Build pipeline
```
cd book/genesis/saeren-chronicles-book-2
python3 tools/assemble_manuscript.py   # -> manuscript/full-manuscript-<rev>.md
python3 tools/build_pdf.py             # -> delivery/production/...-interior-<rev>.pdf  (RGB)
bash    tools/make_pdfx.sh             # -> delivery/production/...-interior-<rev>-PDFX1a.pdf  (CMYK/PDF-X-1a)
```

## Spec (mirrors Book One)
- Trim 6" × 9"; margins side 0.75", top 0.75", bottom 0.70" (gutter-safe ≤ ~500pp).
- IBM Plex Serif, fully embedded; body 11/15.5pt justified, 16pt indent.
- Chapter-title running heads; page numbers start at 1 on Chapter One.
- Even physical page count (auto-padded) for perfect binding.
- Body text is pure K-only black, so the CMYK pass yields clean black with no rich-black.

## Cover wrap
`../../../tools/compose_wrap.py book-2` builds the full wrap (back + spine + front,
full bleed) from `delivery/cover/the-resistance-front-cover-fractured-light.png`.
Spine = page count x `PPI_FACTOR`; that factor is set to IngramSpark **white 50#**
(0.002252"/pp), which is what the accepted Book One and Book Two wraps were built at.
**Confirm the paper stock at upload and re-check the spine against IngramSpark's own
spine calculator before ordering** — it is the one dimension a reprint can't fix.
Convert the wrap to PDF/X-1a with `bash tools/make_pdfx.sh <wrap.pdf> <wrap-PDFX1a.pdf>`.

## Current build
- **r11** — 20 chapters, 103,245 words, **308 pages** (even).
  - `Saeren-Chronicles-Book-Two-6x9-interior-r11.pdf` — RGB review/proof copy.
  - `Saeren-Chronicles-Book-Two-6x9-interior-r11-PDFX1a.pdf` — PDF/X-1a:2001 (IngramSpark).
  - `../cover/Saeren-Book-Two-FULL-WRAP-r11.pdf` + `-PDFX1a.pdf` — spine 0.694",
    canvas 12.944" x 9.250", real EAN-13 for 979-8-2409-9382-4.
  - `../ebook/Saeren-Chronicles-Book-Two-The-Resistance.epub` — eBook ISBN
    979-8-2561-0025-4 (also the OPF `dc:identifier`).
- What changed from r10: an **"Also by Post Peleos"** page was added to the front
  matter, on the verso facing the title page (where a trade paperback conventionally
  carries it). It lists the trilogy, then — under a rule — the adult line as
  *A Bond of Scale and Silver* by **Søren Stromberg**, labelled 18+ so the YA brand
  stays clean. The Book Three teaser at the back now names the title. Page count
  306 -> 308, so the cover was re-cut to match.
- Front matter is fully filled (ISBN, imprint, dedication, acknowledgments, bio) —
  no placeholders remain in this book.
