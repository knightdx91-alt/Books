# Evaluation: FULL MANUSCRIPT (confirmation pass 3): *Sygl* (Ch.1–30, 90,359 words)
**Evaluator:** book-evaluator (independent) | **Date:** 2026-10-21 | **Mode:** book-level. I read all 30 chapters in full and in order, after the 15 required fixes from `eval-full-manuscript-2.md` §7 were applied. The book is judged on the author's own terms, as set out in STATE.yaml `decisions`: a light, warm tone; close third on Bal only, past tense; justified violence; "Master" only where the source has it; a happy ending; the provisional closing line; "beautiful women" kept as source wording; the expanded descriptions in Ch.2 and Ch.3 kept. No author ruling is penalized. Optional polish items P1–P5 were deliberately not applied and are not counted against the book.

## HEADLINE
**CVI-Launch:** 8.9 | **CVI-Legacy:** 6.3 | **Genesis Floor:** 8.5 | **Genesis Average:** 8.5 | **Casual:** 8.5
**Engagement Type:** Self-Insertion / wish-fulfilment (primary, ~55%), Empathy (secondary, ~35%), Fascination (tertiary, ~10%)
**Divergence Alert:** none (Launch minus Floor = 0.4).
**8.5 gate: PASS (Floor 8.5, Casual 8.5).**

All 15 fixes landed. Each was checked in place, in context, against the lines on either side of it. The two dimensions that held the floor at 8.0, **Prose & Voice** and **Pacing & Coherence**, both clear 8.5:
- The Winespring and Aleric contradictions are gone.
- The Ch.12 title line is now Bal's.
- The five fix-pass seams are closed.
- The Ch.17 ending now pulls the reader forward.

The fix pass created **two small new echoes**. Neither moves a score, but one breaks a standing project rule (STYLE_CONSTRAINTS §3, no new cross-chapter repeated phrase), so both are listed as **hygiene fixes to apply before packaging**. Together they cost +3 words.
1. **Ch.17's new last line ends "…was anybody's guess."** This repeats Ch.21 L139, "which of the red on it was strawberry was anybody's guess." The Ch.21 line is one of the better lines in the book, and it is the original.
2. **Ch.28's "He pushed himself upright, and not quietly."** This follows Ch.27 L119, "Bal pushed himself upright.", in the same wake-up-injured situation, in the next chapter.

**Mechanical gates** (run on a scratch copy laid out as `manuscript/chapters/`):
- `style_check.py`: clean (exit 0)
- `tic_report.py --gate`: clean. The busiest gesture class is object handling at 0.26/1k; kneel/crouch is 0.22/1k.
- `voice_wear_check.py`: clean (strict)
- `grammar_check.py`: clean

**Manual counts:**
- Em dashes 0. Joined quotes `." "` 0. No "sigil", "sygil" or "Waisura".
- "grey" appears only in the surname *Jazen Grey*.
- "Master" is used as address only at Ch.9 ×3 and Ch.28 ×1, plus Viridia's reported Ch.10 line, as ruled.
- 90,359 words.

---

## 1. Genesis Score (whole book)

