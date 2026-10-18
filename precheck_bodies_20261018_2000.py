#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-18 20:00 批次：正文六语属性预检 + 撞车检查"""
import os, re, sys
from html.parser import HTMLParser

ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)

BODIES = ["blog/_body_compost.html", "blog/_body_destroy.html"]
SLUGS = ["compostable-packaging-certification-guide.html", "trim-scrap-destruction-certificate-guide.html"]
LANGS = ["en", "ja", "ko", "fr", "es"]
NEED = ["data-zh", "data-en", "data-ja", "data-ko", "data-fr", "data-es"]


class Scan(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.stack = []
        self.problems = []
        self.counts = {k: 0 for k in NEED}
        self.tags = 0

    def handle_starttag(self, tag, attrs):
        if tag in ("br", "img", "hr", "meta", "link", "input"):
            self.stack.append((tag, dict(attrs)))
            return
        self.stack.append((tag, dict(attrs)))

    def handle_startendtag(self, tag, attrs):
        pass

    def handle_endtag(self, tag):
        if not self.stack:
            return
        t, a = self.stack.pop()
        if t != tag:
            self.problems.append("标签不配对: <%s> vs </%s>" % (t, tag))
            return
        if t in ("ul", "table", "tr", "section", "div", "br"):
            return
        self.tags += 1
        missing = [k for k in NEED if k not in a or not a[k].strip()]
        if missing and t not in ("script", "style", "head", "html", "body", "main"):
            self.problems.append("<%s> 缺属性 %s | 文本=%s" % (t, missing, (a.get("data-zh") or "")[:30]))
        for k in NEED:
            if k in a:
                self.counts[k] += 1

    def handle_data(self, data):
        if not self.stack:
            return
        t, a = self.stack[-1]
        if t in ("th", "td", "p", "h2", "h3", "li", "div", "a", "section", "span") and data.strip():
            if "data-zh" in a and data.strip() != a["data-zh"]:
                self.problems.append("<%s> 默认文本与 data-zh 不一致: 文本=%s / zh=%s"
                                     % (t, data.strip()[:24], a["data-zh"][:24]))


for b in BODIES:
    s = open(b, encoding="utf-8").read()
    p = Scan()
    p.feed(s)
    print("=" * 70)
    print(b, "元素数=%d" % p.tags, p.counts)
    print("  中文正文字数(去标签)=%d" % len(re.sub(r"<[^>]+>", "", re.sub(r'(data-[a-z]{2})="[^"]*"', "", s))))
    if p.problems:
        print("  ⚠ 问题 %d 条:" % len(p.problems))
        for x in p.problems[:15]:
            print("   -", x)
    else:
        print("  ✓ 六语属性完整，无标签/文本不一致")
    # 引号畸形扫描
    bad = re.findall(r'data-(?:zh|en|ja|ko|fr|es)=""', s)
    if bad:
        print("  ⚠ 空属性引号畸形 %d 处" % len(bad))
    # 软连字符
    if "\u00ad" in s:
        print("  ⚠ 含软连字符 U+00AD %d 处" % s.count("\u00ad"))
    # 相对链接检查
    for m in re.findall(r'href="([^"]+)"', s):
        if not m.startswith(("http", "#", "../")) and m != "index.html":
            if not os.path.exists(os.path.join("blog", m)):
                print("  ⚠ 站内链接不存在:", m)

print("=" * 70)
for slug in SLUGS:
    paths = ["blog/%s" % slug] + ["%s/blog/%s" % (l, slug) for l in LANGS]
    hit = [x for x in paths if os.path.exists(x)]
    print("撞车检查 %-38s %s" % (slug, "存在：" + str(hit) if hit else "OK 全新"))
sm = open("sitemap.xml", encoding="utf-8").read()
for slug in SLUGS:
    print("sitemap 检查 %-38s %s" % (slug, "已含（撞车）" if "/blog/%s</loc>" % slug in sm else "OK 无"))
mj = open("js/main.js", encoding="utf-8").read()
print("BUST_VERSION =", re.search(r'var BUST_VERSION = "(\d+)"', mj).group(1))
