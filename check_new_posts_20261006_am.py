#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-06 上午批次校验：六语属性完整性、引号畸形、JSON-LD、生成页残留、sitemap、列表卡片、内链。"""
import re, json, os
from html.parser import HTMLParser

NEW = ["blog/garment-security-tag-guide.html", "blog/garment-wash-dye-trims-guide.html"]
LANGS = ["en", "ja", "ko", "fr", "es"]

BAD = 0


class Body(HTMLParser):
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


print("== 1) 正文六语属性完整性（根目录 zh-Hant 版）==")
total_missing = 0
for f in NEW:
    s = open(f, encoding="utf-8").read()
    p = Body(); p.feed(s)
    dzh = [(t, a) for t, a in p.tags if "data-zh" in a]
    missing = []
    for t, a in dzh:
        for need in ("data-en", "data-fr", "data-es", "data-ja", "data-ko"):
            if not a.get(need, "").strip():
                missing.append((t, need))
    total_missing += len(missing)
    print("  %s" % f)
    print("    article-body 标签 %d 个，带 data-zh 的 %d 个；缺 en/fr/es/ja/ko 的 %d 个 %s"
          % (len(p.tags), len(dzh), len(missing), missing[:8]))
    print("    引号畸形 data-xx=\"\" : %d ; 属性值后裸字符: %d ; 裸 & : %d"
          % (len(re.findall(r'data-(?:zh|en|fr|es|ja|ko)=""', s)),
             len(re.findall(r'data-(?:zh|en|fr|es|ja|ko)="[^"]*"[a-zA-Z]', s)),
             len(re.findall(r'&(?!amp;|nbsp;|quot;|#)', s))))
    lds = re.findall(r'<script type="application/ld\+json">(.*?)</script>', s, re.S)
    for x in lds:
        json.loads(x)
    print("    JSON-LD %d 处合法" % len(lds))
    t = re.search(r'<title[^>]*>(.*?)</title>', s, re.S).group(1)
    d = re.search(r'<meta name="description"[^>]*?content="([^"]*)"', s, re.S)
    print("    title: %s" % t[:70])
    print("    desc : %s" % (d.group(1)[:70] if d else "NONE"))
    print("    h2 数: %d ; cta-box: %d ; 相关文章块: %d"
          % (len(re.findall(r'<h2 ', s)), s.count('class="cta-box"'), s.count('相关文章')))
    if total_missing:
        BAD = 1

print("\n== 2) 五语生成页残留检查 ==")
for f in NEW:
    slug = os.path.basename(f)
    for lang in LANGS:
        path = os.path.join(lang, f)
        s = open(path, encoding="utf-8").read()
        m0 = re.search(r'<section class="article-body">', s)
        m1 = re.search(r'</section>', s[m0.end():])
        body = s[m0.end():m0.end() + m1.start()]
        body_no_script = re.sub(r'<script.*?</script>', '', body, flags=re.S)
        cjk = len(re.findall(r'[\u4e00-\u9fff]', body_no_script))
        han_simp = len(re.findall(r'[\u4e00-\u9fff]', re.sub(
            r'<script.*?</script>', '', re.search(
                r'<section class="article-body">.*?</section>', s, re.S).group(0), flags=re.S)))
        q = Body(); q.feed(s)
        residue = sum(1 for t, a in q.tags if any(
            k.startswith("data-") and k[5:] in ("zh", "en", "fr", "es", "ja", "ko") for k in a))
        d = re.search(r'<meta name="description" content="([^"]*)"', s)
        t = re.search(r'<title[^>]*>(.*?)</title>', s, re.S).group(1)
        print("  %-52s data-*残留=%-3d 正文汉字=%-4d desc=%-3d title=%s"
              % (path, residue, cjk, len(d.group(1)) if d else -1, t[:38]))

print("\n== 3) 根目录页（繁体）残留简体检查 ==")
SIMP = re.compile(r'[这件为准发后词汇语标贴纸织钢银费说过选购实际]')
for f in NEW:
    s = open(f, encoding="utf-8").read()
    body = re.search(r'<section class="article-body">.*?</section>', s, re.S).group(0)
    hits = ['%s' % m for m in re.findall(r'.{6}[这件为准发后词汇语标贴纸织钢银费说过选购实际].{6}', body)][:6]
    print("  %s 简体嫌疑 %d 处 %s" % (f, len(hits), hits))

print("\n== 4) sitemap ==")
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
    print("  %-24s lastmod=%s" % (u, m.group(1) if m else "MISS"))

print("\n== 5) 列表页卡片 ==")
for p in ["blog/index.html", "en/blog/index.html", "ja/blog/index.html",
          "ko/blog/index.html", "fr/blog/index.html", "es/blog/index.html"]:
    s = open(p, encoding="utf-8").read()
    hit = [os.path.basename(f) for f in NEW if os.path.basename(f) in s]
    grid = s.index('class="post-grid"')
    first = re.search(r'<a class="more" href="([^"]+)"', s[grid:])
    print("  %-24s 新卡片命中=%d %s ; 首卡=%s" % (p, len(hit), hit, first.group(1) if first else "?"))

print("\n== 6) 内链存在性（根目录文章里的相关文章 href）==")
for f in NEW:
    s = open(f, encoding="utf-8").read()
    body = re.search(r'<section class="article-body">.*?</section>', s, re.S).group(0)
    for h in re.findall(r'href="([^"#?]+)"', body):
        if h.startswith("http"):
            continue
        p = os.path.normpath(os.path.join("blog", h))
        if not os.path.exists(p):
            BAD = 1
            print("  MISS %s -> %s" % (f, h))
        else:
            print("  OK   %s -> %s" % (os.path.basename(f), h))

print("\n== 7) BUST_VERSION / 版本号 ==")
mj = open("js/main.js", encoding="utf-8").read()
print("  BUST_VERSION = %s" % re.search(r'BUST_VERSION = "(\d+)"', mj).group(1))
s = open(NEW[0], encoding="utf-8").read()
print("  main.js 引用: %s ; css: %s" % (re.search(r'js/main\.js\?v=[\d.]+', s).group(0),
                                        re.search(r'css/style\.css\?v=[\d.]+', s).group(0)))

print("\n结论: %s" % ("需要修复" if BAD else "全部通过"))
raise SystemExit(BAD)
