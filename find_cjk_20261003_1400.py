#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""定位生成页正文里的汉字残留（ko 页应为 0）。"""
import re, sys

path = sys.argv[1] if len(sys.argv) > 1 else "ko/blog/zipper-selection-guide.html"
s = open(path, encoding="utf-8").read()
m0 = re.search(r'<section class="article-body">', s)
m1 = re.search(r'</section>', s[m0.end():])
body = s[m0.end():m0.end() + m1.start()]
body = re.sub(r'<script.*?</script>', '', body, flags=re.S)
for m in re.finditer(r'[\u4e00-\u9fff]', body):
    a, b = max(0, m.start() - 60), m.end() + 60
    print("...%s..." % body[a:b].replace("\n", " "))
    print("-" * 80)
