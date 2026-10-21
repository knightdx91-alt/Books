# Evaluation: Chapter 29 — Blood Elemental
**Evaluator:** book-evaluator | **Date:** 2026-10-21

## HEADLINE
**CVI-Launch:** 9.0 | **CVI-Legacy:** 6.3 | **Genesis Floor:** 7.5 | **Genesis Average:** 8.2
**Engagement Type:** Self-Insertion/wish-fulfilment (primary), Empathy (secondary), Fascination with the magic (tertiary)
**Divergence Alert:** 1.5 (Launch over Floor), under 2.0. The pattern is the same as Ch.23 and Ch.25–28: the content is at 8.5, but a hand count of gesture classes caps Characters at 7.5. Most of the clusters are the source's own "looks" rendered as a different synonym each time. There is also one logic slip (L38), one contradiction of the source (L198, "no flash"), and one continuity slip (L58, the dress at her knees). Every fix below is a cut or a word swap and adds no plot. With F1–F24 applied, the chapter projects to **Floor 8.5 / Casual 8.5: PASS**.

## Mechanical gates (scratch copy, Ch.1–29, `manuscript/chapters/`)
- `voice_wear_check.py`: **clean**. No retired phrases, no device over its cap; 3 cross-chapter self-repetition WARNs, none strict.
- `tic_report.py --gate`: **clean**. Ch.29 is the book's worst chapter for the breath-beat class (2 by the gate's patterns). The hand count below finds 4 breath beats within about 495 words, which the gate's patterns miss.
- `style_check.py --dir`: clean. Simile 2.1/1k, em dashes 0, no new distinctive repeated phrase. `grammar_check.py`: 0 errors. No "the way" similes.
- Length: 3,759 words of prose. The target is 4,000 (range 3,600–4,400), so it is in range.

## Hand gesture count (fail = 3+ of one class within 500 words)
Word positions are measured from the chapter's first prose line.

| Class | Instances (line) | Span | Result |
|---|---|---|---|
| Looks | "searched the girls over" (L22); "smiled at whatever he saw in Bal's face" (L30); "met his gaze and held it" (L44) | ~260w | **FAIL (3)** (source: looks, seeing, eye) |
| Looks | "could not do anything but stare" (L106); "Bal stared up into it" (L134); "He found the circle" (L136) | ~310w | **FAIL (3)** |
| Looks | "checked behind himself" (L192); "studied Toma's huddled shape" (L204); "raising his head to find Amelia" (L216); "considered Bal" (L218); "found the circle again" (L230); "brought his gaze back" (L232); "sought Amelia's agreement" (L238) | 7 in ~650w (5 within L216–L238, ~375w) | **FAIL (7)**. The source's "looks at / looks to / looking back" are kept beat for beat under different words. This is the gesture-tic pattern the 2026-10-18 ruling targets |
| Looks/eyes | "held each other's eyes" (L272); "His gaze came around to Bal" (L282); "studying it" (L306) | ~275w | **FAIL (3)** |
| Eyes/brows | "frowned at him from under white brows" (L258); "held each other's eyes" (L272); "Bal's brows rose in a question" (L312) | ~470w | **FAIL (3)** |
| Posture (stand) | "tried to stand… he stood, swaying" (L182); "Bal stood above him" (L192); "Aren stood with his long white beard" (L204); "staying upright" (L222) | 3 within ~220w | **FAIL (4)** |
| Turning | "he turned to Bal" (L226); "Aren sighed and faced him" (L242); "turned to Amelia" (L260) | ~350w | **FAIL (3)** (the source has 2 of these) |
| Breath | "Aren breathed out through his beard" (L238); "Aren sighed" (L242, source); "until Bal forgot to breathe" (L272); "breathed her in" (L294) | ~495w | **FAIL (4)** |
| Hands | "Toma held up a hand" (L18); "both fists up" and "both palms pressed" (L22) | ~90w | **FAIL (3)** |
| Hands | "Lora had both hands pressed together" (L66); "ran his fingers down the bandolier" (L68); "his fingers were already at the bandolier" (L82) | ~135w | **FAIL (3)** |
| Hands | "one lift of her hand, palm up" (L238); "Amelia's grip closed on his arm" (L252); "Bal's fist clenched. He made it open again." (L256) | ~135w | **FAIL (3)** |
| Pauses (Toma) | "He let that stand." (L34); "He stopped." (L36); "For a breath he kept silent." (L48) | ~230w | **FAIL (3)** |
| Smile / face alight | "Amelia's mouth curved" (L262); "Amelia was shining" (L292); "Her face was alight" (L298) | ~330w | **FAIL (3)**. Shining/alight is also a word echo within 6 lines |
| Finger-snaps | Aren L248, Aren L276, Amelia L310 (all source) | ~530w | pass, by about 30 words. Do not add a beat between L248 and L310 |
| Smile/grin (other) | L30, L56, L114 | 2 max per 500w | pass |
| Laughs, blushes, nods, tilts, chest/heart, freezing | 0–1 each (L124 laugh; L18 "halted"; no nods) | — | pass |
| Prop fiddling | bandolier check (L68), which repeats Ch.28's stopper check ("All secure"); Toma brushes his sleeve (L92), used once | — | L68 is a cross-chapter echo (F7) |

