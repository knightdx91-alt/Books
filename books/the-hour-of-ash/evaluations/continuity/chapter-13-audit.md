# Continuity Audit: Chapter 13 (run 2, per-chapter drift audit)

**Date:** 2026-10-20
**Mode:** MANUSCRIPT AUDIT. Ch.13 "The Seventh of Bysios" (post-disruptor) checked against Ch.1–12 as they stand on disk, ENTITY_STATE.yaml (as of Ch.12, read only; the tracker is running in parallel), outline.md, foundation.md, voice-dna.md, character-bible.md, voice-bank samples 01–13, and STATE.yaml guardrails + resolved_author_decisions.
**Chapter reviewed:** `manuscript/chapters/chapter-13.md`
- Length: **7,587** prose words by shape_check (7,836 `wc -w` with header). Brief range 7,500–8,500: **87 words of headroom.**
- Dialogue **37.8%** (band 35–45; floor headroom ~2.8 points). 4 breaks. Median sentence 14 (gear mid).
- **246 prose paragraphs.** `pN` counts prose paragraphs only (title, HTML comments and `* * *` not counted); `l.NNN` is the file line. p1 = l.6 "The morning on which Apollo…", p246 = l.504 "Pompeii."

**Mechanical baseline** (`bash tools/check_chapter.sh 13`, run read-only): **ALL CLEAN.** Retired phrases 0; tic gate clean; echo scan 0; command echo 0; and-chains 5 (cap 9); credential asides 0; negation pivots 0; "So" openers 0; swallow ×2 (worst chapter for the class, under cap); fig 2.5/1k; shape **CLEAN** (`13 7587 4 38 14 scene-set dialogue`).

**My own sweeps:** 3-grams vs every voice-bank sample and every bible Sample line; 4- and 5-grams vs Ch.1–12 (only the allowlisted title phrase and one function-word 4-gram recur); by-hand pass of every closed / spent / at-risk registry in the bible (after Ch.1 through after Ch.13); timeline arithmetic from Ch.12; geography of the sanctuary and Sicily; Delphic procedure c. AD 71.

**Total findings: 51. CRITICAL: 1 | WARN: 20 | INFO: 30** (IDs W-01–W-21; W-08 was folded into W-12(b) and is not used)

**Summary**
- **The one CRITICAL is a canon breach:** Mara names "the Bay of Naples" (aloud) as a candidate for the god's "mountain of vines by the western sea" one page before Theano says "Pompeii". Her father ran a Campanian survey (Ch.1–2). Either she has thought of Vesuvius and passes over it, or the narration winks. voice-dna §0: "Ch.13: only the word." One-word swap fixes it.
- **Information flow:** clean on who hears what (answer: Valens, Felix, Kallia, Mara; "Pompeii": Mara alone; Felix absent for every arena/school line). One leak: the Elateian's question presupposes that Mara hit a man, which the cover story never admitted (W-06).
- **Timeline:** Ch.12's "three days" holds exactly. Three internal clock slips: lodgers "since the road" against Ch.12's "all week" (W-03); lodgers "waiting their turns" while the Pythia is home off duty (W-04); Kallia's "till dark" against her own "all afternoon" (W-05).
- **History:** goat drench, Pindar's chair, the omphalos net, laurel-and-barley hearth, Chian altar, three Pythias → one (Plutarch), monthly days, widowhood and age all hold. Two geography faults: Praxias goes **down** the Way to reach the stadium, which is uphill (W-02); Mara's Etna rebuttal is muddled and contradicted by her own next line (W-01).
- **Theano:** matches her card and Ch.8 (CH8-2 can be RESOLVED). One card conflict: she explains her crows, against "never explains" (W-13).
- **Objects:** no watch ✓, no lens cap ✓, camera only as "the thing of my father's" / "your father's silver thing" ✓. The ibuprofen lands but the page never says these are the last two, or what "the bottle" is after ten chapters (W-18).
- **Voice:** no tics; gates clean. Hand-found drift: the Ch.5 votive-mold beat rebuilt (W-11); the father's slides contradict Ch.1/Ch.7's kitchen-bedsheet-September show (W-07); Ch.11's "By then, if there was any justice…" frame reused (W-10); two anaphora triads (W-09); the "same… same… same" triad (W-09); three narrator call-out pointers (W-15); two voice-bank lifts, one from the reserved Ch.42 sample (W-14); a betting vehicle and a lentil joke, both spent (W-16, W-17); in-law joke-butt ×2 (W-12); "the Amphissan" now names two different people (W-12).
- **Foreshadowing / forward reach:** none in narration apart from C-01. The imagined first hour home is present hope, not reach.

**Word ledger for the recommended fixes:** about **−19 words** net (→ ~7,568; still 68 over the 7,500 floor). Dialogue share stays ~37.9% (dialogue-side edits net 0). Optional extras are marked and costed separately.

---

## Scorecard by category

