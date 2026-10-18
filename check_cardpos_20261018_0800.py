#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""确认 blog/index.html 顶部 3 张卡片的顺序与内容。"""
import re

s = open("blog/index.html", encoding="utf-8").read()
grid = s[s.index('<div class="post-grid">'):]
cards = re.findall(r'<article class="post-card">(.*?)</article>', grid, re.S)[:3]
for i, c in enumerate(cards, 1):
    h3 = re.search(r"<h3[^>]*>(.*?)</h3>", c, re.S).group(1)
    href = re.search(r'class="more" href="([^"]*)"', c).group(1)
    tag = re.search(r'<span class="tag"[^>]*>(.*?)</span>', c, re.S).group(1)
    print("%d. [%s] %s  -> %s" % (i, tag, h3, href))