**Shared gestures:** "pressed" against the barrier or air belongs to the girls 4 times (L22, L66, L136, L230; only L230 is source). Body parts that have opinions or object is a narrator device that has worn into a pattern: Ch.22 "thigh complained… decided not to forgive", Ch.24 "the house had opinions", Ch.28 "objected" twice, Ch.29 "His knees had opinions" (F5).

## Genesis Score

| Dimension | Score | Evidence | Cap Reasons |
|---|---|---|---|
| Originality | 8.5 | "It was like whipping a river. The blood passed clean through the light, and the light did not care." (L146). The column of blood "like a creek running under ice" (L186). Bal turns the duel rules into a shield for the girls (L46). | none |
| Theme | 8.5 | "I just want to live my life with my girls… But it isn't something I'm setting out to do." (L232). Protecting, not conquering, is enacted through the accidental conversion. Plenty of texture is not theme: the rusted gate "and something animal, long gone", who swept the arena, the fly. | none |
| Characters | **7.5** | Toma's grief is human: "As I cared for my fellow priests." He stopped. "But at least yours are still alive." (L36), and later the fly he won't brush off (L224). Raizen stays possessive and never addresses Bal. Aren is the judge. Inhabited chaos: "whether it needed feeding, and what on earth it would eat" (L222); "his arms folded under him" (L182). | **Capped at 7.5:** 13 gesture clusters (table). The content sits at 8.5. |
| Prose & Voice | 8.0 | Underlines: L146 (river); "To Bal it seemed to come from another country." (L168); "Raizen shook. Bal had taken that for a figure of speech until now." (L246); "Raizen's protest went with him before it was a word." (L276). Voice under pressure: "His foot came down wrong. The sand gave. / He crashed to the ground." Ugly sentence: "Bal blinked up at it. He didn't understand any of it." | Held at 8.0 by worn devices and echoes: "had opinions" (F5), "patient" twice (F6), "pressed" ×4 (F9), shining/alight (F21), counting tries (F23). Pattern #11 has 2 instances (0.5/1K), under the cap. |
| Pacing | 8.5 | Arrival, then terms, then a duel that accelerates into one-line paragraphs (L128–138), then the maelstrom, then a slower tribunal and a coda. The value shift is the largest in the book: from "he was about to die" to "It was over. It was really over." It hooks on the fire at home. | none |
| Emotion | 8.5 | Anchor: Akora turning to blood (L172) and the sygl on Toma's palm (L208). Surprise: the irrelevant thought about feeding it, and Raizen's literal shaking. Body rebel: "his arms folded under him." Investment: the mouthed "I'm sorry" (L138). The gods' alarm (L212) is real and brief, and the hug lands clean (L294). | none |
| Source Fidelity (Dim 7) | 8.0 | Every outline beat is present in source order. The author's corrected line is verbatim (L212). "Kona Niente" appears only at the duel opening. "I just want to live my life with my girls" and "Try not to start another war" are verbatim. Raizen's sentence (L268) is close to verbatim. The elemental is sent to her domain. No new spells. The four reworded lines keep their meaning: "This is exactly why we locked Amelia away!" ("in the first place" dropped), "Agreed" (for the nod), "I must return", and "At least somebody did" (which drops the "one of us" pairing but keeps the sense). | F1: the L38 logic slip. F2: "No sound came, and no flash" contradicts the source's "flashed into existence". F3: the dress at her knees contradicts Ch.2 and Ch.28. F4: the spent map-under-hand image. |
| **FLOOR** | **7.5** | | |
| **AVERAGE** | **8.2** | | Single-dimension weakness: Characters (mechanical) |

