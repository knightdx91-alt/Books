# Continuity Audit: Chapter 7 (run 2, per-chapter drift audit)

**Date:** 2026-10-19
**Mode:** MANUSCRIPT AUDIT. Ch.7 checked against Ch.1–6 as they stand on disk (all re-read in full), against the plan, and against canon.
**Chapter reviewed:** `manuscript/chapters/chapter-7.md` (6,142 prose words by `shape_check`, 6,306 by `wc -w`; **194 prose paragraphs**; breaks after p58, p128 and p182). The file was re-checked at the end of the audit and had not changed since the first read.
**Paragraph numbering:** `ch-07:pN` counts prose paragraphs only. The title, the two HTML comments and the `* * *` breaks are not counted. This is the ENTITY_STATE and Ch.6-audit convention. So p1 = "A woman in Phocis…" and p194 = the closing question. Prior-chapter citations are to the files **as they stand now**. Ch.6 currently has **341** prose paragraphs. The ENTITY rows and the Ch.6 audit cite up to p342, so they are off by one from about p102 on (N-23).
**Read against:**
- outline.md: Ledger row 7; `## Chapter 6` to `## Chapter 10`; beat 3 as patched to public silence.
- STATE.yaml: guardrails, canon, resolved decisions, ARCH-1…18. ARCH-14: "Ch.7 registers Mara as Kallia's kinswoman"; "Mara's breaks = three".
- foundation.md §3 (Mara, Valens).
- voice-dna.md: §0 stance and foreshadowing, §1, Dialogue conventions, VOICE UNDER PRESSURE, §3b.
- character-bible.md: Mara, Valens, Kallia, Emilio, Dunphy and Sosandros cards; the Ch.4–7 walk-on and spent notes; the retired and at-risk lists.
- voice-bank/samples.
- ENTITY_STATE.yaml. The file on disk is still `last_updated_chapter: 6` and carries **no ch-07 rows**, so there was no parallel-tracker content to discount. Every Ch.7 fact below is derived from the page.

**Mechanical baseline (re-run for this audit, read-only, `bash tools/check_chapter.sh 7`):**
- Style clean: simile 2.6/1k, adverb 2.9/1k, em-dash 2, foreshadow 0.
- Grammar clean (0 errors). Rhythm: 0 flagged.
- Show/tell: no flags (dialogue meter 21.0%).
- Voice-wear strict: clean. Tic gate clean, including the gesture layer. Echo scan: 0.
- And-chains 2 (cap 9). Credential asides 0 by the detector (manual count 2, N-19). Negation pivots 0.
- Metaphor: fig 3.3/1k; median sentence 17; 15.2% of sentences over 40 words.
- Semicolons: 3.1/1k (target about 3).
- Shape audit across 7 chapters: CLEAN, `--strict` clean. Ch.7 computes as `narrative` → `question`, 3 breaks, dialogue 22%, median 17.

**Total findings:** 46. **CRITICAL: 2 | WARN: 20 | NOTE: 24**

The gates are clean, the chapter hits every ledger cell, and the non-negotiable registration beat is legally exact. The page says free, kinswoman, "of her house and in her keeping", and never property.
- **The two CRITICALs:**
  - A canon break in Mara's founding wound: she says her father took her to Sicily.
  - The third and fourth book-wide uses of a construction the at-risk list closed after Ch.1.
- **The WARNs are mostly one clause each:**
  - information-flow seams: the month of silence against the spoken name; Kallia asking a name she heard; the "last boat" against the town's own dates;
  - a body break that pre-empts Ch.22;
  - cross-chapter constructions below the n-gram gate's length;
  - phrases lifted from the voice-bank samples;
  - one history slip: a governor at Corinth while Greece is still "free".

---

## Scorecard by category

