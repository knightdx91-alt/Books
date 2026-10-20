# Sygl — Pipeline Progress / Handoff

Workflow: book-* agents do the writing. Per chapter loop:
**book-writer → book-evaluator (8.5 gate) → book-editor (only if gate fails) → commit+push to `main`.**
Everything strictly on `main`. No PRs.

## 2026-10-20 re-plan (author ruling)
"Make it more like my original script. And it's supposed to be Sygl." The blueprint was rebuilt:
`project/outline.md` is now **30 chapters in source order (≈91,400 words)**, `project/foundation.md` and
`project/STYLE_CONSTRAINTS.md` were rewritten, and every ruling is recorded in `STATE.yaml` → `decisions`.

## Hard constraints (full list in STYLE_CONSTRAINTS.md)
- **Sygl / sygl / sygls / sygl-less** — never sigil/sygil. Mausoleum. Naisura.
- Follow `Sygl_Complete.txt` **in its order**; expand summary to scene; no invented plot, friction, motives,
  quirks or backstory; keep each scene's meaning and the happy ending.
- PAST tense, **close third on Bal only**; report what he doesn't witness. No dual narration in prose.
- **NO TICS** (sole exception: Amelia may call Bal "Master"). Em dashes ≤2/1k (target ~0). "the way [x]" ≤2/chapter, staggered.
- Fade-to-black.

## Status
| Ch | Title | Target | State |
|----|-------|--------|-------|
| 1 | The Roof and the Flicker | 3,800 | FINAL 2026-10-20: 3,196w, Floor 8.5 |
| 2 | The Queen in the Temple | 4,200 | FINAL 2026-10-20: 2,744w, Floor 8.5 |
| 3 | A New Hand | 3,200 | FINAL 2026-10-20: 2,601w, Floor 8.5 |
| 4 | Mrs. Brown | 3,000 | FINAL 2026-10-20: 3,268w, Floor 8.5 |
| 5–30 | see outline.md | — | TODO |

## RESUME HERE: Chapter 5 "Verin's Cottage" (source [pp.17–25], L259–284)
- Pierre (an orphan who helps Mrs. Brown) wakes Bal at six; then the outline's Ch.5 beats in source order.
- Author's dialogue is the base; polish into natural speech without changing meaning or speaker.

## Key files
- Source of truth: `Sygl_Complete.txt`
- Blueprint: `project/foundation.md`, `project/outline.md` ([pp.] + source line ranges + word targets)
- Constraints: `project/STYLE_CONSTRAINTS.md`
- Diagnostics (historical, pre-re-plan): `project/baseline-evaluation.md`, `project/scores.md`
- Superseded drafts (not part of final): `superseded/`
