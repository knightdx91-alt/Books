# Evaluation: Chapter 20 — The Mender's Shop (run 2) · the last chapter before CHECKPOINT 4
**Evaluator:** book-evaluator (independent; did not write or revise this prose) | **Date:** 2026-10-21
**Text evaluated:** `manuscript/chapters/chapter-20.md` (md5 `59c35189…`, sha256 `4dc4d10e…`). This is the page after writer → dialogue-polish → hook-craft → disruptor → continuity repair (C-01…C-03 option A, W-01…W-14). It runs **8,052 words** by shape_check (8,077 style, 8,081 show_tell, 8,825 `wc -w`). Dialogue is **34.2%** (show_tell; shape 34).

**Read against:**
- the book's CLAUDE.md;
- STATE.yaml `guardrails` and `resolved_author_decisions`, especially **AUTHOR-CP3-3** (the pregnancy gap stays unremarked) and **AUTHOR-END-1**;
- `feedback/progress.md`: the Ch.20 brief and the **"seam" ruling**;
- voice-dna §0–§8, with **sample-11** as this chapter's calibration, plus samples 02, 07, 08, 09, 10 and 13, which the scans hit;
- character-bible.md:
  - every at-risk and spent block, from "after Ch.1" to "after Ch.20";
  - the GRATA, ZOSIMUS and FELIX cards;
  - the Ch.20 walk-on block;
  - the Retired / at-risk table;
- outline `## Chapter 20` and Ledger row 20, plus outline Ch.31 for the reserved anchor;
- `evaluations/chapter-19-eval.md`;
- `evaluations/continuity/chapter-20-audit.md`, for what was applied;
- chapters 18–19 for pacing, and Ch.2, 3, 7, 9, 11, 13, 14, 15, 17 wherever a scan hit them.

**Genre profile and settings:**
- **Genre:** commercial historical romance / time-slip; comp *Outlander*.
- **Anti-AI band:** commercial (0–8 clean).
- **Explanation-density cap:** >6 or >0.8/1k caps Prose.
- **Engagement (book):** empathy 55 / fascination 30 / self-insertion 15. This chapter is the book's most **empathy**-driven since Ch.15.
- **Dimension 7:** IMMERSION.

**Measured** (`bash books/the-hour-of-ash/tools/check_chapter.sh 20`, run from /home/user/Books): **clean on every gate.**
- style: simile 1.5/1k, em-dash 0, foreshadow 0;
- grammar 0; rhythm 0;
- show/tell: no flags, dialogue 34.2%;
- voice-wear strict: clean;
- tic gate: clean (and-chains 2/9, credential asides 1, pivots 0, "So" 0; every gesture class under cap);
- echo 0; metaphor 2.0 fig/1k, median 15;
- `shape_check --strict`: `20 8052 6 34 16 narrative dialogue`, CLEAN.
- `tic_report.py --echoes 20`: **none / none / none**.

**My own scans** (scratch only, not gates):
- 3–7-grams of Ch.20 against Ch.1–19 and all 13 voice-bank samples, **stop-word-bounded strings included**;
- every spoken sentence of ≤6 words against every earlier chapter's speech, so the 1–2-word whole lines the echo gate's floor misses are covered;
- in-chapter repeated 3–5-grams;
- narration-only scans: paragraph-final negations, present-tense verbs, similes and "the way", "so that", "before [X] had", "a while" and the pause family, payment beats, time markers;
- by hand: every SPENT, CLOSED, RESERVED and WATCH item in the bible, grepped by frame as well as by string; every Valens line checked for a comparison; every order checked for an echo, relayed orders included.

**The fix set was tested together on a scratch copy.**
- The copy was swapped into the manuscript path, and the real `check_chapter.sh 20`, `tic_report.py --gate`, `--echoes 20` and `shape_check --strict` were run from /home/user/Books.
- The original was restored after each run and its checksum verified (md5 `59c351890d0ca1ad18aa413c56a6ae44`, sha256 `4dc4d10eb1f6a47449c2b7714c60543a73e3746f08f0a63a3e42cad5d4b98dc8`). **I did not edit the manuscript.**

*(l.N = line number in the current `chapter-20.md`; the header comments are l.5–9.)*

---

## HEADLINE
**CVI-Launch (CVI-L):** 9.4 (8.9 + 0.5 strong anchor) | **CVI-Legacy:** 7.1 (provisional) | **Genesis Floor:** **8.0** | **Genesis Average:** **8.71** | **Casual Reader:** **9.0**

**Engagement type:**
- **Empathy** leads: the pebble, the bowl, the fig wrapped in the dark, and "It's a child you've got."
- **Fascination** is second: real Pompeian walls, read aloud by people who will never know what the reader knows.
- **Self-insertion** is third: a shop of one's own on the Via dell'Abbondanza, and a landlady who narrates you to your face.

**Divergence alert:** none. The CVI-L gap above the Floor is 1.4, the right direction for a warm commercial chapter held back by book law.

**Gate (Floor ≥ 8.5 AND Casual ≥ 8.5 AND pacing OK): NOT MET at cycle 0.**
- Casual 9.0 ✓; pacing OK ✓; mechanical gates clean ✓.
- **Prose & Voice holds the floor at 8.0, on merit, with no cap.**
  - The sentences are 8.5 and better: "Then he kept two of his fingers on it, after it was in my palm, until he was sure it would stay." / "It was gray, and not black at all." / "My lower lip found that before my eye did."
  - What holds them is a **reuse-and-law cluster that no gate sees**, as in Ch.19's cycle 0.
- **The cluster:**
  - **The SPENT moving-thing hold, in the very words Ch.19's R1 cut:** "tooth by tooth, while the carts went by behind me." (l.295). Ch.19 cut "while a cart went by behind me".
  - **Ch.14's fountain set piece rebuilt at this chapter's anchor** (l.493). Ch.14 l.10 has her frozen at a public spout, water running "down my wrists into my sleeves and on down my ribs", and a woman behind her losing patience. Ch.20 has her frozen at a public spout, water running "down my side and my leg and into my sandal", and "The next woman in line reached round me and pushed her jar in". It is also a **logic slip**: she was "waiting my turn" (l.467), so the jar was empty.
  - **The reserved Ch.42 sample (sample-07) at two body beats:**
    - "I put out my hand." (l.489) against "I put my hand out." (the sample);
    - "my hand went over my mouth." (l.583) against "My hand went in." (the sample).
  - **sample-11's pickup at the bottle** (l.345): "She came for it … holding it to the daylight, looking for the break" against "When she came for it she held it up to the doorway and traced the line".
    - This is also the walk-on object-to-the-eye beat, which the bible says **Ch.20 has none of**.
    - "came for it" appears ×3 in the chapter (l.289, l.345, l.561).
  - **Two more voice-bank strings:**
    - sample-10's "It will hold," (the heat scene's line) as Mara's "It will hold anything you put in it." (l.143);
    - sample-08's "up there in this" as Mara's "Up there in this." (l.365).
  - **Ch.9's document image:**
    - "which was scratched over as high as an arm could stretch" and "its letters gone soft at their edges" (l.437, l.453);
    - against Ch.9 l.8: "the wall was written over from the paving to as high as a man could reach off a ladder … The old ones had weathered soft".
  - **A recast moved sideways.** The audit's W-02 fix put Ch.3's knucklebone image (the bone "gone glossy, the polish fingers left on a thing after a very long time") onto the lamp: "dark and glossy from his thumb, pressed there each dawn for years" (l.545).
  - **Two-chapters-back frames:**
    - Ch.18's "flour dried white in the hair of his forearms" → "shavings of bone in the hair of his arms" (l.283);
    - Ch.19's bed ("let him down an inch") → "the bed walked an inch on its legs" (l.277);
    - Ch.19's finder layout ("on the left") and Ch.15's heat-scene "held still for" → the named frame's "the jar on the left and his gray soles on the right … so I held still for it" (l.213).
- **Characters sits at 8.5, held by:**
  - **Borrowed whole lines** that the gate's floor cannot see:
    - Valens's "Today," (his Ch.17 whole line, l.252) and "Not tomorrow." (his Ch.11 whole line, l.274), assembled into one fig line (l.575);
    - that line also carries **SPENT fig lore**: Ch.11's wasp line, "A fig that gives has gone to the wasps.";
    - Valens's "What's in it?" (l.189) is his Ch.15 "What's in it, then?";
    - the turner's "Twice," … "Once for … Once for …" (l.287) is "Twice" as a reply in its 5th chapter, and it rebuilds Kallia's Ch.7 skeleton ("Twice. Once on my good hearthstone and once in the lentils.").
  - **A narrator button device:** "paid me in [kind]" closes four mini-scenes (l.71, l.171, l.329, l.361), with "She paid me," and "He paid me," twice more (l.347, l.569).
  - **Smaller doubles:**
    - Valens's doubled pause at the stone ("He waited, in case more came" + "He looked at it a while", l.513);
    - Zosimus's "black finger" ×2 (l.527, l.539);
    - the turner's fingertip round the slot (l.289, the audit's W-10 recast), which rehearses the anchor's touch-test one section early.

**The fix set: 41 swaps, tested together** (script below). All are cuts or near-even swaps, and none adds a sentence.
- **7,785 words** (shape_check), against the 7,700 floor;
- dialogue **35.2%**, against the 30% floor; median 16 (mid ✓); 6 breaks; `narrative` → `dialogue`;
- every gate clean; echoes / command echoes / spoken-line echoes none / none / none.
- **Byte-identical after the fixes:**
  - the opening notice;
  - "My lower lip found that before my eye did.";
  - the bowl onto the cart and the carter's line;
  - "I was crying.";
  - the two fingers;
  - "It was gray, and not black at all.";
  - "That's a good stone,";
  - Zosimus's request;
  - the soot in the join;
  - both thumbs on the welt;
  - the tremor note;
  - Polybius and the I on the crack;
  - Grata's closing speech.

---

## Genesis Score (Craft Assessment)

