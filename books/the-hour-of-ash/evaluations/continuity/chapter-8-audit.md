# Continuity Audit: Chapter 8 (run 2, per-chapter drift audit)

**Date:** 2026-10-19
**Mode:** MANUSCRIPT AUDIT. Ch.8 checked against Ch.1–7 as they stand on disk (all re-read in full), against the plan, and against canon.
**Chapter reviewed:** `manuscript/chapters/chapter-8.md` (7,697 prose words by `shape_check`, 7,840 by `wc -w`; **241 prose paragraphs**; no breaks).
**Paragraph numbering:** `ch-08:pN` counts prose paragraphs only. The title and the two HTML comments are not counted, so p1 = "And once we're above the last house…" and p241 = the closing paragraph ("When I woke the snow had stopped…"). Prior-chapter citations use the same convention for the files as they stand now: Ch.3 has 84 prose paragraphs, Ch.4 83, Ch.5 210, Ch.6 341 and Ch.7 195.
**Read against:**
- outline.md: Ledger rows 7–10, `## Chapter 7` through `## Chapter 10`.
- STATE.yaml: guardrails, canon, resolved decisions, ARCH-1…18.
- voice-dna.md: §0, §1 (including Dialogue conventions and VOICE UNDER PRESSURE), §3 and §3b.
- character-bible.md: the Mara, Valens, Kallia, Theano, Nikaso, Sostrata, Philista and Timo cards; the Ch.5–8 walk-on and spent notes; every at-risk block (after Ch.1, 3, 5, 6, 7, 7 cycle 1 and 8) and the at-risk table.
- voice-bank/samples 01–13.
- ENTITY_STATE.yaml. On disk it is `last_updated_chapter: 7`. Its 14 `ch-08` mentions are all plan rows (`source: outline:ch-08`) and none are Ch.8 page facts. I treated them as unverified. Every Ch.8 fact below comes from the page.

**Mechanical baseline (re-run for this audit, read-only, `bash tools/check_chapter.sh 8`):**
- Style clean: simile 3.1/1k, adverb 3.0/1k, em-dash 2, foreshadow 0.
- Grammar clean. Rhythm 0 flagged. Show/tell: no flags (dialogue meter 26.4%).
- Voice-wear strict clean. Tic gate clean, including the gesture layer. Echo scan: 0.
- And-chains 3 (cap 9). Credential asides: 0 by the detector, 3 by a manual count (W-10). Negation pivots 0. 'So' openers 0. 'before I decided' 0.
- Metaphor: fig 3.6/1k, 24 similes, median sentence 15, 6.4% of sentences over 40 words.
- Shape audit across 8 chapters: CLEAN. Ch.8 computes as `dialogue` → `quiet`, 0 breaks, dialogue 27%, median 15.
- A sub-gate 4-gram sweep (mine, run against Ch.1–7 and the voice bank) found 6 echoes. All are logged below (W-08, N-12).

**Total findings:** 47. **CRITICAL: 0 | WARN: 20 | NOTE: 27**

The gates are clean and every ledger cell is hit. All five beats are on the page, and nothing supernatural happens: the hand goes into the crack and finds "January cold and no more". The rite is physical and not lurid, and the women stay distinct from one another. Nothing breaks canon or plot. The WARNs fall into four groups:
- **Character seams with Ch.7:** Kallia sits, although Ch.7 and voice-dna both say she never does. Her hair is "always" under a kerchief, but Ch.7 showed her washing it at the bath.
- **Information flow:** Kallia asks "Was it shut?" when nobody ever told her that the cave opens. Mara follows fast, overlapping and whispered talk in the dark without losing a word.
- **Spent or lifted material:**
  - the towing image from Ch.6;
  - the voice-bank's "pin at my shoulder" and its could-not-stop laugh;
  - the "whose" question again;
  - a knotted-footwear identification that repeats Ch.7's boot knot;
  - a persistence formula used five times;
  - two gesture phrases repeated inside the chapter.
- **Geography and history:** the stalagmite is on the wrong side; there is snow in the town although the snow "begins" on the cliff; the shepherds' huts are ignored; Plutarch's frozen cloaks are attributed to the wrong people.
- **Theano:** her crows read as a wink in two places. Both can be fixed by cutting.

---

## Scorecard by category

