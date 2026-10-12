#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""手动 IndexNow 提交本次 2 篇新文章的 12 个 URL（六语），确认线上 sitemap 已含这些 URL"""
import json, re, urllib.request

KEY = "IMPLQzV8ZJL3XT7alCYPLLhxLidYNlkc"
SLUGS = ["hang-tag-folding-types.html", "retail-floor-ready-apparel-packaging.html"]
LANGS = ["", "en", "ja", "ko", "fr", "es"]

sm = open("F:/hermes/cache/scratch/sitemap_live.xml", encoding="utf-8").read()
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

req = urllib.request.Request("https://api.indexnow.org/indexnow", data=payload,
                             headers={"Content-Type": "application/json; charset=utf-8"})
try:
    with urllib.request.urlopen(req, timeout=30) as r:
        print("IndexNow HTTP", r.status, "(200/202 = 成功)")
except urllib.error.HTTPError as e:
    print("IndexNow HTTP", e.code, e.read()[:200])