### The "They cannot hear you" reassignment: ACCEPTED
The source has "Lora nods, 'They can not hear you…'". Lora is inside a soundproof circle, and the line speaks of the girls in the third person ("They… their magyk"), so it cannot be hers. It is a source slip, and the standing ruling ("fix the source's small slips silently") covers it. Toma is the only speaker the context allows, and the line follows on naturally from his "They are fine." The meaning is unchanged. The cost is Lora's nod, which is replaced by Lora shaping words for him (L22). That beat is better and needs no nod. Recommendation: log it in STATE.yaml `decisions`, because the dialogue rule says "do not give a line to someone else" and the author should see the exception. (The character bible already records it.)

## CVI-Launch Breakdown
| Input | Score | Evidence |
|---|---|---|
| Commercial Pacing | 9/10 | The climax runs at speed and the tribunal resolves cleanly. |
| Tomorrow Test | 4 anchors → 10 | IMAGE: the storm turning to a column of blood. IMAGE: the red tears and the Blood sygl on Toma's palm. IMAGE: the fly on Toma's knuckles. QUOTE: "I just want to live my life with my girls." |
| Casual Reader | 8.5/10 | The underdog wins by accident, the villain god is locked away, and the payoff is huge. |
| Shareability (quote/plot/emotional) | 3/4/3 | max 8×0.6 + avg 6.7×0.4 = 7.5 |
| Concept Pitch | yes (10) | |
| Human Closeness | partial (5) | It is mostly a duel and a tribunal. Closeness comes in the hug and the girls at the barrier. |

CVI-Launch = 1.8 + 2.0 + 1.7 + 1.5 + 1.0 + 0.5 = 8.5, plus 0.5 for the strong anchor = **9.0**.
CVI-Legacy (default weights) = 8.5×.30 + 8.5×.25 + 3×.20 + 5×.15 + 3×.10 = **6.3**.

