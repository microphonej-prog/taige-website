#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""量 2026-10-06 上午批次 desc / sum 长度。"""
from daily_meta_20261006_am import ARTICLES

for a in ARTICLES:
    print(a["slug"])
    for k in ("desc_zh", "desc_en", "desc_ja", "desc_ko", "desc_fr", "desc_es"):
        print("   %-8s %3d" % (k, len(a[k])))
    for k in ("sum_zh", "sum_en", "sum_ja", "sum_ko", "sum_fr", "sum_es"):
        print("   %-8s %3d" % (k, len(a[k])))
