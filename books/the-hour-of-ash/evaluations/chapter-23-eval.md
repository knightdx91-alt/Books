# Evaluation: Chapter 23 — An Inn on the Appian Way (run 2) · HEAT 2, the key turn
**Evaluator:** book-evaluator (independent; did not write or revise this prose) | **Date:** 2026-10-23
**Text evaluated:** `manuscript/chapters/chapter-23.md`, md5 `a49ba4459b0efeb0302031929b61af28`. This is the page after writer → dialogue-polish → hook-craft → disruptor → continuity repair (C-01…C-05, W-01…W-17, W-19, I-02/I-03/I-13; W-18 and I-04/I-12 skipped by ruling). Measurements:
- **3,518 words** (style), 3,499 (metaphor/shape), 3,781 (`wc -w` with the header comments). That is 84% of the 4,200 target.
- Dialogue **16.8%** (show_tell); ledger band 15–25. Median sentence 12 (gear low). 0 breaks. Simile 1.4/1k. Em-dash 0.
- `short-punch` object open (8 words) → `long-fade` close (83 words).

**Read against:**
- The book's CLAUDE.md.
- STATE.yaml: guardrails, retired reflexes, AUTHOR-CP2-2 (memories), CP3-3 (pregnancy gap unremarked), CP4-1, CP4-2 and END-1.
- outline.md: ledger row 23, `## Chapter 23` and its writer warnings, and Ch.24 for the handoff.
- foundation.md §6d/§6e.
- voice-dna.md §5, the heat register and its three-scene table.
- character-bible.md:
  - the Valens card, including "His Thracian childhood surfaces only as the onion memory, never as words";
  - the ACCA card and the Ch.23 walk-ons;
  - At-risk after Ch.15, including the **Heat 1 SPENT staging** list;
  - At-risk after Ch.21, Ch.22 (with its Ch.23 guards) and Ch.23.
- chapter-15.md (HEAT 1, l.520–582) and chapter-22.md (the close).
- voice-bank sample-10 (heat register).
- `dialogue-chapter-23.md`, `hook-chapter-23.md`, `disruption-chapter-23.md`, and `continuity/chapter-23-audit.md` **with its repair log**. I do not re-raise anything the repair fixed or ruled on.

**Genre profile:**
- Commercial historical romance / time-slip (comp *Outlander*).
- Anti-AI band: commercial (0–8 clean). The #11 cap is >6 instances or >0.8/1k.
- Dimension 7 = **IMMERSION**.
- Engagement: empathy 55 / fascination 30 / self-insertion 15. This chapter is pure empathy.

**Measured on the real file** (from the book folder):
- `bash tools/check_chapter.sh 23`: **ALL MECHANICAL GATES CLEAN**.
  - Style clean; grammar 0; rhythm 2 sentences flagged, not failing; show/tell no flags.
  - Voice-wear strict: clean. Tic gate: clean. SHAPE CLEAN.
  - And-chains 2/9; credential asides 0; negation pivots 0; 'So' openers 0.
- `python3 tools/tic_report.py --echoes 23`: 0 echoes, 0 command echoes, 0 spoken-line echoes.
- **My own hand scans:**
  - Ch.23's heat against Ch.15's heat, sentence by sentence.
  - Narrated states counted per character.
  - Forward-reach words (would / never / last / ahead / always / years): **foreshadowing 0**. "the whole wet night ahead of them" belongs to the fleas.
  - The spent and closed lists:
    - Mara's laugh: 0 new ("I had laughed it away" refers back to Ch.22).
    - Mouth channel: 0. Hand on belly: 0. The child's heel: 0. "heel" appears once, l.250, as the boot-jack sense "toe against heel".
    - Who-pays / "Whose …?": 0. Work dust: 0. Backlit doorway: 0 (Acca "waiting in the doorway" is not lit from behind).
    - Lying-awake close: no, because he sleeps and the fade watches the bed. Thracian words: 0. Teeth: 0. Citizenship: 0. Month count: 0.

*(l.N = line number in the current `chapter-23.md`.)*

---

## HEADLINE
**CVI-Launch:** **9.4** (8.9 + 0.5 strong anchor) | **CVI-Legacy:** **6.8** | **Genesis Floor:** **7.5** | **Genesis Average:** **8.36** | **Casual Reader:** **9.0**

**Engagement type:**
- Empathy (70): the man who won and is sadder for it, held by his pregnant wife.
- Self-insertion (20): she leads; the reader is the one doing the comforting.
- Fascination (10): Horace's road, the canal, the barge man.

**Divergence alert (1.9, just under the formal 2.0):** commercially this is a very strong quiet chapter. The anchor is unforgettable, and Acca is the best walk-on since Theano. The craft Floor sits on **two law caps, neither visible to any gate**:
1. **Characters 7.5 (NO-TICS, narrated state).**
   - Valens's withdrawn state is noted 4 times (cap 3).
   - His stillness in the heat is noted 3 times inside about 200 words.
