# Evaluation: Chapter 14 — What Pompeii Means (run 2)
**Evaluator:** book-evaluator (independent; did not write or revise this prose) | **Date:** 2026-10-20
**Text evaluated:** `manuscript/chapters/chapter-14.md` (sha256 `df561f3a…`), after writer → dialogue-polish → hook-craft → disruptor → continuity repair (C-01, W-01…W-13). **3,022 prose words** (shape_check), 3,028 (style_check), 3,372 (`wc -w`, with the header).
**Read against:**
- the book's CLAUDE.md hard gates;
- STATE.yaml: guardrails (NO FORESHADOWING, NO TICS incl. gestures, the retired reflexes), resolved_author_decisions, AUTHOR-CP2-1…4;
- voice-dna §0 (stance; "Ch.14: the night she knows"), §1, §3b, §4, §6;
- character-bible.md: the Mara, Valens, Kallia and Theano cards, and every at-risk / spent block from "after Ch.1" to "after Ch.14";
- outline Ledger row 14 and `## Chapter 14`;
- `evaluations/chapter-13-eval.md` (cycle 0, cycle 1, finalize);
- chapters 12 and 13 in full for pacing and reuse; Ch.2 (the Halloran call) and Ch.3 (the sherds) for memory shapes;
- `evaluations/continuity/chapter-14-audit.md`;
- voice-bank samples 01–13 by 3-gram.

**Genre profile:** commercial historical romance / time-slip, comp *Outlander*. Anti-AI band: commercial (0–8 clean, 9–11 watch). Engagement: empathy 55 / fascination 30 / self-insertion 15. Dimension 7 = **IMMERSION**.

**Measured here.** `bash books/the-hour-of-ash/tools/check_chapter.sh 14` is **clean on every gate**: style (simile 0.3/1k, em-dash 0, foreshadow 0); grammar 0; rhythm 0; show/tell no flags (dialogue 4.8%); voice-wear strict clean; tic gate clean (and-chains 1/9, credential asides 0, negation pivots 0, "So" 0); echo 0; command echo none; metaphor fig 0.3/1k, median 12; `shape_check`: `14 3022 9 5 12 I-punch long-fade`, CLEAN.

**My own scans (scratch, not gates):** 4-grams against Ch.1–13 and 3-grams against all 13 samples; a hand count of #11 explanatory extensions, paragraph-final negations, shard openers and shard closers; every SPENT / CLOSED item in the bible grepped by frame as well as by string; Ch.2, Ch.3 and Ch.13 memory shapes compared with Ch.14's.

**The fix set was applied together to a scratch copy, swapped into the manuscript path, run through the real `check_chapter.sh 14`, `shape_check --strict`, `voice_wear_check.py` and `tic_report.py --gate` from /home/user/Books, and the original was then restored (sha256 `df561f3a…` verified after every run).** I did not edit the manuscript.

*(l.N = line number in the current `chapter-14.md`.)*

---

## HEADLINE
**CVI-Launch (CVI-L):** 8.9 (8.45 base + 0.5 strong anchor) | **CVI-Legacy:** 6.9 (provisional) | **Genesis Floor:** **7.5** | **Genesis Average:** **8.71**
**Casual Reader:** **9.0**
**Engagement type:** Empathy leads (a woman alone with the one fact nobody around her can be told), with Fascination second (Pliny "a boy of nine now"; the dog going past the door). Self-insertion is tertiary: the reader holds the date with her.
**Divergence alert:** none (8.9 − 7.5 = 1.4).

**Gate (Floor ≥ 8.5 AND Casual ≥ 8.5 AND pacing OK AND gates clean): NOT MET.** Casual 9.0 ✓, pacing OK ✓, gates clean ✓. **One dimension holds the floor, by a cap:**
- **Prose & Voice 7.5: #11 explanatory extension is over the commercial density cap** (4 instances at 1.32/1k against >0.8/1k; in a 3k chapter the cap is reached at 3). On merit Prose is **8.0**, held there by narrator frames the gates cannot see: a fourth use of the SPENT "Whoever [made] it had" frame, the SPENT "took in my [X]" two-item look, a SPENT gaze-arrival "then", a call-out pointer opening a shard, a Ch.13 line paraphrased, six turned shard-closers in nine, a soft anaphora triad, and three in-chapter or cross-chapter doubles.

**Every fix is a swap or a clause cut; 23 strings, tested together:** 3,007 words (shape_check; ≥3,000 ✓), dialogue 5%, median 12, 9 breaks, `I-punch` → `long-fade`, all gates clean, echo 0, the first sentence and the last paragraph byte-identical.

---

## Genesis Score (Craft Assessment)

