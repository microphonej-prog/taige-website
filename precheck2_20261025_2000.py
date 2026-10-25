#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""预检：只针对带 data-zh 的元素检查其余五语；裸 & 检查；中文字数对比"""
import re
from html.parser import HTMLParser

LANGS = ["en", "ja", "ko", "fr", "es"]
FILES = ["blog/_body_jersey.html", "blog/_body_rental.html", "blog/_body_tyvek.html"]


class P(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.issues = []
        self.n = 0

    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        if "data-zh" not in d:
            return
        self.n += 1
        for l in LANGS + ["zh"]:
            if d.get("data-" + l, "").strip() == "":
                self.issues.append("%s data-%s 缺失或为空" % (tag, l))
        for l in LANGS + ["zh"]:
            v = d.get("data-" + l, "")
            for m in re.finditer(r"&(?!(?:amp|lt|gt|quot|nbsp|#\d+|#x[0-9a-fA-F]+);)", v):
                self.issues.append("%s data-%s 裸&: ...%s" % (tag, l, v[max(0, m.start() - 25):m.start() + 8]))


for f in FILES:
    s = open(f, encoding="utf-8").read()
    p = P()
    p.feed(s)
    zh = "".join(re.findall(r'data-zh="([^"]*)"', s))
    zh = re.sub(r"<[^>]+>", "", zh)
    print("== %s  六语元素=%d  中文净字数=%d  字节=%d" % (f, p.n, len(zh), len(s.encode("utf-8"))))
    if p.issues:
        for i in p.issues[:15]:
            print("   ! " + i)
        print("   问题数:", len(p.issues))
    else:
        print("   通过（六语齐全，无裸 &）")
    bad = re.findall(r'data-(?:zh|en|ja|ko|fr|es)=""[^ "\s]', s)
    print("   引号畸形:", len(bad))
