# Outline — *The Hour of Ash* (run 2, architect v4)

> Built from canon and `foundation.md`. Every chapter has a row in the Anti-Predictability Ledger,
> and **the Writer is prompted from that row**: structural approach, opening move, ending move,
> target words, dialogue band and theme. **Zero-tic ruling applies:** no beat below depends on a
> character's catchphrase landing. **NO FORESHADOWING applies:** the narrator's horizon is always the
> moment narrated (foundation §6a).

## Macro-Structure

**(a) Structure chosen: an UNEVEN DIPTYCH WITH AN ELASTIC CLOCK.**
- **Part One, *Where*** (Ch.1–18, ~41% of words): Philadelphia, 1998, then Phocis and Corinth, AD 70–72. The question is whether she can exist here at all, and where the way home is.
- **Part Two, *When*** (Ch.19–44, ~59%): Campania, AD 72–79. The question is when the door opens, and what she will do with the years until then.
- The hinge is a sea crossing and a ten-word wedding on the quay at Lechaion (Ch.18, ~41%). It sits deliberately off-centre.
- The eruption is **not a separate act.** It is the last compression of Part Two's clock. The chapters shorten from 8,000 words to 4,000, then 2,400, then 1,500 as story time collapses from years to hours to minutes.

**(b) Why this premise demands it.**
1. **The premise asks two questions in sequence, not three acts' worth of escalation.** The Oracle answers *where* and withholds *when*. Everything in Greece serves the first question; everything in Campania serves the second. A diptych states that plainly. The terms of the book change when she crosses the sea: from nonexistence and searching to belonging and waiting.
2. **The antagonist is a date.** Mara knows AD 79 from the moment Theano says "Pompeii." The tension is a known deadline approaching at a rate she refuses to calculate. The right structure is therefore a *clock whose speed changes*, not a staircase of confrontations. Part One moves in days and weeks (eighteen months over 18 chapters). Part Two's early chapters leap months and years, each with a **dateline**: she is counting, whether or not she admits it. From Ch.36 the clock tightens to weeks, then one day (Ch.38), then hours (Ch.39–41), then minutes (Ch.42–44). How fast the story moves through time *is* the theme: the visitor who thought she had time.
3. **Why not three acts:** the climax is not a confrontation that a midpoint reversal sets up. It is a choice at a door, prepared by nine years of living. **Why not the retired run's five movements and 36 chapters:** that shape was a slow-burn with movement labels and a retrospective narrator leaning forward. Here there is no retrospective frame, the hinge is a place-change, and pacing comes from clock elasticity and chapter-shape variety, not from movement boundaries. **Why not in-media-res or a frame:** canon requires the story told in order, ending in AD 79 with no modern coda.
4. **Part One has no datelines; Part Two has them.** In Greece she does not know the year until a herald tells her (Ch.5). In Campania she always knows. The headings (dateline from Ch.19: e.g. "Pompeii · AD 74") carry that change silently.

**(c) Turning-point map (jittered; none on 25/50/75).**
| Beat | Ch | ≈ % |
|---|---|---|
| The crossing (1998 → AD 70) | 3 | ~6.8 |
| The WHERE: Theano names Pompeii | 13 | ~30 |
| HINGE: wedding on the quay, sail for Italy | 18 | ~41 |
| Valens says his own name in the Basilica Julia (Celer resolved) | 22 | ~53 |
| The WHEN: Fenn says "late summer, seventy-nine," and Mara refuses it | 25 | ~60 |
| The fever: her want turns from going home to taking the children to the future | 32 | ~77 |
| The arithmetic, done at last | 36 | ~86 |
| The column rises | 39 | ~93 |
| The door opens for her alone | 42 | ~98 |
| The choice | 43 | ~99 |

**(d) Section labels.** Two reader-visible Part titles:
- **PART ONE · WHERE**
- **PART TWO · WHEN**

Chapter titles throughout. A **place-and-year dateline under each chapter title from Ch.19 onward only** (e.g. *Puteoli · spring, AD 72*). There are no act labels anywhere.

**(e) Chapter-count logic.** There are 44 chapters because the beats break that way. Part One's granularity is fine, because *existing* in AD 70 is made of discrete trials: a cave, a law, a rite, a letter, a fight, a prophecy. Part Two's early granularity is coarse, with long dated chapters that each carry a year. Its last nine chapters splinter, because the eruption is lived hour by hour. Seven chapters are short punches (1,500–3,400 words: Ch.4, 10, 14, 18, 30, 42, 44, plus 40–43 shortening). Fourteen are long and immersive (7,400–8,400 words). Length follows the beat. Nothing was computed as target ÷ count.

**Σ chapter targets = 260,300 ≥ manuscript_target_words (245,000) ✓**, a +6.2% margin. Hard floor 220,000: +40,300 of headroom. Longest 8,400 (Ch.19, 25) ÷ shortest 1,500 (Ch.44) = 5.6×. Length CV 0.34. Immersive peaks are capped near the ~7,000–8,500 range in which, per the author's length policy, they land naturally. No chapter should be padded to reach its number. If a chapter lands 10% short, the book still clears 245k only if the others hold. The orchestrator should track the running total against the cumulative targets in the ledger.

### Anti-Predictability Ledger

**Legend.** *Shape sig* = the signature `tools/shape_check.py` will compute from the finished chapter's first and last sentences:
- `I-statement`: the first sentence starts with "I" and has more than 8 words.
- `I-punch`: starts with "I", 8 words or fewer.
- `short-punch`: 8 words or fewer, not starting with "I".
- `long-spiral`: 28 words or more.
- `scene-set`: begins with a time opener ("It was", "That morning", "By dawn", "In the spring", "On the…", "Two days…").
- `dialogue`: begins or ends inside quotation marks.
- `narrative`: 9–27 words, none of the above.
- Endings: `punch` (7 words or fewer), `quiet` (8–24), `long-fade` (25+), `question`, `dialogue`.

