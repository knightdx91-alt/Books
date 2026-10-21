# STORY-LEVEL STRENGTHENING (STATE.yaml decision 2026-10-21), fixes 3 and 4 only.
# Fix 3: Lora / Viridia correct Bal on a PRACTICAL point and he adopts it (Ch.22, Ch.23 x2).
# Fix 4: one short war-pressure beat in each school chapter 9-17 (Ch.18 already widens the war).
# Each entry: (id, chapter, anchor text occurring exactly once in that chapter, anchor + insertion).
# Not applied to the manuscript. Does not touch Ch.25, Ch.28, Ch.29.
G = [
# ---------------- FIX 4: war pressure, Ch.9-17 ----------------
("W09", "09",
'''Once or twice somebody at the Tempus table leaned out to see who Viridia was eating with, and leaned back in.''',
'''Once or twice somebody at the Tempus table leaned out to see who Viridia was eating with, and leaned back in. The second time, Bal caught a scrap of what they were saying over there. The clap, and what Raizen's face had done at it. A boy with his collar turned up said a god didn't get made to jump in front of the whole school and then forget it, and nobody at his end of the bench told him he was wrong.'''),

("W10", "10",
'''"I, um. I've had practice," she said. "My father trained me. He was with Kenmei's army when he was younger."''',
'''"I, um. I've had practice," she said. "My father trained me. He was with Kenmei's army when he was younger."

Bal had read about that army that same morning, in a book by the library window: a command tent sealed in stone and sunk, and everybody left outside it finished soon after. He didn't ask her which war her father had marched in, or how many of the men beside him had come home again. You didn't ask that of someone whose name you had learned a minute ago.'''),

("W11", "11",
'''Flags stood up all through the main camp on tall poles, and each carried the same jagged yellow mark, snapping in the wind. It was Raizen's. Tempus.''',
'''Flags stood up all through the main camp on tall poles, and each carried the same jagged yellow mark, snapping in the wind. It was Raizen's. Tempus. Not an hour ago that mark had gone up the castle steps on the back of Viridia's sweater. Here it flew over every tent in the valley.'''),

("W12", "12",
'''Tonight she was back in the dorm, or off in the mountains moving people into a canyon, and the place at his elbow stayed a plain stretch of wood.''',
'''Tonight she was back in the dorm, or off in the mountains moving people into a canyon, and the place at his elbow stayed a plain stretch of wood. Whoever she was moving tonight had his own mark on their palms and a crate or two of what they owned, and had left home because Amelia had a feeling about Raizen and did not mean to wait and learn whether she was right.'''),

("W13", "13",
'''At the counter he paid for all five.''',
'''At the counter he paid for all five. The stout woman turned Raizen's history over to find the price and told her ledger that he was the third person this month to want that one. For years before that, nobody had asked. Bal answered that it was for school, which was nearly true, and she wrote it down.'''),

("W14", "14",
'''The last mile was uphill. Bal's feet hurt and the meat rolls were miles behind him and nobody said much on that stretch.''',
'''The last mile was uphill. Bal's feet hurt and the meat rolls were miles behind him and nobody said much on that stretch. On the climb his mind wandered off to yesterday's hill without asking him, to the cold wind and the gray tents and the soldiers wheeling in their blocks below. It would not sit beside grandmothers in the plaster and a girl who had walked into a puddle for being right. The two refused to belong to the same week, and they were in it anyway.'''),

("W15", "15",
'''Mr. Porter set the class an essay on the duties of a familiar before he had sat down, and watched Bal the whole time they wrote it.''',
'''Mr. Porter set the class an essay on the duties of a familiar before he had sat down, and watched Bal the whole time they wrote it. At the bell he bent and said something low to Huginn, and the raven left by the open top of the window without its cheese and flew off over the forest, steady and straight, until Bal lost it against the trees.'''),

("W16", "16",
'''"At least four more hours," he said. "Maybe five." He paid for his own pie.''',
'''"At least four more hours," he said. "Maybe five." He paid for his own pie.

The pie man took the coins off Bal's left palm by their edges, careful as somebody lifting a coal off a hearth, and wiped his fingers down his apron afterward. Nobody else at the stall saw it. Bal decided not to mention it with Amelia standing right there.'''),

("W17", "17",
'''It was an uneventful walk, though his head ached most of the way.''',
'''It was an uneventful walk, though his head ached most of the way. Twice before Whitehaven he felt in his pocket for Thad's stone. It was cool and dark each time. Somewhere out there Raizen's men were drilling for a war, and all the stone could tell him was that nobody had sent for him yet.'''),

# ---------------- FIX 3: the girls are right, Bal changes the plan ----------------
("P22", "22",
'''"Yeah," she said. "Didn't figure you would. So that leaves us doing it ourselves. And Amelia can't come. The others would see it as interfering, so she'll have to stay behind."''',
'''"Yeah," she said. "Didn't figure you would. So that leaves us doing it ourselves. And Amelia can't come. The others would see it as interfering, so she'll have to stay behind."

Lora pushed the map away an inch.

"And then there's me. What am I, in all this? To Viridia, I mean."

"Her companion," Bal said. "A friend from home. Somebody she'd travel with."

"Then I'm a lady too, and ladies get introduced. The first priest who sits down with us asks whose daughter I am and where my father's land is, and I don't have an answer that lasts past the soup. Make me her maid. Nobody asks a maid anything. A maid can go out alone to the shops and the market, and nobody bothers to remember her face."

Bal had pictured the three of them riding in as near enough equals. It was plain now how fast that would come apart at a supper table.

"Maid it is," he told her.'''),

("P23a", "23",
'''It was hot and the cheese went soft. At night they made no fire.''',
'''It was hot and the cheese went soft.

The first night, Bal had an armful of deadwood together before Viridia saw what he was doing.

"Put that down," she said. "Out here? Anybody could see that smoke from a day off. Back home we always knew when the tinker was coming, because he cooked his supper every night on the road in. Half the village would be waiting for him at the well." She tore off a piece of biscuit. "He thought we were just friendly."

Bal turned to look. The grass ran flat and yellow to the edge of the sky all around them, and a single farm showed from miles away. He let the wood fall where he stood.

After that they made no fire at all.'''),

("P23b", "23",
'''He hoped he looked enough like a servant. He had seen plenty of servants. He had never paid attention to how they stood.''',
'''He hoped he looked enough like a servant. He had seen plenty of servants. He had never paid attention to how they stood.

Lora had. "Sit up," she said, low, without turning her head. "You look like you stole that horse and you're sorry about it. A servant from a good house rides straight and looks at nothing. He isn't ashamed. He's bored."

Bal straightened in the saddle. He picked out a stone in the wall above the guards' heads and gave it his whole attention, and did his best to be bored by it.'''),
("P24", "24",
'''"That's a lot of rooms." Viridia had stopped on the opposite side of the street, as though she were only waiting for a cart to pass. "The inn in my village had six. And that wasn't counting the one the innkeeper and his wife slept in."''',
'''"That's a lot of rooms." Viridia had stopped on the opposite side of the street, as though she were only waiting for a cart to pass. "The inn in my village had six. And that wasn't counting the one the innkeeper and his wife slept in."

Bal had half a mind to cross over and stroll down the side of the place, past the stable, to see the back half the priests would take.

"Don't," Viridia said, still facing the street. "A lady's manservant doesn't wander off to poke around somebody else's stable while she stands in the road. Somebody would ask him his business. Then they'd ask me." She tipped her chin at the traffic. "We're waiting for a cart. Watch for the cart."

Bal watched for the cart.'''),
]

if __name__ == "__main__":
    import sys, os
    root = sys.argv[1] if len(sys.argv) > 1 else '/home/user/Books/books/sygl-book'
    miss = 0
    for i, ch, o, n in G:
        p = os.path.join(root, 'manuscript', f'chapter-{ch}.md')
        t = open(p).read(); c = t.count(o)
        if c != 1:
            print('MISS', i, ch, c, o[:70]); miss += 1; continue
        open(p, 'w').write(t.replace(o, n))
    print('applied', len(G) - miss, 'missed', miss)
