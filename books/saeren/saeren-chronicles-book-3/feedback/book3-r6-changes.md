# Book Three — r5 → r6 changes log
**Date:** 2026-07-15 · **Build:** r6 (20 ch; word floor held at 111,688 w; r5 kept as history)
**Driver:** SUBTRACTION-ONLY de-ticking pass — the same literary-preserving line work r4 did to
Act Three, now applied to the tics the r5 beta panel (`feedback/beta-panel-r5-2026-07-15.md`) and
r5 evaluator (`evaluations/full-book-eval-r5-2026-07-15.md`) named. Pure deletion / light recasting
to concrete sensation-action of over-repeated signature phrases. **No structure, canon, plot, or
scene order changed.** Each motif's load-bearing instances preserved.

## Targets — before → after (per chapter)

### 1. "the cold working part" — front-half thinning (r4 had cleared Act Three to 0)
Book-wide **43 → 16.** Kept ~1 load-bearing instance per chapter (the one doing real character work);
converted the rest to concrete action ("she was filing it already," "she counted while she ran,"
"the reckoning," "some cold part of her") or cut.
| Ch | before | after | keeper |
|----|:--:|:--:|--------|
| 1  | 3 | 1 | l57 — the phrase's introduction/definition |
| 2  | 5 | 1 | l63 — "had a word for everything… reached for a word and found nothing" |
| 3  | 3 | 1 | l109 — the river-district temptation reach |
| 4  | 2 | 1 | l139 — the high-wall accounting |
| 5  | 5 | 1 | l151 — "made herself do the cold working part one more time" |
| 6  | 2 | 1 | l113 — "not in time for the next one" |
| 7  | 4 | 1 | l77 — "did the sum and set it down" at the fount |
| 8  | 2 | 1 | l131 — reads the tide twice/three times |
| 9  | 3 | 1 | l91 — holds the grief on the mountain |
| 10 | 7 | 4 | LIGHT TOUCH per brief (sanctioned peak): kept l27/l29/l37 (bins-vs-sight core); recast l19/l81/l87 to "the cold" |
| 11 | 3 | 1 | l51 — "flat grammar of the cold working part" |
| 13 | 1 | 1 | untouched (Act-Three load-bearing synthesis) |
| 20 | 3 | 1 | l23 — "could feel the cold working part reaching for it" (temptation refusal) |

**Ch.5 / Ch.7 / Ch.9 note:** only individual surplus tic PHRASES removed (4 / 3 / 2 respectively).
**No scene merged, moved, re-ordered, or restructured** — the Ch.5→7→9 corridor architecture is
untouched and survives any later restructure proposal.

### 2. Migrated finale tics
- **"the doorpost" (prose):** Ch.15-20 **18 → 9.** Eliminated every stacked doublet/triple
  ("the second warmth, the doorpost, the line…") down to a single term; kept the defining promise
  (Ch.15 "I'll be the doorpost" / "We're the doorpost"), both hand-on-doorpost similes (Ch.18 l43,
  Ch.19 l45 — the evaluator's explicit keeps), and single anchor uses (Ch.18 l103 "the doorpost held,"
  Ch.19 l129 "held, sleeping," Ch.20 l161 "snapping taut").
- **"the second warmth" (prose):** Ch.15-20 **10 → 8** (the stack-trims that dropped a paired term).
  Combined doorpost+second-warmth wallpaper **28 → 17**; the cosmology/character marker and every
  payoff kept, the metronome broken.
- **"the slow way" — Ch.20 8 → 2.** Kept the two load-bearing (Alice's teaching-way; the finale
  void-contrast at l157, which pays off the socket ending). Recast the rest to concrete variation
  ("unhurried," "easing to its edge," "the long road," "hand over hand," "a degree a year, to its edge").

### 3. Ch.6 Sela scene (the book's first grief-landing — needs the reader close)
- **"the careful surface" 8 → 2** (kept l45 primary grief statement + l139 chapter-close; recast the
  six distancing repeats to concrete "kept her face still / flat / held").
- **"did not weep" 4 → 2** (per evaluator: kept l45 opening + l83 "carried Sela down"; dropped the
  l45 internal echo and the l61 restatement). Grief landing preserved.

### 4. Pattern #11 — "the way you…" self-completing simile (evaluator's named pass, Ch.17-20)
Cut the least load-bearing connective ones; kept every simile carrying a real image.
| Ch | before | after | cut |
|----|:--:|:--:|-----|
| 17 | 6 | 4 | l7 "set your feet before a wave" (recast); l89 doubled "take up a post" (→ one) |
| 18 | 6 | 4 | l19 second "hand tightens on a rope" (recast, non-second-person); l93 "feel a tide turn" (recast) |
| 19 | 9 | 5 | l7 "small frightening thing you have put off"; l11 first "feel a thing you have learned to feel"; l47 "brace a thing that might go over"; l97 "feel a goodbye coming" |
| 20 | 4 | 4 | untouched — already at the literary line; images (missing-stair, missing-tooth) pay off the void finale |
Kept (Ch.19): the "key to a lock," "people you love when they do not know they are seen" (l39),
the doorpost simile (l45), "lamp in a window" (l53), Drake's dialogue "the way you can, I'd wager"
(l99). Ch.19 now 1.53/1K → ~0.85/1K.

## Gates (all green, whole book)
- `python3 tools/style_check.py`: **RESULT: clean** (em-dash ≤4/chapter holds; no NEW cross-chapter
  repeated phrase introduced — recasts were varied, concrete, under ceiling).
- `python3 tools/grammar_check.py`: **RESULT: clean** (0 errors; long-sentence notes pre-existing, non-gating).
- `python3 tools/rhythm_check.py`: **30 → 30** — identical to the r4/r3 baseline, no new flat triplets.
- Word floor (95k): clear at **111,688** (r5 was ~111,853; ~165 words net cut, all tic deletions).

## Canon / continuity
No canon moved. All guardrails intact: balance-not-victory; void/Fen finale unexplained; no public
weeping (the two sanctioned breaks — Bk2 Ch.16, Bk3 Ch.10 — untouched); Raizen dark ordinary eyes;
source = physical Book-One cavern; doorpost/second-warmth cosmology and the socket ending preserved.
The Ch.5/7/9 corridor scene architecture was NOT touched (subtraction of surplus tic phrases only),
so it survives any later corridor-restructure proposal. No Book-One/Two touchpoint altered.
</content>
