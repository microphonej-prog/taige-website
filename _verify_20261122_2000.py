# -*- coding: utf-8 -*-
"""2026-11-22 20:00 交付自检：属性完整性 / noindex / hreflang / canonical / 死链 / 品牌名 / 卡片。"""
import os
import re
from html.parser import HTMLParser

LANGS = ["zh", "en", "fr", "es", "ja", "ko"]
SLUGS = ["hang-tag-paper-weight-conversion-guide.html", "vellum-translucent-hang-tags.html"]
FILES = ["blog/" + s for s in SLUGS] + ["%s/blog/%s" % (l, s) for s in SLUGS for l in LANGS[1:]]


class P(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.bad = []
        self.count = 0
        self.imgs = []

    def handle_starttag(self, tag, attrs):
        dd = dict(attrs)
        if "data-zh" in dd:
            self.count += 1
            miss = [l for l in LANGS if ("data-" + l) not in dd]
            if miss:
                self.bad.append((tag, miss, (dd.get("data-zh") or "")[:40]))
        if tag == "img":
            self.imgs.append(dd)


print("== 1) 六语属性完整性")
for f in FILES:
    if not os.path.exists(f):
        print("  MISSING", f)
        continue
    p = P()
    p.feed(open(f, encoding="utf-8").read())
    print("  %-58s 元素%3d 缺属性%d %s" % (f, p.count, len(p.bad), p.bad[:2]))

print("\n== 2) noindex / hreflang / canonical")
for f in FILES:
    s = open(f, encoding="utf-8").read()
    can = (re.search(r'<link rel="canonical" href="([^"]+)"', s) or ["", "NONE"])[1]
    print("  %-58s noindex=%d hreflang=%2d canonical=%s" % (
        f, s.count("noindex"), s.count('rel="alternate" hreflang='), can.replace("https://taigetag.com", "")))

print("\n== 3) 正文内链死链")
for f in FILES:
    s = open(f, encoding="utf-8").read()
    bad = []
    for h in re.findall(r'href="([^"]+)"', s):
        if h.startswith(("http", "mailto:", "tel:", "#", "javascript:", "data:")):
            continue
        t = h.split("?")[0].split("#")[0]
        if not t:
            continue
        p = os.path.normpath(os.path.join(os.path.dirname(f), t))
        if not os.path.exists(p):
            bad.append(h)
    print("  %-58s 死链%d %s" % (f, len(bad), bad[:4]))

print("\n== 4) 品牌名残留（TAIGE/Taige）")
for f in FILES + ["blog/index.html"] + ["%s/blog/index.html" % l for l in LANGS[1:]]:
    s = open(f, encoding="utf-8").read()
    n = len(re.findall(r"(?<![a-z])Taige|(?<![A-Za-z])TAIGE", s))
    if n:
        print("  ", f, n)

print("\n== 5) blog/index.html 新卡片（六语）")
for l in [""] + LANGS[1:]:
    f = "%sblog/index.html" % (l + "/" if l else "")
    s = open(f, encoding="utf-8").read()
    print("  %-28s cards=%d/%d" % (f, s.count(SLUGS[0]), s.count(SLUGS[1])))

print("\n== 6) hreflang 目标存在性")
for f in FILES:
    s = open(f, encoding="utf-8").read()
    miss = []
    for u in re.findall(r'<link rel="alternate" hreflang="[^"]+" href="([^"]+)"', s):
        rel = u.replace("https://taigetag.com/", "")
        p = rel if rel else "index.html"
        if p.endswith("/"):
            p += "index.html"
        if not os.path.exists(p):
            miss.append(u)
    print("  %-58s 缺目标%d %s" % (f, len(miss), miss[:3]))
