# -*- coding: utf-8 -*-
"""新文章 6 语页面体检：存在性 / noindex / hreflang 条数 / href 转义 / title。"""
import os
import re

SLUGS = ["woven-label-loom-types-guide", "trim-attachment-strength-pull-test-guide"]
DIRS = ["blog", "en/blog", "fr/blog", "es/blog", "ja/blog", "ko/blog"]

for slug in SLUGS:
    print("==", slug)
    for d in DIRS:
        p = "%s/%s.html" % (d, slug)
        if not os.path.isfile(p):
            print("  缺失", p)
            continue
        s = open(p, encoding="utf-8").read()
        title = re.search(r"<title[^>]*>([^<]*)</title>", s).group(1)
        print("  %-8s noindex=%d hreflang=%2d href&#x27;=%d title=%s"
              % (d.split("/")[0], s.count("noindex"), len(re.findall(r'hreflang="', s)),
                 s.count("href=&#x27;"), title[:60]))
