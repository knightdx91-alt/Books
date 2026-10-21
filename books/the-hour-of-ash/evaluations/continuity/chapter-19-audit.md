# Continuity Audit: Chapter 19 (run 2, per-chapter drift audit)

**Date:** 2026-10-21
**Mode:** MANUSCRIPT AUDIT. Ch.19 "Puteoli" (post-disruptor) is checked against:
- Ch.1–18 as they stand on disk;
- ENTITY_STATE.yaml as of Ch.18 (read only; the tracker update is running in parallel and this audit does not touch it);
- outline.md (Ch.19 and its ledger row; Ch.20 for the handoff; Ch.41–43 for the reserved ending vocabulary);
- foundation.md (§3 Valens / Felix / Grata, §4f re-read architecture, §9 Campania anchors and the doors, §10 counts, §12 allowlist);
- voice-dna.md (§0 no-foreshadowing and the mountain rule, §1 anti-patterns and dialogue conventions, §6 sample-13 note) and character-bible.md (Grata, Valens, Felix, Pacuvius, the Ch.19 walk-on block, the at-risk lists after Ch.5, 8, 12, 13, 14, 15, 18 and 19);
- voice-bank sample-13 (this chapter's register sample) and every other sample;
- STATE.yaml guardrails and resolved_author_decisions (AUTHOR-END-1, CP3-3, CP3-4, CP3-5; CH18-5 open).

**Chapter reviewed:** `manuscript/chapters/chapter-19.md`
- **Length:** **8,474** prose words (shape_check). The floor is 7,900, so there are **574 words of headroom**. `wc -w`: 9,087 (comments included). Dialogue is **24.0%** (band 20–30, floor 20). 4 breaks. Median sentence 18 (gear high).
- **Ledger:** the opener is a `scene-set` ("By the twelfth morning of my marriage…"). The close is a `long-fade` (the shutters knocked into their sills, the street's supper noise, the girl singing). It is a Chronological walk: harbor → coast road with a night near Neapolis → Pompeii → the tomb roads. All of this matches the ledger row.
- **Citations:** `l.NN` is the file line in chapter-19.md. Lines in other chapters are cited as `ChN l.NN`.

**Mechanical baseline** (`bash tools/check_chapter.sh 19`, run read only): **ALL CLEAN.**
- Style: simile 1.1/1k; em-dash 0. Grammar: 0 errors. Rhythm: 0 flagged.
- Voice-wear: clean. Tic gate: clean, gesture classes included. And-chains 5 (cap 9). Credential asides 0 by gate.
- Shape audit: SHAPE CLEAN.
- `tic_report.py --echoes 19`: **0 echoes, 0 command echoes, 0 spoken-line echoes.**

**My own sweeps:**
- 4–5-grams of Ch.19 against Ch.1–18 and against all 13 voice-bank samples, including stop-word-bounded grams. Against Ch.1–18 the only hit of substance is the allowlisted phrase. Against the samples the hits are "fine mountain for vines" (mandated) and three function-word grams.
- Intra-chapter 3-grams.
- Narration-only present-tense sentences.
- Counts of the reserved ending words and the at-risk families.
- A day-by-day and night-by-night timeline of the crossing and the first four days.
- The gulf, Ionian, Straits and Tyrrhenian route.
- The bay approach (Capri / the Minerva cape → Puteoli).
- The Nuceria road's orientation and the sun.
- An information-flow table for Valens, Felix, Grata and the walk-ons.
- Felix's question bursts, counted.

**Total findings: 33. CRITICAL: 0 | WARN: 15 | INFO: 18**

---

## Summary

- **No CRITICAL.**
  - There is no hard contradiction with Ch.1–18, ENTITY_STATE, the outline or canon.
  - Foreshadowing is 0 by gate and by my reading (no banned form). "Seventy-nine" is thought exactly once (l.44).
  - The mountain is green, single-summited and never menacing.
  - **None of the reserved ending words appears**: seam 0, niche 0, "painted plaster" 0, "hand flat" 0.
  - "Where the dead go out" is used once (l.344), so the allowlist stands at **2 of 3** book-wide.
  - No line settles the children's citizenship (CH18-5).
  - END-1 is untouched.
- **History and geography are strong.** Every anchor in the brief checks out, often to a fine grain: the Alexandrian topsail, the scholae with lion's feet, the Stabian Gate bench tombs, the columellae, programmata on tombs, the shutter-groove sills, the hipposandal. There are four slips:
  - the bay crossing cannot be made in a flat calm by noon (W-02);
  - Phocis is placed at the Rhion narrows (W-03);
  - the "Only two have tombs worth the walk" count (W-04);
  - "nearly to the season" against a February quake (I-03).
- **Information flow** is sound on the plot level:
  - Valens holds Pompeii as a place and the painted-door marker, and never voices either.
  - Felix never learns the purpose.
  - Grata tells and never asks.
  - **Two narrator-knowledge slips:**
    - Mara quotes Grata's flood past the point where she says she lost it (W-01).
    - Grata "saw" a wall on another street (W-05).
- **Objects** agree:
  - camera: no frame fired, no cap, the dented ring;
  - leaf: two boards, Corinth, Nero's year;
  - knife: used on the brooch;
  - microcassette: staged a fresh way;
  - four mules; the purse.
  - **Three small physical slips:** the barred door (W-06), the fig on a boy's hip (W-07), the cobbler's leather (W-08).
- **Voice:**
  - One sample-13 lift (W-09).
  - A Grata line that winks past AD 79 (W-10).
  - "Ten years" ×7 (W-11).
  - A role label ×4 against the bible's own rule (W-12).
  - Felix's question bursts metronomic (W-13).
  - Grata's arm-touch twice in one scene (W-14).
  - Bible lag (W-15).
- **Word ledger:** with every WARN fix applied as written, the net is about **−36 words, to ~8,438** (floor 7,900). Dialogue is about **24.0%** (speech −4; narration −32).

---

## CRITICAL ISSUES (must fix before proceeding)

None.

---

## WARNING ISSUES

### [W-01] Grata's first flood is quoted in full past the point where Mara says she lost it. This is also the third use of a spent mechanism.
- **Audit:** Information flow (narrator knowledge / the comprehension rule). Voice drift (spent move).
- **Evidence:**
  - l.230 quotes the whole speech, including everything after the inns: "And work for him, there's not a man here with a beast and a back to him that's not carting, ten years we've been at it, ten years since the earth went, and the forum still looks like a builder's yard. Drink that before it cools."
  - l.232: "Her Latin had come at me broad and fast, with the ends of its words worn down, and I had lost my hold on it somewhere after the inns."
  - Fast speech also outruns her at l.64 (the mother-in-law, "of which I caught perhaps half") and at l.278 (Grata again, "lost the baker entirely").
  - The at-risk list after Ch.18 says "a speech that outruns Mara … the next takes another mechanism".
- **Problem:**
  - The book's rule (independent review Ch.6–10: "she follows slow plain speech and loses fast talk") forbids the narrator reporting verbatim what she says she did not catch.
  - The baker case is self-repairing: she gets it on the second, louder pass. The l.230 case never is.
  - Three speed-losses in one chapter, right after the Ch.18 note, make the mechanism a pattern.
- **Fix (−27, narration):** delete the l.232 sentence "Her Latin had come at me … after the inns." The paragraph keeps "The wine was hot, and the pepper in it shot up the back of my nose." "Are there rooms to be had?" / "Rooms, I said, and I've got them." still lands: she was not listening, and no claim of loss is needed. That leaves two speed-losses: the mother-in-law, and the baker as a comic repair.
- **Cascade:** none in later chapters. Dialogue rises fractionally.

### [W-02] The bay is crossed in a flat calm between sunrise and a noon departure from Puteoli
- **Audit:** Timeline / world rules (sailing).
- **Evidence:**
  - l.26: "The bay opened as the sun rose. We came past an island that stood out of the water on cliffs, and a cape with a temple on its end" (Capri and the Minerva cape).
  - l.26: "The water was so still that a fishing boat a mile off drew lines on it with its oars, and the lines held."
  - l.48: the fleet ship passes "fast, with no wind to help her".
  - l.136: "by noon we were out of Puteoli on the road east".
- **Problem:**
  - The Minerva cape to the Puteoli mole is about 19 nautical miles. A merchantman under sail needs wind and about 4–5 hours even with it.
  - After berthing, the chapter still has the landing, the mother-in-law, the clerk, the letter board and the wine in the street.
  - In a stated dead calm, arriving and being gone by noon is impossible.
- **Fix (−2):**
  - l.48: cut "with no wind to help her" (−5). The fleet ship rows as warships do, and the calm is no longer stated as lasting.
  - l.136: "by noon" → "**by the middle of the afternoon**" (+3).
  - The night "beyond the city's eastern gate" still works: about 14 km with mules, done by dusk in spring.
- **Cascade:** l.158 needs no change.

### [W-03] Phocis placed at the Rhion narrows
- **Audit:** Geography.
- **Evidence:** l.12: "until the shores pinched in at the narrows; Felix hung over the rail there. 'I could spit on the pair of them from here, Achaea to the left and Phocis to the right'".
- **Problem:**
  - Phocis's gulf coast ends well east of the strait.
  - The north shore at Rhion–Antirrhion is Locrian/Aetolian (Naupaktos).
  - The narration's "the mountains of Phocis on the other" is true for the first day only. Felix's line ties Phocis to the narrows, and nothing corrects him.
- **Fix (+1):** "and Phocis to the right" → "**and the Locrians to the right**". Felix knows Amphissa is Locrian; the Amphissan with the quail is his Ch.11 enemy.
- **Cascade:** none.

### [W-04] "Only two have tombs worth the walk" does not fit her own search
- **Audit:** Plot logic / information flow.
- **Evidence:**
  - l.202: she has already read the Herculaneum road's tombs on arrival.
  - l.296: the Stabian road has "only a few tombs".
  - l.324: "Seven or eight. Only two have tombs worth the walk." / "And the other?" / "The Nuceria Gate. Tomorrow."
  - Ch.15 (knowledge_index): she told Valens there are "tombs along the roads out of every gate".
- **Problem:** her two are evidently the Stabian and the Nuceria roads. That leaves out the grandest tomb road, which she walked the day before, and it calls the thin Stabian road "worth the walk".
- **Fix (0):**
  - "Only two have tombs worth the walk." → "**Three have tombs worth the walk.**"
  - "And the other?" → "**And the third?**"
- **Cascade:** the bible's at-risk-after-Ch.19 search line (W-15).

### [W-05] Grata "saw" Mara at a wall on another street
- **Audit:** Information flow.
- **Evidence:**
  - l.210: the pink stripe is "At the next corner" on the street in from the gate.
  - l.222: Grata's counter is "Further down, on a long straight street running east".
  - l.284 (Grata): "I saw you at that wall yesterday with your nail in it, half the street saw you."
- **Problem:** Grata was at her counter when they reached it, and no page puts her on the gate street. She can know it as gossip, which is in character, but not as sight.
- **Fix (+2):** "I saw you at that wall yesterday with your nail in it, half the street saw you." → "**I heard about you at that wall yesterday with your nail in it, half that street saw you.**"
- **Cascade:** none. "That was my cousin did that wall" still explains how she heard.

### [W-06] The bar is across the door after Valens has gone out through it
- **Audit:** Physical logic.
- **Evidence:**
  - l.264: the door between the rooms has "a bar to drop across it on the inside" (the back room's side).
  - l.244: the back room's only other exit is "a stair … to the roof".
  - l.272: "Valens and Felix had left with the string in the dark … I woke alone in a room with a door, and lay looking at the bar across it."
- **Problem:** Valens leaves through the shop, so he cannot drop the bar behind him. Nothing says Mara rose to bar it.
- **Fix (+1):** "lay looking at the bar across it." → "**lay looking at the bar leaning beside it.**"
- **Cascade:** none.

### [W-07] The fig in its jar carried on a fourteen-year-old's hip
- **Audit:** Object consistency.
- **Evidence:**
  - l.82: "Felix had the fig on his hip, jar and all."
  - ENTITY: the jar is "the bottom half of a big jar, sawn off at the shoulder and packed with earth" (Ch.11).
  - Ch.18 l.155: Valens and Mara carry it up the plank between them, one rim each.
- **Problem:** two adults carried it a day earlier in the story. One boy holding it on his hip at a clerk's table reads as a different, smaller object.
- **Fix (0):** "Felix had the fig on his hip, jar and all." → "**The fig stood in its jar at Felix's feet.**" The clerk's "And that?" still points at it.
- **Cascade:** l.246 ("Valens had the fig on the roof") is unaffected.

### [W-08] The noseband is cut from "the cobbler's leather" that the nephew took
- **Audit:** Internal consistency.
- **Evidence:**
  - l.236 (Grata): "his nephew walked in from Nola and took the leather and left me the smell".
  - l.244 / l.274: only "scraps", "crescents and tags of leather" are left.
  - l.306: "Valens was cutting a new noseband for the black out of a strip of the cobbler's leather".
- **Fix (+3):** "out of a strip of the cobbler's leather" → "**out of the one long strip the nephew had missed**".
- **Cascade:** none.

### [W-09] Voice-bank sample-13 lift: the number "sitting in my head"
- **Audit:** Voice drift (voice-bank lift; the echo gate misses it because the shared run is under 5 words).
- **Evidence:**
  - sample-13: "Seventy-nine, I thought. That was all; the number, **sitting in my head** like a coin under the tongue."
  - l.44: "Seventy-nine. It came unasked and **sat in my head**, two figures with nothing round them, while the mountain stood small and green in the glass."
- **Problem:** the sample's beat order (camera to the eye → the number lodged in her head) is mandated by the outline. The wording must not be. This is the image itself, a number resting in the head, carried over.
- **Fix (−4):** "It came unasked and sat in my head, two figures with nothing round them," → "**It came unasked, two figures with nothing round them,**"
- **Cascade:** the bible's at-risk-after-Ch.19 quote of the spent wording (W-15).

### [W-10] Grata's "for another ten years" winks past AD 79
- **Audit:** No foreshadowing (reader-irony wink in a character's mouth).
- **Evidence:** l.276: "the town won't, so there it'll stand on its sticks for another ten years."
- **Problem:**
  - Spoken in spring 72, the line fixes a horizon in 82. Every reader with Vesuvius in mind hears the irony.
  - The outline's subversion is explicit: "The only ominous thing is that she declines to take a photograph."
  - Earlier audits treated a wink of this kind as a defect (the Ch.10 Julia Domna wink, the Ch.9 Thracian name).
  - It also feeds W-11.
- **Fix (+1):** "for another ten years." → "**till one of them gives in.**"
- **Cascade:** none.

### [W-11] "Ten years" ×7: an in-chapter refrain
- **Audit:** NO TICS (a repeated phrase becoming a device inside one chapter).
- **Evidence:**
  - l.176 Mara: "ten years ago";
  - l.178 Valens: "Ten years";
  - l.186 Felix: "ten years over it", then "Ten years!";
  - l.230 Grata: "ten years we've been at it, ten years since the earth went";
  - l.276 Grata: "another ten years".
- **Problem:**
  - Foundation §10 wants the count printed in Ch.19–20, not hammered.
  - Felix's pair is history (the Senate's ban of 59) and a separate fact, so the phrase lands as a drumbeat across three speakers.
  - The tic gate does not catch it because each 3-gram differs.
- **Fix (−5, speech):**
  - l.230: "ten years we've been at it, ten years since the earth went," → "**we've been at it since the earth went,**" (−5).
  - Together with W-10, the count falls to 4 (Mara, Valens, and Felix's historical pair).
- **Cascade:** none. Ch.20 should print the quake count once, at most, in fresh words.

### [W-12] "Pacuvius's girl" ×4 as a name, against the bible's role-label rule
- **Audit:** NO TICS (role label as a name). Character bible, at-risk after Ch.5: "When a walk-on recurs inside a chapter, name her or vary the reference."
- **Evidence:**
  - l.10 "Pacuvius's girl slept under an awning";
  - l.12 "Pacuvius's girl was sick for every mile";
  - l.16 "Pacuvius's girl found me at the hurdles";
  - l.64 "Pacuvius's girl went down our plank first".
- **Problem:** she carries a full beat (the brooch, the greeting, "They had mules."), and the same two-word label runs across five paragraphs. Ch.8 solved this by naming.
- **Fix (−2):**
  - Name her the Roman way, once, at first mention: l.10 "Pacuvius's girl slept" → "**Pacuvius's girl, Pacuvia, slept**" (+1).
  - l.12, l.16, l.64: "Pacuvius's girl" → "**Pacuvia**" (−1 each).
  - If the Writer prefers her unnamed, vary instead: "the girl" / "the bride" / "the master's girl", no label twice.
- **Cascade:** add a Pacuvia line to the bible's Ch.19 walk-on block (W-15).

### [W-13] Felix's stacked questions have become a metronome
- **Audit:** NO TICS (syntax pattern into device).
- **Evidence:**
  - Bursts of 3–4 questions: l.50 (4), l.144 (3), l.152 (3), l.186 (3), l.220 (3), l.300 (3), l.332 (4).
  - Bursts of 2: l.102, l.120, l.304, l.312.
  - That is 11 of his ~15 speeches. Several end on the same three-beat question run.
- **Problem:**
  - The card allows "two or three questions before anyone answers one" as syntax, not a fixed count. It also asks for "Boasts in superlatives" and "no boast formula".
  - Seven bursts of exactly 3–4 questions in one chapter is the "Is it…" problem of Ch.16 moved from the opener to the rhythm.
- **Fix (≈0):** turn two bursts into a boast or a statement.
  - l.144: "Do you live in there? What if it goes out? Can I carry one?" → "**Do you live in there? Give me one. I've the steadiest hand on this road.**"
  - l.152: "Who's your best man? Has anybody ever put him down?" → "**Who's your best man? I'd put him down for you.**"
- **Cascade:** none.

### [W-14] Grata's arm-touch, the same beat twice in one scene
- **Audit:** Voice drift (voice-dna §1 dialogue conventions: "no character gets the same beat twice in a chapter").
- **Evidence:**
  - l.236: "She put her hand on my arm, on the sleeve, and talked on with it there, warm from the pot."
  - l.242: "she touched him on the arm too as she went by him … He looked at the place on his sleeve where her hand had been."
- **Problem:**
  - The l.242 touch is a deliberate plant (Valens's mind-reading about Grata, Ch.21) and must stay.
  - The l.236 touch spends the same beat a paragraph earlier. "too" then points at the repeat.
- **Fix (+2):**
  - l.236 → "**She took a pinch of my sleeve between finger and thumb and talked on holding it, warm from the pot.**" (+2).
  - l.242: "she touched him on the arm too as she went by him" → "**she touched him on the arm as she went by him**" (−1). Net +1.
- **Cascade:** later chapters vary her contact (the card's "touches people's arms" is a physicality axis, not one gesture).

### [W-15] Character-bible lag: the Ch.19 blocks quote the writer's draft
- **Audit:** Bookkeeping (the bible feeds the Writer and the evaluator).
- **Evidence:** the bible quotes strings that are not on the post-disruptor page:
  - Grata card: "reached the street's edge in two arms of masonry set at a right angle". The page: "Her counter ran out to the street's edge".
  - Ch.19 walk-ons:
    - "Whose freedman?" (page: "Freedman of whom?");
    - "which no other ship in the harbor flew" (page: "carried a little three-cornered sail high on the mast above the yard");
    - "the man raking water into the lime pit" (cut).
  - At-risk after Ch.19:
    - "Eight, in all. Only two have tombs worth the walk." (page: "Seven or eight. Only two…");
    - "This was where the dead go out, as the god had put it in Valens's mouth" (page: "…and they had followed the road out in their hundreds and settled in");
    - the frost/ownership exchange (cut);
    - "I agreed with all of it" (page: "I agreed with him");
    - "Anybody in the street could see exactly where that house had split." (not on the page);
    - "He looked hard." (not on the page).
- **Fix:** sync the Ch.19 Grata, Valens, Felix, Mara, walk-on and at-risk blocks to the final page after the editor's pass. Fold in W-03, W-04, W-09, W-12 and W-14.
- **Cascade:** the evaluator's reuse check reads these blocks.

---

## INFO

### [I-01] History and geography: confirmed (the brief's list)
- **Puteoli:**
  - the mole "on arches … a road carried on piers" (opus pilarum) with columns and statues;
  - concrete piers with the facing eaten off;
  - Alexandrian grain ships with the topsail (Seneca, *Ep.* 77);
  - a shaved Isis priest;
  - the Misenum fleet: a long dark oared ship with a forward-raking boat-sail mast.
- **The road:**
  - the Crypta Neapolitana: torch boys, choking dust, two carts passing (Strabo, Seneca *Ep.* 57);
  - Neapolis Greek, and its four-yearly games for the emperor (the Sebasta);
  - the inn by a reedy river east of the city (the Sebeto);
  - villas, fishponds, vines married to elms, pitch-lined wine;
  - Herculaneum "on a spur of ground between two streams";
  - salt pans near Pompeii;
  - two days with mules, a night near Neapolis.
- **Pompeii in repair (ten years after 62):**
  - stepping stones; shoring props; a mason pointing a patch;
  - new column drums on old, a treadwheel crane;
  - a trench for a new lead pipe;
  - programmata (the muleteers' *rogant*);
  - a thermopolium counter with sunk dolia and marble offcuts;
  - shop sills grooved for shutter boards;
  - the sunken amphitheater;
  - the AD 59 Nucerian riot and the Senate's ten-year ban.
- **The gates:**
  - Herculaneum road: the three-bay gate, scholae with lion's feet, altar tombs on stepped bases;
  - Stabian: two bench tombs with names along the backs (Tullius and Minius type);
  - Nuceria: the road running east–west under the south wall, columellae (some with a hair knot), programmata on tombs, roses for the dead.
- **The mountain:** "only the one" hump, broad and bare at the top, wooded belt, vines below. No Somma/cone split. The pizzeria two-hump outline is the modern contrast, correctly placed.
- **The crossing:** 11 nights. Gulf (2 days) → Ionian islands → 2 days open sea → Italy on the 6th morning → round the toe → the Straits (Charybdis on the Sicilian side) → Rhegium → the 8th night off an unseen coast → the bay on the 12th day. Exceptions: W-02, W-03.

### [I-02] "somebody under Augustus had cut a road" (l.140)
The tunnel was cut c. 37 BC for Agrippa, under Octavian, before the name Augustus. Mara's loose "under Augustus" is a period-natural shorthand. Optional: "**in Augustus's time**" (+1).

### [I-03] "ten years ago, nearly to the season" (l.176)
The quake was 5 February 62 (Seneca). The chapter is spring, with roses for the dead on the Nuceria road, which suggests April–May. That is a different season. Optional: "**ten years ago, in the winter**" (−1).

### [I-04] "By the twelfth morning of my marriage … all eleven nights before it" (l.10)
- The wedding was in the early afternoon (Ch.18), so the first *morning* of the marriage follows night 1, and the twelfth follows night 12. Counted as days (day 1 = the wedding day), the landing is day 12 after 11 nights, which is the brief's 11-night crossing.
- "Twelve days" to Grata (l.238) and "Twelve days into my own" (l.192) both fall on day 13 and are right as elapsed time.
- Optional: "twelfth morning" → "**eleventh morning**" (0; the `scene-set` "By the" opener is unchanged).

### [I-05] The Sarno and "scaffolds" are not named
- The river below the Stabian Gate (l.296) is the Sarno, unnamed; Grata's "Sarno Gate" (l.230) uses the modern gate name, as the outline allows. The Sarno lies south of the town, not on the coast road, so the outline's beat-3 listing was loose; nothing on the page is wrong.
- "Scaffolds" (beat 4) are carried by the props, the ladder and the crane. The NON-NEGOTIABLE's substance is met.

### [I-06] The carting route past the amphitheater
- l.272: the contractor is "at the Stabian Gate".
- l.300 (Felix): "The loads go out past it [the amphitheater]".
- The amphitheater is in the far south-east corner, nearer the Sarno and Nuceria gates. This works if the job is in the east of town and the dump lies east, which nothing contradicts. Leave it.

### [I-07] Foreshadowing pass: 0 banned forms; borderline lines kept
- "Seventy-nine": 1 (l.44), as a present thought.
- Mountain descriptors: none of the banned list. "It stood at the head of the bay where it had to stand" (l.30) is her map knowledge, not personification, and stays.
- "went on being green" (l.46) carries the outline's own "green and lovely, and that is the dread".
- Reader-irony from mouths, kept:
  - Pacuvius's "row the admiral round this bay till his beard comes in gray" (l.52): the fleet goes out in 79;
  - Valens's "There'll be men sleeping in those tombs" (l.258), against Ch.41's night in the tomb;
  - the eel-seller's boy's "Is this one yours?" / "No," (l.360–362).
  - Each is innocent in scene. **Ch.41–44 must not call any of them back.**
- W-10 is the only line that names a horizon past 79.

### [I-08] Reserved ending vocabulary (AUTHOR-END-1): clear, with the closest approaches logged
- "seam" 0, "niche" 0, "painted plaster" 0, "hand flat" 0.
- Closest approaches:
  - "I spread my fingers and gave it the whole of my palm." (l.354): foundation §4f's sanctioned "palm on the tomb's painted false door";
  - "it stayed a picture of a door" (l.356);
  - "Paint and white lay on a single coat of plaster" (l.354).
- None uses the reserved wording. Ch.42's "Aelia's palm flat … against painted plaster" stays unspent. Leave them.

### [I-09] Allowlist ledger
- "where the dead go out": Ch.13 l.292 (1), Ch.19 l.344 (2). **2 of 3.** Ch.44's optional third must not be load-bearing (foundation §4f.6).
- The present-tense "go" inside the narration is the quotation, and it is the chapter's only present-tense narration sentence.

### [I-10] Information flow: the table
- **Valens:**
  - Holds "Pompeii" as a place (Ch.15). He says it once, to the wine-woman (l.134), and calls it "This town of yours" (l.166).
  - He carried the god's answer (Ch.13), so he knows she is looking for a painted door. He never voices it, and deflects Felix ("Out where the dead are.").
  - He reads (Ch.11): "The muleteers have a man, then" (l.222) is his own reading. Felix, who believes he cannot read, is ahead with the dun.
  - He does **not** know the door is found: the chapter ends before they meet.
  - He does not know AD 79.
- **Felix:**
  - Knows "your gate" (l.312), plausibly from Valens over a day of carting.
  - Does not know the purpose ("Looking for what, at the gates?").
  - Cannot read; "Thirty pairs" is his own invention against the panel.
- **Grata:**
  - Tells, never asks: 0 personal questions on the page.
  - Reads "Greek" off Mara's walk and "married" off her standing.
  - Knows the Nuceria road from the red dust.
  - Except for W-05, every claim is observed or gossip.
- **The mother-in-law:** the Ch.18 plant ("will have the name of every soul who slept on this deck out of her") pays off at l.66.
- **The clerk:** records "Valens. Gaius Iulius." and Pacuvius's oath. Short sight, not recognition.
- **Mara's comprehension elsewhere:** consistent. She has the Neapolis balcony Greek whole ("stayed in the street for the rest of it"), the slow question whole, and the rose woman cut off by the passage's echo.

### [I-11] Objects: agree
- **Camera:**
  - Drawn "from under my dress" (l.42).
  - The dented front ring "flashed".
  - No cap, no counter.
  - Finger on the button, then off. **No frame fired.**
  - "where it had hung since Lechaion" is true but short: it has been on her body since Ch.12, and under Myrrhine's dress since Ch.17. Harmless.
- **Watch** (RIGHT wrist) and **bracelet** (LEFT): neither is mentioned. No conflict. Ch.24's winding is the next touch.
- **Leaf:** two boards opened on the table. "Corinth … Nero's year" agrees with Vettius and Caninius, "the year Nero was here". Back under the tunic with the belt drawn over it.
- **Pen-knife:** Plautia's, from her case, in the belt (l.20, l.124). It closes the brooch's coil, a good use.
  - Thread note: "Her woman can come to Puteoli for it" (Ch.17 l.450). They pass through Puteoli in half a day and leave nothing at the letter board for Myrrhine. The thread stays open with no return route on the page (plot_threads.the-knife-comes-home, unplanned).
- **Microcassette:**
  - "the toe of the old wool sock stuck out"; a hub turned a quarter through the knit (l.382).
  - None of the spent forms is used (rolled tight, flat weight, rummage).
  - This is foundation §4f's Ch.19 touch. Ch.35's must be a fourth staging.
- **Money:**
  - Valens's purse (the brother's road money) pays the torch boys, the wine and the first month at 24 HS.
  - The innkeeper's "two coppers a head … four the lot" is unpaid on the page, which is fine.
- **Mules:** **four** ("the four of them in a row", l.10; "four the lot", l.160). The black (a hipposandal off fore; noses the trench) and the dun (stepping stones) are named by colour.
- **Fig:** in its jar on deck, at the clerk's, on the roof (l.246, l.298, l.310). Valens walks round the inn's fig once with no opinion; foundation keeps the fig talk for Ch.11/20/34. Exception: W-07.

### [I-12] Characters against their cards
- **Grata:**
  - Entry by voice. Forty, broad, a scald scar.
  - Floods end in a command.
  - The husband's dice as a joke; the son unnamed and "one day" for aedile (Secundus, Ch.31).
  - The whitewash patch planted and unexplained (her irrational behavior; Ch.31 owns it).
  - **Teeth 0** (Ch.31).
  - "Sit there. Eat that." / "Drink that before it cools.": the "[verb] that" closing command is used twice. **Watch it:** Ch.20 varies the command's shape.
- **Valens:**
  - Short, level, practical. Bare "No." 0, comparisons 0.
  - Mind-reading the clerk ("He knew me", "He'll know me again"), exactly the foundation's chaos.
  - Hands find work: the shoe, the noseband.
  - "love" 0.
- **Felix:**
  - Arena-mad (the fleet, the Neapolis fighting, the thirty pairs, the sunk bowl, the dead fighter's stone).
  - Is-it openers 0. No palm scratched (reserved for Ch.21/28).
  - Exception: W-13.
- **Pacuvius:** within card. "That's the last I'll say to you." He does not recur unless the letter thread needs him.

### [I-13] The children's citizenship (CH18-5, OPEN): lines that touch it, none that settles it
- l.96–98: "And the woman?" / "His," said Pacuvius … "Married at Lechaion, on the stones, in front of my crew, and I'll swear to it here or anywhere you like." This is a vouched marriage in a harbor clerk's wax.
- l.88: "Valens. Gaius Iulius." His citizen name is recorded, and his citizenship rests on the contested manumission.
- l.236 (Grata): "You're Greek, you've the walk". Mara is read publicly in Pompeii as a Greek, that is, a peregrine.
- None says "citizen" or anything about conubium or the children. **Keep it so** until the author rules at checkpoint 4. No later chapter should treat the Puteoli wax as legal proof of anything.

### [I-14] Voice: echoes, commands, spoken lines, tense, samples
- Cross-chapter echoes: 0 (tool, and my 4–5-gram sweep). Spoken-line echoes: 0.
- **Command echoes: 0.** "Sit there. Eat that." → "I took the bench … and emptied it" (l.386–388) is narrated compliance in other words, the form the bible's Ch.8 note accepts.
- Present-tense generalisations in narration: 0, apart from the allowlisted quotation.
- "A join showed or it did not." (l.210) is a past-tense gnomic line. It is the all-or-nothing distortion, stated once; Ch.20 must not restate it.
- Credential / provenance asides: 1 ("as I had sounded many a plaster panel at home", l.354), within the cap of 2.
- **Sample-13:**
  - The beat order is mandated.
  - "Fine mountain for vines" is the outline's line (allowed). It rhymes with the god's "mountain of vines", and Mara never points at the match.
  - "I studied the farms on its lower slopes until I could have drawn them" (l.38) repeats the sample's response shape ("watched the villa … until the headland took it"). Optional: "**and I studied the farms on its lower slopes, one roof at a time**" (0).
  - No cap is put back: sample-13's "I put the cap back on the lens" is correctly impossible.
- Memory inserts (CP2-2): the pizzeria outline, the Broad Street subway, the parked car, the kitchen sink. Each is triggered by the scene and returns to it. No stand-alone memory.

### [I-15] Intra-chapter echoes (optional)
- "leather trodden into" ×2: l.244 "scraps of leather trodden into it" and l.274 "crescents and tags of leather trodden into the earth". At l.274: "**crescents and tags of leather pressed into the earth everywhere**".
- "the white plaster next to the door" ×2 (l.352, l.372).
- "the afternoon sun" ×2 (l.348, l.354).
- The paired modern temperature similes at l.352/354 ("as warm as the hood of a parked car…" / "cool as a glass of water left standing…") are a designed pair at the chapter's slowest moment. Keep both, but no later threshold uses the warm-as/cool-as pairing.

### [I-16] Ledger, shape and pacing: honored
- `scene-set` → `long-fade`; 4 breaks; dialogue 24% (band 20–30); median 18 (high); 8,474 words (target 8,400).
- Reading speed matches the outline:
  - quick at the harbor (clerk, board, wine);
  - panoramic on the road;
  - very slow at the tomb (l.346–378, about 900 words for one afternoon).
- The outline's beat order is met, including "a page at most" for the search (two one-sentence roads).

### [I-17] Handoff to Ch.20 (for the outline patch and the Writer's prompt)
1. **The shop's location:**
   - Outline Ch.20 premise: "a repair shop in Grata's front room".
   - The page: the dead cobbler's shop **next door** to her counter (l.236–244), as foundation §3 and sample-11 have it.
   - Patch the outline's wording.
2. **Beat 5, the notice over "the old earthquake crack in Grata's wall":**
   - Ch.19 puts the visible quake crack on **another** house (the cousin's pink stripe, l.210) and gives Grata's own wall a fresh whitewash patch (l.286).
   - Ch.20 may put a crack under that patch, or move the notice onto the cousin's stripe, but must not re-describe either in Ch.19's words.
3. **All-or-nothing:** spent on the plaster stripe (l.210, "the plasterer should have been made to stand in front of it"). Ch.20's NON-NEGOTIABLE thrown-away bowl must stage it with her own work and no verdict line.
4. **"seam":** reserved for the ending by this brief, and 0 in Ch.19. But outline Ch.20 ("learns to let a seam show") and sample-11 ("So I left the seam") plan the word for Ch.20. **The orchestrator should rule before Ch.20 is prompted.**
5. **The door is found, and only Mara knows.** Grata knows only "out among the dead"; the eel family thought she was praying. When and how Valens is told is open.
6. **The Puteoli letter board:** somebody from Pompeii must fetch the brother's letter ("When the praetor names our day") by Ch.21–22.
7. **Household:**
   - the bed cord rotted at one leg;
   - the shutter boards never put up;
   - the bar on the inner door;
   - the fig on the roof (Ch.20's named frame, staged fresh);
   - Felix stabling at the Stabian Gate inn;
   - Valens carting for a contractor by the load.

### [I-18] Forward: the tomb's geometry against Ch.41's niche
- l.348: "a small square house of rubble, plastered white, with a low gable over its front and no higher at the ridge than Valens's head". The painted door fills the front "from the ground nearly to the gable".
- Outline Ch.41: the family shelters overnight "in the niche of the tomb with the painted door, among strangers".
- No niche or enclosure is described in Ch.19, correctly, since the word is reserved. **Ch.41 must place the niche** (side, back, or a walled precinct) so that it does not contradict a head-high, door-fronted house.

---

## SUGGESTED YAML PATCHES (for the entity-tracker's next UPDATE; apply after the editor's pass)

```yaml
suggested_patches:
  - entity: "timeline (Ch.19)"
    action: "add"
    value: "Day 1 the Lechaion wedding (spring AD 72, after the Kalends, before the Ides of an unnamed month); nights 1-11 at sea; day 12 Puteoli landing, road through the hill, inn beyond Neapolis's eastern gate (night 12); day 13 coast road to Pompeii, Grata, the cobbler's shop; day 14 Valens carting, the Stabian road searched; day 15 the Nuceria road, the tomb found, sleep, Grata at lamp-lighting"
    reason: "ch-19 l.10-l.388; W-02 changes 'by noon' to mid-afternoon on day 12"
  - entity: "locations (new)"
    action: "create"
    value: ["puteoli-mole-and-letter-board (wine-shop at the quay's foot)", "crypta-neapolitana (unnamed: 'the road through the hill')", "inn-east-of-neapolis", "gratas-thermopolium (long straight street running east = Via dell'Abbondanza per foundation)", "cobblers-shop (rented, 24 HS/month, next door to Grata)", "stabian-gate-inn (stables the mules)", "nuceria-road-tomb (Aulus Numisius Eros, freedman of Aulus; painted false door; town side of the road)"]
    reason: "first appearances in ch-19"
  - entity: "door_location (knowledge_index)"
    action: "add"
    value: { who: "mara-reyes", what: "FOUND and dormant: the leaf faintly cool under warm plaster; the knuckle tap dull, rubble behind", learned: "ch-19 l.346-l.356", method: "discovered" }
    reason: "valens, felix, grata: NOT told on the page"
  - entity: "plautias-grandfathers-pen-knife"
    action: "add"
    value: { chapter: 19, detail: "closes the sprung coil of Pacuvius's daughter's brooch; still in Mara's belt; no arrangement for Myrrhine left at Puteoli" }
  - entity: "vettius-first-book leaf"
    action: "add"
    value: { chapter: 19, detail: "shown to the Puteoli harbor clerk; read to the witnesses; 'Corinth … Nero's year'; Valens recorded as 'Valens. Gaius Iulius.'" }
  - entity: "microcassette"
    action: "add"
    value: { chapter: 19, location: "in the old wool sock in her bag on the back-room floor of the cobbler's shop, Pompeii", detail: "a hub turned a quarter through the knit" }
  - entity: "maras-camera"
    action: "add"
    value: { chapter: 19, detail: "raised at the mountain from the deck, finger on the button and off; no frame fired; frame count unchanged" }
  - entity: "pomponia-grata"
    action: "update"
    value: "first live appearance; teeth 0; son unnamed; husband glimpsed; whitewash patch planted; the cobbler's shop rented to them"
  - entity: "CH18-5"
    action: "note"
    value: "Ch.19 touches, settles nothing: Pacuvius vouches for the marriage before the Puteoli clerk; Valens's citizen name in the clerk's wax; Grata reads Mara as Greek"
```
