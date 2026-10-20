# Outline audit — 2026-10-20

Scope: `project/outline.md` (Ch.1–4, 6–30, header, ledger, totals and summary sections), `project/foundation.md`,
`project/STYLE_CONSTRAINTS.md`. I checked each entry against the `STATE.yaml` decisions, the CLAUDE.md guardrails,
`Sygl_Complete.txt` and the approved Ch.1–4 manuscript. The Ch.5 entry was left byte-identical (md5 checked).
`manuscript/` was not touched. Nothing was committed.

## 1. Decision conflicts
- Ch.1: now records Fredrick's goodbye as an author-approved addition (lesser Sygldry school). Ch.2: the claiming
  is placed at the Heir's School.
- Ch.3: no cup; she cuts her wrist. Bal's pain tolerance is noted as written.
- Ch.4/6: no conflict with the Pierre decision. Ch.4 keeps "I will send Pierre for you in the morning".
- Dialogue rule: none of the three files said "verbatim". I added the BASE rule to the outline's binding rules
  and to foundation §7. I also fixed two "preserve almost verbatim" instructions in `project/baseline-evaluation.md`.
  The existing evaluation files only describe past results and were left as they are.
- Foundation: the war rules now cite Ch.21 for the no-help rule. Fredrick's and Pierre's cards are filled in.

## 2. Unsupported content
- Ch.17: the anchor showed the stones "going up and down while he answers". The source has him let them fall
  first (L763), so the anchor is fixed.
- Ch.18: "the only time the others see her storm power" was stated as fact. It now cites Lora's own line (Ch.23).
- Ch.20: "Viridia's village is safe" is now "should be left alone", as the source has it.
- Ch.25: "her hair gone still" during the toast was not in the source. I cut it, because it is the source's
  Ch.26 beat.
- Foundation: "keeps trying to settle things" is now "resolves… (once)".

## 3. Tic and echo risks
- Ch.22 anchor "map under Xavier's finger" repeated Ch.18's map under Fern's fingers. Ch.22's anchor is now
  Amelia's "No" / "Damn their war".
- Ch.8 anchor (fire and her face) leaned on "firelight in her eyes", which Ch.2 already used. It is now his
  hand taking hers.
- Tongue-out: the source gives it to both Amelia (p.24) and Viridia (p.35), which makes it a shared device. It
  is used for Amelia only (Ch.5). Ch.7 drops Viridia's tongue-out.
- Ch.12: Viridia's cough is flagged so it is not staged like the Ch.7 choke.
- Single-use list added to the outline, foundation and STYLE: softball, juggling, the flexed hand, the
  finger-snap and the hair are not to become signatures.
- Ch.25 was missing an Opening line, so one was added.

## 4. Citations
I verified every boundary. A `[Page N]` marker line opens page N. Fixes:
- Ch.1: L4–14 → L4–20 (the written chapter ends on "Hello?"). Ch.2: L14 → L22.
- Ch.6: ended on the marker L303 → L304.
- Ch.7/8 split at L325: Ch.7 now ends on the walk back. "I like her too / She'd do well" moves to Ch.8,
  which matches Ch.8's opening.
- Ch.22: L834 overlapped Ch.21 → L835.
- Ch.23/24: L870 is a marker → L871.
- Ch.28/29: the cut is at the coliseum.
- Ch.30: L1006 overlapped Ch.29 → L1007.
- Estimated pages: Ch.2 ~4–7, Ch.3 ~7–10, Ch.4 ~10–16, Ch.10 50–~55.
- Every shared line is named with its cut-point.

## 5. Ch.1–4 as written
- Entries are marked FINAL, with their source ranges, written Opening/Hook, and actual word counts.
- wc -w: 3,195 / 2,731 / 2,592 / 3,238 = **11,756** against 14,200 planned.

## 6. Totals
- The old sum of 91,800 was arithmetically correct.
- The new total is 11,756 (written) + 80,100 (Ch.5–30 targets) = **91,856**.
- The shortfall was spread to the chapters with the most source relative to their budgets: Ch.7 +400, Ch.9
  +400, Ch.13 +300, Ch.16 +400, Ch.22 +500, Ch.24 +500.
- Range is now 1,300–5,300. The shortest chapter is 1,300.
- Header, STYLE §6, `PROGRESS.md` and `STATE.yaml` phase.status are updated.

## 7. Internal consistency
- Ledger: Ch.1–3 are no longer three "single-scene" entries in a row, and Ch.18 now includes the water-snake job.
- Restored list: added the shirts finished, the water-snake job, the heart-ring payoff and the "We heard"
  confirmation.
- New list: "Author-approved additions".
- Removed list: added the cup, the Kona Niente slip, the tongue and the reused images.
- Protected anchors: added Ch.1–3.

## Open for the author
- Ch.7: is it acceptable to drop Viridia's stuck-out tongue (source p.35) to keep the device unshared?
- STATE says Ch.1–4 are 11,809 words; wc -w gives 11,756, so the counters differ. I did not change the
  STATE.yaml word_floor comment (≈91,400), the book CLAUDE.md (≈91,800) or the old 91,400 decision text.
- Ch.5 is being drafted at about 3,900 words against a 3,500 target. If it lands there, the total rises to
  about 92.3k.
