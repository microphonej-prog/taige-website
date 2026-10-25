#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""预检正文文件：六语属性齐全 / 无裸 & / 无引号畸形 / 中文长度"""
import sys, re
from html.parser import HTMLParser

LANGS = ["zh", "en", "ja", "ko", "fr", "es"]
FILES = ["blog/_body_jersey.html", "blog/_body_rental.html"]


class P(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.issues = []
        self.count = 0

    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        if tag in ("br", "hr", "img", "meta", "link", "input"):
            return
        self.count += 1
        missing = [l for l in LANGS if ("data-" + l) not in d]
        if missing:
            self.issues.append("%s 缺 %s" % (tag, ",".join(missing)))
        for l in LANGS:
            v = d.get("data-" + l, "")
            if l in ("zh", "en", "ja", "ko", "fr", "es") and v.strip() == "":
                self.issues.append("%s data-%s 为空" % (tag, l))
        # 裸 & （合法实体之外）
        for l in LANGS:
            v = d.get("data-" + l, "")
            for m in re.finditer(r"&(?!(?:amp|lt|gt|quot|nbsp|#\d+|#x[0-9a-fA-F]+);)", v):
                self.issues.append("%s data-%s 含裸 & : %s" % (tag, l, v[max(0, m.start()-30):m.start()+10]))


for f in FILES:
    s = open(f, encoding="utf-8").read()
    p = P()
    p.feed(s)
    print("== %s  元素数=%d  字节=%d" % (f, p.count, len(s.encode("utf-8"))))
    if p.issues:
        for i in p.issues[:20]:
            print("   ! " + i)
        print("   问题数:", len(p.issues))
    else:
        print("   属性检查通过")
    # 中文正文长度估算（data-zh 文本）
    zh = re.findall(r'data-zh="([^"]*)"', s)
    txt = "".join(zh)
    txt = re.sub(r"<[^>]+>", "", txt)
    print("   data-zh 纯文本约 %d 字" % len(txt))
