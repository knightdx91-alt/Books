# Revision Log: Chapter 10, Polish Cycle 1

**Input:** `manuscript/chapters/chapter-10.md` after the continuity repair (2,563w by shape_check). **Eval:** `evaluations/chapter-10-eval.md` (POLISH; Floor 8.0, held by Prose & Voice alone; Casual 8.5; Emotion 9.0).
**Scope:**
- the top seven fixes (P1–P7 = Revisions #1–#7);
- the smaller fixes: #12 (¶64), #8 (¶194), #9 (¶94), #11 (¶118) and #13 (the blind moved);
- ENTITY CH10-5 (Nikaso's gate).

Optional #15 was not applied. #14 is a WATCH with no change. #16 and #17 are bookkeeping and pipeline items, outside the editor's scope.
**Pre-cycle backup:** a scratch copy outside the book folder.
**Held fixed:**
- The first sentence, "The letter had been folded down very small.", is byte-identical.
- The last paragraph is byte-identical (cmp), so the shape is still `short-punch` → `quiet`.
- 0 breaks.
- The text of the reed-blind paragraph is byte-identical; only its position changed.
- Not touched: the yawn, the neighbour-news answer, the reply (¶160–¶186), ¶190–¶192 and the broom anchor.

## Results (run from /home/user/Books)
| Measure | Before | After |
|---|---|---|
| Words, shape_check | 2,563 | **2,446** |
| Words, style_check / wc -w | 2,574 / 2,741 | 2,457 / 2,624 |
| Dialogue (shape / show-tell) | 39% / 36.5% | **40% (raw 40.47%) / 38.0%** |
| Median sentence | 15 | **15** |
| Breaks | 0 | 0 |
| `check_chapter.sh 10` | clean | **clean on every gate** (style, grammar 0, rhythm 0, show/tell no flags, voice-wear strict clean, tic gate clean, metaphor no flags, shape CLEAN) |
| `tic_report.py --echoes 10` | 0 | **0 echoes; command-echo candidates: none** |
| "could have" in Ch.10 | 5 | **0** |

## Entries (before → after)

### Logic first
1. **¶64 (Rev #12).**
   - Before: "Jerusalem had fallen that summer, and the Temple with it, burning."
   - After: "Jerusalem had fallen in the summer just gone, and its temple with it, burning."
   - The Armada sentence is kept.
   - "the summer just gone" gives the date an antecedent. The lowercase "temple" matches Ch.5.

### P1, the curse-tablet skeleton (Rev #1): a new order and new details
2. **¶6.**
   - Before: "…wanted it known. It was a strip of papyrus folded over and over on itself into a packet I could have closed my fist on. A thread went round it twice, sealed at the knot with a thumb of gray clay. One end had stood in wet somewhere and dried with a brown tidemark across it."
   - After: "…wanted it known. One end had stood in wet somewhere and dried with a brown tidemark across it. The thread round its middle was knotted under a thumb of gray clay."
   - Ch.9's material sentence ("It was a [material]") is gone. So are the fist ruler and the fold count, which the first sentence already covers.
   - The order is now stain, then fastener. Ch.9 ran material, then folds, then fastener, then water damage.
   - The tidemark sentence is kept verbatim (Strength #1).
3. **¶50.**
   - Before: "The clay crumbled off the knot in one piece. I worked the thread loose with a thumbnail. The papyrus opened a fold at a time, stiff as a dried leaf, and lay over my palms in a strip the length of my forearm. The hand inside…"
   - After: "The clay broke from the knot at the first push, and the thread slid off over the end. Unfolded, the papyrus was mostly creases and needed both my hands to keep it flat. The hand inside…"
   - Removed: "worked … loose", the slow fold-by-fold opening, the material simile, the forearm ruler and "in one piece" (Ch.9 ¶156).
   - This also clears Rev #10, the in-chapter body-ruler double with "at the length of her arm", which stays.
   - "The hand inside was small and level from top to foot." is kept (N-18).
   - Deviations from the evaluator's strings:
     - I did not use "the thread loosened under my thumbnail". "with my thumbnail" is Ch.1 ¶383's cassette door, and there "my thumb" would be its fifth use.
     - A first draft, "longer than I would have guessed from the packet", tripped the echo scan ("longer than i", Ch.2). It would also have been an object-size impression.
     - "than the packet had looked" was rejected as an echo of Ch.1 ¶339's cake ("than it had looked").
     - "into a long strip" was rejected because "into a long" is already in Ch.5 and Ch.6.
   - Pre-grepped, 0 in Ch.1–9 and the 13 samples: "broke from the", "first push", "slid off over", "Unfolded", "mostly creases", "both my hands", "keep it flat".

### P2, the reading-time measure (Rev #2)
4. **¶134.**
   - Before: "She looked at it from where she stood, without coming nearer, for the time it would have taken her to read it if she could read. It was seven letters. At that distance, in that hand, they could have been anything."
   - After: "She looked at it from where she stood, and came no nearer. From there, in that hand, it was any name in Phocis."
   - This also removes the #13 count ("seven letters").
   - Deviation: the evaluator wrote "it could have been any name in Phocis". I changed it to "it was any name in Phocis" to take one more "could have" out of the chapter (see entry 9).
   - "it was any name" is 0 in Ch.1–9 and the samples.

### P3, the speech ledger (Rev #3)
5. **¶72.**
   - Before: "It was the best Greek I had spoken since October, and it was his from beginning to end."
   - After: "Kallia corrected none of it. The Greek was his, from beginning to end."
   - The heart of the line, that the Greek was his, is kept, as the author's read asked.
   - "since October" is gone from the sentence about his words, which removes the nearest trace of the parallel.
   - Kallia's correcting habit (Ch.7 ¶126, "she corrected me the way she did everything else, by doing it") lands without being pointed at.
   - "corrected none" and "from beginning to end" are 0 elsewhere.

### P4, the purse comparison (Rev #4)
6. **¶44.**
   - Before: "Once she put her hand flat across it in passing, the way a woman in a crowd checks her purse."
   - After: "Once, going past the jar, she touched the place through her clothes."
   - The second use of the pickpocket/purse vehicle (Ch.8 ¶340) is gone, and so is the flat-hand gesture (Ch.5, Ch.7).

### P5, the held silences measured by motion (Rev #5)
7. **¶112.**
   - Before: "She wanted no reply to that, and I made none. The spindle hung at the end of its thread, turning a little one way and then the other."
   - After: "She wanted no reply to that, and I made none."
   - This takes Kallia's work-suspended tell down to two expressive uses (¶122, ¶126).
8. **¶130: kept whole, by the conditional in the brief.**
   - Trimming ", and every so often it moved" (with every other fix applied) put shape_check at 41% (990 of 2,432 words quoted, 40.7%).
   - Following "if dialogue would go over 40%, keep the tunic sentence whole", the clause is restored. ¶130 now reads exactly as it did before the cycle. (See entry 17 for the remaining margin.)

### P6, the sample-08 pair (Rev #6)
9. **¶158.**
   - Before: "I could have left out the roof. I could have left out the father with no son of his own, and read the wife as so much talk about rain. There was not a soul in that court or in that lane who could have told the difference."
   - After: "Nobody in that court or in that lane could read a word, and I might as easily have made the roof into so much talk about rain and left out the father with no son of his own."
   - It is now one sentence. The anaphora and the 2+1 shape are gone, and so is sample-08's "could have said / could have told".
   - The author's read flagged "could have" for a broken thing as a device forming, so the counterfactual is now "might as easily have", and the "could have told the difference" tail is gone.
   - The content is kept: the roof read as rain talk, the father left out, and nobody able to check her.
   - Deviation: the evaluator's string kept "could have caught me". I did not use it, for the same reason.
   - "could read a word", "read a word", "might as easily", "as easily have" and "made the roof" are 0 elsewhere.
   - "could have" in Ch.10 is now **0** (it was 5).

### P7, the weighted packet in the closing run (Rev #7)
10. **¶196.**
    - Before: "Before I folded it I read it once more, without moving my lips, from the greeting down to the date. I folded the papyrus, and it made a fatter packet than before."
    - After: "I read it once more to myself, from the greeting down to the date, and rolled it up."
    - The niche and the cumin follow unchanged.
    - Deviation: the evaluator's string ended "and folded it". "and folded it" is sample-12's refold ("took the letter … and folded it along its old creases"), which is the very slot P7 removes. Rolling an opened papyrus is a different act, and it carries no size or weight.
    - The reading-lips beat is gone too.
    - "once more to myself", "from the greeting", "rolled it up" and "and rolled it" are 0 elsewhere.

### The smaller fixes
11. **¶194 (Rev #8).**
    - Cut: "Her shoes receded over the stones at the pace she used for the spring."
    - Now: "The gate came to behind her and bounced once. Up at the last door the broom still lay over the threshold, from post to post."
    - The composure-gait exit and the footwear exit are gone, along with the double of Nikaso's receding voice.
12. **¶94 (Rev #9).**
    - Before: "My voice went on through the oxen without me."
    - After: "The oxen went by while I was still at that desk."
    - The dissociation is kept but is no longer on the retired voice channel. The Ch.5 near-string "The voice went on me there" is gone.
13. **¶118 (Rev #11).**
    - Before: "She said it to the letter. I raised it for her."
    - After: "She was answering the letter, and I raised it for her."
    - sample-09's "said it to the [object]" is gone.
14. **The reed blind (Rev #13).**
    - The paragraph, byte-identical, moves from after "She drew a fresh pull of wool from the hank, and let it run back." to the start of the spinning scene.
    - ¶46 is split after "…and spun."
    - New order: the spindle and the first warm afternoon → the blind let down → "I sat on the step with a basket of chickpeas…".
    - Deviation: the evaluator said to place it after "…to work without a cloak." I put it two sentences later. The paragraph ends "She came back to her place.", which needs her place (beside the lean-to, spinning) set up first, and "one-handed" reads right once the spindle is in her hand.
    - The blow at ¶122–¶126 now stands on "Kallia stood in the sun with the wool in her hand.", the wrong comfort and the wool run back. The broom is the only displaced-labour answer. The soot still comes before "Keep it out of the smoke,".
15. **ENTITY CH10-5, ¶138.**
    - Before: "It was Nikaso, from three gates down, with flour on her hands…"
    - After: "It was Nikaso, from along the lane, with flour on her hands…"
    - Kallia's gate is at the lane's end (Ch.5), and Nikaso comes out "Midway along the lane" (Ch.8 ¶30). The gate count CH8-5 cleared is gone again.
    - Deviation: the brief's example, "from down the lane", tripped both voice-wear (strict self-repeat) and the echo scan on "down the lane with" (Ch.7 ¶218). "from along the lane" is 0 elsewhere.
    - Nikaso calling "at the next gate, and the one after, and fainter at the bottom" (¶156) is unchanged; it does not count back to her own gate.

### Dialogue-band words (honest, not padding)
16. With the tunic restored, the chapter was still 7 narration words short of 40%. Three small additions supply them, each a real detail, not filler:
    - "the papyrus was mostly creases" in ¶50: the evaluator's pre-grepped texture, moved to the opening, where the folds belong.
    - "could read a word" in ¶158: it states the fact the counterfactual rests on.
    - "rolled it up" in ¶196, for the cadence.
    - In ¶6, "The thread round it" became "The thread round its middle".
    - Each is pre-grepped 0 in Ch.1–9 and the samples.
17. **Margin.** shape_check reads 40% (40.47% raw, 990 of 2,446). That is inside the band but thin: about 3 narration words of headroom before the meter rounds to 41. The show/tell meter reads 38.0%. A later edit that cuts narration here needs a re-check.

## Changes not made (and why)
- **Optional #15** ("lifted the broom off its boards"): left alone. The evaluator ruled it the designed payoff, and the sweep is a preserved strength.
- **#14** (the last paragraph against sample-12's slots): no change in Ch.10, per the eval. Ch.31, 34 and 44 must not stop on a chore resumed, an offstage complaint or an object put away.
- **#16** (bible Ch.10 blocks sync) and **#17** (pipeline regexes, skeleton check): bookkeeping and root work for the orchestrator.
- **The wife paragraph (¶70):** not expanded. It is the one place the evaluator said would honestly take words, but it is quoted letter text and would raise the dialogue share.

## Concerns for re-evaluation
- **¶130 is whole again** ("every so often it moved"). That is the SPENT held-silence family, kept only by the dialogue-band conditional. If the evaluator wants it gone, the band needs about 13 narration words from elsewhere first.
- **¶50 vs Ch.9 ¶278.** The fastener-then-opening sequence is unavoidable for any sealed letter. Check that what remains (clay, thread, unfolding, a two-handed hold, the hand inside) reads as its own beat, now that the material sentence, the ruler, "worked", the slow folds and the simile are gone.
- **The blind's new place.** It now comes before Mara sits down, as plain seasonal work. Check that it no longer reads as a response to anything.
- **Word count 2,446** is under the 2,500 range floor. STATE has no per-chapter floor; the chapter was not padded.
