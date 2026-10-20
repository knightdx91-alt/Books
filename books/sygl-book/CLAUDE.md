# CLAUDE.md — Sygl

Per-book playbook. A fresh Claude Code session should read this first, then `STATE.yaml` and
`feedback/progress.md`. The shared pipeline lives at the repo root (`.claude/`, `tools/`, `docs/`);
never copy it in here. We work only on `main`.

## What this is
A revise/expand project: the author's original script `Sygl_Complete.txt` (~49.7k words) becomes a
≈91k-word novel in 30 chapters, **following the script in its order**. Author direction (2026-10-20):
"make it more like my original script. And it's supposed to be Sygl."

## Project layout
```
books/sygl-book/
├── STATE.yaml                 # READ FIRST — state, decisions, open questions
├── Sygl_Complete.txt          # SOURCE OF TRUTH (pp.16–50 and 71–186 carry [Page] markers)
├── project/foundation.md      # canon lock, premise, theme, character cards (no tics)
├── project/outline.md         # binding 30-chapter plan: [pp.] + source line ranges + targets
├── project/STYLE_CONSTRAINTS.md
├── manuscript/chapter-NN.md   # the book (flat layout)
├── feedback/progress.md       # exact resume point (+ manga track notes)
├── sygl-manga/                # SET ASIDE by the author (2026-10-20); out of scope, ignore
├── superseded/                # old drafts, not part of the book
└── tools/                     # style_check.py, grammar_check.py, tic_report.py, voice_wear_check.py
```

## How to continue
1. Read `STATE.yaml` and `feedback/progress.md`.
2. Write the next chapter IN ORDER from its outline entry, working from the cited source lines.
   Revise/expand the source; do not invent.
3. Gate: book-evaluator ≥ 8.5, `python3 tools/style_check.py`, `tic_report.py --gate`,
   `voice_wear_check.py`. Then commit to `main`.

## Canon guardrails (settled author decisions — never violate)
- **Spelling: Sygl / sygl / sygls / sygl-less.** Never "sigil" or "sygil". Also mausoleum, Naisura (never
  "Waisura"), Viridia Vizer, Balthazaar "Bal" Norheart, The Heir's School of Magykal Artes.
- **Source order is plot order** (`project/outline.md`). The day-two cluster (Raizen's army, "break their
  toys", Peter, the hidden temple, Thad & Xavier, the ring, the diary, "I like you too") precedes New Spring
  and the Card; Amelia's origin and the convert-Viridia proposal follow Viridia's first appearance; Fern's war
  room and the Londra priests precede the rule and conversion; war rules appear where the source reveals them.
- **No invented plot, friction, motives, quirks or backstory.** The girls' choice is shown through the source's
  own beats (the diary and "I like you too", the juggling talk, the willing conversions).
- **Tone as the source:** Bal's violence against those who threaten his girls is justified (Iro hangs from the
  blood whip); Amelia loves and protects her own and manipulates no one; the conversions are free choices; the
  ending is unambiguously happy ("the first day of the rest of their life together").
- **Premise:** Bal converts willing loved ones (and Toma by accident); not "stealing other gods' followers".
- **Canon facts:** Mrs. Brown's husband's late affinity was **Blood** (fired so the factory wouldn't be "seen
  as a blood mage supporter"); sygls are **on the palm**; Bal has a **high pain tolerance**; other orphans have
  no magic at all; Fredrick was a **friend**; Amelia's familiar brand is on her forehead and can be hidden.
- **POV:** close third on **Bal only**, PAST tense. What he doesn't witness is reported, as the source reports
  it. No dual narration.
- **NO TICS** (repo law 2026-10-18): distinguish characters by worldview, syntax, evasion, physicality.
  **Explicit exception (author ruling 2026-10-20): Amelia may call Bal "Master"** — a legitimate title from a
  familiar to her bonded mage — where the source uses it or the relationship makes it natural. All other
  catchphrase/tic allowances are gone.
- **Dialogue:** Author's dialogue is the BASE, not sacred text (author, 2026-10-20: "my dialogue might not be exactly right"). Keep what each line says, who says it, and where it falls, plus the memorable lines (e.g. "They have made me a myth?!", "Because it's magic", the binding vows, "No one threatens my girls"). Freely fix grammar, stiff or awkward phrasing, and anything that doesn't sound natural spoken aloud. Do not change meaning, add information, or give a line to someone else.
- Fade-to-black. Keep separate from the-fourfold-crown.

## Open author decisions (ask, don't invent)
None open (all resolved 2026-10-20; see `STATE.yaml` → `decisions`). New questions go in `open_author_decisions`.

## Status (update as you go)
- 2026-10-20: blueprint rebuilt to source order (30 chapters, ≈91,856 words after the outline audit).
- Ch.1–10 FINAL 2026-10-20 (30,918w): rewritten to the source; all gates clean; Genesis Floor 8.5 each.
- **Next: Ch.11 "Break Their Toys"** (see project/outline.md). Open on the uniform details; don't restate Ch.10's last line.
- Gate tools voice_wear_check.py / tic_report.py read `manuscript/chapters/`; run them on a scratch copy laid out
  that way (the book uses flat `manuscript/chapter-NN.md`).