| Category | Result |
|---|---|
| (a) Beats / ledger | **PASS.** Essayistic, *claim → evidence → cost*. Claim p1 (27 words, `narrative`: **at the ceiling**; see N-01). Evidence: the bath hours p38; the latrine p36; walk/sit/eyes lessons p15–p35. Beat 3, public silence after the market laughs: p63–p72; she has talked indoors "since the morning of the shovel" (p60), as patched. Beat 2 NON-NEGOTIABLE, the registration: p141–p173, entry p172; MAIRA written without a question p161. Beat 4, the swept room with the broom across it, no explanation: p37, p95, p185. Beat 5, cost + Dunphy: p183–p184. Opens toward Ch.8: the midwinter invitation p186–p193. Close `question` p194, a real question (the distance from the dance to the cave), not a button ✓. 3 breaks ✓. Dialogue 22% (`shape_check`) / 21.0% (show/tell meter) against 20–30 ✓. Gear high: median 17 ✓. 6,142 words against 6,600 (range 6,000–7,200) ✓. Character chaos: teeth (lentisk, horn powder) ✓; Dunphy, green cardigan ✓; all-or-nothing (the month) ✓. |
| (1) Character consistency | **Mara: CRITICAL ×1** (C-01, the Sicily trip). **WARN** W-02 (the bench years), W-06 (the laughter fit), W-17 (the job statement). **Kallia against her card: PASS** with W-03 and W-14. She sits once, to demonstrate, and the page marks it (p26). She answers with tasks. Her questions are about labor (p77–p86). She never names the son ("It's swept", p95) and never speaks of herself beyond the jar (p128). She had never asked the name (p157). She uses it first as "Maira. The water." (p182). **Valens: PASS.** Boots only (p96–p106); three short level lines; no comparison; no hands business; does not learn her name; knows she can talk ("No.", p106). **Sosandros: PASS** against Ch.5. Thin, at the doorway, corrected the herald (ch-05:p100, p116 "the clerk in the doorway"). Mara learns his name from Kallia (p142). He corrects a name once (p150); see N-13. |
| (2) Timeline | **PASS with NOTE N-02.** The day count holds (see the Master Timeline). The chapter runs from the morning after the late-November climb to about the turn of the year AD 70/71. The midwinter rite lies ahead, matching outline Ch.8 "(midwinter, AD 71)". "Second year of Vespasian" is correct (dies imperii 1 July 69). WARN W-15 (governor at Corinth) is a history-layer item. |
| (3) Information flow | **WARN ×3:** W-01 (silence "for a month" against the spoken name), W-03 (Kallia asks a name she heard), W-04 ("the last boat" against "since the olives"). Otherwise clean. Who knows her name, and since when, is fully traceable (Knowledge DB). Kallia never asked it (ch-05; ch-06:p115 "Kallia has not asked it"; ch-07:p157). The first Delphian hearing is the council table (p158). The gossip carries exactly what Ch.6 seeded and no more: the boat (Valens's lie, ch-06:p319 → p139–p140), "Kallia's" (ch-06:p315 → p119), the mountain ("So the town says", p20). The nymph is not retold (but see W-05). |
| (4) Objects | **PASS.** The watch is with Valens and there is **no clock time** anywhere in AD 70. "I had morning, noon by the shadow of Kallia's gatepost, and the day's end by the lamps" (p107), consistent with ch-06:p13. Dunphy's "three o'clock" is 1970s memory. Shovel: returned p2–p7 to "the ash pail where it lived" (ch-06:p42) ✓. Flashlight: under the jeans in the duffel "since October without anybody in that house setting eyes on it" (p10; ch-05:p206; ch-06:p7) ✓. Duffel: jeans, fleece, the buttoned shirt, flashlight, toothbrush (p10, p58). Clothes: tunic, cord, the girl's himation; boots kept (p14) ✓. The himation recurs as the anchor (p11, p174, p183, p197) ✓. Pale band "since March" (p48; ch-06:p164) ✓. N-10 covers the sweater and jacket. |
| (5) Plot threads | **PASS with WARN W-05.** Son's room: swept, broom across, unexplained; Ch.10 untouched ✓. Letters from the east: not touched ✓ (held for Ch.10). Nymph rumour: not retold ✓, but the narration hands Mara the word again (W-05). **"Men will come asking": PASS.** Nobody asks after Mara. The drover is a man at a spring (p109–p122), the fountain man only watches (p70), and the clerk's questions are the census, not a pursuit. Ch.9's notice is not pre-empted. "Husband's brother": Mara asks (p136), Kallia evades (p137), and Mara then supplies "Aimilios" as her father (p163), with Kallia's cover (p165). Coherent; cascade in N-07. |
| (6) World rules | **PASS.** The cave is shut; no door word ("the dark arch and its painted letters", p194; CH3-7 holds). No crossing mechanics. **History: WARN ×1** (W-15). The rest passes (N-21). |
| (7) NO FORESHADOWING | **PASS.** Gate 0. Manual read: the closing question is a present plan, not foreknowledge. "Kallia had been nearer the truth than she could have known" (p54) is past-facing. "Next year's list" (p174) is council practice, not plot. "Halfway through my silence" (p96) and "for a month" (p71) are iterative summary within the chapter's own span (W-01 fixes the latter's accuracy). No 79, no Italy. |
| (8) NO TICS | **Mechanical: PASS. Manual, constructions the gates cannot see: CRITICAL ×1** (C-02) **and WARN ×8:** W-07, W-08, W-09, W-10, W-12, W-13, W-14, W-20; W-11 (sample lifts) and W-18 (indefinites) are density/lift items. Spoken refrains: none at 3+. "Simple" ×5 and the spitting wood are watched (N-05, W-13). |
| (9) Voice drift | **Mostly PASS.** High gear, spirals in calm, and asides at density are exactly the voice-dna "voice opens" row for Ch.7. 1998 comparison domains rotate: a zip-code clerk, a pediatric clinic, Rittenhouse gin, the Philadelphia vowel, fourth grade. Mara's Greek is uncontracted throughout ✓ (bible sync, Ch.6). It is long and fluent at p79–p87 (N-04, same as Ch.6 N-06). The bible's Ch.7 "as written" blocks drift from the page (W-19). |

---

## PRIORITY: UNRESOLVED ENTITY_STATE CONFLICTS (processed first)

ENTITY_STATE on disk = Ch.1–6 only (`chapters_tracked: [1..6]`, no `ch-07` rows, no CH7-n). Each open conflict was checked against Ch.7:

| ID | What Ch.7 does to it | Verdict |
|---|---|---|
| **P2** outline Ch.7 "grateful to be owned" | outline.md Ch.7 beat subversion now reads "grateful to be written down as somebody's kin"; beat 2 "a free woman under Kallia's guardianship (never property…)". The page agrees (p146–p147 "Free."; p172). | **RESOLVE.** The outline now carries one value. "The worst humiliation" (the emotional-surprise line) is a feeling, not a legal status; leave it. |
| CH4-3 jacket vs fleece | p10 names "the fleece" and, new, "the shirt with the buttons" going into the bag. "Jacket" still appears only in Ch.3. | Unchanged. Ch.7 adds evidence that the Part One outer garment is the fleece. Open (N-10). |
| CH3-7 door never named | Still never named (p194 "the dark arch") | In character. Recommend RESOLVE, prose wins. |
| CH4-2 granola; CH4-4 inscription; CH5-3 film frame; CH5-4 microcassette | Not on the page in Ch.7 (p194 recalls only "painted letters", consistent with ch-04:p28 and ch-06:p221) | Unaffected; schedules intact (tape next in Ch.19). |
| CH6-5 the first attempt | Not touched | Open, unchanged. |
| P5 notice timing | Valens still works openly at Kallia's gate (p96–p106) | Consistent with the patched plan (notice reaches Delphi in spring 71). |
| CH1-2, CH1-3, CH2-1, CH2-3, CH2-4, CH2-5, CH3-1, CH3-2, CH3-3, P1, P3, P4 | Not touched by Ch.7 | No change. |

---

## CRITICAL ISSUES (fix before finalize)

