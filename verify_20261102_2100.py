#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""校验 2026-11-02 21:00 补跑批次"""
import os, re, sys, html
from html.parser import HTMLParser

os.chdir(r"C:\Users\micro\taige-website")
LANGS = ["zh", "en", "fr", "es", "ja", "ko"]
SLUGS = ["garment-label-inhouse-printing-vs-outsourcing.html", "trim-order-currency-exchange-guide.html"]
TEXT_TAGS = {"p", "h1", "h2", "h3", "h4", "li", "td", "th", "div", "a", "span", "strong", "em"}


class Checker(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.depth_body = 0
        self.in_body = False
        self.missing = []
        self.seen = 0

    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        cls = d.get("class", "")
        if tag == "section" and "article-body" in cls:
            self.in_body = True
            return
        if not self.in_body:
            return
        present = [l for l in LANGS if ("data-" + l) in d]
        if not present:
            return
        if tag in TEXT_TAGS:
            self.seen += 1
            miss = [l for l in LANGS if l not in present]
            if miss:
                self.missing.append((tag, miss, (d.get("data-zh") or "")[:40]))


def attr_scan(s):
    """找出畸形属性：data-xx="" 空值 或 属性值内含未转义裸引号导致截断"""
    bad = []
    for m in re.finditer(r'data-(?:zh|en|fr|es|ja|ko)=""', s):
        bad.append(("empty", s[max(0, m.start() - 60):m.start() + 20]))
    # 引号不配对的粗略检测：属性值以双引号开头却紧跟另一个双引号
    for m in re.finditer(r'data-(?:zh|en|fr|es|ja|ko)="[^"]*"[^ >]', s):
        bad.append(("glued", m.group(0)[:60]))
    return bad


ok = True
for slug in SLUGS:
    p = os.path.join("blog", slug)
    s = open(p, encoding="utf-8").read()
    c = Checker()
    c.feed(s)
    bad = attr_scan(s)
    print("=== %s" % slug)
    print("  六语属性元素: %d, 缺属性元素: %d, 畸形属性: %d" % (c.seen, len(c.missing), len(bad)))
    for m in c.missing[:5]:
        print("    MISSING", m)
    for b in bad[:5]:
        print("    BAD", b)
    if c.missing or bad:
        ok = False
    # 语言残留：ja/ko 值里不应有大段中文
    for lang in ("ja", "ko"):
        vals = re.findall(r'data-%s="([^"]*)"' % lang, s)
        han = sum(1 for v in vals if len(re.findall(r'[\u4e00-\u9fff]', v)) > 40)
        print("  data-%s 值中中文占比过高条目: %d / %d" % (lang, han, len(vals)))
    # 内链存在性
    links = re.findall(r'href="([a-z0-9\-]+\.html)"', s)
    for l in sorted(set(links)):
        if not os.path.exists(os.path.join("blog", l)):
            print("  BROKEN LINK:", l)
            ok = False
    # desc / title 存在
    print("  title:", re.search(r"<title[^>]*>(.*?)</title>", s, re.S).group(1)[:60])
    print("  canonical:", re.search(r'rel="canonical" href="([^"]+)"', s).group(1))

# 卡片
idx = open("blog/index.html", encoding="utf-8").read()
grid = idx.split('<div class="post-grid">', 1)[1][:2000]
for slug in SLUGS:
    print("card %s in top region: %s" % (slug, ('href="%s"' % slug) in grid))

# sitemap
sm = open("sitemap.xml", encoding="utf-8").read()
print("sitemap loc total:", sm.count("<loc>"))
for slug in SLUGS:
    n = len(re.findall(r"<loc>https://taigetag\.com/(?:[a-z]{2}/)?blog/%s</loc>" % re.escape(slug), sm))
    print("  %s urls: %d (expect 6)" % (slug, n))
    if n != 6:
        ok = False

# 各语言文件
for lang in ["en", "ja", "ko", "fr", "es"]:
    for slug in SLUGS:
        p = "%s/blog/%s" % (lang, slug)
        exists = os.path.exists(p)
        if not exists:
            print("MISSING FILE", p)
            ok = False
    print("%s: 2 files -> %s" % (lang, all(os.path.exists("%s/blog/%s" % (lang, s)) for s in SLUGS)))

print("BUST_VERSION:", re.search(r'var BUST_VERSION = "(\d+)"', open("js/main.js", encoding="utf-8").read()).group(1))
print("RESULT:", "PASS" if ok else "FAIL")
sys.exit(0 if ok else 1)
