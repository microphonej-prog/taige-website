#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-09-29 晚间批次正文自检（引号感知）：六语属性齐备 + 标签配平 + 无泄漏字面量"""
import re, os, sys, importlib.util

FILES = ["blog/_body_shrinkage.html", "blog/_body_measure.html"]
spec = importlib.util.spec_from_file_location("gi", os.path.join(os.path.dirname(os.path.abspath(__file__)), "gen_i18n.py"))
gi = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gi)

bad = 0
for f in FILES:
    s = gi.protect(open(f, encoding="utf-8", newline="").read())
    i, n = 0, len(s)
    tot = {l: 0 for l in ["zh", "en", "fr", "es", "ja", "ko"]}
    mismatch, leak, ntags = [], [], 0
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
                cnt = {l: len(re.findall(r'data-%s="' % l, tag)) for l in tot}
                for l in tot:
                    tot[l] += cnt[l]
                if any(cnt.values()) and len(set(cnt.values())) != 1:
                    mismatch.append((cnt, tag[:120]))
            i = j + 1
        else:
            j = s.find("<", i)
            chunk = s[i:(j if j != -1 else n)]
            if "data-" in chunk:
                leak.append(chunk[:120])
            i = j if j != -1 else n

    print("== %s  标签 %d  属性总数 %s" % (f, ntags, tot))
    if len(set(tot.values())) != 1:
        print("   !! 六语属性总数不等")
        bad += 1
    if mismatch:
        print("   !! 属性不齐元素 %d 个：%s" % (len(mismatch), mismatch[:3]))
        bad += 1
    if leak:
        print("   !! 文本节点泄漏 %d 处：%s" % (len(leak), leak[:2]))
        bad += 1

    raw = open(f, encoding="utf-8", newline="").read()
    for a, b in [("<tr", "</tr>"), ("<td", "</td>"), ("<th", "</th>"), ("<li", "</li>"), ("<p ", "</p>"), ("<table", "</table>")]:
        ca, cb = raw.count(a), raw.count(b)
        print("   %-7s %3d / %-8s %3d  %s" % (a, ca, b, cb, "OK" if ca == cb else "!!! 不配平"))
        if ca != cb:
            bad += 1
    print("   h2 %d  表格 %d  内链 %d  字节 %d"
          % (raw.count("<h2 "), raw.count("<table>"), len(re.findall(r'<a href=', raw)), len(raw.encode())))

print("\n结论：", "全部通过" if bad == 0 else "%d 项待修" % bad)
sys.exit(1 if bad else 0)
