#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把香氛吊牌英文 description 从 199 字符缩到 153 字符（Google 显示长度）"""
import io

OLD = "Scented hang tags: how microcapsule fragrance releases, choosing full or spot coating versus a scent patch, matching fragrance families to garment types, measuring longevity, and allergen compliance."
NEW = "Scented hang tags: microcapsule release, full versus spot coating, scent families per garment type, longevity testing and allergen compliance for export."
assert len(NEW) == 153, len(NEW)

targets = ["blog/scented-hang-tag-guide.html", "en/blog/scented-hang-tag-guide.html"]
for p in targets:
    s = io.open(p, encoding="utf-8").read()
    n = s.count(OLD)
    s = s.replace(OLD, NEW)
    io.open(p, "w", encoding="utf-8", newline="").write(s)
    print("%s 替换 %d 处" % (p, n))

# 同步元数据文件，保持下次可复现
mp = "daily_meta_20261020_1400.py"
s = io.open(mp, encoding="utf-8").read()
assert OLD in s
io.open(mp, "w", encoding="utf-8", newline="").write(s.replace(OLD, NEW))
print("元数据已同步")
