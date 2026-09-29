#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""引号感知：找出六语属性数不匹配的元素（含 protect 处理值内 < >）"""
import re, sys, importlib.util, os

spec = importlib.util.spec_from_file_location("gi", os.path.join(os.path.dirname(os.path.abspath(__file__)), "gen_i18n.py"))
gi = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gi)

for f in ["blog/_body_shrinkage.html", "blog/_body_measure.html"]:
    raw = open(f, encoding="utf-8").read()
    s = gi.protect(raw)
    i, n = 0, len(s)
    bad = []
    while i < n:
        if s[i] == '<':
            j, in_q, qc = i + 1, False, None
            while j < n:
                ch = s[j]
                if in_q:
                    if ch == qc:
                        in_q = False
                elif ch in '"\'':
                    in_q, qc = True, ch
                elif ch == '>':
                    break
                j += 1
            tag = s[i:j + 1]
            name = re.match(r'<([a-zA-Z0-9]+)', tag)
            counts = {l: len(re.findall(r'data-%s="' % l, tag)) for l in ['zh', 'en', 'fr', 'es', 'ja', 'ko']}
            if name and not tag.startswith('</') and any(counts.values()) and len(set(counts.values())) != 1:
                bad.append((name.group(1), counts, tag[:160]))
            i = j + 1
        else:
            j = s.find('<', i)
            i = j if j != -1 else n
    print("%-34s 不匹配元素 %d 个" % (f, len(bad)))
    for b in bad:
        print("   <%s %s\n      %s" % b)
