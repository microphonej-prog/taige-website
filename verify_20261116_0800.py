# -*- coding: utf-8 -*-
"""2026-11-16 08:00 新增 2 篇的本地验收：属性完整度 / 语言纯净度 / 内链存在 / 无 de・pt 残留。"""
import os
import re
from html.parser import HTMLParser

LANGS = ["zh", "en", "fr", "es", "ja", "ko"]
SLUGS = ["bag-hardware-d-rings-swivel-hooks-guide", "snap-fastener-press-stud-guide"]
DIRS = ["blog", "en/blog", "fr/blog", "es/blog", "ja/blog", "ko/blog"]


class P(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tags = []
        self.links = []

    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        self.tags.append((tag, d))
        if tag == "a" and d.get("href"):
            self.links.append(d["href"])


print("=== 1) data-* 属性完整度（缺任一语种即报） ===")
bad_total = 0
for dr in DIRS:
    for slug in SLUGS:
        f = "%s/%s.html" % (dr, slug)
        s = open(f, encoding="utf-8").read()
        p = P()
        p.feed(s)
        tags_with_zh = [d for t, d in p.tags if "data-zh" in d]
        missing = 0
        detail = []
        for d in tags_with_zh:
            lack = [l for l in LANGS if ("data-%s" % l) not in d]
            if lack:
                missing += 1
                detail.append(lack)
        stale = [k for k in ("data-de", "data-pt") if (" " + k + "=") in s]
        print("%-60s 元素%d 缺语言元素%d de/pt残留%s" % (f, len(tags_with_zh), missing, stale or "无"))
        if missing:
            print("    缺:", detail[:3])
        bad_total += missing
print("缺失元素合计:", bad_total)

print("\n=== 2) 语言页正文语言抽查（前 120 字） ===")
for dr in DIRS:
    f = "%s/%s.html" % (dr, SLUGS[0])
    s = open(f, encoding="utf-8").read()
    m = re.search(r"<p class=\"article-lead\"[^>]*>(.*?)</p>", s, re.S) or re.search(r"<article-body.*?<p>(.*?)</p>", s, re.S)
    if not m:
        m = re.search(r"<h1[^>]*>(.*?)</h1>", s, re.S)
    txt = re.sub(r"<[^>]+>", "", m.group(1)).strip()[:120]
    print("%-60s %s" % (f, txt))

print("\n=== 3) 相关文章内链目标存在性 ===")
miss = 0
for dr in DIRS:
    for slug in SLUGS:
        f = "%s/%s.html" % (dr, slug)
        s = open(f, encoding="utf-8").read()
        for h in re.findall(r'<a[^>]+href="([^"]+)"', s):
            if h.startswith(("http", "mailto:", "tel:", "#", "javascript:")):
                continue
            t = h.split("?")[0].split("#")[0]
            if not t:
                continue
            path = os.path.normpath(os.path.join(os.path.dirname(f), t))
            if not os.path.exists(path):
                print("  死链:", f, "->", h, "(解析:", path, ")")
                miss += 1
print("死链数:", miss)
