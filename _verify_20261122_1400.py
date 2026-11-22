# -*- coding: utf-8 -*-
"""2026-11-22 14:00 交付自检：属性完整性 / noindex / hreflang / canonical / 死链 / 品牌名。"""
import glob
import os
import re
from html.parser import HTMLParser

LANGS = ["zh", "en", "fr", "es", "ja", "ko"]
SLUGS = ["clothing-label-compliance-indonesia.html", "eu-csddd-apparel-trims-suppliers.html"]
FILES = ["blog/" + s for s in SLUGS] + ["%s/blog/%s" % (l, s) for s in SLUGS for l in LANGS[1:]]


class P(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.bad = []
        self.count = 0

    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        if "data-zh" in d:
            self.count += 1
            miss = [l for l in LANGS if ("data-" + l) not in d]
            if miss:
                self.bad.append((tag, miss, (d.get("data-zh") or "")[:40]))


print("== 1) 六语属性完整性")
for f in FILES:
    if not os.path.exists(f):
        print("  MISSING", f); continue
    p = P(); p.feed(open(f, encoding="utf-8").read())
    print("  %-55s 元素%3d 缺属性%d %s" % (f, p.count, len(p.bad), p.bad[:3]))

print("\n== 2) noindex / hreflang / canonical")
for f in FILES:
    s = open(f, encoding="utf-8").read()
    print("  %-55s noindex=%d hreflang=%2d canonical=%s" % (
        f, s.count("noindex"), s.count('rel="alternate" hreflang='),
        (re.search(r'<link rel="canonical" href="([^"]+)"', s) or ["", "NONE"])[1].replace("https://taigetag.com", "")))

print("\n== 3) sitemap 对照")
sm = open("sitemap.xml", encoding="utf-8").read()
for f in FILES:
    if f.startswith("blog/"):
        url = "https://taigetag.com/" + f
    else:
        lang, _, rest = f.partition("/")
        url = "https://taigetag.com/%s/%s" % (lang, rest)
    print("  %-55s in_sitemap=%s" % (f, ("<loc>%s</loc>" % url) in sm))

print("\n== 4) 死链（新页 href 目标存在性）")
missing = 0
for f in FILES:
    s = open(f, encoding="utf-8").read()
    for h in re.findall(r'href="([^"]+)"', s):
        if h.startswith(("http", "mailto:", "tel:", "#", "javascript:", "data:")):
            continue
        t = h.split("?")[0].split("#")[0]
        if not t:
            continue
        p2 = os.path.normpath(os.path.join(os.path.dirname(f), t))
        if not os.path.exists(p2):
            print("  DEAD", f, h); missing += 1
print("  死链数:", missing)

print("\n== 5) 语言页语言抽检（title + 首段）")
for f in FILES[1:]:
    s = open(f, encoding="utf-8").read()
    t = re.sub(r"<[^>]+>", "", re.search(r"<title[^>]*>(.*?)</title>", s, re.S).group(1))
    h1 = re.sub(r"<[^>]+>", "", re.search(r"<h1[^>]*>(.*?)</h1>", s, re.S).group(1))
    cjk = len(re.findall(r"[\u4e00-\u9fff]", h1))
    print("  %-55s title=%s | h1=%s | h1汉字=%d" % (f, t[:46], h1[:40], cjk))

print("\n== 6) 品牌名残留（应仅域名/邮箱）")
bad = []
for f in FILES:
    s = open(f, encoding="utf-8").read()
    n = len(re.findall(r"\bTAIGE\b|\bTaige\b", s))
    if n:
        bad.append((f, n))
print("  TAIGE/Taige 残留文件:", len(bad), bad[:5])

print("\n== 7) 语言页里可接受中文残留量（人名/JSON-LD）")
for f in FILES[1:]:
    s = open(f, encoding="utf-8").read()
    s2 = re.sub(r"<script.*?</script>|<style.*?</style>|<!--.*?-->", " ", s, flags=re.S)
    cjk = len(re.findall(r"[\u4e00-\u9fff]", re.sub(r"<[^>]+>", " ", s2)))
    print("  %-55s 正文汉字 %d" % (f, cjk))
