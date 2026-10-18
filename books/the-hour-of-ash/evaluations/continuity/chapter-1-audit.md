# Continuity Audit: Chapter 1 (run 2, per-chapter drift audit)

**Date:** 2026-10-18
**Mode:** MANUSCRIPT AUDIT. Ch.1 checked against the PLAN (it is the only chapter so far).
**Chapter reviewed:** `manuscript/chapters/chapter-1.md` (7,107 words by `style_check`; 425 lines)
**Read against:** outline.md (Macro-Structure, Ledger row 1, `## Chapter 1`), foundation.md (§3 Mara/Emilio/Fenn, §4 row 1, §4f, §5, §6/6a, §9, §10), voice-dna.md (§0, §1, §3b), character-bible.md (Mara, Emilio, Halloran, Szabo, Fessler, Gloria, Pat, walk-ons, at-risk list), ENTITY_STATE.yaml, STATE.yaml guardrails and canon, voice-bank samples.
**Mechanical baseline (re-run for this audit):** `style_check` clean (simile 2.1/1k, em-dash 2, foreshadow 0, no repeated 4–6-grams). `tic_report` clean. `shape_check`: I-statement → quiet, 3 breaks, dialogue 31%. All clean. The findings below are the ones the gates cannot see.

**Total findings:** 33. **CRITICAL: 0 | WARNING: 10 | NOTE: 23**

---

## Scorecard by category

