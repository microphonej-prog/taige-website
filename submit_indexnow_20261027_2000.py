#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-27 20:00 批次：手动向 IndexNow 提交本批 12 个 URL，并打印 HTTP 码"""
import json, ssl, urllib.request

KEY = "IMPLQzV8ZJL3XT7alCYPLLhxLidYNlkc"
SLUGS = ["collab-capsule-collection-trims-guide.html", "offshore-sewing-trims-supply-guide.html"]
PRE = ["blog", "en/blog", "ja/blog", "ko/blog", "fr/blog", "es/blog"]

urls = []
for s in SLUGS:
    for p in PRE:
        urls.append("https://taigetag.com/%s/%s" % (p, s))

payload = {
    "host": "taigetag.com",
    "key": KEY,
    "keyLocation": "https://taigetag.com/%s.txt" % KEY,
    "urlList": urls,
}
ctx = ssl.create_default_context()
req = urllib.request.Request("https://api.indexnow.org/indexnow",
                             data=json.dumps(payload).encode("utf-8"),
                             headers={"Content-Type": "application/json; charset=utf-8"})
try:
    r = urllib.request.urlopen(req, timeout=60, context=ctx)
    print("IndexNow HTTP", r.status, "提交 URL:", len(urls))
except urllib.error.HTTPError as e:
    print("IndexNow HTTP", e.code, e.read()[:300])
for u in urls:
    print("  ", u)
