# Continuity Audit: Chapter 6 (run 2, per-chapter drift audit)

**Date:** 2026-10-19
**Mode:** MANUSCRIPT AUDIT. Ch.6 checked against Ch.1–5 as they stand on disk, all re-read in full, and against the plan.
**Chapter reviewed:** `manuscript/chapters/chapter-6.md` (6,634 prose words by `shape_check`, 6,749 by `wc -w`; **342 prose paragraphs**, 2 breaks after p35 and p243)
**Paragraph numbering:** `ch-06:pN` counts prose paragraphs only. The title, the two HTML comments and the `* * *` breaks are not counted. This is the same convention ENTITY_STATE uses for ch-01…ch-05, where p1 = "I had scraped the floor of the crack…" and p342 = the last line.
**Read against:** outline.md (Ledger row 6; `## Chapter 5` to `## Chapter 9`), STATE.yaml (guardrails, canon, resolved decisions), voice-dna.md (§0, §1, VOICE UNDER PRESSURE, §3b), character-bible.md (Mara, Valens, Kallia; the Ch.5/Ch.6 walk-on and spent notes; the retired and at-risk lists), and ENTITY_STATE.yaml. The committed copy covers Ch.1–5. The live file now also carries the parallel tracker's ch-06 rows and CH6-1…CH6-8; I treated those as **unverified** and re-derived every one from the page. Where the tracker and this audit agree, that is noted.
**Mechanical baseline (re-run for this audit, read-only, `bash tools/check_chapter.sh 6`):**
- Style clean: simile 0.9/1k, adverb 3.2/1k, em-dash 3, foreshadow 0.
- Grammar clean. Rhythm: 0 flagged.
- Show/tell: no flags (its meter reads dialogue 33.0%).
- Voice-wear strict: clean. Tic gate clean, including the gesture layer. Echo scan: 0.
- And-chains 5 (cap 9). Credential asides 1 (cap 4).
- Metaphor: median sentence 11, 3.7% of sentences over 40 words.
- Shape audit across 6 chapters: CLEAN. Ch.6 computes as `I-statement` → `dialogue`, 2 breaks, dialogue 38%, median 11.

**Total findings:** 45. **CRITICAL: 1 | WARN: 19 | NOTE: 25**

