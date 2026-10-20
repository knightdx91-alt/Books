# Continuity Audit: Chapter 16 (run 2, per-chapter drift audit)

**Date:** 2026-10-20
**Mode:** MANUSCRIPT AUDIT. Ch.16 "Plautia" (post-disruptor) is checked against:
- Ch.1–15 as they stand on disk;
- ENTITY_STATE.yaml as of Ch.15 (read only; the tracker update is running in parallel and this audit does not touch it);
- outline.md (Ch.16 as restaged; Ch.17, Ch.18 and Ch.22 for the handoff), foundation.md (§3, Plautia's card, §9, §10), voice-dna.md, character-bible.md and voice-bank samples 01–13;
- the STATE.yaml guardrails and resolved_author_decisions (AUTHOR-CP3-3 in particular).

**Chapter reviewed:** `manuscript/chapters/chapter-16.md`
- **Length:** **7,626** prose words by shape_check (7,632 style; 8,199 `wc -w` with the header). The floor is 7,100, so there are **526 words of headroom**. The recommended CRIT and WARN fixes come to about **−76 net** (about 7,550; see the word ledger).
- **Shape:** dialogue **43.8%** (band 40–50). 6 breaks, 7 sections, alternating C1/D1/C2/D2/C3/D3/C4. Median sentence 15 (gear mid). `dialogue` → `question`. All of this matches the ledger row.
- **Citations:** `l.NN` is the file line in chapter-16.md. Lines in other chapters are cited as `ChN l.NN` or by ENTITY paragraph (`ch-NN:pNN`).

**Mechanical baseline** (`bash tools/check_chapter.sh 16`, run read only): **ALL CLEAN.**
- Style clean (simile 1.0/1k, em-dash 3); grammar 0 errors (3 reports); rhythm 0 flagged.
- Show/tell: dialogue 43.8%, no flags. Voice-wear strict clean.
- Tic gate clean (gesture classes included); echo scan 0; command echo 0.
- And-chains 6 (cap 9); credential asides 1 by gate (2 by hand: l.204 "In the lab…", l.230 "At work I would have…").
- Metaphor 1.4 fig/1k; long sentences 12.7% over 40 words. Shape audit: SHAPE CLEAN.

**My own sweeps:**
- 4–6-grams of Ch.16 against Ch.1–15 and all thirteen voice-bank samples, with stop-word-bounded grams included (one 5-gram lift the echo scan missed: W-01).
- Gaze, prop-handling and duration beats counted by hand. The gate has no gaze class, and it missed one 3-handlings-in-400-words prop.
- Felix's question openers counted against his card ("highest two-word frame 2").
- The Isthmian and Pythian cycles computed from the Olympiad count.
- The Delphi day count (D1 → D2 → D3) and the Corinth day count (C1 → C4).
- Kallia's farewell checked against Ch.5, 7, 10 and 15 and the outline restage.
- The camera, flashlight, himation and bracelet traced from their first appearances.
- An information-flow table for every speaker.

**Total findings: 55. CRITICAL: 3 | WARN: 14 | INFO: 38**

**Summary**
- **Three CRITICALs:**
  - **C-01 (history).** AD 72 is **not** an Isthmian year. The Isthmia fell in the spring of the 2nd and 4th years of each Olympiad. Olympiad 212 began in summer AD 69, so they fell in spring **AD 71** and spring **AD 73**. The error is in foundation §9 and outline Ch.17 as well as on this page (l.476). It needs an author or architect decision before the Ch.17 writer runs. Options are given below.
  - **C-02 (closed device).** The item-by-item look is reopened. It has been CLOSED since the Ch.4/5 audits and was CRIT in Ch.12. Here it appears as Valens's four-item street scan (l.286), plus three two-item gaze sequences (l.274, l.310, l.356).
  - **C-03 (forming tic).** Felix opens **ten** questions with "Is it…?" / "Is that…?". His card caps any two-word frame at 2. No earlier chapter has more than 3 such questions across all speakers.
- **Canon points the brief asked about all hold**, apart from C-01:
  - the restored proconsul and Celer back on his staff;
  - "Gaius Iulius Valens, freedman of Gaius";
  - the dowry, divorce and custody law;
  - Marcus at seven, named for his grandfather;
  - Kallia's covert farewell, with the himation made hers by labor and the broom hung up;
  - the lamp frame;
  - the flashlight near its end;
  - the bracelet anchor;
  - no line noticing the pregnancy gap;
  - foreshadowing 0;
  - Valens never compares.
- **CH12-2 and CH12-8 are SETTLED on the page:**
  - The record is two waxed boards (a leaf) cut from the magistrate's cord-bound, double-sealed book.
  - "Valens" is his own name. Lupus is the arena name.
  - Outline Ch.17 still says "bronze-and-wax diptych" (W-14).
- **The WARNs are mostly drift the gates cannot see:**
  - a sample-13 lift (W-01);
  - Felix knowing about the sword with no knowledge path (W-02);
  - Parnassus casting an evening shadow onto the gulf, which geography does not allow (W-03);
  - "a whole winter without my name" against Ch.7 (W-04);
  - a one-day slip in the boat date (W-05);
  - a prop handled three times in 110 words (W-06);
  - per-character beats repeated inside the chapter (W-07);
  - four body-part rulers (W-08);
  - the porch dog over its bible cap (W-09);
  - a Valens gaze cluster (W-10);
  - two plausibility gaps about Celer's reach (W-11, W-12);
  - an unattributed exchange with a dropped question (W-13);
  - the Ch.17 handoff (W-14).

---

## Scorecard by category

| Audit | CRIT | WARN | INFO |
|---|---|---|---|
| History / world rules (Corinth AD 71–72) | 1 (C-01) | 3 (W-03, W-11, W-12) | 12 |
| Characters (Plautia, Marcus, Kallia, Felix, Myrrhine, Valens) | 0 | 1 (W-04) | 8 |
| Timeline | 0 | 1 (W-05) | 2 |
| Information flow | 0 | 1 (W-02) | 3 |
| Objects (himation, camera, flashlight, bracelet) | 0 | 1 (W-06) | 5 |
| CH12-2 / CH12-8 | 0 | 1 (W-14, handoff) | 1 |
| Pregnancy gap (AUTHOR-CP3-3) | 0 | 0 | 1 (clean) |
| Voice drift / NO TICS | 2 (C-02, C-03) | 6 (W-01, W-07, W-08, W-09, W-10, W-13) | 6 |
| Foreshadowing | 0 | 0 | 1 (clean) |

---

## PRIORITY: ENTITY_STATE conflicts (processed first)

There are 33 UNRESOLVED conflicts in ENTITY_STATE.yaml (Ch.1–15). Ch.16 touches these:

| ID | Ch.16 effect | Verdict |
|---|---|---|
| **CH12-2** (form of the archive record) | **SETTLED by the page.** "it is boards, not a roll" (l.538); "A cord. Through holes at the back edge, and knotted, and the knot sealed." / "His, and his colleague's." (l.542; l.546); "You want two of its boards. The leaf with your name on it is near the front … two boards that close on each other with the writing inside; once the cord is cut they come away together" (l.554). One value survives: a leaf of the magistrate's book. Ch.15's "that book in my hand" gives way, in-scene, to Plautia's "You cannot have the book, Valens." (l.538). | Tracker may mark **RESOLVED (by the page)**. The outline Ch.17 "bronze-and-wax diptych" must be patched (W-14). |
| **CH12-8** (which name is written) | **SETTLED by the page.** "It will say Gaius Iulius Valens, freedman of Gaius, set free by his master before the magistrate of the games and before the emperor, with the witnesses' names under it, and the day." (l.554); "Iulius," / "The lanista's," … "I had it with the sword." (l.558; l.560); the benches knew him as Lupus (l.524). This agrees with Ch.12's "I gave them Valens" (ch-12:p97) and with the Ch.9 notice "answering to the name Lupus" (Ch9 l.352), since Celer's slave claim uses no freedman's name. | **RESOLVED (by the page)**. Ch.22's "his own name" = Gaius Iulius Valens. |
| CH15-6 (pregnancy forward constraint) | No line notices the months without a child. "most nights since July" (l.14) is not a remark (I-19). | Holds; still open, low (forward). |
| CH5-3 (unscheduled frame) | Ch.16's frame is the **scheduled** named frame (Kallia's lamp, l.268–274). | Unchanged. |
| CH10-6 (when Ariston left) | "He has written once … in more than two years." (l.186) does not date his departure (I-24). | Unchanged. |
| CH12-4 (sailing season) | The autumn crossing (l.388) is inside the open season. It does not touch "the first boats of the year". | Unchanged. |
| CH15-9 (Kallia's jars) | The jars are not mentioned. | Unchanged. |
| CH11-4, CH12-5, CH15-10, others | Not touched: no watch, no sender named for the road men, no talk of the camera's provenance. | Unchanged. |

**New conflicts for the tracker** (see the YAML patches):
- CH16-1: the Isthmia year (C-01);
- CH16-2: "a whole winter without my name" against ch-07 (W-04);
- CH16-3: the boat day count (W-05);
- CH16-4: Felix's knowledge of the sword (W-02, knowledge_gap).

---

## CRITICAL ISSUES (must fix before proceeding)

### [C-01] AD 72 is not an Isthmian year (history; plan-level; author decision needed before Ch.17)
- **Audit:** World rules / history (foundation §9; outline Ch.17).
- **Evidence:**
  - l.476: "**At the Isthmia,**" Plautia said, "the proconsul goes out to the god's precinct on the Isthmus with his whole staff, and the magistrates who give the games go out with him…" The plan for the coming spring follows from this (l.482: "on the second morning, at the hour the boys run"; l.516: "on the day after the boys' race").
  - foundation §9: "the **Isthmian Games** fell in spring 72"; outline Ch.17 dateline: "*(Corinth, the Isthmian Games, spring, AD 72.)*"; Ch.19 dateline "Puteoli · spring, AD 72" (ENTITY timeline). The year is therefore fixed at AD 72.
- **The arithmetic:**
  - Olympiad 1 = 776 BC, so Olympiad 212 began in summer **AD 69** (and Olympiad 211 in AD 65, which Nero moved to 67).
  - Olympic years run midsummer to midsummer, and the Isthmia were held in the **spring of the 2nd and 4th years**.
  - Olympiad 212.2 runs summer 70 to summer 71, which puts an Isthmia in **spring AD 71**.
  - Olympiad 212.4 runs summer 72 to summer 73, which puts the next in **spring AD 73**.
  - Spring AD 72 falls in year 3. **No Isthmia.**
  - The rule matches the fixed points: Isthmian games in the even BC years (412 BC, Thucydides 8.9–10), which are the odd AD years. The well-known Isthmia of AD 51, during Paul's stay at Corinth, is one of them. The Caesarea, held with the Isthmia every fourth year, do not help either.
  - Ch.15 is actually right. Felix's "When are the games at the Isthmus? This spring coming, or the next?" (Ch15 l.410) has the true answer "the next". His "the Corinthian boy won it last time" (Ch15 l.434) is the spring-71 games, a few months before.
- **ERROR or INTENT:** error. Nothing in foundation or STATE logs it as licence. The Ch.17 caper depends on it, and so does the Ch.17 title.
- **Suggested fix (choose one; the first two leave Ch.15 untouched):**
  - **(A) Licence by ruling, no text change.** Log an AUTHOR/ARCH decision ("the Isthmia are moved to spring 72 for the story; the book does not state the cycle"). Patch foundation §9 to say it is licence. Zero manuscript cost. The risk is the historically literate reader the authenticity dial is aimed at.
  - **(B) A one-off imperial festival on the Isthmus in spring 72.** Plautia's l.476 becomes "**At the emperor's games on the Isthmus**," (or "At the games for the emperor's victory,", meaning the Judaean triumph of June 71). Cities vowed and held such games, so the boys' race, the proconsul's chair, the horse fair and the empty office all survive. Outline Ch.17 is retitled and re-dated in the same words. Ch.15's "the games at the Isthmus" and "last time" (the true Isthmia of 71) stay as they are. Two words change in Ch.16. The pine crown (outline Ch.17 beat 4) should become a generic crown.
  - **(C) Not recommended: move the theft to the real Isthmia of spring 73.** That means a second Corinth winter. It cascades into Ch.18's "seventeen months", Ch.19's "ten years after the quake", Ch.20–21 and the 72 datelines.
- **Cascade:** foundation §9 and §10; outline Ch.17 (title, dateline, premise, beat 4) and Ch.18 (the "after the Isthmia" references); ENTITY `locations.isthmia` and `timeline` row 17; character-bible Plautia block ("At the Isthmia he will be…").

### [C-02] The item-by-item look reopened (a registered CLOSED device), with three two-item gaze sequences
- **Audit:** NO TICS / closed-device registry.
  - character-bible At-risk after Ch.1: "a third use anywhere in the book is a defect".
  - At-risk after Ch.5: "item-by-item look … CLOSED".
  - At-risk after Ch.13: "the item-by-item gaze … stays CLOSED".
  - The Ch.4, Ch.5 and Ch.12 audits each treated it as CRITICAL. Ch.12's C-01 defines the device as "a gaze moving from item to item", with two-item forms counting (Ch.1's "from the pencil to the garbage bag").
