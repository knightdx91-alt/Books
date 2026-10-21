# Evaluation: FULL MANUSCRIPT (pass 4, after the YA ruling and the book-wide line edit): *Sygl* (Ch.1–30, 90,080 words)
**Evaluator:** book-evaluator (independent) | **Date:** 2026-10-21 | **Mode:** book-level. I read all 30 chapters in full and in order, plus STATE.yaml, the book's CLAUDE.md, character-bible.md, STYLE_CONSTRAINTS.md, eval-full-manuscript-3.md and the three line-edit logs.

The book is judged on the author's own terms:
- Every STATE.yaml `decision` is binding.
- The 2026-10-21 YA (upper YA) ruling applies.
- Grok's structural advice was declined by the author, and none of it is counted against the book: cutting school chapters, longer/costlier conversions, earlier Raizen scenes, an epilogue, less help from Amelia.
- Source-faithful choices are not penalized, such as "beautiful women", "Master" kept rare, and the whip after "a few days".

## HEADLINE
**CVI-Launch:** 8.9 (=) | **CVI-Legacy:** 6.3 (=) | **Genesis Floor:** 8.5 (= eval 3) | **Genesis Average:** 8.5 (=) | **Casual:** 8.5 (=)
**Engagement Type:** Self-Insertion / wish-fulfilment (~55%), Empathy (~35%), Fascination (~10%)
**Divergence Alert:** none.
**8.5 gate: PASS (Floor 8.5, Casual 8.5).** It comes with **5 required hygiene fixes** (R1–R5), which correct two seams the line edit introduced, one weakened antecedent, one older contradiction and one grammar slip. It also comes with **1 required YA fix** (Y1, Ch.24). Without Y1 the book does not meet the author's own "nothing suggestive" YA ruling. Two more YA fixes (Y2 Ch.3, Y3 Ch.20) are recommended and left to the author.

All fixes below were applied to a scratch copy and run through every gate. The result is 90,086 words, and `style_check`, `grammar_check`, `tic_report --gate` and `voice_wear_check` (strict) are all clean. Two of my own first-draft replacement strings had tripped the gate ("the night before", "here she said", "bal turned his", "than it had ever", "there might be", "all three of them"). Those strings were reworded until the gate was clean. Only the final strings appear below.

**Mechanical gates on the current text** (scratch `manuscript/chapters/` layout):
- `style_check.py`: clean
- `grammar_check.py`: clean
- `tic_report.py --gate`: clean. The busiest gesture class is object handling at 0.24/1k; kneel/crouch is 0.22/1k.
- `voice_wear_check.py`: clean (strict)

**Manual counts:**
- Em dashes 0. No "sigil", "sygil" or "Waisura".
- "Master" as address 4: Ch.9 ×3 and Ch.28 ×1, as ruled.
- "the way [x]" similes 2 book-wide.
- Eval 3's hygiene fixes H1 (Ch.17 "no way of knowing") and H2 (Ch.28 "got himself upright") are both in place.

---

## 1. Did the line edit hold? (138 edits verified in context)

On balance the line edit **improved** the book. Most of the 138 edits are invisible at reading speed, which is what a line edit should be. These are the best replacements, and each is better than what it replaced:

| Ch | New line | Why it works |
|---|---|---|
| 25 | "The pulse was going in her throat, as plain as the scar on Aleric's face." | Replaces "She was afraid." |
| 29 | "Amelia was shining, up on her bare toes in the sand" | Replaces "so happy it was coming off her in waves" |
| 28 | "He kept hold of the door, as if he might yet back out." | |
| 22 | "the corners of her mouth kept giving her away" | |
| 9 | "The oatmeal sat heavy in his stomach." | It ties back to the breakfast that opened the chapter. |
| 8 | The hand now lies "on her knee, where she had left it" | This is the factual fix, and it is now correct. |
| 3 | "She didn't so much as blush." | It sets up Ch.5's "Amelia blushed. Bal hadn't known she could." |

**Seams, lost antecedents and close repeats the line edit introduced (3):**

