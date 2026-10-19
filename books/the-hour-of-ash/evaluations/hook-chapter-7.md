# Hook-Craft Report: Chapter 7 — The Laws of Belonging (run 2)

**Result: NO EDITS.** The opening and the ending both clear the threshold of 7, both hit their ledger
signatures as written, and neither breaks the consecutive-type rule. The chapter file is unchanged.

Ledger row (binding): Essayistic (*claim → evidence → cost*) · open = claim/opinion → `narrative`
(first sentence of 9–27 words) · end = question → `question` (a real question Mara has in the present
scene, not a rhetorical button or an aphorism).

I checked the text read-only, from /home/user/Books:
- `python3 tools/shape_check.py books/the-hour-of-ash`: Ch.7 computes as **open `narrative`, end
  `question`** (6,366 words, 3 breaks, dialogue 21%, median sentence 17). RESULT: SHAPE CLEAN across 7
  chapters. `narrative` appears twice (Ch.2 and Ch.7), not consecutively. `question` appears for the
  first time.
- `bash books/the-hour-of-ash/tools/check_chapter.sh 7`: everything clean (style incl. foreshadow 0,
  grammar, rhythm, voice-wear strict, tic gate, echo scan 0, shape).
- `python3 books/the-hour-of-ash/tools/tic_report.py --echoes 7`: **0 echoes**.

Barred types for Ch.7 (consecutive rule, from the Ch.6 report): hook IN MEDIAS RES, pull OMINOUS PROMISE.
Neither is used.

---

## Opening (Hook)
- **First sentence (27 words, at the top of the 9–27 band):** "A woman in Phocis in the second year of
  Vespasian belonged to somebody, and the first thing the town did with a stranger was work out who."
