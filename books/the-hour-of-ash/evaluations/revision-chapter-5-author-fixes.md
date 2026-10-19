# Revision note: Chapter 5, author fixes after the independent read (2026-10-19)

Source: `feedback/independent-review-ch1-5.md`, items 1–4. Only `manuscript/chapters/chapter-5.md` was touched.

## Numbers

| | Before | After |
|---|---|---|
| Words (`wc -w`) | 8,173 | 7,855 (−318) |
| Dialogue (show_tell) | 20.5% (~1,675 quoted words) | 20.2% (1,584) |
| Section words | ~1,300 / ~2,600 / 699 / ~3,160 / 415 | 1,261 / 2,364 / 695 / 3,104 / 414 |
| And-chains (narration, 4+ "and") | 17 (cap 9) | **7** |
| Credential asides | 9 (cap 4) | **4** |
| `* * *` breaks | 4 | 4 |
| First sentence (25w) / last sentence (66w) | — | byte-identical |

Gates: `bash tools/check_chapter.sh 5` all clean (style, grammar, rhythm, show/tell, voice-wear strict, tic gate, metaphor, shape). `tic_report.py --gate`: clean, and no Ch.5 flag. The echo scan shows the same 6 echoes the cycle-1 evaluator ruled functional. A seventh echo ("gone through the") came from my own cut joining two paragraphs, and I removed it by recasting the clause.

## Fix 1: the monument roll-call

The Way itself is about 250 words shorter (section 2: ~2,600 → 2,364). That is **short of the ~400 asked for.** The roll-call is mostly the guide's speech, and dialogue sat at 20.5%. After the first speech cuts (−110 quoted words), dialogue dropped to 19.5%. Following the instruction, I then trimmed narration around the roll-call rather than more speech, and kept one existing guide line by moving it. Cutting all the way to −400 would have pushed dialogue under 20% or forced cuts into the keep list.

Cuts:
- **Bull story** shortened by about 30 words. The herdsman, the tunny "so thick a boy could have walked out on their backs", the god's order and the tenth all stay, and so does "You will ask me why a bull."
- **Arcadians/Spartans** exchange cut (72w). Its line "Everyone beats somebody at Delphi…" was moved onto the boxer, as the cycle-0 evaluation suggested. It is the speech Mara stops listening to.
- **"the Arcadians had the same wet brown-gold shine"** cut from the painted-marble paragraph.
- **Cold-water boy** cut ("Cold water!… I had no obol."). The goat going up to its death stays, because the altar misreading needs it.
- **Siphnian silver/flooded-mine** speech cut. The rival is now set up with "He tells it all wrong, and he's from Amphissa.", and "I heard that." / "You were meant to." are intact.
- **Siphnian treasury** is no longer named, and its porch girls are cut. The frieze is now "the next treasury". The Egyptian blue line is kept, minus the evaluator's "scraped from a sherd from" clunk.
- **Boxer** reduced to "whose statue killed a man, which is another story and costs extra." This also removes the "twenty years" that repeated ¶147. "somewhere in the boxer I had stopped listening" is intact.
- Narration around the roll-call:
  - The second row of empty bases (25w).
  - "I had worked for a decade below street level… This was the first time…" (37w). This was the evaluator's #11 explanatory extension, and it was also a credential aside in spirit.
  - The laurel woman putting "the guide between herself and me" (30w). It repeated ¶41's "put her husband between herself and me".
  - "and I had walked round it twice … could not have said which it was" at the Athenian treasury. This answers the Hostile reader's flag.
- To hold dialogue at 20%, I made three small texture cuts outside section 2: the ox-cart (section 1), "and the country changed at every turn of it" (section 1), and the money-changer's exit (section 4).
- Kept whole: the painted marble, the open-day cast, "Who made it? Nobody asks that.", the sore feet, and the entire Kroton runner and base. The only change in that area is the next base's "where the saw had gone through" → "from the saw".

## Fix 2: and-chains, 17 → 7

I split or recast these sentences:
- Lion heads (¶43).
- Flake (¶153).
- **Beating:** "He hit me on the hip. I went backward…" and "I stood. He came down after me…". Both are shorter and faster.
- Herald's tablet.
- **Basin:** the 9-"and" sentence is now three: "The cold of it stopped my breath. I surfaced… I pushed the sleeves… where the cold bit into the welts, burned, and went numb."
- Kallia's foot under the overflow ("…with her skirt held up. She let the water run over her foot, then changed feet…").
- Mara's hands.
- "My arms were on fire to the shoulder."
- Lentils and smoke.
- The wet sock.

Left alone:
- The olive (strength #2).
- The temple anchor (#17).
- Dr. Pinsky (#28, byte-identical).
- Kallia's lamp-oil sentence.
- The watch sentence and the last sentence (the fade).

## Fix 3: credential asides, 9 → 4

Kept:
- "I had looked at polychromy through a stereo microscope" (1). "since graduate school" became "for most of my working life".
- The Josephus seminar, byte-identical (2).
- The guide's-mockery grammar, "every accent where the grammar had put it" (1).

Recast:
- ¶21: "the only one the grammar had given me" → "the only form of it I knew". The hired-man verb form still carries the point.
- The steps: "a word that was in none of my grammars" → "a word I had never seen written down".
- The date run: "the coins I had cleaned ~~in the lab~~ with a cocktail stick".
- Kallia's inspection: "a scar … from a scalpel ~~in my first year in the lab~~".

## Fix 4: the Greek clause (verbatim)

> It was a speech he had given ten thousand times, worn smooth, **in a town Greek far nearer my books than the boy's had been on the mountain,** and I followed every word.

## Checks
- No forward-gesture was added, and there is no 79 or Pompeii.
- Every new phrase was grepped against Ch.1–4, with 0 hits. The phrases checked were "town Greek", "nearer my books", "form of it I knew", "seen written down", "working life", "all wrong", "next treasury", "statue killed", "from the saw", "changed feet" and "went numb".
- No new gesture or prop handling was added, and the gesture layer is clean.
- US spelling throughout.

## For the next reader
- The Way is about 150 words longer than the author's ~400 target would have left it. Getting the rest means either letting dialogue fall under 20% (which needs an author ruling on the band) or cutting into the keep list.
- The Siphnian name and the silver joke are gone, so drop the evaluator's "Siphnian gold" re-read note.
- ENTITY_STATE and the character-bible were not touched, per instructions. Nothing in them depends on the cut lines except, possibly, a walk-on entry for the cold-water boy, the laurel woman or the ox-cart, if one exists.
