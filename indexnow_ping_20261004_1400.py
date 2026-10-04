#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-04 下午批次：向 IndexNow 单独提交本批 12 个新 URL，打印 HTTP 码（202/200 = 成功）"""
import json, urllib.request

KEY = "IMPLQzV8ZJL3XT7alCYPLLhxLidYNlkc"
SLUGS = ["garment-drawcord-guide.html", "lace-trimming-guide.html"]
URLS = []
for s in SLUGS:
    URLS.append("https://taigetag.com/blog/%s" % s)
    for l in ("en", "ja", "ko", "fr", "es"):
        URLS.append("https://taigetag.com/%s/blog/%s" % (l, s))

payload = json.dumps({"host": "taigetag.com", "key": KEY,
                      "keyLocation": "https://taigetag.com/%s.txt" % KEY,
                      "urlList": URLS}).encode("utf-8")
req = urllib.request.Request("https://api.indexnow.org/indexnow", data=payload,
                             headers={"Content-Type": "application/json; charset=utf-8"})
try:
    with urllib.request.urlopen(req, timeout=60) as r:
        print("IndexNow HTTP %s (%d 个 URL)" % (r.status, len(URLS)))
except urllib.error.HTTPError as e:
    print("IndexNow HTTP %s -> %s (%d 个 URL)" % (e.code, e.reason, len(URLS)))
