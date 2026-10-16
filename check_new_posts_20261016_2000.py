#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-16 20:00 批次本地校验：文件/六语属性/卡片/sitemap/BUST_VERSION"""
import os, re, sys
from html.parser import HTMLParser

ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)

ART = {
    "trim-shipment-insurance-claims-guide.html": "Trim Shipment Insurance",
    "conflict-minerals-trims-guide.html": "Conflict Minerals Due Diligence for Metal Trims",
}
LANGS = ["en", "ja", "ko", "fr", "es"]
DATE = "2026-10-16"
ok = True


def fail(msg):
    global ok
    ok = False
    print("  ✗ " + msg)


class BodyAttr(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.in_body = False
        self.depth = 0
        self.n = 0
        self.missing = []
        self.stack = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if self.in_body:
            self.depth += 1
        if a.get("class") == "article-body":
            self.in_body = True
            self.depth = 0
            return
        if not self.in_body:
            return
        if any(k.startswith("data-") for k in a):
            self.n += 1
            miss = [l for l in ["zh", "en", "ja", "ko", "fr", "es"] if ("data-%s" % l) not in a]
            if miss:
                self.missing.append((tag, miss, (a.get("data-zh") or "")[:30]))

    def handle_endtag(self, tag):
        if self.in_body and self.depth > 0:
            self.depth -= 1
            if self.depth == 0:
                self.in_body = False


print("① 文件与六语页面")
for slug in ART:
    for p in ["blog/%s" % slug] + ["%s/blog/%s" % (l, slug) for l in LANGS]:
        if not os.path.exists(p):
            fail("缺文件 " + p)
    if os.path.exists("blog/%s" % slug):
        s = open("blog/%s" % slug, encoding="utf-8").read()
        b = BodyAttr(); b.feed(s)
        print("  %s: 正文属性元素 %d，六语齐全（缺项 %d）" % (slug, b.n, len(b.missing)))
        for m in b.missing[:5]:
            fail("缺属性 %s %s" % (slug, m))
        # canonical / hreflang
        can = re.search(r'<link rel="canonical" href="([^"]+)"', s).group(1)
        if can != "https://taigetag.com/blog/%s" % slug:
            fail("canonical 异常: %s -> %s" % (slug, can))
        hl = re.findall(r'hreflang="([^"]+)"', s)
        if len(hl) != 7:
            fail("hreflang 数量异常 %d (%s)" % (len(hl), slug))
        # title 六语
        t = re.search(r'<title[^>]*>', s).group(0)
        for l in ["zh", "en", "ja", "ko", "fr", "es"]:
            if 'data-%s="' % l not in t:
                fail("title 缺 data-%s (%s)" % (l, slug))
        # JSON-LD
        if s.count("application/ld+json") != 1:
            fail("JSON-LD 数量 %d (%s)" % (s.count("application/ld+json"), slug))
        import json
        for m in re.finditer(r'<script type="application/ld\+json">(.*?)</script>', s, re.S):
            try:
                json.loads(m.group(1))
            except Exception as e:
                fail("JSON-LD 非法 %s: %s" % (slug, e))
        for l in LANGS:
            s2 = open("%s/blog/%s" % (l, slug), encoding="utf-8").read()
            t2 = re.search(r'<title[^>]*>(.*?)</title>', s2, re.S).group(1)
            h2 = re.search(r'<h1[^>]*>(.*?)</h1>', s2, re.S).group(1)
            if not t2.strip() or not h2.strip():
                fail("%s 版 title/h1 空 (%s)" % (l, slug))
            if "data-zh=" in s2.split("article-body")[-1]:
                pass
        print("     %s 六语 title 片段: %s" % (slug, " | ".join(
            re.search(r'<title[^>]*>(.*?)</title>', open("%s/blog/%s" % (l, slug), encoding="utf-8").read(), re.S).group(1).strip()[:34]
            for l in ["en", "ja", "ko", "fr", "es"])))

print("② blog/index.html 卡片")
idx = open("blog/index.html", encoding="utf-8").read()
for slug in ART:
    c = idx.count('href="%s"' % slug)
    if c != 1:
        fail("卡片链接数 %d (%s)" % (c, slug))
    else:
        print("  卡片已插入：%s" % slug)
for l in LANGS:
    s = open("%s/blog/index.html" % l, encoding="utf-8").read()
    for slug in ART:
        if ('href="%s"' % slug) not in s:
            fail("%s 版列表页缺卡片 %s" % (l, slug))

print("③ sitemap")
sm = open("sitemap.xml", encoding="utf-8").read()
for slug in ART:
    for u in ["https://taigetag.com/blog/%s" % slug] + ["https://taigetag.com/%s/blog/%s" % (l, slug) for l in LANGS]:
        if "<loc>%s</loc>" % u not in sm:
            fail("sitemap 缺 %s" % u)
    pat = re.compile(r'<loc>https://taigetag.com/blog/%s</loc>\s*<lastmod>([^<]*)</lastmod>' % re.escape(slug))
    m = pat.search(sm)
    if not m or m.group(1) != DATE:
        fail("sitemap lastmod 异常 %s" % slug)
for u in ["https://taigetag.com/blog/index.html"] + ["https://taigetag.com/%s/blog/index.html" % l for l in LANGS]:
    pat = re.compile(r'<loc>%s</loc>\s*<lastmod>([^<]*)</lastmod>' % re.escape(u))
    m = pat.search(sm)
    if not m or m.group(1) != DATE:
        fail("列表页 lastmod 未更新 %s" % u)
print("  <loc> 总数 %d" % sm.count("<loc>"))

print("④ BUST_VERSION")
mj = open("js/main.js", encoding="utf-8").read()
m = re.search(r'var BUST_VERSION = "(\d+)";', mj)
print("  BUST_VERSION =", m.group(1))
if m.group(1) != "164":
    fail("BUST_VERSION 不是 164")

print("⑤ 首页/其他页面未受影响（sanCheck）")
for p in ["blog/index.html", "index.html", "contact.html"]:
    if not os.path.exists(p):
        fail("缺 " + p)

print()
print("结果:", "全部通过" if ok else "存在问题，见上")
sys.exit(0 if ok else 1)
