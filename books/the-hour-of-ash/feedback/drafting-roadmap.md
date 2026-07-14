# Drafting Roadmap — Pompeii (working title / "The Hour of Ash")

**Purpose:** the single production plan to draft the whole book, Ch.1 → Ch.36, on the v2
36-chapter / 5-Movement blueprint. Read alongside `outline.md` (structure), `foundation.md`
(character/theme/seeds), `voice-dna.md` (voice), `STATE.yaml` (canon/gates), and this book's
`CLAUDE.md` (per-chapter loop). Update the trackers below as chapters finalize.

Status at write time: **Ch.1–2 finalized (~10,000w). 34 chapters / ~263,000w remaining.**
Target Σ 273,000w · floor 220,000w. All major author decisions resolved (STATE.yaml).

---

## 0. SET-UP (do ONCE, before Ch.3) — currently missing, do first

1. **Build `ENTITY_STATE.yaml`** (entity-tracker, BUILD mode) from Ch.1–2 + foundation.md +
   story-bible. This does not exist yet and is essential for a 9-year, 36-chapter saga with
   heavy re-read seeds. It must track:
   - **Characters:** Mara Reyes (father Emilio Reyes), Valens/"Lupus", Fenn, Kallia, Drusus, Sabina, the legate, Prof. Halloran,
     Lucius, Aelia, Theano/the Pythia — plus each one's fixed traits, Roman-vs-modern names,
     and first/last appearance.
   - **Timeline:** modern frame (late 1990s) → crossing → Greece 70 AD → Campania ~72–78 AD →
     eruption **late summer 79 AD** (Titus). The ~9-year span and children's ages MUST stay
     internally consistent (Lucius born ~Ch.17; Aelia ~Ch.22).
   - **Places:** the coast/threshold; Delphi; the Bay of Naples; the door's site near Pompeii.
   - **Objects (load-bearing):** the map, Fenn's notes/coordinates, the 35mm camera +
     undeveloped roll, the father's dig slides, the wristwatch, the bread starter.
   - **World rules:** the door "only opens for the one it brought"; Oracle gives WHERE not WHEN.
2. **Seed the `voice_map.txt`** (or POV note) — this book is single-POV first-person (Mara),
   so `voice_wear_check.py` runs layer-2 generic repetition; no per-character device map needed.
3. **Tune `style_check.py` ALLOWLIST** for deliberate motifs as they emerge (bread/"rises",
   "the one it brought", "function unknown", the *click*) — add them the first time a gate
   flags a motif you intend to repeat, so real repetition still trips.
4. Confirm the gate tools run clean on Ch.1–2 as a baseline (they do — verified on import).

---

## 1. THE PER-CHAPTER LOOP (the gate stack — every chapter, in order)

For chapter N, do NOT commit until ALL of these pass. This is the CLAUDE.md loop made concrete
with the newly-imported tools:

1. **Re-read** chapter N-1 (voice + last beat) and the outline entry for N.
2. **Draft** (book-writer) to the outline beat + the chapter's word target (±10%).
3. **Self-pass:** dialogue-polish → hook-craft (open with a hook, end with a pull) → disruptor.
4. **Mechanical gates (HARD — must be clean):**
   - `python3 tools/style_check.py` → RESULT: clean (simile ≤4/1k, **em-dash ≤4/ch**, no NEW
     cross-chapter repeated phrase, tics under ceiling).
   - `python3 tools/grammar_check.py` → RESULT: clean (doubled words, a/an, space-before-punct).
5. **Craft assists (non-gating — read + act on the worst):**
   - `python3 tools/metaphor_check.py N` (figurative load + long-sentence %),
   - `python3 tools/rhythm_check.py` (no flat sentence-length triplets),
   - `python3 tools/show_tell_check.py` (filter-verb / abstraction / dialogue-share smoke alarm),
   - `python3 tools/tic_report.py` (verbal tics), `python3 tools/voice_wear_check.py` (self-repeats).
   - Shortcut: `bash tools/check_chapter.sh N` runs the whole stack for chapter N.
6. **PACING check** (required — see CLAUDE.md): scene/summary balance; dialogue ~30–45% (interior
   chapters may run lower BY DESIGN); the emotional "W" — is N's high/low right for its slot;
   **length serves the beat** (variance is intentional here — do NOT flatten it). Log a one-line
   verdict.
7. **Independent evaluation** (book-evaluator): **Genesis Floor ≥ 8.5** across the 7 dimensions.
   Below 8.5 → book-editor polish loop (max 5), then re-gate.
8. **Update trackers** (this file: word-budget row + seed/insert checkboxes) and `feedback/progress.md`.
9. **Commit:** `git add -A && git commit -m "genesis: finalize chapter N"`.

**After every Movement (batch):** run a **continuity-guardian** pass over the Movement's chapters
+ `ENTITY_STATE.yaml` update (entity-tracker, UPDATE mode). Fix drift before the next Movement.

