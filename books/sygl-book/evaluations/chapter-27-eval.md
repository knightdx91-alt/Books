# Evaluation: Chapter 27 — Thunder from a Clear Sky
**Evaluator:** book-evaluator | **Date:** 2026-10-21

## HEADLINE
**CVI-Launch:** 8.5 (8.0 + 0.5 strong anchor) | **CVI-Legacy:** 6.5 | **Genesis Floor:** 7.5 | **Genesis Average:** 8.3
**Engagement Type:** Self-Insertion (primary) / Empathy (secondary) / Fascination (tertiary)
**Divergence Alert:** 1.0 (Launch over Floor), which is under 2.0. As in Ch.23, 25 and 26, a mechanical cap holds the floor: gesture clusters and two shared gestures. There is also one logic slip about the poison clock and one invented Mrs. Brown habit. The content is at 8.5. Every fix below is a cut or a word swap, and none adds plot. With F1–F16 applied, the chapter projects to **Floor 8.5 / Casual 8.5: PASS**.

## Gate tools (scratch copy of Ch.1–27 at `/tmp/claude-0/-home-user/925d8686-989e-5134-a9ef-2d597d7cac42/scratchpad/ev27/manuscript/chapters/`)
- `voice_wear_check.py`: **clean.** There are no retired phrases and no device over cap. Self-repetition is clean under the strict setting (two phrases are informational only).
- `tic_report.py --gate`: **clean.** Auto-recurrence found none. Ch.27 scored and-chains 3 (cap 9), negation pivots 0 and 'So' openers 0. Ch.27 is the worst chapter in "kneel/crouch" at 3x book-wide (L112, L258, L260, all source-driven) and in "a (long) moment" at 2x. Both are under cap.
- `style_check.py --dir manuscript`: **clean.** 4,227 words, simile 3.5/1K, adverb 6.6/1K, **em dashes 0**. The two "the way" hits (L66 "along the way", L182 "Some of the way") are not similes. There are no distinctive cross-chapter repeats.
- `grammar_check.py --file`: 0 errors.
- The gates do not see 500-word class clusters or shared gestures. The hand count below does.

## Source fidelity (L939–962, pp.162–170)
Every beat is present in source order. They walk the horses with no rush, and Viridia is herself again, laughing. Bal's question is prompted by the bookshop (L20 matches Ch.13 L218). "I bet all the boys were chasing after you" is kept. Her face darkens and then clears, and Bal fears a mistake. Bran is given in the source's order: two years old, the smirk, "he would have me eventually", the sygl that saved her, "Are sygls rare", the water bottle, "basically gave me a new life", her laugh, the father who refused, six months, "Bran was not happy". After that comes Bal's smile, and her hair popping again. The hot day and the rag. He checks the road and Lora asks. **"A bow pointed at my back"** and "probably me being paranoid" are both there. The orphanage jokes follow, and the feeling grows into the head on a swivel. The girls go quiet and trust him. The hour of the poison brings **the thunderclap from Londra under a clear sky**. The saddles creak. Then "Can you feel it now?", Lora's confusion, "I can't explain it", "Are we in danger?" / "can you tell from what?". A bolt falls between the horses and they are thrown. Viridia is the lightning rod with her arms up, there are too many bolts, and the stone knocks him out. **The capture is not shown** (L116 cuts straight to dark). He wakes hours later. His head throbs and he tastes copper from the bitten tongue. His voice is a croak. Blackened craters, burnt horse, calling. No tracks: "as if they had dropped off the edge of the world". Lora's bedroll comes off her dead horse and goes upwind. Troubled sleep. The sun in his face, the blow again, ranging out, "taken", and Pashar too far without a horse, so he turns south. Two days on foot. The evacuating village has black eyes, split lips, a broken arm and cursing villagers, and he would kill anyone who stopped him. **Jazen Grey**: "High Priest", "Take mine", noon tomorrow, the message for Fern. **Barda**, white, big head, "Ol' Barda", the wave. He rides all night, alternating gait. Before noon he crests the hill above the scouting party. **Thad and Xavier deflect bolts with blood whips.** He comes in behind, finds no sentries, and the platform puzzles him. **Dagger LEFT, whip RIGHT** (the rulings are met: each palm opens on its own and closes after). The eye only partly pierced, the kick. The young blond mage's **lightning whip**, "You're too late", ozone. **Razor-sharp and spiked.** Back and forth, the off-hand bolt, the whip across his chest, thrown off. Burnt skin, the body that won't work. **"I think I'll get a promotion after killing you"**, the blue-orange whip, **the silent apology**. The arrow, the crossbow bolt, the blood soldiers, dark.
- Source slip "Bal obeyed to the night" is rendered sensibly as "told his own whip what he wanted".
- Dialogue is the author's base, polished. The memorable lines are kept nearly verbatim. Additions such as Viridia's "Yeah, I can" (for the nod), Bal's "Yes" (for the nod), "I'll tell him" and "I owe you for this. Truly." (for "thanks") add no information.
- Register is American throughout ("gray", "go-round", "Ol'"). Tone is warm through the first quarter (the leaf, the jokes, "he hoped she did"). The battle is clear and brave, and only mildly graphic (see F15).

