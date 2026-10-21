# Writer Report: Chapter 17 — "Games on the Isthmus"

- **Word count:** 7,194 (shape_check) / 7,206 (style_check) / 7,527 `wc -w` with header comments. Target 7,400, range 6,900–7,900: in range, 97% of target. No padding. The first full draft came in at 6,256. The deficit was made up with real beats, not stretched prose: the whispered exchange at the shelves, the board knocking the shelf, the clerk's grandson, the baker's grievance, Celer offering Marcus as bait, Plautia's letter in Latin, the three dead witnesses, the Alexandrian trainer, the coin seller, the latrine, and the empty-city backfill piece.
- **Dialogue:** 31% (shape_check) / 30.9% (show_tell). Band 30–40, so it is at the low end of the band. By section: S1 22.5 / S2 34.8 / S3 41.6 / S4 29.5. The office is narration-heavy by design, because Mara is working with her hands while the clerk reads aloud. If dialogue-polish trims lines, S1 is the place to add speech, not S3.
- **Breaks:** 3 (four sections). **Median sentence:** 11 (shape_check and metaphor_check), which is gear LOW. The one slow beat is Celer's hand at the edge of the shade: one held sentence (l.366).
- **Hook as written (opening, short-punch, 8 words):** "The boards left their dust on my fingers." This is IN MEDIAS RES / SENSORY, not QUESTION. We are in the record office mid-theft, with wax-tablet books and dust.
- **Pull as written (closing paragraph, final sentence `quiet`, 13 words):** "At the harbor, beyond the last of the gardens, a sail was going up." This is ACTION UNFINISHED / ticking clock (CLIFFHANGER-type), not QUESTION PLANT. It comes mid-run for Lechaion. Valens has just said the ship "goes out on the afternoon breeze, whoever's on it", the breeze has risen, and "Will they wait?" got "No." The closing paragraph has several sentences, as the ledger requires for Ch.17.

## How Celer's presence is motivated (on the page)
Plautia placed him in the second row at the Isthmus (Ch.16), and Mara sees him ride out in the dawn procession from the brother's roof (l.180). The book shows three reasons for him being back in the colonnade:
1. His runner says he has ridden back during the boys' race. He wants "Vettius's first book brought out to him, for the copyist" and must be "back at the governor's side before the men's race" (l.164–170).
2. Plautia says: "He has chosen the same morning we chose," … "and for the same reason." (l.176). The city and the proconsul are out at the games, so it is the moment to take the book away quietly.
3. The clerk explains the cover story: "He has a copyist who'll keep it under his bed till everybody's forgotten it. He's paid the copyist a year ahead." Celer's earlier hold on the freedmen (Ch.16) is why the book had been hidden in the wrong year's slot and why the clerk said it was "out with a copyist".

He stays outside, in the colonnade, because he won't walk under the scaffold. Plautia names this superstition once (the ladder, the builder's frame, the painter's plank) and the scene shows it once: his toes stop at the poles' shadow, his hand stops at the bar of shade, and his men carry him round through the sun. He leaves with the cut book, unopened, and pats it while he talks about papers. His career problem appears on the page ("he'll think I've died, and give my seat to somebody he likes better"), and so does the glance at the sun.

## Gate status
`bash books/the-hour-of-ash/tools/check_chapter.sh 17` passes every gate:
- style: clean (simile 1.5/1k, em-dash 0, foreshadow 0);
- grammar: 0 errors;
- rhythm: 0 flagged;
- show/tell: no flags;
- voice-wear: strict clean;
- tic gate: clean;
- echo scan: **0** cross-chapter echoes. The first draft had 203, and all were varied by hand;
- spoken-line echoes: **none**;
- command-echo candidates: 1, a false positive ("His father thinks he'll run at Olympia." → narration). The real ones ("Open it" / "He opened it", "Go on from the lion's paws" / "He went on…", "Go and tell him" / "He went") were removed;
- metaphor: no flags;
- shape audit: CLEAN, and `--strict` is CLEAN as well.