---

## 2. BATCH PLAN (by Movement) + author checkpoints

Draft **sequentially** (each chapter needs the prior finalized chapter for voice + plot + entity
continuity). Batch = one Movement, then a continuity pass + an author checkpoint.

| Batch | Movement | Chapters | Words | After the batch |
|---|---|---|---|---|
| **A** | I — The Drawer and the Door | Ch.3, 4, 5 *(1–2 done)* | ~18,600 | continuity-guardian + **author checkpoint 1** (voice/crossing lands?) |
| **B** | II — Learning to Exist (Greece) | Ch.6–13 | ~78,600 | continuity-guardian; **checkpoint 2** at Ch.10 (Oracle TP) + at Ch.13 (marriage hinge) |
| **C** | III — The Life She Built | Ch.14–18 | ~48,400 | continuity-guardian + **checkpoint 3** at Ch.18 (midpoint reversal) |
| **D** | IV — The Arithmetic | Ch.19–27 | ~71,000 | continuity-guardian + **checkpoint 4** at Ch.20 (Fenn payoff) |
| **E** | V — Ash | Ch.28–36 | ~46,400 | full-book continuity audit + **final checkpoint** (the ending + seed payoffs) |

Because Movements II and IV are long (8–9 chapters), split each into two review passes (mid-Movement
continuity check) rather than waiting for 78k words to accumulate.

**Cadence note (from progress.md):** the standing author preference is **one chapter at a time,
author reviews before the next** for the early chapters. Honor that through at least Batch A; if the
author wants to accelerate, move to Movement-sized batches with checkpoints only at the turning points.

---

## 3. WORD-BUDGET TRACKER (target vs actual — fill `actual` as you finalize)

| Ch | Title | Target | Actual | Ch | Title | Target | Actual |
|----|-------|-------:|-------:|----|-------|-------:|-------:|
| 1 | The Drawer | 4,900 | **4,906** | 19 | Harboring | 8,800 | — |
| 2 | Too Accurate to Be Fake | 5,100 | **4,961** | 20 | The Madman on the Coast (Fenn) | 10,800 | — |
| 3 | Coordinates & the Survey | 7,000 | — | 21 | The Arithmetic She Won't Do | 4,600 | — |
| 4 | The Threshold (SHORT) | 1,800 | — | 22 | Aelia | 8,200 | — |
| 5 | Greece, 70 AD | 9,800 | — | 23 | Small Quakes | 5,200 | — |
| 6 | Kallia's House | 10,400 | — | 24 | The Faction Strikes | 9,600 | — |
| 7 | The Roman With the Mules | 9,800 | — | 25 | After | 4,800 | — |
| 8 | Earning the Yes | 9,000 | — | 26 | The Sea Goes Out | 9,000 | — |
| 9 | The Road to Delphi | 9,000 | — | 27 | Telling Him & Preparing | 10,000 | — |
| 10 | The Pythia (Oracle TP) | 9,600 | — | 28 | The Road to the Door | 7,800 | — |
| 11 | Winter in Delphi (LONGEST) | 12,000 | — | 29 | The Door Will Not Take Them | 7,400 | — |
| 12 | The First Night Is a Mistake | 8,400 | — | 30 | The Hour (SHORT) | 2,600 | — |
| 13 | Leaving Greece & the Marriage | 10,400 | — | 31 | Pliny's Sky (LONG) | 8,800 | — |
| 14 | Under the Mountain | 9,800 | — | 32 | The Law of the Door (SHORT) | 3,200 | — |
| 15 | Building a Life (LONG) | 11,000 | — | 33 | What She Carries | 4,200 | — |
| 16 | The Catalogue of Small Days | 9,200 | — | 34 | The Last Ordinary Thing (SHORT) | 3,400 | — |
| 17 | Lucius | 8,600 | — | 35 | What the Ash Keeps | 7,400 | — |
| 18 | Sabina (MIDPOINT) | 9,800 | — | 36 | The Door (Closing) (SHORTEST) | 1,600 | — |

Running Σ target = **273,000** (floor 220,000). Track running actual after each Movement; if a
Movement lands >5% under, expand its thinnest immersive chapter before moving on, not at the end.

---

## 4. RE-READ SEEDS & FENN INSERTS — plant/pay checklist (do NOT let these slip)

The whole design rests on these landing. Check the box the moment it's on the page.

**Fenn document-inserts (epistolary — the reader assembles the door's law ahead of Mara):**
- [x] #1 — map marginalia, Ch.2 ("the map is honest, the door is not")
- [ ] #2 — journal, Ch.5 ("I, too, woke in the wrong year.")
- [ ] #3 — journal, Ch.10 (doors "only open for the one they brought," unexplained)
- [ ] long letter — Ch.18 (the law stated almost plainly; reader now ahead of Mara)
- [ ] note — Ch.24 ("the doors do not wait for grief")
- [ ] final note — Ch.29 ("I told him. You stopped doing the arithmetic. So would I.")

**Re-read seeds (plant → pay):**
- [ ] Seed #1 "keep nothing you can carry" — Oracle **plants Ch.10** → **pays Ch.33** (she drops
      camera/slides/watch/map).
