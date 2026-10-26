#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""手动 IndexNow 提交本次 12 个新 URL（兜底，验证返回码）"""
import json, urllib.request

KEY = "IMPLQzV8ZJL3XT7alCYPLLhxLidYNlkc"
SLUGS = ["garment-packaging-cleanliness-contamination-control.html", "garment-packaging-budget-allocation.html"]
urls = []
for s in SLUGS:
    urls.append("https://taigetag.com/blog/%s" % s)
    for l in ["en", "ja", "ko", "fr", "es"]:
        urls.append("https://taigetag.com/%s/blog/%s" % (l, s))

body = json.dumps({
    "host": "taigetag.com",
    "key": KEY,
    "keyLocation": "https://taigetag.com/%s.txt" % KEY,
    "urlList": urls,
}).encode("utf-8")

req = urllib.request.Request("https://api.indexnow.org/indexnow", data=body,
                             headers={"Content-Type": "application/json; charset=utf-8"})
try:
    with urllib.request.urlopen(req, timeout=40) as r:
        print("IndexNow HTTP", r.status, "URLs:", len(urls))
        print(r.read(300).decode("utf-8", "replace"))
except urllib.error.HTTPError as e:
    print("IndexNow HTTP", e.code, e.read(300).decode("utf-8", "replace"))
