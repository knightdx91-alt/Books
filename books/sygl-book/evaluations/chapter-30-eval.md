# Evaluation: Chapter 30 — The First Day
**Evaluator:** book-evaluator | **Date:** 2026-10-21

## HEADLINE
**CVI-Launch:** 8.7 | **CVI-Legacy:** 6.1 | **Genesis Floor:** 7.5 | **Genesis Average:** 8.1
**Engagement Type:** Self-Insertion / wish-fulfilment (primary), Empathy (secondary), Fascination (tertiary)
**Divergence Alert:** 1.2 (Launch over Floor), under 2.0. The coda is warm, short and does its job. What holds the floor down is mechanical, the same as Ch.29: a narrator device that has worn into a pattern (body parts that "complain"), plus the gesture-class windows. There are also three continuity and logic slips against Ch.27–29. Barda is the horse, not a place. Bal wore no shirt and no boots to the duel. All fixes are cuts or word swaps, plus at most three short quoted lines from the girls that contain only facts already on the page. With F1–F15 applied, the chapter projects to **Floor 8.5 / Casual 8.5: PASS**.

## Mechanical gates (scratch copy, Ch.1–30, `manuscript/chapters/`)
- `voice_wear_check.py`: **clean**. No retired phrases and no device over its cap. 3 non-strict cross-chapter self-repetition WARNs.
- `tic_report.py --gate`: **clean**. Ch.30 has 0 gate-class gesture hits. The hand count below finds clusters the gate's patterns don't classify.
- `style_check.py --dir`: clean. 0 em dashes and no "the way" similes. `grammar_check.py --file`: 0 errors.
- Length: 1,242 words of prose. The target is 1,300 (range 1,200–1,600), so it is in range. This is a coda by design, and no padding is requested.

## Hand gesture count (fail = 3+ of one class within 500 words)
Word positions are counted from the first prose line.

| Class | Instances (line) | Span | Result |
|---|---|---|---|
| Hugs/holds | the hug (L8–10, one beat); "took Lora by one shoulder… held them off" (L14, source); "He held on to them till the end." (L22) | ~320w | **FAIL (3)**. L22 is added. **F5** |
| Hugs/holds/touch | "caught up her hand" (L58, source); "ran his thumb over her knuckles" (L60); "touched Lora's shoulder" (L68, source); "hauled Lora up… took his hand anyway" (L72, source) | ~140w | **FAIL (4)**. The source alone supplies 3 of these (takes hand, touches shoulder, pulls to feet). Cut the addition. **F8** |
| Looks | "checked them from their hair down" (L14); "had seen his face" (L16); "kept looking anyway" (L18); "one look" (L18); "while he looked" (L20) | 5 in ~45w | **FAIL (5)**. The source has 3 (looking them over, seeing his look, continued looking). **F6** |
| Looks | "regarded the homework" (L44); "stared into it" (L46, source); "swung around to find him" (L54, source) | ~150w | **FAIL (3)**. L44 is added. **F7** |
| Sitting/posture | "dropped her onto the cushions" (L38); "wound up in a row on that couch" (L42, source); "feet drawn up" (L42); "leaned into him" (L62, source); "first on his feet… while he sat" (L72, source + add); "Lora knelt" (L74) | 7 in ~495w | **FAIL**. The source alone supplies 3. Cut two additions. **F4, F9** |
| Laughs | Amelia (L12), Viridia (L38), Bal (L68, source) | 457w / 400w windows | pass (2 max per window) |
| Smile/grin | "smiled at her" (L68, source) | — | pass (1) |
| Turning | "swung around" (L54); "faced the flames again" (L56) | — | pass (2) |
| Breath | "Viridia breathed out slowly" (L62) | — | pass in chapter. It follows Ch.29's "Aren breathed out through his beard", so the beat is consecutive across chapters. **F15**, optional |
| Eyes, chest/heart, nods, tilts, blushes, freezing | 0 | — | pass |
| Prop fiddling | glasses mashed (L8); "She pushed up her glasses" (L64); bootlace (L74); hair down (L74) | spread | pass. The glasses push is the 2nd in the book (Ch.12). Watch it, but it is not yet a signature |

