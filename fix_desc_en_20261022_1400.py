#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把本批次两篇英文 description 同步为缩短版（165+ 字符 → 150-160）"""
import re
from daily_meta_20261022_1400 import ARTICLES

for a in ARTICLES:
    slug, new = a["slug"], a["desc_en"]
    print("%-46s 新 desc_en 长度=%d" % (slug, len(new)))
    # 1) 根目录页：data-en 属性
    p = "blog/" + slug
    s = open(p, encoding="utf-8").read()
    s2, n1 = re.subn(r'data-en="Recycled polyester trims:[^"]*"|data-en="Southeast Asia [^"]*"',
                     'data-en="%s"' % new, s, count=1)
    if n1:
        open(p, "w", encoding="utf-8", newline="").write(s2)
    # 2) 英文版：meta description content
    q = "en/blog/" + slug
    t = open(q, encoding="utf-8").read()
    t2, n2 = re.subn(r'<meta name="description" content="Recycled polyester trims:[^"]*">|<meta name="description" content="Southeast Asia [^"]*">',
                     '<meta name="description" content="%s">' % new, t, count=1)
    if n2:
        open(q, "w", encoding="utf-8", newline="").write(t2)
    print("   根页替换=%d 英文页替换=%d" % (n1, n2))
    # 校验
    for f, pat in [(p, r'data-en="([^"]*)"'), (q, r'<meta name="description" content="([^"]*)">')]:
        m = re.search(pat, open(f, encoding="utf-8").read())
        print("   %-40s → %s" % (f, (m.group(1)[:70] + "…") if m else "未找到"))
