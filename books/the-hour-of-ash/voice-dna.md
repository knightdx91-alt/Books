# Voice DNA — *The Hour of Ash* (run 2, architect v4, voice mode)

> **What this is.** The executable, enforceable voice spec. The **Writer** writes FROM it. **Dialogue
> Polish** and **Hook Craft** check AGAINST it. The **Disruptor** cuts down to its budget (§4). The
> **Editor**, **Continuity Guardian** and **Evaluator** hold the line with it. It consolidates and
> expands `foundation.md` §6 (voice, narrating stance, voice under pressure, tic roster, heat) under
> the author's binding laws.
>
> **Writer's read order for every chapter:** §8 (your ledger row) → §0 → §1 → the `character-bible.md`
> entries for everyone who speaks in the chapter → the voice-bank sample matching the row's gear and
> approach (§6) → draft → §4 self-check.
>
> **Binding laws this document is built around:** NO FORESHADOWING (book-wide 0) · ANTI-PREDICTABILITY
> (the ledger) · RETIRED PIPELINE REFLEXES · **NO TICS (tic budget ZERO, narrator included)**.
>
> **Hard numbers (style gate):** explanatory simile ≤4.0/1k · em-dash ≤4 per chapter ABSOLUTE ·
> foreshadowing 0 · no new cross-chapter repeated phrase · allowlist ≤5 entries, each capped at 3.

---

## §0 POV, TENSE, NARRATING STANCE, AND THE NO-FORESHADOWING RULE

### POV and tense
**First person, past tense, Mara Reyes, single POV, from the first line of Ch.1 to the last line of
Ch.44.** There is no second POV, no close-third coda, no modern frame and no excavation epilogue.
Other voices reach the page only as **dialogue** or as **documents Mara is reading** inside collage
chapters (Fenn's notebook, letters and tables; Delphic inscriptions; Pompeian wall-writing; public
notices; Ariston's letter). A document keeps its own writer's voice (see `character-bible.md`) and its
own tense.

### The narrating stance: "the telling walks beside the told" (foundation §6a)
**Mara's knowledge horizon is the moment being narrated.** The past tense is a storytelling
convention, not a vantage point. There is no older Mara, no survivor looking back, no telling from a
shelter in the dark, and no "years since." When she narrates Ch.12 she does not know Ch.13. Six
consequences, which the Writer applies sentence by sentence:

1. **She cannot reach forward, because there is nowhere forward to reach from.**
2. **Past-facing reflection is free.** Everything before the narrated moment belongs to her: 1998, her
   father, Mrs. Dunphy, last winter in Delphi, the 1979 exhibition of the plaster casts, seen at fourteen, the Forum she
   walked as a student in 1991. She may remember, compare and judge backward.
3. **Her historical knowledge is in-scene feeling, not foreshadowing** (rules below).
4. **No narrating present.** Present tense appears only inside dialogue and documents. General
   reflections are cast in the past: "Grief, in my experience then, came at odd hours."
5. **Weight goes into objects, gestures and present sensation**, never into a sentence of significance.
6. **The ending works because of the stance.** The last chapter's past tense runs up to the last moment
   and stops. Nobody was ever telling it from afterwards.

**The Writer's test for any sentence of reflection:** *could Mara have thought this at that exact
moment, knowing only what she knew then?* If not, cut it.

### ★ THE NO-FORESHADOWING RULE (author ruling 2026-09-28; HARD; book-wide target **0**)
The narrator never gestures forward to an outcome the story has not reached. **Banned forms**, in five
families. The list is illustrative; any sentence that does the same job is banned too.

**A. Foreknowledge intrusion.** "I did not know yet (that)…", "I did not yet know…", "I would learn /
come to / discover / understand / realize / find out…", "as I would later learn", "it would prove…",
"it would turn out…", "little did I know", "had I known", "if I had known then", "I could not have
known", "one day I would…", "later, I would…", "years later…".

**B. Significance-tagging by future loss.** "the last time I would…", "the last [X] I would (see / be
given / hear)", "for the last time", "I would never [X] again", "the first of many", "it was the
beginning of (everything)", "the end of something", "the happiest day of my life", "a day I would
remember", "I wanted to keep it forever" (as a narratorial tag), "one more ordinary day".

**C. Survival or outcome implication.** "in (all) the years since", "over the years that followed",
"the years to come", "the man I would marry / love / lose / become", "my future husband", "the house
where my son would be born", "I never saw him again", "that was the last I saw of…", "it would mean a
great deal later".

**D. Narrating present.** "even now", "I still remember", "to this day", "I can see it still", "looking
back", "in hindsight", "I have often thought since", "I think now", or any address to a reader from a
time after the scene.

**E. Narrator irony about the ash.** Any line that links her trade (conservation, preservation) to
what the ash will do; any mention in Part Two narration of casts, excavators, archaeologists finding
things, or "they would be found." This irony belongs entirely to the reader.

