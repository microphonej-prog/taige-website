#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""量取现有文章 description 四语长度，用于对齐仓库既有口径。"""
import re, sys

FILES = sys.argv[1:]
for f in FILES:
    s = open(f, encoding="utf-8").read()
    m = re.search(r'<meta name="description".*?>', s, re.S)
    blk = m.group(0)
    out = []
    for k in ("data-zh", "data-en", "data-ja", "data-ko", "data-fr", "data-es"):
        mm = re.search(r'%s="([^"]*)"' % k, blk)
        out.append("%s=%d" % (k, len(mm.group(1)) if mm else -1))
    print("%-58s %s" % (f.replace("blog/", ""), "  ".join(out)))
