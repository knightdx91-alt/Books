# Production Notes — The Saeren Chronicles, Book One: Hazel Academy

## Assembled file

`manuscript/full-manuscript.md` — title page + all 18 chapters in order, concatenated from the finalized chapter files.

## Counts

- **Chapters:** 18 (complete).
- **Final assembled word count (full-manuscript.md):** **84,911 words.**
- **Source chapter files total:** 85,115 words. The ~200-word difference is non-prose scaffolding removed during assembly: 18 markdown `# Chapter N:` heading lines and 17 `<!-- … -->` editorial metadata comments. **No narrative prose was cut.** Measured as a manuscript, the book sits at the ~85,000-word floor; the per-chapter source total (85,115) remains above the hard floor in STATE.yaml.

## Assembly / formatting applied

- Title page: "THE SAEREN CHRONICLES / Book One: Hazel Academy."
- Each chapter rendered with a clean two-line heading: `CHAPTER [WORD]` + the chapter title (titles taken from the chapter files / outline.md). Chapter 1's draft-era status preamble ("Working Manuscript… Status Note…") and the `[END OF CHAPTER ONE — Session 1]` marker were dropped; its prose begins at the true opening line.
- Per-chapter markdown headers and HTML metadata comments stripped from the body.
- Scene-break markers normalized: the chapters' in-text dash dividers (`———`) were converted to a consistent `* * *` scene break throughout. Inter-chapter dividers collapsed so the CHAPTER heading itself is the break (no stray `* * *` stacked against a chapter heading).
- Whitespace normalized (no runs of 4+ blank lines).

## Proofread pass (copyedit level only — no rewriting)

A full read of all 18 chapters plus targeted consistency searches was performed. **The manuscript was already clean; effectively no copyedits were required.** Specifically verified:

- **Canon spellings consistent throughout:** Pembrook, Jazen (no "Jasen" slip anywhere), Viridia Saeren, Lor-ar, Raizen, Isolde / Lady Lightwell, rose-tinted. ✓
- **Character-name consistency:** Jazen's sister is "Jan" (ch.15, ch.17) — consistent. Lightwell = Isolde throughout. Amber Summers, Mrs. Zoran, Drake, Varissa, Nargash, Venquar, Quina, Tobias, Coram, Brutus, Hiram/Abe consistent. ✓
- **The High Chancellor is unnamed in the manuscript** (referred to only by title) — preserved as written; no name invented in the assembled text.
- No typos, doubled words, homophone errors, or punctuation slips found that required correction. Interrupted-dialogue em-dashes and the deliberate motifs (the thread in the well, the empty space the size of Alice, "no one sees you do it / you decide who sees") left intact as authorial style.

## Outstanding / not done here (non-blocking)

- No EPUB/print binary was generated (no platform specified). The assembled markdown is the production master; convert to EPUB/PDF once a target platform (KDP / IngramSpark / Apple Books) and trim size are chosen. Recommended defaults are in `~/.claude/agents/book-packager.md` (5.5×8.5 trade paperback; serif body; `* * *` scene breaks; chapter heads page-break-before).
- Front/back matter beyond the title page (copyright, dedication, acknowledgments, about-the-author) not added — supply when publishing details exist.

## r16 (2026-09-01) — "Also by" page
Front matter gained an **"Also by Post Peleos"** page on the verso facing the title
page, matching Books Two and Three: the three Saeren titles, then under a rule the
adult line — *A Bond of Scale and Silver* by **Søren Stromberg**, labelled 18+ and
marked as not part of this series. It fills what was a blank verso, so the book is
still **294 pages** and the existing cover wrap is unchanged and still valid.
Deliverables: `...-interior-r16.pdf`, `...-interior-r16-PDFX1a.pdf`, and a rebuilt
`../ebook/Saeren-Chronicles-Book-One-Hazel-Academy.epub`.

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
