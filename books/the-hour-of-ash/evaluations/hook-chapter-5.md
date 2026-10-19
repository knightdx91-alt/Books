# Hook-Craft Report: Chapter 5 — The Sanctuary (run 2)

**Result: NO EDITS.** The opening and the ending both clear the floor of 7 and both hit their ledger
signatures as written. The chapter file has not been touched.

Ledger row (binding): Chronological (*walk*) · open = scene-setting by time → `scene-set` (outline
opening strategy: "It was most of a day down the mountain…") · end = long fade in the storeroom →
`long-fade` (25+ words, slow, no aphorism about time, no narrator comment, no forward-gesture).

Checked mechanically with `python3 tools/shape_check.py books/the-hour-of-ash` from the repo root. Ch.5
computes as **open `scene-set`, end `long-fade`** (8,269 words, 4 breaks, dialogue 21%, median sentence
17, which is the high gear). RESULT: SHAPE CLEAN across 5 chapters. Opening sigs: I-statement /
narrative / long-spiral / short-punch / scene-set. Ending sigs: quiet / long-fade / punch / dialogue /
long-fade. Long-fade appears twice, but not consecutively (Ch.2 and Ch.5), and no sig runs three in a row.

Types already used: Ch.1 CONTRAST / QUESTION PLANT; Ch.2 VOICE / EMOTIONAL GUT PUNCH; Ch.3 SENSORY
IMMERSION / CLIFFHANGER; Ch.4 IN MEDIAS RES / REVELATION. That leaves QUESTION and TICKING CLOCK as the
available hooks, and OMINOUS PROMISE and DECISION POINT as the available pulls. Ominous Promise is
barred outright by voice-dna §0 (families A–C), and a ticking clock would be invented for this chapter.

---

## Opening (Hook)
- **First sentence (25 words):** "It was most of a day down the mountain, and I spent the first hour of
  it walking toward a road that was not there."
