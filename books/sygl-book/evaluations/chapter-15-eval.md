# Evaluation: Chapter 15 — Rumors
**Evaluator:** book-evaluator | **Date:** 2026-10-20
**Text evaluated:** `manuscript/chapter-15.md` (1,887 words of prose; 1,972 with comments). Target 1,800, range 1,500–2,100. On spec.
**Read first:** STATE.yaml (decisions), CLAUDE.md (canon guardrails), project/STYLE_CONSTRAINTS.md, character-bible.md, outline Ch.15, chapter-14.md (ending at bed, mid-revision), chapter-07.md (the hall's plates), chapter-09/10/12/13 (class lists, Lora's table, the green book), Sygl_Complete.txt L706–715 (to "they both fell asleep"), evaluations/chapter-14-eval.md.

## HEADLINE
**CVI-Launch:** 8.5 (8.0 + 0.5 strong anchor) | **CVI-Legacy:** 6.2 | **Genesis Floor:** 7.5 | **Genesis Average:** 8.4
**Engagement Type:** Self-Insertion (primary) / Empathy (secondary) / Fascination (tertiary)
**Divergence Alert:** none (1.0 gap).

**VERDICT: POLISH.** On merit this is an 8.5 bridge. It is short, light and warm. It runs from morning to bed, and the card on the nightstand ties it to last night's evening. Every source beat from L706 to L715 is here, in order, with the right speaker. Bal "would rather wait" on converting, and he says he will *offer* it, which keeps conversion a choice. Amelia's "Just do what you have to do. We will deal with whatever happens. Together." is kept word for word. Nothing in it is invented plot, lore or backstory. The floor is held at 7.5 by the author's gesture ruling, plus one gate failure:
1. **Gesture clusters (Characters capped at 7.5).** (a) Directed-gaze beats: 4 in 240 words (L56 "She looked at the fork", L64 "Bal looked past her", L78 "He looked at the teacher… The man looked back"). Bal checks the watching teachers twice, at L64 and L78. (b) Lora's food held still in mid-air: 3 in 413 words (L42 "with the roll halfway to her mouth", L50 "stopped with her mouth open on the roll", L76 "Lora stopped eating. The butter knife stayed in her fist"). Ch.14 L158 also had Viridia's hand "stopped in the air halfway", so this class carries over from the last chapter.
2. **Gate FAIL (Ch.15's share).** `tic_report.py --gate` lists "sat down beside" 3x [ch 2, 14, 15]. Ch.15 L34 is one of the three.

Every fix is a cut or a few words. None adds plot. With F1–F3 applied the chapter projects to **Floor 8.5 / Casual 8.5: PASS.**

## Gate tools (scratch copy, Ch.1–15 at `/tmp/claude-0/-home-user/925d8686-989e-5134-a9ef-2d597d7cac42/scratchpad/ev15/manuscript/chapters/`)
- `voice_wear_check.py`: **FAIL**, but none of its hits are in Ch.15. "he was the one" (ch 8, 14 L194), "with it it was" (2 ch), "dead in the walls" (ch 14 x3). They belong to the Ch.14 revision now under way. No retired phrases.
- `tic_report.py --gate`: **FAIL**. Recurring prose phrases "dead in the walls" (ch14), "bal took it" (ch13, 14), **"sat down beside" (ch 2, 14, 15)**. Only the last one touches Ch.15 (L34; see F3). Ch.15 has no entries in the gesture-class table, and its rhythm reflexes are all 0. The clusters in F1/F2 are classes the tool does not classify.
- `style_check.py --dir manuscript`: **clean**.
- `grammar_check.py --file chapter-15.md`: 0 errors.
- Em dashes: **0**. "the way" similes: 0. Similes overall: 2 (L12 cushion, L46 pouring).

## Source fidelity (L706–715)
Each source beat, mapped to the chapter:
- "Gone all day but let me know if you need me", the kiss, she disappears: L6–12. ✓
- Extra work in every class, "even in crafting", "no one even got to chat": L18–22. ✓
- Lora joins them at the Blood table: L26–34. ✓
- The whole hall watching, teachers included: L32, L36. ✓
- They try to ignore the tension, and the easy feeling stays: L38–40. ✓
- Lora butters a roll and asks: L36, L42. ✓
- Bal finishes his drink and waits for the refill: L44–46. ✓ (expanded)
- "Dawn Team member card… Amelia Norheart": L48. ✓
- Lora's mid-bite pause: L50. ✓
- "Look what her family did to her… I would have felt the same way": L54. ✓
- Spaghetti, "happy to be friends… stays this easy": L54–56. ✓
- "What do you mean?" → "Stays easy how?": L58. ✓ (natural polish)
- The shrug and the rumor, word for word in meaning: L60–62. ✓
- Bal looks around at the watchers: L64. ✓
- "Probably… her being a Waves sygl? yea": L68. ✓ (Lora wears Kenmei's sygl at the Waves table, consistent with Ch.10/12.)
- The wince, "hoping he wouldn't ask", school rule = expel, Lead Mages = demerits: L72–74. ✓
- "probably a school rule" from the teachers' looks: L80. ✓
- The breath, "only one way": L82. ✓
- "There is something we could do but I'd rather wait": L84. ✓
- Both agree and are curious: L86. ✓
- The Blood common room, the herb room added that morning, Lora trying recipes: L92–100. ✓
- Raizen's wars and the runes homework: L98. ✓
- "Why are you reading that" / "started training… not going after Naisura": L104–106. ✓
- "Amelia's followers", Bal nods while reading: L110–112. ✓ (the nod is rendered as "Bal turned the page", which is good)
- Viridia quiet: L108, L116. ✓
- He would normally wait until they left, and wants Viridia to understand: L114. ✓
- The originators' reasoning (Raizen lowest, can't trap her again): L114. ✓ (spoken to Viridia, which is consistent with Amelia's later "what he had told Viridia")
- Amelia returned and asks why Viridia was quiet: L118, L124. ✓
- Kenmei, the teachers "pulled": L128. ✓
- "Yeah more than likely… way to bypass… hopefully it doesn't come to that yet… he's gonna lose it": L130. ✓
- Amelia not caring, "He's going to freak regardless": L132–134. ✓ ("lose it whenever it happens" keeps the meaning and is natural American)
- "It's still early… I hope I don't have to do it yet but I will… don't want to lose either of them": L136. ✓ "Do it" becomes "offer it", which matches the wish-only rule.
- Amelia moves closer, the Together line verbatim, head on his chest, asleep: L138–146. ✓

**Additions (all texture, no plot):**
- The mattress rising with nobody standing (L12).
- Porter's essay and the forms in the sand (L20).
- The cup filling from the bottom, and Bal looking under the table (L46). It fits the curiosity he showed about the plates in Ch.7.
- The knife payoff (L76/L88).
- The herb room's fittings (L94).
- The pump and "No, no, no, no" (L100).
- Amelia perched on the couch arm (L118).
- Her hair smelling of wind or pine (L142).

None of these is lore, a habit or backstory. One caution on L46: the refilling cup must not come back as a running bit.

**Continuity**
- Opening: the card propped by the lamp (L8) matches the Ch.14 ending, and does not depend on Ch.14's "where the note used to be" line (being revised).
- The green book (L94) matches Ch.13/14, and so does the poultice chapter read aloud.
- Lora's empty bench "as usual" (L28) matches Ch.12.
- Paper orders on the plate (L34) match Ch.7/10.
- Two slips:
  - **L46 "his first week."** It is still his first week; he arrived only a few days ago. F4.
  - **L144 "The weekend was close. Saturday, then."** Ch.16's source opens on a week of homework and Lora "growing more excited every day", so Saturday is several days off. F5.
- One soft logic point:
  - **L22.** Viridia shares three of Bal's four classes (Ch.9: Familiar, Warfare, Crafting), so "passed Viridia once in a corridor… that was all either of them said" can read as if they were apart all day. The source's point is that they had no chance to talk. F6, optional.

## Genesis Score (Craft Assessment)

| Dimension | Score | Evidence | Cap Reasons |
|-----------|-------|----------|-------------|
| Originality | 8.5 | The hall goes quiet table by table behind Lora: "she walked at the front edge of a quiet that kept growing" (L32). The self-filling cup Bal once checked under the table (L46). The mattress rising "Nobody had stood" (L12) shows Amelia teleporting without naming it. These are execution-level freshness on a stock beat (segregated houses, a friend crossing the room), which is what the genre asks for. | none |
| Theme | 8.5 | Belonging against separation by sygl is carried by action: Lora's walk, the rumored rule, Bal's offer kept back ("I'd rather wait", L84; "I hope I don't have to offer it yet", L136). It is never stated. Texture beyond the theme (pot roast, the pump, scorched ginger, socks) keeps it from becoming an echo chamber. | none |
| Characters | **7.5** | On merit 8.5. Viridia's withdrawal is shown by what she stops doing: "it was Bal who had to ask her how" (L116). Amelia: "had never in her life cared how Raizen felt about anything, and she did not start now" (L132). Lora's knife upright in her fist, which she doesn't know is there (L76), then "used it on her second roll" (L88). Each person is distinct by worldview and evasion, not tics. | **Gesture-class cap:** directed gaze 4 in 240 words (L56, L64, L78 x2); Lora's food suspended mid-bite 3 in 413 words (L42, L50, L76), a class carried over from Ch.14 L158. |
| Prose & Voice | 8.5 | Underlines: "Lora opened the door and smelled dried mint and did not come out again." (L96). "it was not the kind of thing you said over soup" (L82). "She buttered the first roll right out to the crust at every edge, while the whole hall watched her do it." (L36). "He was asleep before they reached the woods." (L146). Under pressure the voice goes clipped: "So the school would make it a rule. Probably." (L80). Ugly sentence present: "smelled faintly of somewhere that was not the castle, wind, maybe, or pine" (L142). American register throughout ("Yeah", "lose it", "How come"). | none |
| Pacing | 8.5 | Seven short movements with scene breaks. The make-up day is compressed to two paragraphs; the dinner is slowed to a walk the length of the hall; the evening runs in quick sound-cues (the pump, the hiss). Value shift: easy friendship (+) → the threat of expulsion (−) → "Together" (+, guarded). The hook lands on Saturday and the woods, as the outline asks. | — (F5 continuity on the hook) |
| Emotion | 8.5 | Anchor: the hall watching Lora sit and butter a roll (L30–36). Emotional surprise: the expulsion threat is met by a butter knife standing on its point, with Lora's body ahead of her mind (L76), which also passes the body-rebel test. It is warm, not anxious. Amelia's line closes on intimacy with no intensity words (L138–142). | none |
| Engagement (Dim 7) | 8.5 | Self-insertion: your friend crosses the whole hall to sit with you, and the goddess says "Together". Empathy: Viridia hearing that her own god is coming for you (L106–116). Fascination: what is the "something we could do"? | none |
| **FLOOR** | **7.5** | | Characters (mechanical gesture-class cap) |
| **AVERAGE** | **8.4** | (8.5×6 + 7.5) / 7 = 8.36 | |

Trajectory: Ch.14 also came in at Floor 7.5 on a gesture-class cap (couch-sinking). That is two chapters in a row capped on the same mechanism. See Cross-chapter patterns.

## CVI-Launch Breakdown
| Input | Score | Evidence |
|-------|-------|----------|
| Commercial Pacing | 8.5/10 | Short bridge (1,887w), breaks every ~250 words, ends on the coming job. |
| Tomorrow Test | 2 anchors (IMAGE + QUOTE) → 7 | Lora's walk and the buttered roll (image). "We will deal with whatever happens. Together." (quote) |
| Casual Reader | 8.5/10 | Warm and funny ("No, no, no, no" to something that hissed). Low stakes on the surface, but the expulsion threat gives it bite. |
| Shareability (quote/plot/emotional) | 3/2/3 → 5.7 | "Together" (quote); "they might ban the houses from mixing" (plot); Lora's walk (emotional). |
| Concept Pitch | yes | |
| Human Closeness | yes | Nearly all of it is friends at dinner and two people in bed talking. |

0.2×8.5 + 0.2×7 + 0.2×8.5 + 0.2×5.7 + 0.1×10 + 0.1×10 = 7.94 → 8.0, +0.5 strong anchor = **8.5**.
CVI-Legacy unchanged from Ch.14 at **6.2** (a bridge chapter adds no cultural vocabulary).

## Anti-AI Scan (20 patterns, 1,887 words; commercial/fantasy thresholds)
1. Forced symmetry: Found, 1 (0.5/1k), minor. "The Terra boys stopped. The Tempus table stopped." (L32). This is deliberate, because it stages the spreading silence.
2. Empty poetic vocabulary: Clear.
3. Automatic rule of three: Found, 2 (1.06/1k), moderate. "They both said all right, and they both meant it, and they were both plainly dying to know" (L86). "She didn't argue. She didn't ask anything else either. Her pencil…" (L116).
4. Em dashes: Clear (0).
5. Empty metaphors: Clear.
6. Dramatic "And" openings: Clear.
7. Pseudo-philosophical closings: Clear. The ending is concrete: asleep before the woods.
8. Excessive parallelism: Found, 1 (0.5/1k), minor. "Nobody chatted. Nobody got the chance." (L22).
9. Overly smooth transitions: Clear. The breaks are hard cuts.
10. Described emotions: Found, 1, minor. "plainly dying to know" (L86).
11. Explanatory extension: Clear. Similes stop at the image (L12, L46). Well under the Pattern-#11 cap.
12. Binary negation opener: Clear.
13. Precision flex: Found, 1, minor. "three places down the line… two tables over… two rolls" is natural counting, not a device.
14. Emotional control demonstration: Found, 1, minor. "Bal drew in a long breath and eased it out" → decision (L82). This is from the source.
15. Authoritative description: Clear. The herb room is pictured as Bal's wish, not catalogued as fact.
16. Philosophical asides: Clear.
17. Clean dialogue: Found, minor. The dinner talk runs in orderly turns, as the source has it. It is broken by Lora's full mouth (L50–52) and Viridia making him wait (L72).
18. Thematic echo chamber: Clear. The pump, the socks, scorched ginger and the self-filling cup are pure texture.
19. Graduated reveal: Clear. Watch: Ch.14 ended at bed and Ch.15 ends at bed. Both are source-mandated.
20. Emotional temperature report: Clear.

**7/20 present, almost all minor.** That is the Commercial clean band (0–8). No over-correction flag.

## Gesture hand count (author ruling: no class 3+ within 500 words)
| Class | Instances (line @ word offset) | Max in any 500w | Verdict |
|-------|-------------------------------|-----------------|---------|
| **Directed gaze (looked at/past/back)** | L56 @760 "looked at the fork"; L64 @820 "Bal looked past her"; L78 @990 "looked at the teacher"; L78 "The man looked back" | **4 in 240w** | **OVER: F1** |
| **Food/hand suspended mid-eat (Lora)** | L42 @560 "roll halfway to her mouth"; L50 @670 "stopped with her mouth open on the roll"; L76 @960 "stopped eating. The butter knife stayed in her fist" | **3 in 413w** | **OVER: F2** (Ch.14 L158 had the same class) |
| Watched (hall/teacher watching) | L20 x2, L36, L102 | 3 in ~250w (L20, L20, L36) | Under cap in spirit. L36 is the anchor and L20's two are separate rooms. Leave, but don't add another. |
| Smile/grin | 0 | — | clean |
| Laugh | 0 | — | clean |
| Blush | 0 | — | clean |
| Face-pulling | L22 x1 | 1 | clean |
| Shrug / wince | L60, L72 (source) | 1 each | clean |
| Breath beat | L82 x1 | 1 | clean |
| Hand squeeze / hand on hand | 0 (L142 hand on back x1) | 1 | clean |
| Couch-sinking / sitting back / leaning in | L86 leaned in, L102 sat back | 2 in ~200w | under cap; don't add a third |
| Laced fingers | L130 laced / L142 unlaced (one gesture, paired) | 1 | clean |
| Wide eyes | L86 x1 | 1 | clean |
| Gestures shared between characters | none. Viridia's hand-pull and Lora's ear-tuck are absent. | — | clean |
| Tics / catchphrases / "Master" | none ("Master" not used) | — | clean |

Lexical watch: "stopped" appears 7 times in L28–L76 (about 600 words). L32's run is deliberate, and L50/L76 go with F2.

## Character Chaos Check (Bal)
- Irrelevant thought: **present, inhabited.** The cup and looking under the table (L46). "between waking up and finding his socks" (L94).
- Cognitive distortion: absent. Fitting: Bal reads the threat accurately.
- Unprompted memory: present and triggered. The cup prompts the first-week memory, which returns straight to the scene. L94's memory of picturing the room is triggered by the door.
- Failed emotional management: mild. "He meant to figure… He was asleep before they reached the woods." (L146)
- Voice under pressure: demonstrated, "So the school would make it a rule. Probably." (L80).
Commercial/fantasy needs 2–3 of 4: met.

## Secondary Character Chaos
- **Lora:** has her own moment. The knife she doesn't know she's holding (L76/L88); "No, no, no, no" (L100).
- **Viridia:** has her own moment. The spaghetti wound "long after it was wound" (L54); she goes quiet and stops asking (L116).
- **Amelia:** has her own moment. Swinging one foot on the couch arm, asking what burned (L118); not caring about Raizen (L132).
No one functions only as a tool.

## The Tomorrow Test
**What the reader remembers:** Lora walking the whole length of the hall while it goes quiet behind her, then buttering her roll to the crust with everyone watching. And "We will deal with whatever happens. Together."
**Anchor type:** BOTH.
**Verdict:** ANCHOR EXISTS. The image type differs from Ch.14's (a gift/card reveal), so there is no repetition.

**Shareability:** "Lora walked across the whole silent dining hall to sit at the forbidden table." That is a one-sentence share.

## Reader Reports
**The Devourer:** Moves fast. The make-up day is two paragraphs, so there is no stall. The threat of expulsion and Bal's secret "something" pull them through, and Saturday's job pulls them into Ch.16. They might skim L114's explanation of the gods' reasoning, which is the longest paragraph and pure summary. Not a stopping point.

**The Critic:** Underlines L96 (the mint), L82 (soup), L132 (Raizen), L36. Likes that Viridia's silence is shown by her not asking about Lora's recipe. Disappointed by the doubled teacher stare (L64 and L78 make the same point twice) and by the three suspended-food beats for Lora in a row.

**The Hostile:** Challenges three things. "His first week". It is his first week. Why does "passed Viridia once in a corridor" seem to mean they never shared a class, when they share three? "The weekend was close": next chapter it is a whole week away. No logic hole in the magic. The teleport and the room-making are consistent with earlier chapters.

**The Casual Reader:** Likes these people and wants to sit at that table. The walk down the hall is the "you have to read this" moment, and the bed scene is cozy, not saccharine. Keeps reading. **8.5.**

**The Devoted Reader (fantasy/series):** Clocks "that rule sounds like something Kenmei would suggest" and the Raizen-ranks-lowest politics as setup. Notes that the card on the nightstand opens and closes the chapter. Will watch whether the self-filling cup recurs. It should not.

## Cross-Reader Matrix
| Issue | Devourer | Critic | Hostile | Casual | Devoted | Severity |
|-------|----------|--------|---------|--------|---------|----------|
| Gesture clusters (gaze; Lora mid-bite) | – | ✓ | – | – | – | INVESTIGATE (but **mechanical cap: blocks gate**) |
| "sat down beside" gate fail | – | ✓ | – | – | – | INVESTIGATE (**gate: blocks**) |
| "first week" | – | – | ✓ | – | ✓ | SHOULD FIX |
| "weekend was close" vs Ch.16 | – | – | ✓ | – | ✓ | SHOULD FIX |
| Corridor-only contact with Viridia | – | – | ✓ | – | – | INVESTIGATE |
| L114 summary paragraph | ✓ | – | – | – | – | INVESTIGATE (source content; leave) |

## Revision Recommendations (Ranked; surgical, no plot added)

| # | Location | Problem type | What happens now | Why it fails | Revision direction | Project rule? |
|---|----------|-------------|-----------------|-------------|-------------------|--------------|
| F1 | L56 and L78 | Character (gesture cluster) | L56: "She looked at the fork." L78: "He looked at the teacher who was watching them. The man looked back." | Four directed-gaze beats in 240 words. L78 repeats L64's "One of the teachers had not bothered to turn his back at all." | **Cut L56's last sentence** ("She looked at the fork."); the line reads `"I'm happy to be friends with her. With all of you, really. I just hope it stays this easy."` **Delete L78 entirely**; L80 "So the school would make it a rule. Probably." follows L76 and still rests on L64. | Yes: one look at the watchers per scene. |
| F2 | L42 and L76 | Character (gesture cluster, cross-chapter) | L42: "Lora asked, with the roll halfway to her mouth." L76: "At *expel*, Lora stopped eating. The butter knife stayed in her fist, upright…" | Three mid-bite freezes for Lora in 413 words; Ch.14 L158 had Viridia's hand stopped "halfway". L50's pause is the source's own ("paused in mid bite") and stays. | L42 → `"So what was it you gave Amelia?" Lora asked.` L76 → `At *expel*, the butter knife in Lora's fist came upright on the tablecloth, point to the ceiling, and Bal doubted she knew it was there.` (keeps the L88 payoff; drops "stopped eating") | Yes: no "stopped/halfway" freeze two chapters running. |
| F3 | L34 | Style (gate fail) | "She sat down beside Viridia, opposite him," | Third book-wide "sat down beside" (ch 2, 14, 15); tic_report --gate fails. | → `She took the bench beside Viridia, across from him,` | No |
| F4 | L46 | Logic | "He had looked under the table, his first week." | It is still his first week. | → `He had looked under the table, his first night.` (Ch.7's first hall meal, where he wondered who washed the plates) | No |
| F5 | L144 | Continuity | "The weekend was close. Saturday, then." | Ch.16's source: a week of homework, Lora "more excited every day". Saturday is days off. | → `The weekend was a few days off. Saturday, then.` | No |
| F6 (optional) | L22 | Logic | "Bal passed Viridia once in a corridor between classes… that was all either of them said to the other until dinner." | She shares three of his classes (Ch.9), so this reads as if they were apart all day. | → `Viridia sat in three of his four classes, and the most either of them managed was a face she pulled at him over an armload of books in the corridor.` | No |
| F7 (optional) | L108 | Style | "Viridia was quiet." before her line | The source's "quiet after that" is L116. This one spends it early. | Cut L108; L110 follows L106 directly. | No |

### Fix order: F4/F6 (logic) → F1/F2 (character cap) → F5 (continuity) → F3/F7 (style)

After F1–F2, recount: gaze 2 in 240w (L64 "looked past", "Bal's eyes reached him"); suspended food 2 in 302w (L50, L76). Both are under the cap.

## Strengths to PRESERVE
- L12 "Nobody had stood. Her side of the bed was smooth." Teleport by absence.
- L30–36 the walk and the roll. Do not add a gesture to it.
- L76/L88 the knife and its payoff.
- L96 the mint line; L100 "No, no, no, no"; L116 "it was Bal who had to ask her how".
- L132 Amelia not caring about Raizen, in place of the source's shrug.
- L136 "offer it", which keeps conversion by wish.
- L140 Amelia's line verbatim; L146 the last line.
- 0 em dashes, 0 smiles, 0 laughs, 0 blushes, no "Master".

## Cross-chapter patterns (pipeline fingerprint)
Ch.14 and Ch.15 are both capped by a gesture cluster. Each time it is a *new* class, because the editor removes the flagged one and the beats migrate: couch-sinking in Ch.14, eye-direction and mid-bite freezes here. The writer is reaching for a body beat between dialogue lines at about the same rate either way. Standing instruction: where a beat is wanted between two lines of the author's dialogue, prefer no beat, or a sound or object in the room (the pump, the cup), over a look or a pause.

## PATH TO 8.5
- **Characters 7.5 → 8.5 requires:** only the mechanical cap lifted. Apply F1 (cut "She looked at the fork."; delete L78) and F2 (L42 drop "with the roll halfway to her mouth"; L76 drop "Lora stopped eating" and keep the knife). On merit the cast is already 8.5: Viridia's silence enacted at L116, Lora's unwitting knife, Amelia's indifference to Raizen. No other surgery.
- **Gate:** F3 (L34 "took the bench beside Viridia"). The remaining voice_wear/tic_report failures are Ch.13/14 phrases and clear with the Ch.14 revision.
- All other dimensions sit at 8.5. F4–F5 protect Pacing and Characters from the Hostile reader; they are not needed for the floor.

## VERDICT
**POLISH.** Genesis Floor 7.5 (Characters, mechanical gesture-class cap); Average 8.4; Casual 8.5. Apply F1–F3 (and F4–F5) and the chapter projects to **PASS at Floor 8.5**. A recount of the two windows and a re-run of `tic_report.py --gate` confirm it; no full re-score is needed.

BIAS CHECK: This evaluation was produced by the same system that wrote the prose. Confidence in scores above 8.0 requires external validation (beta readers, editors, comp analysis).
