# Evaluation: Chapter 14 — The Card
**Evaluator:** book-evaluator | **Date:** 2026-10-20
**Text evaluated:** `manuscript/chapter-14.md` (2,611 words of prose per style_check; 2,713 with comments)
**Read first:** STATE.yaml (decisions), CLAUDE.md (canon guardrails), project/STYLE_CONSTRAINTS.md, character-bible.md, outline Ch.14, chapter-13.md (props), chapter-05.md (the first blood tear), chapter-07.md (pedestal), Sygl_Complete.txt L685–706, evaluations/chapter-13-eval.md.

## HEADLINE
**CVI-Launch:** 8.4 | **CVI-Legacy:** 6.2 | **Genesis Floor:** 7.5 | **Genesis Average:** 8.2
**Engagement Type:** Self-Insertion (primary) / Empathy (secondary) / Fascination (tertiary)
**Divergence Alert:** none (0.9 gap).

**VERDICT: POLISH.** The card scene is the best emotional peak in the book so far, and source fidelity is close to complete: every beat from L691 to L703 is here, in order, with the right speakers. The tone is light and warm, the register is American, the fade-to-black is clean, and Amelia's tear is real, not a ploy. Four mechanical or logic faults hold it under the gate:
1. **Gesture class over cap (Characters cap 7.5).** Sinking or settling back into the couch happens 4 times in 233 words (L60, L66, L70, L74) and 7 times in the chapter. Clutching something to the chest or in the arms happens 4 times (L104, L156, L160, L182), which reaches the chapter cap.
2. **Gate FAIL.** `tic_report.py --gate` flags "pleased with herself" (Ch.5, 13, 14). Ch.14 L24 is the third use.
3. **Logic.** Lora lectures for miles from the brown book she bought that afternoon, which has been riding in Bal's pack the whole time (L18).
4. **Grammar.** "Her fingers were knotted in her lap and was working at something" (L80). grammar_check missed it.

Every fix is a few words, and none adds plot. With F1–F8 applied the chapter projects to Floor 8.5, Casual 8.5: **PASS**.

## Gate tools (scratch copy, Ch.1–14 at `.../scratchpad/ev14/manuscript/chapters/`)
- `voice_wear_check.py`: **clean** (no retired phrases, no device over cap).
- `tic_report.py --gate`: **FAIL**. Recurring phrase "pleased with herself" ×3 [ch 5, 13, 14]. No Ch.14 entries in the gesture-class table (the classes found below are ones the tool does not classify).
- `style_check.py`: clean. Simile 2.3/1k, adverb 8.8/1k, **em-dash 0**, no distinctive repeated phrase.
- `grammar_check.py --file`: 0 errors. It missed L80 (see F4).

## Source fidelity (L691–703)
Every beat is present, in order. The walk with Bal listening; Lora's ancient-civilization book; Viridia genuinely engaged and "not just being polite"; about two hours; the door; two couches and a second table; the diary vanishing at the sight of Viridia; the hug; "gone all day. Did you have fun?"; the girls stalled by the door; Viridia dragging Lora in and introducing her; the raised eyebrow and the sheepish shrug; Amelia's laugh and "you know who I am"; Lora's energy gone; Bal sitting beside Amelia; "stay between us"; Amelia trying to speak and being stopped; the hand; the betrayal speech; the single blood tear wiped with his thumb; "She needs friends. So do I."; Lora opening and shutting her mouth; "I need friends too", said softly with eyes lowered; the alchemy book kept at the bottom; "They give gifts?"; "But when did you"; the unshed tears; the book hugged to her chest; the right pocket, left hand, closed eyes, middle finger, "oooh"; "doesn't look like much", "plenty powerful", the recharging; "It's perfect"; Amelia nervous; "sorry I didn't buy you anything" and the sad look he almost misses; the other pocket; "Turn it over"; turned to stone; sobbing and clutching; "You belong here, with us."; the girls staring; the kiss; "You are a good man"; scooting closer; the shirt that looks like an injury; "It was worth it"; the curfew bell; hugs and thanks; "It's time for bed"; boxers; the Vampire Goddess. Fade-to-black is respected.

