# Continuity Audit: Chapter 11 (run 2, per-chapter drift audit)

**Date:** 2026-10-20
**Mode:** MANUSCRIPT AUDIT. Ch.11 "Valens's Yard" is checked against Ch.1–10 as they stand on disk (all re-read in full), against the plan and against canon.
**Chapter reviewed:** `manuscript/chapters/chapter-11.md`
- Length: **6,083** prose words by `shape_check`, 6,098 by style_check and 6,258 by `wc -w` with the header. The target is 6,200 (range 5,600–6,800).
- **284 prose paragraphs**, 3 breaks.

**Paragraph numbering:** `ch-11:pN` counts prose paragraphs only. The title, the two HTML comments and the `* * *` breaks are not counted, which is the ENTITY and Ch.6–10 audit convention. So p1 is "On the other side of Praxias's wall…" and p284 is "We take the string to Kirrha…". The breaks fall after p67, p149 and p230.

Prior-chapter cites use the files as they stand now: Ch.1 193, Ch.2 69, Ch.3 84, Ch.4 83, Ch.5 210, Ch.6 340, Ch.7 194, Ch.8 240, Ch.9 199 and Ch.10 98 paragraphs. Ch.6 and Ch.9 have shrunk since the Ch.10 audit, after the kneel/crouch and memory trims.

**Read against:**
- outline.md: Ledger row 11 and `## Chapter 10` through `## Chapter 13`.
- STATE.yaml: guardrails, canon, ARCH-1..18, and AUTHOR-CP2-1..4.
- voice-dna.md: read in full, with weight on §0, §1, §3b, §4 and §8.
- character-bible.md, the cards and their "as written" blocks: Valens, Kallia, Felix, Praxias, and the Ch.10 and Ch.11 walk-on blocks.
- character-bible.md, every at-risk/spent block (after Ch.1, 3, 5, 6, 7, 7 cycle 1, 8, 8 cycle 1, 9, 9 cycle 1, 10 and 10 FINAL; the after-Ch.11 draft block), plus the at-risk table.
- voice-bank/samples 01–13, read in full. Samples 08 and 12 got the closest reading.
- ENTITY_STATE.yaml as committed (`last_updated_chapter: 10`, `chapters_tracked: [1..10]`). The tracker is adding Ch.11 in parallel, so every Ch.11 row in it is treated as unverified, and every Ch.11 fact below comes from the page.
- Ch.11's disruption and hook reports, for what those agents changed and what they rely on.

**Mechanical baseline** (`bash tools/check_chapter.sh 11`, re-run read-only):
- **Style, grammar, rhythm:** all clean. Style: simile 1.3/1k, em-dash 2, foreshadow 0. Rhythm: 0 flagged.
- **Show/tell:** dialogue meter 36.9%.
- **Voice-wear strict:** clean. Echo scan 0. Command-echo candidates 0.
- **Tic gate: FAIL.** `short spoken reply "no" 11x in chapter 11 (cap 4)`. The count is Valens ×9 and Mara ×2. This is C-01.
- **Narration counts:** and-chains 3, credential asides 0, negation pivots 0, "So" openers 0.
- **Gesture layer:** bend/stoop 0, kneel/crouch/squat 0, object handling 0, nods 0, head-shakes 0.
- **Metaphor:** fig 1.8/1k, median sentence 14, 5.9% of sentences over 40 words.
- **Shape:** CLEAN. Ch.11 computes as `long-spiral` → `dialogue`, 37%, median 14, 3 breaks.

**My own sub-gate sweeps:** 3- to 6-grams against Ch.1–10 and the voice bank, keeping grams with 2+ content words. They found 39 shared grams, nearly all common idiom. Four are second uses of a distinctive earlier phrase (W-13). Three are beats rebuilt by shape (W-08, W-09, W-12). There is 1 string hit in the voice bank, an idiom from sample-10, which is harmless. The bible's Ch.11 quotes were checked against the page by script (W-14).

**Total findings:** 40. **CRITICAL: 1 | WARN: 14 | NOTE: 25**

**Summary:**
- **The CRITICAL is the one the disruptor reported.** Valens says a bare "No." nine times, and the tic gate now fails the chapter on it.
  - With his three in Ch.6–7, that makes twelve book-wide. A short refusal has become his sound, which is the definition of a tic under the author's zero budget.
  - The fix keeps three: p25, p121 and p240, each doing a different job. Five become his own plain lines or silence, and one pair merges.
  - One of Mara's two "No." lines disappears into Felix's stacked questions, which suits Felix's card.
  - The chapter then holds 4 bare "No." lines, at the gate's cap (it fails only above 4).
