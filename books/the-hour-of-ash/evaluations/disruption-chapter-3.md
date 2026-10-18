# Disruption Report: Chapter 3 (Parnassus), run 2

I backed up the pre-disruption text to `manuscript/reports/chapter-3-pre-disruption.md`. It sits outside `chapters/` because the gates glob `chapter-*.md` there.

**Verdict on the input:** a strong single-scene chapter. It already has chaos (aglet, the pee, the cellar memory, all-or-nothing), an ugly sentence, a granola wrapper chased into a thornbush, and a simile rate of 1.8/1k. So this was a light pass: one mandatory fix, a gesture-tic sweep made almost entirely of cuts, and **3 operations**.

## Mandatory fix: the goatherd (device pattern-tic)
- **Before:** he shouted into a mobile phone, pressed it to his chest to greet her, put it back to his ear, and later "lowered his telephone" for the German. That made him the third character in three chapters to turn to a device instead of Mara (Szabo's TV in Ch.1, the jeweler's phone in Ch.2).
- **After:** he is shouting up the slope at one brown nanny who has climbed onto a ledge "and was eating something there that she preferred." He shouts the same word every time, "her name or his opinion of her," with more disgust each time. "She did not come down. He broke off for me in the middle of the word." After the greeting: "Then he finished the word, and the nanny went on eating." Later, for the German: "The old man on the stone left off with the nanny to greet him."
- His attention still belongs to something other than Mara, but now it is his animal, which suits Parnassus in 1998. I used no nod, shrug, look-away, "moment," point or object handling. The phone is gone from the chapter, so the entity tracker should drop "goatherd with a mobile phone" from the writer report's continuity notes.

## Gesture-tic sweep (standing law: 4+ of one class is a tic; brief: no more than 2 per class)
All of these are cuts or rewordings. Nothing new was added.
| Class | Before | Fix |
|---|---|---|
| Strangers sizing up the duffel | 4 (taxi points at it, desk woman "considered the duffel", German "looked at the duffel with real pleasure", German "revised his opinion") plus the German's tap | Cut the desk woman's clause ("I had said no, up.") and the German's first look. Kept the taxi, the tap and "revised his opinion". |
| Flashlight on/off | 4 of Mara's within about 500 words (3 switch beats plus "lit") | Cut "and switched off again" and "and switched off". "I switched on the flashlight" became "I thumbed the flashlight on." |
| Sitting on the bag | 4 | Cut "sat on it again" (L145 now ends "I climbed back up to the bag."). |
| Ears/face hot | 3 inside 500 words at the crossing (face hot, ears in the blush, "My ears were burning") | Cut "My ears were burning." The anchor's hot ears (L131) and the surprise blush stay. |
| Look | 3 (glancing up, looked out at the mouth, looked at the watch) | "I looked at the watch. Ten to two." became "The watch said ten to two." |
| Laugh | 3 (the taxi driver twice, the German once) | Cut "He was still laughing when". |
| Rest stops | 5 instances of "I stopped" | "From where I stopped to breathe, the plateau…" became "The plateau…". "I stopped and read Fenn's directions" became "I read Fenn's directions". |
| Hand-overs in the camera swap | 3 inside about 400 words | "He had his hand out for… and I gave it to him" became "He had my father's camera before I could think how to keep it". |
| Self-echo | "poles going ahead of him" ×2 | The second became "poles first". |

## Operations Applied
| # | Operation | Location | Before → After (brief) |
|---|---|---|---|
| 1 | Simile Surgery (#11) | German/Pentax; the bone in her pocket | (a) Cut "as though it might go off". Narration had been explaining his line ahead of time; "It is like a gun" now lands on its own. That also takes the chapter's only "as if/as though" to 0. (b) "It was cold from the dirt and then it was not, because my hand had warmed it." → "…and then it was not." The because-clause restated the image. |
| 2 | Missing Paragraph | after "I pocketed it." | Deleted the one-line paragraph "Then I went on into the dark." It was predictable as a scene button, and with "Then I went in." and "Then my face went hot." it made a run of three one-line "Then…" paragraphs. The next paragraph ("Past the slumped stone the floor began to climb…") already carries her movement. |
| 3 | Break the graduated reveal, using human noise that resonates with nothing | between recognizing Fenn's drawing and the last paint boulder | Recognizing the drawing was the top of a neat ladder of steps (arch, drawing, paint, mouth, inscription). The dread now drops into boredom and hunger for one short paragraph: "After that the arch hardly got any nearer. Somewhere on the last zigzags the Hanson song from the summer before got into my head, only the chorus, which had no words in it I had ever been able to make out, and it went round and round in time with my boots. I was hungry again, and it was too soon for another granola bar." The song is true to the period (summer 1997), quotes no lyrics, and connects to nothing in the book. The deferred granola bar quietly sets up "I ate another granola bar in the dark" without changing the count (still two eaten). It adds no portent and no forward-gesture. |

## Operations NOT Applied (and why)
- **Irrelevant Thought (as a separate op):** skipped. The Writer already has four chaos moments. Op 3 is the only addition, and it is placed where the brief asked for a lapse.
- **Emotional Control Break:** skipped. The pocketing (hot ears, standing too fast) and the blush already leak.
- **Precision Deflation:** skipped. The numbers serve the story: coordinates, clock times against the sun, "forty or fifty" goats, 1840s to 1996 graffiti dates.
- **Ugly Sentence:** skipped. One exists ("My shoulder hurt and I moved the bag…").
- **Negation Break:** skipped. There are no define-by-negation openers.
- **Dialogue Mess:** skipped. The German exchange already interrupts ("I don't—") and talks past her ("Phoenix. Good, we send it to Phoenix.").
- **Separate wrong-register beat:** not added. The goatherd's grave "Kalimera" cut off halfway through his curse at a goat already supplies one, and the chapter has the Acme peas and the optative apology to Pan.

## Constraints verified
- The first sentence (79 words) is byte-identical to the backup. The last line is still "I stepped out into October."
- Scene breaks: **0**. Em-dashes: **1** (unchanged, the dialogue interruption). "As if/as though": **0**. Metacognition: 0. Emotional-temperature reports: 0. Foreshadowing: 0.
- Dialogue share is **5.8%** (band 5–15%). No dialogue words changed.
- The anchor (the bone, hot ears, the museum guard, her hand closed on it going out) and the surprise (the blush, the 1989 party, the unsaid "sorry") are intact.
- New phrases were checked against Ch.1–3. My first wording "long enough to" made a 3x book-wide hit, so I reworded it to "left off with the nanny". The tic gate is clean.
- No ENTITY_STATE contradiction: granola count, kit, timeline and film count are all unchanged.
- **Net words: 6,843 → 6,817 (−26)** by `wc -w`.
- `bash tools/check_chapter.sh 3`: style clean (simile 1.6/1k), grammar clean, rhythm 0, show/tell no flags, voice-wear strict clean, tic gate clean (gestures included), metaphor no flags, shape clean.

## Strongest Disruption
The goatherd. A phone in an old shepherd's hand was the book's third turn-to-a-device, and the reader would have started to feel the pattern. A man cursing one disobedient nanny, who stops halfway through a word for a stranger's greeting and then finishes it, gives the same brush-off in its own world, and it is funnier.

## Risk Assessment
- The Hanson song is the one place a modern pop reference enters narration. It is Mara's private 1998 noise, period-safe, and unnamed. If the Evaluator reads it as off-register, cut the second sentence and keep the hunger line.
- After the switch-off cuts, the flashlight's state between the pee and the cold is implied rather than stated ("in the dark", then "I thumbed the flashlight on"). Read in sequence, it holds.
