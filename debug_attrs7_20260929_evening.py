#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""定位第 78 个 data-es 出现位置（是否落在文本节点内）"""
import re

f = "blog/_body_measure.html"
s = open(f, encoding="utf-8", newline="").read()
pos = [m.start() for m in re.finditer(r'data-es="', s)]
print("data-es 出现次数:", len(pos))

# 标记：该位置之前最近的 '<' 与 '>' 谁更近 → 是否在标签内
for p in pos:
    lt = s.rfind("<", 0, p)
    gt = s.rfind(">", 0, p)
    inside = lt > gt
    if not inside:
        print("!! 文本节点内 data-es 位置", p, repr(s[max(0, p - 80):p + 60]))
print("--- 每个出现所属标签的 data-zh 计数校验 ---")
bad = 0
for p in pos:
    lt = s.rfind("<", 0, p)
    gt = s.rfind(">", 0, p)
    if lt > gt:
        j = s.find(">", p)
        tag = s[lt:j + 1]
        n = {l: len(re.findall(r'data-%s="' % l, tag)) for l in ["zh", "en", "fr", "es", "ja", "ko"]}
        if len(set(n.values())) != 1:
            bad += 1
            print("   !!", p, n, tag[:120])
print("标签内计数异常:", bad)
lines = s.split("\n")
for k, ln in enumerate(lines, 1):
    if ln.count('data-es="') > 1:
        print("行 %d 有 %d 个 data-es: %s" % (k, ln.count('data-es="'), ln[:120]))
