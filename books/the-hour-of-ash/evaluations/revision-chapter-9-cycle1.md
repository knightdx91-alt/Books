# Revision Log: Chapter 9, Polish Cycle 1

**Input:** `manuscript/chapters/chapter-9.md` after the continuity repair (5,840w shape_check). **Eval:** `evaluations/chapter-9-eval.md` (POLISH; Floor 8.0, held by Prose & Voice; Casual 9.0).
**Scope:** PATH TO 8.5 items 1–13 (Revisions #1–#15, #18), optional #16, and the ear-to-hive half of #17. Pre-cycle backup: the scratch copy taken before editing (not in the book folder).
**Held fixed:** ¶6 (manumission) is byte-identical (diffed). ¶418 "He let the gray drink first." is byte-identical. There are 5 breaks, and the shape is `narrative` → `punch`.

## Results (run from /home/user/Books)
| Measure | Before | After |
|---|---|---|
| Words, shape_check | 5,840 | **5,762** |
| Words, style_check | 5,869 | 5,789 |
| Dialogue (shape / show-tell) | 28% / 26.8% | **28% / 27.1%** |
| Median sentence | 15 | **15** |
| Breaks | 5 | 5 |
| `check_chapter.sh 9` | clean | **clean on every gate** (style, grammar 0, rhythm 0, show/tell no flags, voice-wear strict clean, tic gate clean, metaphor no flags, shape CLEAN) |
| `tic_report.py --echoes 9` | 0 (old scan) | **0 echoes; command-echo candidates: none** |

Note: since the evaluation ran, the echo scan has gained a pronoun-swapped layer. On the pre-cycle text that layer reports 2 hits: "<S> stayed where <S> was" (cleared by item 12) and "at <O> <S> looked at" (¶414; cleared by item 21 below).

## Entries (before → after)

### PATH 1: Logic
1. **Dawn seam, ¶268 (Rev #1, +22w).** "…with his arm in to the shoulder. I was at the lions with my jar." → "…lying on his belly with one arm down it. Kallia wanted the jars filled before she lit her fire, and I was at the lions with the first of them; the stand would have to go to the priest as it stood."
   - I used my own wording here. The evaluator's "Kallia's first jar" left the cost implied. The added clause states it by fact (her water comes before Mara's dawn try). It is also the real content that keeps the chapter above 5,750.
   - Pre-grepped against Ch.1–8 and the 13 samples, all 0: "jars filled", "lit her fire", "before she lit", "first of them", "with the first", "as it stood", "go to the priest".
2. **"No fire" (Rev #15), ¶100.** "No fire," → "No forge,". The priest's "A smith's price is for a smith's fire" still lands.

### PATH 2: P9, the scrub → the thumb (Rev #2, #14)
3. **¶254.** "I held the thumb clear of the bronze and let it bleed onto the paving until it stopped." → "I sucked it until it stopped." This removes the Ch.6 ¶522 held-clear hand.
4. **¶342.** "…and under my nails the soot would not shift. I kept at them with a corner of the clay after the water had stopped going any blacker." → "…and the cut in my thumb came open in the water and put a thread of red into the black. I cleaned round it. It went on coloring the basin for a while, a little less each time, and then the water stayed black."
   - The wound now runs ¶254 → ¶342. The Ch.5 scrub-past-need is gone. ¶318 is untouched, so "black in every crease" still appears once.
   - Deviations from the evaluator's string:
     - "the cut at the base of my thumb" → "the cut in my thumb", which avoids an in-chapter repeat of ¶254's "open at the base".
     - "I washed round it" became "I cleaned round it", which avoids a second "I washed" two sentences after the first.
     - I added the thinning sentence (+23w) as the second place that earns words.
   - All 0 in Ch.1–8 and the samples: "came open", "thread of red", "into the black", "cleaned round", "coloring the", "less each time", "water stayed", "stayed black".

### PATH 3: P1, "in a hurry" (Rev #3)
5. **¶360.** "The gypsum had gone on in a hurry, and the brush had dragged in it. The red had run a little at the foot of every upright, because it had been painted in the cold and the paint had not wanted to dry." → "The brush had dragged in the gypsum, and the red had run a little at the foot of every upright." This also removes the #11 because-clause. "in a hurry" in Ch.9: 0.

### PATH 4: P2, the stranger-freeze (Rev #4)
6. **¶72.** "The bellows stopped. The slave swung round…" → "The slave swung round…"

### PATH 5: P3, the gaze-arrival "then" (Rev #5)
7. **¶110.** "Euthydikos looked at me then. Until then his eyes had gone to the slave, or to the smith, or to the air a little behind my shoulder, where a husband might have stood." → "Up to then Euthydikos had looked at the slave, or at the smith, or at the air a little behind my shoulder, where a husband might have stood. This question he asked of me."
   - I used "Up to then" in place of the evaluator's "Up to now", because "now" sits wrong in first-person past narration. "Up to then" is 0 in Ch.1–8 and the samples, and it is not a hinge opener.
   - The husband clause is kept verbatim.
8. **¶228.** "His eyes went past me then, into the court:" → "His eyes left me for the court:"
   - The evaluator's "His eyes went past me into the court:" tripped the echo scan ("past me into the", Ch.4). I wrote my own; "left me for" is 0.

### PATH 6: P4, the hearthstone skeleton (Rev #6)
9. **¶332–¶334.** Cut "Who paid?" / "Euthydikos." Kallia's only question is now "Into your hand?", and "Onto it. From above." / "To that she gave no word at all." stand as before.

### PATH 7: P5, the borrowed standing anchor (Rev #7)
10. **¶262.** "I stood the stand up on its three feet on the paving, and it stayed, with the bowl level and the lid hanging still on its chain." → "I set the stand on its three feet on the paving. The bowl sat level, and the lid hung still on its chain."

### PATH 8: P6, the inscription in the cave inscription's words (Rev #8)
11. **¶8.**
    - "The letters had been cut that winter, and the dust of the cutting still lay in the V of every stroke." → "The letters had been cut that winter."
    - "The old ones had weathered soft; lichen had crept into many of them and filled the round letters up like wells." → "The old ones had weathered soft, and the round letters in them had filled with green like wells."
    - The guidelines sentence ("fine as the scratches on a long-playing record") and the corrected letter are untouched.
12. **¶278.** "…and the writing surfaced through the white in scratched capitals, crowded,…" → "…and the writing was scratched in capitals beneath the white, crowded,…" "surfaced" and "lichen" in Ch.9: 0.

### PATH 9: P7, the joint-depth ruler (Rev #9)
13. **¶14.** "…and he was white with dust to the elbows and in the hair of his eyebrows, with a mallet in one fist." → "…and he was floured all over with stone dust, with a mallet in one fist." The doubled eyebrow intro is gone too (the smith keeps his at ¶62).
14. **¶268.** "with his arm in to the shoulder" → "lying on his belly with one arm down it". `to the (elbow|shoulder|wrist|ankle…)` in Ch.9: 0.
15. **¶270, a continuity knock-on of #14 (mine).** "He scrambled out of the culvert with…" → "He scrambled up with…". He is now lying beside the culvert, not in it. "scrambled up" is 0.

### PATH 10: P8, the square-chorus marks (Rev #10)
16. **¶388.** "For three hundred I'd give up my wife's brother, and help them tie him." → "For three hundred I'd give up my landlord, and hold the rope."
17. **¶408.** "The men at the money-changer's had their backs to him." → "The men from the board had their backs to him."
    - My wording. The evaluator's "Those men" sat a paragraph and a half from its antecedent (¶404), across ¶406. "men from the board" is 0.
18. **¶416.** "past the money-changer and the men still at the eel-seller" → "past the men still at the eel-seller". "money-changer" is now at 1 (¶404).

### PATH 11: P10, "the rest" on the money (Rev #11)
19. **¶344** "…and a goat that shakes, and the rest." → "…and more after that."; **¶374** "with the rest of it." → "with the money."; **¶416** "I had his obol in the rag with the rest." → "I had his obol in the rag."
    - The priest's "The rest is only money." (¶130) is kept, so it is now the only "the rest" on the money. The other uses are non-money (the solder ×2, the mirror, the wool, the goat man's water).

### PATH 12: P11 + the close (Rev #12)
20. **¶366.** "'For the god?' he said, before I had asked a thing." → "'For the god?' he said, with his mouth full." (He is eating a heel of bread, ¶364.)
21. **¶416.** "I stayed where I was." → "I kept my place." This also clears the new pronoun-swapped echo with Ch.5.
22. **¶414, my addition, forced by the gate.** "I was looking at him. I looked at his face." → "I was watching him. I looked at his face."
    - The pronoun-swapped layer matched "at <O> <S> looked at" against Ch.7 ("Look at me." / "I looked at the jar."). The Ch.7 match crosses a paragraph boundary, but the brief requires 0.
    - One word changes. The strength survives: the deliberate look at his face, not his hand, still follows the watching. "watching him" is 0 in Ch.1–8 and the samples.
    - The oil cart stays (spent here, per Cross-Book #8).

### PATH 13: second uses and in-chapter (Rev #13, #14, #18)
23. **¶214 (Rev #13).** "At the back gate a line of mules stood loaded with split wood, and the man unloading it into the priest's woodshed was Valens." → "At the back gate Valens was unloading split wood off a line of mules into the priest's woodshed."
24. **¶236 (Rev #13).** "How long will it stand?" → "Will it stand?" Valens's "How long…?" stays at 3 book-wide. Her "With this in it? Years." still answers.
25. **¶44 (Rev #14).** "…on her head and a hand up to steady it, in a tunic…" → "…on her head, in a tunic…"
26. **¶26 (Rev #14).** "…the dust went past my face in a little cloud." → "…the dust went past my face."
27. **¶198 (Rev #14).** "She came and stood over the stand, and not over me." → "She came and stood over the stand."
28. **¶12 (Rev #14).** "a man said above me." → "a man called."
    - My wording, −2w. The evaluator's "a man called down to me" would have doubled "down" against "Mind yourself down there". The chip in her hair (¶10) and the plank (¶14) already place him above.
29. **¶84 (Rev #14).** "shiny as boiled sausages" → "tight and glossy as cherries". Simile count is unchanged at 11.
30. **¶254 (Rev #14).** See #3.
31. **¶54 (Rev #18, the bay-tree verbatim).** "There was a bay tree in a pot at the door, and a slave on a stool beside it shelling beans into his lap, who looked at my feet first…" → "The bay tree stood in its pot, and a slave on a stool beside it, shelling beans into his lap, looked at my feet first…"
    - The evaluator's "…by the door…" made "by the door" a 3x book-wide tic (Ch.2, 7, 9). A split into two sentences then made "He looked at my" a Mara self-repeat (voice-wear FAIL). The final form avoids both.
    - The feet-first look itself is unchanged (CLOSED at 3).
32. **¶308 (Rev #18).** "He brought his face down to it, so close that his beard brushed the bowl, and looked…" → "He bent so close to it that his beard brushed the bowl, and looked…". "brought [x] down" goes from 3 to 2.
33. **¶180 (Rev #18).** "a line as fine as a hair" → "a line a hair wide". "fine as" is now 1 (¶8 only).

### Optional
34. **Curse tablet, ¶266 (Rev #16).** "I give her down to Hermes the Holder and to Earth, and I hold her under the lead." → "I give her down to Hermes below and to Earth, and I nail her under the lead."
    - The bronze nail is on the page at ¶278. "Holder" and "hold her" in Ch.9 are now 0, so the free / bound / hunted diction tie is broken.
    - "Hermes below" and "nail her" are both 0.
35. **The bee-man's ear to the hive ×2, ¶256 (#17, the beat half only).** "The bee-man had his ear to a hive." → "The bee-man was bent over a hive." The beat now occurs once (¶172).

## Not done (and why)
- **#17, naming the bee-man (still "the bee-man" ×14).**
  - It is optional in the PATH and not in this brief's list. Naming him obliges a new character-bible card, and the bible is outside this edit.
  - The tic gate is clean on it.
  - It remains a WATCH item for the re-evaluation and for the orchestrator.
- **#19, the character-bible sync.** This is bookkeeping for the orchestrator after re-evaluation. The quotes now invalidated:
  - Valens's "How long will it stand?" (now "Will it stand?").
  - Kallia's "Who paid?".
  - Mara's "I kept at them with a corner of the clay…".
  - "I stayed where I was", "my wife's brother", "Hermes the Holder".
- **#20, the pipeline gate additions.** Root tooling, out of scope.
- **The pre-existing in-chapter 5-gram "the priest said to the slave" (¶78, ¶158).** The evaluator did not flag it and I left it alone. It is listed here for the re-evaluator.

## Strengths verification
- ¶6 and ¶418 are byte-identical.
- The following are untouched:
  - ¶10's limestone chip.
  - The cutter's lines.
  - ¶50.
  - The court's preserved lines, including the beard, "having no beans left to examine" and the husband clause, which is kept verbatim inside #7.
  - The mending's preserved lines, the hardware store (¶178) and the crayon.
  - Valens's elbow, "That's the god's," "Somebody will.", "An obol." / "He'll pay." and the mule hair.
  - ¶296–¶326 apart from #32: the lamp, the coins "from a little above", "each one, the thumb last", ¶318 "Perhaps it was the soot." and ¶320 "Thank you".
  - Kallia's "Onto it. From above.", the hissing sand, the goat line and "Kallia's sand had gone quiet while I tied it."
  - The notice (¶358) and the goat man's preserved lines.
  - The board's preserved lines.
  - "while a slow man might read it once…".
- **Enhanced:**
  - The dawn seam now resolves as a cost.
  - The cut thumb pays off in the basin, so the peak's body rebel is new to the book.

## Concerns for re-evaluation
- **¶414:** check that "I was watching him. I looked at his face." keeps the force of the preserved "I was looking at him. I looked at his face."
- **The basin:** check that the added thinning sentence reads as body, not as a report beat.
- **Length:** shape_check 5,762 is 38 below the outline range floor of 5,800. STATE has no per-chapter floor, and the brief's floor (5,750) is met with real content only.
