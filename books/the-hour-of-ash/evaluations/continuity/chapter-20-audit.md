# Continuity Audit: Chapter 20 (run 2, per-chapter drift audit)

**Date:** 2026-10-21
**Mode:** MANUSCRIPT AUDIT. Ch.20 "The Mender's Shop" (post-disruptor, 8,142 words by shape_check) is checked against:
- Ch.1–19 as they stand on disk;
- ENTITY_STATE.yaml as of Ch.19 (read only). The tracker's parallel Ch.20 UPDATE had already written rows CH20-1..CH20-6 when this audit read the file; they are cross-referenced below, and nothing in the file was touched;
- outline.md (Ch.20 and its ledger row; Ch.21 for the handoff; Ch.30, Ch.31 and Ch.36 for forward collisions);
- foundation.md (§3 Mara's teeth / all-or-nothing / breaks, Valens's figs; §4f re-read objects; the mending motif; §10 timeline: Lucius born summer AD 74; the collage-document rule);
- voice-dna.md (§0 no-foreshadowing families A–E, §1 anti-patterns and dialogue conventions, voice under pressure);
- character-bible.md (Grata, Valens, Felix and Zosimus cards; the Ch.20 walk-on block; the at-risk lists through "At-risk after Ch.20", including the command-echo registry and the CLOSED item-by-item look);
- voice-bank samples 11 (this chapter's register sample) and 03, plus the rest;
- STATE.yaml guardrails and resolved_author_decisions (AUTHOR-CP3-3 the pregnancy gap stays unremarked; AUTHOR-END-1; CP3-4; CP3-5).

**Chapter reviewed:** `manuscript/chapters/chapter-20.md`
- **Length:** **8,142** prose words (shape_check). The floor is 7,700, so there are **442 words of headroom**. `wc -w` is 8,834 with the comments. **Dialogue is 34.4%** (show_tell; band 30–40, floor 30). 6 breaks / 7 sections. Median sentence 16 / 15 (gear mid).
- **Ledger:** the opener is the italic lost-property notice. Its first sentence is 23 words, so it computes as `narrative`. The close is Grata's spoken line, so it computes as `dialogue`. The approach is Collage. All of this matches the ledger row.
- **Citations:** `l.NN` is the file line in chapter-20.md. Lines in other chapters are cited as `ChN l.NN`.

**Mechanical baseline** (`bash tools/check_chapter.sh 20`, run read only): **ALL CLEAN.**
- Style: simile 1.5/1k; em-dash 0; foreshadowing 0. Grammar: 0 errors. Rhythm: 0 flagged.
- Show/tell: filter 2.1, abstraction 1.5.
- Voice-wear (strict): clean. Tic gate: clean, gesture classes included. And-chains 2 (cap 9); credential asides 1; negation pivots 0; "So" openers 0; present-tense generalisations under cap.
- Metaphor: fig 2.0/1k; >40-word sentences 4%.
- Shape audit: SHAPE CLEAN.
- `python3 books/the-hour-of-ash/tools/tic_report.py --echoes 20`: **0 echoes, 0 command-echo candidates, 0 spoken-line echoes.**

**My own sweeps:**
- A narration-only present-tense scan: 0 hits.
- Reserved-vocabulary scan for the door, the tomb and the cold (seam / niche / painted plaster / hand flat / cool / door / mountain / ash / preserve / bury / excavate / survive): 0 hits on the door or tomb. "seam" appears 0 times.
- A foreshadow read of families A–E.
- A command-echo read by hand (the detector does not see relayed orders).
- A gaze-sequence read against the CLOSED registry.
- Book-wide counts of the at-risk families ("In the finder", "[colour] to the [limb]", the "hold" family, race frames, "looked at X, and at Y").
- Chapter-by-chapter tracing of the notebook, film, fig and lentisk.
- A geography check of the red house and the bull fountain against Ch.19.
- Season arithmetic for the pregnancy.
- An information-flow table (below).
- Period checks on every wall text and every repair.

**Total findings: 35. CRITICAL: 3 | WARN: 15 | INFO: 17**

---

## Summary

The chapter does what the outline asks:
- **The NON-NEGOTIABLES are met.** The bowl leaves her hands for its join. The fountain and the pebble land and are never explained. The lamp's join is left because the customer asks. Grata clocks the pregnancy and the chapter ends on her line.
- **The plants are clean.** The tremor note has no reckoning, and the named frame of Valens under the fig is in place.
- **The handoff to Ch.21 is on the page.** The letter "For Plautia … Where we are" goes by carter to the Puteoli board.
- **Grata:** 0 questions and no teeth.
- **AUTHOR-CP3-3:** no line remarks on a delay before the pregnancy.
- **No preservation or ash irony.** The disruptor already recast the one wink.
- **The wall texts are real Pompeian graffiti, adapted well:** CIL IV 64 (the urn), 429 (Polybius's good bread), 222/7621 (Infantio; *lanternari, tene scalam*), 8258–9 (Successus and Iris), 1904 (*admiror, paries*), 9131 (*fullones ululamque cano*), and 1679 (Edone's price board, re-signed "Grata").

**The three CRITICALs are all "NO TICS" registry or plan collisions, not plot breaks:**
- **C-01:** a fourth command echo. The device has been SPENT at 3 since Ch.9.
- **C-02:** the CLOSED item-by-item gaze, in two forms.
- **C-03:** the night election-painting scene pre-spends the emotional anchor of Ch.31, which is NON-NEGOTIABLE: a household member holding the ladder while a wall is whitewashed by lamplight.

Each CRITICAL has a subtractive fix of a few words. **All CRITICAL and WARN fixes together come to about −71 words.** That leaves Ch.20 at about 8,070 words (floor 7,700) with dialogue at about 34% (floor 30%).

The WARNs fall into four groups:
- **Craft and period logic:**
  - a resin-mended cookpot used on the fire;
  - a stoker who lights his furnaces at dusk although his lamp is used at dawn;
  - a FORTIS factory lamp owned "since before the earthquake";
  - the coppersmith's "Two winters back" against the notice's "at the Saturnalia".
- **Continuity with Ch.15 and Ch.19:**
  - the fig's "first figs" and "never ripen";
  - the red house "at the corner";
  - Felix's bed "among the cobbler's leather".
- **Voice drift:**
  - Ch.9's two-tier reward-notice shape;
  - a sample-11 beat lift at the lamp, plus Ch.16's soot-black nozzle;
  - the race frame over cap;
  - a walk-on object-to-the-eye beat that is CLOSED for Ch.20;
  - four "[colour] to the [limb]" trade tags;
  - the "hold" verb family;
  - a 4th "In the finder".
- **One knowledge gap**, Valens's "your gate". It is plausible off the page.

---

## CRITICAL ISSUES (fix before the evaluator runs)

### [C-01] A fourth command echo (SPENT at 3 book-wide since Ch.9)
- **Audit:** NO TICS / retired narrator moves. Character-bible At-risk after Ch.7: "The command echoed as compliance … book-wide 3 on the page … **SPENT: no fourth anywhere in the book.** Show compliance by its result … or not at all."
- **Precedent:** the Ch.9 audit's C-01 cut "Tell them it is for the god." / "he told them" as the fourth. Command echo has stood at 3 ever since. The gate's detector does not catch a relayed order, so this one has to be found by hand.
- **Evidence:**
  - l.244: "Tell her it hasn't," he said.
  - l.246: "He says it has not," I called over.
- **Problem:** this is an order to tell, followed by the telling, in the order's own words. It has exactly the Ch.9 shape.
- **Minimal fix (−2 words):** make Valens's line a statement, not an order.
  - l.244: "It hasn't," he said.
  - Mara's relay at l.246 is then a relay of what he said, not compliance, and Grata's "I'll charge the wind." still lands.
- **Cascade:** none. The command-echo count stays at 3.

### [C-02] The CLOSED item-by-item look, in two-item form, twice
- **Audit:** NO TICS / closed-device registry. The item-by-item look has been CLOSED since the Ch.4/Ch.5 audits.
  - The Ch.12 audit C-01 defines it as "a gaze moving from item to item", and two-item forms count.
  - The Ch.16 audit C-02 cut "He studied my face, and then the band" on the same rule.
- **Evidence:**
  - l.488: "He looked at it, and at me, and held it up." This is the exact "looked at X, and at Y" form. Its earlier uses on the page, which survived their audits, are Ch.12 l.310 ("He looked at her, and at the road climbing away above us") and Ch.19 l.71 ("She looked at us once, and at Valens for longer"). This is the third on the page, and the bible's Ch.1 rule says "a third use anywhere in the book is a defect".
  - l.430: "Valens studied the panel with the dun's halter in his fist, down to the last red letter, and then looked at Felix." The gaze walks from the panel to Felix, with "and then". This is the same form the Ch.16 audit cut.
- **Minimal fix (−10 words in total):**
  - l.488: "He held it up to me." (−6). The next line, "I put out my hand.", follows cleanly.
  - l.430: "…down to the last red letter." (−4). "It's red," he said, and led the dun on. still reads as said to Felix, who asked.
- **Cascade:** none in the plot. See I-11 for the two finalized survivors in Ch.12 and Ch.19.

### [C-03] Ch.31's NON-NEGOTIABLE anchor is pre-spent (the night whitewash with the ladder held)
- **Audit:** plot threads and forward collision with the outline. The anti-repetition laws apply: set pieces rebuilt across chapters have cost Ch.10, 16 and 17 a Prose cap.
- **Plan:**
  - Outline Ch.31, premise: "Mara spends a night holding a ladder while Grata whitewashes his rivals' notices."
  - Ch.31 **Emotional anchor:** "Grata whitewashing a rival's election notice by lamplight with Mara holding the ladder."
  - Ch.31 beat 1: "the professional sign-painters who work at night".
  - Ch.31 beat 2 **NON-NEGOTIABLE:** "The whitewashing raid. Valens refuses to help, then holds the lamp."
  - Outline Ch.20 beat 5 asks only for "An election notice painted over the old earthquake crack". It does not ask for a night crew.
- **Evidence:** the Ch.20 scene at l.380–412 already stages the night election crew. It has the whitewasher laying fresh white over the house by a lamp on a pole, a boy holding the light, and a member of the household holding the ladder:
  - l.384: "On the ladder a man with a pail of lime and a broad brush was laying a panel of fresh white over the house"
  - l.392: Felix: "Your boy's letting the light swing. Give me the ladder. I hold the dun every day of the year…"
  - l.394: "Hold it, then."
  - l.402: "Felix had both fists round the ladder's legs and his weight on his heels."
  - l.406: "…and me holding it for them half the night. For bread."
  - l.412: "…and took the ladder off Felix"
- **Problem:** if the scene stays as written, Ch.31's anchor and both its NON-NEGOTIABLE beats become a rerun: a night wall, white over red by lamplight, someone from the household holding the ladder and someone holding the light. The bible's own At-risk after Ch.20 entry already marks the wall-writing set SPENT and says Ch.31 "find[s] their own kinds". The professional crew alone is fine, and it even sets up Ch.31's beat 1. **The household hand on the ladder is what has to go.**
- **Minimal fix, option A (recommended; Ch.20 only; about −38 words; dialogue stays about 34%):**
  - l.392: cut the paragraph ("Your boy's letting the light swing. Give me the ladder. I hold the dun …").
  - l.394: start the paragraph at "The painter dried his fingers on his tunic and climbed, while the whitewasher came off." (drop "Hold it, then."). Keep "You, lantern, hold that light still or I'll paint *you* on the wall." The boy's sagging light at l.402 is compliance by result, so it is not an echo.
  - l.402: "Felix had both fists round the ladder's legs and his weight on his heels." → "Felix sat on the curb by the pots with his head back."
  - l.406: "…and me holding it for them half the night." → "…and me out of mine half the night."
  - l.412: "and took the ladder off Felix," → "and shouldered the ladder,"
- **Option B (architect or orchestrator):** keep Ch.20 as written and restage Ch.31's raid in the outline, giving it a different anchor and different hands on the ladder and the lamp. Ch.31 is NON-NEGOTIABLE, so this needs an orchestrator ruling, logged in STATE.yaml.
- **Cascade:**
  - Bible Felix block: "holds the painters' ladder" becomes "watches the painters".
  - The Ch.20 walk-on block: the painter's "Hold it, then." becomes CUT.
  - ENTITY: if the entity tracker recorded Felix holding the ladder, that row needs correcting.
  - *Infantio wrote it. Lantern-boy, hold the ladder.* stays. It is the painter's joke at his own boy, and it is real (CIL IV 7621).

---

## WARNING ISSUES (should fix; a careful reader or the evaluator will catch them)

### [W-01] Ch.9's document shape rebuilt: the two-tier reward notice in red on a support
- **Audit:** voice drift / documents.
  - foundation (Documents): "No document type repeats in consecutive collage chapters." The collage chapters are 2, 9, 20, 26 and 36, so **Ch.9 and Ch.20 are consecutive**.
  - outline Ch.20 Device presence: "Different in kind from Ch.9's inscriptions."
- **Evidence:**
  - Ch.9 l.352–354: an italic notice ending in two reward tiers ("To whoever brings him back … five hundred drachmas. To whoever shows where he is kept … three hundred."), then "It was painted in red on a board whitened with gypsum, pegged to a pillar…".
  - Ch.20 l.10–12: an italic notice ending in two reward tiers ("Sixty-five sesterces if anybody brings it back, and twenty more for the thief, if he comes with it."), then "Somebody had lettered it in red on the pier of a cookshop…".
- **Problem:** the beat is mandated and the text is real (CIL IV 64), but the delivery repeats Ch.9's: a reward in two tiers, then a sentence giving the red paint and its support.
- **Minimal fix (the opener stays byte-identical for hook-craft):**
  - l.12: "Somebody had lettered it in red on the pier of a cookshop above the bull's-head fountain." → "It was up on the pier of a cookshop above the bull's-head fountain." (−4). This also drops a "Somebody" opener.
  - *Optional, author's call:* make the notice single-tier by ending it at "…if anybody brings it back." The cook's l.74 "a fellow wanting the twenty" then becomes "a fellow wanting the sixty-five".
- **Cascade:** the bible's Ch.20 walk-on block ("'Somebody had [verb]' 1 (the notice)") goes to 0.

### [W-02] Voice-bank lifts at the lamp (sample-11), Ch.16's lamp image, and sample-03
- **Audit:** voice drift / voice-bank rule. README: "No sentence, image or line in these samples may be copied". Precedent: the Ch.17 and Ch.18 evaluators capped Prose on sample lifts. The echo scan reads only 5+-word strings, so these are missed.
- **Evidence:**
  - **sample-11, its beat skeleton.** The sample runs: the customer could buy a new one for less → an invisible mend offered → the customer refuses and gives a reason → the join is left → the customer finds the line by touch → the customer leaves holding the lamp. Ch.20 follows that order at l.534–570. Two of its lines are the sample's lines reworded:
    - l.534 "A new one would cost you less than I will ask," against the sample's "she could have bought a new one for less than I charged her";
    - l.530 "Dropped it on the furnace stair," against the sample's "she had dropped it on the threshold".
  - **The sample's bathhouse lamp becomes the bath stoker's lamp.** The outline mandates the request and the touch; the price line and "Dropped it on the …" are optional.
  - **Ch.16 l.268:** Kallia's lamp in the named frame had "a nozzle black to the lip … one night's burning laid over years of others". **Ch.20 l.546:** "The lamp's nozzle was black inside with years of his flame". This is the same image in the book's next lamp anchor.
  - **sample-03:** "a frayed stick of mastic". **Ch.20 l.294:** "a frayed stick of lentisk". This is a synonym-swapped lift, bounded by stop-words (the CP3-4 class).
- **Minimal fix (about −9 words):**
  - l.534: "The potters' row sells this lamp by the basket," I said. Zosimus's "I could buy forty." still answers it.
  - l.530: "It went off the furnace stair," he said.
  - l.546: "The lamp's nozzle was black inside with years of his flame; round the filling hole the clay was dark and glossy from his thumb, pressed there each dawn of those years to tip the oil in." → "Round the filling hole the clay was dark and glossy from his thumb, pressed there each dawn for years to tip the oil in."
  - l.294: "with a chewed twig of lentisk".
- **Cascade:** in the bible's Zosimus card, "Dropped it on the furnace stair" moves to CUT. The anchor (findable by thumb) is untouched.

### [W-03] The fig: "first figs" and "never ripen" against Ch.15 (ENTITY CH20-3)
- **Audit:** objects / character consistency. Figs are Valens's expert obsession (foundation §3), so a self-contradiction stands out.
- **Evidence:**
  - Ch.11 l.194: it fruits "When the summer's done, if it's any good."
  - Ch.15 l.82 and l.104, summer AD 71: "under the leaves a dozen figs, small as olives, green" and "End of the summer." That is his ripening forecast.
  - Ch.20 l.208, summer AD 72: "a small heap of the tree's first figs".
  - Ch.20 l.232: "These would never ripen." … "A young tree carries them all summer and drops them in the autumn, and has none left at the end."
- **Problem:** "the tree's first figs" reads as first-ever, a year after Ch.15's dozen. And Valens now says a young tree's figs never ripen, after promising ripe figs at the end of summer.
- **Minimal fix (about −4 words):** make the AD 71 crop the failure he learned from.
  - l.208: "a small heap of the summer's figs".
  - l.232: "Last year she carried them all summer and dropped every one in the autumn. Without them she makes wood."
- **Horticulture:** pinching fruit off a young potted fig so that it makes wood is sound practice. A potted fig ripening a late crop in its third season is plausible (see I-02 for the month).
- **Cascade:**
  - ENTITY CH20-3 resolves.
  - The bible's "Spent" fig shapes change: "These would never ripen." stays; the young-tree line is replaced.

### [W-04] The handle's date: "at the Saturnalia" (notice) against "Two winters back" (coppersmith)
- **Audit:** timeline.
- **Evidence:**
  - l.10: "with the handle I had riveted on new at the Saturnalia". The notice is spring AD 72, so this reads as last December.
  - l.86: "Riveted that handle on myself," he said. "Two winters back. Good rivets."
- **Problem:** "two winters back" is AD 70–71.
- **Minimal fix (0 words):** l.86 "This winter gone. Good rivets."
- **Cascade:** none.

### [W-05] FORTIS lamp owned "since before the earthquake"
- **Audit:** history / world rules.
- **The lamp itself is fine.** FORTIS factory lamps (Firmalampen, the Loeschcke IX/X family, made at Mutina) are the most widespread lamp name in the empire. They are generally dated from about AD 70, and a few are reported from the Vesuvian sites. One FORTIS lamp in a Pompeian stokehold in AD 73 is therefore defensible, and so is the joke of a shelf of identical names.
- **Problem:** ownership from before AD 62 predates the type.
- **Evidence:** l.536: "I've had it since before the earthquake."
- **Minimal fix (+3 words):** "I've had it since my first winter on that stair."
- **Cascade:**
  - The bible's Zosimus card quotes the old line, so move it to CUT.
  - This also removes a third "earthquake" mention from the chapter.

### [W-06] The stoker lights his furnaces at dusk, but his lamp is the dawn lamp
- **Audit:** world rules (bath practice) / internal logic.
- **Evidence:**
  - l.546: "pressed there each dawn of those years to tip the oil in"
  - l.562: "Zosimus came for it two evenings later, on his way down to light the furnaces."
- **Problem:** public baths were fired from early morning for the afternoon bathing hours. Zosimus's own lamp is lit at dawn.
- **Minimal fix (+3 words):** l.562 "…on his way down to bank the furnaces for the night."
- **Cascade:** none.

### [W-07] A resin join on a pot that goes on the fire
- **Audit:** craft logic (Mara's conservator attention, foundation §3).
- **Evidence:**
  - l.68: "Make it hold. I cook in it."
  - l.70: "Then I ran resin into the new crack from inside … pared it flush"
  - l.566: Mara tells Zosimus, "The join will soften in a great heat."
- **Problem:** lentisk and pitch soften on coals. Mara knows this three sections later, and the lead dogs the customer asked for are the repair that would survive.
- **Minimal fix (0 words; it also thins W-12):** l.68 "Make it tight. My oil lives in it." The pot is retired from the fire to storage, and its "black with old fires" description still stands.
- **Alternative:** keep "I cook in it" and give the new crack a lead dog beside her mother's. That would make the first visible repair in the chapter and step on the lamp anchor, so it is not recommended.
- **Cascade:** the bible's Ch.20 walk-on block quotes "Make it hold. I cook in it." Update it.

### [W-08] The red house "at the corner" against Ch.19's geography
- **Audit:** geography.
- **Evidence:**
  - Ch.19 l.209–223: the cousin's stripe is on the street in from the shore-road gate, "At the next corner" after the temple crossing. Only then do they go "Further down, on a long straight street running east", where Grata's counter is.
  - Ch.19 l.285: Grata: "I heard about you at that wall yesterday … half that street saw you". The wall is on another street.
  - Ch.20 l.380: "It appeared on the red house at the corner"
  - Ch.20 l.382: Felix: "They're painting the corner"
  - Ch.20 l.436: Grata: "from this corner to the basilica"
- **Problem:** Ch.20 reads as if the stripe were at their own corner.
- **Minimal fix (+3 words):**
  - l.380: "It appeared on the red house past the temple crossing in a single night…"
  - l.382: "They're painting the red house,"
  - Grata's "this corner" is her sweep from her own counter, so keep it.
- **Note:** outline beat 5's "Grata's wall" became the cousin's wall. The Ch.19 audit's I-17 anticipated this, and ENTITY CH20-1 records it as info.

### [W-09] The race frame "[act] before [X]": 2 in narration (the Ch.20 cap is 0–1)
- **Audit:** retired narrator moves. The Ch.19 eval and the bible's Ch.19 WATCH say: "the race frame 'before [X] had': 0–1 in Ch.20".
- **Evidence:**
  - l.84: "He knew the pot before it was on his bench."
  - l.150: "My lower lip found that before my eye did."
- **Minimal fix (−4 words):** l.84 "He knew the pot on sight." Keep l.150; the bible's lip-test entry relies on it.

### [W-10] A walk-on object-to-the-eye beat (CLOSED for Ch.20), and "pleased" three times
- **Audit:** at-risk registry. Ch.19 eval and bible: "a walk-on's object-to-the-eye beat: Ch.19's bearer is the clerk, and Ch.20 has none".
- **Evidence:**
  - l.288: "When he came for it he put one eye to the slot and peered in at the nothing inside, and seemed pleased with it."
  - The walk-on "pleased" reaction: l.94 the coppersmith "agreed, pleased"; l.288 the turner; l.452 Felix, "much pleased with them".
- **Minimal fix (−10 words):** l.288 "When he came for it he ran a fingertip round the slot and was satisfied."
- **Cascade:** none.

### [W-11] "[colour] to the [limb]" as the tradesman's introduction, 4 times in the chapter
- **Audit:** NO TICS (an emerging narrator device). The gate does not see it.
- **Evidence:**
  - l.32: Felix "lime-white to the eyebrows"
  - l.386: the painter "with red to the wrists"
  - l.496: the dyer, "a man with his arms blue to the elbow"
  - l.528: Zosimus "black to the elbows"
  - Book-wide the form also appears at Ch.5 l.49 ("black to the wrist") and Ch.16 l.268 ("black to the lip"). In the same chapter, two neighbouring arm markers do the same job: the coppersmith's "burns all up his forearms" and the turner's "shavings of bone in the hair of his arms".
- **Minimal fix (keep Zosimus's, which is the anchor, and the painter's):**
  - l.32: "Felix came in from the string at dusk with lime in his eyebrows," (l.38's "He dug lime out of one eyebrow" then pays it off).
  - l.496: "a man whose hands were stained blue from somebody's vats".
- **Cascade:** the bible's Ch.20 walk-on block quotes the dyer. Sync it.

### [W-12] "hold" as the chapter's repair verb
- **Audit:** NO TICS / intra-chapter phrase family.
- **Evidence:**
  - l.68 "Make it hold."
  - l.140 "Will it hold soup?" and l.142 "It will hold anything you put in it."
  - l.284 "I can make it hold coins,"
  - l.520 "…mended my jug, and it holds."
  - l.356 Felix's "I meant to hold"
  - It follows Ch.19 l.19, Pacuvia's "It won't hold".
- **Minimal fix (0 words):** W-07 already changes l.68 to "Make it tight." Also change l.284 to "I can make it keep coins,". Keep the bowl exchange (bible-spent) and the graffito.

### [W-13] "In the finder": the 4th use in prose (Ch.12, Ch.16, Ch.19, Ch.20)
- **Audit:** NO TICS. Every camera beat is framed the same way: "In the finder …" plus a layout.
- **Evidence:**
  - l.212: "In the finder I had the jar on the left and his gray soles on the right, and the leaves above his face"
  - Ch.12 l.160: "In the finder the plane trees stood upright"
  - Ch.16 l.268: "In the finder the window was a square of dark"
  - Ch.19 l.43: "in the finder the mountain was small enough to cover with a thumb"
- **Minimal fix (+1 word):** l.212 "Through the lens I had the jar on the left…". Record "In the finder" as SPENT for Ch.26, Ch.27 and Ch.38.

### [W-14] Where Felix sleeps (ENTITY CH20-4)
- **Audit:** character location.
- **Evidence:**
  - l.40: "when Felix had already gone in to his blanket among the cobbler's leather". But Ch.19 l.237 says the nephew "took the leather", and l.275 says only scraps were left, which Mara prised up.
  - l.250: "Once Felix was off to the stable,"
  - l.372: "I hear everything in this house"
  - l.382: "he whispered at the door to our room"
- **Problem:** the page has him sleeping in the shop, but l.250 sends him to the stable without saying why.
- **Minimal fix (about 0 words):**
  - l.40: "…gone in to his blanket in the shop."
  - l.250: "Once Felix was off to see to the mules,"

### [W-15] Valens's "your gate": the knowledge path is off the page (ENTITY CH20-6)
- **Audit:** information flow (rule 8: plausible but unshown).
- **Evidence:**
  - Ch.19 l.329–331: "The third?" / "The Nuceria Gate. Tomorrow." She finds the tomb alone, and Ch.19 never shows her telling him.
  - Ch.20 l.262: "Do you still walk out to your gate?" / "On the Kalends." / "And it's the same."
- **Assessment:** a spring passes off the page between the chapters, and the Ch.15 truth-telling means he knows what she is looking for. He knows the gate and the cadence, not the tomb. That fits outline Ch.30 beat 2a ("From here he knows where the door is").
- **Fix:** no text change is required. **Constraint for Ch.21–29:** no line may have Valens name or picture the tomb or the painted door before Ch.30.

---

## INFO (polish, history notes, handoffs, registry)

### [I-01] History check on the wall texts and the repair trades: PASS
- **The lost-property notice** is CIL IV 64, adapted: *urna aenia pereit de taberna … HS LXV … sei furem dabit … HS XX*. The real text offers the 20 for handing over the thief "from whom we can recover the thing". "twenty more for the thief, if he comes with it" is a fair free rendering. The charcoal reply is invented, which is plausible, since charcoal graffiti are common at Pompeii.
- **Polybius as candidate:** "C. Iulium Polybium aed(ilem) o(ro) v(os) f(aciatis). Panem bonum fert." is real (CIL IV 429). C. Julius Polybius ran for aedile in the city's last decade and later for duumvir (traditionally in its last year). No inscription fixes his aedilician year, and the proposed chronologies put it in the late 60s to 70s. **AD 73 is plausible "to a certain point."** Grata's "his grandfather swept out somebody's kitchen in Rome" fits the family's likely descent from an imperial freedman.
- **The election crew:** the whitewasher prepares a panel over old writing, the painter works at night with a lantern-bearer, and Infantio's signature and *lanternari, tene scalam* are real (CIL IV 222, 7621). Campaigning at the end of winter for elections in March is correct.
- **The other graffiti:**
  - Successus and Iris (CIL IV 8258–9); its reply is condensed.
  - The "amazed, wall" line (CIL IV 1904), found at several sites.
  - The fullers' *Aeneid* (CIL IV 9131).
  - Edone's price board (CIL IV 1679), as copper / two / four (Falernian), with 1 as = a copper and 4 asses = 1 sestertius. **The arithmetic is right.**
- **The repairs:**
  - Lead clamps ("dogs") on pottery, poured through drilled holes and beaten flat: correct practice.
  - Riveting a handle onto bronze: correct.
  - Lentisk (mastic) sold for the breath, and mastic toothpicks (Martial 14.22): correct.
  - A terra sigillata bowl with an *in planta pedis* stamp "from the potteries up the coast" (Puteoli or Pisa / Arezzo): correct for the period.
  - The beehive-shaped clay money box broken to get at the money: correct.
  - A bone toothpick with an ear-spoon (*dentiscalpium* / *auriscalpium*): correct.
  - Glass joined cold with thinned resin: plausible.
- **Bath stokers:** olive-stone (pressing-waste) fuel is plausible, and a stokehold staff of boys with a shared lamp shelf is plausible. Fix the timing per W-06.
- **Falernian "from that side of the bay"** (l.316): the ager Falernus lies north of the Volturnus, off the bay. In Grata's mouth ("near enough") it is a seller's stretch. Keep it.

### [I-02] The olive month, and the fig that ripens in it
- **The olive month:** Roman practice put the main olive picking after the vintage, from late autumn into winter (roughly November–December; Cato and Columella treat it as winter work).
- **The fig:** a potted fig ripening "in that same month of the olives" (l.572) is credible only at the very start of that window, in early November. Keep it as written.
- **Constraint for later chapters:** never date the Ch.20 reveal to December.

### [I-03] The pregnancy timeline: PASS; CP3-3 holds
- **The arithmetic:**
  - Reveal in the olive month (≈November AD 73), after about a week of nausea: about 6–8 weeks pregnant.
  - Conception ≈ late September to October 73.
  - About six months pregnant ≈ April 74 (outline Ch.23, spring, the Appian Way).
  - Birth ≈ July 74 (foundation §10, Lucius summer 74). Grata's "It'll come with the heat." agrees.
  - About nine months from conception to birth. ✓
- **CP3-3:** nothing on the page notices or explains the two-year gap. Grata's "the look about the eyes my sister had with each of hers" is observation, not history.
- **The fountain:** the toddler and the pebble come in summer AD 73, before conception. **Constraint for Ch.21–24:** no line may link the fountain to the pregnancy (the bible: "Never explained, by anyone, ever"). Linking them would also breach CP3-3 sideways.

### [I-04] "a carter bound there for lime" (l.258)
- Puteoli's export was *pulvis puteolanus* (pozzolana, the mortar sand). Lime came from kilns nearer home (the Lattari limestone).
- **Optional fix:** "…a carter bound there for the Puteoli sand the builders put in their mortar" (+7). Alternatively, keep "lime" and accept it.

### [I-05] The toddler's "crescent of leather" (l.488)
- The *lunula* was chiefly a girl's amulet. A poor freeborn boy's was the *bulla scortea* (a leather bulla).
- **Optional fix:** "naked but for a little leather bulla on a cord at his throat". Some crescent amulets on infants of either sex are attested, so this is not required.

### [I-06] Fish sauce ladled into a carter's cup (l.584–588)
- "she lifted the lid to ladle some for a carter … and put his cup out for more of it" reads as him drinking garum by the cup.
- **Optional fix:** "…ladle some over a carter's bread" and "…and held his bread out for more of it."

### [I-07] Comprehension in the first weeks (spring 72)
- Ch.19 set Grata as the speaker Mara loses at speed (Ch.19 l.279). Ch.20 S1 renders her paint flood in full (l.26) without a comprehension beat.
- **Assessment:** the bible caps comprehension reports at ≤2 per chapter and does not require one, and a year passes inside the chapter. Accept it. Do not add a "caught every word" claim anywhere.

### [I-08] "Two years and more" of lentisk (l.294; ENTITY CH20-2)
- From the Ch.7 stick (winter AD 70) to the vintage of 72 is about 22–23 months. From the October 70 arrival it is about 24.
- **Optional fix (−2):** "Two years I had cleaned my teeth…"

### [I-09] The bible's Ch.20 blocks quote the writer's draft, not this page (for the bible sync, not for the manuscript)
- "Nobody at home had ever paid me to leave a join where it could be found." is CUT by the disruptor, but the bible lists it as "said once".
- "Then they'll want it shouted." is now "That wants shouting." on the page.
- "She had a tinker do that…" / "Then I'd only break it in the same spot looking." are now "She had a tinker put his dogs in it…" / "I'd only break it in the same spot, looking for it."
- Zosimus "hugs the lamp to his breastbone" is now "cradled the lamp in his palm". His name is given as "Zosimus. Of the crossing baths." (not "for the tag, Zosimus, of the baths").
- The bible says "the toothpick" for teeth, while the page has "Teeth this end. Ears the other." This one is consistent.
- After the fixes above, the C-03 / W-02 / W-05 / W-07 / W-11 strings need updating too.

### [I-10] Handoff to Ch.21
1. **The pregnancy:**
   - **Knows:** Grata (observed). **The carter at the counter** heard "It's a child you've got." (l.584–592), so the street can know.
   - **Does not know:** Valens ("you've not told him either") and Felix.
   - **Ch.21 must place Valens's knowing early** (beat 4, "Mara, pregnant, argues for Rome"). The cleanest version: Mara tells him, in one line or by result, before Felix's barracks news. A path through the carter or the street would make the telling Grata's or the street's, not hers.
2. **The summons path is on the page:** l.250–258 "For Plautia," … "Where we are.", sent "to Puteoli with a carter" in high summer AD 72. This matches outline Ch.21 beat 1 exactly ("in the summer of 72 Valens sent word of their Pompeii lodging to Plautia"). The freedman comes to Grata's counter by name.
   - Plautia asked for Latin "so that my brother cannot read it" (Ch.16). Ch.21 should not have the brother quote the letter.
3. **The Kalends visits are new canon:** Mara walks out monthly, and the door stays "the same".
   - Ch.30 must stage the tremor visit as off-cycle.
   - Ch.36's tomb visit must not contradict the cadence.
4. **Literacy:** Felix still believes Valens cannot read ("It's red"). Valens reads and writes only out of Felix's sight (l.40, l.250). Keep it that way unless a chapter turns it deliberately.
5. **Plautia's pen-knife** is still on loan (Ch.17: "Her woman can come to Puteoli for it."), and it is used at l.146. Nobody has fetched it. It may ride with the Ch.21 freedman; no line is required.
6. **Felix's arena line is primed:** "Will you paint a fighter's name…" and "a name scratched on every wall in this town but mine". The palm-branch is NOT spent (Ch.21's anchor).

### [I-11] The closed-gaze survivors in finalized chapters
- Ch.12 l.310: "He looked at her, and at the road climbing away above us"
- Ch.19 l.71: "She looked at us once, and at Valens for longer"
- Both passed their audits, so the registry has been enforced unevenly. These are not for this chapter.
- **Recommendation:** log both in the bible's CLOSED entry as the counted uses, so that C-02's count is on record.

### [I-12] Spoken "Nobody…" openers: 4 (Grata l.26, Felix l.50 and l.356, the cook l.74)
- Felix's "nobody" has been on WATCH since Ch.11. All 4 are below every gate.
- **Optional:** l.356 "Break that, anybody, and see what you get. It's mine to touch. I carry it up and I carry it down."

### [I-13] Foreshadowing read (families A–E): CLEAN
- The tremor note has no reckoning: "the date and *small shake, lamps, nobody woke*". It was not counted, compared or noticed afterwards.
- The *admiror, paries* graffito with Felix's "It's been standing since before any of us was born" is past-facing and in a character's mouth, so it is not a preservation wink. Do not add any line about walls lasting.
- Valens's "Next year." for the fig and Grata's "It'll come with the heat." are in-scene speech about the near future, not narrator reach.
- 0 mountain, 0 "seventy-nine" (allowed at 1, unused). 0 casts, excavators, ash or preservation.
- Never describing the door, tomb or cold: CLEAN. The door is not described at all; only "your gate" / "It is the same."

### [I-14] Objects: register check
- **Fenn's notebook:**
  - Last physically on the page in Ch.3 (in her jacket, through the slot; ENTITY ch-03:p7/p60). It is unmentioned through Ch.4–19.
  - At l.276 it is "from beneath my spare tunic in the bag". Accept: the move from jacket to bag is off the page over two years.
  - **The back leaf is blank:** CONFIRMED by Ch.2 l.141: "The back half of Fenn's notebook was blank, sixty-odd ruled leaves he had never reached." The consulate carbon sits in the back-cover pocket, not on a leaf.
  - **The writing implement is unstated.** No pen or pencil of Mara's is on the page in any chapter. Ch.30 or Ch.36 can name it (a reed and soot ink would be period-honest). No fix is needed here.
- **Camera / film:**
  - The named frame is shot and wound on (l.212). "Did you spend one on me?" / "One." is consistent with Ch.15's "It keeps what it shows … on a strip" and Ch.16's "Don't spend it on mules" (the flashlight).
  - **Running count:** plan 11 shot / 25 left (8 in 1998 + the Ch.5 Kroton base + the Ch.16 lamp + the Ch.20 fig). On the page, at least 10 shot / at most 26 left. Remaining are the named frames of Ch.26 and Ch.27, and frame 36 in Ch.38. ✓
  - The Pentax is no longer worn ("I went below for the Pentax").
- **The watch and the bracelet:** the watch is not on the page (still right wrist, ENTITY ch-18:p53). Grata's fingertips rest "on the inside of my wrist, beside Plautia's gold", which is the LEFT wrist. ✓
- **The microcassette:** not on the page. ✓ The plan's next touch is Ch.35.
- **Money:** pay comes in bronze, a cheese, wine and dice. Felix has "coppers put by from the contractor". No rent line. ✓
- **The mules:** the dun and the black are named. The foreman wants the black sold ("I'll stand her further off from him"); keep it as texture, unresolved.
- **New objects:**
  - the bone toothpick;
  - the fountain pebble (dried gray);
  - Felix's hare bowl, now the household bowl;
  - the red-slip bowl, gone with the carter;
  - Zosimus's FORTIS lamp, gone with Zosimus;
  - the cook's pot, re-handled.

### [I-15] Characters: PASS
- **Grata:**
  - 0 questions, and no teeth (Ch.31's). The reveal comes before Mara says anything: "It's not my fish. It's a child you've got."
  - She asks nothing at the reveal, and her line ends the chapter.
  - Her touches are varied (upper arm, forearm, two fingertips at the wrist), within the card's "touches people's arms" axis. Ch.21 finds another.
  - She cannot read: a carter reads her board, and her son reads the panel.
- **Valens:**
  - bare "No." 0; comparisons 0; orders to Felix 0 (after C-01 his "Tell her" is gone too);
  - "It's red" keeps his literacy from Felix once;
  - "That's a good stone" asks nothing.
- **Felix:**
  - he cannot read, and has Mara read every wall;
  - at least 8 of his speeches end on a boast or a fact;
  - no palm-branch.
- **Zosimus:** matches his card (he gives reasons of use, never of feeling, and never states the visible-seam theme). Nobody repeats "Leave me the crack."

### [I-16] Ledger and pacing
- **Ledger row:** Collage ✓; a year told in wall-writing and repairs ✓; open `narrative` (the italic notice, 23 words) ✓; close `dialogue` ✓; 6 breaks ✓; gear mid (median 15–16) ✓; dialogue 34.4% (band 30–40) ✓.
- **Neighbours:** Ch.19 Chronological / Ch.21 Chronological, and no two running share an approach ✓.

### [I-17] ENTITY_STATE rows CH20-1..6: the audit's rulings
- **CH20-1 (outline vs page):** ACCEPT. Both NON-NEGOTIABLEs are met.
- **CH20-2:** see I-08.
- **CH20-3:** see W-03.
- **CH20-4:** see W-14.
- **CH20-5 (outbound letters at the board):** compatible. Keep it.
- **CH20-6:** see W-15.

---

## Information-flow table (end of Ch.20, autumn AD 73)

| Fact | Knows | Does not know | Path on the page |
|---|---|---|---|
| Mara is pregnant | Grata; the carter at the counter; Mara (implied) | Valens, Felix | Grata's speech, with the carter present (l.584–592) |
| The letter to Plautia gives their lodging | Valens, Mara | Felix ("Once Felix was off…") | l.250–258; sent by carter to the Puteoli board |
| Valens reads and writes | Mara | Felix ("You can't, can you") | l.40 (reads alone), l.250 (writes alone), l.428–432 |
| Mara walks to "her gate" on the Kalends; it is "the same" | Valens (told) | Felix, Grata | l.262–268 (the gate known off the page: W-15) |
| The tomb / the painted door | Mara | Valens (until Ch.30), everyone else | — |
| The tremor note in Fenn's notebook | Mara | everyone | l.276 |
| Mara cried at the fountain | Grata (by her face / the street), Valens (told by Grata), the fountain line | Felix (not shown) | l.506, l.510 |
| The fuller's wife's bottle was broken | Grata ("the hour it broke"), the street | the fuller (believed) | l.344–350, l.582 |

---

## SUGGESTED YAML PATCHES (recommendations only; the tracker applies them after the editor's fixes)

```yaml
suggested_patches:
  - entity: "objects.film-roll"
    action: "add"
    value:
      frames_shot_ch20: { value: 1, subject: "the named frame: Valens asleep under the potted fig on the roof, high summer AD 72; wound on; he slept through both", source: "ch-20 l.208-212" }
      running_count_after_ch20: { plan: { shot: 11, remaining: 25 }, page: { shot: "at least 10", remaining: "at most 26" } }
    reason: "named frame paid on the page; no count row yet for Ch.20"
  - entity: "registries.command_echo"
    action: "keep_original"
    value: 3
    reason: "C-01 fix removes the l.244 order; if the fix is NOT taken, set 4 and log it as a defect"
  - entity: "registries.item_by_item_look"
    action: "add"
    value: "page uses counted: Ch.12 l.310, Ch.19 l.71 (finalized); Ch.20 l.430 and l.488 removed by C-02"
    reason: "registry enforcement was uneven"
  - entity: "contradictions.CH20-3"
    action: "remove_conflict"
    reason: "resolved if W-03 is applied (the AD 71 crop dropped unripe; 'the summer's figs')"
  - entity: "contradictions.CH20-4"
    action: "remove_conflict"
    reason: "resolved if W-14 is applied (Felix sleeps in the shop; the evening errand is to the mules)"
  - entity: "felix.traits"
    action: "update"
    reason: "if C-03 option A is applied, Felix watches the painters from the curb and does not hold the ladder"
  - entity: "plot_threads.ch31-whitewash-raid"
    action: "add"
    value: "constraint: Ch.20 shows the professional night crew (whitewasher, painter, lantern boy); Ch.31's raid must differ in hands and anchor"
    reason: "C-03"
  - entity: "knowledge_index.pregnancy_lucius"
    action: "add"
    value: { who: "the carter at Grata's counter", method: "overheard", source: "ch-20 l.584-592" }
    reason: "a third party heard the reveal; the Ch.21 telling to Valens must precede street gossip"
  - entity: "objects.fenn-notebook"
    action: "update"
    value: "Ch.20: in her bag beneath the spare tunic; first back leaf used for the tremor note (autumn AD 72). The back half was blank (ch-02 l.141). Writing implement not stated"
    reason: "first physical appearance since Ch.3"
```

---

## Fix ledger (for book-editor; every edit is local)

| ID | Line | Change | Δ words |
|---|---|---|---|
| C-01 | 244 | "Tell her it hasn't," → "It hasn't," | −2 |
| C-02 | 488 | "He looked at it, and at me, and held it up." → "He held it up to me." | −6 |
| C-02 | 430 | cut ", and then looked at Felix" | −4 |
| C-03 | 392–412 | option A: Felix off the ladder (5 edits) | ≈ −38 |
| W-01 | 12 | "Somebody had lettered it in red on the pier…" → "It was up on the pier…" | −4 |
| W-02 | 530 / 534 / 546 / 294 | the stair line; the potters' row; the nozzle clause cut; "chewed twig" | ≈ −9 |
| W-03 | 208 / 232 | "the summer's figs"; "Last year she carried them…" | ≈ −4 |
| W-04 | 86 | "This winter gone." | 0 |
| W-05 | 536 | "since my first winter on that stair" | +3 |
| W-06 | 562 | "to bank the furnaces for the night" | +3 |
| W-07 | 68 | "Make it tight. My oil lives in it." | 0 |
| W-08 | 380 / 382 | "past the temple crossing"; "the red house" | +3 |
| W-09 | 84 | "He knew the pot on sight." | −4 |
| W-10 | 288 | "ran a fingertip round the slot and was satisfied" | −10 |
| W-11 | 32 / 496 | "with lime in his eyebrows"; "whose hands were stained blue" | ≈ 0 |
| W-12 | 284 | "make it keep coins" | 0 |
| W-13 | 212 | "Through the lens" | +1 |
| W-14 | 40 / 250 | "in the shop"; "to see to the mules" | ≈ 0 |
| **Total** | | | **≈ −71 for CRIT + WARN as listed (the INFO optionals are not included)** |

**After the fixes:** about 8,070 words (floor 7,700) and dialogue about 34% (floor 30%). The opener and the closing speech stay byte-identical. Re-run `bash tools/check_chapter.sh 20` and `tic_report.py --echoes 20` after the edits.
