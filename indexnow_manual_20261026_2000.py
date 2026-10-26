#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""IndexNow 手动提交本批次 12 个 URL"""
import json, urllib.request

KEY = "IMPLQzV8ZJL3XT7alCYPLLhxLidYNlkc"
SLUGS = ["apparel-trims-antibacterial-hygiene-packaging.html",
         "apparel-trims-static-dust-control.html"]
LANGS = ["", "en/", "ja/", "ko/", "fr/", "es/"]
urls = []
for s in SLUGS:
    for l in LANGS:
        urls.append("https://taigetag.com/%sblog/%s" % (l, s))

payload = {"host": "taigetag.com", "key": KEY,
           "keyLocation": "https://taigetag.com/%s.txt" % KEY, "urlList": urls}
req = urllib.request.Request("https://api.indexnow.org/indexnow",
                             data=json.dumps(payload).encode("utf-8"),
                             headers={"Content-Type": "application/json; charset=utf-8"},
                             method="POST")
try:
    r = urllib.request.urlopen(req, timeout=60)
    print("IndexNow HTTP %d %s，提交 %d 个 URL" % (r.status, r.reason, len(urls)))
except urllib.error.HTTPError as e:
    print("IndexNow HTTP %d %s" % (e.code, e.reason))
    print(e.read()[:300])
for u in urls:
    print("  ", u)
