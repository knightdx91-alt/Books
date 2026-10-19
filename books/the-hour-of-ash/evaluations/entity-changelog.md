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

---

## 2026-10-18: UPDATE (chapter 2, final text: post-polish, post-disruption)

**Trigger:** chapter loop step D.5, after book-disruptor on Ch.2 (run 2; an earlier attempt was killed by a container restart before it wrote anything: `last_updated_chapter` still read 1 and there was no Ch.2 entry here).
**Inputs read:** `manuscript/chapters/chapter-2.md` (69 prose paragraphs, 6 scene breaks, 4,240 words), the existing `ENTITY_STATE.yaml` (`last_updated_chapter: 1`), outline Ch.2, character-bible (Halloran, Fenn, Margaret, the Ch.2 walk-ons note).
**Meta:** `last_updated_chapter: 2`; `chapters_tracked: [1, 2]`; paragraph rule now records Ch.2 = p1..p69; new `meta.revalidation_needed` block.

### Re-sourced from the plan to the prose (outline:ch-02 → ch-02:pYY)
Mara's five Ch.2 knowledge rows, her location log, possessions and arc waypoint; Fenn's first appearance, cold-air knowledge and arc waypoint; Margaret's Mexico trait and name usage; Halloran's location log; the microcassette, Pentax, film roll, Seiko, notebook, chart, flashlight, granola bars, ibuprofen and permit; the philadelphia and emilio-rowhouse facts (study, chart); timeline row 2 and the 1967/1968 events; the fenn-cautionary-mirror, mending-the-seam, relics-film-roll and halloran-campania threads.