- **Type:** QUESTION. Read flat, the sentence makes no sense: why walk toward a road that does not
  exist? Paragraph 2 gives the answer ("The morning before, a taxi had carried me across this plain on
  asphalt…"). She is still steering by 1998, toward the Arachova road, across the stubble of AD 70. So
  the question is answered inside the chapter and the hook keeps its promise. The time phrase sits in
  front of the question without diluting it, and the type is not one of the eight used in Ch.1–4.
- **Score: 8/10** (Information gap 2/3, Emotional pull 2/3, Voice 2/2, Connection 2/2)
  - Information gap 2: the reader already knows she is in the past, so the gap is less "what happened?"
    and more "does she know yet?" That is a real pull, but it is dramatic irony more than mystery.
  - Emotional pull 2: the night in the sheepfold, and a dog barking "like a car alarm on Baltimore
    Avenue at three in the morning". Homesickness is carried by her own frame of reference and never
    named. Then the dew-soaked canvas, and the granola pouch opened with her teeth.
  - Voice 2: dry, exact and physical, consistent with Ch.3–4. The one simile characterizes her; it
    does not explain anything.
  - Connection 2: Ch.4 ended with the boy pointing "Katō, katō. Delphous" and then naming her. Ch.5's
    second sentence has the boy leaving her "where the slope ran out" and heading off toward the smoke.
    The white space carries her one step on, with no recap.
- **Ledger check:** it opens with "It was", one of the detector's time openers, and runs 25 words
  (inside 9–27), so it is `scene-set` ✓. It is the outline's own line, extended.
- **Notes for the editor, outside a hook fix (below floor is the only licence to rewrite):**
  sentence 3 says "corner" twice in close succession ("along a wall to its corner and sat down in the
  corner of what smelled like a sheepfold"). Paragraph 2's "for an hour there was no road under my
  boots at all" repeats the first sentence's "first hour… a road that was not there". Both are minor,
  and neither pulls the hook under the floor.
- **Rewritten:** no.
- **Alternatives considered (scored as replacements; not used):**
  - TICKING CLOCK: "It was most of a day down the mountain, and I had eaten the last pouch but two
    before I set out." (6) The hunger is real, but it is not a deadline, and the urgency would be
    manufactured.
  - QUESTION, tighter version: "It was most of a day down the mountain to a town that had lost its
    road." (6) It is shorter, but it moves the strangeness off her and onto the town, and it loses the
    "walking toward", which is the character in motion.

## Ending (Pull)
- **Final sentence (66 words):** "Somewhere among the jars a mouse had found its way into the barley,
  and I lay in Kallia's storeroom on Kallia's mat under the goat-hair blanket with my wrist under my
  cheek, and listened to the mouse and the watch going about their two small businesses in the dark,
  one of them in the sack and one of them close beside my head, until I slept."
- **Type:** DECISION POINT. The decision is the penultimate sentence. With the watch ticking an inch
  from her ear, she works out how early she has to get the ashes out and the water in "to be on the
  cart track by full light, with the plain to cross after that, and the long climb to the firs, and
  the cave at the top of it by the middle of the day." This turns the vow made at the spring ("In the
  morning I would go back up") into a timed plan, made after she has been taken in. The choice is open
  to argument: on her first night with a roof she means to do the chores and then walk away from the
  only person who has taken her in, to sit with her hand in a rock crack. The final sentence then
  lets the plan go slack into the dark (mouse, watch, the borrowed mat) without restating it. There is
  no OMINOUS PROMISE and no forward-gesture: the plan is the character's present-scene intention, not
  narrator foreknowledge.
- **Score: 8/10** (Forward pull 3/3, Emotional charge 2/3, Unpredictability 1/2, Promise 2/2)
  - Forward pull 3: the cave is the only door home she knows of, and she has just scheduled her return
    to it. The reader needs to know whether it is open. Ch.6 opens with her in the cave.
  - Emotional charge 2: the boots set side by side "the way I left them by my own door at home". The
    sock with its small flat weight in the toe is touched without comment, as outline beat 6 requires.
    "Kallia's storeroom on Kallia's mat" says ownership twice, and none of it is hers. The goat-hair
    blanket smells of whoever slept under it last.
  - Unpredictability 1: falling asleep is the expected close. The mouse and the watch "going about
    their two small businesses" is the fresh element.
  - Promise 2: it delivers the chapter's promise (taken in as labor, not out of kindness; her name the
    one question not asked) and opens Ch.6's.
- **Sleep-ending check:** "Character going to sleep" is normally a banned pull. Here it is a deliberate
  ledger long-fade, the outline asks for a "slow fade in the storeroom", and the decision sits directly
  above it, so the midnight reader closes on an unanswered plan rather than on rest. It passes the
  Midnight Test because the next morning holds the cave.
- **Gentle-landing / aphorism scan:** the final sentence contains no time-aphorism, no generalization,
  no narrator comment and no "would"-forward construction. The watch is a voice-dna weight carrier
  rendered in fresh words; it is not a scene-button line. Nothing follows the sentence in the file. ✓
- **Ledger check:** 66 words, 25+, so `long-fade` ✓.
- **Rewritten:** no.
- **Alternatives considered (not used):**
  - DECISION POINT, compressed: end on the plan itself ("…and the cave at the top of it by the middle
    of the day."), cutting the mouse sentence. (7) That breaks the binding long-fade signature, and
    with the plan as the final words it would read as a forward-gesture.
  - EMOTIONAL GUT PUNCH, with the sock and microcassette moved to the last sentence. (6) It is barred
    by type diversity (Ch.2), and it would make the cassette a symbol, against the outline's "without
    comment".

## Chain Check
- **Previous chapter pull type:** REVELATION (Ch.4, "Nymphē.")
- **This chapter hook type:** QUESTION
- **Transition momentum:** strong. She is named by the boy, and the next line has her following his
  pointing.
- **This chapter pull type:** DECISION POINT
- **Next chapter hook (planned):** mid-action, `I-statement` (on her knees in the back recess,
  scraping at frozen earth). By type that is IN MEDIAS RES, already used in Ch.4 but not consecutive
  with this chapter.
- **This chapter's pull feeds the next hook:** yes. The decision to go up to the cave becomes the
  first image of Ch.6. The gap between "tomorrow" and "November, in snow" is something Ch.6's backfill
  has to account for honestly (Valens's refusal, the watch as payment), so the decision gets a real
  consequence rather than a one-line resolution.

## Ripple Effects
- Previous chapter connection: OK.
- Next chapter connection: OK. Ch.6 must show why the planned climb "by full light" did not happen the
  next morning (snow, money, Valens). The outline's backfill beat 2 already covers this.

## Types for Ch.6 to avoid (consecutive rule)
- **Hook: do not use QUESTION.** IN MEDIAS RES per the outline is fine.
- **Pull: do not use DECISION POINT.** The planned spoken-line ending can carry REVELATION, QUESTION
  PLANT, EMOTIONAL GUT PUNCH or CLIFFHANGER. It should not be another decision.

## Type Diversity (running tally)
| Ch | Hook | Pull |
|---|---|---|
| 1 | CONTRAST | QUESTION PLANT |
| 2 | VOICE | EMOTIONAL GUT PUNCH |
| 3 | SENSORY IMMERSION | CLIFFHANGER |
| 4 | IN MEDIAS RES | REVELATION |
| 5 | QUESTION | DECISION POINT |

All six hook types are now used except TICKING CLOCK. All six pull types are used except OMINOUS
PROMISE, which this book's §0 law effectively retires. There are no consecutive repeats.
