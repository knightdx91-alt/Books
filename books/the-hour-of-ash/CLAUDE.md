# CLAUDE.md — The Hour of Ash

Per-book playbook. A fresh session reads this first, then `STATE.yaml`, then
`feedback/progress.md`, and continues the loop. (Avoid bare "Pompeii" as a title — Robert
Harris owns it.)

## What this is
A **genesis-from-bible** project: a long Outlander-style time-slip historical romance built
from the author's story bible (`research/story-bible.md`) by the shared pipeline. There is no
author draft — the architect builds the blueprint, the chapter loop writes.

**RUN 2 (2026-10-18).** The author retired the first run in full (Ch.1–10 on a v3 outline) and
restarted from canon. The old blueprint is archived under `research/prior-run-2026-07/` as
reference only; the old manuscript is in git at `2a8db82`. Do not resurrect either.

Git identity: `git config user.email noreply@anthropic.com && git config user.name Claude`

## ▶ THE AUTONOMOUS LOOP (author's standing instruction — this is how the book gets written)

`STATE.yaml` carries `autonomy: full`. **Nobody pauses to ask.** The loop runs, chapter after
chapter, until the manuscript is complete or the author says stop:

```
for N in 1..total_planned:
  A  book-writer        → manuscript/chapters/chapter-N.md (+ chapter-N-report.md)
                           prompted from outline.md INCLUDING the Anti-Predictability Ledger row
                           (structural approach / opening move / ending move / dialogue band)
  B  dialogue-polish    → edits in place; evaluations/dialogue-chapter-N.md
  C  hook-craft         → edits in place; evaluations/hook-chapter-N.md
                           (respects a ledger row that says "no pull — just stop")
  D  book-disruptor     → edits in place; evaluations/disruption-chapter-N.md
  D.5 entity-tracker    → UPDATE mode EVERY chapter (author instruction 2026-10-18: "a full run
                           after each chapter so there is no drift"); contradictions logged, never
                           silently overwritten; evaluations/entity-changelog.md
  D.6 continuity-guardian → MANUSCRIPT AUDIT EVERY chapter: the new chapter against ALL prior
                           chapters + ENTITY_STATE + outline (character consistency, timeline,
                           information flow, plot threads, world rules, objects, VOICE drift vs
                           voice-dna + character-bible). CRITICAL → book-editor before anything
                           else; evaluations/continuity/chapter-N-audit.md
  D.7 shape audit       → EVERY chapter: python3 tools/shape_check.py books/the-hour-of-ash
                           (from the repo root); a flag on the new chapter = fix its opening /
                           closing signature now, not later
  E  mechanical gates   → bash tools/check_chapter.sh N  — ALL clean (style incl. foreshadow 0,
                           grammar, rhythm, show/tell, voice-wear [book-wide], metaphor). Fix via
                           book-editor.
  F  book-evaluator     → evaluations/chapter-N-eval.md (Genesis 7 dims, 20-pattern scan,
                           5 readers, Tomorrow Test; Discovery Test on Ch.1, Residue on the last)
  G  quality gate       → PASS only if Genesis Floor ≥ 8.5 AND Casual ≥ 8.5 AND PACING ok AND
                           gates clean. Else book-editor on the named dimensions → re-run E+F
                           (max 5 cycles; a chapter below the hard floor never ships).
  → update character-bible.md (new named character = new entry; NO tics, ever),
    STATE.yaml (chapters.completed, scores), feedback/progress.md (one-line pacing verdict),
    then: git add -A && git commit -m "the-hour-of-ash: finalize chapter N" && git push origin main
```

**Drift policy (author, 2026-10-18): the FULL run happens after EVERY chapter** — entity
update, continuity audit against all prior chapters, voice-wear, shape audit, and the
independent evaluation. No batching, no "every N chapters". A chapter is not final until the
audit of it against the whole book so far is clean. Phase 4/5/6 (full-manuscript evaluation,
revision, delivery) follow once every chapter is done — still without pausing.

### Session handoff — the LOOP LOCK (so two sessions never write the same chapter)
A scheduled task re-launches the loop in a fresh session on a cadence. Before touching the
manuscript, a session MUST:
1. `git pull origin main`, then read `feedback/LOOP-LOCK` if it exists. It holds
   `session=<id> chapter=<N> updated=<UTC ISO>`. If `updated` is **less than 2 hours old**,
   another session is mid-chapter: do nothing, say so in one line, and end the turn.
   Older than 2 hours = a dead session; take over.
2. Write your own LOOP-LOCK (same format) and commit + push it before dispatching the writer.
3. Refresh `updated=` (commit + push) every time a chapter is finalized.
4. When the loop stops for any reason (book complete, blocked, author said stop), delete the
   lock, commit + push, and disable the scheduled task (`update_trigger enabled=false`) if the
   stop is final.

## Hard gates (ALL must pass before a chapter is "done")
- **Genesis Floor ≥ 8.5 and Casual Reader ≥ 8.5** (book-evaluator, independent of the writer).
- **NO FORESHADOWING** (author ruling 2026-09-28): `tools/style_check.py` runs with
  `--max-foreshadow 0` by default here; the evaluator checks it too. Full rule in voice-dna.md §0.
- **Mechanical suite clean**: `bash tools/check_chapter.sh N`.
- **Anti-predictability**: the chapter matches its ledger row (approach / opening / ending), and
  `tools/shape_check.py` (repo root) is clean every 5 chapters. A flag on finalized chapters means
  a signature change on the most recent offender, not a rewrite.
- **Pacing check** vs neighbours (scene/summary, dialogue band from the ledger, emotional slot,
  length-serves-the-beat; variance is by design — never flatten it).
- **NO TICS (author ruling 2026-10-18): tic budget = 0.** Nobody, narrator included, gets a
  verbal tic, catchphrase, refrain or signature device. Distinctness by worldview, syntax,
  evasion, physicality only. `voice_wear_check.py` self-repetition findings are BLOCKING here;
  `tic_report.py` runs every chapter and any non-allowlisted phrase recurring 3+ times book-wide
  is removed before finalize; the allowlist stays ≤5 entries, each capped at 3 uses.
- **Retired reflexes** (STATE.yaml guardrails): no retrospective significance-tagging, no
  define-by-negation openers, no anaphora triads, no performed-candour tics, no device as a
  scene-button, no closing aphorisms.

## Canon guardrails (settled author decisions — never violate)
Full text in `STATE.yaml` (`guardrails` + `resolved_author_decisions`). In short: Outlander
tone; one long standalone (~245k target, 220k floor, never padded); Flavian era, arrive ~70 AD,
Vesuvius 79 AD under Titus; the map "to the Library of Alexandria" hides a time-door; Greece
(Delphi) first; the Oracle is the first source of WHERE and withholds WHEN; Fenn (marooned, old)
gives the WHEN; Mara Reyes / Emilio Reyes / Halloran / Valens "Lupus" / Lucius & Aelia; explicit
but occasional, earned heat, none after the eruption begins; she STAYS and dies with them — an
active choice; no modern coda; first-person past, in order, never reaching forward; the
authenticity dial split (sensory ~8+, harshness ~7).

## Status
See `STATE.yaml` `phase.status` and `feedback/progress.md` — those are the live resume point.
This file is the protocol, not the log.
