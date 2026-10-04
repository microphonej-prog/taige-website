#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""desc 长度体检：zh 汉字数（目标 80-120）、en/fr/es 字符数（en 目标 150-160）、ja/ko 字符数。"""
import re
from daily_meta_20261004_1400 import ARTICLES

for a in ARTICLES:
    zh = a["desc_zh"]
    han = len(re.findall(r"[\u4e00-\u9fff]", zh))
    print("--- %s" % a["slug"])
    print("  zh 汉字=%d 总长=%d :: %s" % (han, len(zh), zh))
    for lg in ("en", "ja", "ko", "fr", "es"):
        v = a["desc_%s" % lg]
        print("  %-3s len=%3d :: %s" % (lg, len(v), v))
    for f in ("title_zh", "title_en", "h1_zh", "h1_en", "sum_zh"):
        v = a[f]
        print("  %-9s len=%3d" % (f, len(v)))
