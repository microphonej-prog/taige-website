#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-06 下午批次：正文文件六语完整性与 CJK 残留预检（生成前）。"""
import re, os

FILES = ["blog/_body_sequin.html", "blog/_body_ribknit.html"]
CJK = re.compile(r'[\u4e00-\u9fff]')
ZH_ONLY = re.compile(r'[，。；：（）「」、]')

bad = 0
for f in FILES:
    s = open(f, encoding="utf-8").read()
    print("==", f, len(s), "bytes")
    # 每个元素块：以 data-zh 开头
    langs = ["en", "ja", "ko", "fr", "es"]
    # 逐属性扫描
    for lang in ["en", "fr", "es"]:
        vals = re.findall(r'data-%s="([^"]*)"' % lang, s)
        hits = [v[:60] for v in vals if CJK.search(v) or ZH_ONLY.search(v)]
        print("   data-%s 值 %d 个；含中文/CJK 的 %d 个 %s" % (lang, len(vals), len(hits), hits[:5]))
        bad += len(hits)
    vals = re.findall(r'data-ko="([^"]*)"', s)
    hits = [v[:60] for v in vals if CJK.search(v) or ZH_ONLY.search(v)]
    print("   data-ko 值 %d 个；含 CJK 的 %d 个 %s" % (len(vals), len(hits), hits[:5]))
    bad += len(hits)
    vals = re.findall(r'data-ja="([^"]*)"', s)
    hits = [v[:60] for v in vals if ZH_ONLY.search(v)]
    print("   data-ja 值 %d 个；含中文标点的 %d 个 %s" % (len(vals), len(hits), hits[:5]))
    bad += len(hits)
    # 每个 data-zh 元素是否配齐其余五语（块状判断）
    blocks = re.split(r'\n(?=      <|\s*<)', s)
    missing = []
    for b in blocks:
        if 'data-zh="' not in b:
            continue
        for lang in langs:
            if 'data-%s="' % lang not in b:
                missing.append(("?", lang, b[:50]))
    print("   含 data-zh 的块：缺其它语言的 %d 个 %s" % (len(missing), missing[:5]))
    bad += len(missing)
    # 引号畸形
    print("   引号畸形 %d ; 裸 & %d ; data-zh 计数 %d"
          % (len(re.findall(r'data-(?:zh|en|fr|es|ja|ko)=""', s)),
             len(re.findall(r'&(?!amp;|nbsp;|quot;|#)', s)),
             len(re.findall(r'data-zh="', s))))
    bad += len(re.findall(r'data-(?:zh|en|fr|es|ja|ko)=""', s))
    bad += len(re.findall(r'&(?!amp;|nbsp;|quot;|#)', s))

print("\n结论: %s" % ("有 %d 处需修" % bad if bad else "预检通过"))
