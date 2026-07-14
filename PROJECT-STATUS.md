# Books — project status & consolidation log

_Last updated: 2026-07-13._

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

## Outstanding manual steps (owner: Terry)

1. **Delete old branches** on The-Saeren-Chronicles (15), Apathetic-Love (1), The-Manipulators (1)
   — via GitHub website or local terminal.
2. **Apathetic-Love:** set default branch to `main` before deleting its branch.
3. **Archive the 14 original standalone book repos** (Settings → Danger Zone → Archive) once you
   trust this consolidated repo. Content is fully copied here — archiving is lossless.
4. ~~Rename provisional OCR-story folders to real titles~~ — DONE 2026-07-14 (all folders now
   carry final title-based slugs).
