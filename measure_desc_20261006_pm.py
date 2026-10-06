#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""desc 长度体检：与近期批次对比，确认 en/fr/es 落在 150-160 字符目标区间。"""
import re, os, glob

def get_desc_en(p):
    s = open(p, encoding="utf-8").read()
    m = re.search(r'<meta name="description"[^>]*?data-en="([^"]*)"', s, re.S)
    return m.group(1) if m else None

files = ["blog/sequin-rhinestone-trims-guide.html", "blog/rib-knit-collar-cuff-guide.html",
         "blog/garment-security-tag-guide.html", "blog/sewing-thread-selection-guide.html",
         "blog/flame-retardant-trims-guide.html", "blog/reach-svhc-apparel-trims-guide.html"]
for f in files:
    d = get_desc_en(f)
    print("%-52s desc_en=%d" % (os.path.basename(f), len(d) if d else -1))

print("\n-- 全体 blog 文章 desc_en 长度分布（近 30 篇）--")
allf = sorted(glob.glob("blog/*.html"), key=os.path.getmtime, reverse=True)
allf = [f for f in allf if "/_body_" not in f.replace("\\", "/") and not f.endswith("index.html")][:30]
lens = [len(get_desc_en(f) or "") for f in allf]
lens.sort()
print("n=%d min=%d max=%d 中位=%d" % (len(lens), lens[0], lens[-1], lens[len(lens)//2]))
print("超 160 的:", [(os.path.basename(f), len(get_desc_en(f) or "")) for f in allf if len(get_desc_en(f) or "") > 160])
