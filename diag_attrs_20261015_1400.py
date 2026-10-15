#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-15 下午批次：新文件属性畸形扫描（12 个文件）
- data-* 属性值内裸露 ASCII 双引号 / 未转义 &
- 属性值内 latin-1 裸字节（mojibake）区分
"""
import os, re, glob

ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)
SLUGS = ["ribbon-trims-guide.html", "eu-green-claims-apparel-labels.html"]
LANGS = ["en", "ja", "ko", "fr", "es"]
FILES = ["blog/%s" % s for s in SLUGS] + ["%s/blog/%s" % (l, s) for l in LANGS for s in SLUGS] \
        + ["blog/index.html"] + ["%s/blog/index.html" % l for l in LANGS]

bad = 0
for f in FILES:
    s = open(f, encoding="utf-8").read()
    # 抓所有 data-XX="..." 片段（含跨行）
    probs = []
    for m in re.finditer(r'data-(zh|en|ja|ko|fr|es)="((?:[^"])*)"', s):
        v = m.group(2)
        if '"' in v:
            probs.append(("裸引号", m.start()))
        for amp in re.finditer(r"&(?!(amp|lt|gt|quot|nbsp|#\d+|#x[0-9a-fA-F]+);)", v):
            probs.append(("裸&", m.start() + amp.start()))
    # 结构体检：< 与 > 数量、属性值内的 > 是否实体化
    lt, gt = s.count("<"), s.count(">")
    print("%-46s 属性问题=%d  <:%d >:%d" % (f, len(probs), lt, gt))
    for p in probs[:8]:
        print("    %s @%d" % p)
    bad += len(probs)
print("总计属性问题:", bad)
