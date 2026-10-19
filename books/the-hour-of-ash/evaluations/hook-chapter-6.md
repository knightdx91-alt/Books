# Hook-Craft Report: Chapter 6 — Snow at the Cave Mouth (run 2)

**Result: NO EDITS.** The opening and the ending both clear the threshold of 7 and both hit their
ledger signatures as written. The chapter file is unchanged. Because nothing changed, the gates were
not re-run for this pass.

Ledger row (binding): In medias res (*crisis → backfill → after*) · open = mid-action → `I-statement`
(first sentence starts with "I" and runs more than 8 words) · end = spoken line → `dialogue` (the last
paragraph is speech).

I checked this mechanically with `python3 tools/shape_check.py books/the-hour-of-ash` from the repo
root. Ch.6 computes as **open `I-statement`, end `dialogue`** (6,767 words, 2 breaks, dialogue 37%,
median sentence 11). RESULT: SHAPE CLEAN across 6 chapters. I-statement appears twice (Ch.1 and Ch.6)
and dialogue appears twice (Ch.4 and Ch.6), but neither repeat is consecutive.

Types already used: Ch.1 CONTRAST / QUESTION PLANT; Ch.2 VOICE / EMOTIONAL GUT PUNCH; Ch.3 SENSORY
IMMERSION / CLIFFHANGER; Ch.4 IN MEDIAS RES / REVELATION; Ch.5 QUESTION / DECISION POINT. Five of the
six pull types are taken, so **OMINOUS PROMISE is the only pull type left**. The Ch.5 report treated it
as barred, but §0 does not bar it. §0 bans the *narrator* from reaching forward. It explicitly keeps
"present-scene dread", and its gate scans dialogue only for the foreknowledge formulas. A character
saying aloud, in the moment, what he expects to happen is present-scene dread. It is the one form of
OMINOUS PROMISE this book can use, and it is the form this chapter already uses.

---

## Opening (Hook)
- **First sentence (40 words):** "I had scraped the floor of the crack down to bare rock as far in as my
  arm would reach, and now I knelt at the bend with Kallia's ash shovel, chopping at a crust of earth
  that had frozen into plates."
- **Type:** IN MEDIAS RES. She is on her knees, mid-dig, and the reader has to infer the context (the
  cave, the cold seam, a month gone by). The ledger requires this type. IN MEDIAS RES was used in Ch.4,
  but Ch.5 sits between them, so it is not consecutive.
- **Score: 9/10** (Information gap 3/3, Emotional pull 2/3, Voice 2/2, Connection 2/2)
  - Information gap 3: Ch.5 ended with the climb planned for noon the next day. Ch.6 opens on earth
    "frozen into plates" and "a skin of rime", so time has passed and the reader does not know how
    much. "As far in as my arm would reach" says the obvious search is already finished, so the real
    question is whether the door is there at all. Paragraph 2 sharpens the question without answering
    it: "Nothing could have come through that crack that I would have known from the rest."
  - Emotional pull 2: in the first three sentences the desperation is physical (scraped to bare rock,
    chopping, cold under the palm), and nobody names it. It reaches full strength a paragraph later at
    "I dug anyway." The hook gives up a little immediacy so that the emotion stays implied. That is
    the right trade for this voice.
  - Voice 2: this is a conservator's eye. She sees the rime on the underside of each plate and the
    texture of the dirt. No other narrator in the book would notice that.
  - Connection 2: the chapter bridges from Ch.5's plan without restating it. The plan was "the cave at
    the top of it by noon", and here she is at the cave, in a different season.
- **Rewritten:** no.
- **Alternatives considered (not applied):**
  - A pure present-action opener ("I knelt at the bend with Kallia's ash shovel…") would drop the
    past-perfect lead-in. It is faster, but it loses "scraped… as far in as my arm would reach", which
    is what tells the reader the search has already failed once. Est. 8.
  - A TICKING-CLOCK opener built on the watch or the snow ("Ten past one by my father's watch…") would
    use the last unused hook type. The ledger, though, puts the clock in Valens's hand a page later,
    and pulling it forward would turn the watch into a device. Est. 7, and it is against the ledger.
