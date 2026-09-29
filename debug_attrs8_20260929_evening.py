#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""用引号奇偶法判定每个 data-es 是否位于属性位置；找出异常那一个"""
import re

for f in ["blog/_body_measure.html", "blog/_body_shrinkage.html"]:
    s = open(f, encoding="utf-8", newline="").read()
    print("=====", f, "data-es 出现", len(re.findall(r'data-es="', s)))
    for m in re.finditer(r'data-es="', s):
        p = m.start()
        lt = s.rfind("<", 0, p)
        seg = s[lt:p] if lt >= 0 else s[:p]
        if seg.count('"') % 2 == 1:
            print("  在属性值内（无害）:", repr(s[max(0, p - 70):p + 50]))
    # 每个标签的平衡性：按引号奇偶法列出所有属性名
    attrs = []
    for m in re.finditer(r'(?:^|[\s"\'<>])(data-(?:zh|en|fr|es|ja|ko))="', s):
        attrs.append((m.start(1), m.group(1)))
    # 归组：位置落在同一个标签内（“标签内”= 前面最近的 '<' 与 '"' 奇偶）
    groups = []
    for pos, name in attrs:
        lt = s.rfind("<", 0, pos)
        key = lt
        if not groups or groups[-1][0] != key:
            groups.append((key, {}))
        groups[-1][1][name] = groups[-1][1].get(name, 0) + 1
    bad = [(k, g) for k, g in groups if len(set(g.values())) != 1 or len(g) != 6]
    print("  标签组数:", len(groups), " 六语不齐的组:", len(bad))
    for b in bad[:10]:
        print("    !!", b, repr(s[max(0, b[0] - 30):b[0] + 90]))
