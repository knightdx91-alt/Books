# Evaluation: Chapter 12 — The Kirrha Road (run 2)
**Evaluator:** book-evaluator (independent; did not write or revise this prose) | **Date:** 2026-10-20
**Text evaluated:** `manuscript/chapters/chapter-12.md` after writer → dialogue-polish → hook-craft → disruptor → continuity repair (C-01, W-01…W-21, W-23). **4,912 prose words** (shape_check), 4,923 (style_check), 5,100 (`wc -w`, incl. header). Target 5,600; the scene budget's own range is 5,000–6,200.
**Read against:** book CLAUDE.md hard gates; STATE.yaml (guardrails, NO FORESHADOWING, NO TICS incl. gestures, retired reflexes, AUTHOR-CP2-1…4); outline Ledger row 12 and `## Chapter 12`; voice-dna §0, §1 (voice under pressure, level 2 at Ch.12), §3b, §4 (allowlist); character-bible.md (Valens/Mara/Felix cards; every at-risk block from "after Ch.1" to "after Ch.12"; the at-risk table; NO TICS); voice-bank samples 05 (the Ch.12 register) and 08, plus all 13 by n-gram; chapter-11-eval.md (cycle 0 + cycle 1); chapters 10 and 11 for pacing; ENTITY/continuity `chapter-12-audit.md`; the dialogue, hook and disruption reports.
**Genre profile:** commercial historical romance / time-slip, comp *Outlander*. Anti-AI band: commercial (0–8 clean, 9–11 watch). Engagement: empathy 55 / fascination 30 / self-insertion 15. Dimension 7 = **IMMERSION**.

**Measured here (not from any report):** `bash books/the-hour-of-ash/tools/check_chapter.sh 12` is **clean on every gate**.
- Style: simile 1.0/1k, adverb 1.0/1k, em-dash 0, foreshadow 0.
- Grammar 0; rhythm 0; show/tell no flags (dialogue 27.2%); voice-wear strict clean; tic gate clean (and-chains 5/9, credential asides 0, negation pivots 0 by regex, "So" 0); echo scan 0; command echo none.
- Metaphor: fig 1.8/1k, median sentence 10.
- `shape_check --strict`: CLEAN. Ch.12 = `dialogue` → `punch`, 2 breaks, dialogue 27%, median 10. Book 64,823 words over 12 chapters vs 69,600 cumulative target (−6.9%).

**My own scans (scratch, not gates):**
- A 3/4/5-gram scan of Ch.12 against Ch.1–11 and all 13 samples, both raw and pronoun/possessive-normalized: 20 raw 3-gram hits, 33 normalized. Each hit was checked in context.
- Targeted greps for every spent or at-risk item in the bible.
- A count of paragraph-final negations and of anadiplosis across all 12 chapters.
- A structural read against sample-05 and Ch.5's grab-and-beating scene.
- **Every fix in the PATH below was applied together to a scratch copy of the book folder and run through the real `check_chapter.sh 12` and `shape_check --strict`:** all clean, echo 0, and no new n-gram hit against Ch.1–11 or the samples. I did not touch the manuscript.

*(¶N = line number in `chapter-12.md`, as in the Ch.5–11 evaluations.)*

---

## HEADLINE
**CVI-Launch (CVI-L):** 9.7 (9.2 base + 0.5 strong anchor) | **CVI-Legacy:** 6.6 (provisional) | **Genesis Floor:** **7.5** | **Genesis Average:** **8.57**
**Casual Reader:** **9.0**
**Engagement type:** Empathy primary (the hero falls apart after the killing and she holds his hands). Fascination secondary (the frame-up told as a legal chronology: rudis, dowry retention, a backdated bill of sale). Self-insertion tertiary (she saves him a little).
**Divergence alert: YES (9.7 − 7.5 = 2.2).** *Commercially potent; craft held by the narrator's habits, not by the reader experience.* The floor comes from a density cap on one AI pattern (#11, explanatory extension, 0.81/1k against a 0.8 limit) and from a cluster of reused frames that the gates cannot see. The fight, the shaking, the telling and the ending do not need changing.

**Gate (Floor ≥ 8.5 AND Casual ≥ 8.5 AND pacing OK AND gates clean): NOT MET.** Casual 9.0 ✓, pacing OK ✓, gates clean ✓. **One dimension holds the floor: Prose & Voice at 7.5** (capped).
- **#11 is over the commercial density cap.** Four explanatory extensions in 4.9k words: two in the camera paragraphs that a repair added to, and the cold-water and filter clauses. Two subtractive cuts clear it.
- **Narrator recurrence, the same cycle-0 cause as Ch.1–11.** It takes three forms:
  - Frames lifted from earlier chapters and from this chapter's own register sample (sample-05). The worst: Mara seized from behind in Ch.5's exact sentence frame ("A hand took…").
  - The prior run's struck knot device, back in Valens's hands with a barometer sentence ("His hands were sure at it.").
  - Four bible items that are SPENT by name.
- **Every fix is a cut or a clause swap,** and all were tested together. No scene, beat, first line or last line moves.

---

## Genesis Score (Craft Assessment)

