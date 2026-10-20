# Evaluation: Chapter 13 — The Seventh of Bysios (run 2)
**Evaluator:** book-evaluator (independent; did not write or revise this prose) | **Date:** 2026-10-20
**Text evaluated:** `manuscript/chapters/chapter-13.md` at `a94ddd5`, after writer → dialogue-polish → hook-craft → disruptor → continuity repair (C-01, W-01…W-20). **7,541 prose words** (shape_check), 7,559 (style_check), 7,796 (`wc -w`, including the header).
**Read against:**
- book CLAUDE.md hard gates;
- STATE.yaml: guardrails, NO FORESHADOWING, NO TICS (gestures included), the retired reflexes, AUTHOR-CP2-1…4;
- voice-dna §0 (stance, and Ch.13 = "only the word"), §1, §3b, §4 (allowlist);
- character-bible.md: the Valens, Theano, Kallia, Felix and Praxias cards, the Ch.13 walk-on block, and every at-risk block from "after Ch.1" to "after Ch.13", plus the at-risk table;
- outline Ledger row 13 and `## Chapter 13`;
- chapter-12-eval.md (cycle 0 and cycle 1);
- chapters 11 and 12 for pacing;
- the Ch.13 continuity audit;
- voice-bank samples 01–13 by n-gram.

**Genre profile:** commercial historical romance / time-slip, comp *Outlander*. Anti-AI band: commercial (0–8 clean, 9–11 watch). Engagement: empathy 55 / fascination 30 / self-insertion 15. Dimension 7 = **IMMERSION**.

**Measured here.** `bash books/the-hour-of-ash/tools/check_chapter.sh 13` is **clean on every gate**:
- style: simile 2.0/1k, em-dash 2, foreshadow 0;
- grammar 0, rhythm 0, show/tell no flags (dialogue 37.9%);
- voice-wear strict clean; tic gate clean (and-chains 5/9, credential asides 0, negation pivots 0, "So" 0);
- echo 0; command echo none; metaphor fig 2.5/1k, median 14;
- gesture classes for Ch.13: object handling 3, swallow 2, **hand / chin on the knee 2** (cap 8 for this length), jaw 1;
- `shape_check`: `13 7541 4 38 14 scene-set dialogue`, CLEAN.

**My own scans (scratch, not gates):**
- 3-grams against all 13 samples, and 4/5-grams against Ch.1–12;
- a hand classification of the stage business the gate cannot classify;
- a paragraph-final negation count;
- every SPENT / closed item in the bible, grepped;
- an #11 count by hand.

**Every fix in the PATH was applied together to a scratch copy, swapped into the manuscript path, run through the real `check_chapter.sh 13`, `shape_check --strict`, `voice_wear_check.py` and `tic_report.py --gate`, and then the original was restored** (sha256 verified; the worktree is clean). I did not touch the manuscript.

*(l.N = line number in the current `chapter-13.md`.)*

---

## HEADLINE
**CVI-Launch (CVI-L):** 9.8 (9.3 base + 0.5 strong anchor) | **CVI-Legacy:** 6.8 (provisional) | **Genesis Floor:** **7.5** | **Genesis Average:** **8.50**
**Casual Reader:** **9.0**
**Engagement type:** Fascination and Empathy share the lead here: the inside of the oracle through a bodyguard's eyes, a Pythia with bad knees, and the god's own words carried out by the man she cannot stop trusting. Self-insertion is tertiary: the reader holds the word "Pompeii" with her.
**Divergence alert: YES (9.8 − 7.5 = 2.3).** *Commercially the strongest chapter so far, and held below the gate by two mechanical caps.* The story, the structure, the anchor and the last word do not need changing.

**Gate (Floor ≥ 8.5 AND Casual ≥ 8.5 AND pacing OK AND gates clean): NOT MET.** Casual 9.0 ✓, pacing OK ✓, gates clean ✓. **Two dimensions hold the floor at 7.5, each by a cap:**
1. **Prose & Voice: #11 explanatory extension is over the commercial cap.** There are 8 instances, 1.06/1k, against the >6 / >0.8 line. One was added by the continuity repair (W-01's Etna clause). On merit Prose is 8.0, held there by a cluster of book-law items the gates cannot see:
   - two present-tense generalizations in narration;
   - Ch.7's "in that country … said … in it" frame;
   - a fourth command echo;
   - a comparison in Valens's speech;
   - two group-address tags;
   - two gait exits;
   - "at a run" ×3;
   - the boy-introduction skeleton for a third time;
   - a beat that depends on Praxias's capped "little cousin";
   - sample-07's reserved "a painted door".
2. **Characters: the stage business the gate cannot classify.** The *deliberation pause* class (a listener considers, thinks, takes a while before answering) has **9 instances**, which reaches the gate's own cap for a chapter this long (8). Valens carries 4 of them. Book-wide the class had never exceeded 2 in a chapter. This is the author's "pausing for a long moment" class in other words.

**Every fix is a clause swap or a short cut, and all were tested together:**
- 7,508 words, still over the 7,500 brief floor;
- dialogue 38.1%; median 14; 4 breaks; `scene-set` → `dialogue`;
- all gates clean; echo 0;
- the first and last lines are byte-identical.

---

## Genesis Score (Craft Assessment)