## Logic / continuity findings
- **F1 (Logic) L68 poison clock.** "would be getting tired about now, and finding it hard to breathe." Ch.24 L168 gives the mechanics: 24 hours dormant, then lethargy and hard breathing, then the heart stops about six hours later. With a noon lunch, six the next evening is **the end**, not the onset. Ch.26 L74 says "by around six tomorrow night, those priests would all be dead", and the source says "when it came time for the night stalker poison to finish its work". The line contradicts both.
- **F2 (Continuity) L8 "pulled a leaf out of her hair".** Ch.26 ends with the leaf in *Viridia's* hair. "Her" here reads as Lora's own.
- **F3 (Canon/invention) L182 "She would have made him take them off at the door."** This is a new Mrs. Brown habit. It appears nowhere in Ch.1–5 or the source, and the guardrail is "no invented habits". Wondering what she'd say about his boots is fine. Asserting a house rule is not.
- **F4 (Continuity, low) L18 "cried herself to sleep in Lora's arms".** In the source, and in Ch.26 L64→100, she stops crying, lies down, gives Bal a tired smile and then sleeps. Align the wording with Ch.26 as finalized.
- **F5 (Lore, low) L308 "He had not told it to."** This line asserts that the whip returns autonomously when he is stunned, which is a new behaviour. The ruling only says the palm closes when the blood returns. Cut the sentence and keep the return.
- **F6 (Tense) L74 "the kind that comes straight down … and rattles the dishes".** A present-tense generic sits in past narration (STYLE §4). It is also a Pattern #11 extension.
- Checked and clean: the direction (south from Londra, the boom from the north, sunrise on his left); Thad's evacuation remark (Ch.22 L24) and the scouting parties (Ch.22 L72); scarlet robes (Ch.11 L184); the canyon temple; "the black" as Bal's horse (Ch.25); Lora's alchemy chest (Ch.24); Saint Andre's; Pashar beyond Londra (Ch.22/23).

