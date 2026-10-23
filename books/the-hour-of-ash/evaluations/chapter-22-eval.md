# Evaluation: Chapter 22 — The Basilica Julia (run 2) · TURNING POINT (~53%)
**Evaluator:** book-evaluator (independent; did not write or revise this prose) | **Date:** 2026-10-23
**Text evaluated:** `manuscript/chapters/chapter-22.md`, md5 `75b74801c27f869f3bfb314a41f65971`. This is the page after writer → dialogue-polish → hook-craft → disruptor → continuity repair r1 (C-01…C-04, W-01…W-14, I-11/I-13/I-16). Measurements:
- **7,179 words** (metaphor/shape), 7,212 (show_tell), 7,557 (`wc -w` with the header comments).
- Dialogue **35.8%** (show_tell) / 36% (shape); median sentence 17 (gear high).
- 7 breaks / 8 sections; `long-spiral` → `dialogue`.

**Read against:**
- The book's CLAUDE.md.
- STATE.yaml: guardrails, retired reflexes, AUTHOR-CP2-2 (memories), CP3-3, CP4-1, CP4-2 and END-1.
- outline.md: ledger row 22 and `## Chapter 22`, including the legal texture, the Ch.17 and Ch.21 guards, the writer warnings and the beat subversion. Also Ch.21 and Ch.23 for the handoffs.
- voice-dna.md §1: dialogue conventions, voice under pressure, the gear table.
- character-bible.md: **At-risk after Ch.20, Ch.21 and Ch.22** in full, plus the retired/at-risk table.
- chapter-21.md: the close, read whole.
- `evaluations/dialogue-chapter-22.md`, `hook-chapter-22.md`, `disruption-chapter-22.md`, and `continuity/chapter-22-audit.md` **with its repair log**. I do not re-raise anything the repair fixed or ruled on, for example C-02 (the bladder → sweat) and W-04 (Marcus biting).
- `chapter-21-eval.md` for the bar and the format.

**Genre profile:**
- Commercial historical romance / time-slip (comp *Outlander*).
- Anti-AI band: commercial (0–8 clean). The #11 cap is >6 instances or >0.8/1k.
- Dimension 7 = **IMMERSION**.
- Book engagement: empathy 55 / fascination 30 / self-insertion 15. This chapter is the book's **fascination set piece**: the court, the forgery's tell, the sneeze.

**Measured on the real file** (from the book folder):
- `bash tools/check_chapter.sh 22`: **ALL MECHANICAL GATES CLEAN**.
  - Style: simile 1.0/1k, em-dash 0, foreshadow 0.
  - Grammar 0. Rhythm 0. Show/tell: no flags, 35.8%.
  - Voice-wear strict: clean. Tic gate: clean. Metaphor 1.4 fig/1k. SHAPE CLEAN.
