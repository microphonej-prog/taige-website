#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""正文文件预检（2026-09-30 下午批次）：六语属性完整性、引号畸形、裸 &、语言纯净度。"""
import re, sys
from html.parser import HTMLParser

FILES = ["blog/_body_density.html", "blog/_body_calendar.html"]
LANGS = ["zh", "en", "ja", "ko", "fr", "es"]


class Collector(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.tags = []

    def handle_starttag(self, tag, attrs):
        d = {k.lower(): (v or "") for k, v in attrs}
        self.tags.append((tag, d))


total = 0
for f in FILES:
    s = open(f, encoding="utf-8").read()
    p = Collector()
    p.feed(s)
    withzh = [(t, a) for t, a in p.tags if "data-zh" in a]
    missing = []
    for t, a in withzh:
        for need in ("data-en", "data-ja", "data-ko", "data-fr", "data-es"):
            if not a.get(need, "").strip():
                missing.append((t, need))
    total += len(missing)
    print("== %s" % f)
    print("   标签总数 %d，带 data-zh 的 %d，缺其它语言的 %d %s"
          % (len(p.tags), len(withzh), len(missing), missing[:6]))
    print("   空 data-xx=\"\" : %d" % len(re.findall(r'data-(?:zh|en|fr|es|ja|ko)=""', s)))
    print("   属性值后紧跟裸字符: %d" % len(re.findall(r'data-(?:zh|en|fr|es|ja|ko)="[^"]*"[a-zA-Z]', s)))
    print("   裸 & 数量: %d" % len(re.findall(r'&(?!amp;|nbsp;|quot;|#)', s)))
    # 语言纯净度：en/fr/es 值里不应有 CJK；ko 值里不应有汉字；ja 可以有汉字
    for t, a in withzh:
        for lg in ("en", "fr", "es"):
            if re.search(r"[\u4e00-\u9fff\u3040-\u30ff\uac00-\ud7af]", a.get(lg, "")):
                print("   !! %s 值含 CJK/假名/谚文: <%s> %s" % (lg, t, a.get(lg, "")[:60]))
        if re.search(r"[\u4e00-\u9fff]", a.get("ko", "")):
            print("   !! ko 值含汉字: <%s> %s" % (t, a.get("ko", "")[:60]))
    # data-zh 与元素默认文本一致性（抽查前 3 个）
    m = re.findall(r'<(\w+)([^>]*data-zh="([^"]*)"[^>]*)>([^<]*)</\1>', s)
    bad = 0
    for tag, attrs, zh, txt in m:
        if txt and txt.strip() != zh.strip() and "<" not in zh:
            bad += 1
            if bad <= 3:
                print("   ? 默认文本与 data-zh 不同 <%s>: %s | %s" % (tag, zh[:40], txt[:40]))
    print("   默认文本与 data-zh 不一致的元素: %d（含属性在前的正常情况）" % bad)

print("\n缺语言总数 = %d" % total)
