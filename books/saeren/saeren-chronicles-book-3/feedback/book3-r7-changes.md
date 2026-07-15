# Book Three — r6 → r7 changes log
**Date:** 2026-07-15 · **Build:** r7 (20 ch; word floor held at 111,618 w; r6 kept as history)
**Driver:** AGGRESSIVE book-wide tic-cap pass per author's standing rule (overrides the r5
evaluator's "protect the cold-working-part as through-book identity" note): **no signature
narrative tic-phrase may appear more than 2–3 times across the ENTIRE book** (≤4 for the
finale doorpost/second-warmth cosmology cluster, its floor). Pure deletion / concrete-varied
recasting. **No structure, canon, plot, or scene order changed.** Ch.5/7/9 corridor architecture
untouched (only surplus tic phrases capped). Each tic's highest-value load-bearing instances kept.

## Per-tic book-wide counts (prose) — before → after, with keepers

| Tic phrase | before | after | keepers (load-bearing instances retained) |
|---|:--:|:--:|---|
| "the cold working part" | 16 | **3** | Ch.1 l57 (introduction/definition); Ch.10 l29 (the gut-punch failure — the part that files cannot file a *sight*); Ch.20 l23 (the final temptation reach, refused) |
| "did not weep" | 15 | **3** | Ch.6 l45 (Sela grief-landing); Ch.10 l35 (the sanctioned private break); Ch.19 l131 (finale close) |
| "the careful surface" / "careful surface" | 14 | **3** | Ch.1 l129 (introduction/definition); Ch.8 l143 (the Marick-valley flat voice); Ch.13 l151 (the cost-declaration dialogue) |
| "the slow way" | 12 | **3** | Ch.4 l117 (Alice's teaching-way, the seed of the payoff — one kept of five); Ch.20 l77 (the payoff bookend); Ch.20 l157 (the finale void-contrast) |
| "the doorpost" | 8 | **3** | Ch.15 l113 ("I'll be the doorpost… forever"); Ch.15 l135 ("We're the doorpost. Walk."); Ch.20 l161 (the void-socket finale, snapping taut) |
| "the second warmth" | 9 | **1** | Ch.15 l113 (the defining promise; shares the line with the doorpost) |
| **doorpost + second-warmth CLUSTER** | 17 | **4** | (3 + 1 above — at the ≤4 floor) |
| "born and gone" | 6 | **3** | Ch.1 l107 (the doubled introduction ×2); Ch.3 l77 (the source-sense-as-weather use) |
| "far end of the bond" | 5 | **3** | Ch.2 l87 (the bond-drain mechanic introduced); Ch.19 l117 (denouement); Ch.20 l161 (finale, shared with doorpost) |
| "flat careful" | 4 | **1** | Ch.13 l151 (subset of careful-surface keeper) |

Raw grep (incl. HTML build-comments) now matches prose for every tic except an intentional
allowlist/comment note; the one build-comment that named "the slow way"/"the doorpost" (Ch.19 l3
structure note) was reworded so grep stays clean.

### Recast method (no new tic seeded)
Each cut instance was recast to **concrete, varied** sensation/action, deliberately spread so no
single replacement became the next metronome (the r6 doorpost/second-warmth regrowth failure was
explicitly guarded against):
- **cold working part →** "the reckoning part," "the part that did the arithmetic," "the tally,"
  "some cold part of her," "she did the sum," "made herself read it," "the flat level grammar of
  the arithmetic" — varied per site.
- **did not weep →** "kept her face still," "made no sound," "let none of it show," "gave nothing
  away," "held her face still," "she never did" — the grief-held-inward guardrail preserved in
  meaning at every site (references to the one sanctioned break intact). Guarded against an
  "eyes dry" mini-refrain (limited to two uses, then varied).
- **careful surface →** "flat and level," "held her face still," "the held quiet," "a level held
  stillness," "laid down level."
- **slow way →** "the long, patient work," "a winter of afternoons," "one afternoon at a time,"
  "the patient way," "the long way," "little by little."
- **doorpost / second warmth →** "braced there," "rooted," "the steady warmth," "the warmth she
  was tied to," "Raizen held, rooted," "close and rooted" — Raizen's bond-anchor MEANING kept at
  every site; only the two repeated epithets removed. Bond-system vocabulary (far braced end,
  far end of the line, rooted, the line) left intact — that is the world's mechanic, not a tic.

## Pattern #11 — "the way you [X]" self-completing simile (secondary target)
Capped the SELF-COMPLETING-SIMILE construction to ≤3 per chapter in the front-half chapters that
exceeded it (r6 had handled Ch.17–20). Ordinary "the way you" uses (dialogue, instruction) left alone.
- **Ch.1** 6 → 3 similes: kept lamp-in-a-far-room (re-read reward), clock-in-a-quiet-house, the
  reached-into-candle (Death-symbol foreshadow); recast the stone, the sum, the word.
- **Ch.8** 5 → 3 similes: kept the fire-not-yet-let-in, the coal, the rail; recast the banked-coal
  and the size-of-a-thing.
- **Ch.19** 4 → 3 similes: recast "the way you put a key to a lock"; kept the people-unseen, the
  hand-on-a-doorpost (literal-image simile, r6 keep), the lamp-in-a-window.
- Ch.6 already ≤3 self-completing similes; left as-is.

## Gates (all green, whole book)
- `python3 tools/style_check.py --max-emdash 4`: **RESULT: clean** (em-dash ≤4/ch holds; the one
  transient new cross-chapter repeat a recast introduced — "a thing she did not," Ch.1/4/7 — was
  caught and reworded; no NEW distinctive phrase remains).
- `python3 tools/grammar_check.py`: **RESULT: clean** (0 errors; long-sentence notes pre-existing, non-gating).
- `python3 tools/rhythm_check.py`: **30 → 30** — identical to the r4/r6 baseline, no new flat triplets.
- Word floor (95k): clear at **111,618** (r6 was 111,688; ~70 words net cut, all tic deletions/recasts).

## Canon / continuity
No canon moved. All guardrails intact: balance-not-victory; void/Fen finale unexplained; the two
sanctioned breaks (Bk2 Ch.16, Bk3 Ch.10) untouched — their meaning preserved through the recasts;
Raizen dark ordinary eyes; source = physical Book-One cavern; the doorpost/second-warmth cosmology
and the socket ending preserved (cluster thinned to its ≤4 floor, the defining promise and both
finale anchors kept). The Ch.5/7/9 corridor scene architecture was NOT touched (surplus tic phrases
only), so it survives the pending Option-B interior rework. No Book-One/Two touchpoint altered.
