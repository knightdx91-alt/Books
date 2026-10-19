# Review checkpoint 2 — Chapters 6–10 (2026-10-19)

The loop has stopped here for you, as it does after every fifth chapter. Nothing after Ch.10 has been written.
The independent read of these five chapters is in `feedback/independent-review-ch6-10.md`; this file is the
pipeline's own record. **Four decisions are waiting for you at the bottom.**

## The five chapters

| Ch | Title | Words | Floor | Avg | Casual | CVI-L | Polish cycles | Continuity audit |
|---|---|---|---|---|---|---|---|---|
| 6 | Snow at the Cave Mouth | 6,639 | 8.5 | 8.57 | 9.0 | 9.4 | 1 | 1 CRIT / 19 WARN, all fixed |
| 7 | The Laws of Belonging | 6,122 | 8.5 | 8.64 | 8.5 | 9.3 | 1 | 2 CRIT / 20 WARN, all fixed |
| 8 | The Thyiades | 7,459 | 8.5 | 8.64 | 9.0 | 9.8 | 1 | 0 CRIT / 20 WARN, all fixed |
| 9 | The Polygonal Wall | 5,763 | 8.5 | 8.64 | 9.0 | 9.1 | 2 | 1 CRIT / 11 WARN, all fixed |
| 10 | Kallia's Letter | 2,446 | 8.5 | 8.57 | 8.5 | 9.3 | 2 | 1 CRIT / 9 WARN, all fixed |

Book so far: **10 chapters, 54,200 words**, every chapter at Floor 8.5; running average 8.59. On the
architect's budget the book projects to about 245,000 words, which is the target. Emotion reached 9.0 in
Ch.7, 8, 9 and 10; Immersion 9.0 in Ch.8 and 9.

Every chapter's **first** evaluation failed on Prose & Voice, each time for narrator moves the gates could
not yet see. After each one the gate was taught the move (see "What changed in the pipeline").

## Shape audit (strict) — CLEAN

| Ch | Words | Breaks | Dialogue | Median sentence | Opens | Ends |
|---|---|---|---|---|---|---|
| 1 | 6,466 | 3 | 31% | 11 | I-statement | quiet |
| 2 | 4,048 | 6 | 15% | 16 | narrative | long-fade |
| 3 | 5,609 | 0 | 6% | 17 | long-spiral | punch |
| 4 | 1,821 | 7 | 17% | 10 | short-punch | dialogue |
| 5 | 7,843 | 4 | 20% | 17 | scene-set | long-fade |
| 6 | 6,639 | 2 | 38% | 11 | I-statement | dialogue |
| 7 | 6,122 | 3 | 22% | 17 | narrative | question |
| 8 | 7,459 | 0 | 28% | 15 | dialogue | quiet |
| 9 | 5,763 | 5 | 28% | 15 | narrative | punch |
| 10 | 2,446 | 0 | 40% | 15 | short-punch | quiet |

Lengths 1,821–7,843 (max÷min 4.3); dialogue 6–40%; no opening or ending used more than three times in ten.

## Tic and gesture gate — CLEAN

- No phrase recurs 3+ times book-wide outside the allowlist. No spoken refrain. No command echoed back as
  compliance beyond the three the book allows.
- Narration habits, Ch.6–10: and-chains 1–5 (cap 9); credential asides 0–1 (cap 4); negation pivots 0;
  "So…" openers 0 in Ch.7–10 (it ran Ch.2–6); "before I had decided" 1 (Ch.7).
- Gestures: **bending to the work 0.28 per 1,000 words, just under the 0.30 limit** — Ch.11 should carry none.
  Object handling 0.17; every other class 0.04 or less. "A long moment" appears twice in 54,000 words.
- Not gated, your decision below: kneeling and crouching at 0.46 per 1,000.

## Open items in ENTITY_STATE

23 open, all low or info severity; none blocks writing. The ones that matter for the next chapters:
- **CH10-6** — when Ariston left (the page doesn't say), which bears on Kallia's "no other name on that line for years".
- **CH6-5** — Mara knows the plain-to-cave route but not the town-to-plain one; settled on the page, logged for reference.
- **CH8-2** — the crows woman (Theano) is texture only so far; Ch.13 recognises her by situation.
- **P3 / P4** — two outline-level questions for Ch.35 and Ch.38/43 (when Fenn learned of the door; the fate of
  his original tables). They will need settling before those chapters, not now.

## What the bible's at-risk list grew by

Each chapter added a dated block of spent and capped moves. Since Ch.5 the list has gained:
- Valens: answering closeness with a practical order (spent until Ch.12); Mara noticing his hands outside a task
  (spent until Ch.11); "Men will come asking" (used once, never again); footing orders (watch).
- Kallia: "Then…" retorts (≤1/ch); chore replies (≤1/ch); walking off (watch); asking for a name (at 2, no third).
- Narrator: the "So/Then/After that" hinge family; "before I had decided"; command echoes; callback pointers;
  the lying-awake coda (spent); the memory paragraph that ends on a dry kicker (spent); cloth smelling of
  another woman (spent); the room going quiet when she speaks (spent); "looked at me then" (spent).
- Set pieces: the cave in its Ch.3 words (spent); men at a public place doing the arithmetic (spent); the
  address-and-zip-code walk (spent); **whole set pieces rebuilt from the chapter just finished** (new risk).

## What changed in the pipeline (every book inherits these)

- `tic_report.py` finds chapters from its own folder, so a run from the repo root no longer silently checks nothing.
- New gate layers: negation pivots; the hinge family of paragraph openers; "before I had decided"; a bending class;
  a gesture cap that fails when reached and is checked per chapter.
- The echo scan now also reads the voice-bank samples, lists command-echo candidates, and catches
  pronoun-swapped echoes ("She stayed where she was" → "I stayed where I was").
- The voice-wear check ignores header comments.
- The editor spec: a recast must not move a repeat sideways.

## The three things most worth reading

1. **Ch.10, the whole chapter.** It is short, and it is the best thing in the book so far.
2. **Ch.8, from "Then everybody took off her shoes" to the end.** The sandals, "I lost him on the boat", the stranger's cloak.
3. **Ch.6, the bread.** "He had carried it the whole climb inside his clothes, against his skin, and it was exactly the temperature of a person."

## Decisions waiting for you

1. **Valens.** He has had one real scene in 54,000 words. The next chapter in the plan is "Valens's Yard". Should it be
   a full two-hander, with the plot moving from here (Celer's men are Ch.12)? The independent read says yes.
2. **The Philadelphia memory inserts.** A short 1990s memory paragraph appears in nearly every chapter. Cap them at
   one every other chapter, and never end one on a lost name?
3. **Kneeling and crouching** (0.46 per 1,000). Leave it as character (the cave crack; Kallia never sits), or gate it?
4. **The line in Ch.10.** "It was the best Greek I had spoken since October, and it was his from beginning to end"
   became "Kallia corrected none of it. The Greek was his, from beginning to end." The evaluator ruled the first
   half a habit. Keep the change, or restore the original?

Say **"continue"** (with any answers) and the loop resumes at Ch.11.
