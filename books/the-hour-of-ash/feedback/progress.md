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
**Ch.1–3 FINAL (2026-10-18).** Next: **Ch.4 "The Goats Saw Me First"** — read its ledger row and section
in outline.md (AD 70, the plateau changed; the goat-boy is a different person from the 1998 goatherd).
Hook/pull types used so far: Ch.1 CONTRAST / QUESTION-PLANT, Ch.2 VOICE / EMOTIONAL-GUT-PUNCH, Ch.3
SENSORY-IMMERSION / CLIFFHANGER — do not repeat any. WATCH: the GESTURE layer of the tic gate is live (3+ of one
stage-business class within 500 words, or over the chapter cap, fails) — in a chapter of walking and
climbing, vary the body's business; "somebody/nobody" and "X, or Y" hedges are near their book-wide
limits already; the at-risk list in character-bible.md. The blueprint, entity state and bible are current.

## Chapter log
- **Ch.1 "The Reception"** — 6,546w · Floor 8.5 / Avg 8.57 / Casual 8.5 / CVI-L 9.0 · 2 polish cycles
  (Prose was the holdout: chain sentences and an inventory form that was a tic forming) · entity +
  continuity audit per chapter clean · full chain in STATE.yaml history. Re-opened later the same day
  for two subtractive gesture trims (object handling 9 → 4) when the gesture layer went live; 6,503w.
- **Ch.3 "Parnassus"** — 6,837w · Floor 8.5 / Avg 8.57 / Casual 8.5 / CVI-L 8.7 · 1 polish cycle (Prose: five
  book-law repeats; plus three real continuity errors fixed) · the goatherd-phone pattern-tic caught and
  replaced · full chain in STATE.yaml history.
- **Ch.2 "Fenn's Notebook"** — 4,101w · Floor 8.5 / Avg 8.57 / Casual 8.5 / CVI-L 8.8 · 1 polish cycle
  (Prose: counter tears repeating Ch.1, "without" ×4, a handling-beat cluster in the packing stretch) ·
  13 audit warnings all fixed · full chain in STATE.yaml history.

## Pacing log
- Ch.3 (FINAL): PASS — slow sensory climb → one held sentence at the threshold → fast short sentences outside, as planned; curiosity → cold → embarrassment; dialogue 5.8% in the 5–15% band; 6,837w vs 6,800; single unbroken scene after Ch.2's six-break collage; the modern frame closes on a 5-word cliffhanger.
- Ch.2 (FINAL): PASS — brisk documents / slow textural days / quick packing as planned; curiosity rising after the grief-low with one laugh (kept a crack, not a collapse); dialogue 14.7% in the 10–20% band; 4,101w vs 4,200; the italic blocks land unpredictably; document-fragment close with nothing after it.
- Ch.1 (FINAL): PASS — fast reception → slow shop → very slow at the machine, as planned; grief-low slot without melancholy (irritation surprise lands); dialogue 32% in band; 6,546w vs 6,800 target after the trim that fixed pages 2–3; quiet close, pull carried by the unread notebook.

## Shape audits
(every chapter: `python3 tools/shape_check.py books/the-hour-of-ash` from the repo root)
- after Ch.1: n/a (needs 4 chapters); Ch.1 signatures `I-statement` / `quiet`.
- after Ch.2: n/a (needs 4); Ch.2 `narrative` / `long-fade`; lengths 6,503 / 4,101; dialogue 31% / 15%; breaks 3 / 6.
- after Ch.3: n/a (needs 4); Ch.3 `long-spiral` / `punch`; 6,837w; dialogue 6%; 0 breaks; median sentence 18 (gear high). First full audit fires after Ch.4.