**Narrator device (cross-chapter):** body parts that complain or hold opinions. Ch.13 "stomach… put in its opinion", Ch.17 "His back had something to say… complaining", Ch.22 "His thigh complained", Ch.24 "the house had opinions", Ch.29 "His knees had opinions", and **Ch.30 twice**: "His cuts all had complaints about the squeeze" (L10) and "he let them complain" (L72). This is a device that recurs chapter after chapter, so it caps Characters at 7.5 (**F4**).

**Shared gestures:** none between characters. Viridia vaults the table and Lora goes around it, the "same instant, different route" contrast.

## Genesis Score

| Dimension | Score | Evidence | Cap Reasons |
|---|---|---|---|
| Originality | 8.5 | "Lora went around like a sensible person and arrived at the same instant anyway" (L8). "found he liked thinking about due dates. They were the best thing he had thought about in days." (L44). Viridia's soundless shouting is finally heard: "she told them now what she'd been shouting. Some of it Amelia asked her to repeat, slower." (L32) | none |
| Theme | 8.5 | Belief and found family are enacted, not stated: "these two had been sure of him, surer than he'd been of himself on any single mile of that road" (L28). Then the source's "stand together." There is plenty of texture that is not theme: the runes homework, the log splitting, the plates, the bootlace. | none |
| Characters | **7.5** | Cover-the-name passes. Viridia vaults, grips, demands blow by blow, swears at a bootlace and claims the wall side. Lora hands over the beginning, tells the days "as carefully as she'd write up a potion" (L20), and has the lace undone "before Viridia was finished swearing" (L74). Amelia "needed no help whatsoever and took his hand anyway" (L72). Chaos: irrelevant thought (supper, the plates, L48); failed management ("There was no answer to that in him", L30). | **Capped at 7.5:** narrator complain-device (F4) and 5 gesture windows. The content sits at 8.5. |
| Prose & Voice | 8.0 | Underlines: L8 (sensible person), L44 (due dates), L72 ("took his hand anyway"), L74 (bootlace). Ugly sentence present: "which it was never built for" (L42). | Held at 8.0 by: the #16 aside "Days of not knowing weren't paid off by one look." (L18); somebody/nobody ×10 in 1,240w (F11); "The four of them" ×2 (F14). Pattern #11: 1 instance. |
| Pacing | 8.5 | Collision, then the account, then the fight retold, a break, the hearth, the source dialogue, the bedroom, the last line. The value shift is from fear-residue to settled peace. As a final chapter it needs no hook. The speed falls deliberately into the fire passage. | none |
| Emotion | 8.0 | Anchor: the closing line (QUOTE), plus "surer than he'd been of himself" (L28) and Viridia laughing until "her legs gave out" at Raizen's sentence (L38) (IMAGE). Surprise: relief arrives as due dates. Body rebel: Viridia's fist in his clothes, "as though he might be teleported off again". | The captivity account, which the outline calls out ("as they tell it"), is entirely narrated summary (L20). The girls get no spoken word about their own ordeal, so the book's most anticipated reported beat lands at arm's length. **F10** |
| Source Fidelity (Dim 7) | 8.0 | Every L1007–1013 beat is present in order: hug, arm's length, "We're okay", the account, belief, fight and exile talk, couch before the fire, Viridia's question (Bal on her left, L42 "Viridia on his right", correct), "live our life the best we can, and stand together", Lora's school/Dawn line, the laugh, shoulder and smile, "one hell of a break", to the bedroom, and the closing line **verbatim**. Fade-to-black. Unambiguously happy. Dialogue rewordings keep meaning ("unreal" for "surreal"; "Fair point"; "I won't pretend they aren't" renders "acknowledges"). "We knew you'd come" (L26) voices the source's belief and adds no information. | **F1:** "Out on the platform at Barda". Barda is Jazen's horse (Ch.27 L220). Bal was on the ground *below* the platform, and his apology was voiceless. **F2:** "what was left of his shirt". He went shirtless to the duel (Ch.28 L214). **F3:** "His boots were still on". He was barefoot (Ch.28 L214, Ch.29 L126). **F12:** "the big kitchen" is not established for the dorm (Ch.7: rooms appear on demand). |
| **FLOOR** | **7.5** | | |
| **AVERAGE** | **8.1** | | Single-dimension weakness: Characters (mechanical) |

