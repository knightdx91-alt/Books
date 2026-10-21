# Evaluation: Chapter 23 — Road to Londra
**Evaluator:** book-evaluator | **Date:** 2026-10-21
**Text evaluated:** `manuscript/chapter-23.md` (2,211 words of prose; target 2,200, range 2,000–2,600: on spec).
**Read first:** STATE.yaml (decisions), book CLAUDE.md, project/STYLE_CONSTRAINTS.md, character-bible.md, outline Ch.23, manuscript/chapter-22.md (ending), chapter-18.md (the water snake, L50–68), chapter-06.md (Viridia's crackling sygl), Sygl_Complete.txt L859–871, evaluations/chapter-21-eval.md.

## HEADLINE
**CVI-Launch:** 8.4 (7.9 + 0.5 strong anchor) | **CVI-Legacy:** 6.0 | **Genesis Floor:** 7.5 | **Genesis Average:** 8.2
**Engagement Type:** Self-Insertion (primary) / Empathy (secondary) / Fascination (tertiary)
**Divergence Alert:** 0.9 (Launch over Floor), under 2.0. Mechanical caps hold the floor; the content is at 8.5.

**VERDICT: POLISH (FAIL at the 8.5 gate).** Two caps:
- **Characters 7.5:** the looks/watching class reaches 3+ inside 500 words three times, and the opening stacks prop business (collar, buttons, reins, water skin, buttons, reins) inside 450 words.
- **Prose 7.5:** Pattern #11 (explanatory extension) at 4 instances = 1.8/1K, over the commercial 0.8/1K line.
Every fix below is a cut or a word swap. No plot is added. With F1–F10 applied the chapter projects to **Floor 8.5 / Casual 8.5: PASS.**

## Gate tools (scratch copy, Ch.1–23 at `/tmp/claude-0/-home-user/925d8686-989e-5134-a9ef-2d597d7cac42/scratchpad/ev23/manuscript/chapters/`)
- `voice_wear_check.py`: **clean** (strict). The 2 cross-chapter self-repeats are allowlisted.
- `tic_report.py --gate`: **clean.** Ch.23 auto-recurrence 0; and-chains 1 (cap 9); negation pivots 0; adds nothing to the book-wide gesture table.
- `style_check.py` (ch.23 alone): **clean.** Simile 3.2/1K, adverb 7.2/1K, **em dashes 0**. "the way" similes: 1 (L56), within cap.
- `grammar_check.py --file chapter-23.md`: 0 errors.
- `tic_report.py --echoes 23`: 26 second uses. Three are worth varying because they sit in similar scenes: "Heads came around" (Ch.20 L14, also a crowd turning to look at Viridia), "undone the top" button (Ch.20 L8, also a clothes-for-a-role scene), "and watched them go" (Ch.14 L182, a parting). See F7.
- Note: the gate does not see the class failures below; the 500-word hand count does. The gate's chapter cap (4 per class, or 1 per 1K) is not breached; the 500-word cluster rule is.

## Source fidelity (L859–871)
Every source beat is present and in source order: the goodbye; Lora's "Every one else is beneath you" (L10); Bal checking the sun to give Lora more time (L34); falling in love with the Vampire Goddess (L36); feelings for Lora and Viridia growing, "three beautiful women" (L38); "no illusions… not about to trust his girls' safety to anyone else" (L40); avoid the towns, Fern's provisions (L44); gallop and walk (L46–48); the second-day family, boy and girl on the horses, parents walking, stiffening at the hair, sygls seen while swatting flies, the father **spits once**, "Same as everywhere else… Kysmer" (L52–70); he takes his son's reins (L72); Bal can do nothing (L76); two more days of refugees, some bandaged, Raizen's war reaching ordinary people (L80–82); the fifth day, wall, gate, two guards, the big nasal truncheon guard, Viridia's haughty speech, the young guard's awe and eye inspection, **the hair crackles when she is nervous** (first appearance, L106–108), "It's really rare", "filthy blood mages… my own people", directions to the Three Boars (North Street, third right), "Exactly how rare", Lora: lesser version of Raizen's, the lake and the water snake, "That poor snake never stood a chance", "one scary lady"; the Winespring stable boy, "M'Lady… We were told to expect you." The source shrug becomes lifted eyebrows (good: no shrug).
- Dialogue: author's lines are the base throughout, smoothed for speech, meaning and speaker unchanged. The stable boy's "Your rooms are ready…" correctly rolls to Ch.24.
- No invented plot, character, spell or lore. Register is American ("gotten", "gray", "biscuit").
- Bal's love for Amelia is sincere and warm ("fond of her, and amazed by her, and on one or two occasions a little afraid of her"; "He was falling in love with the Vampire Goddess"). No guilt or dread added.
- The refugee family is seen entirely through Bal. Bal-only POV holds.
- Canon check: "Somebody had taken the hand off for it" (L60) is canon (Ch.4 L51 "That's why they took my hand off"; Ch.1 the stump came with him). The lake image matches Ch.18 L66 (lightning beside the snake's neck).
- Small items (see findings): L48 "Lora checked every horse's feet before she would let anyone sleep" is habit-shaped (an invented habit risk, F8); L18 Viridia's quip is unclear (F9); L114 the fingers flicked at the carts point at the wrong people (F6).
- Ledger: outline Opening is "Lora's etiquette lesson in the saddle"; the chapter opens on 104 words of goodbye first. The source does too, so this is defensible; logged as INVESTIGATE, not gate-blocking (F10, optional).

## Gesture hand count (500-word windows; word positions approximate)
| Class | Instances | 3+ in 500w? | Verdict |
|---|---|---|---|
| Smile/grin | Viridia "grinning at him" w364 | no | OK |
| Laughs | 0 | — | OK |
| Blushes | 0 | — | OK |
| **Looks/watching** | Viridia "peered down her nose" w339; Bal "squinted up at the sun" w438; Bal "stole a sidelong glance" w596 · father "His eyes never left Viridia" w1030; "none of them glanced back" w1094; Bal "watched them go" w1157; Viridia "kept her face to the front" w1157; refugees "found something to study in the road" w1337 · "the kind of look" w1546; young guard "gazing at her hair" w1634; Lora "frowned up the street at Viridia's gray shoulders" w2036; "without a look at it" w2129; "sent Lora a questioning glance" w2145 | **YES, three times:** w339–596 (3 in 260); w1030–1157 (4 in 130); w2036–2145 (3 in 110) | F1, F2, F3 |
| Sitting/posture | "Viridia sat in the middle" w182; Viridia "straightened in the saddle" w339; "Bal sat his horse" w1157; "Bal rounded his shoulders" w1440; stable boy "leaning… stood ready" w2185 | no (but "straight/straightened" ×5 in 520 words, L6, L22, L36) | F4 |
| Freezing/stopping | "they stopped anyway. They stopped the way…" w905 (deliberate doublet); guard "put out an arm to stop them" w1486; Viridia "pulled up short" w1774; "drew up" w2129 | no | OK |
| Turning | "twisted around in the saddle" w104; "Heads came around" w1939; "turned her horse off" w2129 | no | OK (vary "Heads came around", F7) |
| Eyes | "His eyes never left" w1030; "inspect her eyes" w1634 (source); "lifted her eyebrows" w2145 | no | OK |
| Chest/heart | 0 | — | OK |
| Hand holds | 0 (hands appear as sygl-bearers, L58–60, not as beats) | — | OK |
| Tilts / nods / shrugs | 0 / 0 / 0 | — | OK |
| **Prop fiddling** | Amelia straightens the collar w80; Viridia undoes two buttons w182; Lora "held her reins gathered in her left fist and pointed with her right" w239; water skin handed over and back w354; "do your buttons up" w371; "slack reins" w438 (source) | **YES:** 6 in 360 words | F5 |

## Genesis Score (Craft Assessment)

| Dimension | Score | Evidence | Cap Reasons |
|-----------|-------|----------|-------------|
| Originality | 8.5 | Viridia, now a Blood convert, performing a Tempus lady who sneers at "filthy blood mages" while the woman in the sling is two days behind her. The lesson turned into a running joke that pays off: "Viridia thanked him, the once Lora had allowed her" (L126); "She rode through it with her chin up and her buttons done" (L132). "A man on a doorstep forgot the pipe in his hand until it went out." | — |
| Theme | 8.5 | Raizen's war reaching ordinary people, carried by the family and "Nobody had written down the woman in the sling" (L82); protection of chosen family in "he was not about to trust their safety to anyone else". Plenty of texture: soft cheese, the goose "that had other plans", onions on a blanket, the guard's nasal voice. | — |
| Characters | **7.5** | Strong underneath: Lora's bossy-exact register on her own subject ("Lora's voice had none of its usual hedging", true to the card); Viridia needling even in the lesson; the father gets one spit and one line, seen through Bal; the wound radiates ("Bal's own left hand had been born with that mark on it. Somebody had taken the hand off for it."). Chaos 3/4 (irrelevant thought, the guard's mother L98; triggered memory, L60, returns to the scene; "it had gone straight through him"). | **CAP 7.5:** looks class 3+/500w three times; prop cluster 6 in 360 words. See table. |
| Prose & Voice | **7.5** | Underlines: "They stopped the way people do when it would be worse not to." (L56). "Nobody had written down the woman in the sling." (L82). "One beautiful woman who wanted to be with him would have been plenty for an orphan from Saint Andre's. He had found three." (L38). Rough sentence present: "He had seen plenty of servants. He had never paid attention to how they stood." Voice under pressure: the clipped run at the family (L58–76). | **CAP 7.5 (#11):** 4 explanatory extensions = 1.8/1K: L36 "Amelia had straightened a collar that did not need it, and it had gone straight through him" (re-explains L6); L62 ", which in Raizen's country these days amounted to one crime"; L74 "he could hand over none of it without giving the three of them away" (also a logic snag: "blood in his veins" and "the Blood sygl" cannot be handed over); L82 "That was how it had always worked. Soldiers fought soldiers, and the farms went on farming." Also two spent images: "threads of… light" (Ch.6 L13) at L108, and the crack felt "in his teeth" (Ch.18 L66) at L142. |
| Pacing | 8.5 | Road episodic done right: a warm lesson, a gallop compressed to one paragraph, a hard stop at the family, two days in four lines, a slow gate scene with comic deceleration, the streets, then a four-line close. Value shift: safe and fond → recognized and expected in enemy country. Hook: "We were told to expect you." | — |
| Emotion | 8.5 | Anchor lands: "The father spat on the ground. / It landed in the dust between his boots and the hooves of Bal's horse. His eyes never left Viridia." Emotional surprise: the guard's nasal voice and his mother at the most dangerous moment of the trip; Viridia's grin ruining the noble act. Care through vulnerability: the children "too small for the saddles, their feet nowhere near the stirrups". The love beat is warm and unforced. | — |
| Engagement (Dim 7) | 8.5 | Self-insertion: the outcast with three women he cannot believe his luck with. Empathy: the refugees. Fascination: the masquerade at the gate and the unexplained "expected". | — |
| **FLOOR** | **7.5** | | Characters, Prose |
| **AVERAGE** | **8.2** | | |

## CVI-Launch Breakdown
| Input | Score | Evidence |
|-------|-------|----------|
| Commercial Pacing | 8.5/10 | 2.2K words, a fast gallop paragraph, a hard hook. |
| Tomorrow Test | 3 anchors → 9 | IMAGE: the spit in the dust; IMAGE: the hair lifting and crackling at the gate; QUOTE: "After passing filthy blood mages on the roads, I'll be glad to be among my own people." |
| Casual Reader | 8.5/10 | Warm, funny lesson; a family you feel for; a gate scene with real risk. |
| Shareability (quote/plot/emotional) | 3/3/3 → 6.0 | "He had found three"; Viridia's sneer as cover; the children on the horses. |
| Concept Pitch | yes → 10 | An outcast blood mage and his girls ride into enemy country disguised as a lady and her servants. |
| Human Closeness | partial → 5 | The love beat and the trio; half the chapter is road and gate. |
| **CVI-Launch** | **7.9 + 0.5 = 8.4** | |

**CVI-Legacy:** Originality 8.5 (×.30) + Theme 8.5 (×.25) + Cultural vocabulary 2 (×.20) + Re-readability 4 (×.15) + Identity 3 (×.10) = **6.0**.

## Anti-AI Scan (20 Patterns), 2,211 words
1. Forced symmetry: found, 1 (0.45/1K, minor): "Viridia kept her face to the front. Lora kept quiet." (L74)
2. Empty poetic vocabulary: clear
3. Automatic rule of three: found, 1 (minor): "fond of her, and amazed by her, and… afraid of her" (L36), deliberate, acceptable; also the triple gesture stack at L22 (F4)
4. Em dashes: clear (0)
5. Empty metaphors: clear
6. Dramatic "And" openings: found, 1 (minor): "And he was not about to trust their safety…" (L40), source-driven
7. Pseudo-philosophical closings: clear
8. Excessive parallelism: clear
9. Overly smooth transitions: clear (section breaks do the work)
10. Described emotions: found, 1 (minor): "He was falling in love" (L36), source line, keep
11. **Explanatory extension: found, 4 (1.8/1K, strong):** L36, L62, L74, L82 (see Prose). Caps Prose.
12. Binary negation: clear
13. Precision flex: clear
14. Emotional control demonstration: found, 1 (minor): "He could not help them. Bal clicked his tongue to his horse and rode on." (L76), source beat
15. Authoritative description: clear (Bal guesses: "Their parents, Bal guessed"; "North Street, Bal assumed")
16. Philosophical asides: found, 1 (minor): L56 "the way people do when it would be worse not to", earned; keep
17. Clean dialogue: clear (the lesson has interruption and play)
18. Thematic echo chamber: clear
19. Graduated reveal: watch: the chapter, like Ch.21 and Ch.22, closes on an unexplained line; source-driven, not penalized
20. Emotional temperature report: clear
**Total: 7 patterns found, all but #11 minor. Commercial clean range (0–8).**

## Character Chaos Check (Bal)
- Irrelevant thought: present (the guard's cold and his mother, L98)
- Cognitive distortion: absent
- Unprompted memory: present, triggered by the children's palms and returning to the scene (L60)
- Failed emotional management: present, mild ("it had gone straight through him", L36)
- Voice under pressure: demonstrated (L58–76 shorten and harden)

## Secondary Characters
- Lora: own moment (the lesson, her register switch; the snake memory).
- Viridia: own moment (the grin that ruins it; the crackle; the performed sneer; the detour to the Winespring she does not explain).
- The father: one spit, one line, one tug on the reins. Correct weight.
- The guards: two distinct men (nasal truncheon man, awed young one).

## The Tomorrow Test
**What the reader remembers:** the father's spit landing between his boots and Bal's horse, his eyes on Viridia's hair.
**Anchor type:** BOTH (spit image; "filthy blood mages" quote)
**Verdict:** ANCHOR EXISTS. Matches the outline's anchor.

## Shareability
"She has to play a Tempus lady who hates blood mages, and she's one." One-sentence shareable.

## Reader Reports
- **Devourer:** No stopping point. The gallop paragraph and the two-days paragraph keep it moving; the hook pulls straight into Ch.24.
- **Critic:** Underlines L38, L56, L82. Disappointed by the opening's prop shuffling and by the narrator explaining what the scene already showed (L36 restating the collar, L82 "That was how it had always worked"). Notices "threads of light" reused from Ch.6.
- **Hostile:** L74: how do you hand over "blood in his veins" or a sygl, and why would giving food to strangers on an empty road expose them? L114: Viridia flicks her fingers at the carts in line to enter Londra, who are not blood mages. L18: what does "I've been not looking at Bal for weeks" mean, when they have been together openly? L48: Lora's nightly hoof check reads as a new habit.
- **Casual:** Likes all three of them and the warmth of the opening; the family hits. Would keep reading. Mild drag in the first 450 words of fiddling (collar, buttons, reins, water skin).
- **Devoted:** Will enjoy "the once Lora had allowed her" and the buttons paying off; will notice the teeth callback to Ch.18 and the Ch.6 threads.

## Cross-Reader Matrix
| Issue | Devourer | Critic | Hostile | Casual | Severity |
|---|---|---|---|---|---|
| Looks class clusters (F1–F3) | | x | x | | SHOULD FIX (gate cap) |
| Opening prop shuffle (F4, F5) | | x | | x | SHOULD FIX (gate cap) |
| #11 glosses (F2b, F3b, F6b) | | x | x | | SHOULD FIX (gate cap) |
| L74 logic | | | x | | INVESTIGATE (fix with F2) |
| L114 fingers at the carts | | | x | | INVESTIGATE (F6) |
| Spent images Ch.6/Ch.18 | | x | | | INVESTIGATE (F7) |
| L18 unclear quip | | | x | x | SHOULD FIX (F9) |
| L48 habit risk | | | x | | INVESTIGATE (F8) |

## Revision Recommendations (Ranked)

| # | Location | Problem type | What happens now | Why it fails | Revision direction | Project rule? |
|---|---|---|---|---|---|---|
| F1 | L38 | Character (gesture) | "Then there were these two. Bal stole a sidelong glance. Lora was demonstrating…" | Third look in 260 words (peered L22, squinted L34). | Cut "Bal stole a sidelong glance." → "Then there were these two. Lora was demonstrating how to hold a cup…" | No |
| F2 | L72–74 | Character (gesture) + Logic + Style #11 | "and none of them glanced back" / "Bal sat his horse and watched them go down the road behind him." / "He had food in his saddlebags and blood in his veins, and the Blood sygl he carried, and he could hand over none of it without giving the three of them away." | 4 looks in 130 words; the reason clause is an explanatory gloss and illogical (blood and a sygl cannot be handed over). | L72: "…went after him with the girl, and none of them said another word." L74: "Bal sat his horse until they were well down the road behind him. Kysmer was days off for children that size. Viridia kept her face to the front. Lora kept quiet." (cut the "He had food…" sentence; this also kills the symmetry by leaving the two "kept" lines as the only beat). | No |
| F3 | L140, L146, L148 | Character (gesture) + Style #11 | "She frowned up the street at Viridia's gray shoulders." / "went past the third turning on the right without a look at it." / "Bal sent Lora a questioning glance." | 3 looks in 110 words. | L140: "She frowned." L146: "…until she went straight past the third turning on the right." L148 keep. | No |
| F4 | L22 | Character (posture) | "Viridia straightened in the saddle, raised her chin, and peered down her nose at Bal…" | Gesture triple; fifth "straight/straightened" in 520 words (L6 ×2, L36 ×2). | "Viridia raised her chin and peered down her nose at Bal…" | No |
| F5 | L16 | Character (prop) | "Lora held her reins gathered in her left fist and pointed with her right. "Us. Especially us.…"" | Prop beat number 3 of 6 in 360 words; pure business. | Cut the narration sentence; Lora's speech carries it. | No |
| F6 | L36, L62, L82, L114 | Style #11 / Logic | L36 "Amelia had straightened a collar that did not need it, and it had gone straight through him." L62 ", or for being the parents of blood mages, which in Raizen's country these days amounted to one crime." L82 "That was how it had always worked. Soldiers fought soldiers, and the farms went on farming." L114 "She flicked her fingers at the line of carts behind them." | L36 re-explains L6; L62/L82 gloss the source line; L114 points the insult at Tempus travellers, not blood mages. | L36: "The goodbye at the gate was still with him. It had gone straight through him." L62: end at "for being blood mages." L82: cut "That was how it had always worked." (keep "Soldiers fought soldiers, and the farms went on farming."). L114: "She flicked her fingers back at the road they had come by." | No |
| F7 | L108, L142, L132, L12, L74 | Style (spent image / echo) | "Thin threads of blue light ran along it" (Ch.6 L13 "Tiny threads of light"); "He had felt it in his teeth." (Ch.18 L66 "hit Bal in the teeth"); "Heads came around" (Ch.20 L14); "She had undone the top two" (Ch.20 L8); "watched them go" (Ch.14; removed by F2) | STYLE §3: a metaphor used once is spent. | L108: "Small blue sparks ran along it and snapped out." L142: "Bal remembered. He could still smell it." L132: "People stopped what they were doing wherever Viridia passed, a good many of them." L12: "She had unfastened two of them before…" | No |
| F8 | L48 | Character (invented habit risk) | "Lora checked every horse's feet before she would let anyone sleep." | Reads as a standing habit not in source. | Make it a single act: "The first night Lora checked the horses' feet before she lay down." or cut. | No |
| F9 | L18 | Voice / clarity | "I've been not looking at Bal for weeks. I'm a natural." | Meaning unclear; nothing establishes her ignoring Bal. | "Not looking at Bal? I'm a natural." (same speaker, same joke, readable) | No |
| F10 | L6–8 | Pacing (ledger) — optional | Opens on the goodbye; outline Opening is "Lora's etiquette lesson in the saddle". | Ledger deviation, though source-ordered. | Optional: open on L10 "Everyone else is beneath you," and fold L6–8 into L36 as Bal's recollection. Not required for PASS. | No |

### Fix order: F2 (logic) → F1, F3, F4, F5 (gesture caps) → F6 (#11) → F7–F9 → F10 optional.

## Strengths to PRESERVE
- The spit: "It landed in the dust between his boots and the hooves of Bal's horse."
- "They stopped the way people do when it would be worse not to."
- "Nobody had written down the woman in the sling."
- "He had found three." and the whole L36–40 love passage: warm, sincere, unhedged.
- The guard's mother (L98); "the once Lora had allowed her"; "her chin up and her buttons done".
- The crackle's first appearance, at the young guard's inspection, tied to nerves as the source has it.
- Zero em dashes, zero nods/shrugs, Bal-only POV, the source shrug turned into eyebrows.

## PATH TO 8.5
- **Characters 7.5 → 8.5 requires:** no gesture class at 3+ in 500 words. Apply F1 (L38), F2 (L72–74), F3 (L140/146), F4 (L22), F5 (L16). After these, looks peak at 2 per window and the opening props drop to collar, buttons, water skin (each doing work). The chaos and cast distinctness are already 8.5.
- **Prose 7.5 → 8.5 requires:** Pattern #11 under 0.8/1K (≤1 instance). Apply F2 (L74 sentence cut) and F6 (L36, L62, L82). The citable close-book sentences already exist (L56, L82's last line). F7 clears the two spent images so the Critic has nothing to dock.
- Projected after F1–F9: Characters 8.5, Prose 8.5. **Floor 8.5, Average 8.5, Casual 8.5: PASS.**

## VERDICT
**POLISH.** Floor 7.5 (Characters, Prose), Average 8.2. Every fix is a cut or a word swap; no plot is added.

BIAS CHECK: This evaluation was produced by the same system that wrote the prose. Confidence in scores above 8.0 requires external validation (beta readers, editors, comp analysis).

## Revision applied (2026-10-21, book-editor, r1)
- **F1** cut "Bal stole a sidelong glance." **F2** "none of them said another word"; "Bal sat his horse until they were well down the road behind him."; "He had food…" sentence cut. **F3** "She frowned."; "went straight past the third turning on the right." **F4** "Viridia raised her chin and peered…". **F5** Lora's reins sentence cut.
- **F6** L36 "It had gone straight through him."; L62 ends "for being blood mages."; L82 "That was how it had always worked." cut; L114 "flicked her fingers back at the road they had come by."
- **F7** "Small blue sparks ran along it"; "He could still smell it."; "unfastened two of them"; "Heads came around" replaced with **"People nudged each other wherever Viridia passed"** (the quoted "People stopped what they were doing" would have put the stopping class at 3 in ~250 words with "pulled up short" and "drew up").
- **F8** cut (safest against an invented habit). **F9** "Not looking at Bal? I'm a natural." **F10** not applied (opening is source-ordered; the fold would rework a preserved passage).
- Kept: the spit + Kysmer line, the crackle, "We were told to expect you." Prose ~2,090 words (range 2,000–2,600).
- Recount: no gesture class 3+ in 500 words; #11 glosses ≤1 (≈0.5/1K); em dashes 0; "the way" 1.
- Gates: style_check (dir) clean; grammar_check (dir) clean; voice_wear_check clean (strict); tic_report --gate clean (scratch copy Ch.1–23 at `/tmp/claude-0/-home-user/925d8686-989e-5134-a9ef-2d597d7cac42/scratchpad/ed23/`).
