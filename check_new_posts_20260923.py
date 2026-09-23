#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-09-23 上午批次交付前校验（六语：zh-Hant 根 + en/ja/ko/fr/es）。
用法: python check_new_posts_20260923.py
"""
import re, os, sys, json
from html.parser import HTMLParser

sys.stdout.reconfigure(encoding='utf-8')
ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)

SLUGS = ["paper-bag-window-guide.html", "trims-kitting-guide.html"]
LANGS = ["en", "ja", "ko", "fr", "es"]
DATE = "2026-09-23"
fails = []


def fail(msg):
    fails.append(msg)
    print("  ✗ %s" % msg)


class Collector(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.in_body = False
        self.tags = []

    def handle_starttag(self, tag, attrs):
        d = {k.lower(): (v or "") for k, v in attrs}
        if tag == "section" and d.get("class", "").startswith("article-body"):
            self.in_body = True
            return
        if self.in_body:
            self.tags.append((tag, d))

    def handle_endtag(self, tag):
        if self.in_body and tag == "section":
            self.in_body = False


print("== 1) 根目录文章：六语属性完整性 ==")
for slug in SLUGS:
    f = "blog/%s" % slug
    if not os.path.exists(f):
        fail("文件不存在 %s" % f); continue
    s = open(f, encoding="utf-8").read()
    p = Collector(); p.feed(s)
    dzh = [(t, a) for t, a in p.tags if "data-zh" in a]
    missing = [(t, k) for t, a in dzh for k in ("data-en", "data-fr", "data-es", "data-ja", "data-ko")
               if not a.get(k, "").strip()]
    q_bad = len(re.findall(r'data-(?:zh|en|fr|es|ja|ko)=""', s))
    q_odd = len(re.findall(r'data-(?:zh|en|fr|es|ja|ko)="[^"]*"[a-zA-Z]', s))
    amp = len(re.findall(r'data-(?:zh|en|fr|es|ja|ko)="[^"]*&(?!amp;|nbsp;|quot;|#)[^"]*"', s))
    print("  %s：article-body 内带 data-zh 元素 %d 个，缺 en/fr/es/ja/ko %d 处" % (f, len(dzh), len(missing)))
    if missing:
        fail("%s 缺属性 %s" % (f, missing[:6]))
    if q_bad or q_odd:
        fail("%s 引号畸形 data-xx=\"\"=%d 值后裸字符=%d" % (f, q_bad, q_odd))
    if amp:
        fail("%s 属性值内裸 & = %d" % (f, amp))

print("== 2) 根目录文章：title/description 静态字段 ==")
for slug in SLUGS:
    s = open("blog/%s" % slug, encoding="utf-8").read()
    t = re.search(r'<title[^>]*data-zh="([^"]*)"[^>]*>(.*?)</title>', s, re.S)
    d_zh = re.search(r'<meta name="description" data-zh="([^"]*)"', s)
    d_ct = re.search(r'<meta name="description".*?content="([^"]*)"', s, re.S)
    if not t or t.group(1) != t.group(2):
        fail("%s 静态 title 与 data-zh 不一致" % slug)
    if not d_zh or not d_ct or d_zh.group(1) != d_ct.group(1):
        fail("%s description content 与 data-zh 不一致" % slug)
    print("  %s title=%d 字 description=%d 字" % (slug, len(t.group(2)), len(d_ct.group(1)) if d_ct else -1))

print("== 3) JSON-LD ==")
for slug in SLUGS:
    s = open("blog/%s" % slug, encoding="utf-8").read()
    lds = re.findall(r'<script type="application/ld\+json">(.*?)</script>', s, re.S)
    for x in lds:
        json.loads(x)
    if len(lds) != 1:
        fail("%s JSON-LD 数量 = %d" % (slug, len(lds)))
    print("  %s JSON-LD %d 处，全部合法" % (slug, len(lds)))

print("== 4) 五语生成页 ==")
for slug in SLUGS:
    for lang in LANGS:
        f = "%s/blog/%s" % (lang, slug)
        if not os.path.exists(f):
            fail("缺 %s" % f); continue
        s = open(f, encoding="utf-8").read()
        residue = len(re.findall(r'data-(?:zh|en|fr|es|ja|ko)=', s))
        m0 = s.index('<section class="article-body">')
        m1 = s.index('</section>', m0)
        body = re.sub(r'<script.*?</script>', '', s[m0:m1], flags=re.S)
        cjk = len(re.findall(r'[\u4e00-\u9fff]', body))
        title = re.search(r'<title>(.*?)</title>', s, re.S).group(1).strip()
        desc = re.search(r'<meta name="description" content="([^"]*)"', s)
        hre = len(re.findall(r'<link rel="alternate" hreflang=', s))
        canon = re.search(r'<link rel="canonical" href="([^"]*)"', s).group(1)
        ok = True
        if residue:
            fail("%s 残留 data-* = %d" % (f, residue)); ok = False
        if lang in ("en", "fr", "es") and cjk:
            fail("%s 正文残留汉字 = %d" % (f, cjk)); ok = False
        if not title or not desc:
            fail("%s 缺 title/description" % f); ok = False
        if hre != 7:
            fail("%s hreflang 数量 = %d" % (f, hre)); ok = False
        if canon != "https://taigetag.com/%s/blog/%s" % (lang, slug):
            fail("%s canonical 异常：%s" % (f, canon)); ok = False
        if ok:
            print("  %-52s 残留=0 汉字=%d desc=%d字符 hreflang=7" % (f, cjk, len(desc.group(1))))

print("== 5) sitemap ==")
sm = open("sitemap.xml", encoding="utf-8").read()
n_new = 0
for slug in SLUGS:
    for pre in ["blog/"] + ["%s/blog/" % l for l in LANGS]:
        u = "https://taigetag.com/%s%s" % (pre, slug)
        if "<loc>%s</loc>" % u not in sm:
            fail("sitemap 缺 %s" % u)
        else:
            n_new += 1
    blk = re.search(r'<loc>https://taigetag\.com/blog/%s</loc>\s*<lastmod>([^<]*)</lastmod>' % re.escape(slug), sm)
    if not blk or blk.group(1) != DATE:
        fail("%s sitemap lastmod 异常" % slug)
for u in ["https://taigetag.com/blog/index.html"] + ["https://taigetag.com/%s/blog/index.html" % l for l in LANGS]:
    m = re.search(r'<loc>%s</loc>\s*<lastmod>([^<]*)</lastmod>' % re.escape(u), sm)
    if not m or m.group(1) != DATE:
        fail("blog index lastmod 未更新 %s" % u)
print("  新 URL %d/12，<loc> 总数 %d" % (n_new, sm.count("<loc>")))

print("== 6) 列表页卡片（六语） ==")
for p in ["blog/index.html"] + ["%s/blog/index.html" % l for l in LANGS]:
    s = open(p, encoding="utf-8").read()
    hit = [sl for sl in SLUGS if sl in s]
    if len(hit) != 2:
        fail("%s 新卡片命中 = %s" % (p, hit))
    else:
        print("  %-26s 新卡片 2/2" % p)

print("== 7) 版本号 ==")
mj = open("js/main.js", encoding="utf-8").read()
b = re.search(r'var BUST_VERSION = "(\d+)";', mj).group(1)
print("  BUST_VERSION = %s" % b)
if b != "102":
    fail("BUST_VERSION 不是 102")

print("== 8) 相关文章内部链接存在性 ==")
for slug in SLUGS:
    s = open("blog/%s" % slug, encoding="utf-8").read()
    m0 = s.index('<section class="article-body">')
    m1 = s.index('</section>', m0)
    body = s[m0:m1]
    for href in re.findall(r'<li><a href="([^"]+)"', body):
        if href.startswith("http") or href.startswith(".."):
            continue
        if not os.path.exists(os.path.join("blog", href)):
            fail("%s 内链指向不存在文件 %s" % (slug, href))
print("  内链检查完成（仅正文相关文章区）")

print("\n结论：%s（失败 %d 项）" % ("全部通过" if not fails else "有问题", len(fails)))
sys.exit(1 if fails else 0)
