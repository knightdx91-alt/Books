# Hook-Craft Report: Chapter 8 — The Thyiades (run 2)

**Result: NO EDITS.** The opening and the ending both clear the threshold of 7. Both hit their ledger
signatures as written, and neither breaks the consecutive-type rule. The chapter file is unchanged
(byte-identical to the dialogue-polish output).

Ledger row (binding): Single-scene (internal shape: *ritual*) · open = mid-dialogue → `dialogue`, with
Kallia mid-instruction about what not to say on the mountain · end = quiet image → `quiet` (8–24 words),
the anchor being women asleep in a heap in the snow with steam rising off them · 0 breaks · dialogue 25–35%.

I checked the text read-only, from /home/user/Books, with no edits made:
- `python3 tools/shape_check.py books/the-hour-of-ash`: Ch.8 computes as **open `dialogue`, end
  `quiet`** (7,899 words, 0 breaks, dialogue 26%, median sentence 15). RESULT: SHAPE CLEAN across 8
  chapters. This is the book's first `dialogue` opener. `quiet` appears for the second time (Ch.1 and
  Ch.8), not consecutively.
- `bash books/the-hour-of-ash/tools/check_chapter.sh 8`: everything clean (style incl. foreshadow 0,
  grammar 0, rhythm 0, show/tell no flags, voice-wear strict clean, tic gate clean with and-chains 3,
  echo scan 0, metaphor no flags, shape clean).
- `python3 books/the-hour-of-ash/tools/tic_report.py --echoes 8`: **0 echoes**.

Barred types for Ch.8 (consecutive rule, from the Ch.7 report): hook VOICE, pull QUESTION PLANT.
Neither is used. TICKING CLOCK is still the only hook type never used. I considered it below and did
not force it.

---

## Opening (Hook)
- **First paragraph:**
  > "And once we're above the last house you say nothing about men, not husbands and not sons,
  > whatever they've done to you this winter," Kallia said. "Up there you talk about your feet, or the
  > cold, or you hold your tongue. Wind it harder than that, or it'll be round your ankle before you're
  > halfway up the stair."
