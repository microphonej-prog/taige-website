#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-09-30 下午批次本地校验：六语属性完整性、生成页残留与语言纯净度、JSON-LD、
sitemap（12 个新 URL + blog 首页 lastmod）、列表页卡片。"""
import re, os, json
from html.parser import HTMLParser

NEW = ["blog/woven-label-density-guide.html", "blog/garment-trims-development-calendar.html"]
LANGS = ["en", "ja", "ko", "fr", "es"]


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


print("== 1) 正文六语属性完整性（根目录中文版）")
total_missing = 0
for f in NEW:
    s = open(f, encoding="utf-8").read()
    p = Collector()
    p.feed(s)
    dzh = [(t, a) for t, a in p.tags if "data-zh" in a]
    missing = []
    for t, a in dzh:
        for need in ("data-en", "data-ja", "data-ko", "data-fr", "data-es"):
            if not a.get(need, "").strip():
                missing.append((t, need))
    total_missing += len(missing)
    lds = re.findall(r'<script type="application/ld\+json">(.*?)</script>', s, re.S)
    for x in lds:
        json.loads(x)
    t = re.search(r'<title[^>]*>(.*?)</title>', s, re.S).group(1)
    print("  %s" % f)
    print("    body 内标签 %d，带 data-zh %d；缺 en/ja/ko/fr/es 的 %d %s"
          % (len(p.tags), len(dzh), len(missing), missing[:6]))
    print("    引号畸形 data-xx=\"\"=%d 裸字符=%d 裸&=%d；JSON-LD %d 处合法"
          % (len(re.findall(r'data-(?:zh|en|fr|es|ja|ko)=""', s)),
             len(re.findall(r'data-(?:zh|en|fr|es|ja|ko)="[^"]*"[a-zA-Z]', s)),
             len(re.findall(r'&(?!amp;|nbsp;|quot;|#)', s)), len(lds)))
    print("    静态 title: %s" % t[:70])

print("== 2) 五语生成页（en/ja/ko/fr/es）残留与纯净度")
for f in NEW:
    slug = os.path.basename(f)
    for lang in LANGS:
        path = os.path.join(lang, f)
        s = open(path, encoding="utf-8").read()
        m0 = re.search(r'<section class="article-body">', s)
        m1 = re.search(r'</section>', s[m0.end():])
        body = s[m0.end():m0.end() + m1.start()]
        body = re.sub(r'<script.*?</script>', '', body, flags=re.S)
        cjk = len(re.findall(r'[\u4e00-\u9fff]', body))
        kana = len(re.findall(r'[\u3040-\u30ff]', body))
        hangul = len(re.findall(r'[\uac00-\ud7af]', body))
        q = Collector()
        q.feed(s)
        residue = sum(1 for t, a in q.tags if any(k.startswith("data-") and k[5:] in
                      ("zh", "en", "fr", "es", "ja", "ko") for k in a))
        desc = re.search(r'<meta name="description" content="([^"]*)"', s)
        title = re.search(r'<title[^>]*>(.*?)</title>', s, re.S).group(1)
        print("  %-56s data-*残留=%d 漢字=%d かな=%d 한글=%d desc=%d title=%s"
              % (path, residue, cjk, kana, hangul, len(desc.group(1)) if desc else -1, title[:40]))
        if residue:
            print("     !! 残留 data-* 属性")
        if lang in ("en", "fr", "es") and (cjk or kana or hangul):
            print("     !! 非目标语言字符残留")

print("== 3) sitemap")
sm = open("sitemap.xml", encoding="utf-8").read()
n_urls = 0
for f in NEW:
    slug = os.path.basename(f)
    for pre in ("blog/",) + tuple("%s/blog/" % l for l in LANGS):
        u = "https://taigetag.com/%s%s" % (pre, slug)
        assert "<loc>%s</loc>" % u in sm, u
        n_urls += 1
assert re.search(r'<loc>https://taigetag\.com/blog/index\.html</loc>\s*<lastmod>2026-09-30</lastmod>', sm)
for l in LANGS:
    assert re.search(r'<loc>https://taigetag\.com/%s/blog/index\.html</loc>\s*<lastmod>2026-09-30</lastmod>' % l, sm)
print("  新 URL %d 个全部存在；blog 首页六语 lastmod 均为 2026-09-30；<loc> 总数=%d" % (n_urls, sm.count("<loc>")))

print("== 4) 列表页卡片")
for p in ["blog/index.html"] + ["%s/blog/index.html" % l for l in LANGS]:
    s = open(p, encoding="utf-8").read()
    hit = [os.path.basename(f) for f in NEW if os.path.basename(f) in s]
    pos = s.find("post-grid")
    first = re.search(r'<article class="post-card">.*?href="([^"]*)"', s, re.S)
    print("  %-26s 新卡片命中=%s 首张卡=%s" % (p, hit, first.group(1) if first else "?"))

print("== 5) BUST_VERSION")
mj = open("js/main.js", encoding="utf-8").read()
print("  %s" % re.search(r'var BUST_VERSION = "[^"]*";', mj).group(0))

print("\n缺失总数 = %d" % total_missing)
raise SystemExit(1 if total_missing else 0)
