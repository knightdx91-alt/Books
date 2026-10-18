# Entity changelog: *The Hour of Ash*

Each entry is one entity-tracker run against `ENTITY_STATE.yaml`. Newest last.

---

## 2026-10-18: UPDATE (plan re-sync, pre-writing, no chapters yet)

**Trigger:** the architect's patch pass on the outline audit (`evaluations/continuity/outline-audit.md` § RESOLUTIONS), STATE ARCH-4 (revised) and ARCH-14..18.
**Inputs re-read:** foundation.md, outline.md, character-bible.md (all patched); STATE.yaml.
**Meta:** `source: "outline (patched 2026-10-18)"`; `last_updated_chapter: 0`; `chapters_tracked: []`.

### Conflicts: 14/14 RESOLVED (C1–C14)
Each is marked in `meta.conflicts_index` with its decision. The affected field also carries `resolved_from_conflict: true` and `resolved_date`.
- C1 Grata's first appearance → Ch.19 · C2 the microcassette touch is added to Ch.35 · C3 the mime is on a street stage · C4 Ch.7 registers her as a dependent kinswoman (free, never property)
- C5 frame 36 → "may only be cloud" · C6 three breaks (Ch.6 plot-earned; Ch.20 and 22 unearned) · C7 she keeps hoping for an early door and does not give up home
- C8 AD 72 = ten years after the 62 quake · C9 five years from the frame to the trial · C10 Marcus b. autumn AD 64 (7 in Ch.16, 9 in Ch.22)
- C11 three heat scenes · C12 Theano names Pompeii in person, off duty · C13 Ch.27 = thirty-five years · C14 the rumor comes from Grata's husband

### Knowledge changes (47 character entries added or revised; 23 knowledge_index rows)
- **Mara:** effects-slip provenance (Ch.2); the suit's source, told by Valens (Ch.12); the god's answer with its second marker, plus Theano in person (Ch.13); the tomb found after a search (Ch.19); the summons via the brother's freedman (Ch.21); Fenn's tavern story, the opening lasting part of one night, the one-door-with-many-mouths law, openings lasting hours, his 71/73 failures and his rebuild around 79, the "estate sale" exchange (Ch.25); Valens following her to the tomb (Ch.30); the Greek conversation (Ch.33); Fenn saying "Margaret" (Ch.35); the tremor notes kept in Fenn's notebook (Ch.36); the boat-first plan (Ch.37).
- **Valens:** the suit, learned autumn AD 70 from the brother's freedman; the second marker (Ch.13); door + Pompeii, not the city's fate (Ch.15); belief, but no date (Ch.25); the tomb's location (Ch.30); the door might not take them (Ch.33); only the new facts in Ch.37.
- **Fenn:** knows 79 from school; the tavern story, then the door found shut; the 71/73 vigils; the doors-as-one belief; openings last hours; Mara has his notebook; his sister is dead, which he infers (Ch.25). knowledge_absent: her tremor notes, the native exclusion.
- **Others:** Theano (in person, off duty); Felix (told only that Mara fears the mountain; knows nothing of the door); Plautia (twice in three years since the divorce; the Pompeii address, summer 72); Celer (the witness, autumn 70; source unplanned); Grata (the summons at her counter; "the day after tomorrow"); Plautia's brother (Kirrha; the address).

