# Continuity Audit: Chapter 9 (run 2, per-chapter drift audit)

**Date:** 2026-10-19
**Mode:** MANUSCRIPT AUDIT. Ch.9 is checked against Ch.1–8 as they stand on disk (all re-read in full), against the plan and against canon.
**Chapter reviewed:** `manuscript/chapters/chapter-9.md`, last written 20:24:27.
- Length: 5,892 prose words by `shape_check`, 6,065 by `wc -w`.
- **202 prose paragraphs**, with breaks after p23, p80, p127, p141 and p171.

**Paragraph numbering:** `ch-09:pN` counts prose paragraphs only. The title, the two HTML comments and the `* * *` breaks are not counted, which is the ENTITY_STATE and Ch.6–8 audit convention. So p1 is the italic manumission and p202 is "He let the gray drink first." Prior-chapter citations use the files as they stand now: Ch.1 193, Ch.2 69, Ch.3 84, Ch.4 83, Ch.5 210, Ch.6 341, Ch.7 195, Ch.8 241.

**Read against:**
- outline.md: Ledger rows 8–10, and `## Chapter 8` through `## Chapter 11`.
- STATE.yaml: guardrails, canon, resolved decisions, ARCH-1…18.
- foundation.md §3 (Valens's history and the notice's legal basis).
- voice-dna.md: §1, Dialogue conventions, VOICE UNDER PRESSURE (Ch.9 = level 1, brief) and §3b.
- character-bible.md: the Mara, Valens, Kallia and Euthydikos cards, including their Ch.9 blocks; the Ch.5–9 walk-on and spent notes; every at-risk block (after Ch.1, 3, 5, 6, 7, 7 cycle 1, 8, 8 cycle 1 and 9) and the at-risk table.
- voice-bank/samples 01–13, read in full.
- ENTITY_STATE.yaml. On disk it is `last_updated_chapter: 8` and carries **0 `ch-09:pN` cites**. Its 25 Ch.9 mentions are all plan rows (`source: outline:ch-09`). I treated them as unverified, so every Ch.9 fact below comes from the page.

**Mechanical baseline (re-run for this audit, read-only, `bash tools/check_chapter.sh 9`):**
- Style is clean: simile 1.9/1k, adverb 2.7/1k, em-dash 1 (p18, a true interruption), foreshadow 0.
- Grammar clean. Rhythm 0 flagged. Show/tell no flags (dialogue meter 27.0%).
- Voice-wear strict clean. Tic gate clean, gesture layer included. Echo scan 0.
- And-chains 3 (cap 9). Credential asides 0. Negation pivots 0. 'So' openers 0. 'before I decided' 0.
- Metaphor: fig 2.9/1k, median sentence 15, 6.9% of sentences over 40 words.
- Shape audit across 9 chapters: CLEAN, and `--strict` is clean. Ch.9 computes as `narrative` → `punch`, 5 breaks, dialogue 28%, median 15.
- My own sub-gate sweeps were n-grams of 3+ words against Ch.1–8 and the voice bank, keeping only grams with 2 or more content words. They found 4 voice-bank lifts that the 5-gram echo scan cannot see (W-03, W-04), plus one prior-chapter structural repeat (W-04).

**Total findings:** 42. **CRITICAL: 1 | WARN: 11 | NOTE: 30**

Every ledger cell and every outline beat is met, all three documents reveal or texture as planned, and the gates are clean.
- **The one CRITICAL:** a fourth use of a narrator move the bible caps at three, the command echoed as compliance ("Tell them…" / "He went and told them"). It is a single-clause fix.
- **The WARNs fall into five groups:**
  - **Notice timing:** ENTITY P5 is only half-closed by the page.
  - **Craft logic:** Mara's heat argument inverts itself between p37 and p49.
  - **Voice-bank and spent-move leakage:** "it will hold" (sample-10, the Ch.15 line), "where it broke" (sample-11), "office in Phocis" (sample-04), the refold "along its old folds" (sample-12 and Ch.2), and the Delphian-vs-book vowels.
  - **Repeated staging:** Kallia's hearthstone exchange copies Ch.7's broken-jar template, and the price of the god is itemized twice.
  - **Smaller seams:** a wink in the curse tablet's name, a comprehension jump at the board, a father/grandfather slip, and bible quotes that are not on the page.

None of the proposed fixes adds words except W-09 (+12). Their net effect is about −30 words, which leaves the chapter at about **5,860**, still above the 5,800 floor.

---

## Scorecard by category