- **Evidence:**
  - l.286 (the full device, a colon-list of four): "before it had settled he had searched the street with his eyes, both ways: **the corner behind him, the fuller's door opposite with its vats steaming in the cold, the turning beyond, the line of the roofs.**"
  - l.310: "**He studied my face, and then the band, the band for longer.**"
  - l.274: "She looked **at the thing at my face, and then past it, at her lamp**, with the look she gave a jar when a lodger had been standing too near it."
  - l.356: "Her own wrist was bare. **She saw mine before she saw my face.**"
- **ERROR or INTENT:** the CONTENT is intent. It is Valens's bodyguard habit, which the bible marks for one use ("the street searched before a woman steps down … once"), and the beat stays. The FRAME (a gaze walking an inventory) is the error. It is also a catalogue, which the NO TICS law (§3b.2) retires.
- **Suggested fix (one object or one duration each):**
  - l.286: "…and before it had settled he had **looked the street over both ways, slowly.**" Plant the fuller (needed by l.342) in l.282: "I sat on the porch bench, **across the street from the fuller's door,** with the dog, which…" (−19 net).
  - l.310: "**He looked at it again, and that time he took longer.**" (0). It now pairs with l.302 "Valens looked at the band, not long."
  - l.274: "**She looked at her lamp,** with the look she gave a jar when a lodger had been standing too near it." (−10). The camera goes unremarked, which serves the outline better: "does not ask".
  - l.356: "Her own wrist was bare. **She saw the band on mine.**" (−2).