| Dimension | Score | Evidence | Cap reasons / holds |
|---|---|---|---|
| Originality | 9.0 | **The outline's subversion is on the page:** she is not let into the room, the prophecy reaches her through a gladiator's memory, and the precise truth comes from an old woman mid-complaint. The writer's inventions on top of it: (1) **the goat drenched until she shakes**, "It took a jar." (l.86–l.90); (2) **the inside as a bodyguard reports it**: "There's one door. I looked for another."; "Stone color," and the omphalos reaching Mara "as a man with a cough standing next to it" (l.138–l.158); (3) Pindar's iron chair and the Boeotian moved off it: "He said a chair was a chair." (l.144); (4) **Felix in the god's book**: "What did it look like?" / "Small." / "His ears had gone red to the tips." (l.120–l.124); (5) **the word Valens "didn't keep"**, not Greek, given twice (l.174–l.182), which becomes Theano's last word; (6) the priest's raised flat hand, shown with Valens's own scarred one (l.186); (7) **"Where does the town stop, then?" / "Where a board by the road says it does,"** (l.328–l.330); (8) the forms: "You don't go in at the fourth." (l.370); (9) the left-ears votives (l.238); (10) the well-woman: "I'll dig it at night, and tell him the god changed his mind." (l.264); (11) **Theano**: the stool and the council, the god as an employer, the branded basket and the lie, the crows that sat quiet at a burying, "they take it and put shoes on it", and **"Yours stood. I'd have said nobody was there, except the floor gave when he stepped to it."** (l.440–l.470). | **≥9.0 challenge:** would a senior editor set the oracle day beside *Outlander*'s set pieces (Craigh na Dun, the witch trial)? Yes. The genre's trance-lit chamber is replaced by procedure, smoke and knees, and that is fresher than the comp. **Not 9.5:** some frames are borrowed. The jug boy's age-and-tunic introduction is the third boy built that way (V8). The apotropaic spit into one's own dress is the Ch.4 goat-boy's gesture (WATCH, below). |
| Theme | 8.5 | "Where home is, answered with a place that is also a grave" is carried by plot and by texture. **Plot:** "Where is my road home?" gets "where the dead go out of the city". **Texture:** cemeteries "in fields … with fences round them" against "Inside the walls?"; a town's edge as "a board by the road"; names written in the god's book and "Mine's written. At Corinth." (l.382); Kallia's "There's floor," (l.394); Theano's room, "Nothing in it was the god's." (l.448); the imagined first hour home: vent, socks, freezer, fork (l.224). **Texture that means nothing:** the Elateian's ears, the fig-seller "swearing … that they were Chian", the wine-stained bandage, the cat in the ash, the almonds. | **Held at 8.5.** Two lines state the irony instead of letting it stand: "the god had very kindly agreed with the clerk and Kallia and the whole of the lie" (l.308) and "It is not an address. It is a description of the empire." (l.342, in speech). No echo chamber. |
| **Characters** | **7.5** | **On merit, 8.5.** **Valens:**<br>- he watches the crowd, refuses the pills ("I want my head, in there.");<br>- he reports the inside as exits, floors and men;<br>- he stands unasked to give the answer;<br>- he cannot start in the middle;<br>- "The boy wanted it written down somewhere.";<br>- he takes the corner of the street.<br>**Kallia:** her first question is about the servant ("The girl that dressed the wife's hair … What became of her?", l.16); "Five hundred," very low; "There's floor,".<br>**Felix:** a fast question-stacker, red to the ears over his name in the book; "He goes like this when a mule dies," (l.276).<br>**Theano** matches her card point by point: knees, crows, grievances, no comfort, the WHEN refused in her own words.<br>**Praxias:** his fingers smoothing a quail that isn't there (l.50).<br>**Walk-ons are people.**<br>**Cover-the-name: PASS.** Mara's chaos is 4/4 (below). | **CAPPED at 7.5: the deliberation-pause class reaches the gate's cap** (9 ≥ 8 for a 7,541-word chapter; the same rule `tic_report --gate` applies to the classes it can see). The nine:<br>- l.64 "He considered the two small white things";<br>- l.124 "Felix stood with that.";<br>- l.170 "He thought.";<br>- l.218 "gave him some thought";<br>- l.232 "He considered me, and the wall, and the women";<br>- l.254 "He was quiet for three steps.";<br>- l.280 "He thought about it.";<br>- l.328 "He considered that.";<br>- l.378 "That took him a while".<br>Book-wide the class ran 0–2 per chapter (Ch.8 2, Ch.9 2, Ch.12 1). **Valens holds four**, so the pause before answering is starting to become his stage business.<br>**Also on merit:**<br>- one comparison in Valens's speech, "the way you'd read anything out" (l.162), against his card's distinctness guarantee ("never compares one thing to another");<br>- the jug-boy introduction skeleton (V8). |
| **Prose & Voice** | **7.5** | **Stopping sentences:**<br>- "**Yours stood. I'd have said nobody was there, except the floor gave when he stepped to it.**" (l.466);<br>- "**It was the most comforting thing I had seen in Delphi. The god could be helped along. It took a jar.**" (l.90);<br>- "the most famous stone in the world had reached me as a man with a cough standing next to it" (l.158);<br>- "**I left out his hands, which were his.**" (l.12);<br>- "it was as much use to me as a bus ticket with the town torn off" (l.374);<br>- "**Nothing in it was the god's.**" (l.448);<br>- "A thing that'll sit quiet at a burying can have my barley." (l.462).<br>**Underlines:** "a man praying through his teeth"; "like the inside of a stone"; "ears like two folded pancakes"; "his right hand held stiff before him like something borrowed"; "as flat as a price for a lame ewe"; "a row of rooms laid open like cupboards"; "Blood goes brown when it dries,"; "I'm a Phocian,".<br>**Ugly sentence:** "He glanced on at Valens's face, the crust on it and the bruise below it, and back at the coins" (l.52).<br>**The ears sentence (l.238) is inhabited irrelevance,** broken off by Felix going over the wall.<br>**Voice under pressure:** level 1, briefly, at the recital. The asides stop for the hair on her arms, and the analysis that follows is how she copes. | **CAPPED at 7.5: #11 over the commercial density cap** (8 at 1.06/1k against >6 or >0.8/1k; list in the scan). **Without the cap it holds at 8.0** for the law items under "The book's own laws" (P1–P9): present-tense generalizations, the Ch.7 frame, the fourth command echo, Valens's comparison, group tags, gait exits and "at a run", the boy skeleton, the "little—" callback, sample-07's 3-gram, and four in-chapter doubles. Anti-AI 10/20, −2.0 (watch band). |
| Pacing | 9.0 | **The ledger row is hit on every hard field:**<br>- Parallel (*outside / inside*) between Ch.12's In medias res and Ch.14's Fragmented ✓;<br>- open `scene-set` ("The morning on which Apollo would first answer anybody that year…", a fresh paraphrase; the allowlisted day is not in the body) ✓;<br>- close `dialogue`, "Pompeii." ✓;<br>- 4 breaks ✓; dialogue 37.9% (35–45) ✓; gear mid, median 14 ✓;<br>- 7,541 against 8,000, inside the 7,500–8,500 range ✓.<br>**The alternation is the engine.** B1 withholds the answer while A2 shows Mara deciding it is "no road" and being "almost calm" (l.284). The two strands meet at "When he had told that much, he got to his feet." (l.288).<br>**Speed design:** the ritual is slow; the interview is measured; the wait dawdles and is jolted by the false alarm; the recital stops time; Theano is quick and dry; the last word is a drop.<br>**Value shift:** − (she decides there is no road) → + (a direction, the hair) → − ("It is not an address") → + for Mara and − for the reader (Pompeii).<br>**Pull 10.** | **≥9.0 challenge:** a 7.5k ritual-and-report chapter that a reader finishes at a run, because the alternation hides the answer and the last word detonates. **Not 9.5:** A2's wait (l.204–l.264: the well, the bowl summons, the ears, the bandage, the knuckles, the husband) is the slow patch, and A1's retelling at the spring (l.8–l.14) recaps Ch.12 for a reader who has just read it. |
| Emotion | 9.0 | **The anchor lands** as the outline planned: he stands "with his weight on both of them evenly and his hands open at his sides", gives the answer once "with the stops in them where the priest must have put them" (l.290–l.292), and then cannot take it up from the sea ("You don't go in at the fourth.", l.370). **Surprises land:** (a) Mara settles on the worst answer and is "almost calm" (l.284), and is then given a road; (b) the comfort of a rigged omen (l.90); (c) the precise word comes from a woman grunting as she shifts on her stone (l.502). **Body rebel:** "The hair had stood up along both my arms … and it would not lie down again." (l.296); Felix's ears (l.124); "I heard myself and kept on." (l.342). **Techniques ≥5:** physical sensation (frost, cold wall), humor in awe (the drench, "Stone color"), silence ("Valens was silent the length of the Way"), dramatic irony (the reader hears "Pompeii"), object proxy (the pills, the branded basket left "by her foot. I left it there."). The peak is not a laugh ✓. | **≥9.0:** the recital and the last word are the book's strongest one-two so far. **Not 9.5:** by law Mara gives "Pompeii." no reaction, so the reader carries the peak alone, and her own feeling is held in the hair and the analysis. That is right for Ch.13 and caps it. |
| **Immersion** (Dim 7) | 9.0 | The audit verified the period detail:<br>- the lion spouts smoking in frost; priests bathing at the rock basin;<br>- laurel wreaths with woollen tails;<br>- the Chian altar "gone brown with old fat"; the gilt shields lighting one by one;<br>- the goat drench (Plutarch); stamped honey-and-meal cakes on branded trays;<br>- the precinct's rod-bearers; the queue called by city, with Delphians first;<br>- the pronaos maxims; the laurel and barley hearth; the omphalos "tied over in a net";<br>- Pindar's chair; the screen; the *prophetes*; hexameter with a hanging tail;<br>- three Pythias once and one now; clay votive ears; the Corcyraean bull. | **Held at 9.0.** #15 minor: the sunrise paragraph (l.38) and the altar are complete and certain. The ethnonym density (Thessalians ×10, Achaeans, Locrians, Coans, Phocians, Boeotians, Elateia, Amphissa) is a Casual friction. |
| **FLOOR** | **7.5** | Characters (capped) and Prose & Voice (capped) | |
| **AVERAGE** | **8.50** | (9.0 + 8.5 + 7.5 + 7.5 + 9.0 + 9.0 + 9.0) / 7 = 59.5 / 7 | |

