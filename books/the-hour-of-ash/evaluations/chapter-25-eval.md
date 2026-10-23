# Evaluation: Chapter 25 — Augurinus (run 2) · Single-scene, one afternoon in one upper room · TURNING POINT ~60%, the WHEN
**Evaluator:** book-evaluator (independent; did not write or revise this prose) | **Date:** 2026-10-23 | **Cycle:** 0
**Text evaluated:** `manuscript/chapters/chapter-25.md`, md5 `9fe39d862250573bc347e5caea6324c7`. This is the page after writer → dialogue-polish → hook-craft (no edits) → disruptor → continuity repair (CRIT-001…007, WARN-01…19 bar 18, INFO-01/02/05/07/08, all logged as done). Nothing the repair fixed or ruled on is re-raised here.

**Measured on the real file** (from the book folder):
- `bash tools/check_chapter.sh 25`: **ALL MECHANICAL GATES CLEAN** (style, grammar, rhythm, show/tell, voice-wear strict, tic gate including gestures, echo scan 0, metaphor, SHAPE CLEAN).
- `python3 tools/tic_report.py --echoes 25`: 0 echoes, 0 command echoes, 0 spoken-line echoes. `--gate`: clean. The gesture layer finds 2× "a (long) moment" and 1× shrug in Ch.25, both under cap.
- 7,499 words by the shape count (7,865 `wc -w` with the header), 89% of the 8,400 target. Nothing is padded, and the target is a ceiling. Dialogue **49%** (band 45–55). 0 breaks. Median sentence **11**, mean 16.1, 5.6% of sentences over 40 words. Simile 20 (fig 2.9/1k). Em-dash 3, all of them interruptions in speech. And-chains 6/9. Negation pivots 0. "So" openers 0. Credential asides 0.
- Shape: `scene-set` ("It was the first fair week…") → `punch` ("I told him his arithmetic was wrong.", 7 words, a single-sentence closing paragraph, which Ch.25 is on the allowed list for).

