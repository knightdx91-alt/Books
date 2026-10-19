# Hook-Craft Report: Chapter 9 — The Polygonal Wall (run 2)

**Result: NO EDITS.** The opening and the ending both clear the threshold of 7, both hit their ledger
signatures as written, and neither repeats Ch.8's types. The chapter file is unchanged: it is
byte-identical to the dialogue-polish output (md5 `adb271bc2dcc7a8e901b03a5f5842ae8`).

Ledger row (binding): Collage (internal shape: *stones and errands*) · open = document, a Delphic
manumission inscription → `narrative` · end = short punch → `punch`, with the final paragraph a single
sentence of ≤7 words, a plain observed action and not an aphorism · 5 breaks · dialogue 25–35% · gear mid.

I checked the text read-only, from /home/user/Books, with no edits made:
- `python3 tools/shape_check.py books/the-hour-of-ash`: Ch.9 computes as **open `narrative`, end
  `punch`** (6,114 words, 5 breaks, dialogue 27%, median sentence 15). RESULT: SHAPE CLEAN across 9
  chapters. `narrative` is now at 3 openers (Ch.2, 7, 9) and `punch` at 2 closers (Ch.3, 9). Neither
  is consecutive.
- `bash books/the-hour-of-ash/tools/check_chapter.sh 9`: everything clean. That covers style (incl.
  foreshadow 0), grammar 0, rhythm 0, show/tell, voice-wear strict, the tic gate (and-chains 3,
  credential asides 0, no gesture class over cap), echo scan 0, metaphor (no flags) and shape.
- `python3 books/the-hour-of-ash/tools/tic_report.py --echoes 9`: **0 echoes**. "drink first" and "let
  the gray" occur nowhere else in the manuscript.

Barred types for Ch.9 (consecutive rule, from the Ch.8 report): hook IN MEDIAS RES, pull EMOTIONAL GUT
PUNCH. Neither is used. TICKING CLOCK is still the only hook type never used. I considered it below and
did not force it.

---

## Opening (Hook)
- **First line:** *In the archonship of Kleodamos, in the month Poitropios, Xenon son of Euangelos, a
  Delphian, sold to Apollo the Pythian a female body.*
- **Type:** CONTRAST. The document puts two things in one legal instrument that should not share it.
  "that she be free, and not to be laid hold of by anyone all her life, doing what she wishes and
  going to whom she wishes" sits against "let Aphrodisia remain with Xenon as long as Xenon lives …
  let Xenon have power to punish her as he wishes, by beating and by selling". The first sentence
  starts the collision on its own: a sale to a god, and the thing sold is "a female body". It is not a
  QUESTION hook. Nothing in it is impossible; it is a real-style *paramone* formula, and the strangeness
  is the gap between "free" and its conditions. It is not IN MEDIAS RES (barred), because nothing is
  happening. A notary's voice is speaking.
- **Score: 9/10** (Information gap 3/3, Emotional pull 2/3, Voice 2/2, Connection 2/2)
  - Information gap 3: the first sentence raises three questions together. Why is a god buying? Why
    "a body" and not a name? Who is reading this? The paramone clause then opens the chapter's real
    question, what "free" costs here. The chapter pays every part of it: the cutter's "She'll be free
    the day they carry him out", Mara's "So that nobody can say she bought herself", and Aphrodisia
    passing under her own freedom with washing on her head. Euthydikos as a witness is paid off when
    the cutter sends Mara to him ("His name's at the foot of half this wall").
  - Emotional pull 2: the register is a contract's, and it should be. "by beating and by selling"
    lands because the document does not raise its voice. The feeling arrives in ¶2–3 (dust still in
    the V of every stroke; the mended letter "a little fatter than its neighbors"; "She can't read a
    letter of it."). It is not in the hook itself, and that caps this at 2.
  - Voice 2: documents in italics are this book's collage device (Ch.2's notebook, Ch.7's woman in
    Phocis). The witness list is authentic texture and does not trail off, because one of its names is
    load-bearing.
  - Connection 2: Ch.8 ended on belonging that is given (the heap of women in the snow, steam rising).
    Ch.9 opens on belonging that is priced and conditional. Ch.8's upstream thread ("thought about
    money", the two 1998 coins) feeds straight into a document whose subject is a price. There is no
    recap, and Ch.8's decision to consult is not restated. Mara "had climbed the Sacred Way that
    morning to find a priest" picks it up as an errand.
