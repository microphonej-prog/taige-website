#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""手动 IndexNow 提交本次 2 篇新文章的 12 个 URL（六语），并先核对线上 sitemap 已含这些 URL"""
import json, re, ssl, urllib.request, urllib.error

KEY = "IMPLQzV8ZJL3XT7alCYPLLhxLidYNlkc"
SLUGS = ["trousers-pants-trims-guide.html", "tshirt-hoodie-trims-guide.html"]
LANGS = ["", "en", "ja", "ko", "fr", "es"]
ctx = ssl.create_default_context()

req = urllib.request.Request("https://taigetag.com/sitemap.xml?v=2", headers={"User-Agent": "Mozilla/5.0"})
sm = urllib.request.urlopen(req, timeout=45, context=ctx).read().decode("utf-8", "replace")
print("线上 sitemap 长度 %d 字符" % len(sm))

urls = []
for s in SLUGS:
    for l in LANGS:
        u = "https://taigetag.com/%sblog/%s" % (l + "/" if l else "", s)
        assert "<loc>%s</loc>" % u in sm, "线上 sitemap 缺少 %s" % u
        urls.append(u)
print("线上 sitemap 已含 %d 个新 URL" % len(urls))

payload = json.dumps({
    "host": "taigetag.com",
    "key": KEY,
    "keyLocation": "https://taigetag.com/%s.txt" % KEY,
    "urlList": urls,
}).encode("utf-8")

r2 = urllib.request.Request("https://api.indexnow.org/indexnow", data=payload,
                            headers={"Content-Type": "application/json; charset=utf-8"})
try:
    with urllib.request.urlopen(r2, timeout=30, context=ctx) as r:
        print("IndexNow HTTP", r.status, "(200/202 = 成功)")
except urllib.error.HTTPError as e:
    print("IndexNow HTTP", e.code, e.read()[:200])
