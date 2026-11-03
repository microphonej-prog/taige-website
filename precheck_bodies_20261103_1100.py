#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""校验两篇新正文文件的六语属性完整性（用 HTMLParser 逐属性判断，避免正则在属性值内的 > 截断）"""
import sys
from html.parser import HTMLParser

LANGS = ["zh", "en", "ja", "ko", "fr", "es"]
FILES = ["blog/_body_metamerism.html", "blog/_body_curl.html"]


class P(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack = []
        self.issues = []
        self.count = 0
        self.tags = {}

    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        if tag in ("br", "img", "meta", "link", "input", "hr"):
            return
        self.count += 1
        self.tags[tag] = self.tags.get(tag, 0) + 1
        missing = [l for l in LANGS if ("data-" + l) not in d]
        if missing:
            self.issues.append("%s 缺 %s" % (tag, ",".join(missing)))


for f in FILES:
    s = open(f, encoding="utf-8").read()
    p = P()
    p.feed(s)
    print("== %s  元素数=%d  类型=%s" % (f, p.count, p.tags))
    print("   缺语言属性的元素: %d" % len(p.issues))
    for i in p.issues[:10]:
        print("     -", i)
    # 裸引号体检：属性值里出现 " 会破坏解析，用简单计数比对
    print("   data-zh 出现次数: %d" % s.count("data-zh="))
