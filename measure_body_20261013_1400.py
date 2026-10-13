# -*- coding: utf-8 -*-
"""对比：本次新文章与既有文章的正文中文规模（data-zh 中文字符数）"""
import re

FILES = ["blog/_body_embroidery.html", "blog/_body_animalcert.html",
         "blog/_body_piping.html", "blog/_body_dance.html", "blog/_body_thread.html"]

for f in FILES:
    s = open(f, encoding="utf-8").read()
    zh = re.findall(r'data-zh="([^"]*)"', s)
    t = " ".join(zh)
    t = re.sub(r'<[^>]+>', '', t)
    print("%-40s data-zh 条数=%-4d 中文字符=%-5d" % (f, len(zh), len(re.findall(r'[\u4e00-\u9fff]', t))))
