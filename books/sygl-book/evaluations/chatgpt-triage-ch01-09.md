# ChatGPT close reading, Ch.1–9: triage against the text (2026-10-21)

Source: `feedback/chatgpt-close-reading-2026-10-21.txt`, **Installments 01–08** (Ch.1 · Ch.2–3 · Ch.4 · Ch.5 · Ch.6 ·
Ch.7 · Ch.8 · Ch.9). Context read: `feedback/chatgpt-editorial-assessment-2026-10-21.txt`. ChatGPT keys notes to printed
pages; I found each note by its quote in `manuscript/chapter-NN.md`, checked author lines against `Sygl_Complete.txt`
(src l.1–362 covers Ch.1–9), and checked every note against the STATE.yaml rulings and the **231 pending fixes**
(`PENDING-FIXES.md`, `fixsets/*.py`, `muse-triage-2026-10-21.md`, `muse-close-triage-ch01-09.md`).

**No chapter or STATE file was edited, and nothing was committed.** New fixes were applied only to a scratch copy, on top
of all 231 pending fixes, where all four gates pass (see the end of this file).

Buckets: **A** fine / ChatGPT wrong · **B** new fix, story unchanged (apply-ready) · **B-opt** optional cut ·
**B0** already pending · **C** author's call · **D** conflicts with a ruling.

## Counts

454 distinct notes (two notes that make two separate claims are split; the end-of-installment priority lists only repeat
notes already counted, so they are not counted again).

| Installment (chapter) | Notes | B | B-opt | B0 | C | D | A |
|---|---|---|---|---|---|---|---|
| 01 (Ch.1) | 49 | 4 | 1 | 2 | 1 | 1 | 40 |
| 02 (Ch.2–3) | 54 | 0 | 1 | 2 | 2 | 2 | 47 |
| 03 (Ch.4) | 44 | 1 | 0 | 1 | 0 | 2 | 40 |
| 04 (Ch.5) | 57 | 1 | 0 | 0 | 2 | 3 | 51 |
| 05 (Ch.6) | 69 | 1 | 0 | 3 | 0 | 4 | 61 |
| 06 (Ch.7) | 64 | 0 | 0 | 1 | 1 | 4 | 58 |
| 07 (Ch.8) | 58 | 0 | 0 | 0 | 1 | 11 | 46 |
| 08 (Ch.9) | 59 | 4 | 0 | 2 | 3 | 5 | 45 |
| **Total** | **454** | **11** | **2** | **11** | **10** | **32** | **388** |

Why A is so large: most of ChatGPT's notes are KEEP/strength notes (about 45%), and most of the rest ask about the
author's own script lines ("At her words, Balthazaar heard the truth", "You'll find out at the ceremony", "I'm not like
most people", "Like a switch had been flipped", "pieces on a game board") or ask for world rules the next pages already
give. Why D is large: ChatGPT reads the book as if it should be darker (its synthesis asks for "moral accountability"),
so most of its developmental asks for Ch.5–9 want Bal to question Amelia, resist being High Priest, feel guilt, or treat
Amelia's affection and the conversion plan as coercion. The rulings close all of these. Installment 07 (Ch.8) is almost
entirely that kind of note.

## Word count

- **New B: net +24 words.** Pending fixes alone: 89,841. With the new B list: **89,865** (still 135 under 90,000).
- Word-adding C options (gate-clean, below): C4 farewell line **+9**, C1 statue line **+16**.
- B-opt cuts (−17 together) are listed but **not** in the fixset; take them only if another range over-delivers.

## B: apply-ready fixes (`fixsets/gpt-ch01-09.py`, list `G`)

Each old string occurs exactly once in the current chapter file and does not overlap any pending fix. Apply **after**
`apply_all.py`. The file runs on its own: `python3 evaluations/fixsets/gpt-ch01-09.py [dir]`.

