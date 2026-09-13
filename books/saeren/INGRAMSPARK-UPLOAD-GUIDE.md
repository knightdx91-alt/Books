# IngramSpark Upload Guide (from a locked phone, via Google Cloud Shell)

This is the exact workflow we used to upload **The Saeren Chronicles** to IngramSpark
from an FRP-locked Android phone whose native file picker doesn't work. Reuse it for
**Book 3** (and re-uploads). Everything here was learned the hard way — the gotchas
are called out so you don't repeat them.

> **No access token is needed any more.** `knightdx91-alt/Books` is a **public**
> repo (deliberately), so the files download over plain HTTPS with no credentials at
> all. The whole token dance this guide used to open with is gone — see Part B.
> If you ever make the repo private again, you will need a classic `repo`-scope token
> back; never commit one, because GitHub secret-scanning auto-revokes tokens pushed
> to a repo and flags the account.

---

## Why we need all this
- The phone is FRP-locked → the OS file picker doesn't work → can't pick files to
  upload to IngramSpark in the normal browser.
- Fix: run a **full Linux desktop with a real browser inside Google Cloud Shell**,
  streamed into the phone's browser. That desktop's file picker works, and the book
  files are downloaded straight into it from GitHub. The phone is just a screen.

---

## PART A — Get a browser GUI running in Google Cloud Shell

Cloud Shell is free with a Google account, runs entirely in the phone's browser, no
install needed. (Note: installed apt packages and the desktop reset between sessions;
your `~` / `~/Downloads` files persist. If you come back later, just re-run Steps 1–3.)

**1. Open** https://shell.cloud.google.com and sign in. Wait for the black terminal.

**2. Install the desktop + a browser.** Chromium is snap-broken in Cloud Shell and
`firefox-esr` was removed from the repo, so we use **real Firefox from Mozilla**.
We use the full **XFCE** desktop (top panel, Applications menu, Thunar file
manager) so you can confirm `~/Downloads` before uploading:

```
sudo apt-get update -y && sudo apt-get install -y xfce4 xfce4-goodies dbus-x11 tigervnc-standalone-server novnc websockify
cd ~ && rm -rf firefox firefox.tar.xz
wget --content-disposition -O firefox.tar.xz "https://download.mozilla.org/?product=firefox-latest&os=linux64&lang=en-US"
tar xf firefox.tar.xz
ls ~/firefox/firefox && echo "FIREFOX OK"
```

(If Firefox later won't launch for missing libs, run:
`sudo apt-get install -y libgtk-3-0 libdbus-glib-1-2 libx11-xcb1`.)

