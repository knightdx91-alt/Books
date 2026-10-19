# Evaluation: Chapter 10 — Kallia's Letter (run 2)
**Evaluator:** book-evaluator (independent; did not write this prose) | **Date:** 2026-10-19
**Text evaluated:** `manuscript/chapters/chapter-10.md` after the writer, dialogue-polish, hook-craft (one edit to the close), the disruptor and the continuity repair (C-01, W-01…W-08, plus the earned reed-blind paragraph). Length: **2,563 prose words** (shape_check), 2,574 by style_check, 2,741 by `wc -w` (incl. header). Target 2,800 (−8.5%), inside the 2,500–3,100 range by 63 words.
**Read against:** chapters 1–9 in full; book CLAUDE.md hard gates; STATE.yaml (guardrails, NO FORESHADOWING, NO TICS incl. gestures and refrains, retired reflexes, ARCH-13 no-pull list); outline Ledger row 10 + `## Chapter 10` (single-scene *one reading, one afternoon*, object → `short-punch`, **PLAIN STOP (no pull)** → `quiet`, 2,800w, dialogue 30–40%, 0 breaks, gear mid; HARD writer warnings: no hook, no image-with-meaning, no aphorism at the end, no Ariston/Mara parallel in narration); voice-dna §0, §1, §3b, §4, §6, §8; character-bible.md (Mara, Kallia, Nikaso, Ariston cards and their Ch.10 blocks; the Ch.10 walk-on note; every at-risk block through "after Ch.10"; the at-risk table); voice-bank samples 01–13 (sample-12, the Ch.10 calibration, and sample-08/09 by string and structure); feedback/independent-review-ch1-5.md; dialogue-, hook-, disruption-chapter-10.md; continuity/chapter-10-audit.md; revision-chapter-10-continuity.md; chapter-9-eval.md (format and running laws).
**Genre profile:** commercial historical romance / time-slip; comp *Outlander*. Anti-AI band: commercial (0–8 clean, 9–11 watch). Engagement: empathy 55 / fascination 30 / self-insertion 15. Dimension 7 = **IMMERSION**.
**Design ruling applied (author):** this is the first of the four kept no-pull chapters (Ch.10, 31, 34, 44). No pull is the design, not a defect. Casual is scored on whether a reader **stays with** the chapter, not on whether they are pulled into Ch.11; Pacing and CVI commercial pacing are not docked for the absent hook.