| Dimension | Score | Evidence | Cap reasons / holds |
|---|---|---|---|
| Originality | 8.5 | **The genre beat is subverted on the page.** The outline's beat is "the hero saves the heroine and she melts"; on the page, he kills a man and then cannot stop shaking, and "the romance is in her steady hands". The inventions are the writer's own: (1) **the friendly gambler** who forgives his lost bet ("I had two drachmas on the Gaul." He laughed. "I've forgiven you." ¶16); (2) "My brother's a butcher. He's got two like that." (¶28); (3) **the camera swung on its strap and the cap rolling on its rim into the oil** (¶56–¶64); (4) **"Who gets his knife?"** from a boy who has just been sick (¶86); (5) **two versions of one fight**: the stranger's "the emperor rose in his box to see it finished" (¶16) against Valens's "The emperor never got out of his chair." (¶180); (6) Celer's **backdated bill of sale** ("so the lanista had no right to free me, and the magistrate had written down a mistake", ¶200); (7) **the cover story drilled and then embroidered**: "I could have the sword." / "That's nothing to tell." / "Tell it anyway." (¶260–¶266); (8) the dead man's silver "to the god" (¶272–¶278); (9) **Spicula**, "After the murmillo. The one the emperor gave a house to." (¶312); (10) a new sandal "with the thong tied in a bow across the foot. The foot was turned out." (¶82). | **Held at 8.5, not 9.0.** Several frames are borrowed: Ch.5's grab sentence (P2); the Ch.7 darn and the Ch.5 crease-and-nail scrub (P5f, P5g); four sample-05 strings (P6). The spine is also the comp's own: the hero tells his flogging and false accusation in an intimate moment of care, which is *Outlander*'s Jamie telling Claire about Randall while she tends his back. The subversion is real; the spine is genre. |
| Theme | 8.5 | **"The stories other people own about you" is carried by structure:** one event, many versions, none pointed at. The stranger's arena story against Valens's; Celer's story ("His story was that…", ¶200); the robbery Valens authors ("That's what it was. A traveler with his purse cut.", ¶108); Felix's invented sword; the graybeard who "had settled on robbers" (¶300); the women's version ("how new they were, what a shame", ¶294); and Mara's "I am not telling Kallia a story. She gets the whole of it from me, or nothing." (¶360). The subtext is the outline's: she asks no question in the whole chapter (every "?" belongs to someone else), and that is how she believes him. **Texture that means nothing:** the bird "saying the same three notes" (¶66); the sprats in fig leaf (¶244); the lamp seller (¶336); the goat asleep with "her jaw kept moving" (¶366). | **Held at 8.5.** The theme sits one word from the surface: "story" is in Mara's mouth (¶360), and "That's nothing to tell." / "Tell it anyway." (¶264–¶266) are close to a statement. In the ford section nearly every exchange is a version of the event; the texture above keeps it out of #18. The best-executed theme in the book so far. |
| Characters | 8.5 | **Valens** is whole and true to his card. Fast and unseen in the fight ("The ditch hid them. I heard them." ¶46). Practical after it ("Are you cut?", the purse cut to stage a robbery). He falls apart at the fall (¶134–¶152). The telling is a witness's chronology without self-pity: "I was a good bodyguard. That was the use of me." (¶188), the outline's line used once. His first "Mara." is a warning, untagged, from the ditch (¶52). He plans and does not ask: "I'll stay up the summer." (¶352). **Felix:** sick "neatly" against the wall; "It was that crust … It was off."; the sword he wants to have had; Spicula; carrying the goat because she will not walk. Speed and questions, and no catchphrase. **Walk-ons are people:** the talker's "pleasant face" is still pleasant dead (¶94); the big man and his butcher brother; the third man ("Wine. Sweat."); the graybeard ("and it won't be me", ¶296). **Cover-the-name: PASS** for all speakers. **Counts:** Valens's bare "No." 1 (¶332); bare "Felix." 0; walk-offs after a line 2 (¶112, ¶234; cap 3); narrated non-answers 0; Felix's "already" 0; tag-and-exit 0. | **Held at 8.5 (no cap).** WATCH: (a) **the struck knot device's function**: Valens "tried the knots. His hands were sure at it." (¶268), right after the shaking. Charged under Prose (P3), as Ch.11 charged its knot; it would cap Characters if it recurred. (b) The "He" at ¶268 is ambiguous (the nearest narrated "he" is Felix). (c) Hand-offs ×4 (pouch, cloak, pouch back, purse). (d) Felix's "Is…?" openers ×3 plus Valens's "Is it broken?". Mara's chaos is 2–3/4 (below), which is sufficient for the commercial profile. |
| **Prose & Voice** | **7.5** | **Stopping sentences:** "**In the ditch somebody was breathing hard, and then nobody was.**" (¶68); **the cap sentence** (¶64), 66 words of sight narrowing to one rolling object; "**It was still a pleasant face.**" (¶94); "**It was snow water, and my feet stopped belonging to me.**" (¶144); "**There was a knife in his hand, and it was not his own.**" (¶74); "**They'd been shown where to stand.**" (¶192); "**Somebody's hair was wound into the little crank on top**" (¶160). **Underlines:** "Wine. Sweat."; "He looked for blood on me regardless."; "picked a sliver of pot out of the hair there and threw it after the man"; "Cold water. Hot would have set it."; "said good evening and got good evening back"; "if the Calf-Bearer had been twelve and in a temper"; "Its edge found me as I walked."; "her jaw kept moving". **Ugly sentence:** "The oil had got onto that one." / "one slapping and one not" (¶116). **Voice under pressure, level 2, demonstrated:** the asides die from ¶40 to ¶122, and the prose is bodies, hands and sound. They come back at the stream in order: materials, then comparison, then the Orestes aside. | **CAPPED at 7.5: #11 over the commercial density cap** (4 at 0.81/1k against >0.8/1k; Ch.10 cycle-1 precedent). **Without the cap it holds at 8.0** for P2–P7: frames from Ch.4, 5, 7, 9, 10 and 11, from sample-05, and from the bible's SPENT list, plus in-chapter frame doubling. Anti-AI 10/20, −1.625 (watch band). |
| Pacing | 9.0 | **Ledger row hit on every hard field.** In medias res between Ch.11's Chronological and Ch.13's Parallel ✓. *Violence first, story after* ✓. Open `dialogue` ("Lupus? By the Twins, it is.") ✓. Close `punch`: "A cart had stopped beside the ditch." (7 words, a one-sentence closing paragraph, allowed for Ch.12) ✓. 2 breaks ✓. Dialogue 27% (25–35) ✓. **Gear low, median 10** ✓: the book's first drop to low since Ch.4, as planned after two mid chapters. **Speed design:** the fight is fast (~350 words of violence inside ~800); the road is plain; the stream is slow; the telling is flat and broken by work; the ford is brisk; the climb is measured; the last image is far away and still. **Value shift:** Mara and Valens go from a bought goat and a plan (+) to a killing and the knowledge that Celer wants him dead (−). They end with the money closed, a deeper trust and the plan kept under threat (±). **Pull 8:** the body has been found and the headman's version has started; three days to the god. | **≥9.0 challenge:** a fight-to-aftermath arc in 4.9k words with no slack in the first 2,000 would sit beside *Outlander*'s action chapters and be tighter than most. Not higher: (a) **length** is 12% under target and below the scene budget's own 5,000 floor (no per-chapter floor; do not pad); (b) the Kirrha-morning backfill at the ford (¶240–¶244) decelerates straight after the telling, and the Devourer skims it. |
| Emotion | 9.0 | **Anchor lands** (outline's, executed): the camera swung "at his head", then the cap "rolling along the road on its rim, small and black, wobbling and righting itself over the ruts with the white letters on its face going under and coming up again … until it met the edge of the oil and tipped over in it" (¶56–¶64). **Surprise lands:** "They were shaking." (¶138). He hides his hands; she wades in and holds his wrists flat to the stone "and I did not speak" (¶144–¶146); "He let his forehead come to rest on my hair. He stayed there." (¶150). **Body rebel:** his shaking; her feet "stopped belonging to me"; "I could not make myself look toward the ditch again" (¶114); Felix's stomach, lied about. **Techniques ≥6:** physical sensation; object proxy (the camera clutched, the strap wound "until there was no strap left", the bow on the dead man's sandal); dramatic irony ("Did he go down straight off?" / "No." against Ch.11's one-blow lie); humor in shock ("Who gets his knife?", "It was that crust", Spicula); silence (no question asked); a distanced image (the cart). The peak is not a laugh ✓. | **≥9.0:** a senior editor would accept it beside *Outlander*'s aftermath scenes; the reversal of who comforts whom is better than the comp's. Not 9.5: the steadying of shaking hands is the stock comfort beat (sample-05 itself ends on it), and Mara's own feeling is held almost entirely in objects. That is right, but it limits the peak. |
| **Immersion** (Dim 7) | 9.0 | The Kirrha mole: goats "in a pen of hurdles at the root of the mole", boats "with the new pitch still soft on their seams", sprats "in twists of fig leaf". Oil jars packed in straw, and a stone of a jar's weight for ballast. Vespasian's "heavy face" on new denarii. *Rudiarius* unglossed. Retention of dowry for adultery ("you keep a share of what she brought"). Isis at Kenchreai "on her days". The Craneion as "out where the cypresses are". The freedom of Achaea and the legate's lapsed post. Spiculus the murmillo (Suetonius, *Nero* 30). The bare sacred plain under Delphi. Plane buds "just broken", snow water, the rewind crank and the dented filter ring of a K1000. | **Held at 9.0.** #15 minor: the telling's chronology is complete and certain. Trace: "Corinthian bronze" (¶272) is also the name of a luxury alloy, which a conservator would hear (optional O2). |
| **FLOOR** | **7.5** | Prose & Voice (capped) | |
| **AVERAGE** | **8.57** | (8.5 × 3 + 7.5 + 9.0 × 3) / 7 = 60.0 / 7 | |

**Trajectory vs Ch.1–11 (finals 8.50–8.64; cycle 0s 8.0, Ch.10 re-eval 7.5):** this is the twelfth cycle 0 held by narrator recurrence, and the second (after Ch.10) held by the #11 density cap in a short chapter. Two of the four #11 instances, and the knot, came from repairs: continuity W-20 option (a) added the sailor clause, and W-13's "tried the knots" carried the writer's "His hands were sure at it." along with it. The fault is the agent passes, not the draft.

---

## CVI-Launch Breakdown
| Input | Score | Evidence |
|---|---|---|
| Commercial Pacing | 9/10 | A stranger who knows the hero's secret name in line 1; a knife by ¶38; a death by ¶68; the hero's past told by ¶208; a body found at the last line. A non-reader finishes it. Loses 1 for the ford backfill and the money handling (¶240–¶278). |
| Tomorrow Test | 8 anchors → 10 | IMAGE: the cap rolling on its rim into the oil; his hands shaking under the fall and hers holding them; the new sandal tied in a bow, the foot turned out; Felix carrying the goat across his shoulders, the goat asleep and still chewing; the cart stopped beside the ditch, far below. QUOTE: "and then nobody was"; "Who gets his knife?"; "I was a good bodyguard. That was the use of me." |
| Casual Reader | 9.0/10 | See report. |
| Shareability (quote / plot / emotional) | 4 / 4 / 4 → 8 / 8 / 8 → **8.0** | Quote: "That was the use of me."; "Who gets his knife?". Plot: "she hits a hired killer with her dead father's camera". Emotional: "the gladiator kills a man and then can't stop shaking, and she holds his hands under a waterfall". MAX 8 × .6 + AVG 8 × .4 = 8.0. |
| Concept Pitch | yes → 10 | |
| Human Closeness | yes → 10 | The steadying and the telling are the chapter's core. |
| **CVI-Launch** | **9.2 + 0.5 = 9.7** | 9 × .2 + 10 × .2 + 9 × .2 + 8 × .2 + 10 × .1 + 10 × .1 = 9.2. A one-chapter formula; see BIAS CHECK. |

**CVI-L note.** In this project's STATE.yaml, "CVI-L" is **CVI-Launch: 9.7** (Ch.11 9.5; this is the book's highest). It is high because the chapter is the first true crucible: violence, a reversal, a secret told and a body. Expect it to settle around 9.5 after polish (the PATH changes no anchor). **CVI-Legacy (default weights; provisional):** Originality 8.5 × .30 + Theme 8.5 × .25 + Cultural Vocabulary 2 × .20 + Re-readability 7 × .15 + Identity 5 × .10 = **6.6**, unchanged from Ch.11. Re-read rewards:
- the stranger's emperor rises, Valens's emperor never moves;
- "Celer kept the boy." (Marcus, Ch.16);
- "When he was away I slept across her door." before Ch.14's doorway;
- the strap wound "until there was no strap left" against Emilio's strap in Ch.1;
- Ch.11's "On its feet" goat carried up on a boy's shoulders;
- "Did he go down straight off?" / "No." against Ch.11's "Have you ever seen a man killed with one blow?" / "No."

