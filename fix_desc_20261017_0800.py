#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""修正第二篇 desc_en 长度至 150–160 字符（六语文件中同步替换）"""
import os, glob

ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)

OLD = "Recyclable garment packaging is judged by material and local collection, not by a claim: four design levers, bag format comparisons, recycling label schemes and PPWR preparation."
NEW = "Recyclable packaging is judged by material and local collection, not by a claim: four design levers, bag format comparisons, recycling labels and EU PPWR."

slug = "apparel-packaging-recyclability-guide.html"
files = ["blog/" + slug, "en/blog/" + slug, "ja/blog/" + slug,
         "ko/blog/" + slug, "fr/blog/" + slug, "es/blog/" + slug]

print("NEW desc_en 长度 = %d 字符" % len(NEW))
assert 150 <= len(NEW) <= 160, "desc_en 不在 150-160"

hit = 0
for f in files:
    s = open(f, encoding="utf-8").read()
    n = s.count(OLD)
    hit += n
    if n:
        open(f, "w", encoding="utf-8", newline="").write(s.replace(OLD, NEW))
    print("  %-62s 替换 %d 处" % (f, n))
assert hit >= 2, "替换点少于 2，检查原文"
print("合计替换 %d 处" % hit)

# 同步源元数据文件，便于其他脚本复用
mp = "daily_meta_20261017_0800.py"
m = open(mp, encoding="utf-8").read()
assert OLD in m
open(mp, "w", encoding="utf-8", newline="").write(m.replace(OLD, NEW))
print("daily_meta_20261017_0800.py 已同步")
