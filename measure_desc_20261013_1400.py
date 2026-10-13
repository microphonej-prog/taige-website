# -*- coding: utf-8 -*-
"""体检：desc 长度是否符合规范（zh 80-120 字、en 150-160 字符）"""
import re
from daily_meta_20261013_1400 import ARTICLES

for a in ARTICLES:
    print("-" * 70)
    print(a["slug"])
    for k in ["desc_zh", "desc_en", "desc_ja", "desc_ko", "desc_fr", "desc_es"]:
        v = a[k]
        cjk = len(re.findall(r'[\u4e00-\u9fff]', v))
        print("  %-8s len=%-4d CJK=%-4d %s" % (k, len(v), cjk, v[:60]))
    for k in ["title_zh", "title_en", "h1_zh", "h1_en"]:
        print("  %-8s len=%d" % (k, len(a[k])))