**3. Start the GUI.** The `exec startxfce4` line is critical — if the xstartup
script exits, TigerVNC tears the whole session down (that was the "startup
immediately exiting" bug):

```
mkdir -p ~/.vnc
printf '#!/bin/sh\nunset SESSION_MANAGER\nunset DBUS_SESSION_BUS_ADDRESS\n%s/firefox/firefox &\nexec startxfce4\n' "$HOME" > ~/.vnc/xstartup
chmod +x ~/.vnc/xstartup
tigervncserver -kill :1 2>/dev/null
tigervncserver :1 -geometry 1280x800 -localhost no -SecurityTypes None --I-KNOW-THIS-IS-INSECURE
pkill websockify 2>/dev/null; sleep 1
websockify --web=/usr/share/novnc 8080 localhost:5901 >/tmp/novnc.log 2>&1 &
echo "started"
```

- For a **phone-shaped (portrait)** screen, use `-geometry 800x1280` instead of 1280x800.
- **XFCE gives you a full desktop** — a top panel, an Applications menu, and the
  **Thunar file manager** so you can open `~/Downloads` and confirm the book files
  are really there before the upload. `dbus-x11` is **required** or XFCE half-breaks
  (no panel / no menus). If the desktop comes up grey, wait ~15s for the panel to
  paint, or check `cat ~/.vnc/*.log` for errors. Cloud Shell wipes apt packages
  between sessions, so XFCE is reinstalled each time you come back (re-run Steps 1–3),
  but `~` files (including `~/.vnc/xstartup`) persist.

**4. Open the desktop in the phone browser.** Cloud Shell toolbar (top-right) →
**Web Preview** (monitor/eye icon; may be under a `⋮` overflow on a narrow screen) →
**Change port → 8080 → Change and Preview**. A new tab opens.
- If it shows a **directory listing or 404**, add **`/vnc.html`** to that tab's URL.
- Tap **Connect**. You'll see the XFCE desktop (top panel + Applications menu) with
  Firefox already open.

**5. If the desktop is hard to navigate on the phone:** open the small noVNC tab on
the **left edge** → gear/Settings → **Scaling Mode → Local Scaling** (fits the whole
desktop to your screen, no pinch-zoom). There's also a fullscreen button there.

---

## PART B — Get the book files from GitHub into Cloud Shell

We download the files straight into the Cloud Shell desktop (no native picker needed),
then upload them to IngramSpark from there.

> **This part used to require a personal access token.** It no longer does — the repo
> is public. If you are following an older printout, skip every token step in it.

**Take the files from `completed-books/`, never from a book's `delivery/` folder.**
`delivery/` holds every build ever cut — three near-identical wraps per revision, of
which exactly one is the upload copy. `completed-books/<nn-slug>/` holds only the
current, correct four, and `collect_completed.py --check` verifies they are the live
build AND profile-free in the right colour space. Picking from `delivery/` by hand is
how the wrong file gets uploaded.

**1. Download them** — in the Cloud Shell **terminal**. Set `BOOK` to the folder you
want and paste the rest as-is. (Always clear `~/Downloads` first — stale files from a
previous session caused upload failures.)

```
BOOK=02-the-resistance     # 01-hazel-academy | 02-the-resistance |
                           # 03-the-weight-of-the-source | 04-a-bond-of-scale-and-silver

rm -f ~/Downloads/*
mkdir -p ~/Downloads && cd ~/Downloads
base="https://raw.githubusercontent.com/knightdx91-alt/Books/main/completed-books/$BOOK"
curl -sL "https://api.github.com/repos/knightdx91-alt/Books/contents/completed-books/$BOOK" \
  | grep -o '"name": *"[^"]*"' | cut -d'"' -f4 \
  | while read -r f; do curl -sL -o "$f" "$base/$f"; done

echo "=== want 4 files, real sizes, %PDF / PK / JFIF headers — NOT ~112 bytes ==="
for f in *; do printf "%-46s %-7s hdr=" "$f" "$(ls -lh "$f" | awk '{print $5}')"; head -c4 "$f"; echo; done
```

Or, if you would rather have the whole repo (it is ~320 MB, so the per-file version
above is faster):
```
cd ~ && rm -rf Books && git clone --depth 1 https://github.com/knightdx91-alt/Books.git
rm -f ~/Downloads/* && cp ~/Books/completed-books/$BOOK/* ~/Downloads/
```

**GOTCHA — the 112-byte file:** a file of ~112 bytes, or one whose header is `{`, is a
GitHub error message rather than a book. Under the old token flow that meant a bad
token; now it means a wrong path or folder name. Re-check `BOOK` against the list above.

**2. What each of the four files is for:**

| file | IngramSpark slot |
|---|---|
| `*-INTERIOR.pdf` | Print (Perfect Bound) → interior |
| `*-COVER.pdf` | Print (Perfect Bound) → cover |
| `*.epub` | eBook → interior (a PDF is rejected here) |
| `*-EBOOK-COVER.jpg` | eBook → cover image |

**3. Upload in Firefox** (inside the Cloud Shell desktop): go to ingramspark.com, and
when its picker opens, choose the files from **Home → Downloads**.

---

## PART C — IngramSpark settings & file rules we learned

**Two formats per title:** "Print (Perfect Bound)" and "eBook" are separate. Each
has its own interior + cover steps. The "Preview my book" button validates *all*
formats, so an empty eBook format will block you even while you're on the print tab.

**Print Perfect Bound:**
- **Interior = the PDF** (6×9, 294pp Book 1 / 306pp Book 2). It is grayscale, no ICC.
- **Cover = the full-bleed wrap PDF** (CMYK, no ICC). On the cover step choose
  **"my cover already includes a barcode"** so IngramSpark doesn't overlay its own
  white barcode box on top of ours.

**eBook:**
- **Interior = the EPUB** (or a .docx). A PDF is rejected here ("ePub or Word
  interior file is required"). EPUB is preferred.
- eBook "page count" field is nominal — enter the print count (e.g. 306) to match.

**Barcode:** our covers have the barcode baked in (print ISBN), **no price add-on**
(per author preference). So always pick "I supply my own barcode."

**IngramSpark renames your files on upload.** A file you sent as
`The-Resistance-r14-COVER.pdf` can come back on the validation screen as something like
`BB-cover.pdf` — an internal job name, unrelated to what you uploaded. Observed
2026-09-13. Two consequences, and the second one cost us a lot of wasted reasoning:

- **The filename on the validation screen is not evidence of which file you sent.** You
  cannot diagnose anything from it. Don't try.
- **They are re-processing the PDF server-side**, not just storing it. A rename means
  their pipeline rewrites the file, so what their validator inspects is *their* output,
  not your bytes.

**The ICC-profile warning** ("PDF CONTAINS ICC COLOR PROFILES…") is a **non-blocking
warning**, and given the above it can appear even on a file that is verifiably
profile-free when it leaves here — their re-save can attach a profile of its own. So
the sequence that actually works is:

**1. Verify BEFORE you upload, while you still control the bytes:**
```
python3 tools/check_upload_pdf.py cover    <file.pdf>
python3 tools/check_upload_pdf.py interior <file.pdf>
```
Files taken from `completed-books/<nn-slug>/` are already verified on every
`collect_completed.py --check`, so this is a formality unless you sourced the file
elsewhere.

**2. If it passed locally and the warning still appears, proceed.** You have done
everything you can from this side; the profile is theirs. Tick the box, then **order a
printed proof** and confirm the interior text prints solid black (not gray) before
approving for sale. That proof is the real check — do not skip it.

**3. If it failed locally, go Back** and re-upload from `completed-books/<nn-slug>/`.

> **A caution about the `-PDFX1a.pdf` files.** An earlier version of Part B said to
> upload the PDF/X-1a cover instead of the CMYK/no-ICC one, on the grounds that the
> no-ICC file "previews BLANK/WHITE on IngramSpark because it has no OutputIntent."
> That contradicted Part C of this same document and `docs/PUBLISHING.md`, both of which
> have always said CMYK/no-ICC, so it has been removed. The X-1a build does carry an
> OutputIntent by design, so it will certainly trip the warning — but note we have never
> actually confirmed it was the file behind any particular rejection, and the rename
> behaviour above means the validation screen could never have told us. If a no-ICC
> cover ever does preview blank, report that rather than switching files: it is a
> preview-renderer quirk to investigate, not a reason to upload the profiled build.

**Cover document size:** IngramSpark's current template wants a **tight full-bleed
wrap** (no white margins). The original wraps were built to the old 15×12 Lightning
Source template with white margins, which shifted the back content into the spine.
We crop them to the true art box. Final sizes used:
- Book 1: **12.911 × 9.249 in** (spine 0.661", 294pp cream)
- Book 2: **12.937 × 9.249 in** (spine 0.687", 306pp cream)

**Title field:** type the title **once**. Entering it repeatedly is what made the
main page show it 3–4×; the files themselves are clean.

---

## PART C½ — Getting files IN from WhatsApp (FRP-locked device, no native share)

On an FRP-locked phone the native "Save to Drive"/file picker doesn't work, so you
can't share a WhatsApp attachment to Drive directly. Instead, pull the file using
**WhatsApp Web inside the Cloud Shell desktop** (the same desktop from Part A whose
file picker DOES work), then push it to GitHub from the terminal. The phone stays
just a screen. This uses WhatsApp's official **Linked Devices** feature — no
third-party tools, no ToS risk.

**1. Open WhatsApp Web in the Cloud Shell Firefox** (Part A desktop running):
go to **https://web.whatsapp.com** — it shows a QR code.

**2. Link from the phone:** WhatsApp → **⋮ menu → Linked devices → Link a device**
→ point the phone camera at the QR code on the Cloud Shell Firefox screen. (FRP lock
does NOT block this — the WhatsApp app and camera work normally.) Your chats load in
the desktop Firefox.

**3. Download the file into the desktop:** open the chat → click the file → the
download arrow. It saves to **~/Downloads** in the Cloud Shell desktop.

**4. Push it into GitHub** — in the Cloud Shell **terminal**:
```
cd ~ && rm -rf Books && git clone https://github.com/knightdx91-alt/Books.git
cd Books
git config user.email noreply@anthropic.com; git config user.name "Claude"
# copy the WhatsApp file in (change filename + destination folder as needed):
cp ~/Downloads/THE_FILE.pdf  books/saeren/saeren-chronicles/delivery/cover/
git add -A && git commit -m "add file from WhatsApp" && git push
```
Once pushed it's on `main` — Claude can then see it, rename/move it, or rebuild
deliverables from it. **Reading the repo needs no credentials, but pushing does**, so
this step will prompt for a GitHub username + token, or use the Upload-files
alternative below, which authenticates through the browser session you are already
signed into.

- You re-link WhatsApp Web once per Cloud Shell session (the desktop resets between
  sessions, so the QR re-scan is needed each time).
- Alternative to the git commands: in the same Firefox, go to github.com → the repo
  → the target folder → **Add file → Upload files** and pick the file from ~/Downloads.

---

## PART D — How the print/ebook files are produced (for Book 3, in this repo)

Run these in the book's folder (`books/saeren/saeren-chronicles-book-3/`). Needs
Ghostscript (`sudo apt-get install -y ghostscript`) and Python `pymupdf`,`pillow`,
`numpy`,`python-barcode`.

**1. Interior → grayscale, no ICC** (from the RGB interior build):
```
gs -dBATCH -dNOPAUSE -dNOSAFER -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/prepress \
   -sColorConversionStrategy=Gray -sProcessColorModel=DeviceGray -dAutoRotatePages=/None \
   -sOutputFile=INTERIOR-GRAY-noicc.pdf  INTERIOR-rN.pdf
```

**2. Cover → crop white margins to full-bleed.** Read the official IngramSpark
template's vector rects (back/spine/front bleed boxes) to get the crop box
`x[backLeft .. 15.0] y[0 .. 9.249]`; raster the wrap at 300 DPI, (regenerate the
EAN-13 barcode with `python-barcode` for the print ISBN, **no add-on**, and paste it
over the old one), crop to the box, save, then:
```
gs -dBATCH -dNOPAUSE -dNOSAFER -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/prepress \
   -sColorConversionStrategy=CMYK -sProcessColorModel=DeviceCMYK -dAutoRotatePages=/None \
   -sOutputFile=COVER-CMYK-noicc.pdf  cover-fullbleed-rgb.pdf
```
(See the Book-2 commit history for the exact barcode-swap + crop script.)

**3. EPUB ISBN swap:** unzip the epub; replace the old eBook ISBN in `OEBPS/content.opf`
(`dc:identifier`), `OEBPS/toc.ncx` (`dtb:uid`), and `OEBPS/copyright.xhtml`; rezip with
**mimetype stored first**:
```
zip -X -q0 OUT.epub mimetype && zip -X -qrg OUT.epub . -x mimetype
```

**Verify any PDF is clean** (no profiles): `OutputIntent` absent and `/ICCBased` absent.

---

## Quick reference — ISBNs used
- Book 1 print: 979-8-2409-9043-4 · Book 1 eBook: 979-8-2409-9044-1
- Book 2 print: 979-8-2409-9382-4 · Book 2 eBook: 979-8-2561-0025-4
- Book 3 print: 979-8-1827-2380-0 · Book 3 eBook: 979-8-1827-2381-7
- *A Bond of Scale and Silver* (Søren Stromberg) print: 979-8-1827-2378-7 ·
  eBook: 979-8-1827-2379-4

All of these are now baked into the builds: the print ISBN prints on the copyright
page and renders as a real EAN-13 (no price add-on) on the back cover, and the
eBook ISBN is both on the ebook copyright page and the EPUB's `dc:identifier`.

> **Two names, two lists.** The Saeren books publish as **Post Peleos**;
> *A Bond of Scale and Silver* publishes as **Søren Stromberg** (the adult, 18+
> line). Set the author field to the right one per title when you create the
> IngramSpark record — it must match the cover and title page.

---

## Current upload set (2026-09-01)

| Title | Interior (upload) | Cover (upload) | eBook | Pages | Spine |
|---|---|---|---|---|---|
| Book One — Hazel Academy | `…interior-r18-GRAY-noicc.pdf` | `…FULL-WRAP-r18-CMYK-noicc.pdf` | `…Hazel-Academy.epub` | 294 | 0.662" |
| Book Two — The Resistance | `…interior-r13-GRAY-noicc.pdf` | `…FULL-WRAP-r13-CMYK-noicc.pdf` | `…The-Resistance.epub` | 308 | 0.694" |
| Book Three — The Weight of the Source | `…interior-r10-GRAY-noicc.pdf` | `…FULL-WRAP-r10-CMYK-noicc.pdf` | `…The-Weight-of-the-Source.epub` | 324 | 0.730" |
| A Bond of Scale and Silver | `…interior-r4-GRAY-noicc.pdf` | `…wrap-6x9-r4-CMYK-noicc.pdf` | `A-Bond-of-Scale-and-Silver.epub` | 448 | 1.120" |

The `-PDFX1a` builds sitting beside these are the archival/prepress copies. Upload
the **GRAY-noicc** interior and the **CMYK-noicc** cover, per Part C above.

Spines are computed at **white 50#** (0.002252"/pp), which reproduces the sizes the
earlier Book One and Book Two covers were accepted at (0.661" at 294pp, 0.687" at
306pp). Scale & Silver's is at cream 50# per its own playbook. **Confirm the paper
stock you actually select and re-check against IngramSpark's spine calculator before
ordering** — spine width is the one dimension a reprint can't fix.

> **Front-cover art resolution — resolved.** Every cover now places its art at
> **375 dpi or better** (Scale & Silver 470), author photo 1080 dpi, barcodes ~500
> dpi. Scale & Silver's front was genuinely re-rendered at 2x (its type is vector,
> so it is truly sharp); Books One to Three were resampled to `-print` variants,
> which clears the spec but adds no detail — if a higher-resolution export of the
> original art appears, swap it in. See the per-book production notes.

### Known, accepted: the Ghostscript pass costs the text layer

`make_noicc.sh` converts the RGB build to grayscale/CMYK via Ghostscript, and
pdfwrite drops the fonts' ToUnicode mapping on the way through. Consequence: in the
**upload** PDFs, non-ASCII characters (em dashes, curly quotes, ©, ø) no longer
*extract* — `pdftotext` renders them as spaces. Verified: the RGB build extracts
"Søren Stromberg" and "©" correctly; the GRAY-noicc build does not.

**This does not affect printing at all** — every glyph renders correctly on the page;
only the invisible text layer is degraded. It also predates this pipeline: the
previously accepted files went through the same conversion.

It does mean the upload PDFs are poor for full-text search, copy-paste and screen
readers. If a genuinely searchable PDF is ever needed (an ARC, an accessibility
copy), ship the **RGB** build — its text layer is clean.

### Upload failures — "An error has occurred during the upload"

Hit 2026-09-01 uploading Scale & Silver. Generic message, tells you nothing about the
cause. Work through these in order; the files are almost never the problem.

1. **Use Chrome, not Safari.** IngramSpark's uploader has known problems in Safari —
   their own support steers people to Chrome, and Safari's cross-site tracking
   prevention breaks the upload widget. This is the first thing to try.
2. **Safari also mangles downloads.** Its "Open 'safe' files after downloading"
   setting auto-expands archives, and an EPUB *is* a zip — it will silently turn your
   `.epub` into a folder. Turn that off (Safari → Settings → General) before
   downloading anything destined for upload.
3. **Session expiry.** Log out completely, close the tab, log back in. Their tokens
   expire quietly and the upload is the first thing to fail.
4. **Title locked by a previous submission.** After a validation report — especially
   if you accepted the "we can correct this automatically" offer — the title enters
   processing and file controls lock until it clears. Check the title's status on the
   dashboard; cancel or wait before trying to replace files.
5. **Extensions.** Ad-blockers and privacy extensions break the widget. Incognito with
   extensions off.

**Rule out the files first, cheaply:** every file in `completed-books/` is checksummed
in `completed-books/MANIFEST.md`. Compare the byte size of what landed on your machine
(Finder → ⌘I) against the manifest. If it matches, the file is fine and the problem is
the browser, the session, or the title's state.

**Downloading from GitHub:** use the **Download raw file** button. Saving from the file
preview page gives you an HTML page with a `.pdf` name, which is rejected instantly.
