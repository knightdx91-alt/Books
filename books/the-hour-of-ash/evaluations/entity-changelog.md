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

---

## 2026-10-19: UPDATE (chapter 5, final text: post-polish, post-disruption)

**Trigger:** chapter loop step D.5 for chapter 5 (drift policy: every chapter).
**Inputs read:** `manuscript/chapters/chapter-5.md` (212 paragraphs, 4 breaks = 5 shards: p1-p21, p22-p73, p74-p93, p94-p206, p207-p212; wc -w 8,364); outline.md Ch.5 (and Ch.6 for the hand-off); foundation.md §3, §4f; character-bible.md (Kallia card and the Ch.5 walk-on block); chapter-3.md p3 and p76 for cross-checks.
**Meta:** `last_updated_chapter: 5`; `chapters_tracked: [1, 2, 3, 4, 5]`; `paragraph_rule` extended to Ch.5. 846 `ch-05:pYY` citations, all checked against p1..p212.

### Replaced (plan → prose)
- **Mara's location log, Ch.5:** sheepfold → the lip → the village where Arachova was → the valley road (olive harvest; the press) → the gymnasium track → the spring → the gateway → the Sacred Way → the temple → the market square → the spring at dark → the lane → Kallia's storeroom.
- **The year:** the planned knowledge row is replaced. Mara dates it "the autumn of the year seventy". The basis is Titus taking Jerusalem in late summer 70 (Josephus), news reaching Greece by sea in weeks, and the olives coming down. Ouespasianos = Vespasian. 1998 − 70 = 1,928 years. Her first step was at the Kroton base: after Nero's death in June 68, with the lead 2–3 years weathered. **Nothing about 79.**
- **The timeline row** for Ch.5 (day 2 in AD 70, after a night in a sheepfold). **Kallia's** `first_appearance` is now ch-05:p139. **Delphi** facts are confirmed or annotated.

### Added
- **Mara:**
  - `worn_ch5` / `carries_ch5`: fleece, jeans, boots, Seiko, duffel contents, the three taxi coins.
  - `marks_ch5`, the rod injuries: two welts on the right forearm, one split and bleeding; the wrist skinned at the watch band; the knee through the denim; a weeping place on the shoulder that sticks to the fleece; the hip. No fracture.
  - `hands_ch5`: scalpel scar on the left forefinger, acetone shine, a pen callus.
  - `teeth_ch5`: the upper-left filling, and Dr. Pinsky.
  - `hunger_ch5`.
  - 13 Ch.5 traits.
  - 27 knowledge rows, including the clay discs she cannot place, the missed Athenian treasury, the retouched molding, Kallia's name (overheard) and her terms.
  - `knowledge_absent_ch5`.
  - The Ch.5 arc waypoint.
  - Relationships: Kallia, the guide, the rod slave.
- **Kallia:**
  - Physical: about fifty; square brown face lined across the forehead; gray hair under a dark kerchief.
  - Her own moment: the Boeotians' garland flung out, and her feet washed under the overflow with her eyes shut.
  - Seven page traits. She never touches Mara and never asks her name.
  - Household: courtyard, pomegranate tree, gallery, Thebans, a singer, the girl who ran off at the vintage, the sieve neighbor.
  - Possessions: lamp, jar, sieve, blanket.
  - Knowledge, with the basis for "a possible runaway". `knowledge_absent` adds the content of Mara's English outburst, which she heard but did not understand.
- **Characters (21 new):**
  - On the road: olive-press-woman, olive-girl, pilgrim-family-with-kid.
  - On the Sacred Way: sacred-way-guide, rival-guide-in-green, water-boy, wool-seller.
  - At the temple: temple-warden-purple-stripe, temple-slave-with-rod (distinct from the Ch.13 slave).
  - In the square: delphi-herald, council-clerk, clay-figure-seller, fountain-men, procurer-at-dusk.
  - At Kallia's: sieve-neighbor, gallery-pilgrim, singer-upstairs.
  - Mentioned only: dr-pinsky, nero, vespasian, titus.
  - Kleodamos gets the herald's mention. The goat-boy gets his Ch.5 departure.
- **Locations (7 new):** castalian-spring (1998 dry niche / AD 70 lions), delphi-sacred-way, temple-of-apollo-delphi, delphi-market-square, kallias-house, descent-road-to-delphi, jerusalem.
  - Additions to existing locations: AD 70 Arachova; the plateau at night; 1998 Delphi recollections; Kirrha; Corinth; Rome; Philadelphia; the cave → Delphi distance.
- **Objects (6 new):**
  - taxi-drachma-coins: 3 → 2 left in her jeans; the 100-drachma piece goes into the guide's cloak.
  - pierced-clay-discs: chekhov_open, unplanned.
  - kroton-runner-base.
  - temple-rod.
  - kallias-sieve.
  - goat-hair-blanket.
- **Objects updated:**
  - Pentax: one frame, the empty Kroton base.
  - film-roll: running count. Plan 9 shot / 27 left; page at least 8 / at most 28.
  - Seiko: struck by the rod and still going; the luminous paint dead; ticking in the storeroom; not wound.
  - Microcassette: the planned touch at p211; location at the end of Ch.5.
  - Duffel: it came down the mountain.
  - Granola: one pouch eaten; count not stated.
  - Knucklebone: absent.
- **Threads:** maras-legal-nonexistence (opened), return-to-the-cave (opened → Ch.6), maras-greek-refusal (opened), kleodamos-archon (name only, no payoff); notes on mending-the-seam and the relics.
- **Timeline events:** Nero's death (June 68); the bronzes taken; Ch.5 day 2; the sacrifice "on the fourth day from now"; Dr. Pinsky (Feb 1998); the Josephus seminar.
- **World rules (observed):** the social side of a woman alone; temple purity and the altar rules; the sea still open.
- **Organizations:** delphic-sanctuary confirmed and extended; delphi-council added.
- **knowledge_index:** the_year (the row is now prose); mara_origin (Kallia; the guide); fenn_fate_1998. Mara calls the notebook's owner "a dead man", her first stated belief that he is dead.

### Contradictions
- **CH5-1 (info):** Kallia's house is up the road and down a lane from the spring, while the plan says "beside" it.
- **CH5-2 (info):** the character-bible's Ch.5 addenda paraphrase an earlier draft:
  - Kallia: "Who's coming after you?" (the prose has "Who saw you come down here?").
  - The sieve: lent "since the vintage" (the prose has "a month").
  - The slave: "three days of bread" (the prose has "stop it out of my bread").
  - The clay seller: "Since the singer" (the prose has "Since the bronzes were carted off").
- **CH5-3 (info):** a frame on the page (the Kroton base). The plan puts every unnamed antiquity frame off the page.
- **CH5-4 (info):** this is the 3rd contact with the microcassette sock on the page since the packing (Ch.3, Ch.4, Ch.5), not the 2nd.
- **CH5-5 (info):** p2 has the 1998 taxi going "east toward Arachova and … down". Ch.3 has it coming up from Arachova.
- **CH5-6 (info):** the Greek refusal begins at p65-p66, but Mara's replies to Kallia ("No." "Eggs." "Mine.") carry no language tag, and Kallia acts on "Mine."
- **Notes added to open items:**
  - CH3-3: still a pen, no hut.
  - CH3-7: she now has the year and the span, but still no "door".
  - CH4-2: the pouch is still the unit.
  - CH4-3: "fleece" ×6, no "jacket".
  - P5: the Corinth post reaches Delphi in weeks in autumn 70, which adds to the reward-notice gap.

No knowledge_gap. No needs_review (the rod slave is kept distinct from the Ch.13 temple slave, per the bible).

---

## 2026-10-19: UPDATE (re-sync after the Ch.5 editor pass, polish cycle 1 run 2 + finalize fixes N1-N7)

**Trigger:** `evaluations/revision-chapter-5-cycle1.md` edited chapter 5 after its entity update. While this run was underway, the finalize fixes N1-N7 landed in the same file (chapter-5.md last written 02:12:41). This entry is synced to that final text.
**Inputs re-read:** `manuscript/chapters/chapter-5.md` as it stands now (212 paragraphs, 4 breaks, wc -w 8,173); the revision report, including "Finalize fixes N1-N7"; character-bible.md (Kallia card l.189-230; Ch.5 walk-ons l.610-640); outline.md l.213, l.222, l.240-250; foundation.md §3; ch-03:p3, p5, p54, p69; ch-04:p28, p43.
**Meta:** `last_updated_chapter: 5` (unchanged); `chapters_tracked: [1, 2, 3, 4, 5]`; `mode`, `source` and `paragraph_rule` updated; new `revalidation_needed` entry for chapter 5 (RESOLVED).

### Re-anchoring
- The paragraph count is still 212, but the numbering shifted inside the chapter:
  - Old p1-p59 keep their numbers.
  - Old p60 is deleted ("His face lit with joy."), so old p61-p130 are now p60-p129.
  - New p130: "The herald had said the fourth day, I was nearly sure, and nothing about four oxen."
  - Old p131-p171 keep their numbers.
  - New p172: "She took that for a no, which it more or less was." So old p172-p209 are now p173-p210.
  - Old p210 (the boots and the fleece) and old p211 (the sock) are merged into p211.
  - p212 is unchanged.
- Shards: p1-p21, p22-p72, p73-p92, p93-p207, p208-p212.
- All Ch.5 citations were remapped (845 occurrences across 343 lines). Each was then checked by content, and every quoted phrase was checked against the paragraph it cites.
- Old mis-cites fixed: olive-paste hands p49 → p23; "my jeans" p5 → p4; "the backs of bottles" p11 → p5; the lodgers p207 → p211.
- Sources completed: p9 ("I am a foreigner and hungry"); p171 ("Eggs"); p197 ("Scrape it yourself").

### Facts removed (no longer on the page)
- **Injury aftermath (W-08):** "raised" and "red going purple"; the skinned wrist; "my knee had come through the denim". The blows during the beating (p88) still stand.
- **Seiko:** "The watch was going; I listened to it at my ear to be sure"; "its luminous paint was long dead and the hands were invisible". It is still struck (p88) and still running in the storeroom (p212).
- **Storeroom rummage (W-07):**
  - the route past the granola box and "the cold body of the Pentax";
  - "rolled tight" and "small flat weight";
  - boots set "side by side".
  - Granola and Pentax `last_mentioned_manuscript` moved back to p138 and p54.
- **"loved"** (W-02). Cycle 1's replacement, "with my whole chest full of it", was itself replaced by N5: "and wished the light would stay".
- **The guide:** the coin weighed and bitten twice; "a man of fifty" (age is now not stated); "Who asks that?"
- **Walk-on doubling:** "Salt!"; "Off! Off"; the slave's second "Look."
- **Herald:** "like grass under wind".
- **Similes and stock phrases:** "bright as a new penny"; "like a jigsaw puzzle".
- **Laughs:** the wool woman's laugh-fit on a statue base; the procurer's laugh.
- **Provenance lines:** "as I knew the Gettysburg Address" and "in Pausanias"; "Aristophanes".
- **Thumbnail on the chisel bites and on the lead.** The only thumbnail left is on the molding flake, p74.
- **Body-unit measures:** "fingernail-sized" flake; "shin height"; "clay women a hand high" (N6a).
- **Other wording:**
  - "square" face (now "broad");
  - "in exactly those words";
  - "smelled of wet stone";
  - "a house full of" (now "houseful");
  - "the cave by midday" (now "by noon").
- **Tags cut by N3/N4:** "She took the English for a no", "I said it in English. She had the tone of it, if not the word", and "\"Where are we going?\" I said, in English."

### Facts added or corrected
- **Taxi (p2):** "a taxi had brought me up from Arachova and across this plain on asphalt. At first light I set off back the way it had come, on foot, eastward". The repeated "no road" clause is gone. Updated in kalivia-plateau, arachova and CH5-5.
- **Flashlight (W-19):**
  - p1: "I found a wall with the flashlight, and a dog … went frantic at the beam until I put it out".
  - p208: it stays "somewhere in the bottom of the duffel … Kallia was not going to come back and find a light under her stairs that burned nothing".
  - Added to the flashlight object (`ch5_beat`; `last_mentioned_manuscript` → ch-05:p208), Mara's possessions, the duffel and her location log. The "not mentioned in Ch.5" row is corrected.
- **The sock (p211):** her right sock is soaked from the jar water. She reaches into the bag for a dry one, "and my hand closed on the sock and the hard little oblong in its toe. I let it be and drew out the sweater instead". This is the only Ch.5 touch. Dry socks are implied in the duffel.
- **Injuries (p93):** "two hot stripes across my right forearm, and the skin had split on one of them in a short line beaded with blood", and the back of the fleece "pulled at something underneath that had begun to stick".
- **Kallia's lodging (p183):** "A short way above the spring the road turned off between houses into a lane". Updated in kallias-house, delphi, household_ch5 and CH5-1.
- **Language of each reply to Kallia:**
  - Tagged English: p147-p148 ("She heard the English") and p161 ("In English").
  - Head-shake: p169, "I shook my head." (to "Weave?").
  - Untagged: "Eggs. I can do eggs." (p171; p172 "She took that for a no"), "Mine." (p177) and "Where are we going?" (p181).
  - No line of hers after p65 is Greek.
- **Herald and fountain:** "I could follow most of it" (p119). A new Mara knowledge row records her doubt about the four oxen (p130). Added to the delphi decree row and the fountain men.
- **Other wording now on the page:**
  - "clay women" (p23);
  - "planted himself" (p131);
  - "The question was finished before his look was" (p132);
  - "the flame under my chin" (p154);
  - "She let me finish" (p162);
  - the sieve is "my good one" (p187), and Kallia bangs on the door "with her fist" (p183) and goes "round the mesh with one finger" (p190);
  - the lead is scored "with the edge of a coin from my pocket" (p53);
  - the Kourion grains "under my lens like ground sugar" (p37);
  - the bull is "polished bright"; the wall is "fitted together in curving shapes";
  - the guide is "lean, bandy-legged";
  - the slave holds the rod "bent open in his two fists where it had split";
  - "the noise of the square sank under his voice";
  - "smelling of moss and cold water"; "The cold of it stopped my breath";
  - "the word that came to me for all of it was English: ugly".

### Contradictions
- **CH5-1: RESOLVED.** p183 puts the lodging "a short way above the spring". foundation ("by"), the bible ("near … a short walk above") and the page now carry one value.
- **CH5-5: RESOLVED.** The taxi now comes up from Arachova, which matches ch-03:p3 and p5.
- **CH5-2 (info): narrowed, still open.** All five original bible paraphrases now quote the prose. What remains: the bible's Kallia card (l.223-224) says Mara answers "in English throughout" and that "'Mine.' is said in English", but after N3/N4 the page tags neither "Mine." nor "Where are we going?" nor "Eggs". The bible also says "clay lamp"; the page says "a lamp".
- **CH5-6 (info): narrowed, still open.** No Greek from Mara after p65. The head-shake replaces "No.", and p172 and p182 read as Kallia not understanding her. But three replies (p171, p177, p181) carry no language tag again since N3/N4.
- **CH5-3 (info): still open.** The Kroton frame (p54) still breaks the plan's "the rest happen off the page".
- **CH5-4 (info): still open.** Ch.5 now has exactly one touch (p211). The count question comes from ch-03:p69 and ch-04:p43, and both are unchanged.
- **CH3-3 (low): still open.** p138 still has a pen; outline.md:213 and :222 still have the hut.
- **CH3-7 (info): still open.** The year and span are unchanged (p110-p111), and the page still never names a door.
- **CH4-2 (info): still open.** The storeroom "corners of the granola box" are cut; the pouch-vs-bar question is unchanged.
- **CH4-3 (info): still open.** "fleece" still appears six times (p75, p88, p93, p138, p164, p211), with no "jacket".
- **CH4-4 (info): still open.** Ch.5 does not touch the inscription.

No new conflicts. No knowledge_gap. No needs_review.

## 2026-10-19: UPDATE (re-sync after the author fixes to Ch.2, Ch.3 and Ch.5; Ch.1 celery beat)

**Sources:** `evaluations/revision-chapter-2-author-fixes.md`, `revision-chapter-3-author-fixes.md`, `revision-chapter-5-author-fixes.md`, plus the Ch.3 evaluator's restorations and the Ch.5 wording fixes. All were read as the chapters stood on disk at 13:58. `meta.last_updated_chapter` stays 5.

**Earlier run.** A first run of this job re-anchored the ch-03 and ch-05 citations mechanically (ENTITY_STATE.yaml, 13:51) and stopped before the content pass. This run checked that work against an independent paragraph diff. All 443 explicit re-anchors and all 59 bare/range re-anchors match. One bare ref it missed (`p211` → `p209`, Mara's sweater-pillow) is now fixed.

### Re-anchoring
- **Ch.1:** "He turned the celery in his fingers" is removed. No tracked fact cited it, and the numbering is unchanged (193 paragraphs).
- **Ch.2:** 69 paragraphs, numbering unchanged. Text changed inside p22, p44, p45, p47 and p63.
- **Ch.3:** 90 → 84 paragraphs. Old p29 and p30 (the cloud warning, "I'm staying up"), p44-p46 (the camera lesson) and p59 ("If it had come into my lab…") are deleted. The mapping is:
  - old p1-p28 = new p1-p28;
  - old p31-p43 = new p29-p41;
  - old p47-p58 = new p42-p53;
  - old p60-p90 = new p54-p84.
- **Ch.5:** 212 → 210 paragraphs. Old p29 (the Arcadians/Spartans speech) and old p47 ("a decade below street level…") are deleted. The mapping is:
  - old p1-p28 = new p1-p28;
  - old p30-p46 = new p29-p45;
  - old p48-p212 = new p46-p210.
- No `pDEL` markers remain. The highest citations are ch-03:p84 and ch-05:p210.

### Facts removed (no longer on the page)
- **Ch.2:**
  - the limestone book;
  - "from/in the lab" for the fax, the window mat and the magnifier (the fax to Naples is now "that afternoon", sending place not stated);
  - "my department".
- **Ch.3, Delphi and the approach:**
  - **Lodging and town:** the room over the worry-bead / Charioteer-copy shop, the Itea view, and "leaning on the rail".
  - **The phone and the map:** the kiosk telephone, the phone card and "Ray having his fit"; the hotel bed, the map bought "the afternoon I arrived", the map's cardboard cover, "better than a mile", and Livadi (alias dropped).
  - **The plateau:** the bell frame, the snowmelt sheets, the white van, and the road "from the Arachova side" (removed from arachova, kalivia-plateau and CH5-5).
  - **The path:** the E4 signpost (the E4 now survives only in the German's speech), the white-bar blazes, and the silver-gray bark and needle floor.
  - **The taxi:** its speed and the gravel spray.
  - **The German:**
    - the two o'clock cloud and "Be down before" (removed from the German, Parnassus and knowledge_index);
    - "I'm staying up";
    - the sleeping-bag assumption and "a box and a half of granola bars" (Ch.3 granola count now NOT STATED);
    - the camera lesson (focusing ring, needle, "That's the lever");
    - the goatherd greeting him.
  - **"Every tray of his slides."**
- **Ch.3, the cave:**
  - **The mouth:** "as broad as a kitchen table", the fire ring, bottle and candle stub, and "torn at the elbow" / "beaded red".
  - **The hall:** the stalactites and the "folds and draperies".
  - **Memories and Fenn:** Florida and the crawlspace; Fenn's directions re-read in the cave and "by heart since March"; Fenn's "day after day" and his beans and goat; "the whole block"; "the bigger fool" (removed from fenn-cautionary-mirror, the watch and knowledge_index).
  - **The graffiti catalogue:** the regiment, the Greek names, E. WILKINS 1861, the soot names, "for the order things had happened in", and "If it had come into my lab".
  - **The French report:** two volumes, the April reading "slowly, in French", "caught once already", the plates (figurines, rings, lamps, coins, the bronze cicada), the dyed/drilled/lead-filled bones and "trays of dried beans". As a result, Mara's "reads French" trait, the university-library report row and the April 1998 timeline event are dropped.
- **Ch.5, the Sacred Way:**
  - the Arcadians and Spartans (speech and "brown-gold shine");
  - the Siphnian name, the porch girls and the silver/flooded-mine joke (the frieze is now "the next treasury");
  - the water boy (the entry is kept with `last_confirmed`, per merge rule 4, and its traits removed);
  - the laurel woman (removed from strangers and the Pentax);
  - the row of empty bases, and "a decade below street level … first time I had stood where the taking happened";
  - the Athenian treasury "walked round it twice".
- **Ch.5, elsewhere:**
  - the ox-cart;
  - "the country changed";
  - the money-changer's exit;
  - "since graduate school", "in my first year in the lab", the coins "in the lab", and "in none of my grammars".

### Facts added or corrected
- **The Greek clause (ch-05:p28)** is now the basis of Mara's comprehension in town. The speech is "worn smooth, in a town Greek far nearer my books than the boy's had been on the mountain, and I lost none of it". It is recorded as a new Mara knowledge row (contrast ch-04:p8), in the Greek trait, and in the guide's trait.
- **Other Ch.5 wording:**
  - "the only one the book had given me" (p10);
  - "a word I had never seen written down" (p80);
  - "for most of my working life" (p31);
  - "Everyone beats somebody at Delphi…" is now on the boxer (p37);
  - "He tells it all wrong" (p33);
  - "fine-ridged from the saw" (p45).
- **Ch.3 restorations:**
  - the ski lifts on the far slope (p5), so `knowledge_absent_ch3` "the ski lifts" stands;
  - "a roof that went up into darkness in the middle" (p51);
  - Fenn's drawing "copied … from a photograph in some library book, I supposed" (p46);
  - the knuckle scratch, now at the thornbush: "and the knuckles of my right hand with it" (p45). This re-sources the Ch.5 scratch callbacks (p15, p150) to ch-03:p45.

### Contradictions
- **CH3-8 (low): NEEDS-REPLANT, new.** ch-03:p67 still says "the book about limestone had said so", but ch-02:p22 no longer introduces the book.
- **CH5-5: still RESOLVED.** Ch.3 has lost both route clauses, so ch-05:p2 is now the only statement of the route, and nothing contradicts it.
- **CH4-3: re-checked, still open.** The sleeve is torn "on the thorns" (p45), and "at the elbow" is cut.
- **CH3-2, CH3-3, CH3-7, CH4-2, CH4-4, CH5-2, CH5-3, CH5-4 and CH5-6:** re-checked, and none is changed by the cuts.

**Outline dependencies.** I checked outline.md Ch.6-44. No later planned beat depends on any deleted fact.

No new conflicts. No knowledge_gap.

---

## 2026-10-19: UPDATE (chapter 6, final text: post-polish, post-hook, post-disruption, post-continuity-repair)

**Trigger:** chapter loop step D.5 for chapter 6 (drift policy: every chapter).
**Inputs read:**
- `manuscript/chapters/chapter-6.md`: 342 prose paragraphs, two breaks, so three shards (p1-p35, p36-p243, p244-p342). The two HTML comment lines are metadata and are not counted.
- The existing `ENTITY_STATE.yaml` (`last_updated_chapter: 5`); outline.md Ch.6 and Ch.7; character-bible.md (Valens and Kallia cards, Ch.6 walk-ons, at-risk list); the writer's report.
- Cross-checks against ch-01:p116, p141, p190, p191; ch-02:p16; ch-03:p51, p68; ch-04:p28; ch-05:p55-p64, p137, p169-p180, p210.

**Re-sync during the run.** The continuity-guardian audit (`evaluations/continuity/chapter-6-audit.md`) read the live YAML and filed CH6-1..8 as W-01, W-02, W-03, W-17, W-18, W-19, N-04 and N-18. The book-editor then rewrote 25 paragraphs (`evaluations/revision-chapter-6-continuity.md`; chapter last written 15:15:16), and the outline's Ch.7 beat 3 was patched. Every Ch.6 fact was re-checked against the repaired file. The paragraph count and breaks did not change, so every ch-06:pYY keeps its number. 67 + 7 text corrections were applied. The resolved CH6 entries keep their pre-revision quotes, labelled `[pre-revision text]`.

**Meta:** `last_updated_chapter: 6`; `chapters_tracked: [1..6]`; `paragraph_rule` now records Ch.6 = p1..p342 and the paragraphs the repair changed. 301 lines carry `ch-06:pYY`. Every cite is in range, and quoted phrases were machine-checked against the cited paragraphs.

### Replaced (plan → prose)
- **Valens:** first_appearance (p5 on the page; p36 in story order; name from Kallia, p48); the thumb on the crown (p132); the Ch.6 location log and arc waypoint; his relationship with Mara.
- **Mara:** the Ch.6 location log; the planned row "the Corycian door she came by is shut", replaced by a null test with the page's words ("Cold that was only cold"; "The rock was cold. The air did not move.").
- **Seiko:** the Ch.6 custody row.
- **Other:** the timeline row for Ch.6; the Ch.6 occurrence of hand-at-threshold; the-where, romance and valens-known opened on the page; return-to-the-cave **CLOSED**.

### Added
- **Valens:**
  - Physical: a scar the length of a finger across the back of his right hand, stitched too far apart and healed "in a ladder"; big hands (the watch band will not go halfway round his wrist); tunic, boots, a drawstring belt pouch, a bag. Age is not stated on the page.
  - 15 Ch.6 traits:
    - His Greek is flat and foreign; with Kallia he answers her fast Phocian "a word at a time".
    - He speaks Latin to the mules.
    - Footing: ashes on the ice, sacking on the hooves, "Step where she steps".
    - Weather lines.
    - Mind-reading that is wrong in ordinary ways: the donkey man "Somebody for you", hidden silver, "a big house. Corinth, or Patrae".
    - The bargain kept to the letter.
    - The watch handled with care: wound backward, then forward to full.
    - He pays Pan a crust; he does not admit to reading.
    - Evasions: "North.", "On the road.", "Don't.", and her name never asked.
    - The laugh and the bread.
    - The lies to the charcoal burner and "You never had a watch".
    - No simile in his speech.
  - Knowledge: 13 rows. `knowledge_absent_ch6`: her name, which he heard only inside her English speech; the door; how to *set* the watch.
  - Possessions: the mules have no names (the gray, the brown, a dun; five at the delivery; from Corinth); the Seiko; his climbing gear.
- **Mara:**
  - `worn_ch6`, `carries_ch6` (now including the flashlight), `marks_ch6`, `hunger_ch6`; 13 Ch.6 traits.
  - Knowledge: 19 rows. `knowledge_absent_ch6` (no watch from the evening before the climb). New alias "the nymph". A Ch.6 arc waypoint.
- **Kallia:**
  - 6 traits: the pomegranate, the wood haggle, the sea and the letters, orders, "The shovel comes back.", the broom.
  - `household_ch6`; Valens and a Theban lodger as relationships; possessions (the ash shovel, the ash pail, the kerchief money).
  - 3 knowledge rows; `knowledge_absent_ch6` (the watch deal, where Mara went).
  - "The widow" is now on the page, as what others call her.
- **New characters (5):**
  - `charcoal-burner-parnassus`: minor; the goat-boy is "my cousin's boy"; full knowledge rows; a `gossip_risk` field.
  - `theban-on-gallery`: kept distinct from `gallery-pilgrim`.
  - Mentioned only: `delphi-temple-painter`, `man-from-philadelphia-in-asia`, `larchwood-neighbor`.
- **Updated characters:**
  - goat-boy: his story spread "this autumn"; the burner is his kin.
  - Emilio: wound the Seiko at the kitchen counter while the percolator went; "came home when he said he would maybe twice".
  - Ray: snow tires on the Buick.
  - Gloria: the odd earrings, now in place of the freezer keys.
- **New locations (4):** `cliff-stair-above-delphi` ("the stair"; ice from the second turn; the charcoal kiln at the top; the Kaki Skala name is not on the page), `patrae`, `philadelphia-in-asia`, `boeotia`.
- **Updated locations:**
  - corycian-cave: the November mouth, hall and crack; aliases "Korykian" and "Pan's cave"; the cliff-stair distance.
  - kalivia-plateau: snow; the pen's fresh withy; the descent cave → firs → pen → plain → cliff top.
  - parnassus: the snow line, the charcoal men, the cloud bank.
  - delphi: the sanctuary wall's high corner, the dogs, the sacrifice now past, the market gossip.
  - castalian-spring: "the lions"; a round trip with a full jar is about half an hour.
  - temple-of-apollo-delphi: seen from the cliff; repainted each spring.
  - kallias-house: the lane, the court, the gatepost, the woodstack.
  - kirrha: the last ship eight days before.
  - corinth; philadelphia (Larchwood, Kennedy); maras-apartment (the radiator; "behind" on the rent); delphi-modern (the hotel).
- **Objects:**
  - New `kallias-ash-shovel`: chekhov_open, unplanned. "The shovel comes back"; it is in Mara's hands at the end of the chapter, not yet returned.
  - Seiko:
    - Set to local time by the gatepost's noon shadow on her second day at Kallia's; wound "since March".
    - The steel link band (three links out) has a clasp, not a buckle.
    - Paid to Valens the evening before the climb; three Ch.6 windings (his backward one, hers, his forward to full).
    - New fields `physical_ch6`, `time_setting_ch6`, `what_valens_was_told_ch6` and `secrecy_ch6`.
  - taxi-drachma-coins: two remain. The bigger is "brass, and the head of an old man with a beard" ("A poet"); the denomination is not on the page (the editor's note says 50 dr, Homer). Its conflict field is removed after auto-resolve.
  - flashlight: in the duffel "under everything", unused, hidden from Valens (p7).
  - duffel: never unpacked; "Everything"; taken into the cave; in her hands at the end.
  - goat-hair-blanket: folded and thanked for in English.
  - kallias-broom: a broom on the page (p38); the threshold beat is still Ch.7.
  - Pentax and film: 0 frames in Ch.6; 27 left by the plan count.
  - microcassette: not mentioned.
- **Knowledge index:**
  - door_location: Valens hears fragments only, not the door.
  - mara_origin: rows for the charcoal men, Valens (nothing true), the burner (the nymph plus Valens's cover), Kallia (nothing new) and the town (risk).
  - New indexes `seiko_with_valens` and `mountain_trip_ch6`.
- **Timeline:**
  - The Ch.6 row: two days told out of order; about a month after the crossing ("most of a month"); the month is not named (plan: November); snow down to the cliff rim; the sea shut; the weather goes from clear to big wet flakes by about 2 p.m.
  - 12 new timeline_events rows; the sacrifice row is now marked past.
- **Plot threads:**
  - New `nymph-rumor`: the burner is a witness against "You went up by yourself"; the bible says the rumor is not retold again.
  - Ch.6 notes on kallias-son ("Letters."), celer-and-the-frame (nothing on the page), mending-the-seam (the laddered scar), maras-legal-nonexistence ("She's the widow Kallia's" is the first time she is called somebody's), maras-greek-refusal and relics-watch.
- **World rules:**
  - Shut-door implications, OBSERVED:
    - One null afternoon (the door is not shown shut for good).
    - The winter detection limit: the cold sign can't be told from the mountain's cold.
    - No repeating clock hour.
    - Nothing she does moves the door.
    - A native standing by proves nothing.
    - Time runs at the same rate on this side.
    - The consequence: she must stay (Ch.7).
  - Ch.6 observations added to existing rules: the sea is shut, plus the road over to Boeotia; no shoes on the mules (sacking on ice); a woman alone is read as a runaway.
  - New observed rules: offerings to Pan at the cave; the yearly repainting of the temple.

### Contradictions
- **CH5-6: RESOLVED.** ch-06:p39 says "I had spoken no Greek aloud since the guide on the Sacred Way". This matches the audit's N-05.
- **CH5-2: narrowed** to "clay lamp" (bible) vs "a lamp" (page). Still open.
- **CH6-1 (low): RESOLVED.** "Since January" contradicted Ch.1, where the watch is first wound on 14 March. The page now says "since March".
- **CH6-2 (low): RESOLVED.** The coin shown to Valens duplicated Ch.5's hundred-drachma piece. It is now "an old man with a beard" / "A poet".
- **CH6-3 (info): RESOLVED.** "Three months behind" did not fit the time elapsed. The page now says only "behind".
- **CH6-4 (info): RESOLVED.** "In front of the whole square" is now "in front of half the Way".
- **CH6-5 (info): OPEN.** Ch.5's plan names the cart-track route, but p38 says "I had no idea of the way".
- **CH6-6 (info): OPEN.**
  - The bible's Ch.6 notes quote pre-disruption text: "pay men to ask", "if they asked me", "Whoever knows where can be asked where", "three eaten", "Nobody learns Latin on…" and the "milk … cream" simile.
  - The bible (last written 14:31) also lacks every continuity-repair change: the clasp, March, the poet coin, the hidden flashlight, the olives, "In Delphi … Kallia has not asked it", the haggling "a word at a time", and the earrings.
- **CH6-7 (info): RESOLVED** by the outline patch. Ch.7 beat 3 is now a month of *public* silence, with Mara speaking only inside Kallia's house.
- **CH6-8 (info): RESOLVED.** The May hour is now given "by Athens time, which ran an hour and more ahead of this sun" (p14).
- **Re-checked:**
  - CH3-3: a pen under the firs again; no hut.
  - CH3-7: "open" and "shut" are on the page, but there is still no "door".
  - CH4-3: no upper garment is named in Ch.6.
  - P5: Valens lives openly in Delphi, and the sea is shut, which fits a spring arrival for the notice.
  - All others are unchanged.

No knowledge_gap. No needs_review.

### For Ch.7–9
- **No watch.** Mara has no clock time from the evening before the climb; Ch.8's attempt is untimed. Valens has the Seiko, in his belt pouch, wound forward daily. He has not been shown how to *set* the hands, and the plan's Ch.18 "set near noon by the shadow" needs that.
- **The cover story** is "You went up by yourself. You never had a watch." Mara must not mention the watch in public.
- **A witness.** The charcoal burner saw them together and will spread "the nymph … the widow Kallia's … came off a ship … since the olives" "all over the town by the next market". Ch.7's "Syracuse" cover must be compatible with "came off a ship". The rumor itself is SPENT as a retelling.
- **The shovel** is promised back to Kallia and is still in Mara's hands.
- **The flashlight** is hidden in the duffel. Any use must reckon with being seen.
- **The Greek silence** (patched outline): silent with Kallia until now; she speaks Greek to Valens and the charcoal burner. In Ch.7 she goes silent in public for a month and speaks inside the house.
- **Valens's knowledge.** He knows her as a reader with Latin and soft hands, a runaway from a "big house" with no husband; "Philadelphia" is "past the Parthians". He does not know her name. He reads inscriptions without admitting it, which matters for Ch.9, where he reads the notice, and Ch.11, where it emerges that he can read.
- **His scar** is on the back of his right hand, so the Ch.9 notice's "scarred" must fit it.
- **Valens is known** in Delphi as "Valens" or "Mule-man", never "Lupus".
- **Letters.** Kallia asked after "Letters" from the east before the sea shut. Ch.10's letter sitting at Kirrha all winter fits that.
- **Season.** The sea and the Boeotia road are shut. The cliff stair is iced from the second turn; the plain is under snow.
- **Mara's injuries.** The heel of one hand is skinned (which hand is not stated). Her knuckles are split and her palms blistered; she still cannot carry a jar on her head.
- **The crack** gave nothing in cold weather, and Mara knows a hand test can't tell in winter. Ch.8's attempt is "nothing" with "no scream".

---

## 2026-10-19: UPDATE (chapter 7, final text: post-polish, post-hook, post-disruption, post-continuity-repair) + Ch.6 re-anchor

**Trigger:** chapter loop step D.5 for chapter 7 (drift policy: every chapter). Two mid-run instructions from the orchestrator: (1) re-anchor the Ch.6 citations by content, since chapter-6.md has 341 paragraphs after its polish cycle 1; (2) wait for the Ch.7 continuity repair (`evaluations/revision-chapter-7-continuity.md`) and verify against the final text.
**Inputs read:**
- `manuscript/chapters/chapter-7.md` in its final state (last written 16:55:16; checked unchanged against a snapshot before each write): 194 prose paragraphs, 3 breaks, four shards (p1-p58, p59-p128, p129-p182, p183-p194), 6,041 words by shape_check.
- The existing `ENTITY_STATE.yaml` (`last_updated_chapter: 6`); outline.md Ch.7-8 (plus Ch.9-18 for dependencies); character-bible.md (Kallia, Valens, Sosandros, Mrs. Dunphy, the Ch.7 walk-ons, the at-risk list).
- The Ch.7 pass reports (dialogue, hook, disruption, writer); `evaluations/continuity/chapter-7-audit.md`; the continuity repair log; `evaluations/revision-chapter-6-cycle1.md`.
**Meta:** `last_updated_chapter: 7`; `chapters_tracked: [1..7]`; `mode` and `source` updated; `paragraph_rule` extended to Ch.7 and notes the Ch.6 re-anchor; two new `revalidation_needed` rows (chapter 6, RESOLVED). 968 `ch-07:pYY` cites, all in range. Every quoted phrase was machine-checked against its cited paragraph: 0 misses. The YAML loads under a strict loader with no duplicate keys.

### Ch.6 re-anchor (polish cycle 1 had edited chapter-6.md after the Ch.6 update)
- **Map.** Built from a paragraph diff of the pre-cycle backup against the current file: old p1-p100 = new p1-p100; old p101 ('I will not.') + old p102 = new p101; old p103-p342 = new p102-p341. Shards are now p1-p35, p36-p242, p243-p341.
- **Remapped:**
  - 1,096 explicit `ch-06:pYY` cites across 252 lines, with their ranges;
  - bare Ch.6 p-refs on Ch.6-only lines;
  - 8 mixed lines, by hand. Line 467's bare refs are Ch.5 and were left alone.
  - The content check found no mismatch introduced by the remap.
- **Text updated to the cycle-1 page:**
  - 'The rock was cold. Behind me the torch flame stood straight up.' (5 places).
  - Emilio wound the Seiko 'on the few mornings he was there' (his trait, the timeline_events row, Mara's Ch.6 memory trait).
  - 'I make the cracks in old pots disappear'.
  - The plea now reads 'I've done the floors every day for a month, and everything anybody asked me'.
  - 'my bleeding hand held away from it'.
  - CH6-5 gets `prose_now`. It is narrowed but still open: the page now admits 'the long road round'.
  - CH6-4 notes that the sentence is cut altogether.
  - Valens's build gets 'she had to brace a foot under his weight'.
- **Six older cite gaps filled:** Valens knowledge_absent_ch6 (+p334, +p279); theban-on-gallery (+p76); Kallia knowledge_absent_ch6 (+p315, +p319); boeotia (+p150); Seiko custody (+p118).
- **Also fixed:** a duplicate `resolution: null` key in `kallias-ash-shovel`.

### Replaced (plan → prose)
- Mara's Ch.7 location log, arc waypoint, the aliases 'Maira' and 'Kallia's kinswoman from Syracuse', and the planned trait surfacings (teeth, all-or-nothing, Mrs. Dunphy, the Greek refusal).
- Kallia's Ch.7 waypoint, the broom trait, and the possessions himation and broom.
- `mrs-dunphy.first_appearance` and mutation; `kallias-broom.introduced`; `borrowed-himation` (the whole entry); `toothbrush-and-floss.resolution`; timeline row 7.
- knowledge_index `mara_origin`: Kallia's row.
- `kallias-son.opened`; `maras-legal-nonexistence` (PAID, closed); `maras-greek-refusal` (closed).

### Added
- **The legal record** (`objects.delphi-tribute-list-entry`; `mara-reyes.legal_status`):
  - **The text:** *Maira, daughter of Aimilios, of Syrakousai; free; kinswoman of Kallia, of her house and in her keeping.*
  - **Who and where:** made by Sosandros at the council hall beside the square, winter AD 70 (day 19-20 of the silence); Kallia answers 'I do.'; fee two obols.
  - **The occasion:** spring talk that Vespasian will revoke the freedom, so the council is entering every house 'before Rome put a governor back in Corinth to ask for it'.
  - **The medium:** wax, rewritten yearly; no copy issued.
  - **Not in the line:** the husband's brother, the boat, the vintage and the dead parents were told to the clerk but not written.
- **The Syracuse cover** (new thread `syracuse-cover`; new index `syracuse_cover`):
  - Valens invented the boat and 'Since the olives' (Ch.6).
  - Kallia invented Syracuse, the husband's brother, 'Your people died', 'one of the last boats … after the vintage', the cold, and 'Half Syracuse is Roman'.
  - Mara supplied 'Mara' and 'Aimilios'.
  - Sosandros supplied MAIRA, 'Syrakousai' and 'Sicilian'.
  - The husband's brother is never named, so by the record he is Aimilios, 'A Roman'.
  - Mara knows Syracuse only from her father's slides.
- **Names** (new index `maras_name`): Kallia and Sosandros now know it. Kallia's first use is 'Maira. The water.' ('nearer Mera'). New aliases: Mera, Antigone, "Kallia's simple one / the one that doesn't talk". Kallia's knowledge_absent 'Mara's name' is CLOSED.
- **Characters (15 new; `council-clerk` renamed `sosandros`):**
  - **`sosandros`:** the page identifies the Ch.5 doorway clerk at ch-07:p141. Full card: the form's questions, MAIRA, 'Syrakousai', the brick.
  - **Walk-ons:** `bakers-wife-bath`, `girl-with-the-mole`, `bath-keepers-wife`, `salt-seller`, `sprat-seller`, `drover-from-the-west`, `latrine-men`, `cheese-man`, `boundary-wall-father`, `clerks-boy`.
  - **Needs review:** `fountain-man-laughing` and `theban-bassoon-voice`.
  - **Mention only:** `kallias-runaway-girl` (owner of the himation), `west-philadelphia-nurse`, `rittenhouse-friends-husband`.
- **Mara:**
  - New fields: `worn_ch7`, `carries_ch7`, `marks_ch7` (the vaccination scar, the pale band, unsinged legs), `teeth_ch7`, `hunger_ch7`, `hair_ch7`.
  - 10 Ch.7 traits; 20 knowledge rows; `knowledge_absent_ch7`.
  - Relationships: Sosandros, the salt-seller, the drover, the girl.
- **Kallia:**
  - `carriage_ch7`; 10 traits; `household_ch7`; a Ch.7 location row.
  - Possessions: the second-best jar, the old jar, the combs, the pot.
  - 8 knowledge rows; `knowledge_absent_ch7`.
  - Relationships: Sosandros, the salt-seller, the baker's wife, the late husband.
- **Valens:** boots only (`clothing_ch7`); 3 traits; a location row; 3 knowledge rows; `knowledge_absent_ch7` (her name, the registration); a waypoint.
- **Emilio:** the alias 'Aimilios' (the Nicosia offprints); Syracuse in his slides.
- **Mrs. Dunphy:** `memory_ch7` and her 1998-side facts (fourth grade c. 1974-75, derived; the green cardigan 'short of its second button'; the blotter; thirty pencils; the three o'clock bell).
- **Objects:**
  - New: `delphi-tribute-list-entry`, `lentisk-stick`, `burnt-horn-tooth-powder`, `kallias-second-best-jar` (destroyed).
  - `kallias-ash-shovel`: **chekhov_closed** (returned at p2-p7).
  - `borrowed-himation`: the runaway girl's, 'of wet-sand brown'; its smell arc; the anchor at p174; bring it at midwinter.
  - `kallias-broom`: the threshold beats p37 and p185; two brooms.
  - Also updated: the duffel, the flashlight ('since October, unseen by a soul in that house'), the Seiko (Ch.7 custody; not seen) and the toothbrush.
- **Locations:**
  - New: `delphi-baths`, `delphi-latrine`, `delphi-council-hall`, `syracuse`, `amphissa`.
  - Facts added to delphi, castalian-spring, delphi-market-square, kallias-house, kirrha, corinth, boeotia, philadelphia, nicosia, kalivia-plateau, corycian-cave (and a distance) and university-museum.
- **Timeline:** row 7 (late November AD 70 → the end of the month of silence; the day count holds); a note on row 8; 13 timeline events.
- **Threads:**
  - New: `syracuse-cover`, `kallias-fifth-coin` (spitting-oak haggle SPENT, audit W-13), `thyiades-midwinter` (payoff Ch.8).
  - Ch.7 notes on nymph-rumor (effects only; no 'nymph' word in the narration), mending-the-seam, mrs-dunphy, romance, valens-known and the four relics.
- **World rules:**
  - 7 new OBSERVED rules: belonging; how a woman passes; the latrine; the bath; the god's basin; the biennial rite; Delphian vs Erasmian Greek.
  - ch7_observed notes on the guardian law, the freedom and the sea.
- **Organizations:** Ch.7 facts for thyiades, delphi-council and delphic-sanctuary.

### Contradictions
- **CH7-1..CH7-5: found in the pre-repair text, RESOLVED by the continuity repair before finalize.** Each prose field is labelled `[pre-repair text]`.
  - CH7-1: 'fifteen years at a bench' is now 'For ten years'.
  - CH7-2: 'the room at the top of the stair' is now 'the shut room upstairs'.
  - CH7-3: 'the last boat' is now 'one of the last boats'.
  - CH7-4: 'the governor's men in Corinth' is now 'before Rome put a governor back in Corinth'.
  - CH7-5: 'I could not stop' is cut, so the break count stays at three.
- **CH7-6 (info): OPEN.** The bible's Ch.7 blocks quote pre-polish and pre-repair text: the Fiat trip; 'What name did you give him?'; 'like a man in a play'; 'sea-nymph'; 'color of wet sand'; 'on a Theban'; 'for my living'; the drover's and the salt-seller's lines; 'Antigone' ×3. It waits on the separate bible sync (audit W-19).
- **CH7-7 (info): OPEN.** The outline's 'magistrate's clerk' vs the council's clerk; the page never says whose the swept room is (by design).
- **CH7-8 (info): OPEN.** The bible says Mrs. Dunphy 'never speaks in the memory'; the page has the reported 'said we could go'.
- **CH6-9 (info): OPEN.** The bible quotes 'his hands were older than the rest of him', which is not on the Ch.6 page (p44).
- **P2: RESOLVED.** The outline now reads 'written down as somebody's kin', and the page agrees.
- **Auto-resolution check on every open item.** Nothing else resolves. CH6-5 is narrowed by the Ch.6 cycle-1 text. Each open item has a `recheck_ch7` note.

No knowledge_gap. Valens's 'You've stopped talking' has a path (her silence at the gate), and so does Kallia's 'So the town says' (the charcoal burner's gossip, ch-06:p328).

### For Ch.8-10
- **Ch.8:**
  - **The rite as Kallia set it:** midwinter, every other winter ('this is the winter'), onto the snowbound plain at night, torches, 'a skin of wine for every three of you', 'no man past the last house'. Rags over the boots; the girl's himation. Kallia is going ('You'll come').
  - **Mara's closing question is distance, not success.** She has no watch, so any cave attempt is untimed. The flashlight is in the duffel, and any use must reckon with being seen.
  - **The year:** the page does not fix the year's turn. Outline AD 71 needs midwinter to fall after it.
  - **Spent:** 'simple' is retired for Mara. The public mockery set-piece is closed, and 'Antigone' is capped. The broom must not be shown in Ch.8-9.
  - **The husband teasing:** must fit the record (it names no husband; she told Valens 'I have no husband').
- **Ch.9:**
  - Valens has been seen in Ch.7 only as boots. The scar is on the back of his right hand.
  - Her public silence is over: after the council the page does not say she stays silent, so she can bargain in Greek.
  - Women need a male representative for the Oracle. The record names Kallia as her keeper, not a man (Ch.11's cousin).
  - The notice comes with the spring traffic; Valens has not heard Syracuse or her name.
- **Ch.10:**
  - The swept room is 'the shut room upstairs' / 'at the end of the gallery, past the lodgers' rooms'. Kallia has never named the son or said whose the room is.
  - Kallia cannot read ('What did he put?'). Mara reads wax upside down.
  - Four Thebans are in the house 'till the thaw'.
  - Kallia's line on the list has had 'no other name … for years', so her son is not on it.
  - Her late husband's brother is 'Aimilios of Syracuse' by the record, and Ariston's letter must not contradict that.
- **Ch.16/18:**
  - The status rests on a wax entry in Delphi's council book, rewritten yearly, with no copy issued.
  - She is 'free', and 'Maira, daughter of Aimilios, of Syrakousai' is her name on paper.
  - The fifth coin is owed but SPENT as a scene.

## 2026-10-19: UPDATE (re-sync of Ch.7 after polish cycle 1 + finalize fixes F1-F3)

Re-sync of ENTITY_STATE.yaml to chapter-7.md as it stands (last written 17:25:38; revision log `evaluations/revision-chapter-7-cycle1.md`; F1-F3 from `evaluations/chapter-7-eval.md`). `last_updated_chapter` stays 7. chapter-8.md was not read or recorded.

### Numbering
- 194 -> **195** paragraphs; still 3 breaks (after p58, p128, p182).
- The only structural change is a **new p184**, the storeroom address scene. The editor's log calls it ¶378 because it numbers by file line.
- Old p1..p183 keep their numbers; old p184..p194 = new p185..p195.
- Remapped: 68 explicit `ch-07:pYY` cites (including the range p186-p194 -> p187-p195) and 8 bare Ch.7 p-refs.
- Every quoted fragment on a Ch.7 line was then checked against the file.

### Removed (cut from the page)
- The bath laugh (p54).
- The queue laughing "at something Kallia had said" (p170), on three rows: Mara's splinter trait, the boundary-wall father, and the bath woman's trait.
- Kallia "the only woman in the room on her feet" (p44).
- "before I had thought about it" (p183, the Mera alias).
- "of their own accord" (p183).
- The old summary's "I gave up English even with myself" and its one-clause address.

### Moved p183 -> p184
- The zip code.
- The himation's late smell ("had stopped smelling of quince").
- Sleeping under the himation.

### Added
- **maras-apartment**:
  - the street door
  - a vestibule with the mailboxes, hers with "my name inked on a bit of tape"
  - the stairs and "the second landing"
  - the address form: number, street, apartment, "Philadelphia, P-A", and a zip code whose first two figures are 1 and 9
  - the floor is not stated (at or above the second landing, inferred)
  - whether this is the Larchwood building is not stated
- **Mara's knowledge**:
  - her address as prior knowledge
  - the address failing after "P-A" and coming back on the remembered walk (discovered)
  - a knowledge_index row: nobody else knows
- **Mara's Ch.7 location row**: the storeroom night, with a `remembered_walk` field.
- **philadelphia**: the counters (the dry cleaner's, the circulation desk) and p1's zip-code clerk.
- **kallias-house** storeroom at night (the hanging oregano, a Theban snoring along the gallery), plus the lodgers' row.
- The timeline row and a timeline_events entry.
- The cost trait, rewritten from the page.

### Continuity commitment (recorded)
- New Mara trait `CONTINUITY COMMITMENT`, and a new thread `maras-english-to-herself`, status open.
- From ch-07:p184 ("from the next night I kept even my own company in Greek"), Mara speaks **no English to herself**, aloud or under her breath.
- English to a listener is not a break (for example Fenn, outline Ch.25).
- Earlier English to herself (ch-04:p79) comes before the commitment.
- The "falls back on English" trait gets a `ch7_note`, and maras-greek-refusal gets a cross-reference.
- Check point for continuity-guardian, not judged here: outline Ch.26 has her read Fenn's letters aloud to her newborn.

### Contradictions
- CH7-1..CH7-8 were already RESOLVED and stay RESOLVED. The cycle text does not reopen any of them.
- No new contradiction and no knowledge_gap.
- Nothing else is settled by the page: no Ch.7-opened object or thread changes status.
- Older cite gaps filled:
  - CH7-2 "at the bottom" = p187
  - the shovel's "the god's rock" +p4
  - "The god's women. Dionysos's." p190
  - the timeline's "till the thaw" +p144
- Audit trail: `meta.revalidation_needed` (chapter 7, RESOLVED), the header comment and `paragraph_rule`.
- The YAML parses with `yaml.safe_load`.

---

## 2026-10-19: UPDATE (chapter 8, final text: post-writer, dialogue-polish, hook-craft, disruptor and continuity repair)

**Trigger:** chapter loop step D.5 for chapter 8. Mid-run, the orchestrator reported the book-editor's continuity repair (`evaluations/revision-chapter-8-continuity.md`, from `evaluations/continuity/chapter-8-audit.md`). The draft update was then re-checked against the repaired file before it was written.
**Inputs read:**
- `manuscript/chapters/chapter-8.md` in its final state (last written 18:59): 241 prose paragraphs, no breaks, one shard, 7,691 words by shape_check. A paragraph diff against the pre-repair text shows no renumbering and text changed inside 29 paragraphs.
- The existing `ENTITY_STATE.yaml` (`last_updated_chapter: 7`); outline.md Ch.8–9 (and Ch.11–13 for the Oracle thread); character-bible.md (Nikaso, Sostrata, Timo, Philista, Theano, the Ch.8 walk-on note, Kallia, Valens); the repair log; the audit (its priority table and suggested patches).

**Meta:** `last_updated_chapter: 8`; `chapters_tracked: [1..8]`; `paragraph_rule` extended to Ch.8 (with a rough map and the repaired paragraphs); a new `revalidation_needed` row (chapter 8, RESOLVED in the same run). 921+ `ch-08:pYY` cites, all in p1..p241. Every quoted phrase on a new Ch.8 line was machine-checked against its cited paragraphs in the final file. The only misses left are deliberate: pre-repair labels, outline quotes, and the tracker's retired plan row. The YAML loads under a strict loader with no duplicate keys.

### Replaced (plan → prose)
- Mara's Ch.8 location log and arc waypoint.
- Theano's `first_appearance` and Ch.8 location row.
- Kallia's planned row "Mara means to consult the Oracle" (told_by:mara-reyes) is replaced by prose rows (CH8-1).
- Timeline row 8: "a few days past the turn of the year by my private reckoning" (p7) settles the old note. Midwinter falls after 1 January AD 71.
- `hand-at-threshold` Ch.8 occurrence. `thyiades-midwinter` PAID and **closed**.
- The corycian-cave "nothing (Ch.8)" row and the Parnassus and Thyiades rows are confirmed.

### Added
- **Renamed:** `bakers-wife-bath` → **`sostrata`** (`former_slug` kept), because the page links them ("the woman who had offered to singe my legs at the bath", p46; named p48–p49). Index refs updated.
- **New characters:**
  - **`nikaso`**: the sieve neighbour's wife (p17–p18; the relationship key `sieve-neighbors-wife` is now `nikaso`). Her husband's sister's red sandals. She tells the frozen-cloaks story on the stair. She has a `gossip_risk` (she knows about the cave).
  - **`timo`**, **`philista`**.
  - **`woman-at-the-lions`**: the unnamed stranger in the goat-hair cloak.
  - Walk-ons: `liknon-bearer`, `fawnskin-woman`, `stair-scouts`, `crying-mother-pen`.
  - Mention only: `nikasos-sister-in-law`, `timos-husband`, `sostratas-husband`, `philistas-husband`, `vermont-tree-brothers`.
- **Theano:** an identity known to the outline but not to Mara (`ch8_identity`). On the page she is an unnamed old woman at the last gate but one, throwing barley over the frozen ruts with "her eyes on the crows". Mara records no knowledge of her until Ch.13.
- **Mara:**
  - Physical: `worn_ch8` (the himation drawn over her hair; a bronze pin; a wet ivy ring; blanket rags over the boots), `carries_ch8` (split oak; a pine plus "another two pines"; NOT the flashlight; two brass coins), `marks_ch8`, `hunger_ch8` (the wine), `hair_ch8`.
  - Traits (10): her Greek in public, uncontracted; the repairer's eye; the sandal saved; a fair test with no blow; partial comprehension of overlapping talk; belonging (the joke, "I was laughing too", the refrain); money; the Vermont tree-lot memory.
  - 18 knowledge rows; `knowledge_absent_ch8`.
  - New aliases: "the Syracusan" and "You at the lions".
  - Relationships with the five women.
  - The continuity commitment is checked: no English in Ch.8.
- **Kallia:**
  - `hair_ch8` (seen "only once before, plastered flat at the bath"); `clothing_ch8`; `household_ch8`.
  - 10 traits, including "crouched … stayed crouched" (never sits) and "Did you find what you went for?".
  - Knowledge (inferred: the cave; told: "No. It was shut."; prior: the Oracle's terms); `knowledge_absent_ch8`; possessions (the wineskin, split oak, ivy); location row and waypoint.
- **Valens:** `seen_ch8` (from behind at the last roof, with the gray); a trait; a location row (whose building it is is not stated); `knowledge_absent_ch8`; a waypoint.
- **Objects:**
  - New: `liknon`, `thyiades-wineskin`, `nikasos-red-sandals` (chekhov_open, unplanned), `strangers-goat-hair-cloak` (the shared cloak).
  - Updated: `borrowed-himation` (soaked, frozen, cracked; last mention p222), `flashlight` (left under the stair, p10), `taxi-drachma-coins` (both brass), `kallias-ash-shovel` (the scratches recalled), `kallias-sieve` (Nikaso still owes the mending), `maras-duffel`, `fathers-seiko-watch` and `kallias-broom` (both absent).
- **Locations:** Ch.8 facts for kalivia-plateau (the dancing ground; the pen, now edge-set with the hurdle dragged aside; the huts "the width of the plain away"), corycian-cave (drift; the pale stone to the left; the slab; the scratches; "January cold and no more"; a distance row), parnassus, delphi (the upper-town street with frozen ruts and rime; the last roof; the lower town), castalian-spring, kallias-house, cliff-stair-above-delphi (the stair shut by a head-high drift), syracuse, kirrha, athens and philadelphia.
- **Knowledge index:**
  - New **`cave_visit_ch8`**: Mara; Kallia (inferred plus told); Nikaso (told); nobody else; Valens not shown.
  - New **`oracle_access`**.
  - Rows added to `mara_origin`, `maras_name` (Timo and Nikaso say "Maira"; the path is not shown) and `syracuse_cover` (now public as "the Syracusan"; no husband, "Not even a dead one").
- **Threads:**
  - New **`oracle-access`** (opened Ch.8, payoff Ch.13).
  - Ch.8 notes on the-where, romance, valens-known, kallias-son ("not husbands and not sons"; "Who would I send in?"), mending-the-seam, nymph-rumor (not retold), syracuse-cover, maras-english-to-herself (held), maras-greek-refusal, kallias-fifth-coin and the four relics.
- **World rules:** `ch8_observed` on the shut door, the winter limit, the door answering nothing, women and the Oracle, the winter closing of the Oracle, and the shut roads. Three new OBSERVED rules: no talk of men until the god is woken; the child woken in the winnowing basket; snow shutting the stair (and frozen cloaks).
- **Organizations:** thyiades gets its name on the page, the order of the night, Philista and the Athenians, the night in the pen, and its named members.
- **Timeline events:** 6 rows (the night; "the time before last"; the winter the spring froze; Timo's wedding; Sostrata's twenty years; the Vermont lot).

### Contradictions
- **CH8-1 (low, OPEN):** the outline says "she has decided to consult the Oracle (Kallia mentions it on the descent)". On the page Kallia raises it unasked, as a conditional, on the way back to the cliff head. Mara states no decision, and there is no descent on the page.
- **CH8-2 (info, OPEN):** Theano. The plan has the god's barley, the sanctuary crows and a lie. The page has her own door, "That's not for you", and no lie. Her identity rests on the outline only.
- **CH8-3 (info, OPEN):** in Ch.7 the cliff-top-to-cave ride took "the better part of a morning"; in Ch.8 the plain alone took "most of a morning".
- **CH8-4 (info): RESOLVED by the repair.** "Stacked" walls and a vanished hurdle became edge-set walls with the hurdle dragged aside.
- **CH8-5 (info, OPEN):** Nikaso's gate is "Two gates up from Kallia's", while the sieve door is "halfway along" the lane.
- **CH8-6 (info, OPEN):** the bible's Ch.8 notes quote pre-polish and pre-repair text: "Hitch that up"; a silence where the page has "Who would I send in?"; "Was it shut?"; Theano's "Thieves"/"whose it is"; the knotted strap; Plutarch; Kallia sitting; "no stopping it"; "a bank at Fifteenth and Market"; and others. This waits on the bible sync (W-20).
- **CH8-7 (info, OPEN, new from the repair):** "another two pines" but only one change of torch, called "the last of my pines".
- **CH3-7: RESOLVED.** Closed on the guardian's recommendation, relayed by the orchestrator. The conflicting value was the tracker's own retired plan row.
- **CH3-3: still open,** updated. Ch.8 is a fourth look at the site and it is still a pen, now edge-set. The audit recommends patching outline Ch.4 to "pen".
- **All other open items** were re-checked with `recheck_ch8`; Ch.8 does not touch them. P5 gets a ch8_note.

No knowledge_gap. Kallia's cave question has a path (ch-07 "your cave"), and after the repair she does not presume the cave opens. "The Syracusan" and "Maira" in the women's mouths are town talk, and the path is not shown. No needs_review.

### For Ch.9–10
- **The decision is not on the page (CH8-1).** Ch.9 must show Mara deciding to consult, or show it already made. Kallia was told no intent. What she has from Ch.8 is "If it's something you want out of that mountain …".
- **What Mara knows about the Oracle:** no answers in winter; once the road is clear he answers "whoever's paid"; women can't go in, so a man goes in; "It costs. More than you've got. Ask a priest." The pelanos, the goat, the sponsor and the day are new in Ch.9. Kallia has nobody to send ("Who would I send in?").
- **Money:** she has two brass 1998 coins and nothing else, and her worth in Phocis is "anybody's guess". The flashlight is still hidden at the bottom of the bag under the stair.
- **Who knows about the cave visit:** Kallia ("In there"; "No. It was shut.") and Nikaso ("To see if it was open"). Nikaso's discretion is not shown. Valens did not see Mara.
- **Public identity:** "the Syracusan", "Maira", no husband, "not even a dead one". Kallia's order for questions is "what I told the clerk, and not a word over".
- **New neighbours:** Nikaso (two gates up; owes the sieve's mending; red sandals, one ruined) and the stranger at the lions (unnamed; the patched strap). Sostrata, Timo and Philista are named and carded. Kallia still never touches Mara and never sits.
- **Valens:** last seen at the last roof with the gray. His danger (the notice) is untouched. Ch.9 has him reading it in the agora.
- **Spent per the bible:** the threshold form, the shared laugh, the baker's song refrain, "She'll have my eyes", "You at the lions", and "the last house" (cap reached). Theano stays unrecognised until Ch.13.
- **Ch.10:** the swept room is pre-planted only by "not sons" and "Who would I send in?". No son is named.

## 2026-10-19: UPDATE (re-sync of chapter 8 after polish cycle 1 and finalize fixes F1–F4)

- Re-anchored every ch-08:pYY to the final page (241 paragraphs: new p41 = Nikaso's stair story; old p240, the lying-awake coda, cut; old p41–p239 → p42–p240). Removed the cut facts (lentil heckle, aniseed fennel, mule-morning, "two gates up", "another two pines", the wrist coda, the flashlight reason and "thirty or forty", the pale stone and the pool, among others) and added the new ones (the fennel smoke and the Prometheus aside; Nikaso's frozen-cloaks story told on the stair; rent by the month). **CH8-3 RESOLVED** (F1 cut the sentence; only ch-07:p195 remains), **CH8-5 RESOLVED** ("Midway along the lane", ch-08:p13 = ch-05:p181), **CH8-7 RESOLVED** (one spare, one change: ch-08:p75, p84). CH8-6 is still open, narrowed: the bible still quotes the pre-F3 "The rock gave the drums back" (l.1069) and the pre-F4 "froze so hard on the way" (l.1259). No new contradiction or knowledge_gap. chapter-9.md not read.

## 2026-10-19: UPDATE (chapter 9, final text: post-writer, dialogue-polish, hook-craft, disruptor and continuity repair)

**Trigger:** chapter loop step D.5 for chapter 9.
**Inputs read:**
- `manuscript/chapters/chapter-9.md` as last written at 20:48:59, after the continuity repair (`evaluations/revision-chapter-9-continuity.md`: C-01, W-01..W-10). It has 202 prose paragraphs and five breaks (after p23, p80, p127, p141 and p171); the numbering agrees with the audit. Mid-run, the orchestrator reported that polish cycle 1 had started on chapter-9.md. This update is against the pre-polish text, and the orchestrator will run a re-sync.
- Also read: `ENTITY_STATE.yaml` (`last_updated_chapter: 8`); outline.md Ch.9–11 (plus Ch.12–13 for the notice and the goat); foundation §3 (Valens, the notice's legal basis); character-bible.md (Euthydikos, the Mara/Valens/Kallia Ch.9 blocks, the Ch.9 walk-on note, the at-risk list after Ch.9); `evaluations/continuity/chapter-9-audit.md` (priority table and suggested patches).

**Meta:**
- `last_updated_chapter: 9`; `chapters_tracked: [1..9]`.
- `paragraph_rule` is extended to Ch.9 with a shard map.
- There are 919 `ch-09:pYY` cites, all within p1..p202.
- Every single-quoted fragment on a line that cites Ch.9 was machine-checked against the cited paragraphs. The only misses are deliberate: outline and audit quotations, earlier-chapter text on mixed lines, and spans the extractor ran together.
- The YAML loads under a strict loader with no duplicate keys.

### Replaced (plan → prose)
- Mara: the Ch.9 location row; the three planned knowledge rows (the price of the god, the notice, "Valens is the man") are replaced by 17 prose rows.
- Valens: the Ch.9 location row; the planned knowledge row; the planned `legal_status` row. His `Lupus` alias now has a page source.
- Timeline row 9: the plan's "weeks" is replaced by "about four days, then the square".
- Objects: `lupus-reward-notice`, `manumission-inscription` and `curse-tablet` are rewritten from the page, with verbatim texts.
- Celer's `first_appearance` is confirmed at ch-09:p172, by proxy.
- `knowledge_index.oracle_access`: the plan row is replaced by page rows.

### Added
- **New characters:**
  - **`euthydikos`** (supporting; carded).
  - `euthydikos-wife` ("the mistress").
  - `euthydikos-door-slave`, `euthydikos-bee-man`, `delphi-smith`, `smiths-boy`.
  - `letter-cutter`, `aphrodisia`, `culvert-boy`, `goat-man`, `men-at-the-board`.
  - `women-at-the-lions-ch9` (**needs_review**: the page does not say whether any of them is the Ch.8 stranger or Nikaso).
  - Mention only: `xenon-son-of-euangelos`, `damon-son-of-aristion`, `nikandros-priest`, `manumission-private-witnesses` (grouped), `glykera`, `kirrha-eel-seller`.
- **New objects:**
  - `euthydikos-incense-stand` (chekhov_open: the bowl's lead "When I send").
  - `mistress-mirror` (chekhov_open).
  - `maras-money-rag` (background).
  - `goat-mans-she-goat` (chekhov_open, **needs_review**: it may or may not become the consultation goat).
- **Updated objects:** `taxi-drachma-coins` (knotted into the rag; last mention p171); `fathers-seiko-watch` (not mentioned); `consultation-goat` (ch9_note).
- **New locations:** `polygonal-wall`, `euthydikos-house`.
- **Ch.9 facts added to locations:** delphi, delphi-sacred-way, temple-of-apollo-delphi, delphi-market-square (the board beside the herald's door; goat pens by the fountain; the trough), castalian-spring (the drovers' end and the culvert), kallias-house, corinth, boeotia (the oil carts from Thebes), kirrha, patrae, amphissa, syracuse, thrace, philadelphia (the hardware store off Fortieth Street).
- **Mara:**
  - New alias "Kallia's Syracusan".
  - `worn_ch9` / `carries_ch9` / `marks_ch9` (a cut at the base of her thumb, hand not stated; the soot) / `hair_ch9`.
  - 12 traits.
  - Relationships with Euthydikos, the mistress, the cutter, the bee-man and the goat man.
  - The money-rag possession.
  - `knowledge_absent_ch9`; Ch.9 arc waypoint.
  - CONTINUITY COMMITMENT: **HELD** (no English).
- **Valens:**
  - `seen_ch9`; `on_the_notice_ch9` ("about thirty" against foundation's ~32 in AD 70 is an estimate on a notice, not logged as a conflict).
  - 5 traits; "reads but pretends he can't" is marked **UNCONFIRMED** on the page.
  - The pitch pot; 3 knowledge rows; `knowledge_absent_ch9`; waypoint.
- **Kallia:** 3 traits, 2 knowledge rows (who paid and how; the god's price after the fact), `knowledge_absent_ch9` (the notice is not shown reaching her), a location row and a waypoint.
- **Kleodamos:** `ch9_mention` (the manumission's dating formula).
- **Knowledge index:**
  - New **`lupus_notice`**. Mara's Valens = Lupus is recorded as INFERRED, UNSTATED. The men at the board do not connect the notice to him. Kallia is not shown.
  - Rows added to `syracuse_cover`, `maras_name` and `seiko_with_valens`.
- **Threads:**
  - New: `euthydikos-bowl`, `mistress-mirror`, `obol-owed-to-valens`, `goat-kept-warm`, `valens-literacy` (planned payoff Ch.11), `maras-living`.
  - `celer-and-the-frame` is opened on the page.
  - **`mending-the-seam` planned beat 9 WRITTEN.**
  - Ch.9 notes on oracle-access, the-where (the door named), romance, valens-known, syracuse-cover, maras-english-to-herself, kallias-fifth-coin, nymph-rumor and the four relics.
- **World rules:**
  - Ch.9 observations on women and the Oracle, and on the consultation price and procedure (pelanos, the city's terms in the archive, the trembling goat, the sponsor).
  - The sea/roads rule notes that the road from Boeotia reopened with the first carts.
  - New OBSERVED rules: manumission by sale to Apollo with paramone; two priests and a dedication kept at home; runaway notices copied and posted; curse tablets.
- **Organizations:** delphic-sanctuary (narrowed to one priest's private hire; treasury, archive); household-of-celer (the notice on the page); delphi-council ("the clerk", not identified with Sosandros).
- **Timeline events:** 9 rows (Dadaphorios AD 70 notice; Poitropios sale; midwinter mirror; the first carts; the four days; the smith's lead c. AD 62; the grandfather's gift; Aphrodisia's savings; the hardware store). The autumn-70 plan row gets a ch9_note.

### Contradictions
- **CH8-1: RESOLVED** by the page, on the guardian's recommendation. The decision to consult is shown in Ch.9 (p3, p21, p23, p26, p56). Kallia hears the price only afterwards (p166) and never refers to a told intent.
- **P5: RESOLVED** by the page. The notice was posted at Corinth "in the month Dadaphorios" (p172), after the sea shut, and it arrived "With the oil from Thebes. First carts since the snow" (p189). The repair cut "in the autumn" and "Boathoos".
- **CH3-7:** a ch9_note records a NEW FACT, not a conflict. The narration names the door for the first time ("*Where is the door I came in by, now it is shut?*", p23).
- **CH9-1 (info, OPEN):** the outline says "last autumn" and "the first spring traffic", and its premise has her learn of the runaway on the polygonal wall. The page says Dadaphorios, "First carts since the snow", and a board in the square. This is wording only.
- **CH9-2 (low, OPEN):** outline Ch.11–12 has a goat from Kirrha. The page opens a Delphi goat kept warm "till then" (p180).
- **CH9-3 (info, OPEN):** outline Ch.10's letter comes "with the first carter of the year", but Ch.9 has already spent "First carts since the snow".
- **CH9-4 (info, OPEN):** the bible's Ch.9 blocks quote pre-repair text. Examples: "Thraitta"; "it will hold" / "How long will it hold?"; "with two fingers… she stood for it"; "Warm it first"; "with her shoulders to me"; "over his own father"; "Nobody ever lost a wall."; "Come back with a man."; "I'll pay a smith a smith's price…"; "He went and told them…"; "the one office in Phocis"; "stood proud"/"squeeze-out". This waits on the W-11 bible sync.
- **All other open items** were re-checked with `recheck_ch9`; Ch.9 does not touch them. P1, P3 and P4 are unchanged.

No knowledge_gap. Every reference on the page has a path: "I know about the man" (ch-08:p101); "Kallia's Syracusan" (town knowledge after ch-07:p172); Valens knows she reads (ch-06:p328).

### For Ch.10–11
- **Money:** Mara has "The smith's price" (named by the smith as "Three drachmas, and the clay found") plus the two 1998 coins, in a rag. Nothing is counted on the page. She owes Valens an obol and is still holding it. The goat costs "More than that", and the sponsor's present and the man are unpriced. Do not count coins aloud, and give the purse fresh words (bible).
- **Valens:** he has stood at the notice and knows Mara saw him there. Whether he reads is still UNCONFIRMED; Ch.11 reveals it. Nobody in Delphi links him to "Lupus". The watch is still with him and was not mentioned in Ch.9. He still has not asked her name. Do not re-quote the notice's text (bible).
- **Kallia:** she knows who paid and how, and the god's price as Mara summarized it. She is not shown knowing about the notice. Ch.10–11 should account for what she makes of it, or keep her from it (audit N-19). Ch.10's letter needs fresh arrival wording and a reason to have sat at Kirrha (CH9-3).
- **Open threads:** the bowl ("When I send"); the mirror via the kitchen door; the obol; the warm Delphi goat versus the plan's Kirrha goat (CH9-2). Pay these off as texture or let them lapse, never as callback pointers.
- **Spent per the bible:** the redo-the-seam sequence (Ch.2, Ch.9); the wiped hand; the price itemized; the shiver explained; the silent look at the notice; "He let the gray drink first."
- **The door:** Mara now thinks of the crack as a door (p23). Still no "crossing" and no stated year.

## 2026-10-19: UPDATE (re-sync of chapter 9 after polish cycle 1, the bending fix and finalize F1–F4)

- Re-anchored every ch-09:pYY to the final page (chapter-9.md last written 21:28:18; 200 paragraphs; breaks now after p23, p80, p127, p141, p169). Cycle 1 cut old p160–p161 ("Who paid?" / "Euthydikos."), so old p1..p159 keep their numbers and old p162..p202 = new p160..p200 (918 explicit cites, 10 bare refs; the five cites to the cut lines rewritten). Removed the cut facts and quotes: "Who paid?", the thumb bleeding onto the paving, the soot under her nails, "No fire", "The bellows stopped.", the cutter's dusty eyebrows, the V-stroke dust and lichen, "boiled sausages", "looked at me then", "and not over me", "How long will it stand?", "went past me then", the ear-to-hive at the cut, "Hermes the Holder … hold her", "arm in to the shoulder", "surfaced", "and the rest" / "with the rest of it" / "with the rest", "nailed" and the hurried, cold-painted gypsum, "before I had asked a thing", "my wife's brother, and help them tie him", the second money-changer, and "I stayed where I was". Added the new facts: the dawn try is not made ("Kallia wanted the jars filled before she lit her fire … the stand would have to go to the priest as it stood", p129), which puts the curse-tablet morning on the inspection day, and Kallia gets a new house-order trait. The thumb wound is sucked at the bench (p123), reopens in the basin with "a thread of red into the black", and fades until "the water stayed black" (p163). Also new on the page: "No forge,"; "Will it stand?"; "left me for the court"; "smoking a hive"; "tight and glossy as cherries"; "floured all over with stone dust"; "Up to then … This question he asked of me."; "Hermes below … I nail her under the lead"; "lying on his belly with one arm down it"; "pegged to a pillar"; "with his mouth full"; "with the money"; "my landlord, and hold the rope"; "The men from the board"; one money-changer (p193); "I had his obol in the rag. I kept my place."; "more after that". Kallia no longer learns on the page who paid (knowledge row, relationship rows, waypoint and knowledge_absent updated). The page keeps "I was looking at him." (p198), not the revision log's "watching". CH9-1, CH9-2 and CH9-4 re-checked (recheck_cycle1). All stay RESOLVED, and the bible, rewritten at 21:35, quotes the cut strings only as cut. `last_updated_chapter` stays 9. No new contradiction and no knowledge_gap. The YAML loads under a strict loader with no duplicate keys. chapter-10.md was not read.

## 2026-10-19: UPDATE (chapter 10, final text: post-writer, dialogue-polish, hook-craft, disruptor and continuity repair C-01, W-01..W-08)

**Trigger:** chapter loop step D.5 for chapter 10.

**Inputs read:**
- `manuscript/chapters/chapter-10.md`, twice.
  - First in its post-disruptor state (98 prose paragraphs, last written 22:15).
  - Mid-run the orchestrator reported the book-editor's continuity repair. The update was held until the file had stopped changing and was then applied to the repaired page (last written 22:42:17; `evaluations/revision-chapter-10-continuity.md`).
  - The repaired page has **97 paragraphs and no breaks**:
    - old p1..p61 keep their numbers;
    - a new p62 (the reed blind) is added;
    - old p62..p93 = p63..p94;
    - old p94..p95 ("Shall I go up and open it?" / "He can lift a latch.") are cut;
    - old p96..p98 = p95..p97.
- `ENTITY_STATE.yaml` (`last_updated_chapter: 9`).
- outline.md Ch.10–12.
- character-bible.md: Kallia, Ariston, Nikaso, Sostrata and the Ch.10 walk-on note.
- `manuscript/reports/chapter-10-report.md`. It numbers paragraphs by file LINE and is stale in places, so it was used only as a list of claims to check.
- `evaluations/continuity/chapter-10-audit.md` (C-01, W-01..W-09, N-01..N-25).
- foundation §3 (Kallia).

**Meta:**
- `last_updated_chapter: 10`; `chapters_tracked: [1..10]`.
- `paragraph_rule` is extended to Ch.10, with a rough map and the repair's renumbering.
- New block `meta.ch10_requested_checks`.
- 715 `ch-10:pYY` cites, all within p1..p97.
- Every single-quoted fragment on a line that cites Ch.10 was machine-checked against the cited paragraphs. The only misses are deliberate: plan text, pre-repair or cut text (labelled as such), foundation quotes, and earlier-chapter quotes on mixed lines.
- The YAML loads under a strict loader with no duplicate keys.

### Replaced (plan → prose)
- **Mara:** the Ch.10 location row ("Kallia's kitchen" → the gate, the court, the step by the lean-to). The planned knowledge row is replaced by 9 prose rows.
- **Kallia:**
  - the planned knowledge row is replaced by 8 prose rows;
  - the arc waypoint;
  - the `ariston` relationship;
  - confirmations on "cannot read", "sweeps the threshold of her son's empty room" and "never says her son's name until the letter forces it once" (p94).
- **Ariston:** the whole block, written from the letter:
  - the left arm and right-handedness;
  - service and an early discharge with his savings "at the standards" paid out (repair W-04);
  - household: wife **Shalmath** (renamed from Domna by repair W-03), Iamblichos, the child, the roof, the bought land, the oxen;
  - the two years' silence; his boyhood (the mules, the drum, the snails); the greetings;
  - his `knowledge_absent`.
- **Objects:** `ariston-letter` (description, date, route, full text, beats; kept "in behind the cumin"; Ch.6 "Letters." link noted, not drawn by the page); the `kallias-broom` Ch.10 beats (CONFIRMED; `whose_room`: Ariston's).
- **Locations:** the Kirrha plan row ("first carter") is marked replaced; Emesa's plan row is confirmed.
- **Timeline:** row 10 and its events.
- **Threads:** `kallias-son` is **PAID** (coda Ch.16).

### Added
- **Characters:**
  - `elean-pilgrim` (minor; the bible says to card him if he returns as the lodger);
  - `man-from-patrae` ("Patrae" after repair W-06);
  - `shalmath` (with a `former_name` note), `shalmaths-mother`, `iamblichos`, `aristons-child`, `thrasyllos` (dead), `glaukes-girls`, `kirrha-wine-seller`;
  - `bakers-mother`, promoted from a relationship key under Sostrata (Ch.7, 8, 10).
  - Ch.10 notes on Nikaso (traits, 3 knowledge rows, `knowledge_absent_ch10`, location, the sieve in her house), Philista, Sostrata, the baker, the sieve neighbour and Valens (absent).
- **Mara:**
  - `worn/carries/marks/hair_ch10`;
  - 10 traits: reads aloud whole; could have edited and did not; the two-kinds-of-letter distortion; the misread yawn; the Homs postcard at Van Pelt; offers to write;
  - relationships with Ariston and the Elean; `knowledge_absent_ch10`; the arc waypoint;
  - the CONTINUITY COMMITMENT is **HELD** (no English).
- **Kallia:**
  - 13 Ch.10 traits, including the reed blind let down (new p62) and her order "If he comes to the gate before I find him, he waits in the court.";
  - `clothing_ch10`, `household_ch10`, a location row;
  - possessions: the good himation, the spindle, the knife and cumin niche, the letter, the reply obol, the blind;
  - relationships with the Elean, the man from Patrae, Shalmath and Iamblichos; `knowledge_absent_ch10`.
- **Locations:**
  - new: `syria`, `elis`, `aigion`, `van-pelt-library` (**needs_review**: possibly the same as `university-library`);
  - Ch.10 facts on kallias-house (the shut room is Ariston's; the lean-to, the niche and the blind; the gallery full of pilgrims; the lane), castalian-spring, delphi, kirrha, corinth, jerusalem, amphissa and emesa.
- **Objects:** `reply-obol` (chekhov_open, on the bottom stair); `lean-to-reed-blind` (background; the revision log asked for it). `kallias-sieve` gets a Ch.10 beat and a holder **conflict** sub-field (CH10-4).
- **Organization:** `aristons-cohort`.
- **Knowledge index:**
  - new `ariston_letter`: Mara has the whole text; Kallia has it as read to her; Nikaso has only living, the greeting, married and a child; the lane has "Syria, and a wife, and a child"; the Elean has no contents; Valens is not shown.
  - new `aristons_return`: only Mara and Kallia, by inference. Nikaso and the lane do not know; Nikaso expects him "home for the god's day". The page never states it.
  - Ch.10 rows on `lupus_notice` (Kallia still not shown) and `oracle_access`.
- **Threads:**
  - new `ariston-reply` (open; the one line "Tell him the baker's old mother is living."; the obol; the sheet from "The priest's household"; the carrier east for a cup; Iamblichos's name asked again).
  - Ch.10 notes on oracle-access, syracuse-cover, maras-english-to-herself, euthydikos-bowl, obol-owed-to-valens, goat-kept-warm, valens-literacy, maras-living and the four relics (none mentioned).
- **World rules:** the sea rule gets a Ch.10 observation (the gulf is open again). New OBSERVED rules: the Greek letter formula and its address; letters carried by favour for a cup; naming customs (Emesa: the mother's father; Delphi: the father's father); lodgings filling before the god's day at two to three obols a night; early discharge for a wound with savings paid out.

### Contradictions
- **CH10-1 (medium): RESOLVED by the repair.** The pre-repair line "Three nights, till the god opens his house" set the god's first day three days after Ch.10, against outline Ch.11 (a week) and Ch.12 ("three days off"). The page now reads "I'm here till the god opens his house." Forward constraint: at least about ten days between Ch.10 and the seventh of Bysios.
- **CH10-2 (low, OPEN):** the outline and foundation have "discharge land" and "never/not coming home". The page has land bought with his cohort savings and the dowry, an early discharge, and no word of a return.
- **CH10-3 (info, OPEN):** the outline's harbor road vs the page's "nobody he'd trust was bound for Delphi" and a sea passenger (CH9-3 honoured).
- **CH10-4 (low, OPEN):** this file's sieve holder "kallia" vs "your sieve still at my house" (p70). The pages agree with each other; the conflict is with the tracker's field.
- **CH10-5 (info, OPEN):** "three gates down" (p67) vs "Midway along the lane". Compatible only with about six gates.
- **CH10-6 (info, OPEN):** "no other name on that line for years" (ch-07:p169) vs a son gone since about the vintage of AD 68. It depends on when he left, which the page does not state.
- **CH10-7 (info, OPEN):** the bible's Ch.10 blocks and the writer's report quote many lines that are not on the final page, including everything the repair cut. Waits on the W-09 bible sync.
- **Requested checks:**
  - Kallia's age against Ariston's service: NO CONFLICT.
  - The council-list line: CH10-6.
  - The letter against the Syracuse cover and Aimilios: NO CONFLICT. Ariston is her cousin under the cover; exposure noted for any fuller reply.

No knowledge_gap. Kallia's "You read the clerk's wax" has a path (ch-07:p177). Nikaso knows of the son from before the story (prior knowledge). Nobody references Ariston before he is on the page.

### For Ch.11–12
- **The god's day:** no interval is stated now. Keep at least about ten days between Ch.10 and the seventh of Bysios, so that "come early for the god" means two weeks or more early. If the Elean lodges, he stays "till the god opens his house" at three obols a night.
- **Ariston's room:** let to the Elean by Kallia's word, with the broom across the threshold. Whether he takes it, and what becomes of the broom, is not on the page. The room's inside is unseen. Kallia has said "Ariston" once; per the bible, never again.
- **The reply:**
  - one line; Kallia's obol is on the bottom stair "For the sheet";
  - the sheet is to come from "The priest's household" (the priest is not named);
  - a carrier going east "for a cup", "when the boats go east";
  - Iamblichos is the likely address.
- **The letter:** behind the cumin in the lean-to niche, with the good knife.
- **Who knows he will not come home:** only Mara and Kallia, both by inference. Nikaso and the lane have "Syria, and a wife, and a child" and expect a visit for the god's day. Do not have anyone quote him saying he will not return.
- **Names:** Shalmath (not Domna); Patrae (not Patrai). Ariston's discharge brought his savings at the standards, not a bounty.
- **Kallia:** still not shown to know about the notice or Valens (audit N-19). Ch.11's cousin beat is the next chance to account for it or keep her from it. The sieve is CLOSED as a topic (bible).
- **Unchanged since Ch.9:** Mara's money (the smith's price plus two 1998 coins), the obol she owes Valens, the warm Delphi goat versus the plan's Kirrha goat, and the watch, which is with Valens and not mentioned.

## 2026-10-19: UPDATE (re-sync of chapter 10 after polish cycle 1, the cycle-2 PATH set and the finalize line)

- Re-anchored every ch-10:pYY to the final page (chapter-10.md last written 23:23:18, FINAL; 98 paragraphs, no breaks). Cycle 1 split old p21 after "…and spun." and moved the reed blind (old p62, text unchanged) to p22, before the reading, so old p1..p20 keep their numbers, old p22..p61 = new p24..p63, old p62 = new p22 and old p63..p97 = new p64..p98 (714 explicit cites, 54 bare refs; the 16 cites to old p21 assigned by content to p21 and/or p23). Removed the cut facts and quotes: the letter's material and size ("a strip of papyrus folded over and over … closed my fist on", the thread "twice" round it, "a strip the length of my forearm"), "crumbled off the knot in one piece", the thumbnail, "the best Greek I had spoken since October", the purse, the hanging spindle, "I could have left out the roof … could have told the difference", "Letters came in two kinds", "for the time it would have taken her to read it" and "It was seven letters", "She said it to the letter.", "that summer, and the Temple with it", "My voice went on through the oxen without me.", "from three gates down", "without moving my lips", the "fatter packet" refold, the shoes "at the pace she used for the spring", the tunic's "every so often it moved", the lean-to "where the hearth was". Added the new page: "One end of it", "The thread round its middle was knotted under a thumb of gray clay.", "The clay broke from the knot at the first push … mostly creases", "touched the place through her clothes", "Whatever was in a letter, I thought …", "the lean-to that held the hearth", the blind at the start of the spinning, "in the summer just gone, and its temple with it", "Kallia corrected none of it. The Greek was his, from beginning to end.", "The oxen and the man to drive them went by while I was at that desk.", "She was answering the letter", "and came no nearer … any name in Phocis", "from along the lane", "Nobody else … might as easily have made the roof into so much talk about rain", "The gate came to behind her and bounced once.", and "I read it all to myself, from the greeting down to the date, and rolled it up." (the final line, not the PATH's "over again"). **CH10-5 RESOLVED** by the page ("from along the lane" agrees with Ch.5 "halfway along" and Ch.8 "Midway along the lane"; no gate count). **CH10-7** re-checked: the bible, rewritten at 23:24:32, clears every listed quote but still quotes "I read it over again to myself" (l.180; l.2244), so it stays UNRESOLVED, narrowed to that line. CH10-1/2/3/4/6 re-anchored only. `last_updated_chapter` stays 10. No new contradiction and no knowledge_gap. The YAML loads under a strict loader with no duplicate keys. chapter-11.md was not read.

## 2026-10-20: UPDATE (chapter 11, final text: post-writer, dialogue-polish, hook-craft, disruptor and continuity repair C-01, W-01, W-02, W-04..W-13)

**Trigger:** chapter loop step D.5 for chapter 11.

**Inputs read:**
- `manuscript/chapters/chapter-11.md`, twice.
  - First in its post-disruptor state (284 prose paragraphs; md5 462637ff…, last written 02:08:00).
  - Mid-run the orchestrator reported the book-editor's continuity repair (`evaluations/revision-chapter-11-continuity.md`, from `evaluations/continuity/chapter-11-audit.md`). The update was finished, then re-anchored to the repaired page once the file had been unchanged for four minutes (last written 02:32:45; md5 1a9dc825…).
  - The repaired page has **277 paragraphs**, with breaks after p67, p147 and p223:
    - old p1..p127 keep their numbers;
    - old p128 ("No.") and p129 merge into new p128;
    - old p135 (the notice paraphrase) is deleted;
    - old p186..p190 become p184..p185;
    - old p225 (Mara's "No.") is deleted, and old p224 + p226 merge into p219;
    - old p227..p284 = p220..p277.
- `ENTITY_STATE.yaml` (`last_updated_chapter: 10`).
- outline.md Ch.11–13.
- character-bible.md: the Mara, Valens, Kallia, Felix and Praxias cards and their Ch.11 blocks, the Ch.11 walk-on note, and At-risk after Ch.11.
- `manuscript/reports/chapter-11-report.md`. It numbers by file LINE and quotes the pre-polish draft, so it was used only as a list of claims to check.
- `evaluations/disruption-chapter-11.md`, the continuity audit, and the repair log.

**Meta:**
- `last_updated_chapter: 11`; `chapters_tracked: [1..11]`.
- `paragraph_rule` is extended to Ch.11, with a shard map and the repair's renumbering.
- New block `meta.ch11_requested_checks`.
- 1,158 `ch-11:pYY` cites, all within p1..p277.
- Every quoted fragment on a line this run added or changed was machine-checked against the repaired page. The only misses are deliberate: bible, report and plan quotes, and cut text labelled as cut.
- The YAML loads under a strict loader with no duplicate keys. One duplicate this run would have created (Mara's `relationships.felix`) was merged into the planned row.

### Renamed
- `kallias-cousin` → **`praxias`** (`former_slug` kept). The page names him.

### Replaced (plan → prose)
- **Valens:**
  - The Ch.11 location row.
  - "reads but pretends he can't" is CONFIRMED on the page.
  - The figs, mind-reading and animal traits now cite the page.
  - The `felix` relationship (the Cilician, the Kirrha quay, freed by word, no paper).
  - The potted fig possession.
- **Mara:** the Ch.11 location row. The planned knowledge row is replaced by 22 prose rows.
- **Felix:** the block is rewritten from the page: first appearance, age "twelve or so", hair (after repair W-09), origin Side, traits, relationships, status, knowledge, and `knowledge_absent_ch11`. The plan rows are kept.
- **Timeline:** row 11 now covers about eight days. The disruptor removed the ordinal day stamps, so only the order is fixed.
- **Objects:**
  - `fathers-seiko-watch` Ch.11 custody: in his pouch, fast, wound daily, never set, not returned.
  - `potted-fig-tree`: introduced at ch-11:p15.
  - `consultation-goat`: the Kirrha seller and Felix with the barley.
- **Locations:** `valens-yard`, in full. There are no horses on the page.

### Added
- **Characters:**
  - `the-cilician`;
  - `kirrha-quay-eel-seller` (**needs_review**: possibly `kirrha-eel-seller`; not merged);
  - `the-amphissan`;
  - `plane-tree-wine-seller` (kept distinct from the Kirrha wine-seller);
  - `kirrha-goat-dealer`;
  - `boxers-before-the-god-sits`;
  - `boeotian-pilgrim-family`.
- **Other character notes:**
  - Sostrata's husband gets a quail note (**needs_review**: it assumes "the baker" is him).
  - The goat man gets a Ch.11 note.
  - Kallia: 2 traits, `household_ch11`, a location row, 2 knowledge rows, `knowledge_absent_ch11`, a waypoint, the `praxias` relationship and the reply obol's Ch.11 status.
  - Valens: the nose and the eyebrow nick, `seen_ch11`, 16 Ch.11 traits, a legal-status row ("Paper gets taken off you"), 9 knowledge rows (her name, "Mara"; the first wording of her question), `knowledge_absent_ch11` and a waypoint.
- **Locations:**
  - new: `praxias-house` and `side`;
  - Ch.11 facts on kirrha, aigion, delphi, castalian-spring, the temple, the market square, euthydikos-house and kallias-house.
- **Objects:**
  - `maras-question-sherd` (chekhov_open; pays off in Ch.13);
  - `felix-name-sherd`, `mended-breeching`, `sharpened-awl` and `muffled-mule-bells`;
  - `fig-jars-wager` (chekhov_open);
  - Ch.11 rows on the notice, the money (a `container` **conflict** sub-field), `reply-obol` (now in Mara's knot, unspent), `goat-mans-she-goat` (needs_review closed; not bought), `taxi-drachma-coins` and `borrowed-himation`.
- **Knowledge index:**
  - new: `valens_reads`, `maras_question`, `felix_freedom` and `the_agreement`;
  - Ch.11 rows on seiko_with_valens, mountain_trip_ch6, maras_name, syracuse_cover, oracle_access, lupus_notice and ariston_letter.
- **Threads:**
  - **PAID:** valens-literacy and obol-owed-to-valens;
  - **CLOSED:** goat-kept-warm (not bought);
  - **new:** `felix-no-paper` and `praxias-at-the-door`;
  - Ch.11 notes on romance, oracle-access, ariston-reply, felix-arena (seeded early), syracuse-cover, valens-papers (seeded), maras-english-to-herself (HELD), nymph-rumor, the four relics, seventh-of-bysios-phrase (0 used), the-where, valens-known, maras-living and kallias-fifth-coin.
- **World rules (OBSERVED):**
  - the order of the god's first day;
  - the Delphian at the door and the man who carries the question;
  - a freeing by word, with no paper.
- **Organization:** a Ch.11 fact on `delphic-sanctuary`.

### Contradictions (all new, all UNRESOLVED)
- **CH11-1 (info):** the bible's Ch.11 blocks and the writer's report quote draft lines that are not on the page:
  - from the dialogue-polish cuts: "At the end of summer I shall not be here", "It saves arguing", "Come then.", "In the day.", "Those want doing.", "Felix says you cannot read.", Felix's draft question bursts and "a gravel track";
  - the disruptor's cut simile;
  - every change the continuity repair made.
  
  The bible sync is handed off (audit W-14).
- **CH11-2 (info):** Mara's money is in "a rag" in Ch.9 and in "a knot at the corner of my himation" in Ch.11. The 1998 coins are not mentioned. A conflict sub-field sits on `maras-money-rag.container`.
- **CH11-3 (low; audit W-03, flagged at the orchestrator's request):** the money gap.
  - Costs: the cake is about 2 drachmas (Ch.9) and Praxias 1. The Kirrha goat is half a Delphi price that was above 3.
  - Total: about 4½ drachmas or more, against less than 3.
  - **Ch.12 must close it on the page.** Praxias's "three … if the priest's in a good temper" also sits against the smith's "Call it two".
- **CH11-4 (info):** Valens's Ch.6 cover ("You went up by yourself. You never had a watch.") is breached inside the yard.
  - Felix knows "the one he took up to Pan's in the snow". The path is not shown; town talk or Valens would explain it, so this is not a knowledge_gap.
  - Mara tells Felix the watch is hers.
- **CH11-5 (info):** a Boeotian pilgrim family comes up the Kirrha (gulf) road. The Boeotian road is a separate road.

Requested checks:
- The god's-day runway: **NO CONFLICT.** Ch.11 day 1 to Kirrha is about 10 days; with Ch.12's "three days off", the god's day is about 13 days or more after Ch.10.
- Paraphrase only. "Bysios" is not used.
- No reason is given for the agreement.
- The obol is PAID.
- The watch is still with Valens.
- Kallia is still not shown the notice.

The auto-resolution pass found no open conflict that Ch.11 touches. No knowledge_gap.

### For Ch.12–13
- **Kirrha, "the day after tomorrow, at daybreak",** with the oil string.
  - Mara brings her drachmas and wears "something you can walk back up in behind a goat".
  - The goat seller at Kirrha "lets you pick your own out of the pen".
  - Felix leads the goat with barley. He was asleep when the plan was made.
- **Money:** less than 3 drachmas, with Kallia's unspent papyrus obol knotted in. Close the gap on the page in Ch.12 (CH11-3 / W-03). Per the audit, the purchase must not be another counted-down haggle.
- **The Pentax** (needed in Ch.12) was last on the page in the duffel in Kallia's storeroom (ch-05:p208). It is not mentioned in Ch.11.
- **Valens** has read the first wording of her question, the one with "door", and has her name, "Mara", which he has not said aloud. The question he carries is "Where is my road home?". The priest is to get "The clerk's" name, Maira. Do not point at the road/door match against the god's answer.
- **Praxias at the door for a drachma** is not in outline Ch.13 (`praxias-at-the-door`).
- **Felix** believes Valens cannot read. He knows of the Pan's-cave trip and that the watch is Mara's. He has no word of the notice.
- **Kallia** knows only that Mara works the yard unpaid.
- **The watch:** Valens has never set it. The plan's Ch.18 return, "set near noon by the shadow", needs him to learn to set it.
- **Spent:** Valens's bare "No." is capped at one a chapter from Ch.12 (audit C-01). Also spent: the notice's text (do not paraphrase it) and a road-watching beat before the ambush.

## 2026-10-20: UPDATE (re-sync of chapter 11 after polish cycle 1 and finalize F1/F3/F4)

- Re-anchored every ch-11:pYY to the final page (chapter-11.md last written 03:12:29, md5 bef094c6…; 278 paragraphs, breaks after p67, p148 and p224). Cycle 1 split old p114: new p114 is Mara's full answer, "A lock does. In my country every door has its own.", and new p115 is "He was on his feet then, and the bells were in my lap …". So old p1..p113 keep their numbers and old p115..p277 = new p116..p278. That covers 1,156 explicit cites (732 at or after old p114) and 152 bare Ch.11 refs (91 shifted). The 11 lines citing old p114 were assigned by content to p114 and/or p115.
- **Removed** the cut facts and quotes:
  - Valens's broken nose ("healed a shade crooked", and "the healed break in his nose" at the near-kiss), taken out of valens.physical.distinguishing and out of Mara's knowledge row.
  - Felix's tunic and rope belt (the clothing_ch11 row is deleted) and "stood up every way at once".
  - "a knot at the corner of my himation" and "untied the knot".
  - "a family from Boeotia".
  - "a dozen" bells.
  - "Women?" / "Women too.", "Who isn't?" and the cut-off "In my country—".
  - "with great bitterness".
  - "kept his eyes on the hoof", and the black's talk as "Latin, and low" (the language is no longer stated).
  - "lit and there before the word was well out", "Felix reached him before Praxias had the last word out." and "Before his name had finished".
  - The narrated non-answers: "Valens gave him no answer", "He let it be.", "He let that go by him.", "That got no answer." and "I let the question stand".
  - The lead-rope knot hung up "with the knot still in it".
  - "his head coming down", "my knees put me onto it", "very low" and "had not broken so much as".
- **Added** from the new page:
  - "three drachmas in the rag at my belt" (p10) and "I untied the rag first" (p21).
  - "a thin one of twelve or so, with straw in his hair" (p16).
  - "a family of Achaeans" (p69). The character boeotian-pilgrim-family is renamed achaean-pilgrim-family.
  - bells "heaped in his lap" (p98).
  - "Children?" / "Once they are old enough to be late." (p103; p104).
  - "I am." (p111).
  - the lock line (p114). Valens now knows that "every door has its own" lock in her country.
  - the boot lace: "with a foot up on the bench, to put a new lace in his boot" (p225) and "He ran the lace on up the shin and tucked the end in." (p241). This is the new valens.physical.clothing_ch11. Whether it replaces the knotted lace of ch-07:p96 is not stated.
  - "He was a while silent." (p238, F1).
  - Felix's "You've never seen anything." untagged (p123, F3).
  - "the old thread had been sawn through" (p55, F4).
  - "He came nearer, and my face lifted to meet his." (p245) and "The packsaddle had been on its trestle at my back, and I was on it" (p247).
- **CH11-2 RESOLVED** by the page. The money is in the rag again, which agrees with Ch.9. The 1998 coins are still not mentioned and are not said to have left the rag.
- **CH11-5 RESOLVED** by the page. The family is Achaean, from across the gulf, which agrees with the Aigion boats (p273).
- **CH11-1 rechecked and widened.** character-bible.md was last written at 01:45, before the polish, and still quotes these cut lines:
  - "healed a shade crooked" and "the healed break in his nose" (l.395-396)
  - "a knot in a lead rope" and "with the knot still in it" (l.405; l.421)
  - "Who isn't?" and "In my country—" (l.191; l.429; l.2602)
  - "He let that go by him." (l.441; l.2586)
  - "my knees put me onto it" (l.206)
  - the tunic and rope belt (l.778)
  - "with great bitterness" (l.787)
  - "a family from Boeotia" (l.1502)
  - "very low" at the agreement (l.439)
- CH11-3 and CH11-4 are re-anchored only.
- `last_updated_chapter` stays 11. No new contradiction and no knowledge_gap. The YAML loads under a strict loader with no duplicate keys.
- **For Ch.12 onward:** Valens's nose is no longer broken on the page, so do not bring a broken nose back without a cause. His face on the page is the eyebrow nick and the scar on his right hand.

## 2026-10-20: UPDATE (chapter 12, "The Kirrha Road", final text: post-writer, dialogue-polish, hook-craft, disruptor and continuity repair C-01, W-01..W-23)

**Trigger:** chapter loop step D.5 for chapter 12.

**Inputs read:**
- `manuscript/chapters/chapter-12.md`, twice.
  - First in its post-disruptor state (184 paragraphs, breaks after p60 and p116; md5 c72f8bff…, last written 04:16:24; commit 7c5e2e0).
  - Mid-run the continuity audit (`evaluations/continuity/chapter-12-audit.md`, commit ded5077, 1 CRIT / 23 WARN) and the book-editor's repair (commit b43a454, 04:43) landed. The repair edited the chapter, foundation §3 and outline Ch.17/Ch.22. The update was re-anchored to the repaired page (last written 04:42:39, md5 81e139f9…), which had stopped changing.
  - The repaired page has **182 paragraphs**, with breaks after p59 and p114:
    - old p1..p14 keep their numbers;
    - old p15 ("I watched the stones in front of my feet.") is cut;
    - old p16..p98 = new p15..p97;
    - old p99 ("He was quiet for a while.") is cut;
    - old p100..p184 = new p98..p182.
- `ENTITY_STATE.yaml` (`last_updated_chapter: 11`).
- outline.md Ch.11–15; foundation §3 (before and after the patch).
- character-bible.md: the Ch.12 blocks, the walk-on note and At-risk after Ch.12.
- `evaluations/disruption-chapter-12.md`; the continuity audit, including its SUGGESTED YAML PATCHES.
- Ch.5–11 pages, for the money, the camera, the duffel, the notice, the mules and Praxias's price.

**Meta:**
- `last_updated_chapter: 12`; `chapters_tracked: [1..12]`.
- `paragraph_rule` is extended to Ch.12, with a shard map and the repair's renumbering.
- New block `meta.ch12_requested_checks`.
- 1,000+ `ch-12:pYY` cites, all within p1..p182.
- Every quoted fragment on a changed line was machine-checked. Each fragment is on the repaired page and inside a paragraph its line cites. The exceptions are deliberate: bible, plan and pre-repair quotes that are labelled as such.
- The YAML loads under `yaml.safe_load` and under a strict loader with no duplicate keys.

### Replaced (plan → prose)
- **Timeline:** row 12. One day, the fourth of Bysios (derived from "It was three days to the seventh of Bysios.", p180), two days after Ch.11's last evening.
- **Location rows:** the Ch.12 rows for Valens, Mara and Felix.
- **Valens:** the Ch.12 waypoint.
- **Mara:** the two planned knowledge rows, replaced by 19 prose rows.
- **The freedman:** `plautias-brothers-freedman.first_appearance` (told, p101).
- **Objects:**
  - `fathers-pentax-k1000`: the Ch.12 beat.
  - `lens-cap`: LOST.
  - `consultation-goat`: the Ch.12 beat.
  - `lupus-reward-notice`: resolution note.
- **Knowledge index:** the planned rows in `dowry_suit_witness`, `lupus_notice` and `oracle_access`.
- **Re-synced to the patched foundation/outline (old text kept as `was`):**
  - `valens.legal_status[0]`;
  - Celer's contested-manumission trait;
  - the world rule on contested arena manumissions;
  - `manumission-record.note`.

  Each now reads: the freedom was registered, and Celer claims a prior sale.

### Added
- **Characters:**
  - `the-talker` (dead);
  - `big-man-with-the-stick` and `third-man-kirrha-road` (both alive and fled; both heard "Mara." and saw the camera);
  - `graybeard-with-the-donkey`, `graybeards-women`, `graybeards-boy` and `graybeards-son`;
  - `kirrha-headman`, `kirrha-sprat-woman`, `kirrha-oil-men` and `lamp-tray-man`;
  - `gallery-lodgers-ch12` (**needs_review**: possible overlap with achaean-pilgrim-family and the Elateian boxer; not merged).
- **Told-only figures:** `the-gaul`, `corinth-lanista`, `corinth-games-magistrate`, `plautias-mother`, `plautias-father`, `plautias-hairdresser`, `celers-second-false-witness`, `celers-steward`, `gulf-fisherman`, `corinthian-mule-dealer` and `spiculus`.
- **Mara:** `worn/carries/marks/hunger/hair_ch12`, 13 Ch.12 traits, `knowledge_absent_ch12`, a waypoint, a sandals possession, and Ch.12 statuses on Valens, Kallia, Felix and Praxias. She asks no question in the whole chapter.
- **Valens:** `seen/clothing/marks_ch12`; 14 Ch.12 traits, including the shaking at the fall and the telling; a legal_status row; 7 knowledge rows, including "He'll have told them where he found me." as his inference; `knowledge_absent_ch12`; possessions (the talker's knife, the purse, the seized tablet, the cloak); the `marcus` relationship; a Ch.12 note on the Lupus alias.
- **Felix:** `marks_ch12`, 9 traits, 7 knowledge rows, `knowledge_absent_ch12` and a graybeard relationship.
- **Kallia:** `household_ch12`, a location row and `knowledge_absent_ch12`.
- **Plautia, Celer, Marcus, Plautia's brother:** first page mentions (told) and Ch.12 traits.
- **Nero and Vespasian:** Ch.12 traits. **Kirrha goat dealer:** "the Aigion man", now on the page.
- **Locations:**
  - new: `kirrha-road` (the olive terraces above the bare plain, the ditch, the ford, the cleft and pool, the climb, the view), `kenchreai` and `celers-house`;
  - Ch.12 facts on kirrha, corinth, lechaion, aigion, delphi, parnassus, kallias-house and valens-yard.
- **Objects:**
  - new: `talkers-knife` (chekhov_open), `dead-mans-purse` (lost in the stream), `olive-wood-stick`, `cracked-oil-jar` (heaved among the olives) and `valens-manumission-tablet` (seized, 69);
  - Ch.12 rows on the Pentax, film-roll (0 frames), Seiko, money rag, reply-obol, taxi coins, question sherd, flashlight, duffel and borrowed himation.
- **Knowledge index:**
  - new: `valens_frame`, `kirrha_road_killing` and `maras_camera`;
  - Ch.12 rows on seiko_with_valens, valens_reads and the_agreement.
- **Threads:**
  - new: `kirrha-road-killing` and `kallia-told`;
  - Ch.12 notes on celer-and-the-frame, valens-papers, romance, valens-known, plautias-son, felix-arena, the relics (film, watch), seventh-of-bysios-phrase (USED 1 of 3), maras-english-to-herself (HELD), oracle-access, valens-literacy, maras-living and praxias-at-the-door.
- **World rules (OBSERVED):**
  - the wooden sword and the magistrate's book;
  - the dowry share and the father keeping the boy;
  - Celer's prior-sale claim;
  - the freedom and "Robbers off every boat";
  - "the god's road";
  - the precinct's rod-slaves;
  - the high grazing.
- **Organizations:** Ch.12 facts on household-of-celer, corinth-record-office and delphic-sanctuary.

### Resolved
- **CH11-3 (low), the money gap: RESOLVED by the page.**
  - The goat is paid by Mara from her rag ("the rag was thin after it", p118).
  - The sprats are paid by Valens (p118).
  - The dead man's denarii and Corinthian bronze cover "the cake, and Praxias's drachma, and leave plenty over" (p132); "Keep what he doesn't" (p134).
  - Verified against ch-09 and ch-11: no figure clashes. The goat, the cake and Valens's part stay unpriced.
- **Plan gap "How Celer learned …": CLOSED** on the audit's recommendation (W-11). As repaired, Valens infers it: "He'll have told them where he found me." (p101).
- **The Ch.11 forward constraint "the Pentax was last in the duffel": SUPPLIED.** "I had carried it since the lodgers came … under my chiton on its strap" (p78).

### Contradictions
New and UNRESOLVED:
- **CH12-1 (info):** the bible's Ch.12 blocks quote the writer's draft. They predate dialogue-polish, hook-craft, the disruptor and the repair, so lines like these are off the page:
  - "The glass is whole.", "five drachmas", "That's how it gets told.";
  - the Craneion, "A quay doesn't ask twice", "brought knives", "without looking in it";
  - "People do, mostly.", "Her, and nobody else.";
  - the boot lace, "mule-man", the propped jar;
  - "Was it one blow?" and Felix's draft questions.

  The bible sync is handed off.
- **CH12-2 (low):** the archive record is "the magistrate's book" on the page (p87; p97), but outline Ch.17 still has "The bronze-and-wax diptych". The repair aligned the legal claim, not the record's form. **Ch.16–17 must take the book (or a leaf of it) or show where a diptych comes from.**
- **CH12-3 (info):** "I carried on the Kirrha quay that winter … The mules came after" (p97) against Kallia's mule eating the pomegranate "last winter" (ch-06:p49). Compatible only if the mules came during that winter.
- **CH12-4 (info):** "the first boats of the year" at the mole (p116), although boats were already crossing from Aigion (Ch.10, Ch.11).
- **CH12-5 (info):** the outline's "Celer's men". The page never says who sent the three; their sender is Valens's inference only ("He wants me in a ditch."; "He'll have told them where he found me."). The bible's "came on the Lechaion boat" is not stated.
- **CH12-7 (info):** Valens ("Is it broken?") and Felix ("Is it silver?" / "It was my father's") have seen the camera before outline Ch.15's showing.
- **CH12-8 (info):** whether "Valens" is his own name, the book's name or a quay name is open ("They asked my name and I gave them Valens.", p97). This bears on Ch.17 and Ch.22.
- **CH12-9 (info):** wording departures from outline Ch.12:
  - the cap ends in the oil, not the dust;
  - the shaking happens at a pool above the ford;
  - the copy came "after the snow, with the oil carts";
  - the chapter ends before the goat is home;
  - the onions are not tied to Thrace;
  - after his flight Valens carried on the Kirrha quay.

New and RESOLVED in the same run:
- **CH12-6 (info):** "Those three brought knives." against one knife and a stick. Found in the post-disruptor text; the repair made it "Those three brought none."
- **CH12-10 (low):** foundation §3's "never registered before a magistrate" against the page's entered freedom and Celer's prior-sale claim (the audit's W-21). Not caught by this run before the patch, and logged for the trail. Settled when commit b43a454 patched foundation §3 and outline Ch.17/22.

The auto-resolution pass found that no other open flag is touched (CH11-4 rechecked; unchanged). No knowledge_gap.

### For Ch.13 onward
- **The goat:** Spicula to Felix, "the god's" to Mara. She is to be brought to Valens's yard "the evening before" (p171). Where she spends the three nights is not stated (implied with Mara).
- **Valens's marks at the consultation:** the graze, the welt on the left forearm, the split left knuckles and the shoulder bruises (audit I-15).
- **Mara's rag** now holds the dead man's silver, never itemized.
- **Kallia** is to be told "the whole of it" (p176; p177). Until then she has only the walkers' story.
- **Felix** knows the cover story, but not Lupus, the frame or the notice.
- **The two who ran** heard "Mara." and saw the camera.
- **The lens cap** is gone and the filter ring is dented. voice-bank sample-13's "I put the cap back on the lens" is now impossible (audit I-14).
- **The watch** has no touch until Ch.18 (audit I-13).
- **The allowlisted phrase** "the seventh of Bysios" is at 1 of 3.

## 2026-10-20: UPDATE (re-sync of chapter 12 after polish cycle 1 and finalize F1/F2)

- **Input:** `git diff 4e9d889 HEAD -- manuscript/chapters/chapter-12.md` (commits 601fd5c, 2b91fa6). chapter-12.md was last written 05:17:56 (md5 38895374…). It still has 182 paragraphs, with the breaks after p59 and p114. A paragraph diff shows nothing added, cut, split or merged, so **no ch-12:pYY is renumbered**. Text changed inside p2, p11, p22, p27, p28, p45, p55, p57-p59, p62, p65, p67, p73, p74, p77, p78, p84, p90, p96, p103, p112, p126, p130, p132, p148, p160, p171 and p172.
- **Method:** a word 3-gram and 4-gram diff (old page against new page) found every ENTITY line that carried cut wording. 65 lines were corrected. All 35 new quotes were machine-checked against the paragraphs they cite.
- **Removed as page facts** (cut from the page):
  - "The glass was whole." and "no filter would screw onto it now";
  - "The flashlight could take its chances.";
  - the cap's reason clause ("a black disc … off any boat");
  - "A copy came up here after the snow, with the oil carts.";
  - the rod-slaves line ("Inside the precinct there's a slave every few paces with a rod.");
  - "Praxias's drachma";
  - "and the talker's knife" at p45;
  - "so that she would carry level" and "His hands were sure at it.";
  - "the way a man asks a price";
  - "When the god's day is done,".
- **Corrected to the page:**
  - "It caught him above the ear.";
  - "My himation came tight across my throat from behind.";
  - "The camera was still in my arms.";
  - the graze ("with grit in it");
  - the pool ("a clear pool over pale gravel");
  - the cloak ("darned at the hem with green thread");
  - "and it stung.";
  - "The cold had my feet again.";
  - "I saw it too.";
  - "A knife in the precinct would have a hundred men on it.";
  - "The goat comes to the yard the evening before.";
  - "When it's over,";
  - Felix's "I hit him over the head" (F2).
- **The talker's knife:** now acquired at p35 only ("There was a knife in his hand, and it was not his own."). `the-talker` keeps its slug, but its canonical_name now says the page never uses "the talker". The narration has "The man", "the man with the knife", "the dead man's" and "the stranger's knife".
- **Lens cap:** the clause now ends "where I meant it to stay" (p78), and no reason is given. "face up" survives only at p30.
- **Glass:** the page no longer says the glass is unbroken. What it does say: "The ring at the front of the lens had taken the blow and was pushed in at one point. In the finder the plane trees stood upright and in focus." (p77) and "Only the rim is bent." (p80). `fathers-pentax-k1000.physical_ch12` records that whether the glass is whole is not stated.
- **CH11-3 (RESOLVED, mirrored):** the purse now covers the cake "with plenty over" ("This would, with plenty over.", p132). Praxias's drachma is no longer named, so how he is paid is implied, not stated. No figure clashes, so the resolution stands.
- **CH12-1 (UNRESOLVED, widened):** the bible, still last written 03:57, also quotes these cut lines:
  - l.244, l.247, l.249, l.253-254, l.257;
  - l.259 and l.2904;
  - l.547, l.566-567, l.571-573, l.967.

  The eval named three stale strings ("Was it one blow" / "People do, mostly" / "gets told"). They sit on the two CH12-1 lines (`plan`, `note`), and those lines record the bible, not the page. They are kept, because the bible still carries them, and are now explicitly labelled bible-only. One correction: "He had his robbers…" was on the post-disruptor page and was cut by the repair, so it is not a wording "the page never used".
- **CH12-9 (UNRESOLVED, narrowed):** Ch.12 no longer says how the copy reached Delphi. Ch.9's carts stand alone (ch-09:p186), and that departure from the outline is gone.
- **Meta:** `meta.revalidation_needed` has a Ch.12 row (RESOLVED). `paragraph_rule`, `last_updated_by`, `mode`, `source` and the header comment are extended. `yaml.safe_load` and a strict no-duplicate-key loader both pass.
- **No new contradiction and no knowledge_gap.** For Ch.13 onward:
  - do not rely on "the glass was whole", a filter, the flashlight's Ch.12 position, the rod-slaves or "the god's day" as Ch.12 page facts;
  - the page does not itemize the dead man's silver.

## 2026-10-20: UPDATE (chapter 13, "The Seventh of Bysios", final text: post-writer, dialogue-polish, hook-craft, disruptor and continuity repair C-01, W-01..W-20)

**Trigger:** chapter loop step D.5 for chapter 13.

**Inputs read:**
- `manuscript/chapters/chapter-13.md`, twice.
  - First in its post-disruptor state (246 paragraphs, breaks after p46, p97, p139 and p193; md5 c460aab…, last written 06:27:43; commit 323175f).
  - Mid-run the continuity audit (`evaluations/continuity/chapter-13-audit.md`, commit 25d23b9, 1 CRIT / 20 WARN) and the book-editor's repair (commit a94ddd5, 06:52) landed. The update was re-anchored to the repaired page (last written 06:51:47, md5 1585521856c90a53e3c9164b659a8fa8), which matches HEAD and had stopped changing.
  - The repaired page has **245 paragraphs**, with breaks after p45, p96, p138 and p192 (five shards: A1 p1-p45, B1 p46-p96, A2 p97-p138, B2 p139-p192, B3/A3 p193-p245):
    - old p1 and old p2 are merged into new p1 (W-20);
    - old p3..p246 = new p2..p245.
  - Text changed inside new p2, p10, p22, p24, p28, p47, p90, p101, p109, p114, p115, p123, p127, p129, p137, p149, p166, p178, p182, p210 and p225.
- `ENTITY_STATE.yaml` (`last_updated_chapter: 12`).
- outline.md Ch.12–15; foundation §3 (Theano, Felix); character-bible.md (the Ch.13 blocks, THEANO, PRAXIAS, the Ch.13 walk-on note, At-risk after Ch.13).
- `evaluations/disruption-chapter-13.md`; the continuity audit, including its SUGGESTED YAML PATCHES.
- Ch.1, 7, 8, 9, 10, 11 and 12 pages, for the slide shows, the registration, Theano's Ch.8 glimpse, the almonds, "In four months", the agreement and the three days.

**Meta:**
- `last_updated_chapter: 13`; `chapters_tracked: [1..13]`.
- `paragraph_rule` is extended to Ch.13, with the shard map and the repair's renumbering.
- New block `meta.ch13_requested_checks` (14 checks).
- 1,237 `ch-13:pYY` cites, all within p1..p245.
- Every quoted fragment on a new or changed line was machine-checked against the repaired page and the paragraphs its line cites. The exceptions are deliberate: plan, bible, audit and pre-repair quotes, each labelled as such.
- The YAML loads under `yaml.safe_load` and under a strict loader with no duplicate keys.

### Replaced (plan → prose)
- **Timeline:** row 13. One day, the seventh of Bysios AD 71 (the title; the prose never names it), three days after Ch.12's fourth ("I had not had her to myself in three days.", p2). The fifth and sixth are dated from the page (the donkey man's story; the boxing; the goat to the yard at sundown). Against the arrival: about four and a half months or more (Boathoos to Bysios; ch-10:p20 "In four months" plus at least thirteen days). No clash.
- **timeline_events:** the planned "seventh of Bysios … the consultation" row; new rows for Theano's widowhood (c. AD 57), the fifth, the sixth, the seventh and the promised eighth.
- **Location rows:** the Ch.13 rows for Mara, Valens and Theano (two rows: the ramp and the adyton; her doorstep).
- **Knowledge:** the planned Ch.13 rows for Mara (the answer, Pompeii, the WHEN), Valens (the answer) and Theano (Pompeii, the hour), replaced by page rows.
- **Waypoints:** Mara's and Valens's Ch.13 rows.
- **Theano:** `first_appearance` (the Ch.8 glimpse, then the first live appearance and her name), the planned ibuprofen trait.
- **Objects:** `ibuprofen` (used up: "I had the Advil in my belt, down to its last two.", p28; the last two to Theano, p222), `consultation-goat` (CLOSED: she shakes under a jar, p42), `maras-question-sherd` (CLOSED: answered; the sherd is not on the page).
- **Knowledge index:** the planned rows in `door_location`, `door_when` and `oracle_access`.
- **The rename:** `temple-slave-delphi` → `jug-boy` (the page's summoner, "the jug boy", p193; p194). `former_slug` is kept.

### Added
- **Characters:**
  - `kleon` (mention only; "Praxias son of Kleon, of Delphi", p49);
  - `elateian-boxer` (split out of `boxers-before-the-god-sits`; **needs_review**: possibly the "priest's cousin from Elateia" of `gallery-lodgers-ch12`);
  - `altar-priest-ch13`, `prophetes-ch13` (**needs_review**: possibly Euthydikos, CH13-6), `pythias-escort-priests`, `women-at-the-terrace-wall`, `rod-men-ch13`;
  - `boeotian-on-the-bench`, `man-with-the-cough`, `amphissan-woman-at-the-wall`, `amphissan-womans-husband` (**needs_review**: possibly `the-amphissan`, the Ch.11 quail-fighter; not merged);
  - `bandaged-phocian-boy`, `clay-ear-seller`, `thessalian-family-with-ram`, `island-fig-seller`;
  - told only: `theanos-husband`, `theanos-sisters-son`, `former-pythias`, `felixs-mother`, `kirrha-sailor-capua`, `valens-school-trainer`, `pindar` (unnamed on the page).
- **Theano:** two physical rows (veiled at dawn; off duty), `voice_from_below`, seven Ch.13 traits, page confirmations on four plan traits, seven knowledge rows, `knowledge_absent_ch13` and a first `relationships` block.
- **Mara:** `worn/carries/marks/hair_ch13`, 12 Ch.13 traits, 20 knowledge rows, `knowledge_absent_ch13`, Ch.13 statuses on six relationships, two new relationships, possessions (Advil, money, Pentax).
- **Valens:** `marks_ch13` (three days on: the crusted scrape with a bruise below it; the left-forearm bruise purple to yellow; the knuckles "scabbed over, all four"; the shoulders "all of a piece"; agrees with Ch.12), `clothing_ch13`, 13 traits, 9 knowledge rows, `knowledge_absent_ch13`, four relationship statuses and three new relationships, and `ch13_setup` on the Ch.14 floor row.
- **Felix:** `marks_ch13`, 9 traits, 9 knowledge rows, `knowledge_absent_ch13`, 3 new relationships and a location row.
- **Kallia:** 6 traits, `household_ch13`, a location row, 7 knowledge rows, `knowledge_absent_ch13`, 2 new relationships and a waypoint.
- **Praxias:** his father (Kleon), 5 traits, a location row, knowledge and `knowledge_absent_ch13`; `planned` is marked PAID.
- **Euthydikos:** 3 offstage traits (the registrar; Theano's "square beard", inferred; the bowl summons), knowledge, a location row and a `valens` relationship. **His door slave:** the Ch.13 errand.
- **Emilio:** the Tarquinia slide memory (kitchen, September, a bedsheet over the china; agrees with ch-01:p11).
- **Locations:**
  - new: `theanos-house`, `mount-etna`, `tarquinia`, `capua`, `elateia`;
  - Ch.13 facts on temple-of-apollo-delphi (the terrace, the Chian altar, the porch maxims, the inside as Valens saw it, Theano's seven steps), delphi-sacred-way, castalian-spring, kallias-house, delphi, euthydikos-house, syracuse, pompeii (first named on the page), maras-apartment, valens-yard, corycian-cave and delphi-modern.
- **Objects:**
  - new: `consultation-record` (the god's book: Maira of Syracuse; Praxias son of Kleon; the carrier entered as Felix; Valens's own name kept out) and `theanos-barley-basket` (the god's laurel brand);
  - Ch.13 rows on the Pentax, the money rag, the dead man's purse, the Lupus notice, the incense stand, the slide carousel and the painted false door.
- **Knowledge index:**
  - new: `the_answer`, `consultation_record` and `theano_identity`;
  - Ch.13 rows on `door_location`, `door_when`, `oracle_access`, `maras_question`, `kirrha_road_killing`, `maras_camera`, `valens_frame`, `lupus_notice`, `syracuse_cover`, `mara_origin`, `maras_name` and `the_agreement`.
- **Threads:**
  - new: `the-non-greek-word` (a word in the Pythia's voice, given twice, not Greek, left out by the priest; the page never says it was "Pompeii");
  - PAID/CLOSED: `the-where` (secondary payoff Ch.19 still planned), `oracle-access`, `praxias-at-the-door` and `kallia-told`;
  - Ch.13 notes on the-when, theano-phrase (1 of 3), seventh-of-bysios-phrase (title, 2 of 3; the prose never says it), euthydikos-bowl, felix-no-paper, kirrha-road-killing, return-to-the-cave, syracuse-cover, valens-known, felix-arena, romance, maras-english-to-herself (HELD), valens-literacy, maras-living and maras-stated-return.
- **World rules (OBSERVED, Ch.13):** eight:
  - the day's order, and bought precedence;
  - wreaths, branded cakes and votive ears;
  - the goat test in practice;
  - registration;
  - the procedure inside;
  - the answer made verse, with the non-Greek word left out;
  - the Pythia's life and her stool;
  - betting on the god's answers, and men telling men first.

  `ch13_observed` is added to the two plan rules (women ask through a man; monthly days and the shiver).
- **Organizations:** Ch.13 facts on delphic-sanctuary and delphi-council.

### Resolved
- **CH8-2 (info), Theano's Ch.8 glimpse: RESOLVED by the page.**
  - She is named ("Theano wants her.", p195; "The god's woman," p197).
  - She is recognised by her house, as planned: "the house next to the highest", the squared stone, the crows (p208).
  - The god's barley and the lie are shown by the brand, not stated. The basket's laurel leaf (p210) matches the cake-trays (p22). Against it: "That's my own barley," (p223) and "The brand on the basket was by her foot. I left it there." (p226).
  - One wording difference remains and is not a conflict: the crows sit on her own roof-ridge, not the sanctuary's.

New and RESOLVED in the same run (the post-disruptor page, settled by the repair):
- **CH13-2 (low):** the post-disruptor page never said the pills were the last. Now it does: "down to its last two" (W-18).
- **CH13-5 (medium):** the Elateian asked Felix "what you'd hit the man with", a blow by Mara he could not know. This run logged it as a knowledge_gap. The page now reads "what the man was hit with" (W-06), so the cover holds and **no knowledge_gap remains**.
- **CH13-9 (CRITICAL; found by the audit, C-01, not by this tracker):** "Or Sicily after all, or the Bay of Naples, or Spain." named Campania a page before "Pompeii.". This run's first draft had recorded the bay as a neutral detail and did not flag it. Now: "Or Sicily after all, or Massalia, or Spain." (p166). **No CRITICAL stands on the final page.**
- **CH13-10 (low; audit W-07):** the slide show was in a dining room, in winter, on a tablecloth. It is now the kitchen, September and a bedsheet, as in ch-01:p11.
- **CH13-11 (low; audit W-02):** Praxias went "down the Way" to the uphill stadium. Now he goes "off up past the theater" (p129).
- **CH13-12 (low; audit W-03):** "Since the road the house had been full" contradicted Ch.12's "All week". Now: "All that week the house had been full to the eaves." (p2).

### Contradictions
New and UNRESOLVED:
- **CH13-1 (info):** the bible's Ch.13 blocks quote the writer's draft and the pre-repair page. Off the page, among others:
  - "I will come when I am sent for.", "How many ways out?", "Then I will see it shut.";
  - "Keep to this wall", "for a bet", "They made a mountain out of it", "Keep your silver. You'll want it for a boat.", "Was it a stone?";
  - the muleteer-and-crows line, the airport memory, "the Bay of Naples", "out of the coins from the ford", "which his sister never managed", "the tablecloth screen".

  The bible sync is handed off (the audit's W-21).
- **CH13-3 (info):** outline Ch.13's "A temple slave summons her" is, on the page, the jug boy, not said to be a slave, at Kallia's gate.
- **CH13-4 (low):** "the almonds had flowered … without my seeing it" (p12) sits against ch-09:p128, where Mara saw them come into flower a month or more before.
- **CH13-6 (info):** whether Euthydikos, the registrar at the door, is also the priest at the screen who glossed the answer. Valens describes two stations. Mara's narration ties the glossing priest to Euthydikos's wax and lamp (p149). The audit reads them as one man; not merged here.
- **CH13-7 (info):** a cave try is promised for "Tomorrow" (p172-p175). Outline Ch.14 (the same night) and Ch.15 (summer) have no slot for it.
- **CH13-8 (info):** outline wording departures, none against a NON-NEGOTIABLE:
  - the goat is drenched with a jar;
  - "prophetes" is never said;
  - the priest's Etna gloss and the non-Greek word are new;
  - the carrier's name in the god's book is Felix's;
  - the pills are offered to Valens first;
  - the summoner (see CH13-3);
  - Valens's night on Kallia's floor is set up here.
- **CH13-13 (info):** Theano explains her crows (p224; p225) against foundation §3 / her card "never explains". The audit (W-13) recommends a card amendment; the repair kept the passage.

Rechecked with a note: CH6-5, CH10-6, CH11-4, CH12-2, CH12-4, CH12-5, CH12-7 (widened in knowledge: Kallia told of "a heavy thing from my bag", Felix's "silver thing" kept from the Elateian), CH12-8 (Valens kept his name out of the god's book) and CH12-9 (NARROWED: the goat's arrival at the yard "since sundown yesterday" is now on the page). Nothing else is touched.

### The audit's suggested patches
Applied where the page supports them. Not applied:
- "the non-Greek word given twice = 'Pompeii'": the page never says so (`plot_threads.the-non-greek-word`);
- Euthydikos as the priest at the screen: not stated (CH13-6);
- Theano's cat as a character: it is recorded as a fact of `theanos-house`.

### For Ch.14 onward
- **Mara** has the god's answer word for word, the priest's Etna gloss and Theano's one word, "Pompeii.". Her reaction is not on the page. Her list of candidates skips Campania ("Or Sicily after all, or Massalia, or Spain.", p166); the audit's I-29 leaves the blind spot to Ch.14.
- **The hour** is withheld: Theano will not say whether it was never given or not hers to give.
- **The non-Greek word** is unidentified on the page.
- **Who knows what:**
  - the answer: Valens, Mara, Kallia (from the lean-to) and Felix (on the stair);
  - "Pompeii.": Mara and Theano only;
  - Praxias was refused the answer.
- **Valens** is to sleep on Kallia's floor ("There's floor," p192; his acceptance is not stated). Felix sleeps "with the string". Valens's injuries are three days old.
- **Kallia** knows the killing, the frame and the notice ("Five hundred,"). She does not know his hands or what the "heavy thing" is.
- **The Advil** is used up.
- **Valens's name** is not in the god's book; Felix's is.
- **Euthydikos** will send for Mara for the bowl after the season, and she has put it off.
- **Kallia:** "The boats go west at the new moon."

## 2026-10-20: UPDATE (re-sync of chapter 13 after polish cycle 1 and finalize FZ1-FZ3)

- **Input:** `git diff e6a8e26 HEAD -- manuscript/chapters/chapter-13.md` (commits 1db5f24 and 2e1cf91). chapter-13.md was last written 07:28:44 (md5 9c7aaccc…). It still has 245 paragraphs, with the breaks after p45, p96, p138 and p192. A paragraph diff shows nothing added, cut, split or merged, so **no ch-13:pYY is renumbered**. Text changed inside 26 paragraphs: p12, p17, p22, p24, p27, p30, p47, p78, p98, p112, p115, p119, p120, p129, p136, p143, p144, p149, p159, p170, p194, p202, p208, p210, p214 and p219.
- **Method:** a word 4-gram diff (old page against new) and a check of every quoted segment on the Ch.13-only lines found each line carrying cut wording. 48 lines were corrected and 24 added. All new quotes were machine-checked against the final page.
- **Removed as page facts** (cut from the page):
  - the cake trays' reason clause ("so that nobody should take the god's cakes…");
  - Praxias's "little—" and the stop-himself beat;
  - "at a trot" and "without stopping" (Praxias), and "at a run" (the jug boy's exit);
  - the jug boy's age and tunic ("ten or so", "too long for him");
  - Praxias seeing "the crust on it and the bruise below it" (the bruise on Valens's face stays, at p104 and p171, but where on the face is no longer stated);
  - the pills shaken out "under my himation" at Theano's;
  - the scansion tail "left to hang off the end" / "would not fit inside the line";
  - the Etna clause "a Syracusan who wanted a western sea would have to cross the whole island";
  - Valens's manner comparison "the way you'd read anything out".
- **Corrected to the page:**
  - "into his hand" and "He glanced at what the road had done to Valens" (p24);
  - "Next month. And then you pay again, Syracusan," he said, and liked the sound of that. (p27);
  - "He did not touch the two small white things in my palm." (p30; added to Valens's pills trait);
  - "in an ordinary voice" (p78);
  - "admiring the sky" (p120);
  - "with his wreath still on" (p129);
  - "Not this year. Not that he's told me." (p136);
  - "hung off the end of it like a suitcase roped onto the roof of a car that was already full" (p144);
  - "and the god, in the priest's verse, had said west." (p149);
  - "a plaster door" (p170);
  - "The front of his white tunic was dark with spilled water" (p194);
  - Valens's corner (p202);
  - "held them up to her where she sat on her husband's stone" (p219);
  - the Phocian's friend "with an arm round his neck" (p119).
- **CH13-4 (RESOLVED by the page):** p12 now reads "the almonds on the terraces were all in full flower now", and "without my seeing it" is gone. That agrees with ch-09:p128 (file l.266, "had come into flower in the last week"). The page fixes no interval between the two chapters, so nothing is recorded about how long the bloom lasts. The timeline and Delphi rows that cited CH13-4 are updated.
- **Ibuprofen:** stays `chekhov_closed`, and a `used_up` field (0 remaining) is added. `resolution.paragraph` is corrected from 223 to **222**: she swallows the pills at p222 (the eval's l.456), and p223 is "That's my own barley,". Theano's pills trait no longer says "'last' is not on the page" (stale since the repair; CH13-2 RESOLVED).
- **Added:** `cake-stall-keeper`, a minor walk-on new on the final page (p22).
- **CH13-1 (still UNRESOLVED):** a `recheck_final_page` note names the new target md5 and the polish-cycle strings the bible has not yet taken. The bible sync is running in parallel.
- **CH13-8:** item (12) records the 26 reworded paragraphs. **CH13-11:** a `final_page` field records that the walk-off still goes uphill, so its resolution stands.
- **CH13-13 left open**, as instructed (Theano's card, in the parallel bible sync).
- **Eval ENTITY patches** (evaluations/chapter-13-eval.md, final section) are both applied: ibuprofen used up, and the almonds per CH13-4. No other ENTITY patch is named.
- **Meta:** there is a Ch.13 row in `meta.revalidation_needed` (RESOLVED). `paragraph_rule`, `last_updated_by`, `mode`, `source` and the header comment are extended. `yaml.safe_load` and a strict no-duplicate-key loader both pass.
- **No new contradiction and no knowledge_gap.**

## 2026-10-20: UPDATE (chapter 14, "What Pompeii Means", final text: post-writer, dialogue-polish, hook-craft, disruptor and continuity repair C-01 + W-01..W-13)

**Trigger:** chapter loop step D.5 for chapter 14 (the orchestrator asked for the post-disruptor page; the continuity audit and repair landed mid-run, so the update is anchored to the repaired page).

**Inputs read:**
- `manuscript/chapters/chapter-14.md`, twice.
  - First in its post-disruptor state (66 paragraphs; breaks after p8, p13, p17, p21, p27, p38, p51, p58 and p62; md5 777e198…, 08:15:53; commit c2a6d8d).
  - Mid-run the continuity audit (`evaluations/continuity/chapter-14-audit.md`, commit ab8d2cf, 1 CRIT / 13 WARN) and the repair (commit d77c3b7, 08:41) landed. The update was re-anchored to the repaired page (last written 08:41:29, md5 1430f5dc9c64eb73518bab54061ec82f), which matches HEAD and had stopped changing.
  - The repaired page has **64 paragraphs**, with breaks after p8, p13, p17, p20, p25, p36, p49, p56 and p60 (ten shards):
    - old p1..p19 keep their numbers;
    - old p20 + p21 = new p20;
    - old p22..p25 = new p21..p24;
    - old p26 ("I laughed.") is cut; old p27 = new p25;
    - old p28..p66 = new p26..p64.
  - Text changed inside new p7, p8, p13, p15, p16, p18, p20, p24, p25, p26, p30, p33, p37, p45, p54, p61 and p64.
- `ENTITY_STATE.yaml` (`last_updated_chapter: 13`).
- outline.md Ch.14–15 (and the repair's patch to Ch.14 beat 1); voice-dna §0.3; character-bible.md (the Ch.14 blocks, the walk-on note, At-risk after Ch.14).
- The continuity audit, including its SUGGESTED YAML PATCHES.
- `git diff 2e1cf91..HEAD` for chapter-10.md (commit 8332ff3) and chapter-13.md (commit 7ca9352); Ch.2, 6, 7, 8 and 13 pages for Halloran, the cliff path, the household pot, the cave hand and the well.

**Meta:**
- `last_updated_chapter: 14`; `chapters_tracked: [1..14]`.
- `paragraph_rule` is extended to Ch.14, with the shard map and the repair's renumbering.
- New block `meta.ch14_requested_checks` (14 checks).
- 527 `ch-14:pYY` cites, all within p1..p64.
- Every quoted fragment on a new or changed line was machine-checked against the repaired page. A second check confirmed that each Ch.14 quote sits in a paragraph its line cites. The exceptions are deliberate: plan, bible, audit, commit-message and post-disruptor quotes, each labelled as such.
- The YAML loads under `yaml.safe_load` and under a strict loader with no duplicate keys.

### Re-checked outside Ch.14
- **Ch.10 (commit 8332ff3).** p32 now reads "I knew it the way I knew the Armada, as a date on a page with a fire in it." There are still 98 paragraphs. The two lines that quoted "the year of the Armada" (Mara's "knows history as a date" trait; the Emesa/Jerusalem knowledge row) now quote the page. A `revalidation_needed` row records the edit (RESOLVED).
- **Ch.13 (commit 7ca9352).** Only the header comment changed (the md5 is now bf846713…), so no ch-13:pYY and no quote is affected. A `revalidation_needed` row is added (RESOLVED).

### Replaced (plan → prose)
- **Timeline:** row 14. One night, the seventh into the eighth of Bysios AD 71, continuous with ch-13:p245:
  - "It was the year seventy-one … the spring was only started" and "eight years and a little over" (p19);
  - the half moon is "down by midnight" (p33; p61);
  - "the next new moon" is still to come (p54).
- **timeline_events:**
  - the planned "1988 … graduate student" row is now **April 1979**: at fourteen, with her mother (p15; p16);
  - the planned eighth-of-Bysios row is replaced by the night and by first light (the mules; "the bottom of the climb");
  - new rows: the 1850s numbering, Saint Paul's crossing (c. AD 60–61) and the letters to Tacitus (c. AD 106–107).
- **Location rows:** Mara (Theano's door → the fountain → the corner → Kallia's woodpile, storeroom, drain, gate) and Valens (the corner → across the threshold → gone for the mules).
- **Knowledge:** Mara's planned AD 79 row now cites the page. It is in scene, and neither "Pompeii" nor "Vesuvius" is in the prose. `eruption_foreknowledge` is split into the Ch.14 page row and the still-planned Ch.36 row (the 24th and the hours).
- **Waypoints:** Mara's Ch.14 row.
- **Kallia's planned trait** ("puts Valens on the floor") is confirmed on the page; her reasons are not stated.
- **`plot_threads.maras-secret`** is opened on the page (p30; p36).

### Added
- **Characters:**
  - new: `woman-with-the-jug` ("not only Syracuse"), `thessalian-father-from-larisa`, `thessalian-youngest-son` and `thessalian-sleep-talker`;
  - told only: `pliny-the-younger` (unnamed on the page), `tacitus`, `livy`, `saint-paul`, `fiorelli` (unnamed: "An Italian in the 1850s"), `fur-hat-woman-1979`, `casts-gallery-guard-1979` and `pretzel-seller-1979`.
- **Mara:**
  - the "Syracuse" alias;
  - an age note: fourteen in April 1979 with b. 1965 puts her birthday between January and April;
  - `worn/carries/marks/hunger/hair_ch14`;
  - 13 traits: the instant dawning, the overflowing jar, the bounded map knowledge, the plaster, the 1979 memory, the laugh, true-story covers, the withheld hand, the word kept, the plan, the bowl taken back, all-or-nothing about the cave, and three short lines of Greek;
  - 17 knowledge rows and `knowledge_absent_ch14`;
  - Ch.14 statuses on nine relationships, plus two new relationships;
  - the money rag.
- **Valens:**
  - `seen/marks/clothing_ch14`: the bruised left arm uppermost; his cloak; "The knife from the road";
  - 5 traits and 4 knowledge rows, including the well cover and "The moon's down by midnight,";
  - `knowledge_absent_ch14`: the word, why she laughed, 79, and the plan he is in and left out of;
  - "his blanket", two relationship statuses and a waypoint.
- **Kallia:**
  - 5 traits and `household_ch14`;
  - a location row;
  - possessions: her own blanket, the cup and salt, the gate bar, a note on the lidded pot, and a note on the lamp;
  - 4 knowledge rows: "every other piece of the day … over supper"; the stool cover; the boy's fat; the mules;
  - `knowledge_absent_ch14`, 4 relationship notes and a waypoint.
- **Theano:** a `ch14_update` on the water trait ("She had me carry her water instead."), 2 traits, a location row and `knowledge_absent_ch14`.
- **Felix:** an off-page location row and `knowledge_absent_ch14` (the plan has "no boy in it").
- **Others:** Ch.14 notes on Euthydikos (the bowl in her plan), Halloran (agrees with ch-02), Emilio ("never a spare bed"), Mara's mother (the 1979 casts), the Thessalian family (SETTLED as Kallia's lodgers; from Larisa), the gallery lodgers and the Amphissan woman (her well retold).
- **Locations:**
  - new: `larisa`, `malta`, `herculaneum` and `casts-exhibition-1979`;
  - Ch.14 facts on pompeii (the plan, the tombs, garum; never named), vesuvius, neapolis, naples, puteoli, kirrha, corinth, kallias-house (the storeroom plaster, the court, the drain, the morning), theanos-house (the jars; the lion's-head fountain), delphi, cliff-stair-above-delphi ("short turns"), nuceria-road and philadelphia.
- **Objects:**
  - new: `kallias-own-blanket` ("brown, with a burn at a corner"; "folded in four");
  - `talkers-knife` (a beat; `last_mentioned` p32);
  - `maras-money-rag` (short of a crossing; `last_mentioned` p51);
  - `goat-hair-blanket` (a note: "my blanket", not named).
- **Knowledge index:**
  - new: `maras_plan` (Mara only; NOT Valens, Felix, Kallia or Euthydikos; the bargain is planned for Ch.15);
  - Ch.14 rows on `door_location` (Valens, Kallia and the house still NOT), `door_when`, `the_year`, `eruption_foreknowledge` and `syracuse_cover`.
- **Threads:** Ch.14 notes on the-where, the-when, romance, valens-known, felix-arena, euthydikos-bowl (now passage money; forward against outline Ch.16's autumn departure), maras-living, return-to-the-cave, the-non-greek-word, maras-english-to-herself (HELD), halloran-campania, syracuse-cover, theano-phrase (not used; 1 of 3), seventh-of-bysios-phrase (2 of 3), kirrha-road-killing and maras-stated-return.
- **World rules:**
  - two OBSERVED (Ch.14) rules: a woman travels on a man's name; the grain ships come in to Puteoli with the spring;
  - `ch14_observed` added to the sea-season, eruption, Ch.7 household-pot and narrative-law rules.

### Contradictions
New and UNRESOLVED:
- **CH14-1 (info):** the bible's Ch.14 blocks (written 08:01) quote the Writer's draft. Off the page, among others:
  - "Her water carried", "He had not troubled with a permit. He had picked the year", "What did she want?";
  - the 1988 casts, "I laughed", "in its order", "at this new moon";
  - "There's no moon till the new one", "long turns", "fig leaves";
  - the change line's account of the Ch.10 edit ("year" → "date"), which is not the page.

  The bible sync is handed off.
- **CH14-4 (info):** outline Ch.14 departures, none against a NON-NEGOTIABLE:
  - Kallia's reasons for the floor are not on the page;
  - the well cover, rather than withholding only the meaning;
  - the bowl as passage money, reversing ch-13:p114;
  - AD 79's month and the course of the day in present thought (the 24th and the hours stay with Ch.36);
  - Halloran's invitation recalled and turned;
  - "Pompeii" in the title only.
- **CH14-5 (info):** Mara gives Kallia a cover ("She wanted somebody to hear about her stool,") against the mutable: false trait "will not lie to Kallia" (ch-12:p176). It is true in its letter. Left for continuity-guardian.

New and RESOLVED in the same run (the post-disruptor page, settled by the repair):
- **CH14-2 (medium here; the audit's C-01 graded it CRITICAL): the moon.**
  - The post-disruptor page had "There's no moon till the new one", an old crescent before dawn and "this new moon". That sky fits days 24–28 of a lunar month, not the seventh.
  - Now: "The moon's down by midnight," (p33); the half moon "had dropped behind the western hills" (p61); "at the next new moon" (p54).
  - **No CRITICAL stands on the final page.**
- **CH14-3 (low; audit W-02):** "He had carried it out of the temple himself" could be read as the word. Now: "He had carried the god's half of it out of the temple himself" (p30).
- **CH14-6 (low; audit W-01, not caught here):** the February 1988 casts at twenty-three are now April 1979, at fourteen, with her mother (p15; p16). The outline beat 1 and voice-dna §0.3 are patched to match.
- **CH14-7 (low; W-05):** "the latrine" is now "the pot by the water jars" (p37), which agrees with ch-07:p36.
- **CH14-8 (low; W-06):** "long turns" is now "short turns" (p64), which agrees with ch-06:p159's "short zigzags".
- **CH14-9 (low; W-03/W-04):** "from a gladiator, word for word … He had picked the year." is now "with a gladiator standing for me at the screen … He had picked the town." (p24).

Updated:
- **CH13-7 (cave "Tomorrow"):** KEPT and set for the morning of the eighth. Mara decides to see it shut; Valens has "gone down for the mules"; Kallia sends her to "the bottom of the climb" with bread (p57–p64). Severity is raised from info to low because the errand is now in motion. Forward constraint: **Ch.15 (summer, the high pasture) must account for the climb and for what the crack did**, on the page or reported, before Mara tells Valens the door home is in Pompeii.
- **CH13-8:** item (10), Valens on Kallia's floor, is carried out on the page.

Rechecked with a note and left open:
- CH2-1 ("I had said Greece, perhaps." has no "first");
- CH6-5 (the cliff path is in view);
- CH12-4 (the season "opened with the spring").

Nothing else is touched.

### The audit's suggested patches
Applied as the repaired page supports them:
- CH13-7;
- the moon, recorded after the fix only;
- the casts (April 1979, venue unnamed on the page);
- Mara's knowledge;
- the Pompeii-name knowers, as `door_location` rows plus `maras_plan`;
- euthydikos-bowl;
- the-non-greek-word kept open;
- Kallia's blanket;
- the walk-ons;
- the fountain and the jars at theanos-house.

The at-risk registry note is the bible's, so it is not applied here.

### For Ch.15 onward
- **The cave climb** of the eighth is set and not shown (CH13-7).
- **Valens** does not know the city. Outline Ch.15 gives it to him, with the truth.
- **The plan** needs a man and leaves Valens out ("He kept being in it."). The Ch.15 bargain supplies him.
- **The bowl** after the season sits against outline Ch.16's autumn departure for Corinth.
- **The moon** counts from the seventh: half on the seventh, full about the fourteenth or fifteenth, new about three weeks on.
- **Felix** is out of the plan, and his Italy question is unanswered to him.
- **AD 79** in present thought is spent for Ch.14. The 24th and the hours remain for Ch.36–37.
- **Kallia** has the whole day except Theano's word, plus the stool cover.

## 2026-10-20: UPDATE (re-sync of chapter 14 after polish cycle 1 and finalize FZ1-FZ7)

- **Input:** `git diff c09a50c HEAD -- manuscript/chapters/chapter-14.md` (commits d6b2bd9, the 23 swaps, and 6ff55fc, FZ1-FZ7). chapter-14.md was last written 09:17:55 (md5 7942cfa0…, 3,003 words by shape_check).
- **Renumbered:** the page goes from 64 paragraphs to 62.
  - Polish L1 cut old p45 ("Kallia had had every other piece of the day from me over supper.").
  - P2 merged old p57 (the pointer that quoted Ch.13's "Tomorrow") into old p58, which now opens "That left the cave."
  - Map: old p1..p44 keep their numbers; old p46..p56 = p45..p55; old p57 + p58 = p56; old p59..p64 = p57..p62.
  - The breaks now come after p8, p13, p17, p20, p25, p36, p48, p55 and p58.
  - 528 explicit ch-14:pYY were remapped, plus 77 bare refs on Ch.14-only lines. Bare refs in the earlier Ch.14 run log keep their old numbers.
- **Method:** every quoted segment on a ch-14 line, and every line of the CH14-n entries and `ch14_requested_checks`, was checked against the final page by script. What is still flagged is either another chapter's quote, a bible string, or a cut line quoted on purpose and labelled.
- **Corrected to the page:**
  - the jars: "her big jar stood empty, with a small one turned upside down on its mouth" (p3), in theanos-house, Mara's carries and the objects check. The jar Mara carries is presumably the small one (not stated);
  - "the cat opened one eye at me." (p3);
  - "closed on the name" and "Its sea to the west" (p1);
  - Fiorelli's "like sherds in a tray" (p11);
  - the plaster, "thin in places and never floated smooth" (p14);
  - "my father's bed … for the season" (p21), which agrees with Ch.2's "In Emilio's place" (ch-02:p40);
  - "He came home lean and dark" (p23);
  - "On his blanket Valens was up on one elbow." (p26);
  - "He left the knife where it was." (p29), added to Valens's trait, the talkers-knife rows and the check;
  - "He slept almost at once." (p34);
  - "I made the plan while my feet warmed." (p49), with no clock marker in the timeline;
  - "A husband or a brother; failing those, an owner." and "asleep within reach of my hand" (p51);
  - "opened again in spring", "the fare and a man", and Saint Paul's ship "went aground on Malta, and another Alexandrian that had wintered there brought him in to Puteoli" (p53), in Mara's knowledge, saint-paul, malta, puteoli, kirrha, the timeline event, the world rules and the CH12-4 recheck;
  - "bowl to door." with no "and it held" (p55);
  - "That left the cave." (p56), "with my fingers on the crack, and feel nothing come through" (p57) and "with Valens and the mules if he would come, and alone if he would rather sleep" (p58), in CH13-7, the cave thread and Mara's traits;
  - "Kallia stood at the gate, ready to lift the bar." (p60), in Kallia's trait, household and location rows.
- **Removed (cut from the page):**
  - "my wet front";
  - "Either the cave was shut, or it was open." (Mara's all-or-nothing trait is now "wants the cave proved shut by touch");
  - "find out which";
  - "see it shut with my own eyes";
  - "In the middle of the night";
  - "somebody whose name went down first".
- **Unchanged and only re-anchored:** the moon lines (p33; p53; p59), "picked the town" (p24) and "short turns" (p62). These are the eval's ENTITY note, and every item in it is applied.
- **Kallia's knowledge (the deleted "every other piece of the day" sentence):**
  - One row depended on it: "'every other piece of the day' from Mara 'over supper'". It rested only on that sentence, so it is **WITHDRAWN**. The withdrawal is noted in her `knowledge_absent_ch14` ("not on the page since polish cycle 1"), in CH14-5 and in the forward constraint.
  - Her other Ch.14 rows stand: the stool cover (p45), the ram boy (p42) and the mules (p61).
  - The Ch.14 entry's "For Ch.15 onward" line, "Kallia has the whole day except Theano's word", is superseded. She has the stool cover. Theano's summons is hers from Ch.13 (ch-13:p197).
- **CH14-1 RESOLVED:**
  - At the first check (09:19) the bible was still as written at 08:01.
  - The parallel sync then landed (commit e1a2ea6). Its seven Ch.14 blocks are tagged SYNCED, and all 214 of their quotes were checked by script. None is a Ch.14 quote that is off the page.
  - Every bible string CH14-1 listed is gone from the current blocks, and the Armada account is corrected. The `recheck_final_page` and `resolution` fields hold the trail. CH14-6's trailer is updated (the bible now says 1979 too).
- **CH14-5 (still UNRESOLVED):** the cover stands. With the supper line cut, the stool is the only account of the day Mara gives Kallia. This is still for continuity-guardian.
- **CH14-2 and CH14-4:** each gets a `final_page` note. Their resolution and departures stand.
- **CH13-7 (still UNRESOLVED, low):** re-quoted. The errand now names Valens and the mules, so Kallia's dawn line answers it.
- **Meta:**
  - a Ch.14 row in `meta.revalidation_needed` (RESOLVED);
  - a new `ch14_requested_checks` entry;
  - `paragraph_rule`, `last_updated_by`, `mode`, `source` and the header comment extended.
- **Validation:** `yaml.safe_load` and a strict no-duplicate-key loader both pass.
- **No new contradiction and no knowledge_gap.**

## 2026-10-20: UPDATE (chapter 15, "Summer Pasture", final text: post-writer, dialogue-polish, hook-craft and disruptor)

**Trigger:** chapter loop step D.5 for chapter 15 (the orchestrator asked for the post-disruptor page).

**Inputs read:**
- `manuscript/chapters/chapter-15.md`, last written 11:03:44 (md5 33239f8741caa28f43f4353c336bf59e; commit b03816a, the disruptor pass; 7,787 words by shape_check). It is unchanged against HEAD.
  - **295 paragraphs.** Breaks come after p54, p181 and p251, giving four shards: S1 p1–p54 dawn (with both backfills), S2 p55–p181 noon, S3 p182–p251 afternoon to dusk, S4 p252–p295 night.
- `ENTITY_STATE.yaml` (`last_updated_chapter: 14`).
- outline.md Ch.15–16; voice-dna.md (the one contraception thought); character-bible.md (the MNASON card and the Ch.15 notes, read only).
- Ch.3, 5, 6, 7, 11, 12, 13 and 14 pages for the crack, the Castalian spring, Philadelphia on the cliff, the singed legs, Felix's origin, the camera and the foot of the climb.

**Meta:**
- `last_updated_chapter: 15`; `chapters_tracked: [1..15]`.
- `paragraph_rule` is extended to Ch.15.
- New block `meta.ch15_requested_checks` (13 checks).
- 1,035 `ch-15:pYY` cites, all within p1..p295.
- Every new quoted segment was machine-checked against the page, including that it sits in a paragraph its line cites. The exceptions are deliberate: quotes from other chapters, the outline, foundation and the bible, each labelled.
- The YAML loads under `yaml.safe_load` and under a strict loader with no duplicate keys.
- Counts: characters 210 → 220; locations 72 → 74; objects 97 → 100; timeline_events 170 → 173; character knowledge rows 526 → 563; knowledge_index rows 283 → 308; plot threads 55 → 56; world rules 78 → 82.

### Replaced (plan → prose)
- **Timeline row 15:** one day in July AD 71 by Mara's count ("It was July now, by my own count", p8).
  - About four months since Ch.14: "since then, four months, not a word about the light" (p23).
  - The grazing began about May ("In two months I had learned", p25).
  - The two backfills sit inside the dawn shard.
- **timeline_events:** the planned "summer AD 71" row is replaced by four rows:
  - the Corinthian at the lion spouts and Kallia's boat story, in the month after the consultation;
  - the string going up, about May;
  - the July day;
  - Mara's last shave, May 1998.

  The Ch.14 eighth-of-Bysios row gets a `ch15_page`.
- **Location rows** for Mara and Valens, now `summer-pasture`, with the backfill.
- **Waypoints** for Mara.
- **Valens's teeth** ("not one was missing … like a row of new tiles", p274).
- **Valens's three planned knowledge rows** (the nineteen centuries; the cave door and Pompeii; the bargain) are replaced by fourteen page rows. The bargain is now **his** (told_by:valens / his own), not told_by:mara-reyes (CH15-8).
- **knowledge_index:**
  - `door_location` (Valens);
  - `mara_origin` (Valens);
  - `maras_plan` (superseded by the bargain).
- **Threads:** `valens-papers.opened` and `valens-belief.opened`.
- **Objects:**
  - the Pentax's Ch.15 beat;
  - `manumission-record`'s Ch.15 beat;
  - the flashlight's `last_mentioned`.
- **Locations:** the parnassus "high summer pasture" fact.
- **Organizations:** `household-of-celer`'s "still hunting Valens in summer". This is NOT on the page as Celer's men.

### Added
- **Characters:**
  - **mnason**, the herdsman, about sixty by Mara's estimate. Entry covers:
    - the goatskin cap; milking from behind; the fig-twig quarrel; the rennet; the cheese; "your man";
    - where he winters;
    - his hut, the hut he built that they use, the woodstack, his dog.
  - mention-only: `mnasons-mother`, `mnasons-brother`, `mnasons-son`, `mnasons-sons-wife` (from Amphissa);
  - **bandaged-corinthian** (`needs_review`: he could be `third-man-kirrha-road`; the page does not say so);
  - told only: `judaean-teacher`, `calendar-monk`, `alexandrian-door-builder`, `italian-market-cheese-man`.
- **Mara:**
  - `worn/carries/marks/legs/hunger/hair/height/fertility_ch15`. Height is hearsay only: "the tall foreigner" (p5);
  - 15 traits;
  - 14 knowledge rows and `knowledge_absent_ch15`;
  - Ch.15 statuses for Valens, Kallia and Felix;
  - a new relationship with Mnason.
- **Valens:**
  - `seen/marks/clothing_ch15`: the cheekbone seam; two knuckles skinned by the falling bed;
  - 11 traits, including shaving with the ditch knife, "Do they still have mules?", the bargain, "Then I'll wait outside it", and the nightly watch on the plateau;
  - the fig trait confirmed;
  - `knowledge_absent_ch15`: the fate of the town, the tomb, the WHEN, and belief;
  - a waypoint, and relationships with Mnason and Felix.
- **Kallia:** 2 traits (the public lie; the packed bag), a backfill location row, 2 knowledge rows, `knowledge_absent_ch15` and a waypoint.
- **Felix:**
  - `marks_ch15` (skinned shins; swollen lips);
  - 8 traits (the juniper fight; "Felix of Kirrha!"; "Fighters eat on their feet"; the fig);
  - 6 knowledge rows and `knowledge_absent_ch15`;
  - a location row and a relationship with Mnason.
- **Notes on others:** `lucius` (canon note), `third-man-kirrha-road`, `euthydikos`, `euthydikos-door-slave`, `plautias-brother`, `plautias-brothers-freedman`, `plautia`, `quintus-arrius-celer`, `theano`, `emilio-reyes`, `elateian-boxer`, `titus`.
- **Locations:**
  - new: **summer-pasture** (the fold, the huts, the woodstack, the seep, the junipers, the troughs, the watch point; distances) and **alexandria** (told);
  - Ch.15 facts on corycian-cave (the wall a yard past the bend), kalivia-plateau, cliff-stair-above-delphi, castalian-spring (two facts), delphi-modern, delphi, corinth, isthmia, pompeii, puteoli, neapolis, philadelphia, philadelphia-in-asia, amphissa, kirrha, capua, jerusalem and syracuse.
- **Objects:**
  - new: `mnasons-drainer` (damaged), `mnasons-hut-bed` (destroyed: the fork split), `carters-hood`;
  - updated:
    - **flashlight:** first use since Ch.5 and first seen by anyone in this world; first physical description; batteries tiring;
    - **fathers-pentax-k1000:** shown to Valens; worn to bed; no cap; the dented rim;
    - lens-cap; potted-fig-tree (moved, the first move; green figs; Felix's bite); talkers-knife (his razor); maras-money-rag; borrowed-himation ("my himation", which one not named); maras-duffel ("my bag").
- **Knowledge index:**
  - new `cave_visit_ch15`;
  - Ch.15 rows on door_location (Felix and Kallia NOT; Mnason not stated), door_when (Valens NOT), the_year, eruption_foreknowledge (held back, p138), syracuse_cover (Kallia's sailing story; the lane; Valens told "Kallia made Syracuse"), maras_camera and maras_plan.
- **Threads:**
  - new **conception-and-lucius**;
  - Ch.15 notes on the-where, the-door-and-the-choice, celer-and-the-frame, romance (HEAT 1; lovers from p284, recorded as a state), valens-known, felix-arena, maras-secret, maras-stated-return, return-to-the-cave, maras-english-to-herself (HELD), syracuse-cover, maras-living, kirrha-road-killing, theano-phrase (not used; 1 of 3) and seventh-of-bysios-phrase (0; 2 of 3);
  - **euthydikos-bowl CLOSED** (lapsed).
- **World rules:**
  - 4 OBSERVED (Ch.15) rules: man and wife at the gangway; the pasture's dairy; the Isthmus diolkos and the boys' race; the sword before a full arena;
  - `ch15_observed` on the door rule ("by the cold") and on the narrative law.
- **plan_gaps:** `ch15_update` on Mara's height (now hearsay) and on whether Felix knows her origin (still OPEN).

### Contradictions
RESOLVED in this run:
- **CH13-7 (low), resolved by the page.** The eighth-of-Bysios climb is reported in backfill: Valens below the cliffs with two mules; the plateau half under snow; the flashlight; "a face of gray stone that closed the crack from wall to wall" a yard past the bend, with the daddy longlegs; "It was shut, as I had wished it" (p10–p23). It comes before the Pompeii telling, as the forward constraint asked.
- **CH14-4 (info), resolved on the orchestrator's instruction.** The bowl plan gives way to Valens's bargain:
  - Corinth in autumn for "The book with my name in it";
  - the brother pays his witness's road, plus the ford silver and the mules;
  - a spring sailing "As man and wife";
  - Felix comes;
  - "The priest's bowl could keep its lead" (p146–p176).

  The other items are a closed record of Ch.14's departures from its outline.
- **CH12-7 (info), resolved by the page.** The camera is shown and explained to Valens: "It keeps what it shows" (p113–p125).

New and UNRESOLVED:
- **CH15-1 (low):** the Castalian spring in May 1998. Ch.5 has "a dry niche behind a wire fence" (ch-05:p21); Ch.15 has "It still runs. There is a fence round it now" (p106).
- **CH15-2 (info):** Kallia sends Mara to wait for Valens at the bottom of the climb (ch-14:p61), but Ch.15 has "Valens had been waiting below the cliffs" (p10). Compatible.
- **CH15-3 (info):** "Felix! Felix of Kirrha!" (p204) is a ring name; his origin is Side (ch-11:p220).
- **CH15-4 (info):** "In Asia." / "Further than Asia" (p79–p80) re-runs the Ch.6 exchange, where she had already said "Farther" (ch-06:p167).
- **CH15-5 (info):** "by my own count" (p8) sits beside "I had not counted a day since October" (p281). In context the second is her cycle.
- **CH15-6 (low, forward constraint):** lovers from July AD 71 with nothing against a child "but luck" (p281). Canon has Lucius conceived about autumn AD 73 (born summer 74), which leaves about 26 months with no pregnancy on the page. The voice-dna contraception thought is SPENT.
- **CH15-7 (low, forward constraint):** Delphi believes she sailed from Kirrha "at the turn of the month" (p6; p169; p171). Outline Ch.16 has her back at Kallia's house in autumn and crossing from Kirrha.
- **CH15-8 (info):** departures from the outline for Ch.15:
  - the bargain is his;
  - there are no Celer's men in the summer;
  - there is no word of madness;
  - Mnason is named;
  - the cave backfill is added;
  - the bowl is let go.

  None of these is against a NON-NEGOTIABLE.
- **CH15-9 (info):** Kallia's cover says "broke two of my jars" (p6). Only one broken jar is on any page (ch-07:p115).
- **CH15-10 (info):** "The boy says it was your father's." (p119). The telling is undated, against Felix's "To anybody" (ch-13:p123).

Rechecked with a note and left open: CH5-3 (no frame shot), CH6-5, CH12-2 ("that book in my hand"), CH12-4, CH12-5 ("Celer's chose a road for it"), CH12-8.

**No CRITICAL. No knowledge_gap.**

### Knowledge flow (the orchestrator's question)
- **Valens now knows:**
  - the count to 1998, nineteen centuries ahead;
  - the cave door;
  - Pompeii, in Campania below the wine mountain, with the door "out among the tombs, somewhere";
  - that she means to go home by it.
- **Valens does NOT know:** the town's fate (p138), the tomb, or the WHEN.
- **Belief:** he believes only the light ("I was there to see it."). "Then I'll believe it" if he sees the door open.
- **Felix** was at the troughs through the telling (p55; p185) and asleep for the belief exchange. He has Corinth, the winter, a ship and Italy, and none of "man and wife" or Pompeii.
- **Mnason** was in the hollow at noon "with his cap over his face" (p55). Whether he heard is not stated, so no knowledge row is given (the bible says he knows none of it).
- **Kallia** is in Delphi.

### For Ch.16 onward
- **Delphi believes Mara sailed** (CH15-7). Euthydikos's man is to be told "you sailed".
- **Corinth** "When the grazing's done, in the autumn … Before the rains": the brother's house (a porter, a dog, a cook), with Mara as "My wife"; the string sold down at the Isthmus; Felix with them.
- **The record** is still "the book" (CH12-2).
- **Mara's stated condition:** "I shall go home." / "Then I'll wait outside it."
- **The flashlight's batteries** are tiring, and there are none to buy.
- **The Pentax** has no cap; Valens has handled it.
- **No pregnancy** before the Ch.20 reveal (CH15-6).

### Re-anchored mid-run to the repaired page (commit dc4563d)
The continuity audit (`evaluations/continuity/chapter-15-audit.md`, commit 497e1ee, 0 CRIT / 12 WARN) and the repair (commit dc4563d, W-01..W-11 + I-04, 11:32) landed while this update was being drafted.

**The page now used:** chapter-15.md as last written 11:31:45 (md5 5ea1f666105ad27ff7370150bf7b6c30; 7,719 words by shape_check).
- Still 295 paragraphs with the same three breaks, so no ch-15:pYY moves.
- Text changed inside p7, p10, p56, p98, p107, p110, p114, p123, p138, p204, p251, p266, p274, p275, p276 and p281.
- Every Ch.15 quote was re-checked by script against this page. What remains off the page is labelled as post-disruptor, outline or other-chapter text.
- A `meta.revalidation_needed` row for Ch.15 is added (RESOLVED).

**Corrected to the page:**
- **Who waited:** "Valens came up below the cliffs" (p10). This replaces "had been waiting" in CH13-7, the timeline event, Valens's location row and the checks.
- **Valens's razor:** "his knife" (p56). objects.talkers-knife therefore gets **no** Ch.15 beat (`note_ch15` only; `last_mentioned` back to ch-14:p32), and the kirrha-road-killing note is fixed.
- **The emperor:** "Nobody, on my side of the world." (p98).
- **The graze:** "a graze had healed" (p107); "from the road" is cut.
- **Home:** "My landlord, by now. And somebody at my work will have rung my telephone, and got my own voice on a tape" (p110). This is fixed in Valens's knowledge, philadelphia and maras-stated-return.
- **The camera:** "as I had in Kallia's crowded house" is cut (p114), and "the dent in the rim," no longer has "where the man's head had been" (p123).
- **The name:** "The rest of what I knew stood behind the name:" (p138).
- **The Elateian:** the stance is cut from the juniper fight (p204). The Felix trait and the felix-arena seed are fixed, and the elateian-boxer note now records the cut.
- **The belief exchange:** "'Then I'll believe it,' he said." (p251).
- **The belt:** "laid it away in the corner" (p266).
- **The teeth:** "square and even" and "I had flossed every night of my adult life and still paid a man in a white coat to scold me twice a year … and held them against him." (p274). This is fixed in Valens's teeth and Mara's trait, and adds Mara's `teeth_ch15`.
- **The stillness:** "he had gone quite still." (p276).
- **The contraception line:** "I had lost count of my month somewhere around October" (p281). This is fixed in Mara's `fertility_ch15`, CH15-6 and conception-and-lucius.
- **New on the page:** "Before light I was at Valens's yard, and I kept to his loft for some weeks" (p7). It is added to the timeline note and event, Mara's location row and relationships, a valens-yard note, and the CH15-7 trail.

**Outline Ch.16 patched (W-12):**
- The Delphi farewell is "kept quiet": "Delphi has believed since spring that Mara sailed (Ch.15)". Mara goes to Kallia's door after dark and is gone at first light.
- The himation is given "outright (Mara has worn it all summer and folds it to hand back; Kallia makes it hers)".
- The lamp frame is "in the first morning light, before she goes".

This is recorded on CH15-7 and on the borrowed-himation note.

**Flags after the re-anchor:**
- **RESOLVED by the repair:** CH15-2 ("came up") and CH15-5 ("lost count of my month").
- **RESOLVED by the outline patch:** CH15-7. Forward: the Ch.16 page must keep the farewell covert.
- **Still UNRESOLVED:** CH15-1 (low; the spring "still runs", p106 unchanged), CH15-3 (info), CH15-4 (info), CH15-6 (low, forward constraint), CH15-8 (info), CH15-9 (info) and CH15-10 (info).
- **Resolved this run in all:** CH12-7, CH13-7, CH14-4, CH15-2, CH15-5 and CH15-7.
- Open contradictions now total 34 (30 before this run, +7 net).
- **No CRITICAL. No knowledge_gap.**

**The audit's other items:**
- I-03: the back wall is recorded on corycian-cave.
- I-15: CH15-6.
- I-16/I-17: Mnason's position. No knowledge row is given, so he is not stated to have heard.
- I-20: Valens expects the suit heard at Corinth, while canon hears it in Rome in spring 74. This is noted here for Ch.16/21 and not flagged, because it is his expectation.
- I-21: they live as man and wife all winter, before the Ch.18 quay wedding.
- I-22: CH12-2.

Polish items I-06..I-11 are not tracked facts.

## 2026-10-20: UPDATE (re-sync of chapter 15 to the FINAL page after polish cycle 1, the CH15-1 spring line and finalize Z1-Z6)

- **Input:** `git diff dc4563d HEAD -- manuscript/chapters/chapter-15.md`. dc4563d is the page the Ch.15 UPDATE (5d6d8c7) was anchored to. The diff covers commit b917d7a (polish cycle 1: 45 tested eval swaps, plus the CH15-1 spring line) and commit e358758 (finalize Z1-Z6). chapter-15.md was last written 12:09:00 (md5 66916b39…, 7,479 words by shape_check). No other chapter changed after 5d6d8c7, so the cross-chapter cites hold.
- **Renumbered:** the page goes from 295 paragraphs to 294.
  - Finalize C7 cut old p260 ("Mnason built it to fit Mnason," he said.).
  - Map: old p1..p259 keep their numbers; old p261..p295 = p260..p294.
  - The breaks are still after p54, p181 and p251. S4 is now p252-p294.
  - 88 explicit ch-15:pYY and 19 bare refs on Ch.15 lines were remapped (including `objects.mnasons-hut-bed.resolution.paragraph` 268 → 267).
  - The Ch.15 run log, and the fields labelled as an earlier page (CH15-5's post-disruptor and repaired-page quotes, the CH15-1 dc4563d quote), keep their earlier numbers.
- **Method:**
  - Every quoted segment on a Ch.15 line was checked against the final page by script, using 4-gram runs that exist on the old page and not the new one.
  - The first pass had a tokenizer bug that hid changes at the edges of quotes. After the fix it found two more stale quotes (Valens's papers row and the ford-silver note, both "Celer's chose"), and both are corrected.
  - Every on-page quote was also checked against the paragraph its line cites: 0 new mismatches. The 4 pre-existing short-word coincidences are unchanged.
- **The eval's three ENTITY items (chapter-15-eval.md, cycle 1, §I), all applied:**
  1. **CH15-1 RESOLVED.** The page now says "It is dry. There is a fence round it now." (p106), which agrees with ch-05:p21 ("a dry niche behind a wire fence"; chapter-5.md l.43). Only one value is left in the text, so Ch.5's value stands. The CH15-1 entry gets `final_page`, `resolution`, `resolved_from_conflict` and `resolved_date`. The spring rows on castalian-spring, delphi-modern, Valens's knowledge and the knowledge_index say "dry and fenced".
  2. **teeth:** `mara-reyes.physical.teeth_ch15` and the teeth trait now quote "still paid to be scolded twice a year" (p273). The white coat is gone.
  3. **film:** the camera recheck now quotes "a strip as long as you are tall" (p118), and so do Valens's knowledge row and the pentax beat.
- **The fact slips fixed on the page, now carried here:**
  - **ricotta:** the Italian Market memory is "a knot of mozzarella" (p222), in Mara's trait and her 1998 knowledge.
  - **"Further up":** the dust map now has Valens draw the coast from the heel of Italy round to Puteoli, and Mara says "Short of that. There." (p134; p135). This is recorded on pompeii, Valens's knowledge and the Neapolis/Puteoli rows. "Neapolis I know of." is now "I've heard of Neapolis." The YAML never held the old "Further up", so nothing contradicts.
  - **Pompeii's magistrates:** "They elect their magistrates every year" (p137). "two magistrates a year" is gone.
  - **the film strip length:** as item 3.
  - **the hut and bed are Mnason's:** p253 now reads "Mnason's rush baskets hung in a row from pegs … At the back he had made a bed". On the earlier page "His" and "he" could be read as Valens, and finalize then cut "Mnason built it to fit Mnason". This is recorded on mnason.possessions, summer-pasture, objects.mnasons-hut-bed (note and description) and the Ch.15 check. The hut is still distinct from Mnason's "own hut" (p30; p40).
- **Other quotes corrected to the page:**
  - "Delphi thinks you're on a boat. Let it." (p169), in 9 rows;
  - "I'll wait outside it," (p180), in 8 rows;
  - "Celer's men chose a road for it." (p160), in 6 rows. Valens now names Celer's men for the Ch.12 road. CH12-5 is unchanged, because the attribution is still his own reading;
  - "in the autumn, with snow on the way" (p90). Valens is no longer told "October";
  - "and he left the light to me" (p20) and "and I waited." (p21);
  - "on top of everything in my bag in the hut, where it had ridden since spring" and "as much as a hen's egg" (p61);
  - "the box you look through" (p141);
  - "My hiccups were gone." (p181); the hiccup now takes her "exactly on the last word of it";
  - "His jaw had roughened again since noon" (p279);
  - "he was quite still" (p275);
  - "His tunic came off," (p265);
  - "his cheek on my shoulder" (p284), so Mara's hair rows now cite "on my back and in my hair" (p278);
  - "the bitter greens … which I had come round to" and the wine "which I had not" (p234);
  - "The snow at the mouth threw the daylight in behind us" and "farther in, the dim gave out" (p14).
- **Removed (cut from the page):**
  - "and you may not drink";
  - "though up here nobody would take it";
  - "a monk's mistake" and "and that was worse still" (the trait now quotes p83's monk and "I did the sum aloud.");
  - "to have it out before he could stop me";
  - "which had borne me since we came up";
  - "as he had done every few days since our first week" (how often Mnason brings the cheese is no longer stated);
  - "which was the way up to us for anybody coming". Valens's dusk walk is now only "his face to the dark of the plateau", and the trait, the summer-pasture and kalivia-plateau rows and household-of-celer no longer call it a watch point;
  - Valens paring the black's hoof at evening. His Ch.15 location row now has him "splitting pine round the side of the hut" (p216);
  - his face and mouth "in my hair" (old p285; p290).
- **Rechecked against the final page (all still UNRESOLVED, info):**
  - CH15-3: p204 is unchanged ("Felix! Felix of Kirrha!").
  - CH15-4: p77-p79 are unchanged. p80 changed only "The flashlight lay in my lap." → "I had the flashlight in my lap.", and "Further than Asia" stands.
  - CH15-9: p6 is unchanged ("two of my jars").
  - CH15-10: p119 is unchanged, and the telling is still undated.
  - Each gets a `recheck_final_page` field.
- **Also rechecked:**
  - CH15-5 stays RESOLVED (the sentence is unchanged, now p280).
  - CH15-6 stays open (low, forward; the thought is p280, the union p281-p283).
  - CH15-8 gets a final-page note: "Celer's men"; the cut dusk gloss; the p145 cuts; the hut and bed now plainly Mnason's; the teeth at p273.
- **Contradictions:** none was overwritten. Open contradictions go from 34 to 33 (CH15-1 closed). No new contradiction. No knowledge_gap.
- **Not done here (outside this tracker's file, per instruction):** the eval's bible syncs A-H and the voice-dna §5 cell ("olive-wood rope bed" → the forked-stake bed). character-bible.md and STATE.yaml were not touched.
- **Meta:**
  - a second Ch.15 row in `meta.revalidation_needed` (RESOLVED);
  - a new `ch15_requested_checks` entry;
  - `paragraph_rule`, `last_updated_by`, `mode`, `source` and the header comment extended.
- **Validation:** `yaml.safe_load` and a strict no-duplicate-key loader both pass.

## 2026-10-20: UPDATE (chapter 16, "Plautia": drafted on the post-disruptor page, anchored to the REPAIRED page)

**Trigger:** chapter loop step D.5 for chapter 16. The run was drafted against the post-disruptor page (commit 78422e7, md5 839827b3…). The continuity audit (commit e634300; 3 CRIT / 14 WARN) and its repair (commit cf65bc0) landed while the run was in progress, so on the coordinator's instruction the update is anchored to the repaired page.

**Inputs read:**
- `manuscript/chapters/chapter-16.md`, as committed in cf65bc0 (md5 f82f457f9acaa97896e762783fec438e).
  - 283 paragraphs, with breaks after p46, p70, p120, p131, p184 and p227: C1 p1–p46, D1 p47–p70, C2 p71–p120, D2 p121–p131, C3 p132–p184, D3 p185–p227, C4 p228–p283.
  - The repair changed text inside 30 paragraphs and did not renumber any.
- `ENTITY_STATE.yaml` (`last_updated_chapter: 15`); outline.md Ch.16–17 (beat 1 of Ch.17 is now patched); foundation.md §3, §9, §10.
- character-bible.md Ch.16 blocks (read only); `evaluations/continuity/chapter-16-audit.md`, including its SUGGESTED YAML PATCHES.
- Ch.5, 7, 10, 12 and 15 pages, for the name, the Ariston letter, the sword and the bargain.
- Nothing else changed after the Ch.15 re-sync (git diff c6da60b..HEAD), so every earlier cite holds.

**Meta:**
- `last_updated_chapter: 16`; `chapters_tracked: [1..16]`.
- `paragraph_rule` now covers Ch.16.
- A Ch.16 row is added to `meta.revalidation_needed` (the mid-run repair; RESOLVED).
- New block `meta.ch16_requested_checks`: 17 checks, including the re-anchor.
- 451 `ch-16:pYY` cites. Every quoted Ch.16 fragment was checked by script against the repaired page. Quotes from the plan, the bible and earlier pages are labelled as such.
- Counts:
  - characters 220 → 242
  - locations 74 → 78
  - objects 100 → 106
  - organizations 17 → 18
  - timeline_events 173 → 187
  - plot threads 56 → 57
  - world rules 82 → 89
  - knowledge_index keys 35 → 38

### Replaced (plan → prose)
- **Timeline row 16:**
  - Delphi strand, autumn AD 71: the last fair day of the grazing; first light the next morning; the crossing "a day after Kallia's lamp".
  - Corinth strand, winter AD 71–72: after the Saturnalia; "the winter is half gone"; C4 about three months after the arrival.
- **timeline_events:** the planned "autumn AD 71: farewell to Kallia" row is replaced by 15 page rows. These include Marcus's teeth (AD 65), the manumission at the emperor's games, and the suit "two years from this spring".
- **Location rows** for Mara and Valens; new rows for Kallia, Felix, Plautia, Marcus and Myrrhine.
- **Waypoints:** Plautia's and Kallia's waypoints are replaced; Mara and Valens get new ones.
- **Mara's two planned knowledge rows** (never lovers "from watching"; Celer kept Marcus, the record office) are replaced by 16 page rows.
- **Kallia:** `last_appearance` now cites the page (p67; p131).
- **Plautia:** `first_appearance` is p1.
- **Plautia's brother:** `first_appearance` is set to null. He is not on stage in Ch.16.
- **Objects:**
  - **plautias-bracelet:** the planned stub is rewritten from the page.
  - **borrowed-himation** and **kallias-broom:** both now `chekhov_closed` (see Objects below).
  - **fathers-pentax-k1000:** the named-frame beat.
  - **manumission-record:** the Ch.16 beat, and a description in the page's form. The old description is kept as `description_was`.

### Added
- **Characters:**
  - new: **myrrhine** (full entry);
  - the brother's household: `plautias-brothers-cook`, `-porter`, `-advocate`;
  - officials: `proconsul-of-achaea`, `proconsuls-wife`;
  - record office: `record-office-clerk-young` and `record-office-clerk-gray` (both `needs_review`: either may be `archive-clerk-corinth`), `record-office-porter`, `record-office-baker`;
  - Celer's side: `celers-father` (consul "two months in a bad year"), `celers-mother`, `celers-porter`;
  - mention-only and walk-ons: `sicyon-suitor`, `dining-room-floor-layer`, `lechaion-road-papyrus-seller`, `gulf-coaster-master`, `coaster-steering-boy`, `corinth-stable-man`, `patrae-lanista`, `gaul-who-has-killed-four`, `kallias-old-lodger-ch16`.
- **Characters updated:**
  - **plautia:** about thirty; the left earlobe; her hair and skin; 11 traits; 12 knowledge rows; relationships.
  - **marcus:** named on the page; "seven at the vintage" CONFIRMS foundation (born autumn AD 64); ears, temper, the Muses; teeth.
  - **valens:** the alias "Gaius Iulius Valens"; 10 traits; 10 knowledge rows; `knowledge_absent_ch16`.
  - **mara-reyes:** 9 traits; a legal-status row ("My wife" in Corinth).
  - **felix:** 8 traits; 5 knowledge rows.
  - **kallia:** 5 traits; 4 knowledge rows; `household_ch16`.
  - Notes on the brother, the freedman, Plautia's mother and father, Celer, the steward, the lanista, the games magistrate, the Gaul, Nero, Vespasian, Ariston, Mnason and his son's wife, Nikaso and Ray.
- **Locations:**
  - new: `plautias-brothers-house`, `gulf-of-corinth`, `sicyon`, `nemea`;
  - Ch.16 facts on corinth (the forum, the colonnade, the amphitheater, the citadel), lechaion, kirrha, isthmia, kenchreai ("the other harbor"), celers-house, patrae, rome, syracuse, syria, delphi, kallias-house, valens-yard, summer-pasture and philadelphia.
- **Objects:**
  - new:
    - `kallias-lamp` (closed: the named frame);
    - `plautias-mothers-silver` (the purse);
    - `plautias-dowry-instrument`;
    - `plautias-writing-case`;
    - `marcus-saturnalia-ball`;
    - `kallias-letter-to-ariston` (written, not sent).
  - updated:
    - **plautias-bracelet:** Mara's, worn on her left wrist; "Someone had cut his teeth on it." Status `background` → `chekhov_open`.
    - **borrowed-himation:** CLOSED. Mara's outright, mended overnight: the pin hole is worked into an eye and the hem is bound.
    - **kallias-broom:** CLOSED. Hung on its nail.
    - **film-roll:** `frames_shot_ch16: 1`. Running count: plan 10 shot / 26 left; page at least 9 shot / at most 27 left. No frame on any page Ch.6–15.
    - **fathers-pentax-k1000:** the lamp frame.
    - **flashlight:** nearly dead ("Not much. Some."); Felix sees it for the first time.
    - **reply-obol:** still unspent. Which coin bought the sheet is not stated.
    - **potted-fig-tree:** on the boat.
- **Organizations:**
  - new: `household-of-plautias-brother`;
  - updated: **corinth-record-office** (the proconsul's office; two doors; "out with a copyist"; the book; one clerk on the door at the festival) and **household-of-celer**.
- **knowledge_index:**
  - new: **valens_and_plautia**, **isthmia_plan**, **valens_name**;
  - Ch.16 rows on dowry_suit_witness, maras_camera, syracuse_cover and maras_name.
- **Threads:**
  - new: **plautias-question** (the closing question, unanswered by design);
  - **kallias-son:** the coda is PAID;
  - **ariston-reply:** written, not sent;
  - **plautias-son:** opened on the page;
  - notes on valens-papers, romance, valens-known, celer-and-the-frame, felix-arena, mending-the-seam and conception-and-lucius.
- **World rules:** 7 OBSERVED (Ch.16) rules:
  - custody after divorce;
  - the colony's books in the proconsul's office;
  - the book of boards and its sealed cord;
  - freedman naming;
  - the dowry instrument;
  - the suit before a judge in Rome;
  - mules cannot vomit, and the gulf wind drops at sunset.

### Contradictions
The IDs follow the audit's suggested CH16-1..CH16-4.

RESOLVED in this run:
- **CH12-2, by the page.** The magistrate's year is a book of boards, bound by a cord through holes at the back edge, knotted, and sealed by him and his colleague. Valens's leaf is two boards "near the front" that "go into a writing case like any other pair" (p259–p267).
- **CH12-8, by the page.** "Gaius Iulius Valens, freedman of Gaius"; the nomen is "The lanista's … I had it with the sword."; "Lupus" is the benches' name (p252; p267–p272).
- **CH16-2 (low), by the repair.** "a whole winter without my name" against Ch.7. The page now reads "She had me most of an autumn before she wanted my name." (p91).
- **CH16-3 (info), by the repair.** The boat day count. The page now reads "a day after Kallia's lamp" (p185).
- **CH16-4 (low), by the repair.** Felix and the sword, previously a knowledge_gap. The stable man's "and that you got your sword there" (p151) gives the path. The knowledge_gap is withdrawn and replaced by a knowledge row, `told_by:corinth-stable-man`.
- **CH16-6 (medium), by the outline patch.** The "bronze-and-wax diptych" of outline Ch.17 now reads "The two-board leaf, cut from the magistrate's cord-bound book".

New and UNRESOLVED:
- **CH16-1 (CRITICAL), pending the author's decision.** The Isthmia are set in spring AD 72 by foundation §9–§10, outline Ch.17 and the page ("At the Isthmia," p228). The audit's C-01 says AD 72 is not an Isthmian year: the games fell in spring AD 71 and AD 73. The repair held this for the author, and it is not resolved here.
- **CH16-5 (info):** the bible's Ch.16 blocks quote the writer's draft. The bible sync is handed off.
- **CH16-7 (info):** "He serves in Syria." (p81) against Ariston's discharge (ch-10:p28).
- **CH16-8 (info, forward):** the Corinth household takes Mara as Valens's wife ("My wife," p226; "three months", p268) before the Lechaion wedding of spring 72.
- **CH16-9 (info):** the fig has now moved twice on the page; Pompeii would be a third move, against foundation's "moves it twice".
- **CH16-10 (info):** the outline's Ch.16 beats against the page. None goes against a NON-NEGOTIABLE. Outline Ch.17's fig-eating clerk must be one of the two candidates the page names, or a third.

Rechecked with a note and left open: CH5-3 (the frame count), CH12-5 (no sender named), CH15-3, CH15-6 (no pregnancy). CH15-7, already resolved, gets a `ch16_page`: the farewell is covert on the page.

Open contradictions: 33 → 37.
- Opened: 10 (CH16-1..CH16-10).
- Resolved: 6 (CH12-2, CH12-8, CH16-2, CH16-3, CH16-4, CH16-6).

**One CRITICAL is open: CH16-1, the Isthmia year.** No knowledge_gap remains.

### Knowledge flow: Valens and Plautia
- Recorded in `knowledge_index.valens_and_plautia`.
- **Valens and Plautia:** know (prior knowledge).
- **Mara:**
  - Valens told her in Ch.12. She doubted it all autumn (p6).
  - Ch.16 answers it by watching, not asking. At the porch Plautia waits until Valens has looked the street over and moved, passes him on his left, and turns at the corner "to find him"; then he looks at Mara's face (p136–p138).
  - Plautia also says: "I walked in front of him for two years and never heard it." (p179).
- Nobody says "never lovers" in words.
- **Celer** framed it. **The brother** holds the charge a lie.
- **Felix, Kallia, Myrrhine and the household:** nothing on the page.

### Not done here (per instruction)
- The bible sync for CH16-5.
- The author's decision on CH16-1.
- The manuscript, character-bible.md and STATE.yaml were not touched.

**Validation:** `yaml.safe_load` and a strict no-duplicate-key loader both pass.

## 2026-10-21: UPDATE (re-sync of chapter 16 to the FINAL page after the CH16-7 line, AUTHOR-CP3-5, polish cycle 1 and finalize F1-F8)

- **Input:** `git diff 53b1092 HEAD -- manuscript/chapters/chapter-16.md`. 53b1092 is the Ch.16 UPDATE, which was anchored to the cf65bc0 page. Four commits come after it:
  - 6c5a31f: the CH16-7 line, "He lives in Syria now.";
  - f53fc80: AUTHOR-CP3-5, "At the games for Titus's triumph,". The same commit already marked CH16-1 RESOLVED in this file;
  - 7d0cdb8: polish cycle 1, 51 tested eval swaps;
  - 8f4d343: finalize F1-F8.
  - The final page has md5 ed7509889b1c617596f2f0413112058e. No other chapter changed.
- **Renumbered:** the page goes from 283 paragraphs to 281.
  - Old p38 and old p39 are merged into new p38 ("…when at last he chose anything. Everybody who climbs that stair…").
  - Old p126 is cut ("On the gallery the old man coughed and shifted under his blanket.").
  - Map: old p1..p37 keep their numbers; old p40..p125 = new p39..p124; old p127..p283 = new p125..p281.
  - Breaks are now after p45, p69, p119, p129, p182 and p225, so the sections are C1 p1-p45, D1 p46-p69, C2 p70-p119, D2 p120-p129, C3 p130-p182, D3 p183-p225 and C4 p226-p281.
  - About 1,037 explicit ch-16:pYY refs and about 275 bare refs on Ch.16 lines were remapped. That includes the Ch.16 contradiction fields, `knowledge_absent_ch16` and the `ch16_requested_checks` rows.
  - The three refs to old p126 were removed with the fact they carried.
  - These keep cf65bc0 numbers: the header comments, the `revalidation_needed` history, the cf65bc0 re-anchor row, and the fields labelled as the cf65bc0 page (CH16-1's pre-CP3-5 `prose` and `repair_note`, the CH16-7 old quote, and the proconsul's wife's "old p75").
- **Method:**
  - Every quoted segment in the file was checked by script for text that is on the cf65bc0 page but not on the final page. 85 lines were flagged. After false hits from other chapters were set aside (Ch.10's "For the sheet", Ch.13's "She does that.", Ch.14's "his blanket"), every Ch.16 hit was corrected or labelled as cut.
  - Every on-page quote was then checked against the paragraph its line cites: 0 new mismatches. The 8 pre-existing hits are unchanged (Ch.15 run-log lines, and quotes whose second cite holds the text).
- **CH16-7 RESOLVED by the page.**
  - "A woman in Delphi, to her son. He lives in Syria now." (p80) agrees with the discharge and the land below Emesa (ch-10:p28; ch-10:p35; ch-10:p46). The entry gets `resolution`, `resolved_from_conflict` and `resolved_date`.
  - Polish cycle 1 also changed "in more than two years" to "in more than three years" (p86). Counted with Kallia's "Two and a half" (ch-10:p34, read to late winter AD 71), the silence is about three and a quarter years by winter 71-72, so the new figure also agrees. This is recorded in the note, not ruled on.
  - Updated: ariston.ch16_note, the Syria row, and the kallias-son coda.
- **CH16-1 confirmed RESOLVED (AUTHOR-CP3-5).**
  - p226 reads "At the games for Titus's triumph,". Neither "Isthmia" nor "Isthmian" occurs in chapter-16.md. A `recheck_final_page` and a `resolved_date` were added.
  - Every row that called the AD 72 festival "the Isthmia" now names it as the games for Titus's triumph. That covers Plautia, Celer, Marcus, the proconsul, Mara's waypoint and relationship, Felix's and Mara's knowledge_absent, Myrrhine's knowledge, the purse, the writing case, the manumission record, corinth-record-office, plot_threads, timeline_events, Mara's Ch.17 location row and CH16-8's foundation §10 quote.
  - `knowledge_index.isthmia_plan` is renamed `triumph_games_plan`, and the three rows that pointed to it are updated.
  - `locations.isthmia` gets a new canonical_name and aliases (the regular Isthmia of 71 and 73; the one-off games of 72). Its AD 72 fact now follows foundation §10 and outline Ch.17 as patched. The slug is kept so that existing references still resolve.
  - Timeline row 17 follows the patched outline dateline.
  - "Isthmia" survives only in these places: the regular games of AD 71 (Ch.15's boys' race "last time", as AUTHOR-CP3-5 rules), CH16-1's own pre-decision record, and the header and run-log history.
- **New contradiction, CH16-11 (low, UNRESOLVED).** foundation §9 (l.358) still reads "the **Isthmian Games** fell in spring 72." CH16-1's resolution says "foundation §9/§10 patched", but f53fc80 touched only §10 and the set-piece list at l.50. Logged, not overwritten; foundation.md was not touched.
- **The eval's ENTITY items (chapter-16-eval.md, cascade list and bookkeeping):**
  - **The flashlight:** Felix has now seen it (`seen_by_ch16`, his knowledge row). Its batteries are near the end. `batteries_ch16` and Valens's knowledge now quote "How much is left in it?" / "Not much." / "Don't spend it on mules." (p208-p210). "Some." is cut. F1 cut Felix's "What's that?" and "What is it?", so his questions open on "Where's the flame?".
  - **The suit:** "two years from this spring" (p274), unchanged and confirmed.
  - **Valens's post at the games** (the baker's oven, the back door or the horse fair) is still unsettled (p247-p255). Ch.17 decides it.
  - **Forward:** `plautias-bracelet.ch18_forward` records audit I-29: the Seiko and the bracelet will both be on the left wrist when the watch comes back in Ch.18.
- **Quotes corrected to the page:**
  - "slow, with the verb held back for the end"; "Mine came out stiff.";
  - "A sound broke from Plautia";
  - "with her hands folded, and her face was wet";
  - "a rope-maker's wife" (was fuller's), in 5 rows;
  - "or the gray-haired one, and that both of them are fond of money";
  - "go into my writing case among my letters", in 5 rows;
  - "half of it shot under the chest";
  - "She's done it before.", in 3 rows;
  - "Shut your eyes,";
  - "Can you feel it there when you lift your arm?";
  - "He laughed then." (F6 cut "He could not stop");
  - "an unlit coast", in 4 rows;
  - "the line of Lechaion's moles" and the citadel "with a wall running along its crest" (F7; "the first sun on its top" is cut);
  - "Two strokes more along the sill." and "She hung the broom back on its nail beside the fire, and went to the jar for water." (F2);
  - "The sheet was to come from Euthydikos's people";
  - "a hole, with a fringe of broken threads";
  - the finder's "a square of dark, its shutter ajar";
  - "The court grew light";
  - "had burned yellow." (the evening cold is cut);
  - the escape is now "when he rides in from the Isthmus after the boys' race" (p246). "On the day after the boys' race" is gone. This fits outline Ch.17's run for Lechaion, so it is not a contradiction.
- **Cut from the page, so marked rather than deleted (merge rule 4):**
  - **characters.proconsuls-wife:** her only line ("has coughed since the Kalends …") is cut. She gets `page_status` and `last_confirmed: ch-16 (cf65bc0 page, old p75)`. Mara's knowledge row is kept with `page_status`, and the Corinth people fact and the timeline's "Kalends" note drop it.
  - **record-office-clerk-gray:** "who does not" (drink) is cut, so his drinking is no longer stated.
  - **kallias-old-lodger-ch16:** his dawn cough on the gallery is cut, leaving him "Overhead" (p52). The lodger's cloak on the rail and the ridge-tile dawn sequence are cut from kallias-house.
  - **Valens:** "with his back to the wall by the jamb" is cut. He stands "just inside the door" (p228).
  - **Myrrhine:** "She had followed that much." is cut. So is the p6 sighting of her holding a cloak over Plautia; the arrival's maid (p225) is not named.
  - **Kallia:** "and did not go near the stair" is cut.
  - **The porch:** the porter's stool and the fuller's boy's steaming vat are cut.
  - **Plautia:** the narrator's "never the same thing twice" and "She gave his name its weight …" are cut, and both traits are reworded to what the page still shows.
- **Contradictions:** none was overwritten.
  - Open contradictions: 37 at 53b1092 → 36. CH16-1 was closed by f53fc80, CH16-7 is closed here, and CH16-11 is opened here.
  - No knowledge_gap.
- **Not done here (per instruction):** the manuscript, character-bible.md, STATE.yaml and foundation.md were not touched. The eval's bible syncs (items 1-39) and the CH16-5 bible sync stay with the orchestrator.
- **Meta:**
  - a second Ch.16 row in `meta.revalidation_needed` (RESOLVED);
  - a new `ch16_requested_checks` row for this re-sync;
  - Ch.16 part of `paragraph_rule` rewritten;
  - `last_updated` (2026-10-21), `last_updated_by`, `mode`, `source` and the header comment extended.
- **Validation:** `yaml.safe_load` and a strict no-duplicate-key loader both pass.

## 2026-10-21: UPDATE (chapter 17, "Games on the Isthmus", post-disruptor page)

- **Input:** `manuscript/chapters/chapter-17.md` at d6b3291 (writer 92b2ddf, dialogue-polish 9182746, disruptor d6b3291), md5 361981512561c0ee0e573eb9a50ed6e1. No earlier chapter, outline or foundation changed since the Ch.16 re-sync (8f4d343 / c7fd776).
- **Numbering:** p1..p274. Breaks come after p91, p145 and p203: S1 p1-p91 (the record office), S2 p92-p145 (the lane and the oven), S3 p146-p203 (the colonnade), S4 p204-p274 (the forum, the Lechaion road, the run). The four HTML comment lines are not counted. The italic tag line (p41) counts. `paragraph_rule` is extended.
- **Quotes:** every page quote written in this run was checked against chapter-17.md by script (0 misses), then against the paragraphs it cites (0 real misses). One timeline source list was widened to add p127, p191 and p198.
- **Auto-resolution check:** none of the 35 open contradictions has a cited file that changed. Ch.17 itself settles two of them:
  - **CH16-10 RESOLVED.** The fig-eating clerk is the gray-haired one ("The gray one, then. We had wanted the other.", p4), and Celer names him Onesimus (p159). New canonical entry: `characters.onesimus`. `archive-clerk-corinth` and `record-office-clerk-gray` are kept with `merged_into: onesimus` and needs_review false. `record-office-clerk-young` is not on the page, and its note now says he is not the fig clerk.
  - **CH12-5 RESOLVED.** The third man from the Kirrha road is Celer's man on the page: the seam above his left ear (p152), "Celer's seamed man" (p194), "Celer's man, the one with the ear" (p231), and "My man tells me…" (p172). Still not stated: that Celer sent the three men to kill.
  - Rechecks added to the still-open CH16-8 (Myrrhine is expected on the quay, p222) and CH16-9 (the fig goes down to Lechaion, p137).
- **New contradictions (none CRITICAL):**
  - **CH17-1 (medium).** Timeline row 18 and outline Ch.18's example opener ("awake since the second watch") no longer fit. The ship sails on the afternoon breeze (p141), and they reach the harbor a little after noon (p262-p274), so Ch.18 is the same afternoon. "Wet quay" is not on the Ch.17 page either. This is a forward constraint for the Ch.18 prompt.
  - **CH17-2 (medium).** Plautia's age. She married in autumn AD 63 ("A year before the fire", p21; p47) and says "since I was sixteen" (p209), which makes her about 24-25 in spring 72. Ch.16 has "thirty, or a little under" (ch-16:p5). The two fit if sixteen is the age of a betrothal.
  - **CH17-3 (low).** Celer says the notices went up "last year" (p177). The Corinth notice went up in Dadaphorios AD 70 (ch-09:p169).
  - **CH17-4 (info).** The leaf is boards 5-6 of about twelve (p35; p39), against "near the front" (ch-16:p265).
  - **CH17-5 (low, knowledge_gap).** Celer knows the Syracuse cover ("So I hear…", p172) and no path is shown. Logged as `quintus-arrius-celer.knowledge_gap`.
  - **CH17-6 (info).** The bible's Ch.17 blocks quote the writer's draft (about 20 strings not on the page). The bible sync goes to the orchestrator.
  - **CH17-7 (info).** Outline Ch.17 compared with the page: no departure touches a NON-NEGOTIABLE.
  - **Open count:** 35 → 40 (−2 resolved, +7 opened).
- **Entities:**
  - **Characters:** 27 new. Onesimus and his grandson, wife, daughter and son-in-law. Celer's runner, sunshade slave, stranger and bearers. Plautia's hired bearers. L. Caninius; Doris; the Gnaeus witness; Plautia's mother's brother, grandfather, nurse and father's freedman. Marcus's nurse; Celer's copyist. The three dead witnesses (doctor, oil-seller, trainer). On the Lechaion road: the Alexandrian trainer, the athletes, the latrine's fat man, the pine-crown boys, the triumph-coin seller and the sausage-man.
  - **Celer in person (first live appearance):** physical (toga, shave, cup-handle ears, voice), traits, relationships, location_log and knowledge. He now knows Mara's name, the heavy shining thing, the bracelet, Valens's road to Rome, and that Plautia came to read her dowry. He does NOT know the leaf is gone.
  - **Renamed in place:** the games magistrate is now "P. Vettius" (read from p26 and p77), and Plautia's father is now "Sextus" (p53). Plautia's mother's silver is a ladle and two swan spoons, Sicyonian work.
  - **Main cast:** Ch.17 location, knowledge and knowledge_absent rows for Mara, Valens, Plautia, Felix, Marcus and Myrrhine. The planned Ch.17 rows are kept as `plan_was`. Valens's post (the back door, as a baker), his reading of his own name, and his legal_status are on the page.
- **Locations:** 3 new: `record-office-corinth` (the building), `lechaion-road` and `olympia` (mentioned). New Ch.17 facts on corinth, isthmia, lechaion, celers-house, plautias-brothers-house, kenchreai, puteoli, rome and sicyon.
- **Objects:**
  - 8 new: plautias-grandfathers-pen-knife (Mara, in her belt), vettius-first-book (with Celer, showing knot, no receipt), goose-stern-ship, valens-pine-crown-for-felix, onesimus-fig-cake, record-office-scaffold (closed), celers-bill-of-sale and triumph-coins.
  - Updated: manumission-record (WRITTEN; Valens holds it in his tunic) and plautias-bracelet (seen by Celer).
  - Closed: plautias-mothers-silver (the bribe), plautias-dowry-instrument (read as the cover) and plautias-writing-case.
  - Also updated: fathers-pentax-k1000 (custody, and what Celer knows by report), potted-fig-tree and lupus-reward-notice.
- **Timeline:** row 17 is filled from the page: spring AD 72, the boys' race morning of the games for Titus's triumph, from before dawn to a little past noon. Neither "Isthmia" nor "Isthmian" occurs in the chapter. Row 18 carries a ch17_note for CH17-1. One timeline_event is added.
- **Knowledge:**
  - Index rows added to maras_name, syracuse_cover, maras_camera, kirrha_road_killing, triumph_games_plan, valens_name and valens_and_plautia.
  - New indexes: `the_leaf_taken` and `valens_rome_road`.
  - New threads: the-showing-knot, celers-invitation, plautias-letter and the-knife-comes-home.
  - Updated threads: celer-and-the-frame, valens-papers, valens-known, plautias-son, plautias-question (answered in part by action) and kirrha-road-killing.
- **Needs review:** new for celers-stranger-man and dead-witness-trainer, and valens-school-trainer is flagged against the dead trainer. bandaged-corinthian's note is strengthened (Celer's "heavy … that shines", p172), but it stays separate under rule 8.
- **World rules:** 4 added (the two-name year, the year-book form, the open sea in spring, the pine crown).
- **Meta:** last_updated_chapter 17; chapters_tracked adds 17; last_updated_by, mode, source and the header comment are updated; `ch17_requested_checks` has 10 rows.
- **Not touched:** the manuscript, character-bible.md, STATE.yaml, foundation.md and outline.md.
- **Validation:** `yaml.safe_load` and a strict no-duplicate-key loader both pass.

## 2026-10-21: UPDATE re-sync (chapter 17 to the FINAL page)

- **Input:** `manuscript/chapters/chapter-17.md` at HEAD (md5 f30159769ef065525de4b14f63dd19de). Since the UPDATE run on d6b3291, three commits changed it: the continuity repair 141731e (C-01, W-01..W-10), polish cycle 1 2b7ea36 (56 swaps) and finalize F1-F14 6ae6426. The repair also patched outline Ch.18 (the same-afternoon opener) and outline Ch.22 (how the leaf is proved).
- **Numbering:** 274 → 270 paragraphs. Breaks now come after p91, p142 and p199.
  - old p1..p107 = new p1..p107
  - old p108 + p109 = new p108 (one speech of Mara's)
  - old p110..p122 = new p109..p121
  - old p123..p125 = new p122 (Mara's "Lose?" is cut)
  - old p126..p182 = new p123..p179
  - old p183 is cut (the bearers and the donkey; its boys-running clause moved into p226)
  - old p184..p274 = new p180..p270
  - Re-anchored by script: 744 explicit `ch-17:pYY` cites (485 shifted), plus the bare refs on Ch.17 lines, in the CH17-x blocks and in the recheck_ch17 fields, and two object `paragraph` fields (211 → 207, 193 → 189). Four bare-ref lines matched only because they mention Ch.17, but belong to Ch.16 (CH16-10 prose, two ch16_requested_checks rows and knowledge_absent_ch16). I caught them and restored them by hand. The four cites to old p183 were rewritten with their facts.
  - `meta.ch17_requested_checks` keeps the d6b3291 numbers and quotes. It is labelled as such and has a new RE-SYNC row.
  - `paragraph_rule` has the new Ch.17 map and sections. There are now six HTML comment lines, so on the final file line 10 = p1.
- **Page changes carried into the YAML:**
  - **Time of day (C-01):** the litter leaves the door "by the porch bench" (p14), and the hem is trodden "by the fuller's" (p215). The roof scene is now "in the cold before sunup" (p85). This updates the timeline row 17 sequence, Plautia's and Mara's location_log, the brother's house facts and the Corinth fact.
  - "the year Nero was here" (p26): Mara's knowledge and vettius-first-book.
  - Celer:
    - "Come out tomorrow, why don't you? Look down on us from the ladies' benches" (p162);
    - "a farm of his own" (p174);
    - "an entry in a magistrate's book" (p177);
    - "hid it in his toga";
    - "the glare of the forum" and "six paces of good planking" (p171; p189);
    - the toga "the Isthmus road had powdered it down one side" (p148);
    - Plautia's new litter sent back over a ladder (p83).
  - Valens:
    - "They'll take his money too, if he offers it." (p111);
    - "He'll talk at her till she agrees to something." (p138; "two summers and two winters" is cut);
    - he stands "a pace from her, between her and the forum" (p146; no longer "at her back");
    - the leaf read "to the end of the witnesses" (p100);
    - his thumbs leave flour on the frame (p97).
  - The leaf goes "between two of Plautia's letters" (p69).
  - The trainer: "in a Greek that was not Corinth's" (p240). The `alexandrian-trainer` slug is kept, with a note.
  - The washing on the garden wall replaces the dog (p270, lechaion-road).
  - The arch's "gilded bronze chariot … its horses green along their bellies"; the boys-running line moved into p226; the donkey is cut.
  - The latrine (Fortuna, the long seat; the fat man without "Mistress.").
  - The pine boys' and sausage-man's cries.
  - The coin seller's folding table.
  - The wall "gone to rubble in places".
  - Felix's crown "half bald", Valens's fingers "sticky".
  - The fig cake "sold in the market by weight".
  - The record office's bare second table (p4).
  - The scaffold, first seen at the door (p14; Plautia steps under it).
- **Contradictions:**
  - **CH17-1 RESOLVED.** The outline Ch.18 patch fits the same-afternoon arrival: "under an hour on a quay, the same early afternoon as Ch.17's run", the bags with Felix, and a "sunlit" quay, "dry in the sun". Timeline row 18 and locations.lechaion now take the patched outline, with the old values kept as `plan_was`. The bible's "awake since the second watch" is still a bible-sync item (CH17-6).
  - **CH17-2 RESOLVED.** "since I was nineteen" (p205) gives born about AD 44, about 27-28 in spring 72. That agrees with "thirty, or a little under". The derivation is added to plautia.physical.age.
  - **CH17-3 RESOLVED.** "the autumn before last" (p174) is autumn AD 70, which matches Dadaphorios AD 70.
  - **CH16-8:** a new `recheck_ch17_final`. "Her woman can come to Puteoli for it. Walk." (p218) means Myrrhine is no longer expected on the quay, so the sharper Ch.18 constraint is withdrawn. The base item (the household's "My wife" against the Lechaion wedding) stays UNRESOLVED.
  - **CH17-5 stays UNRESOLVED.** The audit's suggested path ("inferred", via Delphi talk and his man) is recorded as `audit_note` on CH17-5 and `audit_path` on knowledge_index.syracuse_cover. The page still shows no path.
  - **CH17-6:** the prose field is updated (ladies' benches; "Is that wax my father's?").
  - **CH17-8 NEW (low).** Mara uses a public latrine with men on the Lechaion road (p246-p252). That goes against the Ch.7 OBSERVED rule (ch-07:p36; CH14-7 was repaired to agree with that rule). The scene was on the d6b3291 page too, and the UPDATE missed it. A `ch17_note` is added to the world rule.
  - **Open count:** 40 → 38.
- **Audit and eval patches applied:**
  - `valens.inventory` mules ch17_note: four to Lechaion, "the two that had found no buyer" (F4), and the gray's fate unstated (I-13);
  - plautia age (W-04);
  - `objects.manumission-record.forward_ch22` from the patched outline Ch.22 (W-10: unsealed leaf, Celer holds the cut book, six living witnesses);
  - the pen-knife forward and `the-knife-comes-home` thread moved to Puteoli (W-09);
  - pine crown "half bald" / "sticky";
  - the gilded chariot.
  - The rest of the audit's suggested patches were already in from the UPDATE run (onesimus, Sextus, Celer's physical and knowledge, CH12-5, the pen-knife, the pine crown, the timeline).
- **Checks:**
  - Every single-quoted Ch.17 fragment was checked against the final page by script. The only misses left are deliberate history (the labelled d6b3291 quotes, the outline and bible quotes).
  - Quotes were also checked against their cited paragraphs. There is 0 new mismatch, except one deliberate history note ("at her back").
  - No cite is above p270 outside the labelled requested-checks block.
- **Not touched:** the manuscript, character-bible.md, STATE.yaml, foundation.md and outline.md.
- **Validation:** `yaml.safe_load` and a strict no-duplicate-key loader both pass. 269 characters, 81 locations, 114 objects, 129 contradiction rows.

## 2026-10-21: UPDATE (chapter 18, "Lechaion", post-disruptor page)

- **Page read:** chapter-18.md at a77ccc3 (the disruptor pass, after the writer d3cb979 and dialogue-polish 055d735), md5 ec8653732184a38e829b64cd6ec1821b. It has 77 paragraphs, one scene and no `* * *` breaks. The title and the four HTML comment lines are not counted, so file line 8 = p1 and file line L = p((L-6)/2). `paragraph_rule` now includes Ch.18.
- **meta:** `last_updated_chapter: 18`; 18 added to `chapters_tracked`; `last_updated_by`, `mode` and `source` updated; new `meta.ch18_requested_checks`.
- **The marriage (WRITTEN):**
  - The master's terms: "no priest and no cake, only the two of you saying so with two others to hear it" (p27).
  - The ten words: "Will you be my wife, Mara?" / "Yes." / "Will you?" / "Yes," (p33-p35).
  - The witnesses are the tar-handed sailor at the plank's head and Felix (p27; p36; p60). Pacuvius: "I heard." (p37). His daughter watches (p45).
  - Place and time: the Lechaion quay, early afternoon of the Ch.17 day, spring AD 72.
  - Updated: `mara-reyes.legal_status`, both characters' relationships and arc_waypoints, `plot_threads.romance.ch18_beat`, `maras-legal-nonexistence.ch18_note`, and the new `knowledge_index.lechaion_wedding`.
- **CH16-8 RESOLVED.** The household's freedman booked them at sunrise as "a muleteer and a wife and a boy" (p12) and had "Gone back up for the men's race" (p8; p20). Nobody from the Corinth household is on the quay. The Corinth "My wife" is now true, and no one who held it saw a first wedding.
- **The watch (WRITTEN):**
  - Valens takes it from his pouch and lays it in Mara's hand without a word (p47). It is warm, with flour in the links and on the crystal by the nick at the two (p48).
  - It is running and the spring is "wound tight to its end" (p48). It reads "twenty to one", with the post's shadow a little past noon (p49).
  - Mara tries it on her LEFT wrist against Plautia's gold, then holds out her RIGHT arm. Valens closes the clasp with his nail (p51; p52). "The watch sat on the wrong wrist and ticked." (p53)
  - The bracelet stays on the LEFT, which meets the audit's I-29 forward item (`plautias-bracelet.ch18_result`).
  - Custody: valens → mara-reyes. The outline's custody row is kept as `plan_was`.
  - New `windings` row: found wound, winder not shown. The page never says he kept it wound for the span. New fields: `time_setting_ch18`, `wrist_ch18`, `physical_ch18` and `witnesses_ch18` (nobody is shown seeing the return).
  - `knowledge_index.seiko_with_valens` gets the return row.
- **Pacuvius (NEW):** `ship-captain-lechaion` is renamed `pacuvius`, with `former_slug` kept and the gulf-coaster-master note updated.
  - Physical and speech: a leather cap; tunic hitched through his belt; harbor Latin; left foot bare after a lost sandal ("if any of you sees a sandal floating past the mole, it's mine", p46; how he lost it is not on the page).
  - His daughter, "married at the Kalends to a man at Puteoli she's never set eyes on", is going to her husband's mother (p17). "By proxy" is noted as a reading, not page wording.
  - The Ostia story (p17).
  - Also new: pacuvius-daughter (the girl in the blue hood), the told-only husband and mother, tar-handed-sailor, goose-ship-crew, towboat-rowers-lechaion, lechaion-fish-seller.
  - New location `ostia` (told). Facts added to lechaion (`ch18_facts`) and puteoli.
- **The goose ship:**
  - Description from the page: the goose carved from the sternpost, flaking white paint, red beak; the plank; the brailed sail with lead rings; the towboat.
  - Destination Puteoli (p17; p30). The page names no cargo, so none is recorded.
  - Status `chekhov_closed`: they are aboard and the plank is in (p77). The sailing itself is not shown.
  - New `objects.italy-marble-ship` (background): "Not out of this harbor before the Ides, and that one's carrying marble, and she won't take a mule." (p22)
- **Aboard:**
  - All four mules: the dun refuses the plank and is blindfolded with Felix's tunic; "The other two" follow; Valens brings the black back (p54-p70).
  - The fig, carried up between Valens and Mara (p73-p76). CH16-9 gets `recheck_ch18` and stays open.
  - Felix, in his loincloth, "bare-shouldered and crowned" (p68; p71).
  - The pine crown is given to Felix (p41) and closed. New background objects: `felixs-tunic-blindfold` and `pacuvius-lost-sandal`.
- **Unchanged:**
  - The pen-knife is not on the page and Myrrhine is not on the quay. It stays for Puteoli (`ch18_note` on the object and on `the-knife-comes-home`).
  - Nobody knows who won the boys' race (Felix p42; Mara p43; the sailor's bet on "the small Sicyonian", p44). New `knowledge_index.boys_race_winner`.
- **Timeline:**
  - Row 18 now comes from the page. The old patched-outline value is kept as `plan_was_patched` beside the earlier `plan_was`.
  - Placed after the Kalends (if that was this month) and before the Ides; the month is not named.
  - The watch span is derived, about 16-18 months; the page states none.
  - Four new timeline_events rows.
- **Knowledge flow:**
  - New Ch.18 rows for Mara, Valens and Felix (incl. his pre-18 BELIEF that she was not married), Pacuvius, the sailor and the daughter, plus the freedman's told trait.
  - New `knowledge_absent_ch18` for Mara, Valens and Felix.
  - New rows on `maras_name` and `valens_name`.
  - No knowledge_gap.
- **World rules (Ch.18):** marriage by consent before two witnesses (Pacuvius's account); the nuts, torches and cake; a master answering for his passengers' standing, with Delphi's rolls carrying no weight in Italy; the brailed sail and towboat. The Ch.17 "every day" row gets a `ch18_note`.
- **Contradictions:**
  - **CH18-1 (low, UNRESOLVED).** The watch is near sun time with no setting shown. In Ch.11 it ran fast with the hands untouched, and Valens was never shown how to set it. The page also never says he kept it wound for the whole span.
  - **CH18-2 (info).** Celer's "Ships leave Lechaion every day" against one Italy ship before the Ides. Compatible.
  - **CH18-3 (info).** Felix holds that she is unmarried after the Corinth winter, and asks "Did you get it?" with no shown path to the errand. Compatible; not logged as a knowledge_gap because "it" is never named.
  - **CH18-4 (info).** Outline Ch.18 vs the page: none against a NON-NEGOTIABLE. The page never calls the watch a "wedding gift" or says "seventeen months".
  - **Resolved:** CH16-8.
  - **CRITICAL:** none.
  - **Open count:** 37 → 40.
- **Checks:** every single-quoted fragment on a ch-18 line was checked against the page by script. Two misquotes were fixed ("'Father,' … 'was mine like that?'" and "I'd money on the small Sicyonian"). The remaining misses are other chapters' quotes on mixed lines, plus the labelled reading "By proxy". No cite is above p77.
- **Not touched:** the manuscript, character-bible.md, STATE.yaml, foundation.md and outline.md.
- **Validation:** `yaml.safe_load` and a strict no-duplicate-key loader both pass. 275 characters, 82 locations, 117 objects, 133 contradiction rows.

## 2026-10-21: RE-SYNC (chapter 18, "Lechaion", FINAL page)

- **Page read:** chapter-18.md at a5af92d, md5 dbd5ac50047ee465bb51f78d85ac44a4. Since the UPDATE (a77ccc3 page), three passes landed: the continuity repair (a81d6e5, audit W-01..W-13), polish cycle 1 (7ab624c, 20 swaps) and finalize F1-F3 (a5af92d). The diff was taken from e2928f9 to HEAD.
- **Numbering:** still 77 paragraphs, one scene, no breaks. Nothing merged or split, so **no ch-18:pYY is renumbered**. A fifth HTML comment line moved file lines down by one, so file line 9 = p1 and L = p((L-7)/2). The audit cites the a77ccc3 file (L = p((L-6)/2)); the eval's final sections cite the final file. Text changed inside 28 paragraphs (listed in `revalidation_needed`).
- **Corrected to the page** (superseded wording kept as `was` / `prose_was` wherever it carried a fact):
  - **The watch:** the old "the spring was wound tight to its end" is now "it took two and stood hard" (p48), so it is wound but not to its stop. The shadow is now "a short shadow on the stone, tipped a little east" (p49), with no sandal ruler. The other changes: "The hands were at twenty to one"; "Valens was minding the dun." (p50); "The case was warm from him."; the clasp now closes with "pressed." (the snap is cut), then "His fingers smelled of bread…" (p52). These went into `objects.fathers-seiko-watch` (custody row, windings row, `time_setting_ch18`), Mara's possessions and knowledge, Valens's relationship row, and the ch18 check results.
  - **The plank sailor:** "by Pollux" (was "by Castor", W-04); "a gray man stained with tar" (was "tar to the elbows"; canonical_name and physical). He now turns to answer Valens's "Keep off her heels," when he is kicked (p58).
  - **Pacuvius:** the harbor Latin is "stuffed with sailors' Greek" and "he stayed at the rail to use it on us" (p12). The priests clause is cut (W-05) from his trait and from the Ch.18 world rule. "Yours had a cake," loses "without turning round". Valens's "Twice over" is cut (W-13), and his offer is now "I'll pay the fare again," (Pacuvius's trait, Valens's relationship row and waypoint).
  - **Felix:** "Did you get it?" is cut (W-01). "like a boy half his age". He now blames the nuts ("It's the nuts," … "There should have been nuts."), not the sun, so "since sunup" is gone from the timeline row. Mara answers him "We are all of us watching the yard"; the master says "Your boy's been on that plank" (W-10).
  - **Mara:**
    - "I found breath enough for Latin, barely."
    - The cucumber memory now has "and rinsed it off under the tap". "to draw the bitterness out" is cut, so the page gives no reason.
    - Her yes is "Yes. Will you?" with "There was no voice under it" cut (W-07). Corrected in legal_status, both relationship rows, her waypoint, the romance thread and the check results.
  - **The opening (p1):** the wind "flattened my dress against my legs". Across the basin, "a man sat in a beached boat mending a net and whistling, as if the afternoon were his to spend". **Note for the orchestrator:** "hammering at a hull" (W-06) was the continuity repair's text, and polish cycle 1 then replaced the hammer with the net-mender (eval R1). The final page has no hammering, so `locations.lechaion` carries the net-mender and records barrel → hull → net in its `was` field.
  - **Objects:** goose ship "like a blind on its cords"; crown "before it reached the slot of water by the hull"; tunic "Felix peeled off his tunic". The daughter gets the alias "the master's daughter" (narration, p45).
- **Audit patches** (chapter-18-audit.md, SUGGESTED YAML PATCHES), applied against the final page:
  - The watch: custody, wrist and winding, as above.
  - mara-reyes ↔ valens: married. Already present; quotes fixed.
  - pacuvius: already created.
  - felix.knowledge (married, witnessed): already present.
  - felix.knowledge_absent_ch18: **adapted**, because the audit's wording assumes "Did you get it?" still stands. It now reads "whether the theft succeeded… (not asked on the final page)", plus "whether Plautia was to come to the quay ('Where's the lady with the litter?', p8)".
  - plautias-bracelet (left wrist) and the pine crown (given to Felix, worn aboard): already present.
- **Eval handoff** (chapter-18-eval.md):
  - The watch is on the RIGHT wrist, Felix's tunic is on the dun and the crown is on Felix. These were already present.
  - The leaf is under Valens's tunic: new `objects.manumission-record.ch18_note`, and the valens-papers `ch18_note` is updated.
  - The pen-knife is in Mara's belt. Already present as presumed; unchanged.
  - New `goose-stern-ship.ch18_handoff`: the towboat line, yard, stern rope and plank are on the page. Leaving "under tow on the afternoon breeze" is the eval's handoff, not shown. Pacuvius and his daughter are aboard. Do not compress the crossing (audit I-03).
- **Forward note on the marriage (new):**
  - Where it is recorded: `mara-reyes.legal_status` (Ch.18 row, `forward_note`), with pointers on `valens.legal_status`, `lucius.status_at_birth` and `aelia.status_at_birth`.
  - The law: a citizen freedman and a registered peregrine marry without conubium, so the marriage is *matrimonium iniustum*. It is valid, but the children take the mother's status.
  - Status: OPEN, pending the author at checkpoint 4. There is a Syracuse-colonia twist.
  - The rule until the author rules: no chapter calls the children citizens.
  - Also derived: Valens's own citizenship rests on the contested manumission.
- **Contradictions:**
  - **CH18-1 NARROWED, still UNRESOLVED.** The winding half no longer stands, because two turns fit a winding that morning (Ch.6, Ch.11). The shadow no longer needs a very short post. What stays open: the hands agree with the sun and nobody is shown setting them.
  - **CH18-3 NARROWED, still UNRESOLVED.** Part (2), "Did you get it?", auto-resolved by the cut. Part (1), the unmarried belief, stands as info. New part (3): "Where's the lady with the litter?" (p8) remains on the page. Audit W-01's optional cut was not applied. It is a question, so it is not a knowledge_gap.
  - **CH18-4:** recheck note added. Still none against a NON-NEGOTIABLE. Foundation row 18 now reads "sunlit quay" and outline Ch.19 now reads "goose ship" (a81d6e5); `locations.lechaion` gets a `foundation_note`.
  - **CH18-5 NEW (info, forward constraint):** the children's status, for checkpoint 4.
  - **CRITICAL:** none. **Open count:** 40 → 41.
- **meta:** header note, `last_updated_by`, `mode`, `source`, `paragraph_rule` (Ch.18 re-anchor), `revalidation_needed` (chapter 18, RESOLVED), and a `ch18_requested_checks` re-sync row.
- **Checks:**
  - Every quoted fragment on the YAML that was on the a77ccc3 page but is not on the final page was found by script. Each was fixed, or kept only as labelled superseded wording.
  - Every quote added in this re-sync was checked against the final page. The only misses are labelled was/prose_was text, other chapters' quotes on mixed lines, and plan/eval quotes.
- **Not touched:** the manuscript, character-bible.md, STATE.yaml, foundation.md and outline.md.
- **Validation:** `yaml.safe_load` and a strict no-duplicate-key loader both pass. 275 characters, 82 locations, 117 objects, 134 contradiction rows (41 open).

## 2026-10-21: UPDATE (chapter 19, "Puteoli", post-disruptor page)

- **Page read:** chapter-19.md at c98aaa0 (writer cb3d2fa, dialogue-polish 8d4e2f7, book-disruptor c98aaa0), md5 c4793a91f3dd935af6a501bd1ada2571.
- **Numbering:** 186 paragraphs, four `* * *` breaks after p24, p63, p95 and p127. The title, the book's first dateline heading (`#### *Puteoli · spring, AD 72*`, a heading, not counted) and the four HTML comment lines are not counted, so file line 10 = p1. The section offsets are in `meta.source_convention.paragraph_rule`.
- **Planned rows replaced by the page** (each keeps `plan_was`): Mara's and Valens's Ch.19 location rows; Mara's door knowledge row; Valens's "papers accepted at Puteoli"; both relationship rows with Grata; timeline row 19; locations puteoli, vesuvius, pompeii (the tomb roads, the distance, Grata's street), nuceria-gate-tomb, neapolis, misenum; the microcassette touch, the Pentax beat, the manumission-record beat; `knowledge_index.door_location`; `hand-at-threshold`.
- **Grata:** her whole entry is rebuilt from the page. It covers her description (p107), her flood, the arm-touching, and "You're Greek, you've the walk". It also covers the rooms (the dead cobbler's shop next door with two rooms behind, 24 sesterces), her husband at dice, her son at the baths, her cousin's bad wall and the whitewash patch. The plan's traits are kept, with `ch19_confirmed` / `ch19_page` notes.
- **gratas-husband:** first appearance moved from the planned Ch.24 to Ch.19. Grata tells of him, and the man in the sleeping tunic is him by reading only.
- **secundus:** first mention moved to Ch.19 (unnamed).
- **The clerk:** the clerk entry is rebuilt from the page. The short sight is shown and never named.
- **Pacuvius, his daughter and the mother-in-law:** all three get Ch.19 rows. The mother-in-law is now on the page, so her importance goes from mentioned_only to minor.
- **New:**
  - **Characters (7):** puteoli-wine-woman, neapolis-innkeeper, nola-carters, nuceria-gate-rose-woman, eel-sellers-family, aulus-numisius-eros (from the inscription), marcus-satrius-proculus (from the panel).
  - **Locations (8):** puteoli-wine-shop, neapolis-tunnel, neapolis-shore-inn, herculaneum-gate-road (the gate is unnamed on the page), stabian-gate, gratas-thermopolium, cobblers-shop, pompeii-amphitheater.
  - **Objects (4):**
    - pacuvius-daughters-brooch: chekhov_closed, mended with the pen-knife.
    - gratas-whitewash-patch: chekhov_open, planted.
    - back-room-barred-door: chekhov_open; "It sticks at the sill,".
    - muleteers-election-panel: background.
  - **Organizations (2):** misenum-fleet, pompeii-muleteers.
  - **Plot thread (1):** puteoli-letter-board, for Ch.21-22.
  - **World rules:** 9.
  - **timeline_events:** 6 rows (the crossing, DAY 1-4 and the carters' games ban).
- **Payoffs written:**
  - **the-where:** the secondary payoff is paid. The door is found at the tomb of Aulus Numisius Eros outside the Nuceria Gate (p165-p178). It is recorded as the home door's location.
  - **valens-papers:** paid (p41-p47). The manumission-record stays `chekhov_open` for Ch.22.
  - **theano-phrase:** "where the dead go out" is used (p164), use 2 of 3.
  - **The camera:** no frame (p19).
  - **"Seventy-nine.":** used once (p18).
  - **The mountain:** never named.
  - **The fig:** on the roof (p116).
  - **The pen-knife:** still with Mara (p6; p57).
- **Knowledge flow:**
  - Only Mara knows the door.
  - Valens: a door_location NOT row. He knows she is walking the tomb roads and has a Ch.15 path to their purpose, but he is not told she found it.
  - NOT rows also for Felix, Grata, the eel-seller's family and the rose-seller.
  - New `knowledge_absent_ch19` for Mara, Valens, Felix and Grata.
  - Rows added to valens_name, lechaion_wedding, felix_freedom, the_year, eruption_foreknowledge and maras_camera.
  - No knowledge_gap.
- **Contradictions:**
  - **CH19-1 (info):** outline Ch.19 against the page. The page has one mole, no Sarno, and a different search order: the tomb road into the town on arrival, the Stabian Gate on DAY 3. It never uses the word "dormant". None of this is against a NON-NEGOTIABLE.
  - **CH19-2 (low, forward constraint for Ch.20):**
    - The plan has the repair shop in "Grata's front room" and the old crack in Grata's wall.
    - On the page the shop is the cobbler's next door, and the crack is on another house, done by her cousin.
  - **CH19-3 (info):** Grata's husband (planned Ch.24) and Secundus (planned mention Ch.20) both appear earlier, unnamed.
  - **CH19-4 (info):** the marriage day count. "The twelfth morning" comes after "eleven nights", and "Twelve days" is said the next afternoon. Compatible if the wedding day counts as day one.
  - **CH19-5 (info):** the road takes about a day and a half, against Ch.15's "A day … or less" and the plan's "two days". Compatible.
  - **CH19-6 (info):** the knife thread. Myrrhine is not at Puteoli and no word is left for her.
  - **CH19-7 (info, forward constraint for Ch.21-22):** the Puteoli letter board against the plan's summons brought to Grata's counter.
  - **Rechecks:** CH16-9 (the fig's moves; still open) and CH18-2 ("no ship but ours yet in from Lechaion"; still info).
  - **Resolved:** none.
  - **CRITICAL:** none.
  - **Open count:** 41 → 48.
- **Checks:**
  - Every quoted Ch.19 fragment added in this run was checked by script against the page before writing; 422 fragments, 0 off the page.
  - Each fragment was then checked against the paragraphs its line cites. The only misses were object descriptions whose source sits on a sibling line.
  - No cite is above p186.
- **Not touched:** the manuscript, character-bible.md, STATE.yaml, foundation.md and outline.md.
- **Validation:** `yaml.safe_load` and a strict no-duplicate-key loader both pass. 282 characters, 90 locations, 121 objects, 20 organizations, 62 plot threads, 106 world rules, 198 timeline_events, 141 contradiction rows (48 open).

## 2026-10-21: RE-SYNC (chapter 19, "Puteoli", FINAL page)

- **Page read:** chapter-19.md at 9c5f9e8, md5 41dedf4d0160019238d30feef12fb042. Since the UPDATE (7c56d74, on the c98aaa0 page), three passes landed: the continuity repair (926f515, audit W-01..W-14; W-15 deferred to the bible), polish cycle 1 (1344b91, 27 swaps) and finalize F1-F5 (9c5f9e8). The diff was taken from 7c56d74 to HEAD.
- **Numbering:** still 186 paragraphs, with breaks after p24, p63, p95 and p127. Nothing was merged or split, so **no ch-19:pYY is renumbered**. A fifth HTML comment line moved the file lines down by one: file line 11 = p1, and the per-section formulas are in `paragraph_rule`. The audit cites the c98aaa0 file; the eval's re-evaluation and finalize sections cite the final file (its l.43 = p17). Text changed inside 44 paragraphs (listed in `revalidation_needed`).
- **Method:** every YAML line was scanned by script for wording that was on the c98aaa0 page but is not on the final page (quoted fragments, plus 4-, 3- and 2-gram scans). Every hit was corrected or kept only as labelled superseded text (`c98aaa0:` / `was` / `prose_was` / `method_was` / `description_was`). Every quote added in this run was checked against the final page.
- **The orchestrator's known changes, as they stand on the page:**
  - **Pacuvia is named:** "The master's girl, Pacuvia," (p2), "Pacuvia found me" (p4), "Pacuvia went down our plank first" (p27). `characters.pacuvius-daughter` is **renamed `pacuvia`**, keeping `former_slug`, new aliases and a `named_ch19` row. All 8 slug references were moved (relationships, a told_by method, three knowledge_index rows). The slugs `pacuvius-daughters-brooch` and `pacuvius-daughters-husband-and-his-mother` are kept.
  - **"by mid-afternoon"** (p63), was "by noon" (W-02). Corrected in timeline row 19, `locations.pompeii` distances (now "an afternoon and a day") and CH19-5.
  - **"the Locrians to the right"** (p2), was "Phocis" (W-03). The UPDATE had not recorded Felix's line, so it is now a new `locations.gulf-of-corinth` fact. The narration still has "the mountains of Phocis on the other" for the gulf itself.
  - **Three gates:** "Seven or eight. Three have tombs worth the walk." / "The third?" / "The Nuceria Gate. Tomorrow." (p154-p157), was "Only two" / "And the other?" (W-04). Corrected in `locations.pompeii`.
  - **Grata heard, did not see:** "I heard about you at that wall yesterday … half that street saw you" (p134), W-05. Her knowledge row's method changed from `witnessed` to unnamed street gossip; `method_was` is kept.
  - **The bar leans beside the door:** "lay looking at the bar leaning beside it" (p128), W-06. Corrected in `objects.back-room-barred-door`. Also "lifted it clear, opened it, and closed it once more" (p125, eval L2).
  - **The fig jar is at Felix's feet:** "The fig was on the stones at Felix's feet, jar and all." (p36), W-07. Corrected in CH16-9 recheck_ch19, Felix's location row and the fig's beats_ch19.
  - **The noseband** is cut "out of the one long strip the nephew had missed" (p145), W-08. Corrected in Valens's trait.
  - **Grata's line:** "it's been carts and dust since the earth went" (p108), W-10/W-11. She now gives no count; only Mara's "ten years ago" (p82, echoed by Valens, p83) carries C8. Corrected in timeline row 19, `locations.pompeii` and the checks.
  - **Pacuvia's recovery:** the page reads "sick for every mile of the Straits and well again by daylight" (p2, eval L1). **Rhegium is no longer on the page in any form.** The route now reads in order: gulf, narrows, islands, open sea, Italy on the sixth morning, round the toe, the Straits, then well again by daylight. "the Straits; Rhegium" was removed from timeline row 19, timeline_events and the crossing check. (The brief's "well again after Rhegium" does not match the page; this file follows the page.)
- **Also corrected to the page:**
  - **Mara:** the comprehension trait now shows 2 reports: "of which I caught perhaps half" (p27) and the baker lost (p131). Cut: "lost my hold…", "slowly enough for me to have all of it" and "I understood every word". At Neapolis she "stood under her balcony for the rest of it".
  - **Mara and the camera:** she draws it with no opener (both "Alone at the rail," and "Left to myself," are cut). "Seventy-nine. It came unasked," (W-09).
  - **The door:** "It was warm, with the whole day's sun in it." The car simile, "no business to be cool", the tomb shadows and "the door stayed cool" are cut; it is now "the door was cool." (p168; p169; p178).
  - **Grata:** "She caught a pinch of my sleeve and talked on holding it" (W-14) and "touched him on the arm" (no "too"). The description of her Latin is cut (W-01). "Sit there. I kept you a bowl." The whitewash is now "new whitewash", with no size given (`description_was` kept).
  - **The mother-in-law:** "Those on your father's deck, who are they?". Pacuvia wears "the brooch at her throat" (the brooch's resolution is corrected); "her good blue" now appears at dawn (p4) only.
  - **The clerk:** reads the leaf "one board and then the other". This is corrected in 6 places: the clerk, Valens, the leaf, the-papers payoff, the checks and knowledge_index.
  - **Puteoli:** the priest is arguing "about it", with no languages. The fleet passes on still water ("with no wind to help her" is cut).
  - **Felix:** W-13 turns two runs of questions into boasts ("Give me one. I've the steadiest hand on this road."; "I'd put him down for you.") and one into a statement ("You could drop a house in it and never see the roof.").
- **Audit patches** (chapter-19-audit.md SUGGESTED YAML PATCHES):
  - Applied:
    - timeline day mapping: marriage days 12-15 = landing DAY 1-4, with W-02;
    - `door_location`: the knuckle tap ("the same dull note, with rubble behind both");
    - `microcassette.location_end_ch19`;
    - CH18-5 `recheck_ch19`: Pacuvius's oath, "Valens. Gaius Iulius." in the wax, "You're Greek"; it settles nothing.
  - Already present, so not duplicated:
    - the new locations, under the UPDATE's slugs: puteoli / puteoli-wine-shop, neapolis-tunnel (the audit's crypta-neapolitana), neapolis-shore-inn, gratas-thermopolium, cobblers-shop, stabian-gate (the inn is a fact there), nuceria-gate-tomb;
    - the pen-knife; the leaf; the camera's no-frame row; Grata's first-appearance rows.
- **Eval handoff cascades:** all were present except the unhung shutter boards. "our boards still leaned against the inside wall because nobody had thought to put them up" (p186) is added to `locations.cobblers-shop`.
- **Contradictions:**
  - **CH19-8 NEW (low):** the bible's Ch.19 blocks quote the writer's draft (W-15; the eval's re-sync list). Examples: l.2073 "I saw you at that wall", l.3006 "well again by Rhegium", l.5121 "Only two have tombs". The daughter is unnamed there and needs a card. It resolves when the bible is synced.
  - **CH19-5 rechecked** (mid-afternoon; still info). CH16-9 and CH18-5 were rechecked and stay open. CH19-1, -2, -3, -4, -6 and -7: their quotes are unchanged on the final page, and they stay open.
  - **Resolved:** none. **CRITICAL:** none. **Open count:** 48 → 49.
- **meta:** header note, `last_updated_by`, `mode`, `source`, `paragraph_rule` (Ch.19 re-sync), `revalidation_needed` (chapter 19, RESOLVED), and the `ch19_requested_checks` rows corrected (each marked RE-SYNC), plus a re-sync row.
- **Not touched:** the manuscript, character-bible.md, STATE.yaml, foundation.md and outline.md.
- **Validation:** `yaml.safe_load` and a strict no-duplicate-key loader both pass. 282 characters, 90 locations, 121 objects, 20 organizations, 62 plot threads, 106 world rules, 198 timeline_events, 142 contradiction rows (49 open).

## 2026-10-21: UPDATE (chapter 20, "The Mender's Shop", post-disruptor page)

- **Page read:** chapter-20.md at e52b0d7 (writer f00ad5c, dialogue-polish 3718350, hook-craft notes 7ed9a4a with no edits, book-disruptor e52b0d7), md5 8486fa155aca3c78fbed98ee90ac7bc1.
- **Numbering:** 286 paragraphs, six `* * *` breaks after p45, p84, p129, p180, p223 and p249 (seven sections). The title, the dateline heading and the four HTML comment lines are not counted, so file line 10 = p1. The italic documents count as paragraphs. The section offsets are in `meta.source_convention.paragraph_rule`.
- **meta:** `last_updated_chapter: 20`; `chapters_tracked` now includes 20; header note, `last_updated_by`, `mode` and `source` updated; new `ch20_requested_checks` (13 rows).
- **Planned rows replaced by the page** (each keeps `plan_was`): Mara's and Valens's Ch.20 location rows; Mara's `pregnancy_1` and her Ch.20 arc waypoint; Grata's pregnancy knowledge row; the tremor-notes item, the fenn-notebook Ch.20 beat and the tremor-notes object (introduced is now ch-20:p131); timeline row 20.
- **Characters updated:**
  - **Mara:** traits (mending hands, boards, seams closed or left, the bowl, teeth), `teeth_ch20`, `weeps_ch20`, 13 knowledge rows, `knowledge_absent_ch20`, and the items bone-toothpick and fountain-pebble.
  - **Valens:** traits. He hides his reading from Felix again (p16; p206-p208). He writes, for the first time on the page (p119). The fig. The stone and the lamp. Also 6 knowledge rows, `knowledge_absent_ch20`, a `knowledge_gap` (CH20-6) and a Ch.20 waypoint.
  - **Felix:** `seen_ch20`, traits, a status row, a location row (he sleeps in the shop), 6 knowledge rows and `knowledge_absent_ch20`.
  - **Grata:** `seen_ch20`, traits (she has writing read to her), relationships (sister, cousin with a needs_review on the fig-selling cousin, the husband's cousin, son, Mara, Valens), 6 knowledge rows, `knowledge_absent_ch20`, a location row and a status row.
  - **Others:** secundus (`ch20_mention`) and dr-pinsky (a trait).
- **New:**
  - **Characters (25):** zosimus, hermes-stoker, gaius-iulius-polybius, infantio, polybius-whitewasher, lantern-boy, lost-pot-cook, coppersmith-next-street, leek-woman-and-husband, stewpot-woman, rubble-carter-bowl, rattle-girl-and-mother, forum-quarrymen, bone-turner, fullers-wife-pompeii (needs_review), fuller-pompeii, fountain-line-women, fountain-toddler, toddlers-father-dyer, board-reading-carter, fish-sauce-carter (needs_review), lime-carter-to-puteoli, carting-foreman (needs_review), successus-the-weaver, iris-innkeepers-slave.
  - **Locations (7):** bull-fountain, red-house-at-the-corner, cookshop-above-the-fountain, pompeii-forum, crossing-baths, fullery-at-the-corner, sarno-gate. Facts added to cobblers-shop, gratas-thermopolium, pompeii-amphitheater, pompeii, stabiae, lechaion, puteoli-wine-shop and nuceria.
  - **Objects (19):**
    - chekhov_closed: lost-pot-notice, cooks-bronze-pot, stewpot-with-lead-dogs, red-gloss-bowl (the bowl given away), clay-pig-rattle, blue-scent-bottle, zosimus-fortis-lamp (the anchor), gratas-fish-sauce-jar.
    - chekhov_open: valens-letter-to-plautia.
    - background: menders-board, bone-turners-money-box, bone-toothpick, gratas-wine-board, fullers-aeneid-graffito, felixs-hare-bowl, polybius-election-notice, fountain-pier-graffiti, fountain-pebble, jug-graffito.
  - **Existing objects updated:** film-roll, fathers-pentax-k1000, potted-fig-tree, fenn-notebook, tremor-notes, plautias-bracelet, plautias-grandfathers-pen-knife, lentisk-stick, back-room-barred-door, gratas-whitewash-patch (not on the page, untouched), muleteers-election-panel, fathers-seiko-watch.
  - **knowledge_index:** new rows pregnancy_lucius and tremor_notes_known. Rows added to door_location, valens_reads, maras_camera and eruption_foreknowledge.
  - **Plot threads (2):** repair-trade and kalends-walks (payoff Ch.30, planned). Notes added to conception-and-lucius (the reveal is paid), plautias-letter, puteoli-letter-board and the-knife-comes-home.
  - **timeline_events:** 9 rows, plus a note on "AD 72 onward".
- **Film count:** the named frame (Valens asleep under the fig) is shot (p99-p100). By the plan count, 11 are shot and 25 are left. By the page count, at least 10 are shot and at most 26 are left.
- **Knowledge flow:**
  - Grata infers the pregnancy and says it aloud (p286). Mara is told by her. The fish-sauce carter overhears (p284). Valens and Felix do NOT know.
  - Only Mara knows of the tremor note ("nobody woke").
  - Valens is told about the Kalends (p126), but his "your gate" has no path on the page (CH20-6).
  - Felix still believes Valens cannot read.
- **Contradictions:**
  - **RESOLVED (2):**
    - **CH19-2:** the trade runs from the cobbler's shop. The notice goes over the crack on the red house, not Grata's wall.
    - **CH15-6:** the forward constraint is met. The pregnancy is revealed in autumn AD 73, the birth is due "with the heat", and there is no second contraception thought.
  - **NARROWED:** CH19-7. Valens's letter to Plautia goes out in summer AD 72 by a carter to the Puteoli board.
  - **Rechecked, still open:** CH16-9 (the fig: no change of home) and CH18-5 (the children's citizenship is still OPEN for the author at checkpoint 4; nothing on the page touches status).
  - **NEW (6):**
    - **CH20-1 (info):** outline beats against the page: the shop, the bowl, the column drums and tiles, the notice's wall, the stoker's reason. No NON-NEGOTIABLE is broken.
    - **CH20-2 (low):** "Two years and more" with the lentisk stick (p140), against a stick cut in winter AD 70 (ch-07:p58). The span is about 22-23 months.
    - **CH20-3 (low):** "the tree's first figs" and "These would never ripen" (p98; p110), against the Ch.15 dozen figs ripe at "End of the summer."
    - **CH20-4 (info):** where Felix sleeps. He has a blanket in the shop (p16), but "off to the stable" (p119).
    - **CH20-5 (info):** the wine-woman puts outgoing letters aboard (p122), against "Somebody comes for it" for incoming letters (ch-19:p61). Compatible.
    - **CH20-6 (low, knowledge_gap):** Valens's "Do you still walk out to your gate?" (p125). There is no page path to him knowing she found the gate. An off-page telling is possible.
  - **CRITICAL:** none.
  - **Open count:** 48 → 52.
- **Checks:**
  - Every quoted Ch.20 fragment on the added lines was checked by script against the page. None is off the page; one wording slip, "will put it aboard", was corrected before writing this entry.
  - Each fragment was also checked against the paragraphs its line cites. Missing cites were added; the only remaining mismatches are first_appearance notes that cite their naming paragraph inline.
  - No cite is above p286.
- **Not touched:** the manuscript, character-bible.md, STATE.yaml, foundation.md and outline.md.
- **Validation:** `yaml.safe_load` and a strict no-duplicate-key loader both pass. 307 characters, 97 locations, 140 objects, 20 organizations, 64 plot threads, 106 world rules, 207 timeline_events, 148 contradiction rows (52 open).

## 2026-10-21: RE-SYNC (chapter 20, "The Mender's Shop", FINAL page)

- **Page read:** chapter-20.md at b591762, md5 20bcc76c76ff17a127421c369cc3f273. Three passes landed after the UPDATE (617b1de, on the e52b0d7 page): the continuity repair (49a9870; C-01..C-03 with C-03 option A, W-01..W-14), polish cycle 1 (4cabab3, 41 swaps) and finalize F1-F11 (b591762). The diff was taken from 617b1de to HEAD.
- **Numbering:** 286 → **284 paragraphs**.
  - Two paragraphs were cut: old p188 (Felix: "Give me the ladder …", C-03) and old p278 ("Today," … "Tomorrow the wasps have them.", finalize).
  - Old p1-p187 keep their numbers. Old p189-p277 = new p188-p276. Old p279-p286 = new p277-p284.
  - Breaks are now after p45, p84, p129, p180, p222 and p248.
  - A fifth HTML comment line moved file lines down by one, so file line 11 = p1. The per-section formulas are in `paragraph_rule`.
  - Text changed inside 72 paragraphs (listed in `revalidation_needed`).
- **Method:**
  - 155 YAML lines were renumbered by script. This covered `ch-20:pYY`, bare Ch.20 refs on Ch.20 lines and in the CH20 rows and checks, and the `chapter: 20, paragraph:` fields of resolutions. No ref pointed at old p188. The refs to old p278 were all on lines rewritten by hand.
  - Every quoted Ch.20 fragment was checked against the final page and against the paragraphs its line cites. Five missing cites were added (p38, p213 twice, p270 twice).
  - A 4-gram and 3-gram scan looked for wording that was on the e52b0d7 page but is not on the final page. Every hit was corrected, or kept only as labelled superseded text (`e52b0d7:` / `*_was`).
  - No cite is above p284.
- **The orchestrator's known changes, as they stand on the page:**
  - **The opening notice has a single reward:** "Whoever brings it back gets sixty-five sesterces. The thief knows who he is, and so do I." (p1). It is "up on the pier" (p2), and "lettered in red" is cut.
    - Corrected in `objects.lost-pot-notice`, with `description_was` kept.
    - The cook's "A fellow told me where, wanting it" (p33) is noted in `cooks-bronze-pot`.
  - **The fig dropped last year's crop:** "a small heap of the summer's figs" (p98); "Last year she carried them all summer and dropped every one in the autumn." (p110). **CH20-3 RESOLVED.**
    - Updated in the fig's beats, Mara's knowledge, Valens's trait and the Valens check row.
    - The late figs now ripen "with the olives" (p275).
  - **Zosimus's lamp:** "I've had it three summers." (p257).
    - Corrected in his trait, Mara's knowledge, the lamp's description and the world rule. The rule had read "a lamp kept for forty years of dawns".
  - **The furnaces are lit in the mornings:** "Zosimus was back two mornings later, on his way down to light the furnaces. It was still dim in the shop." (p270).
    - Updated in his location row (`location_was` keeps "two evenings", "already dim") and in `locations.crossing-baths`.
  - **The mended pot holds oil:** "Make it tight. My oil lives in it." (p30).
    - Updated in the stewpot woman's trait and the stewpot's description, with `description_was` kept.
  - **Felix's blanket is "in the shop"** (p16), and the summer errand is "off to see to the dun and the black" (p119). **CH20-4 RESOLVED.**
    - Updated in Felix's status, location and knowledge_absent rows, Valens's writing trait, knowledge_index, cobblers-shop and the check rows.
  - **"Two years, near enough, I had cleaned my teeth with a chewed twig of lentisk"** (p140). **CH20-2 RESOLVED.**
    - Updated in `objects.lentisk-stick.beats_ch20`.
  - **Felix no longer holds the ladder.** He "sat among the painter's pots and tipped his face up to the ladder" (p192), and says "me out of mine half the night" (p194). The painter "shouldered the ladder" (p197).
    - Felix's status and location rows are corrected; the "holds the painters' ladder" and "the ladder's legs" rows are gone.
  - **One filled molar:** "the gap beside my sixth-grade filling" (p140).
    - `mara-reyes.physical.teeth_ch20` is updated, and it now agrees outright with ch-02:p50, ch-05:p154 and Ch.7 (one old filling). The old "two molars" wording is kept as `value_was`.
  - **Fish sauce on the bread:** "ladle some onto a carter's bread, and I covered my mouth." (p280); "pushed his bread across for more of it" (p282).
    - Updated in pregnancy_1, Mara's knowledge note, the fish-sauce carter's trait, the jar's description and gratas-thermopolium. The "ladle on its lip" is cut.
  - **No jar spill:** "I filled the jar at the spout and carried it home." (p242). The water down her side and the next woman's jar are cut.
    - The fountain-line-women trait is corrected (`trait_was` kept), and the check row is noted.
- **Also corrected to the page:**
  - the coppersmith knew the pot "on sight", and "This winter gone." (p38; p39, W-04);
  - Felix "with lime in his eyebrows" (p12);
  - the red house "past the temple crossing" (p182), and "They're painting the red house" (p183). This is corrected in CH19-2's resolution, CH20-1, pompeii, the whitewash patch, the red-house fact and the checks;
  - the frame "Through the lens the heat off the tiles kept him and his tree wavering" (p100), corrected in film-roll `frames_shot_ch20` and the named-frame row (the left/right layout is cut);
  - Grata's leaves line, "had not dropped a leaf since it budded"; and "It hasn't," (p115; p116);
  - Felix's line, "He went up and wrapped her, and he was no sooner down than up to see had he wrapped her right." (p179);
  - the tremor night, "the bed walked on its legs" (p131; "an inch" is cut);
  - the turner, "a curl of bone caught in his hair", "It buried my wife's mother … and after her a horse.", the box collected "that evening", and no dice (p134-p137; p173);
  - the whitewasher, "from the eaves halfway to the paving" and "at the mill with the donkeys" (p184; p189);
  - the painter, "a thin fellow sat with his pots of red in a row" (p185);
  - Grata's son "as he set off to bathe" (p208);
  - the fountain pier, "Someone had answered it in a deeper hand" and "Higher than any of them" (p213; p218);
  - the dyer, "a man whose hands were stained blue", and "his father insisted" (p238; p241);
  - Valens and the stone, "looked at it by the lamp, small and dry and gray". The phrase "a stone like any other in any gutter" is cut;
  - Zosimus: "The furnace stair did it," (p254); he scratches his beard, and the "black finger" now appears only at the plank (p253; p259). The lamp's nozzle line is cut, and "Round the filling hole the clay was black from his thumb." (p262);
  - repair-trade payments: bronze, a cheese, the toothpick and wine. There is now no payment on the page for Zosimus, the blue bottle or the second money box.
- **Audit patches** (chapter-20-audit.md SUGGESTED YAML PATCHES):
  - Applied:
    - CH20-3 and CH20-4 `remove_conflict`, now RESOLVED by the page;
    - `felix` status and location (C-03);
    - new `plot_threads.ch31-whitewash-raid`, with the C-03 constraint;
    - `objects.fenn-notebook.location_ch20`, which now notes its first physical appearance since Ch.3, the first back leaf, the blank back half (ch-02:p65) and that the writing implement is unstated (I-14);
    - W-15 forward constraint, added as `kalends-walks.forward_constraint` and as CH20-6's `audit_ruling`;
    - I-17 rulings, added as `audit_ruling` on CH20-1 and CH20-5.
  - Already present, so not duplicated:
    - `film-roll.frames_shot_ch20` and `running_count_after_ch20` (plan 11 shot / 25 left; page at least 10 / at most 26). Only the quote was corrected.
    - `knowledge_index.pregnancy_lucius`, the fish-sauce carter's overheard row.
  - Not applied:
    - `registries.command_echo` and `registries.item_by_item_look`. These are prose-pattern registries with no entity in this file's schema; they belong to the bible's at-risk registry.
- **Eval cascades:** Grata, the carter, Valens and Felix on the pregnancy; the letter path; the Kalends cadence; Felix still believing Valens cannot read; and Plautia's knife on loan were all present.
  - Added: `conception-and-lucius.ch21_handoff`, saying Ch.21 places Valens's knowing early, by Mara, before any street path (audit I-10).
- **Contradictions:**
  - **RESOLVED (3):**
    - **CH20-2:** "Two years, near enough".
    - **CH20-3:** last year's crop dropped.
    - **CH20-4:** the blanket is "in the shop", and the errand is the mules.
    - Each row keeps its e52b0d7 `prose` and adds `prose_now`, `resolution`, `resolved_from_conflict` and `resolved_date`.
  - **NEW (1): CH20-7 (low).** The bible's Ch.20 blocks as COMMITTED at HEAD lag the final page. Examples: l.1147 "Today,", l.3175 "Two winters back.", l.3178 / l.5492 "Make it hold. I cook in it.", l.3192 "with red to the wrists", l.3198 "blue to the elbow", l.3931 "Dropped it on the furnace stair," and l.5469 "Tomorrow the wasps have them.".
    - At this read, the working tree held an **uncommitted** bible sync by another pass that already carries the final text (`working_tree_note`). The row resolves when that sync is committed.
  - **Rechecked, still open:**
    - CH20-1: the outline still says "Grata's front room".
    - CH20-5: unchanged on the page.
    - CH20-6: unchanged on the page; the constraint has been added.
  - **CRITICAL:** none.
  - **Open count:** 52 → 50.
- **meta:** header note, `last_updated_by`, `mode`, `source`, `paragraph_rule` (Ch.20 re-sync), `revalidation_needed` (chapter 20, RESOLVED), the `ch20_requested_checks` rows corrected (marked RE-SYNC), and a re-sync row.
- **Not touched:** the manuscript, character-bible.md, STATE.yaml, foundation.md and outline.md.
- **Validation:** `yaml.safe_load` and a strict no-duplicate-key loader both pass. The file holds 307 characters, 97 locations, 140 objects, 20 organizations, 65 plot threads, 106 world rules, 207 timeline_events and 149 contradiction rows (50 open).

## 2026-10-22: UPDATE (chapter 21, "The Wolf's Old Name", post-disruptor page)

- **Page read:** chapter-21.md at 6828354 (writer 7acafef, dialogue-polish e891169, hook-craft d767ea1, book-disruptor 6828354), md5 91b9b3d298f6c27514e028ab4af41495.
- **Numbering:** 259 paragraphs, three `* * *` breaks after p76, p144 and p215 (S1 shop, S2 amphitheater, S3 shop, S4 barracks). The title, the dateline heading and the two HTML comment lines are not counted, so file line 8 = p1. The tablet text (p51) and Plautia's line (p53) count as paragraphs. Per-section formulas are in `paragraph_rule`.
- **Page, not report:** lines that `manuscript/reports/chapter-21-report.md` quotes but later passes cut are NOT recorded ("stood still since Corinth", the list of places, "six years since… sand", the freedman's dead Lupus). The disruptor's changed facts are recorded as they stand: the Capuan Lupus is alive and keeps a cookshop at Puteoli (p155); Grata's rumour is "Twenty times" against the true nine (p161); Felix overhears the argument's tail (p200); Felix's face "had gone young" (p98).
- **meta:** `last_updated_chapter: 21`; 21 added to `chapters_tracked`. Also updated: the header note, `last_updated`, `last_updated_by`, `mode`, `source` (outline now covers Ch.22-44) and `paragraph_rule`. New block: `ch21_requested_checks` (9 rows).
- **Planned rows replaced by the page** (each keeps `plan_was`):
  - Mara's and Valens's Ch.21 location rows.
  - Mara's summons knowledge row. It is now "discovered" (she reads the tablet), not told by the freedman.
  - Valens's Ch.21 waypoint.
  - Grata's summons knowledge row and its `dowry_suit_witness` index row, both now NOT ON THE PAGE.
  - The brother's freedman's "Grata's counter" trait, now NOT ON THE PAGE.
  - Timeline row 21, and the timeline_events row for the summons.
- **Characters updated:**
  - **Mara:** `pregnancy_1_ch21`, 6 traits, 2 relationships (nicanor, fabius-freedman), 12 knowledge rows, `knowledge_absent_ch21`, a Ch.21 waypoint.
  - **Valens:** `seen_ch21`, 9 traits, 2 relationships (nicanor, gaius-fabius-rufinus), 7 knowledge rows, `knowledge_absent_ch21`.
    - The traits cover: the arena record (nine; CH21-2); the heel; the tread; the hand that goes up and the washing; the flat refusal; misreading Grata; the case for being nobody; Felix and the sand; how he reads.
  - **Felix:** `age_ch21` ("The slaver said twelve, at Kirrha" / "Fifteen, then. Sixteen."; fits birth AD 58), `seen_ch21` (taller than Mara), 6 traits (the palm-branch trait CONFIRMED), the nicanor relationship, a status row and a location row, 6 knowledge rows, `knowledge_absent_ch21`.
  - **Grata:** `seen_ch21` (the gold earrings with the pearl), 4 traits (the "fancies Valens" foundation trait now on the page), 3 knowledge rows, `knowledge_absent_ch21`, a location row and a status row.
  - **Others:**
    - plautia: her line, and the four-line letter as knowledge.
    - plautias-brother: the summons trait, plus a ch21_note on the lodging row.
    - quintus-arrius-celer: the advocate and the farm (agrees with ch-17:p179).
    - lucius: ch21_note on timing.
    - ch21_notes on fish-sauce-carter, coppersmith-next-street, fullers-wife-pompeii, gratas-husband, lime-carter-to-puteoli, the-cilician and carting-foreman.
- **New:**
  - **Characters (18):** nicanor (needs_review vs lanista-pompeii and valens-school-trainer), gaius-fabius-rufinus, fabius-freedman, capuan-lupus, nicanors-young-fighters, saturnalia-thracian, arena-herald, youth-under-the-awning (needs_review vs Fabius), eggs-grandmother, cushion-sellers-wife, comb-boy, pompeii-bakers-boy, barracks-porter, show-painter (needs_review vs infantio), spice-seller-pompeii, carting-contractor (needs_review vs carting-foreman), gaul-with-no-wind (needs_review vs the-gaul), boy-from-patrae.
  - **Locations (1):** pompeii-gladiator-barracks. Facts added to pompeii-amphitheater (the north passage, the palaestra lane, the women's top ring, the tribunal, the water organ, the painted walls), pompeii, puteoli-wine-shop, puteoli, corinth ("the old school under the hill"), nuceria and rome (Basilica Julia, April).
  - **Objects (13):**
    - chekhov_open: summons-tablet, lupus-graffito-gatepost, felixs-palm-graffito, felixs-nail, murmillo-bowl-promised.
    - chekhov_closed: fabius-earnest-purse ("Take it back to him."; "I sent it home with him."), roof-stair-tread (oak in overnight; the old tread burned).
    - background: lupus-graffito-pier, spice-sellers-scales, bone-seat-tokens, gratas-pearl-earrings, falernian-from-the-fuller, eggs-grandmothers-egg.
  - **Existing objects:** valens-letter-to-plautia is now **chekhov_closed**: Plautia's reply, p53. back-room-barred-door gains a beat (p194; p195), which agrees with Ch.19.
  - **Plot threads (2):** rome-decision (open; the deadline is the Ides of March; it carries a forward constraint, below) and fabius-exhibition-offer (open).
    - **Paid:** puteoli-letter-board and plautias-letter.
    - **Notes added:** plautias-question, valens-known, felix-arena (opened on the page), felix-no-paper, valens-literacy, conception-and-lucius (Valens told; status updated), syracuse-cover and repair-trade.
  - **World rules (4):** women in the top ring by law; the finger, the editor's hand, the palm and the purse; the bloodless exhibition; a free boy may swear himself to a lanista.
  - **Organizations:** facts added to pompeii-gladiator-school (the planned recognition and refused offer CONFIRMED) and pompeii-muleteers.
  - **timeline_events:** 6 rows (late Nov AD 73 → Feb AD 74, plus the March and April deadlines set on the page).
- **Timing:**
  - S1 is "Twenty-six days" before the Saturnalia, about 21 November AD 73. It is the morning after Ch.20's reveal ("Last night. Grata knew before I did."). That is late autumn under a "winter, AD 73–74" dateline; this is noted, not flagged.
  - The pregnancy is due "With the heat. Summer, she thinks." If her first sickness came about mid-November, conception was about late September to October AD 73. That agrees with Lucius born summer AD 74 and with about six months at an April trial.
  - "The Ides is three months off," / "Less." on the day after the Saturnalia show is consistent.
- **Knowledge flow:**
  - **The summons:** the brother's tablet reaches Valens through the lime carter, who "looks at the board for me" (p25). It is read behind the curtain "because of Felix" (p49).
  - **The pregnancy:**
    - Valens is told first, by Mara (p26), before any street path reaches him ("Who knows?").
    - Felix learns next morning through the street chain, "The baker's boy says the carter says Grata says." (p66).
    - The grandmother has it "Grata says the heat" (p119). That is 26 days after Grata's "I've told nobody"; a path exists, so no gap.
  - **Lupus:** Felix, the fighters, Fabius, the herald, the bowl, the street and Grata all learn the name Lupus. Felix hears it for the first time on the page (p93-p96; p110).
  - **The argument:** Felix overhears its tail ("I'm not listening.", p200). How much he heard is not stated.
  - **No paper:** Nicanor is told Felix is free ("His own. I freed him."). Mara is told there is no paper.
  - **Reading:** Felix still believes Valens cannot read.
  - **No new knowledge_gap.**
- **Contradictions:**
  - **RESOLVED (2):**
    - **CH19-7:** the route is on the page: the board, the letter out by the lime carter, and the tablet back by the lime carter.
    - **CH20-5:** the outbound and inbound rules both work. The reply proves the letter arrived, and the tablet was fetched.
  - **Rechecked, still open:**
    - **CH20-6:** no tomb line in Ch.21; the constraint holds.
    - **CH17-5:** Valens fears a man at Syracuse, and Mara has nobody there.
    - **CH19-6:** no Myrrhine.
    - **CH18-5:** status not raised.
  - **NEW (5):**
    - **CH21-1 (info):** the outline's knowledge path has the freedman at Grata's counter. On the page the lime carter fetches the tablet from the Puteoli board. The NON-NEGOTIABLE's substance is met. The outline still carries the old line.
    - **CH21-2 (info):** the public version of the record. Nicanor, the herald and the freedman all say "Nine". Grata's "Twenty" is rumour. "Nero freed with his own hand" / "from the hand of Caesar" stand against the leaf's "set free by his master before … the emperor". The count is recorded as nine.
    - **CH21-3 (info):** Nicanor's identity is open: the Ch.28 lanista? the Ch.13 forms trainer? He is not the dead trainer of ch-17:p225. The "Gaul that had no wind" may or may not be the Ch.12 Gaul. This is also the first time the page places Valens's school at Corinth.
    - **CH21-4 (info):** the letter's "Four lines" included "the dun's hoof". No page shows trouble with the dun's hoof (the Ch.19 boot is the black's, ch-19:p89).
    - **CH21-5 (low):** Valens's "four years" of letting Felix think he cannot read. From about February AD 74, four years means a purchase in early AD 70. That is compatible with foundation's c. AD 70, but not if the purchase was that autumn.
  - **CRITICAL:** none.
  - **Open count:** 49 UNRESOLVED rows before this run (counted by script; the last entry's "50" was one high), now **52**.
- **Forward constraint (thread rome-decision):** the brother's freedman waits at Puteoli from the Kalends to the Ides of March AD 74. The hearing is in April, the same month as Fabius's Parilia show (21 April). Ch.22 must open with the decision made and the road taken before the Ides.
- **Checks:**
  - Every quoted fragment on the added lines was checked by script against chapter-21.md. Two misquotes were corrected before writing: the comb boy's "She's to be married…" and "There's oak behind the inn yard."
  - Fragments that are deliberately off the page are the plan/outline/foundation quotes and the four report-only lines named above as absent.
  - All ch-21 cites fall in p1..p259. Paragraph numbers were verified against a numbered dump of the file; p101/p102 and p239/p240 were caught and fixed.
- **Not touched:** the manuscript, character-bible.md (another agent is auditing in parallel), STATE.yaml, foundation.md and outline.md. Nothing committed.
- **Validation:** `yaml.safe_load` and a strict no-duplicate-key loader both pass. The file holds 325 characters, 98 locations, 153 objects, 20 organizations, 67 plot threads, 110 world rules, 213 timeline_events and 154 contradiction rows (52 open).

## 2026-10-22: RE-SYNC (chapter 21, "The Wolf's Old Name", FINAL page)

- **Page read:** chapter-21.md at 09443f2: the continuity repair b832f99, eval fixes F1-F11 1cc454c and finalize F-1/F-2 09443f2. md5 23e2aa5722cdd7b0be2d6a6eb692dd16.
- **Numbering:** 259 -> 254 paragraphs. Breaks now fall after p76, p144 and p210.
  - Cut: old p185 ("I saw.", W-13) and old p212-p214 ("Then his mouth began a word…" / "The Ides is three months off," / "Less.", W-08).
  - Merged: old p196 into old p195.
  - Map: old p1-p184 unchanged; p186-p195 → p185-p194; p196 → p194; p197-p211 → p195-p209; p215-p259 → p210-p254. Formulas are in `paragraph_rule`.
- **Renumbering:** 204 Ch.21 refs renumbered by script (ch-21:pYY, plus bare refs on Ch.21 lines). The six refs to the cut Ides lines were rewritten by hand.
- **Checks:** every quoted Ch.21 fragment was checked against the page and against its cited paragraphs, using a quote check and a 4-gram diff of the 6828354 page against the final page. One older wrong cite was fixed: "No. I was not there. I believe you anyway." is p205.
- **Facts carried from the page:**
  - Nicanor:
    - "This is him. The murmillo Nero freed." (p96)
    - "bandy-legged" (p84)
    - "Who does he belong to?" (p137)
  - Places and people:
    - "Kenchreai" (p96; p133), with a new fact on locations.kenchreai.
    - "the Syrian that had no wind and the boy from Argos that cried" (p93).
    - Valens: "I rake sand," (p99).
  - The summons: "It was from Plautia's brother, in a scribe's hand, round and even." (p50). It opens "To Gaius Iulius Valens, greeting." (p51). The brother stays UNNAMED and the audit's "Sextus Plautius" patch is NOT applied.
  - Fabius's freedman:
    - The earnest is "Fifteen hundred there, for earnest" (p150), half the raised 3,000. The 500 figure is replaced everywhere.
    - "when I was little" (p153).
    - "Your husband never asked…" (p155).
  - Felix:
    - "the child was due in the summer" (p151).
    - "Felix slid down and stood by the dun" (p98).
    - "Beyond the curtain Felix stopped turning over." (p197), added to his overheard rows and the knowledge index.
    - "two mornings running … On the third" (p211).
    - "Valens reached for the nail." (p231).
  - Objects:
    - The tread is "hollowed deep" (p41).
    - "tried that door twice" (p193).
    - The pier: "where whoever cut it had been jostled" (p140); "Three paces on, he stopped." (p141).
    - "LVPVS showed again" and the knife: "Valens slid his knife in where the wreath's two ends met and lifted the wreath off whole." (p252).
  - Others:
    - The street "fell away" (p224).
    - Grata's "wine cup" (p159); "she was left with her hand in the air" (p166).
    - Mara: "turned to the lamp until my mouth behaved." (p175).
    - The crier is "a boy" (p146), no longer tied to pompeii-bakers-boy.
- **Removed as page facts:**
  - Mara's laugh at the tread, now "He caught me watching him." (p42).
  - The sand and oak residue on Valens (p23; p42).
  - The black-mat doors (p63).
  - "on ice, and in snow".
  - "Mules, is it?" and "I drive mules".
  - "his face had gone young".
  - "My master can wait for him until the Parilia." The Parilia offer still stands at p129 and p150.
  - The Ides lines (timeline row 21, timeline_events, rome-decision).
  - Cut wording that carried a fact is kept only as labelled `resync_note` / CUT text.
- **Renamed (former_slug kept):**
  - gaul-with-no-wind → syrian-with-no-wind. Its needs_review against the-gaul is CLOSED.
  - boy-from-patrae → boy-from-argos.
- **Flags:**
  - **NARROWED:**
    - CH21-2: the "own hand" part is RESOLVED by Nicanor's "The murmillo Nero freed.". Still open (info): the herald's "from the hand of Caesar himself" puff, Grata's "a sword off Caesar" and the count nine.
    - CH21-3: the Gaul question is CLOSED. Still open (info): Nicanor vs valens-school-trainer and lanista-pompeii.
  - **Rechecked, still open:**
    - CH21-1: route unchanged; the outline is not yet patched.
    - CH21-5: re-anchored to p211, p249 and p251.
  - **Untouched:** CH21-4.
  - **NEW:** CH21-6 (low). The COMMITTED character-bible.md still quotes the Ch.21 writer draft ("brown and creased", "Cenchreae", "Whose is he?", "that Nero freed with his own hand"). The working tree already holds an uncommitted sync to this page. The row resolves when that sync is committed (same pattern as CH20-7).
  - **CRITICAL:** none.
  - **knowledge_gap:** none new.
- **meta:** updated the header note, `last_updated_by`, `mode`, `source` and `paragraph_rule`. Added a `revalidation_needed` chapter-21 row (RESOLVED), a `ch21_requested_checks` re-sync row, and the earlier check rows annotated with RE-SYNC notes.
- **Not touched:** the manuscript, character-bible.md, STATE.yaml, foundation.md and outline.md. Nothing committed.
- **Validation:** `yaml.safe_load` and a strict no-duplicate-key loader both pass. The file holds 325 characters, 98 locations, 153 objects, 20 organizations, 67 plot threads, 110 world rules, 213 timeline_events and 155 contradiction rows. **53 open** (52 before; +1 CH21-6). All ch-21 cites fall in p1..p254.

## 2026-10-23: UPDATE (chapter 22, "The Basilica Julia", post-disruptor page)

- **Source:** `manuscript/chapters/chapter-22.md` as it stands after writer 6aab721, dialogue-polish ff1bf65, hook-craft b4ef927 and book-disruptor f0111b2 (md5 579b651324ff772006d20cfb156bb933, same as git f0111b2). 210 paragraphs; breaks after p35, p67, p86, p119, p139, p157 and p188. The title, the dateline heading and the two HTML comment lines are not counted, so file line 8 = p1. Line formulas are in `paragraph_rule`.
- **Page over report:** `manuscript/reports/chapter-22-report.md` quotes lines that later passes changed. None of them is recorded. Page facts named in the dialogue and disruption reports were checked on the page:
  - The clappers at the verdict (p190, set up at p36). The page does not say "hired".
  - "The sixth?" / "With the rest." (p191; p192).
  - The gallery woman (p142-p144).
  - Celer's foot on the step (p200), and Valens's account of it (p167).
  - The 1991 board "still had the chisel in it" (p130).
  - The hiccups at the amphitheatre (p178).
- **The hearing:**
  - One judge ("a lean old senator with the broad purple stripe", eyes closed) with three assessors on stools and a water clock (p37).
  - Our advocate is short, square and hoarse. Celer's is young, with a beautiful voice.
  - Day one: the dowry is read (Doris, the earrings, the lampstand); the bill of sale is set against the leaf. The leaf has no seal, and "the knot is wherever the book is".
  - Two living names from the leaf come from Corinth: the dyer (fourth name) and the seasick merchant (seventh). The young assessor's uncle was consul "for his two months" but at Tibur in the bill's month.
  - Day two: "Gaius Iulius Valens. Freed at Corinth." to the back of the aisle; Thrace; the onion; his wages "On the Kalends, in silver"; the night of AD 69; the sneeze; the laugh; Mara is walked out.
  - The sentence comes on the judge's third day, the day before the Parilia (derived: 20 April AD 74). The dowry is restored whole, "the sixth part … together with the rest".
- **Celer on the steps:** the ladder, staged once; "Nobody wants the Cornelian law" (not glossed on the page); Marcus to dine at the brother's every market day while Plautia is in Rome, and at Corinth when she sends for him. "Plautia gave him no word." This is a new thread, `cornelian-law-quiet`.
- **New characters (26):**
  - The court: iudex-ch22, iudex-assessors, young-assessor, young-assessors-uncle, water-clock-slave, celers-advocate.
  - Witnesses and onlookers: corinth-dyer-witness, corinth-merchant-witness, onion-man-sneezer, gallery-woman-with-baby, basilica-attendant, celers-friends-rome, celers-slave-rome, will-court-neighbours, basilica-idlers, walnut-porters.
  - Rome walk-ons and offstage names: quirinal-widow, consuls-wifes-hairdresser, rome-chair-bearers, vestal-girl-with-ash, amphitheatre-builders, forum-custodian-1991 (memory).
  - Others: marcus-pedagogue, corinth-cooks-freedman, vitellius, ovid.
- **New locations (8):** basilica-julia, quirinal-widows-house, roman-forum-ad74, flavian-amphitheatre-works, capena-gate, celers-house-esquiline, argiletum, tibur.
- **New objects (5):** plautias-coan-shift (open: Myrrhine wants it back before Mara leaves Rome), widows-stapled-pot, basilica-step-gaming-board, myrrhines-red-shoes, sneezers-onion (closed).
- **Updated characters:**
  - mara-reyes: worn_ch22, pregnancy_1_ch22 ("Five. Nearly six."), mundane break 3 WRITTEN, the July 1991 memory, the encyclopedia at eight, knowledge rows, and the location row that replaces the plan row.
  - valens: testimony traits, the second onion surfacing, legal_status row, location row, arc waypoint, clothing.
  - plautia: hair, "not thirty", traits, relationship statuses, waypoint, location.
  - quintus-arrius-celer: traits, outcome WRITTEN, knowledge, location.
  - marcus: first on the page, no numeric age on the page. Relationships added: Valens "used to carry you", Myrrhine, the pedagogue, his uncle.
  - myrrhine: her origin is now on the page (p184).
  - plautias-brother: on stage, still UNNAMED (`first_on_page`).
  - Others: plautias-brothers-freedman, plautias-brothers-advocate (on the page), celers-steward, plautias-hairdresser, celers-second-false-witness (now "the stable boy", `canonical_name_was` kept), celers-mother, doris-dowry-slave, marcus-nurse, corinth-lanista, corinth-games-magistrate, lucius-caninius, nero, vespasian, lucius, felix, pomponia-grata, carting-contractor, gaius-fabius-rufinus.
- **Objects closed:**
  - celers-bill-of-sale: given "the weight it deserves".
  - manumission-record: proved; holder after the hearing is not stated.
  - rome-summons and summons-tablet: answered at Puteoli on the Kalends.
  - `status_was` kept on each. vettius-first-book was named in court; it stays open, held by Celer.
- **Threads:**
  - Resolved or paid: rome-decision RESOLVED; celer-and-the-frame PAID; plautias-son PAID; valens-known PAID.
  - fabius-exhibition-offer CLOSED by absence. Valens is in Rome on the Parilia eve; Fabius is not on the page.
  - plautias-question: answered in action, not in words. Plautia asks again: "Did he come because you asked him to?" / "He brought me."
  - Notes added to valens-papers, conception-and-lucius and the-knife-comes-home (still open).
- **knowledge_index:**
  - New rows: dowry_verdict and celers_settlement.
  - Rows added to valens_frame (the court; Myrrhine hears it for the first time), valens_and_plautia, valens_name, the_leaf_taken (Celer's side discovers the cut in court), pregnancy_lucius and dowry_suit_witness.
- **Other sections:**
  - world_rules: 7 OBSERVED rows (the court and its water clock, the retained sixth, a slave not heard against his master, no wheels by day, the Parilia ash, "Salve", the Cornelian law).
  - timeline: row 22 rewritten from the page (`plan_was` kept).
  - timeline_events: the 1991 row now comes from the page, without "as a student". The "spring AD 74 trial" row is replaced by dated page rows from the Kalends of March to the 21 April Parilia. Seven backstory rows added (c. 1973 encyclopedia; Myrrhine AD 63; Marcus autumn 64; the bill's month; the last afternoon of Caesar's games; the night of 69; the dog, summer 73).
- **Checked against existing entries, no clash:**
  - The frame is "summer, Vitellius had Rome" = AD 69 (Ch.12), and two years at her back = AD 67-69.
  - Marcus was born "the autumn after the fire" = AD 64.
  - The leaf is "the first book of Vettius and Caninius" (Ch.17), and the six living witnesses are strangers (Ch.17).
  - Plautia is "not thirty" (b. c. AD 44), and "five years" since she laughed (C9).
  - Mara was 26 in July 1991 (b. early 1965).
  - "Five. Nearly six." in mid-April fits Lucius in summer AD 74.
- **Flags:**
  - **NEW (all info except CH22-5, which is low):**
    - CH22-1: outline vs page. All three of the outline's routes against the bill are on the page; the Cornelian law is an addition.
    - CH22-2: about six weeks between the Kalends of March at Puteoli and the mid-April arrival are not accounted for on the page; derived dates.
    - CH22-3: "this city" reads as Marcus born in Rome. Myrrhine, given at twelve, is not in the dowry list, where the girl is Doris, aged eleven.
    - CH22-4: the night-of-69 details beyond Ch.12. The stable boy is the second witness. "When he was away" is dropped. The clerk, not the magistrate, wrote the entry.
    - CH22-5 (low): the bible's Ch.22 walk-on section lags the page ("still at his villa at Tibur"; the advocate reads "like a cargo").
  - **Rechecked, still open:**
    - CH12-9: Thrace is now named; the second onion surfacing.
    - CH16-5 and CH17-6: Myrrhine's "from her father's house" is now on a page.
    - CH18-5: no status line; the sentence does not rule in words on Valens's freedom.
    - CH19-6: Myrrhine is present, the knife is not mentioned.
    - CH21-2: no count of fights; Nero touched the sword.
  - **CRITICAL:** none.
  - **knowledge_gap:** none. Celer's "I hear there's to be a child" is covered by the visible pregnancy; his "They tell me it's Valens now" has no path shown and needs none.
- **meta:** header note, `last_updated`, `last_updated_by`, `mode`, `source`, `last_updated_chapter: 22`, `chapters_tracked` +22, `paragraph_rule` (Ch.22 clause), `ch22_requested_checks`.
- **Not touched:** the manuscript, character-bible.md, STATE.yaml, foundation.md and outline.md. Nothing committed.
- **Validation:**
  - `yaml.safe_load` and a strict no-duplicate-key loader both pass.
  - Every ch-22 cite falls in p1..p210. Every quoted Ch.22 fragment added in this run was checked by script against its cited paragraphs, and four inexact quotes and six cites were corrected.
  - The file holds 351 characters, 106 locations, 158 objects, 20 organizations, 68 plot threads, 117 world rules, 226 timeline_events and 160 contradiction rows.
  - **56 open** (51 before; +5 CH22-1..CH22-5; none closed).

## 2026-10-23: RE-SYNC (chapter 22, "The Basilica Julia", FINAL page)

- **Page read:** chapter-22.md at 2bbc3ee: the continuity repair a0ec3a1 (C-01..C-04, W-01..W-14 with the orchestrator's no-Sinuessa override on W-01, I-11/I-13/I-16), evaluator fix sets cd36062 (cycle 0), 2a832ed (cycle 1), e86ad92 (cycle 2, Q1) and the header refresh 2bbc3ee (cycle 3 PASS). md5 868fb363fdb21eaa1787e94987c16449.
- **Numbering:** still 210 paragraphs, with breaks after p35, p67, p86, p119, p139, p157 and p188. A paragraph-level diff against the f0111b2 page shows only 1:1 replacements, so the line formulas hold and **no cite was renumbered**. Text changed inside 50 paragraphs; they are listed in `paragraph_rule`.
- **Checks:** every quoted Ch.22 fragment in the YAML was checked by script against the final page and its cited paragraphs. 37 fragments were no longer on the page; each is rewritten to the page or marked CUT with the post-disruptor wording kept for the trail. Unquoted paraphrases of cut lines were found by keyword and fixed too. Two older cite gaps were fixed: Celer's "this morning" is p200, and "my young friend" is p190.
- **Facts carried from the page:**
  - Timeline: "and we had a month in it before the court sat." (p7). The roof's "Tomorrow" is now "When the judge sits" (p26) and "On the day" (p35). Derived: they arrive in Rome in March (the road is not timed), then a month in the widow's house, hearing days about 16-18 April, sentence 20 April. Timeline row 22 and timeline_events are updated (`date_was` kept), with a new told row for the month in the house.
  - Mara: "Somewhere in all that I sweated through my shift" (p117, C-02); "a wet shift" on the steps stays. The pregnancy row now dates "Five. Nearly six." to the March arrival, about five months, which is compatible.
  - Myrrhine: "I had my arm round you and my hand on her. I felt it." (p126, C-03). "He's good at waiting, that one." is cut. The spoon and "He bit everything" are cut (p185, W-04); "He bit my ear and hung on" stays. The shoes at her wrist and "She stood, holding her shoes." are cut, so `myrrhines-red-shoes` is last mentioned at p139.
  - Court: "two coached house slaves" (p42, C-04); "and I stood while his clerk wrote." (p103); "for his turn," (p62, W-14); "the law gives him" (p190); "the seals pressed over the cord in a row" (p45). The judge's eyelid lines and "without opening his eyes for it" are cut (F1). "with closed eyes" (p37) and "eyes still closed" (p114) stay, and "the judge sat forward" (p61) is new.
  - Valens: "He pitched it as he would hail the string in a crosswind" (p92); "Who was on the roofs, and where the dogs were." (p148, W-05); "his gaze at the aisle's end" (p152). The door and pier stances are cut (W-08).
  - Celer: "'Valens,' he said, and crossed to us." Neither the hand nor the toga fold is on the page now (C-01). "Celer's bench included" (p65, W-11). "stepped down two steps and along … to the brother" (p199, W-02/W-12).
  - Marcus: "His toga had a purple border … his ears poked out on either side" (p205, W-03/I-16).
  - Plautia: "In two years he never told me" (p30, W-06). The shift is "fine Egyptian linen" (p171, I-13). The object slug `plautias-coan-shift` is kept, with `slug_note` and `description_was`.
  - Places: "the second hill over" (p22); "calf's ash, a horse's dried blood and bean stalks" (p136, I-11); "the beginning of the amphitheatre, not a third built" (p176); "The emperor's building it out of Judaea." (p182, Q1; "Who pays for all that?" is retired); the brother's purse "counted out for two, and then for one again" (p19, W-13); "at their walnuts again" (p208).
  - Cut and NOT logged as used: the amphitheatre hiccups, and the repair's "the child stretched in me from one hip to the other", which evaluator F9 cut (p178). The S3 lying-awake close (p86) is also cut.
- **Audit patches (SUGGESTED YAML PATCHES):**
  - Applied where the page carries them:
    - Timeline (W-01, as amended by the override).
    - Pregnancy row.
    - Laugh channel: the sweat, recorded in the mundane-break trait. There is no `body_channels` field in the schema, so none was made.
    - Basilica seating: a new basilica-julia fact from p38.
    - Marcus's toga.
    - Fabius: a `resync_note` on `fabius-exhibition-offer` records the refusal in Ch.21. Valens in Rome is recorded for 20 April only, because the page does not place him on the 21st.
  - Already present: the Celer ch22 facts, young-assessors-uncle (unnamed), Celer's foot knowledge for Valens and Mara (p167), and the walk-ons. The ladder slave stays a basilica-julia fact, not a character.
- **Flags:**
  - **CLOSED:** CH22-2, RESOLVED. The month in the house accounts for the weeks between the Kalends at Puteoli and the hearing.
  - **Rechecked, still open:**
    - CH22-1 (info): new note that the amphitheatre beat no longer thinks of the child.
    - CH22-3 (info): p31, p41 and p184 are unchanged word for word.
    - CH22-4 (info): the clerk's wording and "coached" updated.
    - CH22-5 (low): the bible has no working-tree change and its Ch.22 blocks are still the writer draft. The lag has grown: "for his two months", "the small wetting", "his ears stuck out from it", "the bitten spoon". It clears when the parallel bible sync to this page is committed.
  - Elsewhere: the CH18-5 and CH21-2 recheck notes are updated (the hiccups are cut; the clerk's wording).
  - **NEW:** none. **CRITICAL:** none. **knowledge_gap:** none.
- **meta:** updated the header note, `last_updated_by`, `mode`, `source` and `paragraph_rule` (Ch.22 clause). Added a `revalidation_needed` chapter-22 row (RESOLVED) and a `ch22_requested_checks` re-sync row; earlier check rows are annotated with RE-SYNC notes.
- **Not touched:** the manuscript, character-bible.md, STATE.yaml, foundation.md and outline.md. Nothing committed.
- **Validation:**
  - `yaml.safe_load` and a strict no-duplicate-key loader both pass. All ch-22 cites fall in p1..p210.
  - The file holds 351 characters, 106 locations, 158 objects, 20 organizations, 68 plot threads, 117 world rules, 227 timeline_events and 160 contradiction rows.
  - **55 open** (56 before; −1 CH22-2; none opened).

## 2026-10-23: UPDATE (chapter 23, "An Inn on the Appian Way", post-disruptor page)

- **Page read:** chapter-23.md at 5948326 (writer 4dcddea, dialogue-polish aa0a7de, hook-craft 48d7211 with no edits, book-disruptor 5948326). md5 be315dc240d5ac16b71108b92bd47975.
- **Numbering:** 157 paragraphs and no breaks. The title, the dateline heading and the two HTML comment lines are not counted, so file line = 2p+6.
- **Not recorded:** lines the writer's report quotes that the polish and disruptor passes cut ("the size of a wine jar", the five-years paragraph, "These days I was always hungry."). The page has "I was hungry the way I was always hungry now, which was all the time" (p58).
- **NEW characters:**
  - `acca`: the landlady, named once by a shout (p46). She has a man's cloak, a dialect, the brown hen ("Fox. Had the other six." / "She sleeps on me."), no pennyroyal left, and has been to Fundi once for a wedding.
  - `appian-inn-barge-man`: heard through the floor with three mules. Valens says the gray is lame "Off hind". What he is to Acca is not stated.
  - `capuan-carriage-driver`: has a single eyebrow and sings to the frogs. His off-side mule is going short on the near fore.
  - `appian-inn-carters`: two of them, carrying roof tiles for Tarracina. They tell the story of the mule with a cough and say "He'll have you over at Fundi."
  - `valens-mother`: mentioned only, unnamed.
  - `horace`: mentioned only.
- **NEW locations:** `marsh-road` (the canal, the towpath, the halfway post, the flood "a hand deep, for two hundred paces"), `forum-appii`, `tarracina`, `fundi`, `sinuessa`.
- **NEW objects:**
  - `horse-blanket-appian-inn`: cavalry girth band, washed at the Kalends. Opened at p1 and closed in the chapter by the fleas at p157.
  - `appian-inn-strung-bed`, `appian-inn-drip-bowl`, and `brothers-hired-carriage` ("as far as Capua").
- **NEW knowledge_index row:** `valens_onion_memory` (Ch.12, Ch.22, Ch.23).
- **Plan rows replaced by the page (plan_was kept):**
  - Mara's and Valens's Ch.23 location rows.
  - `appian-way-inn`'s plan fact.
  - Timeline row 23.
  - Valens's flogged-back row: `outline:ch-23` becomes ch-23:p111, the first time the back is seen on the page.
- **Updates:**
  - Mara: `pregnancy_1_ch23`, `marks_ch23` (flea bites), traits (Horace at nineteen; "Down. Home."; "I missed it"; HEAT 2; the door side), knowledge (+8), `knowledge_absent_ch23`, a Ch.23 waypoint.
  - Valens: `seen_ch23`, traits (+9: the five words; the onion with his mother; reading animals; guard habits; the door-side reversal; the bowl; HEAT 2; the kick; the laugh by a breath), knowledge (+5), `knowledge_absent_ch23`, a Ch.23 waypoint.
  - Other characters: Grata (the winter advice, "until the eighth month"), Plautia's brother (the carriage to Capua), the brother's freedman (walks behind to the city gate with the chair's price) and `lucius.ch23_note`.
  - Places: `capua`, `capena-gate` (the gate is not named in Ch.23) and `pompeii` ("Down. Home.").
  - Timeline: 7 new `timeline_events`.
  - Threads: `romance.ch23_beat` (HEAT 2 of 3 spent), `valens-known` aftermath WRITTEN, `conception-and-lucius.ch23_note`.
  - `knowledge_index.pregnancy_lucius`: +2 rows.
- **Requested checks:** recorded in `meta.ch23_requested_checks`.
  - Dates: the day is not on the page. The inn night falls after the 20 April sentence, with Forum Appii behind them that morning, so it is no earlier than about 22 April AD 74 (derived).
  - The onion memory agrees with Ch.12 (strings under the eaves) and Ch.22 (every house). It adds his mother and an unexplained "us", so it stays unexplained.
  - A remembered mother agrees with "Thracian-born, taken as a boy".
  - The door-side reversal is set against ch-22:p111 and ch-14:p9.
  - The child is "it" in every mouth (AUTHOR-CP4-1 holds).
- **Flags:**
  - **NEW:**
    - CH23-1 (info): the outline's "the truth cost five years" is not on the page. The five words, the unexplained onion and the fade are.
    - CH23-2 (info): "You heard it at Kirrha. At the stream." The Ch.12 telling was at the pool above the ford on the Kirrha road.
    - CH23-3 (info): "At six months" in late April against Ch.22's "Five. Nearly six." in mid-March. Compatible as a round count; the birth still falls in summer AD 74.
    - CH23-4 (low): "the most of a laugh you got" against his laughs on the page in Ch.6, Ch.15 and Ch.16.
  - **Rechecked, still open:** CH12-9 (the third onion surfacing agrees) and CH18-5 (the child is ungendered and its status is not raised).
  - **CLOSED:** none. **CRITICAL:** none. **knowledge_gap:** none.
- **meta:** header note, `last_updated_by`, `mode`, `source` (Ch.1-23; the outline now covers Ch.24-44), `last_updated_chapter: 23`, `chapters_tracked` +23, `paragraph_rule` (Ch.23 clause), `ch23_requested_checks`.
- **Not touched:** the manuscript, character-bible.md, STATE.yaml, foundation.md and outline.md. Nothing committed.
- **Validation:**
  - `yaml.safe_load` and a strict no-duplicate-key loader both pass.
  - All 375 ch-23 cites fall in p1..p157.
  - Every quoted Ch.23 fragment was checked by script against its cited paragraphs. Three cites were corrected. The fragments left unmatched are plan or dateline quotes and are labelled as such.
  - The file holds 357 characters, 111 locations, 162 objects, 20 organizations, 68 plot threads, 117 world rules, 234 timeline_events and 164 contradiction rows.
  - **58 open** (54 before; +4 CH23-1..CH23-4; none closed).

## 2026-10-23: RE-SYNC (chapter 23, "An Inn on the Appian Way", FINAL page)

- **Page read:** chapter-23.md at f797736, after the continuity repair 80e0e9d, evaluator fix set F1-F9 (611926e), G1-G6 (beb6634) and the header refresh f797736 (cycle 2 PASS). md5 3599a74c0b2fe1223da9ce98ef2b5192.
- **Numbering:** still 157 paragraphs and no breaks; file line = 2p+6. No renumbering was needed. Text changed inside 38 paragraphs (p9, p17, p18, p24, p25, p26, p32, p40, p53, p58, p59, p60, p64, p65, p71, p72, p85, p94, p106, p109, p110, p111, p114, p116, p117, p122, p129, p130, p133, p134, p135, p137, p139, p141, p147, p150, p156, p157), found by a paragraph diff against 5948326.
- **Carried from the page:**
  - The two carters are now tilers (W-19). `appian-inn-carters` is renamed `appian-inn-tilers`, with `former_slug` and the old name kept as an alias. "The younger tiler laughed" (p71). "the cheating carter" (p71) is the mule seller, not one of them. The tilers also replace the carters in Mara's knowledge, the driver's alias and trait, the marsh-road, Tarracina and Fundi facts, and the knowledge_index row.
  - "brown as lentil soup" (p9), "His eel was cold." (p58, G1), "in a carrel," (p59), "gave the roof a word" (p72), "Who we were, he left out." (p94) and "spat water onto the floor" (p94).
  - Valens's back: "Between them the skin was brown, so that his back looked combed." (p111, C-05). "road-brown" is cut.
  - HEAT 2: "He looked, and his face gave me nothing to read." (p117), "The muscles of his belly jumped under my thighs every time." (p129, F7), "He let me look at his face with nothing in front of it." (p134) and "my collarbone had it before my ears did" (p137, F8).
  - "Somebody down in the stalls was talking low to the gray." (p147). The speaker is not named; the barge man's row now says so. Continuity I-04 reads it as later than p106's "nobody down there said anything more", not as a clash.
  - "By and by he slept." (p156, C-04 and G3).
- **Cut lines removed as page facts or marked CUT:**
  - "At six months there was no graceful way to do it" and the undressing sentences (C-03). This touched Mara's `pregnancy_1_ch23`, the HEAT 2 trait and the waypoint, `lucius.ch23_note`, `romance.ch23_beat` and `conception-and-lucius.ch23_note`.
  - "The nipples had gone wide and dark" became "The nipples were wider and darker." The narrated chafing, "puffed over the strap marks", the shin and knee bites (W-15) and "slow was all the belly allowed" are cut.
  - The room-read on entering (W-02): this changes Valens's guard trait and the common-room fact (no window or shutter there now).
  - Other Valens lines: "He watched the road." (F1), "He watched it a little." (W-02), "He went quite still." (F9), "with his weight given up …" (W-10), the breathing catch, and the laugh by a breath (C-04, G3). The laugh trait is kept only as a CUT record with `last_confirmed`.
  - The kept-stillness gloss (F7), the lamp below the boards (W-16) and the mule's second kick in the fade (C-04).
  - The radiator (W-17): Mara's Horace trait and the c. 1984 timeline event.
- **Flags:**
  - **CLOSED:**
    - CH23-1: foundation §10 is patched to say the page leaves the five-year count unprinted and any later chapter that prints it says five.
    - CH23-2: the final wording is unchanged ("You heard it at Kirrha. At the stream.", p62). The stream is on the Ch.12 page (ch-12:p60; ch-12:p62), and continuity I-16 rules "at Kirrha" a loose naming. No second value is left.
    - CH23-3: no month count is on the Ch.23 page. About seven months is derived from Ch.22's "Five. Nearly six." in mid-March, and Lucius is due summer AD 74.
    - CH23-4: the line is cut.
  - **NEW:** none. **CRITICAL:** none. **knowledge_gap:** none.
- **meta:** header note, `last_updated_by`, `mode`, `source`, the Ch.23 clause in `paragraph_rule`, a `revalidation_needed` chapter-23 row (RESOLVED) and a `ch23_requested_checks` re-sync row. Earlier Ch.23 check rows are annotated with RE-SYNC notes.
- **Not touched:** the manuscript, character-bible.md, STATE.yaml, foundation.md and outline.md. Nothing committed.
- **Validation:**
  - `yaml.safe_load` and a strict no-duplicate-key loader both pass.
  - All 386 ch-23 cites fall in p1..p157.
  - Every single-quoted Ch.23 fragment that was on the post-disruptor page but is gone from the final page now sits on a line marked CUT or RE-SYNC. Fragments on changed lines were checked against their cited paragraphs.
  - The file holds 357 characters, 111 locations, 162 objects, 20 organizations, 68 plot threads, 117 world rules, 234 timeline_events and 164 contradiction rows.
  - **54 open** (58 before; −4 CH23-1..CH23-4; none opened).

## 2026-10-23: UPDATE (chapter 24, "Lucius", post-disruptor page)

- **Page read:** chapter-24.md at 9d418b7 (writer c9b2f8e, dialogue-polish 48d48ed, hook-craft aee7909 with no edits, book-disruptor 9d418b7). md5 48ec2025cb7f481055c9d26c949bf6d7; working tree clean.
- **Numbering:** 235 paragraphs. Eight breaks (after p38, p67, p93, p117, p152, p183, p213 and p232) make nine shards. Each shard's italic time-stamp line counts as a paragraph, the same rule as the italic lines in Ch.2 and Ch.17. Those lines are p2, p39, p68, p94, p118, p153, p184, p214 and p233. The title, the dateline and the two HTML comments are not counted, so file line 8 = p1.
- **Not recorded (cut before this read):**
  - The lime on Valens's legs and arms, "The lime on him smelled of the kilns.", and the horn dust in his fingers. The one lime left is in his speech: "That arm's carried lime since dawn." (p38).
  - "For a breath, nothing." and "He cried." as a stand-alone line.
  - "Grata laughed and cried at once", "It was meant to be left open." and "He had taken him from me once the feeding was done".
  - Statia's "A boy." The page has her "Mas" (p157) and Grata's "A boy." (p158).
- **Recorded:**
  - **Lucius, born:**
    - A boy, born at cockcrow in Grata's back room, on Statia's stool, after labour from noon. The night runs in Roman hours: ninth, tenth and eleventh hour, lamp-lighting, bedtime, midnight, past midnight, cockcrow, after the cocks, first light, morning.
    - The hour was not marked: "Which cock?" / "All of them." (p206; p207).
    - Summer AD 74. The day is not on the page; derived as about late June to mid-August.
    - Physical: gray newborn eyes, dark hair in whorls, the open fontanelle.
    - What was done for him: the cord tied with red wool, the salt, the swaddling bands. Valens lifted him from the cloth on the floor. Mara nursed him at once, overruling Statia. Valens named him "Lucius" at first light; Grata wanted the naming on the ninth day.
  - **Statia** (`midwife-pompeii` renamed, `former_slug` kept):
    - Teeth: the two front teeth crossed, the left over the right, "like a pair of shears half shut"; a brown one beside them; a gap where the eyetooth should be.
    - She calls a girl five times ("Carried wide") and keeps insisting after the birth.
    - Her boy carries the stool. She speaks Oscan. She has the eagle-stone, and she wants the first milk withheld.
  - **Grata:**
    - Three children born in that house, the youngest feet first.
    - Her bargain with Juno Lucina: two cakes and a lamp, still owed (`gratas-vow-to-lucina`, chekhov_open).
    - She undoes the knots in the room, holds Mara on the stool and announces the birth to the street.
  - **Grata's husband:** first speech on the page under that name. He is "soft, sunburned", with dice and a lamp. He passes on the Chaldean rumour: "On the fish quay, behind the tunny sheds", "mutters gibberish to himself over it, not Greek, not Syrian", and reads your day "in Greek like a schoolmaster". He got it from his brother. He asks the birth hour.
  - **The fuller's wife:** she is "the twins' mother" by reading (needs_review kept). Her Cretan dittany. Grata held her leg "from one dawn to the next".
  - **Felix:** the lamp at the hooves, "four times", "Two years" (agrees with arrival in spring AD 72), asleep at the birth, horn in his hair.
  - **Valens and the dun:**
    - He pares and rasps all four of the dun's feet by lamplight. No shoe is mentioned (the world rule is now observed on the page). "There's a flare on this one."
    - He answers "Were you afraid?" with the mule.
    - At the birth: the cloth ("My man wears that to the Floralia" / "It's a cloth now."). He lifts the child on locked arms "how a man held a jar he had caught just short of the stones", then "by inches".
  - **Mrs. Dunphy, mutation 2:** a brown cardigan "gone thin at the elbows", "at the board with the chalk in her fingers", long division. Mutation 1 (Ch.7) was green, short of its second button, at her desk with her hands on the blotter.
  - **The Seiko:** wound by Valens on Mara's RIGHT wrist, forward until "the crown would go no farther". This agrees with Ch.18's wrist and Ch.6's rule. It is the third winding shown on the page with the watch on her own wrist (Ch.1, Ch.18, Ch.24). `last_mentioned_manuscript` is now ch-24:p235.
  - **The frozen peas:** bought for the back of the neck, never cooked "in four summers" (p91).
- **New entities:**
  - **Characters:** statia (renamed), statias-boy, statias-mother, vesuvius-gate-midwife, milk-girl-two-streets-over, forum-lamp-seller, fullers-twins, soranus, pliny-the-elder (needs_review against pliny-the-younger).
  - **Locations:** gratas-back-room (the room and the court: well, iron ring, woodstack, lane gate), nola-gate, vesuvius-gate, puteoli-fish-quay.
  - **Objects:** statias-birthing-stool, eagle-stone (chekhov_closed in-chapter), statias-knife, gratas-vow-to-lucina (chekhov_open), floralia-cloth, cretan-dittany (destroyed), maras-frozen-peas.
  - **knowledge_index:** lucius_birth. **plot_threads:** lucius-infant (OPENED). **world_rules:** six OBSERVED rows (birth customs, the father's lift and the ninth-day name, the Roman hours, hoof trimming).
- **Updated:**
  - Mara: physical `childbirth_ch24`, five traits, the teeth trait, the lucius and statia relationships, location_log 24, the Chaldean knowledge row taken from the page (`plan_was` kept), seven knowledge rows, knowledge_absent_ch24 and a waypoint.
  - Valens: physical `hands_ch24`, four traits, the lucius, statia and gratas-husband relationships, the mules and watch possession notes, location_log 24, five knowledge rows, knowledge_absent_ch24 and a waypoint.
  - Felix, Grata, Lucius, mrs-dunphy, gratas-husband, fullers-wife-pompeii and august-fenn (`ch24_rumor`; the alias now carries the page source, with the identification marked as the plan's).
  - Locations: gratas-thermopolium, cobblers-shop, pompeii (first naming of the Via dell'Abbondanza on the page; voice-dna allows it), puteoli, fullery-at-the-corner and pompeii-forum.
  - Timeline row 24 now uses the page (`plan_was` kept). Five timeline_events.
  - The fathers-seiko-watch custody, windings and wrist entries; relics-watch; the-when (`ch24_page`); conception-and-lucius.
- **Flags:**
  - **NEW:**
    - CH24-1 (info): outline wording against the page. The plan's "talks gibberish" is "mutters" on the page, and "amphora" is "jar". The plan has her asleep for the winding; the page has "mostly asleep", and she feels the hand on her wrist. The unshod hoof is implied, not stated. Forward: the Chaldean's fish quay against the Ch.25 plan's upper room by the harbor; compatible.
    - CH24-2 (low): Valens is back from the string at the eleventh hour in summer, having "carried lime since dawn". This runs against Ch.20's "In the hot months the carting stopped at noon" (ch-20:p85).
    - CH24-3 (info): Mrs. Dunphy mutation 2 changes more than the planned brown: the place, the cardigan's flaw, and what the class did. Long division is kept for Ch.41. The changes are by design.
  - **Rechecked, still open, with ch24_recheck notes:**
    - CH18-5: the child is a boy; his status is not raised.
    - CH19-3: the husband is on the page; the Ch.19 sleeping-tunic man is still his only by reading.
    - CH21-4: the first hoof work on the dun shown on any page, with no tie to the AD 72 letter.
  - **CLOSED (thread):** plot_threads.conception-and-lucius. The pregnancy timeline agrees end to end: conceived about late September to October AD 73, "Five. Nearly six." in mid-March, about seven months at the inn, born summer AD 74. No flag.
  - **CRITICAL:** none. **knowledge_gap:** none. Valens has the labour from Felix ("Felix said."). Felix's own source is the street and is not shown.
- **meta:** header note, `last_updated_by`, `mode`, `source` (Ch.1-24; the outline now covers Ch.25-44), `last_updated_chapter: 24`, `chapters_tracked` +24, the Ch.24 clause in `paragraph_rule`, and `ch24_requested_checks`.
- **Not touched:** the manuscript, character-bible.md (md5 unchanged), STATE.yaml, foundation.md and outline.md. Nothing committed.
- **Validation:**
  - `yaml.safe_load` and a strict no-duplicate-key loader both pass.
  - All 557 ch-24 cites fall in p1..p235.
  - Every single-quoted Ch.24 fragment on the added lines was checked by script against the page. The one misquote ("like a jar …") was corrected to the page's "how a man held a jar …". The other unmatched fragments are plan or other-chapter quotes.
  - The file holds 365 characters, 115 locations, 169 objects, 20 organizations, 69 plot threads, 123 world rules, 238 timeline_events and 167 contradiction rows.
  - **57 open** (54 before; +3 CH24-1..CH24-3; none closed).

## 2026-10-23: RE-SYNC (chapter 24, "Lucius", FINAL page)

- **Page read:** chapter-24.md at 8b2a8b2, md5 e4e8a96c4daf71d055fc0d823a6b363c. This is after the continuity repair 5a2c4a7 (CRIT-001..006, WARN-01..15, INFO-03/07/10/12, entity CH24-2; repair log in evaluations/continuity/chapter-24-audit.md), the evaluator fix set 8a7f7c6 (F1-F7) and the finalize FN1-FN3 (evaluations/chapter-24-eval.md). Working tree clean for the chapter.
- **Numbering:** 235 → 229 paragraphs.
  - Old p1..p139 = new p1..p139.
  - Old p140 and p141 are recast as one sound-only paragraph, new p140.
  - CUT: old p142-p144 (the stone at the thigh; "To the mule."; the husband snoring) and old p198-p199 (the cold lentils; "He lay wide").
  - Old p145..p197 = new p141..p193. Old p200..p235 = new p194..p229.
  - Breaks are now after p38, p67, p93, p117, p148, p179, p207 and p226. Stamp lines are p2, p39, p68, p94, p118, p149, p180, p208 and p227.
  - Renumbered by script: 557 explicit ch-24 cites, plus 284 bare Ch.24 refs (in the CH24-x blocks, in ch24_requested_checks, on Ch.24-only lines, and in the ch24_* fields of mixed lines).
  - By hand: the eagle-stone resolution paragraph (216 → 210) and lucius-infant.open_items.
  - History lines (header comments, the post-disruptor paragraph_rule clause) are left as they were.
- **Rewritten to the page:**
  - **The rival midwife:** now "There's one near the water tower," (p79). There is no gate on the page and no "Vesuvius" in the chapter.
    - `vesuvius-gate-midwife` is renamed `water-tower-midwife` (former_slug kept), and Statia's relationship key follows it.
    - NEW location `pompeii-water-tower`.
    - `vesuvius-gate` stays as a world entity, sourced only to outline:ch-19's "do not name a 'Vesuvius Gate'", with no Ch.24 cite.
    - Pompeii's Ch.24 fact drops the Via dell'Abbondanza and the Vesuvius Gate. The street is still unnamed on every page.
  - **The watch winding (p229):**
    - The page now reads: "It was Valens, on the bed beside me. The child slept against my left side. Valens had my hand palm down on his knee. He was working the watch's little crown a click at a time, and I felt each click in the small bones of my wrist. When it would turn no farther he tucked my hand under the sheet."
    - Rewritten from this: the windings row, the custody row, `wrist_ch24`, Valens's possession note, relics-watch, Lucius's `ch24_note` (against her left side, not on Valens's chest) and Valens's lucius relationship.
    - RIGHT wrist and the stop still agree.
  - **Valens's evening:** "Valens had the mules bedded by the eleventh hour." (p28). Updated: the Valens work trait, location_log 24 (the stalls) and timeline row 24.
  - **Carried:**
    - "For the boy." / "For the girl, then." (gratas-husband trait).
    - "Dice clicked in his fist".
    - The cord cut "beyond the tie" and "long bands of soft wool" (Lucius birth, Statia's craft, statias-knife, world rule).
    - "the aedile's men" (fuller's wife).
    - "twice your size" (statias-mother).
    - "In the Soranus I had read" (Mara's asides, soranus).
    - The fontanelle "Toward the brow" with no crown.
    - "I made a noise." and the legs "The shaking was back in my legs, and the stool rocked under me." (Mara's `childbirth_ch24`).
    - "burned where he was coming".
    - "his spine was all there".
    - The glue "had set in a brown run down the leg" / "I could have cleaned it off in an evening" (stool, Mara trait).
    - Grata "perched on the bed, her knees bracketing my back".
    - Grata's brazier "in the shop".
    - The dittany smoke without the flies.
    - Mrs. Dunphy's "the long division half written" (memory_ch24, mutations row).
  - **Marked CUT or removed as page facts:**
    - The Philadelphia reading room and the postcard.
    - "who wrote the book on midwives".
    - "horn in his hair".
    - The husband asleep across his counter (gratas-thermopolium, his trait).
    - "To the mule."
    - The stone knocking at her thigh.
    - The Oscan to the bag strap.
    - "He lay wide" / "I'm never wrong about wide" and "finished the lentils cold" (Statia).
    - "by inches" and "He did not move his feet at all."
    - "He cried at the ceiling."
    - The warm plaster and the party wall.
    - "told the dark".
- **Audit's suggested patches (applied where they match the page):**
  - Statia's teeth: three notes (p9; p132; p152).
  - The rival "near the water tower".
  - The dun's "She'll walk tender on the paving a day or two." (p222), added to the mules note.
  - The watch row.
  - Felix's horn CUT.
  - Grata's back room: brazier in the shop, loom p11.
  - Already present and matching p59: the Chaldean knowledge rows for gratas-husband and Mara, and lucius.
- **Flags:**
  - **CLOSED:** CH24-2. The page now has the mules bedded by the eleventh hour, not Valens back off the string. Against Ch.20's noon stop in the hot months (ch-20:p85) that leaves one value. "That arm's carried lime since dawn." (p38) fits a dawn-to-noon day.
  - **Rechecked, still open:**
    - CH24-1 (info). Every cited line stands. The winding is rebuilt but still has no "wind" or "forward", and she is "mostly asleep"; the other wording departures are unchanged.
    - CH24-3 (info), narrowed. The class clause is CUT ("the long division half written"). Colour, flaw and place still differ from Ch.7 by design.
  - **NEW:** CH24-4 (info). The winding's "a click at a time" to a stop (p229), against Ch.6's "the small loose click it gave when you went backward" (ch-06:p130) and Ch.1's forward "small dry ratchet" (ch-01:p191). This is compatible: only the forward turn has a stop (Ch.6's rule, ch-06:p305). Recorded, not judged.
  - **CRITICAL:** none. **knowledge_gap:** none.
- **meta:** header note, `last_updated_by`, `mode`, `source`, the Ch.24 RE-SYNC clause in `paragraph_rule`, a `revalidation_needed` chapter-24 row (RESOLVED) and a `ch24_requested_checks` re-sync row. The earlier Ch.24 check rows are annotated with RE-SYNC notes.
- **Not touched:** the manuscript, character-bible.md, STATE.yaml, foundation.md and outline.md. Nothing committed. The bible still says "the rival at the Vesuvius Gate" (character-bible.md l.4014, 4894, 4902). That belongs to the bible sync and was not edited here.
- **Validation:**
  - `yaml.safe_load` and a strict no-duplicate-key loader both pass.
  - All 558 ch-24 cites fall in p1..p229.
  - No CUT placeholder is left.
  - Every single-quoted Ch.24 fragment that was on the post-disruptor page but is gone from the final page now sits under a RE-SYNC/CUT note, or in a kept post-disruptor `prose` field beside its `prose_final`/`recheck_final`.
  - The quote-to-cite check leaves only pre-existing loose cites. No new mis-cite came from the renumbering.
  - The file holds 365 characters, 116 locations, 169 objects, 20 organizations, 69 plot threads, 123 world rules, 238 timeline_events and 168 contradiction rows.
  - **57 open** (57 before; −1 CH24-2, +1 CH24-4).

## 2026-10-23: UPDATE (chapter 25, "Augurinus", continuity-repaired page)

- **Page read:** drafted on chapter-25.md at 19f49c2 (writer 788e414, dialogue-polish f8c44dd, hook-craft 3c148dd with no edits, book-disruptor 19f49c2), md5 672814f406fcfe562a2f06832db5b221. The continuity repair 6b51af1 was committed mid-run (evaluations/continuity/chapter-25-audit.md). Every Ch.25 fact and quote was then re-anchored to the page as it now stands, md5 9fe39d862250573bc347e5caea6324c7.
- **Numbering:** 221 paragraphs, no breaks. The title, the italic dateline and the two HTML comments are not counted, so file line 8 = p1 and file line N = p(N/2 − 3). The repair changed text inside 33 paragraphs and added or cut none, so the numbers hold.
- **Not recorded (cut before this read, or by the repair):**
  - The Aegean quake "that winter" and "I hadn't, then." p129 now reads only "that's how the Corycian went for me."
  - "the boat over to Athens" (now "the plane").
  - "outside the Nuceria Gate" in Fenn's door line, and "by the Nuceria Gate" in the carter's story (now "a tomb outside the walls"). No gate is named in Ch.25.
  - "on a wall beside the Sacred Way" (now "at her own door").
  - Grata's naming of the pregnancy and "the news in me" at p157.
  - "with his sandals unlaced" (now "in the dark"), "flat as pavement", "pink to the collar of the robe", "It was a room for working in", "in capitals somebody had pressed hard into the cloth", "his pale eyes traveled my face", the three-part horoscope (now "A long life, under his own fig tree."), and "two coppers" at the close (now "My other copper").
  - The planned "dead Zippo", "star charts" and "one rainy afternoon" were never on the page (CH25-4).
- **Recorded:**
  - **August Fenn, in person (p16; named p48):**
    - Physical: "thin as a heron", the long face and white stubble, washed-out blue eyes, brows still black, the faded blue robe and gray felt cap, the ink-black nail, the left hand's steady tremor, "a bad hand", the light dry grip.
    - Voice: Greek "a schoolmaster's"; English "with the vowels in his nose", "wooder", and the 1960s idiom.
    - Aliases: "Augie, back home"; "Augurinus" (the joke, p48; p51); the Chaldean, now confirmed.
    - The room (NEW `fenns-upper-room`): up the outside stair "Behind the third shed", with the split third tread. Charcoal skies on whitewash, the red shake curve, tablets, the sand tray and rod, the star papyrus. On the sill the basil and the lighter. A mat rolled like a sailor's, two robes on a peg, a lamp with no stand, and the packed bag under dust.
    - The trade: a ship's hour for a captain who sails at dawn ("Dawn is propitious"), boys' triangles in a house on the hill, and horoscopes paid to a bathhouse keeper.
    - The story:
      - 22 July 1968: the new flashlight, kite twine tied at the slot's mouth, "the floor tipped", snow.
      - AD 41 at the thaw: Claudius, learned from a leek seller at Amphissa.
      - The Graves book "on the plane".
      - Father Kostas's Greek book.
      - Navy celestial navigation, 1952, "off Korea".
      - Two years in Phocis, then Italy.
      - The fleet's captains' stars at Misenum by 62.
      - Puteoli for eleven years (about AD 64, derived). This rests on the mooring-ring marks and the basil's eleven years.
    - "Thirty-four years" (p120) agrees with AD 41 to AD 75.
    - 62: "Sixty-two. February." Fever over a Misenum wineshop. The carter "Three days after" tells of a tomb "outside the walls" that "breathed cold", and a family on its bench felt it "till close to dawn". Fenn got there "four days" late, and it was shut.
    - The law: "One door with many mouths" (worded once). "It takes back the one it brought. It brought you, so it'll take you." This is use 1 of 3 of the allowlisted phrase, as a promise. Also "A night, tops, never days."
    - Others: "Beats me." / "I've always been on my own." / "No idea. Nobody knows".
    - The WHEN, word for word: "Late summer, seventy-nine." (p75).
    - The failed dates: spring 71, three nights on "Eros's bench"; "October, around the Ides" 73, rain on the second night. Then the tables "ran … backward" from the school year. "Vesuvius" is spoken once, by Fenn (p161). "the night the mountain opens" is compatible with the canon's night after.
    - Traits confirmed on the page: the sunk-cost wine, the coconut cream at Horn and Hardart, the 1964 Phillies, Connie Mack, "not another word" of news, never married ("You don't go buying furniture in a hotel"), the packed bag, courtly Greek to Valens, the notebook refused, the basil.
  - **Knowledge flow:**
    - **Mara:**
      - Knows: Augurinus = Fenn; the date; the law; hours, not days; others unknown; 71 and 73; the school-year rebuild; his road; Puteoli's breathing ground; that he never married; that his tables are "all on paper" (not seen, p162). Fenn knows the year too.
      - She was a mile from his bench on the second night of the 73 vigil (p158).
      - She keeps the dealer's name and the sister's name ("I had the name.", p188) and the stadium fire (p220).
      - She refuses the date: "I told him his arithmetic was wrong." (p221).
    - **Valens:**
      - Witnessed the English ("words with nothing in them that was Latin or Greek"). The flush and his mouth on Lucius's head show belief, but nobody declares it.
      - Asked "Does he know the door?" and was told "He knows it." (p144-p145).
      - knowledge_absent_ch25: everything said in English, including the date and the rules. The repair removed the gate name from Fenn's English (WARN-01).
    - **Fenn:**
      - Knows 1998, the Corycian, May; Philadelphia and Baltimore Avenue; her father dead (inferred); the 1980 Series; the 34 still a trolley; the 23 a bus; the automats closed.
      - Knows her husband and mules, her Pompeii address under Grata's name, and Lucius's hour.
      - Knows she has his notebook, from "a dealer on Antique Row, down on Pine" with the chart in a cigar box, bought at the Chestnut Hill estate sale in October '97. "He did not ask whose."
      - His sister's death is inferred. The page states only the not-asking and the hand.
      - Knows her tremor notes exist, not what they say.
    - "Margaret": 0 occurrences.
  - **Lucius:** "at eight months" on his father's forearm. "glared at the gulls". Nursed. Crawls with his bottom high, pulls up by Fenn's robe, eats and spits the sand, tries the rod in his ear, sleeps in the doorway. His stars are promised free with the letter.
  - **Valens:** tests the stair, then breaks the third tread coming up by twos. Moves the basil into the sun and gives the advice. Sets the wine cup down far from himself. "Will they be true?" "We should see to the mules." Eleven mule-loads of roof tile, paid in silver.
- **New entities:**
  - **Characters:** sea-captain-ch25, ships-boy-ch25, sprat-basket-boy-puteoli, puteoli-tile-builder, puteoli-octopus-seller, puteoli-bathhouse-keeper, neapolis-laundry-widow, serapis-priest, amphissa-leek-seller, misenum-carter, fenns-pupils.
  - **Locations:** fenns-upper-room; puteoli-hot-ground (needs_review: the Forum Vulcani / Solfatara by reading).
  - **Objects:**
    - potted-basil (chekhov_open; had been a possession reference with no object entry)
    - fenns-packed-bag (chekhov_open)
    - fenns-letters (chekhov_open, Ch.26)
    - lucius-horoscope (chekhov_open)
    - fenns-sand-tray, fenns-star-papyrus, fenns-terrible-wine, maras-two-coppers (all background)
    - maras-satchel (needs_review against the Ch.19-20 "bag")
  - **Organizations:** us-navy, philadelphia-phillies, horn-and-hardart.
  - **Thread:** the-refusal (OPENED p165-p175, p221; payoff Ch.36).
  - **World rules (OBSERVED):** a door opens when the ground moves hard; Puteoli's ground rises and sinks; Chaldean customs; the sailing season.
  - **timeline_events:** 1952, 1964, 22 July 1968, AD 40-41, AD 41-43, about AD 64, October 1980.
- **Updated:**
  - Rows that rested on outline:ch-25 are replaced with page cites, with `plan_was` kept where the page differs:
    - august-fenn: aliases, ch25_confirmed, first_appearance, physical (age_ch25, build, face, eyes, hair, clothing, hands, voice, movement), 20 traits, relationships (+7), possessions, location_log, knowledge rows (11 rewritten, 11 added), knowledge_absent and knowledge_absent_ch25, the waypoint.
    - mara-reyes: the "never says Margaret" trait confirmed, 5 traits, nursing_ch25, the Fenn relationship, the satchel and coppers, location_log 25, 9 knowledge rows rewritten and 5 added, knowledge_absent_ch25, the waypoint.
    - valens: the Fenn relationship, 5 traits, location_log 25, the belief row rewritten, 2 rows added, knowledge_absent_ch25, the waypoint.
    - lucius: age_ch25, hair_ch25, 3 traits, status_log, the Fenn relationship, location_log.
  - Notes added to pomponia-grata, gratas-husband, pat (the "wooder" memory), margaret-fenn (name_usage_ch25), irene-szabo, father-kostas, aulus-numisius-eros, pliny-the-younger and emilio-reyes.
  - Locations: puteoli, puteoli-fish-quay, nuceria-gate-tomb, misenum, neapolis, amphissa, vesuvius, corycian-cave, philadelphia, pompeii, cobblers-shop.
  - Timeline row 25 is rewritten to the page: a bright afternoon, `plan_was` "one rainy afternoon". Four timeline_events are rewritten.
  - Objects: fenns-zippo (introduced ch-25:p14; it is on the page only as "a cigarette lighter"), fenn-notebook (physical_ch25, location_ch25, last_mentioned_manuscript ch-25:p197), tremor-notes, fenn-tables (introduced_page ch-25:p161), venetian-map, phillies-cigar-box.
  - knowledge_index: door_location, door_when, mara_origin, eruption_foreknowledge, margaret_fenn, fenn_identity, tremor_notes_known, lucius_birth.
  - Threads:
    - the-when, can-others-pass, fenn-sisters-name and fenn-zippo are OPENED on the page; status set to open.
    - valens-belief is set to "paid (Ch.25), shown not declared".
    - New beats on fenn-cautionary-mirror, the-one-it-brought (use 1), the-door-and-the-choice, maras-secret and lucius-infant.
    - Rechecks on kalends-walks (no tomb from Valens) and maras-english-to-herself (no break).
  - World rules: OPENING RHYTHM, OPENING DURATION and the tremor-dates rule now carry page sources.
- **Flags:**
  - **Opened and CLOSED in this run.** Each was on the post-disruptor page and the continuity repair left only one value:
    - CH25-1 (low): "the boat over to Athens" against Ch.2's TWA. The page now says "plane".
    - CH25-2 (medium): Grata's naming of the pregnancy and "the news in me" put before the Ides of October 73. Ch.20-21 have it about 20 November. The page now gives only the mile and the rain.
    - CH25-3 (low): Theano's "Pompeii" given "on a wall beside the Sacred Way" against her doorstep in Ch.13-14. The page now says "at her own door".
  - **NEW, open (info):**
    - CH25-4: plan against page. The afternoon is fair, not rain. The lighter is not called a Zippo and not shown dead, so Ch.27 and Ch.35 will be the first pages to show it fails. The WHEN comes after about seventy paragraphs, not "within a minute".
    - CH25-5: Fenn is now told the tremor notes exist (p178-p180; p196). The index's "never" becomes "told of, not read". Ch.35's "reads only his front pages" still holds.
    - CH25-6: forward constraints for Ch.26. NARROWED: the repair patched outline Ch.26 beat 2 so the 1964 letter must not retell p65. What remains is that a 1997 World Series question follows "not another word".
    - CH25-7: the new "satchel" holds "everything that had crossed with me", but the watch was last on her wrist (Ch.24). The satchel is not merged with the Ch.19-20 bag.
  - **Rechecked, still open:**
    - CH24-1: its forward clause is now met, because the fish-quay rumour and the plan's upper room are the same room. The rest of the row is unchanged.
    - post_patch_flags P3: the page agrees with foundation, "since sixty-two" for the door and "Thirty-four years" working it out. The Ch.35 outline wording is unchanged.
  - **CRITICAL:** none. **knowledge_gap:** none.
- **meta:** header note, `last_updated_by`, `mode`, `source` (Ch.1-25; the outline now covers Ch.26-44), `last_updated_chapter: 25`, `chapters_tracked` +25, the Ch.25 clause in `paragraph_rule`, and `ch25_requested_checks`.
- **Not touched:** the manuscript, character-bible.md (md5 c63fb728a34c53cfcb02341bb0984443, unchanged), STATE.yaml, foundation.md and outline.md. Nothing committed.
- **Validation:**
  - `yaml.safe_load` and a strict no-duplicate-key loader both pass.
  - All 703 ch-25 cites fall in p1..p221.
  - Every single-quoted fragment on the added Ch.25 lines was checked by script against the repaired page. The fragments that do not match are plan, other-chapter or explicitly labelled post-disruptor quotes.
  - The file holds 376 characters, 118 locations, 178 objects, 23 organizations, 70 plot threads, 127 world rules, 245 timeline_events and 175 contradiction rows.
  - **61 open** (57 before; +7 CH25-1..CH25-7; −3 CH25-1..CH25-3 RESOLVED).

## 2026-10-23: RE-SYNC (chapter 25, "Augurinus", FINAL page)

- **Page read:** chapter-25.md at b69c374, md5 472a9dec950ad052597f723ef0aadc66. This is after the evaluator fix sets 4ec694d (F1-F11), 8ae9cbf (G1-G5, H1-H2), ad58bd2 (J1-J4, H3), bf56a37 (K1-K12, H4) and the header finalize b69c374 (cycle 4 PASS; evaluations/chapter-25-eval.md). The previous pass recorded the continuity-repaired page 6b51af1 (md5 9fe39d862250573bc347e5caea6324c7).
- **Numbering:** still 221 paragraphs, no breaks, none added or cut.
  - A script compared old and new paragraph by paragraph and confirmed old pN = new pN for all 221. No cite moved.
  - Text changed inside 29 paragraphs: p4, p14, p20, p26, p38, p45, p46, p98, p106, p109, p110, p113, p114, p115, p120, p127, p129, p131, p134, p136, p142, p146, p149, p152, p159, p161, p183, p188 and p210.
- **Rewritten to the page (the cut words marked CUT inline):**
  - "Where the hell'd you get to?" (p20). The comma form with "he told it" is CUT (F9). Rewritten in CH24-1's ch25_recheck, Fenn's ch25_confirmed, Mara's identity knowledge row and the lighter beat.
  - "In May. May of ninety-eight. Our ninety-eight." (p45). "Nineteen ninety-eight." and "without the nineteen" are CUT (F7). Rewritten in Fenn's knowledge row and knowledge_index.mara_origin.
  - Lucius "was busy with the gulls" (p4). "glared" is CUT (G4a).
  - The basil is "in a chipped pot" (p14). "mended with a lead staple" is CUT (F8), and so is "the cracked basil pot" (p115). Rewritten in Fenn's possessions and in potted-basil (description, physical).
  - **Valens's sill steps:** "At some point Valens passed behind my stool, saying nothing, took the basil pot off the sill…" (p115). "came two steps inside" and "returned to his post" are CUT (F1a/F1b). Rewritten in Valens's basil trait and the potted-basil beat.
  - **Valens and the child:** he "carried the roaring child out of reach of the tray" (p146). "took up his place in the door again" is CUT. He is in the doorway with Lucius asleep at p192, and p192 is added to the source of his father trait.
  - **Fenn's stool and table:** "He left the stool for his table." (p120). "He swiveled on the table toward Valens, who looked back." and the "The Pythia." echo are CUT (F5/J3). august-fenn.physical.movement now records the stool and table blocking (p81, p106, p114, p120).
  - **The copper:** it is taken (p98) and flicked back (p102). "He stood the copper on its edge and spun it…" is CUT (K6). Updated in the maras-two-coppers beat.
  - **The lighter:** the wave of it at his room is CUT ("He waved a hand at his room", p114), and so is "He looked at it and" (p127). The p114 cite is dropped from fenns-zippo (the beat and Fenn's possession row). p138 ("over his lighter") is added.
  - "I've got a feeling it's fair, that it owes me sixty-eight." (p131). "I figure it owes me sixty-eight." is CUT.
  - "I watched him not ask." (p188). The clause "He was pinning his own hand to the wood and not asking, and" is CUT. The hand "held it down hard" stays.
  - The satchel holds "everything else that had crossed with me through the cave" (p183, F11). Rewritten in Mara's possessions, fenn-notebook.location_ch25 and maras-satchel (description, review_note).
- **Checked, no YAML row to change:**
  - "in a Chaldean's robe" (p26) is now "dressed as a Chaldean". The robe itself is still on the page at p16. Fenn's distinguishing row is sourced to the foundation and is unchanged.
  - Also gone from the page and not quoted anywhere in the YAML: "swung round to the doorway" (p38), the hot springs and "Fenn stayed facing his wall" (p106, p109), "pause for breath" (p113), "Fenn talked straight through it" (p115), "He was away again." (p129), "came a pace off his post" (p134), "weighed the taste" (p136), "then turned to me" (p142), the "Mules." echo (p149), "anyhow" (p152), "He took that in." (p159), "shaking dice" (p161) and "for some while" (p210).
- **Flags:**
  - **CLOSED:** CH25-7. The page now says "everything else", which no longer claims the watch on her wrist (ch-24:p229), so one value is left. `prose_final` and a resolution are added. The satchel-versus-bag question was never a contradiction and stays as needs_review on maras-satchel.
  - **Rechecked, still open:**
    - CH25-4 (info). A `prose_final` and a `recheck_final` are added. The staple is gone and the lighter's wave is cut. The fair weather, the lighter that is never named a Zippo and never shown dead, and the WHEN at p75 all stand.
    - CH25-5 (info). p162, p178-p180, p184, p194 and p196 are unchanged.
    - CH25-6 (info). p57, p59, p60, p62 and p65 are unchanged. Part (b), the 1997 Series question, stands.
  - **NEW:** none. **CRITICAL:** none. **knowledge_gap:** none.
- **meta:** header note, `last_updated_by`, `mode`, `source`, a Ch.25 RE-SYNC clause in `paragraph_rule`, a `revalidation_needed` chapter-25 row (RESOLVED) and a `ch25_requested_checks` re-sync row.
- **Not touched:** the manuscript (md5 still 472a9dec…), character-bible.md, STATE.yaml, foundation.md and outline.md. Nothing committed.
- **Validation:**
  - `yaml.safe_load` and a strict no-duplicate-key loader both pass.
  - All 707 ch-25 cites fall in p1..p221.
  - Every single-quoted fragment in the file that was on the repaired page but is gone from the final page now sits under a RE-SYNC/CUT note, or in a kept earlier `prose`/`note` field beside its `prose_final`/`resolution`. The only other hits are short matches to fragments from other chapters.
  - The file holds 376 characters, 118 locations, 178 objects, 23 organizations, 70 plot threads, 127 world rules, 245 timeline_events and 175 contradiction rows.
  - **60 open** (61 before; −1 CH25-7).

## 2026-10-23: UPDATE (chapter 26, "Letters in English")

- **Page read:** drafted on the post-disruptor page 838ff54 (md5 772a42baf0e529e91ccdb81db9dc95a3), after writer 44b2d22, dialogue-polish 7f5c443, hook-craft 28df8d4 (no edits) and book-disruptor 838ff54. The continuity repair **387bad2 landed mid-run** (md5 9d42bd0cfffd9a3942f6e8507b0908e1; 6 CRIT and 17 WARN applied), so every Ch.26 row was **re-anchored to the repaired page**, which is the page as it now stands.
- **Numbering:** 115 paragraphs, seven breaks after p11, p20, p51, p57, p63, p83 and p96. Map from the post-disruptor page:
  - old p1..p63 = new p1..p63
  - old p64 ("She was out in the rain again …") is CUT
  - old p65..p91 = new p64..p90
  - new p91 ("Till autumn.") is ADDED
  - old p92..p115 = new p92..p115
  - Text changed inside 30 paragraphs (listed in `paragraph_rule`).
- **Note on commits:** the orchestrator's checkpoints e06f66b and 387bad2 swept up this run's YAML while it was still in progress (the post-disruptor draft). The working-tree file now differs from 387bad2 by the re-anchor. This run committed nothing.
- **Aelia:** the entry is rewritten from the plan to the page.
  - Three weeks old at the open (p5). The birth is not narrated. Derived birth: about December AD 75 to January AD 76, conceived about the Puteoli visit (p12) and "so big" at the vintage (p58). This agrees with foundation §10.
  - Eighth day: Grata hangs the bronze crescent on a red thread, with a prayer (p17). The page does not call it a naming.
  - Ages by section: 3 weeks, 4th week, 5th week, the next daybreak, 6th week, then about 7 to 8 weeks. The last two sections give no age.
  - Physical: black thatch; born with nails, a scratch down her nose; the wrist creases. Traits: greed confirmed on the page. Relationships, possessions, location and status rows added.
- **Fenn's six letters** are recorded one by one in `objects.fenns-letters.letters`, in order of arrival:
  - L1, spring AD 75: Lucius's stars; talked American all night; the tunny-salter's broom handle.
  - L2, the summer letter: the 1964 Sunday with his unnamed sister; first read at the vintage.
  - L3, at the vintage: "Sure, I said it … so sue me"; the 1997 question; his birthday and the melon.
  - L4, the birth letter: on a Puteoli wine shipper's spoiled horoscope; Aelia's stars; "near four the summer we go".
  - L5, nine days after her answer: wet, split nib; the voicemail rage.
  - L6, the tables' cover letter: the copyist boy; "P.S. … Your old man. I'm sorry."
  - Carriage is by the fish-sauce carter (new `letter-carter`). Grata's Herculaneum bench delayed one letter; the page does not say which.
- **Mara's replies** are a new object, `maras-letters-to-fenn`, R1-R4: the stair tread, fig and Grata, "nothing whatever about the door"; the birth note (implied); the 1997 answer with her father's voicemail; the ford, the strainer and Grata's son. The voicemail explanation is sponged out.
- **Knowledge flow:** new `knowledge_index.fenn_news_from_home`. In Ch.26 Fenn gets the 1997 result (asked for) and the word "voicemail" (unexplained, refused). Nothing else from 1968-1998. No knowledge_gap.
- **Valens:**
  - "goodnight" given (p51); said at daybreak to Grata and the dun (p53; p55). New thread `valens-english-word`, closed_by_design, with a no-recurrence constraint.
  - The jealousy is shown, never named (p29-p47; p72-p78).
  - The ford: "wet to the thigh" (p8); the dun swam the last of it (p82).
- **Lucius:** about 16 to 19 months (derived); walking. The knucklebone comes out of "my bags" (p20). He rolls it and loses it under the bed (p98). The named frame: "Don't move," (p111-p113).
- **Felix:** "seventeen that winter" (p85; agrees with AD 58); a new cut eyebrow; carries the box; the sea "Till autumn." (p91).
- **Grata:** has Aelia's stars "read out" (p4); the crescent; "My man reckons it's a curse" (p18). Secundus is named for the first time (p63).
- **Objects:**
  - **CLOSED:** `lucius-horoscope`, delivered with L1 (p14) and nailed up (p4).
  - Pentax: one frame. The counter is seen but not read out (p105).
  - Film: plan 12 shot / 24 left; page at least 11 / at most 25. The page confirms no frame since Ch.20 (p105).
  - Updated: knucklebone (last on the page at Ch.3 → p104), `fenn-tables` (the copy in a cedar box under the bedstead, unopened, p96), `fenn-notebook`, `tremor-notes` (in English, p16), `microcassette`, `maras-satchel`, `potted-fig-tree`, `roof-stair-tread`.
  - **NEW:** `aelias-horoscope`, `aelias-lunula`, `inn-strainer` (closed, "held … after a fashion"), `fenns-1964-scorecard`, `fenns-hall-table-note`, `maras-letters-to-fenn`.
- **NEW characters:** `letter-carter` (needs_review vs fish-sauce-carter), `fenns-copyist-boy`, `fenns-mother`, `fenns-downstairs-neighbor`, `bakers-son-candidate` (needs_review).
- **Updated characters:** mara-reyes, valens, august-fenn, lucius, aelia, felix, pomponia-grata, gratas-husband, secundus, margaret-fenn (the 1964 Sunday, the note; name_usage_ch26 = 0), fish-sauce-carter, fenns-pupils and emilio-reyes (alive in October 1997, the voicemail).
- **NEW organization:** `florida-marlins`. The Phillies entry gets the 27 September 1964 game.
- **NEW threads:** `aelia-infant`, `valens-english-word`. Ch.26 beats added to the-refusal, the-when, fenn-sisters-name, fenn-cautionary-mirror, secundus-election, lucius-infant, maras-english-to-herself (HELD) and the relics rows.
- **Locations:** cobblers-shop (the back room on the repaired page), gratas-back-room (both horoscopes above the loom), fenns-upper-room (the stair fixed), philadelphia (the 1964 route, the hall table), herculaneum, stabiae, nuceria, surrentum, fullery-at-the-corner, pompeii-forum, puteoli.
- **Timeline:** row 26 is rewritten to the page. Six timeline_events are added: 27 September 1964; Fenn's note, April 1968; 27 October 1997; and three for the letters in AD 75-76. The Aelia birth event is rewritten.
- **Flags:**
  - **RESOLVED:** CH25-6. The 1964 letter does not retell Ch.25, and the 1997 letter names its own breach (p59).
  - **Opened on the post-disruptor page and RESOLVED by the repair** (one value left):
    - CH26-1 (medium): the family sleeping upstairs over the shop, against Ch.19's back room.
    - CH26-3 (info): Grata reading Greek aloud.
    - CH26-5 (info): "the satchel since the Corycian".
    - CH26-8 (low): the fig frame dated about a year back. This was missed in the first draft and found by the audit's WARN-10.
  - **Open:**
    - CH26-2 (low): five mules against the four that crossed.
    - CH26-4 (info): Aelia "near four" against 3½.
    - CH26-6 (info): NARROWED. The lid is fixed on the page and outline Ch.27 now carries the invitation, but outline Ch.26's "Opens toward Ch.27" line is still unmet.
    - CH26-7 (info): Secundus's wall in winter AD 75-76 against the March AD 77 election.
  - **CRITICAL:** none. **knowledge_gap:** none.
- **meta:** header note, `last_updated_by`, `mode`, `source` (Ch.1-26; the outline now covers Ch.27-44), `last_updated_chapter: 26`, `chapters_tracked` +26, the Ch.26 clause in `paragraph_rule`, a `revalidation_needed` chapter-26 row (RESOLVED in this run) and `ch26_requested_checks`.
- **Not touched:** the manuscript (md5 9d42bd0c…), character-bible.md, STATE.yaml, foundation.md and outline.md. Nothing committed.
- **Validation:**
  - `yaml.safe_load` and a strict no-duplicate-key loader both pass.
  - All 667 ch-26 cites fall in p1..p115.
  - Every single-quoted fragment on the added lines was checked by script against the repaired page. The only misses are plan or report quotes, older YAML phrases, and post-disruptor wording that sits labelled in the CH26-n `prose` fields and the revalidation row.
  - The file holds 381 characters, 118 locations, 184 objects, 24 organizations, 72 plot threads, 127 world rules, 251 timeline_events and 183 contradiction rows.
  - **63 open** (60 before; −1 CH25-6; +4 CH26-2, CH26-4, CH26-6, CH26-7).

## 2026-10-24: RE-SYNC (chapter 26, "Letters in English", FINAL page)

- **Page:** the evaluator fix set G1-G18 (27 replacements, deb497c) and the header finalize (88dab54, cycle 1 PASS). md5 0ba7d411515cf0189ba905963b1681d1. The UPDATE had anchored on 387bad2 (md5 9d42bd0c…).
- **Paragraphs:** still 115, breaks unchanged (after p11, p20, p51, p57, p63, p83, p96). The script confirms old pN = new pN for all 115, so no cite moved. All 670 ch-26 cites fall in p1..p115.
- **Changed paragraphs (21):** p5, p6, p7, p8, p15, p28, p39, p51, p52, p57, p58, p59, p60, p61, p63, p67, p69, p83, p96, p98, p115.
- **Method:** every YAML line holding a 3- or 4-word run that is on 387bad2 but not on the FINAL page was found by script and rewritten to the page, with the cut words marked CUT. Labelled history was left alone: the CH26-n `prose`/`prose_repaired` fields and the 387bad2 revalidation row. Every newly quoted fragment was checked by script against the FINAL page; all match.
- **Facts rewritten to the page:**
  - The string: "four mules" (p52). A `ch26_note` is added to valens.possessions mules-and-horses.
  - The wall by the baths: "rooms to let right across the wall by the baths … that wall's my Secundus's" (p63). Mara writes "Grata's son's wall by the baths was letting rooms" (p83). The baker's son, "my boy's" and "painted out" are CUT. Updated in: mara's knowledge, Grata→Secundus, secundus.ch26_named, plot_threads.secundus-election, Fenn's knowledge and R4.
  - `bakers-son-candidate` is off the page. It is kept as a CUT marker (status, `last_confirmed`) and is a candidate for removal.
  - The shutter is "barred on the wind" (p7). "off the bay" is CUT.
  - Valens: "Only the baby woke him" (p8); Aelia "had fought him" (p39; "roared at" CUT). The word: "He tried it twice … and then its pieces ran together. After that he leaned down over Aelia and gave it to her." (p51). "At his first try / At the second / On the third", "very low" and "She went on sleeping through it" are CUT. She is asleep from p39.
  - Fenn L3: his birthday, "as of this letter that makes two of us who know it" (p59). "one person around here who knows it" is CUT. Updated in Fenn's trait, Mara's knowledge, the L3 row and the thread beat.
  - Fenn L5: "Skip it. I'll find out back there …" (p67). "Don't explain it to me, I mean it." and "like everybody's got one" are CUT. Updated in Fenn's trait and knowledge, Mara's knowledge, the L5 row and knowledge_index.fenn_news_from_home.
  - Mara R3: the strainer "that I did not think would take a patch" (p60). "fool the wine" and "The melon got no mention" are CUT; the page no longer says either way whether she mentions the melon.
  - Mara R4: "What a voicemail was, I did not explain." is CUT. The sponge-out of "It's a machine that" stays (p83).
  - The box: "I traded him the bone for it, and carried the box through" (p96). "took the box from him", "carried it through" and "Back in the shop, I gave him the bone." are CUT. Updated in Mara's traits, the knucklebone, fenn-tables, cobblers-shop and the requested-checks rows.
  - The close: "He sat on in the sun with his lip in her fist and both arms still round her, until his father lifted her away." (p115). "holding her very carefully" is CUT.
  - Aelia's voice row: "straight through to the initials" (p15).
- **Flags:**
  - **RESOLVED:**
    - CH26-2 (low): four mules on the page, the count that crossed (ch-19:p1). One value left.
    - CH26-7 (info): no notice for Secundus is on the wall and no election is named. Nothing runs ahead of March AD 77. One value left.
    - CH26-6 (info): superseded by the outline Ch.27 cascade, as instructed. Outline Ch.27 delivers the invitation in Ch.27 itself, and the eval's Ch.27 guard holds. Outline Ch.26 line 862 ("Opens toward Ch.27: Fenn invites her to Cumae.") is still in outline.md as text; it was not edited here. Forward constraint: Ch.27 must not say the invitation came by letter earlier.
  - **Rechecked, still open:** CH26-4 (info). p2 "near four" is unchanged, against foundation 3½.
  - **New:** none. **CRITICAL:** none. **knowledge_gap:** none.
- **meta:** header note, `last_updated` 2026-10-24, `last_updated_by`, `mode`, `source`, the Ch.26 FINAL clause in `paragraph_rule`, a new `revalidation_needed` chapter-26 row (RESOLVED) and a re-sync row in `ch26_requested_checks`.
- **Not touched:** chapter-26.md, character-bible.md, STATE.yaml, foundation.md and outline.md. Nothing committed.
- **Validation:**
  - `yaml.safe_load` and a strict no-duplicate-key loader both pass.
  - The file holds 381 characters, 118 locations, 184 objects, 24 organizations, 72 plot threads, 127 world rules, 251 timeline_events and 183 contradiction rows.
  - **60 open** (63 before; −3: CH26-2, CH26-6, CH26-7).

## 2026-10-24: UPDATE (chapter 27, "Cumae")

- **Page read:** drafted on the post-disruptor page 4a9ea52 (md5 cedb5f569b59282e603d7a92e70ccee2), after writer 5170211, dialogue-polish c454aa9 and hook-craft (no edits). The continuity repair **b2f1caa landed mid-run** (6 CRIT, 15 WARN; md5 b7d112dd7d6ba23fcfd6648b6ca99e42). It is the page as it now stands, so every Ch.27 row was **re-anchored to it**. The same repair changed one line of Ch.25 (p154), which is re-quoted below.
- **Numbering:**
  - 245 paragraphs, with breaks after p33, p113 and p195. The dateline and the two HTML comments are not counted, so file line 8 = p1.
  - The post-disruptor page had the same count and breaks, so old pN = new pN (checked by script).
  - The repair changed text inside 32 paragraphs, listed in `paragraph_rule`.
- **Not recorded:**
  - Report lines that are not on the page, e.g. "a little short of forty", "I could not laugh", "Thirty-five years gone", "in the dark, in forty-one".
  - Post-disruptor lines the repair cut. Where a flag needs one, it is marked CUT: "with the notebook in the pocket", "conservator for eleven years", the wick's "lamp oil for thirty years", the counter's "not a large number", the answering taps, "One month it's breathing", "every Kalends" at Cumae, the bath keeper's free horoscope, the nickel, "a deep shining bronze", and the bone in Lucius's fist on the way home.
- **The invitation:** made in person on the Puteoli fish wharf: "Then tomorrow you're mine, the three of you." … "We're taking a walk to Cumae." (p8). The letters only fixed the meeting: Mara's R5 and Fenn's one-line L7 (p4). The CH26-6 forward constraint holds.
- **Who went:**
  - Fenn, Mara, Lucius (about 20–22 months, derived) and Aelia (about 3–4 months, derived). Neither age is printed. Aelia is fed at the ridge crest (p114).
  - Valens is hauling brick to Misenum "for a villa going up on the cape" (p7). He is on the page only at the wharf, the carters' inn and the dawn yard (p15–p39).
  - Four mules: "the dun … the other three" (p15). The jenny was chosen by Valens: "She's sound … She bites. Not hard." (p35). She bites Fenn at Cumae (p127).
  - Fenn waits at the yard gate until the string has gone (p39).
- **Route:** Puteoli → the hot ground (scrapers, the hollow boom) → the oyster lake → Avernus (the ruined navy yard, the ducks, the meal on a quay block) → the ridge path → Cumae → the same road back to the last rise above Puteoli at lamp-lighting.
- **The Sibyl's cave (`sibyls-cave`):**
  - The trapezoidal entrance and gallery, cut tuff, side passages to the sky with slabs of light, a window passage over the sea, and the chamber with its bench, figures and coin crack.
  - The keeper (`cumae-cave-keeper`): bees, the pot lid, the swarm lost "for Misenum", "Two coppers each. Children for nothing".
  - The sailor (`cumae-fleet-sailor`) carving his name, "he had reached the third letter".
- **The dead door (`cumae-dead-door`):**
  - Location: a blind storage cut on the landward side, short of the chamber.
  - Fenn's X at shoulder height, "worn soft and dark by hands". He was "thirty-six", in the summer of AD 43, and found it from Virgil and a magazine picture.
  - Visited "the first of every month" for seven years; dead in "Spring of fifty"; "Warm like a wall's warm"; "It just quit."; then "Every month for a year", then yearly.
  - Dead: Mara's name "handed back off it" (p164).
  - Live: "like talking into a pillow", "hang a side of beef" (p165), "Like Eros's, only colder." (p167).
- **Fenn's crossing story:**
  - The coat, "gray Navy wool", slept in at the mouth for a week, then folded on the string rock "with my cigarettes in the pocket" (p192). He believes a goatherd took it (p194).
  - The carbon is in the notebook's back-cover pocket in Mara's satchel and is kept from him (p195).
  - This agrees with Ch.2 (the carbon's text and place, ch-02:p65–p67) and with Ch.3–5: nothing of Fenn's was found at the Corycian, and "I didn't see any string." Her kneeling entry matches ch-03:p73.
- **The Zippo:** named for the first time, "It was a Zippo." (p99). The sparks "fell on the wick and died" (p102). This is the named frame, shot at Avernus "while his thumb was still trying" (p105). The lamp-oil refill is not on the page.
- **Pentax and film:**
  - "My father's." (p92). Fenn refuses talk of it: "Not one word about it".
  - To Fenn, only "Some." frames left; the counter is not read on the repaired page.
  - The Lucius-and-ducks frame is not taken.
  - Film: plan 13 shot / 23 left; page at least 12 shot / at most 24 left.
- **The bone and the diamond:**
  - The bone comes out of the satchel and is thrown down the gallery; its clatter comes back from the blind passage.
  - The dust diamond: "You're Richie Allen." with the bone on third. Lucius stops on every bag. Fenn slides home.
  - The bone is last on the page in Lucius's two hands (p221).
- **The pie:** lemon meringue at Horn and Hardart (p58). "In his room, a year ago, it had been coconut cream. I let him have the lemon." (p59). This is the planned mutation.
- **The request:** "Write me … After the Kalends. Every one. Just that it's cold." / "And if it isn't?" / "It will be," (p242–p244). New thread `fenns-cold-reports` (open; no outline beat).
- **Ages:**
  - Fenn: "Sixty-nine in August, give or take a calendar." (p145) and "thirty-six" in AD 43 (p155). Years since landing are not printed (derived 35).
  - Mara: not on the page; derived about 38–39 in body years.
- **Felix:** not on the page and not named. The chapter ends above Puteoli before the return home. Forward constraint (felix.ch27_note, plot_threads.felix-arena): Ch.28 brings the news that he is missing.
- **NEW characters:** `cumae-cave-keeper`, `cumae-fleet-sailor`, `hot-ground-sulphur-scrapers`.
- **Updated characters:**
  - mara-reyes, valens, august-fenn, lucius and aelia: traits, physical rows, location_log, knowledge, knowledge_absent_ch27 and arc rows. The plan rows for Ch.27 were replaced with page rows, each keeping `plan_was`.
  - felix and pomponia-grata: a `ch27_note` each.
  - margaret-fenn: `name_usage_ch27` = 0.
  - puteoli-bathhouse-keeper (linked by place, not merged) and puteoli-octopus-seller.
- **NEW locations:** `puteoli-carters-inn`, `lucrine-lake` (needs_review), `lake-avernus`, `avernus-ridge-path`, `sibyls-cave`, `cumae-dead-door`, `ischia`.
- **Updated locations:** puteoli, puteoli-fish-quay, puteoli-hot-ground, neapolis, misenum, cumae (plus distances), corycian-cave, philadelphia.
- **NEW objects:** `cumae-jenny`, `gratas-cumae-honey`, `fenns-overcoat`.
- **Updated objects:** fathers-pentax-k1000, film-roll, corycian-knucklebone, fenn-notebook (provenance_ch27_note: not in the coat on the page), fenns-zippo, consulate-effects-slip, fenns-letters (L7), maras-letters-to-fenn (R5), maras-satchel, aelias-lunula, pompeii-painted-false-door (ch27_mention).
- **Knowledge:**
  - New `knowledge_index.cumae_dead_door`.
  - Rows added to maras_camera (august-fenn) and fenn_news_from_home (nothing after 1968).
  - Fenn learns that Valens was a gladiator at Corinth, Mara's Corycian cold, that she saw no string, and that she walks to Eros's door every Kalends and found it "cold" at the last one.
  - Fenn does not know that the coat went home (knowledge_absent_ch27).
  - No knowledge_gap.
- **Threads:** ch27 rows on fenn-cautionary-mirror, fenn-zippo, hand-at-threshold (HIS hand, written), kalends-walks, lucius-infant, aelia-infant, felix-arena, the-refusal (her night's hope of another door) and fenn-sisters-name ("my sister", 0 "Margaret").
- **World rules:**
  - Three OBSERVED rows: a door can die (live = cold and deaf; dead = warm and echoing; no shake felt); Fenn's comparison with Eros's; the Sibyl's cave as a paid sight.
  - A `ch27_page` note on the dormant-temperature ladder.
- **Organizations:** horn-and-hardart (lemon meringue), philadelphia-phillies (Richie Allen 1964), misenum-fleet.
- **Timeline:** row 27 rewritten to the page: spring AD 76, before the Ides, two days. Seven timeline_events added: about 1943; July 1968 (the coat); AD 41–43; summer AD 43; spring AD 50; AD 50–51 and after; spring AD 76.
- **Ch.25 re-quote:** p154 now reads "Cool paint, noon or midnight, and nothing." (the repair's CRIT-4). The one row that quoted the old line (nuceria-gate-tomb) is re-quoted with a RE-SYNC/CUT note. A `revalidation_needed` row is added for chapter 25 (RESOLVED).
- **Flags:**
  - **NEW, open:**
    - CH27-1 (medium): Eros's door is "cold" in AD 76 (p240), and "Like Eros's" is said of a door cold enough to hang beef in (p165–p167). This is against Ch.19's "faintly cool" / "only just cool" and the planned ladder (faintly cool to Ch.30, cold only at Ch.41). The brief's "breathed cold (Ch.19, Ch.25)" is the AD 62 opening night, not the dormant door. The repair aligned Ch.25 and left Ch.27.
    - CH27-2 (low): a week asleep at the mouth in the coat, against Ch.25's "I hiked up there first thing" (reconcilable if the week came earlier). Also, the coat is on the string rock by the slot, not certainly at "the cave mouth" as the outline says.
    - CH27-3 (info): Fenn asks how she went in, when she told him in Ch.25 (ch-25:p83).
    - CH27-4 (info): the August birthday puts him at 33 at the crossing and 67 at Ch.25, against the YAML's derived 34 and 68. Foundation §3 was patched to "33 when he crossed" but still says "aged 34" in the same sentence. A `conflict` sub-field (UNRESOLVED) is added on august-fenn.physical.age.
    - CH27-7 (info): outline Ch.27 vs the page. NARROWED by the repair's outline patch (the anchor now reads "waiting for it to turn cold"). Still standing: "rolls" against the throw, "cave mouth", and the unprinted thirty-five years.
  - **Opened on the post-disruptor page and RESOLVED by the repair:**
    - CH27-5: the notebook in the coat against the goatherd belief.
    - CH27-6: "conservator for eleven years" against ten.
    - CH27-8: the morning shadows "first up the track" against "the opposite direction".
  - **Rechecked:**
    - CH2-3: STILL OPEN. The post-disruptor page put the notebook in the coat pocket; the repair made it "my cigarettes". No page says the notebook came home in the coat, and the foundation still does.
    - CH25-4: NARROWED. The Zippo is now named and shown failing; the weather and the late WHEN still stand.
    - P3: rechecked against the Ch.27 road; still open.
  - **CRITICAL:** none. **knowledge_gap:** none.
- **meta:** header note, `last_updated_by`, `mode`, `source` (Ch.1–27; the outline now covers Ch.28–44), `last_updated_chapter: 27`, `chapters_tracked` +27, the Ch.27 clause in `paragraph_rule`, `revalidation_needed` rows for chapter 27 (mid-run repair) and chapter 25 (both RESOLVED), and `ch27_requested_checks`.
- **Not touched:** chapter-27.md (md5 b7d112dd…), chapter-25.md, character-bible.md, STATE.yaml, foundation.md and outline.md. Nothing committed.
- **Validation:**
  - `yaml.safe_load` and a strict no-duplicate-key loader both pass.
  - All 690 ch-27 cites fall in p1..p245.
  - Every single-quoted fragment on the added lines was checked by script against the repaired page. The only misses are plan, outline, foundation or report quotes, older YAML phrases on lines that gained a field, and post-disruptor wording that sits labelled as CUT.
  - The file holds 384 characters, 125 locations, 187 objects, 24 organizations, 73 plot threads, 130 world rules, 258 timeline_events and 191 contradiction rows.
  - **65 open** (60 before; +5: CH27-1, CH27-2, CH27-3, CH27-4, CH27-7).

## RE-SYNC — Chapter 27 "Cumae", to the FINAL page (2026-10-24)

- **Page:** FINAL page 5633635, md5 `0566b748489b2b0f136ecd2a312ec999` (cycle 4 PASS). Five edit rounds landed after the UPDATE anchored on the repaired page b2f1caa (md5 b7d112dd…):
  - bb5ab32: the evaluator's cycle-0 set, 104 replacements (F1–F6, C1–C18, P1–P8, E1–E67), plus X1 on Ch.25.
  - 2333ad5: D1–D7 and G1–G2.
  - 60db950: S1–S5 and S7–S12.
  - d158a09: T1–T2.
  - 5633635: the header finalize.
- **Renumbering:** 245 → 242 paragraphs. The map was built by script from the git copy of b2f1caa:
  - old p1–p67 = new p1–p67;
  - old p68–p69 CUT (F1, the replayed knees exchange);
  - old p70–p73 = new p68–p71;
  - old p74 CUT (C7, the fly on the jenny's neck);
  - old p75–p245 = new p72–p242.
  - Breaks are now after p33, p110 and p192. Text changed inside 88 paragraphs.
  - 672 cites moved: explicit `ch-27:pYY` cites, and bare refs on Ch.27 rows. On mixed rows, bare refs moved only inside ch27 fields. History rows were left alone.
  - Three rows cited a cut paragraph and were rewritten (the CH27-3 line, Mara's Corycian knowledge row, knowledge_index fenn_news_from_home).
  - CH25-4's three explicit Ch.27 cites were moved by hand.
- **Quotes:** a script found 83 single-quoted fragments that were on the repaired page and are off the final page. Each was re-quoted to the page or marked CUT. Changed to the page:
  - **Eros's door:** "Eros's is only cool," / "Eros's is a little one." (p163–p164); "Still cool?" / "It was cool on the last Kalends." (p236–p237); "Just that it's cool." (p239).
  - **The coat:** "sat at that mouth in it for hours" and "When I did go in" (p189); "you can bet on it" (p191).
  - **The cave:** the gallery windows are now on the LEFT-hand wall (p127); "short of the room" (p150); "as tall as a doorway" (p135); "a girl holding a jug, a woman with a child" (p148); "so soft a key would scratch it" (p126).
  - **Fenn's Philadelphia:** "At the automat" and the meringue "piled a mile high"; "Horn and Hardart" is cut, and "the automat" is already that entry's alias (p58). "it booms like the Spectrum when the Flyers score" (p52). "Like the Marlboro man." (p97). "He played third in sixty-four" (p204).
  - **Fenn's patter and speech:** "Step right up, ladies and gentlemen"; "That's the racket, kid."; "out of Virgil"; "the same cold" (the watch is cut); "He threw his hands out"; "on end"; "on the tuff"; "mornings"; "men built like that"; "whoever drew it".
  - **Other lines:** "up on top like a shaving brush" (the Jupiter callback is cut); "He shall ride." ("sir" stays at p19 and p24); "away up the Misenum road"; "since the corner"; "inside the rim of the hoof"; "everything I had carried into the Corycian"; "a night of it unanswered"; "There had been another one."; the keeper's sea-gaze and "with great bitterness" are cut; "Bone."; "from ahead and behind".
  - **Valens:** "Don't tell Valens about the slide." replaces "your mister".
- **Ch.25:** still 221 paragraphs (md5 `d2ceac85…`), so nothing renumbered.
  - p126 (l.258) is re-quoted in locations.nuceria-gate-tomb: "Cool under my hand with the sun on it, and not a breath out of it." The old "Warm in the sun, like everything else on that road." is marked CUT.
  - p154 (l.314), "Cool paint, noon or midnight, and nothing.", was already quoted correctly.
  - Two revalidation rows were added, for chapter 27 and chapter 25 (both RESOLVED).
- **Facts updated:**
  - august-fenn.physical.age resolved_from_conflict: 67 at Ch.25 and 68 at Ch.27, born August 1934, 33 at the crossing. The old value is kept under `previous`.
  - The coat timeline event is now 22 July 1968, "for hours".
  - fenns-cold-reports now reads "still cool". The slug is kept.
  - The dormant-temperature world rule now records agreement with Ch.19 and Ch.25.
  - Fenn's Philadelphia trait and fact rows now name the automat, the Spectrum and the Flyers.
  - The sibyls-cave rows are corrected (left-hand wall, doorway-tall window, figures).
- **Flags:**
  - **RESOLVED:**
    - CH27-1: Eros's door is cool on every page (Ch.19, Ch.25 p126 and p154, Ch.27 p163, p236 and p237).
    - CH27-2: hours, not a week, which fits Ch.25's "first thing". The which-mouth point moves to CH27-7.
    - CH27-3: the exchange is cut.
    - CH27-4: foundation §3 now says 33 at the crossing and "aged 33", which agrees with the page.
    - CH2-3: the page agrees with the patched foundation §3 Surface (cigarettes in the coat pocket; the notebook home among his effects via the consulate).
  - **Rechecked, still open:**
    - CH27-7 (info): "cave mouth", "rolls", and the unprinted thirty-five years.
    - CH25-4 (info): Ch.27 p33 is now "the same afternoon he first heard my voice", which agrees with Ch.25. The plan's "within a minute" and the rain still stand.
  - **NEW, open:**
    - CH27-9 (info): outline Ch.2 beat 7 (outline.md:166) and foundation §3 Wound (foundation.md:117) still say the notebook came home in the coat. Also, the only consulate carbon on any page lists only the overcoat.
    - CH27-10 (low, knowledge_gap): Fenn says "Valens" at p72 and p226, and no page shows him told the name. p72 was already on the repaired page and was missed by the UPDATE; p226 is new (S-fix). Added as august-fenn.knowledge_gap and a knowledge_index.valens_name row. The knowledge_absent_ch27 entry is rewritten, not deleted.
  - **CRITICAL:** none.
- **Open count:** 65 → **62** (5 closed, 2 opened).
- **Not touched:** chapter-27.md, chapter-25.md, character-bible.md, STATE.yaml, foundation.md and outline.md. Nothing committed.
- **Validation:**
  - `yaml.safe_load` and a strict no-duplicate-key loader both pass.
  - All 710 ch-27 cites fall in p1..p242.
  - 193 contradiction rows, 62 UNRESOLVED.
  - Every remaining off-page Ch.27 quote is labelled CUT, or is a plan or Ch.26 quote.