| # | Location | What happened | Severity |
|---|---|---|---|
| R1 | Ch.14 L119 | The expository-dialogue trim left **"the card in the shop" twice in consecutive sentences**: `"But going by the card in the shop, it should be plenty powerful." The card in the shop, he explained, had promised…`. It sits in the book's emotional summit chapter, and "card" here also collides with the Dawn card that is the chapter's anchor. | Prose / repeat |
| R2 | Ch.27 L329–331 | **Lost antecedent at a load-bearing moment.** "Bal rolled his head on the grass" became `His head rolled sideways.`, and it now follows directly on the storm mage's death ("He fell sideways into the grass and lay still."). "His" reads first as the dead mage's head, and "sideways" now occurs twice in two sentences. | Logic / Style |
| R3 | Ch.20 L135–139 | **Antecedent drift.** "That surge of anger had surprised him." became `The skin of his palm still prickled where it had split.` As a result, `Maybe he'd talk to Amelia about it later.` now points at the palm, not the wish to kill Sean. | Connective |

**Voice flattening:** none found. Bal's plain-practical narration, Amelia's play-to-menace flip, Viridia's needling and Lora's hedge/fluency switch all survive the trims. The cuts to the girls' "telling" beats (Ch.13 "nervously", Ch.24 "exasperated", Ch.22 "did not sound happy") removed redundancy without losing anyone's register.

**Repeated Amelia description:** trimmed well. Red eyes, black dress and rubies now appear only at the beats where they do work: the reveal, Ch.6's "nothing about her had changed at all", the Ch.10 uniform set-up and Ch.28's "the one he loved so much".

**New mouth-corner echo (watch, not a fix):** the line edit added two mouth-corner beats (Ch.11 "The corners of Amelia's mouth turned down", Ch.22 "corners of her mouth kept giving her away"). With Ch.2 "corner of her mouth to twitch" and Ch.9 "at the corners", that makes 4 book-wide, spread across 20 chapters, with no cluster. Leave it, but nothing more of this class should be added.

**Continuity slips the edit uncovered (pre-existing; eval 3 missed them):**

