# -*- coding: utf-8 -*-
"""校验 2026-11-22 08:00 两篇新文章：data-* 完整性 + 语言页中文残留 + noindex/hreflang。"""
import os
import re
from html.parser import HTMLParser

LANGS = ["zh", "en", "fr", "es", "ja", "ko"]
SLUGS = ["embroidery-backing-stabilizer-guide.html", "button-size-ligne-buttonhole-guide.html"]
ROOT = ["blog/" + s for s in SLUGS]


class P(HTMLParser):
    def __init__(self):
        super().__init__()
        self.bad = []
        self.attrs_seen = 0

    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        keys = [k for k in d if k.startswith("data-") and k[5:] in LANGS]
        if not keys:
            return
        self.attrs_seen += 1
        miss = [l for l in LANGS if "data-" + l not in d]
        if miss:
            self.bad.append((tag, miss, (d.get("data-zh") or "")[:40]))


for f in ROOT:
    s = open(f, encoding="utf-8").read()
    p = P()
    p.feed(s)
    print("%s: 带 data-* 元素 %d，缺语种元素 %d %s" % (f, p.attrs_seen, len(p.bad), p.bad[:3]))

print()
CJK = re.compile(r"[\u4e00-\u9fff]")
ALLOW = ["江磊", "Lei Jiang", "吳文潘", "Wenpan Wu", "陳清港", "Chen Qinggang",
         "泰閣", "東莞", "东莞", "台灣", "香港"]
for lang in ["en", "fr", "es", "ja", "ko"]:
    for slug in SLUGS:
        f = "%s/blog/%s" % (lang, slug)
        if not os.path.exists(f):
            print("MISSING", f)
            continue
        s = open(f, encoding="utf-8").read()
        s2 = re.sub(r"<script.*?</script>|<style.*?</style>|<!--.*?-->", " ", s, flags=re.S)
        vis = [m.group(1) for m in re.finditer(r">([^<>]+)<", s2) if CJK.search(m.group(1))]
        vis = [v.strip() for v in vis if v.strip() and not any(a in v for a in ALLOW)]
        attrs = [m.group(2) for m in re.finditer(r'(placeholder|title|alt|aria-label)="([^"]*)"', s2)
                 if CJK.search(m.group(2)) and not any(a in m.group(2) for a in ALLOW)]
        nl = len(re.findall(r'name="robots"', s))
        hl = len(re.findall(r'rel="alternate" hreflang=', s))
        langattr = re.search(r'<html[^>]*lang="([^"]*)"', s).group(1)
        print("%-4s %-40s lang=%-7s robots=%d hreflang=%d 可见中文=%d %s | 属性中文=%d %s" % (
            lang, slug, langattr, nl, hl, len(vis), vis[:2], len(attrs), attrs[:2]))

print()
for lang in ["", "en/", "fr/", "es/", "ja/", "ko/"]:
    f = "%sblog/index.html" % lang
    s = open(f, encoding="utf-8").read()
    print("%-22s 新卡片 %d" % (f, sum(1 for sl in SLUGS if sl in s)))
