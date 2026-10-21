# Evaluation: Chapter 21 — Strawberries
**Evaluator:** book-evaluator | **Date:** 2026-10-21
**Text evaluated:** `manuscript/chapter-21.md` (3,311 words of prose; target 3,400, range 3,100–3,800, so on spec).
**Read first:** STATE.yaml (decisions: the heart-ring payoff lands here; the whip comes from the RIGHT palm, which splits open on its own and closes after; spell-repetition watch; the dialogue rule; no shared gestures), book CLAUDE.md, project/STYLE_CONSTRAINTS.md, project/foundation.md (Magic ledger), character-bible.md (Iro, Heath), outline Ch.21, manuscript/chapter-20.md, chapter-18.md (the lake, Lora's drills), chapter-16.md (Heath, the ring), Sygl_Complete.txt L813–834, evaluations/chapter-20-eval.md.

## HEADLINE
**CVI-Launch:** 8.7 (8.2 + 0.5 strong anchor) | **CVI-Legacy:** 6.2 | **Genesis Floor:** 7.5 | **Genesis Average:** 8.2
**Engagement Type:** Self-Insertion (primary) / Empathy (secondary) / Fascination (tertiary)
**Divergence Alert:** 1.2 (Launch over Floor). That is under 2.0. As in Ch.19 and Ch.20, mechanical caps hold the floor down; the content does not.

**VERDICT: POLISH (FAIL at the 8.5 gate).** What the chapter gets right:
- Every source beat from L813–834 is present and in source order.
- The killing is justified, final and clean, with no guilt: "Okay then." / "No one threatens my girls," Bal told it.
- The whip comes from the RIGHT palm. The palm opens on its own and closes when the blood returns.
- The council comes in Amelia's own telling.
- Raizen's cheating is revealed after the council, where the source reveals it.
- The heart-ring payoff takes two lines and adds no plot.
- The register is American ("Heck", "pants").
- No spell is invented. There are no em dashes.

The floor comes from two caps:
- **Characters is capped at 7.5.** The hand count found three gesture classes at 3+ inside 500 words: stopping, turning and posture. Two more clusters are borderline: hand/chest and props.
- **Prose is capped at 7.5.** Pattern #11 (explanatory glosses) runs at 4 instances, 1.2/1K, over the commercial 0.8/1K line. There is also one real **logic contradiction**: "Bal knew how" (L124) against "I just don't get how they knew we were here" (L170).

Every fix below is a cut or a word swap and adds no plot. With F1–F15 applied, the chapter projects to **Floor 8.5 / Casual 8.5: PASS.**

## Gate tools (scratch copy, Ch.1–21 at `/tmp/claude-0/-home-user/925d8686-989e-5134-a9ef-2d597d7cac42/scratchpad/ev21/manuscript/chapters/`)
- `voice_wear_check.py`: **clean.** No retired phrases and no device over cap. The 2 cross-chapter self-repetitions are WARN only.
- `tic_report.py --gate`: **clean.**
  - Ch.21 auto-recurrence: 0. And-chains: 4 (cap 9). Negation pivots: 0.
  - Ch.21 adds nothing to the book-wide gesture table.
- `style_check.py --dir manuscript/chapters`: **clean.** Simile 2.4/1K, adverb 9.4/1K, em dashes 0.
- `grammar_check.py --file chapter-21.md`: 0 errors.
- `tic_report.py --echoes 21`: 53 second-use echoes. Most are harmless function phrases. Four are worth varying because they sit in the same kind of scene as their first use:
  - "for Bal's legs" and "into the meat of" (both Ch.16, Heath's fight)
  - "his head snapped back" (Ch.17)
  - "her mouth curved" (Ch.19)

  These are F13.
- Filter words: "seemed" (L96) and "seeming" (L184), 1 each. "just" appears only in dialogue, from the source.

The tools do not classify posture, stopping, turning, looks or props, so the hand count below is the binding check.

## FULL gesture hand count (w = word position in the prose; 500-word windows)
| Class | Instances | 3+ in 500w? | Verdict |
|---|---|---|---|
| Smile/grin | Amelia's smile w370 (source); Lora "mouth curved" w520; Iro "grinning" w1150; "The grin went away" w1248 | no | OK |
| Laughs | "hilarious" w150 (reported); Iro laughed w1060 (source); Amelia laugh w2700 (source, one beat) | no | OK |
| Blushes | 0 | — | OK |
| Looks/eyes | Lora "with closed eyes" w185; "opened his eyes" w450; "caught Hopper's eye" w685; Amelia "studied him" w2410; "looking enormously pleased" w2650 (source) | borderline: w185–685, exactly 500 | F15 |
| Sitting/posture | Hopper "lay down" w60; Bal "stretched himself along the rock" w260; Lora "lain down beside him" w470; Bal "eased himself upright" w520; Viridia "stretched out" w570; Bal "stood" w590 · Lora "sitting up" w2020; Amelia "sat him down" w2230; "Amelia had straightened up" w2300; "They sat by the lake" w2530; Amelia "sat down cross-legged" w2650 (source) | **YES**, twice: w60–590 (6 in 530; Bal alone 3 in 330), and w2020–2300 (3 in 280) | F6, F7, F8, F9. "Stretched" is also doubled (L18/L40). |
| Freezing/stopping | Iro "stopped fighting it" w1700; Lora's hand "stopped with it in the air" w2040 (source); Viridia and Amelia "came up behind her, and stopped" w2100; Viridia "stopped chewing" w2915 | **YES**: w1700–2100, 3 in 400 | F4 |
| Turning | Bal "turned the right palm out" w1520; Lora "turned at the sound of him" w2030 (source); "turning him by the arm" w2070; Amelia "had turned toward the woods" w2300; Aren "turned around" w2940; "as I turned to go" w3110 (source) | **YES**: w2030–2300, 3 in 270 | F5 |
| Chest/heart | "made his heart hurt" w370 (source); Lora's hands "on his chest" w2070; cuts "over his chest" w2150 (wound inventory); Amelia's hand "against his breastbone" w2230 | borderline: 3 in 160, though one is wound inventory | F6 |
| Hand holds/hand beats | Lora "lifted her hand to wave" w2040; "Her hands were already on him" w2070; Amelia "set a hand flat" w2230; backs of hands w2710; Aren "put up one hand" w2990 (source) | borderline: 3 in 190 | F6 |
| Tilts / nods / shrugs | 0 / 0 / 0 | — | The source's nod and shrug are rendered without the words. Good. |
| Prop fiddling / set-down | "picked up his rapier" w1960; Viridia "set it on the ground" w2150 (source); Lora's empty pot held upside down w2470; Amelia's pile "set it apart" w2510 | **YES**: w2150–2510, 3 in 360 | F10 |
| Hopper's "once" | "nose against his wet shoulder, once" w270; "thumped her tail once" w700; also "twirled his sword once" w990, "curled once" w1530 | wording, not gesture | F11 trims it |

**No shared gestures across the cast.** Lora's hair is not tucked, and Viridia does not pull Bal by the hand or sleeve. Viridia's reaching hand on the rock (L40) comes from the source, appears once, and is not the pull. Lora retying a bandage that was "fine both times" is a good new beat with no prior use.

## Genesis Score (Craft Assessment)

| Dimension | Score | Evidence | Cap Reasons |
|-----------|-------|----------|-------------|
| Originality | 8.5 | The anchor is fresh: "By the edge of the woods his forearm was sticky to the elbow, and which of the red on it was strawberry was anybody's guess" (L144). Hopper refuses the lake the snake was killed in (L8–14). "Hand over hand without using his hands" (L108). Lora shows him the empty salve pot "upside down … accusingly" (L180). | — |
| Theme | 8.5 | Protection of a chosen family, carried by action: the girls asleep in the sun against "Those pretty girls of yours" (L88, L92). There is plenty of non-thematic texture: a dragonfly, the dent from Lora's glasses, ants on a flat stone, "fee for listening". | — |
| Characters | **7.5** | The work is strong. Iro has a card-true arc from chatter to "his face had turned young and scared" (L120). Lora: "Lora had no wish to hear it and listened anyway," with the knot retied twice (L184). Viridia demands the fight "again from the beginning". Amelia's "Explain," then her council as performance ("Positively purple"). Bal's composure is protective, not cruel. | **CAP 7.5:** three gesture classes at 3+/500w (stopping, turning, posture ×2), with borderline clusters in hand/chest and props. See the table. |
| Prose & Voice | **7.5** | Underlines: "Her mouth curved for a second in her sleep and then forgot to." (L36). "which of the red on it was strawberry was anybody's guess" (L144). "it parted down its middle, by itself, with no more fuss than a mouth opening" (L108). "The strawberries had held up better than he had." (L182). Voice under pressure: the run-on roll through the briars (L62). Deliberately rough sentence: "He gave up and went under." | **CAP 7.5 (#11):** 4 explanatory glosses = 1.2/1K, over the 0.8/1K line (L18 "as if to say he should have listened"; L48 "which meant yes"; L94 "where it could not shake"; L102 "Nobody kept fighting with a sword in his leg"). Also held down by the L124/L170 logic contradiction, the L102 inaccuracy (no sword is in his leg), and "a hundred mornings" (L70) against Ch.18's three mornings a week. |
| Pacing | 8.5 | Respite (about 850w), then an ambush that accelerates into short lines ("A branch snapped behind him." / "That sound saved his life."), then a decelerating aftercare and a reported tale. Value shift: idyll → near-death → a political win (the school rule is lifted, Raizen's cheating is exposed). Hook: "Half the army was getting ready to march somewhere, and nobody had told Bal where." | — |
| Emotion | 8.5 | Anchor: the strawberries in the ruined shirt. Emotional surprise: Amelia laughing until "bloody tears ran down both her cheeks" after a near-assassination. Body rebel: "He bit down on the noise that wanted out of him" (L42). Care built through vulnerability before the threat: Lora's wet lashes, Viridia's reaching hand. | — |
| Engagement (Dim 7) | 8.5 | Self-insertion: the outcast kills the man who threatened his girls and is fussed over by all three. Empathy: Lora's fierce bandaging. Fascination: the gods' council and Raizen caught cheating. | — |
| **FLOOR** | **7.5** | | Characters, Prose |
| **AVERAGE** | **8.2** | | |

## CVI-Launch Breakdown
| Input | Score | Evidence |
|-------|-------|----------|
| Commercial Pacing | 8.5/10 | Ambush at about w850 and kill by w1860; a quick council; hook into the temple. |
| Tomorrow Test | 3 anchors (2 image, 1 quote) → 9 | Strawberries bleeding through the shirt; Amelia laughing bloody tears; "No one threatens my girls." |
| Casual Reader | 8.5/10 | A warm lake day, a sudden fight and a satisfying win. |
| Shareability (quote/plot/emotional) | 4/4/3 → 7.7 | MAX 8 × 0.6 + AVG 7.33 × 0.4 |
| Concept Pitch | yes (10) | — |
| Human Closeness | partial (5) | — |

CVI-Launch = 8.2, +0.5 for the anchor = **8.7**.
CVI-Legacy (default weights): Originality 8.5, Theme 8.5, Vocabulary 2, Re-read 4, Identity 5 = **6.2**. The ring payoff rewards re-reading Ch.16.

## Anti-AI Scan (20 patterns; commercial thresholds)
- #1 Forced symmetry: clear. "and gave none, and gave none" (L82) is deliberate.
- #2 Empty poetic vocabulary: clear.
- #3 Rule of three: minor. "on his side, on his chest, turning him by the arm" (L150); "ate and talked and waited" (L184).
- #4 Em dashes: 0.
- #5 Empty metaphors: clear.
- #6 "And" openings: clear in narration. "And?" comes from the source.
- #7 Pseudo-philosophical closings: clear.
- #8 Parallelism: minor. The "There was…" run (L156) is a wound inventory and acceptable.
- #9 Smooth transitions: clear.
- #10 Described emotions: minor. "Bal's blood ran cold" (source); "Amelia was enjoying this"; "sounded amazed".
- #11 Explanatory extension: **4, 1.2/1K, strong**. These cause the Prose cap. See F2 and F11.
- #12 Binary negation: clear.
- #13 Precision flex: minor. "first three", "three of his strawberries", "twice" are all light.
- #14 Emotional control demonstration: minor. "He held his voice low, where it could not shake" (source: "trying to hide the rage").
- #15 Authoritative description: clear.
- #16 Philosophical asides: clear. "Hurt had never bothered Bal much" is canon (high pain tolerance).
- #17 Clean dialogue: minor. The council is Amelia's monologue with tidy interjections ("And you said?", "And then?").
- #18 Thematic echo chamber: clear.
- #19 Graduated reveal: minor. The shape follows the source.
- #20 Temperature report: clear.

**Total:** 8 patterns, all minor except #11. That is in the commercial clean range (0–8), at its top edge.

## Character Chaos Check (Bal)
- Irrelevant thought: **present.** "Would Amelia eat one, if he brought her one? He couldn't remember her eating fruit." (L46)
- Cognitive distortion: absent. That is acceptable for commercial fiction.
- Unprompted memory: **present and scene-triggered.** "Lora, with the dent on her nose. Viridia's hand open on the rock." (L92) The threat triggers it and the fight resumes.
- Failed emotional management: **present.** "He bit down on the noise that wanted out of him" (L42).
- Voice under pressure: **demonstrated.** The run-on roll (L62), then "The world got very quiet. / Bal could think now."
- Result: 3/4 inhabited. No chaos device runs on a cadence across chapters.

## Secondary Character Chaos
- **Lora:** has her own moment. "Good," fiercely, to nobody; the knot she retied twice; the empty pot.
- **Viridia:** has her own moment. "I killed it. You were there."; the strawberries as her "fee for listening".
- **Amelia:** has her own moment. She shrieks loudest in the water; "nothing friendly was left in her"; the laugh.
- **Iro:** follows his card, banter that collapses into blurting.
- **Hopper:** has her own moment, refusing the water.

## Source Fidelity (L813–834)
All beats are present and in order: lake, Hopper, the girls treating Amelia as human, heart hurt, doze, Lora's forehead kiss, Viridia's hand, the strawberry patch, the branch, the roll right then left, Iro's description and lines, the Heath taunt, the side cut, "pretty girls", "my High Priest of course", the leg cut, the left punch, the kicks, the tree, whip, neck, lift, "steel", "It's Iro" twice, his confession, "Okay then", the close, the headless body, "No one threatens my girls", the shirt bundle, Lora running with her hair flying, the rapier joke, Viridia setting down the bundle, the wound inventory (side, chest, stomach, back from right shoulder to left hip, the deep thigh cut into muscle), pushed to the ground, the potion saved for the thigh, "already dead", "heck", Amelia vanishing, the salve used up, Amelia's pile, forty minutes, "Yep", "And?", bloody tears, "I wish you could have seen it", the council in full, good luck, "would you really", the cheating, the loophole, the clothes, the temple.

Additions are texture only: the swim games, Viridia's "I killed it", the ants, the "fee". All are consistent with Ch.18, where Viridia killed the snake with Hopper present. **Nothing invented in plot, lore or spells.**

**Logic finding:** L124 "Bal knew how" claims Bal understands how they knew where he was. The ring only explains how they knew **Heath was dead**. Six paragraphs later Bal says "I just don't get how they knew we were here," and the source's answer, Raizen's teleporting, comes later. Scope L124 to Heath's death (F1).

## Whip note (Ch.20 → Ch.21 back to back)
**Not repetitive in function, so no rewrite is needed.** Ch.20 uses the whip three ways (strike, wrist-wrap, fling). Ch.21 uses it once, with a different purpose (neck, haul, lift, kill), and the images are new: "hand over hand without using his hands", "no more fuss than a mouth opening". All of it is source-driven.

The one echo is the open/close bracket, which is described in full both times. Compare Ch.20's "split open on its own… the split there closed over behind it until the skin was smooth" with Ch.21's "parted down its middle, by itself… the skin closed over it". That is acceptable because the author's ruling requires both beats. Optional: drop ", by itself," at L108, since Ch.20 already taught it.

**Advisory to the author (spell-repetition watch):** the whip has now carried the action peak of two consecutive chapters. It is not yet worn. Update the ledger, and watch the next uses for function variety.

## The Tomorrow Test
**What the reader remembers:** Bal walking out of the woods with strawberries knotted in his shredded shirt, red to the elbow, unsure which of the red is his.
**Anchor type:** BOTH. The image is the strawberries. The quotes are "No one threatens my girls" and "Would you believe I fell on my rapier?"
**Verdict:** ANCHOR EXISTS. It is not repeated from another chapter's anchor type.

## Shareability
"He gets jumped picking strawberries, beheads the guy with a blood whip, and carries the berries home in his ruined shirt."

## Reader Reports
- **The Devourer:** No stopping point. The branch snap at w850 grabs, and the council reads quickly in Amelia's voice. They might skim the second retelling of the fight (L184), but it is short.
- **The Critic:** Would underline L36, L144 and L182. Would be disappointed by the glossing of Hopper (L18, L48) and the over-explaining "Nobody kept fighting with a sword in his leg."
- **The Hostile:**
  - "Bal knew how" contradicts L170 (F1).
  - No sword is in his leg (F2).
  - "A hundred mornings" against Ch.18's three a week for six weeks (F3).
  - Would ask how Bal links "Heath" to the grey-haired bandit. L124's "back on the Whitehaven road" carries it, which is acceptable.
  - Lora's "Good" at his hiss could read as glad of his pain (F14).
- **The Casual Reader:** Likes them all. Lazy lake, then a jolt, then being fussed over. Would keep reading. The vibe is warm, with no guilt residue.

## Cross-Reader Matrix
| Issue | Devourer | Critic | Hostile | Casual | Severity |
|---|---|---|---|---|---|
| L124/L170 contradiction | – | ✓ | ✓ | – | SHOULD FIX (logic, fix first) |
| Gesture clusters (stop/turn/posture) | – | ✓ | ✓ | – | SHOULD FIX (cap) |
| #11 glosses | – | ✓ | ✓ | – | SHOULD FIX (cap) |
| "sword in his leg" / "hundred mornings" | – | – | ✓ | – | INVESTIGATE |
| Echoes of Ch.16/17/19 phrasing | – | ✓ | – | – | INVESTIGATE |

## Revision Recommendations (Ranked: cut or swap only; no plot added)
| # | Location | Problem type | What happens now | Why it fails | Revision direction | Project rule? |
|---|---|---|---|---|---|---|
| F1 | L124 | Logic | "Bal knew how." | It contradicts L170, "I just don't get how they knew we were here." The ring explains Heath's death, not Bal's location. | → "How they had known Heath was dead, at least, Bal could guess." Keep the next two sentences. | No |
| F2 | L102 | Logic / Style #11 | "The man had not been expecting that. Nobody kept fighting with a sword in his leg." | The leg was cut, not run through, and the sentence glosses the beat. | Cut "Nobody kept fighting with a sword in his leg." | No |
| F3 | L70 | Continuity | "as Lora had drilled him on a hundred mornings" | Ch.18 has three mornings a week for six weeks. | → "as Lora had drilled him all those mornings" | No |
| F4 | L154 | Character (gesture: stopping 3/400w) | "Viridia and Amelia came up behind her, and stopped." | Stopping cluster with L120 and L146. | → "Viridia and Amelia came up behind her." | No |
| F5 | L162 | Character (gesture: turning 3/270w) | "Amelia had straightened up. She had turned toward the woods, and nothing friendly was left in her." | Turning cluster with L146 and L150. It also adds a posture beat. | → "Amelia's eyes had gone to the woods, and nothing friendly was left in her." (source: "looked to the woods") | No |
| F6 | L158 | Character (posture/hand/chest) | "Amelia set a hand flat against his breastbone and sat him down on the grass." | Third hand beat and third chest beat in under 200 words; posture cluster. | → "Amelia pushed him down onto the grass." (source verb) | No |
| F7 | L146 | Character (posture) | "Lora was sitting up with her glasses on again." | Posture cluster at w2020–2300. | → "Lora had her glasses on again." | No |
| F8 | L184 | Character (posture) | "They sat by the lake and ate and talked and waited for her." | Posture cluster with L188 "sat down cross-legged" (source). | → "They ate by the lake and talked and waited for her." | No |
| F9 | L18, L38, L42 | Character (posture 6/530w; "stretched" doubled) | "climbed out and stretched himself along the rock beside Hopper" / "Bal eased himself upright to see where the others had gone." / "and stood without waking anybody." | Bal has 3 posture beats in 330 words, on top of Hopper's, Lora's, Amelia's and Viridia's sleeping positions (which the source requires). | L18 → "climbed out and joined Hopper on the rock, still at her post."; L38 → "Bal raised his head to see where the others had gone."; L42 → "and got clear of them without waking anybody." | No |
| F10 | L182 | Character (props 3/360w) | "made one pile for Amelia and set it apart, on a flat stone where the ants would have to work for it" | Set-down cluster with L156 and L180. | → "made one pile for Amelia, on a flat stone where the ants would have to work for it" | No |
| F11 | L18, L48 | Style #11 | "Hopper put her nose against his wet shoulder, once, as if to say he should have listened, and resumed guarding the water." / "thumped her tail once against the rock, which meant yes." | Glosses that explain the dog, and a doubled "once". | → "Hopper put her nose against his wet shoulder and went back to guarding the water." / "thumped her tail against the rock." | No |
| F12 | L226 | Style (word repeat) | "Amelia still sounded amazed by it." | Echoes "Her cheeks were still streaked" (L218) within 100 words. It is "still" number 7 in the chapter. | → "Amelia sounded amazed by it." | No |
| F13 | L98, L102, L36 | Style (cross-chapter echo) | "swept low, for Bal's legs, and the blade bit into the meat of Bal's right thigh" (Ch.16 used both phrases in Heath's fight); "His head snapped back" (Ch.17); "Her mouth curved" (Ch.19) | Second uses of phrasing from the same kind of scene. | → "swept low, and the blade bit deep into Bal's right thigh."; → "His head rocked back"; → "The corner of her mouth went up for a second in her sleep and then forgot to." | No |
| F14 | L160 | Character (clarity) | "Lora said 'Good,' fiercely, to nobody." | Can read as Lora being glad he is hurting. | Optional: → "and Lora said 'Good,' fiercely, to the potion." | No |
| F15 | L16 | Character (eyes, borderline) | "Lora floated on her back with closed eyes and her glasses left safe on her towel" | Eyes at w185, w450 and w685 are exactly 500 apart. | → "Lora floated on her back with her glasses left safe on her towel" | No |

### Fix order: F1–F3 (logic/continuity) → F4–F10 (gesture caps) → F11 (#11) → F12–F15 (prose)

## Strengths to PRESERVE
- The anchor paragraph (L142–144) and "The strawberries had held up better than he had." (L182).
- "Her mouth … then forgot to" (L36): keep the "forgot to" ending in the F13 swap.
- The flat, unremarked kill: "Okay then." / "He closed the loop with a thought." / "No one threatens my girls," Bal told it.
- The two-line ring payoff (scope only per F1).
- Hopper's refusal opening; "Heath meant nothing to Bal." (L74).
- Amelia's council voice ("Positively purple", "Gone, in the middle of a word").

## PATH TO 8.5
- **Characters 7.5 → 8.5 requires:** no gesture class at 3+ inside 500 words. Apply F4–F10. Re-count turning and posture in w2020–2650 after editing; F5–F8 together leave each class at 2 or fewer. Do not add new stage business to fill the gaps.
- **Prose 7.5 → 8.5 requires:**
  - #11 under 0.8/1K. F2 and F11 leave 1 instance, 0.3/1K.
  - The L124 logic contradiction removed (F1).
  - The continuity slip fixed (F3).
  - The underlines (L36, L144, L182) are already there.
  - F12 and F13 remove the echoes.

## VERDICT
**POLISH.** Floor 7.5 / Average 8.2; Casual 8.5. Below the 8.5 gate. F1–F15 are surgical (cuts and swaps, no plot) and project the chapter to Floor 8.5 / PASS.

BIAS CHECK: This evaluation was produced by the same system that wrote the prose. Confidence in scores above 8.0 requires external validation (beta readers, editors, comp analysis).

## Revision applied (2026-10-21, book-editor, r1)
F1–F15 applied, including optional F14 ("to the potion") and the ", by itself," cut at L108. Ring payoff now reads "How they had known Heath was dead, at least, Bal could guess." "No one threatens my girls." and the anchor are untouched. ~3,260 words.

**Wording changed from the quoted swaps (book-wide repeat gates tripped):**
- F13 L36 → "She smiled for a second in her sleep and then forgot to." ("corner of her mouth" self-repeats Ch.2.)
- F6 → "Amelia got him down onto the grass." ("pushed him down onto" self-repeats Ch.16.)
- F7 → "Lora's glasses were back on." ("Lora had her glasses" self-repeats.)
- F11 L18 → "and resumed her watch on the water." ("went back to" was at 3 uses book-wide.)
- F9 L38 → "Bal lifted his head" ("Bal raised his" was at 3 uses book-wide.)
- F5 → "Amelia was facing the woods, and nothing friendly was left in her." ("Amelia's eyes had gone" made a looks cluster with "studied him" and "looking enormously pleased", 3 in 360w.)

**Extra re-count fixes (cuts/swaps only):** "He stood in the lake" → "He waded into the lake"; Hopper "considered him from the warm rock"; "He leaned the inch" → "He closed the inch"; Lora "lain down beside him" → "come to share his rock"; "Hopper lay against his good leg" → "Hopper had her chin on his good leg"; "twice she leaned across and retied" → "twice she retied"; "his face had turned young" → "had gone young". The result is that no gesture class reaches 3+ in 500 words.

**Gates (Ch.1–21):** style_check clean · grammar_check 0 errors · voice_wear_check clean (strict) · tic_report --gate clean. Em dashes 0. "the way [x]" 0 as a construction. Similes about 1.5/1K. Glosses: 1 left (L94, from the source), about 0.3/1K.
