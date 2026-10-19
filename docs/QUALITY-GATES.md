# Quality gates

Everything a chapter has to clear, and why each gate exists. Two independent layers: the
**judgement layer** (the evaluator's scores) and the **mechanical layer** (Python scripts
that count things). Neither can substitute for the other — a model can talk itself into
thinking a chapter is clean; `grep` can't.

## The Genesis Score — 7 dimensions

1. **Originality** (genre-adjusted)
2. **Theme** (as a question, never an answer)
3. **Characters** — including the cover-the-name test and the tic-proliferation scan
4. **Prose & voice**
5. **Pacing & coherence** — the #2 predictor of commercial success in the benchmark
6. **Emotion** — assessed against the book's engagement type, not a single empathy standard
7. **Configurable** — set per book in `STATE.yaml` (structure, world-building,
   intellectual engagement, momentum, or identity effect)

**The floor is the score.** A chapter is as strong as its weakest dimension. Both floor and
average get recorded, but gates are on the floor — that is what stops a chapter with
brilliant prose and no characters from passing on its average.

### The gate

- **Hard floor** (genre-adjusted): literary 7.5, commercial 7.0, thriller 7.0, memoir 7.5,
  prescriptive NF 7.0. Below this a chapter is *broken* and never ships.
- **Pass** = **Floor ≥ 8.5 AND Casual Reader ≥ 8.5.** Nothing else is a pass. "Good enough"
  is not a state this pipeline has.
- In between: the polish loop. `book-editor` fixes only the 1–2 dimensions holding the
  floor down, quoting the evaluator's "PATH TO 8.5" and the "Strengths to PRESERVE" list —
  the second half matters, since the classic revision failure is fixing a weakness by
  flattening a strength. Max 5 cycles, then escalate.

### Anti-inflation

A model scoring prose produced by the same model is at maximum bias, so the protocol
assumes 0.5–1.0 of inflation by default:

- No score may jump more than **+0.5 per revision cycle**. So 7.5 → 8.5 takes at least two
  cycles. That is expected — budget for it rather than abandoning the loop early.
- Every score needs **textual evidence**: a cited passage.
- A floor above 8.0 without extraordinary evidence should be **challenged**.
- The evaluator scores chapters it did **not** write.

## CVI — the Commercial Viability Index

Co-equal with the Genesis Score, because the benchmark showed the two measure different
things: floor-7.0 books in the sample sold 62M copies between them; floor-8.5 books sold
6M. Craft quality does not predict sales.

- **Genesis Score** governs *revision priority* — what to fix, in what order.
- **CVI-Launch** governs *submission readiness* — commercial pacing, the Tomorrow Test,
  the casual reader's verdict, shareability, concept pitch, human closeness.
- **CVI-Legacy** governs *long-term potential* — originality, theme depth, cultural
  vocabulary, re-readability.

**When Genesis and CVI diverge by 2.0+, the divergence is itself the finding**: well-crafted
but commercially fragile, or commercially potent but critically limited. Both are useful to
know before you publish; neither is automatically a problem to fix.

## The reader simulation

Five readers, run against every chapter. They exist because "is this good?" is the wrong
question — different readers fail a book for different reasons.

| Reader | Fails on |
|---|---|
| **The Devourer** | Boredom. Would they keep turning pages? |
| **The Critic** | Craft. Cliché, unearned emotion, sloppy structure. |
| **The Hostile** | Everything. Fed by the hostile persona from `reader-personas.md`. |
| **The Casual Reader** | Effort. The gate reader — must score ≥ 8.5 to pass. |
| **The Devoted Reader** | Genre expectations, when the genre has them. |

Plus the **Tomorrow Test** (what concrete anchors does the reader still remember tomorrow?),
the **Discovery Test** on chapter 1 (BUY / MAYBE / PUT BACK from three pages) and the
**Residue Test** on the final chapter (emotional residue, not a cliffhanger).

## The 20-pattern anti-AI scan

Ten surface patterns (forced symmetry, empty poetic vocabulary, rule of three, excessive
em-dashes, empty metaphors, "And" openings, pseudo-philosophical closings, excessive
parallelism, over-smooth transitions, described emotions) and ten deep ones. The deep ones
are the ones that matter, because they survive editing:

