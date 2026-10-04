#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""生成前体检：正文六语属性完整性、引号畸形、裸 &、非法残留。"""
import re, os
from html.parser import HTMLParser

BODIES = ["blog/_body_lining.html", "blog/_body_webbing.html"]
LANGS = ("data-en", "data-ja", "data-ko", "data-fr", "data-es")


class Collector(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.tags = []

    def handle_starttag(self, tag, attrs):
        d = {k.lower(): (v or "") for k, v in attrs}
        self.tags.append((tag, d))


bad = 0
for f in BODIES:
    s = open(f, encoding="utf-8").read()
    p = Collector()
    p.feed(s)
    dzh = [(t, a) for t, a in p.tags if "data-zh" in a]
    missing = []
    for t, a in dzh:
        for need in LANGS:
            if not a.get(need, "").strip():
                missing.append((t, need))
    bad += len(missing)
    print("== %s" % f)
    print("   标签总数 %d，带 data-zh 的 %d，缺 en/ja/ko/fr/es 的 %d %s"
          % (len(p.tags), len(dzh), len(missing), missing[:10]))
    print("   引号畸形 data-xx=\"\" : %d ; 属性值后裸字符: %d ; 裸 & : %d"
          % (len(re.findall(r'data-(?:zh|en|ja|ko|fr|es)=""', s)),
             len(re.findall(r'data-(?:zh|en|ja|ko|fr|es)="[^"]*"[a-zA-Z]', s)),
             len(re.findall(r'&(?!amp;|nbsp;|quot;|#)', s))))
    print("   <section> %d ; </section> %d ; data-zh 计数 %d"
          % (s.count("<section"), s.count("</section>"), len(re.findall(r'data-zh=', s))))
    # 正文默认文本必须是中文（简）——抽样检查首段
    m = re.search(r'data-zh="([^"]*)" data-en=', s)
    print("   首元素 data-zh 预览: %s" % (m.group(1)[:50] if m else "?"))

print("\n结论: 缺失总数 = %d" % bad)
raise SystemExit(1 if bad else 0)