| # | Location | Problem |
|---|---|---|
| R4 | Ch.14 L129 vs Ch.5 L131–133 | Ch.14 says "In all the time he had known her, Bal had not seen her nervous over anything." Ch.5 says, in so many words, "He had seen her laugh and tease and turn into a cloud of bats. **Nervous was new.**" (at Verin's door, before asking to feed). This is a direct contradiction, and it falls in the card scene. |
| R5 | Ch.2 L21 | `Then her gaze came back down to him, and to the rug…, and arched a perfectly trimmed eyebrow.` The subject of "arched" is "her gaze". It is a one-word grammar slip on page 3 of the book, inside the Look Inside window. |

---

## 2. YA (upper YA) appropriateness, book-wide

The author's ruling: characters about sixteen; romance fade-to-black; nothing suggestive; the closing bedroom scene plainly cozy. **Ch.30 now meets this fully.** The bootlace, "Amelia took down her hair", "Lora's eyes were already closing", and "Nobody was hunting anybody, and they could all sleep." all read as sleep.

| Ch | Passage | Verdict |
|---|---|---|
| **24 L57–61** | Viridia undresses in front of Bal ("The gray dress slid to the floor… Bal had meant to keep to the window. He didn't… the rest of her was long and tan… caught him at it past the hem."), then: **`"Later," she said, and plainly meant it.`** The next morning (Ch.25 L5) Bal "climbed back in beside her". | **FLAG, required (Y1).** This is the one passage in the book that a YA editor, librarian or retailer would mark as sexual: a watched undressing followed by an explicit promise, with a shared bed the next scene. It breaks the author's "nothing suggestive" ruling. The fix keeps the scene and keeps Viridia teasing. |
| **3 L41–45** | Amelia's stretch, "riding high on her legs… very distracting", then **`"Time for that later,"`** | **FLAG, recommended (Y2).** It is a milder version of the same innuendo. As Ch.24's "Later" stands, it also makes a cross-chapter echo of the same beat. |
| **19 L203–209 → 20 L5** | "I've only got one bedroom." / "Then let's go to bed," they said together. The next chapter opens with the girls dressing in his bedroom. | **FLAG, recommended (Y3).** The line is a memorable source line and stays verbatim. Read cold, though, after he has kissed both girls, it leaves a fade-to-black that implies more than sleep. The author already ruled that the Ch.30 bed scene must read plainly cozy. One cozy line at the top of Ch.20 applies the same ruling here without touching Ch.19. |
| 14 L189 | Bal in his boxers climbs into bed with Amelia ("It's time for bed"). | Acceptable. It is comic, it is sleep, and the next morning shows nothing more. |
| 15 L9, L133–137 | A kiss on the mouth; her head on his chest. | Acceptable (chaste). |
| 2 L15; 11 L5, L23–27; 10 L17 | "exactly the right amount of curves"; admiring Viridia's legs and the "view"; classmates calling it "hot". | Acceptable for upper YA: ordinary teen attraction, nothing shown. |
| 16 L169; 21 L83 | Villains' "have some fun with them" and "enjoy myself afterward". | Acceptable. These are implied threats that are never rendered, and they justify the violence the source endorses. |
| 17 L123 | The bear tears Amelia's bodice. | Acceptable. It is played as embarrassment and nothing is described. |
| 18 L133 | Toma's "several concubines" (file note). | Acceptable. |
| 21 L127; 27 L265 | Iro beheaded; a dagger to the eye. | Acceptable for upper-YA fantasy (Cradle tier), with no gore lingering. |
| passim | "hell", "damned", "piss her off". | Acceptable. |

**YA verdict: appropriate for upper YA once Y1 is applied.** Y2 and Y3 are strongly recommended and cost +18 words net.

---

## 3. Genesis Score (whole book)

| Dimension | Score | Evidence | Cap reasons / holds |
|---|---|---|---|
| Originality | **8.5** (=) | Relocated weight: the whip fails at the climax ("It was like whipping a river", Ch.29), and the war is won by pushing blood into a life-bonded core. This pays off "*No inheritance gift,* Fern had read out of the file." Refused payoff: the poisoning is cancelled by the purification rune under the cup (Ch.25), planted in Ch.9. Inverted actor: the goddess is the boy's familiar and kneels to him (Ch.3, Ch.28). | none |
| Theme | **8.5** (=) | "Being wanted for who you are" is shown, never argued: "*Amelia Norheart.*" (Ch.13–14); "I don't need you here for what you can do for me. I want you here because I like you." (Ch.16); the girls' free "Yes" (Ch.19). There is plenty of texture that doesn't serve the theme: the Terra boy's roll in the soup, Leon's goat story, the old man with his boots off, "who washed them remained an open question" (Ch.30). | none |
| Characters | **8.5** (=) | Cover-the-name passes for all four leads. Lora: "Does either of you know a single thing about alchemy? No. You don't." Viridia: "Not looking at Bal? I'm a natural." Amelia: "Think your next words through, very carefully." Bal: "Who washed the plates, if they went away on their own?" Secondary characters have moments of their own (Verin, Mrs. Brown, Thad's stomach, Toma's "As I cared for my fellow priests"). Chaos is inhabited in Ch.27 ("Nobody was there but him."). | Gesture clusters: the gate is clean. My sweep of the classes the gate doesn't track flags Ch.4/5 laugh, Ch.12 smile and Ch.22 laugh, the same windows eval 3 judged as single beats or spread beats. No cap. R4 is a continuity fact about Amelia, not a character failure. |
| Prose & Voice | **8.5** (=) | Underlined sentences: "Someone had bricked up a door in him while he was too small to know there was a door there at all." (Ch.2); "…it must have taken her a great deal longer than a minute to learn to tell it that short." (Ch.4, the stopping sentence); "Everyone's life could be spent except their own." (Ch.9); "Nobody had written down the woman in the sling." (Ch.23); "In the dark it could have been anybody's hair." (Ch.26). Ugly-on-purpose sentences: "he ate both and then he ate her last piece of toast" (Ch.9); "It was a Tuesday, or it might have been a Thursday." (Ch.18). The voice changes under pressure: Ch.27 goes short and flat. Explanatory-gloss rate ≈0.3/1k, under the 0.8 cap. | **Held, not raised.** The line edit's gains (fewer described emotions, Pattern #10 down) are real. R1 and R2 are new blemishes, R2 in a climax beat. Net: hold at 8.5, and apply R1–R2. |
| Pacing & Coherence | **8.5** (=) | The turn-the-page rate is unchanged at ≈86% (25/29), since no chapter opening or ending was edited. The timeline holds (the poison's 24h + 6h lands at Ch.27's "close to six"). The Winespring thread is intact. | **R4 is a real contradiction** (Ch.5 vs Ch.14). It is a single line and doesn't move the dimension, but it must go. |
| Emotion | **8.5** (=) | Anchors vary. Emotional surprise: Amelia laughing until she weeps blood (Ch.21); strawberries in Iro's shirt. Body rebel: "the nails bit into the sygl" (Ch.4); Viridia's knees giving on the step (Ch.25). The line edit's Ch.25 pulse line strengthens the peak. | none |
| Source Fidelity (Dim 7) | **8.5** (=) | Beat order matches the source, and every 2026-10-20/21 ruling is honoured, including the new YA ruling at Ch.30. No line edit changed a speaker, an event or a memorable line. Ch.24's "Later" breaks the *YA ruling* (an author decision), so Y1 is filed under this dimension. | Y1 required to keep this at 8.5 after the YA ruling |
| **FLOOR** | **8.5** | | |
| **AVERAGE** | **8.5** (59.5/7) | | Gap 0.0 |

---

## 4. Per-chapter table (vs eval 3)

| Ch | Words | Eval 3 | Eval 4 | Note |
|---|---:|:-:|:-:|---|
| 1 | 3,185 | 8.5 | 8.5 | "Then his wits came back." is clean. |
| 2 | 3,137 | 8.5 | 8.5 | **R5** (gaze arched an eyebrow). Jaw/knuckles show-not-tell is an improvement. |
| 3 | 2,913 | 8.5 | 8.5 | **Y2** (recommended). "She didn't so much as blush" pays off in Ch.5. |
| 4 | 3,193 | 8.5 | 8.5 | The stopping sentence is intact. |
| 5 | 3,590 | 8.5 | 8.5 | Thistle's line was split well. "Nervous was new." is the line R4 contradicts. |
| 6 | 3,043 | 8.5 | 8.5 | "One by one, each of them said no." This is a clean head-shake de-dup. |
| 7 | 3,641 | 8.5 | 8.5 | "His shoulders dropped." |
| 8 | 2,257 | 8.5 | 8.5 | The hand-on-knee fix is correct. |
| 9 | 3,447 | 8.5 | 8.5 | The oatmeal callback is good. |
| 10 | 2,780 | 8.5 | 8.5 | "He could have kept at it all afternoon." |
| 11 | 3,609 | 8.5 | 8.5 | "nothing of her to look at but the back of her head" is better than the third sock. |
| 12 | 1,370 | 8.5 | 8.5 | untouched |
| 13 | 5,372 | 8.5 | 8.5 | "Lora said to the floor" |
| 14 | 2,383 | 9.0 | **8.5 → 9.0 after R1/R4** | Two blemishes in the summit chapter (R1 doubled phrase, R4 contradiction). The card scene itself is untouched. |
| 15 | 1,814 | 8.5 | 8.5 | |
| 16 | 4,614 | 8.5 | 8.5 | "still and windless", "She held still." Clean. |
| 17 | 2,443 | 8.5 | 8.5 | H1 is in. |
| 18 | 2,626 | 8.5 | 8.5 | |
| 19 | 2,294 | 8.5 | 8.5 | The ending is ambiguous for YA. Fixed downstream by Y3, with Ch.19 untouched. |
| 20 | 2,612 | 8.5 | 8.5 | **R3** antecedent; **Y3** (recommended). |
| 21 | 3,203 | 8.5 | 8.5 | |
| 22 | 3,387 | 8.5 | 8.5 | |
| 23 | 2,079 | 8.5 | 8.5 | "He hoped he looked enough like a servant." |
| 24 | 4,751 | 8.5 | **8.5 craft / YA: FAIL until Y1** | |
| 25 | 3,030 | 9.0 | 9.0 | The pulse line is an upgrade. |
| 26 | 1,599 | 8.5 | 8.5 | |
| 27 | 4,026 | 8.5 | 8.5 | **R2** lost antecedent at the rescue. |
| 28 | 2,606 | 8.5 | 8.5 | H2 is in. |
| 29 | 3,536 | 8.5 | 8.5 | |
| 30 | 1,540 | 8.5 | 8.5 | The close is plainly cozy and meets the YA ruling. |

**Below 8.5: none.** Mean 8.52 (8.53 once R1/R4 restore Ch.14).

---

## 5. REQUIRED FIXES (apply exactly; all gate-verified on a scratch copy)

| # | Location | Type | Replace | With | Δw |
|---|---|---|---|---|---|
| R1 | Ch.14 L119 | Style (line-edit repeat) | `"But going by the card in the shop, it should be plenty powerful." The card in the shop, he explained, had promised` | `"But it should be plenty powerful." The card propped beside it in the window, he explained, had promised` | −4 |
| R2 | Ch.27 L331 | Logic (lost antecedent) | `His head rolled sideways. It was all of him that would move.` | `Bal managed to roll his head toward the canyon. It was all of him that would move.` | +5 |
| R3 | Ch.20 L139 | Connective | `Maybe he'd talk to Amelia about it later.` | `Maybe he'd ask Amelia about this new temper later.` (This answers "He had never had much of a temper as a kid.") | +1 |
| R4 | Ch.14 L129 | Continuity (vs Ch.5 "Nervous was new.") | `In all the time he had known her, Bal had not seen her nervous over anything.` | `Bal had seen her nervous only once before, in the doorway at Verin's cottage, working up to a question she was afraid to ask.` | +8 |
| R5 | Ch.2 L21 | Grammar | `behind him, and arched a perfectly trimmed eyebrow.` | `behind him, and she arched a perfectly trimmed eyebrow.` | +1 |
| **Y1** | Ch.24 L57–63 (four paragraphs) | YA ruling | `The gray dress slid to the floor and she kicked free of it. Bal had meant to keep to the window. He didn't. She had a fine dusting of road on her shoulders where the collar had ended, and nowhere else, and the rest of her was long and tan. She shook out a clean shift and caught him at it past the hem.` ¶ `She smiled, slow.` ¶ `"Later," she said, and plainly meant it.` ¶ `She got herself into the shift and a plain skirt. Then she combed…` | `Bal turned to the window before the dress came down, and stayed turned, and studied the stable yard below as if he would be tested on it later. Cloth rustled behind him. When she said he could look, she was in a clean shift and a plain skirt, and she was grinning at him for having found the yard so interesting.` ¶ `Then she combed…` (The rest of that paragraph is unchanged. Lora's later "stopped folding the gray dress" still holds.) | −23 |

### Recommended (author's call; brings the two remaining soft spots in line with the YA ruling)
| # | Location | Replace | With | Δw |
|---|---|---|---|---|
| Y2 | Ch.3 L41 and L45 | `until it was riding high on her legs.` … `"Time for that later," she said,` | `until it was well up past her knees.` … `"Eyes up, Balthazaar," she said,` (Her teasing and the "didn't so much as blush" set-up for Ch.5 both stay.) | −1 |
| Y3 | Ch.20 L5, appended after "…at the pair of them." | — | `Last night they had all been asleep within minutes, and by midnight Viridia had taken most of the covers.` (Ch.19's "Then let's go to bed" stays verbatim. This applies the Ch.30 ruling to the book's other shared-bed fade.) | +19 |

**Totals:** R1–R5 + Y1 = −12 words, giving 90,068. All eight fixes = 90,086 (verified with `wc -w`). Both totals are **at or above 90,000.** After applying them:
- Re-run `style_check.py`, `grammar_check.py`, and `tic_report.py --gate` / `voice_wear_check.py` on the scratch `manuscript/chapters/` layout. All were clean in my verification run with all eight applied.
- If only some are applied, re-run the gates anyway.

---

## 6. Anti-AI scan (20 patterns), commercial thresholds

Seven patterns are present, all minor (<0.5/1k). The count is 7/20, in the clean band (0–8), and it is unchanged from eval 3.
- #3 rule of three ("gates, and a courtyard, and a stage", Ch.5)
- #6 "And" openers (~5)
- #10 described emotion: **reduced by the line edit**. About 30 of the "she was nervous / impressed / curious" lines are gone. What remains is deliberate ("Nervous was new.").
- #11 explanatory extension (≈0.3/1k)
- #12 binary negation ("Not hurt him. Kill him.", Ch.20)
- #13 precision ("Ten windows on the second story. Ten on the third.", Ch.24). Nobody carries counting as a device.
- #16 philosophical aside ("worth getting caught for", Ch.4)

Clear: #4 em dashes (0); #17 clean dialogue (interruptions and cross-talk in Ch.4 "Now," Amelia said over him, and in the Ch.30 two-voice account); #18 echo chamber; #20 temperature report. No over-correction flag. **The explanatory-gloss rate is ≈0.3/1k, under the 0.8 cap, so Prose is not capped.** The gesture-cluster check (3+ of one class within ~500 words) finds no real cluster, so Characters is not capped.

## 7. Reader simulation

- **Devourer.** The line edit makes the middle (Ch.13, Ch.24) a little quicker. They read Ch.25 onward in one sitting. They hit R2 at the rescue and reread one line.
- **Critic.** Underlines the same sentences eval 3 cited, plus the new pulse line. Catches R1 ("the card in the shop" twice) in the best chapter.
- **Hostile.**
  - Catches R4: "She was nervous at Verin's, two days in."
  - Still asks how Viridia found the Winespring (Ch.23). That remains texture only.
  - The whip "after a few days" (Ch.20) stays faithful to the source.
- **Casual.** Buys after three pages: a likeable boy, a dangerous and funny goddess, a warm found family. Tells a friend "the goddess is his *familiar*" and "he turned her poison into water". **Casual 8.5. No vibes problem.** The Ch.24 "Later" would be the line a parent or teacher flags if the book is shelved as YA.
- **Devoted (SFF).** The plants still pay off: the avoidance rune leading to the purification rune, the heart ring leading to Iro, "No inheritance gift" leading to Akora, and Amelia's own diary.

| Issue | Devourer | Critic | Hostile | Casual | Severity |
|---|:-:|:-:|:-:|:-:|---|
| Y1 Ch.24 undress / "Later" (YA) | | ✓ | ✓ | ✓ | **IMPORTANT** (market fit) |
| R2 Ch.27 lost antecedent | ✓ | ✓ | | | SHOULD FIX |
| R1 Ch.14 doubled phrase | | ✓ | | | INVESTIGATE (fix anyway; 3 words) |
| R4 Ch.5/Ch.14 contradiction | | | ✓ | | INVESTIGATE (fix anyway; continuity) |
| R3, R5 | | ✓ | | | INVESTIGATE |

## 8. Tomorrow Test, residue, CVI
- **Tomorrow Test:** IMAGE anchors: the blood-soaked shirt and the card ("*Amelia Norheart*"), strawberries in Iro's shirt, the rune under the cup, the still hair in the dark, the chalice. QUOTE anchors: "They have made me a *myth*?", "Because it's magic.", "No one threatens my girls.", "Okay. You can keep her." **BOTH types, 4+ anchors. ANCHOR EXISTS.**
- **Residue (Ch.30):** contentment and safety. Four on a couch "it was never built for", due dates as the best thing he has thought of in days, and now a plainly cozy bedroom. It is an emotion, not an evaluation. **PASS.**
- **Shareability:** quote 3, plot 4, emotional 3, giving 7.5.
- **CVI-Launch 8.9:**
  - Commercial pacing 8.5
  - Tomorrow 10
  - Casual 8.5
  - Shareability 7.5
  - Pitch 10
  - Closeness 10
  - A correctly shelved YA edition widens the market. Y1 is what makes that shelving safe.
- **CVI-Legacy 6.3.** That fits the Cradle / HWFWM lane and is not a revision target.

## Strengths to PRESERVE
- The Ch.4 photograph.
- Porter "the color of the chalk".
- The card and the blood-soaked shirt.
- Lora's long walk down the hall.
- "her two hands were holding each other back".
- The strawberries.
- Amelia's flat "No." and "Damn their war."
- The rune under the cup and the pulse in Viridia's throat.
- The still hair.
- The clear-sky boom.
- Toma's real grief.
- The two-voice account.
- The cozy Ch.30 close.

Do not let further passes touch Ch.9, Ch.14's card beat or Ch.25.

## PATH TO 8.5
Not required. The Genesis Floor is 8.5. To **hold** it through packaging:
1. Apply R1–R5 and Y1 (Y2 and Y3 recommended).
2. Re-run the four gates.
3. Process lesson for any further pass: **re-read the sentence before and after every edited line.** Both line-edit seams (R1, R2) were correct in isolation and wrong in context:
   - R1 doubled a noun phrase across two sentences.
   - R2 changed a subject from "Bal" to "His" right after another man's death.
   - The gate cannot see either.

## VERDICT
**PASS.** Genesis Floor 8.5 / Average 8.5 / Casual 8.5, the same as eval 3, with no chapter below 8.5. The book-wide line edit is a net gain and introduced no voice flattening. It did introduce two seams (R1 Ch.14, R2 Ch.27) and one antecedent drift (R3 Ch.20), and the read-through also surfaced a pre-existing contradiction (R4 Ch.5/Ch.14) and a grammar slip (R5 Ch.2). All five are one-line fixes. **YA: appropriate for upper YA once Y1 (Ch.24) is applied.** Y2 (Ch.3) and Y3 (Ch.20) are recommended. With all fixes the book is 90,086 words and every gate is clean.

BIAS CHECK: This evaluation was produced by the same system that wrote the prose. Confidence in scores above 8.0 requires external validation (beta readers, editors, comp analysis).
