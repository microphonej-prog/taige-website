#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""生成前预检：正文文件六语属性完整性、引号畸形、裸 &，以及 desc 长度。"""
import re, sys, os
from html.parser import HTMLParser

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from daily_meta_20261009_1400 import ARTICLES

LANGS = ("data-zh", "data-en", "data-ja", "data-ko", "data-fr", "data-es")


class Collector(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.in_body = False
        self.tags = []

    def handle_starttag(self, tag, attrs):
        d = {k.lower(): (v or "") for k, v in attrs}
        if tag == "section" and d.get("class", "").startswith("article-body"):
            self.in_body = True
            return
        if self.in_body:
            self.tags.append((tag, d, self.getpos()))

    def handle_endtag(self, tag):
        if self.in_body and tag == "section":
            self.in_body = False


print("== desc 长度 ==")
for a in ARTICLES:
    print("  %-42s zh=%d en=%d ja=%d ko=%d fr=%d es=%d"
          % (a["slug"], len(a["desc_zh"]), len(a["desc_en"]), len(a["desc_ja"]),
             len(a["desc_ko"]), len(a["desc_fr"]), len(a["desc_es"])))

print("== 正文六语属性 ==")
bad = 0
for a in ARTICLES:
    s = open(a["body"], encoding="utf-8").read()
    p = Collector()
    p.feed(s)
    tagged = [(t, d, pos) for t, d, pos in p.tags if "data-zh" in d]
    missing = []
    for t, d, pos in tagged:
        for need in LANGS:
            if not d.get(need, "").strip():
                missing.append((t, need, pos[0]))
    bad += len(missing)
    print("  %s" % a["body"])
    print("    标签总数 %d，带 data-zh 的 %d，缺语言属性 %d %s"
          % (len(p.tags), len(tagged), len(missing), missing[:10]))
    print("    引号畸形 data-xx=\"\" : %d ; 属性值后裸字符: %d ; 裸 & : %d"
          % (len(re.findall(r'data-(?:zh|en|fr|es|ja|ko)=""', s)),
             len(re.findall(r'data-(?:zh|en|fr|es|ja|ko)="[^"]*"[a-zA-Z]', s)),
             len(re.findall(r'&(?!amp;|nbsp;|quot;|#)', s))))
    # 未带 data-zh 的标签（应只有结构与 <li><a> 之类的容器）
    noz = [(t, pos[0]) for t, d, pos in p.tags if "data-zh" not in d]
    print("    无 data-zh 的标签: %s" % noz[:12])
    # 表格列数一致性
    for m in re.finditer(r'<tr>(.*?)</tr>', s, re.S):
        row = m.group(1)
        print("    tr: th=%d td=%d" % (row.count("<th "), row.count("<td ")))

print("\n缺失总数 = %d" % bad)
