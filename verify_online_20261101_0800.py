#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""线上校验：两篇新文章六语 title/正文渲染、sitemap 新 URL、上一批次坏链修复"""
import re, ssl, urllib.request

SLUGS = ["ecommerce-mailer-box-guide", "packaging-tape-guide"]
LANGS = ["zh", "en", "fr", "es", "ja", "ko"]
V = "190"
ctx = ssl.create_default_context()
UA = {"User-Agent": "Mozilla/5.0"}


def get(url):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=45, context=ctx) as r:
        return r.read().decode("utf-8", "replace"), r.status


ok = True
for slug in SLUGS:
    for lang in LANGS:
        path = ("%s/blog/%s.html" % (lang, slug)) if lang != "zh" else ("blog/%s.html" % slug)
        url = "https://taigetag.com/%s?lang=%s&v=%s" % (path, lang, V)
        raw, st = get(url)
        t = re.search(r"<title[^>]*>(.*?)</title>", raw, re.S)
        h1 = re.search(r"<h1[^>]*>(.*?)</h1>", raw, re.S)
        print("%-3s %-34s HTTP=%d title=%s" % (lang, slug[:32], st, t.group(1)[:70] if t else "无"))
        print("      h1: %s" % (re.sub(r"<[^>]+>", "", h1.group(1))[:70] if h1 else "无"))
        if not t:
            ok = False

print("== sitemap 线上 ==")
raw, st = get("https://taigetag.com/sitemap.xml?v=%s" % V)
print("HTTP", st, "loc 总数", raw.count("<loc>"))
for slug in SLUGS:
    for lang in ["", "en/", "fr/", "es/", "ja/", "ko/"]:
        u = "https://taigetag.com/%sblog/%s.html" % (lang, slug)
        hit = u in raw
        print("  %-58s %s" % (u, "OK" if hit else "缺失"))
        if not hit:
            ok = False

print("== 上一批次坏链修复（线上） ==")
raw, st = get("https://taigetag.com/blog/trademark-symbols-garment-labels.html?v=%s" % V)
print("HTTP", st, "含 href=\"blog/index.html\":", 'href="blog/index.html"' in raw,
      " 含 href=\"index.html\":", 'href="index.html"' in raw)
if 'href="blog/index.html"' in raw:
    ok = False

print("结果:", "通过" if ok else "有问题")