### [C-01] Mara went to Sicily with her father at fourteen. Canon says he never took her.
- **Category:** character consistency (Mara's wound); a foundation-level contradiction.
- **Evidence:**
  - **ch-07:p140:** "I had been to Syracuse, as it happened, at fourteen, in a rented Fiat, with my father driving one-handed and pointing out of the window at quarries from Catania on. I remembered a fountain full of papyrus and ducks, and a gelato that tasted of nothing but cold."
  - **foundation.md §3, Mara, Wound:** "He promised 'next season, you come with me' for twenty-five years and **never took her**. He died in January 1998 with the promise still unkept."
  - character-bible, Emilio: "His promise to take her ('next season, you come with me') may be quoted verbatim **once in the whole book**." That promise is still to come on the page; this trip would falsify it in advance.
  - Ch.1 builds the same wound on the page:
    - she sees Sicily only as slides "at our kitchen table every September of my childhood, projected onto a bedsheet" (ch-01:p11);
    - at nine she stays behind when "my father's taxi pulled away for Sicily" (ch-01:p150);
    - Ch.6 adds "he came home when he said he would maybe twice in my whole life" (ch-06:p164).
- **Why CRITICAL:** it is the one fact the arc is built on (visitor → the one who stays; "the people you love go away to the past"). A reader who meets the "next season" promise later will remember that he drove her round Sicily.
- **Minimal fix (p140; keeps the papyrus, the ducks, the gelato and the joke; checked fresh against Ch.1–6):** "I knew Syracuse, as it happened, from his slides: a quarry deep enough to stand a church in, a fountain full of papyrus and ducks, and his voice in our dark kitchen telling me the gelato there tasted of nothing but cold. It did not seem the right moment to bring that up."
- **Cascade:**
  - Remove "Mara's father driving a rented Fiat from Catania to Syracuse when she was fourteen" from the bible's Ch.7 mention-only list.
  - Do not create a travel row in ENTITY.
  - The new wording avoids "every September", "bedsheet" and "projector fan", which are already used twice each in Ch.1/Ch.3.

### [C-02] "The [color] of [thing]": the third and fourth uses in the book, after the shape was closed
- **Category:** NO TICS (closed device). Precedent: Ch.4 audit CRIT, "third uses of … the [color]-of-[thing] shape".
- **Evidence:**
  - At-risk list (bible, after Ch.1): "**the [color] of [thing]** as a sentence shape… a third use anywhere in the book is a defect."
  - Already spent: ch-01:p4 "burned **the pink of boiled ham**"; ch-01:p36 "the water below the bridge was **the color of an old nickel**".
  - Ch.7 adds two:
    - **ch-07:p10** "a himation **the color of wet sand**";
    - **ch-07:p151** "each letter surfaced pale in the dark wax, **the color of the wood showing through**".
- **Minimal fix:**
  - p10: "a himation **of wet-sand brown**, which Kallia shook out by two corners…"
  - p151: "each letter surfaced pale in the dark wax **where the bare wood showed through**."
  - Both were checked clean against Ch.1–6 at 3- and 4-gram length.
- **Cascade:** the bible's Ch.7 anchor note and the header comment ("borrowed himation") are unaffected. Register the shape as CLOSED at 2 in the at-risk list.

---

## WARNING ISSUES (fix before finalize under the drift policy; each is a word or a clause)

### [W-01] "I said nothing outside Kallia's gate … to anyone, for a month", then she speaks at the council
- **Evidence:** ch-07:p71 against p158 ("'Mara,' I said."), p159 ("the first word I had said outside her gate in nineteen days") and p163 ("Aimilios"), all inside the same month (p183 "Before the month was out…"; p185 "On the last morning of the month").
- **Fix (p71):** "I carried the salt home through the town, and **for a month after that, outside Kallia's gate, I said nothing to anyone that I could help.**" The exception is then built in, and p159's "nineteen days" lands as the break it is.

### [W-02] "Fifteen years at a bench" against "ten years in a basement lab"
- **Evidence:**
  - ch-07:p174 "I had spent fifteen years at a bench…";
  - ch-03:p2 "My lungs had spent ten years in a basement lab";
  - ch-03:p25 a graduate seminar at twenty-four;
  - ENTITY `mara-reyes` trait: "has worked about ten years in the basement lab", `mutable: false`.
- **Fix:** "**I had given ten years at a bench to keeping things from being wiped smooth**, and I had just been written into wax…" The plain "had spent ten years" would echo ch-03:p2 at 4-gram length.

### [W-03] Kallia asks "What name did you give him?" She was standing beside Mara when Mara said it
- **Evidence:** p157 ("Kallia opened her mouth beside me and shut it again"), then p158 "Mara," then p180 "What name did you give him?" She cannot read, so "What did he put?" (p177) is right; the name question is not.
- **Fix (p180):** "**Say your name for me.**" p181 "Maira," I said, and p182 stand. This also gives Kallia her first request for Mara herself, which suits the card.

### [W-04] "The last boat before the sea shut" against the town's own sighting of her
- **Evidence:**
  - p135 "you came on the last boat before the sea shut, after the vintage"; p153 to the clerk "She came on the last boat, after the vintage".
  - The last ship left Kirrha about three weeks after Mara came down (ch-06:p69 "eight days ago" in the late-November backfill).
  - Valens's lie, which is the source the spring repeats, says "Since the olives" (ch-06:p317), i.e. late October.
  - The town saw her "in my first week, still in trousers" (ch-07:p36).
- **Fix:** p135 "you came on **one of the last boats** before the sea shut, after the vintage"; p153 "She came on **one of the last boats**, after the vintage." The stranding logic survives.

### [W-05] The Maira/sea-nymph echo: the narration gives Mara the nymph word again
- **Evidence:**
  - ch-07:p161 "a Maira among the **sea-nymphs** who rose from the water…" and "The clerk had made me a **sea-nymph** or a star with four legs".
  - The rumour's word: ch-04:p83 "Nymphē." (the Ch.4 pull line); ch-06:p86 "a nymph walk out of Pan's cave"; ch-06:p314 "That's her. The nymph."
  - Bible: "The goat-boy's nymph story told by a third party: SPENT; the rumor is not retold again."
- **Problem:** nothing is retold, but the paragraph-ending quip lands on the rumour's own word, and a reader reads it as a wink back to Ch.4 and Ch.6.
- **Fix (p161):** "sea-nymphs" → "**Nereids**", and "a sea-nymph or a star" → "**a Nereid or a star**". The Homeric fact (Iliad 18, the Nereid Maira) is exact and needs no "nymph". Update the bible's spent entry to "a Nereid or a star with four legs".

### [W-06] The laughter fit on the step ("I could not stop") pre-empts the Ch.22 break
- **Evidence:**
  - ch-07:p174 "laughed into it. I laughed without a sound, with my shoulders. **I could not stop.**"
  - foundation §3, failed emotional management: three breaks, the third "an uncontrollable fit of laughter" in the Basilica (Ch.22), "earned by nothing".
  - STATE ARCH-14: "Mara's breaks = three".
  - bible, at-risk after Ch.6: "any body rebel before then uses a different channel". Laughter **is** the Ch.22 channel.
- **Fix (p174):** "…pulled the borrowed wool up to my eyes, and laughed into it without a sound, with my shoulders, **until it had run its course**." The relief stays; the loss of control goes.

### [W-07] "There was no Greek for that, and no English either.": the spent language-tag family, ending on a negation
- **Evidence:**
  - ch-07:p92.
  - Bible at-risk after Ch.6: "'[It/That] was English, and…' and 'in (n)either language' SPENT".
  - Sources: ch-05:p208 "I had thanked her in neither language"; ch-06 W-14 cut "in either language".
  - The at-risk list also names "paragraphs ending on a negation".
- **Fix:** "**Hers was the one question I could not answer by doing something.**" This turns Kallia's own method back on Mara, needs no language tag and ends affirmatively.

### [W-08] "I knew to the grain what a powder like that did to a glazed surface": the Ch.5 olive-oil construction again
- **Evidence:** ch-07:p58 against ch-05:p5 "I knew **to the decimal what** olive oil **did to the** fabric of a terracotta lamp". This is the knowledge-provenance aside in the same frame (I knew to the [unit] what [substance] did to [ceramic]).
- **Fix (p58):** "I looked at the grit in it, which showed without my bending close; **I had seen glazes scoured to a dull fog by less**, and the girl stood there smiling at me with every tooth in her head, and all of them sound." This also removes one "anybody" (W-18).

### [W-09] The breathings-and-pitch description of her Attic, a fourth and fifth time
- **Evidence:**
  - ch-05:p57 "with every aspirate and every accent where the grammar had put it";
  - ch-05:p58 "with every aspirate blown and the pitch rising and falling on the accents";
  - ch-06:p79 "The sentence left me with all its breathings in";
  - **ch-07:p59** "and with every breathing breathed";
  - **ch-07:p63** "with the breathing on the front of the word and the pitch climbing wherever the accent stood".
- **Fix:**
  - p59: delete ", and with every breathing breathed", so it reads "…in the vowels a Dutch scholar in the fifteen-hundreds had decided it ought to have, and the Greek of Delphi had not waited for him."
  - p63: "I asked her for an obol's worth in the Attic of the books, **careful with every syllable**, and I added please." (Not "in my best Attic", ch-05:p57, and not "the way the books printed it", ch-04:p10.)

### [W-10] A listener names what her Greek sounds like, again by performance: "like a man in a play"
- **Evidence:**
  - ch-07:p160 (Sosandros) "asked for a cup of water **like a man in a play**", eight paragraphs into a chapter that already has "off the stage" and Antigone (p68–p69).
  - The same move earlier: ch-05:p19 "like the man who reads out the laws"; ch-05:p59 "the Pythia's grandmother"; ch-06:p114 "a schoolmaster's Greek".
  - Bible at-risk after Ch.7: "Mara mocked for her Greek in public … CLOSED. Her accent may draw a remark, never another set-piece".
- **Fix (p160; keeps his pleased-with-himself longer sentence and the Sicilian excuse):** "I heard a Syracusan at the Pythian games once, **and half the stand had to help him get a cup of water**." (Not "It took him three tries", which would echo ch-06:p119 "It took me two tries".)

### [W-11] Phrases lifted from the voice-bank samples (cap 0) and one comparison at its third use
- **Rule:** bible at-risk table, "any phrase in a sample line in this file or in a voice-bank sample | 0". A 4-gram scan of Ch.7 against `voice-bank/samples/` finds:

| ch-07 | Page | Sample | Fix |
|---|---|---|---|
| p184 | "in **a green cardigan with** the second button gone" | sample-04 "She wore a green cardigan with one button missing" | "in a green cardigan **that had lost its** second button" |
| p184 | "when I was **in the fourth grade**" | sample-04 "in the fourth grade" | "when I was in fourth grade" |
| p184 | "**I never found out why**, …" | sample-04 "I never found out why she cried" | cut the sentence (W-12) |
| p76 | "the hearth was **down to a red bed under the ash**" | sample-12 "the fire had gone down to a red seam under the ash" | "the hearth **had burned low**" |
| p36 | "**The women of Delphi**, so far as I could tell" | sample-03 "what the women of Delphi used to clean their mouths" | "**Delphi's women**, so far as I could tell" |
| p161 | "spelling **a word he had** seen all his life" | sample-04 "a word he had got wrong" | "**as easily as** a man spelling **a name he had known** all his life" (this also clears the third book-wide "as plainly as a": ch-02:p4, ch-03:p14) |
| p183 | "**and Kallia told him** the hedge was better company" | sample-04 "and Kallia told him" | "and Kallia **said** the hedge was better company than he was" |
| p38 | "**looked at me over** it" | sample-02 "looked at me over the top of the glasses" | "**eyed me over** it" |
| p48 | "turned **it to the window** to look" | sample-09 "said it to the window" | "turned it **toward** the window to look" |

- The cardigan's green and the missing button are canon (Dunphy card); only the sample's wording goes. The sample-04 registration scene is otherwise **not** followed: there Kallia supplies the name, but on the page she cannot. That is correct per outline.

### [W-12] The memory insert closes the way Ch.6's did: a stranger, then "nobody ever knew"
- **Evidence:** ch-06:p43 (Larchwood) "…In March he moved out. **Nobody in the building ever learned his name.**" ch-07:p184 (Dunphy) "…**I never found out why, and nobody else in that room did either, so far as I could tell.**" Two consecutive chapters close an unprompted-memory paragraph on the same move. This one also lifts sample-04's line (W-11) and ends on a negation.
- **Fix:** delete the last sentence of p184, so the paragraph ends "…and at three o'clock the bell went and she wiped her face with the backs of her fingers and said we could go." The not-knowing stays implicit, and canon is untouched: the Dunphy card's "No one ever learned" is an evasion, not a line.

### [W-13] The spitting-wood exchange is becoming a running bit
- **Evidence:**
  - ch-06:p54–p58, p66: "It'll spit. The last lot spat a coal on **a Theban**'s cloak…" / "That was pine. This is oak." / "Then it'll spit oak." / "…burn without spitting".
  - ch-07:p97–p100: "It burned." / "It spat." / "Oak doesn't spit." / "Twice. Once on my good hearthstone and once **on a Theban**. When it's done a month without spitting…"
  - Seven "spit" words over two chapters, in the same two mouths, with the same victim.
- **Fix (p100):** "Once on my good hearthstone and **once in the lentils**." Then mark the spitting-oak haggle **SPENT** in the bible: the fifth coin is paid or forgotten off-page, never argued a third time.

### [W-14] Two section breaks close on Kallia's water order (device as scene button)
- **Evidence:** the p128 close of section 2, "Go back down and fetch the water in the old one. It leaks. Walk quick.", and the p182 close of section 3, "Maira. The water." Both are Kallia task-lines about water ending a section. That is the retired reflex "any … line used as a scene button".
- **Fix (p128, reorder; keep p182, the stronger and the planned one):** "'That jar came up from Kirrha on my own head, eleven summers ago, and I've not had to buy one since. Go back down and fetch the water in the old one. It leaks.' **She swept the pieces off the hearthstone into the ash pail with her foot.**" Drop "Walk quick." and drop "the side of" (ch-06:p198 and p248 already use "with the side of").

### [W-15] "The governor's men in Corinth" while Achaea is still "free"
- **Evidence:**
  - ch-07:p129 "…before the governor's men in Corinth thought to ask for it".
  - foundation §3, Valens: "Nero's grant of 'freedom' to Achaea (late 67) **abolished the post**".
  - Bible, Celer: "back on the **restored** proconsul's staff by 71–72".
  - The same paragraph has the freedom not yet revoked ("nobody at the spring knew when").
- **Fix:** "…before **Rome put a governor back in Corinth** to ask for it." The spring's guess is now in the future, as the history requires.

### [W-16] The shut room is "at the end of the gallery" and also "at the top of the stair"
- **Evidence:** p37 "at the end of the gallery, past the lodgers' rooms, where they never went" against p95 "who slept in the room at the top of the stair". The Ch.10 anchor (the broom across the threshold) needs one location. ch-06:p153 places Kallia herself "at the top of the outside stair".
- **Fix (p95):** "the room at the top of the stair" → "**the shut room upstairs**".

### [W-17] Mara's job statement for the fourth time, now with the Ch.5 tail "for a living"
- **Evidence:**
  - ch-03:p30 "I fix pots. In a museum.";
  - ch-05:p159 "I glue lamps back together **for a living**";
  - ch-06:p164 "I make the cracks in old pots disappear";
  - **ch-07:p85** "I mend old pots **for my living**".
  - The bible closed the English-speech version of this at three. The Greek answer here is earned (Kallia asks what the women do), but the formula is repeating.
- **Fix (p85):** "They go out to work, the same as the men. **My work is pots older than this house, that somebody has dug up.**" Uncontracted, per her Greek.

### [W-18] Indefinite-pronoun density: 24 in 6.1k words (nobody 8, somebody 8, anybody 6, everybody 2)
- **Evidence:** Ch.2 precedent (audit: somebody/nobody ×16, cut to 5). Ch.6 has 16, Ch.7 24. The thematic "somebody" is intended (p1 "belonged to somebody"; p183 "to be somebody's") and stays. The narration's incidental ones cluster.
- **Fix (narration only, five trims):**
  - p10 "without anybody in that house setting eyes on it" → "**unseen by a soul in that house**";
  - p25 "if nobody spoke to me" → "**if the court stayed quiet**";
  - p36 "There were other lessons that nobody had to teach me, because the town did it for her." → "**Some lessons the town taught for her.**";
  - p122 "if anybody in Delphi had wanted a jar back that had been broken once" → "**if Delphi had any use for a jar that had been broken once**";
  - p58 is cleared by W-08, and p184 by W-12.

### [W-19] Character-bible Ch.7 "as written" blocks quote lines that are not on the page (sync before the next writer prompt)
- **Kallia block:**

| Bible | Page |
|---|---|
| "Then the god can put an edge back on it." | "**Let the god** put an edge back on it." (p7) |
| "When a woman looks at a man, she's asking him something … Out there, somebody answers her." | "Look at a man out there and you've asked him something. And somebody answers." (p33) |
| "Then what do the women do all day?" | "What do the women do all day?" (p84) |
| to the shut-room question: "Nobody." | "It's swept," then "Tighter, I said" (p95). The at-risk entry "Kallia answering a question about the shut room ('Nobody.' / 'Tighter, I said.')" must read "It's swept." |
| "Then who've you got for my house? You've had nobody else on that line for years." | "Who stands for my house, if I don't? You've had no other name on that line for years." (p169) |
| "Every other winter they go, and this is the winter." | "They go every other winter, and this is the winter." (p189) |

- **Valens block:** "She's got you walking." → page "She's taught you to walk," (p102).
- **Sosandros block:** "And what is a girl from Syrakousai doing in Phocis at the year's end?" is **not on the page**; the page has "Resident since when? On what business?" (p152).
- **Walk-ons:**
  - salt-seller: "Antigone! Antigone's come down off the stage" → page "Antigone! … She's come down off the stage" (p68); "Come again tomorrow and ask for pepper, Antigone." → no "Antigone" on the page (p70). **"Antigone" is 2 on the page, not 3.** The cap note should say 2; the rule "if she returns she calls Mara something else" can stand.
  - drover: "Here's the simple one." → page "Here's the one that doesn't talk." (p109); "Look at me, simple." → page "Look at me." (p111). **"Simple" is the drover's twice, not three times** (N-05).
- **Spent list:** "a woman stripped of her clothes in that room was a document" is not on the page; remove it. Change "a sea-nymph or a star with four legs" after W-05.
- **Mention-only list:** remove the Fiat trip (C-01), and the young man in the good cloak, who is not on the Ch.7 page.
- **Why WARN, not NOTE:** later callbacks and the at-risk caps are written from these blocks. Ch.6's N-04 was the same problem, and it recurred.

### [W-20] "As broad as" ×3 book-wide, two of them in Ch.7, and a coin as the ruler twice
- **Evidence:**
  - ch-05:p44 "a rosette of lichen … **as broad as a coin**";
  - **ch-07:p48** "a round pitted mark **about as broad as an obol**";
  - **ch-07:p117** "**as broad as a doorway**".
  - voice-dna §1.5: "no comparison is used twice in the book". An obol is a coin.
- **Fix (both subtractive):**
  - p48 "a round pitted mark, puckered in the middle, and she put her thumb on it" (drop the ruler; "the size of a fingernail" is SPENT, so no substitute is needed);
  - p117 delete ", as broad as a doorway", since p63 already gives "a broad woman".

---

## NOTES

- **N-01 (ledger, the opener).** The first sentence is exactly **27 words**, the top of the `narrative` band (9–27). Any edit to p1's first sentence that adds a word flips it to `long-spiral` and breaks the ledger. None of the fixes above touch it.
- **N-02 (timeline arithmetic).** It holds within the chapter's own looseness:
  - "Halfway through my silence" is about day 15 of the silence, then "Four days after that" (p108), then "that same night" (p130), then "Tomorrow" (p131), which puts the council at about day 20. "Nineteen days" (p159) is close enough.
  - "That same night" (p130) has no explicit antecedent after the section break. It reads as the jar day; optional "That night, the night of the jar,".
  - "The last morning of the month" (p185) is the silence month: about day 65 from the crossing, about the turn of the year. Mara has no calendar since the watch went.
  - Midwinter still lies ahead, consistent with outline Ch.8 "(midwinter, AD 71)".
  - "Fed me lentils for two months" (p157), about 7–8 weeks ✓.
- **N-03 (comprehension).** Since Ch.6's burner ("I lost words out of everything he said") no word gets past her.
  - The bath (p39–p53), the salt row (p68–p69), the drover's western Greek (p111), and the latrine men "in my first week" (p36) are all rendered whole.
  - After about two months of immersion that is plausible, but the first-week latrine chatter sits against Ch.5's partial grasp of fast talk (ch-05:p8, p117 "most of it").
  - Optional: let one word in p36 go past her ("the price of oil at Kirrha, and something about the Jews' war I half caught").
- **N-04 (voice, Mara's Greek).** It is uncontracted throughout ✓. But p79–p87 are long, fluent periods against the card's "short, careful and wrong" for Ch.4–10 (same as Ch.6 N-06). Not blocking; trim one answer if the evaluator asks.
- **N-05 ("simple").** It occurs 5 times: Kallia p73, p75, p105; the drover p111 ×2.
  - It is the spring's label, so the drover carrying it is information-consistent.
  - The bible's retirement after Ch.7 is right. Do not let Valens or anyone else use it again.
- **N-06 (the tree).** Kallia again blames the gray for the pomegranate (p100), though Valens said "That was the brown" (ch-06:p51). That is in character (she does not concede), but the gag is now SPENT.
- **N-07 (cascade: the husband's brother).** The register makes Kallia's late husband's brother "Aimilios", a Syracusan who could pass as Roman ("Half Syracuse is Roman", p165).
  - Ch.10's Ariston letter, and any later mention of Kallia's in-laws, must not contradict this (no uncle with another name, and no "my husband was an only son").
  - "You've had no other name on that line for years" (p169) fits Ariston's long auxiliary absence ✓.
- **N-08 (Kallia's knowledge, new in Ch.7).**
  - Mara speaks Greek, from p3; her reaction is "her eyes came round to me", which is understated and fine.
  - Mara's name and her father's name.
  - Mara reads: she reads the wax and recites the entry (p171, p178), a clean setup for Ch.10's reading with no narratorial nudge.
  - Mara's account of a country with piped hot water, which Kallia disbelieves.
  - She knows of the cave by gossip ("So the town says", p20; "Not as high as your cave", p193) and from Mara herself (p6).
  - She still does not know about the watch deal.
- **N-09 ("Mera at the water", p183).** The spring learns the name off the page (via Kallia, the salt-seller, the council line). It is plausible and unshown; it needs no fix.
- **N-10 (objects).** CH4-3 stays open: Ch.7 names the fleece and a "shirt with the buttons" and never a jacket. The **sweater** (ch-04:p43; ch-05:p1, p209) is unaccounted for in "All of it goes in the bag" (p9); presumably it is already in the bag. The **toothbrush** gets its first description, "purple, with a rubber grip" (p58). That is compatible with Dr. Pinsky's softer, angled-head brush (ch-05:p153); later chapters must keep it. Granola, Pentax, notebook, knucklebone, tape: no touch ✓.
- **N-11 (the vaccination).** "A cow's pox" (p54) is the folk version; US smallpox vaccine in the late 1960s was vaccinia, a cousin of cowpox. Optional for an informed reader: "a cousin of the cow's pox". The scar, "high on my left arm", is a new body fact for ENTITY.
- **N-12 (geography).** "The women had it from first light until the sun was over the cliffs" (p38). The Phaedriades stand north of the town and the winter sun never clears them; morning sun comes over the eastern ridge. Optional: "until the sun was on the paving".
- **N-13 (rendering).** "'Syrakousai,' he said, correcting her" (p150). In the English rendering Kallia's "Syracuse" and his "Syrakousai" are the same word, so the correction has no visible object. Optional: give Kallia the Phocian/Doric form in p149 ("From Syrakosai.") so that his koine form corrects something. The bible's Sosandros card already caps his correction move at two.
- **N-14 (within-chapter bookends, deliberate).** "Zip code" p1 and p183; the broom "at the same slant" p37 and "at its slant" p185; "two steps behind" (p175) after the lesson. Each is ≤2 and designed. Do not carry any of them into Ch.8.
- **N-15 (teeth).** This is the full surfacing as planned (horn powder, lentisk). The lentisk splinter at the upper-left filling (p170) is the third physical use of that tooth (ch-02:p50 floss; ch-05:p154 Kallia's lamp). Rest the filling until Ch.20.
- **N-16 (narrating stance).** p54 "nearer the truth than she could have known" is past-facing and safe. It sits near Family A's "I could not have known", so do not reuse the frame. p174 "next year's list" is practice, not plot. ✓
- **N-17 (rhythm).** p11 "It was heavy, and it was not new, and it smelled of somebody." is a three-clause *it* chain next to the retired anaphora-triad family. The rhythm gate is clean; vary it if touched.
- **N-18 (texture).** "A man at the fountain laughing along … his eyes on me" (p70) rhymes with the Ch.5 procurer at the same fountain (ch-05:p133). That is good menace texture, and he does not come asking ✓. Keep him unnamed and unreturned before Ch.9.
- **N-19 (credential asides, manual).** Two: p59 the Erasmian schooling; p70 "the one tragedy I had read through twice in the original". The workmanship clauses (p58, p122, p151, p174) are her attention axis, not credentials. Under the cap of 4 ✓.
- **N-20 (Valens's new body fact).** Boots of rawhide, laced to the shin, one lace broken and knotted, "the knot standing up like a little fist" (p96). This is the first footwear fact; ENTITY should add it. The bible's "boots-only sighting" is spent ✓.
- **N-21 (period accuracy: passes).**
  - Erasmus, Dutch, 1528 ✓; αι→[e] and η→[i] in rural speech ✓ (consistent with the goat-boy's "Nümfi", ch-04:p7).
  - The Nereid Maira, Iliad 18 ✓; Maira the dog of Ikarios, "somewhere else" (not attributed to Homer) ✓.
  - Tersorium and channel latrine ✓; segregated bath hours ✓; wooden clogs for the hot floor ✓; burnt-horn dentifrice ✓; lentisk (mastic) chew-stick ✓; warp-weighted loom starting border ✓.
  - Thyiades every other winter on Parnassus ✓; Syracuse a Roman colony ✓; Arethusa's papyrus and ducks ✓.
  - Vespasian revoking Achaean freedom, date unknown to the spring ✓ (but W-15).
- **N-22 (the silence audit).** Public speech before the silence: the bath (p56, p58) ✓. After p71: only p158 and p163, at the council ✓. Silent at the gate with Valens (p96–p107) and at the spring with the drover (p109–p122) ✓. Inside the house: p73–p95, p125–p127, p132–p138, p178–p181, p188–p192 ✓. This matches outline beat 3 as patched.
- **N-23 (tracker housekeeping).** chapter-6.md (written 15:45) now has **341** prose paragraphs; ENTITY (15:44) and the Ch.6 audit cite up to **p342**. One paragraph went at about p101–p102, so every `ch-06:pN` from about p102 on is +1 (e.g. "Men will come asking" is now p341, not p342). Re-anchor on the next UPDATE.
- **N-24 (downcast-gaze business).** There are nine instances (p20, p63, p72, p103, p110, p112, p157, p175, p183). They are the chapter's subject (Kallia's lesson in practice) and situational, not a tic. Do not carry the business into Ch.8, where the women's heap is the opposite register.

---

## TRACKING DATABASES (appended for Ch.7)

### Character fact sheet, additions
| Character | Fact | Source |
|---|---|---|
| Mara | Smallpox-vaccination scar, round, pitted, high on the **left** arm (pediatric clinic, West Philadelphia) | p48, p54 |
| Mara | Pale watch band still visible on the wrist weeks after the watch went | p48, p113 |
| Mara | Hair: a dark crimped hair in the himation is "darker than mine" (first relative hair fact; colour still unset) | p11 |
| Mara | Registered: *Maira, daughter of Aimilios, of Syrakousai; free; kinswoman of Kallia, of her house and in her keeping* | p172 |
| Mara | Answers to "Mera" at the water; English given up even alone; lentisk stick daily | p183 |
| Mara | Erasmian pronunciation; the town's αι≈e and η≈i; mocked at the salt market ("Antigone"); a month of public silence | p59–p72 |
| Kallia | Sits once (to demonstrate), up at once; washes standing at the bath; lies flatly for Mara ("Over the sea." / "Pox."); never names the son; the shut room swept daily, the broom left across its threshold, a second broom for the rest | p26, p44–p53, p37, p95, p185 |
| Kallia | Second-best jar carried up from Kirrha "eleven summers ago" (broken in three, Ch.7) | p128 |
| Kallia | Pays fees from the kerchief knot (as ch-06:p67) | p170 |
| Valens | Rawhide boots laced to the shin; one lace broken and knotted | p96 |
| Sosandros | Thin; hot brick under his feet; clerk's boy; warms each wax leaf over the brazier; two-obol fee | p141, p151, p173 |
| The runaway girl | Left "when the grapes came in, in what she stood up in"; quince hair oil; dark crimped hair; a hurried brown darn | p11–p12 |

### Master timeline (AD 70–71; day counts from the crossing, day 0 = late October, Boathoos)
| Day | Event | Source |
|---|---|---|
| ~2–7 | (backfill) the latrine, "still in trousers"; Kallia's lidded pot | p36 |
| ~8–14 | (backfill) the swept-door broom borrowed and put back | p37 |
| ~29 | The climb (Ch.6) | ch-06 |
| ~30 | Shovel returned; first Greek to Kallia | p2–p7 |
| ~32 | The girl's clothes; Mara's own into the duffel | p8–p14 |
| ~32–35 | Walking, sitting and eyes lessons; the women's bath on a frosty morning | p15–p58 |
| S (~35) | Salt market; public silence begins | p63–p71 |
| S+~7 | The town loses interest; "they say you're simple" | p72–p73 |
| S+~15 | Valens at the gate for the fifth coin | p96 |
| S+~19 | Jar broken at the spring; that night, the Syracuse plan | p108, p130 |
| S+~20 | The council hall: registration; "Mara", the first word outside the gate "in nineteen days" | p141–p182 |
| S+~30 (~day 65, about the turn of the year) | "The last morning of the month": the midwinter invitation | p185–p193 |
| → | Ch.8: midwinter, AD 71 | outline:ch-08 |

### Knowledge database, Ch.7 entries
| Information | Origin | Knowers after Ch.7 |
|---|---|---|
| Mara's name | Mara to Sosandros at the council table (p158); before this only the goat-boy (ch-04:p33) and, unparsed, Valens in English (ch-06:p164) | Kallia, Sosandros, the clerk's boy, the line of householders; the spring as "Mera" (p183, off-page). **Valens: still no** |
| Mara's father's name, "Aimilios" | p163 | Kallia, Sosandros |
| Mara reads Greek | She reads the stylus upside down and recites the entry (p171, p178) | Kallia (sets up Ch.10) |
| Mara speaks Greek | p3 (Kallia); the salt row (p68) | Kallia, the market; the spring thinks her "simple" |
| The boat story | Valens's lie at the kiln (ch-06:p319), carried down with the charcoal | "The whole spring" (p139); Kallia adds Syracuse (p133) |
| "She's Kallia's" | Valens to the burner (ch-06:p315) | The salt-seller (p119) |
| Mara's "country" (pipes, hot water, women at work, cities paying for broken pots) | Mara to Kallia (p79–p87) | Kallia (disbelieves: "There's no such country") |
| Mara went to the cave | Gossip ("So the town says", p20); Mara herself (p6) | Kallia |
| The watch deal | (ch-06 lane) | Still Mara and Valens only |

### Plot threads
| Thread | Status after Ch.7 |
|---|---|
| Legal footing in Greece | **CLOSED for Part One:** free kinswoman under Kallia's keeping (Ch.16, Ch.18 depend on "never property") |
| The month of public silence | **CLOSED** (ends with the month; the name breaks it once, p158) |
| Son's room / the broom | OPEN → Ch.10 (shown twice in Ch.7; not again in Ch.8–9) |
| Letters from the east | OPEN → Ch.10 (not touched) |
| The watch in Valens's keeping | OPEN → Ch.11, Ch.18 |
| "Men will come asking" | OPEN, untouched → Ch.9 (notice) and Ch.12 |
| Nymph rumour | SPENT; not retold (W-05 removes the echo) |
| Midwinter rite / return to the cave | OPEN → Ch.8 (the closing question) |
| The fifth coin | Deferred ("a month without spitting"); close off-page (W-13) |

---

## SUGGESTED YAML PATCHES (for the entity-tracker UPDATE after the editor's fixes)

```yaml
suggested_patches:
  - entity: "post_patch_flags.P2"
    action: "remove_conflict"
    reason: "outline.md Ch.7 beat subversion now reads 'grateful to be written down as somebody's kin'; page agrees (ch-07:p146-p147, p172). One value."
  - entity: "contradictions.CH7-1"
    action: "create"
    value: { entity: "mara-reyes (the wound: father never took her)", plan: "foundation:§3 'never took her'; ch-01:p11, p150", prose: "ch-07:p140 'at fourteen, in a rented Fiat, with my father driving'", flag: "UNRESOLVED until C-01 is applied (Syracuse known from his slides)" }
  - entity: "contradictions.CH7-2"
    action: "create"
    value: { entity: "mara-reyes.traits (years at the bench)", plan: "ch-03:p2 'ten years in a basement lab' (mutable: false)", prose: "ch-07:p174 'fifteen years at a bench'", flag: "UNRESOLVED until W-02" }
  - entity: "contradictions.CH7-3"
    action: "create"
    value: { entity: "mara-reyes cover story (arrival)", plan: "ch-06:p69 last ship ~3 weeks after her arrival; ch-06:p317 'Since the olives'", prose: "ch-07:p135, p153 'the last boat'", flag: "UNRESOLVED until W-04" }
  - entity: "contradictions.CH7-4"
    action: "create"
    value: { entity: "locations.kallias-house (the shut room)", plan: "ch-07:p37 'at the end of the gallery, past the lodgers' rooms'", prose: "ch-07:p95 'at the top of the stair'", flag: "UNRESOLVED until W-16" }
  - entity: "mara-reyes.legal_status"
    action: "add"
    value: { fact: "registered on the Delphian tribute list: Maira, daughter of Aimilios, of Syrakousai; free; kinswoman of Kallia, of her house and in her keeping", chapter: 7, source: "ch-07:p172", note: "never property (ARCH-14; Ch.16, Ch.18)" }
  - entity: "mara-reyes.aliases"
    action: "add"
    value: ["Maira (as written by Sosandros)", "Mera (the Delphian say-so)", "Antigone (the salt-seller's, 2 uses)"]
  - entity: "mara-reyes.physical"
    action: "add"
    value: { vaccination_scar: "round, pitted, puckered in the middle, high on the left arm (ch-07:p48, p54; the obol ruler is dropped by W-20)", hair_relative: "lighter than a dark crimped hair (ch-07:p11)" }
  - entity: "kallia.knowledge"
    action: "add"
    value:
      - { fact: "Mara speaks Greek", learned: "ch-07:p3", method: "heard" }
      - { fact: "Mara's name (Mara/Maira) and her father's name (Aimilios)", learned: "ch-07:p158, p163", method: "witnessed (council table)" }
      - { fact: "Mara reads", learned: "ch-07:p178", method: "told_by:mara-reyes (recites the entry)" }
      - { fact: "Mara's account of her country (piped water, women at work)", learned: "ch-07:p79-p87", method: "told_by:mara-reyes", note: "disbelieved" }
  - entity: "kallia.relationships.husband's brother"
    action: "add"
    value: { name: "Aimilios (fictional, for the register)", of: "Syrakousai", source: "ch-07:p131, p163-p165", note: "cascade: Ch.10 must not contradict" }
  - entity: "sosandros"
    action: "create"
    reason: "named Ch.7 (ch-07:p142); = ch-05:p100 'thin man in the doorway' / p116 'the clerk'"
  - entity: "valens.physical"
    action: "add"
    value: { boots: "rawhide, laced to the shin, one lace broken and knotted", source: "ch-07:p96" }
  - entity: "objects.fathers-seiko-watch.custody"
    action: "add"
    value: { chapter: 7, holder: "valens", detail: "in his belt pouch (Mara's assumption); not seen; no clock time for Mara", source: "ch-07:p107" }
  - entity: "objects.kallias-ash-shovel"
    action: "update"
    value: { location_end_ch7: "the ash pail by the hearth", source: "ch-07:p7" }
  - entity: "objects.duffel.contents"
    action: "add"
    value: ["jeans, fleece, the shirt with the buttons (ch-07:p10)", "flashlight under them (ch-07:p10)", "toothbrush, purple, rubber grip (ch-07:p58)"]
  - entity: "objects.the-girls-himation"
    action: "create"
    value: { description: "heavy undyed-brown wool (fix C-02 wording), woven on an upright loom, starting border tight; one corner darned in browner wool; quince hair oil; slept under and worn", source: "ch-07:p10-p11, p183" }
  - entity: "meta.revalidation_needed"
    action: "add"
    value: { chapter: 6, issue: "chapter-6.md now 341 prose paragraphs; ch-06:pN cites from ~p102 on are +1", action: "re-anchor by content" }
  - entity: "character-bible.at-risk"
    action: "add"
    value: ["'the [color] of [thing]': CLOSED at 2 (Ch.1)", "the spitting-oak haggle: SPENT (Ch.6-7)", "Kallia's water order as a section close: 1 per chapter", "Mara's job statement: SPENT at four (Ch.3, 5, 6, 7)", "the breathings/pitch description of her Attic: SPENT", "a listener's comparison for her Greek: CLOSED", "'as broad as': SPENT", "the unprompted-memory close on 'nobody ever knew': SPENT", "the gray blamed for the pomegranate: SPENT"]
```

---

## Bottom line

Ch.7 delivers its plan cleanly: the essayistic claim, the comic lessons that curdle into the wax, and the relief on the step. The registration is legally exact and matches ARCH-14 and outline beat 2 in every word. The information flow around the name, which is the chapter's point, is airtight up to Kallia's one redundant question. The month of public silence matches the patched beat, and no one comes asking.

**Fix before finalize:**
- **C-01:** p140, Syracuse from the slides, not a trip with him.
- **C-02:** p10 and p151, retire the colour-of shape.

**Should fix (one clause each):**
- W-01, the month "that I could help"
- W-02, ten years
- W-03, "Say your name for me."
- W-04, one of the last boats
- W-05, Nereid
- W-06, the laugh runs its course
- W-07, the question she cannot answer by doing
- W-08, the glaze scoured to a fog
- W-09, the breathings
- W-10, the Syracusan in the stand
- W-11, the sample lifts
- W-12, the Dunphy close cut
- W-13, the lentils
- W-14, the p128 reorder
- W-15, Rome's governor
- W-16, the shut room upstairs
- W-17, "My work is pots…"
- W-18, the five indefinites
- W-20, "as broad as"

**Bookkeeping before the Ch.8 writer prompt:** W-19 (bible sync), the YAML patches above, and N-23 (Ch.6 re-anchor).
