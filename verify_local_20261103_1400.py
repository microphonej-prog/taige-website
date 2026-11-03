#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""本地校验：两篇新文章六语版本、canonical、JSON-LD、sitemap、卡片、语言纯净度"""
import re, json, os

SLUGS = ["hang-tag-scratch-off-guide.html", "woven-label-special-yarn-guide.html"]
LANGS = ["en", "ja", "ko", "fr", "es"]
TODAY = "2026-11-03"


def text(s):
    return re.sub(r"<[^>]+>", "", s).strip()


sm = open("sitemap.xml", encoding="utf-8").read()
print("sitemap <loc> 总数:", sm.count("<loc>"))
missing = []
for slug in SLUGS:
    for u in ["https://taigetag.com/blog/" + slug] + ["https://taigetag.com/%s/blog/%s" % (l, slug) for l in LANGS]:
        if "<loc>%s</loc>" % u not in sm:
            missing.append(u)
        pat = u + r"</loc>\r?\n\s*<lastmod>([^<]*)</lastmod>"
        m = re.search(pat, sm)
        if not m or m.group(1) != TODAY:
            missing.append("lastmod 异常: " + u)
print("sitemap 12 URL 缺失/异常:", len(missing))
for m in missing:
    print("   !!", m)

for slug in SLUGS:
    print("\n=== %s" % slug)
    paths = ["blog/" + slug] + ["%s/blog/%s" % (l, slug) for l in LANGS]
    for p in paths:
        assert os.path.exists(p), "缺文件 " + p
        s = open(p, encoding="utf-8").read()
        title_m = re.search(r"<title[^>]*>(.*?)</title>", s, re.S)
        title = text(title_m.group(1))
        canon = re.search(r'<link rel="canonical" href="([^"]+)"', s).group(1)
        ld = re.findall(r'<script type="application/ld\+json">(.*?)</script>', s, re.S)
        ld_ok = all((json.loads(x) is not None) for x in ld)
        body = s[s.index('<section class="article-body"'):s.index("</main>")]
        h2 = len(re.findall(r"<h2", body))
        visible = text(re.sub(r"<script.*?</script>", "", body, flags=re.S))
        cjk = len(re.findall(r"[\u4e00-\u9fff]", visible))
        attrs = len(re.findall(r"data-(?:zh|en|ja|ko|fr|es)=", body))
        print("  %-52s title=%s" % (p, title[:64]))
        print("      canonical=%s  jsonld=%d(%s)  h2=%d  正文CJK=%d  data属性=%d"
              % (canon, len(ld), "ok" if ld_ok else "BAD", h2, cjk, attrs))

# 卡片检查
idx = open("blog/index.html", encoding="utf-8").read()
for slug in SLUGS:
    print("卡片 %s: %s" % (slug, idx.count('href="%s"' % slug)))

# BUST_VERSION
mj = open("js/main.js", encoding="utf-8").read()
print("BUST_VERSION:", re.search(r'var BUST_VERSION = "([^"]+)"', mj).group(1))

# 六语页里不应出现别语言的 data 属性（gen_i18n 应已固化单语）
