#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-05 晚间批次校验：新文章六语属性、语言页残留、JSON-LD、sitemap、列表卡片、BUST_VERSION"""
import re, json, os
from html.parser import HTMLParser

NEW = ["blog/reach-svhc-apparel-trims-guide.html", "blog/braille-tactile-label-guide.html"]
LANGS = ("en", "ja", "ko", "fr", "es")


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


print("== 1) 中文根页正文六语属性完整性 ==")
total_missing = 0
for f in NEW:
    s = open(f, encoding="utf-8").read()
    p = Collector(); p.feed(s)
    dzh = [(t, a) for t, a in p.tags if "data-zh" in a]
    missing = [(t, n) for t, a in dzh for n in ("data-en", "data-ja", "data-ko", "data-fr", "data-es")
               if not a.get(n, "").strip()]
    total_missing += len(missing)
    print("  %s" % f)
    print("    article-body 内标签 %d，带 data-zh %d，缺语言属性 %d %s"
          % (len(p.tags), len(dzh), len(missing), missing[:6]))
    print("    data-xx=\"\" 畸形 %d ; 裸 & %d" %
          (len(re.findall(r'data-(?:zh|en|ja|ko|fr|es)=""', s)),
           len(re.findall(r'&(?!amp;|nbsp;|quot;|#)', s))))
    lds = re.findall(r'<script type="application/ld\+json">(.*?)</script>', s, re.S)
    for x in lds:
        json.loads(x)
    print("    JSON-LD %d 处合法 ; 语言页残留 data-zh 于正文: %d" %
          (len(lds), s.count('data-zh="#') ))

print("\n== 2) 五个语言版本页面检查 ==")
for f in NEW:
    for lang in LANGS:
        path = os.path.join(lang, f)
        s = open(path, encoding="utf-8").read()
        m0 = re.search(r'<section class="article-body">', s)
        m1 = re.search(r'</section>', s[m0.end():])
        body = s[m0.end():m0.end() + m1.start()]
        cjk = len(re.findall(r'[\u4e00-\u9fff]', re.sub(r'<script.*?</script>', '', body, flags=re.S)))
        q = Collector(); q.feed(s)
        residue = sum(1 for t, a in q.tags for k in a if k.startswith("data-") and k[5:] in ("zh", "en", "ja", "ko", "fr", "es"))
        t = re.search(r'<title>(.*?)</title>', s, re.S).group(1)
        desc = re.search(r'<meta name="description" content="([^"]*)"', s)
        print("  %-46s cjk残留=%3d data残留=%d desc=%3d  title=%s" %
              (path, cjk, residue, len(desc.group(1)) if desc else -1, t[:58]))

print("\n== 3) sitemap ==")
sm = open("sitemap.xml", encoding="utf-8").read()
n_ok = 0
for f in NEW:
    slug = os.path.basename(f)
    for pre in ("blog/",) + tuple(l + "/blog/" for l in LANGS):
        u = "https://taigetag.com/%s%s" % (pre, slug)
        assert "<loc>%s</loc>" % u in sm, u
        n_ok += 1
for pre in ("blog/",) + tuple(l + "/blog/" for l in LANGS):
    u = "https://taigetag.com/%sindex.html" % pre
    m = re.search(r'<loc>%s</loc>\r?\n\s*<lastmod>([^<]*)</lastmod>' % re.escape(u), sm)
    assert m, u
    assert m.group(1) == "2026-10-05", (u, m.group(1))
print("  新 URL %d 个全部在 sitemap；6 个 blog 首页 lastmod 均为 2026-10-05；<loc> 总数 %d" % (n_ok, sm.count("<loc>")))

print("\n== 4) 列表页卡片 ==")
for p in ["blog/index.html"] + ["%s/blog/index.html" % l for l in LANGS]:
    s = open(p, encoding="utf-8").read()
    hit = [os.path.basename(f) for f in NEW if os.path.basename(f) in s]
    print("  %-26s 命中 %s" % (p, hit))

print("\n== 5) BUST_VERSION / hreflang / canonical ==")
mj = open("js/main.js", encoding="utf-8").read()
print("  BUST_VERSION = %s" % re.search(r'BUST_VERSION = "(\d+)"', mj).group(1))
for f in NEW:
    s = open(f, encoding="utf-8").read()
    print("  %-46s canonical=%s hreflang=%d" %
          (os.path.basename(f),
           re.search(r'<link rel="canonical" href="([^"]*)"', s).group(1),
           len(re.findall(r'hreflang="', s))))

print("\n结论: 缺失语言属性总数 = %d" % total_missing)
raise SystemExit(1 if total_missing else 0)
