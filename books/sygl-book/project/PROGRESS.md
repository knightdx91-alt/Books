# Sygl — Pipeline Progress / Handoff

Workflow: book-* agents do the writing. Per chapter loop:
**book-writer → book-evaluator (8.5 gate) → book-editor (only if gate fails) → commit+push to `main`.**
Everything strictly on `main`. No PRs.

## 2026-10-20 re-plan (author ruling)
"Make it more like my original script. And it's supposed to be Sygl." The blueprint was rebuilt:
`project/outline.md` is now **30 chapters in source order (≈91,856 words after the 2026-10-20 audit)**, `project/foundation.md` and
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
| 1 | The Roof and the Flicker | 3,195 | FINAL 2026-10-20: 3,195w, Floor 8.5 |
| 2 | The Queen in the Temple | 2,731 | FINAL 2026-10-20: 2,731w, Floor 8.5 |
| 3 | A New Hand | 2,592 | FINAL 2026-10-20: 2,592w, Floor 8.5 |
| 4 | Mrs. Brown | 3,238 | FINAL 2026-10-20: 3,238w, Floor 8.5 |
| 5 | Verin's Cottage | 3,500 | FINAL 2026-10-20: 3,672w, Floor 8.5 |
| 6 | The Claiming | 2,800 | FINAL 2026-10-20: 3,081w, Floor 8.5 |
| 7 | The Blood Dorm | 3,600 | FINAL 2026-10-20: 3,650w, Floor 8.5 |
| 8 | Too Bad She's a Tempus | 2,400 | FINAL 2026-10-20: 2,344w, Floor 8.5 |
| 9 | The Familiar Class | 3,400 | FINAL 2026-10-20: 3,538w, Floor 8.5 |
| 10 | Hopper and the Rapier | 2,400 | FINAL 2026-10-20: 2,879w, Floor 8.5 |
| 11–30 | see outline.md | — | TODO |

## RESUME HERE: Chapter 11 "Break Their Toys"
- Open on Amelia's uniform details; don't restate Ch.10's last line. Follow outline Ch.11 in source order.
- Author's dialogue is the base; polish into natural speech without changing meaning or speaker.

## Key files
- Source of truth: `Sygl_Complete.txt`
- Blueprint: `project/foundation.md`, `project/outline.md` ([pp.] + source line ranges + word targets)
- Constraints: `project/STYLE_CONSTRAINTS.md`
- Diagnostics (historical, pre-re-plan): `project/baseline-evaluation.md`, `project/scores.md`
- Superseded drafts (not part of final): `superseded/`