### Other updates
- New tracked roles: `plautias-brothers-freedman` (needs_review), `temple-slave-delphi`. New location: `misenum`. New object: `ibuprofen` (closed Ch.13).
- Objects: 8 frames shot in 1998 / 28 rationed / four named frames (Ch.16, 20, 26, 27); frame 36 is rewound and removed, and the camera stays on the shelf. There is ONE notebook (Fenn's), with tremor notes in its back pages from Ch.20 (tremor-notes planted Ch.20, not Ch.36). Zippo and dime go through the door in Ch.43; the paperback stays on the shelf. The knucklebone passes from Lucius to Aelia in Ch.41. Grata's money is for "the day after tomorrow" (closed: she does not go). The chart stays in Philadelphia.
- World rules: "it" = all doors as one; openings last hours (62 = part of one night; 79 = from the night after the mountain opens until before first light); temperature sequence; monthly consultations; Achaea's "freedom" and the Celer re-dating; Junian Latin; single iudex; no nailed shoes.
- Plot threads: the backup-boat order (boat by day, door by night; Ch.37 = Ch.40); fenn-sisters-name opens in Ch.25; new `seventh-of-bysios-phrase` (2 planned uses); allowlisted phrases must work when absent (Ch.42, Ch.44).
- Teeth: goat-boy's teeth removed; Grata's teeth moved to Ch.31; the midwife is the only introduction-by-teeth.
- Plan gaps: 6 closed. Open: Mara's eye colour, hair and height (by design); how Celer learned of the witness in autumn 70; whether Felix knows Mara's origin.

### Flagged, not resolved (`meta.post_patch_flags`, UNRESOLVED)
- **P1** Ch.20 header sig `short-punch` vs ledger/beat `narrative`.
- **P2** Ch.7 subversion "grateful to be owned" vs kinswoman / never property.
- **P3** Ch.35 "waited for since he landed" and shareable #4 "thirty-four years for a door…" vs "waited for that door since 62".
- **P4** fate of Fenn's original tables in Ch.43.
- **P5** notice issued "within the month" of autumn 70, yet Valens is open in Ch.6 and reads it as new in Ch.9.

---

## 2026-10-18: UPDATE (chapter 1, finalized draft: post-polish, post-disruption)

**Trigger:** chapter loop step D.5, after book-disruptor on Ch.1.
**Inputs read:** `manuscript/chapters/chapter-1.md` (209 prose paragraphs), the existing `ENTITY_STATE.yaml` (plan-only, `last_updated_chapter: 0`), outline Ch.1–2, foundation §3, character-bible (Halloran, Szabo, Doug Fessler, Gloria, Pat, Ch.1 walk-on note).
**Meta:** `last_updated_chapter: 1`; `chapters_tracked: [1]`; `source` now says manuscript Ch.1 + outline for Ch.2–44; new `source_convention.paragraph_rule` (pYY counts non-empty lines, not counting the heading or `* * *`); new `meta.contradictions` block.

### Re-sourced from the plan to the prose (outline:ch-01 → ch-01:pYY)
Mara (first appearance, location log, Ch.1 knowledge, arc waypoint, relationships), Emilio, Halloran, Szabo, Margaret Fenn, the microcassette, the Seiko, the Pentax, the notebook, the chart, the permit, the Philadelphia facts, timeline row 1, the halloran-campania thread.

### Added (prose facts)
- **Characters (16):** named: `doug-fessler`, `gloria`, `pat`; mention-only: `maras-mother` (needs_review), `ray`, `tia-nilda`, `dorothy`, `carol`, `frank-registrar`; walk-ons: `dean`, `deans-office-woman`, `loading-dock-guard`, `cab-driver`, `nicosia-caller` (needs_review), `unnamed-woman-caller` (needs_review), `department-office-caller`.
- **Mara:** hair worn up in a knot with a pencil through it (colour, eyes and height still unset, so the plan gap stays OPEN as PARTIAL); the good black jacket, no coat, wet shoes; what she carries (cake, $11, checkbook, license, the house key); she is 26 in Dec 1991; conservator traits as shown; the father's phone number on the check; her deflections. 12 knowledge entries for Ch.1 (2 revised, 10 new).
- **Emilio:** digs (Cyprus: Paphos 1984, Kourion 1992; Sicily; Turkey); slides every September; Dick Francis; the porch; the greeting text verbatim (recorded c. Dec 1991); memorial on Sat 14 Mar 1998, 2 p.m.; death in January from three sources on the page.
- **Halloran:** the message verbatim; the permesso deadline of 20 April; the Soprintendenza; the fax number given only in part; six hours ahead.
- **Szabo:** "I. SZABO" on the window, "Mrs." in the narration; braid, magnifier, cardigan, gloves; Hungarian; the barber bet; the estate sale "last October"; she paid $800, asked $1,400, sold for $1,150; she holds the check with Emilio's number on it.
- **Locations (5):** `university-museum`, `szabo-shop`, `emilio-rowhouse` (off Baltimore Ave, 4th of 12), `nicosia`, `phoenix`. Also new Philadelphia facts: Spruce St, Pine & Tenth, the trolley and 33rd St, the Walnut St lawyer, the Free Library.
- **Objects (12):** `answering-machine`, `phillies-cigar-box`, `szabo-check` (chekhov_open, unplanned), `lemon-cake` (closed p182), `stapled-platter`, `dorothys-pyrex-dish`, `pats-blue-tupperware`, `overdue-library-book`, `kourion-drawings`, `dougs-duffel` (lost), `slide-carousel`, `cypriot-lamp`. Physical descriptions added to the chart (tre lune watermark, verdigris, the 38°31′N 22°32′E ballpoint, GOLFO DI LEPANTO / Castri), the notebook (black oilcloth, "A. J. FENN"), the microcassette, the Seiko (stopped at ten past four, nick at two o'clock) and the Pentax (empty chamber; put back on the shelf). The venetian-map status changes to `chekhov_open` (planned close Ch.3).
- **Organizations (3):** `soprintendenza`, `free-library-of-philadelphia`, `philadelphia-inquirer`.
- **Knowledge index:** new rows `emilio_death_1998` (the Nicosia caller has not heard) and `map_purchase_1998`; `margaret_fenn` and `fenn_identity` revised.
- **Timeline events:** 1687–88, 1890s Kastri, summer 1974/75, 1981, 1984, Dec 1991, 1992, Oct 1997, Thu 12 Mar 1998, Sat 14 Mar 1998.
- **Threads:** mending-the-seam gets a Ch.1 beat (the stapled platter); relics-microcassette and relics-watch are now `open`.

### Contradictions logged (`meta.contradictions`, UNRESOLVED; prose value recorded)
- **CH1-1 (low):** Halloran's deadline is "the twentieth of April" (p192). The character-bible sample line says "the first of June". The outline sets no date.
- **CH1-2 (low):** Szabo looks over a magnifier pushed up into her hair (p55), and Mara holds one corner of the chart (p74–75). The bible's physicality line says "glasses she is not wearing" and "weights a chart's corners".
- **CH1-3 (info):** the tracker's own earlier note said Fenn was "named by Szabo Ch.1". In the prose she calls him only "her brother", and his name appears only as "A. J. FENN" on the notebook cover. Note corrected.

No knowledge_gap. No other departures from the outline's Ch.1 beats.