**Measured here, not taken from any report:** `bash books/the-hour-of-ash/tools/check_chapter.sh 10` (run from /home/user/Books) is **clean on every gate**. Style: 2,574w, simile 0.4/1k, adverb 2.7/1k, em-dash 0, **foreshadow 0**. Grammar 0. Rhythm 0 flagged. Show/tell no flags (dialogue meter 36.3%). Voice-wear strict clean. 5a tic gate clean: and-chains 1 (cap 9), credential asides 0, negation pivots 0, 'So' openers 0, 'before I decided' 0, no gesture class charged to Ch.10 (bend/stoop 0, as the bible ordered). 5c echo scan 0; command-echo candidates none. Metaphor: fig 0.4/1k, 1 simile counted, median 15, 0% over 40 words. Shape: CLEAN; Ch.10 = `short-punch` (8 words) → `quiet` (9 words), 0 breaks, dialogue 39%, median 15. Semicolons 3 (1.2/1k). "as if" 1 (¶148). "the way [x]" frames 2 (¶44, ¶64). Book: **54,333 words over 10 chapters** against 57,800 cumulative target (−6.0%).
**My own scans (scratch scripts, not gates):** a 3/4/5/6-gram scan of Ch.10 against Ch.1–9 and all 13 voice-bank samples, raw and pronoun-normalized (I/she/he → P), keeping 3-grams only with ≥2 content words; then targeted greps across Ch.1–9 for every candidate, and a beat-order comparison of Ch.10's set pieces against the nearest earlier scenes (Ch.9's curse tablet and notice, Ch.7's closing broom, Ch.5's spring, sample-12). As in Ch.9, the gates are right that no content-rich 4-gram recurs. What recurs is (a) **whole set-piece skeletons lifted from the immediately previous chapter**, (b) **narrator moves with a fixed function** (the speech ledger, the held silence measured by something indifferent moving, the object's weight standing in for feeling), (c) **one comparison used twice**, and (d) **voice-bank structure** that survived the continuity repair by being reordered or re-nouned. Every one is named below with its source and, where one can be written, a regex.
*(¶N = line number in the chapter file, as in the Ch.5–9 evaluations. Prior-chapter ¶ = line number in that chapter's file.)*

---

## HEADLINE
**CVI-Launch:** 9.3 (8.8 base + 0.5 strong anchor) | **CVI-Legacy:** 6.6 (provisional) | **Genesis Floor:** **8.0** | **Genesis Average:** **8.50**
**Casual Reader:** **8.5**
**Engagement type:** Empathy primary (a woman who cannot read hears her son is alive, married and never coming back, and rents his room). Fascination secondary (an authentic Greek soldier's letter from Emesa: formula, proskynema, Hyperberetaios, the address on the back; a missio causaria). Self-insertion tertiary (the reader as the one who reads the letter aloud).
**Divergence alert:** none by rule (9.3 − 8.0 = 1.3).
**Gate (Floor ≥ 8.5 AND Casual ≥ 8.5 AND pacing OK AND gates clean): NOT MET → POLISH.** Casual 8.5 ✓, pacing OK ✓, gates clean ✓. One dimension holds the floor: **Prose & Voice 8.0**, for the reason that has held all ten cycle 0s: narrator recurrence the gates cannot see. This time there are **seven blocking items (P1–P7)**, and the heaviest two are lifts from the chapter immediately before: the letter's arrival and opening are built on **Ch.9's curse-tablet skeleton** (a folded document measured against Mara's hand, its fastener "worked" out, the folds opened with a material simile, the hand described by how its lines run), and Kallia's look at the name reuses **Ch.9's reading-time measure** ("while a slow man might read it once" → "for the time it would have taken her to read it if she could read"). Then: the narrator's **speech ledger** in its fourth chapter ("It was the best Greek I had spoken since October"); **a comparison used twice** (Ch.8's "a market woman with a pickpocket in view" → "the way a woman in a crowd checks her purse"); the **held silence measured by an indifferent motion**, spent after Ch.9 and used twice here (the turning spindle, the moving tunic); a **sample-08 structural lift** ("I could have said a hundred things. I could have told him…" → "I could have left out the roof. I could have left out the father…"); and the **closing run's weighted object** ("it made a fatter packet than before"), the last surviving piece of the sample-12 refold. Every fix is a cut or a recast, pre-grepped. The design (the Elean, the belt hours, the reading, the yawn, the proxy questions, Nikaso, the obol, the broom, "Ariston's room") needs nothing.

---

## Genesis Score (Craft Assessment)

| Dimension | Score | Evidence | Cap reasons / holds |
|-----------|-------|----------|-------------|
| Originality | 8.5 | **The beat subversion is the outline's; nearly everything that makes it land is the writer's.** (1) **The yawn as the body rebel** (¶90): "The yawn took her in the middle of the court, enormous. It stretched her face and shut her eyes, and when it let her go her eyes were running with it. A second came behind it, as big." — grief coming out through the one channel she does not have to own, and Mara misreading it in-scene ("She had been on her feet since the dark…; I read the next part faster."). (2) **"Which arm?"** (¶58) right after the arm is read, then "He was never any use with the left," (¶62). (3) The neighbor-news answer to the greeting list (¶116): the dead, the married, "Thrasyllos walked to Kirrha after him in his bare feet." (4) "Here it's for the father's father." (¶88): the grandson's name leaves her house, said as custom. (5) The cup running joke from the gate to the reply (¶22–¶28, ¶154–¶156, ¶180). (6) **The house was never full** (¶32–¶36 "Full." / "The house is full."), and the chapter ends with the room let to the same man at his own price (¶192). (7) "The horse-seller," … "His name again." (¶174), the disruptor's interruption. (8) The bread given twice to the Patrae man, unremarked (¶44). | Held at 8.5. The genre beat (the soldier's letter) and its inversion are planned; the broom anchor was planted in Ch.7 (×2) and is a payoff, not a new image. The reed blind (¶128) duplicates the broom's function (judged below). |
| Theme | 8.5 | **A child who chose the life he made, carried entirely by objects and practical questions:** "Is she Greek?" / "Can she weave?" / "Anybody keeps a house." / "A roof you sit on," … "Where does the rain go?" / "Bought?" (¶74–¶102); "For the house there was no line, nor for anything under its roof." (¶122); "He can have Ariston's room, at the three obols." (¶192). Ch.5's hiring catechism ("Can you card wool?" … "Weave?", Ch.5 ¶335–¶339) comes back unannounced as the questions she asks about her son's wife: a re-read reward, not a pointer. **No one draws the Ariston/Mara parallel** (judged below). **Texture that means nothing:** the Elean's seasickness and the Corinthian's goat (¶38), the Patrae man's foot (¶44), "He used to drop snails in my water jar." (¶148), the flour on Nikaso's lips (¶144), the dead wasp (¶128), the neighbor's blanket (¶198). | Held at 8.5. (a) **Weight gathers at the end:** the blind let down at the moment of the blow (¶128, a drawn blind is a mourning sign to an Anglophone reader), "it made a fatter packet than before" (¶196), and "It was a good while yet till the lamps." (¶198, a time-remaining cadence in a book whose antagonist is a date). Each is defensible alone; together they lean the last third toward meaning (#18 minor). (b) "roof" ×6 is the chapter's one weighted noun; acceptable. |
| Characters | 8.5 | **Kallia's chapter, and her best:** every reply on her labor-and-money axis ("Water," ¶18; "That was a cup." ¶24; "Two and a half," … "At the vintage." ¶68; "Bought?" ¶102; "Put a plate on those, or the mice will be in." ¶164 to "How old was he, when he went?"; "On what?" ¶170; "And whoever carries it to Syria?" ¶178); she never sits, never touches Mara, never speaks of herself; the obol "on the bottom stair, where I would have to pass it" (¶186); the name once. **Nikaso** to her card (borrowed things and blame: "And then it's me that put a hole in his mother's sieve." ¶144) and takes the news as joy, the chapter's public face of it. **The Elean** is a complete walk-on in six lines (what he is owed, where he will sleep). **Mara 4/4 chaos, three inhabited** (below). Cover-the-name PASS for every speaker, the letter included (formula and plain news; no qualifier, no simile). | Held at 8.5, not capped. **WATCH (part of the PATH):** Kallia's **work-suspended tell** is becoming her stage signature: Ch.7 ¶182 (combs held apart, fleece hanging), Ch.9 ¶350 ("Kallia's sand had gone quiet"), and here ¶46 "Presently she let it hang." (functional: a hand freed for the letter), ¶112 the spindle hanging and turning, ¶122 "stood in the sun with the wool in her hand", ¶126 the pull of wool run back. Three expressive uses in one chapter of a class that recurs chapter after chapter is at the gesture-law edge; P5 removes ¶112 and brings it to two. Also: "living" ×3 in Kallia's mouth (¶116, ¶142, ¶184) and the cup ×6 are designed in-chapter rhymes (the last "living" is the chapter's best line); **close both after Ch.10**. Kallia's name-asks ("Which is his name?" ¶132, "His name again." ¶174) are at 2: closed. |
| **Prose & Voice** | **8.0** | **Stopping sentences:** "**Kallia yawned. The yawn took her in the middle of the court, enormous. It stretched her face and shut her eyes, and when it let her go her eyes were running with it.**" (¶90); "**That Elean will have been all round the stadium by now,** … **He can have Ariston's room, at the three obols.**" (¶192); "**Tell him the baker's old mother is living.**" (¶184). **Underlines:** "a young man with a peeling scalp who had been sick on the boat from Aigion and wanted it known" (¶6); "Her face gave him nothing for that." (¶16); "Then drink in Elis." (¶28); "I ran my eye to the foot of the papyrus, looking for a loom." (¶80); "The wool went out between her fingers in a thread so fine it could hardly hold the spindle up." (¶84); "I knew it the way I knew the year of the Armada, as a date on a page with a fire in it." (¶64); "Emesa was Homs." (¶94); "For the house there was no line, nor for anything under its roof." (¶122); "Nikaso put both hands over her mouth, and when she took them away there was flour on her lips." (¶144); "She took it to the lip of the gallery in short strokes, and nothing came over, and back to the door." (¶188). **Ugly sentence:** "The one on top was the cracked one but it fit." (¶166). **Voice under strain** (not fear; level 0–1 by design, the pressure is Kallia's): the reading speeds ("I read the next part faster", ¶90) and detaches ("My voice went on through the oxen without me.", ¶94; but see P9). | **Held at 8.0 for seven law items (P1–P7, below), the standard that held Ch.1–9 in cycle 0.** The two heaviest: **P1** the Ch.9 curse-tablet skeleton rebuilt as the letter's arrival and opening (¶6, ¶50 ← Ch.9 ¶278); **P2** Ch.9's reading-time measure re-used for Kallia (¶134 ← Ch.9 ¶408). Anti-AI −1.125 (8/20, top of the clean band). |
| Pacing | 8.5 | **Ledger row hit on every hard-gated field.** Single-scene (Ch.9 Collage / Ch.11 Chronological, no adjacency) ✓; `short-punch` open, 8 words ✓; `quiet` close, 9 words, multi-sentence closing paragraph (Ch.10 is not on the one-sentence-close list) ✓; 0 breaks ✓; dialogue 39% (30–40, top of band) ✓; gear mid, median 15 ✓; 2,563 in range ✓. **Speed as designed:** the gate brisk and comic (¶8–¶42); the belt hours slow (¶44); the reading held, then quickened by the yawn (¶90); Nikaso a burst (¶138–¶156); the reply quick and broken (¶162–¶186); the sweep slow (¶188); stop. **Value shift:** Kallia from not knowing (hope held unread in a belt) to knowing (bereaved by good news) (−−); Mara from reader to messenger, with an obol and an errand (+, small). **Plain stop:** PASS (judged below). | Held at 8.5. (a) The Jerusalem line (¶64) and the Homs postcard (¶94) are two narrator excursions inside the 400 words of the reading; the second is the chapter's chaos and earns its place, the first re-dates an event Ch.5 already dated (Revision #12). (b) Hook SENSORY IMMERSION 7 by design (hook-craft): a gentle open for a quiet chapter. |
| Emotion | 9.0 | **Anchor lands** (the outline's): "Up at the last door the broom still lay over the threshold, from post to post." (¶194), after a sweep of boards that "At dawn … had been swept already" and from which "nothing came over" (¶188). **Surprise lands, three ways:** the good news as bereavement (Kallia's flat "He's living." ¶142 under Nikaso's "The gods be thanked."); tears that come out as a yawn (¶90); the reply she sends is not about him at all ("Tell him the baker's old mother is living." ¶184). **Techniques ≥6:** object proxy (the broom, the obol on the stair, the room let at three obols); understatement ("Which arm?"); dramatic irony (the yawn misread; the room the house "was full" without); subtext questions (the wife); silence (no word to "He says the arm has knit," ¶124–¶126); humor (the cup, the snails, "Then drink in Elis."). **Body rebel:** Kallia's yawn (face and eyes; the hands channel is rested, as the bible ordered). **The peak is not a laugh** ✓. **≥9.0 challenge:** a senior editor setting this beside the quiet domestic grief scenes of *Outlander* (Jenny at Lallybroch) or of *The Nightingale* would accept that it competes; the restraint is better than the comp's. | Held at 9.0, not higher: the closing run carries one image too many (P7), and the reed blind pre-empts the broom by a few paragraphs (Revision #13). |
| **Immersion** (Dim 7) | 8.5 | **The letter is the period material, and it is exact:** "Ariston to Kallia, his mother, greeting, and many of them. Before everything I pray for your health, and every day I make an offering for you to the gods of this place" (¶52: πολλὰ χαίρειν, πρὸ μὲν πάντων, the daily proskynema); "Know that I was with the cohort before Jerusalem" (¶56); an early discharge by "the prefect" and savings "at the standards" (deposita ad signa; no auxiliary bounty, W-04 fixed); "the twentieth of Hyperberetaios" (¶120, the Syro-Macedonian month) and the address on the verso (¶122); the Orontes flowing north, so land "half a day below Emesa" is downstream; snow on the Lebanon "until the summer" (¶92); a son named for the maternal grandfather in a sonless Syrian house against "the father's father" in Phocis (¶86–¶88). **Delphi:** the Aigion–Kirrha crossing (¶38), the stadium houses (¶40), the lions (¶140), the reed blind and its slip-knot (¶128), the niche with the good knife and cumin (¶196), carded wool and a drop spindle (¶46, ¶84). | Held at 8.5, not 9.0. One court and one afternoon: the physical density that carried Ch.9's 9.0 (bronze, solder, wax, a defixio) is replaced by a document. Sensory range is narrow (warmth, the chickpeas, soot and a wasp, flour). (#15 minor: the packet described with full authority in ¶6.) |
| **FLOOR** | **8.0** | Prose & Voice | |
| **AVERAGE** | **8.50** | (8.5 × 5 + 8.0 + 9.0) / 7 = 59.5 / 7 | |

Floor–Average gap 0.50: no structural bottleneck. **Everything holding the floor is removable without touching a scene.**

**Trajectory vs Ch.1–9 (finals 8.50–8.64; cycle 0s all 8.0):** the identical cycle-0 profile for the tenth time. New this cycle: the recurrence has moved from phrases, to frames, to **whole set pieces copied from the chapter just finished** (the curse tablet's opening sequence; the notice's reading-time measure). A chapter-to-previous-chapter skeleton comparison would have caught both before the evaluator (Cross-Book #1).

---

## CVI-Launch Breakdown

| Input | Score | Evidence |
|-------|-------|----------|
| Commercial Pacing | 8.0/10 | 2,563 words, one afternoon, a comic gate scene to open, a reading with a turn in it, a burst of neighbor at the two-thirds mark. A non-reader finishes it. Loses 2 for no chapter-end pull (by design; not penalized in Genesis) and two excursions inside the reading. |
| Tomorrow Test | 6 anchors → 10 | (1) Kallia's double yawn, eyes running (IMAGE). (2) The broom across the threshold of an already-swept room (IMAGE). (3) "He can have Ariston's room, at the three obols." (QUOTE). (4) "Tell him the baker's old mother is living." (QUOTE). (5) "Which arm?" / "He was never any use with the left," (QUOTE). (6) Nikaso's floury lips (IMAGE). |
| Casual Reader | 8.5/10 | See report. |
| Shareability (quote / plot / emotional) | 4 / 2 / 4 → 8 / 4 / 8 → **7.5** | Quote: "Tell him the baker's old mother is living."; "He was never any use with the left."; "Then drink in Elis." Plot: none (no jolt; by design). Emotional: "her son writes that he's alive and happy in Syria, and she rents out his room." MAX 8 × 0.6 + AVG 6.67 × 0.4 = 7.47. |
| Concept Pitch | yes → 10 | |
| Human Closeness | yes → 10 | Mother and son through a letter; a household; a neighbor's joy. Nearly all of the chapter is intimate relationship. |
| **CVI-Launch** | **8.8 + 0.5 (strong anchor) = 9.3** | 8 × .2 + 10 × .2 + 8.5 × .2 + 7.5 × .2 + 10 × .1 + 10 × .1 = 8.8. One-chapter formula; BIAS CHECK applies. |

**CVI-Legacy (default weights; provisional):** Originality 8.5 × .30 + Theme 8.5 × .25 + Cultural Vocabulary 2 × .20 + Re-readability 7 × .15 + Identity 5 × .10 = **6.6**. Re-read rewards: Ch.6 "Letters." / "Nobody asked what you carry." (the letter was already on its nail at Kirrha when she asked); Ch.8 "not husbands and not sons"; Ch.7 "It's swept"; Ch.5's "Weave?" returning as "Can she weave?"; the girl who "ran off at the vintage" (Ch.5) and the son gone "At the vintage"; "The house is full." at noon.

---

## Anti-AI Scan (20 patterns; density per 1,000 words at 2.56k; commercial band)

| # | Pattern | Result | Count / density | Citation |
|---|---|---|---|---|
| 1 | Forced symmetry | **FOUND: minor** | 1 (0.39) | "the bad to be done with, and the good to be had" (¶44). **−0.125** |
| 2 | Empty poetic vocabulary | Clear | 0 | |
| 3 | Automatic rule of three | **FOUND: minor** | 1 (0.39) | "I could have left out the roof. I could have left out the father… There was not a soul…" (¶158), a 2+1 with an anaphora (also P6). The letter's greeting list and Nikaso's "Syria, and a wife, and a child." (¶156) are designed. **−0.125** |
| 4 | Em dashes | Clear | 0 | |
| 5 | Empty metaphors | Clear | 0 | The one simile counted ("stiff as a dried leaf", ¶50) and the two comparison frames characterize. |
| 6 | Dramatic "And" openings | Clear | narration 0; 1 dialogue paragraph ("And whoever carries it to Syria?", ¶178) | The Ch.9 "And…" rejoinder WATCH is honored. |
| 7 | Pseudo-philosophical closings | Trace | — | "There was not a soul in that court or in that lane who could have told the difference." (¶158) closes a paragraph on a generalizing cadence. The final line is not philosophical. |
| 8 | Excessive parallelism | Trace | — | Folded into #3. |
| 9 | Overly smooth transitions | Clear | hinge 0 | "Halfway through the afternoon" (¶46), "Presently" (¶46) are concrete. |
| 10 | Described emotions | Clear | 0 | "She wanted no reply to that" (¶112) reads her want, not a feeling. |
| 11 | **Explanatory extension** | **FOUND: moderate** | 2 (0.78); under the commercial cap (>6 or >0.8/1k), just | "Letters came in two kinds, I thought, and either kind got read at once: the bad to be done with, and the good to be had." (¶44, the colon unpacks); "I knew it the way I knew the year of the Armada, as a date on a page with a fire in it." (¶64, keep: characterizing). The yawn's misreading (¶90) is designed irony, not counted. **−0.25** |
| 12 | Binary negation | Clear | 0 | "For the house there was no line" (¶122) is the subject, stated. |
| 13 | Precision flex | **FOUND: minor** | 1 (0.39) | "It was seven letters." (¶134): a count in a book that has retired counting; it also sits inside the P2 lift. **−0.125** |
| 14 | Emotional control demonstration | Trace | — | Kallia manages by work throughout; the yawn breaks it. Not a pattern. |
| 15 | Authoritative description | **FOUND: minor** | — | The packet in ¶6 described complete and certain before it is opened (also P1). Offsets: "somewhere near Homs" (¶94), "At that distance, in that hand, they could have been anything." (¶134), "It runs off, I suppose." (¶98). **−0.125** |
| 16 | Philosophical asides | **FOUND: minor** | 1 (0.39) | "Letters came in two kinds…" (¶44) is mug-ready. It is also Mara's all-or-nothing in miniature, so it earns its place once; continuity N-11 WATCH stands. **−0.125** |
| 17 | Clean dialogue | **FOUND: minor** | — | The gate exchange (¶18–¶40) and the reading Q&A run in clean alternation. Offsets: the horse-seller interruption (¶174), "Tell him," unfinished (¶182), two Kallia paragraphs running (¶100–¶102), Nikaso's torrent. **−0.125** |
| 18 | Thematic echo chamber | **FOUND: minor** | — | The end-weighting in Theme (a): blind, packet, lamps. Texture is ample. **−0.125** |
| 19 | Graduated reveal | Clear | — | A letter is read in its own order; the chapter's shape is the outline's *one reading, one afternoon*. |
| 20 | Emotional temperature report | Clear | 0 | |

**8 / 20 found (#1, #3, #11, #13, #15, #16, #17, #18). Total deduction −1.125.** Band: **CLEAN** (commercial 0–8), at its top; Ch.9's final was 7/20. Every finding is minor except #11, which is moderate and under the cap. The over-correction flag does not fire. **#11 hard check:** 2 at 0.78/1k, under the cap; P1's fix and Revision #12 do not add any.

---

## The book's own laws

- **NO FORESHADOWING (target 0): PASS, 0.** Gate 0; read by hand for families A–E. "He'll be home for the god's day, won't he?" (¶144) is Nikaso's wrong guess in speech; "will have been all round the stadium" (¶192) is a present inference; "Somebody going east would take it for a cup." (¶180) is conditional; "It was a good while yet till the lamps." (¶198) is the present afternoon. No 79, no Pompeii, no Italy, no reach toward Ch.11.
- **The HARD no-parallel rule: PASS, with two traces (WATCH).** No line in narration or speech compares Ariston's choice to Mara's. The repair removed both near-misses (the "cheerful letter" line; "For a week I had wanted it back"). Two faint traces remain and are left to the reader: (a) "since October" (¶72), her own arrival date, inside the sentence about speaking his words (P3's fix removes it); (b) the Homs postcard left in a returned library book (¶94), a thing of hers abandoned in a far place, now without the kicker that pointed it. Neither states anything. Do not add a third.
- **NO TICS, verbal (cast): PASS with WATCH items.** Kallia's "Then" retort 1 ("Then drink in Elis.", ¶28; cap). "living" ×5 in the chapter, ×3 in Kallia's mouth, designed; "cup" ×6, designed; close both. Kallia's name-asks ×2, closed. The Elean's "he said" relays cut to 2, as dialogue-polish left them.
- **NO TICS, narrator constructions: FAIL at the cycle-0 standard: P1–P7 (Prose).**
- **NO TICS, gestures:** no regex class charged to Ch.10 (bend/stoop 0, kneel 0, object handling 0 by the gate). By hand: Kallia's work-suspended tell at three expressive uses (Characters WATCH; P5 takes it to two). The letter is handled often (¶10, ¶44, ¶46, ¶50, ¶118, ¶122, ¶134, ¶188, ¶196), but it is the plot's object travelling hand to belt to hand to niche; ruled designed, not a fidget.
- **Retired reflexes:** no define-by-negation opener; one anaphora pair (¶158, P6), not a triad; no performed candour; no closing aphorism; no scene button (the broom closes ¶194, then the chapter goes on for two paragraphs).
- **Bible at-risk compliance, item by item:** gaze-arrival "then" 0 ✓. Hearthstone skeleton 0 ✓. Bend/stoop/lean-over 0 ✓ (the zero order is met). Hinge family 0 ✓. "So…" 0 ✓. "before I had…" 0 ✓. Command echo 0 ✓ ("Water," → "I filled the dipper at the jar."; "Keep it out of the smoke," → the cold niche, by result; "Put a plate on those" → "The one on top was the cracked one but it fit."). Stranger-freeze 0 ✓ (Kallia keeps spinning through Nikaso). Lying-awake coda 0 ✓. Laughs 0 ✓; the peak is not a laugh ✓. **Body-rebel channel:** hands rested ✓; face and eyes used (the yawn) ✓; **Mara's voice used, adjacent to the retired channel** (P9). Callback pointers: "As the Elean did." (¶180, in-chapter) and "He had found room for the old woman who slept between the baker and his wife" (¶122, Ch.8's song; audit N-10) — at the cap. Memory kicker 0 ✓ (the postcard ends on its object, then an act). The unprompted memory breaks into a sentence of the reading ✓, as the Ch.8 eval asked. "the one / the only" 0 ✓. "Whoever [made] it had" 0 ✓. Wiped hand 0 ✓. Cloth smells 0 ✓. Taste reactions 0 ✓. Kallia sits 0 ✓, touches Mara 0 ✓, kerchief-knot payment 0 ✓ (the obol comes from her belt). "said/told the [non-listener]" 1 ("She said it to the letter.", ¶118) ✓ at cap, but it is sample-09's frame (P11). **Held moment measured by indifferent traffic: SPENT, used twice** (P5). **Every document gets a forensic paragraph: not avoided** (P1). Gaze-arrival for Kallia: none ✓ (respect shown by what she does next: the obol on the stair).
- **Independent-read gates (author):** and-chains 1 (cap 9); credential asides 0 by the gate (by hand, one knowledge-provenance frame, ¶64); prop fidget none.
- **Ledger row:** approach ✓, open ✓, end ✓, breaks ✓, length ✓, dialogue ✓ (top of band; see the PATH note), theme ✓, gear ✓. **Beat subversion:** ✓. **Writer warnings:** no hook ✓; no aphorism at the end ✓; image-with-meaning at the end: the last paragraph is clean, the closing run is not (P7); no parallel in narration ✓.

### The ten points the orchestrator asked me to judge

**1. Mara's perfect reading as the instrument of the blow: LANDS, but its one explicit carrier is a spent frame.**
- The reading does the work itself: the formula read whole (¶52), the arm read before she can soften it (¶56), "I read the next part faster" when Kallia yawns (¶90), the voice carrying on through the oxen while her mind is at Van Pelt (¶94), and afterward "I could have left out the roof…" (¶158), the only place the narrator admits the choice she did not make.
- The line that states the non-negotiable outright, "It was the best Greek I had spoken since October, and it was his from beginning to end." (¶72), is the narrator's **speech ledger** in its fourth chapter (P3). The same fact can be shown through Kallia's established habit (Ch.7 ¶126: she corrects by saying the word back the town's way): "Kallia corrected none of it. The Greek was his, from beginning to end." That shows the reading is perfect without measuring it against Mara's months.

**2. Kallia's questions carrying "is he happy?" unspoken: YES. The best-written exchange in the chapter.**
- "Is she Greek?" / "Can she weave?" / "Anybody keeps a house." / "A roof you sit on," … "Where does the rain go?" / "They'll have enough." / "The man," … "Bought?" (¶74–¶102). Every one is a housekeeper's question. Nobody says happy or content, in speech or in a beat.
- Mara's evasions are hers: "The name told me nothing a Phocian would have wanted told." (¶76); "I ran my eye to the foot of the papyrus, looking for a loom." (¶80).
- "Bought?" asks whether her son has become a man who owns men, and leaves it there.
- "It's come, then, whichever it is." (¶110) is the one moment she reckons the grandchild, and she reckons it as a fact already done without her.

**3. "Ariston" said once: LANDS.**
- The name reaches the page only inside the letter's own first line (¶52) and once in Kallia's mouth (¶192). Mara's narration never says it; "Which is his name?" (¶132) makes it a shape on papyrus she cannot read before it is a word she says.
- It arrives as a possessive inside a rental: "He can have Ariston's room, at the three obols." The room becomes his in the same breath that it stops being his. That is the chapter's sentence.
- Information flow is clean (audit p3): Mara learns the shut room is his only here.

**4. The good news landing as bereavement: LANDS.**
- Nikaso supplies the joy the reader expects ("The gods be thanked." … "He'll be home for the god's day, won't he?", ¶144), and Kallia answers it flat: "He's living." (¶142), "He's married, in Syria, and there's a child." (¶150). The two registers side by side do the work; nobody explains.
- The reply she dictates is the inversion completed: news of who is still living at home, to a son who will not come to see them (¶184).
- The yawn (¶90) is the body's version of it, at the exact line where the grandchild's name leaves her house.

**5. The broom unexplained: YES.**
- The narration gives evidence, not reasons: "At dawn they had been swept already; I had been carrying out the ashes when she did them." (¶188); "nothing came over" (¶188); the broom laid back "the head against one post and the handle against the other" (¶188); "still lay over the threshold, from post to post" (¶194).
- No line says why. A reader of Ch.7 knows the morning rule; the mid-afternoon second sweep is the irrational act the outline asked for.
- *WATCH:* the beat order repeats Ch.7's closing broom section (Ch.7 ¶382–¶384: Mara below with water, Kallia sweeps the boards "out to the edge and over", the broom goes across, she comes down and speaks of something practical), and "lifted the broom off its boards" (¶188) is a near-string of Ch.7 ¶78 "borrowed it off those boards". It is the planted payoff and "nothing came over" answers Ch.7's dust shower exactly, so I rule it designed. Optional: "Kallia took up the broom and swept them." (pre-grepped clean).

**6. The ending as a true plain stop: PASS on the last paragraph; the closing run carries one weighted object (P7).**
- The last paragraph is plain: a chore resumed, a neighbor told where else to shake her blanket, the step in shade, "It was a good while yet till the lamps." No hook, no question, no aphorism, nothing withheld. The outline's "the afternoon going on" is literal.
- Two soft weights, both WATCH, not blocking: (a) the step, the basket and the knees all return from ¶46, so the scene is bookended (hook-craft named this reflex and the repair kept its nouns); (b) "a good while yet" is a time-remaining cadence, which in this book's clock can read as faint irony. Hook-craft rated this exact sentence 7 for plainness as a last line; I put it at 8.
- **The real weight is one paragraph up:** "I folded the papyrus, and it made a fatter packet than before." (¶196). The news will not fold back to the size it came in: an image doing meaning-work two paragraphs from a PLAIN STOP, and the last survivor of the sample-12 refold (P7).

**7. The new reed-blind beat: plain work in content, weighted by its placement. Not blocking; relocate it (Revision #13).**
- As work it is right: the first warm afternoon of the year (¶46), the summer blind let down between the water jar and the sun, "letting down a winter's soot and a dead wasp" (the wasp is the chapter's best piece of texture), "one-handed" implying the wool without a third wool beat. It is on her labor axis and it is not a gesture class.
- As placed, it falls at the exact moment the reading finds no line for the house (¶122–¶128), so it reads as a response. And **a blind let down at a death is a mourning custom an Anglophone reader recognizes** (drawing the blinds). Read that way it is an image with meaning, and it pre-empts the broom: the chapter now has two displaced-labor answers to one blow, sixty lines apart.
- Fix (word-neutral): move the paragraph to ¶46, after "…to work without a cloak." There it is pure seasonal work, the soot still precedes "Keep it out of the smoke", and the moment of the blow stands on stillness ("Kallia stood in the sun with the wool in her hand.") and the wool run back, which is enough.

**8. The horse-seller interruption: LANDS. Keep it.**
- "The horse-seller," Kallia said. "His name again." / "Iamblichos." / "And whoever carries it to Syria?" (¶174–¶178). It breaks the cleanest Q&A in the chapter, and it carries two readings without a gloss: practical (she will want the name for the reply) and grief (it is the name her grandson will carry instead of her husband's, ¶86–¶88).
- The disruptor's risk (that a reader who has forgotten "Here it's for the father's father" finds it random) is real for the Devourer and the Casual Reader, but the practical reading covers them, and the Critic gets the other. No explanation should be added.

**9. Any trace of the Ariston/Mara parallel: none stated; two faint traces (see the law above).** P3's fix removes "since October" from the sentence about his Greek. The postcard stays: it is the chapter's irrelevant thought, and without the kicker it points nowhere.

**10. Length: 2,563 against 2,800. Not thin; one beat is light by design.**
- Beat budget (audit): the wife carries ≈190 words against a 450 budget. It is the right weight: two questions and a deflection are what Kallia would ask, and padding them would turn subtext into catechism. Everything else is within a few dozen words of its budget.
- The PATH below nets about **−100 words, to ≈2,460**, under the writer's 2,500 range floor. STATE has no per-chapter floor and Ch.9 set the precedent: **do not pad.** The one place that would honestly take words, if the editor wants them, is the letter's wife paragraph (¶70): a single plain fact Kallia can seize on (what Shalmath's people grow, or whose gods she keeps) gives her one more practical question; nothing else.
- **Dialogue share after the PATH:** the cuts are narration, so the meter rises from 39% to about 40%. If shape_check reads over 40, keep the tunic sentence's first clause ("A lodger's tunic was drying on the rail above us.") rather than cut any speech.
- **Book total:** 54,333 against 57,800 cumulative (−6.0%), projecting ≈244.7k against the 245k target, ≈2.4k under after the PATH. The 220k floor is safe; flag the 245k target margin to the orchestrator (no chapter should be padded for it).

---

## Character Chaos Check (Primary: Mara)
- **Irrelevant thought: PRESENT, inhabited.** "Emesa was Homs. There had been a postcard of a crusader castle somewhere near Homs, a great tawny thing on a hill. I had used it as a bookmark in a library book on another subject entirely and returned the book across the desk at Van Pelt with the castle still in it." (¶94), breaking into the reading while her voice goes on.
- **Cognitive distortion: PRESENT, mediated.** "Letters came in two kinds, I thought, and either kind got read at once" (¶44): all-or-nothing as a rule she makes up and the afternoon disproves.
- **Unprompted memory: PRESENT.** The postcard (a 1998 object, no person; ends on its object).
- **Failed emotional management: PRESENT, inhabited.** The misread yawn and "I read the next part faster." (¶90): she hurries the reader's way through someone else's pain; and her wrong comfort, "He says the arm has knit," (¶124), reaching for the wound she can see.
- **Voice under pressure:** not tested (the pressure is Kallia's; Mara stays at level 0–1, correctly). No body rebel of Mara's own, by design (hands rested; voice retired until Ch.20, see P9).
- **4 / 4**, three inhabited.

## Secondary Character Chaos
- **Kallia:** the second sweep of swept boards (¶188); the Patrae man's bread given twice (¶44); the yawn (¶90); "The horse-seller… His name again." (¶174); the letter carried unread against her stomach for three hours (¶44).
- **Nikaso:** the flour on her lips (¶144); her sieve worry answered by herself, ending on blame (¶144); "He used to drop snails in my water jar." (¶148).
- **The Elean:** the seasickness he wants known (¶6, ¶38); the cup argued down to water (¶22–¶28).
- No secondary with 3+ appearances is a mere function. No cap.

---

## The Tomorrow Test
**What the reader remembers:** a woman standing in her court with a spindle, hearing that her son has a wife, a roof, oxen and a grandchild coming who will carry another man's name, and yawning, twice, enormously, with her eyes running, while the reader of the letter thinks she is tired. Then the same woman sweeping boards in front of a door she swept at dawn, laying the broom across it, putting on her good cloak and going out to rent the room to a stranger for three obols.
**Anchor type:** BOTH. IMAGE: the yawn; the broom across the threshold; flour on Nikaso's lips. QUOTE: "He can have Ariston's room, at the three obols."; "Tell him the baker's old mother is living."; "Which arm?"
**Verdict:** **ANCHOR EXISTS** (strong; +0.5 CVI). Type check: Ch.1 auditory, Ch.2 tactile, Ch.3 an act, Ch.4 a word heard, Ch.5 visual judgment, Ch.6 another's careful wrong act, Ch.7 olfactory, Ch.8 thermal and collective, Ch.9 touch withheld, **Ch.10 an object standing in a person's place, and a face** (new). No two consecutive anchors share a sense.

## The Shareability Test
"An illiterate landlady gets a letter from her soldier son, who's been gone two years. Her lodger reads it to her: he's alive, he's married, he's got land and a baby on the way in Syria, and he says hello to all the neighbors by name and nothing about home. She asks if the wife can weave, sends back word that the baker's old mother is still alive, and goes out and rents his room to a stranger." Running total: 10 chapters, 15+ shareable moments. On track.

---

## Reader Reports

### The Devourer (2.6k after Ch.9's 5.8k; the shortest chapter since Ch.4)
Reads the gate scene fast and grins at "Then drink in Elis." **Speeds up:** the reading (each paragraph of the letter is a little reveal), "Which arm?", Nikaso bursting in, "He can have Ariston's room." **Slows:** the belt hours (¶44, "why doesn't she just open it?" — which is the point), the Jerusalem/Armada line and the Homs postcard inside the reading ("wait, what's Van Pelt?"), the horse-seller beat ("who?"). **Would they stop?** At the end, yes, and they would not mind: the chapter is short, complete and sad, and Ch.9's wanted notice is still unresolved, so the book holds them even though this chapter does not pull. **Vibes:** "the mom one."

### The Critic
Underlines "a young man with a peeling scalp who had been sick on the boat from Aigion and wanted it known", "Her face gave him nothing for that.", "Then drink in Elis.", "Which arm?", "He was never any use with the left", "Two and a half. At the vintage.", "I ran my eye to the foot of the papyrus, looking for a loom.", "Anybody keeps a house.", the yawn, "Here it's for the father's father.", "Bought?", "It's come, then, whichever it is.", "Thrasyllos walked to Kirrha after him in his bare feet.", "For the house there was no line, nor for anything under its roof.", "Put a plate on those, or the mice will be in.", "The one on top was the cracked one but it fit.", "Tell him the baker's old mother is living.", "nothing came over", "He can have Ariston's room, at the three obols." Admires that the house was "full" at noon. **Disappointments:** the letter opened exactly as the curse tablet was opened last chapter ("folded, measured against her hand, the fastener worked out, the folds opened slowly with a simile, the lines of writing described: I've read this"); Kallia looking at the name "for the time it would have taken her to read it" ("that's Valens at the notice"); "the best Greek I had spoken since October" ("she keeps a ledger of her own speech: nineteen days, a month of mornings, since the guide"); "the way a woman in a crowd checks her purse" ("Nikaso and the pickpocket, two chapters ago"); the spindle turning and the tunic moving to measure a silence ("the cart, the car, the disc-buyer"); "I could have left out the roof. I could have left out…" ("rhetorical"); the fatter packet ("too neat"); the blind let down at the bad news ("a drawn blind; and the broom is coming").

### The Hostile
**Logic mostly holds after the continuity repair** (the consultation day no longer fixed; the auxiliary's savings, not a bounty; Shalmath, not Domna; Patrae). Challenges: (1) "Jerusalem had fallen that summer" (¶64): at narration time it is late winter AD 71, so "that summer" has no antecedent; and Ch.5 (¶201, ¶223) already had her hear the herald cry it in the square and date it herself, so "I knew it … as a date on a page" undersells what she heard; "the Temple" is capitalized here and lowercase in Ch.5. (2) The letter's timetable (20 Hyperberetaios at Emesa, on a Kirrha nail before the last ship) is tight but possible (audit N-03). (3) An obol for a sheet of papyrus in Greece is cheap (N-19). (4) "She looked at it from where she stood … for the time it would have taken her to read it if she could read" — how long is that, for a woman who cannot? (the P2 fix removes the question). **Verdict:** "No hole; one date that re-dates Ch.5."

### The Casual Reader (airport, 10 pages)
They like the sick pilgrim and the cup of water at once, and they like Kallia more than they did in any earlier chapter: she lies that the house is full, she won't open the letter, and then she asks if the wife can weave. "Which arm?" makes them laugh and then not. The yawn: half of them take it as tiredness, as Mara does, and the rest feel it; the broom and "Ariston's room" make it clear to everyone by the end. Nikaso's flour on her lips is the kind of thing they repeat. **Frictions:** the Jerusalem/Armada aside and the Homs/Van Pelt postcard (they skim both); the horse-seller line; no Valens. **Would they buy after 3 pages?** Yes: the gate scene is funny and the letter is a promise. **Do they stay with the chapter?** Yes, to the last line; it is short, warm and sad, and the quiet ending does not lose them. **8.5/10.** Not 9.0: the emotional center is a secondary character in a romance, the hero is absent for a second chapter running, and the yawn is subtle enough that some casual readers will miss the chapter's best beat.

### The Devoted Reader (active: long saga)
Will post about: the authentic Greek letter formula (πολλὰ χαίρειν, πρὸ μὲν πάντων, the daily proskynema "to the gods of this place"); Hyperberetaios and the Syro-Macedonian calendar; deposita ad signa and the missio causaria; the Orontes flowing north, so "below Emesa" is the right word; naming a son for the maternal grandfather in a sonless house; Ch.6's "Letters." asked while this letter hung on a nail at Kirrha; "Can you card wool? Weave?" (Ch.5) becoming "Can she weave?"; the girl and the son who both left "at the vintage"; the house that was "Full" at noon. **Will catch:** "that summer" and the Temple's capital; that the blind comes down exactly when the line for the house does not come; the letter opened in the curse tablet's steps.

---

## Cross-Reader Matrix
| Issue | Devourer | Critic | Hostile | Casual | Devoted | Severity |
|---|---|---|---|---|---|---|
| P1 the letter's arrival and opening on Ch.9's curse-tablet skeleton (¶6, ¶50) | | ✓ | | | ✓ | **SHOULD FIX → blocking** (scene skeleton, consecutive chapters; the bible's document-surface rule) |
| P2 Ch.9's reading-time measure (¶134) | | ✓ | ✓ | | ✓ | **IMPORTANT → blocking** |
| P3 the speech ledger, fourth chapter (¶72) | | ✓ | | | | **INVESTIGATE → blocking** (a fixed narrator move in 4 chapters) |
| P4 the pickpocket comparison reused (¶44) | | ✓ | | | ✓ | **SHOULD FIX → blocking** (voice-dna: no comparison twice) |
| P5 held silence by indifferent motion ×2 (¶112, ¶130) | | ✓ | | | | **INVESTIGATE → blocking** (SPENT family by name) |
| P6 sample-08's "I could have…" pair (¶158) | | ✓ | | | | **INVESTIGATE → blocking** (voice-bank lift: zero allowed) |
| P7 "a fatter packet than before" in the closing run (¶196) | | ✓ | | | ✓ | **SHOULD FIX → blocking** (PLAIN STOP closing run; sample-12 refold survivor) |
| Jerusalem "that summer" / re-dated (¶64) | ✓ | | ✓ | ✓ | ✓ | **IMPORTANT (3 of 4 core) → a one-line fix** (each stumbles for a different reason: skim, logic, skim; the Devoted catches the capital) |
| Reed blind placement (¶128) | | ✓ | | | ✓ | SHOULD FIX (word-neutral move) |
| Horse-seller line obscure | ✓ | | | ✓ | | SHOULD FIX → **no change** (the practical reading covers it; explaining would spend the subtext) |
| Hero absent a second chapter | ✓ | | | ✓ | | **VIBES WATCH → Ch.11 brief** (already the outline's plan: Valens's Yard) |

---

## Revision Recommendations (Ranked)

| # | Location | Problem type | What happens now | Why it fails | Revision direction | Project rule? |
|---|---|---|---|---|---|---|
| 1 | ¶6, ¶50 | Style (P1) | ¶6 "It was a strip of papyrus folded over and over on itself into a packet I could have closed my fist on. A thread went round it twice, sealed at the knot with a thumb of gray clay. One end had stood in wet somewhere and dried with a brown tidemark across it." ¶50 "The clay crumbled off the knot in one piece. I worked the thread loose with a thumbnail. The papyrus opened a fold at a time, stiff as a dried leaf, and lay over my palms in a strip the length of my forearm. The hand inside was small and level from top to foot." | **Ch.9 ¶278's curse tablet, step for step:** "It was a sheet of lead about the size of my palm, folded twice over and pierced through every layer with a bronze nail. It had lain in the mud till the creases went white. I worked the nail out and opened the folds slowly, because lead … tore like old cloth, and the writing was scratched in capitals …, every line running uphill at its end." Same six beats: "It was a [sheet/strip] of [material]" + a ruler from Mara's hand; folded n times; the fastener; the water damage; "I worked the [fastener] out/loose" and the folds opened with a material simile; the hand described by how its lines run. Also "in one piece" (Ch.9 ¶156). And it is the forensic document paragraph the Ch.9 eval asked Ch.10 to do without (Cross-Book #7 there). | Break the frame where it is identical; keep the outline's content (folded small, stained from the road). ¶6 s.3 → "**The papyrus had been folded over and over on itself until it was mostly creases.**" (−6; no ruler, no "It was a [material]"). ¶50 s.1–2 → "**The clay broke away from the knot whole, and the thread loosened under my thumbnail.**" (−2); s.3 → "…stiff as a dried leaf, **and covered both my palms.**" (−5; the forearm ruler goes, which also clears #10). Keep "The hand inside was small and level from top to foot." (N-18 needs it). All pre-grepped: 0 outside Ch.10 ("came off the" and "and lay across" were rejected: Ch.6, sample-08, Ch.1). | Yes: "**a set piece is compared beat-by-beat with the previous chapter's set pieces before the evaluator** (document arrival, reading, a look at a text)"; "document intro `\bIt was a (sheet|strip|scrap|square) of \w+\b` cap 1/book-section" |
| 2 | ¶134 | Style (P2) | "She looked at it from where she stood, without coming nearer, for the time it would have taken her to read it if she could read. It was seven letters. At that distance, in that hand, they could have been anything." | **Ch.9 ¶408, the notice:** Valens "stood with the gray's nose at his shoulder while a slow man might read it once, and then as long again." Same move one chapter later: the length of a (possible) non-reader's look at a text measured in reading-time. Ch.9's line is a preserved strength; this spends it. "It was seven letters." is also #13. | "**She looked at it from where she stood, and came no nearer. From there, in that hand, it could have been any name in Phocis.**" (−14). Pre-grepped: 0 outside Ch.10. | Yes: gate `\b(the time it would (have )?take[n]?|while a slow man might|as long as it (would take|takes)) [^.]{0,30}\bread\b` cap 1/book |
| 3 | ¶72 | Style (P3) | "It was the best Greek I had spoken since October, and it was his from beginning to end." | **The narrator's speech ledger** (her speech measured against a stretch of time), fourth chapter: Ch.6 ¶84 "I had spoken no Greek aloud since the guide on the Sacred Way."; Ch.7 ¶326 "It was the first word I had said outside her gate in nineteen days"; Ch.8 ¶456 "That was the whole of what I had said to her in a month of mornings."; here. Same frame as Ch.7: "It was the [first/best] [word/Greek] I had [said/spoken] [since/in] [time]". It also puts "since October" (her arrival; ×5 across Ch.6–10) into the sentence about his words: the parallel's nearest trace. | Show the perfect reading through Kallia's own habit (Ch.7 ¶126: she corrects by saying the word back): "**Kallia corrected none of it. The Greek was his, from beginning to end.**" (−5). Pre-grepped: 0 outside Ch.10 ("it back to me" rejected: Ch.6). | Yes: "speech ledger SPENT (Ch.6, 7, 8, 10)"; gate `\b(It was|That was) the (first|best|whole|only|last) [^.]{0,25}\bI had (said|spoken)\b` and `\bI had (said|spoken) no\b` cap 0 more; "since October" cap 1 more |
| 4 | ¶44 | Style (P4) | "Once she put her hand flat across it in passing, the way a woman in a crowd checks her purse." | **A comparison used twice:** Ch.8 ¶340 Nikaso "as wary of my hands as a market woman with a pickpocket in view". Same vehicle (a woman guarding her money from a thief in a crowd), applied to a Delphian woman's guarding gesture, two chapters apart; voice-dna §1: "no comparison is used twice in the book". The gesture half repeats Kallia's own Ch.5 ¶333 "the flat of her hand on top of her own kerchief" and Ch.7 ¶380's "put her hands flat on the blotter". | "**Once, going past the jar, she touched the place through her clothes.**" (−8; no simile; the chapter keeps two comparison frames). Pre-grepped: 0. | Yes: "simile-vehicle registry: a vehicle domain (pickpocket / purse / crowd-theft) is spent at its first use" |
| 5 | ¶112, ¶130 | Style (P5) / Character | ¶112 "The spindle hung at the end of its thread, turning a little one way and then the other."; ¶130 "A lodger's tunic was drying on the rail above us, and every so often it moved." | **The held moment measured by indifferent motion: SPENT** (bible after Ch.9: Ch.1 ¶373 the car, Ch.5 ¶193 the disc buyer, Ch.9 ¶412 the oil cart). Here twice, sixteen lines apart. ¶112 is also a use of Kallia's work-suspended tell (Characters WATCH: Ch.7 ¶182, Ch.9 ¶350, here ¶46, ¶112, ¶122, ¶126). | Cut ¶112's second sentence (−16): "She wanted no reply to that, and I made none." stands alone, and the silence is the reader's. ¶130: cut "**, and every so often it moved**" (−6) → "The chickpeas had gone warm in their basket. A lodger's tunic was drying on the rail above us." (a time marker, not a measure). If the dialogue meter then reads over 40%, keep ¶130 whole and cut only ¶112. | Yes: "held silence measured by an indifferent motion (traffic, a hanging thing turning, cloth stirring): SPENT book-wide"; gate `\b(every so often|now and then|a little one way and then the other)\b` WATCH |
| 6 | ¶158 | Style (P6) | "I could have left out the roof. I could have left out the father with no son of his own, and read the wife as so much talk about rain. There was not a soul in that court or in that lane who could have told the difference." | **Voice-bank sample-08, by structure:** "I could have said a hundred things. I could have told him the truth, which would have got me … I unbuckled my father's watch instead". The anaphoric pair of counterfactual speech plus "could have told". voice-dna §6: no sentence, image or line from any sample may be reused; the bible: samples leak by structure. The bible's own Ch.10 note logged it as a "two-plus-one shape" without its source. | One sentence, no anaphora, the content kept: "**Nobody in that court or in that lane could have caught me if I had read the roof as so much talk about rain, and left out the father with no son of his own.**" (−13). Pre-grepped: 0 outside Ch.10. | Yes: gate `(?s)\bI could have \w+[^.]{0,80}\.\s+I could have\b` cap 0 |
| 7 | ¶196 | Style (P7) / Pacing (plain stop) | "Before I folded it I read it once more, without moving my lips, from the greeting down to the date. I folded the papyrus, and it made a fatter packet than before." | **A weighted object in the PLAIN STOP's closing run:** the news will not fold back to the size it came in (the disruptor's own note calls it "an object fail[ing] where she does not"). It is the **object-weight-as-feeling** move (Ch.1 ¶383 the cassette "weighed less than the cake had"; Ch.9 ¶350 the rag "weighed very little"), the **refold-and-stow** of Ch.2 ¶145 and sample-12 ("folded it along its old creases … small enough"), "fatter" from Ch.9 ¶8, and the reading-lips beat inverted (Ch.5 ¶113, Ch.9 ¶308 "His lips were moving"). | "**I read it once more to myself, from the greeting down to the date, and folded it.**" (−13). The niche and the cumin follow unchanged. If the re-read itself feels like Ch.9 ¶402's ("I read it through again."), cut to "I folded it." | Yes: "object weight/size as the unspoken feeling at a section close: SPENT (Ch.1, 9, 10)"; gate `\b(weighed (less|very little|nothing)|(fatter|thinner|smaller|bigger) (packet|bundle|parcel) than)\b` |
| 8 | ¶194 | Style (P8) | "The gate came to behind her and bounced once. Her shoes receded over the stones at the pace she used for the spring." | **Composure shown by an unchanged gait, two chapters running** (Ch.9 ¶404 Valens "at his ordinary pace", ¶412 "at a walk"); an exit by footwear (Ch.7 ¶358 "watching the backs of her shoes"; Ch.7 ¶218 Valens's "boots took themselves off down the lane"); and an in-chapter double with Nikaso's receding voice two paragraphs earlier ("We heard her at the next gate, and the one after, and fainter at the bottom", ¶156). | Cut the second sentence (−14). The gate bouncing once and the broom are enough: "The gate came to behind her and bounced once. Up at the last door the broom still lay over the threshold, from post to post." | Yes: "composure-gait exit (`at (his\|her) (ordinary\|usual\|own) pace`, `the pace (she\|he) used`) cap 1 per 3 chapters" |
| 9 | ¶94 | Style / Voice (P9) | "My voice went on through the oxen without me." | Mara's voice acting apart from her is the voice channel the bible retired for Ch.10 by name ("Ch.10's body break uses another channel (and not her voice, which is retired until Ch.20)"), and "voice went on" is a near-string of Ch.5 ¶325's voice failure ("The voice went on me there."). Continuity N-17 ruled it a different channel; I rule it adjacent, and the string settles it. | Keep the dissociation, move it off the voice: "**The oxen went by while I was still at that desk.**" (0). Pre-grepped: 0. | No |
| 10 | ¶46, ¶50 | Style (repair-made) | "held it toward me across the wool at the length of her arm" (the repair's W-07) four lines before "a strip the length of my forearm" | An in-chapter double created by a repair (editor rule after Ch.9: "a repair that adds a phrase is grepped against the chapter it repairs"); three body-rulers in the first 50 lines (fist, arm, forearm). | Cleared by #1 (the forearm goes). Keep "at the length of her arm" (she never touches Mara; the distance is character). | Yes (restate): the repair-grep rule applies to the continuity repair as well as the editor |
| 11 | ¶118 | Style (sample-09) | "She said it to the letter. I raised it for her." | sample-09's frame, "He said it to the window" (exact 4-gram "said it to the"); the bible's "said/told the [non-listener]" cap is met but the frame is the sample's. | "**She was answering the letter, and I raised it for her.**" (−1; "not me" rejected: the SPENT "not on me" tail). Pre-grepped: 0. | No |
| 12 | ¶64 | Logic / Continuity | "Jerusalem had fallen that summer, and the Temple with it, burning. I knew it the way I knew the year of the Armada, as a date on a page with a fire in it." | "that summer" has no antecedent in late winter; "the Temple" against Ch.5's "temple" (¶201, ¶223); Ch.5 already had the herald cry it and Mara date it from Josephus (¶223), so this is the second provenance aside on one event. | "**Jerusalem had fallen in the summer just gone, and its temple with it, burning.**" (+2). Keep the Armada sentence: after the herald, a date on a page is still all it was to her, until a stone broke a man's arm. Pre-grepped: 0. | No |
| 13 | ¶128 → ¶46 | Emotion / Theme | The reed blind let down at the moment the letter has no line for the house. | Placement makes plain work read as a drawn blind (a mourning sign) and gives the blow two displaced-labor answers, sixty lines before the broom. | Move ¶128 whole to follow "…to work without a cloak." in ¶46 (word-neutral; the soot still precedes "Keep it out of the smoke"). The moment at ¶122–¶126 stands on stillness and the wool run back. | Yes: "**one displaced-labor act per blow**; a second goes elsewhere in the chapter as plain work" |
| 14 | ¶198 | Style (sample-12; WATCH) | Last paragraph: legume chore resumed; an offstage domestic complaint; the step and basket from ¶46. | The repair re-ordered and re-nouned sample-12's last two slots (beans → chickpeas; the goat complaining → the neighbor's blanket) rather than removing them; the step/basket/knees bookend ¶46. Acceptable here (the outline mandates "the afternoon going on" and sample-12 is this chapter's register), **not acceptable again**. | No change in Ch.10. **Ch.31, 34 and 44 (the other no-pull chapters) must not stop on a chore resumed, an offstage complaint, or an object put away.** | Yes: "no-pull closes: the act sequence of the last three paragraphs is compared with sample-12's and with Ch.10's" |
| 15 | ¶188 | Style (optional) | "Kallia lifted the broom off its boards and swept them." | Near-string of Ch.7 ¶78 "borrowed it off those boards"; the beat order follows Ch.7 ¶382–¶384. Ruled the designed payoff. | Optional: "**Kallia took up the broom and swept them.**" (−2). Pre-grepped: 0. | No |
| 16 | character-bible.md | Bookkeeping | The Ch.10 blocks still quote cut or changed lines (audit W-09, pending): Domna (now Shalmath); "Everywhere has rain"; "with a cast in her eye from his kiln"; "There'll be a child by now."; "Go and stand him one…"; "There's the lamps to fill…"; "He writes as one who is content there"; "Shall I go up and open it?"; "My eyes ran a line ahead of my voice…"; "In the lane my Greek arrived in single words…"; "To myself it was a cheerful letter…"; "She put the letter inside her belt"; "I found a plate."; "Patrai"; "a palm on the papyrus"; the spent-wording list's "at its slant". | Ch.11–16 writers and Dialogue Polish work from these blocks; a stale spent list mis-counts (the written-vs-spoken contrast is at 2 on the page, not 3). | Sync all Ch.10 blocks to the final page by script after the PATH. Add to at-risk: every "Project rule? Yes" item above; "living" and "cup" CLOSED; Kallia's name-ask CLOSED at 2; the yawn SPENT; spindle as Kallia's stage business WATCH for Ch.11–16. | No |
| 17 | Pipeline | Style (systemic) | Ten of ten cycle 0s held by narrator recurrence; this cycle the two heaviest are skeletons lifted from the previous chapter. | No gate compares a chapter's set pieces with the last chapter's; the comparison registry does not exist; voice-bank structural checks are by hand. | Root (UPDATE RULE): (a) **previous-chapter skeleton check** in the continuity guardian's checklist: list each set piece's beat order (arrival of an object, a reading, a look, an exit) and compare with Ch.N−1's; (b) a **simile-vehicle registry** in `tic_report.py` (vehicle nouns per comparison, flagged on a second chapter); (c) the regexes in #2, #3, #5, #6, #7, #8; (d) a **sample slot check** for the chapter's assigned calibration sample (sample-12 for no-pull chapters): the last three paragraphs' act verbs against the sample's. | Yes (UPDATE RULE: root) |

### Fix order: Logic (#12) → Prose/law (#1–#8) → second uses (#9–#11) → placement (#13) → optional (#15) → watch (#14) → Bookkeeping/Pipeline (#16, #17)

---

## Strengths to PRESERVE (do not touch in polish)
1. **The first sentence, byte-identical:** "The letter had been folded down very small." (`short-punch`). The tidemark sentence stays (the outline's "stained from the road").
2. **The gate (¶8–¶42):** the Elean's route speech and "he said" relays; "Kallia had it out of his fingers and held it shut in her hand."; "Where from?"; "Her face gave him nothing for that."; the dipper "with the rest still in it"; **"That was a cup." / "In Elis a cup has wine in it." / "Then drink in Elis."**; "Full." / "The house is full."; the Corinthian's goat; "Behind her the gallery was hung with other people's cloaks."
3. **The belt hours (¶44)**, apart from #4: "She pushed the letter down behind her belt, against her stomach, and returned to the pots."; the corner showing when she reached for the oil; **the Patrae man's bread "twice over; he took it twice and kept his mouth shut"**; "Letters came in two kinds…" (once; WATCH).
4. **The reading (¶46–¶122)**, apart from #3/#5/#9/#12/#13: "You read the clerk's wax,"; the formula byte-identical; "There's gods enough here,"; **"Which arm?" / "The left." / "He was never any use with the left,"**; "Forgive me the two years." / **"Two and a half," … "At the vintage."**; the wife paragraph; "The name told me nothing a Phocian would have wanted told."; **"I ran my eye to the foot of the papyrus, looking for a loom."**; "Anybody keeps a house." and the fine thread; **"Here it's for the father's father."**; **the yawn (¶90) byte-identical**; the roof and land paragraph; "Emesa was Homs." and the postcard; "A roof you sit on," / "They'll have enough." / "Bought?" / "It says only a man." / "The middle of winter's gone by." / **"It's come, then, whichever it is."**; the greetings and **the neighbor-news answer, byte-identical**; "I raised it for her"; the farewell and the address; **"For the house there was no line, nor for anything under its roof."**; "Kallia stood in the sun with the wool in her hand."
5. **The wrong comfort and its answer:** "He says the arm has knit," / "She drew a fresh pull of wool from the hank, and let it run back."
6. **The reed blind paragraph's text**, byte-identical, wherever it goes (#13): the slip-knot, "one-handed", **"a winter's soot and a dead wasp"**.
7. **"Which is his name?"** and the fingertip; "Keep it out of the smoke,".
8. **Nikaso (¶138–¶156):** "with flour on her hands and her black hair half out of its pins"; **the flour on her lips**; the sieve worry; "Me? He remembers me?"; **"He used to drop snails in my water jar."**; "a grandson in Syria"; "I'll stand him two,"; the news going down the lane gate by gate.
9. **The reply (¶160–¶186):** "Put a plate on those, or the mice will be in." to "How old was he, when he went?"; **"The one on top was the cracked one but it fit."** (ugly sentence, missing comma kept); "On what?"; **the horse-seller interruption**; "And whoever carries it to Syria?"; "Tell him," and the yarn wound up; **"Tell him the baker's old mother is living."**; the obol "on the bottom stair, where I would have to pass it." / "For the sheet."
10. **The sweep (¶188), apart from optional #15:** "At dawn they had been swept already; I had been carrying out the ashes when she did them."; **"in short strokes, and nothing came over, and back to the door"**; "the head against one post and the handle against the other".
11. **¶190–¶192 byte-identical:** the good himation "kerchief and all"; **"That Elean will have been all round the stadium by now," … "He can have Ariston's room, at the three obols. If he comes to the gate before I find him, he waits in the court."**
12. **"Up at the last door the broom still lay over the threshold, from post to post."** (the anchor) and the niche "where Kallia kept the good knife and a twist of cumin".
13. **The last paragraph byte-identical** (`quiet`, 9-word last sentence): it is a true plain stop.

---

## PATH TO 8.5 (mandatory; the Floor is 8.0)

**Prose & Voice 8.0 → 8.5 requires removing P1–P7 and nothing else.** The stopping sentences (¶90, ¶192, ¶184), the underlines, the ugly sentence and the plain stop already exist. Execute in this order. Every edit is to narration, so dialogue share rises slightly (see the note).
1. **Logic first (Revision #12):** ¶64 "in the summer just gone, and its temple with it".
2. **P1, the curse-tablet skeleton (Revision #1):** ¶6 sentence 3; ¶50 sentences 1–3 as written there.
3. **P2, the reading-time measure (Revision #2):** ¶134 as written there.
4. **P3, the speech ledger (Revision #3):** ¶72 "Kallia corrected none of it. The Greek was his, from beginning to end."
5. **P4, the purse (Revision #4):** ¶44 "Once, going past the jar, she touched the place through her clothes."
6. **P5, the held silences (Revision #5):** cut ¶112's spindle sentence; trim ¶130's last clause.
7. **P6, sample-08 (Revision #6):** ¶158 to one sentence.
8. **P7, the packet (Revision #7):** ¶196 "I read it once more to myself, from the greeting down to the date, and folded it."
9. **Second uses (Revisions #8, #9, #11):** cut the shoes sentence (¶194); "The oxen went by while I was still at that desk." (¶94); "She was answering the letter" (¶118).
10. **Placement (Revision #13):** move the blind paragraph to ¶46.
11. **Optional:** #15.
12. Re-run `bash books/the-hour-of-ash/tools/check_chapter.sh 10` and `python3 tools/shape_check.py books/the-hour-of-ash` (¶6's first sentence and ¶198 must stay byte-identical: `short-punch` → `quiet`). Grep every replacement against Ch.1–9 and the voice bank. **Pre-checked here, all 0 outside Ch.10:** "until it was mostly creases", "broke away from the knot whole", "the thread loosened under my thumbnail", "and covered both my palms", "came no nearer", "any name in Phocis", "Kallia corrected none of it", "going past the jar", "touched the place through her clothes", "could have caught me", "read the roof as", "I read it once more to myself", "The oxen went by while I was still at that desk", "She was answering the letter", "in the summer just gone", "its temple with it", "Kallia took up the broom". **Do not use:** "came off the" (Ch.6, sample-08), "and lay across" (Ch.1), "in one piece" (Ch.9 ¶156), "it might have been" / "word at all" (Ch.9), "it back to me" (Ch.6), "would have known" (Ch.6), "her eyes were on" (Ch.8), "not me" (the SPENT "not on me" tail), "read it through" (Ch.9 ¶402), "the flat of her hand" (Ch.5), "two fingers" for Kallia (Ch.8 ¶28).

**Word count after the PATH:** about −100, ≈2,460 (under the 2,500 range floor; no per-chapter floor in STATE; do not pad). **Dialogue share:** ≈40%; if shape_check reads above 40, keep ¶130 whole. With items 1–10 applied and nothing else changed I would expect **Prose 8.5, Floor 8.5, Average 8.57, Casual 8.5 held** (9.0 is arguable once the blind no longer competes with the broom and the closing run is plain). Do not touch Strengths #1, #4's yawn and neighbor-news answer, #9, #11, #12, #13.

---

## Pacing check (one line for `feedback/progress.md`)
Ch.10: 2,563w (target 2,800, −8.5%, inside 2,500–3,100; book 54,333 vs 57,800 cumulative, −6.0%, ≈244.7k projected vs the 245k target, ≈2.4k under after the PATH: flag, do not pad; 220k floor safe) · dialogue 39% (30–40 ✓, top of band; ≈40 after the PATH) · 0 breaks ✓ · gear mid, median 15 ✓ · single-scene between a collage and a chronological chapter ✓ · gate brisk / belt hours slow / reading held then quickened / Nikaso a burst / sweep slow ✓ · value shift −− for Kallia ✓ · `short-punch` / `quiet` (9w), multi-sentence close ✓ · **PLAIN STOP honored (first of the author's four)**: no hook, no aphorism, last paragraph plain; one weighted object in the closing run (P7) · hook SENSORY 7 by design · hinge 0 ✓ · peak not a laugh ✓. **Verdict: OK.**

---

## Cross-Book Pattern Detection (Ch.1–10)
1. **The recurrence fingerprint is ten for ten, and this time it comes from next door.** Ch.1–5 were held by phrases, Ch.6 by a pivot, Ch.7 by moves, Ch.8 by a relocated hinge, Ch.9 by stop-word frames and skeletons. Ch.10's two heaviest items are set pieces copied from **the chapter just finished** (Ch.9's curse-tablet opening; Ch.9's reading-time look). The writer reads the previous chapter last, and its strongest moves come through. Pipeline: Revision #17(a).
2. **The narrator's speech ledger** (her own speech measured against elapsed time): Ch.6 ¶84, Ch.7 ¶326, Ch.8 ¶456, Ch.10 ¶72; "since October / November" ×5 across Ch.6–10 as her private clock. SPENT.
3. **The held silence measured by something indifferent moving:** Ch.1 ¶373 (car), Ch.5 ¶193 (disc buyer), Ch.9 ¶412 (cart), Ch.10 ¶112 (spindle) and ¶130 (tunic). SPENT.
4. **An object's weight or bulk standing in for the feeling at a section's end:** Ch.1 ¶383 (the cassette "weighed less than the cake had"), Ch.9 ¶350 (the rag "weighed very little"), Ch.10 ¶196 (the "fatter packet"). SPENT.
5. **Every document gets a forensic paragraph on its making:** Ch.1, 2, 7, 9 ×3, 10. Ch.20 and Ch.26 must each let one document stand bare.
6. **Kallia's work-suspended tell:** Ch.7 ¶182, Ch.9 ¶350, Ch.10 ×3. With spinning on the page ×6 here, it is close to becoming her stage signature. Her farewell (Ch.16) must not use stopped work or wool.
7. **Exits rendered by gait or footwear:** Ch.7 ¶218 (boots), Ch.7 ¶358 (the backs of her shoes), Ch.9 ¶404/¶412 (ordinary pace, at a walk), Ch.10 ¶194.
8. **Voice-bank leakage by structure is now the main source:** sample-12's closing slots survived the repair by reordering; sample-08's counterfactual pair arrived whole; sample-09's "said it to the [object]". The sample assigned to a chapter's register is the riskiest. Ch.31, 34 and 44 (no-pull) are next in line for sample-12.
9. **One comparison used twice** (pickpocket/purse, Ch.8 → Ch.10): the first breach of the "no comparison twice" rule since the gates were built. A vehicle registry is cheap.
10. **Repairs keep creating second uses inside the chapter they repair:** Ch.9 cycle 1 (the bending recasts), Ch.10's continuity repair ("at the length of her arm" four lines before "the length of my forearm"). The repair-grep rule must cover every agent that edits.
11. **What varies, as it should:** openings (`short-punch`, the second; not adjacent to Ch.4's), endings (`quiet`, after Ch.9's `punch`), structure (single scene between a collage and a chronological), length (the shortest since Ch.4), the anchor (an object in a person's place, and a face), the body-rebel channel (face and eyes, as ordered; hands rested), the peak (not a laugh, as ordered), dialogue 39% (the book's highest so far), the first plain stop. Shape audit CLEAN. Every Ch.9 at-risk item obeyed by name except the two SPENT families in #3 and #5.

---

## VERDICT
**POLISH.** Genesis Floor **8.0** (Prose & Voice) | Average **8.50** | Casual **8.5** | CVI-Launch **9.3** | CVI-Legacy 6.6 (provisional) | foreshadowing **0** | no-parallel rule **held** (two faint traces, one removed by P3) | NO-TICS: the cast is clean apart from WATCH items (Kallia's work-suspended tell, "living" ×3 in her mouth, the cup; all to be closed after Ch.10); **seven narrator-law items P1–P7** (two skeletons from Ch.9, the speech ledger, a reused comparison, a SPENT held-silence family ×2, a sample-08 lift, a weighted object in the closing run) | gesture classes uncapped | AI patterns 8/20 (clean, top of band) | mechanical suite all clean, echo scan 0, hinge 0, shape CLEAN | ledger ✓ on every field | beat subversion ✓ | Mara's reading as the instrument ✓ (its explicit carrier is a spent frame) | Kallia's questions carry the unasked question ✓ | "Ariston" once ✓ | good news as bereavement ✓ | the broom unexplained ✓ | the plain stop ✓ on the last paragraph | the reed blind: plain work, weighted by placement (move it) | the horse-seller interruption ✓ (keep) | not thin; do not pad | pacing **OK**.

**Top fixes (one editor cycle):** (1) the letter's arrival and opening off Ch.9's curse-tablet frame (¶6, ¶50); (2) Kallia's look at the name off Ch.9's reading-time measure (¶134); (3) "Kallia corrected none of it." for the speech ledger (¶72); (4) the purse simile out (¶44); (5) the spindle and tunic measures out (¶112, ¶130); (6) the sample-08 pair to one sentence (¶158); (7) the fatter packet out of the closing run (¶196); then "that summer" (¶64), the shoes (¶194), the voice line (¶94), the letter answered (¶118), and the blind moved to ¶46. Then E (gates) and F (re-evaluation).

This is the book's best secondary-character chapter: a woman who answers the news that her son is alive, happy and gone by asking whether his wife can weave, yawning until her eyes run, sending word that the baker's mother is still living, and renting his room to the man she turned away at noon. What holds it, again, is the narrator's own habit, this time borrowed from the chapter before.

**BIAS CHECK:** This evaluation was produced by the same system that wrote the prose. Confidence in every score at or above 8.5, in Emotion 9.0, in Casual 8.5 and in CVI-Launch 9.3 requires external validation (beta readers, editors, comp analysis). Prose is held at 8.0 to the standard that held Ch.1–9 in cycle 0. Several items here (P1's six-beat skeleton, P5's family of indifferent motions, P6's structural kinship with a voice-bank sample) are judgments about shape rather than strings, and a reader could fairly call them a strict bar; they are held because each reproduces a move the bible names as SPENT, a sample the rules say may not be reused, or a sentence from the immediately preceding chapter. P2 (the reading-time measure) and P4 (the comparison used twice) would hold the floor on their own. Casual 8.5 assumes a romance reader who is patient with a second chapter without the hero; a reader who misses the yawn could put it at 8.0, which would fail the gate, so the PATH's #13 (the blind moved, leaving the yawn and the broom unrivalled) matters for Casual as well as for Emotion. CVI-Launch 9.3 is a one-chapter formula and is not a book forecast.

---

## RE-EVALUATION — polish cycle 1 (2026-10-19)
**Evaluator:** book-evaluator (independent; did not write or revise this prose) | **Text:** `manuscript/chapters/chapter-10.md` after book-editor cycle 1 (`evaluations/revision-chapter-10-cycle1.md`, 17 entries). **2,446 prose words** (shape_check), 2,457 by style_check, 2,624 by `wc -w` (incl. header). Target 2,800 (−12.6%). That is 54 words under the writer's 2,500 range floor. STATE has no per-chapter floor, so it is not a defect. Do not pad.
**Read against:** the cycle-0 evaluation above (every P item, Revision row and Strength); the revision log; Ch.9 ¶278 and ¶408 (the two skeletons P1/P2 lifted); Ch.5, 7 and 8 for every changed sentence; all 13 voice-bank samples. Every changed sentence was 3/4/5-gram scanned against Ch.1–9 and the samples with a scratch script, then checked in-chapter by hand. Every replacement string I prescribe below was **applied to a scratch copy of the book folder and run through the real gate suite**, so none of them should trip a gate. Git was not run and the manuscript was not touched. **¶N = line number in the revised file.** The ¶46 split and the blind's move shift cycle-0 numbers: **+4 from cycle-0 ¶46 to ¶126** (the formula ¶56, Jerusalem ¶68, the yawn ¶94, the postcard ¶98, the address ¶126, "He says the arm has knit" ¶128, the wool ¶130), then **+2 from cycle-0 ¶130 on** (the tunic ¶132, the name ¶136, Nikaso ¶140–¶158, the counterfactual ¶160, the reply ¶162–¶188, the sweep ¶190, the close ¶194–¶200).
**Measured here, not taken from the log:** `bash books/the-hour-of-ash/tools/check_chapter.sh 10` (run from /home/user/Books): **every gate is clean.**
- Style: 2,457w, simile 0.4/1k, adverb 3.7/1k, em-dash 0, **foreshadow 0**.
- Grammar 0. Rhythm 0 flagged. Show/tell: no flags (37.6%).
- Voice-wear strict: clean.
- 5a tic gate: clean. Ch.10: and-chains 1/9, credential asides 0, negation pivots 0, 'So' openers 0, no gesture class charged.
- 5c echo scan: 0. Command echo: none.
- Metaphor: fig 0.4/1k, 1 simile, median 15, 0% over 40 words.
- Shape: CLEAN. Ch.10 is `short-punch` → `quiet`, 0 breaks, **dialogue 40% (raw 990/2,446 = 40.47%)**, median 15. Book: 54,216 words over 10 chapters.
- **Band headroom correction:** the log says about 3 narration words of headroom. It is **1**. At 990 quoted words the meter rounds to 40 down to 2,445 words and to 41 at 2,444.

### PATH items, verified one by one
| PATH item | Now | Verdict |
|---|---|---|
| 1 Logic: ¶64 → ¶68 | "Jerusalem had fallen in the summer just gone, and its temple with it, burning." | **CLEARED.** The date has an antecedent, and the lowercase "temple" matches Ch.5. The Armada sentence is kept, as ruled. |
| 2 P1 the curse-tablet skeleton (¶6, ¶54) | ¶6 "…wanted it known. One end had stood in wet somewhere and dried with a brown tidemark across it. The thread round its middle was knotted under a thumb of gray clay." ¶54 "The clay broke from the knot at the first push, and the thread slid off over the end. Unfolded, the papyrus was mostly creases and needed both my hands to keep it flat. The hand inside was small and level from top to foot." | **CLEARED.** Every identifying mark of Ch.9 ¶278 is gone: the "It was a [sheet/strip] of [material]" opener, the palm/fist/forearm rulers, "worked [x] out/loose", the slow fold-by-fold opening and the material simile. "in one piece" is 0. **What is left** (a stain, a fastener, an unfolding, the hand) is what any sealed travel-letter has. It is split across two places 48 lines apart, in a new order, and its only shared words are "creases" (×1 each) and "wet" (Ch.9 "lain in wet ground"; Ch.10 "stood in wet somewhere", in the tidemark sentence I preserved as Strength #1). The editor's Concern #2 is answered: it reads as its own beat. "both my hands to keep it flat" is the chapter's best new tactile fact. |
| 3 P2 reading-time measure (¶134 → ¶136) | "She looked at it from where she stood, and came no nearer. From there, in that hand, it was any name in Phocis." | **CLEARED.** "the time it would have taken" and "seven letters" (#13) are 0. |
| 4 P3 speech ledger (¶72 → ¶76) | "Kallia corrected none of it. The Greek was his, from beginning to end." | **CLEARED, and better than I forecast.** It lands four lines after "Two and a half," … "At the vintage.", so the reader has just watched her correct the letter. She corrected the length of his absence and none of his wife. Ch.7's correcting habit (¶126) is the re-read reward. "since October" is gone from the sentence about his words, which removes the nearest trace of the parallel. |
| 5 P4 purse comparison (¶44) | "Once, going past the jar, she touched the place through her clothes." | **CLEARED.** The pickpocket/purse vehicle and the flat hand are 0. *Trace:* the passing-touch frame occurs once before, in Ch.5 ¶5 ("I touched the hub as I went by"). That is Mara, five chapters back, in different words. No change. |
| 6 P5 held silences (¶112 → ¶116; ¶130 → ¶132) | ¶116 "She wanted no reply to that, and I made none." stands alone. ¶132 is unchanged: "…and every so often it moved." | **¶116 CLEARED.** The silence now belongs to the reader, and Kallia's work-suspended tell is down to two expressive uses (¶126, ¶130). **¶132 was kept by my own cycle-0 conditional**, so it is not charged to the editor or to the floor. It is ruled below (point 2). |
| 7 P6 sample-08 pair (¶158 → ¶160) | "Nobody in that court or in that lane could read a word, and I might as easily have made the roof into so much talk about rain and left out the father with no son of his own." | **CLEARED.** The anaphora, the 2+1 shape and "could have told" are gone; "could have" in Ch.10 is 0. #3 is cleared with it. One logic snag is new (N3 below). |
| 8 P7 the fatter packet (¶196 → ¶198) | "I read it once more to myself, from the greeting down to the date, and rolled it up." | **CLEARED.** No size, no weight, no refold, no lips. The closing run is now plain from the gate's bounce to the last line. |
| 9 #8 shoes exit (¶194 → ¶196) | "The gate came to behind her and bounced once. Up at the last door the broom still lay over the threshold, from post to post." | **CLEARED.** The gait/footwear exit and the double with Nikaso's receding voice are gone. The anchor now follows the bounce directly, which is better. |
| 10 #9 voice channel (¶94 → ¶98) | "The oxen went by while I was still at that desk." | **CLEARED off the voice channel** ("voice went on" is 0). **But my own string has two faults on the page** (N4 below). |
| 11 #11 sample-09 (¶118 → ¶122) | "She was answering the letter, and I raised it for her." | **CLEARED.** "said it to the" is 0. |
| 12 #13 the blind moved (→ ¶48) | The text is byte-identical, between "…and spun." and "I sat on the step…". | **CLEARED in function.** It now reads as the first warm afternoon's work, before anyone has read a word. The blow at ¶126–¶130 stands on stillness and the wool run back, and the broom is the chapter's only displaced-labor answer. Concern #3 is answered: it responds to nothing. **The move created N2** (below). |
| 13 #10 body-ruler double | — | **CLEARED by #1** (the forearm is gone; "at the length of her arm" is kept). |
| ENTITY CH10-5 (¶140) | "It was Nikaso, from along the lane, …" | **CLEARED.** It is consistent with Ch.8 ¶30 "Midway along the lane". The shared 3-gram is geography, not an echo. |

**All seven law items P1–P7 are cleared** (P5 to the extent my conditional asked), along with the logic item, #8, #9, #11, #13 and the entity fix. Every cycle-0 string I quoted as a defect now greps 0 in Ch.10.

### The editor's departures from my strings
| ¶ | My string → editor's | Ruling |
|---|---|---|
| ¶198 (fix 7) | "…and folded it." → "…and rolled it up." | **ACCEPT; better.** "and folded it" was sample-12's refold, the exact slot P7 removed, and I missed that. Rolling an opened papyrus is a different act and carries no size. *Trace:* "rolled" ×2 in the chapter (¶48 the blind "hung rolled up"; ¶198). 150 lines apart and a different object. No change. |
| ¶140 (CH10-5) | "from down the lane" → "from along the lane" | **ACCEPT.** Mine tripped voice-wear and the echo scan (Ch.7 ¶218 "down the lane with"). |
| ¶136 | "it could have been any name in Phocis" → "it was any name in Phocis" | **ACCEPT; better.** The flat statement is Mara's knowledge of what Kallia sees, and it takes a "could have" out. "from where she stood … From there" re-anchors on purpose. Keep. |
| ¶160 | "could have caught me if I had read the roof as…" → "could read a word, and I might as easily have made the roof into so much talk about rain…" | **ACCEPT; better.** "made the roof into so much talk about rain" now has an in-scene referent: Kallia did exactly that ("A roof you sit on," … "Where does the rain go?"). The Devoted reader gets it. The new premise clause needs one word (N3). |
| ¶54 | "broke away from the knot whole … the thread loosened under my thumbnail … and covered both my palms" → "broke from the knot at the first push … slid off over the end … mostly creases and needed both my hands to keep it flat" | **ACCEPT, all of it.** Each of my strings had a trap he names (Ch.1's thumbnail, "into a long", "than it had looked"). "mostly creases", moved from my ¶6 string to the opening where the folds are, is better placed. |
| ¶6 | my "The papyrus had been folded over and over on itself until it was mostly creases." → cut; stain before fastener; "round its middle" | **ACCEPT** the reorder; the first sentence already says "folded down very small". It created N1's antecedent blip (below), which costs two words to fix. |
| ¶48 (the blind) | "after '…to work without a cloak.'" → two sentences later, after "…and spun." | **ACCEPT.** "She came back to her place." needs the place set up first, and "one-handed" needs the spindle in her hand. The cost is N2's doublet, a word-neutral fix to ¶46 that leaves the blind's text byte-identical. |

Fifth cycle running: the editor caught my prescriptions tripping gates or samples, and four of his departures (¶198, ¶136, ¶160, ¶54) read better than my strings.

### Ruling on the trade-off: the dialogue band against the spent tunic
**The spent move matters more, and the band does not have to lose.**
- **The band is a pacing-design target.** Its purpose (a talk-forward chapter, 30–40%) is met at 39.9% or at 40.5%. No reader can see the difference between the meter rounding to 40 and rounding to 41.
- **The held silence measured by an indifferent motion is reader-visible.**
  - The Critic named it in cycle 0, and the family was declared SPENT after Ch.9 (car, disc buyer, cart).
  - With ¶116's spindle gone, the tunic is now the **only** beat between the wrong comfort ("He says the arm has knit,") and "Which is his name?". That is the chapter's most exposed silence, so it is where the move is most visible, not least.
- **It is not charged to the floor.** The editor kept it on my written conditional ("if shape_check reads above 40, keep ¶130 whole"). Holding the floor on it now would move the goalposts.
- **The narration to replace it.** Cut ", and every so often it moved" (−6). That leaves exactly what cycle 0 sanctioned as "a time marker, not a measure": "The chickpeas had gone warm in their basket. A lodger's tunic was drying on the rail above us."
  - **Do not fill the slot with another clause.** Anything that moves, drips, steams or casts a shadow there is the same family again. A static detail about the tunic invites a reading as the absent son's clothes.
  - **Put the six words where the text needs them:**
    - ¶98 "The oxen **and the man to drive them** went by while I was at that desk." (+5 net). This fixes N4.
    - ¶6 "One end **of it** had stood in wet…" (+2). This fixes N1.
    - ¶160 "Nobody **else** in that court…" (+1). This fixes N3.
  - With the ¶44 recast (−1) and the ¶46 recast (0), **the set nets +1: 990/2,447 = 40.46%. That is in band, with 2 words of headroom instead of today's 1.**
  - The whole set was run through `check_chapter.sh` on a scratch copy: style, grammar, rhythm, show/tell, voice-wear strict, tic gate, echo scan 0 and shape CLEAN.
  - **Do these together.** Any one of them alone moves the meter.

### Did the cycle introduce anything?
- **N0. Pattern #11 now crosses the commercial density cap.** This is a measurement consequence; the cycle added no instance.
  - Cycle 0 found 2 instances at 0.78/1k (2,563w): ¶44 "Letters came in two kinds, I thought, and either kind got read at once: the bad to be done with, and the good to be had." and ¶68 "I knew it the way I knew the year of the Armada, as a date on a page with a fire in it."
  - Both remain. The cycle cut 117 words, so the same 2 now sit at **0.82/1k (2/2.446k; 0.81 by style_check's 2,457)**. That is over the hard check's commercial line (">6 instances OR >0.8/1k → cap Prose at 7.5").
  - Cycle 0 wrote "P1's fix and Revision #12 do not add any". That checked the numerator and not the denominator, and it is my error. The rule is labelled HARD and the evaluator "MUST catch it", and Ch.9 cycle 1 applied the gesture cap at its exact threshold. **I apply it: Prose is capped at 7.5, 8.5 on merit.**
  - **The fix is one sentence (PATH 1).** It is ¶44, the sentence cycle 0 already counted three times (#1, #11, #16). The Armada sentence stays (an underline; kept by Revision #12).
- **N1. The ¶6 antecedent (trace, made by the reorder).** "…a young man … who had been sick on the boat from Aigion and wanted it known. One end had stood in wet somewhere…". The nearest nouns are the boat and the young man, so "One end" reads for a beat as the boat's. Before the cycle, "It was a strip of papyrus…" sat in between. Fix: "One end of it" (+2), which is part of the band set.
- **N2. "beside the lean-to, where the hearth was…" (¶46) → "She went to the front of the lean-to, where a reed blind hung…" (¶48)** (trace, made by the move). Two consecutive sentences, across a paragraph break, each "She [verb] … the lean-to, where …". The Critic hears it. Fix ¶46, not the preserved blind: "beside the lean-to **that held the hearth** and all the kitchen the house had" (word-neutral; "that held the" and "lean-to that" are 0 in Ch.1–9 and the samples).
- **N3. ¶160 "Nobody in that court … could read a word"** (logic trace, made by the recast). The narrator, the one reader, is in that court. The old "not a soul … could have told the difference" implied "but me" more softly. Fix: "Nobody else" (+1; "Nobody else in" is 0).
- **N4. ¶98 "The oxen went by while I was still at that desk."** (my cycle-0 string, two faults now visible on the page):
  - (a) "still" ×2 in adjacent sentences ("with the castle still in it. … while I was still at that desk").
  - (b) After a paragraph about a library, "The oxen went by" can be read for a beat as real oxen in a Delphi lane. The Hostile and the Casual reader both catch it.
  - Fix: "The oxen **and the man to drive them** went by while I was at that desk." This makes them the letter's own oxen. The man who drives them because Ariston cannot is a dry, sad thing to have pass by unheard. It drops "still" and adds 5 narration words.
  - **Do not use "while I was back at that desk"**: "I was back at" fails voice-wear strict against Ch.2 ¶15 "On Monday I was back at work" (tested). Do not use "while I stood at": it would be the chapter's seventh "stood".
- **Echo/n-gram scan of every changed sentence against Ch.1–9 and the voice bank:** the only two hits are generic. "read it once" (Ch.9 ¶408's "might read it once", in pre-existing ¶198 text; a different sense) and "along the lane" (Ch.8 geography). 5c echo scan: 0.
- **Pre-existing traces, not made by the cycle, no change:** "Once more she went over them" (¶190) / "I read it once more" (¶198); "had stood in wet" against Ch.9 ¶278 "had lain in wet ground" (the preserved tidemark sentence).
- **Tics:** no verbal tic and no refrain. Kallia's "Then" retort 1; "living" ×5 and "cup" ×6 are unchanged and designed (both CLOSED after Ch.10). Name-asks 2 (closed).
- **Gestures:** no class charged. Kallia's work-suspended tell is at 2 expressive uses, as cycle 0 asked.
- **Spent moves:** none added. The single surviving SPENT item is the tunic clause, ruled above.
- **Parallel law:** cleaner than cycle 0. "since October" is gone from the sentence about his words, and the postcard trace stands without a kicker.
- **Strengths: none damaged.** Checked on the page, all intact:
  - The first sentence and the last paragraph, byte-identical.
  - The gate exchange.
  - The Patrae man's bread.
  - The formula.
  - "Which arm?" / "He was never any use with the left,".
  - "Two and a half," … "At the vintage."
  - "looking for a loom".
  - **The yawn, byte-identical.**
  - "Here it's for the father's father."
  - "Emesa was Homs." and the postcard.
  - "Bought?" / "It's come, then, whichever it is."
  - The neighbor-news answer, byte-identical.
  - "For the house there was no line…"
  - The wrong comfort and the wool run back.
  - The blind's text, byte-identical.
  - Nikaso, whole.
  - The reply, ¶162–¶188, whole (the ugly sentence included).
  - The sweep ("nothing came over").
  - ¶192–¶194, byte-identical.
  - The broom anchor.

### Anti-AI re-scan (2.45k; commercial band)
| # | Result | Count, density | Note |
|---|---|---|---|
| 1 | FOUND minor | 1 (0.41) | ¶44 "the bad to be done with, and the good to be had" (unchanged) **−0.125** |
| 3 | **CLEAR** | 0 | the ¶158 2+1 anaphora is gone (cycle 0: −0.125) |
| 7 | **CLEAR** | 0 | the "could have told the difference" cadence is gone |
| 11 | **FOUND moderate; OVER THE CAP** | 2 (0.82) | ¶44 (colon unpack), ¶68 (Armada extension) **−0.25**; caps Prose 7.5 (N0) |
| 13 | **CLEAR** | 0 | "seven letters" is cut (cycle 0: −0.125) |
| 15 | trace | — | ¶6 is now two short facts; "mostly creases" is an impression, not an inventory (cycle 0: −0.125) |
| 16 | FOUND minor | 1 (0.41) | ¶44 "Letters came in two kinds…" (unchanged) **−0.125** |
| 17 | FOUND minor | — | the gate and reading Q&A, unchanged **−0.125** |
| 18 | trace | — | blind and packet cleared; only "It was a good while yet till the lamps." is left (WATCH, unchanged; I rated it 8 for plainness in cycle 0) (cycle 0: −0.125) |
| 2, 4, 5, 6, 8, 9, 10, 12, 14, 19, 20 | clear | — | "Kallia corrected none of it. The Greek was his…": the second sentence states whose words they are and does not unpack a comparison. Trace at most; not counted under #11. |

**4/20 found (cycle 0: 8/20). Total −0.625 (cycle 0: −1.125).** CLEAN band (commercial 0–8). The over-correction flag does not fire. **#11 hard check: 2 at 0.82/1k, OVER the >0.8/1k cap → Prose capped at 7.5.** After PATH 1 the count is 1 at 0.41/1k (minor), and #1 and #16 clear with it: **2/20 (#11, #17), −0.25.**

### Genesis Score — cycle 1
| Dimension | Cycle 0 | Cycle 1 | Evidence | Holds |
|---|---|---|---|---|
| Originality | 8.5 | **8.5 (holds)** | All eight inventions are intact (the yawn, "Which arm?", the neighbor news, "father's father", the cup, "The house is full.", the horse-seller, the bread twice). | The beat subversion is the outline's. Not raised. |
| Theme | 8.5 | **8.5 (holds)** | Hold (a), the weight gathering at the end, is two-thirds cleared: the blind is now plain seasonal work (¶48) and the fatter packet is gone (¶198). "Kallia corrected none of it." (¶76) adds a quiet theme beat: she corrects the time he was gone and nothing about the life he chose. | "a good while yet till the lamps" remains (WATCH). Clearing defects is not a 9.0 lever. Not raised. |
| Characters | 8.5 | **8.5 (holds)** | The cycle-0 WATCH is answered: Kallia's work-suspended tell is at 2 expressive uses (¶126, ¶130). Her Ch.7 correcting habit now carries the perfect reading (¶76). Cover-the-name PASS. Mara chaos 4/4, three inhabited: the postcard still breaks into the reading, the ¶44 all-or-nothing rule and the misread yawn are intact, and the wrong comfort is unchanged. | Not raised. |
| **Prose & Voice** | 8.0 | **7.5 (CAPPED; 8.5 on merit)** | **On merit +0.5 to 8.5.** P1–P7 are all cleared (table above: 7 cited changes, far past the three a +0.5 needs). Stopping sentences intact (¶94 the yawn, ¶194, ¶186). **New underlines:** "Kallia corrected none of it. The Greek was his, from beginning to end." (¶76); "From there, in that hand, it was any name in Phocis." (¶136); "Unfolded, the papyrus was mostly creases and needed both my hands to keep it flat." (¶54); "I might as easily have made the roof into so much talk about rain" (¶160). The ugly sentence is intact (¶168). Anti-AI −1.125 → −0.625. | **#11 hard check: 2 instances at 0.82/1k, over the commercial cap** (N0). The cap is mechanical, and the chapter's shrinkage tripped it, not any addition. It lifts on PATH 1. N1–N4 are traces and are not counted against merit. |
| Pacing | 8.5 | **8.5 (holds)** | Hold (a) is cleared: the Jerusalem line has its antecedent (¶68). The plain stop's closing run is now plain from the gate's bounce on (¶196–¶200). Ledger ✓ on every field (`short-punch` → `quiet`, 0 breaks, 40%, median 15). Value shift −− for Kallia, intact. | The two narrator excursions inside the reading (¶68, ¶98) remain, as designed. Not raised. |
| Emotion | 9.0 | **9.0 (holds)** | Both cycle-0 holds are cleared: the closing run no longer carries a weighted object (¶198), and the blind no longer pre-empts the broom (¶48). The broom now follows the gate's bounce directly (¶196). Anchor, the three-way surprise, ≥6 techniques and the yawn as body rebel are intact. | **Not raised to 9.5.** That needs the best-in-class tier, and the yawn's subtlety still loses some casual readers. Held at 9.0, with the cycle-0 BIAS note. |
| Immersion (Dim 7) | 8.5 | **8.5 (holds)** | "needed both my hands to keep it flat" adds touch to a narrow sensory range. "its temple" is consistent with Ch.5. #15 is down to a trace. | The narrow sensory range is unchanged. Not raised. |
| **FLOOR** | 8.0 | **7.5** (Prose, capped) | **8.5 on merit** | |
| **AVERAGE** | 8.50 | **8.43** (59.0 / 7) | **8.57 on merit** (60.0 / 7) | |

**Cross-check of neighbors:** no dimension rose more than 0.5 on merit. Theme, Pacing, Emotion and Immersion cleared holds without a raise. **The floor stayed on Prose and moved from content (P1–P7, cleared) to a density cap that the cuts themselves tripped.** The number is lower than cycle 0 and the chapter is better. Both are true, as in Ch.9 cycle 1.

### Pacing check (one line for `feedback/progress.md`)
Ch.10 (cycle 1): 2,446w (target 2,800, −12.6%; 54 under the writer's range floor; no per-chapter floor in STATE; book 54,216 vs 57,800 cumulative, −6.2%, ≈244.2k projected against the 245k target: flag, do not pad; 220k floor safe) · dialogue 40% (raw 40.47; 30–40 ✓; 1 word of headroom, 2 after the PATH) · 0 breaks ✓ · gear mid, median 15 ✓ · single scene between a collage and a chronological chapter ✓ · gate brisk / belt hours slow / reading held then quickened / Nikaso a burst / sweep slow ✓ · value shift −− ✓ · `short-punch` / `quiet` (9w) ✓ · **PLAIN STOP honored, and the closing run is now plain too** ✓ · hinge 0 ✓. **Verdict: OK.**

### Readers (deltas only)
- **Devourer:** no change in speed. The blind no longer reads as a signal, so the broom is the one thing they carry out. A beat of "what oxen?" at ¶98 (N4). Would not stop.
- **Critic:** every cycle-0 disappointment is gone except one: "the tunic stirring to measure the silence, still". Will underline "Kallia corrected none of it." and "it was any name in Phocis." **New snags:** "the lean-to, where … the lean-to, where" in consecutive paragraphs (N2); "Letters came in two kinds" is still a coffee-mug line (N0 / PATH 1).
- **Hostile:** the Jerusalem date holds and the letter's opening is its own. **New:** "'Nobody in that court could read a word': she's in the court, reading" (N3); "'One end' of the boat?" (N1). Verdict: "Logic holds; two loose pronouns."
- **Casual (8.5, holds):** the blind and the packet were things they never consciously noticed. Removing them leaves the yawn, "Ariston's room" and the broom unrivalled, which makes the chapter's ending clearer to them. **Not raised:** the cycle-0 reasons are unchanged (the emotional center is a secondary character, the hero is absent for a second chapter, and the yawn is subtle). **Would buy; stays to the last line.**
- **Devoted:** will add "Kallia corrected none of it" four lines after "Two and a half", and the roof she herself turned into rain talk.

### CVI
**CVI-Launch:** Commercial Pacing 8.0 × .2 (the two excursions in the reading remain) + Tomorrow 6 anchors → 10 × .2 + Casual 8.5 × .2 + Shareability 7.5 × .2 + Concept 10 × .1 + Human Closeness 10 × .1 = 8.8, **+0.5 strong anchor = 9.3** (unchanged). **CVI-Legacy:** 8.5 × .30 + 8.5 × .25 + 2 × .20 + 7 × .15 + 5 × .10 = **6.6** (provisional, unchanged). Divergence: none by rule (9.3 − 7.5 = 1.8; on merit 0.8).

### Cross-reader matrix (cycle 1)
| Issue | Dev | Crit | Host | Cas | Devo | Severity |
|---|---|---|---|---|---|---|
| N0 #11 at 0.82/1k (¶44, ¶68) | | ✓ | | | | **BLOCKING by the hard check** (PATH 1, one sentence) |
| ¶132 tunic "every so often it moved" (SPENT family, 1 left) | | ✓ | | | ✓ | SHOULD FIX (ruling above; PATH 2, band-neutral set) |
| N4 ¶98 "The oxen went by" (literal reading; "still" ×2) | ✓ | | ✓ | ✓ | | **IMPORTANT (3 of 4 core)**, my own string; PATH 2 |
| N3 ¶160 "Nobody … could read a word" | | | ✓ | | ✓ | INVESTIGATE (PATH 2, +1 word) |
| N1 ¶6 "One end" antecedent | | ✓ | ✓ | | | SHOULD FIX (PATH 2, +2 words) |
| N2 ¶46/¶48 "the lean-to, where" ×2 | | ✓ | | | ✓ | SHOULD FIX (PATH 3, word-neutral) |
| "Once more" (¶190) / "once more" (¶198) | | ✓ | | | | trace (optional F1) |
| Hero absent a second chapter | ✓ | | | ✓ | | carried → the Ch.11 brief (unchanged) |

### VERDICT — cycle 1
**POLISH.** Genesis Floor **7.5** (Prose, capped by the #11 hard check; **8.5 on merit**) | Average **8.43** (**8.57 on merit**) | Casual **8.5** | CVI-Launch **9.3** | CVI-Legacy 6.6 (provisional) | pacing **OK** | mechanical suite all clean (run here; echo 0, shape CLEAN) | foreshadowing **0** | no-parallel rule held, cleaner than cycle 0 | **all seven narrator-law items P1–P7 cleared**, plus #8, #9, #11, #12, #13 and CH10-5 | AI patterns 4/20 (clean band), but #11 density 0.82/1k is over the cap. **Gate: Floor ≥ 8.5 ✗ (7.5) AND Casual ≥ 8.5 ✓ AND pacing OK ✓ AND gates clean ✓.** One sentence holds the gate. The cycle added nothing to it: the chapter got shorter around it.

## PATH TO 8.5 (cycle 2; one floor-holding sentence plus a band-neutral set)
**Prose 7.5 (capped) → 8.5 requires #11 at ≤0.8/1k, which means one of its two instances removed, and nothing else.** Items 2 and 3 clear this cycle's residue and my trade-off ruling. They do not hold the floor, but they share the band arithmetic with item 1, so do them in the same pass. **The whole set below was applied to a scratch copy of the book and passed `check_chapter.sh 10` and shape_check (dialogue 990/2,447 = 40.46%, 2 words of headroom).**
1. **¶44 (floor-holding):** `Letters came in two kinds, I thought, and either kind got read at once: the bad to be done with, and the good to be had.` → `Whatever was in a letter, I thought, a person read it at once, standing at the door it came to, and the pots could wait.` (−1w).
   - This removes #11's colon-unpack, #1's symmetric pair and #16's coffee-mug line in one stroke.
   - It keeps Mara's all-or-nothing rule (the chaos marker), and the afternoon still disproves it: Kallia took this one at the gate and "returned to the pots". The repeat of "the pots" is the point. Leave it.
   - Pre-checked 0 in Ch.1–9 and the samples: "Whatever was in", "a person read", "the door it came", "at once, standing".
   - **Do not use** "before anything else" (Ch.8).
   - Keep the Armada sentence (¶68): an underline, kept by Revision #12.
2. **The band-neutral set (ruling on the trade-off; N1, N3, N4). Apply all four or none:**
   - ¶132: `…on the rail above us, and every so often it moved.` → `…on the rail above us.` (−6). Add nothing in its place.
   - ¶98: `The oxen went by while I was still at that desk.` → `The oxen and the man to drive them went by while I was at that desk.` (+5).
     - **Do not use** "while I was back at" (fails voice-wear strict against Ch.2 ¶15, tested) or "while I stood at" (a seventh "stood").
   - ¶6: `One end had stood in wet somewhere…` → `One end of it had stood in wet somewhere…` (+2). The rest of the tidemark sentence stays verbatim.
   - ¶160: `Nobody in that court…` → `Nobody else in that court…` (+1).
3. **¶46 (N2):** `She stood in it beside the lean-to, where the hearth was and all the kitchen the house had, and spun.` → `She stood in it beside the lean-to that held the hearth and all the kitchen the house had, and spun.` (0). The blind paragraph (¶48) stays byte-identical.
4. Re-run `bash books/the-hour-of-ash/tools/check_chapter.sh 10` and `python3 tools/shape_check.py books/the-hour-of-ash`. Expect 2,447 words and dialogue 40%.
   - The first sentence and the last paragraph must stay byte-identical (`short-punch` → `quiet`).
   - Grep: `Letters came in two kinds` 0; `every so often` 0; `could have` 0; `lean-to, where` 0.

**With 1–3 applied and nothing else changed, I expect Prose 8.5 (the cap lifts; merit as judged above), Floor 8.5, Average 8.57, Casual 8.5 held → PASS.** The cycle-2 re-evaluation needs only to confirm these seven lines, the gate run and the #11 count (1 at ≈0.41/1k). Everything else was verified above. Do not touch any strength listed under "Did the cycle introduce anything?".

**Optional finalize fixes (not required for the gate):**
- **F1 ¶198:** `I read it once more to myself` → `I read it over again to myself` (0w). This breaks the "Once more" (¶190, Kallia's re-sweep) / "once more" (¶198, Mara's re-read) pairing, which a careful reader could take as a pointed rhyme, and drops the Ch.9 "read it once" 3-gram. "read it over" is 0. **Re-check the meter after it.**
- **No change:** "rolled" ×2 (¶48, ¶198); "from where she stood … From there" (¶136); the passing touch (¶44) against Ch.5 ¶5; "a good while yet till the lamps" (WATCH, as ruled in cycle 0).

**Bookkeeping (orchestrator):** sync the character-bible Ch.10 blocks to the final page (cycle-0 Revision #16, still pending), plus this cycle's lines:
- "Kallia corrected none of it."
- "it was any name in Phocis"
- "made the roof into so much talk about rain"
- "rolled it up"
- "from along the lane"
- after the PATH: the ¶44 belief, the oxen and the man, "Nobody else"

**At-risk entries for Ch.11 on:**
- Held silence measured by an indifferent motion: SPENT, **0 more anywhere**. Ch.10's tunic is removed by the PATH; if the author keeps it, it is the last.
- Speech ledger: SPENT.
- Object weight or size at a close: SPENT.
- "X corrected none of it": once.
- Kallia's work-suspended tell: her farewell (Ch.16) must not use stopped work or wool (carried).

**Pipeline (UPDATE RULE, root):**
- (a) **The #11 hard check needs a word-count guard.** At 2.4k words, two instances cross 0.8/1k. A chapter can therefore fail by being cut, and a short chapter can never carry the two keepers a long one can. Either set a minimum instance count before the density cap applies (for example, density only from the 3rd instance in chapters under 3k), or keep the rule as written and have the editor's log report the #11 density after cuts. **Until the author rules, I apply it as written.**
- (b) The editor's band-headroom figure should be computed, not estimated: the raw quoted/total ratio and the word count at which it rounds over. Here it was 1 word, not 3.
- (c) Cycle-0 carry-over: the previous-chapter skeleton check, the simile-vehicle registry and the regexes in Revisions #2, #3, #5–#8 are still to be built (cycle-0 Revision #17).

**BIAS CHECK:** This evaluation was produced by the same system that wrote the prose. Confidence in every score at or above 8.5, in Emotion 9.0, in Casual 8.5 and in CVI-Launch 9.3 requires external validation from beta readers, editors or comp analysis.
- **The 7.5 is a rule-bound cap, not a judgement that the prose got worse.** On merit Prose is 8.5: every item that held cycle 0 is gone.
- A reader could fairly call the cap legalistic. Its trigger is 0.02/1k over the line, its cause is the chapter getting shorter, and one of the two instances (the Armada) is a keeper. It is held because the rule is labelled HARD, Ch.9 cycle 1 applied the gesture cap at its exact threshold, and the fix is one sentence that also clears #1 and #16. **If the author rules that #11 density applies only from a third instance in chapters under 3k words, the floor is 8.5 today and the chapter passes as it stands, tunic and all.** The band-neutral set would then be finalize work.
- Casual 8.5 is unchanged and still rests on a reader catching the yawn. A reader who misses it could put Casual at 8.0, which would fail the gate. This cycle's moves (the blind and the packet out of the broom's way) make that less likely, not more.
- CVI-Launch 9.3 is a one-chapter formula and is not a book forecast.

---

## RE-EVALUATION — polish cycle 2 (confirmation, 2026-10-19)
**Evaluator:** book-evaluator (independent; did not write or edit this prose). **Text:** `manuscript/chapters/chapter-10.md` after the orchestrator applied cycle-1 PATH items 1–3 verbatim, plus optional F1. I did not touch the manuscript and did not run git. **2,447 prose words** by shape_check, 2,458 by style_check and 2,650 by `wc -w` including the header. ¶N = line number in the current file.

### 1. The PATH lines, on the page
| Item | On the page | Verdict |
|---|---|---|
| PATH 1, ¶44 | "Whatever was in a letter, I thought, a person read it at once, standing at the door it came to, and the pots could wait." | ✓ verbatim. "Letters came in two kinds" now greps 0. |
| PATH 2, ¶132 | "The chickpeas had gone warm in their basket. A lodger's tunic was drying on the rail above us." | ✓ The clause is cut and nothing fills the slot. "every so often" greps 0. |
| PATH 2, ¶98 | "The oxen and the man to drive them went by while I was at that desk." | ✓ "still at that desk" greps 0. |
| PATH 2, ¶6 | "One end of it had stood in wet somewhere…" | ✓ The rest of the sentence is verbatim. |
| PATH 2, ¶160 | "Nobody else in that court or in that lane could read a word…" | ✓ |
| PATH 3, ¶46 | "She stood in it beside the lean-to that held the hearth and all the kitchen the house had, and spun." | ✓ The ¶48 blind is byte-identical. "lean-to, where" greps **1**, and that 1 is the preserved blind sentence itself. My cycle-1 grep target of 0 was wrong. The doublet (N2) is gone. |
| F1, ¶198 | "I read it over again to myself, from the greeting down to the date, and rolled it up." | ✓ (see the trace under point 3) |
| Signatures | The first sentence and the last paragraph are byte-identical. Shape reads `short-punch` → `quiet`. | ✓ |

### 2. Pattern #11 re-count
- **1 instance:** ¶68 "I knew it the way I knew the year of the Armada, as a date on a page with a fire in it." This is the keeper.
- **Density:** 1 / 2.447k = **0.41/1k** (0.41 at style_check's 2,458). That is under the commercial >0.8/1k cap and far under the >6 count. **The hard-check cap on Prose lifts.**
- **Checked and not counted:**
  - ¶44's new sentence states Mara's belief in concrete terms. It is not a comparison with an unpacking extension.
  - ¶88 "so fine it could hardly hold the spindle up" is a result clause.
  - ¶150 "as if it might say so again" is a bare simile.
  - ¶76 and ¶136 remain traces, as ruled in cycle 1.
- **Anti-AI total:** 2/20, both minor: #11 (0.41) −0.125 and #17 −0.125, for **−0.25**.
  - #1 and #16 cleared with ¶44. The new sentence is a belief the afternoon disproves, tied to "the pots", so it is not a coffee-mug line.
  - #15 and #18 stay at trace.
  - This is the CLEAN band. The over-correction flag does not fire.

### 3. Anything new? (echo, tic, spent move)
- **Mechanical:** the echo scan is 0, command echo is none, voice-wear strict is clean, and the tic gate is clean. Ch.10 has 1 and-chain, 0 credential asides, 0 negation pivots and no gesture class charged.
- **Hand n-gram check:** I checked every new string against Ch.1–9 and the voice bank. All of these are 0: "Whatever was in", "a person read", "the door it came", "at once, standing", "the pots could", "could wait", "read it over", "that held the", "lean-to that", "the man to drive", "at that desk", "Nobody else in", "One end of it".
- **In-chapter counts:**
  - "at once" ×1.
  - "the pots" ×2, which is designed: ¶44 sets it up and the afternoon disproves it.
  - "stood/standing" 5/1, unchanged except for the new "standing", which is the only one in its paragraph.
  - "held" now has four senses spread over 50 lines. No pairing.
- **¶98 → ¶106 is a gain, not an echo.** The narrator lets "the man to drive them" go by unheard, and eight lines later Kallia picks him up ("The man. Bought?"). The reader sees that she caught what Mara missed. Keep it.
- **Spent moves:** none. The held-silence-by-indifferent-motion family is now **0 in Ch.10**. The ¶132 time marker is static.
- **Logic:** the ¶6 "it" resolves to the letter (sentence 2's subject); "One end" of a sickness is not a live reading. ¶160 is fixed.
- **One trace, from my own optional F1 string (not charged):**
  - ¶198 "I read it over again to myself" is closer than the old "once more" was to **Ch.9 ¶402 "I read it through again."** That is the same narrator, the same act and a "I read it [particle] again" frame, one chapter back.
  - It also sits eight lines after ¶190's "Once more she went over them … over the threshold again", so the over/again rhyme with Kallia's re-sweep has moved rather than gone.
  - Mara re-reading the letter here is the same beat that cycle 0 and cycle 1 passed. Only the wording moved closer, and the echo scan does not register it. **Not charged to the floor.** See the finalize option below.
- **Book-wide WATCH (not Ch.10):** the bend/stoop gesture class is at 15 uses, **0.28/1k against the 0.3/1k book-wide cap**. Ch.10 has none, but Ch.11 onward has almost no room for it.

### 4. Gate run (from /home/user/Books)
`bash books/the-hour-of-ash/tools/check_chapter.sh 10` → **all clean**:
- Style: 2,458w, simile 0.4/1k, adverb 3.7/1k, em-dash 0, foreshadow 0.
- Grammar 0. Rhythm 0 flagged. Show/tell: no flags (37.6%).
- Voice-wear strict: clean. Tic gate: clean. Echo 0. Metaphor: fig 0.4/1k, 0% over 40 words.
- Shape: CLEAN.
- **Dialogue:** quoted 990 / prose 2,447 = **40.458%**, and shape_check reports **40%**. The meter rounds to 41 at 2,444, so there are **2 words of headroom**.

### Genesis Score — cycle 2 (final)
| Dimension | Cycle 1 | Cycle 2 | Evidence |
|---|---|---|---|
| Originality | 8.5 | **8.5** | Unchanged. All inventions intact. |
| Theme | 8.5 | **8.5** | Unchanged. ¶44's rule is now plainly a belief the afternoon overturns (Kallia "returned to the pots"). |
| Characters | 8.5 | **8.5** | Mara's all-or-nothing distortion is kept in the new ¶44. Chaos is 4/4. Cover-the-name PASS. NO-TICS clean. No gesture class charged. |
| **Prose & Voice** | 7.5 (capped; 8.5 on merit) | **8.5** | The #11 cap lifts at 0.41/1k. The +1.0 is the cap lifting onto the cycle-1 merit score, backed by six cited changes: ¶44 (clears #11, #1 and #16), ¶132, ¶98, ¶6, ¶160 and ¶46. Stopping sentences are intact (¶94 the yawn, ¶186, ¶194). Anti-AI is −0.25. **Not raised past 8.5:** the cycle adds no new close-book sentence. |
| Pacing | 8.5 | **8.5** | Ledger ✓, dialogue 40%, 0 breaks, median 15. The plain stop is intact and the ¶98 "what oxen?" stumble is gone. |
| Emotion | 9.0 | **9.0** | The anchor (the broom), the yawn as body rebel and the wrong comfort are intact. With the tunic's motion gone, the silence before "Which is his name?" now belongs to the reader. |
| Immersion (Dim 7) | 8.5 | **8.5** | Unchanged. |
| **FLOOR** | 7.5 | **8.5** | |
| **AVERAGE** | 8.43 | **8.57** (60.0 / 7) | |

**Casual 8.5 (holds).** The oxen fix removes the one stumble the Casual reader had. The cycle-0 reasons for not raising it are unchanged. **CVI-Launch 9.3** (unchanged). **CVI-Legacy 6.6** (provisional, unchanged). There is no divergence alert: 9.3 − 8.5 = 0.8.

### VERDICT — cycle 2
**PASS.**

| Gate condition | Result |
|---|---|
| Genesis Floor ≥ 8.5 | ✓ (8.5) |
| Casual ≥ 8.5 | ✓ (8.5) |
| Pacing | ✓ OK |
| Gates | ✓ all clean, as run here |

Foreshadowing is 0, NO-TICS is clean, and AI patterns are at 2/20.

### For finalize (none of these affects the gate)
- **Optional F1′ (¶198):** this clears the Ch.9 ¶402 "I read it through again" frame and the over/again rhyme with ¶190. Both options were tested on a scratch copy and pass every gate, echo 0, shape CLEAN.
  - (a) `I read it to myself, from the greeting down to the date, and rolled it up.` This is the cleaner sentence, at 2,445 words and 40.49%. It leaves **0 words of headroom**: any later narration cut tips the meter to 41.
  - (b) `I read it all to myself, from the greeting down to the date, and rolled it up.` This gives 2,446 words, 40.47% and 1 word of headroom.
  - "to myself" and "read it all" grep 0 in Ch.1–9.
  - If neither is taken, the current line stands. It is a trace.
- **Chapter header (line 4):** update it to "2,447 after polish cycle 2 (style_check 2,458; wc -w 2,650) | raw dialogue 40.46%". It is stale bookkeeping, not prose.
- **character-bible.md:** it still quotes the retired strings: line 164 "Letters came in two kinds" and line 2187, the old ¶160 "There was not a soul … could have told the". Sync the Ch.10 blocks to the final page: the ¶44 belief, "Kallia corrected none of it.", "it was any name in Phocis", "made the roof into so much talk about rain", "Nobody else", the oxen and the man, "rolled it up" and "from along the lane". This closes cycle-0 Revision #16.
- **At-risk list for Ch.11 on (carried, plus one):**
  - The held silence measured by an indifferent motion is SPENT, with 0 left anywhere.
  - The speech ledger is SPENT.
  - Object weight or size at a close is SPENT.
  - "X corrected none of it" has been used once.
  - Kallia's farewell must not use stopped work or wool.
  - **New:** bend/stoop is at 0.28/1k book-wide against a 0.3 cap.
  - **New:** the narrator re-reading a document to herself now appears in two consecutive chapters (Ch.9 ¶402, mid-scene; Ch.10 ¶198, in the closing run). Give it no third.
- **Pipeline note (cycle 1 (a), still open):** the #11 density cap needs a word-count guard for short chapters. Until the author rules, it is applied as written.

**BIAS CHECK:** This evaluation was produced by the same system that wrote the prose. Confidence in every score at or above 8.5, in Emotion 9.0, in Casual 8.5 and in CVI-Launch 9.3 requires external validation from beta readers, editors or comp analysis.
- The PASS sits exactly on the line for both Floor and Casual.
- Casual still depends on the reader catching the yawn.
- Prose 8.5 is the cycle-1 merit judgement with the mechanical cap lifted. It is not a re-scored raise.