| Dimension | Score | Evidence | Cap reasons / holds |
|---|---|---|---|
| Originality | 9.0 | **The outline's subversion is on the page:** the domestic-happiness montage is told through other people's walls, and its peak is a pebble, not a kiss. **What the writer built on top of it:** (1) a year in real Pompeian wall-writing (CIL IV 64, 429, 222/7621, 8258–9, 1904, 9131, 1679), each wall *read aloud to someone who cannot read it*. (2) Zosimus wants his break left "where the boys can see it's spoken for. It's dark on that stair, and I'll want to find it with my thumb" (l.539). That inverts sample-11's sentiment into use: one lamp among forty identical FORTIS lamps. (3) The bowl Mara throws out for a hair's misalignment becomes a carter's present to his wife: "Have you got any more you don't want?" (l.157). (4) "He had set the upright of the I in Iulius straight down it" (l.417), with Felix's "Polybius is standing on it … and he doesn't know." (l.423). (5) The pregnancy is diagnosed from a fish-sauce jar. | **≥9.0:** would a senior editor set this beside *Outlander*'s Lallybroch settling-in? Yes. It is funnier and stranger. **Not 9.5:** the year-in-vignettes montage is a known form; the execution, not the shape, is new. |
| Theme | 9.0 | "Home as the place you mend" is **never stated**. The disruptor cut the one pointer, and "seam" is 0 on the page. It is carried by acts: the stewpot made invisible against the woman's own joke ("I'd only break it in the same spot, looking for it.", l.69); the bowl thrown out; the bottle hidden so a husband never finds it; the lamp left findable. Mara never says what changed. **Texture that means nothing:** the frog in the pot; the coppersmith's alibi goat; the dowry in fig trees; the drip that follows Valens's foot; Hermes's lamp in the fire. | **Not 9.5:** nearly every object is broken, which is the premise. The extra fault-line rhymes (the bull's chipped horn "gone as dark and smooth as the rest of him", the hollow third step, the drum split in the quake) brush #18 (minor). |
| Characters | 8.5 | **Grata at full strength.** She tells and never asks (0 questions on the page). Each flood ends in a command ("Spell it right."; "Go on with the boy"). Her touches vary (upper arm, forearm push, two fingertips at the wrist). She invents the vow and charges the wind. The reveal is pure card: "you've not told him either, or he'd be standing in my door grinning at nothing the way husbands do … It's not my fish. It's a child you've got." (l.591). **Valens:** 0 comparisons, 0 bare "No.", 0 orders to Felix. The figs pinched to make wood. The tree wrapped twice in the dark ("She can't climb down to me.", l.371). "It's red" keeps his literacy from Felix. "That's a good stone," (l.515). **Felix:** 8+ speeches end on a boast or a fact ("That's a drop of two of me."; "It's gone rotten in the middle. A blind man could tell that."); "a name scratched on every wall in this town but mine" (primes Ch.21's palm without spending it). **Zosimus** matches his card: use, never feeling, and the Hermes feud. **Mara** is 4/4, inhabited (below). Cover-the-name PASS for all speakers. | **No cap:** no character leads with a tic; the gate's gesture classes are clean, and I use its numbers. **Held at 8.5 by C1–C7:** Valens's borrowed "Today," / "Not tomorrow." and the SPENT wasp lore; "What's in it?"; the turner's "Twice … Once … Once"; the payment-in-kind buttons ×4 (+2); the doubled pause; "black finger" ×2; the fingertip rehearsal of the anchor. **WATCH, not changed:** Felix has Mara read him five walls (it is the collage's delivery mechanism, worded fresh each time); walk-ons tend to exit performing their trait (leek woman, girl, carter, Zosimus ×2, painters). |
| **Prose & Voice** | **8.0** | **Stopping sentences:** "Then he kept two of his fingers on it, after it was in my palm, until he was sure it would stay." (l.489); "The stone in my other hand had dried by then. It was gray, and not black at all." (l.505). **Underlines:** "My lower lip found that before my eye did." (l.151); "At every blow the drum rang and gave up another chip of itself." (l.185); "Under it was the one part of his face the dust had not reached." (l.187); "The shadow of a leaf lay over his open lips and stirred when the leaf stirred." (l.209); "I took it, and wound on, and he slept through both." (l.213); "the bottle's own blue did half my work" (l.345); "He opened his eyes, offended for the lamp." (l.567); "The drip went on landing where his foot had been." (l.375). **Ugly sentence:** "Felix, at the opening, watching the rain go past:" (l.373); "'The fig,' I said, one afternoon of that." (l.365). **Voice under pressure:** at the fountain the asides die and the sentences shrink to body ("My mouth was open. I could not shut it."); at the fish jar the body overrides the mind ("The jar had turned, I decided."). | **Merit 8.5, no cap.** #11 is 5 firm (0.62/1k), under the commercial cap. **Held at 8.0 by the law cluster** (R1–R19, L3): the SPENT moving-thing hold; Ch.14's fountain skeleton; sample-07 ×2, sample-11 (+ the CLOSED object-to-eye beat), sample-10, sample-08 and sample-02; Ch.9's wall image; Ch.3's gloss moved sideways; Ch.18 and Ch.19 frames; the camera layout; the lamp re-narrating the bowl's process ("brought the faces" ×2); tool-tip frames ×4; reach-height rulers ×2. Anti-AI 8/20, −1.125 (clean band, at its edge). |
| Pacing | 8.5 | **The ledger row is hit on every hard field:** Collage, between Ch.19's Chronological and Ch.21's ✓; open `narrative` (the italic notice, 22 words; hook VOICE, not CONTRAST) ✓; close `dialogue` on Grata's line (pull REVELATION, not QUESTION PLANT) ✓; 6 breaks ✓; dialogue 34.2% (30–40) ✓; 8,052 against 8,200 ✓; median 16 (mid) ✓. **Speed design as the outline asks** ("documents quick; repairs slow and tactile; the fountain sudden"): each document lands in a line; the bowl night runs slow; the fountain arrives with no lead-in, in the middle of wedding gossip. **Value shift:** a living needed (−) → a trade (+) → the bowl thrown (private −) → the fountain (±) → the lamp (+) → a child (+, with the reader's dread). | **Not 9.0:** there is no forward question between the bowl (about 15%) and the fish jar (about 95%). The pull is incident and warmth. S5 (the night crew and the pier's graffiti, about 1,300 words, Felix asking at each wall) is the stretch a Devourer skims. |
| Emotion | 9.0 | **The anchor lands** ("a lamp she mends for a customer, with the seam showing on purpose"): Zosimus with his eyes shut, his thumb travelling the shoulder, "That's it," (l.561–563); and before it Valens's thumb along the same welt, "slowly, and back." (l.549). It is also the motif's turn against Ch.2, where Mara tests her own invisible join with her thumbnail, eyes shut. **The surprise lands** exactly as planned, unearned and unexplained, and the bible's "never explained, by anyone, ever" holds: "I was crying." **Body rebel ×2:** the tears (the mapped Ch.20 break; voice stays retired) and the nausea, which she misreads. **Techniques ≥5:** object proxy (the stone drying gray; the bowl riding away on a stranger's belly); comedy at the edge of feeling (the dyer's "I never touched her … He gave one to a mule this morning."); restraint ("That's a good stone,"); dramatic irony (the amazed-wall graffito; "It'll come with the heat."); revelation by a third party. | **≥9.0. Not 9.5:** the designated anchor (the lamp) is quieter than the undesignated one (the fountain), and the romance's heart-load is light again (the hip in the dark, the stone, the figs). That is right for a montage, but lighter than Ch.15–18. |
| **Immersion** (Dim 7) | 9.0 | **Period, nearly all verifiable** (audit I-01 confirms):<br>• the texts: CIL IV 64's lost bronze pot; Polybius "He brings good bread."; the whitewasher and the lantern-boy (*lanternari, tene scalam*); Successus and Iris; *admiror, paries*; the fullers' *Aeneid*; Edone's 1/2/4-as price board;<br>• the trades: lead "dogs" in pottery; a riveted bronze handle; lentisk sold for the breath; terra sigillata *in planta pedis*; a beehive money box; a bone *dentiscalpium* with an ear-spoon; a FORTIS Firmalampe; olive-stone fuel;<br>• the town: sledges on a quake-split column drum; the forum temple in a cage of poles.<br>**The authenticity dial:** sensory ~8+ (the fish jar, "salt and rot and something under both"; must and wasps), harshness ~7. | **Held at 9.0:**<br>• garum ladled into a carter's cup (l.583, l.587; → L2);<br>• the fountain's authoritative opening paragraph (l.465; #15 minor);<br>• "Falernian … from that side of the bay" (Grata's seller's stretch, kept);<br>• "a carter bound there for lime" (Puteoli's export was pozzolana; kept, audit I-04). |
| **FLOOR** | **8.0** | Prose & Voice (merit) | |
| **AVERAGE** | **8.71** | (9.0 + 9.0 + 8.5 + 8.0 + 8.5 + 9.0 + 9.0) / 7 = 61.0 / 7 | |

**Trajectory against Ch.1–19** (finals 8.50–8.93; every cycle 0 at 7.5–8.0):
- This is the twentieth cycle 0 below the gate. It is held, as Ch.19 was, by reuse the gates cannot see.
- **Two new failure modes:**
  1. **A recast moves a repeat sideways into a third chapter.** The audit's own fixes did it twice: W-02 put Ch.3's polish image on the lamp, and W-10 put the anchor's touch-test on the turner.
  2. **A 1–2-word whole line** from a previous chapter passes under the gate's floor. Ch.19's "What for?" was the first; here there are three ("Today,", "Not tomorrow.", "Twice").

---

## CVI-Launch Breakdown
| Input | Score | Evidence |
|---|---|---|
| Commercial Pacing | 8/10 | Short vignettes, each closed. The fountain lands at about 60% and the reveal on the last line. It loses 2 because no forward question runs through the middle. |
| Tomorrow Test | 5+ anchors → 10 | IMAGE: a naked toddler keeps two fingers on the pebble "until he was sure it would stay", and the stone dries gray; the red bowl riding away on a tile carter's belly; a stoker with his eyes shut finding his lamp by its blackened join; Valens asleep under the fig with a leaf's shadow on his lips; the drip following Valens's foot across the bed. QUOTE: "It's not my fish. It's a child you've got."; "That's a good stone,"; *I'm amazed, wall, that you haven't come down in a heap…* |
| Casual Reader | 9/10 | See the report below. |
| Shareability (quote / plot / emotional) | 3 / 3 / 4 → 6 / 6 / 8 → **7.47** | **Quote:** the amazed-wall graffito (real, and the reader knows why it's funny) and Grata's last line. **Plot:** "her landlady works out she's pregnant from how she reacts to the fish sauce." **Emotional:** "a toddler hands her a wet pebble at a fountain and she just breaks." MAX 8 × .6 + AVG 6.67 × .4. |
| Concept Pitch | yes → 10 | |
| Human Closeness | yes → 10 | A marriage, a landlady, a boy, a street of neighbours, a child coming. Nearly every scene is intimate conversation. |
| **CVI-Launch** | **8.89 + 0.5 = 9.4** | 8 × .2 + 10 × .2 + 9 × .2 + 7.47 × .2 + 10 × .1 + 10 × .1 = 8.89. |

**CVI-L note.** In this project "CVI-L" means **CVI-Launch: 9.4** (8.9 before the anchor bonus).
- Running CVI-L, Ch.12–20: 9.7 / 9.8 / 8.9 / 9.8 / 9.7 / 9.7 / 10.0 / 8.85 / **9.4**.
- **It recovers from Ch.19's structural dip.**
  - Ch.19's engine was fascination with the place. Ch.20's is empathy with the life, and it ends on a reveal that a reader texts a friend about.
  - Human Closeness goes from partial to yes, and that alone is +0.5 against Ch.19.
- **What drives launch here:** the pebble, and Grata's last line.
- **None of the 41 fixes touches either anchor.** The fountain loses only the jar spill and the next woman (the Ch.14 skeleton) and "I put out my hand" (sample-07). The two fingers, "I was crying.", the stone drying gray and "That's a good stone," are byte-identical.
- **CVI-L is unchanged after the fixes: 9.4.**

**CVI-Legacy (default weights; provisional):** **7.1**. It is the sum of:
- Originality 9.0 × .30;
- Theme 9.0 × .25;
- Cultural Vocabulary 2 × .20;
- Re-readability 8 × .15;
- Identity 5 × .10.

On a re-read the reader finds:
- the first tremor note in Fenn's blank leaves (Ch.36's thread);
- the amazed wall and "the straightest pier on the street";
- Polybius standing on the crack;
- Ch.2's thumbnail, eyes shut, turned inside out by Zosimus's thumb;
- "It'll come with the heat."

None of them is pointed at.

---

## Anti-AI Scan (20 patterns; density per 1,000 words at 8.05k; commercial band)
| # | Pattern | Result | Count / density | Citation |
|---|---|---|---|---|
| 1 | Forced symmetry | FOUND minor | 1 | the finder's "the jar on the left and his gray soles on the right" (l.213; → R13). **−0.125** |
| 2 | Empty poetic vocabulary | Clear | 0 | |
| 3 | Automatic rule of three | FOUND minor | 3 adjective triads (0.37) | "pale and dry and sharp" (l.545); "small and black and round" / "small and dry and gray" (l.489, l.513; a designed pair); "salt and rot and something under both" (l.579; the third turns). Grata's 1/2/4 board is the real text. **−0.125** |
| 4 | Em dashes | Clear | 0 | |
| 5 | Empty metaphors | Clear | 0 | "like a face just shaved of its beard" (l.385) is concrete. |
| 6 | Dramatic "And" openings | Clear | narration 0 | Speech "And…" rejoinders 3 (Mara, Valens, Zosimus); WATCH ≤4. |
| 7 | Pseudo-philosophical closings | Clear | — | The chapter ends on Grata diagnosing a pregnancy. |
| 8 | Excessive parallelism | FOUND minor | 3 | "The jar was on my hip and the stone was in my hand." (pressure, designed); "his head and chest in its shade and the rest of him in the full glare"; "He moved the foot, and the drip moved after it" (comic). **−0.125** |
| 9 | Overly smooth transitions | Clear | — | The section joins vary: a document, an event, a season, the vintage, a document, a place, a document. |
| 10 | Described emotions | FOUND minor | 5 walk-on labels | "pleased" (coppersmith), "much pleased" and "delighted" (Felix), "satisfied" (turner; cut by C7), "offended for the lamp" (kept: the best of them). Mara's own: none. "I was crying." is a state, not a report. **−0.125** |
| 11 | **Explanatory extension** | **FOUND moderate** | **5 firm (0.62/1k)** | (1) the hen squeeze "to feel for the meat on it" (l.27; kept, comic); (2) "so the resin would not chill and go stringy on a cold edge" (l.119; kept, the conservator); (3) "for fear one of them should fall again" (l.283; kept); (4) "a stone like any other in any gutter in the town" (l.513; → C5); (5) "The word belonged to tinkers." (l.63; → R17). **Borderline, not counted:** the *Aeneid* gloss (l.335, needed by most readers); "the break so new that nothing had yet got into it" (l.545); "in case the jar was his pot" (l.23). **−0.25.** Commercial cap PASS. |
| 12 | Binary negation opener | Clear (judged) | narration 0 | Grata's "It's not my fish. It's a child you've got." answers Mara's literal accusation ("That jar has gone off"). It refutes; it does not define by negation. Kept: it is the chapter's protected close. |
| 13 | Precision flex | FOUND minor | — | Sixty-five sesterces (the real notice), "the other thirty-nine", "Third step up", "three summers", "a drop of two of me", forty / forty-two. All are character or period, and Zosimus's thirty-nine is wit. **−0.125** |
| 14 | Emotional control demonstration | Clear | — | Control **fails** twice (the fountain; the fish jar) and is never narrated back. |
| 15 | Authoritative description | FOUND minor | — | The fountain's opening paragraph (l.465); the bowl's provenance (l.105); lentisk's trade (l.119). Offset by "or seemed to" (the drip), "till it seemed he might sleep again", and "The jar had turned, I decided." **−0.125** |
| 16 | Philosophical asides | Clear | 0 | "It ended when it ended." is a plain report, not a maxim. |
| 17 | Clean dialogue | Clear | — | Grata talks past Mara to the oil man; the leek woman calls back over the leeks; the painter answers three questions in three words ("Polybius. Enough. No."); Grata hollers up from the counter. |
| 18 | Thematic echo chamber | FOUND minor | — | The premise breaks everything. The extra fault-line rhymes (the horn, the third step, the drum) are minor; texture abounds. **−0.125** |
| 19 | Graduated reveal | Clear | — | A collage of a year; no escalation shape. |
| 20 | Emotional temperature report | Clear | — | |

