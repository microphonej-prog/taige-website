#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""窄口径简体字检查：只含确属简体、非日文汉字的字符"""
import re
NARROW = "设计缝标签务难应图过这个时关键认语护纸张线记录备边处板样顺试检运质量颜构势变险额编码设备项类别级贴"
for f in ["blog/adaptive-accessible-clothing-trims-guide.html",
          "blog/modest-wear-hijab-trims-guide.html"]:
    s = open(f, encoding="utf-8").read()
    print("=== %s ===" % f)
    for lang in ("ja", "ko", "fr", "es"):
        hit = {}
        for v in re.findall(r'data-%s="([^"]*)"' % lang, s):
            for ch in v:
                if ch in NARROW:
                    hit[ch] = hit.get(ch, 0) + 1
        print("  %s: %s" % (lang, hit or "干净"))