- **Cascade:**
  - Valens's C3 gaze count drops (see W-10).
  - "the fuller's" stays planted for l.342.
  - The bible's "Spent in Ch.16" line for Valens ("the street searched before a woman steps down") stays true.
  - Check the new l.286 against "looked the street" in Ch.1–15. My grep found 0.

### [C-03] Felix's "Is it…? / Is that…?" opener at five times his card's cap: a catchphrase shape forming
- **Audit:** NO TICS (speech habits). The FELIX card, WATCH for Ch.12+, says "question openers are rotated (highest two-word frame 2…); keep rotating". Ch.11's dialogue-polish cut his "Is it…?" from 7 to 2 for exactly this reason. In Ch.11–15, *all* speakers together used "Is it/Is that…?" at most 3 times per chapter (3, 2, 1, 0, 3). Ch.16 has 11, ten of them Felix's.
- **Evidence (Felix):**
  - "Is it every week?" (l.20)
  - "Is that gold? … Is it real?" (l.298)
  - "Is it heavy?" (l.314)
  - "Is it the one?" (l.318)
  - "Is that why they're making that noise?" (l.396)
  - "Is it hers?" (l.418)
  - "Is it gold?" (l.450)
  - "Is that the town, though? Is that Corinth?" (l.454)
  - That makes "Is it" ×6 and "Is that" ×4. He also asks "gold" twice (l.298, l.450).
