# Evaluation: Chapter 20 — The Blood Whip
**Evaluator:** book-evaluator | **Date:** 2026-10-20
**Text evaluated:** `manuscript/chapter-20.md` (2,711 words of prose; target 2,600, range 2,300–3,000, so on spec).
**Read first:** STATE.yaml (decisions: blood whip from the RIGHT palm; spell-repetition watch; dialogue rule; no shared gestures), book CLAUDE.md, project/STYLE_CONSTRAINTS.md, project/foundation.md (Magic ledger), character-bible.md (Sean Kiin, Porter), outline Ch.20, manuscript/chapter-19.md (mid-revision), chapter-07.md (hall layout), chapter-09.md (Porter), chapter-18.md (the lake), Sygl_Complete.txt L798–813, evaluations/chapter-19-eval.md.

## HEADLINE
**CVI-Launch:** 8.7 (8.2 + 0.5 strong anchor) | **CVI-Legacy:** 6.2 | **Genesis Floor:** 7.5 | **Genesis Average:** 8.3
**Engagement Type:** Self-Insertion (primary) / Empathy (secondary) / Fascination (tertiary)
**Divergence Alert:** 1.2 (Launch over Floor). Under 2.0. As in Ch.19, a mechanical gesture cap holds the floor down. The content does not.

**VERDICT: POLISH (FAIL at the 8.5 gate).** What the chapter gets right:
- Every source beat from L798–813 is present and in source order.
- The whip comes from the RIGHT palm.
- Bal's stand is protective and justified.
- The anger surprise is noted once ("Maybe he'd talk to Amelia about it later.") and dropped.
- The speech is earnest, not grandiose ("He had not meant to go on").
- No spell is invented.
- "my girls" appears once (source) and "his girls" once (source), so it is not a refrain yet.

The floor is **Characters 7.5**. The hand count found five gesture classes at 3+ inside 500 words. It also found two other problems:
- Porter's spent colour-rising beat is reused.
- Viridia's hand in Hopper's fur recurs from Ch.19.

**Prose sits at 8.0** because of a quote-format bug, one logic slip and register slips. Every fix below is a cut or a word swap and adds no plot. With F1–F18 applied, the chapter projects to **Floor 8.5 / Casual 8.5: PASS.**

## Gate tools (scratch copy, Ch.1–20 at `/tmp/claude-0/-home-user/925d8686-989e-5134-a9ef-2d597d7cac42/scratchpad/ev20/manuscript/chapters/`)
- `voice_wear_check.py`: **clean.** Two cross-chapter self-repetitions are WARN only.
- `tic_report.py --gate`: **clean.** Ch.20 has 1 and-chain, 0 negation pivots and 0 auto-recurrence, and adds nothing to the book-wide gesture table.
- `style_check.py --dir manuscript`: **clean.** No new repeated phrase.
- `grammar_check.py --file chapter-20.md`: 0 errors. It **missed** the L204 double-quote bug (F1).
- Em dashes: 0. "the way" similes: 0.
- Filter words: "began to" (L22) and "just" (L38), 1 each.

The tools do not classify posture, looking, props, laughs or head/chin, so the hand count below is the binding check.

