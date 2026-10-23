# Dialogue Polish Report — Chapter 23, "An Inn on the Appian Way"

Pass: dialogue-polish, 2026-10-23. Chapter edited in place; not committed.

## Audit Summary
- **Dialogue ratio:** 14.99% before (575 of 3,837 words; show_tell reported 15.0) → **15.21% after** (585 of 3,847; show_tell 15.2). Target 15–25%. Net spoken words +10.
- **Conversations analyzed:** 9 (the blanket at the ladder foot; the hen; the carters' mule quarrel; the driver and the carters; supper and the towpath; the road plan and the bowl; "I missed it"; the fleas; the room upstairs, including the five words, the onion, the barge man below, the heat and the door side)
- **Lines flagged INDISTINCT:** 0
- **Lines flagged WEAK:** 1 (Valens's "A small one.", a voice-card breach rather than a weak voice) → resolved 1
- **FLAT_DIALOGUE flags:** 0. Every exchange runs under its surface: the towpath stands for the barge man, "You're not hungry?" / "Eat it." for his grief, "It was the same." for what she missed, "It's done" for the cover he has lost.
- **Exposition dumps found:** 0. Valens's towpath report is four short sentences in his own register, and Acca asks for it for her own reasons.
- **Tag overuse instances:** 0. "said" is the default and beats are sparse. Creative tags: 0. "complained" and "told" are speech acts.
- **Acca's hen/roof address:** 4 → **3** (brief cap ≤3)
- **Spoken "Then…" openers:** 2 (unchanged: "Then they won't." / "Then I'll hear it.")

## Voice Distinctiveness Results
| Character | Lines | Distinct | Weak | Indistinct | Post-Polish |
|-----------|-------|----------|------|------------|-------------|
| Mara | ~24 | 24 | 0 | 0 | DISTINCT (asking questions, qualifying, dry about her body, quiet in the heat) |
| Valens | ~27 | 26 | 1 | 0 | DISTINCT (level declaratives, footing and animals, no comparison) |
| Acca | ~17 | 17 | 0 | 0 | DISTINCT (verbless facts, the road as water and animals, worry only through repetition to the hen) |
| Carters | 8 | 8 | 0 | 0 | DISTINCT (sardonic mule talk) |
| Driver | 2 | 2 | 0 | 0 | DISTINCT (grievance) |
| Barge man | 3 → 4 | 4 | 0 | 0 | DISTINCT (tired, laconic, mildly teasing) |

## Changes Made
### Voice Adjustments
- **Valens (heat, mounting):** cut `"I'm the size of a wine jar," I said. / "A small one."` (9 spoken words). By agreeing to the comparison, "A small one" has Valens comparing her body to an object out loud, which breaks voice-dna §3 and §5 ("never uses a simile or comparison in speech"; "He never compares her to anything aloud"). It was also Mara's second size joke, coming right after "most of it's swollen", so her humor did not go quiet when the heat began. Replaced with `"Your left knee," he said. "The cords are lower on this side."` (10 words). This is his attention to footing (§3: footing, how a body moves) turned into care. It is plain and true, not coy and not porn-dialogue, and it adds no gesture beat.
- **Acca (going up the ladder):** `"Shout if the roof comes in," the landlady told the hen.` → `…the landlady said to our backs.` This brings her hen/roof address down to 3 notes, each in a different form: speaking to the roof in dialect, gathering the hen up and "told it so", and telling the roof "a word that I did know". The line now reaches the guests as she turns away, which fits her card ("she leaves before the answer settles"). My first wording, "called after us", tripped the echo scan (Ch.17), so I varied it.

### Natural Speech / Net-Speech Replacement
- **Barge man (through the floor):** added `"Let me get them dry first. You can shout after."` (10 words) after Acca's "what have you done to the gray?". He puts the mules first and answers her fury tiredly and fondly. This sets up the narrated "giving him her opinion of the towpath…" and gives nothing away: Valens's "Off hind. He's walked it through the water." is still his alone, heard through the boards. It adds speech to offset the cut.

### Tag/Beat Replacements
- 0 tags replaced with beats. 1 attribution changed ("told the hen" → "said to our backs"). No new gesture beats.

### Kept as written (brief focus)
- **The five words:** `"It's done," he said. "They believed me."` / `"Yes."` Untouched. The subtext ("now I have nothing to hide behind") is carried only by the narrated silence ("Nothing came.") and the onion memory. No character says it.
- No triumph speech and no aphorism about truth anywhere. The Kirrha exchange ("It was the same." … "Near enough the same.") stays deflective.
- Heat dialogue is all short and true: "Look, then. All of it's yours, and most of it's swollen." (her one spoken joke, made while undressing, before the silence), "Not my breasts", "Will it hurt the child?", the Grata exchange, "Let me," "Mara." / "I know.", "Stay," … "A while." No porn-dialogue, nothing coy.
- No who-pays / "Whose …?" construction in any mouth. No foreshadowing. No command echoed back. No spoken line repeats an earlier chapter (echo scan: 0).

## Remaining Concerns
- **character-bible.md re-sync (for the downstream chain):** the at-risk-after-Ch.23 block still quotes `"I'm the size of a wine jar," / "A small one."` as spent staging. Replace it with `"Your left knee," … "The cords are lower on this side."` and list the cut string as CUT (never restore). The ACCA card's "4 on the page (roof twice, hen twice)" should now read **3 (roof twice, hen once)**, and her "Shout if the roof comes in" is addressed "to our backs". Add the barge man's "Let me get them dry first. You can shout after." to the Ch.23 walk-ons.
- The dialogue ratio is still close to the floor (15.2%). Later passes (hook-craft, disruptor) should cut no net speech.
- Acca's "He'll have swapped them" sits near the carter's "He'll have you over at Fundi". The repetition in Acca's line is her designed reassurance and the constructions are common English, so I left both alone. Watch them if the Evaluator flags them.

## Cover-the-Name Test: FINAL
- Ladder foot (Acca / Mara): PASS
- Hen and fox: PASS
- Carters' mule quarrel: PASS
- Driver / carters / Valens on Fundi: PASS
- Towpath (Acca / Valens / Mara): PASS. Acca's worry still reaches the page only through the hen.
- Road plan and the bowl: PASS
- "I missed it": PASS
- Fleas: PASS
- Upstairs: blanket, boots, the five words, the onion: PASS
- Through the floor (Acca / barge man / Valens): PASS
- Heat: PASS. Valens no longer compares her to anything.
- Door side and the child: PASS

## Gates (run from the book folder after the edits)
- `bash tools/check_chapter.sh 23` → **ALL MECHANICAL GATES CLEAN** (style clean, em-dash 0, simile 1.3/1k; voice-wear strict clean; tic gate clean; show/tell dlg 15.2%; shape clean)
- `python3 tools/tic_report.py --echoes 23` → 0 echoes, 0 command echoes, 0 spoken-line echoes
