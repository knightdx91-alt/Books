# Evaluation: Chapter 18 — Six Weeks
**Evaluator:** book-evaluator | **Date:** 2026-10-20
**Text evaluated:** `manuscript/chapter-18.md` (about 2,740 words of prose; target 2,800, range 2,500–3,200, so on spec).
**Read first:** STATE.yaml (decisions: the rune shirts are finished here, the water-snake job is shown here at about 400 words, the war rules are revealed where the source reveals them), book CLAUDE.md, project/STYLE_CONSTRAINTS.md, project/foundation.md (Magic ledger), character-bible.md (Zoran, Thad, Fern, Toma), outline Ch.18 and Ch.19, chapter-17.md (being revised in parallel), Sygl_Complete.txt L767–780 (plus L742, L813, L865, L868 and L997 for cross-reference), evaluations/chapter-17-eval.md.

## HEADLINE
**CVI-Launch:** 8.2 (7.7 + 0.5 strong anchor) | **CVI-Legacy:** 6.4 | **Genesis Floor:** 7.5 | **Genesis Average:** 8.1
**Engagement Type:** Self-Insertion (primary) / Empathy (secondary) / Fascination (tertiary)
**Divergence Alert:** none (0.7 gap).

**VERDICT: POLISH.** This is a faithful, warm and well-shaped compression of the six weeks:
- The flaming dagger is a real small triumph ("he would not have traded it for that sword or for any other blade on the red cloth").
- The snake job runs about 420 words and is vivid. Viridia kills the snake with lightning from her palm, as Ch.21 and Ch.23 require.
- The arrow shirts are finished in two lines and never tested, as the author ruled.
- Fern's war room keeps every source beat. "We will not respond in kind." lands clean.
- The war rules are revealed as a remembered conversation, where the source has them.
- Bal shows no self-dread.

The floor is held at **7.5** by two caps:
- **Characters:** Lora blushes for the third chapter running, and the posture cluster in the closing tableau trips the gesture rule.
- **Prose:** Pattern #11 runs at 3 instances, 1.1/1k, over the commercial cap of 0.8/1k.

The chapter also has two smaller problems:
- **POV/knowledge leak:** Bal knows that Lora had never seen Viridia's power.
- **Pre-spent source beat:** Viridia's crackling hair is the source's Winespring beat (Ch.23).

Every fix below is a cut or a word swap and adds no plot. With F1–F13 applied, the chapter projects to **Floor 8.5 / Casual 8.5: PASS.**

## Gate tools (scratch copy, Ch.1–18 at `/tmp/claude-0/-home-user/925d8686-989e-5134-a9ef-2d597d7cac42/scratchpad/ev18/manuscript/chapters/`)
- `voice_wear_check.py`: **clean.** No retired phrases and no device over cap. Two self-repetitions are WARN only, not strict.
- `tic_report.py --gate`: **clean.** Ch.18 has 0 and-chains (cap 9) and 0 negation pivots. It adds nothing to the book-wide gesture table.
- `style_check.py --dir manuscript`: **clean.** Ch.18 has simile 3.6/1k (cap 4), adverb 10.2/1k, 0 em dashes and no new repeated phrase.
- `grammar_check.py --file chapter-18.md`: 0 errors.

