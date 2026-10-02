#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-02 早上批次校验：六语属性完整性、引号畸形、生成页残留、卡片、sitemap、正文长度"""
import re, json, os, sys
from html.parser import HTMLParser

NEW = ["blog/school-uniform-trims-label-guide.html", "blog/maternity-nursing-wear-trims-guide.html"]
LANGS = ["en", "fr", "es", "ja", "ko"]


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


print("== 1) 正文六语属性完整性（根目录页）==")
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
    m0 = re.search(r'<section class="article-body">', s)
    m1 = re.search(r'</section>', s[m0.end():])
    body = s[m0.end():m0.end() + m1.start()]
    cjk = len(re.findall(r'[\u4e00-\u9fff]', re.sub(r'<script.*?</script>', "", body, flags=re.S)))
    print("  %s" % f)
    print("    正文标签 %d 个，带 data-zh %d 个；缺 en/ja/ko/fr/es 的 %d 个 %s"
          % (len(p.tags), len(dzh), len(missing), missing[:6]))
    print("    正文汉字 %d 字（目标 600-900+）；空属性=%d 引号畸形=%d 裸&=%d"
          % (cjk, len(re.findall(r'data-(?:zh|en|ja|ko|fr|es)=""', s)),
             len(re.findall(r'data-(?:zh|en|ja|ko|fr|es)="[^"]*"[a-zA-Z]', s)),
             len(re.findall(r'&(?!amp;|nbsp;|quot;|#)', s))))
    for x in re.findall(r'<script type="application/ld\+json">(.*?)</script>', s, re.S):
        json.loads(x)
    print("    JSON-LD 合法；静态 title: %s" % re.search(r'<title[^>]*>(.*?)</title>', s, re.S).group(1)[:56])

print("\n== 2) 生成页（5 语）残留与长度 ==")
for f in NEW:
    for lang in LANGS:
        path = "%s/%s" % (lang, f)
        s = open(path, encoding="utf-8").read()
        m0 = re.search(r'<section class="article-body">', s)
        m1 = re.search(r'</section>', s[m0.end():])
        body = s[m0.end():m0.end() + m1.start()]
        cjk = len(re.findall(r'[\u4e00-\u9fff]', re.sub(r'<script.*?</script>', "", body, flags=re.S)))
        q = Collector(); q.feed(s)
        residue = sum(1 for t, a in q.tags if any(k.startswith("data-") and k[5:] in LANGS + ["zh"] for k in a))
        desc = re.search(r'<meta name="description"[^>]*content="([^"]*)"', s, re.S)
        title = re.search(r'<title>(.*?)</title>', s, re.S)
        print("  %-52s 残留=%d 正文汉字=%4d desc=%3d title=%s"
              % (path, residue, cjk, len(desc.group(1)), title.group(1)[:44]))

print("\n== 3) blog 列表页卡片（六语）==")
for pre in ("blog/", "en/blog/", "ja/blog/", "ko/blog/", "fr/blog/", "es/blog/"):
    s = open("%sindex.html" % pre, encoding="utf-8").read()
    hit = [os.path.basename(f) for f in NEW if os.path.basename(f) in s]
    print("  %-12s 新卡片命中=%d %s" % (pre, len(hit), hit))

print("\n== 4) sitemap ==")
sm = open("sitemap.xml", encoding="utf-8").read()
n = 0
for f in NEW:
    slug = os.path.basename(f)
    for pre in ("blog/", "en/blog/", "ja/blog/", "ko/blog/", "fr/blog/", "es/blog/"):
        u = "https://taigetag.com/%s%s" % (pre, slug)
        assert "<loc>%s</loc>" % u in sm, u
        n += 1
print("  12 个新 URL 全部存在；<loc> 总数=%d" % sm.count("<loc>"))
for pre in ("blog/", "en/blog/", "ja/blog/", "ko/blog/", "fr/blog/", "es/blog/"):
    u = "https://taigetag.com/%sindex.html" % pre
    pat = re.compile(r'<loc>%s</loc>\r?\n\s*<lastmod>([^<]*)</lastmod>' % re.escape(u))
    m = pat.search(sm)
    print("  lastmod %-40s = %s" % (u, m.group(1) if m else "MISSING"))

print("\n== 5) BUST_VERSION / 相对路径 ==")
mj = open("js/main.js", encoding="utf-8").read()
print("  BUST_VERSION = %s" % re.search(r'var BUST_VERSION = "([^"]*)"', mj).group(1))
for lang in LANGS:
    s = open("%s/%s" % (lang, NEW[0]), encoding="utf-8").read()
    bad = re.findall(r'(?:href|src)="\.\./(?:css|js|images)/', s)
    print("  %s 相对路径层级错误 %d 处" % (lang, len(bad)))

print("\n== 6) 新文章内部链接存在性 ==")
for f in NEW:
    s = open(f, encoding="utf-8").read()
    links = sorted(set(re.findall(r'href="([a-z0-9][a-z0-9-]*\.html)"', s)))
    for l in links:
        ok = os.path.exists("blog/%s" % l)
        print("  %-46s %-52s %s" % (os.path.basename(f), l, "OK" if ok else "MISSING"))

print("\n结论: 缺失总数 = %d" % total_missing)
sys.exit(1 if total_missing else 0)