## CVI-Launch Breakdown
| Input | Score | Evidence |
|---|---|---|
| Commercial Pacing | 8/10 | Short, warm and quick. The source dialogue block reads fast. |
| Tomorrow Test | 3 anchors (quote + image) = 9 | The closing line; Viridia vaulting the table; due dates as joy |
| Casual Reader | 8.5/10 | The reader gets the reunion they wanted. The summary-only account is the one soft spot. |
| Shareability (quote/plot/emotional) | 3/2/3 → 5.7 | "one hell of a break"; the closing line |
| Concept Pitch | yes | |
| Human Closeness | yes | The whole chapter is intimacy. |
CVI-Launch 8.2, with +0.5 for the strong anchor = **8.7**. CVI-Legacy: Orig 8.5, Theme 8.5, Vocab 2, Reread 4, Identity 4 = **6.1**.

## Anti-AI Scan (20 Patterns) — commercial thresholds; total 4 minor = CLEAN
1 symmetry: minor (L10 arm/arm). 2: clear. 3: minor (L72 triad, from the source). 4: clear (0 em dashes). 5: clear. 6: 1 ("And he knew", the source line, earned). 7: minor ("The good kind of quiet.", L50). 8–10: clear. 11: 1 (L10 "as though he might be teleported off again", acceptable). 12–15: clear. 16: 1 (L18 "Days of not knowing…"). 17: the source exchange is orderly, but the account scene has cross-talk (L20), so mostly clear. 18–20: clear.

## Character Chaos Check (Bal)
Irrelevant thought: present (supper, plates, due dates). Cognitive distortion: absent (appropriate). Unprompted memory: present and triggered (the apology under the whip, prompted by "We knew you'd come", returning to the scene). Failed management: present (L30). Voice under pressure: not tested (coda).
Secondary: Viridia, Lora and Amelia each have their own moment (vault, bootlace, "took his hand anyway").

## The Tomorrow Test
**Remembers:** "the first day of the rest of their life together" over the bedroom doorway, and Viridia vaulting the table while Lora goes around. **Type:** BOTH. **Verdict:** ANCHOR EXISTS.

## Residue Test (final chapter)
Contentment and safety, with no evaluative aftertaste. It matches the foundation's intended residue: the ending is unambiguously happy, with no dread added.

## Reader Reports
- **Devourer:** reads straight through. The source dialogue block is brisk and the last line closes the book cleanly. They would like one line of the girls actually *saying* what happened.
- **Critic:** underlines L8, L44, L72 and L74. Flags the complain-device, the look cluster at L14–20, and "Days of not knowing…".
- **Hostile:** "platform at Barda" (that is the horse); a shirt and boots that don't exist; a dorm kitchen nobody has mentioned. Bal is flayed by glass and nobody remarks on it beyond the squeeze. That is defensible in a coda, so INVESTIGATE only, no fix required.
- **Casual:** loves the hug and the bedtime. Would tell a friend "the ending is so sweet." Feels the summary at L20 as "wait, what happened to them?" (VIBES, see F10).

## Cross-Reader Matrix
| Issue | Dev | Crit | Host | Casual | Severity |
|---|---|---|---|---|---|
| Account all summary (F10) | x | x | | x | IMPORTANT |
| Continuity slips (F1–F3) | | x | x | | SHOULD FIX (Logic, fix first) |
| Complain-device / gesture clusters (F4–F9) | | x | x | | SHOULD FIX (gate-relevant) |
| somebody/nobody, "four of them" (F11, F14) | | x | | | INVESTIGATE |

