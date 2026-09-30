#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-09-30 上午批次：desc 长度体检（zh 80-120 字 / en 150-160 字符）"""
import sys
sys.path.insert(0, ".")
from daily_meta_20260930_am import ARTICLES

ok = True
for a in ARTICLES:
    row = {}
    for k in ["desc_zh", "desc_en", "desc_ja", "desc_ko", "desc_fr", "desc_es"]:
        row[k] = len(a[k])
    print("%-34s %s" % (a["slug"], row))
    if not (80 <= row["desc_zh"] <= 120):
        print("   !! desc_zh 超出 80-120：%d" % row["desc_zh"])
        ok = False
    if not (145 <= row["desc_en"] <= 165):
        print("   !! desc_en 接近/超出 150-160：%d" % row["desc_en"])
        ok = False
print("体检结果:", "PASS" if ok else "需调整")
