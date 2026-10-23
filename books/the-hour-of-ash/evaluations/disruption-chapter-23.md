# Disruption Report: Chapter 23 — An Inn on the Appian Way

Pass: book-disruptor, 2026-10-23. Edited in place; not committed. The Writer's version is backed up at
`manuscript/reports/chapter-23-pre-disruption.md`. It goes there and not in `chapters/`, because the gates glob `chapter-*.md`.

**Verdict on the input:** a strong chapter. It already has chaos (the onion, Horace, the barge man), an ugly sentence, 0 negation
pivots and no simile surplus. I applied 6 small operations. Net prose −19 words (style 3,840 → 3,821). Dialogue went
**15.2% → 15.4%**: net speech went up (+8 spoken words) and narration went down.

## Operations Applied

| # | Operation | Location | Before → After (brief) |
|---|-----------|----------|----------------------|
| 1 | Missing paragraph | after "Nothing came." | Cut the whole "For five years he had been a description on a notice … and gone to his lunch." It summarized the subtext ("nothing to hide behind"), and it was the third time the chapter said the judge heard him out and believed him (also at the steps paragraph and in the five words). "Nothing came." now goes straight into the onion. |
| 2 | Explanation surgery (anchor) | the lamplit back | "The judge had found for the plaintiff. ~~Valens had his name, said out loud in the Basilica Julia, and this was the same back.~~ Every mark was where it had always been." The verdict was a dowry finding for Plautia, and that verdict set against the unchanged marks now carries the emotional surprise with no gloss. |
| 3 | Explanation surgery (heat) | "His hands were on the blanket still" | Cut "He held them open because I had asked" (this restated "This one he kept because I wanted it") and cut "That was new, in three years, by any light." (significance-tagging). Now: "His hands were on the blanket still, open, and he let me look at his face with nothing in front of it." |
| 4 | Rain-as-mood break (×2) | climax; door-side turn | (a) "I came with the rain drumming in my ears and …" → "I came, my fingers spread wide on his chest, …". The weather no longer rises with her. (b) "The rain had eased to a steady wash on the tiles." (calm after sex, matching on cue) → "A lamp had been lit underneath us. It showed in lines between the boards, and somebody down there was talking low to the gray." This answers "He'll do it" without saying so, and he turns his back to the door after hearing it. The 93-word rain fade is untouched, so the rain eases only once, at the end. |
| 5 | Landlady: comic → truer | end of the through-the-floor paragraph | After her tirade against the towpath, the canal and "whoever had dug it", added: "Then she stopped, somewhere about the canal, and nobody down there said anything more." Her comic fury breaks off when the man is home, and it is never explained. It adds no hen/roof address (Acca stays at 3). |
| 6 | Tender aftermath + body comedy | after "He kept hold of me, and I let him" | "…, until my left calf knotted under me. / "Leg," I said. "Leg, leg." / He took my foot behind me and pushed the toes back until it let go." This is the six-months body kneeling on a strung bed, and his care goes back to a task without anyone pointing at it. Then "Getting off him was no more graceful than getting on." has something to follow. |
| 7 | Dialogue mess | the road plan | "And if it doesn't?" / "It won't," the older carter put in from his end. / "Three," Valens said. The carter answers a question nobody asked him. The neat ping-pong breaks, and net speech goes up. |
| — | Trim (state repeat) | supper, "I sat." paragraph | Cut "These days I was always hungry." It was ahead of the Writer's protected ugly sentence ("I was hungry the way I was always hungry now…"), which said the same thing. |

## Operations NOT Applied (and why)
- **Irrelevant thought:** skipped. Horace is already in place, Ch.22 had the 1991 memory, and the onion is the outline's chaos moment. A third would make the device run on a cadence.
- **Ugly sentence:** skipped. The Writer's two already stand.
- **Precision deflation:** skipped. The numbers serve the story or the period ("four pieces of eel", "two hundred paces", the eight-scored loaf, "three by the sound of their feet").
- **Negation break:** none to break (0 pivots).
- **Emotional control break:** skipped. Valens's break is already designed into the heat ("His breath left him and was a while returning", the sound into her skin), and a Mara leak would cut against "her asides go quiet". It would also risk a mouth or laugh channel, which is spent.
- **Simile surgery proper:** at 1.3/1k all similes characterize. The one heat comparison ("as he would steady a load on a bad slope") is the allowed one.

## Protected (unchanged)
The opener "The blanket had been made for a horse."; the five words; the onion lines; "Your left knee … The cords are lower on this
side."; the door-side exchange and the turn; the kick against the scars; "It's right." and the breath through the nose; the 93-word fade.

## Strongest Disruption
#4b, the lamp below. Before, the rain easing gave the tender aftermath its mood. Now the world finishes its own business: someone sees to the lame
gray, which Valens heard through the floor and would not go down to. Only after that does he turn his back to the door. His last duty is discharged by somebody else,
and nobody says so.

## Risk Assessment
- **The cramp (#6)** is comedy inside the afterglow. It is kept to three short lines, with no laugh from Mara and no comment. If the evaluator reads it as
  undercutting "Stay. A while.", cut back to "until my left calf knotted under me." and drop his hand.
- **"somewhere about the canal"** is deliberately loose wording (she stops partway through her list). An editor may want "partway through
  the canal". Keep it loose if possible.
- Deleting the notice/muleteer paragraph drops the reach back to "a description on a notice". It is not a re-read reward that needs keeping, because Ch.9 carries it.
- **Bible re-sync for downstream:** At-risk after Ch.23 should drop "These days I was always hungry." (CUT), add the cramp ("Leg," /
  "Leg, leg.") and the lamp lines below the boards as spent staging, and log the carter's "It won't," as a walk-on line.

## Gates (from the book folder, after edits)
- `bash tools/check_chapter.sh 23` → **ALL MECHANICAL GATES CLEAN** (style 3,821w, simile 1.3/1k, em-dash 0; voice-wear strict clean;
  tic gate clean; dlg 15.4%; shape clean).
- `python3 tools/tic_report.py --echoes 23` → 0 echoes, 0 command echoes, 0 spoken-line echoes. These second uses came from my own new lines and
  were varied before the final run: "had not been asked", "I came with my", "when I came", "below us the", "broke off in the
  middle", "there was only the", "from the stalls", "up toward the", "the mules went". A first version, "kneeling on", also pushed the
  kneel class book-wide and was removed.
