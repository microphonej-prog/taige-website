#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""对比新旧文章各语言 description 长度。"""
import re, glob, os

FILES = ["blog/zipper-selection-guide.html", "blog/fusible-interlining-guide.html",
         "blog/childrenswear-trims-guide.html", "blog/leather-garment-trims-guide.html",
         "blog/elastic-trims-selection-guide.html", "blog/garment-buttons-fasteners-guide.html",
         "blog/woven-label-density-guide.html"]

for f in FILES:
    if not os.path.exists(f):
        print(f, "缺失"); continue
    s = open(f, encoding="utf-8").read()
    m = re.search(r'<meta name="description"(.*?)>', s, re.S)
    blk = m.group(1)
    out = []
    for a in ("data-zh", "data-en", "data-ja", "data-ko", "data-fr", "data-es"):
        mm = re.search(r'%s="((?:[^"])*)"' % a, blk)
        out.append("%s=%d" % (a[5:], len(mm.group(1)) if mm else -1))
    print("%-42s %s" % (os.path.basename(f), "  ".join(out)))
