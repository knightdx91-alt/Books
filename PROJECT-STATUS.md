# Books — project status & consolidation log

_Last updated: 2026-09-07._

This repo is the consolidated home for all books + the shared writing pipeline. This file
records what's here, decisions made, and the manual steps still outstanding.

## What's in `books/`

**Migrated full books** (from their old standalone repos):
`the-gift`, `full-dive`, `scale-and-silver`, `death-and-remembrance`, `the-power-thief`,
`the-replaced`, `a-god-of-thieves`, `all-the-worlds-she-keeps`, `the-hour-of-ash`, `the-long-goodnight`, `apathetic-love`,
`sygl-book`, plus two series: `saeren/` (3 books) and `land-of-the-guardians/` (Ne'veran,
4 books incl. scaffolded `the-dragon-isle` + `the-origin`).

**OCR / early-stage stories** (transcribed from handwritten pages; folders renamed to their
final author-chosen titles 2026-07-14):
`legends-progeny` (James Mason), `anchor-of-the-damned` (Zack), `shadowcrosser`, `the-burning-tree`,
`the-fourfold-crown`, `everything-that-lingers` (John Maxwell premise).

## Key decisions (this session)

- **One repo, subfolders on `main`** (not branch-per-book). Pipeline at root, shared by all.
- **Workflow Law enforced by hooks:** `main` only, no branches, no PRs (SessionStart auto-
  switches off any stray branch + deletes it; a PreToolUse guard blocks branch/PR commands).
- **The Long Goodnight:** the digital docs are **canon**; the handwritten OCR draft (Troy→Xavier,
  Chris→Derek) is kept as source at `books/the-long-goodnight/research/original-handwritten-draft.md`.
- **rosalia** = the OG version of `scale-and-silver`; not needed separately — dropped (git history only).
- **Black Jewels ≠ Sygl**, **Hazel's story ≠ Saeren** — confirmed separate, do NOT merge.
- **apathetic-love** was re-pulled from repo `main` (earlier migration grabbed the smaller
  default-branch/OCR version); now has the full manuscript + `story-notes.md`.
- **scale-and-silver earlier/fuller draft** preserved as deleted-scenes reference at
  `books/scale-and-silver/research/earlier-fuller-draft/` (before deleting the old Saeren branch).

## Branch audit (for safe deletion of old repo branches)

All book repos were audited so branches can be deleted without losing content.
- Repos with **only `main`**: everything already consolidated — nothing on branches.
- **Apathetic-Love:** `main` is the complete superset. ⚠️ **Switch its default branch to `main`
  in GitHub settings BEFORE deleting `claude/book-text-ocr`.**
- **The-Manipulators:** its `claude/new-book-project` branch is identical to `main`.
- **The-Saeren-Chronicles (15 non-main branches):** all safe to delete. Other-book content on
  them is preserved in the dedicated books + here; the only unique prose (scale-and-silver's
  fuller draft) is now saved (above). rosalia was rescued then dropped per author.

Note: **branch deletion does NOT work from the Claude web environment** (git proxy returns 403).
Delete via the GitHub website (repo → Branches → trash icon) or a local terminal.

## Session log — 2026-07-13 (readiness + first architect pass)

**Goal:** get every book folder "ready to start work," then begin architect passes.

- **Normalized all folders to standard pipeline layout** (idempotent; nothing overwritten).
  The 6 OCR stubs, plus the 3 non-standard folders (`apathetic-love`, `sygl-book`,
  `the-long-goodnight`), now have `STATE.yaml`, `CLAUDE.md`, `tools/` (style+grammar),
  standard dirs, and `feedback/progress.md`. OCR premises moved to `research/source-notes.md`;
  apathetic-love's 19.6k draft staged as `research/original-draft.md`. Saeren Bk 1 & 2 got
  per-book `CLAUDE.md`; the two planned LotG books scaffolded.
- **Filled `STATE.yaml`** (genre, subgenre, comps, engagement, one-line premise, canon
  guardrail, open decisions, canon-source path) for 9 pre-blueprint books:
  the-fourfold-crown, anchor-of-the-damned, shadowcrosser, everything-that-lingers, legends-progeny, the-burning-tree,
  apathetic-love (revise-existing-draft), sygl-book (rewrite/expansion), the-long-goodnight.
- **Genre corrections:** `anchor-of-the-damned` = **standard harem** (one male MC Zack + the five
  girls who summon/anchor him — NOT reverse harem). `sygl-book` confirmed harem-romance.
  `legends-progeny` (James Mason) locked **NO-ROMANCE** guardrail per source. Scanned all other books —
  no other hidden harem/romance structures.
