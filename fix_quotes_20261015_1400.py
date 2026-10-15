#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""找出文本节点（标签外）里的裸 ASCII 双引号并替换为中文引号（属性值内不动）"""
import os, sys, re

ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)

for path in sys.argv[1:]:
    s = open(path, encoding="utf-8").read()
    out = []
    i = 0
    in_tag = False
    n = 0
    while i < len(s):
        c = s[i]
        if c == "<":
            in_tag = True
        elif c == ">":
            in_tag = False
        if c == '"' and not in_tag:
            out.append("««%d»»" % n)   # 占位，稍后按开合配对
            n += 1
            i += 1
            continue
        out.append(c)
        i += 1
    t = "".join(out)
    # 配对替换：奇数个为左引号
    cnt = [0]

    def rep(m):
        cnt[0] += 1
        return "“" if cnt[0] % 2 else "”"

    t = re.sub(r"««\d+»»", rep, t)
    print("%s 文本内裸引号 %d 个" % (os.path.basename(path), n))
    if n:
        open(path, "w", encoding="utf-8", newline="").write(t)
