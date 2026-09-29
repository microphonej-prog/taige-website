#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-09-29 晚间批次：两篇新文章（六语共 12 个页面）内部链接落盘校验。"""
import os, re, sys

os.chdir(os.path.dirname(os.path.abspath(__file__)))
SLUGS = ["woven-label-shrinkage-guide.html", "trim-measurement-tolerance-guide.html"]
LANGS = [("zh", "blog"), ("en", "en/blog"), ("ja", "ja/blog"), ("ko", "ko/blog"),
         ("fr", "fr/blog"), ("es", "es/blog")]
bad = 0
for lang, d in LANGS:
    for slug in SLUGS:
        p = os.path.join(d, slug)
        s = open(p, encoding="utf-8", newline="").read()
        links = []
        for L in re.findall(r'(?:href|data-bg)="([^"#?]+)"', s):
            links.extend([x.strip() for x in L.split(",") if x.strip()])
        miss = []
        for L in links:
            if L.startswith(("http", "mailto", "tel", "data:")):
                continue
            target = os.path.normpath(os.path.join(d, L))
            if not os.path.exists(target):
                miss.append(L)
        print("%-2s %-40s 链接 %2d 个，缺失 %d %s" % (lang, slug, len(links), len(miss), miss[:4]))
        if miss:
            bad += 1
print("\n结论：", "全部链接有效" if bad == 0 else "%d 个页面有断链" % bad)
sys.exit(1 if bad else 0)
