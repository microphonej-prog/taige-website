#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""手动 IndexNow 提交本批 12 个新 URL（补 GH Actions 日志不可见的确认）"""
import json, urllib.request, urllib.error

KEY = "IMPLQzV8ZJL3XT7alCYPLLhxLidYNlkc"
SLUGS = ["saree-ethnic-wear-trims-guide.html", "garment-trims-trade-show-sourcing-guide.html"]
urls = []
for s in SLUGS:
    urls.append("https://taigetag.com/blog/%s" % s)
    for l in ("en", "ja", "ko", "fr", "es"):
        urls.append("https://taigetag.com/%s/blog/%s" % (l, s))

payload = json.dumps({
    "host": "taigetag.com",
    "key": KEY,
    "keyLocation": "https://taigetag.com/%s.txt" % KEY,
    "urlList": urls,
}).encode("utf-8")

req = urllib.request.Request("https://api.indexnow.org/indexnow", data=payload,
                             headers={"Content-Type": "application/json; charset=utf-8"},
                             method="POST")
try:
    r = urllib.request.urlopen(req, timeout=60)
    print("IndexNow HTTP %s（%d 个 URL）" % (r.getcode(), len(urls)))
    print(r.read().decode("utf-8", "replace")[:200])
except urllib.error.HTTPError as e:
    print("IndexNow HTTP %s" % e.code)
    print(e.read().decode("utf-8", "replace")[:300])
print("提交清单：")
for u in urls:
    print("  " + u)
