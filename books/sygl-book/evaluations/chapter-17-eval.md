# Evaluation: Chapter 17 — Saegen Woods
**Evaluator:** book-evaluator | **Date:** 2026-10-20
**Text evaluated:** `manuscript/chapter-17.md` (2,630 words of prose; target 2,700, range 2,400–3,100, so on spec).
**Read first:** STATE.yaml (decisions, including the juggling-talk Bal-only POV ruling), book CLAUDE.md, project/STYLE_CONSTRAINTS.md, project/foundation.md (Magic ledger), character-bible.md (Lora, Soren, Ms. Summers, Hopper, the at-risk list), outline Ch.17, chapter-16.md (being revised in parallel, so continuity was checked against its current text), Sygl_Complete.txt L748–766, evaluations/chapter-16-eval.md.

## HEADLINE
**CVI-Launch:** 8.3 (7.8 + 0.5 strong anchor) | **CVI-Legacy:** 6.3 | **Genesis Floor:** 7.5 | **Genesis Average:** 8.1
**Engagement Type:** Self-Insertion (primary) / Empathy (secondary) / Fascination (tertiary)
**Divergence Alert:** none (0.8 gap).

**VERDICT: POLISH.** On merit this is a warm, light 8.5 chapter, and the juggling talk works as the real conversation the author wanted:
- The stones drop *before* he answers ("He let the stones fall. They clattered onto the gravel and lay among all the others, and in a moment he could no longer tell which had been his.", L164).
- "I do not feel more strongly for one over the other" is kept verbatim (L170).
- The overhearing is only implied, through what Bal sees and hears (gravel close behind, the girls nearer than he thought, then dropping back and talking low).
- The torn dress is handled as embarrassment only ("torn her dress open high on the bodice", flaming cheeks).
- There is no nod, and no invented spell.

Three mechanical problems hold the floor at **7.5**:
1. **Look-class clusters.** These cap Characters.
2. **Four Pattern #11 explanatory extensions (1.5/1k).** The commercial cap is 0.8/1k, so this caps Prose.
3. **One retired invented habit is back.** Lora "out there every evening since, moving jars around" brings back the habit STATE removed ("Lora reorganizing supplies").

Every fix below is a cut or a word swap. None adds plot. With F1–F17 applied, the chapter projects to **Floor 8.5 / Casual 8.5: PASS.**

## Gate tools (scratch copy, Ch.1–17 at `/tmp/claude-0/-home-user/925d8686-989e-5134-a9ef-2d597d7cac42/scratchpad/ev17/manuscript/chapters/`)
- `voice_wear_check.py`: **clean.** No retired phrases and no device over cap. Two self-repetitions are reported as WARN only, not strict.
- `tic_report.py --gate`: **FAIL, but not on Ch.17.** The single recurring phrase is "his right hand" in Ch.1, 12 and 16. Ch.17 has no gesture class in the tool's table, 1 and-chain (cap 9) and 0 negation pivots. Resolve it in the parallel Ch.16 revision: the source wording there is "on his right hand", so vary Ch.1 or Ch.12 instead, or allowlist the phrase.
- `style_check.py --dir manuscript`: **clean.** Em dash count is 0.
- `grammar_check.py --file chapter-17.md`: 0 errors.
- The gesture hand count below covers the classes the tool does not classify.