## FULL gesture hand count (w = word position in the prose; 500-word windows)
| Class | Instances | 3+ in 500w? | Verdict |
|---|---|---|---|
| Smile/grin | "grin like an idiot" w97; Porter "smiling… nasty smile" w690/696 (one beat, source); Amelia "smiling again, the real one" w2708 | no | OK |
| Laughs | Bal w1572 (source); Lora "laughed harder" w1886 (invented); Amelia "laugh out loud" w2058 (source); Bal w2590 (source) | **YES**: w1572–2058, 3 in 486 | F8 |
| Blush/colour | Sean blotchy w606; Porter "color had climbed his neck" w975; Lora "pink to the ears" w1240 | no (634 span) | Porter's colour-rising is **spent** per the bible (Ch.9). F4 |
| Looks/eyes | held Sean's eyes w931; glanced w1181; looked out w1606; eyes held w1727; eyes shut w2386; looked to Amelia w2462; held her gaze w2484; stared up w2503; traded glances w2660 | **YES**: w2386–2660, 5 in 274 | F6. The eye-hold is also doubled (L64 + L120): F9 |
| Sitting/posture | slid into seat w319; stood/rose w1126/1131; dropped onto bench w1821; sat on arm w2022; settled w2110; stretched legs ~w2150; propped on one fist w2235; head drop w2492; slid down w2527 | **YES**: w2022–2492, 5 in 470 | F7 |
| Freezing/stopping | spoon stopped w232; arm held still w1239; forks halted w1330 | no | OK |
| Chest/heart/throat | collar to throat w45 (clothing); chest (whip strike) w516; "Sean's throat moved" w1791 | no | OK |
| Hand holds/fists | arm in fist w405; hands folded w779; napkin in fist w1400; boy's fist over palm w1561; propped on fist w2238; fingers in Hopper's fur w2366; arm over shoulders w2594 | borderline (w2238–2594, 3 in 356) | F7 cuts "propped on one fist". Fur recurs from Ch.19 L44/L58: F10 |
| Head tilt/nod/chin | Sean lifts chin w1721; jerk of chin w1800; "Bal tipped his head" w1829 | **YES**: 3 in 108 | F3 |
| Nods / shrugs | 0 / 0 | — | The source's nods and shrug are rendered without the words. Good. |
| Prop fiddling | Viridia: slip + "pencil already" w319–332; "kept her pencil going" w352; pencil skidded w415; "pencil still in her other hand" w557; fresh slip smoothed w789 (Porter's napkin w678/1400 separate) | **YES**: Viridia 5 in 470 | F5. Ch.19 also opened on pencil business. |

## Genesis Score (Craft Assessment)

| Dimension | Score | Evidence | Cap Reasons |
|-----------|-------|----------|-------------|
| Originality | 8.5 | The whip's first appearance is staged as three different actions (strike L38, wrap-and-haul L58–60, fling L70). Viridia keeps writing her breakfast order through the confrontation (L22–24, L54). Viridia's five-times mime with sound effects (L134). For commercial fantasy this is fresh execution on a familiar school-showdown beat. | — |
| Theme | 8.5 | "If anyone else is tired of feeling like they don't belong… the Blood sygl will welcome you with open arms" (L114). It grows organically out of "first years who had been told what Bal was before he had ever said a word to them" (L112). Texture that is not thematic: milk in Lora's lap, jam on Sean's sleeve, "before lunch". | — |
| Characters | **7.5** | Strong. Sean's echo-questions ("Not my concern? Not my *concern*?") match his card. Porter's "nasty smile" and the crushed napkin. Lora "pink to the ears, and her arm did not waver" (L84) against Viridia's showy half-circle. Amelia's plan collapsing: "Oh. Um." | **CAP 7.5:** five gesture classes at 3+/500w (see the table). Porter's spent colour beat reused (L66). Viridia's Hopper-fur gesture recurs from Ch.19. |
| Prose & Voice | 8.0 | Underlines: "It welled out of the middle of the palm without a cut, as though it had been waiting just under the skin, and it did not fall." (L38). "He gave one short jerk of his chin that might have meant yes and might only have meant please stop talking to me, and then he went and dropped onto his bench in the tea." (L128). "there was a clear lane through the center of the wood where the food had been" (L70). "Bal laughed. It got out of him on its own." (L108). Voice under pressure: L34 "Nothing in him stopped to decide." | Held at 8.0 by: the L204 quote bug; the L138 logic slip; "poured"/"did not fall" (L36/38); "swung round" (British); porridge vs oatmeal; the L14 clunk; L166 restating L164. |
| Pacing | 8.5 | A fast confrontation (short paragraphs at L52–58), a decelerating speech, a brisk walk, then the debrief. Value shift: covert to declared, and the girls learn they are now war targets ("Talk about no pressure"). Hook: the lake. The debrief runs about 1,000 words, but every beat in it is source. | — |
| Emotion | 8.5 | Anchor: Sean sliding down his own table into the tea (L70). Emotional surprise: comedy inside a violent showdown (the breakfast order, the jam). Body rebel: "Bal laughed. It got out of him on its own." The anger surprise is noted once and not turned into dread (L138–142). | — |
| Engagement (Dim 7) | 8.5 | Self-insertion: the outcast publicly upends the bully and the teacher who sneered at him. Empathy: Lora's steady palm. Fascination: the war rules turn the girls into the stakes. | — |
| **FLOOR** | **7.5** | | Characters |
| **AVERAGE** | **8.3** | | |

## CVI-Launch Breakdown
| Input | Score | Evidence |
|-------|-------|----------|
| Commercial Pacing | 8.5/10 | Public showdown in the first 1,200 words; the hook into the lake. |
| Tomorrow Test | 3 anchors (2 image, 1 quote) → 9 | Sean in the tea with jam on his sleeve; Viridia writing her order mid-grab; "If you bother either one of my girls again, I'll call you out, and I will kill you." |
| Casual Reader | 8.5/10 | A wish-fulfilment payoff delivered cleanly. |
| Shareability (quote/plot/emotional) | 3/4/3 → 7.5 | — |
| Concept Pitch | yes (10) | — |
| Human Closeness | partial (5) | — |

CVI-Launch = 8.2, +0.5 for the anchor = **8.7**.
CVI-Legacy (default weights): Originality 8.5, Theme 8.5, Vocabulary 2, Re-read 4, Identity 5 = **6.2**.

## Anti-AI Scan (20 patterns; commercial thresholds)
- #1 Forced symmetry: clear.
- #2 Empty poetic vocabulary: clear.
- #3 Rule of three: minor (1). "Toast went. A plate of sausages went. Somebody's teacup went…" (L70). Earned comic rhythm.
- #4 Em dashes: 0.
- #5 Empty metaphors: clear.
- #6 Dramatic "And": clear.
- #7 Pseudo-philosophical closing: clear.
- #8 Parallelism: clear.
- #9 Smooth transitions: minor. "After that the talk went to the war." (L168)
- #10 Described emotion: minor. "plainly impressed", "admired her", "surprised him". All three are source.
- #11 Explanatory extension: 2 instances (0.74/1k), under the cap.
  - L14: "because the doors had opened late and no one was left to come through them but Bal"
  - L166: restates L164.
- #12 Binary negation: 1. "Not hurt him. Kill him." (L138). This renders the source's "Literally." Acceptable.
- #13 Precision flex: clear.
- #14 Emotional control: minor. "Bal kept his voice level." Then the anger, which he does not control.
- #15 Authoritative description: clear.
- #16 Philosophical asides: clear.
- #17 Clean dialogue: minor. The source is turn-based. Overlap is summarised at L160.
- #18 Echo chamber: clear.
- #19 Graduated reveal: clear.
- #20 Temperature report: clear.

**Total: about 6 minor patterns. Clean for the genre.** No over-correction flag.

## Source fidelity (L798–813)
All beats are present and in order:
- uniforms; the doors; the elbowing girl; "What's the meaning of what, Sean?"; Porter's question
- the grab; the whip from the right palm; "She's not your concern anymore"; "filthy blood mage"
- the rule ("nasty smile"); the wrist; the plates; Porter's "Release him"; the throw
- "their Lead Mage now. Not that fool."; the palms; "punish Sean"; the full speech; the declaration; the paled Tempus students; Bal's laugh
- the open-arms offer; the duel warning; "rubbing off on him. Oh well."; the anger and the dart; "talk to Amelia about it later"
- Xavier tonight; Amelia's high spirits; "find all of my priests"; two more priests tonight; the break; the whip told; days of practice; teaching the girls
- the village; Londra; the war rules; "Talk about no pressure"; no plan; the swim; "I can do that"

Invented items are texture only: the milk in Lora's lap, Viridia's mime, the jam, the boy's fist. None adds plot, motive or backstory.

**"Bal suspected he had been saving it since last night"** is legitimate. Ch.19 L30 has Amelia telling them Porter suggested the rule.

**The dart of blood in the eye: KEEP.** It is the source's own hypothetical ("It would not have taken much to send a blood dart into his eye"). It stays a single line of thought: never cast, not developed, and followed at once by the surprise and "Maybe he'd talk to Amelia about it later." That is exactly the outline's "noted once" instruction, and it reads as protective, not as relish or self-dread. One defect: "before Sean got a proper grip" contradicts L32, where Sean already has Viridia's arm in his fist (F2).

**Ledger note:** add "blood dart (hypothetical, Ch.20 thought only; not cast)" so no later chapter treats it as an established spell.

## Blood whip — how it reads (first appearance; for the author's spell-repetition watch)
- **In-chapter:** it reads well, not repetitively.
  - It gets one full description (L38: thickness, light, it "did not fall").
  - Each later use is a different verb: strike (L38), wrap-and-haul (L58), fling (L70).
  - It "came home to Bal's palm" once (L72). The debrief mentions it only as told.
  - That is three uses and one recap, matching the source exactly.
- **Inferred mechanics to confirm:** "without a cut" (L38) and "the skin there was smooth and dry again" (L72) are inferences. The source says only "sprung from the palm of his right hand". The author may want to confirm, since conversion (Ch.19) needs a cut.
- **Across chapters:** the whip carries Ch.20 and then Ch.21 back to back (Iro lifted by the neck). After that the source's only variety is the dagger (Ch.27) and the climax vials and army.
- **FLAG TO AUTHOR:** the whip will be the action spell in two consecutive chapters. Ch.21 should use a different verb set (grab, lift, close) and should not re-describe it. This is not a problem yet.
- **Update the Magic ledger row:** Blood whip → Ch.20 (3 uses).

## Character Chaos Check (Bal)
- Irrelevant thought: present. "So that was the jerk. Bal had wondered." (L26)
- Cognitive distortion: present, mildly. The kill impulse at L138.
- Unprompted memory: absent. That is fine.
- Failed emotional management: present. The laugh at L108 and the anger at L140.
- Voice under pressure: demonstrated. L34–36 goes terse.

## Secondary Character Chaos
- **Sean:** has his own moment (the chin jerk; he sits back down in the tea).
- **Porter:** has his own moment (the napkin crushed into a ball).
- **Lora:** has her own moment (milk in her lap, she "did not even flinch"; "Talk about no pressure").
- **Viridia:** has her own moment (writing the order; the half-circle).
- **Amelia:** has her own moment (her plan collapses: "Oh. Um.").

## The Tomorrow Test
**What the reader remembers:** Sean sliding the length of the Tempus table and ending in a puddle of tea with jam on one sleeve. Then: "I'll call you out, and I will kill you."
**Anchor type:** BOTH.
**Verdict:** ANCHOR EXISTS. The anchor matches the outline.

**Shareability:** "He pulled the bully across the breakfast table with a whip of blood, then made a recruitment speech."

## Reader Reports
- **Devourer:** reads straight through. The debrief at L154–190 slows things, but "the war hinges on us staying alive" re-hooks, and the lake pulls forward.
- **Critic:** underlines L38 and L128. Trips over L204's broken quote, the clunky L14 explanation, "swung round", and the double eye-hold.
- **Hostile:**
  - "proper grip" contradicts L32.
  - L70: Bal flings his arm behind himself, yet Sean "sailed backward".
  - L94: "Terra tables… Waves tables", but there is one table per sygl (Ch.7 L171).
  - L154: "couches", but Ch.7/19 have one couch and a chair.
  - L148: "He tried to act…", but Raizen has not been named.
  - Ch.7 L263 has a *Waves* boy at the next table over, while the source and Ch.20 put the Tempus table beside Blood. That is a Ch.7 continuity item, not a Ch.20 fix.
- **Casual:** buys it. It is a satisfying payoff, and the girls are likeable. Feels the debrief's run of sitting and looking around the couch only as a slight sag.

## Cross-Reader Matrix
| Issue | Devourer | Critic | Hostile | Casual | Severity |
|---|---|---|---|---|---|
| Gesture clusters (posture/looks in the debrief; props; chin) | x | x | | x | IMPORTANT |
| L204 quote bug | | x | x | | SHOULD FIX |
| Logic slips (grip, "backward", tables, couches, "He") | | | x | | INVESTIGATE (fix; cheap) |
| Register (round, porridge/oatmeal, jug) | | x | x | | SHOULD FIX |

## Revision Recommendations (surgical; quoted; no plot added)
| # | Location | Type | Now | Fix |
|---|---|---|---|---|
| F1 | L204 | Style | `"Oh," she said. "Um." "I thought you might have an idea or something."` | `"Oh," she said. "Um. I thought you might have an idea or something."` |
| F2 | L138 | Logic | "before Sean got a proper grip." | "before Sean had her out of the chair." |
| F3 | L130 | Character (chin/head 3 in 108w) | "Bal tipped his head toward the doors. The girls fell in beside him." | "Bal started for the doors, and the girls fell in beside him." |
| F4 | L66 | Character (Porter's spent colour beat, Ch.9) | "Porter wasn't enjoying himself anymore. The color had climbed his neck above his collar." | Cut the second sentence. |
| F5 | L22, L24, L40 | Character (Viridia prop cluster) | "She had a pencil already." / "and kept her pencil going." / "The pencil was still in her other hand." | Cut sentence 1; "and kept her pencil going" → "still writing"; cut sentence 3. |
| F6 | L188, L190, L214 | Character (looks 5 in 274w) | "Amelia only held her gaze and let that be the answer." / "and stared up at the ceiling beams" / "They traded glances around the couch, and nobody had a better idea." | "Amelia let the silence answer her." / cut the clause / "Nobody had a better idea." |
| F7 | L154, L156, L162 | Character (posture 5 in 470w) | "When they were settled she asked" / "He stretched his legs out." / "propped on one fist," | "and asked" / cut / cut |
| F8 | L134 | Character (laughs 3 in 486w) | "and each time Lora laughed harder while she tried to wring the milk from her skirt." | "while Lora tried to wring the milk from her skirt and kept having to stop." |
| F9 | L64 | Character (eye-hold doubled with L120) | "He held Sean's eyes while he said it." | Cut. L120 carries the source's "can't look away". |
| F10 | L172 | Character (recurs from Ch.19 L44/L58) | "Her fingers had gone deep into Hopper's fur." | Cut. Keep "Viridia did not answer that." (Or remove one of Ch.19's instances.) |
| F11 | L14 | Style (#11) | ", because the doors had opened late and no one was left to come through them but Bal" | Cut the clause. |
| F12 | L36 | Logic | "and the blood poured from it." | "and the blood came out of it." (L38 says it "did not fall".) |
| F13 | L70 | Logic | "He sailed backward over the aisle" | "He sailed across the aisle" |
| F14 | L94 | Continuity (Ch.7: one table per sygl) | "the Terra tables and the Waves tables" | "the Terra table and the Waves table" |
| F15 | L100, L16/L60 | Style (American register) | "swung round"; "porridge" vs "oatmeal"; "A jug of milk" | "swung around"; "oatmeal" both times; "A pitcher of milk" |
| F16 | L148 | Logic (pronoun with no antecedent) | "He tried to act as though he hadn't seen it coming." | "Raizen tried to act as though he hadn't seen it coming." |
| F17 | L154 | Continuity | "waved them all to the couches" | "waved them all to the couch" |
| F18 | L166 | Style (restates L164) | "and he had been at it less than a week." | Cut the clause. |

Fix order: F2, F12, F13, F16 (logic) → F3–F10 (character) → F14, F17 (continuity) → F1, F11, F15, F18 (prose).

## Strengths to PRESERVE
- The whip description at L38.
- Viridia's breakfast order (L22–24, L54), in its trimmed form.
- The milk in Lora's lap, "and she did not even flinch".
- "might only have meant please stop talking to me".
- "Bal laughed. It got out of him on its own."
- The speech's opening, "He had not meant to go on".
- The anger paragraph exactly as long as it is.
- Amelia's "Oh. Um." collapse.

## PATH TO 8.5
- **Characters 7.5 → 8.5:** apply F3–F10. Each 3+/500w cluster drops to 2 or fewer, and no spent or shared gesture remains. Re-run the hand count on the debrief (L146–220) after the edit. The posture and look classes live there.
- **Prose 8.0 → 8.5:** apply F1, F2, F11–F18. The underline sentences already exist (L38, L128). The blockers are mechanical.

## VERDICT
**POLISH**: Floor 7.5, Average 8.3, Casual 8.5. Projected **PASS (8.5/8.5)** with F1–F18.

BIAS CHECK: This evaluation was produced by the same system that wrote the prose. Confidence in scores above 8.0 requires external validation (beta readers, editors, comp analysis).

## Revision applied (2026-10-20, book-editor)
- **F1–F18 applied as quoted**, with three gate-driven substitutions:
  - F12: "came out of" tripped the book-wide 3+ phrase gate (ch 5, 8). "rose from" echoed Ch.19 L160 ("It rose from his palm"). Final: "and the blood leapt from it."
  - F14: "the Terra table" tripped the 3+ phrase gate (ch 7, 12). Final: "the Terra and Waves tables" (one table each; continuity intact).
  - F7 follow-up: the debrief still had 3 posture beats in about 460 words (sat on the arm / head drop / slid down off the arm). "Lora let her head drop onto the couch cushions behind her." became "Lora was quiet for a second."
- Kept: the dart of blood in the eye; the RIGHT palm; strike / wrap / fling; the anger noted once; the ending on "I can do that."
- **Hand recount:** no class reaches 3+ in 500 words. Laughs at w1513/1999/2488. Real looks at 3 in 544. Posture at 2 per window.
- **Counts:** em dashes 0; "the way" 0; similes 2 (0.8/1k). Prose is 2,603 words.
- **Gates:** `style_check.py --dir manuscript` is clean. `grammar_check.py --dir manuscript` is clean. On the scratch copy of Ch.1–20, `voice_wear_check.py` and `tic_report.py --gate` are both clean.
- Still for the author: the ledger row (blood dart is a hypothetical; blood whip Ch.20, 3 uses), and the Ch.21 whip-verb flag.
