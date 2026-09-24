# Publishing

Manuscript → EPUB + print PDFs → IngramSpark. Everything here was learned by uploading real
books, including the rejections. The specs are fussier than they look, and the spine is the
one dimension a reprint cannot fix.

## What IngramSpark actually wants

Three files per title, and they are not the files you'd guess:

| File | Spec |
|---|---|
| **Interior** | Print PDF, **grayscale, no ICC profile**, exact trim (6×9 here), fonts fully embedded, **even page count** for perfect binding |
| **Cover** | Full wrap (back + spine + front) at full bleed, **CMYK, no ICC**, real EAN-13 barcode for the print ISBN, **no price add-on** |
| **EPUB** | Carries the **eBook ISBN** as its package identifier, with a working navigation TOC (`nav.xhtml` + `toc.ncx`) |

Plus a **standalone front-cover JPG** for the ebook listing: RGB, ≥1600px on the short side,
aspect ratio around 1.414 (retailers accept 1.33–1.6).

**Do not upload the PDF/X-1a builds.** They are archival/prepress copies and stay in each
book's `delivery/` folder. Upload takes the grayscale interior and the CMYK cover.

## Building the files

```bash
# interior -> grayscale, no ICC
bash tools/make_noicc.sh gray delivery/production/INTERIOR-r7.pdf INTERIOR-r7-GRAY-noicc.pdf

# cover wrap -> CMYK, no ICC
bash tools/make_noicc.sh cmyk delivery/cover/WRAP-r7-fullbleed-rgb.pdf WRAP-r7-CMYK-noicc.pdf
```

Needs Ghostscript. Verify a finished PDF before it goes anywhere near the upload form:

```bash
python3 tools/check_upload_pdf.py interior <file.pdf>   # wants DeviceGray, no profile
python3 tools/check_upload_pdf.py cover    <file.pdf>   # wants DeviceCMYK, no profile
python3 tools/check_upload_pdf.py any      <file.pdf>   # just tell me what this is
```

It reads the colour space and profile markers out of the bytes (raw and decompressed,
so an `/ICCBased` inside an object stream cannot hide) rather than trusting the
filename — which matters, because the three wraps in a `delivery/` folder look alike:

| file | what it is |
|---|---|
| `<name>-rN.pdf` | the build — **DeviceRGB**, wrong colour space |
| `<name>-rN-PDFX1a.pdf` | archival — **carries an OutputIntent**, i.e. the ICC profile IngramSpark objects to |
| `<name>-rN-CMYK-noicc.pdf` | **the upload copy** |

`collect_completed.py --check` runs the same check over everything in
`completed-books/`, so a wrong-colour-space or profile-carrying print file fails there
too instead of at the upload form.

### The cover wrap

Start by taking the specs — trim, stock, page count, ISBN, art:

```bash
python3 tools/compose_wrap.py books/<slug> --init
```

It asks for each one, shows the resulting spine and wrap size for confirmation,
checks the ISBN and the art resolution as you go, and writes
`books/<slug>/delivery/cover.yaml`. Fill in the back-cover copy it leaves as
placeholders, then build:

```bash
python3 tools/compose_wrap.py books/<slug>
```

It stops rather than guessing: refuse the spine confirmation and nothing is
written; art under 300 ppi has to be accepted explicitly; a short ISBN
re-prompts. An existing config is never overwritten without asking.

Config-driven, from `books/<slug>/delivery/cover.yaml` (the twin of `ebook.yaml`).
**You supply front cover art only** — the tool builds everything else on the wrap:
the back panel, the spine, the EAN-13, and the full-bleed canvas.

```
│◄──────────── 2 × 6" + spine + 2 × 0.125" bleed ────────────►│
┌──────────────────────┬─────────┬──────────────────────┐
│      BACK PANEL      │  SPINE  │     FRONT PANEL      │ 9.25"
│  blurb, author block │  title  │   (the supplied art) │
│  photo, EAN-13       │  author │                      │
└──────────────────────┴─────────┴──────────────────────┘
```

**The spine width is `pages × paper factor`,** so the interior must be final before
the cover is built — re-cut the interior and the wrap is wrong. Only the two factors
verified against accepted books ship in the tool:

| stock | factor |
|---|---|
| `white50` | 0.002252 |
| `cream50` | 0.0025 |

Any other stock must set `paper.factor` explicitly, read off IngramSpark's own spine
calculator. The tool refuses to guess, because guessing here wastes a print run.

**The front art is placed scale-to-fill with a centre crop** into the 6.125 × 9.25"
front panel (trim plus bleed). Art at the wrong aspect ratio loses its edges, so the
build report prints the crop and the effective resolution:

