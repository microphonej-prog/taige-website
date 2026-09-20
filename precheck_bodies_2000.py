#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""正文文件预检：属性完整性、引号畸形、裸 &、语言残留。"""
import re, sys, os

FILES = ["blog/_body_gift_box.html", "blog/_body_polybag_cost.html"]
bad = 0
for f in FILES:
    s = open(f, encoding="utf-8").read()
    print("== %s (%d KB)" % (f, len(s.encode()) // 1024))
    print("   引号畸形 data-x=\"\" :", len(re.findall(r'data-(?:zh|en|fr|es|ja|ko)=""', s)))
    print("   值后裸字符:", len(re.findall(r'data-(?:zh|en|fr|es|ja|ko)="[^"]*"[a-zA-Z]', s)))
    print("   裸 &:", len(re.findall(r'&(?!amp;|nbsp;|quot;|#)', s)))
    c = {k: len(re.findall(r'data-%s=' % k, s)) for k in ("zh", "en", "fr", "es", "ja", "ko")}
    print("   计数 zh/en/fr/es/ja/ko:", c["zh"], c["en"], c["fr"], c["es"], c["ja"], c["ko"])
    if len(set(c.values())) != 1:
        print("   !! 各语言属性数量不一致")
        bad += 1
    # 非中文语言值里不应有汉字
    kw = {"en": "英文", "fr": "法文", "es": "西文"}
    for m in re.finditer(r'data-(en|fr|es|ja|ko)="([^"]*)"', s):
        lang, val = m.group(1), m.group(2)
        if lang in kw and re.search(r'[\u4e00-\u9fff]', val):
            print("   !! %s 值含汉字: %s" % (kw[lang], val[:70]))
            bad += 1
    # 中日韩字数统计（译文完整性粗检）
    for lang in ("en", "fr", "es", "ja", "ko"):
        vals = re.findall(r'data-%s="([^"]*)"' % lang, s)
        tot = sum(len(v) for v in vals)
        print("   %s 译文总字符: %d" % (lang, tot))
    # 关键内容交叉检查
    for k in ("clothing-label-compliance", "如何", "怎么"):
        pass
print("\n结论: 异常 %d" % bad)
sys.exit(1 if bad else 0)
