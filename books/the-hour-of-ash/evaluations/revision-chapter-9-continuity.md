# Revision Log: Chapter 9, continuity repair

**Date:** 2026-10-19
**Source:** `evaluations/continuity/chapter-9-audit.md` (run 2). This pass applies C-01 and W-01 to W-10.
**Skipped:** W-11 (the bible sync), which is done separately. N-04 was not used, because the count stayed above the floor.
**Paragraph numbers** follow the audit's convention (prose paragraphs only, so p1 is the manumission). No paragraph was added or removed, so the numbering is unchanged.

Every cited prior text was re-read on disk before its edit, and each one matched the audit:
- ch-01:p48–49, ch-06:p191–192 and ch-07:p65–66 (the three command echoes);
- ch-04:p24, ch-05:p95 and p108, ch-06:p69, p149 and p50–51, and ch-08:p46 and p99 (the notice timing);
- ch-08:p74 (the vowels);
- ch-07:p123–127 (the hearthstone);
- ch-02:p67 (the refold).

Every new phrase was grepped against Ch.1–8, voice-bank samples 01–13, the bible and the outline. There were 0 hits for "takes the weight", "for the eye", "will last", "will it stand", "along the same line", "one window", "tried it over", "closed it up", "Glykera", "Dadaphorios", "across one another" and "came in pieces". The new wording adds no in-chapter repeat.

## Changes (before → after)

| ID | Para | Before | After | Note |
|---|---|---|---|---|
| **C-01** | p90 | "He went and told them, with his mouth close to the clay, and in the morning he brought me a yellow cake of it…" | "In the morning he brought me a yellow cake of it…" | This was the fourth command echo book-wide, against a cap of 3. Compliance is now shown by its result only, as the bible's rule allows ("by its result … or not at all"). I did not use the audit's wording, for two reasons. First, "He bent to the nearest hive" would make "bent to" ×3 in the chapter (p116, p142). Second, "spoke into the clay" near-echoes ch-06:p44, Valens's "He spoke into her ear". The cut is subtractive (−11). |
| **W-01** | p172 | "*Runaway, in the autumn, from the household…*" / "…posted at Corinth in the month Boathoos.*" | "*Runaway from the household…*" / "…posted at Corinth in the month Dadaphorios.*" | Dadaphorios (≈ Nov/Dec) falls after the sea shut (ch-06:p69) and after the Boeotian road was snowed in (ch-06:p149). That makes "First carts since the snow" (p189) the first chance for a copy to arrive. "in the autumn," is cut because it contradicts Ch.6: Valens was hauling for Kallia "last winter" (ch-06:p50–51, November AD 70), so he ran before the winter of 69–70. An undated "autumn" on a notice posted in AD 70 reads as autumn 70. |
| **W-02** | p49 | "The break is at the feet. The coals are in the bowl, at the top. The heat does not come down so far." | "The rod takes the weight. The wax is only for the eye." | This removes the heat argument that inverts p37 and that p93 (wax softening in sunlight) disproves. I used my own wording rather than the audit's "The rod holds it up", which would have put a "hold" back in while W-03 removes them. p50 and p51 still follow. |
| **W-03a** | p69 | "It is not a smith's work. That is why it will hold." | "It is not a smith's work. That is why it will last." | Removes the sample-10 lift (audit wording). |
| **W-03b** | p114 | "How long will it hold?" he said. | "How long will it stand?" he said. | Removes the sample-10 lift in the same speaker, tag and frame (audit wording). It now picks up the smith's "It'll stand till the first warm day" without pointing at it. |
| **W-03c** | p51 | "It will break again where it broke before," I said, … | "It will come apart along the same line," I said, … | Removes the sample-11 lift (audit wording). The rest of the line is unchanged. |
| **W-04a** | p23 | "He was the one office in Phocis that took questions about doors…" | "He kept the one window in Phocis that took questions about doors…" | Removes the sample-04 lift (audit wording). "the one" stays at 1. |
| **W-04b** | p141 | "I closed it up along its old folds and handed it back to him…" | "I closed it up and handed it back to him…" | Removes the sample-12 / ch-02:p67 refold wording, so the gesture is free for Ch.10. A pure cut (−4) is more subtractive than the audit's recast. |
| **W-05** | p23 | "I tried it in a murmur with the Delphian vowels, and again with the book's, and both times it sounded like somebody patting her pockets for a key." | "I tried it over in a murmur, and it sounded like somebody patting her pockets for a key." | The book-vs-mouth Greek contrast is SPENT. Audit wording; the simile is kept. |
| **W-06** | p159 | "Kallia was in the court at home, scouring the big pot with sand, and she looked at my hand before she looked at my face. I opened it over the hearthstone…" | "Kallia was in the court at home, scouring the big pot with sand. I opened my hand over the hearthstone…" | Breaks the Ch.7 broken-jar template, because the eyes no longer go to the body part first. This also removes the pre-echo of p200. The touch question (p162) is kept. Audit wording. |
| **W-07** | p166 | "He says a stater for the god," I said, with my hands in the water. "And a goat that shakes. And a Delphian to stand for me, who will want a present, and the man." | "He says a stater for the god," I said, with my hands in the water, "and a goat that shakes, and the rest." | The second itemization and its "And a…" anaphora are gone. p168 and p169 still have their cues. Audit wording. |
| **W-08** | p128, p138, p139 | "Thraitta" ×3 | "Glykera" ×3 | Removes the "Thracian woman" wink set one section before the Thracian notice. The tablet means nothing again. |
| **W-09** | p181 | "…and had settled among themselves what it said." | "…and had settled among themselves what it said. They talked across one another, and what reached me came in pieces." | The comprehension clause, in the audit's wording (+12). Lines p182–p194 now read as the pieces she caught. |
| **W-10** | p11 | "…haggles with me over his own father." | "…haggles with me over his own grandfather." | Euangelos is on the stone; it is the grandfather who was cut. Audit wording. |