- **ERROR or INTENT:** his stacked questions are his card's syntax. One frame carrying them ten times in one chapter is a tic, the same species as Ch.11's C-01 (Valens's bare "No.").
- **Suggested fix (to "Is it" 2, "Is that" 2, "gold" once):**
  - l.20: "**Every week?**" (−2)
  - l.298: "**Real?**" (−2; keep "Is that gold?")
  - l.314: "**How heavy is it?** What would it buy? Would it buy a mule?" (−2; this drops the doubled "heavy")
  - l.318: see W-02, which replaces "Is it the one?"
  - l.450: "**Is there gold up there?** Do they let boys up?" (+1)
  - l.454: "**That's the town, though? Corinth?** Which way's the ship road, that they haul them over on?" (−3)
  - Keep l.396 "Is that why…" and l.418 "Is it hers?".
- **Cascade:**
  - "Who's/What's" openers rise slightly. They stay under 2 per frame.
  - Re-run `tic_report.py`. The bible's FELIX Ch.16 block must list his rotated openers. Ch.17 is a WATCH: no "Is it" opener at all.

---

## WARN ISSUES (should fix)

### [W-01] A 5-gram lift from voice-bank sample-13 (the Ch.19 camera register), which the echo scan missed
- **Evidence:**
  - l.268: "I lifted **the camera out of my** clothes by its strap."
  - sample-13 l.4: "I took **the camera out of my** bag. I had twenty-two frames left."
  - The same sentence also carries sample-05's "by its strap". That 3-gram is permitted only at Ch.12 by ruling: "do not recur in a fight or a steadying beat". This is neither, but it stacks two sample strings in one camera sentence.
- **Why it matters:** voice-dna §6: "No sentence, image or line from any sample may be reused." Sample-13 is the reserved register for Ch.19's declined photograph, so the camera-out-of-the-bag frame should reach Ch.19 unspent.
- **Fix:** "**I drew the Pentax up from inside my chiton.**" (−1). The phrase has 0 hits in Ch.1–15 and the samples.

### [W-02] Felix knows Valens won his sword in Corinth's arena; no knowledge path on the page
- **Evidence:** l.318 Felix: "Is it the one? Where you got the sword?" and l.322: "Will you show me where you stood? Not in it. Only the gate."
- **Against:** ENTITY `felix.knowledge_absent_ch11–ch15`: the name Lupus and "the arena past" are not known to him. The bible's Ch.15 FELIX block: "nothing of the arena past, Lupus, the truth or Pompeii". The only Ch.15 datum is Valens's evasive "Once or twice" (he has *seen* fights at Corinth; ch-15:p192–193).
- **Plausible off-page:** a winter in the brother's house, where the porter, the cook and the stable all knew Plautia's sworn bodyguard. So this is WARN, not CRIT. But the reader meets his knowledge with no source, in the same breath as "The man at the stable says…".
- **Fix (also clears one C-03 opener):** l.318 end: "…and the whole forum hears it. **He says that's where you got your sword.**" (−1). Valens's "There's only the one." (l.320) still deflects.
- **Cascade:** ENTITY `felix.knowledge` row (learned Ch.16, told_by: the brother's stableman, off-page; he knows the arena past but not Lupus, the frame or the notice unless Ch.17 says so). Ch.21 ("The Wolf's Old Name") inherits that Felix already knows Valens fought.

### [W-03] "the shadow of Parnassus" cannot reach the gulf at evening
- **Evidence:** l.106: "…while **the shadow of Parnassus crept across the olives and the plain and settled at last on the gulf.** When it touched the water there were lamps in Kirrha."
- **Why:**
  - Delphi sits on Parnassus's south flank. The plain and the gulf at Kirrha/Itea lie south-west of it.
  - An autumn evening sun sets in the WSW, so Parnassus's shadow falls ENE, away from the plain.
  - The evening shadow comes over the gulf and plain *from the western mountains* and climbs toward Delphi.
- **Fix:** "…while **the shadow of the western mountains came across the gulf and the plain and up through the olives.** When it reached the cliff foot there were lamps in Kirrha." (+2)

### [W-04] "She went a whole winter without my name" against Ch.6–7
- **Evidence:** l.194: "**She went a whole winter without my name.**"
- **Against:**
  - Ch.6 (November 70): "Kallia has not asked it" (Ch6 l.232).
  - Ch.7: she asks at the registration, "Say your name for me." / "Maira. The water." (ch-07:p180–p182). Ch.7 closes before Ch.8's midwinter.
  - She had Mara's name roughly two to three months after the Boathoos arrival, and before midwinter.
- **Fix:** "**She had me most of an autumn before she asked my name.**" (+4). The bible's Ch.16 spent list must take the new wording.

### [W-05] The boat date slips by one day
- **Evidence:**
  - D1, at night: "When's the boat?" / "**In two days**, from Kirrha, if the wind holds." (l.126; l.128).
  - D2 is the next dawn (Kallia's lamp).
  - D3: "We went over the gulf **two days after Kallia's lamp**" (l.388) is three days after D1.
- **Fix:** l.388 "We went over the gulf **the day after** Kallia's lamp" (−1). The alternative is l.128 "In three days". l.388 is the cheaper change.

### [W-06] A prop handled three times in about 110 words (the author's rule; the gate missed it)
- **Rule:** CLAUDE.md hard gates (from the author's read of Ch.1–5): "no prop handled 3+ times in 400 words".
- **Evidence:** the barley sack.
  - l.286: "He **let the sack slide to the paving**".
  - l.292: "then **carried the sack up the step**, and saw me, **and let it drop again**".
  - That is three handlings: down, up, down. (Felix's sack at l.298 and l.326 is a different prop.)
- **Second instance, borderline:** Kallia's lamp.
  - l.110: "holding the lamp low";
  - l.116: "**Kallia set the lamp on the woodstack.**";
  - l.148: "carried it into her own room, and the lamp with it";
  - about 330 words in all.
- **Fix:**
  - l.292: "He watched the empty turning a while, then **came up the step, and saw me.**" (−8). The sacks stay on the paving for "Take the sacks round."
  - Cut l.116's last sentence (−7).

### [W-07] The same beat twice or more for one character inside the chapter
- **Rule:** voice-dna dialogue conventions: "no character gets the same beat twice in a chapter". The bible's Myrrhine card: "Lupins are her food, once per scene at most". The at-risk list caps "said to the [non-listener]" at 1 per chapter.
- **Evidence (Plautia's eyes to an object):**
  - l.56 "She looked at the brazier.";
  - l.80 "Her eyes left the coals.";
  - l.242 "She looked at the gold in my hand, not at me.";
  - l.366 "She looked at the gray gap of sky.";
  - l.586 "She asked it of me, and not of the coals".
  - That is five, and the last turns the closing paragraph on the same gaze.
- **Evidence (Myrrhine):**
  - l.88 "said Myrrhine, in Greek, **to her lupins**", which is a second lupin beat in C1 after l.18;
  - l.228 "and **split one** with her thumbnail and ate it";
  - l.492 "Myrrhine **split her next lupin** so hard…", the split repeated.
- **Fix (closing paragraph untouched, so the hook-craft/disruptor md5 guard stands):**
  - cut l.366 "She looked at the gray gap of sky." (−8);
  - l.242 "She looked at the gold in my hand." (−3);
  - l.88 "said Myrrhine, in Greek, **from her stool**." (0; this also clears the non-listener count);
  - l.228 "Myrrhine returned to her stool and her lupins, **and ate one,** and watched the curtain." (−5; this also removes a thumbnail).
  - The coals stay at three (l.56, l.80, l.586), a situation inside the chapter, not a book device. They must not follow Plautia into Ch.17 or Ch.22.

### [W-08] Four body-part rulers: a measuring device forming
- **Rule:** the bible SPENT list has "the size of a fingernail" as a ruler. NO TICS §3b.2 retires quantifying as a device, and the disruptor already cut this class from 7 to 4.
- **Evidence:**
  - l.110 "stood open **the width of a hand**";
  - l.204 "**the breadth of a fingertip**";
  - l.260 "a hole **I could have pushed a fingertip into**";
  - l.260 "for **the last hand's breadth**".
- **Fix:**
  - l.110 "Kallia's gate **stood ajar**." (−5);
  - l.260 "…and then, **at the very end**, small again." (0).
  - That leaves two: the bracelet's breadth, which is the anchor's measure, and the pin hole.

### [W-09] The porch dog over its bible cap in C3
- **Rule:** the Ch.16 walk-on note in the bible: "Texture; not a device (one appearance per section at most)."
- **Evidence:** C3 has the dog on her foot (l.282), "The dog is lying on the dry one." (l.296), "Fill the dog's bowl" (l.316), "the dog followed for the bowl's sake" (l.326), and "**The dog came back without Felix and sat in front of us and watched the bread.**" (l.352).
- **Fix:** cut the l.352 dog sentence (−17). The bowl beats can stay as one errand.

### [W-10] A Valens gaze cluster in C3 (6 beats in about 600 words)
- **Evidence:**
  - "searched the street with his eyes" (l.286);
  - "watched the empty turning" (l.292);
  - "looked at my face" (l.292);
  - "looked at the band" (l.302);
  - "studied my face, and then the band" (l.310);
  - "He watched the lane end of the street" (l.342).
- **Rule:** the tic gate has no gaze class. By the gesture rule's own measure (3+ of a class inside 500 words) this fails by hand.
- **Fix (with C-02):** l.342 "I went for barley." **Down at the lane end the fuller's boy was carrying out a vat of something that steamed.** "The porter…" (0). That leaves 4, three of them load-bearing (the turning, her face, the band).

### [W-11] Valens walks Corinth openly under a posted 500-drachma notice, and nothing on the page registers it
- **Evidence:**
  - l.338: "Near the forum." He has scouted the record office's two doors and bought bread from a baker who "said I had the look".
  - He has lived three months in the brother's stable rooms (l.556).
- **Against:**
  - the Ch.9 notice, "Copied from the notice posted at Corinth" (Ch9 l.352);
  - Celer "kind to those freedmen all winter" and dining with the proconsul (l.60; l.76);
  - Plautia's own premise that men from the benches will know "Lupus" (l.524).
- **Mitigation:** Ch.15's "Celer's men chose a road for it" implies Celer will not act in a town, under a house with standing. One clause would close the gap.
- **Fix:** l.338 "Near the forum. **The freedman walked with me.**" (+5). This is plain, uncompared and on Valens's axis.

### [W-12] A night meeting with Valens in Plautia's rooms, in a house whose kitchen talks to Celer's
- **Evidence:**
  - l.476: "It was late, the shutters were barred, and her brother was home from Patrae and asleep in his own rooms."
  - Valens is inside her door (l.480).
  - Her C1 line shows the leak: "Our cook has a cousin in that kitchen." (l.76).
  - The suit turns on adultery with this very man. A night visit would hand Celer the retention argument (*propter mores*).
- **Fix:** add the brother's freedman: "It was late, the shutters were barred, **her brother's freedman sat outside on the stair,** and her brother was home…" (+8). It also seeds Ch.17's go-between.

### [W-13] An unattributed exchange with a dropped question
- **Evidence:**
  - l.498 "What goes in the purse?" (untagged);
  - l.500 Plautia: "My mother's silver … **What would you give?**";
  - l.502 "And while he is fetching it?" (untagged; it ignores her question).
- **Why:** the cover-the-name test cannot tell whether l.498 and l.502 are Mara's or Valens's, and Plautia's question hangs unanswered as if a line were lost.
- **Fix:** l.498 "What goes in the purse?" **said Valens.** (practical, his axis; +2). Cut "What would you give?" (−4). l.502 "And while he is fetching it?" **I said.** (+2).

### [W-14] HANDOFF to Ch.17: the outline still carries the old record form, and Celer's whereabouts are now fixed by Plautia
- **Evidence:**
  - outline Ch.17 beat 1: "**The bronze-and-wax diptych.**" The page (l.538–554) now has two waxed **wooden** boards cut from a cord-bound book, with the knot sealed by the magistrate and his colleague.
  - l.476 puts "the boy's father" in "the second row behind the governor's chair", out at the Isthmus. Outline Ch.17 beat 3 puts Celer face to face with Valens "in the colonnade".
  - l.534 leaves Valens's post open: "We will speak of the door when my brother has spoken to the baker."
  - l.482 names the two possible clerks: "the young one, who drinks, or the gray-haired one, who does not". Outline Ch.17's anchor clerk eats figs.
- **Fix:** patch outline Ch.17 beat 1 to "the two-board leaf, cut from the magistrate's book (cord; two seals; Mara's re-sealing good only past a drinker, l.552)". Add a note that Ch.17 must show why Celer has left the Isthmus, and that the fig-eating clerk is one of l.482's two. The festival name follows C-01. ENTITY `objects.manumission-record.description` takes the page form (YAML patch).

---

## INFO (polish / tracking / cascades)

**History and world rules**
- **I-01 Vespasian's revocation of Achaea's freedom.**
  - Nero proclaimed the freedom at the Isthmia of 28 November 67.
  - Vespasian's revocation is undated in Pausanias 7.17.4 and Suetonius *Vesp.* 8.4. Modern dates run from c. 70 to 73/74; Jerome's chronicle lists the provincial reductions under c. 73–74.
  - The book's "a proconsul again by 71" (foundation §9) is at the early edge and defensible.
  - The page states no year: "Since the emperor took back from this province what Nero had given it" and "now that Corinth has a proconsul to be among" (l.60). No change.
- **I-02 The record office is plausible, and its placement is good.**
  - The colony's books moving into the proconsul's office, kept by his freedmen, is invented. Mara flags it in-scene ("The governor's? Not the colony's own?", l.58).
  - "at the end of the long colonnade, across the forum from the old temple" (l.338) matches the South Stoa and its east end, where an archive building is often placed, across from the archaic Temple of Apollo. No change.
- **I-03 The form of the record is plausible.** A magistrate's year kept as a codex of waxed boards, bound by a cord through holes and sealed at the knot, is consistent with sealed *tabulae* practice. Mara's limit ("So that it slips past a drinker", l.552) keeps the theft honest. This settles CH12-2.
- **I-04 Freedman naming is correct.**
  - "Gaius Iulius Valens, freedman of Gaius" is C. Iulius C. l. Valens: the master's praenomen and nomen, his own name as cognomen.
  - A lanista called Gaius Iulius is very plausible in Colonia Laus Iulia Corinthiensis, refounded by Caesar with freedmen colonists.
  - Legal footnote (no fix; keep Ch.22 off the point). Under the lex Aelia Sentia, a slave freed under thirty without a *consilium* became a Junian Latin, and Valens was about 29 in 67. A slave consigned to a gladiatorial school as punishment became a *dediticius* (Gaius *Inst.* 1.13). The citizen-style name is a licence that most readers will not test. Ch.22's trial must not argue status.
- **I-05 Dowry, divorce and custody are correct.**
  - The son stays in his father's *potestas*: "in his father's house, where the law says he must be" (l.52).
  - Retention for misconduct is the motive (foundation §3).
  - Plautia's dowry instrument "with my father's seal on it" (l.496) is fine.
  - "My mother's silver" (l.500) is her own property, not dowry, so she may spend it.
- **I-06 A woman's standing through her brother.**
  - The *actio rei uxoriae* belongs to the wife once she is *sui iuris* (her father is dead: "a daughter of my father", "once dined at my father's table", l.496).
  - After the lex Claudia, a brother is no longer a woman's statutory tutor, so he acts as her representative (*cognitor/procurator*).
  - The page is consistent ("This house wants the same leaf, for the suit", l.56; "before a judge the praetor gives us", l.572).
  - Ch.22: keep Plautia as the formal party, the brother as her man of business.
  - "at Patrae … about the suit" (l.48) is apt: Patrae was the port for the Italy crossing.
- **I-07 "consul two months in a bad year" (l.366) is plausible.**
  - AD 69's suffects held two-month terms under Otho's schedule, so a "bad year" with two-month consulships points naturally to 69.
  - Be aware: a real Arrius, Gnaeus Arrius Antoninus, was suffect in 69. A literate reader may connect Celer's nomen to him, and his praenomen would not give a grandson named Marcus. Nothing on the page names the year or the man, so no fix. Do not add either later.
- **I-08 Crossing and mules are correct.**
  - Equids cannot vomit: "They had no way to bring it up." (l.392).
  - The gulf's afternoon wind dying at sunset (l.410), Lechaion's moles, Acrocorinth's Aphrodite and the wall on its crest, and the straight Lechaion road are all right.
  - The diolkos lies "East of the harbor" (l.456), which is right for its western end, and agrees with Felix's Ch.15 rollers.
  - The autumn sailing comes before the November close.
- **I-09 The Pythian Games of AD 71 (Olympiad 212.3, late summer 71) are not on the page.** They fell while Mara was on the pasture above Delphi. D1's quiet autumn Delphi, with one coughing lodger, is compatible because it comes after them. This is an unused texture opportunity only, and it is too late to plant. No fix.
- **I-10 "the fuller's door opposite with its vats steaming in the cold" (l.286) and "a vat of something that steamed" (l.342).** Fullers' tubs were cold. Heated vats are a dyer's. Optional: "the dyer's door" in both places, or drop "steaming". This matters for the authenticity dial (8+).
- **I-11 Corinth's amphitheatre stands outside the city.** "the whole forum hears it" (l.318) is Felix's hearsay and can stand.
- **I-12 Mara knows "the other harbor" (Kenchreai) and Aphrodite's temple** (l.142; l.448). This is scholarly knowledge, consistent with her training.

**Characters**
- **I-13 Plautia against her card and foundation: holds.**
  - She uses no contractions anywhere (checked).
  - She never names the night and never says "Celer". "my former husband" appears once (l.76); otherwise "the man I was married to", "my son's father", "the boy's father", "that man".
  - Her periodic Latin breaks into blunt questions, one per visit.
  - She gives the bracelet away and grieves behind the curtain. A cloak is given and bought back (Myrrhine, l.224).
  - There is no rival-trope. The friendship turns on the laugh (l.378–384).
  - Thirty or a little under; Marcus "seven at the vintage" (b. autumn 64); "Twice in three years" (foundation); "I walked in front of him for two years" (agrees with Ch.12).
- **I-14 Marcus's namesake.** "For his father's father" for a Quintus's son is normal Roman practice (eldest sons often, not always, took the father's praenomen). His age is consistent with the bible card.
- **I-15 Kallia: in character.**
  - She never sits and never touches Mara. She hands Mara nothing; the himation is laid on the bag.
  - The broom's position is not described (third wording), and there is no wool work, no stopped work, no speech in D2.
  - "Whether I could carry water." (l.198) is selective; her first words in Ch.5 were "Who beat you?" / "Hands." / "Open your mouth." That is acceptable as Mara's summary.
  - "on the step of a spring" (l.194) paraphrases Ch.5's "the lip of the god's spring". Fine.
- **I-16 Myrrhine (new card) holds her axis:** resale and buy-back; no "Then…"; does not notice workmanship. See W-07 for the lupins.
- **I-17 Valens's speech has no comparisons.** "Up, now, you old fool. Up," (l.426) is to a mule. Bare "No." ×1 (l.526). His hands go to a different object each time. "I'm well here." (l.480) is not in the bible's line list; add it.
- **I-18 Felix's "I'd sooner not look at it" (l.460)** reads oddly after his Ch.15 enthusiasm for the rollers. A day's seasickness explains it, and the beat is good. Keep.
- **I-19 The pregnancy gap (AUTHOR-CP3-3): clean.**
  - No line notices or explains the months without a child.
  - "I had had my palms on the ridges of it most nights since July." (l.14) is not a remark.
  - Plautia's nursing story (l.244) and "Ours" for Felix (l.368) imply nothing.
- **I-20 Foreshadowing 0; AD 79 0.**
  - Every forward-tense line is in dialogue and is a plan or a joke: "He will find out in the spring." (l.382); "you will be on a ship out of Lechaion" (l.516).
  - Narration stays at the moment. Its counterfactuals ("a fingernail would have marked it", "At work I would have measured them", l.230) are past-facing.
  - No retired reflex was found: no closing aphorism, no device button, no define-by-negation opener.

**Timeline**
- **I-21 The Corinth clock holds.**
  - C1 "the winter is half gone" comes after the Saturnalia, with the Kalends of January already past (l.162).
  - C2 is "four mornings after"; C3 is "the end of that month" and "Two days ago" for the bracelet; C4 comes after the brother's ten days at Patrae.
  - Arrival with "the first of the autumn rains" (l.20) against Ch.15's "Before the rains" is close enough: they arrive in drizzle (l.472).
  - "three months" by the porter's account (l.556) is consistent.
- **I-22 "He has written once … in more than two years" (l.186)** is true but loose. He was silent from the vintage of 68 and one letter came in early 71, so by winter 71–72 the span is three-plus years. Optional: "in more than three years". It does not settle CH10-6.

**Information flow**
- **I-23 What Mara understands.**
  - She loses fast periodic Greek and follows slow book Latin. Her spoken Latin is stiff, "each ending sounded to its last letter" (l.34). Myrrhine follows Latin "that much".
  - All of this agrees with foundation ("reads … well and speaks neither") and Ch.6–7 (Valens's Latin is for mules; Mara has spoken Latin to no one).
  - A nuance, no fix: a reader of Attic might follow literary Greek better than village Phocian. The page puts the loss on speed, which is fair.
- **I-24 What Plautia knows of Mara.**
  - From the brother via Valens: the Syracuse upbringing, that she reads and writes both languages, that she is his wife.
  - From the morning itself: she is his lover ("Yes." / "Good,"). Mara concedes the Latin is not Syracusan ("No.", l.38) and Plautia covers for her ("Speak Greek in front of him.").
  - She knows nothing of the door, 1998 or Pompeii. **Track:** Plautia now holds a soft doubt about the Syracuse cover.
- **I-25 Kallia's "When's the boat?" (l.126).** Mara never told Kallia about the Corinth bargain on the page (it was made on the pasture). Kallia may infer it, since she invented the boat, or Valens may have stopped at her gate by daylight. A path exists, so this is not a gap.

**Objects**
- **I-26 The himation.**
  - It is Ch.7's "girl's" wet-sand-brown himation, pinned at the shoulder (Ch.8). It is given back folded and made Mara's by the night's mending.
  - "the darned corner" (l.146) is a new fact; no darn is on any earlier page (Ch.8 only cracked it). Fine.
  - It is with her on the boat (l.404).
  - The fold "lengthwise and then across" is the third fold-in-four act book-wide. The phrase "folded in four" is CLOSED and not used. Fine.
- **I-27 The camera and frame count.**
  - Kallia's lamp is the **named Ch.16 frame** (outline; foundation §4f). The counter is not mentioned. No cap, which agrees with Ch.12.
  - **Plan count:** 8 frames in 1998 + the Kroton base (Ch.5) + the lamp = **10 shot, 26 left** including frame 36. **Page count:** at least 9 shot, at most 27 left.
  - The remaining scheduled frames are Ch.20, Ch.26, Ch.27 and frame 36 (Ch.38), so **22 are unscheduled, off the page**.
  - Voice-bank sample-13 (calibration only) has "twenty-two frames left" at Ch.19. If Ch.19 ever prints a count, it implies 4 off-page frames between Ch.16 and Ch.19. That works, but the writer must count from 26.
  - "a crack of light beside it where the shutter was ajar" (l.270): with Kallia in the lean-to and the lamp on the outer sill, the light in the crack is unexplained. Optional: "a crack of gray".
- **I-28 The flashlight is consistent with Ch.15.**
  - "a poor brown light, browner than in the cave, and it shrank as I held it on them" (l.416). Ch.15 had a brown edge and no batteries to buy.
  - This is **Felix's first sight** (bible). The boat's master and the steering boy may also have seen a flameless light at night; the page does not say. If Ch.17 or Ch.18 uses the boat crew, nobody remarks on it.
  - "turned it off while it still had something left" (l.426): its next use, if any, must be brief and may fail.
- **I-29 The bracelet.** It goes on the **left** wrist ("It was made for the left.", l.248) and Mara keeps it (l.308–312). The Seiko is with Valens until Ch.18. When it comes back on the quay, both sit on the left wrist; Ch.18 may note it or choose the right for the watch, but it must not contradict.
- **I-30 The potted fig.** It rides "roped to the foot of the mast in its jar" (l.388) as texture only. Foundation's "moves it twice" is no longer literal: it has gone up the mountain, down, and across the gulf. Tracker note only.

**Voice / NO TICS (below WARN)**
- **I-31 "the middle of the night" (l.410)** is a 4-gram from sample-06. It is idiom, but samples are calibration only. Optional: "Well after midnight I woke…"
- **I-32 Plautia's consecutive paragraphs (l.84 → l.86).** Mara's "To see what?" gets Plautia's answer, and a new paragraph opens on Plautia again with no beat between. Optional half-line beat for Mara.
- **I-33 Plautia describes the binding** ("A cord. Through holes at the back edge…", l.542). This is Mara's axis (joins), but it is answered to Mara's question, so the bleed guard holds.
- **I-34 The duration family** ("for a little", "for some while", "for some time", "a while", "in a while": 5) is under the gesture cap for a long chapter. WATCH in Ch.17.
- **I-35 "rude to me about a woodstack" (l.168).** Ch.6 shows only "Who showed you that?" (Ch6 l.124). This is Mara's joke in Latin, which is fine.
- **I-36 l.282 "two of her brother's slaves".** "her" grammatically points to Myrrhine. Optional: "two of the brother's slaves".

**Bookkeeping**
- **I-37 The bible's Ch.16 blocks quote the pre-polish draft.**
  - "Then you are the first," is now "That would make you the first," (l.98).
  - "You said the Gaius as though somebody might take it back." is now "You said the Gaius quickly, in case somebody should take it back." (l.562).
  - "Twice she had asked him to sit, and twice he had said that he would stand." is now "There is a stool, Valens," … "I'm well here." (l.480).
  - "received him with great kindness" is now "with every kindness" (l.72).
  - The porter's "a man with a stool and a tablet…" is not on the page.
  - "the mosaic man who laid his little stones drunk" is now "a man laying a floor … a floor laid drunk" (l.158).
  - "my son's father has been kind to each of them" is now "he has been kind to those freedmen all winter" (l.60).
  - Re-sync at finalize, together with the W-04 wording.
- **I-38 Outline Ch.16's "the answer she gets from watching, not asking."** Mara does ask ("Have you?", l.22), but the ask is deflected into Greek she cannot follow, and the answer still comes at the porch. Consistent.

---

## Word ledger (recommended CRIT + WARN fixes)

| Fix | Δ words |
|---|---|
| C-02 (l.282 plant +6, l.286 −25, l.274 −10, l.356 −2, l.310 0) | −31 |
| C-03 (l.20 −2, l.298 −2, l.314 −2, l.450 +1, l.454 −3) | −8 |
| W-01 sample-13 lift | −1 |
| W-02 Felix's source (l.318) | −1 |
| W-03 the western shadow | +2 |
| W-04 "most of an autumn" | +4 |
| W-05 "the day after" | −1 |
| W-06 sack (−8), lamp on woodstack (−7) | −15 |
| W-07 Plautia l.366 (−8), l.242 (−3), Myrrhine l.228 (−5) | −16 |
| W-08 gate ajar | −5 |
| W-09 dog and bread | −17 |
| W-10 lane-end recast | 0 |
| W-11 "The freedman walked with me." | +5 |
| W-12 the freedman on the stair | +8 |
| W-13 tags (+4), dropped question (−4) | 0 |
| **Net** | **≈ −76** (≈ 7,550; floor 7,100; ledger range 7,100–8,100) |

Dialogue share moves up slightly, to about 44%, because most cuts are narration. The first line and the closing paragraph are untouched by every fix above.

---

## SUGGESTED YAML PATCHES (for the entity-tracker UPDATE after the editor's fixes)

```yaml
suggested_patches:
  - entity: "meta.contradictions.CH12-2"
    action: "update"
    value: { flag: "RESOLVED", resolved_from_conflict: true, resolution: "settled by the page (ch-16 l.538-l.554): the record is a leaf of two waxed boards inside the cord-bound book of the magistrate who sat at the games of 66/67, the knot sealed by him and his colleague; Valens needs the two boards, not the book" }
    reason: "one value survives on the page; outline Ch.17 'bronze-and-wax diptych' to be patched (audit W-14)"

  - entity: "meta.contradictions.CH12-8"
    action: "update"
    value: { flag: "RESOLVED", resolved_from_conflict: true, resolution: "settled by the page (ch-16 l.554-l.564): 'Gaius Iulius Valens, freedman of Gaius'; the nomen is the lanista's ('I had it with the sword'); Lupus is the arena name the benches knew" }
    reason: "Ch.22 'his own name' = Gaius Iulius Valens"

  - entity: "objects.manumission-record"
    action: "update"
    value: { description: "two waxed boards (a leaf) near the front of the magistrate's cord-bound year-book in the proconsul's record office; text: 'Gaius Iulius Valens, freedman of Gaius, set free by his master before the magistrate of the games and before the emperor, with the witnesses' names under it, and the day'", was: "a bronze-and-wax diptych" }
    reason: "page form supersedes the plan"

  - entity: "valens.canonical_full_name"
    action: "add"
    value: "Gaius Iulius Valens (C. Iulius C. l. Valens); arena name Lupus"

  - entity: "objects.film-roll.frames_shot_ch16"
    action: "add"
    value: { value: 1, subject: "Kallia's lamp on her window sill at first light, slowest hand-held speed, lens wide (named frame)", running_count: { plan_shot: 10, plan_remaining: 26, page_shot_min: 9, page_remaining_max: 27 } }

  - entity: "objects.flashlight"
    action: "update"
    value: { ch16: "on the boat at night for the downed black; 'a poor brown light, browner than in the cave'; turned off 'while it still had something left'; seen by FELIX for the first time ('Where's the flame? Why doesn't it smoke?'); Valens: 'Don't spend it on mules.'" }

  - entity: "objects.plautias-bracelet"
    action: "create"
    value: { holder: "mara-reyes (left wrist, from ch-16 C2)", description: "plain gold band, the breadth of a fingertip, hinge hidden, opens along a hair-fine seam; two paired tooth marks near the clasp (Marcus's first teeth)", offers: "Myrrhine offers one, then two drachmas to buy it back", valens: "'Give it to her woman tomorrow' -> 'Wear it, then'" }

  - entity: "objects.borrowed-himation"
    action: "update"
    value: { ch16: "folded and handed to Kallia at night; mended overnight (pin hole closed into an eye with gray thread; hem turned and stitched); laid on Mara's bag at dawn: hers now" }

  - entity: "kallia.status_log"
    action: "add"
    value: { chapter: 16, status: "covert farewell; sweeps the storeroom step after Mara and hangs the broom on its nail; does not go near the stair; pinches out her lamp; LAST CHAPTER" }

  - entity: "felix.knowledge"
    action: "add"
    value: { fact: "Valens won his sword in Corinth's arena", learned_chapter: 16, method: "told_by: the brother's stableman (off-page; page source only if audit W-02 is applied)", note: "still not shown: the name Lupus, the frame, the notice" }

  - entity: "myrrhine"
    action: "create"
    reason: "new named speaker in ch-16 (card exists in character-bible.md)"

  - entity: "plautia"
    action: "update"
    value: { physical: "thirty or a little under; left earlobe torn through once, healed in two points; no earrings; face kept from the sun", knowledge_add: "Mara's Latin is not Syracusan (ch-16 l.36-l.38); Mara and Valens are lovers (l.12-l.16)", relationships: { mara-reyes: "friendship from C3 ('Come up when you like.')" } }

  - entity: "meta.contradictions"
    action: "add"
    value:
      - { id: CH16-1, severity: high, entity: "world_rules / locations.isthmia / timeline row 17", issue: "Isthmia in spring AD 72 (foundation §9, outline Ch.17, ch-16 l.476) vs the cycle: spring AD 71 and AD 73 (Olympiad 212 years 2 and 4)", flag: "UNRESOLVED" }
      - { id: CH16-2, severity: low, entity: "kallia / mara-reyes (name)", issue: "'She went a whole winter without my name' (ch-16 l.194) vs the name asked at the registration before midwinter (ch-07:p180)", flag: "UNRESOLVED" }
      - { id: CH16-3, severity: info, entity: "timeline (D1-D3)", issue: "'In two days' (l.128, D1 night) vs 'two days after Kallia's lamp' (l.388) = three days", flag: "UNRESOLVED" }
      - { id: CH16-4, severity: low, entity: "felix.knowledge", issue: "knows Valens got his sword at Corinth (l.318) with no path on the page", flag: "UNRESOLVED", knowledge_gap: true }
```

These patches are recommendations. The entity-tracker applies them on its next UPDATE, after the editor's fixes, and should re-quote any line the editor changes.
