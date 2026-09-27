#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-09-27 上午批次：新增文章站内相对链接与资源引用检查（根页 + 五语生成页）。"""
import os, re, sys

NEW = ["blog/trim-order-contract-terms-guide.html",
       "blog/trim-order-change-cancellation-guide.html"]
LANGS = ["en", "ja", "ko", "fr", "es"]
bad = 0
for f in NEW:
    for path in [f] + [os.path.join(l, f) for l in LANGS]:
        s = open(path, encoding="utf-8").read()
        d = os.path.dirname(path)
        for h in sorted(set(re.findall(r'(?:href|src)="([^"]+)"', s))):
            if h.startswith(("http", "#", "mailto:", "data:", "tel:", "/")):
                continue
            target = os.path.normpath(os.path.join(d, h.split("?")[0].split("#")[0]))
            if not os.path.exists(target):
                print("  断链 %-56s -> %s" % (path, h))
                bad += 1
        # 版本号一致性
        for pat, name in ((r'js/main\.js\?v=([\d.]+)', "main.js"),
                          (r'css/style\.css\?v=([\d.]+)', "style.css"),
                          (r'js/assist\.js\?v=([\d.]+)', "assist.js")):
            m = re.findall(pat, s)
            if not m:
                print("  !! %s 缺 %s 引用" % (path, name))
                bad += 1
print("断链/引用问题总数:", bad)
sys.exit(1 if bad else 0)
