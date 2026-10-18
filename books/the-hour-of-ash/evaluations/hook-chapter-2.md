# Hook-Craft Report: Chapter 2 — Fenn's Notebook (run 2)

**Result: NO EDITS.** The opening and the ending both clear the floor and hit their ledger signatures
as written. The chapter file is untouched.

Ledger row (binding): open = document (a 1967 Fenn entry, italic) → `narrative`; end = document
fragment (Fenn's last entry, July 1968, cheerful) → `long-fade`, with no narrator comment after it.
Checked mechanically with `python3 tools/shape_check.py books/the-hour-of-ash`: Ch.2 computes as
**open `narrative`, end `long-fade`**. RESULT: SHAPE CLEAN.

Floors: romance/commercial 7 for both hook and pull.

---

## Opening (Hook)
- **Type:** VOICE. Fenn's boyish, self-delighted voice is the hook. A sister who thinks a scholiast is
  a foot doctor, a man who refers to himself by full name as he cuts a German's pages "with his
  thumb", Father Kostas paid in a roast pork sandwich. The information gap (a library in a cave) is
  carried inside the voice, so the paragraph holds together as one type. It is not CONTRAST, which
  Ch.1 used.
- **Score: 8/10** (Information gap 2/3, Emotional pull 2/3, Voice 2/2, Connection 2/2)
  - Information gap 2: "scholiast" stops the reader for a moment, and the paragraph pays it off
    quickly with "the cave of the nymphs on Parnassus, and they are there." The pull is real, but it
    takes a long paragraph to arrive.
  - Emotional pull 2: the cheer is charming. Ch.1 already told the reader (through Szabo) that this
    man "didn't come back", so the warmth casts a shadow without the text pointing at it.
  - Voice 2: this is unmistakably Fenn and nobody else. American, 1967, a Navy man, and there is no
    numbering or listing.
  - Connection 2: Ch.1 closes on the lit lid of the cigar box. Ch.2 opens inside the notebook. The
    bridge is object to object, with no recap.
- **Ledger check:** the first sentence is "*Thanksgiving, 1967, and Margaret has decided that a
  scholiast is some kind of foot doctor.*" It has **15 words** and is in italics. "Thanksgiving" is not
  one of the detector's time openers, so it computes as `narrative` (9–27). ✓
- **Banned-opener scan:** no weather, no waking, no recap, no establishing shot, no define-by-negation,
  no metacognition. No foreshadowing either: the 1967 horizon is Fenn's own.
- **Rewritten:** no.
- **Alternatives considered:**
  - QUESTION. Lead with "The Library of Alexandria, Margaret, the whole works, sitting in a cave on a
    mountain." (7). It is louder, but it moves the payoff ahead of its setup and takes away Margaret's
    joke. It would also mean rebuilding the paragraph, which is outside hook territory.
  - IN MEDIAS RES. Open on Fenn slitting the pages in the library (7). This loses the
    Margaret/Thanksgiving frame, and the July ending's "Margaret can stop telling the girls at church"
    depends on that frame.

## Ending (Pull)
- **Type:** EMOTIONAL GUT PUNCH, carried entirely by dramatic irony. Four paragraphs earlier the
  consulate carbon (16 September 1968: one overcoat "forwarded to next of kin, Miss Margaret Fenn")
  told the reader he never came home. The last entry is cheerful and specific: kite string, washed
  shirts, "back before Labor Day", a sunburn on Margaret's front steps. The narrator says nothing, and
  the reader supplies the irony. It is not QUESTION PLANT, which Ch.1 used.
- **Score: 8/10** (Forward pull 2/3, Emotional charge 3/3, Unpredictability 1/2, Promise 2/2)
  - Forward pull 2: "Going in tomorrow first thing with the good flashlight" sits next to the frame
    line "The night before the flight". Both are going in tomorrow, and the reader makes the
    connection without being told. Ch.3 is the cave.
  - Emotional charge 3: the cheer is set against the "small leaning hand" where "the pen had barely
    marked the page". The cold "stayed long enough for a whole cigarette, which is the longest yet."
    The devastation sits in the specifics, and nobody names it.
  - Unpredictability 1: once the consulate carbon has been read, the reader expects irony. The
    details (the Inquirer, the sunburn, the drachma refused) are fresh, but the move can be seen
    coming.
  - Promise 2: the notebook's arc, from confident capitals to an exhausted hand, is completed. The
    flight in the morning is opened.
- **Ledger check:** the final sentence is "*Back before Labor Day, and Margaret can stop telling the
  girls at church I'm in Mexico, because I'll be sitting on her front steps with a sunburn and a story
  she won't believe until she reads it in the Inquirer.*" It has **40 words**, so `long-fade` (25+). It
  is the last line of the file, with no narrator sentence after it. The closing paragraph has 5
  sentences (Ch.2 is not on the one-sentence-closer list). ✓
- **Scene-button check (writer warning):** passes. The line is not clipped or set apart, and it is not
  built to click shut. It is a run-on, garrulous Fenn sentence in the middle of his thought, with a
  boast at the end. It has no aphorism, no forward gesture in narration and no em-dash. The "girls at
  church" / Mexico callback to the February entry is content the outline requires (beat 8). The exact
  phrase "the girls at church" now has **2 uses**, both in Fenn's documents. That is under the 3+
  tic_report threshold, but **do not use it again anywhere in the book.**
- **Midnight Test:** the reader turns the page. The man went in on 22 July and his coat came home
  without him. She flies tomorrow.
- **Rewritten:** no.
- **Alternatives considered:**
  - CLIFFHANGER. End on "Going in tomorrow first thing with the good flashlight and a ball of kite
    string." (7). At 16 words it computes as `quiet`, which breaks the ledger. It also reads as a
    button and drops Margaret, who carries the irony.
  - DECISION POINT. A narrator beat after the entry, closing the notebook and putting it in the
    duffel (6). The ledger forbids any narrator comment after the document.

## Chain Check
- **Previous chapter pull type:** QUESTION PLANT (Ch.1, the lit lid of the cigar box)
- **This chapter hook type:** VOICE
- **Transition momentum (Ch.1 → Ch.2):** strong. The unread notebook on the table becomes the notebook
  being read.
- **Next chapter hook type (planned):** Ch.3 opens on a long sensory spiral of the plateau
  (`long-spiral`), which will most likely be SENSORY IMMERSION. Ch.3 ends on unfinished action
  (`punch`), most likely CLIFFHANGER.
- **This chapter pull feeds into next hook:** yes. Fenn's "going in tomorrow" leads into Mara on
  the mountain, and the dread the reader carries over meets a plateau described with no portent
  (the no-foreshadowing law holds, and the dread stays with the reader).

## Guidance for the Ch.3 pass (variety rule)
- **Do NOT use as Ch.3 hook:** VOICE. (CONTRAST is also best avoided, since Ch.1 used it.)
- **Do NOT use as Ch.3 pull:** EMOTIONAL GUT PUNCH. The planned ≤7-word "wrong season" close reads
  naturally as CLIFFHANGER (or REVELATION). Either is clear of Ch.2.

## Ripple Effects
- Previous chapter connection: OK. The notebook is opened in the father's kitchen with the machine
  blinking over the empty greeting, which matches the end of Ch.1.
- Next chapter connection: OK. The notebook is packed last, on top of the duffel. The consulate carbon
  is back in its pocket. The flashlight is packed. The flight is "tomorrow". This is consistent with
  ENTITY_STATE (the fenn-notebook is packed in Ch.2, and the consulate slip fact is learned in Ch.2).

## Type Diversity (running tally)
| Ch | Hook | Score | Pull | Score | Edited |
|---|---|---|---|---|---|
| 1 | CONTRAST | 9 | QUESTION PLANT | 8 | no |
| 2 | VOICE | 8 | EMOTIONAL GUT PUNCH | 8 | no |

Consecutive same-type hooks: NONE. Consecutive same-type pulls: NONE.