---

## Anti-AI Scan (20 patterns; density per 1,000 words at 4.91k; commercial band)
| # | Pattern | Result | Count / density | Citation |
|---|---|---|---|---|
| 1 | Forced symmetry | FOUND minor | 2 (0.41) | ¶174 "the left with the right and then the right with the left"; ¶152 / ¶230 "he plainly knew nothing about it" / "and it stung, now that I knew about it" (his unnoticed graze, her unnoticed welt, in mirrored words). **−0.125** |
| 2 | Empty poetic vocabulary | Clear | 0 | |
| 3 | Automatic rule of three | FOUND moderate | 4 (0.81) | ¶96 three orders to Felix; ¶188 "To the baths. To her mother's house. Out to Kenchreai…"; ¶162 "Thessalians and Achaeans and a priest's cousin from Elateia"; ¶272 "It would buy the cake, and Praxias's drachma, and leave plenty over." **−0.25** |
| 4 | Em dashes | Clear | 0 | |
| 5 | Empty metaphors | Clear | 0 | "fell in a rope" and the horse-bettor's look both characterize. |
| 6 | Dramatic "And" openings | Clear | narration 0 | Speech 3 ("And good day to you, lady," "And here's the hand." "And still came to the yard."), under the cap of 4. |
| 7 | Pseudo-philosophical closings | Trace | — | The Orestes line (¶278) is mid-paragraph and specific; the purse sinking follows it. |
| 8 | Excessive parallelism | FOUND minor | — | **Anadiplosis ×3:** ¶82 "across the foot. The foot was turned out."; ¶130 "into a pool. The pool was clear to the bottom, and the bottom was pale gravel." Also "past …, past …" (¶64), "I saw … I saw" (¶40), "I held on … I held on" (¶146). **−0.125** |
| 9 | Overly smooth transitions | Clear | hinge 0 | |
| 10 | Described emotions | FOUND minor | 2 (0.41) | "He sounded surprised." (¶298); "His voice was coming back." (¶260). **−0.125** |
| 11 | **Explanatory extension** | **FOUND moderate, OVER THE CAP** | **4 (0.81/1k > 0.8)** | ¶160 "it was pushed in at one point, **and no filter would screw onto it now**"; ¶162 "The camera was the thing in that bag a thief would take first, and the thing I could least explain to anybody who took it, so…"; ¶162 "**a black disc with letters no one at Kirrha would read as a word was a thing a sailor might have dropped off any boat**"; ¶170 "Cold water. **Hot would have set it.**" Borderline, not counted: ¶268 "so that she would carry level"; ¶230 "now that I knew about it". **−0.25 and Prose capped at 7.5.** |
| 12 | Binary negation | FOUND minor | 2 (0.41) | ¶140 "**The shaking was not small.** It started in his shoulders…" (the "was not X." pivot, SPENT by hand-check); speech ¶224 "He doesn't want me back. He wants me in a ditch." (the outline's content). **−0.125** |
| 13 | Precision flex | FOUND minor | — | "six mules", "the same three notes", "twice" ×2, "five years", "Two years", "a hundred men". Mostly natural. **−0.125** |
| 14 | Emotional control demonstration | Clear | — | Control fails and is not reported as managed ("I could not make myself look … and did not try."). |
| 15 | Authoritative description | FOUND minor | — | The telling is complete and certain. Offsets: "The ditch hid them. I heard them."; "I had missed it on the road"; "I was watching something else". **−0.125** |
| 16 | Philosophical asides | FOUND minor | 1 (0.20) | ¶278 "Apollo had been taking money from men with blood on them since Orestes, and had never been known to send any back." (kept: a wry, specific line). Speech: "Whoever wants five hundred brings a rope." (worldview). **−0.125** |
| 17 | Clean dialogue | FOUND moderate | — | The knowledge-path exchange (¶208–¶224) is strict, precisely responsive alternation. Offsets: Felix's stacks; "Quick, though?" / "I was watching something else."; the graybeard talking past them. **−0.25** |
| 18 | Thematic echo chamber | Clear (watch) | — | Texture is present (above). |
| 19 | Graduated reveal | Clear | — | Violence first, story after. |
| 20 | Emotional temperature report | Trace | — | The cold at ¶146 and ¶198 is physical snow water, not an emotion report. |

**10 / 20 found (#1, #3, #8, #10, #11, #12, #13, #15, #16, #17). Total −1.625. Band: WATCH** (commercial 9–11). This is the book's highest pattern count (Ch.11 9/20). **#11 hard check: FAIL** (0.81/1k against the >0.8 cap): it caps Prose at 7.5. After the PATH, #11 is 2 at 0.42/1k (minor) and the scan is 10/20 (9/20 with optional R3, which clears #1).

---

## The book's own laws
- **NO FORESHADOWING: PASS, 0.** Gate 0; families A–E read by hand. "I'll stay up the summer." is a plan, and "Kallia will hear at the spring tomorrow" is speech. "It was three days to the seventh of Bysios." is present fact: the allowlisted phrase's planned use 1 of 3, with the Ch.13 title as 2. No 79, no Pompeii, no Italy. The men arrive with no watching beat or rumor beforehand. The Lechaion boat (¶244) is past-facing backfill, told after the fight.
- **Memory only when the scene triggers it (AUTHOR-CP2-2): PASS.**
  - Valens's onions: Mara crushes a wild onion at the pool, he speaks two sentences, and the scene returns at once to the knife (¶154–¶156).
  - Mara's week of lodgers: triggered by the camera in her hands, and returns to the cap (¶162).
  - The Kirrha morning: triggered by the goat in Felix's lap, and returns to the ford (¶240–¶246).
  - No stand-alone memory paragraph; Mara's 1998 memory 0, which is what the outline asked ("save it"); no lost-name close. The onion memory follows its rules: first surfacing, unexplained, not a scene close.
- **Kneel / crouch gated (AUTHOR-CP2-3): PASS, 0.** "dropped into the ditch" is not a kneel. Sitting ×3 (Mara on a rock, Valens on the lip, Felix on the bank), different people.
- **Valens's bare "No." ≤ 1: PASS, 1** (¶332). Mara's 1 (¶92). **Ruling on the callback:** "Did he go down straight off?" / "No." pays off Ch.11's one-blow lie ("Have you ever seen a man killed with one blow?" / "No."). Same asker and answerer, opposite truth-value, unpointed. Continuity W-19 already removed the phrase "one blow" from it. It is a payoff, not a re-staged skeleton, and the bible closes it after this use. **Not charged.**
- **NO TICS, verbal: PASS.** No catchphrase for anyone. "came on a man in the ditch" ×2 and "We came on him" ×2 are the cover story being drilled and then performed, which is the theme on the page. Not a tic.
- **NO TICS, gestures: gate clean.** By hand:
  - The hit man's hands-to-head beat is doubled within ~150 words (¶60, ¶72), and Felix reports it a third time (¶250) → P6.
  - The camera "held … with both arms" (¶76) is restated as "The camera was still in my arms. My hands kept hold of it." (¶120) → P6.
  - "legs braced" ×2 (¶100 mule, ¶304 goat) → P7.
  - Walk-on "His glance [verb]" ×2 (¶18, ¶290): trace.
  - Hand-offs ×4: WATCH.
- **NO TICS, narrator constructions: FAIL → P1, P7.**
  - #11 density over the cap.
  - Anadiplosis ×3 ("The pool … the bottom, and the bottom …"); book-wide it is now 8.
  - "rose off" ×2 for a smell (¶116, ¶154).
  - "face up" ×2 for the cap (¶64, ¶114), after Ch.11's sherd "face up" ×2.
  - **Paragraph-final negations: 12 true instances, 2.84/1k, the book's highest** (previous maximum Ch.2 2.7/1k; Ch.11 1.35). Many are the chapter's best lines ("and then nobody was", "it was not his own"). WATCH: the PATH removes one ("matched nothing else on it"), and Ch.13 should run under ~1.5/1k.
- **No reuse of earlier chapters' phrases or set pieces: FAIL → P2, P4, P5, P6.** The list is under PATH.
- **Retired reflexes:** no define-by-negation opener (¶140 is a "was not X." pivot, P4d); no anaphora triad (¶188's "To … To … Out to" breaks its third); no performed candour; **no aphorism after the killing** (Orestes is mid-scene, specific); no scene button. Scenes end on an act or a sense: "Before the bend, the noise of water." / "He was first down the goat path to the ford." / the cart. ✓
- **Bible at-risk items, checked one by one:**
  - Clean: hinge 0 ✓; "So" 0 ✓; "before I had…" 0 ✓; command echo 0 ✓ ("Felix went." is compliance by result); held silence measured by something moving 0 ✓; gaze-arrival "then" 0 ✓; lying-awake coda 0 ✓; laughs: walk-on menace only ✓; cloth smells 0 ✓; taste recoil 0 ✓; "the one / the only" 0 ✓; "He meant…" 0 ✓; "as if / as though" 1 ✓ (¶8); credential asides 0 ✓; Mara's English 0 ✓; Mara's Greek uncontracted ✓; the notice not re-quoted ✓; "three drachmas" absent ✓; money gap CLOSED as an act ✓; Valens's practical order as an answer to closeness, 1 (allowed from Ch.12) ✓; the watch, one clause ("Through the leather the watch was going.") ✓; Valens's "Mara." untagged, its own beat ✓; work-suspended tells 0 ✓; "let [it] go by / be / pass / stand" 0 ✓.
  - **Breaches, each in the PATH:** bread "full of grit" (SPENT, Ch.4) → P4a; the flashlight's status mentioned without use → P4b; the god's price itemized → P4c; the "was not X." pivot → P4d; the struck knot at Valens's hands → P3; Mara's hands-as-body-rebel channel (rested until Ch.20) together with sample-05's "My hands did that by themselves" → P6; the scrub-past-need's creases and nails (Ch.5) → P5g; the unseen darner (Ch.7) → P5f; a comparison vehicle reused ("the way [the] men in the [market/square]", Ch.11 ¶50) → P5h.
- **Ledger row:** approach ✓, open ✓, end ✓, breaks ✓, dialogue ✓, theme ✓, gear ✓. **Length −12%** (no per-chapter floor; see Pacing). **Beat subversion ✓. Writer warnings:** "No choreographed action-movie fight" ✓ (mostly unseen); camera use as panic, no flash ✓; account not a grievance monologue ✓ (broken by the cloak work); no aphorism after the killing ✓; final punch concrete ✓.

---

## Character Chaos Check (Primary: Mara)
- **Irrelevant thought: PRESENT, inhabited.** "In the olives a bird was saying the same three notes." (¶66), at the height of the fight. Mediated: the Calf-Bearer (¶318).
- **Cognitive distortion: thin.** She asks no question, which is belief by design. The nearest distortion is "She gets the whole of it from me, or nothing." (¶360), which is all-or-nothing as principle.
- **Unprompted memory: ABSENT by design** (outline: "save it"). Absence is not a defect.
- **Failed emotional management: PRESENT, inhabited.** "I wound until there was no strap left" (¶76); "I could not make myself look toward the ditch again, and did not try." (¶114); "my feet stopped belonging to me" (¶144).
- **Voice under pressure: DEMONSTRATED at level 2** (voice-dna rehearsal map). The asides die and return at the stream.
- **2–3 / 4, mostly inhabited.** Commercial profile met.

## Secondary Character Chaos
- **Valens:** the shaking he tries to hide; a graze "he plainly knew nothing about"; the onion memory; "When he was away I slept across her door."
- **Felix:** "Who gets his knife?"; sick, then the crust lie; the sword he wants to have had; "Are goats sick when they see a dead man?"; Spicula.
- **Walk-ons:** the talker's forgiveness; the butcher brother; the graybeard who will not sit with the dead.
- No secondary character is a mere function. No cap.

---

## The Tomorrow Test
**What the reader remembers:**
- A small black lens cap rolling a long way down a road on its rim, wobbling over the ruts with its white letters going under and coming up, until it tips over in a pool of spilt oil.
- A man's voice in a ditch breathing hard, "and then nobody was".
- Then the gladiator under a waterfall, unable to stop his hands shaking, and Mara holding his wrists flat to the stone with snow water up her sleeves.
**Anchor type:** BOTH. IMAGE: the cap; the hands at the fall; the dead man's new sandal tied in a bow; the goat asleep on Felix's shoulders, still chewing; the cart. QUOTE: "and then nobody was"; "That was the use of me."; "Who gets his knife?".
**Verdict: ANCHOR EXISTS** (strong; +0.5 CVI). **Type check:** Ch.11 was an animal's restraint (still); Ch.12 is a small object in motion (kinetic, visual). This type is new to the book and not adjacent to its kin (Ch.3 "an act").

## The Shareability Test
"She's on a mountain road in ancient Greece when three men come for the gladiator. One grabs her, and she smashes him in the head with her dead dad's 1990s camera. The ex-gladiator kills a man in a ditch, and afterwards he's the one who can't stop shaking, so she holds his hands under a waterfall while he tells her who framed him." Running total: 12 chapters, 21+ shareable moments.

---

## Reader Reports

### The Devourer (4.9k after Ch.11's 5.9k)
From line one: a stranger knows the hero's arena name, and the reader knows something is wrong before Mara does ("Show me your right hand, then."). The fight goes in a blur and reads in one breath to "and then nobody was". **Speeds up:** the fight, Felix sick, "Who gets his knife?", the shaking. **Slows:** the legal middle of the telling (lanista, magistrate, bill of sale) is "a bit court-case"; the Kirrha-morning backfill and the purse-and-rag business at the ford (¶240–¶278) are "we're paying for the goat now?". **Would they stop?** No. The ford is short, the graybeard brings a threat, and the cart at the end pulls the page. **Vibes:** "the camera one. Felix throwing up."

### The Critic
**Underlines:** "I've forgiven you."; "My brother's a butcher. He's got two like that."; "Wine. Sweat."; **the cap sentence**; "the same three notes"; "**and then nobody was**"; "it was not his own"; "It was still a pleasant face."; "He had left the man everything else."; "Let the god's people find him."; "A traveler with his purse cut."; "my feet stopped belonging to me"; "He let his forehead come to rest on my hair. He stayed there."; "Cold water. Hot would have set it."; "They'd been shown where to stand."; "That was the use of me."; "Celer kept the boy."; "Tell it anyway."; "the Calf-Bearer … twelve and in a temper"; "Its edge found me as I walked."; "her jaw kept moving".
**Disappointments:**
- "*A hand took the back of my himation* — that is the Ch.5 grab at the temple, word for word in shape" (P2).
- "His hands were sure at it — the knot again, and his hands as a mood ring" (P3).
- "*full of grit* was the bread in Ch.4" (P4a).
- "*a slave with a rod*, he said that exact thing in Ch.11" (P5b).
- "*the oil carts after the snow*, that was the men at the board" (P5c).
- "the pool, the pool, the bottom, the bottom" (P7a).
- "the camera paragraph explains itself twice, and then the sailor" (P1).

### The Hostile
**Logic is the tightest in the book.** The continuity repair closed the sacred-plain geography, the oil jar left by the body, the mule ballast, Praxias's price, the plural knives and the route by which Celer learned where Valens was. Challenges:
1. **¶94 vs ¶74:** Valens already held the talker's knife when he climbed out the first time ("There was a knife in his hand, and it was not his own."). He then comes back from the ditch with "a purse on a cut thong, **and the talker's knife**", as if he took it from the body the second time → L1.
2. **¶268's "He"** reads first as Felix, the last narrated "he" (P3 fixes it).
3. The purse let go in a clear ford just as walkers come to water a donkey (¶278–¶280): a risk nobody remarks on. Kept as tension; not a hole.
4. The cap left in the oil by a body, with a cart coming: "where I meant it to stay" (after P1) makes it her choice. Not a hole.
5. Why did Valens refuse to testify? Unasked by design (subtext), and his fear is plausible.
**Verdict:** "One small knife slip. No hole."

### The Casual Reader (airport, 10 pages)
The first page is the best since Ch.6. A chatty stranger has bet against the hero once and wants to see his hand; the boy and the goat walk ahead; a knife comes out from under a cloak. They gasp at the camera. They do not notice the cap's symbolism; they just watch it roll. They are moved that the tough guy shakes and she holds him. They love Felix ("Who gets his knife?", the crust, the goat on his shoulders). **Frictions:**
- the legal paragraph about who could free whom;
- *Rudiarius* unglossed (skimmed);
- the sprats-and-goat-pen flashback at the ford.
**Would they buy after 3 pages?** Yes, and they would tell a friend about the camera. **Do they stay?** Yes, and the cart at the end makes them turn the page. **9.0/10.** Not 9.5: the telling's middle is denser than the rest, and the ford slows after the stream.

### The Devoted Reader (active: long saga)
**Will post about:**
- Spiculus and Nero's gift of a house; *retentio propter mores* (the dowry share kept for adultery); the husband keeping the child;
- Isis at Kenchreai "on her days"; the Craneion as cypresses; the Kirrhaean plain left bare for the god;
- the K1000's rewind crank; Vespasian denarii fresh in 71;
- the stranger's emperor standing against Valens's sitting one;
- Ch.11's "On its feet" goat ending up on Felix's shoulders;
- "I slept across her door".
**Will catch:** Ch.5's grab frame (P2); "full of grit" (P4a); Valens's rod line from Ch.11 (P5b); "the god's day" (Ch.10 Nikaso, P5a); the market-men comparison (P5h); "Corinthian bronze" as an alloy name (O2).

---

## Cross-Reader Matrix
| Issue | Devourer | Critic | Hostile | Casual | Devoted | Severity |
|---|---|---|---|---|---|---|
| P1 #11 over the cap: the camera paragraphs explain themselves (¶160, ¶162 ×2, ¶170) | | ✓ | | | ✓ | **SHOULD FIX → blocking** (hard cap) |
| P2 Ch.5's grab sentence ("A hand took…") (¶48) | | ✓ | | | ✓ | **SHOULD FIX → blocking** (set-piece frame reused) |
| P3 knot + "His hands were sure at it" + ambiguous "He" (¶268) | | ✓ | ✓ | | ✓ | **IMPORTANT → blocking** (struck device function; pronoun) |
| P4 spent by name: "full of grit", flashlight status, the god's price list, "was not X." pivot | | ✓ | | | ✓ | **SHOULD FIX → blocking** |
| P5 earlier chapters' words/frames (god's day, rod, oil carts, darn, creases, market-men vehicle) | | ✓ | | | ✓ | **SHOULD FIX → blocking** |
| P6 sample-05 strings + hands-to-head doubled + "My hands kept hold of it." | | ✓ | | | ✓ | **SHOULD FIX → blocking** (sample lines 0) |
| P7 in-chapter frames (anadiplosis, "rose off", "legs braced", "face up") | | ✓ | | | | **INVESTIGATE → blocking** (narrator construction) |
| L1 the talker's knife fetched twice (¶74/¶94) | | | ✓ | | ✓ | **SHOULD FIX → blocking** (logic, −4 words) |
| Ford backfill / money handling slows (¶240–¶278) | ✓ | | | ✓ | | SHOULD FIX → **no change** (the ledger's "ford" beat; the money had to close on the page as an act); P4c shortens it |
| Legal middle of the telling dense (¶192–¶200) | ✓ | | | ✓ | | SHOULD FIX → **no change** (outline knowledge path; Ch.17/22 rest on it) |
| Paragraph-final negations 2.84/1k | | ✓ | | | | INVESTIGATE → WATCH for Ch.13 |
| Length −12% (−16% after PATH) | ✓ | | | | | INVESTIGATE → **no padding**; Ch.13/15 should land full |

---

## Revision Recommendations (Ranked)
*Blocking items (P1–P7, L1) are needed for Prose 8.5. R items are recommended; O items are optional. **Every string below was applied together to a scratch copy and run through `check_chapter.sh 12` and `shape_check --strict`: all clean, echo 0, no new 3-gram against Ch.1–11 or the 13 samples.** Each new string greps 0 in Ch.1–11 and the samples.*

| # | Location | Problem type | What happens now | Why it fails | Revision direction | Project rule? |
|---|---|---|---|---|---|---|
| L1 | ¶94 | Logic | "When Valens climbed back up he had a purse on a cut thong, and the talker's knife." | He already held that knife at ¶74 ("There was a knife in his hand, and it was not his own."), so it reads as fetched from the body twice. | → "…he had a purse on a cut thong." (−4) | No |
| P3 | ¶268 | Character / Style | "He chose a stone … so that she would carry level, and tried the knots. His hands were sure at it." | (a) **A knot in Valens's hands**, with his hands read as a mood barometer straight after the shaking: the prior run's struck device ("hands work a knot when feeling threatens") by function. The Ch.11 eval proposed `\bknot\b` near Valens's hands = defect, and it came back through continuity W-13's own string. (b) "He" first resolves to Felix. (c) "so that she would carry level" is a borderline #11. | → "**Valens chose a stone from the bank, near a jar's weight, and roped it opposite the single one on the mule that had lost hers.**" (−14) | Yes: "a repair grep for `knot` within 200 characters of Valens or his hands, every agent" |
| P1 | ¶160, ¶162 | Style (#11 hard cap) | ¶160 "The ring … had taken the blow; it was pushed in at one point, and no filter would screw onto it now. The glass was whole. In the finder…"; ¶162 "Its cap was still in the oil by the ditch, where I meant it to stay; a black disc with letters no one at Kirrha would read as a word was a thing a sailor might have dropped off any boat." | 4 explanatory extensions in 4.9k words = 0.81/1k, over the commercial cap. The sailor clause came from continuity W-20(a). The camera check is also a five-item condition report (device "retired for everyone"). | ¶160 → "**The ring at the front of the lens had taken the blow and was pushed in at one point. In the finder the plane trees stood upright and in focus.**" (−14; three checks instead of five). ¶162 last sentence → "**Its cap was still in the oil by the ditch, where I meant it to stay.**" (−27; her choice stays). #11 → 2 at 0.42/1k. | Yes: "an additive repair recomputes #11 density for the chapter" (restated from Ch.10) |
| P2 | ¶48 | Style (set piece reused) | "A hand took the back of my himation and pulled. The wool came tight across my throat. I was pulled back against somebody." | **Ch.5 ¶151:** "A hand took me by the collar of the fleece and hauled.", which is Mara seized from behind by her garment at the start of violence, in the same frame. "pulled" ×2 in three sentences. | → "**My himation came tight across my throat from behind. I was pulled back against somebody.**" Keep "Wine. Sweat." (−8). Tested; my first wording, "caught from behind. The…", tripped the echo gate ("from behind the", Ch.11). | Yes: "a seizure / grab opens in a fresh frame each time (Ch.5, Ch.12)" |
| P4a | ¶152 | Style (SPENT) | "A graze full of grit ran along his cheekbone." | Bread "full of grit" is SPENT by name (bible at-risk after Ch.5; Ch.4 ¶119). | → "**There was a graze along his cheekbone with grit in it.**" (+2) | No |
| P4b | ¶162 | Continuity (bible rule) | "The flashlight could take its chances." | Bible after Ch.8: the flashlight is "not mentioned again until it is used or seen". | Cut the sentence (−5). | No |
| P4c | ¶272 | Style (SPENT; #3) | "This would. It would buy the cake, and Praxias's drachma, and leave plenty over." | "The price of the god itemized: SPENT … never as a list again"; also a rule-of-three. | → "**This would, with plenty over.**" (−10) The money still closes as an act (ENTITY CH11-3). | No |
| P4d | ¶140 | Style (SPENT pivot; #12) | "The shaking was not small. It started in his shoulders…" | The "was not X." litotes-then-assertion pivot (bible: SPENT, checked by hand). | Cut "The shaking was not small." (−5). "They were shaking." / "It started in his shoulders…" reads straight on. | No |
| P5a | ¶352 | Style (earlier words) | "When the god's day is done, the mules are for the high grazing," | "the god's day" is Nikaso's (Ch.10 ¶146); "the god's first day" ×2 is Valens's and SPENT (Ch.11). | → "**When it's over,** the mules are for the high grazing," (−3) | No |
| P5b | ¶350 | Style / Voice (his own line) | "Inside the precinct there's a slave every few paces with a rod. A knife in there would have a hundred men on it." | Valens's Ch.11 ¶70: "a slave of the god's with a rod, sorting it." The same fact in his mouth twice (audit I-03). | → "**A knife in the precinct would have a hundred men on it.**" (−11) | No |
| P5c | ¶212 | Style (earlier words) | "I saw it too. A copy came up here after the snow, with the oil carts." | Ch.9 ¶386: "With the oil from Thebes. First carts since the snow" (its arrival is already marked spent in the Ch.10 outline). | → "**I saw it too.**" (−11) | No |
| P5f | ¶186 | Style (Ch.7 frame) | "It was good wool, fulled hard, and somebody had darned the hem with a green thread that matched nothing else on it." | Ch.7 ¶26: "darned in a browner wool by somebody in a hurry" is the unseen darner plus an off-color verdict (the unseen-maker verdict, SPENT at 6 chapters). Also a negation ending. | → "**It was good wool, fulled hard, darned at the hem with green thread.**" (−7) Mara's green-thread noticing stays (the disruptor's chaos beat). | No |
| P5g | ¶136 | Style (Ch.5 skeleton) | "There was blood over the backs of them and dried in the creases, the dead man's, … He tried to work the blood from round his nails with his thumb" | Ch.5 ¶239's scrub-past-need: "the creases still dark and the nails black". Creases + nails + thumbs, at a wash after violence (SPENT). | Cut "**and dried in the creases**" (−5). Keep the thumb slipping off the nail: it is the tremor, not a scrub. | No |
| P5h | ¶8, ¶328 | Style (vehicle reused) | ¶8 "the way men in the square looked at a horse they had once had money on"; ¶328 "straight, the way a man asks a price." | Ch.11 ¶50 "the way the men did in the market". The comparison vehicle (local men's public dealings) is used a second and third time; voice-dna: a vehicle domain is used once. | ¶8 → "the way **a man looked at a horse he had once had money on**." (−2; the image kept, past tense, no market men). ¶328 → "…put the question to him instead, straight." (−6) | Yes: "comparison vehicles are logged per chapter (domain, not string)" |
| P6 | ¶26, ¶58, ¶60, ¶120 | Style (sample-05, lines 0) | ¶26 "The second man had come round on my side."; ¶58 "It hit him above the ear."; ¶60 "He put both hands to the side of his head and walked into the wall"; ¶120 "The camera was still in my arms. My hands kept hold of it." | Sample-05 (the Ch.12 register): "Valens had the second man against the wheel"; "It hit him on the side of the head. He sat down."; "My hands did that by themselves". Also: the hit man's hands-to-head is doubled (¶60, ¶72); ¶120 restates ¶76; Mara's hands as body-rebel channel are rested until Ch.20 (bible after Ch.11). | ¶26 → "**Another of them** had come round on my side."; ¶58 → "It **caught** him above the ear."; ¶60 → "He let go. **He walked into the wall, and slid down it.**" (¶72 keeps "holding his head together in his two hands"); ¶120 → "The camera was still in my arms." (−15 total) | Yes: "the chapter's own register sample is scanned at 3-grams, not 5" |
| P7a | ¶130 | Style (anadiplosis) | "…fell in a rope into a pool. The pool was clear to the bottom, and the bottom was pale gravel." | Three "the X. The X was" pick-ups in one chapter (¶82, ¶130 ×2); 8 book-wide. | → "…fell in a rope into **a clear pool over pale gravel.**" (−10) Keep ¶82 ("The foot was turned out."). | Yes: "anadiplosis ≤1 per chapter (`\b(\w{4,})[.,;] (and )?the \1 (was\|were\|had)\b`)" |
| P7b | ¶154 | Style (in-chapter 2nd use) | "and the smell rose off it, green and sharp, from a clump of flat leaves crushed under my heel." | ¶116 "The smell of it rose off my foot". | → "I had trodden on **a clump of flat leaves at the edge of the pool, and they smelled green and sharp under my heel.**" (−5) The trigger and "Onions," are unchanged. | No |
| P7c | ¶304 | Style (in-chapter 2nd use) | "with her legs braced and her head low" | ¶100's mule "with her hind legs braced". | → "She stood at the foot of the climb **with her head low**." (−4) | No |
| P7d | ¶114 | Style (in-chapter 2nd use) | "where the cap lay in the oil, face up, its letters dark with it" | ¶64's "face up"; Ch.11's sherd "face up" ×2. | Cut ", face up," (−2). | No |
| R1 | ¶198 | Style (closed frame) | "The cold had my feet again, up to the ankle bones." | The to-the-joint depth frame is "CLOSED as a frame" (under its 2/ch regex cap). | → "The cold had my feet again." (−5) | No |
| R2 | ¶230 | Style (#1) | "and it stung, now that I knew about it." | Mirrors ¶152 "he plainly knew nothing about it". | → "and it stung." (−5) | No |
| R3 | ¶174 | Style (#1; ex-Ch.11 spout) | "He was washing his forearms in the spout, the left with the right and then the right with the left." | "spout" is Ch.11's trough (Valens "wet from the spout", ¶44); the chiasmus is the chapter's other #1. | → "**He was washing his forearms.**" (−17). Clears #1 (scan 9/20). Minimum: cut only "in the spout". | No |
| R4 | ¶122 | Style (Ch.11 opener) | "Short of the bend, the noise of water." | Sentence-initial "Short of" is Ch.11's near-kiss ("Short of it by the width of a finger"). | → "**Before the bend,** the noise of water." (0) | No |
| O1 | ¶350 | Voice (optional) | "Bring the goat to me at the yard the evening before." | Ch.11's last line: "Bring your drachmas…". Valens's "Bring [X]" two chapters running. | → "**The goat comes to the yard the evening before.**" | No |
| O2 | ¶272 | Immersion (optional) | "and Corinthian bronze underneath" | *aes Corinthium* is a luxury alloy, and a conservator would hear it (audit I-04). | → "and bronze of Corinth's striking underneath" | No |
| O3 | ¶118 | Gesture (optional) | "Valens came behind me with the last mule, at her pace." | Exits by gait: cap 1 per 3 chapters (Ch.9 "at his ordinary pace"). | Cut ", at her pace" | No |
| O4 | ¶44 | Style (optional) | "The stick went past my ear." | Ch.9 ¶42 "a flake sprang past my ear". | → "The stick went by my head." | No |

### Fix order: Logic/Character (L1, P3) → Prose law (P1, P2, P4, P5, P6, P7) → recommended (R1–R4) → optional (O1–O4) → bookkeeping

**Bookkeeping (orchestrator):**
- **Re-sync the bible's Ch.12 blocks to the final page after the PATH.** Continuity W-22 is still pending. Valens's block still quotes "props the cracked jar in the angle of the wall", "That's how it gets told.", "a house on the Craneion", "A quay doesn't ask twice.", "Those three brought knives.", "People do, mostly.", "Was it one blow?", "The whole of it, then," / "Her, and nobody else.", "Then he left me for the ford." and "knot near his hands 0".
- **At-risk after Ch.12, add:**
  - the grab frame (Ch.5, Ch.12) CLOSED;
  - anadiplosis ≤1/ch;
  - paragraph-final negations WATCH (Ch.12 2.84/1k; Ch.13 ≤1.5);
  - "the way [the] men…" vehicle CLOSED;
  - "the god's day" CLOSED (Ch.13's opener uses neither it nor the Ch.11 paraphrases);
  - the onion trigger (a crushed plant) SPENT;
  - "Did he go down straight off?" / "No." DONE;
  - the camera check: three items, never re-done;
  - the cap: LOST, never mentioned.

---

## Strengths to PRESERVE (do not touch in polish)
1. **The first line, byte-identical**, and the stranger: "Do I? Show me your right hand, then."; the Corinth bet and "I've forgiven you."; "These two never saw you fight… And here's the hand."; "My brother's a butcher. He's got two like that."; "And good day to you, lady,"; "*Rudiarius*."
2. **The fight (¶38–¶76)**, apart from P2/P6: "I saw the knife. I saw Valens's hand shut on the wrist above it."; the cracked jar and the oil; "The ditch hid them. I heard them."; "Wine. Sweat."; "Be still, mistress. Be good."; "**Mara.**" from the ditch; "Something struck stone down there, twice."; the camera swung in a twist of panic; "**I felt it in my wrist.**"; "Nobody came at me."; **the cap sentence (¶64), byte-identical**; "the same three notes"; "**and then nobody was**"; "it was not his own"; the strap wound "until there was no strap left".
3. **The aftermath on the road (¶78–¶120):** Felix's fist "open and nothing in it"; the foot with the sandal tied in a bow; sick "neatly"; "**Who gets his knife?**"; "Are you cut?" / "No." / "He looked for blood on me regardless."; "**It was still a pleasant face.**"; "He had left the man everything else."; the sliver of pot thrown after the man; "This is the god's road." / "Let the god's people find him." / "That's what it was. A traveler with his purse cut."; the sandal slapping, "one slapping and one not".
4. **The fall (¶130–¶152), every beat in its order** (apart from P4d/P5g/P4a): the pouch, "Through the leather the watch was going."; "**They were shaking.**"; the thumb slipping off the nail; the shoulder turned to hide the hands, "and I saw them anyway"; "**It was snow water, and my feet stopped belonging to me.**"; the wrists pressed flat; the stitch marks felt in the scar; "I held on… and I did not speak."; "It stopped by degrees."; **"He let his forehead come to rest on my hair. He stayed there."**; "His stayed flat on the stone. He took them down himself."
5. **The onion memory (¶154), two sentences of speech, unexplained**, and the knife washed after it.
6. **The telling (¶172–¶224), byte-identical** apart from P5c/R3: "They gave me the wooden sword at Corinth,"; "The emperor never got out of his chair."; the tablet in a box; Plautia, the household gods; "**That was the use of me.**"; "out where the cypresses are"; "He was sorry about it. He said so, more than once, with her standing there."; "**They'd been shown where to stand.**"; the fishpond; the steward and the tablet; Celer's bill of sale; "A fisherman took me across the gulf for my belt buckle."; "**Celer kept the boy.**"; the knowledge path; "**Whoever wants five hundred brings a rope. Those three brought none. He doesn't want me back. He wants me in a ditch.**"; "He had you by the cloak." / "It is only the wool,".
7. **The ford (¶238–¶300):** the goat chosen for her temper; "the rag was thin after it"; "It was my father's," … "and it went back inside my clothes."; "**It was that crust … It was off.**"; the invented sword / "That's nothing to tell." / "**Tell it anyway.**"; Orestes; the graybeard and "**it won't be me**"; "He believed me," … He sounded surprised.
8. **The climb (¶302–¶370):** the goat lies down; "She is full,"; Spicula; **the Calf-Bearer**; "which in my hearing he had never managed before"; "I was watching something else."; "**Did he go down straight off?**" / "**No.**"; "If you don't stop,"; "I'll stay up the summer."; "Its edge found me as I walked."; "I am not telling Kallia a story."; "It was three days to the seventh of Bysios."; **the goat asleep, "and her jaw kept moving"**.
9. **The last sentence byte-identical:** "A cart had stopped beside the ditch." (`punch`).

---

## PATH TO 8.5 (mandatory; the Floor is 7.5)

**Prose & Voice 7.5 → 8.5 requires two things and nothing else.** First, take #11 under the commercial cap. Second, remove the reused frames P2–P7 (and L1). The stopping sentences (¶68, ¶64, ¶94, ¶144), the ugly sentence and the level-2 voice under pressure already exist. Apply in this order; the strings are exact.

1. **L1** ¶94: "he had a purse on a cut thong, and the talker's knife." → "he had a purse on a cut thong."
2. **P3** ¶268: the whole sentence pair → "Valens chose a stone from the bank, near a jar's weight, and roped it opposite the single one on the mule that had lost hers."
3. **P1** ¶160: "…had taken the blow; it was pushed in at one point, and no filter would screw onto it now. The glass was whole. In the finder…" → "…had taken the blow and was pushed in at one point. In the finder…". ¶162: "…where I meant it to stay; a black disc … off any boat." → "…where I meant it to stay."
4. **P2** ¶48: "A hand took the back of my himation and pulled. The wool came tight across my throat. I was pulled back against somebody." → "My himation came tight across my throat from behind. I was pulled back against somebody."
5. **P4:**
   - ¶152 "A graze full of grit ran along his cheekbone." → "There was a graze along his cheekbone with grit in it."
   - ¶162 cut "The flashlight could take its chances. "
   - ¶272 "This would. It would buy the cake, and Praxias's drachma, and leave plenty over." → "This would, with plenty over."
   - ¶140 cut "The shaking was not small. "
6. **P5:**
   - ¶352 "When the god's day is done," → "When it's over,"
   - ¶350 "Inside the precinct there's a slave every few paces with a rod. A knife in there would have…" → "A knife in the precinct would have…"
   - ¶212 "I saw it too. A copy came up here after the snow, with the oil carts." → "I saw it too."
   - ¶186 "…fulled hard, and somebody had darned the hem with a green thread that matched nothing else on it." → "…fulled hard, darned at the hem with green thread."
   - ¶136 cut " and dried in the creases"
   - ¶8 "the way men in the square looked at a horse they had once had money on." → "the way a man looked at a horse he had once had money on."
   - ¶328 cut ", the way a man asks a price"
7. **P6:**
   - ¶26 "The second man" → "Another of them"
   - ¶58 "It hit him" → "It caught him"
   - ¶60 → "He let go. He walked into the wall, and slid down it."
   - ¶120 cut " My hands kept hold of it."
8. **P7:**
   - ¶130 → "…fell in a rope into a clear pool over pale gravel."
   - ¶154 → "I had trodden on a clump of flat leaves at the edge of the pool, and they smelled green and sharp under my heel."
   - ¶304 → "with her head low"
   - ¶114 cut ", face up,"
9. **Recommended:** R1–R4 (all tested). **Optional:** O1–O4 (all tested).
10. Re-run `bash books/the-hour-of-ash/tools/check_chapter.sh 12` and `python3 tools/shape_check.py books/the-hour-of-ash --strict` (from /home/user/Books). The first and last sentences must stay byte-identical.

**What the tested run produced** (items 1–9 together, including R and O): **4,713 words** (shape_check; −199). Dialogue **28%** (25–35 ✓), median **10** (gear low ✓), 2 breaks, `dialogue` → `punch`. Every gate clean, echo 0, shape CLEAN, no new 3-gram against Ch.1–11 or the samples. With items 1–8 only, the expected count is about 4,760.
- **Anti-AI after:** #11 2 at 0.42/1k (minor; the cap clears); #3 3 (moderate); #12 speech only. **10/20, or 9/20 with R3**, at −1.375 to −1.5.
- **Expected:** Prose 8.5 → **Floor 8.5, Average 8.71** (Originality 8.5, Theme 8.5, Characters 8.5, Prose 8.5, Pacing 9.0, Emotion 9.0, Immersion 9.0), Casual 9.0 held. Originality 9.0 becomes arguable once P2/P5f/P5g/P6 are out; I would not award it on this chapter alone (the *Outlander* spine).
- **Do not use:** "caught from behind" before "The" (echo gate: "from behind the", Ch.11); "at the bottom" (14 book-wide); "After that" (already Valens's at ¶200); "in green" (4 book-wide).
- **Do not touch:** Strengths #2's cap sentence, #4's beat order, #6, the onion memory, or the last line.

**Word count note:** the PATH is pure subtraction, so the chapter goes from −12% to about −16% against target. There is no per-chapter floor, and the book still projects ~242k against 245k (220k floor safe). **Do not pad Ch.12.** Ch.13 (8,000) and Ch.15 (7,800) should land full.

---

## Pacing check (one line for `feedback/progress.md`)
Ch.12: 4,912w (target 5,600, −12%, below its own 5,000 budget floor; after the PATH ≈4,713, −16%; no per-chapter floor, do not pad; book 64,823 vs 69,600 cumulative, −6.9%, ≈242k projected vs 245k, 220k floor safe) · dialogue 27% (25–35 ✓) · 2 breaks ✓ · gear **low**, median 10 ✓ (down from Ch.10/11's mid 15/14, as planned) · in medias res between Ch.11 Chronological and Ch.13 Parallel ✓ · fight fast / road plain / stream slow / telling flat and broken by work / ford brisk / climb measured ✓ · emotional slot: the book's first crucible after Ch.10's grief and Ch.11's warmth: shock → tenderness → disclosure → dread (the cart) ✓ · value shift −/± ✓ · `dialogue` / `punch` (concrete, pull 8) ✓ · hinge 0 ✓ · peak not a laugh ✓. **Verdict: OK.**

---

## Cross-Book Pattern Detection (Ch.1–12)
1. **The recurrence fingerprint is twelve for twelve, and its sources have moved.**
   - Ch.12's reused frames come from two places: the book's reference shelf (sample-05, the chapter's own register sample; Ch.5's grab; Ch.4's grit; Ch.7's darn; Ch.5's scrub creases) and the chapter just before (Ch.11's rod, spout, "Short of", the market-men vehicle, the god's-day paraphrase).
   - The Ch.10 lesson — "list the previous chapter's set pieces and stage the new one differently" — needs a sentence-level twin: **list the previous chapter's narrator frames** (openers, comparison vehicles, objects' positions).
2. **Repairs added defects again.**
   - Continuity W-20(a) added an explanatory clause that tipped #11 over the cap (as Ch.10's cuts did from the other side).
   - W-13's ballast string carried "His hands were sure at it." with it, putting a knot back in Valens's hands.
   - Every additive repair must re-measure #11 density and grep `knot` near Valens.
3. **The register sample leaks by string at 3-grams.** Sample-05's "It hit him", "side of the head", "the second man" and "my hands did that by themselves" are all under the 5-gram sample scan.
4. **Paragraph-final negation is at a book high (2.84/1k).** Under pressure it is the right register; as a habit across chapters it is the at-risk item from Ch.3. WATCH.
5. **Anadiplosis ("the pool. The pool…") is forming:** 8 book-wide, 3 in Ch.12.
6. **What varies, as it should:**
   - the structure (in medias res, the second);
   - the opening (`dialogue`, not adjacent to Ch.8's) and the ending (`punch`, not adjacent to Ch.9's);
   - gear low after two mids;
   - the anchor type (an object in motion, new);
   - the body-rebel channel (his hands, her feet, Felix's stomach; her voice and seat rested);
   - the peak (not a laugh);
   - the plot (it moves hardest here).
   Shape audit CLEAN; the ledger row honored on every hard field.

**Pipeline (UPDATE RULE, root; not done here):**
- (a) the struck-device grep (Ch.11 #17a, still unbuilt): `knot` within 200 characters of Valens / "his hands";
- (b) a 3-gram scan of each chapter against **its own** register sample;
- (c) an anadiplosis counter (≤1/ch);
- (d) a paragraph-final negation counter (WATCH ≥2.0/1k);
- (e) an editor/continuity rule: any additive repair recomputes #11 density.

---

## VERDICT
**POLISH. Gate NOT MET.**

| Measure | Result |
|---|---|
| Genesis Floor | **7.5** (Prose & Voice, capped: #11 at 0.81/1k over the commercial cap) |
| Average | **8.57** |
| Casual | **9.0** |
| Pacing | **OK** |
| CVI-Launch (CVI-L) | **9.7** |
| CVI-Legacy | 6.6 (provisional) |
| Mechanical suite | all clean (echo 0, tic gate clean, voice-wear strict clean, shape CLEAN) |
| Foreshadowing | **0** |
| Memory triggered by the scene (CP2-2) | ✓ |
| Kneel/crouch (CP2-3) | 0 ✓ |
| Valens's bare "No." | 1 ✓ (a callback payoff, not a skeleton re-stage) |
| Tics | no verbal tics; gesture gate clean; narrator constructions FAIL (P1, P7) |
| Reuse of earlier phrases / set pieces | FAIL (P2, P4, P5, P6) |
| Ledger | ✓ on every hard field; length −12% |
| Beat subversion | ✓ |
| Anchor and surprise | land ✓ |
| AI patterns | 10/20 (watch band) |

**Failing dimension: Prose & Voice only (7.5).** Fixes, all surgical and tested together:
- **L1**: "and the talker's knife" out (¶94).
- **P3**: the knot and "His hands were sure at it." out, with "Valens" named (¶268).
- **P1**: the filter clause, "The glass was whole." and the sailor clause out (¶160, ¶162).
- **P2**: "My himation came tight across my throat from behind." (¶48).
- **P4**: "with grit in it"; the flashlight line out; "This would, with plenty over."; "The shaking was not small." out.
- **P5**: "When it's over,"; the rod sentence out; the oil-carts sentence out; "darned at the hem with green thread"; "dried in the creases" out; the market-men comparisons recast or cut (¶8, ¶328).
- **P6**: "Another of them", "It caught him", the hands-to-head clause out, "My hands kept hold of it." out.
- **P7**: "a clear pool over pale gravel"; "they smelled green and sharp under my heel"; "legs braced" and the second "face up" out.

Then run E (gates) and F (re-evaluation). Expected after one cycle: **Floor 8.5 / Average 8.71 / Casual 9.0 / PASS.**

This is the chapter the romance has been building toward since the snow. A stranger's friendly voice turns into a knife; she swings her father's camera and watches its cap roll away into the oil; a man dies in a ditch out of sight. Then the gladiator cannot stop his hands, she holds them under snow water without a word, and he tells her flatly how a legate's debts made him a slave again. What holds it below the gate is not the story. It is a dozen borrowed frames and four clauses that explain what the scene has already shown.

**BIAS CHECK:** This evaluation was produced by the same system that wrote the prose. Confidence in every score at or above 8.5, in Pacing, Emotion and Immersion 9.0, in Casual 9.0 and in CVI-Launch 9.7 requires external validation (beta readers, editors, comp analysis).
- **The 7.5 rests on a mechanical density cap crossed by a hair** (4 instances where 3.9 is the line). A reader who does not count "Cold water. Hot would have set it." as an extension puts Prose at 8.0. I count it by the standard that counted Ch.10's Armada clause and Ch.11's olive-path sentence.
- Several P5 items are judgments about frames rather than strings (the vehicle domain, the creases, the darn). Each is held because the bible names its source as SPENT or closed.
- Pacing 9.0 is the book's first; a reader who weights the −12% length or the ford backfill would put it at 8.5, which still passes.
- CVI-Launch 9.7 is a one-chapter formula, not a book forecast.

---

## Polish cycle 1 applied (book-editor, 2026-10-20)

**Applied as written (the page matched every quoted string):**
- L1 (¶94), then P3 (¶268, with "Valens" named; the knot and "His hands were sure at it." are out).
- P1 (¶160, ¶162) and P2 (¶48).
- P4a–d, P5a/b/c/f/g/h (¶8 and ¶328), P6 (¶26, ¶58, ¶60, ¶120), P7a–d.
- R1, R2, R3 (the full cut: "He was washing his forearms."), R4.

**Optional items:**
- **O1 applied** ("The goat comes to the yard the evening before.", −1 word).
- **O3 applied** (", at her pace" cut).
- **O2 skipped:** it adds words.
- **O4 skipped:** it is a like-for-like swap, not a cut.

No sentence was added anywhere.

**Measured after:**
- Words: 4,711 (shape_check), 4,722 (style_check), 4,907 (`wc -w` incl. header).
- Dialogue 27.8%; median 10; 2 breaks; `dialogue` → `punch`.
- First and last lines byte-identical.
- `check_chapter.sh 12`: all clean. Style, grammar 0, rhythm 0, show/tell no flags, voice-wear strict, tic gate, echo 0, command echo none, metaphor, shape CLEAN.
- `shape_check --strict`: CLEAN.

**Hand checks:**
- #11 down to 2: "Hot would have set it." and the camera-under-chiton clause.
- Anadiplosis 1 (¶82, kept).
- Valens's bare "No." 1 (¶332); Mara's 1.
- Kneel/bend 0 ("bend" only as the road's).
- `knot` near Valens 0.
- Foreshadow 0.

**Watch for re-eval:**
- The recast "It caught him above the ear" (¶58) and the existing "where the stick had caught it" (¶174) put two blow-landing "caught"s in the chapter about 1,700 words apart. This is under any cap, but it is a verb now doubled.
- "Another of them" (¶26) sits about 100 words after the stranger's "not another hand" (¶18), in a different sense.
- Bible blocks are not re-synced (bookkeeping is the orchestrator's; W-22 is still pending).
