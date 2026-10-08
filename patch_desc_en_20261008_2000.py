#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-08 晚批次：把 stone-paper-hang-tags-guide 的英文 description 收到 150–160 字符
（原 185 字符超出 Google 显示长度），同步更新根文件 data-en 与 en/blog 的 content。"""
import os

ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)

OLD = ("Stone paper hang tags: mineral paper composition and density, waterproof and tear-resistant "
       "behaviour, comparison with coated and PP synthetic paper, printing limits, holes and eyelets.")
NEW = ("Stone paper hang tags: mineral paper composition and density, water and tear resistance, "
       "versus coated and PP synthetic paper, printing rules, holes and eyelets.")
print("新 desc_en 长度 = %d 字符" % len(NEW))

targets = ["blog/stone-paper-hang-tags-guide.html", "en/blog/stone-paper-hang-tags-guide.html"]
for p in targets:
    s = open(p, encoding="utf-8").read()
    n = s.count(OLD)
    if n == 0:
        print("  %-46s 未找到旧值（可能已改）" % p)
        continue
    open(p, "w", encoding="utf-8", newline="").write(s.replace(OLD, NEW))
    print("  %-46s 替换 %d 处" % (p, n))
