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

## Author photo
`books/_assets/author-photo.jpg` (colour, 1080x1080) and `author-photo-gray.jpg`
(the grayscale twin) are shared by every book. Two placements, both automatic:
- **Interior**, centred above the bio on the *About the Author* page, 1.6" square
  from the **grayscale** file — the print interior uploads as DeviceGray, so a
  colour image there would be converted anyway and risks the B&W-interior spec.
  Lands at ~675 dpi.
- **Back cover**, bottom-left beside the name and bio, 1.0" square with a hairline
  border, from the **colour** file (covers print CMYK). Lands at ~1080 dpi.
Set the `AUTHOR_PHOTO` constant to `""` in either script to drop the photo.

## ⚠ Which file to upload (this is easy to get wrong)
IngramSpark takes the **`-GRAY-noicc.pdf`** interior and the **`-CMYK-noicc.pdf`**
cover — *not* the PDF/X-1a builds. The X-1a files are kept as the archival/prepress
copies. Produce the upload pair with the shared converter:
```
bash tools/make_noicc.sh gray <interior-rN.pdf> <interior-rN-GRAY-noicc.pdf>
bash tools/make_noicc.sh cmyk <wrap-rN.pdf>     <wrap-rN-CMYK-noicc.pdf>
```
It leaves images at source resolution rather than resampling them to exactly
300 dpi, and it verifies the output carries no ICC profile or output intent.
