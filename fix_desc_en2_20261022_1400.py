#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""修正 fix_desc_en 的误替换：title 的 data-en 被描述文本覆盖，需恢复 title 并单独改描述"""
import re
from daily_meta_20261022_1400 import ARTICLES

for a in ARTICLES:
    slug = a["slug"]
    root = "blog/" + slug
    s = open(root, encoding="utf-8").read()

    # 1) 恢复 <title> 的 data-en
    m = re.search(r'<title ([^>]*)>', s)
    attrs = m.group(1)
    attrs2 = re.sub(r'data-en="[^"]*"', 'data-en="%s"' % a["title_en"], attrs, count=1)
    s = s[:m.start()] + '<title ' + attrs2 + '>' + s[m.end():]

    # 2) meta description 块内的 data-en 改为缩短版
    i0 = s.index('<meta name="description"')
    i1 = s.index('>', i0)
    block = s[i0:i1]
    block2 = re.sub(r'data-en="[^"]*"', 'data-en="%s"' % a["desc_en"], block, count=1)
    s = s[:i0] + block2 + s[i1:]
    open(root, "w", encoding="utf-8", newline="").write(s)

    # 3) 英文版：title 与 description
    q = "en/blog/" + slug
    t = open(q, encoding="utf-8").read()
    t = re.sub(r'<title>[^<]*</title>', '<title>%s</title>' % a["title_en"].replace("&", "&amp;"), t, count=1)
    t = re.sub(r'<meta name="description" content="[^"]*">',
               '<meta name="description" content="%s">' % a["desc_en"], t, count=1)
    open(q, "w", encoding="utf-8", newline="").write(t)

    # 4) 校验
    s = open(root, encoding="utf-8").read()
    bt = re.search(r'<title ([^>]*)>', s).group(1)
    print("%-46s title_en=%s" % (slug, re.search(r'data-en="([^"]*)"', bt).group(1)[:60]))
    blk = s[s.index('<meta name="description"'):]
    blk = blk[:blk.index('>')]
    den = re.search(r'data-en="([^"]*)"', blk).group(1)
    print("   desc_en(%d)=%s" % (len(den), den[:70]))
    t = open(q, encoding="utf-8").read()
    print("   en页 title=%s" % re.search(r'<title>([^<]*)</title>', t).group(1)[:60])
    print("   en页 desc =%s" % re.search(r'<meta name="description" content="([^"]*)"', t).group(1)[:60])
