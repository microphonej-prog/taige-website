#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""正文预检：六语属性完整性 / fr-es 混入中文 / 裸引号 / 结构统计"""
import re, sys
from html.parser import HTMLParser

LANGS = ["zh", "en", "ja", "ko", "fr", "es"]
CJK = re.compile(r'[\u4e00-\u9fff]')


class P(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.tags = []

    def handle_starttag(self, tag, attrs):
        self.tags.append((tag, dict(attrs), self.getpos()[0]))


for path in sys.argv[1:]:
    s = open(path, encoding="utf-8").read()
    p = P()
    p.feed(s)
    missing, lack, cjk_wrong, n_text = {}, 0, [], 0
    for tag, a, line in p.tags:
        if tag in ("ul", "ol", "table", "tr", "tbody", "section", "div", "style"):
            continue
        if tag in ("thead", "script"):
            continue
        has = [l for l in LANGS if "data-" + l in a]
        if not has:
            lack += 1
            print("  ! 无任何 data-* 语言属性: <%s> line %d" % (tag, line))
            continue
        n_text += 1
        for l in LANGS:
            if "data-" + l not in a:
                missing[l] = missing.get(l, 0) + 1
        for l in ("fr", "es"):
            if l in a and CJK.search(a[l]):
                cjk_wrong.append((line, l, a[l][:60]))
    print("%s: 元素 %d 个，缺属性 %s，fr/es 含中文 %d 处"
          % (path, n_text, missing or "无", len(cjk_wrong)))
    for x in cjk_wrong[:10]:
        print("   CJK混入 line %d [%s]: %s" % x)
    # 裸引号检查：属性名=data-xx="" 形式
    bad = re.findall(r'data-(?:zh|en|ja|ko|fr|es)=""', s)
    print("   空属性/裸引号异常: %d" % len(bad))
    # 结构统计
    print("   字符数 zh 正文合计: %d" % sum(len(v) for t, a, l in p.tags for k, v in a.items() if k == "data-zh"))
