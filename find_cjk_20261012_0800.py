#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""定位 en/fr/es 语言页正文里残留的 CJK 字符（2026-10-12 批次）"""
import re

for p in ["en/blog/hang-tag-folding-types.html",
          "en/blog/retail-floor-ready-apparel-packaging.html",
          "fr/blog/retail-floor-ready-apparel-packaging.html"]:
    s = open(p, encoding="utf-8").read()
    b = s[s.index('<section class="article-body"'):]
    txt = re.sub(r'<[^>]+>', '', b)
    hits = list(re.finditer(r'[\u4e00-\u9fff\u3000-\u303f\uff00-\uffef]+', txt))
    print("==", p, "命中", len(hits))
    for m in hits:
        print("   ...", txt[max(0, m.start() - 80):m.end() + 40].replace("\n", " "))
