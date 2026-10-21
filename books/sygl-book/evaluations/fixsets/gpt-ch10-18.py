# ChatGPT close reading, Ch.10-18 (installments 09-17): new apply-ready fixes.
# (id, chapter NN, old, new). Each old string occurs exactly once in the chapter file,
# both before and after the 231 pending fixes, and overlaps no pending fix.
# Triage: evaluations/chatgpt-triage-ch10-18.md
G = [
("G11.01", "11", "It was the same as Viridia's, with differences.", "Her uniform was the same as Viridia's, with differences."),
("G14.42", "14", "The card propped beside it in the window, he explained,", "The jeweler's card propped beside it in the window, he explained,"),
("G16.27", "16", "through the old man's right knee and out the back of it.", "through the old man's unprotected right knee and out the back of it."),
("G17.22", "17", "He was not really hurt. The thing that had hit him was.", "He was not badly hurt. The thing that had hit him was."),
("G17.25", "17", "It was an uneventful walk.", "It was an uneventful walk, though his head ached most of the way."),
]

# Author's-call options that were gate-tested on the same scratch copy (NOT part of G):
C_TESTED = [
("C-13.38", "13", "I'm nothing like anyone else you've known.", "I won't treat you the way other people have."),
("C-18.inj", "18", "Ever since the road to Whitehaven she had taken his training as her own personal job.", "The cuts from the road to Whitehaven had healed to thin pink lines, and ever since then she had taken his training as her own personal job."),
]

if __name__ == "__main__":
    import sys, os
    os.chdir(sys.argv[1] if len(sys.argv) > 1 else "/home/user/Books/books/sygl-book")
    sets = G + (C_TESTED if "--with-c" in sys.argv else [])
    miss = 0
    for i, ch, o, n in sets:
        p = f"manuscript/chapter-{ch}.md"; t = open(p).read(); c = t.count(o)
        if c != 1: print("MISS", i, ch, c, o[:60]); miss += 1; continue
        open(p, "w").write(t.replace(o, n))
    print("applied", len(sets) - miss, "missed", miss)
