#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""统计全站 blog 文章里每个 <table> 的列数分布，判断 5 列表格是否有先例；
并检查正文表格单元格里最长的不可断词长度（移动端列宽风险的来源）。"""
import os, re, glob, collections

os.chdir(os.path.dirname(os.path.abspath(__file__)))

dist = collections.Counter()
examples = {}
maxword = (0, "", "")
files = sorted(glob.glob("blog/*.html")) + sorted(glob.glob("en/blog/*.html"))
for f in files:
    if "_body_" in f:
        continue
    s = open(f, encoding="utf-8").read()
    for m in re.finditer(r"<table>(.*?)</table>", s, re.S):
        tbl = m.group(1)
        nth = tbl.count("<th") or tbl.split("</tr>")[0].count("<td")
        dist[nth] += 1
        examples.setdefault(nth, os.path.basename(f))
        for cell in re.findall(r"<(?:th|td)([^>]*)>", tbl):
            for v in re.findall(r'="([^"]*)"', cell):
                for w in re.split(r"[\s,;:，、；：（）()\[\]/]+", v):
                    if len(w) > maxword[0]:
                        maxword = (len(w), w, os.path.basename(f))
print("列数分布（列数: 表数量）：")
for k in sorted(dist):
    print("  %d 列 : %d 个表  例：%s" % (k, dist[k], examples[k]))
print("\n最长不可断词: %d 字符  %r  出自 %s" % maxword)

print("\n本批次两个新文件的表格列数：")
for f in ["blog/vacuum-compression-apparel-packaging.html", "blog/stone-paper-hang-tags-guide.html",
          "fr/blog/vacuum-compression-apparel-packaging.html", "es/blog/vacuum-compression-apparel-packaging.html"]:
    s = open(f, encoding="utf-8").read()
    cols = [m.group(1).count("<th") for m in re.finditer(r"<table>(.*?)</table>", s, re.S)]
    print("  %-56s %s" % (f, cols))
