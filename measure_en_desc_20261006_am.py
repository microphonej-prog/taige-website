#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""量 en/ja/ko/fr/es 生成页静态 meta description 长度，作为英文 desc 长度基准。"""
import re, os
slugs = ["sewing-thread-selection-guide.html", "flame-retardant-trims-guide.html",
         "reach-svhc-apparel-trims-guide.html", "knitwear-sweater-trims-guide.html"]
for lang in ("en", "ja", "ko", "fr", "es"):
    for slug in slugs:
        p = "%s/blog/%s" % (lang, slug)
        if not os.path.exists(p):
            print("missing", p); continue
        s = open(p, encoding="utf-8").read()
        m = re.search(r'<meta name="description"[^>]*?content="([^"]*)"', s, re.S)
        print("%-58s desc=%3d" % (p, len(m.group(1)) if m else -1))
    print()
