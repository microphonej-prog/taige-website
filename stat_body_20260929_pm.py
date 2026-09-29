#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-09-29 下午批次篇幅统计：各新文章正文默认可见汉字数（对照往期约 2100–2700 字）。"""
import re, sys, io, os
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
os.chdir(os.path.dirname(os.path.abspath(__file__)))
FILES = ['blog/_body_digital.html', 'blog/_body_coding.html',
         'blog/_body_continuity.html', 'blog/_body_comm.html']
for f in FILES:
    s = open(f, encoding='utf-8').read()
    txt = re.sub(r'<[^>]+>', ' ', s)
    txt = re.sub(r'data-[a-z-]+="[^"]*"', ' ', txt, flags=re.S)
    zh = len(re.findall(r'[\u4e00-\u9fff]', txt))
    print("%-34s 默认可见汉字 %d" % (f, zh))