## Gesture hand count (500-word windows; w = approx. prose word position)
| Class | Instances (line, w) | 3+ in 500? | Fix |
|---|---|---|---|
| Smile/grin | L30 "smirk" (Bran, reported, w398), L44 "She grinned up at the sky" (w579), L48 "Bal smiled" (w592, source) | **YES (3 in ~200w)** | F7 |
| Turning | L52 "twist in the saddle" (w685), L58 "He faced front again" (w718), L72 "twisted in their seats" (w1019, source), L86 "Lora's head went from Viridia to Bal and back" (w1100), L90 "Lora turned to Bal" (w1132) | **YES (5 in ~450w)** | F8 |
| Looks/watching | L52 "study their back trail", L64 "His head kept going around", L66 "kept their eyes moving where his went", L76 "Bal searched the sky", L86 head beat, L90 "staring back toward Londra" (w680–1140) | **YES (6 in ~460w)** | F8 |
| Prop fiddling | L38 "dug out her water bottle" (w492), L40 "pushed the stopper home", L42 "stowed the bottle", L50 "dug a rag out … stuffed it away again damp" (w668) | **YES (5 in ~180w)** | F9 |
| Turning (2) | L146 "his face turned from the smell" (w1796), L148 "turned over, and turned back" (w1865) | YES (3 in ~70w) | F10 |
| Looks (2) | L200 "spun, and stared" (w2575), L202 "looked Bal over" (w2592), L206 "Whatever Jazen saw in his face" | YES (3 in ~70w) | F11 |
| Turning (3) | L270 "Both men spun around" (w3465), L276 "He turned to the other one" (w3563), L298 "twisted aside" (w3821) | YES (3 in ~360w) | F12 |
| Eyes | L320 "Bal's eyes closed" (w4076), L328 "opened one eye", L338 "His eyes fell shut" (w4226) | **YES (3 in 150w)** | F13 |
| Laughs | L6 (w10), L42 (w546), L58 (w744) | no (2 per window) | none |
| Sitting/kneeling/crouch | L112, L156, L258, L260 | no | none |
| Freezing/stopping | L184 "stopped… stopped" (walking), L194 (stop him), L310 (boots stopped) | not gestures | none |
| Chest/heart | alchemy chest, horse's chest, whip across chest | not gestures | none |
| Hand holds | L202, L272, L280 | no | none |
| Tilts / nods / blushes | 0 / 0 / 0 | n/a | none |

**Shared gestures (the "no two characters share a gesture" ruling):**
- **F14a L210 "He jerked his chin at the blood sygls"** (Jazen). This is Viridia's gesture in Ch.12 L22 ("she jerked her chin at Lora's table"), and Ch.7 L139 has a "tipped his chin".
- **F14b L182 "His mouth twitched at that"** (Bal). This is Amelia's in Ch.7 L265 and Soren's in Ch.13 L336, so it would be a third owner.

## Genesis Score

| Dimension | Score | Evidence | Cap Reasons |
|---|---|---|---|
| Originality | 8.5 | The clear-sky boom lands at the exact hour their poison finishes its work, so victory and catastrophe share one minute (L68–78). A lightning whip meets a blood whip in a mirror duel (L280–298). | none |
| Theme | 8.5 | Protecting his own: "He told Viridia not to give anybody any lip until he got there, which was a waste of breath, because she would anyway, and he hoped she did." (L182) The theme is felt through the loss and is never stated. There is plenty of texture: the trough, the boots, the coach line. | none |
| Characters | **7.5** | Viridia's voice is distinct ("That fool Bran… Bran was not happy."). The mage is chillingly friendly. Jazen gives without fuss. Bal has inhabited chaos (L180 "His feet went on without him"; L306 "His body had gone somewhere else and not told him where"). | **Capped at 7.5:** eight 3+/500 gesture clusters (table) plus two shared gestures (F14). Content sits at 8.5. |
| Prose & Voice | 8.5 | Underlines: "He could not search in the dark. He knew that. Stopping was harder." (L144); "in an easy, friendly sort of voice, as if they were waiting together for a coach" (L314); "the beat of the big hooves made more sense than anything else in the night" (L236). The ugly sentence: "He stood. It took two tries." Voice under pressure: L102–116 shatters into fragments ("Then there wasn't anything."). | Pattern #11 runs ~4 in 4.2K, about 0.9/1K, at the commercial edge. F6 and F16 bring it under. |
| Pacing | 8.5 | Disaster in medias res, a compressed lone trek and a propulsive battle. Speed varies (L100–116 against L180–184). The value shift goes from + (Viridia restored, jokes) to − (girls gone, Bal down). It ends on the dark with rescue arriving. | none |
| Emotion | 8.5 | The anchor, "a hot, high, faded blue, without one cloud in it anywhere to have made that sound" (L78), lands. The surprise is that humor survives grief: the boots and "he hoped she did". The body rebels in L306/L312. The apology is carried in actions and few words (L322). | none |
| Source Fidelity (Dim 7) | 8.0 | All beats are present, in order, with the rulings met (dagger left, whip right, palms self-opening, capture unseen). | F1 contradicts Ch.24/26 and the source. F3 is an invented habit. F5 is small new lore. |
| **FLOOR** | **7.5** | | |
| **AVERAGE** | **8.3** | | Single-dimension weakness: Characters (mechanical) |

