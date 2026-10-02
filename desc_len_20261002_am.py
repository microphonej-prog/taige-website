#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-02 早上批次：desc/title 长度体检（不写盘）"""
import sys
sys.path.insert(0, ".")
from daily_meta_20261002_am import ARTICLES

for a in ARTICLES:
    print(a["slug"])
    for k, lo, hi in (("desc_zh", 80, 120), ("desc_en", 150, 160)):
        n = len(a[k])
        flag = "OK " if lo <= n <= hi else "!! "
        print("   %s %s len=%d (目标 %d-%d)" % (flag, k, n, lo, hi))
    for k in ("desc_ja", "desc_ko", "desc_fr", "desc_es"):
        print("      %s len=%d" % (k, len(a[k])))
    for k in ("title_zh", "title_en", "title_ja", "title_ko", "title_fr", "title_es",
              "h1_zh", "crumb_zh", "sum_zh", "tag_zh"):
        print("      %s len=%d" % (k, len(a[k])))
