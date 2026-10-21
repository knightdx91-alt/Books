# ChatGPT close reading, installments 01-08 (Ch.1-9): new apply-ready fixes (story unchanged).
# Format: (id, chapter NN, exact old text (occurs once, untouched by pending fixes), new text).
# Apply AFTER apply_all.py. Triage: evaluations/chatgpt-triage-ch01-09.md
G = [
("G1", "01", "That was a temple.", "Pillars, fire, a statue. That was a temple."),
("G2", "01", "about to attempt something crazy.", "about to attempt something crazy. The rug had never carried anything heavier than itself."),
("G3", "01", "aiming for the flat stretch beside it where he meant to land.", "aiming for the slates just below it where he meant to land."),
("G4", "01", "past the tops of tall pillars, past their fluted columns", "past the carved tops of tall pillars, past their fluted shafts"),
("G5", "04", "That's probably why they locked her away, now that I think about it.", "That's probably why the originators locked her away, now that I think about it."),
("G6", "05", "He yawned hugely in the middle of it and had to start over.", "He yawned hugely halfway through the message and had to start over."),
("G7", "06", "Which one was hers, she kept to herself.", "Which one was hers, she didn't say."),
("G8", "09", "with brown sugar melting in a crust on the top.", "with brown sugar melted into a crust on top."),
("G9", "09", "Some of them were bound to bring something large out of the forest", "Some of them, Bal supposed, were bound to bring something large out of the forest"),
("G10", "09", "to the ceiling to get it down.", "to the ceiling to swallow it."),
("G11", "09", "holding up a silver ring and waiting for something to come.", "holding up a silver ring and waiting for something to come. He remembered Mr. Porter's warning about the forest, and walked faster."),
]

if __name__ == "__main__":
    import sys, os
    os.chdir(sys.argv[1] if len(sys.argv) > 1 else "/home/user/Books/books/sygl-book")
    miss = 0; dw = 0
    for i, ch, o, n in G:
        p = f"manuscript/chapter-{ch}.md"; t = open(p).read(); c = t.count(o)
        if c != 1:
            print("MISS", i, ch, c, o[:60]); miss += 1; continue
        open(p, "w").write(t.replace(o, n)); dw += len(n.split()) - len(o.split())
    print("applied", len(G) - miss, "missed", miss, "net words", dw)
