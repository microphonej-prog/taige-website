#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把首篇 desc_en 调到 150-160 字符（Google 显示长度），并同步更新到已生成的所有语言页。"""
import glob, os

OLD = "Poly bag header card guide: sizing against bag width, 300\u2013400 gsm board and lamination choices, foil and eco inks, punching, fixing and carton tips."
NEW = "Poly bag header card guide: sizing a card against bag width, 300\u2013400 gsm board and lamination choices, foil stamping and eco inks, punching and fixing."

print("len(OLD)=%d  len(NEW)=%d" % (len(OLD), len(NEW)))
assert 150 <= len(NEW) <= 160, "desc_en 长度不合格"

slug = "garment-bag-header-card-guide.html"
targets = ["blog/%s" % slug] + ["%s/blog/%s" % (l, slug) for l in ("en", "ja", "ko", "fr", "es")]
# 语言页里 en 版本的 content 才是这条；其他语言页也一并替换（幂等，找不到就跳过）
n_total = 0
for p in targets:
    s = open(p, encoding="utf-8").read()
    n = s.count(OLD)
    if n:
        s = s.replace(OLD, NEW)
        open(p, "w", encoding="utf-8", newline="").write(s)
        n_total += n
    print("  %-58s 替换 %d 处" % (p, n))
print("共替换 %d 处" % n_total)

# 同步 daily_meta 源码，保持下次可复现
mp = "daily_meta_20260930_evening.py"
s = open(mp, encoding="utf-8").read()
assert OLD in s
open(mp, "w", encoding="utf-8", newline="").write(s.replace(OLD, NEW))
print("daily_meta 已同步")
