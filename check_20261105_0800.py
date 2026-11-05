#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""校验 2026-11-05 08:00 批次：属性完整性 / 标题渲染 / 卡片 / sitemap。"""
import re, os, io
from html.parser import HTMLParser

LANGS = ["en", "ja", "ko", "fr", "es"]
SLUGS = ["clothing-label-compliance-poland.html", "clothing-label-compliance-portugal.html"]
ATTRS = ["data-zh", "data-en", "data-ja", "data-ko", "data-fr", "data-es"]

TAGS = {"p", "h2", "h3", "li", "td", "th", "div", "a", "span", "strong", "em"}


class BodyScan(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.in_body = False
        self.depth = 0
        self.total = 0
        self.missing = []
        self.empty = []

    def handle_starttag(self, tag, attrs):
        if tag == "section":
            d = dict(attrs)
            if "article-body" in (d.get("class") or ""):
                self.in_body = True
                self.depth = 1
                return
        if not self.in_body:
            return
        if tag == "section":
            self.depth += 1
        d = dict(attrs)
        if tag in TAGS and "data-zh" in d:
            self.total += 1
            miss = [a for a in ATTRS if a not in d]
            if miss:
                self.missing.append((tag, d.get("data-zh", "")[:40], miss))
            for a in ATTRS:
                if a in d and d[a].strip() == "":
                    self.empty.append((tag, a))

    def handle_endtag(self, tag):
        if self.in_body and tag == "section":
            self.depth -= 1
            if self.depth == 0:
                self.in_body = False


def scan(path):
    s = open(path, encoding="utf-8").read()
    p = BodyScan()
    p.feed(s)
    return p, s


ok = True
for slug in SLUGS:
    p, s = scan("blog/%s" % slug)
    print("== %s  正文带属性元素 %d 个；缺属性 %d；空属性 %d" % (slug, p.total, len(p.missing), len(p.empty)))
    for m in p.missing[:10]:
        print("   缺:", m)
        ok = False
    for e in p.empty[:10]:
        print("   空:", e)
        ok = False
    # 双引号畸形
    bad = re.findall(r'data-(?:zh|en|ja|ko|fr|es)=""', s)
    print("   畸形双引号 data-xx=\"\" 计数:", len(bad))
    if bad:
        ok = False
    # 标题/描述/canonical
    for lang, path in [(None, "blog/%s" % slug)] + [(l, "%s/blog/%s" % (l, slug)) for l in LANGS]:
        t = open(path, encoding="utf-8").read()
        m = re.search(r"<title[^>]*>(.*?)</title>", t, re.S)
        d = re.search(r'<meta name="description"[^>]*content="([^"]*)"', t, re.S)
        c = re.search(r'<link rel="canonical" href="([^"]*)"', t)
        label = lang or "zh"
        title = re.sub(r"\s+", " ", m.group(1))[:70] if m else "NO TITLE"
        print("   [%s] %s" % (label, title))
        print("        desc=%d 字符 canonical=%s" % (len(d.group(1)) if d else -1, c.group(1) if c else "NONE"))
        if not m or not d or not c:
            ok = False
        if lang in ("en", "fr", "es") and re.search(r"[\u4e00-\u9fff]", title):
            print("       !! 标题含中文")
            ok = False

# 卡片
idx = open("blog/index.html", encoding="utf-8").read()
grid_start = idx.index('<div class="post-grid">')
head = idx[grid_start:grid_start + 6000]
for slug in SLUGS:
    n = head.count('href="%s"' % slug)
    print("卡片 %s 在 post-grid 顶部出现 %d 次（应为 1）" % (slug, n))
    if n != 1:
        ok = False

# sitemap
sm = open("sitemap.xml", encoding="utf-8").read()
for slug in SLUGS:
    for u in ["https://taigetag.com/blog/%s" % slug] + ["https://taigetag.com/%s/blog/%s" % (l, slug) for l in LANGS]:
        if "<loc>%s</loc>" % u not in sm:
            print("sitemap 缺:", u)
            ok = False
print("sitemap blog/index lastmod 2026-11-05 计数:", len(re.findall(r"blog/index\.html</loc>\r\n\s*<lastmod>2026-11-05", sm)))
print("BUST_VERSION:", re.search(r'BUST_VERSION = "(\d+)"', open("js/main.js", encoding="utf-8").read()).group(1))
print("RESULT:", "OK" if ok else "PROBLEM")
