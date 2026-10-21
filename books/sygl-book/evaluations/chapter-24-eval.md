# Evaluation: Chapter 24 — The Winespring Inn
**Evaluator:** book-evaluator | **Date:** 2026-10-21
**Text evaluated:** `manuscript/chapter-24.md` (4,983 words of prose; target 4,900, range 4,500–5,300: on spec).
**Read first:** STATE.yaml (decisions), book CLAUDE.md, project/STYLE_CONSTRAINTS.md, project/foundation.md (magic ledger), character-bible.md (Mrs. Locklan, James, Aleric, retired list), outline Ch.24, manuscript/chapter-23.md, chapter-22.md (Xavier's briefing), chapter-25.md (opening, for the hand-off), Sygl_Complete.txt L868–912, evaluations/chapter-23-eval.md.

## HEADLINE
**CVI-Launch:** 8.7 (8.2 + 0.5 strong anchor) | **CVI-Legacy:** 6.0 | **Genesis Floor:** 7.5 | **Genesis Average:** 8.2
**Engagement Type:** Self-Insertion (primary) / Empathy (secondary) / Fascination (tertiary)
**Divergence Alert:** 1.2 (Launch over Floor), under 2.0. The floor is held down by mechanical caps. The content is at 8.5.

**VERDICT: POLISH (FAIL at the 8.5 gate).** There are two caps:
- **Characters 7.5.** Gesture clusters: the look class hits 3+ in 500 words in four places (your scan's w940–1190 cluster is confirmed, and there are three more). The smile class hits 3 in 320 words (James). The posture class hits 3+ in 500 words three times. The chapter also invents a Viridia hair-snap with no source basis (signature risk) and repeats Lora's glasses-push and eyebrow-raise (eyebrow shared with Soren, Ch.13).
- **Prose 7.5.** Pattern #11 (explanatory extension): 5 instances = 1.0/1K, over the commercial 0.8/1K line.

Every fix below is a cut or a word swap. No plot is added. With F1–F17 applied the chapter projects to **Floor 8.5 / Casual 8.5: PASS.**

## Gate tools (scratch copy, Ch.1–24 at `/tmp/claude-0/-home-user/925d8686-989e-5134-a9ef-2d597d7cac42/scratchpad/ev24/manuscript/chapters/`)
- `voice_wear_check.py`: **clean** (strict). It reports 2 cross-chapter self-repeats as WARN, both allowlisted.
- `tic_report.py --gate`: **clean.** Ch.24: and-chains 1 (cap 9), negation pivots 0. Ch.24 is now the book's worst chapter for object handling (3x).
- `style_check.py`: **clean.** Ch.24 simile 2.8/1K, adverb 7.8/1K, **em dashes 0**, "the way" similes 0.
- `grammar_check.py --file chapter-24.md`: 0 errors. It misses L294 "then stir" (F13).
- `tic_report.py --echoes 24`: 87 second uses, nearly all neutral. The ones to vary are "up her nose and" (Ch.12 glasses-push), "eyebrow went up" (Ch.13 Soren), "something close to" (Ch.23, the chapter before), and "later she said and" plus the unbothered-nudity beat (Ch.3 Amelia). See F10 and F17.
- The gates pass while the hand count fails. The gate's chapter cap (4 per class, or 1 per 1K) is not breached. The 500-word cluster rule is.

## Source fidelity (L871–909)
- **Every outline beat is present and in source order:** Mrs. Locklan (plump, apron, the envelope from the pocket, "Why, by the sparking hair, of course", the husband); the servants' room; Amelia's letter, quoted and signed only "A", then shredded; **"That girl loves having the last word"** (verbatim, once; the only other "last word" in the book, Ch.8, is a different sense); why the Three Boars question; "Later"; Bal's worry; Lora's "if they're looking at you, they won't be looking at us"; James (forties, sleeves, thinning brown hair, sharp eyes, tidy office, drunk the first day and business the second, the warehouse, dated lids, Cartesia, maple casks, the cheaper brandy, the trader vessel, "If you want the best, it isn't cheap", the haggle, delivery to the Winespring); stew and bread; "You could have bought brandy here"; "Not Ventish brandy"; blood darts and Bal's no (they must get out alive, the rapier line); **the nightstalker poison exactly as the source gives it** (24h dormant, lethargy and hard breathing, heart stops ~6h later); the kiss and "You're amazing"; asphodel and ginger; twenty hours; three hours late; the untrained young alchemist and the night-sight potion; the free herbs; she loses herself in her work; "Do either of you know anything about alchemy?"; shooed out; the walk (after school, challenging the others, the jeweler's window once, poison the whole cask); the Three Boars (three stories, white shutters, two chimneys, ten windows a floor, two stable boys, the elbow and the point); "safe behind their walls"; "All they hear is their priests saying how crazy we are"; sweet rolls; Bal's private thoughts (never leaving them, dead or a future, Amelia's certain vengeance as "poor comfort"); Viridia bolts; Aleric (scar through the right eye, no azure robes, early); Lora on Titus/Leon/Aleric; the nightshade; fifteen hours; the clear cauldron; Ms. Summers' praise; the stopper pop; the boot as hammer; "pinning their lives on it"; the knock and the Tempus seal.
- **Dialogue:** the author's lines are the base throughout, smoothed for speech, with meaning and speaker kept. There are two small meaning drifts: F15 (L222 "sure", L250 "counting").
- **Invention check:** no invented plot, character, spell or lore. Small items: the "river" (L92, L128) is invented geography where the source says only "on the water" and "a trader vessel that had come through" (F14). Viridia's hair snapping in the alley (L278) has no source basis (F9). "in the order she'd unpacked it" (L180) has the shape of the retired "Lora reorganizing supplies" quirk (F11). Mrs. Locklan taking the bowl is a harmless invented beat, already logged in the bible.
- **Spells:** none cast. "Blood darts" is Lora's spoken source suggestion, refused. Optionally log it in the foundation magic ledger as "mentioned once (Ch.24), never cast". No spell-repetition flag.
- **POV:** Bal only. Aleric is reported by Viridia, and Bal never sees him, which matches the bible card. **Register:** American, except "Mind you" (L128, F14).
- **Tone:** light and warm. The threat-letter becomes a laugh, the Locklan comedy plays out, the kiss is happy, and Amelia's vengeance is "poor sort of comfort", not dread. This matches the source.
- **Continuity:**
  - L92 "on Wednesdays" contradicts Ch.22 L166 "every other Wednesday" (F13).
  - L338 "brought everyone bolt upright" contradicts Ch.25 L7 "Viridia had not moved since the knock" (F13).
  - L228 "He had missed part of the talk about the poison, between the stew and the bowl" is illogical in this staging. Bal heard Lora's whole explanation after he came back up with the bowl (F13).
  - L198 "She emptied the cup again" follows a cup already drunk, with no refill (F13).
  - The clock arithmetic (brew start ~5 pm, "fifteen hours", done "about five in the afternoon") comes from the source. Hostile-reader note only, no fix required.

## Gesture hand count (500-word windows; word positions are from the prose start. Your scan's offsets run about +140 because they include the header comments)
| Class | Instances (word pos.) | 3+ in 500w? | Fix |
|---|---|---|---|
| Smile/grin | Locklan smile w36; "beamed" w345; Viridia "smiled, slow" w857; **James "one corner of his mouth went up" w1497; Bal "smiled back" w1519; "The corners of James's eyes creased" w1816**; Amelia's remembered smile w3132/3141 (one reference); Lora "smiling" w4466 | **YES:** 3 in 320 (w1497–1816) | F3 |
| Laughs | Viridia laughing w522; James belly laugh w1535; "cracked up" w2950; inn "Laughter rolled out" w3421 (ambient) | no (4 total, at the ≤4 cap; all source) | OK |
| Blushes | 0 | — | OK |
| **Looks/watching** | "without a glance" w240 · **"meant to look" w801; "looked at Viridia" w806; "caught him looking" w850; "people were looking at me" w1006; Lora's "looking at you… looking at us" w1042/1048; "Every face… had gone to the blue hair" w1057** · **"[eyes] took in Bal's coat" w1293; "Bal saw him decide" w1300; "James studied him" w1405** · Locklan "looked at him" w2259; "squinted at the label" w2322 · **"Viridia met Bal's eye" w2819; "stared at it" w2944; "Viridia's eyes went across them" w3217; "People still stared" w3271** · **stable boys "watching the street" w3445; "spotted Viridia" w3463; "She was watching the people" w3511; "Looking at everyone here" w3516; "laid eyes on" w3554; "kept an eye on their backs" w3622** · **"searched the street" w3931; "nobody looking their way" w3944** · "without looking at it" w4311; "watched Lora" w4903 | **YES, four clusters:** w801–1062 (7 in 260: **your flagged cluster, confirmed**); w1293–1405 (3 in 112); w2819–3271 (4 in 452); w3445–3944 (8 in 500) | F1, F2, F4, F5 |
| Sitting/posture | patrons "sat" w70; Viridia "sit down" w531; "stood" w701 · **Lora "on the floor with her back to the bed" ~w2165; "on her knees" ~w2285; "hauled her to her feet" w2414; "knelt… again" w2455; "rocked back onto her heels" w2500** · **"They stood off to the side" w3682; "standing on a corner" w3767; "leaning on the alley wall" w3957** · **"straightened… stretched" w4425; "Bal leaned in close" w4512; "half lying… propped" w4567**; "leaned his whole weight" w4737; "dropped onto the floor" ~w4800; "stood around it" w4815; "Lora stood by the cold grate" w4953 | **YES, three clusters (and a borderline fourth):** w2165–2500 (5 in 335); w3682–3957 (3 in 275); w4425–4567 (3 in 142); w4737–4953 (4 in 216, borderline) | F6, F7, F8 |
| Freezing/stopping | Viridia "stopped", Locklan "stopped too" w311/315 (one sentence); "hands stopped in her hair" w939; "Lora stopped folding" w1017; James "stopped by the final four" w1762; couple "stopped dead" w3179; Viridia "had stopped on the opposite side" w3374 | no | OK |
| Turning | "turned her back to Lora" w703; "turned for home" w3499; "turned it over" w4969 | no | OK |
| Eyes | "His eyes were sharp" w1289 (description); the window glance w3217 (counted under looks) | no | OK |
| Chest/heart | "made Bal's stomach drop" w1875 only (the other "chest"/"heart" hits are the alchemy chest and the poison) | no | OK |
| Hand holds | Bal takes Lora "by both hands" w2414; Bal "caught her there by the arm and drew her" w3912; Viridia "took hold of his sleeve… towing" w4036 / "let himself be towed" w4077 (one beat) | no, but Bal's arm-pull sits 120 words before Viridia's sleeve-pull, which is her owned gesture | F5 (optional swap) |
| Tilts / nods / shrugs / head-shakes | 0 / 0 / 0 / 0 ("jerked his head at the office" once) | — | OK (F3 and F4 each add one, from the source) |
| Prop fiddling | Plot-carrying object actions (bags, letter, stew, vials, packages, cauldron, cask) are source business and are not counted. Fiddles: "wiped the bowl out" w2236; "held a vial to the window" w2322; "Another vial came out" ~w2345 · "Lora wiped the spoon on a rag" w4602; "pulled his boot back on" w4786; "pat her hair flat, push her glasses up her nose" w4905 | **YES (borderline):** w4602–4905 (4 in 303) | F8, F10 |
| Glasses (Lora) | "eyebrow went up over the rim of her glasses" w2077; "glasses had gone crooked" w2437 (keep: best beat); "push her glasses up her nose" w4911 (repeats Ch.12) | 3 in chapter; class recurs book-wide (Ch.10, 12–16, 19, 21) | F10 |

## Genesis Score (Craft Assessment)

| Dimension | Score | Evidence | Cap Reasons |
|-----------|-------|----------|-------------|
| Originality | 8.5 | The lady-and-manservant masquerade played for comedy inside enemy walls. A threat-letter from a goddess that makes its readers laugh. A poison so clear that "what was left looked like you could wash your face in it" (L314), which quietly seeds Ch.25's purification rune. "She looked at him as though he had offered to marry her, and took it away from him." (L160) | — |
| Theme | 8.5 | Chosen family under threat: "Be safe and come home to me" against "If he and the girls died out here, Bal fully believed she would kill Raizen for it… It was a poor sort of comfort." (L268). The ordinary enemy citizen: "All they hear is their priests saying how crazy we are." Plenty of non-thematic texture: the old man with his boots off, the goose, the creaking stairs, dated ale lids, the carter's mule. | — |
| Characters | **7.5** | Strong underneath. Mrs. Locklan over-tells (true to card). James talks money with relish and has the square-edged desk (true to card). Lora goes deep and forgets to surface ("He didn't even know what half the herbs in his own shop were for"). Viridia is haughty in public and needling in private ("She's probably found a shop with a book in it"). Chaos 3/4: irrelevant thought (the stew and Saint Andre's, L146, triggered by the scene and returning to it); failed management (Bal cleaning his boots twice, L186; Viridia checking the window, L194); the body rebels (Viridia laughing so hard she has to sit, L34). | **CAP 7.5:** looks 3+/500w ×4; smiles 3/320w; posture 3+/500w ×3; invented hair-snap signature (L278); Lora glasses-push repeat (Ch.12) and eyebrow (shared with Soren Ch.13; Lora Ch.23). |
| Prose & Voice | **7.5** | Underlines: "At Saint Andre's, meat in a stew had been more of a rumor than an ingredient." (L146). "Just a single *A* at the bottom, with a tail on it that ran on well past where a tail should stop." (L44). "She looked at him as though he had offered to marry her." (L160). "standing on a corner in Londra with sugar on his fingers, he honestly couldn't tell which looked likelier." (L266). Rough sentence present: "Huh," he said. Voice under pressure: the alley run goes short and clipped ("Carts. Shoppers. A dog."). Dialogue ~30%. | **CAP 7.5 (#11):** 5 explanatory extensions = 1.0/1K: L82 "Not one… long enough to tell what color his coat was"; L104 "chosen, he suspected, so nobody would stay in it long"; L138 "A happy brewer forgot a customer quicker than a sore one"; L252 "because it was their job to and it was hot"; L340 "where a manservant ought to be found". Minor ones: L30 "where it would not get kicked", L46 "too fine for anybody to piece together". Grammar slip: L294 "then stir". |
| Pacing | 8.5 | The procedural clock is real and felt: "Twenty hours of brewing, and the priests in two days, and Lora not even started." (L186); "For the next fifteen hours, they did." (L300). Speed variation: a slow, warm inn arrival; James's leisurely sale; the three-hour wait compressed; the alley sprint; the night compressed into two silhouette images; the slow stopper struggle; a two-line hook. Value shift: safe-but-expected → poison in hand, Aleric early, and Raizen's seal at the door. | — |
| Emotion | 8.5 | Anchors land: the letter signed "A" shredded into the grate; the clear spoonful; the boot heel hammering the stopper. Emotional surprise: a death threat on Raizen read as a love letter, and everyone laughs. Body rebel: Viridia's laugh; the cracked-up hallway. Care through vulnerability: Bal's "he would either be dead, or he would need to decide what the rest of his life was for." Techniques: humor, physical sensation, anticipation, longing (the jeweler's window). | — |
| Engagement (Dim 7) | 8.5 | Self-insertion: an outcast loved by three women; "Later," she said, and plainly meant it. Empathy: the quiet future-dread on the corner. Fascination: the masquerade, the poison, and the unexplained early priest. | — |
| **FLOOR** | **7.5** | | |
| **AVERAGE** | **8.2** | | Single-dimension weakness: none over 1.0. Both caps are mechanical. |

Trajectory: same profile as Ch.23 (7.5 floor from the same two mechanical caps). The pipeline fingerprint persists: **look/watching clusters** and **#11 explanatory tails** have now capped two consecutive chapters. Flag both for the Writer pass as standing rules (see Project rule column).

## CVI-Launch Breakdown (Commercial Assessment)
| Input | Score | Evidence |
|-------|-------|----------|
| Commercial Pacing | 8/10 | The clock, the comedy, the alley sprint, and the seal hook. Long at ~5K words, but it moves. |
| Tomorrow Test | 3 anchors (2 image, 1 quote) → 9 | IMAGE: the "A" with the over-long tail, shredded; the clear poison "you could wash your face in". QUOTE: "That girl loves having the last word." |
| Casual Reader | 8.5/10 | Warm, funny, sexy, with a ticking poison. They keep going. |
| Shareability (quote/plot/emotional) | 3/2/2 → 5.5 | MAX 6×0.6 + AVG 4.7×0.4 |
| Concept Pitch | yes → 10 | "Three lovers in enemy territory brew a poison for the priests of the god who wants them dead." |
| Human Closeness | yes → 10 | Banter, the kiss, "Later", the shared sweet roll. |
| **CVI-Launch** | **8.2 + 0.5 anchor = 8.7** | |

**CVI-Legacy:** Originality 8.5×.30 + Theme 8.5×.25 + Cultural Vocab 2×.20 + Re-read 4×.15 + Identity 3×.10 = **6.0** (unchanged from Ch.23).

## Anti-AI Scan (20 Patterns)
1. Forced symmetry: Clear. "Ten windows on the second story. Ten on the third." is source.
2. Empty poetic vocabulary: Clear.
3. Rule of three: Minor. "one bed, one window, and a door" (L30); "Carts. Shoppers. A dog." (L274), 0.4/1K.
4. Em dashes: Clear (0).
5. Empty metaphors: Minor. "as though the house had opinions about guests" (L20), 0.2/1K.
6. Dramatic "And" openings: Clear (dialogue only).
7. Pseudo-philosophical closings: Clear ("They were pinning their lives on it." is source).
8. Excessive parallelism: Clear.
9. Overly smooth transitions: Clear.
10. Described emotions: Clear.
11. **Explanatory extension: Found. 5 strong, 1.0/1K (strong).** See the Prose row. **CAP.**
12. Binary negation opener: Clear.
13. Precision flex: Minor. "the final four" (L128), "Five hard blows" (L326), 0.4/1K.
14. Emotional control demonstration: Clear.
15. Authoritative description: Clear (the Three Boars is source detail; "Bal guessed" hedges).
16. Philosophical asides: Minor. "A happy brewer forgot a customer quicker than a sore one." (L138); "A manservant out on his lady's errands was nobody" (L90), 0.4/1K.
17. Clean dialogue: Minor. False starts present ("Sorry I'm late. Sorry."; "She's fine, Bal."). Mostly orderly turns.
18. Thematic echo chamber: Clear (abundant texture).
19. Graduated reveal: Watch. Calm → anomaly → escalate → close on a hook, the same as Ch.22–23. The clock structure partly breaks it.
20. Emotional temperature report: Clear.

**Total: 8 patterns touched (1 strong, 7 minor). Commercial clean range (0–8).**

## Character Chaos Check (Primary: Bal)
- Irrelevant thought: present (Saint Andre's stew, L146; "sugar on his fingers", L266).
- Cognitive distortion: present, mild ("he honestly couldn't tell which looked likelier").
- Unprompted memory: present, triggered and returning (the stew).
- Failed emotional management: present (boots cleaned twice, L186).
- Voice under pressure: demonstrated (alley, L270–284).

## Secondary Character Chaos
- Lora: has her own moments (roped into the young alchemist's night-sight brew; the 20-hour vigil; "the hardest thing I've done in a while").
- Viridia: has her own moments (the jeweler's window; "I've got nothing after that").
- Mrs. Locklan / James: function-first, but each gets one human beat (the husband; the fond slap on the ale lid).

## The Tomorrow Test
**What the reader remembers:** the letter with no name, just an "A" with a tail that runs too long, torn to snow and tipped into the grate. Then the poison running off the spoon clear as water.
**Anchor type:** BOTH (the "A" and the clear spoon are IMAGE; "That girl loves having the last word" is QUOTE).
**Verdict:** ANCHOR EXISTS.

**Shareability:** "The goddess girlfriend sends a note ahead threatening to kill a god if they get hurt, and they all just laugh."

## Reader Reports
- **The Devourer:** Pulled through by the twenty-hour clock and the early priest. The only drag is the James sale (~900 words), which is carried by his belly laugh and Bal's haggling. They do not stop.
- **The Critic:** Would underline the stew-rumor line, the "A" tail, and the marriage-proposal bowl. Disappointed by look-verbs piling up (L60–82, L242–274) and by tails that explain the joke (L104, L138, L252).
- **The Hostile:**
  - "every other Wednesday" (Ch.22) vs "Wednesdays"
  - "everyone bolt upright" vs Ch.25's motionless Viridia
  - Bal "missed part of the talk" he plainly heard
  - a second cup drained with no refill
  - "then stir"
  - the fifteen-hours arithmetic (source)
  - a river nobody established
- **The Casual Reader:** Likes all three of them. The letter scene is the hook-in. Would buy. 8.5.

## Cross-Reader Matrix
| Issue | Devourer | Critic | Hostile | Casual | Severity |
|---|---|---|---|---|---|
| Look/posture/smile gesture clusters | | ✓ | ✓ | | SHOULD FIX (gate cap) |
| #11 explanatory tails | | ✓ | | | INVESTIGATE (gate cap) |
| Continuity/logic slips (Wednesday, upright, "missed", cup, stir) | | ✓ | ✓ | | SHOULD FIX |
| James section length | ✓ | | | | INVESTIGATE (keep) |

## Revision Recommendations (Ranked). Every fix is a cut or a swap; none adds plot

| # | Location | Type | What happens now | Why it fails | Revision direction | Rule? |
|---|---|---|---|---|---|---|
| F13 | L92, L338, L228, L198, L294 | Logic/Continuity | "on Wednesdays"; "brought everyone bolt upright"; "He had missed part of the talk about the poison, between the stew and the bowl."; "She emptied the cup again."; "then stir, slow and gentle" | Contradicts Ch.22 L166 and Ch.25 L7; Bal heard the whole talk; no refill; tense slip | "every other Wednesday"; "brought Bal bolt upright"; **cut** the "missed part" sentence; **cut** "She emptied the cup again."; "then stirred, slow and gentle" | No |
| F1 | L60, L76, L82 (your w940–1190) | Character (gesture) | "Bal had meant to look at the window. He looked at Viridia." … "caught him looking past the hem of it" … "With how people were looking at me today" … "Every face in the street had gone to the blue hair in front. Not one, that he could recall, had stayed on the manservant behind long enough to tell what color his coat was." | 7 look-class beats in 260 words (also #11) | "Bal had meant to keep to the window. He didn't." / "caught him at it past the hem." / "After today, I'll be noticed everywhere we go." / "It had all been for the blue hair in front. Nobody on that street could have said what color the manservant's coat was." **Lora's line stays verbatim.** | Yes |
| F2 | L96, L104 | Character (gesture) | "They took in Bal's servant's coat and dusty boots, and Bal saw him decide this might be an order." / "James studied him until Bal began to wonder…" / "chosen, he suspected, so nobody would stay in it long" | 3 looks in 112 words (and it sits within 500w of Lora's line); #11 | "Bal's servant's coat and dusty boots plainly said this might be an order." / "James said nothing for long enough that Bal began to wonder what he had gotten wrong." / end the sentence at "hard and straight-backed." | No |
| F3 | L110, L132 | Character (gesture) | "and one corner of his mouth went up" … "Bal smiled back" … "The corners of James's eyes creased." | Smile class 3 in 320 words | **Cut** ", and one corner of his mouth went up"; "The corners of James's eyes creased." → "James shrugged." (the source's shrug; the chapter has none) | No |
| F4 | L200, L206–208, L242 | Character (gesture) / Style | "Viridia met Bal's eye." / "closed it on them. Out in the hall the two of them stared at it." / "People still stared at her hair as they passed" | 4 looks in 452 words; "it" has no antecedent | "Viridia and Bal shook their heads at each other." (source) / "closed the door on them. Out in the hall the two of them cracked up together…" / "Her hair still drew notice, but less than it had at noon." | No |
| F5 | L252, L256, L258, L260, L272, L274 | Character (gesture) | "watching the street go by because it was their job to and it was hot" / "She was watching the people around them. 'Looking at everyone here, you could…'" / "never laid eyes on" / "Bal kept an eye on their backs until they were past." / "and searched the street they'd left" / "nobody looking their way" | 8 looks in 500 words (also #11 at L252) | "…lounging against the stable wall in the heat." / **cut** "She was watching the people around them."; "All these people, you could almost believe…" / "never so much as passed anyone with our sygl" / "Bal kept his pace and let them go by." / end at "…around the corner." / "Nobody hurrying after them." Optional: "caught her there by the arm and drew her" → "caught up with her there and steered her" (keeps the pull Viridia's) | Yes |
| F6 | L156, L164, L178 | Character (gesture) | "She was on the floor with her back to the bed." / "Lora was on her knees with her alchemy chest open" / "She rocked back onto her heels." | Posture 5 in 335 words | **Cut** the first and third; "Lora had her alchemy chest open on the floor, standing vials…" (the source's "pulled Lora up" and "kneels back down" stay) | No |
| F7 | L8, L266 | Character (gesture) | "Six or seven people sat drinking"; "and standing on a corner in Londra" | Posture 3 in 275 words (w3682–3957); borderline at the open | "Six or seven people were drinking in the cool."; "and on a corner in Londra with sugar on his fingers" | No |
| F8 | L308, L314, L320, L326, L328, L346 | Character (gesture) | "Lora straightened at the brazier and stretched" / "Bal leaned in close and could find nothing" / "Lora wiped the spoon on a rag." / "though Bal leaned his whole weight… he dropped onto the floor, pulled his boot off" / "He pulled his boot back on and set the cask" / "Lora stood by the cold grate" | Posture 3 in 142 and 4 in 216; props 4 in 303 | "Lora stretched"; "Bal could find nothing"; **cut** the rag; "put his whole weight on it… In the end he pulled his boot off"; "He set the cask"; "Lora was by the cold grate" | No |
| F9 | L278 | Character (signature) | "Her hair was snapping at the ends." | Not in the source; the crackle is "only where the source has them, never as a signature" (STYLE §2), and it is already spent this chapter (L66) and last (Ch.23) | **Cut** | Yes |
| F10 | L152, L340 | Character (shared gesture) | "Lora's eyebrow went up over the rim of her glasses." / "watched Lora pat her hair flat, push her glasses up her nose, and open the door" | Eyebrow-up shared with Soren (Ch.13 L412) and Lora's own Ch.23; glasses-push repeats Ch.12 | '"You could have bought brandy here," Lora said.' / "watched Lora open the door." Keep "Lora's glasses had gone crooked." (L174), the best of the three. | Yes |
| F11 | L180 | Character (invented quirk) | "packed everything into the chest in the order she'd unpacked it" | The retired "Lora reorganizing supplies" quirk shape | End at "packed everything into the chest" | No |
| F12 | L30, L138, L340 | Style (#11) | ", where it would not get kicked" (with "and set Lora's alchemy chest under the window"); "A happy brewer forgot a customer quicker than a sore one."; ", where a manservant ought to be found," | Explanatory tails (#11 + #16) | "Bal stowed the bags under the bed."; **cut** the aphorism; **cut** the clause. With F1, F2 and F5 this brings #11 to ~2 (0.4/1K). | Yes |
| F14 | L92, L128 | Style / Logic (invented geography, register) | "The river was wide there and slow, the color of tea." / "Mind you, it doesn't stop them…" / "a trader vessel that came up the river" | The source gives only "on the water"; "Mind you" is British | "The water there was slow, the color of tea." / "Not that it stops them spending plenty…" / "a trader vessel that came through" | No |
| F15 | L222, L250 | Voice (dialogue meaning) | "If the war goes our way, sure." / "And that's counting every room except the one the innkeeper and his wife slept in." | "sure" muddles the source's question; "counting every room except" is tangled | "Assuming the war goes our way, you mean?" / "And that wasn't counting the one the innkeeper and his wife slept in." | No |
| F16 | L266 | Voice (at-risk phrase) | "He was never leaving his girls." | Narrator "his girls" is at-risk (bible); already used in Ch.20 narration | "He was never leaving any of them." | No |
| F17 | L6, L60 | Style (echo) | "at something close to a trot" (Ch.23: "with something close to awe"); "entirely unbothered by him" (Ch.3 Amelia, the same nude-"later" beat) | Back-to-back phrase echo; cross-character beat echo | "at nearly a trot"; end the sentence at "long and tan." | No |

### Fix order: F13 (logic) → F1–F11 (character/gesture) → F12, F14–F17 (prose)

## Strengths to PRESERVE
- The letter block (L36–50) exactly as is: the over-long tail on the "A", the flakes in the grate, "Neither of them argued."
- "At Saint Andre's, meat in a stew had been more of a rumor than an ingredient."
- Mrs. Locklan and the bowl.
- The three-hour wait (boots cleaned twice; Viridia checking the window).
- The night compressed into two silhouette wakings; the clear spoonful; the boot-heel stopper and the "fat new dent".
- Bal's corner thoughts (L266–268), which tie back to the grate.

## PATH TO 8.5
- **Characters 7.5 → 8.5 requires:** no gesture class at 3+ in any 500-word window, no invented hair signature, and no shared or repeated Lora face business. F1–F11 do this surgically. Recounted after the fixes: looks max 2 per window (Lora's line counts as one beat); smiles 857 / 1519 / 3132 / 4466, spaced >500; posture max 2; props max 2. Underneath, the character work is already 8.5 (Locklan over-tells, James's square-edged desk, Lora lost in the brew, Viridia's jeweler's-window glance).
- **Prose 7.5 → 8.5 requires:** #11 at or below 0.8/1K. F1 (L82), F2 (L104), F5 (L252) and F12 (L30, L138, L340) cut six tails and leave ~2 (0.4/1K). The stopping sentence is already there (the stew/rumor line; the "A" tail). Also fix "then stir" (F13).

## VERDICT
**POLISH. Genesis Floor 7.5 / Average 8.2 / Casual 8.5. FAIL at the 8.5 gate.** Apply F1–F17 (cuts and swaps only, no plot) and the chapter projects to Floor 8.5, Casual 8.5: PASS. Re-run the 500-word hand count after the edit.

BIAS CHECK: This evaluation was produced by the same system that wrote the prose. Confidence in scores above 8.0 requires external validation (beta readers, editors, comp analysis).

## Revision applied (2026-10-21, book-editor)
- **F1–F17 applied as quoted**, with these gate-driven variants (each quoted swap tripped a book-wide repeat gate):
  - F13 "every other Wednesday" → "every second Wednesday" (same meaning as Ch.22; the exact phrase recurred).
  - F2 "James said nothing for long enough that Bal began to wonder" → "James kept quiet until Bal wondered" ("long enough that" 3x book-wide).
  - F4 "Viridia and Bal shook their heads at each other." → "Viridia might have guessed, and so might Bal." ("shook their heads" 3x; no gesture added).
  - F5 "Bal kept his pace" → "Bal held his pace"; F8 "put his whole weight" → "threw his whole weight".
  - F15 dropped the "Viridia" after "you mean?" ("She went quiet"); F10 brandy line left untagged by alternation ("Lora said. Not" 3-gram).
  - Mid-speech cuts (F6 heels, F8 rag, F9 hair-snap, F13 cup) merged back into single quotes.
- Kept verbatim: the letter block signed "A", "That girl loves having the last word.", the nightstalker poison facts, the "glasses had gone crooked" beat, the knock and Tempus seal ending.
- Recount: no gesture class 3+ in any 500-word window (gestscan clean except non-gesture "chest"/"heart" nouns); #11 tails ~1 (L46 letter-block clause, preserved) ≈ 0.2/1K; em dashes 0; "the way" 0. Prose ~4,740 words.
- Gates (Ch.1–24): style_check clean; grammar_check clean; voice_wear_check clean (strict); tic_report --gate clean.
