# Evaluation: Chapter 15 — Summer Pasture (run 2)
**Evaluator:** book-evaluator (independent; did not write or revise this prose) | **Date:** 2026-10-20
**Text evaluated:** `manuscript/chapters/chapter-15.md` (sha256 `451abfbb…`, md5 `5ea1f666…`), after writer → dialogue-polish → hook-craft → disruptor → continuity repair (W-01…W-11 + I-04). **7,719 prose words** (shape_check), 7,730 (style_check), 8,037 (`wc -w`, with the header).

**Read against:**
- the book's CLAUDE.md hard gates;
- STATE.yaml guardrails (NO FORESHADOWING; NO TICS incl. gestures; the retired reflexes; ROMANCE HEAT: explicit but occasional, earned, none after the eruption) and resolved_author_decisions (ARCH-13: heat at Ch.15; AUTHOR-CP2-1…4);
- voice-dna §0, §1, §3, §3b, §4, §5 (the intimacy register), §6;
- character-bible.md: the MARA, VALENS and MNASON cards, and every at-risk / spent block from "after Ch.1" to "after Ch.15";
- outline Ledger row 15 and `## Chapter 15`;
- `evaluations/chapter-14-eval.md` (cycle 0, cycle 1, finalize);
- chapters 13 and 14 in full for pacing; Ch.3 (the crossing), Ch.6, Ch.8, Ch.11 and Ch.12 wherever Ch.15 revisits a place, a beat or a body;
- `evaluations/continuity/chapter-15-audit.md` (which WARNs were applied, and which INFO items were left);
- voice-bank samples 03, 05, 06, 08 and 10 by structure, and all 13 by 3- and 4-gram.

**Genre profile:** commercial historical romance / time-slip, comp *Outlander*. Anti-AI band: commercial (0–8 clean, 9–11 watch). Engagement: empathy 55 / fascination 30 / self-insertion 15. Dimension 7 = **IMMERSION**.

**Measured here.** `bash books/the-hour-of-ash/tools/check_chapter.sh 15` is **clean on every gate**:
- style: simile 0.5/1k, em-dash 0, foreshadow 0; grammar 0 errors; rhythm 0;
- show/tell: no flags, dialogue 33.6%; voice-wear strict clean;
- tic gate clean (and-chains 6/9, credential asides 0, negation pivots 0, "So" 0); echo 0; command echo none;
- metaphor 1.3 fig/1k, median 16; `shape_check --strict`: `15 7719 3 34 16 long-spiral quiet`, CLEAN.

**My own scans (scratch, not gates):**
- 4–6-grams against Ch.1–14 and all samples; all-content 3-grams against the samples;
- by hand: #11 explanatory extensions, paragraph-final negations, present tense in narration, narrator vague-locators and result clauses;
- every SPENT / CLOSED item in the bible grepped by frame as well as by string;
- the Ch.15 cave set beside Ch.3's cave paragraphs, beat by beat.

**The fix set was applied together to a scratch copy** and swapped into the manuscript path. It was run through the real `check_chapter.sh 15`, `shape_check --strict` and `tic_report.py --gate` from /home/user/Books. The original was then restored, and its checksum verified after every run (sha256 `451abfbb…`, md5 `5ea1f666…`). I did not edit the manuscript.

*(l.N = line number in the current `chapter-15.md`.)*

---

## HEADLINE
**CVI-Launch (CVI-L):** 9.8 (9.29 base + 0.5 strong anchor) | **CVI-Legacy:** 7.1 (provisional) | **Genesis Floor:** **8.0** | **Genesis Average:** **8.71**
**Casual Reader:** **9.0**
**Engagement type:**
- **Empathy** leads: she tells the truth badly, he asks about mules, and the funny part is the tender part.
- **Fascination** is second: the flashlight lighting his fingers red; a herdsman's rennet; the cave's back wall.
- **Self-insertion** is tertiary: the reader is the one who knows what Pompeii means.

**Divergence alert:** none (9.8 − 8.0 = 1.8).

