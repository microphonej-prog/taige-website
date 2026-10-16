#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-16 本日第二批（内衣辅料 / 客供料）本地校验：六语属性完整性、引号畸形、JSON-LD、
语言页残留、正文规模、内链、列表页卡片、sitemap、BUST_VERSION。"""
import re, json, os
from html.parser import HTMLParser

SLUGS = ["lingerie-bra-trims-guide.html", "client-supplied-trim-materials-guide.html"]
LANGS = ["en", "ja", "ko", "fr", "es"]
ATTRS = ["data-zh", "data-en", "data-ja", "data-ko", "data-fr", "data-es"]
fail = 0


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


print("== 1) 正文六语属性完整性（HTMLParser） ==")
for slug in SLUGS:
    p = "blog/%s" % slug
    s = open(p, encoding="utf-8").read()
    c = Collector(); c.feed(s)
    dzh = [(t, a) for t, a in c.tags if "data-zh" in a]
    missing = []
    for t, a in dzh:
        for need in ("data-en", "data-ja", "data-ko", "data-fr", "data-es"):
            if not a.get(need, "").strip():
                missing.append((t, need))
    print("  %s" % p)
    print("    article-body 标签 %d 个，带 data-zh 的 %d 个，缺其它语 %d 个 %s"
          % (len(c.tags), len(dzh), len(missing), missing[:8]))
    fail += len(missing)
    print("    引号畸形 data-xx=\"\" : %d ; 属性值后裸字符: %d ; 裸 & : %d"
          % (len(re.findall(r'data-(?:zh|en|ja|ko|fr|es)=""', s)),
             len(re.findall(r'data-(?:zh|en|ja|ko|fr|es)="[^"]*"[a-zA-Z]', s)),
             len(re.findall(r'&(?!amp;|nbsp;|quot;|#)', s))))
    lds = re.findall(r'<script type="application/ld\+json">(.*?)</script>', s, re.S)
    for x in lds:
        json.loads(x)
    print("    JSON-LD %d 处全部合法" % len(lds))
    print("    title: %s" % re.search(r'<title[^>]*>.*?</title>', s, re.S).group(0)[:120])
    dm = re.search(r'<meta name="description".*?content="([^"]*)">', s, re.S)
    print("    desc content 长度: %d" % len(dm.group(1)))
    # 内链存在性
    for m in re.finditer(r'class="article-body".*?</section>', s, re.S):
        body = m.group(0)
        for href in re.findall(r'href="([^"#]+)"', body):
            if href.startswith("http"):
                continue
            tgt = os.path.normpath(os.path.join("blog", href))
            if not os.path.exists(tgt):
                print("    !! 断链 %s -> %s" % (href, tgt)); fail += 1
        print("    正文内链检查完成（%d 个本地链接）" % len([h for h in re.findall(r'href="([^"#]+)"', body) if not h.startswith("http")]))

print("== 2) 六语页面存在性 + 残留 + 正文规模 ==")
for slug in SLUGS:
    for lang in ["zh"] + LANGS:
        p = "blog/%s" % slug if lang == "zh" else "%s/blog/%s" % (lang, slug)
        if not os.path.exists(p):
            print("  !! 缺文件 %s" % p); fail += 1; continue
        s = open(p, encoding="utf-8").read()
        m0 = re.search(r'<section class="article-body">', s)
        m1 = re.search(r'</section>', s[m0.end():])
        body = s[m0.end():m0.end() + m1.start()]
        plain = re.sub(r'<[^>]+>', '', re.sub(r'<script.*?</script>', '', body, flags=re.S))
        c = Collector(); c.feed(s)
        residue = sum(1 for t, a in c.tags if any(k.startswith("data-") and k[5:] in
                      ("zh", "en", "fr", "es", "ja", "ko") for k in a))
        t = re.search(r'<title[^>]*>(.*?)</title>', s, re.S).group(1)
        cjk = len(re.findall(r'[\u4e00-\u9fff]', plain))
        print("  %-52s title=%-58s 正文%s字 data-*残留=%d 汉字=%d"
              % (p, t[:56], len(plain), residue, cjk))
        if lang in ("en", "fr", "es") and cjk > 0:
            print("    !! %s 页正文残留汉字 %d" % (lang, cjk)); fail += 1

print("== 3) 列表页卡片（六语） ==")
for lang in ["zh"] + LANGS:
    p = "blog/index.html" if lang == "zh" else "%s/blog/index.html" % lang
    s = open(p, encoding="utf-8").read()
    grid = s.split('<div class="post-grid">', 1)[1][:4200]
    hits = [sl for sl in SLUGS if sl in s]
    top = [sl for sl in SLUGS if sl in grid]
    print("  %-28s 命中=%s 顶部=%s" % (p, hits, top))
    if len(hits) != 2 or len(top) != 2:
        print("    !! 卡片缺失或不在顶部"); fail += 1

print("== 4) sitemap ==")
sm = open("sitemap.xml", encoding="utf-8").read()
for slug in SLUGS:
    for pre in ["blog/"] + ["%s/blog/" % l for l in LANGS]:
        u = "https://taigetag.com/%s%s" % (pre, slug)
        if "<loc>%s</loc>" % u not in sm:
            print("  !! 缺 URL %s" % u); fail += 1
print("  新增 12 个 URL 全部存在；<loc> 总数=%d" % sm.count("<loc>"))
for pre in ["blog/"] + ["%s/blog/" % l for l in LANGS]:
    u = "https://taigetag.com/%sindex.html" % pre
    m = re.search(r'<loc>%s</loc>\r?\n\s*<lastmod>([^<]*)</lastmod>' % re.escape(u), sm)
    ok = m and m.group(1) == "2026-10-16"
    print("  blog index lastmod %s -> %s %s" % (u, m.group(1) if m else "N/A", "OK" if ok else "!!"))
    if not ok:
        fail += 1

print("== 5) BUST_VERSION ==")
mj = open("js/main.js", encoding="utf-8").read()
v = re.search(r'var BUST_VERSION = "(\d+)";', mj).group(1)
print("  BUST_VERSION = %s %s" % (v, "OK" if v == "163" else "!!"))
if v != "163":
    fail += 1

print("== 6) 语言页 canonical / hreflang ==")
for lang in LANGS:
    for slug in SLUGS:
        p = "%s/blog/%s" % (lang, slug)
        s = open(p, encoding="utf-8").read()
        canon = re.search(r'<link rel="canonical" href="([^"]*)"', s).group(1)
        want = "https://taigetag.com/%s/blog/%s" % (lang, slug)
        alts = re.findall(r'hreflang="([^"]*)" href="([^"]*)"', s)
        ok = canon == want and len(alts) >= 6
        print("  %-52s canonical OK=%s hreflang=%d" % (p, canon == want, len(alts)))
        if not ok:
            fail += 1

print("\n结论: 问题数 = %d" % fail)
raise SystemExit(1 if fail else 0)
