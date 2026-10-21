# Evaluation: Chapter 22 — The Plan
**Evaluator:** book-evaluator | **Date:** 2026-10-21
**Text evaluated:** `manuscript/chapter-22.md` (3,552 words of prose per style_check; target 3,700, range 3,300–4,100, so on spec).
**Read first:** STATE.yaml (decisions), book CLAUDE.md, project/STYLE_CONSTRAINTS.md, project/foundation.md, character-bible.md, outline Ch.22, manuscript/chapter-21.md, chapter-18.md (Fern's war room, Thad's stone), chapter-11.md (the priests' room), Sygl_Complete.txt L835–859, evaluations/chapter-21-eval.md.

## HEADLINE
**CVI-Launch:** 8.5 (8.0 + 0.5 strong anchor) | **CVI-Legacy:** 6.1 | **Genesis Floor:** 7.5 | **Genesis Average:** 8.2
**Engagement Type:** Self-Insertion (primary) / Empathy (secondary) / Fascination (tertiary)
**Divergence Alert:** 1.0 (Launch over Floor), under 2.0. Same shape as Ch.19–21: the hand count caps Characters; the content is sound.

**VERDICT: POLISH (FAIL at the 8.5 gate).** Source fidelity is very good: every beat of L835–859 is present, in order, with the author's lines as base. "No" and "Damn their war. I will kill him." land as the anchor. Amelia is fierce and loving, never manipulative. What Bal does not witness (Lora vs Marcus, Viridia among the soldiers, Amelia's fear) arrives reported or observed. No spell invented, no em dashes, the map-under-a-finger image avoided (Xavier leans over instead). The floor comes from **gesture clustering** (posture, stopping, prop handling, looks: four classes at 3+ inside 500 words) plus a **timeline slip** (L30) and a **fire/order contradiction** in the last two paragraphs. All fixes are cuts or word swaps; with F1–F16 applied the chapter projects to **Floor 8.5 / Casual 8.5: PASS.**

## Gate tools (scratch copy Ch.1–22 at `/tmp/claude-0/-home-user/925d8686-989e-5134-a9ef-2d597d7cac42/scratchpad/ev22/manuscript/chapters/`)
- `voice_wear_check.py`: **clean** (no retired phrases, no device over cap; 2 cross-chapter self-repetitions are WARN only).
- `tic_report.py --gate`: **clean.** Ch.22 and-chains 1 (cap 9), negation pivots 0. Book-wide gesture table: Ch.22 is now the **worst chapter in the book for "object handling" (3x)**; under the gate's cap of 4, but see the hand count, which finds far more paper/map business than the regex classifies.
- `style_check.py`: clean. Simile 1.4/1K, adverb 9.6/1K, em dashes 0.
- `grammar_check.py`: 0 errors.
- `tic_report.py --echoes 22`: 48 second-use echoes, mostly function phrases. Worth varying: "waved them all to" (Ch.20, Amelia; here Xavier), "and her cheeks red" (Ch.16, Lora again), "one breath. Then" (Ch.16).