**Read against:** the book CLAUDE.md; STATE.yaml guardrails, retired reflexes, ARCH-6/14/16/17, AUTHOR-CP2-2 (memories), CP4-1, END-1; outline ledger row 25 and `## Chapter 25` (every NON-NEGOTIABLE, the writer warnings and the beat subversion); foundation §Fenn, §6a and the emotional-arc row; voice-dna §0 (no foreshadowing, the mountain rule) and §1; character-bible (the FENN card including its "Ch.25 as written" block, LUCIUS, the Ch.25 walk-ons, MARA's five spent laugh shapes, At-risk after Ch.21/22/23/24 and its Ch.25 guards, the at-risk table); voice-bank sample-09 (reserved for this chapter); chapter-24 (handoff), chapter-1 l.179/199 (Szabo, Margaret, the Phillies cigar box), chapter-14 l.6 ("I knew the year"); the dialogue, hook and disruption reports; and `continuity/chapter-25-audit.md` with its repair log.

**Genre profile:** commercial historical romance / time-slip (comp *Outlander*). Anti-AI band commercial (0–8 clean). The #11 cap is >6 instances or >0.8/1k. Dimension 7 = **IMMERSION**. Engagement (STATE): empathy 55 / fascination 30 / self-insertion 15.

*(l.N = line number in the current `chapter-25.md`.)*

---

## HEADLINE
**CVI-Launch:** **9.8** (9.3 + 0.5 strong anchor) | **CVI-Legacy:** **7.3** | **Genesis Floor:** **8.0** | **Genesis Average:** **8.71** | **Casual Reader:** **9.0**

**Engagement type (this chapter):** Fascination 45 (an American from 1968 alive as a Roman astrologer, the doors' law, Puteoli's ground rising and sinking) · Empathy 45 (the estate sale he does not ask about; a wife whose husband finally believes her) · Self-insertion 10.

**Divergence alert:** CVI-Launch 9.8 against a Floor of 8.0 is a gap of 1.8, just under the 2.0 flag. This is the most commercially potent chapter in Part Two and the book's best set piece since the Oracle. The Floor sits on narrated-state counts that no gate measures. **Valens's "post" in the doorway** is noted 6 times, and the stage notes for Fenn (the tremor 4, the runaway talk 4, the turning on his stool 7, with "swung round" twice in 151 words) push past the hand rule. On top of that come two blocking slips, two short lifts from voice-bank sample-09, and one SPENT object (Ch.22's lead-stapled pot). All of these are clause-level cuts (F1–F11, tested). Nothing is structural, and no beat needs rewriting.

**Gate:** Floor 8.0 < 8.5 → **POLISH** (Casual 9.0 ✓, pacing ✓, mechanical gates clean ✓).

---

## PACING VS NEIGHBOURS (gate item, judged)

| | Ch.23 | Ch.24 | **Ch.25** | Ch.26 (planned) |
|---|---|---|---|---|
| Shape | Single-scene, 0 breaks | Fragmented, 9 time-stamped shards | **Single-scene, 0 breaks** | Collage, 7 breaks |
| Length | 3,366 | 5,720 | **7,499** (89%) | 6,000 |
| Gear (planned) / median / mean | low / 11 / 13.0 | low / 10 / 13.3 | **mid / 11 / 15.5–16.1** | mid |
| Dialogue | 17% | 29% | **49%** (band 45–55) | 10–20% |
| Slot | valley (held) | the stakes made flesh | **turning point (the WHEN)** | deepen Fenn; Aelia; the refusal shown |

- **The median of 11 against a mid-gear row serves the chapter here, and it does not hurt it.** The ledger itself sets up the tension: a 45–55% dialogue band in a two-hander guarantees many short turns ("Please.", "Beats me.", "What?", "Mules."). Narration and speech both have a median of about 11. What carries the "mid" feel is the **spread**. The mean rose from 13.3 (Ch.24) to about 16, and 5.6% of sentences run past 40 words. Those long sentences are where the outline puts the slow story: Fenn's runaway and-chains (the 1964 collapse l.136, the snow l.174, Claudius l.182, the Navy l.186, the town "like a fat man asleep" l.210, the carter l.254, the law l.264, the backward tables l.328) and Mara's collapse (l.60). The four reading speeds the outline asks for all land:
  1. **Quick recognition** (l.36–66): one-line paragraphs ("It was a cigarette lighter.", "Thanks," "Jesus H. Christ").
  2. **Slow story**: the long speeches.
  3. **Very fast date** (l.156–162): "Late summer, seventy-nine." is dropped at the end of a happy run, then a two-sentence cutaway ("Down on the quay a man was crying sprats. The gulls went over."), then "What?"
  4. **A dead stop**: the 7-word close.
- **Book-level WATCH, not a Ch.25 finding:** Ch.23, 24 and 25 now all measure a median of 10–11. Ch.26 (collage, 10–20% dialogue, mid) is in a position to break the run, and its letters and narration should genuinely land at 14+.
- **Value shift, clean, on two axes.** Mara goes from not having the WHEN to holding it and refusing it ("I told him his arithmetic was wrong."). Valens goes from carrying a story he loved her through to believing it: the flush at l.80, "Does he know the door?" at l.294.
- **One soft stretch, not a sag.** l.186–236 is about 1,300 words: the Navy sky, the tremor curve, the wine, the automat, the mooring rings, the bathhouse pool and the nursing. It is the lonely-host subtext and the fascination engine, and the ship's boy (l.224) interrupts it, but the Devourer will skim the mooring-rings speech (l.210).
- **Handoff:** from Ch.24 the uncast hour pays off ("He had the hour from me, as near as any of us had it", l.442), and so does the Chaldean rumour, heard first-hand and never quoted back ("gibberish" 0). Toward Ch.26, Fenn promises letters and "every figure" in his tables (l.406, 414), against her refusal. Nothing of Ch.26 is pre-spent except the 1964 collapse, which the audit has already cascaded to the outline (WARN-18).
- **Ledger honoured:** `scene-set` / `punch`, 0 breaks, dialogue in band, theme present, the length serving the beat.

**PACING: OK.**

---

## Genesis Score (Craft Assessment)

| Dimension | Score | Evidence | Cap Reasons |
|-----------|-------|----------|-------------|
| Originality | **9.0** | Three original elements: (1) the recognition comes through a muttered lost-object line, "Where the hell'd you get to," … "It's on the sill, by the basil," … "Thanks," (l.46–52), so the first English in five years is *thanks, for finding his lighter* (l.60); (2) the beat subversion is fully realised: the WHEN arrives as a happy afterthought in mid-boast, "This is swell. Nothing this good's happened to me since Nero was a pup. Late summer, seventy-nine." (l.156), and it is the heroine who withholds; (3) the close is built from two opposite withholdings, the fire she keeps back out of mercy (l.446) and the refusal she says aloud out of need (l.448). Also: the Augurinus/augur joke that only she gets (l.102–106); Valens's horse-sense applied to a basil (l.424). | none |
| Theme | **9.0** | "A man who never unpacked, face to face with a woman who keeps a bag packed" is carried entirely by objects and by Fenn's own mouth, never by the narrator: the oiled-leather bag by the door "with dust on top of it, an even gray fur" against "My hand had gone to the flap of the satchel at my hip." (l.230); "You don't go buying furniture in a hotel." (l.234); and the line that lands on Mara and Valens unremarked, "Marry them and then go home on them. That's a lousy thing to do to a person." (l.234). "You're wrong" is "please be wrong": "Maybe it opens next spring, on some little shake nobody even notices" (l.348). Texture is well over 30% (sprats, octopus seller, olive pits, honeyed sour wine, Pat's hose, the 34 trolley). | not 9.5: the mirror objects (bag, hotel, widow, basil turned to the room) sit close together in l.230–236 and l.418–426; each is earned, but the Critic feels the pressure |
| Characters | **8.0** (uncapped 9.0) | **Fenn is the best-realised secondary character in the book:** frozen 1968 English ("Holy smoke", "whaddaya know", "cripes", "a sap", "a chump") against courtly Greek ("Sir, forgive me my manners; I am old.", l.86; "Leave him, sir," … "He is improving it.", l.276); he sees people last ("looked … at last", the stool turned to the wall while she nurses, l.218); sunk cost ("You finish what you pay for. Otherwise why'd you pay?", l.198); he never lists. **Valens** believes without a word (l.80), turns a basil (l.236, 424), and asks "Will they be true?" (l.434). **Lucius** has his own moment: the sand, "with deep suspicion" (l.270–278). Mara's chaos is 4/4, inhabited (see below). | **Hand rule, >3 notes of one state fails:** Valens's sentry post in the doorway is noted 6 times (l.80, 236 "returned to his post", 274 "came a pace off his post", 298 "took up his place in the door again", 390, 428). Fenn's tremor is noted 4 times (l.38, 328, 382, 394). Fenn's runaway talk is narrated as a state 4 times ("He was off again", l.186; l.228; l.236; "He was away again", l.264). The Fenn-turns class reaches 7 (l.54, 82, 90, 218, 234, 246, 432), with "swung round" verbatim at l.54 and l.82 → **cap 8.0** (the same practice as Ch.24) |
| Prose & Voice | **8.5** | **Stopping sentence:** "I laughed because he had said thanks." (l.60). **Underlines:** "a little smudged moon where there had been no moon before" (l.164); "He did not ask whose." (l.380); "He was pinning his own hand to the wood and not asking, and I watched him not ask." (l.382); "A bus," he said, and later, "a bus," once more (l.388); "and someone had added honey after that, as an apology" (l.200); "I kept the fire to myself." (l.446). **Ugly sentence:** "I drank mine, and it was terrible, and I drank it." (l.200). **Voice under pressure:** the collapse is one breath-starved paragraph with hands acting ahead of her (l.60), and in the argument "My voice was climbing, getting quick, the voice I used on the phone with insurance companies, and I could not bring it down." (l.344). | not capped; the findings below are hygiene: short lifts from sample-09 at l.58 and l.96 (F6/F7), a SPENT stapled pot at l.34 (F8), the "[X] told [object]" frame at l.46 rebuilt from Ch.24 (F9), and narration "breath" at l.232 thinning Fenn's law-word (F10) |
| Pacing | **8.5** | See PACING VS NEIGHBOURS. The date blurted and cut away from ("Down on the quay a man was crying sprats. The gulls went over.", l.158) is the fastest beat in Part Two. The ship's boy (l.224–228) breaks the longest run. The argument tightens to one-line turns (l.336–358). | not 9.0: the l.186–236 middle is long; and see the median WATCH |
| Emotion | **9.0** | **Anchor lands:** "Jesus H. Christ," … "He said it like the men on my father's block, on Sunday afternoons in the fall, when the Eagles fumbled on somebody's radio" (l.56–58). **Surprise:** laughter at "thanks"; the WHEN given as joy; Fenn's modesty during the feeding; the bus. **Body rebel:** "my legs had gone"; "The tears ran straight off my chin."; her hands save the papyrus "while the rest of me laughed and wept and had no air for either" (l.60). **Techniques:** physical, humour in grief, dramatic irony (the reader knows 79), withholding (Margaret, the fire), objects (the 23 to Chestnut Hill). | none |
| Immersion | **9.0** | Two worlds at the Outlander standard. Flavian Puteoli: the tunny sheds, blood channels and gulls (l.8); "after the sea opened" (the sailing season); the astrologer's sand tray and bronze rod; ship's hours cast for captains; resinated wine soured and honeyed; Vespasian's "bad-tempered mouth" on a copper (l.202); bradyseism read off the mooring rings (l.210, true to Puteoli); the Solfatara's hot springs; the Misenum fleet. Fenn's 1960s Philadelphia: Horn & Hardart on Chestnut Street, the 34 out Baltimore Avenue, the 23 on Germantown Avenue (bus since 1992, as she says), Connie Mack and its 1971 fire, a Girard Avenue bar. The 1964 collapse is correct in every detail (6½ up with 12 to play; Bunning and Short on two days' rest; Ruiz stealing home with Frank Robinson up; ten straight losses), and so is the 1980 Series (McGraw, Kansas City, the Broad Street parade). | not 9.5: the l.236/l.246 blocking slips (F1a, F5) cost the Hostile reader's trust in the room |
| **FLOOR** | **8.0** | Characters | |
| **AVERAGE** | **8.71** | (9.0 + 9.0 + 8.0 + 8.5 + 8.5 + 9.0 + 9.0) / 7 | |

### Narrated-state and recurrence hand count (spec: >3 notes of one state, or 3 inside ~500 words, fails)

| Item | Lines | Count | Verdict |
|---|---|---|---|
| **Valens's post in the doorway (sentry state)** | 80, **236, 274, 298**, 390, 428 (68 arrival and 196 the cup are blocking, not counted) | 6, with "post" ×2 | **F1a–d → 3** (l.80, 390, 428) |
| **Fenn's left-hand tremor** | 38, **328**, 382, 394 | 4 | **F2 → 3** (introduction, held down, it stays) |
| **Fenn's runaway talk narrated** | 186 "off again", 228, 236, **264 "away again"** | 4, with "[off/away] again" ×2 | **F3 → 3** |
| **Fenn turning on stool/table** | 54, **82**, 90, 218, 234, **246**, 432 | 7, "swung round" ×2 within 151 words | **F4, F5 → 5** (F5 also fixes the blocking) |
| Fenn's lighter handled | 52, 168, 234, 260 | 4, spread over 210 lines (no 3 in 400 words) | OK; it is his card's object and is never lit |
| Valens stopped / still | 80, 390 | 2 | OK (Ch.24 WATCH ≤3) |
| Valens's narrated waiting | 298 (rocking) | 1 | OK (≤1) |
| Narration "Nobody had …" | 10 | 1 | OK (WATCH ≤1 from Ch.25) |
| Fenn's "nobody … but me" | 102, 210 | 2 | WATCH: no third in Ch.26–27 |
| "Get out" / "kid" / "okay" in Fenn's mouth | 116, 242 / 64, 398 / 90, 152 | 2 / 2 / 2 | at the card's WATCH; rest "Get out" in Ch.26–27 |
| breathe-family | Fenn ×6 (law), narration ×3 (60, 108, **232**) | 9 | **F10** removes l.232 so the narration does not wear the law-word |
| Talking to an object | 46 "he told it" | 1 | **F9**: the frame repeats Ch.24's "Statia told the door" one chapter later |

### Laws (scan)
- **NO FORESHADOWING: 0.** The narration never reaches forward. "They'll be up ladders when..." (l.254) and "Biggest breath the earth's going to take around here for ten centuries" (l.328) are Fenn's present speech. "It sounded littler than I had expected, a number off a classroom wall" (l.308) is her present thought. The mountain at l.360 is in her eyeline, "low and blue with distance, the long green flank … with a small white cloud sitting on top of it". That is the voice-dna mountain rule exactly: it is green, it does nothing, and it is not named in narration. The reader's own knowledge of 79 does the work.
- **NO TICS:** the gates are clean (phrases, gestures). The hand findings are F1–F4 above. Fenn's syntax (and-chains, asking and refusing the answer) is his card, not a device.
- **Fenn never lists: holds.** "So I got the Greek, and I put the stars into Greek…" (l.186) is a chain, not an enumeration. "Who's president, I couldn't care less. The moon, forget the moon." (l.120) is two refusals. "My job's the blanket, yours is the umbrella" (l.444) is a pair.
- **Retired reflexes:** significance-tagging 0. Negation openers 0 in narration ("I don't mean I slipped. The floor tipped." is Fenn's speech). Anaphora triads 0: "He said it like… / He said it in…" (l.58) is a designed pair, and "Maybe… / Maybe…" (l.348) is Mara's speech. Performed candour 0 ("I mean it." at l.120 is emphasis in a refusal). Device as scene button 0 (the lighter, basil, notebook and coppers are all settled before the close). Closing aphorism 0.
- **No spoken line reused:** the echo scan finds 0 spoken-line echoes. "A bus" twice (l.388) is one designed beat.
- **Closed / spent lists:**
  - Mara's laugh: the outline's NON-NEGOTIABLE is the ruling the bible asked for. The shape is new (laugh and tears fused into one fight for breath while her hands save the papyrus). No mouth, shoulders, bench, heels, "without me" or "sound I made" (WARN-02 repair verified).
  - Who-pays / "Whose …?" 0 ("He did not ask whose." is narration, not the question frame). "by degrees" 0. Backlit doorway 0. Wall-turn close 0. Work residue 0. His hand on her belly / the heel 0. Singing walk-on 0.
  - Sample-09's collapse frame ("knees going, then sitting") is RESERVED for this chapter and is used in fresh words ("The client's stool caught me, which was luck, because my legs had gone.").
  - **Rebuilt:** Ch.22's stapled pot (l.34 → F8) and Ch.24's "[X] told [object]" (l.46 → F9).
- **"Vesuvius": 1**, in Fenn's mouth only ("Vesuvius blows its top", l.328). **"Margaret": 0.**
- **Allowlisted promise: 1** ("It takes back the one it brought. It brought you, so it'll take you.", l.264). **"one door with many mouths": 1 on the page** (l.264; the second grep hit is the header comment).
- **"Jesus H. Christ": 1** (its only use). **"Late summer, seventy-nine.": 1** of 2 verbatim. **"breathe with the earth": 1** of 2.
- **Valens learns no date, rules or location:** the date, the law, Eros's tomb, the failed dates and "Pompeii's" all pass in English. Fenn's Greek to Valens is courtesy, the boy's stars and the basil. The repair removed "Nuceria Gate" from the English (WARN-01). Valens's own "Does he know the door?" shows only what he already knew (Ch.15). *Hostile note, no action:* "Vesuvius" and "Pompeii" are proper names a Campanian could catch inside a foreign sentence. That is a word, not knowledge, and Ch.37–38 own the telling.
- **Margaret / ARCH-17:** "estate sale … In Chestnut Hill" → "He did not ask whose." → the hand held down → the 23 → "Keep it. I know what's in it." / "Kid, I wrote it." Mara has the name ("I had the name.", l.382) and does not say it. Ch.35 is protected.
- **Memory rule (CP2-2):** Pat (triggered by "wooder", l.192), the parade (in speech, l.130) and the Connie Mack lot (triggered by his question, l.446) are all short and all return to the room. No longer memory (Ch.24 had Dunphy).
- **CP4-1:** the child's status is never raised.

---

## CVI-Launch Breakdown (Commercial Assessment)
| Input | Score | Evidence |
|-------|-------|----------|
| Commercial Pacing | 8/10 | The lighter at about 600 words in, the WHEN at about 2,300, short turns in the argument, and a 7-word stop. The l.186–236 middle is the only drag. |
| Tomorrow Test | 4+ anchors → 10 | IMAGE: an old man in a Chaldean's robe with a brass lighter in his fist saying "Jesus H. Christ" in a Philadelphia accent; her hands holding the papyrus up and away from her own tears; Fenn turning his stool to the wall while she nurses; the packed bag under its dust; Valens turning the basil. QUOTE: "Late summer, seventy-nine."; "You don't go buying furniture in a hotel."; "He did not ask whose."; "Kid, I wrote it."; "Will they be true?" / "They will be in good Greek, … and very handsome." |
| Casual Reader | 9/10 | see report |
| Shareability (quote / plot / emotional) | 4 / 5 / 4 → 8 / 10 / 8 | MAX 10 × 0.6 + AVG 8.67 × 0.4 = **9.47** |
| Concept Pitch | yes → 10 | "She finds the man whose map she followed: a Philadelphian marooned since 1968, now a Roman astrologer, who has waited thirty-four years for the door that opens the night Vesuvius erupts." |
| Human Closeness | yes → 10 | It is all one room of people: two exiles, a husband, a baby. |

**CVI-Launch** = 8×.2 + 10×.2 + 9×.2 + 9.47×.2 + 10×.1 + 10×.1 = **9.29**, + 0.5 strong anchor = **9.79 → 9.8**.

**CVI-Legacy (default weights, empathy primary):** Originality 9.0×.30 + Theme 9.0×.25 + Cultural vocabulary 3×.20 ("Augurinus" and "late summer, seventy-nine" could become fandom shorthand; niche) + Re-readability 8×.15 (the Phillies cigar box from Ch.1 behind "in a cigar box"; the 23 running to Chestnut Hill; "Marry them and then go home on them"; "the column come out twelve" against Ch.36's matching figures) + Identity 5×.10 = 2.70 + 2.25 + 0.60 + 1.20 + 0.50 = **7.25 → 7.3**.

---

## Anti-AI Scan (20 Patterns), 7,499 words
1. Forced symmetry: Clear in narration ("Cold paint at night and warm paint in the day" is Fenn's speech).
2. Empty poetic vocabulary: Clear.
3. Automatic rule of three: Found, 1 (0.13/1k, minor). "brine, pine tar and the wet straw" (l.8) is a sensory opener triad. "Pots, lamps, now and then a bronze" (l.412) is broken by design.
4. Em dashes: Clear (3, all interruptions in speech).
5. Empty metaphors: Clear. "The walls had the sky on them." (l.32) is concrete.
6. Dramatic "And" openings: Clear in narration. Fenn's "And Mauch…", "And it was shut.", "And look at Delphi…" are his card's and-chains.
7. Pseudo-philosophical closings: Clear. "That's a lousy thing to do to a person." and "this one's got the end of the world behind it" are character speech in scene and do not end paragraphs of narration.
8. Excessive parallelism: Found, 1 (minor). "He said it like… He said it in…" (l.58) is a designed pair and stays.
9. Overly smooth transitions: Clear. Time moves in the scene ("The shakes ran on till the shadows had moved.", "The window's light had gone from white to gold").
10. Described emotions: Found, 3 (0.4/1k, minor): "honestly surprised" (l.234), "which seemed to offend him" (l.304), "at a loss" (l.442). Light and voice-true.
11. Explanatory extension: Found, 4 (0.53/1k, under the 0.8 cap): l.58 "with the vowels in his nose and the last word bitten off short"; l.80 "as he halted in any doorway to learn a room before entering it"; l.192 "with a d in the middle of it and the vowel pulled out long"; l.354 "…and that was the worst of it". Two of them are the accent, which is the anchor's content. No action.
12. Binary negation opener: Clear in narration.
13. Precision flex: Clear. Fenn's numbers are his pattern-mind (card); "eleven mule-loads" is Valens's trade.
14. Emotional control demonstration: Found, 1 (minor). "I brought my eyes back to the room." (l.360) is a managed beat, but the argument around it fails out loud (l.344), so this is not the pattern's "always successfully".
15. Authoritative description: Clear. Gaps are left: "the other thing" (the tears unnamed), "a jar of something", "He saw something in my face, I suppose".
16. Philosophical asides: Clear in narration.
17. Clean dialogue: Clear. Cut-offs (l.154, 340/342, 396/398), talking across her (l.186), Lucius objecting and nobody attending, a refused answer (l.124).
18. Thematic echo chamber: Found, 1 (minor). The bag / satchel-hand / hotel / widow / basil cluster (l.230–236). Each is earned and texture dominates.
19. Graduated reveal: Clear. The reveal is front-loaded (the WHEN at about 30% of the chapter), and the back half is argument and grief.
20. Emotional temperature report: Found, 1 (minor). Fenn's tremor notes at intervals (l.38, 328, 382, 394). F2 removes one.

**Total: 7 / 20 patterns found, all minor or moderate. Commercial band: CLEAN (0–8).** #11 is under the hard cap.

---

## Character Chaos Check (Primary: Mara)
- **Irrelevant thought:** present, inhabited. Pat hosing her steps "even the evenings it rained" (l.192), triggered by "wooder" and returning to "Please."; the smudged moon her palm printed in his ink (l.164), which she looks at instead of at the date.
- **Cognitive distortion:** present, inhabited. She accuses him of fitting the sum to the answer ("Tell somebody the answer's twelve and they'll make the column come out twelve", l.340) while doing the same thing herself, and her hope for "next spring" (l.348) is the tell.
- **Unprompted memory:** present, triggered: the Connie Mack lot from the car on Lehigh Avenue (l.446), out of his question and back into her silence.
- **Failed emotional management:** present. The collapse (l.60), "Ow … set me off again" (l.66), and the voice she "could not bring … down" (l.344).
- **Voice under pressure:** demonstrated. The collapse is one breath-starved sentence of body; in the argument her lines shorten and repeat ("You don't know."). This is a level-1/2 chapter; the level-3 rehearsal was Ch.24.

## Secondary Character Chaos
- **Fenn:** own moments, several. The automat pie "a little damp, like it had been crying"; the wine he finishes because he paid for it; the stool turned to the wall; the bus.
- **Valens:** own moment, the basil ("It was reaching," … "Turn it every few days. Water it less.") and "Will they be true?"
- **Lucius:** own moment, the sand tasted and spat "with deep suspicion".
- **Walk-ons** (the sea captain, the ship's boy) are texture with their own errands.
- No secondary character functions only as a prop.

## The Tomorrow Test
**What the reader remembers:** an old man in a faded blue Chaldean's robe, patting himself down for a lost lighter and muttering in English, then swinging round with the lighter in his fist and saying "Jesus H. Christ" like a man on a Philadelphia stoop, and the heroine laughing until she weeps because the first English anyone has said to her in five years was "thanks". And, quieter: "He did not ask whose."
**Anchor type:** BOTH (image: the lighter and the robe; quote: "Late summer, seventy-nine." / "You don't go buying furniture in a hotel.").
**Verdict:** ANCHOR EXISTS. It is the outline's anchor, delivered. It is auditory and comic, so it is not the same type as Ch.24's gestural jar-lift.

**Shareability:** "The guy who sold her the map isn't dead. He's been a Roman fortune-teller for thirty-four years, and the first thing he says is 'Jesus H. Christ.'" That works as a text to a friend. This is the book's shareable moment #4, as planned.

---

## Reader Reports

### The Devourer
Accelerates from "It was a cigarette lighter." and does not stop until "What?" Skims the mooring-rings speech (l.210) and the bathhouse pool, and comes back for the nursing and the stool turned to the wall. The argument (l.336–358) reads at sprint speed. Turns to Ch.26 for the letters and because everyone knows 79 is right. Would not put the book down here.

### The Critic
Underlines "I laughed because he had said thanks.", the smudged moon, "He did not ask whose.", "I watched him not ask", "a bus", the honey "as an apology", and the close's two withholdings. Admires that Valens's belief is a colour climbing a neck and a mouth pressed to a child's head, and nothing said. Is mildly disappointed by four things. Valens is parked at a "post" so often that he becomes a sentry rather than a man. Fenn's hand trembles on cue. The narration keeps telling us he is "off again" when the speeches already show it. And the hotel/widow/bag/basil cluster sits close together.

### The Hostile
- l.236: Valens "came two steps inside" to reach the sill, but the sill is under the window "down the room" (l.218, 390), where Mara sits at the table. (F1a)
- l.246: Fenn "swiveled on the table", but since l.218 and l.234 he has been on the stool, turned to the wall and back. (F5)
- l.34: a second lead-stapled pot, after Ch.1's platter and Ch.22's "Whoever stapled it…". (F8)
- l.372: the satchel holds "everything that had crossed with me", but the watch is on her wrist (entity tracker CH25-7). (F11)
- Checked and cleared:
  - "thirty years" (1968→1998) and "thirty-four years" (AD 41→75) are correct.
  - "eleven years" of Kalends marks and of the basil agree.
  - "five years" since her crossing is a round figure in a fit (INFO-06).
  - The 23 became a bus in 1992 ("a few years ago" in 1998).
  - Claudius found behind a curtain, his nephew knifed "that winter" (January 41).
  - Navy celestial navigation in 1952 at 18.
  - Ch.1 has Szabo name "Margaret Fenn" and a Phillies cigar box, which agrees with "I had the name" and "in a cigar box".
  - Ch.14 has her knowing 79 already, which agrees with "and so have you" (l.328).
  - Phocis/Amphissa is regionally loose but defensible in Fenn's mouth.

### The Casual Reader (9.0)
Buys, if they have not already. A fish market with gulls standing in blood, a rickety stair, and a fortune-teller who mutters "Where the hell'd you get to" at his lighter: they laugh out loud and then cry with her. They love Fenn at once, the man who won't be told whether we got to the moon, and they feel his face when she says "estate sale". They are a little bored by the tide-marks on the quay wall, and are rescued by a baby eating astrology. The last line makes them say "oh no, she's wrong," which is exactly the feeling that sells the next 19 chapters.

### The Devoted Reader (active: long saga, Outlander readership)
Will connect the Phillies cigar box in Ch.1 to "in a cigar box"; the 23 running up Germantown Avenue to Chestnut Hill, where his sister died; the umbrella joke and its return ("My job's the blanket, yours is the umbrella"); "Marry them and then go home on them" against Mara's whole marriage; and "the column come out twelve" against Ch.36. Will write the Reddit post about "Augurinus". Will also notice Valens at his "post" every few paragraphs. Adopts the chapter; it is the one they quote first.

## Cross-Reader Matrix
| Issue | Devourer | Critic | Hostile | Casual | Devoted | Severity |
|---|---|---|---|---|---|---|
| Valens's doorway "post" ×6 (sentry state) | | ✓ | | | ✓ | SHOULD FIX (hand rule) → F1 |
| Fenn's tremor ×4 / "off/away again" ×2 / turns ×7 | | ✓ | ✓ | | | SHOULD FIX (hand rule) → F2–F4 |
| Blocking: Valens "two steps" to a far sill; Fenn "on the table" while on the stool | | | ✓ | | ✓ | SHOULD FIX (logic) → F1a, F5 |
| Sample-09 lifts ("in a Chaldean's robe"; "Ninety-eight. Nineteen ninety-eight.") | | ✓ | | | | INVESTIGATE (law: samples 0) → F6, F7 |
| Ch.22's stapled pot rebuilt | | ✓ | ✓ | | ✓ | IMPORTANT (law: SPENT) → F8 |
| "he told it" after Ch.24's "Statia told the door" | | ✓ | | | | INVESTIGATE → F9 |
| Narration "breath" against Fenn's law-word | | ✓ | | | | INVESTIGATE → F10 |
| Satchel "everything" vs the watch on her wrist | | | ✓ | | ✓ | SHOULD FIX (continuity, CH25-7) → F11 |
| l.186–236 middle slow (mooring rings) | ✓ | | | ✓ | | SHOULD FIX in principle; **no action** at cycle 0 (it is the lonely-host subtext and the fascination engine; cutting it would cost the ship's boy and the nursing beat) |
| Mirror-object cluster l.230–236 | | ✓ | | | | INVESTIGATE (no action) |

---

## Revision Recommendations (Ranked)

| # | Location | Problem type | What happens now | Why it fails | Revision direction | Project rule? |
|---|---|---|---|---|---|---|
| F1a | l.236 | Logic + Character (sentry state) | "At some point Valens came two steps inside, saying nothing, took the cracked basil pot off the sill" | The sill is down the room (l.218 "carried him down the room", l.390 "watched Fenn down the room"), not two steps from the door. "Two steps inside" also keeps him pinned to the doorway. | → "At some point Valens passed behind my stool, saying nothing, took the basil pot off the sill" | No |
| F1b | l.236 | Character (sentry state) | "…faced the room, and returned to his post." | "post" labels a state already noted at l.80 (and again at 274, 298, 390, 428). | → "…faced the room, and left it." | **Yes:** a character's standing station in a single-scene chapter gets ≤3 narrated notes, and never a label ("post", "place", "station"). |
| F1c | l.274 | Character (sentry state) | "and Valens came a pace off his post." | The second "post". | → "and Valens started forward." | (F1b rule) |
| F1d | l.298 | Character (sentry state) | "he took up his place in the door again with the child roaring against his neck." | The fourth return-to-station note. | → "he carried the roaring child out of reach of the tray." ("He stood rocking there" follows unchanged.) | (F1b rule) |
| F2 | l.328 | Character (narrated state, 4th tremor note) | "He opened his hands, the tremor in the left one making it look as though he were shaking dice." | The tremor is noted at l.38, 382 and 394, and the l.382/394 pair is the Margaret beat. A fourth note between them makes the hand tremble on cue, and "dice" is Grata's husband's Ch.24 prop. | → "He opened his hands." | No |
| F3 | l.264 | Character (narrated state) | '…with a god in a hole in the ground." He was away again. "Here's how I figure it,' | "He was off again" (l.186) and "He was away again" are the same frame. The speech shows the runaway; the narration does not need to label it a second time. | → one quotation: '…with a god in a hole in the ground. Here's how I figure it,' | No |
| F4 | l.82 | Character (gesture class) | '"Husband," said the Chaldean, and swung round to the doorway at last,' | "swung round" verbatim at l.54, and l.90 "turning round" follows 151 words later. Fenn's turn class runs to 7. | → "and looked to the doorway at last," (keeps the card's "sees people last") | No |
| F5 | l.246 | Logic (blocking) + gesture class | "He swiveled on the table toward Valens, who looked back." | He has been on the stool since l.218 ("turned his stool round") and l.234 ("Round he came on the stool"), and l.270 and l.368 need him on the table. | → "He left the stool for his table, facing Valens, who looked back." | No |
| F8 | l.34 | Style (SPENT object) | "On the sill, in a pot mended with a lead staple, a basil" | Ch.22 SPENT "the pot with lead staples", and Ch.1 has Szabo's stapled platter. A third staple-mended vessel turns the conservator's eye into a device. An unmended pot also suits a man who never furnished his room. | → "On the sill, in a chipped pot, a basil" (F1a drops "cracked" at l.236 to match) | **Yes:** the lead staple is SPENT as Mara's mend-notice; her eye finds a different repair or none. |
| F6 | l.58 | Style (voice-bank sample) | "He said it in a Chaldean's robe, with the harbor of Puteoli at his back." | Sample-09: "an old man in a Chaldean's robe with a Philadelphia flatness to the vowels", which is also the outline's anchor plan sentence. Samples are calibration only, with 0 uses. | → "He said it dressed as a Chaldean, with the harbor of Puteoli at his back." | No |
| F7 | l.96, l.98 | Style (voice-bank sample) | "In May. May of ninety-eight. Nineteen ninety-eight." / "He repeated it without the nineteen, slowly," | Sample-09's "Ninety-eight." / "Nineteen ninety-eight." exchange, inverted. | → "In May. May of ninety-eight. Our ninety-eight." / "He repeated it slowly," | No |
| F9 | l.46 | Style (frame repeat) | '"Where the hell'd you get to," he told it.' | Ch.24's "Statia told the door" (talking-to-objects WATCH, 1 used) is rebuilt one chapter later. l.44 already ends "and muttered", so the tag is redundant, and the bare line lets the English hit cold. | → '"Where the hell'd you get to?"' | No |
| F10 | l.232 | Style (diluting the law-word) | '"Did you ever get married?" I asked, at his next pause for breath.' | "breathe" is Fenn's doors-law word (6 uses in his mouth). The narration's idiomatic "breath" (l.60, 108, 232) thins it. | → "…I asked, at his next pause." | No |
| F11 | l.372 | Continuity (entity tracker CH25-7) | "holding everything that had crossed with me through the cave," | The watch also crossed and is on her wrist (Ch.24 close). | → "holding everything else that had crossed with me through the cave," | No |

### Fix order: Logic/Character (F1a–d, F5, F2, F3, F4) → Continuity (F11) → Prose (F8, F6, F7, F9, F10).

### TESTED FIX SCRIPT
`/tmp/claude-0/-home-user/63791ee5-159c-5791-9429-07920f8d9417/scratchpad/fixes25/apply_fixes.py <path/to/chapter-25.md>` holds 15 exact replacements (F1a–d, F2, F3, F4, F5, F6, F7a–b, F8, F9, F10, F11). Each old string must occur exactly once, or the script aborts and writes nothing. A second run aborts.

Tested on a scratch copy of the book folder (`/tmp/claude-0/-home-user/63791ee5-159c-5791-9429-07920f8d9417/scratchpad/eval25/`), starting from the current page (md5 `9fe39d86…`):
- All 15 applied once. The re-run aborted with 0 matches (exit 1). Patched md5 `64f3e4ff52d8eb3221e0ba5771ad29ca`.
- `bash tools/check_chapter.sh 25`: **ALL MECHANICAL GATES CLEAN** (the tic gate's auto-recurrence is clean). The shape audit was run separately from the repo root on the scratch folder: Ch.25 `scene-set` / `punch`, **SHAPE CLEAN**.
- `python3 tools/tic_report.py --echoes 25`: **0 / 0 / 0**.
- Dialogue **49.5%** (band 45–55). 7,458 words (shape), median 11.
- **The first drafts of F1a, F1d and F5 failed the gates and were replaced before the final run.** "came down the room" / "went back up the room" / "hitched himself back onto the table" tripped 3+ book-wide recurrences ("came down the", "back up the", "he went back", "back onto the", "down the room"). "walked the length of" / "to the far end" / "himself up on" were cross-chapter echoes. None of them is in the script.
- **Checks on every new string:**
  - Grepped against Ch.1–24, voice-bank samples 01–13, outline/foundation/voice-dna and the bible: "passed behind my stool", "and left it", "started forward", "out of reach of the tray", "He opened his hands.", "looked to the doorway", "left the stool for his table, facing Valens", "dressed as a Chaldean", "Our ninety-eight", "chipped pot", "hell'd you get to?", "everything else that had crossed". No prior-chapter or sample hit. The only hit is the trivial "a pause." in sample-06 against "at his next pause."
  - Nothing an earlier pass cut is restored (checked against the dialogue / disruption / repair logs): no "without me", no "pink to the collar", no "nobody had disturbed", no second "Give or take", no two-finger gesture, no "front steps", no "schoolmaster's" at l.84.
  - No closed-list item is used: no laugh, mouth, heel, who-pays, "by degrees", backlit doorway, wall-turn or "Nobody had".
  - The F1b rule leaves Valens's arrival (l.68–80), the sleeping-child stillness (l.390) and "Valens stirred in the doorway" (l.428) as his three station notes.

## Strengths to PRESERVE
- **The recognition sequence, word for word:** the room inventory slowing to "It was a cigarette lighter." → the pat-down → "It's on the sill, by the basil," → "Thanks," → the lighter in his fist → "Jesus H. Christ" with the block, the Eagles and the radio. Do not add a reaction sentence between them.
- **The collapse paragraph** (l.60) as repaired: the fused laugh and tears, "I laughed because he had said thanks.", and the hands that save the papyrus. Do not lengthen it or name "the other thing".
- **Valens's flush** (l.80): the colour climbing, the mouth pressed to Lucius's head, "Lucius objected, and nobody attended to him." Nobody says he believes. Never add it.
- **The WHEN as an afterthought of joy** (l.156) and the cutaway "Down on the quay a man was crying sprats. The gulls went over."
- **The estate-sale silence** (l.378–388): "He did not ask whose." / the hand held down / "I had the name." / the 23 / "A bus." Every beat is load-bearing. Mara never says the name.
- **The widow line** (l.234), the stool turned to the wall, the ship's boy's "Dawn is propitious", the basil and Valens's "Turn it every few days. Water it less."
- **"Will they be true?" / "They will be in good Greek, … and very handsome."**
- **The close:** Connie Mack withheld ("I kept the fire to myself."), then the 7-word refusal. No added beat, no reaction, no image after it.

## PATH TO 8.5 (Floor 8.0 → 8.5)
- **Characters 8.0 → 8.5 requires:** every narrated state at ≤3 notes, and no label turning blocking into a station. **Surgery:**
  - F1a–d bring Valens's post from 6 notes to 3, with "post" ×0 (F1a also fixes the far-sill logic).
  - F2 brings Fenn's tremor from 4 to 3.
  - F3 brings "[off/away] again" from 2 to 1.
  - F4 and F5 bring Fenn's turns from 7 to 5, with "swung round" ×1 (F5 also fixes the stool/table blocking).
  - Everything else on this dimension already earns 9.0: Fenn's bilingual voice, chaos 4/4 inhabited for Mara, every secondary with an independent moment, and Valens's belief shown and never declared.
- **No other dimension is below 8.5.** F6–F11 are hygiene that protects Prose 8.5 (zero sample lifts, zero spent objects) and Immersion 9.0 (the room's blocking holds).
- **Projected after F1–F11:** Originality 9.0 · Theme 9.0 · Characters 8.5 (+0.5, the per-cycle cap) · Prose 8.5 · Pacing 8.5 · Emotion 9.0 · Immersion 9.0 → **Floor 8.5 / Average 8.79 / Casual 9.0 / CVI-Launch 9.8 / CVI-Legacy 7.3**. To be confirmed by re-evaluating the patched page.

## Bookkeeping for finalize (not evaluator edits)
- **FENN card, "Ch.25 as written":**
  - "the rich men's boys who throw figs" (the walk-on block) → the page says "olive pits".
  - "tremor (3 notes: on the table, 'shaking dice', held down)" → after F2: on the table, held down, the hand that stays.
  - Add "Holy smoke" and "chump" (not in the pool; ≤2).
  - Add the ship's-boy exchange to SPENT.
  - Turns: "looked to the doorway at last".
- **MARA mentions:** Pat "hosing down her steps every evening all summer, even the evenings it rained" (not "her own hose's spray"). Mara's sixth laugh shape (fused with tears, the papyrus held clear) is SPENT.
- **New at-risk / closed:**
  - The lead staple is SPENT as Mara's mend-notice (F8 rule).
  - The F1b station rule.
  - "Get out" rests in Ch.26–27; Fenn's "nobody … but me" stays at 2.
  - "[X] told [object]" is at 1 per two chapters.
  - CUT strings (never restore): every old string in F1–F11.
- Header comment l.6: re-sync the counts after the fixes (7,458 shape / dialogue 49.5%).
- **Ch.26:** median 14+ to break the 23–25 low-median run. Its hook must not be SENSORY and its pull must not be DECISION POINT (hook-craft chain). Its 1964 material is new (WARN-18 cascade).

## VERDICT
**POLISH.** Genesis Floor 8.0 (Characters) < 8.5; Casual 9.0 ✓; pacing OK ✓; mechanical gates clean ✓. Apply the tested script (F1–F11) and re-evaluate. Nothing structural, and no beat to rewrite: this is the strongest chapter of Part Two, held below the gate only by stage notes repeated past the hand rule.

BIAS CHECK: This evaluation was produced by the same system that wrote the prose. Confidence in scores above 8.0 requires external validation (beta readers, editors, comp analysis).

---

## Re-evaluation — cycle 1
**Evaluator:** book-evaluator (independent) | **Date:** 2026-10-23 | **Text:** `chapter-25.md` md5 `64f3e4ff52d8eb3221e0ba5771ad29ca` (cycle-0 set F1–F11 applied)

### Verification of the cycle-0 set
- **All 15 replacements landed once:** every old string is at 0, and every new string is at 1 on the page.
- **Gates on the real file:**
  - `check_chapter.sh 25`: ALL MECHANICAL GATES CLEAN, SHAPE CLEAN (`scene-set` / `punch`).
  - `tic_report.py --gate`: clean. Ch.25 gesture layer: 'a (long) moment' 2, shrug 1.
  - `--echoes 25`: 0 / 0 / 0.
  - Metrics: 7,460 words (metaphor row), median 11, mean 16.1, 5.6% of sentences over 40 words, simile 19.
- **Cut effects:** none restored. "post", "two steps inside", "swung round to the doorway", "away again", "shaking dice", "lead staple", "in a Chaldean's robe" (page), "Nineteen ninety-eight.", "he told it" and "pause for breath" are all at 0.
- **Sample-09:** no lifts remain on the page. The "five years / first English" idea is the reserved frame in fresh words, as ruled at cycle 0. "Late summer, seventy-nine." is the planned verbatim WHEN, 1 of 2.
- **Closed/spent frames:** no new hits from F1–F11.
- **What the set planted.** F1b "turned it so that the leggy side faced the room, **and left it**" has two problems:
  - *it* takes "the room" as its nearest antecedent, so the clause reads first as Valens leaving the room, and two paragraphs later he is still in it.
  - It rebuilds Valens's Ch.20 l.573 "weighed it **and left it**". The echo scan is too short to catch this. → **G3**

### Narrated-trait hand counts (redone; spec: >3 notes of one state, or 3 inside ~500 words, fails)
| Character | Item | Lines (current page) | Count | Verdict |
|---|---|---|---|---|
| Valens | doorway station | 80, 390, 428 | 3, with "post"/"place" ×0 | ✓ (F1 landed) |
| Valens | looks back at Fenn | 246, 304 | 2 | OK |
| Valens | watches | 80, 390 | 2 | OK |
| Valens | "and left it" | 236 (+ Ch.20 l.573) | ambiguity plus a cross-chapter rebuild | **G3** |
| Fenn | left-hand tremor | 38, 382, 394 | 3 | ✓ (F2 landed). "good hand" 102/426 and "bad hand" 382 are identifiers, not tremor notes: WATCH, ≤1 per chapter from Ch.26 |
| Fenn | **talks on regardless (narrated)** | 186 "off again", **218 "went on at the wall about the bathhouse keeper's pool", 228 "was in the bathhouse keeper's pool again", 236 "talked straight through it"** | **4, and 3 inside ~425 words (218→236)**, with "the bathhouse keeper's pool" verbatim in narration 182 words apart | **FAILS.** Cycle 0 missed l.218. → **G1, G2** |
| Fenn | turns (stool, round, to the wall) | 54, 90, 218, 234, **290**, **414**, 432 | **7** (cycle 0 missed 290 "then turned to me" and 414 "faced the wall again"); "swung round" ×1; no 3 inside 500 words | 0.94/1k, at the long-chapter cap. Cut the one unmotivated turn → **G5** (6) |
| Fenn | lighter handled | 52, 168, 234, 260 | 4, spread | OK (card object, never lit) |
| Fenn | hurries | 210 | 1 | OK (the lonely-host tell) |
| Mara | words escape her | 308 "The number escaped me unchecked", 378 "could not unsay them" | 2 (l.48 is reception, not escape) | OK. WATCH for the book (cf. Ch.7 l.334; the gate tracks 'before I decided'): ≤1 in Ch.26 |
| Mara | voice out of control | 344 | 1 | OK |
| Mara | looks away / at | 164, 360 | 2 | OK |
| Mara | satchel | 230, 372, 400 | 3, spread over 170 lines | OK |
| Mara | legs gone / legs held | 60 / 442 | designed pair | OK |
| Lucius | **adult indignation lent to the baby** | **14 "glared", 80 "objected", 218 "grunt of grievance", 236 "cross about it", 278 "deep suspicion"** | **5** | **FAILS** (>3). Same device as Ch.24's "hated it and said so" / "furious", now a narrator habit. Keep the three the cycle-0 eval preserves (80, 218, 278) → **G4a, G4b** |
| Lucius | crying / fury (events) | 212, 292–298 | 2 | OK: these are things that happen, not labels |

### Re-scored Genesis (max ±0.5 per dimension)
| Dimension | Cycle 0 | **Cycle 1** | Basis |
|---|---|---|---|
| Originality | 9.0 | **9.0** | unchanged; no beat touched |
| Theme | 9.0 | **9.0** | unchanged |
| Characters | 8.0 | **8.0** | Three of cycle 0's four cap reasons are cleared: Valens 6→3, tremor 4→3, "swung round" ×1 with the blocking fixed. **The cap still applies on the corrected count:** Fenn's narrated talk-on is 4, with 3 inside ~425 words (l.218/228/236), and Lucius's lent indignation is 5. Also, the turn class was undercounted at cycle 0 (7, not 5). Uncapped value stays 9.0. |
| Prose & Voice | 8.5 | **8.5** | F6–F10 landed: sample lifts 0, SPENT staple gone, "he told it" gone, and the law-word is Fenn's alone in that passage. The F1b ambiguity is a slip, not a cap. Stopping sentence intact (l.60). |
| Pacing | 8.5 | **8.5** | dialogue 49.5–50% in band; length 89% of target; value shift ×2; the l.186–236 middle is unchanged. **PACING: OK.** |
| Emotion | 9.0 | **9.0** | unchanged; anchor, body rebel, surprise intact |
| Immersion | 9.0 | **9.0** | both blocking slips fixed (F1a far sill, F5 stool/table). G3 removes the last ambiguity in the room. |
| **FLOOR / AVERAGE** | 8.0 / 8.71 | **8.0 / 8.71** | Characters |

**Casual Reader 9.0** (unchanged: the lighter, "Thanks," and the bus all hold). **CVI-Launch 9.8** (9.29 + 0.5 anchor). **CVI-Legacy 7.3.** Anti-AI 7/20, all minor, CLEAN. #11 at 4 (0.54/1k), under cap. Divergence: Launch 9.8 vs Floor 8.0 = 1.8.

### Cycle-1 fixes (TESTED)
`/tmp/claude-0/-home-user/63791ee5-159c-5791-9429-07920f8d9417/scratchpad/fixes25b/apply_fixes.py <path/to/chapter-25.md>` holds 8 exact replacements. Each old string must occur exactly once or the script aborts and writes nothing; a second run aborts.

| # | Location | Type | Now | Revision |
|---|---|---|---|---|
| G1 | l.236 | Character (narrated state) | "Fenn talked straight through it, and then abandoned the shakes in mid-run" | → "Fenn abandoned the shakes in mid-run". Mara's "While you were telling me about the ground" (l.420) and "Who moved my basil?" carry the payoff. |
| G2 | l.218 | Character + Style (verbatim narration) | "and went on at the wall about the bathhouse keeper's pool, a little louder than before." | → "and went on at the wall, louder than before." (The first draft, "…wall, a little louder…", tripped a Ch.16 echo "wall a little" and is not in the script.) l.228's "in the bathhouse keeper's pool again" stays as the single narrated use. |
| G3 | l.236 | Logic + Continuity (planted by F1b) | "…where the sun lay full, turned it so that the leggy side faced the room, and left it." | → "…where the sun lay full, and turned it so that the leggy side faced the room." |
| G4a | l.14 | Character (lent indignation) | "and at eight months Lucius glared at the gulls." | → "and at eight months Lucius was busy with the gulls." (The first draft, "Lucius, eight months old", echoed the outline dateline and is not in the script.) |
| G4b | l.236 | Character (lent indignation) | "Lucius, fed and drowsy and cross about it, was handed" | → "Lucius, fed and drowsy, was handed" |
| G5 | l.290 | Character (turn class) | "He watched Lucius a while longer, then turned to me." | → "He watched Lucius a while longer." (the next line goes to her without the turn) |
| H1/H2 | l.6 header | bookkeeping | stale figures, and the comment quotes sample-09's "in a Chaldean's robe" | re-synced to the patched page |

**Test** (scratch copy `/tmp/claude-0/-home-user/63791ee5-159c-5791-9429-07920f8d9417/scratchpad/rt25c1/books/the-hour-of-ash`, starting from md5 `64f3e4ff…`):
- 8 applied; the re-run aborts (exit 1). Patched md5 **`b48ee45ffd9c66ae10c545431295bb4c`**.
- `check_chapter.sh 25`: **ALL MECHANICAL GATES CLEAN**, SHAPE CLEAN (`scene-set` / `punch`). `--gate` clean. `--echoes 25`: 0 / 0 / 0.
- Metrics: 7,438 words (shape), dialogue 49.7–50%, median 11.
- Every new string was grepped against Ch.1–24, samples 01–13, outline/foundation/voice-dna and the bible ("busy with the gulls", "fed and drowsy, was", "louder than before", "Fenn abandoned", "watched Lucius a while", "leggy side faced the room."). There are no hits outside Ch.25 itself.
- No cut string is restored. No closed-list item is used.

**After G1–G5:** Valens station 3; Fenn talk-on 3 (186/218/228, never 3 in 500); Fenn turns 6; Lucius lent indignation 3. **Projected:** Characters 8.5 (+0.5) → **Floor 8.5 / Average 8.79 / Casual 9.0 / CVI-Launch 9.8 / CVI-Legacy 7.3**, to be confirmed on the patched page.

### Bookkeeping to carry into finalize (in addition to the cycle-0 list)
- LUCIUS card, Ch.25: the "deep offense he kept for anything that moved…" quote is stale (the repair changed it to "glared"; after G4a it is "was busy with the gulls"). Drop "cross about it". SPENT: lent adult indignation for the baby. Aelia (Ch.26) gets none of objected / grievance / suspicion.
- Ch.25 walk-on block: "the rich men's boys who throw figs" → "olive pits". Pat: "hosing down her steps every evening all summer, even the evenings it rained".
- CUT (never restore): every old string in G1–G5, plus F1b's "and left it".

## VERDICT (cycle 1)
**POLISH.** Genesis Floor 8.0 (Characters) < 8.5. Casual 9.0 ✓; pacing OK ✓; gates clean ✓. F1–F11 landed and cleared three of the four cycle-0 cap reasons. On a full recount, Fenn's narrated talk-on (3 inside ~425 words) and Lucius's lent indignation (5) still break the hand rule, and F1b planted one ambiguity. Apply `fixes25b/apply_fixes.py` (tested) and re-evaluate. Nothing structural.

BIAS CHECK: This evaluation was produced by the same system that wrote the prose. Confidence in scores above 8.0 requires external validation (beta readers, editors, comp analysis).

---

## Re-evaluation — cycle 2
**Evaluator:** book-evaluator (independent) | **Date:** 2026-10-23 | **Text:** `chapter-25.md` md5 `b48ee45ffd9c66ae10c545431295bb4c` (cycle-1 set G1–G5, H1–H2 applied)

### Verification of the cycle-1 set
- **All 8 landed once.** Old strings at 0: "talked straight through", "a little louder than before", "and left it", "glared", "cross about it", "then turned to me". "bathhouse keeper's pool" is at 1 (l.228, the designed use). The header is re-synced and no longer quotes sample-09.
- **Gates on the real file:**
  - `check_chapter.sh 25`: ALL MECHANICAL GATES CLEAN, SHAPE CLEAN.
  - `tic_report.py --gate`: clean. Ch.25 gesture layer: 'a (long) moment' 2, shrug 1.
  - `--echoes 25`: 0 / 0 / 0.
  - Metrics: 7,438 words (metaphor row), dialogue 49.7%, median 11, mean 16.0, 5.4% of sentences over 40 words, simile 19.
- **Nothing planted by G1–G5:** no cut string is restored, no closed-list item is used, and no new string echoes another chapter.

### Narrated-trait hand counts: full recount, every recurring character, every state
Spec: more than 3 notes of one state fails, and so do 3 notes inside ~500 words. Positions are word offsets measured on the page.

| Character | State | Lines | Count / spacing | Verdict |
|---|---|---|---|---|
| Fenn | **talks on regardless (narrated)** | 186 "off again, talking across me" · 218 "went on at the wall, louder than before" · **224 "The shakes ran on till the shadows had moved"** · 228 "in the bathhouse keeper's pool again" · (236 "abandoned the shakes in mid-run" implies it too) | **4, with 218/224/228 inside ~180 words.** Cycles 0 and 1 both missed l.224. Its subject is "the shakes", but it narrates his talk running on. | **FAILS** → J1a |
| Fenn | **keeps to the wall** | 218 turns stool to the wall · 222 "and stayed as he was" · 224 "Fenn stayed facing his wall" | **3 inside ~110 words**, with "stayed" ×2 | **FAILS** → J1a (l.226 "the window behind him" carries the position) |
| Fenn | **breaks off mid-speech (narrated)** | 218 "broke off halfway into the hot springs" · 236 "abandoned the shakes in mid-run" · 254 "let that go, short of wherever it had been heading" · 268 "broke off and drank" | **4** (>3). l.254 and l.268 are the designed pair, the going-home sentences he cannot finish. | **FAILS** → J2 (l.236 is also the talk-on spill) |
| Fenn | **grief routed into a look at a thing** | 202 copper "went on looking at it" · 260 lighter "He looked at it and slid it away" · 374 notebook "He looked at it." · 382 "gazed past me at the bay" | **4**, with "He looked at it" verbatim twice, 110 lines apart | **FAILS** → J4 (l.374 is the designed one) |
| Fenn | turns / faces | 54 swung round · 90 turning round · 218 stool to wall · 234 "Round he came" · **246 "facing Valens"** · 414 "faced the wall again" · 432 "turning fast" | 7 (0.94/1k), with 218/234/246 inside ~525 words. Cycle 1 counted 6 and left out l.246. | borderline → J3 (6, none 3 in 500) |
| Fenn | looks away (harbor / ceiling / bay) | 98, 218, 382 | 3, spread | OK |
| Fenn | other looks (doorway at last, stared, eyes flicked, fixed me, the child "properly", weighed Valens, hands over, eye strayed, plant) | 82, 106, 210, 236, 282, 304, 414, 416, 426 | all different states, each motivated | OK |
| Fenn | left-hand tremor | 38, 382, 394 | 3 | OK ("good/bad hand" 82, 102, 382, 426 are identifiers, not notes) |
| Fenn | lighter handled | 52, 168, 234, 260 | 4 across 210 lines, never 3 in 400 words | OK (card object, never lit) |
| Fenn | laughs / grins / smiles | 106, 162 / 268 / 398 | 2 + 1 + 1 | OK |
| Fenn | bows | 84, 196 | 2 | OK |
| Fenn | slaps | 152, 402 | 2 | OK |
| Fenn | "showed me" | 174, 186 | 2 inside ~250 words | WATCH, no action |
| Fenn | look "… and back" | 98, 210 | 2 | WATCH |
| Fenn | still / quiet | 258, 260, 368 | 3 different beats | OK |
| Fenn | hurries | 210 | 1 | OK |
| Valens | doorway station | 80, 390, 428 (196 implied by the cup) | 3 | OK |
| Valens | **meets Fenn's eye** | 246 "who looked back" · 304 "Valens looked steadily back" · 434 "regarded him" | 3, with "looked back" ×2 | at the limit; J3 removes l.246 → 2 |
| Valens | finds me | 68 "found me", 212 "found my eyes" | 2 | OK |
| Valens | watches | 80, 390 | 2 | OK |
| Valens | "over the … head" | 212, 434 | 2 | WATCH |
| Valens | stillness / rocking | 298, 390 | 2 | OK |
| Lucius | lent adult indignation | 80 objected, 218 grievance, 278 suspicion | 3 | OK (G4 landed) |
| Lucius | lent adult scrutiny | 26 "which he studied", 278 "regarded" | 2 | OK |
| Lucius | crying / fury (events) | 212 "complain in earnest", 292 fury, 298 "a sort of complaint" | events, not labels; "complain" ×2 | WATCH |
| Mara | looks away / at | 164, 360 | 2 | OK |
| Mara | satchel | 230, 372, 400 | 3, spread | OK |
| Mara | words escape her | 308, 378 | 2 | OK (≤1 in Ch.26) |
| Mara | voice out of control | 344 | 1 | OK |
| Mara | legs gone / held | 60 / 442 | designed pair | OK |
| Cross-character | "Nobody knows" | Fenn 290, Mara 348 | 2 | INVESTIGATE, no action: she throws his phrase back at him in the argument |
| Narration | "weighed" | 278 (Lucius, the taste), 304 (Fenn, a look) | 2 | WATCH |

**Why this is not nit-picking.** The 218–236 stretch is the nursing comedy: Fenn turns to his wall and lectures it, and the narration is the only carrier because his speech is off the page. In ~420 words it notes him talking on 4 times, keeping to the wall 3 times and breaking off twice. The joke lands on the first note of each; the repeats are stage directions. The l.260/l.374 "He looked at it" pair makes the notebook beat, the chapter's best silence, read as a reprise of the lighter's.

### Re-scored Genesis (max ±0.5 per dimension)
| Dimension | Cycle 1 | **Cycle 2** | Basis |
|---|---|---|---|
| Originality | 9.0 | **9.0** | unchanged |
| Theme | 9.0 | **9.0** | unchanged |
| Characters | 8.0 | **8.0** | G1–G5 cleared cycle 1's two cap reasons (Lucius 5→3; talk-on as cycle 1 counted it). On the full recount the hand rule still fails 4 ways: talk-on (3 inside ~180 words), wall-keeping (3 inside ~110), break-offs (4) and object-looks (4). **Cap 8.0 holds.** Uncapped value 9.0. |
| Prose & Voice | 8.5 | **8.5** | stopping sentence l.60 intact; underlines intact; no sample lifts; no spent object |
| Pacing | 8.5 | **8.5** | dialogue 49.7% in band; 89% of target; value shift on two axes; the l.186–236 middle is unchanged. **PACING: OK.** |
| Emotion | 9.0 | **9.0** | anchor, body rebel and surprise intact |
| Immersion | 9.0 | **9.0** | blocking holds (stool/table/sill) |
| **FLOOR / AVERAGE** | 8.0 / 8.71 | **8.0 / 8.71** | Characters |

**Casual Reader 9.0** (unchanged). **CVI-Launch 9.8** (9.29 + 0.5 anchor). **CVI-Legacy 7.3.** Anti-AI 7/20, all minor, CLEAN; #11 at 4 (0.54/1k), under the cap. Divergence: 1.8.

### Cycle-2 fixes (TESTED)
`/tmp/claude-0/-home-user/63791ee5-159c-5791-9429-07920f8d9417/scratchpad/fixes25c/apply_fixes.py <path/to/chapter-25.md>` holds 6 exact replacements. Each old string must occur exactly once or the script aborts and writes nothing; a second run aborts.

| # | Location | Type | Now | Revision |
|---|---|---|---|---|
| J1a | l.224 | Character (talk-on, wall-keeping) | "The shakes ran on till the shadows had moved. Partway through them a boy bawled … ship's hour. Fenn stayed facing his wall." | → "The shadows on the floor had moved when a boy bawled at the window from the quay below; the broken tread had turned him back, and his master was asking after the ship's hour." |
| J1b | l.226 | Logic (antecedent) | '"Dawn is propitious," he called to the window behind him' | → "Fenn called" (with J1a, "he" would otherwise reach back to the master) |
| J2 | l.236 | Character (break-off, 4th; talk-on spill) | "Fenn abandoned the shakes in mid-run and fixed me with his pale eyes." | → "Fenn fixed me with his pale eyes." |
| J3 | l.246 | Character (turn class; Valens look-back ×2) | "He left the stool for his table, facing Valens, who looked back." | → "He left the stool for his table." (l.270 and l.368 still have him on the table) |
| J4 | l.260 | Character (object-look, 4th; verbatim with l.374) | "He looked at it and slid it away inside his robe." | → "He slid it away inside his robe." |
| H3 | l.6 header | bookkeeping | cycles 0-1, shape 7,438, 49.7% | → cycles 0-2, shape 7,414, 49.8%, 88% |

**Test** (scratch copy `/tmp/claude-0/-home-user/63791ee5-159c-5791-9429-07920f8d9417/scratchpad/rt25c2/books/the-hour-of-ash`, starting from md5 `b48ee45f…`):
- 6 applied; the re-run aborts (exit 1). Patched md5 **`39df960081644e9becf5331cfb362783`**.
- `check_chapter.sh 25`: **ALL MECHANICAL GATES CLEAN**, SHAPE CLEAN. `--gate` clean (Ch.25 gestures unchanged: 'a (long) moment' 2, shrug 1). `--echoes 25`: 0 / 0 / 0.
- Metrics: 7,414 words (shape), dialogue 49.8%, median 11, mean 16.0.
- New strings ("The shadows on the floor had moved", "had moved when", "Fenn called", "He slid it", "left the stool for his table.") were grepped against Ch.1–24, the voice-bank samples, outline and bible: no hits outside Ch.25.
- No cut string is restored, and no closed-list item is used.
- The resulting transition reads clean. l.218 "went on at the wall" → shadows → the boy → "Fenn called to the window behind him" → "Fenn was in the bathhouse keeper's pool again" ("again" now reaches back to l.210 and the l.218 break-off) → Valens and the basil → "Fenn fixed me" → "How'd you know where Pompeii's was?". Mara's "While you were telling me about the ground" (l.420) still holds.

**Counts after J1–J4:**
- Fenn talk-on: 3 (186, 218, 228; 186→218 is ~990 words).
- Fenn wall-keeping: 2 (218, 222).
- Fenn break-offs: 3 (218, 254, 268; span ~1,100 words).
- Fenn object-looks: 3 (202, 374, 382).
- Fenn turns: 6 (0.81/1k; none 3 in 500).
- Valens meets Fenn's eye: 2.
- Every other state is at 3 or fewer, as in the table above.

**Projected:** Characters 8.5 (+0.5) → **Floor 8.5 / Average 8.79 / Casual 9.0 / CVI-Launch 9.8 / CVI-Legacy 7.3**, to be confirmed on the patched page.

### Bookkeeping to carry into finalize (in addition to the cycle-0 and cycle-1 lists)
- **CUT (never restore):** "The shakes ran on till the shadows had moved", "Partway through them", "Fenn stayed facing his wall", "abandoned the shakes in mid-run", "facing Valens, who looked back", "He looked at it and slid it".
- **New WATCH for Ch.26+:**
  - Fenn's narrated break-off is SPENT at 3 ("broke off" ×2 verbatim).
  - Grief shown as a look at an object: ≤1 per chapter for any character.
  - Valens "over the … head" is at 2.
  - Fenn "showed me" is at 2.
- **Header:** "Writer draft 2026-10-24" postdates the continuity repair (2026-10-23). This is a date slip in the comment and has no effect on the page.

## VERDICT (cycle 2)
**POLISH.** Genesis Floor 8.0 (Characters) < 8.5. Casual 9.0 ✓; pacing OK ✓; gates clean ✓. G1–G5 landed and cleared cycle 1's cap reasons. A full recount of every state found four narrated states over the hand rule that the earlier counts missed, all inside Fenn's 218–268 stretch: talk-on, wall-keeping, break-offs and object-looks. Apply `fixes25c/apply_fixes.py` (tested, 6 cuts, nothing added but one name) and re-evaluate. Nothing structural.

BIAS CHECK: This evaluation was produced by the same system that wrote the prose. Confidence in scores above 8.0 requires external validation (beta readers, editors, comp analysis).

---

## Re-evaluation — cycle 3
**Evaluator:** book-evaluator (independent) | **Date:** 2026-10-23 | **Text:** `chapter-25.md` md5 `39df960081644e9becf5331cfb362783` (cycle-2 set J1–J4, H3 applied)

### Verification of the cycle-2 set
- **J1–J4 and H3 landed once.** Every cycle-2 cut string is at 0 ("The shakes ran on", "Partway through them", "Fenn stayed facing his wall", "abandoned the shakes", "facing Valens, who looked back", "He looked at it and slid").
- **Gates on the real file:**
  - `check_chapter.sh 25`: ALL MECHANICAL GATES CLEAN, SHAPE CLEAN.
  - `tic_report.py --gate`: clean. Ch.25 gesture layer: 'a (long) moment' 2, shrug 1. No prop flag.
  - `--echoes 25`: 0 / 0 / 0.
  - Metrics: 7,414 words, median 11, mean 16.0, 5.4% over 40 words, simile 19, dialogue 49.9%.

### Narrated-trait census: EXHAUSTIVE, one pass
Every recurring character and every narrated state, with lines and word offsets. Spec: a state fails at >3 notes in the chapter, or at 3 inside ~500 words. Turning is a gesture class, so it takes the gate's long-chapter rate (one per 1,000 words, cap 7).

**Class rulings, fixed here so later cycles do not re-litigate them:**
- l.168 "let that one in; I saw him decide to" is a *decision to answer*, not an absorption.
- l.416 "his eye strayed to the sill … and stopped" is *noticing*, not a feeling routed into a look.
- Laughs and smiles are separate classes.
- Valens's looks split by kind: finds Mara, watches, meets Fenn.
- Lucius's *mood* (objected / grievance / suspicion) and his *cognition* (studied / weighed / regarded) are separate classes.

| Character | State | Lines (word offset) | Count / spacing | Verdict |
|---|---|---|---|---|
| Fenn | talks on (narrated) | 186 "talking across me" (3039) · 218 "went on at the wall" (~4030) · 228 "in the … pool again" (4121) · **232 "at his next pause" (4245)** | **4; 218/228/232 inside ~215 words** | **FAILS** → K1 |
| Fenn | breaks off / halts (narrated) | **136 "He stopped." (~2315)** · 218 "broke off halfway into the hot springs" · 254 "let that go, short of" · 268 "broke off and drank" | **4**, with "broke off" verbatim ×2 | **FAILS** → K2 |
| Fenn | absorbs news | 98 "testing it" (1766) · 116 "tasting it" (1983) · **324 "He took that in" (5794)** · 388 "let it be" (6619) | **4**; "took that in" also rebuilds 168's "let that one in" | **FAILS** → K3 |
| Fenn | feeling routed into a look at a thing | 202 copper "went on looking at it" · 374 notebook · 382 the bay · **426 "looked at the plant for some while"** | **4**. Cycle 2 filed 426 under "other looks", but its own class includes the bay, so the plant belongs here too. | **FAILS** → K4 |
| Fenn | "slowly" (late manner) | 98 · 388 (6619) · 414 (6938) · 426 (7088) | 4; 388/414/426 inside ~470 words | **FAILS** → K4 |
| Fenn | lighter held or handled | 52 · 168 · **234 "waved the hand with the lighter in it"** · 260 | **4** narrated holds (cycle 2 passed it as a card object, but it is a re-noted state) | **FAILS** → K5 |
| Fenn | copper handled (author's prop rule: 3+ in 400 words) | 202 took (3488) · 202 stood/spun/stopped (~3600) · 210 flicked back (3700) | **3 inside ~210 words**. The gate's regex misses "stood … spun" and "flicked". | **FAILS** → K6 (the flick stays; l.442 "My other copper" needs it) |
| Fenn | bad hand held down | 382 "held it down hard" · 382 "pinning his own hand to the wood" · 394 "the covering hand" | **3 inside ~200 words** | **FAILS** → K7 |
| Fenn | does not ask | 380 "did not ask whose" · 382 "not asking" · 382 "watched him not ask" | **3 inside ~80 words** | **FAILS** → K7 (one cut fixes both) |
| Fenn | bare echo-fragment of Mara's noun before business | 82 Husband · 98 Ninety-eight · **246 The Pythia** · **304 Mules** · 358 · 370 · 388 · 410 Grata | 8 echoes; the "X." + business pattern ×5 | device → K9, K10. That leaves 82/98/410 as the pattern; 358/370/388 are designed. |
| Fenn | "figure" in speech | 162 · 170 · 264 ×2 (the pun) · **268** · 328 | 6; 264/264/268 inside ~140 words | leaned-on word → K11 |
| Fenn | "anyhow" | 152 · 202 · **310** | 3 | third use → K12 |
| Fenn | turns / faces | 54 · 90 · 218 · 234 · 414 · 432 | 6 (0.81/1k, under the cap of 7); none 3 in 500 | OK |
| Fenn | looks away (harbor / ceiling / bay) | 98 · 218 · 382 | 3, spread | OK (K2 keeps the ceiling as the nursing beat) |
| Fenn | looks at people | 82 doorway at last · 106 stared · 210 flicked · 236 fixed me · 282 child properly · 290 watched Lucius · 304 weighed Valens · 414 my hands | each a different state; "sees people last" is the designed arc | OK |
| Fenn | still / quiet | 258 · 260 · 368 | 3 across ~1,500 words | OK |
| Fenn | tremor | 38 · 382 · 394 | 3 | OK |
| Fenn | laughs / smiles | 106, 162 / 156, 268, 398 | 2 / 3, spread | OK |
| Fenn | face moves | 54 and 128 mouth · 140 smoothed · 250 sobered · 318 made a face | different states | OK |
| Fenn | bows · slaps · back-patting | 84, 196 · 152, 402 · 62, 82 | 2 each | OK |
| Fenn | sand on robe | 120 · 282 · 402 | 3, spread (continuity) | OK |
| Fenn | sits on the table / stool | 120 · 168 · 218 · 246 · 368 | blocking that changes; re-notes ≤2 | OK |
| Fenn | eyes "… and back" · "showed me" | 98, 210 · 174, 186 | 2 · 2 | WATCH |
| Valens | doorway station | 80 · 390 · 428 | 3 (390→428 ~480 words, only 2 in the window) | OK |
| Valens | surveys a space | 14 · 68 · 80 | 3; only 68/80 in the window | OK |
| Valens | finds Mara · watches · meets Fenn | 68, 212 · 80, 390 · 304, 434 | 2 · 2 · 2 | OK |
| Valens | "over the … head" | 212 · 434 | 2 | WATCH |
| Mara | words escape her | 48 · 308 · 378 | 3, spread | OK (≤1 in Ch.26) |
| Mara | hands or legs act alone | 60 · 230 · 442 | designed | OK |
| Mara | satchel | 230 · 372 · 400 | 3, spread | OK |
| Mara | looks (smudge / window) | 164 · 360 | 2 | OK |
| Mara | holds it back | 330 "left it empty" · 446 "kept the fire to myself" (+60 "kept them to itself") | 2–3, spread | WATCH: "kept … to itself / myself" ×2 |
| Lucius | lent mood | 80 · 218 · 278 | 3, spread | OK |
| Lucius | lent cognition | 26 studied · **278 weighed** · 278 regarded | 3; "weighed" also repeats Fenn's l.304 inside ~265 words | → K8 |
| Lucius | complaint (events) | 212 · 298 | 2 | OK |
| Walk-ons | captain, sprat boy, crier, ship's boy | 28 · 12 · 158 · 224 | 1 each | OK |
| Narration | "than before" · "was to me" | 218, 382 · 294, 422 | 2 · 2 | WATCH |

### Re-scored Genesis (max ±0.5 per dimension)
| Dimension | Cycle 2 | **Cycle 3** | Basis |
|---|---|---|---|
| Originality | 9.0 | **9.0** | unchanged |
| Theme | 9.0 | **9.0** | unchanged |
| Characters | 8.0 | **8.0** | J1–J4 cleared cycle 2's four counts. The exhaustive census finds more, all present since cycle 0: talk-on 3 inside 215 words (l.232); break-offs 4 (l.136); absorption 4; object-look 4 (l.426); lighter 4; copper 3 inside 210 words (the author's prop rule); held-down hand and "not ask" each 3 inside 200 words. **The cap holds.** Uncapped value is 9.0: Fenn's bilingual voice, Mara's chaos 4/4 inhabited, every secondary with an independent moment, and Valens's belief shown and never declared. |
| Prose & Voice | 8.5 | **8.5** | stopping sentence l.60 intact; no sample lifts; no spent object |
| Pacing | 8.5 | **8.5** | 7,414 words (88%), dialogue 49.9% in band, value shift on two axes. **PACING: OK.** |
| Emotion | 9.0 | **9.0** | anchor, body rebel and surprise intact |
| Immersion | 9.0 | **9.0** | blocking holds |
| **FLOOR / AVERAGE** | 8.0 / 8.71 | **8.0 / 8.71** | Characters |

**Casual Reader 9.0** (unchanged: the lighter, "Thanks," the bus). **CVI-Launch 9.8** (9.29 + 0.5 anchor). **CVI-Legacy 7.3.** Anti-AI 7/20, all minor, CLEAN; #11 at 4 (0.54/1k), under the cap. Divergence: 1.8.

### Cycle-3 fixes (TESTED, all census failures in one script)
`/tmp/claude-0/-home-user/63791ee5-159c-5791-9429-07920f8d9417/scratchpad/fixes25d/apply_fixes.py <path/to/chapter-25.md>` holds 13 exact replacements. Each is a cut or a re-join: there is no new image and no new beat. Each old string must occur exactly once or the script aborts and writes nothing; a second run aborts.

| # | Line | Now | Revision |
|---|---|---|---|
| K1 | 232 | "I asked, at his next pause." | "I asked." |
| K2 | 218 | "Fenn broke off halfway into the hot springs. He looked at the ceiling." | "Fenn looked at the ceiling." |
| K3 | 324 | 'He took that in. "Well, cripes," he said at last.' | '"Well, cripes," he said at last.' |
| K4 | 426 | "Fenn looked at the plant for some while, and then slowly leaned over and nudged the pot" | "Fenn leaned over and nudged the pot" |
| K5 | 234 | "He waved the hand with the lighter in it at his room," | "He waved a hand at his room," |
| K6 | 202 | 'like it had been crying." He stood the copper on its edge and spun it on the table, and stopped it with a finger. "Anyhow."' | 'like it had been crying. Anyhow."' |
| K7 | 382 | " He was pinning his own hand to the wood and not asking, and I watched him not ask." | " I watched him not ask." |
| K8 | 278 | "Lucius tried the sand again, weighed the taste, spat" | "Lucius tried the sand again, spat" |
| K9 | 246 | '"The Pythia." He left the stool for his table. "You asked' | 'He left the stool for his table. "You asked' |
| K10 | 304 | '"Mules." He weighed Valens with a look,' | "Fenn weighed Valens with a look," (named: l.302 ends with Valens as its subject) |
| K11 | 268 | "I've got a feeling it's fair. I figure it owes me sixty-eight." | "I've got a feeling it's fair, that it owes me sixty-eight." |
| K12 | 310 | "You'd find out anyhow." | "You'd find out anyway." |
| H4 | 6 header | stale counts; "Writer draft 2026-10-24" | shape 7,344, ~7,710, 87%, 50.2%, cycles 0-3 (K1-K12); "Writer draft and continuity repair 2026-10-23" (consistent with the eval and audit history) |

**Test** (scratch copy `/tmp/claude-0/-home-user/63791ee5-159c-5791-9429-07920f8d9417/scratchpad/rt25c3/books/the-hour-of-ash`, starting from md5 `39df9600…`):
- 13 applied; the re-run aborts (exit 1). Patched md5 **`b3642f8e4fb711f8b608bf80a541bbbc`**.
- `check_chapter.sh 25`: **ALL MECHANICAL GATES CLEAN**, SHAPE CLEAN. `--gate` clean. `--echoes 25`: 0 / 0 / 0.
- Metrics: 7,344 words (shape), dialogue 50.2%, median 11, mean 16.0.
- New joins ("Fenn looked at the ceiling", "crying. Anyhow", "waved a hand", "that it owes me", "find out anyway", "Fenn leaned over and nudged", "Fenn weighed") were grepped against Ch.1–24, the samples, outline, foundation, voice-dna and the bible. There are no hits. "In the end" was rejected for K4 because Ch.24 l.370 opens a paragraph with it.
- No cut string from F/G/J is restored. No closed-list item is used.

**Counts after K1–K12** (the same classes as the table above):
- Fenn: talk-on 3 (186/218/228, span ~1,080 words); break-offs 3 (136/254/268, "broke off" ×1); absorbs 3; object-look 3; "slowly" 3 (no 3 in the window); lighter 3; copper 2; held-down 2; "not ask" 2; echo-fragment pattern 3; "figure" 5 (one pair is the pun); "anyhow" 2.
- Lucius: cognition 2.
- Everything else is as tabled.

**Projected:** Characters 8.5 (+0.5) → **Floor 8.5 / Average 8.79 / Casual 9.0 / CVI-Launch 9.8 / CVI-Legacy 7.3.** Cycle 4 needs only to verify the patched page against this table, because the census is now complete by construction.

### Bookkeeping to carry into finalize (in addition to cycles 0–2)
- **CUT (never restore):**
  - "at his next pause"
  - "broke off halfway into the hot springs"
  - "He took that in."
  - "looked at the plant for some while, and then slowly"
  - "the hand with the lighter in it"
  - "He stood the copper on its edge and spun it"
  - "pinning his own hand to the wood and not asking"
  - "weighed the taste"
  - '"The Pythia." He left'
  - '"Mules." He weighed'
  - "I figure it owes me sixty-eight"
  - "You'd find out anyhow"
- **FENN card:** "the copper spun on its edge" (SPENT list) and the lighter's "waved" are no longer on the page. The tremor note needs a re-sync (on the table / held down / the hand that stays). The card head and the changelog say "Writer draft 2026-10-24"; make them 2026-10-23.

## VERDICT (cycle 3)
**POLISH.** Genesis Floor 8.0 (Characters) < 8.5. Casual 9.0 ✓; pacing OK ✓; gates clean ✓.
- J1–J4 landed and cleared every count cycle 2 named.
- The exhaustive one-pass census found nine more narrated states over the hand rule, all in the cycle-0 text. Fenn has eight (talk-on, break-offs, absorbing news, object-looks with "slowly", the lighter, the copper fidget, the held-down hand and "not ask"); Lucius has one (lent cognition).
- Three voice-hygiene items are in the same set: the echo-fragment, "figure" and "anyhow".
- Apply `fixes25d/apply_fixes.py` (tested; 13 cuts and re-joins) and re-evaluate. Nothing structural.

BIAS CHECK: This evaluation was produced by the same system that wrote the prose. Confidence in scores above 8.0 requires external validation (beta readers, editors, comp analysis).
