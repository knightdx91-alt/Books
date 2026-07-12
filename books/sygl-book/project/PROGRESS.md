# Sygl — Pipeline Progress / Handoff

Workflow: book-* studio agents do ALL writing. Per chapter loop:
**book-writer → book-evaluator (8.5 gate) → book-editor (only if gate fails) → commit+push to `main`.**
Everything strictly on `main`. No PRs.

## Hard constraints (also in STYLE_CONSTRAINTS.md)
- Em dashes: **0** (source uses zero; even dialogue interrupts use ellipses/recast).
- Zero verbal tics; no repeated phrases/metaphors; "the way [x]" simile capped at <=6/chapter.
- PAST tense, close-third on Bal. Fade-to-black. Canon spellings (Naisura, mausoleum).
- Target whole novel **>= 90,000 words** (24-chapter outline totals ~92,300).

## Status
| Ch | Title | Words | Gate | State |
|----|-------|-------|------|-------|
| 1 | The Roof and the Flicker | 3,878 | 8.5 (after editor) | DONE, pushed |
| 2 | The Queen in the Temple | 4,055 | 8.5 (after editor) | DONE, pushed |
| 3 | A New Hand | 3,225 | 8.5 (first try) | DONE, pushed |
| 4-24 | see outline.md | — | — | TODO |

Cumulative final prose: **~11,158 words** (Ch.1-3).

## RESUME HERE (next session): Chapter 4 "Mrs. Brown" (target 3,800)
- Strongest thematic chapter (Mrs. Brown's late husband: late-surfacing water mark, firing, unsolved shooting; "they can't do it again"). DRAMATIZE, do not info-dump; grief via restraint/objects, never stated.
- Must be multi-scene/movement (Ch.1-3 were each single-scene; structural-diversity rule).
- Pick up from Ch.3's threshold ending (softball-game sound carrying forward).
- Avoid recycling images from Ch.1-3 (fishhook wrist-spike, coin-taste blood, frost-on-a-pane, ledge-grip bond, candle-pinch, wine-glass eyes, brown-of-old-bread).
- Do NOT state theme outright (that was the Ch.1-2 gate failure; Ch.3 passed by dramatizing).

## Key files
- Source of truth: `Sygl_Complete.txt`
- Blueprint: `project/foundation.md`, `project/outline.md` (24-ch map w/ per-chapter [Page] ranges + word targets)
- Diagnostics: `project/baseline-evaluation.md`, running scorecards in `project/scores.md`
- Constraints: `project/STYLE_CONSTRAINTS.md`
- Superseded hand-written drafts (not part of final): `superseded/`

## Note
The book-* agents are installed in `~/.claude/agents/` via the best-seller-studio repo's install.sh.
A fresh container will NOT have them — re-run `bash install.sh` from a clone of
github.com/felipelobomotta-blip/best-seller-studio if the book-* subagents are missing.