| Category | Result |
|---|---|
| Characters (Theano vs card + Ch.8) | Recognised by situation only ✓; body, grievances, evasion, no comfort, withholds WHEN ✓. W-13 (explains the crows). |
| Timeline (7th of Bysios, first consultation, Ch.12's "three days") | Bridge exact ✓. W-03, W-04, W-05. |
| Information flow | ✓ except W-06. |
| History / world rules | ✓ except W-01, W-02; INFO notes on promanteia, Pythia's house, monthly-vs-winter. |
| Canon (Oracle = first WHERE, WHEN withheld; no Vesuvius) | WHERE ✓, WHEN ✓. **C-01.** |
| Objects | Watch ✓, cap ✓, camera ✓. W-18 (ibuprofen), W-19 (rag). |
| Plot threads (Celer, CH12-2, CH12-8) | Untouched or consistent; see ENTITY section. |
| Voice drift | W-07, W-09–W-12, W-14–W-17. |
| Ledger / shape | Sigs ✓, breaks ✓, gear ✓, dialogue ✓. W-20 (one-sentence opening paragraph). |
| Allowlist | "where the dead go out" 1/3 ✓; "the seventh of Bysios" 2/3 (Ch.12 body + this title) ✓, body never says it ✓. |

---

## PRIORITY: ENTITY_STATE conflicts (processed first)

| ID | Status in ENTITY | What Ch.13 does | Recommend |
|---|---|---|---|
| **CH8-2** (Theano's Ch.8 identity; the god's barley and the lie missing) | UNRESOLVED (info) | Recognition by situation: "the house next to the highest", the squared stone at the door, a dozen crows, barley flung "over the ruts", hands on her knees (l.430–l.442). The plan's missing pieces are now on the page: the basket carries the god's laurel brand (l.434), and she lies ("That's my own barley … I wouldn't give them a grain of his.", l.460). | **RESOLVE** (page now carries the plan's barley + lie; the identification is by situation, as designed). |
| CH12-2 (record form: book vs diptych) | UNRESOLVED | "Mine's written. At Corinth." (l.384) fits the magistrate's book; does not choose. | Keep open for Ch.16–17. |
| CH12-5 (who sent the three) | UNRESOLVED | Valens watches for "them" (l.72–l.74); no new fact. | Keep open. |
| CH12-7 (camera seen) | UNRESOLVED | Kallia is told of "a heavy thing from my bag" (l.14), not shown it; Felix says he kept the "silver thing" secret (l.256). | Keep open; add Kallia's knowledge (patch below). |
| CH12-8 (which name is written) | UNRESOLVED | Valens gives the god's registrar **Felix** as the carrier's name (l.116) and says his own is "written. At Corinth." | Keep open; record that no Delphic record carries his name. |
| CH12-9 (goat's three nights) | UNRESOLVED (info) | "She had been at the yard since sundown yesterday, as Valens had said she would be" (l.42). | Narrow: the evening-before arrival is now on the page. |
| ibuprofen `description_note` (bottle vs "packet") | note | Page: "the bottle" (l.62, l.452), matching Ch.2's "a bottle of Advil". | Resolution beat lands; see W-18 for the missing "last two". |

---

## CRITICAL ISSUES (must fix before proceeding)

### [C-01] "the Bay of Naples" named as a candidate for the god's vine mountain, one page before "Pompeii"
- **Audit:** Canon / no-foreshadowing (voice-dna §0 "What is KEPT" 3: "Ch.13: only the word. Theano says 'Pompeii.' The horror arrives in Ch.14."; outline Ch.13 writer warning: "No narratorial foreshadowing … Here it is only the word"; the brief: "Mara must not think of Vesuvius").
- **Location:** p167, l.344 (Mara's speech).
- **Evidence:** "Or Sicily after all, or the Bay of Naples, or Spain. There is a mountain with vines on it beside every sea the Romans have ever reached."
- **Why CRITICAL:** the god said "the mountain of vines by the western sea". On the Bay of Naples that mountain is Vesuvius, and Mara knows it professionally: her father held the *permesso* "for the Campanian survey season" and Halloran rings "from Naples" (ch-01 l.359; ch-02 l.55, l.97). A classicist who lists the bay as a vine-mountain site and does not flinch has either thought of Vesuvius and suppressed it (which breaks the stance: Ch.14's "I knew the year" must be the first time) or the narration is winking at the reader one page before the reveal. It is also an anachronistic place name in her Greek (the ancients called it the Krater). Every earlier wink of this kind was cut (Ch.8 Theano, Ch.10 Julia Domna, Ch.9 the Thracian name); this one points at the book's central secret.
- **Fix (−3 words, dialogue):** "Or Sicily after all, or Massalia, or Spain." (Massalia: a western-sea Greek city in vine country; no Campanian pointer.)
- **Cascade:** none in Ch.13. Note for Ch.14 (INFO I-29): with the bay gone, Mara has skipped Campania entirely despite her father's survey; Ch.14 can own that blind spot as memory if it wants it.

---

## WARN ISSUES (should fix)

### [W-01] Etna "on the eastern sea": the ship sentence is muddled, and Mara's next line undoes her own rebuttal
- **Audit:** World rules / geography; internal logic.
- **Location:** p150, l.310; against p152, l.316.
- **Evidence:** "Except that Etna looked out on the eastern sea. A ship out of Syracuse that wanted it on its western side would have had to sail clean round Sicily." Two exchanges later Mara says: "West of what? West of here? Everything is west of here."
- **Problem:** a ship sailing north out of Syracuse already has Etna on its western side; no circumnavigation is needed, and Etna has no "western side" on any sea. Also, if "west" is reckoned from Delphi, Sicily *is* by the western sea, which is exactly Mara's next objection, so her narration's verdict ("I did not suppose he had ever looked at a map") is unearned. Geography itself is right: Etna stands over the Ionian, on Sicily's east coast, NNW of Syracuse, and its slopes were vine country (Strabo 6.2.3).
- **Fix (+2):** "Except that Etna stood over the eastern sea, the one Syracuse looked out on; a Syracusan who wanted a western sea would have to cross the whole island to find one." The rebuttal is then argued from the priest's own Syracusan frame, and "West of what?" reopens it honestly.
- **Cascade:** none.

### [W-02] Praxias goes *down* the Way "toward the stadium"; the stadium is uphill
- **Audit:** Geography (Delphi; Ch.11).
- **Location:** p130, l.268.
- **Evidence:** "Praxias had gone on down the Way at a trot toward the stadium and the quail ring, without stopping." Ch.11: the ring is "back of the stadium" / "From behind the stadium" (ch-11 l.312, l.346), and Praxias "went off uphill, telling the quail about it" (ch-11 l.324). Delphi's stadium is the highest structure in the sanctuary, above the theater; the Sacred Way runs down from the temple terrace to the gate.
- **Fix (+1):** "Praxias had gone off up past the theater at a trot toward the stadium and the quail ring, without stopping."
- **Cascade:** none; Valens and Mara still go "down the Way" (l.276, l.284), correctly.

### [W-03] "Since the road the house had been full" contradicts Ch.12's lodgers "all week" before the road
- **Audit:** Timeline / Ch.12.
- **Location:** p3, l.10.
- **Evidence:** Ch.13: "I had not had her to myself in three days. Since the road the house had been full to the eaves." Ch.12: "I had carried it since the lodgers came. All week men had slept along Kallia's gallery in rows, Thessalians and Achaeans and a priest's cousin from Elateia" (ch-12 l.162), i.e. before the road.
- **Fix (0):** "All that week the house had been full to the eaves."
- **Cascade:** "in three days" still reads (she has been crowded out since the road).

### [W-04] Lodgers "waiting their turns" while the Pythia is already home off duty
- **Audit:** Timeline (inside the chapter).
- **Location:** p48, l.102; against p196, l.410 and p218, l.448.
- **Evidence:** "For once the court was empty, the lodgers all still up at the sanctuary, waiting their turns or arguing over what they had been given". In the same afternoon, a little later, Theano has her basket, is on her stone "before her knees set", and the jug boy has done his "Forty-one jars … Since the dark." The day's consultation is over.
- **Fix (0):** "…the lodgers all still up at the sanctuary, eating their victims or arguing over what they had been given".
- **Cascade:** fits Kallia's "up at the sanctuary till dark" (sacrificial feasting).

### [W-05] Kallia contradicts herself on when the Thessalians come home
- **Audit:** Timeline / character consistency.
- **Location:** p9, l.22 and p11, l.26.
- **Evidence:** "the Thessalians will be up at the sanctuary till dark" … then, minutes later: "Be home ahead of the Thessalians, or you'll be on the stair all afternoon with their dinners."
- **Fix (+1):** "…or you'll be on the stair half the night with their dinners."
- **Cascade:** none.

### [W-06] The Elateian's question presupposes that Mara hit a man, which the cover story never admitted
- **Audit:** Information flow (Ch.12 cover story; Celer thread).
- **Location:** p124, l.256.
- **Evidence:** "The Elateian asked me yesterday at the gymnasium what you'd hit the man with. He'd heard about the man at the ford. A stone, I told him." The agreed public story is "we came on a man in the ditch below the ford, and the road had been at him before us" (ch-12 l.258), told to the graybeard as "We came on him" (ch-12 l.286), and reached Kallia as "a stranger robbed and dead … and Valens's string come on him" (l.10). Nobody outside the party knows anyone was hit. Either Felix leaked the fight (and "A stone" confirms it, with Valens hunted) and nobody reacts, or the Elateian knows something he cannot.
- **Fix (0, dialogue; recommended):** "…what the man was hit with. He'd heard about the man at the ford. A stone, I told him." Felix's "I never said about your father's silver thing" then stands as his volunteered loyalty, and "It wasn't a stone, was it?" / "It was heavy," still works as Felix half-knowing.
- **Alternative (≈+15):** keep the line, own the leak (Felix had bragged about "the one that ran"), and give Mara one beat of alarm. Plot-heavier; not recommended at this length.
- **Cascade:** none to Ch.14. ENTITY: the Elateian learns only the cover story plus "a stone".

### [W-07] The father's slide show contradicts Ch.1 and Ch.7: dining room / tablecloth / winter vs kitchen / bedsheet / September
- **Audit:** Character / backstory consistency (past-facing memory).
- **Location:** p167, l.344.
- **Evidence:** Ch.13: "thrown six feet wide on the dining-room wall at home on a winter night when my father had his carousel out and the good tablecloth pinned across the dish cupboard for a screen". Ch.1: "I had seen them at our kitchen table every September of my childhood, projected onto a bedsheet thumbtacked over the china cabinet" (ch-01 l.23). Ch.7: "his voice in our dark kitchen" (ch-07 l.288). A habitual family ritual now has a different room, screen, furniture and season.
- **Fix (−5):** "thrown six feet wide across our kitchen one September night, when my father had his carousel out and a bedsheet tacked up over the china for a screen". (4-gram checked: does not repeat Ch.1's "over the china cabinet" or "a bedsheet thumbtacked".)
- **Cascade:** the bible's Ch.13 at-risk line ("the tablecloth screen") should be re-synced to whatever stands. The memory still obeys AUTHOR-CP2-2 (triggered by the painted door, returns into the speech, closes on an image, no lost name; Ch.11 and Ch.12 carry no longer memory).

### [W-09] Two anaphora triads and the broken "same … same … same" triad (retired reflexes)
- **Audit:** Voice drift (STATE guardrail "no anaphora triads"; bible after Ch.5: "the same… the same… the same" triad, broken).
- **Locations and fixes:**
  - p150, l.310: "the god had very kindly agreed with the clerk and with Kallia and with the whole of the lie." → "agreed with the clerk and Kallia and the whole of the lie." (−2)
  - p138, l.284: "that there was no road; that the hole I had come in by was the only one and it was shut; that I was a Syracusan now" → "that there was no road; the hole I had come in by was the only one and it was shut; that I was a Syracusan now" (−1)
  - p179, l.368: "came forward through it at the same pace, with the same stops in the same places" → "came forward through it at the same pace, every stop in its old place" (−2; "where it had been" avoided: it is a Ch.2 4-gram)
- **Cascade:** none.

### [W-10] Ch.11's hope frame reused: "By [time], if [providence] had any [virtue], I would be [home/gone]"
- **Audit:** Voice drift (narrator move the n-gram gate cannot see).
- **Location:** p115, l.238.
- **Evidence:** Ch.13: "By summer, if the god had any decency, I would be gone." Ch.11: "By then, if there was any justice anywhere, I would be standing in a kitchen in Philadelphia with a tap in it." (ch-11 l.196). Same skeleton two chapters apart, beside Ch.13's own imagined-first-hour-home passage (p109), which is a third hope-for-home beat in three chapters.
- **Also in the same paragraph (internal season slip):** the slave says the bowl "wants doing when the god's finished for the year" (autumn), and the narration calls it "a summer's work".
- **Fix (+1 net):** "It was a season's work, if I wanted it, cutting the smith's lead out of that bowl without marking the bronze, and I wanted none of it. I meant to be gone before the god had finished for the year."
- **Cascade:** none.

### [W-11] The votive ears rebuild Ch.5's clay women: one mold, one shared flaw on every piece
- **Audit:** Voice drift ("whole set pieces rebuilt", bible after Ch.10; the bible's own Ch.13 line "Clay votive ears / left ears off one mold: once" misses the Ch.5 precedent).
- **Location:** p116, l.240.
- **Evidence:** Ch.13: "all of them from a single mold … and each had the same chip out of the lobe where the mold was damaged". Ch.5: "the clay women … all pressed from one mold, with the same thumbprint on every hip" (ch-05 l.237).
- **Fix (0):** replace the chip clause with a non-mold detail: "…there was not a right ear on it, and somebody had given each one a dab of red inside, round the hole, and I was asking myself…". The left-ears joke and "the right-hand mold" stay.
- **Cascade:** none.

### [W-12] Two walk-on label/joke problems: "the Amphissan" now names two people; in-law joke-butt ×2
- **Audit:** Voice drift (bible after Ch.8: role labels as names; after Ch.9: "In-law as a joke-butt: cap 1 per chapter").
- **(a) Label collision.** Ch.11 "the Amphissan" is the quail owner whose bird Praxias's beat (×4, ch-11 l.312–l.398). Ch.13 gives the label to a different person, the well-woman (p102 l.212 "the Amphissan said"; p128 l.264 "The Amphissan's husband"). Book-wide the label now points at two people.
  - **Fix (+1):** l.212 "the Amphissan said" → "she said"; l.264 "The Amphissan's husband came out and walked straight past her" → "The man from Amphissa came out and walked straight past his wife".
- **(b) In-law joke-butts.** The well-woman: "South is where his mother planted her fig." (p100) and Theano: "not a crow of them made a sound, which his sister never managed." (p226).
  - **Fix (+2):** Theano's tail → "which is more than the mourners managed." (Keep the Amphissan's fig: the well dispute rests on it.)
- **Cascade:** none.

### [W-13] Theano explains her crows, against her card's "never explains"
- **Audit:** Character (bible THEANO: "Evasion — never says: anything comforting; any explanation"; foundation §3: "She never comforts and never explains"; the irrational behavior is meant to stay irrational).
- **Location:** p225–p226, l.462–l.464.
- **Evidence:** "Why give them any?" / "Because they come." … "They were up on that ridge the day my husband went out of this door feet first … A thing that'll sit quiet at a burying can have my barley."
- **Note:** the passage is strong, and the bible's draft block already celebrates it. The audit flags the conflict and does not rule on it.
- **Fix, either:** (a) **0 words:** keep it and amend her card ("explains herself once, about the crows; never about the god or the hour"). The orchestrator records this as a card change. (b) **≈−47:** stop at "Because they come." and cut the burying lines. That also clears W-12(b), but it spends half the word headroom.
- **Recommended:** (a), given the word floor.

### [W-14] Two voice-bank lifts: the reserved Ch.42 sample, and Ch.13's own register sample by structure
- **Audit:** Voice drift (voice-bank: "any phrase in a … voice-bank sample: 0"; "samples leak by structure as well as by string").
- **(a) sample-07 (Ch.42 "the door"), p167 l.344.** Mara: "A painted door on a tomb." Sample-07: "a painted door on a dead man's tomb". The 4-gram "a painted door on" is reserved for the book's climax. It is also the chapter's third "painted door" (at-risk table: "the painted door" max 2; vary).
  - **Fix (0):** "Tombs with their doors painted on."
- **(b) sample-03 (this chapter's register), p110 l.228 and p130 l.268.** Sample-03's "a murmur went along the line of waiting women" is split across two Ch.13 sentences: "passed along the line of us, looking up into each woman's face" and "he went along the women's faces".
  - **Fix (−2):** "came along below the wall, looking up into each woman's face in turn" ("worked his way" is avoided: the same slave "worked his way up" in ch-09 l.54); and "he searched the women's faces".
- **Cascade:** none.

### [W-15] Three narrator call-out pointers (cap ≤1, "treat it as 0", bible after Ch.8)
- **Audit:** Voice drift.
- **Evidence:**
  - p91, l.188: "On the terrace that morning he had kept it covered except to take hold of the horns." This retrofits a detail A1 never showed.
  - p211, l.434: "…small and brown: the brand that had been on the cake-trays at the altar that morning." p23 already planted the brand hard ("so that nobody should take the god's cakes for anybody else's").
  - p195, l.402: "I knew him for the boy from the altar, who had run for the jar." Keep this one: Mara has to identify him.
- **Fix:** cut the l.188 sentence (**−17**). Optional: end l.434 at "small and brown." (−13 more; the reader makes the link, and "The brand on the basket was by her foot. I left it there." then lands unannounced).
- **Cascade:** none.

### [W-16] A betting comparison vehicle after Ch.12 closed the domain
- **Audit:** Voice drift (bible after Ch.12: "the horse-bettor … is its last use. A vehicle domain is used once").
- **Location:** p23, l.50.
- **Evidence:** "the leaves sat on his cropped head like something another man had put there for a bet." In Ch.12, l.8: "the way a man looked at a horse he had once had money on".
- **Fix (0):** "…like something another man had put there while he slept."

### [W-17] Lentils as a joke (SPENT)
- **Audit:** Voice drift (bible after Ch.8: "'lentils' as a joke: SPENT"; Kallia's sample line was replaced for the same reason).
- **Location:** p184, l.376.
- **Evidence:** "and it was as much use to me as a bowl of cold lentils." Kallia's literal pot and bowl of lentils (l.22, l.100) are fine.
- **Fix (+2):** "…as much use to me as a map with no names on it."

### [W-18] The ibuprofen: "the bottle" is unidentified after ten chapters, and "the last two" is not on the page
- **Audit:** Objects (outline Ch.13 object beat: "the last two ibuprofen"; ENTITY `ibuprofen`, last on the page ch-03 "the Advil bottle chattered").
- **Location:** p29, l.62 (first mention); p220, l.452.
- **Evidence:** "I had the bottle in my belt." The reader last met the Advil bottle in the dark of the cave in Ch.3. Nothing says how many remain, so the gift to Theano does not read as Mara's last.
- **Fix (+6):** "I had the Advil bottle in my belt, with the last two in it." l.452 ("I shook the two pills out of it") then reads as emptying it.
- **Cascade:** ENTITY `ibuprofen` → status closed / used up, Ch.13. The optional Ch.32 past-facing line stays available.

### [W-19] "out of the rag and out of the coins from the ford": the coins are in the rag
- **Audit:** Objects (Ch.12 l.278: "I untied my rag and tipped the dead man's silver in with the little that was mine, and knotted it again.").
- **Location:** p25, l.54.
- **Evidence:** "I paid him first, at the wall, out of the rag and out of the coins from the ford, into his palm." The coins are not a second store. (Not itemized: this complies with the bible's money rule.)
- **Fix (−3):** "…out of the rag, in coins from the ford, into his palm."

### [W-20] One-sentence opening paragraph; the ledger allows it only in Ch.4, 24, 30, 36, 42
- **Audit:** Ledger / anti-predictability (outline legend: "an opening paragraph may be a single sentence ONLY in Ch.4, 24, 30, 36 and 42").
- **Location:** p1, l.6, a single 43-word sentence. shape_check does not test this. Ch.3 (opening) and Ch.4 (closing) already slipped past it, so the one-liner budget is overdrawn.
- **Fix (0):** merge p1 and p2 into one paragraph ("…smoked in the dark. The priests were higher up…"). The `scene-set` sig is unchanged (the first sentence is the same).

### [W-21] Bible's Ch.13 blocks quote the draft, not this page
- **Audit:** Bookkeeping, for the orchestrator. The Ch.12 audit's W-22 found the same pattern.
- **Evidence:** the bible has lines this page does not carry:
  - THEANO: "They made a mountain out of it"; the page has "They put a mountain in it".
  - THEANO: "Keep your silver. You'll want it for a boat."; the page has "Keep your silver. Whatever's paid on this hill goes to the priests, and I get the steps."
  - THEANO: "Not mine to give you," … as a second refusal.
  - FELIX: "Was it a stone?"; the page has "It wasn't a stone, was it?"
  - At-risk after Ch.13 lists "The airport-gate memory", which is not on the page, and "bare 'No.' 0"; the page has 1 (p151).
- **Fix:** re-sync the bible to the final page after the editor pass. Quote the page.

---

## INFO (polish / tracking / cascades)

**History and world rules**
- **I-01 Goat drench ✓.** Plutarch (*De def. or.* 437a–b): cold water poured on the victim, which must tremble through every limb from the hooves; not a toss of the head. p43 matches it ("It began in her hooves and climbed through all four legs"), as do Euthydikos's Ch.9 terms ("from the hooves up, every leg of it"). The extra jar is period-true. Plutarch records priests over-drenching under pressure. Mara does not think of that anecdote; good, since it postdates AD 71.
- **I-02 Pelanos / cake ✓.** Ch.9 made the pelanos a fee "into the god's treasury"; Ch.13 separates the stamped honey-and-meal cake carried in (p23, p13) and never re-itemizes the price (the bible's money rule is honored). By the Roman period the pelanos was effectively a cash fee, so the split is right.
- **I-03 Proxenos.** Praxias "son of Kleon, of Delphi, for the house of Kallia" (p50) works as Ch.9's "a Delphian to stand for you". Formally a foreigner was introduced by her city's *proxenos*. Euthydikos's Ch.9 archive remark leaves Syracuse's terms open, and Mara is registered as a Delphian widow's kinswoman, so a household sponsor is defensible. No change.
- **I-04 Queue order.** "Delphians had gone in first" ✓ (Delphian priority). "Coans who had paid to go ahead of somebody" (p99): *promanteia* was a granted honor, not a fee. This is Mara's sardonic reading and can stand. Strict option: "who had the right to go ahead of somebody".
- **I-05 Monthly days ✓.** Praxias (Ch.11: "The god sits every month now till the winter"), Praxias here ("Next month"), and Theano agree. Theano's "every month he sits" (p218) can be read as every *sitting* month; the card says "the warm season". No change.
- **I-06 The Pythia ✓.**
  - Widowhood and age agree with Diodorus 16.26 (over fifty; the bible notes it).
  - Celibacy: a widow living alone; it is not stated and does not need to be.
  - The "three of us … now there's only me" line follows Plutarch (*De def. or.* 414b: two and a reserve once, one now).
  - Her own farm house with a loom and a nephew's ewes: no ancient source requires the Pythia to live inside the precinct, and Plutarch's peasant-born Pythia supports it.
  - "Seven steps down", and the climb between consultants (p215), are fiction-plausible. Valens's "She's down there" (p79) does not contradict a climb between turns.
- **I-07 Sanctuary furniture ✓.**
  - The Chian altar: dark stone with a white marble lip.
  - The gilt shields on the temple front.
  - The Corcyraean bronze bull at the gate.
  - The pronaos maxims: "Know yourself", "Nothing too much".
  - Laurel and barley on the inner hearth.
  - The omphalos with its woollen net (*agrenon*).
  - Pindar's iron chair (Pausanias 10.24.5). Pindar was a Boeotian, and "five hundred years" is close enough (c. 540).
  - Lion-head spouts at the spring, as in Ch.5 and Ch.7.
  - Almond blossom and frost fit Bysios (Feb/Mar) and the Ch.12 plane buds.
  - The Tomb of the Augurs at Tarquinia has a painted false door flanked by two mourners, hand to brow.
- **I-08 Hexameter ✓.** In AD 71 prose responses were common, and priests versified (Plutarch *De Pyth. or.*). "It scanned … the last part had been left to hang off the end" is exactly right, and Theano's "put shoes on it" confirms it from below.
- **I-09 "Pompeii": named and spelled correctly.** It is the book's first occurrence (grep: none in Ch.1–12) ✓, and it matches canon ARCH-4 / outline Ch.13 / foundation §6 item 4. In Theano's Greek the form would be *Pompēïa* (Strabo's Πομπαΐα); the English convention "Pompeii" is right for the page and matches the Part Two datelines. It is spoken off duty, woman to woman, as designed.
- **I-10 Valens and the foreign word.** A Latin speaker who served a Roman legate's house would probably hear *Pompēïa* as a name like Pompeius. "A word in it I didn't know, not Greek" can stand (a place name he does not know), but an evaluator may poke at it. Optional (+4): "…not Greek; a name, I thought". Not recommended: it would push Mara toward Italy before Theano.

**Timeline**
- **I-11 Ch.12 bridge exact ✓.**
  - Road day = D, the 4th of Bysios ("three days to the seventh").
  - The donkey man's story at the spring "the morning following" (D+1), as Ch.12 predicted.
  - Boxing and the Elateian's question "yesterday" (D+2).
  - Goat "at the yard since sundown yesterday", as Valens said ("the evening before").
  - Consultation at dawn on D+3: "not had her to myself in three days".
- **I-12** No moon is named. The 7th of a lunar month puts the moon down before dawn, which fits "The lane was still black". Kallia's "The boats go west at the new moon" is about three weeks off: a thread for Ch.14's plan ("the sea in spring").
- **I-13** The imagined homecoming falls "in the summer", yet she turns the heat on (p109). That is a cold woman's fantasy; logic-minded readers may notice. Optional: cut "and I would turn it on and stand over the vent in the hall in my socks until it ran warm" (−21). Not recommended at this length.

**Information flow**
- **I-14 Who hears the answer ✓.** Valens recites it in the court to Mara and Felix (stair), with Kallia listening from the lean-to (p48, p146). Praxias is refused it (p97). Euthydikos/the priest and the Boeotian heard it inside. Theano heard what she said and what the priests made of it.
- **I-15 "Pompeii": Mara alone ✓.** The jug boy is gone downhill (p211) and Valens is at the corner below (p203). This matches Ch.15's plan, where she tells Valens "the old woman told her".
- **I-16 Felix hears nothing of the arena ✓.** He is on the stair for the god's book, the porch, the answer and "Italy … Capua" (p162). He is sent off before "A trainer at the school called the forms" (p180) and "Mine's written. At Corinth." (p187). His Capua line is his own arena-mania, not knowledge of Valens.
- **I-17 Kallia told the whole story ✓.** Ch.12 authorized it ("She gets the whole of it from me" / "Kallia, then. Nobody else."). New Kallia knowledge:
  - the killing;
  - Valens = the arena man (the sword at Corinth) and the frame;
  - the notice's five hundred;
  - "a heavy thing from my bag" (not shown).

  Her guardian's decision ("You'll sleep here", "There's floor") sets up outline Ch.14 beat 4.
- **I-18 Comprehension ✓.**
  - Mara catches only fragments of the jug boy's fast message ("no men", "muleteer", crows; p201), which is a good partial.
  - Theano speaks "slowly, taking her breath where she could get it" (p215), which supports full comprehension of the long complaint.
- **I-19 Euthydikos "knew the face" (p52) and the god's book now carries "Felix" as the carrier (p54).** This is a small new exposure for the Celer thread: a priest has seen Valens at close range on a recorded day. Nothing contradicts it; tracker note only.

**Canon**
- **I-20 WHERE / WHEN ✓.** The public answer is the first and only early WHERE; the priest gave nothing on *when* ("No.", p151). Theano: "That's not mine to give you." / "Or it was never given me. Which of those it is, is mine to know." / "Keep your silver." / "You've had your answer to that." Nothing comforts, nothing hints at an hour. The answer is rendered once, standing ✓. Nothing points at the match with Mara's written question ✓.
- **I-21 Forward reach.** Narration has no foreknowledge, significance-tagging or outcome forms (gate 0, and by hand). "By summer … I would be gone" (W-10) and the imagined first hour home are present hope.

**Objects**
- **I-22 Watch:** absent ✓ (next touch Ch.18). **Lens cap:** never mentioned ✓. **Camera:** p5 "the thing of my father's … a heavy thing from my bag" and p124 "your father's silver thing" both agree with Ch.12 (Felix took it for silver, was told "It was my father's"). Valens does not raise it ✓.

**Plot threads**
- **I-23 Celer.** Valens scans the crowd ("Have you seen them?" / "If you see the one you hit…", p34–p35). This is consistent with his Ch.12 reasoning that they will want him "on a road, not in a crowd": he watches anyway, without contradiction. The wine-stained Phocian boy is a clean false alarm. No new knowledge of who sent the men (CH12-5 open).
- **I-24 CH12-2 / CH12-8** untouched in substance (see the ENTITY table).
- **I-25 New threads:**
  - Mara's "You'll try the cave again" / "Tomorrow." (p174), which Ch.14 must drop or explain now that the door is "Pompeii";
  - Euthydikos's bowl ("You'll be sent for.");
  - Felix's "If it's Italy, can I come?" (unanswered; Ch.18–19);
  - Kallia's new-moon boats;
  - Valens sleeping at Kallia's (Ch.14 beat 4).
- **I-26** "what Valens had told me standing in it" (p5). In Ch.12 he began at the fall and then "sat on the lip of the pool with his boots in it". This is loose but not wrong. Optional (0): "at the foot of it".
- **I-27** "the painted notice by our colonnade" (p5). Ch.9 has it "pegged to a pillar of the colonnade in the square". "our" is odd. Optional (0): "the painted notice in the square".

**Voice (registries; below the WARN line)**
- **I-28 Counts on this page:**
  - bare "No." 1, Valens, at the cap ✓;
  - Valens walk-offs 2;
  - Kallia never sits ✓;
  - Kallia "Then…" retorts 0;
  - "said/told the [non-listener]" 1 ("said Theano, to the crows") ✓;
  - em-dashes 2;
  - "the one / the only" claims 3 (cap 3: "the only part of the morning", "the only one" for the hole, "the only way I knew"; the last is a cliché, optional "I took hold of it with what I had");
  - "Then…" speech openers 1;
  - credential asides 0;
  - Felix "Is…" 0 ✓ (the bible's WATCH);
  - Felix "nobody" 0;
  - no teeth, laughs, English, cloth smells, lying-awake coda or knot near Valens.
- **I-29 Ch.14 note (from C-01):** once the bay is cut, Mara's list skips Campania. Her father's survey makes that a blind spot Ch.14 may choose to remember.
- **I-30 Small items, each optional:**
  - Praxias's "little—" (p30) stops short of the capped "little cousin" but still calls it back. Cutting "little—" He stopped himself, and liked himself for it. would cost −10 and an em-dash; fine to keep as his one near-miss.
  - Praxias's "Even money she stands like a post … They do, in a frost" half re-explains the shiver rule (bible: "explained once … Ch.12–13's goat is shown"). It is framed as odds, so it can stand.
  - The jug boy's "ten or so, in a white tunic" (p195) follows Felix's "twelve or so" introduction (Ch.11): the age-hedge-plus-clothing skeleton for boys, second use; vary next time.
  - Theano's "the day my husband went out of this door feet first" rhymes with "where the dead go out". It is in her speech, not narration, and can stay, but the bible's "door" WATCH should note it.
  - "Her by herself," he told Valens (p201) comes right after "Valens stood.", so "he" is ambiguous. Optional (+1): "the boy told Valens".
  - sample-01's "the wind off the [valley]" vs p18 "the wind off the gorge", and sample-10's "came in under" (reserved Ch.15) vs p1 "came in under a frost": 3-gram coincidences, different sense; no action.
  - The Elateian boxer may be Kallia's lodger "a priest's cousin from Elateia" (Ch.12). The page does not say, and Felix introduces him as a stranger. Keep them unlinked or link them later; do not contradict.

---

## Word ledger (recommended fixes only)

| Fix | Δ words | Δ dialogue |
|---|---|---|
| C-01 Massalia | −3 | −3 |
| W-01 Etna | +2 | — |
| W-02 stadium uphill | +1 | — |
| W-03 all that week | 0 | — |
| W-04 eating their victims | 0 | — |
| W-05 half the night | +1 | +1 |
| W-06 what the man was hit with | 0 | 0 |
| W-07 kitchen / bedsheet / September | −5 | — |
| W-09 triads ×3 | −5 | — |
| W-10 season's work / gone before the god finished | +1 | — |
| W-11 votive clause swap | 0 | — |
| W-12 Amphissan label (+1) + mourners (+2) | +3 | +2 |
| W-13 (a) card amendment | 0 | — |
| W-14 tombs (0) / came along below the wall, searched (−2) | −2 | 0 |
| W-15 cut the l.188 sentence | −17 | — |
| W-16 while he slept | 0 | — |
| W-17 map with no names | +2 | — |
| W-18 Advil, last two | +6 | — |
| W-19 rag | −3 | — |
| W-20 merge p1+p2 | 0 | — |
| **Net** | **≈ −19 → ~7,568** | **0 → ≈ 37.9%** |

Optional, not in the net: W-15 brand tail (−13); W-13(b) (≈−47); I-13 (−21). Any one or two keep the chapter over 7,500; **all three together (≈7,487) drop it under the floor.**

---

## SUGGESTED YAML PATCHES (for the entity-tracker UPDATE after the editor's fixes)

```yaml
suggested_patches:
  - entity: "meta.contradictions.CH8-2"
    action: "resolve"
    reason: "Ch.13 recognises Theano by situation (house next to the highest, squared stone, crows, barley over the ruts, hands on knees; l.430-l.442) and supplies the plan's god's barley (laurel brand on the basket, l.434) and the lie ('That's my own barley', l.460)"
  - entity: "theano"
    action: "update"
    value: { first_live: "ch-13", named_by: "the jug boy; Kallia ('The god's woman')", facts: ["widow fourteen years, Pythia since", "three Pythias once, now only her", "nephew keeps her ewes and the cheese money", "her husband's stone at the door", "one room, loom, striped blanket, cat in the ash"], knowledge: ["heard the carrier stand still at the screen", "the non-Greek word given twice = 'Pompeii'"], said_to_mara: "Pompeii (the chapter's last word)" }
  - entity: "mara-reyes.knowledge"
    action: "add"
    value: [{ fact: "the god's public answer, word for word (via Valens)", learned: "ch-13:p142", method: "told_by:valens" }, { fact: "the city is Pompeii", learned: "ch-13:p246", method: "told_by:theano", note: "no one else present" }, { fact: "the priest read the mountain as Etna; nothing given about when", learned: "ch-13:p149; ch-13:p151", method: "told_by:valens" }]
  - entity: "kallia.knowledge"
    action: "add"
    value: [{ fact: "the whole Kirrha road story: the man who knew Valens from the sand, the knife, the ditch, Mara's blow with 'a heavy thing from my bag', Valens's telling from the Corinth sword to the notice (five hundred), the hairdresser", learned: "ch-13:p5-p9", method: "told_by:mara" }, { fact: "the god's answer and the priest's Etna gloss", learned: "ch-13:p142; ch-13:p149", method: "overheard (lean-to)" }]
  - entity: "felix.knowledge"
    action: "add"
    value: [{ fact: "his name is in the god's book as the carrier", learned: "ch-13:p54", method: "told_by:valens" }, { fact: "the god's answer; the priest's Etna gloss", learned: "ch-13:p142-p149", method: "witnessed" }]
    note: "still nothing of Lupus, the arena past or Corinth (sent off before p180, p187)"
  - entity: "valens"
    action: "update"
    value: { ch13: "gave 'Felix' as the carrier's name to the registrar; his own 'written. At Corinth.'; Euthydikos 'knew the face'; sleeps at Kallia's tonight", injuries_ch13: "cheekbone scrape crusted; left-forearm bruise purple to yellow; left knuckles scabbed; shoulders held 'all of a piece'" }
  - entity: "ibuprofen"
    action: "update"
    value: { status: "used up", paid: 13, last_mentioned_manuscript: "ch-13:p223" }
  - entity: "praxias"
    action: "update"
    value: { patronymic: "son of Kleon", ch13: "paid at the wall from the rag (dead man's silver, no sum); calls his name twice at the door; refused the answer for the quail ring" }
  - entity: "euthydikos"
    action: "update"
    value: { ch13: "the registrar at the door ('Beard cut square'; nose 'a hand from mine') and, by the narration and Theano's 'the square beard', the priest at the screen; his bowl summons pending ('You'll be sent for.')" }
  - entity: "new walk-ons (ch-13)"
    action: "create"
    value: ["the-jug-boy (temple boy, ~10, white tunic; 'Forty-one jars')", "the-amphissan-well-woman (+ her husband) — NOT ch-11's quail-owning Amphissan", "elateian-boxer (live; ears; 'that knuckle killed the man')", "boeotian-on-the-bench (boundary-stone question; prayed throughout)", "omphalos-watcher (cough)", "altar-priest (thin; himation pinned high)", "phocian-boy-with-wine-bandage (+ friend)", "thessalian-family-with-black-ram", "island-fig-seller ('Chian')", "clay-ear-seller", "theanos-husband (dead)", "theanos-husbands-sister", "theanos-sisters-son", "theanos-cat", "pindar (mention)", "felixs-mother (mention, once)"]
  - entity: "plot_threads"
    action: "add"
    value: ["cave-try-tomorrow (ch-13:p174; Ch.14 must drop or explain)", "felix-italy-capua (unanswered)", "boats-west-new-moon (Kallia)", "euthydikos-bowl (summons pending)"]
  - entity: "meta.contradictions.CH12-9"
    action: "narrow"
    reason: "the goat's arrival at the yard the evening before is now on the page (ch-13:p19)"
```
