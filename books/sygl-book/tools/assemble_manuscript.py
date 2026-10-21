#!/usr/bin/env python3
"""Assemble Sygl's chapter files into the single-file manuscript the production
tools read (tools/make_epub.py and tools/build_interior.py).

    python3 books/sygl-book/tools/assemble_manuscript.py

In:  manuscript/chapter-01.md ... chapter-30.md   ("# Chapter One: Title", "---" breaks)
Out: manuscript/full-manuscript-<revision>.md      (revision from delivery/ebook.yaml)

Output format (what make_epub.py expects):

    CHAPTER ONE

    The Roof and the Flicker

    prose, one paragraph per block ...

    * * *

GENERATED — never hand-edit the output; fix the chapter files and re-run. The
chapter files are read only. Typesetting typography (curly quotes, ellipsis) is
applied here so print and ebook match.
"""
import glob, os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from production_common import BOOK, load_config, manuscript_path, smarten  # noqa: E402

HEAD = re.compile(r"^#\s+Chapter\s+([A-Za-z]+(?:-[A-Za-z]+)?)\s*:\s*(.+?)\s*$")
BREAK = re.compile(r"^(-{3,}|\*{3,}|\* \* \*)$")


def main():
    cfg = load_config()
    files = sorted(glob.glob(os.path.join(BOOK, "manuscript", "chapter-[0-9][0-9].md")))
    if not files:
        sys.exit("error: no manuscript/chapter-NN.md files")
    out = [cfg["title"], "", cfg["author"], ""]
    problems = []
    for f in files:
        lines = open(f, encoding="utf-8").read().splitlines()
        heads = [l for l in lines if l.startswith("# ")]
        m = HEAD.match(heads[0]) if len(heads) == 1 else None
        if not m:
            sys.exit(f"error: {os.path.basename(f)}: expected exactly one '# Chapter Word: Title' heading")
        word, title = m.group(1).upper(), m.group(2)
        out += ["", f"CHAPTER {word}", "", smarten(title), ""]
        paras, buf = [], []
        for l in lines:
            if l.startswith("# "):
                continue
            if not l.strip():
                if buf:
                    paras.append(" ".join(buf)); buf = []
                continue
            buf.append(l.strip())
        if buf:
            paras.append(" ".join(buf))
        for p in paras:
            if BREAK.match(p):
                out += ["* * *", ""]
                continue
            s = smarten(p)
            if s.count("“") != s.count("”"):
                problems.append(f"{os.path.basename(f)}: unbalanced double quotes: {s[:70]}...")
            out += [s, ""]
    dest = manuscript_path(cfg)
    open(dest, "w", encoding="utf-8").write("\n".join(out).rstrip() + "\n")
    print(f"wrote {dest}  ({len(files)} chapters)")
    for p in problems:
        print("note:", p)


if __name__ == "__main__":
    main()
