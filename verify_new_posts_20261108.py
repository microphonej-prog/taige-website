#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-11-08 新文章验收：属性完整性、noindex、hreflang 条数、语言页正文纯净度、卡片。"""
import glob
import json
import re

SLUGS = ["silica-gel-desiccant-apparel-packaging.html", "care-label-roll-direction-core-guide.html"]
LANGS = ["en", "fr", "es", "ja", "ko", "de", "pt"]
CJK = re.compile(r"[\u4e00-\u9fff]")

print("=== 1) 中文源页属性完整性 (data-* 缺失元素) ===")
for slug in SLUGS:
    s = open("blog/" + slug, encoding="utf-8").read()
    body = s[s.index('class="article-body"'):]
    tags = re.findall(r"<(?:p|h2|h3|li|td|th|span|a|div)\b[^>]*data-zh=[^>]*>", body)
    bad = []
    for t in tags:
        miss = [l for l in ["en", "fr", "es", "ja", "ko", "de", "pt"] if ('data-%s="' % l) not in t]
        if miss:
            bad.append((miss, t[:90]))
    print("%s: 元素 %d 个, 缺属性 %d 个" % (slug, len(tags), len(bad)))
    for b in bad[:5]:
        print("   ", b)

print("\n=== 2) title/description 八语 + JSON-LD ===")
for slug in SLUGS:
    s = open("blog/" + slug, encoding="utf-8").read()
    t = re.search(r"<title[^>]*>", s).group(0)
    d = re.search(r'<meta name="description"[^>]*>', s, re.S).group(0)
    ld = re.search(r'<script type="application/ld\+json">(.*?)</script>', s, re.S).group(1)
    json.loads(ld)
    print("%s: title属性=%d desc属性=%d JSON-LD OK" % (
        slug, len(re.findall(r"data-[a-z]{2}=", t)), len(re.findall(r"data-[a-z]{2}=", d))))

print("\n=== 3) 各语言页：存在 / noindex / hreflang 条数 ===")
for slug in SLUGS:
    row = []
    for l in LANGS:
        p = "%s/blog/%s" % (l, slug)
        try:
            s = open(p, encoding="utf-8").read()
        except OSError:
            row.append("%s=MISSING" % l)
            continue
        ni = "noindex" in s.lower()
        alt = len(re.findall(r'rel="alternate" hreflang=', s))
        can = re.search(r'rel="canonical" href="([^"]+)"', s).group(1)
        row.append("%s: noindex=%s alt=%d" % (l, ni, alt))
    print(slug)
    for r in row:
        print("   ", r)

print("\n=== 4) 语言页语言纯净度（正文中文字符数，de/pt 应为 0，ja 例外看汉字） ===")
for slug in SLUGS:
    for l in ["en", "fr", "es", "de", "pt"]:
        s = open("%s/blog/%s" % (l, slug), encoding="utf-8").read()
        body = s[s.index('class="article-body"'):s.index("site-footer")]
        txt = re.sub(r"<[^>]+>", " ", body)
        print("%s %s: CJK字符 %d" % (l, slug[:28], len(CJK.findall(txt))))

print("\n=== 5) 卡片是否进入各语种 blog 列表 ===")
for l in ["", "en", "fr", "es", "ja", "ko", "de", "pt"]:
    p = ("%s/blog/index.html" % l) if l else "blog/index.html"
    s = open(p, encoding="utf-8").read()
    print(p, {slug[:20]: (slug in s) for slug in SLUGS})

print("\n=== 6) 死链抽查（新页内部链接） ===")
import os
for slug in SLUGS:
    s = open("blog/" + slug, encoding="utf-8").read()
    for h in re.findall(r'href="([^"]+)"', s):
        if h.startswith(("http", "mailto:", "tel:", "#")):
            continue
        t = h.split("?")[0].split("#")[0]
        p = os.path.normpath(os.path.join("blog", t))
        if not os.path.exists(p):
            print("  缺失:", h)
print("死链检查完成")
