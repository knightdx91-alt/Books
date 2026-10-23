# Hook-Craft Report: Chapter 25 "Augurinus"

Turning point (the WHEN, ~60%). One scene, no breaks. Ledger: OPEN `scene-set` / END `punch`. **No edits made.** Both ends
work, so the file is unchanged.

## Opening (Hook)
- **Type:** SENSORY IMMERSION (a place opener). It is not QUESTION ✓.
- **Text:** "It was the first fair week after the sea opened, and the fish quay at Puteoli smelled of brine, pine tar and the
  wet straw the tunny came packed in. … The blood ran off down channels in the floors and under the sills into the gutter, and
  the gulls stood in it to their ankles and fought over what came out."
- **Score: 7/10.** Information gap 1/3, emotional pull 2/3, voice 2/2, connection 2/2.
  - **Gap:** the first noun that matters is "Puteoli". Ch.24 planted Grata's husband's Chaldean there, and the chapter title
    primes it. The real hook comes at the end of paragraph 2 (about 210 words in): "a language no one had heard before … I had
    not let them get as far as a name." That is a withheld word the reader can supply, and it is what keeps the opening from
    sagging.
  - **Pull:** the gulls standing ankle-deep in blood are the wrong note in the sensory field, so the sensory beat carries
    tension and isn't just set dressing.
  - **Voice:** it reads as Mara's own precise, material eye ("the tunny came packed in").
  - **Connection:** it moves straight on from the birth chapter's room to the open harbour, eight months later, with no recap.
- **"Earns its place fast":** it does, at the threshold. "After the sea opened" means the sailing season. It's period-specific
  rather than weather, and it does work later: the captain on the stair, the ship that sails at dawn, Fenn casting ships'
  hours. The measured quay, stair and room section (budgeted at 900 words) is the slow ground that makes the "quick recognition"
  beat at the lighter hit hard. Cutting it shorter would blunt that snap.
- **Rewritten:** no.
- **Alternatives considered (not applied):** IN MEDIAS RES on the split third tread (est. 7). CONTRAST, "The Chaldean behind
  the fish sheds kept a cigarette lighter on his sill" (est. 8). Both break the binding `scene-set` row, and the CONTRAST
  option would give away the recognition, which is the chapter's best beat.

## Ending (Pull)
- **Type:** DECISION POINT (the refusal, as her answer to "You'll be on that road"). It is not QUESTION PLANT ✓.
- **Text:** "…You ever been to Connie Mack?" / "I had been driven past where it had stood. … and explained the fire to me. I
  kept the fire to myself." / "I told him his arithmetic was wrong."
- **Score: 9/10.** Forward pull 3/3, emotional charge 3/3, unpredictability 1/2, promise 2/2.
  - **Forward pull:** every reader knows 79 is right. She has just refused the only date, with her son in the room, so the
    dramatic irony carries straight into Ch.26 and the tables Fenn has promised to send.
  - **Emotional charge:** two withholdings sit side by side. She keeps back a true thing out of mercy (his ballpark burned) and
    says aloud a false one out of need ("please be wrong"). That gap is the turning point, and it is shown without being
    explained.
  - **Unpredictability:** 1/2 because the refusal was already argued in the room. The surprise is where it lands: as the answer
    to a ballgame invitation.
- **Law checks:**
  - Seven words, a single-sentence paragraph, narrated (signature `punch`) ✓.
  - **NO FORESHADOWING:** clean. There is no "would" and no reach forward. "You'll be on that road" is Fenn's belief, spoken
    by him.
  - **No aphorism** ✓.
  - **No device as a scene-button:** the lighter, basil, notebook and coppers are all settled earlier, and none of them ends
    the scene ✓.
  - **Echo:** "arithmetic" appears in Ch.11 and Ch.15, both times in other contexts and not as a spoken line. No new speech
    was added.
  - **Last-sentence compression:** the energy goes from Fenn's run, to three sentences of memory, to a stop. A dead stop, as
    the reading-speed brief asks.
- **Turning-point standard:** met. The structural turn (she has the WHEN and refuses it) lands in the last line and isn't
  glossed.
- **Rewritten:** no.
- **Alternatives considered (not applied):** EMOTIONAL GUT PUNCH, ending on "I kept the fire to myself." (est. 8). That breaks
  the ledger's mandated line and loses the refusal. QUESTION PLANT is barred.

## Chain Check
- **Previous chapter pull type:** QUESTION PLANT (Ch.24, the watch).
- **This chapter hook type:** SENSORY IMMERSION. Not QUESTION ✓.
- **This chapter pull type:** DECISION POINT. Not QUESTION PLANT ✓.
- **Transition momentum (24→25):** adequate to strong. The time thread (the watch, the uncertain hour) gives way to a chapter
  about the WHEN, and the boy's birth hour comes back in at the close, unforced.
- **Next chapter (Ch.26 "Letters in English"):** opens on a document (Fenn's letter). The pull feeds it: yes. "I'll write
  to you … I'll send you my tables" against "I told him his arithmetic was wrong" sets up the letters and the unopened tables.
  **For Ch.26:** the hook should not be SENSORY and the pull should not be DECISION POINT.

## Ripple Effects
- Previous chapter connection: OK.
- Next chapter connection: OK. Nothing in the letters is pre-empted. Note for Ch.26: the address Mara gave and Grata's name in
  charcoal are already set up, so they don't need restating.

## Note (not changed)
- Narrated "kept" withholdings recur three times (l.10 "had kept from her", l.382 "I kept it", l.446 "I kept the fire to
  myself"). This is by design, since the heroine withholds, and the gates pass it. Flagged for the disruptor/evaluator only in
  case the verb starts to read as a refrain.

## Type Diversity
- Ch.20 VOICE / REVELATION → Ch.21 IN MEDIAS RES / QUESTION PLANT → Ch.22 SENSORY / DECISION POINT → Ch.23 CONTRAST /
  EMOTIONAL GUT PUNCH → Ch.24 QUESTION / QUESTION PLANT → **Ch.25 SENSORY / DECISION POINT**. No consecutive repeats.
  TICKING CLOCK is still the only hook type never used.

## Verification
- `python3 tools/shape_check.py books/the-hour-of-ash --strict` gives Ch.25 `scene-set` / `punch` and SHAPE CLEAN.
- `check_chapter.sh 25` was not re-run because no edit was made. The writer's header records it as ALL MECHANICAL GATES CLEAN.
