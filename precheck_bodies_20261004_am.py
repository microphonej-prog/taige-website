#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""生成前体检：正文片段六语属性完整性、引号畸形、裸 &、可疑简繁混用、表格列数一致性。"""
import re, sys
from html.parser import HTMLParser

BODIES = ["blog/_body_reflective.html", "blog/_body_hookloop.html"]
LANGS = ["en", "ja", "ko", "fr", "es"]

# 日语里明显不该出现的简体字（真日语汉字不在此列）
BAD_JA = "衬胶链织唛这们说认让过还个为与门关龙组务词汇专钮锁"

class Collector(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.tags = []
    def handle_starttag(self, tag, attrs):
        d = {k.lower(): (v or "") for k, v in attrs}
        self.tags.append((tag, d))

total_missing = 0
for f in BODIES:
    s = open(f, encoding="utf-8").read()
    p = Collector(); p.feed(s)
    dzh = [(t, a) for t, a in p.tags if "data-zh" in a]
    missing = []
    for t, a in dzh:
        for need in LANGS:
            if not a.get("data-%s" % need, "").strip():
                missing.append((t, need))
    total_missing += len(missing)
    print("== %s" % f)
    print("   标签 %d 个，带 data-zh 的 %d 个；缺 en/ja/ko/fr/es 的 %d 个 %s"
          % (len(p.tags), len(dzh), len(missing), missing[:10]))
    print("   引号畸形 data-xx=\"\" : %d ; 属性值后裸字符: %d ; 裸 & : %d"
          % (len(re.findall(r'data-(?:zh|en|ja|ko|fr|es)=""', s)),
             len(re.findall(r'data-(?:zh|en|ja|ko|fr|es)="[^"]*"[a-zA-Z]', s)),
             len(re.findall(r'&(?!amp;|nbsp;|quot;|#|lt;|gt;)', s))))
    print("   data 值内裸双引号: %d" % len(re.findall(r'data-(?:zh|en|ja|ko|fr|es)="[^"]*"[^>]*"', s)))
    # 各语言值里的异类字符（非拉丁/非假名/非谚文/非汉字的混入）
    for t, a in dzh:
        ja = a.get("data-ja", "")
        bad = [c for c in ja if c in BAD_JA]
        if bad:
            print("   [ja 可疑简体] <%s> %s :: %s" % (t, "".join(bad), ja[:60]))
    for t, a in dzh:
        for lg in ("en", "fr", "es"):
            v = a.get("data-%s" % lg, "")
            if re.search(r'[\uac00-\ud7af\u3040-\u30ff]', v):
                print("   [%s 混入谚文/假名] <%s> :: %s" % (lg, t, v[:60]))
    # 表格列数一致性
    for tb in re.findall(r"<table>(.*?)</table>", s, re.S):
        rows = re.findall(r"<tr>(.*?)</tr>", tb, re.S)
        cols = set(len(re.findall(r"<t[hd][ >]", r)) for r in rows)
        if len(cols) != 1:
            print("   表格列数不一致: %s" % sorted(cols))
    # 中文正文长度（去标签、去属性）
    txt = re.sub(r"<[^>]+>", "", re.sub(r'(data-(?:en|ja|ko|fr|es))="[^"]*"', "", s))
    print("   中文正文字符数(估) = %d" % len(re.findall(r"[\u4e00-\u9fff]", txt)))
    print("   内链: %s" % re.findall(r'href="([^"]+)"', s))

print("\n缺失总数 = %d" % total_missing)
sys.exit(1 if total_missing else 0)
