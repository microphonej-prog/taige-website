#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-16 20:00 批次第二组候选选题缺口扫描（只读）。"""
import os, glob

ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)

files = sorted(glob.glob("blog/*.html")) + sorted(glob.glob("en/blog/*.html"))
files = [f for f in files if not os.path.basename(f).startswith("_")]
corpus = [open(f, encoding="utf-8").read() for f in files]
print("语料文件数:", len(corpus))
print()

CAND = [
    ("原产地证与优惠协定", ["原产地证", "certificate of origin", "FORM A", "FORM E", "RCEP", "普惠制", "自贸协定", "自贸区优惠"]),
    ("原产地规则与实质性改变", ["实质性改变", "substantial transformation", "税则归类改变", "区域价值成分", "原产地规则"]),
    ("冲突矿产与金属辅料尽责", ["冲突矿产", "conflict mineral", "3TG", "CMRT", "OECD 尽责", "due diligence", "冶炼厂清单"]),
    ("CBAM 碳边境机制", ["CBAM", "碳边境", "carbon border", "嵌入碳排放", "碳关税"]),
    ("森林认证与 FSC", ["FSC", "森林认证", "forest certification", "PEFC", "监管链", "chain of custody"]),
    ("回收含量与 GRS 认证", ["GRS", "全球回收标准", "recycled content", "回收含量", "消费后回收", "PCR"]),
    ("大豆油墨与水性油墨", ["大豆油墨", "soy ink", "水性油墨", "water-based ink", "溶剂型油墨", "solvent-based", "UV油墨"]),
    ("可降解与生物基材料", ["生物基", "bio-based", "可降解", "biodegradable", "可堆肥", "compostable", "PLA"]),
    ("耐摩擦色牢度", ["摩擦色牢度", "crocking", "干湿摩擦", "rubbing fastness", "耐磨测试", "abrasion"]),
    ("汗渍与唾液色牢度", ["汗渍色牢度", "perspiration", "唾液", "saliva", "耐汗"]),
    ("印刷套准与色差允差", ["套准", "套印", "registration", "misregistration", "色差允差", "ΔE", "delta E"]),
    ("辅料手感与柔软度", ["手感", "hand feel", "柔软度", "softness", "触感", "handfeel"]),
    ("辅料出口退税与税务", ["出口退税", "出口退稅", "tax rebate", "VAT refund", "增值税发票"]),
    ("辅料的宠物与玩具合规", ["EN 71", "CPSIA", "玩具安全", "toy safety", "ASTM F963"]),
    ("辅料运输保险与货损索赔", ["货物保险", "cargo insurance", "海运保险", "all risks", "一切险", "货损索赔", "survey report", "检验报告"]),
    ("辅料供应商更换与过渡", ["更换供应商", "转厂", "supplier switch", "supplier transition", "并行期", "双轨"]),
    ("打样费与样品费规则", ["打样费", "sample fee", "打样收费", "样品费", "免费打样", "打样费退还"]),
    ("辅料的最小起订量谈判", ["起订量", "MOQ", "最小起订", "起订量与成本"]),
    ("辅料的包装规格与分装", ["分装", "分码", "分色包装", "pre-pack", "预包装", "单件包装"]),
    ("辅料的技术规格书与图纸", ["规格书", "spec sheet", "技术图纸", "tech pack", "工艺单"]),
    ("辅料供应商产能与旺季", ["产能", "满产", "旺季排期", "peak season", "capacity booking"]),
    ("辅料的报价有效期与价格锁定", ["报价有效期", "quotation validity", "价格锁定", "原材料波动", "价格调整"]),
]

for name, kws in CAND:
    hits = {}
    for k in kws:
        c = sum(t.lower().count(k.lower()) for t in corpus)
        if c:
            hits[k] = c
    total = sum(hits.values())
    detail = ", ".join("%s=%d" % (k, v) for k, v in hits.items())
    print("%-26s 合计 %5d   %s" % (name, total, detail if detail else "(全站零命中)"))
