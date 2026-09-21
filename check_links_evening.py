#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""检查新增文章的站内相对链接是否都有对应文件（根目录页与各语言生成页）。"""
import os, re, sys

NEW = ["blog/clothing-label-compliance-saudi-arabia.html", "blog/clothing-label-compliance-turkey.html"]
LANGS = ["en", "ja", "ko", "fr", "es"]
bad = 0
for f in NEW:
    for path in [f] + [os.path.join(l, f) for l in LANGS]:
        s = open(path, encoding="utf-8").read()
        d = os.path.dirname(path)
        hrefs = re.findall(r'href="([^"]+)"', s)
        for h in set(hrefs):
            if h.startswith(("http", "#", "mailto:", "data:", "tel:")):
                continue
            if h.startswith("/"):
                continue
            target = os.path.normpath(os.path.join(d, h.split("?")[0].split("#")[0]))
            if not os.path.exists(target):
                print("  断链 %-52s -> %s" % (path, h))
                bad += 1
print("断链总数:", bad)
sys.exit(1 if bad else 0)
