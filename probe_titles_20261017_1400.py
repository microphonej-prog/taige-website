# -*- coding: utf-8 -*-
"""列出 blog/ 现有文章的 h1 中文标题，用于选题去重判断"""
import os, re, glob

files = sorted(glob.glob("blog/*.html"))
rows = []
for f in files:
    if os.path.basename(f).startswith("_body_"):
        continue
    s = open(f, encoding="utf-8").read()
    m = re.search(r'<h1[^>]*data-zh="([^"]*)"', s)
    t = m.group(1) if m else "(no h1)"
    rows.append((os.path.basename(f), t))

print("文章总数:", len(rows))
for n, t in rows:
    print("%-50s %s" % (n, t))
