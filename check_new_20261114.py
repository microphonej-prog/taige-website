# -*- coding: utf-8 -*-
"""校验新文章：六语属性齐全、无裸引号截断、无占位符泄漏。"""
import re
import sys
from html.parser import HTMLParser

LANGS = ["zh", "en", "fr", "es", "ja", "ko"]
FILES = ["blog/gs1-digital-link-2d-barcode-labels.html", "blog/certificate-of-origin-apparel-trims.html"]


class P(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.bad = []
        self.count = 0
        self.attrs_seen = 0

    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        keys = set(d)
        has = [l for l in LANGS if "data-" + l in keys]
        self.count += 1
        self.attrs_seen += len(has)
        if "data-zh" in keys:
            miss = [l for l in LANGS if "data-" + l not in keys]
            if miss:
                self.bad.append((tag, miss, (d.get("data-zh") or "")[:40]))


ok = True
for f in FILES:
    s = open(f, encoding="utf-8").read()
    p = P()
    p.feed(s)
    print("%s  标签%d 属性组%d  缺语言元素%d" % (f, p.count, p.attrs_seen, len(p.bad)))
    for b in p.bad[:5]:
        print("   缺", b)
        ok = False
    # 裸引号检查：data-xx="" 或属性值里出现未转义的 ASCII 引号导致的畸形
    if re.search(r'data-(zh|en|fr|es|ja|ko)=""', s):
        print("   !! 存在空属性")
        ok = False
    # 占位符泄漏
    for ph in ["DESC_PLACEHOLDER", "euro-hole-retail", "OLD_SLUG"]:
        if ph in s:
            print("   !! 残留占位/旧 slug:", ph)
            ok = False
    # 标签配对初判
    for t in ["section", "div", "ul", "ol", "table"]:
        o = len(re.findall(r"<%s\b" % t, s))
        c = len(re.findall(r"</%s>" % t, s))
        if o != c:
            print("   !! 标签不配对 %s: %d/%d" % (t, o, c))
            ok = False
    # 正文长度
    zh = " ".join(re.findall(r'data-zh="([^"]*)"', s))
    plain = re.sub(r"<[^>]+>", "", zh)
    print("   中文正文（属性合计）字符数 %d" % len(re.sub(r"\s+", "", plain)))

print("结论:", "OK" if ok else "有问题")
sys.exit(0 if ok else 1)
