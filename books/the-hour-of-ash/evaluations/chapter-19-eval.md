# Evaluation: Chapter 19 — Puteoli (run 2) · PART TWO opens
**Evaluator:** book-evaluator (independent; did not write or revise this prose) | **Date:** 2026-10-21
**Text evaluated:** `manuscript/chapters/chapter-19.md` (sha256 `7bea5358…`, md5 `b0500c45…`). This is the page after writer → dialogue-polish → hook-craft → disruptor → continuity repair (W-01…W-14). It runs **8,436 prose words** by shape_check (8,458 style, 8,458 show_tell). Dialogue is **24.1%**.

**Read against:**
- the book's CLAUDE.md;
- STATE.yaml `guardrails` and `resolved_author_decisions`, especially **AUTHOR-END-1**, CP3-3, CP3-4 and CP3-5;
- `feedback/progress.md`: the Ch.19 brief, the **"seam" ruling**, and the open children's-citizenship note;
- voice-dna §0–§8, and **sample-13** (this chapter's register), plus sample-07 (Ch.42), sample-11 (Ch.20) and the rest of the voice bank;
- character-bible.md:
  - every at-risk and spent block, from "after Ch.1" to "after Ch.19";
  - the POMPONIA GRATA card;
  - the Ch.19 walk-on notes;
  - the Retired / at-risk table;
- outline `## Chapter 19` and Ledger row 19;
- foundation §4f (the hand-at-a-threshold architecture);
- `evaluations/chapter-18-eval.md`;
- chapters 17–18 for pacing;
- `evaluations/disruption-chapter-19.md` and `evaluations/continuity/chapter-19-audit.md`, for what was applied and what was cut.

**Genre profile and settings:**
- **Genre:** commercial historical romance / time-slip; comp *Outlander*.
- **Anti-AI band:** commercial (0–8 clean, 9–11 watch).
- **Explanation-density cap:** commercial, >0.8/1k.
- **Engagement (book):** empathy 55 / fascination 30 / self-insertion 15. This chapter leans on **fascination** (the period world, the known date) more than any since Ch.5.
- **Dimension 7:** IMMERSION.

**Measured** (`bash books/the-hour-of-ash/tools/check_chapter.sh 19`, run from /home/user/Books): **clean on every gate.**
- style: simile 1.1/1k, em-dash 0, foreshadow 0;
- grammar 0 errors; rhythm 0;
- show/tell: no flags, dialogue 24.1%;
- voice-wear strict: clean;
- tic gate: clean (and-chains 5/9, credential asides 0, pivots 0, "So" 0; every gesture class under cap);
- echo 0;
- metaphor 1.8 fig/1k, median 18;
- `shape_check --strict`: `19 8436 4 24 18 scene-set long-fade`, CLEAN.
- `tic_report.py --echoes 19`: **none / none / none** (echoes, command echoes, spoken-line echoes).

**My own scans** (scratch only, not gates):
- 3–7-grams of Ch.19 against Ch.1–18 and all 13 voice-bank samples, **stop-word-bounded strings included**;
- in-chapter repeated 3–5-grams;
- narration-only scans: paragraph-final negations, present-tense verbs, "so that", indefinites, "the way / as if / like a", "before [X] had";
- by hand: every SPENT, CLOSED, RESERVED and WATCH item in the bible, grepped by frame as well as by string; every Valens line checked for comparison; every order checked for an echo.

**The fix set was tested together on a scratch copy.**
- The copy was swapped into the manuscript path, and the real `check_chapter.sh 19`, `shape_check --strict`, `tic_report.py --gate` and `--echoes 19` were run from /home/user/Books.
- The original was restored after every run and its checksum verified (sha256 `7bea5358…`, md5 `b0500c45…`). **I did not edit the manuscript.**

*(l.N = line number in the current `chapter-19.md`; the header comments are l.5–9.)*

---

## HEADLINE
**CVI-Launch (CVI-L):** 8.85 (8.35 + 0.5 strong anchor) | **CVI-Legacy:** 7.2 (provisional) | **Genesis Floor:** **8.0** | **Genesis Average:** **8.71** | **Casual Reader:** **8.5**

**Engagement type:**
- **Fascination** leads in this chapter: the reader knows the date and the mountain, and Mara knows them too.
- **Empathy** is second: the ankle held in the dark, the girl's brooch, and the boy whose grandfather sold eels.
- **Self-insertion** is third: arriving in Roman Campania and renting two rooms behind a dead cobbler's shop.

**Divergence alert:** none. The gap between CVI-L and the Floor is 0.85.

**Gate (Floor ≥ 8.5 AND Casual ≥ 8.5 AND pacing OK AND gates clean): NOT MET at cycle 0.**
- Casual 8.5 ✓; pacing OK ✓; mechanical gates clean ✓.
- **Prose & Voice holds the floor at 8.0, on merit, with no cap.** The sentences are 8.5 and better: "Seventy-nine." at the finder, and "it stayed a picture of a door." What holds them is a cluster of breaches that no gate sees:
  - **three held moments measured by things moving past, a SPENT device ("0 more anywhere"):**
    - the cart at the tomb (l.351): "I stood in the road in front of it while a cart went by behind me". This is Ch.9's oil cart and Ch.1's car in the rain.
    - the family going in and the shadows lengthening (l.373). The bible names casting a shadow as one of the banned measures.
    - the porters passing while the clerk reads (l.93).
  - **the previous chapter but one's set piece rebuilt on the same object.** At l.93 the leaf is read "every line, the witnesses and all … Then he shut it". In Ch.17 Valens read it "to the end of the witnesses." / "He shut it.".
  - **a frame from Ch.17, two chapters on.** The girl's line comes "in a Greek that was suddenly as good as anybody's" (l.69). Ch.17's trainer spoke "in a Greek that was not Corinth's", and that use is logged as "once".
  - **comparison domains reused:**
    - "as warm as the hood of a parked car" (l.353) is the **4th car comparison** (Ch.2 "you could have parked a car in", Ch.5 the car alarm, Ch.13 the suitcase on a car roof). It also builds a forced warm-as / cool-as pair at the anchor.
    - "the first tunnel I had been in since the Broad Street subway" (l.149) is the subway's 2nd comparison (Ch.3, the City Hall stairs) and the 3rd "It was the first [X] I had [V]" (Ch.7 ×2).
  - **the disruptor's left clause at the door,** "it had no business to be cool at all" (l.355). **My judgment: cut it.** It tells the reader the anomaly one sentence before the to-and-fro test shows it (white warm, jamb warm, leaf cool). That makes it the chapter's clearest #11, and it sits at the anchor.
  - **a cluster of narrator moves at density:**
    - narration "so that" ×7 (WATCH >4);
    - five comprehension reports (the priest's Greek; half the mother-in-law's; all of her slow question; "I understood every word"; the baker lost), which is a cousin of the SPENT "first Greek I understood" move;
    - "and stayed", CLOSED for the book after Ch.15, at l.151;
    - "Then her eyes went past the girl to us" (l.65), from the SPENT gaze-arrival family;
    - "the size of a" ×3 in the chapter, one of them a whitewash patch "the size of a door" beside the door beat;
    - six "And…" speech rejoinders across four speakers (WATCH ≤4, one owner).
  - **two logic slips:**
    - "well again by Rhegium" (l.13) runs the voyage backwards: Rhegium sits at the Straits' southern mouth;
    - the door is "closed … once more" (l.265) without having been opened.
- **Characters sits at 8.5:**
  - Grata's command "Sit there. Eat that." (l.387) is her card's own rhythm example ("Eat this. Hold that.") and Gloria's spoken "Eat that," in Ch.1.
  - "He considered my hand on the door." (l.359) is the 8th "considered" beat book-wide, running Ch.18 → Ch.19. Ch.13 cut three.
  - "What for?" (l.369) is a whole line in its 3rd chapter and 4th mouth (Ch.8, Ch.9).
  - Valens answers Felix's barrages with an order twice ("Hold her.", "Eat your beans."). This is WATCH, not changed.

**The fix set: 27 swaps, tested together** (script below). All are cuts or near-even swaps.
- **8,279 words** (shape_check), against the 7,900 floor;
- dialogue **24.6%**; median 18 (high ✓); 4 breaks; `scene-set` → `long-fade`;
- every gate clean; echoes / command echoes / spoken-line echoes none / none / none;
- **the first sentence, the mountain, the camera beat, "Seventy-nine.", the door description, the backs-of-fingers test, "it stayed a picture of a door.", the cassette touch and the closing paragraph are byte-identical.**

---

## Genesis Score (Craft Assessment)

| Dimension | Score | Evidence | Cap reasons / holds |
|---|---|---|---|
| Originality | 9.0 | **The outline's subversion is on the page.** The doomed-city arrival under ominous skies becomes spring: a town under props and election paint, a green mountain, and a woman who declines to take one photograph. "Fine mountain for vines," / "Very fine," (l.35–37). **What the writer built on top of it:** (1) the mountain found by elimination against "the outline painted on the wall over the ovens of every pizzeria on Passyunk Avenue, two humps … and the mountain had only the one" (l.29). The reader's own knowledge does the arithmetic and the page does none. (2) The painter's shadows under the door rings, "falling the opposite way from every real shadow on that road" (l.349). (3) The harbor clerk Valens is sure has marked him is simply short-sighted, with "a smudge of black on the tip of his nose" (l.73). (4) "Ours is that one. … He was my grandfather. He sold eels." (l.365). (5) The vines married to elms: "Twelve days into my own, I was in no position to laugh at anybody." (l.193). | **≥9.0:** would a senior editor set this beside *Outlander*'s arrival at Leoch? Yes. It is quieter and stranger, and the dread is all in the reader. **Not 9.5:** the arrival-travelogue spine is a genre standard; its execution, not its shape, is new. |
| Theme | 9.0 | "Home located, in a place that will not last" is carried by objects and acts and never stated: a room "with a door" (l.273) after a ship where "Nobody … had a door to shut on anybody" (l.11); a town "being mended" whose cousin-plasterer's join "showed to everybody" (l.211); "Ten years," … "They're slow." (l.179); "I have some," … "but not here." (l.379). **Texture that means nothing:** the cheese carters and the wife who can tell the hour from the cheese, the priest arguing about fried food, the geese, the fly on a sleeping man's cheek. | **≥9.0:** the theme is a question the reader answers. **Not 9.5:** "door" appears 24 times (2.8/1k). The motif is designed, but the density brushes the echo chamber (anti-AI #18, minor). |
| Characters | 8.5 | **Grata** arrives entirely as her card: a voice before a face; tells, never asks (0 personal questions); flood, then command; the arm-touch; the whitewash planted and unexplained; teeth 0. "You're Greek, you've the walk, and you've not been married long, you stand too near him for that. It wears off." (l.237). **Valens's chaos** (mind-reading) is inhabited and refuted by evidence he will not accept: "He'll know me again." (l.119). His hands find work (the hipposandal, the noseband), there is no comparison in his speech, and bare "No." is 0. **Mara** is 4/4, all inhabited (below). **Secondaries have their own moments:** Pacuvia (the brooch pinned "twice more to be sure"), the clerk, the carter, the rose woman, the boy. Cover-the-name PASS for all speakers. | **No cap:** no catchphrase, and the gate's gesture classes are clean (I use the gate's numbers). **Held at 8.5** by C1–C4: Grata's card example as a line; "considered" ×8 book-wide; "What for?" in a 4th mouth; the race frame "before [X] had" ×3 (l.107, l.191, l.247). **WATCH, not changed:** Felix ends 12 of his 15 speeches on a question (his card, but near a metronome: audit W-13), and Valens deflects him with an order twice. |
| **Prose & Voice** | **8.0** | **Stopping sentences:** "Seventy-nine. It came unasked, two figures with nothing round them, while the mountain stood small and green in the glass." (l.45) / "My finger left the button." (l.47); "and it stayed a picture of a door." (l.357). **Underlines:** "a fishing boat a mile off drew lines on it with its oars, and the lines held." (l.27); "From that close it was simply farmland, tipped up on end." (l.195); "That was the nearest we came, in eleven days, to being married in private." (l.15); "the cord at the rotten end let him down an inch." (l.249); "When my hand left it, the coolness stayed in my palm for some distance, and was gone by the gate." (l.375); "the song dropped down the ladder in pieces whenever his head came round." (l.209). **Ugly sentence:** "Felix slept wherever a sailor had last moved him on from" (l.11). **Voice under pressure:** at the finder the asides die (l.43–47: plain acts, one number); at the tomb the voice narrows to hands and temperature, then **fails into sleep** (l.381). | **Merit 8.0, no cap.** #11 is under the commercial cap: 4 firm (0.47/1k). The ugly sentence and the voice under pressure are both present. **Held by the law cluster** (R1–R15, L1–L2, D1–D6): three moving-thing measures; Ch.17's leaf skeleton and its Greek frame; the car and subway domains; "no business"; "so that" ×7; comprehension ×5; "and stayed"; the gaze-arrival; "the size of a" ×3; the rejoinders. Anti-AI 8/20, −1.0 (clean band, at its edge). |
| Pacing | 8.5 | **The ledger row is hit on every hard field:** Chronological, between Ch.18's Single-scene and Ch.20's Collage ✓; open `scene-set` ("By the twelfth morning of my marriage…", a CONTRAST hook, marriage against mule, not SENSORY after Ch.18) ✓; close `long-fade` (a 150-word held sentence of shutters knocking down the street) ✓; 4 breaks ✓; dialogue 24.1% (20–30) ✓; 8,436 against 8,400 ✓; median 18 (high) ✓; the crossing given its 11 days and not compressed ✓. **Speed design as the outline asks** ("slow, panoramic; quick at the harbor; very slow at the tomb"): the crossing runs in a paragraph of days; the bay decelerates; Puteoli is quick (clerk, board, wine); the road is panoramic; the tomb is very slow (about 900 words for one afternoon). **Value shift:** landed (+) → marked? (−) → the papers work (+) → housed (+) → the door found, real and shut (±). | **Not 9.0:** the chapter's forward question (the search) first surfaces at l.203, about 55% in. From the Puteoli awning to the Herculaneum road (about 2,400 words: tunnel, Neapolis, inn, coast road) the only pull is travel incident. It is good incident, but a Devourer skims it. |
| Emotion | 9.0 | **The anchor lands exactly as planned** ("the green, vine-covered mountain seen from the deck, one broad summit"): in the finder it is "small enough to cover with a thumb, very green", the finger rests on the button and leaves it. **The surprise lands:** she agrees with him, "Very fine," and "I was glad he had said it" (l.39). **Body rebel, a new channel:** "I meant to sit on the bed only while I got my sandals off. I woke with one of them off and the other on" (l.381). Hands and voice stay rested, as the bible requires. **Techniques ≥5:** object proxy (the camera not fired, the cassette's hub turned a quarter); dramatic irony ("Ten years," … "They're slow."; "row the admiral round this bay"); comedy at the threshold (the eel-seller's boy; "She's praying."); temperature as feeling (warm white, cool leaf, the coolness carried "for some distance"); sleep as collapse. | **≥9.0. Not 9.5:** the romance carries less than a romance reader wants in a long chapter (the ankle, the stuck door, Grata's "you stand too near him"). That is right for the beat, but it is a lighter heart-load than Ch.15–18. |
| **Immersion** (Dim 7) | 9.0 | **Period, nearly all verifiable:** Puteoli's mole on arches with statues on columns and concrete faced with brick; the Alexandrians' little topsail; the Misenum fleet; the Crypta Neapolitana's dust and torch boys; Greek Neapolis and its four-yearly games for the emperor; the Sebeto in its reeds; the Nucerian riot and the ten-year ban; the hipposandal; villa fishponds; vines married to elms; salt pans; Herculaneum on its spur unnamed; the Herculaneum Gate's three arches and its bench tombs with lion's feet; stepping stones; the muleteers' election notice; a thermopolium counter in marble offcuts; the sunk amphitheater; the Nuceria road under the wall, with columellae with a knot of hair for women and roses for the dead. **The authenticity dial:** sensory ~8+ (grain dust in the porters' hair; pitch in the wine; the pepper up the nose), harshness ~7. | **Held at 9.0:** Rhegium put after the Straits (L1); tour-guide edges in the stepping-stone gloss (l.207) and the counter (l.229). |
| **FLOOR** | **8.0** | Prose & Voice (merit) | |
| **AVERAGE** | **8.71** | (9.0 + 9.0 + 8.5 + 8.0 + 8.5 + 9.0 + 9.0) / 7 = 61.0 / 7 | |

**Trajectory against Ch.1–18** (finals 8.50–8.93; cycle 0s 7.5–8.0):
- This is the nineteenth cycle 0 below the gate, and again held by narrator moves the gates cannot see.
- **The new failure mode is the moving-thing measure, three times in one chapter,** after the bible had closed it at "0 more anywhere" (Ch.10). Ch.18's eval found the narrating-present simile; this one finds the passing-traffic hold. Both are reflexes of a held moment that the writer will not leave bare.
- The continuity repair added no gloss. Its recasts (W-01…W-14) are clean, and I re-scanned them.

---

## CVI-Launch Breakdown
| Input | Score | Evidence |
|---|---|---|
| Commercial Pacing | 8/10 | A long arrival chapter with a payoff (the door found) at about 80%. Quick harbor, quick Grata. It loses 2 for the road stretch with no forward question. |
| Tomorrow Test | 5+ anchors → 10 | IMAGE: Vesuvius small enough to cover with a thumb in the finder, and the finger coming off the button; the painted door cool in a warm white wall, its painted shadows falling the wrong way; a small boy with rose petals stuck to the soles of his feet; Mara asleep with one sandal on; a clerk with black wax on his nose. QUOTE: "Seventy-nine."; "Fine mountain for vines." / "Very fine."; "He was my grandfather. He sold eels." |
| Casual Reader | 8.5/10 | See the report below. |
| Shareability (quote / plot / emotional) | 3 / 4 / 4 → 6 / 8 / 8 → **7.73** | **Quote:** "Fine mountain for vines." **Plot:** "she finds the door home: a painted door on a tomb that's cool to the touch on a hot day." **Emotional:** "she sees Vesuvius green and covered in vineyards, puts the camera up, and can't take the picture." Calculation: MAX 8 × .6 + AVG 7.33 × .4. |
| Concept Pitch | yes → 10 | |
| Human Closeness | partial → 5 | A marriage in its first fortnight, a landlady, a boy. But much of the word count is place. |
| **CVI-Launch** | **8.35 + 0.5 = 8.85** | 8 × .2 + 10 × .2 + 8.5 × .2 + 7.73 × .2 + 10 × .1 + 5 × .1 = 8.35. |

**CVI-L note.** In this project "CVI-L" means **CVI-Launch: 8.85** (8.35 before the anchor bonus).
- Running CVI-L, Ch.12–19: 9.7 / 9.8 / 8.9 / 9.8 / 9.7 / 9.7 / 10.0 / **8.85**.
- **The dip is structural, not a defect.** After the book's most shareable chapter (a ten-word wedding), Part Two opens on a panoramic arrival whose engine is fascination. The reader's knowledge of the mountain does the work, and romance heat is low by design.
- What will drive launch here is **"Seventy-nine."** at the finder and **the door found**. Those are the two things a reader tells a friend.
- **None of the 27 fixes touches an anchor.** These lines are byte-identical after the fixes:
  - the opening sentence;
  - "Fine mountain for vines," / "Very fine,";
  - the camera beat, l.43–47 (only "Alone at the rail," becomes "Left to myself,");
  - "Seventy-nine.";
  - the tomb description (only the "size" clause changes);
  - the backs-of-fingers test (only the car simile and the "no business" clause go);
  - "it stayed a picture of a door.";
  - the boy and his eels;
  - the sleep;
  - the cassette;
  - the close.
- **CVI-L is unchanged after the PATH: 8.85.**

**CVI-Legacy (default weights; provisional):** **7.2**. It is the sum of:
- Originality 9.0 × .30;
- Theme 9.0 × .25;
- Cultural Vocabulary 2 × .20;
- Re-readability 9 × .15;
- Identity 5 × .10.

This is the book's richest re-read chapter so far. On a second pass the reader finds:
- the one-humped mountain against the pizzeria's two;
- "Ten years," … "They're slow.";
- "row the admiral round this bay";
- "There'll be men sleeping in those tombs.";
- "Is this one yours?" / "No,";
- the backs of her fingers on the door (foundation §4f's rehearsal of Ch.42).

None of them is pointed at.

---

## Anti-AI Scan (20 patterns; density per 1,000 words at 8.44k; commercial band)
| # | Pattern | Result | Count / density | Citation |
|---|---|---|---|---|
| 1 | Forced symmetry | FOUND minor | 2 (0.24) | the warm-as / cool-as pair at the door (l.353–355; → R5); the two search sentences ending on parallel door negations (l.203, l.297; kept). **−0.125** |
| 2 | Empty poetic vocabulary | Clear | 0 | |
| 3 | Automatic rule of three | Clear | — | Felix's stacks are his card's syntax. The narration lists run in fours and twos. |
| 4 | Em dashes | Clear | 0 | |
| 5 | Empty metaphors | Clear | 0 | "a long colonnade of green", "farmland, tipped up on end": both concrete. |
| 6 | Dramatic "And" openings | Clear | narration 0 | Speech has 6 rejoinder openers across 4 speakers → D4–D6. |
| 7 | Pseudo-philosophical closings | Clear | — | The chapter closes on shutters and a girl singing to a baby. "went on being green" is image, not maxim. |
| 8 | Excessive parallelism | FOUND minor | 3 (mostly speech) | Grata's "If you hear dice, that's him, and if you hear shouting after the dice, that's me" (character); "the same two lines … the same two lines" (the close, designed); the warm/cool test rhythm (designed). **−0.125** |
| 9 | Overly smooth transitions | Clear | — | Section joins vary (a place, a road, a gate, a dawn departure). "On the next afternoon it was the Nuceria Gate." is the one one-line hinge. |
| 10 | Described emotions | FOUND minor | 3 | "I was glad he had said it" (l.39; the outline's lie, kept); "He was outraged for them." (l.187); "with enormous pleasure" (l.151). **−0.125** |
| 11 | **Explanatory extension** | **FOUND minor** | **4 firm (0.47/1k)** | (1) l.355 "on that warm road … it had no business to be cool at all" (→ R6); (2) l.11 "Nobody aboard that ship had a door to shut on anybody." (a gloss, but it plants l.273: kept); (3) l.207 "spaced so that a cart's wheels would go between them and a person's feet over them" (kept: the mules use it); (4) l.73 "Every bale and beast landed on that mole went past that table." (kept). **Borderline, not counted:** "to make them shine" (l.349); "for a hollow behind it" (l.355). **−0.125.** Commercial cap (>0.8/1k): PASS. |
| 12 | Binary negation opener | Clear | 0 | Gate pivots 0. |
| 13 | Precision flex | FOUND minor | — | Twelfth morning, eleven nights, sixth morning, eighth night, "three stars … and part of a fourth", fifty paces, twenty-four sesterces, fifty-one years. The marriage clock and the inscription earn theirs; the stars are wit. **−0.125** |
| 14 | Emotional control demonstration | Clear (edge) | — | The camera beat is managed (finger off, camera fed back), but the chapter's control **fails** later (sleep), so it is not "always successfully". |
| 15 | Authoritative description | FOUND minor | — | The stepping stones' function (l.207); the counter (l.229). Offset by gaps and wrong guesses: "poured somehow under water", the wrong hills, "something fried in oil", "off some coast none of us could see". **−0.125** |
| 16 | Philosophical asides | FOUND minor | 1 | "A join showed or it did not." (l.211): a past-tense gnomic line. It is the all-or-nothing distortion, stated once. Ch.20 must not restate it. **−0.125** |
| 17 | Clean dialogue | Clear | — | The carter's interjection from under his cloak; Felix answering nobody; Grata's floods; "the echo of the passage took" the rose woman's tail; the mother calling across. |
| 18 | Thematic echo chamber | FOUND minor | "door" ×24 (2.8/1k) | The motif is designed, and texture abounds (cheese, geese, the fried-food quarrel). R8 removes the gratuitous door-shaped whitewash. **−0.125** |
| 19 | Graduated reveal | Clear | — | A chronological walk that fades out rather than escalating. |
| 20 | Emotional temperature report | Clear | — | No periodic body check-ins. The temperatures at the door are the plaster's. |

**8 / 20 found (#1, #8, #10, #11, #13, #15, #16, #18). Total −1.0. Band: clean (commercial 0–8), at its edge.**
- **#11 hard check:** commercial cap PASS (0.47/1k).
- **After the PATH:** #11 → 3 firm (0.36/1k); #1 stays minor (the search pair); **8/20, −1.0: clean band.**

---

## The book's own laws
- **NO FORESHADOWING: PASS** (gate 0; by reading, 0).
  - **The mountain:** green, vines, farms, woods, "broad and rounded and bare". Never named, never menacing, no banned descriptor, no personification. "where it had to stand" (l.31) is her map knowledge after the wrong hills. "went on being green" (l.47) is the outline's own "green and lovely, and that is the dread".
  - **"seventy-nine": 1** (l.45), as a present thought, in fresh words. Sample-13's "sitting in my head" was cut at W-09 and stays cut.
  - **The pizzeria's two humps** (l.29) is 1998 knowledge against the present sight. It is the outline's anchor ("nothing like the postcards"), and the inference belongs to the reader.
  - **Reader irony in mouths, not narration, all kept:**
    - "row the admiral round this bay till his beard comes in gray" (l.53);
    - "Ten years," … "They're slow." (l.179);
    - "There'll be men sleeping in those tombs." (l.259);
    - "Is this one yours?" / "No," (l.361–363).
  - **Forward guard (orchestrator):** Ch.41–44 never call any of these back.
- **Nothing reaches toward the ending (END-1): PASS on the reserved words, with one judged approach.**
  - "seam" 0, "niche" 0, "painted plaster" 0, "hand flat" 0.
  - **Judged:** "I spread my fingers and gave it the whole of my palm." (l.355) and "The plaster against my palm … it stayed a picture of a door." (l.357) build the same act as sample-07's Ch.42 ("Her palm lay flat against the plaster … the plaster was plaster"). **Kept.** Foundation §4f sanctions exactly this: "Ch.19, palm on the tomb's painted false door, faintly cool", as the rehearsal the re-read is meant to feel. The reserved strings are untouched.
  - **Forward guard:** Ch.42 renders the children's refusal without "picture of a door", "stayed a picture", "the whole of my palm" or a backs-of-fingers test. All are spent here.
- **"the disruptor's one clause at the door", "it had no business to be cool at all": CUT (R6).**
  - It explains the anomaly one sentence before the test shows it, so it is the chapter's clearest #11, and it sits at the anchor.
  - It also carries the paragraph's second "afternoon sun" and a closing "at all".
  - Without it, the cool is a fact the hand finds and the reader weighs. The disruptor offered the same cut at the semicolon if the evaluator flagged it.
- **Memory only when the scene triggers it: PASS.**
  - The pizzeria outline (triggered by the hunt for the mountain, a clause, no person in it).
  - The plaster panels "at home" (triggered by the knock, a clause).
  - The subway (triggered by the tunnel) goes in R7, for its domain and frame, not its trigger.
  - There is no stand-alone memory paragraph, and the shape is different from Ch.18's (the cucumber at a sink).
- **Explanation-density cap: PASS** (0.47/1k → 0.36/1k after R6).
- **Paragraph-final negations ≤1.5/1k: PASS.**
  - **5 in narration (0.59/1k):**
    - "Nobody aboard that ship had a door to shut on anybody." (l.11);
    - "no ship but ours yet in from Lechaion" (l.125);
    - "in no position to laugh at anybody" (l.193);
    - "with no love for it" (l.291);
    - "with not a letter of it read" (l.347).
  - Unchanged after the PATH.
- **Present-tense generalisation ≤1: PASS** (1: the allowlisted "This was where the dead go out", l.345).
  - There are no narrating-present similes; "close as houses in a street" has no verb.
- **No comparisons in Valens's speech: PASS.** Every Valens line was checked, among them:
  - "Fine mountain for vines,"; "They work." … "They're mine."; "It's a fig,";
  - "He knew me,"; "He walked round his table to look at my face."; "He did that to no other man on the mole.";
  - "A lady's brother."; "This town of yours." … "Where do the beasts drink?";
  - "Ten years," … "They're slow.";
  - "Up on the crown with them," … "The edges won't bear a loaded beast.";
  - "Thirty pairs," … "In a town this size."; "The muleteers have a man, then.";
  - "There'll be men sleeping in those tombs."; "It sticks at the sill,";
  - "They dug the bowl and banked the earth…" … "That saved them stone.";
  - "Out where the dead are. Eat your beans."
  - No "like" or "as", no idiom, no hyperbole.
- **No command echoes: PASS** (gate none). By hand, each order is answered by its result or by nothing:
  - "Go and ask." → "Felix took his foot off the rail.";
  - "Hold her." → no compliance narrated;
  - "Drink that before it cools." → "The wine was hot";
  - "Sit there. Eat that." → "I took the bench … and emptied it";
  - "Leave the lady be" / "Come here and carry this." → "The boy returned to his eels.";
  - "Eat your beans." → nothing.
- **No borrowed whole spoken lines: FAIL by hand, cleared by the PATH.**
  - `--echoes 19` reports none, because the tool's whole-line floor is above two words.
  - By hand: "What for?" is a whole line in its 3rd chapter (Ch.8 Nikaso ×2, Ch.9) and its 4th mouth → **C3**.
  - "Eat that." is Gloria's Ch.1 line and the GRATA card's rhythm example → **C1**.
- **No reuse of earlier chapters' phrases or set pieces: FAIL, cleared by the PATH.**
  - **The held moment measured by something moving (SPENT, "0 more anywhere", after Ch.10; with Ch.1's car, Ch.5's disc buyer and Ch.9's oil cart):**
    - l.351 the cart → **R1**;
    - l.373 the family and the shadows → **R2**;
    - l.93 the porters and the swell → **R3**.
  - **Ch.17's leaf scene:** read "to the end of the witnesses" / "He shut it." → l.93 "every line, the witnesses and all … Then he shut it" → **R3**.
  - **Ch.17's trainer:** "in a Greek that was not Corinth's" (logged "once") → l.69 → **R4**.
  - **Comparison domains:**
    - car (Ch.2, Ch.5, Ch.13) → l.353 → **R5**;
    - subway (Ch.3) plus the "It was the first [X] I had" frame (Ch.7 ×2) → l.149 → **R7**.
  - **CLOSED / SPENT moves:**
    - "and stayed" (CLOSED after Ch.15) at l.151 → **R14**;
    - the gaze-arrival "Then her eyes went…" (SPENT family) at l.65 → **R15**;
    - the comprehension report (a cousin of the SPENT "first Greek I understood") ×5 → **R13, R14** (2 explicit left: the half-caught mother-in-law and the baker).
  - **Sample-13 at the camera beat:** "Alone at the rail, I drew the Pentax" against the sample's "beside me at the rail. / I lowered the camera" → **D3**.
- **NO TICS: verbal catchphrases 0; gate gesture classes clean.** By hand:
  - **"considered" as a contemplation beat:** 8 book-wide (Ch.1, 6, 8, 9 ×2, 12, 18, 19), Ch.18 → Ch.19 running. Ch.13 cut three → **C2**.
  - **The race frame "[act] before [X] had":** ×3 in narration (l.107, l.191, l.247) → **C4** takes the competence one.
  - **"two-handed":** 3rd book-wide (Ch.11; Ch.15 heat, where "drawn off two-handed" is SPENT staging) → inside **R3**.
  - **"And…" rejoinders:** 6 across 4 speakers (WATCH ≤4, one owner) → **D4–D6**. The clerk keeps his two.
  - **said/told-the-[non-listener]:** 0 ✓ (Ch.19 "gets none").
  - **Kneel/crouch** 0; **hand-on-knee** 0; **bends** 0 ("leaned his forearms on the rail" is a lean, and the gate passes it); **gait exits** 0; **deliberation pauses** 0 after C2; **bare "No." from Valens** 0; **narrated non-answers** 0.
- **Ch.19 brief items: all honored.**
  - The scene-set time opener is CONTRAST, not SENSORY.
  - The crossing takes 11 days.
  - The Pentax has no cap, its dented ring is shown, and no frame is fired.
  - "all the way up the" 0 (CP3-4).
  - Pompeii is ten years on (the "ten years" count is down to 4 on the page after W-11).
  - Grata rents them rooms, with teeth 0.
  - The search is two sentences (the Herculaneum and Stabian roads), and there is no "Vesuvius Gate".
  - The Nuceria Gate tomb is cool and dormant.
  - The microcassette is touched without comment, staged a third way (the toe of the sock, a hub turned).
  - "where the dead go out" is allowlist use 2 of 3, unannounced.
  - "Fine mountain for vines" is said once.
  - "seventy-nine" appears once.
  - The watch and bracelet are not mentioned, so there is no conflict.
  - The leaf goes under the tunic.
  - The knife thread is honored: Mara watches the boats for Myrrhine.
  - **Citizenship: 0 lines** (CH18-5 stays open).
  - Weather on Mara's body in the opening paragraph: 0.
- **"seam" ruling (orchestrator, 2026-10-21): respected.** "seam" is 0, and nothing describes the door, tomb or cold with the four reserved words.

---

## Character Chaos Check (Primary: Mara)
- **Irrelevant thought: present, inhabited.** In a loft full of cheese carters on her first night in Italy, she plans the roof repair: "With a bit of lead and a hammer that tile would have been back in its course in the time it took to say so, and I lay working out how I would get up to it from the ladder." (l.165).
- **Cognitive distortion: present, inhabited.** All-or-nothing on a stranger's wall: "A join showed or it did not. … the plasterer should have been made to stand in front of it from dawn to dark" (l.211). Her thumbnail is in the stripe before she knows it, and Valens has to call her out of it.
- **Unprompted memory: present, triggered.** The pizzeria outline is triggered by the hunt for the mountain, and it returns to the bay in the next sentence.
- **Failed emotional management: present, inhabited.** The number arrives "unasked" (l.45). After the tomb she sleeps through supper in one sandal (l.381). Neither is narrated as feeling.
- **Voice under pressure: demonstrated (level 1).** The asides die at the finder and at the tomb, and return on the street.
- **Score:** 4/4 (commercial 2–3 is sufficient), all inhabited → no cap.

## Secondary Character Chaos
- **Valens:** his own moment — mind-reading the clerk; the fig on the roof before he looks at the bed; "Ten years. They're slow."
- **Grata:** her own moment — the whitewash, unexplained.
- **Felix:** his own moment — "Thirty pairs" read off an election notice he cannot read; outrage on behalf of Pompeii's banned games.
- **Pacuvia:** her own moment — the brooch pinned twice more; "Don't tell my father it was broken."
- **The clerk:** his own moment — the nose.
- **The carter:** his own moment — the wife who can tell the hour from the cheese.
- **The boy:** his own moment — the eels; the petals.
- **No secondary character is a function only.**

---

## The Tomorrow Test
**What the reader remembers:** Vesuvius in the camera's finder, green and small enough to cover with a thumb, and her finger coming off the button. Then the number. Second, a painted door on a little tomb that is cool under her fingers when the white wall beside it is warm, and a small boy with rose petals stuck to his soles asking "Is this one yours?"
**Anchor type:** BOTH. IMAGE: the finder, the cool door, the petals, one sandal. QUOTE: "Seventy-nine."; "Fine mountain for vines." / "Very fine."
**Verdict:** **ANCHOR EXISTS** (strong) → +0.5 CVI-L.
**Pattern check:** this anchor's engine is **an act withheld** (a photograph not taken). Ch.18's was a gift handed over without a word, and Ch.17's a bystander's appetite. The engines differ. The door is the book's foundation-sanctioned recurring situation (§4f).

## The Shareability Test
- **What a reader texts a friend:** "She finally sees Vesuvius from the ship, all green and vineyards, and her husband goes 'fine mountain for vines' and she says 'very fine' and puts the camera down. I KNOW WHAT YEAR IT IS, MARA."
- **Running count:** at least seven shareable chapters (Ch.6, 8, 12, 15, 17, 18, 19).

---

## Reader Reports

### The Devourer (8.4k after a 2.5k hinge)
- **The first page pulls:** married eleven nights "between my husband and a mule", the ankle held all night, the brooch.
- **Where they slow:** after Puteoli. The tunnel, Neapolis, the inn and the coast road run about 2,400 words with no live question. Valens's fear of the clerk was answered at the awning, and the search has not surfaced yet. They will skim the villas and salt pans.
- **What hooks them back:** the tombs read "as we climbed" (l.203) and "on none of them anything painted in the shape of a door". From there they go fast: Grata, the stuck door, the Stabian road, "The Nuceria Gate. Tomorrow." The tomb pays.
- **Where would they stop?** At the chapter's end, satisfied, with the door found. The long fade does not push them on, but the found door does.

### The Critic
- **Would underline:**
  - "Seventy-nine. It came unasked, two figures with nothing round them…";
  - "My finger left the button.";
  - "and it stayed a picture of a door.";
  - "a fishing boat a mile off drew lines on it with its oars, and the lines held.";
  - "From that close it was simply farmland, tipped up on end.";
  - the painted shadows "falling the opposite way from every real shadow on that road";
  - "Twelve days into my own, I was in no position to laugh at anybody.";
  - "the cord at the rotten end let him down an inch.";
  - "He's a bad plasterer and he's family, so it stays."
- **Would notice and mind:**
  - "it had no business to be cool at all", the narrator explaining the anchor (R6);
  - the hood of a parked car beside a glass of water by a sink: two modern similes in a mirror pair at the book's most important threshold so far (R5);
  - the cart going by "behind me", a held-moment device this reader has now seen four times (R1).

### The Hostile
- **"Rhegium is at the south end of the Straits. How is she well 'by Rhegium' after being sick 'for every mile of the Straits'?"** She can't be. → **L1** ("well again by daylight").
- **"He shut the door, barred it, unbarred it, and 'closed it once more'?"** It was never reopened. → **L2**.
- **"Eleven nights before 'the twelfth morning of my marriage'?"** Counted from the first morning after the wedding, the landing is the eleventh morning (audit I-04, optional "eleventh"). **INVESTIGATE, not changed:** the first sentence is the ledger signature, and "Twelve days" to Grata on day 13 is right as elapsed time.
- **"Valens can read. Why does he agree with Felix there were thirty pairs on that wall?"** He keeps his reading from Felix, as in Ch.11 ("How would I know what it says?"), and "The muleteers have a man, then" was said low, to Mara. Consistent; the page never explains it.
- **"How does Mara know Pompeii has seven or eight gates and which are worth walking?"** Ch.14's plan and Ch.15's telling give her the town from 1998. Consistent (audit W-04 fixed the arithmetic).
- **"A hood pinned at the shoulder?"** → **D2** ("at her throat").

### The Casual Reader (airport, 10 pages)
- **Would buy, and keep going.**
  - The first three pages are a honeymoon on a cargo deck with mules.
  - A girl's broken brooch is fixed with a penknife, and she pins it "twice more to be sure".
  - Then Vesuvius, which this reader knows and the narrator knows, and she cannot take the picture. That is the bookstore moment.
- **The mood dips in the middle** (the road and the villas) and comes back strongly with **Grata**, who is the most fun anyone has been since Felix arrived, and with **the door found**: cool under her fingers, while a kid with petals on his feet asks if it's hers.
- **No vibes problem.** **8.5** (not 9.0: the romance is a background warmth here, not a foreground pull, and the middle stretch reads as travel).

### The Devoted Reader (active: long saga)
- **Would adopt it.** This is the chapter the re-read thread is built on.
- **What they will find:**
  - the one hump against the pizzeria's two;
  - the Misenum fleet and "the admiral";
  - the boy's "Is this one yours?";
  - "There'll be men sleeping in those tombs";
  - the painted shadows falling the wrong way;
  - the backs of her fingers (not her palm) for the test, then her palm;
  - "Ten years. They're slow.";
  - the door that sticks and that she closes with her back.
- **What they will catch (and should not):**
  - the cart behind her, as in Ch.9 (R1);
  - the leaf read to the witnesses and shut, as in Ch.17 (R3);
  - "in a Greek that was…", as in Ch.17 (R4);
  - "What for?" again (C3).
- This reader drives CVI-Legacy, not launch.

---

## Cross-Reader Matrix
| Issue | Devourer | Critic | Hostile | Casual | Devoted | Severity |
|---|---|---|---|---|---|---|
| R1–R3 held moments measured by moving things (SPENT, 0 more) | | ✓ | | | ✓ | **SHOULD FIX → blocking** (SPENT device ×3) |
| R6 "no business to be cool at all" at the anchor | | ✓ | | | | INVESTIGATE → blocking (#11 at the anchor; the disruptor's left clause) |
| R5 car simile (4th domain use) + mirror pair | | ✓ | | | ✓ | SHOULD FIX |
| R3/R4 Ch.17 leaf skeleton and Greek frame | | | | | ✓ | INVESTIGATE → blocking (set-piece reuse) |
| L1 Rhegium after the Straits | | | ✓ | | | INVESTIGATE → fix (logic) |
| L2 door "closed once more" | | | ✓ | | | INVESTIGATE → fix (logic) |
| Road stretch with no forward question | ✓ | | | ✓ | | SHOULD FIX → **not changed** (structural; the ledger's panoramic walk; see PATH note) |
| R7 subway domain + "It was the first" frame | | ✓ | | | ✓ | SHOULD FIX |
| R10–R15 narrator moves at density ("so that" ×7, comprehension ×5, "and stayed", gaze-arrival) | | ✓ | | | | INVESTIGATE → blocking (CLOSED/SPENT) |
| C1–C4 Grata's card line, "considered", "What for?", race frame | | ✓ | | | ✓ | SHOULD FIX |
| R8/R9, D1–D6 in-chapter doubles, rulers, rejoinders, the sample-13 rail | | ✓ | | | | INVESTIGATE |
| "twelfth morning" / "eleven nights" | | | ✓ | | | INVESTIGATE (not changed) |

**No CRITICAL. No VIBES PROBLEM.** The blocking items are book law, not reader-facing, except the road stretch, which the Devourer and the Casual reader both feel and which is judged structural (below).

---

## Revision Recommendations (Ranked)
*Every replacement string below was put through the same reuse checks as writer prose:*
- *the 3–7-gram scan against Ch.1–18 and all 13 voice-bank samples, stop-word-bounded strings included;*
- *the in-chapter repeat scan;*
- *a grep of every at-risk frame;*
- *the real gates, with the whole set swapped in.*

*The first drafts of 26 replacements failed these checks and were changed before the set was tested. They are logged under "Replacement strings rejected".*

### Fix order: Logic (L1–L2) → Character (C1–C4) → Reuse and law (R1–R15) → In-chapter doubles (D1–D6)

| # | Location | Problem type | What happens now | Why it fails | Revision direction (exact swap) | Project rule? |
|---|---|---|---|---|---|---|
| L1 | l.13 | Logic | "was sick for every mile of the Straits and well again by Rhegium." | Rhegium is at the Straits' southern mouth, so the ship passes it first. ("once they were astern" was rejected: "astern" is l.27's. "by the next morning" was rejected: the echo gate caught "the next morning", Ch.11.) | → "…and well again by daylight." | No |
| L2 | l.265 | Logic | "set the bar in its brackets and lifted it clear, and closed it once more, slowly," | The door is closed twice and never opened. ("opened the door and swung it to" was rejected: "and swung it" ×2 earlier. "pulled it to" and "drew it to again, slowly" were rejected: Ch.15's heat block, "pulled him to me" and "drew it off me, slowly".) | → "…lifted it clear, opened it, and closed it once more, slowly," | No |
| C1 | l.387 | Character / Voice | "Sit there. Eat that." | The GRATA card's own rhythm example ("Eat this. Hold that.") as page text, and Gloria's Ch.1 spoken "Eat that,". | → "Sit there. I kept you a bowl." This is her telling, not asking, and l.389's "the bowl she gave me" pays it. | Yes: **card rhythm examples and sample lines are 0 on the page, by shape as well as by string.** |
| C2 | l.359 | Character (gesture) | "He considered my hand on the door." | The "considered" contemplation beat: 8th book-wide, running Ch.18 → Ch.19; Ch.13 cut three. ("took an interest in my" was rejected: sample-01. "much taken with my hand on the" was rejected: Ch.1's car-in-the-rain beat. "He watched my hand" was rejected: Ch.4's goat-boy.) | → **cut.** "Is this one yours?" shows the look. | Yes: **"considered" as a beat: WATCH, 0 in Ch.20.** |
| C3 | l.369 | Character (borrowed line) | "What for?" the boy said. | A whole short line in its 3rd chapter and 4th mouth (Ch.8 ×2, Ch.9). (The tag "the boy said" was then rejected by the echo gate: "to the boy said", Ch.5.) | → "Who to?" asked the boy. (A child's literalism about praying.) | Yes: **"What for?" CLOSED.** |
| C4 | l.191 | Character (competence) | "…through its rings before Felix had a hand on her halter;" | The race frame "[act] before [X] had" ×3 in narration (l.107, l.191, l.247); this is the competence-display one. | → "…through its rings;" | No |
| R1 | l.351 | Style (SPENT device) | "I stood in the road in front of it while a cart went by behind me with an axle that wanted grease." | A held moment measured by passing traffic: Ch.1's car, Ch.5's disc buyer, Ch.9's oil cart; "0 more anywhere". (Rejected: "A cart came up behind me" (Ch.9's "while a cart came in"); "I stepped out of the road" (Ch.3's last line, "I stepped out into October."); "stood aside" (Ch.12, Ch.16 ×2); "gave the cart the road" (Ch.17).) | → "Behind me an ungreased axle squealed, and I moved off the road for the cart." Mara acts, and the hold is gone. | Yes: **gate proposal, below.** |
| R2 | l.373 | Style (SPENT device) | "I did not move, nor did my hand, while the family finished their jug … The shadows of the tombs reached the road's far side. Whenever I touched…" | The held silence measured by people leaving and by shadows (the bible names "casts a shadow"). ("Before long" was rejected: Ch.3, Ch.13.) | → "The family soon had their baskets and their cloths together and went past me in at the gate, the boy last, walking on the outsides of his feet to keep the petals on. Whenever I tried the white plaster…" The petals stay. The hold stays implied by "still giving back the sun's warmth". | (as R1) |
| R3 | l.93 | Style (set-piece reuse; SPENT device) | "The clerk took it up two-handed, raised it to his nose, and read it there, slowly, every line, the witnesses and all, while the porters went by behind us with their sacks and the swell slapped under the mole. Then he shut it and left it lying," | Ch.17's leaf scene ("to the end of the witnesses." / "He shut it."); a reading timed by passing porters; "two-handed" 3rd (Ch.15's SPENT heat staging). (Rejected: "down to the last name on it" ("name on it" 5th); "to the foot of the second board" ("to the foot of" 4th); "The clerk raised" (Ch.17's napkin).) | → "The clerk lifted it to his nose and read it there, slowly, one board and then the other. He left it lying open," | Yes: **a chapter re-using an object from two chapters back greps that chapter's handling of it.** |
| R4 | l.69 | Style (frame reuse) | "the girl told her, in a Greek that was suddenly as good as anybody's." | Ch.17's trainer, "in a Greek that was not Corinth's" (logged "once"). ("in a Greek suddenly…" was rejected as the 3rd "in a Greek".) | → "the girl told her, and her Greek was suddenly as good as anybody's." | No |
| R5 | l.353 | Style (domain reuse; #1) | "It was warm, as warm as the hood of a parked car on a June afternoon, with the whole day's sun in it." | The 4th car comparison (Ch.2, Ch.5, Ch.13), and with l.355 a mirror pair (warm as / cool as) at the anchor. ("warm through" was rejected: Ch.1.) | → "It was warm, with the whole day's sun in it." The one modern simile left at the door is the glass by the sink. | Yes: **car comparison domain CLOSED.** |
| R6 | l.355 | Style (#11) | "…by a kitchen sink; on that warm road, with the afternoon sun square on it, it had no business to be cool at all." | It explains the anomaly the test then shows, and sits at the anchor. | → "…by a kitchen sink." | No |
| R7 | l.149 | Style (domain + frame) | "It was the first tunnel I had been in since the Broad Street subway, and it was worse. The dust lay" | Subway is a used domain (Ch.3, the City Hall stairs); "It was the first [X] I had [V]" is 3rd (Ch.7 ×2). | → "The dust lay" (the torch boys in front place us in the tunnel). | Yes: **"It was the first [X] I had [V]": CLOSED.** |
| R8 | l.287 | Style (ruler ×3; door rhyme) | "there was a patch of new whitewash the size of a door." | "the size of a" ×3 in the chapter (5 book-wide); a door-shaped patch beside the door beat. ("a long patch" was rejected: "there was a long", Ch.1. "a patch of" was rejected: Ch.15 ×2.) | → "there was a broad patch of new whitewash." | No |
| R9 | l.349 | Style (ruler) | "a door had been painted, at the size of a real one as near as the little house allowed," | (as R8) | → "a door had been painted, as near full size as the little house allowed," | No |
| R10 | l.61 | Style ("so that" ×7) | "the lowest courses so that the gray core showed through, packed full of pebbles," | Narration "so that" WATCH >4 (after Ch.15). | → "the lowest courses and bared the gray core, packed full of pebbles," | No |
| R11 | l.209 | Style | "wedged against the curb, so that the mules had to be led round them" | (as R10) | → "wedged against the curb, and the mules had to be led round them" | No |
| R12 | l.345 | Style | "east and west, so that the town rose above it to the north and the fields dropped away southward," | (as R10). **"so that": 7 → 4.** | → "east and west, with the town above it to the north and the fields dropping away southward," | No |
| R13 | l.63 | Style (comprehension device) | "arguing with him about it in a Greek I understood and then in a language I did not." | One of five comprehension reports (a cousin of the SPENT "first Greek I understood"). ("first in Greek and" was rejected: "in Greek and" 4th.) | → "arguing with him about it, in Greek at first and then louder." | Yes: **comprehension reports ≤2 per chapter.** |
| R14 | l.151 | Style (comprehension; CLOSED) | "and I understood every word, and stayed in the street for the rest of it." | A comprehension claim, and **"and stayed", CLOSED for the book after Ch.15.** (Rejected: "and I stayed" (Ch.13, Ch.17); "the mules stood in the" (Ch.6); "and I waited" (Ch.5, Ch.15); "stopped the mules" (Ch.6); "hung back" (Ch.12).) | → "and I stood under her balcony for the rest of it." She follows it, and the act shows it. | No (already a rule) |
| R15 | l.65 | Style (SPENT gaze marker) | "Then her eyes went past the girl to us, and the question she put came slowly enough…" | The gaze-arrival "then" family (SPENT: Ch.1, 5, 6, 7 "her eyes came round to me"). | → "The question she put next was about us, and it came slowly enough for me to have all of it." | No (already a rule) |
| D1 | l.245 | Style (double) | "The floor was beaten earth with scraps of leather trodden into it," | "of leather trodden into" ×2 (l.275). | → "The floor was beaten earth," (l.275 keeps the leather). | No |
| D2 | l.65 | Style (double; logic) | "Pacuvia went down our plank first, in her good blue with the brooch at her shoulder," | "her good blue" ×2 (l.17); the brooch pinned her hood (l.23). ("in the blue" was rejected: Ch.18's blue-hood label.) | → "Pacuvia went down our plank first, with the brooch at her throat," | No |
| D3 | l.43 | Style (sample-13 at its own beat) | "Alone at the rail, I drew the Pentax up" | sample-13: "beside me at the rail. / I lowered the camera", at the same camera beat. | → "Left to myself, I drew the Pentax up" | No |
| D4 | l.329 | Style (rejoinders) | "And the third?" | "And…" speech rejoinders ×6 across 4 speakers (WATCH ≤4, one owner). ("Which is the third?" was rejected: Kallia's Ch.10 "Which is his name?" shape, and a second Valens "Which" in the chapter.) | → "The third?" (terse: Valens) | No |
| D5 | l.171 | Style (rejoinders) | "And carting? Who wants it?" | (as D4) | → "Carting? Who wants it?" | No |
| D6 | l.67 | Style (rejoinders) | "And those on your father's deck, who are they?" | (as D4). **Rejoinders: 6 → 3, the clerk owns two.** | → "Those on your father's deck, who are they?" | No |

**Not changed (judged; INVESTIGATE only):**
- **"By the twelfth morning of my marriage … all eleven nights before it"** (l.11). It is off by one if mornings are counted after the wedding (audit I-04's optional "eleventh"). It is the ledger signature and the hook's CONTRAST, so the author's call.
- **The palm on the door and "it stayed a picture of a door."** Foundation §4f sanctions it, and the reserved strings are 0. A forward guard is logged for Ch.42.
- **"Paint and white lay on a single coat of plaster"** (l.355). It is forensic, and the reserved string is clear (audit I-08).
- **"Out where the dead are. Eat your beans."** (l.339). Valens deflects Felix by paraphrasing the god's words, a page before the narrator's allowlisted use. The Devoted reader will love it. It is a WATCH as a section capper.
- **Valens's two orders to Felix** ("Hold her.", "Eat your beans."): WATCH, ≤1 in Ch.20.
- **Felix's question endings, 12 of 15 speeches** (audit W-13): his card. WATCH; Ch.20 gives him two speeches that end on a boast or a fact.
- **"spaced so that a cart's wheels would go between them…"** (l.207): #11/#15 edge. It is kept because the mules suffer the stones in the next sentence.
- **"A join showed or it did not."** (l.211): the distortion, stated once. Ch.20 must not restate it.
- **"door" ×22 after the PATH**: the designed motif. WATCH in Ch.20.
- **"Nobody aboard that ship had a door to shut on anybody."** (l.11): it plants l.273's "a room with a door".
- **"at the rail"** (l.65): the plank scene, not the camera beat. Kept.

**Replacement strings rejected during testing** (so the editor does not reach for them):
- "A cart came up behind me" (Ch.9); "I stepped out of the road" (Ch.3's closing line); "stood aside" (Ch.12, Ch.16 ×2); "gave the cart the road" (Ch.17);
- "Before long" (Ch.3, Ch.13);
- "down to the last name on it"; "to the foot of the second board"; "The clerk raised it";
- "in a Greek suddenly…"; "first in Greek and";
- "warm through" (Ch.1);
- "took an interest in my" (sample-01); "much taken with my hand on the" (Ch.1); "He watched my hand" (Ch.4);
- "\"Who to?\" the boy said" (echo gate, Ch.5);
- "once they were astern" (l.27 double); "by the next morning" (echo gate, Ch.11); "opened out" (Ch.3 ×2);
- "opened the door and swung it to"; "pulled it to"; "drew it to again, slowly"; "by inches" (Ch.15 heat frames, Ch.9/12);
- "there was a long patch" (Ch.1); "a patch of new whitewash" (Ch.15 ×2); "had gone on" (Ch.13 ×2);
- "and I stayed" (Ch.13, Ch.17); "the mules stood in the" (Ch.6); "and I waited" (Ch.5, Ch.15); "stopped the mules" (Ch.6); "hung back" (Ch.12);
- "Which is the third?" (Ch.10 Kallia's shape); "in the blue" (Ch.18).

### The fix script and the tested result
- **Script:** `/tmp/claude-0/-home-user/63791ee5-159c-5791-9429-07920f8d9417/scratchpad/ch19-fixes.py` (`python3 ch19-fixes.py <in.md> <out.md>`). It holds 27 swaps, and each OLD string must occur exactly once or the script aborts. Header comments are untouched.
- **Tested output:** `/tmp/claude-0/-home-user/63791ee5-159c-5791-9429-07920f8d9417/scratchpad/ch19-fixed.md` (md5 `db9b0e7b…`, sha256 `9af5c485…`).
- **Results with the copy swapped into the manuscript path, run from /home/user/Books:**
  - `check_chapter.sh 19`: **all clean.**
    - style: 8,300 words, simile 1.1/1k, em-dash 0, foreshadow 0;
    - grammar 0; rhythm 0;
    - show/tell 8,301 words, dialogue **24.6%**, no flags;
    - voice-wear strict clean;
    - tic gate clean (and-chains 6/9, credential 0, pivots 0, "So" 0; gesture classes clean);
    - echo **0**; command echoes none; spoken-line echoes none;
    - metaphor 1.6 fig/1k, median 18;
    - shape CLEAN.
  - `tic_report.py --gate`: clean.
  - `--echoes 19`: none / none / none.
  - `shape_check --strict`: `19 8279 4 25 18 scene-set long-fade`, CLEAN. The book stands at 107,490 words.
- **Restored:** the manuscript checksum was verified after every run (sha256 `7bea5358…`, md5 `b0500c45…`).
- **Post-fix numbers:**
  - **8,279 words** (shape_check), 8,300 (style), 8,301 (show_tell). That is −157 in total, 379 above the 7,900 floor, against an 8,400 target.
  - **dialogue 24.6%** (band 20–30, floor 20 ✓); median 18 (high ✓); 4 breaks; `scene-set` → `long-fade`.
  - **#11:** 3 firm (0.36/1k) ✓. **Paragraph-final negations:** 5 (0.60/1k) ✓. **Present-tense generalisations:** 1 (allowlisted) ✓.
  - **"so that" (narration):** 4. **Comprehension reports:** 2 explicit. **"the size of a":** 1. **Car similes:** 0. **"considered":** 0. **"What for?":** 0. **"two-handed":** 0. **"And…" rejoinders:** 3.
  - **Moving-thing holds:** 0. **"as if":** 1. **Em-dash:** 0.
  - **Anti-AI:** 8/20, −1.0 (clean band).

---

## Strengths to PRESERVE (do not touch in polish)
- **The opening:** "between my husband and a mule"; "I slept along Valens"; "Felix slept wherever a sailor had last moved him on from"; the ankle held till morning and "the nearest we came, in eleven days, to being married in private."
- **The brooch:** the coil closed with Plautia's knife; "pinned it again twice more to be sure"; "Don't tell my father it was broken". Paid on the quay by "she read the brooch before she read the face."
- **The bay and the mountain:**
  - the lines the oars draw that hold;
  - the wrong hills;
  - the pizzeria's two humps;
  - "Fine mountain for vines," / "Very fine,";
  - **the whole camera beat** (l.43–47) and "Seventy-nine.";
  - "went on being green".
- **The clerk's nose,** Mara's evidence against Valens's dread ("He has black wax on the end of his nose from doing it."), and Felix's pig at a candle.
- **The tile through the slot** ("three stars showed, and part of a fourth") and the carter's cheese.
- **"The Romans called that marrying the vine to the elm. Twelve days into my own, I was in no position to laugh at anybody."**
- **Grata**, entire.
- **The stuck door** and "I put my back against it and pushed".
- **The tomb:** the painted shadows; "I knew it from twenty paces off, with not a letter of it read."; the backs-of-fingers to-and-fro; the knuckle; "it stayed a picture of a door."
- **The boy:** "Is this one yours?" / "He was my grandfather. He sold eels." / "She's praying."; the petals.
- **"I have some," … "but not here."**
- **The sleep in one sandal, the cassette hub, and the closing sentence.**

---

## PATH TO 8.5 (mandatory; the Floor is 8.0)
- **Prose & Voice 8.0 → 8.5 requires the reuse and law cluster gone, with no new repeat moved sideways.**
  - The sentences already carry the stopping power ("Seventy-nine." / "My finger left the button."; "it stayed a picture of a door."). What is missing is a page that reaches for nothing the book has spent, and a door beat that trusts the hand.
  - **Surgery, in this order:**
    1. **Logic:** **L1** (l.13, Rhegium) and **L2** (l.265, the door).
    2. **The three moving-thing holds:** **R1** (l.351, the cart), **R2** (l.373, the family and the shadows), **R3** (l.93, the porters; this also clears the Ch.17 leaf skeleton and "two-handed").
    3. **The door paragraph:** **R5** (the car) and **R6** (the "no business" clause). Leave the glass of water, the test, the knock, the palm and "it stayed a picture of a door" exactly as they are.
    4. **Frame and domain reuse:** **R4** (l.69), **R7** (l.149).
    5. **Narrator moves at density:** **R10–R12** ("so that"), **R13–R14** (comprehension; R14 also takes the CLOSED "and stayed"), **R15** (the gaze-arrival).
    6. **Rulers and doubles:** **R8, R9, D1–D3**.
  - **Expected:** Prose 8.5. The underline set is untouched, #11 drops to 3 firm, and every gate stays clean (tested).
- **Characters 8.5 holds; C1–C4 keep it there and are part of the set:** Grata's line, "considered", "What for?", the race frame. **D4–D6** take the rejoinders to one owner.
- **Run all 27 swaps together** (the script). They were tested as one set; applying a subset leaves interim echoes (for example, R14's first drafts collided with three chapters).
- **Pacing 8.5 is not floor-holding.** The road-stretch sag (the Devourer and the Casual reader) is **not** fixed by surgery. The ledger's panoramic walk wants that stretch, and cutting it would hollow the arrival. If a later polish wants 9.0, the lever is **one clause of the search planted earlier**, for example at the inn, where Mara lies working out the tile. It would be a present thought, with no pointer at the god's words. It is not in this set because it adds text that has not been tested against the bible.

---

## Pacing check (one line for `feedback/progress.md`)
**Ch.19 (cycle 0):** Chronological walk (harbor → the road through the hill → a night near Neapolis → the coast road → Pompeii → three tomb roads over four days). It sits between Ch.18's Single-scene and Ch.20's Collage ✓.
- **Length:** 8,436 words (target 8,400; range 7,900–8,900; not padded). 8,279 after the PATH, still inside.
- **Dialogue** 24.1% (20–30 ✓; 24.6% after); **4 breaks** ✓; **gear median 18** (high ✓).
- **Signatures:** `scene-set` → `long-fade`. Ch.17 is `short-punch` → `quiet` and Ch.18 `I-statement` → `punch`, so nothing runs three in a row. The hook is CONTRAST (not SENSORY after Ch.18), and the pull is a fade (not DECISION POINT).
- **Neighbours:**

  | Ch | Words | Gear (median) | Dialogue | Approach | Breaks | Open → close |
  |---|---|---|---|---|---|---|
  | 17 | 6,910 | low (12) | 33% | In medias res | 3 | short-punch → quiet |
  | 18 | 2,523 | mid (15) | 34% | Single-scene | 0 | I-statement → punch |
  | **19** | **8,436 → 8,279** | **high (18)** | **24%** | **Chronological** | **4** | **scene-set → long-fade** |
  | 20 | 8,200 planned | mid | 30–40% | Collage | 6 | narrative → dialogue |

- **A long, panoramic, high-gear arrival after the short hinge, as designed.** 6.9k → 2.5k → 8.4k. The gear steps low → mid → high, and the dialogue drops to the chapter's 20–30 band for the first time since Ch.7. The variance is the design.
- **Emotional slot ✓:** after the public romance turn (Ch.18), the deadline-place, met in spring with the dread entirely in the reader. Then the door found and dormant: hope with a date on it.
- **Value shift ✓:** landed (+) → marked? (−) → the papers work (+) → housed (+) → the door found, real and shut (±).
- **Speed ✓:** quick at the harbor; panoramic on the road; very slow at the tomb (about 900 words for one afternoon).
- **Sag (accepted):** about 2,400 words between the awning and the Herculaneum road with no live question. It is full of incident, and it is the walk the ledger asked for.
- **Book:** 107,647 words against 115,000 cumulative target (−6.4%); 107,490 after the PATH. Projected at about 240k against the 220k floor ✓ and the 245k target (slightly under: watch it, never pad).

**Verdict: OK.**

---

## Cross-Book Pattern Detection (Ch.1–19)
1. **The held moment that will not be left bare.**
   - Ch.18's narrating-present similes and Ch.19's three moving-thing holds are the same reflex: when a moment is held, the writer puts something into it to measure or decorate it.
   - The bible closed the moving-thing measure at "0 more anywhere" after Ch.10, and it came back three times.
   - **Gate proposal (UPDATE RULE, root `tools/tic_report.py` and the template):** a narration-only HOLD-MEASURE layer. Flag `\b(while|as)\b[^.]{0,80}\b(went|came|passed|rolled|reached|moved) (by|past|behind|across)\b` and `\bshadows? of\b[^.]{0,40}\breached\b` within two sentences of a stillness verb (stood, did not move, stayed, held). Cap 0.
2. **Set pieces two chapters back.**
   - Ch.18's eval asked that anchors be guarded two chapters back. This chapter rebuilt Ch.17's leaf scene on the same object.
   - **Rule:** a chapter that brings back an object (the leaf, the knife, the watch) greps the last chapter that handled it, for the handling skeleton as well as the strings.
3. **Comparison domains are tracked by string, not by domain.**
   - The car came back for a 4th time because "parked a car", "car alarm" and "roof of a car" never shared a string.
   - **Proposal:** a domain registry in the bible (car, subway, kitchen sink, road, blind, diving board…), checked by the evaluator, with each domain once per book unless the author rules otherwise.
4. **A narrator move migrates into new coats** (the bible's own lesson). Ch.19 shows it twice:
   - the comprehension report: "the first Greek I understood" was SPENT, and it became five varieties of caught, lost and understood;
   - the gaze-arrival "then": SPENT as "looked at me then", and it came back as "Then her eyes went past…".
5. **What varies, as it should:**
   - the structure (Chronological after Single-scene);
   - the opening (`scene-set`, CONTRAST) and ending (`long-fade`, sound);
   - the gear (high);
   - the anchor's engine (an act withheld);
   - the body rebel (sleep, a new channel);
   - the length (the book's longest chapter so far).

**Bookkeeping (orchestrator):**
- **Re-sync the bible's Ch.19 blocks to the final page.** They quote the writer's draft, and dialogue-polish, the disruptor, the continuity repair and (after the PATH) these swaps have all moved on since. Examples:
  - **At-risk after Ch.19:**
    - "It came unasked and sat in my head" → page: "It came unasked, two figures with nothing round them";
    - "I agreed with all of it" → "I agreed with him";
    - the frost/ownership exchange ("It lies right to the sun." / "Whose is it?" / "That's the way to own a mountain.") → cut, and never on the page;
    - "Eight, in all. Only two have tombs worth the walk." / "And the other?" → "Seven or eight. Three have tombs worth the walk." / (after the PATH) "The third?";
    - "Anybody in the street could see exactly where that house had split." → cut;
    - "as the god had put it in Valens's mouth" → cut;
    - "He looked hard." → cut;
    - "It's cheaper," … "You dig, and the earth makes the seats." → "They dug the bowl and banked the earth…" / "That saved them stone.";
    - "Is that the emperor's?" → "What ship's that, the emperor's?";
    - the lime pit and the soldered pipe → cut;
    - the subway comparison, the parked car, "no business", the cart, the shadows → cut (after the PATH);
    - "deliberation pause 1 ('He lay quiet a while')" → cut.
  - **GRATA:**
    - "I saw you at that wall" → "I heard about you at that wall";
    - "ten years we've been at it" → "it's been carts and dust since the earth went";
    - "a patch of new whitewash the size of a door" → (after the PATH) "a broad patch of new whitewash";
    - "Sit there. Eat that." → (after the PATH) "Sit there. I kept you a bowl.";
    - "touched him on the arm too" → "touched him on the arm".
  - **Ch.19 walk-ons:**
    - "Whose freedman?" → "Freedman of whom?";
    - the clerk reads the leaf "two-handed" → (after the PATH) "lifted it to his nose … one board and then the other";
    - "the man raking water into the lime pit" → cut;
    - "What for?" → (after the PATH) "Who to?";
    - the mother-in-law's line → (after the PATH) "Those on your father's deck, who are they?";
    - Pacuvia "in her good blue with the brooch at her shoulder" on the quay → (after the PATH) "with the brooch at her throat".
- **At-risk after Ch.19, add (after the PATH):**
  - **held moments measured by anything moving (traffic, people leaving, shadows):** 0, restated, with the gate proposed (#1 above);
  - **car comparison domain:** CLOSED (Ch.2, Ch.5, Ch.13);
  - **subway comparison domain:** used (Ch.3);
  - **"It was the first [X] I had [V]":** CLOSED (Ch.7 ×2);
  - **comprehension reports:** ≤2 per chapter, never "understood every word";
  - **gaze-arrival "Then [poss] eyes went/came…":** restated SPENT;
  - **"considered" as a beat:** WATCH, 7 book-wide after the PATH, 0 in Ch.20;
  - **"What for?":** CLOSED;
  - **"two-handed":** CLOSED at 2 (Ch.11, Ch.15);
  - **narration "so that":** WATCH >4, restated;
  - **"the size of a" as a ruler:** ≤1 per chapter;
  - **"And…" rejoinders:** ≤4, one owner, restated;
  - **card rhythm examples** ("Eat this. Hold that.") and Ch.1's "Eat that,": 0;
  - **Valens's orders to Felix as deflection:** WATCH (2 in Ch.19), ≤1 in Ch.20;
  - **"Out where the dead are"** in Valens's mouth: once;
  - **the backs-of-fingers temperature test, the knuckle tap, "the whole of my palm", "it stayed a picture of a door":** SPENT. **Ch.30, 36 and 41–42 stage the threshold another way** (foundation §4f), and Ch.42's children's refusal is never "a picture";
  - **the warm-as / cool-as pairing at a threshold:** SPENT (audit I-15).
- **Entity and handoff cascades:**
  - The door is found and only Mara knows (Grata knows "out among the dead"; the eel family thought she was praying).
  - The shutter boards are not up; the bed cord is rotted at one leg; the bar leans by the inner door.
  - The fig is on the roof.
  - The Puteoli letter board holds the brother's letter for "Valens the muleteer" (Ch.21–22).
  - The knife is still in Mara's belt (Myrrhine's thread is open, with no return route on the page).

---

## VERDICT
**POLISH. Gate NOT MET at cycle 0. PASS expected after the tested PATH.**

| Measure | Result |
|---|---|
| Genesis Floor | **8.0** (Prose & Voice, merit; no cap) |
| Average | **8.71** |
| Casual | **8.5** |
| Scores | Originality 9.0 · Theme 9.0 · Characters 8.5 · **Prose 8.0** · Pacing 8.5 · Emotion 9.0 · Immersion 9.0 |
| Pacing | **OK** |
| CVI-Launch (CVI-L) / CVI-Legacy | **8.85** (8.35 + 0.5) / 7.2 (provisional) |
| Mechanical suite | all clean (echo 0, spoken-line echoes none, command echoes none, tic gate clean, voice-wear strict clean, shape CLEAN) |
| Foreshadowing / END-1 reserved words | 0 / 0 ("seam", "niche", "painted plaster", "hand flat") |
| AUTHOR-CP3-3 / CP3-4 / END-1 / citizenship open | ✓ / ✓ / ✓ / ✓ (0 lines) |
| Non-negotiables (the bay with the camera raised and lowered; Pompeii in repair; Grata; the Nuceria Gate tomb door cool and dormant; the microcassette touch) | ✓ all |
| "seventy-nine" once / mountain never menacing | ✓ / ✓ |
| Memory triggered by the scene | ✓ |
| Explanation density | ✓ 0.47/1k → 0.36/1k; the disruptor's door clause **cut** |
| Paragraph-final negations | ✓ 0.59/1k (≤1.5) |
| Present-tense generalisation | ✓ 1 (allowlisted) |
| No comparison in Valens's speech | ✓ |
| Command echoes / borrowed whole lines | 0 / **2 by hand** ("What for?", "Eat that") → 0 |
| Tics | catchphrases 0; gate classes clean; **"considered" (8th), race frame ×3, rejoinders ×6** → fixed |
| Reuse (moving-thing holds ×3; Ch.17 ×2; car and subway domains; CLOSED "and stayed"; SPENT gaze-arrival; sample-13 rail) | **FAIL** → cleared |
| AI patterns | 8/20, −1.0 → 8/20, −1.0 (clean) |

**After the PATH (27 swaps, tested together):**
- **8,279 words**; dialogue **24.6%**; median 18; 4 breaks; `scene-set` → `long-fade`;
- every gate clean; anchors byte-identical;
- **Prose 8.5 → Floor 8.5 / Average 8.79 / Casual 8.5 / pacing OK.**
- The orchestrator applies the script and runs the confirmation re-evaluation.

**BIAS CHECK:** This evaluation was produced by the same system that wrote the prose. Confidence in scores above 8.0 requires external validation (beta readers, editors, comp analysis). In particular, the Casual 8.5 and the Pacing 8.5 for a long panoramic arrival are the scores most likely to differ for a human reader. An *Outlander* reader may rate the road stretch higher than I do, and a romance-first reader lower.

---

# Re-evaluation after cycle 1
**Evaluator:** book-evaluator (independent; did not write or revise this prose) | **Date:** 2026-10-21
**Page evaluated:** `manuscript/chapters/chapter-19.md`, md5 `db9b0e7b…`, sha256 `9af5c485…`. This is byte-identical to the tested `ch19-fixed.md`. A word-level diff against the cycle-0 page (md5 `b0500c45…`) shows all 27 swaps, and nothing else changed.

**Read against:**
- the book's CLAUDE.md;
- STATE.yaml `guardrails` and `resolved_author_decisions`, including **AUTHOR-END-1**, CP3-3, CP3-4 and CP3-5;
- `feedback/progress.md`, including the Ch.19 brief and the **"seam" ruling**;
- voice-dna §0–§8;
- the character-bible:
  - every at-risk and spent block through "after Ch.19";
  - the GRATA, PACUVIUS, MARA, VALENS and FELIX Ch.19 blocks;
  - the Ch.19 walk-ons;
  - the planned-roles table;
- outline `## Chapter 19` and Ledger row 19;
- the cycle-0 evaluation above.

**Measured on the cycle-1 page** (run from /home/user/Books):
- `check_chapter.sh 19` is **all clean**:
  - style: 8,300 words, simile 1.1/1k, em-dash 0, foreshadow 0;
  - grammar 0; rhythm 0;
  - show/tell: dialogue 24.6%, no flags;
  - voice-wear strict: clean;
  - tic gate: clean (and-chains 6/9, every gesture class under cap);
  - echo 0; metaphor 1.6 fig/1k, median 18;
  - shape CLEAN.
- `tic_report.py --echoes 19`: **none / none / none**.
- `shape_check --strict`: `19 8279 4 25 18 scene-set long-fade`, CLEAN.

## Did the 27 swaps introduce anything new?
**Method:**
- Every 3–7-gram touching a changed word was checked against Ch.1–18, all 13 voice-bank samples and the rest of Ch.19. Stop-word-bounded strings were included.
- An anaphora scan covered the whole chapter.
- I read every swap in its paragraph.
- I grepped the law items.

**Clean on the asked-for checks, with five exceptions:**

| Check | Result |
|---|---|
| Added explanation | **None added.** R6 and R5 removed the door's gloss. R15's rewrite **kept** the old explanation clause ("and it came slowly enough for me to have all of it"), and with it a 3rd comprehension report. The cycle-0 eval counted 2 after the PATH; the page holds 3. → **F3** |
| A repeat moved sideways | **Two were created:**<br>• **D3** "Left to myself" put "left" ×4 into ~150 words around the stopping sentence "My finger left the button." (l.41 "he left me", l.43 "Left to myself" and "on the left", l.47). → **F1**<br>• **R13** "in Greek at first and then louder" (l.63) rebuilt l.13's "in a whisper at first and then aloud" fifty lines earlier, louder for aloud. → **F2**<br>**Two were adjacent:**<br>• **R8**'s "broad" is the chapter's 4th, and Grata herself is "broad" at l.229. → **F4**<br>• **R2** rewrote l.373 and kept "the door stayed cool". That leaves "stayed" ×3 in ~150 words, and the other two are protected lines ("it stayed a picture of a door."; "the coolness stayed in my palm"). → **F5** |
| Echo of an earlier chapter, including whole spoken lines | **None.** The gate shows none / none / none. By hand: "Who to?", "I kept you a bowl.", "Freedman of whom?" and "The third?" occur nowhere in Ch.1–18 or the samples. The remaining 3-gram hits ("it was warm", "I put the", "all of it") are grammar. Ch.6's "It was warm." is the watch, not a threshold. |
| New triad | **No new one.** The anaphora scan found one the cycle-0 eval missed (#3 should have read FOUND, minor): l.65 "that the house was up…, that there was fish, that the girl was thinner…", a narration triad and a retired reflex. → **F3** (third clause varied). Mara's "He read… He read… He has…" (l.117) is argument in speech and is kept. |
| Anything loading the door toward the ending | **Nothing:**<br>• END-1 reserved words "seam" / "niche" / "painted plaster" / "hand flat" = 0 / 0 / 0 / 0;<br>• R9's "as near full size as the little house allowed" says what "at the size of a real one" said, and no more;<br>• R1 and R2 take motion out of the hold, they do not add it;<br>• "seam" ruling respected. |

**Judged and kept (no change):**
- **R1 "Behind me an ungreased axle squealed, and I moved off the road for the cart."**
  - The cart interrupts the hold, and Mara answers it with an act. It does not measure the hold.
  - The rule ("nothing that moves… is put into it") is met.
  - **Carts at a threshold are CLOSED at 2** (Ch.9, Ch.19).
- **l.357 "the road's noise went on round me as before"** (the family's jug, the geese, the mule).
  - This is the touch's negative result: the air is the road's air, and nothing hushes. It is not a duration measure. Kept as at cycle 0.
- **R2's family exit "went past me in at the gate, the boy last…".**
  - The exit is the boy's petal walk, an event in its own right. No stillness verb remains.
- **The race frame "before [X] had":** 3 in narration (l.107, l.149, l.247), not 2.
  - The cycle-0 eval counted l.191 (cut by C4) and missed l.149.
  - l.149 ("before we had gone fifty paces") is a distance idiom, not the competence race.
  - l.107 (the master's brusque exit) and l.247 (the fig before the bed) are character.
  - WATCH: 0–1 in Ch.20.
- **"And…" rejoinders:** 3 openers across 2 owners (clerk ×2, wine-woman ×1), not one owner as cycle 0 said. They are within ≤4, and the bible's "one speaker should own it" is a *should*. WATCH.
- **"wedged against the curb, and the mules…" (R11) next to "eaves to curb, and the red…" (l.211).** A stop-word frame; no reader hears it.
- **The clerk's object-to-the-eye beat ×4 in one scene** (list, leaf, his own tablet, a sailor's tablet). One walk-on bears it, as the bible's cap allows, and the repetition is the evidence Mara argues from. It is CLOSED for Ch.20.

## Finalize fixes (F1–F5), tested together
Each fix is a cut or a near-even swap, and each OLD string occurs exactly once.

| # | Location | Now (cycle-1 page) | → Finalized | Why |
|---|---|---|---|---|
| F1 | l.43 | "Left to myself, I drew the Pentax up by its strap" | "I drew the Pentax up by its strap" | "left" ×4 round "My finger left the button." The previous sentence ("he left me to see to it") already leaves her alone. The anchor sentences are byte-identical. |
| F2 | l.63 | "was arguing with him about it, in Greek at first and then louder." | "was arguing with him about it." | It rebuilt l.13's "[X] at first and then [Y]". The priest-and-fried-food texture stays. |
| F3 | l.65 | "that there was fish, that the girl was thinner than she had been told. The question she put next was about us, and it came slowly enough for me to have all of it." | "that there was fish, and the girl thinner than she had been told. The question she put next was about us." | It breaks the narration's one anaphora triad (third clause varied, per voice-dna §4). It also cuts the 3rd comprehension report and its explanation clause: comprehension 3 → 2; narration "slowly" 4 → 3. |
| F4 | l.287 | "there was a broad patch of new whitewash." | "there was new whitewash." | "broad" 4 → 3, and Grata is "broad" at l.229. "a patch of" stays out (Ch.15 ×2). |
| F5 | l.373 | "still giving back the sun's warmth, and the door stayed cool." | "still giving back the sun's warmth; the door was cool." | "stayed" 3 → 2 near the anchor. "it stayed a picture of a door." and "the coolness stayed in my palm" keep their verb. |

**Reuse checks on every replacement string:**
- Ch.1–18 and samples: "I drew the Pentax", "arguing with him about it", "was about us", "and the girl thinner", "there was new whitewash", "the door was cool" and "warmth; the" occur in none of them.
- My n-gram pass on the five seams finds only grammar 3-grams ("the door was", Ch.1 "The door was locked", Ch.11; "I drew the", Ch.9/11/14; "and the girl").
- No in-chapter double was created.

**Script:** `/tmp/claude-0/-home-user/63791ee5-159c-5791-9429-07920f8d9417/scratchpad/re19/ch19-finalize.py` (`python3 ch19-finalize.py <in.md> <out.md>`).
- Input: the cycle-1 page (md5 `db9b0e7b…`).
- Output: `/tmp/claude-0/-home-user/63791ee5-159c-5791-9429-07920f8d9417/scratchpad/re19/ch19-final.md`, md5 `41dedf4d0160019238d30feef12fb042`, sha256 `a6f5e2bc…`.

**Test results:** the copy was swapped into the manuscript path and run from /home/user/Books.
- `check_chapter.sh 19`: **all clean.**
  - style: 8,272 words, simile 1.1/1k, em-dash 0, foreshadow 0;
  - grammar 0; rhythm 0;
  - show/tell: 8,273 words, dialogue **24.7%**, no flags;
  - voice-wear strict: clean;
  - tic gate: clean (and-chains 6/9);
  - echo 0; metaphor 1.6 fig/1k, median 18;
  - shape CLEAN.
- `tic_report.py --gate`: clean (exit 0).
- `--echoes 19`: none / none / none.
- `shape_check --strict`: `19 8251 4 25 18 scene-set long-fade`, CLEAN.
- **Words: 8,251** (shape_check), which is ≥ 7,900 ✓.
- **Restored:** the manuscript checksum was re-verified after the run (md5 `db9b0e7b…`, sha256 `9af5c485…`). **I did not edit the manuscript.**

**Post-finalize counts:**
- "so that" 4; "the size of a" 1;
- comprehension reports 2 (the half-caught mother-in-law; the baker);
- "considered" 0; "What for?" 0; "two-handed" 0; "and stayed" 0;
- moving-thing holds 0; gaze-arrival 0;
- **#11:** 3 firm (0.36/1k: l.11, l.73, l.207);
- paragraph-final negations 5 (0.61/1k);
- present-tense generalisation 1 (allowlisted);
- "as if" 1 in narration (Grata's "as though" is speech);
- semicolons 18 (2.2/1k); "door" 22;
- "seventy-nine" 1; "where the dead go out" 1 (allowlist 2 of 3);
- the END-1 words 0; citizenship lines 0.

## Genesis Score (cycle 1, scored on the page with F1–F5)
Per-cycle rule: no dimension moves more than +0.5 from cycle 0.

| Dimension | Cycle 0 | Cycle 1 | Evidence | Holds / caps |
|---|---|---|---|---|
| Originality | 9.0 | **9.0** | Unchanged and untouched by any swap: the one hump against the pizzeria's two; "Fine mountain for vines," / "Very fine,"; the painted shadows "falling the opposite way from every real shadow on that road"; the short-sighted clerk; "He was my grandfather. He sold eels." | Not 9.5: the arrival-travelogue spine is a genre standard. |
| Theme | 9.0 | **9.0** | "a room with a door" after a ship where "Nobody … had a door to shut on anybody"; "Ten years," … "They're slow."; "I have some," … "but not here." Texture: the carter's cheese, the geese, the fried-food quarrel (which keeps its priest after F2). | "door" ×22 (2.7/1k): the designed motif, #18 minor. |
| Characters | 8.5 | **8.5** | C1–C4 are cleared on the page: "Sit there. I kept you a bowl." (Grata tells, never asks, and l.389's "the bowl she gave me" pays it); "considered" 0; "Who to?" asked the boy (a child's literalism, fresh); the competence race at the hipposandal cut. Mara 4/4 inhabited; Valens's mind-reading refuted by "black wax on the end of his nose"; Pacuvia's brooch "twice more to be sure". Cover-the-name PASS. | **Held at 8.5, not 9.0:**<br>• Felix ends 12 of 15 speeches on a question (his card, near a metronome);<br>• Valens deflects him with an order twice ("Hold her.", "Eat your beans.");<br>• the clerk's nose-reading ×4 in one scene.<br>These are designed, but a cast at 9.0 would not need the WATCH list. No tic cap: catchphrases 0, gate gesture classes clean. |
| **Prose & Voice** | 8.0 | **8.5** (+0.5) | **The law cluster is gone, cited:**<br>• the three moving-thing holds (R1–R3);<br>• Ch.17's leaf skeleton → "one board and then the other";<br>• the car and subway domains;<br>• "no business to be cool at all";<br>• "and stayed"; the gaze-arrival; "so that" 7 → 4; comprehension 5 → 2 (with F3).<br>**The door paragraph now trusts the hand:** "It was warm, with the whole day's sun in it." / "cool as a glass of water left standing an hour by a kitchen sink." **Stopping sentences intact:** "Seventy-nine. It came unasked, two figures with nothing round them…" / "My finger left the button." (now the paragraph's only "left", F1); "and it stayed a picture of a door." (now its only near "stayed", F5). **Ugly sentence:** "Felix slept wherever a sailor had last moved him on from". **Voice under pressure:** the asides die at the finder and at the tomb, then the voice fails into sleep. | **Not 9.0:**<br>• the road stretch carries some tour-guide edge (l.207 stones, l.229 counter);<br>• the chapter's best sentences are the cycle-0 sentences, and nothing new rises to Kalanithi level.<br>8.5 rests on F1–F5. Without them the page carries a new sideways repeat at its own stopping sentence and a retired-reflex triad. |
| Pacing | 8.5 | **8.5** | Ledger row hit on every field: Chronological; `scene-set` (CONTRAST) → `long-fade`; 4 breaks; dialogue 24.7% (20–30); 8,251 against 8,400 (range 7,900–8,900); median 18 (high). Quick harbor, panoramic road, very slow tomb. Value shift: landed (+) → marked? (−) → papers work (+) → housed (+) → the door found and shut (±). | Not 9.0: the road stretch, about 2,400 words with no live question, is unchanged (structural; see cycle-0 PATH note). **Pacing OK.** |
| Emotion | 9.0 | **9.0** | Anchor: the mountain "small enough to cover with a thumb", the finger off the button. Surprise: "Very fine," / "I was glad he had said it". Body rebel: sleep in one sandal. The door beat is now cleaner: no car, no gloss; the hand finds the cool and the reader weighs it. | Not 9.5: a light romance heart-load for a long chapter (by design after Ch.18). |
| Immersion (Dim 7) | 9.0 | **9.0** | L1 is fixed ("well again by daylight": no Rhegium inversion). Puteoli's mole, the Crypta's dust and torch boys, the hipposandal, vines married to elms, the Herculaneum Gate's three arches, the Nuceria road's columellae. | Tour-guide edges (l.207, l.229) hold it at 9.0. |
| **FLOOR** | 8.0 | **8.5** | | |
| **AVERAGE** | 8.71 | **8.79** | (9.0 + 9.0 + 8.5 + 8.5 + 8.5 + 9.0 + 9.0) / 7 = 61.5 / 7 | |

**Casual Reader: 8.5** (unchanged). The polish is invisible to this reader, as it should be. They still buy on the camera beat ("she can't take the picture") and come back for Grata and the cool door. The mid-chapter road still reads as travel, and the romance is a warmth, not a pull. No vibes problem.

**CVI-Launch 8.85** (8.35 + 0.5 strong anchor), unchanged: every anchor is byte-identical, and F1 removes only the opener before "I drew the Pentax". **CVI-Legacy 7.2**, unchanged.

## Anti-AI scan (cycle 1 + F1–F5; 8.25k words; commercial band 0–8 clean)
| # | Result | Note |
|---|---|---|
| 1 Forced symmetry | FOUND minor | Mostly gone with the car simile. What remains is the search pair (l.203, l.297 door negations) and the designed warm/cool to-and-fro. −0.125 |
| 2 Empty poetic vocabulary | Clear | |
| 3 Rule of three | Clear after F3 | The l.65 "that… that… that" triad was FOUND at cycle 0 and cycle 1 and was missed in the cycle-0 table. It is broken by F3. |
| 4 Em dash | Clear | 0 |
| 5 Empty metaphor | Clear | |
| 6 Dramatic "And" | Clear | Narration 0; speech rejoinders 3. |
| 7 Pseudo-philosophical close | Clear | The close is shutters and a girl singing to a baby. |
| 8 Parallelism | FOUND minor | Mara's "He read… He read…" (speech); Grata's dice; the close's "same two lines" (designed). −0.125 |
| 9 Smooth transitions | Clear | |
| 10 Described emotion | FOUND minor | "I was glad he had said it" (the outline's lie); "He was outraged for them."; "with enormous pleasure". −0.125 |
| 11 Explanatory extension | FOUND minor | 3 firm, 0.36/1k (cap 0.8): PASS. −0.125 |
| 12 Binary negation opener | Clear | Pivots 0. |
| 13 Precision flex | FOUND minor | Twelfth morning, eleven nights, "part of a fourth", fifty-one years. −0.125 |
| 14 Emotional control demo | Clear (edge) | Control fails into sleep. |
| 15 Authoritative description | FOUND minor | Stepping stones (l.207), the counter (l.229). −0.125 |
| 16 Philosophical aside | FOUND minor | "A join showed or it did not." (the distortion, once). −0.125 |
| 17 Clean dialogue | Clear | The carter under his cloak; Felix answering nobody; Grata's floods. |
| 18 Thematic echo chamber | FOUND minor | "door" ×22. −0.125 |
| 19 Graduated reveal | Clear | Chronological walk, long fade. |
| 20 Temperature report | Clear | |

**8/20, −1.0: clean band.** Correction for the record: at cycle 0 and cycle 1, #3 should have read FOUND (9/20, watch band). F3 returns it to 8/20.

## Readers (cycle 1)
- **The Devourer.** No change in where they slow: the road after Puteoli. The door paragraph now reads faster: one sentence of warmth, one of cool, then the test. Finishes satisfied on the door found.
- **The Critic.** The underline set is intact, and what they minded at cycle 0 is gone: the parked car, "no business", the cart behind her. On the cycle-1 page they would have caught "Left to myself" against "My finger left the button." F1 removes it. Nothing new to mind.
- **The Hostile.**
  - Rhegium is fixed.
  - The door is now opened before it is "closed … once more".
  - The brooch is at her throat, where a hood pins.
  - "Well again by daylight" after a day in the Straits reads as "by next morning": acceptable.
  - "twelfth morning" / "eleven nights" is still the author's call (INVESTIGATE, unchanged).
  - F3 leaves the mother-in-law's question quoted whole after Mara caught "perhaps half" of her quick Greek. It is a short, slower question put to the girl, and no reader stops on it.
- **The Casual Reader.** 8.5; see above.
- **The Devoted Reader.** The Ch.17 leaf skeleton, the Greek frame and "What for?" are gone. The re-read details survive untouched: the one hump, "Ten years. They're slow.", "Is this one yours?", the backs of her fingers, then her palm.

**Cross-reader:** no CRITICAL; no VIBES PROBLEM. The road-stretch sag (Devourer and Casual) is structural and accepted, as at cycle 0.

## The Tomorrow Test
Unchanged and strong. IMAGE: Vesuvius in the finder, small enough to cover with a thumb, and the finger leaving the button; the painted door cool in a warm white wall, its painted shadows falling the wrong way; a boy with rose petals on his soles. QUOTE: "Seventy-nine."; "Fine mountain for vines." / "Very fine." **ANCHOR EXISTS** → +0.5 CVI-L.

## Pacing check (one line for `feedback/progress.md`)
**Ch.19 (FINAL after F1–F5): PASS.**
- 8,251 words (target 8,400; range 7,900–8,900; not padded);
- dialogue 24.7% (20–30 ✓); 4 breaks ✓; gear high (median 18) ✓;
- `scene-set` → `long-fade` (Ch.17 `short-punch`/`quiet`, Ch.18 `I-statement`/`punch`: no run of three);
- a long panoramic arrival after the short hinge (6.9k → 2.5k → 8.3k);
- quick harbor, panoramic road, very slow tomb;
- the road sag is accepted as the ledger's walk.

**Verdict: OK.**

## VERDICT
**PASS** on the page with **F1–F5 applied** (tested together; the script above). The orchestrator applies the finalize script, confirms md5 `41dedf4d…`, then finalizes.

| Measure | Result |
|---|---|
| Scores | Originality 9.0 · Theme 9.0 · Characters 8.5 · **Prose 8.5** · Pacing 8.5 · Emotion 9.0 · Immersion 9.0 |
| **Genesis Floor** | **8.5** |
| **Average** | **8.79** |
| **Casual** | **8.5** |
| Pacing | **OK** |
| CVI-Launch / CVI-Legacy | 8.85 / 7.2 |
| Mechanical suite (with F1–F5) | all clean; echoes / command echoes / spoken-line echoes none / none / none; shape CLEAN |
| Foreshadowing / END-1 reserved words / "seam" ruling | 0 / 0 / respected |
| Anti-AI | 8/20, −1.0 (clean) |

**Gate (Floor ≥ 8.5 AND Casual ≥ 8.5 AND pacing OK): MET.**

## Character-bible Ch.19 re-syncs (exact list; the bible's Ch.19 blocks still quote the writer's draft)
Every quote below was checked by script against the finalized page (`ch19-final.md`, md5 `41dedf4d…`). Label each synced block: *"SYNCED to the FINAL page 2026-10-21 (md5 `41dedf4d…`): dialogue-polish, hook-craft, disruptor, continuity repair W-01…W-14, polish cycle 1 (L1–L2, C1–C4, R1–R15, D1–D6), finalize F1–F5; quotes checked by script."*

**1. MARA, Ch.19 block (l.511):**
- Remove "None at all." and "Many people's, I should think. A farm each." from the uncontracted-Latin examples. The frost/ownership exchange was cut by dialogue-polish and is never on the page.
- The lie: "I agreed with all of it" → **"I agreed with him, and I was glad he had said it"**.
- Materials list: the lead pipe "soldered down its length" → **cut**. The page has only "a trench where the paving had been lifted for a new lead pipe".
- Add: **comprehension reports 2**, "of which I caught perhaps half" and "I had kept the fuller and his wife out of all that, and lost the baker entirely." Neapolis is followed by act, not claim ("and I stood under her balcony for the rest of it"). "I understood every word" and "slowly enough for me to have all of it" are cut.
- Add: the camera is drawn with no opener ("I drew the Pentax up by its strap"); "Alone at the rail" and "Left to myself" are both off the page.

**2. VALENS, Ch.19 block (l.1092):**
- Cut from Lines: "It lies right to the sun. With the sea under it, that slope'll see no frost to speak of." / "Whose is it?" / "That's the way to own a mountain. A man can walk round his own piece of it in a morning and see to it himself." (dialogue-polish). Also "He looked hard." (cut).
- "And carting? Who wants it?" → **"Carting? Who wants it?"**
- "It's cheaper," … "You dig, and the earth makes the seats." → **"They dug the bowl and banked the earth from it round the sides for the seats," … "That saved them stone."**
- "And the other?" → **"The third?"** (answering "Seven or eight. Three have tombs worth the walk.").
- Hands: "the bar dropped and lifted" → **"shut it, set the bar in its brackets and lifted it clear, opened it, and closed it once more, slowly, to see how it hung on its leather"**.
- "the noseband cut from the cobbler's leather" → **"out of the one long strip the nephew had missed"**.
- The hipposandal is laced with no race ("before Felix had a hand on her halter" cut).
- Add: orders to Felix as deflection ×2 ("Hold her.", "Eat your beans."): WATCH, ≤1 in Ch.20.

**3. FELIX, Ch.19 block (l.1748):**
- "could have spat on either" → **"I could spit on the pair of them from here, Achaea to the left and the Locrians to the right, and never shift my feet. Which shall I do first?"**
- "Is that the emperor's? Who's rowing it? How many are under there?" → **"What ship's that, the emperor's? Who's rowing it? How many are under there?"**. The opener note "one 'Is that'" → **"Is it" / "Is that" openers 0**.
- Torch boys: "What if it goes out? Can I carry one?" → **"Do you live in there?" … "Give me one. I've the steadiest hand on this road."**
- "he had eaten half of Italy already" (narration) → spoken: **"That's half of Italy I've eaten already, and the rest of it's up my nose. Are there more hills like that before Pompeii?"** (after "Felix spat brown at the verge"). In the Spent list, "eaten half of Italy" → "half of Italy I've eaten".
- Add Neapolis: **"In a city this big, where's the fighting? Who's your best man? I'd put him down for you."**
- Cheese men's news: "Ten years! And all that while they had to go by it empty? …" → **"…And the Senate at Rome stopped their games for ten years over it." He was outraged for them. "And all that while they had to go by it empty. They're back now, every spring, the cheese men said. Will it be this spring? Have we missed it?"**
- Amphitheater: "Did you know it would be sunk? Have you seen one sunk before? Why would you sink one?" → **"Did you know it would be sunk? You could drop a house in it and never see the roof."**
- Add: **"Roofs, and somebody's washing, and your fig in the way of the rest of it,"**.
- Add WATCH: question endings 12 of 15 speeches; Ch.20 gives him two speeches that end on a boast or a fact.

**4. POMPONIA GRATA card, Ch.19 block (l.2055).** Change the header to SYNCED.
- Counter: "reached the street's edge in two arms of masonry set at a right angle, faced with offcuts…" → **"Her counter ran out to the street's edge, faced with offcuts of colored marble, green and yellow and a purple shot through with white, pieced together wherever a piece would fit"**.
- "ten years we've been at it, ten years since the earth went" → **"it's been carts and dust since the earth went, and the forum still looks like a builder's yard. Drink that before it cools."**
- "I saw you at that wall yesterday with your nail in it, half the street saw you." → **"I heard about you at that wall yesterday with your nail in it, half that street saw you."**
- "Sit there. Eat that." → **"Sit there. I kept you a bowl."** (C1).
- "touched him on the arm too as she went by him" → **"touched him on the arm as she went by him to the door next to hers"**.
- Touch: "her hand on Mara's sleeve" → **"She caught a pinch of my sleeve and talked on holding it, her fingers warm from the pot."**
- Whitewash: "a patch of new whitewash the size of a door" → **"there was new whitewash. It was still dark with wet at its edges"** (R8 + F4). In the Spent list, "the whitewash patch described" now quotes this.
- Add: **"Rooms, I said, and I've got them."**
- Add rule: **card rhythm examples ("Eat this. Hold that.") and Ch.1's "Eat that," = 0 on the page.**

**5. Pacuvia named** (walk-on note l.3003, at-risk after Ch.18 l.5079, PACUVIUS card l.3674):
- The daughter is **named in narration**: "The master's girl, Pacuvia," (l.13), "Pacuvia found me" (l.17), "Pacuvia went down our plank first, with the brooch at her throat," (l.65). She is labelled "Pacuvius's girl" once (l.11) and "the girl" thereafter.
- Supersede at-risk after Ch.18's "the master's daughter: unnamed; labelled once".
- She is named and speaks in Ch.18 and Ch.19. Per CLAUDE.md step 5 she needs a **MINOR NAMED CHARACTERS card**, with:
  - attention: the mother-in-law's verdict;
  - syntax: practical worry run-ons ("and if it won't hold I'll have to fasten myself up with a thorn");
  - evasion: that the brooch was ever broken;
  - physicality: pins, unpins, pins "twice more to be sure";
  - verbal tic: none.
- The PACUVIUS card's evasion (he never says her name) holds: only the narration names her.
- Walk-on quotes:
  - "well again by Rhegium" → **"well again by daylight"**;
  - "in a Greek that was suddenly as good as anybody's" → **"and her Greek was suddenly as good as anybody's"**;
  - her quay dress → **"with the brooch at her throat"** ("her good blue" now at l.17 only).

**6. Ch.19 walk-ons (l.3003):**
- **The mother-in-law:**
  - Her question to "who had slept on the deck" → **"Those on your father's deck, who are they?"**
  - Her report → **"of which I caught perhaps half: that the house was up at the highest part of the town, that there was fish, and the girl thinner than she had been told. The question she put next was about us."** The gaze-arrival "Then her eyes went past the girl to us" is cut.
- **The harbor clerk:**
  - "Whose freedman?" → **"Freedman of whom?"**
  - The leaf read "two-handed" → **"The clerk lifted it to his nose and read it there, slowly, one board and then the other. He left it lying open,"**.
  - Record his object-to-the-eye beat as **4 instances in one scene** (list, leaf, his tablet, a sailor's tablet): CLOSED for Ch.20.
- **Puteoli texture:**
  - The Alexandrians' topsail "which no other ship in the harbor flew" → **"carried a little three-cornered sail high on the mast above the yard"**.
  - The priest → **"was arguing with him about it."** (no language detail; R13 + F2).
  - The mole → **"the sea had eaten the brick off the lowest courses and bared the gray core, packed full of pebbles"**.
- **Pompeii walk-ons:** "the man raking water into the lime pit" → **cut**. Add "The black nosed into a trench where the paving had been lifted for a new lead pipe, and Felix dragged her out of it by the halter."
- **The eel family:**
  - "What for?" → **"Who to?" asked the boy.**
  - The boy's "He considered my hand on the door." → **cut** (C2).
  - The exit → **"The family soon had their baskets and their cloths together and went past me in at the gate, the boy last, walking on the outsides of his feet to keep the petals on."**
- **The cobbler's shop:** "The floor was beaten earth with scraps of leather trodden into it" → **"The floor was beaten earth,"**. The leather crescents stay at l.275.

**7. At-risk after Ch.19 (l.5084).** Change the header to SYNCED; then:
- "Fine mountain for vines" entry: delete the frost/ownership exchange (never on the page; the cut-detail rule bars restoring it). The lie → "I agreed with him, and I was glad he had said it".
- Seventy-nine → **"Seventy-nine. It came unasked, two figures with nothing round them, while the mountain stood small and green in the glass."**
- The tomb set:
  - "at the size of a real one" → **"as near full size as the little house allowed"**;
  - white plaster warm "as the hood of a parked car on a June afternoon" → **"It was warm, with the whole day's sun in it."**;
  - add the cut: "it had no business to be cool at all";
  - add **"Whenever I tried the white plaster next to the door it was still giving back the sun's warmth; the door was cool."**;
  - add the cart beat **"Behind me an ungreased axle squealed, and I moved off the road for the cart."**
- "where the dead go out": "…as the god had put it in Valens's mouth" → **"This was where the dead go out, and they had followed the road out in their hundreds and settled in."**
- The search:
  - "Eight, in all. Only two have tombs worth the walk." / "And the other?" → **"How many gates are there?" / "Seven or eight. Three have tombs worth the walk." / "The third?" / "The Nuceria Gate. Tomorrow."**
- The distortion set: delete "Anybody in the street could see exactly where that house had split." (cut). The page has **"This one showed to everybody who came down that street, and the plasterer should have been made to stand in front of it from dawn to dark and hear what they said."**
- Mind-reading: delete "He looked hard."; add **"He did that to no other man on the mole. He'll know me again."**
- Texture: delete the Broad Street subway comparison, the lime pit and "the lead pipe soldered down its length".
- Spoken shapes spent:
  - delete "None at all.", "Whose is it?", "That's the way to own a mountain.", "He looked hard.", "It's cheaper," … "You dig…" and "Is that the emperor's?…";
  - add "What ship's that, the emperor's? Who's rowing it? How many are under there?", "Carting? Who wants it?", "How many gates are there?", "Seven or eight. Three have tombs worth the walk.", "The third?", "They dug the bowl…" / "That saved them stone.", "Freedman of whom?", "Those on your father's deck, who are they?", "Married people," … "Corinthians. They had mules.", "Who to?", "Rooms, I said, and I've got them.", "Sit there. I kept you a bowl.", "I could spit on the pair of them from here…", "Light you through, mistress? A copper, and you'll see your own feet.", "You can carry your mule,".
- **Counts → FINAL page:**
  - **Length and shape:** 8,251 words (shape_check), 8,272 (style), 8,273 (show_tell), 8,999 (`wc -w`); dialogue 24.7% (shape 25); median 18; 4 breaks; `scene-set` → `long-fade`.
  - **Punctuation and figures:** em-dash 0; ellipsis 0; semicolons 18 (2.2/1k); "as if" 1 in narration (the ankle) + 1 "as though" in Grata's speech; similes 9 by metaphor_check (1.1/1k style).
  - **Reflexes:** and-chains 6; negation pivots 0; hinge / So openers 0; the race frame "before [X] had" 3 (l.107, l.149, l.247); "without" 2; sentence-initial "Nobody" 1; said/told-the-[non-listener] 0.
  - **Gestures:** kneel/crouch 0; hand-on-knee 0; bends 0; gait exits 0; deliberation pauses **0** ("He lay quiet a while" cut).
  - **Speech:** bare "No." Valens 0 (Mara 1); narrated non-answers 0; command echoes 0; "And…" rejoinders 3 (clerk 2, wine-woman 1).
  - **Narrator moves:** walk-on object to the eye 1 bearer / 4 instances; thumbnail probe 1; "Somebody had [verb]" 1; credential asides 0; comprehension reports 2; "so that" 4; "the size of a" 1; "considered" 0.
  - **Memories:** the pizzeria clause; the plaster panels "at home" clause (both triggered).
  - **Other:** teeth 0; laughs Valens 1; English 0; AD 79 1; "door" 22; #11 3 firm (0.36/1k); paragraph-final negations 5 (0.61/1k); anti-AI 8/20; foreshadowing 0; echoes 0.
- **New SPENT / CLOSED / WATCH entries:**
  - **held moments measured by anything moving** (traffic, people leaving, shadows): 0, restated; **carts at a threshold:** CLOSED at 2 (Ch.9, Ch.19);
  - **car comparison domain:** CLOSED (Ch.2, Ch.5, Ch.13); **subway domain:** used (Ch.3);
  - **"It was the first [X] I had [V]":** CLOSED (Ch.7 ×2);
  - **comprehension reports:** ≤2 per chapter, never "understood every word" (Ch.19 at 2);
  - **gaze-arrival "Then [poss] eyes went/came…":** SPENT, restated;
  - **"considered" as a beat:** WATCH (7 book-wide), 0 in Ch.20;
  - **"What for?":** CLOSED; **"two-handed":** CLOSED at 2 (Ch.11, Ch.15);
  - **narration "so that":** WATCH >4; **"the size of a" as a ruler:** ≤1 per chapter;
  - **"And…" rejoinders:** ≤4, one owner preferred (Ch.19: two owners, 3);
  - **card rhythm examples and Ch.1's "Eat that,":** 0;
  - **Valens's orders to Felix as deflection:** WATCH (2), ≤1 in Ch.20; **"Out where the dead are"** in Valens's mouth: once;
  - **the backs-of-fingers test, the knuckle tap, "the whole of my palm", "it stayed a picture of a door":** SPENT. Ch.30, 36 and 41–42 stage the threshold another way, and Ch.42's refusal is never "a picture";
  - **the warm-as / cool-as pairing at a threshold:** SPENT;
  - **"[X] at first and then [Y]":** 1 per chapter (Ch.19 keeps l.13's whisper-then-aloud);
  - **"[body part] left [object]" as a release beat:** SPENT at 2 ("My finger left the button."; "When my hand left it"), 0 in Ch.20;
  - **"stayed" near an anchor sentence:** ≤2;
  - **reported-speech "that…, that…, that…":** a triad like any other: break the third;
  - **the race frame "before [X] had":** 0–1 in Ch.20;
  - **a walk-on's object-to-the-eye beat:** Ch.19's bearer is the clerk, and Ch.20 has none;
  - **Felix's question endings:** WATCH (12 of 15);
  - **the master's daughter:** named (Pacuvia), done unless she returns.

**BIAS CHECK:** This evaluation was produced by the same system that wrote the prose. Confidence in scores above 8.0 requires external validation (beta readers, editors, comp analysis). The Prose 8.5 depends on F1–F5. The Casual 8.5 and the Pacing 8.5 for a long panoramic arrival are the scores most likely to differ for a human reader.