## FULL gesture hand count (w = prose word position; 500-word windows)
| Class | Instances | 3+ in 500w? | Verdict |
|---|---|---|---|
| Smile/grin | 0 ("trying not to be pleased" L152) | no | OK |
| Laughs | Bal laughed w2684 (source); girls giggling w2952 (source); Bal chuckled w3394 (source); "played and laughed" w3540 (source) | no (nearest three span 588) | OK |
| Blushes | Lora "cheeks red" w1698 (exertion); "Lora went pink" w2071 | no | OK; echo F15 |
| Looks/watching | priests "stared" w531; "eyes on the paper" w335; Lora "studying the marks" w2470 (source); "slid her eyes sideways" w2572 (source); "Her attention returned to the map" w2589; glance flicked w3089 (source); "looked from Lora to Viridia" w3280 | **YES**: w2470–2589, 3 in 120 | F4 |
| Sitting/posture | Viridia "tipped her chair" w2619 (source stretch); Bal "pushed his chair back and rose" w2751 (source); Amelia "lying across the bed" w2860; girls "perched on the bed's edge" w2952; "sitting shoulder to shoulder" w3089 | **YES**: 5 in 470 | F5 |
| Freezing/stopping | Thad "stopped to breathe" w274; Amelia "stopped walking" w3113; "had halted by the bedpost" w3280; "stayed rigid through one breath" w3348 | **YES**: 3 in 235 | F6 |
| Turning | "turn sideways" w65; "turned a page" w795; "turned the sheet over" w2204; "at every turn" w3019; "turned at the washstand" w3089 (source pacing) | no | OK (page-turns go with F3) |
| Eyes | "eyes on the paper"; "Thad's eyes had sunk"; "hair and eyes"; "slid her eyes" | no | OK |
| Chest/heart | "book on her chest" w2860 | no | OK |
| Hand holds/hand beats | robe in one fist, papers in the other w237; palm shown w553; Lora's feint "with her empty hand" w1834; Viridia "flicked a hand at her own head" w1884 + "showed them my palm" (reported) w1890; handshakes w2805 (source); "arms folded tight" w3280; arms around her waist w3348 (source); offered arm + hug w3429 (source) | **borderline**: hands 3 in 60 (w1834–1890); arms 3 in 150 (w3280–3429) | F6, F7 |
| Tilts / nods / shrugs | 0 / 0 / 0 | — | Source nods, head-shakes and Thad's shrug rendered without the words. Good. |
| Prop fiddling (papers/map/pencil) | squared papers w781; "turned a page" w795; "set the paper down" w855; drew papers over w908 (source); pulled map out, drew it to him w1045 (source); "pushed the map aside" w1116 · "ran down to the next line" w2118; "pencil out" w2191; "turned the sheet over" w2204; "put the paper down" w2278 (source); "pulled the map over" w2470 (source) | **YES**, twice: 6 in 335 (w781–1116) and 5 in 352 (w2118–2470) | F3 |
| Cross-chapter | Lora tending Bal's bandage: Ch.21 x3 (bandaged, tied off, "twice she retied the knot") + Ch.22 L276 rewinds them; Lora's pencil: Ch.10, 16, 19, 22 | **becoming Lora's device** | F2, F3 |

## Genesis Score
| Dimension | Score | Evidence | Cap Reasons |
|-----------|-------|----------|-------------|
| Originality | 8.5 | "Boots, mostly." (L6); "a basket that never got any fuller, because a boy kept coming to empty it" (L10); "lacing a pair of boots that were plainly somebody else's"; "The word *they* did not get past either priest." (L128); the girls betting on Amelia's reaction (L222) dramatizes the source's "making comments". | — |
| Theme | 8.5 | Love that protects without controlling: "Would you want me to send Lora and Viridia with somebody else?" against "you're my High Priest. Kill you, and there goes the war." Texture outside theme: the cooking pot clanging the doorframe, the mismatched fourth chair, the drayman's mug. | — |
| Characters | **7.5** | Cast distinct by worldview: Thad blunt and reading off paper, Xavier "more carefully and at greater length", Lora methodical with the map, Viridia physical and plain-spoken ("Nothing she *should* do"), Amelia fierce. Bal's irrelevant thought (the drayman, L182) and Viridia's changed voice (L158). | **CAP 7.5:** posture, stopping, props (x2) and looks at 3+/500w; Lora's bandage-tending and pencil recurring across chapters. |
| Prose & Voice | 8.0 | Underlines: "until now she had never turned a face with nothing in it on him" (L228); "The one word, flat as a table." (L232); "She stayed rigid through one breath. Then she gave." (L266); "the temple and all its boots went out like a lamp" (L274); "The dorm was warm and dark and exactly where they had left it." Rough sentence (source): "We've got a war is what we've got." Voice changes under pressure: the argument runs to clipped lines. | Held below 8.5 by: the L276/L278 fire contradiction; British-leaning "haven't got" x2 and "Go and have" (American register); #11 glosses at 0.56/1K (under the 0.8 cap, but "That much was plain" is pure gloss); two question-form musings within four lines (L182, L186). |
| Pacing | 8.0 | Arrival bustle → council → stair walk → briefing → plan → argument → home. Value shift: a war they cannot win head-on → a plan, and Amelia's flat refusal → her consent. Hook: "Noon and the road were hours off yet." | The two councils (w700–2470) are slowed by 11 bits of paper/map handling (F3). Last paragraph runs backward in time (cards "later", then "They lit the fire"). |
| Emotion | 8.5 | Anchor: the blank face and the flat "No". Surprise: the girls giggling at Bal's face mid-argument (source). Body rebel: Amelia "rigid through one breath. Then she gave." Care: soldiers "scared of getting hurt. They're excited anyway." | — |
| Engagement (Dim 7) | 8.5 | Self-insertion: the boy-High Priest who refuses to send his girls without him and is backed by both of them. Empathy: Amelia's fear "and not only for him". Fascination: the infiltration plan and the noble-lady cover. | — |
| **FLOOR** | **7.5** | | Characters |
| **AVERAGE** | **8.2** | | |

