# Continuity Audit: Chapter 17 (run 2, per-chapter drift audit)

**Date:** 2026-10-21
**Mode:** MANUSCRIPT AUDIT. Ch.17 "Games on the Isthmus" (post-disruptor) is checked against:
- Ch.1–16 as they stand on disk;
- ENTITY_STATE.yaml as of Ch.16 (read only; the tracker update is running in parallel and this audit does not touch it);
- outline.md (Ch.17, plus Ch.18 for the handoff and Ch.22 for the legal thread);
- foundation.md (§3, Celer's card, §9, §10), voice-dna.md, character-bible.md, voice-bank samples;
- STATE.yaml guardrails and resolved_author_decisions (AUTHOR-CP3-3, CP3-5, END-1).

**Chapter reviewed:** `manuscript/chapters/chapter-17.md`
- **Length:** **6,923** prose words by shape_check (6,935 style; 6,939 show_tell; 7,518 `wc -w` with the header). The floor is **6,900**, so there are only **23 words of headroom**. Every fix below is word-neutral or adds words. If you apply all the CRIT and WARN text fixes, the net is about **+12** (see the word ledger).
- **Shape:** dialogue **33.0%** (band 30–40; floor 30). 3 breaks, 4 sections. Median sentence 11 (gear low). The opener is `short-punch`: "The boards left their dust on my fingers." (8 words). The close is `quiet`: the chapter stops mid-run. All of this matches the ledger row.
- **Citations:** `l.NN` is the file line in chapter-17.md. Lines in other chapters are cited as `ChN l.NN`.

**Mechanical baseline** (`bash tools/check_chapter.sh 17`, run read only): **ALL CLEAN.**
- Style clean (simile 1.2/1k, em-dash 0); grammar 0 errors (1 report); rhythm 0 flagged.
- Show/tell: dialogue 33.0%, no flags. Voice-wear strict clean.
- Tic gate clean, gesture classes included. And-chains 3 (cap 9). Credential asides 0 by the gate, 1 by hand (l.60, the accession numbers; this is the outline's one permitted recognition).
- `tic_report.py --echoes 17`: **0 echoes, 0 spoken-line echoes.** One command-echo candidate ("His father thinks he'll run at Olympia." → "he took his loaves up the step") is a false positive.
- Metaphor 1.3 fig/1k; 3.5% of sentences over 40 words. Shape audit: SHAPE CLEAN.

**My own sweeps:**
- 4–6-grams of Ch.17 against Ch.1–16 and every voice-bank sample, with stop-word-bounded grams included. This found one voice-bank lift the echo gate missed (W-06).
- Intra-chapter 4-grams.
- A time-of-day walk through all four sections plus the backfill.
- The Ch.16 plan set beside the Ch.17 execution, beat by beat.
- An information-flow table for every speaker.
- The Kirrha-road man traced through Ch.12 → Ch.15 → Ch.17.
- The four objects (camera, bracelet, pen-knife, leaf), the pine crown and the flashlight traced.
- Celer's card rules counted line by line.
- Escort-animal and command beats counted across Ch.11–17.

**Total findings: 33. CRITICAL: 1 | WARN: 10 | INFO: 22**

**Summary**
- **One CRITICAL (C-01, timeline):**
  - The backfill puts the litter leaving the brother's door, and Mara treading on Plautia's hem, "in the dark" (l.34, l.450).
  - That cannot fit the rest of the day. Plautia watched the procession leave from the roof "with the sky still gray" before she left (l.176). The plan was to go in "at the hour the boys run" (Ch.16 l.480). The city had already "emptied itself for the games" when the litter crossed it (l.34). And it is "near enough noon" when Mara reaches the oven (l.264), after a scene that lasts perhaps an hour.
  - The fix is two small swaps (+4 words).
- **Canon points the brief asked about all hold:**
  - never "Isthmia" (0 hits; CP3-5 kept);
  - the boys' race, the Isthmus precinct, pine crowns and sausage sellers;
  - the Lechaion road topography (stepped and colonnaded, the arch with the bronze chariot, the fountain beside it, the old wall, market gardens, about 3 km), which agrees with Ch.16 l.460;
  - the afternoon breeze, consistent with the book's day wind (Ch.12 l.244, Ch.16 l.408);
  - Onesimus as Ch.16's gray-haired clerk ("We had wanted the other.");
  - the man Mara hit, recognisable by the wound she gave him and by his "Mistress";
  - Celer's knowledge paths (name, camera, Syracuse);
  - Celer to his card: genial, contractions, "we", never "wife", no threat, no violence, the scaffold aversion shown;
  - the leaf's legal content;
  - Plautia's marriage in autumn 63, which fits Marcus born in autumn 64;
  - foreshadowing 0 by reading;
  - no pregnancy-gap line (CP3-3);
  - nothing that touches END-1.
- **The WARNs:**
  - three dating slips: Nero's year (W-01), the notices "last year" (W-02), Plautia "since I was sixteen" (W-04);
  - a seating-law contradiction with Ch.16 (W-03);
  - one narrator-knowledge slip, "the Greek of Alexandria" (W-05);
  - a voice-bank lift from sample-01 (W-06);
  - an escort-dog beat now used in consecutive chapters (W-07);
  - three handoff constraints for Ch.18 and Ch.22 (W-08 to W-10).

---

## CRITICAL (fix before the evaluator)

### [C-01] The departure "in the dark" contradicts the gray-dawn roof scene, the plan's hour and noon at the oven
- **Audit:** Timeline (2b), logical sequence.
- **Evidence:**
  - l.34: "She had told me so at the brother's door **in the dark**, while the bearers were lifting her … The bearers had carried her through a city that had emptied itself for the games and barred its doors behind it: shutters down along every street…"
  - l.450: "Twice. In the street, **in the dark**."
  - l.176: "That morning, on the brother's roof, **with the sky still gray**, Plautia had stood at the parapet in her cloak and watched the procession go out…" (This comes *before* the litter: she is on the roof, then in the litter.)
  - Ch.16 l.480: "I will go in myself, on the second morning, **at the hour the boys run**, when the office is emptiest."
  - l.28: "The boys race out on the Isthmus this morning." (The race is still to come when they arrive.)
  - l.264: "It's near enough noon." (Mara reaches the lane after one ladder trip and one reading of the dowry.)
  - l.336: Celer left the Isthmus *before* the boys ran ("so he'll shout himself hoarse"). He is in the forum before noon, which puts the theft in the late morning.
- **Why it is CRITICAL:** two time anchors run backward. The roof is gray, and then the street is dark. If the litter left in the dark, the S1 scene would have to fill about five hours before noon, and the city could not yet have "emptied itself" behind a procession that had not left.
- **Minimal fix (+4 words, no speech removed):**
  - l.34: "at the brother's door in the dark, while" → "at the brother's door, **in the shade of the porch**, while" (+3). The porch is Ch.16's: "In the brother's porch a dog on a chain…", l.460.
  - l.450: "Twice. In the street, in the dark." → "Twice. In the street, **by the fuller's**." (+1). The fuller's door is across from the brother's house in Ch.16 l.280 ("across the street from the fuller's door"), and l.34 already has "a fuller's vats standing full and untrodden". Dialogue words go up by 1.
- **Cascade risk:** none. The "before dawn" water (l.82) and the lamplight packing (l.116) stay true, because both come before the roof scene. Afterwards, check that nothing else in S1 places the arrival at first light (nothing does).

---

## WARN (should fix; a careful reader may notice)

### [W-01] "The year Nero came" against "early in that year" and "five years"
- **Audit:** World rules / history; internal consistency with Ch.5 and Ch.16.
- **Evidence:**
  - l.58: "Vettius and Caninius, **the year Nero came**."
  - Ch.5 l.105: "Nero had come to Greece for the games in sixty-six and stayed into sixty-seven." (Mara knows the arrival is late in 66.)
  - Ch.16 l.552: "near the front, because **the emperor's games were early in that year**".
  - l.138: "It had lain in those holes **five years**". That gives AD 67.
- **Problem:** Nero arrived in autumn 66, so a year whose *early* months held his games is 67. That is the year he was in Greece, not the year he came. Ch.12 l.16 already uses the safe form: "The year the emperor was in Greece."
- **Fix (+1):** l.58 "the year Nero came" → "**the year Nero was here**". Optionally also update the character-bible walk-on line ("the duoviri of the year Nero came").

### [W-02] Celer's notices "last year" against Dadaphorios AD 70
- **Audit:** Timeline.
- **Evidence:**
  - l.364: "My steward put up some notices, **last year**."
  - Ch.9 l.352: "Copied from the notice posted at Corinth **in the month Dadaphorios**." That is about November/December AD 70.
  - Ch.12 l.208: "Last autumn a freedman … Inside the month that notice went up" (spoken in spring 71).
- **Problem:** in spring 72, "last year" is 71. No notice went up in 71 on the page.
- **Fix (+2):** "last year" → "**the autumn before last**". Alternatively "a while back" (+1), which is vaguer and also suits Celer's ease.

### [W-03] Celer invites Plautia to sit "right at the governor's back", against Ch.16's women's benches
- **Audit:** World rules (4c), consistency of an on-page social rule.
- **Evidence:**
  - l.340: "Sit with us tomorrow, why don't you? **Right at the governor's back**, where everybody can see how well we all get on."
  - Ch.16 l.54: "once at the theater, from the women's benches at the top".
  - Ch.16 l.514: "From the women's benches at the top, over the heads of half Corinth, while one race is run. I have done that."
  - Ch.16 l.566: "Where the wives sit".
- **Problem:** the book has twice set the rule that women sit at the top (the Augustan seating law, applied in a colony). The second row is for men and their sons (Marcus "in the second row … beside his father", Ch.16 l.510). As written, Celer offers something the page has said is impossible, and nothing on the page marks it as a taunt.
- **Fix (+2; keeps his "we" and the sting):** "Sit with us tomorrow, why don't you? Right at the governor's back, where everybody…" → "**Come out tomorrow, why don't you? Look down on us from the women's benches**, where everybody can see how well we all get on." This also fits Ch.16 l.514 (the top, "over the heads of half Corinth").

### [W-04] Plautia "since I was sixteen" against Mara's "thirty, or a little under"
- **Audit:** Character consistency (1b, age).
- **Evidence:**
  - l.430: "I have been by myself in front of that man **since I was sixteen**".
  - l.100: "I was married in the autumn." In the year "before the great fire" (l.40, l.48), that is autumn AD 63.
  - Ch.16 l.20: "thirty, or a little under".
- **Problem:** married at 16 in 63 makes her about 24 or 25 in spring 72. Mara saw a woman of about 28–30 who has been kept from the sun all her life. Mara's eye for surfaces is her primary axis, so a five-year misjudgement reads as an error, not a characterization.
- **Fix (word-neutral):** "sixteen" → "**nineteen**". That makes her born about 44 and about 28 in 72, which fits Ch.16. Nothing else on the page dates her. ENTITY should record the age.

### [W-05] "In the Greek of Alexandria": the narrator cannot identify that accent
- **Audit:** Information flow (narrator knowledge) / comprehension.
- **Evidence:** l.500: "'Murmillo,' he said, **in the Greek of Alexandria**, to Valens's chest."
- **Problem:** Mara's Greek is classroom Attic learned by ear in Phocis ("my Greek is from Phocis … When it runs, I lose it", Ch.16 l.28). Nothing has given her an ear for Egyptian Koine. The character bible's "Alexandrian trainer" is a writer's label, and it has leaked into the narration.
- **Fix (+2):** → "in a Greek that was not Corinth's," or "in a Greek from somewhere far down the sea," (+4).

### [W-06] A voice-bank lift: sample-01's sausage seller, "the smell of fat and …", and the slung tray
- **Audit:** Voice drift (voice-bank lifts). The echo gate missed it because the 4-gram is bounded by stop-words.
- **Evidence:**
  - sample-01 l.2: "A man beside me was selling **sausages from a tray slung** around his neck. **The smell of fat and** fennel came and went…"
  - l.494: "A sausage-man … The coils on his grill spat and smoked, filling the colonnade with **the smell of fat and** cumin."
  - l.492: "a man had **a tray of new silver slung** from a strap".
- **Problem:** this is the same street seller, the same smell frame and the same slung tray, in two adjacent paragraphs. The samples are benchmarks, never source text.
- **Fix (word-neutral):**
  - l.494: "spat and smoked, filling the colonnade with the smell of fat and cumin." → "spat and smoked, **and the whole colonnade reeked of scorched fat and cumin**." (10 → 10)
  - l.492: "a tray of new silver slung from a strap" → "a tray of new silver **hung** from a strap" (0).

### [W-07] The escort dog is now in consecutive chapters (an emerging situation device)
- **Audit:** Voice drift / NO TICS (repeated situation beat).
- **Evidence:**
  - l.560: "**A dog burst from a garden gate and ran with us for a stretch**, delighted, and dropped off."
  - Ch.16 l.108: "**A dog joined me from among the treasuries and walked at my side to the precinct gate**, and stretched across it there, its duty done."
  - The same beat also occurs at Ch.16 l.324 ("the dog followed for the bowl's sake") and Ch.11 l.564 ("the dog … went with him").
- **Problem:** a stray dog that attaches itself for a stretch and then leaves has now been used four times in seven chapters, twice in this exact shape back to back. The disruptor kept it deliberately ("trainer 'delighted' cut (dog's kept)"), but it is a situation shape, and the gesture gate cannot count it.
- **Fix (+1):** change the animal and the action: "**A gander came hissing out of a garden gate at our heels, and thought better of it at the ditch.**"

### [W-08] Ch.18 handoff: the outline's opener example and its "one hour on a quay" do not fit how Ch.17 ends
- **Audit:** Plot thread / handoff.
- **Evidence:**
  - Ch.17 ends with the sun "a little past its height" at the gate (l.536). The breeze has just arrived ("That's the breeze", l.546), the ship "goes out on the afternoon breeze, whoever's on it" (l.290), and "a sail was going up" (l.560).
  - The outline's Ch.18 opening example is "awake since the second watch, **sitting on their bags**", and its shape is "*one hour on a quay*".
- **Problem:** they cannot have been sitting on their bags. Felix and the mules were on the quay from before sunrise, and Mara arrives running in the early afternoon. An hour of the captain's terms, the wedding and the mule may also be too long if the sail going up is their ship's.
- **Fix:** no Ch.17 change. Patch the outline before the Ch.18 writer runs:
  - The opener stays an I-statement over 8 words, but it should be an in-moment fact on arrival. For example, Mara has been awake since the second watch, and her lungs or her hem are still in it. The bags are with Felix.
  - Either the raised sail belongs to another ship, or Ch.18 runs in well under an hour. "A ship that won't wait" already allows this.
  - The ship has "the goose carved on her stern" (l.290). It sails for Puteoli (l.424).
  - The quay is dry in the sun (the outline says "wet quay"; spray is fine, rain is not).
  - The watch reads early afternoon, which agrees with "near enough to the sun's noon".

### [W-09] Ch.18 handoff: Valens has promised Myrrhine "on the quay before us"
- **Audit:** Plot thread (5a, opened).
- **Evidence:**
  - l.116: Myrrhine: "Everything in this case comes home tonight. If it goes to anybody else, I shall know whose house."
  - l.440: Plautia gives Mara the knife ("It belongs with whoever knows what it is for.").
  - l.444: "Myrrhine will find you,"
  - l.456: Valens: "**Her woman will be on the quay before us.** Walk."
- **Problem:** outline Ch.18 has only Felix and a sailor on the quay. The character bible says "Ch.18 is not bound to bring her". But a line in Valens's mouth sets a concrete expectation, and the pen-knife is in Mara's belt (l.454). If Ch.18 never mentions her, the reader is left with a dangling thread.
- **Fix:** either Ch.18 spends one clause on it (Myrrhine on the quay with a drachma, or her absence noticed; the knife bought back or kept), or Ch.17 softens the line. A word-neutral option for l.456: "Her woman will be on the quay before us." → "**Her woman will be at Lechaion before the week's out.**" (+1). That keeps the buy-back joke without binding Ch.18 to a scene.

### [W-10] Ch.22 handoff: the leaf carries no seal, and Celer now holds the cut book
- **Audit:** Plot thread / legal logic (5c risk for Ch.22).
- **Evidence:**
  - l.76: the seals are on the knot ("The knot was buried in a lump of red wax with two seals").
  - l.124: Mara cut "as far from the seals as it ran".
  - l.148: "a second knot … small and pale and naked, with no wax on it".
  - l.396: "the book went with him, lighter by two boards".
  - l.370: "there's a line in a magistrate's book … and a judge … chooses."
- **The logic in Ch.17 holds:**
  - Celer concedes that the line exists. His claim is a prior sale.
  - The leaf names the lanista as master freeing him "before the magistrate of the games and before the emperor" with nine witnesses (Ch.16 l.552; l.90). That is direct evidence against a sale a month earlier.
  - Celer taking the book does not change his claim. It does give him the official volume with its fresh second knot and its gap. Once he opens it, he knows who took the leaf, because he saw Plautia there that morning.
- **What Ch.22 must answer:**
  - How an unsealed, removed leaf is authenticated in Rome. The options are the duovir's hand, the six living witnesses, Onesimus, or the cut book itself, if Celer is made to produce it.
  - Whether Celer's side alleges theft from the public record.
  - The Ch.15 fallback ("Half Corinth sat on those benches", Ch.15 l.314) is available.
- **Fix:** none in Ch.17. Add this to outline Ch.22 as a writer constraint.

---

## INFO (polish / tracking / verified-clean notes)

### [I-01] The Judaea coin type
- **Evidence:** l.492: "a tray of **new silver** … a woman sat in the dust beneath **a palm** with her head in her hand, and **a soldier stood over her**".
- **Note:** as far as I recall the RIC types, the palm-tree-with-standing-figure scene is the big brass *sestertius*. The silver denarius usually shows Judaea mourning beside a trophy. Verify before changing anything.
- **Optional fix (0 words):** "new silver" → "**new brass**". The hawker's "the emperor's new money" stands either way.

### [I-02] The triumph date and the hawker's "for the triumph"
- **Evidence:** l.492.
- **Note:** Titus's Judaean triumph was held in Rome in mid-71. "For the triumph" in spring 72 reads as celebratory and fits CP3-5's one-off festival. No change.

### [I-03] The duoviri names are fictional and plausible
- **Evidence:** "P. VETT. L. CANIN." (l.58).
- **Note:** both are good Roman gentilicia. Dating a colony's year by its two duoviri is correct ("In a colony two names made a year"). Corinth's real duoviri for 66/67 appear on its ADVENTVS AVGVSTI coin issue. I can't confirm the names from here; check RPC I if you want to be safe from pedants. The Outlander standard allows fiction.

### [I-04] Celer rides out on a gray but is back with a litter
- **Evidence:** l.176 "on a gray"; l.312 "His litter waited behind him"; "the dust of the Isthmus road along the bottom of it in a brown band a hand deep".
- **Note:** this is plausible, since a litter can follow and he may have ridden in. One clause would settle it if the evaluator asks. Optional.

### [I-05] Celer's round trip works on the page
- **Note:** Celer left the Isthmus before the boys ran ("so he'll shout himself hoarse", l.336). The sanctuary is about 10 km away, so a litter takes about two hours, which puts him in the forum before noon. "Back … before the men's race" (l.166) then means the early afternoon.
- Plautia's Ch.16 forecast ("when he rides in … after the boys' race", Ch.16 l.514) was a guess, and the page lets it be wrong. Clean.

### [I-06] The man Mara hit: identity and knowledge path, CONFIRMED
- **Identity:**
  - Ch.12 l.50 "Be still, mistress. Be good."
  - Ch.12 l.58 "It caught him above the ear."
  - Ch.12 l.72 he runs "holding his head together in his two hands".
  - Ch.15 l.14 the bandaged Corinthian in Delphi, "the one with something heavy and bright inside her clothes".
  - l.314 "a seam of new skin above his left ear … where nobody had stitched it"; l.326 "Mistress," with two fingers to it.
- **His knowledge:**
  - He heard "Mara." shouted (Ch.12 l.52), which gives Celer "And this will be Mara." (l.348; Mara's own inference at l.350 is correct).
  - He saw the camera swung (Ch.12 l.56), which gives "something heavy under your dress … that shines" (l.354).
  - "Pink" thirteen months on is fine; scars stay pink for a year or more.

### [I-07] Celer's "at Syracuse": a plausible knowledge path
- **Evidence:** l.354.
- **Path:** Delphi's town talk has her as "the Syracusan" who "sailed home" (ENTITY syracuse_cover, Ch.8–15; CH15-7). Celer's man asked about her at the lion spouts (Ch.15 l.14), and the brother's household has the same story (Ch.16 l.32).
- **Note:** no fix. The tracker should add the knower.

### [I-08] Valens's "And the paper in Rome": source unshown but inferable
- **Evidence:** l.368.
- **Note:** the suit is in Rome (Ch.16 l.570), and the brother's people are his source. Celer's reply names the bill of sale, so the reader is never lost. No fix.

### [I-09] Onesimus recognizes a *shut* leaf in a dim lane
- **Evidence:** l.240 "That's out of the emperor's year," after l.216 "He shut it."
- **Note:** this is plausible. He hid that book in the wrong year and handled it that morning, and two boards with raised edges are not common stock. No fix.

### [I-10] Onesimus is the Ch.16 gray-haired clerk, CONFIRMED
- **Evidence:** l.14 "The gray one, then. We had wanted the other."; Ch.16 l.480 and l.552.
- **Note:** CH16-10 can close.
- **Bible-only point:** his card calls him "a freedman of the proconsul", but he has a Corinthian daughter, a grandson, a lane and a wife in the market (l.254–258, l.406). Proconsuls served one-year terms and brought their own freedmen. Consider "a freedman of the office" or "of the governor's establishment" in the card. The manuscript never states his patron, so it needs no change.

### [I-11] The Ch.16 plan against the Ch.17 execution: CONSISTENT

| Ch.16 plan | Ch.17 page |
|---|---|
| One clerk on the door through the festival (l.474) | "There's no one but me in today to mind the door." (l.24) |
| "the young one, who drinks, or the gray-haired one" (l.480); "We must hope for the young one." (l.552) | "The gray one, then. We had wanted the other." (l.14) |
| Dowry instrument as the reason; mother's silver in the purse (l.494, l.498) | Both (l.32, l.40, l.404) |
| "my woman looks along his shelves" (l.502) | Mara reads the tags while he is up the ladder (l.56–94) |
| Cord cut, two boards into the case "among my letters" (l.552) | l.144 "among Plautia's letters" |
| A seal can be got past "a drinker" (l.550) | Better than the plan: she cuts below the boards and never touches the seal (l.124); the clerk is bored, not drunk, and it still works |
| Two doors: colonnade front, lane back with "a baker's oven built against it and a step down" (l.336) | l.182, l.192 |
| Valens "at the back door" once "my brother has spoken to the baker" (l.528, l.532) | l.196 |
| Myrrhine: "the flask … which side … hem" (l.486) | The hem drill and the right side (l.116, l.452); the flask never appears (I-12) |
| Mules to the horse fair (l.522) | Four sent to Lechaion, two "nobody had wanted at any price" (l.282): the sale happened off-page |

### [I-12] Myrrhine's flask (Ch.16 l.486, l.488) never appears
- **Note:** it is harmless. Do not reintroduce it just to tick it off.

### [I-13] The gray mule's fate is unremarked
- **Evidence:** l.282 lists the dun, the black and "the two others". The gray (Mara's tow up the stair in Ch.6; the gall in Ch.9) was last on the page in Ch.11.
- **Note:** a reader fond of her may wonder. Optionally Ch.18 or 19 can give one clause to who has her. No Ch.17 change.

### [I-14] Objects: all consistent
- **Camera:** on its strap under the dress (l.554), as in Ch.12 l.162. Celer never sees it; he has it from his man (I-06).
- **Bracelet:** left wrist (l.146; Ch.16 l.248); "the gold off her arm" (l.354).
- **Pen-knife:** grandfather's, bone handle, fish-skin sheath (l.116). Given away (l.440), which is Plautia's give-away trait, triggered by Mara's "It is a good knife." In Mara's belt (l.454).
- **Leaf:** in Valens's tunic under the belt (l.276; l.554).
- **Pine crown:** bought for Felix (l.526–532) to answer his "Who'll tell me who won?" (l.282). Ch.18 should hand it over.
- **Flashlight:** not on the page. It is in her bag across the dun's withers (l.282), nearly spent (Ch.16 l.434 "Not much."). Clean.
- **Watch:** with Valens; not on the page. Ch.18 returns it.

### [I-15] Legal logic in Ch.17: COHERENT
- Valens: "You hired me," to which Celer says "Did I? … We'll let the lawyers argue that." (l.362–364)
- Celer's own summary (bill of sale against the magistrate's line, l.370) matches foundation §3 and outline Ch.17 beat 1: the registration is not in dispute.
- Taking the book matters for possession and suppression, not for the claim. See W-10 for Ch.22.

### [I-16] Celer against his card and foundation §3: PASS
- Never says "wife" (0). He uses "the lady Plautia", "the lady", and "somebody to write his letters for him".
- He never raises his voice and makes no direct threat; every knife is a pleasantry.
- He uses the warm "we" ("We were never that, were we, you and I?"; "We'll all dine") and contractions.
- No villain monologue; his longest speech is the offer at l.364. No violence.
- The scaffold aversion is shown three ways: named by Plautia (l.172), the hand stopped at the shade line (l.358), and carried round (l.396).
- He is distinct from Plautia. She speaks in the second person, in earnest, with subordinate clauses and blunt questions ("Will you let me speak to him?"); he speaks in the first-person plural, socially.

### [I-17] Valens's speech: in voice
- Short, level and literal, and he rarely subordinates: "Round."; "Alone."; "That was where he was standing."; "I saw where his feet stopped."
- Bare "No." 1 (l.558, to "Will they wait?").
- He reads bodies before faces ("watched the clerk's hands", l.244), and his mind-reading is inverted as the outline asks ("He'll eat his bread.", l.270).

### [I-18] Mara's comprehension: consistent
- Celer is "pleasant and unhurried" (l.318), and Plautia asks for the dowry to be read "slowly" (l.108).
- The baker, the pine boys and the latrine fat man use short spoken Greek.
- Her one Latin line ("I write for the lady.") draws the Syracuse remark, which agrees with Ch.16 l.38.
- Only W-05 overreaches.

### [I-19] The brother's Latin against Ch.16
- **Evidence:** l.444 "his Latin is worse than yours"; Ch.16 l.42 "Speak Greek in front of him."
- **Note:** these are compatible. A man can hear a wrong accent and still read Latin badly. Watch it if the brother speaks in Ch.21 or 22.

### [I-20] An intra-chapter echo: "cloth in the market"
- **Evidence:** l.14 (narration, the fig-cake women) and l.406 (Onesimus: "on a cloth in the market by the Kalends").
- **Optional fix (−2; only if words allow):** l.406 → "on a cloth by the Kalends". Otherwise leave it; the two uses are 390 lines apart.

### [I-21] A command near-repeat
- **Evidence:** l.456 "Walk." and l.478 "Keep walking. Don't look at him." (22 lines apart, same speaker).
- **Note:** this is natural speech, but it sits close to the command-echo zone. If W-09's alternative is taken, l.456 can end on the Lechaion line and drop "Walk." (−1), or turn it into "Come on." (+1).

### [I-22] Foreshadowing and retired reflexes: CLEAN by reading
- No foreknowledge, no significance tags, no narrating present.
- Celer's "Then we'll see each other in Rome" (l.380) and Valens's "a day out to sea" (l.466) are characters' forecasts, not the narrator's.
- No define-by-negation opener, no anaphora triad, no closing aphorism.
- The S1 button "under the ladder" (l.188) is situational irony, not a device line.
- Watch these:
  - the four "white"s in S3–S4 (l.310, l.396, l.420, l.472);
  - the Ch.16 → Ch.17 mirror "wet and perfectly composed" / "perfectly dry and very white" (l.420), which is fine once;
  - the baker's song, touched 5 times in S2.

---

## WORD LEDGER (floor 6,900; current 6,923)

| Fix | Δ words |
|---|---|
| C-01 l.34 "in the shade of the porch" | +3 |
| C-01 l.450 "by the fuller's" | +1 |
| W-01 "the year Nero was here" | +1 |
| W-02 "the autumn before last" | +2 |
| W-03 "Come out tomorrow … Look down on us from the women's benches" | +2 |
| W-04 "nineteen" | 0 |
| W-05 "in a Greek that was not Corinth's" | +2 |
| W-06 sausage-man / tray | 0 |
| W-07 the gander | +1 |
| W-08 / W-10 (outline patches only) | 0 |
| W-09 optional softening | +1 (optional) |
| **Net (CRIT + WARN, excluding the optional W-09)** | **+12 → ≈ 6,935** |

The dialogue share rises slightly (C-01 l.450, W-03 and W-05 all add words inside speech or beside it), so it stays above 30%. The first line, the closing paragraph, the 3 breaks, the bare "No." and the scaffold slow beat are all untouched.

---

## CH.18 HANDOFF CONSTRAINTS (for the outline / writer)
1. They arrive running, early afternoon, in sun and an onshore breeze. Felix and the four mules (the dun, the black, two unwanted) have been on the quay since before sunrise with the brother's freedman. The bags and the potted fig are with them (W-08).
2. The ship has the goose carved on her stern, is bound for Puteoli, and sails on the afternoon breeze. A sail was already going up as the chapter ended.
3. The pine crown goes to Felix, who wanted to know who won. Nobody knows.
4. Myrrhine: decide (W-09).
5. The leaf is in Valens's tunic. Mara has the pen-knife in her belt, the camera under the dress, and the bracelet on her left wrist. The watch is with Valens.
6. Celer's seamed man saw which road they took (l.474–482). Ch.18 need not use him, but he must not be at the quay unannounced.

## CH.22 CONSTRAINT
- See W-10: how the unsealed leaf is authenticated; the cut book in Celer's hands; the six living witnesses (three dead: the school doctor, an oil-seller by the gate, a trainer, l.470).

---

## SUGGESTED YAML PATCHES (for the entity-tracker's next UPDATE; recommendations only)

```yaml
suggested_patches:
  - entity: "onesimus"
    action: "create"
    reason: "the gray-haired record-office clerk named by Celer (l.328, l.380); resolves CH16-10 (record-office-clerk-gray). Family: daughter, her husband, grandson aged 12 in the boys' race; wife who sells in the market. Patron not stated on the page."
  - entity: "plautia.physical.age"
    action: "update"
    value: "married autumn AD 63 'since I was sixteen' (or nineteen, if W-04 is applied); flag against ch-16 'thirty, or a little under' until resolved"
    reason: "W-04"
  - entity: "plautia.relationships.plautias-father"
    action: "add"
    value: { name: "Sextus", source: "ch-17 l.112", note: "two seals by one engraver, his own and his freedman's (the freedman's chipped)" }
  - entity: "plautia.knowledge / timeline_events"
    action: "add"
    value: "married autumn AD 63, 'before the great fire'; dowry entered in the colony's book, third book of that year; dowry items incl. Doris, a Syrian slave girl aged eleven"
    reason: "consistent with Marcus b. autumn 64; Doris may be the hairdresser witness of 69 (ch-12) — keep any Ch.22 naming consistent"
  - entity: "quintus-arrius-celer.physical"
    action: "add"
    value: "ears that 'jutted from his head like the handles of a cup' (Marcus's, ch-16); very carefully shaved; older than his laugh; new white toga"
  - entity: "quintus-arrius-celer.knowledge"
    action: "add"
    value:
      - "Mara's name (from his Kirrha-road man, who heard 'Mara.' shouted, ch-12)"
      - "she carries something heavy that shines (same man, ch-12; asked about in Delphi, ch-15)"
      - "the Syracuse cover (Delphi town talk, via his man)"
      - "Valens will go to Rome on the brother's money ('Her brother's paying my road. To Rome.')"
      - "Plautia read her dowry in the office that morning"
    knowledge_absent: ["the leaf is gone (book unopened on the page)"]
  - entity: "conflicts: CH12-5 (no sender named for the Kirrha-road men)"
    action: "remove_conflict"
    reason: "Ch.17: the man Mara hit is Celer's ('My man tells me…', l.354; 'Celer's seamed man', l.398)"
  - entity: "objects.manumission-record"
    action: "update"
    value: "removed ch-17: boards five and six, closed face to face, raised edges; cord cut below the boards, re-tied with an unsealed reef knot; book returned to the wrong year, then taken by Celer unopened 'lighter by two boards'; the leaf rides in Valens's tunic. Text: C. IVLIVS VALENS, a lanista, the emperor, the arena, liber, nine witnesses (three dead)."
  - entity: "objects.plautias-penknife"
    action: "create"
    value: "Plautia's grandfather's pen-knife, bone handle, fish-skin sheath; cut the cord; given to Mara at the colonnade; in Mara's belt"
  - entity: "objects.pine-crown"
    action: "create"
    value: "bought by Valens on the Lechaion road for Felix ('He'll ask who won.')"
  - entity: "valens.inventory.mules"
    action: "update"
    value: "four to Lechaion with Felix and the brother's freedman: the dun, the black, two unsold; the rest sold off-page; the gray's fate unstated (I-13)"
  - entity: "knowledge_index.syracuse_cover"
    action: "add"
    value: { who: "quintus-arrius-celer", what: "'a Latin they must teach very carefully at Syracuse'", method: "inferred (his man's Delphi enquiry; town talk)" }
  - entity: "timeline (chapter 17)"
    action: "add"
    value: "spring AD 72, the second festival morning: procession at gray dawn; office late morning; Celer in the forum before noon; Lechaion road just after noon; the run as the afternoon breeze rises (subject to C-01)"
  - entity: "character-bible.md (not YAML; for the Writer)"
    action: "sync"
    reason: "Celer/Onesimus/walk-on Ch.17 blocks quote the writer draft, not the final page: 'Didn't you, Plautia?', 'Then go and hear who won it', 'Come and see me after the games, Lupus. Come to the house', 'Come out tomorrow and sit with us', 'you and I' (offer), 'Lupus' x3 (page: 2); Onesimus 'The old years are at the back, lady. Up the ladder.', 'Then the last.', 'He'll have run.' (colonnade), 'If you hear who won the boys'; walk-ons 'ears like knots of dough' and 'a dog asleep on the paving' are cut."
```

---

## TRACKING DATABASES (Ch.17 increment)

**Room audit**
- **S1:** the clerk, Plautia and Mara. The boy enters and leaves (l.158–170). The clerk takes the book out (l.182). Plautia goes by the front; Mara goes by the store and under the ladder.
- **S2:** Mara, Valens and the baker. The clerk comes in at the back door and leaves (l.236–260). Valens leaves first.
- **S3:**
  - the clerk in his doorway;
  - Plautia, with four bearers on the step;
  - Valens at her back;
  - Mara at the litter;
  - Celer in the sun, with his sunshade slave, the boy with the book, "a stranger", and the seamed man.
  - Celer leaves, carried round; the seamed man goes last. Onesimus leaves "by the eastern road".
- **S4:** Plautia leaves in her litter. Mara and Valens; the seamed man at the fountain; the road crowd; the latrine (the fat man and two athletes).

**Information flow (new on the page)**
- **Valens:** reads his own name and the nine witnesses. Three are dead: the doctor, the oil-seller, the trainer.
- **The clerk:** has seen the leaf in Valens's hands and stays silent.
- **Celer:** see the YAML patch. He does not know the leaf is gone.
- **Plautia:** knows Valens will be at Puteoli; knows the knife cut the cord.
- **Mara:** knows the leaf's text, that the clerk hid the book, Celer's face, and the seamed man's link to Celer.

**Threads:**
- **CLOSED:** the archive leaf (Valens's papers).
- **OPEN:**
  - Myrrhine and the knife (W-09);
  - Felix's crown;
  - the cut book in Celer's hands (W-10);
  - Plautia's letter "when the praetor names our day";
  - the dowry suit (Rome);
  - Onesimus's grandson's race (texture; may stay open).
