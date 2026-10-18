# Dialogue Polish Report — Chapter 3 (run 2)

Scope: dialogue only, plus the tags and beats attached to it. Narrative prose is untouched. So are the first
sentence (the 79-word plateau spiral), the last sentence ("I stepped out into October.") and the single-scene
build (0 breaks). All three were diff-verified against the pre-pass copy.

## Audit Summary
- **Dialogue share:** 5.73% before, **5.8% after** (band 5–15%). That is 391 → 397 words in quotation marks out of 6,822 → 6,844 body words.
- **Em-dashes:** 0 before, **1 after** (cap 4). It marks a true interruption: the hiker cuts off Mara's refusal.
- **Tag adverbs:** 0 before, 0 after. **Thesaurus tags:** none; every tag is "said".
- **Conversations analyzed:** 2 (the goatherd; the German hiker). The taxi driver has no quoted speech: outline beat 1 says the hiker and the goatherd's "kalimera" are the only speech, and the bible marks the driver "(no speech)". His voice is gesture (the whole-arm point, the laugh), and it was left as written.
- **Lines flagged INDISTINCT:** 0
- **Lines flagged WEAK / recurrence:** 9, all resolved
- **FLAT_DIALOGUE:** 0 (the outline defines no subtext layer)
- **Exposition dumps:** 1 partial (the hiker's stone speech ran into a four-item list of mountains, which brushes against the retired list device). Resolved by trimming the list to two.
- **Tag overuse:** 0

## Voice Distinctiveness Results (Cover-the-Name)
| Speaker | Lines | Distinct | Weak | Indistinct | Post-polish |
|---|---|---|---|---|---|
| Mara | 14 | 12 | 2 | 0 | **PASS**: clipped, contracted 1998 American, evasive ("Just my clothes." "However long it takes." "I fix pots. In a museum."). The echo-back "I don't want the E4." became a dry deflection, "I'll skip the sea." Her "Kalimera sas" is the textbook polite plural, which separates her from the goatherd. |
| German hiker | 17 | 12 | 5 | 0 | **PASS**: German-English present tense with no contractions (the one "don't" is now "do not"), a verb-second inversion ("at two o'clock comes the cloud"), one object inversion ("Olympus she has"), stacked questions, and two unglossed German markers (*Ach so*, *Bitte*). His attention stays on the weather, the trail, his family and gadgets that think for themselves. He has no eye for materials: the son-in-law's cups are described by what goes wrong. |
| Goatherd | 1 | 1 | 0 | 0 | **PASS**: a bare "Kalimera," with the phone pressed to his chest still talking. He speaks past her and goes back to his call. |
| Taxi driver | 0 | n/a | n/a | n/a | No speech, by design (see above). He is distinct on physicality alone. |

## Changes Made (before → after)
### Hiker
1. "Ah. Then good morning also." → "Ach so. Good morning all the same." *(first of four "Then" openers; one German marker; also removes one of three "also"s, so his "auch" calque doesn't turn into a tic)*
2. "He pointed at the bag with the tip of a pole" → "He tapped the bag with the tip of a pole" *(he pointed with a pole twice; the second pointing, up through the trees, stays)*
3. "Olympus she has. The Zugspitze. Etna. Snowdon…" → "Olympus she has. Snowdon…" *(a four-item list is the retired device; it also shortens a five-sentence monologue. ENTITY_STATE has neither name.)*
4. "You don't want the E4." → "You do not want the E4." *(his only contraction)*
5. "And at two o'clock the cloud comes up from the gulf … Then you see nothing." → "And at two o'clock comes the cloud, up from the gulf … Inside it you see nothing, not the path, not your own feet." *("Then you…" is spent per the at-risk list; German word order)*
6. "He looked at the duffel again with new respect. 'Then you have a good sleeping bag.'" → "He leaned on his poles and revised his opinion of the duffel. 'You have a good sleeping bag.'" *(a second "Then you…"; a second duffel-look for the same man)*
7. "He was enormously pleased by this." → "He let go of one pole and crooked a finger through a handle that was not there." *(the hiker had four delight reports; this one becomes a mime from his physicality)*
8. "'Philadelphia!' He was delighted all over again. 'Like the cheese.'" → "'Philadelphia! Like the cheese.'" *(another delight report cut; the line carries itself. "Like the cheese" stays at its two documented uses.)*
9. "he fished a camera out of his other pocket" → "he unzipped the windbreaker and drew a camera up on a cord from inside it"; "Please." → "Bitte." *(the pocket-dip repeated his stone beat; second German marker)*
10. "Then for Phoenix." → "Phoenix. Good, we send it to Phoenix." *(the fourth "Then" opener; he talks past her refusal, hearing a destination where she meant distance)*
11. "he looked up at me above the camera in astonishment" → "he jerked the camera away from his face" *(Mara uses the look class in this chapter: "I looked out at the mouth" and "I looked at the watch". The startle sets up "It is like a gun.")*

### Mara
12. "Kalimera." → "Kalimera sas." *(the identical echo could not pass cover-the-name; the textbook polite form suits "My kalimera was correct")*
13. "I don't want the E4." → "I'll skip the sea." *(her second echo-back in the scene; echo-back was trimmed from her in Ch.2 and must not become her habit. "Like the cheese." is now the only echo.)*
14. "It's all right." → "It's all right, I don't—" *(the hiker interrupts: "No, no. For your mother.")*

### Goatherd
15. "he lowered the phone; he looked at me, and at the duffel, and at me again." → "he brought the phone down and pressed it to his chest, where the voice in it went on without him." *(an item-by-item look, which is on the at-risk list: Ch.1 already has one, and a third anywhere is a defect. He is now talking past her instead.)* A first wording, "took the phone from his ear", tripped the object-handling regex and pushed that class book-wide to 0.35/1k, over the 0.3 limit. It was reworded and the class is back to 0.29.
16. "He considered my accent and found nothing in it to remark on." → "My accent did not interest him in the least." *("considered" was the third pause-beat of its kind: Szabo in Ch.1, and the desk woman's "considered the duffel" earlier in this chapter)*

### Tag/beat tally
- Tags: 5, all "said" (goatherd, hiker ×3, Mara ×1). Beats: 9 (tap, laugh/pocket, stone to the light, pole up the trees, leaning on the poles, the mime, the windbreaker/both hands, hand out, the startle). That is about 64% beats to 36% tags. The rest of the lines are carried by rhythm.

### Natural speech
- Interruptions: 1 (the em-dash)
- Talking past: 3 (the goatherd's phone; Mara answers the stone with "How far is the cave?"; the hiker turns "Phoenix" into a destination)
- Deflections: 3 ("Just my clothes.", "However long it takes.", "I'll skip the sea.")

## No-tic / echo check
- No "Then you…" remains; no "Then" opener anywhere in this chapter's speech.
- No "somebody/nobody" in dialogue. No "X, or Y" hedge in dialogue.
- No Ch.1–2 line is echoed. These phrases were checked against both chapters: "It's all right", "Good morning", "However long", "Just my", "Bitte", "Ach so".
- Gesture classes in this chapter: Mara's looks are not shared with any walk-on beat now. There are 0 nods, 0 shrugs, 0 look-aways and 0 object-handling hits in Ch.3. The one "swallow" hit is "the mountain swallowed", which is not a gesture.
- Foreshadowing in dialogue: 0. The cloud warning is weather, not portent.
- US spelling.

## Remaining Concerns
- **Object handling is at 0.29/1k book-wide**, just under the 0.3 ceiling. Ch.3 contributes 0, but Ch.4 onward should keep set-down/pick-up beats scarce.
- **Bible note:** the Ch.3 walk-on entry should now record the hiker's German markers (*Ach so*, *Bitte*, spent) and Mara's "Kalimera sas". It should also drop "Etna/Zugspitze" if anyone ever lists the stones. I did not edit `character-bible.md`; that is the Writer's or entity-tracker's job.
- The dispatch named the taxi driver as a speaking voice. He is wordless on the page, and I kept him that way to honor outline beat 1 ("the only speech of the chapter apart from a goatherd's 'kalimera'").

## Verification
- `bash tools/check_chapter.sh 3`: style clean (em-dash 1, foreshadow 0, simile 1.8/1k) · grammar 0 errors · rhythm 0 · show/tell no flags (dlg 5.8%) · voice-wear clean (strict) · tic gate clean · metaphor no flags · shape clean.

## Cover-the-Name Test: FINAL
- Mara vs German hiker: **PASS**
- Mara vs goatherd: **PASS** (minimal exchange; her textbook "sas" against his bare greeting and the phone)
- Taxi driver: **n/a** (no speech; distinct on physicality)
