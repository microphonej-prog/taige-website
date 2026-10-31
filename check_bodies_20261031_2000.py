#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-31 20:00 批次本地校验：四/六语属性完整性、卡片、sitemap、正文长度"""
import re, os, json, html
from html.parser import HTMLParser

ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)

SLUGS = ["medical-ppe-garment-labeling-guide.html", "trademark-symbols-garment-labels.html"]
LANGS = ["en", "ja", "ko", "fr", "es"]
LANGS_ALL = ["zh"] + LANGS


class BodyParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.in_body = False
        self.depth = 0
        self.elems = []   # (tag, attrs-dict)

    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        if tag == "section" and "article-body" in (d.get("class") or ""):
            self.in_body = True
            self.depth = 0
            return
        if self.in_body:
            self.depth += 1
            self.elems.append((tag, d))

    def handle_endtag(self, tag):
        if self.in_body:
            if tag == "section" and self.depth == 0:
                self.in_body = False
            else:
                self.depth = max(0, self.depth - 1)


def check_body(path):
    s = open(path, encoding="utf-8").read()
    p = BodyParser()
    p.feed(s)
    zh = [e for e in p.elems if "data-zh" in e[1]]
    missing = {l: 0 for l in LANGS}
    for tag, d in zh:
        for l in LANGS:
            if "data-" + l not in d:
                missing[l] += 1
    # 空值 / 引号异常
    empty = len(re.findall(r'data-(?:zh|en|fr|es|ja|ko)=""', s))
    zh_chars = sum(len(re.findall(r'[\u4e00-\u9fff]', d.get("data-zh", ""))) for _, d in zh)
    return len(zh), missing, empty, zh_chars


ok = True
for slug in SLUGS:
    for lang in LANGS_ALL:
        p = ("blog/%s" % slug) if lang == "zh" else ("%s/blog/%s" % (lang, slug))
        if not os.path.exists(p):
            print("缺失文件:", p); ok = False
for slug in SLUGS:
    n, miss, empty, chars = check_body("blog/%s" % slug)
    bad = {k: v for k, v in miss.items() if v}
    print("%-46s data-zh元素=%-3d 缺语言=%s 空属性=%d 中文正文字数=%d"
          % (slug, n, bad if bad else "无", empty, chars))
    if bad or empty:
        ok = False
    if not (600 <= chars <= 1100):
        print("   !! 中文字数超出 600-1100:", chars)

# 卡片
for lang in LANGS_ALL:
    p = "blog/index.html" if lang == "zh" else "%s/blog/index.html" % lang
    s = open(p, encoding="utf-8").read()
    hits = [slug for slug in SLUGS if 'href="%s"' % slug in s]
    print("卡片 %-3s %s" % (lang, "OK %d/2" % len(hits) if len(hits) == 2 else "缺失 %s" % hits))
    if len(hits) != 2:
        ok = False

# sitemap
sm = open("sitemap.xml", encoding="utf-8").read()
urls = ["https://taigetag.com/blog/%s" % s for s in SLUGS] + \
       ["https://taigetag.com/%s/blog/%s" % (l, s) for s in SLUGS for l in LANGS]
missing = [u for u in urls if "<loc>%s</loc>" % u not in sm]
print("sitemap 新 URL %d/%d 存在 %s" % (len(urls) - len(missing), len(urls), "OK" if not missing else missing))
if missing:
    ok = False
for u in ["https://taigetag.com/blog/index.html"] + ["https://taigetag.com/%s/blog/index.html" % l for l in LANGS]:
    m = re.search(r'<loc>%s</loc>\s*<lastmod>([^<]*)</lastmod>' % re.escape(u), sm)
    if not m or m.group(1) != "2026-10-31":
        print("  !! blog index lastmod 未更新:", u, m.group(1) if m else None); ok = False

# 各语言 title 是否已静态渲染（非中文）
for lang in LANGS:
    s = open("%s/blog/%s" % (lang, SLUGS[0]), encoding="utf-8").read()
    t = re.search(r"<title>(.*?)</title>", s, re.S).group(1)
    cjk = len(re.findall(r"[\u4e00-\u9fff]", t))
    print("title %-3s CJK=%d %s" % (lang, cjk, t[:70]))

print("BUST_VERSION:", re.search(r'var BUST_VERSION = "(\d+)";', open("js/main.js", encoding="utf-8").read()).group(1))
print("结果:", "通过" if ok else "有问题")