## Anti-AI Scan (20 patterns), about 3.76K words
1 Forced symmetry: minor. "whirled with him and through him and past him and back" (L150).
2 Empty poetic vocabulary: clear.
3 Rule of three: moderate (3, 0.8/1K). "There was also no such thing. They did not exist. They never had." (L176); "His shoulders first. Then his hands." (L290); the "cut his arms and his legs and his back and his face" run (L150).
4 Em dashes: clear (0).
5 Empty metaphors: clear.
6 Dramatic "And" openings: minor (1). "And through it…" (L152).
7 Pseudo-philosophical closings: clear.
8 Excessive parallelism: minor. The cutting run (L150).
9 Overly smooth transitions: clear.
10 Described emotions: minor. "Raizen was furious" (source); "she was enjoying herself enormously".
11 Explanatory extension: 2 (0.5/1K). The river simile plus "and the light did not care" (L146, earned); "Whatever entered the one entered the other." (L210).
12 Binary negation: minor (2). "No sound came, and no flash." (L198, F2); "though no light was left in it. No lightning anywhere. It was blood." (L172, earned).
13 Precision flex: moderate (5, 1.3/1K). "Thirty paces", "six rows up", "taller than three men", "On the third try… on the fourth" (L182; the source says "a few more faltering tries"), "Fifty-six" (a callback). F23 trims the counting.
14 Emotional control demonstration: minor. "Bal's fist clenched. He made it open again." (L256, source-based).
15 Authoritative description: clear. Gaps are left open (who swept the arena).
16 Philosophical asides: clear.
17 Clean dialogue: minor. The terms exchange is orderly (source), but "He did not give Toma room to answer" roughs it.
18 Thematic echo chamber: clear.
19 Graduated reveal: clear (duel, then tribunal).
20 Emotional temperature report: clear.
**Total: 8 of 20 present, mostly minor. Commercial clean band (0–8).**

## Character Chaos Check (Bal)
- Irrelevant thought: present and inhabited ("whether it needed feeding"; who swept the arena).
- Cognitive distortion: present ("they might as well have still been in Pashar").
- Unprompted memory: Amelia teaching the rules on the second night (L52) and Fern's file (L110). Both are triggered by the scene and return to it.
- Failed emotional management: present ("Bal lunged forward", L252).
- Voice under pressure: demonstrated (L126–138).

## Secondary Character Chaos
- Toma: has his own moment (the grief break; the fly).
- Raizen: fury that turns to fear; never speaks to Bal (bible-true).
- Aren: has his own moment ("mild and old and very tired"; "Try not to start another war").
- Amelia: has her own moment (the leap to the stands, the cruel excitement, the hug).
- Lora and Viridia: present only through the barrier (source). They get a distinct beat each in L22 (Viridia shouting, Lora shaping words).

## The Tomorrow Test
**What the reader remembers:** the storm elemental turning into a slow column of swirling blood, and Toma lifting his face with red tears running down it.
**Anchor type:** BOTH. Image (the blood elemental, the palm) and quote ("I just want to live my life with my girls").
**Verdict:** ANCHOR EXISTS.
**Shareable:** "He converted the enemy High Priest by accident, by turning his lightning elemental into a blood elemental."

## Reader Reports
- **Devourer:** won't stop anywhere. L126–166 is the fastest stretch in the book. The tribunal is shorter than feared.
- **Critic:** underlines the river simile, "another country", and Raizen's literal shaking. Would mark the looks/turns/breaths run in the tribunal (L192–L242) as stage-business padding, and notices "had opinions" coming back from Ch.24.
- **Hostile:** L38: "They would have watched Viridia choke" is false. The cask was Bal's poison and the priests never knew it; nightstalker poison kills by the next night and doesn't choke anyone. L198: "no flash" is wrong (the source says she flashed in). L58: a floor-length dress doesn't flare "around her knees". The vials are pending the author's call, so they are not scored.
- **Casual:** a clear triumph, a clear villain punished, warmth at the end. 8.5. The tribunal could drag slightly for this reader. The cuts below tighten it.

## Cross-Reader Matrix
| Issue | Devourer | Critic | Hostile | Casual | Severity |
|---|---|---|---|---|---|
| Gesture clusters in the tribunal (looks/turns/breaths) | x | x | | x | IMPORTANT |
| L38 Viridia "choke" logic | | x | x | | SHOULD FIX |
| L198 "no flash" vs source | | | x | | INVESTIGATE (fix: fidelity) |
| L58 dress at the knees | | | x | | INVESTIGATE (fix: continuity) |
| Worn devices ("had opinions", "patient" ×2, "pressed" ×4) | | x | | | INVESTIGATE |

## Revision Recommendations (Ranked: all cuts or swaps, no plot added)

