# Evaluation: FULL MANUSCRIPT (pass 5, after the NA re-ruling): *Sygl* (Ch.1–30, 90,068 words)
**Evaluator:** book-evaluator (independent) | **Date:** 2026-10-21 | **Mode:** book-level.

**What I read.** STATE.yaml, the book's CLAUDE.md, character-bible.md (principal cards plus the secondary cast), project/STYLE_CONSTRAINTS.md and eval-full-manuscript-4.md. I then read all 30 chapters in full, in order. I checked the source (`Sygl_Complete.txt`) only for the age lines.

**How the book is judged.** On the author's own terms:
- Every STATE.yaml decision is binding.
- The 2026-10-21 NA ruling (every romantic lead 18+, fade-to-black) replaces the same-day YA ruling.
- Source-faithful choices are not penalized.

## HEADLINE
**CVI-Launch:** 8.9 (=) | **CVI-Legacy:** 6.3 (=) | **Genesis Floor:** 8.5 (= eval 4) | **Genesis Average:** 8.5 (=) | **Casual:** 8.5 (=)
**Engagement Type:** Self-Insertion / wish-fulfilment (~55%), Empathy (~35%), Fascination (~10%)
**Divergence Alert:** none.

**8.5 gate: PASS (Floor 8.5, Casual 8.5), with 3 required age fixes (A1–A3).**
- **A1** is the serious one. Lora's own arithmetic in Ch.13 makes her **fifteen**: she was "a girl of thirteen" at the tournament, and she says "That's been my life for the last two years." That is a romantic lead under 18 in an NA harem book. It breaks the author's NA ruling, so it is filed under Dimension 7 the way eval 4 filed Y1.
- **A2** fixes a direct contradiction about Amelia's apparent age.
- **A3** fixes a line the aging left stranded.

Four NA-fit swaps (N1–N4) and one optional swap (N5) are recommended.

All fixes were applied to a scratch copy (`manuscript/chapters/` layout) and run through every gate:
- Required only: **90,079 words**. Required + recommended + optional: **90,082 words**. Both are ≥ 90,000.
- `style_check`, `grammar_check`, `tic_report --gate` and `voice_wear_check` (strict) are all clean.
- My first wording of A2 ("a good deal older") made "a good deal" a 3x book-wide phrase and failed `tic_report --gate`. It was reworded to "far older". Only the final strings appear below.

**Eval 4 fixes verified in place:**
- R1: Ch.14 "The card propped beside it in the window".
- R2: Ch.27 "Bal managed to roll his head toward the canyon".
- R3: Ch.20 "ask Amelia about this new temper".
- R4: Ch.14 "Bal had seen her nervous only once before, in the doorway at Verin's cottage".
- R5: Ch.2 "and she arched".
- Y1: Ch.24 "Bal turned to the window before the dress came down".
- Y2 and Y3 were not applied. Under the NA ruling they are **withdrawn**. Ch.3's "Time for that later" and Ch.19's "Then let's go to bed" are ordinary closed-door NA.

**The author's age edits hold:**
- Ch.3 "for eighteen years"
- Ch.5 "In eighteen years"
- Ch.8 "Eighteen." / "Same as you." / "the same as she had said eighteen" / "Eighteen, alone on a road" / "For eighteen years"
- Ch.11 "only eighteen… an eighteen-year-old" and "He had been six, twelve years ago."

Each reads naturally in context. The arithmetic is right: Peter's twelve years, against an eighteen-year-old Bal, puts Bal at six.

**Mechanical gates on the current text** (before fixes): `style_check` clean, `grammar_check` clean, `tic_report --gate` clean, `voice_wear_check` (strict) clean.

**Manual counts:**
- Em dashes: 0. No "sigil", "sygil" or "Waisura".
- "Master" as address: 4 (Ch.9 ×3, Ch.28 ×1), plus Viridia's reported use in Ch.10. This is as ruled.

---

## 1. AGE AUDIT (required)

### 1a. Hits that need a fix

