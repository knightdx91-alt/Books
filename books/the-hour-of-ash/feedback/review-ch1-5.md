# Review checkpoint 1 — Chapters 1–5 (2026-10-19)

The loop is paused here for your evaluation. Say **"continue"** in any session to resume at Ch.6.
Everything below is measured from the finalized text on `main`.

## What you have

| Ch | Title | Words | Floor / Avg / Casual / CVI-L | Polish cycles | What held it down first time |
|---|---|---|---|---|---|
| 1 | The Reception | 6,473 | 8.5 / 8.57 / 8.5 / 9.0 | 2 | chain sentences; an inventory-look form that was a tic forming |
| 2 | Fenn's Notebook | 4,069 | 8.5 / 8.57 / 8.5 / 8.8 | 1 | a counter-tears beat repeating Ch.1; "without" ×4; a handling cluster |
| 3 | Parnassus | 6,817 | 8.5 / 8.57 / 8.5 / 8.7 | 1 | five book-law repeats; three real continuity errors |
| 4 | The Goats Saw Me First | 1,821 | 8.5 / 8.50 / 8.5 / 8.9 | 1 | five cross-chapter repeats; two capped shapes at a third use |
| 5 | The Sanctuary | 8,184 | 8.5 / 8.57 / 8.5 / 8.7 | 1 | nine cross-chapter repeats, two banned by name; one critical third-use |

**Total: 27,442 words** of the ~245k plan (Σ 260,300 budgeted). Running average 8.56. Immersion
(Dimension 7) scored 9.0 on Ch.1, 3 and 5. Foreshadowing: 0 on every chapter (the year is dated in Ch.5
as a present inference; no 79, no Pompeii, no "nine years"). Tics: 0 on every chapter, gestures included.

## Shape (the anti-predictability audit, strict mode: CLEAN)

```
  ch  words brk  dlg%  med open         end        first → last line
   1   6473   3    31   11 I-statement  quiet      "I had been at my father's memorial rec" → 'Every second or so the red light came '
   2   4069   6    15   16 narrative    long-fade  '*Thanksgiving, 1967, and Margaret has ' → 'Back before Labor Day, and Margaret ca'
   3   6817   0     6   18 long-spiral  punch      'The thyme grew in low gray cushions up' → 'I stepped out into October.'
   4   1821   7    17   10 short-punch  dialogue   'The goats saw me first.' → '"Nymphē."'
   5   8159   4    21   17 scene-set    long-fade  'It was most of a day down the mountain' → 'Somewhere among the jars a mouse had f'

length: min 1,821 / median 6,473 / max 8,159 / CV 0.41 / max÷min 4.5
dialogue share: 6–31% (CV 0.47);  opening sigs: I-statement×1, long-spiral×1, narrative×1, scene-set×1, short-punch×1;  ending sigs: dialogue×1, long-fade×2, punch×1, quiet×1
```

Five chapters, five different openings (an I-statement confession, an italic 1967 document, a 79-word
sensory spiral, a 5-word flat fact, a time-phrase), four different endings (a quiet image, a document
fade, a 5-word punch, a spoken word, a 66-word fade). Lengths run 1,821 → 8,184. Dialogue 6% → 31%.
Scene breaks 0 → 7. **Watch:** the long-fade ending is already at 2 of 5; the ledger will not use it
again before Ch.8.

## Tics and gestures (the no-tics law, book-wide)

```
GESTURE BEATS — stage business by class (book-wide; a repeated gesture is a tic):
     6x   0.22/1k  worst ch 1: 4x   object handling (set down / put down / pick up / take out / put back / hold out / turn over)
     2x   0.07/1k  worst ch 1: 2x   nod
     2x   0.07/1k  worst ch 1: 1x   'a (long) moment'
     1x   0.04/1k  worst ch 3: 1x   swallow
     1x   0.04/1k  worst ch 2: 1x   breath beat (let out a breath / exhaled / breath caught)
     1x   0.04/1k  worst ch 1: 1x   turn away / turn back
     1x   0.04/1k  worst ch 5: 1x   head shake
```

