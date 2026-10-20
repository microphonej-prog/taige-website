#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""手动提交本次 12 个新 URL 到 IndexNow，打印真实 HTTP 状态"""
import json, urllib.request, sys
sys.path.insert(0, ".")
from daily_meta_20261020_1400 import ARTICLES

KEY = "IMPLQzV8ZJL3XT7alCYPLLhxLidYNlkc"
urls = []
for a in ARTICLES:
    urls.append("https://taigetag.com/blog/" + a["slug"])
    for l in ["en", "ja", "ko", "fr", "es"]:
        urls.append("https://taigetag.com/%s/blog/%s" % (l, a["slug"]))

payload = {"host": "taigetag.com", "key": KEY,
           "keyLocation": "https://taigetag.com/%s.txt" % KEY,
           "urlList": urls}
data = json.dumps(payload).encode("utf-8")
req = urllib.request.Request("https://api.indexnow.org/indexnow", data=data,
                             headers={"Content-Type": "application/json; charset=utf-8"})
try:
    with urllib.request.urlopen(req, timeout=60) as r:
        print("IndexNow HTTP %d  (提交 %d 个 URL)" % (r.status, len(urls)))
except urllib.error.HTTPError as e:
    print("IndexNow HTTP %d  (提交 %d 个 URL) body=%s" % (e.code, len(urls), e.read()[:200]))
    sys.exit(1)
