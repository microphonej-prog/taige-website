#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""校验 blog/index.html 顶部两张新卡片是否六语齐全。"""
import re

s = open("blog/index.html", encoding="utf-8").read()
grid = s.index('<div class="post-grid">')
cards = re.findall(r'<article class="post-card">.*?</article>', s[grid:], re.S)[:2]
for c in cards:
    slug = re.search(r'href="([^"]+)"', c).group(1)
    counts = {k: c.count('data-%s="' % k) for k in ("zh", "en", "ja", "ko", "fr", "es")}
    print("%-42s %s" % (slug, counts))
    assert all(v == 4 for v in counts.values()), "卡片语种属性不齐: %s" % counts
print("卡片六语属性齐全")