| Dimension | Score | Evidence | Cap reasons / holds |
|---|---|---|---|
| Originality | 9.0 | **The outline's subversion is on the page:** the dawning is instant, total and private ("I knew the year. … it came whole.", l.6), and the response is a laugh. **The writer's inventions on top of it:** (1) the jar held under the spout until it overflows down her sleeves and ribs, "I kept on holding it." (l.10); (2) the town known only from above: "**What anybody in that town called a single street was beyond me.**" (l.30), and the tombs that give her "only the benches" (l.32); (3) the casts reached through Kallia's plaster, the fur-hat woman who "had thought they would be bigger", the pretzel "as far as Trenton" (l.38–l.40); (4) **"He was a boy of nine now, somewhere in the north of Italy, at his lessons."** (l.46), the time-slip vertigo done in one clause; (5) the door that may stand open "tonight … with nothing going past it but a dog" (l.50); (6) the joke: Halloran's room refused, "and found me a place in Campania after all. He had outranked Halloran." (l.60); (7) the laugh covered with another woman's well (l.76) and "She'll dig it crooked." (l.80); (8) "**To everybody under that roof it was a town in Italy where they made fish sauce.**" (l.86); (9) the plan built on Saint Paul's grain ship and Euthydikos's bowl; "**I left him out of the plan. He kept being in it.**" (l.122). | **≥9.0 challenge:** would a senior editor set the night beside *Outlander*'s quiet chapters of Claire alone with what she knows (the Culloden knowledge)? Yes, and this one refuses the confidant scene the genre expects. **Not 9.5:** the laugh's trigger runs through Halloran again (Ch.2's laugh was Halloran too; W-09 varied its shape, not its source), and the casts memory is a parent-shows-child-antiquity frame one chapter after the slides. |
| Theme | 9.0 | "Home behind a door in a city she knows will die" is carried by acts and texture, never stated. **Acts:** the word kept "behind my teeth" a yard from the man who carried it out (l.74); the hand over his shoulder drawn in (l.84); the plan that "left him there" and "had no boy in it" (l.124); "A year to get there. Seven, after that, to watch a door in." (l.128). **Texture that means nothing:** the Thessalian talking in his sleep, "a long grievance with a girl's name in the middle of it" (l.26); the ram's boy sick into the drain, "He ate the fat off the god's share. His own and his brothers'," (l.100); the burn on Kallia's blanket (l.112). The father carrying his sick son back to the cloaks (l.102) rhymes with family without a word pointing at it. | **≥9.0:** the theme is a question the plan answers wrongly on purpose ("Eight years was plenty of time, I told myself.", l.124). No echo chamber. **Not 9.5:** "It was more time than I had been given for anything in my life." (l.128) edges toward stating the cost. |
| Characters | 8.5 | **Mara: chaos 4/4, inhabited** (below). **Valens** in one exchange: up on one elbow "in silence", the knife "lying back along his forearm" (l.66–l.68), "Was that you?", then the practical deadpan of his card: "The moon's down by midnight," … "She'll dig it crooked." (l.80); "half a step behind" on the house side (l.18). **Kallia:** laid his blanket "crosswise on the threshold … herself" (l.26), salt water for a stranger's child at midnight, "It isn't their knees." (l.110), her own burned blanket over his feet (l.112), folded in four by morning (l.146). **Theano:** lets the crow stay (l.6). **Walk-ons:** the woman with the jug, "not only Syracuse" (l.10); the Thessalian father: "From Larisa it never wanted to come. Every mile, it told us." (l.98). Cover-the-name PASS for all four speakers. | **No cap.** Verbal tics 0; gate gesture classes clean; deliberation pause 0; kneel/crouch 0; hand-on-knee 0; gait exits 0 ✓ (the bible's Ch.14 bar). **WATCH:** Kallia hands Mara an object twice (bread l.20, lamp l.94). **Not 9.0:** Valens's stage business carries two SPENT narrator frames (l.18, l.72; scored under Prose), and the low-dialogue design gives the cast one exchange each. |
| **Prose & Voice** | **7.5** | **Stopping sentence:** "**He was a boy of nine now, somewhere in the north of Italy, at his lessons.**" (l.46). **Underlines:** "What anybody in that town called a single street was beyond me." (l.30); "a woman in a fur hat told her husband she had thought they would be bigger" (l.38); "I ate half of it and carried the other half in its paper as far as Trenton." (l.40); "It stopped some while after the funny part had gone out of it." (l.62); "he had no more idea what it was than the cat on Theano's hearth" (l.74); "and he slept on, or let me think he did." (l.92); "I left him out of the plan. He kept being in it." (l.122); "a town I had never stood in and could have drawn blindfold" (l.126). **Ugly sentence:** "The jar was heavy and I got it up there and she said nothing of it at all." (l.10). **Voice under pressure:** low gear (median 12); the asides die at the fountain and the knife and come back, dry, inside the plan; the body takes over at the jar, the laugh and the fingers that return to the plaster (l.42). | **CAPPED at 7.5: #11 over the commercial cap** (4 at 1.32/1k; list in the scan). **Without the cap it holds at 8.0** for the law items under "The book's own laws" (P1–P11, C1–C4): the "Whoever" frame, "took in … my wet front", "His head came round then", the "'Tomorrow,' I had said" pointer, "see it shut" from Ch.13, six shard kickers, the soft triad, the cat and the September father reused, "asleep across" twice, sample-12's "across the threshold". Anti-AI 9/20, −1.875 (watch band). |
| Pacing | 9.0 | **The ledger row is hit on every hard field:** Fragmented (*one night in shards*) between Ch.13's Parallel and Ch.15's Chronological ✓; open `I-punch`, "I knew the year." (4 words) ✓; close `long-fade` (the cliffs, 49 words) ✓; 9 breaks ✓; dialogue 5% (0–10) ✓; gear low, median 12 ✓; 3,022 against 3,400 (range 3,000–3,800) ✓. **Speed design:** S1 short and physical; S2–S4 dense knowledge; S5 accelerates into the laugh; S6 the knife spikes it; S7 a human interlude in the court; S8 the plan lengthens the sentences (resolve, not panic); S9 short; S10 the fade. **Value shift:** + (the WHERE) → − (what it means) → − (alone with it, the hand drawn back) → + (a plan; the cave errand; Valens gone for the mules unasked). | **≥9.0:** a 3k low-gear night that a reader takes in one sitting after 7.5k of ritual, with two jolts in the middle. **Not 9.5:** the tombs paragraph (l.32) and the Saint Paul paragraph (l.126) are the slow spots, and S8 sits at the top of the gear. |
| Emotion | 9.0 | **Anchor lands** as planned ("held in her head like a stone in her mouth"): "It had been there all evening, the word, behind my teeth" (l.74), then the substitute story, then "I said the word once with no sound in it, toward the jars. To everybody under that roof it was a town in Italy where they made fish sauce." (l.86). **Surprise:** the laugh, loud, "with a squeak in the top of it that I had never heard myself make. My eyes stayed dry." (l.62). **Body rebel:** the hands that keep holding the jar (l.10); the laugh that "came round the sides anyway" (l.62); the fingers "back on the patch by the jamb" (l.42). **Techniques ≥5:** physical sensation, humor in dread, dramatic irony (Pliny now nine; "It was a good plan."), object proxy (the pretzel; the blanket folded in four), concealment and silence. The reader cares before the peak: Ch.13 put the word in her hands. | **≥9.0:** the private-knowledge chapter the genre usually hands to a confidant is carried by a jar, a laugh and a withheld hand. **Not 9.5:** the laugh is the fifth Mara laugh-as-peak in the book (Ch.2, 6, 7, 8, 14); it is mandated and its shape is new, but the channel is familiar. |
| **Immersion** (Dim 7) | 9.0 | Period: the lion-head street fountain "with moss under its lip"; the head-load on a rag ring; sacrifice meat in cabbage leaves (W-13 fixed); mud brick under lime plaster with a straw standing out of it; the drain, salt water as an emetic, the god's mutton; the gate bar; Kirrha shipping, the sailing season, the Alexandrian grain ship to Puteoli. 1998 knowledge used, not lectured: Fiorelli's numbers, the Faun and the Tragic Poet, the bench tombs at the Herculaneum gate, Pliny *Ep.* 6.16/6.20 (the stones "on the far shore", W-07 fixed). | **Held at 9.0.** #15 minor: the sailing-season and Saint Paul sentences are encyclopedic (offset by "beyond me" and "got only the benches"). |
| **FLOOR** | **7.5** | Prose & Voice (capped) | |
| **AVERAGE** | **8.71** | (9.0 + 9.0 + 8.5 + 7.5 + 9.0 + 9.0 + 9.0) / 7 = 61.0 / 7 | |

**Trajectory vs Ch.1–13** (finals 8.50–8.79; cycle 0s 7.5–8.0): the fourteenth cycle 0 held by narrator recurrence, and the fourth held by the #11 cap (Ch.10, 12, 13, 14). As in Ch.13, part of the excess arrived through the chain: the continuity repair's W-08 gloss ("every other piece of the day from me over supper") is one of the four.

---

