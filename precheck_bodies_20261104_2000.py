#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""校验新正文文件的六语属性完整性（2026-11-04 20:00 批次）"""
import re, sys
from html.parser import HTMLParser

FILES = ["blog/_body_de.html", "blog/_body_es.html"]
LANGS = ["zh", "en", "ja", "ko", "fr", "es"]
CJK = re.compile(r'[\u3400-\u4dbf\u4e00-\u9fff]')
HANGUL = re.compile(r'[\uac00-\ud7af\u1100-\u11ff]')


class P(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.tags = []

    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        if any(k in d for k in ("data-zh", "data-en", "data-ja", "data-ko", "data-fr", "data-es")):
            self.tags.append((tag, d, self.getpos()))


bad = 0
for f in FILES:
    s = open(f, encoding="utf-8").read()
    p = P()
    p.feed(s)
    print("== %s  元素数=%d  文件大小=%.1fKB" % (f, len(p.tags), len(s.encode()) / 1024))
    if 'data-zh=""' in s or 'data-en=""' in s or 'data-ko=""' in s:
        print("  !! 存在空属性"); bad += 1
    for tag, d, pos in p.tags:
        miss = [l for l in LANGS if not d.get("data-" + l, "").strip()]
        if miss:
            print("  !! 行%d <%s> 缺 %s" % (pos[0], tag, miss)); bad += 1
        ko = d.get("data-ko", "")
        if CJK.search(ko) or HANGUL.search(d.get("data-ja", "")):
            print("  !! 行%d <%s> 语言污染 ko=%s ja=%s" % (pos[0], tag,
                  "有汉字" if CJK.search(ko) else "", "有韩文" if HANGUL.search(d.get("data-ja", "")) else ""))
            bad += 1
        for l in ("en", "fr", "es"):
            v = d.get("data-" + l, "")
            if CJK.search(v):
                print("  !! 行%d <%s> data-%s 含汉字: %s" % (pos[0], tag, l, v[:40])); bad += 1
    # 中文正文字数（可见文本，粗略）
    body = re.sub(r'<[^>]+>', '', s)
    print("  可见中文字数≈%d" % len(CJK.findall(body)))

print("问题总数:", bad)
sys.exit(0 if bad == 0 else 1)
