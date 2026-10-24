# Continuity Check: Chapter 30 "Tremor" (MANUSCRIPT AUDIT)

**Date:** 2026-10-24
**Audited text:** `manuscript/chapters/chapter-30.md` as it stands (md5 `8e0f735b…`), after writer, dialogue-polish, hook-craft and disruptor. Body about 2,512w. Line refs are to that file.
**Checked against:** Ch.1–29 (targeted greps, plus my own 3/4/5-gram scan of the Ch.30 body against every earlier chapter). ENTITY_STATE.yaml as of Ch.29, read only: cobblers-shop, nuceria-gate-tomb, CH20-7 (door_location), CH26-4 (Aelia's age), the world rule for the door's temperature ladder, the tremor-notes rows. outline Ch.29–32. foundation §3/§4f/§10/§116/§222/§261. voice-dna §0/§1. character-bible: Voices from lives; the MARA, VALENS, GRATA, LUCIUS and AELIA cards; the Ch.30 walk-on block; At-risk after Ch.28 and after Ch.29 (SPENT / CLOSED / CUT / WATCH / the eight Ch.30 guards / craft rules). The four pass reports (writer report, dialogue, hook incl. the foreshadowing ruling, disruption). Ch.6 and Ch.11 are read as committed canon and were not audited.
**Gates re-run by me:** `closed_check.py 30` clean (23 constructions). `tic_report.py --echoes 30` found 0 echoes, 0 command echoes and 0 spoken-line echoes. `tic_report.py --gate` clean. My n-gram scan hit only "in front of him and", which is generic. Everything below was found by reading.
**Total issues:** 44. **Critical:** 3 | **Warning:** 16 | **Info:** 25

**Verdict:** The facts underneath are sound:
- **Dates and ages.** February AD 77 sits between Ch.29 (December 76) and Ch.31 (March 77). Fifteen years after the quake of February AD 62 is exact. "Nearly five years of Kalends" is right (arrival spring 72; Ch.29's "fifth Saturnalia"). Lucius is about 2y7m and Aelia about 13–14 months, still at the breast. "Wall broke," fits his two-word stage. "A mile" matches Ch.25.
- **The house.** The hearth corner, light-well, bed and pallet are all in the back room. The stalls are heard from there. The hearth wall is the party wall with Grata. The house has no kitchen and no upper floor.
- **The tomb.** The route runs east, then south to the Nuceria Gate. The tomb is low and white with a big tomb next door, two painted leaves, the name in the gable and Eros's bench. The coolness is faint, never cold, which keeps Ch.19/25/27's door law. The carter's story comes from Ch.25/27.
- **The knowledge beat.** Valens has known of a door since Ch.15. He knew the gate and her Kalends cadence from Ch.19–20, and he never heard a gate named in Ch.25. So "Its place I had told nobody" is true, and the beat (dust, reads the name, asks nothing) now gives him the tomb, as CH20-7 planned.
- **The notebook and the objects.** The notebook is in the satchel under Fenn's letters (Ch.26). The back leaves were blank at the crossing (Ch.20). The entries are in English, written with a reed, with no count. There are four mules.
- **Guards.** Grata's oath by Castor is a woman's oath and the book's first. No reserved word appears, "the painted door" appears 0 times (1 left), nobody names the mountain, there is no portent, and the closing line is clean.

**The three CRITs are all re-spends:**
- a narrator frame on its third book-wide use, which also states Valens's habit as a rule;
- Ch.29's SPENT sneeze cloud (white powder hanging in the sun over dough), rebuilt and fused with Ch.26's light-well dust;
- Grata's race-frame arrival, which Ch.28 cut and logged "never restore".

Each fix is a pure cut of 3 to 10 words.

---

## CRITICAL ISSUES (must fix before the evaluator)

### [CRIT-001] "the look he gave a ford once the mules were over it": a narrator frame on its third use, and a habit stated as a rule
- **Audit:** 1 / voice (NO TICS: a frame that recurs 3+ times book-wide is a defect; Ch.29 craft rule: "The narration never states a character's habit as a rule."; Voices from lives, the nameable-rule test)
- **Evidence:**
  - Ch.16 l.272 (Kallia): "with the look she gave a jar when a lodger had been standing too near it."
  - Ch.25 l.390 (Valens): "watched Fenn down the room with the look he kept for a horse gone lame that had still to find it out."
  - Ch.30 l.120 (Valens): "In the arch he turned for one look back at the tombs, the look he gave a ford once the mules were over it."
- **Description:** The skeleton "the look [S] gave/kept [for] a [work object] [when/once clause]" is used a third time, and this is its second use on Valens. It also tells the reader what Valens always does at fords, which is the habit-as-rule move.
- **Fix (l.120):** cut the appositive. "In the arch he turned for one look back at the tombs. He entered the passage ahead of me." ("one look back at the tombs" appears 0 times in Ch.1–29 and the CUT logs.)
- **Cascade:** none. The beat (he looks back, then goes ahead) is kept.

### [CRIT-002] The crack's dust "hung, turning, where the light-well sent its slant down": Ch.29's SPENT sneeze cloud and Ch.26's light-well dust, rebuilt over dough
- **Audit:** 4 / SPENT ledger (At-risk after Ch.29, SPENT "never again, in any words": "the farce (the trough, the sneeze cloud…)". The Ch.29 walk-on block quotes the cloud as "burst up and hung in the sun". Ch.30 guard 2: the dust-on-bread anchor must not call back Ch.29.)
- **Evidence:**
  - Ch.29 l.228: "under his knuckles the youth sneezed; a cloud of flour burst up and hung in the sun over the front row". This is a kneading trough.
  - Ch.26 l.232: "A slab of sun lay in from the light-well over the blanket, warm, with the dust turning in it."
  - Ch.30 l.14: "All along it a thin white dust sifted out and hung, turning, where the light-well sent its slant down. It settled on the hearthstone. It settled on the board, and on the dough."
- **Description:** The opening shard is kneading with white powder hanging in a shaft of sun over the dough. That is Ch.29's farce image, and the participle "turning" in the light-well's light is Ch.26's. The anchor is the dust *settling on* the dough, so the hanging clause is not needed for it.
- **Fix (l.14):** "All along it a thin white dust sifted out. It settled on the hearthstone. It settled on the board, and on the dough."
- **Cascade:** the light-well leaves the chapter, which is harmless (it is canon in Ch.19/26). The anchor and the S1 word budget are intact (−9 words).

### [CRIT-003] "She saw us coming and started before we were in earshot.": the CUT Grata race frame restored, putting the chapter over the race-frame cap
- **Audit:** 1 / CUT log + caps (Ch.28 CUT LOG, cycle 2, S1–S5: "start on him before he had sat", never restore. Ch.28 eval S4/S5: "Two of them clock Grata's speed with the same frame, so a trait of hers is narrated twice through one device". WATCH for Ch.30: race frame ≤1.)
- **Evidence:**
  - Ch.30 l.142: "She saw us coming and started before we were in earshot."
  - Ch.30 l.162: "Before we had finished, a wad of rag came worming through the top of the split". That makes 2 race frames against a cap of 1.
- **Description:** This is the same construction on the same character doing the same thing: Grata's flood starts before the other party has arrived. It is the restoration in substance that Ch.29's CRIT-003 precedent treats as critical.
- **Fix (l.142):** "Grata had Aelia on her hip at the counter and Lucius sitting on the marble with his legs hanging down. She saw us coming." The flood paragraph follows unchanged and supplies the speed by itself.
- **Cascade:** the race frame count is now 1 (l.162), which meets the cap. The disruptor's earlier cut ("from forty paces") stays.

---

## WARNING ISSUES (should fix)

### [WARN-01] Back-room floor: earth here, boards in Ch.26
- **Audit:** 4 / geography (the same room: bed, light-well, Lucius's pallet)
- **Evidence:** Ch.26 l.22: "Valens lay asleep … with one arm dangling to the floor, the palm up on the boards." Ch.30 l.12: "Under my feet the trodden floor heaved"; l.18: "Aelia had been sitting on the earth by Lucius's pallet".
- **Fix:** l.12 "the trodden floor" → "the floor". l.18 cut "on the earth": "Aelia had been sitting by Lucius's pallet, drumming a lid on her knees."
- **Cascade:** l.16 "The floor lay still." and l.18 "slapped the floor" stay neutral. The shop's beaten earth (Ch.19 l.245) is untouched.

### [WARN-02] "and written none of it down" against Fenn's standing request to write after every Kalends
- **Audit:** 3 / information flow
- **Evidence:** Ch.27 l.490: "Write me," he said. "After the Kalends. Every one. Just that it's cool." (spring AD 76). Ch.30 l.178: "Nearly five years of Kalends I had walked to his door, and written none of it down."
- **Fix (l.178):** "Nearly five years of Kalends I had walked to his door, and none of them had gone in here." This limits the claim to the notebook. "had gone in here" appears 0 times in Ch.1–29 and the CUT logs.

### [WARN-03] The door-status formula "the same" is forming a refrain (4 book-wide, 2 in this chapter)
- **Audit:** 1 / NO TICS (a phrase that recurs 3+ times as a formula); in-shard redundancy
- **Evidence:** Ch.20 l.267/269: "And it's the same." / "It is the same." Ch.30 l.100: "faintly cool, the same as on the day I found it." Ch.30 l.186: "*Eros: the same.*". l.92 has already said it: "the coolness was the one I had found there when we were new in the town."
- **Fix:** l.100: "Sweat was going cold along my spine, and the door was a door on a tomb, faintly cool." l.186: "*Eros: no change.*" ("no change" appears 0 times in Ch.1–29.)
- **Cascade:** the outline's "the same faint coolness she felt the day she found it" is still met by l.92. "No colder." stays. Bible writer-note quote "*Eros: the same.*" → update at sync.

### [WARN-04] Pressing beats three in about 150 words, the last one a full flat hand (Ch.19's spent palm, Ch.42's reserved gesture)
- **Audit:** 1 / gesture gate by hand (3+ of a class inside 500 words) + Ch.30 guard 4 / Ch.42 reservation
- **Evidence:** l.88 "My palm met it … and I pressed."; l.94 "I pressed harder."; l.98 "I bore down with palm and fingers together, and waited for the door to answer the ground." Ch.19 l.355: "I spread my fingers and gave it the whole of my palm."
- **Fix (l.98):** "I waited for the door to answer the ground."
- **Cascade:** "Eros's bench was against my shin…" stays. The palm is still on the door from l.88.

### [WARN-05] "His lips moved on it once, without sound.": Valens's Ch.17 reading beat rebuilt (reading-with-lips class at 5 book-wide)
- **Audit:** 1 / gesture + Valens card
- **Evidence:** Ch.17 l.210 (Valens reading his own name): "His mouth moved on the first word, and then it stopped moving, and he read the rest of it with his lips shut". Also Ch.5 l.113, Ch.9 l.306, Ch.25 l.28. Ch.30 l.116: "His lips moved on it once, without sound."
- **Fix (l.116):** cut the sentence. "He read the name over it. I watched him read it. His hands hung empty at his sides; the headstall lay by my board at home."
- **Cascade:** the NON-NEGOTIABLE reading of the name is kept. Post-positive ", once" falls from 2 to 1.

### [WARN-06] Talking to a non-listener: 2 against a cap of 1
- **Audit:** 1 / at-risk cap ("said/told the [non-listener]" ≤1 per chapter; "[X] told [object]" ≤1 per two chapters; Ch.29 had 0 "told [object]")
- **Evidence:** l.46 "'It goes clean through,' Valens told the crack."; l.138 "a woman … was telling the snakes about her roof". l.28's "'Castor,' said the wall." is the designed opener of S2, so it is not counted, but it is a third object-as-addressee beat.
- **Fix (l.138):** "At the crossing shrine a woman had set a honey cake on the altar under the painted snakes." This keeps Valens's line, which is really addressed to Grata.
- **Cascade:** the bible's Ch.30 walk-on block entry "telling the snakes about her roof" must be moved to its CUT line.

### [WARN-07] Grata's voice "getting through" the barrier, twice in the chapter (three times book-wide)
- **Audit:** 1 / repeated joke shape
- **Evidence:** Ch.26 l.24: "her voice, which the wall did very little to stop." Ch.30 l.30: "The crack brought her through to us whole." Ch.30 l.166: "She talked on till the light changed, and the rag let most of it through."
- **Fix (l.166):** "She talked on till the light changed."

### [WARN-08] The X-first-then-Y skeleton: 4 by reading against a cap of 1
- **Audit:** 1 / WATCH caps (Ch.29 eval l.727: `first … (after|then)`, `at the start, and then`, cap 1)
- **Evidence:** l.10 "The board went first. … Then the water jar beside the hearth began to talk."; l.40 "First he tried the beam over Aelia's head … He dropped the headstall"; l.90 "at first I felt only the two warmths together … It left slowly. Under it, when it rose"; l.146 "Valens looked in on the mules first, and then set his shoulder to our wall".
- **Fix:** l.10 "Then the water jar…" → "The water jar beside the hearth began to talk." l.40 "First he tried…" → "He tried the beam over Aelia's head, shoving up at it, and the beam held." l.146 → "After the mules, Valens set his shoulder to our wall beside the crack and leaned on it, hard."
- **Cascade:** l.90 (the protected tomb beat) is the one that stays, which meets the cap. Note that l.146's "After the mules" is a sequence word, not a "first", so the race/first-then census is not moved sideways.

### [WARN-09] Grata knows the plasterer is promised to the cooper before anyone could have told her
- **Audit:** 3 / information flow (plausible but unshown)
- **Evidence:** l.136, the plasterer to Valens in the street: "Tell her she's behind the cooper and the widow and this fellow here." Then l.142–144: Grata has started her flood before Valens reaches her ("…And the plasterer's promised to the cooper."). Dialogue-polish read this as designed.
- **Fix (l.144):** cut "And the plasterer's promised to the cooper." Her opening "there goes a plasterer's day" (l.32) already carries her plasterer worry.
- **Cascade:** the plasterer's "Tell her" stays unrelayed. That is fine, and it means no command echo.

### [WARN-10] "the question" reads as Valens's, but a "my dead" cover makes no sense to a man who asks after "your gate"
- **Audit:** 3 / information flow
- **Evidence:** Ch.20 l.263–269: "Do you still walk out to your gate?" / "On the Kalends." / "And it's the same." Ch.30 l.118 "He put no question to me." Ch.30 l.140: "Passing the fountain I had an answer ready for the question, a poor one, about my dead and what a Greek owed them out of season. I did not need it." Ch.30 l.160 "Once during the meal I thought Valens would ask."
- **Fix (l.140):** "Passing the fountain I had an answer ready for the women there, a poor one, about my dead and what a Greek owed them out of season." These are the l.74 women who watched her run. "the women there" appears 0 times prior.

### [WARN-11] Fenn's carter story has drifted: "a family eating late"
- **Audit:** 3 / information (paraphrase of Ch.25 canon)
- **Evidence:** Ch.25 l.254: "There'd been people out on that road all night, out of their houses, scared to sleep under the roofs, and a whole family sitting on the bench by that tomb felt it on their legs". Ch.30 l.56: "a family eating late on the tomb road had felt cold come off Eros's door till nearly dawn".
- **Fix (l.56):** "On the night of the big shake a family sitting out the night on the tomb road, afraid of their roofs, had felt cold come off Eros's door till nearly dawn, and Fenn heard of it from a carter, too late to go." ("sitting out the night" and "afraid of their roofs" appear 0 times prior; "cold as a cellar" is not reused.)

### [WARN-12] "the ink gone brown on the oldest": the established ink cannot brown
- **Audit:** 4 / objects + the conservator's eye (voice-dna §1.1)
- **Evidence:** Ch.26 l.182: "the one mercy of lampblack and gum". That is carbon ink, which stays black. Iron-gall ink is the kind that browns. Ch.30 l.178: "each dated and short, the ink gone brown on the oldest."
- **Fix (l.178):** cut ", the ink gone brown on the oldest" → "now my writing ran across them, entry after entry, each dated and short."

### [WARN-13] "I had her in my arms with no memory of crossing the room.": a stock line from the body-acts-without-me family
- **Audit:** 1 / retired frame (Ch.6 l.85 and Ch.22 l.254 "without me"; Ch.25 audit WARN-02 cut three; generic genre cliché)
- **Evidence:** l.20.
- **Fix (l.20):** "I had her up in my arms. She was warm and whole and she wanted down; …" ("up in my arms" appears 0 times prior.)

### [WARN-14] "Valens was a long ridge of wool on the wall side.": the bed sides swap, brushing Ch.23's SPENT door-side turn
- **Audit:** 1 / character location + SPENT (Ch.23 "He turned over, to face the wall, and the door was behind him, and so was I.": the anchor of his trust, SPENT)
- **Evidence:** Ch.26 l.20–22: Mara "leaned on the wall"; Valens "with one arm dangling to the floor", which puts him on the open side. Ch.30 l.190: "on the wall side".
- **Fix (l.190):** "Valens was a long ridge of wool." Cut "on the wall side".

### [WARN-15] Violets "each Kalends": a February flower carried all year
- **Audit:** 4 / world (authenticity dial ~8; violets bloom roughly February–April in Campania; the Violaria fell in March)
- **Evidence:** l.76: "Each Kalends I passed under that arch at a walk, with a few violets in a cloth … A woman with violets got no second look on that road."
- **Fix (l.76):** "with a few flowers in a cloth: a woman going out to her dead. A woman with flowers got no second look on that road."
- **Cascade:** l.80's goat "eating the violets off a tomb step" stays, and is true in February. Ch.19's rose woman agrees with "flowers".

### [WARN-16] "Valens laughed. Lucius laughed … and Aelia laughed": a three-clause verb triad
- **Audit:** 1 / retired reflex (anaphora/parallel triads; outline Ch.30 writer warning "No anaphora")
- **Evidence:** l.44.
- **Fix (l.44):** "Valens laughed. Lucius copied him, eyes squeezed shut, both hands clapped over his mouth, and Aelia laughed at the pair of them at the top of her lungs, for no reason she needed." ("copied him" appears 0 times prior. I rejected "joined in" because it is Ch.23 l.212's hen.)
- **Cascade:** the outline's "the family laughs" is kept, and l.50's "He saw I was not laughing" stays.

---

## INFO (no change required unless noted)

- **I-01 "Two babies" (l.126): RULED ACCEPTABLE.** This is Mara's panic word in a self-reproach sentence, not a stated age. The page elsewhere keeps the ages exact: Lucius speaks two-word lines, and Aelia is nursed. Lucius is about 2y7m (born summer 74), Aelia about 13–14 months (born about December 75 / January 76, per ENTITY CH26-4). "I had run a mile" matches Ch.25's "a mile" (nuceria-gate-tomb row). Use the disruptor's fallback ("Our two, left with…") only if the evaluator objects.
- **I-02 "Wall broke," (l.24) and "Grata," (l.36):** right for his stage (bible LUCIUS: about 2 = single words and two-word utterances; Ch.29 "Tata. Ball."). There is no lent adult mood in the words. Separately, "hands clasped behind him" (l.158) and "at a solemn crawl" (l.160) are two lent-solemnity postures in three lines. Consider keeping one.
- **I-03 Timeline:** February AD 77 is consistent with Ch.29 (December 76), Ch.31 (March 77), Ch.32 (summer 77, Lucius 3) and foundation §10 ("77: tremor, elections (March)"). The AD 62 quake fell on the Nones of February, so "fifteen years back" is exact, and it agrees with ARCH-14's "ten years" in AD 72. The day runs mid-morning, then midday, then "till the light changed", then lamplighting, then night. The outline dateline has no month: patch it to "*Pompeii · February, AD 77*". The visit is off the Kalends cycle, as the ENTITY forward constraint requires ("out of season", l.140).
- **I-04 House geography: consistent.** The back room holds the bed, a high window onto the light-well (Ch.19 l.245; Ch.26 l.232), the hearth (Ch.21 l.90), Lucius's pallet (Ch.28/29), and the mule stalls heard from it (Ch.28 l.58). The hearth wall is the party wall with Grata (Ch.28 l.290), and Grata's back room "ran the depth of the house" (Ch.24 l.18), so "my bed" fits. Valens is "out front" in the shop opening. There is no kitchen and no upper floor. Harmless, and unremarked: Grata's eye "high against the beam" means she is standing on something.
- **I-05 The tomb: consistent.** The route runs east past the fullery and fountain, then south at the crossing to the Nuceria Gate. That agrees with Ch.25 l.408 ("east of the forum, the street with the fullery") and with the real Via di Nocera. "Low and white among its neighbors" and "the big tomb next door" match Ch.19 l.347–349. Two leaves are on the page (the left this time, the right in Ch.19). The name is in the gable ("read the name over it"). Eros's bench and Fenn's nights come from Ch.25 l.314. The faint coolness keeps Ch.27's law (a live door is the cold one; Eros's is only cool) and the ENTITY temperature ladder. "Cold" is used only of the AD 62 night and of her sweat. The carter, three days late with a fever, matches Ch.25 l.254 and Ch.27 l.338 (except WARN-11).
- **I-06 The knowledge beat: consistent with Ch.15, Ch.19, Ch.20 and Ch.25.** Valens knows a door exists (Ch.15 l.292 "How will you know the door, among all those tombs?"). He heard that the Nuceria Gate was next (Ch.19 l.331). He knows her Kalends cadence and "your gate" (Ch.20 l.263–269). In Ch.25 he heard Fenn's English with no gate named (the Ch.25 W-01 repair) and "He knows it." (the door's existence). He has learned no date, law or place. So l.114 is literally true, and from l.116 he has the tomb. "Eros" was said four times in Ch.25's English, so his silent read may connect it. He asks nothing, which agrees with the card. Optional sharpening: "Which tomb, I had told nobody." **CH20-7 can now be closed** (see patches).
- **I-07 Fenn's notebook: consistent.** It is in the satchel under Fenn's letters (Ch.26 l.32 "lying on top of the notebook"). The back leaves were blank at the crossing (Ch.20 l.277). The entries are dated and short (Ch.26 l.40), in English, written with a reed (Ch.26 l.182). Eros was in none of them, and Ch.20's entry was "*small shake, lamps, nobody woke*". The new entry has no count and no reckoning and is shaped unlike Ch.20's (guard 6 met). "Off its nail" is new and fits Ch.25's satchel carried at her hip when travelling.
- **I-08 Objects:** "all four mules" (l.12) agrees with Ch.26 l.116 and Ch.28 l.58. The dun is not singled out, which is fine. The headstall's path holds: out front (l.22), dropped by the board (l.40), "by my board at home" (l.116). That last clause is an explanation tail; it is optional to cut.
- **I-09 Grata's oath by Castor: period-correct.** Gellius NA 11.6 says women swore by Castor, men by Hercules, and both by Pollux. voice-dna §1 lists "by Castor". It is the book's first Castor (Ch.18 has "by Pollux"; Ch.24 Juno Lucina). "Their mother" is Leda. She asks no question, and her floods end on a command or a telling, both per her card. "The man I married" is new ("My man" was CUT by dialogue-polish).
- **I-10 "it's the landlady's purse for it, same as always" (l.32):** Grata naming herself in the third person. Valens's "The landlady's." (l.134) agrees with Ch.19 (she lets the shop) and Ch.26 (Fenn: "your landlady"). A cold reader could imagine a second landlady. Optional: "and it's my purse for it, same as always".
- **I-11 Reserved and allowance words:** "seam", "niche", "painted plaster" and "hand flat" all appear 0 times (but see WARN-04 for the gesture). "The painted door" appears 0 times; the book has 1 use (Ch.13 l.342), leaving 1. "Breathe with the earth" appears 0 times (Ch.25 used 1 of 2); the paraphrase "the doors went with the ground. When it moved hard enough, they could open." is fine. No mountain, no Vesuvius, no portent. The closing "I did not wake him." is a decision, not a plant, and has no forward reach. Fenn's rule is paraphrased in Mara's words.
- **I-12 Valens's dust (l.110), given once (guard 5 met):** ", from our ceiling" adds a plastered ceiling the chapter never shows. S1's dust comes from the wall crack, and Ch.20 has "a cracked tile over the bed". It is also a rationale clause. Optional: "There was plaster dust in his hair." Cut ", from our ceiling".
- **I-13 Mara's mender voice:** "and mended it well" (l.52) is the absent-workman verdict at 1 (cap ≤1 per chapter). "as I would a dropped pot" (l.22) is the second "as I would a [object]" after Ch.15 l.374, so rest that frame. "the way a zipper parts" is new as a comparison (Ch.4's zipper is literal). The "two lead clamps" are her own planned mend, not a mend-notice, so they do not touch the SPENT lead staple.
- **I-14 Voice, nameable-rule test:** all five Valens lines are 4 words or fewer, with no question. That is distinct, but a reader could start to state a rule. Give him one longer line in Ch.31's refuse-then-hold-the-lamp beat. Mara speaks no line in the chapter, which suits the silent run.
- **I-15 Lexical density:** fist-words 4 (l.20, 40, 146, 168), none of them Lucius's, so the WATCH is met. "hard" 6, with the post-positive ", hard" twice (l.18, l.146). ", once" twice (l.60, l.116; WARN-05 removes one). Optional: l.146 "leaned on it, hard" → "leaned his weight on it".
- **I-16 Kneading at home vs Ch.29 l.12's daily loaves:** compatible (hearth cakes under a clay bell) but unexplained, as the writer report notes. Leave it.
- **I-17 Honey cake on the shrine (l.138):** a word echo of Ch.29 l.548 (honey cakes for Cerdo). It is not a guard item, and the Lares offering is period-true.
- **I-18 The woman "with a hen clamped under one arm" (l.66):** kin to Acca's hen in the crook of her arm (Ch.23 l.22). She is a different walk-on. Acceptable at one.
- **I-19 The cookshop man (l.74, l.168):** ENTITY has a "cookshop above the bull's-head fountain" whose cook was Mara's Ch.20 customer. The tracker should log this man as distinct (the bible already does). If the writer meant the same man, "A man in a cookshop door" is wrong.
- **I-20 Dogs setting each other off (l.12):** kin to Ch.20 l.271 ("a dog barked, and another answered it"). Fine at one; rest it.
- **I-21 The tomb shard's negations** ("Nothing in it altered.", "No breath moved out of it.", "No colder."): designed denial, and the negation-pivot gate is at 0. Fine.
- **I-22 Grata-through-the-wall as a situation** (Ch.26 raps, Ch.28 husband's line, Ch.30 S2): a motif of situation, which is allowed. Rest it in Ch.31.
- **I-23 Ch.31 forward guard:** Ch.30 has spent Grata's lime price, the plasterer queue and her husband sleeping through the shake. Ch.31's mid-complaint opener should take the outline's subjects (dice debts, Secundus). No trestle-for-ladder swap back: the ladder is still Ch.31's alone.
- **I-24 Ch.29 guards 1–8: all met** apart from the items above. Hook IN MEDIAS RES / pull DECISION POINT. No Saturnalia callback (no cap, cup, jug, king, wreath, pits, lesson or ball; no Cerdo delivery). The family laughs and Mara does not. Her relief takes no spent channel (it comes through the full breasts and the side stitch). None of Ch.19's threshold staging is used verbatim. Dust is given once. The entry has no count. No portent. Command echo 0: "Get your finger out of my wall" gets no compliance, and "You keep off that hearth" is disobeyed at l.158, which is not an echo. Item-look 0, without-looking 0, "kept … to itself" 0, "curled up" 0.
- **I-25 Outline/ENTITY wording:** outline Ch.30's premise and ENTITY's mara-reyes Ch.30 location row say "kitchen". Canon is "the hearth corner of the back room (party wall with Grata)". Patch both.

---

## SUGGESTED YAML PATCHES (for the entity-tracker's Ch.30 UPDATE, after the editor's fixes)

```yaml
suggested_patches:
  - entity: "flags.CH20-7 (valens.knowledge_gap / knowledge_index.door_location)"
    action: "remove_conflict"
    reason: "Ch.30 l.110-l.118: Valens follows her out of the Nuceria Gate, sees her hand on the door, reads the name, asks nothing. l.114 confirms the pre-Ch.30 state (door known, place untold). The forward window closed clean; RESOLVED."
  - entity: "valens.knowledge"
    action: "add"
    value: { fact: "the tomb itself: Eros's painted door outside the Nuceria Gate", learned: "ch-30 (l.110-l.118)", method: "witnessed; read the name" }
    reason: "planned row (outline:ch-30 2a) now on the page"
  - entity: "cobblers-shop.facts"
    action: "update"
    value: "back room: hearth with a shelf, water jar and clay bell; a beam; the hearth wall is the party wall with Grata, mended after AD 62 and split beam-to-hearth on the old repair in Feb AD 77; plugged with Grata's rag (top) and Valens's straw (bottom). Floor material: boards (ch-26 l.22); keep Ch.30 neutral (WARN-01)."
    reason: "new page facts; avoid recording 'earth' if WARN-01 is applied"
  - entity: "objects.maras-satchel"
    action: "update"
    value: "hangs on a nail at home (ch-30 l.176); Fenn's letters on top, the notebook beneath"
  - entity: "objects.tremor-notes"
    action: "update"
    value: "second staged entry, Feb AD 77: '*Mid-morning. Hearth wall split down the old repair.*' / Eros line (wording per WARN-03); first entry naming Eros; Valens not recorded"
  - entity: "nuceria-gate-tomb.facts"
    action: "update"
    value: "Feb AD 77 after the shake: sun on the leaf since morning; under it the same faint coolness, no colder; no draught, dust at its foot undisturbed; Valens witnesses (ch-30 l.86-l.118)"
  - entity: "timeline row 30"
    action: "update"
    value: { time: "one day, mid-morning to night", season: "winter (February)", year: "AD 77" }
  - entity: "mara-reyes.locations ch30"
    action: "update"
    value: "back room (hearth corner) -> street east, Nuceria Gate, the tomb -> home; travel_noted: true"
  - entity: "new walk-ons (no card)"
    action: "create"
    reason: "the cookshop man (distinct from the Ch.20 cookshop above the fountain unless the writer says otherwise); the plasterer and his boy; the two old men on the fuller's bench; the dyer's wife; the girl of nine; the boy in the gate passage; the wine seller"
```

## Bible sync notes (for the evaluator's consolidated list)
- Ch.30 walk-on block: move "telling the snakes about her roof" to CUT if WARN-06 is applied. Writer's note "*Eros: the same.*" → the new wording.
- Add to the CUT log of the At-risk after Ch.30 block: "the look he gave a ford once the mules were over it"; "and hung, turning, where the light-well sent its slant down"; "and started before we were in earshot"; "His lips moved on it once, without sound."; "with no memory of crossing the room"; "and the rag let most of it through"; "I bore down with palm and fingers together".
- Candidate CLOSED row for `tools/closed_ledger.tsv`: the "the look [he/she] (gave|kept for) a/an …" frame (3 uses: Ch.16, Ch.25, Ch.30 as found).
