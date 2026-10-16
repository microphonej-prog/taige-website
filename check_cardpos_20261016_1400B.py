#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""确认 blog/index.html 顶部两张新卡片的实际位置与顺序。"""
import re
p = "blog/index.html"
s = open(p, encoding="utf-8").read()
grid_start = s.index('<div class="post-grid">')
cards = [(m.start(), m.group(1)) for m in re.finditer(r'<article class="post-card">.*?href="([^"]+)"', s[grid_start:], re.S)]
print("post-grid 起始偏移 %d，卡片总数 %d" % (grid_start, len(cards)))
for i, (off, href) in enumerate(cards[:4]):
    print("  第 %d 张 (偏移 %d): %s" % (i + 1, grid_start + off, href))
