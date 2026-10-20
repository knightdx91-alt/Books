# Evaluation: Chapter 12 — I Like You Too
**Evaluator:** book-evaluator | **Date:** 2026-10-20 | **Draft:** R1 (1,410 words of text; target 1,500, range 1,300–1,900; short single-scene chapter by design)

## HEADLINE
**CVI-Launch:** 8.9 (8.4 + 0.5 strong anchor) | **CVI-Legacy:** 6.1 | **Genesis Floor:** 8.5 | **Genesis Average:** 8.5
**Engagement type:** Self-Insertion (primary) / Empathy (secondary) / Fascination (tertiary)
**Divergence alert:** none. Launch is above Legacy, the same profile as Ch.6–11.

**VERDICT: PASS** (Floor 8.5, Casual 8.5). The chapter is light, warm and playful, which is what the author asked for. It is one dinner scene. "And Viridia? I like you too." is its heart, and the dropped fork lands it. Every source beat is present, in source order, with the right speaker. Nothing in it is invented plot, character, habit or backstory. Four small surgical fixes follow (F1–F4). **F1 and F2 should go in before commit.** They bring two lines back toward the author's script. None adds plot, and none needs re-scoring.

---

## Mechanical gates
I ran these on a scratch copy of Ch.1–12, laid out as `manuscript/chapters/chapter-N.md`, at /tmp/claude-0/-home-user/925d8686-989e-5134-a9ef-2d597d7cac42/scratchpad/ev12.
- `voice_wear_check.py`: **clean.** No retired phrases and no device over cap. The one soft self-repetition WARN is book-wide, non-gating, and is not from this chapter.
- `tic_report.py --gate`: **clean.** Auto-recurrence: none. Ch.12 rhythm: and-chains 0, negation pivots 0, 'So' openers 0. No Ch.12 gesture class appears in any "worst chapter" column. By hand count: shrug 1 (L38, from the source), grin as a tag 1 (L104, from the source), laugh 1 (L52, from the source), glance 1 (L94), nod 0 (the source's "Bal nods" is rendered without a nod, L56). Nothing picked up and set down.
- `style_check.py --dir`: **clean.** Similes 2.8/1k, adverbs 8.5/1k, em dashes 0. No distinctive cross-chapter repeated phrase.
- `grammar_check.py --file`: 0 errors.
- "the way [x]": 0. Filter words appear only inside dialogue ("really", "just"), where they are natural speech.
- **"Master"**: 0. The source has none here. Correct.
- **Gesture ownership:** Bal takes Viridia's hand (from the source). There is no hand or sleeve pull, so Viridia's gesture is untouched. Lora's hair-behind-the-ear is not used, and stays saved for Ch.13. Lora's glasses push (L8) is her own established physicality (Ch.10).
- **Dialogue density:** about 27%, normal for this lane.

## Source fidelity (L541–593: Lora at the Waves table to "You better")
- **Every beat is present, in order:**
  - Lora alone at the Waves table, the shy smile, and her eyes going back to her food (L8).
  - "That's someone else who needs a little time", as a thought (L12).
  - The usual breakfast for dinner (L16), and Viridia cutting into a steak (L14).
  - Viridia noticed Lora noticing him ("She saw you", L24). She asked Lora again and Lora refused (L24–28).
  - Lora is shy and will take a while to open up (L30). Sitting at the Blood table would make her a target (L32).
  - The fork stopped halfway to his mouth (L34), then "The others haven't tried anything with you… have they?" (L36).
  - The shrug; snide comments, nothing physical; the Tempus students who won't talk to her; the grin; "funny they think I care"; others, even from other sygls, asking about him (L38–40).
  - The oatmeal swallowed (L42), then "Asking about me? Why?"
  - Her speech: High Priest, originator as familiar, every day, no one else, once a year at the start of school, "They want to know what it's like" (L48).
  - "Then why don't they come and ask me?" Her laugh. Amelia's favor and not angering her; others might treat them the same way; "give them time" (L50–54).
  - Bal knows it is true (L56).
  - Getting Amelia to eat with them, and the mystery (L60). The diary warning, "may or may not" (L60).
  - The cough on her drink, **restaged** (L62–64). In Ch.7 she inhales pizza and gulps water. Here the drink slops across her steak and she grabs a napkin. The bible's "stage it differently" requirement is met.
  - "She did what?" (L66). The nervous look; Amelia had been telling the truth (L68).
  - "Priest stuff", and Amelia reading the diary (L72).
  - "How'd you know it was mine?" and the color (L74–76).
  - "really cute when you blush", meaning every word of it, pinker; the name on the front; "Your secrets are safe with her" (L78).
  - Avoiding his eyes (L80). "Couldn't resist" becomes "He could have let it go there. He didn't." (L82).
  - **"And Viridia?"** He waits for her eyes. **"I like you too."** (L84–88).
  - The dropped fork (L90–92). "But you… you said she only told you it was my diary!", cried out (L94).
  - He takes her hand; "honestly all she told me. I promise"; the courage line (L96–98).
  - She wipes her eyes with her other hand. "That was still mean." (L100–102). The grin. "I'll find some way to make it up to you." "You better," muttered, her hand still in his (L104–110).
- **Speakers, meaning and placement are kept everywhere.** The polish is natural American speech ("Some of the Tempus kids won't talk to me anymore"; "How'd you know it was mine?"). There are two exceptions. One softens the author's register (F1). The other changes the source's "like he's crazy" into a different comic image (F2).
- **Additions, all texture, none plot:**
  - Lora's empty bench gap (L8).
  - The paper order, continuing from Ch.9–10 (L16).
  - Viridia eyeing the breakfast and then the sunset window, a wordless breakfast-for-dinner joke (L18).
  - The empty place where Amelia appeared yesterday (L20, consistent with Ch.7 L215–229).
  - The Terra boys and the bread rolls (L58, L114).
  - The steak cut down to crumbs (L80).
  - The fork's two bounces (L92).
  - The walk back (L114–116). The "spear partner's shins" calls back Ch.10 L198.

  None adds a named character, a habit, backstory or lore. The one exception is the lamps lighting "on their own" (L114), a small piece of invented castle magic. It is optional fix F4.
- **Seam with Ch.11:** Ch.11 ends on Bal not knowing "what his face ought to do about that". Ch.12 pays it off at L70: "Bal's face would not stay straight." It does not restate Ch.11's last line. Well done.
- **Seam with Ch.13:** the hook (L118) uses the source's banging (L595), as the outline directs. **Ch.13 must open after the banging** (Amelia asleep, the hurry to the door) and must not restate it.
- **POV:** Bal only throughout. Lora leaving is "never saw Lora go" (L114). Correct.

## Spell / magic-effect watch
No spells. The on-page magic is the castle's own: the paper order and plates that vanish, both established in Ch.7. The self-lighting lamps (L114) are new, and F4 removes them. No ledger update is needed.

## Genesis Score

| Dimension | Score | Evidence | Cap Reasons |
|-----------|-------|----------|-------------|
| Originality | 8.5 | A confession set up by a goddess reading the girl's diary and paid off at breakfast-for-dinner. The fresh execution is the fork that "neither of them went under the bench after" (L110), and the sunset-window joke, which is never spoken (L18). Familiar romance beat, fresh take | none (romance: fresh take on a familiar beat) |
| Theme | 8.5 | Being chosen, and being given time, carried by action. Lora "needs a little time" (L12); sitting here would be "choosing a side" (L32); Viridia, a Tempus girl, "choosing to sit with him" (L32). It sits against plenty of texture with no theme in it (the rolls, the steak, the shins). One narrator line underlines the motif: "Everybody needed time today." (L56, F3) | none |
| Characters | 8.5 | Cover-the-name passes. Viridia is dry and doesn't hedge: "It's funny they think I care" (L40); "That was still mean" (L102). Bal is plain and frank: "Then why don't they come and ask me?" Lora is shy without a word (L8). Chaos 3/4, inhabited, not narrated: an irrelevant thought (the Terra rolls, L58); a memory set off by the scene that comes back to it (the empty place at his elbow, L20); failed management (L70, "Bal's face would not stay straight"; Viridia cutting her steak to crumbs, L80; her outburst, L94). There is no fixed chaos cadence. No tics, no shared gestures | no cap; gesture gate clean |
| Prose & Voice | 8.5 | Stopping sentence (romance variant, warmth): "She kept her hand where it was, inside his, on the table between the oatmeal and the ruined steak, and neither of them went under the bench after the fork." (L110). Underlines: "Bal smiled back. She didn't see it." (L10); "He could have let it go there. He didn't." (L82); "He could have taken the stairs three at a time. Maybe he did. He didn't remember them." (L116); "The second roll went into a girl's soup, and the friends cheered anyway." (L58). Ugly sentence: "Nobody ever sat at it but Bal and one Tempus girl choosing to sit with him…" (L32). Voice under pressure: Viridia's voice "came out thin and wet" (L66), and the louder outburst (L94); the prose goes clipped at the confession (L84–90) | #11 at 1 instance (L68, 0.7/1k), under the commercial cap |
| Pacing | 8.5 | One scene, as the outline designs it. The value shift is clear: unspoken (a diary he hasn't read) → spoken and mutual (her hand in his). Speed varies: slow table-setting (L14–20), quick banter (L36–54), a comic burst (L62–66), stillness at the confession (L84–90), then summary (L114–116). Hook: "It was barely light when something started pounding on the wall of his dorm." (L118). It is a modest hook, but it is the source's next beat | 6% under target, by design. Not a cap |
| Emotion | 8.5 | Anchor: the dropped fork. It "rang off the silver… two little bounces and then nothing. Viridia's hand stayed in the air where the fork had been." (L92). Surprise: tears in a comic scene, followed straight away by "That was still mean." (L100–102). Body rebel: the cough (L64), red "to the hairline" (L94), the wiped eyes (L100). The peak is carried by objects (fork, napkin, hand) with no intensity words | none |
| Engagement (Dim 7) | 8.5 | Self-insertion: the girl across the table likes you, and you get to say it first and then hold her hand. Empathy comes through Viridia's mortification and Lora's lonely gap on the bench | none |
| **FLOOR** | **8.5** | | |
| **AVERAGE** | **8.5** | | |

Trajectory: Ch.1–11 are all 8.5, and Ch.12 holds. It is the warmest chapter so far, and the short length suits it.

## CVI-Launch Breakdown
| Input | Score | Evidence |
|-------|-------|----------|
| Commercial Pacing | 8.5 | Short, one scene, a payoff the reader was promised in Ch.11, and a dawn hook |
| Tomorrow Test | 2 anchors (7) | IMAGE: the fork under the bench that neither of them picks up. QUOTE: "And Viridia? I like you too." |
| Casual Reader | 8.5 | A cute confession, a likable couple, a funny cough, no lag |
| Shareability (quote/plot/emotional) | 4/3/4 (7.5) | "He just says 'I like you too' and she DROPS HER FORK"; "That was still mean." |
| Concept Pitch | yes (10) | |
| Human Closeness | yes (10) | Intimate conversation is the whole chapter |

CVI-Launch = 0.2(8.5) + 0.2(7) + 0.2(8.5) + 0.2(7.5) + 0.1(10) + 0.1(10) = 8.3, plus 0.5 for the strong anchor = **8.8–8.9** (reported as 8.9).
CVI-Legacy (default weights) = 0.3(8.5) + 0.25(8.5) + 0.2(2) + 0.15(4) + 0.1(5) ≈ **6.1**.

## Anti-AI Scan (20 patterns; commercial thresholds; 1,410 words)
1. Forced symmetry: Clear.
2. Empty poetic vocabulary: Clear.
3. Automatic rule of three: Found, minor (1): the escalating cuts, "in half… smaller… smaller again" (L80). This one is comic and earned.
4. Em dashes: Clear (0).
5. Empty metaphors: Found, minor (1): "the kind of look usually saved for somebody who had walked into a door" (L46). It is a stock construction, and the same frame as Ch.9 L174 ("the kind of looks you might send a dog that had turned out to be a bear"). See F2.
6. Dramatic "And" openings: Found, minor (1): "And there was the table itself." (L32). "And Viridia?" is dialogue from the source.
7. Pseudo-philosophical closings: Clear. The chapter ends on a sound, not a maxim.
8. Excessive parallelism: Clear.
9. Overly smooth transitions: Clear. The single break is a hard cut.
10. Described emotions: Clear. "In shock" from the source becomes the hand left in the air.
11. Explanatory extension: Found (1; 0.7/1k): "and nerves were an answer all by themselves" (L68). This is under the cap of 0.8/1k, but close to it. See F3.
12. Binary negation opener: Found, minor (1): "Her face held no anger at all, only nerves" (L68). Same line as #11.
13. Precision flex: Clear ("three more people" and "two little bounces" are characterful).
14. Emotional control demonstration: Clear.
15. Authoritative description: Clear.
16. Philosophical asides: Found, minor (1): "Everybody needed time today." (L56).
17. Clean dialogue: Clear. She talks around a mouthful (L40), restarts ("But you… But you *said*", L94), and her coughing interrupts her (L64–66).
18. Thematic echo chamber: Clear overall. There is plenty of noise, but L56 nudges the "time" motif.
19. Graduated reveal: Clear. Single-scene structure, different from Ch.11's three-stop chain.
20. Emotional temperature report: Clear.

**Total: 6 minor patterns.** That is CLEAN for commercial fiction (0–8). There is no over-correction flag.

## Character Chaos Check (Bal)
- Irrelevant thought: present: the Terra boy stacking bread rolls (L58), paid off at L114.
- Cognitive distortion: absent. Absence is not a defect; the chapter is a happy one.
- Unprompted memory: present. The empty bench sets it off (Amelia at his elbow yesterday, L20), and it comes back to the present ("stayed a plain stretch of wood").
- Failed emotional management: present. "Bal's face would not stay straight." (L70); the giddy amnesia on the stairs (L116).
- Voice under pressure: not tested. This is not a crisis chapter. The prose does tighten at the confession.

## Secondary Character Chaos
- **Viridia:** has her own moments. The coughing fit, the steak cut to crumbs, the outburst heard two tables down, the tears and "That was still mean."
- **Lora:** a single smile and the glasses push. That is all the source gives her here, and it is right.
- **Amelia:** absent from the scene, as in the source. She is present through the empty bench (L20).

## The Tomorrow Test
**What the reader remembers:** the fork ringing off the plate and landing under the bench, Viridia's hand still in the air, and the two of them leaving the fork there while they hold hands. Close second: "And Viridia? I like you too."
**Anchor type:** BOTH (image + quote).
**Verdict:** ANCHOR EXISTS. It is a different type from Ch.11's anchor (a told tale and a window).

**Shareability:** "He tells her 'I like you too' and she drops her fork, cries, and goes 'That was still mean.'" Yes.

## Reader Reports
**The Devourer:** Reads straight through, with no stop point. The confession was promised by Ch.11's last page and arrives inside 1,400 words. The dawn banging pulls them into Ch.13. They skim L16–20 (the order, the empty bench) as setup.
**The Critic:** Underlines L110, L82, L116 and L10. Likes the window joke being left unspoken (L18) and the fork left on the floor. Would query: the "kind of look… walked into a door" frame, which echoes Ch.9 (L46); "nerves were an answer all by themselves" (L68), which explains itself; and "Everybody needed time today" (L56) underlining the motif.
**The Hostile:** (1) "Afterward not one word of it stayed with him" sits next to a list of what they talked about (L114). This is defensible: he remembers the topics but not the words. (2) The lamps that "came up on their own" are new castle magic that no earlier chapter shows (L114). (3) Viridia "busies herself with eating" in the source, but in the chapter she doesn't eat at all (L80). This is a comic expansion that keeps the beat's meaning, which is avoiding his eyes. Acceptable. (4) "Make her mad" is softer than the author's "piss her off", against Viridia's casual teen register (L54).
**The Casual Reader:** Stays and smiles. The girl confesses, sort of, by accident, and he says it back. It is short, sweet and funny, and they like both of them. 8.5.

## Cross-Reader Matrix
| Issue | Devourer | Critic | Hostile | Casual | Severity |
|-------|----------|--------|---------|--------|----------|
| "make her mad" softens the author's line (L54) | | | X | | INVESTIGATE (fidelity: fix, author direction) |
| "kind of look… walked into a door" repeats Ch.9's frame and shifts "crazy" (L46) | | X | X | | SHOULD FIX |
| "Everybody needed time today." (L56) | | X | | | INVESTIGATE |
| L68 self-explaining line | | X | | | INVESTIGATE |
| Self-lighting lamps (L114) | | | X | | INVESTIGATE (invented lore) |
| L16–20 setup skimmable | X | | | | INVESTIGATE (keep; it is short) |

## Revision Recommendations (Ranked)

| # | Location | Problem type | What happens now | Why it fails | Revision direction | Project rule? |
|---|----------|-------------|-----------------|-------------|-------------------|--------------|
| F1 | L54 | Voice (source fidelity) | "Because Amelia's made it pretty obvious she favors you, and nobody wants to make her mad." | The author's line is "they don't want to piss her off". That is Viridia's casual American teen register (bible: "Nah", "jerk", "lame"), and the author asked for "more like my original script". Sanding it down is not grammar polish. | "Because Amelia's made it pretty obvious she favors you, and nobody wants to piss her off." | No |
| F2 | L46 | Style / fidelity | "Viridia gave him the kind of look usually saved for somebody who had walked into a door." | The same "the kind of look(s) [you'd give] X" frame as Ch.9 L174, so a construction is starting to recur. It also changes the source's meaning, "like he's crazy", into "clumsy". | "Viridia looked at him like he'd lost his mind." | Yes: "the kind of look(s)…" comparison frame is spent (Ch.9, Ch.12). |
| F3 | L56; L68 | Style (#16 / #11–12) | "Everybody needed time today. It was hard to argue with her when she was right." / "Her face held no anger at all, only nerves, and nerves were an answer all by themselves." | L56: the narrator points at the motif the dialogue already carries. L68: a not-X-only-Y line that then explains itself. Together they are the chapter's only AI-pattern hits of any weight, and they sit close to the #11 cap. | L56: cut the first sentence. Keep "It was hard to argue with her when she was right." L68: "There was nothing on her face but nerves. Amelia hadn't been teasing him on that bed. She had been telling the truth." | No |
| F4 | L114 | Continuity (invented lore, optional) | "the lamps along the walls came up on their own to make up for it" | Self-lighting lamps are new castle magic. They are small, but no earlier chapter or the source shows them. | "and the lamps along the walls were lit." | No |

### Fix order: F1, F2 (fidelity) → F3 (prose) → F4 (optional). All are line-level, none adds plot, and the word count changes by less than 10 words.

**Ch.13 handoff note:** Ch.12 already uses the banging. Ch.13 should open after it (Amelia still asleep, Bal hurrying to the door in his boxers) and should not restate the pounding as its first line.

## Strengths to PRESERVE
- L110: the hand "between the oatmeal and the ruined steak", and the fork nobody fetches. This is the chapter.
- L82: "He could have let it go there. He didn't." It renders the source's "couldn't resist" in Bal's own plain voice.
- L18: the unspoken breakfast-for-dinner joke through the sunset window.
- L62–66: the cough, restaged so it does not echo Ch.7's pizza choke.
- L70: "Bal's face would not stay straight." The seam with Ch.11's last line.
- L116: the stairs he can't remember. Giddiness rendered without naming it.
- Lora: the gap on her bench and the smile "gone nearly as soon as it started", with no invented business and the hair-tuck held for Ch.13.

## PATH TO 8.5
Floor is 8.5, so no dimension is below the gate. To hold it, apply F1–F3. If a later pass wants Emotion at 9.0, the place to work is L100. Give one beat more weight to the moment between "wiped her eyes" and "That was still mean": for example, a laugh caught inside the tears, using only her body and no intensity words. Do not add lines or plot.

## VERDICT
**PASS** (Genesis Floor 8.5, Average 8.5, Casual 8.5). Apply F1–F2 (and preferably F3) before commit. No re-score is needed.

BIAS CHECK: This evaluation was produced by the same system that wrote the prose. Confidence in scores above 8.0 requires external validation (beta readers, editors, comp analysis).
