#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""确认法语页 title 的撇号在线上是 HTML 转义形式（渲染后正常），不是缺页。"""
import urllib.request, re, random

CB = "?cb=%d" % random.randint(100000, 999999)
for p in ["fr/blog/garment-trims-order-tracking-guide.html",
          "fr/blog/hang-tag-ink-safety-guide.html",
          "fr/blog/index.html"]:
    req = urllib.request.Request("https://taigetag.com/" + p + CB,
                                 headers={"User-Agent": "Mozilla/5.0", "Cache-Control": "no-cache"})
    h = urllib.request.urlopen(req, timeout=45).read().decode("utf-8", "replace")
    t = re.search(r"<title>(.*?)</title>", h, re.S)
    print("== %s" % p)
    print("   title 原文 : %s" % (t.group(1) if t else "-"))
    print("   含 d&#x27;accessoires : %s ; 含 Sécurité : %s"
          % ("d&#x27;accessoires" in h, "S&#233;curit&#233;" in h or "Sécurité" in h))
