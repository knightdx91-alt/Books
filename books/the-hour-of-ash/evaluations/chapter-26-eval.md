# Evaluation: Chapter 26 — Letters in English (run 2) · Collage, six Fenn letters against Aelia's first weeks
**Evaluator:** book-evaluator (independent; did not write or revise this prose) | **Date:** 2026-10-24 | **Cycle:** 0
**Text evaluated:** `manuscript/chapters/chapter-26.md`, md5 `9d42bd0cfffd9a3942f6e8507b0908e1`. This is the page after writer → dialogue-polish → hook-craft (no edits) → disruptor → continuity repair (CRIT-001…006, WARN-01…18 bar 09/13/14/19, I-16, all logged). Nothing the repair fixed or ruled on is re-raised, except where noted (WARN-09, "very carefully", is re-raised on new grounds).

**Measured on the real file** (from the book folder):
- `bash tools/check_chapter.sh 26`: **ALL MECHANICAL GATES CLEAN** (style incl. foreshadow 0, grammar, rhythm, show/tell, voice-wear strict, tic gate incl. gestures, echo scan 0, metaphor, SHAPE CLEAN).
- `python3 tools/tic_report.py --gate`: clean. `--echoes 26`: 0 echoes, 0 command echoes, 0 spoken-line echoes.
- 5,315 words (shape), 89% of the 6,000 target. 7 breaks, 8 sections. Dialogue **11%** (band 10–20). Median sentence **15**, mean 17.6, 4.0% over 40 words. Simile 12 (fig 2.6/1k). Em-dash 0. And-chains 3/9. Credential asides 1. Negation pivots 0.
- Shape: `narrative` (italic letter, 23 words) → `quiet` ("He sat on in the sun with his lip in her fist…"), matching ledger row 26.

