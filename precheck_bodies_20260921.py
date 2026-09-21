#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""预检新增正文：六语覆盖、引号畸形、裸 & 、JSON-LD 无关项（正文无）、表格结构。"""
import re, sys
from html.parser import HTMLParser

BODIES = ["blog/_body_hanger_bag.html", "blog/_body_shrink_film.html"]

class C(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.tags = []
    def handle_starttag(self, tag, attrs):
        self.tags.append((tag, {k.lower(): (v or "") for k, v in attrs}))

bad = 0
for f in BODIES:
    s = open(f, encoding="utf-8").read()
    p = C(); p.feed(s)
    print("== %s ==" % f)
    dzh = [(t, a) for t, a in p.tags if "data-zh" in a]
    missing = []
    for t, a in dzh:
        for need in ("data-en", "data-ja", "data-ko", "data-fr", "data-es"):
            if not a.get(need, "").strip():
                missing.append((t, need))
    print("  标签 %d 个，带 data-zh 的 %d 个，缺 ja/ko/en/fr/es 的 %d 个 %s"
          % (len(p.tags), len(dzh), len(missing), missing[:10]))
    bad += len(missing)
    print("  引号畸形 data-xx=\"\" : %d ; 属性值后裸字符: %d ; 裸 & : %d ; 标签数异常: %s"
          % (len(re.findall(r'data-(?:zh|en|fr|es|ja|ko)=""', s)),
             len(re.findall(r'data-(?:zh|en|fr|es|ja|ko)="[^"]*"[a-zA-Z]', s)),
             len(re.findall(r'&(?!amp;|nbsp;|quot;|#|hellip;)', s)),
             p.tags[-1][0]))
    print("  <li> %d / </li> %d ; <p> %d / </p> %d ; <tr> %d ; <td> %d ; <th> %d"
          % (s.count("<li"), s.count("</li>"), s.count("<p "), s.count("</p>"), s.count("<tr>"),
             s.count("<td "), s.count("<th ")))
    # 属性跨行时 引号计数应为偶数
    print("  双引号总数（应为偶数）: %d" % s.count('"'))
    for m in re.finditer(r'data-(?:zh|en|fr|es|ja|ko)="[^"]{0,400}"', s):
        pass
    # 中文字符数（默认文本）
    txt = re.sub(r'<[^>]+>', '', s)
    print("  纯文本中文汉字数: %d" % len(re.findall(r'[\u4e00-\u9fff]', txt)))
print("\n缺失属性总数 = %d" % bad)
sys.exit(1 if bad else 0)
