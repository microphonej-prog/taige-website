#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把第一篇的英文 description 补到 Google 展示区间（150-160 字符），同步根页 data-en 与 en/ 页 content"""
import re, os

OLD = "Folded hang tags compared: bi-fold, accordion, multi-panel and card formats, with panel layout, creasing, hole placement and paper weight advice."
NEW = "Folded hang tags compared: bi-fold, accordion, multi-panel and card formats, plus panel layout across the fold, creasing, hole placement and paper weight."
print("旧长度 %d -> 新长度 %d" % (len(OLD), len(NEW)))
assert 150 <= len(NEW) <= 162, "长度不在区间"

SLUG = "hang-tag-folding-types.html"
targets = [
    ("blog/%s" % SLUG, 'data-en="%s"' % OLD, 'data-en="%s"' % NEW),
    ("en/blog/%s" % SLUG, 'content="%s"' % OLD, 'content="%s"' % NEW),
]
for path, o, n in targets:
    s = open(path, encoding="utf-8").read()
    assert s.count(o) == 1, "%s 中未唯一找到旧串" % path
    open(path, "w", encoding="utf-8", newline="").write(s.replace(o, n, 1))
    print("已更新", path)

# meta 文件同步（记录用）
mp = "daily_meta_20261012_0800.py"
s = open(mp, encoding="utf-8").read()
assert s.count('desc_en="%s"' % OLD) == 1
open(mp, "w", encoding="utf-8", newline="").write(s.replace('desc_en="%s"' % OLD, 'desc_en="%s"' % NEW, 1))
print("已更新", mp)
