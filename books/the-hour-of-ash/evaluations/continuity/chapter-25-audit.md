# Continuity Check: Chapter 25, "Augurinus" (manuscript audit vs Ch.1–24)

**Date:** 2026-10-23
**Scope:** `manuscript/chapters/chapter-25.md` as it stands after dialogue-polish, hook-craft (no edits) and the disruptor. Checked against Ch.1–24 (targeted greps: Ch.1 Szabo/notebook/house, Ch.2 Fenn documents, Ch.3 and Ch.15 cave geometry, Ch.13–14 Theano and the year, Ch.19–24 Pompeii, tremor note, pregnancy, the Ch.24 Chaldean plant), ENTITY_STATE.yaml (tracked to Ch.24; the Ch.25 UPDATE runs in parallel and was not touched), outline Ch.25 / 26 / 30 / 31 / 35, foundation §3, §4d, §9, §10, §12, STATE (guardrails, ARCH-6/16/17, AUTHOR-CP4-1/2, AUTHOR-END-1), character-bible (Fenn, Szabo, Pat, Margaret cards; At-risk after Ch.20–24; the Ch.25 guards), and the dialogue/hook/disruption reports for Ch.25.
**Line refs** are file lines in chapter-25.md (header comments = l.5–6; prose l.8–448).
**Total:** 7 CRITICAL · 19 WARNING · 16 INFO

**Clean on:** "Vesuvius" ×1, Fenn's (l.328). "Margaret" ×0, and Mara holds the name ("I had the name.", l.382). "the one it brought" ×1 as a promise ("It takes back the one it brought. It brought you, so it'll take you.", l.264). "One door with many mouths" ×1 on the page (the second grep hit is the l.5 comment). "breathe with the earth" 1 of 2. "Late summer, seventy-nine." 1 of 2. "Jesus H. Christ" 1 of 1. "in (all) the years since" ×0. "by degrees" ×0. Lucius is never called a citizen (CP4-1). The tomb is only talked about, never on the page (CP4-2). The Ch.31 guard holds: "up ladders" (l.252, 254) is scaffolding talk, not a ladder held, and the charcoal on Fenn's walls is not election paint. Narrator foreshadowing: none. The mountain with its cloud (l.360) is a present look, and Fenn's broken-off "They'll be up ladders when..." (l.254) is his line, not hers. Talking to objects: 1 ("he told it", l.46), at the cap. "gibberish" is not quoted back, and nobody says the hour was "all of them" (Ch.24 guard). Lucius is about eight months old (born summer 74, early spring 75), crawls, pulls up and nurses, which fits. The WHEN comes before the story, flat. Fenn's failed dates hold up against Mara's movements: spring 71 she was in Phocis, and October 73 she was in Pompeii, a mile off (ENTITY: conceived late Sept–Oct 73). The estate-sale chain matches Ch.1 exactly: Antique Row on Pine, a Phillies cigar box, "Estate sale, Chestnut Hill, last October. Margaret Fenn.", the coordinates in ballpoint on the chart, a black oilcloth notebook with perished elastic, A. J. FENN on the cover. The notebook's contents match Ch.2: the slot, the goat that ate half a postcard, the July 21 entry ("Going in tomorrow first thing with the good flashlight and a ball of kite string") against l.170's "July twenty-second, sixty-eight". Mara's tremor notes match Ch.20 (first entry at the vintage of 72, on the back leaves). Fenn's counts are right: born 1934, 34 in 1968, about 68 now; thirty years between 68 and 98; thirty-four years since AD 41; eleven years of Kalends marks and an eleven-year basil, so Puteoli since about AD 64, which squares with Misenum in 62. Mara's age is right: fifteen at the October 1980 parade, b. early 1965 (ENTITY: fourteen in April 1979). Dialogue 48% (band 45–55). Em-dashes 3 (cap 4; the header says 2, see INFO-01).

