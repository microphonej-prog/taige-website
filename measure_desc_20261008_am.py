#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""量一量最近若干篇线上文章的 desc_zh / desc_en 长度，确认站内既有口径"""
import os, re, glob

ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)

files = sorted(glob.glob("blog/*.html"), key=os.path.getmtime, reverse=True)[:12]
for p in files:
    if p.endswith("blog/index.html"):
        continue
    s = open(p, encoding="utf-8").read()
    m = re.search(r'<meta name="description"[^>]*data-zh="([^"]*)"', s, re.S)
    e = re.search(r'<meta name="description"[^>]*data-en="([^"]*)"', s, re.S)
    print("%-46s zh=%3d en=%3d" % (os.path.basename(p),
                                   len(m.group(1)) if m else -1,
                                   len(e.group(1)) if e else -1))