```
  art      2452x3469px -> crop 2297x3469px (lost 6.3% w, 0.0% h)
  art ppi  375.0 effective across the 6.125" front panel [OK]
```

Under 300 ppi it says so and gives the pixel dimensions to ask for. A square
1024×1024 cover, for instance, loses a third of its width and lands at 110 ppi.
`tools/cover_art_to_print_res.py` upscales art to clear the 300 ppi floor — it
clears the spec and adds no detail, so prefer real resolution when it exists.

The output is an RGB proof; run `make_noicc.sh cmyk` on it for the upload copy.

Both factors were verified against books this pipeline has had accepted and printed.

Verified by rebuilding every shipped wrap from config — each renders **pixel-identical**
to the PDF that was accepted, across both paper stocks.

## Audiobook — the ACX cover

ACX wants a **square** cover, and a print cover is portrait. Centre-cropping one to
square cuts off the top and bottom, which is where the series line and the byline
usually sit — and ACX **requires the author name on the cover**, so that crop fails
review. The builder recomposes instead:

```bash
python3 tools/make_acx_cover.py books/<slug> --measure   # find the element boxes
python3 tools/make_acx_cover.py books/<slug>             # build the cover
```

`--measure` scans the art for bright elements and prints their bounding boxes (and
warns about bright edge artifacts, which otherwise drag every box out to the edge).
Those boxes go in `books/<slug>/delivery/acx.yaml`; the builder lifts each element
from the print art and re-lays them out on the square. Lifting the **rendered
pixels** rather than re-typesetting means the audiobook cover carries the identical
typeface, weight, letterspacing and colour as the print and ebook editions, with no
font to identify or licence.

Three compositing modes, because light-on-dark art does not lift uniformly:

| mode | what it does | use for |
|---|---|---|
| `add` (default) | subtracts the element's own background, adds the rest | type, rules, anything lit |
| `replace` | places the element whole | a focal object **darker** than its surroundings |
| `lighten` | keeps the brighter of the two | simple highlights |

`add` is what stops a lifted rectangle showing its edges — a plain lighten carries
the crop's background across, and since print art is vignetted that background
differs from the canvas and the box becomes visible. But `add` **erases** anything
darker than its surroundings, so a dark focal object (a black gem, a silhouette)
needs `replace`.

### What ACX enforces

Checked automatically on every build:

| requirement | |
|---|---|
| square 1:1 | minimum 2400 × 2400 px |
| JPG / PNG / TIF | RGB, not CMYK |
| at least 72 dpi | at least 24-bit |
| 8 MB maximum | title and author on the cover |

ACX also rejects pixelated or blurry text, Audible logos, watermarks or third-party
images, references to physical media, other retailers or websites, runtime or
pricing, barcodes and QR codes — and **book jacket designs**. So the print wrap is
never a valid audiobook cover: it would fail as a jacket design and again on its
EAN-13 barcode.

Every build also writes `_acx-thumbnail-check.jpg`, the cover at Audible's display
sizes (500 / 300 / 200 / 100 px). The 100px one is the browse grid — if the title
and author stop reading there, the cover is not finished, and that is a judgement
no check can make for you.

### The EPUB

```bash
python3 tools/make_epub.py books/<slug>
```

Config lives in `books/<slug>/delivery/ebook.yaml` (new books get an annotated copy;
otherwise start from `books/_template/delivery/ebook.yaml`). Required: `full_title`,
`author`, `isbn` + `isbn_hyphen`, `cover`. Everything else falls back to `STATE.yaml` or is
optional — subtitle, series title, publisher, year, dedication, bio, acknowledgments, author
photo, and an "Also by" page. All paths are relative to the book folder, so a book folder
stays portable.

Input is an assembled single-file manuscript using `CHAPTER ONE` headings — what the
per-book `assemble_manuscript.py` produces. If `manuscript` isn't set, the newest
`manuscript/full-manuscript*.md` is used, or the one matching a `REVISION` file.

**The `isbn` must be the EBOOK ISBN**, not the print one: it becomes the EPUB's package
identifier, which is what retailers read.

The output is EPUB3 with an EPUB2 NCX fallback, mimetype stored first and uncompressed, and
a working `nav.xhtml` + `toc.ncx`.

EPUB ISBN swap (when reusing an existing build for a new identifier, rather than rebuilding):
unzip, replace the ISBN in `OEBPS/content.opf` (`dc:identifier`), `OEBPS/toc.ncx`
(`dtb:uid`) and `OEBPS/copyright.xhtml`, then rezip with **mimetype stored first**:

```bash
zip -X -q0 OUT.epub mimetype && zip -X -qrg OUT.epub . -x mimetype
```

