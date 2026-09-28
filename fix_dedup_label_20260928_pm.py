#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""去掉属性值里重复的小标题：<strong>X：</strong>X：…… → <strong>X：</strong>……
（2026-09-28 下午批次，六语通用，幂等）
用法: <python> fix_dedup_label_20260928_pm.py [--apply]
"""
import re, sys

sys.stdout.reconfigure(encoding="utf-8")
APPLY = "--apply" in sys.argv
FILES = ["blog/_body_origin.html", "blog/_body_pp.html"]
LANGS = ["zh", "en", "ja", "ko", "fr", "es"]


def pat_body(label):
    """把小标题文本变成宽松正则：标点/空格可缺省或变化"""
    out = []
    for ch in label:
        if ch.isalnum():
            out.append(re.escape(ch))
        elif ch in " \u00a0":
            out.append(r"\s*")
        else:
            out.append(r"[\s:：·・\-]*")
    return "".join(out).rstrip(r"[\s:：·・\-]*").replace(r"[\s:：·・\-]*$", "")


fixed = 0
for f in FILES:
    s = open(f, encoding="utf-8").read()
    rep = []

    def fix_attr(m):
        global fixed
        lang, val = m.group(1), m.group(2)
        mm = re.match(r"(<strong>)(.*?)(</strong>)(.*)$", val, re.S)
        if not mm:
            return m.group(0)
        lab, rest = mm.group(2), mm.group(4)
        p = re.compile(r"^\s*" + pat_body(lab) + r"[\s:：·]*", re.I)
        m2 = p.match(rest)
        if not m2 or m2.end() == m2.start():
            return m.group(0)
        fixed += 1
        return 'data-%s="%s%s%s%s"' % (lang, mm.group(1), lab, mm.group(3), rest[m2.end():])

    s2 = re.sub(r'data-(zh|en|ja|ko|fr|es)="([^"]*)"', fix_attr, s)
    if s2 != s:
        rep.append(f)
        if APPLY:
            open(f, "w", encoding="utf-8", newline="").write(s2)
    print("%s：%s" % (f, "已修正" if s2 != s else "无重复"))
print("合计修正属性 %d 处（%s）" % (fixed, "APPLY" if APPLY else "dry-run"))
