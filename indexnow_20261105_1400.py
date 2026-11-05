#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""手动向 IndexNow 提交本批次 12 个新 URL，并打印 HTTP 状态"""
import json, ssl, urllib.request

KEY = "IMPLQzV8ZJL3XT7alCYPLLhxLidYNlkc"
SLUGS = ["nordic-apparel-labelling-compliance.html", "garment-trims-low-temperature-performance.html"]
LANGS = ["en", "ja", "ko", "fr", "es"]

urls = []
for s in SLUGS:
    urls.append("https://taigetag.com/blog/%s" % s)
    urls += ["https://taigetag.com/%s/blog/%s" % (l, s) for l in LANGS]

payload = json.dumps({
    "host": "taigetag.com",
    "key": KEY,
    "keyLocation": "https://taigetag.com/%s.txt" % KEY,
    "urlList": urls,
}).encode("utf-8")

req = urllib.request.Request(
    "https://api.indexnow.org/indexnow",
    data=payload,
    headers={"Content-Type": "application/json; charset=utf-8"},
    method="POST",
)
try:
    with urllib.request.urlopen(req, timeout=60) as r:
        print("IndexNow HTTP %d  (提交 %d 个 URL)" % (r.status, len(urls)))
except urllib.error.HTTPError as e:
    print("IndexNow HTTP %d  body=%s" % (e.code, e.read()[:300]))

for u in urls:
    print("  " + u)
