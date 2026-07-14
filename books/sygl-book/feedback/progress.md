# Progress — Sygl
Normalized 2026-07-13. Existing work retained: project/ (foundation.md, outline.md, STYLE_CONSTRAINTS.md,
scores.md, baseline-evaluation.md, PROGRESS.md), manuscript/ (chapter-01..03.md), superseded/ drafts,
Sygl_Complete.txt. NOTE: chapters are flat in manuscript/ (chapter-01.md), not manuscript/chapters/.
## Resume point
3 chapters drafted; **Chapter 1 finalized 2026-07-14** (de-glossed theme → clears 8.5 gate; "the way"
tic trimmed 16→6; scorecard in project/scores.md). Next: same polish for Ch.2, then draft Ch.4 onward.
Also pending: fill STATE.yaml from project/foundation.md + outline.md; point canon_sources at project/;
decide whether to migrate manuscript/chapter-0N.md → manuscript/chapters/.

## Manga adaptation (parallel track)
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

### Dual-narration device (candidate — manga now, PROSE possibly)
Bal narrates; **Amelia butts into the narration** (margin-banter: teasing/correcting/adding
her 3,000 years of context). **Ch.1 is solo-Bal** (isolation theme + protects the reveal);
Amelia's whisper "Because it's magic" is her first intrusion and launches the device, which
runs from Ch.2 on. Currently locked for the MANGA (distinct caption-box style). OPEN: whether
to retrofit this into the prose chapters — decide before drafting Ch.2 prose.