## CVI-Launch Breakdown
| Input | Score | Evidence |
|---|---|---|
| Commercial Pacing | 8/10 | Three movements, each ending on a jolt: the stone, "They had been taken.", "the dark took him". |
| Tomorrow Test | 3 anchors → 9 | IMAGE: the boom under a cloudless sky. IMAGE: Viridia as a human lightning rod, arms up and hair spread. QUOTE: "I think I'll get a promotion after killing you." |
| Casual Reader | 8.5/10 | Warm open, shock, and a hero on his back. |
| Shareability (quote/plot/emotional) | 2/4/3 | max 8×0.6 + avg 6×0.4 = 7.2 |
| Concept Pitch | yes (10) | |
| Human Closeness | partial (5) | Half the chapter is alone, but it is about the girls. |
| **CVI-Launch** | **8.0 + 0.5 anchor = 8.5** | |

CVI-Legacy 6.5 (default weights: Orig 8.5, Theme 8.5, Vocab 3, Re-read 5, Identity 5).

## Anti-AI Scan (20 patterns, commercial thresholds; ~4.2K words)
1 Forced symmetry: clear. 2 Empty poetic vocab: clear. 3 Rule of three: 1, minor ("He saw… He saw… He saw", L114, which earns its place in action). 4 Em dashes: 0. 5 Empty metaphors: 1, minor ("long as a barn", L250). 6 "And" openers: clear. 7 Pseudo-philosophical closings: clear. 8 Parallelism: minor (L294 "Blood on lightning, lightning on blood"). 9 Smooth transitions: clear. 10 Described emotion: minor (L194 "a cold, steady calm"). **11 Explanatory extension: ~4, about 0.9/1K, moderate** (L74 dishes, L160 "by somebody he hadn't seen coming", L236 "as if he knew the road better than his rider did", L288 "sharp, the smell after a storm"). **12 Binary negation: 1** (L218 "Not gray, not dappled. White as new snow"). 13 Precision flex: clear. 14 Emotional control: clear (L160 he waits; he does not manage it). 15 Authoritative description: clear (L262 "he couldn't guess" leaves a gap). 16 Philosophical asides: clear. 17 Clean dialogue: minor (Jazen exchange, source-shaped). 18 Echo chamber: clear. 19 Graduated reveal: clear (disaster-first structure). 20 Temperature report: clear.
**Total: 8/20 present, mostly minor. That is CLEAN for commercial fiction.**

## Character Chaos Check (Bal)
- Irrelevant thought: present (Mrs. Brown and his boots, L182; dozing in the saddle, L236).
- Cognitive distortion: present ("he would kill them", L194; "days and days", L170).
- Unprompted memory: present and triggered (the boots, the creek bed), and it returns to the scene.
- Failed emotional management: present (L160; L312 "He had to move. He had to.").
- Voice under pressure: demonstrated.

## Secondary characters
- Viridia: her own moment (Bran, "That fool", the lightning-rod stand).
- Lora: thin by source design ("Feel what?", the groan at the joke). No flag.
- Jazen: his own moment (gives his horse; the fond pat is his gesture alone). Barda carries the ride.

## The Tomorrow Test
**What the reader remembers:** one boom out of a clear blue sky at six o'clock, and Viridia standing in the bolts with her arms up.
**Anchor type:** BOTH (plus the promotion quote). **ANCHOR EXISTS.** It differs in type from the Ch.25 anchor (the rune under the cup) and the Ch.26 anchor (the hand on the cheek).
**Shareable:** "They poison the priests and the sky answers at the exact hour."

## Reader Reports
- **Devourer:** No stopping point. The trek (L178–184) is short enough. Pulled through by "They had been taken." and the duel.
- **Critic:** Underlines L144, L182 ("he hoped she did") and L314. Disappointed by "white as new snow", "long as a barn" and "edge of the world".
- **Hostile:** Catches the poison clock (F1). Wonders why the whip comes home by itself (F5). Notices the glut of turning and looking in L52–90.
- **Casual:** Loves the leaf, the jokes and Barda. The ambush is a real shock. Would keep reading: 8.5.

