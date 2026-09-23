#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""确认 6 个 blog/index.html 里新卡片排在最前两位"""
import re

FILES = ["blog/index.html"] + ["%s/blog/index.html" % l for l in ("en", "ja", "ko", "fr", "es")]
NEW = ["pet-apparel-trims-guide.html", "loungewear-pajama-trims-guide.html"]
for p in FILES:
    t = open(p, encoding="utf-8").read()
    grid = t.split('<div class="post-grid">')[1]
    order = re.findall(r'<a class="more" href="([^"]+)"', grid)
    print("%-24s 卡片总数=%d 前两张=%s" % (p, len(order), order[:2]))
    assert order[:2] == NEW, "顺序不符: %s" % order[:2]
print("全部 6 个列表页新卡片均在最前两位 ✓")