Hand counts:
- reflexes: and-chains 4 (cap 9); negation pivots 0; hinge and "So" paragraph openers 0; "before I had…" 0; "without looking" 0; credential asides 0;
- gestures: kneel/crouch 0; bends 0; hand-on-knee 0; deliberation pauses 0 by the gate (one "sat a while" counted by hand); gait exits 0; object handling 3;
- other: "kept … eyes on" 0; "had gone quiet" 0; item-by-item looks 0 (the runner's look was recast to a single sweep);
- speech: Valens bare "No." 1 (the run), no comparisons in his speech, narrated non-answers 0; Plautia "Then…" openers 1, no contractions, never names Celer or the night, no coals, ≤1 pause beat per scene; Myrrhine no prices and no lupins; Felix no "Is it" opener;
- objects: no watch; the bracelet is on Mara's wrist ("the gold on my wrist" / "the band at my wrist"; Celer sees it); the camera is under her dress in the run; no flashlight. "Isthmia" / "Isthmian Games": 0.

## Emotional anchor
Hit. The gray clerk digs figs out of a pressed fig cake with the blunt end of his stylus through the whole theft:
- while taking the bribe;
- up the ladder with the cake;
- reading the dowry aloud between figs;
- chewing at the back door when he sees the leaf in Valens's hands;
- eating bread through Celer's whole conversation;
- digging with his thumb at the end, because the stylus is locked inside the office.

The emotional surprise lands. The escape works because he is bored and wants nothing written down: "Not today, legate." He declines Celer's seal on a receipt. "You were never in." His one real wish is that his grandson loses the boys' race, so there will be peace in his daughter's house.

## Chaos moments
- **Mara:**
  - all-or-nothing about the knot ("It was done well or it was a botch, and it was a botch." l.148);
  - her body rebels: her bladder (l.82), paid off at the latrine (l.536);
  - failed management: her hands shake at the arch, a threshold (l.496);
  - one triggered memory sentence: the museum storerooms and the accession numbers, the single recognition moment (l.60).
- **Valens:** mind-reading, inverted. He lets the clerk see the leaf and trusts him ("He'll eat his bread." l.276), and he is right.
- **Celer:** the scaffold (l.328, l.366, l.404).
- **Secondary characters:**
  - Onesimus wants his grandson to lose (l.260–264);
  - Plautia gives away her grandfather's knife the moment Mara praises it, this time without weeping;
  - Myrrhine drills Mara on the hem and the right-hand side of the litter, and says "I shall know whose house";
  - the baker's grievance about the coin held up "just so";
  - the Alexandrian trainer reads Valens's walk ("Whose school?" / "I lead mules.").

## Ugly sentence
"I finished, and it was slow, and then it was over." (l.536, the latrine, a quiet bodily moment.)

## Impulse deviations
- **Kept: Celer comes for the book himself, and leaves with it already cut.** The outline only had him meeting them. Making him use the same empty morning for the same purpose gives his presence its reason. It also makes the danger legal and slow: the leaf is safe only until he opens the book "tonight". The outline's subversion lands harder this way, because the villain carries off the evidence of the theft and pats it.
- **Kept: Valens breaks the plan** and walks round under the poles to stand at Plautia's back. This answers Plautia's Ch.16 closing question in action ("Her brother's paying my road. To Rome."), in front of her, with nobody remarking on it.
- **Kept: the dowry instrument read aloud** as cover noise while Mara cuts. It contains "*Earrings, two pairs, gold, with drop pearls*", which is never connected on the page to Plautia's torn earlobe from Ch.16.
- **Kept: the pine crown** that Valens buys mid-escape "For Felix… He missed the boys."
- **Kept: the latrine.** It is the payoff of the bladder line. It punctures the grandeur, and it is period-true (the shared marble seat, the sponge-stick, the fat man asking about the javelin).
- **Cut while drafting:** a simile in Celer's look at the bracelet (a dog gone to live next door), because level-1 pressure kills the asides. Also a gait exit for the clerk.

## Outline deviations
- The beat order is in medias res as the ledger asks. The how-we-got-here material comes in five short pieces, each triggered by something in the present scene: the bribe → the dark at the brother's door; the empty city on the litter's route; the knife → Myrrhine's packing; Celer's runner → the roof at dawn; Valens's "Get down to Felix" → Felix at the gate. Plautia's brother and the baker are handled in one paragraph at the oven.
- The "games crowd" is the morning's ship coming up the Lechaion road for the later days of the games, because the crowd itself is at the Isthmus, 10 km east. It includes athletes, pine crowns, sausage sellers and a Judaea Capta coin seller, which ties the festival to Titus's triumph on the page.
- No violence, and no villain monologue. Celer's longest speech is the offer, in short genial sentences.
- **Hand-off to Ch.18:** the ship sails "on the afternoon breeze", so **Ch.18's hour on the quay is the same afternoon**. The outline's example opener ("awake since the second watch") no longer fits, but any in-the-moment I-statement on the quay will. Felix is on the quay with the dun, the black, two others, both bags and the fig. Valens carries the leaf inside his tunic and a pine crown for Felix. Nobody knows who won the boys' race. The captain's condition (a married couple) is untouched and left for Ch.18. Ch.18 must not re-narrate the run.

## Structural approach used
In medias res: the theft first, how-we-got-here in pieces. Ch.16 was Parallel, so the structure is not repeated.

## Canon decisions made on the page (for entity-tracker and continuity)
1. **The fig-eating clerk is the gray-haired clerk of Ch.16**, now named **Onesimus**, a freedman of the proconsul. This resolves CH16-10. The young drinker does not appear.
2. **Valens's post was by the baker's oven at the back door**, disguised as a baker. The horse fair was not used. (This was open in the Ch.16 eval.)
3. The magistrate's book is **the first book of the year of the duoviri Vettius and Caninius** (tag "*P. VETT. L. CANIN.*", the year Nero came). It had been hidden in an earlier year's slot. The leaf is the **fifth and sixth boards**, written in wax on their inner faces only: "*C. IVLIVS. VALENS.*", the lanista's name, the emperor's, the arena, *liber*, and nine witnesses. **Three of the witnesses are dead**: the school's doctor, an oil-seller by the gate, and a trainer. The cord was cut below the boards, away from the two seals (a ship, and a helmeted head), and retied in a visible reef knot. **Celer has the cut book unopened**, and **no receipt was written**.
4. **The bribe:** Plautia's mother's silver, a ladle and two swan-headed spoons. The clerk's wife will sell them "by the Kalends". The dowry year is the autumn of AD 63 ("before the great fire"). **Plautia's father is Sextus.**
5. **Mara keeps Plautia's grandfather's pen-knife** (bone handle, fish-skin sheath) in her belt. This is a new possession for ENTITY.
6. **Celer now knows** Mara's name (from his men), that she carries "something heavy under your dress, too, that shines", and that Valens will go to Rome on the brother's money. The man Mara hit on the Kirrha road (seam above his left ear, unstitched) is with him and watches which road they take from the fountain by the Lechaion arch. The link to Ch.15's bandaged Corinthian is left for the reader.
7. **The ship** is "the one with the goose carved on her stern", sailing on the afternoon breeze. Felix took the mules down before sunrise with the household's freedman.
8. **AUTHOR-CP3-5 honored.** The festival is "the games", "the boys' race", "the Isthmus" and "the triumph". Never "Isthmia". CP3-3 (no pregnancy remark) and END-1 (no Ch.15 door lines quoted) are untouched.

## Bible
- New card: **ONESIMUS**.
- **CELER**: first live block, covering his entry, the page reason for his presence, the scaffold, every pleasantry, his men, and a spent list.
- Ch.17 blocks for **MARA, VALENS, FELIX, PLAUTIA, MYRRHINE**.
- A **Ch.17 walk-on** block and an **At-risk after Ch.17** block.
- The outline's "Archive clerk (17)" row is marked WRITTEN.
- A change-log line.
- Every Ch.17 quote in the new blocks was checked against the page by script.
- Tic-bearer roster: still NONE.

## Weakest dimension (self-assessment)
**Prose/Originality risk in S1.** The theft is necessarily procedural (holes, cord, boards). I kept it to plain verbs, interrupted by the dowry reading and the board knocking the shelf, so it does not read as a competence cascade. An evaluator may still find the threading paragraph (l.138–146) slow. The slip, Plautia's cover and the botched knot are the counterweights. **Dialogue sits at the band floor (31%).**
