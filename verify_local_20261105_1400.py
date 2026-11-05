#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-11-05 14:00 批次本地校验：文件/卡片/sitemap/六语 title/属性完整性/JSON-LD"""
import os, re, sys, json, html
from html.parser import HTMLParser

ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)

SLUGS = ["nordic-apparel-labelling-compliance.html", "garment-trims-low-temperature-performance.html"]
LANGS = ["en", "ja", "ko", "fr", "es"]
CJK = re.compile(r"[\u4e00-\u9fff]")
KANA = re.compile(r"[\u3040-\u30ff]")
HANGUL = re.compile(r"[\uac00-\ud7af]")
ok = True


def fail(msg):
    global ok
    ok = False
    print("  ✗ " + msg)


def title_of(path):
    s = open(path, encoding="utf-8").read()
    m = re.search(r"<title[^>]*>(.*?)</title>", s, re.S)
    return html.unescape(m.group(1)).strip() if m else ""


print("== 文件与 title")
for slug in SLUGS:
    for lang in ["zh"] + LANGS:
        p = "blog/%s" % slug if lang == "zh" else "%s/blog/%s" % (lang, slug)
        if not os.path.exists(p):
            fail("缺文件 %s" % p)
            continue
        t = title_of(p)
        if not t:
            fail("%s 无 title" % p)
        if lang == "en" and CJK.search(t):
            fail("%s 英文 title 含汉字：%s" % (p, t))
        if lang == "ko" and not HANGUL.search(t):
            fail("%s 韩文 title 无韩文：%s" % (p, t))
        if lang == "ja" and not KANA.search(t):
            fail("%s 日文 title 无假名：%s" % (p, t))
        print("  %-52s %s" % (p, t[:60]))

print("\n== 六语属性完整性（正文 data-zh 元素）")


class P(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.nodes = []

    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        if any(k.startswith("data-") for k in d):
            self.nodes.append((tag, d, self.getpos()[0]))


for slug in SLUGS:
    p = "blog/%s" % slug
    s = open(p, encoding="utf-8").read()
    body = s[s.index('<section class="article-body">'):s.index("</main>")]
    par = P()
    par.feed(body)
    miss = []
    for tag, d, line in par.nodes:
        if "data-zh" not in d:
            continue
        for l in ["en", "ja", "ko", "fr", "es"]:
            if not (d.get("data-" + l) or "").strip():
                miss.append((line, l))
    print("  %-52s 元素 %d，缺属性 %d" % (slug, len(par.nodes), len(miss)))
    if miss:
        fail("缺属性 %s" % miss[:5])

print("\n== 生成语言页语言纯度")
for slug in SLUGS:
    for lang in LANGS:
        p = "%s/blog/%s" % (lang, slug)
        s = open(p, encoding="utf-8").read()
        body = s[s.index('class="article-body"'):s.index("</main>")]
        txt = re.sub(r"<[^>]+>", " ", body)
        cjk = CJK.findall(txt)
        if lang in ("en", "fr", "es") and cjk:
            fail("%s 正文含汉字 %d 个：%s" % (p, len(cjk), "".join(cjk[:12])))
        if lang == "ko":
            if cjk:
                fail("%s 韩文页含汉字 %d 个：%s" % (p, len(cjk), "".join(cjk[:12])))
            if not HANGUL.search(txt):
                fail("%s 韩文页无韩文" % p)
        if lang == "ja" and not KANA.search(txt):
            fail("%s 日文页无假名" % p)
print("  完成")

print("\n== canonical 与 hreflang")
for slug in SLUGS:
    for lang in ["zh"] + LANGS:
        p = "blog/%s" % slug if lang == "zh" else "%s/blog/%s" % (lang, slug)
        s = open(p, encoding="utf-8").read()
        m = re.search(r'<link rel="canonical" href="([^"]+)"', s)
        if not m:
            fail("%s 无 canonical" % p)
            continue
        exp = "https://taigetag.com/blog/%s" % slug if lang == "zh" else "https://taigetag.com/%s/blog/%s" % (lang, slug)
        if m.group(1) != exp:
            fail("%s canonical=%s 应为 %s" % (p, m.group(1), exp))
        n = len(re.findall(r'rel="alternate" hreflang=', s))
        if n != 7:
            fail("%s hreflang 数量 %d" % (p, n))
print("  完成")

print("\n== JSON-LD")
for slug in SLUGS:
    p = "blog/%s" % slug
    s = open(p, encoding="utf-8").read()
    blocks = re.findall(r'<script type="application/ld\+json">(.*?)</script>', s, re.S)
    if not blocks:
        fail("%s 无 JSON-LD" % p)
    for b in blocks:
        try:
            json.loads(b)
        except Exception as e:
            fail("%s JSON-LD 非法: %s" % (p, e))
    if "nordic" in slug and blocks:
        print("  headline:", re.search(r'"headline": "([^"]*)"', blocks[0]).group(1)[:40])
print("  完成")

print("\n== blog/index.html 卡片")
for lang in ["zh"] + LANGS:
    p = "blog/index.html" if lang == "zh" else "%s/blog/index.html" % lang
    s = open(p, encoding="utf-8").read()
    for slug in SLUGS:
        if slug not in s:
            fail("%s 缺卡片 %s" % (p, slug))
    cards = s.count('<article class="post-card">')
    print("  %-30s 卡片 %d" % (p, cards))

print("\n== sitemap")
sm = open("sitemap.xml", encoding="utf-8").read()
for slug in SLUGS:
    for u in ["https://taigetag.com/blog/%s" % slug] + ["https://taigetag.com/%s/blog/%s" % (l, slug) for l in LANGS]:
        if "<loc>%s</loc>" % u not in sm:
            fail("sitemap 缺 %s" % u)
    m = re.search(r"<loc>https://taigetag.com/blog/%s</loc>\s*<lastmod>([^<]+)</lastmod>" % re.escape(slug), sm)
    print("  %s lastmod=%s" % (slug, m.group(1) if m else "?"))
print("  <loc> 总数 %d" % sm.count("<loc>"))
for u in ["https://taigetag.com/blog/index.html"] + ["https://taigetag.com/%s/blog/index.html" % l for l in LANGS]:
    m = re.search(r"<loc>%s</loc>\s*<lastmod>([^<]+)</lastmod>" % re.escape(u), sm)
    if not m or m.group(1) != "2026-11-05":
        fail("blog index lastmod 未更新 %s" % u)
print("  blog index lastmod 检查完成")

print("\n== BUST_VERSION")
mj = open("js/main.js", encoding="utf-8").read()
print("  ", re.search(r'var BUST_VERSION = "[^"]*";', mj).group(0))

print("\n结论：", "全部通过" if ok else "存在问题")
sys.exit(0 if ok else 1)
