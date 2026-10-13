#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-13 第三批修正：相关文章链接指向不存在的 garment-trims-spec-sheet-guide.html，
全站实际 slug 为 apparel-trims-spec-sheet-guide.html，六语页面一并修正。"""
import glob

OLD = 'href="garment-trims-spec-sheet-guide.html"'
NEW = 'href="apparel-trims-spec-sheet-guide.html"'
FILES = ["blog/_body_neckwear.html",
         "blog/neckwear-trims-label-guide.html"] + \
        ["%s/blog/neckwear-trims-label-guide.html" % l for l in ("en", "ja", "ko", "fr", "es")]

for f in FILES:
    s = open(f, encoding="utf-8").read()
    n = s.count(OLD)
    if n:
        s = s.replace(OLD, NEW)
        open(f, "w", encoding="utf-8", newline="").write(s)
    print("%-56s 替换 %d 处，残留 %d" % (f, n, s.count(OLD)))
