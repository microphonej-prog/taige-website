#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""IndexNow 手动提交本批次 12 个 URL，并打印 HTTP 状态。"""
import json, urllib.request

KEY = "IMPLQzV8ZJL3XT7alCYPLLhxLidYNlkc"
SLUGS = ["clothing-label-compliance-poland.html", "clothing-label-compliance-portugal.html"]
LANGS = ["en", "ja", "ko", "fr", "es"]
urls = []
for s in SLUGS:
    urls.append("https://taigetag.com/blog/%s" % s)
    urls += ["https://taigetag.com/%s/blog/%s" % (l, s) for l in LANGS]

payload = json.dumps({"host": "taigetag.com", "key": KEY,
                      "keyLocation": "https://taigetag.com/%s.txt" % KEY,
                      "urlList": urls}).encode()
req = urllib.request.Request("https://api.indexnow.org/indexnow", data=payload,
                             headers={"Content-Type": "application/json; charset=utf-8"})
try:
    with urllib.request.urlopen(req, timeout=60) as r:
        print("IndexNow HTTP %d  (%d URL)" % (r.status, len(urls)))
except urllib.error.HTTPError as e:
    print("IndexNow HTTP %d  (%d URL)  %s" % (e.code, len(urls), e.read()[:200]))