**What the gate catches mechanically.** `tools/style_check.py --max-foreshadow 0` (the default for this
book) scans **narration AND dialogue** for: "little did [I/we/she/he/they] know"; "[pronoun] would
(soon / later / one day) come to / learn / discover / understand / realize / find out"; "would (later)
prove / turn out"; "as [pronoun] would (later) learn / discover / come to"; "the last [X] [pronoun]
would"; "for the last time"; "in/over (all) the years since / that followed / to come / after"; "would
mean (a great deal / much / everything) later"; "did not yet know (it / that it / how much)"; "the
(man / woman / girl / boy) [I / she / he] would (marry / love / become / lose)". **The gate is literal:**
an innocent conditional such as "she would understand if I explained" still trips it. Rephrase ("she'd
see it", "she might understand"). Fenn must say "thirty-four years" or "since I landed," never "in all
the years since." Anything the gate misses, the Evaluator and the Continuity Guardian catch by reading.

### What is KEPT (and is not foreshadowing)
1. **Past-facing reflection.** See consequence 2 above.
2. **Present-scene dread.** What she fears, in the scene, now: the sound of a man's breath, a child's
   heat, a door that might not open.
3. **Her own knowledge of AD 79, as a present thought in a present scene.** This is the book's most
   honest dread engine. Rules of use:
   - **Ch.1–12:** she has no reason to think of Pompeii. In Ch.5 she dates the year (AD 70, Vespasian)
     and does **not** jump to 79.
   - **Ch.13:** only the word. Theano says "Pompeii." The horror arrives in Ch.14.
   - **Ch.14:** the night she knows. The 1979 exhibition of the plaster casts, seen at fourteen, is a memory of what she saw then, told as memory.
   - **Ch.15–35:** the year may surface as a present thought **at most once per chapter** ("Seventy-nine,
     I thought."), worded differently each time. **Never in Ch.34.** Never as narration of her own fate.
   - **Ch.36 on:** she reckons openly. The date (24 August, from Pliny's letters as she remembers them)
     is present calculation. She still never narrates her own outcome.
4. **The reader's own Vesuvius knowledge.** The page supplies period detail; the reader supplies the
   irony.

### The mountain rule
The mountain is described as it looked to people then: green, vine-terraced to the shoulder, one broad
summit, villas, somebody's kitchen smoke. It appears only when the scene puts it in her eyeline.
**Banned descriptors for the mountain:** looming, brooding, sullen, menacing, ominous, threatening,
waiting, patient, watchful, crouching, slumbering, sleeping, "sleeping giant," "like a beast," and any
personification at all. Before Ch.39 the mountain does nothing on the page, and that is where the
dread lives (sample-13).

### Weight carriers (instead of significance sentences)
The watch and its winding · the film counter and the frames she chooses · the microcassette in its
sock · the knucklebone · Fenn's Zippo · a hand on a threshold (cave rock, painted plaster) · bread,
lamps, figs and other present sensation. **Each is rendered in fresh words every time it appears**
(§3b): the situation repeats, the sentence never does.

---

## §1 GLOBAL NARRATIVE VOICE (how the narration sounds when no one is speaking)

| Setting | Spec |
|---|---|
| **Vocabulary level** | **6/10.** Literate, sensory, period-textured, never antiquarian-showy. A good general reader never needs a dictionary twice in a page. |
| **Sentence rhythm** | **Mixed.** Book-wide target (Outlander, §7): median ~15 words, ~15% at ≤6 words, ~7% at ≥35. Each chapter's **gear** comes from its ledger row: low ≈ median 9–12, mid ≈ 14–16, high ≈ 17–20. Long spirals belong to wonder and intimacy; short declaratives to fear. |
| **Punctuation** | **Semicolons (~3/1k)** where the AI habit reaches for an em-dash. **Em-dash ≤4 per chapter, absolute;** aim for 0–2, and spend them only on true interruption in dialogue. Ellipses ≤~1.5/1k, for trailing speech, never as narration mood. Spaced en-dashes are not a loophole: treat them as em-dashes. |
| **Formality** | Conversational-to-measured. A modern American intelligence inside a period surface, producing friction rather than lecture. |
| **Humor** | Dry and frequent in calm chapters; defensive; often at her own expense. It **vanishes entirely** under real fear (level 1 of pressure below). |
| **Emotional register** | Open but earned; restraint is the default, so the breaks land. |
| **Simile** | **Characterizing only**: it makes you *see* a thing or *smile* ("the face of a good leather handbag, creased in all the places that had been useful"). Never **analytical**: it never interprets a feeling. Aim ≤3/1k; gate ≤4/1k. |
| **Period material** | **One or two specific period materials per scene** (garum, red-slip ware, birch tar, a lamp's soot line, terracotta roof tiles, burnt-horn tooth powder, lead fixings, the carbonized ridge on a loaf scored into eight). Never generic "ancient" atmosphere. |
| **Latin and Greek** | Sparingly, *italicized*, made clear by context, **never glossed in parentheses or an aside**. Unglossed entirely at pressure level 3. |
| **Spelling** | **US English** (`grammar_check.py` runs LanguageTool en-US): color, labor, gray, molded, favor, center. *Note: the voice-bank samples use some UK spellings ("colour," "moulded," "labour"). Read them for register only; spell US.* |
| **Modern reference** | Late-1990s only (answering machine, Pentax K1000, Discman, payphones, SEPTA, film you send away to develop). Nothing after spring 1998, ever. Modern idiom appears only in Mara's private comparisons and in her English with Fenn, never in narration of fact. |

### Distinctive features
1. **The conservator's eye.** Her attention goes to what a thing is made of, how it was joined, where
   it will fail and how it was mended, and she reads people the same way (their hands, the repaired
   places in them). **This attention belongs to the narrator alone.** No other character notices
   materials or joins (see the character bible's bleed guards).
2. **The dry aside.** One clause wanders sideways into a joke or a hypothesis, then comes back.
   Density guide: calm chapters ~2–4 per 1,000 words, mid-tension chapters ~1–2, none under pressure.
   **Vary its form every time** (a subordinate clause, a following short sentence, a semicolon turn);
   it never settles into a formula such as "which, I thought, …" or "the conservator in me…".
3. **Bodily realism punctures grandeur.** Hunger at the arrival, the midwife's teeth during labor, sore
   feet on the Sacred Way. The body's comedy keeps the romance human.
4. **Friction, not lecture.** Every period fact is something Mara *uses or suffers*. If she merely
   knows it, cut it.
5. **Her private comparisons from 1998.** Rotate their source domains: the lab, Philadelphia streets
   and weather, her father's house, school, kitchen and body, 1990s objects. No single domain supplies
   more than about half of a chapter's comparisons, and **no comparison is used twice in the book**.

### Anti-patterns (NEVER)
Analytical simile · metacognitive narration ("I realized that I was realizing," "I found myself
thinking") · emotional-temperature reports ("a wave of grief washed over me") · info-dump history ·
Latin glossed in parentheses · modern slang in narration of fact · lyrical escalation at a climax ·
tour-guide catalogues of a place · a period detail Mara neither uses nor suffers · **every retired
reflex:** retrospective significance-tagging, define-by-negation openers ("Not X. Not Y. It was Z."),
anaphora triads, performed-candour lines, an object or device used as a scene button,
chapter-closing aphorisms, proverb-as-button.

### Dialogue conventions (all characters)
- All speech is rendered in English. **The register signals the language.** Ancient speakers use **no
  modern idiom** ("okay," "kids," "guys," "deal with it," "stressed," "process this," "hang out") and no
  modern units in their mouths (no "minutes" or "seconds"; hours, watches of the night, the time it
  takes to boil a pot). Their oaths are period oaths, used rarely (by Hercules, by Castor, by the gods,
  Apollo's name in Delphi). **Only Fenn, and Mara when speaking English, use modern idiom.**
- Tags: "said" by default, "asked" when needed. **No adverbs in tags.** No "growled," "hissed,"
  "purred." Action beats come from the speaker's physicality axis in the bible, but **no character
  gets the same beat twice in a chapter**, and no beat becomes a signature.
- **Address forms:** use names. No character has a recurring pet name or epithet for another
  (no "girl," "little one" or "my dove" as a hallmark). An endearment may occur, varied, never as a
  refrain.
- Dialogue share follows each chapter's ledger band (§8).

### VOICE UNDER PRESSURE (foundation §6b; no cataloguing device)
When Mara is overwhelmed the prose **deflates**. It does three things, in order of severity:

1. **The asides die.** The sideways clause and the 1998 comparison disappear. Their absence is the tell.
2. **She narrates only what hands and bodies do.** Plain verbs, physical sequence, no interpretation:
   "I put the lamp down. I picked it up again. I went to the door." Sentences shorten toward 4–8 words
   and paragraphs thin out.
3. **Unglossed and unattributed.** At the extreme, Greek and Latin stop being made clear, speech stops
   being tagged, and **the senses narrow to one**, usually sound.

**What it is NOT:** a list, an inventory, a catalogue, a condition report or a packing list (the prior
run's "catalogue under stress" is retired as a device); soaring lyricism; a switch into present tense;
a cascade of ellipses; stacked one-word paragraphs that make an anaphora triad.

**Two neighboring states that must not be confused with breaking:**
- **Heat** (Ch.15, 23, 34): the asides go quiet, but the **senses widen** and the sentences lengthen
  and slow. See §5.
- **Steadiness** (the designed calm of Ch.36, 43 and 44): no asides, but **complete, unhurried
  sentences, one deliberate act per sentence, speech tagged again, foreign words made clear again.**
  This is acceptance, not numbness and not breakage. The returning tags are how the reader feels the
  difference from Ch.42.

**Rehearsal and climax map (the levels are trained before they pay off):**

| Ch | State | What happens to the voice |
|---|---|---|
| 6 | level 1 (brief) | The scream at the cave wall: the asides vanish for a paragraph, then return when he laughs. |
| 9 | level 1 (brief) | Watching Valens read the notice: one plain observed action, no comment. |
| **12** | **level 2: full rehearsal** | The fight. Bodies and hands only, the lens cap, the goat rope (sample-05). Asides return at the stream. |
| 17 | levels 1–2 | Celer in the colonnade (level 1); the run for Lechaion (level 2). |
| **24** | **level 3: full rehearsal** | Labor. Latin unglossed, speech untagged, the senses narrowed to sound (sample-06). |
| 30 | level 1 | The tomb after the tremor: warm plaster, nothing; no aside on the walk back until the last line. |
| **32** | **levels 2–3** | The fever night. Hands and breath; sound only in the worst hour; *amoxicillin* as one useless word. |
| 36 | steadiness | The arithmetic. The designed surprise is calm, so the voice does not break. |
| 39 | levels 1→2 | Noon. The column is held for one long sentence, then the voice drops gear. |
| 40 | level 2 | Pumice. The asides are gone; Lucius's delight is reported plainly. |
| 41 | eased level 1 | The night in the tomb. Tagged speech returns, mid gear, a held breath; still no asides. |
| **42** | **level 3, maximum** | The door. Shards, one sense at a time, no list (sample-07). |
| **43** | **steadiness** | The choice. Calm, complete sentences, each one a single act of the hands. |
| 44 | steadiness → stop | The road. Plain past tense; the last sentences narrow to light, heat and a hand, and stop. |

**When the voice opens** (high gear, long spirals, full asides): Ch.3, 5, 7, 8, 15, 19, 22, 27, 29,
33, 34, 38. Lyricism lives here, in calm, and nowhere near the climax.

---

## §2 PER-CHARACTER VOICE CARDS → `character-bible.md`

**The cards live in `character-bible.md`, not here.** That file holds one card per named character,
covering all four axes, every card's tic line reading "none — distinguished by <axis>", plus the NO-TICS
section, the retired/at-risk phrase list, the cast-wide matrix, the guide to unnamed walk-on roles,
and the cover-the-name test. **It is a living document:** the Writer adds an entry the moment a new
named character first appears on the page, *before* finalizing that chapter. Dialogue Polish writes
from the cards. The Evaluator audits against them.

---

## §3 VOICE DIFFERENTIATION MATRIX (cover-the-name, pre-solved)

### Principal pairs (≥3 independent markers each)

**Mara ↔ Valens** (the most-heard pair; Ch.37 is the highest-dialogue chapter in the book)
| Axis | Mara | Valens |
|---|---|---|
| Attention | materials, joins, mends; reads people by hands and teeth | footing, exits, weather, the moods of animals and men; reads bodies before faces |
| Syntax | qualifies, stacks clauses, answers a question with a question | short, level declaratives; rarely subordinates |
| Questions | curious; asks *why*, including about feelings | practical (where, how far, who saw); asks *why* only of plans, never of feelings |
| Figurative speech | compares freely, wry | **never uses a simile or comparison in speech** |
| Humor | verbal, dry, deliberate | deadpan literalism, mostly unintended |
| Evasion | "love" in narration until Part Two; her father's death; bravery | the men he killed; his fear; "love" until once in Ch.43; any grievance about the frame |
| Hands | **inspection and repair of made things** (a thumbnail along a seam) | **maintenance of gear and animals** (strap, hoof, wick), always a different object |

**Mara ↔ Fenn** (the only two English speakers; the pair most at risk of collapsing)
| Axis | Mara | Fenn |
|---|---|---|
| Era idiom | 1998 American | frozen 1968 American (§ bible pool), no item used more than twice book-wide |
| Attention | how things are made; people's hands and teeth | systems and patterns (tides, tremors, star tables, door timing); sees people last |
| Syntax in English | precise, clipped in speech, semicolon spirals in narration | runaway "and…and" chains when excited; four-word fragments when tired |
| Tense orientation | after Ch.25 she will not put Fenn's *date* in the future tense until Ch.36 (hoping for an earlier opening, and arguing whether it would take the children, are allowed) | talks about going back in a confident future tense ("when I get back") until the day he dies |
| Evasion | her father's death; love; bravery | his sister's name (until Ch.35); fear of dying here; never calls anywhere here "home" |
| Body | steady hands, touches surfaces | ink-stained fingers, a left-hand tremor, the Zippo, fast pats |
| Breaks | weeps or laughs at the wrong moment | rages at words that moved on without him |

**Valens ↔ Fenn** (the two exiles; the Saturnalia baseball scene puts them side by side)
| Axis | Valens | Fenn |
|---|---|---|
| Volume | spare; silence between statements | torrential when awake to a subject |
| Attention | bodies, ground, animals | systems, stars, dates |
| Register | Latin-plain, concrete nouns | American slang in English; perfect, formal Greek |
| Time orientation | the present: the next step, the next hour | the future (79) and the past (1964) |
| Evasion | his past violence | his sister |
| Stillness | still; hands find work | fidgets (the Zippo turned over and over) |

**Mara ↔ Kallia** · Mara is curious and verbal; Kallia answers with tasks. Mara's attention goes to how
a thing is made; Kallia's to who will carry it and clean it. Mara touches surfaces to read them;
Kallia never stops working and touches objects, not people.

### Nearest-neighbour contrasts (everyone who speaks in 2+ scenes)
| Character | Sharpest distinguisher | Nearest neighbour → contrast |
|---|---|---|
| **Mara** | notices how things were made and mended; qualifying, spiralling syntax | Fenn → she is precise and 1998; he is runaway and 1968 |
| **Valens** | never compares, never asks *why* of a feeling; short level statements | Philokrates → both calm men at bedsides; Valens never explains, Philokrates explains everything, kindly |
| **Fenn** | frozen-1968 English in runaway chains; sees systems before people | Halloran → both American(-ish) academics of a kind; Fenn is boyish slang and certainty, Halloran is euphemism and paperwork |
| **Kallia** | answers a question with a task; attention to labor (who carries, who cleans) | Theano → both Phocian women; Kallia never talks about herself, Theano talks about nothing else (knees, priests, the god as an employer) |
| **Theano** | grumbling about her own body and the priests; never comforts, never explains | Kallia → see above; Theano sits, Kallia never sits |
| **Felix** | stacks questions before anyone answers one; boasts; always moving | Lucius → Felix asks three fast questions and boasts; Lucius asks one grave question and waits |
| **Plautia** | formal, subordinate-heavy Latin broken by sudden blunt questions | Celer → both aristocratic; her formality breaks into bluntness, his never breaks |
| **Celer** | genial first-person plural ("we"), conditionals, never raises his voice, never says *wife* | Plautia → see above; Celer uses contractions and warmth, Plautia uses neither |
| **Grata** | tells you about yourself, never asks a personal question; every sentence a sale or a complaint | Felix → both fast Pompeian talkers; Felix asks, Grata tells. Kallia → Kallia is few words and imperatives; Grata is a torrent, and touches arms |
| **Lucius** | grave, literal, whole sentences; takes adults at their word | Aelia → he is still and asks; she grabs and exclaims |
| **Aelia** | exclamations, imperatives, sensory nouns; delight where adults see danger | Lucius → see above |
| **Halloran** | permit-speak and euphemism; never says "died" | Emilio → both archaeologists on the phone or tape; Emilio performs warmth and never names a date, Halloran gives dates and deadlines and no warmth he can't apologize for |
| **Emilio** (tape and memory) | warm, performing, locates himself by place; never commits to *when* | Fenn → both men who left; Fenn gives dates (wrongly), Emilio never gives one |
| **Irene Szabo** | no contractions; verdicts on authenticity; no condolence | Grata → both shopkeepers; Szabo sells by contempt in few words, Grata by flood and flattery |

**No two characters share a sharpest distinguisher, and no character carries a device.** The full card
for each, with the cover-the-name test run against the finished bible, is in `character-bible.md`.

---

## §3b NO TICS: THE LAW (author's standing ruling 2026-10-18; HARD; every book, permanently)

For the Writer, Dialogue Polish, Hook Craft, the Disruptor, the Editor and the Evaluator.

1. **Tic-bearer roster: EMPTY.** No character, **Mara included**, carries a verbal tic, catchphrase,
   refrain, pet phrase, signature line or signature gesture. Every card in `character-bible.md` reads
   "Verbal tic: none — distinguished by <axis>". Distinctness comes **only** from the four axes:
   attention/worldview, syntax, evasion and physicality/silence.
2. **No devices, for anyone.** Counting, numbering, listing, enumerating, pricing, rating, quantifying,
   cataloguing, condition-reporting and proverb-quoting are one device in different coats, and the
   device is retired for everyone. It is not rationed out to one "earned" character. (The prior run's
   Fenn numbering, Kallia proverbs and Mara catalogue-under-stress are all struck.)
3. **Motifs are OBJECTS and SITUATIONS, never phrases.** The watch, the film, the microcassette, the
   knucklebone and a hand at a threshold may recur. A line may not. **No beat in this book depends on a
   character's line "landing again."** "Do they still have mules?", "Fine mountain for vines", "Mama,
   look" and Valens's single English word (Ch.26) are each spoken **once** and never called back.
4. **The variation rule.** A repeated situation is written in fresh words every time. The watch is
   wound in Ch.18, 24, 32 and 41, and the verb phrase must differ each time (the mechanical gate below
   fails "wound the watch" on its third use). The same goes for the painted door, the cassette, the
   knucklebone, the film counter, Fenn's cold air and the threshold touches.
5. **Chaos traits are SUBJECTS, not phrases.** Mara's teeth, Valens's figs, Fenn's 1964 Phillies, the
   onion memory, the automat and Mrs. Dunphy recur as *topics*. Each surfacing is worded fresh, never
   ends a scene, and never becomes a formula. In particular, **teeth must not become the standard way
   Mara introduces a new character:** at most one introduction-by-teeth in any four chapters.
6. **The allowlist** (`tools/style_check.py` ALLOWLIST) holds **≤5 entries; this book uses three, each
   capped at 3 uses book-wide** (§4). Nothing else may recur verbatim.
7. **No signature may repeat across the author's other books.** Do not import another book's motif
   vocabulary, devices or recurring images.
8. **The Amelia Lesson.** In an earlier book a counting device and the phrase "never once" calcified
   into a tic and bled across the cast until everyone sounded alike, and a manuscript-wide de-tic was
   needed. Earned tics spread exactly like unearned ones. That is why the budget is zero. **Watch for
   the narrator's habits bleeding onto the cast** (see the bible's bleed guards).

### The mechanical gates that enforce it (every chapter, via `bash tools/check_chapter.sh N`)
| Gate | What fails |
|---|---|
| `tools/voice_wear_check.py` (strict by default) | (1) any **retired phrase** anywhere (seeded: "never once", the performed-candour family, "for the record"); (2) **self-repetition:** any 4–6-word phrase (not starting or ending on a stop word) that appears in **2 or more chapters**, or 3+ times in total. This is BLOCKING for this book, not informational. |
| `tools/tic_report.py --gate` | any content-rich **3–6-word phrase recurring 3+ times book-wide in prose**, and any **3+-word phrase recurring 3+ times inside quoted speech** (a catchphrase forming). Exempt: allowlisted motifs and `WORLD_TERMS`. |
| `tools/style_check.py` | cross-chapter repeated 5–6-word phrases (FLAG at 3+ uses or 3+ chapters); tic-word ceilings; simile, em-dash and foreshadow ceilings. |
| Evaluator | tic-proliferation scan: **any character leading with a tic caps Characters at 7.5.** |
| Continuity Guardian | the per-chapter audit checks for emerging devices and voice drift against this file and the bible. |

**Practical consequence for the Writer:** ordinary English 4-grams ("I did not want," "for a long time,"
"out of the city") will trip the two-chapter self-repeat check. Vary them as you draft. The Editor
fixes what slips through before finalize.

### Tool configuration the orchestrator must apply before Ch.1 (flagged, not applied here)
This dispatch writes only `voice-dna.md` and `character-bible.md`.
- **Done (verified at the 2026-10-18 patch pass):** all three allowlisted phrases ("the one it brought",
  "where the dead go out", "the seventh of bysios") are in `tools/style_check.py` ALLOWLIST,
  `tools/voice_wear_check.py` SELF_REPEAT_ALLOW and `tools/tic_report.py` MOTIFS. The inline comments
  in `style_check.py` were updated to the planned uses in §4 below.
- `tools/tic_report.py` WORLD_TERMS: add the proper place-names the story cannot avoid, because the
  tic gate scans 3-grams: **"nuceria gate", "corycian cave", "castalian spring", "sacred way",
  "polygonal wall", "via dell'abbondanza", "basilica julia", "flavian amphitheatre", "isthmian games",
  "temple of isis", "herculaneum gate", "sarno mouth"**. Proper nouns only. Object phrases ("father's
  watch," "painted door") are **not** world terms; they get varied.
- `STATE.yaml` `character_bible:` should be updated to `created: true`, with the entry count and
  `tic_bearers: []`.

---

## §4 ANTI-PATTERN BUDGET (genre: commercial historical romance / time-slip; density per 1,000 words unless stated)

The Writer aims under these; the Disruptor cuts down to them; the Evaluator scores against them.

| Pattern | Budget | Note |
|---|---|---|
| **Explanatory / analytical simile** (Pattern #11, the #1 AI fingerprint) | **≤4.0/1k gated; aim ≤3.0** | Characterizing simile only. Heat scenes: ≤2 per scene. Ch.42–44: ≤1 per chapter. |
| **Em-dash** | **≤4 per chapter, ABSOLUTE** | Aim 0–2. Semicolons do the work. Spaced en-dashes count as em-dashes. |
| **Adverbs in dialogue tags** | **near-zero** (target 0) | "said" plus a varied action beat. |
| **"as if" / "as though" / "it was as if" / "almost as though"** | **≤1 per chapter** | Each use must be characterizing, never interpretive. |
| **Metacognitive narration** | **0** | "I realized," "I found myself," "I noticed that I." Show the act. |
| **Emotional-temperature reports** | **≤1 per chapter** (aim 0) | "A wave of / a flood of / a rush of [feeling]." Use the object or the gesture. |
| **Foreshadowing / foreknowledge** | **0, book-wide** | §0, families A–E. `style_check --max-foreshadow 0`. |
| **Define-by-negation openers** | **0 sentence-initial** | No "Not X. Not Y. It was Z." and no "It wasn't grief. It was…" at the start of a sentence or paragraph. |
| **Anaphora triads** | **break every one** | Three parallel clauses or sentences opening alike ("No road. No wires. No sound."). Vary the syntax of the third or merge two. `rhythm_check.py` flags them. |
| **Performed-candour phrases** | **0** | "I want that on the record / written down," "I want to be exact / clear / honest," "let it be said (plainly)," "I will be honest," "I mention it because," "for the record," "truth be told," "if I'm honest." |
| **Closing aphorisms** | **0** | No chapter or scene ends on a generalization about life, time, love, fate, home or the dead. |
| **Scene-button device** | **0** | No object, gesture or line used to "click" a scene shut. Endings follow the ledger row. |
| **Fragments in calm narration** | rare | Fragments are a pressure signal; spending them in calm chapters blunts the break. |
| **Ellipses** | ≤~1.5/1k | Trailing speech only. |
| **Semicolons** | target ~3/1k | The Outlander linking move. |

### The ALLOWLIST (foundation §12): exactly three phrases, each **capped at 3 uses book-wide**
| Phrase | Owner and planned uses |
|---|---|
| **"the one it brought"** | Fenn's law of the doors ("it" = all the doors as one door with many mouths, so the phrase states the canonical law exactly). Ch.25 (a *promise*); Ch.42 optional (a *limit*, in Mara's present thought). **Ch.42 must work without it**: the limit is discovered in the action. Never a button. |
| **"where the dead go out"** | The god's answer, as Valens carries it out. Ch.13 (rendered **once**, in Valens's repetition only); Ch.19 (the Nuceria Gate tombs); Ch.44 optional. **Ch.44 must land without it.** |
| **"the seventh of Bysios"** | The consultation day. **The Ch.13 title counts as a use.** Planned: the Ch.12 bridge and the Ch.13 title, two in all. The Ch.11 beat and the Ch.13 opener paraphrase the day ("the year's first consultation day", Apollo's birthday). Nothing later. |

Everything else that recurs must vary in wording every time it appears.

---

## §5 THE EXPLICIT INTIMACY SCENES: HOW THEY READ ON THE PAGE

**Canon:** explicit when it occurs (on-page, detailed, sensual), but this is not an erotica book.
**Three scenes, all before the eruption: Ch.15, Ch.23, Ch.34.** Yearning without sex: Ch.11 (the
refused kiss), Ch.16–18 (the Corinth winter). **Nothing explicit from Ch.35 on, and none from Ch.39 by
law.** Once the mountain opens, the body's language is hands, carrying, and a watch being wound.
*(Three is canon. Foundation §6e and §11.13 now agree, and use the strictest cut-off: none from Ch.35 on.)*

### Register
- **Sensual and character-driven; never clinical, never purple.** Specificity and restraint carry the
  heat, not elevated diction.
- **Anatomy serves character.** The body is named plainly and only when naming it does work. Each scene
  advances what each of them fears and lets go of. It is never a parts inventory (that would also be the
  retired catalogue device).
- **Vocabulary:** plain, adult, unembarrassed nouns and verbs, chosen as Mara would choose them: frank,
  neither coy nor pornographic. One or two specific period materials per scene (the rope-strung bed,
  wool, the inn blanket, lamp oil, fleas, sea salt on skin).
- **Consent is unambiguous and mutual,** in action and when needed in a line. The risk is emotional, never
  coercive.
- Mara's 1998 mind may register the absence of contraception **once**, in Ch.15, as a present thought.
  No lecture, and no narrator resolution of it.

### How the two voices behave in heat
- **Mara:** the dry asides go **quiet**, the one time they do so outside fear. That silence is how the
  reader knows it is real. But unlike pressure, her **senses widen**: touch, smell, sound and the cold
  air all arrive together, and her sentences lengthen and slow rather than shrink. Humor may come
  *before* the silence (Ch.15) or *alongside* it once they are at ease (Ch.34).
- **Valens:** his **stillness breaks**. The man who keeps everyone at a working distance has nowhere to
  put his hands except on her, and no task to hide in. He is enormously careful, as he is with small
  objects, and he speaks very little. **In Ch.34 alone he talks more than anywhere else in the book;**
  that is the sign of ease. He never compares her to anything aloud.

### The three scenes are built to differ
| | Ch.15 Summer Pasture (AD 71) | Ch.23 Inn on the Appian Way (AD 74) | Ch.34 Surrentum (AD 78) |
|---|---|---|---|
| Function | first union, after she has told him the truth and he has asked about mules | the key turn: publicly believed for the first time, he lets himself be held | the late unshadowed joy |
| Emotional motion | clumsy and funny → the laugh stops → tender | sad → held → tender; **he** is the one comforted | unhurried, at ease, joyful; nothing points anywhere |
| Who leads | mutual; she pulls him down | she does; she is the steady one | both; they talk throughout |
| Mara's body | ordinary; the cold of the high pasture | **six months pregnant, handled frankly and tenderly**; positions adapted, her humor about her body, his care | at ease, sun and salt |
| Gear | high (long, slow, specific) | low (rain, short, close) | high (long, warm) |
| Period material | the olive-wood rope bed that gives way, sheep-smelling blanket | the rough inn blanket, rain on roof tiles, fleas | inn shutters, salt, the sea's noise |
| After | Felix snoring outside; a quiet image | a long fade into rain and the fleas | breakfast; the chapter just stops |

### Anti-patterns specific to heat
No purple euphemism ("core," "manhood," "member," "his length," "folds," "nub," "molten," "throbbing").
No clinical terminology. No metaphor-stacking ("her body a [noun] of [noun]"). No emotional-temperature
reports ("waves of pleasure," "she shattered," "she came undone"). No dirty-talk set-pieces. No
significance-tagging ("I had never been so happy," "I wanted to keep it forever"). **The em-dash budget
is easy to blow in a breathless scene; use none.** No similes interpreting feeling: one characterizing
comparison at most per scene (sample-10 uses one). No closing aphorism about love or bodies.

---

## §6 BENCHMARK SAMPLES (the canonical targets every downstream agent measures against)

| ★ | File | Why it is canonical |
|---|---|---|
| ★ | `voice-bank/samples/sample-01-controlled-sanctuary.md` | **Controlled voice at full strength:** a material spiral (painted marble, lead fixings), one dry undercut, bodily realism (aching feet, a temple slave interested in her trousers), wonder that refuses to soar. The high-gear target. |
| ★ | `voice-bank/samples/sample-03-irrelevant-thought-teeth.md` | **Human noise at a tense moment:** the obsession surfaces as subject, worded freshly, and makes her miss the moment that matters. The target for chaos traits. |
| ★ | `voice-bank/samples/sample-07-breaking-the-door.md` | **Maximum pressure:** shards, one sense at a time, plain verbs, no list. The low-gear and climax target. |
| ★ | `voice-bank/samples/sample-13-dread-in-scene.md` | **The NO-FORESHADOWING engine:** historical knowledge as a present thought, the lovely mountain, the declined photograph. Re-read it before any chapter in which the mountain appears. |

> **sample-13 (the Ch.19 register):** NB after Ch.12: the Pentax has no lens cap (left at Kirrha) and a dented filter ring; the sample's 'I put the cap back on the lens' cannot happen on the page.

Supporting calibrations: sample-05 and sample-06 (pressure levels 2 and 3), sample-08 (Valens against
Mara), sample-09 (Fenn's 1968 English), sample-10 (heat), sample-11 (the visible seam *shown*), sample-12
(the no-pull stop). **No sentence, image or line from any sample may be reused in the manuscript.**
They calibrate register only, and the n-gram gates will flag reuse.

---

## §7 OUTLANDER COMP CALIBRATION (measured from the source text, 2026-07-10; adapted to this book's stance)

Measured from Diana Gabaldon, *Outlander*: ~57,000 words sampled across a feast/dialogue chapter, a
capture/peril chapter and a tense-infiltration chapter. These are **targets**, not gates (the gates are
in §4). Use them when `metaphor_check`, `rhythm_check` or `show_tell_check` drifts and you need to know
which way the register leans.

| Dimension | Outlander (measured) | This book |
|---|---|---|
| Median sentence length | **15 words** (mean 16.8) | Book-wide median 14–16, **varied by the ledger's gear** (low 9–12 / mid 14–16 / high 17–20) so the median is not flat across chapters. |
| Short sentences (≤6 words) | **16%** | ~15%+; more in low-gear chapters; fragments reserved for pressure. |
| Long sentences (≥35 words) | **7%** (max ~80) | ~7%; the 40–80-word spiral belongs to wonder, memory and heat; ledger "long-spiral" openings require ≥28. `metaphor_check` flags >18% long. |
| **Em-dashes** | **~0/1k** | ≤4 per chapter absolute; aim 0–2. |
| **Semicolons** | **3.3/1k** | ~3/1k. *This is the Outlander move:* two independent clauses in one breath. |
| En-dashes | 3.0/1k | **Not borrowed.** Treat spaced dashes as em-dashes; use commas, semicolons or a new sentence. |
| Ellipses | 1.5/1k | ≤~1.5/1k, in speech. |
| Dialogue share | **~28%** (lower in peril chapters) | Book plan ~32% (romance band 30–45%), with per-chapter bands from 0–10% (Ch.14, 44) to 50–60% (Ch.37) per the ledger. |

**Craft signature to carry:** (1) wry modern intelligence through *characterizing* simile, never
analytical; (2) dry asides that wander one clause sideways and return; (3) bodily realism puncturing
grandeur; (4) sensory-material specificity as the immersion engine (authenticity dial ~8+), with
harshness held at ~7; (5) in-the-moment observation under threat.

**Two deliberate divergences from the comp:**
1. **No forward-spoiling.** Gabaldon's retrospective "I would learn…" is banned here (§0). Our narrator
   has no vantage after the scene.
2. **Deeper deflation under pressure.** Claire stays sensory in peril; Mara drops to hands and bodies,
   then to one sense (§1 Voice Under Pressure). The deflation is plain physical sequence, **not** the
   prior run's inventory or catalogue. The fuller Gabaldon register lives in the calm chapters.

**One-line directive for the Writer:** write Mara at Gabaldon's median-15, semicolon-not-em-dash,
one-specific-material-per-scene, characterizing-not-analytical-simile register in calm and immersive
chapters, set to the ledger's gear; then let it deflate to plain hands-and-bodies sentences under fear,
further than Gabaldon would, without ever reaching forward past the moment narrated.

---

## §8 THE SHAPE RULE

Each chapter is written to its row in the outline's **Anti-Predictability Ledger**. That row is a
contract, not a suggestion. The **structural approach** (and its named internal shape) decides how the
chapter is built. The **opening move** must produce the planned shape signature in the first sentence:
`I-statement` means it starts with "I" and runs more than 8 words; `I-punch` starts with "I" in 8 words
or fewer; `short-punch` is 8 words or fewer not starting with "I"; `long-spiral` is 28 words or more;
`scene-set` begins with a time opener; `dialogue` begins in quotation marks; `narrative` is 9–27 words
otherwise. The **ending move** likewise: `punch` is 7 words or fewer, `quiet` 8–24, `long-fade` 25+,
`question` or `dialogue` as named. One-sentence paragraphs are permitted only where the ledger allows
them. The **dialogue band** sets the share of the chapter in quotation marks. The **scene-break count**
and the **sentence gear** set the cut rhythm and the median sentence length. Hitting the row is what
makes `tools/shape_check.py` pass by construction, and it is checked every chapter. **A row marked
"PLAIN STOP (no pull)" (Ch.10, 31, 34 and the book's end at Ch.44) means the chapter simply stops.** It
ends on a plain moment of the ongoing day, with no hook, no question, no image weighted with meaning and
no aphorism (sample-12). Hook Craft must leave such an ending alone, and the next chapter begins on its
own terms.