### Added (prose facts)
- **Fenn's notebook:** eight entries, Thanksgiving 1967 → July 21, 1968:
  - the scholion via Father Kostas ("…the cave of the nymphs on Parnassus, and they are there")
  - the coordinates as written, 38° 31′ N, 22° 32′ E, and Margaret's question mark
  - the Plymouth sold; TWA to Athens on 2 April 1968; Margaret's "Mexico" cover
  - Delphi and the cave: four hours up, names scratched on the walls, "No books"
  - the slot: "cold in a way air isn't" for a minute or so, again one Tuesday, then nothing; "Slept up there"
  - June: boots, "Tired today."
  - the Herald Tribune bridge column
  - last entry: cold for "a whole cigarette"; going in on 22 July with a flashlight and kite string; "Back before Labor Day"

  Also recorded: the hand-change (capitals pressed through until April; a small leaning hand from May); the back half blank (sixty-odd leaves); the stuck back board, humidified; the consulate carbon (16 Sept 1968; overcoat "with contents of pockets"; "Pennsylvania" mistyped and x'd out).
- **Mara (17 knowledge rows: 5 re-sourced, 12 new; 11 traits):**
  - Days: the North African lamp, rejoined twice to an invisible seam; the Leipzig 1838 volume in the stacks (slit only to the scholion; the sunflower-seed boy).
  - The Seiko: three links out on Sansom Street ($8; her throat shuts over it).
  - Halloran's call (Sat 28 Mar): *Firma mancante*, then the laughing fit; the heir's declaration, signed 1 Apr and faxed; the 20 April deadline met by fax, outcome not stated; the north-transect notebooks wanted by the end of June; the 6 July invitation "in Emilio's place"; her answer, "I might be in Greece."
  - The chart: matted and pinned, Sat 4 Apr. Her father's notebooks: left unopened.
  - The decision, made while flossing: Tue 5 May, Olympic from JFK for Tue 19 May. Gloria's call (via Pat; "Till the ninth of June").
  - Belief about Fenn: does not believe the scholion; puts the cold down to caves breathing; draws no conclusion about his fate.
- **Packing:** Pentax loaded Sun 17 May, Kodak, 36 frames, **0 shot**, counter at 1 (packing implied). Seiko on her wrist. Microcassette in a gray wool sock in a hiking-boot toe. Notebook last, on top. Flashlight, two boxes of granola bars, a bottle of Advil, toothbrush, floss (packed before the passport). The chart stays. No flash is mentioned.
- **Characters (10):** `father-kostas`, `goat-boy-1968` and `goat-boys-mother-1968` (both needs_review; kept separate from the AD 70 goat-boy), `hallorans-wife`, `naples-new-tenants`, `sansom-street-jeweler`, `check-cashing-notary`, `olympic-airways-agent`, `sunflower-seed-boy`, `maras-department-head`. Halloran, Gloria, Pat, Ray, Dorothy, Emilio and Margaret extended.
- **Locations (4):** `maras-apartment`, `university-library`, `delphi-modern`, `athens`. Facts added to the corycian-cave (1968 walls, the slot, the breaths; 4 h from the village), the lab, the rowhouse study/kitchen/porch, and Naples (Halloran's flat; the 6 July season).
- **Objects (9):** `consulate-effects-slip`, `leipzig-scholia-volume`, `seiko-band-links`, `maras-duffel` (contents listed), `toothbrush-and-floss`, `maras-passport`, `olympic-booking`, `emilio-field-notebooks` (chekhov_open, unplanned: Halloran's request), `north-african-lamp` (closed p9).
- **Organizations (3):** `us-consulate-athens`, `olympic-airways`, `twa`. The Soprintendenza, the museum and the Inquirer extended.
- **Knowledge index:** new `cave_coordinates`, `mara_greece_trip`, `fenn_fate_1998`; `margaret_fenn` and `fenn_identity` updated.
- **Threads:** new `emilio-north-transect-notebooks` (open errand) and `maras-stated-return` (9 June). relics-film-roll is now `open`.
- **World rules:** Fenn's observed 1968 breaths recorded neutrally (their relation to the opening-duration rule is not stated on the page).

### Contradictions
- **CH1-1 RESOLVED:** Ch.2 keeps 20 April, and the bible's sample line now says the same.
- **CH2-1 (low):** plan "might be in Greece *first*"; prose "I might be in Greece." Halloran hears a holiday.
- **CH2-2 (info):** plan "no flash unit" in the Ch.2 packing; prose silent.
- **CH2-3 (low):** plan "the notebook came home in his coat"; the carbon says only "overcoat … with contents of pockets", and there is no shepherd.
- **CH2-4 (info):** plan "eight weeks"; prose about nine weeks and three days (14 Mar → 18/19 May).
- **CH2-5 (info):** the bible's Ch.2 addenda paraphrase loosely ("you'll practically be next door", "only beeps", "after BIBLIOTHECA", "taps").
- **CH2-6 (info):** the Pentax is loaded, but its packing is only implied.

### Flagged for the orchestrator
`meta.revalidation_needed`: chapter-1.md now has 193 paragraphs, against the 209 tracked, so the ch-01:pYY sources are offset. Revision cycle 1 cut facts still recorded here (see its § "ENTITY_STATE facts changed"). Chapter 1 was also written again during this run. Run UPDATE on chapter 1.

No knowledge_gap. Halloran's knowledge is "might be in Greece" only, with no date and no reason.

---

## 2026-10-18: UPDATE (re-sync after editor passes, Ch.1 + Ch.2)

**Trigger:** chapter-1.md had two gesture trims and chapter-2.md had polish cycle 1 (`revision-chapter-2-cycle1.md`), both after their last entity update. An earlier attempt at this re-sync was killed by a container restart before it wrote anything (no entry here; YAML unchanged), so this run did the full re-sync.
**Inputs re-read:** `chapter-1.md` (193 paragraphs) and `chapter-2.md` (69 paragraphs) as they stand now; revision-chapter-1-cycle1.md § "ENTITY_STATE facts changed"; revision-chapter-2-cycle1.md; the a7d8aea gesture-trim diff; outline Ch.2; character-bible (Szabo, Halloran, Ch.2 addenda).
**Meta:** `last_updated_chapter: 2` (unchanged); `chapters_tracked: [1, 2]`; `revalidation_needed` items for Ch.1 and Ch.2 are now RESOLVED; the paragraph rule records Ch.1 = p1..p193.

### Citations re-anchored
- **Ch.1:** 491 of 554 `ch-01:pYY` citations renumbered by content, from the old 209-paragraph draft to the current file. They now run from a 0 offset at the start of the chapter to −16 from the old p131 on. Bare in-text refs (p194→p178, p157→p141, p182→p166, p195-p203→p179-p187, and the others) are fixed too. The source for Szabo's Hungarian was wrong (p63) and now points to p134.
- **Ch.2:** the numbering is stable at 69 paragraphs. Every citation was checked against the current text. The notebook-packing sentence moved from p65 to p67. Three earlier mis-citations that had used manuscript line numbers are corrected: hands p17→p7, seam test p21→p9 (in two places), and the notebook hand p41→p12. The Mara belief source moves from p67 to p66.

### Facts removed (no longer on the page)
- **Ch.1:**
  - The dean's-office woman's fire-department bill.
  - The cab driver's rosebushes and Jersey mulch.
  - The guard's "Nobody finds one in this". He now says "You won't, in this."
  - The carousel's empty white square.
  - The lilies' "tall white spray, stamens nipped".
  - Arroz con pollo and the classroom-wing screen.
  - The Hogarth restrike and the 1796 map. A Hogarth still hangs in the shop.
  - The magnifier taken out and laid on the ledger, and the tissue lift.
  - The cassette turned over and the watch picked up. No YAML entries recorded these.
  - The all-or-nothing quote "There was no staying a little…". The trait is re-sourced to p11.
  - "Jacket wet through … dark at the cuffs".
  - The cigar-box label "faded to weak-tea brown".
  - "On her wrist" for the Acme sack.
  - The Halloran message text now reads "The Soprintendenza want another name on it".
- **Ch.2:**
  - At the jeweler: the telephone, the ten on the glass, the change left behind, and her eyes and throat.
  - The laugh's slide down the cabinet door. She now stays on her feet.
  - "Said so to the kitchen".
  - The notebook put back on its tobacco crumbs. The cigar box is no longer mentioned in Ch.2, so it was last mentioned at ch-01:p193.
  - The Leipzig volume put back "where it lived".
  - "Did not go looking for [the passport] until the week I left".
  - "Or Mrs. Szabo's seven".
  - "Nobody finds the books…" is now "You don't find the books…".
  - "A minute or so" is now "about a minute", corrected in 6 places.
  - "Gray" wool sock, and "cartridge", which is now "roll".
  - Halloran's room "nobody's been given" is now "standing empty".
  - The thumbnail along the spines is now a finger. "Then or on later Saturdays" is gone.

### Facts added
- **Fenn's coordinate source:** "the Army map down at the Free Library puts the cave up the mountain from" Castri. Fenn's knowledge method changes from inferred (from the chart) to discovered. This updates his knowledge, Mara's knowledge, cave_coordinates, the venetian-map ink, the Free Library location and organization, and Fenn's 1967 location log.
- **The chart's doorway drawing:** it is Fenn's "little picture of the cave mouth beside it so I'd know which hole I meant", tied to ch-01:p78.
- **The jeweler:** the Daily News crossword in ink, and humming a show tune he can't get the middle of. **The department head:** signs against a seed catalogue and asks whether the Greeks grow a decent tomato. This is a new knowledge row: he knows she is going to Greece.
- **The jeweler scene's new ending:** the watch "snug against my wristbone for the first time", with the envelope "in my pocket beside the tape". This adds a new microcassette touch at ch-02:p16.
- **Smaller additions:** the laugh as "a bark first … bent me over the sink"; the cereal box knocked off the drainboard; Halloran's "as if I'd said Florida", "clicked twice, somewhere under the ocean" and "went round his bare room"; the watch "rode down onto the back of my hand"; the chart "perforated all along its green edge"; Szabo underlining the surname.

### Contradictions
- **CH2-1..CH2-6: all still OPEN.** The revised text and the plan documents still disagree in every case:
  - CH2-1: no "first" in the prose; outline.md:163 still has it.
  - CH2-2: still no flash on the page.
  - CH2-3: the carbon text is unchanged and there is no shepherd.
  - CH2-4: the span is still about nine weeks and three days, against "Over eight weeks".
  - CH2-5: the bible still paraphrases ("only beeps", "practically be next door", "after BIBLIOTHECA", "taps").
  - CH2-6: Pentax packing is still only implied, now by p67.
- **CH1-1:** stays RESOLVED, re-anchored to p176 (line 359). **CH1-2:** still OPEN; the bible's physicality line is unchanged, and the magnifier is now used only once, at p52. **CH1-3:** still OPEN (info); re-quoted as "That is the brother. Treasure hunter." (p90).
- No new contradictions. foundation:§9's "Fenn's coordinates on a 1680s Venetian chart" is compatible with the Army-map source. No knowledge_gap.

---

## 2026-10-18: UPDATE (chapter 3, final text: post-polish, post-disruption)

**Trigger:** chapter loop step D.5, after book-disruptor on Ch.3.
**Inputs read:** `manuscript/chapters/chapter-3.md` (91 prose paragraphs, no scene breaks, 6,817 words), the existing `ENTITY_STATE.yaml` (`last_updated_chapter: 2`), outline Ch.3–4, foundation §4f/§9/§10, character-bible (the Ch.3 walk-ons note).
**Meta:** `last_updated_chapter: 3`; `chapters_tracked: [1, 2, 3]`; the paragraph rule records Ch.3 = p1..p91. Ch.1 (193) and Ch.2 (69) paragraph counts re-checked; both unchanged.

### Re-sourced from the plan to the prose (outline:ch-03 → ch-03:pYY)
Mara's Ch.3 location log, arc waypoint and knowledge; the knucklebone (introduced ch-03:p62); the Pentax Ch.3 beat; the hand-at-threshold Ch.3 occurrence; the corycian-cave facts (first chamber, stalagmites, graffiti, the crack, the missing blaze); the kalivia-plateau facts; timeline row 3; the-door-and-the-choice (now `open`); relics-knucklebone (now `open`).

### Added (prose facts)
- **Route:** Delphi (room over a worry-bead shop, given up at 7) → a taxi out of Arachova to the end of the asphalt (a little after nine) → the red-square path above the plain the map calls Livadi (Kalivia huts, tin roofs, a white church, ski lifts idle) → goats and goatherd → the herringbone pen with a bedspring hinge → the firs (the German) → zigzags → the last paint boulder → the mouth (fire ring, candle stub, the ΝΥΜΦ/ΠΑΝ inscription) → the first chamber (the slumped stalagmite; graffiti from the 1840s to a 1996 felt-tip heart) → the flowstone → the slab and the vertical crack.
- **Characters (5):**
  - `german-hiker`: about 65; red windbreaker; a stone from Liakoura for his daughter in Ulm; his wife in Arachova; an Olympus. He knows: American, Philadelphia, fixes pots, staying up, mother in Phoenix.
  - `goatherd-1998`: the brown nanny on the ledge; "Kalimera".
  - `arachova-taxi-driver`.
  - Mentioned only: `delphi-hotel-desk-woman`, `delphi-museum-guard`.
- **Mara:**
  - 13 knowledge rows (learned_chapter 3). The planned row "the cave door is real" is replaced (CH3-7).
  - 12 traits: reads French; ten years in the lab; her father's framing and lens-cap habits; the sherd shoebox; memories of 1977, 1989 and the cellar dark at seven; Gloria not called.
  - What she wore and carried in Ch.3; `knowledge_absent_ch3` (the year; any conclusion about a door).
- **Crossing:**
  - The cold at 1:40: dry, edged, her breath visible, the drip thinning, the bells gone, ear pressure.
  - Inside the crack: the blush.
  - She backs out: cave air again, nothing from the crack.
  - At the exit: low gold-orange light, the lit half of the plateau gone brown, a chill, woodsmoke, fresh dung; the blaze gone under lichen.
  - "October" is recorded as her inference.
- **Objects:**
  - New: `walkers-map-parnassus`, `charioteer-postcard`, `sherd-shoebox`, `germans-summit-stone`, `germans-olympus-camera`.
  - Knucklebone: physical description, find spot, in her pocket, intends to hand it in.
  - Seiko: RUNNING (wound that morning; 12:20, 12:30, 1:40, then 1:50 under a low sun; its luminous dots are dead).
  - Fenn's notebook: in her jacket.
  - Lens cap: in her jacket pocket. Its status changes from lost to background; the loss stays planned for Ch.12.
  - Venetian map: `chekhov_closed`.
  - Duffel: contents and use. Flashlight, granola bars and Advil touched.
- **Film:**
  - Delphi stadium, "a little of the roll" (count unstated).
  - Six frames on the page: the plateau; the pen's join (two frames); Mara, shot by the German; the cave arch; the inscription.
  - Total by the exit is at least 7, and 8 only if Delphi took 2. The counter is not mentioned. Indeterminate, not a contradiction.
- **Locations / organizations:** new `arachova`, `french-excavators`, `delphi-ephorate`. Ch.3 facts added to parnassus, delphi-modern, philadelphia, the museum lab, the rowhouse (crawlspace, cellar), maras-apartment and university-library.
- **Knowledge index:** new `crossing_1998` (nobody in Philadelphia knows where she went). Rows added to cave_coordinates, mara_greece_trip and fenn_fate_1998.
- **Threads and world rules:**
  - Threads with Ch.3 beats: hand-at-threshold (first instance), mending-the-seam (the bedspring pen), fenn-cautionary-mirror, maras-stated-return.
  - World rules, observed: what the door felt like; the ancient knucklebone passing in the 1998 → past direction (past → modern still not established); the watch keeping 1998 time.

### Contradictions
- **CH2-2 RESOLVED:** "The camera had no flash" (p64).
- **CH2-6 RESOLVED:** the Pentax is in the duffel's end pocket (p6).
- **CH2-5:** extended. The bible still gives the jeweler a telephone, which was cut in polish.
- **CH3-1 (low):** p78 says Fenn felt the cigarette-length cold and then "come back on Tuesday". In Ch.2 the Tuesday came weeks earlier, and after the cigarette he was going in the next day (Monday).
- **CH3-2 (info):** Fenn's drawn doorway is "smaller than a lentil" (Ch.3) but "the size of my littlest fingernail" in Ch.1.
- **CH3-3 (low):** the plan's 1998 refuge hut is not on the page. The 1998 structure is already a shepherd's pen, so Ch.4's "refuge hut is now a pen" has no antecedent.
- **CH3-4 (info):** the bible gives the goatherd a mobile phone. The prose has none.
- **CH3-5 (info):** "October" is named where the plan says "the wrong season". It is inside the plan's autumn and is recorded as her inference.
- **CH3-6 (info):** the microcassette is not mentioned. Its Ch.2 hiding place was a sock in a boot toe, and she is wearing boots in Ch.3.
- **CH3-7 (info):** the tracker's planned knowledge row "door is real" is replaced. She draws no conclusion on the page.

No knowledge_gap.

---

## 2026-10-18: UPDATE (re-sync of Ch.3 after the editor pass)

**Trigger:** polish cycle 1 (run 2) on Ch.3, `evaluations/revision-chapter-3-cycle1.md`, edited the chapter after its entity update.
**Inputs re-read:** `manuscript/chapters/chapter-3.md` as it stands now (90 paragraphs, 6,834 words, no scene breaks); the revision report; character-bible.md (goatherd card); outline.md (Ch.4 beat 4, Ch.5 beat 6); chapter-1.md line 159.
**Meta:** `last_updated_chapter: 3` (unchanged); `chapters_tracked: [1, 2, 3]`; `paragraph_rule` now says Ch.3 = p1..p90; new `revalidation_needed` entry for chapter 3 (RESOLVED).

### Re-anchoring
- The one-line paragraph "Then I went in." (old p56) is folded into p55. Old p57..p91 are now p56..p90, and p1..p55 keep their numbers.
- 251 `ch-03:pYY` citations re-anchored. Bare p-refs on Ch.3 lines and two manuscript-line refs (157 → 155, 183 → 181) were also re-anchored. Every quoted phrase was checked against its cited paragraph, and none is misplaced.

### Facts removed (no longer on the page)
- Her ears going hot at the theft, and the bag swinging against her hip (old p66).
- At the slot: "the watch case went cold … against my wristbone", "It was not cave cold", and the beam that "did not shake". The beam now "shook on the rock" (p76).
- The crack "as wide as a narrow door turned on its side" at knee height.
- The slumped stalagmite's parking-space size. The last-paint boulder "as broad as a car's hood" is now "a kitchen table" (p53).
- "dishwater gray" (now "pale gray", p8). The snow's "sink-white" colour (now just "streaked with old snow", p50).
- "tens of thousands" of knucklebones. The prose now says "more than twenty thousand", "dyed or drilled through, and a few filled with lead" (p60).
- The cellar memory's September is now **July** (p70), in the Mara trait, the Emilio trait, the relationship note and the history event.
- The pen photo's "in a way I could not have explained" (now "than with anything I had taken in Delphi", p14).

### Facts added
- **Microcassette:** in its sock, down among her clothes in the duffel, "since I laced the boots on at home". She touches it without comment while groping for a granola bar (p69). It crosses in the duffel. Added as a new `touches` row and `location_end_ch3`; `last_mentioned_manuscript` is now ch-03:p69. Mara's carried items, the duffel's contents and the boots (now known to be the packed hiking boots) are updated.
- **Slot mechanics:** the crack is forearm-wide at shoulder height, pinches shut above, and is "a good foot and a half" across at the floor; past the bend, "the beam ran on into black" (p67). She "sank onto my knees and went in sideways", back to the slab, and "knelt in the nothing" (p79). She backs out on her knees and is "upright" again in the hall (p83). Updated in Mara's knowledge, `corycian-cave` facts, the location log, the duffel, and world rule ch3_observed.
- **Autumn evidence:** at the mouth, the summit gullies are now bare gray rock "where the snow had lain that morning", and "the thyme was over, every flower head dried to a brown husk" (p88). These are recorded as the `basis` of her "October" inference, together with the low orange light (p86), the browned plateau, the chill and woodsmoke (p88), and the lichened boulder (p89). They are added to `kalivia-plateau`, `parnassus`, `corycian-cave`, the timeline row and the knowledge index.
- **Other wording:** the blush is now "of a kind I had thought I was too old for" (p81). At the slot, "Under my cuff the steel of the watch took the cold and held it" (p76), recorded under Seiko and Mara/worn.

### Contradictions
- **CH3-1 (low): still open.** The p77 sentence is unchanged.
- **CH3-2 (info): still open.** "lentil" (p51) vs "littlest fingernail" (ch-01 line 159). Both are unchanged.
- **CH3-3 (low): still open.** There is still no refuge hut on the page, and outline.md:222 still has one.
- **CH3-4: RESOLVED.** The phone is gone from the prose, and he is cursing a nanny goat (p10, p13). character-bible.md l.535-540 already says "cursing a nanny goat on a ledge" and marks the phone beat as cut. Any further bible edit must keep that wording.
- **CH3-5: RESOLVED.** The page now gives the evidence for "October" (p86-p89). It stays her inference and agrees with the plan's autumn.
- **CH3-6: RESOLVED.** The microcassette is located (p69) and matches outline Ch.5 "touched in its sock".
- **CH3-7 (info): still open.** She kneels in and reads more autumn signs, but she still names no door, crossing or year.

No new conflicts. No knowledge_gap. No needs_review.

---

## 2026-10-19: UPDATE (chapter 4, final text: post-polish, post-disruption)

**Trigger:** loop step D.5 (drift policy: every chapter).
**Inputs:** `manuscript/chapters/chapter-4.md` as it stands (83 paragraphs, 7 breaks = 8 shards, 1,869 prose words); outline.md Ch.4; character-bible.md (Ch.4 walk-on note); outline-audit.md N-23; Ch.3 for cross-checks.
**Meta:** `last_updated_chapter: 4`; `chapters_tracked: [1, 2, 3, 4]`; `paragraph_rule` gives the Ch.4 shard ranges.

### Entries added
- **Characters:** `kleodamos` (mentioned only: the boy's archon, not a dating clue). The `goat-boy` card is rebuilt from the prose:
  - "nine, perhaps": tunic, sling, bag, stick, crust, one ear, saddle-hard soles.
  - Every transliterated word on the page; *nymphē* three times (Nümfi x2, Nymphē on the third).
  - Physical traits: the spit, the rubbed-out ΔΕΛΦΟΙ, the laugh, the thorn.
  - Seven knowledge rows. He is still unnamed. "Phocian" is the plan's label, because the page does not name the dialect.
- **Mara:**
  - Aliases *nymphē* (now sourced to the prose) and "Mára".
  - `worn_ch4` (jeans, fleece), `carries_ch4` and `hunger_ch4`.
  - Nine Ch.4 traits.
  - A goat-boy relationship.
  - Seven `learned_chapter: 4` knowledge rows: book Greek a liability; *nymphē*; autumn evidence and Boathoos; Kleodamos and "Késar … En Rhōmē"; what she sees (fresh inscription, unbroken pen, no road); "Delphous … Makran"; a belief row.
  - `knowledge_absent_ch4`: the YEAR, which Kaisar, the boy's name, what *nymphē* means. Also a location-log row and an arc waypoint.
- **Objects:**
  - New `granola-foil-wrapper` (kept by the boy, down his tunic).
  - `granola-bar`: one two-bar pouch eaten (he spits his out; she eats both). Count left NOT STATED.
  - `corycian-knucklebone`: Ch.4 beat; left hand.
  - `microcassette`: touch, "beside the sock".
  - `maras-duffel`: sweater first named; not mentioned after p43.
  - `walkers-map`: recalled.
  - Pentax: no frames (`frames_shot_ch4: 0`; 28 remain, per the plan). Seiko: not mentioned.
- **Locations:**
  - Kalivia: AD 70 goat track, the pen whole, brush-roofed huts, grass where the road was, bare ridge.
  - Corycian Cave: ΝΥΜΦΑΙΣ / ΠΑΝΙ fresh with red paint; lamp and three knucklebones on the ledge.
  - Also Parnassus (descent), Delphi distance ("Makran"), Rome (a Kaisar), and Philadelphia (the Wawa).
- **Timeline:** the Ch.4 row (first hour, late sun to dusk, autumn, year NOT known to Mara) and one event row. **Index:** new `the_year`; the goat-boy row in `mara_origin` is now sourced to the prose. **Threads/rules:** relics-knucklebone, mending-the-seam (`ch4_note`), and the dates rule (`ch4_observed`).

### Contradictions
- **CH3-3: still open.** Ch.4 reuses the Ch.3 pen, unbroken, and there is no hut by the path. The outline still says "refuge hut" (l.222) and "a stone hut" (l.213).
- **CH3-7: still open.** Her questions presume antiquity, but the narration names no door, crossing or year.
- **CH4-1 (info):** the knucklebone is touched in Ch.4. The plan leaves it absent for Ch.4–25.
- **CH4-2 (info):** in Ch.4 a pouch holds "two bars, as there always were". Ch.3 counts single bars.
- **CH4-3 (info):** the garment is "fleece" in Ch.4 but "jacket" in Ch.3.
- **CH4-4 (info):** the inscription reads ΠΑΝΙ in AD 70 (Ch.4) but ΠΑΝ "very clear" in 1998 (Ch.3).
- **CH4-5 (info):** on the way down there is no fir belt between the mouth and the pen (Ch.3 had firs above the pen). The "slab behind" the pen is new.

The year stays unknown to Mara. No knowledge_gap. No needs_review.

---

## 2026-10-19: UPDATE (re-sync after the Ch.4 editor pass, polish cycle 1)

**Trigger:** `evaluations/revision-chapter-4-cycle1.md` edited chapter 4 after its entity update.
**Inputs re-read:** `manuscript/chapters/chapter-4.md` as it stands now (83 paragraphs, 7 breaks = 8 shards, 1,803 prose words / wc -w 1,832); the revision report; character-bible.md (Ch.4 walk-on block: Kleodamos clarified); chapter-3.md p14-p15 and p84 for cross-checks.
**Meta:** `last_updated_chapter: 4` (unchanged); `chapters_tracked: [1, 2, 3, 4]`; `paragraph_rule` updated; new `revalidation_needed` entry for chapter 4 (RESOLVED).

### Re-anchoring
- All edits fall inside paragraphs. The paragraph count and shard ranges are unchanged (p1-p2, p3-p12, p13-p35, p36-p42, p43-p58, p59-p62, p63-p73, p74-p83), so every `ch-04:pYY` keeps its number. All 343 Ch.4 citations were checked by content, and each quoted phrase was checked against its cited paragraph.
- Fixes: the goat-boy's cat-and-sofa trait was cited to p9; it is p3. The citations to p5 for the jeans and the duffel are dropped, because p5 now reads only "His eyes came to my face and stayed." Sources were completed where a quote's paragraph was missing (p9 "Khaire"; p75 "Delphous"; p79 "What is your name?"; p83 "Nymphē"). The file now has 354 Ch.4 citations.

### Facts removed (no longer on the page)
- **Knucklebone:** her left hand "shut on mine" (p28). Her bone is not mentioned anywhere in Ch.4. The ledge's three offered knucklebones stay. `last_mentioned_manuscript` → ch-03:p84.
- **Mara's clothes and bag:** the boy's eyes going to her jeans and "over the duffel" (p5). Jeans are no longer in `worn_ch4`.
- **The goat-boy:**
  - He no longer wipes his nose on his wrist (p80).
  - He no longer laughs "until he coughed, a hoarse little bark" (p34).
  - He no longer gives the name "with enormous patience" (p22).
- **Wording:**
  - "black and brown and dirty white" goats (p2).
  - "the color and hardness of a saddle" (p73).
  - "the last of the sun" (p56).
- **Descent:** "At the edge of the firs" and the stick pointed "downhill between the trunks" (p74).
- **Mara's doubled lines:**
  - "Out of the cave. I came out of the cave."
  - "Alone. I am alone."
  - "From the west. From beyond…"
  - "Your name. What is your name?"

### Facts added or corrected
- **Descent order:** cave → "Past the firs a pen stood where the pen had stood that morning" (p61) → "more firs" across the plain, a different stand (p62) → halfway (p68) → "At the foot of the slope he stopped, took me by the sleeve, and turned me toward the dark gap" (p74). Updated in Mara's location log, the goat-boy's location log and relationship, kalivia-plateau, parnassus, corycian-cave, the delphi distance, the timeline row, the history event and the pen thread note.
- **The goats:** "a few dozen, with burrs in their coats" (p2). Ch.4 gives no colours.
- **The laugh:** "his mouth fell open… laughed in high hiccups, like a much smaller child" (p34).
- **The sole of his foot:** "as hard as saddle leather" (p73).
- **The low sun:** on the foil wrapper (p56).
- **Recognition beat (p8):** his speech slides past her "all but the case endings. I knew those from my grammars, and I had only ever heard them in my own voice." Added as a new Mara knowledge row (discovered) and added to her Greek trait. "That one I heard whole" (p76).
- **The last "Nymphē." is the boy's:** p82 ends "his voice came down on an eta". Recorded on the nymphē alias and the knowledge row.
- **Kissa:** "And to Kissa, in the same breath, 'Sitta! Sitta, íkade.'" (p78). The page still does not say what Kissa is.
- **The boy's words are now spelled as sound** (`words_on_page` rewritten): ílthes, Móni í?, thélis, Mí! Mí gráfe, Ti dósis, Káki, En Rómi, íkade. Every "En Rhōmē" in the file is now "En Rómi".
- **Kleodamos:** the page gives only the archon's name. The boy frowns at "Archon" and gives the name (p21-p22, p25). The note carries the bible's clarification: not the pen's owner, not the boy's father, not a dating clue.

### Contradictions
- **CH4-1: RESOLVED.** The hand-on-bone sentence is cut, so the knucklebone is absent in Ch.4, as the plan has it.
- **CH4-5: RESOLVED.** The firs now come before the pen on the way down, which matches ch-03:p15. The pen's "slab behind it" is still a new detail, but it is not part of the order question.
- **CH3-3 (low): still open.** Ch.4 still has a pen and no hut; outline.md:213 and :222 still have the hut.
- **CH3-7 (info): still open.** The new case-endings beat draws no conclusion. No door, crossing or year is named.
- **CH4-2 (info): still open.** p43 still says "Two bars … as there always were".
- **CH4-3 (info): still open.** p50 and p80 still say "fleece". The editor suggests "fleece jacket"; that is not decided here.
- **CH4-4 (info): still open.** The ΠΑΝΙ / ΠΑΝ wording is unchanged.

No new conflicts. No knowledge_gap. No needs_review.
