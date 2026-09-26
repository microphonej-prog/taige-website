#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-09-26 晚间批次：对新文章 12 个 URL 单独提交 IndexNow，并打印 HTTP 状态码。"""
import json, urllib.request

KEY = "IMPLQzV8ZJL3XT7alCYPLLhxLidYNlkc"
SLUGS = ["trim-tooling-ownership-guide.html", "trim-limit-sample-inspection-guide.html"]
LANGS = ["en", "ja", "ko", "fr", "es"]

urls = []
for s in SLUGS:
    urls.append("https://taigetag.com/blog/%s" % s)
    for l in LANGS:
        urls.append("https://taigetag.com/%s/blog/%s" % (l, s))

payload = {"host": "taigetag.com", "key": KEY,
           "keyLocation": "https://taigetag.com/%s.txt" % KEY,
           "urlList": urls}
req = urllib.request.Request(
    "https://api.indexnow.org/indexnow",
    data=json.dumps(payload).encode("utf-8"),
    headers={"Content-Type": "application/json; charset=utf-8"})
try:
    with urllib.request.urlopen(req, timeout=60) as r:
        print("IndexNow HTTP %d（202/200 = 成功），提交 %d 个 URL" % (r.status, len(urls)))
except urllib.error.HTTPError as e:
    print("IndexNow HTTP %d %s" % (e.code, e.read()[:200]))