## Cross-Reader Matrix
| Issue | Devourer | Critic | Hostile | Casual | Severity |
|---|---|---|---|---|---|
| Look/turn glut L52–90 | – | ✓ | ✓ | – | SHOULD FIX (also a mechanical cap) |
| Poison clock F1 | – | – | ✓ | – | INVESTIGATE (Logic, fix first) |
| Clichés / extensions | – | ✓ | – | – | INVESTIGATE |
| Shared gestures F14 | – | ✓ | ✓ | – | SHOULD FIX (author law) |

## Revision Recommendations (surgical; no plot added)
| # | Location | Type | Now | Fix |
|---|---|---|---|---|
| F1 | L68 | Logic | "would be getting tired about now, and finding it hard to breathe." | → "would be dying about now, if Lora's book was right." |
| F2 | L8 | Continuity | "pulled a leaf out of her hair" | → "pulled a leaf out of Viridia's hair" |
| F3 | L182 | Canon | "She would have made him take them off at the door." | Cut the sentence. |
| F4 | L18 | Continuity | "Last night she had cried herself to sleep in Lora's arms." | → "Last night she had cried in Lora's arms until there was nothing left, and slept." (or match Ch.26 final) |
| F5 | L308 | Lore | "…and the palm closed over it. He had not told it to." | Cut "He had not told it to." |
| F6 | L74 | Style/tense | "the kind that comes straight down on top of a house in a summer storm and rattles the dishes." | → "the kind that came straight down on a house in a summer storm." |
| F7 | L44 | Gesture (smile) | "She grinned up at the sky, enjoying it." | → "She told it to the sky, enjoying it." |
| F8 | L52–90 | Gesture (turn/look) | L52 "He would twist in the saddle and study their back trail. It was always empty."; L58 "He faced front again, with an effort."; L66 "and kept their eyes moving where his went,"; L76 "Bal searched the sky." + L78 "It was clear…"; L86 "Lora's head went from Viridia to Bal and back. \"Feel what?\""; L90 "Lora turned to Bal. He was still staring back toward Londra, and he could not make himself stop." | L52 → "The road behind them was always empty."; L58 cut the sentence; L66 cut the clause; L76+78 → "Overhead the sky was clear from one edge to the other, …"; L86 → "\"Feel what?\" Lora said."; L90 → "Bal's attention was still back toward Londra, and he could not pull it loose." then "\"Are we in danger?\" Lora asked him." |
| F9 | L38–50 | Gesture (props) | dug out / pushed the stopper home / stowed / dug a rag … stuffed it away again damp | L38 → "Viridia took a long drink from her water bottle before she answered, and the sun winked off the neck of it."; L40 cut "She pushed the stopper home."; L42 cut "She stowed the bottle."; L50 → "…running into his eyes, and he mopped his forehead with a rag from his pocket." |
| F10 | L146 | Gesture (turn) | "with his face turned from the smell" | → "breathing through his mouth" |
| F11 | L200 | Gesture (look) | "Jazen heard boots behind him, spun, and stared." | → "Jazen heard boots behind him and spun." |
| F12 | L276 | Gesture (turn) | "He turned to the other one." | → "That left the other one." |
| F13 | L338 | Gesture (eyes) | "His eyes fell shut, and the dark took him." | → "Then the dark took him." |
| F14a | L210 | Shared gesture | "He jerked his chin at the blood sygls and their cart." | → "Over by the blood sygls and their cart, another soldier was leading horses up." (merge with the next sentence) |
| F14b | L182 | Shared gesture | "His mouth twitched at that, and then it didn't." | → "It nearly made him smile, and then it didn't." |
| F15 | L272 | Tone (not gory) | "He landed somewhere below with a thud and went on screaming." | → "He landed somewhere below with a thud." |
| F16 | L218, L250 | Style (#12, #5) | "Not gray, not dappled. White as new snow, and in the late sun his coat shone."; "long as a barn" | → "He was white all over, and in the late sun his coat shone."; cut "long as a barn," |

Fix order: F1, F3, F5 (logic/canon) → F2, F4 → F7–F14 (gestures) → F6, F15, F16.

## Spell repetition watch — the blood whip (Ch.20, 21, 27): author asked to be told
**Verdict: the function does not read as repetitive, but the ritual is starting to.** Each use does something different, and all come from the source. Ch.20 shows discipline (strike, wrist-wrap, throw). Ch.21 is an interrogation (around the neck, lift). Ch.27 is a duel: the whip is shaped (edged, spiked) against a lightning twin, Thad and Xavier use theirs as shields, and **Bal loses**. That is fresh. What repeats is the **palm opening on its own and closing after**. It is described on page in Ch.20 (L38/L72) and Ch.21 (L108/L136), and **three times in Ch.27** (L266 both palms, L274 dagger closes, L308 whip closes). Recommendation: from here on, show the open/close once per chapter at most, and let it be implied otherwise (F5 already trims L308). Looking ahead, Ch.29's duel should lean on what the source gives it (the vials, the abilities from the chalice, Kona Niente/Czak) rather than the whip again, or the reader will feel it. Ledger count after Ch.27: whip on page in 3 chapters, dagger in 2.

## Strengths to PRESERVE
The leaf-and-laugh opening. "he hoped she did". L144's three short sentences. The friendly coach-voice of the mage. The anchor sky line (L78). Barda dozing south under him (L236). The fragmented blackout (L114–116). The capture never shown.

## PATH TO 8.5
- **Characters 7.5 → 8.5:** apply F7–F14 exactly. The content already earns 8.5: Viridia's distinct voice, inhabited chaos in L180/L306, Jazen's own moment. The cap is purely mechanical.
- **Source Fidelity 8.0 → 8.5:** F1 (the poison clock matches Ch.24 L168 and Ch.26 L74), F3 (cut the invented habit), F5 (cut the autonomy line).

## VERDICT
**POLISH.** Floor 7.5, Average 8.3, Casual 8.5. Projected **PASS (8.5/8.5)** once F1–F16 are applied.

BIAS CHECK: This evaluation was produced by the same system that wrote the prose. Confidence in scores above 8.0 requires external validation (beta readers, editors, comp analysis).

## Revision applied (2026-10-21, book-editor r1)
- **F1–F16 applied as quoted**: poison clock ("would be dying about now, if Lora's book was right"); leaf in Viridia's hair; Mrs. Brown boots-rule sentence cut; tense slip fixed ("came straight down on a house"); grin → "told it to the sky"; L52–90 turn/look glut trimmed; water-bottle/rag prop cluster trimmed; "breathing through his mouth"; Jazen "spun" only; "That left the other one."; chin jerk (Viridia's) removed from Jazen; mouth twitch → "It nearly made him smile"; "went on screaming", "Not gray, not dappled. White as new snow" and "long as a barn" cut; "He had not told it to." cut.
- **Gate-driven variants of quoted wording** (book-wide repeat gate): F4 → "cried herself out in Lora's arms, and then she had slept" ("there was nothing" 3x); F8 L52 → "Behind them the road was always empty." ("the road behind" 3x); F8 L86 → `Lora said, "Feel what?"` (cross-quote "I can feel" 3x).
- **Palm open/close narrated once**: the full description stays at the call (left dagger, right whip, palms opening on their own). The dagger's return is now "Bal released the dagger."; the whip "came crawling back to him over the dirt, and slid home." Closing is implied, not narrated.
- **Hinge openers** 5 → 3 ("Then she laughed" → "She laughed"; "Then the dark took him" → "The dark took him").
- Dagger LEFT and whip RIGHT with spikes are kept. The capture is still unseen and the ending stays in the dark. No plot, characters or habits were added.
- **Gates (Ch.1–27):** style_check clean (em dashes 0; "the way" hits are not similes); grammar 0 errors; voice_wear_check clean (strict); tic_report --gate clean; gestscan has no 3+/500 clusters. A hand recount of turning, looks, eyes, smiles and props shows at most 2 in any 500-word window.