## Gesture hand count (full, 500-word windows)
| Class | Ch.17 instances (line) | 3+ in 500w? | Verdict |
|---|---|---|---|
| Smile/grin | grinned L132 (source), smiled grimly L152 (source) | no (2) | OK |
| Laughs | 0 | — | OK |
| Blush | Lora "gone pink and stayed pink" L38 (invented); Amelia "cheeks were flaming red… very bright indeed" L130 (source) | no | **Cross-chapter recurrence.** "went pink" also appears in Ch.13 ×3, Ch.14 and Ch.16 ("so warmly that Lora went pink"). Lora goes pink in consecutive chapters → F2 |
| Looks/glances/watching | checked the map L14, study the forest L18, squinting L48; looked him over L106, inspected L106, checked the vials L108, glares L114, checked her front L128, caught it on their faces L128; watching L152, watched L156, glance L160, checked behind L172, watched L174 | **YES ×3.** L14–48 has 3 in about 475 words. L106–128 has 6 in about 250 words. L152–174 has 5 in about 280 words. | **CAP.** This class is already flagged book-wide near the density cap → F3–F8 |
| Face (expression) | "all over her face" L40, "Her face lit up" L72, "face was white and set with fury" L98, "face went blank" L124, "on their faces" L128, "On her white face" L130 | **YES.** L98–130 has 4 in about 420 words. | Fixed by the same cuts (F1, F5, F6) |
| Sitting/sinking/crouch | down on her heels L70 (source crouch), one knee under him L94 | no | OK |
| Freezing/stopping | none as gesture (birds stopped, tree stopped him: not body business) | — | OK. The adverb "still" appears 3 times in about 120 words (L102, 114, 120) → F17 |
| Eyes | "his eyes would focus" L98 | no | OK |
| Chest/heart | waves at his chest L126 (source) | no | OK |
| Hand holds/squeezes | "was holding his hand instead" L202 | no | **Ending-move repeat.** Ch.16 closes on hands: "kept hold of her hand", "Amelia's hand found his", "fell asleep holding on to her". Ch.17 closes on her hand in his → F10 |
| Nods | 0 (the source's "Amelia nods" is dropped, correctly) | — | OK |
| Turns | turned L118, spun L128 (both source) | no | OK |
| Sound reprise | "gravel crunched" L10, L154, L172 | 2 within about 150 words | Minor: L154 dulls the functional crunch at L172 → F16 |

## Source fidelity (L748–766)
Every beat is present and in order:
- **The pass and the plan.** Gravel pass, half a mile, hill and worn path ✓. Map, "Well, this is it" (fixes the source's "Bay") ✓. Lora's paper from her pocket, which ties to the Ch.16 receipt ✓. River 500 ft in ✓. They follow the river because they need water ✓.
- **The lore.** Aurora felis is rare, healing, blood red and yellow, blooms every three years, hurry, seventy-two hours, expensive, two potions as part payment, money needed only for dues, Lora excited to watch a master ✓.
- **The river.** Bright fish ✓. Viridia's ley-line line ✓. Amelia on consuming energy, "quite large indeed", nothing that can't be killed, Hopper's pelt ✓.
- **The flowers.** Six flowers, three kept ✓. Amelia's question ✓. Lora cuts them into six vials, "no use being greedy", a month's income, her face lights up, "She's lonely, I think" ✓. Padded vials into Bal's pack ✓. Apprentice and "An alchemist is important" ✓.
- **The bear.** The quiet ✓. Hit, across the river, into the tree, head snapped back, unsteady ✓. "not really hurt. The thing that had hit him was." ✓. Amelia chokes it by the neck in fury, "kill it a second time" ✓. Bear ✓. Carried over the river and glad not to swim ✓. Checked over, vials safe in the side pocket ✓.
- **The dress.** Glares ✓. "Uh. Amelia" / "Yes?" with the playfulness gone ✓. Clothes line, blank look, wave at chest, turns away ✓. Embarrassment only ✓. The girls saw and kept quiet ✓. Flaming cheeks, Bal grins, they give her time ✓.
- **The pass talk.** Bal walks beside her, thanks her for the bear ✓. "I honestly never heard it… very old" ✓. Stones, "lightly", learned as a boy ✓. "You have no idea… It had tried to run… didn't get far", grim smile ✓. "So you like to juggle, huh?" ✓. Glance to the girls, "wasn't talking about the rocks" ✓. **The stones fall before the answer** ✓. Both lines ✓. Overhearing implied only (author ruling) ✓. Amelia thinks in silence, a few miles ✓. Girls talk low, Hopper trots happily ✓.
- **The return.** Straight back, uneventful ✓. Dawn Hall staffed round the clock, Soren ✓. Change to the reward, ledger, recount minus dues ✓. Stew ✓. After curfew, hugs ✓. Bal exempt from curfew ✓ (Ch.7 canon: Lead Mage). The slow walk ✓.

**Dialogue rule.** The author's lines are the base, with grammar fixed. Two changes need comment:
- "they mean a lot to me" becomes "how much they matter to me". This is acceptable: it avoids echoing Ch.16's "You mean a lot to me", and the anchor clause is verbatim.
- "if Lora and Viridia would have had to fight it" becomes "if **the girls** had had to fight it". Spoken *to Amelia*, this makes her not one of "the girls", and it puts the at-risk "the girls/my girls" phrasing into Bal's mouth. Restore the names → F14.

**Inventions:**
- L40, "she had been out there every evening since, moving jars around": an **invented habit**. STATE explicitly removed "Lora reorganizing supplies". **CRITICAL** → F1.
- L204, "By next week they would need another": an invented *need*. The source says none of them needs the money, and Ch.18's reason for jobs is getting away from the school → F11.
- L202, the torn dress carried into the final beat: it extends the dress past the embarrassment moment → F10.

Harmless texture, no plot: Viridia's spear as a walking stick, the cold water, the fishing thought, "accepted three, though he suspected it had been two", "Side pocket," the Whitehaven collar.

**Continuity:**
- The bandages and back from Ch.16 ✓, the town-limit collar ✓, the herb room (Ch.15 name) ✓, the Blood dorm ✓.
- Slip: L184 "the guild hall off the square". Ch.13 L294 places the Dawn Hall "at the top of the square" → F12.
- Clarity: L106 "On the far bank" comes right after he is carried "back to the other bank". Which bank is meant is ambiguous → F13.
- Small logic: L144 "flat and smooth, egg-sized" stones for juggling. Flat stones are poor for juggling and are not egg-shaped → F15.

## Magic-repetition note
There are **no spells** in this chapter, which matches the source. Amelia kills the bear with her bare strength, and Hopper's collar is a Ch.13 item. Nothing is invented and nothing repeats. No flag to the author is needed.

## Genesis Score (Craft Assessment)

| Dimension | Score | Evidence | Cap Reasons |
|-----------|-------|----------|-------------|
| Originality | 8.5 | The juggling metaphor resolved physically: the stones "lay among all the others, and in a moment he could no longer tell which had been his" (L164). The bear told as aftermath pieced together by a concussed POV ("he had to put it together from what was in front of him", L98). "something had eaten something that had eaten something, for generations" (L54). | none |
| Theme | 8.5 | The book's question (can love for three be fair and freely chosen?) is embodied in the source's own beat and never stated by the narrator. The girls' choice is set up by implication. Plenty of plain texture (cold water, fingers, stew, second bowl). | none |
| Characters | **7.5** | On merit 8.5. Lora is fluent on craft ("Aurora felis is rare…", L32) and hedged with people ("Oh. Um. The reward's changed a little", L190), which matches her card. Amelia moves from fury to mortification to silence. Viridia is practical. Hopper is wanted-or-not. Chaos (commercial): irrelevant thought ✓ (the fishing, L54); triggered memory that returns to the scene ✓ (juggling learned as a boy, L148); failed management ✓ (Amelia's fury and flaming cheeks); distortion ✗. 3/4. | **Gesture-class cap:** look class 3+ in 500 words three times (L14–48, L106–128, L152–174); face cluster L98–130; Lora's "went pink" recurs in consecutive chapters. **Invented habit** (L40). |
| Prose & Voice | **7.5** | Underlines: "For a while the world was green and full of bells." (L92). "The birds had stopped, and he had missed them going." (L82). "asked how many fingers she was holding up, and accepted three, though he suspected it had been two." (L106). Close-the-book: L164, the stones lost among the others. Under pressure the voice breaks into fragments ("He got one knee under him. Then the other foot. The tree helped.", L94). Ugly sentence present ("The water went by underneath him.", L90). American register throughout ("Pretty much", "Uh", "I figured"). The book-wide "grey" convention stands. | **Pattern #11: 4 instances (1.5/1k > 0.8 commercial cap):** "It was all over her face." (L40); "On her white face it was very bright indeed." (L130); "He had believed they were much farther back." (L174); "He had put it about as plain as it would go, and there was no plainer way he knew of" (L178). Plus #16: "There were always more stones." (L178). Read beside the juggling talk, that line also implies more girls are coming, which is a **tone hazard**. |
| Pacing & Coherence | 8.0 | Value shift: errand (+) → bear and torn dress (−) → the talk lands (+). Speed variation is good: unhurried lore, a one-line hit, fragmented recovery, a slow walk. Scenes break about every 300 words. | Closing line invents a need (L204) and dilutes the outline hook. Small continuity slip (L184). |
| Emotion | 8.5 | Anchor: the stones drop, then the line (L164–170). Emotional surprise: Bal *grins* at her embarrassment minutes after a bear threw him into a tree (L132), and the comic finger count inside the concussion check. Body rebel: Amelia's flaming cheeks; her fury past reason ("I snapped"). Techniques: physical, humor-in-danger, restraint, anticipation (the girls overhearing). | none |
| Engagement (Dim 7) | 8.5 | Self-insertion: a goddess kills a bear for him, and he tells the truth about loving three. Empathy: Amelia's mortification. Fascination: what the girls heard. | none |
| **FLOOR** | **7.5** | | Characters (gesture cap and invented habit); Prose (Pattern #11) |
| **AVERAGE** | **8.1** | (8.5×4 + 7.5×2 + 8.0) / 7 = 8.14 | |

## CVI-Launch Breakdown
| Input | Score | Evidence |
|-------|-------|----------|
| Commercial Pacing | 8/10 | Short scenes, a bear in the middle, the talk at the end |
| Tomorrow Test | 2 anchors (image + quote) → 7 | The stones lost in the gravel; "I do not feel more strongly for one over the other" |
| Casual Reader | 8.5/10 | Warm, funny, a romantic payoff |
| Shareability (quote/plot/emotional) | 3/2/3 → 5.7 | The juggling line; the bear choked by a goddess |
| Concept Pitch | yes (10) | |
| Human Closeness | yes (10) | |
| **CVI-Launch** | 7.8 + 0.5 (strong anchor) = **8.3** | |

CVI-Legacy is unchanged from Ch.16 at **6.3**.

## Anti-AI Scan (20 Patterns), 2,630 words
1. Forced symmetry: Clear. "He was not really hurt. The thing that had hit him was." is from the source.
2. Empty poetic vocabulary: Clear.
3. Automatic rule of three: Minor (1, 0.4/1k). "the first stone… the second… the third" is literal, so acceptable.
4. Em dashes: Clear (0).
5. Empty metaphors: Clear.
6. Dramatic "And" openings: Clear. One appears in dialogue only.
7. Pseudo-philosophical closing: **Found (1).** "There were always more stones." (L178).
8. Excessive parallelism: Clear.
9. Overly smooth transitions: Minor. "Next they checked the vials." (L108).
10. Described emotions: Minor. "which was a relief" (L186) and "He was glad" (L102) are both from the source.
11. Explanatory Extension: **Found (4, 1.5/1k, strong).** L40, L130, L174, L178. See Prose.
12. Binary negation: Clear.
13. Precision flex: Clear.
14. Emotional control demo: Clear.
15. Authoritative description: Clear.
16. Philosophical asides: **Found (1).** L178, the same line as #7.
17. Clean dialogue: Minor. Exchanges are orderly, broken only by "Uh." and "Um."
18. Thematic echo chamber: Clear. There is plenty of texture.
19. Graduated reveal: Clear. The chapter does not close on tension.
20. Temperature report: Clear.

**Total:** 4 patterns with real weight (#7, #11, #16, #17 minor), which is in the clean range for commercial fiction.

## Character Chaos Check (Bal)
- Irrelevant thought: present (L54).
- Cognitive distortion: absent.
- Unprompted memory: present. Juggling as a boy, triggered by the stones and returning to them (L148).
- Failed emotional management: present, in Amelia.
- Voice under pressure: demonstrated (L88–98).

## Secondary Character Chaos
- **Lora:** has her own moment ("Side pocket," faintly, fingers to her mouth; the lonely-alchemist read).
- **Viridia:** has her own moment (the chin tilt, drinking from her cupped hands, the low word to Lora).
- **Hopper:** has her own moment (wading in, trotting over "in case she was wanted").
- **Soren:** functional, which is right for her card. The eyebrow stays spent.

## The Tomorrow Test
**What the reader remembers:** the stones falling into the gravel and becoming indistinguishable, then "I do not feel more strongly for one over the other."
**Anchor type:** BOTH. **Verdict:** ANCHOR EXISTS. It is a different type from Ch.16's (stillness) and Ch.14's.

## Shareability
"He stopped juggling the rocks to tell her he loves all three equally, and they heard."

## Reader Reports
- **Devourer:** The bear lands at the halfway mark, and the talk pays off the harem question. They might slide through the lore paragraph (L32) but would not stop. The final line is flat.
- **Critic:** Would underline L82, L92 and L164. Would be disappointed by L178's reprise ("always more stones" undoes L164 by explaining it), by "very bright indeed", and by "He had believed they were much farther back".
- **Hostile:** Would challenge "flat and smooth, egg-sized" juggling stones; which bank is "the far bank" (L106); "guild hall off the square" against Ch.13; Lora's evening jar-moving as a new habit; and "need another" when nobody needs money. Would also note the run of looks during the talk: watching, watched, glance, checked, watched.
- **Casual:** Likes it. The bear is fun, Amelia is adorable when mortified, and the line is sweet. 8.5.

## Cross-Reader Matrix
| Issue | Devourer | Critic | Hostile | Casual | Severity |
|---|---|---|---|---|---|
| L178 stone reprise / "always more stones" | | ✓ | ✓ | ✓ (tone) | IMPORTANT |
| Look cluster in the talk (L152–174) | | ✓ | ✓ | | SHOULD FIX (gate cap) |
| Invented habit L40 | | ✓ | ✓ | | SHOULD FIX (canon law → CRITICAL) |
| Flat final line L204 | ✓ | | ✓ | | SHOULD FIX |
| Pattern #11 extensions | | ✓ | | | INVESTIGATE (Prose cap) |
| Bank ambiguity, flat stones, hall location | | | ✓ | | INVESTIGATE |

## Revision Recommendations (ranked; cuts and swaps only, no plot)

| # | Location | Problem type | What happens now | Why it fails | Revision direction | Project rule? |
|---|---|---|---|---|---|---|
| F1 | L40 | Character / canon | "She was already halfway into that shop in her head. It was all over her face. She had spent her own money last week on plants and supplies to stock the herb room off the dorm, and she had been out there every evening since, moving jars around." | It revives the retired invented habit ("Lora reorganizing supplies"). "It was all over her face" is #11 and part of the face cluster. | Replace with: "She was already halfway into that shop in her head. She had already bought plants and supplies to stock the herb room Bal had put in for her, and now she was going to watch a real master work from start to finish." | Yes (already law) |
| F2 | L38 | Character (gesture) | "and Lora had gone pink and stayed pink for most of a street" | The blush class recurs: Lora went pink in Ch.16 too, and Ch.13–14 have it as well. It is invented. | Cut the clause. End the sentence at "without much of a discussion." | Yes: Lora's blush is closed until a source beat |
| F3 | L48–50 | Character (gesture) | "Viridia kept squinting at the fish as they walked." | Third look in 475 words. | Cut the line. Make L50 read: "I'm surprised they're normal size," Viridia said as they walked. "I figured…" | No |
| F4 | L106 | Character (gesture) | "the girls looked him over. Viridia tipped his chin up and inspected the knot" | Look cluster. | "On their own bank the girls went over him. Viridia tipped his chin up and found the knot…" (also fixes F13) | No |
| F5 | L128 | Character (gesture) | "Both girls had seen already. Bal had caught it on their faces while they were fussing over him. They had kept quiet about it, which Bal found interesting." | Look and face cluster. | "Both girls had seen it already, while they were fussing over him, and had kept quiet about it, which Bal found interesting." | No |
| F6 | L130 | Style (#11) | "Her cheeks were flaming red. On her white face it was very bright indeed." | It explains the blush. "indeed" is Amelia's word from L52, bleeding into the narration. Face cluster. | Cut the second sentence. | No |
| F7 | L152 | Character (gesture) | "You have no idea." Amelia was watching the stones. "Seeing you…" | First of 5 looks in about 280 words. L156 (source) already has her watching. | Cut "Amelia was watching the stones." | No |
| F8 | L172–174 | Character (gesture) / Style (#11) | "Bal checked behind him. Lora and Viridia were nearer than he had thought, only a couple of paces off. He had believed they were much farther back. While he watched, Viridia said…" | Two looks plus a restatement. | "Gravel crunched behind them, close. Over his shoulder, Lora and Viridia were nearer than he had thought, only a couple of paces off. Viridia said something to Lora, too low to hear, and the two of them slowed…" | No |
| F9 | L178 | Style (#7/#11/#16), tone | "He had put it about as plain as it would go, and there was no plainer way he knew of, so that would have to do. The stones were back in the pass somewhere among all the others. That was fine. There were always more stones." | It restates L164's image and moralizes it. "always more stones" reads as more girls coming, which contradicts the talk. | Keep "Bal ran through it again in his own head." Cut everything from "He had put it" to "more stones." Continue "They left the pass…" | Yes: a single-use image is not reprised in the same chapter |
| F10 | L202 | Character (gesture) / continuity | "She had stopped holding the torn place in her dress at last and was holding his hand instead." | Hand-holding closes Ch.16 and Ch.17 back to back (ending-move repeat). It also extends the dress past the embarrassment beat. | Cut the sentence. "The castle was dark around them. They did not talk." | No |
| F11 | L204 | Pacing / logic | "One job down, he thought. By next week they would need another." | Invented need: nobody needs the money (L38). It pre-empts Ch.18's reason for taking jobs. | Cut the line and end on "They did not talk." Or keep only "One job down, he thought." | No |
| F12 | L184 | Continuity | "the guild hall off the square" | Ch.13 L294 has it "at the top of the square". | "went straight to the Dawn Hall at the top of the square" | No |
| F13 | L106 | Logic (clarity) | "On the far bank" | Right after "back to the other bank", it is unclear which bank is meant. | Covered by F4 ("On their own bank"). | No |
| F14 | L140 | Voice / dialogue rule | "if the girls had had to fight it" | Said to Amelia, it excludes her. The source names them, and "the girls" is on the at-risk list. | "if Lora and Viridia had had to fight it" | No |
| F15 | L144 | Logic | "flat and smooth, egg-sized" | Flat stones are poor for juggling, and flat contradicts egg-sized. | "round and smooth, egg-sized" | No |
| F16 | L154 | Style | "They walked. The gravel crunched." | It dulls the functional crunch at L172. | Cut "The gravel crunched." | No |
| F17 | L120 | Style | "She was still in the fight, he figured." | Third "still" in about 120 words (L102, L114). | "Her head was in the fight, he figured." | No |

### Fix order
- Character/logic first: F1, F2, F11, F14, F15, F12, F13.
- Gesture cuts: F3–F8, F10.
- Prose: F6, F9, F16, F17.

## Strengths to PRESERVE
- L164, the stones lost among the others. This is the close-book sentence.
- L82, the birds stopping.
- L92, "green and full of bells".
- L94, the fragmented recovery.
- L106, the three-or-two fingers.
- L54, the fishing thought.
- Lora's two registers.
- The overhearing rendered only through Bal's senses.
- Amelia's grim "But it didn't get far."
- No nods, no em dashes, no spells.

## PATH TO 8.5
- **Characters 7.5 → 8.5 requires:** no gesture class at 3+ in 500 words, and no invented habit. Apply F1–F5, F7, F8 and F10. Each one cuts a look, face, blush or hand-hold beat or swaps it for a non-look verb. After them, the talk (L146–174) carries only the two source looks (L156 watched, L160 glance). L106–130 carries only the glares (L114) and "checked her front" (L128). The opening keeps only the map and the forest. Lora's invented habit is gone.
- **Prose 7.5 → 8.5 requires:** Pattern #11 at or under 2 instances (0.8/1k), and the #16 aside removed. Apply F1 ("It was all over her face"), F6, F8 ("He had believed…") and F9. That leaves 0 extensions. L164 then stands alone as the stopping sentence, which is where its force comes from.
- **Pacing 8.0 → 8.5 requires:** a clean close and no slip. F11 (end on "They did not talk.") and F12.

Projected after fixes: Originality 8.5, Theme 8.5, Characters 8.5, Prose 8.5, Pacing 8.5, Emotion 8.5, Engagement 8.5. **Floor 8.5 / Casual 8.5 → PASS.**

## VERDICT
**POLISH.** Genesis Floor 7.5, Average 8.1. Apply F1–F17 (cuts and swaps only, no plot), then re-gate. The book-level `tic_report.py --gate` FAIL ("his right hand", Ch.1/12/16) belongs to the parallel Ch.16 revision, not to Ch.17.

BIAS CHECK: This evaluation was produced by the same system that wrote the prose. Confidence in scores above 8.0 requires external validation (beta readers, editors, comp analysis).