| Dimension | Score | Evidence | Cap reasons / holds |
|-----------|-------|----------|-------------|
| Originality | **8.5** (=) | Meets the 8.5 unlock: the genre-standard beat is subverted three ways. (1) *Relocated weight:* the power-up weapon fails at the climax ("It was like whipping a river. The blood passed clean through the light", Ch.29), and the war is won by pushing blood into a life-bonded core. This pays off "*No inheritance gift,* Fern had read out of the file" (Ch.18 → Ch.29) and the vials thrown in the opening move. (2) *Refused payoff:* the heroine's poisoning is cancelled by a rune class planted in Ch.9 (the purification rune carved under the cup, Ch.25). (3) *Inverted actor:* the goddess is the boy's familiar, and she kneels to him twice (Ch.3, Ch.28). | The claiming/sorting frame and the harem shape are familiar, but that is normal for the lane and not a cap. |
| Theme | **8.5** (=) | "Being wanted for who you are" is shown, never argued: "*Amelia Norheart.*" (Ch.13–14); "I don't need you here for what you can do for me. I want you here because I like you." (Ch.16); the girls' free "Yes" (Ch.19). There is plenty of texture that doesn't serve the theme: the sock on the ceiling, the Terra boy's roll in the soup, Leon's unfinished goat story, the old man with his boots off at the Winespring. | none |
| Characters | **8.5** (=) | Cover-the-name passes for all four leads. Viridia needles ("Not looking at Bal? I'm a natural."). Lora hedges with people but is exact on her subjects ("Does either of you know a single thing about alchemy? No. You don't."). Amelia flips from play to menace ("Think your next words through, very carefully."). Bal answers marvels with a practical question ("Who washed the plates, if they went away on their own?"). Secondary characters get moments of their own: Verin ("He had no idea who had slept on his floor"), Mrs. Brown's minute-long story, Thad's stomach, Toma's "As I cared for my fellow priests." Chaos is 3–4/4 and inhabited in Ch.27 ("Nobody was there but him."). | **Fix 13 thinned the open-mouth class from 11 to 6** (Ch.2, 6, 8, 9, 14, 30), with no consecutive-chapter run left. "Honestly" is down from 29 to 26 (Ch.13 now ×2). That is a watch item already accepted in eval-2, not a cap. The 500-word cluster sweep finds no real cluster (§5). |
| Prose & Voice | **8.5** (↑0.5) | Underlined sentences: "Someone had bricked up a door in him while he was too small to know there was a door there at all." (Ch.2); "…it must have taken her a great deal longer than a minute to learn to tell it that short." (Ch.4, the stopping sentence); "Everyone's life could be spent except their own." (Ch.9); "Anyone who came in now would have taken him for stabbed." (Ch.14); "Nobody had written down the woman in the sling." (Ch.23); "In the dark it could have been anybody's hair." (Ch.26); "The wind shifted, and he smelled burnt horse." (Ch.27). Deliberately ugly sentences are present ("and he ate both and then he ate her last piece of toast", Ch.9; "It was a Tuesday, or it might have been a Thursday.", Ch.18). The voice changes under pressure: Ch.27 goes short and flat, and Ch.21 drops to "Something in Bal went very still." Pattern #11 is low (~0.3/1k). | **The +0.5 rests on 8 cited repairs:** Fix 1 (Ch.12 L85), Fixes 5–9 (Ch.24 L225 / L335, Ch.25 L141, Ch.27 L257, Ch.28 L89), Fix 11 (Ch.21 L85) and Fix 12 (Ch.13 L97 / Ch.14 L23). There is no misreadable line at any load-bearing moment. The two new echoes (H1, H2 below) are too small to hold the score down, but they break §3 and should go. Ch.27's "punched in the stomach" simile remains, as accepted polish (P4). |
| Pacing & Coherence | **8.5** (↑0.5) | **Zero internal contradictions found.** The briefing (Ch.22 L165), the arrival ("Nobody had given Viridia directions to the Winespring…", Ch.23 L143), the stable boy's line, and "That would be Amelia's letter, as Xavier had said…" (Ch.24 L7) now read as one consistent thread. Aleric's scar is described while the girls are in the room (Ch.22 L163), so "from what Xavier told us" (Ch.24 L273) holds. The turn-the-page rate is **≈86% (25/29)**: Ch.17 now ends on an open question that Ch.19 answers ("We heard what you told Amelia in the pass"). Chapter lengths range from 1,370 to 5,378 words; acceleration runs (Ch.16 bandits, Ch.27 bolts) alternate with deceleration runs (Ch.14, Ch.26). The timeline was checked: the poison's 24h + ~6h puts the priests' deaths at ~6 pm the day after lunch, and Ch.26 L69 and Ch.27 L65 agree. | The long middles of Ch.13 (shopping) and Ch.24 (warehouse and cask) remain. They are optional trims, already accepted, and the word floor argues against cutting them. |
| Emotion | **8.5** (=) | The anchors vary (see the Tomorrow Test). Emotional surprise: Amelia laughs until she weeps blood (Ch.21); the strawberries are carried back in the shirt Iro shredded; "I did want evidence. I'll accept you standing here." (Ch.30). Body rebel: the new fingers curl "hard enough that the nails bit into the sygl" (Ch.4); Viridia's knees give on the step (Ch.25); Viridia's still hair (Ch.26). | none |
| Source Fidelity (Dim 7) | **8.5** (=) | Beat order matches the source chapter for chapter, and every 2026-10-20/21 ruling is honoured. The Winespring set-up (option A) is now executed *and* reconciled. The Ch.23 directions line is connective tissue, not invented plot. | none |
| **FLOOR** | **8.5** | | |
| **AVERAGE** | **8.5** (59.5/7) | | Gap 0.0, so there is no single-dimension bottleneck. |