Dialogue polish is natural and keeps meaning, speaker and placement ("I know it's something you want and have no idea how to ask for"). Small additions:
- Viridia's introduction line (the source says she "introduces her").
- Bal's "So you'll want to save it. For when it counts." (L122). It is consistent with the drawback, adds no information, and is acceptable.
- The reported banter about the dorm's "terrible taste" (L182). Light texture, no plot.

Props match Ch.13: the ring in the right pocket and the card in the other (left); six books and the collar in the pack, plus the job paper; the card's corner worn under his thumb on the road (Ch.13's last paragraph). Two continuity slips:
- **L192:** the card is propped on the nightstand "where the note he had left her that morning used to be". In Ch.13 the note was stood "up on the pillow beside her hand". F6.
- **L18:** the brown book. See Logic below. F3.

**The history-book contents (the judgment you asked for).** The source gives only "something to do with an ancient civilization". Putting words in Lora's mouth needs some content, and texture about a vanished people's roads, food, calendar, floods and earthquake is acceptable. It touches no god, sygl, magic rule or plot, and it dramatizes the source beat (Viridia "clearly interested and engaged").
- **Dead kept in the house walls: keep.** It is the chapter's opening hook. It produces the best exchange ("Did anybody ever knock back?"), and Lora turns it curious and warm ("It's not, though. Not to them."). Condition: it is never referenced or paid off again, so it cannot become lore.
- **The king who married his sister: cut** (L20, L24, L26). (a) It is the one detail that reads as plantable lore, because it lands minutes before a speech about Amelia's family betraying her, and in this world her family are the gods. A Hostile or Devoted reader will take it as a hint the source never makes. (b) Incest is the wrong note for the "lighter, warm" register. (c) The chapter needs neither. Swap in the floods it already has (F5).

**The tear vs Ch.5.** The trajectory is differentiated: in Ch.5 the tear runs down her cheek, smears, and he leaves his thumb unwiped; here it runs sideways toward her ear and is caught at the temple with the side of his thumb while his other hand stays on hers. The **staging** is a copy, though. Ch.5 L225: "Amelia leaned back against the stone wall of the cottage and let her eyes fall shut." Ch.14 L74: "Amelia had let her head tip back against the couch. Her eyes were shut." Head back, eyes shut, one blood tear, thumb: the same picture. The source here says only "Amelia had closed her eyes." Restaging it (F2) removes the echo and also removes one beat from the over-cap couch cluster.

## Genesis Score (Craft Assessment)

