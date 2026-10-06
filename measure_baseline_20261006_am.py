#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""量最近几篇上线文章静态 meta description / sum 的长度，作为本批次长度基准。"""
import re, glob, os

files = ["blog/reach-svhc-apparel-trims-guide.html",
         "blog/braille-tactile-label-guide.html",
         "blog/sewing-thread-selection-guide.html",
         "blog/flame-retardant-trims-guide.html",
         "blog/knitwear-sweater-trims-guide.html"]
for f in files:
    if not os.path.exists(f):
        print("missing", f)
        continue
    s = open(f, encoding="utf-8").read()
    m = re.search(r'<meta name="description"[^>]*?content="([^"]*)"', s, re.S)
    t = re.search(r'<title[^>]*>(.*?)</title>', s, re.S).group(1)
    print("%-46s desc=%3d title=%d" % (os.path.basename(f), len(m.group(1)) if m else -1, len(t)))

# 列表卡片摘要长度（最近两张卡）
s = open("blog/index.html", encoding="utf-8").read()
cards = re.findall(r'<article class="post-card">(.*?)</article>', s, re.S)[:3]
for c in cards:
    d = re.search(r'<p data-zh="([^"]*)"', c)
    de = re.search(r'data-en="([^"]*)"', c)
    print("card sum_zh=%d sum_en=%d" % (len(d.group(1)) if d else -1, len(de.group(1)) if de else -1))
