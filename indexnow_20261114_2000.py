#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-11-14 20:00 批次：IndexNow 提交本批 12 个文章 URL + 6 个博客列表页。"""
import json
import ssl
import urllib.request

KEY = "IMPLQzV8ZJL3XT7alCYPLLhxLidYNlkc"
SLUGS = ["trim-dry-cleaning-fastness-guide.html", "back-neck-tape-guide.html"]
PRE = ["blog", "en/blog", "fr/blog", "es/blog", "ja/blog", "ko/blog"]

urls = []
for s in SLUGS:
    for p in PRE:
        urls.append("https://taigetag.com/%s/%s" % (p, s))
for p in PRE:
    urls.append("https://taigetag.com/%s/index.html" % p)

payload = {"host": "taigetag.com", "key": KEY,
           "keyLocation": "https://taigetag.com/%s.txt" % KEY, "urlList": urls}
req = urllib.request.Request("https://api.indexnow.org/indexnow",
                             data=json.dumps(payload).encode("utf-8"),
                             headers={"Content-Type": "application/json; charset=utf-8"})
try:
    r = urllib.request.urlopen(req, timeout=60, context=ssl.create_default_context())
    print("IndexNow HTTP", r.status, "提交 URL:", len(urls))
except urllib.error.HTTPError as e:
    print("IndexNow HTTP", e.code, e.read()[:300])
for u in urls:
    print("  ", u)