2. **Prose 7.5 (#11 density, 0.85/1k > 0.8).** Three explaining clauses. Two of them sit inside a **rebuild of HEAT 1's spent staging**: "he held still for me … as he could hold still for anything"; "and he was quite still."; "a sound … low"; "all of him", slowly.

Nine narration-only swaps clear both caps. They are tested in the fix script below.

**Gate (Floor ≥ 8.5 AND Casual ≥ 8.5 AND pacing OK): NOT MET at cycle 0.**
- Casual 9.0 ✓. Pacing OK ✓ (see the next section). Mechanical gates clean ✓.
- Floor 7.5 ✗.

---

## PACING VS NEIGHBOURS (gate item, judged)

| | Ch.22 The Basilica Julia | **Ch.23 An Inn on the Appian Way** | Ch.24 Lucius (planned) |
|---|---|---|---|
| Words | 7,177 (target 7,600) | **3,518 (target 4,200; 84%)** | 6,200 target |
| Shape | Parallel court/city, 7 breaks | **Single scene, one night, 0 breaks** | Fragmented shards, 8 breaks |
| Gear | high (median 17) | **low (median 12)** | low/very fast shards |
| Dialogue | 36% | **16.8% (band 15–25)** | 25–35% |
| Slot | public turning point, fascination | **private consolation, heat** | birth, voice under pressure |

**Verdict: length serves the beat, and the chapter is not padded.**
- The chapter is the valley between the book's loudest public chapter and its rawest private one. A 3.5k single night is the right weight, with the same intent as Ch.14 (3.0k) and Ch.18 (2.5k).
- The 16% shortfall comes from cuts, not missing beats. The disruptor and the continuity repair removed ~300 words of repeats and rebuilt frames. All four of the outline's beats are on the page: the bad supper and landlady; the five words and the onion; HEAT 2; the long fade.
- **Proportion is the one thing to watch.** The downstairs half runs ~1,750 words against the heat's ~850. The plan budgeted 1,700 / 1,200.
  - The heat is shorter than planned, but it is complete for a "low (rain, short, close)" scene, which is how voice-dna §5 defines Ch.23. Nothing is missing.
  - The supper earns its length: Acca's worry, put into the towpath question, pays off through the floor.
  - The one sag is l.124–136: Horace, the journey summary and what Mara missed make three retrospective paragraphs in a row (~330 words). F1 and F2 tighten it.
- **Do not pad back the words F1–F9 remove (~95).** Variance by design: never flatten it.
- **Value shift:**
  - Valens goes from vindicated-and-alone (−) to held, his back to the door (+).
  - Mara goes from guilt ("I had laughed it away") to taking the door side (+).
- **Speed variation:**
  - Brisk comic cross-talk downstairs (the coughing mule, Fundi, "It won't,").
  - It slows at the five words, holds through the heat, and runs out in one 83-word sentence.

**Pacing OK.**

---

## Genesis Score (Craft Assessment)

| Dimension | Score | Evidence | Cap Reasons |
|-----------|-------|----------|-------------|
| Originality | **8.5** | The genre's "victory sex" turned into consolation after a hollow win, with **the man as the one held**. A six-months-pregnant heroine leads the scene and puts his hands down: "I lowered them to the blanket, palms up, one each side of his head, and left them there. / 'Let me,' I said." (l.258–260). The bed is a cavalry horse's blanket with its fleas. Acca's terror for the barge man reaches the page only as a question about the towpath: "Brown mule leading? A white blaze?" (l.82). | — |
| Theme | **8.5** | Home as being held, embodied: "He turned over, to face the wall, and the door was behind him, and so was I." (l.300). The five words carry the subtext without saying it (l.180). Organic texture is everywhere: the coughing mule, the eyebrow, the fly in the salt. **Held from 9.0 by two tells:** l.136 "None of it made any difference;" states the emotional surprise a page before the back shows it, and l.264 "This one he kept because I wanted it" glosses the being-held. | — |
| Characters | **7.5** (uncapped 8.5) | Acca is a complete person in 17 lines: worry spoken only to a hen; "He'll have swapped them. He's sense enough for that, hasn't he? He's that much sense." (l.86); then "Then she stopped, somewhere about the canal, and nobody down there said anything more." (l.218). Valens is sad in his own register: "Past the halfway post, a hand deep, for two hundred paces. … They didn't like it. They went." (l.80); "He's dead, or sold." (l.164). Chaos 4/4 (see below). Cover-the-name passes for all six voices. | **NO-TICS narrated-state rule.** Valens withdrawn ×4: bread held (l.68), "He watched the road." (l.126), eyes on the floor (l.178), "and he sat on in it" (l.194). His stillness in the heat ×4, with **3 inside ~200 words**: "did not shift" (l.250), "stirred once … and went loose" (l.262), "His old stillness … This one he kept" (l.264), plus "He went quite still." (l.306). Cap 7.5. |
| Prose & Voice | **7.5** (uncapped 8.5) | Stopping sentence: **"The judge had found for the plaintiff. Every mark was where it had always been."** (l.230). Underlines: "where the man with the whip had changed his footing" (l.228); "He let me look at his face with nothing in front of it." (l.274); "spoke his name into the top of it, Gaius Iulius Valens, the one in the court's wax, and then only Valens." (l.280); "That was to me." (l.132). Ugly sentence: "I was hungry the way I was always hungry now, which was all the time, and I ate his." (l.122). Voice under pressure: the asides go quiet in the heat and the senses widen (l.272: lamp oil, the horse in the blanket, the mules, sweat, the flea "and I did not care about it at all"). | **#11 density 3 / 3.5k = 0.85/1k > 0.8 → cap 7.5** (l.176, l.238, l.264). Also **HEAT 1 rebuilt in four places** (table below); voice-dna's "Ch.23 and Ch.34 find other orders, other bodies, other senses" is broken. |
| Pacing | **8.5** | See PACING VS NEIGHBOURS. Ledger honoured: object open ("The blanket had been made for a horse."), long fade, 0 breaks, dialogue in band, gear low. The value shift is clean. One sag, l.124–136. | — |
| Emotion | **9.0** | **Anchor lands:** the marked back on the horse blanket and the judge's verdict set against it (l.228–230). **Surprise:** the hollow victory; Acca's comic fury breaking off when her man is home; "Does it do that all night?" / "Most nights. It likes the carriage least." / "It's right." (l.312–316). **Body rebel:** "His breath left him and was a while returning." (l.266); the cramp, "Leg," I said. "Leg, leg." (l.286); "the long muscles beside his spine let go in turn, down to the hip" (l.306). **Techniques:** physical, comic counterpoint, subtext, silence ("I kept quiet." before the onion), and sensory widening. Investment is high: Mara's guilt at missing his hour comes first (l.128–136). | — |
| Immersion | **9.0** | Period texture carries the night: the eel stew "in something that had once been wine", the eight-scored loaf with its gray inside, the fly fished from the salt (l.66). The drip bowl shoved an inch, and "The drip found it again." (l.32). The Decennovium towpath and barge mules; "A temple of Jupiter was supposed to be up there; we saw rock going into a cloud and took it on trust." (l.24); pennyroyal (l.146). A tiled roof with no ceiling, "every tile taking its own share" (l.158), and the mules' smell rising between the boards. Horace's Satire 1.5 "made up none of it" (l.124). | — |
| **FLOOR** | **7.5** | Characters and Prose (law caps) | |
| **AVERAGE** | **8.36** | | |

**Uncapped scores are declared now** so that the re-evaluation can lift the caps without re-deriving them. Characters 8.5 and Prose 8.5 are the scores the page earns once the caps are cleared.
- Each lift is +1.0, and each is backed by 3+ cited improvements: Characters F1, F7, F9; Prose F3, F4, F6, F7, F8.

### HEAT 1 → HEAT 2: what the page rebuilds (gates cannot see these)

| Ch.15 (SPENT, bible "At-risk after Ch.15") | Ch.23 now | Fix |
|---|---|---|
| "he held still for me through it, **as he could hold still for anything**; then the stillness left him" | "**His old stillness was the one he kept for strangers and road posts and men on benches. This one he kept because I wanted it**, and it cost him; the cost was there…" (l.264). It is the same generalised-stillness-held-for-her frame, now with a triad and a third road word in the heat (C-02's concern). | F7 |
| "His knuckles stayed at my mouth, and he was **quite still**." | "He went **quite still**." (l.306) | F9 |
| "a sound came from him **against my breast, low**"; "he **made a sound into** the fleece" | "His breath was hot on the sore skin of my breast … **the sound he made was into my skin, low**." (l.280) | F8 |
| "I drew him into me, **slowly, all of him**" | "sank onto him **by slow degrees** … till I had **all of him**" (l.266) | F6 |

**Accepted as a difference, not a rebuild:**
- She comes first while he waits (l.276), which is HEAT 1's order.
- But his release is different. In Ch.15 it was to drive ("He drove into me hard"). Here it is to **hold on**: "Then he raised the hand still lying open. It found the back of my thigh…". That is the chapter's thesis, so it stays.

### Narrated-state hand count (spec: >3 notes of one state, or 3 inside ~500 words, fails)

| Character / state | Notes on the page | After fixes |
|---|---|---|
| Valens withdrawn | l.68 bread held · l.126 "He watched the road." · l.178 eyes on the floor · l.194 "he sat on in it" = **4 ✗** | F1 → 3 ✓ |
| Valens door/road watch | l.54 "the door in his eye" · l.126 (the road) · l.174 latch and stool · l.292 elbow = **4 if l.126 counts** | F1 → 3 ✓ (the l.300 turn is the payoff, not a note) |
| Valens still (heat) | l.250 · l.262 · l.264 · l.306 = **4, and 3 inside ~200w ✗** | F7 + F9 → 2 ✓ |
| Acca holding the hen | l.22 · l.86 · l.98 (l.38 sets it down) = 3 | at cap ✓ |
| Mara hungry | l.40 · l.122 = 2 | ✓ |
| "let / allowed" as a frame | Valens l.178, l.274; Mara l.234, l.280 = 2 each | thematic; WATCH ✓ |
| The bed answering (object) | l.176 dipped · l.250 sank · l.252 creaked · l.272 answered: 3 inside ~350w, and l.176/l.250 are the same beat (his weight on the cords) | F5 → 3, spread ✓ |

---

## CVI-Launch Breakdown (Commercial Assessment)
| Input | Score | Evidence |
|-------|-------|----------|
| Commercial Pacing | 8/10 | A short single scene with no break, ending on a quiet fade. It does not pull hard, but Ch.24 is the birth, and the child kicking him "so hard I felt it go through me into him" (l.304) carries the reader across. |
| Tomorrow Test | 4 anchors → 10 | IMAGE: his hands set palms-up on the horse blanket ("Let me"). IMAGE + QUOTE: "Every mark was where it had always been." IMAGE: the turn to the wall, "the door was behind him, and so was I". IMAGE: the fleas climbing out "singly to learn what had been brought them". |
| Casual Reader | 9/10 | See the report below. |
| Shareability (quote/plot/emotional) | 4 / 2 / 4 (→ 8 / 4 / 8) | Quote: "That's a river with mules in it."; "It likes the carriage least." / "It's right."; "Every mark was where it had always been." Plot: none, by design. Emotional: "she puts his hands down and says 'Let me'". MAX 8×0.6 + AVG 6.67×0.4 = **7.5** |
| Concept Pitch | yes (10) | "After he's finally believed in court, his pregnant wife holds the gladiator in a flea-bitten inn." |
| Human Closeness | yes (10) | The whole chapter. |

0.2×8 + 0.2×10 + 0.2×9 + 0.2×7.5 + 0.1×10 + 0.1×10 = **8.9**, + 0.5 strong anchor = **9.4**.

**CVI-Legacy (default weights, empathy primary):** Originality 8.5×.30 + Theme 8.5×.25 + Cultural vocabulary 3×.20 + Re-readability 7×.15 + Identity 5×.10 = **6.83 → 6.8**.
- Re-readability is 7 because the chapter rewards a second read: "You'll share it with more than him" pays off in the fleas; Acca's swapped-team reasoning pays off in the lame gray; "That was to me." answers Ch.12's stream.
- After the fixes, Theme rises to 9.0 and the total to 6.95 → 7.0. That matches the book's standing profile (Launch > Legacy by ~2.5), which comes from book-level inputs, not from a chapter defect.

---

## Anti-AI Scan (20 Patterns), 3,518 words
1. Forced symmetry: **Clear.** "Getting off him was no more graceful than getting on." (l.290) is earned by the two tries at l.252.
2. Empty poetic vocabulary: Clear.
3. Automatic rule of three: **Found, 6 (1.7/1k).** Polysyndeton triads: l.126 "the driver and the post-house men and me"; l.136 the three witnesses (factual, kept); l.218 "the towpath, and the canal, and whoever had dug it"; **l.264 "strangers and road posts and men on benches"**; l.276 "a long, slow, shaking time"; l.280 thigh / hip / small of back (a path the hand travels, kept). Most carry content. l.264 is the empty one, and F7 cuts it. Logged as a WATCH on Mara's polysyndeton.
4. Excessive em dashes: Clear (0).
5. Empty metaphors: Clear.
6. Dramatic "And" openings: Clear (0 in narration).
7. Pseudo-philosophical closings: Clear. The fade is fleas and rain.
8. Excessive parallelism: Clear. Acca's repeated reassurance (l.86) is her designed register.
9. Overly smooth transitions: **Found, minor, 1 (0.3/1k).** l.124 → l.126: Horace's comfort "did not last", then "Since the city gate he had been like this." The hinge is a little too neat.
10. Described emotions: **Found, minor, 1 (0.3/1k).** "There was a small, mean comfort in that." (l.124). It is in voice, so it stays.
11. **Explanatory Extension: Found, 3 (0.85/1k), over the commercial density cap.**
    - l.176 "…all my weight at once, **because they gave me no choice**."
    - l.238 "**They were sore; the wool of the tunic had chafed them all day in the carriage.**" This pre-explains her own next line, "They're sore from the carriage." (l.242).
    - l.264 "**This one he kept because I wanted it, and it cost him; the cost was there…**"
    - Not counted: the characterising tails "and perhaps it was" (l.10) and "and then forgotten to stop" (l.24). They add jokes; they do not unpack.
12. Binary Negation Opener: Clear (0 pivots).
13. Precision Flex: Clear. "two hundred paces", "four pieces of eel" and "eight scored sections" are period or plot load.
14. Emotional Control Demonstration: Clear. Control is given up, not shown off.
15. Authoritative Description: Clear. The setting has gaps: the temple "taken on trust", the dialect "I could not follow at all".
16. Philosophical Asides: Clear. No aphorism about truth (writer warning honoured).
17. Clean Dialogue: Clear. The tiler answers a question nobody asked him ("It won't," l.112); the quarrel through the floor; "The hen joined in."
18. Thematic Echo Chamber: Clear. There is plenty of noise (the eyebrow, the coughing mule, Fundi's wedding).
19. Graduated Reveal: Clear.
20. Emotional Temperature Report: Clear.

**Total: 4 / 20 patterns (#3, #9, #10, #11): commercial CLEAN band.** Only #11 binds, through its density cap. After F3, F4 and F7: #11 = 0, #3 = 5.

---

## Character Chaos Check (Primary: Mara)
- **Irrelevant thought:** present. "I believed her about the Kalends." (l.22); the driver's eyebrow; Horace's road.
- **Cognitive distortion:** present and **inhabited**. "It was what I had come for, and I had laughed it away." (l.136). Valens answers it plainly ("It was the same. Near enough the same.") and she does not take it.
- **Unprompted memory:** present, **triggered and returned** (CP2-2 passes).
  - Horace is triggered by the road and the singing driver, and goes back into the room ("I sat with it, and it did not last").
  - Valens's onion is triggered by the rain and goes back into the rain ("The rain sheeted on the tiles now."). It stays unexplained ("Who we were, he left out.").
  - No memory paragraph on a cadence: Ch.22 had the 1991 Forum; this one is a single clause.
- **Failed emotional management:** present. The cramp in the afterglow (l.284–288); her climax given plainly with no temperature report.
- **Voice under pressure:** demonstrated. The asides go quiet in the heat, and the senses widen (voice-dna §5).

## Secondary Character Chaos
- **Valens:** own moments. The onion; "He'll do it. He's brought it this far." (l.224), where he will not go down to the gray; the door side handed over. His breath, and the muscles giving way.
- **Acca:** own moment, the strongest walk-on chaos in Part Two. The hen kept since the fox; the drip she cannot catch; the fury that stops "somewhere about the canal".
- **The barge man:** "Let me get them dry first. You can shout after." / "On you."
- **The tilers and the driver:** grievances of their own.
- No secondary character functions only as a prop.

## The Tomorrow Test
**What the reader remembers:**
- The lamplit back. "The judge had found for the plaintiff. Every mark was where it had always been."
- Then her hands setting his down palms-up on a dead cavalry horse's blanket: "Let me."
**Anchor type:** BOTH (image + quote). This is a different type from Ch.22's spoken-name anchor, so the type is not repeated.
**Verdict:** ANCHOR EXISTS (strong).

**Shareability:** "He wins the trial and she has to hold him, in a flea-bitten inn on the Appian Way, six months pregnant, and she tells him 'Let me.'"

---

## Reader Reports

### The Devourer
- Hooked by line one (a horse blanket for a marriage bed), and kept in the supper by Acca. The towpath question is a mystery solved through the floor.
- **Would slow at l.124–136:** Horace, then "Since the city gate he had been like this", then the steps paragraph. Three looks back in a row, about a minute of reading with nothing happening. Would not stop; "Valens stood. 'Bed.'" restarts the scene.
- The heat reads fast and warm. The fade is a smile. Reads straight into Ch.24.

### The Critic
- Would underline l.228–230 (the whip-man's changed footing; every mark where it had been), "He let me look at his face with nothing in front of it.", the full name "in the court's wax, and then only Valens", and "That was to me."
- **Disappointed by:**
  - **the heat leaning on HEAT 1's sentences:** "quite still", the low sound into her skin, "all of him", slowly, and the stillness kept "for anything" → "for strangers and road posts and men on benches";
  - two explaining clauses that tell what the scene already shows (l.264, l.238);
  - l.136's "None of it made any difference;", which says aloud what the back will say better a page later.

### The Hostile
- l.136 says "The judge had heard Valens out and believed him." Two pages later he says "They believed me." The five words are pre-spent in narration.
- l.122: "His eel had been in the pot longer than mine" — both came from one pot at the same time. A small logic snag (INFO).
- l.252–254: "Getting a knee across him needed two tries", and only then "Your left knee." The advice is narrated after the act it advises (INFO; readable as said between tries).
- l.136 opens "The day he spoke I had been outside on the steps", then "I had heard the beginning". The order is reversed, but it is parseable (INFO).
- Would count Valens's downcast beats and find four.
- The fleas "climbed out … singly" in the dark: the narrator's whimsy, not a knowledge violation (INFO).

### The Casual Reader (9.0)
- Loves Acca and the hen at once ("She sleeps on me."), and the eel supper, and the man who rubbed the mules down himself.
- Feels the sadness without being told why: he pushes his bowl across.
- The sex scene is frank and warm, never embarrassing, and the "Leg, leg." cramp makes them laugh out loud. "It likes the carriage least." / "It's right." is the line they read aloud to whoever is next to them.
- Would tell a friend: "the inn chapter, with the hen."
- No vibes problem.

### The Devoted Reader (active: long saga, Outlander readership)
- Will adopt it. Re-read rewards:
  - Acca expected "Brown mule leading? A white blaze?" and reasons that the barge man swapped teams. The gray Valens saw leading is the one that comes in lame.
  - "You'll share it with more than him" pays off in the fleas.
  - "You heard it at Kirrha. At the stream." / "That was to me." against Ch.12.
  - The full name "in the court's wax" against the Ch.17 leaf.
- Would also be the reader who spots the Ch.15 lines coming back (feeds CVI-Legacy; fixed by F6–F9).

## Cross-Reader Matrix
| Issue | Devourer | Critic | Hostile | Casual | Devoted | Severity |
|---|---|---|---|---|---|---|
| HEAT 1 staging rebuilt (l.264, 266, 280, 306) | | ✓ | ✓ | | ✓ | SHOULD FIX → **law cap (Prose 7.5)** |
| Valens narrated states over 3 (withdrawn; stillness cluster) | | ✓ | ✓ | | | SHOULD FIX → **law cap (Characters 7.5)** |
| #11 explaining clauses (l.176, l.238, l.264) | | ✓ | | | | INVESTIGATE → **density cap (Prose)** |
| l.136 pre-spends "They believed me." / tells the surprise | | ✓ | ✓ | | | SHOULD FIX |
| Three-paragraph look-back sag, l.124–136 | ✓ | | | | | INVESTIGATE (F1/F2 tighten it) |
| Eel "in the pot longer" logic | | | ✓ | | | INVESTIGATE (optional) |

---

## Revision Recommendations (Ranked)

| # | Location | Problem type | What happens now | Why it fails | Revision direction | Project rule? |
|---|---|---|---|---|---|---|
| F7 | l.264 | Character / Style (#11, #3) | "so I kissed what I could reach: his chest, the hollow at the base of his throat, the hard place over his heart, the stubble along his jaw when I stretched. His old stillness was the one he kept for strangers and road posts and men on benches. This one he kept because I wanted it, and it cost him; the cost was there in the muscles of his belly under my thighs." | It rebuilds Ch.15's SPENT "as he could hold still for anything" as a triad. It explains the being-held (#11). It is the 3rd stillness note in ~200 words. The four-part kiss list is a parts inventory (voice-dna §5). "road posts" puts a third road word in the heat. | → "so I kissed what I could reach, the hard place over his heart and the stubble along his jaw when I stretched. The muscles of his belly jumped under my thighs every time." The cost is now shown as a body rebel, not told. | Yes: HEAT 2 and HEAT 3 never re-state a frame from an earlier heat scene, even in new words. |
| F9 | l.306 | Character / Style | "He went quite still. His shoulders dropped," | Ch.15 SPENT: "and he was quite still." It is also the 4th stillness note. | → "His shoulders dropped," The release now follows the kick directly. | No |
| F8 | l.280 | Style | "He made no sound until the end, and then the sound he made was into my skin, low." | It fuses two Ch.15 SPENT strings ("a sound … against my breast, low"; "made a sound into the fleece"). | → "He made no sound until the end, and then my collarbone had it before my ears did." His face is already against her collarbone; the image is a new sense. | No |
| F6 | l.266 | Style | "sank onto him by slow degrees, the child's weight sinking with me, till I had all of him and sat on him." | Ch.15 SPENT: "I drew him into me, slowly, all of him". | → "sank onto him by degrees, the child's weight sinking with me, until I was sitting on him." | No |
| F1 | l.126 | Character | "He was not short with anybody. He watched the road." | The 4th note of Valens withdrawn. Read as vigilance, it is also the 4th door/road watch. | Cut "He watched the road." Both states drop to 3. | No |
| F2 | l.136 | Exposition / Theme | "The judge had heard Valens out and believed him. None of it made any difference; he had stood up for an hour…" | It pre-spends "They believed me." (l.180) and tells the hollow-victory surprise before l.230 shows it. | → "He had stood up for an hour in front of half of Rome even so, and I had been outside for most of it." "even so" keeps the point: the witnesses decided it, and he stood up anyway. | Yes: narration never paraphrases a line a character will say in the same chapter. |
| F4 | l.238 | Style (#11) | "The nipples were wider and darker. They were sore; the wool of the tunic had chafed them all day in the carriage." | The narration pre-explains her line "They're sore from the carriage." (l.242). | Cut the second sentence. The speech keeps the fact, and l.280's "sore skin" still pays it off. | No |
| F3 | l.176 | Style (#11) | "…all my weight at once, because they gave me no choice." | An explanatory tail on a self-evident image. It is also the one clause that leans the beat toward sample-10's laughing rope bed. | Cut the tail. | No |
| F5 | l.250 | Style | "and did not shift. The cords sank under him. He got his boots off" | It doubles l.176 "The cords dipped toward him" (his weight on the cords). The bed answers 3× inside ~350 words. | Cut "The cords sank under him." | No |
| I-1 | l.122 | Logic (optional) | "His eel had been in the pot longer than mine and tasted it." | One pot, served together. | Optional: "His eel had gone cold in front of him." I did not test it, so it is not in the script; run `--echoes` if it is taken. | No |
| I-2 | l.250 | — | "toe against heel" | Boot sense, not the spent child's heel. | Leave it. | No |
| I-3 | Ch.24 guard | Continuity | Ch.22 and Ch.23 both close a beat on Valens turning to the wall. | A third would be a frame. | Ch.24 does not end a section on anyone turning to a wall to sleep. | Bible note |

### Fix order: Logic/Character (F7, F9, F1) → Structural/Connective (F2) → Prose (F8, F6, F4, F3, F5) → optional I-1.

### TESTED FIX SCRIPT
`/tmp/claude-0/-home-user/63791ee5-159c-5791-9429-07920f8d9417/scratchpad/fixes23/apply_fixes.py <chapter-23.md>`
- Nine exact old→new replacements, F1–F9. Each must match **exactly once**, or the script aborts and writes nothing. A second run correctly aborts at F1.
- Narration only: **0 spoken words cut**. Nothing restored that dialogue-polish, the disruptor or the repair cut: not the wine jar, not "These days I was always hungry", not the five-years paragraph, not the rain-as-mood lines, not the lamp below.
- Tested on a scratch copy of the book folder:
  - `bash tools/check_chapter.sh 23` → **ALL MECHANICAL GATES CLEAN**.
  - Style 3,424 words; **dialogue 17.2%** (≥15 ✓); simile 1.5/1k; em-dash 0; rhythm 1 flagged (was 2).
  - Voice-wear strict clean; tic gate clean; shape clean.
  - `python3 tools/tic_report.py --echoes 23` → 0 echoes / 0 command / 0 spoken-line.
- Two first-draft strings were varied to pass: "a little at a time" (a Ch.7 echo, and a voice-wear self-repeat) and "I felt in my … before I heard" (Ch.3).
- Each new string was hand-checked against the Ch.15 Heat 1 SPENT list, the Ch.21–23 at-risk blocks, sample-10 and the outline's plan sentences.
- Patched-page md5 on the scratch copy: `9377b9af2f707f2d7e17716e1bf8527d`.

---

## Strengths to PRESERVE
- The opener "The blanket had been made for a horse." and the Kalends exchange: "I believed her about the Kalends."
- **Acca**, entire: the hen and the fox; the towpath questions; "He'll have swapped them…"; the fury that stops "somewhere about the canal". Her address count stays at 3.
- The tilers' mule ("In a basket. He threw it in for nothing." / "I'll tell his mule."), and the unasked "It won't," / "Three."
- "That's not a towpath out there," / "That's a river with mules in it."
- "Valens pushed his bowl over to me." / "You're not hungry?" / "Eat it." and the protected ugly sentence.
- "I missed it," … "That was to me." / "It was the same. Near enough the same."
- The five words, untouched, and "Usually there was a next thing … Nothing came."
- The onion in the rain, unexplained.
- The back, l.228–232, and **"The judge had found for the plaintiff. Every mark was where it had always been."** (W-18's "five years" stays off the page by ruling.)
- "Look, then. All of it's yours, and most of it's swollen." / "Grata says what she thinks will rile me."
- The hands set down palms-up; "Let me,"; "Mara." / "I know."; the thumb; "Then he raised the hand still lying open."
- The full name "in the court's wax, and then only Valens"; "Stay," … "A while."; the cramp.
- The door side ("The latch is wood." / "Then I'll hear it.") and **"the door was behind him, and so was I."**
- The kick through her into him; "It's right."
- The 83-word flea fade.

---

## PATH TO 8.5 (Floor 7.5 → 8.5)
- **Characters 7.5 → 8.5 requires:** no character's narrated state noted more than 3 times, or 3 times inside 500 words. The NO-TICS cap is the only thing holding the dimension; the uncapped page is 8.5.
  - Surgery:
    - **F1** cuts "He watched the road." (l.126), which takes the withdrawn and watching states to 3 each.
    - **F7** replaces the l.264 stillness gloss with the belly muscles jumping, a body rebel. It is shown, not told.
    - **F9** cuts "He went quite still." (l.306).
  - Stillness then has 2 notes (l.250, l.262), and the being-held is carried by actions only: hands down, "Let me", the open hand raised, the muscles letting go.
  - 3 cited improvements → a +1.0 lift is allowed.
- **Prose 7.5 → 8.5 requires:** #11 under 0.8/1k, and HEAT 2 built from its own sentences, not HEAT 1's.
  - Surgery:
    - **F3, F4, F7** remove all three explaining clauses (#11 → 0).
    - **F6, F8, F9, F7** remove the four Ch.15 rebuilds ("all of him" slowly; the low sound into skin; "quite still"; stillness "for anything").
    - **F5** removes the doubled cords beat.
  - The stopping sentence (l.230) and the underlines already meet the 8.5 bar.
  - 5 cited improvements → a +1.0 lift is allowed.
- **Theme 8.5 → 9.0 (not floor-binding):** F2 removes the told surprise and the pre-spent "believed". F7 removes the told being-held.
- **Projected after F1–F9:** Originality 8.5 · Theme 9.0 · Characters 8.5 · Prose 8.5 · Pacing 8.5 · Emotion 9.0 · Immersion 9.0 → **Floor 8.5 / Average 8.71 / Casual 9.0 / CVI-Launch 9.4 / CVI-Legacy 7.0**. To be confirmed by re-evaluation of the patched page.

**Bible re-sync for the downstream chain (not applied by me):**
- Log as CUT: "He watched the road."; "None of it made any difference"; "because they gave me no choice"; "the wool of the tunic had chafed them"; "The cords sank under him."; "by slow degrees … till I had all of him"; the l.264 stillness sentences and the four-part kiss list; "the sound he made was into my skin, low"; "He went quite still."
- Log as SPENT: the F2/F6/F7/F8 replacement strings.

## VERDICT
**POLISH.** Genesis Floor 7.5 (Characters and Prose, both law caps) < 8.5. Casual 9.0 ✓. Pacing OK ✓. Mechanical gates clean ✓.

Apply `apply_fixes.py` (F1–F9, tested), re-run `bash tools/check_chapter.sh 23` and `--echoes 23` on the real file, then re-evaluate. The projected result is PASS at Floor 8.5.

**BIAS CHECK:** This evaluation was produced by the same system that wrote the prose. Confidence in scores above 8.0 requires external validation (beta readers, editors, comp analysis).

---

## Re-evaluation — cycle 1
**Evaluator:** book-evaluator (independent) | **Date:** 2026-10-23
**Text evaluated:** `manuscript/chapters/chapter-23.md`, md5 **`9377b9af2f707f2d7e17716e1bf8527d`**. This matches the tested scratch copy byte for byte (`scratchpad/eval23/.../chapter-23.md`). F1–F9 landed exactly as tested.

### Measured on the real file
- `bash tools/check_chapter.sh 23`: **ALL MECHANICAL GATES CLEAN**.
  - Style 3,424 words. Dialogue **17.2%**. Simile 1.5/1k. Em-dash 0.
  - Rhythm: 1 flagged. Grammar: 0.
  - Voice-wear strict, tic gate (`--gate`) and shape: all clean.
  - And-chains 2/9. Credential asides 0. Negation pivots 0.
- `python3 tools/tic_report.py --echoes 23`: 0 echoes, 0 command echoes, 0 spoken-line echoes.

### Hand re-counts on the patched page

**Narrated physical states** (the rule: >3 notes of one state, or 3 inside ~500 words, fails). Word offsets are from the chapter open.

| Character / state | Notes now | Verdict |
|---|---|---|
| Valens withdrawn (physical) | bread held l.68 (w825) · eyes on the floor l.178 (w1833) · sat on in the spray l.194 (w1953) | **3 ✓**. l.126 is now behaviour in summary ("a word or two apiece"), not a physical state. |
| Valens door watch | l.54 (w668) · latch l.174 (w1779) · elbow l.292 (w3137) | **3, spread ✓**. l.300 is the payoff. |
| Valens still (heat) | l.194 · "did not shift" l.250 (w2524) · fingers "went loose" l.262 (w2640) | **3, spanning 687 words ✓**. F7 and F9 removed the other two. |
| Valens breath (heat) | l.232 · l.266 · l.280 · l.318 | 4 notes, but 4 different states (calm, shock, contact, release), so it does not fail the rule. **WATCH → G3 takes it to 3.** |
| Valens face | "nothing to read" l.240 → "nothing in front of it" l.274 | 2. A designed turn ✓ |
| Acca holding the hen | l.22 (w144) · l.86 (w964) · l.98 (w1006) | **3, spanning 862 words ✓** (l.38 sets it down) |
| Mara hungry | l.40 · l.122 | 2 ✓ |
| Mara guilt | l.136 | 1 ✓ |
| The bed answering | dipped l.176 · creaked l.252 · answered l.272 | 3, spread ✓ (F5 landed) |
| "He let …" sentence openers (Valens) | "He let me lean." l.178 · "He let me look" l.274 · "He let a breath go" l.318 | 3. The first two are a deliberate pair; the third is an idiom that blurs it. **G3** |

**Explanation density (#11):**
- The three cycle-0 instances are gone (F3, F4, F7). **#11 = 0 at full weight.**
- One restatement remains at l.136: "and I had been outside for most of it" repeats "and then I was gone" two sentences earlier. It also makes "outside" appear 3× in 90 words, with "I had been outside" twice. That is 0.29/1k, minor and under the cap. **G2**

**HEAT 1 rebuilds:**
- 0 of the 4 remain. "quite still", "all of him" slowly, the low sound into skin, and the stillness kept "for anything" are all gone.
- The replacement strings checked against Ch.15 and the bible's SPENT staging list:
  - "collarbone", "jumped", "shoulders dropped" and "had it before" are new to the book.
  - "slow" is no longer used of entry.
  - Bible caps: "somewhere" 2 (cap 2) ✓; "so that" 2 ✓; "and stayed" 0; "in my hair" 0; "had gone quiet/still" 0.
- **Residual WATCH, not a cap:** she guides his hand (l.276) as Ch.15 did ("I put my own hand over it and took it where I wanted it").
  - It is accepted because the act is new (the thumb, beneath the child, her on top) and it *is* the chapter's lead-the-scene design.
  - The tail "until I was done" is the last echo of Ch.15's "held still for me through it". **G5**
  - Ch.34 must not guide the hand a third time. *(bible note)*

**Echoes the gates cannot see: what F6 planted.**
- "by degrees" is now the narrator's **3rd use book-wide**: Ch.12 "It stopped by degrees.", Ch.20 "sagged by degrees", Ch.23 l.266. It is a 2-word recurrence below the tic gate's reach, and under the book's NO-TICS law a narrator phrase at 3 is a defect. **G4**
- F6's "until I was sitting on him" adds to a cluster. The heat and afterglow run **six narrated "until" clauses in ~550 words**: l.266; l.276 ×2; l.280; l.284; l.288. It is a syntactic reflex, action-until-result, and the Critic hears it. **G4–G6 take it to 3** (l.276 "until he had the way of it", l.280, l.284), plus one spoken (l.246).
- The other cycle-0 strings check clean:
  - "even so": 1 in the book.
  - "every time": generic, 8 uses across 6 chapters, none of them a frame.
  - "sank onto": 2 in the book.

**Closed and spent channels, re-run:**
- Laugh 0. Mouth 0. Hand on belly 0. Child's heel 0 ("toe against heel" is the boot).
- Who-pays 0. Work dust 0. Backlit doorway 0. Thracian words 0. Teeth 0. Citizenship 0. Month count 0.
- Foreshadowing 0: "the whole wet night ahead of them" belongs to the fleas.

**Cut effects restored:**
- **None.** The wine jar, "These days I was always hungry", the five-years paragraph, the rain-as-mood lines and the lamp below are all still absent.
- l.122's ugly sentence is intact.

**l.122, the eel: a real logic error.**
- Both bowls came from one pot at one time ("The eels came in a pot.", l.66). His eel cannot have "been in the pot longer than mine".
- What happened is that it sat while he held his bread (l.68).
- **G1** fixes it plainly, so the protected ugly sentence still carries the beat.

### Scores, cycle 1 (strict: +0.5 max per dimension per cycle)

| Dimension | C0 | **C1** | Evidence | Cap |
|---|---|---|---|---|
| Originality | 8.5 | **8.5** | Unchanged. Consolation, not victory sex; the man is the one held; "Let me," and the hands set palms-up on a cavalry horse's blanket. | — |
| Theme | 8.5 | **9.0** | Both cited tells are gone: "None of it made any difference;" (F2) and "This one he kept because I wanted it" (F7). The hollow win is now carried by the back alone: "The judge had found for the plaintiff. Every mark was where it had always been." Being held is carried by actions alone, ending in "the door was behind him, and so was I." **≥9.0 challenge:** a senior editor would set this beside *Outlander*'s quiet post-crisis nights (the Lallybroch return) and find the theme better embodied than stated. Granted. | — |
| Characters | 7.5 | **8.0** | All narrated-state counts are ≤3 (table above). Acca is unchanged and still the best walk-on. Chaos 4/4, inhabited. "The muscles of his belly jumped under my thighs every time." turns the told cost into a body rebel. | **Per-cycle cap (+0.5).** The page earns 8.5. Nothing on it holds this dimension down; G3 is hygiene. |
| Prose & Voice | 7.5 | **8.0** | #11 is at 0 full-weight. HEAT 1 rebuilds are at 0. The stopping sentence (l.230) and the underlines stand. The new "then my collarbone had it before my ears did" is a fresh sense in the right place. | **Per-cycle cap (+0.5).** Uncapped 8.5 **only once G4–G6 land**: the 3rd "by degrees" and the "until" reflex are on the page now. Without them, next cycle's lift would not be clean. |
| Pacing | 8.5 | **8.5** | The l.124–136 sag is tighter (F1, F2), and the value shift is unchanged. Not raised to 9.0: three look-backs still run in a row, and this is a valley chapter by design. | — |
| Emotion | 9.0 | **9.0** | The anchor, the surprise and the body rebel all intact. The F9 release now follows the kick directly: "His shoulders dropped, and the long muscles beside his spine let go in turn". | — |
| Immersion | 9.0 | **9.0** | Unchanged. The eel slip (G1) is too small to cost a point. | — |
| **FLOOR** | 7.5 | **8.0** | Characters and Prose, both per-cycle cap | |
| **AVERAGE** | 8.36 | **8.57** | | |

**Casual Reader: 9.0.** Unchanged. Acca and the hen, "Leg, leg.", "It's right." The cuts are invisible to this reader.

**CVI-Launch: 9.4.** Inputs unchanged: Pacing 8, Tomorrow 10, Casual 9, Shareability 7.5, Pitch 10, Closeness 10 → 8.9, plus 0.5 for the strong anchor.

**CVI-Legacy: 7.0.** 8.5×.30 + 9.0×.25 + 3×.20 + 7×.15 + 5×.10 = 6.95.

**Gate:** Floor 8.0 < 8.5 → **NOT MET**. Casual ✓. Pacing OK ✓. Mechanical gates ✓.

### Is it only the cap?
**No, not quite.**
- **Characters:** the cap alone holds it.
- **Prose:** the cap is what binds this cycle. But the page also carries one F6 plant (the narrator's 3rd "by degrees") and a six-deep "until" cluster in the heat. Either would block an honest 8.5 next cycle.
- **Immersion:** carries one real logic error (the eel).

So I recommend the six swaps below, all narration and all tested. **None of them changes a score this cycle.** Their job is to make next cycle's cap release clean.

| # | Location | Type | Now | Why | New |
|---|---|---|---|---|---|
| G1 | l.122 | Logic | "His eel had been in the pot longer than mine and tasted it." | One pot, served together. | "His eel was cold." |
| G2 | l.136 | Style (#11 restatement) | "…even so, and I had been outside for most of it." | Repeats "and then I was gone"; "outside" 3× in 90 words. | "…in front of half of Rome even so." |
| G3 | l.318 | Style / NO-TICS | "He let a breath go through his nose, and by and by he slept." | The 3rd "He let" opener blurs the l.178/l.274 pair, and it is the 4th breath note. | "By and by he slept." |
| G4 | l.266 | Style (F6 plant) | "sank onto him by degrees, … until I was sitting on him." | The 3rd "by degrees" book-wide (Ch.12, Ch.20); also one of 6 "until"s. | "sank onto him, the child's weight sinking with me." ("He shut his eyes." follows.) |
| G5 | l.276 | Style | "while his thumb waited on me until I was done." | "until" cluster; last trace of Ch.15's "held still for me through it". | "while his thumb waited on me." |
| G6 | l.288 | Style | "pushed the toes back until it let go." | "until" two lines after "until my left calf knotted". | "pushed the toes back, and it let go." |

**TESTED:** `/tmp/claude-0/-home-user/63791ee5-159c-5791-9429-07920f8d9417/scratchpad/fixes23b/apply_fixes.py <chapter-23.md>`
- Each replacement must match exactly once, or the script writes nothing. A second run correctly aborts at G1.
- Tested on `scratchpad/reeval23/books/the-hour-of-ash/`:
  - `check_chapter.sh 23`: **ALL MECHANICAL GATES CLEAN**. Style 3,385 words; **dialogue 17.4%**; simile 1.5/1k; rhythm 1; voice-wear strict, tic gate and shape all clean.
  - `--echoes 23`: 0 / 0 / 0.
- Hand checks:
  - Narrated "until" drops 6 → 3. "by degrees" drops 3 → 2 book-wide. Valens breath 4 → 3. "He let" 3 → 2.
  - The new strings ("His eel was cold.", "By and by he slept.", "sinking with me.", "waited on me.", "and it let go.") have no prior-chapter matches.
  - 0 spoken words touched. Nothing previously cut is restored.
- Patched md5: **`746fdf5c2e71c8af81638e87bdee0e59`**.

**Bible re-sync (not applied by me):**
- Log as CUT: "by degrees" (Ch.23), "in the pot longer", "outside for most of it", "He let a breath go".
- Log **"by degrees": CLOSED, 2 uses** (Ch.12, Ch.20).
- Log as WATCH: narrated "until" clauses, ≤3 per heat scene.
- Log for Ch.34: no hand-guiding (Ch.15 and Ch.23 have each used it once).

**Projected after G1–G6, cycle 2:**
- Characters 8.5 and Prose 8.5, each a +0.5 cap release with nothing left on the page to hold them.
- Floor **8.5**, Average **8.71**, Casual 9.0 → **PASS** expected.

### VERDICT (cycle 1)
**POLISH.**
- Genesis Floor 8.0 (Characters and Prose, held by the per-cycle cap). Average 8.57. Casual 9.0 ✓. Pacing OK ✓. Gates clean ✓.
- Apply G1–G6, run `check_chapter.sh 23` and `--echoes 23` on the real file, then run cycle 2.

**BIAS CHECK:** This evaluation was produced by the same system that wrote the prose. Confidence in scores above 8.0 requires external validation (beta readers, editors, comp analysis).