**#11 Explanatory Extension** — observations that explain themselves; similes with an
extension that unpacks the comparison. The single most reliable AI fingerprint, and the
disruptor's priority-one target. Write similes **raw**; do not extend them.

Then: #12 binary negation openers ("Not X. Not Y. It was Z."), #13 precision flex
(unnecessarily exact numbers), #14 emotional control demonstration (notice → manage →
continue, always successfully), #15 authoritative description (settings with no gaps or
wrong impressions), #16 philosophical asides (thoughts that work on coffee mugs), #17 clean
dialogue (orderly turn-taking, no interruptions or cross-talk), #18 thematic echo chamber
(every detail resonates; zero texture, zero noise), #19 graduated reveal (the same
establish → anomaly → escalate → close shape every chapter), #20 emotional temperature
reports at even intervals.

Scoring is by **density per 1,000 words**, not raw count, and thresholds are
**genre-adjusted** — human bestsellers score 0–13/20 on this scan, and commercial fiction
is *supposed* to hit more of these than literary fiction. Clean bands: literary 0–3,
memoir 0–4, commercial 0–8, prescriptive NF 0–12.

**Prevention beats detection.** The whole anti-AI apparatus is aimed at not writing these
in the first place — the writer works under the anti-pattern budget, the architect varies
structure, the bible caps tics. The scan is the backstop.

## The mechanical gates

Per-book scripts in `books/<slug>/tools/`. They are deterministic, they gate by exit code,
and they catch what judgement misses across a whole manuscript.

### `style_check.py`

```bash
python3 books/<slug>/tools/style_check.py
python3 books/<slug>/tools/style_check.py --max-simile 4
```

- **Verbal tics** — crutch words (just, suddenly, seemed, somehow, for a moment…) over a
  ceiling.
- **Repeated phrases** — distinctive 4–6 word n-grams reused within or across chapters.
- **Simile/metaphor load** — markers per 1,000 words against a ceiling.
- Reports adverb (-ly) and em-dash density per chapter.

**The ALLOWLIST is per-book** and is the one pipeline file that is *not* shared — your
deliberate motifs are yours. It is also **a capped registry, not an exemption**:

> **The motif cap.** No signature narrative phrase may recur more than **3 times across a
> whole book**. Declaring a motif in the ALLOWLIST does *not* license unlimited use — it
> exempts the phrase from the generic repeat check while still holding it to the cap.
> Entries are `"phrase"` (cap 3) or `("phrase", N)` to raise the cap for a genuinely
> load-bearing image. Keep overrides rare and small. The gate fails if a motif exceeds its
> cap.

That rule exists because a motif is only a motif at low frequency. At the seventh use it
is a tic, and readers notice the shape of it before they notice the meaning.

### `grammar_check.py`

```bash
python3 books/<slug>/tools/grammar_check.py
python3 books/<slug>/tools/grammar_check.py --languagetool     # optional tier 2
```

**Tier 1 gates** (deterministic, near-zero false positives): doubled consecutive words
("the the", "Bella Bella"), space before punctuation, a/an mismatch. **Tier 1 reports**
(non-gating, needs judgement): the longest sentences per chapter, double spaces. **Tier 2**
(optional, never gates): tense/agreement/dangling-modifier scan via LanguageTool — an
assist, not an authority, because it is false-positive-prone on fiction dialogue.

### `voice_wear_check.py`

```bash
python3 books/<slug>/tools/voice_wear_check.py
```

Shipped with every new book. The Amelia Lesson made mechanical: three layers —
book-wide **retired phrases** (a hard gate; seeded with "never once"), **auto-detected
self-repetition per POV** (no configuration; it finds phrases a POV repeats across its own
chapters), and optional **named-device caps** per character. Multi-POV books get a
`feedback/pov-map.txt` (`chapter-N: Name` per line); single-POV books can skip it.

### `tic_report.py --gate` — the no-tics gate (shipped with every book)

```bash
python3 books/<slug>/tools/tic_report.py --gate      # every chapter
```