| # | Location | Type | What happens now | Why it fails | Revision direction | Rule? |
|---|---|---|---|---|---|---|
| F1 | L38 | Logic | "They would have watched Viridia choke and called it a celebration." | The priests never knew of the poison (Bal's cask, Ch.25), and nightstalker poison kills the next night, not by choking | Cut the sentence | No |
| F2 | L198 | Continuity/source | "No sound came, and no flash." | Contradicts the source's "flashed into existence"; also binary negation (#12) | "Amelia flashed into being beside him, her bare feet on the sand at his elbow, and a heartbeat behind her came Raizen, with Aren after him." | No |
| F3 | L58 | Continuity | "her dress flaring out around her knees" | Her black dress falls to her ankles (Ch.2 L11; Ch.28 "long hem") | "her long skirt flaring out around her" | No |
| F4 | L110 | Style | ", with his map spread out under his hands" | The map-under-a-hand image is spent (ledger; Ch.18) | Cut the clause | No |
| F5 | L222 | Style | "His knees had opinions." | Recurring device: Ch.22, Ch.24 "had opinions", Ch.28 ×2 | Cut | Yes: retire body-part protest |
| F6 | L172 | Style | "patient, as if summoned" | "patient" again at L222 | Cut "patient," | No |
| F7 | L68 | Character | "Bal ran his fingers down the bandolier once. Every vial was where he had put it." | Repeats Ch.28's stopper check; hand cluster | Cut both sentences | No |
| F8 | L66 | Character | "Lora had both hands pressed together in front of her mouth." | Hand cluster; "pressed" ×4 | Cut | No |
| F9 | L22, L136 | Character | "both palms pressed to the air"; "pressed up together" | "pressed" ×4 for the girls; L230 (source) needs it | L22 "both palms flat against the air"; L136 "were up against the edge of it together" | No |
| F10 | L48 | Character | "For a breath he kept silent." | Third Toma pause in ~230w | Cut | No |
| F11 | L134 | Character | "Bal stared up into it, and he knew." | Look cluster (L106/L134/L136) | "Bal lay under it, and he knew." | No |
| F12 | L192 | Character | "Bal stood above him, at a loss." | Stand cluster | "Bal was at a loss." | No |
| F13 | L204 | Character | "Aren stood with his long white beard stirring in the breeze and studied Toma's huddled shape, and his old face was deeply troubled." | Stand plus look clusters | "Aren's long white beard stirred in the breeze, and Toma's huddled shape put a deep trouble in his old face." | No |
| F14 | L216, L218 | Character | ", raising his head to find Amelia"; "Amelia considered Bal for a moment before she gave Aren her answer." | Look cluster (7 looks) | Cut the clause; cut the L218 sentence | No |
| F15 | L226 | Character | "Then he turned to Bal." | Turn cluster | "Then he put his question to Bal." | No |
| F16 | L232 | Character | ", and brought his gaze back to Aren" | Look cluster | Cut the clause | No |
| F17 | L238 | Character | "Aren sought Amelia's agreement. She gave it with one lift of her hand, palm up… Aren breathed out through his beard. It would do." | Look, hand and breath clusters at once | "Amelia agreed at once, as if she had never wanted anything else, and Aren accepted it." | No |
| F18 | L252 | Character | "Amelia's grip closed on his arm." | Hand cluster | "Amelia stopped him." | No |
| F19 | L272 | Character | "It lasted until Bal forgot to breathe." | Breath cluster | Cut | No |
| F20 | L282 | Character | "His gaze came around to Bal, mild and old and very tired." | Look cluster | "When he spoke to Bal, his voice was mild and old and very tired." | No |
| F21 | L298 | Style | "Her face was alight." | Echoes "shining" (L292); smile cluster | Cut | No |
| F22 | L312 | Character | "Bal's brows rose in a question." | Brows/eyes cluster | "Bal didn't have to ask." | No |
| F23 | L182 | Style | "On the third try… and on the fourth he stood" | Counting (#13); source says "a few more faltering tries" | "After a few more tries he got as far as his knees, and then, swaying, he was up" | No |
| F24 | L316 | Style | "laced her fingers through his" | Echoes Ch.28's hook ("Her fingers fit between his") | "took his hand" (source) | No |
| Opt | L150 | Tone | "shredding the skin off him a strip at a time" | The brief says "not gory" | "shredding him" (source: "shredding it to pieces") | No |

### Fix order: F1–F3 (logic/continuity), then F7–F22 (gesture clusters), then F4–F6, F23, F24 (prose).

## Strengths to PRESERVE
The river simile (L146). "another country" (L168). The creek under ice (L186). The fly (L224). Raizen's literal shaking (L246). "before it was a word" (L276). Toma's grief break (L34–40). The author's corrected line, verbatim (L212). The feeding thought (L222). Fern's file callback ("*No inheritance gift*", L110, without the map). The hook.

## PATH TO 8.5
- **Characters 7.5 → 8.5:** apply F7–F22. They take every look/turn/stand/breath/hand/pause cluster under 3 per 500 words. The tribunal (L192–L242) is the main surgery: keep only the source's looks that carry a beat (L230, girls at the barrier). After the edit, re-run the hand count; finger-snaps must stay at 530+ words apart.
- **Prose 8.0 → 8.5:** F5, F6, F9, F21, F23, F24. The stopping sentences are already there (L146, L168, L246).
- **Source Fidelity 8.0 → 8.5:** F1–F4, and log the Toma "cannot hear you" reassignment in STATE decisions.

## VERDICT
**POLISH.** Floor 7.5, average 8.2, Casual 8.5. All mechanical gates are clean. It fails only on the hand count plus three logic/continuity/fidelity slips. Projected PASS after F1–F24. The blood-vial payoff is not scored (pending the author).

BIAS CHECK: This evaluation was produced by the same system that wrote the prose. Confidence in scores above 8.0 requires external validation (beta readers, editors, comp analysis).

## Revision applied (2026-10-21, book-editor)
- **F1–F24 + Opt applied** as quoted: Viridia "choke" sentence cut; "Amelia flashed into being beside him…" (now opens the section, replacing "Amelia was beside him." to avoid the doubled "beside him"); "her long skirt flaring out around her"; map clause, "had opinions", "patient," bandolier check, Lora's pressed hands, Toma's third pause, "forgot to breathe", "alight" cut; all look/stand/turn/breath/hand/brows swaps made; "a few more tries"; "shredding him".
- **Gate-driven equivalents** (quoted swaps tripped book-wide repeat gates): "both palms on the air" (not "flat against"); "The girls were together at the edge of it"; "To Bal he sounded mild and old and very tired."; "caught his hand" (not "took"); "Amelia agreed at once, plainly wanting nothing else, and Aren accepted it."; the "proud of you" line untagged; "Toma lowered his hands from his face."
- **Unlisted clusters also cleared:** L22 hands ("Viridia was hammering on nothing"; "Lora was beside her", stood ×3 in 70w); L22–44 looks ("Bal met his gaze and held it" cut; next line tagged "Bal said"); tribunal looks ("Bal saw his palm then" → "Then Bal understood…"; "He saw the rage drain" → "The rage drained…").
- **Author decision (vials):** at the core, after "every last drop": "When there was none left in him, he called on the two vials he had thrown at the start, and their blood rose from the sand and crossed the arena to him, and he forced that in too." Logged in STATE.yaml decisions.
- **Re-count:** no gesture class 3+ in 500w (gestscan clean; turns 2363/2982/3122 = 759w; snaps unchanged). Em dashes 0; "the way" 0; similes ~1.1/1k. ~3,620 words (in range, low end).
- **Gates:** style_check clean; grammar_check 0 errors; voice_wear_check clean; tic_report --gate clean (scratch copy Ch.1–30).
