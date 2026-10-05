#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""对比新旧文章 meta description 长度，确认中文 desc 与既有批次量级一致。"""
import re

FILES = ["blog/garment-piping-bias-binding-guide.html",
         "blog/shoulder-pad-structure-trims-guide.html",
         "blog/hang-tag-moq-cost.html",
         "blog/sewing-thread-selection-guide.html",
         "blog/flame-retardant-trims-guide.html"]

for p in FILES:
    s = open(p, encoding="utf-8").read()
    m = re.search(r'<meta name="description"[^>]*content="([^"]*)"', s, re.S)
    d = m.group(1)
    print("%-52s 汉字=%3d 总长=%3d" % (p, len(re.findall(r'[\u4e00-\u9fff]', d)), len(d)))
