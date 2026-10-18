#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""列出 blog 全部文章的 h1_zh（data-zh 首值）以判断选题覆盖度。"""
import re, glob

rows = []
for p in sorted(glob.glob("blog/*.html")):
    if p.endswith("index.html"):
        continue
    s = open(p, encoding="utf-8").read()
    m = re.search(r'<h1[^>]*data-zh="([^"]*)"', s)
    if not m:
        m = re.search(r'<h1[^>]*>(.*?)</h1>', s, re.S)
        t = re.sub(r"<[^>]+>", "", m.group(1)) if m else "?"
    else:
        t = m.group(1)
    rows.append((p.split("/")[-1], t))

print("total", len(rows))
kws = ["色差", "灰卡", "ΔE", "霉", "自动", "体积", "重量", "运费", "AQL", "抽样",
       "Pantone", "TCX", "条码", "等级", "医护", "工业洗涤", "15797", "清真",
       "可回收", "单一材质", "数码", "激光", "刻字", "吊粒", "扣件", "暗码",
       "价格", "报价", "碳", "毒", "邻苯", "甲醛", "偶氮", "燃烧", "阻燃"]
for k in kws:
    hit = [r for r in rows if k in r[1]]
    print("\n== %s (%d) ==" % (k, len(hit)))
    for f, t in hit[:12]:
        print("   %-52s %s" % (f, t[:60]))
