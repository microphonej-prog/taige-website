#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""抽取相关文章链接所需的六语 h1 标题"""
import os, re

ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)
FILES = ["denim-garment-trims-guide.html", "elastic-trims-selection-guide.html",
         "zipper-selection-guide.html", "clothing-size-label-guide.html",
         "knitwear-sweater-trims-guide.html", "rib-knit-collar-cuff-guide.html",
         "garment-drawcord-guide.html", "print-on-demand-apparel-labels.html"]
LANGS = ["blog", "en/blog", "ja/blog", "ko/blog", "fr/blog", "es/blog"]

for f in FILES:
    print("===", f)
    for d in LANGS:
        p = os.path.join(d, f)
        s = open(p, encoding="utf-8").read()
        m = re.search(r'<h1[^>]*>(.*?)</h1>', s, re.S)
        t = re.sub(r'<[^>]+>', '', m.group(1)).strip() if m else "MISSING"
        print("  %-8s %s" % (d.split("/")[0], t[:110]))
