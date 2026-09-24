#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""定位 en/fr/es 版本里的残留汉字位置"""
import re
for p in ["en/blog/chinese-new-year-trims-order-planning.html",
          "en/blog/clothing-label-compliance-uae.html",
          "fr/blog/clothing-label-compliance-uae.html",
          "es/blog/chinese-new-year-trims-order-planning.html"]:
    s = open(p, encoding="utf-8").read()
    i = s.index('class="article-body"')
    j = s.index("</main>")
    seg = s[i:j]
    print(p)
    print("   正文段（article-body→/main）内汉字:", len(re.findall(r"[\u4e00-\u9fff]", seg)))
    for m in re.finditer(r"[\u4e00-\u9fff]+", s):
        ctx = s[max(0, m.start() - 50):m.end() + 25].replace("\n", " ")
        print("     ", repr(ctx))
    print()