- **Type:** VOICE. This is the chapter's thesis, given in Mara's voice: a dry, flat claim from an
  outsider who reads the town as a system. The next sentence ("the way a clerk at a counter wanted a
  zip code, because the form had a box for it") is the 1998 conservator explaining Phocis to herself,
  and no other narrator in the book could have written it. The opening is not a CONTRAST hook. The
  claim is historically plain, and nothing collides in it. It is not a QUESTION hook either, because
  it is not a statement that "cannot be true".
- **Score: 8/10** (Information gap 2/3, Emotional pull 2/3, Voice 2/2, Connection 2/2)
  - Information gap 2: "work out who" turns the claim into the chapter's question, *whose will she
    be?* By sentence 5 the stakes are spelled out: "a woman with nobody was a piece of luck lying in
    the road for whoever bent down first." The gap is implied in sentence 1 and becomes urgent only in
    sentence 5, so it scores 2 rather than 3.
  - Emotional pull 2: the register is cool and wry on purpose. The menace builds through the five
    sentences (men slowing in the lane, then the luck in the road) and nobody names it. That is right
    for an essayistic chapter, and it gives up some immediacy.
  - Voice 2: the zip-code clerk and the form with a box. These sentences set up the clerk scene that
    pays the chapter off, and the setup is never flagged.
  - Connection 2: Ch.6 closed on Valens's theory that she belongs to "a big house" and that men will
    come to claim her. Ch.7 opens by saying that here every woman is somebody's, and then the town
    works out whose. His misreading becomes the chapter's subject without a word of recap.
- **Rewritten:** no.
- **Alternatives considered (not applied):**
  - CONTRAST: "In Phocis that winter the worst thing a woman could be was free." It sounds louder, but
    it is an aphorism in the opening position, and it uses up the irony of the clerk's later "free".
    Est. 7.
  - TICKING CLOCK: open on the census ("The council wanted every house in Delphi on wax before the
    governor's men thought to ask."). That pulls the register to the front and breaks *claim →
    evidence → cost*, so the chapter would open on the evidence. It is off-ledger. Est. 7.
  - QUESTION, as a statement that pivots on what is missing ("The first thing Delphi wanted from me
    was not my name."). This is a define-by-negation shape, which is a retired reflex. Est. 6, and
    barred.
- **Note (flagged only, not changed):** sentence 2 begins "Nobody asked it unkindly". The dialogue
  polish counted 3 sentence-initial "Nobody" openers in the narration. One in the opening paragraph is
  not a device, and recasting it would weaken the hook's second sentence. The disruptor or editor can
  thin the other two if the count matters.

## Ending (Pull)
- **Last four sentences:**
  > I tipped the water into the store jar and watched it climb to the shoulder. Over Kallia's roof the
  > cliffs were white to their rim, and past the rim, out of sight from the court, lay the plain under
  > its snow, then the firs, and above the firs the dark arch and its painted letters. In November the
  > gray mule had needed the better part of a morning to carry me from the cliff top to the cave. How
  > far was it, at night, on foot, from wherever the women danced to the cave?
- **Type:** QUESTION PLANT, asked in Mara's present thought. Kallia has just said the women go up
  "Onto the plain" at night and added "Not as high as your cave." Mara is working out the distance
  from the dance to the door. The question she asks herself is practical. The question it plants in
  the reader is *will she slip away from the rite and try the door again?* She never says that, and
  the reader feels it.
- **Score: 8/10** (Forward pull 3/3, Emotional charge 2/3, Unpredictability 1/2, Promise 2/2)
  - Forward pull 3: Ch.6 showed the door shut. The reader has just watched her become "Maira", of
    Kallia's house and in her keeping, answer to "Mera" at the water, and lose her own zip code. Now
    she is calculating the route back to the cave. The reader has to see whether she goes.
  - Emotional charge 2: the charge is the contradiction. In the same month she has been relieved to be
    somebody's, and she still measures the way out. The paragraph stays cool and logistical (a mule, a
    morning, a distance) and never states what she feels, which is correct. That restraint keeps it
    below 3.
  - Unpredictability 1: Kallia's "Not as high as your cave" points at the turn just before it comes,
    so an attentive reader sees it coming a line early. The surprise is quieter: after the chapter's
    surrender she has not let go of the door at all.
  - Promise 2: the chapter keeps its promise (she belongs, and it cost her). It opens a new one, and
    Ch.8 beat 3 (she slips off to the cave) pays it within one chapter.
- **Is it rhetorical?** No. The question has a factual answer, and she does not know it. She has one
  data point, set in the sentence before (by mule, by day, from the cliff top, the better part of a
  morning). She needs a second one (on foot, at night, from somewhere on the plain she cannot yet
  place, hence "wherever"), and she cannot get it. It is arithmetic she cannot finish, with a plan
  depending on the result. No answer is implied, and the line is not a "but would it last?" button.
- **Does it reach forward? (no-foreshadowing law, voice-dna §0):** No. The tense is the narrative past
  of her thought in that moment ("How far was it"). There is no "would", no foreknowledge formula, no
  outcome tag and no significance tag. What it contains is a present intention, which the law allows:
  she is planning, and the narration does not predict whether the plan works. Her knowledge stops at
  the courtyard. The pan from the cliffs to the plain to the firs to the arch happens "out of sight
  from the court", so it is her mental map of the route and not a camera moving ahead of her. None of
  the families A–E are present (foreshadow gate 0).
- **Retired reflexes:** this is not a closing aphorism, since nothing is generalized about home,
  belonging or fate. It is not a device used as a scene-button: the cave is the plot, not a recurring
  phrase or object clicked shut, and the line does not echo the chapter's opening.
- **Continuity check on the data point:** Ch.6 has Valens give "In summer, a morning. In this, a
  morning and more" for the whole trip from town. Daylight came on the last of the cliff, and the gray
  carried her across the plain to the cave. "The better part of a morning … from the cliff top to the
  cave" is consistent with that. "Painted letters" is consistent with Ch.6's letters "still red at the
  bottom of their strokes".
- **Midnight test:** pass. The reader knows the door was shut, and she is measuring the way to it in
  the snow, at night, on foot. They turn the page.
- **Rewritten:** no.
- **Alternatives considered (not applied):**
  - Speak the question aloud to Kallia ('"How far is the plain from the cave?" I said.'). It still
    ends on a `question`, but Kallia hears the plan, and she would answer or forbid it in a line of
    her own. The private intention becomes a conversation, and "at night, on foot" is lost. Est. 7.
  - Shorten it to "…from the dancing to the cave?" It is tighter by two words, but it loses
    "wherever", the one word that carries what she does not know. Est. 7–8, and not clearly better.
  - DECISION POINT: end on a declarative ("I would go up with them, then.") That fails the `question`
    signature, turns a calculation into an announcement, and leans toward forward-statement. It is
    off-ledger. Est. 7.
- **Note (flagged only, not changed):** "watched it climb to the shoulder" is the chapter's fourth
  water-rising-in-a-jar beat (L152 "watched it fill", L230 "I watched the water rise", L234 "The water
  came up into its neck", L398). The gesture gate is clean, and here the beat does a job. At the spring
  her eyes were kept on the jar out of submission. At the end her eyes go from the jar up over the
  roof to the route. I am keeping it for that turn. If a later pass trims the run, take one of the
  middle two, not this one.

## Chain Check
- **Previous chapter pull type:** OMINOUS PROMISE (character-voiced: "Men will come asking… You never had
  a watch.")
- **This chapter hook type:** VOICE.
- **Transition momentum:** strong. Valens's dread is about who owns her. Ch.7 opens on the town's
  question of whose she is, and the clerk who "does not ask" plays against his "men will come asking",
  as the Ch.6 report requested.
- **This chapter pull type:** QUESTION PLANT.
- **Next chapter hook (planned):** Ch.8 opens mid-dialogue, with Kallia instructing her about what
  not to say on the mountain (`dialogue`). By type it is likely IN MEDIAS RES, which is allowed after
  a VOICE hook.
- **This chapter's pull feeds the next hook:** yes. The question is about the mountain night, and Ch.8
  opens on Kallia's instructions for that night. The reader goes in already knowing Mara has a second
  agenda that Kallia's rules do not cover.

## Ripple Effects
- Previous chapter connection: OK.
- Next chapter connection: OK. For the Ch.8 writer:
  - Do not answer the distance question in narration at the top of Ch.8. Let the climb answer it.
  - Do not have Mara restate the plan. Ch.8 beat 3 delivers it.
  - The Ch.8 hook must not be VOICE, and the Ch.8 pull must not be QUESTION PLANT (consecutive rule).
    The ledger's quiet-image ending fits EMOTIONAL GUT PUNCH, which was last used in Ch.2.

## Type Diversity (running tally)
| Ch | Hook | Score | Pull | Score |
|---|---|---|---|---|
| 1 | CONTRAST | 9 | QUESTION PLANT | 8 |
| 2 | VOICE | 8 | EMOTIONAL GUT PUNCH | 8 |
| 3 | SENSORY IMMERSION | 7 | CLIFFHANGER | 9 |
| 4 | IN MEDIAS RES | 8 | REVELATION | 8 |
| 5 | QUESTION | 8 | DECISION POINT | 8 |
| 6 | IN MEDIAS RES | 9 | OMINOUS PROMISE (character-voiced) | 8 |
| 7 | VOICE | 8 | QUESTION PLANT | 8 |

- Consecutive same-type hooks: none. Consecutive same-type pulls: none.
- Hook types used: 5 of 6 (TICKING CLOCK unused). Pull types used: 6 of 6.
