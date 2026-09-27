#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-09-27 上午批次：desc 长度体检（中文 80-120 字 / 英文 150-160 字符）。"""
from daily_meta_20260927_am import ARTICLES

for a in ARTICLES:
    print(a["slug"])
    for k in ("desc_zh", "desc_en", "desc_ja", "desc_ko", "desc_fr", "desc_es",
              "title_zh", "title_en", "h1_zh", "sum_zh"):
        print("   %-9s %d" % (k, len(a[k])))
    ok_en = 150 <= len(a["desc_en"]) <= 160
    ok_zh = 80 <= len(a["desc_zh"]) <= 120
    print("   desc_zh 合规=%s  desc_en 合规=%s" % (ok_zh, ok_en))
