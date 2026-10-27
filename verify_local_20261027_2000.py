#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-27 20:00 批次本地校验：六语属性完整性、引号畸形、JSON-LD、lang 残留、sitemap、卡片、canonical/hreflang"""
import re, json, os, sys
from html.parser import HTMLParser

os.chdir(os.path.dirname(os.path.abspath(__file__)))
NEW = ["blog/collab-capsule-collection-trims-guide.html",
       "blog/offshore-sewing-trims-supply-guide.html"]
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


print("== 1) 根页正文六语属性完整性 ==")
total_missing = 0
for f in NEW:
    s = open(f, encoding="utf-8").read()
    p = Collector(); p.feed(s)
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
    t = re.search(r"<title[^>]*>(.*?)</title>", s, re.S).group(1)
    desc = re.search(r'<meta name="description"[^>]*content="([^"]*)"', s, re.S).group(1)
    print("  %s" % f)
    print("    正文标签 %d，带 data-zh %d，缺语 %d %s"
          % (len(p.tags), len(dzh), len(missing), missing[:6]))
    print("    引号畸形 %d ; 裸 & %d ; JSON-LD %d 处合法"
          % (len(re.findall(r'data-(?:zh|en|fr|es|ja|ko)=""', s)),
             len(re.findall(r'&(?!amp;|nbsp;|quot;|#)', s)), len(lds)))
    print("    静态 title: %s" % t[:70])
    print("    静态 desc [%d 字]: %s" % (len(desc), desc[:60]))

print("== 2) 语言页残留与标题 ==")
for lang in LANGS:
    for f in NEW:
        path = os.path.join(lang, f)
        s = open(path, encoding="utf-8").read()
        m0 = re.search(r'<section class="article-body">', s)
        m1 = re.search(r"</section>", s[m0.end():])
        body = s[m0.end():m0.end() + m1.start()]
        cjk = len(re.findall(r"[\u4e00-\u9fff]", re.sub(r"<script.*?</script>", "", body, flags=re.S)))
        residue = len(re.findall(r'data-(?:zh|en|fr|es|ja|ko)="', s))
        title = re.search(r"<title>(.*?)</title>", s, re.S).group(1)
        print("  %-46s 汉字残留=%4d data-*残留=%d | %s" % (path, cjk, residue, title[:58]))

print("== 3) sitemap ==")
sm = open("sitemap.xml", encoding="utf-8").read()
n = 0
for f in NEW:
    slug = os.path.basename(f)
    for pre in ["blog/"] + ["%s/blog/" % l for l in LANGS]:
        u = "https://taigetag.com/%s%s" % (pre, slug)
        assert "<loc>%s</loc>" % u in sm, u
        n += 1
print("  新增 URL 全部存在: %d 个；<loc> 总数=%d" % (n, sm.count("<loc>")))

print("== 4) canonical / hreflang 与 sitemap 一致性 ==")
for lang in LANGS:
    for f in NEW:
        path = os.path.join(lang, f)
        s = open(path, encoding="utf-8").read()
        canon = re.search(r'<link rel="canonical" href="([^"]*)"', s).group(1)
        expect = "https://taigetag.com/%s/%s" % (lang, f.replace("\\", "/"))
        assert canon == expect, (canon, expect)
        assert "<loc>%s</loc>" % canon in sm, canon
        hl = dict(re.findall(r'<link rel="alternate" hreflang="([^"]*)" href="([^"]*)"', s))
        assert set(hl) == {"zh-Hant", "en", "ja", "ko", "fr", "es", "x-default"}, hl
        for k, v in hl.items():
            assert "<loc>%s</loc>" % v in sm, (k, v)
print("  10 个语言页 canonical 与 sitemap 一致，hreflang 7 条齐全且均在 sitemap 内")

print("== 5) 列表页卡片（六语） ==")
for p in ["blog/index.html"] + ["%s/blog/index.html" % l for l in LANGS]:
    s = open(p, encoding="utf-8").read()
    hit = [os.path.basename(f) for f in NEW if os.path.basename(f) in s]
    print("  %-26s 新卡片命中=%d %s" % (p, len(hit), hit))

print("== 6) BUST_VERSION ==")
mj = open("js/main.js", encoding="utf-8").read()
print("  ", re.search(r'var BUST_VERSION = "[^"]*";', mj).group(0))
print("\n结论: 缺语总数 = %d" % total_missing)
sys.exit(1 if total_missing else 0)
