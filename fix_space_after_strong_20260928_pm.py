#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""补齐 </strong> 之后缺失的空格（2026-09-28 下午批次，六语）。
规则：en/fr/es/ko/ja 的属性值中，</strong> 后紧跟 ASCII 字母数字或韩文时补一个空格；
中文（zh）不改动（后接汉字无需空格）。幂等。
用法: <python> fix_space_after_strong_20260928_pm.py [--apply]
"""
import re, sys

sys.stdout.reconfigure(encoding="utf-8")
APPLY = "--apply" in sys.argv
FILES = ["blog/_body_origin.html", "blog/_body_pp.html"]
NEED_SPACE = re.compile(r"^[A-Za-z0-9\u00c0-\u024f\uac00-\ud7af]")
count = 0
for f in FILES:
    s = open(f, encoding="utf-8").read()

    def fix(m):
        global count
        lang, val = m.group(1), m.group(2)
        if lang == "zh":
            return m.group(0)
        mm = re.match(r"^(.*?</strong>)(.*)$", val, re.S)
        if not mm:
            return m.group(0)
        head, rest = mm.group(1), mm.group(2)
        if rest and NEED_SPACE.match(rest):
            count += 1
            return 'data-%s="%s %s"' % (lang, head, rest)
        return m.group(0)

    s2 = re.sub(r'data-(zh|en|ja|ko|fr|es)="([^"]*)"', fix, s)
    if s2 != s and APPLY:
        open(f, "w", encoding="utf-8", newline="").write(s2)
    print("%s：%s" % (f, "已更新" if s2 != s else "无需改动"))
print("补空格 %d 处（%s）" % (count, "APPLY" if APPLY else "dry-run"))
