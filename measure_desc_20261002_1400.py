#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-02 下午批次：desc/title 长度体检 + 非中文语种汉字残留检查"""
import re, sys
sys.path.insert(0, ".")
from daily_meta_20261002_1400 import ARTICLES

LANGS = ["en", "ja", "ko", "fr", "es"]
bad = 0
for a in ARTICLES:
    print("== %s ==" % a["slug"])
    print("  desc_zh %d 字（目标 80-120）" % len(a["desc_zh"]))
    print("  desc_en %d 字符（目标 150-160）" % len(a["desc_en"]))
    for l in ["ja", "ko", "fr", "es"]:
        print("  desc_%s %d 字符" % (l, len(a["desc_" + l])))
    for l in LANGS:
        for k in ("title_", "desc_", "h1_", "sum_", "crumb_", "tag_"):
            v = a.get(k + l, "")
            if l in ("en", "fr", "es", "ko") and re.search(r"[\u4e00-\u9fff]", v):
                print("  !! %s%s 含汉字残留: %s" % (k, l, v[:60]))
                bad += 1
    for k in ("title_zh", "desc_zh", "h1_zh", "crumb_zh", "sum_zh", "tag_zh"):
        if not a.get(k):
            print("  !! 缺 %s" % k)
            bad += 1
    if not (80 <= len(a["desc_zh"]) <= 120):
        print("  !! desc_zh 超出 80-120")
    if not (140 <= len(a["desc_en"]) <= 165):
        print("  ! desc_en 长度偏离 150-160（%d）" % len(a["desc_en"]))
print("\n汉字残留/缺字段问题数 = %d" % bad)
sys.exit(1 if bad else 0)
