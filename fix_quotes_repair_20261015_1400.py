#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""修复 fix_quotes2 的误伤：把被误转成 “/” 的属性分隔引号还原为 ASCII " ，
仅保留真正的“值内引号”为中文引号，并重新按顺序配对。"""
import os, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)

NEI = "\u201c\u201d"   # “ ”


def repair(path):
    s = open(path, encoding="utf-8").read()
    out = list(s)
    inner = []
    n_delim = 0
    for i, c in enumerate(s):
        if c not in NEI:
            continue
        prev = s[i - 1] if i else ""
        nxt = s[i + 1] if i + 1 < len(s) else ""
        rest = s[i + 1:i + 10]
        if prev == "=":
            out[i] = '"'
            n_delim += 1
        elif nxt in (" ", "\n", "\r", ">", "\t") or rest.startswith("data-"):
            out[i] = '"'
            n_delim += 1
        else:
            inner.append(i)
    # 值内引号重新配对
    for k, i in enumerate(inner, 1):
        out[i] = "\u201c" if k % 2 else "\u201d"
    s2 = "".join(out)
    print("%s 还原分隔引号 %d 个；保留值内引号 %d 个" % (os.path.basename(path), n_delim, len(inner)))
    open(path, "w", encoding="utf-8", newline="").write(s2)


for p in sys.argv[1:]:
    repair(p)
