# Revision Report: Chapter 8, Polish Cycle 1

**Editor:** book-editor | **Date:** 2026-10-19 | **Input:** `evaluations/chapter-8-eval.md` (POLISH; Floor 8.0 on Prose & Voice, P1–P11; Casual 9.0)
**Scope:** the full PATH TO 8.5 (P1–P11), the cave beat, the fennel, the optional stair plant, and the entity contradictions CH8-3 / CH8-5 / CH8-7. Disruptor changes were not reverted. Strengths #1–#16 were left alone, apart from the clauses the PATH itself names inside them (see "Strengths verification").
*(¶N = line number in the pre-revision file, as in the evaluation.)*

## Result

| Measure | Before | After |
|---|---|---|
| Prose words (shape_check) | 7,691 | **7,476** (−215; the evaluator expected ≈7,440, plus the +~40-word stair plant) |
| `wc -w` incl. header | 7,834 | 7,635 |
| Dialogue (shape_check / show_tell) | 27% / 26.4% | **28% / 27.6%** (band 25–35) |
| Median sentence | 15 | **15** (gear mid) |
| Breaks | 0 | 0 |
| Sequencer paragraph openers (`So/Then/After that/Afterward/Later…`) | 8 (gate FAIL, cap 3) | **2** (¶132 "After that it was dancing.", ¶250 "Then everybody took off her shoes.") |
| "Everybody" openers | 3 | 2 |
| Simile / 1k | 3.1 | 2.8 |
| And-chains | 3 | 2 |
| First paragraph | | byte-identical (md5 checked) |
| Final paragraph and sentence | | unchanged |
| `check_chapter.sh 8` | 5a FAIL (hinges) | **all clean**: style, grammar 0, rhythm 0, show/tell, voice-wear strict, tic gate, metaphor, shape CLEAN |
| `tic_report.py --echoes 8` | 0 | **0** |

---

## Items, before → after

