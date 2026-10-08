#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把 wooden-bamboo-hang-tags 的英文 description 从 166 字符压到 150–160 字符
（Google 展示长度），同步修改 meta 定义文件、根目录文件 data-en 与 en/blog 静态 content。
"""
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

OLD = "Wooden and bamboo hang tags: birch plywood, solid wood, bamboo and MDF compared, moisture and grain control, laser engraving versus printing, hardware and acceptance."
NEW = "Wooden and bamboo hang tags: birch plywood, solid wood, bamboo and MDF compared, moisture and grain control, laser engraving versus print, and acceptance."

print("旧 %d 字符 / 新 %d 字符" % (len(OLD), len(NEW)))
assert 150 <= len(NEW) <= 160, len(NEW)

TARGETS = [
    "daily_meta_20261008_1500.py",
    "blog/wooden-bamboo-hang-tags.html",
    "en/blog/wooden-bamboo-hang-tags.html",
]
for p in TARGETS:
    s = open(p, encoding="utf-8").read()
    n = s.count(OLD)
    if n == 0:
        print("  !! %s 未找到旧串" % p)
        continue
    s = s.replace(OLD, NEW)
    open(p, "w", encoding="utf-8", newline="").write(s)
    print("  %-42s 替换 %d 处" % (p, n))