- **Information flow is clean on every axis the brief named:**
  - who knows Valens is Lupus (Mara by inference; nobody in Delphi);
  - who knows he reads (Mara only; she keeps it from Felix);
  - what Mara knows of Felix (his own boast, plus Valens's four answers);
  - Mara giving her name ("Mara." once; the priest's record stays "Maira").
- **One knowledge slip:** Felix knows Valens was up "Three times" in a night he "never heard a thing" (W-01).
- **Two internal blocking contradictions:** the knot (W-05) and the bench (W-04).
- **One logic collision with Ch.9's goat:** a cold-kept goat will not shiver (W-02).
- **No-foreshadowing holds.** The question's rewording, "Where is my road home?", is not pointed at.
- **Two lines prime Ch.12's road by narration** (W-06 the notice paraphrase; W-07 the nightly look at the road). They break bible rules that hook-craft's pull relies on, and the orchestrator should rule on them.
- **Kallia is clean.** She never sits and never touches Mara. Her labor axis holds, with 0 chore-replies.
- **Felix has no catchphrase.**

**Word ledger for the proposed fixes:** net about **−49**.
- C-01: +20.
- WARN: −69.
- The chapter would land at about **6,034** by shape_check, inside 5,600–6,800.
- Dialogue rises to about 37.3%, inside the 35–45 band.
- Neither the first sentence nor the last is touched, so the ledger signature is unchanged.

---

## Scorecard by category

| Category | Result |
|---|---|
| (a) Ledger / beats | **PASS.** **Structure:** Chronological ✓, after Ch.10 Single-scene and before Ch.12 In medias res, so no consecutive repeat. The internal shape is the *slow reveal of a person* ✓. **Open:** the first sentence is 70 words, a sound, the yard "already at work in the half dark" → `long-spiral` ✓. **Close:** p284 is a spoken, practical line → `dialogue` ✓. The outline says "practical, not a romantic button" ✓. **Breaks:** 3 ✓. **Dialogue:** 36.9% (meter) / 37% (shape), band 35–45 ✓. **Gear:** median 14, mid ✓. **Length:** 6,083 vs 6,200 ✓. **Beat 1** (cousin's price; the walk), p1–p14 ✓. **Beat 2** (refusal: a full sanctuary of eyes, p29–p33; the notice, raised by Mara at p34; a week of harness from p68) ✓. **Beat 3**, in the outline's order: figs (p72–p97), the lame mule (p124–p141), he reads but pretends (p205–p222), Felix freed without paper (p224–p247) ✓. **Beat 4** NON-NEGOTIABLE: the near-kiss in the tack shed, he steps back, she is relieved, and neither explains (p250–p254) ✓. **Beat 5** NON-NEGOTIABLE: the god's first day is named by paraphrase only ("The day he first sits this year. His birthday, the priests say.", p267). The allowlisted phrase is not used ✓, no reason is given ✓, and the watch is not returned ✓. **Anchor:** Felix asleep against the black, who stands on her bad foot (p256) ✓. **Chaos traits:** figs ✓; mind-reading of Praxias, wrong in a mundane way (p163–p174), with its after-effects (p196–p203) ✓. AUTHOR-CP2-1 ("a FULL two-hander … away from the gray mule as his frame"): **PASS.** His entrance comes by voice and the trough (p1, p18, p20), and the gray appears once, as a chest sore (p231). |
| (1) Character consistency | **Valens: CRITICAL ×1 (C-01); WARN ×1 (W-02's hyperbole quip); NOTES N-02, N-15, N-16.** **Speech card:** short level declaratives ✓. Questions are practical ✓, and his one *why* is of a practice ("Why does anybody need the hour that close?", p107) ✓. **No simile or comparison in speech: PASS.** His lines were checked one by one; "Pressed, they're a cake." is a category (the fig cake was a real product), not a figure. **Evasions held:** the men he killed (p121), fear (the barred gate unexplained, p198–p202), the frame ("Paper gets taken off you" / "Who took yours?" unanswered, p245–p247) and any request that she stay (the fig wager is subtext only, p94) ✓. **The scar:** the hand scar is not mentioned, which is consistent, and the notice's words are not re-quoted except at p135 (W-06). New body facts: a nose broken and healed "a shade crooked", and "a white nick ran through one eyebrow" (p47, p251). No conflict, but see N-07. **The watch:** in his belt pouch since ch-06:p141. He reads it from the open pouch (p42–p43). It is fast against the spout's shadow (p44–p45), and he winds it daily before his bread (p57). Mara set it by Kallia's gatepost shadow (ch-06:p13), so the drift fits a 1966 movement unset since then ✓. He **reads, and hides it** ✓: he reads the sherd, says "It was on the bench." / "I did hear it.", and, in front of Felix, "How would I know what it says?" (p209–p222). **Hands:** knife and whetstone, the load test, bells, hoof, knot, wick, the stones in the goats' gap; never tack as a frame ✓. **Felix: PASS.** No catchphrase; stacked questions with rotated openers; a different boast each time (hawk p57, ear p127, the Thessalian p120, poultices p149); speed (p70, p168); the wish for approval kept unspoken (p149). See W-01, W-08(b), W-09, N-24. **Praxias: PASS.** Price first, then the favor, then bargaining down against himself (p2, p151, p156). "little cousin" ×2 and "for family" ×2, both at cap. Never the notice, never a Thracian. See W-10, W-13. **Kallia: PASS.** **Never sits:** "She stood over the pot with the ladle" (p142). **Never touches:** 0. Labor axis: "Whose water washes it?" (p143). Chore-replies 0, "Then" retorts 0, walk-offs 0, name-asks 0 ✓. Praxias's "Kallia never asks for herself." (p7) agrees with her evasion card ✓. **Mara:** her Greek is uncontracted in every line (checked one by one). CONTINUITY COMMITMENT (Greek in private): no English on the page ✓. Credential asides 0 ✓. |
| (2) Timeline | **PASS, with one forward note (W-03, money, not time).** **Span:** about eight days. D1: Praxias at first light, the breeching, dusk. D2: the sharpened awl. Then "For a week I mended his harness." (p68). Inside the week: the fig day, then the rain "the next morning" (p98), then the boxing morning and "that evening" the black comes back lame (p116–p124), then "By morning" the fresh sack (p148) and Praxias (p150) and "That evening" the walk up (p175). "In the morning" the barred gate and, "that noon", the sherd (p196–p205). Finally "the last evening of the week" (p231). Then "the day after tomorrow" for Kirrha (p284). **Runway after Ch.10:** the gap from Ch.10 to D1 is unstated. Ch.11 (~8 days), plus 2 days to Kirrha (Ch.12), plus Ch.12's "three days off" puts the 7th of Bysios about 13 days after D1. This agrees with the Elean's "I'm here till the god opens his house" (ch-10:p13, the C-01 fix) and Nikaso's "He'll be home for the god's day" (ch-10:p71) ✓. **Delphic calendar:** first consultation on Apollo's birthday, the 7th of Bysios (paraphrased, p176, p267). "The god sits every month now till the winter" (Praxias, p156) matches the monthly 7th-day consultations, suspended in the three winter months ✓. Delphians enter first (promanteia), Thessalians push to the front, and the priests wash at the spring before dawn (p179, p183) ✓. **Season, late winter AD 71:** a rain shower (p98). The potted fig "had not a leaf on it" (p15), then a few days later "Its twigs had come green and hard at the tips" (p92) ✓. Cloak thrown back at work (p20), which follows Ch.10's first cloakless afternoon (ch-10:p21) ✓. Pilgrims arrive early and camp on the terraces (p69, p175). Ch.12 is "early spring", two days on ✓. Small chronology backstep: N-14. |
| (3) Information flow | **WARN ×1 (W-01).** Otherwise **PASS**. **Who knows Valens is Lupus:** Mara, by inference from the notice (ch-09:p169: Thracian, right-hand scar, Latin, arena) plus his reading it and looking at her (ch-09:p195–p198). She raises the board as his reason (p34), and he answers only "I heard it read out." (p35). Nobody in Delphi says it. Praxias calls him "the Corinthian" and "Mule-man" (p11, p158); "Mule-man" comes from the burner (ch-06:p307), see N-11. Felix has no word of the notice. Kallia has not been shown it ✓. **Who knows he reads:** Mara only (p210–p213). Felix believes he cannot ("He can't. Nobody in this yard can but you.", p224). Mara keeps it: "I kept quiet" (p223) ✓. **What Mara knows of Felix:** everything from Felix's own boast (p224–p230) and four answers from Valens (p236–p245). Her "Felix says you freed him on the quay at Kirrha" (p235) compresses Felix's "bought me off him on the quay" plus "He said I could go wherever I liked" (p226, p228). It is a fair inference, and Valens confirms it ✓ (N-05). **Felix's knowledge of Mara:** "You're the one he took up to Pan's in the snow. Did you hit Pan?" (p17) comes from the burner's gossip. Valens's lie "She hit Pan" (ch-06:p322) went to a man who would have her "all over the town by the next market" (ch-06:p327) ✓ (N-04). **Mara giving her name:** "What name does the priest write?" / "The clerk wrote Maira." / "And you?" / "Mara." (p271–p274). This is the first time he has her name from her: ch-06:p333–p334 has "You have not asked my name either." / "No.", and her English "My name is Mara Reyes" on the cliff went past him (ch-06:p163–p164). She knows what the clerk wrote because she read it upside down (ch-07:p161, p171) ✓. **Valens's other knowledge:** the three drachmas he heard over the wall (p4–p5 → p27); Praxias's loss, from Felix (p170 → p263, p265) ✓. **The Ch.10 rewording:** the narration at p214 ("It was shorter, and it said less, and a priest would have nothing to ask me about it except where home was") is present-scene reasoning. It does not reach toward the god's answer ✓. Ch.13 cascades: N-17. |
| (4) Money and objects | **WARN ×1 (W-03, forward).** **The obol repaid:** owed since ch-09:p117–p119 ("An obol." / "He'll pay."), paid "For the pitch" (p21–p22) ✓. The staging is W-08(a). **Drachmas:** "three drachmas … all that the priest had paid me" (p10) = the smith's price (ch-09:p67, p148) ✓. After the obol, "less than three now" (p155) ✓. The purse is now "a knot at the corner of my himation" (p10), where it was a rag (ch-09:p168), so it is worded fresh as the bible asked; see N-01. **Kallia's papyrus obol:** still unspent and "knotted in with the remains of the priest's money"; "I had never gone up to the priest's house to buy the sheet, and her son's line was still unwritten" (p205). This agrees with ch-10:p85 and p92 ✓. **The watch:** see (1). Not returned ✓. **The sherd:** Mara's question was scratched on a piece of broken jar with a nail. The first text was "*The door that let me in is shut. Where is another?*" (p205, refining ch-09:p23). The back now reads "*Where is my road home?*" (p214). Felix's ΦΗΛΙΞ is on "another piece of the same jar" (p217), and he keeps it (p228–p230). ΦΗΛΙΞ is the correct Greek spelling of Felix ✓. **New objects:** the horn-handled awl, sharpened overnight (p55, p67); the breeching, girth, headstall, pad and breastband; the mules' bells stuffed with wool; the potted Caunian cutting; the twitch; the bran sacks; the yard gate's bar. |
| (5) World / history | **PASS** (W-02 is book-internal logic, not history). Checked: an obol carried in the cheek (p23); Caunian figs as the prized kind against Chian, dried whole on rushes (p75–p90); fig cakes pressed under a leaf (p78); a hoof abscess pared to the black spot, with gray pus and a hot bran poultice; the twitch and earing a mule (p124–p137); a Cilician slaver, a boy from Side, the Kirrha quay (p224–p226); boxing at the gymnasium before a festival (p117); quail fighting with side bets (p153, p170). Felix's "lucky, in Latin" is right ✓. Mara knows the god's birthday from her own reading, so it is not a credential aside ✓. |
| (6) NO FORESHADOWING | **PASS.** The gate reads 0. On a manual read: p95 ("By then, if there was any justice anywhere, I would be standing in a kitchen in Philadelphia with a tap in it.") is her expectation at the time, inside the scene. Any irony belongs to the reader, which voice-dna §0 keeps ✓. Praxias's "By then you'll have sailed for Syracuse" (p9) and Felix's "she's four years old and sound, or she was" (p226) are speech. Nothing in the narration reaches past the last evening of the week. Two lines *prime* the next chapter by narration. That is not foreshadowing in the law's sense, but it breaks the bible's "No pre-announcing Ch.12" rule: W-06 and W-07. |
| (7) NO TICS | **CRITICAL ×1 (C-01). WARN ×1 (W-11, a "said/told the [non-listener]" over cap).** **Gestures: PASS.** Bend/stoop 0, kneel/crouch/squat 0 (the CP2-3 gate holds), object handling 0, nods 0. "sat down" ×2 (Mara p253, Felix p256) are different people and different acts. **Caps held:** "as if" 1 (p7); "the way [X]" 2 (p23, p217); "Then…" speech openers 2 (p39 Mara, p97 Valens), at cap (N-01b); hinge paragraph openers 0; "Somebody/Nobody" paragraph openers 0; "the one / the only" claims 0; command echo 0, since every order is answered by its result ("Lamp," → "Felix had it lit and there before the word was well out."; "Hold this end," → "His fist closed on the end of the strap."); "He meant…" 0; lying-awake coda 0; laughs on the page 0 (one reported: the Cilician); cloth smells 0; taste recoil 0 (the fig is "very sweet"). **Running bits:** "the god's first day" ×2 (p29, p33); "board" ×4 (p34, p35, p135, p212; p135 is cut by W-06); the spout's shadow as a clock ×2 (N-08). |
| (8) Spent moves (every bible block) and Ch.10's set pieces | **WARN ×4:** W-08 (two set-piece beats rebuilt from Ch.9–10), W-09 (the Ch.4 boy's knife-cut hair), W-10 (the spent purse vehicle), W-06 (narrator pointer to the notice). **NOTES ×4:** N-09 (Kallia's work-suspended tell migrating to Mara), N-10 (a depth-by-joint sibling), N-12 (the haggle as a set piece), N-13 (sacking on a hoof spent). **Clean** against the rest, each checked by string and by shape: the [color]-of-[thing] shape (0); "Whoever [made] it had" (0); the absent-workman verdict 1, the cap ("sewn on by somebody who had never seen one sewn", p115); the stranger-freeze (0); men at a public place as a set piece (0, since Praxias at the wine-seller is Felix's report); a wound reopening (0); the emotional peak as a laugh (0, the peak is the near-kiss → hunger); the gaze-arrival "then" (0); Kallia's hearthstone shape (0); the reading-time measure (0); a held silence measured by something moving (0: p244's knot and p254's wick are his acts inside the silence, not measures of it; see N-08 for p130); "a man" as the requirement, voiced (0: Praxias describes the role and does not tell her she needs one); the god's price itemized (0 strictly, see N-23); the goat explained (W-02 removes a third, oblique explanation); Valens answering closeness with a practical order (0 after the near-kiss: wick, exit, stretch); Valens naming himself as traceable (0); footing orders (0); "How long…?" / "What for?" (0). **Ch.10's set pieces against Ch.11:** arrival at the gate, the reading, the name asked and shown, the neighbor, the reply offered, the obol, the broom, the exit, alone. Rebuilt in Ch.11: the name asked and shown (W-08b) and the coin set down instead of handed (W-08a). Not rebuilt: everything else ✓. |
| (9) Voice-bank lifts (zero allowed) | **WARN ×1 (W-12), sample-08 by structure.** By string: 1 hit, an idiom ("time and neither of", sample-10, the Ch.15 heat register), with no shared image; leave it. No sample-12 furniture. No sample-03 (Ch.13's goat) and no sample-05 (Ch.12's road). N-19: the close's plan-plus-payment shape sits near sample-08's last line, but the outline mandates that content. |
| (10) Memories (AUTHOR-CP2-2) | **PASS.** Memories on the page: 0, stand-alone or otherwise (the bible set Ch.11 at none). The 1998 frame enters only as present comparison: the toll collector "at the end of a shift" (p3), "kitchen matches" (p92), "a hat brim" (p231). The kitchen tap is a forward hope (p95), not a memory. See N-03 for its weight. |
| (11) Voice drift | **PASS, two WATCH items.** Mid gear holds (median 14). Dry asides sit at calm-chapter density and vary in form: "Kallia had one cousin, and I had just spent him." / "which sounded much like crying in anything else" / "the gray had not forgiven me for finding". The conservator's eye is on the breeching, as material and failure, not as credential (p55). Under the near-kiss the voice deflates correctly, to legs and hunger with no simile (the disruptor's surgery holds). **WATCH:** Valens is given deliberate wit in Greek (N-02; W-02 removes the sharpest), and the fig subtext is stated twice (N-03). |

---

## PRIORITY: UNRESOLVED ENTITY_STATE CONFLICTS (processed first)

The committed ENTITY_STATE covers Ch.1–10. I reviewed every open flag for relevance to Ch.11:
- **Chapter flags:** CH1-2, CH1-3, CH2-1, CH2-3, CH2-4, CH2-5, CH3-1, CH3-2, CH3-3, CH4-2, CH4-3, CH4-4, CH5-3, CH5-4, CH6-5, CH8-2, CH10-4 and CH10-6.
- **Blueprint flags:** P1, P3 and P4. P5 is resolved.

**None touches a Ch.11 fact.**
- **CH10-6** concerns who stood on Kallia's council line in AD 70. Ch.11's "Kallia said you would stand for her house" (p6) is the oracle sponsorship (ch-09:p60's "a Delphian to stand for you"), a different act. No action.
- **Plan rows the page supersedes** (prose wins; tracker to update, see patches):
  - `locations.valens-yard` "mules, horses, a tack shed": the page shows mules and a dog, and no horses.
  - `kallias-cousin` (unnamed, plan): the page names him **Praxias**, and the bible has a card.
  - ENTITY l.1823 leaves open whose building stood at "the last roof" (ch-08:p28). Ch.11 puts the yard on the Kirrha road below the town, which is compatible: Ch.8 shows him only standing at that corner.

---

## CRITICAL ISSUES (must fix before proceeding)

### [C-01] Valens's bare "No." has become his verbal tic (tic gate FAIL)
- **Audit:** NO TICS (author's law: tic budget 0, "nothing repetitive that makes it seem like AI"); `tic_report.py --gate` short-reply layer.
- **Evidence:**
  - The gate reports `short spoken reply "no" 11x in chapter 11 (cap 4)`: Valens ×9 and Mara ×2 (p146, p225).
  - Valens's prior bare "No." lines: ch-06:p235 (the fire), ch-06:p334 (her name) and ch-07:p106 ("No," said Valens, to "She's simple"; the bible logs that as spent).
  - So Ch.11 alone triples his book-wide total, to twelve. In two places the word comes twice inside four paragraphs (p119/p121; p187/p189).
  - No n-gram gate could see this, and a reader hears it as the way Valens sounds. That is a catchphrase by attrition.
- **Every instance, and what becomes of it:**

| # | ch-11 | Prompt | What the "No." does | Verdict | Becomes (his own plain syntax, silence, or a different refusal) | Δw |
|---|---|---|---|---|---|---|
| 1 | **p25** | "I need somebody … to carry my question in to the god." | the premise refusal: the chapter's first thing he says to her | **KEEP** | — | 0 |
| 2 | p40 | "Then sell me back the watch," | a second refusal of her, 15 paragraphs after #1 | REPLACE | **"With the god's money?"** A practical question back. He has just named her three drachmas (p27), so he refuses with her own arithmetic and promises nothing. p41 "Have you let it stop?" still follows, as her counter. | +3 |
| 3 | p119 | Felix: "Can I go? I'll have the stalls done before noon." | refusal #1 of the boxing | REPLACE | **"The yard's yours till I'm back."** It says what he means: you stay, and you mind it. This is refusal by assignment, not praise. p120 "It costs you nothing…" still answers it. | +5 |
| 4 | **p121** | Felix: "Have you ever seen a man killed with one blow?" | his card's evasion (the men he killed). The lie earns Felix's "You've never seen anything." | **KEEP** | — | 0 |
| 5 | p128 | Felix: "Do you want the twitch? … Or the rope on her hind leg?" | refusal | SILENCE | Delete p128. p129 "Felix stopped short." → **"Valens kept his eyes on the hoof, and Felix stopped short."** The reason still arrives at p139 ("She'd remember it."). | +7 |
| 6 | p187 | "You have been in yourself, surely." | factual denial | MERGE → SILENCE | p186 → **"You have been in yourself, surely. Or sent a question in by somebody else."** Delete p187–p189. p190 → **He answered neither. "Why not?" I said.** The ladder of two "No."s becomes one bare silence, and p191's "I don't want anything he's got." still lands. | +2 (with #7) |
| 7 | p189 | "Not even a question, sent in by somebody else?" | the second denial in three lines | (merged into #6) | — | — |
| 8 | **p240** | "There is no paper." | confirmation; it lands the chapter's paper theme ("He can say it." / "Paper gets taken off you,") | **KEEP** | — | 0 |
| 9 | p260 | "Will you wake him?" | refusal | REPLACE | **"He'll wake when he's cold."** A plain fact about bodies that means no. It is not an order and makes no comparison. | +4 |
| — | p225 (Mara) | Felix: "Has he told you about the Cilician?" | Mara's "No." | DELETE | Merge p224 and p226: Felix runs straight on into "He bought me off him…" without waiting. That is his card ("stacks two or three questions before anyone answers one"). | −1 |

- **Result:**
  - Bare "No." in Ch.11 goes from 11 to **4**: Valens p25, p121, p240 and Mara p146. That is the gate's cap, and the gate fails only above 4.
  - The three Valens keeps are spread across the chapter (opening, middle, late) and do three different jobs.
  - Valens's book-wide total becomes 6 over four chapters.
- **Headroom option (if the editor wants 3):** p25 → silence, **"He kept the stone going."** It stays compatible with p37 "He started on the blade's other face."
- **Freshness:** every replacement string has 0 uses in Ch.1–10 and the voice bank (grepped), and none duplicates a Ch.11 line.
- **Cascade:**
  - The dialogue share rises slightly, to about 37.2%.
  - The bible's Valens Ch.11 block must drop "'No.' twice to the boxing", "(never been in)", "(never sent a question)" and "(he will not wake the boy)".
  - **New cap for Ch.12 on:** Valens's bare "No." ≤1 per chapter. Ch.12 is gear-low and violent, and that is exactly where the tic would re-form.

---

## WARN ISSUES (should fix)

### [W-01] Felix knows Valens was up "Three times" in a night he "never heard a thing"
- **Audit:** Information flow.
- **Evidence:** ch-11:p149: "He was up all night with her. **Three times he was up to change it, and I never heard a thing.**"
  - If Felix heard nothing, he has no way to count. A reader will ask how he knows.
- **Suggested fix:** "He was up all night with her. **There's three sacks gone, and I never heard him once.** Why won't he let me? …" (−4). Felix counts the evidence, which suits his speed, and "sacks gone" and "never heard him" have 0 prior uses.
- **Cascade:** the bible's "up three times in the night (Felix)" stays true.

### [W-02] "none of his have ever been near a fire" turns Ch.9's shiver logic against the consultation, in a hyperbolic quip
- **Audit:** Book-internal logic and the spent goat explanation (bible after Ch.9: "explained once … demonstrated once. Ch.12–13's goat is shown, not explained"); Valens's register.
- **Evidence:**
  - ch-11:p280: "**He'd want more than you have if you had twice as much.** At Kirrha there's a man brings them over from Aigion on the boats, at half his price, and **none of his have ever been near a fire.**"
  - ch-09:p173, the goat man: "Mine all do it; **I keep them warm, so the water surprises them.** The fellow out beyond the stadium keeps his on the hill all winter, and you can pour a river on them and they'll only look at you."
- **The problem:**
  - By Ch.9's rule, a goat never warmed will *not* shiver, and an unshaken goat means "the god isn't receiving" (ch-09:p60).
  - Valens is recommending the one kind of goat the book has told us fails. A reader will either think he has blundered or read it as a plant for Ch.13's goat that "doesn't, then does". The second reading makes the line a setup.
  - It also re-explains the warm-goat trick by allusion.
  - The first sentence is a crafted hyperbole. His card gives him deadpan literalism, "mostly unintended", and saves dry understatement for Latin.
- **Suggested fix:** p280 → "**He prices for pilgrims.** At Kirrha there's a man brings them over from Aigion on the boats, at half his price, and **he lets you pick your own out of the pen.**" (−7). Valens picking the goat is his animal axis. "prices for pilgrims", "pick your own" and "out of the pen" have 0 prior uses.
- **Cascade:** p281–p282 are unchanged. Ch.13's shiver beat keeps its outline shape with nobody to blame.

### [W-03] The god's costs exceed Mara's money, and Ch.12 must close the gap on the page (forward-binding)
- **Audit:** Money/objects (cross-chapter arithmetic).
- **What she has:** "three drachmas … all that the priest had paid me" (p10), and after the obol "less than three now … And the god's share comes out of that first" (p155).
- **What it costs:**
  - The pelanos: "Call it a stater" (ch-09:p58). The priest's own wager logic, a stater against the smith's three drachmas (ch-09:p63–p72), puts the stater at about two drachmas.
  - Praxias "for a drachma" (p263).
  - The goat: the Delphi she-goat costs "More than that", more than her whole rag (ch-09:p175). The Kirrha man sells at "half his price" (p280), so more than 1½ drachmas.
  - Total: at least about 4½ drachmas against less than 3.
- The page knows it is short (p155), but nobody covers the difference, and Valens's close says "Bring your drachmas" (p284). A reader who counts will notice.
- **Suggested fix:** none in Ch.11. Mara's p155 shows she is aware, which is honest. **The Ch.12 brief must settle it on the page.** Either the Kirrha price comes in low enough to name, or Valens quietly pays the difference as an act, with no line about it (his card: help given as work, never as speech). Do not leave it to Ch.13.
- **Cascade:** if the editor prefers to ease it in Ch.11, p263's "for a drachma" → "for the two obols he lost" (+3, fresh) cuts the sponsor to a third and gives Praxias a joke. But it does not close the goat gap.

### [W-04] Blocking: she hears his back crack "from the bench", but she is sitting on the packsaddle
- **Audit:** Character location.
- **Evidence:**
  - ch-11:p253: "I sat down. There was **the packsaddle on its trestle** behind me, and my knees put me onto it".
  - ch-11:p254: "…until something in his back went with a crack **I heard from the bench**."
  - The shed holds "a bench under a window hole, a packsaddle on a trestle" (p55): two different seats.
- **Fix:** "a crack I heard **from the packsaddle**." (0 words; 0 prior uses).

### [W-05] The knot "came loose", then hangs up "with the knot still in it"
- **Audit:** Internal consistency (objects).
- **Evidence:**
  - ch-11:p244: "**The knot came loose in his fingers.** He was a while silent…"
  - ch-11:p247: "He hung the rope up **with the knot still in it**."
  - The disruptor kept p247 as the image of the unanswered question.
  - "came loose" reads as undone, which empties p247.
- **Fix:** p244 → "**The knot slackened under his thumbs.**" (−1). The knot is loosened, still there, and abandoned at p247. "slackened" and "under his thumbs" have 0 prior uses, and the fix avoids Ch.11's own "in his fingers" ×2.

### [W-06] p135 paraphrases the notice's text, as a narrator pointer, in the middle of the hoof scene
- **Audit:** Spent moves.
  - Bible after Ch.9: "**The notice's text: do not re-quote.** Ch.12's knowledge path refers to it in Valens's own words."
  - Bible after Ch.8: "Narrator call-out pointers to callbacks: SPENT … treat it as 0".
  - Bible after Ch.11 (draft): "No pre-announcing Ch.12".
- **Evidence:**
  - ch-11:p135, a one-sentence paragraph between "Not tomorrow." and "Bran": "**The board in the square had advised whoever went to fetch him to bring friends.**"
  - The notice's own words are "whoever takes him should take him with others" (ch-09:p169).
  - The sentence is the narrator's irony laid over his gentleness. It does the reader's work for them, and the scene has already done it.
  - It is also the narration's only flat statement that the notice is about him.
- **Fix:** delete p135 (−14). The juxtaposition survives without the pointer: Mara raised the board at p34, and the reader carries it into the hoof scene.
- **Cascade:** hook-craft's pull analysis (evaluations/hook-chapter-11.md, "Ending") cites this line as one source of the close's dread. After the cut, that dread rests on the barred gate and the olive path (p196–p203) and on the plan itself. The ledger is unaffected. See W-07: the orchestrator should rule on the two together.

### [W-07] A further road-watching beat one paragraph before the close
- **Audit:** Bible after Ch.11 (draft): "**No pre-announcing Ch.12.** The mind-reading's after-effect (gate, olive path) is done; Ch.12's men arrive on the road with **no further watching beat, look-out, ship or rumor in between**".
- **Evidence:** ch-11:p283: "He went to the gate **to look at the road, as he did every night** before he put the bar across. The dog got up off its side of the gutter and went with him."
  - This is a new watching beat placed directly before the line that names the road and the hour. It is built as dread for Ch.12's "Lupus?" on that road, and the hook report says so.
  - It is not foreshadowing under §0, because nothing in the narration reaches forward. But it is exactly the "further watching beat" the bible rules out.
- **Fix:** p283 → "**He went to bar the gate, and the dog got up off its side of the gutter and went with him.**" (−14). "bar the gate" has 0 prior uses, and the habitual night bar stays consistent with p197.
- **Cascade:** the close's pull changes from OMINOUS PROMISE to a plain practical plan. Hook-craft would rescore it, likely a point lower; the ledger asks only for `dialogue`. **Orchestrator call:** the writer's bible rule and hook-craft's design conflict here. I recommend the bible rule, under the book's no-reaching-forward stance.

### [W-08] Two beats rebuilt from the chapters just finished
- **Audit:** Bible after Ch.10 FINAL, NEW NAMED RISK: "list the previous chapter's set pieces and their beat order, and stage the new one in a different order with different beats."
- **(a) A coin set down to avoid a hand, three chapters running:**
  - ch-09:p149: the priest drops coins "from a little above, so that his fingers stayed clear of my palm".
  - ch-10:p92: Kallia sets an obol "on the bottom stair, where I would have to pass it".
  - ch-11:p21: "I untied the knot first and **put the obol on the stone of the trough beside him**."
  - Fix: p21 → "I untied the knot first and **held out the obol**." and p23 "He picked it off the stone and tucked it…" → "**He took it and tucked it** into his cheek…" (−10; both strings 0 prior). A plain handover carries no romance signal. Ch.6's "pinched it up off my palm" is avoided.
- **(b) An illiterate asks which marks are the name, two chapters running:**
  - ch-10:p65–p66: "Which is his name?" / "I turned the papyrus to her and showed her the opening word with a fingertip."
  - ch-11:p224: "**Which bit's me? Where does it start?** That one, with its arms on its hips, **that's the F.**"
  - Ch.9 also had the curse-tablet boy's "What's it say?". The last clause also has an illiterate boy naming a letter.
  - Fix: p224's middle → "**Is that one me, with its arms on its hips?**" (−8). He guesses at a shape and names no letter. The rest of Felix's speech stands. "Is that one me" has 0 prior uses.
- **Cascade:** the bible's Felix block (W-14).

### [W-09] Felix is introduced through a knife-cut haircut, which is the Ch.4 goat-boy's introduction plus a verdict on the maker
- **Audit:** Spent moves.
  - Bible after Ch.9: "The unseen maker judged … SPENT at 6 chapters (… Ch.4 the boy's hair …)".
  - Bible after Ch.10: whole set pieces rebuilt.
- **Evidence:**
  - ch-04:p4: "his hair had been cut short **with a knife** by a person in a hurry".
  - ch-11:p16: "**he had cut his own hair, with a knife, without a mirror**".
  - Two boys, both introduced through knife-cut hair, and "without a mirror" grades the cutter.
- **Fix:** "…belted up with a length of rope, and **his hair stood up every way at once, with straw in it**." (0 words). Fresh ("every way at once" and "straw in it" have 0 prior uses), and the straw anticipates the stall where he falls asleep.

### [W-10] "tighter than a priest's purse" reuses a vehicle the bible has spent, as a proverb in Praxias's mouth
- **Audit:** Bible after Ch.10 FINAL: "the pickpocket / purse / crowd-theft vehicle is spent at its first use (Ch.8); a vehicle domain is not reused for a second comparison anywhere". Praxias's card: "No oaths, no proverbs".
- **Evidence:** ch-11:p170, Felix's report: "he told the wine-seller the Syracusan **was tighter than a priest's purse**". The vehicle's first use is ch-08:p167: "as wary of my hands as a market woman with a pickpocket in view."
- **Fix:** "…he told the wine-seller the Syracusan **had haggled him down to nothing**, and then he went to the ring…" (0 words). It is Praxias's own spin, so it is funnier: he lowered the price himself (p151, p156). "haggled him down" and "down to nothing" have 0 prior uses.

### [W-11] Two "said/told the [non-listener]" frames (cap 1 per chapter)
- **Audit:** Bible after Ch.5 / Ch.9: "said/told the [non-listener]" is capped at 1 per chapter.
- **Evidence:**
  - ch-11:p71: '"Cooked," **I said, to the octopus**, but he was already on the roof.'
  - ch-11:p159: "he went off uphill, **telling the quail about it**."
  - Felix scolding the mules (p1, p38) is realistic animal-address and is not counted.
- **Fix:** keep the quail. p71 → '"Cooked," I said, but he was already on the roof.' (−3).

### [W-12] p231 rebuilds sample-08's pretext-maintenance tag
- **Audit:** Voice-bank lifts (zero allowed; voice-dna §6). Bible after Ch.8: samples "leak by structure as well as by string".
- **Evidence:**
  - sample-08: "He was rubbing tallow into a girth strap **that did not look as if it needed it**."
  - ch-11:p231: "…and found the knot in the end of a lead rope to work at, **which I had watched him tie that morning**."
  - The move is the same: on the threshold of a close conversation, his hands take up tack-work that isn't needed, and Mara adds a dry clause that exposes the pretext. The card's maintenance hands are legitimate. The exposing tag is the sample's.
- **Fix:** p231 → "…and he stayed, and found **a knot** in the end of a lead rope to work at." (−8). The knot still loosens at p244 (after W-05) and is hung up at p247.

### [W-13] Four second uses of earlier-chapter phrases that the 5-gram echo scan cannot see (CLAUDE.md step 5c)

| ch-11 | prior | Fix (fresh: 0 prior uses) | Δw |
|---|---|---|---|
| p3 Praxias "a **soft, heavy**, early-rising man" | ch-07:p42 Sostrata "a baker's wife with **a soft heavy** body" (the same pair, for a second walk-on's body) | "a **well-fed, slow-spoken**, early-rising man" (slow-spoken fits his card's unhurried sales talk) | 0 |
| p44 "**Since the snow** he had kept it going" | ch-09:p186 "First carts **since the snow**" (the Ch.10 brief already called it spent) | "**Since the mountain** he had kept it going" (avoid "all winter", already p50; and "since October/November", which the bible caps) | 0 |
| p228 "He put the sherd face up on the bench **with great care**" | ch-06:p131 Valens winding "**with great care**" | "He **laid the sherd** face up on the bench, his name to the light." | −3 |
| p69 "I had Kallia's water in before the sky was gray and was on the Kirrha road **by full light**" | ch-05:p210 "have … the water in to be on the cart track **by full light**" (the same sentence logic, chore then road) | "…and was on the Kirrha road **before the sun was on it**, going down while the pilgrims came up." | +3 |

### [W-14] The bible's Ch.11 blocks quote lines that are not on the final page, and the spent list therefore mis-records
- **Audit:** Bible currency. The blocks themselves say "the polish chain re-syncs", and this is that flag.
- **Evidence** (script: each quoted fragment in the Ch.11 blocks, checked against chapter-11.md):
  - **Valens block and At-risk after Ch.11:** "Felix can't either. It saves arguing." (0 on the page; it is listed as SPENT and as part of the reading reveal); "Come then."; "At the end of summer I shall not be here" (the page has "Somebody else would have to open mine," p96); Valens's "In the day." (the page has Mara's "and sleep in the day", p112); "Those want doing." (the page stages the refusal as action, p114).
  - **Felix block:** most of the stacked questions quoted are pre-polish. For example: "Is it you he took up to Pan's", "Which hand was it? Did it bleed much?", "Does it want feeding? Why can't I hold it?", "If the string's back by noon can I go?", "Why not? What's it cost you?", "Have you seen a Thessalian box?", "Shall I hold her ear for you?", "Is it true the baker's bird was fed on wine?", "Can I come down? Is it still nobody you want?", "Go on. What do I say?", "Is that the F? Will it stay on…", "Did he hit the Cilician?", "Do you know what it is in Latin?", "Can I show the dog?", "Is it cut on the wall?", "Did he take you to the god?". His "WATCH" opener counts (Is it…? ~9, etc.) were measured on the draft.
  - **Felix block:** Mara's "Felix says you cannot read." is not on the page.
  - **Valens block:** the page has "**He let that go by him.**" (p269), with "I waited for him to tell me why." standing bare after it.
  - **At-risk after Ch.11:** "Dialogue 35.5%; 6,288 words" is now 36.9% / 6,083.
- **Fix:** re-sync the Valens, Felix, Kallia and Praxias Ch.11 blocks, the Ch.11 walk-on block and "At-risk after Ch.11" to the final page **after** the fixes above. That covers C-01's "No." table, W-02's goat line, W-08(b), W-09's hair, W-10 and W-12.

---

## NOTES (polish / tracking)

- **N-01** (a) **The purse.** It is now "a knot at the corner of my himation" (p10, p21, p205), where it was "a rag" (ch-09:p168). That is fresh wording, as the bible asked, but the knot-corner purse is Kallia's (ch-06:p66, ch-07:p170). WATCH: it must not become a shared payment gesture. (b) **"Then…" openers in speech** are at 2 (p39 Mara, p97 Valens), the book's cap. Ch.12 should have ≤1.
- **N-02** **Valens's deliberate wit in Greek:** "Pressed, they're a cake. If I want a cake I'll buy a cake." (p84); "Chian are for men who've never had a Caunian." (p90). The fig argument is his chaos trait, so these stand. But his card gives Part One Valens "deadpan literalism, mostly unintended", and saves dry understatement for Latin. W-02 removes the sharpest. No crafted quip in Ch.12.
- **N-03** **The fig subtext is stated twice:** p95 ("By then … I would be standing in a kitchen in Philadelphia with a tap in it.") and p96 ("Somebody else would have to open mine"). The outline calls the fig argument subtext. Optional: cut p95's second sentence (−24) and let her line carry it.
- **N-04** **Felix's "Did you hit Pan? Which hand?"** (p17) is the burner's version of the Ch.6 story (ch-06:p322, p327). It is not the goat-boy's nymph rumor (spent) ✓. Nobody retells either again.
- **N-05** **p235 "Felix says you freed him on the quay at Kirrha":** Felix said "bought me off him on the quay" (p226). Mara's inference, confirmed by "Yes." No change.
- **N-06** **"Somebody selling eels" (p238)** on the Kirrha quay will make readers think of Ch.9's "Thracian sells eels at Kirrha" (ch-09:p190–p191). It is not winked, which is good. The tracker must not link the two, and later chapters must not either.
- **N-07** **New body facts against the notice.** The crooked nose and the eyebrow nick (p47) are marks a runaway notice would normally list, and the notice gives only the hand scar (ch-09:p169). This is acceptable for a copied board. Do not add facial marks to any later description of the notice.
- **N-08** **The spout's shadow used as a clock twice:** p44 ("by it the morning was nowhere near so far along") and p169 ("before the shadow of the spout had left the trough"). Logical, since she has lived without the watch, but it is an in-chapter running bit. Rest it. Separately, p130's Latin "went on until Felix gave it up and perched on the trough" measures a duration by a bystander. It is a cousin of the spent measured silence, so do not repeat that shape.
- **N-09** **Mara's stopped work as a tell:** "I had the headstall over my knees, and I put no stitch in it." (p130). This is Kallia's work-suspended tell (ch-07:p88, ch-09:p168, ch-10:p61/p63) migrating to the narrator. WATCH.
- **N-10** **"elbow-deep" (p115)** is a sibling of the CLOSED "to the [joint]" depth frame. Optional: "Felix stuffed it again from the barley straw in the loft" (−1).
- **N-11** **"Mule-man" is now 2 book-wide** (the burner, ch-06:p307; Praxias, p158). No third speaker uses it.
- **N-12** **The haggle as a set piece:** Ch.1 (Szabo), Ch.6 (the oak), Ch.9 (the stater), Ch.10 (the Elean's rate) and Ch.11 ×2 (Praxias, five → four → three and a half). This is Praxias's card, so it stands. **Ch.12's goat purchase must not be another counted-down haggle.**
- **N-13** **The bran-sack poultice bound round the fetlock** (p137, p148, p160, p256) spends the bible's "Sacking bound on mules' hooves … one more at most, worded fresh" (ch-06:p171, p314). That allowance is now used up.
- **N-14** **A chronological backstep:** p204 "Felix spent the afternoon climbing the gate" comes before p205's "that noon I left it on the bench". This is minor, but the chapter is Chronological. Optional: move p204 to follow p230.
- **N-15** **Valens's one- and two-word lines are dense.** Beyond the "No." lines there are "Again," "Near fore," "Lamp," "Bran," … "Hot." "Paid." "Yes." and "Felix." ×2 (p167, p265). They are different in kind, but Ch.12 (gear low) should vary the *kind* of short line, not only the word.
- **N-16** **Two list-shaped speeches in Valens's mouth:** p77 (the drying procedure) and p183 (the crowd by region). Neither is a device yet. His Ch.12 telling must stay a chronology of events, as his card says, and not become a catalogue.
- **N-17** **Ch.13 cascades.** Never point at any of these in narration or speech:
  - (a) "Take out the door" (p207) against the god's "at the door painted on a dead man's house".
  - (b) "Ask for a road. A road they'll answer." (p209) against "the road home lies…".
  - (c) Ch.9 rejected "*Where is the way back?*" as too short (ch-09:p23), and Ch.11 accepts a shorter question.
- **N-18** **Whose name the priest writes is open by design.** p29 says "A priest writes down the name of whoever goes in". The agreement (p271–p277) has the priest getting "The clerk's" name. Ch.13 must show it without a gloss from Valens.
- **N-19** **The close's plan-plus-payment shape** ("…the day after tomorrow, at daybreak … Bring your drachmas") sits near sample-08's last line ("Then we go at first light, and you pay me this") and ch-06:p142–p144. The outline mandates the content. Optional: drop "at daybreak" (−2). The last sentence is untouched, so the shape signature is unchanged.
- **N-20** **Two wine-sellers:** Ch.10's at Kirrha (a nail behind his jars) and Ch.11's in Delphi, "under the plane tree" (p170). The tracker should keep them distinct.
- **N-21** **p133 "put his wrist against it":** "it" reads as the lamp. Optional: "against the boy's arm" (+2).
- **N-22** **p44 "he had not put a finger to the hands"** is Mara's inference stated as fact. Optional: "and by the look of it he had not…" (+5).
- **N-23** **Praxias's p5 lists goat / cake / man** as what three drachmas will and will not buy. These are alternatives, not the spent itemized bill (ch-09:p58–p62). Near miss; leave it.
- **N-24** **Felix's "nobody" ×5 in speech** (p127, p204 ×2, p224 ×2). It is not a formula yet. WATCH in Ch.12, where the bible already asks for fewer Felix lines.
- **N-25** **Checked and correct:**
  - the Delphic calendar: Apollo's birthday on 7 Bysios, monthly consultations except the winter months, Delphian promanteia, the Castalian washing;
  - the pelanos as "the god's cake";
  - Caunian against Chian figs, dried whole on rushes;
  - the spelling ΦΗΛΙΞ;
  - hoof-abscess treatment and the twitch;
  - an obol carried in the cheek;
  - a Cilician slaver and a boy from Side.

---

## SUGGESTED YAML PATCHES (for entity-tracker UPDATE after the editor's fixes)

```yaml
suggested_patches:
  - entity: "timeline[chapter=11]"
    action: "update"
    value: { time: "about eight days: D1 Praxias at first light, the yard, the breeching tested at dusk; D2 the awl sharpened; 'For a week I mended his harness' (figs; the rain 'the next morning'; the boxing morning and the black lame 'that evening'; the fresh sack 'By morning' and Praxias; the walk up 'That evening'; the gate barred 'In the morning' and the sherd 'that noon'); 'the last evening of the week' (near-kiss, agreement)", next: "Kirrha 'the day after tomorrow, at daybreak'", season: "late winter AD 71: a rain shower; the potted fig leafless (p15), then 'twigs … green and hard at the tips' (p92); cloak thrown back at work", source: "ch-11:p3; p67; p68; p98; p124; p148; p175; p196; p205; p231; p284" }
  - entity: "praxias"
    action: "create"
    value: { replaces: "kallias-cousin (plan)", role: "Kallia's cousin on her mother's side; olive grower on the Kirrha road, one wall from Valens's yard; fighting quail", physical: "soft/heavy (or 'well-fed, slow-spoken' after W-13); beard clipped to a fringe; early-rising", prices: "Five (p2) -> Four, 'the standing thrown in' (p151) -> 'Three and a half' (p156); final: 'at the door for a drachma, if his name's said out loud' (Valens, p263)", lost: "two obols on the Amphissan's new bird against the baker's (Felix, p170)", calls_valens: ["the Corinthian (p11)", "Mule-man (p158)"] }
  - entity: "locations.valens-yard"
    action: "update"
    value: { place: "on the Kirrha road below Delphi, forty paces along Praxias's wall (p14)", features: ["cobbles and trodden dung; a long stable, rubble below and timber above, reed roof (p15)", "a shed at the end with a bench under a window hole, a packsaddle on a trestle, a shelf with pitch and flax thread (p55)", "a trough along the wall under a spout; gutter to the road (p15)", "the potted Caunian fig cutting in a sawn-off jar by the house door (p15, p92)", "a goats' gap in the back wall onto the olive terraces (p168)", "a gate with a bar, barred at night (p197, p283)", "a yellow dog"], horses: "none on the page (plan said mules and horses)" }
  - entity: "felix"
    action: "update"
    value: { first_appearance: "ch-11:p1 (voice), p16 (on the page)", physical: "thin, about twelve; tunic made for somebody broader, belted with rope (p16)", origin: "from Side; sold by a Cilician 'from Side to Kirrha'; bought on the Kirrha quay for more than the black (p224-p226)", freed: "no paper; witnesses 'The Cilician. Somebody selling eels.' (p238); 'He said I could go wherever I liked' (p228)", objects: "a sherd with ΦΗΛΙΞ scratched in capitals by Mara (p217-p230)", knowledge: ["believes Valens cannot read (p224)", "the watch is Mara's and 'He is keeping it for me' (p58)", "Mara 'hit Pan' (rumor, p17)", "no word of the notice, Lupus or the arena"] }
  - entity: "valens.knowledge"
    action: "add"
    value: [ { fact: "Mara's own name is 'Mara'; the clerk's record says 'Maira'", learned: "ch-11:p272-p274", method: "told_by:mara-reyes" }, { fact: "her question, both versions ('The door that let me in is shut. Where is another?' / 'Where is my road home?')", learned: "ch-11:p207-p214", method: "read (hidden)" }, { fact: "Praxias lost two obols at the quail ring", learned: "ch-11:p170", method: "told_by:felix" } ]
  - entity: "mara-reyes.knowledge"
    action: "add"
    value: [ { fact: "Valens reads Greek and hides it", learned: "ch-11:p207-p213", method: "witnessed" }, { fact: "Felix was freed on the Kirrha quay without paper before the Cilician and an eel-seller", learned: "ch-11:p226; p235-p243", method: "told_by:felix; told_by:valens" }, { fact: "Valens has never consulted the god or sent a question in", learned: "ch-11:p186-p191 (as fixed by C-01)", method: "told_by:valens (silence)" } ]
  - entity: "objects.fathers-watch"
    action: "update"
    value: { ch11: "in Valens's pouch; read without taking it out ('The short one's past the nine' / 'The long one's at the two'); fast against the spout's shadow; wound daily before his bread (Felix); not returned", source: "ch-11:p42-p46; p57" }
  - entity: "objects.maras-money"
    action: "update"
    value: { ch11: "'three drachmas in a knot at the corner of my himation' (p10); one obol paid to Valens (p21); 'less than three now' (p155); Kallia's papyrus obol knotted in with it, unspent (p205); owed: the god's share, Praxias's drachma, a Kirrha goat (see audit W-03)" }
  - entity: "objects.maras-sherd"
    action: "create"
    value: { made: "a piece of broken jar, scratched with a nail under Kallia's stair and in the shed (p205)", front: "The door that let me in is shut. Where is another?", back: "Where is my road home?", now: "with Mara" }
  - entity: "plot_threads.consultation"
    action: "update"
    value: { carrier: "Valens: 'I'll take it in. The day he first sits this year.' (p267); no reason given", sponsor: "Praxias 'at the door' (p263)", priest_record: "'The clerk's' name, Maira (p276-p277)", goat: "from the Kirrha man, 'at half his price'; Felix leads it up with barley (p280-p282)", money_gap: "OPEN, audit W-03" }
  - entity: "plot_threads.obol-owed-for-pitch"
    action: "update"
    value: { status: "PAID", where: "ch-11:p21-p23" }
  - entity: "plot_threads.fig-wager"
    action: "create"
    value: { status: "open", detail: "'You dry them your way, and I'll dry mine, and we'll open the two jars at midwinter and see.' (p94); Mara: 'Somebody else would have to open mine' (p96); 'Then I'm right.' (p97)" }
  - entity: "plot_threads.valens-paper"
    action: "create"
    value: { status: "open (Ch.12 telling)", detail: "'Paper gets taken off you,' / 'Who took yours?' unanswered (p245-p247)" }
  - entity: "plot_threads.the-black-mule"
    action: "create"
    value: { status: "healing", detail: "lame near fore from a gravel track, pared and poulticed (p124-p137); stands square on the bad foot so as not to wake Felix (p256)" }
  - entity: "plot_threads.kallias-reply-letter"
    action: "update"
    value: { status: "open, unwritten; the sheet not bought (p205)" }
```

---

## Proposed-wording freshness check

Every proposed string was grepped against Ch.1–10 and voice-bank/samples 01–13. All of the following have 0 prior uses and do not duplicate a Ch.11 line:
- "With the god's money?"
- "The yard's yours till I'm back."
- "kept his eyes on the hoof"
- "He answered neither."
- "He'll wake when he's cold."
- "He kept the stone going." (optional)
- "There's three sacks gone" / "never heard him once"
- "He prices for pilgrims." / "he lets you pick your own out of the pen"
- "from the packsaddle"
- "slackened under his thumbs"
- "He went to bar the gate"
- "held out the obol" / "He took it and tucked it"
- "Is that one me"
- "his hair stood up every way at once, with straw in it"
- "had haggled him down to nothing"
- "well-fed, slow-spoken"
- "Since the mountain"
- "laid the sherd"
- "before the sun was on it"
- "for the two obols he lost" (optional)

**Rejected candidates and their collisions:**
- "soon after" (ch-01)
- "a little after" (×2)
- "all winter" (ch-11:p50, plus ×2 prior)
- "in his fingers" (ch-11 ×2)
- "the gray went a dozen steps before he answered" (a silence measured by movement, ch-06:p278, spent)
- "Who would I send in?" shape (Kallia, ch-08:p106, spent)
- "With what?" (ch-06)
- "Let him sleep" (cliché)
- "did not so much as" (a negation tail)
