# Evaluation: Chapter 2 — The Queen in the Temple
**Evaluator:** book-evaluator | **Date:** 2026-10-20
**File:** manuscript/chapter-02.md (2,839 words; outline target 4,200) | **Source span:** Sygl_Complete.txt L14–110 (Amelia steps out of the darkness through "Are you thirsty?")
**Lens:** adapted run (faithful revise/expand). Commercial fantasy with romance elements; Self-Insertion primary, Empathy secondary. Judged on its own terms: light, warm, playful; Amelia open, confident, flirtatious. Fidelity to the source is a requirement, not a weakness.

## HEADLINE
**CVI-Launch:** 8.7 (8.2 + 0.5 anchor bonus) | **CVI-Legacy:** 5.9 | **Genesis Floor:** 7.5 | **Genesis Average:** 8.0
**Engagement Type:** Self-Insertion (primary) / Empathy (secondary) / Fascination (tertiary)
**Divergence Alert:** none at the 2.0 threshold (Launch vs Floor = 1.2). Commercially the chapter works; two mechanical caps hold the craft floor down, and both can be fixed in the same pass.
**Verdict:** **POLISH** (Floor 7.5 < 8.5). Casual Reader 8.5.

## Genesis Score

| Dimension | Score | Evidence | Cap Reasons |
|-----------|-------|----------|-------------|
| Originality | 8.5 | The inverted-actor premise becomes concrete here: a goddess offers to be a sygl-less boy's *familiar* ("I will bond myself to you as your familiar. Doing so will free me from this place.", L151). Fresh execution touches: "one boy who tried to talk them open by being very polite to them. I rather liked him." (L23); the single bat wisp that "vanished before it reached the floor" (L117). | — |
| Theme | 8.0 | "Being wanted for who you are" is seeded by the source line "Even without my magic, you're still powerful in your own right" (L125), and the empty place kept for her at the claiming mirrors the boy no school will take without a sygl, without anyone stating the parallel (L103–105). But the mirror sits inside a summary block and is told twice (L101–105 narrated, then L109 "He took a breath and explained it to her, all of it"). | — |
| Characters | 7.5 | Amelia is vivid and in register: playful ("I won't bite. Not without asking.", L69), quick ("Only when I'm cross", L121), with her calm-menace edge visible ("I should like to see them try", L155). Bal's tongue-tied boy has a lived interior (the planned speech, L13). Chaos 3/4. | **CAP 7.5: gesture class at cap.** Amelia's LAUGH class = 4 in 2,839 words (L25 "she laughed out loud", L29 "laughed again", L83, L149), plus "delighted" ×2 (L23, L149). Cap = 4 for this length. Only 3 of the laughs are in the source; the sock laugh (L25) is added. Also "Amelia laughed, delighted, and" recurs verbatim in Ch.3 (style_check informational list). |
| Prose & Voice | 7.5 | Warm, plain, conversational, past tense, 0 em dashes, no filter words. Lines worth underlining: "Cutting off the hand doesn't cut out the blood." (L93); "a door someone had bricked up while he was too small to know there was a door there at all" (L97); "swung her feet beneath the hem of her dress like a girl half her apparent age" (L149); "I won't bite. Not without asking." (L69). Voice changes under pressure (short sentences at the bats, L113). | **CAP 7.5: Pattern #11 density.** 5 explanatory extensions in 2.84k = 1.76/1K (commercial cap 0.8/1K): L31, L55, L97, L99, L131. Pattern #12 adds 3 more (L97 ×2, L131). |
| Pacing | 8.0 | Single-scene dialogue chapter as the outline ledger says. Clean value shift (no sygl, no school → a way out, L129 → L151) and a strong end hook ("Are you thirsty?", L171). Speed variation works (the bats burst after a slow stretch). The drag is L95–109: about 450 words of exposition, then the same content summarized again as Bal's off-stage explanation. The bats' trigger therefore happens in summary. Length 2,839 vs 4,200 target (−32%). | — |
| Emotion | 8.0 | Anchor lands (the bats, L113–117). Emotional surprise is present: comedy straight after terror ("Does that happen often?" / "Only when I'm cross"). Body rebel is present: "He didn't decide to; his legs simply took him there" (L87). Techniques: physical, humor, longing (L163 school daydream), attraction (L143). | Not capped; held at 8.0 because the outrage that causes the bats builds off the page (L109 summary). |
| Source Fidelity (Dim 7) | 8.5 | Every source beat is present, in order, with the author's dialogue near-verbatim. Canon is respected (see Source Fidelity check below). Additions are texture or playful lines that do not change meaning. Minor slips: L55, L35, L55/L163. | — |
| **FLOOR** | **7.5** | | Characters (laugh class), Prose (#11 density) |
| **AVERAGE** | **8.0** | | Gap 0.5; no single-dimension bottleneck beyond the two caps |

## CVI-Launch Breakdown
| Input | Score | Evidence |
|-------|-------|----------|
| Commercial Pacing | 8/10 | One scene, short, ends on a question that forces the page. The exposition stretch L95–109 is the only drag. |
| Tomorrow Test | 3 anchors (1 image / 2 quote) → 9 | The bats; "I won't bite. Not without asking."; "Are you thirsty?" |
| Casual Reader | 8.5/10 | Likable, funny, flirtatious, and a goddess who explodes into bats. |
| Shareability (quote/plot/emotional) | 3/3/2 → 5.7 | Quote: "Cutting off the hand doesn't cut out the blood." Plot: "the vampire goddess offers to be his familiar." Emotional: mild. |
| Concept Pitch | yes → 10 | "Orphan with no hand finds the forgotten blood goddess sealed behind his orphanage; she offers to be his familiar." |
| Human Closeness | yes → 10 | The whole chapter is a two-person intimate conversation. |
| **CVI-Launch** | **8.2 + 0.5 (strong anchor) = 8.7** | |

CVI-Legacy (default weights): Originality 8.5×.30 + Theme 8.0×.25 + Cultural vocab 3×.20 + Re-readability 4×.15 + Identity 3×.10 = **5.9 at chapter level.** This is normal for a single early chapter. The re-read plant is the itching stump paying off ("The itch was there again, under the skin, sharper than he'd ever felt it", L79).

## Mechanical gates (run by evaluator)
- `style_check.py --dir manuscript`: **clean** (simile 2.8/1k, em-dash 0, no gated repeats; informational ×2: "amelia laughed delighted and" Ch.2/Ch.3).
- `tic_report.py --gate` and `voice_wear_check.py`: **DID NOT RUN.** Both hard-code `manuscript/chapters/` (voice_wear_check.py L33), but this book uses a flat `manuscript/`. tic_report refuses: "no chapters found … refusing to report a clean result". **STATE.yaml / CLAUDE.md say "tic/voice-wear gates clean" for Ch.1–3; that claim is unverified.** Pipeline fix: point the per-book tools at `STATE.yaml adaptation.manuscript_path` or accept `--dir`. The laugh-class count above is the evaluator's manual count.
- Dialogue share: 483/2,839 words = **17%**. Unusually low for the romance-element register (30–45%). This is caused by the two summarized explanations (L25, L109).

## Anti-AI Scan (20 Patterns) — 2,839 words
1. Forced symmetry: **Found**, 1 (0.35/1K, minor). L109 "until the place became a kind of joke, and the joke became a fairy tale, and the fairy tale became a myth."
2. Empty poetic vocabulary: Clear.
3. Automatic rule of three: **Found**, 5 (1.76/1K, strong). L25 "The pillars, the fire, the statue."; L35 "without a word, without even a pause for breath, as easily as…"; L97 "The blockage in his wrist. The itch. The magic…"; L101 "made you crazy, made you hungry, made you dangerous"; L23 "Kicking, prying, chanting" (character voice, acceptable).
4. Em dashes: Clear (0).
5. Empty metaphors: **Found**, 1 (minor). L67 "a storm about to break."
6. "And" openings: Clear (1, L105, functional).
7. Pseudo-philosophical closings: **Found**, 2 (0.7/1K, moderate). L105 "People had stopped expecting her. And after long enough, they'd stopped believing in her at all."; L109 "There wasn't a gentle way to say most of it."
8. Excessive parallelism: **Found**, 3 (1.06/1K, strong). L35 "He had spent… He'd spent…"; L71 "Bal didn't sit. He didn't run, either."; L163 "It all sounded wonderful. It sounded so wonderful…"
9. Smooth transitions: Clear.
10. Described emotions: 4, all **source-mandated** ("still confused", "nervously", "Still nervous", "still fuming"). Not penalized because fidelity requires them.
11. Explanatory extension: **Found**, 5 (1.76/1K, strong, HARD CAP). L31 "They might have been sitting there all along, waiting for him to notice."; L55 "because she was the oldest and the worst, and also because she was the one that was supposed to be true once…"; L97 "It had never been a missing hand that stopped it. It had been a missing sygl…"; L99 "much as everybody knew the things nobody discussed at the dinner table"; L131 "the deep, rich red of fresh blood, a match for the rubies at her ears."
12. Binary negation: **Found**, 3 (1.06/1K, strong). L97 "It was not a sound, exactly, more a kind of settling"; L97 "It had never been… It had been…"; L131 "Not brown with a reddish tinge, not a trick of the braziers, but red through and through."
13. Precision flex: Clear.
14. Emotional control demonstration: 2, both **source-mandated** (L67 "visibly tries to calm herself"; L125 fuming). Not penalized.
15. Authoritative description: Clear (texture includes the lion's feet and dust, L31).
16. Philosophical asides: folded into #7.
17. Clean dialogue: Clear (stutters, "Uhm", interruption "Your familiar?").
18. Thematic echo chamber: Clear (sock, apple, cheese-sandwich texture).
19. Graduated reveal: N/A; the structure comes from the source.
20. Temperature report: Clear.

**Total: 7 patterns counted (commercial CLEAN band 0–8).** Per-pattern intensity arithmetic: −2.5. That is the measured distance between the chapter's voice and 8.5+. Most of it sits in #3, #8, #11 and #12, which are trims, not rewrites. Prose is reported at the #11 cap (7.5); I did not stack further deductions, because the pattern count is inside the genre's clean band.

## Source Fidelity Check
**Beats (source order):** voice and Hello → steps from darkness → "Hello yourself… how did you get in?" → dress, rubies, curves → speechless, points at ceiling → "You flew in?" → "no one's tried that one" → explains the flicker → "Who are you? How did you get in?" → benches → "My name is Amelia and this is my temple" → "a temple for what?" → Queen of the vampires / "I thought you were a myth!" → outrage → Bal backs away, she calms → "Did the thought of having a myth sygl disgust you…" → "My, how the fates are working" → "You mean I had a blood sygl?" / "A good strong connection too" → he hears the truth (frowned-upon sygls, hands removed, madness, Dracula, the claiming seat) → explains → bats for a minute → "They lock me up in here…" → "No sygl. No school…" → red eyes, grin → "Would you do anything…" / "Uhm, within reason" → the familiar offer verbatim → "How am I going to get your sygl back?" → "Are you thirsty?" **All present, in order. PASS.**

**Canon vs STATE.yaml decisions:**
- Sygldry / Heir's School: **PASS.** L103 "the Heir's School, the first and grandest of the Sygldry schools" matches the 2026-10-20 ruling. L163 "Going to a Sygldry school, as Fredrick had" is consistent (Fredrick went to a lesser one).
- No early reveal of the eight high priests: **PASS.** Only "They lock me up in here" (source). No mention of priests, Naisura or the peace offering.
- Sygl on the palm: not engaged in this chapter; nothing contradicts it.
- No dual narration / Bal-only POV: **PASS.** ("Amelia saw this. He watched her see it.", L67, is a good close-third move.)
- Amelia not manipulative: **PASS.** The offer keeps "I will not ask anything of you that you are unwilling to give" and adds "You have my word on that." Her flirtation is open and warm.
- No invented plot, quirks or backstory: **PASS with notes.** The polite boy at the doors (L23) extends the source's "many of the boys and girls had tried to open the doors". "Dracula… everyone had felt rather foolish" (L109) and "Let them call me a myth with me standing in the middle of their courtyard" (L155) are flavor and foreshadowing, not plot.
- **Minor slips (fix):**
  1. L55 "because she was the oldest and the worst". Foundation §3 says Amelia became the *newest* originator. A nursery story can be wrong, but "oldest" gives a careful reader a false canon fact. Cut "oldest".
  2. L55 "a flashlight lit beneath your chin" vs Ch.1's "a torch" in his backpack (Ch.1 L91) and L163 "by torchlight". Use one register: "torch".
  3. L35 "He had spent the last year of his life struggling to float tin cups" vs Ch.1 "Bal had mastered the first-year levitation charms in the spring, alone, in the boiler room, with a stack of tin cups." "Struggling for a year" contradicts "mastered in the spring". Fix the wording.

## Character Chaos Check (Bal)
- Irrelevant thought: **present.** The planned speech, "reasonable and apologetic and only a little bit untrue" (L13).
- Cognitive distortion: absent. Not required (commercial 2–3/4).
- Unprompted memory: **present and triggered.** The dormitory ghost stories (L55), triggered by "Queen of the vampires", returning to the scene. Fredrick's car (L163).
- Failed emotional management: **present.** Legs carry him to the seat (L87); speechlessness (L15).
- Voice under pressure: demonstrated (L113 short clauses).
Score: 3/4, inhabited rather than mediated.

## Secondary Character Chaos
- Amelia: has her own moment. The bats are her control failing (inhabited, not reported), and she recovers with comedy rather than a speech.

## The Tomorrow Test
**What the reader remembers:** the girl on the bench bursting into a shrieking cloud of bats, and the single wisp that drifts past Bal's nose afterwards. Then "Are you thirsty?"
**Anchor type:** BOTH (image: the bats; quote: "I won't bite. Not without asking." / "Are you thirsty?")
**Verdict:** ANCHOR EXISTS. It matches the outline's planned anchor.

**Shareability:** "She's a vampire goddess who's been locked up so long the world thinks she's a myth, and when he tells her that she literally explodes into bats."

## Reader Reports
**The Devourer:** Pulled through by the dialogue and the bats. Would skim L95–105 (sygl-history exposition) and slow again at L109, which repeats what they just skimmed in summary. "Are you thirsty?" makes them turn the page. No stop point.

**The Critic:** Would underline L93 and L97 ("bricked up"). Disappointed by the explanatory habit: after every image the narration explains it (L31, L99, L131), and the "Not brown… not a trick… but red" construction reads as machine polish. Also notices that the main explanation scene happens off stage.

**The Hostile:** Flags "oldest" (L55) against Amelia's canon as newest originator; flashlight vs torch; "a year struggling" vs "mastered in the spring". Asks why she can conjure benches and burst into bats but cannot leave. The source answers this later (only in her own place of power), and the chapter correctly does not front-load it. Not a hole.

**The Casual Reader:** Likes Bal at once (tongue-tied, honest) and likes Amelia more (funny, a bit dangerous, flirting). The bats and "I won't bite. Not without asking" are what they'd tell a friend. Would keep reading. 8.5. The only "huh, getting long" moment is the history paragraph.

## Cross-Reader Matrix
| Issue | Devourer | Critic | Hostile | Casual | Severity |
|-------|----------|--------|---------|--------|----------|
| Exposition told twice; explanation off stage (L95–109) | ✓ | ✓ | | ✓ | IMPORTANT |
| Explanatory extension / negation polish (#11/#12) | | ✓ | ✓ | | SHOULD FIX |
| Laugh-class at cap; "laughed, delighted" cross-chapter repeat | | ✓ | ✓ | | SHOULD FIX (gate cap) |
| Continuity slips (oldest; flashlight; tin cups) | | | ✓ | | INVESTIGATE (cheap, fix anyway) |
| Length 2,839 vs 4,200 | ✓ | | | | INVESTIGATE (book word floor) |

## Revision Recommendations (Ranked)
All fixes stay inside the source span. Nothing below adds plot, new characters, darker themes, backstory or tics.

| # | Location | Problem type | What happens now | Why it fails | Revision direction | Project rule? |
|---|----------|-------------|-----------------|-------------|-------------------|--------------|
| 1 | L95–L109 | Pacing / Exposition | L101–105 narrate the sygl history (hands removed, madness rumors, Dracula, the empty claiming seat). Then L109 says "He took a breath and explained it to her, all of it", repeats the list in summary, and ends with the joke→fairy tale→myth chain. | The reader gets the same information twice, and the scene that triggers the bats happens off the page. Dialogue share is only 17%. | Keep L95 and L97 (the "heard the truth" beat, trimmed per #4 below). Cut L101–105 to at most two short sentences of narration ("Blood sygls, while not strictly outlawed, were frowned upon. Badly."). Replace L109 with Bal *telling her in speech*: the hands, the madness rumors, Dracula, then the empty seat at the Heir's School last. Use only facts from source L82. Let Amelia interject briefly in her established voice, building from disbelief to cold to very still, then "Once he was done, Amelia exploded." (L111). She must not reveal any lore (no priests, no imprisonment details; her only lore line stays "They lock me up in here…"). Delete the joke→fairy tale→myth chain. About +500–800 words and dialogue share near 25–30%. | Yes: "When the source says X *explains* Y, dramatize it as dialogue; never narrate the content and then summarize the telling." |
| 2 | L25 | Pacing / Voice | "His tongue came unstuck enough to explain about Saint Andre's and the carvings and the apple… the sock… she laughed out loud." | This is the source's "Bal then explains about seeing the flicker", left as summary. It also adds the fourth laugh. | Render 3–5 lines of Bal's actual explanation (the flicker, the too-short ladder, the carpet), with one dry spoken reaction from Amelia at the sock instead of a laugh. Delete "and when he got to the sock she laughed out loud." About +150–250 words. | No |
| 3 | L25, L29, L149, L23 | Character (gesture class) | Amelia laughs 4 times (cap 4); "delighted" ×2; "Amelia laughed, delighted, and" repeats in Ch.3. | Reaches the gesture-class cap, so Characters is capped at 7.5. | (a) L25: cut the sock laugh (see #2). (b) L29: "The girl laughed again and gave…" → "The girl laughed and waved a hand." (source: "laughs and waves a hand"). (c) L149: "Amelia laughed, delighted, and the spell of the moment broke." → "Amelia laughed and sat down beside him, and the spell of the moment broke." (source verbatim; this also removes the Ch.3 repeat). Result: 3 laughs, all from the source. Do not swap laughs for smiles; smile/grin is already at 3 (L69, L133, L169). | Yes: "Laugh is a gesture class; source laughs only." |
| 4 | L97 | Style #11/#12 | "It was not a sound, exactly, more a kind of settling, a click… The blockage in his wrist. The itch. The magic that always ran smoothly to the elbow and then stuck. It had never been a missing hand that stopped it. It had been a missing sygl, a door someone had bricked up while he was too small to know there was a door there at all." | Two negation openers and an explanation of the image the paragraph already gives. | "It was a settling more than a sound, a click deep down in his chest, as something that had been crooked all his life slid into its proper place. The blockage in his wrist. The itch. Someone had bricked up a door in him while he was too small to know there was a door there at all." | No |
| 5 | L131 | Style #11/#12 | "They were red. Not brown with a reddish tinge, not a trick of the braziers, but red through and through, the deep, rich red of fresh blood, a match for the rubies at her ears." | A textbook binary-negation opener followed by an extension. The source image is "the firelight reflecting off her blood red eyes". | "The firelight caught them as she did, and now Bal saw clearly what color they were. Red, the same red as the rubies at her ears." (Uses the spent-once firelight image here, as the source does.) | No |
| 6 | L31 | Style #11 | "…as solid as if they had been carved there a hundred years ago… A thin film of dust lay on them. They might have been sitting there all along, waiting for him to notice." | The last sentence explains the dust detail. | Cut "They might have been sitting there all along, waiting for him to notice." End on the dust. | No |
| 7 | L99 | Style #11 | "He knew what blood sygls were. Everybody did, much as everybody knew the things nobody discussed at the dinner table." | Extension. | "He knew what blood sygls were. Everybody did." (Or fold into #1.) | No |
| 8 | L55 | Continuity / Style #11 | "a flashlight lit beneath your chin. The Queen of the vampires was the one you saved for last, because she was the oldest and the worst, and also because she was the one that was supposed to be true once, ages and ages ago." | "Oldest" contradicts canon (newest originator). "Flashlight" contradicts Ch.1's "torch". The clause is also an extension. | "…a torch lit beneath your chin. The Queen of the vampires was the one you saved for last, because she was the worst, and because she was supposed to have been real once, ages ago." | Yes: "British register: torch, not flashlight." |
| 9 | L35 | Continuity / Style #3/#8 | "He had spent the last year of his life struggling to float tin cups. He'd spent three evenings coaxing one rug off the floorboards. She had pulled… without a word, without even a pause for breath, as easily as he might scratch his nose." | Contradicts Ch.1 (mastered in the spring), and has paired parallelism plus a triplet. | "He had spent a whole spring on tin cups in the boiler room, and three evenings coaxing one rug off the floorboards. She had pulled two pieces of furniture out of the air with a flick of her wrist, without a word." | No |
| 10 | L163 | Style #8 | "It all sounded wonderful. It sounded so wonderful that he didn't quite trust it." | Echo-parallel. | "It all sounded so wonderful that he didn't quite trust it." | No |
| 11 | L67 | Style #5 | "…a good deal less like a storm about to break." | Stock image. | "…and a good deal less like something that had just set his arm hair on end." Or cut after "a girl in a black dress". | No |
| 12 | L105 | Style #7 | "People had stopped expecting her. And after long enough, they'd stopped believing in her at all." | A mug-line closing. It is redundant once #1 puts the empty seat in Bal's mouth. | Cut, or give the substance to Bal in the dialogue rendered in #1. | No |

### Fix order
Structural first (#1, #2), then Character (#3), then Continuity (#8, #9), then Prose (#4–7, #10–12). #1 must come before #7 and #12 because it may absorb them.

## Strengths to PRESERVE
- The author's dialogue, near-verbatim, including "Uhm, within reason", the familiar offer, and "Are you thirsty?" as the last line.
- Amelia's invented-but-in-register lines: "I won't bite. Not without asking." / "Does that happen often?" / "Only when I'm cross" / "Cutting off the hand doesn't cut out the blood." / the polite boy at the doors.
- The bats sequence and its single-wisp aftermath (L113–117).
- "Amelia saw this. He watched her see it." (L67): exact close third.
- The opening handoff from Ch.1 ("Hello?" → "For a few heartbeats nothing answered him.") and the handoff to Ch.3.
- Zero em dashes; no filter words; past tense throughout.

## PATH TO 8.5
- **Characters 7.5 → 8.5 requires:** (1) Take the laugh class below cap with fix #3 (3 source laughs only). That lifts the cap. (2) Give Bal and Amelia an on-stage exchange where each voice is tested side by side. Fix #1 does this: Bal's plain, friendly, slightly-joking delivery of hard facts ("everyone felt pretty stupid about Dracula") against Amelia's interjections, which move from teasing to cold to silent. Then cover-the-name works across a run of 8+ lines, and her bats become an inhabited control failure the reader watches build.
- **Prose 7.5 → 8.5 requires:** (1) Bring #11 density under 0.8/1K (fixes #4–#8 remove 5 instances; at most 1 may remain). (2) Clear #12 entirely (#4, #5). (3) Remove the strong #3/#8 runs (#9, #10, the myth chain in #1). The chapter already has its stopping sentence ("Cutting off the hand doesn't cut out the blood."). For this romance-element register the remaining lift is banter quality, which #1 and #2 supply.
- **Theme 8.0 → 8.5 requires:** the empty seat at the claiming spoken *by Bal, to her* in fix #1, as the last item in his telling, with no narrated parallel to his own unclaimed state. The reader makes the link. Keep the source line "Even without my magic, you're still powerful in your own right" exactly where it is; it is the thematic answer.
- **Pacing 8.0 → 8.5 requires:** fix #1 (removes the double-telling and puts the bats' trigger on stage) and fix #2. Together they add about 650–1,000 words, which brings the chapter toward its 4,200 target with scene rather than padding. Do not add any new beat.
- **Emotion 8.0 → 8.5 requires:** the outrage shown building in Amelia's interjections during fix #1 (object/action only: the braziers dipping, her hands going still in her lap, no intensity words), so the bats land as the peak of a scene rather than after a summary.

## VERDICT
**POLISH.** Genesis Floor 7.5 (Characters: laugh-class cap; Prose: #11 density) | Average 8.0 | Casual Reader 8.5 | Source Fidelity PASS.
The chapter is faithful, warm and commercially sound. All of the work above is cutting and dramatizing material the source already contains.

BIAS CHECK: This evaluation was produced by the same system that wrote the prose. Confidence in scores above 8.0 requires external validation (beta readers, editors, comp analysis).

## Revision applied (2026-10-20, surgical editor)
- #1: The sygl-history block (old L99–109) is now an on-page dialogue. Bal says the source facts aloud: doctors take the hand, the madness rumors, Dracula, then the empty place at the Heir's School last. Amelia's interjections go from teasing ("Do I look mad to you?") to flat ("Dracula") to silent while a brazier dips. No new lore. The joke→fairy tale→myth chain, the "mug line" closing and the offstage summary are cut.
- #2: The flicker/ladder/sock explanation is now dialogue. Amelia answers the sock with a dry line ("Poor sock") instead of a laugh.
- #3: Laughs cut to 3, all from the source. "laughed, delighted" is gone (source: "laughed and sat down beside him").
- #4–#7, #10, #11: explanatory extensions and "Not X but Y" constructions trimmed at the benches' dust, the click, the red eyes ("Red, the same red as the rubies at her ears") and "storm about to break". The doubled "sounded wonderful" is merged into one sentence.
- Continuity: "oldest" cut (Amelia is the newest originator per source L334). American register is kept: "flashlight" in both places (the old "by torchlight" is now "by flashlight"). Ch.1 still says "a torch" in the backpack and needs the same change. Tin cups now read as "a whole spring", matching Ch.1. The "red gaze" line that came before the eye reveal is removed.
- Gates (with Ch.1–4): style_check clean, grammar 0, voice_wear clean, tic_report --gate clean. Em-dashes 0, "the way" 1, simile 2.2/1k. The word count is 2,757 (−82). Dramatizing the history replaced the double-telling, so the chapter did not grow.

## Re-evaluation (round 2)
**Evaluator:** book-evaluator | **Date:** 2026-10-20 | **File:** manuscript/chapter-02.md (2,757 words; dialogue 830 words = 30%, up from 17%)
**Lens:** unchanged from round 1. This is a faithful revise/expand: light, warm, playful; Amelia open, confident and flirtatious, never manipulative; American register; no tics. Line numbers below refer to the revised file.

### HEADLINE
**CVI-Launch:** 8.9 (8.4 + 0.5 anchor) | **CVI-Legacy:** 6.2 | **Genesis Floor:** 8.5 | **Genesis Average:** 8.5 | **Casual Reader:** 9.0
**Verdict:** **PASS, conditional on one one-word Logic fix (R2-1 below).** The fix is mechanical and does not need another evaluation.

### Gates (rerun by evaluator in the scratch layout /tmp/claude-0/-home-user/925d8686-989e-5134-a9ef-2d597d7cac42/scratchpad/re2/manuscript/chapters/, Ch.1–4)
- `tic_report.py --gate`: **clean.** Ch.2 has 1 negation pivot (cap 1), 0 and-chains, and no gesture class at cap. Book-wide auto-recurrence: none.
- `voice_wear_check.py`: **clean** (strict).
- `style_check.py`: **clean.** Em dashes 0; "the way" 1; Ch.2 has no gated repeat. The old informational repeat "Amelia laughed, delighted, and" is gone.
- Round 1 could not verify the gates. They are now verified.

### Genesis Score

| Dimension | R1 | R2 | Evidence | Cap check |
|---|---|---|---|---|
| Originality | 8.5 | 8.5 | The goddess offers to be the boy's *familiar* (L191). "Poor sock … I see you moved up in the world." (L37) is fresh, in-register comedy built on a source beat. | — |
| Theme | 8.0 | 8.5 | The empty place at the claiming is now spoken by Bal, to her, as the last item: "There's a place set aside for you there… After enough years of an empty chair, people decided the chair was all there was." (L133). The narration no longer draws the parallel with his own unclaimed state. The source answer "Even without my magic, you're still powerful in your own right" (L155) stays in place. | — |
| Characters | 7.5 | 8.5 | The laugh cap is lifted: 3 laughs (L41, L95, L183), all from the source. Cover-the-name passes over a run of more than 8 lines: "Mad … Do I look mad to you?" / "Not right now," (L119–123); "I don't think anybody asks the baby." (L115) is Bal's dry honesty. Amelia's control fails on the page and is inhabited: "Dracula," with her voice gone flat, then the brazier dipping and her hands stopping (L127–131). Chaos 3/4. | Gate: no class at cap. Watch the smile family (L81 rueful smile, L167 grinned, L203 smiled, plus L123 mouth twitch). It is under the gate's cap; do not add more. |
| Prose & Voice | 7.5 | 8.5 | #11 is now 2 in 2.76k (0.73/1K, under the 0.8 commercial cap). #12 is 1, the source's own "wasn't skinny / wasn't fat". Stopping sentences: "Cutting off the hand doesn't cut out the blood." (L101); "Someone had bricked up a door in him while he was too small to know there was a door there at all." (L105). Rough sentence present: "Bal looked. Rubies, black dress, one eyebrow up." (L121). | — |
| Pacing | 8.0 | 8.5 | The double-telling is gone, and the trigger for the bats happens on stage. Speed varies from a slow, quiet build (L127–133) to the bat burst. "Are you thirsty?" is the hook. Length is −34% against the 4,200 target but inside the outline's 1,300–5,000 band, with every source beat covered. Watch the book-level word floor elsewhere. | — |
| Emotion | 8.0 | 8.5 | The outrage builds through objects and actions only (the brazier sinks and flares "though there wasn't a breath of wind", her hands stop), so the bats land as the peak. Emotional surprise: "Does that happen often?" / "Only when I'm cross" (L145–147). Body rebel: "his legs simply took him there" (L99). | — |
| Source Fidelity | 8.5 | 8.5 | Every beat from L14–110 is present and in order. Dialogue is near-verbatim. The familiar offer is verbatim, plus "You have my word on that." No priests, Naisura or other lore come early. Heir's School wording matches the ruling. "Flashlight" is now consistent with Ch.1 L91. Held at 8.5 by R2-1. | — |
| **FLOOR / AVG** | 7.5 / 8.0 | **8.5 / 8.5** | | |

**Trajectory check:** +1.0 on Characters and Prose. That needs 3+ cited improvements: laughs 4→3 (all source), #11 5→2, the on-stage dramatization of the history, and the gates verified clean. Rule satisfied.

### CVI-Launch
Commercial Pacing 8.5 · Tomorrow 3 anchors → 9 · Casual 9.0 · Shareability 3/3/2 → 5.7 · Pitch yes (10) · Closeness yes (10) = 8.4, + 0.5 anchor = **8.9**.
CVI-Legacy: 8.5×.30 + 8.5×.25 + 3×.20 + 4×.15 + 3×.10 = **6.2** (chapter level).

### Anti-AI Scan (2,757 words)
- #1 Clear: the myth chain is cut.
- #3 Minor, 2: "her hand, and then at her face, and then down at the stump" (L195); "Kicking, prying, chanting" (character voice).
- #5 Minor, 1: "She grinned, and it changed her whole face." (L167), a stock phrase.
- #7 Clear.
- #8 Minor, 1: "not from the teachers…, not from anyone" (L45).
- #10 and #14: source-mandated only (confused, nervously, fuming, calming herself).
- #11 Minor, 2: L105 "as something that had been crooked all his life slid into its proper place"; L171 "Bal answered immediately. He didn't even need to think about it." (the second sentence explains the first).
- #12: 1, source line.
- #17 Clear: interruptions and false starts appear ("Usually?", "Mostly.").
- #18 Clear.
- All other patterns Clear.
- **Total: 5 patterns, all minor. Commercial clean band.**

### Reader Reports
- **Devourer:** no drag left. The history now reads as a conversation that escalates into the bats. Turns the page at "Are you thirsty?"
- **Critic:** underlines L101 and L105. Small notes on the stock phrase at L167 and the doubled sentence at L171.
- **Hostile:** **"Poor sock," Amelia said gravely (L37).** Bal does not learn her name until L51 ("My name is Amelia"). Everywhere else before that point the narration calls her "the girl". This breaks Bal-only knowledge rights. Also minor: narration's "one rather large problem" (L197) leans British against the American-register ruling. Amelia's own "cross" and "rather" are her voice and acceptable.
- **Casual:** 9.0. "Poor sock" and "Do I look mad to you?" make her irresistible, and the bats are the thing they'd tell a friend about.

Cross-reader: R2-1 flagged by Hostile only, so INVESTIGATE. It is still a canon/POV guardrail violation and must be fixed regardless.

### Remaining fixes (surgical)
| # | Location | Type | Now | Fix |
|---|---|---|---|---|
| R2-1 (required) | L37 | Logic / POV | "Poor sock," Amelia said gravely. | "Poor sock," the girl said gravely. |
| R2-2 (optional) | L171 | Style #11 | "Bal answered immediately. He didn't even need to think about it." | "Bal answered immediately." |
| R2-3 (optional) | L167 | Style #5 | "She grinned, and it changed her whole face." | "Then she grinned." (source: "Suddenly she grins") |
| R2-4 (optional) | L197 | Register | "there was still one rather large problem standing in the way." | "there was still one big problem standing in the way." |

### VERDICT (round 2)
**PASS: Genesis Floor 8.5, Average 8.5, Casual 9.0, Source Fidelity PASS, all gates clean, conditional on R2-1 (one word).** R2-2 to R2-4 are optional polish and do not affect the verdict.

BIAS CHECK: This evaluation was produced by the same system that wrote the prose. Confidence in scores above 8.0 requires external validation (beta readers, editors, comp analysis).