- **First architect pass DONE — `legends-progeny` (James Mason):** foundation.md + outline.md +
  voice-dna.md built; STATE phase→2, total_planned **26 chapters (~115k words)**;
  macro-structure = 5-movement progression ladder (not 3-act). Blueprint is **staged/committed
  but awaits author sign-off** on: (A) grandfather = Seminova-native legend "Corin Vale";
  (B) one tower per book (Bk1 = Strength Tower); and invented names (towns Hallowmere/Draeval,
  ally Wren, Corin Vale) — all renameable. **Ready for Chapter 1 once confirmed.**

### Architect-pass readiness map (for next session)
- **Blueprint complete → near ch1:** `death-and-remembrance`, `the-gift` (already had F+O+V);
  `legends-progeny` (done this session, pending author confirm).
- **Needs partial pass:** LotG Bk 1 (`land-of-the-guardians/land-of-the-guardians`) — has
  foundation+outline, needs only `voice-dna.md`.
- **Needs full architect pass (STATE filled):** the-fourfold-crown, anchor-of-the-damned,
  shadowcrosser, everything-that-lingers, the-burning-tree, full-dive, all-the-worlds-she-keeps, the-replaced, a-god-of-thieves,
  the-power-thief, LotG `son-of-none`/`the-dragon-isle`/`the-origin`.
- **Special (reconcile / adaptation, NOT fresh architect):** `sygl-book` (lift `project/`
  blueprint to root), `the-long-goodnight` (reconcile 2 chapters + docs to canon),
  `apathetic-love` (entity-tracker BUILD → architect in revise mode).
- **Open per-book author decisions still pending** in each STATE.yaml's `open_author_decisions`
  (e.g. anchor-of-the-damned heat level + harem roster; greater-demon-vs-Demon-Lord; sygl friction).
- **Check:** LotG README calls `son-of-none` "Drafted ~26k words" but its `manuscript/chapters/`
  is empty — locate that draft before treating it as adaptation vs from-scratch.

## Session log — 2026-09-07 (make the pipeline usable by other people)

**Goal:** turn this from "Terry's repo that happens to contain a pipeline" into something a
stranger can fork and run — without weakening anything we settled.

- **New `docs/` suite** (9 documents + index): GETTING-STARTED, PIPELINE (12 agents, phases,
  every file), CHARACTER-BIBLE (four axes, tic budget, the Amelia Lesson, retrofitting onto an
  existing draft), SERIES (series bible, canon carry-over checklist), QUALITY-GATES (Genesis
  Score, CVI, the 20-pattern scan, motif cap, mechanical checkers, second opinions, APODICTIC),
  PUBLISHING (the IngramSpark specs + every rejection we ate), WORKFLOW-AND-HOOKS,
  TROUBLESHOOTING, GLOSSARY. Root README rewritten as the front door; CLAUDE.md points into docs.
- **Series support made real, not just convention:** `tools/new-series.sh`,
  `books/_series-template/` (SERIES-BIBLE.md + README), and `tools/new-book.sh --series <slug>
  --position N`, which writes the `series:` block into STATE.yaml and auto-links the previous
  book. The orchestrator now tells the architect to read the series bible + previous book's
  character bible for a series entry.
- **Character bible wired into the pipeline properly.** It was a required architect deliverable
  in `book-architect` §3b but the orchestrator never asked for it or verified it. Now it does:
  produced in the voice dispatch, verified after, read by the writer (with the tic budget called
  out as a hard ceiling) and by dialogue-polish. Added `character_bible:` to the STATE schema.
- **Fork blockers fixed:** orchestrator wrote books to `~/Desktop/livros/{slug}/` (upstream
  leftover) → now `books/<slug>/`; template CLAUDE.md still told sessions to clone Best Seller
  Studio and use `book/genesis/<slug>/` → rewritten for the monorepo; template STATE.yaml
  decisions line and the Saeren-named gate docstrings generalized.
- **Second-opinion scripts generalized.** `gemini_review.sh`/`grok_review.sh` hardcoded Saeren
  Book Two's series context and a YA-fantasy editor persona, so every other book got reviewed
  against the wrong book. New `tools/review_context.py` derives the persona and briefing from
  the book's own STATE.yaml (title, genre, premise, comps, series position, settled guardrails),
  overridable via `<book>/review-context.md` or `$REVIEW_CONTEXT`.
- **`.claude/pipeline.conf` added.** `WORKFLOW_LAW` (main-only | off) is now read by BOTH hooks,
  so a fork can choose branches/PRs; this repo stays `main-only`. Also `AGENT_SOURCE`,
  `PIPELINE_MODEL`, `PIPELINE_MAXTURNS`.