| Fix | Note | Ch | Exact current text | Replacement | Δw |
|---|---|---|---|---|---|
| G1 | I01 p.7 "That was a temple" (needs Bal's reason) | 01 | `That was a temple.` | `Pillars, fire, a statue. That was a temple.` | +4 |
| G2 | I01 p.9 practice ladder (rug never carried his weight) | 01 | `about to attempt something crazy.` | `about to attempt something crazy. The rug had never carried anything heavier than itself.` | +8 |
| G3 | I01 p.11 peaked roof with a "flat stretch" | 01 | `aiming for the flat stretch beside it where he meant to land.` | `aiming for the slates just below it where he meant to land.` | +1 |
| G4 | I01 p.12 "pillars … fluted columns" redundant | 01 | `past the tops of tall pillars, past their fluted columns` | `past the carved tops of tall pillars, past their fluted shafts` | +1 |
| G5 | I03 #22 who "they" are | 04 | `That's probably why they locked her away, now that I think about it.` | `That's probably why the originators locked her away, now that I think about it.` | +1 |
| G6 | I04 #05 "in the middle of it" referent | 05 | `He yawned hugely in the middle of it and had to start over.` | `He yawned hugely halfway through the message and had to start over.` | +1 |
| G7 | I05 p.60 "she kept to herself" (Bal can't know) | 06 | `Which one was hers, she kept to herself.` | `Which one was hers, she didn't say.` | −1 |
| G8 | I08 "melting in a crust" (a crust is set) | 09 | `with brown sugar melting in a crust on the top.` | `with brown sugar melted into a crust on top.` | −1 |
| G9 | I08 untagged speculation reads omniscient | 09 | `Some of them were bound to bring something large out of the forest` | `Some of them, Bal supposed, were bound to bring something large out of the forest` | +2 |
| G10 | I08 "to get it down" misreadable | 09 | `to the ceiling to get it down.` | `to the ceiling to swallow it.` | −1 |
| G11 | I08 closing: Bal should register the forest's danger | 09 | `holding up a silver ring and waiting for something to come.` | `holding up a silver ring and waiting for something to come. He remembered Mr. Porter's warning about the forest, and walked faster.` | +11 |
| | | | | **Net** | **+24** |

Why each is safe:
- **G1.** The glimpse in Ch.1:35 shows exactly these three things (pillars, a fire, a statue). Bal now names his evidence,
  so "That was a temple" reads as his conclusion, not a narrator's fact. Source: "what looked like a temple".
- **G2.** Before G2 the book's practice ladder ends with the bare rug hovering, and the next thing it carries is Bal. One
  line of Bal's awareness makes the risk ("something that could kill him") concrete. No plot change: the rug holds.
- **G3.** The mausoleum has "a peaked roof" (Ch.1:13), so it has no "flat stretch". He now aims for the slates below the
  ridge, the same slate he watched flicker (Ch.1:35).
- **G4.** "Tops" and "columns" were the same objects. Carved tops (capitals) and fluted shafts are two parts of each pillar.
  Pending fix B2 (concrete → stone) is in the same sentence but touches a different phrase.
- **G5.** In Mrs. Brown's speech "they" means the schools in one sentence and the originators in the next. The source
  meaning is the originators ("That's probably why they locked her away"). One word, meaning unchanged.
- **G6.** The quoted line before it is complete ("Mrs. Brown wants you"), so "in the middle of it" had no clear referent.
  The restart is the next quote ("She says grab your things…").
- **G7.** Close third on Bal: he can see that she says nothing, but not what she "kept to herself". A first wording ("She
  said nothing about which one was hers") made "too she said" recur three times book-wide and was replaced.
- **G8.** Melted sugar that has set is a crust; "melting in a crust" mixed the two.
- **G9.** Source: "As some were sure to get large familiars it made sense…" This is Bal's reasoning about the outside door,
  now tagged as his.
- **G10.** "Get it down" could read as lowering the cheese.
- **G11.** Porter says "Students have died in there" (Ch.9:268) and Viridia is in the forest. The chapter's last beat is
  Bal wondering about her; this lets him register the warning. Adds words, no new fact.

## B-opt: optional cuts (not in the fixset; gate-clean)

| Cut | Note | Ch | Exact current text | Replacement | Δw |
|---|---|---|---|---|---|
| GO1 | I01 p.4 three sentences say "the warning didn't stop him" | 01 | ` He had heard it as many times as anyone.` | *(delete)* | −8 |
| GO2 | I02 p.14 double location slows Amelia's entrance | 02 | `Out of the darkness at the back of the temple, behind the last of the pillars where the firelight gave up, a pale girl` | `Out of the darkness behind the last of the pillars, a pale girl` | −9 |

Recommendation: leave both while the book is under 90,000.

## B0: already pending (with Muse/ChatGPT agreement)

| Note | Pending fix | Agreement |
|---|---|---|
| I05 p.67 "Balthazaar Norheart": surname not established before the claiming | **R1/B1** (Ch.1: "Balthazaar Norheart, or Bal to his friends, was eighteen…") | **Strong.** Muse priority item 7 and Muse chapter note 6.2 flag the same moment. Highest-agreement item in the range. |
| I01 p.12 "Solid concrete floor" clashes with the stone temple | **R1/B2** (concrete → stone) | **Strong.** Muse 1.3 and ChatGPT make the identical point. |
| I05 p.66 uniform shock: "All four originators respond in near-identical shock" | **CB42** deletes "The same shock was on every one of their faces." | **Agree.** The four reactions are already individual (Aren stumbles, Kenmei grips, Naisura sits bolt upright, Raizen's hands come apart). The caption is what made them read as uniform; CB42 removes it. |
| I05 p.66 "That made sense" skips the question | **CB44** cuts "A lot of sense." | **Partial.** Both flag the line. ChatGPT also wants the reason Bal can see through the disguise; Amelia's line just before gives it ("You could see me as I was"). A bond-based mechanism would be a new rule, so it is not added. |
| I06 #62 second round of hostile looks repeats the first | **CB52, CB53** tighten the two stares | **Agree** on the passage. The beat itself is source ("a few hostile stares… no one bothered him"). |
| I03 #02 hall echo explanation overstates the clacking shoes | **CB24** ("echo underfoot") | **Agree,** same clause. |
| I01 pp.8–9 "No school would take you without one" repeats the rule | **CB4** ("take him… he could push") | **Partial.** Both flag the sentence; CB4 fixes its frame. The sentence is source and stays. |
| I02 p.16 "Every claw had been carved separately": does conjuring create or transport? | **CB9** deletes the bench dust | **Related.** The dust made the benches look moved from somewhere old. Without it they read as made on the spot, which suits "as solid as if they had been carved there". |
| I08 p.93 "A few went around by the windows" (ChatGPT: keep this behavior) | **CB58** ("gave his corner a wide berth") | **No conflict.** CB58 keeps the avoidance ChatGPT praises and fixes the logic (Bal sits under the window). |
| I02 p.27 "It was very distracting": repeated attention to Amelia's body | **O10** (optional cut) | **Agree.** Not in `apply_all.py`. ChatGPT's agreement is a reason to promote O10 (−4) if words allow. |
| I08 p.96 red, purple, white: "trim one color beat" | **O14** (optional cut of "He was the color of the chalk.") | **Agree.** Not in `apply_all.py`. Promote O14 (−7) if words allow. |

No ChatGPT note conflicts with a pending fix. ChatGPT praises three passages that pending fixes touch (the windows, the
ring's warmth at CB59, and the "grandfather" smile that CB40 varies); in each case the fix keeps the praised thing.

## C: author's call

| # | Note | Options | Recommendation |
|---|---|---|---|
| C1 | I01 p.12 the statue is seeded three times (Ch.1:35, 1:111, 2:61) and never identified | (a) Leave. The source never pays it off. (b) One line in Ch.3 after `She stood up and brushed off her knees where she had knelt on the stone.` add ` Behind her the sunlight had crept onto the statue, and the face it lit was hers.` (+16, gate-clean). This is a new detail, although a temple built for Amelia holding her statue is the natural reading. | **(b) if the author likes it.** It closes a three-times-planted image, adds words and changes nothing else. Otherwise leave. |
| C2 | I02 p.20 the infant amputation needs a stronger response | Repeats Muse C 2.4. "I don't think anybody asks the baby" and "Someone had bricked up a door in him" already carry it. | Leave. |
| C3 | I02 p.32 school-plane exposition mid-walk | Repeats Muse C 3.2 / 3.213. Source places it here. | Leave. |
| C4 | I04 #15 "Please don't take too long saying your goodbyes": the farewell to the other orphans is skipped | (a) Leave. The source skips it, and Mrs. Brown's hug is the goodbye. (b) Ch.5: after `He dressed without a sound and shouldered the pack he had buckled yesterday.` add ` Nobody else was awake yet to say goodbye to.` (+9, gate-clean). It notes the absence, so Verin's line lands, without inventing a scene. | **(b).** It adds words and invents no event: the other boys are asleep (Ch.5:5), and Verin confirms they are "in their rooms". |
| C5 | I04 #18 the "enrolling as well" cover story is fragile | Repeats Muse C 5.1 / 5.062. Source line. | Leave. |
| C6 | I06 #14 the curfew exemption removes a constraint | Repeats Muse C 7.1 / 7.057. Source line. | Leave. |
| C7 | I07 #24 conversion seems medically trivial | Repeats Muse C 8.5 / 8.088. Source mechanism. | Leave. |
| C8 | I08 p.94 first-years sent into a deadly forest with no safeguards | Repeats Muse C 9.1. Source. Huginn is sent after the class (Ch.9:364), which is a safeguard on the page. | Leave. |
| C9 | I08 p.95 "Students have died in there" needs an institutional reason | Same as C8. G11 lets Bal register the warning. | Leave. |
| C10 | I08 p.95 "a rodent, perhaps? Or a toad?": Porter is a caricature | Repeats Muse C 9.3. Source line. | Leave. |

## D: conflicts with a ruling

| Note(s) | ChatGPT's ask | Ruling |
|---|---|---|
| I01 p.6 move "others who could do no magic" later | Canon fact: other orphans have no magic. Source places it here, and Ch.3's softball boy "with no magic" pays it off. |
| I02 p.26 "Bal had always had a high tolerance for pain" mutes the ordeal; I04 #53 "Bal barely felt it" | Canon fact: Bal has a high pain tolerance (src l.281). |
| I02 p.26 regrowth plus power boost removes his limits | Follow the script: src "should be way more stronger". |
| I03 #08 dramatize Mrs. Brown as a trusted adult through a remembered incident | No invented backstory. |
| I03 #41 interrogate Amelia's attitude to followers and power | Amelia manipulates no one; no invented friction. |
| I04 #17 confront the coercion in familiar commands | Same. |
| I04 #36 Bal should show bodily apprehension about the feeding | Contradicts his source answer ("Nah, just makes you more interesting"). |
| I05 p.66–69 originators capitulate too easily; High Priest conferred without consent; Bal should object (4 notes) | Source beats ("Bal nods accepting her reasoning"); no invented friction or new Bal flaw. |
| I06 #03, #15, #56, #60 Amelia's casual bodily command, "I'll reward you" as manipulation, policing his peers, "You can keep her" as possessive | Amelia is never manipulative; the lines are source. |
| I07 #16, 17, 19, 21, 27, 28, 29, 47, 48, 49, 54 (11 notes) Bal should challenge the Viridia plan, see "too good to pass up" as opportunism, register being used, weigh the battlefield deaths, test Amelia's "not like the others" | Amelia not manipulative; conversions are free choices (Ch.8:67 "Hers to choose"); no invented friction. Muse made the same ask (D 8.050), so both readers agree, and both are overruled. |
| I08 Bal's "I prefer handling my own problems" as irony; Viridia should register moral danger; Amelia's threat should matter to Bal; a flicker of guilt; research "still in service of Amelia's revenge" (5 notes) | No invented Bal flaw or friction; source beats. |

## A: fine as is / ChatGPT wrong (brief)

About 205 of the 388 are KEEP/strength notes that agree with the text. The rest, by type:

- **Source lines kept under the dialogue/script ruling** (~95): e.g. the opening sentence; "Balthazaar, or Bal to his
  friends" (pending B1 also edits this sentence); "Levimotorcorpus"; "What Bal didn't expect"; "curves" and "a first for
  Bal"; "Did the thought… cut off your hand?" (her ignorance is the point: she has been locked away); "At her words,
  Balthazaar heard the truth"; "for about a minute"; Ch.3's opening line; Mrs. Brown's dossier, goldfish and "they really
  don't have a choice"; "You'll find out at the ceremony"; "grandfather"; "deathly quiet"; washing bowls in the trough;
  Aren's speech and the four portraits; "Blood guy"; "I'm not like most people" (it sets up the hair joke); "lame
  familiars"; "You'd be surprised" (ruling); "full story"; "leg up"; "Like a switch had been flipped"; "pieces on a game
  board".
- **Answered on the page** (~60): roof geometry (the orphanage roof is the flat one; the mausoleum is peaked); the apple
  browning over minutes ("until it went brown"); "The spell let go" (the rug is not still enchanted); the paradox of the
  sky (the next lines raise it and "Because it's magic" answers it); late versus at-birth manifestation (Mrs. Brown
  explains both, Ch.4:264/274); why originators can't interfere (Ch.6:502); the five who "left a few days ago" set out for
  the claiming; why the blood mages are secretive (the next sentence: never admitted to a school); the portal's evening
  light (a different plane); Amelia taking the buggy (portalling in would unmask her); rooms appearing by thought (Bal *is*
  the Lead Mage); sweater sygl ("Verin had said it would"); Viridia's privilege (she states it herself); "Any paper would
  do now" (Ch.7:185); "Rune working" is spelled the same way everywhere; "This would be all over the castle" (paid off at
  the next lunch, src p.50); the avoidance rune (Ch.9) is planted for later use by author ruling.
- **ChatGPT misread** (6): I05 p.59 "lacks residue from leaving Verin" (Verin is still driving; the farewell is at the
  gate, Ch.6:320); I05 sibling inference (it is marked as Bal's guess, and Ch.7:117 corrects it by author ruling); I05 the
  Tempus girl's missing name (author ruling: she introduces herself in Ch.7 and Bal recognises her); I06 #25 permanent
  rooms need the Lead Mage (that is Bal); I05 p.68 "should he feel fear" (Ch.6:460 "Now he was starting to"); I08 the
  forest closing (it already ends on concern; G11 adds the warning).
- **Style notes too small to act on** (~20): "all down both rows", "further/farther" (house style), "his half", "Out of
  the darkness", "the hallway went on", "deathly quiet".

## Gate results (scratch copy)

Scratch: `/tmp/claude-0/-home-user/925d8686-989e-5134-a9ef-2d597d7cac42/scratchpad/g1/`, the whole manuscript plus
`tools/`, `STATE.yaml` and `character-bible.md`, with `apply_all.py` (231 applied, 0 missed) and then `gpt-ch01-09.py`
(11 applied, 0 missed). Baseline for comparison: `scratchpad/g0/` (pending fixes only).

| Gate (run from g1/) | Pending only (g0) | Pending + G1–G11 (g1) |
|---|---|---|
| `style_check.py --dir manuscript` | clean | clean (repeated-phrase list identical to g0) |
| `grammar_check.py --dir manuscript` | clean | clean |
| `tic_report.py --gate` (on `manuscript/chapters/chapter-N.md`) | clean | clean |
| `voice_wear_check.py` (strict) | clean | clean (output identical to g0) |
| Words | 89,841 | 89,865 (+24) |

First run: G7's first wording made "too she said" recur three times book-wide (tic gate fail); reworded. In a second copy
(`scratchpad/g2/`), C1(b), C4(b), GO1 and GO2 applied on top are also clean on all four gates (89,871 words). C1's first
two wordings tripped "at the far end", "bal saw that" and "across the hall"; the version above is the clean one.
