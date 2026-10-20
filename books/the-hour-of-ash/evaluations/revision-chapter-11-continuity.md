# Revision Log: Chapter 11, continuity repair (audit run 2)

**Date:** 2026-10-20
**Source:** `evaluations/continuity/chapter-11-audit.md` (1 CRITICAL, 14 WARN)
**Applied:** C-01 (with the headroom option), W-01, W-02, W-04, W-05, W-06, W-07, W-08a, W-08b, W-09, W-10, W-11, W-12, W-13 (×4).
**Skipped, per orchestrator:** W-03 (the money gap goes into the Ch.12 brief) and W-14 (the bible re-sync is done separately).
**Orchestrator ruling on W-06 and W-07:** the bible rule wins. The narrator does not paraphrase the notice, and there is no extra road-watching beat. The close stays the practical line.

I checked every cited prior text on disk before editing:
- ch-07 l.88 "a soft heavy body"; ch-09 l.386 "since the snow"; ch-06 l.266 "with great care"; ch-05 l.429 "by full light"; ch-04 l.11, the knife-cut hair.
- ch-08 l.338, the pickpocket simile; ch-09 l.360, "I keep them warm"; ch-09 l.310, "fingers stayed clear of my palm".
- ch-09 l.352, the notice ("whoever takes him should take him with others"); ch-10 l.188, the obol on the bottom stair; ch-10 l.134, "Which is his name?".
- sample-08 l.6, the tallow tag.
- character-bible l.2309, "The notice's text: do not re-quote"; l.2577, "No pre-announcing Ch.12".

All of them stand as the audit quotes them.

## Changes (before → after)

### C-01: Valens's bare "No." (11 → 3)
| # | Before | After |
|---|---|---|
| p25 (headroom) | "I need somebody … to the god." / **"No."** | / **He kept the stone going.** |
| p40 | "Then sell me back the watch," I said. / **"No."** | / **"With the god's money?"** |
| p119 | …for a pad off the trestle. / **"No."** | / **"The yard's yours till I'm back."** |
| p121 | "Have you ever seen a man killed with one blow?" / "No." | KEPT |
| p128–129 | …Or the rope on her hind leg?" / **"No."** / **Felix stopped short.** | / **Valens kept his eyes on the hoof, and Felix stopped short.** |
| p186–190 | "You have been in yourself, surely." / "No." / "Not even a question, sent in by somebody else?" / "No." / "Why not?" | **"You have been in yourself, surely. Or sent a question in by somebody else."** / **He answered neither. "Why not?" I said.** |
| p240 | "There is no paper." / "No." | KEPT |
| p260 | "Will you wake him?" / **"No."** | / **"He'll wake when he's cold."** |
| p225 (Mara) | …Has he told you about the Cilician?" / **"No."** / "He bought me off him… | p224 and p226 merged: **…Has he told you about the Cilician? He bought me off him…** |

Bare "No." lines remaining: **3**: Valens p121 (the men he killed), Valens p240 (no paper), and Mara to Kallia ("Is he paying you?"). The gate's cap is 4.

### WARN
- **W-01:** "Three times he was up to change it, and I never heard a thing." → "**There's three sacks gone, and I never heard him once.**"
- **W-02:** "He'd want more than you have if you had twice as much. … and none of his have ever been near a fire." → "**He prices for pilgrims.** … and **he lets you pick your own out of the pen.**"
- **W-04:** "a crack I heard from the bench." → "a crack I heard **from the packsaddle**."
- **W-05:** "The knot came loose in his fingers." → "**The knot slackened under his thumbs**". This sentence now also takes in the next one (see the gear note).
- **W-06:** the paragraph "The board in the square had advised whoever went to fetch him to bring friends." → deleted.
- **W-07:** "He went to the gate to look at the road, as he did every night before he put the bar across. The dog got up off its side of the gutter and went with him." → "**He went to bar the gate, and the dog got up off its side of the gutter and went with him.**"
- **W-08a:** "I untied the knot first and put the obol on the stone of the trough beside him." → "…and **held out the obol**." Also "He picked it off the stone and tucked it into his cheek" → "**He took it and tucked it** into his cheek".
- **W-08b:** "Which bit's me? Where does it start? That one, with its arms on its hips, that's the F." → "**Is that one me, with its arms on its hips?**"
- **W-09:** "and he had cut his own hair, with a knife, without a mirror." → "and **his hair stood up every way at once, with straw in it**."
- **W-10:** "the Syracusan was tighter than a priest's purse," → "the Syracusan **had haggled him down to nothing**,"
- **W-11:** '"Cooked," I said, to the octopus, but…' → '"Cooked," I said, but…' (the quail stays as the chapter's one non-listener tag).
- **W-12:** "found the knot in the end of a lead rope to work at, which I had watched him tie that morning." → "found **a knot** in the end of a lead rope to work at."
- **W-13 (a):** "a soft, heavy, early-rising man" → "a **well-fed, slow-spoken**, early-rising man"
- **W-13 (b):** "Since the snow he had kept it going" → "**Since the mountain** he had kept it going"
- **W-13 (c):** "He put the sherd face up on the bench with great care, his name to the light." → "He **laid the sherd** face up on the bench, his name to the light."
- **W-13 (d):** "on the Kirrha road by full light, going down…" → "on the Kirrha road **before the sun was on it**, going down…"

### Gear hold (two punctuation joins, not in the audit)
The fixes cut a 14-word sentence (W-06) and shortened two others (W-08a, W-13c). That dropped shape_check's median sentence from 14 to 13, below voice-dna's mid band (14–16). Two adjacent pairs of short narration sentences were joined, adding one word in total:
- "The knot slackened under his thumbs. He was a while silent…" → "The knot slackened under his thumbs**;** he was a while silent, and I let the question stand."
- "Valens was in the shed on my return. The sherd was as I had left it." → "Valens was in the shed on my return, **and the sherd** was as I had left it."

After the joins the median is back to 14 on both meters.

### Header
The word-count comment was updated: 6,038, 3 bare "No.", and the revision line.

## Freshness
I grepped all 28 new strings against Ch.1–10 and voice-bank samples 01–13. Each has 0 prior uses and appears once in Ch.11. That includes "on my return, and" and "found a knot" from the joins and W-12.

## Held fixed
- First sentence and final spoken line: unchanged.
- Breaks: 3.
- Dialogue: 37% by shape, 36.9% by meter.
- Median: 14 by both shape and metaphor.
- Bend, kneel and crouch: 0. The one "bend" in the chapter is the road's, in Felix's speech.
- Memories: none added.
- Ledger signature: `long-spiral` → `dialogue`.

## Gate results
- `bash books/the-hour-of-ash/tools/check_chapter.sh 11`: **all clean.**
  - Style: 6,055 words, simile 1.3/1k, em-dash 2.
  - Grammar: 0 errors.
  - Rhythm: 0 flagged.
  - Show/tell: 36.9%.
  - Voice-wear strict: clean.
  - **Tic gate: clean.** The earlier failure, `"no" 11x`, is gone.
  - Echo: 0. Metaphor: fig 1.7/1k, median 14.
  - Shape: CLEAN.
- `python3 books/the-hour-of-ash/tools/tic_report.py --echoes 11`: **0 echoes, no command-echo candidates.**

## For the bible sync (W-14)
- The Valens Ch.11 block should drop "'No.' twice to the boxing", "(never been in)", "(never sent a question)" and "(he will not wake the boy)". It should take in the new lines above.
- Carry the audit's new cap forward: Valens's bare "No." is at most 1 per chapter from Ch.12 on.
