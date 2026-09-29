#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""决定性校验：protect + 引号感知分词，统计各语言属性总数与文本节点中泄漏的 data-* 字面量"""
import re, os, importlib.util

spec = importlib.util.spec_from_file_location("gi", os.path.join(os.path.dirname(os.path.abspath(__file__)), "gen_i18n.py"))
gi = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gi)

for f in ["blog/_body_shrinkage.html", "blog/_body_measure.html"]:
    s = gi.protect(open(f, encoding="utf-8", newline="").read())
    i, n = 0, len(s)
    tot = {l: 0 for l in ["zh", "en", "fr", "es", "ja", "ko"]}
    leak = []
    ntags = 0
    while i < n:
        if s[i] == "<":
            j, in_q, qc = i + 1, False, None
            while j < n:
                ch = s[j]
                if in_q:
                    if ch == qc:
                        in_q = False
                elif ch in '"\'':
                    in_q, qc = True, ch
                elif ch == ">":
                    break
                j += 1
            tag = s[i:j + 1]
            if not tag.startswith(("</", "<!")):
                ntags += 1
                for l in tot:
                    tot[l] += len(re.findall(r'data-%s="' % l, tag))
            i = j + 1
        else:
            j = s.find("<", i)
            chunk = s[i:(j if j != -1 else n)]
            if "data-" in chunk:
                leak.append(chunk[:120])
            i = j if j != -1 else n
    print("%-34s 标签 %d，各语言属性总数 %s" % (f, ntags, tot))
    print("   文本节点内泄漏 data-* 字面量: %d 处 %s" % (len(leak), leak[:2]))