- **Note (outside my territory, flagged only):** sentence 3 is an and-chain ("black and gritty and
  packed hard, and cold"). It counts toward the chapter's and-chain budget. The gate decides whether
  it matters.

## Ending (Pull)
- **Last two paragraphs:**
  > He gave me the duffel. Then he gave me the shovel.
  >
  > "Men will come asking," he said. "You went up by yourself. You never had a watch."
- **Type:** OMINOUS PROMISE, voiced by a character in the present scene and not by the narrator. Valens
  predicts that men will come and then hands her the lie to tell them. The dread belongs to him, in
  that moment, and it rests on his own theory of who she is. The narrator adds nothing forward.
- **Score: 8/10** (Forward pull 2/3, Emotional charge 3/3, Unpredictability 1/2, Promise 2/2)
  - Forward pull 2: the reader knows from 1998 that nobody is chasing Mara, so the threat as Valens
    states it is hollow for the reader. The pull comes from the gap. He believes it enough to coach
    her, and "I don't want it in my head when they come" sounds like a man who has been asked before.
    Readers will turn the page to find out what he is afraid of. They will not turn it because they
    fear pursuers. That is a real pull, but not a full 3.
  - Emotional charge 3: the paragraph before the line hands back everything she brought (the duffel,
    then the widow's shovel he went back into the cave for), so the watch is the one thing not returned.
    "You never had a watch" does two jobs at once. It protects her, because he is keeping her out of
    his story and himself out of hers. It also erases her father's watch from the record, in the
    chapter where the cave has just erased her way home. Neither the narration nor the line points at
    the double meaning, and the watch is never named as a symbol (outline warning respected).
  - Unpredictability 1: the evidence speech has already set up the coaching ("they'll ask who took you
    up there"). "Men will come asking" is the third time he states that prediction ("pay men to ask",
    "when they come", then this). The surprise comes from the swerve in the last five words to the
    watch, not from the prediction itself.
  - Promise 2: the chapter keeps its implicit promises. The door is shut, and he keeps the fee, as the
    outline's beat 5 says ("He keeps the watch, because that was the deal"). It also opens a new one,
    Valens's own exposure to men who ask, without the narration gesturing at it.
- **Different kind of line from Ch.4:** Ch.4 ended on a single word of *his* that named her
  ("Nymphē."). This line is three short declaratives that write her a story: an instruction and a
  coached lie. The register is different, the job is different and the length is different, so the
  `dialogue` signature repeats but the line does not.
- **Midnight test:** pass. A man she met yesterday holds her father's watch and has told her to deny it
  exists, and he is visibly afraid of being asked about her. The reader turns the page.
- **Rewritten:** no.
- **Alternatives considered (not applied):**
  - Cut the prediction and end '"You went up by yourself," he said. "You never had a watch."' This
    removes the third statement of the threat and tightens the line. But it strips the ominous frame,
    so the pull collapses into an EMOTIONAL GUT PUNCH on the watch, which repeats Ch.2's type. It also
    loses the beat in which he pays for his involvement by coaching her. Est. 7. Not a clear
    improvement.
  - Recast as '"If they ask," he said. "You went up by yourself. You never had a watch."' This avoids
    repeating "come", but the conditional turns the promise into contingency planning, and his fear
    disappears. Est. 7.
  - End on Mara accepting the lie ('"I never had a watch," I said.'). The last paragraph would still
    be speech, but this is a DECISION POINT (Ch.5's type, consecutive), and as a callback it turns the
    line into a device. Barred.
- **No-foreshadowing check:** the narration contains no forward gesture. "Men will come asking" is a
  character's present-tense expectation, built on a theory the reader can see is wrong about Mara. None
  of the §0 families A–E apply. It is not a closing aphorism, it is not a scene-button, and none of the
  words recur elsewhere as a device. The dialogue polish already checked the "by yourself" echo and
  marked it deliberate and local.

## Chain Check
- **Previous chapter pull type:** DECISION POINT (Ch.5: the timed plan to climb, then sleep).
- **This chapter hook type:** IN MEDIAS RES.
- **Transition momentum:** strong. Ch.5 says she will be at the cave by noon. Ch.6 puts her there in
  the first sentence, and the frost shows the plan was delayed. The backfill then accounts for the
  delay honestly (the work at Kallia's, not knowing the way, the snow, Valens's refusal, the watch).
- **This chapter pull type:** OMINOUS PROMISE (character-voiced).
- **Next chapter hook (planned):** Ch.7 opens with a claim, `narrative`: a woman in Phocis belonged to
  someone. By type that is CONTRAST or VOICE (writer's choice). Neither is IN MEDIAS RES, so the
  consecutive-hook rule is satisfied.
- **This chapter's pull feeds the next hook:** yes, thematically. Valens's theory is that she belongs
  to "a big house" and that someone will come to claim her. Ch.7 opens on the claim that a woman here
  exists only as somebody's, and the chapter makes her Kallia's. His misreading becomes the next
  chapter's subject.

## Ripple Effects
- Previous chapter connection: OK.
- Next chapter connection: OK.
- **Promise delivery (the OMINOUS PROMISE rule: pay off within 2–3 chapters):** OK, by inversion. In
  Ch.9 (outline beat 4) a notice arrives looking for a scarred runaway "answering to Lupus", and she
  watches Valens read it. The men who "come asking" turn out to be asking about him, not her. That
  falls inside the window and is honest, with no narrator gesture needed now. Writers of Ch.7–8 should
  not have anyone come asking after Mara. Ch.7's clerk "does not ask", which already plays against
  this line, so keep it that way.

## Types for Ch.7 to avoid (consecutive rule)
- **Hook: do not use IN MEDIAS RES.** The outline's claim opening is fine.
- **Pull: do not use OMINOUS PROMISE.** The ledger's `question` ending should be a QUESTION PLANT
  (spoken or narrated in the present scene). It must not be a "but would it last?" rhetorical question,
  and it must not reach forward.

## Type Diversity (running tally)
| Ch | Hook | Score | Pull | Score |
|---|---|---|---|---|
| 1 | CONTRAST | 9 | QUESTION PLANT | 8 |
| 2 | VOICE | 8 | EMOTIONAL GUT PUNCH | 8 |
| 3 | SENSORY IMMERSION | 7 | CLIFFHANGER | 9 |
| 4 | IN MEDIAS RES | 8 | REVELATION | 8 |
| 5 | QUESTION | 8 | DECISION POINT | 8 |
| 6 | IN MEDIAS RES | 9 | OMINOUS PROMISE (character-voiced) | 8 |

Hooks: 5 of 6 types are used, and only TICKING CLOCK is unused. Pulls: all 6 types are now used.
There are no consecutive same-type hooks and no consecutive same-type pulls. From Ch.7 on, every pull
type repeats something earlier, so the rule that matters from here is the consecutive rule.