- **Type:** IN MEDIAS RES (conversational). The opening "And" puts the reader inside an instruction
  that has already begun. Nothing is set up. The reader works out the situation (a night climb, a
  women's rite, rags being wound over shoes) from the rule and the wrapping. The concrete grounding the
  type needs comes in sentence 3: the rag that will be round her ankle before the stair. It is not a
  VOICE hook. The voice is Kallia's, not the narrator's, and what hooks is the rule, not the
  personality. It is not a QUESTION hook either, because the rule is odd but not impossible.
- **Score: 8/10** (Information gap 2/3, Emotional pull 2/3, Voice 2/2, Connection 2/2)
  - Information gap 2: Ch.7 has already told the reader the women go up to dance ("Dance. Drink.
    Freeze."), so where they are going is not the gap. The gap is the prohibition, and it holds:
    Mara asks "Why nothing about men?" and gets "Because it's the mountain". The rule is not lifted
    until Philista's "Say what you like" some 350 lines later. Sostrata's skipped verse for Kallia
    ("as near as anyone in the pen came that night to keeping Kallia's rule") pays it off. The hook
    promises something and the chapter delivers it.
  - Emotional pull 2: "whatever they've done to you this winter" is dry and warm, with a grievance under
    the joke. "not sons" is a widow's exact word, set without comment. Both are present-scene speech
    with no reach forward, and they protect the Ch.10 reveal. The register is wry rather than urgent,
    which suits the chapter and keeps the score below 3.
  - Voice 2: imperatives, labor and cost, and nothing about herself. The paragraph sounds like Kallia,
    and the second paragraph (hands on the knot, eyes on the pot) sounds like this book.
  - Connection 2: Ch.7 closed on Mara privately working out the distance from the dance to the cave.
    Ch.8 opens on Kallia's rules for that night, rules that do not cover a second agenda the reader
    already knows about. There is no recap, the distance question is not answered in narration, and
    the plan is not restated. The handoff the Ch.7 report asked for is honored.
- **Setups in the opening that must survive any later pass:** the no-men rule (paid off in the pen,
  the release and the husband test); "talk about your feet" (paid off in "For a while, as Kallia had
  said it would be, the talk was all of feet"); "not sons" (Kallia's question back, "Who would I send
  in?", and Ch.10).
- **Rewritten:** no.
- **Alternatives considered (not applied):**
  - TICKING CLOCK, still in dialogue: '"We go up when the drums start, and you've till then to get that
    wound tight," Kallia said.' The clock is real (the departure at dusk) but soft, since nothing is
    lost by being late. It also drops the rule about men, which is the chapter's spine. Est. 6.
  - QUESTION: open on Mara's "Why nothing about men?" with the rule implied. That breaks the ledger
    (Kallia mid-instruction) and hands the opening to the asker rather than the one setting the rule.
    Est. 6–7.
  - Cut the opening "And". That gives a cleaner first sentence but loses the mid-stream entry, which
    is the whole mechanism. Est. 7.

## Ending (Pull)
- **Last paragraph:**
  > When I woke the snow had stopped. I raised the edge of the stranger's cloak an inch and saw the pen
  > in the first gray light: the fire a black ring in the gateway, and Nikaso's one good sandal standing
  > up in the snow outside it where it had landed. Everything else was white and still. All down the
  > length of the wall the women lay heaped together asleep, and the steam rose off them into the cold.
- **Signature:** the last sentence is 22 words, which is `quiet` (8–24) and on the anchor exactly.
- **Type:** EMOTIONAL GUT PUNCH, in the quiet register. The punch here is tenderness, not loss. It
  works through one physical fact: under a snow-whitened heap, the only motion is the heat of
  thirty-odd bodies rising off them. The chapter has earned it: the stranger's "Come here, and bring
  your feet", a hand nobody owns drawing the himation over her boots, and "she can have the loan of
  ours". The image leaves the residue the outline names ("belonging found where the door wasn't")
  without stating it. Last used in Ch.2.
- **Score: 7/10** (Forward pull 1/3, Emotional charge 3/3, Unpredictability 2/2, Promise 1/2)
  - Forward pull 1: by design, the image closes the chapter's emotional question. The pull into Ch.9
    sits upstream, where the user's brief places it, inside the scene: Kallia on the god who "doesn't
    answer them in winter" and "It costs" / "More than you've got" / "Who would I send in?" on the
    attempted descent, then Mara on the plain who "thought about money" and counts the two 1998 coins.
    That is the decision to consult, shown rather than announced. It feeds Ch.9 (money, a sponsor, a
    man to ask the question). The only live threads in the final lines are small ones: the descent in
    the morning and Nikaso's one sandal.
  - Emotional charge 3: earned and specific. No feeling is named, there is no thermostat sentence, and
    there is no reflection.
  - Unpredictability 2: Nikaso's one good sandal "standing up in the snow … where it had landed" is
    the surprise. It is the farce's last remnant, nobody fetched it, and it sits as a private joke
    between reader and narrator next to the solemn image. "Everything else was white and still" then
    makes the steam the only moving thing in the frame.
  - Promise 1: the chapter's promise is paid in full (the door shut, the heap open). The new promise
    (the Oracle and its price) is opened upstream, not in the last lines.
- **Retired-reflex and law check:** not a closing aphorism (nothing is generalized). Not a device used
  as a scene-button: no phrase or object is clicked shut, and the line does not echo the opening. Not
  symmetrical. Not a sleep ending, since it ends on waking to an image. No reach forward: the tense is
  narrative past, nothing is tagged with significance, and none of the foreshadowing families are
  present. "When I woke" is a time hinge inside the paragraph, not the opener, so it carries no
  signature risk.
- **Midnight test:** marginal on its own. The reader is warm and might close the book here. It passes
  for the chain, because the Oracle's price is the open debt, and Ch.9 opens straight into what a
  woman's freedom costs at Delphi. That is a quiet-chapter trade, and the skill's rule covers it: a
  quiet pull that fits the register beats a loud one that breaks it.
- **Rewritten:** no. Any lever that would raise forward pull has to come from outside the image, which
  would be bolted on, or from the middle of the chapter, which is outside hook-craft's territory.
- **Alternatives considered (not applied):**
  - DECISION POINT: add one line of resolve after the image ("I would need a man, then, and money.").
    That bolts a device onto the image, moves the anchor off the last line, comes close to stating
    forward, and spends Ch.9's beat. Est. 6.
  - OMINOUS PROMISE, as present-scene dread: end on the stair ("Below the plain's edge the stair lay
    under its drift."). That is off-anchor and breaks the very slow register the outline asks for. The
    women come down in the morning, so the dread would be manufactured. Est. 6.
  - Reorder so the sandal comes last ("…and outside the gateway Nikaso's one good sandal stood up in
    the snow where it had landed."). The comic object would become the button, which is the retired
    reflex, and the anchor would be lost. Est. 7, and worse in kind.
  - Cut "Everything else was white and still." That is tighter by six words, but it loses the stillness
    the steam moves against. Est. 7, not clearly better.

## Chain Check
- **Previous chapter pull type:** QUESTION PLANT (how far from the dance to the cave, on foot, at night).
- **This chapter hook type:** IN MEDIAS RES (conversational).
- **Transition momentum:** strong. The reader goes in carrying Mara's private calculation and meets
  Kallia's public rules, and the gap between the two drives the first half of the chapter until she
  slips off to the cave.
- **This chapter pull type:** EMOTIONAL GUT PUNCH (quiet).
- **Next chapter hook (planned):** Ch.9 opens on a document, a Delphic manumission inscription in
  italics (`narrative`). By type it is likely CONTRAST ("sold to Apollo", "free" on condition she
  remain with her former owner until death).
- **This chapter's pull feeds the next hook:** partially by the final image, fully by the chapter. The
  image is about belonging that is given. The inscription is about belonging that is priced and
  conditional, so the tonal hinge is strong. The plot hinge (money, a man to ask the question) is
  carried by the descent exchange, as the brief intended.

## Ripple Effects
- Previous chapter connection: OK.
- Next chapter connection: OK. For the Ch.9 writer:
  - The Ch.9 hook must not be IN MEDIAS RES, and the Ch.9 pull must not be EMOTIONAL GUT PUNCH
    (consecutive rule). The planned ≤7-word punch on Valens walking away from the notice fits
    DECISION POINT or REVELATION.
  - Do not have Mara restate the decision to consult. Ch.8 has shown it ("thought about money").
    Ch.9 can open on the inscription and let the cost-of-a-consultation beat pick it up.
  - Kallia's question back is spent (per the dialogue report). If she touches the Oracle again in
    Ch.9, give her silence or an act.
- **Flagged for the disruptor, in the middle of the chapter (not touched; outside hook-craft
  territory):**
  - **Steam before the anchor.** The final image is the chapter's fourth steam beat: the ring of
    sandals "steamed" (¶ "Then everybody took off her shoes"), Kallia's rags with "steam came off her
    knuckles", and Kallia's rags again, "The rags steamed in her hands." (¶ "Kallia was turning her
    rags to the fire"). The second and third are the same object steaming in the same hands, and the
    third closes its paragraph after Kallia withholds a husband, so it is starting to act as a button.
    Recommendation: cut or recast the third ("The rags steamed in her hands.") so the anchor's steam
    arrives fresher. The gate does not see this, since it is not a gesture class and not a repeated
    phrase.
  - **Where the forward pull sits.** The pull into Ch.9 lands around 55–60% of the way through the
    chapter, and the last ~3,000 words carry no forward thread beyond the morning descent. That is the
    ledger design (ritual shape; the snow-heap "very slow"). The evaluator's PACING check should read
    it as intended, not as sag.

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

- Consecutive same-type hooks: none. Consecutive same-type pulls: none.
- Hook types used: 5 of 6 (TICKING CLOCK unused). IN MEDIAS RES is now at 3 uses (Ch.4, 6, 8), the
  most of any type. Prefer a different hook in Ch.9–10 where the ledger allows it.
- Pull types used: 6 of 6. EMOTIONAL GUT PUNCH and QUESTION PLANT are each at 2.
- Ch.9 barred: hook IN MEDIAS RES, pull EMOTIONAL GUT PUNCH.
