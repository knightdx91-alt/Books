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
**LOOP RUNNING — resume at Ch.8 "The Thyiades" (2026-10-19). Ch.7 FINAL.** Checkpoint 1 reviewed; the
author said "Make the fixes then continue". The independent-read fixes are in (Ch.2 asides; Ch.3
trimmed to 5,628; Ch.5 to 7,858 with the town-Greek clause) and Ch.3/Ch.5 re-evaluated PASS. Next
checkpoint after Ch.10 (`feedback/review-ch6-10.md`). Hook/pull types used so far: Ch.1 CONTRAST /
QUESTION-PLANT, Ch.2 VOICE / EMOTIONAL-GUT-PUNCH, Ch.3 SENSORY-IMMERSION / CLIFFHANGER, Ch.4
IN-MEDIAS-RES / REVELATION, Ch.5 QUESTION / DECISION-POINT, Ch.6 IN MEDIAS RES / OMINOUS PROMISE, Ch.7 VOICE / QUESTION PLANT — from here only no back-to-back repeats (Ch.8 must not use a VOICE hook or a QUESTION PLANT pull; TICKING CLOCK is the one hook type never used). Ending signatures so far:
quiet, long-fade, punch, dialogue, long-fade, dialogue, question. Gear: Ch.1 and Ch.6 were mid rows that landed low (median 11) — Ch.8's writer gets a gear brief. New gates in `tic_report.py
--gate`: and-chains ≤ max(9, words/900), credential asides ≤4, no prop handled 3+ in 400 words.
**Keep Ch.6–8 moving** — Valens arrives in Ch.6, the book's first romance beat. WATCH: the at-risk
list in character-bible.md; `--echoes N` on every fresh draft; Kallia's hands are tasks, never
handling beats; "in English" as a tag ≤2 per chapter.

## Chapter log
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
- Ch.7 (FINAL): PASS — 6,122w (target 6,600, in range) · dialogue 22% (20–30 ✓) · 3 breaks · gear high (median 17) · essayistic without lecture: every claim paid off in a scene; the cost now shown (storeroom) not summarised · relief lands on the step.
- Ch.6 (FINAL): PASS — 6,639w (target 7,200, in range) · dialogue 38% (35–45 ✓) · 2 breaks (sections ~800 / ~4,000 / ~1,800) · fast open, measured backfill, short hard break at the wall, slow descent, as planned · gear median 11–12 vs mid accepted · first two-hander lands without romance signals in narration.
- Ch.5 (FINAL): PASS — decelerates on the Sacred Way, accelerates on the steps and the beating, slow storeroom fade, as planned; dialogue 20.4% at the bottom of the band (narration-heavy by design: a woman who cannot speak); 8,184w vs 8,300; slot: hunger → disappointment/shame → pain → date-shock → shelter; sags noted but accepted: the monument roll-call, the fountain men (now pays off).
- Ch.4 (FINAL): PASS — fast throughout; the 6,817 → 1,876 collapse is the structural shock the ledger asked for, and the evaluator confirms it lands rather than thins; dialogue 16% in band; theme recedes cleanly (body and survival only); ends on his word, nothing after.
- Ch.3 (FINAL): PASS — slow sensory climb → one held sentence at the threshold → fast short sentences outside, as planned; curiosity → cold → embarrassment; dialogue 5.8% in the 5–15% band; 6,837w vs 6,800; single unbroken scene after Ch.2's six-break collage; the modern frame closes on a 5-word cliffhanger.
- Ch.2 (FINAL): PASS — brisk documents / slow textural days / quick packing as planned; curiosity rising after the grief-low with one laugh (kept a crack, not a collapse); dialogue 14.7% in the 10–20% band; 4,101w vs 4,200; the italic blocks land unpredictably; document-fragment close with nothing after it.
- Ch.1 (FINAL): PASS — fast reception → slow shop → very slow at the machine, as planned; grief-low slot without melancholy (irritation surprise lands); dialogue 32% in band; 6,546w vs 6,800 target after the trim that fixed pages 2–3; quiet close, pull carried by the unread notebook.

## Shape audits
(every chapter: `python3 tools/shape_check.py books/the-hour-of-ash` from the repo root)
- after Ch.7 (--strict): CLEAN. Ch.7 `narrative` / `question`; 6,122w; dialogue 22%; 3 breaks; median 17.
- after Ch.6 (--strict): CLEAN. Openings I-statement / narrative / long-spiral / short-punch / scene-set / I-statement; endings quiet / long-fade / punch / dialogue / long-fade / dialogue; lengths 6,466 / 4,048 / 5,617 / 1,821 / 7,844 / 6,639; dialogue 31 / 15 / 6 / 17 / 20 / 38%; breaks 3 / 6 / 0 / 7 / 4 / 2; median sentence 11 / 16 / 17 / 10 / 17 / 11.
- after Ch.1: n/a (needs 4 chapters); Ch.1 signatures `I-statement` / `quiet`.
- after Ch.2: n/a (needs 4); Ch.2 `narrative` / `long-fade`; lengths 6,503 / 4,101; dialogue 31% / 15%; breaks 3 / 6.
- after Ch.3: n/a (needs 4); Ch.3 `long-spiral` / `punch`; 6,837w; dialogue 6%; 0 breaks; median sentence 18 (gear high). First full audit fires after Ch.4.
- after Ch.5 (--strict): CLEAN. Five different openings; endings quiet / long-fade / punch / dialogue / long-fade; lengths 6,473 / 4,069 / 6,817 / 1,821 / 8,184 (CV 0.42, max÷min 4.5); dialogue 31 / 15 / 6 / 17 / 20%; breaks 3 / 6 / 0 / 7 / 4; median sentence 11 / 16 / 18 / 10 / 17.
- after Ch.4 (FIRST FULL AUDIT, --strict): CLEAN. Openings I-statement / narrative / long-spiral / short-punch; endings quiet / long-fade / punch / dialogue; lengths 6,473 / 4,069 / 6,817 / 1,876 (CV 0.42, max÷min 3.6); dialogue 31 / 15 / 6 / 18%; breaks 3 / 6 / 0 / 7; median sentence 11 / 16 / 18 / 9.
