# Books — project status & consolidation log

_Last updated: 2026-07-13._

This repo is the consolidated home for all books + the shared writing pipeline. This file
records what's here, decisions made, and the manual steps still outstanding.

## What's in `books/`

**Migrated full books** (from their old standalone repos):
`the-gift`, `litrpg-josh`, `scale-and-silver`, `finding-lady-death`, `the-manipulators`,
`nanobot`, `shadow-god`, `multiverse`, `pompeii`, `the-long-goodnight`, `apathetic-love`,
`sygl-book`, plus two series: `saeren/` (3 books) and `land-of-the-guardians/` (Ne'veran,
4 books incl. scaffolded `the-dragon-isle` + `the-origin`).

**OCR / early-stage stories** (transcribed from handwritten pages this session; provisional
folder names — rename to real titles once decided):
`litrpg` (James Mason), `demon-academy` (Zack), `hazels-story`, `norse-story`,
`black-jewels-like-book`, `horror-story` (John Maxwell premise).

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

## Outstanding manual steps (owner: Terry)

1. **Delete old branches** on The-Saeren-Chronicles (15), Apathetic-Love (1), The-Manipulators (1)
   — via GitHub website or local terminal.
2. **Apathetic-Love:** set default branch to `main` before deleting its branch.
3. **Archive the 14 original standalone book repos** (Settings → Danger Zone → Archive) once you
   trust this consolidated repo. Content is fully copied here — archiving is lossless.
4. **Rename provisional OCR-story folders** to real titles once chosen.