- [ ] Seed #3 Valens's hands find a task (knot/strap) whenever feeling threatens — **Ch.11 onward** →
      re-read reward at the loss, when his hands have nothing left to tie. (REVISED 2026-07-11: was
      "Valens counts the children"; counting cut — device reused in another of the author's books and
      overlapped Drusus. Physical tell replaces the verbal tic.)
- [x] Seed #4 fieldwork kit ritual (load camera/watch/slides) — **PLANTED Ch.3** (2026-07-11: 35mm
      camera loaded step by step, father's watch wound, and the date written in her own hand at the head
      of a fresh gridded page) → **pays Ch.26** (date matches one already in her own field notebook, in
      her own hand).
- [ ] Seed #5 Aelia's "It's snowing!" — **Ch.31** (child's sweetness / reader's dread).
- [ ] Bread-starter thread — dead in **Ch.1** → first that *rises* **Ch.16** → Aelia's bread-frown
      **Ch.22** → Mara lets it die on purpose **Ch.27**.
- [ ] Theano/Pythia's first prophecy encodes the ending — **plants Ch.10** → **pays Ch.35** (mercy,
      not cruelty).
- [ ] "The one it brought" / "function unknown" motif convergence — **pays Ch.35–36**.

---

## 5. STANDING CRAFT CONSTRAINTS (apply every chapter — from CLAUDE.md/foundation)

- **Voice:** first-person, past, **retrospective** (older Mara; dread bleeds backward). Match Ch.1–2 exactly.
- **Authenticity dial — "best of both":** SENSORY/period detail cranked to ~8+ (carbonized bread,
  garum, insulae, lamps, Pliny's black-noon sky); HARSHNESS/pace held at Outlander ~7 (slavery/
  gender-powerlessness real and present but never grinds the romance/pace down — escapism wins ties).
- **Voice-under-pressure:** Mara's prose goes **flat/procedural** in fear/violence/birth (Ch.9, 17,
  24, 29, 31) — rehearsed for life (Ch.17 birth) before it's used for the catastrophe.
- **YA/heat is N/A here — adult historical romance:** explicit intimacy is OCCASIONAL/earned
  (~Ch.12, 15-area, + a late payoff), **none after the eruption begins**. Not erotica, no per-page quota.
- **Violence:** consequence, not spectacle; cut the camera on the worst of it; the horror lives in
  the aftermath (esp. Ch.29–36 — surge is light/heat/silence, NOT gore).
- **Length is a signal:** honor the swell-then-collapse. Do NOT pad short punch chapters (4, 30, 32,
  34, 36) or rush the long immersive ones (11, 15, 20). Flag only length that FIGHTS its beat.
- **No modern coda.** The book ends in 79 AD, inside Mara's last hours. Never a future survivor's frame.

---

## 6. RISK REGISTER (watch these across the draft)

- **Timeline drift** (9-year span, kids' ages, 70→79 AD) — the #1 continuity risk; ENTITY_STATE +
  per-Movement continuity-guardian is the mitigation.
- **The dramatic-irony clock** (reader ahead of Mara via Fenn's notes) must stay *taut, not smug* —
  Mara's refusal to do the arithmetic has to read as human avoidance, not authorial withholding.
- **Sagging middle** (Movements II–III are ~127k of immersion) — each long chapter needs a live
  scene-question, not just texture; watch show_tell dialogue-share and the emotional "W".
- **The ease-is-the-horror rule** (Ch.14–16, 22) — Mara must NOT sense doom in the happy chapters;
  only the retrospective narrator's shadow, never the character's foreboding.
- **Heat placement** — keep it earned and pre-eruption; do not let it drift late.
- **Word undershoot** — 34 chapters at ambitious targets; check running Σ per Movement, expand early.

---

## 7. IMMEDIATE NEXT ACTIONS (in order)

1. Build `ENTITY_STATE.yaml` (Set-up §0.1) from Ch.1–2 + foundation + bible.
2. Draft **Ch.3 "Coordinates & the Survey"** (~7,000w) — re-anchor on the fieldwork **kit-ritual**
   (the "Fenn exactly her age" beat was spent as Ch.2's final line); plant re-read seed #4; run the
   full gate stack; author checkpoint before Ch.4.
3. Then Ch.4 (SHORT crossing punch, ~1,800w) → Ch.5 (LONG landing, ~9,800w) to close Movement I;
   continuity-guardian + ENTITY_STATE update; author checkpoint 1.
4. Proceed by Movement per the batch plan.
