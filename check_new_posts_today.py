#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""校验新增文章：四语属性完整性（HTMLParser）、引号畸形、JSON-LD、生成页残留、sitemap。"""
import re, json, os
from html.parser import HTMLParser

NEW = ["blog/clothing-label-compliance-colombia.html", "blog/clothing-label-compliance-chile.html"]

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

print("== 1) 正文四语属性完整性 ==")
total_missing = 0
for f in NEW:
    s = open(f, encoding='utf-8').read()
    p = Collector(); p.feed(s)
    dzh = [(t, a) for t, a in p.tags if "data-zh" in a]
    missing = []
    for t, a in dzh:
        for need in ("data-en", "data-fr", "data-es"):
            if not a.get(need, "").strip():
                missing.append((t, need))
    total_missing += len(missing)
    print("  %s" % f)
    print("    article-body 内标签 %d 个，其中带 data-zh 的 %d 个；缺 en/fr/es 的 %d 个 %s"
          % (len(p.tags), len(dzh), len(missing), missing[:8]))
    print("    引号畸形 data-xx=\"\" : %d ; 属性值后裸字符: %d ; 裸 & : %d"
          % (len(re.findall(r'data-(?:zh|en|fr|es)=\"\"', s)),
             len(re.findall(r'data-(?:zh|en|fr|es)=\"[^\"]*\"[a-zA-Z]', s)),
             len(re.findall(r'&(?!amp;|nbsp;|quot;|#)', s))))
    lds = re.findall(r'<script type="application/ld\+json">(.*?)</script>', s, re.S)
    for x in lds:
        json.loads(x)
    print("    JSON-LD %d 处全部合法" % len(lds))
    t = re.search(r'<title[^>]*>(.*?)</title>', s, re.S).group(1)
    print("    静态 title: %s" % t[:60])

print("== 2) 生成页（en/fr/es）残留检查 ==")
for f in NEW:
    for lang in ("en", "fr", "es"):
        path = os.path.join(lang, f)
        s = open(path, encoding='utf-8').read()
        m0 = re.search(r'<section class="article-body">', s)
        m1 = re.search(r'</section>', s[m0.end():])
        body = s[m0.end():m0.end() + m1.start()]
        cjk = len(re.findall(r'[\u4e00-\u9fff]', re.sub(r'<script.*?</script>', '', body, flags=re.S)))
        q = Collector(); q.feed(s)
        residue = sum(1 for t, a in q.tags if any(k.startswith("data-") and k[5:] in
                      ("zh", "en", "fr", "es") for k in a))
        desc = re.search(r'<meta name="description" content="([^"]*)"', s)
        print("  %-58s data-*残留=%d 正文汉字=%d desc=%d字符" %
              (path, residue, cjk, len(desc.group(1)) if desc else -1))

print("== 3) sitemap ==")
sm = open("sitemap.xml", encoding="utf-8").read()
for f in NEW:
    slug = os.path.basename(f)
    for pre in ("blog/", "en/blog/", "fr/blog/", "es/blog/"):
        u = "https://taigetag.com/%s%s" % (pre, slug)
        assert "<loc>%s</loc>" % u in sm, u
print("  8 个新 URL 全部存在；<loc> 总数=%d" % sm.count("<loc>"))

print("== 4) blog 列表页卡片 ==")
for p in ("blog/index.html", "en/blog/index.html", "fr/blog/index.html", "es/blog/index.html"):
    s = open(p, encoding='utf-8').read()
    hit = [os.path.basename(f) for f in NEW if os.path.basename(f) in s]
    print("  %-26s 新卡片命中=%s" % (p, hit))

print("\n结论: 缺失总数 = %d" % total_missing)
raise SystemExit(1 if total_missing else 0)
