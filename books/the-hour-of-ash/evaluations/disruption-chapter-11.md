# Disruption Report: Chapter 11 — Valens's Yard (run 2)

**Verdict on the input: a strong two-hander with a predictable spine.** The scenes are alive and varied
in how they are discovered: an argument for the figs, watching hands for the mule, an inference from a
sherd for the reading, and Felix blurting his own story. Three things flattened it:
- **A day-counter** stamped the week at even intervals (third day / fifth day / fifth evening / sixth
  morning / seventh morning / seventh day). The four reveals therefore read as a checklist.
- **Five narrator glosses** told the reader what a scene had just shown.
- **A week of repeated stage business**: tack hung on pegs, Valens walking off to the trough or stable,
  and Felix vanishing before he could be answered.

This was a light pass: **4 operations plus the mandatory gesture scan.** All narration; no speech cut.

Backup of the hook-craft version (md5 `bd856b12…`, matching hook-craft's report):
`manuscript/reports/chapter-11-pre-disruption.md`. Backups stay out of `chapters/` because the gates glob
`chapter-*.md`.

**Held (verified by diff):**
- The first paragraph is byte-identical, including hook-craft's inserted clause.
- The last two paragraphs are byte-identical, including the practical closing line.
- The anchor paragraph (Felix asleep against the black) is byte-identical.
- 3 breaks; `long-spiral` → `dialogue`; gear mid.
- Speech words are **2,253 before and after**. One beat removed between two quotes by the same speaker
  merges them into one quote, with no word lost.
- No foreshadowing added (gate 0). No memory or irrelevant thought added. No bend, kneel or crouch
  added (book-wide counts unchanged at 15 / 12).

| Measure | Before | After |
|---|---|---|
| Words (shape_check) | 6,318 | **6,083** (range 5,600–6,800) |
| Dialogue share | 35.6% | **37.0%** (band 35–45) |
| Median sentence | 14 | **14** (gear mid) |
| Breaks | 3 | 3 |
| Simile /1k | 1.3 | 1.3 |
| Em-dashes | 2 | 2 |
| And-chains | 3 | 3 |
| Echoes | 0 | **0** |

## Pre-pass: NO-TICS gesture scan (mandatory)

Counted by hand; the gate's regex classes see few of these.

| Class | Before | After | What changed |
|---|---|---|---|
| Tack/props hung up on pegs (hang-up acts) | 6 | 3 | Cut "At dusk I hung the breeching back on its peg." (folded into "Valens came in for the breeching at dusk, before…"). "The girth went back on its peg, and after it a headstall" → "After the girth came a headstall". "hanging the black's halter on its peg" cut: "Valens was in the shed on my return." stands bare. "had come in to hang up the black's halter for the night" → "had come in with the black's halter". Kept: he hangs the tested breeching himself (acceptance), the rope "with the knot still in it" (the unanswered question) and the lamp after the wick (the near-kiss block). |
| Valens resumes work after a line ("returned to…") | 3 | 1 | "and returned to the knife" cut (his work on the knife now runs whetstone → other face → forearm test → sheathed, a real progression rather than a fidget between lines). "returned to the trough" → "took the bran to the black" (real work: the poultice). Kept: "Valens returned to the black's foot." |
| Whetstone beats inside the refusal | 4 | 3 | "The stone went round." cut; the speech runs on. |
| Valens walks off across the yard | 7 | 6, two re-staged | "He crossed to the stable" ×2 → the second is now "and he took the last of the rain on his back to the stable", which belongs to this scene (rain day), keeps the rush of the rising and is no longer a duplicate of the first. The trough exit is now 1. |
| Felix gone before anyone answers | 5 | 3 | "and was gone before he had the answer" cut from the week summary (the octopus exchange shows it two lines later). "and was round the end of the stable before anybody could answer him" → "Felix said." (Valens answers past him by pointing at the fig tree, which shows the boy's speed some other way). Kept: the shovel exit, "and was gone" after "He doesn't keep things for people," and "already on the roof". |
| Mara stitches as a reaction beat | 3 | 2 | "I put my next stitch in the headstall and stayed on it until I heard the gate." cut. Kept: the awl through the girth at the fig subtext, and "I put no stitch in it" at the hoof (the inversion). |
| Valens "considers" between lines | 1 | 0 | "He considered that, with the next bell in his fingers." cut; "They could meet at dawn." now answers at once. |
| Looks in the closing 500 words | 3 | 2 | "and he went on looking at the boy" cut; "I waited for him to tell me why." stands bare. Kept: "Valens stood and looked at the two of them." and the hook-craft-relied gate/road look. |

Gate: gesture layer clean; book-wide classes unchanged (bend 15, kneel 12, object handling 9).

## Operations Applied

| # | Operation | Location | Before → After (brief) |
|---|-----------|----------|----------------------|
| 4 | **Precision Deflation**: the day-counter (the checklist fix) | figs, boxing, lame black, Praxias, barred gate, sherd | See note 1 below the table. |
| 1 | **Simile Surgery** (the chapter's one analytical simile) | the near-kiss, the relief | See note 2 below the table. |
| 7 | **Missing Paragraph** | the reading reveal | See note 3 below the table. |
| 1b | **Explanation cuts** (the self-explaining extension, applied to narrator glosses) | figs; Praxias at the gate; sherd; breastband; near-kiss | See note 4 below the table. |

**Notes to the table:**

1. **Precision Deflation (the day-counter).**
   - Six ordinal stamps changed:
     - "On the third day" → "One day".
     - "On the morning of the fifth day Valens was taking…" → "Valens was taking the string to Kirrha
       without Felix one morning" (the time moved to the end of the sentence).
     - "on the fifth evening" → "that evening". This ties the lame black causally to the Kirrha run Felix
       was refused.
     - "on the sixth morning" cut. Praxias arrives while the black's foot is still in bran, and that is
       placement enough.
     - "On the seventh morning" → "In the morning" (after the walk up).
     - "on the seventh day I left it on the bench" → "that noon I left it on the bench".
   - Kept: "For a week…", "the next morning" (the ugly-sentence paragraph) and "On the last evening of
     the week" (the frame).
   - The reveals now come when the work brings them, not on a calendar tick.
2. **Simile Surgery (the near-kiss relief).**
   - Before: "Everything in me that had been held up went down at once, the way a body went down at the
     end of a long walk once the shoes were off, and I was hungry."
   - After: "Everything in me that had been held up came down, and I was hungry."
   - The simile interpreted the feeling, which voice-dna §1 bans as analytical. Now relief is legs plus
     appetite, raw and unexplained.
3. **Missing Paragraph (the reading reveal).**
   - Cut the one-line paragraph "In the yard and on the mountain both, I had kept doors out of all I told
     him." It explained why "Take out the door" lands.
   - Now: "Take out the door," he said. / "What?". The reader catches it with Mara, and "You read it."
     names it four lines later.
4. **Explanation cuts (narrator glosses).**
   - (a) "His voice did not change for it at all." cut after "They don't, in Syracuse." His next speech
     going straight on about dust and flies shows that his voice didn't change.
   - (b) "…and he had not looked round once while Praxias was in the gate" cut. Mara's line "You had your
     back to him the whole time he was in the gate." now delivers the mind-reading discovery in dialogue,
     not in narration first.
   - (c) "Whatever I put to the god had to be said under the god's roof by somebody else, in front of a
     priest who wrote things down, and I wanted it in Greek that nobody could mistake." cut. It was a
     recap of the refusal scene, and Valens's "they'll write that down too" now does the work.
   - (d) The breastband gloss "a band of ox leather that went across a mule's chest to keep the load from
     sliding back on a climb" cut. It rebuilt the breeching gloss's skeleton ("the strap that went round
     under a mule's tail to keep the load from running forward on a descent"), a set piece repeated
     inside the chapter. It is now "Its felt lining had matted…".
   - (e) Near-kiss: "and the rest of the shed was gone" cut. It was romance-coded tunnel vision (the
     world-falls-away cliché). The face is now only the nick and the break, which are the facts.

**The checklist question (brief focus).** The order stays figs → lame mule → reading → Felix, as the
outline requires. What changed is the meter:
- **No ordinal ticks.** The day numbers are gone.
- **Uneven spacing.** The figs and the bells are a day apart. The boxing and the lame black are now the
  same day. Praxias and the barred gate are back to back. The reading reveal lands at "that noon" inside a
  paragraph that began as a week-long summary.
- **The discovery modes now differ more sharply.** Figs are argued. The mule is watched (Mara puts no
  stitch in). The reading is caught by Mara and reader at once, with no gloss. The mind-reading is
  exposed by Mara's own line. Felix is boasted by Felix and then cross-examined by Mara over the
  breastband.

## Operations NOT Applied (and why)

- **2. Irrelevant Thought:** SKIPPED by rule.
  - Ch.10 carries one (Homs on the map) and Ch.9 two (the crayon smell, the hardware clause).
  - The at-risk block sets Ch.11 at none, and AUTHOR-CP2-2 rules out stand-alone memories.
  - The chapter already has its present-tense intrusion ("a kitchen in Philadelphia with a tap in it").
- **3. Emotional Control Break:** the near-kiss collapse is the chapter's body-rebel (legs). The bible
  rests hands and voice until Ch.20, so a second break would spend a closed channel.
- **5. Ugly Sentence:** it already exists ("It rained a bit the next morning and then it stopped.") and
  is untouched.
- **6. Negation Pattern Break:** there are no define-by-negation openers. The negatives are plain refusals
  in speech ("No.").
- **8. Dialogue Mess:** skipped.
  - Dialogue-polish has just recast all 11 conversations, adding deflections, a non-sequitur and two
    cut-offs.
  - The walk-up Q&A, the cleanest exchange, already has Valens answering a different question ("Where
    would you stand…" → the crowd).
  - Messing it further would mean cutting or adding speech at the floor, or putting a moving thing into a
    held silence (SPENT).
- **Valens's "No." count (9):** noted, not touched. Every one is speech, and cutting speech was barred.
  The evaluator may want to weigh it.

## Strongest Disruption
**The relief simile cut, together with "the rest of the shed was gone".** The outline's surprise is
that both are relieved and neither explains. The draft had Mara's narration explaining twice: first the
romance-novel tunnel, then a walk-and-shoes simile telling us what the relief felt like. Without either,
the scene is plain facts:
- a lamp, a nick, a broken nose;
- a finger's width;
- a step back into girths;
- knees;
- hunger;
- a man stretching until his back cracks.

That is the most unexplained the moment can be and still read as relief.

A close second is the day-counter deflation. It makes the week feel like a week and not a syllabus.

## Risk Assessment
- **Timeline legibility.** Without the ordinals, the week is carried by "For a week", "One day", "the next
  morning", "one morning", "that evening", "By morning", "That evening", "In the morning", "that noon" and
  "the last evening of the week".
  - The sequence is still linear and unambiguous.
  - The entity tracker should log the span as "about a week" (the Writer's report counted days 1–7 plus
    the last evening; no fact changed).
- **"Valens was in the shed on my return."** It now has no business attached. Why he is there is left to
  the sherd on the bench, which is the point.
- **The bells exit** keeps an and-rush ("…he was on his feet, and the bells were in my lap, the lot of
  them, and he took the last of the rain on his back to the stable"). It is a designed hurry, and the
  and-chain count is still 3 of 9.
- **Valens's "He doesn't have to. On the god's first day…"** is now one unbroken speech of four sentences.
  That is within his card (evidence in order), but it is his longest run before the figs.

## Gates (run from /home/user/Books)
- `bash books/the-hour-of-ash/tools/check_chapter.sh 11` is **all clean**:
  - style: simile 1.3/1k, em-dash 2, foreshadow 0;
  - grammar: 0 errors;
  - rhythm: 0 flagged;
  - show/tell: no flags;
  - voice-wear: strict, clean;
  - tic gate: clean;
  - echo scan: 0;
  - metaphor: no flags;
  - shape: clean, with `--strict` exiting 0.
- `python3 books/the-hour-of-ash/tools/tic_report.py --echoes 11` gives **0 echoes**, with no
  command-echo candidates.
- My first wordings tripped gates, and I varied all of them before finishing:
  - **Voice-wear self-repeats:** "at once and I" and "them and he was".
  - **Echo:** "over his shoulder", already used in Ch.4.
  - **Book-wide recurrence:** "all the way", which reached 3 uses.
  - **as-as count:** "as far as".
- Post-pass md5: `462637ff809c98dd4cf36f4713608804`. The chapter's header comment is updated.

## Bible quotes my edits invalidate (character-bible.md NOT edited; for the next sync)
- **MARA, Ch.11 block** (the "Relief at the refused kiss" sentence): "Everything in me that had been
  held up went down at once, the way a body went down at the end of a long walk once the shoes were off,
  and I was hungry." → now **"Everything in me that had been held up came down, and I was hungry."** The
  rest of that quote ("I sat down. … my knees put me onto it …" / "I wanted bread, and whatever Kallia had
  in the pot, and I wanted it now.") is unchanged.
- **At-risk after Ch.11, "The near-kiss as staged: SPENT":** still accurate. If the sync lists the
  staging verbatim, "the rest of the shed was gone" is no longer on the page. "Relief as appetite" is
  still SPENT.
- **Stale from earlier passes, not mine (flagged so the sync catches them):** the MARA and VALENS Ch.11
  blocks still quote dialogue-polish's cut lines ("At the end of summer I shall not be here", "Felix says
  you cannot read.", "Come then.", "It saves arguing.", "In the day.", "Those want doing."). The FELIX
  card still quotes the pre-polish question bursts. The dialogue-polish report lists them all.
- No Valens, Felix, Praxias, Kallia or walk-on quote is affected by this pass. Checked by script
  against a line-joined copy of the bible: "His voice did not change", "rest of the shed", "on the
  mountain both", "halter on its peg", "the stone went round", "considered that", the ordinal day
  stamps and "keep the load from" all appear 0 times.
