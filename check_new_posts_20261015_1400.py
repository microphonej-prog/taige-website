#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-15 下午批次：本地六语完整性校验"""
import os, re, json, subprocess, sys, html
from html.parser import HTMLParser

ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)
LANGS = ["en", "ja", "ko", "fr", "es"]
SLUGS = ["ribbon-trims-guide.html", "eu-green-claims-apparel-labels.html"]
DATE = "2026-10-15"
fail = []


def chk(cond, msg):
    print(("  OK  " if cond else "  FAIL") + "  " + msg)
    if not cond:
        fail.append(msg)


class P(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.tags = []
        self.in_article = 0
        self.body_tags = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        self.tags.append((tag, a))
        if tag == "section" and "article-body" in (a.get("class") or ""):
            self.in_article = 1
        elif self.in_article:
            if tag == "section":
                self.in_article = 0
            self.body_tags.append((tag, a))


print("== 1) 文件存在性 ==")
for s in SLUGS:
    for p in ["blog/%s" % s] + ["%s/blog/%s" % (l, s) for l in LANGS]:
        chk(os.path.exists(p), "存在 %s" % p)

print("== 2) 中文根页 head/结构 ==")
for s in SLUGS:
    src = open("blog/%s" % s, encoding="utf-8").read()
    t = re.search(r"<title ([^>]*)>([^<]*)</title>", src, re.S)
    attrs = dict(re.findall(r'data-([a-z]{2})="([^"]*)"', t.group(1)))
    chk(len(attrs) >= 6, "%s title 六语属性 %d" % (s, len(attrs)))
    chk(attrs.get("zh") == t.group(2), "%s title 正文=繁体中文版" % s)
    m = re.search(r'<meta name="description"([^>]*)>', src, re.S)
    da = dict(re.findall(r'data-([a-z]{2})="([^"]*)"', m.group(1)))
    c = re.search(r'content="([^"]*)"', m.group(1))
    chk(len(da) >= 6 and c is not None, "%s description 六语+content" % s)
    chk(c and c.group(1) == da.get("zh"), "%s description content=繁体中文版" % s)
    can = re.search(r'<link rel="canonical" href="([^"]*)"', src)
    chk(can and can.group(1) == "https://taigetag.com/blog/%s" % s,
        "%s canonical %s" % (s, can.group(1) if can else "无"))
    hl = re.findall(r'<link rel="alternate" hreflang="([^"]*)"', src)
    chk(set(hl) >= {"zh-Hant", "en", "fr", "es", "ja", "ko", "x-default"},
        "%s hreflang %s" % (s, sorted(hl)))
    h1 = re.search(r"<h1 ([^>]*)>", src)
    h1a = dict(re.findall(r'data-([a-z]{2})="([^"]*)"', h1.group(1)))
    chk(len(h1a) >= 6, "%s h1 六语属性 %d" % (s, len(h1a)))
    p = P()
    p.feed(src)
    miss = 0
    tot = 0
    for tag, a in p.body_tags:
        has = [k for k in a if k.startswith("data-") and k[5:] in ["zh", "en", "ja", "ko", "fr", "es"]]
        if not has:
            continue
        tot += 1
        for l in ["zh", "en", "ja", "ko", "fr", "es"]:
            if ("data-%s" % l) not in a or not a["data-%s" % l].strip():
                miss += 1
    chk(miss == 0, "%s 正文带data元素 %d 个，缺/空 data-fr|es|ja|ko|en = %d" % (s, tot, miss))
    ok = 0
    for blk in re.findall(r'<script type="application/ld\+json">(.*?)</script>', src, re.S):
        try:
            json.loads(blk)
            ok += 1
        except Exception as e:
            chk(False, "%s JSON-LD 解析失败 %s" % (s, e))
    chk(ok >= 1, "%s JSON-LD 可解析块数 %d" % (s, ok))
    # 相关文章链接目标存在
    for href in re.findall(r'<a href="([a-z0-9\-]+\.html)"', src):
        chk(os.path.exists("blog/%s" % href), "%s 内链 %s 存在" % (s, href))

print("== 3) 各语言页 title/description 是否取到对应语言 ==")
for s in SLUGS:
    src = open("blog/%s" % s, encoding="utf-8").read()
    root_title = re.search(r"<title ([^>]*)>", src, re.S).group(1)
    root_desc = re.search(r'<meta name="description"([^>]*)>', src, re.S).group(1)
    for l in LANGS:
        tgt = "%s/blog/%s" % (l, s)
        t = open(tgt, encoding="utf-8").read()
        tt = re.search(r"<title[^>]*>([^<]*)</title>", t, re.S).group(1)
        exp = re.search(r'data-%s="([^"]*)"' % l, root_title).group(1)
        chk(html.unescape(tt) == html.unescape(exp), "%s title=%s 语" % (tgt, l))
        dd = re.search(r'<meta name="description"[^>]*content="([^"]*)"', t, re.S).group(1)
        edd = re.search(r'data-%s="([^"]*)"' % l, root_desc).group(1)
        chk(html.unescape(dd) == html.unescape(edd), "%s description=%s 语" % (tgt, l))

print("== 4) 列表页卡片 ==")
idx = open("blog/index.html", encoding="utf-8").read()
for s in SLUGS:
    chk('href="%s"' % s in idx, "blog/index.html 含卡片 %s" % s)
    pos = idx.index('href="%s"' % s)
    card_start = idx.rindex("<article", 0, pos)
    card = idx[card_start:pos + 200]
    n = len(set(re.findall(r"data-([a-z]{2})=", card)))
    chk(n >= 6, "%s 卡片六语属性 %d" % (s, n))
for l in LANGS:
    t = open("%s/blog/index.html" % l, encoding="utf-8").read()
    for s in SLUGS:
        chk('href="%s"' % s in t, "%s/blog/index.html 含卡片 %s" % (l, s))

print("== 5) sitemap ==")
sm = open("sitemap.xml", encoding="utf-8").read()
for s in SLUGS:
    for u in ["https://taigetag.com/blog/%s" % s] + ["https://taigetag.com/%s/blog/%s" % (l, s) for l in LANGS]:
        chk("<loc>%s</loc>" % u in sm, "sitemap 含 %s" % u)
    blk = re.search(r"<loc>https://taigetag.com/blog/%s</loc>\s*<lastmod>([^<]*)</lastmod>" % re.escape(s), sm)
    chk(blk and blk.group(1) == DATE, "%s lastmod=%s" % (s, blk.group(1) if blk else "?"))
for u in ["https://taigetag.com/blog/index.html"] + ["https://taigetag.com/%s/blog/index.html" % l for l in LANGS]:
    blk = re.search(r"<loc>%s</loc>\s*<lastmod>([^<]*)</lastmod>" % re.escape(u), sm)
    chk(blk and blk.group(1) == DATE, "blog index lastmod %s = %s" % (u, blk.group(1) if blk else "?"))
print("   sitemap <loc> 总数:", sm.count("<loc>"))

print("== 6) JS 语法 & BUST_VERSION ==")
r = subprocess.run(["node", "--check", "js/main.js"], capture_output=True, text=True)
chk(r.returncode == 0, "node --check js/main.js %s" % (r.stderr.strip()[:120] or "ok"))
mj = open("js/main.js", encoding="utf-8").read()
chk('var BUST_VERSION = "160";' in mj, "BUST_VERSION=160")

print()
print("FAIL 数:", len(fail))
for f in fail:
    print("  -", f)
sys.exit(1 if fail else 0)
