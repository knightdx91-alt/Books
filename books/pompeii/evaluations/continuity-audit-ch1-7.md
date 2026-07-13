# Continuity Audit — "The Hour of Ash" — Chapters 1–7 (single batch)

**Date:** 2026-07-13
**Scope:** manuscript/chapters/chapter-1.md … chapter-7.md (all seven finalized chapters)
**Canon read:** STATE.yaml · CLAUDE.md · character-bible.md · outline.md · voice-dna.md · feedback/pov-map.txt
**Mode:** read-only cross-manuscript audit (no chapter or tracker files modified)

## VERDICT: NOT CLEAN — 3 CRITICAL, 6 WARNING, 5 MINOR

The prose voice, motif discipline (the *click* correctly withheld Ch.4–7), the dating machinery
(Nero's stripped bronzes + Vespasian → ~70 AD), Fenn inserts #1/#2, the Kirrha/Krisa geography,
and the Caedicius/Caedicia alias are all internally sound. The problems cluster at two seams:
(a) **the WHERE-of-the-door information chain runs ahead of the Oracle** (the single most important
finding), and (b) **a handful of hard facts drift between chapters** (a headland's country, Kallia's
son, Kallia's house, the time-gap number).

Findings are ranked by severity, then by how likely a careful reader is to catch them.

---

## CRITICAL

### CRIT-1 — Mara knows the door-home's WHERE before the Oracle gives it (information-flow)
- **Audit:** 3 (Information Flow) + canon check
- **Chapters/lines:** Ch.6 L173; Ch.7 L67, L69, L71
- **Canon:** STATE guardrails + outline Ch.10 "The Pythia" [TP ~28%]: *the Oracle tells Mara WHERE
  the door home is (Pompeii) but NOT WHEN; she learns the when later.* The Oracle has **not yet
  been consulted** as of Ch.7 — Ch.7 is where she *plans* to climb the sacred way and ask.
- **The violation, three-layered:**
  1. **Premature destination knowledge (systemic).** Ch.6 L173 — Mara to Kallia: *"how a person
     went from here to Italy. To the bay below the smoking mountain, I said; I had a thing I must do
     there."* She already knows her destination is Italy / the bay below the mountain. Ch.7 L71 —
     Kallia: *"whatever is under your mountain in the south that you will not tell me about."* The
     destination is treated as settled knowledge across both chapters, before the Oracle scene.
  2. **Acute self-contradiction inside Ch.7.** L67: *"The Oracle had told me, in the first hour, in
     words I had turned over ten thousand times since, that the door home lay under a mountain by
     the Roman sea."* This asserts the Oracle already spoke — but there is **no Oracle consultation
     anywhere in Ch.1–7** (Ch.5's arrival includes the temple but no consultation), and it directly
     contradicts the same chapter two paragraphs later — L69: *"she told me where the door is not.
     She might tell me where it is,"* and L71, the whole "two locks" plan to *go* ask the Pythia the
     WHERE. L67 says the Oracle gave the where; L69/L71 say she must still go get it.
  3. **Root gap.** If L67 is deleted as the error it appears to be, the manuscript then never sources
     her knowledge that the home-door is in **Italy** at all. The door she crossed through is the
     **Greek** one (Fenn's Greek coordinates; she lands at Delphi). Her entire Ch.6–7 project (buy
     passage *south to Italy*) presupposes a WHERE she is not supposed to have until Ch.10.
- **Suggested fix (design decision for architect/author — pick one):**
  - (A) **Honor canon strictly:** in Ch.6–7 Mara does **not** yet know the destination is Italy; her
    Ch.7 goal is to reach and consult the Oracle (a morning's walk) to *learn* the where. Rework the
    "buy passage south to Italy" plot so the southward push is *motivated by the Oracle answer she is
    about to seek*, not by a destination she already holds. Cut Ch.7 L67's Oracle attribution; cut
    Ch.6 L173's Italy/"smoking mountain" destination statement.
  - (B) **Move a first WHERE-fragment earlier on purpose:** if the author wants Ch.6–7's southward
    momentum, give the rough where ("a mountain by the Roman sea") a *legitimate early source* —
    e.g., a Fenn-paper line, or a first Oracle fragment at Ch.5 arrival — and reserve only the
    **specific** naming (Pompeii/Vesuvius) + the withheld WHEN for Ch.10. This changes canon and
    must be logged in STATE before it propagates.
- **Cascade risk:** HIGH. This chain feeds Ch.10 (the Oracle beat loses its punch if she already
  knew), the Ch.14 "beautiful green mountain" ease-is-the-horror beat, and Ch.26's arithmetic. Fix
  before Ch.8 is written or Ch.8 will inherit the premature-where assumption.

### CRIT-2 — The crossing headland is called "an English headland" (geography)
- **Audit:** 4 (World/Geography)
- **Chapters/lines:** Ch.5 L37 vs Ch.3 L21–35, Ch.4
- **Contradiction:** Ch.5 L37 — *"…before the afternoon I had knelt on an **English** headland and
  laid my kit down on the lid of the world."* But the survey/kneeling-with-kit and the crossing
  happen **abroad**: Ch.3 has her fly out of England ("England go under the wing," "over France the
  cloud broke"), land in a hot olive country, hire a car, and walk out to *"a fist of pale rock
  pushed out into the sea past the last of the olives."* She crosses there (Ch.4, "the small white
  hire car at the top") and lands at Delphi (Ch.5). The headland is Greek, not English. There is no
  English headland anywhere in Ch.1–7 (Ch.1–2 England scenes are a study and a coastal antique shop —
  no kit-on-the-rock).
- **Suggested fix:** Ch.5 L37 → "a headland at the edge of the world" / "a Greek headland" / "a
  headland two aeroplanes from home." Do **not** write "English."
- **Cascade risk:** Medium. The Ch.26 payoff ("the date written in her own hand," re-read seed #4)
  and any later frame-callback must agree on where the kit was laid out. See also WARN-6.

### CRIT-3 — Kallia says she "buried a son"; her son is missing, not dead (character fact + motif)
- **Audit:** 1 (Character Consistency) + 5 (motif integrity)
- **Chapters/lines:** Ch.7 L223 vs Ch.5 L131–133, Ch.6 L205–215, L229–235
- **Contradiction:** Ch.7 L223 — Kallia: *"I have buried a husband and a son and a great deal
  else…"* But the entire lamp motif rests on the son being **unheard-from, not confirmed dead**:
  Ch.6 L207–211 — "He went for a soldier, six years past… then no more, two years gone… *He will
  come up that road one evening with a beard I won't know.*" Ch.6 L233 — "He'll come up the road…
  and he'll not know the house without the light." The nightly lamp exists precisely because she
  has **not** buried him and cannot know his fate (a soldier vanished "at the edge of the world" —
  no body to bury). Character-bible confirms: *"A son in the legions, unheard-from two years… never
  says her son's name aloud."* "Buried a son" collapses the motif.
- **Suggested fix:** Ch.7 L223 → keep the husband literal, keep the son ambiguous: e.g. "I have
  buried a husband, and as good as lost a son, and a great deal else," or "…a husband and a son I
  will not bury and cannot mourn…" — anything that does not assert a completed burial.
- **Cascade risk:** Low mechanically, high thematically — the lamp/son thread is load-bearing to the
  end. A stray "buried" here would make a later "he never came" reveal read as a contradiction.

---

## WARNING

### WARN-1 — Kallia's dwelling: one-room house (Ch.5) vs multi-room inn (Ch.6)
- **Audit:** 4 (World/setting)
- **Lines:** Ch.5 L121 — *"A single low room of the grey polygonal stone, a hearth at one end, a
  byre partitioned off… a loft…"* (a one-room hovel + byre). Ch.6 L105–107 establishes it as an
  **inn** that "let two rooms to the traffic of the sacred road," and L205 names *"the third and
  best room of the inn, dry, with a real window and a bed frame."* A house with (at least) three
  lettable rooms is not "a single low room."
- **Suggested fix:** In Ch.5, describe the main living room as one of several (e.g., "the low main
  room," implying rooms off it), or in Ch.6 downscale the "inn" to a house that takes the odd lodger
  in the one spare room. Decide the floor plan and make both chapters state it.
- **Cascade risk:** Low, but the "best shut room kept for the son" (Ch.6) needs a house big enough to
  have it.

### WARN-2 — Knowledge reset across the Ch.6/7 seam (she re-learns she needs a man's name)
- **Audit:** 3 (Information Flow) + 5 (plot redundancy)
- **Lines:** Ch.7 L39 — *"I had not once understood, until she said it, that in this world I was not
  a person…"* — but Ch.6 L183–195 already delivered Kallia's full "a woman needs a man's name to
  exist / now you know the size of your mountain" lecture, and Ch.6 L247–249 already had Mara act on
  it ("a widow… on her dead husband's business… I could build the story"). Ch.7 then re-discovers
  the need and re-builds the widow "over three nights" as though from zero. (Ch.7 L85 *does*
  correctly acknowledge she already knew *of the muleteer* from Ch.6 — so the muleteer thread is
  clean; only the "needs-a-man/build-a-widow" realization resets.)
- **Suggested fix:** Reframe Ch.7's opening beats as *execution* of a Ch.6 decision, not fresh
  revelation: cut/soften L39's "I had not once understood, until she said it"; have the wagoner
  rejection *confirm* the lesson she already learned rather than teach it new. The three-night
  widow-build can stay as the concrete construction of the story she resolved to build in Ch.6.
- **Cascade risk:** Low; a tone/framing fix.

### WARN-3 — Time-gap figure drifts to "eighteen hundred years" in Ch.7
- **Audit:** 2 (Timeline) — internal arithmetic
- **Lines:** Ch.7 L39 ("crossed half the width of the world and **eighteen hundred** years") and
  L147 ("a place **eighteen hundred** years from here") vs the precise figure established in Ch.5
  L37 ("one thousand nine hundred and twenty-eight years"), Ch.5 L57 ("nineteen centuries"), Ch.6
  L21 ("nineteen hundred years"). 1998 − 70 AD = 1928 ≈ **nineteen** centuries; "eighteen hundred"
  is ~130 years short and clashes with the very exact Ch.5 count.
- **Suggested fix:** Ch.7 L39 & L147 → "nineteen hundred years." (Note: STATE's Ch.7 history log
  records fixing a modern-mileage leak "twelve hundred miles → half the width of the world"; the
  paired "eighteen hundred years" in the same clause was not caught.)
- **Cascade risk:** None; number swap.

### WARN-4 — "the smoking mountain" telegraphs the volcano (foreknowledge + history)
- **Audit:** 1/4 + canon tone dial
- **Line:** Ch.6 L173 — Mara names her destination "the bay below **the smoking mountain**." Two
  problems: (a) **doom-telegraph** — canon (outline Ch.14) requires Vesuvius to read as the
  "beautiful green mountain," Mara's ease being "the whole horror; do NOT let her sense doom." A
  smoking-mountain tag pre-loads the dread the design wants withheld. (b) **History to a point** —
  in ~70 AD Vesuvius was not recognized as an active volcano and was not visibly smoking
  (vineyard slopes); a 1st-century Greek would not know it as "the smoking mountain," so it also
  reads as Mara's modern foreknowledge leaking into speech.
- **Suggested fix:** Neutral phrasing — "the bay under the green mountain," "the Campanian bay," or
  simply "the bay in the south." (Overlaps CRIT-1: this line is also premature-where.)
- **Cascade risk:** Medium — protects the Ch.14/Ch.22 "unshadowed mountain" beats.

### WARN-5 — Datebook "permit, Turkey" vs Halloran's "Campanian coast" permit
- **Audit:** 4 (institutional/geography)
- **Lines:** Ch.1 L41 — datebook: *"Ring Halloran back re: permit, Turkey, be quick."* Ch.1 L87 &
  Ch.3 L15 — Halloran "had been holding a permit for a survey season on the **Campanian coast** /
  the Italian coast." Read naturally, the diary line ties Halloran to a **Turkey** permit, but the
  permit he holds is **Campanian**. (The father's past digs include "the parched hill in Turkey,"
  Ch.1 L47, so a separate Turkey thread is *possible* — but as written the reader connects the
  Halloran/permit line to the Campanian permit and hits a mismatch.)
- **Suggested fix:** Disambiguate. Either the datebook line names the same place ("re: permit,
  Campania/Italy"), or split the notes so Turkey is visibly a *different* item (e.g. two diary
  lines), so "Ring Halloran re: permit" and "Campanian coast" agree.
- **Cascade risk:** Low, but see WARN-6 (permit + crossing-site geography interact).

### WARN-6 — Manuscript crossing site = GREECE; character-bible says CAMPANIAN coast (tracker/manuscript mismatch)
- **Audit:** 4 (geography) — advisory, latent
- **Evidence:** Manuscript: Fenn's coordinates carry **Greek** place-names (Ch.3 L7); she flies to a
  Greek olive coast, crosses on the seaward headland (Ch.3–4), and lands at **Delphi, Greece**
  (Ch.5). So the *modern* crossing site is the Greek coast. But character-bible L229 states the
  Halloran permit "routes Mara's survey to **the Campanian coast (canon: the crossing site)**."
  The manuscript's executed geography (Greek crossing) and the bible's note (Campanian crossing) do
  not agree.
- **Note:** This is a **tracker vs. manuscript** divergence, not a within-manuscript error; per the
  read-only brief I have not edited the bible. Flagging because it is latent and will bite at the
  Ch.26 payoff ("the date in her own hand… where I would one day see it written again," Ch.3 L45)
  and any excavation/return callback if a later chapter assumes the kit was laid out in Campania.
- **Suggested fix:** Author/architect to reconcile: confirm the modern crossing site is Greece (as
  written) and update the bible note; or, if Campania was intended, the Greek-coordinates/Delphi
  landing chain in Ch.3–5 needs revisiting (much larger change — not recommended given the chapters
  are finalized around Greece).

---

## MINOR (polish-level)

### MINOR-1 — Ch.7 seasonal ordering: "spring market" before "tail of winter"
- Ch.7 L12 places the wagoner rejection at *"the spring market, on the first fair-weather day,"*
  but the subsequent Kallia widow-building (which the rejection *causes*) is L31 *"the tail of
  winter, the light coming back thin and grudging,"* and the yard visit is L97 *"the first morning
  the road was dry enough."* A spring-market scene reading as earlier than a tail-of-winter scene
  it precedes is a small seasonal j5. **Fix:** call L12 "the first market of the turning year" or
  move it firmly into the same late-winter window.

### MINOR-2 — The film roll: shot-months-ago roll vs fresh load on the rock
- Ch.1 L89 — the camera holds *"a roll of film I had shot months ago and never developed."* Ch.3
  L49 — on the headland she loads a **fresh** cassette ("the cassette seated, the leader drawn
  across the gate… two blank frames wound off… frame counter came up off S to one"), then never
  fires the shutter (counter stays on 1). The earlier exposed roll is never unloaded/developed
  on-page, and it is unclear which roll is "the undeveloped roll" relic. **Fix:** one clause in Ch.3
  acknowledging she swapped in fresh film (and what became of the old roll), or align Ch.1 so the
  camera is empty until the Ch.3 load.

### MINOR-3 — The Discman disappears
- Ch.1 L89 lists "A Discman and the one disc I always carried" in the laid-out kit. It is absent
  from the Ch.3 fieldwork-kit ritual (notebook/watch/camera/meter/compass) and from Ch.5's
  anachronism inventory. **Fix:** either note she left it (like the slides/datebook) or drop it
  from the Ch.1 kit; as a period-relic touchstone it may be wanted later, so decide deliberately.

### MINOR-4 — Valens's face: jaw-scar/beard (Ch.5) vs eyebrow-seam (Ch.7)
- Ch.5 L103 — a scar *"down the side of his jaw that pulled his short beard askew."* Ch.7 L105 —
  *"a seam through one eyebrow that pulled the brow into a permanent slight question"* (no beard
  mentioned). Both note forearm scarring, so not a hard contradiction, but the signature facial
  scar shifts from jaw→eyebrow and the beard goes unmentioned in his first live scene. **Fix:**
  harmonize — keep both scars if desired, but let Ch.7 nod to the jaw-scar/beard already established.

### MINOR-5 — Mara's "Greek shape" of her name never specified
- Ch.5 L127 — she gives Kallia "the nearest true thing my mouth could make of my name," Kallia
  "made a Greek shape of it," and Mara "let the Greek shape stand." That Greek shape is never
  stated, and she is simply "Mara" thereafter (including Kallia addressing her "Mara," Ch.7 L63).
  Harmless if Mara ≈ the Greek shape, but it is a dangling promise. **Fix:** either name the Greek
  form once, or soften L127 so no distinct unnamed form is implied.

---

## Tracking notes (for future batches)

- **Dating spine (holds):** Nero strips Delphi = 67 (Ch.5) → after Nero's fall → Vespasian → ~70 AD.
  1998 − 70 = 1928 yrs = "nineteen centuries." Keep all cross-references at nineteen-hundred/nineteen
  centuries (see WARN-3).
- **Motif *click*:** correctly present Ch.1–3, correctly withheld Ch.4–7 (reserved for Ch.36). Clean.
- **Fenn inserts:** #1 (Ch.2 L108) and #2 (Ch.5 L141) present and consistent; #3 ("only the one it
  brought") is due Ch.10 — watch it does not leak early.
- **Names/spelling:** no drift found. Reyes/Emilio Reyes, Halloran, Verrall, Fenn, Kallia, Melita,
  Valens, Caedicius/Caedicia, Kirrha vs Krisa (distinct places, used consistently), Amphissa,
  Puteoli — all stable.
- **Valens knowledge chain (clean):** name withheld in Ch.5 ("I did not have his name for weeks"),
  supplied by Kallia in Ch.7 L87 after a full autumn/winter; scandal kept vague (Kallia: "a great
  man's household, a woman's name in it") — the legate's-wife specifics are correctly still withheld.
- **Open, on-track (not errors):** widow alias built (Ch.7), Oracle plan seeded (Ch.7 "two locks"),
  factor's-widow safe road introduced (Ch.7) → feeds Ch.8. No dropped threads beyond MINOR-2/3.

*End of audit. No chapter or tracker files were modified.*

---

## RESOLUTION LOG (applied 2026-07-13, same session)

**CRITICAL — all 3 fixed:**
- **CRIT-1 (Oracle WHERE-chain):** resolved via option B — Mara's ROUGH "where" now sourced to
  **Fenn's notes** ("under a mountain by the Roman sea"), the Oracle (Ch.10) reserved for the PRECISE
  place + withheld WHEN. Edited Ch.7 Oracle beat (removed the self-contradicting "The Oracle had told
  me, in the first hour…"; reframed the closing thought to Fenn-gave-the-mountain / god-may-give-the-name)
  and Ch.6 L173 (neutralized "smoking mountain" → "the bay in the south, under its mountain"). Canon
  clarification logged in STATE.yaml guardrails; **flagged for Terry to confirm or override.**
- **CRIT-2 (English headland):** fixed in BOTH places — Ch.5 L37 and a second instance the audit
  missed at Ch.6 L157 → "a headland at the edge of the world."
- **CRIT-3 (Kallia "buried a son"):** Ch.7 → "buried a husband, and as good as lost a son" (keeps the
  son ambiguous; protects the lamp/return motif).

**WARNING — 5 of 6 fixed; 1 reconciled in tracker:**
- WARN-1 (one-room vs inn): Ch.5 L121 rewritten to a larger house with "two cold rooms she let… to
  the traffic of the sacred way," consistent with Ch.6's inn + "third and best room."
- WARN-2 (knowledge reset): Ch.7 L39 reframed — the wagoner now CONFIRMS what Kallia already taught,
  not a fresh revelation.
- WARN-3 (time-gap drift): Ch.7 "eighteen hundred years" ×2 → "nineteen hundred years."
- WARN-4 (smoking mountain telegraph): fixed with CRIT-1 (Ch.6 L173 neutralized).
- WARN-5 (permit Turkey vs Campania): Ch.1 datebook "permit, Turkey" → "permit, Italy" (agrees with
  Halloran's Campanian permit; the father's separate Turkey DIG at Ch.1 L47 is untouched).
- WARN-6 (crossing-site tracker mismatch): reconciled in character-bible.md — added a CROSSING-SITE
  NOTE confirming the modern crossing is **Greece** (Fenn's Greek coordinates → Delphi); the Campanian
  permit is the father's thread + Mara's destination-goal, not the crossing point.

**MINOR — 2 fixed, 3 deferred (logged, non-blocking):**
- MINOR-1 (seasonal ordering): Ch.7 "spring market" → "first market of the turning year." FIXED.
- MINOR-4 (Valens face jaw→eyebrow): Ch.7 harmonized to the Ch.5 jaw-scar + short beard. FIXED.
- MINOR-2 (film roll shot-months-ago vs fresh load), MINOR-3 (the Discman vanishes), MINOR-5 (Mara's
  unnamed "Greek shape" of her name): DEFERRED — polish-level, low cascade risk; touching Ch.1/Ch.3
  kit descriptions risks new seams. Revisit in a later polish pass.

All edited chapters re-verified: style_check / grammar / voice-wear clean; em-dash within gate; all
above word floor.
