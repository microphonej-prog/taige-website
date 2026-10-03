#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-03 上午批次：正文文件（_body_*.html）六语完整性 + 残留体检"""
import re, sys
from html.parser import HTMLParser

BODIES = ["blog/_body_leather.html", "blog/_body_children.html"]
NEED = ("data-en", "data-ja", "data-ko", "data-fr", "data-es")
CJK = re.compile(r'[\u4e00-\u9fff]')

class Collector(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.tags = []
    def handle_starttag(self, tag, attrs):
        self.tags.append((tag, {k.lower(): (v or "") for k, v in attrs}))

bad = 0
for f in BODIES:
    s = open(f, encoding="utf-8").read()
    p = Collector(); p.feed(s)
    withzh = [(t, a) for t, a in p.tags if "data-zh" in a]
    miss = []
    for t, a in withzh:
        for need in NEED:
            if not a.get(need, "").strip():
                miss.append((t, need, a.get("data-zh", "")[:24]))
    # 非中日语值里的汉字残留（ja 允许汉字；ko/fr/es/en 不应有汉字）
    residue = []
    for t, a in p.tags:
        for k in ("data-en", "data-ko", "data-fr", "data-es"):
            v = a.get(k, "")
            if CJK.search(v):
                residue.append((t, k, v[:40]))
    rawamp = re.findall(r'&(?!amp;|nbsp;|quot;|#)', s)
    malq = re.findall(r'data-(?:zh|en|ja|ko|fr|es)=""', s)
    after = re.findall(r'data-(?:zh|en|ja|ko|fr|es)="[^"]*"[a-zA-Z_]', s)
    print("== %s" % f)
    print("   标签总数 %d，带 data-zh 的 %d；缺语言属性 %d 项 %s"
          % (len(p.tags), len(withzh), len(miss), miss[:6]))
    print("   非中文值汉字残留 %d 项 %s" % (len(residue), residue[:6]))
    print("   空 data 属性 %d；属性后裸字符 %d；裸 & %d" % (len(malq), len(after), len(rawamp)))
    bad += len(miss) + len(residue) + len(malq) + len(after) + len(rawamp)
print("\n结论: 问题总数 = %d" % bad)
sys.exit(1 if bad else 0)
