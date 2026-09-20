#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""检查 data-ko / data-fr / data-es / data-en 值里混入汉字（简体残留），以及 data-ja 里混入简体特征字。"""
import re, sys, glob

FILES = sys.argv[1:] or (glob.glob("blog/_body_*.html") + ["daily_gen_20260920_pm.py"])
BAD_KO = re.compile(r'data-(?:ko|fr|es|en)="([^"]*)"')
CJK = re.compile(r'[\u4e00-\u9fff]')
# 简体专属字（繁体/日文不用的常见简体字）
SIMP = set("質们个为说业务经历对标记标注纸张织标签带给从这选饰样时间问题应对产与买卖价贵贱简复杂")

issues = 0
for f in FILES:
    s = open(f, encoding="utf-8").read()
    for m in BAD_KO.finditer(s):
        val = m.group(1)
        hits = set(CJK.findall(val))
        if hits:
            issues += 1
            print("[%s] 非法汉字 %s → %s" % (f, "".join(sorted(hits)), val[:90]))
print("问题数:", issues)
sys.exit(1 if issues else 0)