## Gesture hand count (full, 500-word windows; word positions from the chapter start)
| Class | Instances | 3+ in 500w? | Verdict |
|---|---|---|---|
| Smile/grin | Amelia "smiled at him. The smile came slowly" (~w2461, one beat, source) | no (1) | OK |
| Laughs | 0 | — | OK |
| Blush | Lora "went red with pleasure and stayed that way until breakfast" (L22, invented) | no (1) | **Cross-chapter recurrence.** Lora also goes pink in Ch.16 ("so warmly that Lora went pink") and Ch.17 ("gone pink and stayed pink", flagged as F2 in the Ch.17 eval). Three chapters running, so the class recurs chapter after chapter. **CAP** → F3 |
| Looks/watching | "looking up at something" (w1053); "staring into the fire" (w2719); "glancing up at her" (w2738) | no (2 in the closing window) | OK |
| Sitting/lying posture | "Bal sat in his dorm" (w2553); "girls were curled up" (w2655); "Hopper… lay across both their feet" (w2690); "Amelia sat on the hearthrug" (w2701) | **YES. 4 in about 150 words** (L172–176) | **CAP** → F8 |
| Freezing/stopping | "Zoran stopped behind him" (L16); "Bal's fingers had stopped" (L128, the drumming anchor) | no | OK |
| Eyes | "dark circles under his eyes" (Thad, description); "grey eyes that missed very little" (Fern, description); "Fern lifted his grey eyes to Bal" (gesture) | 3 mentions in about 310 words (w1475–1783), only 1 a gesture | Borderline. "missed very little" also duplicates Xavier's Ch.11 descriptor ("did not miss much"), so two characters share it → F7 |
| Chest/heart | Hopper's chest in the water (not a gesture) | — | OK |
| Hand holds/objects | "held the dagger above the stone bench" (L34); "Amelia held it by the guard and turned it" (L42); Fern picks up the papers, thumbs through them, leaves the rest (L134, once) | no (2 in window) | OK |
| Tilts / nods / shrugs | 0 / 0 / 0 (the source's nod and shrug were converted into speech) | — | OK |
| "Lifted" | lifted her right hand (L64); lifted his grey eyes (L112); lifted her chin (L164) | no (spread over about 1,340 words) | Lexical repeat; F5 and F7 remove two of them |
| Narrator reflex "went X and stayed (that way)" | L22, plus Ch.13 ×2, Ch.17 | — | A cross-chapter syntax habit; F3 removes it here |

## Genesis Score (Craft Assessment)

| Dimension | Score | Evidence | Cap Reasons |
|-----------|-------|----------|-------------|
| Originality | 8.5 | The hostility rendered as a joke on Bal's isolation: "His own kind, as far as the castle went, was Bal. There was a dorm full of it." (L10). Fern's map: "It had no mark on it anywhere for a village." (L100). The dagger measured against the vendor and found wanting, then loved anyway (L38–40). The snake "as if the lake were standing up" (L58). | none |
| Theme | 8.5 | The book's question (can Bal protect what he loves without becoming what he fights?) is embodied by the source's own line, "We will not respond in kind." (L110). Fern's "See how they like it?" puts the other side of the question on the table. There is plenty of non-thematic texture: wooden spoons, a brass box with a stiff lid, buttons "that never did anything at all" (L28), "It was a Tuesday, or it might have been a Thursday." (L32), Hopper twitching in a dream (L174). | none |
| Characters | **7.5** | On merit 8.5. Zoran's two-word praise fits his economy (L18). Lora's drill-sergeant care (L22) matches her card. Viridia's dry wit after the kill (L72). Amelia's playful withholding (L168). Fern is blunt and practical, the only voice proposing retaliation (bible distinctness kept). Thad's deepening circles (L88). Chaos (commercial): irrelevant thought ✓ ("He wrote that down twice without meaning to", L172; the spies drinking, L122); distortion ~; triggered memory that returns to the scene ✓ (the vendor, L28; the rules conversation, framed and returned to the present, L150–172); failed management ✓ (Lora's flush of pride, L22). 3/4. | **Gesture caps:** Lora's blush is the third consecutive chapter of it (L22). Posture cluster of 4 in about 150 words (L172–176). Shared "eyes missed little" descriptor (Fern/Xavier). |
| Prose & Voice | **7.5** | Underlines: "just loud enough to carry and just low enough to deny" (L8); "had stopped at not liking" (L86); "It had no mark on it anywhere for a village." (L100, the close-the-book line); "The map had not changed while Fern was gone." (L138). Ugly sentence present ("It was a Tuesday, or it might have been a Thursday.", L32). Under pressure the voice shortens to one-line paragraphs ("The water behind her rose.", L56; "Hopper was out of the water before Bal saw her move.", L60). American register is mostly good ("laborers", "rowboat"). | **Pattern #11: 3 instances (1.1/1k > 0.8 commercial cap):** "as if the win were hers" (L22); "because in all the months since the mausoleum she had not praised a single thing to be kind" (L42); "The smile came slowly, and it took its time crossing her face." (L164). Register slips: "top up the skins" (L54), "hearthrug" (L176). |
| Pacing & Coherence | 8.0 | The structure follows the outline: time-skip, then the lake, the war room, the remembered rules and the present evening. The order is varied and not a graduated reveal. Speed variation is strong: summary weeks, a slow craft scene, a fast snake attack, a deliberate war room, a quiet hearth. Value shift: the school turns hostile and the villages bleed (−), then Bal has a target and an order given (+, purposeful). | The hook is withheld. The outline's Ch.18 hook is "It's going to happen tomorrow."; the chapter stops at "saw her lips part" (L176), a soft tease. POV leak at L76 ("Lora hadn't either"). |
| Emotion | 8.5 | Anchor: the dagger's finger-high flame, "and he would not have traded it" (L36–40). Second anchor: Fern's map under the drumming fingers, with no village on it (L100). Emotional surprise: Amelia *applauds* a kill (L74); Viridia's deadpan "I won't be filling my water skin here" seconds after the lightning (L72); Bal turns the castle's insult into a joke (L10). Body rebel: "a crack that hit Bal in the teeth" (L66); Lora's pride getting away from her (L22, to be re-rendered without a blush). Techniques: pride, humor in danger, quiet dread at the map, anticipation (Amelia's demand). | none |
| Engagement (Dim 7) | 8.5 | Self-insertion: an outcast mage who becomes the man a general takes orders from, and a goddess who keeps a secret prize for him. Empathy: the castle's slow freeze. Fascination: what Amelia will demand, and why a giftless man is High Priest. | none |
| **FLOOR** | **7.5** | | Characters (gesture caps); Prose (Pattern #11) |
| **AVERAGE** | **8.1** | (8.5×4 + 7.5×2 + 8.0) / 7 = 8.14 | Single dimensions are not the bottleneck; the caps are mechanical |

## CVI-Launch Breakdown (Commercial Assessment)
| Input | Score | Evidence |
|-------|-------|----------|
| Commercial Pacing | 8/10 | Short sections, a monster at the midpoint, a war plan, a soft cliff |
| Tomorrow Test | 3 anchors (2 image + 1 quote) → 9 | The finger-high flame; the map with no villages; "We will not respond in kind." |
| Casual Reader | 8.5/10 | Warm crew, a monster kill, a goddess with a secret. They would keep reading |
| Shareability (quote/plot/emotional) | 3/2/2 → 5.5 | "We will not respond in kind."; Viridia one-shots a lake snake |
| Concept Pitch | yes (10) | |
| Human Closeness | partial (5) | Half the chapter is war room and exposition |
| **CVI-Launch** | 7.7 + 0.5 (strong anchor) = **8.2** | |

**CVI-Legacy (default weights):** Originality 8.5×0.30 + Theme 8.5×0.25 + Cultural Vocabulary 3×0.20 + Re-readability 5×0.15 (the demand and the giftless Toma both pay off later) + Identity 4×0.10 = **6.4**.

## Anti-AI Scan (20 Patterns; commercial thresholds, 2.74k words)
1. Forced symmetry: Found, 1 (0.4/1k). "just loud enough to carry and just low enough to deny" (L8). Minor.
2. Empty poetic vocabulary: Clear.
3. Automatic rule of three: Found, 2 (0.7/1k). "spoons… hinges, … a brass box…, … buttons" (L28); "asking straight out, and guessing, and pretending not to care" (L168). Both earn their place; minor.
4. Em dashes: Clear (0).
5. Empty metaphors: Clear.
6. Dramatic "And" openings: Found, 1. "And once the war was finished" (L160). Minor.
7. Pseudo-philosophical closings: Clear.
8. Excessive parallelism: Clear. The "strike and pull back" repetition (L144) is functional.
9. Overly smooth transitions: Clear. "The war was a different matter." (L80) is the source's own pivot.
10. Described emotions: Found, 2. "The thing he was proudest of" (L26); "Bal was startled" (L118). Minor.
11. Explanatory extension: **Found, 3 (1.1/1k), over cap.** L22, L42, L164 (see Prose). The Toma line at L172 ("which ought to make him easier, and kept making him harder, because…") is thought-in-motion and is tolerated.
12. Binary negation opener: Clear.
13. Precision flex: Clear ("Three mornings a week" and "most of two classes" are natural).
14. Emotional control demonstration: Clear.
15. Authoritative description: Clear. The snake scene has gaps ("a distance Bal did not want to guess at").
16. Philosophical asides: Borderline, 1. "The war could be over and men could still be killed in it, simply because the winner felt like going on." (L158). It stays tied to Bal and the source rule. Tolerated.
17. Clean dialogue: Found, mild. The Fern exchange runs in turns, which follows the source's own Q&A.
18. Thematic echo chamber: Clear (plenty of texture).
19. Graduated reveal: Clear.
20. Emotional temperature report: Clear.
**Total: 7/20 present, most minor. CLEAN for commercial fiction (0–8).**

## Character Chaos Check (Bal)
- Irrelevant thought: present ("He wrote that down twice without meaning to"; the spies "to drink, Bal suspected").
- Cognitive distortion: faint (the dagger is weak, yet he would not trade it).
- Unprompted memory: present and triggered: the vendor (L28) and the rules conversation (L150), each returning to the scene.
- Failed emotional management: Lora's pride (L22); Bal's fingers drumming and then stopping (L100/128).
- Voice under pressure: demonstrated (the snake scene goes to one-line paragraphs).

## Secondary Character Chaos
- Lora: has her own moment (the drill, pride she can't hide).
- Viridia: has her own moment (the kill, the deadpan line, the silent dinner).
- Amelia: has her own moment (applause, the withheld demand, the silence at the fire).
- Fern: functions as a source-faithful briefing voice, with one moment of his own ("Spies, of course." Faintly surprised to be asked). Acceptable for a first appearance.
- Thad: reported only (deepening circles). Acceptable.

## Source Fidelity (L767–780)
Every source beat is present and in order:
- jobs as escape;
- "his own kind";
- Warfare praise, Lora training him;
- the flaming dagger as "a weak version";
- Thad's signals;
- Raizen's statement through his High Priest;
- the army afraid;
- the villagers beating and killing;
- Amelia unable to get involved;
- Fern's description;
- "There's not much we can do… pointless";
- the drumming on the dark wood;
- "nowhere to put them";
- the death toll;
- "Could we do the same…" / "We will not respond in kind.";
- accepted deaths but won't stand by;
- three priests and the High Priest in Pashar;
- monthly at an inn in Londra;
- the spies with no sygls;
- "They hate seeing what's happening";
- measuring Pashar to Londra;
- the order to learn how often they meet the High Priest;
- Toma's file;
- Aren won't step in;
- why no gift / "his case was different";
- Raizen's squads and Naisura (source "Waisura" correctly fixed);
- the war rules in source order;
- "smiled slowly… I know exactly what I shall demand";
- "you'd have to win";
- notes and rune homework.

The author-ruled additions are present:
- **Shirts:** materials bought, each rune charged, worn on jobs, never tested. ✓
- **Snake:** about 420 words, at the lake, near the end of the six weeks, killed by lightning from Viridia's hand. ✓ It fits Ch.21's "the lake we found last week".

Fidelity problems (all fixed below):
- **L76:** "Lora hadn't either." Bal cannot know this. It is the content of Lora's Ch.23 line (source L868: "The only time I've seen her use it…"), so it pre-spends her reveal. "She kept a good arm's length from Viridia until they were home." adds friction and fear between friends that the source does not have. In Ch.23 Lora's tone is admiring and teasing ("one scary lady"), so this cuts against the requested warm tone.
- **L70:** Viridia's hair "standing out… blue and crackling". The source's first crackling-hair beat is at Winespring (L865, "As happened when she was nervous her hair began to crackle"; the guard's awe and Ms. Locklan's "by the sparking hair"). STYLE_CONSTRAINTS rules that this gesture appears "only where the source has them". Here it pre-spends the Ch.23 moment.
- **L42:** "in all the months since the mausoleum she had not praised a single thing to be kind" invents a trait for Amelia and is also an explanatory extension.
- **L42:** "Viridia asked if it would light a pipe" implies a smoking habit the source never gives her (source L918: she "seldom partake[s] in spirits").
- **L156:** "Nobody had formally declared anything yet. Bal had noticed that, lying there, and kept it to himself." This is an invented inference that adds information (Bal privately tracking the undeclared war) and steps toward Amelia's declaration in Ch.19.
- **Minor, optional:** L108 "See how they like it?" (source: "see how they respond to it"; the bible's sample line keeps "respond"). L86 "it trained harder" (source: "would fight harder").

**The two items the caller asked about:**
- **Bal: "he would never be that kind of winner" (L158). ACCEPTABLE, trimmed.** It is interior, not plot. It follows directly from the source's "We will not respond in kind." It is not dread, and the source never contradicts it: the war ends with Toma's conversion (L997, "technically the war was over") and no post-war slaughter follows. Cut its tail ", and he had not needed to say so to her either". That tail doubles the "kept it to himself" shape of L156 and makes a habit of Bal's silent resolutions.
- **Viridia: "Well. I won't be filling my water skin here." (L72). ACCEPTABLE, keep.** The author ordered the scene shown, and the source gives it no dialogue. The line adds no information or lore and fits her dry register ("miss book smart"). It also reads naturally as a joke that Ch.21's swim answers. One invented Viridia quip per scene is the limit, which is another reason to cut the pipe line (F6).

## Magic Repetition Note
- **Spells used:** runes (the flaming dagger, the arrow shirts; both source); Viridia's lightning (once, author-ruled); Amelia's teleport only implied ("Amelia took him to the hidden temple", offstage); the rune stone's signal. No blood whip, and no invented spell.
- **Ledger update:** Runes, add 18. Lightning (Viridia), add 18. Teleport, add 18 (implied, offstage). Teleport stays the most-used effect so far, but here it is offstage and costs nothing. No repetition flag for the author this chapter.

## The Tomorrow Test
**What the reader remembers:** a flame no taller than a finger creeping up a dagger nobody at the next bench looks up from, and Bal refusing to trade it for any sword. Then Fern's map with every troop marked and no villages on it.
**Anchor type:** BOTH (IMAGE: the dagger, the map, the lit-up lake; QUOTE: "We will not respond in kind.")
**Verdict:** ANCHOR EXISTS. It is not a repeat of Ch.17's anchor type (the stones dropped); the single-use map image is spent here as the ledger requires.

**Shareability:** "Viridia one-shot a lake monster and then complained about her water." Also "We will not respond in kind."

## Reader Reports
**The Devourer:** carried by the snake and the war room. Might skim the Toma paragraph and the squads history (L140–146). The final line, "saw her lips part", is a soft stop. The outline's actual hook line would have turned the page for them.
**The Critic:** underlines "There was a dorm full of it", "had stopped at not liking" and "no mark on it anywhere for a village". Is disappointed by three over-explained beats (L22, L42, L164) and the cosy "as if the win were hers".
**The Hostile:** challenges the following:
- How does Bal know Lora had never seen Viridia's power (L76)?
- Why is Viridia's hair crackling, when the source introduces that as a startling sight at Winespring?
- Does Viridia smoke?
- A third "grey" for Fern's eyes, and Fern's "missed very little" lifted from Xavier.
**The Casual Reader:** likes the crew, laughs at the water-skin line and the applause, and feels the castle's coldness without being depressed by it. Keeps reading: 8.5.

## Cross-Reader Matrix
| Issue | Devourer | Critic | Hostile | Casual | Severity |
|---|---|---|---|---|---|
| POV leak / Lora wary of Viridia (L76) | | ✓ | ✓ | ✓ (sours the warm moment) | IMPORTANT |
| Pattern #11 over-explaining (L22, L42, L164) | | ✓ | ✓ | | SHOULD FIX (cap) |
| Lora blushing again / "stayed that way" (L22) | | ✓ | ✓ | | SHOULD FIX (cap) |
| Posture cluster in closing tableau (L172–176) | | ✓ | ✓ | | SHOULD FIX (cap) |
| Crackling hair pre-spent (L70) | | ✓ | ✓ | | SHOULD FIX |
| Soft hook (L176) | ✓ | | | ✓ | SHOULD FIX |
| Pipe implies a habit (L42) | | | ✓ | | INVESTIGATE |
| "top up" / "hearthrug" register | | ✓ | ✓ | | SHOULD FIX |

## Revision Recommendations (Ranked)
| # | Location | Problem type | What happens now | Why it fails | Revision direction | Project rule? |
|---|---|---|---|---|---|---|
| F1 | L76 | Logic / Character | "Until that day Bal hadn't seen Viridia use her own power. Lora hadn't either. She kept a good arm's length from Viridia until they were home." | Bal can't know Lora's history. It pre-spends Lora's Ch.23 line and invents fear between friends (tone). | Cut "Lora hadn't either. She kept a good arm's length from Viridia until they were home." Keep the first sentence. | Yes: a later chapter's reveal is not pre-spent |
| F2 | L70 | Continuity / Canon | "Her hair was standing out around her head, blue and crackling at the ends, and she hadn't noticed." | The crackling hair is a source gesture whose first appearance is Winespring (L865, Ch.23). It is used only where the source has it. | Cut the sentence. L72 then follows "Viridia lowered her hand." directly. | Already a rule |
| F3 | L22 | Character (gesture recurrence) + Style (#11) | "she told him it had been adequate, and then went red with pleasure and stayed that way until breakfast, as if the win were hers." | It is Lora's third consecutive chapter blushing. "went X and stayed" is a narrator reflex. It is also an explanatory extension. | → "she told him it had been adequate, and was pleased with herself all through breakfast." | Yes: Lora's blush is rested for 3+ chapters |
| F4 | L42 | Style (#11) / invented trait | "said it was lovely work, and Bal believed her, because in all the months since the mausoleum she had not praised a single thing to be kind." | It explains the beat and invents an Amelia trait. | → "said it was lovely work, and Bal believed her." | No |
| F5 | L164 | Style (#11) | "Amelia had lifted her chin and smiled at him. The smile came slowly, and it took its time crossing her face." | "slowly" and "took its time" say the same thing. It is also the third "lifted". | → "Amelia had smiled at him. The smile came slowly." | No |
| F6 | L42 | Character (invented habit) | "Viridia asked if it would light a pipe." | It implies a smoking habit the source never gives her, and it is the second invented Viridia quip in the chapter. | Cut the sentence. | No |
| F7 | L94, L112 | Character (shared descriptor) / Style | "grey eyes that missed very little"; "Fern lifted his grey eyes to Bal" | It duplicates Xavier's Ch.11 "did not miss much". It is a third "grey" in 20 lines and a "lifted" repeat. | L94 → "intelligent grey eyes" (the source's word). L112 → "Fern looked up at Bal and left the idea where it lay." | No |
| F8 | L172, L176 | Character (gesture cluster) / register | "Bal sat in his dorm"; "curled up"; "lay across"; "Amelia sat on the hearthrug" | 4 posture beats in about 150 words; "hearthrug" is British. | L172 → "Bal was in his dorm with a pad of paper on his knee". L176 → "Amelia was on the rug by the hearth with her feet folded under her skirt." | No |
| F9 | L156 | Logic (invented inference) | "Nobody had formally declared anything yet. Bal had noticed that, lying there, and kept it to himself." | It adds information the source does not have. | Cut both sentences. | No |
| F10 | L158 | Character (trim) | "…that kind of winner, and he had not needed to say so to her either." | It doubles the silent-resolution shape. The resolution itself is acceptable (see Source Fidelity). | End at "he would never be that kind of winner." | No |
| F11 | L176 (end) | Pacing (hook) | The chapter stops at "saw her lips part." | The outline's Ch.18 hook is the line itself, so the chapter ends on a tease and not a hook. | Append: `"It's going to happen tomorrow," she said.` Ch.19 then opens on Bal's startled "What's going to happen tomorrow?" (tell the Ch.19 writer). | No |
| F12 | L54 | Style (register) | "top up the skins" | British. | → "fill the skins". | No |
| F13 | L8 | Style (#1 + filter) | "just loud enough to carry and just low enough to deny" | Two "just"s, symmetric. | → "loud enough to carry and low enough to deny". | No |
| F14 (optional) | L108, L86 | Dialogue fidelity | "See how they like it?"; "it trained harder" | Source: "see how they respond to it"; "would fight harder". | → "See how they respond?"; "it would fight harder for being afraid". | No |

**Keep as is:** Viridia's "Well. I won't be filling my water skin here." Bal's "never be that kind of winner" (trimmed per F10). Fern licking his thumb (once; logged in the bible as not recurring).

### Fix order: Logic/Character (F1, F2, F6, F9, F3, F7, F8, F10) → Structural (F11) → Prose (F4, F5, F12, F13) → Factual (F14)

## Strengths to PRESERVE
- "His own kind, as far as the castle went, was Bal. There was a dorm full of it." (L10)
- The dagger scene: the false start, "Nothing happened.", the finger-high flame, nobody looking up, "would not have traded it" (L34–40).
- "It was a Tuesday, or it might have been a Thursday." (L32), the right kind of ugly.
- The snake's rise in one-line paragraphs (L56–62) and Amelia's applause (L74).
- "It had no mark on it anywhere for a village." (L100) and "The map had not changed while Fern was gone." (L138).
- The present-evening tableau with Hopper twitching in a dream (L174).

## PATH TO 8.5
- **Characters 7.5 → 8.5 requires:** F3 (rest Lora's blush; re-render her pride as "pleased with herself"), F8 (break the 4-posture tableau at L172–176) and F7 (give Fern back the source's "intelligent grey eyes" so he doesn't share Xavier's descriptor). Also F1/F6/F9 to remove invented friction, habit and inference. Chaos already stands at 3/4 and stays inhabited.
- **Prose 7.5 → 8.5 requires:** F3, F4 and F5 cut the three Pattern #11 extensions, taking #11 from 1.1/1k to about 0.4/1k. The close-the-book sentence is already there (L100). F12 and F8 fix the register slips.
- **Pacing 8.0 → 8.5 requires:** F11. End on Amelia's spoken "It's going to happen tomorrow." so the chapter closes on a question, not a parted lip. F1 also clears the logic leak.

## VERDICT
**POLISH.** Genesis Floor 7.5 / Average 8.1 / Casual 8.5. With F1–F13 applied: projected Floor 8.5 (Characters 8.5, Prose 8.5, Pacing 8.5) → **PASS**.

BIAS CHECK: This evaluation was produced by the same system that wrote the prose. Confidence in scores above 8.0 requires external validation (beta readers, editors, comp analysis).

## Revision applied (2026-10-20, book-editor)
- **Applied as quoted:** F1, F2, F3, F4, F5, F6, F8, F9, F10, F12, F13.
- **F7, adjusted:** L94 → "intelligent grey eyes" as quoted. At L112 the quoted "Fern looked up at Bal" pushed "looked up at" to 3 uses book-wide (Ch.3, 14, 18) and failed `tic_report.py --gate`, so it is now "Fern met Bal's eyes and left the idea where it lay."
- **F11 skipped:** Ch.19 is being drafted in parallel and already opens on Amelia's "It's going to happen tomorrow." Ch.18 therefore still ends just before she says it ("saw her lips part"), so the line is not spoken twice.
- **F14 (optional):** not applied.
- **Gesture re-count fixes** (500-word windows, all classes now ≤2):
  - Hand holds: the vendor's "longsword held high" → "longsword raised".
  - Looks: "she had watched other people play" → "seen".
  - Posture: Amelia "lying across the foot of his bed" → "at the foot of his bed"; the book "lay open" → "was open".
- **Other checks:** em dashes 0, "the way [x]" 0, similes about 2.3/1k. Word count is now about 2,630, still within the 2,500–3,200 range.
- **Gates:** `style_check` clean, `grammar_check` 0 errors, and `voice_wear_check` and `tic_report --gate` both clean on a scratch copy of Ch.1–18.
