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
**LOOP RUNNING — resume at Ch.15 "Summer Pasture" (2026-10-20). Ch.14 FINAL.** Ch.15 briefs: ledger row = Chronological day-in-full on the high pasture, `long-spiral` open (dawn in one long sentence), quiet-image close, 7,800w (land it full), dialogue 30–40%, 3 breaks, gear HIGH; HEAT 1 (explicit, earned, character-driven, no purple, no clinical terms, no metaphor-stacking, no temperature report); NON-NEGOTIABLE the truth told badly and "Do they still have mules?" (once, never a refrain), she does NOT tell him Pompeii's fate; hook must NOT be VOICE and pull must NOT be DECISION POINT (Ch.14); CH13-7: Ch.14 ended on her going up to the cave at first light "with Valens and the mules if he would come" — Ch.15 must give that visit real weight (a backfilled scene or a substantial passage in fresh words; a throwaway "it was shut" is a bait-and-switch); CH14-4: her Ch.14 plan to take Euthydikos's bowl job after the season must give way on the page to the bargain (Corinth for his papers in autumn, sail in spring as man and wife); the camera has no lens cap and a dented filter ring; Valens and Felix have seen it (Ch.12); check the flashlight's last state in ENTITY; the ibuprofen is gone; no "kept … eyes on" look, no "had gone quiet", no lying-awake coda, no shard kickers; no bends, kneel/crouch ≤1, hand-on-knee ≤1, deliberation pauses minimal, no gait exit; Valens bare "No." ≤1, no narrated non-answers, no comparisons in his speech. This is the LAST chapter before CHECKPOINT 3 (review-ch11-15.md). Ch.19 writer brief: the Pentax has no lens cap and a dented filter ring.
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

## Chapter log
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
