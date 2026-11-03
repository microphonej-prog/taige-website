#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""语言纯净度 + 内链存在性检查"""
import re, os

SLUGS = ["label-color-metamerism-guide.html", "hang-tag-moisture-curl-guide.html"]
LANGS = ["en", "ja", "ko", "fr", "es"]
SIMPLIFIED = "们这说为计时后东车马门问间问题优级认证质检测输运储湿复应类标签纸张织订购价钱费单价总总数个种类别区单双面里外头开关闭"

for slug in SLUGS:
    for p in ["blog/" + slug] + ["%s/blog/%s" % (l, slug) for l in LANGS]:
        s = open(p, encoding="utf-8").read()
        body = s[s.index('<section class="article-body"'):s.index("</main>")]
        txt = re.sub(r"<[^>]+>", "", body)
        bad = [(c, txt[max(0, txt.find(c) - 20):txt.find(c) + 10]) for c in SIMPLIFIED if c in txt]
        if bad:
            print("  !! %s 含疑似简体字:" % p, bad[:6])
        # 内链
        for href in re.findall(r'href="([^"#]+)"', body):
            if href.startswith(("http", "mailto", "../")):
                continue
            base = os.path.dirname(p)
            if not os.path.exists(os.path.join(base, href)):
                print("  !! %s 死链 %s" % (p, href))
print("纯净度与内链检查完成")

# 六语 title 抓取
for slug in SLUGS:
    print("\n" + slug)
    for p in ["blog/" + slug] + ["%s/blog/%s" % (l, slug) for l in LANGS]:
        s = open(p, encoding="utf-8").read()
        t = re.sub(r"<[^>]+>", "", re.search(r"<title[^>]*>(.*?)</title>", s, re.S).group(1))
        d = re.search(r'<meta name="description"[^>]*content="([^"]*)"', s, re.S)
        print("  %-50s %s" % (p, t))
        print("     desc:", (d.group(1)[:70] if d else "缺失"))
