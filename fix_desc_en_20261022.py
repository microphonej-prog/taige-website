#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把两篇文章的英文 description 收敛到 150-160 字符（root + en 副本）"""
import os, re, glob

PAIRS = [
    ("magnetic-trims-air-freight-guide.html",
     "Magnetic trims and smart tags by air: which items get special handling, what the 0.418 A/m at 2.1 m limit measures, UN38.3 for coin cells, paperwork and packing.",
     "Magnetic trims and smart tags by air: which items get special handling, what the 0.418 A/m at 2.1 m limit measures, UN38.3 for coin cells, and the paperwork."),
    ("trim-label-consistency-audit-guide.html",
     "Trim label consistency audit: why hang tags, woven labels, care labels and bags drift apart, eight fields that disagree with their consequences, and a master-first check order.",
     "Trim label consistency audit: why hang tags, woven labels, care labels and bags drift apart, the eight fields that disagree, and a master-first check order."),
]

for slug, old, new in PAIRS:
    print("%s new_len=%d" % (slug, len(new)))
    for p in ["blog/%s" % slug, "en/blog/%s" % slug]:
        if not os.path.exists(p):
            print("  缺失 %s" % p)
            continue
        s = open(p, encoding="utf-8").read()
        n = s.count(old)
        s = s.replace(old, new)
        open(p, "w", encoding="utf-8", newline="").write(s)
        print("  %s 替换 %d 处" % (p, n))
