#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-16 20:00 批次缺口扫描（修正版）：中文关键词同时统计简体与繁体两种写法。
用法: F:/hermes/venvs/tools/Scripts/python.exe gapscan3_20261016_2000.py
"""
import os, glob, opencc

ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)
s2t = opencc.OpenCC("s2t")

files = sorted(glob.glob("blog/*.html")) + sorted(glob.glob("en/blog/*.html")) \
        + sorted(glob.glob("ja/blog/*.html")) + sorted(glob.glob("ko/blog/*.html")) \
        + sorted(glob.glob("fr/blog/*.html")) + sorted(glob.glob("es/blog/*.html"))
files = [f for f in files if not os.path.basename(f).startswith("_")]
corpus = [open(f, encoding="utf-8").read() for f in files]
print("语料文件数:", len(corpus), "  (全站六语 blog 目录)")
print()

CAND = [
    ("原产地规则与实质性改变", ["原产地规则", "实质性改变", "substantial transformation", "区域价值成分", "税则归类改变", "rules of origin"]),
    ("CBAM 碳边境机制", ["CBAM", "碳边境", "carbon border", "嵌入碳排放", "碳关税"]),
    ("冲突矿产与尽责调查", ["冲突矿产", "conflict mineral", "3TG", "CMRT", "冶炼厂", "smelter", "OECD"]),
    ("辅料运输保险与货损索赔", ["货物保险", "cargo insurance", "海运保险", "一切险", "all risks", "货损", "理赔", "survey report"]),
    ("辅料供应商更换与过渡", ["更换供应商", "转厂", "supplier switch", "supplier transition", "并行期", "双轨期"]),
    ("辅料出口退税与税务", ["出口退税", "tax rebate", "VAT refund", "增值税发票"]),
    ("打样费与样品费规则", ["打样费", "样品费", "sample fee", "免费打样", "打样收费"]),
    ("辅料的包装规格与分装", ["分装", "分码", "分色包装", "pre-pack", "预包装", "单件包装"]),
    ("辅料的技术规格书", ["规格书", "spec sheet", "技术图纸", "tech pack"]),
    ("辅料的报价有效期", ["报价有效期", "quotation validity", "价格锁定", "价格调整"]),
    ("交货延误与催单", ["催单", "逾期交货", "交货延误", "逾期", "expedite", "overdue", "delay"]),
    ("印刷套准与色差允差", ["套准", "套印", "misregistration", "registration", "色差允差", "色差仪"]),
    ("耐摩擦与汗渍色牢度", ["摩擦色牢度", "crocking", "rubbing fastness", "汗渍色牢度", "perspiration", "唾液色牢度"]),
    ("辅料手感与柔软度", ["手感", "hand feel", "柔软度"]),
    ("木质与竹制辅料检疫", ["熏蒸", "fumigation", "ISPM", "植物检疫", "木质包装"]),
    ("辅料的防霉防潮", ["防霉", "anti-mold", "mildew", "防潮剂", "干燥剂", "silica gel", "霉斑"]),
    ("辅料供应商产能与旺季", ["产能", "capacity", "旺季排期", "peak season"]),
    ("金属辅料的镍释放与过敏", ["镍释放", "nickel release", "过敏", "allergy"]),
    ("辅料增值税与发票", ["增值税", "invoice", "发票"]),
    ("辅料的检验报告与测试", ["检测报告", "test report", "第三方检测", "third-party test"]),
]

for name, kws in CAND:
    hits = {}
    for k in kws:
        variants = {k}
        try:
            variants.add(s2t.convert(k))
        except Exception:
            pass
        c = sum(t.lower().count(v.lower()) for t in corpus for v in variants)
        if c:
            hits[k] = c
    total = sum(hits.values())
    detail = ", ".join("%s=%d" % (k, v) for k, v in hits.items())
    print("%-26s 合计 %5d   %s" % (name, total, detail if detail else "(全站零命中)"))
