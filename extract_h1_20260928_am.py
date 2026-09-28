#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""提取指定文章 h1 的六语属性，供「相关文章」锚文本复用。"""
import re, sys

SLUGS = ["paper-bag-types.html", "recycled-paper-packaging.html",
         "eu-ppwr-packaging-compliance.html", "poly-bag-eco-options.html",
         "garment-packaging-ecofriendly.html", "eco-friendly-hangtag-materials.html"]

for sl in SLUGS:
    s = open("blog/" + sl, encoding="utf-8").read()
    m = re.search(r"<h1 ([^>]*)>", s)
    print("=== %s" % sl)
    print(m.group(1))
    print()
