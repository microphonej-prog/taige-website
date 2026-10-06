#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-06 下午批次：用 OpenCC s2t 反查 ja/ko 属性值与 ja 生成页里疑似简体字。"""
import re
from opencc import OpenCC

CC = OpenCC('s2t')
FILES = ["blog/sequin-rhinestone-trims-guide.html", "blog/rib-knit-collar-cuff-guide.html",
         "ja/blog/sequin-rhinestone-trims-guide.html", "ja/blog/rib-knit-collar-cuff-guide.html",
         "ko/blog/sequin-rhinestone-trims-guide.html", "ko/blog/rib-knit-collar-cuff-guide.html"]

bad = 0
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
    body = re.search(r'<section class="article-body">.*?</section>', s, re.S)
    if body and f.startswith(("ja/", "ko/")):
        txt = re.sub(r'<[^>]+>', '', body.group(0))
        sus = sorted({c for c in txt if re.match(r"[\u4e00-\u9fff]", c) and CC.convert(c) != c})
        if sus:
            print("   正文可疑字: %s" % "".join(sus))
    print("   可疑条数: %d" % hits)
    bad += hits

print("\n结论: %s" % ("有 %d 处简体嫌疑" % bad if bad else "无简体残留"))
