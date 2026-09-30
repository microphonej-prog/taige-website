#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把 daily_meta_20260930_pm.py 里微调后的 desc 同步进已生成的文章（根目录版 data-en/fr/es
与 en|fr|es 目录版的 meta content），避免重新跑整条生成链。"""
import re, sys
sys.path.insert(0, ".")
from daily_meta_20260930_pm import ARTICLES

for a in ARTICLES:
    slug = a["slug"]
    root = "blog/%s" % slug
    s = open(root, encoding="utf-8").read()
    # 根目录版：多行 desc 块内的 data-en / data-fr / data-es
    blk = re.search(r'<meta name="description".*?>', s, re.S)
    assert blk, "找不到 desc 块: %s" % root
    old_blk = blk.group(0)
    new_blk = old_blk
    for lg in ("en", "fr", "es"):
        m = re.search(r'data-%s="([^"]*)"' % lg, new_blk)
        assert m, "desc 缺 data-%s: %s" % (lg, root)
        old = m.group(1)
        if old != a["desc_%s" % lg]:
            new_blk = new_blk.replace('data-%s="%s"' % (lg, old), 'data-%s="%s"' % (lg, a["desc_%s" % lg]), 1)
    if new_blk != old_blk:
        s = s.replace(old_blk, new_blk, 1)
        open(root, "w", encoding="utf-8", newline="").write(s)
        print("根版已更新 %s" % root)

    # 语言目录版：<meta name="description" content="...">
    for lg in ("en", "fr", "es"):
        p = "%s/blog/%s" % (lg, slug)
        s = open(p, encoding="utf-8").read()
        m = re.search(r'<meta name="description" content="([^"]*)">', s)
        assert m, "找不到 desc: %s" % p
        if m.group(1) != a["desc_%s" % lg]:
            s = s.replace(m.group(0), '<meta name="description" content="%s">' % a["desc_%s" % lg], 1)
            open(p, "w", encoding="utf-8", newline="").write(s)
            print("  %s 已更新" % p)

print("desc 同步完成")
for a in ARTICLES:
    print("  %-42s en=%d fr=%d es=%d" % (a["slug"], len(a["desc_en"]), len(a["desc_fr"]), len(a["desc_es"])))
