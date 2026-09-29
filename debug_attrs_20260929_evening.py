#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""定位 _body_measure.html 中多出的一个 data-es（引号感知扫描）"""
import re

f = "blog/_body_measure.html"
s = open(f, encoding="utf-8").read()

# 引号感知切标签
i, n = 0, len(s)
tokens = []
while i < n:
    if s[i] == '<':
        j, in_q = i + 1, None
        while j < n:
            ch = s[j]
            if in_q:
                if ch == in_q:
                    in_q = None
            elif ch in '"\'':
                in_q = ch
            elif ch == '>':
                break
            j += 1
        tokens.append(s[i:j + 1])
        i = j + 1
    else:
        j = s.find('<', i)
        if j == -1:
            j = n
        i = j

ids = []
for t in tokens:
    if not t.startswith('<'):
        continue
    name = re.match(r'<([a-zA-Z0-9]+)', t)
    if not name or t.startswith('</') or t.startswith('<!'):
        continue
    counts = {l: len(re.findall(r'data-%s="' % l, t)) for l in ['zh', 'en', 'fr', 'es', 'ja', 'ko']}
    if len(set(counts.values())) != 1 or counts['zh'] == 0:
        ids.append((name.group(1), counts, t[:200].replace('\n', ' ')))

print("异常元素数:", len(ids))
for x in ids:
    print("  <%-6s %s  %s" % x)
