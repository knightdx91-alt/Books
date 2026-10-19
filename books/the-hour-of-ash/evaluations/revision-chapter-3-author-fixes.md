# Revision note: Chapter 3, author fixes after the independent read (2026-10-19)

Source: `feedback/independent-review-ch1-5.md` (problems 1–3). Only `manuscript/chapters/chapter-3.md` was touched.

## Counts

| | Before | After |
|---|---|---|
| Words (`wc -w`) | 6,834 | 5,598 (−1,236) |
| And-chains (narration, 4+ "and") | 21 | 6 (the held crossing sentence + 5) |
| Credential asides (gate count) | 8 | 4 |
| Dialogue share | 5.8% | 6.1% |
| Scene breaks | 0 | 0 |

`bash tools/check_chapter.sh 3` gives clean results on every Ch.3 line. `tic_report.py --gate`: Ch.3 reads and-chains 6 (cap 9) and credential asides 4 (cap 4). There are no Ch.3 flags; the remaining flags are Ch.5's. The echo scan dropped from 27 to 20, and the 20 are all pre-existing. The first sentence, the held sentence and the last line are byte-identical.

## Cuts (first words of the cut text)

**Named by the review**
- Camera swap: "and then I had to show him everything. He had never held a camera…" through "That's the lever. The other one." The stone, the windowsill, "this was evidence", "For your mother"/Phoenix, his frame on her Pentax and "It is like a gun" all stay.
- Graffiti wall: "I went along the wall reading it as I would have read the underside of a pot…", "one man had added his regiment", "There were Greek names in Greek capitals…", "An E. WILKINS of Bristol…", "The newest cuts were white…", "Higher up, out of reach of any knife…" (the soot names), and "If it had come into my lab…". Kept: the raking light, the French 1840s–50s, the 1952 through the lieutenant, and the 1996 heart.
- French report: "Their report was in the university library in two fat volumes…" (with "caught once already"), "The plates showed…", "Some had been dyed or drilled…", "The floor still showed it." Kept: the dig, "more than twenty thousand knucklebones", Pan and the nymphs, and the goat's print.
- Toilet beat: cut to one sentence ("At half past twelve I peed behind the big stalagmite and begged Pan's pardon… optative…").

**Plateau / approach slack**
- "The road came across all of it from the Arachova side…" (the ski lifts) and "A white van was going along it…"
- "Out on the flat there were sheets of standing water…", "The map called the plain Livadi.", "with its bell hung in an iron frame…"
- The map paragraph folded to one sentence plus "He had read the map right… 1967…". Cut: "I had bought it at a kiosk… snowy summit…" and "A minute of latitude covered better than a mile…"
- "Lower down, a yellow-and-black metal sign… E4… I kept to the red." and "sometimes with an arrow under it and sometimes with a white bar…"
- The Delphi room: "It was a room over a shop that sold blue worry beads…" and "He had climbed to the cave day after day…" (this repeated the later Fenn paragraph). Also "leaning on the rail".
- Taxi: "He had taken the road out of his village…" and "He turned the car around in a spray of gravel…"
- "Every tray of his slides had begun with one.", "with silver-gray bark", "The ground under them was brown with needles…"
- German: "Something occurred to him then, and his face changed…", "revised his opinion of the duffel. 'You have a good sleeping bag.'…", the two-o'clock cloud warning plus "I'm staying up.", and "The old man on the stone left off with the nanny…"
- "and the sky above was a blue so hard and clean…"
- "He must have copied it out of a photograph in some library book…" (becomes "drawn too exactly for a guess")
- At the mouth: "There had been a fire in a ring of blackened stones…", "My sleeve was torn at the elbow…" / "A scratch I had not noticed…", and "as broad as a kitchen table".

**Cave / wait slack**
- "with a roof that went up into darkness… folds and draperies of stone" and "Stalactites hung from it in bunches…" (now "The floor was full of stalagmites…")
- "Fenn had known it from the sinkholes in Florida; I knew it from the crawlspace…"
- "I read Fenn's directions again by it…" and "The wall was cold and furred with wet."
- Cellar: "for the whole block" and "the real thing,"
- Postcard: "There was a telephone at the kiosk in Delphi… Ray having his fit." "Unwritten" stays.
- Fenn: "going down in the evenings to his beans and his goat…" and "I sat in his place with my bag packed… the bigger fool."

## Chain splits (sentence broken, not comma-swapped)
These were split at "and": the air/"hauling it in" sentence, the goats' bells, the German's description, the Olympus window, the wind/bird, "The floor sloped down… loose and stony", the cave-cold smell, "stood up too fast… piece of sky", the slab/crack, the dry cold "went in through the skin". The graffiti, WILKINS, French and Fenn chains went with the cuts. Five chains remain besides the held sentence, all left deliberately: the opener, the taxi ("whole arm… bag… me"), the second stop and wrapper, the procedure, and the 1989 bedroom.

## Credential asides
Kept: the procedure "for the interns" (counted twice by the gate), the raking light "in the lab", and the sherds seminar. Recast: "since the seminar" → "since", and "Every Monday in the lab I unpacked" → "Every Monday I unpacked". Cut: "If it had come into my lab…" and "I had read them cross-legged in the stacks".

## Not touched
The knucklebone, the procedure and "I pocketed it.", the wait in the dark, the cold at the crack, the crossing sentence, the blush, the exit, the four autumn signs, and "I stepped out into October."

## For re-evaluation
- Dialogue is 6.1%, still near the floor, because the cloud warning (dialogue) went.
- The E4 is now introduced only by the German.
- Entity bookkeeping (other agents' files): the Ch.3 cuts remove the room-over-a-shop detail, the kiosk phone call, and "caught once already" (the Hostile's continuity flag). ENTITY_STATE cites some of these as Ch.3 sources and may want a resync.
