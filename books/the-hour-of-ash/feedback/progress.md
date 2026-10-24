# Progress — The Hour of Ash (run 2)

## 2026-10-18 — FULL RESTART (author Terry)

The author retired the first run in full (Ch.1–10 finalized on a v3 outline) and asked for:
1. a **complete restart**;
2. a **fully autonomous loop** — write a chapter, run every agent and gate on it, and only
   when it fully passes move to the next, chapter after chapter, until told to stop;
3. a book that is **not predictable** — no three-part skeleton, nothing that reads machine-made.

What was done:
- Folder wiped to canon: manuscript, evaluations, trackers, ENTITY_STATE, stale outlines deleted
  (recoverable at git `2a8db82`). The v3 blueprint is archived under
  `research/prior-run-2026-07/` as reference only.
- `STATE.yaml` rewritten: canon and every author ruling kept; `autonomy: full`; progress reset;
  new guardrails for anti-predictability and the retired pipeline reflexes.
- Pipeline (root, UPDATE RULE): `tools/shape_check.py` (manuscript predictability audit), the
  architect's Anti-Predictability Ledger (book-architect §0.5 Step 5), orchestrator FULL AUTONOMY
  mode + Step D.6 shape audit, docs updated.

## Resume point
**CHECKPOINT 6 — AWAITING AUTHOR REVIEW (2026-10-24).** Ch.1–30 FINAL. The loop has STOPPED: read `feedback/review-ch26-30.md`. `awaiting_author_review: true` in STATE.yaml; LOOP-LOCK deleted; no session (this or the scheduled task) starts Ch.31 until the author says "continue". Pending author decision: the optional Gemini/Grok outside read (suggested Ch.27 + Ch.29). On "continue": set the flag false, record the answer as AUTHOR-CP6-n, and resume at Ch.31 "Election Paint". Ch.31 briefs (carry): the ledger row and outline section; the hook must NOT be IN MEDIAS RES (Ch.30) — the ledger ends on a plain stop (no pull); no "So…" paragraph opener (5 chapters in a row); the bible's At-risk after Ch.30 (WATCH for Ch.31 + Ch.31 guards: Secundus's wall is a rooms-to-let notice; no fullery at the bull's-head crossing — the fullery is the shop's EAST corner, the fountain crossing the WEST) read in full before drafting; Valens now knows which tomb holds the door; `bash tools/check_chapter.sh 31` incl. 5d (28 ledger rows) clean before hand-off; the exhaustive census at cycle 0; four mules; no upper floor; no foreshadowing (a wish about future ground movement never closes a chapter — hook-craft precedent, Ch.30); nobody names the mountain.
author said "Make the fixes then continue". The independent-read fixes are in (Ch.2 asides; Ch.3
trimmed to 5,628; Ch.5 to 7,858 with the town-Greek clause) and Ch.3/Ch.5 re-evaluated PASS. Next
checkpoint after Ch.10 (`feedback/review-ch6-10.md`). Hook/pull types used so far: Ch.1 CONTRAST /
QUESTION-PLANT, Ch.2 VOICE / EMOTIONAL-GUT-PUNCH, Ch.3 SENSORY-IMMERSION / CLIFFHANGER, Ch.4
IN-MEDIAS-RES / REVELATION, Ch.5 QUESTION / DECISION-POINT, Ch.6 IN MEDIAS RES / OMINOUS PROMISE, Ch.7 VOICE / QUESTION PLANT, Ch.8 IN MEDIAS RES / EMOTIONAL GUT PUNCH, Ch.9 CONTRAST / DECISION POINT — no back-to-back repeats (Ch.10's hook must not be CONTRAST; its ending is a ledger PLAIN STOP). Ending signatures so far:
quiet, long-fade, punch, dialogue, long-fade, dialogue, question, quiet. No chapter-end lying awake listening in the dark (SPENT after Ch.5-8). Gear: Ch.1 and Ch.6 were mid rows that landed low (median 11) — Ch.8's writer gets a gear brief. New gates in `tic_report.py
--gate`: and-chains ≤ max(9, words/900), credential asides ≤4, no prop handled 3+ in 400 words.
**Keep Ch.6–8 moving** — Valens arrives in Ch.6, the book's first romance beat. WATCH: the at-risk
list in character-bible.md; `--echoes N` on every fresh draft; Kallia's hands are tasks, never
handling beats; "in English" as a tag ≤2 per chapter.

**RESOLVED AT CHECKPOINT 4 (AUTHOR-CP4-1 = a, leave it):** the children's citizenship. Ch.18's quay marriage is a citizen freedman (Valens) + a woman registered as a peregrine (Mara, "of Syracuse", Kallia's kinswoman) = matrimonium iniustum: valid, but children take the mother's status, so Lucius and Aelia would NOT be Roman citizens by birth. Twist: Syracuse was a Roman colonia (Augustus), so a "Syracusan" could claim citizenship. Ruling: no chapter calls the children citizens and nobody makes a matter of it.

**RULING (orchestrator, 2026-10-21, on the Ch.19 audit's question): "seam".** The outline's Ch.20 mending beat ("learns to let a seam show") and voice-bank sample-11 use "seam" for a visible repair; that is canon and stays. What is reserved for the ending (Ch.42–43) is "seam" used of the DOOR, the tomb or the cold — never describe the door, the tomb or its cold with "seam", "niche", "painted plaster" or "hand flat" before Ch.42.

**PHASE 5 TODO (2026-10-24):** the echo scan became a hard fail in `tools/check_chapter.sh` at Ch.27. Chapters finalized earlier with advisory echoes are listed in `tools/echo_grandfathered.txt` (Ch.2: 11, Ch.3: 23, Ch.4: 9, Ch.5: 6, Ch.21: 54, Ch.22: 93) — vary them in the Phase 5 revision, then empty the file. Also clear the two pre-existing closed-ledger hits that `tools/closed_check.py` (step 5d, added at Ch.28) finds in finalized chapters: "and stayed" in Ch.21 l.42 and Ch.25 l.222 (closed after Ch.15); and the two Ch.25 strings grandfathered when the Ch.29 ledger rows were added: "without a glance" (l.270) and "with great care" (l.200).

## Chapter log
- **Ch.30 "Tremor"** — 2,296w · Floor 8.5 / Avg 8.57 / Casual 9.0 / CVI-L 9.4 · 2 polish cycles (cycle 0: explaining tails, object-first sentences, a rebuilt run, the door warm in sun, the route; cycle 1 the per-cycle cap only) + a continuity repair (3 CRIT / 16 WARN) · the crack, the bread dust and all, "No colder.", Valens reading the name, "I did not wake him." · pacing: a short low-gear hinge between Saturnalia and the comedy, as planned · shape clean · full chain in STATE.yaml history. Same day: author watch beats in Ch.6 and Ch.11 (see evaluations/author-revisions.md).
- **Ch.29 "Saturnalia"** — 6,647w · Floor 8.5 / Avg 8.71 / Casual 9.0 / CVI-L 9.4 · 2 polish cycles (exhaustive census at cycle 0 caught nearly everything: obeyed-order echoes, closed looks and strings, three entity flags; cycle 1 only the swaps' own slips) + a continuity repair (3 CRIT / 16 WARN) · the farce and the roll, the olive-pit diamond, the bad song, Cerdo's jug and the cup · pacing: argument brisk, table warm and slow, nothing erupts · shape clean · full chain in STATE.yaml history.
- **Ch.28 "Felix in the Arena"** — 6,481w · Floor 8.5 / Avg 8.71 / Casual 9.0 / CVI-L 9.4 · 4 polish cycles (reused lines + census; then a Ch.20 gossip chain and swap-made doubles; then the bible's lexical caps; then the SPENT/CLOSED ledger in full) + a continuity repair (7 CRIT / 18 WARN) · the thraex, the unfinished palm, the one man sitting, "You were sitting down." · pacing: the bout held off ~68% by design, then fast · shape clean · full chain in STATE.yaml history.
- **Ch.27 "Cumae"** — 7,472w · Floor 8.5 / Avg 8.79 / Casual 9.0 / CVI-L 9.4 · 4 polish cycles (83 echoes; then Fenn's doubled words; then a full speech-habit census; then habits the cycle-2 swaps left) + a continuity repair (6 CRIT / 15 WARN) · the dead door, Fenn young in the cave, the diamond in the dust, "Just that it's cold." · pacing: a slow walk, still in the cave, as planned · shape clean · full chain in STATE.yaml history.
- **Ch.26 "Letters in English"** — 5,195w · Floor 8.5 / Avg 8.79 / Casual 9.0 / CVI-L 9.4 · 1 polish cycle (exhaustive census at cycle 0 caught everything at once: Aelia's states, narrator triads, a Ch.25 frame) + a continuity repair (6 CRIT / 19 WARN, incl. an upper floor the house does not have) · six letters; Aelia; the box unopened; "goodnight"; the photograph · pacing: a quiet collage between two 7,000+ chapters, letters brisk and the house slow · shape clean · full chain in STATE.yaml history.
- **Ch.25 "Augurinus"** — 7,342w · Floor 8.5 / Avg 8.79 / Casual 9.0 / CVI-L 9.8 · 4 polish cycles (Characters: narrated states, found in full only at cycle 3 — pipeline now censuses exhaustively at cycle 0) + a continuity repair (7 CRIT / 19 WARN) · the WHEN: Fenn in English, Valens believes, "Late summer, seventy-nine", the refusal · pacing: quick recognition, slow story, very fast date, a dead stop · shape clean · full chain in STATE.yaml history.
- **Ch.24 "Lucius"** — 5,707w · Floor 8.5 / Avg 8.71 / Casual 9.0 / CVI-L 9.3 · 1 polish cycle (closed frames, a spent laugh shape, Statia's refrain) + a continuity repair (6 CRIT / 15 WARN, incl. "Vesuvius" removed from the page) · the birth in nine night-hour shards; the teeth; the hooves at midnight; the jar caught short of the stones; the watch wound · pacing: fast shards, slow at the birth, still at the watch, as planned · shape clean · full chain in STATE.yaml history.
- **Ch.23 "An Inn on the Appian Way"** — 3,385w · Floor 8.5 / Avg 8.71 / Casual 9.0 / CVI-L 9.4 · 2 polish cycles (Characters: narrated states; Prose: explanation density, HEAT 1 lines rebuilt; then the eel logic and an until-chain) + a continuity repair (5 CRIT / 19 WARN) · HEAT 2: he is the one held; the five words; the onion with his mother; the kick against the scars · pacing: a deliberate quiet stretch between the court and the birth, short by design · shape clean · full chain in STATE.yaml history.
- **Ch.22 "The Basilica Julia"** — 7,177w · Floor 8.5 / Avg 8.79 / Casual 9.0 / CVI-L 9.6 · 3 polish cycles (Characters: narrated-trait tics — the iudex's shut eyes, Myrrhine barefoot, Valens waiting, Plautia's stillness; then the who-pays frame) + a continuity repair (4 CRIT / 14 WARN) · the TURNING POINT: Valens's name to the back benches, the sneeze, the laugh, the verdict under the next court's applause, Marcus on the steps · pacing: high gear after Ch.21's low, the court deliberate and the city wandering, as planned · shape clean · full chain in STATE.yaml history.
- **Ch.21 "The Wolf's Old Name"** — 6,800w · Floor 8.5 / Avg 8.57 / Casual 9.0 / CVI-L 9.5 · 1 polish cycle (Prose: Ch.22's laugh pre-spent, Ch.18's entrance rebuilt, spent channels) + a continuity repair (4 CRIT / 19 WARN) · the child told first; the summons by the board; Nicanor and the raised hand; the flat No; Felix's palm · pacing: brisk after two long chapters, low gear serves it · shape clean · full chain in STATE.yaml history.
- **Ch.20 "The Mender's Shop"** — 7,792w · Floor 8.5 / Avg 8.79 / Casual 9.0 / CVI-L 9.4 · 1 polish cycle (Prose: retired devices, Ch.14 rebuild, sample-07 echoes) + a continuity repair (3 CRIT / 15 WARN) · a year in Pompeii; the lamp; the pebble; Grata guesses the child · full chain in STATE.yaml history.
- **Ch.19 "Puteoli"** — 8,251w · Floor 8.5 / Avg 8.79 / Casual 8.5 / CVI-L 8.85 · 1 polish cycle (Prose: door explanation, pause device, Ch.17 frames) + a continuity repair (0 CRIT / 15 WARN) · the bay, the mountain declined, Grata, the door found · full chain in STATE.yaml history.
- **Ch.18 "Lechaion"** — 2,523w · Floor 8.5 / Avg 8.93 / Casual 9.0 / CVI-L 10.0 · 1 polish cycle (Prose: a reserved sample frame, present-tense similes) + a continuity repair (0 CRIT / 14 WARN) · the quay wedding in ten words; the watch handed back · full chain in STATE.yaml history.
- **Ch.17 "Games on the Isthmus"** — 6,909w · Floor 8.5 / Avg 8.86 / Casual 9.0 / CVI-L 9.7 · 1 polish cycle (Prose: lifts and rebuilt set pieces) + a continuity repair (1 CRIT / 10 WARN) · the theft by boredom; Celer at the scaffold's shadow; the run · full chain in STATE.yaml history.
- **Ch.16 "Plautia"** — 7,175w · Floor 8.5 / Avg 8.86 / Casual 9.0 / CVI-L 9.7 · 1 polish cycle (Prose: earlier delivery frame rebuilt, borrowed whole lines, retired pause-fillers) + a continuity repair (3 CRIT / 14 WARN; the Isthmia year → CP3-5) · Plautia, the bracelet, Kallia's quiet farewell, the plan · full chain in STATE.yaml history.
- **Ch.15 "Summer Pasture"** — 7,479w · Floor 8.5 / Avg 8.86 / Casual 9.0 / CVI-L 9.8 / Emotion 9.0 · 1 polish cycle (Prose: the cave in Ch.3's words, spent frames, Valens's register) + a continuity repair (0 CRIT / 12 WARN) · the truth, the mules, the bargain, the hut · full chain in STATE.yaml history.
- **Ch.14 "What Pompeii Means"** — 3,003w · Floor 8.5 / Avg 8.86 / Casual 9.0 / CVI-L 8.9 / Emotion 9.0 · 1 polish cycle (Prose: explanation, spent frames, shard kickers) + a continuity repair (1 CRIT moon / 13 WARN) · the night she knows; the laugh; the plan · full chain in STATE.yaml history.
- **Ch.13 "The Seventh of Bysios"** — 7,503w · Floor 8.5 / Avg 8.79 / Casual 9.0 / CVI-L 9.8 / Emotion 9.0 · 1 polish cycle (Characters: pause beats; Prose: explanation clauses) + a continuity repair (1 CRIT / 20 WARN) · the consultation; Valens recites the answer; Theano says "Pompeii." · full chain in STATE.yaml history.
- **Ch.12 "The Kirrha Road"** — 4,711w · Floor 8.5 / Avg 8.71 / Casual 9.0 / CVI-L 9.7 / Emotion 9.0 · 1 polish cycle (Prose: explanation density + reused frames) + a continuity repair (1 CRIT / 23 WARN) · the ambush; Valens kills a man; he shakes, she holds steady · full chain in STATE.yaml history.
- **Ch.11 "Valens's Yard"** — 5,910w · Floor 8.5 / Avg 8.64 / Casual 9.0 / CVI-L 9.5 / Emotion 9.0 · 1 polish cycle + a continuity repair (1 CRIT / 14 WARN) · the full two-hander; the near-kiss; he agrees to carry her question · full chain in STATE.yaml history.
- **Ch.10 "Kallia's Letter"** — 2,446w · Floor 8.5 / Avg 8.57 / Casual 8.5 / CVI-L 9.3 / Emotion 9.0 · 2 polish cycles + a continuity repair (1 CRIT / 9 WARN) · the letter; "Ariston's room, at the three obols"; plain stop · full chain in STATE.yaml history.
- **Ch.9 "The Polygonal Wall"** — 5,763w · Floor 8.5 / Avg 8.64 / Casual 9.0 / CVI-L 9.1 / Emotion 9.0 · 2 polish cycles (Prose: narrator moves; then a bending cluster the first cycle made) + a continuity repair (1 CRIT / 11 WARN) · the notice; Valens reads it in silence · full chain in STATE.yaml history.
- **Ch.8 "The Thyiades"** — ~7,470w · Floor 8.5 / Avg 8.64 / Casual 9.0 / CVI-L 9.8 / Emotion 9.0 · 1 polish cycle (Prose: eleven narrator recurrences) + a continuity repair (20 WARN) · the rite, the shut cave, the heap · full chain in STATE.yaml history.
- **Ch.7 "The Laws of Belonging"** — 6,122w · Floor 8.5 / Avg 8.64 / Casual 8.5 / CVI-L 9.3 / Emotion 9.0 · 1 polish cycle (Prose: narrator moves) + a continuity repair (2 CRIT / 20 WARN) · the registration as Kallia's free kinswoman · full chain in STATE.yaml history.
- **Ch.6 "Snow at the Cave Mouth"** — 6,639w · Floor 8.5 / Avg 8.57 / Casual 9.0 / CVI-L 9.4 / Emotion 9.0 · 1 polish cycle (Prose: nine narrator-law items) + a continuity repair (1 CRIT / 19 WARN) · Valens's first appearance · full chain in STATE.yaml history.
- **Author fixes (checkpoint 1, 2026-10-19)** — Ch.2 asides 8→3; Ch.3 6,837→5,628 (chains 21→6, asides 4) re-eval PASS Floor 8.5 / Casual 9.0; Ch.5 8,184→7,858 (chains 7, asides 4, town-Greek clause) re-eval PASS Floor 8.5 / Casual 8.5.
- **Ch.1 "The Reception"** — 6,546w · Floor 8.5 / Avg 8.57 / Casual 8.5 / CVI-L 9.0 · 2 polish cycles
  (Prose was the holdout: chain sentences and an inventory form that was a tic forming) · entity +
  continuity audit per chapter clean · full chain in STATE.yaml history. Re-opened later the same day
  for two subtractive gesture trims (object handling 9 → 4) when the gesture layer went live; 6,503w.
- **Ch.5 "The Sanctuary"** — 8,184w · Floor 8.5 / Avg 8.57 / Casual 8.5 / CVI-L 8.7 / Immersion 9.0 · 1 polish
  cycle (Prose: nine cross-chapter repeats; one critical third-use; 17 audit warnings) · full chain in
  STATE.yaml history.
- **Ch.4 "The Goats Saw Me First"** — ~1,825w · Floor 8.5 / Avg 8.50 / Casual 8.5 / CVI-L 8.9 · 1 polish
  cycle (Prose: five cross-chapter repeats; two critical third-uses of capped shapes) · first full shape
  audit clean in strict mode · full chain in STATE.yaml history.
- **Ch.3 "Parnassus"** — 6,837w · Floor 8.5 / Avg 8.57 / Casual 8.5 / CVI-L 8.7 · 1 polish cycle (Prose: five
  book-law repeats; plus three real continuity errors fixed) · the goatherd-phone pattern-tic caught and
  replaced · full chain in STATE.yaml history.
- **Ch.2 "Fenn's Notebook"** — 4,101w · Floor 8.5 / Avg 8.57 / Casual 8.5 / CVI-L 8.8 · 1 polish cycle
  (Prose: counter tears repeating Ch.1, "without" ×4, a handling-beat cluster in the packing stretch) ·
  13 audit warnings all fixed · full chain in STATE.yaml history.

## Pacing log
- Ch.30 (FINAL): PASS — 2,296w (target 2,600, no floor) · dialogue 11% (5–15 ✓) · 6 breaks · gear low (median 11) · fast shards, still at the door, quick walk home, a dead stop; Ch.31 is comedy, 40–55% dialogue.
- Ch.29 (FINAL): PASS — 6,647w (target 6,600) · dialogue 38% (35–45 ✓) · 3 breaks · gear high (median 19) · the street brisk, the farce quick, the table long and warm by design; Ch.30 drops to a short low-gear fragmented morning.
- Ch.28 (FINAL): PASS — 6,481w (target ~6,600) · dialogue 31% (25–35 ✓) · 4 breaks · gear low (median 11) · news-driven backfill brisk, the bout held off ~4,500w by the ledger's shape, then fast; Ch.29 opens on a claim.
- Ch.20 (FINAL): PASS — 7,792w (target 8,200) · dialogue 35% (30–40 ✓) · 6 breaks · gear mid (median 16) · documents quick, repairs slow, the fountain sudden; Ch.21 must open fast.
- Ch.19 (FINAL): PASS — 8,251w (target 8,400) · dialogue 25% (20–30 ✓) · 4 breaks · gear high (median 18) · slow panoramic arrival; the road stretch sags by design; very slow at the tomb.
- Ch.18 (FINAL): PASS — 2,523w (target 2,800) · dialogue 34% (30–40 ✓) · 0 breaks · gear mid (median 15) · a short quick hinge between the long chase and the long arrival.
- Ch.17 (FINAL): PASS — 6,909w (target 7,400) · dialogue 33% (30–40 ✓) · 3 breaks · gear low (median 12) · fast and fragmented with one slow beat at the scaffold; the gear steps down across Ch.15–17 as planned.
- Ch.16 (FINAL): PASS — 7,175w (target 7,600) · dialogue 46% (40–50 ✓) · 6 breaks · gear mid (median 14) · Corinth quick and talky against Delphi slow and silent; the parallel never rhymes mechanically.
- Ch.15 (FINAL): PASS — 7,479w (target 7,800) · dialogue 34.5% (30–40 ✓) · 3 breaks · gear high (median 16) · a long talky day after the short night; ~600w of backfill at dawn earns its place.
- Ch.14 (FINAL): PASS — 3,003w (target 3,400; no padding) · dialogue 5% (0–10 ✓) · 9 breaks · gear low (median 12) · a short private pressure chapter between the long consultation and the long pasture day.
- Ch.13 (FINAL): PASS — 7,503w (target 8,000) · dialogue 38% (35–45 ✓) · 4 breaks · gear mid (median 14) · Parallel structure: terrace wait against the court telling; the recitation is the peak, "Pompeii." lands flat.
- Ch.12 (FINAL): PASS — 4,711w (target 5,600; no per-chapter floor, not padded) · dialogue 28% (25–35 ✓) · 2 breaks · gear low (median 10) · fast fight, slow stream, the telling flat and unhurried; first crisis lands after the Ch.11 two-hander.
- Ch.11 (FINAL): PASS — 5,910w (target 6,200) · dialogue 38% (35–45 ✓) · 3 breaks · gear mid (median 14) · unhurried working rhythm; reveals land unevenly; the plot moves (carrier, sponsor, goat, question).
- Ch.10 (FINAL): PASS — 2,446w (target 2,800; no per-chapter floor) · dialogue 40% (30–40 ✓) · 0 breaks · gear mid (median 15) · slow, held, one room; the plain stop is plain.
- Ch.9 (FINAL): PASS — 5,763w (target 6,400; no per-chapter floor; do not pad) · dialogue 28% (25–35 ✓) · 5 breaks · gear mid (median 15) · documents brisk, mending slow, the square sudden, as planned.
- Ch.8 (FINAL): PASS — ~7,470w (target 8,200; no per-chapter floor; book projects ~246k vs 245k target, so no padding) · dialogue 28% (25–35 ✓) · 0 breaks · gear mid (median 15) · rite fast, cave slow, heap very slow as planned · forward pull (the Oracle's price) at ~60% by design.
- Ch.7 (FINAL): PASS — 6,122w (target 6,600, in range) · dialogue 22% (20–30 ✓) · 3 breaks · gear high (median 17) · essayistic without lecture: every claim paid off in a scene; the cost now shown (storeroom) not summarised · relief lands on the step.
- Ch.6 (FINAL): PASS — 6,639w (target 7,200, in range) · dialogue 38% (35–45 ✓) · 2 breaks (sections ~800 / ~4,000 / ~1,800) · fast open, measured backfill, short hard break at the wall, slow descent, as planned · gear median 11–12 vs mid accepted · first two-hander lands without romance signals in narration.
- Ch.5 (FINAL): PASS — decelerates on the Sacred Way, accelerates on the steps and the beating, slow storeroom fade, as planned; dialogue 20.4% at the bottom of the band (narration-heavy by design: a woman who cannot speak); 8,184w vs 8,300; slot: hunger → disappointment/shame → pain → date-shock → shelter; sags noted but accepted: the monument roll-call, the fountain men (now pays off).
- Ch.4 (FINAL): PASS — fast throughout; the 6,817 → 1,876 collapse is the structural shock the ledger asked for, and the evaluator confirms it lands rather than thins; dialogue 16% in band; theme recedes cleanly (body and survival only); ends on his word, nothing after.
- Ch.3 (FINAL): PASS — slow sensory climb → one held sentence at the threshold → fast short sentences outside, as planned; curiosity → cold → embarrassment; dialogue 5.8% in the 5–15% band; 6,837w vs 6,800; single unbroken scene after Ch.2's six-break collage; the modern frame closes on a 5-word cliffhanger.
- Ch.2 (FINAL): PASS — brisk documents / slow textural days / quick packing as planned; curiosity rising after the grief-low with one laugh (kept a crack, not a collapse); dialogue 14.7% in the 10–20% band; 4,101w vs 4,200; the italic blocks land unpredictably; document-fragment close with nothing after it.
- Ch.1 (FINAL): PASS — fast reception → slow shop → very slow at the machine, as planned; grief-low slot without melancholy (irritation surprise lands); dialogue 32% in band; 6,546w vs 6,800 target after the trim that fixed pages 2–3; quiet close, pull carried by the unread notebook.

## Shape audits
(every chapter: `python3 tools/shape_check.py books/the-hour-of-ash` from the repo root)
- after Ch.20 (--strict): CLEAN. Ch.20 `narrative` / `dialogue`; 6 breaks; dialogue 35%; median 16. Twenty chapters: lengths 1,821–8,251, dialogue 5–46%.
- after Ch.19 (--strict): CLEAN. Ch.19 `scene-set` / `long-fade`; 4 breaks; dialogue 25%; median 18.
- after Ch.18 (--strict): CLEAN. Ch.18 `I-statement` / `punch`; 0 breaks; dialogue 34%; median 15.
- after Ch.17 (--strict): CLEAN. Ch.17 `short-punch` / `quiet`; 3 breaks; dialogue 33%; median 12.
- after Ch.16 (--strict): CLEAN. Ch.16 `dialogue` / `question`; 6 breaks; dialogue 46%; median 14.
- after Ch.15 (--strict): CLEAN. Ch.15 `long-spiral` / `quiet`; 3 breaks; dialogue 35%; median 16. Fifteen chapters: lengths 1,821–7,833, dialogue 5–40%, no signature more than four times.
- after Ch.14 (--strict): CLEAN. Ch.14 `I-punch` / `long-fade`; 9 breaks; dialogue 5%; median 12.
- after Ch.13 (--strict): CLEAN. Ch.13 `scene-set` / `dialogue`; 4 breaks; dialogue 38%; median 14.
- after Ch.12 (--strict): CLEAN. Ch.12 `dialogue` / `punch`; 2 breaks; dialogue 28%; median 10.
- after Ch.11 (--strict): CLEAN. Ch.11 `long-spiral` / `dialogue`; 3 breaks; dialogue 38%; median 14.
- after Ch.10 (--strict): CLEAN. Ch.10 `short-punch` / `quiet`; 0 breaks; dialogue 40%; median 15. Ten chapters: lengths 1,821–7,843, dialogue 6–40%, no signature used more than three times.
- after Ch.9 (--strict): CLEAN. Ch.9 `narrative` / `punch`; 5 breaks; dialogue 28%; median 15.
- after Ch.8 (--strict): CLEAN. Ch.8 `dialogue` / `quiet`; 0 breaks; dialogue 28%; median 15.
- after Ch.7 (--strict): CLEAN. Ch.7 `narrative` / `question`; 6,122w; dialogue 22%; 3 breaks; median 17.
- after Ch.6 (--strict): CLEAN. Openings I-statement / narrative / long-spiral / short-punch / scene-set / I-statement; endings quiet / long-fade / punch / dialogue / long-fade / dialogue; lengths 6,466 / 4,048 / 5,617 / 1,821 / 7,844 / 6,639; dialogue 31 / 15 / 6 / 17 / 20 / 38%; breaks 3 / 6 / 0 / 7 / 4 / 2; median sentence 11 / 16 / 17 / 10 / 17 / 11.
- after Ch.1: n/a (needs 4 chapters); Ch.1 signatures `I-statement` / `quiet`.
- after Ch.2: n/a (needs 4); Ch.2 `narrative` / `long-fade`; lengths 6,503 / 4,101; dialogue 31% / 15%; breaks 3 / 6.
- after Ch.3: n/a (needs 4); Ch.3 `long-spiral` / `punch`; 6,837w; dialogue 6%; 0 breaks; median sentence 18 (gear high). First full audit fires after Ch.4.
- after Ch.5 (--strict): CLEAN. Five different openings; endings quiet / long-fade / punch / dialogue / long-fade; lengths 6,473 / 4,069 / 6,817 / 1,821 / 8,184 (CV 0.42, max÷min 4.5); dialogue 31 / 15 / 6 / 17 / 20%; breaks 3 / 6 / 0 / 7 / 4; median sentence 11 / 16 / 18 / 10 / 17.
- after Ch.4 (FIRST FULL AUDIT, --strict): CLEAN. Openings I-statement / narrative / long-spiral / short-punch; endings quiet / long-fade / punch / dialogue; lengths 6,473 / 4,069 / 6,817 / 1,876 (CV 0.42, max÷min 3.6); dialogue 31 / 15 / 6 / 18%; breaks 3 / 6 / 0 / 7; median sentence 11 / 16 / 18 / 9.
