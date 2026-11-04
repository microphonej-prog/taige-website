#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""批次校验：属性完整性（六语）、无畸形属性、卡片、sitemap、标题长度"""
import os, re, sys
from html.parser import HTMLParser

os.chdir(os.path.dirname(os.path.abspath(__file__)))
SLUGS = ["trims-ph-value-skin-safety.html", "garment-trims-sewing-equipment-guide.html"]
LANGS = ["zh", "en", "ja", "ko", "fr", "es"]
TAGS = {"p", "h2", "h3", "li", "td", "th", "div", "a", "span"}
fail = 0


class Checker(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.in_body = 0
        self.problems = []
        self.count = 0

    def handle_starttag(self, tag, attrs):
        if tag == "section" and dict(attrs).get("class") == "article-body":
            self.in_body = 1
            return
        if not self.in_body or tag not in TAGS:
            return
        d = dict(attrs)
        if "data-zh" not in d:
            return
        self.count += 1
        missing = [l for l in LANGS if not d.get("data-" + l)]
        if missing:
            self.problems.append((tag, d.get("data-zh")[:36], missing))


for slug in SLUGS:
    p = "blog/" + slug
    s = open(p, encoding="utf-8").read()
    # 畸形属性：data-xx=""text" / 裸引号
    bad = re.findall(r'data-(?:zh|en|ja|ko|fr|es)=""', s)
    c = Checker()
    c.feed(s)
    print("%s  元素=%d  缺语言=%d  畸形属性=%d" % (slug, c.count, len(c.problems), len(bad)))
    for pr in c.problems[:10]:
        print("   !", pr)
    if c.problems or bad:
        fail += 1
    # title / desc
    m = re.search(r"<title([^>]*)>(.*?)</title>", s, re.S)
    print("   title_zh:", m.group(2)[:70])
    d = re.search(r'<meta name="description"([^>]*)>', s, re.S)
    print("   desc 语言数:", len(re.findall(r'data-(?:zh|en|ja|ko|fr|es)=', d.group(1))))
    # 正文中文量
    zh = re.findall(r'data-zh="([^"]*)"', s)
    print("   data-zh 字符总量:", sum(len(x) for x in zh))

# 列表页卡片
idx = open("blog/index.html", encoding="utf-8").read()
for slug in SLUGS:
    n = idx.count('href="%s"' % slug)
    print("卡片 %s -> %d" % (slug, n))
    if n != 1:
        fail += 1

# sitemap
sm = open("sitemap.xml", encoding="utf-8").read()
for slug in SLUGS:
    for l in ["", "en/", "ja/", "ko/", "fr/", "es/"]:
        u = "https://taigetag.com/%sblog/%s" % (l, slug)
        if ("<loc>%s</loc>" % u) not in sm:
            print("   !! sitemap 缺", u)
            fail += 1
print("sitemap <loc> 总数:", sm.count("<loc>"))
print("BUST:", re.search(r'var BUST_VERSION = "(\d+)"', open("js/main.js", encoding="utf-8").read()).group(1))
print("RESULT:", "FAIL" if fail else "PASS")
