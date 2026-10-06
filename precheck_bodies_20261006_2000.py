#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-06 晚间批次：正文文件六语完整性与引号/CJK 残留预检（生成前）。"""
import re

FILES = ["blog/_body_saltspray.html", "blog/_body_functional.html"]
CJK = re.compile(r'[\u4e00-\u9fff]')
ZH_PUNCT = re.compile(r'[，。；：、（）「」]')
LANGS = ["en", "ja", "ko", "fr", "es"]

bad = 0
for f in FILES:
    s = open(f, encoding="utf-8").read()
    print("==", f, len(s), "bytes")
    # 1) 逐元素（start tag）检查 data-zh 元素是否配齐其余五语
    tags = re.findall(r'<[a-zA-Z][^>]*>', s)
    n_zh = 0
    incomplete = []
    for t in tags:
        if 'data-zh="' not in t:
            continue
        n_zh += 1
        miss = [l for l in LANGS if ('data-%s="' % l) not in t]
        if miss:
            incomplete.append((miss, t[:70]))
    print("   含 data-zh 的起始标签：%d；缺语言：%d %s" % (n_zh, len(incomplete), incomplete[:6]))
    bad += len(incomplete)
    # 2) 属性值逐语言扫描
    for lang in ["en", "fr", "es"]:
        vals = re.findall(r'data-%s="([^"]*)"' % lang, s)
        hits = [v[:60] for v in vals if CJK.search(v) or ZH_PUNCT.search(v)]
        print("   data-%s: %d 个，含中文/CJK %d %s" % (lang, len(vals), len(hits), hits[:4]))
        bad += len(hits)
    for lang in ["ja", "ko"]:
        vals = re.findall(r'data-%s="([^"]*)"' % lang, s)
        hits = [v[:60] for v in vals if ZH_PUNCT.search(v)]
        print("   data-%s: %d 个，含中文标点 %d %s" % (lang, len(vals), len(hits), hits[:4]))
        bad += len(hits)
    # 3) 畸形引号 / 裸 &
    q = re.findall(r'data-(?:zh|en|fr|es|ja|ko)=""', s)
    amp = re.findall(r'&(?!amp;|nbsp;|quot;|lt;|gt;|#)', s)
    print("   空属性 %d ; 裸 & %d ; data-zh 总数 %d ; 平衡引号 %s"
          % (len(q), len(amp), len(re.findall(r'data-zh="', s)), s.count('"') % 2 == 0))
    bad += len(q) + len(amp)
    if len(q) or len(amp):
        print("   空属性样例:", q[:3], "裸&样例:", amp[:5])

print("\n结论: %s" % ("有 %d 处需修" % bad if bad else "预检通过"))