**Period facts verified:**
- 1964 Phillies: 6½ games up with 12 to play; Mauch starting Bunning and Short on two days' rest; Chico Ruiz stealing home with Frank Robinson at bat on 21 Sept 1964; ten straight losses. All correct.
- 1980 World Series: won against Kansas City; McGraw struck out the last man and jumped; the Broad Street parade. All correct.
- Connie Mack Stadium: at 21st and Lehigh, used by the Phillies until 1970, burned 1971, demolished 1976, and a church later built on the lot. Correct, and Fenn in 1968 would naturally say "Connie Mack".
- Trolleys: the 34 on Baltimore Avenue was still a trolley in 1998. The 23 on Germantown Avenue was bused in 1992 ("a few years ago" fits), and it ran up to Chestnut Hill, which is why Fenn asks about it.
- Horn & Hardart: the automat on Chestnut Street is real, and the last New York automat closed in 1991.
- Aegean quake: 19 Feb 1968, Agios Efstratios. Correct (logic issue at WARN-08).
- Claudius: found behind a curtain after his nephew Caligula was killed, January AD 41, as Graves tells it. Correct.
- Misenum fleet; a Serapis priest at Puteoli; the Solfatara's yellow smoke: all correct.
- Puteoli bradyseism: the town sinks, so the mooring rings go under while "the sea hasn't gone anyplace". This matches Roman-period subsidence.

Each item is something Fenn could know in 1968 or Mara could know in 1998.

---

## CRITICAL ISSUES (fix before the evaluator)

