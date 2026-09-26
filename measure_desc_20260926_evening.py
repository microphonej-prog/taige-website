#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""对比既有文章 desc 长度，判断新批次 desc 是否符合本站惯例。"""
import re

FILES = ["blog/trim-third-party-testing-guide.html",
         "blog/sample-room-trims-checklist.html",
         "blog/knitwear-sweater-trims-guide.html",
         "blog/garment-trims-quality-inspection.html",
         "blog/trim-tooling-ownership-guide.html",
         "blog/trim-limit-sample-inspection-guide.html"]

for f in FILES:
    s = open(f, encoding="utf-8").read()
    m = re.search(r'<meta name="description"[^>]*data-zh="([^"]*)"', s)
    c = re.search(r'<meta name="description"[^>]*content="([^"]*)"', s)
    print("%-46s data-zh=%3d 字  content=%3d 字符"
          % (f.split("/")[-1], len(m.group(1)) if m else -1, len(c.group(1)) if c else -1))
