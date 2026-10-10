#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""校验本批次新增文章：六语属性完整性（HTMLParser）、引号畸形、JSON-LD、生成页残留、表格列数、sitemap、卡片、BUST。"""
import re, json, os
from html.parser import HTMLParser

HERE = os.path.dirname(os.path.abspath(__file__))
os.chdir(HERE)

NEW = ["blog/uflpa-apparel-trims-traceability-guide.html", "blog/corrugated-carton-strength-guide.html"]
LANGS = ("en", "ja", "ko", "fr", "es")
TODAY = "2026-10-10"


class Collector(HTMLParser):
    """收集 article-body 内的开始标签及其属性"""
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
    s = open(f, encoding='utf-8').read()
    p = Collector(); p.feed(s)
    dzh = [(t, a) for t, a in p.tags if "data-zh" in a]
    missing = []
    for t, a in dzh:
        for need in ("data-en", "data-ja", "data-ko", "data-fr", "data-es"):
            if not a.get(need, "").strip():
                missing.append((t, need))
    total_missing += len(missing)
    print("  %s" % f)
    print("    article-body 内标签 %d 个，其中带 data-zh 的 %d 个；缺其他五语的 %d 个 %s"
          % (len(p.tags), len(dzh), len(missing), missing[:8]))
    print("    缺 data-fr 或 data-es 的元素数: %d" % len([m for m in missing if m[1] in ("data-fr", "data-es")]))
    print("    引号畸形 data-xx=\"\" : %d ; 属性值后裸字符: %d ; 裸 & : %d"
          % (len(re.findall(r'data-(?:zh|en|fr|es|ja|ko)=\"\"', s)),
             len(re.findall(r'data-(?:zh|en|fr|es|ja|ko)=\"[^\"]*\"[a-zA-Z]', s)),
             len(re.findall(r'&(?!amp;|nbsp;|quot;|#)', s))))
    lds = re.findall(r'<script type="application/ld\+json">(.*?)</script>', s, re.S)
    for x in lds:
        json.loads(x)
    t = re.search(r'<title[^>]*>(.*?)</title>', s, re.S).group(1)
    can = re.search(r'<link rel="canonical" href="([^"]*)"', s).group(1)
    hl = re.findall(r'<link rel="alternate" hreflang="([^"]*)"', s)
    print("    JSON-LD %d 处全部合法；静态 title: %s" % (len(lds), t[:70]))
    print("    canonical: %s ; hreflang: %s" % (can, "/".join(hl)))

    for ti, tb in enumerate(re.findall(r'<table.*?</table>', s, re.S), 1):
        rows = re.findall(r'<tr>(.*?)</tr>', tb, re.S)
        counts = [len(re.findall(r'<(?:th|td)\b', r)) for r in rows]
        ok = len(set(counts)) == 1
        print("    表 %d：%d 行，各行列数 %s %s" % (ti, len(rows), counts, "OK" if ok else "!! 列数不一致"))

    # 内部链接指向的文件是否存在
    for href in set(re.findall(r'<a href="([^"#?]+)"', s)):
        if href.startswith(("http", "mailto", "tel")):
            continue
        tgt = os.path.join(os.path.dirname(f), href)
        if not os.path.exists(tgt):
            print("    !! 死链: %s" % href)

print("== 2) 生成页（en/ja/ko/fr/es）残留检查 ==")
for f in NEW:
    for lang in LANGS:
        path = os.path.join(lang, f)
        s = open(path, encoding='utf-8').read()
        m0 = re.search(r'<section class="article-body">', s)
        m1 = re.search(r'</section>', s[m0.end():])
        body = s[m0.end():m0.end() + m1.start()]
        cjk = len(re.findall(r'[\u4e00-\u9fff]', re.sub(r'<script.*?</script>', '', body, flags=re.S)))
        q = Collector(); q.feed(s)
        residue = sum(1 for t, a in q.tags if any(k.startswith("data-") and k[5:] in
                      ("zh", "en", "ja", "ko", "fr", "es") for k in a))
        desc = re.search(r'<meta name="description" content="([^"]*)"', s)
        ttl = re.search(r'<title>(.*?)</title>', s, re.S).group(1)
        print("  %-62s data-*残留=%d 正文汉字=%d desc=%d字符 title=%s"
              % (path, residue, cjk, len(desc.group(1)) if desc else -1, ttl[:46]))

print("== 3) sitemap ==")
sm = open("sitemap.xml", encoding="utf-8").read()
for f in NEW:
    slug = os.path.basename(f)
    for pre in ("blog/", "en/blog/", "ja/blog/", "ko/blog/", "fr/blog/", "es/blog/"):
        u = "https://taigetag.com/%s%s" % (pre, slug)
        assert "<loc>%s</loc>" % u in sm, u
    print("  %s 六语 URL 全部存在" % slug)
for pre in ("", "en/", "ja/", "ko/", "fr/", "es/"):
    u = "https://taigetag.com/%sblog/index.html" % pre
    m = re.search(r'<loc>%s</loc>\r?\n\s*<lastmod>([^<]*)</lastmod>' % re.escape(u), sm)
    print("  %s lastmod=%s %s" % (u, m.group(1), "OK" if m and m.group(1) == TODAY else "!!"))
print("  <loc> 总数=%d" % sm.count("<loc>"))

print("== 4) 六语列表页卡片（应为前两张） ==")
for p in ("blog/index.html",) + tuple("%s/blog/index.html" % l for l in LANGS):
    s = open(p, encoding='utf-8').read()
    hit = [os.path.basename(f) for f in NEW if os.path.basename(f) in s]
    grid = s.index('<div class="post-grid">')
    first = re.findall(r'<a class="more" href="([^"]*)"', s[grid:])
    print("  %-26s 新卡片命中=%d ; 首卡=%s" % (p, len(hit), first[:2]))
    assert len(hit) == 2, "%s 卡片缺失" % p
    assert os.path.basename(NEW[0]) in first[:2] and os.path.basename(NEW[1]) in first[:2], "%s 新卡片不在顶部" % p

print("== 5) BUST_VERSION ==")
mj = open("js/main.js", encoding="utf-8").read()
print("  ", re.search(r'var BUST_VERSION = "[^"]*";', mj).group(0))

print("\n结论: 缺失总数 = %d" % total_missing)
raise SystemExit(1 if total_missing else 0)
