# Revision Log: Chapter 6, continuity repair (2026-10-19)

Source: `evaluations/continuity/chapter-6-audit.md`. Applied C-01, W-01 to W-16, W-18 and W-19. Skipped W-17, which is an outline fix for the orchestrator. Before making each fix I re-read the cited text in Ch.1–5 on disk. First sentence, last sentence and both breaks are unchanged.

| ID | Before | After | Note |
|---|---|---|---|
| C-01 | "The buckle was stiff with the cold. It took me two tries to work the tongue out of the hole" | "The clasp was stiff with the cold. It took me two tries to spring it" | Verified ch-01:p190 (steel band) and ch-02:p14 (pins and links). Audit wording. |
| W-01 | "since January" | "since March" | ch-01:p190–191: first wound in March. |
| W-02 | "brass, and the profile of a young man with the wind in his hair." / "A king. From farther away…" | "brass, and the head of an old man with a beard." / "A poet. From farther away…" | Ch.1–5 never describe the two coins left after ch-05:p55, so the 50-drachma piece (Homer, 1990s issue) fits. "Profile" and the hair band were dropped because the coin's exact portrait was not verified. The ENTITY coin row should record 50 dr + one smaller coin. |
| W-03 | "…at twenty minutes short of two. It was nothing to go on" | "…at twenty minutes short of two, by Athens time, which ran an hour and more ahead of this sun. It was nothing to go on" | One clause. The audit's "I had been on my knees through both" was dropped: at 1:10 the face-value hour has not come yet, so that phrase would claim a future event. |
| W-04 | "a story at the vintage" / "at the vintage" / "Since the vintage." | "a story this autumn" / "at the olive beating" / "Since the olives." | The audit's "when the olives were coming down" echoed Ch.5, so I used fresh wording. |
| W-05 | "the two of them went at it in Phocian too fast for me to follow" | "Kallia went at him in Phocian too fast for me to follow, and he answered her a word at a time" | Audit wording. |
| W-06 | "I lost half his words" | "I lost words out of everything he said," | Audit wording. The optional split of p315 was not done, so dialogue is untouched. |
| W-07 | "In this whole country not one person knows my name." | "In Delphi not one person knows my name." | |
| W-08 | "I stood up… when I stood they gave" / "standing in the bottom of the crack" | "I straightened as far as the roof let me… when I rose they gave" / "crouched in the mouth of the crack" | "I got up" would have been a 3rd book-wide use and a Ch.3 echo, so I used "straightened". |
| W-09 | "On the plain there was only snow… The huts were gone." / "somewhere on the plain" / (cliff top with no crossing) | "Below the mouth there was only snow…" (huts sentence cut) / "somewhere on the slope" / "Past the pen we crossed the plain, and I did not see the huts. At the top of the cliff path…" | Order is now cave, firs, pen, plain, cliff top, matching Ch.3–4. |
| W-10 | (none) | After the duffel at p7: "My flashlight was in there, under everything, and I had let him burn his pines rather than have him see it." | One sentence. It deals with being seen, per the bible, and avoids Ch.5's "bottom of the duffel" and "burned nothing". |
| W-11 | "I have a cousin who keeps her husband's keys in the freezer door." | "I have a cousin who wore a pearl in one ear and a gold hoop in the other through a whole church service, and her husband thought she meant it." | Takes Gloria's ch-01 earrings as the subject, not the phrase. Avoids "it was a style" and "funeral". |
| W-12 | "had let the cold out as one thread, dry, with an edge to it, while the walls around it stayed damp and slow." | "had let out a cold of its own, and my skin had singled it out at once." | Fresh wording, with no Ch.3 or Ch.5 n-grams. Two drafts were rejected for echoes ("before I knew where", "before I could"). |
| W-13 | "broad as a dinner plate" / "like the glaze on a cheap plate" | "broad as my two hands" / "like the paint on a fire escape" | Ch.3 also has a "soup plate", so the plate domain is now out of Ch.6 entirely. |
| W-14 | "That was English, and he let it pass." / "I had no answer to that, in either language." | "He let it pass." / "I had no answer to that." | The audit's "He let the English go by" was rejected because it echoes ch-01 "She let the French go by". |
| W-15 | "so I talked to his back, low." | "so I went on, low." | The audit's "uphill into the dark" was rejected as a variant of Ch.5's spent "said to the dark". |
| W-16 | p116 "The widow has not asked it" / p159 "Does the widow know" / p165 "the widow's storeroom" / p289 "Under the widow's stairs" | "Kallia has not asked it" / "Does Kallia know" / "lain awake on Kallia's floor" / "Under Kallia's stairs" | Count is now 10 → 6 (Mara p28, p30; Valens p103, p271, p316, p327). "in Kallia's storeroom" echoed Ch.5, so it became "on Kallia's floor". |
| W-18 | "in front of the whole square" | "in front of half the Way" | |
| W-19 | "I'm three months behind by now" | "I'm behind by now" | |
| (header) | stale figures | adds "6,680 / 37% after continuity repair" | Comment only. |

## Gates (run from repo root)
- `bash books/the-hour-of-ash/tools/check_chapter.sh 6`: style clean (simile 0.9/1k, adverb 3.1/1k, em-dash 3, foreshadow 0); grammar 0; rhythm 0; show/tell no flags; voice-wear strict clean; tic gate clean; echo scan 0; metaphor no flags (median 12); shape audit CLEAN.
- `python3 books/the-hour-of-ash/tools/tic_report.py --echoes 6`: 0 echoes.
- Words: 6,680 prose (shape_check), 6,795 `wc -w`. Dialogue: 37% (shape_check, the ledger metric; band 35–45), 33.0% (show/tell meter).

## For the entity tracker
- Seiko band: steel link bracelet, fold-over clasp.
- Coins: two left; the bigger is the 50-drachma (Homer). Before print, verify the portrait details (beard, profile vs three-quarter, fillet).
- The flashlight is in the duffel, unused in the cave, kept from Valens's sight.
- Emergence dated to the olive harvest, not the vintage.
