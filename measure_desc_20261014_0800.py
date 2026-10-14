#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""测量 desc 长度（对照既有文章 + 本次新增）。"""
import os, re, io

ROOT = os.path.dirname(os.path.abspath(__file__))
FILES = ["neckwear-trims-label-guide.html", "belts-suspenders-trims-guide.html",
         "apparel-relabeling-service-guide.html", "secondhand-resale-apparel-label-guide.html",
         "apron-trims-label-guide.html", "clothing-label-compliance-netherlands.html",
         "clothing-label-compliance-argentina.html", "uniform-workwear-labeling-guide.html"]


def desc(s):
    m = re.search(r'<meta name="description"(.*?)>', s, re.S)
    seg = m.group(1)
    out = {}
    for k in ("content", "data-zh", "data-en", "data-fr", "data-es", "data-ja", "data-ko"):
        mm = re.search(r'%s="([^"]*)"' % k, seg)
        out[k] = mm.group(1) if mm else ""
    return out


for f in FILES:
    p = os.path.join(ROOT, "blog", f)
    if not os.path.exists(p):
        print("缺文件", f)
        continue
    d = desc(io.open(p, encoding="utf-8").read())
    print("%-46s zh=%3d en=%3d fr=%3d es=%3d ja=%3d ko=%3d"
          % (f, len(d["content"]), len(d["data-en"]), len(d["data-fr"]),
             len(d["data-es"]), len(d["data-ja"]), len(d["data-ko"])))
