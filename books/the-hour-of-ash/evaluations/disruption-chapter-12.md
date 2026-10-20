# Disruption Report: Chapter 12 — The Kirrha Road (run 2)

**Verdict on the input: a strong chapter.** The fight is fast and ugly, the cap sentence holds the anchor, and
Valens's shaking at the fall lands as the surprise. The telling is flat and broken up by work. Mara asks no
questions. The chaos is already present: Felix's "Who gets his knife?", the crust lie, Spicula, the green darn and
the onion memory. The ugly sentence is in place. What weighed it down was **stage business repeated in varied
wording**:
- people turning round and looking back;
- Valens handing Mara things;
- Felix's fist;
- the goat "across his neck" twice in one paragraph;
- a cloak-washing run that included a work-suspended tell.

There were also two narrator pointers and the required "without looking in it" cut. This was a **light pass: the
gesture pre-pass plus 4 operations, all narration-only.** No speech words were cut. Dialogue rose because
narration fell.

**Backup:** the hook-craft output (md5 `0406055d…`, matching hook-craft's report) is in
`manuscript/reports/chapter-12-pre-disruption.md`. It is kept outside `chapters/` because the gates glob
`chapter-*.md`.

**What did not change:**
- The first line, "Lupus? By the Twins, it is. Lupus, walking behind mules.", and the final line, "A cart had
  stopped beside the ditch.", are byte-identical. So is the panorama before the final line.
- The fight is untouched from the knife to "The man in the brown cloak stayed in the ditch.", including the
  cap sentence and "and then nobody was".
- The shaking at the fall is untouched.
- The ledger shape holds: 2 breaks, `dialogue` → `punch`, median sentence 10 (gear low).

| Measure | Before | After |
|---|---|---|
| Words (shape_check) | 5,083 | **4,946** |
| Words (`wc -w`, incl. headers) | 5,262 | **5,125** |
| Dialogue share (shape_check / show_tell) | 26.2% | **27% / 26.9%** (band 25–35) |
| Median sentence | 10 | 10 |
| Breaks | 2 | 2 |
| Simile /1k | 1.0 | 1.0 |
| Em-dashes | 0 | 0 |
| And-chains | 5 | 5 |
| Bare "No." | 2 (Valens 1, Mara 1) | 2 (Valens 1, Mara 1) |
| Echoes | 0 | **0** |

## Pre-pass: NO-TICS gesture scan (mandatory; counted by hand, since the gate's regex sees only 3 handling hits)

| Class | Before | After | What changed |
|---|---|---|---|
| **Turning round / facing about** | 4 (Mara twisted round, Felix "turned round", Valens "faced about", Valens "shifted round") | 2 | Cut Felix's "and turned round": "He dragged a forearm across his mouth." now runs straight into his gray face. "He faced about, toward the sea. Far below…" became "Far down toward the sea, where the olives ended…". Kept: the twist in the hostage grip (the fight), and Valens shifting to hide his hands (the anchor). |
| **Looking back along the road** | 4 (Felix "head twisted back, looking"; Valens "every little way his head came round … to the olives where the two had gone"; the walkers' boy; Valens "half turned about" on the climb) | 2 | "Felix went." now stands alone. The walk to the ford is now "Valens came behind me with the last mule, at her pace." Kept: the boy and the goat, and Mara's two glances on the climb, which set up "You need not take it in". Valens's vigilance is still on the page at "He was looking up the slope into the olives." |
| **Valens's gaze on Mara** | 4 (ran his eyes over her; "watching me do it"; "Then it was my neck he was looking at"; "Valens looked at me" at the goat pen) | 2 | At the pen: "Valens left it to me, and I paid it myself" (the act, not the look). The neck: "He had you by the cloak." shows where he is looking, so the gaze sentence and its mid-paragraph "Then" are cut. Kept: the check for cuts, and the watching while she wrings the cloak. |
| **Valens hands Mara or Felix a thing** | 4 (pouch, cloak, purse, water skin) | 3 | The water skin: "Valens had left the string for the bank. Felix had the water skin off the last saddle; he drank…". The pouch return is restaged (see op 5). |
| **Sitting down** | 4 (Mara on a rock, Valens on the lip, Felix on the bank, Mara "sat on the stones at the edge of the ford") | 3 | "At the edge of the ford I washed the oil off my foot…" |
| **Cloak-washing beats inside the telling** | 5 in ~600 words, including **"My hands stayed in the cloak."**, a work-suspended tell (Ch.11 FINAL at-risk: any further instance, for anyone, is a defect) | 3 | Cut "My hands stayed in the cloak." and "I worked another handful of gravel into it." The darn paragraph now ends on the green thread, which is Mara's chaos noticing. The dowry-share and flogging speeches are joined into one 4-sentence Valens paragraph: "…Her father had given plenty with her. They flogged me in his courtyard…". The active beat "I held the cloak down in the fall, and the water went through it." now sits after "They'd been shown where to stand." Kept: pushed under with gravel, held down, wrung and spread. |
| **Felix's fist** | 5 | 3 | "…and Felix's fist was empty" (a pointer back to the fight's "fist open and nothing in it") became "She had found the barley he dropped in the road and eaten every grain of it while we were busy." "and his fists full of her legs" is cut, because it re-said the line above it. Kept: the fist and barley in paragraph 2 (one sentence) and the legs "in one fist… in the other". |
| **"across his neck" / goat on the shoulders** | 4, including 2 "across his neck" in one paragraph | 3 | "At a hairpin under a wild fig he waited for me, red in the face under her." |
| **Camera lifted and lowered** | "I lifted it and looked it over" … "and lowered it"; "hung on its strap" twice in 16 lines | 0 lift/lower | "The camera hung against the front of my himation. I looked it over." / "In the finder the plane trees stood upright and in focus." |

Unchanged and already at 0: nods, swallows, sighs, "a (long) moment", bends/stoops, kneel/crouch/squat. Gate gesture
layer: clean. Book-wide classes are unchanged (bend 15, kneel 12, object handling 12).

## Operations Applied

| # | Operation | Location | Before → After (brief) |
|---|-----------|----------|----------------------|
| 7 | **Missing Paragraph** (narrator pointer) | after the Pentax backstory | Cut "Valens had seen it in the road. He had looked at it once." The road beat ("across the camera in my arms, and off it") already showed it. "Nobody was supposed to see it." now leads straight into "Is it broken?", and the question carries the fact that he saw. |
| 7 | **Missing Paragraph** (indifferent-nature beat) | after "Now," he said | Cut "The bird in the olives had not stopped." It was a call-back to the fight's three notes and a cousin of the SPENT held-moment-measured-by-indifferent-motion device. The fight's bird stays, as the senses narrowing to sound. |
| 3 | **Control-management cut** (a condition report, not a break) | the walk to the ford | Cut "My knees were all right. My hands were all right." It was an inventory under pressure (voice-dna §1: never a condition report) and the first two legs of an anaphora triad with the next sentence. The paragraph now opens on the failed management already there: "I could not make myself look toward the ditch again, and did not try." |
| 4 | **Precision / forward reach** | the camera at the stream | "and no filter would ever screw onto it again" → "and no filter would screw onto it now". The "ever … again" read as significance-tagging; it is now a present judgement on the object. |
| 5 | **Required recast: "without looking in it"** | the stepping stones | "At the stepping stones he put the purse in my hand. I gave him back his pouch, and he tied it on without looking in it." → "At the stepping stones I gave him back his pouch. He put the purse in my hand." The "without looking [X]" construction (Ch.1, 5, 7, 11) is gone, and nothing replaces it. The exchange is the trust act: her father's watch goes back to him, the dead man's money comes to her, and it is not glossed. "tied it on" also left the page, so there is no knot in Valens's hands. |

## Operations NOT Applied (and why)
- **Simile Surgery:** nothing to cut. 1.0/1k, and every one characterizes: the horse they had money on; "as the
  shepherds carried them"; the Calf-Bearer "if the Calf-Bearer had been twelve"; "the way a man asks a price".
  The only commentary clause is "a great distance for so small a thing", which sits inside the protected anchor
  sentence.
- **Irrelevant Thought:** skipped. The brief says Mara's unprompted memory must NOT appear. Valens's onion memory
  is the chapter's one triggered memory, and the green darn is her noticing (AUTHOR-CP2-2; no new memory of any
  shape).
- **Emotional Control Break:** skipped by design. The chapter's surprise is that Valens breaks and Mara holds. Her
  body-rebel channels are rested or retired: hands (rested), voice (retired until Ch.20), seat (used in Ch.11). Her
  failed management is already on the page in the strap wound until no strap is left, the camera she cannot let
  go of and the ditch she cannot look at.
- **Ugly Sentence:** already present ("The goat was heavy and he carried it."). Protected.
- **Negation Pattern Break:** no "Not X. Not Y." openers. Negation pivots are at 0.
- **Dialogue Mess:** already messy where it counts. Mara answers a different question each time ("I heard it." /
  "I was watching something else."), and "Three days" talks past her offer. Dialogue sits near the band floor, so
  I touched no speech.
- **Precision Deflation (general):** the numbers are story numbers: two drachmas, five years, two years, five
  against five hundred, three days. They stay.

## Strongest Disruption
**Cutting "My hands stayed in the cloak."** and thinning the cloak run. The telling had become a duet of his
sentences and her washing, beat for beat, and the stopped-hands line was the only place Mara reacted to the
accusation. That reaction was a capped tell, and it told the reader what to feel. Now "They'd been shown where to
stand." goes into the water going through the cloak, and the dowry share runs straight into the flogging with no
breath between. The flatness is now in the rhythm, so the account reads more like testimony.

## Risk Assessment
- **"Valens left it to me"** at the goat pen is slightly drier than "looked at me". It keeps the money-gap act
  (she pays herself) and drops the look.
- **The neck beat** loses its gaze sentence. "He had you by the cloak." / "I felt for it." still lands, because the
  line can only be about her.
- **Valens's watchfulness on the walk to the ford** is now carried only by "looking up the slope into the olives"
  before they move off, and by the climb ("walking half turned about"). The continuity audit should confirm that
  this is still enough vigilance after two men ran.
- **Bible sync (not edited here):** the Ch.12 at-risk block has stale lines.
  - "The pouch handed to her to hold, returned unopened: once." still holds; "unopened" is now implicit.
  - "My hands stayed in the cloak.", "Valens had seen it in the road…", "The bird in the olives had not stopped."
    and "My knees were all right…" are off the page.
  - Counts: object handling (gate) 3 → 3; Valens gaze-on-Mara beats 2; bare "No." 2; "without looking" 0 in Ch.12.

## Gates (run from /home/user/Books)
`bash books/the-hour-of-ash/tools/check_chapter.sh 12` is ALL CLEAN:
- style (simile 1.0/1k, em-dash 0, foreshadow 0)
- grammar 0
- rhythm 0
- show/tell
- voice-wear (strict)
- tic gate, including the gesture layer and hinge/So/before-I-decided/pivots at 0
- echo scan 0 echoes, 0 command echoes
- metaphor
- shape: `12 4946 2 27 10 dialogue punch`, SHAPE CLEAN

`python3 tools/tic_report.py --gate` (the book's copy, as check_chapter runs it) exits 0. My first pass
created three wording problems, all now varied:
- "came up from (the)" crossed the 3+ book-wide line;
- "put my eye to" was an echo of Ch.3;
- that same echo also failed voice-wear.