## CVI-Launch Breakdown
| Input | Score | Evidence |
|---|---|---|
| Commercial Pacing | 8/10 | Short, two jolts (the laugh, the knife), a plan that pulls; loses 2 for 5% dialogue and two history paragraphs a page-turner skims. |
| Tomorrow Test | 6 anchors → 10 | IMAGE: the jar overflowing down her sleeves; the pretzel carried to Trenton; the dog cast; the hand hanging over his shoulder; Kallia's blanket folded in four. QUOTE: "a town in Italy where they made fish sauce"; "He was a boy of nine now". |
| Casual Reader | 9.0/10 | See report. |
| Shareability (quote / plot / emotional) | 4 / 3 / 4 → 8 / 6 / 8 → **7.73** | Quote: "To everybody under that roof it was a town in Italy where they made fish sauce." Plot: "she knows exactly when Pompeii dies and decides to go there anyway." Emotional: "she laughs so hard she squeaks, alone, a yard from the man she can't tell." MAX 8 × .6 + AVG 7.33 × .4. |
| Concept Pitch | yes → 10 | |
| Human Closeness | partial → 5 | The night is solitary by design; Valens across the door and Kallia's midnight care carry the closeness. |
| **CVI-Launch** | **8.45 + 0.5 = 8.9** | 8 × .2 + 10 × .2 + 9 × .2 + 7.73 × .2 + 10 × .1 + 5 × .1 = 8.45. One-chapter formula; see BIAS CHECK. |

**CVI-L note.** In this project "CVI-L" means **CVI-Launch: 8.9**, down from Ch.13's 9.8 (the book's high, with Ch.8) and above every Part One quiet chapter's band. That drop is the design working, not a weakness: Ch.13 is the reveal, Ch.14 the pressure chapter that turns it into dread and resolve, with no event, 5% dialogue and a solitary frame. It holds near 9 on anchors and the fish-sauce line. The PATH moves no anchor, so **CVI-L is unchanged after polish (8.9).** Running CVI-L Ch.11–14: 9.5 / 9.7 / 9.8 / 8.9, which is the right shape for a turn followed by a breath before Ch.15's romance turn.

**CVI-Legacy (default weights; provisional):** Originality 9.0 × .30 + Theme 9.0 × .25 + Cultural Vocabulary 2 × .20 + Re-readability 7 × .15 + Identity 5 × .10 = **6.9** (Ch.13 6.8). Re-read rewards: "It was a good plan." (l.130); the dog past the door after the dog cast (l.38, l.50); "Whoever took me to that town, the plan left him there." (l.124); "years ahead of the mountain" (l.126); "He's gone down for the mules" (l.148) answering a plan that left him out.

---

