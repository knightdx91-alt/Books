# Evaluation: Chapter 6 — The Claiming
**Evaluator:** book-evaluator | **Date:** 2026-10-20 | **Draft:** R1 (3,097 words vs 2,800 target)

## HEADLINE
**CVI-Launch:** 8.6 (8.1 + 0.5 strong-anchor bonus) | **CVI-Legacy:** 6.0 | **Genesis Floor:** 8.5 | **Genesis Average:** 8.5
**Engagement Type:** Self-Insertion (primary) / Empathy (secondary) / Fascination (tertiary)
**Divergence Alert:** none. Launch is above Legacy, as expected for a warm commercial fantasy.

**VERDICT: PASS** (Floor 8.5, Casual 8.5). Three small line fixes are listed below. F1 is a continuity slip and should go in before commit. None of the fixes adds plot or needs re-scoring.

---

## Mechanical gates (scratch copy: ch.1–6 in `manuscript/chapters/`)
- `voice_wear_check.py`: **clean.** No retired phrases, no device over cap, no self-repetition.
- `tic_report.py --gate`: **clean.** No auto-recurrence. Gesture classes are all under cap (Ch.6 has 2 nods plus "heads bobbed"; the head shakes are source beats). Negation pivots 0, and-chains 1.
- `style_check.py --dir`: **clean.** Simile 1.6/1k, adverbs 9.0/1k, em-dashes **0**, no cross-chapter repeated phrase.
- `grammar_check.py`: 0 errors.
- Filter words: "began to" ×2 (L105, L123), "just" ×1 (in dialogue, L209). Acceptable.
- Markdown: every `---` has a blank line before it, so there is no setext-heading risk (the Ch.5 defect does not recur).

