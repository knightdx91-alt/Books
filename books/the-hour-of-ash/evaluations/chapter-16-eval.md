# Evaluation: Chapter 16 — Plautia (run 2)
**Evaluator:** book-evaluator (independent; did not write or revise this prose) | **Date:** 2026-10-21
**Text evaluated:** `manuscript/chapters/chapter-16.md` (sha256 `a7783a01…`, md5 `8a386d98…`), after writer → dialogue-polish → hook-craft → disruptor → continuity repair (C-02, C-03, W-01…W-13), plus the AUTHOR-CP3-5 plan line ("At the games for Titus's triumph"). **7,540 prose words** (shape_check), 7,546 (style_check), 8,195 (`wc -w`, with the header). The brief's 7,536 predates the CP3-5 line, which added four words.

**Read against:**
- the book's CLAUDE.md hard gates;
- STATE.yaml guardrails and resolved_author_decisions, especially:
  - **AUTHOR-CP3-5**: a one-off festival on the Isthmus for Titus's triumph, never "the Isthmia";
  - **AUTHOR-CP3-3**: the pregnancy gap stays unremarked;
  - ARCH-5 (the suit in Rome, AD 74), ARCH-14 (Marcus 7 in Ch.16), ARCH-15;
- voice-dna §0, §1, §3, §3b, §4, §6;
- character-bible.md:
  - the MARA, VALENS, KALLIA, FELIX, PLAUTIA, MYRRHINE and MARCUS cards, and the Ch.16 walk-on note;
  - **every at-risk and spent block**, from "after Ch.1" to "after Ch.16", read in full;
- outline `## Chapter 16` and Ledger row 16;
- `evaluations/chapter-15-eval.md` (cycle 0, cycle 1, finalize);
- chapters 14 and 15 in full for pacing;
- `evaluations/continuity/chapter-16-audit.md` (what was applied, and which INFO items were left).

**Genre profile:** commercial historical romance / time-slip, comp *Outlander*.
- Anti-AI band: commercial (0–8 clean, 9–11 watch).
- Engagement: empathy 55 / fascination 30 / self-insertion 15.
- Dimension 7 = **IMMERSION**.

**Measured here.** `bash books/the-hour-of-ash/tools/check_chapter.sh 16` is **clean on every gate**:
- style: simile 1.1/1k, em-dash 3, foreshadow 0;
- grammar: 0 errors;
- rhythm: 0;
- show/tell: no flags, dialogue 44.3%;
- voice-wear: strict clean;
- tic gate: clean (and-chains 5/9, credential asides 1, negation pivots 0, "So" 0); gesture classes all under cap;
- echo: 0; command echo: none;
- metaphor: 1.5 fig/1k, median 15 (shape_check median 14);
- `shape_check --strict`: `16 7540 6 44 14 dialogue question`, CLEAN.

**My own scans (scratch, not gates):**
- 4–6-grams against Ch.1–15 and all 13 samples, **including stop-word-bounded strings** the echo scan skips;
- content 3-grams against Ch.1–15 and the samples;
- **every whole spoken sentence of five words or fewer**, checked against every earlier chapter's speech;
- by hand: #11 explanatory extensions, paragraph-final negations, pause and posture beats the gesture layer cannot classify;
- every SPENT / CLOSED item in the bible, grepped by frame as well as by string.

**The fix set was tested together on a scratch copy.** I swapped it into the manuscript path and ran the real `check_chapter.sh 16`, `shape_check --strict` and `tic_report.py --gate` from /home/user/Books. Then I restored the original and verified its checksum after every run (sha256 `a7783a01…`, md5 `8a386d98…`). I did not edit the manuscript.

*(l.N = line number in the current `chapter-16.md`.)*

---

## HEADLINE
**CVI-Launch (CVI-L):** 9.7 (9.24 base + 0.5 strong anchor) | **CVI-Legacy:** 6.9 (provisional) | **Genesis Floor:** **8.0** | **Genesis Average:** **8.71**
**Casual Reader:** **9.0**

**Engagement type:**
- **Empathy** leads: a mother who gives away whatever anyone admires, because everything she had was taken.
- **Fascination** is second: a Roman divorce suit, a magistrate's book of boards, a heist planned around a festival.
- **Self-insertion** is tertiary: Mara's jealousy, which every reader has felt about a partner's past.

**Divergence alert:** none (9.7 − 8.0 = 1.7).

