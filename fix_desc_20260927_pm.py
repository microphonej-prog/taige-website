#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把 2026-09-27 下午两篇文章的 desc_en 修到 150-160 字符，并重新生成 en 版本页面。"""
import subprocess, sys

PAIRS = [
    ("blog/garment-spare-button-bag-guide.html",
     "A spare button bag is one of the first things a shopper touches. This guide covers four formats, sizes worked back from contents, printing and child safety rules.",
     "A spare button bag is often the first thing a shopper touches. This guide covers four formats, sizes worked back from contents, printing and child safety."),
    ("blog/trim-supplier-scorecard-guide.html",
     "How to score trim suppliers: on-time rate, defect rate, response speed and documents, plus weights, tiers and how scores drive order allocation, improvements and backups.",
     "How to score trim suppliers: on-time rate, defect rate, response speed and documents, plus weights, tiers and how scores drive order allocation and backups."),
]

for path, old, new in PAIRS:
    s = open(path, encoding="utf-8").read()
    n = s.count(old)
    assert n == 1, "%s 中旧 desc_en 命中 %d 次" % (path, n)
    s = s.replace(old, new, 1)
    open(path, "w", encoding="utf-8", newline="").write(s)
    print("已更新 %s（新 desc_en %d 字符）" % (path, len(new)))

r = subprocess.run([sys.executable, "gen_i18n.py", "en"] + [p for p, _, _ in PAIRS],
                   capture_output=True, text=True, encoding="utf-8")
print(r.stdout.strip(), r.stderr.strip())
assert r.returncode == 0, "gen_i18n en 失败"

for p, _, new in PAIRS:
    en = "en/" + p
    s = open(en, encoding="utf-8").read()
    assert 'content="%s"' % new.replace("&", "&amp;") in s, "en 页 desc 未更新：%s" % en
    print("校验通过 %s desc=%d" % (en, len(new)))
