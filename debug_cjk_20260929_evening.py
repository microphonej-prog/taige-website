#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
s = open("en/blog/woven-label-shrinkage-guide.html", encoding="utf-8", newline="").read()
body = re.sub(r'<script.*?</script>', '', s, flags=re.S)
for m in re.finditer(r'[\u4e00-\u9fff]+', re.sub(r'<[^>]*>', '', body)):
    print("汉字片段:", repr(m.group(0)))
print("--- 上下文 ---")
for m in re.finditer(r'[\u4e00-\u9fff]', body):
    print(repr(body[max(0, m.start() - 90):m.start() + 60]))
    print("  ---")
print("=== zh index 卡片偏移 ===")
idx = open("blog/index.html", encoding="utf-8", newline="").read()
g = idx.find('<div class="post-grid">')
for sl in ["woven-label-shrinkage-guide.html", "trim-measurement-tolerance-guide.html"]:
    print(sl, "位置", idx.find(sl), "相对 grid 起点", idx.find(sl) - g)