The gates are clean and the chapter hits its plan. The one CRITICAL is a physical contradiction in the book's principal object, sitting in the anchor scene. Most WARNs are one-clause fixes:
- facts that drift from Ch.1–5 (when the watch was first wound, the coin's face, the vintage, the crack's height, the route's order);
- comprehension that outruns the Ch.4–5 rule;
- constructions starting to form that the n-gram gates are too coarse to see.

---

## Scorecard by category

| Category | Result |
|---|---|
| (a) Beats / ledger | **PASS.** In medias res, internal shape *crisis → backfill → after*. Beat 1 (recess, cold only): p1–p35. Beat 2 BACKFILL, non-negotiable (firewood at Kallia's; the ask and the refusal on snow p94–p100, money p106–p111 and her p103–p105; the Seiko offered; wound backward until she stops him): p36–p152. Beat 3 (climb: mules, footing, weather): p153–p243. Beat 4, non-negotiable (she hits the wall and screams, he laughs, bread and no comfort): p244–p258. Beat 5 (descent in falling snow; he keeps the watch "You paid it to go up", p302): p274–p342. Opening `I-statement` (p1, 39 words, starts "I") ✓. Ending `dialogue` (p342) ✓. Exactly 2 breaks ✓. 6,634 words against 7,200, inside the header's 6,500–7,600 range ✓. Dialogue 38% by `shape_check`, the ledger metric, against a 35–45 band ✓ (meter disagreement in N-01). Gear: median 11 against the ledger's *mid* (N-02). |
| (1) Character consistency | **Mara:** WARN ×3 (W-01, W-07, W-19; all facts she states aloud). Voice NOTE N-06. **Valens against his card, first live appearance:** PASS on attention (ice, ashes, footing, weather, the donkey man), syntax (no simile or comparison in his speech; questions only about where, how far and who; *why* only of plans, p100), evasion ("North.", "On the road.", "Don't.") and the mind-reading threat (p184–p188, p265–p267, p329). WARN W-05 (his "fast Phocian"). **Kallia against her card:** PASS. She never sits, never touches Mara and never asks her name. She answers with tasks ("You. Under the stair. Bark up."). Her son appears only as "Letters." Nothing about herself. |
| (2) Timeline | **PASS with WARNs.** Day count and dates are in the Master Timeline below; they hold together. WARN W-04 (the vintage), W-19 (rent arithmetic), W-03 (the watch's time base). NOTE N-03 (the turn where the ice starts). |
| (3) Information flow | **WARN ×4:** W-05 (fast haggling), W-06 (the burner's fast Greek rendered nearly verbatim), W-07 (the boy knows her name), W-17 (the Greek refusal versus outline Ch.7). Otherwise clean. She learns Valens's name from Kallia (p48), the widowhood from Valens (p103), the closed sea from Valens (p69). Valens's reading of her uses only what he saw or heard: the charcoal men's story, her hands, the Latin laugh, the coin, the watch, the inscription (p329). He catches only "Philadelphia" from her English (p166). The burner's knowledge comes from his cousin's boy, the Ch.4 goat-boy. |
| (4) Objects | **CRITICAL ×1** (C-01, the band's fastening). **WARN ×3:** W-01 (winding start), W-02 (the coin), W-10 (the flashlight). The shovel's chain holds: pail p42 → taken p153 → "The shovel comes back" p155 → left in the crack p274 → retrieved by Valens → returned p341. The duffel holds: packed "since it had never been unpacked" p153, "Everything" p159, on the dun, by the slab p239, returned p341. The welts from the Ch.5 beating are about a month old and not mentioned, which is acceptable. The fleece, the granola, the microcassette, the Pentax and the knucklebone are absent (NOTES N-08, N-09; the tape and bone absences are by design). |
| (5) Plot threads | **PASS with WARN ×1** (W-17, outline Ch.7). The Ch.5 plan to go back up is accounted for: the attempt that failed and why (p38), then the hired climb. "Letters" from the east (p72–p74) opens Kallia's son thread for Ch.10 without naming him (✓ card). "Men will come asking" (p342) is consistent with Valens's prior knowledge (ENTITY: Plautia's brother's freedman, Kirrha, autumn 70) and does not pre-empt Ch.9's notice. |
| (6) World rules: the door is shut | **PASS.** Only cold, everywhere: "Rock. Air. Cold that was only cold." (p240); "The rock was cold. The air did not move." (p246). This matches the Ch.3 aftermath (ch-03:p78–p79, nothing coming from the crack), the world rule "A door used for a crossing can stay shut afterwards", and outline Ch.8 (shut again). Mara still never says "door" (p165 "if it's shut"; p232 "Until it opens"). See N-19 (CH3-7). |
| (7) NO FORESHADOWING | **PASS.** Gate 0, and a manual read finds no forward reach. "I will not [be here in the spring]" (p101) is a present intention. "Men will come asking" is a character's warning, not narration. No 79, no Pompeii, no Italy. |
| (8) NO TICS | **Mechanical: PASS** (tic gate, gesture layer, voice-wear strict). **Manual, constructions the gates cannot see: WARN ×5:** W-12 (a Ch.3 phrase echoed), W-13 (a plate comparison reused), W-14 (the language-tag aside forming), W-15 (a spent "to his back" construction), W-16 ("the widow" ×10 across two speakers). Also W-11, a bible sample line lifted onto the page. Spoken refrains: none ("You've got Latin" ×2 by Valens is a recap, N-07). |
| (9) Voice drift vs voice-dna and bible | **Mostly PASS.** VOICE UNDER PRESSURE level 1 at the wall is exactly as mapped: p249–p252 are plain hand verbs and sound, with no aside. The asides return when he laughs (p254 "a laugh with nobody at the end of it"; p258 "salted it with conviction"). The 1998 comparison domains rotate: a neighbour, the percolator, Ray's Buick, a crossing guard, sugar, a plate. Valens: no simile in speech ✓. NOTES N-06, N-11, N-12, N-13. |

---

## PRIORITY: UNRESOLVED ENTITY_STATE CONFLICTS (processed first)

| ID | What Ch.6 does to it | Verdict / where it lands |
|---|---|---|
| **CH5-6** language of "Eggs" / "Mine." / "Where are we going?" | p39: "I had spoken no Greek aloud since the guide on the Sacred Way … whatever got away from me got away in English". p61: Kallia, "She doesn't talk." | **Settled by the page: English.** One value in prose, foundation and bible. RESOLVE (N-05). |
| **CH5-2** residual (bible says the replies to Kallia are English) | Same evidence | Bible now matches the page. RESOLVE (N-05). |
| CH3-7 door never named | Still never named (p165, p232) | In character. Recommend RESOLVE, prose wins (N-19). |
| CH3-3 refuge hut vs pen | p220 "By the pen under the firs" | Still a pen with no hut. Plan-vs-prose only; patch outline Ch.4 lines 213/222 (N-24). |
| CH4-2 granola unit | Not on the page except "a cake made of hay" / "It was oats" (p321–p322) | Unchanged. Open (N-08). |
| CH4-3 jacket vs fleece | Ch.6 names no outer garment at all (a snow climb) | Unchanged. Open (N-09). |
| CH4-4 inscription | p222 "letters were still red at the bottom of their strokes"; p224 "To the Nymphs. To Pan." (datives = ΝΥΜΦΑΙΣ / ΠΑΝΙ) | Consistent with ch-04:p28. The 1998 "ΠΑΝ" question is unaffected (N-20). |
| CH5-3 film frame | No frame in Ch.6 | Unaffected. |
| CH5-4 microcassette | No touch in Ch.6 | ✓ schedule (next is Ch.19). |
| P5 Corinth notice timing | Valens works openly in Delphi; "Men will come asking" (p342) | Consistent with the patched plan (the notice reaches Delphi in spring 71). Housekeeping: `post_patch_flags` header says P1–P5 RESOLVED but the rows still read UNRESOLVED (N-24). |
| CH1-2, CH1-3, CH2-1, CH2-3, CH2-4, CH2-5, CH3-1, CH3-2 | Not touched by Ch.6 | No change. |
| *(unverified, parallel tracker)* **CH6-1 … CH6-8** | Re-derived independently | CH6-1 = **W-01**; CH6-2 = **W-02**; CH6-3 = **W-19**; CH6-4 = **W-18**; CH6-5 = N-18; CH6-6 = N-04; CH6-7 = **W-17**; CH6-8 = **W-03**. All eight confirmed on the page. The tracker did not log C-01 or W-04 to W-16. |

---

## CRITICAL ISSUES (fix before finalize)

### [C-01] The Seiko's band is a link bracelet, but Ch.6 unfastens it as a tongue-and-hole buckle
- **Category:** objects; physical-attribute contradiction in the principal object, inside the chapter's anchor scene.
- **Evidence:**
  - ch-01:p190: "its steel band coiled beside it like a dropped ribbon".
  - ch-02:p14: the jeweler "pushed the pins out of the band with a little steel punch… Three links went into a manila envelope". A link band is shortened by removing links because it has no holes.
  - **ch-06:p120:** "The buckle was stiff with the cold. It took me two tries to work the tongue out of the hole, and then I had it off my wrist".
  - **ch-06:p124**, four paragraphs later: "over the band where the three links had come out". The chapter states both forms.
- **Why CRITICAL:** a tongue and a hole belong to a strap with punched holes, and that kind of band cannot have links taken out. The reader who saw the jeweler scene and the "three links" callback gets both in a single page. The object recurs through Ch.18, 24, 32, 41 and 43, so the error would propagate.
- **Minimal fix (p120):** "The clasp was stiff with the cold. It took me two tries to spring it, and then I had it off my wrist, and I passed it to him across the gray mule's withers, still warm on the inside of the band." (This adds no thumbnail; the thumbnail-probe cap is 1 per chapter.)
- **Cascade:** "buckled it on" (ch-01:p191) can stand as a loose verb for fastening. Every later scene that touches the band (Ch.18 return; Ch.24, 32 and 41 windings; Ch.43) must say clasp, not buckle or holes. Add `band: steel link bracelet, fold-over clasp` to `objects.fathers-seiko-watch.physical`.

---

## WARNING ISSUES (fix before finalize under the drift policy; each is a word or a clause)

### [W-01] "I've wound it every morning since January" (CH6-1, confirmed)
- **Evidence:** ch-06:p165 against ch-01:p190 ("It had stopped at some ten past four in January … and had not been wound since"), ch-01:p191 (she first winds it on the night of Sat 14 March), and ch-02:p63 ("The microcassette had been in my jacket since March … I gave its crown its turns each morning").
- **Fix:** "since January" → "**since March**". Nothing else moves; "which hasn't helped him or me" still lands.

### [W-02] The coin Valens is shown is the coin the guide already pocketed (CH6-2, confirmed)
- **Evidence:** ch-05:p55: of three taxi coins she gives "the biggest", "a hundred-drachma piece … brassy, with a young man's head on it in profile and his hair blowing back". The guide keeps it (ch-05:p64). The bible lists "the hundred-drachma coin" as **spent in Ch.5**. ch-06:p108–p110: "I had two taxi coins left … I offered him the bigger … brass, and the profile of a young man with the wind in his hair." / "A king."
- **Problem:** a reader will take it for the same coin, now back in her pocket. If she had two identical hundreds, Ch.5's "the biggest by feel" makes no sense.
- **Fix (preferred):** make the bigger of the two left the 50-drachma piece. The 1990s issue is brass with Homer's bearded head; verify before printing. p108: "…brass, and the profile of an old man with a beard and a band round his hair." p110: "**A poet.** From farther away than you would believe." **Fallback:** keep the king and add "the twin of the one the guide had pocketed" (this costs the Ch.5 "biggest" logic a little).
- **Cascade:** the ENTITY coin row: two remain; record the denominations.

### [W-03] The watch's time base: "the May hour" compared across two clocks (CH6-8, confirmed)
- **Evidence:** In May the watch kept Greek civil time, i.e. summer time, UTC+3. Ch.3's readings prove it: the taxi a little after nine, the cave by noon, 12:20, 12:30, the cold "at twenty to two" (ch-03:p68). ch-06:p13: "I had set the hands on my second day at Kallia's by the shortest shadow of her gatepost". p14–p15: she waits for "twenty minutes short of two". p248: "Five to two".
- **Problem:** Mara plotted 22° 32′ E herself (ch-03:p7). Delphi's sun keeps about UTC+1:30, so 1:40 Athens summer time was about **12:10 by the gatepost**. She is waiting at the wrong hour by an hour and a half. The narration does not notice, though it is the kind of sum the narrator does on her fingers (ch-05:p109). An informed reader will. Valens's "Past the middle of the day" at 1:10 (p10) correctly matches the sun-set watch, so the page is internally consistent. Only the comparison is unexamined.
- **Fix (one clause, p14):** "In May the cold had come at twenty minutes short of two **by Athens time, which ran an hour and more ahead of this sun; I had been on my knees through both.** It was nothing to go on, and I had nothing else." This keeps p15 and p28, the long hand at the eight, and p248.
- **Cascade:** the Ch.8 attempt has no watch, so nothing to carry. Fenn's door tables in Part Two must keep sun time and civil time distinct.

### [W-04] Her emergence is dated "at the vintage", but Ch.5 places the vintage a month before her arrival
- **Evidence:**
  - ch-06:p86 "The charcoal men had a story **at the vintage**".
  - p315 "My cousin's boy saw her step out of Pan's cave **at the vintage**".
  - p318 (Valens's cover story) "**Since the vintage.**"
  - Against Ch.5:
    - ch-05:p185: the neighbour borrowed the sieve "to strain her must", and "It's been in your house a month".
    - ch-05:p171: "the girl ran off at the vintage", i.e. before Mara came.
    - ch-05:p4: on arrival the olives are being beaten.
  - So the vintage ended about a month before she walked out of the cave.
- **Fix:** p86 "at the vintage" → "**this autumn**". p315 → "**when the olives were coming down**". p318 → "**Since the olives.**"
- **Cascade:** none. Kallia's "the girl ran off at the vintage" stays, since it sets up the vacancy.

### [W-05] Valens "went at it in Phocian too fast for me to follow", then his Greek is slow, flat and foreign
- **Evidence:** ch-06:p67 "the two of them went at it in Phocian too fast for me to follow". Then p81, ten paragraphs later: "His Greek was as foreign as mine. He spoke it slowly and flatly, every ending in its place … I followed all of it without reaching." The bible gives Valens "a soldier's Greek, flatly literal" and statements "in ones and twos". p312 keeps the rule: she loses the burner but "none of Valens's answers".
- **Fix (p67):** "…and after that **Kallia went at him in Phocian too fast for me to follow, and he answered her a word at a time**, until he gave her one coin back."

### [W-06] "I lost half his words", yet the charcoal burner is rendered almost verbatim
- **Evidence:** ch-06:p312 "He talked fast, in the mountain Greek, and I lost half his words". But p309, p311, p315, p317, p319, p323 and p326 are quoted whole. Only p313 shows loss ("The rest ran on past me"). The Ch.4–5 rule is that slow plain speech is followable and fast talk is not (ch-04:p8; ch-05:p8; Ch.5 audit W-03).
- **Fix (cheapest, p312):** "…and I lost **words out of everything he said**, and none of Valens's answers." Optionally break p315 into what she catches ("…the nymph… my cousin's boy… Pan's cave…").
- **Cascade:** dialogue share is unaffected.

### [W-07] "In this whole country not one person knows my name": the goat-boy does
- **Evidence:** ch-06:p116 against ch-04:p33 ("I laid my palm on my chest. 'Mara.'") and ch-04:p35 ("'Mára,' he said, and then to the goats, 'Mára!'"). The same chapter brings that boy back twice, by report (p86, p315).
- **Fix (p116):** "**In Delphi** not one person knows my name. The widow has not asked it." This also stops echoing ch-05:p159 ("There isn't a person on earth who knows where I am").

### [W-08] She stands up and eats standing "in the bottom of the crack", where Ch.3 says she cannot
- **Evidence:** ch-03:p60: near the slab "the roof came down … until I had to stoop". ch-03:p61: the crack is a foot and a half at the floor, "just wide enough to take my forearm" at shoulder height, "and above that it pinched shut". ch-03:p73: she enters it kneeling. ch-06:p1 and p241 have her kneeling in it ✓. But p249 "My fingers came free of the gap and **I stood up**… when I stood they gave a little and then held". p258 "I ate it **standing in the bottom of the crack**".
- **Fix:** p249 "I stood up" → "**I got up off my knees as far as the roof let me**". The next clause ("when I stood they gave…") becomes "when I rose they gave…". p258 "standing in the bottom of the crack" → "**crouched in the mouth of the crack**".

### [W-09] The descent goes plain → firs → cliff top, the reverse of the ascent and of Ch.3–4
- **Evidence:** Ascent: cliff top, then "Where the cliffs ended there was the plain" (p191), then "By the pen under the firs I knew where I was" (p220), then the cave. Ch.3 and Ch.4 agree: plateau → pen → firs → zigzags → cave (ch-03:p14–p15; ch-04:p61, after CH4-5). Descent as written: "On the plain there was only snow… We were under the firs before I saw them" (p277); "somewhere on the plain" (p278); "We came in among the firs" (p287); "down between the trunks" (p305); then straight to "At the top of the cliff path" (p308). The firs now lie between the plain and the cliff, and the plain is never crossed after them.
- **Fix (three touches):**
  - p277 → "**Below the mouth** there was only snow and wind and the gray's ears ahead of me… We were under the firs before I saw them…", cutting "The huts were gone." here.
  - p278 "somewhere on the plain" → "**somewhere on the slope**".
  - p308 opens: "**Past the pen the plain had no huts left in it that I could see.** At the top of the cliff path there was a red glow…"
- **Cascade:** none. The firs conversation (p287–p305) keeps its wind-shadow logic.

### [W-10] The flashlight is in the duffel at her feet while the pines are the clock
- **Evidence:** ch-05:p206: "The flashlight was somewhere in the bottom of the duffel". The bible says it is deliberately kept hidden, and "any later use must reckon with being seen". ch-06:p153: the duffel is packed and "had never been unpacked"; p159 "Everything"; p239 the bag stands by the slab. The deadline is light itself: "Two more pines after this one … Then down" (p35); "You'll be ready when the pine's gone" (p148); "The last pine but one was burning" (p244). The Ch.5 audit flagged the same gap (W-19).
- **Fix (one sentence, after p7 or p239):** "**My flashlight was in the bottom of the bag. I left it there; a light that burned nothing would have been one more thing for him to carry down the mountain.**" (Or state that the batteries are dead.)
- **Cascade:** fixes where the flashlight is for the Ch.8 night attempt.

### [W-11] A bible sample line lifted onto the page
- **Evidence:** ch-06:p165 "I have a cousin who keeps her husband's keys **in the freezer door**." The bible's Gloria sample line reads "Your keys are **in the freezer door**, don't ask me why…". The bible rule: "Sample lines are illustrations, not script. Never paste one into the manuscript". The at-risk table caps any sample-line phrase at **0**. (A 4-gram scan of Ch.6 against all sample lines and the 13 voice-bank samples finds only this one.)
- **Fix:** use a Ch.1 fact instead, for example "I have a cousin who wore one pearl and one gold hoop through a whole church service, and her husband told her it was a style." This draws on ch-01:p141, Gloria's chaos trait, as a subject not a phrase, and avoids "funeral" to keep Mara's evasion.

### [W-12] A Ch.3 sensation re-used nearly word for word
- **Evidence:** ch-06:p2 "In May this rock had let the cold out as one **thread, dry, with an edge** to it, while the walls around it stayed **damp and slow**." ch-03:p69 "a single **thread** of cold", and ch-03:p70 "It was **dry and it had an edge**, where the cold off the walls was **damp and slow**." The echo scan misses it because no single span reaches 4 words. The law (check step 5c) is that every second use of an earlier chapter's phrase is varied.
- **Fix:** recall it in fresh words, e.g. "In May this rock had breathed out a cold of its own, sharp and dry, unlike anything the walls gave off."

### [W-13] A plate comparison used twice in the book (and twice in this chapter)
- **Evidence:** ch-06:p34 "broad as a **dinner plate**". ch-06:p37 "one coat on another, like the **glaze on a cheap plate**". ch-02:p6 "the shellac had gone orange and **crazed like an old dinner plate**". voice-dna §1.5 says "no comparison is used twice in the book". p37's glaze-and-coats image is the same comparison as Ch.2's crazed glaze.
- **Fix:** p34 → "broad as **my two hands**". p37 → another domain, e.g. "one coat on another, **like paint on a fire escape**". Update the bible's Ch.6 spent list to the new wording.

### [W-14] The language-tag aside is turning into a construction
- **Evidence:**
  - ch-06:p7 "**That was English, and** he let it pass." against ch-05:p133 "**It was English, and** the words were nothing to him".
  - ch-06:p272 "I had no answer to that, **in either language**." against ch-05:p208 "I had thanked her **in neither language**".
  - In the same chapter: p156 "in English", p245 "in English", p306 "It was the wrong language".
  - Five language tags in Ch.6, two of them a cross-chapter frame.
- **Fix:** p7 → "**He let the English go by.**" p272 → "**I had no answer to that.**" Keep p156, p245 and p306; they carry information.
- **Cascade:** register this on the at-risk list: "[It/That] was English, and…" and "in (n)either language" are both SPENT.

### [W-15] "I talked to his back": a variant of a spent construction
- **Evidence:** ch-06:p164 "so I talked to his back, low." The bible's at-risk list: "**'I said to his/her back'** (SPENT)". Source: ch-04:p63 "'Is there a Kaisar in Rome?' I said to his back".
- **Fix:** "so I talked, low, **uphill into the dark**."

### [W-16] "The widow": ten uses shared by two speakers, including Mara's English
- **Evidence:** Valens: p103, p159, p271, p316, p327. Mara in Greek: p28, p30, p116, p289. Mara in English: p165 "the widow's storeroom". voice-dna §1: "No character has a recurring … epithet for another". The bible forbids shared devices. Mara knows the name Kallia (ch-05:p194–p200), so in her English monologue the epithet is Valens's word bleeding into hers.
- **Fix:** p116 "**Kallia** has not asked it". p165 "in **Kallia's** storeroom". p289 "Under **Kallia's** stairs". p159 "Does **Kallia** know you're going?" That brings it from 10 to 6 and leaves the epithet mostly to Valens, whose detachment it suits.

### [W-17] Outline Ch.7 beat 3 is now out of step with the page (CH6-7, confirmed). Patch before the Ch.7 writer is prompted.
- **Evidence:**
  - outline Ch.7 beat 3: "She refuses to speak for a month (all-or-nothing)", plus the chaos moment "the month of silence".
  - Ch.6 has already put that month on the page: "I had spoken no Greek aloud since the guide on the Sacred Way" (p39), with "most of a month" (p37).
  - She has broken it for Valens: "You go up on the mountain … all its breathings in" (p78–p79), and Greek all the next day.
  - She has broken it for the charcoal burner too: "It was oats," p322, which he answers.
  - It still holds with Kallia: "She doesn't talk" (p61); the thanks for the blanket are in English (p156).
- **Fix (outline, not manuscript):** recast Ch.7 beat 3 as the refusal **ending in front of Kallia** (or holding in front of her only, a second month). It must not start a fresh month. Foundation §3 ("won't speak it in front of Kallia for a month") is already satisfied.

### [W-18] "Laughed at on the Sacred Way, in front of the whole square" (CH6-4, confirmed)
- **Evidence:** ch-06:p254 against ch-05:p58–p61. The mimicry happens on the Way, at the bend above the Kroton base, before the rival guide, the wool-seller and two pilgrims. The market square is a separate place below the gate (ch-05:p23). Ch.6 p39 itself says "the guide on the Sacred Way".
- **Fix:** "in front of the whole square" → "**in front of half the Way**".

### [W-19] "Three months behind" on the rent (CH6-3, confirmed)
- **Evidence:** ch-06:p165. By her own clock she left Kennedy on Tue 19 May (ch-02:p52). She crossed a day or two after the Wednesday in Delphi (ch-03:p59). It is now "most of a month" later (p37), about late June 1998 in her time. Only one rent day (1 June) has passed. Ch.1 never says she owed rent before (ch-01:p116 says only that it was "unchecked"). If she is guessing by the season jump instead, the answer is six months, not three.
- **Fix:** "and I'm three months behind by now, I suppose," → "**and I'm behind by now, I suppose,**".

---

## NOTES

- **N-01 (ledger, dialogue meters).** `shape_check` (the ledger metric) gives 38% ✓. Strict quoted-words-only gives 33.6%, and the show/tell meter 33.0%. The chapter passes on the declared metric. Do not cut dialogue in any fix, and do not let the header comment ("36.8% … 38%") be read as the strict figure.
- **N-02 (ledger, gear).** Median sentence length is 11, the *low* band (9–12), against the row's *mid* (14–16). Semicolons are 0.9/1k against the ~3/1k target. This is the same pattern as Ch.1 (audit N-03), and the author's "keep Ch.6–8 moving" partly excuses it. If the evaluator wants it, rejoin 6–8 narration pairs in the backfill (p36–p44) and the climb (p161–p177) on semicolons. Leave p249–p252 short; that is the designed pressure gear.
- **N-03 (timeline, minor).** p96 "The stair's ice from the second turn" against p173 "Two turns up, the ice began", which falls *after* the third turn (p163). Make one of them agree, e.g. p96 "ice from halfway".
- **N-04 (bible drift, CH6-6 confirmed).** Valens's Ch.6 card and the Ch.6 spent list quote text that is not on the page:
  - "Don't tell me where. Whoever knows where can be asked where." (page: "Don't.", p332)
  - "I'll tell you what I'd tell them, if they asked me." (page: "So here's what I make of you.", p329)
  - "can pay men to ask" (page: "he's got the money to look")
  - "Forward. Till it stops." (page adds "and not past", p307)
  - "Nobody learns Latin on this road" (page: Mara's "Latin is not learned on this road.", p339)
  - "like milk being poured off cream" (not on the page)
  - the burner's "the council had three eaten before the fire was lit" (page: Mara catches only "the number four…", p313)
  
  Correct the card to the prose so later callbacks quote the page.
- **N-05 (conflicts resolved).** CH5-6 and the CH5-2 residual are settled by p39 and p61: the replies to Kallia in Ch.5 were English.
- **N-06 (voice, Mara's Greek).** The bible's Mara card says early Greek (Ch.4–10) is "short, careful and wrong". Ch.6's Greek is careful but often long and fluent-sounding: p28 is a 50-word period; p209–p211 explain an escapement; p331. Valens's "schoolmaster's Greek" (p115) and p79 carry the wrongness. Consider trimming p28 to two short sentences. Not blocking.
- **N-07 (spoken repetition).** Valens says "You've got Latin" twice (p115, p329). The second is the evidence recap and reads as deliberate. Do not let it recur.
- **N-08 (objects, granola; CH4-2).** Not mentioned. p272 ("could have eaten the same again") implies none is left or she is saving it; the count is never stated. Leave it, but the next mention must not contradict this.
- **N-09 (objects, outer garment; CH4-3).** A snow climb with no garment named. Valens's evidence uses only "in trousers". Fine for now. The Ch.7 himation will supersede it.
- **N-10 (new facts for ENTITY_STATE):**
  - Mara's apartment building is on Larchwood, by implication (p43).
  - Kallia's widowhood is first on the page, by Valens (p103).
  - The Seiko was reset by the gatepost's noon shadow on Mara's second day at Kallia's (p13).
  - Valens's scar is "the length of my finger" across the back of his right hand, stitched too far apart, "in a ladder" (p42).
  - The last ship left Kirrha eight days before the backfill (p69).
  - Valens was at Kirrha for the god's oxen (p314).
  - The mules: gray, brown and dun, unnamed (p197–p199).
  - The burner's kiln has been burning nine days (p311).
- **N-11 (echoes under the gate's length).** p240 "Rock. Air. Cold that was only cold." recalls ch-03:p62 ("It was rock and air, cave cold"). It is a three-fragment line, not an anaphora triad, but it sits next to that retired family. Also p239 "the two faces of rock" against ch-02:p6 "two faces of fired clay", and p209 "round and round" against ch-03 (the Hanson chorus). Minor; vary if touched.
- **N-12 (retired-reflex watch).** p330 "Most of it was true, and the whole of it was wrong." is an antithesis close to aphorism. It is mid-chapter, so not a closing aphorism, and allowed. Keep it to one.
- **N-13 (no romance signals).** p257, the bread "exactly the temperature of a person", carried against his skin, is warmth carried by an object and inside the rule. Don't stack a second such beat in Ch.7. p42, the scar, is Mara's workmanship eye ✓.
- **N-14 (plausibility).** Weeks of layered ice on a Delphi lane at about 570 m by late November (p37) is a hard year but possible. Harmless.
- **N-15 (geography, minor).** The woodstack "under the outside stair" (p59) and the storeroom "under the stairs" (ch-05:p205; p289) share the stair. That is compatible if it is long, and the page need not say so.
- **N-16 (Valens's hands).** His maintenance business in Ch.6 is all mule tack: girths (p77, p80), a lead (p152), sacking (p173, p316), unlashing (p340). The bible says "it is always a different object". Within the chapter they differ, but the class is "tack". Vary the class in Ch.7–11 (a knife edge, a lamp wick, a sandal strap).
- **N-17 (comparison domains).** "like a glass dipped in sugar" (p39) after Ch.5's "like ground sugar" (ch-05:p36) is a sugar domain twice in two chapters. Both are registered as spent. Do not reach for sugar again soon.
- **N-18 (CH6-5).** p38 "I had no idea of the way" reconciles: she knew the day-long road but not the cliff. Optional clause: "and the long road round was a day each way".
- **N-19 (CH3-7).** Mara still never says "door". Recommend resolving it, prose wins.
- **N-20 (CH4-4).** The inscription is consistent with Ch.4 (red paint; datives).
- **N-21 (header).** The comment's figures ("6,790 prose … 36.8%") are stale; the current figures are 6,634 and 38%. Cosmetic.
- **N-22 (spatial, minor).** p7 "Behind him my duffel leaned on the slab". Mara kneels in the crack and Valens stands below her, so the slab is in front of him, not behind. Make it "Beside him".
- **N-23 (information flow).** p322 "It was oats" is Greek, spoken to a stranger in front of Valens. That is fine, and it feeds W-17. Two Greek speakers have now heard her Attic.
- **N-24 (tracker housekeeping).** The CH3-3 hut is still only in outline lines 213 and 222; patch the outline. `post_patch_flags` P1–P5: the header says RESOLVED but the rows still say UNRESOLVED; align them.
- **N-25 (Seiko facts check).** These pass: the 1966 hand-wind ✓; seconds hand ✓; ratchet click forward, loose backward ✓; "a day and a night. A little more", i.e. about 40 hours ✓; *hōrologion* for a timepiece ✓ (italic, unglossed); "no sun and no water" (sundial / clepsydra) ✓; the band will not go halfway round his wrist, consistent with the Ch.2 shortening ✓. The bible's spent list should add "the watch shown on his palm without being handed over" (p12, p248). It is already registered.

---

## TRACKING DATABASES (appended for Ch.6)

### Character fact sheet, additions
| Character | Fact | Source |
|---|---|---|
| Valens | Big; his thumb covers the crown entirely; a finger-length ladder scar across the back of the **right** hand | p42, p132 |
| Valens | Greek "as foreign as mine", slow and flat; talks to the mules in Latin ("They came from Corinth") | p81, p44, p201 |
| Valens | From "North"; Latin "On the road"; pays Pan with a crust; does not admit reading ("That's what the goat boys say it says") | p206, p338, p226–p231, p225 |
| Valens | Was at Kirrha (the god's oxen; the last ship) | p69, p314 |
| Valens | Mules: the gray (lead), the brown (ate Kallia's pomegranate last winter), a dun; "five empty mules" in the string | p51, p76, p158, p199 |
| Kallia | Pays from a knot in her kerchief; buys oak; asks after the sea and "Letters" from the east | p67–p74 |
| Kallia | "the widow" (Valens's word, first on the page) | p103 |
| Mara | 33; apartment building on Larchwood (implied); the rent | p165, p43 |
| Mara | Hands after a month: split knuckles, a healing blister on each palm | p112 |
| Mara | Heel of her hand skinned on the slab (bleeding) | p249, p258, p323 |
| Charcoal burner (walk-on) | Kiln at the top of the cliff path, nine days burning; his cousin's boy = the Ch.4 goat-boy | p308–p315 |

### Master timeline (AD 70; day counts from the crossing)
| Day | Event | Source |
|---|---|---|
| 0 | Crossing; out of the cave in "October" (Boathoos); the goat-boy | ch-03:p84; ch-04 |
| 1 | Down to Delphi; olives being beaten; herald (sacrifice "the fourth day from now"); Kallia at night | ch-05 |
| 2 | Watch set by the gatepost's noon shadow | ch-06:p13 |
| 5 | "The fourth morning": an aborted start up the town; no way up the cliff | ch-06:p38 |
| ~5 | The god's oxen; Valens at Kirrha | ch-05:p99; ch-06:p314 |
| ~20 | The last ship leaves Kirrha (sea closes, about mid-November) | ch-06:p69 |
| ~28 | **Backfill:** firewood, ashes on the ice, the ask, the watch paid; snow coming lower every night | ch-06:p36–p152 |
| ~29 | **Climb:** leave before light; daylight on the last of the cliff; the plain in snow; the cave by late morning; dig until "Five to two"; snow at the mouth; descent; the kiln at dusk; the town after dark | ch-06:p153–p342 |

- **Mara's 1998 clock:** left Tue 19 May; crossed about 21–23 May; now about late June 1998 (see W-19).
- **Season check:** a November snow day on Parnassus ✓ (outline). The sea is closed ✓.

### Knowledge database, Ch.6 entries
| Information | Origin | Knowers after Ch.6 |
|---|---|---|
| Valens's name | Kallia, "Not in my court, Valens" (p48) | Mara |
| Kallia is a widow | Valens (p103) | Mara |
| The sea is shut; the last ship left eight days ago | Valens to Kallia (p69) | Kallia, Mara |
| The cave is shut (only cold) | Mara's hand, the dig, "Five to two" (p240–p248) | Mara (Valens saw failure, not meaning) |
| The watch "goes in the dark", needs winding forward, runs "a day and a night" | Mara to Valens (p129–p142) | Valens |
| Mara's "Philadelphia" | her English (p165) | Valens catches only the word; he maps it to Lydia |
| Mara's name, said in English (p165) | — | Valens hears it but does not parse it; Mara says he never asked (p335–p336) |
| "The nymph" is Kallia's | Valens's cover story (p316–p320) | the charcoal burner, and soon "all over the town" (p329) |
| Valens's reading: runaway from "a big house. Corinth, or Patrae" | his inference (p329) | Valens (wrong); Mara |

### Plot threads
| Thread | Status after Ch.6 |
|---|---|
| Return to the cave (the Ch.5 plan) | **CLOSED:** shut. Next attempt Ch.8 |
| The watch in Valens's keeping | OPEN → Ch.11 (not returned), Ch.18 (returned) |
| "Letters" from the east (Kallia's son) | OPEN → Ch.10 |
| "Men will come asking" | OPEN → Ch.9 (notice) and Ch.12 |
| The goat-boy rumor | **SPENT** (bible); not retold |
| The Greek refusal | Broken for Valens and the burner; holds with Kallia → Ch.7 (W-17) |
| The flashlight's whereabouts | OPEN (W-10) → Ch.8 night |

---

## SUGGESTED YAML PATCHES (for the entity-tracker UPDATE after the editor's fixes)

```yaml
suggested_patches:
  - entity: "contradictions.CH5-6"
    action: "remove_conflict"
    reason: "ch-06:p39 ('I had spoken no Greek aloud since the guide on the Sacred Way') and p61 ('She doesn't talk') settle the Ch.5 replies as English. One value everywhere."
  - entity: "contradictions.CH5-2"
    action: "remove_conflict"
    reason: "the residual (bible: replies to Kallia in English) now matches the page via ch-06:p39."
  - entity: "contradictions.CH3-7"
    action: "remove_conflict"
    reason: "Ch.6 keeps 'open/shut' and never says 'door' (p165, p232); in character. Prose wins."
  - entity: "objects.fathers-seiko-watch.physical"
    action: "update"
    value: { band: "steel link bracelet (links removed with pins, ch-02:p14); fold-over clasp, not a tongue-and-hole buckle" }
    reason: "audit C-01; ch-06:p120 to be re-worded by the editor"
  - entity: "contradictions.CH6-1"
    action: "keep_original"
    reason: "Ch.1 is canonical (first wound Sat 14 March 1998). Editor changes ch-06:p165 to 'since March' (W-01); then remove_conflict."
  - entity: "contradictions.CH6-2"
    action: "keep_original"
    reason: "Ch.5's hundred-drachma piece is gone with the guide. Editor re-describes the Ch.6 coin (W-02); record the denominations of the two left."
  - entity: "contradictions.CH6-3"
    action: "keep_original"
    reason: "one rent day elapsed; editor drops 'three months' (W-19)."
  - entity: "contradictions.CH6-4"
    action: "keep_original"
    reason: "Ch.5 places the mimicry on the Way; editor changes 'the whole square' (W-18)."
  - entity: "contradictions.CH6-5"
    action: "remove_conflict"
    reason: "reconcilable: she knew the long road, not the cliff path (N-18)."
  - entity: "contradictions.CH6-6"
    action: "update"
    reason: "bible Valens card and Ch.6 spent list to be corrected to the prose (N-04); then remove_conflict."
  - entity: "contradictions.CH6-7"
    action: "update"
    value: { decision_pending: "outline Ch.7 beat 3: the refusal ends (or holds) in front of Kallia only; no fresh month" }
    reason: "audit W-17"
  - entity: "contradictions.CH6-8"
    action: "update"
    value: { decision_pending: "editor adds the Athens-vs-sun clause at ch-06:p14 (W-03)" }
  - entity: "contradictions.CH6-9"
    action: "create"
    value: { entity: "timeline (the vintage)", plan: "ch-05:p171, p185 (vintage ~a month before arrival); ch-05:p4 (olives at arrival)", prose: "ch-06:p86, p315, p318 'at/since the vintage'", flag: "UNRESOLVED until W-04 is applied" }
  - entity: "contradictions.CH6-10"
    action: "create"
    value: { entity: "locations.corycian-cave (the crack's height)", plan: "ch-03:p60-p61 (stoop; forearm-wide at shoulder; pinched shut above)", prose: "ch-06:p249 'I stood up', p258 'standing in the bottom of the crack'", flag: "UNRESOLVED until W-08 is applied" }
  - entity: "contradictions.CH6-11"
    action: "create"
    value: { entity: "locations.parnassus (route order on the descent)", plan: "ch-03:p14-p15; ch-04:p61; ch-06:p191, p220 (plain -> pen -> firs -> cave)", prose: "ch-06:p277-p308 (plain -> firs -> cliff top)", flag: "UNRESOLVED until W-09 is applied" }
  - entity: "mara-reyes.knowledge"
    action: "add"
    value:
      - { fact: "Valens's name", learned: "ch-06:p48", method: "overheard (Kallia)" }
      - { fact: "Kallia is a widow", learned: "ch-06:p103", method: "told_by:valens" }
      - { fact: "the sea is closed; the last ship left Kirrha eight days before", learned: "ch-06:p69", method: "overheard" }
      - { fact: "the Corycian crack gives only cold; the way back is shut", learned: "ch-06:p240-p248", method: "discovered" }
  - entity: "valens.knowledge"
    action: "add"
    value:
      - { fact: "the watch: wound forward to full, never past; runs a day and a night; needs no sun or water", learned: "ch-06:p129-p142", method: "told_by:mara-reyes" }
      - { fact: "Mara is the 'nymph' of the charcoal men's story; she says she came 'from in there'", learned: "ch-06:p84-p91", method: "told_by:mara-reyes" }
      - { fact: "the word 'Philadelphia' in her English", learned: "ch-06:p166", method: "overheard (no other English understood)" }
  - entity: "objects.fathers-seiko-watch.custody"
    action: "add"
    value: { chapter: 6, holder: "valens", detail: "paid the evening before the climb; wound backward then forward to full; kept in his belt pouch; shown on his palm, never handed back; 'You never had a watch'", source: "ch-06:p120-p147; ch-06:p12; ch-06:p248; ch-06:p302; ch-06:p342" }
  - entity: "objects.flashlight"
    action: "update"
    value: { location_end_ch6: "in the duffel (packed 'Everything'); unused in the cave", note: "pending W-10" }
  - entity: "character-bible.at-risk"
    action: "add"
    value: ["'[It/That] was English, and…' and 'in (n)either language': SPENT (Ch.5-6)", "'talked/said to his/her back': SPENT in all wordings", "plate/glaze comparisons: SPENT (Ch.2, Ch.6)", "'the widow' as Mara's word for Kallia: avoid; she knows the name", "sample-line content on the page: 0 (freezer-door keys removed)"]
```

---

## Bottom line

Ch.6 does what the outline asks. The door is shut and only cold. Valens arrives fully formed on his four axes, with no simile, no tic, *why* only of plans, and wrong in mundane ways. Kallia stays exactly on her card. The backward winding is the anchor and is earned. The pressure gear at the wall is textbook level 1. No narration reaches forward.

**Fix before finalize:**
- **C-01:** p120, clasp, not buckle.

**Should fix (one word or one clause each, all mechanical):**
- W-01, "since March"
- W-02, the coin
- W-03, the Athens-vs-sun clause
- W-04, the vintage
- W-05, Kallia talks fast and Valens does not
- W-06, the comprehension hedge
- W-07, "In Delphi"
- W-08, crouch, don't stand
- W-09, the descent order
- W-10, the flashlight
- W-11, the freezer-door keys
- W-12, the Ch.3 echo
- W-13, the plates
- W-14, the language tags
- W-15, "to his back"
- W-16, "the widow" ×10 → 6
- W-18, "half the Way"
- W-19, the rent

**Outline, before the Ch.7 writer prompt:** W-17 (the month of silence is already spent, except in front of Kallia).