---

## 1b. Per-chapter table

| Ch | Words | Score | Note (weakest thing / what changed) |
|----|------:|:----:|---|
| 1 | 3,193 | 8.5 | The orphanage-history paragraph (L9) sits between two hooks. Harmless. |
| 2 | 3,163 | 8.5 | The expanded description (benches, Dracula engraving, the attic smell) reads as texture, not padding. L89/L91 still open "Bal wasn't sure…" / "Bal stayed…" back to back (accepted). |
| 3 | 2,928 | 8.5 | The expanded courtyard and softball detail work. The steps still stutter slightly (P1, not applied by choice). |
| 4 | 3,211 | 8.5 | Holds the stopping sentence of the book. |
| 5 | 3,604 | 8.5 | Ends on "four gods standing on it who expected her place to be empty again." |
| 6 | 3,051 | 8.5 | "That made sense, Bal thought. A lot of sense." (P2, not applied). |
| 7 | 3,652 | 8.5 | **Fix 13a landed:** "he froze on the threshold." Clean. "froze" appears 3× book-wide (Ch.4, 7, 13), spread out. |
| 8 | 2,261 | 8.5 | The best open-mouth beat in the book, and the only one in this run. |
| 9 | 3,444 | 8.5 | Porter "the color of the chalk." "as promised" (P3) is defensible, since Amelia did name the floor in Ch.7. |
| 10 | 2,776 | 8.5 | The bestiary block is the only exposition lump. |
| 11 | 3,618 | 8.5 | **Fix 13b landed:** the cover reveal now cuts straight to "You're reading her diary?", which is better than the old jaw-drop. |
| 12 | 1,370 | 8.5 (↑) | **Fix 1 landed:** `"I like you too," he said.` The line is unambiguous now, and her outburst follows logically. **Fix 14 landed:** one blush beat left in the window. |
| 13 | 5,378 | 8.5 | **Fix 12a** ("breakfast felt like yesterday") is literally true for Bal, who slept through breakfast. Fixes 15a–c landed; "honestly" is down to 2 here. |
| 14 | 2,395 | 9.0 | **Fix 12b landed** ("the meat rolls were miles behind him", a quiet pun on the uphill mile). The card scene and the blood-soaked shirt are the emotional summit of the first half. |
| 15 | 1,815 | 8.5 | **Fix 13c landed:** "the roll forgotten in her hand. Then she bit…" It reads naturally (she forgets the roll, then remembers it). Optional polish P6 below. |
| 16 | 4,630 | 8.5 | "her two hands were holding each other back." |
| 17 | 2,472 | 8.5 (↑) | **Fix 10 landed** and gives forward pull. **New echo:** "was anybody's guess" repeats Ch.21 L139 (H1). |
| 18 | 2,631 | 8.5 | none of note |
| 19 | 2,309 | 8.5 | **Fix 13d landed:** "Lora had forgotten to breathe." The payoff line for Ch.17 works. |
| 20 | 2,614 | 8.5 | Its whip mode (strike, wrap, fling) is distinct from Ch.21's. |
| 21 | 3,210 | 8.5 | **Fix 11 landed:** "Something in Bal went very still." It matches his bible card. |
| 22 | 3,407 | 8.5 | **Fixes 2a/2b landed.** The scar is now spoken while the girls are present (they came in at L157). |
| 23 | 2,090 | 8.5 (↑) | **Fix 3 landed.** The glance now questions *how she found it*, not *where they're going*. INVESTIGATE only (§4, Hostile): the question is never answered. That is acceptable as texture. |
| 24 | 4,762 | 8.5 (↑) | **Fixes 4, 5, 6 landed.** L7 now worries about *who else knows*; L225 `"About Lora's poison," he said. "Does it go in their drinks?"` flags the topic change; L335 reads "He was out of bed…". |
| 25 | 3,037 | 9.0 | **Fix 7 landed:** "held it upside down, left-handed. His other palm, the right, split open by itself." This keeps the dagger ruling (free hand) exactly. It is still the best chapter in the book. |
| 26 | 1,603 | 8.5 | The still hair. |
| 27 | 4,041 | 8.5 | **Fix 8 landed:** "From up there, the pair of them were killing his soldiers one bolt at a time." Clean. P4 (punched in the stomach) left by choice. |
| 28 | 2,615 | 8.5 | **Fix 9 landed:** "He pushed himself upright, and not quietly." The orphaned "This" is gone. **New echo** of Ch.27 L119 (H2). |
| 29 | 3,549 | 8.5 | The life-bond gloss is necessary exposition. |
| 30 | 1,530 | 8.5 | "those three beautiful women" is source wording, kept by author ruling. The closer lands. |