## CVI-Launch Breakdown
| Input | Score | Evidence |
|-------|-------|----------|
| Commercial Pacing | 7.5/10 | Two briefings back to back (source-mandated); the argument at w2900 rescues momentum. |
| Tomorrow Test | 3 anchors → 9 | IMAGE: Amelia's blank face; QUOTE: "Damn their war. I will kill him."; IMAGE: "the temple and all its boots went out like a lamp". |
| Casual Reader | 8.0/10 | Warm, clear, funny argument; the middle is homework. |
| Shareability (quote/plot/emotional) | 3/2/2 → 5.5 | "Damn their war." / "the High Priest is going in as the manservant" / Amelia's fear. |
| Concept Pitch | yes | Outcast becomes a goddess's High Priest and walks into enemy country as a servant to save the war. |
| Human Closeness | yes | The bedroom argument and the dorm evening. |
CVI-Launch = 1.5+1.8+1.6+1.1+1.0+1.0 = 8.0, +0.5 anchor = **8.5**. CVI-Legacy (default weights) = 2.55+2.13+0.40 (vocab 2)+0.60 (re-read 4)+0.40 (identity 4) = **6.1**.

## Anti-AI Scan (20 patterns; commercial thresholds; 3.55K words)
1 Forced symmetry: Found, 1 (0.28/1K) — "Thad said so outright. Xavier said it more carefully..." (minor, characterful).
2 Empty poetic vocabulary: Clear.
3 Rule of three: Found, 2 (0.56) — "horses and lamp oil and wet rope"; the boots/shouting/clatter ladder (L6). Minor.
4 Em dashes: Clear (0).
5 Empty metaphors: Clear.
6 Dramatic "And" openings: Found, 1 — "And Bal would be the lowly manservant" (L184). Minor.
7 Pseudo-philosophical closings: Clear (the close is the source's line).
8 Excessive parallelism: Found, 1 — "Viridia bet on shouting. Lora bet Amelia would simply forbid it." Minor, earned.
9 Smooth transitions: Clear.
10 Described emotions: Found, 3 (0.85) — "Bal liked that"; "She was not angry anymore... She was afraid"; "trying not to be pleased". The middle one is the source's beat rendered as observation.
11 Explanatory extension: Found, 2 (0.56) — "Nobody in Raizen's lands would ever mistake it" (L40); "That much was plain." (L262). Under cap; F10.
12 Binary negation: Found, 1 — "She was not angry anymore... She was afraid". Minor.
13 Precision flex: Clear (the two-or-three ratio is source).
14 Emotional control demonstration: Clear.
15 Authoritative description: Clear (opening has noise and error: the sergeant telling men they are wrong).
16 Philosophical asides: Clear.
17 Clean dialogue: Found, minor — councils are turn-based; the argument has an interruption.
18 Thematic echo chamber: Clear.
19 Graduated reveal: Clear.
20 Temperature report: Clear (thigh mentioned twice, F2/F12).
**Total: 9 present, all minor/moderate; within the commercial clean band (0–8 is clean by count of strong patterns; none strong).**

## Source fidelity (L835–859)
All present and in order: battalion, Eric, decoy + refuge terms; Lora to the weapons master, Viridia out with Hopper, Amelia stays in the bedroom so as not to seem to help; Thad's report (scouts x2, cohort on the cliffs, casualties, "We've got a war is what we've got"); two-or-three-for-one; Xavier's priests-then-High-Priest; Aleric; Three Boars in a week; four or five days; the spies dilemma; Thad on palms and the self-correction; Viridia's inheritance as cover; priests reluctant, Bal won't send her without him; Marcus and the feint, Viridia among the soldiers (reported); bows; the full Londra briefing (south of Pashar, NW, upper class, back half, every other Wednesday, bribe, patrols); the noble-lady plan; danger and consent; Lora on the map and her father; "best shot"; Viridia's stretch and line; Bal's laugh and reply; clothes/Fern/horses by noon; handshakes; "within Raizen's reach"; the blank stare and flat No; giggling; "Then get someone else"; "Would you want me to send..."; "you're my High Priest"; Lora's support; arms around her; "Damn their war"; "Warrior Goddess"; teleport home; played and laughed. Thad's stubble left uncoloured (source slip avoided). Three regular priests matches Ch.18.

**The writer's added staging, judged:**
- **Card game (L276):** ACCEPTABLE. One plain beat that dramatizes "played and laughed"; adds no plot. Keep, but fix the paragraph order (F2).
- **Lora rebinding the thigh (L276):** CUT. It is the fourth Lora-bandage beat in two chapters (Ch.21 bandages, ties off, retied "twice"); it is turning into Lora's device, and the wound is already recalled at L142 and L254.
- **The extra argument exchange (L238–240):** Bal's interrupted attempt is ACCEPTABLE (source: "Bal tried to explain") and gives the dialogue a real interruption. Amelia's "I heard you. All of it. No." should lose its "No.": a second flat No dilutes the anchor, and the source's "No, I don't expect you to do that" follows (F8).
- **Other added lines** (Thad on the landing, "I'll stay put", "Converted. Last night.", "Nobody's going to think less of you"): acceptable; no new information, and "Last night" is right (Ch.19 conversion, Ch.20–21 next day).
- **L132 Iro reasoning** ("Iro had found them that afternoon at a lake nobody had planned to visit"): an inference from Ch.21, not a new motive; keep.

## Character Chaos Check (Bal)
- Irrelevant thought: present (the drayman's mug, L182).
- Cognitive distortion: absent (not required, commercial).
- Unprompted memory: present, triggered and returning (Fern's map, L30; Amelia's bloody tears, L228).
- Failed emotional management: present in Amelia, observed (rigid, then gives).
- Voice under pressure: demonstrated (clipped argument lines).
Commercial 3/4: no chaos cap.

## Secondary Character Chaos
- Thad: own moment (starts to argue, thinks better of it).
- Xavier: own moment (the lingering grip; "had been waiting to").
- Lora: own moment (the feint demonstration nearly ribbing a soldier).
- Viridia: own moment (voice changes about the soldiers).
- Amelia: own moment (the blank face; fear for all three).

## The Tomorrow Test
**What the reader remembers:** Amelia's face going blank and the single flat "No", and "Damn their war. I will kill him."
**Anchor type:** BOTH. **Verdict:** ANCHOR EXISTS (matches outline).

**Shareability:** "Damn their war. I will kill him." texts well.

## Reader Reports
- **Devourer:** Opening bustle and the argument pull; slows in the two paper-heavy councils (w700–1700, w2100–2500). Keeps going for the bedroom scene.
- **Critic:** Underlines L228, L232, L266, L274. Disappointed by the paper fiddling and by "the dorm was warm" followed by "They lit the fire".
- **Hostile:** "A few weeks ago, standing over Fern's map" (L30): Fern's war room was the evening before the conversion, i.e. yesterday (Ch.18 "Now, with Fern's orders given" → Ch.19). "A sword had been in his leg" overstates Ch.21's thigh cut (the Ch.21 eval already corrected the same claim). "Xavier stepped out of his own door": the priests share one room (Ch.11).
- **Casual:** Likes the warmth and the girls laughing at Bal mid-argument; would skim the briefing. 8.0.

## Cross-Reader Matrix
| Issue | Devourer | Critic | Hostile | Casual | Severity |
|---|---|---|---|---|---|
| Paper/map/posture business clotting the councils | x | x | | x | IMPORTANT |
| L30 timeline | | | x | | INVESTIGATE (fix: logic) |
| Fire/order contradiction, last paragraphs | | x | x | | SHOULD FIX |
| Lora bandage/pencil becoming a device | | x | x | | SHOULD FIX |
| Second "No" diluting the anchor | | x | | | INVESTIGATE |

## Revision Recommendations (surgical; no plot added)
| # | Location | Type | What happens now | Why it fails | Revision direction | Rule? |
|---|---|---|---|---|---|---|
| F1 | L30 | Logic | "A few weeks ago, standing over Fern's map, Bal had said..." | Fern's war room was yesterday (Ch.18–19). | → "Standing over Fern's map, Bal had said..." | No |
| F2 | L276–278 | Logic/Character | "The dorm was warm and dark..." / "Lora unwound his bandages..." / "Later there were cards..." / "They lit the fire and played and laughed" | Warm before the fire is lit; time runs backward; Lora's 4th bandage beat in two chapters. | L276 → "The dorm was dark and exactly where they had left it. Viridia shrank Hopper with her collar, and Hopper took the hearth rug. They lit the fire. Later there were cards, and Amelia lost at them loudly. She sat closer to Bal than she needed to all evening, her shoulder against his, and nobody remarked on it." L278 → "Noon and the road were hours off yet. They played and laughed, trying to forget what tomorrow would bring." | Yes: no character gets a recurring caretaking prop |
| F3 | L70, 72, 74, 100, 170, 172, 174, 180 | Character (prop class) | squared/turned/set down/pushed aside; ran down/pencil/turned over | Prop class 6 in 335w and 5 in 352w; Lora's pencil in a 4th chapter. | L70 → "He read from the top sheet in front of him." Cut "He turned a page." (L72). Cut L74 "He set the paper down." Cut L100 "Bal pushed the map aside." Cut "He ran down to the next line." (L170). Cut L172 entirely. Cut "He turned the sheet over." (L174). L180 → "Lora and Viridia had none. Neither did Bal." | Yes: max 2 paper/map handlings per council |
| F4 | L200 | Character (looks) | "Her attention returned to the map." | 3 gaze beats in 120w. | Cut the line. | No |
| F5 | L224, 234, 250 | Character (posture) | "Amelia was lying across the bed with the book on her chest." / "perched on the bed's edge" / "sitting shoulder to shoulder" | 5 posture beats in 470w. | L224 → "He laid it all out for Amelia, from the beginning: ..." L234 → "Behind him, Lora and Viridia burst out giggling." L250 → "Amelia's glance flicked to the girls on the bed, who were following every word." | No |
| F6 | L252, 262 | Character (stopping, arms) | "She stopped walking." / "She had halted by the bedpost, arms folded tight, and she looked" | Stop/freeze 3 in 235w; arms 3 in 150w. | Cut "She stopped walking." L262 → "She was by the bedpost now, and she looked from Lora to Viridia..." | No |
| F7 | L156 | Character (hand) | "She flicked a hand at her own head." | Hand beats 3 in 60w (feint hand, flick, palm). | Cut; "You can see why" carries it. | No |
| F8 | L240 | Voice/Emotion | "I heard you," Amelia said. "All of it. No." | A second flat "No" dilutes the anchor before the source's third. | → "I heard you," Amelia said. "All of it." Keep Bal's interrupted L238. | No |
| F9 | L262 | Style (#11) | "She was not angry anymore. That much was plain." | Gloss explains the observation. | Cut "That much was plain." | No |
| F10 | L76, L210, L56 | Style (register) | "They just haven't got the experience"; "we haven't got that kind of time"; "Go and have your war." | British-leaning in an American-register book. | → "They just don't have the experience" (source wording); "we don't have that kind of time"; "Go have your war." | No |
| F11 | L254 | Continuity | "A sword had been in his leg that afternoon." | Overstates Ch.21's cut (same issue the Ch.21 eval corrected); repeats "that afternoon" from L132. | → "Iro's blade had opened his thigh to the muscle." | No |
| F12 | L186 | Style | "Did a manservant brush the horses down himself...? He would have to ask Lora." | Second question-form musing within four lines of L182. | → "He would have to ask Lora whether a manservant brushed the horses down himself at an inn like that, or left it to a stable boy." | No |
| F13 | L36 | Continuity | "Xavier stepped out of his own door" | Priests share one room (Ch.11). | → "stepped out of the priests' door" | No |
| F14 | L134, L138 | Style (filter) | "Thad started to argue anyway"; "they started to sort out" | "started to" x2. | → "Thad was going to argue anyway, and thought better of it." / "Between them they sorted out..." | No |
| F15 | L144, L166 | Style (echo) | "her cheeks red" (Ch.16 Lora); "Xavier waved them all to the table" (Ch.20 Amelia) | Second-use echoes in like scenes. | → "with her hair falling down and the fight still in her face"; "Xavier made room for them at the table." | No |
| F16 | L40/L118 | Style (optional) | priests "stared" then "both priests staring at it" recalled | Light repetition. | L118 → "Bal thought of Viridia's pale blue hair out on the landing." | No |

### Fix order: F1, F11, F13 (logic/continuity) → F2–F7 (character/gesture) → F8 → F9–F16 (prose).

## Strengths to PRESERVE
"Boots, mostly." opening and its callback ("the temple and all its boots went out like a lamp"); the bandage basket that never fills; "The word *they* did not get past either priest."; the blank face, the flat "No", "flat as a table"; the girls' bets and giggling; "rigid through one breath. Then she gave."; Xavier leaning over the map instead of the spent finger; the reported Marcus spar and the soldiers' courage; the card game as the single "played and laughed" beat.

## PATH TO 8.5
- **Characters 7.5 → 8.5:** apply F2–F7. That clears posture (to 2 in the w2619–3089 window), stopping (to 2), props (to 2 per council), looks (to 2), hands/arms (to 2), and retires Lora's bandage and pencil beats. Re-run the hand count on the bedroom scene (L222–272) after the edit; nothing should be added there.
- **Prose 8.0 → 8.5:** F2 (fire contradiction), F9, F10, F12. The stopping sentences already exist (L228, L274).
- **Pacing 8.0 → 8.5:** F3 removes about 60 words of paper business from the two councils and lets the briefing read as information, not choreography; F2 restores forward time in the close so the hook ("Noon and the road") lands last.

## VERDICT
**POLISH** (Floor 7.5; Casual 8.0). With F1–F16, projected Floor 8.5 / Casual 8.5: PASS.

BIAS CHECK: This evaluation was produced by the same system that wrote the prose. Confidence in scores above 8.0 requires external validation (beta readers, editors, comp analysis).

## Revision applied (2026-10-21, book-editor)
- **F1–F16 applied as quoted:** L30 "A few weeks ago" cut; thigh line → "Iro's blade had opened his thigh to the muscle."; "the priests' door"; close reordered (dark dorm → Hopper → "They lit the fire." → cards → "Noon and the road...") with Lora's rebinding cut and the card game kept; paper business cut to ≤2 per council (squared/turned page/set down/pushed aside/ran down/pencil/turned over); "Her attention returned to the map." cut; posture cluster (lying across the bed, perched, shoulder to shoulder) cut; "She stopped walking." cut; "She was by the bedpost now"; hand-flick cut; "I heard you... All of it." (single "No" kept); "That much was plain." cut; "don't have" x2; "Go have your war."; F12 musing recast; "was going to argue"; "sorted out"; "the fight still in her face"; "made room for them at the table"; F16.
- **Gate-driven equivalents (book-wide repeat gates):** F3's "Lora and Viridia had none" → "The girls had none, and neither did Bal."; "still arguing about it at the door" → "Nobody had won yet when he went in."; "She was not having any of it. She was up" → "Amelia was up and pacing"; same-speaker paragraphs left by the cuts merged (Thad L72/76, Lora L198/202).
- **Kept:** "Damn their war. I will kill him."; "That's my Warrior Goddess."; all Strengths to PRESERVE.
- **Recount:** no gesture class at 3+ in 500w; em dashes 0; "the way" 0; simile 1.5/1K. 3,429 prose words (in range).
- **Gates (Ch.1–22):** style_check clean; grammar_check 0 errors; voice_wear_check clean (strict); tic_report --gate clean.
