#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-06 上午批次：用 OpenCC s2t 反查 ja/ko 属性值与 ja/ko 生成页里疑似简体字。"""
import re
from opencc import OpenCC

CC = OpenCC('s2t')
FILES = ["blog/garment-security-tag-guide.html", "blog/garment-wash-dye-trims-guide.html",
         "ja/blog/garment-security-tag-guide.html", "ja/blog/garment-wash-dye-trims-guide.html",
         "ko/blog/garment-security-tag-guide.html", "ko/blog/garment-wash-dye-trims-guide.html"]

for f in FILES:
    s = open(f, encoding="utf-8").read()
    print("== %s" % f)
    hits = 0
    for m in re.finditer(r'data-(?:ja|ko)="([^"]*)"', s):
        v = m.group(1)
        sus = sorted({c for c in v if re.match(r"[\u4e00-\u9fff]", c) and CC.convert(c) != c})
        if sus:
            hits += 1
            print("   %s  <<%s>>" % ("".join(sus), v[:70]))
    # 正文文本节点里（非属性）简体嫌疑
    body = re.search(r'<section class="article-body">.*?</section>', s, re.S)
    if body and f.startswith(("ja/", "ko/")):
        txt = re.sub(r'<[^>]+>', '', body.group(0))
        sus = sorted({c for c in txt if re.match(r"[\u4e00-\u9fff]", c) and CC.convert(c) != c})
        if sus:
            print("   正文可疑字: %s" % "".join(sus))
    print("   可疑条数: %d" % hits)