| Category | Result |
|---|---|
| (a) Beats / ledger | **PASS.** Collage ✓. Ch.8 and Ch.10 are both Single-scene, so there are no consecutive repeats. **Open:** p1 is an italic document, and its first sentence is 23 words → `narrative` ✓. **Close:** p202 is 6 words → `punch`, and it is a single-sentence closing paragraph, which the ledger allows for Ch.9 ✓. **Breaks:** 5 ✓. **Dialogue:** 28% (shape) / 27.0% (meter), against a band of 25–35 ✓. **Gear:** median 15, mid ✓. **Length:** 5,892 against a target of 6,400 (range 5,800–7,000) ✓. **Beats:** 1, the manumission and its paramone clause, p1 ✓ (REVEAL). 2, NON-NEGOTIABLE, the bronze incense stand mended cold with a rod, wax and pitch, no welding, for coins, p28–p151 ✓. 3, NON-NEGOTIABLE, the pelanos, the goat, the Delphian sponsor and the man, p58–p61 ✓; "I know about the man" respects the Ch.8 handoff (N-01 of the Ch.8 audit) ✓. 4, the notice, p172 ✓ (REVEAL; see W-01). 5, the curse tablet as texture, p128–p141 (see W-08). 6, NON-NEGOTIABLE, Valens reads the notice and walks off at a walk, p197–p202 ✓. The chaos moment (all-or-nothing: the join redone three times) is at p92–p125 ✓. The emotional surprise (money and contempt in one breath; the wiped hand) is at p150–p154 ✓. The writer warnings hold: no condition-report form, no coins counted aloud, and the final punch is a plain observed action ✓. |
| (1) Character consistency | **Valens: PASS.** The scar is not shown in his live scene (p103–p120). It reaches the page only through the notice, "on the back of the right hand from a wound badly stitched" (p172), which matches ch-06:p42 (right hand, stitches set too far apart). His speech is short and level, with no simile, and his questions are practical ("What for?", "How long will it…?"); see W-03 for one wording. His attention is on who is watching (p110). Literacy stays **unconfirmed**: "while a slow man might read it once, and then as long again" (p199) measures time and does not confirm reading. This agrees with ch-06:p222–p224, where he asks what the inscription says and does not admit to reading, and it leaves Ch.11's reveal intact. "Greek like a foreigner" (p172) matches ch-06:p81. "Thracian" is new to Mara, and "North." (ch-06:p205) agrees with it. "About thirty" sits within foundation's ~32. **Kallia: PASS.** She does not sit (she scours, p159). She does not touch Mara: the basin and the clay are *set down* (p164). She asks practical questions ("Who paid?" / "Into your hand?" / "Who takes the goat up?"). Her varied reply is an act, as the Ch.8 note asked (p164). She uses one "Then" retort (p170), which is the cap, and she never speaks of herself. See W-06 for the staging. **Euthydikos: PASS against his card.** He talks of Mara in the third person through the slave (p36, p46, p55). His chilblains are at p39 and p76–p78. He never touches her and he wipes his fingers (p150–p151). He is a witness on p1 and "likes it in stone" (p22), and he gives no thanks and names no price first (p66). Card quotes that are not on the page are logged in W-11. **Mara: PASS.** Her Greek is uncontracted throughout. There is no English, so the CONTINUITY COMMITMENT holds. Credential asides: 0. |
| (2) Timeline | **PASS.** The inscription is dated Poitropios (≈ Dec/Jan) and the cutter says "Last month" (p13), so it is now Amalios (≈ Jan/Feb). That falls after Ch.8's "a few days past the turn of the year" (ch-08:p7) and before the god's return in Bysios ✓. "the almond trees … had come into flower in the last week" (p129) is right for Delphi in February ✓. The mistress's mirror broke "at midwinter" (p98), which agrees with Ch.8 ✓. **"First carts since the snow" (p189) is right:** the Boeotian road was "under snow. All of it." in November (ch-06:p149), the roads were "shut" at midwinter (ch-08:p46), and Kallia's "Once the road's clear of snow" (ch-08:p99) ties the god's season to the thaw. The page never states the day the snow cleared, and it does not need to. Internal span: Day 1, the wall and the court; Day 2, the core and the rod ("the first morning", p83; "Late in the day", p86); Day 3, the wax and four fills (p90–p127); Day 4, the inspection (p142), with the spring at dawn (p129) most naturally that morning; then the square (see N-04). |
| (3) Information flow | **WARN ×2** (W-01 notice timing; W-09 comprehension). Otherwise clean. "I know about the man" comes from Kallia (ch-08:p101) ✓. "Kallia's Syracusan" (p35) and "From Syracuse" (p83) are town knowledge after the registration (ch-07:p172) ✓. Nobody in Delphi calls Valens "Lupus", and the men at the board joke about the name without connecting it to the mule-man (p190–p194) ✓. Mara's recognition is never stated, and every clue to it is on the earlier page: the scar (ch-06:p42), Latin to his mules (ch-06:p45), his "Greek as foreign as mine" (ch-06:p81) and mules that "came from Corinth" (ch-06:p200) ✓. She reads the Doric manumission as a classicist would, and the cutter can read his own work ✓. Valens knows she reads (ch-06:p328), so the look at p200–p201 carries ✓. Kallia learns the price only from Mara (p166). The "door" word enters Mara's narration here for the first time (p23; N-01). |
| (4) Objects and money | **PASS.** Ch.5 began with three taxi coins (ch-05:p55). The 100-drachma piece went to the guide (ch-05:p55–p64), which left two: "the poet" (the bigger, the old bearded head, ch-06:p107–p110) and "the other" (p171), as in ch-08:p122 ✓. The fee is "The smith's price" (p149) = "Three drachmas" (p67), since the clay was paid separately (p76) and the rod obols were the priest's (p81). The pelanos is "a stater" (p58), or two by the smith's mockery (p59). The goat is "More than that" (p178), and the sponsor's present and the man are still unpaid. **It adds up to not enough**, which is the chapter's point. She owes Valens an obol and is holding it (p119, p201) ✓. Nothing she had in Ch.8 has gone missing. The watch is with Valens and is not mentioned (N-17). |
| (5) Conservation craft | **PASS with one WARN** (W-02). The lead solder ringing the bowl, dressed down, is accurate (p31), and so is lead letting go at about 327°C long before bronze runs (p37, p44). The gas porosity at a brittle cast break is right (p45). So is the smith's cast-on with a clay collar (p28, p75). The burnt clay core is raked out (p84). The filed internal rod is a cold join, with no welding (p86). Beeswax toned with lamp soot and earth (p91–p93), wax hardened with pine pitch (p121), the wax gloss reading as "a thin gold thread" in raking sun (p92), and the stippled fourth fill matching an orange-peel patina (p122, p125) are all real restorer practice. Pitch as a gall salve for a mule is period-correct. The curse is on lead sheet folded and pierced with a nail (p134) ✓. See N-03 on "No fire" and the lamp. |
| (6) Manumission / history | **PASS.** The formula is authentic in every clause: archon and month dating; "sold to Apollo the Pythian a female body"; "home-born"; price and "he has the whole price"; "entrusted the sale to the god"; "free … not to be laid hold of … doing what she wishes and going to whom she wishes". The paramone clause ("remain with Xenon as long as Xenon lives … without complaint") is authentic, and so are its sanction (beating, selling) and voidance clause, the guarantor "according to the law", and the priests plus private witnesses. Three minae is a typical price. The cutter's account is accurate too: the god as fictive buyer, and the wall as the public record that defeats a resale (p13–p19). Other historical details hold: the goat must tremble "from the hooves up" (Plutarch, *De def. or.* 437A–B; p60); the pelanos and the city-by-city tariff (p58); the proxenos-style Delphian sponsor (p60); the runaway-notice form with two rewards, "in a sanctuary or in the house of a man able to answer for him" (p172; cf. P.Paris 10); and the defixio to "Hermes the Holder and to Earth" (p128). |
| (7) NO FORESHADOWING | **PASS.** The gate reads 0. On a manual read, the "would" forms are counterfactual (p28, p45, p121), and "was never going to be hard enough" (p102) is an in-scene inference. The forecasts are in speech (p80, p116, p155), and the narration never reaches forward. |
| (8) NO TICS | **Mechanical: PASS. Manual: CRITICAL ×1** (C-01, the command echo) **and WARN ×3** (W-05 the spent Greek-sound contrast, W-06 the hearthstone template, W-07 the list given twice). Caps that are held: "said/told the [non-listener]" is 1 (the smith "told his clay", p59); Kallia's "Then" retort is 1; "the one / the only" is 1 (p23); "as though" is 1 (p33); feet-first looks reach 3, at the cap (p24); hinge openers 0; lying-awake coda 0; laughs 0; cloth smells 0; taste reactions 0. Watch items are at N-09 to N-13. |
| (9) Spent moves (every bible block) | **WARN ×2** (W-05; W-04's refold). Clean against the Ch.5, 6, 7 and 8 spent lists and the at-risk table (each was checked string by string and by shape). Notable holds: the emotional peak is not a laugh (p153–p154, as asked after Ch.8); the unprompted memory breaks its old frame (the crayon smell inside a sentence, p91; the hardware store, a place with no person in it, ending on an act, p85); there are no callback pointers (one borderline, N-24); "Maira" is not in any walk-on mouth; no Theban appears; the flashlight is not mentioned. |
| (10) Voice-bank lifts | **WARN ×2** (W-03, W-04): four lifts from samples 10, 11, 04 and 12. Three structural mirrors (samples 03, 08, 11) are designed, and their wording is distinct (N-26 to N-28). |
| (11) Voice drift | **PASS.** The gear is mid. Asides are dry and varied in form ("I think in the hope that I would ruin it", p84; "having no beans left to examine", p57; "which was where I was from, now", p54). They die at the notice, as voice-dna's map wants for Ch.9 (pressure level 1: "one plain observed action, no comment", p195–p202). The 1998 comparisons are an LP's scratches, a crayon on a radiator and pocket-patting; see N-06 and N-07 for two domain repeats. The ugly sentence is kept (p84). |

---

## PRIORITY: UNRESOLVED ENTITY_STATE CONFLICTS (processed first)

ENTITY on disk covers Ch.1–8, and nothing in it comes from the Ch.9 page.

| ID | What Ch.9 does to it | Verdict |
|---|---|---|
| **P5** notice timing (outline Ch.12 "within the month" of autumn 70, set against Valens working openly in Delphi through Ch.6–8) | The page now supplies the delay: "With the oil from Thebes. First carts since the snow, and the clerk had it on the wall before the oil was off." (p189). That agrees with ch-06:p149 and ch-08:p46. **But** the notice is dated "in the month Boathoos" (p172), and Boathoos is Mara's own arrival month (ch-04:p24). In that month Corinth letters reached Delphi by ship "in weeks" (ch-05:p95, ch-05:p108), and the sea stayed open until November (ch-06:p69). | **Half-closed. WARN W-01.** A one-word fix closes it. |
| **CH8-1** the decision to consult is not shown in Ch.8 | It is shown in Ch.9: "I had climbed the Sacred Way that morning to find a priest" (p3), the question composed (p23), and "Tell me first what a question to the god costs." (p56). Kallia never refers to being told of an intent. She hears the price after the fact (p166). | **Recommend RESOLVE** (the page satisfies the outline's "Builds on Ch.8: her decision to consult"). |
| **CH3-7** (RESOLVED: "the page never names the door") | Ch.9 names it in Mara's narration twice: "*Where is the door I came in by, now it is shut?*" and "questions about doors" (p23). This is a natural turn (she is drafting an oracle question, and the god's answer in Ch.13 is about a painted door), and it is not a contradiction. | **Record the new fact**; the resolution's wording is superseded (N-01). |
| CH4-3 (fleece/jacket), CH4-4 (inscription), CH5-3 (film), CH5-4 (microcassette), CH6-5 (first attempt), CH8-2 (Theano) | Ch.9 touches none of them (no 1998 garment, no cave inscription, no Pentax, no tape, no crows). | Unchanged, open. |
| CH1-2, CH1-3, CH2-1, CH2-3, CH2-4, CH2-5, CH3-1, CH3-2, CH3-3, CH4-2; P1, P3, P4 | Not touched. | No change. |

---

## CRITICAL ISSUES (must fix before the evaluator)

### [C-01] The command echoed as compliance, a fourth use book-wide (cap: "no fourth anywhere")
- **Audit:** NO TICS / spent narrator move (hand-enforced; the gate's detector, pipeline #15a, is not built).
- **Evidence:**
  - ch-09:p89 (Mara): "Tell them it is for the god."
  - ch-09:p90: "**He went and told them**, with his mouth close to the clay, and in the morning he brought me a yellow cake of it…"
  - Book-wide count before Ch.9 is **3, SPENT** (character-bible.md, at-risk after Ch.7 cycle 1): ch-01:p48/p49 "Stand on the mat." / "I stood on the mat."; ch-06:p191/p192 "Sit back." / "I sat back."; ch-07:p65/p66 "Say it again." / "I said it again." The rule reads "**SPENT: no fourth anywhere in the book.** Show compliance by its result … or not at all."
  - The direction is reversed (Mara gives the order and the bee-man complies), but the narrator move is the same: the order's verb comes back as the compliance. The writer, the disruptor and the bible's Ch.9 counts all report "command-echo 0", so this one slipped past every pass. Ch.4 and Ch.5 set the precedent that a closed device used past its cap is CRITICAL.
- **Minimal fix (fresh against Ch.1–8 and the voice bank):** p90 "He bent to the nearest hive and spoke into the clay, and in the morning he brought me a yellow cake of it wrapped in a fig leaf, and a sherd with lamp soot in it scraped off the kitchen wall."
- **Cascade:** in the bible's at-risk after Ch.9, "Telling the bees … narrated once in Ch.9 ('He went and told them…')" must be re-quoted. The near-form at p44/p45 is a NOTE (N-12).

---

## WARN ISSUES (fix before the evaluator)

### [W-01] The notice's posting month leaves the five-month delay unexplained (ENTITY P5)
- **Audit:** information flow / timeline.
- **Evidence:**
  - ch-09:p172: "*Runaway, in the autumn, … Copied from the notice posted at Corinth in the month Boathoos.*"
  - Boathoos is the month Mara arrived (ch-04:p24, "Boathoos."). In that same month "Letters have come up from Corinth with the ship" (ch-05:p95), and news reached Greece "in weeks, by sea, and the sea was still open" (ch-05:p108). The last ship left Kirrha only in November (ch-06:p69).
  - A Boathoos copy should therefore have reached Delphi before the snow. The page's explanation, "First carts since the snow" (p189), fits only a notice posted after the sea and the Boeotian road had shut (ch-06:p149, ch-08:p46).
  - The outline's knowledge note (Ch.9 beat 4) depends on this delay: "which is why Valens could work openly through the winter of Ch.6–8 and reads it here as news." Foundation §3 has the notice go up "within the month" of the freedman's autumn visit, so a late-autumn month is canon-safe.
- **Minimal fix (one word, fresh):** "…posted at Corinth in the month **Dadaphorios**." (Dadaphorios ≈ Nov/Dec: after the sea shut and with the road already under snow, so first carts is the first chance.)
- **Optional second fix:** cut "in the autumn," so the notice opens "*Runaway from the household of Quintus Arrius Celer at Corinth: …*". As written, a notice posted a year after the frame (foundation: framed in 69) says "in the autumn" without a year. A reader who remembers that Valens was hauling wood to Kallia "last winter" (ch-06:p50–p51) may take it to mean autumn 70, which the page contradicts.
- **Cascade:** ENTITY P5 → RESOLVED by the page. Celer's timeline row: notice posted Dadaphorios AD 70. Ch.12's knowledge path ("within the month") is unaffected.

### [W-02] Mara's heat argument inverts itself (p37 against p49), and her own fill disproves the second half (p93)
- **Audit:** conservation craft / internal logic. Mara is the expert, and a reader will check her.
- **Evidence:**
  - ch-09:p37: "When the shaft is hot enough for new bronze, **the heat will climb to the top**, the lead will let go".
  - ch-09:p49, answering the smith's "It'll stand till the first warm day and then lie down in the incense": "The break is at the feet. The coals are in the bowl, at the top. **The heat does not come down so far.**"
  - ch-09:p93: "by noon the sun on the paving was warm enough to make it softer". The fill softens in February sunlight alone.
  - Heat travels both ways along the same shaft, and wax softens at a few tens of degrees against lead's 327°C. The smith's objection is the right one, and her answer is the wrong one. The correct answer is already in her plan (p47): the rod carries the load, and the wax is cosmetic.
- **Minimal fix (p49, fresh):** "The rod holds it up. The wax only hides the crack."
- **Cascade:** p50 ("And when some slave knocks it over again?") still follows. p102's resin motive (a thumbprint shows) is now purely about appearance, which is what the fills are for. This saves 11 words.

### [W-03] Voice-bank lifts in the mending talk: "it will hold" (sample-10) and "where it broke" (sample-11)
- **Audit:** voice-bank lifts (zero allowed). Both are below the echo scan's 5-gram floor.
- **Evidence:**
  - sample-10 (the Ch.15 first-union anchor), Valens about the rope bed: "**It will hold,**" **he said.** / "It will not."
    - ch-09:p69 (Mara): "That is why **it will hold**."
    - ch-09:p114 (Valens, about the mend): "How long **will it hold?**" **he said**.
    - So in Ch.9 Valens, the same speaker, uses the same verb, frames it the same way and tags it the same way, six chapters before his scripted line. "hold/held" about the mend now runs ×5 in the chapter (p41, p69, p96, p97, p114).
  - sample-11 (the Ch.20 visible-seam anchor), the customer's key line: "I want to see **where it broke**." → ch-09:p51: "It will break again **where it broke** before". The phrase is the same and so is the theme, in the chapter that sets up Ch.20.
- **Minimal fix (all fresh):**
  - p69 "It is not a smith's work. That is why it will last."
  - p114 "How long will it stand?" he said.
  - p51 "It will come apart along the same line," I said, "and in no new place, and the next mender will have nothing to undo but wax."
- **Cascade:** the mistress's "Does it hold?" / "It holds." (p96–p97) can stay (no sample collision), and the chapter's "hold" count drops to 3. Valens's "Somebody will." (p116) still answers "If nobody knocks it over."

### [W-04] Two more voice-bank lifts: "office in Phocis" (sample-04) and the refold "along its old folds" (sample-12, plus Ch.2)
- **Audit:** voice-bank lifts and prior-chapter structure.
- **Evidence:**
  - sample-04: "in a magistrate's **office in Phocis** with flies walking on the shutters" → ch-09:p23 "He was the one **office in Phocis** that took questions about doors".
  - sample-12 (the Ch.10 no-pull close): "Kallia took the letter … and **folded it along its old creases**" → ch-09:p141 "I **closed it up along its old folds**".
    - ch-02:p67 already has "I folded it back along its own creases" (the consulate carbon).
    - Ch.10's letter scene is next, and its sample owns this gesture, so Ch.9 spends it one chapter early and makes it two on the page.
- **Minimal fix (fresh):**
  - p23 "Whether I believed in Apollo was beside the point. He kept the one window in Phocis that took questions about doors, and the cave had been shut to me twice." (This keeps "the one" at 1.)
  - p141 "I shut the sheet over on itself and handed it back to him, with the nail, and he ran off up the steps…"
- **Cascade:** Ch.10's refold, if it is used, must be worded fresh against both Ch.2 and Ch.9.

### [W-05] The Delphian-vowels-against-the-book's contrast is back after being spent
- **Audit:** spent moves.
- **Evidence:**
  - ch-09:p23: "I tried it in a murmur **with the Delphian vowels, and again with the book's**".
  - The prior uses:
    - ch-04:p10 "the way the books printed it";
    - ch-07:p59–p61, the vowel lesson ("the vowels a Dutch scholar … had decided it ought to have");
    - ch-08:p74 "my mouth made it Delphian", which the Ch.8 repair kept **in place of** the near-identical "in my mouth it had the Delphian vowels, not the book's" (Ch.8 audit N-25: "Keep it as the last of its kind").
  - The bible marks it SPENT twice: "The breathings-and-pitch description of Mara's Greek … SPENT" (after Ch.7) and "the book-vs-mouth Greek contrast" (after Ch.8 P6–P11).
- **Minimal fix (p23, fresh; it also saves 10 words):** "I tried it over in a murmur, and it sounded like somebody patting her pockets for a key."
- **Cascade:** none. The pocket-patting simile stays. Combine this with W-04's p23 edit.

### [W-06] Kallia's hearthstone exchange re-runs Ch.7's broken-jar template
- **Audit:** NO TICS (a repeated scene shape).
- **Evidence:**
  - ch-07:p123–p127 runs: objects laid on the hearthstone; Kallia "looked past them, at my wrist"; "Who?"; "Did he touch you?"; "Only my wrist."
  - ch-09:p159–p163 runs: "she looked at my hand before she looked at my face"; coins tipped on the hearthstone; "Who paid?"; "Into your hand?"; "Onto it. From above."
  - Both have the same five steps in the same order: the hearthstone, Kallia's eyes going to the body part first, a one-word *who* question, a touch question, and Mara's two-word answer.
  - The touch question is Kallia's to ask, and it is good. The staging around it is the copy. The look-at-the-hand-before-the-face clause also pre-echoes p200's "I looked at his face".
- **Minimal fix (p159, cut 11 words; fresh):** "Kallia was in the court at home, scouring the big pot with sand. I opened my hand over the hearthstone and tipped the coins out on the stone."
- **Cascade:** p160–p164 are unchanged. Bible Kallia Ch.9 block: re-quote.

### [W-07] The price of the god is itemized twice in one chapter
- **Audit:** NO TICS (listing/pricing device; the outline warns against a catalogue form).
- **Evidence:**
  - ch-09:p58–p60, Euthydikos: "First the pelanos … Then the goat … And a Delphian to stand for you … And a man to carry the thing in".
  - ch-09:p166, Mara to Kallia: "He says a stater for the god … **And a goat that shakes. And a Delphian to stand for me, who will want a present, and the man.**"
  - The second pass repeats the list and the "And a…" anaphora within about 1,100 words. The bible already marks the list SPENT after Ch.9, counting both.
- **Minimal fix (p166, fresh; −13 words):** "He says a stater for the god," I said, with my hands in the water, "and a goat that shakes, and the rest."
- **Cascade:** Kallia's "Who takes the goat up?" (p168) still has its cue, and "The man, I suppose." (p169) still works.

### [W-08] The cursed weaver is named "Thraitta", which means "Thracian woman", one section before the Thracian runaway
- **Audit:** outline Ch.9 beat 5 ("A lead curse tablet against a rival's loom. **It means nothing.**"; "the curse tablet is the deliberate texture exception"); the spirit of NO FORESHADOWING; and the Ch.8 lesson about winks (W-05 there).
- **Evidence:**
  - ch-09:p128 "*I bind Thraitta the weaver … and I hold her under the lead*"; p138 "Thraitta."; p139 "There's no Thraitta at the spring."
  - Θρᾷττα is the stock name for a Thracian slave woman. Mara reads Greek, and so does any classically minded reader.
  - Two sections later the notice gives "a Thracian … whoever takes him should take him with others" (p172). A binding curse on a Thracian woman, set right before a Thracian wanted for capture, reads as planted. The document stops meaning nothing.
- **Minimal fix (fresh name, no ethnic sense):** "Glykera" at p128, p138 and p139.
- **Cascade:** bible Ch.9 walk-on note (Thraitta, mention-only) → Glykera.

### [W-09] Comprehension jump: six men's quick banter at the board, all caught whole
- **Audit:** information flow (Mara's Greek). This is the same class as Ch.8 W-06, which was fixed there with one clause.
- **Evidence:**
  - ch-09:p182–p194: thirteen lines from "five or six" men trading quips, each rendered whole, with no loss. The bee-man's undertone to his hives is also caught whole (p83).
  - The earlier record: ch-06:p311 "I lost words out of everything he said" (mountain Greek, November); ch-08:p112 "for a while I could not sort one voice from the next" (after the repair). Since then she has had about six weeks of house and street Greek. Growth is plausible; a perfect take on overlapping street wit is not.
- **Minimal fix (p181, +12 words, fresh):** add after "…settled among themselves what it said." the sentence "They talked across one another, and what reached me came in pieces."
- **Cascade:** none. The lines read as the pieces she caught.

### [W-10] The letter-cutter says "grandfather", then "father"
- **Audit:** internal consistency (walk-on speech).
- **Evidence:**
  - ch-09:p9: "He made me leave his **grandfather** off."
  - ch-09:p11: "And son of Xenon, it ought to say … A man frees a girl and haggles with me over his own **father**."
  - Xenon's father, Euangelos, *is* on the stone (p1, p10). Only the grandfather was cut, so the punchline names the wrong man.
- **Minimal fix (fresh):** p11 "…haggles with me over his own grandfather."

### [W-11] The bible's Ch.9 blocks quote lines that are not on the final page
- **Audit:** bookkeeping. Dialogue Polish and the Ch.10–13 writers work from these blocks.
- **Cause:** character-bible.md was last written at 20:06, and chapter-9.md at 20:24, after the disruptor.
- **Not on the page:**
  - **Valens block:** "with two fingers, slowly, and she stood for it" (the page has "Her ears were flat. When she swung her head round to bite him he put her nose away with his elbow and went on working.", p104); "Warm it first. It'll crack cold."
  - **Kallia block:** "Ends 'with her shoulders to me', the scraping continuing". The page ends the opposite way: "Kallia's sand had gone quiet while I tied it." (p171).
  - **Mara block:** "a soot smear".
  - **Euthydikos card:** "I'll pay a smith a smith's price. I'll not pay a woman a smith's price for doing it with wax." (the page has "A smith's price is for a smith's fire. I have wax from my own bees.", p68); a second "Ask her,"; "Then you have the worst of it."
  - **Walk-ons:**
    - the cutter's "The god's the buyer, so nobody can say afterward she bought herself" (on the page this is *Mara's* p14 "So that nobody can say she bought herself.") and "Nobody ever lost a wall." (the page has "I've never had to cut one of these twice.", p19);
    - the bee-man's "…, you know.";
    - the boy's "Is it a letter? … What's written on it? Is it a treasure? Who's it from?" (the page has "Is there money in it?" / "What's it say?" / "Which weaver?");
    - the woman at the lions' "Whoever buried it meant it to stay buried." (the page has "It's been given to the ones below, and they don't want it handed round.", p131);
    - the goat man's "Come back with a man. I'll keep her warm for you." (the page has "Send whoever's leading her up, with the rest of it. I'll keep her warm till then.", p180).
  - **At-risk after Ch.9:** the "A man as the requirement" closure cites the goat man's line, which is gone, so the page count is Kallia ×2 (Ch.8, Ch.9) plus Euthydikos. The spent craft wording lists "stood proud" and "squeeze-out", but neither is on the page (the disruptor cut both). "squeeze-out" is also Mara's card vocabulary and sample-11's Ch.20 word, so marking it spent would wrongly bar Ch.20.
- **Fix:** re-sync every Ch.9 block to the page after the editor applies this audit, quoting by script as was done for Ch.6–8. Also correct the counts it states ("command echo 0" → 1 before C-01's fix; telling the bees narrated "once" → re-quote).

---

## NOTES (polish, or for later chapters)

- **N-01 The door is named.** p23 is the first time Mara's narration says "door" for the crack. It is natural here, and it matches Ch.13's "door painted on a dead man's house". For the tracker, this supersedes CH3-7's "the page never names the door". No manuscript action.
- **N-02 Valens's literacy.** p199's "while a slow man might read it once, and then as long again" is exactly the right hedge, and the bible approves it. Keep it. Do not add a lip-move or a finger on the board.
- **N-03 "No fire" (p47).** She still warms a knife over a lamp (p91) and pours hot pitch-wax into the bronze (p121). That is not the smith's fire, but a pedant may object. Optional: p47 "No forge," I said.
- **N-04 The dawn try left hanging (p127 → p142).** "I wanted one more try at dawn" is never resolved, and the spring scene that follows is "barely light" with her jar. If any words are added to the chapter, this seam is where they belong. Optional opener for p142 (fresh): "Kallia's jars took the dawn. Once the sun was full on the court…". That also places the spring scene on inspection morning.
- **N-05 Length.** The chapter does not read thin. The mending was trimmed by the disruptor and still carries; the notice section is short by design (pressure level 1); Kallia's scene is brief and should stay brief before Ch.10, which is hers. The fixes above net about −30 words, leaving about 5,860, still above the floor. **Do not pad.** The only place where a sentence would be earned is N-04.
- **N-06 "shiny as boiled sausages" (p39).** It repeats ch-01:p4's "the pink of boiled ham" (inflamed skin as boiled pork) and the "shiny as" frame of ch-03:p49 ("shiny as olive pits"). voice-dna §1 says no comparison is used twice. Fresh: "red and swollen across every knuckle with chilblains, tight and glossy as cherries".
- **N-07 Comparison domains.**
  - **The radiator:** "a red crayon left on a schoolroom radiator" (p91) is the fourth radiator in Mara's 1998 material (ch-01:p163, ch-05:p108, ch-06:p164).
  - **School:** it is the comparison source three chapters running (ch-07:p185 Dunphy, ch-08:p45 the teacher at the classroom door, ch-09:p91).
  - Rotate both out in Ch.10.
- **N-08 Memory loss as a beat.** "its name had gone, and I filed through most of an afternoon hunting for it" (p85) is the second time a 1998 particular goes missing (ch-07:p184, the zip code). It is a legitimate arc thread. Cap it at 2 and do not stage a third.
- **N-09 "brought [X] down" ×3:** "brought his gaze down to me" (p68), "brought my eye down level" (p122), "brought his face down to it" (p148). Vary p148 (fresh): "He bent so close to it that his beard brushed the bowl, and looked at my finger and at the bronze around it."
- **N-10 The bee-man.** He is referred to by role 14 times, and his ear-to-the-hive beat appears twice (p82, p124). voice-dna says no character gets the same beat twice in a chapter. Vary p124: "She's cut herself." The bee-man was bent over a hive. "On his bronze…" If he returns for the bowl, name him (the Ch.8 role-label lesson).
- **N-11 "a bay tree in a pot at the door"** appears verbatim at p22 (the directions) and p24 (the arrival). Vary p24 (fresh): "The bay tree stood in its pot by the door, and a slave on a stool beside it was shelling beans into his lap…"
- **N-12 "Look at it." / "Everyone had looked at it but the priest." (p44–p45)** is the near-form of C-01. It is defensible, because the point is that the priest did *not* look. Keep it, but do not let a second echo stand beside it.
- **N-13 Section 2 ends on a walk-on's parting quip** ("When it lies down … send to me. I'll bring the lead.", p80). It is acceptable once, and it pays off at p155. Watch for walk-on punchlines becoming the section button.
- **N-14 The cut thumb vanishes.** It is laid open at p123 and does not come back at the payment, the washing or Kallia's look. Optional: one sting in the basin at p165.
- **N-15 Ch.10/11 handoff.**
  - (a) Outline Ch.10 has Kallia's letter come up "with the first carter of the year" after sitting "at Kirrha harbor all winter". Ch.9 has already spent "First carts since the snow" (p189), and the Kirrha road was open all winter (Valens hauls on it, p103). Ch.10 must word the arrival freshly and give the letter a reason to have sat at Kirrha.
  - (b) The goat man is keeping a she-goat "warm till then" (p180), but outline Ch.11 sends them to Kirrha for a goat. Close the Delphi goat in Ch.11 by price, or make it the goat.
- **N-16 New open threads (tracker, not motifs):** Euthydikos's bowl ("When I send", p155); the mistress's mirror via "the kitchen door" (p98, p157); the obol owed to Valens (p119, p201). The outline schedules none of them, so pay them off as texture or let them lapse quietly, and never as a callback pointer.
- **N-17 The watch.** Mara meets Valens (p103–p120) and owes him an obol, with no flicker of the watch in his pouch. Outline Ch.11 has her wanting it back. This is optional and needs no pointer; a glance at his belt would be enough. Leaving it out is defensible.
- **N-18 Returning to the scene of the beating.** She stands under the temple terrace (p3), near the ramp where she was hauled off the step and beaten (ch-05:p73–p88), and registers nothing. Optional: one body beat. A callback pointer is SPENT, so do not name the beating.
- **N-19 The men at the board fail to link the mule-man.** This is plausible: the town knows him as Valens and not as a Thracian. But Kallia has dealt with him for two winters and has seen his hands. Ch.10–11 should account for what Kallia makes of the notice, or keep her from seeing it.
- **N-20 Valens's wipe** ("He wiped his fingers on the gray's mane", p113) comes 37 paragraphs before the priest's wipe, which is the chapter's anchor gesture (p151). It dulls the peak slightly and invites a comparison the page does not mean. Optional (fresh): "He hooked the pot off the post and broke the cake of pitch in it with the haft of his knife…"
- **N-21 The p129 phrase "the water was still in January"** can be read as stating the month. Optional (fresh): "the water had stayed in January".
- **N-22 Kallia's "Then you'll want…" (p170)** is both her one "Then" retort and a "Then you…" reply shape (at-risk after Ch.1). Both caps are reached for Ch.9.
- **N-23 "somebody" ×4 in narration** (p23, p28, p31, p71). Hold incidental uses down. p71 could be "Above us someone in a long hem had stepped out onto the gallery".
- **N-24 A borderline pointer:** "and the cave had been shut to me twice" (p23) names earlier scenes. It reads as a reason rather than a rhyme being pointed at, so it stays, but it is the chapter's one.
- **N-25 The money units.** A stater is two drachmas on the standard Delphi used, but the page never says so, so a reader cannot tell whether three drachmas covers the pelanos. The ambiguity serves the chapter. Leave it.
- **N-26 A structural mirror of sample-11 (Ch.20).** The priest hunting the line with a swollen finger (p144–p148) is the designed inverse of sample-11's customer who "traced the line with her fingernail". The wording is distinct ✓. Ch.20 must stage its customer's touch differently (add this to the bible's redo-the-seam note).
- **N-27 A structural mirror of sample-03 (Ch.13).** The goat's shiver is explained (p60) and demonstrated (p176). Ch.13 shows it only and must not explain again (the bible already says this).
- **N-28 A structural mirror of sample-08.** The coin drop "so that his fingers stayed clear of my palm" (p150) echoes the bank's watch hand-off "without touching my fingers". This is the outline's anchor, and the wording is distinct ✓. Later Valens hand-backs of the watch (Ch.11/18) must not use the no-touch-at-the-palm frame.
- **N-29 History, on two notice details** (no action). The original at Corinth, a Latin colony, would have been in Latin with Roman dating and sesterces. A Delphian clerk's copy in drachmas, dated by a Delphic month, is the right rendering. The Aphrodite-on-a-tortoise caryatid mirror (p98) would be an old heirloom by AD 71, which suits "my mother's".
- **N-30 The olive-picking gloves (p78).** Gloves were known in Roman olive harvesting (Varro's *digitalia*), so the priest's sneer is period-sound. No action.

---

## TRACKING DATABASES (Ch.9 deltas, cumulative with the Ch.8 audit)

### Character Fact Sheet (new or changed on the Ch.9 page)
| Character | Fact | Source |
|---|---|---|
| Valens | delivers split wood to the priest's woodshed by the rear gate; treats a saddle gall on the gray with pitch from a pot on the gatepost; "The new saddle's rubbed her"; sells Mara a walnut of pitch for an obol (unpaid); at the board "at his ordinary pace", reads (or looks) for twice a slow reading; leaves at a walk and waters the gray | p103–p120, p197–p202 |
| Valens (per the notice) | Thracian; "Lupus"; about thirty; tall, broad-shouldered; a scar on the back of the right hand, badly stitched; Latin, and Greek like a foreigner; has been in the arena; claimed as property of Q. Arrius Celer's household at Corinth; rewards of 500 / 300 drachmas | p172 |
| Kallia | scours the big pot with sand; sets out the basin and the gray washing clay; asks who paid and whether into the hand; "Who takes the goat up?"; one "Then" retort | p159–p171 |
| Euthydikos | priest; a long gray beard cut square; chilblained hands kept in his sleeves; purse on a cord round his neck; a witness on Aphrodisia's stone; owns his grandfather's bronze thymiaterion (sanctuary property); a younger wife; slaves (door, bees); never touches Mara; wipes his fingers | p1, p22, p29, p39, p150–p151 |
| The mistress (unnamed) | much younger than the priest; himation over her head indoors; crimped hair; her mother's caryatid-mirror handle, broken at midwinter; wants it mended "Not in his court" | p95–p100, p157 |
| The letter-cutter (unnamed) | at the polygonal wall; dust-white; resents men who cut ancestors to save letters; cut Aphrodisia's stone deep for an extra obol and read it to her twice | p4–p22 |
| Aphrodisia | home-born in Xenon's house; freed for 3 minae under paramone until Xenon dies; cannot read; seen carrying washing | p1, p13–p20 |
| Mara | public identity "Kallia's Syracusan"; "In Syracuse," … "which was where I was from, now."; mends bronze for pay; cut thumb (base); owes Valens an obol; money is 3 drachmas plus the two 1998 coins, in a rag | p35, p54, p123, p171, p201 |

### Master Timeline
| When | Event | Source |
|---|---|---|
| Poitropios AD 70/71 (≈ Dec/Jan) | Aphrodisia's sale to Apollo; stone cut that winter | p1, p13 |
| Boathoos AD 70 (as written; see W-01) | the notice posted at Corinth | p172 |
| Amalios AD 71 (≈ Jan/Feb), Day 1, morning | the wall and the cutter; the priest's court; the bet | p2–p80 |
| Day 2 | core raked; rod filed and seated late | p81–p86 |
| Day 3 | wax; fills 1–4; Valens at the rear gate in the afternoon (pitch) | p87–p127 |
| Day 4, barely light (most likely) | the curse tablet at the drovers' end of the basin | p129–p141 |
| Day 4, full sun | inspection; payment; the wiped hand; home to Kallia | p142–p171 |
| that day or soon after | the goat man; the notice ("First carts since the snow"); Valens reads it | p174–p202 |
| ahead | the god's return (Bysios) | p65, p98 |

### Knowledge Database (Ch.9)
| Information | Origin | Who knows now |
|---|---|---|
| Consulting needs the pelanos (a stater, perhaps two), a goat that trembles, a Delphian sponsor with a present, and a man to carry the question in | Euthydikos, p58–p60 (the man already from Kallia, ch-08:p101) | Mara; Kallia (from Mara, p166) |
| The notice: Lupus, a Thracian claimed by Celer's household; the scar; the rewards | the board, p172; the clerk posted it | Mara, the men at the board, the town; Valens (reads it, p199) |
| Valens is the man on the notice | inferred by Mara (scar ch-06:p42; Latin ch-06:p45; foreign Greek ch-06:p81; Corinth mules ch-06:p200); never stated | Mara (unstated); the reader |
| Mara saw him read it | p200–p201 | Valens, Mara |
| Mara mends bronze for Euthydikos | p112 | Valens; the priest's household; the smith |
| Mara can mend bronze and wants the god | p35–p80 | Euthydikos, the smith, the slaves, the mistress |
| How the priest paid (onto her palm, from above) | p163 | Kallia |
| Mara's oracle question concerns "the door I came in by" | p23 (narration only) | Mara |

### Plot Threads
| Thread | Status after Ch.9 |
|---|---|
| The Oracle | cost known; money short; man and sponsor still to find → Ch.11 |
| Valens's danger | the notice is in Delphi; he has read it; nobody has connected him yet → Ch.11–12 |
| Money / Mara's living | first earnings (3 dr); more bronze work possible ("When I send") |
| Euthydikos's bowl; the mistress's mirror | OPEN (unscheduled; N-16) |
| The obol owed to Valens | OPEN |
| The goat man's she-goat | OPEN (N-15b) |
| Aphrodisia | texture, closed |
| The curse tablet | texture, closed |
| The watch | with Valens, unmentioned → Ch.11 |

---

## SUGGESTED YAML PATCHES (for entity-tracker, after the editor's fixes)

```yaml
suggested_patches:
  - entity: "meta.post_patch_flags.P5"
    action: "update"
    value: { ch9_note: "page supplies the delay: 'With the oil from Thebes. First carts since the snow' (ch-09:p189). As written the notice is dated 'in the month Boathoos' (p172), when the sea was still open (ch-05:p95; ch-06:p69); continuity W-01 proposes Dadaphorios. RESOLVE once applied." }
  - entity: "meta.contradictions.CH8-1"
    action: "remove_conflict"
    reason: "the decision to consult is shown: 'I had climbed the Sacred Way that morning to find a priest' (ch-09:p3); the question drafted (p23); price asked (p56). Kallia is not told of intent; she hears the price after (p166)."
  - entity: "meta.contradictions.CH3-7"
    action: "update"
    value: { ch9_note: "first use of 'door' for the crack in Mara's narration: '*Where is the door I came in by, now it is shut?*' and 'questions about doors' (ch-09:p23). New fact, not a conflict." }
  - entity: "timeline.chapter-9"
    action: "update"
    value: { time: "about four days, then the square", season: "late winter (almond blossom)", year: "AD 71", month: "Amalios (the sale was 'last month', Poitropios)", source: "ch-09:p1; p13; p83; p86; p90; p129; p142; p189" }
    reason: "replace the outline row ('weeks')"
  - entity: "mara-reyes.knowledge"
    action: "add"
    value:
      - { fact: "the price of a consultation: pelanos (a stater), a trembling goat, a Delphian sponsor with a present, a man to carry it in", learned: "ch-09:p58-p60", method: "told_by:euthydikos" }
      - { fact: "a notice claims a Thracian 'Lupus' with a badly stitched scar on the back of the right hand as Celer's runaway property", learned: "ch-09:p172; p195-p196", method: "witnessed (read)" }
      - { fact: "Valens is the man on the notice", learned: "ch-09:p196-p201", method: "inferred (unstated)" }
  - entity: "mara-reyes.inventory.money"
    action: "update"
    value: { value: "three drachmas from Euthydikos ('The smith's price') knotted in a rag with the two 1998 brass coins; holding the obol she owes Valens", source: "ch-09:p67; p149; p171; p201" }
  - entity: "mara-reyes.physical"
    action: "add"
    value: { fact: "knife cut at the base of the thumb", source: "ch-09:p123" }
  - entity: "valens.knowledge"
    action: "add"
    value: { fact: "the reward notice is posted in Delphi; Mara saw him read it", learned: "ch-09:p198-p201", method: "witnessed" }
  - entity: "valens.relationships.mara-reyes"
    action: "update"
    value: { ch9: "sells her pitch on credit (an obol, unpaid); learns she mends for the priest; the silent look at the board" , source: "ch-09:p105-p120; p200-p201" }
  - entity: "kallia.knowledge"
    action: "add"
    value: { fact: "Euthydikos paid Mara onto her palm from above; the god's price as Mara summarizes it", learned: "ch-09:p160-p166", method: "told_by:mara-reyes" }
  - entity: "euthydikos"
    action: "create"
    reason: "named priest with dialogue (card exists); witness on the p1 manumission"
  - entity: "euthydikos-household (slave at the door, bee-man, the mistress, the smith and his boy)"
    action: "create"
    reason: "walk-ons with dialogue; the mistress and the bee-man carry open threads (mirror; 'kitchen door')"
  - entity: "letter-cutter / aphrodisia / goat-man / men-at-the-board"
    action: "create"
    reason: "Ch.9 walk-ons; Aphrodisia named in a document and glimpsed"
  - entity: "quintus-arrius-celer.first_appearance"
    action: "update"
    value: { chapter: 9, mode: "by proxy (reward notice)", source: "ch-09:p172" }
  - entity: "objects.reward-notice"
    action: "create"
    value: { text_source: "ch-09:p172", posted: "Delphi square, a colonnade pillar beside the herald's door, red on gypsum", arrived: "with the first carts from Thebes since the snow (p189)" }
  - entity: "objects.thymiaterion (Euthydikos's stand)"
    action: "create"
    value: { facts: "three lion's feet, fluted shaft, bowl with pierced lid on a chain; old lead solder at the bowl (the smith's, nine years back); shaft snapped above the feet; mended cold: core raked, filed rod, pitch-wax seat, four fills (three dug out), the last stippled; bowl's lead to be cut out 'When I send'", source: "ch-09:p28-p31; p84-p127; p155" }
  - entity: "plot_threads"
    action: "add"
    value: [ "euthydikos-bowl (open)", "mistress-mirror (open)", "obol-owed-to-valens (open)", "goat-kept-warm (open)" ]
  - entity: "locations.delphi"
    action: "add"
    value:
      - { fact: "polygonal wall below the temple terrace: manumissions cut from the paving up 'as high as a man could reach off a ladder'; a cutter at work in winter", source: "ch-09:p2-p5" }
      - { fact: "Euthydikos's house off the gymnasium lane: a bay tree in a pot at the door; a paved court with a colonnade on two sides, a well-head, hives along the back wall, a rear gate with a woodshed", source: "ch-09:p22; p24; p28; p82; p103" }
      - { fact: "goat pens in hurdles at the lower end of the square by the fountain", source: "ch-09:p175" }
```
