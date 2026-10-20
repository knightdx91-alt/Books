# Progress — Sygl
Normalized 2026-07-13. Existing work retained: project/ (foundation.md, outline.md, STYLE_CONSTRAINTS.md,
scores.md, baseline-evaluation.md, PROGRESS.md), manuscript/ (chapter-01..03.md), superseded/ drafts,
Sygl_Complete.txt. NOTE: chapters are flat in manuscript/ (chapter-01.md), not manuscript/chapters/.
## Resume point (updated 2026-10-20)
**Plan rebuilt to follow the author's original script** ("make it more like my original script. And it's
supposed to be Sygl."). `project/foundation.md`, `project/outline.md` (now **30 chapters, source order,
≈91,856 words** after the 2026-10-20 outline audit) and `project/STYLE_CONSTRAINTS.md` were rewritten; STATE.yaml records every ruling as a
2026-10-20 author decision.

- **Ch.1–6 FINAL** (`manuscript/chapter-01..06.md`, 18,509w): written/rewritten to the source 2026-10-20, all
  four mechanical gates clean, book-evaluator Genesis Floor 8.5 each (reports in `evaluations/`).
- **RESUME HERE → Chapter 7 "The Blood Dorm"** (outline Ch.7). Open after Ch.6's "We'll talk more about it
  tonight" (don't repeat it). Viridia introduces herself and Bal recognises her as the girl from the buggy (one line);
  she sticks her tongue out once, answering the hair joke (author decision).
- Dialogue rule (2026-10-20): the author's lines are the base; polish grammar/stiffness into natural speech,
  keep meaning, speaker, placement and the memorable lines.
- Gate tools `voice_wear_check.py` / `tic_report.py` read `manuscript/chapters/`; this book is flat, so run them
  on a scratch copy laid out as `manuscript/chapters/chapter-N.md` (see CLAUDE.md).

## Manga adaptation — SET ASIDE (author, 2026-10-20: "disregard the manga")
Out of scope; not kept in sync with the prose. Notes below are historical only.

### (historical) Manga adaptation (parallel track)
See `sygl-manga/` for the illustrated version. Image generation works end-to-end via a personal RunPod
serverless endpoint (ComfyUI **5.8.5** + FLUX; the 5.8.6 build crash-loops — see sygl-manga/README.md).
First working Bal panel: sygl-manga/panel-bal-flux.png.

### Manga — state as of 2026-07-14 (session end)
DONE:
- Script (chapter-01-script.md), full 22-page STORYBOARD (chapter-01-storyboard.md, story-accuracy
  verified vs prose), cast sheet (chapter-01-cast.md), CHARACTER-LOCK.md.
- Visual style LOCKED: monochrome manga + spot-color sygls (element-colour map in README).
- LOCKED cast refs: REF-bal-preregrowth.png (stump, no sygl), REF-fredrick.png (pale hair/freckles,
  distinct from Bal), REF-posy.png (green Terra on palm), REF-statue-amelia-likeness.png (face hidden).
  Amelia deferred to Ch.2.
- Locked rules: STUMP-COMPOSE (isolate left arm for clean inpaint; never stack inpaints),
  SETTING/PROP CONTINUITY, and ORPHANAGE-GROUNDS GEOGRAPHY (mausoleum BEHIND orphanage, kids in
  FRONT yard, Bal ALONE) — all in the storyboard.
KNOWN-HARD: the flight splash (p.9) — one-shot generation can't satisfy all constraints (Bal alone +
tiny oblivious kids + sealed windowless mausoleum behind orphanage + free-floating rug + stump). Many
attempts in sygl-manga/ (flight-*, flightstory-*) are drafts, not final.
RESUME HERE → COMPOSITE the flight (author chose option A): (1) generate BACKGROUND plate (orphanage
+ sealed mausoleum behind + yard w/ tiny kids, no character); (2) generate Bal-alone-on-rug plate
(match REF-bal, left arm hanging into sky, clean stump via single inpaint); (3) LAYER them. Then
proceed page-by-page per the storyboard, then lettering.

INFRA: RunPod serverless ComfyUI+FLUX endpoint `lyistjk2ebyi0u` (Hub "ComfyUI 5.8.5", NOT 5.8.6).
Driven by API (see sygl-manga/README.md working config). ~$2.30 of $10 spent. NOTE: the RunPod API
key used this session is live — ROTATE/DELETE it in RunPod when done (never committed to repo).

### Manga consistency (open): plain FLUX drifts faces; using prompt-match + img2img from locked refs.
If drift is bad across full chapter, train per-character LoRA (Option B). Deferred.

### Dual-narration device — MANGA ONLY (decided 2026-10-20)
Bal narrates; Amelia butts into the narration (margin banter in a distinct caption-box style), Ch.1 solo-Bal,
from Ch.2 on. This stays **manga-only, if the author wants it there**. It is **not** used in the prose novel,
which is close third on Bal only throughout.
