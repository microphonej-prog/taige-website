#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""检查 2026-09-30 下午批次元数据的 desc / sum 长度是否落在目标区间。"""
import sys
sys.path.insert(0, ".")
from daily_meta_20260930_pm import ARTICLES

for a in ARTICLES:
    print(a["slug"])
    for k in ("desc_zh", "desc_en", "desc_ja", "desc_ko", "desc_fr", "desc_es"):
        n = len(a[k])
        flag = ""
        if k == "desc_zh" and not (80 <= n <= 125):
            flag = "  <-- 期望 80-120 字"
        if k == "desc_en" and not (145 <= n <= 165):
            flag = "  <-- 期望 150-160 字符"
        if k in ("desc_ja", "desc_ko", "desc_fr", "desc_es") and not (100 <= n <= 200):
            flag = "  <-- 期望 100-200"
        print("   %-8s %3d%s" % (k, n, flag))
    for k in ("sum_zh", "sum_en", "sum_ja", "sum_ko", "sum_fr", "sum_es"):
        print("   %-8s %3d" % (k, len(a[k])))
    for k in ("title_zh", "title_en", "title_ja", "title_ko", "title_fr", "title_es"):
        if '"' in a[k]:
            print("   !! 标题含裸双引号: %s" % k)
