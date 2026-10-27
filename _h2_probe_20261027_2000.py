# -*- coding: utf-8 -*-
"""打印指定 blog 文章的 h2 标题（用于选题去重判断）"""
import re, sys, io, os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
files = sys.argv[1:]
for f in files:
    if not os.path.exists(f):
        print("!! 缺文件", f); continue
    s = open(f, encoding="utf-8").read()
    hs = re.findall(r'<h2[^>]*data-zh="([^"]*)"', s)
    if not hs:
        hs = re.findall(r'<h2[^>]*>(.*?)</h2>', s, re.S)
        hs = [re.sub(r'<[^>]+>', '', h).strip() for h in hs]
    print("=== %s (%d h2)" % (f, len(hs)))
    for h in hs[:14]:
        print("   -", h[:70])