**Read against:** book CLAUDE.md; STATE.yaml guardrails, retired reflexes, AUTHOR-CP2-2 (memories), CP5-0b (voices from lives / nameable-rule test), CP5-1 (mountain never named); outline ledger row 26, `## Chapter 26` (beats, writer warnings, beat subversion) and Ch.27/35 cascades; voice-dna §0 (no foreshadowing, mountain rule, weight carriers) and §1; character-bible ("Voices from lives, not rules"; FENN incl. idiom pool and Ch.25/26 blocks; VALENS, GRATA, SECUNDUS, LUCIUS, AELIA, FELIX; At-risk after Ch.24/25/26 and the at-risk table); chapter-25 (Fenn's voice, the handoff, l.120); chapter-19 (rooms); the dialogue, hook, disruption reports and `continuity/chapter-26-audit.md` with its repair log; `chapter-25-eval.md` (bar and format). Coordinator's mid-task items CH26-2 (mule count) and CH26-7 (Secundus's notice) are folded into the fix set (G14, G15).

**Genre profile:** commercial historical romance / time-slip (comp *Outlander*). Anti-AI band commercial (0–8 clean). #11 cap: >6 instances or >0.8/1k. Dimension 7 = **IMMERSION**. Engagement (STATE): empathy 55 / fascination 30 / self-insertion 15.

*(l.N = line number in the evaluated `chapter-26.md`; word offsets in brackets.)*

---

## HEADLINE
**CVI-Launch:** **9.4** (8.9 + 0.5 strong anchor) | **CVI-Legacy:** **7.3** | **Genesis Floor:** **8.0** | **Genesis Average:** **8.64** | **Casual Reader:** **9.0**

**Engagement type (this chapter):** Empathy 60 (a mother reading a stranger's English to a newborn; a husband who wants into the letter; "Your old man. I'm sorry.") · Fascination 30 (a 1968 man raging at the word *voicemail*) · Self-insertion 10.

**Divergence alert:** none (CVI-Launch 9.4 vs Floor 8.0 = 1.4). The chapter is commercially warm and craft-strong. The Floor sits on two things no gate measures: (1) the narrated-trait census — Aelia's crying noted 5× (3 inside ~380 words), Aelia asleep noted 6× (3 inside ~210 words), Valens speaking "low" 3× in ~210 words; (2) two narrator reflexes that pass the nameable-rule test against themselves — the baby's reception of each letter told as a recap triad of its items (l.18, 38, 154, plus the street recap l.126), and the narrated omission from Mara's own letters (door, melon, voicemail: l.40, 134, 182). On top: a polysyndetic-triad cadence (9× = 1.7/1k), Fenn's Ch.25 refusal frame rebuilt by the dialogue pass ("Don't explain it to me, I mean it." ← Ch.25 l.120 "Don't tell me a thing. I mean it."), and a logic slip that pass also introduced ("one person around here"). All are clause-level; nothing structural; no beat needs rewriting.

**Gate:** Floor 8.0 < 8.5 → **POLISH** (Casual 9.0 ✓, pacing ✓, mechanical gates clean ✓). Tested fix set G1–G18 projects Floor 8.5 / Average 8.79.

---

## PACING VS NEIGHBOURS (gate item, judged)

| | Ch.24 | Ch.25 | **Ch.26** | Ch.27 (planned) |
|---|---|---|---|---|
| Shape | Fragmented, 8 breaks | Single-scene, 0 breaks | **Collage, 7 breaks** | Chronological walk, 3 breaks |
| Length | 5,696 | 7,343 | **5,315** (89%; 5,195 after G1–G18) | 7,600 |
| Gear / median | low / 10 | mid / 11 | **mid / 15** | high |
| Dialogue | 29% | 50% | **11%** (12% after fixes) | 35–45% |
| Slot | the stakes made flesh | turning point (the WHEN) | **deepen Fenn; Aelia; the refusal shown** | the cautionary mirror |

- **Length serves the beat.** 5,315 against 6,000 is right for a quiet interlude wedged between the book's two longest consecutive set pieces (7,343 and 7,600). Every outline beat lands (birth off the page; new 1964 material; the 1997 question and the voicemail rage; the box unopened with no reason; the word given and used wrongly and happily; the knucklebone; the named frame), and no section is underfed: the shortest (S4 dawn, ~370 words; S7 tables, ~350) are the comic and the withholding beats, which want brevity. Padding a letters chapter toward 6,000 would mean a seventh letter or more nursing texture, and both would dilute. The fix set takes it to 5,195 (87%); still serves the beat. Never padded: **holds.**
- **The median-run break is achieved.** Ch.23–25 sat at 10–11; Ch.26 measures 15, inside the mid gear the ledger asks for. The reading speeds the outline specifies land: letters brisk and voicey (Fenn's chains, the 1964 walk, the rage), domestic slow (the night feed l.16–22, the bench in the rain l.130–136).
- **Value shift, two axes.** Mara: Fenn's English as joy (l.18) → his tables shoved "under the bedstead, deep, into the dust" (l.210) — the refusal made physical. Valens: outside the language ("asleep in a language he did not have", l.104) → inside it by one word, given wrongly and happily at dawn (l.118–122).
- **Transitions:** all seven breaks hold (hook report concurs). S3→S4 ("gave it to her" → "Goodnight." to Grata) is the best cut in Part Two.
- **Handoff:** from Ch.25 the letters and tables promised arrive at once; toward Ch.27, the invitation is not in any letter (WARN-13 cascade already in the outline). Ch.27 is not pre-empted.
- **One soft stretch, not a sag:** S1's opening paragraphs (l.12–22, ~700 words of letter-description and night-feed texture before any exchange). The Devourer slows here; Grata's knock (l.24) rescues it.

**PACING: OK.**

---

## Genesis Score (Craft Assessment)

| Dimension | Score | Evidence | Cap Reasons |
|-----------|-------|----------|-------------|
| Originality | **9.0** | (1) The birth arrives secondhand, in the wrong language, from the wrong person: "*A girl, holy cow, and the carter swears the kid has a set of lungs on her they can hear at the river.*" (l.8) — the beat subversion fully realised. (2) "The letter was written on the reverse of a stranger's future." (l.12): a horoscope's blot as stationery. (3) The 1990s word as the one wound a 1968 man can't parse: "*But what in God's name is a voicemail?*" (l.150), answered by Mara sponging off "*It's a machine that*" (l.182). (4) The English word used wrongly and happily as a street greeting, and Grata answering it in kind (l.118–120). | none |
| Theme | **9.0** | "Two languages, two homes, one family" is carried by acts and objects, never stated: "asleep in a language he did not have" (l.104); Mara naming the street to Aelia "in the language she heard all day from everybody but me at night" (l.126); Fenn's "*All this time I've been keeping the words… Nobody said they'd go on making new ones without me.*" (l.150); the box slid under the bed with no reason (l.210). Texture well over 30% (the eye-splice, the strainer's three rivets, the swaddling bands strung across the shop front, the carter's wife's luck, Felix's eyebrow, the dun's ford). | not 9.5: the language motif runs very dense in S1–S4 (Grata's "scratching", the street's Latin, the scissors/shears); each instance earns its place, but the Critic feels the pressure |
| Characters | **8.0** (uncapped 9.0) | **Fenn** is fully alive with zero narration of him: the stair "*charged me like he was putting up the Walt Whitman Bridge*" (l.8); the self-correction "*Okay, he told me in Greek. You get the idea.*" (l.36); his sister's scorecard "*like a bank deposit slip, every little diamond*" (l.60); the deflection to the bathhouse pool (l.64); "*I bought myself a melon.*" (l.132); "*P.S. I read your letter again. Your old man. I'm sorry.*" (l.208). **Valens** is jealous of a language without a word of jealousy: "Who's dead?" (l.68), "All that way with her, and no name." (l.80), "She sleeps for that." / "She was full last night." (l.90–94), "Put that in." (l.180). **Felix** has his own moment (the eyebrow lie, "Is it open for good?", l.190–198). **Grata** floods and commands (l.140 "You'd best stop eating standing up."). Mara's chaos 4/4 inhabited (below). | **Hand rule (>3 notes of one state, or 3 inside ~500 words):** Aelia crying 5 (l.16, 22, 28 inside ~380 words); Aelia asleep 6 (l.88, 104, 112 inside ~210 words); Valens speaking low 3 in ~210 words (l.88, 112 ×2). **Nameable-rule test fails twice on the narrator:** the baby-reception recap triad (l.18, 38, 154 + l.126) and the omissions from her own letters (l.40, 134, 182). → **cap 8.0** (same practice as Ch.24/25; the spec's 7.5 NO-TICS cap is reserved for a verbal tic or a cast-wide device, which this is not) |
| Prose & Voice | **8.0** | **Stopping sentences:** "He sat bent forward with his big hands hanging loose, gazing at his daughter, who was asleep in a language he did not have." (l.104); "My father was not in it anywhere." (l.156, one-line paragraph). **Underlines:** "until somebody knocked the ink over the son" (l.12); "A drop of milk had already landed on the Walt Whitman Bridge" (l.12); "Partway down the sheet I stopped over scissors and wrote it twice in the margin to see which looked right; both looked wrong, and I wrote shears instead and went on." (l.40); "every long stroke in the letter had a hair of a second stroke running beside it" (l.148); "so that the wine going through would find a strainer and never learn of the patch" (l.136). **Ugly sentence:** "Piercing it was dull and slow." (l.136). **Voice under pressure:** at the rage letter the prose deflates to body and plain verbs ("It soaked my tunic through to the skin, warm and then cold. I sat at the bench in it and read her the rest.", l.154). | not 8.5 at cycle 0: polysyndetic triad cadence 9× (1.7/1k, Pattern #3 strong); the reused Fenn refusal frame and "I mean it" (l.150 ← Ch.25 l.120); the "one person around here" logic slip (l.132); the wine-as-dupe conceit twice in ~110 words (l.134, 136); "very carefully" 4th book-wide in the close, lifted from the outline's design note (l.250) |
| Pacing | **8.5** | See PACING VS NEIGHBOURS. The S3→S4 cut ("gave it to her" → "Goodnight.") and the 1964 letter's run ("*under every streetlight she stops and reads me the game off the card… before we're home she's read it so we nearly won*", l.62) are the speed peaks; the bench in the rain is the deliberate slow. | not 9.0: S1's ~700-word lead-in before Grata's knock |
| Emotion | **9.0** | **Anchor lands:** "I read it in English. Since my first winter in Phocis I had used no English aloud unless somebody was there to hear it. I had settled the question of whether Aelia was somebody on the night the letter came; nobody else was awake to argue." (l.18), with the bakers' voices "the only others in the street". **Surprise:** Valens's "Who's dead?" at a baseball letter; the word for a day's end said as a dawn greeting; Fenn's rage that is grief. **Body rebel:** "Partway down, my milk let down, both sides at once, though she had fed an hour since and wanted nothing." (l.154). **Techniques:** physical, humour in grief (the carter's hood; "*I got used to Claudius*"), dramatic irony (the reader knows the summer Fenn means), withholding (Margaret's name in the satchel, l.82; the box), objects (the pale cloud of the sponged line, l.182), memory (the voicemail, l.134). | none |
| Immersion | **9.0** | Flavian Pompeii: the raised stepping stones in a flooded street (l.130); the girl's eighth day and the bronze lunula on a red thread (l.42, correct); lampblack-and-gum ink lifting with a wet sponge (l.182, correct); a horoscope's reverse as stationery; the carter's post via a thermopolium; the sailing season opening (l.198–200); a painted wall notice (and after G15, a "rooms to let" notice, Pompeii's best-known genre). 1964 Philadelphia (Callison's three home runs in a 14–8 loss on 27 Sept, 21st and Lehigh, Germantown Avenue to Mount Airy at dusk) and 1997 (Marlins in eleven innings, the office voicemail's red light) are exact (audit verified). | not 9.5: the Hostile's trust slips on the mule count (l.116, CH26-2), a campaign notice a year before the election (l.140, CH26-7), and a bay wind at a light-well window (l.20) — G14, G15, G18 |
| **FLOOR** | **8.0** | Characters, Prose | |
| **AVERAGE** | **8.64** | (9.0 + 9.0 + 8.0 + 8.0 + 8.5 + 9.0 + 9.0) / 7 | |

### Narrated-trait census: EXHAUSTIVE, cycle 0 (spec: >3 notes of one state, or 3 inside ~500 words, fails)
Every recurring character, every narrated state. **Class rulings, fixed here so later cycles do not re-litigate them:** feeding is Aelia's situation, not a re-noted state (the chapter is her first weeks); her grip on Lucius's lip at l.244/246/250 is ONE designed action (grab → held through the breath → held past release), the named frame; Valens's looks split into attention-to-work (rope, flame) and looks-at-people; Lucius's rolling sequence at l.216 is the outline's beat 6 (the act itself, not fidget), so the prop rule applies only to the business around it.

| Character | State | Lines [word offset] | Count / spacing | Verdict |
|---|---|---|---|---|
| Aelia | crying ("roar" ×6) | 16 [~450] ×2 · **22 [~830]** · 28 [~920] · 38 [~1,300] · **88 [~2,400]** | **5; l.16/22/28 inside ~380 words** | **FAILS** → G1 (l.22, l.88 recast) → 3, none 3-in-500 |
| Aelia | asleep | 38 [~1,330] · 88 [~2,330] · 104 [~2,490] · **112 [~2,600]** · **130 [~3,100]** · **136 [~3,560]** | **6; l.88/104/112 inside ~210 words** | **FAILS** → G2 → 3 (38, 88, 104) |
| Aelia | mouthing / sucking reflex | 42 + 46 (one adjacent beat) · 136 · 232 | 3, spread | OK (WATCH) |
| Aelia | grip | 38 neckline · 154 thumb · 244–250 the frame (one action) | 3 events | OK |
| Aelia | lent adult mood | — | 0 | OK (Ch.26 guard) |
| Valens | asleep / wakes | 22 · 158 · 182 | 3, spread | OK |
| Valens | looks at people | 104 gazing · 158 lay watching me · 234 watching the boy | 3 [~2,500 / 4,200 / 5,160] | OK (WATCH) |
| Valens | eyes on work | 54 rope · 112 flame | 2 | OK |
| Valens | speaks low | 88 [~2,400] · **112 "low" [~2,560]** · **112 "very low" [~2,600]** | **3 inside ~210 words** | **FAILS** → G2 → 2 |
| Valens | hands | 66 stopped · 104 hanging loose · 240 drawn back and held | different states | OK |
| Valens | arm over eyes | 168 · 170 | 2, one beat | OK |
| Lucius | gaze | 48 (one sentence) | 1 | OK |
| Lucius | bone handled (prop rule, business around the rolling) | 216 "in his fist" · 216 "showed the bone" · 226 Valens rolls it on his palm | 3 in ~60 words on top of the rolling | → G9 (−1); G8 removes the l.210 hand-off line |
| Lucius | still / breath held | 244 · 246 | one event | OK |
| Felix | stacked-question burst | 122 (three, reported) · 198 (two) | 2 bursts; form rotated (l.190 is a single) | OK (Ch.24 WATCH) |
| Felix | exits before an answer | 122 | 1 (audit WARN-04 repaired) | OK |
| Grata | through the plaster | 24 · 120 (her speech) | 2 | OK |
| Grata | flood → command | 26 · 44 · 120 · 140 | her card's syntax; asks no question ✓ | OK |
| Fenn (narration) | handwriting described | 12 · 148 | 2 | OK |
| Fenn | tremor | 8 (his) · 12 "where the wrist had tired" · 206 (his) | 3, spread | OK |
| Fenn | Ch.25 SPENT narrated states (talking on, break-offs, object-looks, taking in news, lighter) | — | 0 as narration | OK |
| Mara | recap triad of a letter's items as the baby's reception | 18 · 38 · 154 (+126 the street) | 3–4; nameable | **device** → G3 |
| Mara | omissions from her own letters | 40 door · **134 melon** · **182 voicemail** (+82 satchel, 124 did not call) | 3 + 2 kin; nameable ("she tells you what she left out") | → G5 → 1 (l.40), the sponge carries l.182 |
| Mara | words escape her | — | 0 | OK (≤1 in Ch.26) |
| Narration | "fist" | 16 · 38 · 66 · 154 · 216 · 232 · 246 · 250 (+140 Grata) | 8 | leaned-on word → G9, G16, G17 → 5 |
| Narration | "every customer" / "wanted nothing" | 14, 130 / 154, 216 | 2 / 2 | in-chapter echoes → G11, G12 |
| Narration | bakers as time marker | 18 · 28 · 126 | 3 | OK (audit I-16 applied) |
| Narration | "every" | 11 in narration, 7 Fenn, 2 Grata | 20 (3.8/1k) | WATCH; G11 takes one |

**Nameable-rule test (CP5-0b):** Fenn PASSES (his and-chains, asking and refusing, the confident future are his life; openers and sign-off deflections all differ). Valens PASSES (no comparison in his mouth; nobody remarks on it; the audit removed "which he did seldom enough that I noticed it"). Grata PASSES (she never asks; it reads as her trade, not a rule). Felix PASSES (WATCH). **The narrator FAILS twice** (recap triad; listed omissions) → G3, G5. Aelia's "roar" reads as a word-rule by l.38 → G1.

### Laws (scan)
- **NO FORESHADOWING: 0.** Fenn's "*She'll be near four the summer we go, by my book*" (l.10) is his own confident future (card). The narrator never touches it (WARN-03 repair verified; after G3 the l.18 recap is gone entirely). No forward reach: l.12's damp-day clause and l.126's "would hear" were repaired. "Before him, the only English ever spoken aloud in that street had been mine." (l.124) is past-facing fact, not a tag.
- **NO TICS:** gates clean (phrases, gestures). Hand-count findings G1, G2, G9; narrator devices G3, G5.
- **Fenn never lists: holds.** "*about the automat and the El on Market Street and a girl in homeroom who sat behind me and smelled of oranges, and somewhere around the third watch…*" (l.36) dissolves into the broom-handle story: a runaway chain, not an inventory. The rage's "*like it's bread, like everybody's got one, like a fellow ought to know*" (l.150) is an anaphora triad → G6 makes it a pair. "*Is it a letter you talk into? Who carries it? Where's it go when nobody's home?*" is asking-and-refusing (card) and stays.
- **Retired reflexes:** significance-tagging 0; define-by-negation 0 in narration; **anaphora triads 2** (l.112 "At his first try… At the second… On the third" → G2; l.150 → G6); **performed candour 1** ("I mean it.", l.150 → G6); **device as scene button 1 beyond allowance** (the knucklebone closes §2 *and* §7: "Back in the shop, I gave him the bone.", l.210, which also repeats l.48's "I gave him the knucklebone" → G8; §2's "since somebody's goat died" stays as the one); closing aphorism 0.
- **No spoken line reused:** echo scan 0, but the scan cannot see a reused frame: "*Skip it. Don't explain it to me, I mean it.*" (l.150) rebuilds Ch.25 l.120 "Don't tell me a thing. I mean it." — the dialogue pass's swap for "Don't you dare" moved the echo sideways → G6 cuts the sentence ("*Skip it.*" already refuses).
- **Closed / spent lists:** who-pays frame 0 ("Who carries it?" is postal, audit I-12); "by degrees" 0; Ch.24 birth machinery 0 (no teeth, stool, watch, jar-lift, "whole?"); Ch.25 SPENT narrated states 0; "kept … to myself" 0; "Nobody had [verb]" 1 (l.16, WATCH ≤1 ✓); idiom pool within caps (holy cow 1, the whole shebang 1, knock it off 1, monkey's uncle 1; Chico Ruiz 2/2 now SPENT; the 23 1). **"very carefully" 4th book-wide** (Ch.17 ×2, Ch.21, Ch.26) and the outline's own design words → G13. *INVESTIGATE, no action:* "*a long life and so forth*" (l.36) is Fenn summarising his own Ch.25 horoscope ("A long life, under his own fig tree", SPENT); a wry self-report, not a quote.
- **The mountain: 0. "Margaret": 0** (her name stays in the notebook, l.82: "I left the satchel as it was.").
- **House on Ch.19's layout:** no upper floor (CRIT-001 repair verified: the shop opening, the back room, the light-well, the outside roof stair at l.182). One residue: "the shutter barred on the wind off the bay" (l.20) puts the bay at a window that opens onto a light-well → G18.
- **Memory rule (CP2-2):** the voicemail (l.134) is triggered by Fenn's question and returns into the letter she writes; one longer memory, and Ch.25 had none (alternation holds). "Marlins." (l.136) is a short irrelevant thought that returns to the rivets.
- **Writer warnings:** the English word is never a callback ("Goodnight." quoted once, l.118) ✓; Fenn never numbers ✓; no narrator commentary on the unopened box (l.210: an act, no reason) ✓. Valens learns no date, rule or place ✓.
- **Dialogue ≥10%:** 11% now; 12% after the fix set (all cuts are narration or letter text).

---

## CVI-Launch Breakdown (Commercial Assessment)
| Input | Score | Evidence |
|-------|-------|----------|
| Commercial Pacing | 8/10 | Short sections, letters that read in a breath, a comic dawn, a quiet close with no cliffhanger (correct for the ledger, but it does not pull like Ch.25). |
| Tomorrow Test | 4+ anchors → 10 | IMAGE: Valens saying "Goodnight." to Grata over her shutter boards at daybreak, then to the dun; the newborn's fist on her brother's lip while he holds his breath for the camera; the sponge lifting "*It's a machine that*" and leaving a pale cloud; the milk letting down at the rage letter; the tables slid under the bed into the dust. QUOTE: "*Who won the Series in ninety-seven?*"; "*Nobody said they'd go on making new ones without me.*"; "Who's dead?"; "*Your old man. I'm sorry.*"; "*I bought myself a melon.*" |
| Casual Reader | 9/10 | see report |
| Shareability (quote / plot / emotional) | 4 / 3 / 4 → 8 / 6 / 8 | MAX 8 × 0.6 + AVG 7.33 × 0.4 = **7.73** |
| Concept Pitch | yes → 10 | "The only other American in the Roman world writes her letters in 1968 slang, and she reads them aloud to her newborn while her husband grows jealous of a language." |
| Human Closeness | yes → 10 | A nursing mother, a husband at the bedside, a neighbour through the wall, a lonely old man on paper. |

**CVI-Launch** = 8×.2 + 10×.2 + 9×.2 + 7.73×.2 + 10×.1 + 10×.1 = **8.95**, + 0.5 strong anchor = **9.45 → 9.4**.

**CVI-Legacy (default weights, empathy primary):** Originality 9.0×.30 + Theme 9.0×.25 + Cultural vocabulary 3×.20 (niche: "the summer we go", "voicemail" as Fenn's wound) + Re-readability 8×.15 (the box under the bed against Ch.35–36; "*A line about the milk*" in a nursing chapter; the scorecard on the hall table against Ch.35; Margaret's name in the satchel; "the summer we go") + Identity 5×.10 = 2.70 + 2.25 + 0.60 + 1.20 + 0.50 = **7.25 → 7.3**.

---

## Anti-AI Scan (20 Patterns), 5,315 words
1. Forced symmetry: Clear ("warm and then cold" is sensation).
2. Empty poetic vocabulary: Found, 1 (minor): "something else that was only hers" (l.16), stock new-baby phrasing → G4.
3. Automatic rule of three: **Found, 9 (1.7/1k, strong)** — polysyndetic "X and Y and Z": l.16 fists/feet/jaw; l.16 milk/wool/something only hers; l.18 rope walk/bridge/peanuts; l.38 broom handle/tables/initials; l.46 hair/beard/blanket; l.126 loaves/boys/bucket; l.130 charcoal/old wine/milk; l.154 God's name/fish/Syrian sailors; l.216 bone/dust/cobweb. Plus the ordinal triad l.112. → G2, G3, G4, G9 leave 3 (l.16 body, l.130, l.40's four-item reply list), 0.6/1k.
4. Em dashes: Clear (0).
5. Empty metaphors: Clear. "a red eye in its ash", "a warm sack of flour" are concrete.
6. Dramatic "And" openings: Clear in narration (Fenn's "*And tell him my stair's fixed.*", "*And we lose fourteen to eight.*" are his chains).
7. Pseudo-philosophical closings: Found, 1 (minor): "The bone had lain in the dark since somebody's goat died." (l.48) closes §2 wryly; it stays as the bone's one section close once G8 removes the second.
8. Excessive parallelism: Found, 2 (minor): "every rule I was ever taught and every rule I had since taught to other people" (l.48, designed pair, stays); l.112 ordinal series (G2).
9. Overly smooth transitions: Clear; the collage jumps in time without glue ("When Aelia was eight days old…" after week four).
10. Described emotions: Clear in narration ("He's angry with me." is speech).
11. Explanatory extension: Found, 3 (0.56/1k, under the 0.8 cap): l.134 "The melon got no mention; whatever there was to say about it, the sheet had no room for."; l.182 "What a voicemail was, I did not explain." (glosses the sponge); l.12 "where the wrist had tired" (stays). → G5 removes two.
12. Binary negation opener: Clear.
13. Precision flex: Clear (nine days, three rivets, fourteen to eight are functional; "I read it just enough to know the roll had not run out", l.230, refuses the flex).
14. Emotional control demonstration: Clear; the milk lets down against her will and she reads on in it, which is the opposite pattern.
15. Authoritative description: Clear; gaps are left ("for no reason I could find", "The feet went still while he worked at it in there").
16. Philosophical asides: Clear in narration.
17. Clean dialogue: Clear. Non-sequitur answers ("It's uphill, that street."), a question ignored for his own news ("The ford at Stabiae's… Put that in."), Felix gone before the answer.
18. Thematic echo chamber: Clear (WATCH: language is dense in S1–S4, but the strainer, the rope, the rain, Felix and the mules are pure texture).
19. Graduated reveal: Clear; collage, not normal→anomaly→escalate.
20. Emotional temperature report: Clear.

**Total: 5 patterns found (#2, #3, #7, #8, #11) — commercial CLEAN band (0–8).** Weighted: #3 strong −0.50; #11 moderate −0.25; #2, #7, #8 minor −0.125 each = −1.125, reflected in the Prose 8.0. After G1–G18: #3 drops to moderate, #2 and one #8 clear, #11 to 1 → 3 patterns.

---

## Character Chaos Check (Primary: Mara)
- Irrelevant thought: **present, inhabited** — "Marlins. A marlin was a fish men hung from a dock by its tail to be photographed beside, not a fish anybody ate. A boy on the 34 had worn the team's cap all that fall…" (l.136), mid-riveting, unremarked.
- Cognitive distortion: **present, inhabited** — the rationalised exception, "I had settled the question of whether Aelia was somebody on the night the letter came; nobody else was awake to argue." (l.18); the refusal enacted as housekeeping (the box "deep, into the dust", l.210).
- Unprompted memory: **present, triggered and returned** — the voicemail (l.134), grown from Fenn's question, written into her answer.
- Failed emotional management: **present** — the milk let-down at the rage letter (l.154).
- Voice under pressure: **demonstrated** — l.154–156 deflate to plain verbs and a one-line paragraph.

## Secondary Character Chaos
- **Fenn:** own moments throughout (the broom handle, the melon, the rage, the P.S.).
- **Valens:** own moment — the wrong theory ("She sleeps for that."), the word asked for, the ford "Put that in."
- **Grata:** own moment — the Chaldean prophecy and her husband's curse (l.44); the wall grievance (l.140).
- **Felix:** own moment — the eyebrow lie and the sea question (l.190–198).
- **Lucius:** own moment — the held breath for the camera, "His eyes ran over." (l.246).
- No secondary is a mere function.

## The Tomorrow Test
**What the reader remembers:** Valens, at daybreak, halting his mules beside Grata's shutter boards and saying "Goodnight." in a clear voice — and Grata answering it as a greeting, "and to all your mules". Close second: "*Nobody said they'd go on making new ones without me.*"
**Anchor type:** BOTH (image: the dawn "Goodnight."; quote: the rage letter's last line).
**Verdict:** ANCHOR EXISTS (strong). Not a repeat of Ch.25's type (Ch.25's was a spoken recognition line; this is a comic misuse plus a written line).

## Shareability
"There's a guy stuck in ancient Rome since 1968 who writes her a furious letter because she used the word *voicemail*." One clean shareable moment.

---

## Reader Reports

### The Devourer
Flies through the letters; Fenn is the reason to read. Slows in S1 (l.12–22, the handwriting and the night feed) and would skim the strainer paragraph (l.136) if the Marlins thought weren't in it. Keeps going because of "Who's dead?" and the dawn "Goodnight." Would not stop anywhere. Notes the close is quiet, no hook — fine, Cumae is promised by the book's own momentum.

### The Critic
Underlines l.12 ("the reverse of a stranger's future"), l.40 (scissors/shears), l.104, l.148, l.156, and the whole 1964 letter. Disappointed by the cadence: by l.38 the "X and the Y and the Z" recap has become audible ("the rope walk and the bridge and the peanuts" / "the broom handle and the tables and both initials" / "God's name and the fish and the Syrian sailors"), and by l.182 Mara has told us three times what she left out of a letter. Flags "something else that was only hers" as the one generic phrase, and the wine fooled twice in two paragraphs (l.134, 136).

### The Hostile
- l.116 "five mules": four crossed in Ch.18/19 and nobody bought a fifth (CH26-2) → G14.
- l.140: an election-style name painted for Secundus more than a year before the March AD 77 election (CH26-7) → G15.
- l.132 "as of this letter that's one person around here who knows it": the person who now knows is Mara, who is not "around here" → G7.
- l.150 vs Ch.25 l.120: Fenn's "Don't … I mean it." refusal, again → G6.
- l.20: wind off the bay through a window that opens on a light-well (Ch.19) → G18.
- l.46: a 1–6-week-old who "put everything in her mouth" is early (deliberate mouthing is a 3–4-month skill); rooting at hair and beard is plausible. INVESTIGATE, no fix (the bible's age-stage note).
- l.250 "very carefully": fourth use book-wide → G13.

### The Casual Reader (9.0)
Picks it up on the first line and grins: a baby announced by a cranky old American in ancient Rome. Likes everyone on the page, laughs at "Goodnight." at dawn, gets a lump at the voicemail and the P.S. Would text a friend about the voicemail letter. Would not notice the triads or the census. Slight drift in the first page of night-feeding description. Buys.

### The Devoted Reader (active: long saga, Outlander readership)
Will catch that the tables go under the bed where Lucius later crawls for the bone ("The feet went still while he worked at it in there"); that "*A line about the milk*" sits in a nursing chapter; that the scorecard on the hall table is the place of the 1968 note; that Margaret's name is in the satchel under the letters. Will write about Valens's "goodnight". Re-read reward high.

## Cross-Reader Matrix
| Issue | Devourer | Critic | Hostile | Casual | Devoted | Severity |
|---|---|---|---|---|---|---|
| Recap triads / triad cadence (G3, G4, G9) | | ✓ | | | ✓ | SHOULD FIX |
| Narrated omissions ×3 (G5) | | ✓ | | | | INVESTIGATE (fix: nameable rule) |
| Aelia crying/asleep census; Valens low (G1, G2) | | ✓ | ✓ | | | SHOULD FIX (gate rule) |
| Fenn's Ch.25 frame reused (G6) | | ✓ | ✓ | | ✓ | IMPORTANT |
| "one person around here" (G7) | | | ✓ | | ✓ | SHOULD FIX |
| Mule count / early notice / bay wind (G14, G15, G18) | | | ✓ | | ✓ | SHOULD FIX |
| "very carefully" 4th (G13) | | ✓ | ✓ | | | SHOULD FIX |
| S1 lead-in slow | ✓ | | | ✓ | | SHOULD FIX → no edit; G3/G4 trim it by ~30 words |
| Bone as second section button (G8) | | ✓ | | | | INVESTIGATE (retired reflex: fix) |

---

## Revision Recommendations (Ranked)
*All are tested together in the script below (applies once each; second run aborts; `check_chapter.sh 26` ALL CLEAN; `--echoes 26` 0).*

| # | Location | Problem type | What happens now | Why it fails | Revision direction (exact) | Project rule? |
|---|---|---|---|---|---|---|
| G1 | l.22, l.88 | Character | "Nothing short of the roaring woke him"; "She had roared at him from start to end of it" | Aelia crying 5 notes, 3 inside ~380 words; "roar" ×6 | → "Only the baby woke him; the English never had." / "She had fought him from start to end of it until I came through." | Yes: an infant's cry/sleep counts in the census |
| G2 | l.112, l.130, l.136 | Character / Style | first/second/third ordinal triad; "very low"; "She went on sleeping through it…"; "asleep against me in the sling"; "did not wake for the tapping" | Aelia asleep 6 notes (3 in ~210 words); Valens "low" 3 in ~210; anaphora triad | → "He tried it twice, low, eyes on the flame; the word broke in two, and then its pieces ran together. After that he leaned down over Aelia and gave it to her." / "with Aelia against me in the sling" / "Through the tapping her cheek stayed squashed flat on my collarbone, and her lips went on sucking at nothing." | No |
| G3 | l.18, 38, 126, 154 | Style / Character | the baby's reception told as a recap triad of the letter's items, ×3 + the street | nameable narrator device; Pattern #3 | → "She had it from me three nights running, in the voice…" (agrees with "On the third night"); "She roared straight through to the initials."; cut "the loaves and the boys and the bucket, "; "She took God's name and the Syrian sailors staring into the brazier, her hand round my thumb." | Yes: no recap-of-items device for a listener's reception |
| G4 | l.16 | Style | "smelled of milk and of the wool… and of something else that was only hers" | stock phrase (#2), a triad | → "and the top of her head, which I put my nose to between paragraphs, smelled of milk and of the wool she had been lying on." | No |
| G5 | l.134, l.182 | Style | "The melon got no mention; whatever there was to say…"; "What a voicemail was, I did not explain." | narrated omissions ×3 (door, melon, voicemail) = nameable; both lines explain what the page shows (#11) | cut both; §6 now ends on "The sheet dried with a pale cloud in that place." | No |
| G6 | l.150 | Voice / Continuity | "*Skip it. Don't explain it to me, I mean it.*"; "*like it's bread, like everybody's got one, like a fellow ought to know*" | rebuilds Ch.25 l.120 "Don't tell me a thing. I mean it." (the dialogue pass's swap moved the echo); anaphora triad | cut "Don't explain it to me, I mean it."; cut "like everybody's got one, " | Yes: a reused frame is a reused line |
| G7 | l.132 | Logic | "*as of this letter that's one person around here who knows it*" | the one who now knows is Mara, not "around here" | → "*and as of this letter that makes two of us who know it.*" | No |
| G8 | l.210 | Style (retired reflex) | "…into the dust. Back in the shop, I gave him the bone." | the bone closes a second section; repeats l.48's "I gave him the knucklebone" | → "I traded him the bone for it, and carried the box through, and slid it under the bedstead, deep, into the dust." | No |
| G9 | l.216 | Character (prop rule) / Style | "with the bone in his fist and dust in his eyebrows and a long gray thread of cobweb…" | business around the rolling: 3 handlings in ~60 words; fifth triad | → "with dust in his eyebrows and a long gray thread of cobweb hanging off his chin, and showed the bone to his father." | No |
| G10 | l.134 | Style | "patch well enough to fool the wine" then l.136 "never learn of the patch" | one conceit twice in ~110 words | → "that I did not think would take a patch." (l.136 keeps the conceit) | No |
| G11 | l.130 | Style | "every customer" (also l.14) | in-chapter echo | → "and customers reached my bench" | No |
| G12 | l.216 | Style | "harness that wanted nothing" (also l.154 "wanted nothing") | in-chapter echo | → "harness with nothing wrong with it." | No |
| G13 | l.250 (+ header l.6) | Style | "holding her very carefully" | 4th book-wide (Ch.17 ×2, Ch.21); the outline's own design words (plan-sentence echo) | → "He sat on in the sun with his lip in her fist and both arms still round her, until his father lifted her away." ("still" keeps the held-past-release) | Yes: outline design phrases never page text |
| G14 | l.116 | Continuity | "five mules" | four crossed (Ch.18/19), no purchase on any page (CH26-2) | → "four mules" | No |
| G15 | l.140, l.182 | Continuity | "a baker's son right over my Secundus"; "Grata's son had been painted out" | campaign painting a year before March AD 77 (CH26-7) | → "*And somebody's painted rooms to let right across the wall by the baths, in red, in letters as high as a child, when every soul in Pompeii knows that wall's my Secundus's.*" / "and Grata's son's wall by the baths was letting rooms." Ch.31's whitewash raid stays unspent; no rival named | No |
| G16–17 | l.66 | Style | "the nail in his fist" | "fist" ×8 in narration | → "the nail still in his hand." (l.154 "hand" in G3) | No |
| G18 | l.20 | Continuity | "the shutter barred on the wind off the bay" | the back room's window is high onto a light-well (Ch.19) | → "the shutter barred on the wind." | No |

### Fix order: Logic/Character (G7, G1, G2, G9) → Continuity (G14, G15, G18) → Connective (G8) → Prose (G3, G4, G5, G6, G10–G13, G16–17).

### TESTED FIX SCRIPT
`/tmp/claude-0/-home-user/63791ee5-159c-5791-9429-07920f8d9417/scratchpad/fixes26/apply_fixes.py <chapter path>` — 27 exact replacements (G1–G18), each verified to match exactly once on md5 `9d42bd0c…`; the script aborts without writing if any does not (a second run aborts, by design). Tested on a scratch copy of the book folder:
- `bash tools/check_chapter.sh 26`: **ALL MECHANICAL GATES CLEAN** (tic gate clean; the first draft of the set tripped "from the first" / "the first line" 3× book-wide and three echoes — all varied before finalising).
- `python3 tools/tic_report.py --echoes 26`: **0** echoes, 0 command, 0 spoken-line.
- shape_check: 5,195 words, 7 breaks, dialogue **12%**, median 15, `narrative` → `quiet` (opening sentence byte-identical; the close keeps its image and length class).
- Every replacement string grepped against Ch.1–25, the at-risk table and the Ch.24/25/26 at-risk blocks; none restores a string the dialogue, disruption or continuity passes cut ("a woman told a dog", "Don't you dare", "nobody … but", "the big fellow", "squinting", "upper shutter" all stay off). The mountain and "Margaret" remain 0.

## Strengths to PRESERVE
- The opening letter's first sentence (l.8) and its ticking line "*She'll be near four the summer we go, by my book*" (l.10), uncommented.
- "The letter was written on the reverse of a stranger's future." and the blot over the son (l.12); the milk on the Walt Whitman Bridge.
- The anchor paragraph l.18 (English aloud, "whether Aelia was somebody").
- The scissors/shears hesitation (l.40) and "nothing whatever about the door".
- The whole 1964 letter (l.60–64), including the turn to the bathhouse pool.
- Valens's sequence l.66–112: "Who's dead?", "All that way with her, and no name.", "It's uphill, that street.", "She sleeps for that." / "She was full last night.", l.104's stopping sentence, "Give me a word of it."
- The dawn "Goodnight." and Grata's answer (l.116–122); "Before him, the only English ever spoken aloud in that street had been mine." (l.124).
- The voicemail memory (l.134), "Marlins." (l.136), the split reed's doubled strokes (l.148), the rage letter's last line, the milk let-down, "My father was not in it anywhere."
- "Put that in." / "I put the ford in." and the sponged half-line's pale cloud (l.180–182).
- The P.S. (l.208); the box shoved under the bed with no reason given.
- The named frame (l.244–250): the held breath, the gust that lifts her hair, "His eyes ran over. I let the shutter go."

## PATH TO 8.5 (Floor 8.0)
- **Characters 8.0 → 8.5 requires:** the census clean and the narrator's two nameable devices gone, with every chaos marker kept inhabited. Surgery: G1 (Aelia's crying 5 → 3; l.22 and l.88 recast so the cry is not re-noted as "roar"), G2 (Aelia asleep 6 → 3 by recasting l.112, l.130, l.136; Valens "low" 3 → 2; the ordinal triad gone), G3 (the baby-reception recap triad out of l.18, 38, 154 and the street recap out of l.126), G5 (the melon and voicemail omission lines cut, so only "nothing whatever about the door" remains as a stated omission and the sponge carries the rest), G9 (the redundant bone handling). Uncapped value is 9.0: Fenn alive on paper, Valens jealous without a word of jealousy, every secondary with an independent moment, Mara 4/4 inhabited.
- **Prose 8.0 → 8.5 requires:** the triad cadence below 1/1k and every reused or slipped line gone, with the stopping sentences untouched. Surgery: G3/G4/G9 (triads 9 → 3), G6 (Fenn's Ch.25 refusal frame and "I mean it" out; the rage's "like" triad to a pair), G7 (the "around here" logic), G10 (one wine conceit), G11/G12 (in-chapter echoes), G13 ("very carefully" out of the close in favour of "both arms still round her"). The stopping sentences (l.104, l.156) and the ugly sentence (l.136) are not touched.

**Projected after G1–G18:** Characters 8.5 (+0.5), Prose 8.5 (+0.5), Immersion 9.0 (G14/G15/G18 secure it) → **Floor 8.5 / Average 8.79 / Casual 9.0 / CVI-Launch 9.4 / CVI-Legacy 7.3.** Cycle 1 should verify the patched page against the census table above with the class rulings unchanged (the census is complete by construction at cycle 0).

## Bookkeeping for finalize (not evaluator edits)
- character-bible: GRATA / SECUNDUS / walk-ons — the l.140 grievance is now a "rooms to let" notice across "the wall by the baths" that Grata calls her son's; **no baker's son, no rival named, no election painting in Ch.26**; Ch.31 owns the campaign and the whitewash, and must not pay off the Ch.26 notice. VALENS — four mules (CH26-2 closed). FENN Ch.26 block — remove "Don't you dare explain it to me" / "Don't explain it to me, I mean it." (both CUT) and "like everybody's got one"; the autumn letter now reads "*that makes two of us who know it*". At-risk after Ch.26 — add CUT (never restore): every G1–G18 old string; add SPENT: "both arms still round her", "rooms to let", "Only the baby woke him", "I traded him the bone for it"; WATCH: "every" (20 in Ch.26), "fist", Aelia's mouthing (3), Valens's looks at people (3), Felix's bursts (2).
- ENTITY_STATE: CH26-2 resolve (four mules); CH26-7 resolve (no election notice in AD 75–76; Secundus first named Ch.26 as the wall's owner in Grata's mouth).
- Header comment l.6 updated by G13; the writer's word count/dialogue figures in l.6 should be refreshed (5,195 / 12%).
- Ch.27 guards stand (no VOICE hook; pull not quiet image; Cumae invitation delivered in Ch.27 itself; the knucklebone's roll avoids rolled / fetched / skittering / flat side / palm).

## VERDICT
**POLISH** — Genesis Floor 8.0 (Characters, Prose) < 8.5; Casual 9.0 ✓; PACING OK ✓; mechanical gates clean ✓. Apply G1–G18 (tested) and re-evaluate.

BIAS CHECK: This evaluation was produced by the same system that wrote the prose. Confidence in scores above 8.0 requires external validation (beta readers, editors, comp analysis).

---

## Re-evaluation — cycle 1
**Evaluator:** book-evaluator (independent) | **Date:** 2026-10-24 | **Cycle:** 1
**Text evaluated:** `manuscript/chapters/chapter-26.md`, md5 `cc88e009985d7392ab6bc98d5de1bac1`. That matches my tested scratch copy (`scratchpad/eval26/manuscript/chapters/chapter-26.md`) byte for byte, so G1–G18 landed exactly as tested. A string-level check of all 27 replacements found every old string OFF the page and every new string ON it (27/27). G13, the closing line, is in as accepted.

**Measured on the real file:** `check_chapter.sh 26` ALL MECHANICAL GATES CLEAN. `tic_report.py --gate` clean (ch 26: and-chains 3/9, credential asides 1/4, negation pivots 0). `--echoes 26` gives 0 echoes, 0 command echoes, 0 spoken-line echoes. Shape: 5,195 words, 7 breaks, dialogue 12%, median 15, `narrative` → `quiet`. SHAPE CLEAN. Metaphor: fig 2.5/1k, 11 similes, 4.1% over 40 words.

### Planted-nothing check
- **Replacement strings checked book-wide.** These occur only in Ch.26: "three nights running", "fought him", "Only the baby", "rooms to let", "letting rooms", "traded him", "nothing wrong with it", "still in his hand", "take a patch", "barred on the wind", "from start to end". These also appear elsewhere, but in unrelated frames: "straight through" (Ch.7 cold through a himation, Ch.18), "two of us" (Ch.15 bed collapse), "both arms" (Ch.7/8/11/12/17; none of them holds an infant, and the Ch.17 "very carefully" is a shave, not a hold). Running `--echoes` came back 0.
- **Cut effects restored or carried.**
  - S3→S4 still cuts on "gave it to her" → "Goodnight." and keeps its force.
  - S6 now closes on "The sheet dried with a pale cloud in that place." That is an image, not a device button. The S6→S7 handoff the hook report praised ("What a voicemail was, I did not explain." → the tables) now runs from the pale cloud to the sacking. It is a withholding into a withholding, so the effect is carried.
  - The melon is now absent from Mara's reply list without being announced, which is stronger. "*that makes two of us who know it*" keeps Fenn's birthday line and fixes the logic.
  - The closing line keeps its image and its quiet length class (24 words). "still" carries the hold past release.
- **Guards held.** The mountain 0, "Margaret" 0, "very carefully" 0, "I mean it" 0. Fenn's promise is unquoted (stays 1 of 3). No Cumae invitation in any letter. *goodnight* appears only in the designed beat (l.112 given, l.118 said). Fenn's l.36 "good night's sleep" predates the beat and is idiom.

### Census re-check (cycle-0 classifications, unchanged; word offsets from l.7)
| Character | State | Cycle 0 | Cycle 1 (lines [offset]) | Verdict |
|---|---|---|---|---|
| Aelia | crying | 5, 3 in ~380 | 3: l.16 [~440] · l.28 [885] · l.38 [1,262] (l.22 "Only the baby woke him" and l.88 "She had fought him" are the G1 recasts, not notes, per the cycle-0 ruling) | **PASS** (two inside 500 at most) |
| Aelia | asleep | 6, 3 in ~210 | 3: l.38 [~1,300] · l.88 [2,302] · l.104 [2,456] (l.112 / l.130 / l.136 recast) | **PASS** |
| Aelia | mouthing | 3 | 3: l.42+46 (one beat) · l.136 · l.232 | OK (WATCH) |
| Aelia | grip | 3 events | 3: l.38 · l.154 "her hand round my thumb" · l.244–250 frame | OK |
| Aelia | lent adult mood | 0 | 0 | OK |
| Valens | speaks low | 3 in ~210 | 2: l.88 · l.112 | **PASS** |
| Valens | asleep / wakes | 3 | 3: l.22 · 158 · 182 | OK |
| Valens | looks at people | 3 | 3: l.104 · 158 · 234 | OK (WATCH) |
| Valens | hands / arm over eyes | varied / 2 | unchanged; l.66 nail now "still in his hand" | OK |
| Lucius | bone business around the rolling | 3 in ~60 | 2: l.216 "showed the bone" · l.226 | **PASS** |
| Felix | bursts / exits | 2 / 1 | 2 / 1 | OK |
| Grata | flood → command, never asks | OK | OK (l.140 recast keeps the syntax) | OK |
| Fenn | tremor / handwriting / Ch.25 spent states | 3 / 2 / 0 | 3 / 2 / 0 | OK |
| Mara | recap triad (baby's reception) | device | gone; l.18 "three nights running", l.38 "straight through to the initials", l.154 a pair | **PASS** |
| Mara | narrated omissions | 3 + 2 kin | 1 (l.40 "nothing whatever about the door") + kin (l.82, l.124) | **PASS** |
| Narration | "fist" | 8 | 5: l.16 · 38 · 232 · 246 · 250 | OK (WATCH: l.232/246/250 in ~270 words; 246/250 are the designed frame) |
| Narration | "every" | 20 | 19 (3.7/1k) | WATCH |

No state crosses its cap, and the gate's gesture layer is clean. **New on re-read, WATCH only (not reclassifications, no fix):**
- "patch" ×5 in ~350 words (l.130–136). It is the object being worked, and G10 removed none and added none.
- The baby's reception is pegged to a point in the letter at l.38, 88 and 154 (3 of 6 letters). Each is worded differently and none is a recap triad now. Ch.27+ should not peg a listener's reception to a read text's content again.
- Fenn's "fellow" ×3 in Ch.26 (l.36 "Mrs. Big Fellow", l.60, l.150) and "okay" ×2 → ≤1 each in Ch.27.

### Nameable-rule test (CP5-0b), on the patched page
- **Mara PASSES.** The recap-triad device and the listed omissions are gone. What remains is one stated omission and acts (the sponge, the box).
- **Fenn PASSES.** Six openers, six different turns. The and-chains are his life. No listing, no numbering. The rage is one rage.
- **Valens PASSES.** No comparison, nobody remarks on it. Jealousy is never named.
- **Grata PASSES.** She floods, commands and never asks.
- **Felix PASSES (WATCH).**
- Aelia's "roar" is now 4 tokens in 3 notes inside ~850 words, all in S1–S2. It no longer reads as the infant's rule, but it is SPENT for her cry from here.

### Closed / spent frames
- Who-pays 0.
- "by degrees" 0.
- Ch.24 birth machinery 0.
- Fenn's Ch.25 narrated states 0.
- "Nobody had [verb]" 1 (l.16).
- "kept … to myself" 0.
- The Ch.25 refusal frame ("Don't … I mean it.") is GONE.
- Anaphora triads 0. G2 removed the ordinal series, and G6 cut the "like" anaphora to a pair.
- Device-as-button: the knucklebone closes §2 only.
- Closing aphorism 0.

### Anti-AI scan (5,195 words), changed rows only
- **#2** Clear (the "only hers" line is cut).
- **#3** 3 polysyndetic noun triads (l.16 body, l.40 four-item reply list, l.130 smells) = 0.58/1k, moderate.
- **#7** 1 minor (l.48).
- **#8** 1 minor (l.48 designed pair).
- **#11** 1 (l.12 "where the wrist had tired") = 0.19/1k, minor.

**Total 4 patterns (#3, #7, #8, #11), commercial CLEAN.** Weighted −0.625, against −1.125 at cycle 0.

### Genesis Score — cycle 1
| Dimension | C0 | C1 | Evidence (patched page) | Cap reasons |
|---|---|---|---|---|
| Originality | 9.0 | **9.0** | Unchanged. The birth arrives secondhand in 1968 English (l.8). The horoscope's reverse serves as stationery (l.12). "*But what in God's name is a voicemail?*" (l.150). The dawn "Goodnight." (l.118). | none |
| Theme | 9.0 | **9.0** | Unchanged: "asleep in a language he did not have" (l.104). "in the language she heard all day from everybody but me at night" (l.126; the street recap is gone, so the line lands cleaner). The box goes under the bed (l.210). | language motif dense in S1–S4 (not 9.5) |
| Characters | 8.0 | **8.5** (+0.5) | Census clean: crying 3, asleep 3, Valens low 2, bone business 2. Both narrator devices are gone (G3, G5). Every chaos marker is still inhabited: "Marlins." (l.136), "whether Aelia was somebody" (l.18), the voicemail memory (l.134), the milk (l.154). Fenn is alive on paper, with "*that makes two of us who know it.*" (l.132) now logical. Valens is jealous without the word. Felix, Grata and Lucius each have an independent moment. | not 9.0: "Only the baby woke him" sits ~50 words from the l.16 roar (accepted under the cycle-0 ruling, but the Critic feels the baby's noise as the S1 constant) |
| Prose & Voice | 8.0 | **8.5** (+0.5) | **Stopping sentences intact:** l.104, l.156 "My father was not in it anywhere." **Underlines:** l.12 (both), l.40 scissors/shears, l.136 the strainer that "never learn[s] of the patch" (now the conceit's only use), l.148 the doubled strokes. **Ugly sentence:** l.136 "Piercing it was dull and slow." **Pressure:** l.154–156. The triad cadence is down to 0.58/1k. The Ch.25 frame, the "around here" slip, the doubled conceit and "very carefully" are all gone. The rage letter (l.150) now runs "*Skip it. I'll find out back there…*" and is better for the cut. | not 9.0: "patch" ×5 in l.130–136; l.182 "Grata's son's wall by the baths was letting rooms" asks a half-beat of the reader |
| Pacing | 8.5 | **8.5** | 5,195 words (87%), serving the beat between 7,343 and 7,600. G4 trimmed S1's lead-in. The speed peaks (S3→S4, the 1964 run) and the slow bench are intact. | S1 lead-in still the soft stretch (not 9.0) |
| Emotion | 9.0 | **9.0** | Anchor l.18. Body rebel l.154. Surprise "Who's dead?" and the dawn "Goodnight." P.S. l.208. The frame l.244–250 is unchanged except the close. | none |
| Immersion | 9.0 | **9.0** | G14 four mules, G15 rooms-to-let notice (Pompeii's signature genre, no anachronistic election), G18 the light-well shutter. Every Hostile continuity slip from cycle 0 is closed. | l.46 newborn "put everything in her mouth" stays INVESTIGATE; the +0.5 per cycle is not needed |
| **FLOOR** | 8.0 | **8.5** | Characters, Prose, Pacing | |
| **AVERAGE** | 8.64 | **8.79** | (9.0+9.0+8.5+8.5+8.5+9.0+9.0)/7 | |

**Casual Reader: 9.0** (unchanged; the cuts are all below a casual reader's notice, and the S1 drift is ~30 words shorter).
**CVI-Launch: 9.4.** Pacing 8, Tomorrow 10, Casual 9, Shareability 7.73, Pitch 10, Closeness 10 = 8.95, plus 0.5 for the strong anchor, gives 9.45 → 9.4.
**CVI-Legacy: 7.3** (unchanged inputs).
**PACING: OK.** Mechanical gates: clean.

**Tomorrow Test:** unchanged. The anchor is the dawn "Goodnight." and Grata's "and to all your mules" (IMAGE), plus "*Nobody said they'd go on making new ones without me.*" (QUOTE). **Bias check:** produced by the same system that wrote the prose; scores above 8.0 need external validation.

### VERDICT — cycle 1: **PASS**
Genesis Floor 8.5 ≥ 8.5; Casual 9.0 ≥ 8.5; PACING OK; gates clean.

### FINALIZE (tested)
`/tmp/claude-0/-home-user/63791ee5-159c-5791-9429-07920f8d9417/scratchpad/fin26/finalize.py <chapter path>` makes 3 replacements, all in the **header comment l.6 only (FN1)**. **Body text is byte-identical** (diffed from l.7). The header was stale on six counts: 5,315 → 5,195; 94% → 87%; dialogue 11% → 12%; median 17 → 15; first sentence 22 → 23 words; close 22 → 24 words; and-chains 2 → 3. It also adds the line "Evaluator cycle 0 fix set G1-G18 applied; cycle 1 PASS (Floor 8.5)". Tested on the scratch copy: applies once, and a second run aborts. `check_chapter.sh 26` ALL CLEAN; `--echoes 26` 0. **Final page md5 `0ba7d411515cf0189ba905963b1681d1`.** No body swap is genuinely needed. "fist" at l.232 and "patch" ×5 are WATCH items, and each swap I tried would plant a fresh repeat ("knuckles" beside the knucklebone, "hand" already ×9).

### Character-bible sync list (FINAL page, md5 `0ba7d411…`) — replaces every "Writer draft 2026-10-24 … downstream passes to re-sync" Ch.26 block
**MARA (card l.779–792), replace the stale parts:**
- She reads the birth letter "three nights running, in the voice I would have used to read out a recipe", and on the third night reads the reverse too, in Greek.
- No recap-of-items device: the reception lines are l.38 "She roared straight through to the initials." and l.154 "She took God's name and the Syrian sailors staring into the brazier, her hand round my thumb."
- ONE stated omission: "nothing whatever about the door" (l.40). The melon line and "What a voicemail was, I did not explain." are CUT. The refusal is the sponge ("The sheet dried with a pale cloud in that place.") and the box: "I traded him the bone for it, and carried the box through, and slid it under the bedstead, deep, into the dust."
- Her replies:
  - The Marlins answer: "The Florida Marlins beat Cleveland in the seventh game, in extra innings … and my father left me the news on my voicemail at work, first thing Monday". Then the weight in Grata's wrist-creases, the rain, and the strainer "that I did not think would take a patch".
  - Second reply: the ford; "The strainer had held … after a fashion"; Lucius on the stair; "Grata's son's wall by the baths was letting rooms"; the sponged *It's a machine that*.
- Credential asides 1. Chaos 4/4 (unchanged). Words escaping her 0. No laugh.

**VALENS (card l.1581–1591):**
- **Four mules** (CH26-2 closed).
- The nail "still in his hand" (l.66).
- "Only the baby woke him; the English never had." (l.22).
- His Latin walking night: "talking to her low in Latin. She had fought him from start to end of it until I came through."
- The word: "He tried it twice, low, eyes on the flame; the word broke in two, and then its pieces ran together. After that he leaned down over Aelia and gave it to her."
- Page lines, verbatim:
  - The letters: "From Puteoli?" / "Who's dead?" / "What side?" / "What was she called?" / "All that way with her, and no name." / "You read it slow."
  - The baby and the word: "She sleeps for that." / "She was full last night." / "She knows it … Grata says they come out knowing the voice they heard inside." / "She hears it now." / "Give me a word of it." / "One she knows." / "Goodnight."
  - The night reply: "Is he sick?" / "With you?" / "Then use the ones he knows." / "Do you tell him about me?" / "What?" / "The ford at Stabiae's up to a mule's belly, and the dun swam the last of it. Put that in."
  - The bone and the frame: "Where did he get that?" / "And you?" / "Is it lucky?" / "He'll drop her." / "He's never held anything that kicks." / "You can move now."
- States: speaks low 2, asleep/wakes 3, looks at people 3 (WATCH ≤2 in Ch.27), arm over eyes 2 (one beat).

**FENN letters (card l.1701–1720), replace the stale quotes:**
- (2): "I sat on the stool and talked American till the gulls started up" (not "at the ceiling").
- (3): "She won't take the trolley home, after. She starts walking." (no "23" in Ch.26).
- (4): "*and as of this letter that makes two of us who know it. I bought myself a melon.*"
- (5): "*Skip it. I'll find out back there same as the rest of them…*" and "*like it's bread, like a fellow ought to know*".
- **Idiom pool, Ch.26 final:** holy cow 1, the whole shebang 1, knock it off 1 (Fenn's only; Ch.8's is Mara's narration), I'll be a monkey's uncle 1, tickled pink 1, so sue me 1, pipe down 1, by my book 1, if you squint 1, believe me 1, kid 1 (noun), okay 2 (book: Fenn 4 across Ch.25–26 → ≤1 per chapter), "figuring" 1 (the one "figure" verb), fellow 3 incl. "Mrs. Big Fellow" (→ ≤1 in Ch.27), Chico Ruiz 1 (2/2 book-wide, SPENT), slowly 0.
- Promise 1 of 3 (unquoted). Tremor 3, handwriting 2, Ch.25 narrated states 0. The rage is the one rage.
- **The voicemail rage is a one-off: never repeated in person, never alluded to by him in Ch.27+.**

**LUCIUS (card l.3007–3016):**
- Bone: given at l.48 ("It was to keep that finger busy that I gave him the knucklebone"; "it rolled, and was fetched, and rolled again"; "since somebody's goat died" is the bone's one section close). Traded back to him for the box lid at l.210. At l.216 he rolls it off his palm on its flat side, and "backed out a while after with dust in his eyebrows and a long gray thread of cobweb hanging off his chin, and showed the bone to his father". "with the bone in his fist" is CUT.
- Frame: "Don't move," in Latin (no "Hold her"). Valens "fitted one of the boy's arms under her head and the other over her middle", then drew his own hands back "barely clear".
- **Close: "He sat on in the sun with his lip in her fist and both arms still round her, until his father lifted her away."** "holding her very carefully" is CUT.

**AELIA (card l.3040–3046), her states on the final page:**
- Crying 3 notes: l.16 "choking and roaring at once … with the roar still in her"; l.28 "roared at the wall until the bakers laughed"; l.38. "roar" ×4 is SPENT for her cry; any later cry finds new words, ≤1.
- Asleep 3: l.38, l.88 at the breast "with a bead of milk standing at the corner of it", l.104.
- Mouthing 3: thread and crescent / hair, beard, blanket, strainer as one beat; "her lips went on sucking at nothing"; "hunting along her own fist for a mouthful". WATCH ≤2 in Ch.27+.
- Grip 3: fist in the neckline, "her hand round my thumb", the lip.
- Awake and roving after the lamp flame (week five); awake in Mara's lap for the rage letter.
- "a warm sack of flour"; head "smelled of milk and of the wool she had been lying on". "something else that was only hers" is CUT.
- Lent moods 0.

**GRATA (card l.2954–2959), replace:**
- "My man reckons it's a curse, what he sends you. He'd call the moon a curse if it rose on a market day." (**"My man" 1**, not 2.)
- The stars "read out to every customer that day" and nailed "with a better nail".
- At the strainer: "Let's have it, he's at my counter now, the fish-sauce man, wanting his cup on credit like a son of mine…" then "**And somebody's painted rooms to let right across the wall by the baths, in red, in letters as high as a child, when every soul in Pompeii knows that wall's my Secundus's.** That one's grown in a week. Look at her wrists. You'd best stop eating standing up."
- Dawn answer, verbatim l.120.
- **SECUNDUS:** first named Ch.26, in Grata's mouth only, as the wall's owner. No election painting, no rival, no baker's son anywhere in Ch.26 (CH26-7 closed). Ch.31 owns the campaign and the whitewash and must NOT pay off the rooms-to-let notice.

**FELIX (card l.2424–2428), replace the stale burst:**
- "From the Chaldean? It's heavy for letters. It's gold, I'd know that weight anywhere." / "The dun threw her head." / "She's been jumpy since the rain. Two boats came round from Surrentum this morning, I watched them in from the wall. Is the sea open, then, or is it only them being stupid? Is it open for good?"
- The cut is "closed and crusted, that was new" (drop "since the Kalends").
- Dawn questions are reported and he exits before an answer (l.122). After the tables: "He was out and away, whistling."
- Bursts 2 (WATCH). No palm scratch (Ch.28).

**Walk-ons (block l.4314):**
- Strike "a baker's son (the rival candidate's name…)". Add "the rooms-to-let notice by the baths (no landlord named)".
- The carter, the bakers opposite (fire the oven, laugh at the roar), the bakers' boys, the fuller's lads, the stationer by the forum, the inn at the crossroads: all functional, no habit.
- The mention lists stand.

**At-risk after Ch.26 — REPLACE the writer-draft block with the FINAL block:**
- **SPENT:**
  - *goodnight* (given l.112, said l.118; never called back in any form, by anyone, ever).
  - Fenn's rage and the voicemail (one-off; never repeated in person).
  - The sponged *It's a machine that* / the pale cloud.
  - The birthday melon; "that makes two of us who know it".
  - Callison's three home runs, the scorecard, the Germantown Avenue walk, the hall-table note ("Home by Labor Day … A line about the milk.").
  - The cedar box under the bedstead (never explain why).
  - The named frame and its close ("both arms still round her").
  - The knucklebone's hand-off and its roll (rolled / fetched / skittering / flat side / palm: Ch.27's Cumae roll uses none).
  - "Sleep when she sleeps."; "a language he did not have"; "My father was not in it anywhere."; "Only the baby woke him"; "rooms to let"; "I traded him the bone for it"; "the wall by the baths" (2, both Ch.26).
  - Aelia's "roar".
- **CUT (never restore), all 27 G1–G18 old strings verbatim:**
  - "Nothing short of the roaring woke him"
  - "She had roared at him from start to end of it"
  - "At his first try the word broke in two. At the second the pieces ran together. On the third … very low. She went on sleeping through it, full of milk, with her fingers spread on my breast."
  - "with Aelia asleep against me in the sling"
  - "Aelia did not wake for the tapping"
  - "three times over, the rope walk and the bridge and the peanuts"
  - "She roared through the broom handle and the tables and both initials."
  - "the loaves and the boys and the bucket"
  - "God's name and the fish and the Syrian sailors"
  - "her fist round my thumb"
  - "something else that was only hers"
  - "The melon got no mention; whatever there was to say about it, the sheet had no room for."
  - "What a voicemail was, I did not explain."
  - "Don't explain it to me, I mean it."
  - "like everybody's got one"
  - "that's one person around here who knows it"
  - "I took the box from him" / "Back in the shop, I gave him the bone."
  - "with the bone in his fist"
  - "patch well enough to fool the wine"
  - "every customer reached my bench"
  - "harness that wanted nothing"
  - "holding her very carefully"
  - "five mules"
  - "a baker's son right over my Secundus … that wall's my boy's"
  - "Grata's son had been painted out by the baths"
  - "the wind off the bay"
  - "the nail in his fist"
  - Plus the earlier passes' cuts, still off the page: "Don't you dare explain it to me", "a woman told a dog", "the big fellow", "squinting", "upper shutter", "nobody … but", "talked American at the ceiling", "nobody here knows it but you now", "Is it from the Chaldean? … is it money", "Hold her", "My man would call the moon". The full verbatim lists are in `dialogue-chapter-26.md`, `disruption-chapter-26.md` and the `continuity/chapter-26-audit.md` repair log.
- **WATCH:**
  - "every" 19 in Ch.26 (3.7/1k).
  - "fist" 5 (narration).
  - "patch" 5.
  - "bed's end" 1 / "bed's head" 1 (the old "2" is stale).
  - Valens's looks at people 3.
  - Aelia's mouthing 3.
  - Felix's bursts 2.
  - Fenn "fellow" 3 / "okay" 2.
  - A listener's reception pegged to a read text's content: 3 (spent as a form).
- **Ch.27 guards:**
  - **(1) The Cumae invitation is delivered IN Ch.27 itself** (outline cascade). It is in no Ch.26 letter, and Ch.27 must not say it came by letter earlier.
  - **(2) Hook must NOT be VOICE; pull must NOT be EMOTIONAL GUT PUNCH** (Ch.26's pair). The ledger's long fade suits QUESTION PLANT or a character-voiced OMINOUS PROMISE.
  - **(3) Nobody names the mountain**, Fenn included (CP5-1).
  - **(4) Fenn's promise phrase stays at 1 of 3.** Quote it at most once, and only if the outline asks.
  - **(5) The voicemail rage is a one-off:** never repeated, reprised or apologised for in person.
  - **(6) "goodnight" is never called back:** not by Valens, Grata, Felix, Mara or Fenn, in any language or form.
  - (7) The Zippo frame is Ch.27's.
  - (8) The automat's lemon meringue needs a non-coin trigger.
  - (9) The knucklebone's roll avoids rolled / fetched / skittering / flat side / palm.
  - (10) No infant lent an adult mood.
  - (11) No "very carefully".
  - (12) Median sentence suits the high gear.

**ENTITY_STATE:** CH26-2 resolved (four mules). CH26-7 resolved (no election notice in AD 75–76; Secundus first named Ch.26 as the wall's owner in Grata's mouth; the wall carries a rooms-to-let notice).
