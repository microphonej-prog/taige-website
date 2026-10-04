#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-04 晚间批次校验：正文六语属性（HTMLParser）、引号畸形、JSON-LD、链接可达、
生成页残留（en/ja/ko/fr/es）、sitemap、blog 列表卡片。"""
import re, json, os, sys
from html.parser import HTMLParser

NEW = ["blog/lining-fabric-selection-guide.html", "blog/webbing-tape-selection-guide.html"]
LANGS = ["en", "ja", "ko", "fr", "es"]
fails = []


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
for f in NEW:
    s = open(f, encoding="utf-8").read()
    p = Collector(); p.feed(s)
    dzh = [(t, a) for t, a in p.tags if "data-zh" in a]
    missing = []
    for t, a in dzh:
        for need in ("data-en", "data-ja", "data-ko", "data-fr", "data-es"):
            if not a.get(need, "").strip():
                missing.append((t, need))
    fails += missing
    print("  %s" % f)
    print("    article-body 内标签 %d，带 data-zh 的 %d；缺 en/ja/ko/fr/es 的 %d %s"
          % (len(p.tags), len(dzh), len(missing), missing[:8]))
    print("    引号畸形 data-xx=\"\" : %d ; 属性值后裸字符: %d ; 裸 & : %d"
          % (len(re.findall(r'data-(?:zh|en|ja|ko|fr|es)=""', s)),
             len(re.findall(r'data-(?:zh|en|ja|ko|fr|es)="[^"]*"[a-zA-Z]', s)),
             len(re.findall(r'&(?!amp;|nbsp;|quot;|#)', s))))
    lds = re.findall(r'<script type="application/ld\+json">(.*?)</script>', s, re.S)
    for x in lds:
        json.loads(x)
    print("    JSON-LD %d 处全部合法" % len(lds))
    print("    静态 title: %s" % re.search(r'<title[^>]*>(.*?)</title>', s, re.S).group(1)[:70])
    print("    canonical: %s" % re.search(r'<link rel="canonical" href="([^"]*)"', s).group(1))
    # 内部链接可达性
    print("    内部链接检查:")
    for href in sorted(set(re.findall(r'href="([^"#?]+\.html)"', s))):
        if href.startswith("http"):
            continue  # canonical / hreflang 绝对地址，非文件链接
        path = os.path.normpath(os.path.join("blog", href))
        ok = os.path.exists(path)
        if not ok:
            fails.append("dead link %s in %s" % (href, f))
        print("      %-46s %s" % (href, "OK" if ok else "缺失!"))

print("== 2) 生成页（en/ja/ko/fr/es）残留检查 ==")
for f in NEW:
    for lang in LANGS:
        path = os.path.join(lang, f)
        s = open(path, encoding="utf-8").read()
        m0 = re.search(r'<section class="article-body">', s)
        m1 = re.search(r'</section>', s[m0.end():])
        body = s[m0.end():m0.end() + m1.start()]
        cjk = len(re.findall(r'[\u4e00-\u9fff]', re.sub(r'<script.*?</script>', '', body, flags=re.S)))
        q = Collector(); q.feed(s)
        residue = sum(1 for t, a in q.tags if any(k.startswith("data-") and k[5:] in
                      ("zh", "en", "ja", "ko", "fr", "es") for k in a))
        desc = re.search(r'<meta name="description" content="([^"]*)"', s)
        can = re.search(r'<link rel="canonical" href="([^"]*)"', s)
        ttl = re.search(r'<title>(.*?)</title>', s, re.S)
        if residue:
            fails.append("data-* 残留 %s" % path)
        print("  %-56s data-*残留=%d 正文汉字=%d desc=%d字符 canonical=%s" % (
            path, residue, cjk, len(desc.group(1)) if desc else -1, can.group(1) if can else "NONE"))
        print("      title: %s" % ttl.group(1)[:84])

print("== 3) sitemap ==")
sm = open("sitemap.xml", encoding="utf-8").read()
for f in NEW:
    slug = os.path.basename(f)
    for pre in ("blog/", "en/blog/", "ja/blog/", "ko/blog/", "fr/blog/", "es/blog/"):
        u = "https://taigetag.com/%s%s" % (pre, slug)
        if "<loc>%s</loc>" % u not in sm:
            fails.append("sitemap 缺 %s" % u)
print("  12 个新 URL 全部存在；<loc> 总数=%d" % sm.count("<loc>"))
for u in ["https://taigetag.com/blog/index.html"] + ["https://taigetag.com/%s/blog/index.html" % l for l in LANGS]:
    blk = re.search(r'<loc>%s</loc>\s*<lastmod>([^<]*)</lastmod>' % re.escape(u), sm)
    d = blk.group(1) if blk else "缺失"
    if d != "2026-10-04":
        fails.append("blog index lastmod=%s (%s)" % (d, u))
    print("  %-46s lastmod=%s" % (u, d))

print("== 4) blog 列表页卡片 ==")
for p in ["blog/index.html"] + ["%s/blog/index.html" % l for l in LANGS]:
    s = open(p, encoding="utf-8").read()
    hit = [os.path.basename(f) for f in NEW if os.path.basename(f) in s]
    pos = s.find('<div class="post-grid">')
    first = re.search(r'href="([^"]+\.html)"', s[pos:pos + 3000])
    if len(hit) != 2:
        fails.append("卡片缺失 %s -> %s" % (p, hit))
    print("  %-26s 新卡片命中=%s 首卡=%s" % (p, hit, first.group(1) if first else "?"))

print("== 5) BUST_VERSION / 版本号 ==")
mj = open("js/main.js", encoding="utf-8").read()
bv = re.search(r'var BUST_VERSION = "([^"]*)"', mj).group(1)
print("  BUST_VERSION = %s" % bv)
if bv != "136":
    fails.append("BUST_VERSION=%s" % bv)
for f in NEW:
    s = open(f, encoding="utf-8").read()
    print("  %-46s css=%s js=%s" % (f,
          re.search(r'style\.css\?v=(\d+)', s).group(1) if re.search(r'style\.css\?v=(\d+)', s) else "?",
          re.search(r'main\.js\?v=([\d.]+)', s).group(1) if re.search(r'main\.js\?v=([\d.]+)', s) else "?"))

print("\n结论: 失败项 %d %s" % (len(fails), fails[:10]))
sys.exit(1 if fails else 0)
