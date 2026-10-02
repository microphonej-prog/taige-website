#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-02 下午批次正文预检：六语属性完整性、引号畸形、裸&、韩/日文汉字残留、篇幅"""
import re, sys

BODIES = ["blog/_body_imposition.html", "blog/_body_hanfu.html"]
ATTRS = ["data-zh", "data-en", "data-ja", "data-ko", "data-fr", "data-es"]

# 提取每个标签的全部属性（含多行属性）
TAG = re.compile(r"<([a-zA-Z][a-zA-Z0-9]*)\b([^>]*)>", re.S)
ATTR = re.compile(r'([a-zA-Z-]+)="([^"]*)"', re.S)

bad_total = 0
for f in BODIES:
    s = open(f, encoding="utf-8").read()
    n_ele = 0
    missing = []
    ko_cjk = []
    ja_cjk = 0
    for m in TAG.finditer(s):
        tag, raw = m.group(1), m.group(2)
        d = dict(ATTR.findall(raw))
        if "data-zh" not in d:
            continue
        n_ele += 1
        for a in ATTRS:
            if not d.get(a, "").strip():
                missing.append((tag, a))
        k = d.get("data-ko", "")
        if re.search(r"[\u4e00-\u9fff]", k):
            ko_cjk.append(k[:70])
        ja_cjk += len(re.findall(r"[\u4e00-\u9fff]", d.get("data-ja", "")))

    zh = "".join(d for d in re.findall(r'data-zh="([^"]*)"', s))
    cjk = len(re.findall(r"[\u4e00-\u9fff]", re.sub(r"<[^>]*>", "", zh)))
    print("== %s ==" % f)
    print("  带 data-zh 的元素 %d 个；缺属性 %d %s" % (n_ele, len(missing), missing[:8]))
    print("  空属性=%d  引号畸形(data-x=\"..\"后紧跟字母)=%d  裸&=%d"
          % (len(re.findall(r'data-(?:zh|en|ja|ko|fr|es)=""', s)),
             len(re.findall(r'data-(?:zh|en|ja|ko|fr|es)="[^"]*"[a-zA-Z]', s)),
             len(re.findall(r"&(?!amp;|nbsp;|quot;|#)", s))))
    print("  中文正文汉字（data-zh，去标签）=%d 字" % cjk)
    print("  韩文串内汉字残留 %d 处 %s" % (len(ko_cjk), ko_cjk[:3]))
    print("  日文串汉字数 %d（正常，日语用汉字）" % ja_cjk)
    bad_total += len(missing)

print("\n结论：缺失属性总数 = %d" % bad_total)
sys.exit(1 if bad_total else 0)
