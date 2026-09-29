#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""扫描：形如  '">\n   data-xx="'  的断标签模式（属性被甩出标签之外）"""
import re, glob

files = ["blog/_body_shrinkage.html", "blog/_body_measure.html",
         "blog/_body_continuity.html", "blog/_body_comm.html", "blog/_body_nonwoven.html"]
for f in files:
    s = open(f, encoding="utf-8", newline="").read()
    m = list(re.finditer(r'">\r?\n\s+data-(?:zh|en|fr|es|ja|ko)=', s))
    print("%-34s 断标签 %d 处" % (f, len(m)))
    for mm in m[:5]:
        print("     ...", repr(s[max(0, mm.start() - 60):mm.start() + 40]))
    # 首行 p 标签末尾
    i = s.find("<p data-")
    j = s.find("\n", i)
    print("     首个 p 行尾:", repr(s[i:j][-24:]))
