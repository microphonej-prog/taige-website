#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""选题空白扫描：候选关键词在全站正文(_body_*.html + blog/*.html)中的出现次数与分布"""
import glob, os, re, collections

ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)

files = sorted(glob.glob("blog/_body_*.html")) + sorted(glob.glob("blog/[a-z]*.html"))
KWS = [
    "换标", "改标", "重新贴标", "返修", "re-label", "relabel", "private label",
    "BOM", "物料清单", "用量核算", "单件用量", "排版用量",
    "二手", "转售", "租赁", "寄卖", "resale", "rental", "vintage", "循环时尚",
    "同色异谱", "metamerism", "DE值", "色差",
    "可降解", "可堆肥", "生物基", "PBAT", "PLA", "compostable",
    "拉力", "剥离", "附着强力", "pull test", "张力",
    "产能", "排产", "旺季", "插单",
    "GS1", "GTIN", "SSCC",
    "湿度", "盐雾", "耐磨"
]
res = collections.OrderedDict((k, []) for k in KWS)
tot = collections.Counter()
for f in files:
    try:
        s = open(f, encoding="utf-8").read()
    except Exception as e:
        print("skip", f, e)
        continue
    txt = s
    for k in KWS:
        n = txt.count(k)
        if n:
            res[k].append((os.path.basename(f), n))
            tot[k] += n

for k in KWS:
    lst = sorted(res[k], key=lambda x: -x[1])
    print("== %-12s 总计 %-4d 涉及 %d 个文件" % (k, tot[k], len(lst)))
    for name, n in lst[:6]:
        print("      %-52s %d" % (name, n))