## Revision Recommendations (fix order: Logic → Character → Prose)

| # | Location | Type | Now | Why it fails | Revision direction | Rule? |
|---|---|---|---|---|---|---|
| F1 | L28 | Logic | "Out on the platform at Barda, with the storm mage's whip over his face, he had told them he was sorry." | Barda is the horse. Bal lay on the ground below the platform. | → "Flat on his back under the storm mage's platform, with the lightning whip over his face, he had told them he was sorry." | No |
| F2 | L10 | Continuity | "Viridia had one fist knotted in what was left of his shirt" | Shirtless since Ch.28 L214 | → "Viridia had one fist knotted in the strap of his bandolier" | No |
| F3 | L46 | Continuity | "His boots were still on and that was fine." | Barefoot in Ch.28/29 | → "His feet were still bare and gritty with arena sand, and that was fine." | No |
| F4 | L10, L72 | Character (narrator device) | "His cuts all had complaints about the squeeze. He told them to wait their turn." / "His legs had stiffened while he sat, and he let them complain." | 7th–8th use of the body-complains device (Ch.13/17/22/24/29); also a posture hit | L10 → "His cuts stung under the squeeze, and he let them." Delete the L72 sentence entirely. | **Yes**: retire "body part complains/has opinions" book-wide |
| F5 | L22 | Character (gesture) | "Bal heard every word. He held on to them till the end." | 3rd hold within ~320w | → "Bal heard every word." | No |
| F6 | L18–20 | Character (gesture) / Style #16 | "He kept looking anyway. Days of not knowing weren't paid off by one look. / They told him while he looked." | 5 looks in 45w; coffee-mug aside | Delete "Days of not knowing weren't paid off by one look."; "They told him while he looked." → "They told him all of it." | No |
| F7 | L44 | Character (gesture) | "Bal regarded the homework and the due dates waiting behind it" | 3 looks in ~150w | → "Bal thought about the homework and the due dates waiting behind it" | No |
| F8 | L60 | Character (gesture) | "He ran his thumb over her knuckles and the earth ring there." | 4 touches in ~140w (3 from the source) | Delete the sentence. | No |
| F9 | L42 | Character (gesture) | "Amelia had the end, with her feet drawn up on the cushion." | Posture window over the limit | → "Amelia had the end." | No |
| F10 | L20 | Emotion / Exposition | The whole account is summary: "Viridia told how they'd been taken… Lora took over for the days after…" | The outline's "as they tell it" beat gets no voice. Readers waited three chapters for this. | Add at most three short quoted lines using only facts already on the page (Bal downed by the bolts in Ch.27; held in Pashar; unharmed per Toma, Ch.29). E.g. after "handed Viridia the beginning": *"You went down and you didn't get up," Viridia said. "That was the worst part."*; for Lora's days: *"No one hurt us. They just kept us."*; and the cut-in quoted: *"She's making it sound tidy," Viridia said. "It wasn't tidy."* No new events. | **Yes**: reported off-page ordeals get at least one line in the teller's own voice |
| F11 | L10, L44 | Style | somebody/nobody ×10 in 1,240w | Reflex density | L10 "until somebody made him" → "for anything"; L44 "Somebody's runes homework" → "Runes homework". Keep the deliberate "Nobody was hunting anybody. Nobody had to be…" at L76. | No |
| F12 | L48 | Continuity | "Through the wall the big kitchen sat dark." | No dorm kitchen is established | Delete the sentence. "Had the dorm thought to put out any supper?" stands alone. | No |
| F13 | L50 | Style #7 | "It was quiet a long while. The good kind of quiet." | Mild pseudo-closing | → "It was quiet a long while." (optional) | No |
| F14 | L42 | Style | "The four of them wound up in a row" (2nd "The four of them", after L8) | Echo | → "They wound up in a row" | No |
| F15 | L62 | Style (cross-chapter breath) | "Viridia breathed out slowly and leaned into him" | Breath beat right after Ch.29's | → "Viridia leaned into him, warm and heavy on his shoulder." (optional) | No |