| Category | Result |
|---|---|
| NON-NEGOTIABLE beats present, in order | **PASS.** Beat 1 reception (l.3–69); beat 2 Pine St/Szabo (l.73–305); beat 3 FLEX coat and cousin (l.309–361); beat 4 rowhouse (l.365–425). Order holds. |
| Ledger row | **PASS** on approach (chronological errand), open `I-statement`, end `quiet` (23 words), 3 breaks, dialogue 31% (band 30–40), no one-line open/close paragraph. Gear is borderline: see N-03. |
| Anchor / surprise / beat subversion | **PASS.** The greeting is played 3× (l.397, 407, 411) and not erased. Irritation at the lemon cake and the "generous with his time" eulogy. "Shopping." Szabo haggles to get rid of it; the only uncanny thing is accuracy (l.175–179). |
| Information flow (Mara's horizon) | **PASS.** Mara knows only what the chart and Szabo give her: coordinates, BIBLIOTHECA?, a drawn doorway, Castri/Delphi, Margaret Fenn, the brother who went in '68, the Library of Alexandria. Nothing about caves, doors, time or Italy-as-destiny. The notebook stays **unread** (cover seen only, lid closed, l.225). Halloran's Campania is a neutral fact, erased, nothing written down (l.395). |
| Foreshadowing (voice-dna §0) | **PASS.** Every "would" is a conditional or counterfactual inside the scene. No survivor's hindsight, no "last", no "later". One *stance* issue (generic present tense): W-03. |
| Canon (STATE) | **PASS.** Late-1990s frame (Saturday 14 March 1998 really was a Saturday). Emilio Reyes. Halloran's *permesso* for the Campanian survey season. Provenance: Margaret Fenn's estate sale, Chestnut Hill. "The coast is right" as Szabo's only reason. |
| Objects (§4f) | **PASS with one defect.** Microcassette ejected, blank label, buttoned in the jacket pocket (l.415). Pentax K1000 empty, back opened and closed, no frame spent (l.423). Seiko wound and worn, too big (l.419–421). Defect: the watch's age arithmetic (W-02). |
| Anachronism (March 1998 Philadelphia) | One WARNING (W-01, Cyprus 1974) and three low NOTEs (N-05, N-06, N-07). Brands, prices, tech and idiom are otherwise clean: Acme, Sterno, Crock-Pot, Royal Jordanian at JFK, *Come to Grief* (1995), the Walnut Street West branch, Panasonic dual microcassette, SEPTA 33rd St station, Naples six hours ahead before either DST change. |
| Retired reflexes | No define-by-negation opener, no performed candour, no closing aphorism. One anaphora run (W-08) and one section-close signature (W-07). |
| Tics / emerging devices | No verbatim catchphrase reaches the gate thresholds. Several constructions and beats already recur 3+ times in this one chapter: W-04 to W-07, W-09. |
| ENTITY_STATE | Stale. No Ch.1 UPDATE has run (W-10). |

---

## CRITICAL ISSUES

None. No beat is missing. Mara does not know anything she could not know. There is no canon violation and no forward-gesture.

---

## WARNING ISSUES

### [WARN-001] Age-nine summer = 1974: Emilio leaves "for Cyprus" in the summer of the coup and invasion
- **Category:** timeline / period accuracy
- **Location:** chapter-1.md:337
- **Evidence:** "It was a look I knew from the age of nine. She had been sent to stay with us the summer her mother had the twins, and she had given me exactly this look through the screen door when my father's taxi pulled away for Cyprus"
- **Why it is fixed to 1974:** Mara is 33 in March 1998 (foundation §3) and born in 1965 (bible, ENTITY). That puts her birthday between 1 January and 14 March 1965. Ch.1 confirms it with "I had been twenty-six" in December 1991 (l.407). Her ninth summer is therefore 1974: the Greek-backed coup on Cyprus (15 July) and the Turkish invasion (20 July), when foreign excavations were evacuated. A careful, archaeology-literate reader will catch it, and Mara would never pass that summer without comment.
- **ERROR or INTENT:** ERROR. The memory works with any destination.
- **Suggested fix:** change the destination (Sicily or Turkey; the slide carousel already shows both, l.23, 57), or make her eight (summer 1973).
- **Cascade:** none. Gloria's age (~36 in 1998, about 12 then) is unaffected.

### [WARN-002] The 1966 Seiko "knocked against four decades of trench walls"
- **Category:** object continuity / arithmetic
- **Location:** chapter-1.md:421 (with l.419 "a 1966 Seiko")
- **Evidence:** "scratched in fine circles where it had knocked against four decades of trench walls"
- **Problem:** the watch was made in 1966 (foundation §9; ENTITY timeline_events "1966 the Seiko made"). By January 1998 that is about 32 years, and the line sits two sentences after the date. ("Forty years of my father's trenches" at l.5 is fine, because it is about the man, not the watch.)
- **ERROR or INTENT:** ERROR.
- **Suggested fix:** "three decades", or drop the count.
- **Cascade:** none. The Seiko has no later count, but the tracker should log "nick at two o'clock, steel band, stopped at ten past four, too big for her wrist".

### [WARN-003] Narrating present: generic present tense in narration (voice-dna §0.4, foundation §6a.4)
- **Category:** voice drift / narrating stance
- **Locations and evidence:**
  - chapter-1.md:149 "turned the tissue back the way you turn back a sheet from a face"
  - chapter-1.md:155 "the cheap brilliant pigment that eats what it is laid on"
  - chapter-1.md:357 "held it open behind me, low, at the height you hold a coat for a child"
- **Problem:** the stance law says "Present tense appears only inside dialogue and documents. General reflections are cast in the past." None of these is a forward-gesture. But they are the narrating present in its mildest form, and it is the form most likely to spread. The chapter elsewhere gets it right (l.57 "which was what you said"; l.89 "because you could see it from the street").
- **ERROR or INTENT:** ERROR (drift), low reader impact.
- **Suggested fix:** past-shift each one ("the way you turned back a sheet", "that ate what it was laid on", "the height you held a coat for a child").

### [WARN-004] Indefinite-pronoun habit shared across the cast: "somebody / someone / nobody" about 27× (Amelia-Lesson bleed)
- **Category:** emerging device / voice bleed (voice-dna §3b.8; bible bleed guards)
- **Evidence (narration):** the agentless "somebody/someone had + participle" construction appears 7×: l.59 "someone had wrapped in electrical tape", l.89 "Somebody had drilled half through", l.155 "Somebody had colored it by hand", l.171 "someone had written two lines", l.225 "someone had written A. J. FENN", l.369 "Somebody had a key", l.419 "somebody had turned the radiator down". Further narration uses: l.5, 7, 23, 135, 303, 423 (somebody/someone), and l.7, 59, 291, 315, 419 (nobody).
- **Evidence (dialogue, four other speakers):** Szabo l.109 "Somebody broke it and somebody else put holes in it", l.219 "Then somebody comes with a pen… somebody's grandmother's house", l.237 and 253 "nobody". The dean's-office woman l.19 "Somebody from the slide library". Gloria l.319 "Nobody said one word", l.357 "Just so nobody gets him". Emilio l.401 "somebody else's country".
- **Problem:** the agentless "somebody had…" is Mara's attention made into grammar (reading the trace of an unknown mender), so it is partly INTENT. In Ch.1, though, the word is the chapter's most frequent shared habit, and it already sits in Szabo's, Gloria's, the walk-on's and Emilio's mouths. That is exactly the narrator-to-cast bleed the Amelia Lesson warns about. Across 44 chapters it will calcify.
- **ERROR or INTENT:** intent at the root; the frequency and the spread to the cast are drift.
- **Suggested fix (Editor):** keep 2–3 of the narrator's agentless constructions where the unknown hand matters (l.89, l.155, l.171). Vary the rest with a passive, a named agent or a recast. In dialogue, give Szabo a different shape for l.109/219 (e.g., "It was broken, and then a man put holes in it"). Leave Emilio's l.401 and Gloria's l.357, because they are load-bearing.
- **Cascade:** add "somebody had" to the per-chapter tic watch so Ch.2+ does not inherit it.

### [WARN-005] Narrator constructions already at 3+ in one chapter: "the [color] of [thing]" ×4; the gaze inventory ×3
- **Category:** emerging device (voice-dna §1.5: "no comparison is used twice"; §3b)
- **Evidence:**
  - Color-of: l.9 "burned the pink of boiled ham"; l.81 "the color of an old nickel"; l.99 "a cardigan the color of liver"; l.223 "faded to the brown of weak tea".
  - Gaze inventory (a character's look travels over Mara, item by item, "and at…, and at…"): l.61 guard "He looked at my jacket, and at the sky, and back at my jacket."; l.113 Szabo "the look went down to my wet shoes and came back up by way of the pocket"; l.337 Gloria "She looked at the knot…, and at my jacket…, and at the garbage bag…, and at the paper sack… She kept looking."
- **Problem:** each comparison is good on its own. Together, the color-of frame has become Mara's default simile slot. The appraising look is a fair *situation* to repeat (Mara hates being looked at, l.59). But the *sentence* repeats as well, and for the third time it is the Gloria beat the outline flagged as FLEX.
- **ERROR or INTENT:** intent in content, drift in form.
- **Suggested fix:** re-frame two of the four color comparisons (for instance l.99 "a liver-colored cardigan" or a different predicate; l.223 "worn soft… as weak tea" or a plain color). Give the guard's look a different shape (a single action: "He considered my jacket, then the sky"), so that Gloria's inventory is the only full one.

### [WARN-006] The same character beat used 3+ times in the chapter (voice-dna §1 dialogue conventions: "no character gets the same beat twice in a chapter")
- **Category:** emerging device / voice-dna §1
- **Evidence:**
  - **Szabo turns to the TV/game ×5:** l.129 "looked past me at the television"; l.253 "She turned and looked at the television"; l.257 "She watched the screen… she told it"; l.291 "Mrs. Szabo was watching the game"; l.303 "On the television… She spoke a word to it in Hungarian".
  - **Szabo's magnifier in her hair ×3:** l.113 "a magnifier she had pushed up into her hair"; l.147 "pulled the magnifier down out of her hair"; l.219 "pushed it back into her hair".
  - **The dean's change ×3:** l.7 "jingled the change in his pocket"; l.25 "jingling"; l.31 "went back to his change".
  - **The dean's-office woman by her lids ×3:** l.5 "kept lifting the lids", l.13 "the lid-lifter", l.309 "The woman with the lids".
- **Problem:** the bible deliberately gives Szabo "her own life" in the bet (INTENT, and it carries the subtext of her not looking at Mara). But five returns to the screen is a running beat, and the second "pushed into her hair" repeats the first. The dean and the lid-lifter are tagged by one gesture each, three times over. For one-scene walk-ons that is a cheap way to make a device.
- **ERROR or INTENT:** Szabo's TV is intent but overused. The rest is drift.
- **Suggested fix:** cut Szabo's TV returns to three, each a different act (glance, bet line, net). Change l.219 to a different hand action (she sets the magnifier on the ledger, or wipes it). Give the dean's third appearance (l.31) a different exit. Re-tag the lid-lifter once (l.309, e.g., "the dean's-office woman").

### [WARN-007] "Then…" as a shared reply and scene-close construction (Szabo ×3; Mara and Gloria close sections 1 and 3 identically)
- **Category:** emerging device / scene-button risk (retired reflex) / cast sharing
- **Evidence:**
  - Szabo's syllogistic "Then [you/it]…" verdict ×3: l.187 "Then you know what a man with a ballpoint pen does to a thing like this."; l.215 "Then you have read it."; l.233 "Then it is for whoever pays." (The pattern also opens her l.219 "Then somebody comes with a pen.") It is lifted from voice-bank sample-02 ("Then you will pay what I ask").
  - Section closers: l.69 "\"Then I'll walk,\" I said, and went down the ramp into the weather." and l.361 "\"Then go do it,\" she said, and I put my arms in the sleeves." These are the same shape: a "Then…" line, a tag, and "and [I] + action". Section 2 also ends on a tagged dialogue line (l.305 "\"Pull the door hard,\" she said… \"It sticks.\""), so three of the four sections close on a speaker's line.
- **Problem:** Szabo's "Then you…" is one construction three times in one scene, by the law's own 3+ count. The identical section closers are a forming scene-button signature, the kind `shape_check` cannot see because it reads only chapter ends.
- **ERROR or INTENT:** drift.
- **Suggested fix:** keep one of Szabo's "Then…" lines (l.233 is the best) and recast the other two as flat verdicts, which matches her card ("You have read it." / "You know what a pen does to a thing like this."). Re-shape one of the two "Then…" section closers (for instance, end §1 on the action alone, or end §3 on Gloria's coat-holding without the tag).

### [WARN-008] Anaphora run "I wrote" (retired reflex: anaphora triads)
- **Category:** retired reflex
- **Location:** chapter-1.md:287
- **Evidence:** "I wrote the date. I wrote her name, which she spelled for me without being asked, … and signed it, and copied my license number off the card. Then I wrote the phone number. I wrote it fast…"
- **Problem:** three sentences open on "I wrote" (four uses in five sentences). The "Then" break does not stop the effect. The writer's report says the rhythm gate's two I-led runs were broken, but this one survives.
- **ERROR or INTENT:** intent (the mechanical act building to the wrong number), but the form is on the retired list.
- **Suggested fix:** merge the first two ("I wrote the date and her name, which she spelled for me…"), so that only "Then I wrote the phone number. I wrote it fast" remains: two, which is the turn.

### [WARN-009] "Mara? Which one stops it?" is quoted verbatim twice, and the second quote carries the turn
- **Category:** tic risk (voice-dna §3b.3: "No beat in this book depends on a character's line 'landing again'")
- **Location:** chapter-1.md:401 and 413
- **Evidence:** l.401 "\"Mara? Which one stops it?\"" (first playback); l.413 "\"Mara?\" he said. \"Which one stops it?\"" (third playback, after which "I took my finger off the button").
- **Problem:** inside Ch.1 this is defensible INTENT. It is a recording, the tape is an object motif, and a replay is a literal repetition. But it is the chapter's strongest line, it was not planned (writer report: impulse deviation), and it is not on the at-risk list. The cassette has scheduled touches in Ch.5, 19, 35 and 43. If the line is quoted at any of them, it becomes the book's refrain.
- **ERROR or INTENT:** INTENT in Ch.1. This is a WARNING for the book, not a fix to this chapter.
- **Suggested fix:** add "which one stops it" to the bible's at-risk table at **max 2 (used: 2)**, so it can never be quoted again; later touches go through the object, not the line. Optionally, render the l.413 instance without the full quote (e.g., "He asked me again which one stopped it").

### [WARN-010] ENTITY_STATE.yaml is stale: no Ch.1 UPDATE has run (Audit 6b/6c)
- **Category:** tracker staleness / coverage gaps
- **Evidence:** ENTITY_STATE.yaml:12–14 `last_updated_chapter: 0`, `chapters_tracked: []`. The last entity-changelog entry is the pre-writing plan re-sync. The pipeline order (D.5 before D.6) has not been met for this chapter.
- **Coverage gaps (entities with dialogue or plot-relevant facts, not tracked):** Doug Fessler (speaks); Gloria (speaks; sets the errand); Pat (on tape); Ray, Tía Nilda (78), Dorothy, Carol, Frank the registrar; Mara's mother (Phoenix, c. 1981); the dean and the dean's-office woman; the Nicosia caller. These are all bible-only.
- **Ch.1 canon facts the tracker must record:**
  - Memorial on Saturday 14 March 1998 at 2 p.m., upper gallery. Mara leaves at about 40 minutes and is back at about 5. The house is reached near dark.
  - Emilio's rowhouse is off Baltimore Avenue, fourth of twelve, with a sagging porch and a radiator under the front window.
  - Mara has her own rent/account (she lives elsewhere). Her hair is in a knot with a pencil (the clip broke). Eyes and height are still unset.
  - Szabo: 1,400 asked, 800 paid, 1,150 sold by check with Emilio's phone number on it.
  - The chart: Venetian copperplate, GOLFO DI LEPANTO, *Castri*, *M. Parnaso*, tre lune watermark, verdigris through the north shore in seven places, blue ballpoint "38° 31′ N / 22° 32′ E", BIBLIOTHECA?, and a doorway drawing embossed through to the back. It is between mat boards, in a garbage bag, on the kitchen table.
  - The Phillies cigar box with tobacco crumbs. The oilcloth notebook "A. J. FENN", perished elastic, warped from damp, unread.
  - Fenn's other boxes: Navy uniforms, *National Geographic*, a diving helmet (sold to Wildwood).
  - Panasonic two-microcassette machine set up December 1991. Incoming tape erased. The greeting tape is in Mara's buttoned jacket pocket. The machine blinks slowly with no greeting.
  - Seiko: steel band, nick at two o'clock, stopped at 4:10 in January, now wound and on Mara's wrist, too big.
  - Pentax K1000: empty, back on the shelf, strap in three turns.
  - Halloran: the *permesso* lapses unless a name is on it by **20 April**; office number begins 081-552.
- **Suggested fix:** run entity-tracker UPDATE for Ch.1 before the evaluator, and apply the patches at the end of this file.

---

## NOTES

- **N-01 (mechanics, report accuracy):** the em-dash count is **2** (l.115 "In the conservation—", l.343 "with a—"), not 0 as the writer report says. Both are true dialogue interruptions, within the ≤4 budget.
- **N-02 (voice drift, punctuation):** 8 semicolons in 7.1k words (1.1/1k) against the voice-dna §1 target of ~3/1k. Long sentences are being carried on comma-and-"and" chains (l.369, l.407). This is consistent with the gear issue in N-03. Watch it in Ch.2 (mid) and Ch.3 (high).
- **N-03 (ledger):** the whole-chapter median sentence is 10 words (`shape_check`), which falls in the ledger's *low* band (9–12). The writer's narration-only median is 14, the bottom of *mid*. If gear is audited book-wide from `shape_check`, Ch.1 will read as low.
- **N-04 (lexical frequency):** "flat" ×12 (l.11, 99×2, 149×2, 207, 297, 301, 309, 369, 379, 425), with "X flat on the Y" ×4. "little" ×14 (l.9, 13, 23, 89, 161, 291, 365, 369, 373, 395, 401, 411, 415×2). Some of the "flat" is situational (the chart must travel flat). Trim the gesture uses (l.11 palm, l.207 gloves) and a few of the "little"s.
- **N-05 (season):** in mid-March the cab radio is "explaining how to put roses to bed for the winter… wrap them loosely in burlap" (l.73, 81). That is an autumn topic, and March shows talk about uncovering and pruning. Either make it a call-in mix-up or switch to a spring topic. The driver's "Every fall… mulch" (l.79) can stay.
- **N-06 (calendar, low confidence):** "somebody was cutting down a net" (l.303) on 14 March 1998. The conference tournaments ended by Selection Sunday (8 March), and NCAA second-round winners do not cut nets. It is low salience, so leave it or change it to celebrating players.
- **N-07 (period):** the K1000 strap is "in the same three turns for as long as I could remember" (l.423). The K1000 came out in 1976, when Mara was 11. Mild overstatement; "for as long as he'd had it" avoids it.
- **N-08 (house logic):** "Two months of mail lay on the hall floor in a drift" (l.367), yet neighbors have stocked the fridge with fresh dishes and turned the radiator down (l.369, 419). Either the food is two months old (Mara, who notices decay, would smell it) or someone recently stepped over the mail. One clause would settle it (the mail pushed into a pile, or the dishes left yesterday for after the memorial).
- **N-09 (logistics):** "In the car" (l.333–335) and "the Volvo place" (l.349) imply that Mara has a car, yet she takes a cab and the trolley with $11. The inference is available (keys in the coat she left behind) but unstated, and a reader may wonder.
- **N-10 (Doug's self-echo):** "Generous with his time" ×2 (l.11), "until two in the morning… Two o'clock in the morning" (l.39), "Always. That was exactly him… agreeing with himself" (l.43). This is the card's syntax fingerprint and fine for a one-scene character. If Fessler returns (he offered to "do the office", l.47), it must not travel.
- **N-11 (shared concern):** "You have to eat something" (l.15) / "Did you eat that cake?" (l.311) / "Did you eat anything?" (l.349) / "I bet it's in your pocket" (l.353). Two characters run the feed-the-mourner beat. It is an INTENT comic run paid off at l.371, but keep it out of later chapters.
- **N-12 (shared gesture):** "She kept her eyes off the ink" (Szabo, l.215) and "She kept her eyes on the bag" (Gloria, l.357). Two characters use the same body beat. Vary one.
- **N-13 (Mara's verdict form):** "Your Hogarth's a restrike" (l.131) and "Your green's verdigris" (l.157). The form is used twice; a third "Your X's Y" anywhere in the book would make it a device.
- **N-14 (sample-line borrowings; at-risk rule "any phrase in a sample line… 0"):**
  - l.391 "a name on it by the twentieth of April" lifts Halloran's calibration sample (bible l.396–397, "a name on it by the first of June").
  - Phrases also lifted from voice-bank sample-02: l.171 "Across the mountains above", l.89 "It had been done", l.113 "over the top of", and Szabo's "Then you…" pattern (W-07).
  - "The coast is right" is also canon wording (STATE/outline), so it is defensible.
  - Vary the Halloran phrase if convenient.
- **N-15 (teeth schedule):** "to the last tooth" (l.291) refers to the check's perforations. Ch.1 is scheduled to have no teeth (outline Ch.1, bible). This is a pun-adjacent word in a no-teeth chapter, harmless, but "to the last perforation" removes the question.
- **N-16 (Szabo edging onto Mara's axis):** "Somebody broke it and somebody else put holes in it" (l.109) and "I know what my green is. Three hundred years it eats" (l.159). Szabo talks condition and material, which is Mara's axis (bible: "Only Mara notices materials and joins"). Her framing is price and authenticity, so this is acceptable. Note it for any future dealer character.
- **N-17 (plan gap):** Mara's eye color and height are still unset (ENTITY `physical_unset`; the plan gap says "set on the page by Ch.1 (or first mention)"). Only the hair in a knot is established (l.329–337). They can be set at first natural mention; log the knot.
- **N-18 (outline function):** "the lie (the packed bag)" has no literal bag in Ch.1. It is enacted by leaving (l.23, 59) and by loving the made thing (l.89 "could have kissed him"). Ch.2's packing completes it. INTENT, no action needed.
- **N-19 (threads opened without a scheduled payoff):**
  - (a) The check carries Emilio's phone number (l.287–291), and the house machine now has no greeting (l.425). If the check bounces, Szabo calls a dead line.
  - (b) Gloria's errand is half-done; callers now get no greeting.
  - (c) The Nicosia friend has not heard and has the Kourion drawings (l.383–385).
  - (d) *Come to Grief* is overdue (l.379).
  - (e) The lecture fund (l.27).
  - (f) Doug's "I can do the office" and "Are you keeping the house?" (l.47–51).
  - All of this is texture under the foundation's 30–40% rule. The writer report frames (a) as a "quiet loop", so do not let it grow into a Chekhov expectation. Ch.2 (eight weeks of ordinary days) may touch (a) or (b) in a clause, or leave both.
- **N-20 (cascade into Ch.2, information flow):** Halloran's deadline is now canon: a name on the *permesso* "by the twentieth of April" (l.391). Ch.2's call inviting Mara to Campania for July "in Emilio's place" must square with it: either the call comes before 20 April, or a name went on. Mara also "wrote nothing down" and erased the message (l.395), so Ch.2 needs a plausible path for Halloran to reach her (he rings the house when she is there, or gets her number from the department).
- **N-21 (implied canon):** Emilio's Seiko lies on his own nightstand, "where he had always taken it off at night", and stopped in January (l.419). This implies he was home, not in the field, when he died. Record it; no later past-facing memory may place his death abroad.
- **N-22 (tracker housekeeping):** ENTITY_STATE.yaml:57–61 P1–P5 still read `flag: "UNRESOLVED"`, while the header comment (l.55) says they were resolved by direct outline edits. Verified: the P1–P3 trigger strings no longer appear in outline.md or foundation.md. Flip the flags on the next UPDATE.
- **N-23 (borderline triad):** l.7 "to see where the strain had gone. It had gone into the dean… It had gone into the graduate students" makes a set-up plus two echoes, which has a triadic feel. It is not a strict anaphora triad. Leave it unless WARN-008's fix leaves the chapter still rhythm-heavy.

---

## Plot threads opened in Ch.1 and their scheduled payoffs

| Thread | Opened | Scheduled | Status |
|---|---|---|---|
| Fenn's notebook (unread) | l.225 | Ch.2 read; packed; Ch.25 refused; Ch.35 read; Ch.43 through the door | OPEN, on plan |
| The chart: coordinates, BIBLIOTHECA?, doorway | l.155–171 | Ch.2 pinned over the desk, coordinates in the notebook; Ch.3 the cave | OPEN, on plan |
| Fenn "did not come back" | l.203–207 | Ch.2 consulate slip; Ch.25 in person | OPEN, on plan |
| Microcassette (greeting) | l.415 | Ch.2 sock; touches Ch.5, 19, 35; Ch.43 through the door | OPEN, on plan (see WARN-009) |
| Seiko (wound, worn) | l.419–421 | Ch.2–5 worn; Ch.6 to Valens; Ch.18 returned | OPEN, on plan |
| Pentax (empty) | l.423 | Ch.2 fresh roll; 8 frames in 1998; Ch.38 frame 36 | OPEN, on plan |
| Halloran / Campanian permit (by 20 April) | l.391 | Ch.2 call (neutral; no payoff by design) | OPEN, on plan (see N-20) |
| Check with the wrong phone number | l.287–291 | none | texture (N-19) |
| Gloria's errand half-done / greeting-less machine | l.357, 425 | none | texture (N-19) |
| Mara's money (check she can't afford; the estate "waiting for a form") | l.267, 309 | none planned | texture |

---

## SUGGESTED YAML PATCHES (for entity-tracker UPDATE, Ch.1)

```yaml
suggested_patches:
  - entity: "meta.chapters_tracked"
    action: "update"
    value: [1]
    reason: "Ch.1 written and audited; no tracker UPDATE has run"
  - entity: "timeline[chapter=1]"
    action: "update"
    value: { time: "Saturday 14 March 1998; memorial 2 p.m.; Mara out ~2:40 to ~5; house near dark", source: "ch-01:p387, p125, p309, p365" }
  - entity: "doug-fessler"
    action: "create"
    reason: "speaks in Ch.1; 11 seasons Cyprus + 2 Sicily with Emilio; Jordan winter season sunburn; Royal Jordanian lost his duffel (six weeks of context sheets); offered to 'do the office'"
  - entity: "gloria"
    action: "create"
    reason: "speaks in Ch.1; Emilio's niece (father's side); married to Ray 14 years; never names Emilio; sets the machine errand; stayed with the Reyes family the summer Mara was nine"
  - entity: "pat"
    action: "create"
    reason: "next-door neighbor; on the incoming tape (erased); has Emilio's blue Tupperware; he shoveled her walk"
  - entity: "mara-reyes.physical.hair"
    action: "update"
    value: "worn in a knot; a pencil through it on 14 March 1998 (clip broke)"
    source: "ch-01:p329-337"
  - entity: "mara-reyes.relationships.mother"
    action: "add"
    value: { type: "mother", current_status: "alive, Phoenix; divorced from Emilio c. 1981; sent lilies + card" }
    source: "ch-01:p7"
  - entity: "emilio-reyes.facts"
    action: "add"
    value:
      - "rowhouse off Baltimore Avenue, 4th of 12, sagging porch (he planned to jack it up)"
      - "outgoing greeting recorded December 1991 with Mara; ends off-mic 'Mara? Which one stops it?'"
      - "his Seiko was on his own nightstand when it stopped in January (implies home, not in the field, at death)"
      - "overdue Free Library book: Come to Grief (Dick Francis); read them on planes"
    source: "ch-01:p365, p373, p401, p419, p379-381"
  - entity: "objects.microcassette"
    action: "update"
    value: { state: "ejected from the Panasonic two-tape machine; blank label; in Mara's buttoned jacket pocket", source: "ch-01:p415" }
  - entity: "objects.fathers-seiko-watch"
    action: "update"
    value: { state: "1966, hand-wound, steel band, crystal nicked at two o'clock; stopped 4:10 in January; wound, set and worn by Mara; far too big", source: "ch-01:p419-421" }
  - entity: "objects.fathers-pentax-k1000"
    action: "update"
    value: { state: "black-and-chrome; strap in three turns; EMPTY (no film); back opened and closed; returned to the shelf", source: "ch-01:p423" }
  - entity: "objects.venetian-map"
    action: "update"
    value: { state: "copperplate, hand-colored; GOLFO DI LEPANTO, Salona, M. Parnaso, Castri; tre lune watermark; verdigris through the N shore in 7 places; blue ballpoint 38°31'N 22°32'E + BIBLIOTHECA? + doorway, embossed through; bought $1,150 by check (asked $1,400; Szabo paid ~$800); between gray mat boards in a garbage bag on Emilio's kitchen table", source: "ch-01:p155-171, p237-265, p297" }
  - entity: "objects.fenn-notebook"
    action: "update"
    value: { state: "black oilcloth, perished elastic in two pieces, warped from damp; cover 'A. J. FENN' in square capitals; in a Phillies cigar box with tobacco crumbs; UNREAD", source: "ch-01:p223-225" }
  - entity: "halloran.knowledge / campanian-survey-permit"
    action: "add"
    value: { fact: "permesso lapses unless a name is on it by 20 April; office number 081-552…; erased by Mara, nothing written down", source: "ch-01:p391, p395" }
  - entity: "meta.post_patch_flags[P1..P5]"
    action: "remove_conflict"
    reason: "sources patched (header comment l.55); trigger strings verified absent for P1-P3"
```

---

## Bottom line

Ch.1 holds the plan. Every NON-NEGOTIABLE beat is present and in order, Mara's horizon is clean, there is zero foreshadowing, and the canon is correct. The work for the Editor is two factual slips (W-01 Cyprus 1974, W-02 "four decades") and a cluster of patterns that will become tics if they carry into Ch.2:
- the cast-wide "somebody" habit (W-04);
- the color-of frame and the gaze inventory (W-05);
- the repeated one-gesture tags (W-06);
- the "Then…" construction and section closers (W-07);
- the "I wrote" run (W-08);
- the generic present (W-03).

Register the tape line at max 2 (W-09) and run the tracker UPDATE (W-10) before the evaluator.
