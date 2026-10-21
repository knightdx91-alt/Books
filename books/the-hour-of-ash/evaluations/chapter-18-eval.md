# Evaluation: Chapter 18 — Lechaion (run 2) · HINGE
**Evaluator:** book-evaluator (independent; did not write or revise this prose) | **Date:** 2026-10-21
**Text evaluated:** `manuscript/chapters/chapter-18.md` (sha256 `20539561…`, md5 `629fcb53…`). This is the page after writer → dialogue-polish → hook-craft → disruptor → continuity repair (W-01…W-13). It runs **2,582 prose words** by shape_check, 2,590 by style and 2,586 by show_tell. Dialogue is **33.6%**.

**Read against:**
- the book's CLAUDE.md;
- STATE.yaml `guardrails` and `resolved_author_decisions`, especially **AUTHOR-CP3-3**, **CP3-5** and **END-1**;
- voice-dna §0–§8;
- character-bible.md:
  - every at-risk and spent block, from "after Ch.1" to "after Ch.18";
  - the PACUVIUS card;
  - the VALENS, FELIX and MARA Ch.17/Ch.18 blocks;
  - the Ch.17 and Ch.18 walk-on notes;
  - the Retired / at-risk phrase table;
- outline `## Chapter 18`, Ledger row 18, and the Ch.19 opening;
- `evaluations/chapter-17-eval.md` (cycle 0, cycle 1 and finalize);
- chapters 16 and 17 for pacing (Ch.17's run and close in full);
- `evaluations/continuity/chapter-18-audit.md` and `evaluations/disruption-chapter-18.md`, for what was applied and what was cut.

**Genre profile and settings:**
- **Genre:** commercial historical romance / time-slip; comp *Outlander*.
- **Anti-AI band:** commercial (0–8 clean, 9–11 watch). **Explanation-density cap:** the short-chapter rule from after Ch.10 ("in a chapter under 3,000 words, allow 1"), on top of the commercial >0.8/1k.
- **Engagement (book):** empathy 55 / fascination 30 / self-insertion 15. **This chapter is empathy-first:** a wedding and a gift.
- **Dimension 7:** IMMERSION.

**Measured** (`bash books/the-hour-of-ash/tools/check_chapter.sh 18`, run from /home/user/Books): **clean on every gate.**
- style: simile 1.1/1k, em-dash 1, foreshadow 0;
- grammar 0; rhythm 0; show/tell no flags, dialogue 33.6%;
- voice-wear strict clean; tic gate clean (and-chains 3/9, credential 0, pivots 0, "So" 0; all gesture classes under cap);
- echo 0;
- metaphor 1.2 fig/1k, median 15;
- `shape_check --strict`: `18 2582 0 34 15 I-statement punch`, CLEAN.
- `tic_report.py --echoes 18`: **none / none / none** (echoes, command echoes, spoken-line echoes).

**My own scans** (scratch only, not gates):
- 3–7-grams of Ch.18 against Ch.1–17 and all 13 voice-bank samples, **stop-word-bounded strings included**;
- content 3-grams against Ch.15–17;
- in-chapter repeated 3–5-grams;
- a narration-only scan for paragraph-final negations and for present-tense generic similes;
- by hand: every SPENT, CLOSED, RESERVED and WATCH item in the bible, grepped by frame as well as by string, and every Valens line for comparison.

**The fix set was tested together on a scratch copy.**
- The copy was swapped into the manuscript path. The real `check_chapter.sh 18`, `shape_check --strict`, `tic_report.py --gate` and `--echoes 18` were run from /home/user/Books.
- The original was restored after every run and its checksum verified (sha256 `20539561…`, md5 `629fcb53…`). **I did not edit the manuscript.**

*(l.N = line number in the current `chapter-18.md`.)*

---

## HEADLINE
**CVI-Launch (CVI-L):** 10.0 (9.49 + 0.5 strong anchor, capped at the scale) | **CVI-Legacy:** 7.1 (provisional) | **Genesis Floor:** **8.0** | **Genesis Average:** **8.79** | **Casual Reader:** **9.0**

**Engagement type:**
- **Empathy** leads: a boy crying open-mouthed under a half-bald crown, and a dead father's watch handed back running with no word said.
- **Fascination** is second: a shipmaster who marries two strangers to satisfy a woman neither of them will meet.
- **Self-insertion** is third: being married in ten words, on the spot, because a ship will not wait.

**Divergence alert:** none to report as a craft problem. The gap is 10.0 − 8.0 = 2.0, which sits right at the threshold, and it means one thing: **this chapter will sell, and the only thing holding it is book-law reuse that no reader at an airport will see.**

**Gate (Floor ≥ 8.5 AND Casual ≥ 8.5 AND pacing OK AND gates clean): NOT MET.**
- Casual 9.0 ✓; pacing OK ✓; mechanical gates clean ✓.
- **Prose & Voice holds the floor at 8.0, on merit, with no cap.** The sentences are 8.5 and better. What holds them is a cluster of breaches that no gate sees:
  - **a voice-bank lift.** The opening's offstage hammer, "two blows and a rest, two blows and a rest" (l.9), is **sample-06's** "three blows and a pause, three blows and a pause". Sample-06 is the reserved Ch.24 labor register. Printing it here makes Ch.24 the echo.
  - **a retired narration phrase.** "as if nothing in Achaea were in a hurry" (l.9). The bible retired "in a hurry" from the narration after Ch.9, and this is its 6th book-wide use. It also ends the paragraph on a negation.
  - **three narrating-present similes.** "the way cords hold up a blind" (l.15), "as a far younger boy cries" (l.83) and "like a diving board after somebody has gone off it" (l.115). voice-dna §0.4 says "No narrating present". The after-Ch.13 block sets present-tense "the way a X does" in narration at 0.
  - **four Ch.15 heat-scene carry-overs, in a chapter that is not a heat scene:**
    - "'Keep off her heels,' Valens said, too late." (l.123) is the skeleton of '"Mind the roof," I said, too late.' That line is SPENT as part of Heat 1's staging.
    - "before she trusted her weight to it" (l.147) is "trusted the poles with his weight", SPENT in those words. It is also Ch.6's "before he trusted it".
    - "he gave me the look he gave a stretch of road before he took the mules onto it" (l.71) reuses Ch.15's one heat comparison: "as a man learned a road he meant to take again at night". It is the same vehicle (road) for the same tenor (Valens's attention to Mara). The bible says no vehicle domain is used twice.
  - **two Ch.16 carry-overs:**
    - the bracelet's closing, "shut again round my wrist with a click", becomes the watch's "shut on my wrist with a small dry snap" (l.111). That is the previous chapter's anchor object, as a skeleton.
    - Mara's Ch.16 "there is not much of it", about her Greek, becomes "if not much of it", about her breath for Latin (l.55).
  - **one Ch.17 carry-over:** the last paragraph's "The wind blew harder into our faces" becomes l.9's "the wind blew straight in off the water into our faces", two pages later.
  - **two CLOSED frames, re-nouned:**
    - "a gray man with tar to the elbows" (l.79) is the "[substance] to the [joint]" depth frame, CLOSED after Ch.9.
    - "a harbor Latin with the ends of the words knocked off, and he threw it down at us" (l.31) is the delivery frame, CLOSED after Ch.16: a speaker's endings described, and speech laid or thrown down. Here it is inverted, but it is the same attention channel.
  - **explanation density over the short-chapter rule.** There are 2 firm #11s (0.77/1k) in a chapter under 3,000 words, where the rule allows 1.
  - **four in-chapter doubles:**
    - "stood hard." / "The hands stood" in adjacent sentences (l.103–105);
    - "The girl in the blue hood had…" opening two paragraphs (l.69, l.97);
    - "between the quay and the" ×2 (l.115, l.143);
    - "between us" in consecutive sentences (l.155, l.159).
- **Characters sits at 8.5**, not 9.0:
  - Felix's "It's the sun" (l.85) is Plautia's Ch.16 anchor skeleton: tears blamed on an irritant ("The smoke has got into my eyes."). A line's skeleton is never moved into another character's mouth soon after (after-Ch.17 block).
  - "He was watching the dun." (l.107) is Valens's Ch.13 beat of looking away while Mara handles her small things ("He was watching the crowd past my shoulder while I did it"). It is the 3rd book-wide "He was watching the [X]".
  - There are two narrator moves on a walk-on's tags: "he **promised her**" (Felix to the dun: a second said-to-a-non-listener, where the cap is 1 and "told the harbor" already holds it) and "the sailor **complained**" (a non-"said" tag; voice-dna: "said" by default).

**The fix set: 20 swaps, tested together** (script below). Six are cuts or near-cuts, all inside the 2,500 floor, and the rest are word-for-word or near-even swaps.
- 2,528 words (shape_check); dialogue 34.3% (34); median 15 (mid ✓); 0 breaks; `I-statement` → `punch`;
- every gate clean; echo 0; spoken-line echoes none; command echoes none; tic gate clean; shape CLEAN;
- **the first sentence, the ten words, the closing line and every anchor line are byte-identical.**

---

## Genesis Score (Craft Assessment)

