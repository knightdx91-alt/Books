# Evaluation: Chapter 21 — The Wolf's Old Name (run 2)
**Evaluator:** book-evaluator (independent; did not write or revise this prose) | **Date:** 2026-10-22
**Text evaluated:** `manuscript/chapters/chapter-21.md` (md5 `86becc02d312e9337ffd7f52cdcdba81`), the page after writer → dialogue-polish → hook-craft → disruptor → continuity repair (C-01…C-04, W-01…W-19, I-02/04/06/08/09). **6,869 words** (shape_check; 7,225 `wc -w` with the header comments); dialogue **42%** (shape) / 41.9% (show_tell); median sentence 12; 3 breaks / 4 sections; `dialogue` → `question`.

**Read against:** the book's CLAUDE.md; STATE.yaml `guardrails`, the retired reflexes and AUTHOR-CP3-1…5, CP4-1/2, END-1; outline ledger row 21 and `## Chapter 21` (plus Ch.20, Ch.22 for the handoffs); voice-dna §0, §1 (gear, voice under pressure), §3b; character-bible.md (the Nicanor and Fabius cards, the Ch.21 walk-on block, the laugh-channel rulings after Ch.8 and Ch.14, the "could not stop" ruling after Ch.15, **At-risk after Ch.20** in full); chapter-20.md (whole ending), Ch.12 and Ch.16–18 at the points the scans hit; `evaluations/dialogue-chapter-21.md`, `hook-chapter-21.md`, `disruption-chapter-21.md`, `continuity/chapter-21-audit.md` **with its repair log** (I do not re-raise anything it fixed); `evaluations/chapter-20-eval.md` for the bar and format.

**Genre profile:** commercial historical romance / time-slip (comp *Outlander*). Anti-AI band commercial (0–8 clean). #11 cap >6 or >0.8/1k. Dimension 7 = **IMMERSION**. Engagement (book) empathy 55 / fascination 30 / self-insertion 15; this chapter leans **fascination** harder than Ch.20 (the arena, the name), with empathy carried by Felix.

**Measured on the real file** (from the book folder):
- `bash tools/check_chapter.sh 21`: **ALL MECHANICAL GATES CLEAN** (style clean, foreshadow 0; grammar 0; rhythm 0; show/tell no flags, dlg 42%; voice-wear strict clean; tic gate clean; metaphor 1.3 fig/1k, median 12; shape CLEAN).
- `tic_report.py --gate`: clean. And-chains 4/9, credential asides 0, negation pivots 1/1, 'So' 0; every gesture class under cap (I use the gate's numbers).
- `tic_report.py --echoes 21`: 56 advisory echoes; **command echoes none; spoken-line echoes none.**

**My own scans (scratch only):** 4-grams of Ch.21 against all 13 voice-bank samples (stop-word-bounded); hand greps of every short spoken line (≤4 words) against Ch.1–20; narration-only scans for forward reach (would / last / never / since / years / still), "the last of", hair/arm residue frames, laughs, "could not"; per-section narration medians (S1 12 · S2 13 · S3 11 · S4 11.5; Ch.20 narration 14, Ch.19 18); last lines of Ch.1–20 against the close.

*(l.N = line number in the current `chapter-21.md`.)*

---

## HEADLINE
**CVI-Launch:** **9.5** (9.0 + 0.5 strong anchor) | **CVI-Legacy:** 6.8 (provisional) | **Genesis Floor:** **8.0** | **Genesis Average:** **8.50** | **Casual Reader:** **9.0**
**Engagement type:** Fascination (the herald, the name rolling round the bowl, the offer) → Empathy (Felix and the palm; the scrubbed hand) → Self-insertion (a street that knows your business and brings you eggs).
**Divergence alert:** none (CVI-L above Floor by 1.5, the right direction for a crowd-pleasing chapter held back by book law).

**Gate (Floor ≥ 8.5 AND Casual ≥ 8.5 AND pacing OK): NOT MET at cycle 0.**
- Casual 9.0 ✓ · pacing OK ✓ (judged below) · mechanical gates clean ✓.
- **Prose & Voice holds the Floor at 8.0, on merit, no cap.** The sentences are 8.5 and better. What holds them is a **reuse-and-law cluster no gate can see**:
  1. **Mara's body rebels on three retired / reserved channels:**
     - **l.90, the laugh at the burned tread** ("That was when I began to laugh, and he waited … until I was done"). The bible maps Mara's next laugh to **Ch.22's fit** ("nothing like the pen before then", after Ch.8; "Ch.22's fit … must find a fifth", after Ch.14). The audit's W-06 shrank the rendering but kept the event, so a full laugh still lands one chapter before the mapped one. Its words are also **sample-09's** ("began to laugh and could not stop").
     - **l.360, "My face was doing something I could not stop."** "`could not stop` for a laugh: SPENT (Ch.15; sample-09's frame)."
     - **l.404, "I heard my voice go up, and could not bring it down."** The voice as body-reaction channel is RETIRED ("voice stays retired", At-risk after Ch.20).
  2. **Valens's entrance rebuilds Ch.18's proposal staging.** l.52 "He had sand in the hairs of his forearms and something in his hand." against Ch.18 l.71 "Valens faced me with flour dried white in the hair of his forearms and the crown hanging from his hand." Ch.20's cycle 0 cut a version of this same frame ("shavings of bone in the hair of his arms"). Ch.21 then puts the cut shape back at l.90: "**oak shavings in his hair**" (also Ch.20 l.283's turner, "a curl of bone caught in his hair"). That is two residue-in-hair beats for Valens in one chapter, in a frame closed last chapter.
  3. **A voice-bank frame:** l.134 "…turn your foot," Valens said, **beside me in the black.** against sample-13's "…Valens said, **beside me at the rail.**"
  4. **Felix's silence narrated four times in S2:** "His legs stopped." (l.196, inhabited, keep) / "Felix slid down, **wordless**." (l.204) / "**looking at nothing**" (l.282) / "and he asked not one thing." (l.296, the section close, keep). The audit cut the S1 one (W-07). The middle two turn an enacted silence into a reported one.