| Category | Result |
|---|---|
| (a) Beats / ledger | **PASS.** Single-scene, in the rite's own order. Open `dialogue`: Kallia mid-instruction, p1 ✓. Close `quiet`: the closing sentence is 20 words, the heap and the steam ✓. Breaks 0 ✓. Dialogue 27% (`shape_check`) / 26.4% (meter), band 25–35 ✓. Median 15, gear mid ✓. Length 7,697 against a target of 8,200 (range 7,500–8,800) ✓. Beats: 1, the crows (p25–p27; see W-05). 2, the ascent: ivy p10, fawnskin p31, fennel wands p31, drums and pipe p29, wine p67, dance p65–p73 ✓. 3, the cave: hand at the threshold, nothing, no scream, p80–p83 ✓. 4, snow shuts the stair and they wait for dawn, p108–p118 ✓ (Plutarch p174). 5, the sandals farce p140–p173, the shared cloak p218–p222, the bawdy song p192–p212, and a woman she has never spoken to pulling her into the heap (p221, p225) ✓. Opens toward Ch.9: money and the god who answers, p98–p106 and p121 ✓. Anchor p215 and p241 ✓. |
| (1) Character consistency | **Kallia: WARN ×2** (W-01 she sits; W-02 the hair gloss against the bath). Otherwise on-card. She answers with tasks (p4, p6). She uses the "Then" retort once (p15). Her one non-task reply is a question back, "Who would I send in?" (p106), which is the variant the Ch.7 note asked for. She never touches Mara: "two fingers on the bronze and none on me" (p12), and Mara holds her himation "which she allowed" (p92). She walks off once (p90). She says nothing about herself, though "not sons" (p1) is allowed by her card. **Nikaso against ch-05:p181–p191: PASS.** She is the wife of the man with the sieve. She was asleep, and the sieve still wants mending (p17–p18). "Two gates up" fits a short lane with the sieve house "halfway along". **Sostrata against Ch.7's bath (ch-07:p38–p53): PASS.** She is the baker's wife, with the mother-in-law who has moved in (p47, p72, p182, p190, p235). She is identified by the singeing offer (p46) and named by Timo (p48). **Valens via the mule: PASS** (p28). He is known by the gray, his back is turned, and there is no line, face or romance signal. **Mara: PASS** with W-06, W-09 and W-10. Her Greek is uncontracted throughout (p21, p34, p36, p38, p61, p135, p164, p168, p184, p207, p210, p224, p231). |
| (2) Timeline | **PASS.** "a few days past the turn of the year by my private reckoning" (p7) puts midwinter after 1 Jan AD 71. That follows Ch.7's "the last morning of the month" (ch-07:p186) after a December registration ("fed me lentils for two months", ch-07:p157, from an October arrival). It matches outline Ch.8, AD 71, and retires the open note in ENTITY's ch.8 timeline row. "January cold" (p81) agrees. "the coldest week since October" (p7) agrees with the October arrival (ch-03:p84). The night runs from dusk (the crows, p25) to the snow at the cave (p84), the shut stair, the pen, and first gray light (p241). There is no clock time. "the time before last" (p226) fits Ch.7's "every other winter" (ch-07:p190). |
| (3) Information flow | **WARN ×2** (W-04 Kallia's "shut"; W-06 comprehension). Clean elsewhere. Mara knows Valens's name from Ch.6 (ch-06:p48), and nobody says "Lupus". The record names no husband: p190 matches ch-07:p172. "the Syracusan" (p19, p204) and "Maira" (p183, p228) are both town knowledge after the public registration (ch-07:p161–p173; "I turned my head for Mera at the water", ch-07:p183). The boat in Mara's joke (p207) is Kallia's story (ch-07:p139, p172). Nikaso learns about the cave from Mara herself (p229–p232). |
| (4) Objects | **PASS.** The **watch** is with Valens, and there is no clock time anywhere (ch-07:p107). The **flashlight** stays in the bag under the stair, unused, and the page explains why (p10; ch-07:p10). No one saw it. The **himation** is the girl's brown wool (p10): soaked at the drift (p76, p174), black-kneed (p90), frozen and cracked along the fold (p174), and lying over her boots in the heap (p222). This is consistent with ch-07:p10–p11 and p184. The **boots and rags** are blanket strips over the boots (p2), showing "for a step under the hem" (p16; compare ch-07:p14–p16), with outer rags iced and inner rags wet. She keeps her boots on in the pen (p137) ✓. The **coins**: "two brass coins … with a poet on the bigger one" (p121) = ch-06:p103–p105 ✓. The **shovel scratches** (p79) = ch-06:p3, ch-06:p34 and ch-07:p4 (but see N-05). Not touched: the microcassette, the knucklebone, the Pentax, the notebook (all on schedule). |
| (5) Plot threads | **PASS.** The cave is shut a second time. The Oracle question opens: women cannot go in, a man must, it costs, and it is shut in winter (p98–p106). See N-01 for the Ch.9 overlap. The swept room is not shown, and the broom is not used (at-risk rule, Ch.8–9) ✓. Kallia's "not sons" (p1) and "Who would I send in?" (p106) are present-scene subtext ahead of Ch.10, not narration reaching forward. "Men will come asking" is not touched ✓. The fifth coin and the spitting oak are not argued again ✓. Nikaso's sieve is still unmended (texture). |
| (6) World rules | **PASS on the door.** The cave is shut. There is no door word ("Was it shut?" / "To see if it was open", p95–p96, p231; CH3-7 holds). The test is null and physical. **History:** Liknites woken in the winnowing basket, the trieteric rite, the Athenian Thyiades (p45), the fennel wands, the fawnskin, the tympana and pipe, unmixed wine, *euoi*, and Apollo away for the winter (p59, p98) are all plausible. **WARN** on Plutarch (W-17). NOTE on the fennel's burn (N-18). **Geography: WARN ×3** (W-03, W-15, W-18), plus N-03 and N-04. |
| (7) NO FORESHADOWING | **PASS.** Gate 0. Manual read: the "would" forms are present-scene suppositions (p10, p68, p83) or speech. Plutarch is past-facing reading. Theano is unnamed, and nothing in the narration reaches forward. Her line "you know very well whose it is" is not foreshadowing in the narration, but it plays as a planted riddle (W-05). |
| (8) NO TICS | **Mechanical: PASS.** Manual check of the constructions the gates cannot see: **WARN** W-11 (the persistence formula ×5), W-12 (two gesture phrases repeated inside the chapter), W-13 ("whose" past its cap) and W-16 (the "supplied" triad); NOTEs N-10, N-11, N-13 and N-14. Spoken refrains: "She'll have my eyes" ×2 (cap) and "Knead it…" ×2 (cap) are held as the bible says. Command-echoed-as-compliance: 0 ✓. Memory kicker: 0 (p71 ends on its image) ✓. Mara's voice failing: 0 ✓. |
| (9) Voice drift | **PASS.** Mid gear. The dry asides are present and varied in form ("which I suspected was not the intention", p31; "which I would not have done in her place", p166; "since I could not sing to save my life", p207; "owed him an apology", p174). The 1998 comparisons rotate through home, street, school, shop, kitchen and laundromat, and none is reused (but see N-08). There is no analytical simile and no lyrical climax. The CONTINUITY COMMITMENT holds: no English at all, aloud or to herself, including at the crack (p80–p83). Her memory paragraph (p71) is narration, not speech. |

---

## PRIORITY: UNRESOLVED ENTITY_STATE CONFLICTS (processed first)

ENTITY on disk covers Ch.1–7 (`chapters_tracked: [1..7]`). The parallel tracker's Ch.8 content is not on disk as page rows. Each open conflict was checked against Ch.8:

| ID | What Ch.8 does to it | Verdict |
|---|---|---|
| **CH3-3** pen vs refuge hut | This is the fourth look at the site, and it is a pen again: "The pen had walls of stacked stone to the height of my chest and no roof" (p122). There is still no refuge hut. The new wording "stacked stone" drifts from the herringbone set on edge (N-03). | Open (plan vs prose). Recommend RESOLVE, prose wins: outline Ch.4 should say pen. |
| **CH3-7** the door is never named | Still never named: "Was it shut?" / "Yes. It was shut." (p95–p96); "To see if it was open." (p231) | In character. **Recommend RESOLVE, prose wins.** No manuscript action. |
| **CH4-3** jacket vs fleece | Ch.8 names no fleece or jacket. She is in the tunic and himation. | Unchanged, open. |
| **CH4-4** inscription | Not mentioned (p76 has the arch and the drift only) | Unchanged. |
| **CH6-5** first attempt | Not touched | Unchanged. |
| ENTITY timeline row ch.8 note ("the page does not say whether midwinter falls before or after the turn of the year") | p7: "a few days past the turn of the year" | **Satisfied.** Replace the plan row with the page fact (see patches). |
| CH1-2, CH1-3, CH2-1, CH2-3, CH2-4, CH2-5, CH3-1, CH3-2, CH4-2, CH5-3, CH5-4; P1, P3, P4, P5 | Not touched by Ch.8 (P5: Valens still works openly in Delphi, p28) | No change. |

---

## CRITICAL ISSUES

None.

---

## WARN ISSUES (fix before the evaluator)

### [W-01] Kallia sits in the pen. Ch.7 and voice-dna both say she never does.
- **Audit:** character consistency.
- **Evidence:**
  - ch-08:p137 "Kallia, beside me, had her shoes off and her rags hung over her two hands toward the fire" (seated, by implication).
  - ch-08:p157 "Kallia said nothing through any of it. **She sat** and let it go by her like weather".
  - ch-07:p26 "sitting was the one thing Kallia never did in my sight" (the one exception is staged and marked).
  - voice-dna §3: "Theano sits, Kallia never sits". This is the cast-wide distinguisher between the two Phocian women, and Ch.8 has just shown Theano sitting (p25).
- **Why WARN:** the narrator glossed this exception in Ch.7 and lets it pass unremarked here. Ch.8's one Kallia rarity gloss is already spent on her hair (p66, cap ≤1), so the fix is to keep her off her seat rather than to add a gloss.
- **Minimal fix (wordings fresh):** p137 "Kallia was squatting beside me with her shoes off and her rags hung over her two hands toward the fire, turning them like flatbreads on a griddle." p157 "She stayed on her heels and let it go by her like weather, until…"
- **Cascade:** Lying down to sleep (p215) is not sitting, so keep it. Do not have Mara notice the squat.

### [W-02] Kallia's hair is "always" under a kerchief, but Ch.7 showed her washing it at the bath
- **Audit:** character consistency / internal contradiction.
- **Evidence:**
  - ch-08:p66 "it had been under a kerchief every day I had known her, and I had begun to think of it as something she did not have."
  - ch-07:p53 (the bath) "She poured a dipper of water over her own head and shook it off."
  - ch-07:p38 has her "washing standing up" in the women's bath.
- **Minimal fix (fresh):** "Her hair came down gray to her shoulder blades. I had seen it only once before, plastered flat at the bath, and I had begun to think of it as something she did not have."
- **Cascade:** It stays Ch.8's single rarity gloss.

### [W-03] The pale stone is on the wrong side
- **Audit:** geography (the cave interior).
- **Evidence:**
  - ch-08:p78, going IN: "The great pale stone in the middle slid past **on my right**".
  - ch-03:p78, coming OUT by the same route: "the slumped shape went by **on my right**".
  - ENTITY corycian-cave: the slot is reached "past the slumped stone", with the roof coming down on the left. Ch.8 keeps the left-hand roof (p78).
- **Minimal fix:** "slid past to my left". ("on my left" is already in p78 for the roof; "to my left" is unused book-wide.)
- **Cascade:** None. Ch.19 and Ch.42 do not use this cave.

### [W-04] Kallia's "Was it shut?" assumes knowledge nobody gave her
- **Audit:** information flow.
- **Evidence:**
  - ch-08:p95 "Was it shut?"
  - Kallia's sources on the page: the shovel came back with its edge turned "on the god's rock. At the cave." (ch-07:p4–p6); "Not as high as your cave." (ch-07:p194); the town's nymph rumour.
  - Mara has never told her the cave opens. The only person she told is Valens: "Until it opens." (ch-06:p231), "Where I came in." (ch-06:p84). Kallia's "There's no such country." (ch-07:p89) argues against her having built that model.
- **Why WARN:** it is plausible that Valens passed it on off the page, but nothing shows it. The question is the hinge into the Oracle offer, so the reader will notice how much Kallia knows.
- **Minimal fix (Mara supplies the word; Kallia asks a practical question, on card):** p95 "In there." Then, further on, …: "Did you find what you went for?" p96 "No. It was shut."
- **Cascade:** p98 "If it's something you want out of that mountain" still follows. "what you went for" is unused book-wide.

### [W-05] Theano's crows read as a wink
- **Audit:** outline Ch.8 writer warning ("Don't use Theano's crows as a wink; they are texture"); the at-risk rules on walk-on word-doubling and negation endings.
- **Evidence:**
  - ch-08:p26 "Thieves," she was shouting at them. "Black thieves, every one of you. That's not for you, **and you know very well whose it is.**"
    - The clause is a riddle with no answer on the page (the god's barley). Read beside the Theano card ("Feeds the crows the god's barley"), it plants her.
    - "Thieves… Black thieves" is walk-on word-doubling (at-risk after Ch.5: "none for walk-ons").
  - ch-08:p27 "…and gave us not a look as we went by. **Nor did any of us spare her one.**" The narrator points at how little anyone noticed her, and the paragraph ends on a negation (at-risk after Ch.3).
- **Minimal fix:**
  - p26: "Black thieves," she was shouting at them, "every one of you. That's not for you." She threw another handful. "Go on, then. Take it. Choke on it."
  - p27: "She kept her free hand on her knee the whole time, and her eyes on the crows."
  - "her eyes on the crows" is unused book-wide.
- **Cascade:** Bible Theano Ch.8 block: re-quote. Ch.13 still recognizes her by the crows and the knee, by situation only, and must not re-quote these lines.

### [W-06] Comprehension jump: fast, overlapping, whispered and sleeping talk in the dark, all caught whole
- **Audit:** information flow (Mara's Greek).
- **Evidence:**
  - ch-08:p111 "Everybody talked at once." This is followed by six separate voices, each rendered whole (p111–p117).
  - ch-08:p233 "Further along the heap Timo was whispering to Sostrata, and Sostrata was whispering back." The whispered exchange follows in full (p234–p237).
  - ch-08:p238 "Sostrata talked in her sleep about the dough."
  - Against: ch-06:p67 "Kallia went at him in Phocian too fast for me to follow"; ch-06:p302 she "lost words out of everything" the charcoal burner said.
  - Since then she has had about five weeks of house Greek indoors (ch-07:p60) and a month of public silence. Growth is plausible. Losing no word at all is not, and earlier audits flagged the same jump (Ch.5, Ch.6).
- **Minimal fix (two clauses, fresh):**
  - p111: "Everybody talked at once, and for a while I could not sort one voice from the next, until single ones came clear of it."
  - p233: add "…and Sostrata was whispering back, near enough that I got about half of it."
  - p238: "Later Sostrata talked in her sleep, a word of it about the dough, and…"
- **Cascade:** None. The song (p193–p212) can stay: the women sing it slowly, it repeats, and "by the last of them I had the refrain".

### [W-07] The spent Ch.6 towing image is reused
- **Audit:** spent moves.
- **Evidence:**
  - ch-08:p30 "Then I had been towed up it on a mule's tail".
  - ch-06:p162 "I climbed the cliff above Delphi in the dark being towed by a mule".
  - The bible's Spent-in-Ch.6 list: "being towed up the cliff by a mule's tail" (do not reuse).
- **Minimal fix (fresh):** "The path took the cliff in its switchbacks, as it had in November. In November I came up it in the dark behind the gray; now I had a torch in my fist…"

### [W-08] Voice-bank lift: "the pin at my shoulder" (sample-10, the Ch.15 heat anchor)
- **Audit:** voice-bank lifts (zero allowed). The echo scan missed it because the phrase is a 4-gram.
- **Evidence:**
  - ch-08:p12 "She caught **the pin at my shoulder**, two fingers on the bronze and none on me".
  - sample-10: "He undid **the pin at my shoulder** with the same patience…". That is the first-union gesture, and spending it now on Kallia uses it up.
- **Minimal fix:** "She caught the pin, two fingers on the bronze and none on me, and moved it higher." p10's "pinned at my shoulder" can stay.

### [W-09] Voice-bank structural lift: the laugh she cannot stop (sample-09) pre-spends Ch.22 and Ch.25
- **Audit:** voice-bank lifts, and the at-risk entry for Mara laughing WITH others.
- **Evidence:**
  - ch-08:p208 "I was laughing with them. The laugh started down under the wine, **and there was no stopping it, and I did not try**, and when it was done my face ached in the cold."
  - sample-09 (Ch.25): "began to laugh and could not stop".
  - Bible: "The next mapped laugh is Ch.22's fit."
  - "laughing with them" also repeats ch-04:p34 "I laughed with him". That makes the bible's "her first shared laugh" claim inaccurate (N-27).
- **Minimal fix (also removes one and-chain):** "I was laughing too. The laugh started down under the wine, and when it was done my face ached in the cold." ("laughing too" is unused; Ch.7 has "I nearly laughed too".)

### [W-10] Three knowledge-provenance asides in one chapter (cap 2)
- **Audit:** at-risk after Ch.5 ("I knew X from [text/lab]": max 2 per chapter).
- **Evidence:**
  - p73 "a word I had met in Euripides".
  - p79 "my thumb **knew it from** a hundred bad repairs that had reached my bench from other people's hands". This one is also a work/bench reference next to the SPENT job statement.
  - p174 "Plutarch had a story…".
- **Minimal fix:** end p79 at "It was an ordinary feeling, the edge of a scratch in stone." Cut the rest of the clause.

### [W-11] The persistence formula ("where it had [verb]"), 5× in one chapter
- **Audit:** device emergence.
- **Evidence:**
  - p10 "The flashlight stayed where it was"
  - p76 "**The arch was where it had always been.**"
  - p78 "the slab… leaning **where it had leaned**"
  - p159 "It lay **where it had landed**"
  - p241 "standing up in the snow outside it **where it had landed**"
  - p159 and p241 also repeat the same 4-gram inside the chapter.
  - The formula is already in ch-07:p10 ("where it had lain since October"), ch-04:p61 ("where the pen had stood that morning"), ch-02 ("where I had left it") and ch-06:p42.
- **Minimal fix (keep p10 and p241):**
  - p76: delete the first sentence and begin "The drift inside the arch had grown, long and smooth, nearly to the lip."
  - p78: "…there was the slab in front of me, propped against the wall as before, with the crack running the height of it into blackness."
  - p159: "It lay smoking faintly on the stones while each woman in the pen decided it was some other woman's."

### [W-12] Two gesture phrases repeated inside the chapter
- **Audit:** NO TICS (gesture layer below gate resolution).
- **Evidence:**
  - p218 "The stranger **lifted her head out of the heap**."
  - p238 "until Philista **lifted her head out of the heap**."
  - p221 "and **raised the edge of her cloak** with her other arm"
  - p241 "I **raised the edge of the stranger's cloak** an inch".
- **Minimal fix:** p238 "until Philista spoke from the far end of the wall." p241 "I pushed the stranger's cloak up an inch and saw the pen…"

### [W-13] "Whose" questions past their SPENT cap
- **Audit:** at-risk table: "Whose are you?" / "Whose is she?", 2 uses (ch-05:p76, ch-05:p173), SPENT. "A third 'whose' question would make it a refrain."
- **Evidence:**
  - p145 "**Whose** is the stone?"
  - p155 "**Whose** has a knot in the strap?"
  - In the same chapter: p26 "you know very well **whose** it is" and p222 "I could not tell **whose** it was".
  - The sandal farce wittily inverts the ownership question, but it makes the word a refrain.
- **Minimal fix:** p145 "Who put a stone in the ring?" p155: see W-14. p26 is handled by W-05. p222 can stay as narration.

### [W-14] The footwear-knot identification repeats Ch.7's boot knot
- **Audit:** spent moves. The bible lists Valens's "boots-only sighting" as SPENT and "Mara's eyes-down business" as CLOSED after Ch.7.
- **Evidence:**
  - ch-08:p138 "the left strap had been mended with a thong of paler leather and **knotted twice** over the instep, the second knot tighter than the first. I had studied **that knot** at the spring every morning for weeks".
  - ch-07:p96 Valens's boots: "one lace broken and **knotted** where it had broken, **the knot** standing up like a little fist" ("I kept my eyes on the knot in the broken lace").
  - Both times Mara knows a person by a knotted mend on footwear seen with her eyes down.
- **Why WARN, not CRITICAL:** the recognition beat (p221, "each morning you look at my feet") is designed and is the chapter's best payoff. Only the mark repeats.
- **Minimal fix (vary the mark; fresh):**
  - p138: "the left strap had been patched over the instep with a square of paler leather, sewn on with a thong and set on askew. I had studied that patch at the spring every morning for weeks…"
  - p155: "It's got a patch on the strap. Who has a patch on her strap?"
- **Cascade:** Bible walk-on note for the stranger. p156 "Not that one" is unchanged.

### [W-15] Snow in the town, then "The snow had begun there, on the cliff path"
- **Audit:** internal continuity (weather).
- **Evidence:**
  - p25 "threw it **over the snow**… black **on the white**, walking about **on the frozen crust**".
  - p35 "**The snow had begun there**, on the cliff path, a hard old crust in the angles of the rock". Nikaso's sandals only get wet here.
  - p7 "The frost had not gone off the court all day": frost, not snow, in town.
- **Minimal fix (fresh):** p25 "…threw it over the frozen ruts a fistful at a time. The crows had dropped to it out of the dusk, a dozen and more, black on the white rime, walking about with their shoulders up."

### [W-16] The "supplied" triad
- **Audit:** retired reflex (anaphora/epistrophe triads).
- **Evidence:** p190 "She had **supplied** dead people and a boat that got in ahead of the winter; she had **supplied** no husband, and she did not **supply** one now."
- **Minimal fix:** "She had supplied dead people and a boat that got in ahead of the winter, but no husband, and she did not add one now."

### [W-17] Plutarch's frozen cloaks: the attribution
- **Audit:** world rules (history).
- **Evidence:** p174 "Plutarch had a story of women caught by snow on this mountain, **whose clothes froze** so hard that they snapped when anybody tried to unfold them".
  - In *De primo frigido* 18 (953D), as I recall it, the cloaks that froze and broke "like wood" when spread out were the men's. These were the rescuers sent up after the snowbound Thyiades, not the women's own clothes.
  - Confidence is moderate, so check the text before editing. Mara is a careful reader of Greek, and an error here undercuts her.
- **Minimal fix (correct either way; fresh):** "Plutarch had a story of the women caught by snow on this mountain, and of cloaks that froze so hard they snapped when anybody tried to unfold them;"
- **Cascade:** It suits the page: the men who "will bring … up the stair in the morning" (p117) are Plutarch's rescuers. Do not add a rescue.

### [W-18] Snowbound women choose a roofless pen and ignore the shepherds' huts
- **Audit:** plot logic / geography.
- **Evidence:**
  - p118 "Back to the pen. Get under its wall".
  - p122 "The pen had walls of stacked stone… and no roof".
  - Huts are established on this plain: ch-04:p62 "Low huts stood down there, roofed with brush held down by stones"; ch-06:p190 "The huts… with their brush roofs weighed down". A reader will ask why they do not go there.
- **Minimal fix (one clause at the head of p122; fresh):** "The shepherds' huts were the width of the plain away, in the dark and the drift. The pen had walls…"

### [W-19] "a stranger to me" (p185), then "The stranger" (p218) is a different woman
- **Audit:** reference clarity.
- **Evidence:**
  - p185 "A woman behind Nikaso, **a stranger to me**, stopped wringing out her rag to look."
  - p218 "**The stranger** lifted her head out of the heap." This means the big woman of p138, who until here has been "a big woman" / "the big woman". The nearest antecedent is the p185 woman.
- **Minimal fix:** p185 "A woman behind Nikaso, one I did not know, stopped wringing out her rag to look."

### [W-20] The character-bible's Ch.8 blocks quote lines that are not on the page
- **Audit:** bookkeeping. Dialogue Polish and the Ch.9–13 writers work from these blocks.
- **Evidence (bible → page):**
  - Kallia: "Hitch that up, or you'll be on your face before the stair." → not on the page (p1 has "Wind it harder than that…").
  - Kallia "gives no answer at all (silence)" to "Have you asked him anything?" → the page has "Who would I send in?" (p106).
  - Walk-ons: "Then they're warmer than you … glad of a night off from you." → p112 "They'll be warmer than you … glad of a night without your feet in their backs."
  - Spent list:
    - "as warm as a kitchen with the oven going" → p227 "as warm as a laundromat in February";
    - "waking a god with a farmyard chore" → not on the page;
    - "a bank at Fifteenth and Market" → p121 "a bank downtown".
  - Philista's card: "and I'll not carry her" → not on the page.
  - At-risk after Ch.8: "the only part of me that had been warm" → not on the page.
  - Mara block: "her first shared laugh" → ch-04:p34 already has one (N-27).
- **Fix:** re-sync the bible's Ch.8 blocks to the final page after the editor applies this audit, quoting by script as was done for Ch.6 and Ch.7.

---

## NOTES (polish, or for later chapters)

- **N-01 (Ch.9 handoff).** Kallia's p100 ("Women can't go in to him. A man goes in for you…") and p104 ("It costs… Ask a priest") already give part of outline Ch.9 beat 3. Ch.9 should add only what is new (the *pelanos*, the goat, the Delphian sponsor) and must not re-explain male representation.
- **N-02 Torch budget.**
  - Ch.6 fixes a pine at about half an hour: "until the long hand is at the eight" → "Most of a pine, then." (ch-06:p15, p18).
  - In daylight with a bag, the firs to the cave took an hour (ch-03:p27).
  - Ch.8 has her do the round trip at night in snow on one torch plus one spare (p74, p83).
  - p83's "lit the second pine off it and crushed the first out" also echoes Valens's relay (ch-06:p7, ch-06:p273).
  - Fix: p74 "took two more pines off the pile"; p83 "Once the torch began to gutter I lit the last of my pines from it and put the old one out on the rock."
- **N-03 The pen.** "walls of stacked stone" (p122) blurs the herringbone, every stone on edge, of ch-03:p14, ch-04:p61 and ch-06:p219. Mara is the narrator who sees joins, so restore the edge-set stones. "the gap where the hurdle had been" (p122): the hurdle stood in November (ch-06:p219), so where did it go? One clause fixes it (pulled aside, or burned).
- **N-04 Firs to arch.** In p75–p76 and p84 she climbs straight from the trees to the arch ("Outside, the stars had gone. The dark beyond the trees…"). Ch.3 (p45) and Ch.6 (p276–p286) put an open slope with zigzags between them. Add one clause of open slope.
- **N-05** p79 "when I was sure there was earth down there to dig". There was earth, and she dug it out (ch-06:p1, p34). Suggest "Kallia's little shovel had made them in November, after the last of the earth was out."
- **N-06 The ivy-askew image ×3** (Timo's ivy over her eyebrow, p48; a dancer's ivy over her ear, p65; Philista's "Your ivy's down over your eye", p91). Vary p91, e.g. "Your ivy's crooked."
- **N-07 "hot stone" ×2:** the wine "like a hot stone" (p67), then Timo's real hot stone (p180, plus p182 and p235). Vary the p67 simile.
- **N-08 Comparison domains.**
  - p29: the pine catches "with a noise like a sheet being shaken out". ch-07:p10 has the himation shaken out "with a crack like a sail filling". Both compare the sound of shaken cloth, and voice-dna §1 says no comparison is used twice. Cut the simile or change its domain.
  - p44: Philista "like a teacher at a classroom door after the bell". ch-06:p49 has Kallia "like a crossing guard". The domain is the same (a woman as school authority), but the image differs. Watch it.
- **N-09 "fished"** at p157 and p160 (two paragraphs apart), plus Kallia fishing the garland at ch-05:p138. In p160, "She had fished the red pair out" → "She had grabbed the red pair out".
- **N-10 Sentence-initial "Everybody" ×3 in narration** (p53, p111, p144). p144 → "The women near her had leapt up too".
- **N-11 "Mine…" openers ×6 in dialogue,** with a triad at p181–p183 (Nikaso / Sostrata / Timo). p182 → "The baker will be asleep on the flour sacks…".
- **N-12 Sub-gate voice-bank echoes (4-grams):**
  - p63 "came in under the" (sample-10)
  - p112 "the woman next to" (sample-03)
  - p191 "the women of Delphi" (sample-03) → "the women here"
  - p74 "burned down to a red heap" ~ sample-12 "gone down to a red seam" → "When the oak had gone to coals"
  - p222 "the smell of goat hair and woodsmoke" ~ sample-10 "the smell of sheep and woodsmoke" → drop "and woodsmoke".
  - Fix the last three. The first two are common phrases.
- **N-13 Word-doubling barks:** Philista's "Louder," … "Louder!" (p65) and "Down! … and down" (p91). Theano's is handled in W-05. Philista is now named, but the at-risk rule names the move. Drop the first "Louder," and the first "Down!".
- **N-14 "girl" as address ×2** (p150, unattributed; p239, Philista to Timo). voice-dna's address rule bans "girl" as a hallmark. p239 → "He can't hear you from Delphi, Timo. We can."
- **N-15** p7: the Thebans' shutters are closed, yet "When Kallia stood up the singing stopped". How did they know? Add "through a crack in a shutter" or let the gate's noise cue it.
- **N-16** p24 "Men stood in their doorways to watch" vs p28 "like every other man in the street" with his back turned. Narrow p28 to "like every other man at the top of the street".
- **N-17** p240 "with my wrist still warm where the stranger had taken hold of it" underlines the inversion of the drover (ch-07:p113) that p221 already delivers. There is a button risk. Consider cutting p240, or ending it on what she listened to.
- **N-18 Giant fennel (low confidence).** *Narthex* pith is known for smoldering slowly (Prometheus carried fire in it). "burned fast and bright with a smell of aniseed" (p122) may be wrong on both counts, since *Ferula* is not anise-scented. Worth a check.
- **N-19 The memory at p71** (the Vermont brothers' tree lot) is resonant rather than irrelevant: hands out to a fire "among strangers" in a chapter whose payoff is a stranger. Voice-dna's chaos rule wants "uninvited and irrelevant". It also places Mara's bus stop near 22nd and Pine. ENTITY should record that, and it is not contradicted (Larchwood, ch-06:p43, is unplaced).
- **N-20** p13 "The Thyiades, the town called them, the god's wild women" is an appositive gloss of a Greek word (voice-dna §1: never glossed in an aside). It is mild. Keep it, or let the scene define them.
- **N-21 Mara's "no husband" declaration is now at 3** (ch-05:p13 "I have no man."; ch-06:p117 "I have no husband."; ch-08:p184 "There is no he."). Cap it: no fourth.
- **N-22** Philista "inspected each of us" at the cliff head (p44), and Mara is gone for what must be two hours (p74–p85). Only Kallia and Nikaso register it. It is plausible in the crowd. Optionally, have Philista eye her at p91 (she already speaks to her there).
- **N-23 Negation paragraph endings:** p27 (fixed by W-05) and p86 ("the leg gave up nothing"). One is fine.
- **N-24** p57 lists the basket's contents in one sentence (loaf, apple, wool, ivy). It is a single list, not a device yet. Watch for list-sentences in Ch.9's documents.
- **N-25** p73 "in my mouth it had the Delphian vowels, not the book's" is next to the SPENT descriptions of her Greek (breathings, pitch, Ch.7's vowel lesson). It reads as progress. Keep it as the last of its kind.
- **N-26 Kallia's "Who would I send in?"** (p106) is allowed (the question-back variant). It brushes her "never speaks of herself" evasion. Do not give her a second one before Ch.10.
- **N-27** Bible bookkeeping: the Mara block calls the pen laugh "the first laugh she shares WITH others". ch-04:p34 has "I laughed with him without knowing what at." Correct the claim. The SPENT status of the shared-laugh device stands.

---

## TRACKING DATABASES (Ch.8 deltas, cumulative with the Ch.7 audit)

### Character Fact Sheet (new or changed on the Ch.8 page)
| Character | Fact | Source |
|---|---|---|
| Kallia | gray hair to the shoulder blades, seen loose when she dances; binds her own shoes in blanket strips; carries the wineskin "on a cord"; dances "all of her at once, with no expression"; never touches Mara | p2, p40, p66, p12, p92 |
| Nikaso | small and quick, a mass of black hair, a nose once broken and set a little to the left; wears her husband's sister's new red sandals (one ruined, one saved); drinks the whole skin | p13, p18, p14, p160–p173, p86–p89 |
| Sostrata | the baker's wife (Ch.7 bath); married twenty years; the mother-in-law and the dough; sings the baker's song; her frozen cloak stands on its hem | p46–p51, p175, p190–p204 |
| Timo | very young bride, married at the vintage to a potter's son from the lower town; ivy over one eyebrow; a flask of hair oil; two right sandals (one is her mother's) | p48, p151, p166, p180 |
| Philista | leads the Thyiades; lean, old, upright; drum; despises Athens; her man "went off to the Athenians" | p44–p45, p91, p118, p200–p201 |
| The stranger (unnamed) | big; black goat-hair shepherd's cloak; mended left strap (see W-14); talks to Mara about the weather each morning at the lions | p138, p156, p218–p227 |
| Theano (unnamed) | old woman on a block by her door at the last gate but one; barley to the crows; hand on her knee | p25–p27 |
| Valens | at the corner of the last roof holding the gray, his back turned | p28 |
| Mara | cannot sing; keeps her boots on in the pen; knows leather drying; laughs with the women | p207, p137, p135, p168, p208 |

### Master Timeline
| When | Event | Source |
|---|---|---|
| ~31 Dec AD 70 | "At midwinter the women climb Parnassus" | ch-07:p187 |
| a few days after 1 Jan AD 71, dusk | the court and the rags; the lane; the crows; the last roof; the drums | p1–p29 |
| evening | the cliff stair (old snow crust); the plain; the basket tossed; the dance | p30–p73 |
| night | Mara to the cave and back (about two hours); snow begins at the arch | p74–p85 |
| night | the stair is shut by a drift; back to the pen | p108–p122 |
| late night | the sandals; the song; the heap | p123–p240 |
| first gray light | the snow has stopped; the women asleep and steaming | p241 |

### Knowledge Database (Ch.8)
| Information | Origin | Who knows now |
|---|---|---|
| The Oracle does not answer in winter; women send a man; it costs "more than you've got" | Kallia to Mara, p98–p104 | Mara |
| Mara went to the cave "to see if it was open" | Mara to Nikaso, p229–p231; Kallia infers "in there" from her knees, p93–p95 | Nikaso, Kallia |
| Mara has no husband, "not even a dead one" | Mara in the pen, p184–p188 | all the Thyiades present (town gossip by morning) |
| The stranger and Mara are "the lions" acquaintances | p219–p221 | both |
| Nobody on the page knows Valens as Lupus; Mara knows the name Valens | ch-06:p48 | unchanged |

### Plot Threads
| Thread | Status after Ch.8 |
|---|---|
| The way home (the cave) | shut again (second null test); no door word |
| The Oracle | OPENED (cost, male proxy, winter closure) → Ch.9 and Ch.12–13 |
| Money | OPENED (two brass coins) → Ch.9 |
| Kallia's son / the swept room | subtext only ("not sons", "Who would I send in?") → Ch.10 |
| Nikaso's sieve | open texture |
| Valens's danger (the notice) | not touched → Ch.9 |

---

## SUGGESTED YAML PATCHES (for entity-tracker, after the editor's fixes)

```yaml
suggested_patches:
  - entity: "timeline.chapter-8"
    action: "update"
    value: { time: "dusk to first light", season: "midwinter", year: "AD 71", note: "a few days past the turn of the year by Mara's private reckoning (ch-08:p7); January cold (p81)" }
    reason: "the page now answers the row's open question; replace the outline-sourced row"
  - entity: "meta.contradictions.CH3-7"
    action: "remove_conflict"
    reason: "Ch.8 again names no door ('Was it shut?' p95; 'To see if it was open' p231); prose wins and the tracker plan row is retired"
  - entity: "meta.contradictions.CH3-3"
    action: "update"
    value: { ch8_note: "fourth look: a pen, 'walls of stacked stone to the height of my chest and no roof' (p122); no hut. Wording drift vs herringbone (audit N-03)" }
  - entity: "kallia.knowledge"
    action: "add"
    value: { fact: "Mara went into the cave on the night of the Thyiades", learned: "ch-08:p93-p95", method: "inferred (wet knees)" }
  - entity: "nikaso.knowledge"
    action: "add"
    value: { fact: "Mara went to the cave 'to see if it was open'", learned: "ch-08:p229-p231", method: "told_by:mara-reyes" }
  - entity: "mara-reyes.knowledge"
    action: "add"
    value: { fact: "the Oracle is closed in winter; women must send a man; it costs", learned: "ch-08:p98-p104", method: "told_by:kallia" }
  - entity: "nikaso / sostrata / timo / philista"
    action: "create"
    reason: "named on the Ch.8 page with dialogue (character-bible cards exist)"
  - entity: "thyiades-stranger"
    action: "create"
    reason: "unnamed walk-on with dialogue, recurring from the Ch.7 spring mornings"
  - entity: "theano"
    action: "update"
    value: { first_appearance: { chapter: 8, source: "ch-08:p25-p27" } }
    reason: "replace the outline-sourced row with the page"
  - entity: "corycian-cave.facts"
    action: "add"
    value: { fact: "AD 71 (Ch.8): drift in the arch nearly to the lip; Mara's shovel scratches at the bend; hand in to the wrist: January cold and no more", source: "ch-08:p76-p83" }
  - entity: "mara-reyes.memories"
    action: "add"
    value: { fact: "the Vermont brothers' Christmas-tree lot at Twenty-second and Pine; she passed it coming home from the bus", source: "ch-08:p71" }
```
