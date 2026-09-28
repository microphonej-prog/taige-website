#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-09-28 晚间批次：新页面内部链接可解析性检查（含本地文件是否存在）。"""
import re, os, glob

NEW = ["blog/garment-trims-freight-mode-guide.html",
       "blog/trim-order-quantity-tolerance-guide.html",
       "blog/index.html"]
bad = 0
for f in NEW:
    d = os.path.dirname(f)
    s = open(f, encoding="utf-8").read()
    hrefs = set(re.findall(r'href="([^"#]+)"', s))
    miss = []
    for h in sorted(hrefs):
        if h.startswith(("http", "mailto:", "tel:", "javascript:", "data:")):
            continue
        p = os.path.normpath(os.path.join(d, h.split("?")[0]))
        if not os.path.exists(p):
            miss.append(h)
    bad += len(miss)
    print("%-46s 链接 %3d 个，缺失 %d %s" % (f, len(hrefs), len(miss), miss))

# 生成的语言页也走一遍
for lang in ("en", "ja", "ko", "fr", "es"):
    for f in NEW:
        p = os.path.join(lang, f)
        d = os.path.dirname(p)
        s = open(p, encoding="utf-8").read()
        hrefs = [h for h in set(re.findall(r'href="([^"#]+)"', s))
                 if not h.startswith(("http", "mailto:", "tel:", "javascript:", "data:"))]
        miss = [h for h in hrefs if not os.path.exists(os.path.normpath(os.path.join(d, h.split("?")[0])))]
        bad += len(miss)
        if miss:
            print("%-52s 缺失 %s" % (p, miss))
print("\n结论: 缺失链接总数 = %d" % bad)
raise SystemExit(1 if bad else 0)
