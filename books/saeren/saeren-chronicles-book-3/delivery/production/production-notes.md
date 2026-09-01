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
on a page. `DEDICATION` is now set (author-supplied, 2026-09-01), so Book Three's front
matter matches Books One and Two exactly: half-title / "Also by" / title page /
copyright / dedication / blank verso.

## Cover wrap
`../tools/compose_wrap.py book-3` builds the full wrap from
`delivery/cover/the-weight-of-the-source-front-cover-eclipse.png`. Spine =
page count x `PPI_FACTOR`, set to IngramSpark **white 50#** (0.002252"/pp) to match
the accepted Book One and Book Two wraps. **Confirm the paper stock at upload and
re-check the spine against IngramSpark's spine calculator before ordering.**
The back-cover copy lives in `../tools/compose_wrap.py` (BOOKS["book-3"]) and is a
first pass written from STATE.yaml's premise — worth an author read before print.

## Current build
- **r8** — 20 chapters, 111,618 words, **324 pages** (even). First build since r5;
  it picks up the r6 (Act-One + finale de-tick) and r7 (aggressive tic-cap) prose.
  - `Saeren-Chronicles-Book-Three-6x9-interior-r8.pdf` — RGB review/proof copy.
  - `Saeren-Chronicles-Book-Three-6x9-interior-r8-PDFX1a.pdf` — PDF/X-1a:2001.
  - `../cover/Saeren-Book-Three-FULL-WRAP-r8.pdf` + `-PDFX1a.pdf` — spine 0.730",
    canvas 12.980" x 9.250", real EAN-13 for 979-8-1827-2380-0. First wrap this
    book has had.
  - `../ebook/Saeren-Chronicles-Book-Three-The-Weight-of-the-Source.epub` — eBook
    ISBN 979-8-1827-2381-7.
- New in r8: the author's dedication; print ISBN 979-8-1827-2380-0 on the copyright page; imprint, bio and
  acknowledgments filled in (were `[IMPRINT]` / `[EXPANDED BIO OPTIONAL]` /
  `[Acknowledgments]`); and an **"Also by Post Peleos"** page in the front matter,
  on the verso facing the title page, listing the trilogy and — under a rule — the
  adult line as *A Bond of Scale and Silver* by **Søren Stromberg**, labelled 18+.

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

## Front-cover art resolution — resolved 2026-09-01
All four covers now place their front art at **375 dpi or better** (Scale & Silver
at 470), clear of IngramSpark's 300 dpi floor.

- **Scale & Silver** is the real fix: its front is composited in-repo
  (`delivery/cover/compose_cover.py` = art bed + HTML/CSS type), so it was
  **re-rendered at 2x** through headless Chromium. The *type* is genuinely
  vector-sharp at that size rather than resampled — and type is what shows
  softness in print. Only its art bed is interpolated.
  ```
  python3 delivery/cover/compose_cover.py
  chromium --headless --no-sandbox --disable-gpu --hide-scrollbars \
    --force-device-scale-factor=2 --window-size=1600,2263 \
    --screenshot=front-cover-soren-stromberg-2x.png "file://$PWD/compose.html"
  ```
- **Books One, Two and Three** are fixed rasters with no design source in the repo,
  so they were resampled with `tools/cover_art_to_print_res.py` into `-print`
  variants that the wrap generator now points at. **Be straight about what that
  is:** it clears the spec and puts our resampler in charge instead of the
  printer's RIP, but it adds no detail. The cost is unusually low here — the art is
  soft gradient (smoke, glow, a crack, an eclipse) with almost no high-frequency
  detail, and the type on it was already antialiased — but it is not the same as a
  true high-res export.
- **If the original design files ever turn up**, re-export the front art at
  ≥1838 x 2775 px, drop it in under the plain filename, and point `front=` back at
  it. That is the only way to get real detail rather than a clean number.
