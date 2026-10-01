#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-01 20:00 批次：canonical 与 sitemap 逐 URL 一致性比对（仅新文章）"""
import os, re

SLUGS = ["hang-tag-special-effects-guide.html", "rainwear-waterproof-garment-trims-guide.html"]
sm = open("sitemap.xml", encoding="utf-8").read()
locs = set(re.findall(r"<loc>([^<]+)</loc>", sm))

bad = 0
for pre in ("blog/", "en/blog/", "ja/blog/", "ko/blog/", "fr/blog/", "es/blog/"):
    for slug in SLUGS:
        p = "%s%s" % (pre, slug)
        s = open(p, encoding="utf-8").read()
        canon = re.search(r'<link rel="canonical" href="([^"]+)"', s).group(1)
        ok = canon in locs
        if not ok:
            bad += 1
        print("%-56s canonical=%-64s in sitemap=%s" % (p, canon, "YES" if ok else "NO"))
print("不一致数量 = %d" % bad)
