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
Architect v4 pass (foundation + outline, then voice mode) → entity BUILD → outline audit →
chapter loop from Ch.1. Each finished chapter is committed and pushed to `main`.

## Pacing log
(one line per finalized chapter)

## Shape audits
(every 5 chapters: `python3 tools/shape_check.py books/the-hour-of-ash` from the repo root)