The header word-count comment is annotated as well (it is an HTML comment, so it does not count as prose).

## Held fixed (verified after the edits)

| Item | Before | After |
|---|---|---|
| Prose words (shape_check) | 5,892 | **5,840** (floor 5,800; N-04 not needed, so not used) |
| style_check count / wc -w | — | 5,869 / 6,013 |
| Dialogue | 27.8% shape / 27.0% meter | **28% shape / 26.9% meter** (band 25–35) |
| Median sentence | 15 | **15** (gear mid); fig 2.9/1k; 6.9% of sentences over 40 words |
| Breaks | 5 | **5** |
| Open / close | p1 manumission (`narrative`) / "He let the gray drink first." (`punch`) | both untouched |
| And-chains / asides / pivots / So / hinge | 3 / 0 / 0 / 0 | 3 / 0 / 0 / 0 |

## Gates

- `bash books/the-hour-of-ash/tools/check_chapter.sh 9`: all clean.
  - Style clean (simile 1.9/1k, adverb 2.9/1k, em-dash 1). Grammar 0. Rhythm 0. Show/tell no flags. Voice-wear strict clean.
  - Tic gate clean, gesture layer included. Echo scan 0. Command-echo candidates: none.
  - Shape audit CLEAN.
  - The book-wide 'So …' WATCH line refers to the Ch.2–6 streak, which was already there; Ch.9 has 0.
- `python3 books/the-hour-of-ash/tools/tic_report.py --echoes 9`: **0 echoes**; command-echo candidates: none.

## For the bible sync (W-11) and the tracker
- **Bible at-risk after Ch.9, "Telling the bees":** the narrated instance is gone. The page now has two tags (p82 "he told them"; p83) and the order at p89; the wax arrives by result only. **Command echo stays at 3 book-wide.**
- **"Similes spent in Ch.9":** unchanged (the pocket-patting simile was kept).
- **"the one / the only":** 1, now "the one window in Phocis".
- **The price of the god:** the page itemizes it once (Euthydikos). Mara's line to Kallia is no longer a list.
- **Walk-on note:** Thraitta → Glykera.
- **ENTITY:** P5 resolved by the page (Dadaphorios AD 70; "First carts since the snow"). Celer timeline row: notice posted Dadaphorios. The notice no longer states a season for the flight.