**Below 8.5: none.** Mean chapter score 8.53.

---

## 2. Verification of the 15 required fixes (eval-2 §7)

| # | Location | Landed? | Clean in context? | Note |
|---|---|---|---|---|
| 1 | Ch.12 L85 | Yes | Yes | Tagged; Viridia's "But you *said*…" now follows logically. |
| 2a | Ch.22 L81 | Yes | Yes | Scar removed from the girls-absent briefing. |
| 2b | Ch.22 L163 | Yes | Yes | Spoken with the girls at the table. "over the right eye" matches Ch.24 L273 and Ch.25 L83. |
| 3 | Ch.23 L143 | Yes | Yes | Reworded to the *how did she find it* angle. Consistent with Ch.22 L165. |
| 4 | Ch.24 L7 | Yes | Yes | "That would be Amelia's letter, as Xavier had said…" |
| 5 | Ch.24 L225 | Yes (reworded) | Yes | `"About Lora's poison," he said. "Does it go in their drinks?"` The next exchange (untagged "Why not poison the whole cask?") still reads as Bal's. |
| 6 | Ch.24 L335 | Yes | Yes | |
| 7 | Ch.25 L141 | Yes (reworded) | Yes | "left-handed." followed by "His other palm, the right" reads smoothly. |
| 8 | Ch.27 L257 | Yes | Yes | |
| 9 | Ch.28 L89 | Yes (reworded) | **Minor echo** | Repeats Ch.27 L119 "pushed himself upright". See H2. |
| 10 | Ch.17 L195 | Yes (reworded) | **Minor echo** | "…was anybody's guess." repeats Ch.21 L139. See H1. |
| 11 | Ch.21 L85 | Yes | Yes | |
| 12a/b | Ch.13 L97, Ch.14 L23 | Yes (reworded) | Yes | "hungry again" is now 1× in the book (Ch.13 L267, dialogue). |
| 13a–d | Ch.7, 11, 15, 19 | Yes | Yes | The open-mouth class is down to 6, with no run. |
| 14 | Ch.12 L91 | Yes | Yes | |
| 15a–c | Ch.13 | Yes | Yes | |

**No fix introduced a contradiction.** Two introduced a phrase echo; both are below.

---

## 3. Remaining fixes

### Hygiene: apply before packaging (project rule STYLE_CONSTRAINTS §3; not gate-blocking)

| # | Location | Problem type | What happens now | Why it fails | Replace with | Project rule? |
|---|---|---|---|---|---|---|
| H1 | Ch.17 L195 (last sentence) | Style (new cross-chapter repeat) | `Back in the pass the girls had been closer behind him than he'd thought, and how much of it they had heard was anybody's guess.` | "was anybody's guess" is already the payoff of a strong Ch.21 line ("which of the red on it was strawberry was anybody's guess"). Reusing it first, four chapters earlier, uses up the idiom before the better line arrives. | `Back in the pass the girls had been closer behind him than he'd thought, and he had no way of knowing how much of it they had heard.` (+3 words; "no way of knowing" occurs nowhere else in the book) | Yes: re-grep any reworded fix line against the whole book, not only the gate's n-gram list (the gate misses 2–3-word idioms) |
| H2 | Ch.28 L89 | Style (adjacent-chapter echo) | `He pushed himself upright, and not quietly.` | Ch.27 L119 is "Bal pushed himself upright." in the same waking-up-hurt situation, one chapter earlier. | `He got himself upright, and not quietly.` (0 words; "got himself upright" occurs nowhere else) | — |

