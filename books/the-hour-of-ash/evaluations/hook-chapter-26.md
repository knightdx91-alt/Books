# Hook-Craft Report: Chapter 26 "Letters in English"

**Verdict: both ends work. No edits. The chapter file is unchanged.**

## Opening (Hook)
- **Type:** VOICE (a document: Fenn's birth letter). Not SENSORY IMMERSION ✓.
- **Score:** 9/10 (Information gap 3/3, Emotional pull 3/3, Voice 2/2, Connection 1/2)
- **Rewritten:** no.
- **First sentence:** *"A girl, holy cow, and the carter swears the kid has a set of lungs on her they can hear at the river."*
  It is 23 words by plain count (the writer's header says 22), so it sits inside the ledger's 9–27 either way, and shape_check
  reads it as `narrative` ✓.
- **Why it grabs:** the birth happened offstage, and the reader learns of it secondhand, from the wrong person, in the wrong
  language, in a cheerful 1960s Philadelphia idiom. Outline beat 1 is met: greedy, loud, Aelia already in the world. The
  connection score loses a point because the leap from Ch.25 ("his arithmetic was wrong") to a delivered baby is a deliberate
  hard cut. It still works: Ch.25's promised letters arrive at once, and the voice is the bridge.
- **The ticking-clock line ("She'll be near four the summer we go, by my book…"):** **legitimate. Allowed.** It is Fenn, in the
  scene, stating his own plan in his own letter. He has believed in the 79 date since Ch.25 and keeps his own reckoning
  ("by my book"). The arithmetic is consistent: born 75, near four in 79. The narrator makes no comment on it. Her only later
  reference is a neutral list of the letter's contents ("the rope walk and the bridge and the peanuts and the summer", l.18),
  with no gloss, no significance tag and no dread. Nothing in the chapter comes back to it.
- **Why the hook is not TICKING CLOCK:** the line falls in the letter's second paragraph, outside the 3–5 sentence hook
  window, and the opening's pull comes from personality and not from a deadline. Moving the line to the front to fill the
  unused type would turn the chapter's first breath into dread. It would come close to narrator-level emphasis on 79 and would
  break the joy that the birth letter carries. TICKING CLOCK stays unused rather than forced.
- **Alternatives considered:** TICKING CLOCK (the "near four" line moved to the front): 7, wrong register, rejected.
  CONTRAST ("The letter was written on the reverse of a stranger's future." as the opener): 7, but it breaks the ledger's
  document open.

## Ending (Pull)
- **Type:** EMOTIONAL GUT PUNCH (quiet register: tenderness by understatement). Not DECISION POINT ✓.
- **Score:** 8/10 (Forward pull 2/3, Emotional charge 3/3, Unpredictability 2/2, Promise 1/2)
- **Rewritten:** no.
- **Last sentences:** *His father rested a hand on his hair. "You can move now." / He sat on in the sun with his lip in her
  fist, holding her very carefully, until his father lifted her away.*
- **Why it works:** it is the named frame from the outline, and the writer found the image (the newborn's fist on her
  brother's lip, his eyes running, the breath out through his nose). The turn in the last two lines is that release is
  offered and refused: the boy keeps holding past permission, and the image ends on an adult taking the baby away. That gives
  the weight without one forward-reaching word. The last sentence is tighter than the paragraph before it, so the close
  compresses. There is no aphorism, no foreshadowing and no reflection.
- **Device-as-scene-button check:** passes. The shutter and the advance lever ("I thumbed the lever round for the next
  frame") come two beats before the end and are mechanical, not significance-tagged. The final line belongs to the children
  and the father, not the camera.
- **Promise:** 1/2. The chapter's implicit promise (the tables avoided) was kept in S7, and the close opens no new thread.
  Momentum into Ch.27 comes from the book's held irony and Fenn's relationship, which is right for a quiet ledger close. It
  does not pre-empt Cumae ✓.
- **Midnight test:** page turns. The reader is holding the photograph of these two children in a town the reader knows the
  end of, and nobody in the chapter says so.
- **Alternatives considered:** close on "You can move now." (QUESTION PLANT-ish, 6): weaker, and it loses the refused
  release. Close on the shutter (6): a device as scene-button, which is banned here.
- **Watch item (no action):** "very carefully" also appears in Ch.17 (twice) and Ch.21 (l.360). It is below the echo and tic
  gates, which pass clean, and here it is the outline's own image. Flagged for the evaluator only, in case a sixth use turns
  up later.

## Break transitions (7)
Letters brisk, domestic slow, as briefed. All hold momentum:
1. S1→S2 (bakers laugh → "His first letter had come…"): adequate. A backward step in time, recovered in two sentences by
   the walking night.
2. S2→S3 (the bone rolling → fifth week, the rope): strong. The jealousy section starts at once.
3. S3→S4 (Valens gives "goodnight" to the sleeper → daybreak "Goodnight." to Grata): strongest cut in the chapter. The
   wrong, happy use comes on the very next line.
4. S4→S5 (the street's Latin → the autumn letter): strong. The language axis carries across.
5. S5→S6 (Grata out in the rain → "The same carter brought his answer nine days after"): brisk, strong.
6. S6→S7 ("What a voicemail was, I did not explain." → the tables in sacking): strong. One withholding hands off to another.
7. S7→S8 ("I gave him the bone." → the bright day): adequate to strong. The bone carries straight into the final scene.

## Chain Check
- **Previous chapter pull type:** DECISION POINT (Ch.25, "I told him his arithmetic was wrong.")
- **This chapter hook type:** VOICE. Not SENSORY (Ch.25 hook) ✓.
- **This chapter pull type:** EMOTIONAL GUT PUNCH. Not DECISION POINT ✓.
- **Transition momentum (25→26):** strong. Ch.25 promised letters and the tables, and Ch.26 opens on a letter. The refusal
  carries forward into the tables avoided.
- **Next chapter (Ch.27 "Cumae"):** opens on an I-claim about what she expected of the Sibyl's cave. **For Ch.27:** the hook
  should not be VOICE and the pull should not be EMOTIONAL GUT PUNCH. Its ledger close is a long fade, so QUESTION PLANT or
  OMINOUS PROMISE (character-voiced only) fit.

## Ripple Effects
- Previous chapter connection: OK.
- Next chapter connection: OK. Cumae is not pre-empted. The invitation is Ch.27's to make.

## Type Diversity
- Ch.21 IN MEDIAS RES / QUESTION PLANT → Ch.22 SENSORY / DECISION POINT → Ch.23 CONTRAST / EMOTIONAL GUT PUNCH → Ch.24
  QUESTION / QUESTION PLANT → Ch.25 SENSORY / DECISION POINT → **Ch.26 VOICE / EMOTIONAL GUT PUNCH**. No consecutive repeats.
  TICKING CLOCK is still the only hook type never used, and this was deliberate (see above).

## Verification
- `bash tools/check_chapter.sh 26` (run unedited) prints **ALL MECHANICAL GATES CLEAN**.
- `python3 tools/shape_check.py books/the-hour-of-ash` gives Ch.26 `narrative` / `quiet`, which matches the ledger row.
- The mountain is not named in Ch.26 (grep clean). No spoken line was added and nothing was edited.
