#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-06 下午批次校验：正文六语属性（HTMLParser）、引号畸形、JSON-LD、生成页残留、
canonical 与 sitemap 一致性、sitemap、blog 列表卡片、内链、正文字数、版本号。"""
import re, json, os
from html.parser import HTMLParser

NEW = ["blog/sequin-rhinestone-trims-guide.html", "blog/rib-knit-collar-cuff-guide.html"]
LANGS = ["en", "ja", "ko", "fr", "es"]
SITEMAP_DATE = "2026-10-06"
BAD = 0


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


print("== 1) 正文六语属性完整性（根中文页） ==")
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
    print("  %s" % f)
    print("    article-body 内标签 %d 个，带 data-zh 的 %d 个；缺 en/ja/ko/fr/es 的 %d 个 %s"
          % (len(p.tags), len(dzh), len(missing), missing[:8]))
    print("    引号畸形 data-xx=\"\" : %d ; 属性值后裸字符: %d ; 裸 & : %d"
          % (len(re.findall(r'data-(?:zh|en|ja|ko|fr|es)=""', s)),
             len(re.findall(r'data-(?:zh|en|ja|ko|fr|es)="[^"]*"[a-zA-Z]', s)),
             len(re.findall(r'&(?!amp;|nbsp;|quot;|#)', s))))
    lds = re.findall(r'<script type="application/ld\+json">(.*?)</script>', s, re.S)
    for x in lds:
        json.loads(x)
    print("    JSON-LD %d 处合法" % len(lds))
    t = re.search(r'<title[^>]*>(.*?)</title>', s, re.S).group(1)
    d = re.search(r'<meta name="description"[^>]*?content="([^"]*)"', s, re.S)
    print("    title: %s" % t[:70])
    print("    desc : %s" % (d.group(1)[:60] if d else "NONE"))
    print("    h2 数: %d ; cta-box: %d ; 表格: %d"
          % (len(re.findall(r'<h2 ', s)), s.count('class="cta-box"'), s.count('<table>')))
if total_missing:
    BAD = 1

print("\n== 2) 中文正文字数（不含相关文章） ==")
for f in NEW:
    s = open(f, encoding="utf-8").read()
    body = re.search(r'<section class="article-body">.*?</section>', s, re.S).group(0)
    cut = body.find('相關文章')
    main = body[:cut] if cut != -1 else body
    zh_attrs = re.findall(r'data-zh="([^"]*)"', main)
    text = re.sub(r'<[^>]+>', '', re.sub(r'data-[a-z]+="[^"]*"', '', main))
    n = len(re.findall(r'[\u4e00-\u9fff]', ' '.join(zh_attrs))) + len(re.findall(r'[\u4e00-\u9fff]', text))
    print("  %-46s 正文汉字 = %d" % (os.path.basename(f), n))

print("\n== 3) 五语生成页残留检查 ==")
for f in NEW:
    slug = os.path.basename(f)
    for lang in LANGS:
        path = os.path.join(lang, f)
        if not os.path.exists(path):
            BAD = 1; print("  MISS %s" % path); continue
        s = open(path, encoding="utf-8").read()
        body = re.search(r'<section class="article-body">.*?</section>', s, re.S).group(0)
        body_ns = re.sub(r'<script.*?</script>', '', body, flags=re.S)
        cjk = len(re.findall(r'[\u4e00-\u9fff]', body_ns))
        d = re.search(r'<meta name="description" content="([^"]*)"', s)
        t = re.search(r'<title[^>]*>(.*?)</title>', s, re.S).group(1)
        can = re.search(r'<link rel="canonical" href="([^"]*)"', s).group(1)
        print("  %-50s 正文汉字=%-4d desc=%-3d canonical=%s" % (path, cjk, len(d.group(1)) if d else -1, can))
        print("      title=%s" % t[:66])
        if cjk > 0 and lang != "ja":
            BAD = 1; print("      ⚠ 残留汉字")
        if can != "https://taigetag.com/%s/%s" % (lang, f):
            BAD = 1; print("      ⚠ canonical 不符")

print("\n== 4) canonical 与 sitemap 逐 URL 一致性 ==")
sm = open("sitemap.xml", encoding="utf-8").read()
for f in NEW:
    slug = os.path.basename(f)
    for pre in ("blog/", "en/blog/", "ja/blog/", "ko/blog/", "fr/blog/", "es/blog/"):
        u = "https://taigetag.com/%s%s" % (pre, slug)
        ok = ("<loc>%s</loc>" % u) in sm
        if not ok:
            BAD = 1
        print("  %-6s %s %s" % (pre, "OK " if ok else "MISS", u))
    m = re.search(r'<loc>https://taigetag\.com/blog/%s</loc>\r?\n\s*<lastmod>([^<]*)</lastmod>' % re.escape(slug), sm)
    print("  lastmod=%s ; <loc> 总数=%d" % (m.group(1) if m else "?", sm.count("<loc>")))
for u in ["blog/index.html", "en/blog/index.html", "ja/blog/index.html",
          "ko/blog/index.html", "fr/blog/index.html", "es/blog/index.html"]:
    m = re.search(r'<loc>https://taigetag\.com/%s</loc>\r?\n\s*<lastmod>([^<]*)</lastmod>' % re.escape(u), sm)
    got = m.group(1) if m else "MISS"
    if got != SITEMAP_DATE:
        BAD = 1
    print("  %-24s lastmod=%s" % (u, got))

print("\n== 5) 列表页卡片（六语） ==")
for p in ["blog/index.html", "en/blog/index.html", "ja/blog/index.html",
          "ko/blog/index.html", "fr/blog/index.html", "es/blog/index.html"]:
    s = open(p, encoding="utf-8").read()
    hit = [os.path.basename(f) for f in NEW if os.path.basename(f) in s]
    grid = s.index('class="post-grid"')
    first = re.search(r'<a class="more" href="([^"]+)"', s[grid:])
    print("  %-24s 新卡片命中=%d %s ; 首卡=%s" % (p, len(hit), hit, first.group(1) if first else "?"))
    if len(hit) != 2:
        BAD = 1

print("\n== 6) 内链存在性（根目录文章相关文章 href） ==")
for f in NEW:
    s = open(f, encoding="utf-8").read()
    body = re.search(r'<section class="article-body">.*?</section>', s, re.S).group(0)
    for h in re.findall(r'href="([^"#?]+)"', body):
        if h.startswith("http"):
            continue
        p = os.path.normpath(os.path.join("blog", h))
        if not os.path.exists(p):
            BAD = 1; print("  MISS %s -> %s" % (f, h))
        else:
            print("  OK   %s -> %s" % (os.path.basename(f), h))

print("\n== 7) BUST_VERSION / 静态资源版本 ==")
mj = open("js/main.js", encoding="utf-8").read()
print("  BUST_VERSION = %s" % re.search(r'BUST_VERSION = "(\d+)"', mj).group(1))
s = open(NEW[0], encoding="utf-8").read()
print("  main.js 引用: %s ; css: %s" % (re.search(r'js/main\.js\?v=[\d.]+', s).group(0),
                                        re.search(r'css/style\.css\?v=[\d.]+', s).group(0)))

print("\n结论: %s" % ("需要修复" if BAD else "全部通过"))
raise SystemExit(BAD)