**Gate (Floor ≥ 8.5 AND Casual ≥ 8.5 AND pacing OK AND gates clean): NOT MET.**
- Casual 9.0 ✓; pacing OK ✓; gates clean ✓.
- **One dimension holds the floor: Prose & Voice 8.0, on merit, with no cap.** The sentences are 8.5-plus. What holds them is the book-law cluster below, which no gate sees:
  - **An earlier chapter's delivery frame, used four times.** Ch.5 has the herald's "every word set down by itself and every ending given its full weight"; Ch.6 has Valens's "every ending in its place, a man setting things down one by one". Ch.16 rebuilds that frame at l.33, l.35, l.539 and l.587.
  - **Two whole spoken lines from earlier chapters.**
    - "She does that." (l.307, Valens) is Kallia's Ch.13 l.406 line, word for word and in the same function.
    - "For the sheet." (l.143) is Kallia's Ch.10 l.188 line, landing again.
  - **Three SPENT held-beat fillers.** The rain "in a rope" inside Plautia's pause (l.53). The fuller's boy and his steaming vat in Valens's evasion (l.343). The coughing lodger shifting under his blanket after the sweep (l.267).
  - **Six beats or images from Ch.10 and Ch.15:**
    - the lodger's garment on "the rail above" (Ch.10 l.132);
    - the cold rising from the turf (Ch.15 l.6);
    - dawn light descending first/then/then (Ch.15 l.8);
    - a summit with "the first sun on its top" (Ch.15's SPENT day frame);
    - the dog that barks once into the night (Ch.15 l.494);
    - the bed retold in Ch.15's words ("the fork at its head split").
  - **"quite still" for a third time book-wide** (Ch.5, Ch.15).
  - **A sibling of the CLOSED gaze-hold:** "she kept her face to the stair".
  - **Three voice-bank strings:** sample-12 "She took the broom", sample-06 "the middle of the night", sample-11 "the day after the".
  - **A stance slip:** "a low coast I never saw".
  - **A two-item lit inventory** (audit C-02's rule).
  - **A run of in-chapter doubles.**
- **Characters sits at 8.5**, not 9.0, for the following:
  - Valens borrows Kallia's line;
  - Plautia's long-period-then-blunt-question syntax is run as a formula twice running, and the narrator names it;
  - Plautia has a pause cluster (three beats in about 150 words);
  - Myrrhine's lupins appear in all four Corinth sections;
  - Valens's voice is tagged "low" twice;
  - Felix prices the bracelet a page after Myrrhine does.

**Every fix is a swap or a cut. 51 strings, tested together:**
- 7,203 words (shape_check; floor 7,100 ✓); dialogue 45.7% / 46 (40–50 ✓); median 14 (14–15 ✓); 6 breaks; `dialogue` → `question`;
- all gates clean, echo 0, gesture classes unchanged from the original;
- the first line and the closing question are byte-identical, and so is every anchor line.

---

## Genesis Score (Craft Assessment)

| Dimension | Score | Evidence | Cap reasons / holds |
|---|---|---|---|
| Originality | 9.0 | **The outline's subversion is on the page:** the hero's ex arrives as a supplicant, not a rival. She was never his lover, and she ends the chapter an ally. **What the writer built on top of it:** (1) the hooks: "bronze hooks with nothing hanging from them" (l.19), the giving-away shown before it is acted and never explained, which Mara reads as a conservator: "The bronze is worn bright at the bend." (l.51); (2) **the bracelet whose marks are a baby's first teeth**: "Someone had cut his teeth on it." (l.233); (3) Myrrhine pricing the gift for buy-back while her mistress weeps behind the curtain (l.221–229); (4) the porch choreography: a bodyguard's old protocol, done by both bodies without a word, answers the jealousy (l.287–293); (5) mules that cannot vomit, and "Felix, who could, was sick into the sea for the lot of them." (l.395); (6) the himation mended overnight, its stitches growing "a fraction longer, and then, at the very end, small again" (l.261); (7) the dowry instrument as the pretext for the theft, and Valens's fame used as the decoy (l.497, l.525); (8) the two strands converge: the Delphi strand ends on the first sight of Plautia, from behind, that the Corinth strand began with (l.473 → l.21). | **≥9.0 challenge:** would a senior editor set this beside the Laoghaire chapters of *Outlander*? Yes. It inverts that beat and makes the ex the more wounded woman. **Not 9.5:** the Parallel frame is the outline's, and the heist-planning scene (C4) is genre-standard in shape. |
| Theme | 9.0 | The theme is "What is owed to the people you leave". It is carried by acts and closed as a question. **Acts:** Kallia's line to her son, which Mara carries (l.175–203); the obol kept for the sheet (l.143); the himation made Mara's by a night's sewing; the lamp pinched out at first light; Plautia's son, glimpsed twice in three years (l.53). **The close is the theme as a real question:** "what was there left in Rome that would bring him to stand up before a court and tell it the truth about her?" (l.587). It is the outline's "real one, unanswered, and not rhetorical". **Texture that means nothing:** the scorpion and "its brother in the woodstack" (l.111–113); the floor-layer who works drunk (l.159); the Sicyon match "with a vineyard and a cough" (l.91); mastic spat into the sea (l.389); the dun in the cook's cabbages (l.581); Gloria's Ray on the Lewes–Cape May ferry (l.405). | **≥9.0:** a question with two sides. Kallia is left owed nothing she will say; Plautia is owed testimony she cannot compel. **Not 9.5:** the gift motif is dense (hooks, ball, cloak, shoes, bracelet, himation, obol), at the edge of an echo chamber. The texture above saves it. |
| Characters | 8.5 | **Mara: chaos 4/4** (below). **Plautia** is fully a person: book Latin "broken by sudden blunt questions"; no contractions (verified, every line); the torn earlobe; "her face was wet and perfectly composed" (l.237); "You will think me very badly governed," (l.239); her one laugh (l.379); the bow (l.577). She is **not a rival-trope**: "What he had chosen … when at last he chose anything." (l.85) is grief, not designs. **Myrrhine:** her axis is resale ("Everything she gives away is for sale again by morning.", l.225); she is jealous of the writing case (l.485–493). **Kallia:** her own life first (the scorpion); the griddle line; "Pay him when he's aboard," (l.145); her farewell given as labor, with no speech. **Valens:** the guard's reflex at the porch; the baker's change, "I bought another loaf with it." (l.351); the black mule down at sea; "Don't spend it on mules." / "You asked for it." / "I did." (l.439–443); "It was new," (l.565). **Felix:** stacked questions; sick for everyone; "I'd sooner not look at it" (l.461). Cover-the-name PASS for all six speakers. | **No cap.** No character leads with a catchphrase, and the gate's gesture classes are all under cap (I use the gate's numbers). **Held at 8.5:** see the bullets under the table. |
| **Prose & Voice** | **8.0** | **Stopping sentences:** "**Someone had cut his teeth on it.**" (l.233); "Toward the second corner they grew a fraction longer, and then, at the very end, small again." (l.261). **Underlines:** "her face was wet and perfectly composed" (l.237); "Which was true." (l.245); "Behind him the street might have been a wall." (l.293); "When it reached me there were lamps in Kirrha." (l.107); "Felix, who could, was sick into the sea for the lot of them." (l.395); "a long low sound like furniture being dragged across a floor upstairs" (l.393); "the flame on the sill went from being the brightest thing in the court to being only one of the things in it" (l.269); "one night's burning laid over years of others" (l.271); "I had been married to a man in that house for three months … and I had had one name for him." (l.557); "When his letter came, did she weep?" / "She swept a floor." (l.189–191). **Ugly sentence:** "I wrote it out twice because the first one blotted and the second one was not better." (l.155). **Voice under pressure:** the night at sea drops to plain hands-and-bodies sequence, with no aside between l.411 and l.427. C2's weeping section goes plain too ("Behind the curtain the sound had stopped. I went in.", l.235). | **Merit 8.0, no cap.** #11 is under the cap (4 firm, 0.53/1k), and the ugly sentence and the voice change are both present. **Held by the law cluster** (R1–R29 below): an earlier chapter's delivery frame ×4; two whole spoken lines from earlier chapters; three SPENT held-beat fillers; six reused beats and images; "quite still" for the third time; a CLOSED-frame sibling; three sample strings; a stance slip; a run of in-chapter doubles. Anti-AI: 8/20, −1.625 (clean band, at its edge). |
| Pacing | 8.5 | **The ledger row is hit on every hard field:** Parallel, between Ch.15's Chronological and Ch.17's In medias res ✓; open `dialogue` ("Have you seen his back?") ✓; close `question` ✓; 6 breaks / 7 sections ✓; dialogue 44.3% (40–50) ✓; 7,540 against 7,600 ✓; median 14 (mid) ✓. **Speed design, as the outline asks:** "Corinth quick and talky; Delphi slow and silent." Measured by section: C1 57%, C2 43%, C3 51%, C4 73% dialogue; D1 22%, D2 **0%**, D3 22% (action pace). **Value shift:** jealous and outside (−) → given the bracelet (+) → the friendship turn (+) → a plan (+) → doubt about Valens's testimony (−). In Delphi: leaving (−) → the mended cloth (+). | **Not 9.0.** C1's record-office politics run 20 lines of exposition (Nero's grant, the proconsul's freedmen, the copyist; l.57–77), and C4's book-of-boards mechanics another 15 (l.539–555). Both are dialogue and both are needed for Ch.17, but the Devourer slows in both. Three ~7.5k chapters run back to back (Ch.15–17); the ledger planned it. |
| Emotion | 9.0 | **The anchor lands exactly as planned:** Plautia gives away the bracelet Mara admired, then weeps "in the next room": "You admired it." … "The smoke has got into my eyes." (l.213), then the curtain and the sound "held in, then loosed" (l.217). Then the marks, then "Will you wear it?" / "On the left. It was made for the left." (l.245–249). **The surprise, as planned:** the jealousy turns into friendship over a broken bed (l.377–385). Also, Myrrhine haggles over the bracelet while her mistress weeps: humor in grief. **Body rebel:** Mara's blush, "and she watched it go" (l.15); Plautia's tears, and her laugh breaking "from her again, and that time she let it" (l.379); Felix sick at the rail. **Techniques ≥5:** object proxy (bracelet, hooks, ball, himation, lamp); subtext (archives and bribes over "did he love you?"); humor in grief; physical sensation (the dun's "whole hot weight"); dramatic irony ("He'd want in." / "He'd stay in.", l.331–335). **Kallia's farewell is all object and act:** the mended hole, the sweep, the flame pinched out. | **≥9.0.** **Not 9.5:** Mara's own feeling at leaving Kallia is withheld entirely. That is the design, and it is the right one, but some readers will not register the goodbye until D3 begins. |
| **Immersion** (Dim 7) | 9.0 | **Period:** the proconsul's office at the end of the long colonnade, across the forum from the old temple (the South Stoa and the Temple of Apollo, l.339); the Lechaion road and moles; Acrocorinth and Aphrodite; the diolkos "East of the harbor"; the women's benches at the top of the theater; the *actio rei uxoriae* before "a judge the praetor gives us" (l.573); freedman nomenclature, "Gaius Iulius Valens, freedman of Gaius" (l.555); a magistrate's year kept as sealed boards on a cord (audit I-03); a dowry instrument in the colony's books; lupins; mastic; a brailed sail; mules that cannot vomit; a reed cut for papyrus. **1998, used:** the drugstore at Twentieth and Walnut and its seasickness bands (l.405). | **Held at 9.0.** The record office as the proconsul's is good fiction on real bones. Slips: "the crack of light" beside a dark window, while the lamp stands outside on the sill (l.271, L2); "two years" for Ariston's silence, which is three (audit I-22, L4); the fullers' steaming vat (audit I-10; cut by R10). |
| **FLOOR** | **8.0** | Prose & Voice (merit) | |
| **AVERAGE** | **8.71** | (9.0 + 9.0 + 8.5 + 8.0 + 8.5 + 9.0 + 9.0) / 7 = 61.0 / 7 | |

**Why Characters is held at 8.5:**
- **Valens speaks Kallia's line.** "She does that." (l.307) is Kallia's Ch.13 l.406 sentence, word for word and in the same job: explaining another woman's habit. The echo scan cannot see it, because every word is a stop word.
- **Plautia's syntax becomes a formula** (C2, C3):
  - l.159 and l.163 run the same skeleton twice running: a long period about nothing, then "she said on the first / second", then the blunt question.
  - The narrator names the habit ("never the same thing twice", l.157).
  - The fingerprint is legal. Its formula is not.
- **A Plautia pause cluster** (C4–C6): "She was quiet for a little." (l.371), "Plautia sat quite still." (l.379) and "she said at last" (l.381), all inside about 150 words. The gate's pause class reads 0, so this is a finding, not a cap.
- **Myrrhine's lupins in all four Corinth sections** (l.19/101, l.229, l.363, l.493). Her card says "once per scene at most; never a fidget". Twice the skins go "onto the coals" or "in the coals".
- **Valens's voice is tagged "low" twice** (l.411, l.433). His card rule is not twice in a chapter.
- **Valens's back is to the wall** at l.287 and l.481. That is two here and three book-wide (Ch.13 "with the wall at his back").
- **Felix prices the bracelet a page after Myrrhine:** "What would it buy? Would it buy a mule?" (l.315). The pricing device is spreading across the cast.

**Trajectory vs Ch.1–15** (finals 8.50–8.86; cycle 0s 7.5–8.0):
- This is the sixteenth cycle 0 below the gate, and the twelfth held by narrator moves the gates cannot see.
- As with Ch.15, the #11 cap did not hold it, and the continuity repair added no gloss.
- The new failure mode is **whole short lines and stop-word-bounded frames** carried over from earlier chapters ("She does that.", "For the sheet.", "every ending…"). They pass the echo scan by construction. See Cross-Book #1.

---

## CVI-Launch Breakdown
| Input | Score | Evidence |
|---|---|---|
| Commercial Pacing | 8/10 | Short, talky Corinth scenes, cut against silent Delphi, with a question close. It loses 2 for C1's politics and C4's mechanics, and for its length. |
| Tomorrow Test | 6+ anchors → 10 | IMAGE: the gold band with a baby's tooth marks; the empty bronze hooks; Kallia's lamp left burning on the sill and pinched out; the pin-hole closed "into a round eye"; the mules groaning like furniture dragged upstairs. QUOTE: "Someone had cut his teeth on it."; "She swept a floor."; "The smoke has got into my eyes."; "Your feet are wet." / "The dog is lying on the dry one." |
| Casual Reader | 9.0/10 | See the report below. |
| Shareability (quote / plot / emotional) | 4 / 3 / 5 → 8 / 6 / 10 → **9.2** | Quote: "Someone had cut his teeth on it." Plot: "the woman he was framed with is a mother who gives everything away, and she plans the heist." Emotional: "she gives Mara the bracelet, goes next door and cries, and the marks on it are her baby's first teeth." MAX 10 × .6 + AVG 8 × .4. |
| Concept Pitch | yes → 10 | |
| Human Closeness | yes → 10 | Two women in a room for most of the chapter; a farewell; a man and a boy keeping a mule alive. |
| **CVI-Launch** | **9.24 + 0.5 = 9.7** | 8 × .2 + 10 × .2 + 9 × .2 + 9.2 × .2 + 10 × .1 + 10 × .1 = 9.24. One-chapter formula; see BIAS CHECK. |

**CVI-L note.** In this project "CVI-L" means **CVI-Launch: 9.7**.
- Running CVI-L Ch.11–16 is **9.5 / 9.7 / 9.8 / 8.9 / 9.8 / 9.7**. The first chapter of "yearning without sex" after the heat chapter holds the readership Ch.15 earned.
- It holds because the romance is kept warm in small beats:
  - "I had had my palms on the ridges of it most nights since July." (l.15);
  - "Behind him the street might have been a wall.";
  - the warm half-loaf (l.353);
  - "You asked for it." / "I did.";
  - "I had had one name for him."
- Shareability shifts from the romance to Plautia. That is healthy: the book now has a second woman readers will talk about.
- **None of the 51 fixes touches an anchor**, so **CVI-L is unchanged after the PATH (9.7).** The bracelet, the marks, "Someone had cut his teeth on it.", the curtain, the hooks, the mended hole, the lamp and "She swept a floor." are all byte-identical.

**CVI-Legacy (default weights; provisional):** **6.9** (Ch.15 7.1). It is the sum of:
- Originality 9.0 × .30;
- Theme 9.0 × .25;
- Cultural Vocabulary 2 × .20 (no fandom-quotable catchline this time);
- Re-readability 7 × .15;
- Identity 5 × .10.

What rewards a re-read:
- "Have you seen his back?" against Ch.12's flogging "by the fishpond";
- "He'd want in." / "He'd stay in." against Felix's later sworn school;
- "Don't spend it on mules." (the batteries kept for a door);
- the lamp frame on the roll, for Ch.43;
- the bracelet on the left wrist, where the watch will go back on in Ch.18 (audit I-29).

---

## Anti-AI Scan (20 patterns; density per 1,000 words at 7.54k; commercial band)
| # | Pattern | Result | Count / density | Citation |
|---|---|---|---|---|
| 1 | Forced symmetry | FOUND moderate | 5 (0.66) | l.367 "his father's ears, which stand out, and my mother's temper, which does not"; l.483 "the young one, who drinks, or the gray-haired one, who does not" (the same pair twice in Plautia's mouth; Ch.15 l.476's narration has it too); l.159 / l.163 as twin paragraphs; l.331–335 "He'd want in." / "He'd stay in." (designed; kept); l.533 "Plautia held his look, and he held hers". **−0.25** |
| 2 | Empty poetic vocabulary | Clear | 0 | |
| 3 | Automatic rule of three | FOUND moderate | 11 triads, **4 automatic (0.53)** | Automatic: l.21 "crossing the court …, going out at the porch, climbing to these rooms"; l.147 "thorn, scree and Mnason's fold"; l.237 bed / window / lamp; l.269 "first … then … then". Characterful, not counted: the master's deck / jars / god (l.407); Plautia's legal rights (l.497), her archive / theater / baths (l.517), her advocate / brother / praetor (l.573), her tomb simile (l.31); the procession out of the door (l.283); the lane known by three marks (l.109). **−0.25** |
| 4 | Em dashes | Clear | 3 (cap 4) | All three are cut-off speech (l.71, l.87, l.211). |
| 5 | Empty metaphors | Clear | 0 | The street "might have been a wall"; "a pewter sky"; furniture dragged upstairs. All concrete. |
| 6 | Dramatic "And" openings | Clear (narration 0) | — | Speech rejoinders: 3 (Mara ×2, l.75 and l.503; the porter ×1, l.469). Under the ≤4 WATCH. |
| 7 | Pseudo-philosophical closings | Clear | — | Every section ends on an act, a touch, a line or an image, and the chapter ends on a real question. |
| 8 | Excessive parallelism | FOUND moderate | 6 (0.80) | The l.159 / l.163 twin skeletons; "I'll be by the baker's oven." / "I'll be at the back door." (l.519, l.531); Plautia's repeat-back of Myrrhine's list (l.491, witty; kept); "until he had looked, and until he had moved" (l.289); "held his look, and he held hers" (l.533); "This is the suit. The suit is…" (l.517). **−0.25** |
| 9 | Overly smooth transitions | FOUND minor | — | The strands are sutured by time stamps ("four mornings after that first one", l.155; "a day after Kallia's lamp", l.389), and "At that same moment" (l.285). The Parallel needs the orientation, so minor. **−0.125** |
| 10 | Described emotions | Clear | 0 | The blush is physical ("The heat went up my neck into my ears", l.15). Nothing is named. |
| 11 | **Explanatory extension** | **FOUND moderate, under the cap** | **4 firm (0.53/1k)** | (1) l.89 "She had caught the cloak and the cook, and no more." (comprehension gloss); (2) l.485 "She had followed that much." (the same gloss again → C7); (3) l.443 "where she could not go over again without going over onto him" (purpose tail; a keeper); (4) l.577 "the small bow a woman of her kind gave a porter who offered to carry what she meant to carry herself" (it interprets the gesture; a keeper). Borderline, not counted: l.31's tomb simile with its unpacking (speech); l.261 "to keep the hole from going any further"; l.289 "so that he was at her back"; l.539 "as she gave every word" (→ R1c); l.53 "It came in the same voice as the rest." **−0.25.** Cap (commercial >6 or >0.8/1k): **PASS.** |
| 12 | Binary negation opener | Clear | 0 | Gate pivots 0. |
| 13 | Precision flex | Clear | — | The numbers do work: the teeth ("two at the bottom by midsummer … two at the top by the vintage"), "Twice in three years", the timeline stamps. No counting habit. |
| 14 | Emotional control demonstration | Clear | — | Plautia's composure is the subject, and it fails twice (the curtain, the laugh). |
| 15 | Authoritative description | FOUND minor | — | The record office's two doors (Valens's report, l.339); the hinge mechanics (l.205). Offsets: Greek lost "a clause at a time" (l.11); "something small and yellow" before it is a scorpion (l.111); "a coast" never seen. **−0.125** |
| 16 | Philosophical asides | FOUND minor | 2 (speech) | "one freedman does not call another a liar at his patron's door" (l.69); "A son in Syria has the whole of Syria to look at, and a lane in Delphi must be very small from there." (l.185). Both are characterful, both are in Plautia's mouth, and both are kept. **−0.125** |
| 17 | Clean dialogue | FOUND minor | — | C2's run from l.173 to l.203 is about 14 orderly one-line turns. Elsewhere the talk breaks up: Myrrhine butts in, "Can your brother not—", "I have not finished.", Felix's shout from the court. **−0.125** |
| 18 | Thematic echo chamber | Clear (edge) | — | The gift motif is dense; the texture listed under Theme keeps it clear. |
| 19 | Graduated reveal | Clear | — | Parallel. |
| 20 | Emotional temperature report | Clear | — | |

**8 / 20 found (#1, #3, #8, #9, #11, #15, #16, #17). Total −1.625. Band: clean** (commercial 0–8), at its edge. **#11 hard check: PASS** (0.53/1k).

**After the PATH:**
- #1 → minor (C11, C2);
- #3 → minor (R7, R18);
- #11 → minor (C7, R1c; 3 firm, 0.42/1k);
- #8 stays moderate (the designed pairs stay);
- → **8/20, −1.125, clean band.**

---

## The book's own laws
- **NO FORESHADOWING: PASS on the gate (0). One stance slip by hand.**
  - "we lay all night off a low coast **I never saw**" (l.411). "Never" claims a vantage after the scene: she cannot know, that night, that she will never see that coast. It belongs to family C (the "I never saw him again" construction), applied to a coastline → **L3**.
  - AD 79 appears 0 times (allowed ≤1).
  - Character forecasts are speech, not narration: "He'd stay in."; "He will find out in the spring."; "you will be on a ship out of Lechaion".
  - Kallia's farewell carries no significance tag: no "last time", no "never again".
- **AUTHOR-CP3-5: PASS.** l.477 reads "At the games for Titus's triumph". The page never says "Isthmia" or "Isthmian Games". The festival is "the games", the sanctuary is "the god's precinct on the Isthmus", and the boys' race belongs to this festival.
- **AUTHOR-CP3-3 (the pregnancy gap unremarked): PASS.**
  - "most nights since July" (l.15) and "Every night, lying beside him" (l.21) do not notice the months.
  - The nursing bracelet on Mara's wrist is never linked to a child of hers, by anyone.
- **Plautia is not a rival-trope: PASS, strongly.**
  - She asks to see "What he had chosen" (l.85).
  - She evades "Have you?" with a lawyer's answer (l.25), which feeds Mara's jealousy without any claim on him.
  - She gives rather than takes. Her want is her son and her suit.
  - The porch answers "were they lovers?" by watching (outline ✓). The reader sees a guard's protocol, not a lover's.
- **Kallia's farewell has no speech or proverb: PASS.**
  - D1's lines are practical: the mules, the boy, the boat, the bread, the griddle joke, "Pay him when he's aboard".
  - D2 has **no speech at all**.
  - There is no wool, no stopped work, no water order at a close, and no "had gone quiet".
  - She never sits and never touches Mara, and she hands Mara nothing: the cloth is laid on the bag.
  - The covert farewell holds (Delphi believes Mara sailed): Mara waits above the stadium until dark (l.107).
- **The non-negotiables: all on the page.**
  - The himation is given without speech: folded and handed back, taken in silence, made Mara's by a night's mending (l.147–149, l.259–263).
  - The sweep and the broom are worded fresh. The broom's position is not described (the Ch.10 rule); but see R14 for "jamb to jamb" and the sample-12 string.
  - The lamp frame is shot at first light; Kallia does not ask what the camera does (l.269–277).
  - The Isthmus plan (C4).
- **Memory only when triggered by the scene: PASS.** One clause-length 1998 memory: the drugstore's seasickness bands and Gloria's Ray. It is triggered by the seasick dun's head in Mara's arms, and returns at once ("The dun groaned again.", l.405). No parent is in it (the Ch.14 rule), and there is no longer memory (the Ch.15–16 rule). The credential asides (l.205, l.231) are the conservator's eye on the bracelet in front of her.
- **Explanation-density cap: PASS** (4 firm, 0.53/1k) → 3 after the PATH (0.42/1k).
- **Paragraph-final negations ≤1.5/1k: PASS.**
  - **9 in narration (1.19/1k):** l.19, 89, 155, 157, 219, 263, 265, 355, 443. My script also flags l.109, l.289 and l.587, but each only contains a negation mid-clause.
  - **After the PATH: 7 (0.97/1k).** C3 cuts l.157's; R14b cuts l.265's opaque "and did not go near the stair".
- **No comparisons in Valens's speech: PASS.** Every Valens line was checked. None uses "like" or "as", and none is figurative. "Up, now, you old fool. Up," is spoken to a mule; "he said I had the look" is the baker's judgment, reported.
- **No command echoes: PASS** (the gate reads none; hand check agrees). Compliance is shown by result:
  - "Then sit." → "I took Myrrhine's stool.";
  - "Hold the dun's head up." → "I cupped the dun's jaw";
  - "Take the sacks round." → Felix's exit, which the PATH keeps free of "round" (R22);
  - "Go to sleep" → no shown compliance after R13.
- **NO TICS, verbal: PASS on catchphrases.** Spoken lines carried over from earlier chapters: **FAIL ×2** → C1, R3.
  - "She does that." (Valens, l.307) is Kallia's Ch.13 l.406 line.
  - "For the sheet." (Mara, l.143) is Kallia's Ch.10 l.188 line, quoted back.
  - Lesser stock overlaps, each a second use in a different mouth: "Go to sleep." (Ch.8), "Give it here" (Ch.13), "All of it?" (Felix's own Ch.11 question), and the one-word line "Some." (Valens, Ch.15 l.398) → R23–R26.
  - Two stock lines stay: "And yours?" (Ch.13 Theano; 2 book-wide) and "Not much." (Ch.1, Ch.13).
- **NO TICS, gestures and narrator moves the gate cannot classify:**
  - **Pause cluster (Plautia):** l.371, l.379, l.381 → C4–C6.
  - **"quite still", third use book-wide** (Ch.5 l.287 "stood quite still"; Ch.15 l.560 "he was quite still"; l.379 "sat quite still"). The CLOSED "had gone (quite )?(quiet|still)" family has grown a sibling verb → C5.
  - **"kept her face to the stair"** (l.473): the CLOSED gaze-hold "kept [poss] eyes on the [X]", in a sibling noun, exactly as Ch.15's H2 ruled → R17.
  - **Two-item lit inventory** (l.417 "were the white of her eye and the sweat on her shoulder, and Valens in the straw"). Audit C-02 holds two-item gaze sequences to the CLOSED item-by-item rule → R28. (The lamp's parts in the finder, l.271, are the outline's named frame: one object, not a gaze over a person. Kept.)
  - **Valens:** voice tagged "low" ×2 (l.411, l.433 → C9); back to the wall ×2, third book-wide (l.481 → C10).
  - **Myrrhine:** lupins in four of four Corinth sections → C8a–c.
  - **Narrator naming a character's habit** (l.157) → C3. **In-chapter call-out pointer** "as they had been in the chair" (l.237) → C13.
  - **The pricing device across the cast:** Myrrhine prices the bracelet (designed, once). Felix prices it a page later (l.315) → R29.
  - Gate classes: object handling, kneel / crouch, hand / chin on the knee, bend, deliberation pause, exit by gait: all 0–1 in this chapter ✓.
- **SPENT devices: FAIL ×3** → R8, R9, R10. The rule: a held silence measured by something moving — "nothing that moves, drips, steams, turns or casts a shadow" — 0 more.
  - l.53: the rain "in a rope", placed inside Plautia's pause before "Would a porter keep a child's ball?".
  - l.343: the fuller's boy with a vat "of something that steamed", placed inside Valens's evasion ("I went for barley."). It is also passing traffic (SPENT, Ch.9) and a factual slip (audit I-10: fullers' tubs were cold).
  - l.267: "the old man coughed and shifted under his blanket", placed into the held moment after the sweep.
- **No reuse of earlier chapters' phrases or set pieces: FAIL, cleared by the PATH.**
  - **The delivery frame** (Ch.5 l.199 the herald: "every word set down by itself and every ending given its full weight"; Ch.6 l.166 Valens: "every ending in its place, a man setting things down one by one"). Ch.16 rebuilds it four times:
    - l.33 "book Latin, laid down slowly";
    - l.35 "each ending sounded to its last letter";
    - l.539 "She gave his name its weight, every sound of it, as she gave every word";
    - l.587 "with each word laid down on its own".
    - → **R1a–d**, the highest-value set.
  - **Ch.10 l.132** "A lodger's tunic was drying on the rail above us." → l.117 "A lodger's cloak was hung over the rail above" → **R4**.
  - **Ch.15 l.6** the cold that "rose from the turf" → l.105 "the evening cold rose from it" → **R11**.
  - **Ch.15 l.8** the light worked down "…, then the hut, then a hump" → l.269 "first the ridge tiles…, then the coping…, then the highest leaves" → **R7**.
  - **Ch.15 l.6** "The summit took the sun first" (the SPENT summit day frame) → l.445 "the great rock of the citadel with the first sun on its top" → **R6**.
  - **Ch.15 l.494** "The herdsman's dog barked once near the fold … and it did not bark again." (the night before the chapter's last intimate exchange) → l.585 "the dog gave one bark and stopped" (likewise) → **R5**.
  - **Ch.15's heat staging retold in its own words:** "the fork at its head split" (Ch.15 l.542 "the fork at the head of the bed split") and "for some while" → **R12**. The retelling itself stays. It is the friendship turn, and the outline's best use of the bed.
  - **Ch.14 l.82 + Ch.15 l.490:** "Felix lay down again on his rope" → **R13**.
  - **Ch.10's "from post to post" span** → l.265 "jamb to jamb" (the bible asked for a third wording) → **R14a**.
  - **Voice-bank strings:**
    - sample-12 "She took the broom" (l.265; sample-12's own broom slot) → **R14b**;
    - sample-06 "the middle of the night" (l.411; audit I-31) → **R15**;
    - sample-11 "the day after the" (l.517) → **R16**.
  - **Ch.15 l.306** "a porter on the door and a dog in the porch", re-said at the arrival (l.463), which also doubles l.339's "a porter on a stool" → **R19**.
  - **Smaller echoes:** Felix's exit verb "made for" (Ch.15 l.416; → R22); "like any other" (Ch.7; → R27).
- **The Parallel structure must not rhyme mechanically: PASS, with one fix.**
  - The paired beats are thematic and varied in execution:
    - two gifts, one spoken over and one silent;
    - two withdrawals behind a barrier, one to weep behind a curtain and one to sew behind a shutter;
    - two objects read for the hand behind them. The bracelet's inference is stated ("Someone had cut his teeth on it."). The stitches' inference is left unstated.
  - The narrator never points at a pairing.
  - **The one mechanical element:** C1 pre-describes, nearly in D3's words, the image D3 closes on ("under a cloak that Myrrhine held up to keep the rain off her", l.21, against l.473 "a maid behind her holding a cloak over her against the drizzle"). So the convergence lands twice → **R18**. After it, C1 says only "from behind and at a distance", and D3's image arrives fresh.
- **Logic and fact:**
  - **L1** "two of her brother's slaves" (l.283): "her" points to Myrrhine (audit I-36).
  - **L2** "a crack of light beside it where the shutter was ajar" (l.271): there is no inner light once the lamp stands on the sill.
  - **L3** the stance slip (above).
  - **L4** "in more than two years" (l.187): Ariston has been silent since the vintage of 68, so it is three-plus years (audit I-22).
  - **L5** Plautia speaks twice running with no beat between (l.85 → l.87; audit I-32).
- **Retired reflexes:** no define-by-negation opener; no performed candour; no scene button; no closing aphorism; and-chains 5/9; em-dash 3 ✓.
- **Ledger:** approach ✓, open ✓, end ✓, breaks ✓, dialogue ✓, theme ✓, length ✓, gear ✓.
  - **Outline beats:** all on the page, in the alternation asked for. Corinth: the brother's house, Marcus "seven at the vintage", the archive under the restored proconsul with Celer on his staff. Delphi: the farewell. Then the bracelet, the crossing with seasick mules, and the triumph-games plan.
  - **Chaos moments ✓:** Plautia's giving-away; Mara's all-or-nothing over the cakes (l.21), "enemy, then sister".
  - **Subtext ✓:** archives and bribes over "did he love you?" (l.79–85, l.371–375, l.567–569).
  - **Writer warnings ✓:** no rival-trope; no speech or proverb in Kallia's goodbye; the closing question real and unanswered.

---

## Character Chaos Check (Primary: Mara)
- **Irrelevant thought: PRESENT, inhabited.**
  - The seasickness bands from the drugstore at Twentieth and Walnut, and Ray sick "from Lewes into Cape May", while a mule groans into her himation (l.405).
  - The bronze "worn bright at the bend" when she should be answering (l.51).
- **Cognitive distortion: PRESENT, inhabited.** All-or-nothing, enacted as a loop: "If Valens had lain with her, then all of his telling by the stream had been a story … If he had not, no woman alive sent honey cakes to a muleteer's wife. Every night … I went round it and came out where I had gone in." (l.21). Plautia breaks it: "You are lying." (l.99).
- **Unprompted memory: PRESENT, triggered** (the bands); the lab trays of bracelets (l.205).
- **Failed emotional management: PRESENT.** The blush, which Plautia watches (l.15); "No," I said. "Lady, I only—" (l.211); the lie caught (l.97–99).
- **Voice under pressure: demonstrated** (the night at sea; the curtain).
- **4/4, mostly inhabited.** The cakes loop is narrated reasoning, but it is a reasoning that fails, so it counts.

## Secondary Character Chaos
- **Plautia:** gives away what is admired, then weeps (irrational, outline ✓); her laugh breaks out of her. Her own moment.
- **Myrrhine:** buys back what her mistress gives away; is jealous of the writing case. Her own moment.
- **Kallia:** the scorpion and its brother; the night spent sewing. Her own moment.
- **Valens:** the guard's reflex on the step before he has thought (l.287); "I bought another loaf with it." His own moment.
- **Felix:** sick for everyone; then "I'd sooner not look at it", about the ship-road he begged to see. His own moment.
- No secondary character is a mere function. No cap.

---

## The Tomorrow Test
**What the reader remembers:**
- A woman who owns almost nothing gives Mara the gold band off her wrist because Mara admired its hidden clasp. She says the smoke has got into her eyes and goes behind a red curtain.
- While she weeps, her maid offers Mara a drachma for it.
- Then Mara finds two small paired marks near the clasp: "**Someone had cut his teeth on it.**"
- And in Delphi, at first light, a lamp left burning on a sill all night, the cloak mended, and the flame pinched out with wet fingers.

**Anchor type:** BOTH.
- IMAGE: the tooth marks; the empty hooks; the round eye sewn where the pin had torn; the lamp on the sill; the black mule sitting up "like a dog".
- QUOTE: "Someone had cut his teeth on it."; "She swept a floor."; "The smoke has got into my eyes."; "Your feet are wet." / "The dog is lying on the dry one."

**Verdict: ANCHOR EXISTS** (strong; +0.5 CVI).

**Type check:** an object read for the life of an absent child, plus weeping heard through a cloth. Earlier anchors were a question that was another question (Ch.15), a concealment (Ch.14), a recitation and a one-word reveal (Ch.13), an object in motion (Ch.12) and an animal's stillness (Ch.11). The emotional channel (offstage weeping) is new to the book.

## The Shareability Test
"The woman the gladiator was supposedly sleeping with turns out to be a mother whose ex-husband kept her son. She gives away anything anyone admires. She gives Mara her bracelet, goes into the next room and cries, and the little marks on it are her baby's first teeth. Then the two of them plan a heist." Running total: 16 chapters, 30+ shareable moments.

---

## Reader Reports

### The Devourer (7.5k after Ch.15's 7.5k)
- **Speeds up:**
  - "Have you seen his back?";
  - the Greek-to-Latin switch;
  - the hooks and the ball;
  - the bracelet and the curtain;
  - the porch;
  - "I bought another loaf with it.";
  - the mules at sea and the black going down;
  - the baker's back door;
  - Valens refusing the horse fair, "No." / "I have not finished.".
- **Slows:**
  - C1's archive politics (l.57–77: Nero's grant, the freedmen, the copyist);
  - Plautia's twin "charcoal" mornings (l.157–171);
  - C4's boards, cord and seals (l.539–555).
- **Would they stop?** No. Every Corinth section is a conversation with an edge, and every Delphi section is short.
- **Last page:** the question is real ("what was there left in Rome…?"), and the reader knows the games are next. They turn.

### The Critic
**Underlines:**
- "Someone had cut his teeth on it.";
- the stitches growing longer, then small again;
- "her face was wet and perfectly composed";
- "Which was true.";
- "Behind him the street might have been a wall.";
- "When it reached me there were lamps in Kirrha.";
- "Felix, who could, was sick into the sea for the lot of them.";
- furniture dragged across a floor upstairs;
- "one night's burning laid over years of others";
- "I had had one name for him.";
- "She swept a floor.".

**Disappointments:**
- "*every ending … laid down … every word*: the herald's frame from Ch.5, four times" (R1);
- "*She does that.*: Kallia's line, in Valens's mouth" (C1);
- "*the rain poured off the eaves in a rope*: a pause filled with weather again" (R9);
- "*the first sun on its top*: last chapter's summit" (R6);
- "*the dog gave one bark and stopped*: last chapter's dog" (R5);
- "*she said on the first … she said on the second*: the trick shown twice, then named" (C2, C3).

### The Hostile
1. **Whose brother?** "Myrrhine came out first … then two of her brother's slaves" (l.283) → **L1**.
2. **Where is the light coming from?** The window is dark, "a crack of light beside it", yet the lamp is outside on the sill (l.271) → **L2**.
3. **"a low coast I never saw"**: never, as in for the rest of her life? (l.411) → **L3**.
4. **"more than two years"**: Ariston left at the vintage of 68 (l.187; audit I-22) → **L4**.
5. **Fullers' vats do not steam** (l.343; audit I-10) → R10 (cut).
6. **Felix has now seen the flashlight** (l.419). So, in principle, have the master and his boy, though they are aft and it is night. The Ch.5 rule ("any use must reckon with being seen") is met for Felix: Valens shuts him down twice. Entity note for Ch.17; no change.
7. **"There's only the one."** (l.321) reads oddly at first. It is Valens's deadpan: there is only one amphitheater in Corinth, so of course that is where he got his sword. In character; no change.
8. **Why does Plautia switch to plain Latin for the last question?** Directness, shown, not glossed. No change.

**Verdict:** "Three small slips (a pronoun, a light source, a span of years), one stance word. The timeline holds: the autumn rains, the winter half gone, ten days at Patrae, 'three months' married by the porter's account."

### The Casual Reader (airport, 10 pages)
- **Hooked at once:** a stranger's first words are "Have you seen his back?", and the heroine blushes to her ears. The reader wants to know who this woman is to him.
- **Feels it at:**
  - the empty hooks;
  - "My son was seven at the vintage.";
  - the ball the porter took in;
  - the bracelet and the curtain (they cry);
  - the maid haggling over it (they laugh while crying);
  - the porch, where the reader sees the old bodyguard and his lady;
  - the mules being sick, and the black mule down in the night.
- **Frictions:** C1's proconsul-and-freedmen politics; the seals and cords.
- **Would they buy after 3 pages?** Yes. **Do they stay?** Yes. Plautia is the character they will talk about. **9.0/10.**
- **Not 9.5:** the archive politics, and Kallia's goodbye is so quiet that a fast reader may not register it as a goodbye until the boat.

### The Devoted Reader (active: long saga)
**Will post about:**
- the South Stoa as the proconsul's office and the "old temple" across the forum;
- the *actio rei uxoriae* and "a judge the praetor gives us";
- freedman naming (Gaius Iulius, from the lanista);
- a magistrate's year on sealed boards;
- mules' inability to vomit;
- the diolkos seen from Lechaion;
- the Lewes–Cape May ferry;
- "Have you seen his back?" against Ch.12's fishpond;
- "He'd stay in.".

**Will catch:**
- the herald's delivery frame from Ch.5 (R1);
- "She does that." from Ch.13 (C1);
- last chapter's summit and dog (R5, R6);
- the lodger's garment on the rail above, from Ch.10 (R4).

---

## Cross-Reader Matrix
| Issue | Devourer | Critic | Hostile | Casual | Devoted | Severity |
|---|---|---|---|---|---|---|
| R1 the Ch.5/6 delivery frame ×4 | | ✓ | | | ✓ | **SHOULD FIX → blocking** (no reuse) |
| C1, R3 whole spoken lines from Ch.13 / Ch.10 | | ✓ | | | ✓ | **SHOULD FIX → blocking** (no reuse; no line lands again) |
| R8–R10 SPENT held-beat fillers | | ✓ | ✓ (vat) | | ✓ | **IMPORTANT → blocking** (SPENT, 0 more) |
| R4–R7, R11–R13 reused beats and images (Ch.10, 14, 15) | | ✓ | | | ✓ | **SHOULD FIX → blocking** (no reuse) |
| C5, R17, R28 CLOSED-frame siblings ("quite still", the gaze-hold, the lit inventory) | | ✓ | | | ✓ | **SHOULD FIX → blocking** (law) |
| R14b–R16 voice-bank strings | | ✓ | | | ✓ | **SHOULD FIX → blocking** (voice-dna §6) |
| L3 "I never saw" | | ✓ | ✓ | | | **SHOULD FIX → blocking** (no foreshadowing; narrating stance) |
| C2–C6 Plautia's formula, the narrator's naming, the pause cluster | | ✓ | | | | INVESTIGATE → **fix** (tic budget 0) |
| C8 Myrrhine's lupins; C9, C10 Valens's "low" and wall; R29 Felix's pricing | | ✓ | | | ✓ | **SHOULD FIX** (card law) |
| L1, L2, L4, L5 logic and fact | | | ✓ | | ✓ | **SHOULD FIX** (cheap) |
| R18–R27, C11–C13 in-chapter doubles and small echoes | | ✓ | | | | INVESTIGATE → **fix** (cheap, tested) |
| C1 archive politics / C4 mechanics | ✓ | | | ✓ (frictions) | | SHOULD FIX → **no change.** Both are needed for Ch.17's theft, both are in dialogue, and both are broken by Plautia's turns ("Kind." / "Dined that evening with my former husband."). The PATH trims around them. |

---

## Revision Recommendations (Ranked)
*All 51 strings below were applied together to a scratch copy and run through `check_chapter.sh 16`, `shape_check --strict` and `tic_report.py --gate`. All are clean, echo 0, and the gesture classes are unchanged from the original. Strings that tripped a gate on my first tries are listed under "Do not use".*

| # | Location | Problem type | What happens now | Why it fails | Revision direction (exact) | Project rule? |
|---|---|---|---|---|---|---|
| L1 | l.283 | Logic | "then two of her brother's slaves in their cloaks" | "her" points to Myrrhine (audit I-36). | → "then two of **the** brother's slaves in their cloaks" | No |
| L2 | l.271 | Logic | "a square of dark with a crack of light beside it where the shutter was ajar." | There is no light source inside once the lamp is on the sill. | → "In the finder the window was a square of dark, **its shutter ajar**." | No |
| L3 | l.411 | Logic (stance) | "off a low coast I never saw, rolling" | "never" narrates from after the scene (family C). | → "off a **dark coast**, rolling" | Yes: add `\b(a\|the) \w+ I never (saw\|heard\|learned)\b` to the foreshadow scan |
| L4 | l.187 | Factual | "in more than two years." | Silent since the vintage of 68 (audit I-22). | → "in more than **three** years." | No |
| L5 | l.85–87 | Clarity | Two Plautia paragraphs running, the second re-tagged. | Audit I-32. | Merge: "…when at last he chose anything. **Everybody who climbs that stair wants something of mine. My** brother's advocate…" | No |
| C1 | l.307 | Voice (reuse, cross-character) | "She does that. Give it to her woman" | Kallia's Ch.13 l.406 line, word for word, in the same function. | → "**She's done it before.** Give it to her woman" | Yes: see Cross-Book #1 (short-line registry) |
| C2 | l.163 | Character (formula) + doubles | The proconsul's-wife period, "she said on the second.", then the question. | The l.159 skeleton again; the fourth cough in the chapter. | → "\"Were you afraid of him, at the beginning?\" **she said on the second.**" | Yes: a character's syntax fingerprint never runs the same skeleton twice running |
| C3 | l.157 | Character (narrator names a habit) | "asked me one thing straight out, never the same thing twice." | It turns her syntax into a labeled device; para-final negation. | → "asked me one thing straight out." | Yes: the narrator never names another character's verbal habit |
| C4 | l.371 | Character (pause cluster) | "I watched him at the well.\" She was quiet for a little. \"Does he laugh?" | Three pause beats in about 150 words (l.371, 379, 381). | → "I watched him at the well. Does he laugh? Your husband." | No |
| C5 | l.379 | Character (CLOSED family; pause) | "Plautia sat quite still. Then a sound broke from her" | "quite still": third use book-wide (Ch.5, Ch.15). | → "**A sound broke from Plautia**, short, surprised;" | Yes: extend the CLOSED entry to `(had gone\|was\|sat\|stood) quite (quiet\|still)` |
| C6 | l.381 | Character (pause) | "\"The herdsman?\" she said at last." | The third of the cluster; "at last" ×3 in the chapter. | → "\"The herdsman?\" she said." | No |
| C7 | l.485 | Style (#11) | "in Greek. She had followed that much." | The second comprehension gloss (l.89 keeps one). | Cut the sentence. | No |
| C8a | l.229 | Character (card) | "returned to her stool and her lupins, and ate one, and watched" | Lupins in four of four Corinth sections (card: once per scene). | → "Myrrhine returned to her stool and watched the curtain." | No |
| C8b | l.363 | Character (card) | "The lupin skins were still in a heap under it, and I moved them with my foot." | as above | Cut the sentence. | No |
| C8c | l.493 | Character (card) + double | "so hard that half of it landed in the coals." | Skins "onto the coals" at l.101. | → "so hard that half of it **shot under the chest**." | No |
| C9 | l.433 | Voice (card) | "he spoke across her, low." | Valens's voice tagged "low" twice (l.411). | Cut ", low". | No |
| C10 | l.481 | Character (posture) | "with his back to the wall by the jamb." | Back to the wall ×2 here (l.287), third book-wide (Ch.13). | → "Valens stood just inside the door." | Yes: WATCH Valens back-to-wall, 2 book-wide |
| C11 | l.483 | Style (#1) | "or the gray-haired one, who does not, and" | The "X, which does / Y, which does not" pair again (l.367; Ch.15 l.476). | → "or the gray-haired one, and that both" | Yes: the paired relative-negation frame ≤1 per chapter |
| C12 | l.225 | Voice (bleed) | "off a fuller's wife at the Saturnalia" | "a fuller's wife" is in Plautia's mouth 20 lines later (l.245). | → "off a **rope-maker's** wife at the Saturnalia" | No |
| C13 | l.237 | Style (pointer) | "with her hands folded as they had been in the chair" | An in-chapter call-out pointer. | → "with her hands folded, and her face" | No |
| R1a | l.33 | Style (reuse) | "book Latin, laid down slowly, the verb held back" | Ch.6 "a man setting things down one by one". | → "It was book Latin, **slow, with** the verb held back for the end," | Yes: CLOSE the delivery frame (words set or laid down singly; endings given weight) |
| R1b | l.35 | Style (reuse) | "Mine came out stiff, each ending sounded to its last letter." | Ch.6 "every ending in its place"; Ch.5 "every ending given its full weight". | → "Mine came out stiff." | (as R1a) |
| R1c | l.539 | Style (reuse; #11) | "She gave his name its weight, every sound of it, as she gave every word." | Ch.5's herald. | Cut the sentence and merge the speech: "\"You cannot have the book, Valens. It is the book…" | (as R1a) |
| R1d | l.587 | Style (reuse) | "plain enough for the stableboy, with each word laid down on its own." | Ch.5 "every word set down by itself". | → "plain enough for the stableboy." (the question sentence is untouched) | (as R1a) |
| R3 | l.143 | Style (line lands again) | "\"For the sheet. I never went to Euthydikos's people for it," | Kallia's Ch.10 l.188 line, quoted back. | → "\"**The sheet was to come from** Euthydikos's people, and then" | No |
| R4 | l.117 | Style (reuse) | "A lodger's cloak was hung over the rail above, and up there somebody coughed" | Ch.10 l.132 "A lodger's tunic was drying on the rail above us." | → "**Overhead** somebody coughed in his sleep," | Yes: CLOSE "a lodger's [garment] on the rail above" |
| R5 | l.585 | Style (reuse) | "and at the porch the dog gave one bark and stopped." | Ch.15 l.494's dog that barks once, before that chapter's last intimate exchange too. | Cut the clause. | Yes: a dog barking once into a silence is SPENT |
| R6 | l.445 | Style (SPENT image + double) | "the long low line of Lechaion's moles … the citadel with the first sun on its top" | Ch.15's summit-takes-the-sun frame (SPENT); "long low" also at l.393. | → "and the line of Lechaion's moles, … the great rock of the citadel with a wall running along its crest." | Yes: first sun on a peak at dawn is SPENT for any peak |
| R7 | l.269 | Style (reuse; #3; habitual) | "The light came the way it came every morning into that court, downward: first … then … then…" | Ch.15 l.8's light descending in sequence. | → "**The court grew light**, and the flame on the sill went from being the brightest thing **there** to being only one of the things in it." | Yes: dawn light inventoried in sequence is SPENT |
| R8 | l.267 | Style (SPENT device) | "On the gallery the old man coughed and shifted under his blanket." | A held beat after the sweep, filled by movement; the cough ×4. | Cut the paragraph. | No |
| R9 | l.53 | Style (SPENT device) | "took it in at the gate.\" Outside the shutter the rain poured off the eaves in a rope. \"Would a porter keep" | A pause filled by moving water (0 more anywhere). | → "took it in at the gate. Would a porter keep a child's ball?\"" | Yes: gate a narration sentence of motion or weather wedged between two quotes of one speaker (WATCH) |
| R10 | l.343 | Style (SPENT) + fact | "\"I went for barley.\" At the lane end the fuller's boy was carrying out a vat of something that steamed." | An evasion filled by passing traffic; fullers' vats were cold (audit I-10). | → "\"I went for barley. The porter on the colonnade is the proconsul's. The baker's not.\"" | (as R9) |
| R11 | l.105 | Style (reuse) | "and the evening cold rose from it sooner each night." | Ch.15 l.6's cold rising from the turf. | → "when the turf in the hollow had burned yellow." | No |
| R12 | l.377 | Style (reuse) | "the fork at its head split, … He could not stop for some while." | Ch.15 l.542's words; "some while" (Ch.14, Ch.15). | → "and **it broke under us**, and we went to the floor with the fleeces on top of us. He laughed then. He could not stop." | No |
| R13 | l.433 | Style (reuse) | "Felix lay down again on his rope." | Ch.15 "Felix lay down" plus Ch.14 "lay down again". | Cut the sentence (no compliance is shown for "Shut your eyes"). | No |
| R14a | l.265 | Style (reuse frame) | "Two strokes more along the sill, jamb to jamb." | Ch.10's "from post to post" span; the bible asked for a third wording. | → "Two strokes more along the sill." | No |
| R14b | l.265 | Style (sample-12 string; para-final negation) | "She took the broom back … and did not go near the stair." | sample-12 "She took the broom"; the stair clause is opaque. | → "She **carried** the broom back to the lean-to and hung it from its nail beside the fire, and went to the jar for water." | No |
| R15 | l.411 | Style (sample-06) | "Sometime after the middle of the night I woke" | sample-06 4-gram (audit I-31). | → "**In the small hours** I woke" | No |
| R16 | l.517 | Style (sample-11) | "And on the day after the boys' race, when he rides in from the Isthmus with the dust on him," | sample-11 "the day after the". | → "And when he rides in from the Isthmus after the boys' race, with the dust on him," | No |
| R17 | l.473 | Style (CLOSED sibling) | "and she kept her face to the stair." | "kept [poss] eyes on the [X]", in a sibling noun. | → "against the drizzle." | Yes: extend the CLOSED gaze-hold to `kept (her\|his\|my) (eyes\|face\|gaze)` |
| R18 | l.21 | Style (#3; Parallel rhyme) | "each time from behind: crossing the court under a cloak that Myrrhine held up to keep the rain off her, going out at the porch, climbing to these rooms." | A triad that pre-describes D3's closing image. | → "each time from behind **and at a distance**." | Yes: in a Parallel chapter the narration never pre-describes an image the other strand will dramatize |
| R19 | l.463 | Style (double; restated plan) | "Plautia's brother kept a porter on a stool in his porch and a dog on a chain, which rose" | "a porter on a stool" also at l.339; it re-says Ch.15 l.306. | → "**In the brother's porch** a dog on a chain rose and announced us to everyone in the lane." | No |
| R20 | l.261 | Style (ruler double) | "into a hole I could have pushed a fingertip into, with a fringe" | Fingertip ruler also at l.205 (audit W-08's family). | → "into a hole, with a fringe" | No |
| R22 | l.327 | Style (echo) | "Felix made for the stables" | Ch.15 l.416, Felix's exit verb. ("went round" would echo the order "Take the sacks round".) | → "Felix **started** for the stables" | No |
| R23 | l.299 | Voice (echo) | "Give it here, I'll show you." | Ch.13 l.432. | → "**Hand it over**, I'll show you." | No |
| R24 | l.401 | Voice (echo) | "\"All of it?\"" | Felix's own Ch.11 l.272 question. | → "\"**Every bit?**\"" | No |
| R25 | l.431 | Voice (echo) | "\"Go to sleep,\" said Valens." | Ch.8 l.478. | → "\"**Shut your eyes,**\" said Valens." | No |
| R26 | l.437 | Voice (one-word registry) | "\"Not much. Some.\"" | "Some." is Valens's one-word line in Ch.15 l.398. | → "\"Not much.\"" | No |
| R27 | l.555 | Style (echo) | "go into a writing case like any other pair." | Ch.7 "like any other". | → "go into **my writing case among my letters**." | No |
| R28 | l.417 | Style (CLOSED look) | "In the light were the white of her eye and the sweat on her shoulder, and Valens in the straw" | A two-item lit inventory of a body (audit C-02's rule). | → "In the light **her eye rolled white**, and Valens **was** in the straw at her head" | No |
| R29 | l.315 | Character (device spreading) | "\"What would it buy? Would it buy a mule?\"" | Felix prices the bracelet a page after Myrrhine prices it. | → "\"How heavy is it?\" said Felix. \"**Can you feel it there when you lift your arm?**\"" | Yes: one pricing voice per scene, at most |

*(R2 and R21 are not used: R2 was folded into C1, and R21 was dropped once C10 removed the second "with his back to the".)*

### Fix order: Logic / fact (L1–L5) → Character (C1–C13, R29) → Reuse and law (R1–R20) → Echoes (R22–R28)

**Kept on purpose (and why):**
- **The first line, byte-identical**, and the closing question sentence. The `dialogue` → `question` signatures hold.
- **The bracelet scene entire:** "You admired it." / the curtain / the buy-back / the marks / "Someone had cut his teeth on it." / "Which was true." / "On the left."
- **Kallia's farewell entire,** apart from R14 (two strings) and R7/R8 (the light and the cough).
- **The bed story to Plautia** (l.377). Only Ch.15's words go. It is the friendship turn, and the outline wants the jealousy turned in this room.
- **"He'd want in." / "He'd stay in."**: a designed pair. The second line lands.
- **The coals as Plautia's gaze, closed by "and not of the coals"** (l.57, l.81, l.587): designed, and it pays once.
- **The two dogs** (Delphi l.109; the porch l.283). Each is one presence in one section, and R5 removes the third dog beat.
- **The lamp's parts in the finder** (l.271): the outline's named frame.
- **"the white of her eye" was checked** against the CLOSED "[color] of [thing]" shape. It is anatomy, and Ch.15's "the dark of the bones" is the precedent. R28 removes it anyway, for the inventory.
- **"I said no and"** (l.347; a Ch.7 4-gram): Valens's reported speech, stop-word-heavy, under the gate. Left.
- **"And yours?"** (Ch.13 Theano, Ch.16 Plautia) and **"Not much."** (Ch.1, Ch.13): stock lines in different mouths. Left, and logged for the registry.

**Do not use** (each tripped a gate on my first try):
- "Up on the gallery" (voice-wear and tic gate: Ch.7 ×2);
- "did not look round" (tic gate: "did not look" 3× with Ch.1, 2);
- "one end of it" (echo: Ch.2, Ch.10);
- "came down the court" (tic gate: "came down the" / "and came down", Ch.5, 8, 10);
- "The light reached" (echo: Ch.10);
- "I said. \"I never…" (voice-wear and tic: "said I never", Ch.13, 15);
- "I meant to buy the sheet" (echo: "said I meant to", Ch.2; "to buy the sheet", Ch.11);
- "a coast I could not see" (voice-wear: "I could not see", Ch.6);
- "set off for the" (echo: Ch.5);
- "after midnight I" (echo: Ch.6);
- "went across the" (echo: Ch.7);
- "Let me have it" (Ch.8 l.328);
- "Felix put his head down" (Ch.11);
- "curled up" (an in-chapter double with the scorpion's tail, l.109);
- "flew off her knee" (it trips the gate's hand / chin-on-the-knee class: 13 → 14 book-wide).

---

## Strengths to PRESERVE (do not touch in polish)
1. **The opening, byte-identical:** "Have you seen his back?" with the long Greek she cannot follow, "The question was short and plain, and all of it reached me.", the blush, "Good,".
2. **Plautia's room:** the torn earlobe, the empty loom, the bronze hooks; "The bronze is worn bright at the bend."; the switch to Latin, "Plautia's hands came apart."
3. **The cakes:** "You sent cakes." / "You did not eat them." / "The boy ate them." / "the honey off the dish with his thumb".
4. **Marcus:** "My son was seven at the vintage."; the ball the porter took in; "Would a porter keep a child's ball?" / "A porter would be asked where he got it." / "So I tell myself."
5. **"What he had chosen … when at last he chose anything."**; "That would make you the first … You are lying."
6. **Kallia at night:** the scorpion and its brother; the griddle; "Pay him when he's aboard,"; the himation taken "as she would have taken a pile of a lodger's bedding"; the light that stayed in the shutter; the beaten mat that "smelled of the sun".
7. **"When his letter came, did she weep?" / "She swept a floor."** and "Whether I could carry water." / "Can you?" / "Now."
8. **The bracelet scene entire** (l.205–253).
9. **First light:** the mended hole, "it slid home without catching", the sweep outward, the frame, "with the look she gave a jar when a lodger had been standing too near it", the flame pinched out with wet fingertips.
10. **The porch:** the guard's protocol on the step; "Behind him the street might have been a wall."; "Your feet are wet." / "The dog is lying on the dry one."; "Someone has done that already,"; "He'd want in." / "He'd stay in."; the baker's change and the warm half-loaf.
11. **The friendship turn:** "I have come for nothing," / "Then sit."; the Muses and the Graces; "I walked in front of him for two years and never heard it."; her laugh.
12. **The gulf:** the furniture upstairs; "Felix, who could…"; the black sitting up "like a dog"; "Don't spend it on mules." / "You asked for it." / "I did."; "I'd sooner not look at it".
13. **C4:** "laughing a breath behind the governor"; "My woman reads."; "By whom? … looking at boys."; "I have done that."; "No." / "I have not finished."; "a man carrying a door"; "Iulius." / "The lanista's," / "It was new,"; "From up there a man on the sand has a shield and a crest, and no face."; the bow; the dun in the cabbages; **the closing question, byte-identical.**

---

## PATH TO 8.5 (mandatory; the Floor is 8.0)

**Prose & Voice 8.0 → 8.5 requires:**
- **The earlier delivery frame retired from the page:** R1a–d. The frame is Ch.5's herald and Ch.6's Valens ("every word set down by itself", "every ending given its full weight / in its place"), here four times.
- **No spoken line from an earlier chapter:** C1 ("She does that.") and R3 ("For the sheet."), plus the stock overlaps R23–R26.
- **The three SPENT held-beat fillers out:** R8, R9, R10.
- **The six reused beats and images out:** R4, R5, R6, R7, R11, R12; plus R13.
- **The CLOSED-family siblings out:** C5 ("quite still"), R17 (the gaze-hold), R28 (the lit inventory).
- **The sample strings out:** R14b, R15, R16.
- **The stance slip fixed:** L3.
- **The in-chapter doubles and pointers cleared:** C12, C13, R18, R19, R20, R22, R27.

The stopping sentences, the underlines, the ugly sentence, every anchor and the first and last lines all stay. **The single highest-value set is R1a–d.** It is the clearest case of an earlier chapter's frame rebuilt, and it costs the chapter about 30 words and nothing it needs.

**Characters 8.5 → 9.0 (expected with C1–C13 and R29):**
- Valens gets his own words (C1).
- Plautia's fingerprint is kept but no longer run as a formula or named (C2, C3).
- Her pause cluster is broken (C4–C6).
- Myrrhine's lupins drop to two scenes (C8).
- Valens is tagged once, and the wall is gone from C4 (C9, C10).
- The relative-pair frame appears once (C11).
- The pricing stays Myrrhine's (R29).

**Apply in one pass; the strings are exact (see the table), or run the tested script:**
```
python3 /tmp/claude-0/-home-user/63791ee5-159c-5791-9429-07920f8d9417/scratchpad/ch16-eval-fixes.py \
  books/the-hour-of-ash/manuscript/chapters/chapter-16.md \
  books/the-hour-of-ash/manuscript/chapters/chapter-16.md
```
- Run it from /home/user/Books.
- It asserts one match per string and aborts, writing nothing, on any miss.
- Then run `bash books/the-hour-of-ash/tools/check_chapter.sh 16` and `python3 tools/shape_check.py books/the-hour-of-ash --strict`, and update the chapter's word-count HTML comment.
- The swap harness used for the test is `ch16-eval-swaprun.sh` in the same scratchpad. It always restores the original from `ev16/ch16-original.md` and prints the checksum.

**What the tested run produced (all 51 strings applied together; fixed copy sha256 `3fc626eb…`, md5 `eb8769d9…`):**

| Measure | Before | After |
|---|---|---|
| Words (shape_check) | 7,540 | **7,203** (floor 7,100 ✓; target 7,600, −5%, not padded) |
| Words (style_check / `wc -w`) | 7,546 / 8,195 | 7,210 / 7,858 |
| Dialogue | 44.3% (show/tell) / 44 (shape) | **45.7% / 46** (40–50 ✓) |
| Median sentence | 14 (shape) / 15 (metaphor) | **14 / 14** (14–15 ✓) |
| Breaks / signatures | 6 / `dialogue` → `question` | unchanged |
| First line / closing question / anchor lines | | byte-identical |
| `check_chapter.sh 16` | clean | **all clean**: style (simile 1.0/1k, em-dash 3, foreshadow 0), grammar 0, rhythm 0, show/tell no flags, voice-wear strict clean, tic gate clean (and-chains 5/9, credential 1), echo 0, command echo none, metaphor 1.4/1k |
| Gesture classes (gate) | all under cap | **unchanged** (book-wide counts identical to the original) |
| `shape_check --strict` | CLEAN | **CLEAN** |
| #11 (firm) | 4 (0.53/1k) | **3 (0.42/1k)** |
| Paragraph-final negations | 9 (1.19/1k) | **7 (0.97/1k)** ✓ |
| Delivery-frame uses (Ch.5/6) | 4 | **0** |
| Whole spoken lines from earlier chapters | 6 | **0** (two stock lines left by choice) |
| SPENT / CLOSED frames on the page | 7 | **0** |
| Voice-bank 4-grams | 3 | **0** |
| Content 3-grams shared with Ch.1–15 / samples | 3 | **0** |
| Anti-AI | 8/20, −1.625 | **8/20, −1.125** (clean band) |

**Expected:** Prose 8.5 (merit 8.0 → 8.5 on 51 cited changes, inside the +0.5 limit) and Characters 9.0 (8.5 → 9.0) → **Floor 8.5, Average 8.86** (9.0 / 9.0 / 9.0 / 8.5 / 8.5 / 9.0 / 9.0). Casual 9.0 holds. CVI-L 9.7 holds.

---

## Pacing check (one line for `feedback/progress.md`)
Ch.16 (cycle 0) · Parallel *two places, two farewells*, between Ch.15's Chronological and Ch.17's In medias res ✓.
- **Length:** 7,540w (target 7,600, −1%; 7,203 after the PATH, ≥7,100).
- **Book:** 90,143 against 96,400 cumulative (−6.5%; −6.8% after the PATH). Projected about 243k against the 220k floor ✓ and the 245k target (slightly under: watch, never pad).
- **Dialogue** 44.3% (40–50 ✓); **6 breaks** ✓; **gear median 14** (mid ✓, down from Ch.15's high 16, as planned).
- **Neighbours:**

  | Ch | Words | Gear (median) | Dialogue | Approach | Breaks |
  |---|---|---|---|---|---|
  | 14 | 3,003 | low (12) | 5% | Fragmented | 9 |
  | 15 | 7,479 | high (16) | 35% | Chronological | 3 |
  | **16** | **7,540 → 7,203** | **mid (14)** | **44% → 46%** | **Parallel** | **6** |
  | 17 | 7,400 planned | low | 30–40% | In medias res | 3 |

  **A social, talky chapter after the private, sensual one.** The temperature moves from a bed in a hut to two women in a cold room, with a farewell cut in silence between them. The variance is the design ✓.
- **The run of long chapters:** Ch.15–17 are all about 7.2–7.5k. The ledger planned it, and Ch.18 (2,800) breaks it. Gear (high → mid → low) and dialogue (35 → 46 → 30–40) both move, so the run does not flatten.
- **Signatures:** `dialogue` / `question`; no three running (Ch.14 `long-fade`, Ch.15 `quiet`).
- **Emotional slot ✓:** the first chapter of "yearning without sex". The romance is kept warm in small beats while the emotional weight moves to two women and two losses.
- **Value shift ✓:** jealous and outside (−) → the bracelet (+) → friendship (+) → a plan (+) → doubt (−). In Delphi: leaving (−) → mended (+).
- **Pull ✓:** a real question, unanswered, with the games next.
- **Slow patches:** C1's archive politics and C4's boards and seals. Both are load-bearing for Ch.17; the PATH trims around them, not through them.

**Verdict: OK.**

---

## Cross-Book Pattern Detection (Ch.1–16)
1. **What the gates cannot see has moved to whole short lines and stop-word frames.** "She does that.", "For the sheet.", "Go to sleep.", "All of it?" and "Some." are each a whole spoken sentence carried from an earlier chapter. The echo scan drops them by design, because every word is a stop word. Likewise "every ending" / "every word set down" survive as a frame in fresh nouns.
   **Proposal (UPDATE RULE, root `tools/tic_report.py` and the template):** a **short-line registry**. Any whole spoken sentence of ≤5 words that is not a stock word (yes, no, then, good, now, a name), and that appears as a whole spoken sentence in an earlier chapter, prints as an echo. My scratch implementation is `xgram.py` in the scratchpad.
2. **Held beats filled by weather, steam or a lodger's movement** came back three times in one chapter, after "0 more anywhere" (Ch.10). The shape is regex-able: a one-sentence narration of motion, weather, sound or steam wedged between two quotations by the same speaker. Add it to the gate as a WATCH.
3. **The adjacent chapter is the likeliest source of reuse.** Five of the six reused beats came from Ch.15 (turf cold, dawn sequence, summit sun, the single bark, the bed's words). The Ch.10 rule ("list the previous chapter's set pieces and stage the new one differently") is being applied to set pieces, not to the incidental ambience around them. **Extend it to ambience:** dawn, night sounds, animals at the edge of a scene.
4. **The deliberation-pause class misses its commonest forms.** "She was quiet for a little", "sat quite still", "said at last", "stared that way for some time" and "took longer over it" all read 0 at the gate (audit I-34 counted the duration family at 5). Widen `tic_report.py`'s pause regex to `quiet for a (little\|while)`, `(sat\|stood\|was) quite still`, `said at last`, `for some (time\|while)`, `took longer over`.
5. **What varies, as it should:**
   - the structure (Parallel after Chronological);
   - the opening (`dialogue`) and ending (`question`);
   - the gear (mid);
   - the dialogue share (44%, the book's highest yet);
   - the anchor type (a child's tooth marks; weeping through a curtain: new);
   - the body-rebel channels (a blush; tears and a laugh breaking from another woman).

**Bookkeeping (orchestrator):**
- **Re-sync the bible's Ch.16 blocks to the final page** (audit I-37). They still quote the Writer's draft:
  - "She went a whole winter without my name." (page: "She had me most of an autumn before she wanted my name.");
  - "Twice she had asked him to sit, and twice he had said that he would stand." (page: "There is a stool, Valens," … "I'm well here.");
  - "You said the Gaius as though somebody might take it back." (page: "quickly, in case somebody should take it back");
  - "Then you are the first," (page: "That would make you the first,");
  - "And after the hour?" (page: "When the hour was out?");
  - "for the last hand's breadth" (page: "at the very end");
  - "She looked at the thing at my face, and then past it, at her lamp" (page: "She looked at her lamp");
  - "received him with great kindness" (page: "with every kindness");
  - "the mosaic man who laid his little stones drunk" (page: the floor-layer);
  - the porter "with a stool and a tablet" (not on the page).
- **After the PATH, also sync:**
  - "She does that." → "She's done it before.";
  - "Go to sleep" → "Shut your eyes";
  - the proconsul's wife and her cough are off the page;
  - Myrrhine's "fuller's wife" → "rope-maker's wife";
  - "Not much. Some." → "Not much.";
  - the Corinth porter is introduced by his line only.
- **At-risk after Ch.16, add (post-PATH):**
  - **the delivery frame** (a speaker's words set or laid down singly; endings given weight or sounded to the last letter): CLOSED (Ch.5, Ch.6);
  - **"[verb] quite still"**: CLOSED at 2 (Ch.5, Ch.15);
  - **a dog barking once into a silence**: SPENT (Ch.15);
  - **first sun on any peak at dawn**: SPENT (Ch.15);
  - **dawn light inventoried in sequence**: SPENT (Ch.15);
  - **"a lodger's [garment] on the rail above"**: CLOSED (Ch.10);
  - **"kept [poss] face to"**: inside the CLOSED gaze-hold;
  - **Myrrhine** (if she returns in Ch.17): no price figure in her mouth, no lupins (both used);
  - **Plautia** (Ch.17, Ch.22): her period-then-blunt-question never twice running in one skeleton, and the narrator never names it;
  - **Valens's back to the wall**: 2 book-wide (Ch.13, Ch.16 C3), WATCH;
  - **"And yours?"**: 2 book-wide, no third;
  - **Parallel chapters (Ch.22, 35, 38):** the narration never pre-describes an image the other strand will dramatize.
- **Entity / continuity cascades:**
  - Felix has seen the flashlight (l.419); its batteries are near the end ("Don't spend it on mules.").
  - The Seiko and the bracelet will both sit on the left wrist in Ch.18 (audit I-29).
  - Celer's whereabouts at the games are fixed by Plautia (second row, behind the governor's chair). Outline Ch.17's colonnade meeting must account for him leaving it (audit W-14).
  - The suit is registered as Rome, "two years from this spring" (ARCH-5 ✓; Ch.15 audit I-20 closed).
  - Valens is to stand "by the baker's oven" or at the Isthmus horse fair, unresolved. Ch.17 decides on the page.

---

## VERDICT
**POLISH. Gate NOT MET.**

| Measure | Result |
|---|---|
| Genesis Floor | **8.0** (Prose & Voice, merit; no cap) |
| Average | **8.71** |
| Casual | **9.0** |
| Pacing | **OK** |
| CVI-Launch (CVI-L) | **9.7** |
| CVI-Legacy | 6.9 (provisional) |
| Mechanical suite | all clean (echo 0, tic gate clean, voice-wear strict clean, shape CLEAN) |
| Foreshadowing / own outcome narrated | **0 by gate; one stance slip by hand** ("a low coast I never saw" → L3) |
| AUTHOR-CP3-5 (triumph games, never "Isthmia") | ✓ |
| AUTHOR-CP3-3 (pregnancy gap unremarked) | ✓ |
| Plautia not a rival-trope | ✓ (strongly) |
| Kallia's farewell: no speech, no proverb | ✓ |
| Non-negotiables (himation, sweep and broom, lamp frame, Isthmus plan) | ✓ all four |
| Memory triggered by the scene | ✓ (one clause; returns at once) |
| Explanation-density cap | ✓ (4 firm, 0.53/1k) → 3 after the PATH |
| Paragraph-final negations | 9 (1.19/1k) ✓ → 7 (0.97/1k) |
| No comparisons in Valens's speech | ✓ |
| Command echoes | 0 ✓ |
| Tics | verbal catchphrases 0; gate classes clean; **carried-over spoken lines 2 + 4 stock → 0; pause cluster, Myrrhine's lupins, Plautia's named formula → fixed** |
| Reuse (the Ch.5/6 delivery frame ×4; six Ch.10/15 beats; samples ×3) | **FAIL** → cleared |
| SPENT held-beat fillers | **FAIL ×3** → 0 |
| Parallel rhyme | not mechanical ✓ (one pre-description → R18) |
| Ledger | ✓ on every hard field |
| AI patterns | 8/20 (clean band) → 8/20 at a lower penalty |

**Failing dimension:** Prose & Voice (8.0 on merit). The fixes are surgical and were tested together: L1–L5, C1–C13, R1–R29 (51 strings). The result is 7,203 words, dialogue 45.7%, median 14 and every gate clean; the first line, the closing question and every anchor line are unchanged. Then run E (gates) and F (re-evaluation). **Expected after one cycle: Floor 8.5 / Average 8.86 / Casual 9.0 / PASS.**

The chapter does what the outline asked and more. The woman the book has been dreading for ten chapters arrives as a mother whose hooks are empty. She asks one blunt question, gives away the one thing she still wears, and weeps behind a curtain while her maid haggles over it. Meanwhile, at Delphi, Kallia says goodbye with a needle, a broom and a lamp she lets burn all night. What holds it below the gate is small and countable. The narrator keeps describing speech in an earlier chapter's way. Two characters borrow lines that belonged to someone else. And three times a pause is filled with weather or steam, a habit the book had retired.

**BIAS CHECK:** This evaluation was produced by the same system that wrote the prose. Confidence in scores above 8.0 requires external validation (beta readers, editors, comp analysis).
- **The delivery-frame finding (R1) is a judgment about a frame, not a string.** No gate sees it. A reader who holds that describing someone's careful Latin is simply what a narrator does would call R1 polish, not law. I count it because Ch.16 rebuilds the same three components four times (words set or laid down singly, endings given full weight, every word), and two of them sit within a word or two of Ch.5's herald.
- **"She does that." is three stop words.** A reader could call it too ordinary to own. I count it because it is the whole sentence, it does the same job (one character explaining another woman's habit to Mara), and it comes three chapters after Kallia's.
- **Characters 8.5 → 9.0 is my forecast, not a score.** It assumes C1–C13 land as written. A re-evaluator may hold 8.5 on Plautia's fingerprint still being frequent (it is her card), or on the two stock short lines I left.
- Originality, Theme, Emotion and Immersion at 9.0, Casual 9.0 and CVI-Launch 9.7 are one-chapter judgments by the system that wrote the book.

---
---

# Re-evaluation after cycle 1
**Evaluator:** book-evaluator (independent; did not write, polish or apply any of this prose) | **Date:** 2026-10-21
**Text evaluated:** `manuscript/chapters/chapter-16.md` after polish cycle 1, sha256 `3fc626eb…` / md5 `eb8769d9…`. That is **byte-identical to the tested fixed copy** of the first evaluation (`ev16/ch16-fixed.md`), so all 51 swaps are on the page exactly as tested.
- **Length:** 7,203 words (shape_check), 7,210 (style), 7,858 (`wc -w`).
- **Read against:** the book's CLAUDE.md; STATE.yaml guardrails, including **AUTHOR-CP3-3**, **AUTHOR-CP3-5** and **AUTHOR-END-1**; voice-dna §0–§8; character-bible.md (the MARA, VALENS, KALLIA, FELIX, PLAUTIA, MYRRHINE, MARCUS and ARISTON cards, the Ch.16 walk-on note, every at-risk and spent block); outline `## Chapter 16` and Ledger row 16; the cycle-0 evaluation above.
- **My own scans:**
  - a word-level diff of the cycle-0 page against the cycle-1 page (all 73 changed spans);
  - every new string grepped against Ch.1–15 and all 13 voice-bank samples, **stop-word-bounded strings included**;
  - **every whole spoken sentence of five words or fewer, 1–2-word lines included**, checked against every earlier chapter's speech (the gate's spoken-line layer starts at three words);
  - in-chapter doubles around every swap (verb, noun and root families);
  - paragraph-final negations, #11 and the pause and gesture classes by hand;
  - CP3-3, CP3-5, END-1 and the foreshadow families by grep and by reading.

*(l.N = line number in the cycle-1 `chapter-16.md`.)*

## HEADLINE
**CVI-Launch:** 9.7 | **CVI-Legacy:** 6.9 (provisional) | **Genesis Floor:** **8.5** | **Genesis Average:** **8.86** | **Casual:** **9.0**
**Engagement type:** Empathy 55 / Fascination 30 / Self-insertion 15 (unchanged).
**Divergence alert:** none (9.7 − 8.5 = 1.2).

**Gate: PASS.**
- Floor 8.5 ✓; Casual 9.0 ✓; pacing OK ✓; `check_chapter.sh 16` clean ✓.
- It passes with **eight finalize fixes (F1–F8)**, tested together and listed below.
- Five of the eight (F2–F6) undo repeats that the cycle-1 swaps themselves moved sideways. The brief asks for "nothing new", so that check **did not fully pass**. Each of the five is a word-level double inside one paragraph or speech, not a frame, a device or a gated class. None of them holds a dimension.

## Did the 51 swaps introduce anything new?
| Check | Result | Evidence |
|---|---|---|
| **Added explanation** | **None** ✓ | #11 firm count fell from 4 to **3 (0.42/1k)**. No swap adds a clause that unpacks a gesture or a line. R7's "The court grew light, and the flame on the sill went from being the brightest thing there to being only one of the things in it." is observation, not gloss. |
| **New triad** | **None** ✓ | R10 makes three short sentences in Valens's mouth ("I went for barley. The porter on the colonnade is the proconsul's. The baker's not."). That is a deadpan sequence, not a list and not anaphora. Automatic triads fell from 4 to 2 (l.145 thorn / scree / fold; l.235 bed / window / lamp). |
| **Echo of an earlier chapter** | **None introduced** ✓ | The echo scan reads 0, and my grep of every new string against Ch.1–15 and the samples finds nothing. **Two pre-existing carry-overs that cycle 0 missed are now caught**, and both are cut in finalize: **F1**, Felix's "What's that?"; and **F6**, "He could not stop", which is **Ch.15 l.548's** "could not stop" for this same laugh and also sample-09's laugh frame. Cycle 0's R12 took "for some while" off that sentence but left the verb phrase. |
| **Repeat moved sideways** | **FAIL ×5 → cleared by F2–F6** | See below. |

**The five sideways repeats, each made by a swap:**
1. **R14b** "She **carried** the broom back to the lean-to" lands four sentences after "She came out **carrying** the broom." (l.263) → **F2**.
2. **L3** "off a **dark** coast" shares its paragraph with "Valens's voice in **the dark**" (l.407). D3 now carries "dark" four times → **F3**.
3. **R28** "her eye **rolled** white" (l.413) is the fourth roll-word in D3, after "against the roll", "with every roll" and "rolling on a long swell" → **F4**.
4. **R13** cut "Felix lay down again on his rope." and so left '"Shut your eyes," **said Valens.**' immediately before "**Valens** stayed by the black" (l.427–429) → **F5**.
5. **R12** "it **broke under us**" (l.373) comes one sentence after "a bed **fell in under us**". The same sentence also keeps "we **went to the floor**", which l.513's cup repeats ("The cup went to the floor by her chair") → **F6**, together with the Ch.15 "could not stop" above.

**What the swaps fixed, verified on the page:**
- **The Ch.5/6 delivery frame: 0.**
- **Spoken lines borrowed from earlier chapters: 0** ("She's done it before.", "The sheet was to come from…", "Hand it over", "Every bit?", "Shut your eyes,", "Not much.").
- **SPENT held-beat fillers: 0** (the rain rope, the fuller's vat and the lodger's cough are gone).
- **The Ch.10 and Ch.15 ambience beats: 0** (the turf cold, the dawn sequence, the summit sun, the single bark, the rail above, Felix lying down).
- **CLOSED-family siblings: 0** ("quite still", "kept her face", the lit inventory).
- **Voice-bank strings: 0.**
- **The stance slip: gone** ("a low coast I never saw").
- **Logic L1–L5: fixed** (the brother's slaves; the light source; three years; the merged speech).
- **Characters:**
  - Plautia's skeleton no longer runs twice (C2), and the narrator no longer names it (C3).
  - Her pause cluster is broken (C4–C6).
  - Myrrhine's lupins now appear in two scenes, C1 and C4 (C8).
  - Valens's voice is tagged "low" once (C9), and he is off the wall in C4 (C10).
  - Pricing is Myrrhine's alone (R29).
- **Anti-AI: 8/20 at −1.125** (from −1.625).

## The echo-scan line, judged
`tic_report.py --echoes 16` lists **"what is it"** (Ch.1, Ch.7).
- **On its own it is stock English in other mouths and other jobs.**
  - In Ch.1 l.87 it is Szabo's intercom ("Yes? What is it?" = *what do you want?*).
  - In Ch.7 l.116 it is Mara asking about the tooth powder.
  - Alone, I would leave it.
- **But it is fused to a real pattern the scan cannot see.** At l.415 Felix opens with **"What's that?" … "What is it?"** at the flashlight. Felix has reacted to Mara's strange object with "What's that…?" in:
  - Ch.11 l.432 ("What's that, writing?"), at the sherd;
  - Ch.12 l.250 ("What's that? Is it silver?"), at the camera;
  - here, at the flashlight.
- **Book-wide, the whole sentence "What's that?" occurs four times:** Kallia in Ch.5 l.317, Felix in Ch.12, Theano in Ch.13 l.452, and Felix in Ch.16. Counting the Ch.11 variant, it has five uses.
- **His card's bleed guard says "no catchphrase … repeated".** This is the same trigger and the same opener, in the same mouth, for the third time.
- **Why it does not cap Characters at 7.5:**
  - his exact whole line has occurred twice (Ch.12, Ch.16), with one variant;
  - it is the most ordinary question in English;
  - it does not distinguish him: his mark is the stack, not its first two words.
- **Severity: INVESTIGATE → fix.** **F1** cuts both "What's that?" and "What is it?". The stack now opens on "Where's the flame?", which is fresh. The `--echoes` layer then reads **none**.
- **Registry entry for the bible:** "What's that?" as a reaction to Mara's object is CLOSED at 4 on the page (Ch.5, 11, 12, 13), with no fifth for anyone.

The 1–2-word sentences the gate's spoken layer skips:
- **"I did."** (Valens; Ch.11 l.128 inside a longer line): an anchor pair here ("You asked for it." / "I did."). Kept.
- **"Not much."** (Ch.1 l.315; Mara here): stock, kept as cycle 0 ruled.
- **"And yours?"** (Ch.13 Theano; Plautia): 2 book-wide, no third.
- **"And you?"** (Ch.6, Ch.11; Plautia l.89): **4 chapters, cap reached.** No fifth.
- **"My wife,"** (Ch.15 l.340; Ch.16 l.467): Ch.15 has Valens planning the word for the porter; Ch.16 has him say it to the porter. That is the situation arriving, not a line landing again: it is the only word for the fact. Kept, and logged so it is never said to a gatekeeper a third time.

## Genesis Score (cycle 1)
| Dimension | Cycle 0 | **Cycle 1** | Δ | Evidence | Cap / hold |
|---|---|---|---|---|---|
| Originality | 9.0 | **9.0** | 0 | Unchanged elements: the ex as a supplicant mother; the empty hooks; a baby's teeth in the gold; the maid's buy-back during the weeping; the bodyguard's protocol on the porch; mules that cannot vomit; the mended himation. R18 now lets the two strands converge on D3's stair image once, fresh ("each time from behind and at a distance", l.21 → l.469). | Not 9.5: the Parallel frame and the heist-planning shape are genre-standard. |
| Theme | 9.0 | **9.0** | 0 | "What is owed to the people you leave" is carried by acts: the obol, the night's mending, the lamp pinched out, "Twice in three years". The close is a real question (l.583). The texture that means nothing survives: the scorpion and its brother, the floor laid drunk, the Sicyon match "with a vineyard and a cough", the mastic, the dun in the cabbages, Ray on the ferry. | Not 9.5: the gift motif is still dense. |
| Characters | 8.5 | **9.0** | +0.5 | Every Characters hold from cycle 0 is cleared on the page: Valens speaks his own line ("She's done it before.", l.303, the bodyguard's knowledge of her habit); the two "charcoal" mornings no longer share a skeleton (l.157 period + question; l.161 a bare question); the narrator no longer names Plautia's habit (l.155); no pause cluster ("Does he laugh? Your husband." is folded into her speech, l.367; "she said.", l.377); Myrrhine's lupins are in two scenes; Valens is tagged "low" once (l.407) and is not against the wall in C4 (l.477); Felix asks about the bracelet's weight, not its price (l.311). Cover-the-name passes for all six speakers. Mara's chaos is 4/4. | **Held at 9.0, not 9.5:** Felix's "What's that?" opener (F1, above); Plautia's "And you?" / "And yours?" four lines apart, both stock lines at their caps. **The gate's gesture numbers:** object handling 1 (the cup); the jaw class 1 (the dun's jaw, cupped); every other class 0. |
| **Prose & Voice** | 8.0 | **8.5** | +0.5 | **Earned on 51 cited changes:** the narrator's delivery frame gone (l.33 "It was book Latin, slow, with the verb held back for the end"; l.35 "Mine came out stiff."; l.535; l.583); no SPENT filler; no ambience beat from Ch.15; no CLOSED sibling; no sample string. **Stopping sentences intact:** "Someone had cut his teeth on it." (l.231); "Toward the second corner they grew a fraction longer, and then, at the very end, small again." (l.259). **Underlines intact:** "her face was wet and perfectly composed"; "Which was true."; "Behind him the street might have been a wall."; "Felix, who could, was sick into the sea for the lot of them."; "one night's burning laid over years of others". **Ugly sentence intact** (l.153). **Voice under pressure intact** (the night at sea, the curtain). | **Not 9.0:** the five sideways doubles (F2–F6); "could not stop" in Ch.15's words (F6); and cycle 0's slow patches, which are prose-adjacent. The +0.5 cap would also bind. |
| Pacing | 8.5 | **8.5** | 0 | Every hard field of the ledger row is still hit: Parallel; `dialogue` → `question`; 6 breaks; dialogue 45.7% (40–50); median 14 (mid); 7,203 against 7,600. One Devourer slow spot is lighter: the second charcoal morning lost its 33-word period about the proconsul's wife (C2). | **Not 9.0:** C1's record-office politics (l.57–77) and C4's boards, cord and seals (l.535–551) are unchanged by design. They are load-bearing for Ch.17. |
| Emotion | 9.0 | **9.0** | 0 | The anchor is byte-identical: "You admired it." / "The smoke has got into my eyes." / the curtain / Myrrhine's drachma / the marks / "On the left." The surprise is the jealousy turning to friendship over the broken bed and Plautia's laugh (l.373–375). The body rebel: the blush, Plautia's tears, her laugh, Felix at the rail. | Not 9.5: Mara's own feeling at Kallia's farewell is withheld. That is the design, and it costs fast readers the goodbye. |
| Immersion (Dim 7) | 9.0 | **9.0** | 0 | All three cycle-0 fact slips are fixed: the light source (l.267 "its shutter ajar"), the three years (l.185), and the cold fullers' vat (gone). The period bones are intact: the proconsul's office on the long colonnade; the actio rei uxoriae; the magistrate's sealed boards on a cord; Gaius Iulius Valens; Lechaion's moles; the brailed sail; mastic. | **Held at 9.0, not raised:** the cuts also removed some period texture (the steaming vat, the proconsul's wife's remedies, the lupin skins under the stool). Clearing the slips restores 9.0; it does not lift it. |
| **FLOOR** | 8.0 | **8.5** | | Prose & Voice, Pacing | |
| **AVERAGE** | 8.71 | **8.86** | | (9.0 + 9.0 + 9.0 + 8.5 + 8.5 + 9.0 + 9.0) / 7 = 62.0 / 7 | |

**Per-cycle rule:** no dimension moves more than +0.5. Characters and Prose each move +0.5, on 13 and 51 cited changes respectively.

## Anti-AI Scan (cycle 1; 7.20k; commercial band)
- #1 forced symmetry: **minor**, 3 (0.42/1k): the ears / temper pair, "He'd want in." / "He'd stay in." (designed), "held his look, and he held hers". **−0.125**.
- #3 rule of three: **minor**, 2 automatic (0.28/1k). **−0.125**.
- #8 parallelism: **moderate**, 5 (0.69/1k): the oven / door pair, "until he had looked, and until he had moved", the look pair, "This is the suit. The suit is…", Plautia's repeat-back of Myrrhine's list (witty). **−0.25**.
- #9 smooth transitions: minor (the Parallel's time stamps). **−0.125**.
- #11 explanatory extension: **minor, 3 firm (0.42/1k)**:
  - "She had caught the cloak and the cook, and no more.";
  - "where she could not go over again without going over onto him";
  - the bow (l.573).
  - The cap (commercial >6 or >0.8/1k) **PASSES**. **−0.125**.
- #15 authoritative description: minor (the record office's two doors). **−0.125**.
- #16 philosophical asides: minor, 2, both in Plautia's mouth and in character. **−0.125**.
- #17 clean dialogue: minor (C2's run from l.171 to l.201). **−0.125**.
- Clear: #2, #4 (em-dash 3, all cut-off speech), #5, #6 (narration 0; speech-paragraph "And" openers 3), #7, #10, #12, #13, #14, #18, #19, #20.
- **8/20, −1.125, clean band** (cycle 0: 8/20, −1.625). The finalize set leaves this unchanged.

## The book's own laws (cycle 1 page; the finalize copy agrees)
- **NO FORESHADOWING: PASS.** The gate reads 0. By hand: "I never saw" is gone; "never again", "last time", "years since", "even now", "I still" and "would learn" are each 0. AD 79 / "seventy-nine" is 0. "Pompeii" is 0.
- **AUTHOR-CP3-5: PASS.** "At the games for Titus's triumph," Plautia said (l.473) is byte-identical. "Isthmia" and "Isthmian" are 0. The festival is "the games" and "the god's precinct on the Isthmus", and the race is "the boys' race" (l.513 now reads "after the boys' race").
- **AUTHOR-CP3-3: PASS.** "pregnan", "with child", "my month" and "my blood" are each 0. "most nights since July" and "Every night, lying beside him" do not count the months. The nursing bracelet is never linked to a child of Mara's.
- **AUTHOR-END-1: PASS.** None of Ch.15's door or camera lines is quoted, near-quoted or recalled: "wait outside", "keeps what it shows", "bring it out", "see it open", "believe it", "know the door", "go in by it" and "everything is kept" are each 0. The lamp frame is shot, not described as kept. The camera is not explained to Kallia.
- **Kallia's farewell: PASS.** No speech in D2; no wool; no stopped work; no "had gone quiet"; she never sits, never touches Mara and hands her nothing. The broom's position is not described ("Two strokes more along the sill.").
- **Memory triggered by the scene: PASS.** One clause (the drugstore bands, Gloria's Ray), triggered by the dun's head in her arms, returning at once ("The dun groaned again.").
- **Paragraph-final negations: 7 (0.97/1k)** ✓ (from 9).
- **Command echoes: 0.** "Shut your eyes" now has no shown compliance.
- **No comparisons in Valens's speech: PASS** (the new lines "She's done it before." and "I went for barley. … The baker's not." included).
- **NO TICS:** verbal catchphrases 0; gate classes clean; one forming opener (Felix, above) → F1.
- **Retired reflexes:** no define-by-negation opener; no performed candour; no button; no closing aphorism; and-chains 5/9; "as if / as though" 1 (Plautia's laugh); semicolons 18 (2.5/1k).

## Character Chaos (Mara): unchanged, 4/4
- **Irrelevant thought:** the seasickness bands (l.401); the bronze "worn bright at the bend" (l.51).
- **Cognitive distortion:** the cakes loop (l.21).
- **Unprompted, triggered memory:** the bands.
- **Failed management:** the blush, which Plautia watches; "Lady, I only—"; the lie caught.
- **Voice under pressure:** demonstrated.

Every secondary character still has an independent moment, so there is no cap.

## The Tomorrow Test
**What the reader remembers:**
- the gold band with a baby's tooth marks near its clasp;
- "Someone had cut his teeth on it.";
- the weeping behind the red curtain while the maid offers a drachma;
- Kallia's lamp left burning on the sill all night, then pinched out with wet fingers.

**Anchor type:** BOTH. **ANCHOR EXISTS (strong, +0.5 CVI).** Every anchor line is byte-identical to cycle 0 (12 of 12 checked by script).

**Shareability:** unchanged ("the woman he was supposedly sleeping with is a mother who gives everything away; she gives Mara her bracelet, goes next door and cries, and the marks on it are her baby's first teeth").

## Reader Reports (cycle 1)
### The Devourer
- **What has lightened:**
  - the second charcoal morning is one line now ("Were you afraid of him, at the beginning?" she said on the second.);
  - the porch arrival no longer re-explains the porter;
  - the night at sea runs cleaner without Felix lying down again.
- **Still slow:** C1's archive politics and C4's seals.
- **Would they stop?** No. **Last page:** the question is real, and the games are next. They turn.

### The Critic
- **Underlines:** all of cycle 0's, intact.
- **What no longer disappoints:** the herald's frame, Kallia's borrowed line, the weather in a pause, last chapter's summit and dog.
- **New disappointments, all small:**
  - "She carried the broom back" four words after "carrying the broom";
  - "a bed fell in under us … it broke under us";
  - "He could not stop.", the laugh in Ch.15's words.
- All three are cleared by F2 and F6.

### The Hostile
- **The cycle-0 complaints are answered:** the pronoun, the light, the years, the vat, "I never saw".
- **One new question:** "The sheet was to come from Euthydikos's people" (l.141) reads as if the priest's household would supply the papyrus. The page means his fee would buy it, against Kallia's obol. It is readable, and less clear than the line it replaced.
  - **No change:** every clearer wording I tried trips a gate or the cycle-0 "Do not use" list ("I meant to buy the sheet", "to buy the sheet").
  - Logged so that Ch.17 or Ch.18 never re-explains the obol.

### The Casual Reader (airport, 10 pages)
- **Unchanged:** "Have you seen his back?" and the blush hook them.
- **They cry** at the bracelet and the curtain.
- **They laugh while crying** at the maid's drachma.
- **Frictions:** the proconsul and the freedmen; the cord and the seals.
- **Would they buy after 3 pages?** Yes. **Do they stay?** Yes. **9.0/10.**
- **Not 9.5:** the same two frictions, and a goodbye to Kallia that a fast reader may not register.

### The Devoted Reader
- **Will post about:** the same items as in cycle 0.
- **Will catch on this page:** Felix's third "What's that?" and the bed laugh in Ch.15's words.
- **After finalize:** nothing.

## Cross-Reader Matrix (cycle 1)
| Issue | Devourer | Critic | Hostile | Casual | Devoted | Severity |
|---|---|---|---|---|---|---|
| F2–F6 sideways doubles made by the swaps | | ✓ | | | | INVESTIGATE → **fix** (cheap, tested) |
| F6 "could not stop" (Ch.15 l.548, sample-09) | | ✓ | | | ✓ | SHOULD FIX → **fix** (no reuse) |
| F1 Felix's "What's that?" opener (third time in his mouth) | | ✓ | | | ✓ | SHOULD FIX → **fix** (tic budget 0) |
| F7, F8 pre-existing doubles ("the flat land" ×2; "some time" ×2) | | ✓ | | | | INVESTIGATE → **fix** (cheap) |
| The sheet line's clarity (l.141) | | | ✓ | | | INVESTIGATE → **no change** (no gate-clean alternative) |
| C1 politics / C4 seals | ✓ | | | ✓ | | SHOULD FIX → **no change** (load-bearing for Ch.17) |

## Pacing check (one line for `feedback/progress.md`)
**Ch.16 (cycle 1 + finalize):** Parallel *two places, two farewells* · **7,175 words** (shape_check; target 7,600, −5.6%, not padded; ≥7,100 ✓) · dialogue **45.7% / 46** (40–50 ✓) · **median 14** (mid ✓) · 6 breaks ✓ · `dialogue` → `question` ✓.
- **Neighbours:** Ch.15 7,479w high gear (16), 35% → **Ch.16 7,175w mid (14), 46%** → Ch.17 7,400 planned, low gear, 30–40%. The three long chapters still differ in gear and dialogue share; Ch.18 (2,800) breaks the run.
- **Book:** 89,779 words against about 96,400 cumulative target (−6.9%). Projected about 242k against the 220k floor ✓ and the 245k target (slightly under: watch, never pad).
- **Emotional slot ✓:** the first "yearning without sex" chapter after the heat chapter.
- **Value shift ✓:** jealous (−) → bracelet (+) → friendship (+) → plan (+) → doubt (−); Delphi: leaving (−) → mended (+).
- **Pull ✓:** a real question, unanswered.
- **Verdict: OK.**

## CVI
- **CVI-Launch 9.7,** unchanged: Commercial Pacing 8, Tomorrow 10, Casual 9, Shareability 9.2, Pitch 10, Closeness 10 → 9.24 + 0.5. No fix touches an anchor.
- **CVI-Legacy 6.9** (provisional; default weights), unchanged.

## Finalize fixes (F1–F8), tested together
**Script:** `/tmp/claude-0/-home-user/63791ee5-159c-5791-9429-07920f8d9417/scratchpad/re16/ch16-finalize.py` (run from /home/user/Books):
```
python3 /tmp/claude-0/-home-user/63791ee5-159c-5791-9429-07920f8d9417/scratchpad/re16/ch16-finalize.py \
  books/the-hour-of-ash/manuscript/chapters/chapter-16.md \
  books/the-hour-of-ash/manuscript/chapters/chapter-16.md
```
- **Base:** the cycle-1 page (sha256 `3fc626eb…`). The script asserts exactly one match per string and aborts without writing on any miss.
- **Harness:** `re16/ch16-reeval-swaprun.sh` in the same scratchpad. It swaps the fixed copy in, runs the command from /home/user/Books, and **always restores the cycle-1 page from `re16/ch16-cycle1.md`**. Do not use cycle 0's `ch16-eval-swaprun.sh`: it restores the *pre-polish* original and would undo all 51 swaps.
- **Restore verified:** after every run the manuscript checksum printed `3fc626eb…`. I did not edit the manuscript.

| # | Location | Problem type | Now (cycle 1) | Why it fails | Replace with (exact) | Project rule? |
|---|---|---|---|---|---|---|
| F1 | l.415 | Voice (forming opener; `--echoes` hit) | `"What's that?" Felix had raised himself on an elbow on the coil of rope he slept on. "What is it? Where's the flame?` | Felix's "What's that…?" at Mara's object: Ch.11, Ch.12 and here (5 book-wide); "What is it?" is the echo-scan line (Ch.1, Ch.7). | `Felix had raised himself on an elbow on the coil of rope he slept on. "Where's the flame?` | Yes: "What's that?" CLOSED at 4 |
| F2 | l.263 | Style (double made by R14b) | `She carried the broom back to the lean-to and hung it from its nail beside the fire, and went to the jar for water.` | It comes four sentences after "She came out carrying the broom." | `She hung the broom back on its nail beside the fire, and went to the jar for water.` | No |
| F3 | l.407 | Style (double made by L3) | `off a dark coast, rolling` | "in the dark" is in the same paragraph; dark ×4 in D3. | `off an unlit coast, rolling` | No |
| F4 | l.413 | Style (double made by R28) | `In the light her eye rolled white,` | It is the fourth roll-word in D3. | `In the light her eye showed white,` | No |
| F5 | l.427–429 | Style (double made by R13) | `"Shut your eyes," said Valens.` / `Valens stayed by the black, and presently he spoke across her.` | The name twice running across a break. ("He stayed by the black" was tried first: it made the 3-gram "said valens he", Ch.11 l.444.) | `"Shut your eyes," said Valens.` / `Presently, from beside the black, he spoke across her.` | No |
| F6 | l.373 | Style (double made by R12) + reuse | `It was the herdsman's own bed, and it broke under us, and we went to the floor with the fleeces on top of us. He laughed then. He could not stop."` | "under us" twice in two sentences; "went to the floor" again at l.513; "could not stop" is Ch.15 l.548's verb phrase for this same laugh (and sample-09's laugh frame). | `It was the herdsman's own bed, and it put us on the floor with the fleeces on top of us. He laughed then."` | Yes: a retold scene is grepped against its source chapter *including stop-word frames* (cycle 0's R12 checked content words only) |
| F7 | l.441 | Style (pre-existing double) | `rising from the flat land behind the town, the great rock` | "the flat land" again at l.459, which keeps it. | `rising behind the town, the great rock` | No |
| F8 | l.455 | Character (duration pause) + double | `Felix stared that way for some time.` | "after some time" at the curtain (l.215); a duration pause the gate cannot classify. | `Felix stared that way.` | No |

**Gate-tested and rejected:**
- "He stayed by the black": echo with Ch.11, "said valens he".
- "all at once": a third use book-wide (Ch.4, Ch.5).
- "back to the lean-to": an in-paragraph double.

**What the tested run produced** (all 8 together; finalize copy sha256 `63a1dac0…`, md5 `ed750988…`):

| Measure | Cycle 1 | **After F1–F8** |
|---|---|---|
| Words (shape_check / style / `wc -w`) | 7,203 / 7,210 / 7,858 | **7,175** / 7,181 / 7,830 (≥ 7,100 ✓) |
| Dialogue (show/tell / shape) | 45.7% / 46 | **45.7% / 46** ✓ |
| Median (shape / metaphor) | 14 / 14 | **14 / 15** ✓ |
| Breaks / signatures | 6 / `dialogue` → `question` | unchanged |
| `bash books/the-hour-of-ash/tools/check_chapter.sh 16` | clean | **all clean**: style (simile 1.0/1k, em-dash 3, foreshadow 0); grammar 0 errors; rhythm 0; show/tell no flags; voice-wear strict clean; tic gate clean (and-chains 5/9, credential asides 1, negation pivots 0); **echo 0**; command echo none; metaphor 1.4 fig/1k; shape CLEAN |
| `tic_report.py --echoes 16` spoken-line layer | "what is it" (Ch.1, Ch.7) | **none** |
| `shape_check --strict` | CLEAN | **CLEAN** (`16 7175 6 46 14 dialogue question`) |
| Gesture classes (Ch.16) | object handling 1, jaw 1 (the dun's) | **unchanged**; book-wide counts identical |
| Paragraph-final negations | 7 (0.97/1k) | 7 (0.97/1k) |
| #11 firm | 3 (0.42/1k) | 3 |
| First line, closing question, the triumph-games line, every anchor line | | **byte-identical** (12/12 by script) |

After applying the script, update the chapter's word-count header comment. Lines 3–8 still describe the Writer's draft, and the SCENE BUDGET still quotes the retired line "She does that.".

## Character-bible Ch.16 re-syncs (PASS → do these at finalize)
Each item gives the bible line, the stale text, and **→** the final-page text (after F1–F8). Every quote below was checked by script against the finalize copy. These cover the dialogue-polish, disruptor, continuity-repair, polish-cycle-1 and finalize passes, because **every Ch.16 block in the bible still quotes the Writer's draft**.

**VALENS card, "Ch.16 as written" (l.862–889).** Retitle the block "SYNCED to the FINAL page".
1. l.866 "You said the Gaius as though somebody might take it back." → "You said the Gaius quickly, in case somebody should take it back."
2. l.871–872 "In C4 he stands inside the door with his back to the wall by the jamb and will not sit ("Twice she had asked him to sit, and twice he had said that he would stand.")" → "In C4 he stands just inside the door and has not sat in that room ("There is a stool, Valens," … "I'm well here.", twice)". **Back to the wall in Ch.16: 0** (the porch beat is "stood aside against the house wall"). Book-wide WATCH: 2 (Ch.13 and the Ch.16 porch).
3. l.873 "She does that. Give it to her woman tomorrow…" → "She's done it before. Give it to her woman tomorrow, early, and say nothing to her about it. She'll be sorry by dark."
4. l.874–877: "Near the forum." stays; the office's two doors stay. Add the new evasion line: "I went for barley. The porter on the colonnade is the proconsul's. The baker's not."
5. l.879 "Go to sleep," → "Shut your eyes,". Add: voice tagged "low" **once** (l.407 "Valens's voice in the dark, low."); the second tag was cut.
6. l.886 Spent: "She does that." → "She's done it before."; add "Shut your eyes,", "The light.", and "There's only the one.".

**KALLIA card, "Ch.16 as written" (l.1201–1226).**

7. l.1209 "then, for the last hand's breadth, small again." → "then, at the very end, small again."
8. l.1216 "Two strokes more along the sill, jamb to jamb." → "Two strokes more along the sill."
9. l.1216–1217 "She took the broom back to the lean-to and hung it from its nail beside the fire, and went to the jar for water, and did not go near the stair." → "She hung the broom back on its nail beside the fire, and went to the jar for water." (F2). Add: "the court grew light"; the window in the finder "a square of dark, its shutter ajar".
10. l.1219 "She looked at the thing at my face, and then past it, at her lamp, with the look she gave a jar…" → "She looked at her lamp, with the look she gave a jar when a lodger had been standing too near it."
11. l.1219 "wet her fingertips at her mouth, and pinched the flame out." → "She crossed to the sill, wet her fingertips at her mouth, pinched the flame out, and turned to her pot."
12. Add to D1: the gallery cough is **once** ("Overhead somebody coughed in his sleep, with long gaps between, an old man's cough."). The lodger's cloak on the rail is not on the page.

**PLAUTIA card, "Ch.16 as written" (l.1485–1531).**

13. l.1503 "my son's father has been kind to each of them all this winter" → "he has been kind to those freedmen all winter" (and "My son's father is among the proconsul's people again this year").
14. l.1512 "Plautia opens it "along a seam as fine as a hair"" → "until a line showed in the gold, a seam as fine as a hair; she opened it along the seam".
15. l.1518 "a sound broke from her, short, surprised" → "A sound broke from Plautia, short, surprised; … and it broke from her again, and that time she let it." The pause cluster is gone: no "quite still", no "said at last", no "quiet for a little".
16. l.1521 the blunt-question list:
    - "And after the hour?" → "When the hour was out?"
    - "Does he laugh? Your husband." now runs inside one speech after "I watched him at the well."
    - "Were you afraid of him, at the beginning?" now stands with no period before it.
    - The proconsul's-wife period is **off the page**.
17. l.1525 "Then you are the first," → "That would make you the first,". Add: "Everybody who climbs that stair wants something of mine." is now inside the "What he had chosen" speech (one speech, one tag).
18. **The triumph-games line (AUTHOR-CP3-5): add it verbatim to the record-office bullet.** C4 opens: "At the games for Titus's triumph," Plautia said, "the proconsul goes out to the god's precinct on the Isthmus with his whole staff…". Add the rule: the 72 festival is "the games", "the god's precinct on the Isthmus" or "the boys' race", **never "the Isthmia" or "the Isthmian Games"** (Ch.16 page: 0). Also add "And when he rides in from the Isthmus after the boys' race, with the dust on him".
19. Add to the rules line: **her syntax fingerprint never runs the same skeleton twice running, and the narrator never names it** (cycle 0, C2/C3). Pause beats: ≤1 per scene. **"And you?" is at 4 chapters book-wide (cap reached) and "And yours?" at 2 (no third).**
20. Add to the spent list: "So I tell myself."; "That would make you the first,"; "Your boy has a mule's manners and two good hands."; "You cannot have the book, Valens."; "It was book Latin, slow, with the verb held back for the end"; the merged want-speech.

**MYRRHINE card (l.2883–2908).**

21. l.2886 "Follows Latin only "that much"." → 'follows Latin when it is slow ("She had caught the cloak and the cook, and no more.", once)'. "She had followed that much." is cut.
22. l.2893 "splits one "with great force" when overruled" → "split her next lupin so hard that half of it shot under the chest". The "coals" double is gone.
23. l.2893–2894: lupins on the final page **in two scenes only**: C1 (shelling into her skirt; the skins shaken onto the coals) and C4 (the split lupin). None in C2 ("returned to her stool and watched the curtain") or C3.
24. l.2899 "off a fuller's wife at the Saturnalia" → "off a rope-maker's wife at the Saturnalia" ("fuller's wife" belongs to Plautia's nursing line alone).
25. l.2903–2905: add lines "He looks at it every time the chest is open," / "She knows her shoes are on her feet." / "She'll stand on your hem." (on the page). Spent: the buy-back offer, the flask-and-litter objection, "She knows her shoes are on her feet.". **Ch.17 rule:** no price figure in her mouth, and no lupins.

**Ch.16 walk-ons and mention-only names (l.2372–2394).**

26. l.2374 porter "a porter on a stool in his porch and a dog on a chain" and l.2375 "a man with a stool and a tablet, who might have put it in writing and did not" → **neither is on the page**. The porter is introduced by his line only ("What name shall I take in to the master?" / "And her?" / "Round by the lane for the stable, and there are rooms over it,"). The porch reads "In the brother's porch a dog on a chain rose and announced us to everyone in the lane."
27. l.2378 the brother's dog "barks once at the end" → **cut** (R5). It does not bark at the close.
28. l.2386 the old man "coughed and shifted under his blanket" at dawn → **cut** (R8). He coughs once, in D1.
29. l.2388:
    - the proconsul "received him with great kindness" → "received him with every kindness";
    - **the proconsul's wife ("cough") is off the page**;
    - "the gray-haired one, who does not" → "the gray-haired one";
    - the mosaic man "who laid his little stones drunk" → "a man laying a floor in the dining room below us, whom this house pays by the day" ("a floor laid drunk takes twice as many days");
    - "a fuller's wife" (Myrrhine's buy-back) → "a rope-maker's wife".
30. l.2393 Gloria's Ray and the drugstore "triggered by Felix's seasickness" → "triggered by the seasick dun's head in her arms" (l.401). Add: "The fuller's boy and his steaming vat: cut (SPENT passing traffic; fullers' tubs were cold)".

**MARA card and FELIX card: no Ch.16 block exists in either. Add one to each.**

31. **MARA, Ch.16:**
    - no English;
    - Latin with Plautia ("Mine came out stiff.");
    - credential asides 1 (the bracelet trays);
    - chaos 4/4 (the cakes loop; the bands; the blush Plautia watches; "Lady, I only—");
    - her lines: "I have known you a morning. There is nothing of yours I want."; "I have your obol still," … "The sheet was to come from Euthydikos's people, and then it was the mountain."; "In the summer a bed fell in under us," … "It was the herdsman's own bed, and it put us on the floor with the fleeces on top of us. He laughed then."; "Not much." (to "How much is left in it?"); "You asked for it.";
    - **bare "No." 1** (l.39).
32. **FELIX, Ch.16:**
    - "When's the next? Every week? Does she know it's me eating them?";
    - the bite test, "Hand it over, I'll show you.";
    - "How heavy is it?" … "Can you feel it there when you lift your arm?";
    - the amphitheater speech;
    - "Will you show me where you stood? Not in it. Only the gate.";
    - sick into the sea; "Why don't they spew?…"; "Every bit?";
    - **he has now seen the flashlight**: "Where's the flame? Why doesn't it smoke? Is it hers? Can I hold it?" / "What's it burning?" / "Does it go back on?";
    - the citadel questions; "I'd sooner not look at it";
    - the shout about the dun in the cabbages.
    - **Bleed-guard note:** his "What's that?" opener at Mara's objects is CLOSED (Ch.11 variant, Ch.12; cut from Ch.16 by F1).

**ARISTON card.**

33. Add a Ch.16 status line. The reply is **written** in Corinth, "in Plautia's room four mornings after that first one, on a sheet of papyrus from a stall at the top of the Lechaion road". Its content is told, never quoted ("the news of her lane", "Not a word." of herself). It has not yet been sent ("find somebody going to Syria"; Kallia: "Pay him when he's aboard," … "Not before."). The l.3450 OPEN THREAD (Ch.10 at-risk) → **written, not yet sent**.

**MARCUS card.**

34. Add "Ch.16 (mention only, in Plautia's mouth)":
    - "My son was seven at the vintage.";
    - named "Marcus. For his father's father";
    - his father's ears, her mother's temper, the Muses, not the Graces;
    - the ball taken in at the gate;
    - the tooth marks on the bracelet;
    - at the games "in the second row, in a new tunic, beside his father".

**"At-risk after Ch.16" block (l.4011–4048).** Retitle it "SYNCED to the FINAL page (polish cycle 1 + F1–F8)".

35. l.4026–4028 the flashlight line "Not much. Some." → "Not much.".
36. l.4033 "each ending sounded to its last letter" (Mara's spoken Latin) → **cut**; the page has "Mine came out stiff.". l.4035 "She went a whole winter without my name." → "She had me most of an autumn before she wanted my name.".
37. Replace "Counts on the draft" (l.4044–4048) with the final counts:
    - Length and shape: **7,175 words** (shape_check), 7,181 (style), 7,830 (`wc -w`); dialogue 45.7% (shape 46); median 14 (shape) / 15 (metaphor); 6 breaks; `dialogue` → `question`.
    - Punctuation: em-dashes 3 (all cut-off speech); semicolons 18 (2.5/1k).
    - Reflex counts: and-chains 5; credential asides 1; negation pivots 0; hinge 0; "So" 0; "before I had" 0.
    - Gestures: object handling 1; jaw 1 (the dun's); every other class 0.
    - Speech habits: bare "No." Valens 1, Mara 1; narrated non-answers 0; command echo 0; "low" for Valens 1.
    - Other: "as if / as though" 1; "the way" 0; para-final negations 7 (0.97/1k); #11 3 firm (0.42/1k); memories 1 clause; AD 79 0; English 0; laughs: Plautia 1 (breaking twice), Mara 0; echoes 0; spoken-line echoes 0; anti-AI 8/20 (−1.125).
38. **New SPENT / CLOSED entries** (cycle 0's list, confirmed on the final page, plus this cycle's):
    - **the delivery frame**: CLOSED (Ch.5, Ch.6): a speaker's words set or laid down singly; endings given weight or sounded to the last letter;
    - **"[verb] quite still"**: CLOSED at 2 (Ch.5, Ch.15);
    - **a dog barking once into a silence**: SPENT (Ch.15);
    - **first sun on any peak at dawn**: SPENT (Ch.15);
    - **dawn light inventoried in sequence**: SPENT (Ch.15);
    - **"a lodger's [garment] on the rail above"**: CLOSED (Ch.10);
    - **"kept [poss] (eyes|face|gaze)"**: inside the CLOSED gaze-hold;
    - **a narration sentence of weather or motion wedged between two quotes of one speaker**: SPENT (0 more);
    - **Valens's back to the wall**: WATCH at 2 book-wide;
    - **"And you?"**: 4 chapters, cap reached; **"And yours?"**: 2, no third;
    - **"What's that?" as a reaction to Mara's object**: CLOSED at 4 (Ch.5, 11, 12, 13);
    - **"could not stop" for a laugh**: SPENT (Ch.15; sample-09's frame);
    - **"My wife," to a gatekeeper**: used (Ch.16); never a third time;
    - **Parallel chapters (Ch.22, 35, 38)**: the narration never pre-describes an image the other strand will dramatize;
    - **Plautia in Ch.17/22**: no skeleton twice running, the narrator never names it, ≤1 pause beat per scene;
    - **Myrrhine in Ch.17**: no price, no lupins;
    - **the 72 festival never "the Isthmia" / "the Isthmian Games"** (CP3-5).
    - **Spent in these words this cycle:** "She's done it before."; "Shut your eyes,"; "Hand it over, I'll show you."; "Can you feel it there when you lift your arm?"; "Every bit?"; "In the small hours"; "an unlit coast"; "her eye showed white"; "The court grew light"; "a square of dark, its shutter ajar"; "it put us on the floor"; "started for the stables"; "among my letters"; "a rope-maker's wife".
39. **SCENE BUDGET header of chapter-16.md** (l.3) still quotes "She does that."; refresh lines 3–8 with the final counts (item 37).

**Bookkeeping outside the bible (for the orchestrator):**
- **voice-dna.md l.352** still proposes "isthmian games" as a tic-gate WORLD_TERM. CP3-5 forbids the name for the AD 72 festival, and a world-term exemption would hide a slip from the gate. Strike it from the list. The tool does not carry it today.
- **ENTITY:** Felix has seen the flashlight; its batteries are near the end ("Don't spend it on mules."). The suit is "two years from this spring". Valens's post at the games (the baker's oven / the back door / the horse fair) is unresolved, and Ch.17 decides it on the page.

## VERDICT
**PASS** (cycle 1; finalize F1–F8 to apply, tested).

| Measure | Result |
|---|---|
| Genesis Floor | **8.5** (Prose & Voice 8.5, Pacing 8.5) |
| Average | **8.86** |
| Casual | **9.0** |
| Pacing | **OK** |
| Scores | Originality 9.0 · Theme 9.0 · Characters 9.0 (+0.5) · Prose 8.5 (+0.5) · Pacing 8.5 · Emotion 9.0 · Immersion 9.0 |
| CVI-Launch / CVI-Legacy | 9.7 / 6.9 (provisional) |
| Mechanical suite | clean on the cycle-1 page and on the finalize copy (echo 0; spoken-line echoes none after F1) |
| Swaps introduced nothing new? | No added explanation ✓; no new triad ✓; no echo ✓; **5 repeats moved sideways → F2–F6** |
| "what is it" | stock alone, but fused to Felix's third "What's that?" → cut both (F1) |
| CP3-3 / CP3-5 / END-1 / foreshadowing | ✓ / ✓ / ✓ / 0 |
| Words after finalize | **7,175** (≥ 7,100 ✓) |
| Anti-AI | 8/20, −1.125 (clean band) |

**BIAS CHECK:** This evaluation was produced by the same system that wrote the prose. Confidence in scores above 8.0 requires external validation (beta readers, editors, comp analysis).
- **Characters 9.0 rests on a judgment.** I did not count Felix's "What's that?" as a tic cap, because his exact whole line has occurred twice, not three times, and it does not distinguish him. A stricter reader would cap Characters at 7.5 on the cycle-1 page and pass the chapter only after F1. F1 is in the tested finalize set either way.
- **Prose 8.5 is the most the per-cycle rule allows.** The five sideways doubles are word-level and are cleared by the finalize set. A reader who weighs "the polish moved repeats again" more heavily would hold Prose at 8.0 until F2–F6 are on the page. The finalize set does that.
- **Immersion was deliberately not raised** although its three named slips are fixed, because the same cuts removed some period texture.
