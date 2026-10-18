#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""打印指定文章的 h2 data-zh 清单，用于判断选题是否重叠。"""
import re, sys

for p in sys.argv[1:]:
    s = open(p, encoding="utf-8").read()
    print("=====", p)
    for m in re.finditer(r'<h2[^>]*data-zh="([^"]*)"', s):
        print("  -", m.group(1))