**8 / 20 found (#1, #3, #8, #10, #11, #13, #15, #18). Total −1.125. Band: clean (commercial 0–8), at its edge.**
- **#11 hard check:** commercial cap PASS (0.62/1k).
- **After the fixes:** #1 cleared (R13); #11 → 3 firm (0.39/1k), minor; **7/20, −0.875: clean band.**

---

## The book's own laws
- **NO TICS: verbal catchphrases 0; gate gesture classes clean. By hand, the following hold Characters at 8.5:**
  - **Spoken refrains:**
    - "Twice" as a whole reply is in its 5th chapter (Ch.6, 7, 13, 17, 20), and here it carries Kallia's Ch.7 "Once… once…" skeleton → **C2**;
    - "Today," and "Not tomorrow." are Valens's own earlier whole lines → **C1**;
    - "What's in it?" is his Ch.15 line → **C3**;
    - "nobody" in speech is 4 openers across 3 speakers (Felix 2): under every gate. WATCH.
  - **Narrator moves:**
    - "paid me in [kind]" as a paragraph-final button ×4, plus "She paid me," / "He paid me," → **C4**: 3 left, each worded fresh;
    - "with the tip / point of [tool]" ×4 → **R15**: 2 left;
    - reach-height rulers ×2 (l.385, l.437) → **R16, R9**;
    - "dusk" ×4 for arrivals → **D7**: 3 left;
    - "that same month" ×2 → **D6**.
  - **Gestures:**
    - Valens's pause doubled at the stone ("waited" + "a while") → **C5**;
    - Zosimus's "black finger" ×2 → **C6**;
    - the tradesman's arm-marker introduction: coppersmith (burns on the forearms), turner (bone in the hair of his arms), painter (red to the wrists), Zosimus (black to the elbows). The audit's W-11 left two; the turner's is the Ch.18 frame → **R12**.
- **No foreshadowing; the tremor note does no reckoning: PASS.**
  - "the date and *small shake, lamps, nobody woke*" (l.277): two sentences, no count, no comparison, never noticed afterwards.
  - Mountain 0. "seventy-nine" 0. Casts, excavators, ash and preservation 0.
  - The amazed-wall graffito and Felix's "It's been standing since before any of us was born" are the reader's irony. The narration says nothing about them (audit I-13).
  - "It'll come with the heat." and "Next year." are speech about the near future, not narrator reach.
- **The theme of the visible seam is never stated: PASS.** "seam" is 0. The bowl is thrown out with no reason given: Felix asks "Was there a fault in it?" and Valens answers "We'll manage with the cookpot,". The lamp's request is the customer's alone.
  - **Judged:** Mara's "He wants to find it in the dark." to Valens (l.557) restates the request once, in dialogue, as the answer to "Left like that." It is a reason given to a question, not a theme. Kept.
- **Mending is hands at work, never a catalogue: PASS, with one repeat.**
  - The bowl night (l.119–147) is sequential hands: warm, bead, seat, thread, shave. Its one rationale clause is counted in #11.
  - **The lamp re-narrated the bowl's process** ("brought the faces" ×2; the bead, the cane and the welt again) → **R14**.
- **Memory only when triggered by the scene: PASS.** Dr. Pinsky's pick (l.295) is triggered by the toothpick, takes a clause, and returns to the doorway. There is no stand-alone memory paragraph. **WATCH:** the filled molar is now on the page for the 4th time (Ch.2, 5, 7, 20); → **L1** aligns it to one filling.
- **Explanation density: PASS** (0.62/1k → 0.39/1k after the fixes).
- **Paragraph-final negations ≤1.5/1k: PASS.**
  - **8 in narration (0.99/1k):** l.187, 203, 243, 345, 499, 505, 545, 577.
  - **After the fixes:** 7 (0.90/1k).
- **Present-tense generalisation ≤1: PASS** (0 in narration).
- **No comparisons in Valens's speech: PASS.** Every Valens line was checked, among them:
  - "Glass," … "Who breaks glass, in this street?"; "Grata will want her name on it somewhere.";
  - "The black bit him. He found the load after that."; "In his pride. And in the meat of his arm, a little.";
  - "I'll stand her further off from him."; "Will it hold soup?"; "Beans will do,";
  - "These would never ripen." … "Without them she makes wood."; "Next year."; "It hasn't,";
  - "For Plautia," … "Where we are."; "She'll put it aboard one for a copper, and keep the copper if there's no ship.";
  - "Do you still walk out to your gate?"; "Then I'll keep to the other.";
  - "She doesn't mind the wet. It's the cold that creeps over at night she minds."; "She can't climb down to me.";
  - "It's red,"; "That's a good stone,"; "Who's this for?"; "Left like that."
  - None has "like" or "as". "Left like that" means "in that state".
- **No command echoes, relayed orders included: PASS** (gate none; by hand):
  - "Tell her it hasn't" became the statement "It hasn't," (audit C-01). Mara's "He says it has not," now relays a statement, not an order.
  - "hold that light still" is answered by result ("until he was told about it, and then it rose").
  - "Come and read it in the morning" is answered by "At daybreak I found this", an act in other words.
  - "Put that Grata says." becomes the board itself: dictation, not compliance, and in varied words.
  - "Do it the same." / "Make it tight." are answered by the mend. "Leave me the crack." is answered by "Then I let it stand." "Go on with the boy" is answered by "From there Felix took me".
- **No borrowed whole spoken lines: FAIL by hand, cleared by C1–C3.** `--echoes 20` reports none: its whole-line floor is above two words. My sentence-level scan finds:
  - "Today," (Valens, Ch.17 l.252: `"Today," said Valens.`);
  - "Not tomorrow." (Valens, Ch.11 l.274, a whole line);
  - "What's in it?" (Valens, Ch.15 l.138 "What's in it, then?");
  - "Twice" (5th chapter).
- **No reuse of earlier chapters' phrases or set pieces: FAIL, cleared by the fixes.**
  - **SPENT, "0 more anywhere":** the moving-thing hold, "while the carts went by behind me" (l.295) → **R1**. The bible's cut-detail rule says a string cut in one chapter is grepped before it comes back; this is Ch.19's R1 cut, near-verbatim.
  - **Ch.14's fountain skeleton** (l.493): frozen at a spout, water down the body, the woman behind → **R2** (+ **L3**: the jar was empty while she waited her turn).
  - **The voice bank:**
    - **sample-07, reserved for Ch.42:** "I put my hand out. My hand went in." against l.489 and l.583 → **R3, R4**;
    - **sample-11:** "When she came for it she held it up to the doorway" against l.345 (+ the CLOSED object-to-eye beat) → **R10**; "came for it" ×3 → **R10, R11, C7**;
    - **sample-10:** "It will hold," (l.143) → **R6**;
    - **sample-08:** "up there in this" (l.365) → **R7**;
    - **sample-02:** "the face of a" (its signature simile, quoted in voice-dna §1) as "you've the face of a payer" (l.27) → **R18**.
  - **Ch.9's document shapes:**
    - the wall written over to reach-height, its old letters gone soft (l.437, l.453) → **R9**;
    - **judged, kept:** "It was up on the pier of a cookshop above the bull's-head fountain." (l.13). Audit W-01 already removed the red paint, the support-making clause and the second reward tier. What remains is a bare placement sentence, followed by a charcoal reply and a passer-by reading aloud, and Ch.9 has neither.
  - **Recasts moved sideways:**
    - Ch.3's knucklebone gloss onto the lamp (l.545; audit W-02) → **R8**;
    - the anchor's touch-test onto the turner (l.289; audit W-10) → **C7**.
  - **Two chapters back:** Ch.18 "in the hair of his forearms" → **R12**; Ch.19's bed "inch" → **D4**; Ch.19's finder layout + Ch.15's heat-scene "held still for" → **R13**; Ch.19's counter, "a ladle hung on the lip of each" → **R19**.
  - **SPENT fig lore:** Ch.11's wasp line ("A fig that gives has gone to the wasps.") → **C1**. The bible lists the wasp line inside the spent fig argument.
- **Ch.31's reserved anchor ("Grata whitewashing a rival's election notice by lamplight with Mara holding the ladder"): not pre-spent after the audit's C-03 option A. Judged.**
  - **Nobody from the household holds anything:** Felix sits "among the painter's pots", and Mara stands in the road.
  - **What Ch.20 has:** a professional crew, a crack-stripe (not a rival's notice), and a boy with a lamp on a pole.
  - **What Ch.20 does spend:** the generic tableau of night whitewash by a lamp and a ladder, and the real graffito *Lantern-boy, hold the ladder.*
  - **Forward guard (orchestrator, for Ch.31):**
    - stage the raid by Grata's own lamp, on a rival's red letters, with Mara's hands on the ladder;
    - no professional crew on the page;
    - no "hold the ladder" in any mouth or on any wall;
    - no comparison of the wall to a shaved face.
- **The Ch.20 brief: all honored.**
  - Collage ✓; the italic notice opens (`narrative`) ✓; the close is Grata's line ✓.
  - The shop is the dead cobbler's, next to Grata's counter ✓ (CH19-2).
  - The election notice goes over the crack Ch.19 put on the cousin's red house ✓ (chosen and kept).
  - The bowl is thrown out ✓; the fountain and pebble are unearned ✓; the lamp's join is left visible at the customer's wish ✓; Grata clocks the pregnancy before Mara says it ✓.
  - The pregnancy falls late in AD 73 (the olive month, about November; audit I-02/I-03) ✓; **CP3-3: no line remarks on the months without a child** ✓.
  - Beat 3a is two sentences in Fenn's blank back leaves ✓. The named frame is on the page ✓.
  - The "seam" ruling is respected: "seam" 0, and the door is never described ✓.
  - The hook is VOICE ✓ and the pull is REVELATION ✓.
  - Felix's boast/fact endings number 8+ ✓; Valens's orders to Felix 0 ✓; Grata's teeth 0 ✓; citizenship 0 lines ✓.
  - Bends 0, kneel/crouch 0, hand-on-knee 0 and gait exits 0 ✓. Deliberation pauses are 2 at the stone → 1 (**C5**). Present-tense generalisation 0 ✓. Valens's bare "No." 0 ✓. No narrated non-answers from Valens ✓ (Mara's "I gave him no answer." to the carter is hers). Comparisons 0 ✓.

---

## Character Chaos Check (Primary: Mara)
- **Irrelevant thought: present, inhabited.** The toothpick tour of her mouth in the shop door, with the carts and the customers forgotten, and the absurd happiness shown and never named (l.293–295).
- **Cognitive distortion: present, inhabited.**
  - All-or-nothing: the bowl goes onto a rubble cart for a hair's step at the rim, with no reason given (l.151–153). Ch.19's rule is not restated.
  - Misreading the body: "The jar had turned, I decided." (l.579).
- **Unprompted memory: present, triggered.** Dr. Pinsky's pick, from the bone point, in one clause, returning to the doorway.
- **Failed emotional management: present, inhabited.** The fountain ("My mouth was open. I could not shut it."); the hand over her mouth at the fish jar.
- **Voice under pressure: demonstrated (level 1).** The asides die at the fountain and come back at Grata's counter.
- **Score:** 4/4 (commercial 2–3 is sufficient), all inhabited → no cap.

## Secondary Character Chaos
- **Valens:** his own moment — the figs pinched for wood; the tree wrapped twice in the dark; the bed dragged from the drip.
- **Grata:** her own moment — she invents the vow; she charges the wind; she cannot read (her son reads her the panel); the reveal.
- **Felix:** his own moment — the sledge "a hand's breadth from his own foot", then "It's an old drum"; the hare bowl; "a name … on every wall in this town but mine".
- **Zosimus:** his own moment — the Hermes feud.
- **The walk-ons:** the leek woman's dent "the shape of Nuceria"; the coppersmith's alibi goat; the dyer's "He gave one to a mule this morning."; the fuller's wife's comb.
- **No secondary character is a function only.**

---

## The Tomorrow Test
**What the reader remembers:** a naked toddler at a street fountain hands her a wet black pebble and keeps two fingers on it "until he was sure it would stay", and she cannot stop crying; by the time she gets home the stone has dried gray. Then Valens turns it over by the lamp and says "That's a good stone,". Second: "It's a child you've got."
**Anchor type:** BOTH. IMAGE: the pebble; the bowl on the tile cart; Zosimus's eyes shut and his thumb on the welt; the leaf's shadow on Valens's lips. QUOTE: "It's not my fish. It's a child you've got."; "That's a good stone,".
**Verdict:** **ANCHOR EXISTS** (strong) → +0.5 CVI-L.
**Pattern check:** this anchor's engine is **a gift from a stranger that undoes her**. Ch.19's was an act withheld (the photograph), Ch.18's a gift handed over without a word, Ch.17's a bystander's appetite. The engines differ.

## The Shareability Test
- **What a reader texts a friend:** "a baby hands her a pebble at the fountain and she just SOBS and the dad's like 'I never touched her' 😭 and then the landlady figures out she's pregnant from the FISH SAUCE"
- **Running count:** at least eight shareable chapters (Ch.6, 8, 12, 15, 17, 18, 19, 20).

---

## Reader Reports

### The Devourer (8k after an 8.3k arrival)
- **The first page pulls:** a thief "enjoying his soup", a leek woman who won't stop talking, Grata's paint flood.
- **What keeps them going:** the bowl thrown away (why?), the bed and the drip, and Felix taking the sledge.
- **Where they slow:** S5. The night crew, then the fountain pier's graffiti one wall at a time, each read aloud for Felix. Two long chapters back to back, both without a plot engine, is felt here.
- **What hooks them back:** the fountain arrives with no warning in the middle of wedding gossip, and from there they read fast to Grata's line.
- **Where would they stop?** Not at the end. "It's a child you've got." pushes them straight into Ch.21.

### The Critic
- **Would underline:**
  - "Then he kept two of his fingers on it, after it was in my palm, until he was sure it would stay.";
  - "It was gray, and not black at all.";
  - "My lower lip found that before my eye did.";
  - "Under it was the one part of his face the dust had not reached.";
  - "The shadow of a leaf lay over his open lips and stirred when the leaf stirred.";
  - "He opened his eyes, offended for the lamp.";
  - "She can't climb down to me."
- **Would notice and mind:**
  - "while the carts went by behind me", the held-moment device this reader has now seen five times (R1);
  - the jar running over at a fountain while a woman waits behind her, which they read in Ch.14 (R2);
  - "a stone like any other in any gutter in the town", the narrator explaining the anchor she has just shown (C5);
  - the payments closing scene after scene (C4).

### The Hostile
- **"She was 'waiting my turn' at the spout. What water ran from her jar's lip?"** None could. → **L3** (with R2).
- **"Garum by the cupful? And he asks for more?"** It reads as drinking fish sauce. → **L2** (on his bread).
- **"'the two molars that had held a filling': Ch.2, 5 and 7 give her one filled molar."** → **L1**.
- **"The stewpot woman says she'd only break it again looking for a hidden crack, and Mara hides it anyway?"** Yes. It is Mara's habit, before the lamp. **INVESTIGATE, kept:** it is the "before" of the chapter's turn, and nothing glosses it.
- **"Lime from Puteoli?"** Puteoli sent pozzolana (audit I-04). **INVESTIGATE, kept** (author's call).
- **"A boy's crescent amulet?"** Usually a girl's lunula (audit I-05). **INVESTIGATE, kept.**

### The Casual Reader (airport, 10 pages)
- **Would keep reading, and would tell a friend.** In this mid-book chapter the life is the plot, and the life is very good company:
  - Grata, who is now the book's best supporting character;
  - Felix losing a fight to a column drum;
  - Valens tucking a fig tree in for the night.
- **The pebble is the moment this reader cries.** The pregnancy line is the moment they turn the page.
- **The only drag** is the third wall of graffiti in a row.
- **No vibes problem.** **9.0** (not 9.5: two long, low-plot chapters back to back).

### The Devoted Reader (active: long saga)
- **Would adopt it.** This is the chapter they quote in the re-read thread.
- **What they will find:**
  - Ch.2's thumbnail-with-eyes-shut on her own invisible join, answered by a stranger's thumb on a visible one;
  - the first tremor note in Fenn's back leaves;
  - the amazed wall;
  - Polybius's I on the crack;
  - Felix's "a name … on every wall in this town but mine" before Ch.21's palm;
  - the hare bowl (Ch.2's lamp had a hare on its discus; probably an accident, and harmless).
- **What they will catch (and should not):**
  - the Ch.14 fountain (R2);
  - "Today," / "Not tomorrow." in Valens's mouth again (C1);
  - Kallia's "Twice. Once… once…" from the turner (C2).
- This reader drives CVI-Legacy, not launch.

---

## Cross-Reader Matrix
| Issue | Devourer | Critic | Hostile | Casual | Devoted | Severity |
|---|---|---|---|---|---|---|
| R1 SPENT moving-thing hold (Ch.19's cut string) | | ✓ | | | ✓ | **SHOULD FIX → blocking** (SPENT, "0 more anywhere") |
| R2 + L3 Ch.14 fountain skeleton; empty jar spills | | ✓ | ✓ | | ✓ | **IMPORTANT → blocking** (set-piece reuse + logic, at the anchor) |
| R3/R4 sample-07 (reserved Ch.42) at two body beats | | | | | ✓ | INVESTIGATE → blocking (reserved-sample lift) |
| R10/R11/C7 sample-11 pickup; CLOSED object-to-eye; "came for it" ×3 | | ✓ | | | ✓ | SHOULD FIX → blocking (CLOSED for Ch.20) |
| R6/R7/R18 samples 10, 08, 02 | | | | | ✓ | INVESTIGATE (fix: cheap) |
| R9 Ch.9's wall image | | | | | ✓ | INVESTIGATE → blocking (named in the brief) |
| R8, C7 audit recasts moved sideways | | ✓ | | | ✓ | SHOULD FIX |
| C1–C3 borrowed whole lines; SPENT wasp lore | | ✓ | | | ✓ | SHOULD FIX → blocking (law) |
| C4 payment buttons | | ✓ | | | | INVESTIGATE → fix (device) |
| C5 gloss + doubled pause at the stone | | ✓ | | | | INVESTIGATE → fix (#11 at the anchor's coda) |
| L1 molar; L2 garum cup | | | ✓ | | | INVESTIGATE → fix (logic) |
| S5 graffiti stretch sags | ✓ | | | ✓ | | SHOULD FIX → **not changed** (structural; the ledger's wall-writing collage; see PATH note) |
| R12–R19, D1–D7 frames, rulers, doubles | | ✓ | | | ✓ | INVESTIGATE |
| Ch.31 tableau partly spent | | | | | ✓ | INVESTIGATE (forward guard, no change) |

**No CRITICAL. No VIBES PROBLEM.** The blocking items are book law. Only the fountain spill is reader-facing, and only to the Hostile and the Critic.

---

## Revision Recommendations (Ranked)
*Every replacement string below was put through the same reuse checks as writer prose:*
- *the 3–7-gram scan against Ch.1–19 and all 13 voice-bank samples, stop-word-bounded strings included;*
- *the in-chapter repeat scan;*
- *a grep of every at-risk frame;*
- *the real gates, with the whole set swapped in.*

*Eleven first drafts failed and were changed before the set was tested. They are logged under "Replacement strings rejected".*

### Fix order: Logic (L1–L3) → Character (C1–C7) → Reuse and law (R1–R19) → In-chapter doubles (D1–D7)

| # | Location | Problem type | What happens now | Why it fails | Revision direction (exact swap) | Project rule? |
|---|---|---|---|---|---|---|
| L1 | l.295 | Logic / Continuity | "It found the gap at the two molars that had held a filling since sixth grade," | Ch.2, 5 and 7 give her **one** filled molar. ("the old filling" was rejected: Ch.7's own words.) | → "It found the gap beside my sixth-grade filling," | No |
| L2 | l.583, l.587 | Logic (period) | "ladle some for a carter" … "and put his cup out for more of it." | It reads as garum drunk by the cup (audit I-06). | → "ladle some onto a carter's bread" … "and pushed his bread across for more of it." (His cup of wine stays at l.587's first clause.) | No |
| L3 | l.503 | Logic | "It ended when it ended. The jar was half empty by then, and I filled it again at the spout" | She was "waiting my turn" (l.467), so the jar was empty. This pairs with R2. | → "It ended when it ended. I filled the jar at the spout and carried it home." | No |
| C1 | l.575 | Character (borrowed lines; SPENT lore) | "Today," he said. "Not tomorrow. Tomorrow the wasps have them." | Valens's Ch.17 whole line and his Ch.11 whole line, joined, carrying Ch.11's wasp line (SPENT). | → **cut the paragraph.** The fig "came away into his hand by its own weight" and goes "on my plank among the broken things"; "I ate all three." follows. His silence is his card (hands find work). | Yes: **a 1–2-word whole line in the same mouth is a borrowed line** (see gate proposal). |
| C2 | l.287 | Character (borrowed shape) | "Twice," he repeated. "Once for my wife's mother's funeral. Once for a horse that died." | "Twice" as a reply is in its 5th chapter, and this rebuilds Ch.7 Kallia's "Twice. Once on … and once in …". ("and then a horse" was rejected: the "he said, and then" 4-gram, Ch.4.) | → "It buried my wife's mother," he said, "and after her a horse." | Yes: **"Twice" as a reply: CLOSED.** |
| C3 | l.189 | Character (borrowed line) | "What's in it?" | Valens's Ch.15 "What's in it, then?" | → "What's she sent?" "Grata's olives." still answers it. | No |
| C4 | l.347, l.361, l.569 | Character / Style (button device) | "She paid me, and wrapped it up…" / "He paid that time in dice." / "He paid me, and put the lamp back" | Payment-in-kind closes 4 mini-scenes (l.71 bronze, l.171 cheese, l.329 wine, l.361 dice), with 2 more "paid me" beats. | → "She wrapped it up again in the same wool." / cut " He paid that time in dice." / "He put the lamp back in the fold of his tunic," **3 payments remain, each worded fresh** (bronze, cheese, wine). | Yes: **payment-in-kind as a scene close: CLOSED after Ch.20.** |
| C5 | l.513 | Character (pause) / Style (#11) | "He looked at it a while by the lamp, small and dry and gray, a stone like any other in any gutter in the town, and passed it back" | A doubled pause ("He waited" + "a while"), and a gloss that explains the anchor's ordinariness after l.505 has shown it. | → "He looked at it by the lamp, small and dry and gray, and passed it back to me" | No |
| C6 | l.539 | Character (gesture double) | "He scratched in his beard with a black finger." | "black finger" ×2 in 12 lines (l.527). The card says "Each beat once." | → "He scratched in his beard." | No |
| C7 | l.289 | Character (sideways recast) / Style (sample-11) | "When he came for it he ran a fingertip round the slot and was satisfied." | The audit's W-10 recast puts the anchor's touch-test on a walk-on one section early. It is also sample-11's "came for it". ("he had it back that evening" was rejected: "he had it" ×5 book-wide. "said when he saw it" was rejected: the tic gate tripped on "he said when" / "said when he".) | → "I joined it for him next day and left the slot as it was, and he collected it that evening." | Yes: **a recast greps the anchor of its own chapter.** |
| R1 | l.295 | Style (SPENT device) | "tooth by tooth, while the carts went by behind me." | A held moment measured by passing traffic, the string Ch.19's R1 cut ("0 more anywhere"). | → "tooth by tooth." | Yes: **gate proposal, below.** |
| R2 | l.493 | Style (set-piece reuse) | "Water from the jar's lip ran down my side and my leg and into my sandal, and I could not right the jar, because my hands were full. The next woman in line reached round me and pushed her jar in under the bull's mouth." | Ch.14 l.10's frozen-at-the-spout beat (water down the body; the woman waiting behind), at this chapter's anchor. It is also a moving-people measure. ("ran out over the paving" was rejected: "over the paving" is l.579. "slopped … onto the stones" was rejected: Ch.6's water carried on the hip.) | → **cut both sentences.** The paragraph ends "My mouth was open. I could not shut it." The pressure voice is purer for it. | Yes: **a public-spout beat greps Ch.6, Ch.13 and Ch.14.** |
| R3 | l.489 | Style (reserved sample) | "I put out my hand." | sample-07 (Ch.42): "I put my hand out." ("I opened my hand" was rejected: Ch.9. "my palm open" was rejected: Ch.11.) | → "I turned my hand up." | Yes: **sample-07 strings are 0 before Ch.42, at any length.** |
| R4 | l.583 | Style (reserved sample) | "and my hand went over my mouth." | sample-07: "My hand went in." | → "and I covered my mouth." ("behind my hand" at l.585 still pays.) | (as R3) |
| R5 | l.499 | Style (sample-09; Ch.15) | "From his father's hip the boy watched me. I could not stop." | "could not stop" is sample-09's laugh-into-tears (reserved for Ch.25) and Ch.15's laugh. | → "From his father's hip the boy watched me cry." | No |
| R6 | l.143 | Style (sample-10) | "It will hold anything you put in it." | sample-10's whole line "It will hold," in a bed exchange. | → "Anything you put in it." | No |
| R7 | l.365 | Style (sample-08) | "Up there in this." | sample-08's "There's nothing up there in this," (weather, a height). ("Out in this" was rejected: Ch.5.) | → "In this rain." | No |
| R8 | l.545 | Style (sideways recast; #11) | "dark and glossy from his thumb, pressed there each dawn for years to tip the oil in." | Ch.3's knucklebone, "gone glossy, the polish fingers left on a thing after a very long time", put here by the audit's W-02 fix. | → "Round the filling hole the clay was black from his thumb." | No |
| R9 | l.437, l.453 | Style (Ch.9 document shape) | "which was scratched over as high as an arm could stretch" / "older than everything round it, its letters gone soft at their edges, there was one more." | Ch.9 l.8: "written over from the paving to as high as a man could reach … The old ones had weathered soft". ("in an older hand" was rejected: Ch.6's "an older hand than the rest of him". "than the rest" was rejected: Ch.3, Ch.6.) | → "…to read him the pier at its back." / "Highest of all on the pier there was one more." | No |
| R10 | l.345 | Style (sample-11; CLOSED beat) | "She came for it while Grata was at the baths, and stood in the opening holding it to the daylight, looking for the break and not finding it." | sample-11's pickup ("When she came for it she held it up to the doorway"), and the walk-on object-to-the-eye beat (CLOSED for Ch.20). ("could not find the break" was rejected: Ch.13, "He could not find the join on his own grandfather's incense stand".) | → "She called for it while Grata was at the baths." Her next line ("There's his mother's bottle … that nobody ever threw at anybody.") carries the unfound break. | No (already a rule) |
| R11 | l.561 | Style (sample-11) | "Zosimus came for it two mornings later" | "came for it" ×3 (sample-11). | → "Zosimus was back two mornings later" | No |
| R12 | l.283 | Style (Ch.18 frame; arm-marker family) | "shavings of bone in the hair of his arms." | Ch.18's "flour dried white in the hair of his forearms", and the 3rd tradesman's arm marker in the chapter. | → "He was a small man with a curl of bone caught in his hair." | Yes: **a tradesman's arm marker: ≤2 per chapter.** |
| R13 | l.213 | Style (camera layout; Ch.15 heat; #1) | "Through the lens I had the jar on the left and his gray soles on the right, and the leaves above his face; the heat rising from the tiles made all of it waver, so I held still for it to settle and it never did." | The finder layout ("on the left", Ch.19's camera beat) as a three-item sequence, plus Ch.15's heat-scene "held still for". ("and it would not settle" was rejected: Ch.13's 4-gram.) | → "Through the lens the heat off the tiles kept him and his tree wavering, and the waver never settled." "I took it, and wound on, and he slept through both." is untouched. | Yes: **camera beats: no left/right layout after Ch.20.** |
| R14 | l.547 | Style (process repeat) | "I warmed the pieces and the resin, drew the bead along the broken shoulder with the cane and brought the faces home, and the brown welt swelled from the break. Then I let it stand." | It re-narrates the bowl's process (l.119–121); "brought the faces" ×2. ("joined them along the shoulder" was rejected: "along the shoulder" ×2.) | → "I warmed the pieces and joined the shoulder, and when the welt swelled from the break I let it stand." The trim, the warmed knife and the soot are untouched. | No |
| R15 | l.169, l.407 | Style (frame ×4) | "with the tip of the knife" / "with the point of a nail" | "with the tip / point of [tool]" ×4 (l.71, 147, 169, 407). | → "with the blade" / "with a nail" | No |
| R16 | l.385 | Style (ruler) | "from the eaves down to the height of a tall man's chin" | A reach-height ruler (Ch.19 "to the height of a man"; Ch.9). | → "from the eaves halfway to the paving" | No |
| R17 | l.63 | Style (#11; comprehension) | "\"Which are the dogs?\" The word belonged to tinkers." | A gloss justifying the question. | → "\"Which are the dogs?\"" | No |
| R18 | l.27 | Style (sample-02) | "you've the face of a payer" | sample-02's signature simile opener, which voice-dna §1 quotes. | → "you've a payer's face" | No |
| R19 | l.579 | Style (Ch.19 counter) | "with a ladle on its lip" | Ch.19's spent counter: "a ladle hung on the lip of each". ("the hot end of her counter" was rejected: "end of her counter" ×2 with l.319.) | → "It stood at her counter's brazier end, and every morning" | No |
| D1 | l.59 | Style (double) | "standing proud of the clay like scabs" | "proud of the clay" ×2 (l.547, the lamp, keeps it). ("up from the" was rejected: the tic gate, "up from the" ×3 book-wide.) | → "raised on the clay like scabs" | No |
| D2 | l.501 | Style (double) | "his father told a woman with a basket," | "a woman with a basket" ×2 (l.13). ("said over his shoulder" was rejected: Ch.4.) | → "his father insisted," | No |
| D3 | l.443 | Style (double) | "Under it, in a different hand, deeper:" | "Under it, in [a] … hand" ×2 (l.13). | → "Someone had answered it in a deeper hand:" ("Somebody/Someone had" is now 1 in the chapter.) | No |
| D4 | l.277 | Style (Ch.19 frame) | "the bed walked an inch on its legs" | The same bed, the same measure, one chapter on (Ch.19 "let him down an inch"). | → "the bed walked on its legs" | No |
| D5 | l.553 | Style (double) | "The stoker from the baths at the crossing." | It repeats l.527's narration label in Mara's mouth. | → "The furnace man at the baths." | No |
| D6 | l.571 | Style (double) | "in that same month of the olives," | "that same month" ×2 (l.527). | → "with the olives," | No |
| D7 | l.549 | Style (double) | "Valens got in from the mules at dusk, while the lamp" | "dusk" ×4 for arrivals; "in from the mules" ×2 (l.41). ("Valens came home" was rejected: Ch.19's 3-gram.) | → "Valens walked in while the lamp" | No |

**Not changed (judged; INVESTIGATE only):**
- **"It's not my fish. It's a child you've got."** It refutes Mara's own accusation, so it is not a define-by-negation opener. It is the protected close.
- **"He wants to find it in the dark."** It answers "Left like that." with a reason. It is not a relayed order.
- **"It was up on the pier of a cookshop…"** (l.13). After audit W-01 the Ch.9 residue is a bare placement sentence.
- **The stewpot made invisible against the customer's joke** (l.67–71). It is Mara's "before" and is unglossed.
- **The night crew and *Lantern-boy, hold the ladder.*** Real (CIL IV 7621), and nobody from the household holds anything. The forward guard for Ch.31 is above.
- **Felix has Mara read five walls.** This is the collage's delivery, worded fresh each time. WATCH.
- **Walk-on exits on a trait** (leek woman, girl, carter, Zosimus ×2, painters): WATCH.
- **"lime" from Puteoli; the boy's crescent amulet** (audit I-04, I-05): author's call.
- **The hare bowl against Ch.2's hare lamp:** likely accidental and harmless.
- **"put her hand on my forearm"** (l.435): a sample-07 3-gram ("Aelia put her hand"), but generic, and Grata's card axis. Kept.

**Replacement strings rejected during testing** (so the editor does not reach for them):
- "the old filling" (Ch.7);
- "could not find the break" / "find the join" (Ch.13);
- "and then a horse" (Ch.4 4-gram);
- "he said when he saw it" (tic gate: "he said when" / "said when he" ×3);
- "he had it back" ("he had it" ×5);
- "up from the clay" (tic gate ×3);
- "I opened my hand" (Ch.9); "my palm open" (Ch.11);
- "Out in this" (Ch.5);
- "in an older hand" (Ch.6); "than the rest" (Ch.3, Ch.6);
- "and it would not settle" (Ch.13);
- "joined them along the shoulder" (in-chapter double);
- "the hot end of her counter" (in-chapter double);
- "Valens came home" (Ch.19);
- "said over his shoulder" (Ch.4);
- "ran out over the paving" (l.579); "slopped onto the stones" (Ch.6).

### The fix script and the tested result
- **Script:** `/tmp/claude-0/-home-user/63791ee5-159c-5791-9429-07920f8d9417/scratchpad/ev20/ch20-fixes.py` (`python3 ch20-fixes.py <in.md> <out.md>`).
  - It holds 41 swaps (L1, L2a/b, L3, C1–C7a, R1–R19 with R9a/b, R15a/b, D1–D7).
  - Each OLD string must occur exactly once in the body, or the script aborts.
  - The header comments are untouched.
- **Tested output:** `/tmp/claude-0/-home-user/63791ee5-159c-5791-9429-07920f8d9417/scratchpad/ev20/ch20-fixed.md` (md5 `d650c6c57f4d671f62976c2276fb14c7`, sha256 `edced3c3…`).
- **Results with the copy swapped into the manuscript path, run from /home/user/Books:**
  - `check_chapter.sh 20`: **all clean.**
    - style: 7,811 words, simile 1.4/1k, em-dash 0, foreshadow 0;
    - grammar 0; rhythm 0;
    - show/tell: 7,814 words, dialogue **35.2%**, no flags;
    - voice-wear strict: clean;
    - tic gate: clean (and-chains 2/9, credential 1, pivots 0, "So" 0; gesture classes clean);
    - echo **0**; command echoes none; spoken-line echoes none;
    - metaphor 1.8 fig/1k, median 15;
    - shape CLEAN.
  - `tic_report.py --gate`: clean (exit 0).
  - `--echoes 20`: none / none / none.
  - `shape_check --strict`: `20 7785 6 35 16 narrative dialogue`, CLEAN (exit 0).
  - **A first test run failed the tic gate** on two of my own strings ("up from the"; "he said when" / "said when he"). Both were replaced and the set re-run clean, as listed above.
- **Restored:** the manuscript checksum was verified after every run (md5 `59c35189…`, sha256 `4dc4d10e…`).
- **Post-fix numbers:**
  - **7,785 words** (shape_check), 7,811 (style), 7,814 (show_tell). That is −267, **85 above the 7,700 floor**, against an 8,200 target. **Do not cut further in this chapter.**
  - **Dialogue 35.2%** (band 30–40, floor 30 ✓); median 16 shape / 15 metaphor (mid ✓); 6 breaks; `narrative` → `dialogue`.
  - **#11:** 3 firm (0.39/1k) ✓. **Paragraph-final negations:** 7 (0.90/1k) ✓. **Present-tense generalisations:** 0 ✓.
  - **Borrowed whole lines:** 0. **Payment buttons:** 3, worded fresh. **"came for it":** 0. **Object-to-eye:** 0. **Moving-thing holds:** 0. **Sample strings (07, 08, 10, 11, 02):** 0.
  - **Tool-tip frames:** 2. **"dusk":** 3. **Semicolons:** 12. **"so that":** 3. **"the size of a":** 1. **Em-dash:** 0. **"as if":** 0.
  - **Anti-AI:** 7/20, −0.875 (clean).

---

## Strengths to PRESERVE (do not touch in polish)
- **The opening:** the notice, the thief "enjoying his soup", the leek woman's dent "the shape of Nuceria if you stand still for it", and the cook watching her jar.
- **Grata's paint flood** and "Spell it right. There's people on this street can read."
- **The coppersmith's alibi goat** and "Like nothing on earth," … agreed, pleased.
- **The bowl:** Felix's "a drop of two of me"; the lentisk night; "My lower lip found that before my eye did."; the bowl on the tile heap; "Have you got any more you don't want?"; Felix's "Can a mended thing go bad in a night?"; "We'll manage with the cookpot,".
- **The clay pig** that talks again.
- **The forum:** the drum that "gave up another chip of itself"; the rag line on his face; Felix and the sledge.
- **The named frame:** the leaf's shadow on his lips; "I took it, and wound on, and he slept through both."; "On a man asleep." / "And a tree."
- **The fig:** pinched for wood; wrapped twice in the dark; "She can't climb down to me."; the late ripening by its own weight; "I ate all three."
- **The drip that follows his foot.**
- **The tremor note**, exactly as written.
- **The toothpick:** the turner's "Teeth this end. Ears the other. Don't mix them."; Valens keeping "to the other"; Grata's vow.
- **The fuller's wife:** "I want him looking at that shelf for a year … wondering what it is he's sorry for"; the comb.
- **Polybius:** "Polybius," … "Enough. No."; "Chalk," / "Ask anybody."; Infantio; the I on the crack; "It's red,".
- **The fountain:** the wedding gossip; the two fingers; "I was crying."; the dyer's defence; Grata's wordless cup; "It was gray, and not black at all."; "That's a good stone,".
- **The lamp:** "Leave me the crack."; the soot rubbed in; both thumbs on the welt; "offended for the lamp"; Hermes.
- **The fish jar** and the closing speech.

---

## PATH TO 8.5 (mandatory; the Floor is 8.0)
- **Prose & Voice 8.0 → 8.5 requires the reuse-and-law cluster gone, with no repeat moved sideways.**
  - The chapter already has its stopping sentences (the two fingers; "It was gray, and not black at all.").
  - **What is missing** is a page that reaches for nothing the book or the voice bank has spent, and a fountain that trusts the body without Ch.14's water.
  - **Surgery, in this order:**
    1. **Logic:** **L3** with **R2** (the fountain: cut the spill and the next woman; fill the jar once at the end); **L1**; **L2**.
    2. **The SPENT device:** **R1**.
    3. **The reserved and calibration samples:** **R3, R4, R5** (sample-07, sample-09); **R10, R11** (sample-11 and the CLOSED object-to-eye); **R6, R7, R18**.
    4. **Book reuse:** **R9** (Ch.9's wall); **R8** (Ch.3's gloss); **R12, R13, R19, D4** (Ch.15/18/19 frames); **R14** (the lamp re-narrating the bowl).
    5. **Narrator frames and rulers:** **R15, R16, R17**.
    6. **In-chapter doubles:** **D1–D7**.
  - **Expected:** Prose 8.5. The underline set is untouched, #11 drops to 3 firm, and every gate stays clean (tested).
- **Characters 8.5 holds; C1–C7 keep it there and are part of the set:** the borrowed lines and wasp lore, "Twice", the payment buttons, the doubled pause, "black finger", and the fingertip recast.
- **Run all 41 swaps together** (the script). They were tested as one set; a subset leaves interim collisions (for example, R2 without L3 leaves "The jar was half empty by then" with nothing to have emptied it).
- **Pacing 8.5 is not floor-holding.** The S5 sag (the Devourer and the Casual reader) is **not** fixed by surgery: the ledger's "year told in wall-writing" wants those walls, and the chapter is now 85 words from its floor.
  - If a later polish wants 9.0, the lever is **one wall fewer in S5**, with the words moved to a plain scene beat elsewhere, for example a line more for Valens in the rain.
  - It would need its own tested set.

---

## Pacing check (one line for `feedback/progress.md`)
**Ch.20 (cycle 0):** Collage, a year told in wall-writing and repairs (spring AD 72 → the olive month of 73, seven sections). It sits between Ch.19's Chronological walk and Ch.21's Chronological two-rooms ✓.
- **Length:** 8,052 words (target 8,200; range 7,700–8,700; not padded). 7,785 after the fixes, still inside; **do not cut further**.
- **Dialogue** 34.2% (30–40 ✓; 35.2% after); **6 breaks** ✓; **gear median 16** (mid ✓).
- **Signatures:** `narrative` → `dialogue`. Ch.18 is `I-statement` → `punch` and Ch.19 `scene-set` → `long-fade`, so nothing runs three in a row. The hook is VOICE (not CONTRAST after Ch.19), and the pull is REVELATION (not QUESTION PLANT).
- **Neighbours:**

  | Ch | Words | Gear (median) | Dialogue | Approach | Breaks | Open → close |
  |---|---|---|---|---|---|---|
  | 18 | 2,523 | mid (15) | 34% | Single-scene | 0 | I-statement → punch |
  | 19 | 8,251 | high (18) | 25% | Chronological | 4 | scene-set → long-fade |
  | **20** | **8,052 → 7,785** | **mid (16)** | **34% → 35%** | **Collage** | **6** | **narrative → dialogue** |
  | 21 | 7,200 planned | mid | 40–50% | Chronological | 3 | dialogue → question |

- **The design works.** The gear steps down from high to mid, and the dialogue rises 25 → 34 → (40–50) as Part Two turns from place to people.
- **The one cost:** the book's two longest chapters sit back to back, and neither has a plot engine before its last pages. That is planned (8,400 / 8,200), and it is accepted. Ch.21 must open fast (its ledger row is mid-dialogue, with Felix bursting in).
- **Emotional slot ✓:** after the arrival (the dread is all in the reader), a year of belonging. Then the book's first unprompted break (the fountain), and a positive revelation that opens Ch.21's "family coming".
- **Value shift ✓:** a living needed (−) → a trade (+) → the bowl thrown (private −) → the fountain (±) → the lamp (+) → a child (+).
- **Speed ✓:** documents quick; repairs slow; the fountain sudden.
- **Sag (accepted):** S5, about 1,300 words of night crew and pier graffiti.
- **Book:** 115,514 words against 123,200 cumulative target (−6.2%); 115,247 after the fixes. Projected at about 243k against the 220k floor ✓ and the 245k target (slightly under: watch it, never pad).

**Verdict: OK.**

---

## Cross-Book Pattern Detection (Ch.1–20)
1. **The fixer's fix becomes the next finding.**
   - The audit's W-02 and W-10 recasts each moved a repeat sideways: Ch.3's gloss onto the lamp, and the anchor's touch onto the turner.
   - The editor rule ("a recast must not move a repeat sideways") exists, but the continuity repair runs before the evaluator with no n-gram pass of its own.
   - **Proposal:** the continuity repair runs `tic_report.py --echoes N` **and** a 3–4-gram pass against Ch.1–(N−1) and the voice bank on every changed sentence before it hands over.
2. **Whole lines under the gate's floor.**
   - "What for?" (Ch.19), and now "Today,", "Not tomorrow." and "Twice". The echo scan's whole-line floor is above two words, so same-speaker one- and two-word lines pass.
   - **Gate proposal (UPDATE RULE, root `tools/tic_report.py` and the template):** in the spoken-line layer, flag a 1–2-word spoken sentence repeated by the **same speaker** across chapters, or by anyone in a 3rd chapter. Speaker attribution can be approximated by the nearest tag within 2 sentences.
3. **The moving-thing hold, a sixth time** (Ch.1, 5, 9, 19 ×3 before the fix, 20).
   - The Ch.19 eval's HOLD-MEASURE proposal (`while … went/came/passed (by|past|behind)`) would have caught l.295 mechanically.
   - **Implement it before Ch.21.**
4. **Voice-bank strings below five words.**
   - This chapter hit samples 07 (reserved for Ch.42), 08, 10, 11 and 02 with 3–4-word strings at the same beats.
   - **Proposal:** for the RESERVED samples (07 → Ch.42, 09 → Ch.25, 13), lower the echo scan's sample floor to 4 words, stop-word-bounded included.
5. **What varies, as it should:**
   - the structure (Collage after Chronological);
   - the opening (a document, VOICE) and the ending (a spoken reveal);
   - the gear (mid);
   - the anchor's engine (a stranger's gift);
   - the body rebel (tears, the mapped channel; then nausea, new);
   - the dialogue band.

**Bookkeeping (orchestrator):**
- **Re-sync the bible's Ch.20 blocks to the final page.** They quote the writer's draft (audit I-09). Examples:
  - **At-risk after Ch.20:**
    - "Nobody at home had ever paid me to leave a join where it could be found." is "said once" in the bible, but the disruptor cut it → delete;
    - "Then they'll want it shouted." → "That wants shouting.";
    - "Make it hold. I cook in it." → "Make it tight. My oil lives in it.";
    - (after the fixes) "Today," … "Not tomorrow. Tomorrow the wasps have them." → cut;
    - "Twice … Once … Once" → "It buried my wife's mother," … "and after her a horse.";
    - "It will hold anything you put in it." → "Anything you put in it.";
    - the bed "walked an inch" → "walked on its legs";
    - the named frame's waver → "Through the lens the heat off the tiles kept him and his tree wavering, and the waver never settled.";
    - the fountain: the jar spill and "the next woman" → cut; "I put out my hand." → "I turned my hand up."; "I could not stop." → "the boy watched me cry.";
    - Grata's "the face of a payer" → "a payer's face".
  - **ZOSIMUS:**
    - "hugs the lamp to his breastbone" → "cradled the lamp in his palm";
    - "Dropped it on the furnace stair" → "The furnace stair did it";
    - "since before the earthquake" → "three summers";
    - name "for the tag, Zosimus, of the baths" → "Zosimus. Of the crossing baths.";
    - (after the fixes) "Zosimus was back two mornings later"; "He scratched in his beard."; no payment beat.
  - **Ch.20 walk-ons:**
    - the coppersmith's "Two winters back" → "This winter gone";
    - the dyer "arms blue to the elbow" → "hands were stained blue from somebody's vats";
    - the turner: pays in the toothpick only (dice cut); "a curl of bone caught in his hair";
    - the stewpot woman's lines → as on the page.
  - **FELIX:** "holds the painters' ladder" → "sits among the painter's pots" (audit C-03).
- **At-risk after Ch.20, add (after the fixes):**
  - **"Twice" as a reply:** CLOSED;
  - **1–2-word whole lines in the same mouth across chapters:** 0 ("Today,", "Not tomorrow.", "What's in it?" are Valens's spent lines);
  - **payment-in-kind as a scene close:** CLOSED;
  - **"came for it" (a pickup):** CLOSED (sample-11);
  - **tradesman arm markers:** ≤2 per chapter;
  - **camera left/right layout:** CLOSED;
  - **tool-tip frames ("with the tip/point of"):** ≤2 per chapter;
  - **a public-spout freeze** (Ch.14, Ch.20): SPENT;
  - **sample-07's "I put my hand out" / "My hand went":** 0 before Ch.42;
  - **forward guard for Ch.31:** see "The book's own laws";
  - **no line in Ch.21–24 links the fountain to the pregnancy** (audit I-03).
- **Entity and handoff cascades:**
  - Grata knows about the pregnancy, and the carter at the counter heard it. Valens and Felix do not.
  - Ch.21 must place Valens's knowing early (audit I-10).
  - The letter for Plautia went by a carter to the Puteoli board (Ch.21's knowledge path).
  - The Kalends visits to the door are canon.
  - Felix still believes Valens cannot read.
  - Plautia's knife is still on loan.

---

## VERDICT
**POLISH. Gate NOT MET at cycle 0. PASS expected after the tested fix set.**

| Measure | Result |
|---|---|
| Genesis Floor | **8.0** (Prose & Voice, merit; no cap) |
| Average | **8.71** |
| Casual | **9.0** |
| Scores | Originality 9.0 · Theme 9.0 · Characters 8.5 · **Prose 8.0** · Pacing 8.5 · Emotion 9.0 · Immersion 9.0 |
| Pacing | **OK** |
| CVI-Launch (CVI-L) / CVI-Legacy | **9.4** (8.9 + 0.5) / 7.1 (provisional) |
| Words / dialogue (constraints 7,700 / 30%) | 8,052 / 34.2% ✓ → after the fixes 7,785 / 35.2% ✓ |
| Mechanical suite | all clean (echo 0, spoken-line echoes none, command echoes none, tic gate clean, voice-wear strict clean, shape CLEAN) |
| Foreshadowing / END-1 reserved words / "seam" ruling | 0 / 0 / respected |
| AUTHOR-CP3-3 / END-1 / citizenship open | ✓ / ✓ / ✓ (0 lines) |
| Non-negotiables (the bowl thrown out; the fountain and pebble; the lamp's join left visible at the customer's wish; Grata clocks the pregnancy and closes the chapter) | ✓ all |
| Tremor note without reckoning / named frame | ✓ / ✓ |
| Memory triggered by the scene | ✓ |
| Explanation density | ✓ 0.62/1k → 0.39/1k |
| Paragraph-final negations | ✓ 0.99/1k → 0.90/1k (≤1.5) |
| Present-tense generalisation | ✓ 0 |
| No comparison in Valens's speech | ✓ |
| Command echoes (relayed included) / borrowed whole lines | 0 / **4 by hand** ("Today,", "Not tomorrow.", "What's in it?", "Twice") → 0 |
| Tics | catchphrases 0; gate classes clean; **payment buttons ×4, doubled pause, "black finger" ×2, arm markers** → fixed |
| Reuse (SPENT hold; Ch.14 fountain; samples 07/08/10/11/02; Ch.9 wall; Ch.3/15/18/19 frames; sideways recasts) | **FAIL** → cleared |
| Ch.31 reserved anchor | not pre-spent (judged); forward guard logged |
| AI patterns | 8/20, −1.125 → 7/20, −0.875 (clean) |

**After the fixes (41 swaps, tested together):**
- **7,785 words**; dialogue **35.2%**; median 16; 6 breaks; `narrative` → `dialogue`;
- every gate clean; anchors byte-identical;
- **Prose 8.5 → Floor 8.5 / Average 8.79 / Casual 9.0 / pacing OK.**
- The orchestrator applies the script, confirms md5 `d650c6c5…`, and runs the confirmation re-evaluation before CHECKPOINT 4.

**BIAS CHECK:** This evaluation was produced by the same system that wrote the prose. Confidence in scores above 8.0 requires external validation (beta readers, editors, comp analysis). The Casual 9.0 and Emotion 9.0 rest heavily on the fountain. A human reader may find the pebble more or less earned than I do, and a romance-first reader may rate a montage chapter with a light heart-load lower.

---
---

# Re-evaluation after cycle 1
**Evaluator:** book-evaluator (independent; did not write or revise this prose) | **Date:** 2026-10-21
**Text evaluated:** `manuscript/chapters/chapter-20.md`, md5 `d650c6c57f4d671f62976c2276fb14c7`. This is **byte-identical to the tested output of the 41-swap set above**, so all 41 swaps are on the page exactly as tested. It runs **7,785 words** by shape_check (7,811 style, 7,814 show_tell, 8,558 `wc -w`). Dialogue is **35.2%**.
**Read against:**
- the book's CLAUDE.md;
- STATE.yaml AUTHOR-CP3-3 and AUTHOR-END-1;
- `feedback/progress.md`: the Ch.20 brief and the "seam" ruling;
- voice-dna §0–§8;
- character-bible.md:
  - the at-risk blocks after Ch.18, 19 and 20, and the at-risk table;
  - the cards for GRATA, ZOSIMUS, FELIX and VALENS, and their Ch.20 lines;
  - the Ch.20 walk-on block;
- outline `## Chapter 20` and Ledger row 20;
- the cycle-0 evaluation above.

**Gates on the page as it stands** (`bash books/the-hour-of-ash/tools/check_chapter.sh 20`, run from /home/user/Books): **clean on every gate.**
- style: simile 1.4/1k, em-dash 0, foreshadow 0;
- grammar 0; rhythm 0;
- show/tell: no flags, 35.2%;
- voice-wear strict: clean;
- tic gate: clean (and-chains 2/9, credential 1, pivots 0, gesture classes under cap);
- echo 0; command echoes none; spoken-line echoes none;
- metaphor 1.8/1k, median 15;
- `shape_check --strict`: `20 7785 6 35 16 narrative dialogue`, CLEAN.
- `tic_report.py --echoes 20`: none / none / none.

## Verification of the 41 swaps (does the polish introduce anything new?)
**Method.**
- I diffed the cycle-0 page (md5 `59c35189…`) against this page at sentence level and found 37 changed sentences.
- Every changed sentence went through four checks:
  1. a 3–7-gram scan against Ch.1–19 and all 13 voice-bank samples, stop-word-bounded strings included;
  2. an in-chapter repeat count;
  3. a whole-spoken-line scan (every spoken sentence of ≤6 words against all earlier speech);
  4. a by-hand read for explanation and triads.

| Check | Result |
|---|---|
| **Cycle-0 law cluster gone?** | **Yes**, verified string by string on the page, every count 0:<br>• sample-07 ("put my hand out" / "put out my hand" / "my hand went");<br>• sample-11 "came for it";<br>• sample-10 "It will hold"; sample-08 "up there in this"; sample-02 "the face of a";<br>• the carts hold; Ch.9's "as high as" / "gone soft" on a wall; Ch.3's gloss on the lamp;<br>• Ch.18's "in the hair of his"; Ch.19's finder "on the left"; Ch.15's "held still for"; Ch.19's "with a ladle";<br>• "Not tomorrow" and the wasp line; "What's in it"; "Twice" as a reply; "a while";<br>• the empty-jar spill; "next woman"; "two molars"; "his cup out".<br>What remains is within its caps: payments 3, each worded fresh; "black finger" 1; "brought the faces" 1 (the bowl); tool-tip frames 2; "dusk" 3. |
| **Added explanation** | **None.** #11 stays at 3 firm (0.39/1k). R8's "Round the filling hole the clay was black from his thumb." carries no extension, and C5 removed one. |
| **New triad** | **None.** R14's process line is a two-step. C5's "small and dry and gray" is the designed pair carried over from cycle 0. |
| **Cross-chapter echo (gate)** | none / none / none. |
| **Cross-chapter echo (my n-gram pass)** | **No 4+-gram from any swap matches Ch.1–19 or the voice bank.** The 4-gram hits in the changed sentences ("the price of a", "I stood in the", "with my back to the", "fold of his tunic and"…) all sit in words the swaps did not touch. |
| **Borrowed whole spoken lines** | **None.** "What's she sent?", "Anything you put in it.", "In this rain.", "The furnace man at the baths." and "It buried my wife's mother," … "and after her a horse." match no earlier speech. |
| **Repeats moved sideways** | **Three small ones made by the swaps, and two cycle-0 items left standing. None reaches the floor.** All five are fixed below.<br>• **R5** put a third "cry" into eight lines ("I was crying." / "The crying heaved…" / "the boy watched me cry."). It re-narrates the stopping line → **F9**.<br>• **R9b** put "on the pier" into a run of five "pier" in 25 lines (l.437–461) → **F5**.<br>• **R12** moved the turner's marker from his arms to his hair but kept the device. On the page, all five tradesmen are introduced by their trade's residue on the body (forearms, hair, wrists, hands, elbows), and three of the markers are arms against the ≤2 the cycle-0 table proposed → **F10**, which takes the painter's off.<br>• **Left by cycle 0:**<br>  – **Felix's "He went up twice. Once to wrap her and once to see…" (l.373)** is the same "[N] twice. Once … and once …" skeleton that C2 closed on the turner. With Kallia (Ch.7) and the Ch.8 narration, this is its third chapter → **F1**. *This is the one book-law item.*<br>  – **"on his way" ×5** (l.41, 95, 425, 433, 561), against a book maximum of 2 elsewhere (Ch.9) → **F2, F2b, F3**. |

**Smaller doubles found on the fresh read (not made by the swaps):**
- the sun and the rain both "found" a flaw within 30 lines (l.345 "the sun came in sideways and found a line"; l.375 "the rain found a cracked tile") → **F4**;
- "I warmed the" twice in one paragraph (l.547) → **F6**;
- two men's alibis "at the bakery" (the whitewasher at l.395; the dyer at l.501, which is protected) → **F7**, on the whitewasher's side;
- Grata's "paint the candidates" (l.27) is Mara's Ch.15 3-gram ("paint the candidates' names") → **F8**.

---

## Genesis Score (cycle 1)

| Dimension | Cycle 0 | **Cycle 1** | Evidence | Cap / rule |
|---|---|---|---|---|
| Originality | 9.0 | **9.0** | Unchanged:<br>• the year in real wall-writing, read aloud to a boy who cannot read;<br>• Zosimus's break kept "where the boys can see it's spoken for" (l.539);<br>• the thrown bowl becomes a carter's present ("Have you got any more you don't want?", l.157);<br>• Polybius's I set on the crack (l.417). | Not 9.5: the montage form is known. |
| Theme | 9.0 | **9.0** | "Home as the place you mend" is still **never stated**. "seam" is 0, and no swap adds a pointer. The thrown bowl, the hidden bottle, the findable lamp and "He wants to find it in the dark." (l.557, an answer to a question) carry it. | #18 minor: the "found a flaw" verb chain and the fig's "bead of something sweet". |
| Characters | 8.5 | **8.5** | C1–C7 are on the page:<br>• Valens's fig day is now silent, which fits his card (hands find work): "he brought it down to the shop with two more and put them on my plank among the broken things." (l.573);<br>• the turner's "It buried my wife's mother," … "and after her a horse." (l.287);<br>• 3 payments, each worded fresh; one pause at the stone; one black finger.<br>Grata, Felix and Zosimus are on their cards. Chaos is 4/4, inhabited. Cover-the-name: PASS. | **Held at 8.5, not 9.0:** Felix's "twice. Once … once …" skeleton (F1) is still on the page; the trade-residue introduction covers 5/5 tradesmen (F10 → 4/5); walk-on exits on a trait stay WATCH. No tic. The gesture gate is clean, and I use its numbers. |
| **Prose & Voice** | 8.0 | **8.5** (+0.5, the cycle maximum) | **The reuse-and-law cluster that held cycle 0 is gone, and nothing replaced it at that weight.**<br>**Stopping sentences:** "Then he kept two of his fingers on it, after it was in my palm, until he was sure it would stay." (l.489); "It was gray, and not black at all." (l.505).<br>**The fountain is purer:** with the Ch.14 spill cut, the paragraph ends "My mouth was open. I could not shut it." (l.493), so pressure voice level 2 is enacted, not described.<br>**Underlines intact:** "My lower lip found that before my eye did." (l.151); "At every blow the drum rang and gave up another chip of itself." (l.185); "The shadow of a leaf lay over his open lips and stirred when the leaf stirred." (l.209); "He opened his eyes, offended for the lamp." (l.567).<br>**Ugly sentence present:** "Felix, at the opening, watching the rain go past:". | No cap. #11 is 0.39/1k. The residue is the five small doubles above, which are D-class, not floor-holding. **Not 9.0:** the S5 walls are read one by one in the same delivery. |
| Pacing | 8.5 | **8.5** | The ledger row is met on every field:<br>• Collage; `narrative` → `dialogue`; 6 breaks;<br>• dialogue 35.2% (band 30–40);<br>• 7,785 words (range 7,700–8,700);<br>• median 16 (mid).<br>Hook VOICE, pull REVELATION. The fountain still arrives without a lead-in. | Not 9.0: the S5 sag, and no forward question between the bowl and the fish jar (unchanged, structural, accepted). |
| Emotion | 9.0 | **9.0** | **Anchor:** the lamp — Zosimus, eyes shut, his thumb on the welt, "That's it," (l.561–563).<br>**Surprise:** the pebble and "I was crying." (byte-identical).<br>**Body rebel ×2:** the tears, and the nausea she misreads ("The jar had turned, I decided.").<br>**Techniques ≥5.** R2's cut strengthens the break. | Not 9.5: the designated anchor is quieter than the fountain, and the romance heart-load is light. |
| Immersion | 9.0 | **9.0** | L2 puts the garum on the carter's bread ("ladle some onto a carter's bread", l.581; "pushed his bread across for more of it", l.585). The CIL texts, lentisk, lead dogs, the beehive box and the FORTIS lamp are unchanged. | Unchanged INVESTIGATE items: lime from Puteoli; the boy's crescent. |
| **FLOOR** | 8.0 | **8.5** | Characters, Prose and Pacing | |
| **AVERAGE** | 8.71 | **8.79** | (9.0 + 9.0 + 8.5 + 8.5 + 8.5 + 9.0 + 9.0) / 7 = 61.5 / 7 | |

**Per-cycle rule:** Prose rises +0.5 (the maximum) on the 19 cited cycle-0 items removed; every other dimension is unchanged.

**Adjacent check:**
- C1 (Valens's fig line cut) costs Characters nothing. His silence over the three figs is truer to his card.
- R2 (the spill cut) costs Emotion nothing and gains Prose.
- No dimension falls.

**Anti-AI (cycle 1): 7/20, −0.875, clean band (commercial 0–8).**
- Found: #3 (adjective pairs and triads), #8, #10 (walk-on labels), #11 (3 firm, 0.39/1k), #13, #15 and #18, all minor.
- #1 is cleared.
- #12 is judged clear: "It's not my fish." refutes Mara's accusation.

**Character chaos (Mara): 4/4, inhabited.**
- the toothpick tour;
- the bowl thrown out;
- Dr. Pinsky's pick, triggered by the scene, one clause, returning to the doorway;
- the fountain and the fish jar.

**Voice under pressure:** demonstrated (level 2 at the fountain).

**Secondary characters:** every speaking secondary has a moment of their own (Grata, Valens, Felix, Zosimus).

**Book law:**
- foreshadowing 0; mountain, "seventy-nine", ash, casts and excavators 0;
- "seam" / "niche" / "painted plaster" / "hand flat" 0 / 0 / 0 / 0, and the door is never described ("On the Kalends." / "It is the same.");
- **AUTHOR-CP3-3 ✓:** no line remarks on the months without a child. "the look about the eyes my sister had with each of hers" and "It'll come with the heat." are Grata's present diagnosis.
- **AUTHOR-END-1 ✓:** no reserved Ch.41–44 words or shapes;
- citizenship 0 lines; Grata asks 0 questions; Valens: bare "No." 0, comparisons 0, orders to Felix 0;
- Felix: 8+ speeches end on a boast or a fact;
- kneel, bend, hand-on-knee and gait exits 0; present-tense generalisation 0;
- the tremor note is two sentences and makes no reckoning.

## Five readers (cycle 1)
- **Devourer:** reads straight through to "It's a child you've got.".
  - The one slowdown is still S5 (the night crew, then the pier's walls one by one).
  - The fountain's leaner paragraph moves faster.
- **Critic:**
  - **Would underline:** the two fingers; the stone drying gray; the lip finding the step; the leaf's shadow; "offended for the lamp"; "She can't climb down to me."
  - **What no longer bothers them:** the carts, the Ch.14 water and the payment buttons are gone.
  - **What they would still notice:** the third "cry" in eight lines, and Felix's "twice. Once… once…" if they remember Kallia. Both are fixed by F9 and F1.
- **Hostile:** L1–L3 are closed: one filling; garum on bread; the jar filled once, at the end.
  - **INVESTIGATE, kept (author's call):**
    - lime from Puteoli (pozzolana);
    - the boy's crescent (usually a girl's lunula);
    - the stewpot's invisible join against its owner's joke. This is Mara's "before", unglossed.
  - **Checked by hand:** Valens reads the board "when Felix had already gone in", so Felix's belief that he cannot read survives.
- **Casual (airport, 10 pages): 9.0.**
  - The opening notice, the leek woman, Grata's paint flood and the coppersmith's alibi goat are company they want to keep.
  - The pebble is where they cry, and the fish jar is where they turn the page.
  - The only drag is the third wall in a row.
  - No vibes problem.
  - Not 9.5: a second long, low-plot chapter running.
- **Devoted (active):** would adopt it.
  - What they find: Ch.2's thumbnail with eyes shut, answered by Zosimus's thumb on a visible join; the first tremor note in Fenn's back leaves; the amazed wall; the I on the crack.
  - What they would catch now: only the skeleton F1 removes.

| Issue | Dev | Crit | Host | Cas | Devoted | Severity |
|---|---|---|---|---|---|---|
| F1: Felix's "twice. Once … once …" (3rd chapter) | | ✓ | | | ✓ | SHOULD FIX (book law; closed shape) |
| F9 third "cry"; F5 pier run; F2/F3 "on his way" ×5 | | ✓ | | | | INVESTIGATE (fix: cheap, tested) |
| F10 trade-residue introduction on 5/5 tradesmen | | ✓ | | | ✓ | INVESTIGATE |
| S5 graffiti stretch | ✓ | | | ✓ | | SHOULD FIX → not changed (structural; the ledger's wall-writing collage; 92 words above the floor) |

**No CRITICAL. No VIBES PROBLEM.**

## Tomorrow Test / Shareability / CVI
- **Tomorrow Test:** unchanged and strong (BOTH types).
  - IMAGE: the toddler's two fingers on the wet pebble, and the stone dried gray. QUOTE: "It's not my fish. It's a child you've got." → +0.5.
- **Shareability:** unchanged ("the landlady figures out she's pregnant from the FISH SAUCE").
- **CVI-Launch: 9.4** (8.9 + 0.5).
- **CVI-Legacy: 7.1**, provisional.
- None of the 41 swaps or the finalize set touches either anchor.

## Pacing check (cycle 1): OK
- **Length:** 7,785 words (7,792 after the finalize set) against an 8,200 target. The range is 7,700–8,700; the chapter is not padded and should not be cut further.
- **Dialogue** 35.2% (band 30–40 ✓); **6 breaks** ✓; **median 16** (mid ✓); `narrative` → `dialogue`.
- **Neighbours:** Ch.19 is `scene-set` → `long-fade` and Ch.18 `I-statement` → `punch`. No signature runs three in a row; `shape_check --strict` is CLEAN.
- **Emotional slot:** belonging → the first unprompted break → a positive revelation.
- **Speed:** documents quick; repairs slow; the fountain sudden.
- **Sag (accepted):** S5.
- **Book:** 115,247 words (115,254 after finalize).

---

## Finalize fixes (word-neutral or additive; tested together)
**11 swaps; net +7 words** (shape_check 7,785 → **7,792**, against the 7,700 floor).
- **Script:** `/tmp/claude-0/-home-user/63791ee5-159c-5791-9429-07920f8d9417/scratchpad/ev20c1/ch20-finalize.py`. Run it as `python3 ch20-finalize.py <in.md> <out.md>`.
  - The input must be the cycle-1 page (md5 `d650c6c5…`).
  - Each OLD string must occur exactly once, or the script aborts.
  - The header comments are untouched.
- **Tested output:** `/tmp/claude-0/-home-user/63791ee5-159c-5791-9429-07920f8d9417/scratchpad/ev20c1/ch20-final.md`, md5 `20bcc76c76ff17a127421c369cc3f273`, sha256 `24fd5686d3feb75dceabd68c8c4fa8a37770bc30dc512d02bf5d1561326b8886`.

| # | Line (cycle-1 page) | Type | Now | Why | Swap (exact) |
|---|---|---|---|---|---|
| **F1** | l.373 | Character (closed shape, 3rd chapter) | "He went up twice. Once to wrap her and once to see had he wrapped her right." | Kallia's Ch.7 "Twice. Once on… and once in…" skeleton (the one C2 closed on the turner), also used in the Ch.8 narration. | → "He went up and wrapped her, and he was no sooner down than up to see had he wrapped her right." (Felix's run-on; the speech still ends on his boast) |
| F2 | l.425 | Style (frame ×5) | "Valens came by us with the string on his way to the yard," | "on his way" ×5; the book's maximum elsewhere is 2. | → "Valens came by us with the string, going out to the yard," |
| F2b | l.433 | Style (frame ×5) | "by her son on his way to bathe," | as F2 | → "by her son as he set off to bathe," |
| F3 | l.95 | Style (frame ×5) | "The cook stopped at my plank with it on his way home." | as F2 | → "…with it as he went home." ("on his way" ends at 2: Valens l.41 and Zosimus l.561) |
| F4 | l.375 | Style (parallel) | "the rain found a cracked tile over the bed and came through onto Valens's foot." | The sun "found a line" 30 lines earlier, in the same shape. | → "the rain got in at a cracked tile over the bed and fell onto Valens's foot." |
| F5 | l.453 | Style (swap R9b, density) | "Highest of all on the pier there was one more." | "pier" ×5 in 25 lines. | → "Higher than any of them there was one more." |
| F6 | l.547 | Style (in-paragraph double) | "I warmed the pieces and joined the shoulder" | "I warmed the knife" follows two sentences later. | → "I heated the pieces and joined the shoulder" |
| F7 | l.395 | Style (double) | "my wife thinks I'm at the bakery kneading," | It shares "at the bakery" with the dyer's alibi (l.501, protected). | → "my wife thinks I'm at the mill with the donkeys," (Pompeian bakeries milled with donkeys) |
| F8 | l.27 | Style (cross-chapter 3-gram) | "Them that paint the candidates live" | Mara's Ch.15 "paint the candidates' names". | → "Them that paint for the candidates live" |
| F9 | l.499 | Style (swap R5) | "From his father's hip the boy watched me cry." | A third "cry" in eight lines, restating "I was crying." | → "From his father's hip the boy watched me and sucked his cord." (the cord of l.487's crescent; no feeling named) |
| F10 | l.387 | Character (swap R12; device) | "a thin fellow with red to the wrists sat with his pots in a row," | The third arm marker (with the coppersmith's forearms and Zosimus's elbows). | → "a thin fellow sat with his pots of red in a row," (Felix's "All that red" still pays) |

**Results with the copy swapped into the manuscript path, run from /home/user/Books:**
- **`check_chapter.sh 20`: all clean.**
  - style: 7,818 words, simile 1.4/1k, em-dash 0, foreshadow 0;
  - grammar 0; rhythm 0;
  - show/tell: 7,821 words, **35.2%**, no flags;
  - voice-wear strict: clean;
  - tic gate: clean (and-chains 2/9, credential 1);
  - echo 0; command echoes none; spoken-line echoes none;
  - metaphor 1.8/1k, median 15.
- **`tic_report.py --gate`:** clean (exit 0).
- **`--echoes 20`:** none / none / none.
- **`shape_check --strict`:** `20 7792 6 35 16 narrative dialogue`, CLEAN (exit 0).
- **`voice_wear_check.py`:** clean (exit 0).
- **Restored:** md5 `d650c6c57f4d671f62976c2276fb14c7`, verified after every run. **I did not edit the manuscript.**

**Reuse checks on every replacement string:**
- a 3–7-gram scan against Ch.1–19, all 13 samples, and the rest of the chapter;
- a whole-spoken-line scan;
- the rule that no repeat moves sideways.

**Result:**
- no 4+-gram anywhere;
- no sample string;
- the only 3-gram match is "the yard and" in F2's sentence, which is already on the cycle-1 page.

**After the set, in the chapter:**
- "on his way" 2; "pier" 10; "warmed" 3; "cry/crying" 2; "at the bakery" 1; "twice" 5 (within the book's range of 0–7);
- "found" 12, with the weather finding a flaw once.

**Replacement strings rejected during testing** (so the editor does not reach for them):
- "and went back to see": the tic gate fails "and went back" ×3 (Ch.1, 14, 20);
- "went back up to see": the tic gate fails "back up to" ×3 (Ch.5, 15, 20);
- "a second time": sample-11 and Ch.7;
- "up again to see": "wrapped it up again" (l.347) in the same section;
- "when he came in from the mules": it doubles "Felix came in from the string" eight lines earlier;
- "the rain came in through": it rebuilds the sun's "came in sideways" one verb over;
- "his cord in his mouth": "in his mouth" would be in its 7th chapter;
- "at the baker's": Grata's spoken Ch.19 3-gram;
- "red spattered down his tunic": "tunic" ×2 with "dried his fingers on his tunic".

**A first test run failed the tic gate on my own F1 string** while `check_chapter.sh` exited 0. See the pipeline note below.

---

## Character-bible Ch.20 re-sync (orchestrator; apply with the finalize set)
**The Ch.20 blocks still quote the writer draft.** Run against the finalize page, a script finds **24 quoted strings no longer on the page**.

Re-sync each block to md5 `20bcc76c…` and mark it "SYNCED to the FINAL page", as Ch.19's blocks are. Each item lists the draft string, then the page string.

**1. At-risk after Ch.20 (l.5448–5501):**
- **Lamp:**
  - Delete "Nobody at home had ever paid me to leave a join where it could be found." The disruptor cut it. Log it as a CUT entry, never to be restored.
  - Add the page's process: "I heated the pieces and joined the shoulder, and when the welt swelled from the break I let it stand." (R14, F6); "Round the filling hole the clay was black from his thumb." (R8).
  - Zosimus "cradled the lamp in his palm and shut his eyes".
  - "Valens walked in while the lamp was still on my plank" (D7).
- **Fountain:**
  - Delete "the jar running over" and the next woman (R2).
  - "I put out my hand." → "I turned my hand up." (R3).
  - "I could not stop." → "From his father's hip the boy watched me and sucked his cord." (R5, F9).
  - "I filled the jar at the spout and carried it home." (L3).
  - "He looked at it by the lamp, small and dry and gray, and passed it back to me" (C5).
  - "his father insisted," (D2).
- **Tremor note:** "the bed walked an inch on its legs" → "the bed walked on its legs" (D4).
- **Named frame:** add "Through the lens the heat off the tiles kept him and his tree wavering, and the waver never settled." (R13; there is no left/right layout).
- **Fig:**
  - Delete ("Today," … "Not tomorrow. Tomorrow the wasps have them."); log it as CUT (C1).
  - The picking day is silent: "put them on my plank among the broken things." / "I ate all three."
  - Mara's "In this rain." (R7).
  - Felix's "He went up and wrapped her, and he was no sooner down than up to see had he wrapped her right." (F1).
  - The drip: "the rain got in at a cracked tile over the bed and fell onto Valens's foot." (F4).
- **Teeth:**
  - "It found the gap beside my sixth-grade filling" (L1);
  - "tooth by tooth." with the carts cut (R1);
  - keep "Then I'll keep to the other." (write it as the page has it, not "keep[s]").
- **Grata:**
  - "you've the face of a payer" → "you've a payer's face" (R18);
  - "Them that paint for the candidates" (F8);
  - "It stood at her counter's brazier end" (R19);
  - "ladle some onto a carter's bread" (L2).
- **Wall-writing set:**
  - "Someone had answered it in a deeper hand:" (D3);
  - "to read him the pier at its back" (R9a);
  - "Higher than any of them there was one more." (F5);
  - "from the eaves halfway to the paving" (R16).
- **Felix line:** "That wants shouting." (not "Then they'll want it shouted.").
- **Spoken shapes spent:**
  - Replace:
    - "Then they'll want it shouted." → "That wants shouting.";
    - "Make it hold. I cook in it." → "Make it tight. My oil lives in it.";
    - "It will hold anything you put in it." → "Anything you put in it.".
  - Add:
    - "What's she sent?" / "Grata's olives." / "That's yesterday's bread." / "Grata says it is today's.";
    - "Which are the dogs?" / "These. Lead. They've not shifted since.";
    - "I'd only break it in the same spot, looking for it.";
    - "In this rain.";
    - "The furnace man at the baths.";
    - "It buried my wife's mother," … "and after her a horse.";
    - "He should have chained it to the wall." (the husband's line, not "Then he should…").
- **Counts → FINAL:**
  - 7,792 words (shape_check), 7,818 style, 7,821 show_tell; dialogue 35.2%; median 16; 6 breaks; `narrative` → `dialogue`;
  - "Somebody had [verb]" 0, "Someone had" 1;
  - race frame before-X **0** ("before he was over the sill" is not on the page);
  - payments 3; "on his way" 2; "dusk" 3; tool-tip frames 2; #11 3 firm (0.39/1k);
  - anti-AI 7/20 (−0.875); echoes none / none / none.

**2. ZOSIMUS card (l.3908–3940):**
- **Physicality:** "at the pickup he hugs the lamp to his breastbone" → "at the pickup he cradles the lamp in his palm, shuts his eyes, and finds the welt with his thumb". "with one black finger" stays (once). "scratches in his beard" stays, with no black finger.
- **Ch.20 as written:**
  - "Dropped it on the furnace stair," → "The furnace stair did it,";
  - "on its foot a maker's name stamped in tall capitals: FORTIS" → "It was a plain round lamp with FORTIS stamped in tall capitals on its foot.";
  - "I've had it since before the earthquake." → "I've had it three summers.";
  - the name "for the tag, Zosimus, of the baths" → "Zosimus. Of the crossing baths. Down at the furnace, not up with the bathers.";
  - the pickup is "Zosimus was back two mornings later, on his way down to light the furnaces. It was still dim in the shop.";
  - **no payment beat** (C4c); the exit is unchanged.
- **Mark SPENT:** "three summers"; "The furnace stair did it".
- The sample line stays (calibration only).

**3. GRATA (l.2162):**
- Add the touches as on the page: the hen-squeeze on the upper arm; the forearm push "the way she moved customers along her counter"; two fingertips on the inside of the wrist "beside Plautia's gold".
- Add "you've a payer's face".
- Add the fish jar "at her counter's brazier end", ladled onto a carter's bread.
- The cup is set down without a word.
- Questions still 0. Ch.21 finds a fourth touch.

**4. Ch.20 walk-ons (l.3166–3205):** mark the block SYNCED, then apply:
- **The leek woman's husband:** "He should have chained it to the wall." (his line; her reply "He should have chained you.").
- **The coppersmith:** "Two winters back" → "This winter gone. Good rivets."
- **The stewpot woman:** "She had a tinker put his dogs in it the winter I was born. Do it the same." / "Which are the dogs?" / "These. Lead. They've not shifted since." / "I'd only break it in the same spot, looking for it." / "Make it tight. My oil lives in it."
- **The bone-turner:**
  - "a small man with a curl of bone caught in his hair" (R12);
  - "It buried my wife's mother," … "and after her a horse." (C2);
  - collected "that evening" (C7);
  - pays in the toothpick only; the dice are cut (C4b).
  - The box returns: "Full again in under a month," … "Don't tell my wife it was full."
- **The fuller's wife:** "She called for it while Grata was at the baths." (R10); "She wrapped it up again in the same wool." (C4a); "Twice he's had it from the shelf to look at, and back it goes." (the line's "Twice" opener is not a reply).
- **The night crew:**
  - the painter is "a thin fellow sat with his pots of red in a row" (F10; there is no "red to the wrists");
  - the whitewasher's "Four, and my wife thinks I'm at the mill with the donkeys" (F7);
  - **Felix sits among the painter's pots and holds nothing** (continuity C-03).
- **The toddler's father:** "a man whose hands were stained blue from somebody's vats" (not "arms blue to the elbow"); "his father insisted," (D2). The boy "sucked his cord" (F9).
- **The carter at the fish jar:** "pushed his bread across for more of it" (L2).
- **Unchanged:** the cook, the clay-pig girl, the quarrymen, the foreman, the tile carter, the fountain line, the oil man.

**5. Principal cards' Ch.20 lines:**
- **VALENS (l.1147):** "the fig pinched, wrapped and picked ("Today," … "Not tomorrow.")" → "the fig pinched, wrapped, and picked in silence (three figs on her plank among the broken things)". Add "What's she sent?" … "Grata would."
- **FELIX (l.1817):**
  - "holds the painters' ladder" → "sits among the painter's pots, holding nothing (C-03)";
  - add his rain line (F1);
  - "That wants shouting.".

**6. New SPENT / CLOSED / WATCH entries** (add to "At-risk after Ch.20"):
- **"Twice" as a whole reply:** CLOSED. **The "[N] twice. Once … and once …" skeleton:** CLOSED, having been used in Ch.7 (Kallia) and Ch.8 (narration). Both Ch.20 instances are cut (C2 and F1).
- **1–2-word whole lines in the same mouth across chapters:** 0. "Today,", "Not tomorrow." and "What's in it?" are Valens's spent lines.
- **Payment-in-kind as a scene close:** CLOSED after Ch.20 (3 on the page).
- **"came for it" as a pickup:** CLOSED (sample-11).
- **Tradesman arm markers:** ≤2 per chapter. **A walk-on introduced by his trade's residue on his body:** ≤1 per chapter in Ch.21–25 (Ch.20 has 4 after F10: forearms, hair, hands, elbows).
- **Weather that "finds" a flaw:** SPENT at 1 (the sun's line on the bottle).
- **"on his way":** ≤2 per chapter.
- **Tool-tip frames:** ≤2 per chapter. **Camera left/right layout:** CLOSED. **A public-spout freeze** (Ch.14, Ch.20): SPENT.
- **sample-07's "I put my hand out" / "My hand went…":** 0 before Ch.42, at any length.
- **No line in Ch.21–24 links the fountain to the pregnancy** (audit I-03).
- **CUT entries** (never to be restored): the disruptor's "Nobody at home had ever paid me…"; C1's fig line; R2's spill; R1's carts.

**7. Ch.31 forward guard** (add under "At-risk after Ch.20", and as a writer warning in outline Ch.31). Ch.31's reserved anchor is Grata whitewashing a rival's election notice by lamplight with Mara holding the ladder. Ch.20 has spent the generic night-crew tableau (a ladder, a boy with a lamp on a pole, lime over red, the real graffito *Lantern-boy, hold the ladder.*). So Ch.31:
- stages the raid by **Grata's own lamp**, on a **rival's red letters**, with **Mara's hands on the ladder**;
- puts **no professional crew** on the page and **no lamp on a pole**;
- has **no "hold the ladder"** in any mouth or on any wall;
- makes **no comparison of the wall to a shaved face**;
- sets **no letter on a crack**;
- quotes **no wall in Ch.20's kinds**.

**Pipeline note (UPDATE RULE; for the orchestrator, not done here):** `check_chapter.sh` pipes every gate through `grep`/`sed`, so **its exit status is 0 even when a gate prints FAIL**. My first F1 draft produced "5a … RESULT: FAIL — 2 recurring phrase(s)", and the suite still exited 0.
- **Fix:** have the suite collect each gate's own status (or grep its output for `RESULT: FAIL`) and exit non-zero.
- **Where:** in `books/_template/tools/check_chapter.sh` and in this book's copy.
- **Until then:** read the RESULT lines, not the exit code.

## VERDICT (cycle 1)
**PASS.** Genesis Floor **8.5** ≥ 8.5 · Casual **9.0** ≥ 8.5 · pacing **OK** · all mechanical gates clean.

| Measure | Result |
|---|---|
| Scores | Originality 9.0 · Theme 9.0 · Characters 8.5 · **Prose 8.5** (+0.5) · Pacing 8.5 · Emotion 9.0 · Immersion 9.0 |
| Floor / Average | **8.5 / 8.79** |
| Casual | **9.0** |
| CVI-Launch / CVI-Legacy | 9.4 / 7.1 (provisional) |
| Words / dialogue | 7,785 / 35.2% (7,792 / 35.2% after finalize) |
| Anti-AI | 7/20, −0.875 (clean) |
| CP3-3 / END-1 / "seam" ruling / foreshadowing | ✓ / ✓ / ✓ / 0 |

**Before the finalize commit:**
1. Apply `ch20-finalize.py` (all 11 swaps; they were tested as one set) and confirm md5 `20bcc76c…`.
2. Re-run `check_chapter.sh 20` and read every RESULT line, not the exit code.
3. Apply the bible re-sync above.

F1 is the book-law item: a closed shape in its 3rd chapter. The other ten are cheap doubles. None changes a score. They are what keeps 8.5 honest.

**BIAS CHECK:** This evaluation was produced by the same system that wrote the prose. Confidence in scores above 8.0 requires external validation (beta readers, editors, comp analysis). The PASS rests on Prose reaching 8.5 once the reuse cluster is gone; a human editor may weigh the S5 sag and the montage's light romance load more heavily than I do.