The author's standing law is that **no character, narrator included, carries a verbal tic,
catchphrase, refrain or device — in any book, ever.** `voice_wear_check.py` catches a POV
repeating itself across chapters (its self-repetition findings FAIL, not warn). This gate
closes the other door: any content-rich phrase of 3–6 words recurring **3+ times across the
whole book**, and any spoken phrase of 3+ words recurring in dialogue (a catchphrase
forming), fails the chapter. The only exemptions are the few allowlisted object-motif
phrases (≤5, each capped at 3 uses) and a short list of unavoidable world terms (place
names, titles). On a finished unguided draft it typically finds a dozen lines the writer
never noticed — "for the first time" fourteen times, a character's favourite saying six
times — which is exactly the creep it exists to stop.

It also carries a **gesture layer**, because a tic does not need repeated words: a cast
that keeps picking things up and setting them down, nodding, swallowing, looking away or
pausing "for a long moment" is repeating stage business with the wording varied. The
script counts gesture *classes* by meaning (object handling, nods, shrugs, sighs,
swallows, breath beats, jaws, looking/turning away, "a long moment", hair, grips, eyes,
lips, head shakes) book-wide and per chapter, and fails three shapes of cluster: **a scene
running on one gesture** (3+ of a class within 500 words — the reader-visible tic: a
headmistress who sets down the paper, takes off her spectacles, picks them up, turns them
over, puts them back on, all between lines of one conversation); a chapter over its cap
(4, or one per 1,000 words for a long chapter); and, once the manuscript has 20,000 words,
more than 0.3 per 1,000 words across the book. Measured on an earlier finished book it
found "a long moment" 65 times and object handling 49 times with eight scene clusters —
the exact reflex a reader had noticed. The handling class is deliberately narrow
(set/put down, pick up, take out of, put back, hold out, turn over) so that functional
actions and idioms ("put money on it", unpacking a bag) do not fire it; the evaluator
judges the business the regex cannot classify. Extend `GESTURE_CLASSES` in the book's
copy when a new piece of business starts to recur.