## Source fidelity (L286–304, to "Bal nods accepting her reasoning")
Every source beat is present, in order: the carriages joining; the buggy with two boys and the older Tempus girl whose sygl sparks; Bal's guess that they are siblings (kept as *his* guess, which is consistent with the author decision); the castle, five towers, wall and raised gate; the blue-veined thrones with gold sygls; Verin's warning and goodbye; the crowd grouping by sygl; "keeps the thought … alive"; the gong; "Can they sense you here?"; the flash; Aren/Nera, Kenmei, Naisura (gym), Raizen; the empty far-right throne; Aren's speech including "lesser schools"; about fifty students; "You okay?" / "About three thousand years, right?"; the last two standing; the whispers; "Young man, come closer"; "Are they yours?"; "come so far for nothing"; "But what if she did claim us?" projected to carry; the clap and Aren's stumble; the disguise; the claim and High Priest naming; "at their peril"; the domains; the stares; Aren's clap; the stairs and the painted corridor; the angry vampire Goddess; havoc; "other ways to get revenge"; the High Priest explanation; the reasoning accepted.
- **Viridia** is present and **unnamed** (L9–15, L125). "Bal had missed her name. He hadn't been listening." handles this cleanly and is consistent with L105. Correct per the decision.
- **Heir's School / lesser schools** match the Sygldry ruling (L21, L95, L97). The palm sygl is respected (L39–41).
- **Handoff note.** The chapter runs past the stated source cut to include "Anything special…?" / "We'll talk more about it tonight." (L233–237). The outline's own Hook for Ch.6 asks for exactly this line, so it is correct. **Ch.7 must therefore open at the pedestal** (its outline Opening) and must not repeat the exchange.
- **Added texture, none of it plot:** the boy hauled in by his belt, the trunk boy, Bal wondering if a god can catch cold, the pigeon, the woman holding a fish, the Fredrick aside (triggered by "lesser schools"; Ch.1 has him leave by car, so that is consistent). Nothing is invented about character, lore, habit or backstory. The tone is warm, light and playful, with no darkening.
- **Dialogue rule:** each line keeps its speaker, meaning and position. The polish is natural American speech ("wreaked" fixes the source's "wrecked"; "I guess you do know"; "Not only as far as a familiar is allowed to"). No line has been reassigned and no information added.
- **Amelia** comes across as confident (the walk to the throne, L173–175), playful (the grin, the laugh in the stairwell) and protective ("I did it to keep you safe"). "Master" is unused, which is fine.

## Genesis Score

| Dimension | Score | Evidence | Cap Reasons |
|-----------|-------|----------|-------------|
| Originality | 8.5 | The reveal is played *quiet*: "It wasn't loud. Half the students at the back probably never heard it. But Aren stumbled backward…" (L163). Bal sees her unchanged while gods stagger: "She looked exactly the same to him." (L167) | none (commercial: 1 fresh element needed) |
| Theme | 8.5 | The boy nobody claims is claimed by name. "Bal went and stood behind Amelia's throne by himself. It was the shortest line in the courtyard by a wide margin." (L197). Earlier: "There was no group for them to join." (L57) | none. Theme is embodied, never stated |
| Characters | 8.5 | Bal: "About three thousand years, right?" (L113); "Bal wondered whether a god could catch cold, and decided it was probably not a thing he should ask." (L87). Amelia: "She settled into it as if she had last sat there yesterday." (L175) | No tics. Chaos 3/4 inhabited (irrelevant thought L87/L211; body L41; triggered memory L97, which returns to the scene) |
| Prose & Voice | 8.5 | Stopping sentence: "A pigeon was walking on the flagstones, and Bal could hear its feet." (L133). Underlines: L163, L175, L195 ("had his mouth open, and nobody had told him"), L199 ("This one was an ordinary clap. Nobody stumbled.") | #11 at 1 instance (0.3/1k), under the cap. Rough sentences present (L87, L213) |
| Pacing | 8.5 | Decelerated ceremony (L121–131, "The sun moved off one throne and onto the next"), then a silence beat, then a fast clap sequence. Value shift: refused ("come so far for nothing", L149) to claimed and named High Priest | Hook is soft but outline-mandated. One continuity slip (F1) |
| Emotion | 8.5 | Anchor: the empty throne, then the clap. Surprise: the god-staggering moment is *not loud*, and Bal answers it with "That made sense… A lot of sense." Body: "His left hand closed. He opened it again." (L41) | Claim moment carried by restraint/humour (L197); deliberate, no cap |
| Engagement (Dim 7) | 8.5 | The self-insertion fantasy pays off ("Let the first one harm him at their peril," L181). Empathy runs through the unclaimed-orphan line | none |
| **FLOOR** | **8.5** | | |
| **AVERAGE** | **8.5** | | |

## CVI-Launch Breakdown
| Input | Score | Evidence |
|-------|-------|----------|
| Commercial Pacing | 8.5 | The set-piece is the book's first public payoff; there is no stopping point after L75 |
| Tomorrow Test | 3 anchors → 9 | IMAGE: the soft clap / Aren catching his throne arm. IMAGE: the one-boy line behind the empty throne. QUOTE: "Let the first one harm him at their peril." |
| Casual Reader | 8.5 | Big, fun, readable reveal |
| Shareability (quote/plot/emotional) | 3/4/2 → 7.2 | Plot: "the 'mythical' goddess was standing in the crowd the whole time" |
| Concept Pitch | yes (10) | |
| Human Closeness | partial (5) | |
| Raw | 8.1 | +0.5 strong anchor = **8.6** |

CVI-Legacy: Orig 8.5×.3 + Theme 8.5×.25 + Vocab 2×.2 + Reread 4×.15 + Identity 3×.1 = **6.0** (Ch.5: 5.9).

## Anti-AI Scan (20 patterns)
1 Forced symmetry: minor. "Some looked confused. Some looked awed." (L195; a source triad). 0.3/1k
2 Empty poetic vocab: clear
3 Rule of three: minor. L51 "his cottage and his fire pit and his one chair"; L195. 0.6/1k
4 Em dashes: clear (0)
5 Empty metaphors: clear
6 "And" openers: clear in narration
7 Pseudo-philosophical closings: clear (section ends are concrete)
8 Parallelism: minor. L163 hand-by-hand list (earned; it pays off L89)
9 Smooth transitions: minor. Source-derived ("It wasn't long until…")
10 Described emotion: minor. "He was curious." (L213)
11 Explanatory extension: 1 counted. "He could tell she wasn't going to." (L219). L171 and L231 are source beats and are not counted
12 Binary negation: minor. "No one came to stand by them. Nobody needed to." (L57)
13 Precision flex: clear
14 Emotional control demo: clear
15 Authoritative description: clear. Gaps are built in (which tower is hers, Viridia's missed name)
16 Philosophical asides: clear ("Something like this stays with you" is the author's line)
17 Clean dialogue: watch. The corridor Q&A is orderly, as in the source; "Mm-hm." and the hesitation loosen it
18 Echo chamber: clear (pigeon, fish painting, trunk boy)
19 Graduated reveal: watch. Ch.5 is a journey into night and Ch.6 a set-piece, so the ledger varies
20 Temperature report: clear
**Total: 7 minor + 2 watch, all <0.5/1k → CLEAN for commercial (0–8).**

## Character Chaos Check (Bal)
- Irrelevant thought: present (god catching cold, L87; the woman with a fish, L211)
- Cognitive distortion: absent (not required)
- Unprompted memory: present and triggered (Fredrick at "lesser schools," L97; it returns to the scene)
- Failed emotional management: present (L41, the hand closes)
- Voice under pressure: demonstrated (L127–133: short lines, silence, the pigeon)

## Secondary characters
- Verin: has his own exit ("He had no idea who had slept on his floor," L51)
- Aren: distinct and humane ("his smile was still a sad one," L155)
- The Tempus girl: present, unnamed, physicalized by the spark only

## The Tomorrow Test
**Remembered:** a clap so quiet the back rows missed it, which sends a god stumbling into his own throne arm. Then one boy standing alone behind the empty throne.
**Anchor type:** BOTH (image + "Let the first one harm him at their peril"). **ANCHOR EXISTS.** The type differs from Ch.5 (the wiped tear).
**Shareable:** "The goddess everyone thinks is a myth was standing in the back row, and he asks, 'But what if she did claim us?'"

## Reader Reports
- **Devourer:** the road and castle section (L3–27) is the only slow stretch, and it is short. From the gong on, they cannot stop. The hook is mild but carried by curiosity.
- **Critic:** would underline L133, L163, L175 and L199. Would dislike the double "made sense" (L171/L231) and "in the row… in the row" (L37).
- **Hostile:** "staring at in his own hand since yesterday" (L39) is wrong. The hand was regrown the day before Ch.5, so this is two days ago. Also "Nobody needed to" (L57) is muddled logic.
- **Casual:** 8.5. This is the "oh, here we go" moment the premise promised. Would buy.

## Cross-Reader Matrix
| Issue | Devourer | Critic | Hostile | Casual | Severity |
|---|---|---|---|---|---|
| L39 timeline "since yesterday" | | | X | | INVESTIGATE (Logic; fix before commit) |
| L57 "Nobody needed to." | | X | X | | SHOULD FIX |
| Double "made sense" (L171/L231) | | X | | | INVESTIGATE |
| L37 "in the row" ×2 | | X | | | INVESTIGATE |
| L219 redundant explanation | | X | | | INVESTIGATE |

## Revision Recommendations (surgical; no plot added)
| # | Location | Type | Now | Why | Fix | Rule? |
|---|---|---|---|---|---|---|
| F1 | L39 | Continuity | "the shape he had been staring at in his own hand since yesterday." | The hand was regrown the day before Ch.5, which makes it two days ago | "…in his own hand for two days." (or "since the temple.") | No |
| F2 | L57 | Logic/Style | "No one came to stand by them. Nobody needed to. There was no group for them to join." | "Nobody needed to" contradicts the point and reads as a negation flourish | Cut "Nobody needed to." | No |
| F3 | L219 | Style (#11) | "Bal waited, but she left it there. He could tell she wasn't going to. So he tried something else." | The second sentence explains the first | Cut "He could tell she wasn't going to." | No |
| F4 | L171 / L231 | Style | "That made sense, Bal thought. A lot of sense." … "Then he nodded. Her reasoning made sense." | The same phrase twice in one chapter (both are source beats) | L231: "Then he nodded." and stop there (the Aren image already carries the acceptance) | No |
| F5 | L37 | Style | "…one sygl after another, until they reached the last throne in the row." | "in the row" appears twice in one sentence | "…until they reached the last one." | No |

Optional (do not apply if it risks the cap): L213 "He was curious." can stay as the chapter's rough sentence.

### Fix order: F1 (logic) → F2 → F3/F4/F5 (prose)

## Strengths to PRESERVE
- The quiet clap (L161–163) and Raizen's hands coming apart, which pays off L89.
- "She looked exactly the same to him." (L167). The disguise is told from Bal's side.
- The silence beat with the pigeon (L133).
- "the shortest line in the courtyard by a wide margin" (L197) and "an ordinary clap" (L199).
- Viridia unnamed and glimpsed twice, with only the spark (L13, L125).

## Trajectory
Ch.1–5 each FINAL at 8.5, and Ch.6 R1 holds 8.5 on first draft. The cross-chapter pipeline fingerprints (orderly corridor Q&A; section-ending one-liners) are at watch level only and have not escalated.

BIAS CHECK: This evaluation was produced by the same system that wrote the prose. Confidence in scores above 8.0 requires external validation (beta readers, editors, comp analysis).