## Strengths to PRESERVE
The closing line, verbatim. Viridia vaults while Lora goes around. "as carefully as she'd write up a potion". Viridia's unheard shouting retold. Viridia, once Heir of Raizen, laughing until her legs give out. The due-dates joy. The plates callback to Ch.7 (one echo only; do not use it again). "took his hand anyway". The bootlace. "Nobody was hunting anybody."

## PATH TO 8.5
- **Characters 7.5 → 8.5:** apply F4–F9. After that, every remaining window is down to the source's own three beats.
- **Prose 8.0 → 8.5:** apply F6 (the aside), F11 and F14. The underline sentences already qualify.
- **Emotion 8.0 → 8.5:** apply F10. Three lines at most, and each one must restate facts from Ch.27/29.
- **Source Fidelity 8.0 → 8.5:** apply F1, F2, F3 and F12.

## How the ending lands for the book
As the close of a found-family progression fantasy, the ending works. The source's own last page is respected beat for beat. The tone is untroubled, exactly as the author ruled: no residue of dread, no guilt, no stinger. The coda's small domestic textures (homework, bootlace, a contested wall side) answer a book that began with a sygl-less orphan alone on a roof. Bal ends inside a home with three people who were sure of him. The final line, plain and a little old-fashioned, reads as earned because everything before it is calm and specific. The one thing that keeps the ending from landing at full weight is that the girls never speak about their ordeal. Give them a line each, and the last chapter closes the book's emotional loop as well as its plot.

## VERDICT
**POLISH**. Floor 7.5, Casual 8.5. After F1–F15, the chapter projects to Floor 8.5: PASS.

BIAS CHECK: This evaluation was produced by the same system that wrote the prose. Confidence in scores above 8.0 requires external validation (beta readers, editors, comp analysis).

## Revision applied (2026-10-21, book-editor r1)
- **F1** "Out on the platform at Barda" → "Down in the dirt below the platform, with the storm mage's whip humming over his face" (Ch.27: thrown off the platform to the ground; the whip hummed. "Flat on his back" and "the lightning whip" tripped book-wide repeat gates, so equivalent wording was used.)
- **F2** shirt → "the strap of his bandolier". **F3** boots → "His feet were still bare and gritty with arena sand".
- **F4** "His cuts stung under the squeeze, and he let them."; the L72 legs-complain sentence deleted. Body-complains device retired in this chapter.
- **F5, F6, F8, F9, F11, F12, F13, F14** applied as quoted. F6 "They told him all of it" became "They told him everything" to clear a cross-chapter self-repeat ("all of it at"). F7 "Bal thought about" (3x book-wide) became "Bal's mind went to the homework".
- **F15** "Viridia's head came down on his shoulder, warm and heavy." (no breath beat, no lean).
- **F10** three spoken lines, facts from Ch.27/29 only: "You went down and you didn't get up," Viridia said. "That was the worst part." / "No one hurt us," she said. "They just kept us." / "She's making it sound tidy," Viridia said. "It wasn't tidy."
- **Window trims beyond F-list:** "because his face had given him away" (look); "She swung around toward Bal, on her left." (look); "Lora knelt" → "Lora had it undone" and "He was first on his feet" cut (posture); "Bal brought Lora up with him" (repeat gates on "up off/from the", "from the couch").
- **Closing line verbatim.** Happy coda, fade to black intact.
- **Gates:** gestscan clean; em dashes 0; "the way" 0; similes 2. style_check, grammar_check, voice_wear_check (strict) and tic_report --gate all clean (scratch copy, Ch.1–30).
- **Note:** prose is now ~1,186 words, 14 under the 1,200 floor, because every fix was a cut. No padding was added, per the evaluation. Remaining touch beats in the last ~140 words (her hand, Lora's shoulder, "took his hand anyway") are all source beats.