**Trajectory vs Ch.1–12** (finals 8.50–8.71; cycle 0s mostly 8.0; Ch.10 and Ch.12 at 7.5 on the #11 cap): this is the thirteenth cycle 0 held by narrator recurrence, and the third held by the #11 cap. The pattern from Ch.10 and Ch.12 repeats: **a continuity repair added an explanatory clause.** W-01's Etna sentence is one of the eight. The new finding is a **stage-business class the gate does not model** (the deliberation pause), which reached the gate's own cap.

---

## CVI-Launch Breakdown
| Input | Score | Evidence |
|---|---|---|
| Commercial Pacing | 8/10 | The hidden answer pulls through B1/A2; the false alarm (l.240) and Valens's silence down the Way (l.282) keep the wait alive; the last word is the book's hardest pull. Loses 2 for the length, the recap at the spring and A2's dawdle. |
| Tomorrow Test | 8 anchors → 10 | IMAGE: the goat drenched until she shakes; Valens standing in the court, hands open, reciting; a board of clay ears, all left ones; Theano throwing the god's branded barley to the crows. QUOTE: "It took a jar."; "Yours stood."; "they take it and put shoes on it"; "**Pompeii.**" |
| Casual Reader | 9.0/10 | See report. |
| Shareability (quote / plot / emotional) | 4 / 5 / 4 → 8 / 10 / 8 → **9.5** | Quote: "they take it and put shoes on it"; "It took a jar." Plot: "the Oracle of Delphi tells her the door home is in **Pompeii**". Emotional: "the gladiator carries her prophecy out word for word and can't start it in the middle". MAX 10 × .6 + AVG 8.67 × .4 = 9.47. |
| Concept Pitch | yes → 10 | |
| Human Closeness | yes → 10 | The telling in Kallia's court, Kallia and Mara at the spring, and woman to woman at Theano's door. |
| **CVI-Launch** | **9.3 + 0.5 = 9.8** | 8 × .2 + 10 × .2 + 9 × .2 + 9.47 × .2 + 10 × .1 + 10 × .1 = 9.29. A one-chapter formula; see BIAS CHECK. |

**CVI-L note.** In this project "CVI-L" means **CVI-Launch: 9.8**, level with Ch.8 as the book's highest (Ch.12 9.7, Ch.11 9.5). It is high because this is the turning point: the WHERE, delivered by the one word every reader already knows. The PATH moves no anchor, so CVI-L is unchanged after polish.

**CVI-Legacy (default weights; provisional):** Originality 9.0 × .30 + Theme 8.5 × .25 + Cultural Vocabulary 2 × .20 + Re-readability 7 × .15 + Identity 5 × .10 = **6.8** (Ch.12 6.6). Re-read rewards:
- the word Valens "didn't keep" (l.178) is the city;
- "Not Greek, so not the god's" (l.474);
- Felix's "What if it's Italy?" (l.332);
- "Etruria is by a western sea, with vines on its hills" (l.342);
- "Which of those it is, is mine to know." (l.488).

---

## Anti-AI Scan (20 patterns; density per 1,000 words at 7.54k; commercial band)
| # | Pattern | Result | Count / density | Citation |
|---|---|---|---|---|
| 1 | Forced symmetry | FOUND minor | 1 (0.13) | l.194 "I told him the goat was hers." / l.198 "I told him it was hers." (designed). **−0.125** |
| 2 | Empty poetic vocabulary | Clear | 0 | |
| 3 | Automatic rule of three | FOUND moderate | 5 (0.66) | l.8 "bread, or hot water, or the way to the stadium"; l.68 "the ramp, the steps, the faces at the wall"; l.92 "the cut and the blood … and the boy beginning on the skin"; l.204 "Achaeans and Locrians and a whole ship of Coans"; l.282 "past the treasuries and the bronze bull and the stalls at the gate". **−0.25** |
| 4 | Em dashes | Clear | 2 | Both are speech cut-offs (Felix, Praxias). |
| 5 | Empty metaphors | Clear | 0 | Every simile characterizes. |
| 6 | Dramatic "And" openings | Clear | narration 0 | Speech only ("And yours?", "And the boy?"). |
| 7 | Pseudo-philosophical closings | Clear | — | Scenes end on an act or a line ("There's floor," / "Pompeii."). |
| 8 | Excessive parallelism | FOUND minor | — | Doubled-verb pick-ups 2 (l.10/l.12 "told her the rest. / I told it"; l.366 "He began, and broke off. He began over"), at the ≤2 the Ch.12 eval set. "a road … A road could be said" (l.282). Speech anadiplosis (Praxias "frost. A frost-morning"; Theano "council. The council!") is character. **−0.125** |
| 9 | Overly smooth transitions | Clear | hinge 0 | "Outside, the morning went on without him." is the Parallel seam, by design. |
| 10 | Described emotions | FOUND moderate | 4 (0.53) | "delighted" (tag, l.246); "comforted on my account" (l.214); "surprised at himself" (l.132); "liked himself for it" (l.58). **−0.25** |
| 11 | **Explanatory extension** | **FOUND strong, OVER THE CAP** | **8 (1.06/1k)** | (1) l.48 "**so that nobody should take the god's cakes for anybody else's**"; (2) l.52 "**which were plainly the only part of the morning that concerned him**"; (3) l.90 "**The god could be helped along.**"; (4) l.204 "moved the way a line moves when somebody at the front of it is being paid, **by fits, and in between not at all**" (a simile unpacked); (5) l.296 "**In that country nobody had yet said a thing to me that had a direction in it. I took hold of it the only way I knew.**" (the body rebel explained); (6) l.298 "**because it would not fit inside the line however the priest had pushed at it**"; (7) l.308 "**a Syracusan who wanted a western sea would have to cross the whole island to find one**" (added by continuity W-01); (8) l.416 "**where a man could see the whole climb of the street … and every gate along it**". Not counted: "having no other use for them" (l.206); "from which she could hear every word" (l.100); Mara's lecture in speech (l.342, which she hears herself give). **−0.50 and Prose capped at 7.5.** |
| 12 | Binary negation | FOUND minor | 1 (speech) | l.342 "It is not an address. It is a description of the empire." Narration 0. **−0.125** |
| 13 | Precision flex | FOUND minor | — | "four words" (l.14), "all four" (knuckles, l.48), "three steps", "six feet wide"; in speech "Forty-one jars", "Seven steps", "Fourteen years" (character). **−0.125** |
| 14 | Emotional control demonstration | Clear | — | Control is wrong ("almost calm") or fails ("I heard myself and kept on."). |
| 15 | Authoritative description | FOUND minor | — | The sunrise and the altar (l.38, l.78). Offsets: the word not kept, "or a photograph of one", Mara never sees inside. **−0.125** |
| 16 | Philosophical asides | FOUND minor | 2 (0.27) | Present-tense generalizations in narration: l.100 "the way a house does that has been loud for a week"; l.204 "the way a line moves when…". **−0.125** |
| 17 | Clean dialogue | FOUND moderate | — | B1's interview is strict Q&A ("Darker with what?" / "Their feet."; "What was it like?" / "Stone color,"). Offsets: Felix's stacks, "Try." / "It's gone,", Theano's run-on, the jug boy's message half-caught (l.412). **−0.25** |
| 18 | Thematic echo chamber | Clear | — | Texture present (see Theme). |
| 19 | Graduated reveal | Clear | — | Parallel. |
| 20 | Emotional temperature report | Clear | — | The cold is physical. |

**10 / 20 found (#1, #3, #8, #10, #11, #12, #13, #15, #16, #17). Total −2.0. Band: WATCH** (commercial 9–11). **#11 hard check: FAIL** (8 > 6 and 1.06 > 0.8): it caps Prose at 7.5. **After the PATH:** #11 is 2 at 0.27/1k (the Praxias gloss and "The god could be helped along.", both kept); #16 clears; the scan is **9/20 at −1.5**.

---

## The book's own laws
- **NO FORESHADOWING: PASS, 0.** The gate agrees, and so does a hand read of families A–E.
  - "Before the bowl's turn came I meant to be gone." and the imagined first hour home are present hope.
  - **Mara does not think of Vesuvius.** The Bay of Naples was cut (C-01). Her list is "Sicily after all, or Massalia, or Spain"; she reaches Etruria and stops.
  - **"Pompeii." lands with no reaction:** it is the last word, delivered while Theano "shifted on the stone, and grunted with it". ✓
  - The mountain rule is untouched (the mountain is not described).
- **Allowlist:**
  - "where the dead go out" is use 1 of 3, in Valens's repetition only ✓;
  - "painted on a dead man's house" is 1 (at-risk max 1) ✓;
  - "the seventh of Bysios" appears in the title only, with the body at 0 ✓.
  - Nothing points at the match between the written question and "the road home" ✓.
- **Memory only when the scene triggers it (CP2-2): PASS.** The slides (l.342) are triggered by the god's painted door, and they run straight back into her speech ("I said"). That is one longer memory, and Ch.11–12 had none. Its shape (an image projected, a parent clicking on) is new. No lost-name close.
- **Kneel / crouch (CP2-3): 0.** **Hand / chin on the knee: 2** (l.98 "going cold on his knee", l.366 "lifted an inch from his knee"), under the cap of 8. Theano's knees are her subject in speech, not stage business. ✓
- **Valens's bare "No.": 1** (l.312) ✓.
- **Explanation-density cap: FAIL** (#11 above).
- **NO TICS, gestures the gate cannot classify: FAIL.** The deliberation-pause class (9, cap 8) is listed under Characters. The other unclassified classes, by hand:
  - **exits by gait**: Felix "from the gate he ran" (l.338), the jug boy "off downhill at a run" (l.432) and Praxias "at a trot" (l.266). That is three against the bible's cap of 1 per 3 chapters.
  - **"at a run" ×3 in the chapter** (l.86, l.238, l.432), making 4 book-wide with Ch.10. The tic gate skips it because it is stop-word bounded.
  - **"watching the street" ×2 within 260 words** (l.418 Valens; l.428 the crows).
  - Felix "studying" ×2 (l.92, l.248).
  - The pills offered from a hidden palm, staged twice in one frame (l.60 / l.450).
  - "into his palm. He weighed the silver in his palm" (l.52).
- **NO TICS, verbal:** no catchphrase for anyone. Valens's "I told him [it / the goat] was hers" pair is designed.
- **No reuse of earlier phrases or set pieces: FAIL**, P2–P8 below. The echo gate is 0 by string; these are frames.
- **Retired reflexes:**
  - no define-by-negation opener;
  - no anaphora triad (the audit's three were fixed);
  - no performed candour, no aphorism, no scene button.
- **Bible at-risk items, checked one by one.**
  - **Clean:**
    - hinge 0; "So" 0; "before I had…" 0;
    - "the one / the only" 3 (at the cap);
    - "as if" 1; credential asides 0;
    - lying-awake coda 0; held silence measured by something moving 0;
    - teeth 0; laughs: walk-on only (the men clapping the husband);
    - English 0; cloth smells 0; Kallia sits 0; Kallia touches Mara 0;
    - "said/told the [non-listener]" 1 ("said Theano, to the crows");
    - the watch 0; the lens cap 0; the camera only as "a heavy thing from my bag" / "your father's silver thing";
    - a knot near Valens 0; Valens walk-offs 1;
    - narrated non-answers 0; the god's day and the Ch.11 paraphrases 0;
    - anadiplosis in narration ≤1;
    - paragraph-final negations in narration 4 (0.53/1k; the WATCH asked for ≤1.5) ✓.
  - **Breaches:** see P1–P9 and C1–C4 under Revision Recommendations.
- **Ledger row:** approach ✓, open ✓, end ✓, breaks ✓, dialogue ✓, theme ✓, gear ✓, length ✓ (inside the range). **Beat subversion ✓. Writer warnings:**
  - no riddling Theano ✓ (her register is a farmer's widow's);
  - no hint at the hour ✓;
  - no narratorial horror ✓;
  - the word-for-word recall shown once ✓;
  - "where the dead go out" once ✓.

---

## Character Chaos Check (Primary: Mara)
- **Irrelevant thought: PRESENT, inhabited.** The left-ears board (l.238), a 90-word wander broken by Felix going over the wall.
- **Cognitive distortion: PRESENT, inhabited.** She reads Valens's silence as "no road" and talks herself into calm with it: "By the lions I had it settled. I was almost calm." (l.284).
- **Unprompted memory: PRESENT, triggered** (the Tarquinia slide, l.342), and returned to the scene at once.
- **Failed emotional management: PRESENT.** The hair that "would not lie down again" (l.296); "I heard myself and kept on." (l.342).
- **Voice under pressure:** level 1, brief, at the recital (not a mapped rehearsal chapter).
- **4/4, mostly inhabited.** One mediated sentence ("I took hold of it the only way I knew.") explains the coping; the PATH removes it, and the chaos becomes fully inhabited.

## Secondary Character Chaos
- **Valens:** the one word he "didn't keep", and the hand that goes to the crust as he says so (l.174); he stands to recite when nobody asked; he sends Felix off when Capua is named.
- **Felix:** "My mother could have told them that." He stopped, surprised at himself (l.132); his ears; he grabs a stranger's cloak.
- **Kallia:** spits at a death; her first thought is the hairdresser.
- **Theano:** the branded barley and the lie; "A thing that'll sit quiet at a burying can have my barley."
- **Praxias:** his fingers stroke the absent quail.
- No secondary character is a mere function. No cap.

---

## The Tomorrow Test
**What the reader remembers:**
- A gladiator standing in the middle of a courtyard with his hands open, saying the god's answer in one breath "in a voice that was new to me". Asked for only the middle part, he cannot begin there: "You don't go in at the fourth."
- Then an old woman on a stone at her door, throwing the god's barley to the crows, complaining about her knees and a stool. Asked "Which city?", she says one word: "Pompeii."

**Anchor type:** BOTH.
- IMAGE: the recital; the goat shaking off the jar; the left-ears board; the crows and the branded basket.
- QUOTE: "It took a jar."; "Yours stood."; "put shoes on it"; "Pompeii."

**Verdict: ANCHOR EXISTS** (strong; +0.5 CVI). **Type check:** Ch.11's anchor was an animal's stillness and Ch.12's an object in motion. Ch.13's is a body held still to carry words, plus a one-word reveal. New to the book.

## The Shareability Test
"The Oracle won't let women in, so the ex-gladiator carries her question in and comes out with the answer memorized like a sword drill. He can't even start it from the middle. Then the actual Pythia, an old widow with bad knees, calls her over to complain about the priests and tells her the door home is in POMPEII." Running total: 13 chapters, 23+ shareable moments.

---

## Reader Reports

### The Devourer (7.5k after Ch.12's 4.7k)
- **Speeds up:**
  - the goat ("It took a jar.");
  - Felix in the god's book;
  - "Stone color";
  - the false alarm;
  - "He goes like this when a mule dies";
  - the recital;
  - every line of Theano.
- **Slows:**
  - the retelling at the spring ("I just read this") (l.8–l.14);
  - the terrace wait: the well-woman, the bowl summons, the ears (l.204–l.238);
  - "the line moved the way a line moves…".
- **Would they stop?** No. The interview withholds the answer, A2 shows Valens coming out silent, and the reader has to get back to the court.
- **Last page:** they turn it at a sprint.
- **Vibes:** "the goat and the old lady."

### The Critic
**Underlines:**
- "I left out his hands, which were his.";
- "like the inside of a stone";
- "two folded pancakes";
- "The god could be helped along. It took a jar.";
- "the most famous stone in the world had reached me as a man with a cough standing next to it";
- "He said a chair was a chair.";
- "a bus ticket with the town torn off";
- "Where a board by the road says it does";
- "laid open like cupboards";
- "as flat as a price for a lame ewe";
- "they take it and put shoes on it";
- "**Yours stood.**";
- "Nothing in it was the god's."

**Disappointments:**
- "*the way a line moves when*, a present-tense maxim, and then it explains itself" (F2);
- "*In that country nobody had yet said a thing to me…*, Ch.7's sentence again" (F3);
- "the Etna sentence argues past its point" (F5);
- "*He considered*, three times" (C1–C3);
- "*the way you'd read anything out*: Valens compares?" (V1);
- "*little—*: a joke on Ch.11's 'little cousin'" (V12).

### The Hostile
1. **A classicist whose father ran a Campanian survey** hears "the mountain of vines by the western sea … where the dead go out of the city … a door painted on a dead man's house". She lists Etruria, Sicily, Massalia and Spain, and never Campania. This is required by law (Ch.14 is the night she knows), and the page does not wink. **Not a hole: a blind spot Ch.14 can own** (audit I-29).
2. **Valens, who keeps everything word for word, "didn't keep" the one word.** "It's gone," and his hand goes to the crust (l.174–l.182). Is he hiding it? The page leaves it open. That is a strength, provided Ch.15 does not have to explain it.
3. **The pills.** She offers them to Valens, he says "After", and she gives them to Theano without a thought for his shoulders. A payment, as the outline says, but it reads as a small unexplained choice. No change.
4. **The fantasy of home** is in summer, yet she turns the heat on (l.224). This is a cold woman's wish on a frosty wall; logic-minded readers may notice. No change.
5. **How does Theano know "the woman that asked about a road"** and where to send? The question is read aloud at the screen (l.162), and the registrar's wax says "of the house of Kallia" (l.114). ✓

**Verdict:** "No hole; one blind spot by design."

### The Casual Reader (airport, 10 pages)
- **The first page is quieter than Ch.12's:** frost, jars, priests, a retelling.
- **Pulled in by:** the crowd and Felix's boxer; then the goat, which makes them laugh. "Stone color" makes them laugh again.
- **Gets goosebumps at:** the standing recital.
- **Loves Theano.**
- **The last word lands like a dropped plate:** they know what Pompeii means even if they know nothing else about Rome.
- **Frictions:** the name soup on the terrace (Thessalians, Achaeans, Locrians, Coans); the retelling at the spring; the line and bowl business in A2.
- **Would they buy after 3 pages?** Yes, on the strength of the book so far. **Do they stay?** Yes, and they would tell a friend the oracle said Pompeii. **9.0/10.**
- **Not 9.5:** the first two pages are slow, and A2 is a waiting room.

### The Devoted Reader (active: long saga)
**Will post about:**
- Plutarch's drench and the over-drenching anecdote;
- Pindar's iron chair;
- the omphalos *agrenon*;
- three Pythias becoming one;
- the hexameter with the priest's hand in it;
- the Tomb of the Augurs' painted door and mourners;
- left-ear votives;
- the word "not Greek, so not the god's" being Pompeii;
- Felix's "What if it's Italy?";
- Kallia's "The boats go west at the new moon."

**Will catch:**
- the Ch.7 "in that country … said … in it" sentence (F3);
- the third boy introduced as age-plus-tunic (V8);
- Kallia's spit into her dress, the goat-boy's gesture from Ch.4 (WATCH);
- the reserved sample line "a painted door" (V9, invisible to the public but a law item).

---

## Cross-Reader Matrix
| Issue | Devourer | Critic | Hostile | Casual | Devoted | Severity |
|---|---|---|---|---|---|---|
| F1–F6 #11 over the cap (8 at 1.06/1k) | ✓ (the line) | ✓ | | | ✓ | **SHOULD FIX → blocking** (hard cap) |
| C1–C4 deliberation-pause class at 9 (cap 8) | | ✓ | | | ✓ | **SHOULD FIX → blocking** (gesture cap) |
| P1 present-tense generalizations (l.100, l.204) | ✓ | ✓ | | | | **SHOULD FIX → blocking** (voice-dna §0.4) |
| P2 Ch.7 frame "in that country … said … in it" (l.296) | | ✓ | | | ✓ | **SHOULD FIX → blocking** |
| P3–P8 fourth command echo, Valens comparison, group tags, gait exits / "at a run", boy skeleton, "little—", sample-07 3-gram | | ✓ | | | ✓ | **SHOULD FIX → blocking** (law items) |
| P9 in-chapter doubles (watching the street, studying, palm, the pills' frame, Praxias's gaze inventory) | | ✓ | | | | INVESTIGATE → recommended |
| The retelling at the spring; A2's wait | ✓ | | | ✓ | | SHOULD FIX → **no change** (the retelling pays Ch.12's "She gets the whole of it from me"; A2 carries the misreading that sets up the surprise) |
| Terrace name soup | | | | ✓ | | VIBES (IMPORTANT by rule) → **no change in this cycle**: every ethnonym is load-bearing for the queue-by-city procedure. WATCH: Ch.16's Corinth crowd must not catalogue peoples. |
| The Campania blind spot | | | ✓ | | ✓ | INVESTIGATE → no change (law); Ch.14 may own it |

---

## Revision Recommendations (Ranked)
*Every string below was applied together to a scratch copy and run through `check_chapter.sh 13`, `shape_check --strict`, `voice_wear_check.py` and `tic_report.py --gate`: all clean, echo 0, no new 3-gram against the samples. Earlier versions of my strings that tripped a gate are listed under "Do not use".*

| # | Location | Problem type | What happens now | Why it fails | Revision direction | Project rule? |
|---|---|---|---|---|---|---|
| F1 | l.48 | Style (#11) | "on trays with a laurel leaf burned into the wood of the rim so that nobody should take the god's cakes for anybody else's." | The brand explains itself. Theano's basket (l.432) and "a grain of his" make the link without it. | → "…burned into the wood of the rim, **and the stall-keeper sucking his fingers between sales.**" (−3) | No |
| F2 | l.204 | Style (#11) + Voice (§0.4) | "moved the way a line moves when somebody at the front of it is being paid, by fits, and in between not at all." | A simile unpacked by its own tail, and in the narrating present. | → "The line at the foot of the ramp moved by fits, and in between not at all, **and those who had stood in it since first light began on the corners of their cakes.**" (+3; bodily realism punctures the queue) | Yes: "present-tense generalization in narration (`the way an? \w+ (does\|moves\|is)`) = defect" |
| F3 | l.296 | Style (#11) + reused frame | "In that country nobody had yet said a thing to me that had a direction in it. I took hold of it the only way I knew." | It explains the body rebel (mediated chaos). It rebuilds Ch.7 l.356 ("the only thing in that whole country that had ever said I was in it"). It is also a "the only" claim at the cap. | → "**I looked where he had been looking, and the wall was bare but for a lizard, flat in the sun with its toes spread.**" (−3). An inhabited irrelevance at the peak; "It scanned." then turns to analysis unannounced. | No |
| F4 | l.298 | Style (#11) | "and the last part had been left to hang off the end because it would not fit inside the line however the priest had pushed at it." | "because…" completes the thought the image already gives. | → "and the last part **hung off the end of it like a suitcase roped onto the roof of a car that was already full.**" (−2; a characterizing 1998 comparison, new vehicle) | No |
| F5 | l.308 | Style (#11, repair-added) | "the one Syracuse looked out on; a Syracusan who wanted a western sea would have to cross the whole island to find one." | Continuity W-01 added an argument clause. | → "the one Syracuse looked out on, **and the god, in the priest's verse, had said west.**" (−7) | Yes (restated): "an additive repair recomputes #11 density" |
| F6 | l.416 | Style (#11) | "There he set his shoulders to the wall, where a man could see the whole climb of the street…" | It explains his vantage. | → "There he set his shoulders to the wall **with the whole climb of the street in front of him,** to the head of the town and every gate along it;" (0) | No |
| C1 | l.64 | Character (gesture class) | "He considered the two small white things in my palm." | Deliberation pause, Valens #1 of 4. | → "**He did not touch the two small white things in my palm.**" (+1) | Yes: add a *deliberation pause* class to `tic_report.py` (`considered (it\|that\|me\|him\|her\|the)`, `gave \w+ some thought`, `thought about (it\|that)`, `took (him\|her) a while`, `stood with that`, `(He\|She) thought\.`) |
| C2 | l.232 | Character (gesture class) | "He considered me, and the wall, and the women round me, who were all listening." | Pause beat (the slave). | → "**He had a look at me, and at the women round me,** who were all listening." (+1) | No |
| C3 | l.328 | Character (gesture class) | "He considered that. "Where does the town stop, then?"" | Valens pause #3; the line needs no wind-up. | Cut "He considered that." (−3) | No |
| C4 | l.280 | Character (gesture class) | ""Not this year." He thought about it. "Not that he's told me."" | Felix pause (his third, with l.124 and l.254). | → ""Not this year. Not that he's told me."" (−4) | No |
| P1 | l.100 | Voice (§0.4 narrating present) | "the house had gone quiet the way a house does that has been loud for a week," | A general present-tense reflection in narration. | → "the house had gone quiet, **after a week of being loud,**" (−6). "as quiet as it had been" trips voice-wear. | (with F2) |
| P3 | l.440 | Style (command echo, SPENT at 3) | "Sit down; my neck won't go back that far…" / "She watched me sit on her doorstep" | A fourth "order → the order's word as her act". The gate's detector misses it across the quote. | → "She **waited until I was on** her doorstep, below her," (+1). Compliance by result. | No |
| P4 | l.162 | Voice (Valens card) | "He reads the question off the wax, at the screen, the way you'd read anything out." | A comparison in Valens's speech; his card's distinctness guarantee is that he never compares. | → "…at the screen, **in an ordinary voice.**" (−2) | No |
| P5 | l.246 | Style (cap 1/ch) | "said the friend beside him, delighted, to all of us." | A second group-address tag after "told the terrace" (l.88). | → "…delighted, **with an arm round his neck.**" (+2) | No |
| P6a | l.432 | Style (gait exit; "at a run" 4 book-wide) | "and was off downhill at a run, glad to." | Exits by gait are capped at 1 per 3 chapters (Felix's l.338 is the keeper). | → "and was off downhill, glad to." (−3) | Yes: "`at a run` and gait-exits counted by hand until gated" |
| P6b | l.238 | Style ("at a run") | "when Felix vaulted the wall beside me at a run." | The third "at a run" in the chapter. | → "when Felix vaulted the wall beside me." (−3) | No |
| P6c | l.266 | Style (gait exit) | "Praxias had gone off up past the theater at a trot toward the stadium and the quail ring, without stopping." | A reported exit by gait. | → "…toward the stadium and the quail ring **with his wreath still on.**" (0; against Valens's "wreath in his hand" in the next sentence) | No |
| P7 | l.400 | Character / Style (introductions travel) | "He was ten or so, in a white tunic too long for him, with a cloth-covered basket…" | Age-hedge plus tunic is the third boy built so (Ch.4 the goat-boy, Ch.11 Felix). Bible after Ch.11. | → "**The front of his white tunic was dark with spilled water,** and he had a cloth-covered basket hooked over one arm; he stopped at the gatepost." (−2) | No |
| P8a | l.58 | Voice (a line landing again) | ""Next month. And you pay me again, little—" He stopped himself, and liked himself for it. "Syracusan."" | The beat depends on Ch.11's capped "little cousin" landing again (voice-dna §3b.3). | → ""Next month. And you pay me again, Syracusan," he said, and liked the sound of that." (−2; em-dashes 2 → 1) | No |
| P8b | l.350 | Style (sample-07, reserved Ch.42; at-risk "painted door") | "find a painted door every other mile." | "a painted door" is sample-07's 3-gram, and this is the chapter's second "painted door". | → "find **a plaster door** every other mile." (0; the bible's own variant) | No |
| R1 | l.428 | Style (in-chapter 2nd use) | "hunched against the cold, watching the street." | l.418 "watching the street above", 260 words earlier. | → "hunched against the cold, **beaks to the wind.**" (+1) | No |
| R2 | l.248 | Style (in-chapter 2nd use) | "studying the sky." | l.92 "studying his hands" (Felix both times). | → "**admiring** the sky." (0) | No |
| R3 | l.450 | Style (in-chapter frame doubled) | "I shook the two pills out of it, under my himation, and offered them to her on my palm." | l.60 stages the same hidden-palm offer. | → "I shook the two pills out of it **and held them up to her where she sat on her husband's stone.**" (+2) | No |
| R4 | l.52 | Style (the item-by-item gaze) | "He glanced on at Valens's face, the crust on it and the bruise below it, and back at the coins," | A gaze moving item to item over a body (the closed frame of Ch.12 audit C-01). Also "into his palm. He weighed the silver in his palm". | → "He glanced at **what the road had done to Valens**, and back at the coins," (−4) and "into his **hand**. He weighed the silver in his palm" (0) | No |
| O1 | l.296 | Style (optional) | "to the shoulder" | The to-the-joint depth frame is closed as a frame (under its regex cap). | Cut (−3). **Not in the tested set:** it would take the chapter to 7,505. | No |
| O2 | l.38 | Style (optional) | "until the wind off the gorge found it" | Sample-01's "the wind off the valley" frame (3-gram). | → "until a draught up from the gorge found it" (+1). Untested. | No |

### Fix order: Character (C1–C4, P7) → #11 (F1–F6) → Voice law (P1, P3, P4, P8) → Style law (P5, P6, R1–R4) → optional (O1, O2)

**Kept on purpose:**
- the two remaining #11 instances ("which were plainly the only part of the morning that concerned him"; "The god could be helped along.");
- "He thought." (l.170), "Felix stood with that.", "gave him some thought", "He was quiet for three steps.", "That took him a while". That leaves 5 in the class, spread across four speakers, with no cluster;
- the altar boy's "went at a run" (book-wide "at a run" is then 2);
- Kallia's spit (l.14). This is the apotropaic gesture the goat-boy made in Ch.4: a period custom, two uses, different people and triggers. **CLOSED: no third.**

---

## Strengths to PRESERVE (do not touch in polish)
1. **The first sentence, byte-identical**, and "Down at the lions it was Kallia and me, and the cold, and the long noise of the water."
2. **The spring:** "I left out his hands, which were his."; the spit; "Five hundred," very low; the hairdresser question and "Sold on, or sent out to his farm."
3. **The drench (l.78–l.90), every beat:** "One ear flicked. That was all."; Praxias "telling the nearest man that he had said so"; the full jar "in one long cold sheet"; **"It took a jar."**
4. **B1 entire** (apart from P4): "He put his nose a hand from mine"; "I gave him Felix."; "Small." and the ears; "My mother could have told them that."; "Their feet."; "There's one door. I looked for another."; "He said a chair was a chair."; "Stone color,"; the cough; **"I didn't keep it." / "Try." / "It's gone,"**; the raised hand; "I told him the goat was hers."
5. **A2's spine:** the well-woman ("I'll dig it at night…"); the ears; the false alarm and "I'm a Phocian,"; "It wasn't a stone, was it?" / "It was heavy,"; "like something borrowed"; "He goes like this when a mule dies,"; **"By the lions I had it settled. I was almost calm."**
6. **The recital (l.288–l.294), byte-identical.** The answer string is the allowlisted and at-risk text.
7. **B2:** Kallia's "Somebody was paid to paint that door."; the priest's Syracuse; "Where does the town stop, then?" / "**Where a board by the road says it does,**"; Felix's Italy; the slides; "It is not an address."; the forms; "a bus ticket with the town torn off"; "Mine's written. At Corinth."; "**There's floor,**".
8. **Theano entire** (apart from P3 and R3), and **the last line byte-identical: "Pompeii."**

---

## PATH TO 8.5 (mandatory; the Floor is 7.5)

**Characters 7.5 → 8.5 requires:**
- the deliberation-pause class taken well under the gate's cap (C1–C4: 9 → 5, Valens 4 → 2);
- the boy introduction made fresh (P7).

The merit evidence (Valens's recital, Kallia's hairdresser, Theano's card, cover-the-name, 4/4 chaos) is already there. **C1** is the most visible: Valens's refusal of the pills becomes a refusal by the hands, not a pause.

**Prose & Voice 7.5 → 8.5 requires:**
- #11 under the cap: F1–F6, which takes it from 8 to 2 (0.27/1k);
- the law cluster cleared: P1, P3–P8;
- the in-chapter doubles cleared: R1–R4.

The stopping sentences (l.466, l.90, l.158, l.12, l.374, l.448) and the ugly sentence stay. **F3** is the single highest-value cut. It removes a Ch.7 rebuild, an explanation and a "the only", and it turns the recital's body rebel from mediated to inhabited.

**Apply in this order; the strings are exact (see the table):** C1, C2, C3, C4 → P7 → F1, F2, F3, F4, F5, F6 → P1, P3, P4, P8a, P8b → P5, P6a, P6b, P6c → R1, R2, R3, R4 (both halves). Then run `bash books/the-hour-of-ash/tools/check_chapter.sh 13` and `python3 tools/shape_check.py books/the-hour-of-ash --strict` from /home/user/Books. Also update the chapter's word-count HTML comment (l.4).

**What the tested run produced (every item above except O1/O2, applied together):**

| Measure | Before | After |
|---|---|---|
| Words (shape_check) | 7,541 | **7,508** (≥ 7,500 ✓) |
| Words (style_check) | 7,559 | 7,527 |
| Dialogue | 37.9% | **38.1%** (35–45 ✓) |
| Median sentence | 14 | **14** (gear mid ✓) |
| Breaks / signatures | 4 / `scene-set` → `dialogue` | unchanged |
| First and last lines | | byte-identical |
| `check_chapter.sh 13` | clean | **all clean**: style (simile 2.1/1k, em-dash 1, foreshadow 0), grammar 0, rhythm 0, show/tell no flags, voice-wear strict clean, tic gate clean (and-chains 5/9), echo 0, command echo none, metaphor 2.7/1k |
| `shape_check --strict` | CLEAN | **CLEAN** |
| #11 | 8 (1.06/1k) | **2 (0.27/1k)** |
| Deliberation-pause class | 9 | **5** |
| "at a run" (book-wide) | 4 | **2** |
| Gait exits | 3 | **1** |
| "the only" claims | 3 | **2** |
| Em-dashes | 2 | **1** |
| Anti-AI | 10/20, −2.0 | **9/20, −1.5** |

**Expected:** Characters 8.5 (cap lifted to merit), Prose 8.5 (merit 8.0 → 8.5 on 25 cited changes; the +0.5 limit applied to the merit score, as in Ch.10 and Ch.12) → **Floor 8.5, Average 8.79** (9.0 / 8.5 / 8.5 / 8.5 / 9.0 / 9.0 / 9.0). Casual 9.0 holds.

**Do not use** (each tripped a gate on my first try):
- "men who had" (tic gate: 3× book-wide);
- "there was nothing" (tic gate);
- "as quiet as it had been" (voice-wear);
- "nothing on it but" (voice-wear);
- "to Valens's face and" (echo, Ch.12);
- "and the boy ran" (echo, Ch.11);
- "he looked from" (echo, Ch.6);
- "in the priest's own" (an in-chapter 4-gram with Felix's "In the priest's own writing?");
- "slopped" (5 uses in Ch.5–6);
- "between one sale and the next" (it turned F1 into an and-chain).

**Do not touch:** the recital string, the first sentence, "Pompeii.", the drench, or B1's interview order.

---

## Pacing check (one line for `feedback/progress.md`)
Ch.13 (cycle 0) · Parallel *outside / inside* between Ch.12 In medias res and Ch.14 Fragmented ✓.
- **Length:** 7,541w (target 8,000, −5.7%, inside the 7,500–8,500 range; after the PATH ≈7,508).
- **Book:** 72,162 vs 77,600 cumulative (−7.0%); the 220k floor is safe.
- **Dialogue** 37.9% (35–45 ✓; 38.1% after the PATH); **4 breaks** ✓.
- **Gear mid, median 14** ✓, back up from Ch.12's low 10, as planned. Neighbours: Ch.11 mid 14 at 38%; Ch.12 low 10 at 28%.
- **Signatures:** `scene-set` / `dialogue`, and no three running (Ch.11 `dialogue`, Ch.12 `punch`).
- **Emotional slot ✓:** after Ch.12's crucible (shock → tenderness), a ritual day of suspense. She misreads "no road" and goes calm, a road is given, then the WHERE lands at about 28% of the plan (the outline's ~30% turn).
- **Speed:** the ritual slow, the interview measured, the wait jolted by the false alarm, the recital stopped, Theano quick.
- **Value shift** −/+/−/+ ✓; pull 10; hinge 0; the peak is not a laugh.
- **Slow patches:** the spring recap and A2's middle. Both are load-bearing; no cut.

**Verdict: OK.**

---

## Cross-Book Pattern Detection (Ch.1–13)
1. **Repairs add explanation, for the third time** (Ch.10, Ch.12, Ch.13). Continuity W-01 turned Etna into a 17-word argument clause. The rule "an additive repair recomputes #11" is already written; it is not yet being run. **Pipeline:** `tic_report.py` (or `style_check`) should compute an #11 proxy (`\b(so that|because|which (was\|were) plainly)\b` and `the way an? \w+ (does\|moves)` in narration) and print it per chapter, so the editor sees the density move.
2. **Stage business moves to the classes the gate does not model.** Knees were gated after this chapter's draft (12 → 2). The same chapter then grew a deliberation-pause class (9) and "at a run" gait exits. **Pipeline (UPDATE RULE, root):**
   - add `deliberation pause` (the regex in C1) to `GESTURE_CLASSES`;
   - add `exit by gait` (`\b(at a (run\|trot\|walk)\|from the gate he ran\|was off (downhill\|uphill))\b`).
3. **Narrator frames recur from five or six chapters back, not only from the previous one.** Ch.7's "in that country … said … in it" and the Ch.4 / Ch.11 boy introduction both slipped through. Ch.12's lesson ("list the previous chapter's narrator frames") needs widening: **grep the anchor lines of every finished chapter** (the bible lists them), not only the last one.
4. **Valens's card held almost everywhere.** One comparison slipped into reported procedure, where explanation tempts a comparison. WATCH his reports in Ch.17 and Ch.22, which are the same kind of speech.
5. **What varies, as it should:**
   - the structure (Parallel, the book's first);
   - the opening (`scene-set`) and the ending (`dialogue`);
   - the gear (back to mid);
   - the anchor type (a recitation, new);
   - the body-rebel channel (hair; Felix's ears);
   - the peak (a single word, not a laugh).

   Shape audit CLEAN; the ledger row is honored on every hard field.

**Bookkeeping (orchestrator):**
- **Re-sync the bible's Ch.13 blocks to the final page** (continuity W-21 is still pending). The Valens Ch.13 block quotes strings that are not on the page:
  - "like something another man had put there for a bet";
  - "Keep to this wall.";
  - "One. The way in's the way out.";
  - "in a voice that was not his road voice";
  - "There was no answer to that in my Greek.";
  - "Valens kept his eyes off me, and I kept mine off him.";
  - "that hand's knuckles had scabbed over in a row".
- **Theano card:** amend "never explains" to "explains herself once, about the crows; never the god or the hour" (W-13(a)).
- **At-risk after Ch.13, add:**
  - deliberation-pause class (Ch.13 5 after the PATH; ≤3 per chapter; Valens ≤1);
  - exits by gait (Felix's l.338 is the Ch.13–15 allowance);
  - "at a run" 2 book-wide, CLOSED;
  - Kallia's spit into her dress (2 with Ch.4), CLOSED;
  - the "in that country … said … in it" frame (Ch.7, Ch.13 draft), CLOSED;
  - present-tense "the way a X does" generalizations: 0;
  - the hidden-palm offer: once;
  - the item-by-item gaze over a body: still CLOSED (R4);
  - "a lizard … toes spread" and "a suitcase roped onto the roof of a car": once each, after the PATH.
- **ENTITY:** the ibuprofen is used up, Ch.13 (audit patch).

---

## VERDICT
**POLISH. Gate NOT MET.**

| Measure | Result |
|---|---|
| Genesis Floor | **7.5** (Characters and Prose & Voice, both capped) |
| Average | **8.50** |
| Casual | **9.0** |
| Pacing | **OK** |
| CVI-Launch (CVI-L) | **9.8** |
| CVI-Legacy | 6.8 (provisional) |
| Mechanical suite | all clean (echo 0, tic gate clean, voice-wear strict clean, shape CLEAN) |
| Foreshadowing / Vesuvius / reaction to "Pompeii." | **0 / 0 / none** ✓ |
| Memory triggered by the scene (CP2-2) | ✓ |
| Kneel / crouch (CP2-3) · hand / chin on the knee | 0 · 2 (cap 8) ✓ |
| Valens's bare "No." | 1 ✓ |
| Explanation-density cap | **FAIL** (8 at 1.06/1k) → PASS after the PATH (2 at 0.27/1k) |
| Tics | verbal 0; gate classes clean; **deliberation-pause class 9 ≥ cap 8: FAIL** → 5 after the PATH |
| Reuse of earlier phrases / set pieces | **FAIL** (P2 frame, P7 skeleton, P8 callback / sample) → cleared |
| Ledger | ✓ on every hard field |
| AI patterns | 10/20 (watch band) → 9/20 |

**Failing dimensions:** Characters (7.5) and Prose & Voice (7.5). The fixes are surgical and were tested together: C1–C4, P7, F1–F6, P1, P3–P8, R1–R4 (25 strings). The result is 7,508 words, dialogue 38.1%, median 14, every gate clean, and the first and last lines unchanged. Then run E (gates) and F (re-evaluation). **Expected after one cycle: Floor 8.5 / Average 8.79 / Casual 9.0 / PASS.**

Every reader has been waiting for this chapter since the map, and it delivers. The goat has to be drenched until she shakes. The gladiator comes out with the god's words held like a sword drill and cannot start them from the middle. The precise answer comes from an old widow on her husband's stone, between complaints about a stool. What holds it below the gate is the narrator explaining eight things the scene already shows, and a cast that keeps pausing to think before it speaks.

**BIAS CHECK:** This evaluation was produced by the same system that wrote the prose. Confidence in scores above 8.0 requires external validation (beta readers, editors, comp analysis).
- **The #11 count is a judgment.** Six instances are firm. Two (l.52 Praxias's gloss; l.90 "The god could be helped along.") are clauses a lenient reader would call wit, and with those uncounted the chapter sits exactly at the cap (6, 0.80/1k). I counted all eight by the standard that counted Ch.10's Armada and Ch.12's "Hot would have set it." The PATH clears it either way.
- **The deliberation-pause class is my classification, not the gate's.** I used the gate's own number: cap = max(4, words/1000) = 8, and reaching it fails. A reader who left out "Felix stood with that" and "He was quiet for three steps" would count 7, one under the cap. In that case Characters would rest on its merit (8.5) and Prose alone would hold the floor.
- Originality 9.0, Pacing / Emotion / Immersion 9.0, Casual 9.0 and CVI-Launch 9.8 are one-chapter judgments by the system that wrote the book.

---

## Polish cycle 1 applied (book-editor, 2026-10-20)

**Applied from the fix table, as written (24 strings):** C1, C2, C3, C4; P7; F1, F2, F4, F5, F6; P1, P3, P4, P5, P6a, P6b, P6c, P8a, P8b; R1, R2, R3, R4 (both halves).
- **P6c:** the "with his wreath still on" swap also drops "at a trot" (that is how the table's 0-word delta works out, and it takes the gait exit off).

**Applied with one word changed:**
- **F3:** "with its toes spread" became "with its toes **splayed**". Ch.8 l.252 already has the women's feet "with their toes spread" at the fire, so the table's string would have repeated a frame across chapters. "splayed" is used once in the book.

**Optional items:**
- **O2 applied, reworded:** "until a draught **from** the gorge found it" (0 words). The table's "a draught up from the gorge" made "up from the" 3× book-wide (Ch.1, Ch.8, Ch.13), which fails the tic gate.
- **O1 not applied:** cutting "to the shoulder" leaves "under the wool, and", a 4-gram echo with Ch.7.

**ENTITY CH13-4 (almonds):** Ch.9 l.266 has Mara see them come into flower, so the line no longer says she missed it. "the almonds had flowered on the terraces, white, every tree together, without my seeing it," → "the almonds on the terraces were all in full flower now, white, every tree together," (15 words → 15). I tried two other wordings first and rejected both: "to the gorge" doubled "gorge" with l.38, and "down the slope" made the phrase 3× book-wide (Ch.4, Ch.5).

**Not used:** nothing from "Do not use".

**Measured after (shape_check / check_chapter.sh 13):**

| Measure | Result |
|---|---|
| Words | 7,508 (shape_check), 7,527 (style_check) |
| Dialogue | 38.0% |
| Median sentence | 14 |
| Breaks / signatures | 4 / `scene-set` → `dialogue` |
| First line and final beat | byte-identical |
| Mechanical gates | **ALL clean**: style (simile 2.1/1k, em-dash 1, foreshadow 0), grammar 0, rhythm 0, show/tell no flags, voice-wear strict clean, tic gate clean (and-chains 5/9), echo 0, command echo none, metaphor fig 2.7/1k, shape CLEAN (`--strict` too) |

**Gesture classes in Ch.13 (the gate's regex):**
- deliberation pause **3** ("stood with that", "He thought.", "took him a while"), cap 7–8. Valens has 2. The evaluator's hand count, which also takes in "gave him some thought" and "He was quiet for three steps", is 5.
- exit by gait **1** (the altar boy "went at a run", the keeper).
- hand / chin on the knee 2; kneel / crouch 0; bend / stoop 0.

**Other checks:**
- Valens's bare "No." 1.
- #11 by the evaluator's list: 2 remain, both kept on purpose.
- No new rationale clauses.
- Bible, STATE.yaml and ENTITY_STATE.yaml untouched. The bible's at-risk line for "a lizard … toes spread" should read "toes splayed" when the orchestrator re-syncs it.
- Pre-polish backup: `/tmp/claude-0/-home-user/63791ee5-159c-5791-9429-07920f8d9417/scratchpad/ch13-pre-polish1.md` (sha256 e88b4969…).

**Next:** run F again (re-evaluation).
