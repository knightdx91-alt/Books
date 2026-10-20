# Evaluation: Chapter 11 — Break Their Toys
**Evaluator:** book-evaluator | **Date:** 2026-10-20 | **Draft:** R1 (3,624 words of text; target 3,800, range 3,400–4,200)

## HEADLINE
**CVI-Launch:** 8.8 (8.3 + 0.5 strong anchor) | **CVI-Legacy:** 6.1 | **Genesis Floor:** 8.5 | **Genesis Average:** 8.5
**Engagement type:** Self-Insertion (primary) / Empathy (secondary) / Fascination (tertiary)
**Divergence alert:** none. Launch is above Legacy, the same profile as Ch.6–10.

**VERDICT: PASS** (Floor 8.5, Casual 8.5). The chapter is light, warm and playful, as the author asked. Peter is told by Amelia, and Bal's stand against the gods is principled without being grim. Nothing in it is invented plot. Five surgical fixes follow (F1–F5). **F1–F3 should go in before commit:** they are small source-fidelity and logic corrections. None adds plot, and none needs re-scoring.

---

## Mechanical gates
Scratch copy of Ch.1–11 in `manuscript/chapters/` (/tmp/claude-0/-home-user/925d8686-989e-5134-a9ef-2d597d7cac42/scratchpad/ev11).
- `voice_wear_check.py`: **clean.** No retired phrases, no device over cap, no strict self-repetition. One soft WARN on Bal's self-repetition. It is non-gating and does not come from this chapter.
- `tic_report.py --gate`: **clean.** No auto-recurrence. Ch.11 rhythm: and-chains 2 (cap 9), negation pivots 0, 'So' openers 0. Gesture classes: none at cap. The worst Ch.11 class is "turn away / turn back" at 2x (L26, L156/168), which is under the cap of 4. Nods 0, shrugs 1 (L148, source), look-away 0 (the source's "looks away" is rendered as rolling onto her other side, L254. That is a good variation).
- `style_check.py --dir manuscript`: **clean.** Simile 3.6/1k (under 4), adverbs 9.4/1k, em dashes 0. No distinctive cross-chapter repeated phrase. Informational repeats: "her voice had gone" (Ch.2 L135 "flat" / Ch.11 L270 "small") and "it had taken her" (Ch.4 L115 / Ch.11 L198). Both are generic; see F5.
- `grammar_check.py --file`: 0 errors.
- "the way [x]": 0. "as if / as though": 1 (L84).
- **"Master"**: 0. The source has none here. Correct.
- Laugh class: 2 (L28, L244), both from the source. Smile/grin family: 9 tokens. That is acceptable for a teasing chapter but at the upper edge (see F5).

## Source fidelity (L394–539: the uniform to "Lets get back.")
- **Every beat is present, in source order:** the uniform (short black skirt, tight black sweater, blood sygl, black and red socks above the calves); the jump down and the widening smile; Viridia trying not to stare, Bal amused; "how have your classes been" / last class / errands; "partly why I'm here"; "steal him for a while"; Viridia waves her off and offers to tell the teacher; "I've taken care of it"; "You two have fun!"; Bal watching the skirt and legs; Amelia watching him watch; "What?" / "Just admiring the view"; the teleport by hand to the hill; Tempus flags; "He doesn't already know…"; marching drills, the merging groups, sun on swords and spears; two armies found, Naisura licking his wounds after Nera; "The games they play" begun and stopped; the ranking; "Like Naisura…"; the burden falling to Raizen; "beneath their notice"; "They do not share… could not let an insult like that stand"; "So where does that leave us?"; the hard, fanged smile; **"We play their game and break their toys"**; the hidden temple and **Peter** (lone blood sygl in a Terra stoneworking family, sixteen, the family business, shunned, the mountains, a few days, every stone by his hand); the offerings (bowl, stone knife, priest seals the wound, recent memories); twelve years; the death on her altar; all his memories, birth to death; the hurt and the gladness; the hug, stiff then returned; her gratitude rendered from Bal's side (L110); "What can I do to help?"; the High Priest chain of command and "everything has to go through you"; "only sixteen" / "If they do not, it will be handled"; Bal's mental note; military strategy books; the week of moving; weapons drills; "When do I need to meet them?"; upper command already there; "before dinner?" / "You just want to go hang out with Viridia"; the shrug; the arm grab and the teleport; the canyon temple (three mountains, one pass, several hundred rooms, priests' quarters, two High Priest suites, twelve years understood); two priests promoted yesterday; Amelia on the bed; the conjured book; "this is something you need to do on your own"; the ring (slim, white, ruby eye, middle finger, "proof", "various other things" with a grin); the priests' room, scarlet robes and white sashes, confused, the ring shown, "High Priest! … We did not know you were coming"; **Thad** and **Xavier** exactly as the source describes them; surprised at his age, Lady Amelia's choice good enough; the table; the story of her imprisonment to spread; "she did not abandon them by choice"; train to strike Raizen, who is already training; the element of surprise; the dark stone with the light and pair runes in white, tossed, red light, tap it, push magyk; dismissed, they bow and go for the commander; Amelia still reading; "I think she actually likes you…"; "Oh, you mean Viridia?"; "she does say some interesting things"; the cover, the jaw drop, "You're reading her diary?"; "I like to know people's secrets"; "Do you have a diary?" both ways; "mainly girls"; the blush; "Maybe. You'll never find it though."; Bal resolving to find it; the diary vanishes; "We'd better get going…"; "You know you can eat with us right? … no reason you should hide away"; lowered eyes, "Just give me a little time"; takes her hand, "Let's get back."
- **Peter is told by Amelia,** in her voice, with no flashback. Bal's reaction (L100–102) is the only addition, and it stays in his head. Good.
- **Amelia manipulates no one.** Her menace ("it will be handled") is the source's line. Bal's response is the source's mental note, kept light ("in his most reasonable voice"). The diary reading is the source's own mischief and is played as comedy.
- **POV:** the source's head-hop into Amelia's gratitude ("Amelia was grateful… Bal treated her as a friend") is correctly converted to Bal's inference (L110). Clean.
- **Dialogue rule:** every source line keeps its speaker, meaning and placement, with natural American polish ("Me winning a few of their followers over"; "Says? Says where?"; "That's never really been my thing"). The exceptions are F1 and F2.
- **Additions, all texture:** the rune kit under his arm (continuity from Ch.10 L186, carried and returned; well tracked); the sewn flags (L44, Bal's who-does-the-work worldview); the missed turn and the horns; "He had been four, twelve years ago" (L100); the washing line in the courtyard (L162); Thad's flat hands and Xavier's fixed eyes (L202); "Bal liked the cut of the lines" (L210); "said the book" (L234); the dinner hook (L276). None adds plot, characters, habits or lore. Two small inventions are flagged in F4 and F3: the flag colour, and a sygl placement that contradicts Ch.6.
- **Seam with Ch.10:** the chapter opens on the uniform details without restating "She was wearing a school uniform." That is correct. "It was the same as Viridia's" picks up the last line cleanly.

## Spell / magic-effect watch (author's standing request)
- **No invented spells.** The on-page magic is all source: Amelia's teleport by touch (x2 on page: courtyard to hill at L34, hill to temple at L150; the return is implied), conjuring the book (L172), the ring (L176), the diary vanishing (L260), and the priests' paired rune stone (light + pair, L210–214).
- **The snap is well varied.** The source snaps three times here (book, ring, diary). The chapter renders them as an empty hand that "was not empty anymore", "clicked her fingers", and an unseen vanish. No signature gesture forms.
- **FLAG FOR THE AUTHOR (watch, not a fault): Amelia's teleport** has now carried a scene transition in Ch.2, 3, 6, 7, 9 and 11, and twice in this chapter. It is the source's own device, and its "the X went out" rendering is so far varied ("the courtyard went out" / "the hill went out"). However, those two lines are the same construction 116 lines apart (F3b). Worth raising with the author as the ledger's busiest effect after the whip arrives.
- **Ledger update (orchestrator):** add Ch.11 to the Teleport row. Add a row: "High Priest ring (white, ruby eye; 'various other things') — conjured Ch.11." Add the "paired rune stone (light + pair; Thad's, signal by red light / push magyk)" to the Runes row as Ch.11 (priests', not Bal's).

## Genesis Score

| Dimension | Score | Evidence | Cap Reasons |
|-----------|-------|----------|-------------|
| Originality | 8.5 | A goddess explains the gods' war as a ranked league ("their fights are ranked, I suppose is the best way to put it", L54). The plan is to "break their toys", and the temple was built by one outcast for a god "who would never come to see it" (L102). Fresh in its genre lane | none (commercial: 1+ fresh element) |
| Theme | 8.5 | Wanted for who you are, never stated: Peter shunned for a red palm (L86); "Her followers were afraid of her. The other originators couldn't be bothered with her. Bal just liked her" (L110); "Viridia likes you. So do I." (L266). It sits against texture with no theme in it (the sewn flags, the washing line, the socks) | none |
| Characters | 8.5 | Cover-the-name passes. Amelia teases and then turns hard: "No. I expect them to listen to their High Priest. If they do not, it will be handled." (L128). Viridia is breezy: "You two have fun!" Bal is plain and practical: "What can I do to help?"; "Says? Says where?" Thad is practical in his only real speech (L214). Chaos 3/4, inhabited: an irrelevant thought (the flag-sewer, L44); a scene-triggered memory that returns to the scene (the library, L68); failed management ("laughed, because his ears had gone warm", L28; Amelia "went pink", L254). No tics, no shared gestures (Amelia takes his hand to teleport, as the source has it. It is not a sleeve pull) | no cap; gesture gate clean |
| Prose & Voice | 8.5 | Stopping sentence: "And then the god herself, standing on a cold hill, carrying the whole of him around inside her, birth to death, with nobody to tell." (L102). Underlines: "He had been four, twelve years ago." (L100); "Twelve years. Looking out at it, Bal believed them all." (L164); "and he was a kid in a school sweater" (L184); "'Mm-hm,' said the book." (L234); "She let that hang for exactly as long as it took him to work out which view she meant." (L30). Ugly sentence: "So many soldiers in one place was a thing Bal had no practice at." (L42). Voice under pressure: the register drops to placating ("in his most reasonable voice", L132) when Amelia goes hard | #11 at 2 instances (0.55/1k), under the commercial cap |
| Pacing | 8.5 | A chain of revelations across three places, as the outline structures it. Each place changes the value: the hill (a war is coming to her followers → "break their toys"); the temple (Bal goes from schoolboy to ring-bearing High Priest with priests answering to him); the bedroom (a comic diary reveal → the gentle refusal). Speed varies: quick banter at the stage and in the bedroom, slow at Peter, summary for the chain of command. Hook: dinner across from a girl whose diary has his name in it (L276) | 5% under target. Not a cap |
| Emotion | 8.5 | Anchor: Peter's twelve years (L98–102), paid off visually in the window (L164). Surprise: right after the dead boy on the altar, the diary farce, and a goddess hiding behind "one striped sock" (L254). Body rebel: "Amelia went stiff in his arms… her chin settled on his shoulder" (L106); "Her voice had gone small" (L270). The peak is carried by actions (the hug, the window), not intensity words | none |
| Engagement (Dim 7) | 8.5 | Self-insertion: a goddess pulls you out of class, hands you a ring and two priests, then admits she keeps a diary you're now obliged to find. Empathy holds through Peter and the hug | none |
| **FLOOR** | **8.5** | | |
| **AVERAGE** | **8.5** | | |

Trajectory: Ch.1–10 are all 8.5. Ch.11 holds. It is the most emotionally weighted chapter so far (Peter), and the tone stays light around it.

## CVI-Launch Breakdown
| Input | Score | Evidence |
|-------|-------|----------|
| Commercial Pacing | 8.0 | Three locations, a fresh reveal in each, a comic last act, a pull to dinner |
| Tomorrow Test | 3 anchors (9) | IMAGE: Peter laying every stone for twelve years, then the canyon temple seen through the window. QUOTE: "We play their game and break their toys." IMAGE/QUOTE: the goddess reading Viridia's diary ("Maybe. You'll never find it, though.") |
| Casual Reader | 8.5 | Uniform tease, an army, a sad story, a ring, a diary. Likable leads and steady warmth |
| Shareability (quote/plot/emotional) | 4/3/3 (7.3) | "the goddess is READING HER DIARY"; "break their toys" |
| Concept Pitch | yes (10) | |
| Human Closeness | yes (10) | Bal and Amelia carry nearly the whole chapter |

CVI-Launch = 0.2(8.0) + 0.2(9) + 0.2(8.5) + 0.2(7.3) + 0.1(10) + 0.1(10) = 8.3, plus 0.5 for the anchor = **8.8**.
CVI-Legacy (default weights): 0.3(8.5) + 0.25(8.5) + 0.2(2: "break their toys" is quotable but niche) + 0.15(4) + 0.1(5) ≈ **6.1**.

## Anti-AI Scan (20 patterns; commercial thresholds; 3,624 words)
1. Forced symmetry: Clear.
2. Empty poetic vocabulary: Clear.
3. Automatic rule of three: Found, minor (2; 0.55/1k): "priests and armies and rune stones" (L228); the followers/originators/Bal triad (L110) is the source's own.
4. Em dashes: Clear (0).
5. Empty metaphors: Found, minor (1): "She said the name gently, as if it might break." (L84).
6. Dramatic "And" openings: Found, minor (3; 0.8/1k): L86 "And then his palm came up red.", L98 "And he was glad", L102 "And then the god herself". Each earns its place, but three in one telling is the edge.
7. Pseudo-philosophical closings: Clear. The chapter ends on comic dread, not a maxim.
8. Excessive parallelism: Clear.
9. Overly smooth transitions: Clear. The scene breaks are hard cuts.
10. Described emotions: Found, minor (1): "neither of them was in any hurry to let go" (L106) is close to telling. Acceptable.
11. Explanatory extension: Found (2; 0.55/1k): "and laughed, because his ears had gone warm" (L28); "from how long she had held on he understood that it was worth something to her" (L110, source-mandated). Under the cap.
12. Binary negation opener: Clear.
13. Precision flex: Clear ("He had been four" is characterful, not a flex).
14. Emotional control demonstration: Clear (Bal's note is the source's).
15. Authoritative description: Minor. The temple paragraph (L158–160) is confident, but it is seen from one window, so it is earned.
16. Philosophical asides: Minor (1): "nobody in the books had ever asked the people in the rows" (L68). It is grounded in Ch.9's library and stays Bal's.
17. Clean dialogue: Clear. There are a stopped start (L54), a book that answers (L234), and a broken-off question (L236).
18. Thematic echo chamber: Clear. Plenty of noise.
19. Graduated reveal: Clear. The structure is a three-stop chain, different from Ch.9–10.
20. Emotional temperature report: Clear.

**Total: 6 minor patterns.** That is CLEAN for commercial fiction (0–8). There is no over-correction flag (the score is not 0/20).

## Character Chaos Check (Bal)
- Irrelevant thought: present: "Somebody had sewn all those flags. Hundreds. Bal wondered if they had a person whose whole job it was." (L44)
- Cognitive distortion: present, mild: the rumination over what could have impressed Viridia, "That was a worse idea, because then it could have been anything." (L232)
- Unprompted memory: present, triggered by the army and returned to it (L68, the library this morning).
- Failed emotional management: present (ears going warm, L28; the stare he can't stop, L8).
- Voice under pressure: demonstrated lightly (L130–132). This is not a crisis chapter.

## Secondary Character Chaos
- **Amelia:** has her own moments: the stopped start (L54), stiffness in the hug, going pink and hiding, the small voice.
- **Viridia:** brief here (the stare at the socks, L12), as the source has her.
- **Thad / Xavier:** first appearance. Each gets one independent reaction (L202) and a distinct function (Thad speaks and hands over the stone, Xavier watches). That fits their cards.

## The Tomorrow Test
**What the reader remembers:** a boy with a red palm laying every stone of a temple for twelve years, for a god who would never come to see it, and Bal at the window believing every one of those years. Close second: "We play their game and break their toys."
**Anchor type:** BOTH.
**Verdict:** ANCHOR EXISTS.

**Shareability:** "The goddess literally reads the girl's diary, then admits she keeps one too: 'You'll never find it.'" Yes.

## Reader Reports
**The Devourer:** No stop point. The army on the hill delivers stakes at once, and the ring and priests feel like a level-up. The diary turn and the dinner hook pull straight into Ch.12. The chain-of-command summary (L116–120) is the only patch they skim.
**The Critic:** Underlines L102, L100 and L164. Likes that Peter's story sits in Amelia's mouth and Bal's reaction stays small. Would query "as if it might break" (L84) as stock, and notices "the courtyard went out" / "the hill went out" as a repeated construction.
**The Hostile:** (1) "It was the same as Viridia's except for one thing", and then a second difference follows (the socks, L6). (2) The blood sygl is "on the front" of Amelia's sweater and "the same mark Bal had on his own chest", but Ch.6 puts the uniform sygl on the BACK of the sweater (Ch.6 L11, L125), and "on his own chest" reads as if Bal's body carries the mark when canon puts it on his palm. (3) "Catching her meaning" became "the only explanation he was going to get", which inverts the source beat. (4) The flags are "yellow", a colour no earlier chapter or the source gives.
**The Casual Reader:** Stays. Amelia in striped socks, a goddess pulling the hero out of class, a sad story that doesn't wallow, and a funny ending. Likes both leads. 8.5.

## Cross-Reader Matrix
| Issue | Devourer | Critic | Hostile | Casual | Severity |
|-------|----------|--------|---------|--------|----------|
| Sygl placement / "on his own chest" (L6) | | | X | | INVESTIGATE (canon; fix) |
| "except for one thing" logic (L6) | | | X | | INVESTIGATE |
| "Catching her meaning" inverted (L178–180) | | X | X | | SHOULD FIX (fidelity) |
| "innocent" / "amusement" dropped (L68–70) | | X | X | | SHOULD FIX (fidelity) |
| Repeated "the X went out" teleport construction | | X | | | INVESTIGATE |
| Chain-of-command summary skimmable | X | | | | INVESTIGATE (source summary; keep) |

## Revision Recommendations (Ranked)

| # | Location | Problem type | What happens now | Why it fails | Revision direction | Project rule? |
|---|----------|-------------|-----------------|-------------|-------------------|--------------|
| F1 | L68–70 | Continuity (source fidelity) | "…so that an originator who never thought about them could feel he'd answered an insult… He would not stand aside and let that happen to anyone." | The source's stance is specific: Bal won't step aside "while innocent people were killed for the originator's amusement" (outline: "for the gods' amusement"). The rewrite drops both "innocent" and "amusement", so Bal's principle is softened into a reaction to one insult. | Change the end of L68's second sentence to "…so that an originator who never thought about them could be amused." Change L70 to: "He would not stand aside while innocent people were killed for the originators' amusement. He knew that already, the same as he knew his own name." (Optionally cut the stock simile: "He knew that already.") | No |
| F2 | L178–180 | Continuity (source fidelity) | "She turned a page, smiling at it, and that was the only explanation he was going to get. / Bal knew when a subject had closed." | The source has Amelia say it "with a grin" and Bal "catching her meaning". The rewrite turns a shared, teasing understanding into a closed door. | "'It also enables you to do various other things.' She grinned at the page and turned it. / Bal caught her meaning. He left his kit lying on the coverlet, waved to her, and went next door." | No |
| F3 | L6 | Logic / Continuity | "It was the same as Viridia's except for one thing. Where Viridia had Raizen's mark, the blood sygl sat on the front of Amelia's tight black sweater, red on black, the same mark Bal had on his own chest… Where every other girl… socks" | (a) "one thing" is followed by two differences. (b) Ch.6 puts the uniform sygl on the sweater's BACK. (c) "on his own chest" reads as a mark on Bal's body, when his sygl is on his palm. | "It was the same as Viridia's, with two differences. Where Viridia's sweater carried Raizen's mark, Amelia's tight black one carried the blood sygl, red on black, the same as Bal's own sweater, and below it was a short black skirt. And where every other girl…" (Keep the socks sentence as is.) | Yes: uniform sygl placement = back of the sweater (Ch.6); never "on his chest". |
| F3b | L34 / L150 | Style | "the courtyard went out" / "the hill went out" | The same construction carries both teleports. It is a fresh image used twice in one chapter, which starts to make it a device. | Keep L34. Change L150 to "…and hooked her arm through his, and the wind stopped." (or any other non-"went out" rendering). | Yes: vary every teleport rendering; "the X went out" is now spent (Ch.11 L34). |
| F4 | L42 | Continuity (invented detail) | "each carried the same jagged yellow mark" | No colour for the Tempus sygl appears in the source or in Ch.1–10 (Ch.6 calls it "sharp and angular" and crackling). Small, but it is invented lore. | "each carried the same sharp, angular mark, snapping in the wind." | No |
| F5 | L84; L86/98/102 | Style (optional polish) | "She said the name gently, as if it might break." Three "And" openings inside Peter's telling. | Stock simile (#5). The "And" openings are at the edge for one passage (#6). | Cut L84 to "She said the name gently." Change L98 "And he was glad, at the end." to "He was glad, at the end, though." (Amelia's speech; meaning unchanged.) Keep L86 and L102. | No |

### Fix order: F3 (logic/canon) → F1, F2 (fidelity) → F3b, F4 → F5. All are line-level. None adds plot, and none affects the word count materially.

## Strengths to PRESERVE
- L100–102 (the four-year-old, and "carrying the whole of him around inside her, birth to death, with nobody to tell") and L164 ("Bal believed them all"). These carry the chapter.
- The diary sequence (L226–260): "said the book", "Says? Says where?", "one striped sock". The source comedy is fully dramatized.
- The rune kit tracked from Ch.10 onto the hill, onto the coverlet, and home.
- Amelia's gratitude converted to Bal's inference (L110). It is the right POV fix.
- Snap renderings, all varied (L172, L176, L260).
- The closing hook (L276). It is anticipatory and funny, and it sets up Ch.12's diary warning without pre-empting it.

## PATH TO 8.5
Not required. The floor is 8.5. Applying F1–F3 preserves it. Skipping F1–F2 would leave two small departures from the source, which the author has asked never to happen. That alone would not drop a dimension, but the fixes are expected before commit.

## VERDICT
**PASS** — Genesis Floor 8.5, Genesis Average 8.5, Casual 8.5. Apply F1–F3 (and preferably F3b–F5) before commit. Update the magic ledger (Teleport: Ch.11; ring; paired rune stone) and raise the teleport-frequency watch item with the author.

BIAS CHECK: This evaluation was produced by the same system that wrote the prose. Confidence in scores above 8.0 requires external validation (beta readers, editors, comp analysis).
