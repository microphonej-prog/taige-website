# -*- coding: utf-8 -*-
"""修复：<td>/<th> 默认文本与 data-zh 不一致（仅本次两篇文章的正文源文件与 zh 根页）
同时全站扫描同类历史问题并只做报告，不擅自改动历史文章。
"""
import re, sys

TARGETS = ["blog/_body_relabel.html", "blog/_body_resale.html",
           "blog/apparel-relabeling-service-guide.html",
           "blog/secondhand-resale-apparel-label-guide.html"]

pat = re.compile(r'(<t[dh]\b[^>]*?data-zh="([^"]*)"[^>]*?>)([^<]*)(</t[dh]>)', re.S)


def fix(s):
    n = 0

    def repl(m):
        nonlocal n
        if m.group(2) != m.group(3):
            n += 1
            return m.group(1) + m.group(2) + m.group(4)
        return m.group(0)

    return pat.sub(repl, s), n


for f in TARGETS:
    s = open(f, encoding="utf-8").read()
    s2, n = fix(s)
    if n:
        open(f, "w", encoding="utf-8", newline="").write(s2)
    print("%-60s 修复 %d 处" % (f, n))

print("--- 全站历史同类问题扫描（仅报告）---")
import glob, os
tot = 0
for f in sorted(glob.glob("blog/*.html")) + sorted(glob.glob("*/*/blog/*.html")):
    if os.path.basename(f).startswith("_body_"):
        continue
    s = open(f, encoding="utf-8").read()
    i = 0
    for m in pat.finditer(s):
        if m.group(2) != m.group(3):
            i += 1
    if i:
        tot += i
        print("   %-70s %d 处" % (f, i))
print("历史文件同类问题合计:", tot)