### [CRIT-001] Theano's naming of Pompeii moved to "a wall beside the Sacred Way"
- **Audit:** Information flow / plot facts (Ch.13)
- **Line:** 244
- **Description:** In Ch.13 Theano names Pompeii at her own house, "the house next to the highest", sitting on her husband's stone by the door with Mara on her doorstep below her (ch-13 l.428–502). Ch.14 opens "It came to me on Theano's doorstep". Nothing puts her on a wall on the Sacred Way.
- **Evidence:** l.244 "And afterward the Pythia told me herself, on a wall beside the Sacred Way with her knees aching, that it meant Pompeii."
- **Fix:** "on a wall beside the Sacred Way" → "at her own door". (Grepped: not in Ch.1–24. This avoids "her doorstep" and "her husband's stone", which are Ch.13's words.)
- **Cascade:** None. Ch.14 opener stays consistent.

### [CRIT-002] Fenn went to Athens by "boat"; Ch.2 has him fly TWA
- **Audit:** Character facts (Ch.2 documents)
- **Line:** 182
- **Evidence:** Ch.2 l.29 "*Athens on the second of April, TWA.*" (ENTITY: "flew TWA to Athens, 2 April 1968") against l.182 "I'd read the Graves book on the boat over to Athens."
- **Fix:** "boat" → "plane".
- **Cascade:** Ch.35's "coverless paperback" can now be the Graves, if the Writer wants it to be. Nothing else changes.

### [CRIT-003] The coppers: one was flicked back to Mara, but at the close "two" are still on the table
- **Audit:** Object continuity (within the chapter)
- **Lines:** 202, 210, 442
- **Evidence:** l.202 "Fenn reached across me and took one of my two coppers off the table's corner." · l.210 "He flicked the copper back to me, and I trapped it against my breastbone." · l.442 "My two coppers were still on the corner of the table. I reached for them, and then, at a loss, I let them lie."
- **Fix:** l.442 → "My other copper was still on the corner of the table. I reached for it, and then, at a loss, I let it lie."
- **Cascade:** None. The fee-left-anyway beat survives with one coin.

### [CRIT-004] The item-by-item look, CLOSED book-wide, appears five times
- **Audit:** Voice / closed device (bible: "item-by-item look … CLOSED"; "the two-item looked-at-X-and-at-Y form: CLOSED … No further use anywhere")
- **Evidence and fixes:**
  - l.54 "He took in my face, then my hair, then my face again, and his mouth came open." → "His mouth came open."
  - l.80 "He watched the Chaldean's mouth while it talked, and mine while it answered, and back again." → "He watched our mouths."
  - l.82 "and swung round to the doorway at last, to the man there, and the size of him, and the child, and he stopped hitting my back." → "and swung round to the doorway at last, and he stopped hitting my back."
  - l.414 "his pale eyes traveled my face and my hands slowly" → "his eyes went over my hands slowly". This also cuts the second "pale eyes" (l.236 keeps it), and it leaves the look on the hands that mend, which is the card's "studies Mara only when she says she mends things".
  - l.426 "Fenn looked at the plant for some while, and at Valens, and then slowly leaned over" → "Fenn looked at the plant for some while, and then slowly leaned over" (and see CRIT-005 for the rest of the sentence).
- **Cascade:** The recognition at l.54 still has "Thanks" → the lighter → the turn → his mouth → "Jesus H. Christ". The NON-NEGOTIABLE flush at l.80 is untouched.

### [CRIT-005] Command echoes (the device has been SPENT book-wide at 3 since Ch.9): two compliance lines repeat the order's verb
- **Audit:** Voice / closed device. The gate missed both because each order sits mid-speech and the compliance falls in a later paragraph.
- **Evidence:**
  - l.424 Valens: "Turn it every few days. Water it less." → l.426 "and turned the pot a shade further toward the room with his good hand."
  - l.432 Fenn: "Give me his hour and I will do it tonight" → l.442 "I gave him the hour, as near as any of us had it, and the season".
- **Fix:** l.426 "turned the pot" → "nudged the pot". l.442 "I gave him the hour," → "He had the hour from me,", which with CRIT-003 makes the paragraph "He had the hour from me, as near as any of us had it, and the season, and he set it down in charcoal … My other copper was still …".
- **Cascade:** The bible's SPENT note "Fenn turns it 'a shade further'" needs re-wording at sync.

### [CRIT-006] Fenn lists: a three-item anaphoric horoscope
- **Audit:** Outline writer warning ("Fenn must NOT enumerate or list (zero-tic ruling)"); the Fenn card ("No enumerating, numbering or listing habit, ever"); retired anaphora triads
- **Line:** 436
- **Evidence:** "They will be in good Greek," said Fenn, "and very handsome. A long life. A rich wife. A house with a garden and a fig tree in it."
- **Fix:** → "They will be in good Greek," said Fenn, "and very handsome. A long life, under his own fig tree." (Grepped: fresh.)
- **Cascade:** "Grata will like that." / "Everyone likes that." still land. A fig tree in Fenn's mouth is not Valens's fig obsession; it stays an image.

### [CRIT-007] Ch.24's SPENT unlaced sandal comes back as Mara's simile
- **Audit:** Voice / spent material (bible At-risk after Ch.24: SPENT "… the unlaced sandal …"; Statia, ch-24 l.22 "that sandal's unlaced yet")
- **Line:** 10
- **Evidence:** "a child without his stars cast was a child let out of doors with his sandals unlaced."
- **Fix:** "with his sandals unlaced" → "in the dark". (Grepped: "out of doors in the dark" is fresh. Avoid "unwatched", which is Ch.11/17's, and "barefoot", which is Myrrhine's spent device.)
- **Cascade:** None.

---

## WARNING ISSUES

### [WARN-01] Valens hears "Nuceria Gate" in the English, which edges toward Ch.30's knowledge beat
- **Audit:** Information flow (outline Ch.25: Valens "does **not** learn the date or the door's rules"; Ch.30 2a: "From here he knows where the door is")
- **Line:** 156 (Valens has been in the doorway since l.68)
- **Evidence:** "The freedman's place outside the Nuceria Gate, with the door done on its front in paint. Eros's." A proper noun stays a proper noun inside English. With "Eros's door" said four times (l.156, 264, 314, 328), a Pompeii muleteer who heard "Nuceria" could find the tomb, and that takes the edge off Ch.30's road scene.
- **Fix:** Cut "outside the Nuceria Gate" → "The freedman's place, with the door done on its front in paint. Eros's." ("Eros" alone is a common freedman's name.)
- **Cascade:** Valens still hears "Pompeii", "Vesuvius" (l.328) and "seventy-nine", none of which gives him the date or the rules. The entity UPDATE should log Valens's Ch.25 knowledge as: heard the English; believes; learned that "he knows the door" (l.294–296); not where, not when, not the law.

### [WARN-02] The collapse: its core is a new shape, but it wears borrowed frames
- **Audit:** Mara's laugh/mouth channels (all five laugh shapes spent; outline Ch.25 rules this one in); the Ch.22 rebuild; the Ch.24 echo
- **Verdict:** The core is new. Laughter and crying are fused into one fight for breath, triggered by "thanks", while her hands save the papyrus. No mouth is used as the rebel. Three frames are reused, though:
  - **Body acting "without me"** is Ch.22's fifth shape ("the laughing went on by itself in my shoulders, without me, and then it ran down and left me with wet cheeks", ch-22 l.254) and Ch.6's "my hands could understand without me". Here it appears three times: l.60 "my legs had settled the matter without me", l.60 "My hands had no part in any of this;", and l.230 "Without my sending it, my hand had gone to the flap".
  - **"no part in"** appears twice in the chapter: l.38 Fenn's left hand "with no part in what the right hand was doing" and l.60.
  - **"The sound I made"** (l.60) re-uses Ch.24's spent "A sound left me that was nobody's I knew." / "I made a noise."
- **Fix:**
  - l.60 "because my legs had settled the matter without me" → "because my legs had gone".
  - l.60 "The sound I made then had a laugh at the front of it and the other thing right behind" → "It began as a laugh, with the other thing right behind it,". Then continue "so close that they were one breath …".
  - l.60 "My hands had no part in any of this; they saw the drops" → "My hands saw the drops".
  - l.230 "Without my sending it, my hand had gone" → "My hand had gone".
- **Cascade:** "Ow … set me off again" (l.66) still works. Log in the bible: Mara's sixth laugh shape (fused with tears) is SPENT.

### [WARN-03] A second flush in the chapter dilutes Valens's NON-NEGOTIABLE one
- **Lines:** 80, 218
- **Evidence:** l.80 "The color came up out of his collar." (Valens, fresh book-wide) · l.218 "a little louder than before, pink to the collar of the robe." (Fenn)
- **Fix:** l.218 cut ", pink to the collar of the robe". The stool turned to the wall already shows his embarrassment.

### [WARN-04] The "Nobody had [verb]" frame appears twice (WATCH from Ch.24: ≤1 per chapter from Ch.25)
- **Lines:** 10 "and nobody had done it" · 230 "an even gray fur that nobody had disturbed"
- **Fix:** l.230 cut "that nobody had disturbed" → "There was dust on top of it, an even gray fur."

### [WARN-05] Narrated traits exceed the evaluator's hand-count (>3 per chapter fails)
- **Evidence:**
  - l.14 "as Lucius preferred to travel"
  - l.14 "with the deep offense he kept for anything that moved without asking him first"
  - l.80 "as he halted in any doorway to learn a room before entering it"
  - l.270 "which Lucius had been explaining at length was where he meant to be"
  - l.354 "as he must have been with grain-ship captains displeased with their stars"
  - l.390 "the look he kept for a horse gone lame that had still to find it out"
  That is six. There are also two of the "[look/feeling] he kept for" frame (l.14, l.390), which is the third use book-wide after Ch.1's "in the voice another woman might have kept for *bookie*".
- **Fix:**
  - l.14 cut "as Lucius preferred to travel,".
  - l.14 "and at eight months Lucius watched the gulls with the deep offense he kept for anything that moved without asking him first." → "and at eight months Lucius glared at the gulls."
  - l.270 cut ", which Lucius had been explaining at length was where he meant to be,".
  That leaves 3 (l.80, 354, 390). l.278 "with deep suspicion" can then stay, because "deep" is no longer doubled.

### [WARN-06] The notebook's cover rebuilds Ch.1's description of Fenn's capitals
- **Line:** 372
- **Evidence:** Ch.1 l.159 "in square capitals pressed so hard the pen had nearly gone through" / l.201 "The cover said A. J. FENN in the same square capitals." against l.372 "On the cover, in capitals somebody had pressed hard into the cloth, it read A. J. FENN."
- **Fix:** → "On the cover it read A. J. FENN."

### [WARN-07] The "voice flat as [X]" simile frame, a third time
- **Line:** 58
- **Evidence:** Ch.1 l.347 "a man's recorded voice … flat as a train station"; Ch.13 Theano "as flat as a price for a lame ewe"; l.58 "with the vowels laid out flat as pavement". (Ch.21's "flat as a griddle cake" is a coin.)
- **Fix:** "with the vowels laid out flat as pavement" → "with the vowels in his nose". (Do not use "pulled out long", which is l.192's.)

### [WARN-08] The Aegean quake: Fenn's own example breaks his own rule two sentences later
- **Audit:** World rules / internal logic
- **Line:** 264
- **Evidence:** "The ground moves hard, and the door opens a crack, and that's how the Corycian went for me; there'd been a big quake out in the Aegean that winter, had you heard? I hadn't, then." Then l.268: "When it goes, it goes for hours. A night, tops, never days." A winter quake explaining a July opening is a five-month lag, stated outright. "I hadn't, then" also invites the question of how he knows now (he heard of it in Greece that spring, but the line suggests he learned it later).
- **Fix:** "; there'd been a big quake out in the Aegean that winter, had you heard? I hadn't, then." → "; there'd been a bad quake out in the Aegean that year." Fenn stays fallible, and the lag is no longer spelled out.
- **Cascade:** Ch.36's arithmetic is unaffected.

### [WARN-09] "the news in me" at the Ides of October 73 runs ahead of Ch.20's timing
- **Audit:** Timeline (ENTITY lucius ch21_note: first sickness about mid-November 73, conception late Sept–Oct; Ch.20: Grata names it after a week of fish nausea, and Mara herself had decided "The jar had turned")
- **Line:** 320
- **Evidence:** "That autumn Grata had looked at me over her fish and named what I had not yet told Valens. I had lain in our bed … with the rain on the tiles and the news in me, not sure of anything, a mile from Eros's bench, while a Girard Avenue man sat on it in the wet … and waited for a door to breathe." The paragraph reads as if Mara had the news, or a suspicion of it, by the Ides. At that point she was at most a few weeks pregnant and unaware of it.
- **Fix (also covers WARN-10):** "and the news in me, not sure of anything, a mile from Eros's bench, while a Girard Avenue man sat on it in the wet" → "and the child in me, unguessed, while a Girard Avenue man sat on Eros's bench in the wet". Then "waited for a door to breathe" → "waited for a door to open".
- **Cascade:** "I was a mile from you" (l.322) now carries the distance alone (the paragraph had said "a mile" twice).

### [WARN-10] The narrator picks up Fenn's idiom (bleed guard)
- **Line:** 320 "waited for a door to breathe". "breathe" is Fenn's law-word, and the chapter already has 8 of the family (l.64, 210, 254 ×2, 264, 268, 328, 320). The card's bleed guard: "Mara must never pick up his idiom." Fixed by the WARN-09 string.

### [WARN-11] Fenn's self-doubling is becoming a device
- **Evidence:**
  - l.108 "Since Claudius I've been waiting … Since Claudius."
  - l.136 "Twelve. You could've…" and "steals home, steals home"
  - l.210 "give or take. Give or take."
  - l.304 "Nothing surprises me. Nothing surprises me anymore."
  - l.258 "Shut tight." after "And it was shut."
  That is six repeat-for-emphasis beats in one chapter, which reads as a rhythm signature (the no-tics law covers devices, not just phrases).
- **Fix:**
  - l.108 cut the second "Since Claudius." → "… once he had breath. "I told it to a priest of Serapis …".
  - l.210 cut the second "Give or take." → "… every time, give or take. That's the part that kills you."
  - l.304 → "Nothing surprises me anymore."
  - Keep "steals home, steals home" (the 1964 rant) and "Shut tight."

### [WARN-12] A counting gesture, the retired Fenn-numbering device in physical form
- **Line:** 314
- **Evidence:** "Twice." He held up two fingers, looked at them, and put them away in his sleeve.
- **Fix:** Cut the gesture → "Twice."

### [WARN-13] The room is catalogued twice in five paragraphs
- **Audit:** Retired cataloguing device (narrator)
- **Lines:** 230, 234
- **Evidence:** l.230 "As he talked I took stock of his room. It was a room for working in, with the table and his stool and the client's stool and the tablets, and the sky on the walls." restates l.30–34. Then l.234 re-lists l.230: "at his room, at the rolled mat and the peg and the lamp on the floor".
- **Fix:** l.230 cut the first two sentences, so the paragraph opens "In a corner a sleeping mat had been rolled tight …". l.234 cut ", at the rolled mat and the peg and the lamp on the floor" → "He waved the hand with the lighter in it at his room, and rested his case."
- **Cascade:** The packed bag with dust (the theme object) stays.

### [WARN-14] Mara lists in speech
- **Line:** 392
- **Evidence:** "Your writing's all in the front, all of it, the cave and the slot and the goat that ate your postcard."
- **Fix:** → "Your writing's all in the front, down to the goat that ate your postcard."

### [WARN-15] "schoolmaster" quotes the Ch.24 plant back, twice
- **Audit:** Ch.25 guard (the husband's plant "pays off only by what Mara hears for herself"); ch-24 l.126 "he tells you your day in Greek like a schoolmaster"
- **Lines:** 42 "It was beautiful Greek, a schoolmaster's," · 84 "and spoke in his schoolmaster's Greek."
- **Fix:** l.84 → "and spoke in Greek." (l.42 stays as her own hearing.)

### [WARN-16] Fenn's "all this time" is next to the banned "in (all) the years since"
- **Line:** 402
- **Evidence:** "You didn't lose it, over here, all this time?" The dialogue pass removed two "in all this/that time" from Mara's mouth as adjacent to the banned pattern, so the same reasoning applies to Fenn.
- **Fix:** → "You didn't lose it, over here?"

### [WARN-17] Pat's "front steps" crowds Fenn's one approach to Margaret
- **Lines:** 192, 268
- **Evidence:** l.268 "walk up the front steps and ring the..." is the card's "only approach to her" and quietly echoes his last entry in Ch.2 ("I'll be sitting on her front steps with a sunburn"). l.192 Pat "hosing down her front steps every evening" (the disruptor's line) uses the same two words 76 lines earlier.
- **Fix:** l.192 "her front steps" → "her steps". (Do not restore the cut "standing in her own hose's spray".)

### [WARN-18] CASCADE: Ch.25 uses up the 1964 collapse that Ch.26's letter is meant to REVEAL
- **Audit:** Outline Ch.26 beat 2 "(document, REVEAL) Fenn on the Phillies' 1964 collapse"; Fenn card period references ≤2 each
- **Evidence:** l.136 gives the whole collapse: the lead, Mauch, Bunning and Short, Ruiz stealing home with Robinson at bat, ten straight losses, the Girard Avenue bar.
- **Fix:** No change to Ch.25 (the outline asks for a first mention, and the argument is the chaos trait). **Outline Ch.26 patch:** the letter's 1964 material must REVEAL something new, from the card's unused pool: Callison, Bunning's Father's Day perfect game, or where he was on 21 Sept, but not the lead, Mauch, Ruiz or the losing streak. Each named reference here is now 1 of 2.

### [WARN-19] The ship's-boy reply and the closing "I told him" sit in a field of "told" tags
- **Lines:** 46, 198, 204, 276, 430, 432, then the mandated close l.448 "I told him his arithmetic was wrong."
- **Description:** Six "[X] told [Y]" speech tags before the closing sentence, which also turns on "told". The close is weakened by the run-up.
- **Fix:** l.430 "he told me" → "he said". l.432 "Fenn told him, turning fast" → "Fenn said, turning fast".

---

## INFO

- **INFO-01** Header comment l.6 says "Em-dash 2"; the page has 3 (l.154, 340, 396). Under the cap. Correct the header at finalize.
- **INFO-02** l.134 "He slapped his glove on his leg before he threw." McGraw's glove-slap on the thigh was a coming-off-the-mound celebration, not a pre-pitch habit. Optional: "before he threw" → "when he got a man out". Mara was fifteen, so leaving it is defensible.
- **INFO-03** l.328 "it's all in Pliny": Pliny's two eruption letters never name Pompeii. This is Fenn's schoolboy compression, in character, and Mara does not catch it. Leave it, or make it "it's all in the books" if the evaluator flags it.
- **INFO-04** l.116 "clear out to the cemetery and past it": the 34's terminus was 61st and Baltimore. "and past it" is not verified. It is Fenn's memory, so no action is required.
- **INFO-05** "a few years ago" ×2 in Mara's mouth (l.204 automat, l.386 trolley). Optional: l.204 "and it closed a few years ago" → "and that's closed too".
- **INFO-06** l.60 "in five years the first English": Mara has been here about 4½ years (autumn 70 → early spring 75). It is a round figure in a fit and not printed as a count elsewhere. Optional: "in more than four years".
- **INFO-07** "first thing" in Fenn's voice ×3 book-wide (Ch.2 entry; l.170; l.444). Optional: cut ", first thing," at l.444.
- **INFO-08** "kills" ×2 in Fenn's mouth 12 lines apart (l.198 "if it kills me", l.210 "That's the part that kills you"), near the card's sample line ("You know what kills me?", never to be printed). Optional: l.198 cut " if it kills me".
- **INFO-09** l.380 "He did not ask whose." is narration (the outline's own words), not a spoken "Whose …?". The who-pays frame is closed for speakers only. If the evaluator reads it as the frame, "He did not ask." loses nothing.
- **INFO-10** Fenn's broken-off lines ×3 (l.148 "Is he still...", l.254 "when...", l.268 "ring the..."). All are motivated. WATCH in Ch.26–27 so trailing-off does not become his signature.
- **INFO-11** l.280 "Would it take him?" stands alone after a Lucius paragraph, and the speaker is fixed only by l.284 "I asked". It reads correctly, so no action.
- **INFO-12** Ch.26 outline: Fenn asks in a letter who won the 1997 Series, after l.124 "One thing … and then not another word". He asks and refuses answers, so this is consistent with the card. No change.
- **INFO-13** l.444 Fenn's ballgame "when we come out … Connie Mack" assumes they emerge together, and in 1968. Mara keeps the fire to herself (l.446). This is designed irony, consistent with "Near where you went in" (l.268).
- **INFO-14** l.254 "It came in the night": the ancient sources give 5 Feb 62 but no hour. Foundation §9 puts the opening at "part of one night". Consistent.
- **INFO-15** l.322 "in bed by the forum" against l.408 "east of the forum". Loose but compatible.
- **INFO-16** New canon from the page for the tracker, all consistent with the foundation:
  - Navy celestial navigation, 1952, a destroyer off Korea.
  - The Graves book.
  - Landed in snow; the year learned at the thaw in Amphissa's market.
  - Two years in Phocis.
  - With the Misenum fleet before 62.
  - Puteoli from about 64.
  - Teaches triangles mornings in a house on the hill.
  - A bathhouse keeper on the hot ground.
  - A Neapolitan laundress-widow.
  - A packed oiled-leather bag with dust on it.
  - A brass lighter, never lit.
  - Fenn now knows Mara keeps tremor notes in the back pages, but not their content. ENTITY's knowledge_absent wording should keep "not read", not "unknown".

---

## SUGGESTED YAML PATCHES (for the entity-tracker's next UPDATE; not applied)

```yaml
suggested_patches:
  - entity: "august-fenn.traits"
    action: "add"
    value: "Navy celestial navigation, 1952, on a destroyer off Korea; read Graves's Claudius on the way over (by plane after CRIT-002); landed in snow, learned 'Forty-one' / Claudius at the thaw in Amphissa; two years in Phocis; Misenum fleet captains' stars before 62; Puteoli since c. AD 64 (eleven years of Kalends marks; the basil eleven years); teaches rich men's boys triangles"
    reason: "ch-25 l.170-186, 210, 254, 422"
  - entity: "august-fenn.knowledge"
    action: "add"
    value: { fact: "Mara keeps her tremor notes in the back of his notebook (content unread)", learned_chapter: 25, method: "told_by:mara-reyes" }
    reason: "l.362-366; knowledge_absent should read 'content of', not existence"
  - entity: "valens.knowledge"
    action: "add"
    value: { fact: "Mara and the Chaldean share a language no one here speaks; he believes her; the Chaldean 'knows' the door", learned_chapter: 25, method: "witnessed", note: "does not follow the English: no date, no law; after WARN-01 not the gate either" }
  - entity: "lucius"
    action: "update"
    value: "early spring AD 75: ~8 months; crawls, pulls up on a robe, nurses; horoscope promised by Fenn with his first letter"
  - entity: "plot_threads.fenn-correspondence"
    action: "create"
    reason: "l.406-414: he will write, send his tables 'every figure' and Lucius's stars; address = the mender's shop beside Grata's"
  - entity: "august-fenn.possessions.fenns-zippo"
    action: "update"
    value: "on the page as 'a little brass oblong' / 'a cigarette lighter' (unnamed); handled 4x; never lit"
```

---

## Repair log (book-editor, 2026-10-23)

Pre-repair copy: scratchpad only (not in the book folder). After: shape 7,499 words (style 7,555), dialogue 49% (show/tell 49.3%, shape 49), em-dash 3, and-chains 6. `bash tools/check_chapter.sh 25` prints ALL MECHANICAL GATES CLEAN. `tic_report.py --echoes 25`: 0 echoes, 0 command echoes, 0 spoken-line echoes.

**CRITICAL**
- CRIT-001: done. Changed to "at her own door with her knees aching".
- CRIT-002: done. "boat" → "plane".
- CRIT-003: done, as the audit wrote it ("My other copper … I reached for it … I let it lie.").
- CRIT-004: done, all five. l.54 "His mouth came open." · l.80 "He watched our mouths." · l.82 cut. · l.426 "and at Valens" cut. · l.414 is not the audit string: "his eyes went over my hands" made "his eyes went" 3x book-wide, so it now reads "he looked my hands over slowly, taking his time about it now". This still leaves the look on the mending hands and cuts the second "pale eyes".
- CRIT-005: done. "nudged the pot"; "He had the hour from me, as near as …".
- CRIT-006: done. "A long life, under his own fig tree."
- CRIT-007: done. "let out of doors in the dark".

**WARNING**
- WARN-01: done, and taken further. Cut "outside the Nuceria Gate" at l.156. The carter's story at l.254 also said "a tomb by the Nuceria Gate" in Valens's hearing, so it now reads "a tomb outside the walls". "Nuceria" appears 0 times. Valens hears no gate, no date he can parse and no rules.
- WARN-02: done. "my legs had gone"; "A laugh came first, with the other thing right behind it, so close …". I used this instead of "It began as a laugh" because "It" had no clear referent after the legs. Also "My hands saw the drops" and "My hand had gone to the flap". "without me" 0, "sound I made" 0. "no part in" stays only on Fenn's left hand at l.38. The core is kept: fused laugh/tears, one fight for breath, the hands saving the papyrus.
- WARN-03: done. Cut "pink to the collar of the robe".
- WARN-04: done. Cut "that nobody had disturbed".
- WARN-05: done. Cut "as Lucius preferred to travel"; "Lucius glared at the gulls"; cut the l.270 clause.
- WARN-06: done. "On the cover it read A. J. FENN."
- WARN-07: done. "with the vowels in his nose".
- WARN-08: done, differently. The audit's "that year" still lets a February quake explain a July opening. I cut the Aegean clause entirely. Fenn's account now runs: the ground moves hard, the door opens, and that is how the Corycian went for him. His own floor that "tipped on me like a boat" (l.174) is the movement, so the "hours, never days" rule holds with no added words.
- WARN-09: done, differently. The narration no longer holds the pregnancy at all. The child "in me, unguessed" at the Ides could predate conception (Ch.20 has the nausea in November, about the Kalends). With the news gone, the rest of the paragraph only restated Mara's next line (bed, mile, rain), so it is now one sentence: "A Girard Avenue man had sat on Eros's bench in the wet with a blanket over his ears and waited for a door to open." Grata's naming stays Ch.20's alone.
- WARN-10: done. "to breathe" → "to open". "breathe/breathes/breathed" now appear only in Fenn's mouth.
- WARN-11: done. Cut the second "Since Claudius.", the second "Give or take." and the first "Nothing surprises me.". Kept "steals home, steals home" and "Shut tight."
- WARN-12: done. Cut the two-finger gesture → "Twice. I had it for seventy-one."
- WARN-13: done. Cut l.230's first two sentences and l.234's list.
- WARN-14: done. "down to the goat that ate your postcard."
- WARN-15: done. "and spoke in Greek."
- WARN-16: done. "You didn't lose it, over here?"
- WARN-17: done. "hosing down her steps".
- WARN-18: skipped here. The Ch.26 outline cascade is the orchestrator's. Ch.25 is unchanged, as the audit directs.
- WARN-19: done and extended. l.430 "he said", l.432 "Fenn said, turning fast", l.204 "I said". At l.276 the tag is just "Fenn said": "Fenn said to Valens" was a cross-chapter echo and "said in Greek" hit the 3x gate, and "sir" plus the courtly register carry the Greek. The told-tags left are l.46 (to the lighter, by design) and l.198, so the close stands alone.
- Brief item, Fenn never lists: as well as CRIT-006, I cut "the runs and the gaps," from l.314's appositive and cut "and it all comes out" from the l.328 three-beat ("the runs fit, and the gaps fit.").

**INFO**
- INFO-01: done. Header now says Em-dash 3, and the word count and dialogue % are re-synced.
- INFO-02: done. "after the big outs". The first two tries ("when he got a man out", "coming off the mound") tripped the tic and echo gates.
- INFO-05: done. "and that's closed too".
- INFO-07: done. Cut "first thing," at l.444.
- INFO-08: done. Cut "if it kills me".
- INFO-06: skipped. "five years" is a round figure in a fit, and "more than four" reads as a correction.
- INFO-03, INFO-09 (protected by disruption), INFO-04, INFO-10 to INFO-16: no action, per the audit.

**For the bible/entity sync:** Fenn's lighter look is now "looked my hands over"; "turns it a shade further" → "nudged the pot a shade further". The carter's tomb is "outside the walls". The Ch.25 pregnancy reference is gone from the narration. Mara's sixth laugh shape (fused with tears) is SPENT.
