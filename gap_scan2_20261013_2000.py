#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""第二轮精确扫描：换标/改标服务 & 二手转售服装 两条候选线索的空白确认"""
import glob, os, collections

ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)

files = sorted(glob.glob("blog/**/*.html", recursive=True))
KWS = ["换标服务", "改标服务", "重贴", "标签替换", "替换标签", "返工", "贴标服务",
       "库存成衣", "成品换标", "折扣渠道", "过季库存", "吊牌替换", "补贴标",
       "二手服装", "二手衣", "旧衣", "翻新", "再售", "转卖", "寄卖", "闲鱼",
       "resale platform", "second-hand", "secondhand", "Vinted", "Depop", "ThredUp",
       "circular fashion", "服装回收", "以旧换新", "单次穿着"]
cnt = collections.Counter()
where = collections.defaultdict(list)
for f in files:
    s = open(f, encoding="utf-8").read()
    for k in KWS:
        n = s.count(k)
        if n:
            cnt[k] += n
            where[k].append((f.replace("\\", "/"), n))

for k in KWS:
    lst = sorted(where[k], key=lambda x: -x[1])
    print("== %-16s %-4d %s" % (k, cnt[k], " | ".join("%s:%d" % (a, b) for a, b in lst[:4])))