| Dimension | Score | Evidence | Cap reasons / holds |
|---|---|---|---|
| Originality | 9.0 | **The outline's subversion is on the page:** the lavish wedding set piece becomes ten words on a sunlit quay, said to satisfy a shipmaster: "Will you be my wife, Mara?" / "Yes. Will you?" / "Yes," (l.73–77). **What the writer built on top of it:** (1) **the master's reason is his daughter's new mother-in-law**, a woman neither of them will meet: "his mother will have the name of every soul who slept on this deck out of her before she's got her cloak off" (l.41); (2) the daughter's question, at the rail with a cucumber: "Father, was mine like that?" / "Yours had a cake," (l.97–99); (3) "As I was told at sunrise, and nobody on my ship has lied to anybody." (l.99), where the cover lie becomes true without anyone saying so; (4) the master's lost sandal as his own bad day; (5) the watch moved to the right wrist because the left carries another woman's gold "with a child's teeth in it already" (l.109); (6) the mule blindfolded with the boy's tunic, so that the boy goes aboard crowned and in his loincloth (l.143–149). | **≥9.0:** would a senior editor set this beside *Outlander*'s handfasting at the inn? Yes. It is the anti-wedding, and it is funnier and quicker. **Not 9.5:** the balking animal at the gangplank is a stock comic beat, and its execution here is fresh rather than new. |
| Theme | 9.0 | The outline's theme is "home as the person beside you on the gangplank". It is carried by acts and never stated. "The fig was all that was left on the quay, in its jar by the ring, and me." (l.153), and then "the little tree shook all its leaves between us" (l.155). "Then she's nobody's, which is worse." (l.61) is belonging as a shipmaster's rule. The daughter married by messenger to a man "she's never set eyes on" (l.41) is set against two people who chose each other in ten words, and the page never compares them. **Texture that means nothing:** the sandal, the small Sicyonian, the sprats, the rowers eating, the bitter knob of the cucumber. | **≥9.0:** the theme is a question the reader answers, with no aphorism and no narrator significance. **Not 9.5:** the fig jar carried between them is the obvious emblem, and it lands because it is underplayed. |
| Characters | 8.5 | **Pacuvius** is complete in about 300 words and matches his card. His attention is the far port's opinion. His syntax is consequence run-ons, then a verdict ("Then she's nobody's, which is worse."). His one chaos is the sandal. He never comes down the plank, and he says nothing warm. **Felix** stacks questions and rotates his openers (Where / Why / Are / Who / When / Wouldn't / Here? / Who / From / Were / Which / Mine?). His crying is inhabited: "crying open-mouthed … out loud … he scrubbed at them with the heel of his hand and they came faster" (l.83). **The sailor** has his own day: the bet, the witnessing, the kick, and "that's your mule". **The daughter** has one line and one act. **Valens:** no comparison in speech (every line checked), bare "No." 0, no walk-off, footing orders caused by the plank, and his evasion carried by attention. **Mara:** chaos 3/4, all inhabited (below). Cover-the-name PASS for all five speakers. **The vulnerability is right:** Mara's Latin fails her ("The rest of it outran me.", l.41) and she is cut off (l.55). | **No cap.** There is no catchphrase, and the gate's gesture classes are clean (I use the gate's numbers). **Held at 8.5** by C1–C4: Felix's tears blamed on an irritant (Plautia's Ch.16 skeleton); Valens's Ch.13 look-away, 3rd book-wide; the "promised her" said-to (2nd in the chapter against a cap of 1); and "complained" as a tag. |
| **Prose & Voice** | **8.0** | **Stopping sentences:** "Felix took it and put it on, and cried underneath it." (l.89); "The fig was all that was left on the quay, in its jar by the ring, and me." (l.153). **Underlines:** "Gold that soft took a scratch from anything, and it had a child's teeth in it already." (l.109); "the dun stood still in the dark he had made her, with her ears turning." (l.143); "the only thing moving on that quay that nobody was shouting at" (l.103); "As I was told at sunrise, and nobody on my ship has lied to anybody." (l.99); "I put the crown back on him." (l.145); "The rest of it outran me." (l.41). **Ugly sentence:** "The watch sat on the wrong wrist and ticked." (l.113). **Voice under pressure:** the run is in the body (blood, legs, ears; "breath for Latin") and in the failing Latin (the master outruns her; she is cut off at the dash). The asides go quiet through the condition. The voice opens again at the cucumber and the watch. | **Merit 8.0, no cap.** #11 is under the commercial cap (0.77/1k), but **over the short-chapter "allow 1" rule (2 firm)**. The ugly sentence and the voice under pressure are both present. **Held by the law cluster** (R1–R13, D1–D4): the sample-06 hammer; the retired "in a hurry"; three narrating-present similes; four Ch.15 heat carry-overs; two Ch.16 and one Ch.17 carry-overs; two CLOSED frames re-nouned; the explanation density; the in-chapter doubles. Anti-AI: 7/20, −1.0 (clean band). |
| Pacing | 9.0 | **The ledger row is hit on every hard field:** Single-scene, between Ch.17's In medias res and Ch.19's Chronological ✓; open `I-statement` (29 words, in the moment, the run in the mouth, not re-narrated) ✓; close `punch`, "They drew the plank in after us." (7 words, single-sentence paragraph, which is allowed for Ch.18) ✓; 0 breaks ✓; dialogue 33.6% (30–40) ✓; 2,582 against 2,800 (−8%, inside 2,500–3,100) ✓; median 15 (mid) ✓; under an hour, the same afternoon ✓. **Speed design, as the outline asks** ("fast and practical; one still moment with the watch"): the condition runs as talk; the ten words are three lines; **the watch is the one deceleration** (l.101–113); then the mule chaos accelerates to the plank. **Value shift:** refused passage (−) → married (+) → loading fails, the sailor kicked, the black loose, the yard up (−) → aboard (+). **The sail from Ch.17 is answered at once,** and it is theirs (l.15): the hoist becomes the master's deadline ("You have till the yard's at the top.", l.61). | **Not 9.5:** l.11–15 are three descriptive paragraphs (the goose, the plank tug-of-war, the sail mechanics with a tow boat), about 250 words before the first spoken line, straight after Ch.17's cliffhanger. Felix on the plank is a hook inside them, so it is a small sag, not a stop. |
| Emotion | 9.0 | **The anchor lands exactly as planned** ("the watch, handed back on a sunlit quay as a wedding gift, already wound"): "He took out the watch and laid it in my hand. / The case was warm from him." … "I put my nail to the crown to give it its turns, and it took two and stood hard." (l.101–103). It is running and wound, and the time sits by the sun (twenty to one, a short shadow tipped east). **Nothing is explained, and no word is spoken about it** (END-1 ✓). **The surprise lands:** the wedding is ten words, and they nearly miss the ship over a mule. **Body rebel:** Felix's tears bypass him and get worse when he scrubs at them. Mara's own feeling goes entirely into objects and acts: she wipes the crystal, winds the crown, chooses the wrist. That is the outline's "the emotion is in a wound watch", with **zero intensity-words** in her narration. **Techniques ≥5:** object proxy (the watch, the fig jar, the crown); displacement (Felix cries the chapter's tears); comedy at a wedding (the sandal, "Throw a nut at this ship…"); subtext (her mother, who is not at her wedding, via the cucumber; never glossed); dramatic irony ("nobody on my ship has lied to anybody"). | **≥9.0. Not 9.5:** Mara gives the reader one interior beat about the man at the moment of the proposal only by way of the cucumber. That is the right restraint, but a share of romance readers will want one more breath from her inside the ten words. |
| **Immersion** (Dim 7) | 9.0 | **Period:** stern-to mooring with the gangplank off the stern; the goose-head sternpost (*cheniscus*), white paint flaking and a red beak; a square sail brailed up through lead rings, the yard climbing in jerks on a single halyard, then "making it fast to a pin"; a tow boat with a slack line off the bow for an onshore breeze; cleats on the plank; the Kalends and the Ides; the magistrate's people at Puteoli; marriage by consent before witnesses, "no priest and no cake" (verified in audit I-01); the *mustaceum* in "Yours had a cake"; nuts thrown at a bride; "by Pollux" in a man's mouth; mules as deck cargo, and the marble ship that will not take one. **The authenticity dial:** sensory ~8 (pitch going soft, sprats, flour in the watch links) and harshness ~7 (the Ostia brothers with cudgels, told in one line). | **Held at 9.0.** Small slips: the opening hammer belongs to a sample (R1); "a crown that's got no leaves" for pine needles is Felix's word, so it is kept. |
| **FLOOR** | **8.0** | Prose & Voice (merit) | |
| **AVERAGE** | **8.79** | (9.0 + 9.0 + 8.5 + 8.0 + 9.0 + 9.0 + 9.0) / 7 = 61.5 / 7 | |

**Why Characters is held at 8.5:**
- **C1, Felix's irritant excuse (l.85).** "It's the sun," … "I've been sat in it since sunup. Don't look at me." Ch.16's anchor is Plautia's "The smoke has got into my eyes." after "You admired it.": tears blamed on something in the air, two chapters back. The bible lists that line as SPENT in its words, and the after-Ch.17 block forbids moving a line's skeleton into another mouth soon after. The Devoted reader catches it at once.
- **C2, Valens's look-away (l.107).** "He was watching the dun." while Mara reads the watch. In Ch.13 l.68 it is "He was watching the crowd past my shoulder while I did it", while she put her small things back. That is the same evasion at the same kind of moment. With Ch.12's stranger, it is the 3rd "He was watching the [X]". Two uses on Valens at an object hand-off is the start of a signature beat.
- **C3, "he promised her as they came" (l.115).** Felix speaks to the dun, and the tag names the animal as addressee. That is the said/told-the-[non-listener] family, which has a cap of 1 per chapter. "the sailor told the harbor" (l.95) already holds it, and that is the family's 5th use book-wide (audit I-12). "promised" is also a non-"said" tag.
- **C4, "the sailor complained from the coil" (l.127).** A non-"said" tag, against voice-dna §1: "'said' by default … No 'growled,' 'hissed'".

**Trajectory against Ch.1–17** (finals 8.50–8.86; cycle 0s 7.5–8.0):
- This is the eighteenth cycle 0 below the gate, and the fourteenth held by narrator moves the gates cannot see.
- The continuity repair added no gloss. Its recasts (W-02, W-07, W-09) are clean, and I re-scanned them.
- **The new failure modes:**
  - **narrating-present similes**, three in one chapter, which the book had not shown before at this density;
  - **Ch.15's heat scene mined outside heat**: four frames here, after W-12's "the heat of him" was already caught;
  - **the last paragraph of the previous chapter reused in the first paragraph of this one** ("the wind blew … into our faces").

---

## CVI-Launch Breakdown
| Input | Score | Evidence |
|---|---|---|
| Commercial Pacing | 9/10 | A short single scene with a clock (the yard). The wedding takes three lines, the chaos runs at speed, and the chapter ends on the plank drawn in. It loses 1 for the three descriptive paragraphs straight after a cliffhanger. |
| Tomorrow Test | 6 anchors → 10 | IMAGE: Felix crying open-mouthed under a half-bald pine crown; the watch handed over with flour in its links, wound to the stop and right by the sun; the dun walking up the plank blindfolded in the boy's tunic while the boy stands in his loincloth; the fig jar carried up between them. QUOTE: "Yes. Will you?"; "Father, was mine like that?" / "Yours had a cake,"; "Do I get my tunic back, or is she wearing it to Italy?"; "And if any of you sees a sandal floating past the mole, it's mine." |
| Casual Reader | 9.0/10 | See the report below. |
| Shareability (quote / plot / emotional) | 4 / 4 / 5 → 8 / 8 / 10 → **9.47** | **Quote:** "Yes. Will you?" **Plot:** "the captain won't sail with an unmarried couple, so they get married on the dock in ten words with the mule boy as witness." **Emotional:** "he kept her dead father's watch running for a year and a half and hands it back without a word." Calculation: MAX 10 × .6 + AVG 8.67 × .4. |
| Concept Pitch | yes → 10 | |
| Human Closeness | yes → 10 | A proposal, a gift, a boy's tears, two people carrying a tree up a plank. |
| **CVI-Launch** | **9.49 + 0.5 = 10.0 (scale cap)** | 9 × .2 + 10 × .2 + 9 × .2 + 9.47 × .2 + 10 × .1 + 10 × .1 = 9.49. The one-chapter formula saturates on a short romance hinge (see BIAS CHECK). |

**CVI-L note.** In this project "CVI-L" means **CVI-Launch: 10.0** (9.49 before the anchor bonus).
- Running CVI-L, Ch.12–18: 9.7 / 9.8 / 8.9 / 9.8 / 9.7 / 9.7 / **10.0**.
- This is the book's hinge and its most shareable chapter so far. After Part One's action climax (comedy under legal threat), the chapter turns to **the romance's public turn**: the first time the two of them say anything binding out loud, and they say it in front of a boy, a sailor and a stranger's daughter.
- What drives launch here is the Casual reader's pleasure: a wedding that takes ten words, a crying boy, a gruff man with one sandal, a mule in a blindfold. Craft is not the driver.
- **None of the 20 fixes touches an anchor.** These lines are byte-identical after the fixes:
  - the ten words;
  - the crown and "cried underneath it";
  - the watch hand-over ("He took out the watch and laid it in my hand. / The case was warm from him."), the crystal, the seconds hand, the crown taking two, twenty to one by the shadow;
  - the wrist business ("Gold that soft…"), "The watch sat on the wrong wrist and ticked.";
  - the daughter's question and "Yours had a cake,"; "nobody on my ship has lied to anybody"; the sandal;
  - the tunic blindfold; "I put the crown back on him."; the fig and "me"; the closing line.
- **CVI-L is unchanged after the PATH: 10.0.** C1 changes Felix's excuse from the sun to the nuts. The image (crying under the crown) is untouched, and the line gets funnier, because it pays off his own nut grievance from l.63.

**CVI-Legacy (default weights; provisional):** **7.1** (7.05). It is the sum of:
- Originality 9.0 × .30;
- Theme 9.0 × .25;
- Cultural Vocabulary 2 × .20;
- Re-readability 8 × .15;
- Identity 5 × .10.

What rewards a re-read:
- the watch, set to the sun by a man the reader saw read it ten minutes fast in Ch.11, and never explained;
- Felix's Ch.15 "Would you cry, if it was me?" / "Not in front of everybody." against his crying here in front of everybody, never pointed at;
- "In a pot, it goes where I go." (Ch.11) against the fig carried up the plank;
- the daughter married by messenger to a stranger, against a marriage chosen in ten words.

---

## Anti-AI Scan (20 patterns; density per 1,000 words at 2.58k; commercial band)
| # | Pattern | Result | Count / density | Citation |
|---|---|---|---|---|
| 1 | Forced symmetry | FOUND minor | 2 (0.77) | "He hauled. She leaned." (l.119; physical, kept); the master's "A husband … she'll swallow. A man your size … she will not swallow" (l.41; character). **−0.125** |
| 2 | Empty poetic vocabulary | Clear | 0 | |
| 3 | Automatic rule of three | Clear | — | Felix's stacks are his card's syntax. No narration triad. |
| 4 | Em dashes | Clear | 1 | Mara cut off (l.55). |
| 5 | Empty metaphors | Clear | 0 | The blind, the diving board and "a bar" are all concrete. |
| 6 | Dramatic "And" openings | Clear | narration 0 | Speech: one rejoinder ("And if any of you sees a sandal…"), with one owner. |
| 7 | Pseudo-philosophical closings | Clear | — | The chapter closes on the plank drawn in. |
| 8 | Excessive parallelism | FOUND minor | 3 (1.16, mostly speech) | "two blows and a rest, two blows and a rest" (l.9, narration; → R1); "I stood witness … I stood up and witnessed" (l.127, character); "Is that all of it? … Is that them married?" (l.79, character). **−0.125** |
| 9 | Overly smooth transitions | Clear | — | One single scene, with no sutures. "By then Valens had the thong of his pouch undone." (l.101) is a plain time link. |
| 10 | Described emotions | FOUND minor | 1 | "with no great liking for the flour on him" (l.27). It names an attitude, and it is wry. **−0.125** |
| 11 | **Explanatory extension** | **FOUND moderate; over the short-chapter rule** | **2 firm (0.77/1k)** | (1) l.109 "Gold that soft took a scratch from anything, and it had a child's teeth in it already." (explains the act; **the keeper**); (2) l.69 "to draw the bitterness out" (a purpose tail inside the memory). **Borderline, not counted:** l.15 the blind (a comparison with no unpacking); l.103 "the only thing moving on that quay that nobody was shouting at" (a characterizing extension); l.9 "as if nothing in Achaea were in a hurry" (interpretive; → R1). **−0.25.** Commercial cap (>0.8/1k): PASS. **After-Ch.10 short-chapter rule ("allow 1"): FAIL** → R12. |
| 12 | Binary negation opener | Clear | 0 | Gate pivots 0. "It isn't the fare." is the master restating terms (his card). |
| 13 | Precision flex | FOUND minor | — | "three sailors", "four mules", "the third hour", "twenty to one", "it took two", "the finest of the three hands". Each one works, and the disruptor already deflated the crew counts. **−0.125** |
| 14 | Emotional control demonstration | Clear | — | Felix's control fails. Mara's is never narrated. |
| 15 | Authoritative description | FOUND minor | — | The sail paragraph (l.15) is rigging explained with confidence. It is offset by "What I saw first, and clearly" and "The rest of it outran me." **−0.125** |
| 16 | Philosophical asides | FOUND minor | 1 | "Gold that soft took a scratch from anything" is a past-tense general truth, practical rather than philosophical. **−0.125** |
| 17 | Clean dialogue | Clear | — | Cross-talk throughout: Felix answering questions nobody asked him, the master's speech outrunning Mara, Mara cut off mid-word, the sailor talking to the harbor. |
| 18 | Thematic echo chamber | Clear | — | The sandal, the Sicyonian, the sprats, the rowers eating. |
| 19 | Graduated reveal | Clear | — | Single scene; the close releases the tension instead of raising it. |
| 20 | Emotional temperature report | Clear (edge) | — | Three run-body beats in the first 55 lines (l.9, l.37, l.55), then none. They are clustered, not periodic. |

**7 / 20 found (#1, #8, #10, #11, #13, #15, #16). Total −1.0. Band: clean (commercial 0–8).**
- **#11 hard check:** commercial cap PASS (0.77/1k); short-chapter rule FAIL (2 firm, allow 1).

**After the PATH:**
- #11 → 1 firm (0.40/1k), minor;
- #8 → minor (the hammer pair goes);
- **7/20, −0.875: clean band.**

---

## The book's own laws
- **NO FORESHADOWING: PASS** (gate 0; by reading, 0).
  - No "would" reaches forward. "Who ever died of a plank?" is Felix's, it is comic, and it is diegetic. The narrator never comments on it.
- **The watch must not be loaded toward the approved ending (END-1): PASS.**
  - The disruptor's cut of the Ch.11 recall stands, and nothing on the page now says or implies that he set it or kept it.
  - "The watch sat on the wrong wrist and ticked." (l.113) is literal: her habit was the left (audit I-05).
  - **Judgment:** the outline puts the watch on her wrist at Ch.43 ("She keeps the watch on her wrist") and ticking at Ch.44. That makes this line the plant, and no page points at it. That is design (the outline's "re-read thread"), not loading.
  - **Forward guard (orchestrator, for the Ch.24/32/41/43/44 briefs):**
    - no "…and ticked." one-line paragraph again;
    - Ch.44's watch on her wrist must be worded fresh and must not recall "the wrong wrist".
- **AUTHOR-CP3-3: PASS.** Nothing about a child.
- **AUTHOR-CP3-5: PASS.** "Isthmia" 0; "Isthmian" 0. The festival is "the men's race" and "the boys".
- **AUTHOR-END-1: PASS.** No Ch.15 door, camera or "wait outside" line is quoted or paraphrased.
- **The outline's NON-NEGOTIABLES: all on the page.**
  - **Consent before witnesses, in ten words:** "Will you be my wife, Mara?" (6) / "Yes." (1) / "Will you?" (2) / "Yes," (1) = 10. Felix and the plank sailor witness, and the master's rule is stated once.
  - **Felix cries** (l.83–89).
  - **The sailor wants to get on:** "Is that all of it? … Is that them married? Then get your mules up, by Pollux, the yard's nearly there. Pacuvius, they're done." (l.79).
  - **The watch, given back wound, with no speech and nothing explained:** Valens says nothing about it; "it took two and stood hard"; it reads by the sun. The page never says he set it or kept it wound.
  - **A mule refuses the plank:** the dun, forefoot on and then back, "until the rope between her and Felix was a bar" (l.115).
  - **No vows** (a question and two yeses), **no narrator significance**, **no aphorism**, and **an action close**.
  - The Ch.16 rules hold: the gangplank mule is not seasick and does not go down (the sailor does).
- **Memory only when the scene triggers it: PASS.**
  - The one memory is the cucumber end at her mother's sink. It is triggered by the daughter's bitter knob in the same paragraph, two sentences long, and the next paragraph returns to the scene: "Valens faced me".
  - It is a different source and shape from Ch.16 (a clause-run) and Ch.17 (the storeroom, no person).
  - It does not close on a lost name, and it is not a parent showing the child antiquity.
  - **R12 removes its purpose tail,** so the mother's ritual stands as an act.
- **Explanation-density cap: FAIL by the short-chapter rule** (2 firm in 2,582 words; allow 1) → R12. **After: 1 (0.40/1k).**
- **Paragraph-final negations ≤1.5/1k: PASS.**
  - **2 in narration (0.77/1k):** l.9 "as if nothing in Achaea were in a hurry"; l.27 "with no great liking for the flour on him".
  - **After the PATH: 1 (0.40/1k)**, because R1 ends l.9 on "his to spend".
- **No comparisons in Valens's speech: PASS.** Every Valens line was checked: "Where's the freedman?"; "Valens. A freedman from the city paid you."; "I'll pay the fare again,"; "You were told wife,"; "Is there another ship for Italy?"; "Nobody's coming after her."; "Will you be my wife, Mara?"; "Yes,"; "Keep off her heels,"; "The boy's,"; "Cover her eyes, Felix. Her eyes."; "Tread on the cleats … It gives in the middle." No "like" or "as", no idiom, no hyperbole.
- **No command echoes: PASS** (gate none). By hand, each order is answered by its result:
  - "Haul now" → nobody hauls in words;
  - "Get your mules up" → "Felix had the dun loose";
  - "Hold her head, boy" → no;
  - "Cover her eyes" → "threw the tunic over the dun's face";
  - "Get them aboard" → the loading;
  - "Tread on the cleats" → "We went up together";
  - "Ask her," → nothing.
- **No borrowed whole spoken lines: PASS** (`--echoes 18`: none).
  - By skeleton: Felix's "It's the sun" is Plautia's irritant excuse → **C1**.
  - "Is that all of it?" he said (l.79, the sailor) has Ch.11's frame, "Is that the last of it?" he said (Valens). Ordinary English, seven chapters apart, a different speaker: logged as INVESTIGATE.
- **No reuse of earlier chapters' phrases or set pieces: FAIL, cleared by the PATH.**
  - **sample-06 (Ch.24 labor, RESERVED by register)** l.12 "a hammer … three blows and a pause, three blows and a pause" → l.9 "somebody was hammering at a hull, two blows and a rest, two blows and a rest" → **R1**. This is the highest-value single fix.
  - **Ch.17's last paragraph,** "The wind blew harder into our faces" → l.9 "the wind blew straight in off the water into our faces" → **R2**.
  - **Ch.15 heat:**
    - '"Mind the roof," I said, too late.' → l.123 → **R11**;
    - "trusted the poles with his weight" (and Ch.6 "before he trusted it") → l.147 → **R9**;
    - "as a man learned a road he meant to take again at night" → l.71 → **R6**.
  - **Ch.16:**
    - the bracelet's "shut again round my wrist with a click" → l.111 "shut on my wrist with a small dry snap" → **R8**;
    - Mara's "there is not much of it" (her Greek) → l.55 "if not much of it" (her Latin breath) → **R13**;
    - Plautia's irritant excuse → **C1**.
  - **Ch.13:** Valens's look-away at an object hand-off → **C2**.
  - **CLOSED frames re-nouned:**
    - "with tar to the elbows" ("with dust to the", after Ch.9) → **R7**;
    - the delivery frame (endings described; speech laid or thrown down; after Ch.16) → **R10**.
  - **Retired:** "in a hurry" in narration (after Ch.9; the 6th book-wide use) → **R1**.
- **NO TICS: verbal catchphrases 0; gate gesture classes clean.** By hand:
  - **said/told-the-[non-listener], cap 1:** "told the harbor" (kept) plus "promised her" (the dun) → **C3**.
  - **Non-"said" tags:** "promised", "complained" → **C3, C4**. ("shouted" and "called" are volume, and they are kept.)
  - **Narrating present** ×3 → **R3, R4, R5**.
  - **Valens's doubling** "Cover her eyes, Felix. Her eyes.": urgency, one use, kept (audit I-09 optional).
  - **Indefinites in narration: 5** ("somebody" ×3, "nobody", "nothing"; 1.9/1k, WATCH) → **2 after the PATH.**
- **The "without" family: PASS at the cap, improved by the PATH.**
  - Before: 4 (3 narration + Felix's "without nuts"), 1.55/1k, against a Ch.15–17 average of about 0.33/1k. No frame is at a 3rd use after W-09 ("without stopping" is the 2nd).
  - R10 removes "without leaving the rail": **3 (1.16/1k).**
- **"as if / as though" ≤1: PASS** (1).
- **Em-dash: PASS** (1, a true interruption).
- **Body-rebel channels** (after Ch.17: seat and hands resting until Ch.20; voice retired): **respected.** Mara's hands act (wipe, wind, clasp, catch, carry) but never rebel. The voice break on "Yes" was cut (W-07). The chapter's body rebel is Felix's.

---

## Character Chaos Check (Primary: Mara)
- **Irrelevant thought: present, inhabited.** The cucumber end at her mother's sink, at the moment of her own wedding, with no gloss (l.69). After the PATH, also the pine needles stuck in the flour of his forearm hair, which is what she sees while he proposes.
- **Cognitive distortion: present, inhabited.** At the instant she gets her father's watch back, her mind goes to protecting a soft bracelet from scratches ("it had a child's teeth in it already", l.109). It is the conservator's eye displacing the feeling.
- **Unprompted memory: present, triggered by the scene** (the cucumber).
- **Failed emotional management: not on Mara.** The outline says "none forced. Let it be quick." The failure is displaced onto Felix, and her Latin fails instead (l.41, l.55).
- **Voice under pressure: demonstrated (level 1).** The run is in the body, and the asides go quiet through the condition.
- **Score:** 3/4 (commercial 2–3 is sufficient), all inhabited → no cap.

## Secondary Character Chaos
- **Felix:** his own moments — the nuts, the tears, the tunic, "is she wearing it to Italy?"
- **Pacuvius** (new): his own moment — the lost sandal.
- **The plank sailor:** his own moment — the Sicyonian bet, and "that's your mule".
- **The daughter:** her own moment — "was mine like that?", and the bitter end dropped over the rail.
- **Valens:** his own moment — the watch, said with nothing but a pouch thong and a nail on a catch.
- **No secondary character is a function only.**

---

## The Tomorrow Test
**What the reader remembers:** a boy crying open-mouthed under a pine crown with half its needles gone, while two people get married in ten words on a hot quay; and the watch, put back in her hand warm, with flour in its links, wound to the stop, right by the sun.
**Anchor type:** BOTH. IMAGE: the crown, the watch, the blindfolded mule, the fig jar. QUOTE: "Yes. Will you?"; "Yours had a cake,".
**Verdict:** **ANCHOR EXISTS** (strong) → +0.5 CVI-L.
**Pattern check:**
- The anchor's engine is **an object handed over without a word**. Ch.16 is a gift with a word ("You admired it.") and Ch.17 is a bystander's appetite, so the engines differ.
- **Watch:** Ch.16's bracelet and Ch.18's watch are both a gift worn on the wrist two chapters apart. The page keeps them apart (the steel is moved off the gold), and R8 removes the shared closing sound.

## The Shareability Test
- **What a reader texts a friend:** "They get MARRIED on the DOCK in TEN WORDS because the captain won't sail with them otherwise, the mule boy cries, and then a mule kicks the witness into a pile of rope."
- **Running count:** the book now has at least six shareable chapters (Ch.6, 8, 12, 15, 17, 18).

---

## Reader Reports

### The Devourer (2.6k after a 6.9k chase that ended mid-run)
- **The relief is instant.** The sail is theirs within a paragraph, and Felix is literally sitting on the plank to hold the ship.
- **The slow patch:** l.11–15, the goose, the tug-of-war and the sail mechanics with the tow boat, before anyone speaks. They will skim the rigging.
- **What pulls them through:** the master's condition, delivered as a grievance; "You have till the yard's at the top."; a ten-word wedding; a mule fight against a clock. After that the closing line hands them to Part Two.
- **Where would they stop?** Nowhere in the chapter, and probably not at its end either.

### The Critic
- **Would underline:**
  - "Felix took it and put it on, and cried underneath it.";
  - "The fig was all that was left on the quay, in its jar by the ring, and me.";
  - "Gold that soft took a scratch from anything, and it had a child's teeth in it already.";
  - "the dun stood still in the dark he had made her, with her ears turning.";
  - "As I was told at sunrise, and nobody on my ship has lied to anybody.";
  - "Then she's nobody's, which is worse.";
  - "Father, was mine like that?" / "Yours had a cake,";
  - "The rest of it outran me.";
  - "I put the crown back on him."
- **Would notice and mind:**
  - three present-tense similes in a past-tense book whose narrator has no present (R3–R5);
  - "Valens said, too late", which they last read in the heat scene (R11);
  - the road comparison for his look, last used for his hands in bed (R6);
  - the master's Latin described by its endings, the way the herald's and Valens's speech were (R10).

### The Hostile
- **"Did he set it, or is the reader meant to guess?"** The reader is meant to work it out from "twenty to one" beside a short shadow tipped east. That is consistent at Lechaion, a little after solar noon (audit W-03). The disruptor's cut stands, and the page is honest.
- **"Three sailors have been hauling a boy off a plank since mid-morning?"** The page says he has been on it since the third hour and that the pulling started later ("since the shadow was over by that post"). It is comic, and it is the master's restraint. Kept.
- **"Felix calls Plautia 'the lady with the litter' after living a winter in her brother's house?"** (audit W-01, optional, not applied.) It is a boy's tag for a lady who goes everywhere by litter. INVESTIGATE only.
- **"Is a quayside consent marriage valid between a Roman freedman and a peregrine woman?"** Yes, as *matrimonium iuris gentium* (audit I-01). The page claims nothing more.
- **"The watch's crown takes two turns at 12:40?"** Yes, if he wound it at dawn as Ch.11 shows (W-02, applied).
- **"Why is the sailor kicked?"** As written, Valens warns him "too late". After R11, the sailor turns to answer Valens's warning, and that is when the dun kicks. The cause is now on the page, with no comment.

### The Casual Reader (airport, 10 pages)
- **Would buy, and would tell a friend.** The chapter gives this reader everything they came for:
  - the man finally says it, and it is six words;
  - she says yes and asks him back;
  - the boy cries so hard he cannot stop, and says it is because nobody threw nuts (after C1);
  - a grumpy captain wants his sandal back;
  - a mule kicks the witness into a coil of rope;
  - the boy goes aboard in his underwear with a crown on.
- **The watch** is felt even by a reader who does not follow the sun: the dead father's watch, still running, handed back without a word.
- **No vibes problem.** **9.0** (9.5 is possible after C1; the nuts line is the kind they read aloud to someone).

### The Devoted Reader (active: long saga)
- **Would adopt it.** This is the chapter Reddit threads quote.
- **What they will find:**
  - the watch going from fast-by-the-trough (Ch.11) to right-by-the-sun, unexplained;
  - Felix crying "in front of everybody" after Ch.15's "Not in front of everybody";
  - the fig in its jar after "In a pot, it goes where I go.";
  - the bracelet's tooth marks deciding which wrist;
  - the master's daughter, married by messenger, as the marriage this one is not.
- **What they will catch (and should not):**
  - Felix's sun excuse as Plautia's smoke excuse (C1);
  - Valens "watching" elsewhere while Mara handles her things, as in Ch.13 (C2);
  - "said, too late" (R11);
  - the road look (R6);
  - the Ch.17 wind (R2).
- This reader drives CVI-Legacy, not launch.

---

## Cross-Reader Matrix
| Issue | Devourer | Critic | Hostile | Casual | Devoted | Severity |
|---|---|---|---|---|---|---|
| R1 sample-06 hammer + retired "in a hurry" + PFN | | ✓ | | | ✓ | **SHOULD FIX → blocking** (reserved sample; retired phrase) |
| R3–R5 narrating-present similes ×3 | | ✓ | ✓ | | | **SHOULD FIX → blocking** (voice-dna §0.4) |
| R6, R9, R11 Ch.15 heat frames outside heat | | ✓ | | | ✓ | **SHOULD FIX → blocking** (SPENT) |
| C1 Felix's irritant excuse = Plautia's anchor skeleton | | ✓ | | | ✓ | SHOULD FIX |
| R2 Ch.17's last-paragraph wind, two pages later | ✓ | ✓ | | | ✓ | IMPORTANT |
| R8 Ch.16 bracelet closing sound on the watch | | ✓ | | | ✓ | SHOULD FIX |
| R7, R10 CLOSED frames re-nouned | | ✓ | | | | INVESTIGATE → blocking (CLOSED) |
| R12 #11 ×2 in a <3k chapter | | ✓ | | | | INVESTIGATE → blocking (short-chapter rule) |
| C2 Valens's Ch.13 look-away | | | | | ✓ | INVESTIGATE → fix (signature forming) |
| C3, C4 tag verbs / said-to ×2 | | ✓ | | | | INVESTIGATE → fix (cap 1) |
| R13 Ch.16 "not much of it" | | ✓ | | | | INVESTIGATE |
| D1–D4 in-chapter doubles | | ✓ | | | | INVESTIGATE |
| Descriptive l.11–15 before the first line | ✓ | | | | | INVESTIGATE (not changed) |
| "the lady with the litter" | | | ✓ | | | INVESTIGATE (not changed) |

**No CRITICAL. No VIBES PROBLEM.** The blocking items are book-law, not reader-facing.

---

## Revision Recommendations (Ranked)
*Every replacement string below was put through the same reuse checks as writer prose:*
- *the 3–7-gram scan against Ch.1–17 and all voice-bank samples, stop-word-bounded strings included;*
- *content 3-grams against Ch.15–17;*
- *the in-chapter repeat scan;*
- *a grep of every at-risk frame;*
- *the real gates, with the whole set swapped in.*

*The first drafts of six replacements failed these checks and were changed before the set was tested. They are logged under "Replacement strings rejected".*

### Fix order: Logic (none) → Character (C1–C4) → Reuse and law (R1–R13) → In-chapter doubles (D1–D4)

| # | Location | Problem type | What happens now | Why it fails | Revision direction (exact swap) | Project rule? |
|---|---|---|---|---|---|---|
| C1 | l.85 | Character / Voice | "It's the sun," he said. "I've been sat in it since sunup. Don't look at me." | Plautia's Ch.16 anchor skeleton (tears blamed on an irritant: "The smoke has got into my eyes."), two chapters on, in another mouth. | → "It's the nuts," he said. "There should have been nuts. Don't look at me." This is his own grievance from l.63. The excuse is Felix's, and the tears are still his. | Yes: **tears excused by an irritant: CLOSED at 1 (Ch.16).** |
| C2 | l.107 | Character | "He was watching the dun." | Valens's Ch.13 look-away during Mara's handling of her small things ("He was watching the crowd past my shoulder while I did it"); 3rd "He was watching the [X]". | → "Valens was minding the dun." Same evasion, his animal axis, a fresh verb. | Yes: Valens's look-away at an object hand-off **CLOSED at 2**. |
| C3 | l.115 | Style (narrator move) | "Best plank in Lechaion, that," he promised her as they came, and she put one forefoot on the wood. | A said-to-the-animal tag (cap 1; "told the harbor" holds it) plus a non-"said" tag. | → "Best plank in Lechaion, that." She put one forefoot on the wood. (untagged; Felix is the paragraph's subject) | No |
| C4 | l.127 | Style | "the sailor complained from the coil." | A non-"said" tag. ("said from the" was rejected: it would be its 3rd book-wide use.) | → "the sailor said." | No |
| R1 | l.9 | Style (sample lift; retired) | "across the basin somebody was hammering at a hull, two blows and a rest, two blows and a rest, as if nothing in Achaea were in a hurry." | sample-06's reserved Ch.24 hammer rhythm; "in a hurry" retired from narration (6th use); a paragraph-final negation. | → "across the basin a man sat in a beached boat mending a net and whistling, as if the afternoon were his to spend." The indifference stays, now through a mender (Mara's eye). It is positive, with no count and no negation. | Yes: **add sample-06's "N blows and a pause" to the reserved-sample frames.** |
| R2 | l.9 | Style (adjacent-chapter echo) | "and the wind blew straight in off the water into our faces;" | Ch.17's last paragraph: "The wind blew harder into our faces". | → "and a wind straight in off the water flattened my dress against my legs;" ("the wind came" would be a 3rd use, and "the wind off the" is sample-01's; both rejected.) | Yes: **a chapter's opening paragraph is grepped against the previous chapter's last two paragraphs.** |
| R3 | l.15 | Voice (narrating present) | "the way cords hold up a blind." | Present tense in narration (§0.4; after-Ch.13 block). | → "like a blind on its cords." ("drawn up" would be a 3rd use, and "pulled up" ×5; both rejected.) | Yes: **present-tense generic simile in narration: 0 (gate proposal).** |
| R4 | l.83 | Voice | "as a far younger boy cries," | Narrating present. | → "like a boy half his age," | (as R3) |
| R5 | l.115 | Voice | "like a diving board after somebody has gone off it," | Narrating present. ("had gone off" would be a 3rd use; rejected.) | → "like a diving board after a jump," | (as R3) |
| R6 | l.71 | Style (vehicle reuse) | "and he gave me the look he gave a stretch of road before he took the mules onto it." | Ch.15's heat comparison: the same vehicle (road) for the same tenor (his attention to her). The bible says no vehicle domain is used twice. | → The whole sentence becomes: "Valens faced me with flour dried white in the hair of his forearms, a few pine needles in it, and the crown hanging from his hand." The held moment is left bare, and what she sees is material (her axis). ("looked at me for as long as…" was rejected: the gaze marker belongs to sample-02, and "as long as the" was another reuse.) | Yes: **Ch.15's heat block (strings AND frames) is reserved: no heat-scene skeleton outside a heat scene.** |
| R7 | l.79 | Style (CLOSED frame) | "a gray man with tar to the elbows," | The "[substance] to the [joint]" depth frame, CLOSED after Ch.9. ("tar on his arms" was rejected: "on his arms" is Ch.17's floured Valens.) | → "a gray man stained with tar," (l.121's "tar-handed" still IDs him) | No (already a rule) |
| R8 | l.111 | Style (prev. anchor skeleton) | "…and pressed until it shut on my wrist with a small dry snap." | Ch.16's bracelet: "shut again round my wrist with a click". ("until it held" was rejected: it doubled l.109's "held my right arm out".) | → "…and pressed." The next sentence already has "once the catch was home". | No |
| R9 | l.147 | Style (Ch.15 SPENT) | "before she trusted her weight to it;" | Ch.15 heat "trusted the poles with his weight"; Ch.6 "before he trusted it". ("let it take her" was rejected as the 5th "she let it"; "gave it her weight" doubles "The plank gave".) | → "before she stepped;" | No |
| R10 | l.31 | Style (CLOSED frame) / "without" | "a harbor Latin with the ends of the words knocked off, and he threw it down at us without leaving the rail." | The delivery frame (endings described; speech laid or thrown down), CLOSED after Ch.16; the "without" family at density. | → "a harbor Latin stuffed with sailors' Greek, and he stayed at the rail to use it on us." Vocabulary, not endings, and Mara's classicist ear. "quick" keeps "The rest of it outran me." | No (already a rule) |
| R11 | l.123 | Style (Ch.15 SPENT) | "Keep off her heels," Valens said, too late. | Ch.15 heat: '"Mind the roof," I said, too late.' ("Valens said." and "Valens said, and…" were both rejected: the tic gate failed "valens said the", and the echo scan flagged "valens said and", Ch.6.) | → "Keep off her heels," Valens called, and the sailor turned to answer him. The cause of the kick goes on the page, with no comment. | Yes: **"said, too late" CLOSED at 1.** |
| R12 | l.69 | Style (#11) | "until a white froth came up between them, to draw the bitterness out, and then she had eaten" | A purpose tail; the 2nd firm #11 in a <3k chapter. | → "until a white froth came up between them, and rinsed it off under the tap, and then she had eaten" (an act, not a reason) | No |
| R13 | l.55 | Style | "I found enough breath for Latin, if not much of it." | Ch.16 Mara: "there is not much of it" (her Greek). | → "I found breath enough for Latin, barely." | No |
| D1 | l.105 | Style | "…and stood hard. / The hands stood at twenty to one" | Adjacent "stood". | → "The hands were at twenty to one," | No |
| D2 | l.97 | Style | "The girl in the blue hood had taken…" | The l.69 paragraph opener repeated; the role label as a tag. | → "The master's daughter had taken…" | No |
| D3 | l.143 | Style | "before it reached the water between the quay and the hull." | "between the quay and the" ×2 (l.115). | → "before it reached the slot of water by the hull." | No |
| D4 | l.159 | Style | "…and the jar between us." | "between us" in consecutive sentences (l.155). ("held level" was rejected: it doubled R8's interim "held".) | → "…and the jar kept level." | No |

**Not changed (judged; INVESTIGATE only):**
- "the lady with the litter" (W-01's optional item);
- "Is that all of it?" (Ch.11's skeleton, ordinary English, seven chapters apart);
- the cucumber trigger, "a girl … was eating a cucumber" (sample-03 opens on "The woman next to me was eating…". This is a trigger, not the sample's content. Watch it: the next eating-stranger trigger is a different act);
- "blood" ×2 in the run-body beats (l.9, l.37);
- the two nails on the watch (Mara's on the crown, Valens's on the catch: a designed mirror);
- "Cover her eyes, Felix. Her eyes." (Valens, urgency, once);
- "I wiped it clean with my thumb": "with my thumb" is its 3rd book-wide use (Ch.3, Ch.9), and the gate passes it. Every swap I tried (thumbed, cleared, rubbed) collided with something else. Leave it.

**Replacement strings rejected during testing** (so the editor does not reach for them):
- "the wind came in off the water" (a 3rd "the wind came"); "the wind off the" (sample-01);
- "sat on an upturned boat" (the 4th "on an upturned", Ch.6/7/11);
- "drawn up on its cords" / "pulled up";
- "looked at me for as long as the yard would let him" (sample-02's gaze marker; Ch.11);
- "took his time" (a 3rd use, Ch.4/5);
- "tar on his arms";
- "He had turned his head to the dun" (Ch.9's spent mutual-look sentence);
- "His face was toward the dun" (Ch.11's spent near-kiss "his face was");
- "pressed until it held" (doubled "held");
- "let it take her" (a 5th "she let it");
- "after somebody had gone off it" (a 3rd "had gone off");
- "There ought to have been nuts" (a 3rd "ought to have"); "There were meant to be nuts" (a 4th "meant to be");
- "I thumbed it clear" (Ch.16's "thumbed it on");
- "he said as they came" (a 3rd "he said as");
- "the sailor said from the coil" (a 3rd "said from the");
- "Valens said." (tic FAIL, "valens said the" ×3); "Valens said, and the sailor…" (an echo of Ch.6);
- "Valens told him" + "The dun…" (a 3rd "told him the").

### The fix script and the tested result
- **Script:** `/tmp/claude-0/-home-user/63791ee5-159c-5791-9429-07920f8d9417/scratchpad/ch18-fixes.py` (`python3 ch18-fixes.py <in.md> <out.md>`). It holds 20 swaps, and each OLD string must occur exactly once or the script aborts.
- **Tested output:** `/tmp/claude-0/-home-user/63791ee5-159c-5791-9429-07920f8d9417/scratchpad/ch18-fixed.md` (md5 `55741e53…`, sha256 `50dd464e…`). Header comments untouched.
- **Results with the copy swapped into the manuscript path, run from /home/user/Books:**
  - `check_chapter.sh 18`: **all clean.**
    - style: simile 2.0/1k, em-dash 1, foreshadow 0;
    - grammar 0; rhythm 0;
    - show/tell 2,532 words, dialogue **34.3%**, no flags;
    - voice-wear strict clean;
    - tic gate clean (and-chains 2/9, credential 0, pivots 0, "So" 0; gesture classes clean);
    - echo 0; command echoes none; spoken-line echoes none;
    - metaphor 2.0 fig/1k, median 15;
    - shape CLEAN.
  - `tic_report.py --gate`: clean.
  - `--echoes 18`: none / none / none.
  - `shape_check --strict`: `18 2528 0 34 15 I-statement punch`, CLEAN. The book stands at 99,212 words.
- **Restored:** the manuscript checksum was verified after every run (sha256 `20539561…`, md5 `629fcb53…`).
- **Post-fix numbers:**
  - **2,528 words** (shape_check), 2,536 (style), 2,532 (show_tell). That is 28 above the 2,500 floor, against a 2,800 target and a 2,500–3,100 range: −54 words in total. Six swaps are net cuts; the rest are near word-for-word.
  - **dialogue 34.3%** (band 30–40, floor 30 ✓); median 15 (mid ✓); 0 breaks; `I-statement` → `punch`.
  - **#11:** 1 firm (0.40/1k) ✓. **Paragraph-final negations:** 1 (0.40/1k) ✓. **"without":** 3 (1.16/1k).
  - **"as if":** 1. **Narration indefinites:** 2. **Narrating-present similes:** 0. **Similes:** 4 in narration (1.6/1k).
  - **Anti-AI:** 7/20, −0.875.

---

## Strengths to PRESERVE (do not touch in polish)
- **The ten words, and Mara asking him back** ("Yes. Will you?").
- **"Felix took it and put it on, and cried underneath it."**
- **The watch stretch:**
  - "He took out the watch and laid it in my hand. / The case was warm from him.";
  - the flour on the crystal;
  - the seconds hand "the only thing moving on that quay that nobody was shouting at";
  - "it took two and stood hard";
  - twenty to one by the shadow;
  - **no word from Valens**;
  - the wrist choice and "a child's teeth in it already";
  - "The watch sat on the wrong wrist and ticked."
- **Pacuvius:** his whole condition speech, "Then she's nobody's, which is worse.", "Throw a nut at this ship…", "nobody on my ship has lied to anybody", the sandal.
- **The daughter:** "was mine like that?" / "Yours had a cake," and the bitter end dropped over the rail.
- **The tunic blindfold,** "the dark he had made her", "I put the crown back on him.", "is she wearing it to Italy?" / "Ask her,".
- **The close:** "The fig was all that was left on the quay … and me.", "the little tree shook all its leaves between us", "Tread on the cleats," and the plank drawn in.
- **The disruptor's cut of the Ch.11 recall.** Do not restore it in any wording.

---

## PATH TO 8.5 (mandatory; the Floor is 8.0)
- **Prose & Voice 8.0 → 8.5 requires the reuse and law cluster gone, with no new repeat moved sideways.**
  - The sentences already carry the stopping power ("cried underneath it"; "and me."). What is missing is a page that reaches for nothing the book has spent.
  - **Surgery, in this order:**
    1. **l.9 (R1 + R2):** the opening paragraph's second sentence. Replace the sample-06 hammer, the retired "in a hurry" and Ch.17's "into our faces" with the net-mender and the wind on her dress. The first sentence (the ledger sig) is untouched.
    2. **The three present-tense similes (R3 l.15, R4 l.83, R5 l.115).**
    3. **The Ch.15 heat frames:**
       - **R6 l.71:** the proposal's road look becomes the needles in the flour; the moment is left bare;
       - **R9 l.147:** "trusted her weight";
       - **R11 l.123:** "said, too late".
    4. **The Ch.16 frames:** **R8 l.111** (the clasp's snap) and **R13 l.55** (breath for Latin).
    5. **The CLOSED frames:** **R7 l.79** (tar to the elbows) and **R10 l.31** (the master's Latin by its endings).
    6. **The density:** **R12 l.69** (the memory's purpose tail).
    7. **The doubles:** **D1–D4**.
  - **Expected:** Prose 8.5. The underline set is untouched, #11 drops to 1 firm, and every gate stays clean.
- **Characters 8.5 → 9.0** (not floor-holding, but the PATH carries it): **C1** (Felix's excuse becomes his own nut grievance), **C2** ("Valens was minding the dun."), and **C3/C4** (tags).
- **Run all 20 swaps together** (the script). They were tested as one set; applying a subset leaves interim doubles (for example, "until it held" next to "held my right arm out").

---

## Pacing check (one line for `feedback/progress.md`)
**Ch.18 (cycle 0):** Single-scene, under an hour on a sunlit quay, the same early afternoon as Ch.17's run. It sits between Ch.17's In medias res and Ch.19's Chronological ✓.
- **Length:** 2,582 words (target 2,800, −8%, inside 2,500–3,100; not padded). 2,528 after the PATH, still inside.
- **Dialogue** 33.6% (30–40 ✓; 34.3% after); **0 breaks** ✓; **gear median 15** (mid ✓).
- **Signatures:** `I-statement` → `punch`. Ch.16 is `dialogue` → `question` and Ch.17 `short-punch` → `quiet`, so nothing runs three in a row.
- **Neighbours:**

  | Ch | Words | Gear (median) | Dialogue | Approach | Breaks | Open → close |
  |---|---|---|---|---|---|---|
  | 16 | 7,175 | mid (14) | 46% | Parallel | 6 | dialogue → question |
  | 17 | 6,909 | low (12) | 33% | In medias res | 3 | short-punch → quiet |
  | **18** | **2,582 → 2,528** | **mid (15)** | **34%** | **Single-scene** | **0** | **I-statement → punch** |
  | 19 | 8,400 planned | high | 20–30% | Chronological | 4 | scene-set → long-fade |

- **The hinge is short and quick after a long chase, as designed.** Three long chapters (7.5k → 7.2k → 6.9k) give way to 2.6k, and the next is 8.4k. The gear steps low → mid → high, and the variance is the design.
- **Emotional slot ✓:** after comedy under legal threat (Ch.17), the romance's public turn, ten words and a gift, before Part Two opens on Italy. It is the book's first short chapter since Ch.14, at about 41% of the book.
- **Value shift ✓:** refused (−) → married (+) → loading collapses, the yard up (−) → aboard (+).
- **Pull ✓:** the punch hands off to Ch.19's "By the time the goose ship…" with no hook beyond the act. That is right for a hinge.
- **Slow patch:** l.11–15 (descriptive, before the first line). Not changed: it is the ledger's in-moment arrival, and Felix on the plank is inside it.
- **Book:** 99,266 words against 106,600 cumulative target (−6.9%); about 99.2k after the PATH. Projected at about 241k against the 220k floor ✓ and the 245k target (slightly under: watch it, never pad).

**Verdict: OK.**

---

## Cross-Book Pattern Detection (Ch.1–18)
1. **Ch.15's heat scene is being mined outside heat.**
   - W-12 caught "the heat of him", and the page still carries three more: "said, too late", "trusted … weight" and the road comparison.
   - Ch.15 is the book's most-quoted source chapter, and its strings are spent while its frames are not tracked.
   - **Proposal (UPDATE RULE, root `tools/tic_report.py` and the template):** a **reserved-chapter frame registry**, like the sample-frame registry that Ch.17's Cross-Book #1 proposed. The Ch.15 heat block's frames are written as patterns and fail on sight outside Ch.23 and Ch.34. Examples: `\bsaid, too late\b`, `\btrusted\b.{0,30}\bweight\b`, and a road vehicle for Valens's attention.
2. **The voice bank is still leaking by structure.**
   - sample-06's counted hammer rhythm opens this chapter (R1). sample-03's "a woman next to me was eating…" trigger shape recurs (INVESTIGATE).
   - **Add sample-06's `\b(two|three|four) blows and a (pause|rest)\b` to the reserved-sample frames.**
3. **Narrating present inside similes** is new at this density (3 in 2.6k).
   - **Gate proposal:** in narration, flag `\b(the way|as a|like a)\b[^.;]{0,60}\b(\w+s|has|have|does|do)\b` when the verb is present tense.
4. **Retired narration phrases survive because the gate does not hold them.** "in a hurry" was retired after Ch.9 and came back.
   - **Gate proposal:** a narration-only retired list in `tic_report.py` (`in a hurry` cap 0).
5. **The previous chapter's last paragraph comes back in the next chapter's first** ("the wind blew … into our faces").
   - **Rule:** the opening paragraph is grepped against the previous chapter's closing two paragraphs, stop-word frames included.
6. **The anchor of the chapter before last comes back as a skeleton** (Plautia's irritant excuse → Felix).
   - The after-Ch.17 rule ("the evaluator's underline and anchor sentences are added to the at-risk block as skeletons") should be applied **two chapters back**, not one.
7. **What varies, as it should:**
   - the structure (Single-scene after In medias res);
   - the opening (`I-statement`) and ending (`punch`, action);
   - the gear (mid);
   - the anchor's engine (a wordless gift);
   - the body rebel (Felix's, not Mara's);
   - the length (the first punch chapter since Ch.14).

**Bookkeeping (orchestrator):**
- **Re-sync the bible's Ch.18 blocks to the final page.** They quote the Writer's draft, and the continuity repair, the disruptor and (after the PATH) these swaps have all moved on since. Examples:
  - **At-risk after Ch.18:**
    - "the crown 'stood hard against my nail; the spring was wound tight to its end.'" → page: "it took two and stood hard";
    - "the only thing on that quay that moved without being shouted at" → page: "the only thing moving on that quay that nobody was shouting at";
    - "shorter than my sandal" → page: "a short shadow";
    - "the Ch.11 fast reading recalled once" → cut, and must not be restored;
    - "'as if' 1 (the barrel hoop)" → after the PATH, the net-mender;
    - the voice breaking on "Yes" → cut (W-07);
    - '"Yes." / "Will you?" / "Yes,"' → page: "Yes. Will you?" / "Yes," said Valens;
    - "We're all of us" → "We are all of us";
    - "Nobody passed us with the news," → "We were the only two people leaving,".
  - **FELIX:** "Did you get it?" (cut); "Nobody ever told me she was."; "Who's to carry the torches, then?"; "with nobody throwing nuts at you"; "Nobody look." (cut); "Up, you." → "On, you,"; "It's the sun" → (after the PATH) "It's the nuts" / "There should have been nuts.".
  - **VALENS:** "Twice over." (cut); "shorter than my sandal"; "He was watching the dun." → (after the PATH) "Valens was minding the dun."; the clasp's "snap" (cut after the PATH); the road look → (after the PATH) the needles in the flour of his forearm hair; "Keep off her heels," … "and the sailor turned to answer him."
  - **PACUVIUS:** audit W-14's list, plus "with the ends of the words knocked off" (Mara's description) → (after the PATH) "a harbor Latin stuffed with sailors' Greek". **The card's "Mara's one description of it; never again" still holds.**
  - **The Ch.18 walk-on note:**
    - "by Castor" → "by Pollux";
    - "tar to the elbows" → (after the PATH) "stained with tar";
    - "complained" → "said";
    - "a barrel-hoop hammerer ('two blows and a rest')" → (after the PATH) a man in a beached boat mending a net and whistling;
    - the fish-seller's "Whose is the black?" → "That black's yours, is she?";
    - "hits a dog" → cut;
    - "six rowers" → "a rowing boat".
- **At-risk after Ch.18, add (after the PATH):**
  - **tears excused by an irritant:** CLOSED at 1 (Ch.16);
  - **"said, too late":** CLOSED at 1 (Ch.15);
  - **Valens's look-away at an object hand-off:** CLOSED at 2 (Ch.13, Ch.18);
  - **a road as the vehicle for Valens's attention to Mara:** SPENT (Ch.15);
  - **a clasp or catch closing on her wrist, rendered by its sound:** SPENT (Ch.16);
  - **narrating-present similes:** 0, restated;
  - **"in a hurry" in narration:** 0, restated, with a gate proposed;
  - **sample-06's counted hammer:** reserved for Ch.24 in any count;
  - **the opening paragraph never reuses the previous chapter's last paragraph;**
  - **the watch:** no "…and ticked." one-liner again; Ch.44's watch on her wrist is worded fresh and never recalls "the wrong wrist";
  - **said/told-the-[non-listener]:** the 5th book-wide ("told the harbor"), so **Ch.19 gets none** (audit I-12);
  - **similes spent:** the blind on its cords; a boy half his age; a diving board after a jump. **Vehicles spent:** blind, diving board.
- **Entity and handoff cascades:**
  - The watch is on Mara's **RIGHT** wrist.
  - Felix's tunic is on the dun, and the crown is on Felix.
  - The leaf is under Valens's tunic, and the pen-knife is in Mara's belt.
  - The goose ship is under tow on the afternoon breeze. Do not compress the crossing into a night (audit I-03).
  - Pacuvius and the daughter are aboard. The gray sailor gets "something else" if he returns.

---

## VERDICT
**POLISH. Gate NOT MET.**

| Measure | Result |
|---|---|
| Genesis Floor | **8.0** (Prose & Voice, merit; no cap) |
| Average | **8.79** |
| Casual | **9.0** |
| Scores | Originality 9.0 · Theme 9.0 · Characters 8.5 · **Prose 8.0** · Pacing 9.0 · Emotion 9.0 · Immersion 9.0 |
| Pacing | **OK** |
| CVI-Launch (CVI-L) / CVI-Legacy | **10.0** (9.49 + 0.5) / 7.1 (provisional) |
| Mechanical suite | all clean (echo 0, spoken-line echoes none, command echoes none, tic gate clean, voice-wear strict clean, shape CLEAN) |
| Foreshadowing / watch loading (END-1) | 0 / none |
| AUTHOR-CP3-3 / CP3-5 / END-1 | ✓ / ✓ / ✓ |
| Non-negotiables (ten words before witnesses; Felix cries; the sailor wants on; the watch back wound, no speech, nothing explained; the mule refuses) | ✓ all |
| Memory triggered by the scene | ✓ |
| Explanation density | **✗** by the short-chapter rule (2 firm, allow 1) → 1 |
| Paragraph-final negations | ✓ 0.77/1k → 0.40/1k |
| No comparison in Valens's speech | ✓ |
| Command echoes / borrowed whole lines | 0 / 0 (one skeleton → C1) |
| Tics | catchphrases 0; gate classes clean; **said-to ×2, non-said tags ×2, Valens's look-away (2nd) → fixed** |
| Reuse (sample-06; Ch.13, 15, 16, 17; CLOSED frames; retired "in a hurry") | **FAIL** → cleared |
| Narrating present | **FAIL ×3** → 0 |
| "without" family | 4 (1.55/1k) → 3 (1.16/1k) |
| AI patterns | 7/20, −1.0 → 7/20, −0.875 (clean) |

**After the PATH (20 swaps, tested together):**
- **2,528 words**; dialogue **34.3%**; median 15; 0 breaks; `I-statement` → `punch`;
- every gate clean; anchors byte-identical;
- **forecast Floor 8.5 / Average 8.93 / Casual 9.0 (9.5 possible) / PASS.**
- **Next steps:** run E (gates) and F (re-evaluation).

This chapter is the hinge, and it earns that place. Two people marry in ten words on a hot quay to satisfy a stranger's mother-in-law. The boy who has held the ship by sitting on its plank since mid-morning cries under a crown with no needles left. The man hands back her father's watch with flour in its links, wound and set by the sun, and says nothing at all. What holds it below the gate is small and countable. Its sentences keep borrowing frames the book has already spent:
- a hammer from the labor sample;
- three lines from the first night in the hut;
- the bracelet's click;
- the last chapter's wind.

**BIAS CHECK:** This evaluation was produced by the same system that wrote the prose. Confidence in scores above 8.0 requires external validation (beta readers, editors, comp analysis).
- **CVI-L 10.0 is a formula ceiling, not a claim.** Every input but Commercial Pacing and Casual saturates on a short romance hinge. The useful signal is the running Ch.12–18 line, and that this chapter tops it.
- **C1 changes a line the disruptor protected** ("It's the sun"). I judge the irritant-excuse skeleton to be Plautia's, two chapters back. A reader who holds the excuse to be universal human behavior would call C1 optional. Then Characters rests on C2–C4, and the PATH still clears the floor.
- **R6 removes a comparison many readers will like.** The road look is Valens's own attention axis. I count it because the bible says no vehicle is used twice, and Ch.15 used the road for his attention to her body. The replacement (needles in the flour) keeps Mara's eye on the man at the moment of the question.
- **R10 rewrites a description the PACUVIUS card endorses** ("Mara's one description of it"). I count it because the after-Ch.16 delivery frame is CLOSED by attention channel (endings; speech set down), not by string.
- **Characters 8.5 → 9.0 and Prose 8.0 → 8.5 are forecasts, not scores.** Originality, Theme, Pacing, Emotion and Immersion at 9.0, and Casual 9.0, are one-chapter judgments by the system that wrote the book.

---
---

# Re-evaluation after cycle 1
**Evaluator:** book-evaluator (independent; did not write, revise or apply any of this prose) | **Date:** 2026-10-21
**Text evaluated:** `manuscript/chapters/chapter-18.md`, md5 `55741e53f482f00bea489e07bc2e701a`, sha256 `50dd464e…`. That is **byte-identical to the tested copy** `ch18-fixed.md` (md5 checked side by side), so all 20 swaps are in exactly as tested. **2,528 words** (shape_check), 2,536 (style), 2,532 (show_tell); dialogue **34.3%**.

**Read against:**
- the book's CLAUDE.md;
- STATE.yaml AUTHOR-CP3-3, CP3-5 and END-1;
- voice-dna §0–§4;
- character-bible.md: the at-risk blocks after Ch.16, Ch.17 and Ch.18, the Retired / at-risk table, the PACUVIUS card, the VALENS and FELIX Ch.18 blocks, the Ch.18 walk-on note and the roles table;
- outline `## Chapter 18` and Ledger row 18;
- Ch.17's close in full;
- `disruption-chapter-18.md`, for what the disruptor cut.

**chapter-19.md:** none in `chapters/`.

**Measured on the current page** (`bash books/the-hour-of-ash/tools/check_chapter.sh 18`, from /home/user/Books): **clean on every gate.**
- style: simile 2.0/1k, em-dash 1, foreshadow 0;
- grammar 0; rhythm 0; show/tell no flags;
- voice-wear strict clean;
- tic gate clean (and-chains 2/9, credential 0, pivots 0, "So" 0, gesture classes clean);
- echo 0; metaphor 2.0 fig/1k, median 15;
- `shape_check --strict`: `18 2528 0 34 15 I-statement punch`, CLEAN.
- **`tic_report.py --echoes 18`: none / none / none** (echoes, command echoes, spoken-line echoes).

## Verification of the 20 swaps (did any of them introduce something new?)
**Method.** I word-diffed the cycle-0 page (md5 `629fcb53…`) against the current page, then checked every replacement string four ways:
- a 3–7-gram scan against Ch.1–17 and all 13 voice-bank samples, stop-word-bounded strings included;
- a string grep across the book;
- a frame check against every SPENT, CLOSED and RESERVED entry in the bible;
- a check against what the disruptor cut.

| Swap | New string | Verdict |
|---|---|---|
| C1 | "It's the nuts," … "There should have been nuts. Don't look at me." | **Clean.** The excuse is now his own grievance (l.63), with no irritant and nothing explained. "It's the" is ordinary speech (Ch.17 ×2). |
| C2 | "Valens was minding the dun." | **The string is clean, but it creates a skeleton double.** "Valens was [V]ing the [mule]." now opens l.107 and l.141 ("Valens was chasing the black."), and it makes a third "Valens was" paragraph opener (l.155) → **F2** |
| C3 | "Best plank in Lechaion, that." (untagged) | **Clean.** Felix is the paragraph's subject; "She" is the dun. |
| C4 | "the sailor said." | Clean. |
| R1 | "a man sat in a beached boat mending a net and whistling, as if the afternoon were his to spend." | **Clean** (0 hits). It is the chapter's one "as if", and it characterizes rather than explains. No count, no negation. |
| R2 | "a wind straight in off the water flattened my dress against my legs" | **The string is clean; INVESTIGATE.** Ch.17 l.536, nine paragraphs before its close, has the same breeze "came inland off the water … and it lifted the hair off my neck". It is the same wind, outside the last-two-paragraphs rule, and cycle 0 kept "in off the water" knowingly. **Not changed.** Ch.19's opening puts no weather on Mara's body. |
| R3 | "like a blind on its cords" | **Clean.** Ch.3's "like a blind woman" is another word (a person, not a window blind). |
| R4 | "like a boy half his age" | Clean. |
| R5 | "like a diving board after a jump" | Clean. |
| R6 | "…the hair of his forearms, a few pine needles in it, and the crown hanging from his hand." | **FAIL, on three counts → F1:** (1) **a cut repeat moved sideways.** The disruptor cut "the few needles still clinging to them" from the crown, and this puts "a few pine needles" on his arm. (2) It re-describes the crown indirectly (shed needles), and the after-Ch.17 block allows the crown "no re-description". (3) The with-X, Y, and Z cadence at the proposal is a new three-beat list over his body, which edges the CLOSED item-by-item gaze. |
| R7 | "a gray man stained with tar" | **Clean.** "the tar-handed sailor" (l.121) still identifies him. |
| R8 | "…with the edge of his nail and pressed." | Clean. |
| R9 | "before she stepped" | Clean (ordinary English). |
| R10 | "a harbor Latin stuffed with sailors' Greek, and he stayed at the rail to use it on us." | **Clean.** It describes vocabulary, not endings, and nothing is laid or thrown down. "to use it on us" is a wry purpose clause, not a #11. The card's "Mara's one description" holds. |
| R11 | "Valens called, and the sailor turned to answer him." | **Clean.** The cause of the kick is on the page, with no comment. "called" is volume. |
| R12 | "and rinsed it off under the tap" | **Clean.** It is an act; the purpose tail is gone. |
| R13 | "I found breath enough for Latin, barely." | **Clean.** It is breath, not a description of her Latin, so the CLOSED frame is untouched. |
| D1–D4 | "The hands were at"; "The master's daughter"; "the slot of water by the hull"; "the jar kept level." | **Clean.** D2 labels the girl before her "Father," line. Mara can infer it from "My girl's aboard" (l.41), and the joke is "was mine like that?", not who she is. INVESTIGATE only. |

**Summary:**
- **Added explanation: none.** #11 is 1 firm (0.40/1k).
- **Echo of an earlier chapter: none** by the gates. By hand, there are no whole spoken lines and no frames, apart from the R2 INVESTIGATE.
- **Repeat moved sideways: one** (R6's needles).
- **New triad: one, borderline** (R6's list).
- **New in-chapter double: one** (C2 against l.141).
- **One double the earlier passes did not catch (it predates cycle 1): "haul" ×8 in the chapter.** Most are rope (l.13, l.15 ×2, l.67), and those are right. But Felix's three fall within 25 lines (l.119 "He hauled.", l.135 "still hauling", l.143 "Felix hauled his tunic off"), and l.143's "tunic off" sits against Ch.17's last paragraph ("swept a tunic off it") → **F3**.

## Finalize fixes (F1–F3), tested together
| # | Location | Now | → Finalize | Why |
|---|---|---|---|---|
| F1 | l.71 | "Valens faced me with flour dried white in the hair of his forearms, a few pine needles in it, and the crown hanging from his hand." | "Valens faced me with flour dried white in the hair of his forearms and the crown hanging from his hand." | R6's three faults (above). This is the cycle-0 text minus the road look, so the moment stays bare, with Mara's eye on the flour, and the crown at the proposal stays (the comic image). |
| F2 | l.141 | "Valens was chasing the black." | "Valens had gone after the black." | Clears the C2 skeleton double and leaves two "Valens was" openers, which have different shapes. "gone after" and "after the black": 0 book-wide. |
| F3 | l.143 | "Felix hauled his tunic off." | "Felix peeled off his tunic." | "haul" 8 → 7, and Felix's three → two. The word order avoids "tunic off" (Ch.17's last paragraph). "peeled off his": 0 book-wide (Ch.1 has "peeled it off", Ch.15 "peeled it"). |

**Replacement strings rejected during testing:**
- "dragged his tunic over his head": it makes "tunic over" ×2 in one paragraph, against "threw the tunic over the dun's face".
- "stripped his tunic off": Ch.12's "He stripped his cloak off." (Valens).
- Changing l.107 instead of l.141: "had gone to the dun's head" would put him away from her in the sentence before she holds her arm out to him.

**Script and test:**
- **Script:** `/tmp/claude-0/-home-user/63791ee5-159c-5791-9429-07920f8d9417/scratchpad/ch18-finalize.py` (`python3 ch18-finalize.py <in.md> <out.md>`). It checks the input md5 is `55741e53…` and aborts on any OLD string that does not occur exactly once.
- **Tested output:** `/tmp/claude-0/-home-user/63791ee5-159c-5791-9429-07920f8d9417/scratchpad/ch18-final.md`, md5 `dbd5ac50047ee465bb51f78d85ac44a4`. Header comments are untouched.
- **Results with the copy swapped into the manuscript path, run from /home/user/Books:**
  - `check_chapter.sh 18`: **all clean.**
    - style: 2,531 words, simile 2.0/1k, em-dash 1;
    - grammar 0; rhythm 0;
    - show/tell 2,527 words, dialogue **34.3%**, no flags;
    - voice-wear strict clean;
    - tic gate clean (and-chains 2/9; gesture classes clean);
    - echo 0; command echoes none; spoken-line echoes none;
    - metaphor 2.0 fig/1k, median 15;
    - shape CLEAN.
  - `tic_report.py --gate`: clean, exit 0.
  - `--echoes 18`: none / none / none.
  - `shape_check --strict`: `18 2523 0 34 15 I-statement punch`, CLEAN, exit 0.
  - **Every replacement string was put through the reuse checks above** (3–7-grams against Ch.1–17 and the samples, stop-word-bounded strings included). The only hits are ordinary stop-word strings ("and the crown" Ch.6; "white in the" Ch.17, which is the forum paving; "and I caught it" Ch.7).
- **Restored:** the original was put back, and its checksums were verified (md5 `55741e53…`, sha256 `50dd464e…`). **I did not edit the manuscript.**
- **Post-finalize numbers:**
  - **2,523 words** (shape_check), which is ≥ 2,500 ✓. Against the 2,800 target that is −9.9%, inside the 2,500–3,100 range.
  - dialogue 34.3%; median 15; 0 breaks; `I-statement` → `punch`;
  - em-dash 1; "as if" 1; semicolons 5 (2.0/1k);
  - #11: 1 firm; paragraph-final negations 1; "without" 3.
- **The anchors are byte-identical:** the ten words; "cried underneath it"; the watch stretch from "He took out the watch" to "…and ticked."; the daughter's line and "Yours had a cake,"; the sandal; the tunic blindfold; "I put the crown back on him."; "…and me."; the closing line.

## Genesis Score (fresh; per-cycle cap of +0.5 against cycle 0)

| Dimension | Cycle 0 | **Cycle 1** | Evidence | Holds / caps |
|---|---|---|---|---|
| Originality | 9.0 | **9.0** | The anti-wedding is untouched: ten words to satisfy a stranger's mother-in-law; "Yours had a cake,"; the sandal; the wrist chosen by a child's tooth marks. **New texture:** R10's "a harbor Latin stuffed with sailors' Greek" is a classicist's ear, and it is right for a Puteoli shipmaster. | Not 9.5: the balking animal at the gangplank is a fresh execution, not a new beat. |
| Theme | 9.0 | **9.0** | "The fig was all that was left on the quay, in its jar by the ring, and me." / "the little tree shook all its leaves between us"; "Then she's nobody's, which is worse." It is never stated. The texture means nothing: the net-mender, the sprats, the rowers eating. | Not 9.5: the fig jar is the obvious emblem, and it lands because it is underplayed. |
| Characters | 8.5 | **9.0** (+0.5) | **C1–C4 cleared:** "It's the nuts," … "There should have been nuts." is Felix's own grievance from l.63, so the excuse is his and the tears are his. "Valens was minding the dun." is his animal axis, maintenance rather than a look-away. Both tags are clean. **Pacuvius** matches his card (consequence run-ons, then "Then she's nobody's, which is worse."; the sandal; never down the plank). **Cover-the-name:** PASS for all five speakers. **Chaos:** Mara 3/4, inhabited; Felix's body rebel. **NO-TICS:** no catchphrase; gate gesture classes clean (gate numbers used); no device. | **No cap.** Not 9.5: D2 labels the daughter before her line, and "the sailor" carries seven tags. **F2** clears the one new skeleton double. |
| **Prose & Voice** | 8.0 | **8.5** (+0.5, the cap) | **The law cluster is gone:** the sample-06 hammer, "in a hurry", the three narrating-present similes, the Ch.15 heat frames, the Ch.16 clasp sound and "not much of it", the CLOSED frames and Ch.17's wind-into-faces. **Stopping sentences:** "Felix took it and put it on, and cried underneath it."; "The fig was all that was left on the quay, in its jar by the ring, and me." **Underlines:** "Gold that soft took a scratch from anything, and it had a child's teeth in it already."; "the dun stood still in the dark he had made her, with her ears turning."; "As I was told at sunrise, and nobody on my ship has lied to anybody."; "The rest of it outran me." **Ugly sentence:** "The watch sat on the wrong wrist and ticked." **Voice under pressure:** the run is in the body and the Latin is cut off at the dash; the asides return at the cucumber. | **8.5 on the page with F1–F3** (all D-class: one cut detail restored, one skeleton double, one verb cluster; no law breach). #11 is 1 firm, inside the short-chapter rule. Not 9.0: the per-cycle cap, the rigging paragraph (l.15, #15), and "Gold that soft…" as the one explanation. Anti-AI 7/20, −0.875. |
| Pacing | 9.0 | **9.0** | The ledger row is hit on every hard field (Single-scene; `I-statement` → `punch`; 0 breaks; 34%; 2,523; median 15). The condition runs as talk; the ten words are three lines; the watch is the one deceleration; then the mule chaos runs against the yard. **Value shift:** − → + → − → +. | Not 9.5: l.11–15 still runs about 250 words of description before the first spoken line. |
| Emotion | 9.0 | **9.0** | **The anchor lands:** the watch, warm from him, with flour in the links, the crown taking two, twenty to one by the shadow, and no word said (END-1 ✓). **Surprise:** ten words and a mule. **Body rebel:** Felix. Mara's feeling goes into objects and acts, with zero intensity-words. Techniques ≥5. C1 makes the displacement funnier, and the tears are still his. | Not 9.5: there is no breath of Mara inside the ten words. That is correct restraint, and it carries a cost for part of the audience. |
| Immersion | 9.0 | **9.0** | Stern-to mooring, the *cheniscus*, brails through lead rings, the halyard made fast to a pin, the tow boat, consent before witnesses, "Yours had a cake," and "by Pollux". **New in cycle 1:** the net-mender, and sailors' Greek in harbor Latin. | Held. |
| **FLOOR** | 8.0 | **8.5** | Prose & Voice | |
| **AVERAGE** | 8.79 | **8.93** | (9.0 + 9.0 + 9.0 + 8.5 + 9.0 + 9.0 + 9.0) / 7 = 62.5 / 7 | |

**Casual Reader: 9.0.** An airport reader buys this:
- the six-word proposal and "Yes. Will you?";
- a gruff captain with one sandal;
- a boy crying under a bald crown who says it is because nobody threw nuts;
- a mule kicking the witness into a rope pile;
- the boy going aboard in his underwear, crowned.

The nuts line is the kind they read aloud. I hold the score at 9.0, not 9.5, because one funnier line does not change the whole chapter's vibe. **No vibes problem.**

**CVI-Launch: 10.0** (9.49 + 0.5 anchor, capped at the scale; unchanged, since no anchor was touched). **CVI-Legacy: 7.1** (provisional; unchanged).

## Anti-AI Scan (cycle 1 page, with F1–F3)
**Found (each minor):**
- **#1** forced symmetry: "He hauled. She leaned."; the master's swallow pair;
- **#8** parallelism: speech only ("I stood witness … I stood up and witnessed"; "Is that all of it? … Is that them married?"; Felix's "I told him you'd come, I told him you'd come running");
- **#10** described emotion: "with no great liking for the flour on him";
- **#11** explanatory extension: 1 firm ("Gold that soft…", 0.40/1k);
- **#13** precision: the counts and the time;
- **#15** authoritative description: the rigging at l.15;
- **#16** philosophical aside: "Gold that soft took a scratch from anything".

**Clear:**
- **#3** rule of three: **R6's list was borderline on the cycle-1 page, and F1 clears it**;
- **#20** emotional temperature report: the three run-body beats are clustered in the first 55 lines (l.9, l.37, l.55), not periodic;
- all others.

**7/20, −0.875: clean band (commercial 0–8).**

## The book's own laws (re-checked on the final copy)
- **Foreshadowing 0** (gate and reading).
- **END-1 ✓:** the watch is never explained.
- **CP3-3 ✓:** "a child's teeth" is Marcus's marks on the bracelet, not a pregnancy thought.
- **CP3-5 ✓:** "Isthm-" 0.
- **No Ch.15 door, camera or "wait outside" line.**
- **No comparison in Valens's speech.**
- **Non-negotiables all on the page:**
  - ten words before two witnesses;
  - Felix cries;
  - the sailor wants on;
  - the watch is given back wound, with no speech;
  - the mule refuses the plank;
  - the close is a ≤7-word single-sentence paragraph.
- **The memory is triggered by the scene** (the cucumber) and returns to it.

## Reader reports (cycle 1)
- **Devourer:** no stop anywhere. The descriptive run at l.11–15 is the only skim, and Felix on the plank carries it.
- **Critic:**
  - **No longer finds:** the present-tense similes, "said, too late", the road look, or the master's Latin by its endings.
  - **Would underline:** the same set as cycle 0, plus "a harbor Latin stuffed with sailors' Greek".
  - **Would mind, until F1–F3:** "a few pine needles" at the proposal, "Valens was minding … / Valens was chasing …", and Felix hauling three times.
- **Hostile:**
  - "Why does the sailor get kicked?" Because he turned to answer Valens. It is now on the page.
  - "How does Mara know the girl is the master's daughter?" From "My girl's aboard." INVESTIGATE.
  - "Did he set the watch?" Inferable from the shadow, and never stated. Honest.
- **Casual:** 9.0 (above).
- **Devoted** (active):
  - **No longer catches:** Plautia's smoke excuse, the Ch.13 look-away, Ch.15's heat lines, or the Ch.17 wind in faces.
  - **Might still catch:** the breeze on her body two pages after Ch.17's breeze on her neck (R2, INVESTIGATE), and the needles the disruptor once cut (F1).

| Issue | Dev | Crit | Host | Cas | Devoted | Severity |
|---|---|---|---|---|---|---|
| R6 needles / list (F1) | | ✓ | | | ✓ | SHOULD FIX → finalize |
| C2 "Valens was [V]ing the [mule]" double (F2) | | ✓ | | | | INVESTIGATE → finalize |
| "haul" ×8, Felix ×3 in 25 lines (F3) | | ✓ | | | | INVESTIGATE → finalize |
| R2 breeze on her body after Ch.17 l.536 | | | | | ✓ | INVESTIGATE (not changed) |
| D2 the daughter labelled before "Father," | | | ✓ | | | INVESTIGATE (not changed) |

**No CRITICAL, no IMPORTANT, no VIBES PROBLEM.**

## The Tomorrow Test
**What the reader remembers:**
- a boy crying open-mouthed under a pine crown with no needles left, because "There should have been nuts";
- the watch put back in her hand warm, with flour in the links, wound to the stop, right by the sun, and nothing said.

**Anchor type:** BOTH.
- IMAGE: the crown, the watch, the blindfolded mule, the fig jar.
- QUOTE: "Yes. Will you?"; "Yours had a cake,".

**Verdict:** ANCHOR EXISTS (strong).

**Shareable:** "They get married on the dock in ten words because the captain won't sail otherwise, and the mule boy cries because nobody threw nuts."

## Pacing check (one line for `feedback/progress.md`)
**Ch.18 (cycle 1 + F1–F3):**
- Single-scene, under an hour on a sunlit quay, the same early afternoon as Ch.17's run.
- **2,523 words** (target 2,800, −9.9%, inside 2,500–3,100; not padded); dialogue 34.3% (30–40 ✓); median 15 (mid ✓); 0 breaks.
- `I-statement` → `punch`, between Ch.17's `short-punch` → `quiet` and Ch.19's planned `scene-set` → `long-fade`.
- The hinge is short after two 7k chapters, with the next at 8.4k. The value shift runs − / + / − / +, and the close hands straight to "By the time the goose ship…".
- Book total about 99,207 words.

**Verdict: OK.**

## VERDICT
**PASS.** Gate met: Floor 8.5 ≥ 8.5, Casual 9.0 ≥ 8.5, pacing OK, gates clean.

| Measure | Result |
|---|---|
| Scores | Originality 9.0 · Theme 9.0 · Characters **9.0** · Prose & Voice **8.5** · Pacing 9.0 · Emotion 9.0 · Immersion 9.0 |
| Genesis Floor / Average | **8.5 / 8.93** |
| Casual | **9.0** |
| Pacing | **OK** |
| CVI-Launch / CVI-Legacy | 10.0 / 7.1 |
| Mechanical suite (current page and F1–F3 copy) | all clean; echoes / command echoes / spoken-line echoes: none / none / none |
| Swaps verified | 17 clean; R6 → F1; C2 → F2; one pre-existing cluster (haul) → F3; R2 and D2 INVESTIGATE |
| Finalize | **apply F1–F3 with the script, exactly as tested** (2,523 words). No re-evaluation is needed: F1 restores cycle-0 text, and F2/F3 are single-verb swaps that cleared every gate and every reuse check. |

## Character-bible Ch.18 re-sync (finalize; the bible still quotes the Writer's first draft)
**The rule for every block:** re-tag it "SYNCED to the FINAL page 2026-10-21 (md5 `dbd5ac50…`): dialogue-polish, disruptor, continuity repair W-01…W-13, polish cycle 1 (C1–C4, R1–R13, D1–D4), finalize F1–F3". Every quote must then be verbatim on that page.

**VALENS, Ch.18 block (l.1011):**
- "I'll pay the fare again," … "Twice over." → **"I'll pay the fare again,"** ("Twice over." was cut by the disruptor).
- "Keep off her heels," (too late) → **"Keep off her heels," Valens called, and the sailor turned to answer him.** (R11).
- the time "shorter than my sandal" → **"The hands were at twenty to one, and beside my foot the mooring post laid a short shadow on the stone, tipped a little east."** (repair, D1).
- "He was watching the dun." → **"Valens was minding the dun."** (C2).
- The clasp: the page reads "…with the edge of his nail and pressed. His fingers smelled of bread, and once the catch was home he released my wrist." (R8; the snap is cut).
- **Add:**
  - the proposal staging, **"Valens faced me with flour dried white in the hair of his forearms and the crown hanging from his hand."** (R6 + F1; no look, no comparison);
  - **"Valens had gone after the black."** (F2) before "Cover her eyes, Felix. Her eyes.";
  - "Valens brought the black back with a sprat scale stuck to her nose".
- **Spent, add:** minding an animal during a hand-off (CLOSED at 2 with Ch.13); the warning, then the turn.

**FELIX, Ch.18 block (l.1633):**
- The first line → **"He won't take us! He's had them pulling at this since the shadow was over by that post, and I told him you'd come, I told him you'd come running and you'd tell him yourself, and he says it's not the fare and it's not the mules. Where've you been? Why are your arms white?"** ("Did you get it?" was cut.)
- "Nobody ever told me she was. Who married her? …" → **"I said she wasn't married." … "That's all I said. They asked was she, and she isn't, or if she is, it's news to me. Who married her? When was it? Wouldn't I have been there?"**
- "Nobody's going over but him." → **"I asked them all," … "All morning, each of them along the mole, while you were up there. Not one of them's going over but him."**
- The torches and nuts line → **"Here?" … "On the stones? With no torches? Who throws the nuts? You can't be married without nuts; they threw them at a bride at Kirrha till she hid behind her mother."**
- "as a far younger boy cries" → **"like a boy half his age"** (R4).
- "It's the sun," … "I've been sat in it since sunup. Don't look at me. Nobody look." → **"It's the nuts," … "There should have been nuts. Don't look at me."** (C1; "Nobody look." was cut).
- The unanswered crown questions: "Nobody passed us with the news," → **"We were the only two people leaving,"** (Mara's line).
- **Add:** **"Best plank in Lechaion, that."** (untagged, C3).
- "Up, you." → **"On, you,"** … "Who ever died of a plank?"
- "Strips his tunic" → **"Felix peeled off his tunic."** (F3).
- **Spent:** "It's the sun" → "It's the nuts" / "There should have been nuts."; add "Best plank in Lechaion, that."

**MARA: there is no Ch.18 block at all. Add one from the final page:**
- **Lines:** "Yes. Will you?"; "I am a free woman," … "I am registered at Delphi, as a kinswoman of the house of—" (cut off); "We are all of us watching the yard,"; "We were the only two people leaving,"; "Ask her,".
- **Body:** the taste of blood; "my ears were full of my own blood"; "I found breath enough for Latin, barely." The voice break on "Yes" was cut (W-07). Her hands act and never rebel: wipe, wind, catch, carry. The seat is resting.
- **Memory:** the cucumber end at her mother's sink, ending "and rinsed it off under the tap, and then she had eaten the end herself, standing, with salt."
- **The watch:** "I wiped it clean with my thumb"; "the only thing moving on that quay that nobody was shouting at"; "I put my nail to the crown to give it its turns, and it took two and stood hard."; the wrist choice; "The watch sat on the wrong wrist and ticked."
- **Acts:** "I put the crown back on him."; "The fig was all that was left on the quay, in its jar by the ring, and me."
- **Chaos:** 3/4, inhabited.
- **Counts:** credential asides 0; teeth 0; laughs 0; English 0; AD 79 0.

**PACUVIUS card (l.3436):**
- **Vocabulary band:** "with the ends of the words knocked off" → **"quick and hard, a harbor Latin stuffed with sailors' Greek, and he stayed at the rail to use it on us"** (R10). **Keep "Mara's one description of it; never again."**
- **Lines.** Replace the stale ones:
  - "Your boy's been sitting on my plank since the third hour, telling my men about a mountain." → **"Your boy's been on that plank since the third hour, telling the crew about a mountain."**
  - "Then Delphi can have you back." (cut) → **"They don't keep Delphi's rolls at Puteoli." He spoke to Valens.**
  - "Nobody's carrying anybody's wife onto my ship, nor anybody's woman either." → **"I'll put no man's wife aboard, nor any man's woman either."**
  - "Marry her … My man at the plank can stand for it, and your boy. … the way it was done before there were priests to ask, …" → **"Marry her, then, if you mean to, and be quick. That one at the plank can stand for it, and the boy. It wants no priest and no cake, only the two of you saying so with two others to hear it, and I don't care to be told how they manage it in Corinth. You have till the yard's at the top."**
  - "Nobody's throwing anything at my ship." → **"Throw a nut at this ship and you'll swim after her."**
  - "That's the yard!" … "Muleteer! That's my yard at the top! On my ship or off my plank, …" → **"The yard's up!" the master shouted. "Muleteer! Aboard or off the plank, the lot of you, and I'm not particular which!"**
- **Beats, add:** "squinted past the mole"; "scowled up at the yard"; "To Valens he said".
- **Note:** dialogue-polish cut "my [ship / deck / plank / yard / men / man]" from 12 to 3.
- **Spent, add:** "They don't keep Delphi's rolls at Puteoli."; "I'll put no man's wife aboard…"; "Throw a nut at this ship…".

**The Ch.18 walk-on note (l.2819):**
- **The sailor:**
  - "a gray man with tar to the elbows" → **"a gray man stained with tar"** (R7), and later **"the tar-handed sailor"**;
  - "by Castor" → **"by Pollux"**;
  - **add** "Haul now, and laugh at Puteoli," (to the mast hand who laughs) and "Hold her head, boy, and I'll warm her up behind,";
  - he **turns to answer Valens** before the kick;
  - "I stood witness for you," **the sailor said** (C4).
- **The deck:**
  - "four men round the mast" → **"The men round the mast"** (no count on the page);
  - "six rowers in a tow boat" → **"a rowing boat"** … "the rowers", with "Give him another!" one of them shouted.
- **The quay:**
  - the barrel-hoop hammerer ("two blows and a rest") → **"a man sat in a beached boat mending a net and whistling, as if the afternoon were his to spend"** (R1);
  - the fish-seller: "Whose is the black?" → **"That black's yours, is she?"**;
  - "hits a dog" → **"the fish-seller threw one after her"** (the dog is cut).
- **The daughter:** add **"The master's daughter had taken the cucumber out of her mouth."** (D2) and "she called along the deck".
- **Mention only:** the mother's cucumber memory now ends **"and rinsed it off under the tap"** (R12).

**The roles table (l.3491):** "the gray plank sailor with tar to the elbows" → **"the gray plank sailor, stained with tar"**.

**At-risk after Ch.18 (l.4752): rewrite it to the final page.** First, the quotes that change:
- **The ten words:** '"Yes." / "Will you?" / "Yes,"' → **"Yes. Will you?" / "Yes," said Valens**.
- **The watch:**
  - "stood hard against my nail; the spring was wound tight to its end." → **"it took two and stood hard"**;
  - "…the only thing on that quay that moved without being shouted at." → **"…the only thing moving on that quay that nobody was shouting at."**;
  - "shorter than my sandal, tipped a little east" → **"a short shadow on the stone, tipped a little east"**;
  - **the Ch.11 fast-reading recall ("ten past nine … over the trough") is CUT and must never be restored.**
- **The similes:**
  - "cords hold up a blind" → **"like a blind on its cords"**;
  - "like a diving board after somebody has gone off it" → **"like a diving board after a jump"**;
  - add **"like a boy half his age"**.
- **"as if" 1:** the barrel hoop → **the net-mender**.
- **Mara's body:** the voice breaking on "Yes" ("it broke in the middle with the run still in it") → **cut (W-07)**; add "I found breath enough for Latin, barely."
- **Spoken spent:**
  - "We're all of us watching the yard," → **"We are all of us watching the yard,"**;
  - "Nobody passed us with the news," → **"We were the only two people leaving,"**;
  - add "It's the nuts," / "There should have been nuts."; "Best plank in Lechaion, that."; "Throw a nut at this ship and you'll swim after her."; "They don't keep Delphi's rolls at Puteoli."; "I'll put no man's wife aboard, nor any man's woman either."; "Keep off her heels," with the sailor's turn.

**Counts (final page):**
- 2,523 words (shape_check), 2,531 (style), 2,527 (show_tell), 3,080 (`wc -w`);
- dialogue 34.3% (shape 34); median 15; 0 breaks; `I-statement` → `punch`;
- em-dash 1 (Mara cut off); ellipsis 1 (the master); semicolons 5; "as if" 1; similes 5 by metaphor_check (2.0/1k);
- and-chains 2/9; credential 0; pivots 0; "So" 0;
- bare "No." 0; said/told-the-[non-listener] 1 ("told the harbor"); non-"said" tags: "called" ×2 (volume) and "shouted" ×4 (volume);
- #11 1 firm; paragraph-final negations 1; "without" 3; indefinites in narration 2;
- gate gesture classes clean; echoes / command echoes / spoken-line echoes: none / none / none; foreshadowing 0; "Isthmia" 0;
- anti-AI 7/20 (−0.875).

**New SPENT / CLOSED / WATCH entries.** Patterns are written as patterns, not page text. **From cycle 0, now confirmed on the page:**
- tears excused by an irritant: CLOSED at 1 (Ch.16);
- "said, too late": CLOSED at 1 (Ch.15);
- Valens's look-away (or minding) at an object hand-off: CLOSED at 2 (Ch.13, Ch.18);
- a road as the vehicle for Valens's attention to Mara: SPENT (Ch.15);
- a clasp or catch on her wrist rendered by its sound: SPENT (Ch.16);
- narrating-present similes: 0; "in a hurry" in narration: 0;
- sample-06's counted hammer (`(two|three|four) blows and a (pause|rest)`): RESERVED for Ch.24 in any count;
- the opening paragraph never reuses the previous chapter's last two paragraphs;
- the watch: no "…and ticked." one-liner again, and Ch.44's watch on her wrist never recalls "the wrong wrist";
- said/told-the-[non-listener]: 5th book-wide, so Ch.19 gets none;
- vehicles spent: blind, diving board.

**New from this re-evaluation:**
- **A crown or garland's shed needles or leaves, described on anyone:** SPENT (Ch.17's "half bald"; the disruptor cut and F1). Felix's "a crown that's got no leaves on it" is the last word on it.
- **A cut detail is grepped before any later swap restores it, on any noun:** the disruptor's cut list becomes part of the evaluator's reuse check.
- **"[Name] was [V]ing the [animal]." as a short narration line:** ≤1 per chapter.
- **"haul" in a non-rope sense** (breath, clothing): ≤1 per chapter (Ch.18 keeps "long hauls through the nose").
- **"like a [person] half [poss] age":** once.
- **Nuts thrown at a bride:** SPENT as a topic (Felix twice, the master once).
- **A narrator "as if [the time] were his to spend" indifference at an opening:** once.
- **Weather acting on Mara's body in an opening paragraph:** Ch.19 gets none, after Ch.17's breeze on her neck and Ch.18's on her dress.
- **The master's daughter:** unnamed; labelled once.

**ENTITY_STATE / handoff (unchanged from cycle 0):**
- the watch is on Mara's RIGHT wrist;
- Felix's tunic is on the dun, and the crown is on Felix;
- the leaf is under Valens's tunic, and the pen-knife is in Mara's belt;
- the goose ship is under tow on the afternoon breeze;
- Pacuvius and the daughter are aboard.

**BIAS CHECK:** This evaluation was produced by the same system that wrote the prose. Confidence in scores above 8.0 requires external validation (beta readers, editors, comp analysis).
- **Prose 8.5 is the per-cycle maximum, and I give it on the page with F1–F3.** Without them the page carries one cut detail restored and two in-chapter doubles. A strict reader could hold Prose at 8.5 only after finalize; that is why F1–F3 are mandatory, not optional.
- **F1 removes a detail many readers would like** (the needles in the flour). I count it because the disruptor cut the same detail from the crown, and the bible allows the crown no re-description.
- **Casual is held at 9.0** although the C1 line is better. A single line does not change a chapter's vibe.
