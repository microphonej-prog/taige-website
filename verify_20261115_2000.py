# -*- coding: utf-8 -*-
"""验收：语言页存在性 / noindex / hreflang 条数 / 六语属性完整性 / 列表卡片 / sitemap。"""
import os
import re

SLUGS = ["fringe-tassel-pom-pom-trims-guide", "cord-locks-toggles-drawstring-hardware-guide"]
LANGS = ["en", "fr", "es", "ja", "ko"]
ATTR = re.compile(r'data-(zh|en|fr|es|ja|ko)="')

for slug in SLUGS:
    root = "blog/%s.html" % slug
    s = open(root, encoding="utf-8").read()
    # 元素级属性完整性：逐个开始标签检查
    tags = re.findall(r"<(?:p|h1|h2|li|td|th|div|span|a|title|meta)\b[^>]*data-zh=\"[^\"]*\"[^>]*>", s)
    missing = 0
    for t in tags:
        have = set(ATTR.findall(t))
        if have != {"zh", "en", "fr", "es", "ja", "ko"}:
            missing += 1
            print("  缺属性:", sorted({"zh", "en", "fr", "es", "ja", "ko"} - have), t[:90])
    print("%s 根页属性元素 %d，缺语言属性元素 %d" % (slug, len(tags), missing))
    for l in LANGS:
        f = "%s/blog/%s.html" % (l, slug)
        if not os.path.exists(f):
            print("  ✗ 缺失", f)
            continue
        p = open(f, encoding="utf-8").read()
        hl = len(re.findall(r'hreflang="', p))
        ni = "noindex" in p
        card = slug in open("%s/blog/index.html" % l, encoding="utf-8").read()
        print("  %s: 存在 hreflang=%d noindex=%s 列表卡片=%s" % (f, hl, ni, card))
    card0 = slug in open("blog/index.html", encoding="utf-8").read()
    print("  根 blog/index.html 卡片:", card0)

sm = open("sitemap.xml", encoding="utf-8").read()
for slug in SLUGS:
    n = len(re.findall(r"<loc>https://taigetag\.com/(?:en/|fr/|es/|ja/|ko/)?blog/%s\.html</loc>" % slug, sm))
    print("sitemap %s: %d 条（应 6）" % (slug, n))
