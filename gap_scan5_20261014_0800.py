#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""round5：核对 France / Germany / Netherlands 在全站的出现范围（判断是否有专篇）。"""
import os, glob

ROOT = os.path.dirname(os.path.abspath(__file__))
rows = []
for lang in ["", "en/", "ja/", "ko/", "fr/", "es/"]:
    for f in glob.glob(os.path.join(ROOT, lang + "blog/*.html")):
        if os.path.basename(f).startswith("_body"):
            continue
        rows.append((lang or "zh", f, open(f, encoding="utf-8").read()))

for kw in ["France", "French", "法國", "français", "Germany", "German", "德國", "deutsch",
           "Netherlands", "荷蘭", "Dutch", "Nederland", "Spain", "Spain's", "西班牙",
           "Italy", "意大利", "Poland", "波蘭", "Sweden", "瑞典", "Norway", "挪威"]:
    hits = [(l, os.path.basename(f)) for l, f, t in rows if kw.lower() in t.lower()]
    print("%-14s files=%3d  %s" % (kw, len(hits), sorted(set(x[1] for x in hits))[:6]))

# 每个语言各有多少篇，以及 slug 是否有 france/germany 等
slugs = sorted(set(os.path.basename(f) for _, f, _ in rows))
print()
print("含 fra/germ/neth/country 后缀的 slug:", [s for s in slugs if any(k in s for k in ("france", "german", "neth", "spain", "ital", "poland", "swed", "norw"))])
