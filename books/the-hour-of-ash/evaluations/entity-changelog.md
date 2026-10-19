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