### P1: the sequencer hinge (Revision #3)
| ¶ | Before | After |
|---|---|---|
| 112 | "Then the drums stopped, and the pipe…" | "The drums stopped, and the pipe…" |
| 124 | "Then she began a cry, high and long…" | "She began a cry, high and long…" |
| 164 | "Then I knelt at the crack's widest…" | (see P2) "I knelt at the crack's widest…" |
| 322 | "After that the sandal went unclaimed. It lay…" | "The sandal went unclaimed after that. It lay…" |
| 430 | "Afterward the fire was a red line in the gateway…" | "The fire was down to embers in the gateway…" (also drops "red line", the sample-12 dying-fire frame named in Cross-Book #3) |
| 480 | "Later Sostrata talked in her sleep…" | "Sostrata talked in her sleep…" (the gate's regex counts "Later"; it now follows "Go to sleep." directly) |
| 292 | "Everybody near her had leapt up too" | "The women near her had leapt up too" |
| kept | ¶132 "After that it was dancing."; ¶250 "Then everybody took off her shoes." | (the two the evaluator kept) |

### P2: the cave in its spent words (Revision #1), and the cave beat
| ¶ | Before | After |
|---|---|---|
| 158 | "…and the drum with them. There was the drip, somewhere far back, dropping into its pool, and the torch." | "…and the drum with them." |
| 160 | "I crossed into the hall at a walk. The great pale stone in the middle slid past to my left, its shoulder wet and shining. Beyond it the floor rose. … I had been here twice. I knew the roof would come down…" | "I crossed into the hall at a walk, and beyond the middle of it the floor rose. … Twice before I had been this far, and I knew the roof would come down…" (the PATH text left three "I…" sentence openers in a row, which tripped the rhythm gate's anaphora check; "Twice before I had come up here" then made "had come up" a 3× book-wide phrase, so it became "been this far") |
| 164 | "Then I knelt at the crack's widest, at the floor, and eased my hand in flat, palm to the dark, up to the wrist." | "I knelt at the crack's widest, at the floor, and sent my hand in to the wrist." (the PATH's "put my hand in" made "put my hand" 3× book-wide [Ch.1, 2, 8] and echoed Ch.2; "pushed / slid / worked my hand" are all used in Ch.3 or Ch.6) |
| 166 | "I waited with my cheek on the slab…" | "I kept my cheek on the slab…" (P8 waiting class; the rest of ¶166 is untouched, so the drip "fell, and fell again" is now the cave's only drip) |
| 170 | "I stayed on my knees; this time I hit nothing, and there was nobody to laugh. Once the torch began to gutter I lit the last of my pines from it and crushed the spent one out on the rock, and in the new light I looked at the crack again: a black gap the height of the slab, a crack like any other. My knees were soaked." | "I stayed on my knees. There was nobody to laugh. When the torch began to gutter I changed it for my last pine, and in the new light I looked at the crack again: a black gap the height of the slab. My knees were soaked." ("Down on the plain Nikaso would be drinking my share." kept) |

### P3: the cloak in borrowed senses (Revision #2)
| ¶ | Before | After |
|---|---|---|
| 448 | "Beneath it was her heat, a great store of it, and the smell of goat hair and woodsmoke and another woman's sleep, with the coarse black hair of the cloak against my face." | "Beneath it was her heat, a great store of it, and the coarse black hair of the cloak against my face." |
| 458 | "She seemed to think that was enough talk. Her breathing went long and slow against my neck, and soon I could feel she was asleep. Under the cloak…" | "Soon she went heavy against my back, and she was asleep. Under the cloak…" (I did not use the PATH's "the knees behind mine went slack" because ¶456 directly above ends "She worked her knees in behind mine", so the phrase would repeat within two lines. The new sentence avoids the sample-10 neck/breath frame and removes the second "seem" gloss) |

### P4: the narrator's callback pointers (Revision #4)
| ¶ | Before | After |
|---|---|---|
| 170 | "this time I hit nothing, and there was nobody to laugh" | "There was nobody to laugh." (see P2) |
| 252 | "For a while, as Kallia had said it would be, the talk was all of feet." | "For a while the talk was all of feet." |
| 386 | "They were all looking at me. I had been looked at by the women of Delphi at the bath and in the salt row, and I had felt it go one way before; in the light of the last fennel I could not tell which way this was going to go." | "They were all looking at me, and in the light of the last fennel I could not tell which way it was going to go." (also removes sample-03's "the women of Delphi") |
| 484 | "I listened to all of it, with my wrist still warm where the stranger had taken hold of it." | cut (see P5) |

### P5: the fourth lying-awake night coda (Revision #5)
| ¶ | Before | After |
|---|---|---|
| 470 | "I lay awake long after the others. The snow hissed on the cloak…" | "The snow hissed on the cloak…" |
| 484 | (whole paragraph, above) | cut. The night now runs from Philista's "He can't hear you from Delphi. We can." straight into the dawn paragraph. |

### P6: second uses (Revision #7)
| ¶ | Before | After |
|---|---|---|
| 62 | "…and the pine caught with a noise like a sheet being shaken out." | "…and the pine caught." |
| 64 | "The drums came back late off the rock, so that every beat arrived twice." | "The rock gave the drums back, so that every beat arrived twice." (cutting only "late", as the PATH says, produced "came back off the rock", a Ch.6 echo that also failed voice-wear) |
| 66 | "Whoever dressed it had left fat on the belly before the tawing, and the hide there…" | "It had been tawed with the fat still on the belly, and the hide there…" |
| 68 | "…carried it up a cliff in the dark without putting a hand to it. … and it rode the switchbacks as level as a tray in a good restaurant." | "…carried it up a cliff without putting a hand to it. … and not one turn unsettled it." (the PATH's "no turn of the path" echoes Ch.3's "turn of the path" and failed voice-wear) |
| 136 | "She stepped into the ring with her arms stuck out stiff from her sides and her chin up…" | "She stepped into the ring stiff-elbowed, with her chin up…" |
| 150 | "My boots kept time with the drum…" | "My feet went with the drum as well as they could…" |
| 152 | "When the oak had burned down to a red heap, the women came to it by twos and threes to put new pine to the coals." | "When the oak had gone to coals, the women came by twos and threes to put new pine to them." |
| 154 | "Past the pen the firs began" | "Beyond the pen the firs began" |
| 232 | "…and nobody would find you till the shepherds' dogs did, in the spring." | "…and the shepherds' dogs would be the ones to find you." |
| 446 | "She took my wrist, not hard, and pulled…" | "She took my wrist and pulled…" |

### P7: the negation pivot and the book-vs-mouth tail (Revision #6)
| ¶ | Before | After |
|---|---|---|
| 282 | "She was not looking at me now. She was chewing something…" | "She was chewing something…" |
| 150 | "…and in my mouth it had the Delphian vowels, not the book's." | "…and my mouth made it Delphian." (the PATH's "it came out Delphian" made "it came out" 3× book-wide [Ch.2, 5, 8]) |

### P8: in-chapter trims (Revision #11)
| ¶ | Before | After |
|---|---|---|
| 324 | "She had fished the red pair…" | "She had snatched the red pair…" |
| 134 | '"Louder," she was shouting. "He's been asleep three months. Louder!"' | '"He's been asleep three months," she was shouting. "Louder!"' |
| 186 | '"Your ivy's down over your eye," … "Down! Torches lit, all of you, and down, before it shuts the stair."' | '"Your ivy's slipped," … "Torches lit, all of you, and down, before it shuts the stair."' |
| 482 | '"He can't hear you from Delphi, girl. We can."' | '"He can't hear you from Delphi. We can."' |
| 166 | "I waited with my cheek on the slab" | "I kept my cheek on the slab" (see P2) |
| 138 | "like a hot stone" | see P10 |
| 368 | '"Mine will be asleep on the flour sacks," Sostrata put in' | '"The baker will be asleep on the flour sacks," Sostrata put in' (breaks the Mine/Mine/Mine triad) |
| 188 | "I held on to Kallia's, which she allowed." | "I held on to Kallia's." (rarity glosses on Kallia back to 1: the hair at ¶136) |

### P9: the flashlight explained again (Revision #8)
| ¶ | Before | After |
|---|---|---|
| 24 | "The flashlight stayed where it was, at the bottom of my bag under the stair. Thirty or forty women with pine torches would know a light that was not fire the moment they saw it, and I had no story for it in Greek or in anything else." | "I left the flashlight at the bottom of my bag under the stair." |

### P10: the taste-and-cough reaction (Revision #9)
| ¶ | Before | After |
|---|---|---|
| 138 | "…and it went down into me like a hot stone. It made my eyes water. I passed the skin back; she drank again, and was shoving it at me once more while I was still coughing." | "…and it landed in my stomach like a coal. I passed the skin back; she drank again, and shoved it at me once more." (I did not use the PATH's "like a swallowed coal" because "went down" also appears in ¶144, "The second mouthful went down easier", and "swallowed" repeats "went down". The hot stone is now held back for Timo's real one) |

### P11: the Theban lentil heckle (Revision #10)
| ¶ | Before | After |
|---|---|---|
| 20 | "Bring us back some of the god's wine, Kallia, and we'll forgive you the lentils." | "Bring us back some of the god's wine, Kallia, and we'll pay you the month early." |
| 22 | '"There's lentils in the pot," Kallia said. "If the house burns down, you'll pay for the house."' | '"The month's due on the day, wine or none," Kallia said. "If the house burns down, you'll pay for the house."' (on her money axis; lentils are now 0 in Ch.8. ¶436's scraped pot is untouched) |

### Logic minimum (Revision #12)
| ¶ | Before | After |
|---|---|---|
| 162 | "…in November, when I was sure there was earth down there to dig." | "…in November, after the last of the earth was out." |
| 124 | "It was the toss any Phocian woman gave a basket of threshed barley in a yard in summer, a lift and a jerk…" | "It was the winnowing toss, a lift and a jerk…" |
| 60 | "…like every other man in the street…" (men in ¶52 stood watching) | "…like every man who had come that far…" |
| 18 | "When Kallia stood up the singing stopped, and a shutter opened." (the Thebans are behind shut shutters) | "The singing stopped, and a shutter opened." |

### Fennel (¶248)
Giant fennel (*narthex*, *Ferula communis*) has a pith that smoulders slowly, which is how Prometheus carried fire, and it is not anise-scented.
- **Before:** "After it the fennel stalks went on singly, ivy and pine cones and all, and the god's wands burned fast and bright with a smell of aniseed, like a licorice store on fire."
- **After:** "After it the fennel stalks went on singly, ivy and pine cones and all, and the god's wands gave us mostly smoke. The pith in them took the fire and nursed it a long while before any flame showed. Prometheus had stolen fire in one of these; I had always pictured it blazing in his fist, and it must have smoked under his cloak."
- The new lines are something Mara suffers (freezing women, a fire that only smokes) and they keep her dry aside. "smoldered" was avoided because ¶286 uses it for Timo's hem. The later burning stalks (¶318, ¶360, ¶386, ¶416) still hold, since the wands flame in the end. Knowledge asides are now 2 by hand (Euripides, Prometheus), within the cap.

### Optional: Nikaso's frozen-cloaks story on the stair (Revision #12, Hostile #1)
- **Added** after ¶84 (Kallia climbs past; the snow crust has just appeared at ¶74), in Nikaso's catastrophizing register: '"Snow caught the women up here once, when my mother was a girl," Nikaso said behind her. "They sent men up in the morning to fetch them, and the men's cloaks froze so hard on the way that they broke in two when anybody tried to unfold them."' (The detail follows Plutarch, *De primo frigido* 953D: the rescuers' cloaks broke when they were unfolded.)
- **¶352 shortened to the callback.** Before: "On the stair Nikaso had told me of women caught by snow on this mountain, and of the cloaks of the men sent up for them, frozen so hard they snapped when anybody tried to unfold them; I had taken it for Nikaso's nerves, and I sat…". After: "I had taken Nikaso's story on the stair for nerves, and I sat…".
- About +40 words in dialogue, −30 in narration. The story looks back, so it is not foreshadowing. "up the stair" was kept out of it because Ch.8 already has two.

### Entity contradictions
| ID | Before | After |
|---|---|---|
| **CH8-3** | ¶108 "On a mule's back the crossing had taken me most of a morning." (the plain alone, against Ch.7's whole ride from the cliff top to the cave) | "A mule had taken most of a morning to bring me from here to the cave." (the women stand at the plain's edge below the cliff head, so "from here to the cave" is Ch.7's span. "On a mule's back the way…" was tried first and made "back the way" 3× book-wide) |
| **CH8-5** | ¶30 "Two gates up from Kallia's, a small quick woman…" (against Ch.5: the sieve door is "halfway along" the lane, and Kallia's gate is at the end) | "Midway along the lane a small quick woman…" ("Midway up the lane" made "up the lane" 3× book-wide with Ch.6) |
| **CH8-7** | ¶152 "took another two pines off the pile", but there is only one change of torch, and ¶170 calls it "the last of my pines" | ¶152 "took a second off the pile"; ¶170 "changed it for my last pine". One spare and one change, so the counts agree |

---

## Strengths verification
- **#1 first paragraph:** byte-identical (md5).
- **#2–#5:** preserved. In #3, ¶18's Corinth song is untouched; only the "When Kallia stood up" clause was cut (logic). In #5, Valens's hand on the mule is untouched; only the comparison clause changed (logic).
- **#6 the climb:** preserved, including "every beat arrived twice" (the verb before it changed for P6/echo), "after that I watched the rock" (mid-sentence, not an opener), the fennel "not the intention" and the basket.
- **#7 the waking and the dance:** preserved. Kallia's dance changed only in the posture fix #7 asked for. The tree lot is byte-identical.
- **#8 the cave:** "like a party through the wall…", "The climb went on and on.", the himation slide, the scratches paragraph (only its logic clause changed, as the PATH orders), ¶166 apart from the one P8 verb, and the hand tucked to warm are all preserved.
- **#9:** "There was nobody to laugh." now stands as its own sentence, as asked. "Nikaso would be drinking my share" is preserved.
- **#10–#14:** preserved, apart from the named P-items inside them.
- **#15:** "It's a cave… It's always open.", the whisper, "Go to sleep." and "We can." are preserved.
- **#16 last paragraph:** unchanged.

## Changes not made (and why)
- **¶172 "I retraced the ridged rock, the hall and the slope to the arch"** (#3 rule of three, minor), **¶246 paragraph button** (#7), **¶244 Kallia's near-proverb** (#16) and **¶410's "Kallia's rule" wink**: all flagged by the evaluator but not in the PATH. The evaluator said to keep ¶410.
- **¶304 "girl"** (unattributed): the evaluator ordered only ¶482 cut. "girl" as address is now 1 in Ch.8.
- **Revision #13 (bookkeeping) and #14 (pipeline):** outside this cycle's brief. **Stale quotes this cycle adds to the sync list:** character-bible.md l.999 (the Theban's lentil line), l.1012 (spent list: "like a licorice store on fire", "as level as a tray in a good restaurant"), l.1168 (Nikaso "two gates up the lane"); ENTITY_STATE.yaml CH8-3 / CH8-5 / CH8-7 (resolve them against this revision), l.927 ("another two pines"), l.932 ("my wrist still warm…", now cut), l.1100 / l.1333 / l.1757 / l.2674 / l.2967 / l.3846 ("two gates up"), l.1733 (Kallia's "There's lentils in the pot" trait), l.5979 (fennel "with a smell of aniseed"). The at-risk list should add: Prometheus/fennel pith SPENT; Nikaso's frozen-cloaks story told once, CLOSED.

## Concerns for re-evaluation
1. **Seven PATH strings were varied** because, once joined to their neighbours on the page, they tripped a gate: ¶64, ¶68, ¶150, ¶160, ¶164, ¶108 and the ¶30 wording. Each is noted above, and each variant was checked against Ch.1–7 and all 13 voice-bank samples.
2. **¶458 and ¶138** depart from the PATH text to avoid in-paragraph repetition ("behind mine", "went down"). Please check that the cloak beat still lands in its own senses.
3. **The Prometheus aside (¶248)** is new narration. It adds a knowledge aside (manual count 2) and is meant as dry humour, not a lecture. Please check it against #15 / #11.
4. **Nikaso's stair story** gives her two speeches in a row (the story, then the Syracuse baths "on the next turn"). That is meant as her subject-jumping. Please check it reads as character, not as a plant.
5. **"Everybody" openers are at 2** (¶110, ¶226), as the evaluator expected. The proposed gate would cap them at 1.