No class is near its cap (object handling peaked at 4 in Ch.1 and has been trimmed to 6 across the
whole book; "a long moment" 2; nod 2). The three catches worth knowing about:
- **A device-turning pattern** (a character turns to a TV / a phone instead of Mara) appeared in
  Ch.1, Ch.2 and was about to appear a third time in Ch.3's goatherd. Cut in the disruption pass; on the
  at-risk list.
- **Kallia's "always something in her hands"** drifted into four lamp-handling beats in the Ch.5 draft;
  dialogue-polish cut them to one. Her work is now tasks and results, not business between lines.
- **Cross-chapter echoes** were the holdout on every chapter's first evaluation (the 3+ gate fires one
  use too late). Added an **echo scan** (`tic_report.py --echoes N`) that lists every distinctive
  phrase a new chapter repeats from an earlier one at its *second* use. Ch.5 went from 28 echoes to 6,
  all functional (a date payoff, two street names, a continuity pickup, one coincidental n-gram).

## The at-risk list (character-bible.md)

Three dated blocks now: after Ch.1 ("Which one stops it?" spent; "the [color] of [thing]"; item-by-item
looks; "Then you…"; TV-turning), after Ch.3 (device-turning closed; "My [part] went hot"; "you could
have"; "wristbone"; "Then…" pivots; negation endings), after Ch.5 ("longer than [X] needed/deserved"
spent; the stranger-gaze "with [his/her] eyes on my [X]" ≤1 per chapter; "in English" as a tag ≤2; "took
me by the [garment]" spent; Baltimore Avenue / Walnut Street / Chestnut at 3 each; body-unit measures
≤4; the microcassette touch at 2 of its 4 planned; "the ninth of June" spent).

## Open contradictions (ENTITY_STATE.yaml, all minor plan-vs-prose, prose wins)

CH1-2 Szabo's magnifier vs glasses (bible updated) · CH1-3 Szabo never names Fenn (plan said she did) ·
CH2-1..6 (nine weeks not eight; "first" dropped; the flash unit never mentioned; notebook-in-coat not
stated; bible paraphrases; Pentax packing implied) · CH3-1..3, CH3-7 (order of Fenn's breaths; the
doorway drawing's size; no 1998 refuge hut — Ch.4 used the stone pen; narration names no "door") ·
CH4-2..4 (pouch of two bars vs single; "fleece" vs "jacket"; ΠΑΝΙ vs ΠΑΝ) · CH5-2, CH5-3 (bible lines vs
prose; the unplanned frame shown on the page). None blocks anything; none involves canon.

## Decisions the architect made that you have not yet ruled on

Logged as ARCH-1..18 in STATE.yaml. The ones that have now reached the page: Philadelphia / Mara is
American (Ch.1); the crossing at the Corycian Cave (Ch.3); Fenn's coordinates from an Army map at the
Free Library (Ch.2); the goat-boy mistakes her for a nymph (Ch.4); Kallia takes her in as unpaid help
(Ch.5). Still ahead and overridable: the door as a tomb outside the Nuceria Gate; the Oracle speaking to
her in person after Valens carries the question in (Ch.13); Fenn as "Augurinus" in Puteoli; the
24–25 August eruption date.

## The three things most worth reading

1. **Ch.4 whole** (1,821 words, ten minutes). It is the book's first structural shock and the purest
   test of the no-tics law: eight shards, a child who dislikes her snack, "Nymphē." alone at the end.
2. **Ch.5, the Sacred Way section** (from "Below the gate the town opened…" to the temple steps). This
   is where the authenticity dial is set: the looted bases, the painted temple she finds ugly, her shame
   at being disappointed. If the immersion register is wrong for you, it is wrong here.
3. **Ch.1, the answering machine** (the last 800 words). The anchor "Mara? Which one stops it?" and the
   quiet 23-word close. If the narrating stance (first person, in order, never reaching forward) feels
   right here, it holds everywhere.

## If you want changes

Say what, in any session. A note like "Kallia is too soft" or "cut the fountain men in Ch.5" becomes an
editor pass with a re-evaluation; a canon change goes into STATE.yaml first. Otherwise: **"continue"**.
