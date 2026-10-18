#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""手动向 IndexNow 提交本批次 12 个新 URL，并打印响应码。"""
import json, urllib.request, urllib.error

KEY = "IMPLQzV8ZJL3XT7alCYPLLhxLidYNlkc"
SLUGS = ["trim-inner-packing-spec.html", "adhesive-trim-shelf-life.html"]
LANGS = ["", "en/", "ja/", "ko/", "fr/", "es/"]
urls = []
for s in SLUGS:
    for pre in LANGS:
        urls.append("https://taigetag.com/%sblog/%s" % (pre, s))
urls += ["https://taigetag.com/%sblog/index.html" % pre for pre in LANGS]

body = json.dumps({
    "host": "taigetag.com",
    "key": KEY,
    "keyLocation": "https://taigetag.com/%s.txt" % KEY,
    "urlList": urls,
}).encode("utf-8")

req = urllib.request.Request("https://api.indexnow.org/indexnow", data=body,
                             headers={"Content-Type": "application/json; charset=utf-8"},
                             method="POST")
try:
    r = urllib.request.urlopen(req, timeout=60)
    code = r.getcode()
    print("IndexNow HTTP %s，提交 %d 个 URL" % (code, len(urls)))
except urllib.error.HTTPError as e:
    code = e.code
    print("IndexNow HTTP %s（%s），提交 %d 个 URL" % (code, e.reason, len(urls)))
print("成功判据：200 或 202")
for u in urls[:3]:
    print("  ", u)
