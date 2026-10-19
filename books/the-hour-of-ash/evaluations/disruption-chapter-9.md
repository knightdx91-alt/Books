# Disruption Report: Chapter 9 — The Polygonal Wall (run 2)

Backup of the pre-pass text: `manuscript/reports/chapter-9-pre-disruption.md` (md5 `adb271bc…`, the
dialogue-polish / hook-craft output). It is in `reports/` because the gates glob `chapter-*.md` in `chapters/`.

**Verdict on the input:** strong. The chaos was already in place: the Fortieth Street hardware store, the
crayon smell inside a sentence, and the wager. The ugly sentence was already there ("It was too fat, and I
filed it, and it was still too fat."), and the peak was a wrong reaction rather than a laugh. So this was a
light pass. Every cut is subtractive except three. The work went into the three flagged items and the stage
business the gesture regex cannot see. No chaos was added.

**Held fixed:**
- **First document:** byte-identical (diffed).
- **Final line:** "He let the gray drink first." is unchanged.
- **Breaks:** 5.
- **Dialogue:** 26.8% → **27.8%** by shape_check (show/tell measure 27.0%). Band 25–35.
- **Median sentence:** **15** (shape_check and metaphor_check).
- **Open / end:** `narrative` → `punch`.
- **Word count:** 6,114 → **5,892** by shape_check (`wc -w` 6,282 → 6,065). That is inside the 5,800–7,000
  range and was not padded.
- **Romance signals:** none. One was removed (see 1).
- **Foreshadowing:** 0.
- **Spent narrator moves:** none added. That covers hinge-family openers (0), "before I had decided" (0),
  command-echo (0), callback pointers (0) and a lying-awake coda (0). "The one / the only" stays at 1.
- **Em-dashes:** 0 → 1, a true interruption in dialogue (op 8).
- **Semicolons:** none added.

## Flagged items, resolved

### 1. Valens and the gall: judged a romance cue, recast as plain work
"He did it with two fingers, slowly, and she stood for it." The verdict is that it reads as a cue. The camera
lingers on his fingers with an adverb of tenderness, and the mule's patience is offered as the payoff. The
hook report confirms the reading: it scored the final line's charge as "tenderness by transfer, back to his two
fingers of pitch". That is the narration doing romance work at a point where the bible wants none.

The recast:

> "…where the saddle had galled her. Her ears were flat. When she swung her head round to bite him he put her
> nose away with his elbow and went on working."

- This is his card: attention to the moods of animals, and competence that is unsentimental.
- The mule's resentment is comic noise.
- The final line now reads as a man who looks after his animal, not as a caress remembered.
- "He kept his eyes on the sore." is cut too. It duplicated the "kept [her] eyes on" beat at the lions.

### 2. The mending stretch: catalogue risk broken
The stretch ran fill → carry into the light → report what shows → dig out, three times over, with procedure
clauses inside each fill. That form is the "condition report" the outline forbids. The ladder now has uneven
rungs:
- **Deleted the first dig-out paragraph** ("I dug it out with the point of the knife, every crumb, and cleaned
  the line with a splinter.") as op 7. "On the second try" implies it. Of the three dig-outs, one is now
  implied, one is the bee-man's "Out it comes", and one is the thumb.
- **Second fill:** cut the soot-smear sentence, which was a second finding in the report. The thumbprint alone
  motivates the resin.
- **Third fill:** cut "Across that grained skin the smooth band caught the light and made a ring." It explained
  what "the line was there … my fill was smooth" had already shown. Also cut "I rocked back on my heels and
  stayed so. Then", so she goes straight from seeing the line to "I dug it out a third time, too fast". The
  impulse is now on the page, not narrated.
- **Procedure clauses trimmed:**
  - "With the blade I took off what stood proud"
  - "keeping the flame to the sherd and well clear of the bronze"
  - "took the squeeze-out off with the blade before it set"
  - "so that the soot stayed only in the holes"
  - "and blew the grit off the break" (the cutter's blowing gesture, repeated)
  - the second "a pinch at a go"
  - "and it was a hair too thick", which pre-told the filing's discovery and doubled with "fine as a hair"
  - "for most of the day", which doubled "most of an afternoon" one paragraph later
- What remains is hands at work: rake, sweep, file, seat, press, polish, prick, rub.

### 3. The collage documents: each checked
- **The manumission (REVEAL):** the paramone clause, the price scale of three minae, and Euthydikos as witness.
  Untouched.
- **The curse tablet (TEXTURE):** it means nothing, and nothing new was made to mean. One voice fix: "lead that
  has lain in wet ground will tear" was a gnomic present in narration (voice-dna §0.4, no narrating present).
  It is now "lead that had lain in wet ground tore like old cloth".
- **The runaway notice (REVEAL):** Lupus, Celer, the scar on the right hand, the two rewards. Untouched.

## Operations Applied

| # | Operation | Location | Before → After (brief) |
|---|-----------|----------|----------------------|
| 1 | Simile/explanation surgery | the court; 3rd and 4th fills | Cut "That was why it had snapped there." (the gas cavities already show it); "the smooth band … made a ring"; "so that the soot stayed only in the holes". |
| 3 | Emotional control break | Kallia's basin | Added "I kept at them with a corner of the clay after the water had stopped going any blacker." She is still scrubbing when she recites the god's price. It goes unexplained and is not reflected on, and it uses the hands channel (her voice-failure channel is retired for Ch.7–9). Kallia's sand going quiet now has something to watch. |
| 6 | Negation break / logic fix | the resin | "The priest's household burned only oil, so there was no pine in the place to get any from." was a paragraph ending on a negation, and it contradicted the woodshed being filled two lines later. It is now "it wanted resin. The priest's lamps burned oil, and his kitchen burned oak." That is a direct assertion, and the split oak links quietly to the wood Valens sells. |
| 7 | Missing paragraph | first dig-out | Deleted (see 2). |
| 8 | Dialogue mess | the letter-cutter | The tidiest exchange in the chapter was a feeder-question ping-pong. Now the cutter cuts Mara off: "And if he sells her before then? To some man in Amphissa who has never—" / "She brings him up here…". He knows the answer before she has finished asking. |
| — | Gesture / stage-business tic sweep | throughout | See below. |

## Gesture / stage-business sweep (NO TICS, gestures included)
The `tic_report` regex classes are 0 for Ch.9 before and after. A hand count found these classes the regex
does not see:
- **The letter-cutter's tool business: 6 → 3 in ~600 words.**
  - Cut: "He aimed the chisel down the wall.", "He set the chisel's edge to the next letter.", "He tried the new
    stroke with his thumb."
  - Kept: the dust blown past her face, the flake that "ticked away down the steps", and the mallet tilted at
    the Way for "That's her."
- **Turning to face: 4 → 3.** The priest's "He was at the house door before he turned." is now "…and then,
  from the house door, 'In Syracuse…'". Kept: the slave's swing, the smith on his knees, and Valens's head at
  the board.
- **The priest's sleeves: 3 → 2.** Cut "The priest drew his hands deeper into the sleeves." The chilblain
  reveal (out, inspected, back) stays whole.
- **The pitch pot on its hook: 3 in ~30 lines → 2.** Cut "He had the pot back on its hook." This also clears
  the gate's "no prop handled 3+ times in 400 words" spirit.
- **Wiping: 4 → 2.**
  - Cut "I wiped the knife on my hem" and "wiped the surface clean".
  - Left: Valens on the mane and the priest on the linen. The unpointed rhyme now has no other wipes
    diluting it.
- **"Kept [her/his] eyes on": 2 → 0.** Valens's is cut (see 1). The woman at the lions now just speaks, and
  "None of them would look at it" carries the avoidance.
- **Kallia's looks: 2 → 1.** "She looked at the coins on the stone and at the hand they had come from" is now
  "To that she gave no word at all." Her one look stays: hand before face.
- **Folding: 3 → 2.** Cut "The bee-man folded the linen in four and put it in his belt."
- **Pause beat:** cut "and stayed so" (see 2).
- **No gesture was added that is already in the chapter.** The elbow and the scrubbing are new to it.

## Operations NOT Applied (and why)
- **2 Irrelevant thought:** the Writer already has two (the hardware store and the crayon smell), plus the
  wager. A third would make her scattered.
- **4 Precision deflation:** the numbers here serve the story (three minae, a stater, three drachmas, five
  hundred and three hundred, "nine years back", "forty, and eats for two"). The chapter's subject is price,
  and "five or six" and "a dozen" are already vague. Nothing was flexing.
- **5 Ugly sentence:** one already exists ("It was too fat, and I filed it, and it was still too fat."). It is
  better placed now that the "hair too thick" pre-telling is gone.

## Strongest Disruption
**The gall recast.** One sentence carried the chapter's only romance cue. It also made the closing line lean
on it. Now the gray tries to bite him and he elbows her nose away and carries on. That is truer to both of
them, and it lets "He let the gray drink first" stand as character rather than sentiment. A close second is
the mending ladder: with one rung implied and the impulse dig-out given no pause, the all-or-nothing reads as
compulsion rather than procedure.

## Risk Assessment
- **The hook report's pull score** credited 1 of its 2 emotional-charge points to "tenderness by transfer"
  from the two fingers. That transfer is gone on purpose. If the evaluator reads the close as cooler, the
  charge still lives in "I had his obol in the rag with the rest" and the held look. Do not restore the
  caress.
- **The scrubbing line** is the one addition. It is small and in the hands channel, not the voice. It sits a
  beat after the payment peak, so it extends the peak rather than competing with it. If it reads as a second
  peak, cut it. The chapter worked without it.
- **Word count** is 5,892, 92 words above the range floor. Every cut was surplus, but no further trims should
  come out of this chapter without a matching addition of real content.
- **The em-dash** is the chapter's first. It is a true interruption, inside the ≤4 absolute budget and the 0–2
  aim.

## Bible quotes these edits invalidate (character-bible.md NOT edited)
- **VALENS, Ch.9 block:**
  - "with two fingers, slowly, and she stood for it" (hands only inside a task) is now "Her ears were flat.
    When she swung her head round to bite him he put her nose away with his elbow and went on working."
  - "He had the pot back on its hook." is gone. "How long will it hold?" now has a plain tag ("he said").
  - The "For her back." … "The new saddle's rubbed her." pair is now one speech, with no beat between.
  - "Warm it first. It'll crack cold." is already cut, per dialogue-polish.
- **MARA, Ch.9 block:**
  - "a thumbprint 'the whorls raised in the fill' and a soot smear": the smear is gone.
  - "a smooth band on a bronze 'skin like an orange's'": "skin like an orange's" stays, but the band sentence
    is gone. The page now has "and my fill was smooth."
  - "seats the halves on it" is still true.
  - New: "I kept at them with a corner of the clay after the water had stopped going any blacker." (Kallia's
    basin).
  - Her line at the wall is now "And if he sells her before then? To some man in Amphissa who has never—"
    (interrupted).
- **At-risk after Ch.9:**
  - "Spent craft wording": "stood proud" and "squeeze-out" are no longer on the page. "a pinch at a go" is now
    once. "dressed down level" and "gas … caught in the metal" remain. The entries can stay as spent.
  - The redo-the-seam summary ("three fills dug out: the gold thread…, the thumbprint whorls, the smooth band…")
    should read: the first dig-out implied, the thumbprint, and the line seen along the sun.
  - "Counts on the final draft": em-dashes are now **1** (was 0). "The one / the only", "as if / as though"
    and and-chains are unchanged.
  - "The wiped hand: SPENT … Valens wiping his fingers on the gray's mane …": still on the page and still
    correct.
- **Ch.9 walk-on note:**
  - The woman at the lions: "she keeps her eyes on her own jar" is cut.
  - The letter-cutter: his "She brings the man up here" is now "She brings him up here".
  - The bee-man's folded linen is gone. It was not quoted.
- **EUTHYDIKOS:** "For a Syracusan?" … "First the pelanos…" are now one unbroken speech, and both strings
  are still verbatim. His exit no longer turns ("and then, from the house door"). There are no other quote
  changes.
- **KALLIA, Ch.9 block:** "gave no word at all" is still on the page ("To that she gave no word at all."). The
  look at "the coins on the stone and at the hand they had come from" is gone.

## Gates after the pass (from /home/user/Books)
`bash books/the-hour-of-ash/tools/check_chapter.sh 9`:

| Gate | Result |
|---|---|
| style | clean (simile 1.9/1k, em-dash 1, foreshadow 0) |
| grammar | 0 errors, 0 reports |
| rhythm | 0 flagged |
| show/tell | no flags (dlg 27.0%) |
| voice-wear (strict) | clean |
| tic gate | clean (and-chains 3, credential asides 0, negation pivots 0, 'So' openers 0, no Ch.9 gesture class) |
| echo scan | 0 |
| metaphor | no flags (median 15, 6.9% over 40 words) |
| shape | CLEAN, also with `--strict` (5,892 words, 5 breaks, dlg 28%, median 15, `narrative` → `punch`) |

`python3 books/the-hour-of-ash/tools/tic_report.py --echoes 9`: **0 echoes.**

One interim note came from my own edit and was fixed. The first form of the interruption ("before then, to
some man…") gave the grammar splitter no sentence boundary, so it reported a false 86-word sentence.
Restoring the question mark ("before then? To some man…") cleared it.
