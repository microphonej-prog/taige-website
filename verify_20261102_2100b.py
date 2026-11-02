#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""校验 2026-11-02 21:00 补跑批次（v2：修正假报警）"""
import os, re, sys
from html.parser import HTMLParser

os.chdir(r"C:\Users\micro\taige-website")
LANGS = ["zh", "en", "fr", "es", "ja", "ko"]
SLUGS = ["garment-label-inhouse-printing-vs-outsourcing.html", "trim-order-currency-exchange-guide.html"]
TEXT_TAGS = {"p", "h1", "h2", "h3", "h4", "li", "td", "th", "div", "a", "span", "strong", "em"}
SIMPLIFIED = "这们说时业给对应还让没个为图页标准级认识开关闭证书费价买东车门问题实现机构种类别样那么经济"


class Checker(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.in_body = False
        self.missing = []
        self.seen = 0

    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        if tag == "section" and "article-body" in d.get("class", ""):
            self.in_body = True
            return
        if not self.in_body:
            return
        present = [l for l in LANGS if ("data-" + l) in d]
        if present and tag in TEXT_TAGS:
            self.seen += 1
            miss = [l for l in LANGS if l not in present]
            if miss:
                self.missing.append((tag, miss, (d.get("data-zh") or "")[:40]))


def attr_scan(s):
    bad = []
    for m in re.finditer(r'data-(?:zh|en|fr|es|ja|ko)=""', s):
        bad.append(("empty", m.group(0)))
    for m in re.finditer(r'data-(?:zh|en|fr|es|ja|ko)="[^"]*"[^ \t\r\n>]', s):
        bad.append(("glued", m.group(0)[:80]))
    return bad


ok = True
for slug in SLUGS:
    s = open(os.path.join("blog", slug), encoding="utf-8").read()
    c = Checker()
    c.feed(s)
    bad = attr_scan(s)
    print("=== %s" % slug)
    print("  六语属性元素: %d | 缺属性: %d | 畸形属性: %d" % (c.seen, len(c.missing), len(bad)))
    for m in c.missing[:5]:
        print("    MISSING", m)
    for b in bad[:5]:
        print("    BAD", b)
    if c.missing or bad:
        ok = False

    for lang in ("en", "fr", "es"):
        han = [v for v in re.findall(r'data-%s="([^"]*)"' % lang, s) if re.search(r'[\u4e00-\u9fff]', v)]
        print("  data-%s 含汉字条目: %d" % (lang, len(han)))
        if han:
            ok = False
            print("    e.g.", han[0][:60])
    for lang in ("ja", "ko"):
        vals = re.findall(r'data-%s="([^"]*)"' % lang, s)
        hits = [v for v in vals if any(ch in SIMPLIFIED for ch in v)]
        print("  data-%s 含简体专用字条目: %d" % (lang, len(hits)))
        if hits:
            ok = False
            print("    e.g.", hits[0][:60])

    links = re.findall(r'href="([a-z0-9\-]+\.html)"', s)
    broken = [l for l in sorted(set(links)) if not os.path.exists(os.path.join("blog", l))]
    print("  内链 %d 个，坏链: %s" % (len(set(links)), broken or "无"))
    if broken:
        ok = False
    print("  title:", re.search(r"<title[^>]*>(.*?)</title>", s, re.S).group(1)[:50])

idx = open("blog/index.html", encoding="utf-8").read()
after_grid = idx.split('<div class="post-grid">', 1)[1]
cards = re.findall(r'<a class="more" href="([^"]+)"', after_grid)
print("blog/index.html 前 4 张卡片:", cards[:4])
if cards[:2] != SLUGS:
    ok = False
    print("  !! 新卡片不在顶部")

sm = open("sitemap.xml", encoding="utf-8").read()
print("sitemap <loc> 总数:", sm.count("<loc>"))
for slug in SLUGS:
    n = len(re.findall(r"<loc>https://taigetag\.com/(?:[a-z]{2}/)?blog/%s</loc>" % re.escape(slug), sm))
    print("  %s: %d/6 URL" % (slug, n))
    if n != 6:
        ok = False

for lang in ["en", "ja", "ko", "fr", "es"]:
    missing = [x for x in SLUGS if not os.path.exists("%s/blog/%s" % (lang, x))]
    print("%s 语言文件: %s" % (lang, "齐全" if not missing else missing))
    if missing:
        ok = False

print("BUST_VERSION:", re.search(r'var BUST_VERSION = "(\d+)"', open("js/main.js", encoding="utf-8").read()).group(1))
print("RESULT:", "PASS" if ok else "FAIL")
sys.exit(0 if ok else 1)