`build_pdf.py` and `assemble_manuscript.py` stay per-book, because trim size, front matter
and typography differ per title. A series with locked shared front matter can keep its own
builder in the series folder; `tools/make_epub.py` covers everything else.

## The gotchas, in the order they bit

**Image resolution: 300 ppi is a target, not a floor.** An upload was rejected for
*excessively high* resolution ("Excessively high resolution images will not increase the
quality of the printed book, and can lead to the book being delayed"). Their preflight
objects to too-high as well as too-low. `make_noicc.sh` downsamples to 300 (600 for bitmap
line art) — and the threshold overrides matter, because Ghostscript's `/prepress` only
downsamples above 1.5× the target by default, so 300–450 ppi images would slip through.

**The Ghostscript pass costs the text layer.** The grayscale/CMYK conversion drops the
fonts' ToUnicode mapping, so non-ASCII characters (em dashes, curly quotes, ©, ø) don't
*extract* from the upload PDF. Printing is unaffected. If you need a searchable or
accessible PDF, use the RGB build from `delivery/`.

**Cover wrap must be tight full-bleed.** IngramSpark's current template wants no white
margins. Wraps built to the older Lightning Source template have white margins that shift
the back-cover content into the spine. Crop to the true art box.

**Supply your own barcode.** On the cover step choose "my cover already includes a barcode"
so IngramSpark doesn't overlay its own white box on yours. Generate the EAN-13 from the
print ISBN with `python-barcode`, no price add-on.

**Print and eBook are separate formats** with separate interior + cover steps — and the
"Preview my book" button validates *all* formats, so an empty eBook format blocks you while
you're still on the print tab.

**The eBook interior must be an EPUB or .docx.** A PDF is rejected there. The eBook "page
count" field is nominal; enter the print count to match.

**If "PDF CONTAINS ICC COLOR PROFILES" appears, check which file you uploaded first.**
The usual cause is not a bad build — it is the archival `-PDFX1a.pdf` going up instead of
the `-CMYK-noicc.pdf` upload copy, and the two differ by a filename. Run
`python3 tools/check_upload_pdf.py cover <file.pdf>` on whatever you sent; if it comes back
FAIL, go Back, upload the file from `completed-books/<nn-slug>/` instead, and do not tick
the authorize-anyway box. The warning *is* non-blocking, so if the file genuinely checks
out clean you can proceed — but then order a printed proof and confirm the interior text
prints solid black, not gray.

**Type the title once.** Entering it repeatedly is what made a title display three or four
times on the product page.

**Confirm the paper stock before ordering a proof.** Spine width is computed from page
count × paper thickness (IngramSpark white 50# = 0.002252"/pp here; one book uses cream
50#). Re-check the final number against IngramSpark's own spine calculator.

## `completed-books/` — the upload staging folder

Every finished book's three upload files, collected in one place.

```bash
python3 tools/collect_completed.py           # refresh from each book's current revision
python3 tools/collect_completed.py --check   # verify nothing has gone stale (exit 1 if it has)
```

**It is generated — never hand-edit it.** Copies go stale the moment a book is re-cut, and
a stale print file is exactly the kind of thing that gets uploaded by mistake. Every file
is checksummed into `MANIFEST.md` alongside the revision it came from, so staleness is
*detectable* rather than silent. Re-run after any re-cut, and add new books to the `BOOKS`
list in the script.

`completed-books/LISTING-METADATA.md` holds the answers to the publishing form per book —
including the ones with byte limits (IngramSpark's Short Description cap is 250 **bytes**,
not characters, which matters the moment you use a curly quote or an em dash).

## Uploading from a locked-down device

If the machine you're on can't drive a file picker (a locked phone, a kiosk), the route
that works is a full Linux desktop in **Google Cloud Shell** — XFCE plus real Firefox,
streamed into the browser — with the book files pulled straight from your repo into that
desktop's `~/Downloads`. The desktop's file picker works, and the device is just a screen.

Keep your own notes on this in the book folder once you've done it — including the "an error
has occurred during the upload" path, which is the one that wastes an afternoon. One warning
if you do: never commit a GitHub access token to those notes. Secret scanning auto-revokes
any token pushed to a repo, so it would be dead within minutes anyway — mint a fresh one when
you need it (about 30 seconds).

## Before you approve for sale

- Order a **printed proof**. Check the interior prints solid black, the spine text is
  centred, and nothing has crept into the gutter.
- Confirm the ISBNs: print and ebook are **different ISBNs**, and the one baked into the
  barcode must match the print ISBN on the record.
- Confirm the author name field matches the cover and title page exactly — a pen name that
  differs between the record and the artwork is a rejection.
- Run `collect_completed.py --check` one last time so you know the files in your hand are
  the current build.
