#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""生成后校验：12 个页面 title/h1/desc 语言正确、语言页无中文残留、卡片与 sitemap"""
import os, re, sys
from html.parser import HTMLParser

SLUGS = ["magnetic-trims-air-freight-guide.html", "trim-label-consistency-audit-guide.html"]
LANGS = ["", "en", "ja", "ko", "fr", "es"]
CJK = re.compile(r'[\u4e00-\u9fff]')
KANA = re.compile(r'[\u3040-\u30ff]')
HANGUL = re.compile(r'[\uac00-\ud7af]')

print("== 12 个页面 ==")
for slug in SLUGS:
    for l in LANGS:
        p = ("blog/%s" % slug) if l == "" else ("%s/blog/%s" % (l, slug))
        s = open(p, encoding="utf-8").read()
        t = re.search(r'<title[^>]*>(.*?)</title>', s, re.S).group(1).strip()
        h1 = re.search(r'<h1[^>]*>(.*?)</h1>', s, re.S).group(1).strip()
        d = re.search(r'<meta name="description"[^>]*?content="([^"]*)"', s, re.S).group(1)
        body = s[s.index('class="article-body"'):s.index('</main>')]
        txt = re.sub(r'<[^>]+>', ' ', body)
        flags = []
        if 'data-zh=' in body or 'data-en=' in body:
            flags.append("残留data属性")
        if l in ("en", "fr", "es") and CJK.search(txt):
            flags.append("正文含中文")
        if l == "ja" and not KANA.search(txt):
            flags.append("日文无假名")
        if l == "ko" and not HANGUL.search(txt):
            flags.append("韩文无谚文")
        if "TAGE" not in t:
            flags.append("标题缺TAGE")
        if "magnetic-trims" in slug and l == "ja" and "磁性" not in t:
            flags.append("JA标题异常")
        print("%-42s %-4s desc=%3d  %s  %s" % (slug, l or "zh", len(d), t[:52], "OK" if not flags else ",".join(flags)))
        print("      h1: %s" % h1[:70])

print("\n== blog/index.html 卡片 ==")
for l in LANGS:
    p = "blog/index.html" if l == "" else "%s/blog/index.html" % l
    s = open(p, encoding="utf-8").read()
    print("%-6s %s" % (l or "zh", ["%s:%d" % (sl[:18], s.count(sl)) for sl in SLUGS]))

print("\n== sitemap ==")
sm = open("sitemap.xml", encoding="utf-8").read()
for slug in SLUGS:
    urls = re.findall(r'<loc>([^<]*%s)</loc>' % re.escape(slug), sm)
    print("%s -> %d 个 URL" % (slug, len(urls)))
    for u in urls:
        print("   ", u)
i = sm.index("https://taigetag.com/blog/index.html")
print("blog/index lastmod:", re.search(r'<lastmod>([^<]*)</lastmod>', sm[i:i + 200]).group(1))
print("\nBUST_VERSION:", re.search(r'BUST_VERSION = "(\d+)"', open("js/main.js", encoding="utf-8").read()).group(1))
print("总 <loc>:", sm.count("<loc>"))