| Dimension | Score | Evidence | Cap Reasons |
|-----------|-------|----------|-------------|
| Originality | 8.5 | The card itself is the author's beat. What is fresh is the execution: the card handed over **face up** first, so "Turn it over" has a reason (L144–148); "as if the hearth had always had a statue of a girl beside it and nobody had noticed until now" (L152); the comedy flip from sobbing to "Anyone who came in now would have taken him for stabbed" (L176) | none (romance/commercial: a fresh take on a familiar beat) |
| Theme | 8.5 | Belonging, carried by objects (a team card, a surname, a ring, a book) and never stated. "She needs friends. So do I." / "I need friends too" (L78–82). Texture that is not theme: salt for the castle kitchen (L24), the puddle (L24), the dorm's couches (L34), poultices read aloud (L182). The sister-king is the only detail that echoes the theme too neatly (F5) | none |
| Characters | **7.5** (merit 8.5) | Cover-the-name passes. Viridia needles ("Did anybody ever knock back?"; "a look that promised trouble if this was a trick", L114; the dorm's "terrible taste", L182). Lora's fluent-to-mute switch is the source's own beat ("Oh," and nothing after it, L54; "She said it to her knees", L84). Amelia's nerves are new in the book and earned (L134). Bal's plain worldview: "wondered where the dorm got its couches" (L34). Chaos 3/4, inhabited: irrelevant thought (salt, L24); memory triggered by the scene and returning to it (the boys in Lora's town, L22); failed management (Amelia's freeze and sobbing). Lora's hands arriving "before the rest of her had caught on" (L100) gives her her own moment | **CAP 7.5, gesture class.** (a) Sinking/settling back into the couch: L60 "settled beside", L66 "sank against the cushions", L70 "Lora sank down onto the edge", L74 "head tip back against the couch". That is **4 in 233 words**, 7 in the chapter with L108, L128, L168. (b) Clutching to chest/arms: L104, L156, L160, L182 = 4, the chapter cap; L160 and L182 are not in the source. Tip/tilt is at 4 too (L74, L124, L128, L154; L124 and L128 are back to back). **Cadence watch:** Bal's "who does the work" thought appears twice in this chapter (salt carrier L24; "somebody somewhere had probably chosen that color" L34) after Ch.5, 7, 11, 13. Not capped, but cut one (F7). Fixes F1, F2 |
| Prose & Voice | 8.0 (merit 8.5) | Stopping sentence (warmth variant): L152, the statue at the hearth. Underlines: "Lora's hands came up for it before the rest of her had caught on." (L100); "She said it to her knees, so softly it nearly went into the fire." (L84); "scooted closer, until there was no couch left between them" (L168); "Bal decided the diary was a conversation for later, with fewer of its authors in the room." (L44). Ugly sentence: "and the red stain on his front got on neither of them because they were careful" (L186). Voice under pressure: at the card the prose drops to single-clause sentences (L150–154) | Gate FAIL on the third "pleased with herself" (L24). Grammar error at L80. Both are mechanical (F4, F8). #11 is at 2 (0.77/1k), just under the commercial cap |
| Pacing & Coherence | 8.0 | A quiet single scene, as designed, with a clear positive value shift: Lora mute → "I need friends too" → the book; Amelia nervous → "You belong here". Speed varies: talky road, a brisk arrival, a slow still card beat (L150–162), a quick light close. Dialogue about 14% (low for the romance lane; fine for a quiet scene). The chapter ends on warmth with the diary as the only open loop (L44). The outline's hook ("gone for the day") is rightly deferred to Ch.15's opening | Coherence: the brown book's contents (L18, F3); the note's location (L192, F6); "the girls had to run" (L184) followed by unhurried hugs at the bottom of the steps (F8) |
| Emotion | 8.5 | Anchor: the card turned over, and the statue stillness ("not her lashes and not her breath", L152). Surprise: the sob turns into the stabbing joke and "It was worth it" (L176–178). Body rebel: the tear, the shaking shoulders, Lora's "Oh" and nothing after. The peak is carried by objects (card, thumbs, white letters, shirt) with no intensity words. Investment is built by Lora's unshed tears first (L104), which are kept short | none |
| Engagement (Dim 7) | 8.5 | Self-insertion: you hand out three perfect gifts and the goddess cries into your shirt. Empathy: Amelia's nerves (L134) and Lora's "I need friends too" | none |
| **FLOOR** | **7.5** | | Characters (gesture-class cap) |
| **AVERAGE** | **8.2** | | Single-dimension bottleneck. Projects to 8.5 / 8.5 after F1–F8 |

Trajectory: Ch.1–12 are at 8.5. Ch.13's eval found the same failure (a gesture-class cap) and noted the "in the grain" conceit; Ch.14 uses "in the grain" once (L152), which is acceptable. **Pipeline fingerprint:** the gesture-class cap has now fired in two consecutive chapters. Have the writer self-check the "sit/settle/sink" and "hold to chest" classes before handing off, since tic_report does not classify them.

## CVI-Launch Breakdown
| Input | Score | Evidence |
|-------|-------|----------|
| Commercial Pacing | 7.5/10 | A short single scene with no cliffhanger; the bedtime ending is a natural stopping point |
| Tomorrow Test | 3 anchors → 9 | IMAGE: Amelia turned to stone over the card. IMAGE: the shirt soaked red, "taken him for stabbed". QUOTE: "You belong here. With us." |
| Casual Reader | 8.5/10 | Gift-giving scenes are pure pleasure, and the card lands even for a reader who skimmed Ch.13 |
| Shareability (quote/plot/emotional) | 3/2/4 → 7.2 | "I'm sorry about your shirt"; the surname on the card; "the card scene wrecked me" |
| Concept Pitch | partial (5) | Book-level, unchanged |
| Human Closeness | yes (10) | Wall-to-wall intimacy and friendship |

CVI-Launch = 1.5 + 1.8 + 1.7 + 1.44 + 0.5 + 1.0 = 7.94, +0.5 strong anchor = **8.4**.
CVI-Legacy = 8.5×.30 + 8.5×.25 + 3×.20 + 4×.15 + 3×.10 = **6.2**.

## Anti-AI Scan (20 patterns), 2,611 words
1. Forced symmetry: minor (1). "Lora into his collar and Viridia against his ear" (L186).
2. Empty poetic vocabulary: Clear.
3. Rule of three: moderate (2; 0.77/1k). "where they had built their roads and what they had eaten and how they had counted their years" (L18); "The fire went on popping. Lora breathed. Viridia's ring caught the light and lost it." (L152). The second earns its place.
4. Em dashes: Clear (0).
5. Empty metaphors: Clear.
6. Dramatic "And" openings: Clear. "And you know what friends do?" is source dialogue.
7. Pseudo-philosophical closings: minor (1). "They knew enough." (L160). Acceptable.
8. Excessive parallelism: Clear. "Somebody's boy… Somebody with a cart…" is voice.
9. Smooth transitions: Clear.
10. Described emotions: minor (1). "Bal realized she was nervous" (L134, from the source).
11. Explanatory extension: moderate (2; 0.77/1k, under the commercial 0.8 cap). "Nobody was being polite. The difference was easy to hear." (L20); "because they were careful" (L186). F8 cuts both.
12. Binary negation opener: Clear.
13. Precision flex: Clear. The numbers come from the source or from Ch.13's props.
14. Emotional control demonstration: Clear ("Nothing spilled" is the source's unshed tears).
15. Authoritative description: Clear. Bal guesses about the couches.
16. Philosophical asides: Clear.
17. Clean dialogue: Clear. Lora's "Oh," and nothing; "But when did you..." breaks off.
18. Thematic echo chamber: Clear (salt, puddle, poultices). The sister-king is the one echo (F5).
19. Graduated reveal: Clear.
20. Temperature report: Clear.
**Total 6/20, all minor or moderate.** Clean for the commercial lane (0–8).

## Character Chaos Check (Bal)
- Irrelevant thought: **present**. The salt (L24); the couches (L34). Keep one (F7).
- Cognitive distortion: absent (fine for the lane).
- Unprompted memory: **present**. The boys at the tournament (L22) are triggered by Lora walking backward and return to her.
- Failed emotional management: present in others (Amelia, Lora). Bal stays steady, which is right for the scene.
- Voice under pressure: demonstrated lightly at the card (L150–162).

## Secondary Character Chaos
- Amelia: has her own moment. Nervous for the first time on the page (L134), the diary panic (L38–40).
- Lora: her own moment. Lecturing fluently, then mute (L6–26, L54).
- Viridia: her own moment. The puddle (L24), "a look that promised trouble" (L114), the ring trance (L128).

## The Tomorrow Test
**What the reader remembers:** Amelia turning the card over and going still as a statue; the red-soaked shirt and "It was worth it."
**Anchor type:** BOTH (image + "You belong here. With us.")
**Verdict:** ANCHOR EXISTS. It differs in type from Ch.13 (the lettering): this one is a reaction, not an object being made.

## Shareability
"He made her a guild card with his last name on it and she cried blood all over his shirt." Strong.

## Reader Reports
- **Devourer:** Reads straight through; the gifts are a three-step escalation and the card is the payoff. Will close the book at bedtime because the chapter does too. The diary thread (L44) is the only pull forward.
- **Critic:** Underlines L100, L84, L152, L168. Disappointed by the doubled settle-into-the-couch beats (L60–74) and the second tilt of the ring (L124/L128). Notices that the tear's staging repeats Ch.5.
- **Hostile:** "When did Lora read the brown book? Bal's been carrying it since the shop" (L18). "The note was on the pillow" (L192). "The girls 'had to run', then stand around hugging" (L184–186). "Her fingers ... and was working" (L80). Raises an eyebrow at the incest king next to a family-betrayal speech.
- **Casual:** Loves it. Warm, funny (the puddle, "stabbed"), and the card scene hits. Would buy. 8.5.

## Cross-Reader Matrix
| Issue | Devourer | Critic | Hostile | Casual | Severity |
|-------|----------|--------|---------|--------|----------|
| Couch/chest gesture clusters | | ✓ | ✓ | | SHOULD FIX (mechanical cap → blocking) |
| Brown-book logic, note location | | | ✓ | | INVESTIGATE (cheap; fix) |
| Ch.5 tear staging echo | | ✓ | ✓ | | SHOULD FIX |
| Sister-king lore | | ✓ | ✓ | | SHOULD FIX |
| "pleased with herself" ×3 | | ✓ | | | Gate FAIL → blocking |
| Soft ending hook | ✓ | | | | INVESTIGATE (by design) |

## Revision Recommendations (Ranked). Surgical, no new plot

| # | Location | Problem type | What happens now | Why it fails | Revision direction | Project rule? |
|---|----------|-------------|------------------|-------------|-------------------|---------------|
| F1 | L60, L70, L108, L128, L124, L160, L182 | Character (gesture class) | Settle/sink into the couch ×7 (4 in 233 words); clutch-to-chest ×4; tip/tilt ×4 | Over the gesture-class cap → Characters 7.5 | L60 "Bal went and settled beside Amelia." → "Bal sat down beside Amelia." · L70 "Lora sank down onto the edge of the new couch." → "Lora sat on the edge of the new couch." · L108 "She settled into the cushions with it held there, watching him" → "She stayed like that, watching him" · **cut L124** ("Viridia tipped her hand one way and the other.") · L128 "She leaned into the cushions next to Lora and tilted" → "She tilted" · L160 cut "Lora had both arms wrapped around her present, and" (start the sentence at "Viridia's hand…") · L182 cut "The alchemy book never left Lora's arms." Keep L66 and L168 (source) | Yes: writer self-checks sit/settle and hold-to-chest classes |
| F2 | L74–76 | Character / Style | "Amelia had let her head tip back against the couch. Her eyes were shut. One tear got out. With her head back it did not run down her cheek. It ran sideways…" | Same staging as Ch.5 L225/233 (head back, eyes shut, tear, thumb); also part of the couch cluster | → "Amelia had closed her eyes. One tear got out and hung on her lashes, red in the firelight, and Bal took it off with the side of his thumb before it could fall. His other hand stayed on hers." (This is the source's line, with a new trajectory: caught at the lashes, no smear, no cheek.) | No |
| F3 | L18 | Logic | "The book was the brown one with the broken column on the cover, the one riding in his pack with everything else." | She bought it that afternoon and has not had it in hand since, yet she knows it cover to cover | → "It was the book she was partway through back at school, not the new brown one riding in his pack." (The source says "the book she was currently reading.") | No |
| F4 | L80 | Style (grammar) | "Her fingers were knotted in her lap and was working at something" | Subject–verb break | → "Her fingers were knotted in her lap, and she was working at something" | No |
| F5 | L20, L24, L26 | Exposition / canon (invented lore) | "a king who married his own sister deserved whatever had happened to his city"; "the earthquake or the king"; "one more thing about the king's sister" | Reads as plantable lore beside Amelia's family-betrayal speech; wrong tone for the warm register | L20 → "to argue that anybody who built a city on a floodplain deserved what they got." · L24 → "which came first, the earthquake or the floods" · L26 → "one more thing about the floods". Keep the dead in the walls (texture, never to recur) | Yes: book-in-book contents stay generic and never recur |
| F6 | L192 | Continuity | "where the note he had left her that morning used to be" | Ch.13: the note stood "on the pillow beside her hand" | → "propped against the lamp with the name facing her, and his note from that morning folded beside it." | No |
| F7 | L34 | Character (cadence watch) | "Still, somebody somewhere had probably chosen that color." | Second "who does the work" thought in one chapter (salt at L24), after Ch.5, 7, 11, 13 | Cut the sentence; keep the salt | Yes: one "who does the work" thought per chapter, max |
| F8 | L24, L20, L184, L186, L196 | Style | "Viridia looked so pleased with herself that she walked into a puddle"; "The difference was easy to hear."; "the girls had to run"; "because they were careful"; "this time the pink was all his" | tic_report gate FAIL (3rd use book-wide); #11 tails; pace contradiction; ambiguous joke (pink boxers?) | L24 → "Viridia was so busy being right that she walked into a puddle." · L20 cut "The difference was easy to hear." · L184 "had to run" → "had to go" · L186 cut "because they were careful" · L196 → "and this time he was the one going pink." | No |

### Fix order: F3, F6 (logic/continuity) → F1, F2, F7 (character) → F5 → F4, F8 (prose)

## Strengths to PRESERVE
- The card handed over face up first (L144), so "Turn it over" carries weight.
- L152: the statue at the hearth, "not her lashes and not her breath", and *Amelia Norheart* under her thumbs.
- The sob-to-joke turn, "taken him for stabbed" / "It was worth it" (L176–178).
- Amelia's first visible nerves (L134). Lora "said it to her knees" (L84). Hands "before the rest of her had caught on" (L100).
- The opening exchange about the dead in the walls and knocking (L6–14).
- Zero em dashes; the American register throughout.

## PATH TO 8.5
- **Characters 7.5 → 8.5:** apply F1 and F2. That leaves settle/sink at 2 (L66, L168, both source), clutch-to-chest at 2 (L104, L156, both source), tip/tilt at 2. Recount before handoff: no class may have 3 in any 500-word window or 4 in the chapter. F7 keeps the irrelevant-thought device off a cadence.
- **Prose 8.0 → 8.5:** F8 (L24) clears the tic_report gate; F4 fixes L80. The merit is already 8.5 (L152 is the stopping sentence).
- **Pacing & Coherence 8.0 → 8.5:** F3 and F6 close the two holes a Hostile reader will find; L184 "had to go". Do not add a hook; the morning departure belongs to Ch.15's opening.
- After the fixes: re-run `tic_report.py --gate` (expect PASS) and recount the windows. No full re-score is needed.

## VERDICT
**POLISH.** Genesis Floor 7.5 (Characters, gesture-class cap); Average 8.2; Casual 8.5. Apply F1–F8 and the chapter projects to **PASS at Floor 8.5**.

BIAS CHECK: This evaluation was produced by the same system that wrote the prose. Confidence in scores above 8.0 requires external validation (beta readers, editors, comp analysis).

## Revision applied (2026-10-20, book-editor)
- **F1** gestures: L60 "sat down beside"; L70 "had ended up on the edge"; L108 "She stayed like that"; L124 cut; L128 "She tilted"; L160 clause and L182 alchemy-book line cut. Further sit/settle cuts: Amelia's "sat as if", "sat up straighter", "sat holding the card", "She sat up" (→ "She drew back"), "histories sat". Viridia's "shut her eyes"/"opened her eyes" and Amelia's "looked from Lora to Bal" removed (eyes/look windows). Recount: no class at 3+ in any 500-word window.
- **F2** tear: "Amelia had closed her eyes." Tear hangs on her lashes, brushed away with the side of his thumb.
- **F3** Lora talks from the book she's partway through at school. **F4** L80 fixed. **F5** sister-king gone (floodplain / floods / earthquake); dead in the walls kept. **F6** note folded beside the card. **F7** couch-color line cut. **F8** all five applied ("so busy being right"; "had to go"; stain line recast; "now his own face went pink").
- New phrasings varied until clean: style_check, grammar_check (ch.1–15) clean; voice_wear_check and tic_report --gate (ch.1–14 scratch copy) clean. Em-dashes 0; "the way" 0.