## Anti-AI Scan (20 patterns; density per 1,000 words at 3.02k; commercial band)
| # | Pattern | Result | Count / density | Citation |
|---|---|---|---|---|
| 1 | Forced symmetry | FOUND moderate | 2 (0.66) | l.140 "Either the cave was shut, or it was open."; l.126 "The sailing season closed with the autumn and opened with the spring." ("I left him out of the plan. He kept being in it." is designed and not counted.) **−0.25** |
| 2 | Empty poetic vocabulary | Clear | 0 | |
| 3 | Automatic rule of three | FOUND moderate | 2 (0.66) | l.122 "A ship's master at Kirrha would want the same, and a landlord in Italy, and any magistrate."; l.26 "Kallia's oil jars stood round my mat, and the barley sack, and the smell of both." ("regions and blocks and doors" is Fiorelli's real system; not counted.) **−0.25** |
| 4 | Em dashes | Clear | 0 | |
| 5 | Empty metaphors | Clear | 0 | One comparison (the cat, l.74), characterizing. |
| 6 | Dramatic "And" openings | FOUND minor | 1 (0.33) | l.60 "And the god of Greece had heard my question out". **−0.125** |
| 7 | Pseudo-philosophical closings | Clear | — | The chapter ends on the cliffs and the empty path; no shard ends on a generalization. |
| 8 | Excessive parallelism | FOUND moderate | 3 (0.99) | Doubled pick-ups: l.28 "I had the town. I had it from above"; l.74 "It was there. It had been there"; l.10 "I held the jar … I kept on holding it" (the designed one). Anadiplosis l.124 "if it was Italy. It was Italy." (1, at the ≤1 cap). **−0.25** |
| 9 | Overly smooth transitions | FOUND minor | — | Shard openers as a time ladder: l.90 "Some hours on," / l.118 "In the middle of the night" (adjacent) / l.144 "Long before the gray". **−0.125** |
| 10 | Described emotions | Clear | 0 | No named feeling; "My eyes stayed dry." is the body. |
| 11 | **Explanatory extension** | **FOUND strong, OVER THE CAP** | **4 (1.32/1k)** | (1) l.28 "numbered every one, **to find his way about in it**"; (2) l.54 "a room with a window in it, **so that somebody would see the place**"; (3) l.122 "A husband, a brother or an owner: **somebody whose name went down first**"; (4) l.106 "**Kallia had had every other piece of the day from me over supper.**" (repair-added, W-08: a gloss explaining her question, and a seam with l.20 "Kallia asked me nothing."). Not counted (borderline, kept): l.84 "and none of it would be the question"; l.10 "She was indoors already."; l.60 "He had outranked Halloran. He had picked the town." (the joke itself). **−0.50 and Prose capped at 7.5.** |
| 12 | Binary negation opener | Clear | 0 | |
| 13 | Precision flex | FOUND minor | — | The arithmetic is the chapter's subject ("eight years and a little over", "ten or eleven years", "A year … Seven"); incidental: "folded in four", "most of an hour". **−0.125** |
| 14 | Emotional control demonstration | Clear | — | Control fails (the jar, the laugh, the fingers); "I drew the hand in." is a choice, not a management beat. |
| 15 | Authoritative description | FOUND minor | — | l.126 the sailing season and Paul's ship; l.28 the plan. Offsets: "beyond me", "got only the benches", "a town I had never stood in". **−0.125** |
| 16 | Philosophical asides | FOUND minor | 1 (0.33) | l.124 "Men went where the work was." (framed by "I told myself", so it is her rationalization, not the narrator's maxim). **−0.125** |
| 17 | Clean dialogue | Clear | — | "Was that you?" is answered with a substitute story; Kallia and the father talk across the boy's back. |
| 18 | Thematic echo chamber | Clear | — | Texture present (see Theme). |
| 19 | Graduated reveal | Clear | — | Fragmented. |
| 20 | Emotional temperature report | Clear | — | No periodic body check-ins. |

**9 / 20 found (#1, #3, #6, #8, #9, #11, #13, #15, #16). Total −1.875. Band: WATCH** (commercial 9–11). **#11 hard check: FAIL** (1.32/1k > 0.8). **After the PATH:** #11 has no firm instance (the three borderline clauses stay); #1 drops to 1 (minor); #9 clears (the adjacent time openers are split); #8 drops to 2 → **7/20, −1.125, clean band.**

---

## The book's own laws
- **NO FORESHADOWING: PASS, 0.** The gate agrees. By hand, families A–E:
  - Every forward line is an intention, a plan or a conditional: "Eight years was plenty of time, I told myself." (l.124); "years ahead of the mountain" (l.126); "I could stop listening for the other" (l.138); "It was a good plan." (l.130). **She never narrates her own outcome.**
  - AD 79 as present thought, Ch.14's allowance (voice-dna §0.3): the year and month only ("Seventy-nine, late in the summer, in August."); the day stays for Ch.36. The letters' facts are memory of a text (l.46).
  - Family E: the casts are a 1979 memory in Part One ✓; the mender's trade is not linked to the ash ("so the join never showed" is about lamps and bronze) ✓. The dog past the door (l.50) after the dog cast (l.38) is a rhyme her own mind makes; nothing points at it ✓.
  - The mountain rule: "The mountain with the vines on it was that mountain." No descriptor, no personification ✓.
- **Memory only when the scene triggers it (CP2-2): PASS, with a WATCH.**
  - The casts: triggered by Kallia's plaster under her fingers (l.36), and returned to it ("Kallia's plaster was cold.", l.42) ✓. It closes on an object (the pretzel), not a lost name ✓.
  - Halloran and the father (l.54–l.58): triggered by her own chain of thought (the letters → the bay → Neapolis), returned to the court by the laugh ✓.
  - **Conflict on file:** the bible's Ch.13 block says the next longer memory "waits at least one chapter". The outline (beat 1) and voice-dna §0.3 mandate the casts in Ch.14, and the contract wins. **Ch.15 and Ch.16 carry no longer memory.**
  - **Memory shapes:** the father coming home *in September* is now Ch.3 (the sherds), Ch.13 (the slides, "one September night") and Ch.14 (l.58): a third use of one frame → **P10**. And "a parent shows the child antiquity in a dim room" runs Ch.13 → Ch.14 (slides, then casts): different acts, but the next memory must not involve a parent.
- **Explanation-density cap: FAIL** (#11, 4 at 1.32/1k) → 0 firm after the PATH.
- **Paragraph-final negations ≤1.5/1k: PASS.** 4 in narration (1.32/1k): l.50 "nothing going past it but a dog"; l.74 "no more idea … than the cat"; l.136 "no sea in the way, and no town"; l.150 "nobody on it yet". The PATH adds none (re-counted on the fixed copy: 4).
- **NO TICS, verbal: PASS.** No catchphrase. "the word" as the stand-in for the city runs 3 (l.6, l.74, l.86) → P8 makes it 2.
- **NO TICS, gestures the gate cannot classify:**
  - **"took in" + a two-item look** (l.18 "He took in the crows' house above us, and my wet front."): "took in my [X]" is SPENT (after Ch.6) and the item-by-item look is CLOSED; Ch.13 l.400 has "He took in Valens on the stool and Kallia at the jar" one chapter back → **C1**.
  - **Gaze-arrival "then"** (l.72 "His head came round then, and he found where I lay."): the "looked at me then / her eyes came round to me" family is SPENT → **C2**.
  - **Valens's breathing told twice** (l.26 "slow and even"; l.82 "His breathing evened.") → **C3**.
  - **"asleep across [the] door"** twice (l.24, l.122), the second a near-echo of Valens's own Ch.12 line "I slept across her door" (SPENT for Ch.22). Keep the first as the one rhyme → **C4**.
  - Kallia hands Mara an object twice (l.20, l.94): WATCH, not a cap.
  - Stepping over a sleeper (l.92, l.114): twice by design; SPENT after this chapter.
- **The reflexes fragmented chapters breed:**
  - **Anaphora triads:** l.6 "The mountain … was that mountain. The sea to the west was the bay under it. The dead of that town…": three sentences opening "The [noun]" in a decoding run (the third varied). The outline's writer warning names this reflex → **P6**.
  - **Shard-closing kickers: 6 of 9 internal shards end on a turned line** (S2 "and got only the benches."; S4 "…but a dog."; S5 "after the funny part had gone out of it."; S6 the fish sauce; S8 "and it held."; S9 "find out which."). The disruptor's own ceiling was "one kicker per shard … about the most before it reads as a device"; six reads as the device → **P4, P5** take S8 and S9 to plain acts; the four strongest stay (4 of 9).
  - **Aphorisms:** none at a close ✓.
  - **Repeated shard openings:** a time ladder, two adjacent (l.90 "Some hours on," / l.118 "In the middle of the night") → **P11**. No two shards open on the same word otherwise.
  - **Memory shapes:** see P10 above.
- **No reuse of earlier chapters' phrases or set pieces:**
  - **"Whoever plastered it had not troubled to finish it smooth." (l.36): the "Whoever [made] it had" frame is SPENT at 3 (Ch.6 ×2, Ch.8 draft; "No fourth, in any verb")**, and it is an absent-workman verdict besides → **P1**.
  - **"'Tomorrow,' I had said, about the cave." (l.134)** quotes her Ch.13 line to open a shard: a narrator call-out pointer (bible: treat as 0) → **P2**.
  - **"see it shut with my own eyes" (l.138)** paraphrases Ch.13 l.360 "I want to see it shut for myself." ("see it shut" verbatim) → **P3**.
  - **The cat** (l.10 "the cat was asleep on the hearth beside it") reorders Ch.13 l.448 "a cat on the hearth asleep" one page before l.74 uses the cat as the comparison → **P7**.
  - **"Across the threshold"** (l.66) is sample-12's 3-gram (the broom), and the chapter's third threshold → **P9**.
  - **The laugh's trigger** is Halloran again (Ch.2's laugh was his call). W-09 already varied the shape; the source stays because the joke needs it. **Halloran is CLOSED as a laugh trigger.**
  - "Halloran had rung me from there in March, sitting on the bare floor of a flat he was leaving." (l.54) recalls Ch.2's set-piece detail. It is one sentence and the joke needs the reminder: **kept**, noted.
- **Retired reflexes:** no define-by-negation opener; no performed candour; no scene button; no closing aphorism. Anaphora: P6.
- **Ledger row:** approach ✓, open ✓, end ✓, breaks ✓, dialogue ✓, theme ✓, gear ✓, length ✓. **Beat subversion ✓** (instant, total, private; the response is a laugh). **Writer warnings:** no own-outcome line ✓; casts as memory of then ✓; no closing aphorism ✓; anaphora triads: P6. **Outline beats 1–5 all on the page**, including "Kallia put him there herself" (l.26) and "She does not tell him" (l.76, l.84).

---

## Character Chaos Check (Primary: Mara)
- **Irrelevant thought: PRESENT, inhabited.** The fur-hat woman's "bigger" (l.38); the Thessalian's girl's name (l.26, l.82); "What anybody in that town called a single street was beyond me." (l.30).
- **Cognitive distortion: PRESENT, inhabited.** "Eight years was plenty of time, I told myself. Men went where the work was." (l.124): she talks Valens out of the danger she is planning around. And the swing to the other pole: "This summer would do. For all anybody could tell me, it stood open tonight" (l.50).
- **Unprompted memory: PRESENT, triggered** (the plaster → the casts → the plaster).
- **Failed emotional management: PRESENT.** The jar held past full (l.10); the laugh that "came round the sides anyway" (l.62); the fingers back on the patch "some while later" (l.42).
- **Voice under pressure: demonstrated** (level 1–2: asides gone at the fountain and the knife; plain hands-and-bodies sentences; they return, dry, once the plan steadies her).
- **4/4, inhabited.** No mediated sentence explains the chaos.

## Secondary Character Chaos
- **Valens:** the knife up before he is awake enough to know what woke him (l.68); "She'll dig it crooked." His own moment, not a tool.
- **Kallia:** midnight salt water for a stranger's son; her own blanket, burned at the corner, over a man's feet; folded in four by morning. Her own moment.
- **Theano:** lets the crow stay (l.6).
- **The Thessalian father:** blames the ram, "Every mile, it told us."
- No secondary character is a mere function. No cap.

---

## The Tomorrow Test
**What the reader remembers:** a woman lying a yard from the man who carried the god's answer out of the temple, with the name of the city behind her teeth, telling him instead about another woman's well, and then saying the word with no sound toward the jars: "To everybody under that roof it was a town in Italy where they made fish sauce." And, at the edges: the jar overflowing down her sleeves; a schoolboy Pliny, nine years old somewhere in northern Italy, eight years before he watches the mountain.
**Anchor type:** BOTH. IMAGE (the hand over his shoulder; the jar; the pretzel; the dog cast; the folded blanket). QUOTE ("fish sauce"; "a boy of nine now"; "I left him out of the plan. He kept being in it.").
**Verdict: ANCHOR EXISTS** (strong; +0.5 CVI). **Type check:** Ch.11 an animal's stillness, Ch.12 an object in motion, Ch.13 a recitation and a one-word reveal; Ch.14 a concealment (a word withheld, a hand withheld). New to the book.

## The Shareability Test
"She finally works out what 'Pompeii' means: the door home is in the one city she knows is going to be buried, and she knows the YEAR. She can't tell anyone. To everyone around her it's just a town where they make fish sauce. So she laughs until she squeaks, then lies there planning how to get there." Running total: 14 chapters, 25+ shareable moments.

---

## Reader Reports

### The Devourer (3.0k after Ch.13's 7.5k)
- **Speeds up:** the year arriving whole; the jar overflowing; the laugh; the knife; "She'll dig it crooked."; the fish sauce; the plan's man problem.
- **Slows:** the tombs paragraph (l.32); the Saint Paul paragraph (l.126); the night court with the sick boy (l.94–l.114) reads as an interlude until Kallia's blanket pays it.
- **Would they stop?** No. It is short, and every quiet shard is followed by a spike.
- **Last page:** "He's gone down for the mules" makes them turn it: he went without being asked.

### The Critic
**Underlines:** "a boy of nine now"; "beyond me"; "she had thought they would be bigger"; "as far as Trenton"; "after the funny part had gone out of it"; "the cat on Theano's hearth"; "or let me think he did"; "He kept being in it."; "could have drawn blindfold".
**Disappointments:**
- "*Whoever plastered it had not troubled* — the book's oldest frame, a fourth time" (P1);
- "*He took in … my wet front*: the inventory look again" (C1);
- "*'Tomorrow,' I had said* — a callback announced" (P2);
- "six of nine shards end on a click" (P4, P5);
- "*to find his way about in it*, *so that somebody would see the place*: explanations the facts did not need" (F1, F2).

### The Hostile
1. **Theano's jars** (l.10): "her jar stood empty" … "I held the jar under the spout" … "I tipped it into her big jar". Which jar did she carry? (audit I-24, still open) → **L2**.
2. **Kallia "asked me nothing"** (l.20) at supper, yet "had had every other piece of the day from me over supper" (l.106). If Mara talked through supper, she did not eat on the woodpile in silence → **L1**.
3. **The gate bar** (l.146–l.150): Kallia stands "with the bar in her hands", then "took the bar down" (audit I-01, still open) → **L3**.
4. **Paul's ship** (l.126): "His grain ship was an Alexandrian; it wintered on Malta". In Acts 27–28 his grain ship was wrecked on Malta; a second Alexandrian that had wintered there carried him to Puteoli. A classicist's daughter knows the wreck → **R23** (tested).
5. **A classicist who knows the year still hopes for an early door:** "This summer would do." (l.50). That is canon (she refuses the arithmetic until Ch.36) and the page earns it with "The god had not said when." ✓
6. **The casts in New York, April 1979:** the AMNH showing of "Pompeii A.D. 79" ran April–July 1979 (audit W-01) ✓.

**Verdict:** "Three small logic seams, one compressed fact; no hole."

### The Casual Reader (airport, 10 pages)
- **Hooked at once:** Ch.13 ended on "Pompeii."; this one opens "I knew the year." They already know what she knows.
- **Feels it at:** the water running down her sleeves while she keeps holding the jar; the fur-hat woman; the laugh with a squeak in it; the knife on his forearm; "fish sauce", which makes them grin and wince at once.
- **Gets a jolt from:** "He was a boy of nine now."
- **Frictions:** the house names and Fiorelli; the two letters "for Tacitus"; Saint Paul; Halloran's room needs them to remember Ch.2.
- **Would they buy after 3 pages?** Yes. **Do they stay?** Yes: she has decided to walk toward the one place on earth they would never go, and the man is "in it" whether she likes it or not. **9.0/10.**
- **Not 9.5:** almost no talk, and three history passages in a row of shards.

### The Devoted Reader (active: long saga)
**Will post about:** Fiorelli's regiones and insulae; the bench tombs outside the Herculaneum Gate; the 1978–79 "Pompeii A.D. 79" tour and the dog cast; Pliny reading Livy at seventeen and being nine *now*; the Alexandrian grain ships and Paul at Puteoli; "a door that was only paint"; the dog on the tomb road against the dog in the gallery; the half moon setting at midnight on the 7th.
**Will catch:** the "Whoever … had" frame (P1); "took in … my wet front" (C1); "see it shut" from Ch.13 (P3); the father home "in September" a third time (P10); Paul's ship (R23).

---

## Cross-Reader Matrix
| Issue | Devourer | Critic | Hostile | Casual | Devoted | Severity |
|---|---|---|---|---|---|---|
| F1–F3, L1 #11 over the cap (4 at 1.32/1k) | | ✓ | ✓ (L1 seam) | | ✓ | **SHOULD FIX → blocking** (hard cap) |
| P1 "Whoever … had" (SPENT frame, 4th) | | ✓ | | | ✓ | **SHOULD FIX → blocking** (law) |
| C1, C2 SPENT look frames ("took in"; "came round then") | | ✓ | | | ✓ | **SHOULD FIX → blocking** (law) |
| P2, P3, P7, P9 reuse of Ch.13 / sample strings and pointers | | ✓ | | | ✓ | **SHOULD FIX → blocking** (law) |
| P4, P5 shard kickers 6/9; P6 soft triad; P11 time ladder | ✓ (the clicks) | ✓ | | | | **SHOULD FIX → blocking** (fragmented-chapter reflexes, named in the brief) |
| L2, L3 jars and bar | | | ✓ | | | INVESTIGATE → fix (cheap logic) |
| R23 Paul's ship | | | ✓ | | ✓ | SHOULD FIX → fix (+5 words, helps the floor) |
| P10 father-in-September memory frame (3rd) | | ✓ | | | ✓ | SHOULD FIX → fix |
| History passages (Fiorelli, the letters, Paul) | ✓ | | | ✓ | | SHOULD FIX → **no change**: each is used (the plan, the dread, the crossing) and short; cutting them would break the 3,000 floor |
| Halloran as the laugh's trigger again | | ✓ | | ✓ (needs Ch.2) | | INVESTIGATE → **no change** (the joke needs him); Halloran CLOSED as a trigger |

---

## Revision Recommendations (Ranked)
*All 23 strings below were applied together to a scratch copy and run through `check_chapter.sh 14`, `shape_check --strict`, `voice_wear_check.py` and `tic_report.py --gate`: all clean, echo 0. Strings that tripped a gate on my first tries are listed under "Do not use".*

| # | Location | Problem type | What happens now | Why it fails | Revision direction (exact) | Project rule? |
|---|---|---|---|---|---|---|
| L1 | l.106 | Logic + Style (#11, repair-added) + pointer | "Kallia had had every other piece of the day from me over supper." | Contradicts l.20 "Kallia asked me nothing." / "I ate on the end of the woodpile while the Thessalians argued", and glosses why she asks. Without it, her midnight question is the payoff of her silence at supper. | **Delete the paragraph** (and its blank line). (−12) | Yes: "a continuity repair that adds a gloss recomputes #11 density" (restated; 4th chapter running) |
| L2 | l.10 | Logic | "Inside her door, beside the loom, her jar stood empty." … "I tipped it into her big jar" | Two jars, one introduced (audit I-24). | → "Inside her door, beside the loom, her **big jar stood empty, with a smaller one turned upside down on its mouth.**" (+12) | No |
| L3 | l.146 | Logic | "Kallia stood at the gate with the bar in her hands." then "She took the bar down" | If the bar is in her hands it is already down (audit I-01). | → "Kallia stood at the gate, **ready to lift the bar.**" (−1) | No |
| C1 | l.18 | Style (SPENT frame; closed look) | "He took in the crows' house above us, and my wet front." | "took in my [X]" is SPENT; a two-item look over the house and her body is the CLOSED item-by-item look; Ch.13 l.400 has "He took in Valens … and Kallia" one chapter back. | → "**He gave the crows' house above us one look.**" (−3) | No |
| C2 | l.72 | Style (SPENT gaze-arrival) | "His head came round then, and he found where I lay." | The "looked at me then / eyes came round to me" family is SPENT. | → "**He kept his eyes on the gate while he asked it.**" (0; his card: exits first) | Yes: add `\b(head\|eyes\|face) came round (then\|to me)\b` to the tic gate |
| C3 | l.82 | Style (in-chapter double) | "His breathing evened." | l.26 already gave "His breathing was slow and even". | → "**He slept almost at once.**" (+1) | No |
| C4 | l.122 | Style (in-chapter double; Ch.12 echo) | "The one man I had was asleep across my doorway with a price on him" | Second "asleep across [the] door" (l.24), and Valens's own Ch.12 "I slept across her door" (SPENT for Ch.22). Keep l.24 as the one rhyme. | → "…was asleep **within reach of my hand** with a price on him in Corinth." (+2; it answers l.84's drawn-back hand) | No |
| F1 | l.28 | Style (#11) | "and numbered every one, to find his way about in it." | Purpose tail. | → "and numbered every one, **like sherds in a tray.**" (−2; her lab domain, characterizing) | No |
| F2 | l.54 | Style (#11) | "He had offered me a bed in the house the survey rented, a room with a window in it, so that somebody would see the place." | Purpose clause paraphrasing Ch.2. | → "He had offered me **my father's bed** in the house the survey rented, a room with a window in it, **for the season.**" (−3; sets up "never a spare bed" two lines on, unannounced) | No |
| F3 | l.122 | Style (#11) | "A husband, a brother or an owner: somebody whose name went down first." | Colon gloss. | → "**A husband, or a brother, or failing those an owner.**" (−2; the dry aside returns as she steadies) | No |
| P1 | l.36 | Style (SPENT frame) | "Behind my mat the wall was mud brick under a skin of lime plaster. Whoever plastered it had not troubled to finish it smooth." | "Whoever [made] it had" is SPENT at 3, "no fourth, in any verb"; and it grades an absent workman. | → "Behind my mat the wall was mud brick under a skin of lime plaster. **It was thin in places and never floated smooth.**" (−1; a condition, not a verdict) | Yes: gate `\bWhoever \w+ (it\|that\|them)\b[^.]{0,20}\bhad\b` at 0 |
| P2 | l.134–l.136 | Style (call-out pointer opener) | "\"Tomorrow,\" I had said, about the cave." / "There was no need of the cave now," | Quotes her Ch.13 line to open the shard. | → "**That left the cave. There was no need of it now,** if the god meant…" (one paragraph; −4) | Yes: gate `^"[^"]+," I had said` as a pointer |
| P3 | l.138 | Style (Ch.13 phrase) | "I wanted to stand in it in daylight and see it shut with my own eyes." | Paraphrases Ch.13 l.360 "I want to see it shut for myself." | → "I wanted to stand in it in daylight, **with my fingers on the crack, and feel nothing come through.**" (+3; a threshold touch in fresh words) | No |
| P4 | l.140 | Style (#1 binary + shard kicker) | "Either the cave was shut, or it was open. I meant to go up as soon as it was light and find out which." | A symmetric binary and a click. | → "**I meant to go up as soon as it was light, with Valens and the mules if he would come, and alone if he would rather sleep.**" (+2; plain logistics, and S10's "He's gone down for the mules" now answers it) | No |
| P5 | l.130 | Style (shard kicker) | "It was a good plan. I said it over once more, bowl to door, and it held." | "and it held" clicks the shard shut. "It was a good plan." stays: it is the resolve, and the reader's irony. | → "It was a good plan. I said it over once more, bowl to door." (−3) | Yes: "Fragmented chapters: ≤ half the internal shards close on a turned line" |
| P6 | l.6 | Style (anaphora triad) | "The mountain … was that mountain. The sea to the west was the bay under it. The dead of that town…" | Three sentences opening "The [noun]" (writer warning). | → "**Its sea** to the west was the bay under it." (0) | No |
| P7 | l.10 | Style (Ch.13 image reordered) | "the cat was asleep on the hearth beside it." | Ch.13 l.448 "a cat on the hearth asleep"; l.74 uses the cat as the comparison anyway. | → "the cat **opened one eye at me.**" (−2) | No |
| P8 | l.6 | Voice (stand-in forming) | "before her mouth had quite closed on the word," | "the word" stands in for the city 3× (l.6, l.74, l.86). | → "…closed on **the name**," (0) | No |
| P9 | l.66 | Style (sample-12 3-gram; 3rd threshold) | "Across the threshold Valens was up on one elbow." | sample-12's "across the threshold" (the broom); the chapter's third threshold. | → "**On his blanket** Valens was up on one elbow." (0) | No |
| P10 | l.58 | Style (memory shape, 3rd) | "He came home in September brown to the elbows," | Father-home-in-September: Ch.3 (sherds), Ch.13 (slides), Ch.14. Also the "[color] to the [joint]" frame. | → "He came home **lean and dark**, with his boots…" (−3) | Yes: "the father's September return is CLOSED as a memory frame" |
| P11 | l.118 | Style (repeated shard openings) | "In the middle of the night I made the plan." | Adjacent time-stamp openers (l.90 "Some hours on,"). | → "**I made the plan in the middle of the night.**" (0; rhymes with "I knew the year." for the outline's two non-negotiables) | No |
| R22 | l.28 | Style (#8 doubled pick-up) | "I had the town. I had it from above, the way" | Third doubled pick-up in a 3k chapter. | → "**I had the whole town from above,** the way" (−2) | No |
| R23 | l.126 | Factual | "His grain ship was an Alexandrian; it wintered on Malta and came in to Puteoli with the spring." | Acts 27–28: his ship was wrecked on Malta; another Alexandrian that had wintered there took him on. | → "His grain ship **went aground on Malta, and another Alexandrian that had wintered there brought him in to Puteoli** with the spring." (+5) | No |

### Fix order: Logic (L1–L3) → Character frames (C1–C4) → #11 (F1–F3) → Style law (P1–P11) → R22 → Factual (R23)

**Kept on purpose (and why):**
- The four strongest shard closers: S2 benches (l.32, a plain result that Ch.19's search can start from), S4 the dog (l.50), S5 the laugh's stop (l.62), S6 the fish sauce (l.86).
- The three borderline #11 clauses ("and none of it would be the question"; "She was indoors already."; "He had outranked Halloran. He had picked the town.").
- l.24 "Valens was asleep across the door of the storeroom." (the one rhyme with Ch.12, unannounced).
- l.54's Halloran recall (the joke needs it).
- The well story retold as cover (l.76): a substitute anecdote is this chapter's device and is SPENT after it.
- "Theano told it to get off, and it stayed, and she let it." (l.6): the "let it [verb]" frame is at its cap of 1.

**Do not use** (each tripped a gate on my first try):
- "on Kallia's floor" (echo, Ch.6);
- "glanced up at the" and "he looked up" (echo, Ch.1 / Ch.2);
- "and shut it again" and "me and shut it again" (echo and voice-wear, Ch.7);
- "went back to sleep" (tic gate: "went back to" 3× book-wide);
- "at first light" (tic gate: 3× book-wide);
- "with her hands on" and "with my hand on" (voice-wear self-repeat);
- "I meant to be" (voice-wear self-repeat);
- merging P1 or P6 into single sentences (median rose to 13, out of the low gear).

---

## Strengths to PRESERVE (do not touch in polish)
1. **The first sentence, byte-identical**, and "it came whole. Seventy-nine, late in the summer, in August."
2. **The jar** (l.10): "I kept on holding it. The water came over the rim and ran down my wrists into my sleeves and on down my ribs, very cold."; "not only Syracuse"; the ugly sentence.
3. "I wanted to throw something at it, and my hands were empty." (l.18).
4. "What anybody in that town called a single street was beyond me." and "got only the benches."
5. **The casts and the pretzel** (l.38–l.42), every beat, and the fingers returning to the patch.
6. **"He was a boy of nine now, somewhere in the north of Italy, at his lessons."** and the dog on the tomb road.
7. **The laugh paragraph** (l.62), byte-identical.
8. **The knife and the well** (l.68–l.80): "She'll dig it crooked."
9. **The anchor paragraph** (l.74) and **the hand** (l.84); "**To everybody under that roof it was a town in Italy where they made fish sauce.**"
10. The ram's boy and Kallia (l.94–l.112): "It isn't their knees."; the burned blanket.
11. "I left him out of the plan. He kept being in it."; "a town I had never stood in and could have drawn blindfold"; "It was a good plan."
12. **The close:** the half moon, the empty doorway, the blanket folded in four and "He's gone down for the mules," (l.144–l.148, touched only by L3's bar), and **the last paragraph byte-identical** (the cliffs).

---

## PATH TO 8.5 (mandatory; the Floor is 7.5)

**Prose & Voice 7.5 → 8.5 requires:**
- **#11 under the cap:** L1, F1, F2, F3 take it from 4 firm instances (1.32/1k) to 0 firm (the three borderline clauses stay, ≤0.99/1k even if a stricter reader counts them all).
- **The law cluster cleared:** P1 (the fourth "Whoever"), C1 ("took in … my wet front"), C2 ("came round then"), P2/P3 (the Ch.13 pointer and paraphrase), P7/P9 (the cat, sample-12), P10 (the September father).
- **The fragmented-chapter reflexes cleared:** P4/P5 (kickers 6 → 4 of 9), P6 (the soft triad), P11 (the adjacent time openers), R22 (doubled pick-ups 3 → 2), C3/C4/P8 (in-chapter doubles).

The stopping sentence (l.46), the underlines and the ugly sentence stay. **L1 is the single highest-value cut:** it removes an #11 instance, a logic seam and a pointer at once, and it lets Kallia's silence at supper pay off at midnight.

**Characters (8.5) and everything else hold on merit;** C1–C4 make Valens's stage business clean.

**Apply in this order; the strings are exact (see the table), or run the tested script:**
```
python3 /tmp/claude-0/-home-user/63791ee5-159c-5791-9429-07920f8d9417/scratchpad/ch14-eval-fixes.py \
  books/the-hour-of-ash/manuscript/chapters/chapter-14.md \
  books/the-hour-of-ash/manuscript/chapters/chapter-14.md
```
(from /home/user/Books; it asserts one match per string and aborts on any miss). Then run `bash books/the-hour-of-ash/tools/check_chapter.sh 14` and `python3 tools/shape_check.py books/the-hour-of-ash --strict`, and update the chapter's word-count HTML comment (l.4).

**What the tested run produced (all 23 strings applied together):**

| Measure | Before | After |
|---|---|---|
| Words (shape_check) | 3,022 | **3,007** (≥ 3,000 ✓) |
| Words (style_check) | 3,028 | 3,013 |
| Dialogue | 5% | **5%** (0–10 ✓) |
| Median sentence | 12 | **12** (gear low ✓) |
| Breaks / signatures | 9 / `I-punch` → `long-fade` | unchanged |
| First sentence / last paragraph | | byte-identical |
| `check_chapter.sh 14` | clean | **all clean**: style (simile 0.7/1k, em-dash 0, foreshadow 0), grammar 0, rhythm 0, show/tell no flags, voice-wear strict clean, tic gate clean (and-chains 1/9), echo 0, command echo none, metaphor 0.7/1k |
| `shape_check --strict` | CLEAN | **CLEAN** |
| #11 (firm) | 4 (1.32/1k) | **0** |
| Paragraph-final negations | 4 (1.32/1k) | **4 (1.33/1k)** ✓ |
| Shard closers on a turned line | 6 / 9 | **4 / 9** |
| SPENT frames on the page ("Whoever … had", "took in", gaze "then", call-out opener) | 4 | **0** |
| Anti-AI | 9/20, −1.875 | **7/20, −1.125** (clean band) |

**Expected:** Prose 8.5 (merit 8.0 → 8.5 on 23 cited changes; the +0.5 limit applied to the merit score, as in Ch.10, 12 and 13) → **Floor 8.5, Average 8.86** (9.0 / 9.0 / 8.5 / 8.5 / 9.0 / 9.0 / 9.0). Casual 9.0 holds. CVI-L 8.9 holds.

---

## Pacing check (one line for `feedback/progress.md`)
Ch.14 (cycle 0) · Fragmented *one night in shards* between Ch.13 Parallel and Ch.15 Chronological ✓.
- **Length:** 3,022w (target 3,400, −11%, inside 3,000–3,800; 3,007 after the PATH). **Book:** 75,143 vs 81,000 cumulative (−7.2%); the 220k floor is safe at that rate (≈242k projected).
- **Dialogue** 5% (0–10 ✓); **9 breaks** ✓; **gear low, median 12** ✓, down from Ch.13's mid 14, as planned.
- **Neighbours:** Ch.12 4,710w, low (10), 28%, In medias res → Ch.13 7,503w, mid (14), 38%, Parallel → **Ch.14 3,022w, low (12), 5%, Fragmented** → Ch.15 planned 7,800w, high, 30–40%, Chronological. A short low-gear pressure chapter after the long mid-gear turn, then the long high-gear romance turn: the variance is the design ✓.
- **Signatures:** `I-punch` / `long-fade`; no three running (Ch.12 `punch`, Ch.13 `dialogue`).
- **Emotional slot ✓:** after Ch.13's revelation, the private dread → laugh → concealment → resolve; the peak is a mandated laugh in a new shape.
- **Value shift** + / − / − / + ✓; the pull is soft by design (long fade) and real (the cave, the mules).
- **Slow patches:** the tombs paragraph and the Saint Paul paragraph. Both are load-bearing and short; no cut (the floor forbids it).

**Verdict: OK.**

---

## Cross-Book Pattern Detection (Ch.1–14)
1. **Repairs add explanation, for the fourth chapter running** (Ch.10, 12, 13, 14). W-08's suggested fix turned a pointer into a gloss ("every other piece of the day from me over supper") and kept the seam. The rule exists; an #11 proxy in the tic gate would make the density visible to the editor (`\b(so that|to find|whose name)\b`, `: [a-z]+body whose`) — **pipeline, UPDATE RULE.**
2. **The oldest spent frames come back in new verbs.** "Whoever [made] it had" (SPENT at 3, "no fourth, in any verb") returned as "Whoever plastered it"; "took in my [X]" (SPENT after Ch.6) returned with an object in front of "my". Both are regex-able: add `WHOEVER_RX` and `TOOK_IN_RX` to `tic_report.py` (root), with the gaze-arrival and call-out pointer patterns from C2 and P2.
3. **Fragmented chapters breed shard kickers.** Ch.4 was fixed for it; Ch.14 reached 6 of 9 through a chain whose disruptor wrote "one kicker per shard is about the most". Next fragmented chapters: **Ch.24, 30, 42.** Brief them with "≤ half the shards close on a turned line; the rest end on an act".
4. **Memory frames recur by their marker word.** "September" is the father's return in three chapters. The bible should register memory *markers* (season, room, parent) next to memory shapes.
5. **What varies, as it should:** the structure (Fragmented, after Parallel); the opening (`I-punch`, the book's first) and the ending (`long-fade`); the gear (low); the dialogue share (5%, the book's lowest, by design); the anchor type (concealment, new); the body-rebel channels (hands on a jar, the laugh's squeak, fingers on plaster).

**Bookkeeping (orchestrator):**
- **Re-sync the bible's Ch.14 block and "At-risk after Ch.14" to the final page** (audit I-26). It still quotes the Writer's draft: "the 1988 casts", "the carbonized loaf as a briquette", "He had picked the year.", "There's no moon till the new one", "the old moon before dawn … a paring of it", "Her water carried.", "ran on well after the funny part", "in its long turns", "Kallia had had every other piece of it from me, in its order", "He weighed me a while longer.", and a simile count of 2 that included the briquette.
- **At-risk after Ch.14, add (post-PATH):**
  - Halloran: CLOSED as a laugh trigger (Ch.2, Ch.14);
  - the father's September return: CLOSED as a memory frame (Ch.3, Ch.13); a parent showing the child antiquity: 2 running (Ch.13, Ch.14), so the next memory has no parent in it;
  - **no longer memory in Ch.15 or Ch.16**;
  - the substitute anecdote as cover: SPENT; stepping over a sleeper: SPENT; Valens asleep "across the door": once (the Plautia rhyme);
  - "the word" as the city's stand-in: 2, CLOSED;
  - "like sherds in a tray", "failing those an owner", "within reach of my hand", "my father's bed": once each;
  - Kallia handing Mara an object: 2 in Ch.14 (WATCH, ≤1 in Ch.15–16);
  - the "Whoever … had" frame: still SPENT, and now recurred once after the ban (zero tolerance).
- **Ch.15 carry-overs:** account for the cave visit in a clause (CH13-7); register the plan's change from "Corinth in autumn" (audit I-17: the page plans to winter in Delphi on the bowl and sail next spring).

---

## VERDICT
**POLISH. Gate NOT MET.**

| Measure | Result |
|---|---|
| Genesis Floor | **7.5** (Prose & Voice, capped) |
| Average | **8.71** |
| Casual | **9.0** |
| Pacing | **OK** |
| CVI-Launch (CVI-L) | **8.9** |
| CVI-Legacy | 6.9 (provisional) |
| Mechanical suite | all clean (echo 0, tic gate clean, voice-wear strict clean, shape CLEAN) |
| Foreshadowing / own outcome narrated | **0 / never** ✓ |
| Memory triggered by the scene (CP2-2) | ✓ (casts ← plaster; S5 ← her own chain, returned by the laugh) |
| Explanation-density cap | **FAIL** (4 at 1.32/1k) → 0 firm after the PATH |
| Paragraph-final negations | 4 (1.32/1k) ✓ ≤1.5 |
| Tics | verbal 0; gate classes clean; **SPENT look frames 2 (C1, C2)** → 0 |
| Fragmented reflexes (triads, kickers, shard openings, memory shapes) | **FAIL** (soft triad; kickers 6/9; adjacent time openers; September ×3) → cleared |
| Reuse of earlier phrases / set pieces | **FAIL** (P1, P2, P3, P7, P9, C4) → cleared |
| Ledger | ✓ on every hard field |
| AI patterns | 9/20 (watch band) → 7/20 (clean band) |

**Failing dimension:** Prose & Voice (7.5, capped; merit 8.0). The fixes are surgical and were tested together: L1–L3, C1–C4, F1–F3, P1–P11, R22, R23 (23 strings). The result is 3,007 words, dialogue 5%, median 12, every gate clean, and the first sentence and the last paragraph unchanged. Then run E (gates) and F (re-evaluation). **Expected after one cycle: Floor 8.5 / Average 8.86 / Casual 9.0 / PASS.**

The chapter does what the outline asked and the genre usually spends a confidant scene on. She knows the year on a doorstep, holds a jar under a spout until it runs down her ribs, and finds Pliny nine years old somewhere in the north of Italy. She laughs until she squeaks a yard from the man who carried the answer out, tells him about another woman's well instead, and plans her way toward the one town she knows will be buried, with him in the plan whether she likes it or not. What holds it below the gate is a narrator who explains four small things the page already shows, and a handful of the book's oldest frames returning in new verbs.

**BIAS CHECK:** This evaluation was produced by the same system that wrote the prose. Confidence in scores above 8.0 requires external validation (beta readers, editors, comp analysis).
- **The #11 count is a judgment.** Two instances are firm by any standard (the purpose tails, F1 and F2). F3's colon gloss and L1's repair gloss are counted by the standard that counted Ch.13's "where a man could see the whole climb". With only F1 and F2 the chapter sits at 0.66/1k, under the cap, and Prose would rest on its merit (8.0), still below the gate because of the law items. The PATH clears both readings.
- **The six shard kickers are my classification.** A reader who calls S2 ("got only the benches") a plain result counts five. The PATH brings either count to half or less.
- Originality, Theme, Pacing, Emotion and Immersion at 9.0, Casual 9.0 and CVI-Launch 8.9 are one-chapter judgments by the system that wrote the book.
