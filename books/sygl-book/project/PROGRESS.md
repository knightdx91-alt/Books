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
| 11 | Break Their Toys | 3,800 | FINAL 2026-10-20: 3,709w, Floor 8.5 |
| 12 | I Like You Too | 1,500 | FINAL 2026-10-20: 1,455w, Floor 8.5 |
| 13 | New Spring | 5,300 | FINAL 2026-10-20: 5,557w, Floor 8.5 |
| 14 | The Card | 2,600 | FINAL 2026-10-20: 2,556w, Floor 8.5 |
| 15 | Rumors | 1,800 | FINAL 2026-10-20: 1,948w, Floor 8.5 |
| 16 | Whitehaven Road | 4,800 | FINAL 2026-10-20: 4,786w, Floor 8.5 |
| 17 | Saegen Woods | 2,700 | FINAL 2026-10-20: 2,616w, Floor 8.5 |
| 18 | Six Weeks | 2,800 | FINAL 2026-10-20: 2,718w, Floor 8.5 |
| 19 | The Rule | 2,600 | FINAL 2026-10-20: 2,465w, Floor 8.5 |
| 20 | The Blood Whip | 2,600 | FINAL 2026-10-20: 2,729w, Floor 8.5 |
| 21 | Strawberries | — | FINAL 2026-10-21: 3,379w, Floor 8.5 |
| 22 | The Plan | — | FINAL 2026-10-21: 3,576w, Floor 8.5 |
| 23 | Road to Londra | — | FINAL 2026-10-21: 2,187w, Floor 8.5 |
| 24 | The Winespring Inn | — | FINAL 2026-10-21: 4,905w, Floor 8.5 |
| 25 | The Three Boars | — | FINAL 2026-10-21: 3,208w, Floor 8.5 |
| 26 | Together | — | FINAL 2026-10-21: 1,723w, Floor 8.5 |
| 27 | Thunder from a Clear Sky | — | FINAL 2026-10-21: 4,246w, Floor 8.5 |
| 28 | The Chalice | — | FINAL 2026-10-21: 2,790w, Floor 8.5 |
| 29 | Blood Elemental | — | FINAL 2026-10-21: 3,760w, Floor 8.5 |
| 30 | The First Day | — | FINAL 2026-10-21: 1,596w, Floor 8.5 |

## RESUME HERE: full draft complete
- Author read-through; closing line provisional. Then optional full-manuscript eval, continuity audit, packaging.

## Key files
- Source of truth: `Sygl_Complete.txt`
- Blueprint: `project/foundation.md`, `project/outline.md` ([pp.] + source line ranges + word targets)
- Constraints: `project/STYLE_CONSTRAINTS.md`
- Diagnostics (historical, pre-re-plan): `project/baseline-evaluation.md`, `project/scores.md`
- Superseded drafts (not part of final): `superseded/`