A third layer, **RHYTHM & VOICE REFLEXES**, counts narration only (speech and italic documents
excluded): **AND-CHAINS**, sentences with four or more "and"s, capped at max(9, words ÷ 900) per chapter
(one designed held sentence is a device; a dozen is the narrator's default rhythm — Hazel Academy ran 2–8
early and drifted to 20–26 late), and **CREDENTIAL ASIDES**, the book-specific phrases by which a narrator
files the world under her own expertise (`CREDENTIAL_PATTERNS` in the book's copy; capped at 4 per chapter).
The echo scan also lists **COMMAND ECHO candidates**: a short quoted order whose verb returns at the head of
the next narration paragraph ("Hold that corner." / "I held it…"), the narrator answering an order by repeating
it as compliance. Defiance and plain narrative match too, so the list is judged by hand and never fails; a
book allows about three real ones. It exists because the move slipped past the writer, the disruptor and the
bible in Hour of Ash Ch.9.

The **ECHO SCAN** (`--echoes N`) also reads the book's `voice-bank/samples/` when there is one: a 5+-word phrase
shared with a benchmark sample is listed as an echo from "voice-bank", because the samples are register targets,
never text to reuse (shorter matches are left out; the samples share the book's own nouns).

It also counts **NEGATION PIVOTS**: a short negated clause hinged on a semicolon to a pronoun that says
what happened instead ("the mule did not pull; she sat back"). That is define-by-negation in miniature,
and it reads as a device quickly. The cap is 1 per chapter, and the gate fails at 3 book-wide. The pattern
is deliberately narrow, so an ordinary negative sentence followed by a new one does not fire.
Two **NARRATOR MOVES** are capped at 1 per chapter: a paragraph opening "So I…" (the narrator's consequence
hinge) and "before I had decided/thought…" (the body outrunning the mind). A "So" opener in 4+ consecutive
chapters prints a WATCH without failing, so the streak shows before it hardens.
Because a capped habit moves rather than dies, the whole **HINGE FAMILY** of paragraph openers (So / Then /
After that / Afterward / Later / Next) is also capped, at max(3, words ÷ 2,500) per chapter.

A second layer, **PROP FIDGET**, follows a single object through a scene — including "it" and "them"
back to the prop named last — and fails when it is fidgeted with (turned, set down, picked up, taken
off, put back, held in the fingers or the mouth) 3+ times within 400 words. That is the exact shape of
the Hazel Academy spectacles scene, where the prop does the acting between lines of dialogue. Real
action (fighting for a bag, packing a parcel) uses other verbs and does not fire.

### `shape_check.py` — the predictability audit (shared, book-agnostic)

```bash
python3 tools/shape_check.py books/<slug>            # every ~5 chapters, from the repo root
python3 tools/shape_check.py books/<slug> --strict   # Phase 4: exit 1 on any flag
```

No per-chapter gate can see the loudest machine tell, which lives *between* chapters: every
chapter the same length, opening the same way, closing on a punch-line, with the same number
of scene breaks and the same dialogue share. This script measures the shape of every chapter
and flags uniformity (`LEN-CLUSTER`, `OPEN-RUN`, `END-RUN`, `PUNCH-REFLEX`, `DIALOGUE-FLAT`,
`BREAKS-SAME`, `RHYTHM-FLAT`, …). It is the mechanical counterpart of the architect's
Anti-Predictability Ledger (book-architect §0.5 Step 5): the ledger plans the variety, the
Writer is prompted from it, and this script proves the manuscript actually kept it. A flag
on finalized chapters means revising the most recent offender's opening or closing — a
signature change, not a rewrite.

### Other per-book checkers

Books that needed them grew them; copy any into a book with the same problem:
`rhythm_check.py`, `tic_report.py`, `show_tell_check.py`, `metaphor_check.py`.

### The word floor

```bash
wc -w books/<slug>/manuscript/chapters/chapter-*.md
```

Gated on the **book total** against `manuscript_min_words`. There is deliberately **no
per-chapter floor** — a per-chapter minimum recreates the uniform 20 × 5,000-word shape
the architect works hard to avoid. `shortest_chapter_floor` is only a sanity check on the
shortest allowed chapter.

## Cross-model second opinions

The evaluator shares a model family with the writer, which makes it blind in exactly the
places the writer is.

```bash
bash tools/gemini_review.sh books/<slug>/manuscript/chapters/chapter-12.md
bash tools/grok_review.sh   books/<slug>/manuscript/chapters/chapter-12.md "focus on the middle sag"
```

Or the slash commands `/gemini-second-opinion` and `/grok-second-opinion`.

The editor persona and book briefing are **derived from the book** by
`tools/review_context.py`: it walks up to the nearest `STATE.yaml` and builds the context
from title, genre, premise, comps, series position and the settled guardrails (so the
outside model doesn't propose undoing decisions you already made). Override it per book by
writing `books/<slug>/review-context.md`, or per run with `REVIEW_CONTEXT="..."`.

Keys live **outside the repo**: `~/.gemini_env` / `~/.grok_env` (mode 600) or the
environment. Never commit them.

Treat the result as a second opinion, not an authority. Where two different models agree,
the finding is high-confidence. Where an outside model objects to something your canon
settled deliberately, note it and move on.

## APODICTIC

`tools/apodictic/` is a full developmental-editing plugin (enabled in `.claude/settings.json`)
that works at the manuscript level rather than the chapter level: structural diagnosis,
plot-architecture selection, specialized audits (scene, character architecture, emotional
craft, comedy, consent, interiority, shelf positioning), submission-readiness verdicts, and
a nonfiction argument engine. Start with `/apodictic:start`, which routes you in two or
three questions. Use it when a finished draft has a *structural* problem — the chapter loop
polishes chapters, and no amount of chapter polish fixes a spine.

## The running order

```bash
# per chapter, after the agent loop
python3 books/<slug>/tools/style_check.py
python3 books/<slug>/tools/grammar_check.py
python3 books/<slug>/tools/voice_wear_check.py   # whole-book; run periodically
git add -A && git commit -m "finalize chapter N"

# every 3-5 chapters
#   entity-tracker UPDATE, continuity-guardian audit

# at the end
wc -w books/<slug>/manuscript/chapters/chapter-*.md    # word floor
#   full-manuscript evaluation, then Phase 5 revision to floor 8.5 everywhere
```