- **SessionStart hook made self-contained.** It now installs the 12 agents from THIS repo's
  `.claude/agents/` instead of always refetching the upstream tarball — which had been
  overwriting our improved agents in `~/.claude/agents` every session. Upstream fetch is kept as
  an opt-in (`AGENT_SOURCE=upstream`) and as the fallback if repo agents are ever missing.

Verified: both hook paths (law on → blocks, law off → passes), the SessionStart hook end-to-end
(installs 12 agents, leaves the tree clean), series scaffolding for books 1/2/3 including
previous-book auto-detection and valid YAML, and the derived review context on a real book.

**Not done (author's call):** no LICENSE file at the repo root. The pipeline is forkable but the
manuscripts under `books/` are copyrighted work — the README says so explicitly and tells a
forker to delete the book folders. Add a license covering `.claude/`, `tools/` and `docs/` only
if you want to make the pipeline's terms explicit.

### Follow-up the same day — "plug and play" pass

A second sweep for anything a fresh fork would trip over, beyond documentation.

- **`setup-script.sh` was the worst blocker — rewritten.** It cloned the separate personal
  `knightdx91-alt/book-pipeline` repo (which no forker can reach, and which contradicts this
  repo's own "the pipeline lives here" model, installing stale agents over the good ones),
  and it wrote a personal global `~/.claude/CLAUDE.md` — i.e. it installed the author's own
  standing instructions into anyone else's account. It now installs only the toolchain, and
  carries a commented placeholder for whatever you want your own global instructions to be.
  ⚠️ **Terry: your environment's setup-script field still has the OLD version.** Paste the
  new one in. If you want your global CLAUDE.md recreated in fresh containers, put it in the
  commented block at the bottom of your own copy — it is no longer shipped in the repo.
- **`tools/install.sh`** — local one-command setup (deps + agents). The SessionStart hook
  only runs in the web environment, so a local clone previously got nothing.
- **`tools/doctor.sh`** — preflight: deps, agents in both locations, hook syntax, config,
  tools, templates, keys, and per-book STATE health. Exits non-zero on real problems, so it
  doubles as a CI check. It immediately found a real bug: **saeren-chronicles-book-2's
  STATE.yaml did not parse** (two `key:"value"` entries missing the space after the colon,
  so `book1_entity_state` and `book1_final_chapter` were silently not keys at all) — fixed.
- **`tools/make_epub.py`** — the EPUB builder was copy-pasted into 17 book folders; 16 of
  them were byte-identical copies hardcoding Saeren metadata and dead absolute paths
  (`/home/user/The-Saeren-Chronicles/...`), so running the one in e.g. `books/the-gift/`
  would try to build Saeren Book One. Now one shared, config-driven tool
  (`<book>/delivery/ebook.yaml`, falling back to STATE.yaml, paths relative to the book).
  Verified against the shipped Saeren Book One EPUB: identical file set, spine length and
  metadata. The 16 dead copies are removed (git history keeps them); `books/saeren/make_epub.py`
  stays because the trilogy's production notes drive rebuilds through it.
- **`requirements.txt` + `.gitignore`** — declared deps, and ignore rules for `__pycache__`,
  key files and OS noise. Dropped two committed `.pyc` files.
- **`voice_wear_check.py` now ships in `books/_template/tools/`** — the template's own
  character-bible.md referenced it, but no new book got a copy. Genericized (it was already
  book-agnostic in logic) and seeded by `new-book.sh`, along with `delivery/ebook.yaml`.

Verified by building a clean fork from scratch (only `.claude/`, `docs/`, `tools/`, the two
templates) and running install → doctor → new-book → new-series → doctor end to end, plus
the doctor's failure paths (broken series-bible link exits 1).

Still open, surfaced by the doctor and left as your call: 23 books have no
`character-bible.md` (it needs an architect pass, not a file copy — docs/CHARACTER-BIBLE.md
has a retrofit procedure), and 3 have no `word_floor.manuscript_min_words`.

## Outstanding manual steps (owner: Terry)

1. **Delete old branches** on The-Saeren-Chronicles (15), Apathetic-Love (1), The-Manipulators (1)
   — via GitHub website or local terminal.
2. **Apathetic-Love:** set default branch to `main` before deleting its branch.
3. **Archive the 14 original standalone book repos** (Settings → Danger Zone → Archive) once you
   trust this consolidated repo. Content is fully copied here — archiving is lossless.
4. ~~Rename provisional OCR-story folders to real titles~~ — DONE 2026-07-14 (all folders now
   carry final title-based slugs).