- **The fix set: 11 swaps, tested together on a scratch copy** (script below). All are cuts or even swaps. No sentence is added except one six-word narration line that *replaces* l.404's voice sentence.
  - After: **6,820 words** (shape), dialogue **42%** (shape) / 42.2% (show_tell), median 12; `dialogue` → `question`; 3 breaks.
  - `check_chapter.sh 21`: ALL MECHANICAL GATES CLEAN. Tic gate clean. Shape CLEAN.
  - `--echoes 21`: 56 → **55**, no new echo; command / spoken-line echoes none / none. Voice-bank 4-gram hits 2 → **0**.
  - **Byte-identical after the fixes:** the opening burst; "I ate the cheese. It sat."; "Who knows?"; the stair and "It'll take the both of you."; the tablet and Plautia's four lines; "All my palm found was supper."; the whole Nicanor heel scene; the herald, the hand, "Then he gripped the back of Felix's tunic with that hand and sat him down."; the egg; "No," said Valens; "Lupus died in Asia"; "The fish faces the wrong way,"; the washed hand; the freedman's fat Lupus; Grata's flood; Felix's gate speech; the closing paragraph.

---

## Genesis Score (Craft Assessment, cycle 0)

| Dimension | Score | Evidence | Cap reasons |
|-----------|-------|----------|-------------|
| Originality | **8.5** | The genre beat (retired fighter pulled back for one last bout) is refused, and fame arrives sideways: a herald's puff, a boy's fan graffito, a stranger's warm egg. Recognition by **the heel**, not the face or the scar: "Heel, and then the weight." (l.194). The critic's line where the emotion should be: "**The fish faces the wrong way,**" he said. (l.292). The freedman's Lupus who became "fat" and keeps a cookshop (l.320). | Not 9.0: this is the book's 4th stranger-reads-Valens beat (planned, WATCH at 3), and the summons is a functional letter. |
| Theme | **8.5** | "Home where no one knows you, or where you are known" is staged twice over: the street knows the pregnancy before Valens does ("The baker's boy says the carter says Grata says.", l.138) as the bowl knows Lupus before Fabius does. Never stated in narration. Texture is real and non-thematic (the comb and the dog, the cushion wife, the sausage, the heartburn). The close turns the theme into a question for the child: "…and asked him what he had been?" Mara's own exposure stays unspoken: "I had a name in a clerk's book at Delphi … I told him none of it" (l.428). | Not 9.0: the argument says its two positions nearly in the theme's words ("You can be nobody in Pompeii…" / "be believed"); the outline's subtext layer (does she need him to be *somebody*) stays under the surface only in "You weren't there." / "I believe you anyway." |
| Characters | **8.5** | **Valens:** "Who knows?" as his first answer to the child (l.62); love as carpentry ("It'll take the both of you."); the hand that rises unbidden and the hand that sits Felix down; the back "as straight as a post" he keeps letting down (l.294); "My hand went up to them. I hadn't told it to." The mind-reading of Grata is played straight and is funny ("She was looking for the place to start."). **Felix:** bear-burst, then "His legs stopped.", then the gate: "He'll get tired of saying it before I get tired of hearing it." **Grata:** 0 questions; the fourth touch (the shoulder, "and let her hand stay on it after the sand was gone"); the pearls "for the baths". **Nicanor:** verdicts and a prediction that fails. **The freedman** has his own story. Cover-the-name PASS for all six speakers. Chaos 4/4 for Mara (below). | **No cap** (gate clean; no tic). **Held at 8.5 by:** Felix's silence narrated ×4 in S2 (→ F6, F7); Grata's men-in-general lines ×2 here after ×2 in Ch.20 (WATCH, not changed). |
| Prose & Voice | **8.0** | Underlines: "I ate the cheese. It sat." (l.40) · "All my palm found was supper." (l.132) · "It was boiled, and still warm from being sat on in her basket." (l.244) · "He dried it and looked at it, and plunged it again." (l.300, **the close-the-book sentence**) · "Lupus died in Asia," said Valens. "Or drowned off Kenchreai. Ask Nicanor." · "No. I was not there. I believe you anyway." Ugly sentence present ("The baker's boy says the carter says Grata says."). Voice under pressure: the arena section narrows to what Mara refuses to watch ("I did not watch that. I watched the girl beside me unwrap a sausage"), inhabited. | **Held at 8.0 by the cluster above** (three retired/reserved body channels; the Ch.18 staging rebuilt plus the Ch.20-cut hair frame; a sample-13 frame; Felix's silence reported). No cap applies; #11 PASS (0.44/1k). |
| Pacing | **8.5** | Opens in a burst ("And a bear, a live one…"), lands the summons at ~20%, alternates rooms as the ledger asks, and every section exit pulls (S2→S3 "he asked not one thing"; S3→S4 Grata laughing after Valens has misread her). Value shift: positive (a child; a street that brings eggs) → negative and open (Felix at the gate with a nail; Rome undecided, the Ides running). Speed varies inside the chapter: S2 holds 17 sentences ≥30 words (the crowd), S3/S4 run clipped. | Gear judged below; it serves. |
| Emotion | **8.5** | **Anchor:** the palm branch scratched by the barracks gate, "He had cut the stem twice over, so that it sank deeper." (l.466), and Mara's fingertip in it, "the white came away on my skin" (l.502). **Surprise** (outline: fame flatters him and he hates it): the hand rising "as high as his ear", then the scrubbing "well past what the dust of one day needed". **Body rebel:** Valens's hand ("I hadn't told it to."). Techniques: physical, comedy-in-dread (the cushion wife during the fight), object (egg, tread, palm), withheld speech (Felix). | Not 9.0: Mara's own rebels are on spent channels (l.90, l.360, l.404); the fix gives her one clean one (the mouth that will not behave). |
| Immersion | **9.0** | The amphitheater as a working building: bone seat tokens strung at Felix's throat; the lane "between the palaestra wall and the vineyards"; the north passage; women in the top ring "the law said so"; the water organ "that wheezed and caught"; *missio* by finger and the palm and the thrown purse; the quadriporticus walled up into barracks "before the earthquake"; Falernian as the whole street's gift. Every detail is used or suffered. | — |
| **FLOOR** | **8.0** | | Prose & Voice |
| **AVERAGE** | **8.50** | | |

---

## CVI-Launch Breakdown

| Input | Score | Evidence |
|-------|-------|----------|
| Commercial Pacing | 8.5/10 | Short chapter for this book, 42% dialogue, a bear on line one, an open question on the last. |
| Tomorrow Test | 4+ anchors → 10 | IMAGE: Felix's palm at the gate; the scrubbed hand; the warm egg. QUOTE: "The fish faces the wrong way."; "Lupus died in Asia … Ask Nicanor." |
| Casual Reader | 9.0/10 | See report. |
| Shareability (quote/plot/emotional) | 4 / 3 / 4 (→ 8/6/8; 0.6×8 + 0.4×7.33 = **7.7**) | "The fish faces the wrong way"; the gladiator outed by a cheering arena who says no; the boy with the nail. |
| Concept Pitch | yes (10) | "A retired gladiator is recognized by a cheering crowd the week his wife tells him she's pregnant, and has to decide whether to give his real name in a Roman court." |
| Human Closeness | yes (10) | Marriage, a child coming, a foster son, a landlady. |

**CVI-L = 0.2×8.5 + 0.2×10 + 0.2×9 + 0.2×7.7 + 0.1×10 + 0.1×10 = 9.0, +0.5 strong anchor = 9.5.**
**CVI-Legacy (provisional):** Originality 8.5×0.30 + Theme 8.5×0.25 + Cultural vocabulary 3×0.20 + Re-readability 7×0.15 (the closing question changes on a re-read, given Lucius's age in 79) + Identity 5×0.10 = **6.8**.

---

## Anti-AI Scan (20 patterns; per 1,000 words at 6.87k; commercial band)

| # | Pattern | Result | Count · density | Citation |
|---|---|---|---|---|
| 1 | Forced symmetry | Found, minor | 2 · 0.29 | "It'll want teeth before it wants a bowl" / "I'll keep the bowl till it's got them."; "He'll get tired of saying it before I get tired of hearing it." Both characterful. −0.125 |
| 2 | Empty poetic vocabulary | Clear | 0 | |
| 3 | Automatic rule of three | Found, moderate | 5 · 0.73 | "on ice, and in snow, and on the deck" (l.192, → F5); "before a judge, and Celer's advocate, and every idler" (l.382); "the length of the road, and through the gate, and as far as our door" (l.296, the designed held sentence; kept); "his face and his nape and his forearms" (l.300); the rim chorus (3 voices, kept). No anaphora triad. −0.25 |
| 4 | Em dashes | Clear | 0 | |
| 5 | Empty metaphors | Clear | 0 | |
| 6 | Dramatic "And" openings | Clear | 0 in narration | Speech "And…" rejoinders are natural turn-taking. |
| 7 | Pseudo-philosophical closings | Clear | 0 | No section or chapter closes on a maxim. |
| 8 | Excessive parallelism | Clear | 1 | Mara's "You can … Or you can…" (l.404) is argument, once. |
| 9 | Overly smooth transitions | Clear | — | S1's time markers are chronological and plain. |
| 10 | Described emotions | Clear | 0 | "The pleasure in him stayed round his eyes" is externalized. |
| 11 | Explanatory extension | Found, minor | 3 firm · 0.44 | "because from here they could see who sat beside whom" (l.218, comic, keep); "the way the pair on the sand had held their hands up" (l.234, needed); "I had watched him do the same on ice…" (l.192). −0.125. **Commercial cap PASS.** |
| 12 | Binary negation opener | Clear | 0 | |
| 13 | Precision flex | Found, minor | 3 · 0.44 | "Twenty-six days." (Felix, in character); "Four lines since Corinth." (Plautia, earned); the sums (plot). No counting device. −0.125 |
| 14 | Emotional control demonstration | Found, minor | 1 · 0.15 | "I turned it to the lamp until it behaved." (l.360; comic, and it survives F10 in a lighter form). −0.125 |
| 15 | Authoritative description | Clear | — | "The walls round it were painted with things I had no time to look at" leaves the gap. |
| 16 | Philosophical asides | Found, minor | 3 · 0.44 | Mara "Men who have lost do not come looking. They go home and dine."; Valens "Slavers say what sells."; Grata "They come back when it's money." All in speech, in character. −0.125 |
| 17 | Clean dialogue | Found, minor | S3 volley | The curtain argument runs in clean one- and two-line turns (l.362–428); Felix's interruption is what breaks it. −0.125 |
| 18 | Thematic echo chamber | Clear | — | Comb, dog, cushion, sausage, heartburn: real noise. |
| 19 | Graduated reveal | Clear | — | Not the establish → anomaly → escalate shape. |
| 20 | Emotional temperature report | Clear | 0 | |

**7/20 patterns, −1.0. Clean band (commercial 0–8).** #11 hard check PASS.

## The book's own laws
- **NO FORESHADOWING: PASS.** Narration scanned for would / last / never / since / years / still: every hit is past-facing or in-scene ("the child was due in the summer"; "He was taller than me now, I saw, and had been for some time."). "When it was grown" is Valens's question in the scene; the irony is the reader's own Vesuvius knowledge, which voice-dna §0 keeps. No mountain, no AD 79, families A–E clean, gate 0.
- **NO TICS: PASS on the gate; four by-hand findings** (the cluster above). No phrase reaches 3 book-wide. Gesture classes clean.
- **Retired reflexes: PASS.** No significance-tagging, no negation opener, no anaphora triad, no performed candour, no device as a button, no closing aphorism.
- **No spoken line reused: PASS.** Gate none; every ≤4-word spoken line grepped by hand ("So I see.", "You did.", "I have.", "In the mornings.", "To whom?", "You have a mouth.", "It's a stair,", "Who knows?"): all first uses.
- **CP3-3 (gap unremarked): PASS.** **CP4-1 (children's status): PASS**, untouched. **CP4-2: PASS.** The summons comes by the Puteoli board via the lime carter; no tomb, no door on the page.
- **Outline warnings: PASS.** No arena fight set up for Valens (Nicanor's "with a beard" is about Felix); no speech about honor; the closing question is open, not rhetorical.
- **Mapped laugh / voice channels: FAIL at cycle 0** (l.90, l.360, l.404). F2, F10 and F11 fix it.

## Character Chaos Check (Primary: Mara)
- Irrelevant thought: **present, inhabited.** The heartburn and her made-up Latin for it, "the fire under the bone", on the walk to fetch Felix (l.436); the comb boy's dog.
- Cognitive distortion: **present.** She reads the summons as Plautia's wish and is corrected ("She wants you. Her brother wants me."); she tallies the purse against a year's carting.
- Unprompted memory: **present, triggered and returned.** The cumin brings back her father's stove (l.28). Her palm on her stomach brings back the maternity floor (l.132), cut off at a smell. Two sentence-scale memories, no fixed cadence (Ch.20 had one clause).
- Failed emotional management: **present**, but on spent channels at cycle 0 (laugh, "could not stop", voice). After F10: "turned to the lamp until my mouth behaved."
- Voice under pressure: **demonstrated** at the fight (refusing to watch, narrowing to the girl's sausage).

## Secondary Character Chaos
- **Felix:** has his own moments (the bear, the bowl for the baby, the palm and the nail).
- **Grata:** has her own (the earrings, the Falernian "paid for by the whole street", the hand left in the air).
- **Nicanor:** has his own (the rumors of dead pupils; the prediction that fails; "He eats my porter's bread.").
- **Fabius's freedman:** has his own (the father who laughed and then sold him; "I went in once.").
- **No secondary character is only a prop.**

## The Tomorrow Test
**What the reader remembers:** Felix under the barracks lamp with a nail, cutting the stem of a palm branch twice so it sinks deeper, the only name he can write. Close behind it: Valens at the basin scrubbing the hand that went up, and "The fish faces the wrong way."
**Anchor type:** BOTH (image + quote). **Verdict:** ANCHOR EXISTS. It is a different type from Ch.20's (a mended object handed back), so no anchor-type repeat.

## The Shareability Test
"He gets recognized at the games, the whole arena chants his old name, his hand goes up on its own, and that night he scrubs it." Text-able. **3 shareable moments in the last two chapters; the book is well over the minimum.**

---

## Reader Reports

### The Devourer (6.9k after 8.2k and 7.8k)
Relief. The shortest, fastest chapter of the run, opening on a bear. They race the arena section and Fabius's offer. They might skim the comb boy (l.42–50), but it is 150 words and funny. They never stop: S2 ends on Felix's silence and S4 on a question that drags them into Ch.22. **No stop point.**

### The Critic
Underlines: "I ate the cheese. It sat."; "All my palm found was supper."; the egg "still warm from being sat on"; "He dried it and looked at it, and plunged it again."; "No. I was not there. I believe you anyway."
Disappointments:
- Valens arrives dusted like the Ch.18 proposal, and is shaved again an hour later (l.52, l.90).
- Mara laughs at the tread a chapter before the book's big laugh.
- "My face was doing something I could not stop" is a phrase this book has already spent.
- The argument states its positions a little too cleanly before Felix's blanket breaks it.

### The Hostile
- **l.288 "where the boy had been jostled":** which boy? The definite article reads as Felix, who was on the benches and cannot write. → F8.
- **"a baker's boy" twice as town crier** (l.136, l.302). → F9.
- **The reported-question close is a frame reused from Ch.16**, which also ended on someone's question to Mara about Valens standing up in Rome. It works, and I am not changing it, but it is now CLOSED.
- **The amounts are fine:** 1,500 HS earnest ≈ a year's carting.
- **The timeline is fine:** two missed mornings plus the third = "Three days".
- **Nothing to challenge in the arena history.**

### The Casual Reader (airport, 10 pages)
They stay for the bear, for Grata ("he'd sell his mother's secrets to a mule for a carrot"), and for a husband whose first words on hearing about the baby are "Who knows?", who then goes upstairs at night to replace the stair she might fall on. That is the book's whole promise in ten pages: a hard man who loves with his hands. Then a stadium chants his name. They'd buy it. **9.0.**

### The Devoted Reader (active: long saga)
They will catch "Four lines since Corinth" (Plautia counting his letters), "You'll curse that stair" (Ch.20) paid by the tread, "Felix thinks I can't read" kept alive, and the closing question about a child who will be five in 79. That last one is the line the Reddit post gets written about. They will also notice that Valens arrives with residue in his arm hair, as he did at the proposal.

## Cross-Reader Matrix

| Issue | Devourer | Critic | Hostile | Casual | Devoted | Severity |
|---|---|---|---|---|---|---|
| Mara's laugh / "could not stop" / voice on spent channels (l.90, 360, 404) | | ✓ | | | ✓ | SHOULD FIX (book law: blocking) |
| Hair/arm residue staging rebuilt (l.52, l.90) | | ✓ | | | ✓ | SHOULD FIX |
| Felix's silence reported ×4 in S2 | | ✓ | | | | INVESTIGATE |
| "the boy" antecedent (l.288) | | | ✓ | | | INVESTIGATE |
| sample-13 frame (l.134) | | ✓ | | | | INVESTIGATE (voice-bank law) |
| Argument states theme cleanly | | ✓ | | | | INVESTIGATE (not changed) |
| No Casual-only flag | | | | — | | — |

---

## Revision Recommendations (Ranked)

| ID | Location | Problem type | What happens now | Why it fails | Revision direction | Project rule? |
|---|---|---|---|---|---|---|
| F2 | l.90 | Style / Character | "That was when I began to laugh, and he waited with oak shavings in his hair and looked at me until I was done." | Pre-spends Ch.22's mapped laugh; sample-09's words; a hair-residue beat | "There was oak dust all down his sleeves, and he caught me watching him." "It's a stair," still answers her look. | Yes: no Mara laugh before Ch.22's fit |
| F10 | l.360 | Style | "My face was doing something I could not stop. I turned it to the lamp until it behaved." | "could not stop" for a laugh is SPENT | "…very carefully, and turned to the lamp until my mouth behaved." | — |
| F11 | l.404 | Style / Voice | "I heard my voice go up, and could not bring it down." | The voice channel is retired | "Beyond the curtain Felix stopped turning over." The loudness is shown by the listener and sets up "I'm not listening." | Yes: show Mara's loudness by its effect |
| F1 | l.52 | Style | "He had sand in the hairs of his forearms and something in his hand." | Rebuilds Ch.18 l.71's proposal staging; the frame was cut in Ch.20 | "Valens stood in the opening with the last light on his back and something in his hand." | Yes: residue in Valens's hair/arm hair CLOSED |
| F3 | l.134 | Style | "Valens said, beside me in the black." | sample-13's "Valens said, beside me at the rail." | "Valens said." | — |
| F6 / F7 | l.204, l.282 | Character | "Felix slid down, wordless." / "and looking at nothing." | The enacted silence is reported twice between "His legs stopped." and "he asked not one thing" | Cut both glosses. | Yes: Felix's silence is shown, never labelled |
| F8 | l.288 | Logic | "where the boy had been jostled" | "the boy" reads as Felix, who cannot write | "where whoever cut it had been jostled" | — |
| F9 | l.302 | Continuity / Style | "and a baker's boy ran after him" | The second baker's boy as crier in the chapter | "and a boy ran after him" | — |
| F4 | l.172 | Style | "He tore the last of the bread" | "the last of the" ×3 in the chapter | "He tore the crust in two" | — |
| F5 | l.192 | Style (#3) | "on ice, and in snow, and on the deck…" | An automatic triad; ice and snow are one item | "on ice, and on the deck of Pacuvius's ship when it was wet." | — |

**Tested-and-rejected strings (they planted findings; do not use):** "He came away from it…" ("away from it" 3× book-wide → tic gate FAIL); "He tore what was left of the bread" ("what was left" 3× → FAIL); "Felix had stopped turning over" (a new 2nd-use echo of Ch.12's "Felix had stopped"); "kept my face to the lamp" (CLOSED gaze-hold frame); "stood over it" (would be a 3rd use); "he found me watching" ("he found me" would be a 3rd use).

### Fix order: Logic (F8) → Character (F6, F7) → Law / reuse (F2, F10, F11, F1, F3) → Prose (F4, F5, F9)

### The fix script (tested)
Run from the book folder. Each `old` string matches **exactly once** (the script exits on any other count).
```python
# apply_fixes.py  —  usage: python3 apply_fixes.py manuscript/chapters/chapter-21.md
import sys
path = sys.argv[1]
FIXES = [
 ("F1", "Valens stood in the opening with the last light on his back. He had sand in the hairs of his forearms and something in his hand.",
        "Valens stood in the opening with the last light on his back and something in his hand."),
 ("F2", "It went on the hearth for burning. That was when I began to laugh, and he waited with oak shavings in his hair and looked at me until I was done.",
        "It went on the hearth for burning. There was oak dust all down his sleeves, and he caught me watching him."),
 ("F3", "will turn your foot,\" Valens said, beside me in the black.",
        "will turn your foot,\" Valens said."),
 ("F4", "He tore the last of the bread in two", "He tore the crust in two"),
 ("F5", "on ice, and in snow, and on the deck of Pacuvius's ship", "on ice, and on the deck of Pacuvius's ship"),
 ("F6", "Felix slid down, wordless. He stood by the dun", "Felix slid down and stood by the dun"),
 ("F7", "leading the last mule and looking at nothing.", "leading the last mule."),
 ("F8", "where the boy had been jostled.", "where whoever cut it had been jostled."),
 ("F9", "and a baker's boy ran after him calling it.", "and a boy ran after him calling it."),
 ("F10", "I lowered the scales onto the plank, very carefully. My face was doing something I could not stop. I turned it to the lamp until it behaved.",
         "I lowered the scales onto the plank, very carefully, and turned to the lamp until my mouth behaved."),
 ("F11", "before the Kalends.\" I heard my voice go up, and could not bring it down. \"Or you can",
         "before the Kalends.\" Beyond the curtain Felix stopped turning over. \"Or you can"),
]
t = open(path, encoding="utf-8").read()
for fid, old, new in FIXES:
    n = t.count(old)
    if n != 1:
        sys.exit(f"{fid}: expected 1 match, found {n}")
    t = t.replace(old, new)
    print(f"{fid}: applied")
open(path, "w", encoding="utf-8").write(t)
```
Saved at `/tmp/claude-0/-home-user/63791ee5-159c-5791-9429-07920f8d9417/scratchpad/fixes21/apply_fixes.py`.

**Tested result** (scratch copy at `/tmp/claude-0/-home-user/63791ee5-159c-5791-9429-07920f8d9417/scratchpad/eval21/books/the-hour-of-ash/`, with `tools` linked so the shape audit runs; md5 after `1a05b02c8f593b12ec3c9dcc151c51ba`):
- All 11 applied once each.
- `bash tools/check_chapter.sh 21`: **ALL MECHANICAL GATES CLEAN** (style, grammar, rhythm, show/tell 42.2%, voice-wear strict, tic gate, metaphor, shape).
- `tic_report.py --gate`: clean (and-chains 4, pivots 1/1).
- `--echoes 21`: 55, a strict subset of the 56 before (the one that dropped is "the stone where the"); command / spoken-line echoes none / none.
- Voice-bank 4-gram hits: 0.
- shape_check: `21 6820 3 42 12 dialogue question`, CLEAN.
- **The real file was never touched** (md5 still `86becc02…`).

## Strengths to PRESERVE (do not touch in polish)
- The opening burst (l.8) and "You have a mouth." / "I ate the cheese. It sat."
- **"Who knows?"** as Valens's first answer (l.62), the stair at night, "It'll take the both of you.", and "It's a stair," / "So I see." / "Everything is Grata's fish."
- The tablet and **Plautia's four lines** ("Four lines since Corinth. Is she well?") with "There was the dun's hoof to tell her about."
- "All my palm found was supper." and the maternity floor, ended on its smell.
- The heel scene complete: "that one doesn't drown, he walks home on the bottom"; "His legs stopped."
- Mara refusing to watch the second pair (the girl's sausage); the herald; **the hand to the ear and the hand that sits Felix down**; the rim chorus; the warm egg; the cushion wife.
- "Lupus died in Asia … Ask Nicanor."; **"The fish faces the wrong way,"**; the back he keeps letting down.
- **The washed hand** (l.300), the freedman's fat Lupus, Grata's earrings and her hand left in the air, Valens's misreading of her.
- "No. I was not there. I believe you anyway." and Felix's blanket through the curtain.
- The heartburn and "the fire under the bone"; Felix's gate speech; "He was taller than me now, I saw"; the palm; the wreath lifted off whole; **the closing question, verbatim.**

## PATH TO 8.5 (mandatory; Floor is 8.0)
- **Prose & Voice 8.0 → 8.5 requires:** the reuse-and-law cluster gone, with the stopping sentences left untouched. Apply F1–F3, F10, F11 (and F4, F5, F9 for the in-chapter doubles). The sentence-level quality is already there ("He dried it and looked at it, and plunged it again."). Do not polish anything else in S2 or the closing paragraph.
- **Characters (8.5, at the bar):** F6 + F7 so Felix's silence is enacted between "His legs stopped." and "he asked not one thing". Nothing else.
- **Emotion (8.5, at the bar):** F2/F10 give Mara one clean body rebel (the mouth) and leave Ch.22's laugh unspent. Do not add a replacement emotion beat at the tread; Valens's "It's a stair," carries it.

## Pacing check (one line for `feedback/progress.md`)
**OK.** After Ch.19 (8,251w, long-fade, narration median 18) and Ch.20 (7,792w, dialogue-end, 35%, median 14), Ch.21 is the run's fastest gear. It has 6,869w, 42% dialogue and a narration median of 12 against a planned "mid". **The low gear serves this chapter:**
- It is the acceleration the book needs between two long, slow chapters and Ch.22's high-gear spiral.
- S1's short sentences are a day of waiting to tell him ("Each time a man laughed outside I lifted my head.").
- S4 is cold, night and a missing boy.
- Speed still varies: S2's crowd holds 17 sentences ≥30 words.

**The one place it costs:** the outline asked for the argument to be slower, and S3 (median 11) runs as a volley instead. The deceleration comes from Felix's blanket and the beat in which Grata laughs. That is acceptable; do not pad it. The ledger's "mid" should be read as *landed low, by design*.

## Cross-Book Pattern Detection (Ch.1–21)
- **Residue-on-Valens's-body staging** (Ch.18 flour, Ch.20's cut bone shavings, Ch.21 sand + oak): a pipeline reflex for "man returns from work". F1/F2 close it; log it in the bible as CLOSED.
- **Mara's body-rebel channels:** laugh, voice and "could not stop" are all spent or reserved. **Ch.22's laugh must find its fifth shape** (bible) and stay the only laugh until then.
- **Reported indirect question as a chapter close** (Ch.16, Ch.21; both about Valens before a court): **CLOSED** from here; later `question` endings use a direct question or Mara's own.
- **Grata on "men"** (Ch.20 ×2, Ch.21 ×2): WATCH, ≤1 per chapter from Ch.22.
- **Felix's silence as a reported beat** ("asked nothing" ×4 book-wide after this chapter's close): CLOSED; show it, never label it.

## Bible sync (for the tracker; not the manuscript)
- Nicanor's card: "Who does he belong to?" (not "Whose is he?"); "This is him. The murmillo Nero freed."; "Kenchreai"; "bandy-legged" (not "brown and creased"). Fabius card: 3,000 + **1,500** earnest; the Parilia date is off the page. Freedman card: the Capua Lupus "keeps a cookshop at Puteoli … He's fat. I went in once." (not "killed at Puteoli"; "another wolf" is not on the page). Walk-on block: Grata's husband "a wine cup" (not "dice cup").
- At-risk after Ch.21: the CLOSED items above; spent lines: "Who knows?"; "It's a stair,"; "Everything is Grata's fish."; "The fish faces the wrong way,"; "Lupus died in Asia … Ask Nicanor."; "I believe you anyway."; "I can count to the Ides."; "Four lines since Corinth."

## VERDICT
**POLISH. Gate NOT MET at cycle 0** (Floor 8.0, Prose & Voice; Casual 9.0; pacing OK; mechanical gates clean). **PASS is expected after the tested 11-swap fix set**, which the evaluator must confirm on re-run (projected Floor 8.5 / Average ≈ 8.57).

**BIAS CHECK:** This evaluation was produced by the same system that wrote the prose. Confidence in scores above 8.0 requires external validation (beta readers, editors, comp analysis). A human editor may weigh the S3 argument's clean volley and the theme-on-the-surface more heavily than I do.

---

## Re-evaluation — cycle 1
**Evaluator:** book-evaluator (independent; did not write or revise this prose) | **Date:** 2026-10-22
**Text evaluated:** `manuscript/chapters/chapter-21.md`, md5 `1a05b02c8f593b12ec3c9dcc151c51ba`. This is **byte-identical to the scratch copy tested at cycle 0**, so every number from the cycle-0 test still holds: 6,820 words (shape), dialogue 42%, median 12, `dialogue` → `question`, 3 breaks.

**Measured on the real file:**
- `check_chapter.sh 21`: ALL MECHANICAL GATES CLEAN. Style is clean with foreshadow 0. Grammar, rhythm, show/tell, voice-wear strict, metaphor (1.3 fig/1k) and shape all CLEAN.
- `tic_report.py --gate`: clean. And-chains 4/9, credential asides 0, negation pivots 1/1, 'So' 0. Every gesture class is under cap.
- `--echoes 21`: 55 advisory echoes. Command echoes none, spoken-line echoes none.
- Voice-bank hits: 0 for every new string.

### Fix verification (F1–F11)

| Fix | Landed | New problem? |
|---|---|---|
| F1 (l.52) | ✓ hair residue gone | **Yes, a frame the cycle-0 eval missed and F1 kept.** "Valens stood in the opening with the last light on his back" repeats l.10 "Felix filled the shop opening with the morning behind him". Both are S1 arrivals: a figure in the opening, lit from behind by the time of day. Grata "stood in my opening" (l.326) makes three opening stagings. The line also says "light" twice in two sentences ("as the light failed" … "the last light"). → **F-2** |
| F2 (l.90) | ✓ the laugh is gone and Ch.22's fit is unspent | **Yes, and this cycle-0 string is mine.** "There was oak dust all down his sleeves" keeps the residue-on-Valens's-body beat that cycle 0 meant to CLOSE. It moved from his hair to his sleeves, and it is the third on-page chapter running: Ch.18 flour "in the hair of his forearms", **Ch.19 l.299 "stone dust in the creases of his neck and furring his arms"** (cycle 0 missed this one), Ch.21 the sleeves. Grata's sand-brush (l.332) is the pretext for her planned fourth touch and stays as the chapter's one residue beat. → **F-1** |
| F3 (l.134) | ✓ sample-13 frame gone | none |
| F4 (l.172) | ✓ "the last of the" is now ×2 | none |
| F5 (l.192) | ✓ triad gone | none (#3 drops 5 → 4) |
| F6 / F7 | ✓ Felix's silence is acted out between "His legs stopped." and "he asked not one thing" | none |
| F8 (l.288) | ✓ antecedent fixed | none |
| F9 (l.302) | ✓ | none |
| F10 (l.360) | ✓ "could not stop" gone | **WATCH, not a fix.** The mouth has now carried Mara's body two chapters running: Ch.20's fountain "My mouth was open. I could not shut it." (crying), then Ch.21's "until my mouth behaved" (amusement held down). The emotions differ, the frame differs and the line is light. But **Ch.22's laugh must not go through the mouth** or use "behaved". |
| F11 (l.404) | ✓ the voice channel is gone. Her loudness now shows in its effect and sets up "I'm not listening." | **WATCH.** "Felix stopped turning over." is the chapter's second time that Felix goes still on hearing Valens's past (after l.196 "His legs stopped."). Each does a different job and the gate is clean. Log *Felix going still as a listening signal* as SPENT for the book. |

**Laws (all PASS):**
- **NO FORESHADOWING: PASS.** No changed line reaches forward, and gate 0.
- **NO TICS: PASS.** The gate and the gesture classes are clean, and no phrase reaches 3 book-wide.
- **Retired reflexes: PASS.**
- **No reused spoken lines: PASS.** The echo scan shows none, and no fix touches speech.
- **Ch.22's mapped laugh: unspent.** This is the cycle-0 FAIL, now cleared.
- **Voice channel: retired again.**
- **"could not stop": 0.**

### Genesis Score (cycle 1)

| Dimension | Cycle 0 | Cycle 1 | Evidence / reason |
|---|---|---|---|
| Originality | 8.5 | **8.5** | No change. The fixes touch no originality evidence. |
| Theme | 8.5 | **8.5** | No change. |
| Characters | 8.5 | **8.5** | F6/F7 landed. Felix's silence is acted out ("His legs stopped." → "he asked not one thing"). The Felix-goes-still double (l.196 / l.404) stops this rising. |
| Prose & Voice | 8.0 | **8.5** (+0.5, the cap) | Three body channels that were spent or reserved are gone (laugh, "could not stop", voice), as are the sample-13 frame and the hair residue. The stopping sentences are untouched ("He dried it and looked at it, and plunged it again."; "I ate the cheese. It sat."; "All my palm found was supper."). **The 8.5 assumes F-1 is applied at finalize.** F-1 removes the last piece of the cycle-0 reuse cluster, the residue beat my own F2 left in place. #11 0.44/1k PASS. |
| Pacing | 8.5 | **8.5** | 6,820w and 42% dialogue. This is the fast gear between Ch.20 and Ch.22, as judged at cycle 0. **Pacing OK.** |
| Emotion | 8.5 | **8.5** | Mara has one clean body rebel now ("until my mouth behaved"), and Valens's hand is untouched ("I hadn't told it to."). Not 9.0: Mara's rebel is light and is held in, and the mouth was the channel last chapter. |
| Immersion | 9.0 | **9.0** | No change. |
| **FLOOR** | 8.0 | **8.5** | |
| **AVERAGE** | 8.50 | **8.57** | |

**Anti-AI:**
- 7/20 patterns, −1.0. Clean band (commercial 0–8).
- #3 is 4 instances, 0.59/1k, still moderate.
- #14 is 1 instance ("until my mouth behaved", minor).
- The other five are unchanged.

**Casual Reader: 9.0** (no change). The ten pages they read are the same pages, now without a laugh that pulled against the book's mapped one.

**CVI-Launch:**
- **9.5** (no change: 9.0 + 0.5 strong anchor).
- The anchor is unchanged: Felix's palm, cut twice so it sinks deeper, with the scrubbed hand and "The fish faces the wrong way," just behind it.

**CVI-Legacy:** 6.8 (provisional, no change).

### GATE VERDICT: **PASS**
- Floor 8.5 ✓ · Casual 9.0 ✓ · pacing OK ✓ · mechanical gates clean ✓.
- **Condition:** apply F-1 at finalize.
- F-2 is recommended. It is not required for the score.

### FINALIZE fixes (tested on a scratch copy; the real file was not touched, md5 still `1a05b02c…`)

| ID | Location | Old | New | Why |
|---|---|---|---|---|
| **F-1** (required) | l.90 | `It went on the hearth for burning. There was oak dust all down his sleeves, and he caught me watching him.` | `It went on the hearth for burning. He caught me watching him.` | Closes the residue-on-Valens beat (Ch.18, Ch.19, Ch.21). The oak stays in the house through "The smell of cut oak reached us through the dark." "It's a stair," still answers her look. |
| **F-2** (recommended) | l.52 | `Valens stood in the opening with the last light on his back and something in his hand.` | `Valens had something in his hand.` | Removes the backlit-arrival frame that repeats Felix's at l.10, the double "light" and one of three opening stagings. "He stayed on the sill." still places him. |

Script: `/tmp/claude-0/-home-user/63791ee5-159c-5791-9429-07920f8d9417/scratchpad/reeval21/finalize21.py`. Usage: `python3 <script> manuscript/chapters/chapter-21.md`. It exits unless each old string matches exactly once.

**Tested result** (scratch copy at `/tmp/claude-0/-home-user/63791ee5-159c-5791-9429-07920f8d9417/scratchpad/reeval21/books/the-hour-of-ash/`, tools linked; md5 after `23e2aa5722cdd7b0be2d6a6eb692dd16`):
- Both fixes applied once.
- `check_chapter.sh 21`: ALL MECHANICAL GATES CLEAN. The tic gate and SHAPE are clean.
- shape: `21 6800 3 42 12 dialogue question`.
- `--echoes 21`: identical to before (55). Command and spoken-line echoes none / none.
- New strings book-wide:
  - "He caught me" appears once (Ch.20 has "Grata caught me at it", a different frame).
  - "caught me watching" appears once.
  - "Valens had something in his hand" is a first use.
  - Voice-bank hits: 0.

### Character-bible sync (card lines that do not match the final page)
- **Nicanor card:**
  - The syntax line and the Ch.21 line have "Whose is he?". Change both to **"Who does he belong to?"**
  - "drowned off Cenchreae" → **"Kenchreai"**.
  - Physicality "brown and creased" → **"bandy-legged"**.
  - Ch.21 line "that Nero freed with his own hand. Nine times…" → **"This is him. The murmillo Nero freed. Nine times at Corinth…"**
  - "to Mara by look only, 'It's cold for her out here.'" → he looks at the cloak, then **says it to Valens**: "Go home. Both of you. It's cold for her out here."
- **Fabius card:**
  - "3,000 with 500 earnest" → **1,500 earnest** ("Fifteen hundred there, for earnest").
  - "Or drowned off Cenchreae" → **"Kenchreai"**.
- **Freedman:**
  - "at Nuceria at nine" → **"when I was little"**.
  - "killed at Puteoli 'the spring after' when the editor wanted blood" → **"He keeps a cookshop at Puteoli now, by the fish market. He's fat. I went in once."**
  - "Is it true your husband never asked for the finger?" → **"Your husband never asked for the finger? Not once, in nine?"**
  - Delete **"he'll find another wolf."** It is not on the page.
- **Ch.21 walk-on block:**
  - Grata's husband "dice cup" → **"wine cup"**.
  - Add the coppersmith, who shouts it to Valens from his doorway, and "a boy ran after him calling it".
  - The baker's boy carries the news to Felix ("The baker's boy says the carter says Grata says.").
- **Grata card:**
  - "Ch.21 finds a fourth" → used: **the shoulder** ("brushed the sand off the shoulder of his tunic … and let her hand stay on it after the sand was gone").
  - Earrings "the gold ones with the little pearl that she kept for the baths".
  - Questions on the page: 0.
- **Felix card:**
  - The palm scratch is **used once (Ch.21)**; Ch.28 is the last reservation.
  - His silence is shown, never labelled.
- **At-risk after Ch.21 (new entries):**
  - Residue on Valens's body: **CLOSED** after F-1. Ch.21 keeps only Grata's sand-brush.
  - A backlit arrival in the doorway: **CLOSED** after F-2.
  - Mara's mouth as body channel: **USED twice (Ch.20, Ch.21)**, so Ch.22's laugh finds another way.
  - Felix going still as a listening signal ("His legs stopped." / "Felix stopped turning over."): **SPENT**.
  - A reported-question chapter close: **CLOSED** (cycle 0).
  - Grata on "men": WATCH, ≤1 per chapter.
  - Spoken lines spent, as listed at cycle 0.

**BIAS CHECK:** This evaluation was produced by the same system that wrote the prose. Confidence in scores above 8.0 requires external validation (beta readers, editors, comp analysis). Two of this cycle's findings (F-1, and the frame F1 kept) come from my own cycle-0 strings. That is the failure the evaluator spec warns about, and it is why F-1 is required, not optional.
