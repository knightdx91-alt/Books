# Evaluation: Chapter 17 — Games on the Isthmus (run 2)
**Evaluator:** book-evaluator (independent; did not write or revise this prose) | **Date:** 2026-10-21
**Text evaluated:** `manuscript/chapters/chapter-17.md` (sha256 `f106cf63…`, md5 `f28ef11c…`), after writer → dialogue-polish → hook-craft → disruptor → continuity repair (C-01, W-01…W-07, W-09). **6,935 prose words** (shape_check), 6,947 (style_check), 6,951 (show_tell), 7,654 (`wc -w` with the header comments).

**Read against:**
- the book's CLAUDE.md hard gates;
- STATE.yaml `guardrails` and `resolved_author_decisions`, especially **AUTHOR-CP3-5** (a one-off festival on the Isthmus for Titus's triumph, never "the Isthmia"), **AUTHOR-CP3-3** (the pregnancy gap unremarked) and **AUTHOR-END-1** (the approved ending; no Ch.15 door lines quoted back);
- voice-dna §0–§8;
- character-bible.md: **every at-risk and spent block, "after Ch.1" to "after Ch.17", read in full**; the CELER and ONESIMUS cards; the PLAUTIA, MYRRHINE, VALENS, MARA and FELIX Ch.16/Ch.17 blocks; the Ch.17 walk-on note;
- outline `## Chapter 17` and Ledger row 17;
- `evaluations/chapter-16-eval.md` (cycle 0, cycle 1, finalize);
- chapters 15 and 16 in full for pacing;
- `evaluations/continuity/chapter-17-audit.md` (what was applied).

**Genre profile:** commercial historical romance / time-slip, comp *Outlander*. Anti-AI band: commercial (0–8 clean, 9–11 watch). Engagement (book): empathy 55 / fascination 30 / self-insertion 15; **this chapter tilts to fascination** (a heist, a villain). Dimension 7 = **IMMERSION**.

**Measured here.** `bash books/the-hour-of-ash/tools/check_chapter.sh 17` is **clean on every gate**:
- style: simile 1.2/1k, em-dash 0, foreshadow 0;
- grammar 0; rhythm 0; show/tell no flags, dialogue 33.0%;
- voice-wear strict clean; tic gate clean (and-chains 3/9, credential asides 0, negation pivots 0, "So" 0); gesture classes all under cap;
- echo 0; spoken-line echoes none (`tic_report.py --echoes 17`); command echo: one candidate, a false positive (the clerk's "His father thinks…" is not an order);
- metaphor 1.3 fig/1k, median 11;
- `shape_check --strict`: `17 6935 3 33 11 short-punch quiet`, CLEAN.

**My own scans (scratch, not gates):**
- 4–7-grams of Ch.17 against Ch.1–16 and all 13 voice-bank samples, **stop-word-bounded strings included** (the echo gate skips these by design);
- content 3-grams against the same;
- every whole spoken sentence of five words or fewer, against every earlier chapter's speech;
- in-chapter repeated 3–5-grams;
- by hand: #11 explanatory extensions, paragraph-final negations, indefinites, body-rebel channels against the bible's rest schedule, and every SPENT / CLOSED / RESERVED item in the bible, grepped by frame as well as by string.

**The fix set was tested together on a scratch copy.** It was swapped into the manuscript path, and the real `check_chapter.sh 17`, `shape_check --strict`, `tic_report.py --gate` and `--echoes 17` were run from /home/user/Books. The original was restored after every run, and its checksum was verified each time (sha256 `f106cf63…`, md5 `f28ef11c…`). **I did not edit the manuscript.**

*(l.N = line number in the current `chapter-17.md`.)*

---

## HEADLINE
**CVI-Launch (CVI-L):** 9.7 (9.24 + 0.5 strong anchor) | **CVI-Legacy:** 6.9 (provisional) | **Genesis Floor:** **8.0** | **Genesis Average:** **8.71** | **Casual Reader:** **9.0**

**Engagement type:**
- **Fascination** leads in this chapter: a theft from a bound book, a villain who will not walk under a scaffold, a clerk who will not write anything down.
- **Empathy** is second: a mother asking whether her son ate breakfast, and a man reading his own freedom with his lips shut.
- **Self-insertion** is third: needing the toilet in the middle of an escape.

**Divergence alert:** none (9.7 − 8.0 = 1.7).

**Gate (Floor ≥ 8.5 AND Casual ≥ 8.5 AND pacing OK AND gates clean): NOT MET.**
- Casual 9.0 ✓; pacing OK ✓; mechanical gates clean ✓.
- **One dimension holds the floor: Prose & Voice 8.0, on merit, with no cap.** The sentences are 8.5 and better. What holds them is a cluster of book-law breaches that no gate sees:
  - **two voice-bank sample-09 lifts.** "My knees gave, and the step was under me" (l.267) rebuilds sample-09's "my knees went, and I sat down", which is reserved for Ch.25. "He said it to the cake." (l.21) is sample-09's "said it to the" frame, which the bible bans by name;
  - **one sample-12 lift:** "a donkey was complaining about something" (l.377) is sample-12's offstage animal complaint, placed in a held silence;
  - **Ch.7's latrine, rebuilt.** The marble bench round three walls, the holes, the channel of water, the sponge on a stick at the entrance, and men on the bench deep in a topic, all in Ch.7's order (l.519 against Ch.7 l.76);
  - **Ch.14's hand, rebuilt.** Celer's hand "hung there … and drew it in" (l.359) repeats Ch.14 l.84, Mara's hand that "hung above his shoulder … I drew the hand in". The bible lists that gesture as used once;
  - **Ch.12's stranger introduction, reused for Celer:** "the dust of the plain was on the hem of his cloak" becomes "the dust of the Isthmus road along the bottom of it" (l.313);
  - **Ch.15's heat scene inside the latrine:** "It was slow, and stayed slow" becomes "I finished, and it was slow" (l.525);
  - **six Ch.16 carry-overs:** the Sicyon match "with a vineyard and" (l.365); the plan's "among my letters", possessive-swapped (l.145); "had gone in to [a meal]" (l.197); the anchor sentence's shape, "Someone had cut his teeth on it." → "Somebody had taken pains for the emperor's year." (l.87); the underline "her face was wet and perfectly composed" → "perfectly dry" (l.421); Plautia's "I walked in front of him for two years" → Valens's "I walked at her back for two summers and two winters" (l.291);
  - **four SPENT devices:** a held silence filled with sound, a stopped murmur and an animal (l.377); running water measuring a held moment (l.519); the knees (seat) and hands channels, both resting in the bible until Ch.20 (l.267, l.485);
  - **in-chapter doubles:** a ladder-creak clock ×3, the scaffold's strength said twice, the forum "white" ×3, "a cloth in the market" ×2, and anadiplosis ×2 against a cap of 1.
- **Characters sits at 8.5**, not 9.0:
  - Valens wipes his hands before taking the leaf (l.203). It is his third wipe-before-handling (Ch.9 the mane, Ch.15 the tunic before the flashlight), and the bible lists it as SPENT;
  - Valens's one idiom, "They'd carry her off a cliff for him" (l.233), which his card forbids;
  - the Ch.16 porch protocol re-staged ("stopped at her back, half a pace to her left", l.309), which the bible says is never re-staged;
  - walk-on word-doubling ("Mules! … Mules!", Myrrhine's "Further back. Further.", the pine cry);
  - the boy borrows the clerk's whole-line "Lady.";
  - Plautia contradicts herself about the seal (l.105 against l.155).

**Every fix is a swap, or a cut offset by restored narration. 56 strings, tested together:**
- 6,935 words (unchanged); dialogue 32.8% / 33 (30–40 ✓); median 12 (low gear ✓); 3 breaks; `short-punch` → `quiet`;
- every gate clean; echo 0; spoken-line echoes none;
- the first line, the closing paragraph and the bare "No." are byte-identical (md5 checked);
- every anchor line is kept.

---

## Genesis Score (Craft Assessment)

| Dimension | Score | Evidence | Cap reasons / holds |
|---|---|---|---|
| Originality | 9.0 | **The outline's subversion is on the page:** there is no duel; the danger is legal; the escape succeeds because a clerk is bored. **What the writer built on top of it:** (1) **the theft covered by the victim's own dowry, read aloud through a mouthful of figs**: "*Plautia, daughter of Sextus*," he read, chewing. "*Gave*." He swallowed. (l.113); (2) the noise of the cut covered by a lie about Mara: "My woman has dropped her pen. She is clumsy … You were at the lion's paws." (l.135); (3) **the clerk is the man who hid the book**, shown and never said: "His hand found the wrong year's hole at the first try" (l.175); (4) the villain's superstition rendered as a line of shade: the hand stopped "in the bar of shade" (l.359); (5) "the book went with him, lighter by two boards" (l.397); (6) the clerk's wish that his grandson **lose** (l.255–259); (7) a toilet stop in the middle of the escape, with a javelin question; (8) "Put it on him and they'll think he won something!" / "He has," (l.489–491). | **≥9.0:** would a senior editor set this beside *Outlander*'s Wentworth or Leoch set pieces? Yes. It is a heist whose engine is anti-heroic, and that is fresher than Gabaldon's breakouts. **Not 9.5:** the noise-cover and look-out mechanics are genre-standard in shape, and the latrine repeats Ch.7's set piece. |
| Theme | 9.0 | The theme is "Proof of who you are, and who gets to hold it." It is carried by acts and left as a question. "That's out of the emperor's year." / "It's mine." (l.241–243); Celer, patting the cut book: "Papers are no more than that." (l.371); the clerk's erasure as mercy: "You were never in." (l.403); a slave girl "aged eleven" read out as dowry property (l.119), unremarked; "He has," (l.491); "I lead mules." (l.503); the knife that "belongs with whoever knows what it is for" (l.441). **Texture that means nothing:** the sunshade lost "altogether" (l.393), the fat man's javelin, Lucanian sausages, the washing swept off a wall, the trainer walking backward. | **≥9.0:** two answers, one in each man's mouth: who holds the paper (Celer), and who can read it (Valens). **Not 9.5:** "It belongs with whoever knows what it is for" leans toward a maxim. |
| Characters | 8.5 | **Onesimus** is the best walk-on in the book: the figs, the cobweb, the mended sandal strap, "Lady didn't ask," (l.331), "Not today, legate." (l.391), "I'd have liked to see him lose." He is the card's "only man who saves anybody out of sheer unwillingness to write it down", to the letter. **Celer is distinct from Plautia:** contractions, the warm "we", tag questions ("We'd have done that, wouldn't we, Onesimus?"), never *wife* (0), never a direct threat; every knife is a pleasantry ("When all this has been tidied away.", "Bring Mara."). **Plautia:** "Did he eat, this morning, before you left him?" (l.335); the honey "too hot" (l.339); "Let her go on asking." (l.395); no contractions (verified). **Valens:** mind-reading inverted and right ("He'll eat his bread.", l.271); "You hired me," (l.363); the crown bought mid-flight. **Mara chaos 4/4** (below). Cover-the-name PASS for Celer, Plautia, Onesimus, Valens and Mara. | **No cap.** No catchphrase, and the gate's gesture classes are clean (I use the gate's numbers). **Held at 8.5** by C1–C12 (bullets below the table). |
| **Prose & Voice** | **8.0** | **Stopping sentence:** "and he looked at his hand there, in the bar of shade, as though somebody else had put it out, and drew it in." (l.359). **Underlines:** "Close to, he was older than his laughing had been" (l.313); "The ladder said what he thought of that." (l.55); "His head had not moved." (l.137); "and the book went with him, lighter by two boards" (l.397); "He eyed us under his scaffold like a bench somebody had left in his way." (l.401); "Nobody's going to rob the proconsul this morning." (l.385); "My name, in his mouth. It had come to him from the road below Delphi, with that ear." (l.351); "His mouth moved on the first word, and then it stopped moving, and he read the rest of it with his lips shut." (l.209). **Ugly sentences:** "It was done well or it was a botch, and it was a botch." (l.149); "I finished, and it was slow, and then it was over." (l.525). **Voice under pressure:** level 1 at Celer (Mara's only line is "I write for the lady."; no asides); level 2 in the run ("My sandals slapped. We overtook the cart. My breath went short, then raw."). | **Merit 8.0, no cap.** #11 is under the cap (4 firm, 0.58/1k against the commercial >0.8). The ugly sentence and the change of voice under pressure are both present. **Held by the law cluster** (R1–R28): the sample-09 and sample-12 lifts, the Ch.7 latrine, Ch.14's hand, Ch.12's introduction, Ch.15's heat words, six Ch.16 carry-overs, four SPENT devices, and the in-chapter doubles. Anti-AI: 9/20, −1.625 (watch band, at its bottom). |
| Pacing | 8.5 | **The ledger row is hit on every hard field:** In medias res, between Ch.16's Parallel and Ch.18's Single-scene ✓; open `short-punch` ("The boards left their dust on my fingers.", 7 words; the outline's "wax tablets, dust (≤8 words)") ✓; close `quiet` (13 words, the run unfinished) ✓; 3 breaks ✓; dialogue 33% (30–40) ✓; 6,935 against 7,400 (−6%, in range) ✓; median 11 (low) ✓. **Speed design, as the outline asks** ("fast and fragmented; one slow beat with Celer"): S1 fragments at the cord ("I sawed. Nothing."); the one 120-word held sentence at the shade line; S4 accelerates to "We ran." **Value shift:** hidden (−) → leaf in hand (+) → seen by the clerk (−) → trusted, and right (+) → named by Celer (−) → Celer leaves, nothing noticed (+) → watched at the arch (−) → the breeze, and a sail going up (−). | **Not 9.0.** S1's procedural run (the tags, *VETT. CANIN. II/III/IIII*, the boards' raised strips, the cord through the holes; l.59–91, l.125–147) and S4's hawker parade (three vendor paragraphs, each with an exclamation triad) both slow the Devourer, the second in the middle of an escape. |
| Emotion | 9.0 | **The anchor lands exactly as planned:** "the bored archive clerk who will not stop eating figs during a theft": "With the same stylus he dug out a fig and ate it, and began." (l.111), through to "He dug a fig out of the cake with his thumb" (l.411). **The surprise lands:** the escape turns on boredom ("Not today, legate.", "You were never in."). **Humor in peril:** the bladder; the ladder; the javelin question. **Body rebel:** "My hands were steady. My bladder was another matter." (l.83), a fresh channel. **Techniques ≥5:** dramatic irony (Celer pats the cut book; "Nobody's going to rob the proconsul"); subtext (every Celer pleasantry is a threat); object proxy (the leaf under the tunic, the pine crown, the knife); a mother's grief by inventory (the honey "too hot"); the quiet gut punch "Three of them are dead." (l.215). | **≥9.0.** **Not 9.5:** Mara's feeling for Plautia at the parting stays almost entirely implicit ("her curtain stayed down"). That is the right restraint, but some readers will miss the friendship's goodbye. |
| **Immersion** (Dim 7) | 9.0 | **Period:** the South Stoa as the proconsul's office; the Lechaion road's broad steps and colonnades; the propylaea arch with its gilded bronze chariot; the fountain by it; wax-tablet codices with raised rims, corded and sealed; years dated by the duoviri; *liber*; the lanista; *murmillo*; Judaea Capta silver "still sharp from the die" (l.493); Lucanian sausage with cumin; Isthmian pine crowns; strigils and flasks on rings; a pressed fig cake; the litter and the sunshade slave; a mended sandal strap. | **Held at 9.0.** Slips: "the horses' gilding gone green" (gold does not green; the bronze under it does; l.473, L3); dust "gray" on the boy (l.159) against "brown" on Celer's toga (l.313), the same road; "a letter will come from this house" said in the forum (l.423, L2); the latrine in Ch.7's words (R4). |
| **FLOOR** | **8.0** | Prose & Voice (merit) | |
| **AVERAGE** | **8.71** | (9.0 + 9.0 + 8.5 + 8.0 + 8.5 + 9.0 + 9.0) / 7 = 61.0 / 7 | |

**Why Characters is held at 8.5:**
- **Valens's SPENT wipe (C1).** "He wiped one hand on his thigh, then the other. The flour stayed." (l.203). This is his third wipe before handling a thing that matters: Ch.9 l.232 (the mane, before the pitch) and Ch.15 l.128 ("wiped both hands dry on his tunic before he would accept it", the flashlight). The Ch.9 at-risk block lists it as SPENT. His card says "always a different object … never a fixed gesture". Three uses book-wide is not "chapter after chapter", so I do not cap; see BIAS CHECK.
- **Valens's idiom (C2).** "They'd carry her off a cliff for him, if he paid." His card says flatly literal, without idiom; he never uses a comparison. This is hyperbole.
- **A Plautia line in Valens's mouth, and a re-staged protocol (C3, C4).**
  - "I walked at her back for two summers and two winters." (l.291) runs Plautia's Ch.16 l.372 skeleton ("I walked in front of him for two years").
  - Celer then says "Two years at her back" (l.361), and the narration has "stopped at her back, half a pace to her left" (l.309): "at her back" ×3.
  - The left-side guard position is the Ch.16 porch set, which the bible says is "Never re-staged; Ch.17 and Ch.22 show Valens and Plautia some other way."
- **Walk-on word-doubling (C5, C6, R22)**, which the bible allows for no walk-on:
  - the trainer's "Mules! … Mules!";
  - Myrrhine's "Further back. Further.";
  - the pine boys' "The god's pine! The winners' pine!";
  - the sausage-man's "Not for the athletes, the athletes…".
- **Bleed (C7, C8).**
  - The boy's whole-line "Lady." (l.171) is the clerk's line, and the card gives it to him.
  - The fat man's "Mistress." (l.521) blunts the seamed man's "Mistress," (l.327), which recalls Ch.12's "Be still, mistress." and should stand alone.
- **Mara's echo-question (C9).** "Lose?" (l.257) is the echo-question shape the bible rested after Ch.16 ("Kind.").
- **The role label (C10).** "the clerk" appears 25 times. After Celer names Onesimus (l.329), the narration still uses the label three times. The Ch.8/9 rule is that a recurring walk-on is named or varied.
- **Plautia's seal contradiction (L1).** "The seal is my father's … I know it from here." (l.105), then "My father kept two seals … Which is that?" (l.155).

**Trajectory against Ch.1–16** (finals 8.50–8.86; cycle 0s 7.5–8.0):
- This is the seventeenth cycle 0 below the gate, and the thirteenth held by narrator moves the gates cannot see.
- The **#11 cap did not hold it**, and the continuity repair added no gloss.
- **The new failure modes:**
  - **voice-bank samples leaking by structure** (sample-09's collapse, reserved for Ch.25; sample-12's offstage animal);
  - **a whole earlier set piece rebuilt in its own order** (Ch.7's latrine);
  - **the previous chapter's underline sentences reused as skeletons** ("Someone had cut his teeth on it.", "perfectly composed").

See Cross-Book #1–#4.

---

## CVI-Launch Breakdown
| Input | Score | Evidence |
|---|---|---|
| Commercial Pacing | 8/10 | In medias res; a theft in real time; a villain scene; an escape; it ends mid-run with a sail going up. It loses 2 for S1's procedural tags and boards and for S4's hawker parade, and it is 6.9k long. |
| Tomorrow Test | 6+ anchors → 10 | IMAGE: the clerk digging figs out of a pressed cake with his stylus while he reads the dowry aloud and Mara saws the cord; Celer's hand stopped at the line of shade; the book carried off "lighter by two boards"; Valens reading his own name with his lips shut; the clerk eating his bread under the scaffold through the whole confrontation. QUOTE: "My woman has dropped her pen. She is clumsy."; "Nobody's going to rob the proconsul this morning."; "That's out of the emperor's year." / "It's mine."; "Three of them are dead."; "Put it on him and they'll think he won something!" / "He has,". |
| Casual Reader | 9.0/10 | See the report below. |
| Shareability (quote / plot / emotional) | 4 / 5 / 3 → 8 / 10 / 6 → **9.2** | Quote: "Nobody's going to rob the proconsul this morning." Plot: "they steal his freedom out of the archive while the clerk eats figs and reads her dowry out loud, and the villain won't walk under scaffolding." Emotional: "He has," for the crown; "Three of them are dead." MAX 10 × .6 + AVG 8 × .4. |
| Concept Pitch | yes → 10 | |
| Human Closeness | yes → 10 | A mother asking after her son's breakfast; the two women's parting; Valens's crown for Felix; "Valens ran beside me, not in front". |
| **CVI-Launch** | **9.24 + 0.5 = 9.7** | 8 × .2 + 10 × .2 + 9 × .2 + 9.2 × .2 + 10 × .1 + 10 × .1 = 9.24. One-chapter formula; see BIAS CHECK. |

**CVI-L note.** In this project "CVI-L" means **CVI-Launch: 9.7.**
- Running CVI-L Ch.12–17 is 9.7 / 9.8 / 8.9 / 9.8 / 9.7 / **9.7**.
- This is Part One's action climax, and it holds the readership on a new engine. Ch.15–16 ran on intimacy; Ch.17 runs on **comedy under threat**: the clerk, the ladder, the javelin question and the sunshade.
- The romance is kept warm by small beats rather than scenes: "Valens read my face before he read the case." (l.199); "Valens ran beside me, not in front" (l.555); the crown "For Felix … He missed the boys." (l.529).
- **None of the 56 fixes touches an anchor:**
  - the fig cake, the stylus and the thumb;
  - "She is clumsy";
  - "His head had not moved.";
  - "lighter by two boards"; "Nobody's going to rob the proconsul"; "Three of them are dead."; "He has,";
  - the shade-line sentence. Its last clause is re-verbed (R6) to clear Ch.14's gesture, and its image ("as though somebody else had put it out") is untouched.

**CVI-L is unchanged after the PATH: 9.7.**

**CVI-Legacy (default weights; provisional):** **6.9**. It is the sum of:
- Originality 9.0 × .30;
- Theme 9.0 × .25;
- Cultural Vocabulary 2 × .20;
- Re-readability 7 × .15;
- Identity 5 × .10.

What rewards a re-read:
- the dowry's "*Earrings, two pairs, gold, with drop pearls*" against Plautia's torn earlobe (Ch.16), never connected;
- Celer's ears "like the handles of a cup" against Marcus's "father's ears, which stand out";
- "Like a wolf." from the man who named Valens Lupus;
- the gray, sober clerk, when Ch.16 hoped for "the young one" because a sober clerk would find the knot.

---

## Anti-AI Scan (20 patterns; density per 1,000 words at 6.94k; commercial band)
| # | Pattern | Result | Count / density | Citation |
|---|---|---|---|---|
| 1 | Forced symmetry | FOUND moderate | 5 (0.72) | "My hands were steady. My bladder was another matter." (designed; kept); "Valens read my face before he read the case."; "He's not opened it … He'll not open it."; "an old wall nobody had mended and a gate nobody kept" (→ R27b); "everybody's forgotten it / somebody decides to remember it". **−0.25** |
| 2 | Empty poetic vocabulary | Clear | 0 | |
| 3 | Automatic rule of three | FOUND moderate | ~6 automatic (0.87) | l.35 the emptied city (shutters / vats / fountain); "small and pale and naked" (l.149); the crowd and the athletes (l.487, two triads); **the hawker parade**: three consecutive vendor paragraphs, each ending in an exclamation triad (l.489, 493, 495); "salt and weed and pitch" (l.543). Characterful, not counted: the dowry list; the three dead witnesses; "To his face, in the forum, with his men behind him." **−0.25** |
| 4 | Em dashes | Clear | 0 | |
| 5 | Empty metaphors | Clear | 0 | "tight as iron"; "like the handles of a cup"; "like a bench somebody had left in his way". All concrete. |
| 6 | Dramatic "And" openings | Clear (narration 0) | — | Speech rejoinders: 4 across three speakers ("And the book?", "And the paper in Rome,", "And this will be Mara.", "And then?"). At the WATCH of ≤4. |
| 7 | Pseudo-philosophical closings | Clear | — | Sections end on an act ("under the ladder"; "followed"; "by the eastern road"; the sail). |
| 8 | Excessive parallelism | FOUND moderate | 6 (0.87) | "He read all of it. He read the witnesses." (→ R19); "Then he goes home and eats. Then he wants his book."; "past the city, past the walls" (→ R5); "When we arrived he was digging, and while … he was digging still"; the hawker paragraphs; "nobody had mended … nobody kept". **−0.25** |
| 9 | Overly smooth transitions | FOUND minor | — | Six backfill inserts sutured by the past perfect ("That morning, on the brother's roof", "An evening or two after the plan", "Felix had taken the mules down…"). The design calls for them; they are minor. **−0.125** |
| 10 | Described emotions | Clear | 0 | |
| 11 | **Explanatory extension** | **FOUND moderate, under the cap** | **4 firm (0.58/1k)** | (1) l.85 "had been left raised at the edges so the two faces would not touch" (purpose tail); (2) l.193 "which was the only disguise anybody had been able to think of for him, and it fooled nobody who had ever seen a baker" (a joke-gloss; a keeper); (3) l.359 "as it must have reached for the shoulders and forearms of a thousand men … to take a fellow by the elbow…" (an interpretive extension; a keeper); (4) l.535 "That meant nothing; the steps were all people." Borderline, not counted: l.11 "In a colony two names made a year."; l.61 "the one out of its place was always louder than anything written on it"; l.87 the stroke for the *L*; l.319 "the voice of a man telling a story to listeners who had begged for it". **−0.25.** Cap (commercial >6 or >0.8/1k): **PASS.** |
| 12 | Binary negation opener | Clear | 0 | Gate pivots 0. |
| 13 | Precision flex | FOUND minor | — | Body-part rulers 5 against the ≤4 WATCH: "each a finger thick", "a hand deep", "a finger's breadth", "a long arm's length", "by a head". Also "half a pace", "six paces", "a dozen boards". **−0.125** |
| 14 | Emotional control demonstration | Clear | — | Control fails and is funny (the bladder). |
| 15 | Authoritative description | FOUND minor | — | The wax-book mechanics, the scaffold's lashings ("put on wet and had dried tight as iron"), the latrine inventory. Offsets: "a Gnaeus somebody"; "or was hidden in it"; "missed no footing that I saw"; "There was a sign." **−0.125** |
| 16 | Philosophical asides | FOUND minor | 2–3 (speech) | "It belongs with whoever knows what it is for." (Plautia); "Papers are no more than that." (Celer); "That's a man who's had enough of the day." (Valens; a judgment). Characterful; kept. **−0.125** |
| 17 | Clean dialogue | FOUND minor | — | S4's walk (l.461–471) is orderly Q&A. Elsewhere the talk is broken by reading aloud, a runner, ignored lines ("It'll be over.") and non-answers ("Lady didn't ask,"). **−0.125** |
| 18 | Thematic echo chamber | Clear | — | Plenty of texture that means nothing. |
| 19 | Graduated reveal | Clear | — | In medias res. |
| 20 | Emotional temperature report | Clear (edge) | — | Five body beats spread through the chapter (bladder, sweat, knees, hands, breath). All are inhabited acts, not reports, and they land on peaks, not at intervals. R1 and R28 change two of them. |

**9 / 20 found (#1, #3, #8, #9, #11, #13, #15, #16, #17). Total −1.625. Band: watch (commercial 9–11), at its bottom.** **#11 hard check: PASS** (0.58/1k).

**After the PATH:**
- #13 clears (rulers 5 → 3);
- #3 and #8 → minor (R19, R22, R27b, R5);
- **8/20, −1.25: clean band**, at its edge.

---

## The book's own laws
- **NO FORESHADOWING: PASS (gate 0; by reading, 0).**
  - The narration's "would" lines are all counterfactual ("A copyist would have had a long walk.", "would have carried a loaded cart").
  - Forecasts stay in speech ("By then we're a day out to sea, wind willing.").
  - There is no "never again", no "the last time", and no vantage after the scene.
  - Celer's "grew old in the sun … in Italy" carries the reader's own irony about Vesuvius, and no page points at it (kept under voice-dna §0 "What is KEPT" 4). R10 keeps it free of "vineyard" and "vines", so it does not echo the god's "mountain of vines".
- **AUTHOR-CP3-5: PASS.** "Isthmia" 0 and "Isthmian" 0. The festival is "the games", "the boys race out on the Isthmus", "the boys' day", "the men's race".
- **AUTHOR-CP3-3: PASS.** Nothing notices a child.
- **AUTHOR-END-1: PASS.** No Ch.15 door, camera or "wait outside" line is quoted or paraphrased.
- **The outline's non-negotiables: all on the page.**
  - **The fig-eating clerk**, from start to finish.
  - **Mara's one moment of archive recognition**: the accession-number storeroom (l.61). It is triggered by the shelves, takes one sentence, returns to the scene at once, and has no person in it.
  - **Celer in the colonnade with no violence and no monologue.** His longest speech is the offer: five short sentences after one conditional (l.365).
  - **Valens gets his papers**: the leaf goes inside his tunic (l.277).
  - **The theft succeeds by luck and boredom.** The cord's noise is covered by a lie and by a clerk who does not turn his head. The clerk himself carries the cut book out, unlooked-at. He sees the leaf in the lane and says nothing. Celer will not come under the poles.
- **No heist-competence cascade: PASS, with a WATCH.**
  - S1 holds six expertise beats: the misshelving recognized; "Somebody who wanted it lost and knew where to find it again."; the boards' raised strips; the hand's *L*; "Somebody had taken pains for the emperor's year."; the linen cord "twisted hard and waxed".
  - Each is undercut at once: the bladder, "I sawed. Nothing.", the board knocking the shelf, the last hole missed twice, and a knot that "was a botch".
  - Success is never earned by skill. R13 removes one verdict beat.
- **Celer distinct from Plautia: PASS, strongly.** He has contractions, the warm "we", tag questions, "Oh, not that", "Splendid man.", never *wife*, and never a direct threat. She has no contractions (verified, every line), periods broken by blunt questions ("Did he eat, this morning, before you left him?"), never names him, and never mentions the night. No bleed either way.
- **Memory only when the scene triggers it: PASS.**
  - The storeroom sentence is the only 1998 memory.
  - The six backfill pieces are this morning's (the spoons, the litter speech, Myrrhine's packing, the roof at dawn, the brother and the baker, Felix at the gate). The in-medias-res design asks for them, and each is triggered by an object or a person on the page and returns at once.
  - No stand-alone memory paragraph; no lost-name close.
- **Explanation-density cap: PASS** (4 firm, 0.58/1k), and 4 after the PATH.
- **Paragraph-final negations ≤1.5/1k: PASS.**
  - **9 in narration (1.30/1k):** l.35, 59, 103, 137, 193, 195, 315, 377, 487. My script also flags l.131 and l.535, but each has its negation mid-clause.
  - **After the PATH: 7 (1.01/1k).** R5 cuts l.377's; X1 ends l.35 on an act.
- **No comparisons in Valens's speech: one breach.** Every Valens line was checked. None uses "like" or "as". One is figurative hyperbole: "They'd carry her off a cliff for him, if he paid." (l.233) → **C2.**
- **No command echoes: PASS.** The gate's one candidate is a false positive. By hand, each order is answered by its result:
  - "Open it" → "The boards parted";
  - "Keep walking. Don't look at him." → "We passed beneath the arch";
  - "Walk." → "We left the colonnade for the sun.";
  - "Bring all three." → "three books stacked";
  - "Shut up your door" → "locked the door with a key on a thong" (no shared word).
- **No borrowed whole spoken lines: PASS** (`--echoes 17`: none). My ≤5-word scan matches only stock words ("No", "Then", "Good", "Lady", "Mistress", a name), and the stock "Good," is Plautia's own.
  - **In-chapter bleed:** the boy's whole-line "Lady." (C7).
  - **Lines that land again by situation:** "Mistress," in the seamed man's mouth recalls his Ch.12 "Be still, mistress." It is kept as the menace, and the fat man's echo is cut (C8).
- **NO TICS: verbal catchphrases 0; gate gesture classes clean.** By hand:
  - **Valens's wipe-before-handling**, third book-wide → C1.
  - **"said/told the [non-listener]"**, cap 1 per chapter: "He said it to the cake." (l.21, and sample-09's banned wording) and "putting his questions to the black" (l.283, a sibling of Ch.15's SPENT "snowplow told to a ewe") → R2, R3. The trainer's "to Valens's chest" is a listener addressed at his body; kept.
  - **Walk-on word-doubling** → C5, C6, R22.
  - **Anadiplosis ≤1 per chapter:** l.79 has two in one sentence (tray → tray, wax → wax), and l.303–305 a third (one → that one) → R20, R21. l.311's "paving … on the paving" is loose, and kept as the one.
  - **"stood where she was"** (l.421) is a sibling of the SPENT "stayed where [pron] was" → C12.
  - **The narrator's "[thing] nobody had [verb]ed"** relative clause ×4 (l.283, l.315, l.537 ×2), and indefinites in narration at 20 (2.9/1k, WATCH) → R27a, R27b; l.315's "where nobody had stitched it" is kept. 16 after the PATH.
  - **The role label "the clerk" ×25** → C10.
- **SPENT / RESERVED devices: FAIL ×5** → R1, R5, R4/R5 (water), R28, C1.
  - **sample-09's collapse** ("my knees went, and I sat down"), reserved for Ch.25, and Ch.4's knees-before-hunger, SPENT: l.267 "My knees gave, and the step was under me".
  - **A held silence filled with sound and movement**, SPENT, 0 more: l.377. The bearers "left off their talk" (a sibling of the SPENT stranger-freeze); a donkey "complaining about something" (sample-12's offstage animal, a string and frame the bible names); "not a sound reached us"; "past the city, past the walls" anaphora.
  - **Running water measuring a held moment:** l.519 "and the water in the channel ran by".
  - **Body-rebel channels the bible is resting until Ch.20:** "The seat as the body-rebel channel: used; rest it (and hands, and voice) until Ch.20's weeping" (after Ch.11). Ch.17 uses the seat (l.267) and the hands (l.485, "My hands had begun to shake … they shook there"). Ch.12's "The shaking went into my arms" already spent a shaking channel.
  - **Valens's wipe** (SPENT after Ch.9).
- **No reuse of earlier chapters' phrases or set pieces: FAIL, cleared by the PATH.**
  - **Ch.7 l.76, the latrine, rebuilt** in order: "a marble bench round three walls, holes cut along it … over a channel of running water, and a sponge on a stick standing in a bucket at the entrance. Four men were sitting in it…, deep in the price of oil." → l.519, "a marble seat ran round three walls, cut with a row of holes, and water ran in a channel at our feet, and a stick with a sponge on it stood in a pot at the entrance; and on the bench, already, a fat man … discussing the javelin." The inversion (nobody glances; the fat man asks her opinion) is the right idea, and it survives R4 in fresh words → **R4**, the highest-value single fix.
  - **Ch.14 l.84, the hand that "hung … I drew the hand in"** → Celer's hand "hung there … and drew it in" (l.359) → **R6** (two verbs; the image stays).
  - **Ch.12 l.8, the friendly stranger's introduction** ("the dust of the plain was on the hem of his cloak") → Celer's "the dust of the Isthmus road along the bottom of it in a brown band a hand deep" (l.313) → **R7**. Introductions do not travel between characters (bible, after Ch.11).
  - **Ch.15 l.574/heat, "It was slow, and stayed slow"** → the latrine's "it was slow, and then it was over" (l.525) → **R9.**
  - **Ch.16 carry-overs:**
    - "with a vineyard and a cough" (SPENT) → "with a vineyard and somebody to write his letters" (l.365) → **R10**;
    - the plan's "among my letters" → "among Plautia's letters" (l.145; possessive swap) → **R11**;
    - "had gone in to its suppers" → "had gone in to his dinner" (l.197) → **R12**;
    - **the Ch.16 anchor sentence's skeleton** ("Someone had cut his teeth on it.") → "Somebody had taken pains for the emperor's year." (l.87; also a second absent-workman verdict beside "took no trouble for anybody", where the cap is ≤1) → **R13**;
    - the underline "her face was wet and perfectly composed" → "her face under it was perfectly dry and very white" (l.421) → **R14**;
    - Plautia's "I walked in front of him for two years" → Valens (l.291) → **C3**;
    - the road "dead straight over the flat land" → "flat and straight" (l.537) → **R17**.
  - **Ch.14 l.120** "His own freedom was a line in a book in a record office" → Celer's "a line in a magistrate's book" (l.371) → **R15**.
  - **Ch.15's Felix exit verb**, "made for the" → Valens (l.299) → **R16**.
  - **Ch.9's "a bay tree in a pot at the door"** (now at 1) → "a sponge … stood in a pot at the entrance" → cleared by R4.
  - **sample-01's slung tray** (audit W-06 varied the sausage-man's words; the coin-seller kept "a tray of new silver hung from a strap") → **R18**.
- **Logic and fact:**
  - **L1:** the seal "my father's … I know it from here" (l.105) against "Which is that?" (l.155).
  - **L2:** "a letter will come from this house," said in the forum (l.423).
  - **L3:** "gilding gone green" (l.473).
  - **L4:** Mara speaks twice running with no beat between (l.225 → l.227; Ch.16's L5 shape).
  - The gray/brown dust is cleared by R7.
- **Retired reflexes:** no define-by-negation opener, no performed candour, no scene button, no closing aphorism; and-chains 3/9; em-dash 0 ✓.
- **Ledger:** approach ✓, open ✓, end ✓, breaks ✓, dialogue ✓, theme ✓, length ✓, gear ✓. **Outline chaos moments ✓:** Valens's mind-reading inverted ("He'll eat his bread." He is right: the clerk says nothing in the colonnade); Celer's irrational behavior (the shade line; carried round).

---

## Character Chaos Check (Primary: Mara)
- **Irrelevant thought: PRESENT, inhabited.** While Valens stands with the leaf in plain view of the man who could hang them: "The clerk's sandals were old, one strap mended in a different leather" (l.245). Her eye for a mend, at the worst moment. Also "A copyist would have had a long walk." (l.65).
- **Cognitive distortion: PRESENT, inhabited.** All-or-nothing on the knot: "There was no half of that. It was done well or it was a botch, and it was a botch." (l.149).
- **Unprompted memory: PRESENT, triggered.** The storeroom accession numbers, set off by the shelves and back in the scene in the next sentence.
- **Failed emotional management: PRESENT.** The bladder (l.83, paid off at l.519–525); the knees and hands (l.267, l.485; recast by R1 and R28 into a plain act and a fresh channel, skin prickling under the dress).
- **Voice under pressure: demonstrated.** Level 1 under Celer; level 2 in the run (voice-dna §1's map row "17: levels 1–2" ✓).
- **4/4, inhabited.**

## Secondary Character Chaos
- **Onesimus:** wants his grandson to lose; eats through a theft; gives the game away by hiding nothing. His own moment.
- **Celer:** stops his hand at a shadow and looks at it "as though somebody else had put it out". His own moment.
- **Plautia:** "Will you let me speak to him?"; gives away the knife without weeping (a new giving, staged differently from Ch.16). Her own moment.
- **Valens:** breaks the plan to stand by her; buys a crown in the middle of an escape. His own moment.
- **Myrrhine** (backfill): "If it goes to anybody else, I shall know whose house." Her own moment.
- No secondary character is a mere function. No cap.

---

## The Tomorrow Test
**What the reader remembers:**
- A bored clerk digs figs out of a fig cake with his stylus while he reads a woman's dowry aloud, chewing.
- Behind him, the heroine saws through the cord of a magistrate's book to steal her lover's freedom.
- The cord parts with a knock, and the clerk's head does not even turn.
- Then a charming villain will not step under a builder's scaffold. His hand stops at the edge of its shadow, he looks at it as if it were somebody else's, and he walks off patting the book that is two boards lighter.

**Anchor type:** BOTH.
- IMAGE: the fig cake and the stylus; the hand at the shade line; the clerk eating his bread under the scaffold through the whole confrontation; Valens reading with his lips shut.
- QUOTE: "My woman has dropped her pen. She is clumsy."; "Nobody's going to rob the proconsul this morning."; "That's out of the emperor's year." / "It's mine."; "He has,".

**Verdict: ANCHOR EXISTS** (strong; +0.5 CVI).

**Type check:**
- **New to the book:** comedy as the anchor's carrier, and a bystander's appetite as the engine of a climax.
- **Earlier anchors:** an object read for an absent child (Ch.16); a question that was another question (Ch.15); a concealment (Ch.14); a recitation and one word (Ch.13).

## The Shareability Test
"They break into the Roman records office to steal the page that proves he was freed. The clerk is so bored he eats figs and reads her dowry out loud the whole time, and when he catches them he just buys his bread. And the villain is too superstitious to walk under the scaffolding."

Running total: 17 chapters, 33+ shareable moments.

---

## Reader Reports

### The Devourer (6.9k after two 7.2–7.5k chapters)
- **Speeds up:** "Behind me the clerk was eating figs."; the ladder; the swapped book; the dowry read aloud against the sawing; "The clerk stopped reading." / "My woman has dropped her pen."; Celer's runner at the door; the clerk drawing the book out of the wrong year at the first try; the lane; "That's out of the emperor's year." / "It's mine."; the whole colonnade; the seamed man at the fountain; "We ran."
- **Slows:** the tags, *II*, *III*, *IIII* (l.59); the boards and their raised strips (l.85–91); the cord threaded back hole by hole (l.139–147); the three hawker paragraphs and the latrine description in the middle of an escape.
- **Would they stop?** No. Every slow patch sits under a ticking clock (the ladder; the reading; the sail).
- **Last page:** mid-run, with a sail going up. They turn.

### The Critic
**Underlines:**
- the shade-line sentence;
- "older than his laughing had been";
- "The ladder said what he thought of that.";
- "His head had not moved.";
- "lighter by two boards";
- "like a bench somebody had left in his way";
- "My name, in his mouth.";
- "It was done well or it was a botch, and it was a botch.";
- the honey "too hot".

**Disappointments:**
- "*the latrine*: Ch.7's room again, bench, holes, channel, sponge, in the same order" (R4);
- "*my knees gave, and the step was under me*: the collapse the voice bank keeps for Fenn" (R1);
- "*a donkey was complaining*: the held silence filled again" (R5);
- "*hung there … drew it in*: the hand from the night she learned the year" (R6);
- "*Somebody had taken pains*: last chapter's best sentence, re-nouned" (R13);
- "*I walked at her back for two summers*: Plautia's line, turned round" (C3).

### The Hostile
1. **Which is it?** Plautia knows the seal "from here", then asks which of two seals it is (l.105/155) → **L1**.
2. **"From this house"**, said in the open forum (l.423) → **L2**.
3. **Gilding does not go green**; the bronze under it does (l.473) → **L3**.
4. **The same road** leaves gray dust on the boy and a brown band on Celer (l.159/313) → **R7**.
5. **How does the clerk know** the freedman's seal "had a chip out of the rim"? He keeps the colony's books, so he has seen it sealed. Plausible; no change.
6. **Athletes coming up from the harbor at noon** on the day of the men's race, "oiled for the road"? They are a boxing troupe off the morning ship, bound for the Isthmus later. Plausible; no change.
7. **Why does Celer fetch a book his copyist was already "keeping"?** Plautia's line answers it: the same empty morning, for the same reason. Coherent.
8. **"I walked at her back"**, then "Two years at her back", then "stopped at her back" → **C3, C4.**

**Verdict:** "Two small slips and a self-contradiction; the timeline holds: dawn procession, late-morning office, noon at the oven, the afternoon breeze."

### The Casual Reader (airport, 10 pages)
- **Hooked at once:** dust on the fingers, then "Behind me the clerk was eating figs." The reader is in a theft before they know it, and it is funny.
- **Feels it at:**
  - the clerk taking the cake up the ladder;
  - "Doris, aged eleven" (a small cold shock);
  - the sawing under the reading;
  - "She is clumsy";
  - Valens reading his name with his lips shut, then "Three of them are dead.";
  - Celer, whom they love to hate;
  - "Did he eat, this morning?";
  - the toilet stop (they laugh out loud);
  - "He has,";
  - the crown for Felix.
- **Frictions:** which year is which (the year of the fire, the year of Nero); the board mechanics.
- **Would they buy after 3 pages?** Yes. **Do they stay?** Yes. It is the most purely entertaining chapter since Ch.11. **9.0/10.**
- **Not 9.5:** the archive procedure, and the S4 crowd catalogue before the run.

### The Devoted Reader (active: long saga)
**Will post about:**
- the South Stoa as the proconsul's office;
- Judaea Capta denarii sold as souvenirs at a triumph festival;
- the Lechaion road's steps and the propylaea chariot;
- wax-tablet codices with raised rims;
- years dated by duoviri;
- the dowry's pearl earrings against the torn earlobe;
- Celer's ears against Marcus's.

**Will catch:**
- the latrine from Ch.7 (R4);
- the hand from Ch.14 (R6);
- "perfectly" and "Somebody had…" from Ch.16 (R13, R14);
- the knees from the Fenn sample (R1), if they ever read the voice bank (they will not; but the pattern shows when Ch.25 arrives).

---

## Cross-Reader Matrix
| Issue | Devourer | Critic | Hostile | Casual | Devoted | Severity |
|---|---|---|---|---|---|---|
| R4 Ch.7 latrine rebuilt | | ✓ | | | ✓ | **SHOULD FIX → blocking** (no set-piece reuse) |
| R1, R2, R5 voice-bank lifts (sample-09 ×2, sample-12) | | ✓ | | | ✓ | **SHOULD FIX → blocking** (voice-dna §6; RESERVED for Ch.25) |
| R5, R4-water, R28, R1 SPENT devices and resting body channels | | ✓ | | | ✓ | **SHOULD FIX → blocking** (SPENT, 0 more) |
| R6, R7, R9, R10–R15 reused frames (Ch.12, 14, 15, 16) | | ✓ | | | ✓ | **SHOULD FIX → blocking** (no reuse) |
| C1–C4 Valens's wipe, idiom, borrowed frame, re-staged protocol | | ✓ | ✓ (C3/C4) | | ✓ | **IMPORTANT** (card law) |
| L1–L4 logic and fact | | | ✓ | | ✓ | **SHOULD FIX** (cheap) |
| C5–C10, R19–R27 doubling, bleed, anadiplosis, in-chapter doubles | | ✓ | | | | INVESTIGATE → **fix** (cheap, tested) |
| S1 procedure / S4 hawker parade | ✓ | | | ✓ (frictions) | | SHOULD FIX → **trim only** (R22, R23, R24). The procedure carries the theft's tension, and the hawkers are the outline's crowd. |

---

## Revision Recommendations (Ranked)
*All 56 strings below were applied together to a scratch copy and run through `check_chapter.sh 17`, `shape_check --strict`, `tic_report.py --gate` and `--echoes 17`. All are clean and echo 0. Strings that tripped a gate on my first tries are listed under "Do not use".*

| # | Location | Problem type | What happens now | Why it fails | Revision direction (exact) | Project rule? |
|---|---|---|---|---|---|---|
| L1 | l.105 | Logic | `"The seal is my father's," said Plautia. "I know it from here. Read it to me."` | It contradicts l.155's "Which is that?" | → `"Is that wax my father's?" said Plautia. "I cannot tell it from here. Read it to me."` (a blunt question: her fingerprint) | No |
| L2 | l.423 | Logic | `a letter will come from this house,"` | Said in the forum. | → `a letter will come from my brother's house,"` | No |
| L3 | l.473 | Fact | `and the horses' gilding gone green along their bellies.` | Gold does not patinate. | → `, its horses green along their bellies where the gilding had long since worn away.` | No |
| L4 | l.225/227 | Clarity | Two Mara paragraphs running, the second re-tagged. | The Ch.16 L5 shape. | Merge: `"Whenever somebody wants to look. He is in the colonnade. Celer. The clerk has taken…` | No |
| C1 | l.203 | Character (SPENT gesture) | `He wiped one hand on his thigh, then the other. The flour stayed. He took the leaf…` | Valens's third wipe-before-handling (Ch.9, Ch.15); SPENT. | → `He took the leaf by its edges, a hand to each, and his thumbs left flour on the wood of the frame.` | Yes: Valens wiping or drying his hands before taking an object is CLOSED |
| C2 | l.233 | Voice (card) | `They'd carry her off a cliff for him, if he paid.` | An idiom and a hyperbole in Valens's mouth. | → `They'll take his money too, if he offers it.` | No |
| C3 | l.291 | Voice (borrowed frame) | `I walked at her back for two summers and two winters.` | Plautia's Ch.16 l.372 skeleton; "at her back" ×3 here. | → `He'll talk at her till she agrees to something.` (his read of a man; wrong in a mundane way, as his card says) | Yes: one character's line skeleton is never reversed into another's mouth a chapter later |
| C4 | l.309 | Character (re-staged set) | `and stopped at her back, half a pace to her left.` | The Ch.16 porch protocol, "Never re-staged". | → `and stood a pace from her, between her and the forum.` | No |
| C5 | l.117 | Voice (walk-on doubling) | `Further back. Further.` | Word-doubling. | → `Further back.` | No |
| C6 | l.505 | Voice (walk-on doubling) | `Did you hear him? Mules!"` | "Mules!" ×2. | → `Did you hear him?"` | No |
| C7 | l.171 | Voice (bleed) | `The boy stared at her veil. "Lady." The doorway…` | The clerk's whole-line reply. | → `The boy stared at her veil. The doorway was empty again.` | No |
| C8 | l.521 | Voice (dilution) | `"Mistress. Would you say…` | It blunts the seamed man's "Mistress,". | → `"Would you say…` | No |
| C9 | l.255–259 | Voice (rested shape) | `…see him lose."` / `"Lose?" I said.` / `"His father thinks…` | Mara's echo-question, rested after Ch.16. | Merge into one grievance speech (his card: the longest speeches are about his family): `"I'd have liked to see him lose. His father thinks…` | No |
| C10 | l.331, 373, 401 | Character (role label ×25) | `the clerk said` / `The clerk took` / `The clerk finished` | He is named at l.329. | → `Onesimus said,` / `Onesimus took another bite` / `Onesimus finished his bread,` | Yes: once a walk-on is named on the page, the narration uses the name |
| C11 | l.173 | Character (pre-description) | `once, in the rain, he walked the whole forum round sooner than pass under a painter's plank."` | It pre-describes l.397's carry-round; the superstition becomes 5 beats. | → `he once sent a new litter back to its maker because a ladder had leaned against it in the yard."` | Yes: a character never pre-describes the image the next section dramatizes |
| C12 | l.421 | Style (SPENT sibling) | `Plautia stood where she was until the litter had left the forum…` | "stayed where [pron] was". | → `Plautia watched the litter out of the forum by its farthest corner.` | No |
| R1 | l.267 | Style (RESERVED sample-09 frame; resting channel) | `My knees gave, and the step was under me, with the case in my lap.` | sample-09 "my knees went, and I sat down" (Ch.25); the seat channel is resting. | → `I lowered myself onto the step with the case in my lap.` | Yes: sample-09's collapse is RESERVED for Ch.25 in any wording |
| R2 | l.21 | Style (sample-09 string) | `He said it to the cake.` | "said it to the" is banned by name. | → `His answer went to the cake.` | No |
| R3 | l.283 | Style (said-to cap; Ch.15 sibling) | `putting his questions to the black instead.` | The second "said to a non-listener"; Ch.15's ewe. | → `after the dun with his questions unanswered.` | No |
| R4 | l.519 | Style (set piece rebuilt) | Ch.7's latrine, in order, plus water running through the held moment. | Ch.7 l.76; SPENT device. | Whole paragraph → `There was. Fortuna was painted over the door, with her rudder and her horn of plenty. It was dim inside after the street, and cool, and the talk in it rang off the plaster: on the long seat, already, a fat man in a festival wreath sat elbow to elbow with two of the athletes, discussing the javelin. None of them so much as glanced at me. I took the nearest place and tried to think of nothing, and the fat man went on explaining the javelin to the athletes. He broke off and called along to me.` (Fortuna guarding latrines is attested in Roman latrines, e.g. at Pompeii.) | Yes: extend "a revisited place: its sequence and geometry are spent" to a revisited **kind** of place (latrine, bath, gate) |
| R5 | l.377 → l.473 | Style (SPENT held silence; sample-12) | `The bearers on the step had left off their talk. Among the temples a donkey was complaining…, past the city, past the walls…` | A held silence filled with movement and sound; sample-12's animal; anaphora. | Cut the paragraph (the silence after "To Rome." stands bare). Move the boys' sentence into the forum walk, after "with her basket in her lap.": `Past the city walls and the long road and the trees, not a sound reached us of the boys running. At the forum's north side…` | No |
| R6 | l.359 | Style (Ch.14 gesture) | `and it hung there in the sun … and drew it in.` | Ch.14 l.84, "hung … I drew the hand in". | `hung` → `waited`; `and drew it in.` → `and hid it in his toga.` The image and the rest of the sentence are untouched. | No |
| R7 | l.313 | Style (Ch.12 intro) + fact + ruler | `The toga was brilliantly new, with the dust of the Isthmus road along the bottom of it in a brown band a hand deep.` | Ch.12's stranger introduction; brown against the boy's gray; a 5th ruler. | → `The toga was brilliantly new, and the Isthmus road had powdered it down one side.` | No |
| R8 | l.177 | Style (doubles) | `with the sky still gray` … `in a white toga, very new, on a gray,` | Gray ×2 in two sentences; "new" said again at l.313. | → `in the cold before sunup` … `in a white toga on a gray,` | No |
| R9 | l.525 | Style (Ch.15 heat words) | `I finished, and it was slow, and then it was over.` | Ch.15's "It was slow, and stayed slow". | → `I finished, and it took an age, and then it was over.` (still the ugly sentence) | No |
| R10 | l.365 | Style (Ch.16 SPENT) | `with a vineyard and somebody to write his letters for him` | "a vineyard and a cough". | → `on a farm of his own, with somebody to write his letters for him` (no "vines": the god's "mountain of vines") | No |
| R11 | l.145 | Style (plan echo) | `among Plautia's letters` | Ch.16 "among my letters", possessive-swapped. | → `between two of Plautia's letters` | Yes: a chapter that executes the previous chapter's plan greps the plan's sentences |
| R12 | l.197 | Style (Ch.16 frame) | `and had gone in to his dinner.` | Ch.16 "had gone in to its suppers". | → `and called for his dinner to be brought.` | No |
| R13 | l.87 | Style (Ch.16 anchor skeleton; verdict cap) | `The writing on these was larger. Somebody had taken pains for the emperor's year.` | "Someone had cut his teeth on it."; a second absent-workman verdict. | → `The writing on these was larger and rounder, for the emperor's year.` | Yes: a finalized chapter's anchor and underline sentences are SPENT as skeletons |
| R14 | l.421 | Style (Ch.16 underline frame) | `her face under it was perfectly dry and very white.` | "her face was wet and perfectly composed". | → `her face under it was very white, and dry.` (the wet/dry contrast stays, unpointed) | (as R13) |
| R15 | l.371 | Style (Ch.14 phrase) | `a line in a magistrate's book` | Ch.14 "a line in a book in a record office". | → `an entry in a magistrate's book` | No |
| R16 | l.299 | Style (Ch.15 exit verb) | `He made for the colonnade` | Felix's Ch.15 exit verb. | → `He left for the colonnade` | No |
| R17 | l.537 | Style (Ch.16 road) | `the way lay flat and straight through market gardens` | Ch.16 "dead straight over the flat land". | → `the way ran on through the market gardens` | No |
| R18 | l.493 | Style (sample-01 tray) | `a man had a tray of new silver hung from a strap and was shouting it.` / `on the tray` | sample-01's slung tray (audit W-06). | → `a man stood behind a folding table of new silver, shouting it.` / `on the table` | No |
| R19 | l.209 | Style (#8 anaphora triad) | `…with his lips shut. He read all of it. He read the witnesses.` | "he read" ×3. | → `…with his lips shut, to the end of the witnesses.` | No |
| R20 | l.79 | Style (anadiplosis ×2) | `into a shallow tray and the tray was filled with black wax, and the wax was crowded` | Cap 1 per chapter. | → `into a shallow tray of black wax, and the wax was crowded` | No |
| R21 | l.303–305 | Style (anadiplosis) | `but one.` / `In front of that one stood the scaffold.` | Third pick-up. | → `but one, with the scaffold in front of it.` and l.305 opens on `Men had been patching…` | No |
| R22 | l.489, 495 | Style (#3/#8 hawker parade; doubling) | `The god's pine! The winners' pine!…` / `Not for the athletes, the athletes aren't let have them,` | Three exclamation triads in a row; doubling. | → `"The god's pine! Wear what the winners wear!"` / `"Lucanian, all of them! The athletes aren't let have them,` | No |
| R23 | l.67 | Style (in-chapter clock ×3) | `"Well?" Plautia asked from the table. Overhead the ladder creaked.` | The third creak, wedged into dialogue. | Cut `Overhead the ladder creaked.` (l.45 and l.93 keep the clock) | No |
| R24 | l.397 | Style (double) | `under six paces of planking that would have carried a loaded cart.` | The scaffold's strength again (l.305 "A mule could have stood on it."). | → `under six paces of good planking.` (his "good shoes": irony, unpointed) | No |
| R25 | l.397 | Style (double) | `through the white sun of the forum` | The forum is "white" ×3. | → `through the full sun of the forum` | No |
| R26 | l.15 | Style (in-chapter double) | `sold off a cloth in the market:` | The clerk's l.407 line (audit I-20). | → `sold in the market by weight:` | No |
| R27 | l.283, l.537 | Style (narrator device) | `the two others nobody had wanted at any price` / `an old wall nobody had mended and a gate nobody kept` | "[thing] nobody had [verb]ed" ×4; #1/#8. | → `the two he had failed to sell` / `an old wall gone to rubble in places and an unwatched gate` (l.315's "where nobody had stitched it" stays) | Yes: WATCH "[noun] nobody had [verb]ed", ≤2 per chapter |
| R28 | l.485 | Style (resting channel) | `My hands had begun to shake. I put them into the folds of Myrrhine's dress and they shook there…` | Hands are resting until Ch.20; a shaking channel was spent in Ch.12. | → `Between my shoulders and all down my back, under Myrrhine's dress, the skin prickled from there to the first broad step, and then the street took us.` | Yes: the at-risk block carries a one-line "body-rebel channels: resting / available" schedule |
| X1 | l.35 (end) | Restore | The scaffold is first met in the boy's line (l.161). | Plant it, and end the paragraph on an act. | Append `At the office door they had set her down beside a builders' scaffold, and she had walked in under it.` | — |
| X2 | l.15 (end) | Restore | | Pays off Ch.16's hope for "the young one". | Append `The young one's table, across the room, stood bare, its stool pushed in and a wine ring dried on the wood.` | — |
| X3 | l.555 | Restore (level 2) | The run is about 100 words. | It lengthens the unfinished action. | After `My breath went short, then raw.` add `A stitch caught me under the ribs, and I ran through it. The carter called after us, wanting to know which of us was winning. The road back to the city gate was empty. By the first gardens Felix's crown was half bald, and Valens's fingers were sticky with it.` | — |
| X4 | l.459 | Restore | `We left the colonnade for the sun.` | | → `We left the colonnade for the sun, and the paving was hot underfoot, even through my sandals.` | — |

### Fix order: Logic (L1–L4) → Character (C1–C12) → Reuse and law (R1–R28) → Restores (X1–X4)

**Kept on purpose (and why):**
- **The first line, the closing paragraph and the bare "No."**: byte-identical (md5 checked).
- **The fig cake, the stylus and the thumb**; "The gray one, then. We had wanted the other."; "The ladder said what he thought of that."; "His head had not moved."; "It was done well or it was a botch, and it was a botch."
- **The shade-line sentence**, apart from R6's two verbs.
- **"Mistress,"** in the seamed man's mouth: a menace recall of his own Ch.12 word, the only one now.
- **The trainer's "Murmillo"** beat. It is a third stranger reading Valens as a fighter (Ch.12's bettor, Ch.16's baker, reported), but it is comic, unnamed, and pays off "it fooled nobody who had ever seen a baker". WATCH: no fourth before Ch.21's trainer.
- **The six backfill inserts.** The design asks for them, and each is triggered on the page.
- **"In a colony two names made a year."**: the one gloss the reader needs to follow the shelves.

**Do not use** (each tripped a gate on my first try):
- "I sat on the step with" (voice-wear; Ch.10);
- "one side of it was" (voice-wear; Ch.12);
- "the far end" (tic: Ch.1, 5);
- "up off the" / "came up off the" (tic: Ch.3, 4);
- "the whole way" (tic: Ch.4, 5);
- "and sat down" (tic: Ch.5, 7);
- "had set up" (tic: Ch.5, plus the chapter's sausage-man);
- "put it away" (tic: Ch.5, 15);
- "Plautia waited until the" (echo: Ch.16);
- "my father's seal" (echo: Ch.16);
- "under the window" (echo: Ch.16);
- "behind us the" (echo: Ch.8);
- "by the door" (tic: Ch.2, 7);
- "out of sight" (tic: Ch.6, 7);
- "tucked it into" (echo: Ch.11);
- "let go of" (tic: Ch.3, 7);
- "Valens was still" (echo: Ch.14);
- "what was left" (tic: Ch.2, 9);
- "came up through" (echo: Ch.1).

**Rejected by my own scan:**
- "and the heat of" (Ch.15's heat scene);
- "the soles of my" (Ch.15's heat scene);
- "the skin of my" (Ch.3);
- "it was dry and" (Ch.3);
- "it was a long" (Ch.3, 4);
- "stood in front of" (sample-05);
- "to the kitchen for" (Ch.9).

---

## Strengths to PRESERVE (do not touch in polish)
1. **The opening, byte-identical:** the dust, the tags, "Behind me the clerk was eating figs.", the fig cake, "The gray one, then. We had wanted the other."
2. **The bribe:** the napkin, the swan spoons, "He let the corner fall back.", the bundle under the cake, "He rose, taking the cake."
3. **The ladder** and "The ladder said what he thought of that."
4. **The swapped book:** "Nobody had taken it anywhere. A copyist would have had a long walk."; "*C. IVLIVS. VALENS.*"
5. **The reading against the sawing:** "*Gave*." He swallowed.; Doris; "as to a child who had asked twice"; "rasping like a nail drawn down a bedsheet"; "She is clumsy … You were at the lion's paws."; "His head had not moved."; the botched knot.
6. **The clerk drawing the book from the wrong year at the first try.**
7. **The lane:** "Valens read my face before he read the case."; lips shut; "Nine." / "Three of them are dead."; "That's out of the emperor's year." / "It's mine."; "I'd have liked to see him lose."; "He'll eat his bread."; "He can look at it, and leave her be."
8. **The colonnade, entire:** "older than his laughing had been"; the ears; "Free air's put flesh on you."; "Lady didn't ask,"; "Did he eat, this morning…?" / "Like a wolf."; the honey "too hot"; "And this will be Mara."; "My name, in his mouth."; the shade line; "You were the best money I ever laid out" / "You hired me,"; "Papers are no more than that."; "Her brother's paying my road," / "To Rome."; "Nobody's going to rob the proconsul this morning."; "Not today, legate."; the sunshade; "Let her go on asking."; "lighter by two boards"; "like a bench somebody had left in his way"; "You were never in."; the Sicyonian swans.
9. **The parting:** "You came out under the poles." / "You were by yourself." / "That was where he was standing."; the knife; "Did you stand on my hem?"; "her curtain stayed down".
10. **S4:** the three dead witnesses; the seamed man "with his feet in the water"; "He has,"; Judaea weeping on the new coins; the fat man's javelin question and "Off."; "For Felix … He missed the boys."; "I saw where his feet stopped."; "That's the breeze,"; "Asking him how."; "We ran."; **the closing paragraph, byte-identical.**

---

## PATH TO 8.5 (mandatory; the Floor is 8.0)

**Prose & Voice 8.0 → 8.5 requires:**
- **The earlier set pieces retired:** R4 (Ch.7's latrine; the highest-value single fix), R6 (Ch.14's hand), R7 (Ch.12's introduction).
- **The voice-bank lifts out:** R1 (sample-09's collapse, reserved for Ch.25), R2 (sample-09's "said it to the"), R5 (sample-12's complaining animal), R18 (sample-01's tray).
- **The SPENT devices out:** R5 (a held silence filled with sound), R4 (water running through a held moment), R28 and R1 (resting channels).
- **The Ch.15 and Ch.16 carry-overs out:** R9, R10, R11, R12, R13, R14, R15, R16, R17.
- **The in-chapter doubles and caps cleared:** R19–R27, plus the logic set L1–L4.

The stopping sentence (re-verbed only), every underline, both ugly sentences, every anchor, the first line and the closing paragraph all stay.

**Characters 8.5 → 9.0 (expected with C1–C12):**
- Valens's SPENT wipe goes (C1).
- He speaks literally (C2) and in his own words (C3).
- The Ch.16 porch protocol is not re-staged (C4).
- No walk-on doubles a word (C5, C6, R22).
- "Lady." is the clerk's alone (C7), and "Mistress," the seamed man's alone (C8).
- The echo-question rests (C9).
- The narration uses Onesimus's name once he has one (C10).
- The superstition is told once and not pre-described (C11).
- The SPENT "stood where she was" goes (C12).

**Apply in one pass. The strings are exact (see the table), or run the tested script from /home/user/Books:**
```
python3 /tmp/claude-0/-home-user/63791ee5-159c-5791-9429-07920f8d9417/scratchpad/ch17-eval-fixes.py \
  books/the-hour-of-ash/manuscript/chapters/chapter-17.md \
  books/the-hour-of-ash/manuscript/chapters/chapter-17.md
```
- The script asserts exactly one match per string, and aborts without writing on any miss.
- Then run `bash books/the-hour-of-ash/tools/check_chapter.sh 17` and `python3 tools/shape_check.py books/the-hour-of-ash --strict`, and refresh the chapter's word-count header comments (lines 3–7 still describe the pre-polish page).
- The swap harness used for the test is `/tmp/claude-0/-home-user/63791ee5-159c-5791-9429-07920f8d9417/scratchpad/ch17-eval-swaprun.sh`. It always restores the original from `ev17/ch17-original.md` and prints both checksums.

**What the tested run produced (all 56 strings applied together; fixed copy sha256 `e0b21e0d…`, md5 `95c1e145…`):**

| Measure | Before | After |
|---|---|---|
| Words (shape_check / style / show_tell) | 6,935 / 6,947 / 6,951 | **6,935 / 6,947 / 6,951** (every cut offset by restored narration; floor 6,900 ✓) |
| Dialogue (show/tell / shape) | 33.0% / 33 | **32.8% / 33** (30–40 ✓) |
| Median sentence (shape / metaphor) | 11 / 11 | **12 / 12** (low gear 9–12 ✓, at its top: the cuts removed short sentences) |
| Breaks / signatures | 3 / `short-punch` → `quiet` | unchanged |
| First line / closing paragraph / bare "No." | | **byte-identical** (md5 checked) |
| `check_chapter.sh 17` | clean | **all clean**: style (simile 1.2/1k, em-dash 0, foreshadow 0); grammar 0; rhythm 0; show/tell no flags; voice-wear strict clean; tic gate clean (and-chains 2/9, credential 0, pivots 0); **echo 0**; command echo none; spoken-line echoes none; metaphor 1.3/1k |
| `shape_check --strict` | CLEAN | **CLEAN** (`17 6935 3 33 12 short-punch quiet`) |
| Gesture classes (gate) | clean | **clean** |
| #11 (firm) | 4 (0.58/1k) | 4 (0.58/1k) |
| Paragraph-final negations (firm) | 9 (1.30/1k) | **7 (1.01/1k)** ✓ |
| Indefinites in narration | 20 | 16 (WATCH) |
| Voice-bank lifts (sample-01, 09 ×2, 12) | 4 | **0** |
| Earlier set pieces / introductions / gestures rebuilt (Ch.7, 12, 14) | 3 | **0** |
| Ch.15/16 frames carried over | 9 | **0** |
| SPENT devices / resting channels on the page | 5 | **0** |
| Body-part rulers | 5 | **3** |
| Anadiplosis | 3 | **1** (l.311's loose one) |
| Anti-AI | 9/20, −1.625 (watch) | **8/20, −1.25** (clean band) |

**Expected:** Prose 8.5 (merit 8.0 → 8.5 on 56 cited changes; the +0.5 limit holds) and Characters 9.0 (8.5 → 9.0) → **Floor 8.5, Average 8.86** (9.0 / 9.0 / 9.0 / 8.5 / 8.5 / 9.0 / 9.0). Casual 9.0 holds; CVI-L 9.7 holds.

---

## Pacing check (one line for `feedback/progress.md`)
**Ch.17 (cycle 0):** In medias res, *theft first, how-we-got-here in pieces*, between Ch.16's Parallel and Ch.18's Single-scene ✓.
- **Length:** 6,935 words (target 7,400, −6%, inside the 6,900–7,900 range; not padded; unchanged after the PATH).
- **Dialogue** 33% (30–40 ✓); **3 breaks** ✓; **gear median 11** (low ✓; 12 after the PATH).
- **Signatures:** `short-punch` → `quiet` (Ch.15 `long-spiral` → `quiet`, Ch.16 `dialogue` → `question`: no three running).
- **Neighbours:**

  | Ch | Words | Gear (median) | Dialogue | Approach | Breaks | Open → close |
  |---|---|---|---|---|---|---|
  | 15 | 7,479 | high (16) | 35% | Chronological | 3 | long-spiral → quiet |
  | 16 | 7,175 | mid (14) | 46% | Parallel | 6 | dialogue → question |
  | **17** | **6,935** | **low (11 → 12)** | **33%** | **In medias res** | **3** | **short-punch → quiet** |
  | 18 | 2,800 planned | mid | 30–40% | Single-scene | 0 | I-statement → punch |

- **The gear steps down high → mid → low**, as the ledger planned, and the dialogue share moves 35 → 46 → 33. The three long chapters (Ch.15–17, 7.5k → 7.2k → 6.9k) shorten, and none flattens into the next. Ch.18 (2,800) breaks the run.
- **Emotional slot ✓:** after the heat chapter (Ch.15) and the two-women chapter (Ch.16), Part One's action climax runs on comedy under legal threat, with no violence. The variance is the design.
- **Value shift ✓:** hidden (−) → the leaf (+) → seen (−) → trusted (+) → named by Celer (−) → he leaves blind (+) → watched (−) → running, a sail going up (−).
- **Pull ✓:** the action is unfinished, as the ledger asks. The sail is Ch.18's first question.
- **Slow patches:** S1's procedure and S4's crowd. The PATH trims both (R22, R23, R24) and lengthens the run (X3).
- **Book:** 96,713 words against 103,800 cumulative target (−6.8%). Projected about 242k against the 220k floor ✓ and the 245k target (slightly under: watch, never pad).

**Verdict: OK.**

---

## Cross-Book Pattern Detection (Ch.1–17)
1. **The voice bank is leaking by structure, not by string.**
   - sample-09's collapse ("my knees went, and I sat down") and its "said it to the" frame; sample-12's offstage animal "complaining about"; sample-01's sausage seller and tray (audit W-06).
   - These are four samples' signature beats in one chapter. Three are frames that the 5+-word sample check cannot see.
   - **Proposal (UPDATE RULE, root `tools/tic_report.py` and the template):** a **sample-frame registry**. Each sample's signature beats are written as patterns, e.g. `\bknees (went|gave)\b.{0,40}\b(sat|under me)\b`, `\b(said|told) it to the\b`, `\bcomplaining about\b` (animal subject), `\btray (slung|hung)\b`. Reserved samples (sample-09 → Ch.25, sample-10 → heat) fail on sight before their chapter.
2. **Whole earlier set pieces return when the situation recurs.** Ch.7's latrine came back as a latrine, in the same inventory order. The Ch.10 rule ("list the previous chapter's set pieces and stage the new one differently") looks back only one chapter.
   - **Extend it:** when a scene's *kind* recurs anywhere in the book (latrine, bath, gate, a hand held out and withdrawn, a stranger's introduction), grep every earlier instance and change the inventory and its order.
3. **The previous chapter's best sentences come back as skeletons:**
   - "Someone had cut his teeth on it." → "Somebody had taken pains for the emperor's year.";
   - "her face was wet and perfectly composed" → "perfectly dry";
   - Plautia's "I walked in front of him for two years" → Valens's "I walked at her back for two summers".
   - **Rule:** at finalize, the evaluator's underline and anchor sentences are added to the at-risk block **as skeletons**, not only as strings.
4. **The bible's body-rebel rest schedule did not reach the writer.**
   - "Rest it (and hands, and voice) until Ch.20" sits in the after-Ch.11 block, and Ch.17 used both the seat and the hands.
   - **Proposal:** a one-line *body-rebel channels — resting / available* entry at the top of the newest at-risk block, refreshed every chapter, so it travels in every writer prompt.
5. **Plan-to-execution echoes.** When a chapter carries out the previous chapter's plan, the plan's words come with it ("among my letters", "with my father's seal on it", "a step down", "a baker's oven built against it").
   - **Rule:** grep the plan's sentences before drafting the execution.
6. **What varies, as it should:**
   - the structure (In medias res after Parallel);
   - the opening (`short-punch`) and ending (`quiet`, mid-action);
   - the gear (low);
   - the anchor's engine (comedy; a bystander's appetite);
   - the body-rebel channel (the bladder: new to the book);
   - the villain's first scene (no violence, no monologue; pleasantries as knives).

**Bookkeeping (orchestrator):**
- **Re-sync the bible's Ch.17 blocks to the final page.** They quote the Writer's draft. Examples of strings that are not on the current page:
  - MARA: "A thing that was lost was nearly always only put back wrong."; "My Latin was stiff, and too quick."; "Twice. In the street, in the dark." (page: "by the fuller's").
  - PLAUTIA: "I will mind your door."; "since I was sixteen" (page: nineteen); "Is that seal my father's … or his freedman's?" / "By what?".
  - CELER: "Come out tomorrow and sit with us … Right at the governor's back"; "Didn't you, Plautia?"; "Then go and hear who won it."; "Come and see me after the games, Lupus."; "Lupus" ×3 (page: 2).
  - ONESIMUS: "The old years are at the back, lady. Up the ladder."; "Then the last."; "He'll have run." in the colonnade; "If you hear who won the boys".
  - VALENS: "What was it she gave you?"; "Her woman will be on the quay before us."; "He'll be asking him who won." (page: "Asking him how.").
  - The walk-on note: "The biggest had ears like knots of dough"; the dog "delighted".
  - The at-risk Ch.17 counts still describe the Writer's draft.
- **After the PATH, also sync:**
  - L1's "Is that wax my father's?"; C2, C3, C4 (Valens's new lines; no "at her back");
  - Onesimus named in narration after l.329; the knees and the hands → the step and the skin;
  - the latrine (Fortuna, dim and cool; no marble, holes, channel or sponge);
  - Celer's toga "powdered … down one side"; the hand "hid … in his toga";
  - "a farm of his own"; the litter anecdote replacing the painter's plank;
  - the young one's bare table with a wine ring; the run's stitch, carter, empty road and half-bald crown.
- **At-risk after Ch.17, add (post-PATH):**
  - **Valens's wipe or dry before handling:** CLOSED at 2 (Ch.9, Ch.15).
  - **sample-09's collapse frame:** RESERVED for Ch.25, any wording. **sample-12's "complaining about"** for an animal: SPENT. **sample-01's slung or hung tray:** SPENT.
  - **The latrine:** SPENT as a set piece (Ch.7, Ch.17); no third.
  - **A hand held out toward a person and withdrawn:** SPENT (Ch.14, Ch.17).
  - **"perfectly [adj]" for a face:** CLOSED at 1 (Ch.16). **"[S]omebody had [verb] [object] [for/on] it" inference sentences:** ≤1 per chapter, and never the anchor of the chapter before.
  - **"at her back":** CLOSED for the Valens–Plautia protocol; Ch.22 stages them some other way.
  - **A stranger reading Valens as a fighter:** WATCH at 3 (Ch.12, Ch.16 reported, Ch.17); none before Ch.21's trainer.
  - **Walk-on hawker cries:** no exclamation triad in a row.
  - **"Mistress,"** as the seamed man's word: used; never his line again.
  - **Body rebels:** seat and hands still resting until Ch.20; the bladder SPENT; skin prickling (post-PATH) used.
- **Entity and handoff cascades:**
  - The ship "with the goose carved on her stern" goes "on the afternoon breeze". Ch.18 opens on the quay that same afternoon (audit W-08).
  - Mara has Plautia's grandfather's pen-knife in her belt; Myrrhine has said "I shall know whose house", and Valens has said "Her woman can come to Puteoli for it." (audit W-09).
  - The leaf is under Valens's belt; Celer holds the cut book (W-10).
  - After the PATH, Felix's crown is half bald and sticky.

---

## VERDICT
**POLISH. Gate NOT MET.**

| Measure | Result |
|---|---|
| Genesis Floor | **8.0** (Prose & Voice, merit; no cap) |
| Average | **8.71** |
| Casual | **9.0** |
| Scores | Originality 9.0 · Theme 9.0 · Characters 8.5 · **Prose 8.0** · Pacing 8.5 · Emotion 9.0 · Immersion 9.0 |
| Pacing | **OK** |
| CVI-Launch (CVI-L) / CVI-Legacy | **9.7** / 6.9 (provisional) |
| Mechanical suite | all clean (echo 0, spoken-line echoes none, tic gate clean, voice-wear strict clean, shape CLEAN) |
| Foreshadowing | 0 (gate and reading) |
| AUTHOR-CP3-5 / CP3-3 / END-1 | ✓ / ✓ / ✓ |
| Non-negotiables (fig-eating clerk; one archive recognition; Celer, no violence and no monologue; Valens's papers; luck and boredom) | ✓ all |
| Heist-competence cascade | none (WATCH: six expertise beats, each undercut) |
| Celer distinct from Plautia | ✓ (strongly) |
| Memory triggered by the scene | ✓ |
| Explanation density | ✓ (4 firm, 0.58/1k) |
| Paragraph-final negations | ✓ 1.30/1k → 1.01/1k |
| No comparison in Valens's speech | 1 idiom → C2 |
| Command echoes / borrowed whole lines | 0 / 0 |
| Tics | catchphrases 0; gate classes clean; **Valens's SPENT wipe, walk-on doubling, said-to ×2, anadiplosis ×3 → fixed** |
| Reuse (sample-01/09/12; Ch.7, 12, 14, 15, 16) | **FAIL** → cleared |
| SPENT devices / resting channels | **FAIL ×5** → 0 |
| AI patterns | 9/20 (watch) → 8/20 (clean) |

**Failing dimension:** Prose & Voice (8.0 on merit). The fixes are surgical and were tested together (L1–L4, C1–C12, R1–R28, X1–X4; 56 strings). The result has the same 6,935 words, dialogue 32.8%, median 12, and every gate clean; the first line, the closing paragraph and every anchor are kept. Then run E (gates) and F (re-evaluation). **Expected after one cycle: Floor 8.5 / Average 8.86 / Casual 9.0 / PASS.**

Part One's climax is the funniest chapter in the book, and it earns it:
- the heroine steals her lover's freedom out of a bound book while a bored clerk eats figs and reads the dowry aloud through a mouthful;
- the villain stops at the edge of a scaffold's shadow and looks at his own hand as if somebody else had put it out.

What holds it below the gate is small and countable. The chapter keeps reaching back for beats the book has already spent or set aside: Ch.7's latrine; the collapse the voice bank keeps for Fenn; the hand from the night Mara learned the year; a held silence filled with a complaining animal; last chapter's best sentences in new nouns.

**BIAS CHECK:** This evaluation was produced by the same system that wrote the prose. Confidence in scores above 8.0 requires external validation (beta readers, editors, comp analysis).
- **R4 (the latrine) is a judgment about a set piece, not a string.** A reader who holds that Roman latrines simply looked like that would call it accuracy. I count it because the description is Ch.7's, in Ch.7's order (bench, three walls, holes, channel, sponge at the entrance, men on the bench mid-topic), and the bible spends a revisited place's sequence as well as its words.
- **Valens's wipe (C1) is not capped.** It is three uses in three non-consecutive chapters, and its rate is far under 0.3/1k. A stricter reader could call it "a class that recurs chapter after chapter" and cap Characters at 7.5 until C1 lands. C1 is in the tested set either way.
- **R6 re-verbs the chapter's stopping sentence.** I judge the image ("as though somebody else had put it out") to be the stopping power, and Ch.14's verbs ("hung", "drew … in") to be the reuse. A reader who prizes "and drew it in" as the cadence would hold R6 as optional; then Prose rests on the other 27 R-items.
- **The restores (X1–X4, R5b, about 110 words) are new narration written by the evaluator** to keep the word count equal, as the brief asks. Each passed every gate and my scans. They are offered as work orders: the editor may substitute their own, provided the count still nets to zero.
- **Characters 8.5 → 9.0 and Prose 8.0 → 8.5 are forecasts, not scores.** Originality, Theme, Emotion and Immersion at 9.0, Casual 9.0 and CVI-Launch 9.7 are one-chapter judgments by the system that wrote the book.