**The Writer must hit the planned sig.** That alone makes the audit pass by construction.
- **Detector notes (from `tools/shape_check.py`):** a `scene-set` opener must begin with one of the detector's time openers: "It was", "That morning/night/…", "The morning/day/first/last/next…", "In the spring/…", "By the/then/morning/noon/evening/dawn/dusk", "On the first/second/third/fourth/fifth/morning/day/night", or "Two/Three… days/weeks/months/years". "On the seventh…", "On the nineteenth…" and "By first light…" do **not** match. Collage chapters that open on a document (Ch.2, 9, 20, 26) set it in *italics*, never in quotation marks, or it computes as `dialogue`. Ch.14 and Ch.40 open on a short first sentence *inside* a longer paragraph (they are not on the one-sentence-opening list).
- Opening sigs: no sig over 18% (short-punch 7, scene-set 7, dialogue 7, narrative 7, I-statement 6, long-spiral 6, I-punch 4), none three running.
- Ending sigs: quiet 27%, punch 23%, long-fade 20%, dialogue 20%, question 9%. None over 50%, none three running, punch well under 60%.
- **NO-PULL chapters (they simply stop, with no hook):** Ch.10, 31, 34, and 44 (the book's end).
- **Theme RECEDES:** Ch.4, 28, 31, 34.
- **One-sentence paragraphs:** an opening paragraph may be a single sentence ONLY in Ch.4, 24, 30, 36 and 42. A closing paragraph may be a single sentence ONLY in Ch.3, 9, 12, 18, 25, 30, 36, 39, 42 and 44. That is 5/44 and 10/44, well under the 50% one-liner reflex.
- **Scene breaks** vary from 0 to 9, with no four-in-a-row repeat. **Sentence gear** (low ≈ median 9–12 words, mid ≈ 14–16, high ≈ 17–20) varies so that the median sentence length is not flat across the book.
- **Approach counts:** Chronological 11 (25%), Single-scene 10, Collage 5, Fragmented 5, In medias res 5, Parallel 5, Essayistic 3. No approach appears in two consecutive chapters.

| Ch | Working title | Structural approach | Opening move → shape sig | Ending move → shape sig | Target words | Dialogue band | Theme | Scene breaks | Sentence gear |
|---|---|---|---|---|---|---|---|---|---|
| 1 | The Reception | Chronological | flat confession of a failure → `I-statement` | quiet image → `quiet` | 6,800 | 30–40% | present | 3 | mid |
| 2 | Fenn's Notebook | Collage | document (a Fenn notebook entry) → `narrative` | document fragment → `long-fade` | 4,200 | 10–20% | present | 6 | mid |
| 3 | Parnassus | Single-scene | long sensory spiral → `long-spiral` | action unfinished → `punch` | 5,600 (author trim 2026-10-19) | 5–15% | present | 0 | high |
| 4 | The Goats Saw Me First | Fragmented | flat statement of fact → `short-punch` | spoken line → `dialogue` | 1,700 | 15–25% | **RECEDES** | 7 | low |
| 5 | The Sanctuary | Chronological | scene-setting (time) → `scene-set` | long fade → `long-fade` | 8,300 | 20–30% | present | 4 | high |
| 6 | Snow at the Cave Mouth | In medias res | mid-action → `I-statement` | spoken line → `dialogue` | 7,200 | 35–45% | present | 2 | mid |
| 7 | The Laws of Belonging | Essayistic | claim/opinion → `narrative` | question → `question` | 6,600 | 20–30% | present | 3 | high |
| 8 | The Thyiades | Single-scene | mid-dialogue → `dialogue` | quiet image → `quiet` | 8,200 | 25–35% | present | 0 | mid |
| 9 | The Polygonal Wall | Collage | document (a Delphic manumission inscription) → `narrative` | short punch → `punch` | 6,400 | 25–35% | present | 5 | mid |
| 10 | Kallia's Letter | Single-scene | an object → `short-punch` | **PLAIN STOP (no pull)** → `quiet` | 2,800 | 30–40% | present | 0 | mid |
| 11 | Valens's Yard | Chronological | a sound (sensory spiral) → `long-spiral` | spoken line → `dialogue` | 6,200 | 35–45% | present | 3 | mid |
| 12 | The Kirrha Road | In medias res | mid-dialogue → `dialogue` | short punch → `punch` | 5,600 | 25–35% | present | 2 | low |
| 13 | The Seventh of Bysios | Parallel | scene-setting (date) → `scene-set` | spoken line → `dialogue` | 8,000 | 35–45% | present | 4 | mid |
| 14 | What Pompeii Means | Fragmented | flat statement (I) → `I-punch` | long fade → `long-fade` | 3,400 | 0–10% | present | 9 | low |
| 15 | Summer Pasture | Chronological | long sensory spiral → `long-spiral` | quiet image → `quiet` | 7,800 | 30–40% | present | 3 | high |
| 16 | Plautia | Parallel | mid-dialogue → `dialogue` | question → `question` | 7,600 | 40–50% | present | 6 | mid |
| 17 | Games on the Isthmus | In medias res | mid-action → `short-punch` | action unfinished → `quiet` | 7,400 | 30–40% | present | 3 | low |
| 18 | Lechaion | Single-scene | flat statement of fact (I) → `I-statement` | short punch → `punch` | 2,800 | 30–40% | present | 0 | mid |
| 19 | Puteoli | Chronological | scene-setting (place/time) → `scene-set` | long fade → `long-fade` | 8,400 | 20–30% | present | 4 | high |
| 20 | The Mender's Shop | Collage | document (a painted lost-property notice, 9–27 words) → `narrative` | spoken line → `dialogue` | 8,200 | 30–40% | present | 6 | mid |
| 21 | The Wolf's Old Name | Chronological | mid-dialogue → `dialogue` | question → `question` | 7,200 | 40–50% | present | 3 | mid |
| 22 | The Basilica Julia | Parallel | long sensory spiral → `long-spiral` | spoken line → `dialogue` | 7,600 | 35–45% | present | 7 | high |
| 23 | An Inn on the Appian Way | Single-scene | an object → `short-punch` | long fade → `long-fade` | 4,200 | 15–25% | present | 0 | low |
| 24 | Lucius | Fragmented | flat opinion (I) → `I-punch` | quiet image → `quiet` | 6,200 | 25–35% | present | 8 | low |
| 25 | Augurinus | Single-scene | scene-setting (place) → `scene-set` | short punch → `punch` | 8,400 | 45–55% | present | 0 | mid |
| 26 | Letters in English | Collage | document (Fenn's letter) → `narrative` | quiet image → `quiet` | 6,000 | 10–20% | present | 7 | mid |
| 27 | Cumae | Chronological | claim/opinion (I) → `I-statement` | long fade → `long-fade` | 7,600 | 35–45% | present | 3 | high |
| 28 | Felix in the Arena | In medias res | mid-action (crowd noise) → `short-punch` | spoken line → `dialogue` | 7,000 | 25–35% | **RECEDES** | 4 | low |
| 29 | Saturnalia | Essayistic | claim/opinion → `narrative` | quiet image → `quiet` | 6,600 | 35–45% | present | 3 | high |
| 30 | Tremor | Fragmented | flat statement (I) → `I-punch` | short punch → `punch` | 2,600 | 5–15% | present | 6 | low |
| 31 | Election Paint | Chronological | mid-dialogue → `dialogue` | **PLAIN STOP (no pull)** → `long-fade` | 4,800 | 40–55% | **RECEDES** | 2 | mid |
| 32 | Fever | Single-scene | scene-setting (time) → `scene-set` | quiet image → `quiet` | 7,800 | 15–25% | present | 0 | low |
| 33 | The Case for Penicillin | Essayistic | claim/opinion (I) → `I-statement` | question → `question` | 5,600 | 20–30% | present | 3 | high |
| 34 | Surrentum | Chronological | long sensory spiral → `long-spiral` | **PLAIN STOP (no pull)** → `quiet` | 7,600 | 30–40% | **RECEDES** | 3 | high |
| 35 | Fenn's Winter | Parallel | mid-dialogue → `dialogue` | document fragment → `long-fade` | 7,000 | 35–45% | present | 6 | mid |
| 36 | News of Vespasian | Collage | flat statement of fact → `short-punch` | short punch → `punch` | 4,400 | 15–25% | present | 5 | low |
| 37 | The Boat at the Sarno Mouth | Single-scene | flat statement (I) → `I-statement` | spoken line → `dialogue` | 6,400 | 50–60% | present | 0 | mid |
| 38 | Vinalia | Parallel | scene-setting (date) → `scene-set` | quiet image → `quiet` | 8,000 | 25–35% | present | 5 | high |
| 39 | Noon | In medias res | mid-dialogue → `dialogue` | short punch → `punch` | 4,000 | 20–30% | present | 3 | low |
| 40 | Pumice | Chronological | flat statement (I) → `I-punch` | long fade → `long-fade` | 5,800 | 15–25% | present | 4 | low |
| 41 | The Tomb Road | Single-scene | long sensory spiral → `long-spiral` | spoken line → `dialogue` | 4,200 | 30–40% | present | 0 | mid |
| 42 | The Door | Fragmented | flat statement of fact → `short-punch` | short punch → `punch` | 2,400 | 10–20% | present | 6 | low |
| 43 | What She Did | Single-scene | an object (narrative) → `narrative` | quiet image → `quiet` | 3,000 | 25–35% | present | 0 | low |
| 44 | Second Dawn | Chronological | scene-setting (time) → `scene-set` | **PLAIN STOP (the book ends)** → `punch` | 1,500 | 0–10% | present | 1 | low |

**Anti-default internal shapes.** No chapter runs establish → anomaly → escalate → close by default. Each chapter entry below names its **internal shape**. Chronological chapters in particular use named alternatives: *errand* (a task that goes sideways and is completed anyway), *day-in-full* (dawn to night, no crisis), *walk* (one journey, the scene changes as the road does), *two rooms* (alternating locations in one evening), *aftermath-first* (open after the event, never show the event), *slow reveal of a person* (each scene shows one more side of one character), *ritual* (a ceremony's own order dictates the structure).

---

# PART ONE · WHERE

## Chapter 1: The Reception
**Ledger:** Chronological (internal shape: *errand*) · open: flat confession of a failure → `I-statement` · end: quiet image → `quiet` · 6,800 · dialogue 30–40% · theme present · 3 breaks · gear mid
*(Philadelphia, March 1998. No dateline in Part One.)*

**Premise:** Mara walks out of her father's memorial reception to look at antiques, buys a map she shouldn't, and goes home to his answering machine.
**Function in arc:** Establish the voice, the wound (the father who always left for the past), the lie (the packed bag) and the inciting objects: the map, Fenn's notebook, the microcassette, the watch and the camera.
**Emotional anchor:** her father's recorded voice on the outgoing message, which she plays three times and cannot erase.
**Emotional surprise:** at the memorial she is irritated, by the lemon cake, by a colleague's eulogy about "Emilio's generosity with his time." She is not grief-struck. She leaves to go shopping.
**Opening strategy:** **The failure** (foundation §8). First sentence: Mara leaving the reception forty minutes in, cake in her pocket. It must be an `I-statement` of more than 8 words.
**Key scenes/beats:**
1. **NON-NEGOTIABLE.** The reception, in the museum's upper gallery: casseroles of condolence, a dig colleague's sunburned eulogy, Mara watching the room the way she watches a cracked pot. She leaves.
2. **NON-NEGOTIABLE.** Pine Street in sleet; Szabo's shop. **Irene Szabo** is seventies, Hungarian, brisk and unsentimental. The map is a Venetian chart of the Gulf of Corinth and Phocis from the 1680s, with modern ink coordinates on Parnassus, "BIBLIOTHECA?" and a little drawn doorway. It came with a cigar box holding a notebook. Szabo bought the lot at Margaret Fenn's estate sale in Chestnut Hill: "Her brother. Treasure hunter. Went to Greece in sixty-eight and didn't come back." She bought it only because the coastline is *right* for its period, not a fake. Haggling. Mara writes a check she can't really afford.
3. **FLEX.** Back to the reception for her coat; a cousin's look.
4. **NON-NEGOTIABLE.** Her father's rowhouse, near dark. The answering machine blinks: condolences, then **Prof. Halloran** from Naples about "Emilio's permit for the Campanian survey season" and whether "the family" will send anyone. Then her father's outgoing message, his voice. She ejects the microcassette and keeps it. The 1966 Seiko on his nightstand, stopped; she winds it. The Pentax on the shelf.
**Progressive structure:**
- Builds on: (opening chapter).
- Adds: who Emilio was through his objects, and that Mara does what he did (walks out toward the past).
- Opens toward Ch.2: the notebook unread on the kitchen table.
**Theme presence:** the visitor's life. A daughter of a man who always left, leaving.
**Character chaos moments:** the all-or-nothing distortion: she can't stay "a little" at the reception, so she goes. (No teeth here: the teeth schedule is Ch.2, 5, 7, 15, 20, 24, 31 only.)
**Device presence:** none.
**Subtext layer:** Mara and Szabo appear to be haggling over a map. Underneath, Szabo is asking whether this woman is a dealer or a mourner, and Mara is refusing to say.
**Shareable moment:** none designed.
**Reading speed:** fast in the reception (short observations), slow in the shop (material spiral over the chart's paper and ink), very slow at the machine.
**Word count target:** 6,800
**Writer warnings:** Do not explain the father; let the casseroles, the watch and the voice do it. No define-by-negation opener ("It wasn't grief. It wasn't..."). No closing aphorism about the dead; the ledger ends on a quiet *image* of the machine's light. Szabo must not deliver a warning or a destiny line. NO forward-gestures of any kind: Mara does not know she will go anywhere. Watch the em-dash budget (≤4).
**Beat subversion:** *Genre beat:* the mysterious shopkeeper hands the heroine a destined artifact with a warning. *Subversion:* Szabo wants it off her shelves, haggles hard, and the only uncanny fact about the map is that it is accurate.

## Chapter 2: Fenn's Notebook
**Ledger:** Collage (internal shape: *notebook against days*) · open: document (a Fenn notebook entry) → `narrative` · end: document fragment → `long-fade` · 4,200 · dialogue 10–20% · theme present · 6 breaks · gear mid
*(Philadelphia, March–May 1998.)*

**Premise:** Over eight weeks Mara reads a vanished man's notebook against her own ordinary days, and decides to go to Greece.
**Function in arc:** Introduce Fenn's voice and the legend, give her a concrete plan, and pack the relics. Plant Halloran's Campanian invitation without letting it point anywhere.
**Emotional anchor:** Fenn's handwriting going from confident capitals to small, tired script across the notebook's pages.
**Emotional surprise:** Halloran's call about her father's permit forms makes her laugh: the bureaucracy of the dead is the funniest thing she has heard in months.
**Opening strategy:** bridge by **document**. An entry from 1967 in Fenn's boyish voice. **No numbered or listed format** (zero-tic ruling).
**Key scenes/beats:**
1. **NON-NEGOTIABLE (document, REVEAL).** Fenn's theory: a Byzantine scholiast's marginal note that Ptolemaic scrolls were carried to "the cave of the nymphs on Parnassus." His coordinates.
2. Mara's lab: she rejoins a Roman lamp's nozzle with an invisible seam. Professional pride.
3. **NON-NEGOTIABLE (document, REVEAL).** Fenn, 1968: "I put my hand in at the back and the air was cold in a way air isn't." The handwriting has changed.
4. A phone call with Halloran. He invites her to Campania for July "in Emilio's place." She says she might be in Greece first. **Neutral, with no portent.**
5. **FLEX.** Her father's field notebooks in his study; she does not open them.
6. **NON-NEGOTIABLE.** Packing: the Pentax with a fresh roll, the Seiko on her wrist, the microcassette in a sock, Fenn's notebook (half its pages still blank at the back), a flashlight, granola bars, ibuprofen, her toothbrush and floss. The chart stays pinned over her father's desk; the coordinates are in the notebook. (No flash unit: the K1000 has none.)
7. **(document, REVEAL, one line).** Folded inside the back cover, the US consulate's slip from Athens, 1968: personal effects of Fenn, August J., forwarded to next of kin. One line of provenance: the notebook came home in his coat, without him.
8. **NON-NEGOTIABLE (end document).** Fenn's last entry, July 1968, cheerful: back before Labor Day, Margaret can stop telling people he's in Mexico.
**Progressive structure:**
- Builds on Ch.1: the notebook from the cigar box is opened.
- Adds: the cave, the cold air, and Fenn as a voice and a person.
- Opens toward Ch.3: the flight; the plateau.
**Theme presence:** Fenn and Emilio as two men who left. She is packing to do the same.
**Character chaos moments:** teeth (floss packed before passport). Mrs. Dunphy does not appear yet.
**Device presence:** documents inside a collage. Each must reveal something the narrative does not.
**Subtext layer:** Halloran is asking about permits. Underneath, he is asking whether anyone will carry Emilio's work. Mara hears it and dodges.
**Shareable moment:** —
**Reading speed:** documents brisk, days slow and textural, the packing quick.
**Word count target:** 4,200
**Writer warnings:** Fenn's documents must NOT enumerate ("First... second..."); his mind for patterns shows in content only. Halloran's Campania must stay a neutral fact: no narratorial weight, and no "if I had gone to Italy instead." Don't let the ending document read as a scene button. It is a plain, cheerful line from 1968, and the reader supplies the irony.
**Beat subversion:** *Genre beat:* the heroine deciphers a cryptic code to unlock the quest. *Subversion:* nothing is cryptic. Fenn wrote the coordinates plainly. The obstacle is her own decision, and she makes it while flossing.

## Chapter 3: Parnassus
**Ledger:** Single-scene (internal shape: *walk → threshold*) · open: long sensory spiral → `long-spiral` · end: action unfinished → `punch` · 5,600 (author trim 2026-10-19) · dialogue 5–15% · theme present · 0 breaks · gear high
*(Greece, May 1998.)*

**Premise:** Mara climbs from the Kalivia plateau to the Corycian Cave, follows Fenn's coordinates into its cold back recess, and walks out into the wrong season.
**Function in arc:** The crossing. Point of no return, rendered as sensation and embarrassment rather than spectacle.
**Emotional anchor:** the knucklebone she pockets from the cave floor. It is a conservator's sin, and she knows it.
**Emotional surprise:** at the moment of crossing she feels *embarrassed*, as if she has walked into the wrong room at a party.
**Opening strategy:** a single 28-word-plus sentence of plateau: thyme, goat bells, the wind, the road far below.
**Key scenes/beats:**
1. The path up from the plateau. A German hiker passes, the only speech of the chapter apart from a goatherd's "kalimera." She takes photographs. The exposure counter on the Pentax reads 9 (eight frames shot; on a K1000 the counter shows the next frame), and that number is not mentioned.
2. **NON-NEGOTIABLE.** The cave: the vast first chamber, stalagmites, tourist graffiti, the cold. She finds a stray knucklebone in the dirt and pockets it.
3. **NON-NEGOTIABLE.** The back recess by Fenn's coordinates. A **hand at a threshold**: cold air on her palm, the sound of the world thinning to nothing. She steps in. A long continuous sentence, then the change.
4. **NON-NEGOTIABLE.** Walking back out of the mouth: the light is lower and gold, the air smells of woodsmoke and dung, and the trail's paint blaze is gone. Final line: she steps out into the wrong season (≤7 words, a single-sentence closing paragraph).
**Progressive structure:**
- Builds on Ch.2: Fenn's "cold in a way air isn't" made physical.
- Adds: the door is real.
- Opens toward Ch.4: the plateau, changed.
**Theme presence:** a woman walking deliberately into the past.
**Character chaos moments:** all-or-nothing (she won't turn back at the cold: "properly or not at all").
**Device presence:** none.
**Subtext layer:** —
**Reading speed:** slow and sensory all the way up; one long held sentence at the threshold; then fast, short sentences outside.
**Word count target:** 5,600 (author trim 2026-10-19; was 6,800)
**Writer warnings:** No portent before the cave ("something waited for me"). No voices, glow or special effects; the door is cold and silent, nothing more. No "I didn't know it then"; she doesn't. Avoid analytical simile at the crossing; prefer one characterizing comparison or none.
**Beat subversion:** *Genre beat:* the portal opens in a blaze of light and terror. *Subversion:* it is cold, quiet and socially awkward. She notices the change only by the color of the light and a missing paint mark.

## Chapter 4: The Goats Saw Me First
**Ledger:** Fragmented (internal shape: *shards of one hour*) · open: flat statement of fact → `short-punch` · end: spoken line → `dialogue` · 1,700 · dialogue 15–25% · **theme RECEDES** · 7 breaks · gear low
*(Parnassus, autumn, AD 70, though she does not know the year.)*

**Premise:** Her first hour in the past is a goatherd boy, a stone hut, a language she can read but not hear, and terrible hunger.
**Function in arc:** A short structural shock after the long crossing. Survival, before meaning.
**Emotional anchor:** the boy's word for her, which she can spell in her head but cannot hear as Greek until the third try.
**Emotional surprise:** what overwhelms her is hunger, not wonder.
**Opening strategy:** "The goats saw me first." This opening paragraph may be a single sentence.
**Key scenes/beats:**
1. Goats; a boy of about nine; staring.
2. Her Attic Greek against his Phocian dialect: farce.
3. A granola bar split with the boy. He spits it out.
4. The refuge hut is now a shepherd's stone pen. No road. No pylons.
5. **NON-NEGOTIABLE.** The boy says *nymphē*, which is nymph, bride and young woman at once, because she came out of the nymphs' cave. The chapter ends on his spoken line.
**Progressive structure:**
- Builds on Ch.3: the wrong season, confirmed.
- Adds: the language barrier is real; her book Greek is a liability.
- Opens toward Ch.5: he points her down the mountain.
**Theme presence:** **RECEDES.** Body and survival only.
**Character chaos moments:** none forced; the hunger is the chaos (teeth are not used here, see Ch.1 note).
**Subtext layer:** the boy is asking whether she is a goddess or trouble. She is trying to ask what year it is.
**Shareable moment:** —
**Reading speed:** fast throughout.
**Word count target:** 1,700
**Writer warnings:** Do not date the year here; that is Ch.5's beat. No anaphora triads in the fragments ("No road. No wires. No sound."); vary the syntax. Keep it under 2,000 words.
**Beat subversion:** *Genre beat:* the awestruck arrival and her first vision of the ancient world. *Subversion:* she sees goats and a pen, eats a granola bar, and is mistaken for a minor goddess by a child who doesn't like her snack.

## Chapter 5: The Sanctuary
**Ledger:** Chronological (internal shape: *walk*, the city changing as the road does) · open: scene-setting (time) → `scene-set` · end: long fade → `long-fade` · 8,300 · dialogue 20–30% · theme present · 4 breaks · gear high

**Premise:** Mara walks down into Delphi, finds the sanctuary whole and painted, learns the year from a herald, and is taken in, as labor, by a widow at the Castalian spring.
**Function in arc:** Land the premise, establish her legal nonexistence (the Part One engine) and immerse the reader (Dimension 7).
**Emotional anchor:** the temple of Apollo *painted*: red, blue and gilt. To a woman who loved the white ruin it looks ugly.
**Emotional surprise:** the living sanctuary disappoints her, and she is ashamed of being disappointed.
**Opening strategy:** bridge by **time**: "It was most of a day down the mountain…" (a time opener, so the sig is `scene-set`).
**Key scenes/beats:**
1. The descent through terraces and olive-pressing season to the sanctuary.
2. **NON-NEGOTIABLE.** The Sacred Way: crowds, hawkers, treasuries, painted statues, and **empty statue bases**, because Nero carried off hundreds three years earlier. The conservator in her notices the fresh pry-marks.
3. Seized on the temple steps as a madwoman or runaway (jeans, fleece). A temple slave beats her off with a rod.
4. **NON-NEGOTIABLE.** A herald in the agora: Titus has taken Jerusalem. She does the history in her head. **AD 70. Vespasian.** It is a present realization, not foreknowledge, and there is no reference to 79 yet.
5. **NON-NEGOTIABLE.** Night at the Castalian spring. **Kallia** finds her washing her face, inspects her hands (soft, useless) and her teeth, and takes her home as unpaid help, not out of kindness.
6. The storeroom. The Seiko ticking. She touches the microcassette in its sock without comment.
**Progressive structure:**
- Builds on Ch.4: she followed the boy's pointing.
- Adds: the exact year, the political moment, and the fact that a woman alone has no status.
- Opens toward Ch.6: she means to go back up to the cave.
**Theme presence:** the past she loved as a ruin, living and indifferent.
**Character chaos moments:** teeth (Kallia inspects *hers*, a reversal). All-or-nothing (she refuses to speak Greek after being laughed at).
**Subtext layer:** Kallia asks practical questions (can you carry water, can you card wool). Underneath, she is asking whether Mara is a runaway who will bring trouble to her door.
**Shareable moment:** —
**Reading speed:** decelerate on the Sacred Way (dense, sensory); accelerate on the steps and the beating; slow fade in the storeroom.
**Word count target:** 8,300
**Writer warnings:** Do not tour-guide. Every period detail must be something Mara *uses or suffers*. When she dates the year, she must not jump to "nine years until the mountain"; she has no reason to think of Pompeii yet. Keep harshness at about 7: the beating is brief and real, not lingered on. End on a long fade, not an aphorism about time.
**Beat subversion:** *Genre beat:* the wonder-struck first look at the ancient city. *Subversion:* it disappoints her. Her first real wonder is the stolen statues' empty bases, the past already looted.

## Chapter 6: Snow at the Cave Mouth
**Ledger:** In medias res (internal shape: *crisis → backfill → after*) · open: mid-action → `I-statement` · end: spoken line → `dialogue` · 7,200 · dialogue 35–45% · theme present · 2 breaks · gear mid
*(Parnassus, November, AD 70.)*

**Premise:** Mara pays a scarred muleteer with her father's watch to take her up to the cave in snow, and the cave is only a cave.
**Function in arc:** Close her first hope (the door she came by is shut), and give the leads their first two-hander.
**Emotional anchor:** Valens winding her father's watch the wrong way, carefully, with a thumb too big for the crown.
**Emotional surprise:** she hits the cave wall and Valens laughs, kindly, because it's the first honest thing she has done in front of him.
**Opening strategy:** mid-action: on her knees in the back recess, scraping at frozen earth. The first sentence starts with "I" and runs more than 8 words.
**Key scenes/beats:**
1. In the recess: digging, with no cold seam, just cold.
2. **Backfill (NON-NEGOTIABLE).** Valens delivering firewood to Kallia's lodging. She asks to be taken up; he refuses (snow, money, her). She offers the Seiko. He examines it like a horse's teeth and winds it backward until she stops him.
3. The climb: his mules, his silence, footing, weather.
4. **NON-NEGOTIABLE.** Back to the present: she hits the wall and screams. He laughs. He doesn't comfort her; he gives her bread.
5. The descent in falling snow. He keeps the watch, because that was the deal.
**Progressive structure:**
- Builds on Ch.5: she meant to go back up.
- Adds: the door is shut, Valens exists, and he holds her father's watch.
- Opens toward Ch.7: she has to learn to *live* here.
**Theme presence:** the way back denied.
**Character chaos moments:** Mara's failed emotional management (the scream at the wall). Valens's mind-reading (he assumes she's a runaway noblewoman who will get him killed).
**Subtext layer:** they appear to argue about snow and payment. Underneath, she is asking for someone to believe her without saying what, and he is refusing to be the one who gets involved.
**Shareable moment:** —
**Reading speed:** the opening is fast, the backfill measured, the cave break short and hard, the descent slow.
**Word count target:** 7,200
**Writer warnings:** Valens's distinctness lives in syntax and attention (footing, weather, the mules), not a catchphrase or a fixed gesture. No "meet-cute" banter. Don't make the watch a symbol in prose; he is a man who likes a well-made object. No romance signals in narration.
**Beat subversion:** *Genre beat:* the rugged hero rescues the stranded heroine on the mountain. *Subversion:* there is no rescue. He is a hired hauler who charges her and keeps the fee, and the event is her failure and his laugh.

## Chapter 7: The Laws of Belonging
**Ledger:** Essayistic (internal shape: *claim → evidence → cost*) · open: claim/opinion → `narrative` · end: question → `question` · 6,600 · dialogue 20–30% · theme present · 3 breaks · gear high
*(Delphi, winter, AD 70–71.)*

**Premise:** Through one winter Mara learns that in Phocis a woman exists only as somebody's, and becomes Kallia's.
**Function in arc:** Make the Greece-first obstacle concrete: she needs a guardian, a name, a story and clothes before she can do anything.
**Emotional anchor:** a borrowed wool himation that smells of the woman who wore it before her.
**Emotional surprise:** the worst humiliation, being registered as Kallia's dependent kinswoman "from Syracuse," lands as *relief*. At last she is somebody's.
**Opening strategy:** a claim. A woman in Phocis in the second year of Vespasian belonged to someone (9–27 words, so `narrative`).
**Key scenes/beats:**
1. Claim → evidence: the bathhouse women's hours; the public latrine; Kallia's fierce lessons in how to walk, sit and not meet a man's eyes.
2. **NON-NEGOTIABLE.** The council's clerk (Sosandros, as written) enters Mara as Kallia's dependent kinswoman, a free woman under Kallia's guardianship (never property; Ch.16 and Ch.18 depend on it). The "Syracuse" accent excuse: Sicilian Greek would sound odd here too. She keeps her name; the clerk writes it as Maira, an old Greek name, and does not ask.
3. Language: her Erasmian pronunciation versus living Koine, the comedy and the shame. She already speaks Greek when she must (Valens, the charcoal burner, Ch.6) and has been silent only with Kallia; now, after the market laughs at her, she goes silent *in public* for a month and speaks only inside Kallia's house (all-or-nothing). (Patched 2026-10-19, continuity W-17: Ch.6 already shows her speaking.)
4. Kallia's son's room: swept every morning, the broom laid across its threshold. No explanation.
5. Personal turn: what belonging cost, and Mrs. Dunphy crying at her desk, uninvited and irrelevant.
**Progressive structure:**
- Builds on Ch.6: no way back, so she must stay.
- Adds: legal status, Kallia's own life, and the cost of passing.
- Opens toward Ch.8: Kallia says the women go up the mountain at midwinter.
**Theme presence:** home as belonging-to versus belonging-with.
**Character chaos moments:** teeth (her mastic-stick toothbrush, and her horror at burnt-horn tooth powder). Mrs. Dunphy (green cardigan). All-or-nothing (the month of public silence; she talks only indoors).
**Subtext layer:** Kallia's lessons look like etiquette. Underneath, she is teaching Mara how not to be killed.
**Shareable moment:** —
**Reading speed:** argument passages brisk; scenes slow; the Dunphy memory a sudden drop in pace.
**Word count target:** 6,600
**Writer warnings:** Essayistic must not become lecture. Every claim is followed by a scene in which it hurts or amuses. No anaphora in the argument passages. The closing question must be a real question Mara has, not a rhetorical button or an aphorism.
**Beat subversion:** *Genre beat:* the fish-out-of-water montage of comic mistakes. *Subversion:* the comedy curdles into one bureaucratic act, and the heroine is grateful to be written down as somebody's kin.

## Chapter 8: The Thyiades
**Ledger:** Single-scene (internal shape: *ritual*, the rite's own order is the structure) · open: mid-dialogue → `dialogue` · end: quiet image → `quiet` · 8,200 · dialogue 25–35% · theme present · 0 breaks · gear mid
*(Parnassus, midwinter, AD 71.)*

**Premise:** Mara goes up the mountain at night with the Thyiades, the Delphian women of Dionysus, slips away to the cave, finds it shut again, and comes back to a snowbound heap of women who make room for her.
**Function in arc:** Immersion set-piece (Dimension 7). Her second attempt at the door fails, and the failure is answered by her first belonging.
**Emotional anchor:** women asleep in a heap in the snow, steam rising off them.
**Emotional surprise:** a sacred midnight rite turns into a farce about wet sandals, and that farce is where she first belongs.
**Opening strategy:** mid-dialogue. Kallia, mid-instruction about what not to say on the mountain.
**Key scenes/beats:**
1. Passing a house where an old woman throws barley to the crows and shouts at them for taking it (Theano, unnamed and unrecognized; texture now, recognized in Ch.13 by situation only).
2. **NON-NEGOTIABLE.** The ascent by torchlight: ivy, fawnskins, drums, wine, the dance. It is real and strange and not lurid.
3. **NON-NEGOTIABLE.** Mara slips off to the cave. A hand at the threshold: nothing. She doesn't scream this time.
4. Snow closes the path, and the women are trapped until dawn (Plutarch records a real instance).
5. **NON-NEGOTIABLE.** The wet-sandals farce, a shared cloak, a bawdy song. A woman she has never spoken to pulls her into the heap.
**Progressive structure:**
- Builds on Ch.7: Kallia's world, from the inside.
- Adds: the cave is consistently shut, and Mara is beginning to belong.
- Opens toward Ch.9: money; she has decided to consult the Oracle (Kallia mentions it on the descent).
**Theme presence:** belonging found where the door wasn't.
**Character chaos moments:** none of Mara's forced; the women's own (the wet-sandals worrier, the bawdy singer) carry the chapter. Teeth are not used.
**Subtext layer:** the women's teasing about Mara's "husband" (she has none) is really a test of whether she will laugh with them.
**Shareable moment:** —
**Reading speed:** the rite is fast and rhythmic; the cave slow and silent; the snow-heap very slow.
**Word count target:** 8,200
**Writer warnings:** Avoid "mystical experience" prose. Keep the rite physical and specific. No lyrical climax. Don't use Theano's crows as a wink; they are texture. Keep the women's voices distinct by worldview, not tics.
**Beat subversion:** *Genre beat:* the ecstatic ritual reveals a supernatural truth. *Subversion:* nothing supernatural happens. The revelation is social: a stranger's cloak.

## Chapter 9: The Polygonal Wall
**Ledger:** Collage (internal shape: *stones and errands*) · open: document (a Delphic manumission inscription) → `narrative` · end: short punch → `punch` · 6,400 · dialogue 25–35% · theme present · 5 breaks · gear mid
*(Delphi, late winter, AD 71.)*

**Premise:** To pay for the Oracle Mara starts mending bronze for the sanctuary's priests. Reading the inscriptions on the polygonal wall, she learns what freedom costs here; on the board in the square she learns that a scarred Thracian is wanted as a runaway.
**Function in arc:** The Greece-first obstacle in money and male representation. The Celer threat is introduced. Her conservator skill becomes her living.
**Emotional anchor:** a real-style manumission inscription: a woman "sold to Apollo" for three minae, on condition she remain with her former owner until death.
**Emotional surprise:** her skill earns her money and contempt in the same breath. A priest pays her and wipes his hand.
**Opening strategy:** a document, the inscription's text.
**Key scenes/beats:**
1. **(document, REVEAL)** The manumission text, with its *paramone* clause: freedom with strings attached.
2. **NON-NEGOTIABLE.** She mends a priest's bronze incense stand (her craft, accurate: a cold join, wax, no welding) and gets coins.
3. **NON-NEGOTIABLE.** The cost of a consultation: the *pelanos* fee, a goat, a Delphian sponsor, and a man to ask the question, because women do not go in.
4. **(document, REVEAL)** A notice, newly posted on the board in the square, come over the Boeotian road with the first carts since the snow, copied from one posted at Corinth in Dadaphorios (as written, 2026-10-19): reward for a runaway Thracian, scarred, "answering to Lupus," claimed as property of the household of Q. Arrius Celer. (Knowledge flow: the Corinth original went up in autumn 70; the Delphi copy arrives only now, which is why Valens could work openly through the winter of Ch.6–8 and reads it here as news.)
5. **(document, texture)** A lead curse tablet against a rival's loom. It means nothing.
6. **NON-NEGOTIABLE.** She sees Valens read the notice in the agora and walk away without hurrying. The chapter ends on a ≤7-word line, a single-sentence closing paragraph.
**Progressive structure:**
- Builds on Ch.8: her decision to consult.
- Adds: the price of everything, and Valens's danger.
- Opens toward Ch.10: Kallia's letter arrives (the next chapter is hers).
**Theme presence:** freedom and belonging as legal fictions.
**Character chaos moments:** all-or-nothing (she redoes a join three times because the seam shows).
**Device presence:** documents inside a collage. Each must REVEAL; the curse tablet is the deliberate texture exception.
**Subtext layer:** the priest's bargaining over her fee is really about whether a woman's skill can be worth money.
**Shareable moment:** —
**Reading speed:** documents brisk; mending slow and tactile; the agora sighting sudden.
**Word count target:** 6,400
**Writer warnings:** Mara's mending must NOT become a catalogue device or a recurring "condition report" form (zero-tic ruling); render it as hands at work. No counting of coins aloud. The final punch is a plain observed action, not an aphorism.
**Beat subversion:** *Genre beat:* the heroine discovers the hero's dark secret through a dramatic confrontation. *Subversion:* she reads it on a public notice and watches him read it too. Neither says anything.

## Chapter 10: Kallia's Letter
**Ledger:** Single-scene (internal shape: *one reading, one afternoon*) · open: an object → `short-punch` · end: **PLAIN STOP (no pull)** → `quiet` · 2,800 · dialogue 30–40% · theme present · 0 breaks · gear mid
*(Delphi, late winter, AD 71.)*

**Premise:** A letter comes from Kallia's son in Syria. Kallia can't read, so Mara reads it to her: he is alive, married, and never coming home.
**Function in arc:** A secondary character's own life, fully onstage (Outline Check #9). A short, quiet punch between the money chapter and the Valens chapters.
**Emotional anchor:** the broom, still lying across the empty room's threshold when Kallia goes out.
**Emotional surprise:** the good news (he's alive) is the worst news Kallia could get.
**Opening strategy:** an object. The letter, folded small and stained from the road (≤8 words). It was sent in the autumn and sat at Kirrha harbor all winter while the sea was closed; it comes up the hill with the Elean pilgrim, who brings it on from Kirrha (as written: nobody Ariston trusted was bound for Delphi). (Ch.9 has spent "first carts since the snow": word the arrival freshly.)
**Key scenes/beats:**
1. **NON-NEGOTIABLE.** Mara reads it aloud. Her reading is perfect, unlike her speech, so her gift becomes the instrument of the blow.
2. Ariston writes from Emesa: a wife, a child coming, land in Syria bought with what he saved at the standards and the dowry, after an early discharge for a broken arm (as written, 2026-10-19). He never says he is not coming home; the reader and Kallia hear it. He sends greetings to the neighbors by name and not to the room.
3. **NON-NEGOTIABLE.** Kallia says his name for the first time, once.
4. Kallia goes out to rent the room to a pilgrim from Elis. The chapter **just stops**: Mara alone in the kitchen with the letter, the afternoon going on. No hook.
**Progressive structure:**
- Builds on Ch.7 and 9: the swept room, explained.
- Adds: Kallia as a person with her own loss.
- Opens toward Ch.11: nothing deliberately. The next chapter begins on its own.
**Theme presence:** a child who chose the life he made over the place he came from. **No one draws the parallel**, neither the narrator nor anyone else.
**Character chaos moments:** Kallia's irrational behavior (the broom).
**Subtext layer:** Kallia's questions about the wife ("Is she Greek? Can she weave?") are really asking whether he is happy, which she cannot bear to ask.
**Shareable moment:** —
**Reading speed:** slow, held, one room.
**Word count target:** 2,800
**Writer warnings:** HARD: **do not end on a hook, an image-with-meaning or an aphorism.** End on a plain moment, mid-afternoon. No comparison of Ariston's choice to Mara's in narration; that would be the author's thumb on the scale.
**Beat subversion:** *Genre beat:* the soldier son's letter brings news of death. *Subversion:* he is alive and happy, and that is the bereavement.

## Chapter 11: Valens's Yard
**Ledger:** Chronological (internal shape: *slow reveal of a person*) · open: a sound (sensory spiral) → `long-spiral` · end: spoken line → `dialogue` · 6,200 · dialogue 35–45% · theme present · 3 breaks · gear mid
*(The Kirrha road, late winter, AD 71.)*

**Premise:** Mara needs a man to carry her question into the temple and wants her watch back, so she goes to work in Valens's mule yard. Each scene shows her one more side of him.
**Function in arc:** Slow-burn romance foundation. Felix enters. Valens agrees to carry her question.
**Emotional anchor:** Felix asleep against a mule's belly, the mule standing very still so as not to wake him.
**Emotional surprise:** Valens refuses a kiss, and Mara is relieved.
**Opening strategy:** the yard at dawn as sound, in one long sentence of more than 28 words.
**Key scenes/beats:**
1. Kallia's cousin wants too much to stand as her representative. Mara walks to the yard.
2. He refuses (the sanctuary is full of eyes, and there's a notice with his description on it). She mends harness for a week anyway.
3. **Slow reveal, in this order:** his figs (an absurd argument about drying them); his gentleness with a lame mule; that he reads but pretends he can't; Felix, the boy he bought off a slaver and freed with no paperwork at all.
4. **NON-NEGOTIABLE.** The near-kiss, in the tack shed. He steps back and she is relieved. Neither explains.
5. **NON-NEGOTIABLE.** He agrees to carry her question on the year's first consultation day. Name the day by paraphrase (Apollo's birthday, the god's first day); do **not** use the allowlisted phrase here. He gives no reason, and she doesn't get the watch back.
**Progressive structure:**
- Builds on Ch.9: she saw him read the notice.
- Adds: who he is, piece by piece, and Felix.
- Opens toward Ch.12: they will need a goat from Kirrha (the Delphi goat man's she-goat, Ch.9, costs more than her rag; Kirrha is cheaper).
**Theme presence:** a man who keeps a life no one can take, letting someone in by inches.
**Character chaos moments:** Valens's fig obsession (first appearance). His mind-reading (he is sure the cousin informed on him; the cousin just wanted money).
**Subtext layer:** the fig argument is really about whether she is staying long enough to see a harvest.
**Shareable moment:** —
**Reading speed:** unhurried, a working rhythm.
**Word count target:** 6,200
**Writer warnings:** No banter-for-banter's-sake. His hands are busy because there is work, not as a signature gesture. Do not give Felix a catchphrase; his distinctness is speed and questions. The closing spoken line should be practical, not a romantic button.
**Beat subversion:** *Genre beat:* forced proximity builds to a first kiss. *Subversion:* the kiss is refused and both are relieved. The intimacy that grows is trust, not desire, for now.

## Chapter 12: The Kirrha Road
**Ledger:** In medias res (internal shape: *violence first, story after*) · open: mid-dialogue → `dialogue` · end: short punch → `punch` · 5,600 · dialogue 25–35% · theme present · 2 breaks · gear low
*(Road to Kirrha, early spring, AD 71.)*

**Premise:** Celer's men catch Valens on the road with Mara and the consultation goat. After the killing, he tells her the truth about the legate's wife.
**Function in arc:** The first crucible. Celer's threat made real. Valens's backstory delivered flat. A rehearsal of Mara's voice under pressure.
**Emotional anchor:** Mara hitting a man with her father's camera, and the plastic lens cap rolling in the dust.
**Emotional surprise:** afterward it is Valens who shakes and Mara who steadies him.
**Opening strategy:** mid-dialogue. A stranger's friendly "Lupus?" on the road.
**Key scenes/beats:**
1. **NON-NEGOTIABLE.** Three men. Valens is fast, efficient and unglamorous. Mara swings the Pentax (it survives; the lens cap doesn't). One man dies; two run. Voice under pressure: the asides die and she narrates only what bodies do.
2. **NON-NEGOTIABLE.** After: Valens's hands shaking at the stream. She holds them still.
3. **NON-NEGOTIABLE.** He tells it while washing: the *rudis*, Nero's games at Corinth, Plautia, Celer, the dowry. Flat, chronological, no self-pity. "I was a good bodyguard. That was the use of me." **Knowledge path (one plain passage):** last autumn Plautia's brother's freedman found him at Kirrha harbor and asked him to testify in the dowry suit; he said no; the notice with his description went up in Corinth within the month, and a copy reached Delphi with the spring traffic (Ch.9). So Celer wants a dead witness, not a returned slave, and today's men proved it.
4. Felix brings the goat home. They leave the body for the road's owners to find.
**Progressive structure:**
- Builds on Ch.11: the goat errand.
- Adds: the full scandal, and the knowledge that Celer wants him dead, not merely recaptured (the dowry suit).
- Opens toward Ch.13: the seventh of Bysios is three days off.
**Theme presence:** the stories other people own about you.
**Character chaos moments:** Mara's unprompted memory does NOT appear (save it). Valens's onion memory surfaces at the stream.
**Subtext layer:** he tells her the scandal. Underneath, he is asking whether she will believe him when no one else did, and she answers by not asking a single question.
**Shareable moment:** —
**Reading speed:** very fast fight; slow stream; flat telling.
**Word count target:** 5,600
**Writer warnings:** No choreographed action-movie fight; keep it short, ugly and confused. Using the camera is panic, not cleverness (the K1000 has no flash, so none appears). Valens's account must not be a monologue of grievance. NO aphorism after the killing. The final punch is concrete.
**Beat subversion:** *Genre beat:* the hero saves the heroine and she melts. *Subversion:* she saves a little of him, he falls apart afterward, and the romance is in her steady hands, not his sword.

## Chapter 13: The Seventh of Bysios
**Ledger:** Parallel (internal shape: *outside / inside*, her wait and his account alternating) · open: scene-setting (date) → `scene-set` · end: spoken line → `dialogue` · 8,000 · dialogue 35–45% · theme present · 4 breaks · gear mid
*(Delphi, the year's first consultation day, spring, AD 71.)*

**Premise:** Women may not go in, so Valens carries Mara's question to the god and brings back the answer word for word. Then the Pythia herself, off duty, sends for Mara to her own house and names the city to her face.
**Function in arc:** **TURNING POINT, the WHERE (~30%).** The Oracle is the first and only early source of where. The hour is withheld.
**FINAL VERSION (resolves STATE ARCH-4 / audit WARN-001):** the formal consultation is male-only, and Valens is Mara's representative inside it, so the god's *public* answer reaches her through him. Theano's word "Pompeii" is spoken **in person**, afterwards, at Theano's house: a widow talking to a woman outside the formal consultation, not an oracular response. This is historically defensible and closer to canon ("the Oracle tells her WHERE"). The orchestrator should update STATE ARCH-4 to match.
**Emotional anchor:** Valens repeating the god's answer word for word, the way he once drilled sword-forms.
**Emotional surprise:** the answer comes from a tired woman with bad knees, mid-complaint about the priests' stool. It is precise.
**Opening strategy:** a time opener that the detector recognizes and that does **not** spend the allowlisted phrase, e.g. "The first consultation day of the year came in cold…" (`The first` → `scene-set`). The chapter *title* already carries "the seventh of Bysios" (allowlisted use 2 of 3).
**Key scenes/beats (alternating A/B):**
- **A.** Outside: dawn on the terrace, the crowd, the sprinkling of cold water on the goat. It must shiver to be accepted, and it doesn't, then does. Mara among the waiting women.
- **B.** Inside, as Valens tells it afterward at Kallia's lodging: the laurel smoke, the priest (*prophetes*), the voice from below. The voice is *described* (pitch, the pause, the priest's hand), never quoted.
- **NON-NEGOTIABLE (B).** The public answer, given **once**, in Valens's word-for-word repetition only: *the road home lies under the mountain of vines by the western sea, where the dead go out of the city, at the door painted on a dead man's house.* (Allowlisted phrase, use 1 of 3. "A door painted on a dead man's house" is the second marker that lets Mara find the tomb in Ch.19; it is at-risk, max 1 verbatim.)
- **A.** Mara's frustration: which mountain, which city? A painted door could be anywhere there are tombs.
- **NON-NEGOTIABLE (A).** A temple slave summons her to the house of the old woman who shouts at crows (recognized by situation, from Ch.8). **Theano**, off duty: knees, crows, plain mountain Greek.
- **Object beat (one line, resolves the ibuprofen).** Theano complains about her knees; Mara gives her the last two ibuprofen from the 1998 packet and shows her how to take them. Theano swallows them without thanks. It is a payment, never a joke and never mentioned again in this chapter.
- **NON-NEGOTIABLE.** Mara asks *when*. Theano: not hers to give, or not given. She will not say which, and will not comfort.
- **NON-NEGOTIABLE.** Mara asks *which city*. Theano's last word, which ends the chapter: "Pompeii."
**Progressive structure:**
- Builds on Ch.9, 11, 12: the money, the man, the goat.
- Adds: the door's place. The reader and Mara both know what that city means.
- Opens toward Ch.14: the night she knows.
**Theme presence:** where home is, answered with a place that is also a grave.
**Character chaos moments:** Theano's irrational behavior (the god's barley to the crows).
**Subtext layer:** Theano's grumbling about knees and priests is the cover under which she decides to tell a stranger more than the god gave.
**Shareable moments:** #1 (she alone knows what "Pompeii" means) and #2 (the gladiator carrying her prophecy out word for word).
**Reading speed:** ritual slow; Valens's account measured; Theano's house quick and dry.
**Word count target:** 8,000
**Writer warnings:** Theano must not speak in riddling verse or deliver a theatrical prophecy; her register is a farmer's widow's. She must not hint at the hour ("you will learn it in the fire"). **No narratorial foreshadowing:** Mara's horror arrives in Ch.14. Here it is only the word. Valens's word-for-word recall is shown once, not turned into a running device. Keep "where the dead go out" to its one use here (Valens's repetition, not also the voice). Neither "the seventh of Bysios" in the opener nor anywhere in the body: the title is the chapter's one use.
**Beat subversion:** *Genre beat:* the heroine stands before the Oracle in a trance-lit chamber. *Subversion:* she isn't allowed in the room. The prophecy reaches her second-hand through a gladiator's memory, and the truth comes from an old woman complaining about her knees.

## Chapter 14: What Pompeii Means
**Ledger:** Fragmented (internal shape: *one night in shards*) · open: flat statement (I) → `I-punch` · end: long fade → `long-fade` · 3,400 · dialogue 0–10% · theme present · 9 breaks · gear low
*(Delphi, the same night.)*

**Premise:** Alone that night, Mara holds what she knows about Pompeii and AD 79, and decides to go anyway.
**Function in arc:** Turn the WHERE into dread and resolve. Her plan forms: reach Pompeii, find the door, and be gone long before the mountain.
**Emotional anchor:** Pompeii's fate held in her head like a stone in her mouth, unspeakable to anyone here.
**Emotional surprise:** she laughs, alone, at the cosmic bad taste of it.
**Opening strategy:** "I knew the year." (≤8 words, starting with "I.")
**Key scenes/beats (fragments):**
1. What she knows: the city's plan, the forum, the 1979 exhibition of the plaster casts, seen at fourteen. This is a **past-facing memory of 1998-era knowledge**, not her own future.
2. Eight years. The door could open on any day in them.
3. **NON-NEGOTIABLE.** The laugh.
4. Valens asleep on the floor of Kallia's lodging across Mara's doorway. Kallia put him there herself: the lodging is crammed with consultation-day pilgrims, Celer's men were on the road three days ago, and a guardian uses the guard she has. She does not tell him what Pompeii means.
5. **NON-NEGOTIABLE.** The plan: money, a man, the sea in spring, Italy.
**Progressive structure:**
- Builds on Ch.13: the word.
- Adds: the reader sees what Mara's knowledge costs her, and that she chooses to walk toward it.
- Opens toward Ch.15: she has to tell him something.
**Theme presence:** home behind a door in a city she knows will die.
**Character chaos moments:** none forced. This is a pressure chapter.
**Reading speed:** very short fragments, white space, low sentence gear.
**Word count target:** 3,400
**Writer warnings:** **CRITICAL no-foreshadowing chapter.** Mara may think about AD 79 and the city's fate (her knowledge), but she must not narrate *her own* outcome or any future of hers ("I would be there when…" is banned). The casts are a memory of 1979, described as what she saw then. No anaphora triads in the fragments. No closing aphorism about fate; the ledger asks for a long fade, the night thinning.
**Beat subversion:** *Genre beat:* the prophecy's meaning dawns in a dramatic revelation scene with a confidant. *Subversion:* the dawning is instant, total and private. The drama is that she cannot tell anyone, and the response is a laugh.

## Chapter 15: Summer Pasture
**Ledger:** Chronological (internal shape: *day-in-full*, dawn to night on the high pasture) · open: long sensory spiral → `long-spiral` · end: quiet image → `quiet` · 7,800 · dialogue 30–40% · theme present · 3 breaks · gear high
*(High pasture on Parnassus, summer, AD 71.)* · **HEAT 1: first union**

**Premise:** Hiding from Celer's men with the mules on the high pasture, Mara tells Valens she comes from nineteen centuries ahead. He asks whether they still have mules, and that night they go to bed together.
**Function in arc:** The romance turns. The truth is told, he doesn't believe it and wants her anyway, and the first union follows. The bargain is set: work the summer, go to Corinth for his papers in autumn, sail in spring as man and wife.
**Emotional anchor:** his question, "Do they still have mules?"
**Emotional surprise:** the first union is clumsy and funny before it is anything else, and the funny part is the tender part.
**Opening strategy:** the pasture at dawn in one long sentence: bells, dew, thyme, cold.
**Key scenes/beats:**
1. The bargain spoken plainly. He needs his manumission record from Corinth to travel safely in Italy. She needs a husband to travel at all. Plautia's brother's suit needs his testimony.
2. **NON-NEGOTIABLE.** She tells him the truth, badly. She shows him the flashlight and the camera. **What Valens is told here (knowledge flow):** that she is from nineteen centuries ahead; that a door in the Corycian cave brought her; that the old woman told her the door home is in Pompeii, which is why she must get to Italy. **She does not tell him what will happen to Pompeii** (that waits for Ch.37). He asks practical questions: mules, the emperor, whether the sea is still salt. He decides she is mad in a harmless way, *and does not care*. Pompeii he accepts as a place, because a place is a place.
3. A day of work: milk, mules, Felix's endless questions, the figs that aren't ripe.
4. **NON-NEGOTIABLE (HEAT 1).** The shepherd hut. Explicit, sensual and character-driven: elbows, a collapsing bed, laughter, then the moment the laughter stops. Her asides go quiet. His stillness breaks.
5. Night. Felix snoring by the fire outside. A quiet image to end.
**Progressive structure:**
- Builds on Ch.14: the plan needs a man.
- Adds: he knows her truth (and disbelieves it), and they are lovers.
- Opens toward Ch.16: Corinth in autumn.
**Theme presence:** being known completely and wanted anyway, the home that is a person.
**Character chaos moments:** Valens's figs. Mara's teeth (his are excellent; she notes it at an inappropriate moment).
**Subtext layer:** the mule question is really "will there be a place for me in your world?" Neither hears it that way yet.
**Shareable moment:** #3 ("Do they still have mules?").
**Reading speed:** slow and sensory; brisk in the bargain; slow and specific in the heat; then very quiet.
**Word count target:** 7,800
**Writer warnings:** Heat: no purple euphemism, no clinical terms, no metaphor-stacking, no emotional-temperature report. Watch the em-dashes. The mule line must land once as *his* worldview (practical), and is **never repeated later as a callback or refrain** (zero-tic ruling). No aphorism to close.
**Beat subversion:** *Genre beat:* the hero swears he believes her impossible truth, a declaration of faith. *Subversion:* he doesn't believe her at all and loves her anyway. Belief comes four years later, from overhearing two people speak English (Ch.25).

## Chapter 16: Plautia
**Ledger:** Parallel (internal shape: *two places, two farewells*: Corinth now / the last days at Delphi) · open: mid-dialogue → `dialogue` · end: question → `question` · 7,600 · dialogue 40–50% · theme present · 6 breaks · gear mid
*(Corinth, winter, AD 71–72, intercut with Delphi in autumn.)*

**Premise:** In Corinth, Mara meets the woman Valens was accused with, a ruined aristocrat who wants her son back. Their wary alliance is intercut with Mara's goodbye to Kallia months before.
**Function in arc:** Bring the past in as a supplicant, not a villain. Set the Corinth caper. Close Kallia's arc.
**Emotional anchor:** Plautia giving away a bracelet Mara admired, then weeping over it in the next room.
**Emotional surprise:** Mara's jealousy of Plautia turns into her first female friendship in the past.
**Opening strategy:** mid-dialogue. Plautia's first blunt question to Mara.
**Key scenes/beats (alternating):**
- **Corinth:** Plautia in her brother's house. Exquisite Latin, sudden bluntness. Celer kept her son Marcus (seven this winter). The archive copy of Valens's manumission sits in the provincial record office, newly back under the restored proconsul, on whose staff Celer now serves again.
- **Delphi, autumn:** Kallia's farewell, kept quiet: Delphi has believed since spring that Mara sailed (Ch.15). The string comes down off the mountain for Corinth; Mara goes back to Kallia's door after dark and is gone at first light. **NON-NEGOTIABLE:** Kallia gives Mara the borrowed himation from Ch.7 outright (Mara has worn it all summer and folds it to hand back; Kallia makes it hers). No speech. A sweep of the threshold and the broom put away. **Film (named frame):** Mara photographs Kallia's lamp on the sill in the first morning light, before she goes. Kallia does not know what the camera does and does not ask.
- **Corinth:** the bracelet. Mara's jealousy (were they lovers?) and the answer she gets from watching, not asking.
- **Delphi/the gulf:** the crossing from Kirrha to Lechaion, with mules seasick.
- **NON-NEGOTIABLE (Corinth):** the plan for the triumph games on the Isthmus, when the officials will be at the games.
**Progressive structure:**
- Builds on Ch.15: the bargain in motion.
- Adds: Plautia's own loss (a mother separated from a child) and the Kallia goodbye.
- Opens toward Ch.17: the archive during the games.
**Theme presence:** what is owed to the people you leave.
**Character chaos moments:** Plautia's giving-away (her irrational behavior). Mara's all-or-nothing about Plautia (enemy, then sister).
**Subtext layer:** Plautia and Mara discuss archives and bribes. Underneath, each is asking the other whether Valens loved her.
**Shareable moment:** —
**Reading speed:** Corinth quick and talky; Delphi slow and silent.
**Word count target:** 7,600
**Writer warnings:** Don't make Plautia a rival-trope or a femme fatale. Don't let Kallia's goodbye become a speech or a proverb. The closing question is a real one, unanswered, and not rhetorical.
**Beat subversion:** *Genre beat:* the hero's ex arrives to make trouble. *Subversion:* she was never his lover, she needs help rather than him, and the two women end up allies.

## Chapter 17: Games on the Isthmus
**Ledger:** In medias res (internal shape: *theft first, how-we-got-here in pieces*) · open: mid-action → `short-punch` · end: action unfinished → `quiet` · 7,400 · dialogue 30–40% · theme present · 3 breaks · gear low
*(Corinth, during the one-off games on the Isthmus for Titus's Judaean triumph, spring, AD 72. Not the regular Isthmia, which fell in 71 and 73; AUTHOR-CP3-5.)*

**Premise:** During the games on the Isthmus for Titus's triumph, Mara uses an archivist's instincts to find Valens's manumission record. Then Celer finds them.
**Function in arc:** The Part One action climax, and Celer in person. Valens gets his papers.
**Emotional anchor:** the bored archive clerk who will not stop eating figs during a theft.
**Emotional surprise:** the escape succeeds because a bureaucrat is bored, not because anyone was brave.
**Opening strategy:** mid-action, in the record office: wax tablets, dust (≤8 words).
**Key scenes/beats:**
1. **NON-NEGOTIABLE.** The record office: the fig-eating clerk, Plautia's bribe, and Mara reading shelf-marks the way she reads museum accession numbers. The two-board leaf, cut from the magistrate's cord-bound book (per Ch.16). (Per Ch.12: the registration is not in dispute. The record proves the lanista freed him before witnesses and the emperor; Celer's claim is a bill of sale dated the month before the games.)
2. Fragments of how they got in: Plautia's brother, the games emptying the city.
3. **NON-NEGOTIABLE.** **Celer** in the colonnade: genial, reasonable, patient, a friend you never had. Face to face with Valens. No violence; a conversation with knives underneath.
4. Into the games crowd: athletes, pine-crowns, sausage sellers.
5. Running for Lechaion. The chapter ends mid-run (action unfinished).
**Progressive structure:**
- Builds on Ch.16: the plan.
- Adds: Celer as a person, and Valens's papers recovered.
- Opens toward Ch.18: the quay and a ship that won't wait.
**Theme presence:** proof of who you are, and who gets to hold it.
**Character chaos moments:** Valens's mind-reading, inverted (he trusts the clerk and is right). Celer's irrational behavior (he won't walk under the scaffolding).
**Subtext layer:** Celer's pleasantries ("You look well, Lupus. Free air suits you.") are a threat and an offer at once.
**Shareable moment:** —
**Reading speed:** fast and fragmented; one slow beat with Celer.
**Word count target:** 7,400
**Writer warnings:** No heist-movie competence cascade. The theft succeeds by luck and boredom. Celer gets no villain monologue. Do not let Mara's archive skill become a "competent professional" set-piece; one moment of recognition is enough.
**Beat subversion:** *Genre beat:* the daring heist and the duel with the villain. *Subversion:* there is no duel. The villain is charming, the heist succeeds because a clerk is eating figs, and the danger is legal, not physical.

## Chapter 18: Lechaion
**Ledger:** Single-scene (internal shape: *under an hour on a quay, the same early afternoon as Ch.17's run, with a sail already going up*) · open: flat statement of fact (I) → `I-statement` · end: short punch → `punch` · 2,800 · dialogue 30–40% · theme present · 0 breaks · gear mid
*(Lechaion harbor, spring, AD 72.)* · **HINGE (~41%)**

**Premise:** The ship will only take a married couple, so they marry on the quay in ten words, with Felix and a sailor as witnesses. Valens gives her back her father's watch, wound.
**Function in arc:** The diptych's hinge. Part One closes: lovers become spouses, and Greece is left behind.
**Emotional anchor:** the watch, handed back on a sunlit quay as a wedding gift, already wound.
**Emotional surprise:** the wedding is ten words long and they nearly miss the ship over a mule.
**Opening strategy:** a flat in-moment statement starting with "I" (more than 8 words), a fact of the moment they reach the quay out of the run in the early afternoon (e.g. her lungs or her legs still in the run). The bags are already with Felix, who has had the mules on the quay since before sunrise, so nobody is sitting on them. **Not** a summary of the coming wedding, and **not** a re-narration of the run. **The sail going up at the end of Ch.17 is not waved away in a throwaway line:** the first beats show whose it is (their own ship making ready, or another vessel going out past them), and its pressure carries into the captain's condition. The quay is dry in the sun and the breeze is onshore; spray is fine, rain is not.
**Key scenes/beats:**
1. The captain's condition: a respectable man with his wife and boy, or no passage.
2. **NON-NEGOTIABLE.** The wedding is consent before witnesses (Roman marriage needed no priest). Ten words. Felix cries; the sailor wants to get on.
3. **NON-NEGOTIABLE.** The watch, given back and wound. He has kept it wound for seventeen months (November 70 to spring 72). No speech.
4. A mule refuses the gangplank. Chaos. Aboard.
5. The chapter ends on a ≤7-word line, a single-sentence closing paragraph.
**Progressive structure:**
- Builds on Ch.17: the run to the harbor.
- Adds: marriage, and the watch's return (the re-read thread).
- Opens toward Ch.19: Italy.
**Theme presence:** home as the person beside you on the gangplank.
**Character chaos moments:** none forced. Let it be quick.
**Subtext layer:** the captain's rules are about respectability. The wedding, under them, is the most honest thing either has said.
**Shareable moment:** —
**Reading speed:** fast and practical; one still moment with the watch.
**Word count target:** 2,800
**Writer warnings:** No wedding vows or speeches. No narrator significance ("it was the beginning of everything"). Don't explain that he kept the watch wound; let her notice it is running, and near enough to the sun's noon that he must have set it by the shadow. End on action, not an aphorism.
**Beat subversion:** *Genre beat:* the wedding as a lavish emotional set-piece. *Subversion:* it is ten words on a sunlit quay, conducted to satisfy a ship's captain, and the emotion is in a wound watch.

---

# PART TWO · WHEN

## Chapter 19: Puteoli
**Ledger:** Chronological (internal shape: *walk*, harbor → coast road (a night on the road) → city → the tomb roads, over the first days) · open: scene-setting (place/time) → `scene-set` · end: long fade → `long-fade` · 8,400 · dialogue 20–30% · theme present · 4 breaks · gear high
**Dateline:** *Puteoli · spring, AD 72*

**Premise:** They land at Puteoli under a green mountain Mara refuses to photograph, settle in a Pompeii still rebuilding from an old earthquake, and in her first days she walks the city's tomb roads until, outside the Nuceria Gate, she finds the tomb with the painted door.
**Function in arc:** Arrive at the deadline-place. The door is located and dormant. The Pompeii world is established (Dimension 7).
**Emotional anchor:** the green, vine-covered mountain seen from the deck, one broad summit and nothing like the postcards.
**Emotional surprise:** she refuses to photograph it. Valens says it's a fine mountain for vines, and she agrees with him.
**Opening strategy:** a time opener (e.g. "By the time the goose ship…"), so `scene-set`.
**Key scenes/beats:**
1. **NON-NEGOTIABLE.** The bay from the deck: Puteoli's moles, Misenum's fleet, the mountain. The camera is raised and lowered. The reader's own knowledge does the work.
2. The harbor clerk Valens is sure has marked him (he is short-sighted). The papers work.
3. The coast road to Pompeii: villas, salt pans, the Sarno. With mules and baggage it is two days, with a night at a roadside inn near Neapolis.
4. **NON-NEGOTIABLE.** Pompeii in repair: scaffolds, patched columns, painted election notices, a city ten years after the quake and still mending. **Grata** at her thermopolium rents them rooms.
5. **Search beat (short, a page at most; resolves how she finds it).** The answer gave her the necropolis and one marker, a door painted on a dead man's house. Pompeii's dead go out by every gate. On her first free afternoon she tries the Herculaneum Gate road (marble benches, grand altars, no painted door), then the Stabian Gate's few tombs. Do not tour; one sentence of each road. (Use the book's modern gate names; do not name a "Vesuvius Gate", which would put the mountain's name in her eyeline.)
6. **NON-NEGOTIABLE.** On the next afternoon, alone, Mara walks out of the Nuceria Gate into the tombs, where the dead go out of the city (allowlisted phrase, use 2 of 3). A small freedman's tomb with a painted false door, which she knows at once. **A hand at the threshold:** faintly cool on a warm spring afternoon. Dormant. Real.
7. She touches the microcassette in her bag without comment. A long fade into the city's evening noise.
**Progressive structure:**
- Builds on Ch.18: the ship arrives.
- Adds: Campania, Grata, the door found.
- Opens toward Ch.20: they need a living.
**Theme presence:** home located, in a place that will not last.
**Character chaos moments:** Valens's mind-reading (the clerk). (Teeth not used: Grata's teeth wait for Ch.31.)
**Subtext layer:** "Fine mountain for vines" is just what he thinks. Her agreement is a lie told to a man who can't know why she's lying.
**Shareable moment:** —
**Reading speed:** slow, panoramic; quick at the harbor; very slow at the tomb.
**Word count target:** 8,400
**Writer warnings:** **No foreshadowing via the mountain.** Mara may think "seventy-nine" in scene (her knowledge) once. The narration must not dwell, portend or describe the mountain as menacing. It is green and lovely, and that is the dread. No "little did they know." Pompeii is a working town, not a museum, so avoid tour-guide catalogues. Vary the long canon place-phrases.
**Beat subversion:** *Genre beat:* arriving at the doomed city under ominous skies. *Subversion:* it is spring, the mountain is green and the town is cheerful and under scaffolding. The only ominous thing is that she declines to take a photograph.

## Chapter 20: The Mender's Shop
**Ledger:** Collage (internal shape: *a year told in wall-writing and repairs*) · open: document (the painted lost-property notice, 9–27 words, italics) → `narrative` · end: spoken line → `dialogue` · 8,200 · dialogue 30–40% · theme present · 6 breaks · gear mid
**Dateline:** *Pompeii · AD 72–73*

**Premise:** Mara opens a repair shop in Grata's front room while Valens hauls rubble for a rebuilding city. Over a year, told partly in the town's own wall-writing, she becomes a resident and learns to let a seam show.
**Function in arc:** Build the life the climax will cost. The mending motif turns. The pregnancy is revealed.
**Emotional anchor:** a lamp she mends for a customer, with the seam showing on purpose.
**Emotional surprise:** she weeps at a street fountain because a stranger's toddler hands her a wet pebble.
**Opening strategy:** a document. The real-style painted lost-property notice of beat 1, 9–27 words, in italics (so `narrative`, not `short-punch` or `dialogue`).
**Key scenes/beats:**
1. **(document, REVEAL; the chapter's opening, 9–27 words, set in italics)** A lost-property notice painted on a shopfront ("a bronze pot has gone from this shop…"). Mara takes the trade: people here mend rather than replace.
2. **NON-NEGOTIABLE.** She throws out a bowl she mended because the seam shows (all-or-nothing).
3. Valens's carting: column drums, roof tiles, the quake's leftovers. His fig tree in a pot on the roof. **Film (named frame):** Valens asleep on the roof in the afternoon heat under the potted fig.
3a. **Object plant (one or two sentences, no comment).** After a small shake one night that rattles the lamps and bothers no one, Mara writes the date and a line in the blank back pages of Fenn's notebook. It is a private eruption watch: she knows 62 and she knows the year. She does not reckon anything from it. This is the first entry of the tremor notes Ch.36 depends on.
4. **NON-NEGOTIABLE.** The fountain and the pebble. Unearned and inexplicable.
5. **(document, REVEAL)** An election notice painted over the old earthquake crack in Grata's wall. Texture with a reveal: the city papers over its fault lines.
6. **NON-NEGOTIABLE.** The lamp: she leaves the join visible because the customer wants to see where it broke.
7. Teeth: she trades a repair for a bone toothpick and is absurdly happy.
8. **NON-NEGOTIABLE (end).** Grata clocks Mara's pregnancy before Mara has said it. The chapter ends on Grata's spoken line.
**Progressive structure:**
- Builds on Ch.19: the rooms at Grata's.
- Adds: livelihood, community, and her change in craft.
- Opens toward Ch.21: a child coming, and Valens's past coming too.
**Theme presence:** home as the place you mend.
**Character chaos moments:** teeth; the fountain break; all-or-nothing (the bowl); Valens's figs.
**Device presence:** documents inside a collage (wall-writing). Different in kind from Ch.9's inscriptions.
**Subtext layer:** the customer's wish to see where the lamp broke is a lesson Mara takes without anyone saying it.
**Shareable moment:** —
**Reading speed:** documents quick; repairs slow and tactile; the fountain sudden.
**Word count target:** 8,200
**Writer warnings:** Mending must be hands at work, never a catalogue or a "condition report" device. Do NOT state the theme of the visible seam in narration; let the customer's request carry it. No narrator irony about preservation, ash or excavators.
**Beat subversion:** *Genre beat:* the domestic-happiness montage. *Subversion:* it is told partly through other people's graffiti, and its emotional peak is crying over a pebble, not a romantic moment.

## Chapter 21: The Wolf's Old Name
**Ledger:** Chronological (internal shape: *two rooms*, the amphitheatre and the shop, in alternation) · open: mid-dialogue → `dialogue` · end: question → `question` · 7,200 · dialogue 40–50% · theme present · 3 breaks · gear mid
**Dateline:** *Pompeii · winter, AD 73–74*

**Premise:** A summons comes for Valens to testify in Rome under his own name, just as Pompeii's arena crowd rediscovers "Lupus." He must choose between being nobody and being known.
**Function in arc:** Set Valens's Part Two arc. Felix's arena mania begins.
**Emotional anchor:** Felix's palm-branch scratched into the plaster outside the gladiator barracks.
**Emotional surprise:** Valens's old fame flatters him, and he hates that it does.
**Opening strategy:** mid-dialogue. Felix bursting in with news from the barracks.
**Key scenes/beats:**
1. **NON-NEGOTIABLE (early).** The summons from Plautia's brother: the dowry suit will be heard in Rome in spring, and Valens is the witness. **Knowledge path (one line):** the brother's freedman brings it to Grata's counter by name, because in the summer of 72 Valens sent word of their Pompeii lodging to Plautia, the one person in Corinth who wanted him alive.
2. The amphitheatre at a minor show: an old trainer recognizes him. Graffiti about Lupus. An editor's offer of an exhibition bout. Felix's face.
3. **NON-NEGOTIABLE.** Valens refuses the arena flatly. He has not decided about Rome.
4. Mara, pregnant, argues for Rome: speak, be believed. He argues for invisibility, the children and safety.
5. Ending on a real, open question between them.
**Progressive structure:**
- Builds on Ch.20: a family coming.
- Adds: the summons, the arena pull, Felix's hunger.
- Opens toward Ch.22: Rome.
**Theme presence:** is home where no one knows you, or where you are known?
**Character chaos moments:** Felix's palm-branch; Valens's mind-reading (he thinks Grata is hostile; she fancies him).
**Subtext layer:** they argue about Rome. Underneath, he is asking whether she wants him to be *somebody* because she can't love a nobody, and she is asking whether he will ever stand still in the open.
**Shareable moment:** —
**Reading speed:** brisk scenes; the argument slower.
**Word count target:** 7,200
**Writer warnings:** Do not set up an arena fight for Valens; that expectation is subverted for good in Ch.28. No speeches about honor. The closing question must be genuinely open, not rhetorical.
**Beat subversion:** *Genre beat:* the retired fighter is pulled back for one last bout. *Subversion:* he refuses, and his real "fight" is testimony in a courtroom.

## Chapter 22: The Basilica Julia
**Ledger:** Parallel (internal shape: *court / city*, testimony intercut with Mara walking Rome) · open: long sensory spiral → `long-spiral` · end: spoken line → `dialogue` · 7,600 · dialogue 35–45% · theme present · 7 breaks · gear high
**Dateline:** *Rome · spring, AD 74* · **TURNING POINT (~53%)**

**Premise:** In a Roman court Valens says his own name aloud and tells the truth about Celer. Mara, walked out for laughing, wanders the Rome she once knew as ruins.
**Legal texture (keep accurate, keep light):** a dowry action (*actio rei uxoriae*) is heard by a single *iudex* with his assessors, at a tribunal in the Basilica Julia among the crowded benches of the other courts sitting there. There is no jury.
**Function in arc:** Valens's arc turns from invisibility to being known. Celer is resolved by law. Fascination set-piece.
**Emotional anchor:** Valens saying his own name, loud enough for the back benches.
**Emotional surprise:** Mara's uncontrollable laughter when a man on the benches sneezes during the gravest testimony of Valens's life.
**Opening strategy:** Rome in one long sensory sentence (more than 28 words): scaffolds, noise, the smell of the Tiber.
**Key scenes/beats (alternating):**
- **Court:** the Basilica Julia's tribunals, crowds, lawyers. Celer's advocate is smooth. Plautia veiled. Celer's paper is the backdated bill of sale (the record of the freedom is not in dispute, per Ch.12); the suit defeats it on the lanista's books, the date, or Celer having hired Valens for wages after the games ("After the sword I needed work", Ch.12). **Continuity (Ch.17):** the leaf carries no seal (the seals stayed on the knot of the book) and Celer holds the cut book, so the hearing must say on the page how the leaf is proved, e.g. by the living witnesses among the nine or by the magistrate's colleague of that year, and the choice is the writer's.
- **NON-NEGOTIABLE.** Valens's testimony: plain, his name stated, the frame described. The sneeze. Mara's laughter. She is walked out.
- **City:** Mara in the Forum she visited as a student in 1991, the stones she knew broken now whole. The **Flavian Amphitheatre rising in scaffolding**. She carries a gladiator's child to look at the arena being built, and doesn't think about it more than once.
- **Court:** the verdict is money. Celer must return the dowry. Needing his praetorship more than his pride, he settles the rest privately: the price of quiet is that Plautia may see her son. (Custody is not a remedy in a dowry suit; the access is Celer's concession.) Celer genial in defeat. No violence, ever.
- **NON-NEGOTIABLE.** A glimpse of Plautia with Marcus, nine (b. autumn AD 64), on the basilica steps.
- **End:** a spoken line, Valens's or Plautia's, plain.
**Progressive structure:**
- Builds on Ch.21: he chose to come.
- Adds: vindication, and Celer done.
- Opens toward Ch.23: the road home.
**Theme presence:** being known as a kind of home.
**Character chaos moments:** Mara's failed emotional management (the laugh). Valens's onion memory (in the witness stand).
**Subtext layer:** the lawyers argue dowry law. The real question in the room is whether a gladiator's word can outweigh a senator's.
**Shareable moment:** —
**Reading speed:** court deliberate; city sensory and wandering.
**Word count target:** 7,600
**Writer warnings:** No courtroom-drama clichés: no surprise witness, no outburst, no triumphant speech. The amphitheatre beat must not become narrator irony or symbolism. Her 1991 memory is past-facing and allowed. Keep the em-dashes down.
**Beat subversion:** *Genre beat:* the villain is defeated in a dramatic confrontation. *Subversion:* he is defeated by dowry law and pays. The emotional climax of the trial is interrupted by a sneeze, and the heroine misses it.

## Chapter 23: An Inn on the Appian Way
**Ledger:** Single-scene (internal shape: *one rainy night*) · open: an object → `short-punch` · end: long fade → `long-fade` · 4,200 · dialogue 15–25% · theme present · 0 breaks · gear low
**Dateline:** *The Appian Way, near Tarracina · spring, AD 74* · **HEAT 2: the key turn**

**Premise:** In a flea-bitten roadside inn on the way home, Valens is sad rather than triumphant. Mara, six months pregnant, holds him until he lets himself be held.
**Function in arc:** The marriage turns real on both sides: he is known and lets himself need someone.
**Emotional anchor:** the rough inn blanket, rain on the roof tiles, her pregnant body, and his care.
**Emotional surprise:** after vindication he is sad. The truth cost five years (the frame was in 69) and changes nothing about his back.
**Opening strategy:** an object. The blanket (≤8 words).
**Key scenes/beats:**
1. The inn: a bad supper, a landlady, rain.
2. **NON-NEGOTIABLE.** His sadness, said in five plain words. The onion memory, unexplained.
3. **NON-NEGOTIABLE (HEAT 2).** Explicit and tender: her pregnant body handled frankly and without coyness. He lets himself be the one who is held. Her asides go quiet.
4. A long fade into rain and the fleas.
**Progressive structure:**
- Builds on Ch.22: the verdict.
- Adds: Valens is changed; the marriage deepens.
- Opens toward Ch.24: home, and the birth.
**Theme presence:** home as being held.
**Character chaos moments:** Valens's onion memory. (Teeth not used: the midwife's in Ch.24 is the book's one introduction-by-teeth.)
**Subtext layer:** "It's done" is about the trial on the surface. Underneath it means *now I have nothing to hide behind.*
**Shareable moment:** —
**Reading speed:** slow throughout.
**Word count target:** 4,200
**Writer warnings:** Heat rules (foundation §6e). No triumph speech. No aphorism about truth. No metaphor-stacking. Keep the fleas.
**Beat subversion:** *Genre beat:* victory sex. *Subversion:* it is consolation after a hollow victory, and he is the one being comforted.

## Chapter 24: Lucius
**Ledger:** Fragmented (internal shape: *a night in time-stamped shards*) · open: flat opinion (I) → `I-punch` · end: quiet image → `quiet` · 6,200 · dialogue 25–35% · theme present · 8 breaks · gear low
**Dateline:** *Pompeii · summer, AD 74*

**Premise:** Mara gives birth to Lucius through one long night in Grata's back room, and the voice breaks as it has to.
**Function in arc:** The stakes made flesh. The main rehearsal of voice under pressure.
**Emotional anchor:** Valens holding his son like a dropped amphora he has just caught.
**Emotional surprise:** in the worst of labor she is fixated on the midwife's terrible teeth.
**Opening strategy:** "I hated the midwife." (≤8 words, starting with "I"; the opening paragraph may be a single sentence.)
**Key scenes/beats (shards):**
1. The midwife, the birthing stool, Grata, Juno Lucina invoked, the heat.
2. **NON-NEGOTIABLE.** Voice under pressure: the asides die; she narrates only what hands and bodies do; Latin goes unglossed; speech goes untagged; the senses narrow to sound.
3. Mrs. Dunphy (brown cardigan), uninvited.
4. Valens outside the door, unable to stand still, trimming a mule's hooves by lamplight at midnight. (No nailed horseshoes: the period's equids went barefoot or in strapped hipposandals.)
5. **NON-NEGOTIABLE.** Birth. Lucius. Valens can't hold him until the midwife shows him how.
6. Morning: Valens winds the Seiko on her wrist while she sleeps. No comment. The quiet image ends the chapter.
**Progressive structure:**
- Builds on Ch.23: the pregnancy.
- Adds: a child, so the family is now irreversible.
- Opens toward Ch.25: a rumor from Puteoli (Grata's husband mentions a Chaldean who "talks gibberish to himself").
**Theme presence:** the present made flesh.
**Character chaos moments:** teeth (the midwife's); Mrs. Dunphy (memory mutation 2 of 3).
**Subtext layer:** —
**Reading speed:** very fast shards; slow at the birth; still at the watch.
**Word count target:** 6,200
**Writer warnings:** Voice breaking ≠ list or inventory (zero-tic ruling). Keep the birth real but at harshness ~7, not grinding. No "the first of many" or any future gesture about Lucius. The watch winding is not remarked on.
**Beat subversion:** *Genre beat:* the radiant birth scene. *Subversion:* her strongest memory of it is the midwife's teeth. The tenderness belongs to the man outside trimming a mule's hooves at midnight.

## Chapter 25: Augurinus
**Ledger:** Single-scene (internal shape: *one afternoon in one upper room*) · open: scene-setting (place) → `scene-set` · end: short punch → `punch` · 8,400 · dialogue 45–55% · theme present · 0 breaks · gear mid
**Dateline:** *Puteoli · early spring, AD 75* · **TURNING POINT, the WHEN (~60%)** *(Lucius is about eight months old, in Valens's arms; Mara is not yet pregnant with Aelia, who is born winter 75–76.)*

**Premise:** Mara tracks down a mad old astrologer in Puteoli who turns out to be August Fenn. He speaks English, tells her within a minute when the door will open, and she tells him he is wrong.
**Function in arc:** The cautionary mirror arrives. The WHEN is on the table. Valens finally believes her. The refusal begins.
**Emotional anchor:** an old man in a Chaldean's robe saying "Jesus H. Christ" in a Philadelphia accent.
**Emotional surprise:** the WHEN comes first, bluntly. The mystery is no mystery to him.
**Opening strategy:** a time/place opener (e.g. "It was raining in Puteoli…"), so `scene-set`.
**Key scenes/beats:**
1. Fenn's upper room by the harbor: star charts, wax tablets, a dead Zippo, a potted basil.
2. **NON-NEGOTIABLE.** She speaks English. He answers. His language is frozen in 1968. Her collapse is laughter and tears, both at once.
3. **NON-NEGOTIABLE.** Valens, in the doorway with Lucius, hears two people speak fluently in a language no one knows. He believes her, and it shows on his face. Nobody says so.
4. **NON-NEGOTIABLE.** Fenn's story: 1968, the cave, landing in AD 41, thirty-four years. The doors "breathe with the earth." **How he knows about 62:** the quake opened Pompeii's door for part of one night; he was down with fever in Misenum, and three days later heard a tavern story about a tomb whose painted door "breathed cold" the night of the quake. That is how he found the door, already shut. **The law, in his words:** to Fenn the doors are one door with many mouths (worded once, here), so *it* takes back the one it brought: the cave brought her, so Pompeii's mouth will take her (allowlisted phrase, use 1 of 3, as a *promise*). An opening is brief, hours at most, never days.
5. **NON-NEGOTIABLE.** Mara asks whether it would take others. Fenn: he doesn't know. He has always been alone. **Leave it unknown.**
6. **NON-NEGOTIABLE.** The WHEN, flat and fast: "Late summer, seventy-nine." He has waited for this door since 62.
7. **NON-NEGOTIABLE (the fig leaf, reconciled).** Fenn admits his first two dates for the door's reopening (71, then 73) failed. He worked them from the tremor rhythm alone, sat three nights at the tomb each time, and it stayed shut. (FLEX: Mara realizes that in the autumn of 73 she was living a mile from where he sat.) After 73 he rebuilt the tables around the one thing he knew was coming. He knows from school what happens to Pompeii in 79, says so plainly, and reasons that the earth's biggest breath will open the door: be at the tomb the night after the mountain opens, and gone before the worst. His tremor figures now fit. Mara's refusal seizes on exactly this: he has been wrong twice, and his third date is a year he already knew.
7a. **NON-NEGOTIABLE (the notebook, Margaret; resolves the unplanned reunion).** Mara tells him she has his notebook: she bought his things at an estate sale in Chestnut Hill. He hears "estate sale" and understands that his sister is dead. He does not ask whose sale, and Mara, seeing that, does not say the name. She offers the notebook; he will not take it or open it ("Keep it. I know what's in it."). Nobody says "Margaret" in this chapter, and Mara never says it to him at all. That protects Ch.35, where he says it first.
8. **NON-NEGOTIABLE (end).** She tells him his arithmetic is wrong (≤7 words, a single-sentence closing paragraph).
**Progressive structure:**
- Builds on Ch.24: the rumor from Grata's husband.
- Adds: Fenn, the date, the law of return, and the open question about others. **Valens's knowledge after this chapter:** he believes she is from the future and that a door leads there (he heard the English). He does not follow the English, so he does **not** learn the date or the door's rules here.
- Opens toward Ch.26: his letters begin.
**Theme presence:** a man who never unpacked, face to face with a woman who keeps a bag packed.
**Character chaos moments:** Fenn's automat memory (coconut cream pie). The Phillies (first mention).
**Subtext layer:** Fenn's lecture on tremor-cycles is really a lonely man trying to keep a visitor talking. Mara's "you're wrong" is really "please be wrong."
**Shareable moment:** #4 (the American astrologer, thirty-four years in the past, who has waited since the quake of 62 for a door that opens the night Vesuvius erupts).
**Reading speed:** quick recognition; slow story; very fast date; a dead stop.
**Word count target:** 8,400
**Writer warnings:** Fenn must NOT enumerate or list (zero-tic ruling). His pattern-mind shows in his subject matter. Fenn's dialogue must avoid the banned pattern "in (all) the years since". The style gate scans dialogue too, so use "thirty-four years" or "since I landed." Valens's belief is shown, not declared. Mara's refusal must read as human denial with a fig leaf (two failed dates and a third built around the history-book year), not stupidity. No narrator dread about 79 beyond her own present thought. The "one door with many mouths" idea is worded once, by Fenn, and never repeated verbatim (at-risk list). Mara must not say "Margaret".
**Beat subversion:** *Genre beat:* the mysterious mentor withholds the crucial secret until the right moment. *Subversion:* he blurts it out in the first five minutes, and it is the heroine who withholds, from herself.

## Chapter 26: Letters in English
**Ledger:** Collage (internal shape: *letters against a newborn's months*) · open: document (Fenn's letter) → `narrative` · end: quiet image → `quiet` · 6,000 · dialogue 10–20% · theme present · 7 breaks · gear mid
**Dateline:** *Pompeii · AD 75–76*

**Premise:** Fenn writes to Mara in English by carter's post. She reads his letters aloud to her newborn daughter while her husband grows jealous of a language.
**Function in arc:** Deepen Fenn. Aelia arrives (off the page). The refusal is shown: she doesn't open the copy of his tables.
**Emotional anchor:** Fenn's English read aloud to a three-week-old, in a language no one else in the street speaks. (A present fact of the scene; the anchor must not be rendered as an outcome such as "will never know.")
**Emotional surprise:** Valens is jealous of a language.
**Opening strategy:** a document. A Fenn letter in his runaway 1960s idiom (9–27 words, so `narrative`).
**Key scenes/beats:**
1. **NON-NEGOTIABLE.** The chapter opens with Aelia three weeks old. The birth happened between chapters and is not narrated. Greedy, grabbing, loud.
2. **(document, REVEAL)** Fenn on the Phillies' 1964 collapse, his sister ("I left her a note on the hall table"), unnamed.
3. **(document, REVEAL)** Fenn asks who won the World Series in 1997. He is furious at a word she used ("voicemail").
4. **NON-NEGOTIABLE.** The copy of his tables lies in a box under the bed, unopened. No narration of why.
5. Valens asks her to teach him an English word. She teaches him one, and he uses it wrongly and happily. This happens only in this chapter. **No recurring callback.**
6. Lucius with the knucklebone, rolling it. **Film (named frame):** Lucius, about eighteen months, made to sit still holding his newborn sister, very carefully. (Design note only; the Writer finds the image.)
**Progressive structure:**
- Builds on Ch.25: the correspondence begins.
- Adds: Aelia; Fenn's interior; the tables avoided.
- Opens toward Ch.27: Fenn invites her to Cumae.
**Theme presence:** two languages, two homes, one family.
**Character chaos moments:** Fenn's failed emotional management (the voicemail fury, in a letter). The Phillies. Valens's jealousy (mind-reading).
**Device presence:** documents inside a collage (letters). Each one REVEALS.
**Subtext layer:** Fenn's letters about baseball are really about who he was before.
**Shareable moment:** —
**Reading speed:** letters brisk and voicey; the domestic sections slow.
**Word count target:** 6,000
**Writer warnings:** The English word Valens learns must NOT become a recurring tic or callback. Fenn: no numbering. No narrator commentary on the unopened box.
**Beat subversion:** *Genre beat:* a second birth scene. *Subversion:* it happens off the page. The chapter is about letters, and the newborn is simply there.

## Chapter 27: Cumae
**Ledger:** Chronological (internal shape: *walk*, Puteoli → the Phlegraean fields → the Sibyl's cave) · open: claim/opinion (I) → `I-statement` · end: long fade → `long-fade` · 7,600 · dialogue 35–45% · theme present · 3 breaks · gear high
**Dateline:** *Cumae · AD 76*

**Premise:** Fenn takes Mara, little Lucius and the baby to the Sibyl's cave at Cumae to show her a door that died, and she watches what thirty-five years of waiting have done to him. (Aelia, a few months old, rides in a sling against Mara and sleeps through the Sibyl.)
**Function in arc:** The cautionary mirror at full strength, through example and never lecture. The rules of the doors are deepened.
**Emotional anchor:** Fenn pressing his palm to the rock of a dead door, as if it might be warm.
**Emotional surprise:** in the cave Fenn is funny and young, and it is Mara who feels old.
**Opening strategy:** a claim starting with "I" (more than 8 words), about what she had expected the Sibyl's cave to be.
**Key scenes/beats:**
1. The road: sulphur fields at Puteoli, steam vents (texture, not portent), Lake Avernus. **Film (named frame):** Fenn on the road in daylight, trying to light the dead Zippo for the picture.
2. **NON-NEGOTIABLE.** The long trapezoidal gallery of the cave, cut light. Fenn finds the dead door. A **hand at the threshold**, *his*.
3. Fenn's crossing story, more of it: the coat he left at the cave mouth in 1968.
4. **NON-NEGOTIABLE.** Lucius rolls the knucklebone down the gallery. Fenn draws a baseball diamond in the dust for him.
5. Long fade on the walk back, the bay going purple. (The 1990s-word rage stays a one-off in the Ch.26 letter; it is not repeated in person.)
**Progressive structure:**
- Builds on Ch.26: his invitation.
- Adds: doors can die, and Fenn's waiting has a texture.
- Opens toward Ch.28: Felix has gone missing (news on return).
**Theme presence:** what waiting for another life costs.
**Character chaos moments:** the Phillies, the automat (lemon meringue: memory mutation).
**Subtext layer:** Fenn's tour of the dead door is really a confession that he has never lived anywhere.
**Shareable moment:** —
**Reading speed:** a slow walk; still in the cave.
**Word count target:** 7,600
**Writer warnings:** The Phlegraean steam is texture. Do NOT let narration connect it to the mountain. Fenn must not say "don't end up like me," and neither may the narrator. Dialogue must avoid "in (all) the years since". No closing aphorism.
**Beat subversion:** *Genre beat:* the mentor shows the hero the place of power. *Subversion:* the place of power is dead. The lesson is the mentor himself, and he doesn't know he is teaching it.

## Chapter 28: Felix in the Arena
**Ledger:** In medias res (internal shape: *the bout, then the week that led to it, then the bout's end*) · open: mid-action (crowd noise) → `short-punch` · end: spoken line → `dialogue` · 7,000 · dialogue 25–35% · **theme RECEDES** · 4 breaks · gear low
**Dateline:** *Pompeii · AD 76*

**Premise:** Felix, now eighteen, has sworn himself to Pompeii's gladiator school. Valens, who refused the arena for himself, sits in the stands with his son on his knee to watch the boy he freed fight.
**Function in arc:** A secondary character's own life (Outline Check #9). Valens's arena arc closes without him fighting. A breathing chapter for the theme.
**Emotional anchor:** Valens in the stands, holding Lucius on his knee while Felix fights below.
**Emotional surprise:** the fight is short and dull. Felix survives, and the crowd hated it.
**Opening strategy:** mid-action. The crowd's roar as a short line (≤8 words).
**Key scenes/beats:**
1. The bout begins, a thraex against a murmillo.
2. **Backfill.** Felix vanished. Valens found him at the barracks, sworn by oath as a free man for a term (*auctoratus*), which cannot be bought out before his first fight. Felix's pride. A girl at the fuller's he wants to impress.
3. **NON-NEGOTIABLE.** Valens's decision to *watch* rather than intervene, since he can't save him by fighting.
4. **NON-NEGOTIABLE.** The bout: clumsy, cautious, short. Both are sent off standing. The crowd jeers. Felix is alive.
5. Felix's spoken line to Valens afterward ends the chapter.
**Progressive structure:**
- Builds on Ch.27: news of Felix's disappearance waiting at home.
- Adds: Felix's adulthood, and Valens's arena past closed.
- Opens toward Ch.29: the household together for Saturnalia.
**Theme presence:** **RECEDES.** This is Felix's chapter.
**Character chaos moments:** Felix's palm-branch, scratched under the seats. Valens's mind-reading (he thinks the lanista is cheating Felix; he isn't, much).
**Subtext layer:** Valens and Felix argue about the contract. Underneath, the son asks the father whether he is ashamed of him.
**Shareable moment:** —
**Reading speed:** fast bout; measured backfill; fast end.
**Word count target:** 7,000
**Writer warnings:** No glorious arena set-piece. Valens must NOT step into the arena; that is the expectation this chapter refuses. Felix's speech is distinct by speed and questions, with no catchphrase. Harshness ~7.
**Beat subversion:** *Genre beat:* the old champion's protégé fights for his life in a thrilling bout, or the champion steps in. *Subversion:* it is dull, both men walk off alive, and the crowd is angry. The champion's courage is to sit still.

## Chapter 29: Saturnalia
**Ledger:** Essayistic (internal shape: *claim → evidence → shame*) · open: claim/opinion → `narrative` · end: quiet image → `quiet` · 6,600 · dialogue 35–45% · theme present · 3 breaks · gear high
**Dateline:** *Pompeii · December, AD 76*

**Premise:** Mara argues that Saturnalia was the best idea Rome ever had, and proves it with a household where the gladiator weeps at a farce and the old astrologer explains baseball. Then she has to face that she enjoyed it.
**Function in arc:** The family at its fullest, with Fenn inside it. Valens and Fenn's friendship (two exiles). Light before the tremor.
**Emotional anchor:** Valens weeping helplessly at a mime farce about a cuckolded baker.
**Emotional surprise:** Saturnalia's slave-and-master inversion is truly joyful, and Mara is ashamed of enjoying a festival in a slave society.
**Opening strategy:** a claim (9–27 words, so `narrative`).
**Key scenes/beats:**
1. Evidence: wax candles, clay figurines as gifts, the felt caps, gambling in the open. Felix on leave from the school, crowned mock-king.
2. **NON-NEGOTIABLE.** Fenn at dinner: baseball explained to Valens with olive pits. Valens's questions (practical, of course).
3. **NON-NEGOTIABLE.** The mime show at a street stage. Valens weeps; Lucius (about two and a half, on his father's shoulders) leans down and pushes a piece of bread at his father's mouth to make it stop.
4. Mara refuses to sing because she can't do it well (all-or-nothing). Then she sings, badly.
5. The personal turn: the household's own enslaved neighbor served at table, and the shame. A quiet image to end.
**Progressive structure:**
- Builds on Ch.28: Felix alive.
- Adds: Fenn as family, and Valens's tears.
- Opens toward Ch.30: winter turns; the floor moves.
**Theme presence:** home as a table.
**Character chaos moments:** Valens's failed emotional management (the mime). Fenn's Phillies. Mara's all-or-nothing (singing).
**Subtext layer:** the baseball lesson is two exiles agreeing to be friends without saying so.
**Shareable moment:** —
**Reading speed:** argument brisk; dinner warm and slow.
**Word count target:** 6,600
**Writer warnings:** Essayistic is not lecture. Every claim pays off in a scene. Hold slavery's harshness at ~7: present, real, not grinding. The shame beat must not resolve into an aphorism.
**Beat subversion:** *Genre beat:* the festive set-piece in which a hidden tension erupts. *Subversion:* nothing erupts. The only tension is Mara's private shame at being happy.

## Chapter 30: Tremor
**Ledger:** Fragmented (internal shape: *one morning, shaken apart*) · open: flat statement (I) → `I-punch` · end: short punch → `punch` · 2,600 · dialogue 5–15% · theme present · 6 breaks · gear low
**Dateline:** *Pompeii · AD 77*

**Premise:** A small earthquake cracks the kitchen wall. The family laughs, and Mara runs to the tomb hoping the doors might breathe early.
**Function in arc:** The first physical tremor. Her hope for an early door shows, and fails.
**Emotional anchor:** plaster dust on the bread; the family laughing at a crack in the wall.
**Emotional surprise:** Mara is *relieved* by the tremor. If the doors "breathe with the earth," this could be an early chance.
**Opening strategy:** "I was kneading when the floor moved." (≤8 words, starting with "I"; the opening paragraph may be a single sentence.)
**Key scenes/beats:**
1. Dust, a cracked wall, Grata swearing, Aelia laughing.
2. **NON-NEGOTIABLE.** Mara runs out of the Nuceria Gate. **A hand at the threshold:** nothing more than the same faint coolness she felt the day she found it, under sun-warmed plaster. No colder.
2a. **Knowledge beat (no dialogue needed).** When she turns, Valens is standing in the road with plaster dust in his hair; he followed her when she ran. He looks at the painted door and at her hand on it and asks nothing. From here he knows where the door is.
3. The walk back past people re-plastering already. In Campania this is ordinary. That night she adds the tremor to the back pages of Fenn's notebook.
4. A ≤7-word last line, as a single-sentence closing paragraph.
**Progressive structure:**
- Builds on Ch.29: winter into spring.
- Adds: her secret watching for an early door.
- Opens toward Ch.31: town life goes on.
**Theme presence:** the door wanted, and denied again.
**Character chaos moments:** none forced.
**Reading speed:** fast.
**Word count target:** 2,600
**Writer warnings:** No portent ("the first warning"). The tremor is an ordinary Campanian event for everyone but Mara, and her thought is about the door, not the eruption. No anaphora.
**Beat subversion:** *Genre beat:* the first ominous tremor of the coming catastrophe. *Subversion:* for the heroine it is a burst of hope, and for everyone else a plastering job.

## Chapter 31: Election Paint
**Ledger:** Chronological (internal shape: *errand*, one night's sign-painting) · open: mid-dialogue → `dialogue` · end: **PLAIN STOP (no pull)** → `long-fade` · 4,800 · dialogue 40–55% · **theme RECEDES** · 2 breaks · gear mid
**Dateline:** *Pompeii · March, AD 77*

**Premise:** Grata's son is running for aedile on money they don't have. Mara spends a night holding a ladder while Grata whitewashes his rivals' notices.
**Function in arc:** Pompeian civic comedy and Grata's own life. A breather before the fever.
**Emotional anchor:** Grata whitewashing a rival's election notice by lamplight with Mara holding the ladder.
**Emotional surprise:** pure comedy with no stakes, in a book about to break.
**Opening strategy:** mid-dialogue. Grata, mid-complaint.
**Key scenes/beats:**
1. Grata's husband's dice debts, Secundus's campaign, and the professional sign-painters who work at night.
2. **NON-NEGOTIABLE.** The whitewashing raid. Valens refuses to help, then holds the lamp.
3. Teeth: Grata's, discussed at length with Grata, to Mara's shame.
4. **NON-NEGOTIABLE.** It **just stops**. They finish, Grata rinses her brush, and they go to bed. The result of the election is not given.
**Progressive structure:**
- Builds on Ch.30: life goes on after the tremor.
- Adds: Grata's family, and Pompeii's democracy as farce and texture.
- Opens toward Ch.32: nothing deliberately.
**Theme presence:** **RECEDES.**
**Character chaos moments:** teeth (Mara, third appearance). Grata's irrational behavior.
**Subtext layer:** Grata's ambitions for Secundus are really about not being only a woman who sells lentils.
**Shareable moment:** —
**Reading speed:** brisk and comic.
**Word count target:** 4,800
**Writer warnings:** Do NOT end on a hook, an image-with-meaning or an aphorism. A plain stop, more than 25 words in the final sentence (`long-fade`). Real-style electoral formula ("…asks you to elect…") at most once. **(after Ch.20)** The night whitewash must not restage Ch.20's hired crew: no lamp on a pole, no "hold the ladder" in anyone's mouth or on any wall, no wall-writing of Ch.20's kinds, no letter set on a crack. Mara's own hands on the ladder by Grata's lamp are the deliberate counterpoint (see character-bible "Ch.31 guard").
**Beat subversion:** *Genre beat:* a secondary-character subplot that sets up a later plot turn. *Subversion:* it sets up nothing. It is a night of whitewash.

## Chapter 32: Fever
**Ledger:** Single-scene (internal shape: *one night, by breath*) · open: scene-setting (time) → `scene-set` · end: quiet image → `quiet` · 7,800 · dialogue 15–25% · theme present · 0 breaks · gear low
**Dateline:** *Pompeii · summer, AD 77* · **TURNING POINT (~77%)**

**Premise:** Through one night, three-year-old Lucius burns with a fever that a week of 1998 antibiotics would have cured. Mara, who knows the name of the pill, can do nothing but what the Greek doctor does.
**Function in arc:** The want turns. From here on, Mara wants the door for the children.
**Emotional anchor:** Lucius's breath, counted by sound in the dark; the doctor's honey and vinegar.
**Emotional surprise:** he recovers through nursing, luck and the doctor's ordinary care. Her modern knowledge is useless.
**Opening strategy:** a time opener ("It was the third night…"), so `scene-set`.
**Key scenes/beats:**
1. **Philokrates**, the Greek physician: honey-and-vinegar, poultices, cool cloths. Mara refuses the bleeding. They argue in Greek she can now speak.
2. **NON-NEGOTIABLE.** Voice under pressure, at full strength: the asides die; she narrates only hands and breath; the senses narrow to sound.
3. Valens at the Temple of Isis, then home. He winds the watch at midnight without a word.
4. **NON-NEGOTIABLE.** The word *amoxicillin* in her head, useless as a prayer. (One past-facing line, if the scene wants it: the last of the 1998 ibuprofen went into a priestess's knees six years ago. It would only have cooled him anyway.)
5. **NON-NEGOTIABLE.** Dawn. The fever breaks. A quiet image of breathing.
**Progressive structure:**
- Builds on Ch.31: an ordinary town, an ordinary summer sickness.
- Adds: what 1998 would mean for her children.
- Opens toward Ch.33: her argument for the future.
**Theme presence:** home as the place where your child can be saved.
**Character chaos moments:** Valens's onion memory (once, in the small hours).
**Subtext layer:** the argument with the doctor over bleeding is really about whose knowledge counts.
**Shareable moment:** —
**Reading speed:** slow and held; short sentences in the worst hour.
**Word count target:** 7,800
**Writer warnings:** Do not let Mara save him with modern knowledge (no improvised penicillin, no germ-theory heroics). Voice breaking ≠ list. No "if he died…" future speculation in narration beyond her present fear. No aphorism at dawn.
**Beat subversion:** *Genre beat:* the time traveler saves the day with modern knowledge. *Subversion:* her knowledge is worthless. The ancient doctor and blind luck save him, and that is what changes her.

## Chapter 33: The Case for Penicillin
**Ledger:** Essayistic (internal shape: *argument → evidence → what it frightens in her*) · open: claim/opinion (I) → `I-statement` · end: question → `question` · 5,600 · dialogue 20–30% · theme present · 3 breaks · gear high
**Dateline:** *Pompeii and Puteoli · autumn, AD 77*

**Premise:** Mara builds the case for taking her children through the door into her century, and the case is so good it frightens her.
**Function in arc:** Her want is reframed. The question of whether others can pass becomes urgent, and it is still unanswerable.
**Emotional anchor:** Mara drawing a pill on a wax tablet for Valens. A white oval, the most important object in the world.
**Emotional surprise:** her case is so persuasive that it scares her.
**Opening strategy:** a claim starting with "I" (more than 8 words).
**Key scenes/beats:**
1. The argument: medicine, schools, a girl's life in 1998 against a girl's life here, the small tombs at the necropolis. **No counted list** (zero-tic ruling).
2. **NON-NEGOTIABLE.** The pill on the wax tablet. Valens's practical questions: what would *he* be there? A man with scars and no papers, nobody again.
3. **NON-NEGOTIABLE.** At Puteoli: will the door take them? The conversation is in **Greek**, with Valens present, so that he hears that the door might not take him or the children. Fenn: he doesn't know, and he has never seen anyone try. He says, gently, that he would like to see it. **Nobody names the date in front of Valens** (Mara steers away from it); he learns it, and what the mountain will do, in Ch.37.
4. Personal: the fear her own eloquence raises. She is planning her children's lives the way her father planned digs.
5. A real question ends the chapter.
**Progressive structure:**
- Builds on Ch.32: the fever.
- Adds: the door for four, and Valens's fear of being nobody in her world.
- Opens toward Ch.34: next summer (a leap of a year).
**Theme presence:** home for the children: which world?
**Character chaos moments:** Mara's all-or-nothing (the whole family through, or no one).
**Subtext layer:** Valens's questions about 1998 jobs are really "will you still need me there?"
**Shareable moment:** #5 (she wants to take her children through the door to penicillin).
**Reading speed:** argument fast; scenes slow.
**Word count target:** 5,600
**Writer warnings:** Avoid anachronism lectures. Her picture of 1998 must be personal and specific (her school, her pediatrician's lollipops), not a statistics speech. No narrator irony about what the door will do.
**Beat subversion:** *Genre beat:* the heroine longs to go home. *Subversion:* she no longer wants home for herself. She wants to *export* her family to it, and that is a new kind of danger.

## Chapter 34: Surrentum
**Ledger:** Chronological (internal shape: *day-in-full*) · open: long sensory spiral → `long-spiral` · end: **PLAIN STOP (no pull)** → `quiet` · 7,600 · dialogue 30–40% · **theme RECEDES** · 3 breaks · gear high
**Dateline:** *Surrentum · summer, AD 78* · **HEAT 3: the late unshadowed joy**

**Premise:** A perfect family day at the sea across the bay. Lucius swims, Aelia eats sand, and that night, at the inn, the marriage is at its most at ease. Then the day simply ends. *(Design labels such as "happiest" are for the architect only and must never reach the page; see N-19.)*
**Function in arc:** The banked joy, unshadowed inside the scene. The last heat scene.
**Emotional anchor:** Lucius swimming three strokes to his father in green water.
**Emotional surprise:** nothing goes wrong, and the chapter ends without anything happening.
**Opening strategy:** the sea in one long sentence of more than 28 words.
**Key scenes/beats:**
1. The boat across, the cliffs of Surrentum, a fish lunch.
2. **NON-NEGOTIABLE.** Lucius's three strokes. Aelia and the sand. The knucklebone lost in the sand and found.
3. Valens and the Surrentine figs (third and last appearance of the obsession).
4. **NON-NEGOTIABLE (HEAT 3).** The inn. Explicit, joyful and unhurried, the most at-ease they ever are. Nothing in the scene points anywhere.
5. Morning: breakfast. The chapter **just stops**.
**Progressive structure:**
- Builds on Ch.33: a year has passed; the plan is held, not settled.
- Adds: the family at its happiest.
- Opens toward Ch.35: nothing deliberately.
**Theme presence:** **RECEDES.**
**Character chaos moments:** figs (third); teeth not used.
**Subtext layer:** none; that is the design.
**Shareable moment:** —
**Reading speed:** slow, sun-warm.
**Word count target:** 7,600
**Writer warnings:** **The mountain must not be mentioned or framed.** It is across the bay, and Mara does not look at it in this chapter. No foreshadowing, no "happiest day of my life" significance-tagging, no "I wanted to keep it forever." Do NOT end on an image-with-meaning. A plain breakfast stop.
**Beat subversion:** *Genre beat:* the idyllic day before disaster, shot through with dread. *Subversion:* there is no dread in the scene at all, and the chapter ends without a turn. The dread is entirely the reader's.

## Chapter 35: Fenn's Winter
**Ledger:** Parallel (internal shape: *deathbed / 1968*, Fenn's dying intercut with the story of his leaving, told in his own words) · open: mid-dialogue → `dialogue` · end: document fragment → `long-fade` · 7,000 · dialogue 35–45% · theme present · 6 breaks · gear mid
**Dateline:** *Puteoli · winter, AD 78–79*

**Premise:** Fenn dies in his upper room, still waiting for the door he has watched since the quake of 62 (and for a way home since he landed in 41), arguing about baseball and insisting to the end that he would have gone through. (Mara still refuses his date until Ch.36, so her narration must not say the door is "months" away. If a count is spoken, it is Fenn's: thirty-seven years, nearly thirty-eight.)
**Function in arc:** The cautionary mirror completes as negative example, not lesson. His tables and his 1968 objects pass to her.
**Emotional anchor:** the Zippo, refilled with lamp oil, finally catching once in Fenn's hand.
**Emotional surprise:** his dying is irritable and funny.
**Opening strategy:** mid-dialogue. Fenn complaining about the doctor.
**Key scenes/beats (alternating):**
- **Deathbed:** Mara nursing him; Valens carrying him to the window; the children kept away, then not.
- **1968, in his words:** Philadelphia, the morning he left, the note on the hall table. **NON-NEGOTIABLE:** he asks at last for the notebook he refused in Ch.25, reads his own 1968 front pages (not her tremor notes at the back), and says his sister's name, Margaret, for the first time. Mara has never said it to him; she does not say it now.
- **Object beat (one line, no comment).** Waiting by the bed while he sleeps, Mara touches the microcassette in its sock in her bag.
- **NON-NEGOTIABLE.** The Zippo catches once.
- **NON-NEGOTIABLE.** He gives her his original tables and his things (the Zippo, a 1964 dime, a coverless paperback), and the notebook back. He insists he'd go. He does not have a deathbed conversion.
- **Death.** Rendered plainly.
- **End (document fragment):** the last line in his own hand in the margin of his tables, something practical and in English. It ends the chapter as a long fade.
**Progressive structure:**
- Builds on Ch.33–34: Fenn's health failing offstage.
- Adds: his death, and the tables now hers alone.
- Opens toward Ch.36: news from Rome in the summer.
**Theme presence:** a man who never unpacked dies packed.
**Character chaos moments:** the Phillies (last); the automat (mutation 3: he can't remember the pie).
**Subtext layer:** the baseball argument is the only way he can say he is frightened.
**Shareable moment:** —
**Reading speed:** slow; the 1968 sections quicker and brighter.
**Word count target:** 7,000
**Writer warnings:** No deathbed wisdom, and NO "don't waste your life waiting" speech. Fenn must not enumerate. Mara's narration must not tag significance ("the last thing he ever said to me" is banned). The document fragment is practical, not a moral.
**Beat subversion:** *Genre beat:* the mentor's death delivers a final lesson. *Subversion:* he learns nothing, says so, and dies wanting the door. The lesson is all in what Mara sees.

## Chapter 36: News of Vespasian
**Ledger:** Collage (internal shape: *the notice, the tables, the tomb*) · open: flat statement of fact → `short-punch` · end: short punch → `punch` · 4,400 · dialogue 15–25% · theme present · 5 breaks · gear low
**Dateline:** *Pompeii · July, AD 79* · **TURNING POINT, the arithmetic (~86%)**

**Premise:** The emperor's death reaches Pompeii, and Mara finally sits down with Fenn's tables and her own seven years of tremor notes. The arithmetic puts the door in the eruption's night. (The news has been in the streets since late June; the posted notice she reads in early July is what makes her sit down. Her notes were kept independently of Fenn's tables, which is why their agreement ends the refusal.)
**Function in arc:** The refusal ends. The clock compresses from years to weeks.
**Emotional anchor:** a wax tablet of Fenn's tables, her own figures beside his, matching.
**Emotional surprise:** the day she stops pretending, her first feeling is calm.
**Opening strategy:** "The emperor was dead." (≤8 words; the opening paragraph may be a single sentence.)
**Key scenes/beats:**
1. **(document, REVEAL)** The public notice: Vespasian dead on 23 June, Titus emperor.
2. **NON-NEGOTIABLE.** Year arithmetic she can no longer avoid: it is AD 79, and she knows what late August means.
3. **(document, REVEAL)** Fenn's tables beside her own tremor notes, kept since 72 in the back pages of Fenn's 1968 notebook (planted Ch.20 and Ch.30). The figures agree. The door opens in the night after the mountain opens. She copies his key figures into the notebook beside hers, so the notebook now carries both.
4. **NON-NEGOTIABLE.** The tomb with the tables in her hand. **A hand at the threshold:** cooler than before.
5. A ≤7-word last line, as a single-sentence closing paragraph.
**Progressive structure:**
- Builds on Ch.35: the tables are hers.
- Adds: the date accepted, and the door confirmed as the eruption's door.
- Opens toward Ch.37: she must tell Valens everything.
**Theme presence:** the visitor runs out of time.
**Character chaos moments:** none forced.
**Device presence:** documents inside a collage (the notice; the tables). Each must REVEAL.
**Subtext layer:** —
**Reading speed:** quick, then a held moment at the tomb.
**Word count target:** 4,400
**Writer warnings:** Mara now knows the eruption date (24 August, from Pliny), and she may state it in present thought. She must NOT narrate *her own* outcome. Her tremor notes are a document, shown once, and must not become a recurring catalogue device. No aphorism.
**Beat subversion:** *Genre beat:* the terrible revelation lands as shock. *Subversion:* she always knew. The revelation is that she stops lying, and what she feels is calm.

## Chapter 37: The Boat at the Sarno Mouth
**Ledger:** Single-scene (internal shape: *one argument, start to finish, at the river port*) · open: flat statement (I) → `I-statement` · end: spoken line → `dialogue` · 6,400 · dialogue 50–60% · theme present · 0 breaks · gear mid
**Dateline:** *The Sarno river port · early August, AD 79*

**Premise:** Mara tells Valens everything: the mountain, the date, the door, the hours people had to escape. They fight over whether to flee now or wait for the door. He agrees to stay, with a hired boat as backup, because she has never asked him for anything.
**Function in arc:** The marriage's truth-test. **The plan is locked, and its order is set by the clock:** they stay in Pompeii for the door. Because the door only breathes in the night after the mountain opens, Valens's one condition is that the daylight hours go to the boat. When the mountain opens they go first to the river mouth; if the sea lets them out, they all go by sea, Mara included, and the door is let go; if the sea refuses, they go to the tomb for the night. (This is the order Ch.40 follows.)
**What Valens knows coming in, and what is new here:** he already knows she is from the future (Ch.15, believed Ch.25), that the door leads there and might not take him or the children (Ch.33), and where the door is (Ch.30). **New in this chapter:** what the mountain will do, the day, the hours of falling stone, and that the door's night is the eruption's night. Felix is told only that Mara fears the mountain; he takes the boat for the money and for Valens, and knows nothing of the door.
**Emotional anchor:** the hired boat's painted eye at the Sarno mouth, with Felix (his term at the school served out) asleep in it.
**Emotional surprise:** Valens agrees not because he believes in the door, but because she has never asked him for anything.
**Opening strategy:** a flat statement starting with "I" (more than 8 words).
**Key scenes/beats:**
1. **NON-NEGOTIABLE.** The whole truth, in order: what the mountain will do, what day, and the hours of falling stone before the end, from Pliny's letters as she remembers them. Valens believes her (Ch.25 settled that).
2. **NON-NEGOTIABLE.** His case: take the children to Neapolis tomorrow, and the future be damned. Her case: the door, for them, with time to run if it fails.
3. The compromise: the boat, Felix, the river mouth; the boat first in daylight, the door at night (see Function).
4. **NON-NEGOTIABLE.** Why he agrees. A plain line, not a speech.
5. His spoken line ends the chapter.
**Progressive structure:**
- Builds on Ch.36: she has to tell him.
- Adds: the plan, its backup, and his consent.
- Opens toward Ch.38: the weeks contract to days.
**Theme presence:** home as the person who trusts you against his own judgment.
**Character chaos moments:** Valens's mind-reading (the boat-owner, wrongly).
**Subtext layer:** they argue about routes and hours. Underneath, she is asking whether he will let her gamble with their children, and he is asking whether she will ever choose *here*.
**Shareable moment:** —
**Reading speed:** fast, high-dialogue.
**Word count target:** 6,400
**Writer warnings:** This is the highest-dialogue chapter in the book. Keep both voices distinct by syntax (his short and level, hers spiralling and then clipped). No "if only we had fled" hindsight. No narrator pronouncement on the wisdom of the plan.
**Beat subversion:** *Genre beat:* the husband refuses to believe the wife's impossible warning. *Subversion:* he believes every word, and that makes it harder. The fight is about trust, not truth.

## Chapter 38: Vinalia
**Ledger:** Parallel (internal shape: *the festival / the packing*) · open: scene-setting (date) → `scene-set` · end: quiet image → `quiet` · 8,000 · dialogue 25–35% · theme present · 5 breaks · gear high
**Dateline:** *Pompeii · 19 August, AD 79*

**Premise:** On the wine festival five days before the mountain opens, the city is sweet and drunk. Mara photographs the mountain with frame 36, the end of the roll, tries to get the people she loves out of town, and is happy.
**Function in arc:** A full ordinary day, rendered fully and with no tagging. The final long immersion before the lengths collapse.
**Emotional anchor:** frame 36, the end of the roll, spent on the mountain at dawn: a thread of cloud on the summit that may only be cloud.
**Emotional surprise:** the Vinalia is ordinary and lovely, and she is happy.
**Opening strategy:** a time opener the detector recognizes: "It was the Vinalia…" (not "On the nineteenth…", which does not compute as `scene-set`).
**Key scenes/beats (alternating):**
- **Festival:** first new wine offered, garlands, Grata's thermopolium overflowing, Aelia sticky with must.
- **Packing:** what goes in the bag: the tape, the camera, the notebook and the tables, Fenn's Zippo and dime (his coverless paperback stays on the shelf). The watch on her wrist.
- **NON-NEGOTIABLE.** Frame 36, written as an act and never as a tag. She rewinds the roll, takes it out of the camera and puts the canister in the bag; the camera goes back on the shelf.
- **NON-NEGOTIABLE.** She gives Grata money to visit her sister in Nuceria "the day after tomorrow, and stay the month." Grata takes the money and laughs. Whether she goes is not resolved here. (She does not go: Ch.40 finds her in her shop. It is her choice, never explained.)
- Felix with the boat. Valens's figs are not mentioned (the obsession is spent).
- A quiet image ends the chapter.
**Progressive structure:**
- Builds on Ch.37: the plan, the days.
- Adds: the people she can't save, and the people she tries to.
- Opens toward Ch.39: five days later.
**Theme presence:** home as an ordinary day in a city.
**Character chaos moments:** none forced. Let joy be uncomplicated.
**Subtext layer:** Grata's laughter at the travel money is really her refusing to ask why.
**Shareable moment:** —
**Reading speed:** slow, festive, sensory.
**Word count target:** 8,000
**Writer warnings:** **The highest foreshadowing-risk chapter.** No "last" tagging of anything: not the last festival, not the last ordinary day. Mara knows the date and may feel it in scene; the narration must not reach past the 19th. The final frame is shown as an act, not a symbol. No aphorism.
**Beat subversion:** *Genre beat:* the eve of catastrophe, drenched in ominous signs. *Subversion:* it is the happiest day in the late book. The one "sign" is a wisp of cloud she cannot be sure of.

## Chapter 39: Noon
**Ledger:** In medias res (internal shape: *the cloud first, then the morning that led to it*) · open: mid-dialogue → `dialogue` · end: short punch → `punch` · 4,000 · dialogue 20–30% · theme present · 3 breaks · gear low
**Dateline:** *Pompeii · 24 August, AD 79* · **TURNING POINT (~93%)**

**Premise:** At about one in the afternoon the column rises over the mountain, shaped like an umbrella pine. People in the street applaud, and the family begins to move.
**Function in arc:** The detonation. The clock is in hours.
**Emotional anchor:** Aelia saying "Mama, look," the pine-shaped cloud, the noon sun going brown.
**Emotional surprise:** people in the street *applaud* the cloud.
**Opening strategy:** mid-dialogue, Aelia's line.
**Key scenes/beats:**
1. **NON-NEGOTIABLE.** The column in Pliny's terms, through Mara's eyes and ears: the sound, then the height.
2. Backfill: the ordinary morning, bread and Grata.
3. **NON-NEGOTIABLE.** The family moves: bag, children, Valens. The streets.
4. **NON-NEGOTIABLE.** The first pumice falls, light as bread. A ≤7-word last line, as a single-sentence closing paragraph.
**Progressive structure:**
- Builds on Ch.38: five days on.
- Adds: it has begun.
- Opens toward Ch.40: the falling stone.
**Theme presence:** —
**Character chaos moments:** none.
**Reading speed:** fast; the column held for one long sentence.
**Word count target:** 4,000
**Writer warnings:** Use Pliny's real details (the umbrella-pine shape, the dark), not spectacle verbs. No lyricism. Voice under pressure begins. No aphorism.
**Beat subversion:** *Genre beat:* mass panic at the first sign. *Subversion:* the crowd applauds a marvel. The panic is one woman's, and it is quiet.

## Chapter 40: Pumice
**Ledger:** Chronological (internal shape: *aftermath-first*, opens after the roof falls and never shows it falling) · open: flat statement (I) → `I-punch` · end: long fade → `long-fade` · 5,800 · dialogue 15–25% · theme present · 4 breaks · gear low
**Dateline:** *Pompeii and the river mouth · 24 August, afternoon into night*

**Premise:** Through the afternoon of falling stone the family reaches the river mouth, where the boat cannot come in, and then turns back for the tombs and the door. (This is the Ch.37 plan's own order: boat in daylight, door at night.)
**Function in arc:** The backup fails, for real historical reasons (Pliny's choked shore and onshore wind). Felix's fate is left open.
**Emotional anchor:** pumice stones, light as bread, rattling on roof tiles; the boat unable to come in.
**Emotional surprise:** Lucius is delighted by stones that float on the water.
**Opening strategy:** "I carried Aelia." (≤8 words, starting with "I.")
**Key scenes/beats:**
1. Aftermath-first: Grata's roof has already fallen in. She is alive and refuses to leave her shop.
2. **NON-NEGOTIABLE.** The river mouth: the sea heaving, rafts of pumice, wind against them. Felix shouting from the boat.
3. **NON-NEGOTIABLE.** Felix takes the boat out to try for Stabiae and come back. He is lost to sight in the murk. **His fate is not resolved.**
4. **NON-NEGOTIABLE.** Lucius and the floating stones.
5. The turn back through the dark afternoon to the Nuceria Gate. A long fade.
**Progressive structure:**
- Builds on Ch.39: the pumice begins.
- Adds: the backup gone. Only the door is left.
- Opens toward Ch.41: night at the tombs.
**Theme presence:** home narrowed to four people.
**Character chaos moments:** none forced.
**Reading speed:** fast and heavy.
**Word count target:** 5,800
**Writer warnings:** Do not show Grata's death; she is alive and stubborn when they leave. No "I never saw Felix again" (BANNED foreshadowing). No gore, harshness ~7. Voice under pressure: the asides are gone.
**Beat subversion:** *Genre beat:* the daring escape by sea. *Subversion:* the sea refuses them. The boy takes the boat out alone, and the family walks back toward the danger because that is where the door is.

## Chapter 41: The Tomb Road
**Ledger:** Single-scene (internal shape: *one night in one tomb*) · open: long sensory spiral → `long-spiral` · end: spoken line → `dialogue` · 4,200 · dialogue 30–40% · theme present · 0 breaks · gear mid
**Dateline:** *The Nuceria Gate tombs · night, 24–25 August, AD 79*

**Premise:** Sheltering through the night in the niche of the tomb with the painted door, among strangers doing the same, the family waits, and Valens winds the watch.
**Function in arc:** The held breath before the door. The family close together in the niche, with nothing to do but wait.
**Emotional anchor:** the watch wound in the tomb's niche by lamplight.
**Emotional surprise:** a stranger shares figs and complains about his landlord.
**Opening strategy:** the night in one long sentence: the hiss of falling stone, the lamp, the smell of sulphur and wet wool.
**Key scenes/beats:**
1. Strangers in the neighboring tombs. The fig-sharing man and his landlord grievance.
2. **NON-NEGOTIABLE.** Valens winds the Seiko. No comment from anyone.
3. Mrs. Dunphy surfaces (third mutation: Mara is no longer sure it was long division).
4. Aelia's delight at the falling stones (FLEX: she may call it snow, because Mara once told her about Philadelphia). Lucius gives her the knucklebone to hold so that she will stop grabbing the lamp; she keeps it (the hand-off that Ch.44 depends on).
5. **NON-NEGOTIABLE.** A hand at the threshold: the painted door is cold in the hot night.
6. A spoken line ends the chapter, plain and in the present scene.
**Progressive structure:**
- Builds on Ch.40: the turn back.
- Adds: the door waking.
- Opens toward Ch.42: it opens.
**Theme presence:** home as a niche in a tomb, with everyone in it.
**Character chaos moments:** Mrs. Dunphy (3 of 3). Valens's onion memory (last).
**Subtext layer:** the stranger's landlord complaint is the only way anyone there can talk about tomorrow.
**Shareable moment:** —
**Reading speed:** slow, close.
**Word count target:** 4,200
**Writer warnings:** No significance-tagging for the watch, the children or anything else. No farewells in advance. Nobody says goodbye before the door. Valens's "love" is NOT spent here.
**Beat subversion:** *Genre beat:* the family's tearful last-night confessions. *Subversion:* nobody confesses anything. A stranger complains about his landlord and the watch gets wound.

## Chapter 42: The Door
**Ledger:** Fragmented (internal shape: *seconds in shards*) · open: flat statement of fact → `short-punch` · end: short punch → `punch` · 2,400 · dialogue 10–20% · theme present · 6 breaks · gear low
**Dateline:** *before dawn, 25 August, AD 79* · **TURNING POINT (~98%)**

**Premise:** The door opens. Mara's hand goes through into a cool night smelling of diesel and pine, and her children's hands meet painted plaster.
**Function in arc:** The central tragedy. The law of the doors is discovered, not explained.
**Emotional anchor:** her hand in cool night air smelling of diesel and pine; Aelia's hand flat against painted plaster.
**Emotional surprise:** the door *works*.
**Opening strategy:** "The cold came first." (≤8 words; the opening paragraph may be a single sentence.)
**Key scenes/beats (shards):**
1. **NON-NEGOTIABLE.** The seam of cold and quiet. Through it: a sodium streetlamp, a chain-link fence, a cicada, the distant whine of a scooter, the smell of diesel and pine. 1998, or near it.
2. **NON-NEGOTIABLE.** Her hand goes through.
3. **NON-NEGOTIABLE.** The children's hands and Valens's meet painted plaster where hers met air. Render it **without a parallel triad**: Aelia's palm flat and pressing; Lucius trying once, exactly as told; Valens last, with his shoulder, in a sentence built differently from both.
4. The law, understood without anyone stating a rule. **The beat must work with no phrase at all;** the plaster under three hands is the discovery. If "the one it brought" appears, it is incidental (allowlisted use 2 of 3): a limit, in Mara's present thought, never load-bearing and never a button.
5. A ≤7-word last line, as a single-sentence closing paragraph.
**Progressive structure:**
- Builds on Ch.41: the door waking.
- Adds: everything.
- Opens toward Ch.43: what she does.
**Theme presence:** the two homes, side by side, with one door between them.
**Reading speed:** very fast.
**Word count target:** 2,400
**Writer warnings:** The modern side is glimpsed, not toured. Do not make it legible as the Pompeii excavations; a fence and a lamp are enough. No lyricism, no anaphora triads. Voice under pressure at full strength, which is NOT a list.
**Beat subversion:** *Genre beat:* the portal fails at the crucial moment. *Subversion:* it works perfectly, for her. The failure is everyone else.

## Chapter 43: What She Did
**Ledger:** Single-scene (internal shape: *one choice, made with the hands*) · open: an object → `narrative` · end: quiet image → `quiet` · 3,000 · dialogue 25–35% · theme present · 0 breaks · gear low
**Dateline:** *before dawn, 25 August, AD 79*

**Premise:** Valens begs her to go and means it. Mara sends her father's voice, the film and the notebook through the door to the other side, and stays. (The narration never asserts the year beyond it. Ch.42's "1998, or near it" is the only stance-safe phrasing; the doors do not deliver to matching dates.)
**Function in arc:** THE CHOICE, as active agency. The door is a live exit she turns from, by her own hand, in calm.
**Emotional anchor:** the tape, the film roll and Fenn's notebook going through the door; her hand empty.
**Emotional surprise:** calm, not anguish, at the moment of choosing.
**Opening strategy:** an object. The microcassette in the old sock in her hand (9–27 words, so `narrative`).
**Key scenes/beats:**
1. **NON-NEGOTIABLE.** Valens begs her through: the children's future is gone, so let *her* have one. He says *love*, once, plainly. It is not a payoff line, and the scene does not pause on it.
2. **NON-NEGOTIABLE.** Her choice, in actions: the microcassette, the film canister and Fenn's 1968 notebook (his tables and her tremor figures in its back pages), with his Zippo and dime, one by one, through the seam to the other side. Fenn's ORIGINAL tables go with them, folded inside the notebook (she copied his key figures into the notebook in Ch.36, so nothing stays behind that she needs). Fenn's things go home without him. She does not explain.
3. **NON-NEGOTIABLE.** She keeps the watch on her wrist. She lifts Aelia.
4. **NON-NEGOTIABLE.** The seam closes, and she watches it close without mending it open.
5. A quiet image: her empty hand on Aelia's back.
**Progressive structure:**
- Builds on Ch.42: the law.
- Adds: the choice.
- Opens toward Ch.44: dawn.
**Theme presence:** answered by action, never stated. Home is the people she stays beside.
**Character chaos moments:** none.
**Subtext layer:** Valens's begging is the most loving thing he says. Her refusal is the most loving thing she does. Neither names it.
**Shareable moment:** #6 (she throws her father's voice through into her own century and stays).
**Reading speed:** slowed time; very short sentences.
**Word count target:** 3,000
**Writer warnings:** NO speech explaining her choice. NO aphorism. NO "I chose them" thesis line; the actions carry it. The door must be clearly usable, with nothing preventing her. Her calm must not read as numbness or as the all-or-nothing distortion. It is acceptance of a seam.
**Beat subversion:** *Genre beat:* the agonized last-second decision, a cry and a leap. *Subversion:* there is no leap. She takes the things out of her bag one by one and puts them through like a woman mailing letters.

## Chapter 44: Second Dawn
**Ledger:** Chronological (internal shape: *walk*, out along the road) · open: scene-setting (time) → `scene-set` · end: **PLAIN STOP (the book ends)** → `punch` · 1,500 · dialogue 0–10% · theme present · 1 break · gear low
**Dateline:** *the Nuceria road · morning, 25 August, AD 79*

**Premise:** At first light the family walks out along the road where the dead go out of the city, Aelia's fist closed on a knucklebone. Then the light comes.
**Function in arc:** The residue chamber, and the end, in AD 79 with no coda.
**Emotional anchor:** the knucklebone in Aelia's fist; the road; the light.
**Emotional surprise:** none designed. The chapter is the residue (foundation §4c).
**Opening strategy:** a time opener the detector recognizes, e.g. "By dawn…" (not "By first light…", which does not compute as `scene-set`).
**Key scenes/beats:**
1. Walking the road between tombs, out of the city. The re-read works through the road and the place; **the chapter must land with the allowlisted phrase absent.** If used, it is incidental (use 3 of 3).
2. Valens carrying Lucius; Mara carrying Aelia; the knucklebone; the watch ticking on her wrist.
3. **NON-NEGOTIABLE.** The surge, rendered as light, heat and then silence in no more than three sentences, with no gore.
4. **NON-NEGOTIABLE.** The past tense runs up to the last moment and **stops**. The final sentence has ≤7 words, as a single-sentence closing paragraph. It is concrete (a hand, warmth), not a verdict.
**Progressive structure:**
- Builds on Ch.43: the choice.
- Adds: nothing. It ends.
**Theme presence:** answered by the image alone.
**Reading speed:** slow, then over.
**Word count target:** 1,500
**Writer warnings:** **NO modern coda, no excavators, no casts, no "they would be found."** No aphorism, no summing-up, no central question restated. No final-line wisdom. The narrator's horizon is this moment, so she cannot know what follows and does not say.
**Beat subversion:** *Genre beat:* the final speech or flash of meaning before death. *Subversion:* a woman walks down a road holding her daughter, and the book stops.

---

## OUTLINE QUALITY CHECKS (architect self-audit)

1. **Progressive, not parallel.** Read only the Premise lines: each one depends on the last (cave shut → belonging → money → letter → yard → fight → Oracle → night → bargain → …). They cannot be reordered. ✓
2. **No orphans.** Every chapter builds back and opens forward. The no-pull chapters (10, 31, 34) open nothing *deliberately*, and the next chapter starts on its own. ✓
3. **Anchor variety.** Auditory (1, 13, 15, 32, 39), tactile (7, 23, 42), gestural (6, 11, 18, 24, 28, 41), visual (5, 8, 19, 38), verbal (13, 15, 25). No three consecutive anchors share a sense. ✓
4. **Chaos distribution.**
   - Mara: teeth full 7/20/31, glancing 2/5/15/24 (Ch.24's midwife is the only introduction-by-teeth); all-or-nothing 1/5/7/9/20/29/33; Dunphy 7/24/41; breaks 6 (plot-earned)/20/22 (unearned).
   - Valens: figs 11/20/34; mind-reading 6/11/19/21/28/37; onion 12/22/23/32/41; the mime 29.
   - Fenn: Phillies 25/26/29/35; automat 25/27/35; rage 26 only (a one-off, never a bit).
   - Secondaries each have an own-life scene: Kallia 10, Plautia 16/22, Felix 28, Grata 31. ✓
5. **Opening diversity.** See the ledger: there are 12 distinct opening moves, and no mechanical sig appears three in a row. ✓
6. **Breathing room.** Theme RECEDES in Ch.4, 28, 31 and 34. ✓
7. **Length variance.** 1,500–8,400 (5.6×). Short punches: 4, 10, 14, 18, 30, 42, 44. Long immersions: 5, 8, 13, 15, 19, 20, 25, 32, 38 and others. ✓
8. **Structural diversity.** Seven approaches, none consecutive, max 25%. ✓
9. **Secondary character scenes.** Ch.10 (Kallia), 16/22 (Plautia), 28 (Felix), 31 (Grata). ✓
10. **Originality engineering.** Every chapter has a designed beat subversion above. ✓

**NON-NEGOTIABLE vs FLEX.** Beats marked NON-NEGOTIABLE carry canon, the re-read architecture or the ledger. Everything else may flex. **The Writer should follow a strong impulse** in: Ch.8 (the women's songs), Ch.20 (which repairs), Ch.29 (the Saturnalia business) and Ch.38 (festival texture). In those four chapters the outline is deliberately loose.

**Heat map:** Ch.15 (first union) · Ch.23 (key turn) · Ch.34 (late unshadowed joy). Yearning only in Ch.11 and 16–18. **None from Ch.39 onward.**
