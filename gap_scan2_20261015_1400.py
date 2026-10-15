#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-15 14:00 批次：候选两个选题的覆盖度细查（按文件定位）"""
import os, glob, re

ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)

KEYS = ["医用", "医疗", "防护服", "PPE", "medical gown", "isolation gown", "医療用", "의료",
        "丝带", "缎带", "grosgrain", "satin ribbon", "ribbon trims"]
print("=== 关键词出现文件（中文根页 blog/*.html，排除 _body_） ===")
files = sorted(glob.glob("blog/*.html"))
for k in KEYS:
    hits = []
    for f in files:
        if os.path.basename(f).startswith("_body_"):
            continue
        s = open(f, encoding="utf-8").read()
        c = s.count(k)
        if c:
            hits.append((c, os.path.basename(f)))
    hits.sort(reverse=True)
    print("%-16s %d 文件: %s" % (k, len(hits), ", ".join("%s(%d)" % (n, c) for c, n in hits[:8])))

print()
print("=== 现有文章 h1 一览（判断选题空间） ===")
for f in files:
    b = os.path.basename(f)
    if b.startswith("_body_") or b == "index.html":
        continue
    s = open(f, encoding="utf-8").read()
    m = re.search(r'<h1[^>]*data-zh="([^"]*)"', s)
    print("%-52s %s" % (b, m.group(1) if m else "?"))
