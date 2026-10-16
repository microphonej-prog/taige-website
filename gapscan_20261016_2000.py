#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-16 20:00 批次选题缺口扫描：统计候选主题关键词在全站文章中的命中数。
只读，不改文件。用法: F:/hermes/venvs/tools/Scripts/python.exe gapscan_20261016_2000.py
"""
import os, re, glob, sys, io

ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)

# 收集语料：中文根目录 blog/*.html + en/blog/*.html
files = sorted(glob.glob("blog/*.html")) + sorted(glob.glob("en/blog/*.html"))
files = [f for f in files if not os.path.basename(f).startswith("_")]
corpus = {}
for f in files:
    corpus[f] = open(f, encoding="utf-8").read()
print("语料文件数:", len(corpus))
print()

CAND = [
    ("对色光源/灯箱/色差判定", ["灯箱", "对色光源", "light box", "light booth", "D65", "D50", "色差仪", "spectrophotometer"]),
    ("交货延误/催单/加急", ["催单", "逾期交货", "交货延误", "加急", "expedite", "overdue delivery", "delay penalty", "延误赔偿"]),
    ("拉力与牢固度测试", ["拉力测试", "剥离强度", "pull test", "tensile", "牢固度测试", "attachment strength", "拉脱"]),
    ("原料涨价/价格调整机制", ["原材料涨价", "价格调整机制", "price adjustment", "surcharge", "汇率波动", "raw material price"]),
    ("更换供应商/转厂过渡", ["更换供应商", "转厂", "supplier switch", "supplier transition", "切换供应商", "第二供应商", "dual source"]),
    ("分码分色包装/预包装", ["分码包装", "分色包装", "预包装", "pre-pack", "polybag per size", "单件包装", "成套包装"]),
    ("辅料孔径与挂孔", ["孔径", "挂孔", "hole size", "holediameter", "孔距", "打孔尺寸"]),
    ("货物运输保险", ["货物保险", "cargo insurance", "运输保险", "保价"]),
    ("价格谈判/议价", ["价格谈判", "议价", "negotiation", "降价", "cost breakdown", "成本拆解"]),
    ("针距与缝制强度", ["针距", "stitch density", "缝制强度", "seam strength", "缝线密度", "每英寸针"]),
    ("甲醛与pH值检测", ["甲醛", "formaldehyde", "pH值", "pH value", "异味检测"]),
    ("辅料水洗测试", ["水洗测试", "wash test", "水洗循环", "wash cycle", "家庭洗涤测试"]),
    ("防霉与防潮处理", ["防霉", "anti-mold", "mildew", "防潮剂", "干燥剂", "silica gel"]),
    ("静电与防静电", ["防静电", "anti-static", "ESD", "静电"]),
    ("儿童辅料拉力安全", ["小零件", "small parts", "拉力测试要求", "choking", "锐利边缘", "sharp point"]),
    ("辅料订单变更与改版费", ["改版费", "revision fee", "订单变更", "order change", "改单"]),
    ("库存呆滞与尾货处理", ["呆滞", "尾货", "obsolete stock", "excess stock", "余料处理"]),
    ("辅料的运输时效与门到门", ["门到门", "door to door", "运输时效", "transit time", "海运时效"]),
    ("辅料报价单结构解读", ["报价单", "quotation", "价格构成", "unit price breakdown", "分项报价"]),
    ("供应商产能与排产", ["产能", "capacity", "排产", "production schedule", "旺季排期"]),
]

for name, kws in CAND:
    hits = {k: 0 for k in kws}
    for txt in corpus.values():
        low = txt.lower()
        for k in kws:
            hits[k] += low.count(k.lower())
    total = sum(hits.values())
    detail = ", ".join("%s=%d" % (k, v) for k, v in hits.items() if v)
    print("%-24s 合计 %5d   %s" % (name, total, detail if detail else "(全站零命中)"))
