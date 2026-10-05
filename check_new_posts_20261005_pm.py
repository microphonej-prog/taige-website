#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-05 下午批次校验：正文六语属性（HTMLParser）、引号畸形、JSON-LD、
生成页残留（en/ja/ko/fr/es）、canonical 与 sitemap 一致性、sitemap、blog 列表卡片。"""
import re, json, os, sys
from html.parser import HTMLParser

NEW = ["blog/sewing-thread-selection-guide.html", "blog/flame-retardant-trims-guide.html"]
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


print("== 1) 正文六语属性完整性（根中文页） ==")
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
    print("    JSON-LD %d 处全部合法" % len(lds))
    t = re.search(r'<title[^>]*>(.*?)</title>', s, re.S).group(1)
    print("    静态 title: %s" % t[:70])
    d = re.search(r'<meta name="description"[^>]*content="([^"]*)"', s, re.S)
    print("    静态 desc 汉字=%d : %s" % (len(re.findall(r'[\u4e00-\u9fff]', d.group(1))), d.group(1)[:60]))
    can = re.search(r'<link rel="canonical" href="([^"]*)"', s)
    print("    canonical: %s" % can.group(1))

print("== 2) 生成页（en/ja/ko/fr/es）残留检查 ==")
gen_issues = []
for f in NEW:
    for lang in LANGS:
        path = os.path.join(lang, f)
        s = open(path, encoding="utf-8").read()
        m0 = re.search(r'<section class="article-body">', s)
        m1 = re.search(r'</section>', s[m0.end():])
        body = s[m0.end():m0.end() + m1.start()]
        body_wo_json = re.sub(r'<script.*?</script>', '', body, flags=re.S)
        cjk = len(re.findall(r'[\u4e00-\u9fff]', body_wo_json))
        q = Collector()
        q.feed(s)
        residue = sum(1 for t, a in q.tags if any(k.startswith("data-") and k[5:] in
                      ("zh", "en", "ja", "ko", "fr", "es") for k in a))
        desc = re.search(r'<meta name="description" content="([^"]*)"', s)
        can = re.search(r'<link rel="canonical" href="([^"]*)"', s)
        ttl = re.search(r'<title>(.*?)</title>', s, re.S)
        print("  %-58s data-*残留=%d 正文汉字=%d desc=%d字符" % (
            path, residue, cjk, len(desc.group(1)) if desc else -1))
        print("      title: %s" % ttl.group(1)[:80])
        print("      canonical: %s" % (can.group(1) if can else "NONE"))
        if residue:
            gen_issues.append("%s data-* 残留 %d" % (path, residue))
        if lang != "ja" and cjk > 0:
            print("      ⚠ 非日文页正文含汉字 %d 个" % cjk)
        if not can:
            gen_issues.append("%s 缺 canonical" % path)

print("== 3) canonical 与 sitemap 一致性 ==")
sm = open("sitemap.xml", encoding="utf-8").read()
c123 = []
for f in NEW:
    slug = os.path.basename(f)
    for pre in ("blog/", "en/blog/", "ja/blog/", "ko/blog/", "fr/blog/", "es/blog/"):
        u = "https://taigetag.com/%s%s" % (pre, slug)
        assert "<loc>%s</loc>" % u in sm, u
        c123.append((pre, slug, u))
print("  12 个新 URL 全部存在；<loc> 总数=%d" % sm.count("<loc>"))
bad = 0
for pre, slug, u in c123:
    lang = pre.split("/")[0]
    path = ("blog/%s" % slug) if lang == "blog" else ("%s/blog/%s" % (lang, slug))
    s = open(path, encoding="utf-8").read()
    can = re.search(r'<link rel="canonical" href="([^"]*)"', s).group(1)
    if can != u:
        bad += 1
        print("  ✗ canonical 与 sitemap 不一致: %s -> %s（期望 %s）" % (path, can, u))
print("  canonical 不一致数量 = %d" % bad)

print("== 4) blog 列表页卡片 ==")
for p in ["blog/index.html"] + ["%s/blog/index.html" % l for l in LANGS]:
    s = open(p, encoding="utf-8").read()
    hit = [os.path.basename(f) for f in NEW if os.path.basename(f) in s]
    pos = s.find('<div class="post-grid">')
    first = re.search(r'href="([^"]+\.html)"', s[pos:pos + 3000])
    print("  %-26s 新卡片命中=%s 首卡=%s" % (p, hit, first.group(1) if first else "?"))

print("\n结论: data 缺失总数 = %d ; 生成页问题 = %d ; canonical 不一致 = %d" % (total_missing, len(gen_issues), bad))
sys.exit(1 if (total_missing or gen_issues or bad) else 0)
