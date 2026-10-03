#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""用 OpenCC s2t 反查 ja 属性值里疑似简体字（s2t 会改动的字），逐条打印上下文供人工判断。"""
import re
from opencc import OpenCC

CC = OpenCC('s2t')
FILES = ["blog/zipper-selection-guide.html", "blog/fusible-interlining-guide.html",
         "blog/interlining-check.html"]

for f in FILES:
    try:
        s = open(f, encoding="utf-8").read()
    except FileNotFoundError:
        continue
    print("== %s" % f)
    hits = 0
    for m in re.finditer(r'data-ja="([^"]*)"', s):
        v = m.group(1)
        sus = sorted({c for c in v if re.match(r"[\u4e00-\u9fff]", c) and CC.convert(c) != c})
        if sus:
            hits += 1
            print("   %s  <<%s>>" % ("".join(sus), v[:80]))
    print("   可疑条数: %d" % hits)