- `tic_report.py --gate`: clean.
  - And-chains 6/9; credential asides 0; negation pivots 0; 'So' 0.
  - Gesture classes in Ch.22 (computed with the gate's own regexes): object handling 4, deliberation pause 2, bend 1, on-the-knee 1. The long-chapter cap is 7, so all are under it.
- `tic_report.py --echoes 22`: 99 advisory echoes. **Spoken-line echoes: none.** Command-echo candidates: 1 (reported speech, "Myrrhine says that I shook" → "Myrrhine looked"), a false positive.

**My own scans (scratch only):**
- Stop-word-bounded 4/5-grams of Ch.22 against all voice-bank samples.
- Every short spoken line (≤5 words) grepped against Ch.1–21.
- Narration scanned for forward reach (would / never / last / still / years).
- Laugh channel scan: mouth 0, "behaved" 0.
- "nine" 0, "citizen" 0, the brother's name 0.
- By hand: recurring stage business that the gesture gate cannot classify, and within-chapter doubles.

*(l.N = line number in the current `chapter-22.md`.)*

---

## HEADLINE
**CVI-Launch:** **9.6** (9.1 + 0.5 strong anchor) | **CVI-Legacy:** **7.0** (provisional) | **Genesis Floor:** **7.5** | **Genesis Average:** **8.57** | **Casual Reader:** **9.0**

**Engagement type:** Fascination (60): the forgery undone by a consul's calendar, the name thrown to the back of the aisle, the sneeze. Empathy (30): Mara sent out and missing it; Plautia's son on the steps. Self-insertion (10): a box ride into Rome.

**Divergence alert (2.1):** commercially this is the strongest chapter of the run, but its craft Floor sits on **one law cap that no gate can see**. The judge's shut eyes are a walk-on's running device, noted 11 times in the chapter, three of them as his own speech beat. Four cuts remove the cap. The divergence is a defect in the book's law, not a flaw in the chapter.

**Gate (Floor ≥ 8.5 AND Casual ≥ 8.5 AND pacing OK): NOT MET at cycle 0.**
- Casual 9.0 ✓. Pacing OK ✓ (judged below). Mechanical gates clean ✓.
- **Characters is capped at 7.5** under the gesture-tic law (spec: a class that reaches the chapter cap, 7 here, or 3+ inside 500 words). The class is **the judge's closed eyes**:
  - l.82 "listened with closed eyes" / "took him to be asleep"; l.130 "the judge's eyes opened again"; l.176 "The judge keeps his eyes shut."
  - l.190 "the judge said, **from behind his eyelids**"; l.208 "the judge remarked **to the inside of his eyelids**"; l.228 "to the judge's closed eyes"; l.240 "The judge, eyes still closed, said it."
  - l.262 "The judge saw, and he was asleep."; l.328 "the judge opened his"; l.398 "without opening his eyes for it."
  - That is **11 mentions, and 4 of them (l.190, l.208, l.228, l.240) fall inside about 500 words.**
  - It also breaks voice-dna's dialogue rule: "no character gets the same beat twice in a chapter". l.190, l.208 and l.240 are all his speech beat.
  - **Narrated waiting by Valens** is a second, smaller class of the same kind, 5 times (l.84, l.210, l.244, l.266 ×2 in Myrrhine's mouth, l.320 ×2). l.320 explains itself back to the sneeze.
  - **Uncapped, Characters is 8.5.**
- **Prose & Voice 8.5** (not 9.0), held by a small law-and-polish cluster:
  - one voice-bank lift (sample-04's "clerk wrote me down", in Valens's testimony);
  - an adverb in a speech tag ("he said hoarsely", which voice-dna forbids);
  - "the law allows him" ×2;
  - a false superlative (the amphitheatre as "the largest work of hands in this world that I knew of");
  - the arena thought paired with the child's body. The outline says "must not become … symbolism".
- **The fix set: 17 replacements, tested together on a scratch copy** (script below). All but three are cuts or one-for-one swaps.
  - After: **7,093 words** (shape), dialogue **36.2%** (show_tell; shape 36), median 17, `long-spiral` → `dialogue`, 7 breaks.
  - `check_chapter.sh 22`: **ALL MECHANICAL GATES CLEAN.** The tic gate is clean. And-chains 6 → 5.
  - `--echoes 22`: 99 → **95**, a **strict subset** (compared on the full, uncapped echo list). **No new echo.** Spoken-line echoes none.
  - Voice-bank content hits 3 → **0**. The one survivor, "the back I said", is a quote-boundary artifact.
  - The judge's eyes go from 11 to **6** (under the cap of 7; no three inside 500 words). Valens's narrated waiting goes from 5 to **3**.
  - **Projected:** Floor 8.5 / Average 8.71.

---

## Genesis Score (Craft Assessment, cycle 0)

| Dimension | Score | Evidence | Cap reasons |
|-----------|-------|----------|-------------|
| Originality | **8.5** | The genre beat (the villain beaten in a dramatic confrontation) is refused twice over. The climax of the testimony is **interrupted by a sneeze and a courtroom "Salve" chorus** ("The judge, eyes still closed, said it."), and the heroine is carried out laughing and **misses it** (l.246–250). The verdict lands **under a neighbouring lawsuit's hired applause**, so the brother has to ask "The sixth?" (l.400–404). The forgery falls to a bored assessor's family calendar: "My uncle will be sorry to hear it … He'd have liked the extra months." (l.136). The name is thrown past the judge to the idlers at the back (l.192–196). | Not 9.0: the backdated document betrayed by its date is a familiar forgery tell. The comedy makes it fresh, but the mechanism is not. |
| Theme | **9.0** | "Being known as a kind of home" is acted, never stated. "…and the man next to him said the name back." (l.196). The verdict that clears him does not use it: "Nobody said the name of the witness." (l.406). A stranger's shrug complicates it: "Where's this gladiator?" / "The one standing still." / "Oh, him." (l.300–304). The counter-case is Plautia, the one person in the suit "whom nobody needs to hear" (l.58). The closing line passes the name one generation down: "Marcus, this is Valens. He used to carry you." The texture is real noise with no theme in it (the wax nose in the cupboard, the onion, the walnuts, the dog that "bit a magistrate"). | — |
| Characters | **7.5** (uncapped 8.5) | **Plautia's best chapter:** "Of everything about him, that alone ever frightened me." / "What I did, I cannot say. I would be grateful if nobody told me." / the veil she lets her son hold. **Valens:** "Who was on the roofs, and where the dogs were." / "You never heard it," / the onion memory, triggered by the bench and dropped by the judge. **Celer:** practising the name on his steward, the ladder, the foot that "had begun to go on the step". **Myrrhine:** prices, red shoes, "Nothing's given,". **Marcus:** the formula, then the dog. The advocates, the dyer and the merchant each have their own syntax. Cover-the-name PASS for all 14 speakers. Mara's chaos is 4/4, the laugh inhabited (below). | **CAPPED 7.5:** the judge's shut eyes ×11 (4 inside ~500 words; his speech beat ×3); Valens's narrated waiting ×5 (→ F1, F2). Not 9.0 uncapped: Myrrhine's four deflating quips in two sections ("That makes it a game." / "Nothing's given," / "He got it cheap" / "He's good at waiting, that one") are WATCH. |
| Prose & Voice | **8.5** | **Underlines:** the 98-word opening spiral, each noise drowned by the next; "the crack of one showed the yellow wax of somebody's nose." (l.20); "He pitched it as he would hail the string in a crosswind" and the will-reader who "lost his place in it" (l.196); "He sneezed again, smaller, and one old voice at the rear of the aisle said 'Salve' to him all by itself, kindly, and that finished me." (l.246); **"This one still had the chisel in it, and my fingertips came away from its cups gray with grit."** (l.274, **the close-the-book sentence**). Ugly sentence present: "The shift was too long for me and I wore it anyway." Voice under pressure: the laugh paragraph drops every aside and narrates only the body ("My heels had begun knocking on the marble by themselves"), then the blur. | Held at 8.5 by the cluster above (→ F3–F9). #11: 4 firm, 0.56/1k, PASS. |
| Pacing | **8.5** | Strict court/city alternation, as the ledger asks. Every exit pulls: the veil instruction; "went to his lunch"; "he slept."; **"and the curtain swung across it"** (the heroine shut out of her own climax); the empty bench; the Parilia date. Value shift: Valens begins as "my client's property" and "not heard against his master", and ends named, believed and introduced to the boy he carried. Speed varies: the spiral and the Forum run long; the night carts and the cross-examination run clipped. | The post-climax stretch S5–S7 (about 2,500 words: steps, Forum, gallery, bedroom, amphitheatre, Argiletum) is the chapter's one slow run. It is earned (the three days the judge takes), but it is where a Devourer skims. |
| Emotion | **9.0** | **Anchor (outline):** Valens says his own name to the back benches, and it lands on strangers (l.194–196). **Surprise (outline):** the laugh at the sneeze during "the gravest testimony of Valens's life", body-only and never through the mouth: "It started under the child … the bench shook under them … Myrrhine's thigh was against mine, and I felt her feel it." **Body rebel:** inhabited, the heels on the marble. **Second rebel, reported:** Plautia "shaking too … Under the veil." Techniques: physical, comedy-in-gravity, withheld scene (Mara misses the testimony; Valens "looked first at the place where I had been … both empty"), object (the veil's fringe wound and let go), formula breaking into a child's rush. | Not 9.5: the Marcus reunion is held at arm's length by design. The strongest beat (the empty bench) is seen from the gallery and lightly narrated. |
| Immersion | **9.0** | Rome AD 74 as a working city that Mara uses and suffers: the daylight wheel ban and the night carts "on iron tires"; the hired chair; the ancestors' wax masks in cupboards; the rosemary pot stapled with lead; built Flavian hair on a cane frame; four courts behind curtains; the water clock's jar; "Salve" to a sneeze; walnuts on the steps; the Vestal spooning Parilia ash, "Ovid had stood in that line once"; the treadwheel cranes and the lead run into the cramps; travertine "with holes in it of its own, like bread"; the Argiletum cobblers. | Not 9.5: one false superlative (F8). |
| **FLOOR** | **7.5** | | Characters (law cap) |
| **AVERAGE** | **8.57** | | |

---

## CVI-Launch Breakdown (Commercial Assessment)

| Input | Score | Evidence |
|-------|-------|----------|
| Commercial Pacing | 8.5/10 | High gear, 36% dialogue, 8 short scenes alternating. Plants (the veil, the foot, the hair) pay off in the chapter itself. The S5–S7 middle is slower. |
| Tomorrow Test | 4+ anchors → 10 | IMAGE: the idler who sits up and says the name back; the whole court, judge included, saying "Salve"; Mara's heels knocking on the marble; Marcus holding the veil's edge. QUOTE: "Gaius Iulius Valens. Freed at Corinth."; "You never heard it,"; "Marcus, this is Valens. He used to carry you. Greet him." |
| Casual Reader | 9.0/10 | See report. |
| Shareability (quote/plot/emotional) | 4 / 4 / 4 → 8/8/8; 0.6×8 + 0.4×8 = **8.0** | "You never heard it." / "she got thrown out of her husband's trial for laughing at a sneeze" / the boy at the bottom of the steps. |
| Concept Pitch | yes (10) | "A time-stranded woman watches the ex-gladiator she married say his real name in a Roman court, and gets carried out laughing when a man sneezes." |
| Human Closeness | yes (10) | Marriage, a child coming, a mother and her son, a maid and her lady. |

**CVI-Launch = 0.2×8.5 + 0.2×10 + 0.2×9 + 0.2×8.0 + 0.1×10 + 0.1×10 = 9.1, + 0.5 strong anchor = 9.6.**
**CVI-Legacy (provisional, default weights):** Originality 8.5×0.30 + Theme 9.0×0.25 + Cultural vocabulary 3×0.20 + Re-readability 7×0.15 (Celer's foot, the veil, the hair, the ladder all reward a second read) + Identity 5×0.10 = **6.95 → 7.0**.

---

## Anti-AI Scan (20 patterns; per 1,000 words at 7.18k; commercial band)

| # | Pattern | Result | Count · density | Citation |
|---|---|---|---|---|
| 1 | Forced symmetry | Found, minor | 2 · 0.28 | "Whoever stapled it was better at his trade than whoever threw it."; "That board had been worn … This one still had the chisel in it" (earned). −0.125 |
| 2 | Empty poetic vocabulary | Clear | 0 | |
| 3 | Automatic rule of three | Found, moderate | 5 · 0.70 | "a light, sick, scoured feeling"; "black mud, old drains and wet rope"; "through the carts, and the singing, and the knocking" (the designed held sentence, keep); "to me, and to the lady, and … to the gods in the cupboard" (testimony, keep); "by two coached house slaves, and by the defendant's word …, and by nothing else" (an advocate's period, keep). No anaphora triad. −0.25 |
| 4 | Em dashes | Clear | 0 | |
| 5 | Empty metaphors | Clear | 0 | |
| 6 | Dramatic "And" openings | Clear | 0 in narration | |
| 7 | Pseudo-philosophical closings | Clear | 0 | No section closes on a maxim in narration. |
| 8 | Excessive parallelism | Found, minor | 1 | "the four courts were four crowds round four small platforms … the four of them … four rooms of one party" (l.296, → F12). The Salve cascade is designed comedy. −0.125 |
| 9 | Overly smooth transitions | Clear | — | |
| 10 | Described emotions | Clear | 0 | "a light, sick, scoured feeling, as after an hour's crying" is bodily. |
| 11 | Explanatory extension | Found, moderate | 4 · 0.56 | "from his manner, this was his daily work"; "as he had waited for the sneeze to finish" (→ F2b); "for the wax had darkened since Corinth"; "because four courts sat in it at once". −0.25. **Commercial cap PASS.** |
| 12 | Binary negation opener | Clear | 0 | |
| 13 | Precision flex | Found, minor | 3 · 0.42 | "eleven days", "the fourth name" / "the seventh", "four" ×5 (F12). No counting device. −0.125 |
| 14 | Emotional control demonstration | Clear | 0 | Every control in the chapter fails (Mara, Plautia). |
| 15 | Authoritative description | Found, minor | 1 | "already the largest work of hands in this world that I knew of" (l.370, wrong for a narrator who knows the Circus Maximus; → F8). Gaps elsewhere are good: "a crescent of cane, I thought, or of wire". −0.125 |
| 16 | Philosophical asides | Found, moderate | 4 · 0.56 | All in speech, in character: "Written fair, a mistake is still a mistake."; "That makes it a game."; "Nothing's given,"; "They grow so fast." (Celer's deliberate commonplace). −0.25 |
| 17 | Clean dialogue | Found, minor | testimony Q&A | Turn-based by the genre of a court; broken by the onion, the sneeze, the applause and Celer's interjection. −0.125 |
| 18 | Thematic echo chamber | Clear | — | The onion, walnuts, the wax nose, the dog that bit a magistrate. |
| 19 | Graduated reveal | Clear | — | Parallel; not the establish → anomaly shape. |
| 20 | Emotional temperature report | Clear | 0 | |

**8/20 patterns, −1.375. Clean band (commercial 0–8), at its top edge.** After the fix set, #8 and #15 clear and #11 drops to 3 (0.42, minor): **6/20, −1.0.**

## The book's own laws
- **NO FORESHADOWING: PASS.**
  - The narration was scanned for would / never / last / still / years. Every hit is in-scene or past-facing: "nothing in my legs would stop them"; the 1991 memory, which the outline allows.
  - "already … not a third built" reaches no outcome.
  - No mountain, no 79. The gate count is 0.
  - S3's "Look to the back … Talk to them." is in-scene planning that the scene then pays off, not a narrator reaching forward.
- **NO TICS: the gate PASSES; the hand scan FAILS at cycle 0.**
  - The judge's closed eyes ×11 (F1) and Valens's narrated waiting ×5 (F2) are both stage business the gesture classes cannot see.
  - No phrase reaches 3 book-wide.
- **Retired reflexes: PASS.** No significance-tagging, no negation opener, no anaphora triad, no performed candour, and no closing aphorism in narration. **WATCH:** S5 exits on Myrrhine's "Nothing's given," followed by the image of the red shoes. It works as character, but it is the nearest thing to a proverb-button in the chapter.
- **No spoken line reused: PASS.** The gate shows none. I grepped 31 short lines by hand ("People.", "Five. Nearly six.", "So it does.", "His name.", "He brought me.", "Thrace.", "The lanista's.", "With the rest.", "Games.", "Laughing?", "I didn't ask her.", "Not to the court.", "It is given.", "At the judge.", "I watched the street.", "He did.", "What they asked.", "That's a heel," …), and all are first uses.
- **No courtroom clichés: PASS with one finding.**
  - No surprise witness: Nicanor is absent, and the witnesses are the names on the leaf. No outburst except the outlined one. No triumphant speech.
  - **l.324 "The court has heard the question."** is TV courtroom drama's "Withdrawn, but the jury heard it", transplanted (→ F10). "I find for the plaintiff" is plain legal English, so keep it.
- **Mara's laugh not through the mouth: PASS.** Mouth 0 and "behaved" 0 in the whole chapter. The laugh lives in the body (under the child, shoulders, fists, heels, eyes and nose). It is the only Mara laugh since Ch.20, as mapped.
- **The witnesses never "the nine": PASS.** "nine" does not appear in the chapter. They are "two of them", "the fourth name", "the seventh".
- **The brother unnamed: PASS.** He is "Plautia's brother" or "the brother" throughout.
- **The child never called a citizen: PASS.** "citizen" 0. The child is ungendered; "Does it weigh on her?" refers to Mara.
- **Memories (CP2-2): PASS.** One longer memory, the 1991 board. It is triggered by the step's board and returns to it ("This one still had the chisel in it"). Ch.21's memories were sentence-scale, so the every-other-chapter rule holds. The R-volume clause in S1 is a clause.
- **CP4-1 / CP4-2 / CP3-3: PASS.** No tomb, no door, no gap remark.
- **Outline warnings: PASS** except F9. The amphitheatre thought comes once, but it is set against "the child stretched in me from one hip to the other". The continuity repair's swap for the spent hiccups put back the gladiator's-child pairing that the disruptor had cut. **Em-dashes 0.**

## Character Chaos Check (Primary: Mara)
- **Irrelevant thought: present, inhabited.** The stapled pot "by somebody who knew what he was doing"; the wax nose in the cupboard; the last passenger's hair oil.
- **Cognitive distortion: present.** She takes the judge to be asleep for the first hour; she misreads the shaking under the veil and has to ask "Laughing?".
- **Unprompted memory: present, triggered and returned.** The 1991 board, the peach and the custodian's whistle.
- **Failed emotional management: present, inhabited.** The laugh. No narrator commentary until the steps, and even there the laughing "went on by itself in my shoulders, without me".
- **Voice under pressure: demonstrated.** The asides vanish during the fit, and the court goes "to a blur".

## Secondary Character Chaos
- **Plautia:** has her own moments (the pot she offers and remembers is not hers; the hand "under her cloak"; the night visit in which she will not be told what she did).
- **Myrrhine:** her own (the shoes "hot coals to her ever since"; the fuller who "can whistle"; going to price the Vestal's crock barefoot).
- **Celer:** his own (practising the name on his steward; the ladder; the foot).
- **The judge, the advocates, the dyer, the merchant, the sneezer, Marcus, the gallery woman:** each has a line that is theirs.
- **No secondary character is only a prop.**

## The Tomorrow Test
**What the reader remembers:**
- An idler asleep against a pillar at the back of the Basilica comes off it upright when Valens says his name, and "the man next to him said the name back".
- Close behind: the whole court saying "Salve" to a sneeze, the judge with his eyes shut, and Mara carried out shaking.
- And the last line, "He used to carry you. Greet him."

**Anchor type:** BOTH (image + quote). **Verdict:** ANCHOR EXISTS. It is a different type from Ch.21's (a mark scratched in plaster) and Ch.20's (a mended object).

## The Shareability Test
"She's six months pregnant at her husband's trial in ancient Rome, a man sneezes during his testimony, the whole court including the judge says bless you, and she laughs so hard she gets carried out." This is text-able. The book is well past the minimum of 3–4 shareable moments.

---

## Reader Reports

### The Devourer
They ride the spiral into Rome and Plautia's hair, then race S2 to S4. The forgery's tell and the sneeze are the fastest pages of the run.
- **Where they skim:** S7's construction detail, the cramps and the lead (about 300 words), and possibly the Forum paragraph. Both are short.
- **Why they never stop:** every section is under 1,500 words, and each exit pulls. The verdict under someone else's clapping and the boy on the steps carry them over the line into Ch.23.
- **No stop point.**

### The Critic
**Underlines:**
- the wax nose;
- "He pitched it as he would hail the string in a crosswind";
- "said 'Salve' to him all by itself, kindly, and that finished me";
- "This one still had the chisel in it";
- "Who was on the roofs, and where the dogs were.";
- "I would be grateful if nobody told me.";
- "You never heard it,".

**Disappointments:**
- The judge's eyes become a running joke the chapter keeps winking at: "behind his eyelids", then "the inside of his eyelids" eighteen lines later.
- "The largest work of hands in this world" is not what this narrator would say.
- The arena thought is underlined by the child moving.
- "The law allows him" comes twice.

### The Hostile
- **l.370 "the largest work of hands in this world that I knew of":** the Circus Maximus and the pyramids are larger, and she knows both (→ F8).
- **l.324 "The court has heard the question.":** a borrowed courtroom-drama trope (→ F10).
- **l.218 "his clerk wrote me down":** a voice-bank sentence in Valens's mouth (→ F3).
- **"Not to the court." (l.282), then she is in the gallery (l.296).** Read as the bench versus the gallery, this is consistent: she watches unseen. I am not changing it.
- **The laugh paragraph** does not name laughter until the steps ("the laughing went on by itself"). For three sentences "It started under the child … a jolt low down" can read as labor. The sneeze, the "Salve" and "that finished me" resolve it inside the paragraph. **INVESTIGATE, no change:** the delay is the design, and naming it risks the closed mouth channel.
- **"The lead fumed white and sweet-smelling":** molten lead has little smell. INVESTIGATE; it is plausible as the brazier's smell.
- **Nothing to challenge** in the law (audit I-01…I-08), the dates or the seating (C-03 fixed).

### The Casual Reader (airport, 10 pages)
They are carried into Rome in a box that smells of the last passenger's hair oil. They meet a lady whose hair has a frame inside it, and who offers away a pot and remembers it is not hers. Then a courtroom where four trials shout at once through curtains. They stay because it is funny and warm and nobody is a cardboard villain: Celer is charming, the judge naps, the dyer cannot remember the face but remembers his cloak. By the sneeze they are hooked. **They'd buy it. 9.0.**

### The Devoted Reader (active: long saga)
They will catch:
- Valens's dinner-table read of Celer's foot, paid off on the steps;
- the veil instruction paid by the boy holding the veil;
- "Your hair's different." answering S1's built hair;
- Celer going round the ladder (Ch.17's scaffold);
- "a pace back" (the wages line) beside Ch.18's quay;
- the Ovid in the Vestal's line.

The Reddit post is about the empty bench seen from the gallery. They will also notice the judge's eyes being re-noted.

## Cross-Reader Matrix

| Issue | Devourer | Critic | Hostile | Casual | Devoted | Severity |
|---|---|---|---|---|---|---|
| The judge's shut eyes re-noted ×11 (his speech beat ×3) | | ✓ | | | ✓ | SHOULD FIX (book law: blocking; Characters cap) |
| Valens's waiting narrated ×5, one explaining itself | | ✓ | | | | INVESTIGATE (law: fixed with F1) |
| Voice-bank lift / adverb tag / "law allows" ×2 | | ✓ | ✓ | | | SHOULD FIX |
| False superlative (amphitheatre) | | ✓ | ✓ | | | SHOULD FIX |
| Arena thought paired with the child | | ✓ | | | ✓ | SHOULD FIX (outline warning) |
| "The court has heard the question." | | | ✓ | | | INVESTIGATE (law: no courtroom clichés → fix) |
| S5–S7 slow middle | ✓ | | | | | INVESTIGATE (no change) |
| Laugh unnamed for three sentences | | | ✓ | | | INVESTIGATE (no change) |
| No Casual-only flag | | | | — | | — |

---

## Revision Recommendations (Ranked)

| ID | Location | Problem type | What happens now | Why it fails | Revision direction | Project rule? |
|---|---|---|---|---|---|---|
| F1a–d | l.190, l.208, l.228, l.328 | Character (gesture tic) | The judge's closed eyes noted 11 times; "from behind his eyelids" / "to the inside of his eyelids" / "to the judge's closed eyes" / "the judge opened his" | Reaches the chapter cap (7) with 4 inside ~500 words; the same speech beat ×3 breaks voice-dna's dialogue conventions | Cut the four. Keep the six that do work: the introduction, the eyes opening at the date, "Salve" with eyes closed, "The judge keeps his eyes shut." (Valens's reason to look to the back), "he was asleep", and the verdict "without opening his eyes". | **Yes: a walk-on's trait is noted ≤3 times per chapter** |
| F2a–b | l.210, l.320 | Character | "Valens waited for the next question." / "and waited, as he had waited for the sneeze to finish," | Valens's waiting narrated ×5 and Myrrhine names it ("He's good at waiting, that one"); l.320 explains itself (#11) | "Our advocate supplied the next question, and the next, and Valens answered them…" / "…his gaze at the aisle's end, and the water ran in the clock." | — |
| F3 | l.218 | Style (voice-bank law) | "and his clerk wrote me down." | sample-04, "The clerk wrote me down" | "and I stood while his clerk wrote." The advocate's next question, "while he wrote?", picks it up. | — |
| F4 | l.24 | Style (voice-bank) | "It had been built up" | sample-10 4-gram | "It was built up" | — |
| F5 | l.298 | Style (voice-bank + echo) | "Celer's advocate stood in front of him" | sample-05 4-gram; Ch.19 echo | "Celer's advocate had closed on him" | — |
| F6 | l.326 | Style | "he said hoarsely." | Adverb in a tag (voice-dna); "hoarse" ×3 | "he said." | — |
| F7 | l.400 | Style | "within the time the law allows him." | Repeats Plautia's "which the law allows him" (l.58) | "within the time the law gives him." | — |
| F8 | l.370 | Logic / #15 | "already the largest work of hands in this world that I knew of," | False for this narrator | Cut the clause: "stood the beginning of the amphitheatre, not a third built." | — |
| F9 | l.374 | Style (outline warning) | "…while a whole city watched them. I thought that, standing in the white dust, and the child stretched in me from one hip to the other. Then a carter bellowed" | The body beat answers the thought, so the gladiator's child becomes symbolism. Also "whole city" ×2 in four sentences. | "…while Rome watched them. I was thinking that, in the white dust, when a carter bellowed" (the thought once, cut off by an oxcart) | Yes: the arena thought never gets a body reply |
| F10 | l.324 | Style (courtroom cliché) | "The court has heard the question." | The "withdrawn, but the jury heard it" trope | Cut the sentence. "It knows my client's family, and it can see the witness." keeps the insinuation. | — |
| F11 | l.238 | Style | "and the curtain beside him swung." | "swung" twice in 12 lines; the exit's "the curtain swung across it" is protected | Cut the clause. The sentence now ends "and when it came it was enormous." | — |
| F12 | l.296 | Style (#8, #13) | "four" ×5 in one sentence | Rhetorical counting | "the courts were four crowds round small platforms, … and I heard all of them at once, four rooms of one party." | — |
| F13 | l.354 | Style | "He slept on his back before the lamp had burned down a finger's width." | Valens on his back again (l.154); a body-part ruler (WATCH); a Ch.8 echo | "He was asleep before the lamp wanted trimming." | — |

**Tested and rejected (these strings planted findings; do not use):**
- "Celer's advocate was a yard from him" ("a yard from" would be a 3rd use book-wide: Ch.12, 13, 22 → tic gate FAIL).
- "said the judge." for F1b (a 3rd "said the judge" in the chapter → FAIL).
- "the judge said." for F1b (with "The judge said salve." it makes 3 → FAIL).
- "and they could be heard together" (a pronoun-swapped echo of Ch.8).
- "up here I" (Ch.6, Ch.9 echo).
- "bellied" (Ch.20).

### Fix order: Logic (F8) → Character (F1, F2) → Law / reuse (F3–F5, F9, F10) → Prose (F6, F7, F11–F13)

### The fix script (tested)
Saved at `/tmp/claude-0/-home-user/63791ee5-159c-5791-9429-07920f8d9417/scratchpad/fixes22/apply_fixes.py`. Run it from the book folder: `python3 <script> manuscript/chapters/chapter-22.md`. It checks that **every** old string matches exactly once **before writing anything**, and exits without writing if any does not.
```python
FIXES = [
 ("F1a", "\"I'll hear him first,\" the judge said, from behind his eyelids, \"and decide afterward",
         "\"I'll hear him first,\" the judge said, \"and decide afterward"),
 ("F1b", "\"The court is not buying onions,\" the judge remarked to the inside of his eyelids.",
         "\"The court is not buying onions,\" the judge remarked."),
 ("F1c", "\"In silver,\" our advocate repeated, to the judge's closed eyes. \"To his own slave.\"",
         "\"In silver,\" our advocate repeated. \"To his own slave.\""),
 ("F1d", "seen with its own eyes, and the judge opened his and promised his sentence",
         "seen with its own eyes, and the judge promised his sentence"),
 ("F2a", "Valens waited for the next question. Our advocate supplied it, and the next, and he answered them",
         "Our advocate supplied the next question, and the next, and Valens answered them"),
 ("F2b", "his gaze at the aisle's end, and waited, as he had waited for the sneeze to finish, and the water ran in the clock.",
         "his gaze at the aisle's end, and the water ran in the clock."),
 ("F3",  "and his clerk wrote me down.\"", "and I stood while his clerk wrote.\""),
 ("F4",  "It had been built up over her forehead", "It was built up over her forehead"),
 ("F5",  "Celer's advocate stood in front of him, with his free hand open.",
         "Celer's advocate had closed on him, with his free hand open."),
 ("F6",  "against a steward's,\" he said hoarsely.", "against a steward's,\" he said."),
 ("F7",  "within the time the law allows him.", "within the time the law gives him."),
 ("F8",  "stood the beginning of the amphitheatre, already the largest work of hands in this world that I knew of, and not a third built.",
         "stood the beginning of the amphitheatre, not a third built."),
 ("F9",  "It was a place for men to fight in, while a whole city watched them. I thought that, standing in the white dust, and the child stretched in me from one hip to the other. Then a carter bellowed",
         "It was a place for men to fight in, while Rome watched them. I was thinking that, in the white dust, when a carter bellowed"),
 ("F10", "\"As the court pleases,\" said Celer's advocate. \"The court has heard the question. It knows",
         "\"As the court pleases,\" said Celer's advocate. \"It knows"),
 ("F11", "and when it came it was enormous, and the curtain beside him swung.", "and when it came it was enormous."),
 ("F12", "the four courts were four crowds round four small platforms, their curtains moving whenever somebody pushed through, and the four of them could be heard together,",
         "the courts were four crowds round small platforms, their curtains moving whenever somebody pushed through, and I heard all of them at once,"),
 ("F13", "He slept on his back before the lamp had burned down a finger's width.",
         "He was asleep before the lamp wanted trimming."),
]
```

**Tested result.** The scratch copy is at `/tmp/claude-0/-home-user/63791ee5-159c-5791-9429-07920f8d9417/scratchpad/eval22/books/the-hour-of-ash/`, with the repo `tools/` linked so the shape audit runs. md5 after: `6835a01ea73b60b54bb8e727eaf2b1e3`.
- All 17 applied, once each.
- `bash tools/check_chapter.sh 22`: **ALL MECHANICAL GATES CLEAN**.
  - Style: 7,106 words, simile 1.0/1k, em-dash 0, foreshadow 0.
  - Grammar 0. Rhythm 0.
  - Show/tell: 7,128 words, **dialogue 36.2%**.
  - Voice-wear strict: clean. Tic gate: clean, and-chains 5/9. Metaphor 1.4. SHAPE CLEAN.
- shape: `22 7093 7 36 17 long-spiral dialogue`.
- `--echoes 22`: 95, a **strict subset** of the 99 before, checked on the full uncapped list. Dropped: "stood in front of", "a finger's width", "back before the", "from behind his". Spoken-line echoes none. The command-echo candidate is unchanged (a false positive).
- Voice-bank content hits: 0.
- Every new string was grepped against Ch.1–21, the bible and voice-dna: "closed on him", "Rome watched", "I was thinking that", "while his clerk wrote", "the law gives", "heard all of them", "wanted trimming". All are first uses, and none touches a CLOSED or SPENT entry.
- **The real file was never touched** (md5 still `75b74801…`).

## Strengths to PRESERVE (do not touch in polish)
- **The 98-word opening spiral, verbatim.** "Felix … booted it over the verge and turned home for the mules."
- The widow's ancestors with "the yellow wax of somebody's nose"; Plautia's built hair; the stapled pot and "It belongs to the widow." / "So it does."
- Plautia's roof lines ("Of everything about him, that alone ever frightened me." / "He brought me." / "It is the only answer I have." / the veil instruction).
- The Thirtieth Street comparison; the water clock; Celer's "I've been practicing it on my steward"; the dyer's cloak and the seasick merchant's Nero; **the assessor's uncle** ("He'd have liked the extra months.").
- The night carts and "That's a heel," / "It's the shape of one."; "Look to the back … Talk to them." / "I'll talk to them," and the held sleeping sentence.
- **The name sequence l.192–196 complete**, the onion and "The court is not buying onions,"; the night told plain and "If she'd wanted out in the night she'd have had to step over me."
- **The sneeze, the Salve cascade, the sneezer's thanks, and the laugh paragraph complete**, then the attendant and **"and the curtain swung across it."**
- The steps: Myrrhine's cloak and shoes; "The judge saw, and he was asleep."; the 1991 board through **"This one still had the chisel in it…"**; Castor whole; the Vestal's ash and Ovid; "Nothing's given,".
- The gallery woman's "Oh, him."; "I watched the street." / "Who was on the roofs, and where the dogs were."; **the empty bench** (l.330).
- The boots and the dinner-foot; Plautia's night visit complete; "The shift was too long for me and I wore it anyway."
- The cramps and the lead; "He got it cheap, the emperor,"; the Argiletum and the ear.
- The verdict under the clapping; "The sixth?" / "With the rest."; the brother's "And a better chair."; the ladder; the Cornelian law and the foot; **"You never heard it,"**; the boy's formula and the dog; **the closing line, verbatim.**

## PATH TO 8.5 (mandatory; Floor is 7.5)
- **Characters 7.5 → 8.5 requires** the law cap removed, and nothing more.
  - Apply **F1a–F1d**: the judge's eyes go from 11 to 6, his speech beat from 3 to 1, and no three fall inside 500 words.
  - Apply **F2a–F2b**: Valens's narrated waiting goes from 5 to 3, and the explaining callback goes.
  - The uncapped evidence is already 8.5. Do not add character beats, and do not touch Myrrhine's lines; her quips are WATCH, not defects.
- **Prose & Voice (8.5, at the bar):**
  - Apply F3–F7 and F9–F13 so it holds there and stops collecting law findings.
  - The stopping sentence is already on the page ("This one still had the chisel in it…"). **Do not polish S4's name-and-sneeze run or the closing paragraph.**
  - 9.0 is reachable on re-evaluation if the fixes land clean.
- **Immersion / Hostile:** F8.

## Pacing check (one line for `feedback/progress.md`)
**OK.** Ch.21 was 6,800w in low gear (median 12) and closed on a reported question. Ch.22 is the high-gear peak the ledger planned:
- 7,179w (7,093 after fixes), 7 breaks, 36% dialogue, median 17;
- it opens on a 98-word spiral and closes on a plain spoken line.

Ch.23 drops to a single-scene 4,200w low-gear night, so the book moves fast (21) → long and wide (22) → slow and close (23). That is the right oscillation around the ~53% turn.

Inside the chapter the court sections run deliberate and the city sections wander, as the outline asks. The one soft stretch is S5–S7 (about 2,500 words between the climax and the verdict). It is earned by the judge's three days; do not pad it or cut it further.

The length is 5.5% under the 7,600 target, which is not a problem: never pad.

## Cross-Book Pattern Detection (Ch.1–22)
- **A walk-on's single trait, re-noted until it becomes his device.** This is now a pipeline fingerprint:
  - Ch.11 Valens's bare "No." ×11;
  - Ch.16 Felix's "Is it" ×10;
  - Ch.18 Pacuvius's "my ship" ×12;
  - Ch.22 the judge's shut eyes ×11.
  The phrase gates catch the verbal ones. **The narrated physical state is invisible to them.** Recommend at the root: the writer and dialogue-polish cap any single character's narrated trait or state at 3 per chapter, and the evaluator keeps counting by hand until `tic_report.py` can.
- **A repair swap that reinstates the problem the disruptor cut** (W-10 replaced the hiccups with a stretch, which put back the arena–child pairing). This is the same failure the evaluator spec warns about for the evaluator's own strings. The continuity repair should check its swaps against the disruptor's report as well as the at-risk list.
- **Mara's laugh channel:** the fifth shape is used here and well. All five laugh shapes are now spent, so the next Mara laugh needs an outline ruling before it is drafted.

## Bible sync (for the tracker; not the manuscript)
**At-risk after Ch.22** is still a writer-draft block. Sync it to the final page:
- "the small wetting" → **"sweated through my shift"** (C-02).
- Delete **"Walking behind a woman in the street, a man watches what's coming at her."**; it is not on the page (W-05). Add **"Who was on the roofs, and where the dogs were."**
- "Fabius's Parilia offer is left unanswered" → **refused in Ch.21; Valens is in Rome at the Parilia** (audit I-15).
- **Spoken lines to add as SPENT:**
  - "The sixth?" / "With the rest."
  - "Where's this gladiator?" / "The one standing still." / "Oh, him."
  - "It is given." / "Nothing's given,"
  - "That makes it a game."
  - "Laughing?" / "I didn't ask her."
  - "And a better chair."
  - "I would be grateful if nobody told me."
  - "The judge said salve."
  - "Your man has a carter's lungs."
- **New SPENT entries:**
  - the judge's shut eyes as a running beat (six survive F1);
  - the verdict under another court's applause;
  - Celer's foot on the step (the payoff of Valens's dinner read);
  - the empty bench seen from the gallery;
  - the boots set "toes outward";
  - Plautia's Egyptian-linen shift.
- **WATCH:**
  - Myrrhine's deflating quips (4 in this chapter; ≤2 in any later one);
  - Valens's waiting as a narrated beat (≤1 per chapter);
  - the arena thought never gets a body reply (F9).
- **Hiccups:** never on the page (W-10). Do not log them as used in Ch.22.
- **The chapter's header comment is stale:**
  - it says "77-word sensory sentence", but the opening is now 98 words;
  - it gives the pull as "EMOTIONAL / DECISION-free", but hook-craft typed it DECISION POINT.
  Header comments are not prose; the writer should refresh them at finalize.

## VERDICT
**POLISH. The gate is NOT MET at cycle 0.**
- Floor 7.5: Characters, under the law cap for the judge's shut eyes.
- Uncapped Floor 8.5.
- Casual 9.0. Pacing OK. Mechanical gates clean.

**PASS is expected after the tested 17-replacement fix set**, projected at Floor 8.5 / Average 8.71. The evaluator must confirm it on re-run.

**BIAS CHECK:** This evaluation was produced by the same system that wrote the prose. Confidence in scores above 8.0 requires external validation (beta readers, editors, comp analysis). Two judgement calls here could go the other way with a human editor:
- the judge's shut eyes could be read as a deliberate running gag rather than a tic;
- the unnamed laugh could be read as a few sentences of confusion rather than suspense.
I ruled the first under the author's no-tics law and left the second alone.

---

## Re-evaluation — cycle 1
**Evaluator:** book-evaluator (independent; did not write or revise this prose) | **Date:** 2026-10-23
**Text evaluated:** `manuscript/chapters/chapter-22.md`, md5 `6835a01ea73b60b54bb8e727eaf2b1e3`. This is exactly the tested cycle-0 result, so the fix set landed byte-for-byte as tested.
**Spec in force:** the evaluator spec as of commit `192cfa7`, which adds the **narrated-trait rule**: "more than 3 notes of the same state in one chapter, or 3 inside ~500 words, is a NO-TICS failure under Characters, even when `tic_report.py --gate` is clean." The cycle-0 fix set was designed against the gesture-class chapter cap (7). The new rule is stricter, so I recounted every recurring character by hand.

### HEADLINE
**CVI-Launch:** 9.6 | **CVI-Legacy:** 7.0 | **Genesis Floor:** **7.5** (Characters, still law-capped on the page) | **Genesis Average:** 8.64 | **Casual:** 9.0
**Gate: NOT MET.** Casual ✓, pacing ✓, mechanical gates ✓, but Floor is 7.5.
**This is not the +0.5 cap at work.** The page itself still fails the narrated-trait rule for four characters (below). A tested 11-replacement set clears all four.

### Measured on the real file
- `bash tools/check_chapter.sh 22`: **ALL MECHANICAL GATES CLEAN**.
  - Style: 7,095w (5b), simile 1.0/1k, em-dash 0, foreshadow 0. Show/tell: dialogue 36.2%.
  - Shape: `22 7093 7 36 17 long-spiral dialogue`. SHAPE CLEAN.
- `tic_report.py --gate`: clean. And-chains 5/9. Gesture classes are all under the cap.
- `--echoes 22`: 95. **Spoken-line echoes: none.** Command-echo candidate: 1, the same false positive as before ("Myrrhine says that I shook").

### Did the 17 cycle-0 fixes land, and did they plant anything?
**All 17 are on the page as tested** (l.24, 190, 208, 210, 218, 228, 238, 296, 298, 320, 324, 326, 328, 354, 370, 374, 400). **None planted a finding:**
- Echoes are a strict subset of the 99 before.
- Voice-bank hits: 0.
- F9's oxcart interruption reads clean, and the arena thought gets no body reply.
- F10's cut leaves the insinuation intact.
- F12 no longer counts the courts.
- No cut effect was restored, and no CLOSED or SPENT channel was touched.

### Narrated-trait count by hand (new rule: more than 3 per chapter, or 3 inside ~500 words, fails)
| Character | State | Notes on the current page | Verdict |
|---|---|---|---|
| The judge | eyes shut / asleep | 1. l.82 "listened with closed eyes … took him to be asleep"<br>2. l.130 "the judge's eyes opened again"<br>3. l.176 "The judge keeps his eyes shut." (Valens)<br>4. l.240 "eyes still closed, said it"<br>5. l.262 "he was asleep" (Myrrhine)<br>6. l.398 "without opening his eyes for it" | **6. FAIL.** F1 halved it from 11; the new rule needs 3. |
| Myrrhine | barefoot / shoes off | 1. l.258 takes off both shoes<br>2. l.266 "worked her toes on the warm marble"<br>3. l.280 "She stood, holding her shoes."<br>4. l.292 "barefoot, with her red shoes in her hand"<br>5. l.380 "She was barefoot again; the red shoes hung from her wrist"<br>6. l.386 "walked the whole of it barefoot" | **6. FAIL.** This is a running state, not a plant-and-payoff. |
| Valens | waiting | 1. l.84 "Valens waited with the witnesses"<br>2. l.244 "and waited while the court finished"<br>3. l.266 "He stood and waited for the bench to stop."<br>4. l.266 "He's good at waiting, that one." | **4. FAIL.** |
| Valens | standing still (S6) | 1. l.298 "Valens had not moved from his place."<br>2. l.302 "The one standing still."<br>3. l.320 "He stood with his arms hanging"<br>4. l.330 "He stood looking at them" | **3 narrated plus 1 spoken inside ~450 words. FAIL.** |
| Plautia | stillness | 1. l.22 "kept her place"<br>2. l.84 "none of her stillness"<br>3. l.246 "went stiller than she already was"<br>4. l.406 "did not move until he had stood" | **4. FAIL** (narrowly). |
| Celer | talking | 1. l.86 "all talking"<br>2. l.416 "still talking"<br>3. l.418 "without once losing the thread" | 3. At the limit; OK. |
| Celer's advocate | the hand | 1. l.96<br>2. l.298<br>3. l.328 | 3. At the limit; OK. |
| Plautia | veil fringe | 1. l.76 instruction<br>2. l.198<br>3. l.230<br>4. l.406<br>5. l.436 payoff | Plant → wind → release → the boy holds it. A designed prop arc with a payoff, not a re-noted state. OK. |
| Valens | boots | l.344 / l.348 / l.352: three handlings in ~70 words, all as speech beats | The gate's prop verbs miss "unlaced" and "pulled". The cast rule's spirit ("the prop does the acting") applies. **WATCH**; trimmed in the set below. |

**Characters therefore stays capped at 7.5 on the page.**
- The uncapped evidence is unchanged at 8.5: Plautia's roof and night lines, "Who was on the roofs, and where the dogs were.", Celer's foot, the assessor's uncle, 14 speakers who pass cover-the-name, Mara's chaos 4/4 inhabited.
- The cycle-0 F1/F2 work was real (judge 11 → 6). It aimed at the old cap.

### Genesis Score (cycle 1)
| Dimension | c0 | c1 | Evidence / reason |
|---|---|---|---|
| Originality | 8.5 | **8.5** | Unchanged. The climax is refused by the sneeze, and the verdict lands under another court's applause. The forgery tell is still familiar. |
| Theme | 9.0 | **9.0** | Unchanged. "and the man next to him said the name back." / "Nobody said the name of the witness." |
| Characters | 7.5 | **7.5** | Law cap. Narrated-trait rule failed ×4 (table above). Uncapped 8.5. |
| Prose & Voice | 8.5 | **9.0** (+0.5, the cycle maximum) | Every cited hold is cleared: the voice-bank lift (F3), the adverb tag (F6), "the law allows" ×2 (F7), the false superlative (F8), the arena–child pairing (F9), the courtroom cliché (F10), the counting run (F12). The close-the-book sentence is intact: "This one still had the chisel in it, and my fingertips came away from its cups gray with grit." The laugh paragraph still enacts the breakdown. #11 is now 3 (0.42/1k). ≥9.0 challenge: at the sentence level this outwrites the comp (*Outlander*) and holds its own in a historical-literary lane (Mantel's court scenes), so 9.0 stands. |
| Pacing | 8.5 | **8.5** | Unchanged. The S5–S7 slow run is earned. 7,093w, 7 breaks, 36%. |
| Emotion | 9.0 | **9.0** | Unchanged. The anchor (the name thrown to the back), the surprise (the laugh at the sneeze, body-only), the empty bench. |
| Immersion | 9.0 | **9.0** | F8 cleared its one named hold. I am not raising it to 9.5: "the lead fumed white and sweet-smelling" is still the Hostile's open query, and 9.5 is the practical ceiling. |
| **FLOOR** | 7.5 | **7.5** | Characters (law) |
| **AVERAGE** | 8.57 | **8.64** | |

### Anti-AI scan (current page)
**6/20 patterns, −1.0. Clean band.**
- #1 minor (2).
- #3 moderate (5, three of them designed).
- #11 minor (3): "from his manner, this was his daily work"; "for the wax had darkened since Corinth"; "because four courts sat in it at once".
- #13 minor.
- #16 moderate (4, all in speech).
- #17 minor.
- #8 and #15 have cleared.

### Laws (current page)
- **No foreshadowing: PASS.** The gate count is 0. All 14 "would" and 10 "never" are in-scene or past-facing.
- **NO TICS: phrase and gesture gates PASS; the narrated-trait hand count FAILS** (table above).
- **Retired reflexes: PASS.**
- **No reused spoken lines: PASS**, with one frame finding. Myrrhine's "Who pays for all that?" rebuilds the Ch.7 working woman's "Who pays for a pot that's broken?", which the bible logs as spent. That is the same question frame on the same class of speaker. The gate cannot see a frame, so I fixed it in the set below.
- **Not "the nine", no "citizen", unnamed brother, laugh never through the mouth, em-dash 0: PASS.**

### Readers (deltas only)
- **Casual: 9.0, unchanged.** The fixes are invisible to this reader.
- **Critic:** the "behind his eyelids" wink is gone. What they still notice is Myrrhine's shoes coming off, being held, swinging from her wrist and being walked barefoot, six times.
- **Hostile:** nothing new. The lead smell is still INVESTIGATE.
- **Devoted:** they would still catch the judge's eyes re-noted at the verdict.

### CVI
- **CVI-Launch: 9.6**, inputs unchanged: 0.2×8.5 + 0.2×10 + 0.2×9 + 0.2×8.0 + 0.1×10 + 0.1×10 = 9.1, plus 0.5 for a strong anchor.
- **CVI-Legacy: 7.0**: 8.5×.30 + 9.0×.25 + 3×.20 + 7×.15 + 5×.10 = 6.95.

### What remains between the chapter and 8.5
- **Characters 7.5 → 8.5:** only the four narrated-trait failures above, plus the boots as a WATCH. Nothing else on the page holds Characters down; the uncapped evidence is 8.5. Apply the tested set below. **After it, recommend NO further text changes for Characters.** Do not add character beats, and do not touch Myrrhine's three surviving quips.
  - Once the set is applied, only the per-cycle cap stands between Characters and 8.5. The orchestrator's +0.5 rule would score it 8.0 at cycle 2 and 8.5 at cycle 3, with no edits in between.
  - Spec rule 2 permits a jump above 0.5 when 3+ improvements are cited, and this set cites 11. Invoking it is the orchestrator's decision, not mine.
- **No other dimension is below 8.5.** Originality and Pacing sit exactly at the bar and need no work. Prose: no further text changes.

### Tested fix set (cycle 1)
**Script:** `/tmp/claude-0/-home-user/63791ee5-159c-5791-9429-07920f8d9417/scratchpad/fixes22b/apply_fixes.py`
- Run it from the book folder: `python3 <script> manuscript/chapters/chapter-22.md`.
- Every old string must match exactly once, or nothing is written.
- It contains 11 replacements, all cuts or one-for-one swaps.

| ID | Now | After | Count it fixes |
|---|---|---|---|
| G1 | "and the judge's eyes opened again." | "and the judge sat forward." | judge |
| G2 | "The judge keeps his eyes shut. And Celer sat on his left today, with the light behind him." | "Celer sat on his left today, with the light behind him." ("You need not look at him at all" now points at Celer.) | judge |
| G3 | "…on the dowry's earrings, and without opening his eyes for it." | "…on the dowry's earrings." | judge 6 → 3 (l.82 intro, the Salve, "he was asleep") |
| V1 | "Valens waited with the witnesses along the pier." | "Valens was along the pier with the witnesses." | waiting |
| V2 | "He stood and waited for the bench to stop. He's good at waiting, that one. I was holding you up; I'd only an eye for you." She worked her toes on the warm marble. "She was shaking too," | "I was holding you up; I'd only an eye for you. She was shaking too," | waiting 4 → 1; toes; Myrrhine's quips 4 → 3 |
| V3 | "Valens had not moved from his place. Celer's advocate had closed on him," | "Celer's advocate had closed on Valens," | stillness |
| V4 | "Valens let the question go by. He stood with his arms hanging and his gaze at the aisle's end," | "Valens let the question go by, his gaze at the aisle's end," | stillness 4 → 2 |
| M1 | "She stood, holding her shoes." | "She stood." | barefoot |
| M2 | "…I've seen them." She was barefoot again; the red shoes hung from her wrist by their laces. "Who pays for all that?" / "The emperor. Out of Judaea." | "…I've seen them. Whose money is it?" / "The emperor's. Out of Judaea." | barefoot 6 → 3 (off, the S5 exit, the Argiletum); retires the Ch.7 frame |
| P1 | "and rose. Plautia did not move until he had stood, and then she stood up beside him, and I saw" | "and rose, and his sister after him, and I saw" | Plautia stillness 4 → 3 |
| B1 | "What they asked." He pulled the boot off. "The cook's freedman" | "What they asked. The cook's freedman" | boots 3 → 2 |

**Tested on** `/tmp/claude-0/-home-user/63791ee5-159c-5791-9429-07920f8d9417/scratchpad/reeval22/books/the-hour-of-ash/` (md5 after `251a664c923a7fb858da4b46ec8c3d55`).
- `check_chapter.sh 22`: **ALL MECHANICAL GATES CLEAN**. Dialogue **36.3%** (≥35 ✓). Tic gate clean; and-chains 6/9 (P1 adds one). Shape: `22 7008 7 36 17 long-spiral dialogue`, SHAPE CLEAN.
- `--echoes 22`, full uncapped list: 95 → **93, a strict subset**. Dropped: "stood holding her" and "the judge the judge". Spoken-line echoes: none.
- **One string was rejected in testing:** "Plautia stood up after him" planted "plautia stood up", a Ch.17 echo. It was replaced by "and his sister after him".
- Every new string was grepped against Ch.1–21, the bible, voice-dna and the voice bank: "the judge sat forward", "was along the pier", "Whose money is it?", "The emperor's.", "his sister after him", "closed on Valens". All are first uses, and none touches a CLOSED or SPENT entry.
- **Protected beats untouched:** the Salve cascade; "The judge saw, and he was asleep."; "The one standing still." / "Oh, him."; the empty bench; the S5 exit with the red shoes; the boots "toes outward".
- **The real file was not touched** (md5 still `6835a01e…`).

**Projected after the set:** Characters is uncapped (8.5 on the evidence; 8.0 under the +0.5 cap). Floor 8.0 or 8.5, Average 8.71 or 8.79. Casual 9.0.

**Bible sync (for finalize):**
- Add the spent frame "Who pays for …?" (Ch.7; Ch.22 retired).
- WATCH: Myrrhine barefoot ≤3 per chapter.
- The chapter's header comment is still stale (it says 77-word opening and EMOTIONAL pull). Refresh it at finalize.

### VERDICT (cycle 1)
**POLISH.** Floor 7.5 (Characters, the narrated-trait law, failed on the page ×4). Casual 9.0. Pacing OK. Gates clean.

Apply `fixes22b/apply_fixes.py` and re-run E+F. After that set, no dimension has anything on the page holding it below 8.5. Only the per-cycle cap remains, and no further text changes are recommended.

**BIAS CHECK:** This evaluation was produced by the same system that wrote the prose. Confidence in scores above 8.0 requires external validation (beta readers, editors, comp analysis). One judgement call could go the other way: I counted spoken mentions (Valens's "eyes shut", Myrrhine's "good at waiting") as notes of the state. The cycle-0 count did the same. Counting narration only would put the judge at 4, which still fails.