**Gate (Floor ≥ 8.5 AND Casual ≥ 8.5 AND pacing OK AND gates clean): NOT MET.**
- Casual 9.0 ✓; pacing OK ✓; gates clean ✓.
- **One dimension holds the floor: Prose & Voice 8.0, on merit, with no cap.**
  - #11 is under the commercial cap (5 firm at 0.65/1k).
  - What holds it is a cluster of book-law items the gates cannot see:
    - a third narrated fronted object (CLOSED at 2), on a sample-05 4-gram;
    - the SPENT gaze-arrival "then";
    - two present-tense generalizations in narration;
    - the cave re-entered in Ch.3's geometry, plus Ch.3's closing "into October";
    - a held silence filled by a fire catching (SPENT);
    - "had gone quite still" (the CLOSED "had gone quiet" family);
    - two sample 4-grams and a sample-10 image;
    - a forming narrator habit: "somewhere" ×5, result-clause "so that" ×7;
    - in-scene doubles in the union ("in my hair" ×3, which also re-stages Ch.12's spent forehead-on-hair; "and stayed" ×3);
    - four small fact and logic slips the continuity audit left as INFO.
- **Characters sits at 8.5**, not 9.0, for four Valens register slips (an idiom, a kenning, Mnason's fronted object in his mouth, and a paired "Then I'll ___ it") and the hoof re-staged from Ch.11.

**Every fix is a swap or a cut. 45 strings, tested together:**
- 7,507 words (shape_check; floor 7,300 ✓); dialogue 34% (30–40 ✓); median 16 (floor 16 ✓); 3 breaks; `long-spiral` → `quiet`;
- all gates clean, echo 0;
- the first sentence, the mule line and the last paragraph are byte-identical.

---

## Genesis Score (Craft Assessment)

| Dimension | Score | Evidence | Cap reasons / holds |
|---|---|---|---|
| Originality | 9.0 | **The outline's subversion is on the page:** he does not believe her and wants her anyway ("I believe that cave had a light in it with no flame. I was there to see it." / "The rest is yours.", l.498–502). **The writer's inventions on top of it:** (1) the truth told by a man half-shaved with a wet knife in his fist: "**Half his face was shaved and half was not, and he turned the whole of it on me.**" (l.168); (2) the flashlight under his cupped palm: "his fingers lit red along their edges, all of them, with the dark of the bones down their middles" (l.132), and the Energizer rabbit "who went drumming through other people's commercials and would not stop" against batteries that are tiring; (3) the crack's back wall and the harvestmen coming apart "one leg at a time" (l.34); (4) the bargain punctuated by hiccups, the last landing "exactly on the last word" (l.328); (5) Mnason's fig twig refused and the kid's stomach he had all along: "you'll know whose doing that was" (l.90); (6) the juniper fight, "The crowd was ewes." (l.416); (7) the bed's fork splitting, and "His palm was under my skull before the floor was" (l.546); (8) the teeth held against him in the wreck (l.558); (9) the close: Felix's swollen lips and one bitten green fig (l.600). | **≥9.0 challenge:** would a senior editor set this beside *Outlander*'s wedding-night chapter? Yes. It keeps the genre's first-night beat and makes the comedy the intimacy. **Not 9.5:** the dawn-to-night day on a pasture is the outline's frame, and the laugh is again the emotional channel (see Emotion). |
| Theme | 9.0 | "Being known completely and wanted anyway" is carried by acts. **Acts:** "Do they still have mules?" / "Who leads them?" / "Men in hats. They walk in front." (l.190–196): the outline's subtext, a man asking whether there is work for him in her world, which neither hears; "Then I'll wait outside it," (l.366); "It'll get you on a boat." (l.506). **Her side:** "Because there I know where everything is kept." (l.364). **Texture that means nothing:** the snowplow described to a ewe (l.62); Mnason's son's wife "from Amphissa" (l.466); the brother's six figs "for a bet" (l.454); the boatman's cousin and a wager (l.392). | **≥9.0:** a question with no answer yet. He disbelieves and stays; she means to leave and lies down with him. No echo chamber. **Not 9.5:** "Because it is my own" (l.364) states her side once in speech. That is earned, but stated. |
| Characters | 8.5 | **Mara: chaos 4/4, inhabited** (below). **Valens:** practical questions only (emperor, roads, the god's house, the spring, "Is the sea still salt?"); deadpan ("Italy's long," l.390; "I saw the juniper," l.444; "I was watching the figs.", l.556); his stillness breaks at last (l.578). **Felix:** stacked questions, the boys' race, and "**Would you cry, if it was me?**" / "Only a little," … "Not in front of everybody." (l.434–438). He flinches only when unwatched (l.440). **Mnason:** the dead mother's kitchen ("Fig, she turned it with, every day she lived", l.90); never asks who they are ("Your man's shaved," l.480). **Kallia,** in backfill: the public lie with "half the lane listening" (l.16). Cover-the-name PASS for all five speakers. | **No cap** (verbal tics 0; gate gesture classes clean). **Held at 8.5 by four Valens register slips:** "Delphi's put you on a boat. Leave yourself on it." (l.344, an idiom; his Part One Greek is "flatly literal, without idiom"); "the box with the eye in it" (l.288, a kenning, which is a metaphor in his mouth); "Neapolis I know of." (l.274, Mnason's fronted-object fingerprint, bled across in the same chapter); and "Then I'll wait outside it," / "Then I'll believe it," (l.366, l.510), the same four-word skeleton closing two sections. **Also:** the black's near fore is his business twice (l.8, l.440), and l.440's paring re-stages Ch.11's paring of the same hoof. |
| **Prose & Voice** | **8.0** | **Stopping sentences:** "his fingers lit red along their edges, all of them, with the dark of the bones down their middles" (l.132); "**His palm was under my skull before the floor was, and the floor took the back of his hand instead**" (l.546). **Underlines:** "He put the wrong end to his eye first and got nothing but his own lashes in the glass." (l.234); "It keeps what it shows." (l.238); "One print on that glass … and I might as well never look through it again." (l.254); "her tail switching at his face and his face not caring" (l.54); "The crowd was ewes." (l.416); "Where he could see me looking he never flinched. When he took me to be looking elsewhere, he did, each time." (l.440); "and hung it on the peg … with the lens turned to the wall" (l.542); "so that his hands would find no work in it" (l.542); "then they remembered themselves and were careful, which was worse, and better" (l.568). **Ugly sentence:** "The cheese was good and Mnason said it was not and ate most of it." (l.452). **Voice under pressure / heat:** the asides go quiet after "Here?" (l.564) and the senses widen into one long sentence (l.576), as voice-dna §5 asks. | **Merit 8.0, no cap.** #11 is under the cap (5 firm, 0.65/1k), and the ugly sentence and the voice change are both present. **Held by the law cluster** (P1–P17, H1–H9, F1–F6 below): CLOSED and SPENT frames, present tense in narration, the cave in Ch.3's words, sample strings, a forming "somewhere" / "so that" habit, and doubles inside the union. Anti-AI 10/20, −1.75 (watch band). |
| Pacing | 8.5 | **The ledger row is hit on every hard field:** Chronological day-in-full (between Ch.14's Fragmented and Ch.16's Parallel) ✓; open `long-spiral` (the bells, cold, thyme and dew sentence) ✓; close `quiet` (15 words) ✓; 3 breaks ✓; dialogue 33.6% (30–40) ✓; 7,719 against 7,800 ✓; median 16 (the floor; narration alone runs about 20) ✓. **Speed design:** S1 slow dawn, with a backfill ladder (the runner, the loft, the cave); S2 brisk Q&A and bargain, punctuated by hiccups; S3 Felix's quick talk, the fight and supper; S4 slow and specific, then very quiet. **Value shift:** alone with the secret (−) → known and disbelieved (±) → bargained (+) → lovers (+). | **Not 9.0:** the present day stalls at l.14–l.50. About 650 words of backfill (the runner, Kallia, the loft, then the full cave scene) run before the milking resumes the morning. The bible asked for "a clause or a short backfill". It earns its place, because it is Valens's first sight of the flashlight and noon pays it ("The light in the cave," l.126), but the Devourer feels it. The gear sits at the floor of high. |
| Emotion | 9.0 | **Anchor lands** exactly as planned: "Do they still have mules?" (l.190), asked by a half-shaved man still holding the knife (l.184), after he has looked at the cave so long that she thinks he understood nothing. **Surprise:** the hiccup on "wife" (l.328); the union as a fit of laughter in a collapsing bed (l.548–558); "**I was watching the figs.**" **Body rebel:** the shiver in the dark cave, "hard enough that he heard my teeth" (l.46); the hiccups (l.300, l.324); laughter neither can stop (l.550); "I came with my heel hooked behind his knee" (l.578); his stillness leaving him "the whole of it at once" (l.578). **Techniques ≥5:** physical sensation, humor in intimacy, dramatic irony (Pompeii's fate withheld at l.282; "Then I'll wait outside it"), object proxy (the lens to the wall, the belt out of reach, the bitten fig), subtext (the mule question), and a child's question about crying. | **≥9.0.** **Not 9.5:** the peak is a laugh again (Mara's laugh-as-peak: Ch.2, 6, 7, 8, 14, 15). It is outline-mandated and new in shape (shared, his and hers), but the channel is familiar. |
| **Immersion** (Dim 7) | 9.0 | **Period:** transhumance huts, folds and a winter at the gorge foot; milking ewes from behind at a hurdle gap; fig sap and kid's rennet (*Il.* 5.902 behind it); pitch versus lamp-flame depilation; the forked-stake bed of poles, bracken and fleeces; a leather pail threat; Hero's self-opening temple doors as sailor's hearsay; the diolkos as a boy's rumor; the Isthmian boys' race and the pine; the Corinth arena. **1998, used:** the Energizer rabbit, the answering-machine tape, the Grand Canyon mules, the fenced Castalian spring, Dionysius Exiguus's four years, a 36-exposure strip. | **Held at 9.0.** Fact slips: "ricotta … squeaked" (fresh ricotta does not squeak; L3); "Further up" on the dust map (Pompeii lies short of Puteoli coming round from the heel; L2); "two magistrates a year" (Pompeii elected four; L6); "a strip as long as your arm" (a 36-exposure roll is about 1.6 m; L5). |
| **FLOOR** | **8.0** | Prose & Voice (merit) | |
| **AVERAGE** | **8.71** | (9.0 + 9.0 + 8.5 + 8.0 + 8.5 + 9.0 + 9.0) / 7 = 61.0 / 7 | |

**Trajectory vs Ch.1–14** (finals 8.50–8.86; cycle 0s 7.5–8.0): the fifteenth cycle 0 below the gate, and the eleventh held by narrator moves the gates cannot see. This one is **not** held by the #11 cap, which held Ch.10, 12, 13 and 14. That cap had been the recurring cause, and here the repair chain stayed out of it: the continuity repair added no gloss.

---

## CVI-Launch Breakdown
| Input | Score | Evidence |
|---|---|---|
| Commercial Pacing | 8/10 | A long chapter that never sags in its middle (Q&A, bargain, fight, supper, bed). It loses 2 for the front-loaded backfill and the length. |
| Tomorrow Test | 6+ anchors → 10 | IMAGE: fingers lit red over the flashlight; the half-shaved face; the harvestmen; the bed's head dropping onto his palm; Felix's fat lips and the bitten fig; the lens turned to the wall. QUOTE: "Do they still have mules?"; "Then I'll wait outside it,"; "The crowd was ewes."; "I was watching the figs." |
| Casual Reader | 9.0/10 | See report. |
| Shareability (quote / plot / emotional) | 5 / 3 / 5 → 10 / 6 / 10 → **9.47** | Quote: "Do they still have mules?" Plot: "she tells him she's from 1998, and his first question is whether they still have mules." Emotional: "their first time, the bed collapses and they can't stop laughing, and then they do." MAX 10 × .6 + AVG 8.67 × .4. |
| Concept Pitch | yes → 10 | |
| Human Closeness | yes → 10 | Almost the whole chapter is two or three people talking close, then two people in a hut. |
| **CVI-Launch** | **9.29 + 0.5 = 9.8** | 8 × .2 + 10 × .2 + 9 × .2 + 9.47 × .2 + 10 × .1 + 10 × .1 = 9.29. One-chapter formula; see BIAS CHECK. |

**CVI-L note.** In this project "CVI-L" means **CVI-Launch: 9.8**.
- It ties the book's high (Ch.8, Ch.13) and recovers from Ch.14's designed breath (8.9). Running CVI-L Ch.11–15: **9.5 / 9.7 / 9.8 / 8.9 / 9.8**: a turn, a held night, then the romance turn the outline built Part One toward.
- It rests on what a reader texts a friend: the mule line, the bed and the laugh. None of the 45 fixes touches an anchor (the mule line, the red fingers, the palm under her skull, the teeth, the fig), so **CVI-L is unchanged after the PATH (9.8).**
- This is the first heat scene in the book. Outlander readers recommend on exactly this beat, so Shareability is the input carrying the score. The risk is ahead: Ch.16–18's yearning without sex has to hold a readership this chapter has just rewarded.

**CVI-Legacy (default weights; provisional):** Originality 9.0 × .30 + Theme 9.0 × .25 + Cultural Vocabulary 3 × .20 ("Do they still have mules?" is fandom-quotable) + Re-readability 7 × .15 + Identity 5 × .10 = **7.1** (Ch.14 6.9). Re-read rewards:
- "eight years on from this summer, and a few weeks over" (l.282) under "I'll wait outside it";
- "How will you know the door, among all those tombs?" (l.292);
- "Who's looking for you, there?" / "That's true, then." (l.224–228);
- the camera that "keeps what it shows … in the dark" (l.238–242), with no pointer from the narrator.

---

## Anti-AI Scan (20 patterns; density per 1,000 words at 7.72k; commercial band)
| # | Pattern | Result | Count / density | Citation |
|---|---|---|---|---|
| 1 | Forced symmetry | FOUND moderate | 4 (0.52) | l.440 "Where he could see me looking he never flinched. When he took me to be looking elsewhere, he did"; l.568 "which was worse, and better"; l.476 "which were bitter in a way that grew on you … which did not"; l.186 "in my year … into yours". **−0.25** |
| 2 | Empty poetic vocabulary | Clear | 0 | |
| 3 | Automatic rule of three | FOUND moderate | 6 (0.78) | l.296 "the count, the cave, the door in the town"; l.340 "The porter will ask, and the brother, and his cook"; l.364 "a house … and my work, and my name on a door"; l.476 bread / greens / wine; l.234 "the plateau … and the shadowed notch, and the cliff above it"; l.580 "the fork split, the poles off it, half the fleeces on the floor". **−0.25** |
| 4 | Em dashes | Clear | 0 | |
| 5 | Empty metaphors | Clear | 0 | Similes are characterizing: "like old bread" (moonmilk), the bronze in its crate, the goat late for something. |
| 6 | Dramatic "And" openings | Clear (narration) | 0 | Speech has four "And…?" rejoinders, all Mara's (l.316, 350, 356, 500). That is at the bible's WATCH cap of ≤4, owned by one speaker. |
| 7 | Pseudo-philosophical closings | Clear | — | The chapter and all three sections end on acts, a line or an image. |
| 8 | Excessive parallelism | FOUND moderate | 4 (0.52) | l.6's double anadiplosis (the designed spiral; kept); l.296 "put it away as Kallia put away"; "As man and wife." said twice across speakers (l.326, l.330; designed); "Then I'll wait outside it," / "Then I'll believe it," (l.366, l.510). **−0.25** |
| 9 | Overly smooth transitions | FOUND minor | — | Section and scene openers as a time ladder: "At noon" (l.116), "In the worst of the afternoon heat" (l.372), "At sundown" (l.446), "While he walked the line in the dusk" (l.514). This is the day-in-full spine, so minor. **−0.125** |
| 10 | Described emotions | FOUND minor | 2 (0.26) | l.46 "I waited to see what I would feel about it" (metacognitive); l.572 "it went through me" (sanctioned contraception thought; kept). **−0.125** |
| 11 | **Explanatory extension** | **FOUND moderate, under the cap** | **5 firm (0.65/1k)** | (1) l.178 "I, **who had begun with a monk's mistake and could not see how to get from there to anywhere**, did the sum aloud, **and that was worse still**" (tells the reader it went badly; the speech already shows it); (2) l.184 "told him the rest in one go, **to have it out before he could stop me**"; (3) l.296 "**; I had not thought he would be kind about it**" (interprets the simile it follows); (4) l.328 "**so that I seemed to answer him with it**" (explains the joke); (5) l.514 "the dark of the plateau, **which was the way up to us for anybody coming**" (Ch.12 already planted it). Borderline, not counted: l.34 the batteries "had begun to tire"; l.234 "though up here nobody would take it"; l.378 "so as not to hear him"; l.450 "the most I had heard him say to Mnason in a week"; l.542 "so that his hands would find no work in it" (a keeper); l.570 the road simile's "feeling where it led and where it gave"; l.282 "his question had been about the road". **−0.25.** Cap (commercial >6 or >0.8/1k): **PASS.** |
| 12 | Binary negation opener | Clear | 0 | |
| 13 | Precision flex | FOUND minor | — | The AD count is the chapter's subject ("nineteen hundred years, and twenty-seven more. Twenty-six, and some months"); incidental: "three times since the full moon", "a dozen figs", "a hundred small places". **−0.125** |
| 14 | Emotional control demonstration | Clear | — | Control fails (the shiver, the hiccups, the laugh, his stillness). |
| 15 | Authoritative description | FOUND minor | — | The hut's construction (l.516) and the fold (l.54) are encyclopedic. Offsets: "something pale and soft-looking" (l.34); "I had never looked underneath it" (l.516). **−0.125** |
| 16 | Philosophical asides | FOUND minor | 1 (0.13) | l.476 "bitter in a way that grew on you", a generic "you" in narration. **−0.125** |
| 17 | Clean dialogue | FOUND minor | — | The noon Q&A runs eight orderly question-and-answer turns (l.200–228). The outline mandates the practical questions, and the shaving business interleaves them. Elsewhere the talk breaks up: hiccups; Felix "faster than my Greek would go"; Mnason talking to the pot. **−0.125** |
| 18 | Thematic echo chamber | Clear | — | Texture present (see Theme). |
| 19 | Graduated reveal | Clear | — | Day-in-full, no crisis. |
| 20 | Emotional temperature report | Clear | — | No periodic body check-ins, and none in the heat scene. |

**10 / 20 found (#1, #3, #8, #9, #10, #11, #13, #15, #16, #17). Total −1.75. Band: WATCH** (commercial 9–11). **#11 hard check: PASS** (0.65/1k).

**After the PATH:**
- #11: no firm instance (F1–F6; seven borderline clauses stay, at most 0.8/1k by the strictest count, at the cap's edge, not over it);
- #10 clears (P12);
- #16 clears (P10);
- #8 drops to minor (C5);
- → **7/20, −1.125, clean band.**

---

## The book's own laws
- **NO FORESHADOWING: PASS, 0.** The gate agrees, and so does a hand read of families A–E.
  - AD 79 appears **once**, as a present thought in fresh words: "The rest of what I knew stood behind the name: eight years on from this summer, and a few weeks over." (l.282). The Ch.14 words ("Seventy-nine, late in the summer", stones, roofs) are not reused.
  - Every forward line is an intention or a conditional: "When I find the door … I shall go home." (l.360); "Then I'll wait outside it," (l.366); "Suppose you see it open?" / "Then I'll believe it," (l.508–510).
  - The contraception thought implies no outcome (l.572), and the narrator does not resolve it.
  - Delphi's ruin (l.214) is world history in Mara's mouth. Family E is clean: the camera that "keeps what it shows … in the dark" is not linked to the ash by the narrator, and that irony is left to the reader.
- **The truth told badly, without Pompeii's fate: PASS.**
  - Valens is told 1998 by the Judaean count, Philadelphia "Further than Asia", the cave as a door for one afternoon, Pompeii as a place, the tombs and her intention.
  - The fate is withheld in narration ("I left it standing where it was", l.282).
  - He disbelieves, and stays (l.498–506).
  - It is told badly: she starts from a monk's arithmetic, misstates the count and corrects it ("Twenty-six, and some months"), and explains May ("It is a month we have; it comes after April." / "I know May.").
- **"Do they still have mules?" once: PASS** (l.190, 1 of 1). There is no callback, and no paraphrase about another animal or trade.
- **The bargain: PASS.** It is spoken plainly, and brisk:
  - the book at Corinth (l.298);
  - the brother's suit and testimony (l.306);
  - the archive;
  - Corinth in autumn before the rains, winter there, sail in spring "As man and wife" (l.326);
  - the bowl let go (l.342–354);
  - Felix in (l.358).
  It also registers the change from Ch.14's Delphi-winter plan (continuity I-17 closed).
- **HEAT 1, NON-NEGOTIABLE: PASS on craft** (see the heat verdict below).
- **Memory only when the scene triggers it (CP2-2): PASS.**
  - The Italian Market cheese is triggered by the herdsman's cheese squeaking and returns to it ("the herdsman's was sharper, and had a hair in it", l.452).
  - The pink razor is triggered by her own shins at the seep (l.374) and returns to them.
  - Both are clauses. **No longer memory** (the bible's Ch.14 rule for Ch.15–16) ✓. No parent appears in either (the Ch.14 rule) ✓.
- **Explanation-density cap: PASS** (5 firm at 0.65/1k) → 0 firm after F1–F6.
- **Paragraph-final negations ≤1.5/1k: PASS.**
  - **10 in narration (1.30/1k):** l.20, 24, 50, 88, 124, 296, 414, 526, 542, 572. My count matches the audit's I-28.
  - l.24 and l.50 make the same "said nothing but the path" move 13 paragraphs apart. P11 cuts l.24's.
  - **After the PATH: 8 (1.07/1k).**
- **No comparisons in Valens's speech: PASS on simile and comparison.** He uses no "like" or "as" and makes no figurative comparison.
  - The Alexandrian temple door (l.258) is a literal precedent offered as evidence ("It was made somewhere."). It is his worldview (a marvel has a maker), not a comparison.
  - **Register slips (not comparisons) → C2, C3:** "Leave yourself on it" (an idiom) and "the box with the eye in it" (a kenning).
- **NO TICS, verbal: PASS.** No catchphrase. "Then I'll ___ it" ×2 is a forming reply shape → C5.
- **NO TICS, gestures and narrator moves the gate cannot classify:**
  - **Narrated fronted object** (l.44 "**the thing in my hand he left to me**"): the bible keeps the pair (Ch.9 ¶110, ¶336), "**A third fronted-object sentence anywhere in the book is a tic.**" This is the third. It also carries sample-05's 4-gram "thing in my hand" (audit I-24, left as INFO) → **P1**.
  - **Gaze-arrival "then"** (l.188 "and then he was facing me"): the "looked at me then / came round then" family is SPENT, and Ch.14's C2 cut the last one → **P2**.
  - **A held silence filled by something moving** (l.494 "Valens laid a root of juniper on the embers **and watched it catch.**", just before "You do not believe a word of it"): SPENT, "0 more anywhere" → **P9**.
  - **"had gone quite still"** (l.562): "had gone quiet" is CLOSED at 2 (Ch.9, Ch.13). This is the same frame with a sibling adjective → **H2**.
  - **"somewhere" as the narrator's vague locator, ×5 in narration** (l.368, 532, 550, 560, 572), four of them in the hut. Two make the same move: a bodily thing ends unnoticed ("My hiccups had gone, somewhere in the course of it." / "somewhere in that his laughing ran out"). That is also Ch.6's "so slowly that I could not have said when it was gone". **Kept:** l.560 (the outline's "the moment the laughter stops") and l.572 ("lost count of my month somewhere around October"). → **P14, P16, H1**.
  - **Result clauses "so that …", ×7 in narration** (l.6, 28, 300, 328, 526, 542, 550): the narrator's consequence reflex → P3, P15, F4, H1 take it to 3.
  - **Valens's hands on the black's near fore twice** (l.8, l.440). His card says "always a different object". l.440's paring re-stages Ch.11's paring of the same hoof, and its "and he kept on paring" echoes Ch.14's "I kept on holding it." → **C6**.
  - **Removal gestures** ("picking a needle out of his eye", l.526; "picked the thyme from his teeth", l.326; "picked the bracken out with my teeth", l.560): three in the chapter, two within 500 words. That is under the cap; C1 varies the verb on l.326.
  - Gate classes: object handling, nod and the rest are all under cap; kneel/crouch 0; hand-on-knee 0; bend 0; deliberation pause 0; exit by gait 0 ✓.
- **Present tense in narration (voice-dna §0.4; bible "Present-tense … in narration: 0"): FAIL ×2.**
  - l.28 "like a kitchen when the heat **comes on** in a cold house". The vehicle is also the book's third heat-in-a-cold-home image (Ch.1's heater ticked; Ch.13's imagined first hour home with "the heat … off", SPENT) → **P3** (the simile is cut).
  - l.128 "it weighed about what a hen's egg **weighs**" → **P4**.
- **No reuse of earlier chapters' phrases or set pieces, including the cave in its Ch.3 words: FAIL, cleared by the PATH.**
  - **The cave staged in Ch.3's order and geometry** (l.32). Ch.3 l.121 runs: daylight fails, "the floor began to climb", "the roof came down", flashlight. l.32 runs: "far in, where the roof dropped and the floor climbed to meet it, the dim gave out, and I dug in the bag for the flashlight." l.32's "The daylight went farther in than I had ever seen it go" also reworks Ch.3 l.161's crossing anomaly ("Now it reached far into the cave in a long slant"). → **P5**.
  - **"whose far end had always been black to me"** (l.34) against Ch.3 l.123 "Beyond the bend the beam ran on into black." "Did it ever go on?" / "Once." (l.38–40) carries the contrast unaided → **P6**.
  - **"into October"** (l.186) re-says the book's first cliffhanger, Ch.3's last line "I stepped out into October." → **P7**.
  - **Ch.12's spent intimacy beat:** "He let his forehead come to rest on my hair" (Forehead resting on her hair: once). Ch.15 has "in my hair" ×3 in the union (l.568, l.580, l.590) → **H3, H4** (one stays: l.568).
  - **Voice-bank strings:**
    - sample-05 "thing in my hand" (l.44) → P1;
    - sample-06 "water in a basin" (l.476, as a simile) → **P8**;
    - sample-10's image of a shepherd's dwelling built to its builder's size: "built for one small shepherd who did not move in his sleep" against l.530 "Mnason built it to fit Mnason" (audit I-25, left) → **C7**.
  - **In-chapter and adjacent-chapter doubles:**
    - "uppermost" (l.30, l.128; Ch.14 l.26 had it too) → **P13**;
    - "breastbone" ×3 → **H8**;
    - "by the cheese baskets" twice in two sentences (l.542) → **H6**;
    - the bed "had held me" (l.516) and "had borne me" (l.544) → **H7**;
    - "and stayed" ×3 in the union (l.576, 578, 596) → **H5**;
    - "a man in a [paper hat / white coat]" for two 1998 tradesmen four lines apart (l.452, l.558; with Mara's "Men in hats", l.196) → **P17**.
- **Retired reflexes:** no define-by-negation opener; no performed candour; no scene button; no closing aphorism; and-chains 6/9; em-dash 0 ✓.
- **Logic and fact (continuity INFO items left on the page):**
  - **L1** the hut pronouns: "His rush baskets … he had made a bed" follow a paragraph about Valens, but the hut and the bed are Mnason's ("the herdsman's bed", l.558; "The herdsman will want his bed", l.584).
  - **L2** "Further up." on the dust map.
  - **L3** ricotta does not squeak.
  - **L4** the Pentax "as it had hung all afternoon", after she bathed all over at the seep.
  - **L5** the film strip's length.
  - **L6** "two magistrates a year".
  - **C1** "Celer's chose a road for it." (a dropped noun; audit I-11).
- **Ledger:** approach ✓, open ✓, end ✓, breaks ✓, dialogue ✓, theme ✓, length ✓, gear ✓ (16 = floor).
  - **Outline beats 1–5 all on the page:** the bargain; the truth with the flashlight and camera; the day's work (milk, mules, Felix's questions, the unripe figs); the hut (elbows, a collapsing bed, laughter, the laugh stopping, her asides quiet, his stillness broken); night, with Felix asleep by the fire.
  - Chaos moments ✓ (Valens's figs at the worst moment; Mara's teeth at an inappropriate moment).
  - Beat subversion ✓ (no declaration of faith).
  - Writer warnings ✓: no purple, clinical or stacked metaphor; no temperature report; em-dash 0; the mule line once; no closing aphorism.

### The heat scene, judged on craft (l.514–596): **PASS**
- **Explicit and on-page, plain and adult.**
  - "I had him in my hand"; "I drew him into me, slowly, all of him"; "I came with my heel hooked behind his knee and a fistful of the fleece"; "He drove into me hard, and I wanted it".
  - No euphemism from §5's banned list. No clinical term. No metaphor-stacking: one comparison, "as a man learned a road he meant to take again at night", which is his axis seen through her and stays inside §5's one-per-scene. No temperature report: "which was worse, and better" and "it went through me" are both borderline and both acceptable.
- **Character-driven.** Every beat is one of them being themselves:
  - she wears the Pentax to bed ("I wear it to everything.");
  - he hangs it "with the lens turned to the wall";
  - she puts his belt out of reach "so that his hands would find no work in it" (his card's deflection, disarmed);
  - his reflex, "His palm was under my skull before the floor was";
  - her mender's act turns the comedy: she picks the bracken and grit from his skinned knuckles with her teeth, "and somewhere in that his laughing ran out";
  - his "Here?", her "Here.", and her hand guiding his. Consent is mutual and unambiguous.
- **Clumsy and funny before tender, exactly as ordered:** the roof poles, the chiton trapping her arms, the elbow in his eye ("That was my eye."), the fork splitting, the helpless shared laugh, "**I was watching the figs.**", and the teeth "held … against him".
- **Then tender:** "then they remembered themselves and were careful, which was worse, and better".
- **The voice behaves as §5 asks.** Her asides go quiet after "Here?". The senses widen into one long sentence (bracken smell, cut ends, draft, heat, grit, fire, the catch in both breaths: l.576). His stillness "left him, the whole of it at once".
- **After:** practical and funny ("He can have the end that's standing."; "Corinth has clerks."), then the quiet image.
- **What to fix is in the doubles, not the register:** "in my hair" ×3 (H3, H4), "and stayed" ×3 (H5), "had gone quite still" (H2), "somewhere" ×4 in the hut (P16, H1), the dentist's "man in a white coat" (P17), and "already growing back since noon" (H9, a tense slip, not the designed ugly sentence).
- **Bible sync:** the bible's heat block quotes "like a row of new tiles", which is no longer on the page (W-04 cut it). The page has no teeth comparison, so the scene's one comparison is the road.

---

## Character Chaos Check (Primary: Mara)
- **Irrelevant thought: PRESENT, inhabited.** The snowplow described to a ewe (l.62); the Energizer rabbit (l.132); the teeth at the worst moment (l.558); the leg hair at the seep (l.374).
- **Cognitive distortion: PRESENT, inhabited.** All-or-nothing, twice in action: "One print on that glass … and I might as well never look through it again." (l.254); "Inside that one look I decided it was pitch or nothing" (l.374).
- **Unprompted memory: PRESENT, triggered** (the cheese squeak → the Italian Market → back; the shins → the razor → back).
- **Failed emotional management: PRESENT.** The shiver in the dark cave (l.46); the hiccups through the bargain (l.300–328); the laugh (l.550).
- **Voice under pressure / heat: demonstrated.** Asides off, senses widened, sentences lengthened (voice-dna §5).
- **4/4, inhabited.** The one mediated sentence (l.178, the narrator explaining that the telling went badly) is F1.

## Secondary Character Chaos
- **Valens:** he looks at the cave so long she thinks nothing reached him, then asks about mules; "I was watching the figs."; his reflex under her skull. His own moments, not tools.
- **Felix:** "Would you cry, if it was me?"; flinching only when unwatched; the bitten green fig. His own moment.
- **Mnason:** the fig twig refused, the rennet "you'll know whose doing that was", the son's wife who counts his mouthfuls. His own moment.
- **Kallia** (backfill): the lie to the runner, "She ate more than she carried, that one, and broke two of my jars." Her own line.
- No secondary character is a mere function. No cap.

---

## The Tomorrow Test
**What the reader remembers:** a man with half his face shaved and a wet knife in his fist. He has just been told the woman he wants comes from nineteen centuries ahead. He looks at the cave so long she thinks it has all gone by him, then asks: "**Do they still have mules?**" And that night, the herdsman's bed giving way under them, his hand under her head before the floor, and the two of them laughing until they stop.
**Anchor type:** BOTH.
- IMAGE: the fingers lit red with the bones dark down the middle; the half-shaved face; the harvestmen; the palm under the skull; the lens turned to the wall; Felix's swollen lips and the bitten fig.
- QUOTE: "Do they still have mules?"; "Then I'll wait outside it,"; "The crowd was ewes."; "I was watching the figs."

**Verdict: ANCHOR EXISTS** (strong; +0.5 CVI).
**Type check:** a question that is really another question, set against Ch.11 (an animal's stillness), Ch.12 (an object in motion), Ch.13 (a recitation and a one-word reveal) and Ch.14 (a concealment). New to the book.

## The Shareability Test
"She finally tells the gladiator she's from 1998. Time travel, the cave, everything. He thinks for a long time and asks: 'Do they still have mules?' He doesn't believe a word of it, says he'll wait outside the door anyway, and that night the shepherd's bed collapses under them and they can't stop laughing." Running total: 15 chapters, 28+ shareable moments.

---

## Reader Reports

### The Devourer (7.7k after Ch.14's 3.0k)
- **Speeds up:** the cave's back wall and the spiders; the fig standoff; the flashlight in his hand; the mule question; the hiccups; "I'll wait outside it"; the juniper fight; the hut.
- **Slows:** S1's backfill ladder (the runner, Kallia, the loft, the cave) before the milking resumes the morning (l.14–l.50); the monk's arithmetic (l.172); Mnason's rennet speech; the supper paragraph (l.476).
- **Would they stop?** No. The noon section is the book's most propulsive talk so far, and the reader knows what the evening is for.
- **Last page:** the bitten fig is a laugh, not a hook. They turn the page anyway, for Corinth.

### The Critic
**Underlines:** the red fingers; "his own lashes in the glass"; "It keeps what it shows."; "her tail switching at his face and his face not caring"; "The crowd was ewes."; "Where he could see me looking he never flinched."; "with the lens turned to the wall"; "so that his hands would find no work in it"; "His palm was under my skull before the floor was"; "careful, which was worse, and better"; the ugly cheese sentence.
**Disappointments:**
- "*the thing in my hand he left to me*: a third fronted object, on a sample string" (P1);
- "*and then he was facing me*: the gaze arriving again" (P2);
- "*where the roof dropped and the floor climbed*: Ch.3's cave, re-walked" (P5–P7);
- "*somewhere* five times, three of them in bed" (P14, P16, H1);
- "*in my hair* three times, after Ch.12's forehead on her hair" (H3, H4);
- "*so that I seemed to answer him with it*: the joke explained" (F4).

### The Hostile
1. **Whose hut?** (l.516) "His rush baskets … he had made a bed" reads as Valens's, but the bed is "the herdsman's" (l.558, l.584) → **L1**.
2. **The dust map** (l.274–276): coming round from the heel, Pompeii lies before Puteoli. "Further up" is backwards (audit I-06) → **L2**.
3. **Ricotta squeaking** (l.452): fresh ricotta is soft and grainy. Mozzarella squeaks (audit I-08) → **L3**.
4. **The Pentax "all afternoon"** (l.536), after she bathed "all over" at the seep with her chiton on the rock (audit I-13) → **L4**.
5. **"a strip as long as your arm"** (l.242): a 36-exposure roll is about 1.6 m (audit I-09) → **L5**.
6. **"two magistrates a year"** (l.280): Pompeii elected two *duoviri* and two aediles (audit I-07) → **L6**.
7. **"Celer's chose a road for it."** (l.326): a dropped noun the reader has to supply (audit I-11) → **C1**.
8. **A hearing at Corinth** (l.306, l.326): canon puts the suit in Rome in spring 74 (ARCH-5). This is Valens's expectation, not a contradiction, but Ch.16 or Ch.21 must register the move (audit I-20; cascade).
9. **The lane hears Kallia's lie the day Mara is still in the house** (l.16): the lane's complicity is implied, and Ch.16 must know it (audit I-31). No change.
10. **A man and his "wife" all winter in the brother's house** (l.340): Ch.16–18's "yearning without sex" must read as no on-page heat, not chastity, and Ch.18's quay wedding needs a reason beyond the shipmaster (audit I-21). Cascade.

**Verdict:** "Four small fact slips, one pronoun seam, one dropped noun; no hole. The timeline (Bysios → the loft → May → July) and the flashlight's history both hold."

### The Casual Reader (airport, 10 pages)
- **Hooked at once:** they have waited fourteen chapters for this and they know it. The pasture at dawn is pretty, and then a stranger with a bandaged head is asking for "the tall foreigner" at the spring.
- **Feels it at:** the spiders letting go one leg at a time; his fingers glowing red; "Do they still have mules?" (they laugh out loud); the hiccup on "wife"; "I'll wait outside it" (they stop laughing); the boy fighting a juniper; the bed.
- **Gets a jolt from:** "Would you cry, if it was me?"
- **Frictions:** a page and a half of how-we-got-here before the day starts; the monk's arithmetic; the rennet.
- **Would they buy after 3 pages?** Yes. **Do they stay?** Yes, and this is the chapter they tell a friend about. **9.0/10.**
- **Not 9.5:** the front-loaded backfill, and a few literary sentences they skim (the opening spiral runs 120 words).

### The Devoted Reader (active: long saga)
**Will post about:**
- moonmilk and overwintering harvestmen;
- fig latex as rennet (*Iliad* 5.902) and the green fig's lip burn, paid off on Felix's mouth;
- Hero of Alexandria's temple doors;
- the diolkos as a harbor boy's rumor ("with the masts still in them");
- Dionysius Exiguus's four years;
- the Energizer rabbit against tiring batteries;
- the camera that "keeps what it shows … in the dark";
- "How will you know the door, among all those tombs?";
- "eight years on from this summer, and a few weeks over".

**Will catch:** Ch.3's cave re-walked and "into October" (P5–P7); the fronted object (P1); ricotta (L3); Pompeii before Puteoli (L2); "two magistrates" (L6).

---

## Cross-Reader Matrix
| Issue | Devourer | Critic | Hostile | Casual | Devoted | Severity |
|---|---|---|---|---|---|---|
| P1, P2, P9, H2 SPENT / CLOSED frames (fronted object, gaze "then", silence filled, "had gone … still") | | ✓ | | | ✓ | **SHOULD FIX → blocking** (law) |
| P3, P4 present tense in narration | | ✓ | | | ✓ | **SHOULD FIX → blocking** (voice-dna §0.4) |
| P5–P7 the cave in Ch.3's geometry and "into October" | | ✓ | | | ✓ | **SHOULD FIX → blocking** (the brief's named law) |
| P8, C7, P1 sample strings and image | | ✓ | | | ✓ | **SHOULD FIX → blocking** (voice-dna §6) |
| P14, P16, H1, P15 "somewhere" ×5 / "so that" ×7 | | ✓ | | | | INVESTIGATE → **fix** (a narrator habit forming; tic budget 0) |
| H3–H9 doubles in the union | | ✓ | | | ✓ | **SHOULD FIX** |
| F1–F6 #11 (under cap) | | ✓ | | | | INVESTIGATE → **fix** (margin; four chapters running the repair chain added glosses) |
| C2–C6 Valens register and hoof re-stage | | ✓ | | | ✓ | **SHOULD FIX** (card law) |
| L1–L6, C1 logic and fact | | | ✓ | | ✓ | **SHOULD FIX** (cheap) |
| S1 backfill before the day resumes | ✓ | | | ✓ (frictions) | | SHOULD FIX → **no change.** The cave is Valens's first sight of the flashlight and noon pays it; P5–P7 and P11–P12 trim it by about 40 words. Cutting the scene would move the truth-telling's trigger off the page. |
| Laugh as the emotional channel again | | ✓ | | | | INVESTIGATE → **no change** (outline-mandated; new shape, shared) |

---

## Revision Recommendations (Ranked)
*All 45 strings below were applied together to a scratch copy and run through `check_chapter.sh 15`, `shape_check --strict` and `tic_report.py --gate`: all clean, echo 0. Strings that tripped a gate on my first tries are listed under "Do not use".*

| # | Location | Problem type | What happens now | Why it fails | Revision direction (exact) | Project rule? |
|---|---|---|---|---|---|---|
| L1 | l.516 | Logic | "His rush baskets hung in a row from pegs, … At the back he had made a bed" | The pronouns follow a Valens paragraph; the hut and the bed are Mnason's. | → "**Mnason's** rush baskets hung in a row from pegs," (the following "he" then resolves) | No |
| L2 | l.276 | Factual | "Further up. There." | Coming round from the heel, Pompeii lies short of Puteoli. | → "**Short of that.** There." | No |
| L3 | l.452 | Factual | "passed me ricotta across his counter" … "it had squeaked the same" | Ricotta does not squeak. | → "passed me **a knot of mozzarella** across his counter" | No |
| L4 | l.536 | Logic | "the Pentax hung as it had hung all afternoon." | She bathed at the seep that afternoon. | → "…all **evening**." | No |
| L5 | l.242 | Factual | "on a strip as long as your arm." | A 36-exposure roll is about 1.6 m. | → "on a strip **as long as you are tall**." | No |
| L6 | l.280 | Factual | "They elect two magistrates a year and paint" | Pompeii elected four. | → "They elect **their magistrates every year** and paint" | No |
| C1 | l.326 | Voice / clarity | "Celer's chose a road for it." He picked the thyme from his teeth | A dropped noun; the third "picked" removal gesture. | → "**Celer's men** chose a road for it." He **took** the thyme from his teeth | No |
| C2 | l.344 | Voice (card) | "Delphi's put you on a boat. Leave yourself on it." | An idiom; his Part One Greek is "flatly literal, without idiom". | → "**Delphi thinks you're on a boat. Let it.**" | No |
| C3 | l.288 | Voice (card: no comparison) | "With the light, and the box with the eye in it." | A kenning: the lens as an eye. | → "With the light, and **the box you look through**." | No |
| C4 | l.274 | Voice (bleed) | "Neapolis I know of. Puteoli." | Mnason's fronted-object fingerprint in Valens's mouth, in the same chapter. | → "**I've heard of Neapolis.** Puteoli." | Yes: "a fronted object in speech belongs to the card that owns it" |
| C5 | l.366 | Voice (forming shape) | "Then I'll wait outside it," / l.510 "Then I'll believe it," | The same four-word skeleton closing two sections. | → "**I'll wait outside it,**" he said. (flatter; "Then" speech openers 2 → 1) | No |
| C6 | l.440 | Character (card) + reuse | "Valens had the black's near fore up across his thigh by then and was paring at it, and he kept on paring." | His hands on the same hoof twice (l.8); re-stages Ch.11's paring; "kept on [-ing]" echoes Ch.14's "I kept on holding it." | → "Valens was **splitting pine at the woodstack** by then, **with his back to the pair of us**." ("I saw the juniper," now lands harder: he saw it with his back turned.) | No |
| C7 | l.530 | Style (sample-10 image) | "Mnason built it to fit Mnason," he said. | sample-10's dwelling sized to "one small shepherd". | **Delete the paragraph.** "Mind the roof," I said, too late. stands as the beat. | No |
| F1 | l.178 | Style (#11) | "He waited, and I, who had begun with a monk's mistake and could not see how to get from there to anywhere, did the sum aloud, and that was worse still." | The narrator tells us the telling is bad; the speech already shows it. | → "**He waited, and I did the sum aloud.**" | No |
| F2 | l.184 | Style (#11) | "and told him the rest in one go, to have it out before he could stop me." | Motive tail. | → "and told him the rest in one go." | No |
| F3 | l.296 | Style (#11 + #3 + para-final negation) | "He had heard all of it, the count, the cave, the door in the town, and put it away as Kallia put away a lodger's tale…; I had not thought he would be kind about it." | A triad recap, then a gloss interpreting the simile. | → "**He had heard all of it and put it away as Kallia put away a lodger's tale of a sister who married a magistrate.**" | No |
| F4 | l.328 | Style (#11) | "The hiccup took me exactly on the last word of it, so that I seemed to answer him with it." | It explains the joke. | → "The hiccup took me exactly on the last word of it." | No |
| F5 | l.514 | Style (#11) | "his face to the dark of the plateau, which was the way up to us for anybody coming," | Ch.12 planted it ("Up there you see a man coming a whole morning off"). | Cut the clause. | No |
| F6 | l.234 | Style (#11, borderline) | "I wore it next to my skin still, though up here nobody would take it, and it had rubbed" | A rationale clause; brings the strictest borderline count to the cap's edge (≤0.8). | → "I wore it next to my skin still, and it had rubbed" | No |
| P1 | l.44 | Style (CLOSED frame + sample-05 4-gram) | "while I held it there; the thing in my hand he left to me." | A third narrated fronted object (the pair is kept; "no third"); "thing in my hand" is sample-05's. | → "while I held it there, **and he left the light to me.**" | Yes: gate `^[^".]*\b(the \w+ (in\|on) my \w+\|this question\|to that)\b[^.]{0,30}\b(he\|she\|I) (left\|gave\|asked)` as a fronted-object detector |
| P2 | l.188 | Style (SPENT gaze arrival) | "until I thought he had not understood one word, and then he was facing me." | The "looked at me then" family is SPENT. The question lands harder while he is still looking at the cave. | → "until I thought **it had all gone by him**." (no negation added) | Yes: add `\band then (he\|she) was (facing\|looking at) me\b` to the C2 regex proposed in Ch.14 |
| P3 | l.28 | Style (present tense; spent vehicle) | "so that the whole plateau ticked and trickled like a kitchen when the heat comes on in a cold house." | Narrating present; the third heat-in-a-cold-home image (Ch.1 heater, Ch.13 SPENT). | → "**and all of it** ticked and trickled." | Yes: gate present-tense verbs inside narration similes (`like a \w+ when [^.]*\b\w+s\b`) |
| P4 | l.128 | Style (present tense) | "and it weighed about what a hen's egg weighs." | Narrating present. | → "and it weighed **about as much as** a hen's egg." | No |
| P5 | l.32 | Style (the cave in Ch.3's words) | "The daylight went farther in than I had ever seen it go, with the snow at the mouth throwing it in. … far in, where the roof dropped and the floor climbed to meet it, the dim gave out," | Ch.3 l.121's floor-climbs / roof-comes-down order, and Ch.3 l.161's light reaching far in. | → "**The snow at the mouth threw the daylight in behind us.** Valens followed with a pine he had not troubled to light, and **farther in**, the dim gave out," | No |
| P6 | l.34 | Style (Ch.3 descriptor) | "I shone it along the crack, whose far end had always been black to me." | Ch.3 l.123 "Beyond the bend the beam ran on into black." "Did it ever go on?" / "Once." carries the contrast. | → "I shone it along the crack." | No |
| P7 | l.186 | Style (Ch.3's last line) | "and I crawled out of it into yours, into October," | Re-says "I stepped out into October." | → "…into yours, **in the autumn**," | No |
| P8 | l.476 | Style (sample-06 4-gram) | "and the dark rose on the plateau like water in a basin filled from below, until only the summit" | "water in a basin" is sample-06's; the simile is not needed. | → "and **the plateau filled with dark**, until only the summit" | No |
| P9 | l.494 | Style (SPENT device) | "Valens laid a root of juniper on the embers and watched it catch." | A held silence filled by something moving, just before "You do not believe a word of it". SPENT, 0 more. | → "Valens laid a root of juniper on the embers." | No |
| P10 | l.476 | Style (#16 generic "you"; #1) | "the wild greens … which were bitter in a way that grew on you, and a little of the wine from the skin, which did not." | Generic-you maxim in narration. | → "the **bitter** greens … **which I had come round to**, and a little of the wine from the skin, **which I had not**." | No |
| P11 | l.24 | Style (para-final negation; double with l.50) | "and we climbed with nothing said between us that was not about the path." | l.26 shows it; l.50 says it again on the way down. | → "and we climbed." | No |
| P12 | l.46 | Style (#10 metacognitive) | "and I waited to see what I would feel about it." | It announces the feeling the shiver then delivers unannounced. | → "and I waited." | No |
| P13 | l.128 | Style (double; Ch.14) | "The flashlight lay in the bag in the hut, uppermost, as it had ridden since spring." | "uppermost" at l.30 and in Ch.14 l.26. | → "The flashlight lay **on top of everything in my bag** in the hut, **where** it had ridden since spring." | No |
| P14 | l.368 | Style ("somewhere"; ended-unnoticed move) | "My hiccups had gone, somewhere in the course of it." | The same move as l.560 and Ch.6's "could not have said when it was gone". | → "**My hiccups were gone.**" | Yes: cap narration "somewhere" at 2 per chapter |
| P15 | l.300 | Style ("so that" reflex) | "I hiccuped, out of nowhere, so that my shoulders jumped." | Result-clause habit (7 in narration). | → "…out of nowhere, **and** my shoulders jumped." | Yes: WATCH narration "so that" > 4 per chapter |
| P16 | l.532 | Style ("somewhere") | "and somewhere at the top the cloth caught on itself" | | → "and at the top the cloth caught on itself" | No |
| P17 | l.558 | Style (repeated introduction shape) | "still paid a man in a white coat to scold me twice a year," | "a man in a paper hat" four lines up (l.452); "Men in hats" (l.196). | → "still **paid to be scolded** twice a year," | No |
| H1 | l.550 | Style ("somewhere", "so that") | "It started somewhere low in him … and shook the poles under us so that more of the bed gave way," | Both reflexes in one sentence. | → "It started low in him and went on, helpless, and shook the poles under us; more of the bed gave way, and that set us off harder." | No |
| H2 | l.562 | Style (CLOSED family) | "and he had gone quite still." | "had gone quiet" CLOSED at 2. | → "and he **was** quite still." | Yes: extend the CLOSED entry to `had gone (quite )?(quiet\|still)` |
| H3 | l.580 | Style (Ch.12 SPENT; triple) | "with his arm across me and his face in my hair." | "in my hair" ×3; Ch.12's forehead on her hair is spent. | → "…and **his cheek on my shoulder**." | No |
| H4 | l.590 | Style (triple) | "he asked, with his mouth in my hair, \"do they" | as above | → "he asked, \"do they" | No |
| H5 | l.596 | Style (triple "and stayed") | "His arm went heavy across me, and stayed heavy." | "and stayed" at l.576 and l.578. | → "His arm went heavy across me." | No |
| H6 | l.542 | Style (double) | "His tunic came off and landed by the cheese baskets," | "beside the cheese baskets" one sentence earlier. | → "His tunic came off, and he was very large" | No |
| H7 | l.544 | Style (double) | "the fork at the head of the bed, which had borne me since we came up, split" | l.516 "all summer it had held me". | Cut the clause. | No |
| H8 | l.536 | Style (triple "breastbone") | "on its strap, against my breastbone, the Pentax hung" | ×3 (l.234, 536, 542). | → "on its strap, **between my breasts**, the Pentax hung" | No |
| H9 | l.570 | Grammar slip | "His beard was already growing back since noon," | A tense collision, not a designed ugly sentence (the chapter's ugly sentence is the cheese). | → "**His jaw had roughened again since noon**," | No |

### Fix order: Logic/fact (L1–L6, C1) → Character (C2–C7) → #11 (F1–F6) → Book law (P1–P17) → Heat doubles (H1–H9)

**Kept on purpose (and why):**
- **The opening spiral, byte-identical.** Its double anadiplosis ("behind the bells came the cold … behind the cold came the thyme") is the ledger's long sensory sentence; audit I-45 passed it.
- **The cave scene itself** (l.22–l.50): it is the flashlight's first sighting, and noon's "The light in the cave," pays it. Only its Ch.3 words go (P5–P7).
- **"somewhere in that his laughing ran out"** (l.560, the outline's "the moment the laughter stops") and "lost count of my month somewhere around October" (l.572).
- **"so that his hands would find no work in it"** (l.542): a #11 borderline, kept as one of the chapter's best lines.
- **The road comparison** (l.570): the scene's one comparison, inside §5.
- **"As man and wife." said twice across speakers** (l.326, l.330): designed.
- **The noon Q&A run** (#17 minor): outline-mandated practical questions, interleaved with the shave.
- **"which was worse, and better"** and **"it went through me"**: borderline temperature, acceptable (audit I-44).
- **Felix's "I'm not tired" before sleep** (l.490): stock, but his.
- **The Alexandrian temple door** (l.258): a literal precedent, not a comparison.

**Do not use** (each tripped a gate on my first try):
- "a long way in" (tic gate: "a long way" 3× book-wide, Ch.2, 4);
- "came off over his head" (tic gate: "over his head" 3×, Ch.5, 11);
- "every word of it" (echo, Ch.2);
- "from the bottom up" (echo, Ch.12);
- "the plateau from" (echo, Ch.3);
- "he asked, without lifting his head" (echo, Ch.3 "he asked without");
- "while he talked" (echo, Ch.11);
- "By the end of it" (echo, Ch.2).

---

## Strengths to PRESERVE (do not touch in polish)
1. **The first sentence, byte-identical** (the `long-spiral` sig), and "The summit took the sun first and held it, gold, while everything under it was still blue."
2. **Kallia's lie** (l.16) and "folding each thing smaller than I would have folded it" (l.18).
3. **The harvestmen** coming apart "unhurriedly, one leg at a time" (l.34); "Did it ever go on?" / "Once."; the shiver "hard enough that he heard my teeth".
4. **Mnason entire:** the gap, "Talk to her … Sad, she holds it back."; the torn-ear ewe; "One twig." / "It would."; the rennet speech; "Your man's shaved,".
5. **The flashlight on his palm** (l.128–l.152): the red fingers, the rabbit, "It's not warm," / "It never is.", "Don't burn it, then,".
6. **The half-shaved face** (l.168), the knife still wet (l.184), and **"Do they still have mules?" byte-identical, with its run of practical questions** to "That's true, then."
7. **The camera:** "his own lashes in the glass"; "It keeps what it shows."; the wrist turned aside from the dented rim; "One print on that glass…".
8. **The bargain and the hiccups**, and "Because there I know where everything is kept." / "I'll wait outside it,".
9. **The seep and the legs** (l.374), "pitch or nothing".
10. **Felix:** the Isthmus questions, "The crowd was ewes.", "The juniper won.", "Would you cry, if it was me?" / "Only a little," … "Not in front of everybody."; "Where he could see me looking he never flinched."
11. **The cheese at sundown,** and the ugly sentence.
12. **"You do not believe a word of it"** through "Then I'll believe it,".
13. **The hut:** the roof poles, the chiton, "That was my eye.", the Pentax to the wall, the belt, the fork, the palm, the laugh, the figs, the teeth, the knuckles, "Here?" / "Here.", the careful hands, the long senses sentence, and the stillness leaving him.
14. **The after and the close, byte-identical:** "He can have the end that's standing."; "Corinth has clerks."; the last paragraph, Felix and the fig.

---

## PATH TO 8.5 (mandatory; the Floor is 8.0)

**Prose & Voice 8.0 → 8.5 requires:**
- **The book-law cluster cleared:**
  - P1 (the third fronted object, on a sample string);
  - P2 (gaze "then");
  - P3 and P4 (present tense in narration);
  - P9 (a silence filled by a fire);
  - H2 ("had gone … still").
- **The cave re-entered in fresh words:** P5–P7, so that Ch.3's floor-and-roof geometry, its light reaching far in, its "black" beyond the bend and its "into October" all go.
- **Sample strings out:** P1 (sample-05), P8 (sample-06), C7 (sample-10).
- **The forming narrator habits broken:** "somewhere" 5 → 2 (P14, P16, H1); "so that" 7 → 3 (P3, P15, F4, H1).
- **The doubles in the union cleared:** H3–H8; H9 corrects the tense slip.
- **#11 margin:** F1–F6 take it from 5 firm (0.65/1k) to 0 firm (borderline ≤0.8/1k at the strictest).

The stopping sentences, the underlines, the ugly sentence and every anchor stay. **The single highest-value set is P5–P7.** It is the brief's named law (the cave in its Ch.3 words), and the fix is three short swaps that cost the scene nothing.

**Characters 8.5 → 9.0 (expected with C1–C7):** Valens's register made literal (C2, C3), Mnason's syntax returned to Mnason (C4), the "Then I'll" pair broken (C5), and his hands on a new object, with his back turned as the courtesy (C6).

**Apply in this order; the strings are exact (see the table), or run the tested script:**
```
python3 /tmp/claude-0/-home-user/63791ee5-159c-5791-9429-07920f8d9417/scratchpad/ch15-eval-fixes.py \
  books/the-hour-of-ash/manuscript/chapters/chapter-15.md \
  books/the-hour-of-ash/manuscript/chapters/chapter-15.md
```
Run it from /home/user/Books. It asserts one match per string and aborts, writing nothing, on any miss. Then run `bash books/the-hour-of-ash/tools/check_chapter.sh 15` and `python3 tools/shape_check.py books/the-hour-of-ash --strict`, and update the chapter's word-count HTML comment (l.4). The swap harness used for the test is `ch15-eval-swaprun.sh` in the same scratchpad; it always restores the original.

**What the tested run produced (all 45 strings applied together; fixed copy sha256 `738dc991…`):**

| Measure | Before | After |
|---|---|---|
| Words (shape_check) | 7,719 | **7,507** (floor 7,300 ✓) |
| Words (style_check / `wc -w`) | 7,730 / 8,037 | 7,518 / 7,825 |
| Dialogue | 33.6% (show/tell) / 34 (shape) | **34.4% / 34** (30–40 ✓) |
| Median sentence | 16 | **16** (floor 16 ✓) |
| Breaks / signatures | 3 / `long-spiral` → `quiet` | unchanged |
| First sentence / mule line / last paragraph | | byte-identical |
| `check_chapter.sh 15` | clean | **all clean**: style (simile 0.3/1k, em-dash 0, foreshadow 0), grammar 0, rhythm 0, show/tell no flags, voice-wear strict clean, tic gate clean (and-chains 7/9), echo 0, command echo none, metaphor 1.2/1k |
| `shape_check --strict` | CLEAN | **CLEAN** |
| #11 (firm) | 5 (0.65/1k) | **0** |
| Paragraph-final negations | 10 (1.30/1k) | **8 (1.07/1k)** ✓ |
| Present tense in narration | 2 | **0** |
| SPENT / CLOSED frames on the page | 5 | **0** |
| Narration "somewhere" / "so that" | 5 / 7 | **2 / 3** |
| Voice-bank 4-grams | 2 | **0** |
| Anti-AI | 10/20, −1.75 (watch) | **7/20, −1.125** (clean band) |

**Expected:** Prose 8.5 (merit 8.0 → 8.5 on 45 cited changes, inside the +0.5 limit) and Characters 9.0 (8.5 → 9.0 on C1–C7) → **Floor 8.5, Average 8.86** (9.0 / 9.0 / 9.0 / 8.5 / 8.5 / 9.0 / 9.0). Casual 9.0 holds. CVI-L 9.8 holds.

---

## Pacing check (one line for `feedback/progress.md`)
Ch.15 (cycle 0) · Chronological *day-in-full*, between Ch.14's Fragmented and Ch.16's Parallel ✓.
- **Length:** 7,719w (target 7,800, −1%; 7,507 after the PATH, ≥7,300). **Book:** 82,843 against 88,800 cumulative (−6.7%). Projected about 243k against the 220k floor ✓ and 245k target (slightly under: watch).
- **Dialogue** 33.6% (30–40 ✓); **3 breaks** ✓; **gear median 16**: the ledger's high floor, with narration alone at about 20. Up from Ch.14's 12 and Ch.13's 14, as planned.
- **Neighbours:**

  | Ch | Words | Gear (median) | Dialogue | Approach |
  |---|---|---|---|---|
  | 13 | 7,503 | mid (14) | 38% | Parallel |
  | 14 | 3,003 | low (12) | 5% | Fragmented |
  | **15** | **7,719** | **high (16 / narration 20)** | **34%** | **Chronological** |
  | 16 | 7,600 planned | mid | 40–50% | Parallel |

  **A long high-gear day after a short low-gear night:** the night held its breath in shards and nine breaks; this day talks, and closes in a bed. The variance is the design ✓.
- **Signatures:** `long-spiral` / `quiet`; no three running (Ch.13 `dialogue`, Ch.14 `long-fade`).
- **Emotional slot ✓:** after Ch.14's private dread, this is the romance turn. The truth comes out, it is disbelieved, they strike the bargain and become lovers. The emotional temperature rises from the coldest chapter to the warmest.
- **Value shift ✓:** − (alone with it) → ± (told, not believed) → + (bargain) → + (lovers). The pull is soft and real (Corinth in autumn; the bitten fig), as a `quiet` row allows.
- **Slow patch:** S1's backfill ladder before the morning resumes. It is load-bearing (the flashlight's first sighting), and the PATH trims about 40 words from it.

**Verdict: OK.**

---

## Cross-Book Pattern Detection (Ch.1–15)
1. **Revisited places come back in their old order.** The bible's rule ("grep the paragraph of its last visit and reuse none of its descriptors") was obeyed for Ch.6/8's spent words. Ch.15 then rebuilt Ch.3's *sequence* (light fails → floor climbs → roof drops → flashlight) in synonyms, and borrowed Ch.3's closing line. **The rule should name sequence and geometry as well as descriptors.** Next at risk: Ch.19's tomb road, and Ch.41–42's tomb. *(Pipeline, UPDATE RULE: book-writer and continuity-guardian prompts.)*
2. **The narrator's small connectives become the tic once the big ones are gated.** With "So", "Then / After that", "before I had", negation pivots and "Whoever … had" all gated, the reflex moved to "somewhere" (an ending unnoticed) and "so that" (a result clause). Both are regex-able. Add a narration cap for `\bsomewhere\b` (2) and a WATCH for `\bso that\b` (>4) to `tic_report.py` at the root.
3. **Present tense leaks through similes.** Both Ch.15 instances sit inside a comparison's vehicle ("when the heat comes on", "what a hen's egg weighs"). The Ch.13 rule named "the way a X does"; widen it to any present-tense verb after `like a` / `what a` in narration.
4. **Continuity INFO items that are facts should be applied, not left.** Ch.15's audit flagged ricotta, the map, the magistrates, the strip and the hut pronouns as optional; the repair took only the WARNs; and the Hostile and Devoted readers catch every one. Proposal: a continuity INFO tagged *factual* or *pronoun* is applied with the WARNs.
5. **What varies, as it should:**
   - the structure (Chronological after Fragmented);
   - the opening (`long-spiral`) and ending (`quiet`);
   - the gear (back up to high);
   - the dialogue share (34% after 5%);
   - the anchor type (a question that is another question, new);
   - the body-rebel channels (a shiver, hiccups, the shared laugh, his stillness, the first unmanaged pleasure).

**Bookkeeping (orchestrator):**
- **Re-sync the bible's "At-risk after Ch.15" block to the final page.** It still quotes the Writer's draft:
  - "Was it ever further?" (page: "Did it ever go on?");
  - "Then don't burn it";
  - "a door that is only a picture of a door" (not on the page);
  - "No shipmaster takes on a woman alone…" / "At the gangway.";
  - "It's lower than me";
  - "like a row of new tiles" (cut by W-04);
  - "as a man learns a road he means to take";
  - after the PATH: "Delphi's put you on a boat. Leave yourself on it." → "Delphi thinks you're on a boat. Let it."; "Then I'll wait outside it," → "I'll wait outside it,"; "Mnason built it to fit Mnason" cut;
  - counts 7,914 / 30.3% → the final page's.

  Also sync the MNASON card (audit I-35) and voice-dna §5's Ch.15 period-material cell (the forked-stake pole bed, not "olive-wood rope bed"; audit I-40).
- **At-risk after Ch.15, add (post-PATH):**
  - narrated fronted objects: 2, CLOSED, zero tolerance (the third was l.44);
  - "somewhere" in narration: cap 2 per chapter;
  - "so that" in narration: WATCH >4;
  - "had gone (quiet|still)": CLOSED;
  - "in my hair" for Valens's head or mouth: SPENT with Ch.12's forehead; Ch.23 and Ch.34 find another place;
  - "Then I'll [verb] it" in Valens's mouth: 1 used;
  - the black's near fore: rest it as Valens's business;
  - a revisited place's sequence and geometry, not only its words.
- **Cascades:**
  - W-12: outline Ch.16's Delphi farewell must be re-staged as covert, with the himation given by refusal. The outline already carries this.
  - I-20: Ch.16 or Ch.21 registers why the suit moves to Rome.
  - I-21: Ch.18's quay wedding needs a reason beyond the shipmaster, and Ch.16–18's "yearning without sex" means no on-page heat, not chastity.
  - I-34: Ch.19's "fine mountain for vines" must not read as Valens quoting l.272's "a mountain they grow wine on".

---

## VERDICT
**POLISH. Gate NOT MET.**

| Measure | Result |
|---|---|
| Genesis Floor | **8.0** (Prose & Voice, merit; no cap) |
| Average | **8.71** |
| Casual | **9.0** |
| Pacing | **OK** |
| CVI-Launch (CVI-L) | **9.8** |
| CVI-Legacy | 7.1 (provisional) |
| Mechanical suite | all clean (echo 0, tic gate clean, voice-wear strict clean, shape CLEAN) |
| Foreshadowing / own outcome narrated | **0 / never** ✓ (AD 79 once, as a present thought) |
| Truth told badly, without Pompeii's fate | ✓ |
| "Do they still have mules?" | once ✓ |
| The bargain | ✓ (and the Ch.14 plan's change registered) |
| HEAT 1 | **PASS on craft** (explicit, character-driven, clumsy and funny before tender; no purple, clinical, stacked metaphor or temperature report) |
| Memory triggered by the scene (CP2-2) | ✓ (two clauses; no longer memory) |
| Explanation-density cap | ✓ (5 firm at 0.65/1k) → 0 firm after the PATH |
| Paragraph-final negations | 10 (1.30/1k) ✓ → 8 (1.07/1k) |
| No comparisons in Valens's speech | ✓ (two register slips, C2 and C3) |
| Tics | verbal 0; gate classes clean; **SPENT / CLOSED frames 5 → 0; "somewhere" / "so that" forming → broken** |
| Present tense in narration | **FAIL ×2** → 0 |
| Reuse (the cave in Ch.3's words; samples; Ch.12's hair) | **FAIL** → cleared |
| Ledger | ✓ on every hard field |
| AI patterns | 10/20 (watch band) → 7/20 (clean band) |

**Failing dimension:** Prose & Voice (8.0 on merit). The fixes are surgical and were tested together: L1–L6, C1–C7, F1–F6, P1–P17, H1–H9 (45 strings). The result is 7,507 words, dialogue 34%, median 16, every gate clean, and the first sentence, the mule line and the last paragraph unchanged. Then run E (gates) and F (re-evaluation). **Expected after one cycle: Floor 8.5 / Average 8.86 / Casual 9.0 / PASS.** Ch.15 is the third review checkpoint, so the loop stops after it is finalized.

The chapter does what fourteen chapters were built for. She tells him the truth as badly as a frightened person would, starting from a monk's arithmetic. He looks at the cave for a long time with half his face shaved and asks whether they still have mules. He believes the light and nothing else, and says he'll wait outside the door. That night the herdsman's bed gives way, his hand is under her head before the floor is, and the laughing is the tenderness, exactly as the outline asked. What holds it below the gate is small and countable: a narrator walking back into Ch.3's cave in Ch.3's order, a handful of the book's closed frames in new clothes, two present-tense verbs, and the same few words repeated in the bed.

**BIAS CHECK:** This evaluation was produced by the same system that wrote the prose. Confidence in scores above 8.0 requires external validation (beta readers, editors, comp analysis).
- **The cave finding is a judgment about sequence, not strings.** The gates found no echo. A reader who holds that "the floor climbed" is simply where a cave goes would score P5 as polish, not law. The brief named "the cave in its Ch.3 words", and l.32 rebuilds Ch.3 l.121's order and l.161's light, so I count it.
- **The #11 count is a judgment.** Five are firm by the standard that counted Ch.14's purpose tails. Seven more are borderline. Counting all twelve would put the chapter at 1.55/1k, over the cap, and cap Prose at 7.5. I do not count them: several are the dry aside the voice is built on (l.450, l.378). F1–F6 clear the firm five and the most rationale-like of the rest either way.
- **Characters 8.5 → 9.0 is my forecast, not a score.** It assumes C1–C7 land as written. A re-evaluator may hold 8.5 on Valens's talk volume in this chapter (the most he has spoken anywhere before Ch.34).
- Originality, Theme, Emotion and Immersion at 9.0, Casual 9.0 and CVI-Launch 9.8 are one-chapter judgments by the system that wrote the book.
