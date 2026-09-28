#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把 2026-09-28 上午批次两篇文章的中文 desc 收敛到 80-120 字（规范要求），
同步更新根目录页面的 data-zh 与静态 content（繁体化，与页面一致）。"""
import re
from opencc import OpenCC
from daily_meta_20260928_am import ARTICLES

CC = OpenCC("s2t")

for a in ARTICLES:
    path = "blog/%s" % a["slug"]
    s = open(path, encoding="utf-8").read()
    new = CC.convert(a["desc_zh"])
    m = re.search(r'<meta name="description".*?>', s, re.S)
    blk = m.group(0)
    blk2 = re.sub(r'data-zh="[^"]*"', 'data-zh="%s"' % new, blk, count=1)
    blk2 = re.sub(r'content="[^"]*"', 'content="%s"' % new, blk2, count=1)
    s2 = s.replace(blk, blk2, 1)
    assert s2 != s
    open(path, "w", encoding="utf-8", newline="").write(s2)

    # 复核：根页 description（data-zh / content）长度；五语页 desc 长度
    chk = open(path, encoding="utf-8").read()
    m2 = re.search(r'<meta name="description".*?>', chk, re.S).group(0)
    zh = re.search(r'data-zh="([^"]*)"', m2).group(1)
    ct = re.search(r'content="([^"]*)"', m2).group(1)
    print("%-50s zh=%d 字  content 一致=%s" % (a["slug"], len(zh), zh == ct))
    for lang in ("en", "ja", "ko", "fr", "es"):
        p = "%s/blog/%s" % (lang, a["slug"])
        t = open(p, encoding="utf-8").read()
        d = re.search(r'<meta name="description" content="([^"]*)"', t)
        print("   %-4s desc=%d 字符 %s" % (lang, len(d.group(1)), d.group(1)[:60]))