### Optional polish (not needed for 8.5; author's call)
| # | Location | Now | Replace with |
|---|---|---|---|
| P6 | Ch.15 L47 | `Lora stopped, the roll forgotten in her hand. Then she bit and chewed and went on chewing.` | `Lora stopped, the roll forgotten in her hand. Then she remembered it, and bit, and went on chewing.` (+2 words; this makes the forget-then-resume sequence explicit. "halfway to her mouth" can't be used because Ch.1 has "the apple halfway to his mouth") |

P1–P5 from eval-2 stay as the author left them. They are not re-raised.

**After H1/H2:** re-run `style_check.py`, `tic_report.py --gate` and `voice_wear_check.py` on the scratch layout. The book will be 90,362 words.

---

## 4. Five-reader simulation

**The Devourer.**
- Hooked by the roof, the flicker and "something that could kill him".
- Ch.12–17 now read straight through: Ch.17 ends on "how much of it they had heard", and Ch.18 opens on a time-skip.
- **Likely put-downs:** the New Spring shopping middle (Ch.13) and James's warehouse (Ch.24). Both were accepted as optional trims.
- From "Get her a cup." onward, they read to the end in one sitting.

**The Critic.**
- Underlines the bricked-up door, the photograph, "Everyone's life could be spent except their own", the woman in the sling, the still hair and the burnt horse.
- With the open-mouth run thinned, finds no habit visible at reading speed.
- Might notice "anybody's guess" twice (H1).

**The Hostile.**
- **(1) Cleared:** the Winespring set-up. Briefing, arrival and inn now agree.
- **(2) Cleared:** the scar.
- **(3) Cleared:** "I like you too".
- **(4) New, minor:** "How *did* Viridia find the Winespring without directions?" (Ch.23 L143). It is never answered, but it costs nothing. It reads as Viridia being street-smart, and Lora's raised eyebrows invite exactly that reading. INVESTIGATE, no fix.
- **(5) Still standing, faithful to the source:** the whip comes "after only a few days of practice" (Ch.20). Leave it.

**The Casual Reader.**
- Buys after three pages: a likeable boy, a dangerous and funny goddess, a warm found family.
- Stays for Amelia and the card.
- Tells a friend about "the goddess who's his *familiar*" and "she drinks the poison and he's turned her cup into water".
- **Casual 8.5. No vibes problem.**

**The Devoted Reader (SFF, active).**
- Rewarded on re-read by the plants: the itching stump; the avoidance rune leading to the purification rune; the heart ring leading to Iro; "No inheritance gift" leading to Akora; Amelia's own diary; the blood elemental sent to her domain.
- The Ch.17 → Ch.19 "we heard" plant now pays off cleanly.

| Issue | Devourer | Critic | Hostile | Casual | Devoted | Severity |
|---|:-:|:-:|:-:|:-:|:-:|---|
| "anybody's guess" echo (H1) | | ✓ | | | ✓ | INVESTIGATE (rule hygiene) |
| "pushed himself upright" echo (H2) | | ✓ | | | | INVESTIGATE (rule hygiene) |
| Ch.23 unexplained directions | | | ✓ | | | INVESTIGATE (no fix) |
| Ch.13 / Ch.24 long middles | ✓ | | | | | INVESTIGATE (accepted, optional) |

Nothing is flagged by two or more of the four core readers.

---

## 5. Anti-AI scan and gesture / gloss checks

**Anti-AI (20 patterns), commercial thresholds.** Seven patterns are present, all at minor density (<0.5/1k):
- #3 rule of three ("gates, and a courtyard, and a stage", Ch.5)
- #6 "And" openers (~5)
- #10 described emotion ("She was afraid.", Ch.25)
- #11 explanatory extension (~0.3/1k)
- #12 binary negation ("Not hurt him. Kill him.", Ch.20)
- #13 precision ("Ten windows on the second story. Ten on the third.", Ch.24; nobody carries counting as a device)
- #16 philosophical aside (Ch.4, "worth getting caught for", earned)

Clear: #4 em dashes (0); #17 clean dialogue (there are interruptions and cross-talk, e.g. "That's not fair. You can't just…" / "Now," Amelia said over him, and the Ch.30 two-voice account); #18 echo chamber; #20 temperature report. **Clean band (0–8). No over-correction flag.**

**Explanatory-gloss rate:** ≈0.3 per 1k book-wide (e.g. Ch.10 L75, Ch.24 L197, Ch.28 L115, Ch.29 L47). That is under the 0.8 cap, so **Prose is not capped by #11.**

**Gesture clusters (3+ of one class within ~500 words).** The gate's classes are all clean. A scripted sweep of the classes the gate can't classify (laugh, smile, grin, blush, hug, glance, stare, kiss, shrug, sigh, eyebrow, squeeze, hand-taking) flagged six windows. On a judgement read, none is a real cluster:
- Ch.4 laugh: a single beat with the noun repeated ("Mrs. Brown laughed. It was a real laugh…").
- Ch.5 laugh: separate beats ~300 words apart.
- Ch.8 laugh: one is a remembered laugh.
- Ch.9 "hug": a false positive ("Huginn").
- Ch.12 smile: one beat ("smiled… a smile that was gone…", then Bal "smiled back").
- Ch.13 kiss: dialogue about the kissing rule.
- Ch.22 laugh: laughed / laugh (a recollection) / giggling, spread across three beats.

**Characters is not capped.**

---

## 6. Pacing, tension, residue

**Tension map (1–5):** 3 3 2 2 2 3 2 2 3 2 3 2 2 2 2 4 3 3 3 4 4 3 3 3 5 2 5 3 5 1
- **Midpoint spike:** Ch.16.
- **Peaks:** Ch.25, 27 and 29, with Ch.29 the highest.
- **Breath chapters:** Ch.26 and Ch.28, well placed.
- **Coda:** Ch.30, a deliberate drop.
- **Sag:** Ch.12–15 sits at tension 2 but carries emotional payload, so it is not dead.
- **Oscillations:** about 10 major swings, evenly spread.

**Turn-the-page:** ≈86% (25/29). Ch.17 has moved into the hooked column.

**Residue test (final chapter):** what lingers is contentment and safety: four on a couch "it was never built for", and due dates as the best thing Bal has thought about in days. That is an emotion, not an evaluation, and it matches the intended "unambiguously happy" ending. **PASS.** The provisional closer lands.

## Tomorrow Test
IMAGE anchors:
- the blood-soaked shirt and the card ("*Amelia Norheart*")
- strawberries in Iro's ruined shirt
- the rune under the cup
- the still hair in the dark
- the chalice
- the fork bouncing under the bench

QUOTE anchors:
- "They have made me a *myth*?"
- "Because it's magic."
- "No one threatens my girls."
- "Okay. You can keep her."

**Type: BOTH, 4+ anchors. ANCHOR EXISTS (+0.5 to CVI-Launch).**

**Shareability:** quote 3/5, plot 4/5, emotional 3/5. There are 3+ shareable moments.

## CVI-Launch breakdown
| Input | Score | Evidence |
|-------|-------|----------|
| Commercial Pacing | 8.5/10 | Short, varied chapters; hook rate ≈86%; strong final third |
| Tomorrow Test | 4+ anchors (image + quote) → 10 | above |
| Casual Reader | 8.5/10 | likeable Bal, magnetic Amelia, warm found family |
| Shareability (quote/plot/emotional) | 3/4/3 → **7.5** | MAX 8×0.6 + AVG 6.67×0.4 |
| Concept Pitch | yes (10) | "An orphan with no hand flies into a sealed temple and walks out with the Vampire Goddess as his *familiar*." |
| Human Closeness | yes (10) | most of the book is intimate conversation |

**CVI-Launch 8.9.** **CVI-Legacy 6.3** with default weights (Originality 8.5, Theme 8.5, Cultural Vocabulary 3, Re-readability 4, Identity 4). That fits the Cradle / HWFWM lane and is not a revision target.

---

## Strengths to PRESERVE
- The Ch.4 photograph.
- Porter "the color of the chalk".
- The card and the blood-soaked shirt.
- Lora crossing the silent hall.
- "her two hands were holding each other back".
- The strawberries.
- Amelia's blank "No." and "Damn their war."
- The rune under the cup, and Viridia's knees giving on the step.
- The still hair.
- The clear-sky boom and the two-day walk.
- Toma's real grief.
- The girls' two-voice account.
- The newly reconciled Winespring thread.

Do not let anyone "improve" Ch.9, 14 or 25.

## PATH TO 8.5
Not required: Genesis Floor is 8.5. To **hold** 8.5 through packaging:
- Apply H1 and H2 (3 words net).
- Re-run the gates.
- Before shipping any further reworded line, grep it against the whole book. Both new echoes came from rewording made to clear the n-gram gate, and both are 2–3-word idioms the gate does not track.

## VERDICT
**PASS.** Genesis Floor 8.5 / Average 8.5; Casual 8.5; CVI-Launch 8.9. All 15 required fixes from eval-2 landed cleanly and introduced no contradiction. Two minor phrase echoes (H1 Ch.17, H2 Ch.28) should be cleared for STYLE_CONSTRAINTS §3 compliance before packaging. They do not affect the gate. The word count stays ≥ 90,000.

BIAS CHECK: This evaluation was produced by the same system that wrote the prose. Confidence in scores above 8.0 requires external validation (beta readers, editors, comp analysis).
