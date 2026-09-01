# Completed books — upload-ready files

Everything finished and ready to go to IngramSpark, in one place. **Generated, not
hand-maintained** — run `python3 tools/collect_completed.py` from the repo root to
refresh, and `--check` to verify nothing here has gone stale against the live builds.

| # | Title | Pen name | Pages | Spine | Print ISBN | eBook ISBN | Rev |
|---|---|---|---|---|---|---|---|
| 1 | Hazel Academy | Post Peleos | 294 | 0.662" | 979-8-2409-9043-4 | 979-8-2409-9044-1 | r19 |
| 2 | The Resistance | Post Peleos | 308 | 0.694" | 979-8-2409-9382-4 | 979-8-2561-0025-4 | r13 |
| 3 | The Weight of the Source | Post Peleos | 324 | 0.730" | 979-8-1827-2380-0 | 979-8-1827-2381-7 | r10 |
| 4 | A Bond of Scale and Silver | **Søren Stromberg** | 448 | 1.120" | 979-8-1827-2378-7 | 979-8-1827-2379-4 | r5 |

Books 1–3 are the upper-YA Saeren trilogy under **Post Peleos**. Book 4 is a
standalone adult romantasy (18+) under **Søren Stromberg** — set the author field to
the right name per title when you create the IngramSpark record; it must match the
cover and title page.

## What each folder holds

- `*-INTERIOR.pdf` — the print interior. Grayscale, no ICC profile, 6×9 exact trim,
  fonts fully embedded, even page count for perfect binding.
- `*-COVER.pdf` — the full wrap (back + spine + front) at full bleed. CMYK, no ICC,
  with a real EAN-13 barcode for the print ISBN and no price add-on.
- `*.epub` — the ebook, carrying the eBook ISBN as its package identifier, with a
  working chapter-navigation TOC (`nav.xhtml` + `toc.ncx`).
- `*-EBOOK-COVER.jpg` — the standalone front-cover image the ebook listing asks for
  separately from the EPUB. RGB JPG, at least 1600px on the short side, ratio 1.414
  (inside the 1.33–1.6 retailers accept). Not revision-stamped, because it is artwork
  rather than a build output.

These are the three files IngramSpark wants. The PDF/X-1a builds are archival /
prepress copies and stay in each book's own `delivery/` folder — **do not upload
those**; per the upload guide it takes the grayscale interior and the CMYK cover.

## Getting them onto a machine that can upload

```
git clone https://github.com/knightdx91-alt/Books.git ~/Books
mkdir -p ~/Downloads && cp -r ~/Books/completed-books/* ~/Downloads/
ls -la ~/Downloads/*/
```
Full walkthrough, including the Cloud Shell + VNC route from a locked phone, is in
`books/saeren/INGRAMSPARK-UPLOAD-GUIDE.md`.

## Before you order a print proof

- **Confirm the paper stock.** Spines are computed at IngramSpark white 50#
  (0.002252"/pp), which reproduces the widths the accepted Book One and Book Two
  covers were built at. Scale & Silver is at cream 50# per its own playbook. Re-check
  the final number against IngramSpark's spine calculator — the spine is the one
  dimension a reprint cannot fix.
- **Cover art is upscaled, not native 300 dpi.** Every cover places its art at 375 dpi
  or better, but that is reached by resampling (1.24–1.55×; Scale & Silver's front was
  genuinely re-rendered at 2×). It clears the spec and adds no detail. Recorded in each
  book's production notes.
- **The text layer is degraded in the upload PDFs.** The Ghostscript grayscale/CMYK
  pass drops the fonts' ToUnicode mapping, so non-ASCII characters (em dashes, curly
  quotes, ©, ø) do not *extract* — printing is unaffected. If you ever need a
  searchable or accessible PDF, use the RGB build from the book's `delivery/` folder.
