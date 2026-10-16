#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""候选选题与既有近似文章的重复风险检查（只读）。
用法: F:/hermes/venvs/tools/Scripts/python.exe overlap_20261016_2000.py
"""
import os, re, glob, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)

NEAR = {
    "supplier-switch": ["blog/trim-supply-continuity-guide.html",
                        "blog/garment-trims-sourcing-guide.html",
                        "blog/trim-supplier-scorecard-guide.html",
                        "blog/garment-trims-supplier-audit.html",
                        "blog/small-batch-fast-reorder-trims.html"],
    "cargo-insurance": ["blog/garment-trims-freight-mode-guide.html",
                        "blog/garment-trims-sample-shipping-guide.html",
                        "blog/apparel-trims-payment-terms-guide.html",
                        "blog/trim-order-contract-terms-guide.html",
                        "blog/garment-trims-carton-loading-guide.html"],
    "obsolete-stock":  ["blog/garment-trims-inventory-management.html",
                        "blog/trim-order-change-cancellation-guide.html",
                        "blog/trim-vmi-consignment-stock-guide.html",
                        "blog/trim-tooling-ownership-guide.html"],
}
KW = {
    "supplier-switch": ["更换供应商", "转厂", "第二供应商", "备选供应商", "切换", "过渡", "parallel", "second source", "dual source", "switch"],
    "cargo-insurance": ["保险", "货损", "索赔", "理赔", "风险转移", "Incoterms", "insurance", "claim", "risk transfer"],
    "obsolete-stock":  ["呆滞", "尾货", "余料", "报废", "清理", "obsolete", "excess", "scrap", "write-off"],
}

for name, files in NEAR.items():
    print("=" * 70)
    print("候选:", name)
    print("=" * 70)
    for f in files:
        if not os.path.exists(f):
            print("  [缺失]", f)
            continue
        s = open(f, encoding="utf-8").read()
        # 提取 h1 + h2 列表
        hs = re.findall(r'<h[12][^>]*data-zh="([^"]{0,70})"', s)
        hits = {k: s.lower().count(k.lower()) for k in KW[name] if s.lower().count(k.lower())}
        print("  %s  (h2 数 %d)" % (os.path.basename(f), len(hs)))
        for h in hs[:14]:
            print("       · %s" % h)
        if hits:
            print("       关键词命中:", hits)
        rest = hs[14:]
        if rest:
            print("       ...另 %d 个小节" % len(rest))
    print()
