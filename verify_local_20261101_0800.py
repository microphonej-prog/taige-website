#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-11-01 08:00 批次本地校验：六语属性完整性、卡片、sitemap、canonical/hreflang、语言纯净度、链接"""
import os, re, sys
from html.parser import HTMLParser

ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)

SLUGS = ["ecommerce-mailer-box-guide.html", "packaging-tape-guide.html"]
LANGS = ["en", "ja", "ko", "fr", "es"]
LANGS_ALL = ["zh"] + LANGS
SITEMAP_DATE = "2026-11-01"
HAN = re.compile(r"[\u4e00-\u9fff]")
CJK = re.compile(r"[\u4e00-\u9fff\u3040-\u30ff\uac00-\ud7af]")


class BodyParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.in_body = False
        self.elems = []

    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        if tag == "section" and "article-body" in (d.get("class") or ""):
            self.in_body = True
            return
        if self.in_body:
            self.elems.append((tag, d))

    def handle_endtag(self, tag):
        if self.in_body and tag == "section":
            self.in_body = False


ok = True
print("== 文件存在性 ==")
for slug in SLUGS:
    for lang in LANGS_ALL:
        p = ("blog/%s" % slug) if lang == "zh" else ("%s/blog/%s" % (lang, slug))
        if not os.path.exists(p):
            print("缺失文件:", p); ok = False

print("== 六语属性 / 字数 ==")
for slug in SLUGS:
    s = open("blog/%s" % slug, encoding="utf-8").read()
    p = BodyParser(); p.feed(s)
    zh = [(t, d) for t, d in p.elems if "data-zh" in d]
    miss = {l: sum(1 for _, d in zh if "data-" + l not in d) for l in LANGS}
    bad = {k: v for k, v in miss.items() if v}
    empty = len(re.findall(r'data-(?:zh|en|fr|es|ja|ko)=""', s))
    chars = sum(len(HAN.findall(d.get("data-zh", ""))) for _, d in zh)
    print("%-40s data-zh元素=%-3d 缺语言=%s 空属性=%d 中文字数=%d"
          % (slug, len(zh), bad or "无", empty, chars))
    if bad or empty:
        ok = False
    if not (600 <= chars <= 1500):
        print("   !! 中文字数超出 600-1500:", chars); ok = False
    # 旧批次的坏链接不应出现在新文章
    if 'href="blog/index.html"' in s:
        print("   !! 存在坏链接 href=\"blog/index.html\""); ok = False

print("== 各语言静态 title / canonical / 正文语言纯净度 ==")
for lang in LANGS:
    for slug in SLUGS:
        p = "%s/blog/%s" % (lang, slug)
        s = open(p, encoding="utf-8").read()
        t = re.search(r"<title>(.*?)</title>", s, re.S).group(1)
        canon = re.search(r'<link rel="canonical" href="([^"]*)"', s).group(1)
        body = s[s.index('<section class="article-body">'):s.index("</main>")]
        txt = re.sub(r"<[^>]+>", " ", body)
        cjk = len(CJK.findall(txt))
        print("%-3s %-40s CJK正文字符=%-4d canon=%s" % (lang, slug[:38], cjk, canon))
        print("    title: %s" % t[:78])
        if cjk and lang in ("en", "fr", "es"):
            print("    !! 正文混入中日韩字符"); ok = False

print("== 卡片 ==")
for lang in LANGS_ALL:
    p = "blog/index.html" if lang == "zh" else "%s/blog/index.html" % lang
    s = open(p, encoding="utf-8").read()
    hits = [slug for slug in SLUGS if 'href="%s"' % slug in s]
    print("卡片 %-3s %s" % (lang, "OK 2/2" if len(hits) == 2 else "缺失 %s" % hits))
    if len(hits) != 2:
        ok = False
    grid = s[s.index('<div class="post-grid">'):]
    first = re.search(r'<article class="post-card">.*?href="([^"]*)"', grid, re.S)
    print("   首张卡片 href: %s" % (first.group(1) if first else "无"))

print("== sitemap ==")
sm = open("sitemap.xml", encoding="utf-8").read()
urls = ["https://taigetag.com/blog/%s" % x for x in SLUGS] + \
       ["https://taigetag.com/%s/blog/%s" % (l, x) for x in SLUGS for l in LANGS]
missing = [u for u in urls if "<loc>%s</loc>" % u not in sm]
print("新 URL %d/%d 存在 %s" % (len(urls) - len(missing), len(urls), "OK" if not missing else missing))
if missing:
    ok = False
for u in ["https://taigetag.com/blog/index.html"] + ["https://taigetag.com/%s/blog/index.html" % l for l in LANGS]:
    m = re.search(r'<loc>%s</loc>\s*<lastmod>([^<]*)</lastmod>' % re.escape(u), sm)
    if not m or m.group(1) != SITEMAP_DATE:
        print("   !! blog index lastmod 未更新:", u); ok = False

print("== hreflang 一致性（新文章） ==")
s = open("blog/%s" % SLUGS[0], encoding="utf-8").read()
print(sorted(re.findall(r'hreflang="([^"]*)"', s)))
print("BUST_VERSION:", re.search(r'var BUST_VERSION = "(\d+)";', open("js/main.js", encoding="utf-8").read()).group(1))
print("结果:", "通过" if ok else "有问题")
sys.exit(0 if ok else 1)
