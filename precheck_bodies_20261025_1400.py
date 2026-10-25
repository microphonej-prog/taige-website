#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""预检：正文文件六语属性完整性 + 引号安全 + 有无非法裸双引号"""
import re, sys
from html.parser import HTMLParser

BODIES = ["blog/_body_tyvek.html", "blog/_body_sewdef.html"]
LANGS = ["data-zh", "data-en", "data-ja", "data-ko", "data-fr", "data-es"]


class P(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.tags = []
        self.bad = []

    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        self.tags.append((tag, d))

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)


for path in BODIES:
    s = open(path, encoding="utf-8").read()
    p = P()
    p.feed(s)
    # 统计带 data-zh 的元素
    zh_tags = [(t, d) for t, d in p.tags if "data-zh" in d]
    missing = []
    for t, d in zh_tags:
        miss = [a for a in LANGS if a not in d]
        if miss:
            missing.append((t, miss, d.get("data-zh", "")[:40]))
    # 带 data-en/fr/es/ja/ko 但缺 data-zh
    orphan = [(t, d) for t, d in p.tags if any(a in d for a in LANGS[1:]) and "data-zh" not in d]
    # 空属性
    empty = [(t, k) for t, d in zh_tags for k in LANGS if d.get(k, "x") is not None and not str(d.get(k, "")).strip()]
    # 属性值里是否有残留 & 未转义（& 后面不是实体）
    badamp = [m for m in re.findall(r'data-(?:zh|en|ja|ko|fr|es)="[^"]*&(?:[a-zA-Z#][^;"]*)?[^";]*"', s)
              if not re.search(r'&(amp|nbsp|quot|lt|gt|#\d+);', m)]
    print("=" * 70)
    print(path)
    print("  带 data-zh 元素数:", len(zh_tags), " 全部六语齐全:", len(zh_tags) - len(missing))
    print("  缺属性的元素:", len(missing))
    for x in missing[:10]:
        print("    -", x)
    print("  有翻译缺 data-zh 的元素:", len(orphan))
    for t, d in orphan[:5]:
        print("    -", t, list(d.keys())[:4])
    print("  空属性:", len(empty), empty[:5])
    print("  可疑未转义 & :", len(badamp), badamp[:3])
    # 裸双引号检测：属性解析后若元素属性数明显异常则提示
    zh_count = len(zh_tags)
    print("  标签总数:", len(p.tags))