| # | Ch / line | Current text | Problem | Replacement | Δw | Status |
|---|---|---|---|---|---|---|
| **A1** | **Ch.13 L241** (Lora, bookstore) | `That's been my life for the last two years.` | L231 says she won the tournament as "a girl of thirteen", and L241 counts "the last two years" since then. **Lora is 15.** This is the only place in the book that fixes her age, so it is the only way a reader can work it out, and it puts a romantic lead under 18. The source has the same arithmetic ("last two years"), but it was never aged up. | `That's been my life for the last five years.` (13 + 5 = 18, the same as Bal) | 0 | **REQUIRED** |
| **A2** | **Ch.2 L9** (first sight of Amelia) | `Bal guessed she was a few years older than he was.` | Ch.8 L101–103 now says she was turned at "Eighteen." / "Same as you." A vampire turned at eighteen does not look "a few years older" than an eighteen-year-old. This contradicts the new canon directly, and the Hostile reader catches it on page 3 versus page 60. | `Bal guessed she was about his own age, though she carried herself like someone far older.` This keeps the source's impression of age as bearing, and it sets up Ch.3's "For once, she looked no older than Bal" as a payoff. | +5 | **REQUIRED** |
| **A3** | **Ch.11 L85** (Peter's story) | `Sixteen. The red mark on Bal's palm seemed to sit up and want attention.` | This was written when Bal was sixteen: Peter's age was Bal's age, and that is why the palm "sits up". With Bal at eighteen the echo has lost its reason. The fragment "Sixteen." now reads as if the narration were stating Bal's age, which undercuts the NA ruling three paragraphs before "I'm only eighteen". | `Sixteen, and cast off for the very mark on Bal's own palm. It seemed to sit up and want attention.` The resonance is now the mark, not the age. "Thrown out" and "shunned" were avoided because L83 already uses both. | +6 | **REQUIRED** |
| N1 | Ch.3 L101 | `She looked like a young girl who had been cooped up` | "Young girl" is the source's phrase, and it falls a page after the stretch and "Time for that later". In an NA harem book, an apparent-age description of a lead should not say "young girl". | `She looked like someone who had been cooped up` | −2 | recommended |
| N2 | Ch.2 L199 | `like a girl half her apparent age.` | Half of eighteen is nine. It is a childish image, and it sits in the moment she sits knee-to-knee with him. | `like a girl let out of lessons early.` | +1 | recommended |
| N3 | Ch.8 L171 | `Grown-ups with red marks in their palms` | "Grown-ups" is a child's word for adults. It makes an eighteen-year-old narrator sound about twelve. | `Grown men and women with red marks in their palms` | +3 | recommended |
| N5 | Ch.18 L5 | `A younger student he had never spoken to` | Bal is a first year, and the castle has no students younger than first years. "Younger" therefore implies either an under-18 student or a younger Bal. | `A Waves first year he had never spoken to` | +1 | optional |

**Continuity hygiene found in the sweep (not age-related):**

| # | Ch / line | Current | Problem | Replacement | Δw |
|---|---|---|---|---|---|
| N4 | Ch.7 L263 | `A Waves boy at the next table over` | Ch.20 L13 says "The Tempus students ate at the table beside Bal's own". Ch.12 L91 also has "the Waves boy two tables down". Ch.7 is the outlier. | `A Tempus boy at the next table over` (this also sharpens the beat, because Viridia is a Tempus) | 0 |

### 1b. Swept and cleared (no change)

**Bal (18):**
- Ch.3 L11, Ch.5 L39, Ch.8 L139 ("eighteen years").
- Ch.11 L97 ("He had been six, twelve years ago"). This is correct.
- Ch.11 L121.
- "kid" applied to him: Ch.11 L181 "a kid in a school sweater". This is the view of two priests in their twenties, so it reads as relative age, not as a minor. Keep.
- Past-tense childhood: Ch.5 L95 "a curious kid", Ch.20 L135 "as a kid", Ch.17 L141 "as a boy". These are about his childhood, not his present. Keep.

**Amelia (turned at 18):**
- Ch.8 L101–117 is consistent once A2 is applied.
- Ch.3 L101 "For once, she looked no older than Bal" now pays off A2.
- "thousands / three thousand years" is consistent throughout.

**Viridia (a little older than Bal):**
- Ch.6 L9 "a girl a bit older than either of them" (the source said "around sixteen"; this was correctly aged).
- Ch.7 L115 "a little taller".
- Ch.27 L27 "Bran. He was two at the time" makes Bran two years older.
- Ch.27 L41 "Another six months and we'd have been married" is read with Ch.13 L215 ("Then I got my Tempus sygl… set free").

Her age is never stated. One risk: Ch.1 L19 says sygls come "sometime in childhood". A reader who joins the two could imagine a child engagement six months from marriage. Ch.4 L107 (late affinities) and Ch.11 L83 (Peter's sygl at sixteen) establish that late sygls exist, and the bookstore context reads as recent. **No hit.** If the author wants it airtight, a single clause in Ch.27 saying her sygl came the spring before school would settle it. That adds a fact, so it is the author's call. I have not supplied or gate-tested a string for it.

**Lora:**
- **Never stated.** Her age is implied only by Ch.13's arithmetic (fixed by A1) and by her being a first year with Bal (Ch.10, cohort "around Bal's age", Ch.6 L9).
- Ch.16 L53 "After the tournament" and Ch.10 L139 are clean.
- The character-bible line "two years of training by day and reading by night" carries the same error. **Update the bible to "five years" when A1 is applied.**

**Cohort and school-entry age:**
- Ch.4 L25 ("We had three boys and two girls leave a few days ago"): orphans leave at the intake.
- Ch.4 L93 / Ch.5 L177 "first years".
- Ch.13 L449 "All the other Lead Mages are fourth years".
- Ch.20 L15 (Sean "older than the three of them, a fourth year").
- Ch.22 L7 ("A soldier who could have been in Bal's year").

The intake is about 18–19 and is consistent.

**Fredrick:** "a year older" (Ch.1 L51), and he left a month ago for his own first year (L49, L59 "the kids who'll be in my year"). At 19 he is inside the same 18–19 intake band that Viridia shows. Consistent. "Kids" there is colloquial.

**The orphanage:** an eighteen-year-old still in a twenty-boy dormitory (Ch.7 L63) fits Ch.4's "leave at the intake". Comics and a jar of marbles (Ch.4 L145) are what an orphan owns, not a sign of age. Keep.

**Timeline:** Ch.28 L153 "barely two months" matches 3 days + one week + six weeks + the Londra trip.

**Others:**
- Peter: sixteen (Ch.11), not a lead, source age kept as ruled.
- The children with blood sygls (Ch.23) are actual children, which is correct.
- Iro's "face had gone young" (Ch.21) is not a lead.

**Romance under the NA ruling:**
- Kisses: Ch.14, 15, 19, 24.
- Shared beds: Ch.13 opening, Ch.14 close, Ch.19 → 20, Ch.24/25, Ch.30.
- Ch.24 window turn (Y1).

All of these are closed-door and fine for NA. With A1 applied, every person in a romantic beat is 18 or older.

**Bible updates to make alongside the fixes** (not edited by me):
- Amelia card, "looks a few years older than Bal" → "looks about Bal's age; carries herself older".
- Lora card, "two years of training" → "five years".

---

## 2. NA FIT

**Verdict: it reads as NA, closed-door (clean) NA academy-harem fantasy, once A1–A3 are in.** The NA markers are real:
- an 18-year-old lead who leaves an institution for adult life;
- command of an army and decisions about who dies (Ch.18 "We will not respond in kind", Ch.22);
- killing that is justified and not agonized over (Iro, Ch.21);
- an openly multi-partner relationship negotiated aloud (the juggling talk, Ch.17; "We heard what you told Amelia in the pass", Ch.19);
- shared beds that fade to black;
- narration that calls the leads women at the mature beats: "One beautiful woman who wanted to be with him" (Ch.23), "those three beautiful women" (Ch.30).

**Where it still skews younger** is register, not content. The plain, wholesome voice and the school-life stakes (curfew, demerits, homework, the "No kissing" rule, Ch.13) sit at the YA/NA crossover. That is the Cradle / HWFWM lane, and the market accepts it as clean NA.

To firm up the NA read **without adding sexual content or changing story**:
1. **Apply A1–A3.** A1 is non-negotiable for an NA harem listing. Retailers and readers in this subgenre check lead ages, and Ch.13's "thirteen… last two years" is exactly the sum a hostile reviewer does.
2. **Apply N1–N3.** They remove the three phrases that make an 18-year-old cast read child-sized: "young girl", "half her apparent age", "Grown-ups".
3. **Packaging, not prose:** put "All characters are 18+" in the front-matter or content note, and tag the book clean / closed-door NA. This is standard in harem fantasy, and it protects the listing at no cost to the text.
4. Leave Y2/Y3 unapplied. Ch.3's "Time for that later" and Ch.19's "Then let's go to bed" are on-genre closed-door NA beats.

---

## 3. Genesis Score (whole book)

| Dimension | Score | Evidence | Cap reasons / holds |
|---|---|---|---|
| Originality | **8.5** (=) | The inverted actor: the goddess is the boy's familiar and kneels to him (Ch.3, Ch.28). Relocated weight at the climax: "It was like whipping a river." (Ch.29), and the war is won by pushing blood into a life-bonded core, which pays off "*No inheritance gift,* Fern had read out of the file." A refused payoff: the poison is turned to water by a rune cut under the cup (Ch.25), which Ch.9's runes class planted. | none |
| Theme | **8.5** (=) | "Being wanted for who you are" is shown, not argued: "*Amelia Norheart.*" (Ch.13–14); "I don't need you here for what you can do for me. I want you here because I like you." (Ch.16); the girls' free "Yes" (Ch.19). There is plenty of non-thematic texture: the bread roll in the soup (Ch.12), the milk cup that fills from the bottom (Ch.15), Leon's goat story (Ch.25), "who washed them remained an open question" (Ch.30). | none |
| Characters | **8.5** (=) | Cover-the-name passes for all four leads. Lora: "Does either of you know a single thing about alchemy? No. You don't." Viridia: "Not looking at Bal? I'm a natural." Amelia: "Think your next words through, very carefully." Bal: "Who washed the plates, if they went away on their own?" Secondary characters have their own moments: Mrs. Brown's photograph, Thad's stomach, Toma's "As I cared for my fellow priests". Inhabited chaos in Ch.27: "Nobody was there but him." | **Gesture clusters:** the gate is clean (busiest class is object handling at 0.24/1k). My sweep of the untracked classes finds 3+ in 500 words only at Ch.4 laugh (Mrs. Brown's one laugh, named four times in one beat), Ch.5 laugh, Ch.12 smile and Ch.22 laugh. These are the same windows eval 4 judged single or spread beats. **No cap.** No verbal tics; "Master" is as ruled. A2 is a continuity fact, not a character failure. |
| Prose & Voice | **8.5** (=) | Underlined: "Someone had bricked up a door in him while he was too small to know there was a door there at all." (Ch.2); "…it must have taken her a great deal longer than a minute to learn to tell it that short." (Ch.4, the stopping sentence); "Everyone's life could be spent except their own." (Ch.9); "Nobody had written down the woman in the sling." (Ch.23); "In the dark it could have been anybody's hair." (Ch.26). Deliberately rough: "he ate both and then he ate her last piece of toast" (Ch.9); "It was a Tuesday, or it might have been a Thursday." (Ch.18). The voice changes under pressure, going short and flat in Ch.27. **Explanatory-gloss rate ≈0.3/1k**, under the 0.8 cap. | Held. A3's stranded "Sixteen." is a seam the re-age created. It is one line and does not move the dimension, but it must go. |
| Pacing & Coherence | **8.5** (=) | The turn-the-page rate is unchanged at ≈86%; no chapter opening or ending was touched by the age edits. The poison clock holds (24h + 6h lands at Ch.27's "close to six"). The Winespring thread holds (Ch.22 → Ch.24). | A2 is a real internal contradiction (Ch.2 vs Ch.8), and N4 is a small seating slip (Ch.7 vs Ch.20). Both are one-liners. |
| Emotion | **8.5** (=) | Varied anchors: the card and the blood-soaked shirt; strawberries in Iro's shirt; the pulse in Viridia's throat; the still hair. Emotional surprise: Amelia laughs until she weeps blood (Ch.21). Body rebel: "the nails bit into the sygl" (Ch.4); Viridia's knees giving on the step (Ch.25). | none |
| Source Fidelity & Author Rulings (Dim 7) | **8.5** (=) **once A1 is applied** | Beat order matches the source. Every 2026-10-20/21 decision is honoured, including the new closing line, Toma to the Heir's School, the blue cloth, the vials at the core, and the two-voice account. | **A1 breaks the NA ruling ("every romantic lead 18+").** Like Y1 in eval 4, it is required to hold 8.5. A2 and A3 are also consequences of the same ruling and are fixed under it. |
| **FLOOR** | **8.5** | | |
| **AVERAGE** | **8.5** (59.5/7) | | Gap 0.0 |

---

## 4. Per-chapter table (vs eval 4)

| Ch | Words | Eval 4 | Eval 5 | Note |
|---|---:|:-:|:-:|---|
| 1 | 3,185 | 8.5 | 8.5 | Age-clean. Fredrick "a year older" is consistent with the intake. |
| 2 | 3,138 | 8.5 | 8.5 | R5 in. **A2** (required); N2 (recommended). |
| 3 | 2,913 | 8.5 | 8.5 | "eighteen years" reads well. N1 (recommended). Y2 withdrawn under NA. |
| 4 | 3,193 | 8.5 | 8.5 | Stopping sentence intact. |
| 5 | 3,590 | 8.5 | 8.5 | "In eighteen years… a first name": the age edit lands as comedy. |
| 6 | 3,043 | 8.5 | 8.5 | "a girl a bit older" is correctly aged from the source. |
| 7 | 3,641 | 8.5 | 8.5 | N4 seating slip. |
| 8 | 2,257 | 8.5 | 8.5 | "Eighteen." / "Same as you." works. N3 (recommended). |
| 9 | 3,447 | 8.5 | 8.5 | untouched |
| 10 | 2,780 | 8.5 | 8.5 | |
| 11 | 3,609 | 8.5 | 8.5 | "only eighteen" and "six, twelve years ago" are correct. **A3** (required). |
| 12 | 1,370 | 8.5 | 8.5 | |
| 13 | 5,372 | 8.5 | **8.5 craft / NA ruling: FAIL until A1** | Lora = 15 by her own arithmetic. |
| 14 | 2,387 | 9.0 (after R1/R4) | 9.0 | R1 and R4 in. The card scene is untouched. |
| 15 | 1,814 | 8.5 | 8.5 | |
| 16 | 4,614 | 8.5 | 8.5 | |
| 17 | 2,443 | 8.5 | 8.5 | |
| 18 | 2,626 | 8.5 | 8.5 | N5 (optional). |
| 19 | 2,294 | 8.5 | 8.5 | Closed-door ending suits NA. |
| 20 | 2,613 | 8.5 | 8.5 | R3 in. Y3 withdrawn. |
| 21 | 3,203 | 8.5 | 8.5 | |
| 22 | 3,387 | 8.5 | 8.5 | |
| 23 | 2,079 | 8.5 | 8.5 | "One beautiful woman" is a good NA register. |
| 24 | 4,728 | 8.5 craft / YA FAIL | 8.5 | Y1 in. Reads cleanly as NA. |
| 25 | 3,030 | 9.0 | 9.0 | |
| 26 | 1,599 | 8.5 | 8.5 | |
| 27 | 4,031 | 8.5 | 8.5 | R2 in. Viridia/Bran age cleared (see 1b). |
| 28 | 2,606 | 8.5 | 8.5 | |
| 29 | 3,536 | 8.5 | 8.5 | |
| 30 | 1,540 | 8.5 | 8.5 | The close holds. |

**Below 8.5: none on craft.** One chapter (Ch.13) fails the author's NA ruling until A1 is applied. Mean 8.53.

---

## 5. REQUIRED FIXES (apply exactly; gate-verified on a scratch copy)

| # | Location | Type | Replace | With | Δw |
|---|---|---|---|---|---|
| **A1** | Ch.13 L241 | NA ruling (lead under 18) | `That's been my life for the last two years.` | `That's been my life for the last five years.` | 0 |
| **A2** | Ch.2 L9 | Continuity (vs Ch.8 "Eighteen." / "Same as you.") | `Bal guessed she was a few years older than he was.` | `Bal guessed she was about his own age, though she carried herself like someone far older.` | +5 |
| **A3** | Ch.11 L85 | Connective (stranded age echo) | `Sixteen. The red mark on Bal's palm seemed to sit up and want attention.` | `Sixteen, and cast off for the very mark on Bal's own palm. It seemed to sit up and want attention.` | +6 |

### Recommended (NA fit / continuity)

| # | Location | Replace | With | Δw |
|---|---|---|---|---|
| N1 | Ch.3 L101 | `She looked like a young girl who had been cooped up` | `She looked like someone who had been cooped up` | −2 |
| N2 | Ch.2 L199 | `like a girl half her apparent age.` | `like a girl let out of lessons early.` | +1 |
| N3 | Ch.8 L171 | `Grown-ups with red marks in their palms` | `Grown men and women with red marks in their palms` | +3 |
| N4 | Ch.7 L263 | `A Waves boy at the next table over` | `A Tempus boy at the next table over` | 0 |
| N5 (optional) | Ch.18 L5 | `A younger student he had never spoken to` | `A Waves first year he had never spoken to` | +1 |

**Totals (verified with `wc -w`):**
- A1–A3: **90,079**.
- A1–A3 + N1–N5: **90,082**.

Both are at or above 90,000. With every fix applied, `style_check`, `grammar_check`, `tic_report --gate` and `voice_wear_check` (strict) are all clean. With A1–A3 alone they are also clean. The two bible cards (Amelia's apparent age, Lora's "two years") should be updated in the same pass.

---

## 6. Anti-AI scan (20 patterns), commercial thresholds

**7/20, all minor (<0.5/1k), unchanged.** The book is in the clean band.

Patterns present:
- #3 rule of three ("gates, and a courtyard, and a stage", Ch.5)
- #6 "And" openers (~5)
- #10 described emotion, residual ("Nervous was new.")
- #11 explanatory extension (≈0.3/1k)
- #12 binary negation ("Not hurt him. Kill him.", Ch.20)
- #13 precision ("Ten windows on the second story. Ten on the third.", Ch.24). It is not a device.
- #16 aside ("worth getting caught for", Ch.4)

Clear: #4 (0 em dashes), #17 (cross-talk in Ch.4 "Now," Amelia said over him; Ch.30's two-voice account), #18, #20. No over-correction flag. **Gloss rate is under the 0.8 cap, and no gesture cluster triggers the 7.5 cap.**

## 7. Reader simulation

- **Devourer.** Unchanged. The pull is Ch.21 onward, and the middle (Ch.13, Ch.24) is long but busy. The age edits are invisible at speed.
- **Critic.** Underlines the same sentences as eval 4. Flags "Sixteen." in Ch.11 as a sentence that has lost its reason (A3). Flags "a young girl" and "half her apparent age" in a harem book (N1, N2).
- **Hostile.**
  - Does the sum: "a girl of thirteen" plus "the last two years" makes Lora 15 (A1).
  - Catches Amelia "a few years older" in Ch.2 against "Eighteen. Same as you." in Ch.8 (A2).
  - Still asks how Viridia found the Winespring without directions (Ch.23). That is texture only and was cleared in eval 4.
- **Casual.** Buys after three pages: a likeable orphan, a funny and dangerous goddess, the familiar twist. Tells a friend "the goddess is *his* familiar" and "he turned the poison into water with a rune." **Casual 8.5. No vibes problem.** The one thing that would sour a harem-genre buyer is a lead who turns out to be 15. A1 removes it.
- **Devoted (SFF).** The plants still pay off: avoidance rune → purification rune; heart ring → Iro; "No inheritance gift" → Akora; Amelia's own diary (open thread). A Devoted reader would also do the Ch.13 sum, which is one more reason A1 is required.

| Issue | Devourer | Critic | Hostile | Casual | Severity |
|---|:-:|:-:|:-:|:-:|---|
| A1 Lora = 15 (NA ruling) | | ✓ | ✓ | ✓ | **IMPORTANT** (market and legal perception) |
| A2 Amelia's apparent age contradiction | | ✓ | ✓ | | SHOULD FIX |
| A3 stranded "Sixteen." | | ✓ | | | INVESTIGATE (fix anyway; a seam) |
| N1–N3 child-sized phrasing | | ✓ | | ✓ | SHOULD FIX (NA fit) |
| N4 seating slip | | | ✓ | | INVESTIGATE |

## 8. Tomorrow Test, residue, CVI

- **Tomorrow Test:** ANCHOR EXISTS, with both types and 4+ anchors.
  - IMAGE anchors: the blood-soaked shirt and the card ("*Amelia Norheart*"); strawberries in Iro's shirt; the rune under the cup; the still hair in the dark; the chalice.
  - QUOTE anchors: "They have made me a *myth*?", "Because it's magic.", "No one threatens my girls.", "Okay. You can keep her."
- **Residue (Ch.30):** contentment and safety. Four on a couch "it was never built for", due dates as the best thing he has thought about in days, and then "For the first time in his life, Bal was exactly where he belonged." It is an emotion, not an evaluation. **PASS.**
- **Shareability:** quote 3, plot 4, emotional 3, which gives 7.5.
- **CVI-Launch: 8.9.** Commercial pacing 8.5, Tomorrow 10, Casual 8.5, Shareability 7.5, Pitch 10, Closeness 10. The correct NA shelving and an "all characters 18+" note keep it there; A1 is what makes that shelving safe.
- **CVI-Legacy: 6.3.** This fits the Cradle / HWFWM lane and is not a revision target.

## Strengths to PRESERVE
- The Ch.4 photograph.
- Porter "the color of the chalk".
- The card and the soaked shirt.
- Lora's walk down the hall.
- "her two hands were holding each other back".
- The strawberries.
- Amelia's flat "No." and "Damn their war."
- The rune under the cup and the pulse in Viridia's throat.
- The still hair.
- The clear-sky boom.
- Toma's real grief.
- The two-voice account.
- The cozy Ch.30 close.
- The new "In eighteen years it had not occurred to him that Mrs. Brown had a first name." It is the best of the age edits.

Do not let further passes touch Ch.9, the card beat in Ch.14, or Ch.25.

## PATH TO 8.5
Not required; the Genesis Floor is 8.5. To **hold** it through packaging:
1. Apply A1–A3, and preferably N1–N4.
2. Update the two bible cards.
3. Re-run the four gates on the scratch `manuscript/chapters/` layout.

Process lesson from this pass: **an age change is a search-and-reason job, not a search-and-replace job.** The author's edits changed every explicit "sixteen" correctly. The three hits that remain are all *inferred* ages:
- a sum across two sentences (A1);
- an apparent-age description that the new number contradicts (A2);
- a resonance that only worked at the old number (A3).

`grep sixteen` cannot find any of them.

## VERDICT
**PASS.** Genesis Floor 8.5 / Average 8.5 / Casual 8.5, the same as eval 4, and no chapter is below 8.5 on craft.

**NA ruling:** **not yet met** until **A1** (Ch.13, Lora's "last two years" → "last five years") is applied. With A1–A3 in, every romantic lead is 18 or older, and nothing on the page states or implies otherwise.

**NA fit:** the book reads as clean / closed-door NA academy-harem fantasy. N1–N3 and an "all characters 18+" note firm that up.

Totals: 90,079 words with the required fixes, 90,082 with all of them, and all gates clean.

BIAS CHECK: This evaluation was produced by the same system that wrote the prose. Confidence in scores above 8.0 requires external validation (beta readers, editors, comp analysis).
