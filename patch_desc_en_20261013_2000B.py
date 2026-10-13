#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-13 第三批：把 belts-suspenders-trims-guide 的英文 description 收到 150–160 字符（Google 显示长度）"""
import glob, os

OLD = "Belts and suspenders trims guide: size conventions that cause returns, genuine versus bonded leather marking, buckle nickel release and salt spray, and export packing."
CANDS = [
    "Belts and suspenders trims guide: size conventions that cause returns, genuine versus bonded leather marking, buckle nickel release and export packing.",
    "Belts and suspenders trims guide: size conventions that cause returns, genuine versus bonded leather marking, buckle nickel and export packing.",
]
NEW = None
for c in CANDS:
    print("候选长度 %d: %s" % (len(c), c[:60]))
    if 150 <= len(c) <= 160 and NEW is None:
        NEW = c
if NEW is None:
    raise SystemExit("没有落在 150–160 的候选")
print("采用：%d 字符" % len(NEW))

TARGETS = ["blog/belts-suspenders-trims-guide.html",
           "en/blog/belts-suspenders-trims-guide.html"]
for f in TARGETS:
    s = open(f, encoding="utf-8").read()
    n = s.count(OLD)
    if n == 0:
        print("  未找到旧串: %s" % f)
        continue
    s = s.replace(OLD, NEW)
    open(f, "w", encoding="utf-8", newline="").write(s)
    print("  已更新 %s（%d 处）" % (f, n))

# 复核
for f in TARGETS:
    s = open(f, encoding="utf-8").read()
    print("  复核 %s: 旧串残留 %d，新串出现 %d，长度 %d" % (f, s.count(OLD), s.count(NEW), len(NEW)))
