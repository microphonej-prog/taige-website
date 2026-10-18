#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""清除正文里误入的软连字符（U+00AD）。"""
import sys

for p in sys.argv[1:]:
    s = open(p, encoding="utf-8").read()
    n = s.count("\u00ad")
    if n:
        open(p, "w", encoding="utf-8", newline="").write(s.replace("\u00ad", ""))
    print("%s  软连字符 %d 处" % (p, n))