- **Length note:** the document runs ~170 words, well past the usual "3–5 sentences, shorter is
  better". The ledger requires the inscription, and the paramone clause is the emotional anchor, so it
  cannot be cut down to the first sentence. Trimming the witnesses would lose the Euthydikos setup. I
  left it as it is.
- **Setups in the opening that must survive any later pass:**
  - Euthydikos as a witness, paid off by the cutter's referral.
  - "three minae", the scale against which Mara's stater and goat are priced.
  - "by beating and by selling", which rhymes, unpointed, with the runaway notice's property language
    at the close. Do not point it out.
- **Rewritten:** no.
- **Alternatives considered (not applied):**
  - QUESTION: open on the paramone clause alone ("But let Aphrodisia remain with Xenon as long as Xenon
    lives…"). That is a sharper first sentence, but it drops the sale-to-a-god frame that makes "free"
    mean anything, and it breaks the inscription's formula order, which is the realism the ledger asks
    for. Est. 7.
  - TICKING CLOCK: none is available that is honest. The only clock in the chapter is "as long as Xenon
    lives", and pressing it as urgency would misread a lifetime as a deadline. A manufactured clock in a
    collage chapter would be exactly the dishonest hook the skill bans. Not drafted beyond the test.
  - Cut the witness list. That ends the document on the harsh clause and gives more punch, but it loses
    the Euthydikos setup and the authenticity of the form. Est. 8, and worse for the chapter.

## Ending (Pull)
- **Last paragraphs:**
  > He looked back at me while a cart came in at the top of the square and rolled down past us, oil jars
  > roped in straw, the carter swearing at his ox. Then he took the gray down the square at a walk, past
  > the money-changer and the men still at the eel-seller, to the trough below the fountain. I had his
  > obol in the rag with the rest. I stayed where I was.
  >
  > He let the gray drink first.
- **Signature:** the final paragraph is one sentence of 6 words, a plain observed action. That is
  `punch` and within the ledger's ≤7.
- **Type:** DECISION POINT, observed and not announced. Two choices are made in silence in the last
  five sentences. His is not to hurry: he walks past the men who have just said they would give up a
  wife's brother for three hundred, and he waters the mule before himself, in a square where the board
  describes the scar on his hand. Hers is "I stayed where I was": she does not follow, does not speak,
  and does not look at his hand ("I looked at his face"). Both choices are debatable, so the reader holds
  an opinion: is his calm nerve or a mistake, and is her stillness loyalty or distance? Last used in
  Ch.5, so there is no consecutive conflict.
- **Score: 9/10** (Forward pull 3/3, Emotional charge 2/3, Unpredictability 2/2, Promise 2/2)
  - Forward pull 3: the danger is live and specific. Three hundred drachmas go to "whoever shows where
    he is". The men who priced the betrayal are in the same square. Mara has spent the whole chapter
    learning that she cannot afford the god. "I had his obol in the rag with the rest" puts his debt to
    her and the price on him in one fist without saying either. A reader at midnight does not stop here.
  - Emotional charge 2: withheld on purpose. "I was looking at him. I looked at his face." is the only
    place the charge rises, and the second sentence earns its repetition: she keeps her eyes off the
    hand the notice describes. The final line carries tenderness by transfer, back to his two fingers of
    pitch on the gray's galled withers at the rear gate. The romance pressure stays below the surface,
    which is right for this point in Part One, so not 3.
  - Unpredictability 2: the genre beat (a confrontation, flight, a demand to know) is refused. The
    subversion lands, and "first" quietly says he means to stay and drink after her.
  - Promise 2: the chapter's promise ("the price of everything, and Valens's danger") is paid, and it
    opens a new one: the knowledge sits between them unspoken.
- **Beat-subversion check (the brief's point 2): PASS.**
  - She reads it: "I stepped in among the pillars … and read the board through. I read it through
    again. The rag had gone damp in my fist." The fear is a physical fact with no feeling named.
  - She watches him read it: "He stood with the gray's nose at his shoulder while a slow man might read
    it once, and then as long again." That gives the time without saying he can read, so his literacy
    stays unestablished, as the dialogue report requires.
  - Neither says anything: the look is held through a passing cart, he walks, and she stays.
  - Not glossed: no sentence interprets the look, names a feeling or explains the mule. The last line
    is pure action.
- **Retired-reflex and law check:**
  - Not a closing aphorism, since nothing is generalized.
  - Not a device used as a scene-button. "The gray" is an animal and a situation, not a repeated phrase
    (0 echoes book-wide), and the line does not click a callback shut.
  - Not symmetrical with the opening.
  - No reach forward: "first" is relative to his own drinking in the present scene, not to the future.
    Foreshadow 0 per the gate.
  - "I had his obol in the rag with the rest." is the one object callback near the close, from the
    rear gate's "An obol." / "He'll pay." It sits in the penultimate paragraph, unpointed, and carries
    plot weight (her debt and his price), so I left it.
- **Midnight test:** pass.
- **Rewritten:** no. The line is already the plainest version of the beat, and any change would add a
  device or a gloss.
- **Alternatives considered (not applied):**
  - OMINOUS PROMISE (present-scene dread): "The men at the money-changer's never turned round." That is
    a negation ending, it points at the danger the reader already holds, it is 7 words, and it shifts
    the last image off Valens. Est. 7.
  - REVELATION / object: "His right hand was in her mane." That points at the scar through the hand,
    the glossing the brief forbids, and makes the hand a button. Est. 7, and worse in kind.
  - CLIFFHANGER: "One of the men at the board turned." Ch.10 is Kallia's letter and would not resolve
    it, so the cliffhanger is manufactured and dishonest. Est. 6.
  - Cut "I stayed where I was." to tighten the run-in. That loses Mara's half of the silence, and the
    neither-says-anything beat becomes his alone. Est. 8, and worse.

## Chain Check
- **Previous chapter pull type:** EMOTIONAL GUT PUNCH (quiet). Women asleep in the snow, steam rising.
- **This chapter hook type:** CONTRAST (a document).
- **Transition momentum:** strong. Belonging given is set against freedom priced, and the money thread
  carries over from Ch.8's "thought about money".
- **This chapter pull type:** DECISION POINT (observed, silent, both characters).
- **Next chapter hook (planned):** Ch.10 opens on an object, the letter "folded small and stained
  from the road" (≤8 words, `short-punch`). By type it is likely SENSORY IMMERSION or QUESTION.
- **This chapter's pull feeds the next hook:** partially, by design. Ch.10 is Kallia's chapter and does
  not pick up the square. The reader carries the Valens danger across a quiet chapter, which adds
  tension rather than releasing it. That is the outline's intent ("a short, quiet punch between the
  money chapter and the Valens chapters").

## Ripple Effects
- Previous chapter connection: OK.
- Next chapter connection: OK. Notes for the Ch.10 writer and hook pass:
  - **Consecutive rule:** the Ch.10 hook must not be CONTRAST. The Ch.10 ending is a PLAIN STOP (no
    pull) per the ledger. Classify it as no-pull, or if a type must be named, not DECISION POINT.
  - **Echo risk:** Ch.9 brings the notice up "With the oil from Thebes. First carts since the snow".
    The Ch.10 outline brings the letter up "with the first carter of the year". Vary the wording, or
    the echo scan will catch "first cart(s)". The shared spring traffic is good continuity, and the
    letter and notice arriving on the same opening of the roads can stand without being pointed out.
  - Do not let Ch.10 mention the notice or Valens in narration as dread or a reminder. The quiet
    chapter only holds the tension if it is not restated.
- **Flagged for the continuity guardian (not touched; outside hook-craft territory):**
  - Valens's literacy stays unestablished ("while a slow man might read it once"). Keep it that way
    until the outline decides.
  - The notice's "scar on the back of the right hand" is new physical canon for ENTITY_STATE if it is
    not already logged. Check it against any earlier description of his hands.

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
| 8 | IN MEDIAS RES (conversational) | 8 | EMOTIONAL GUT PUNCH (quiet) | 7 |
| 9 | CONTRAST (document) | 9 | DECISION POINT (observed, silent) | 9 |

- Consecutive same-type hooks: none. Consecutive same-type pulls: none.
- Hook types used: 5 of 6 (TICKING CLOCK unused). IN MEDIAS RES 3, CONTRAST 2, VOICE 2, SENSORY 1,
  QUESTION 1. SENSORY and QUESTION are the underused types, which suits Ch.10's object opener.
- Pull types used: 6 of 6. DECISION POINT, EMOTIONAL GUT PUNCH and QUESTION PLANT are at 2 each;
  CLIFFHANGER, REVELATION and OMINOUS PROMISE are at 1.
- Ch.10 barred: hook CONTRAST, pull DECISION POINT (moot, since Ch.10 is a PLAIN STOP).
