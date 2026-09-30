#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""IndexNow 手动补提交：2026-09-30 晚上批次 12 个新 URL（无头 Chrome 已验证线上可访问）。
返回 200/202 视为成功。"""
import json, urllib.request

KEY = "IMPLQzV8ZJL3XT7alCYPLLhxLidYNlkc"
SLUGS = ["garment-bag-header-card-guide.html", "poly-bag-suffocation-warning-guide.html"]
LANGS = ["en", "ja", "ko", "fr", "es"]
urls = []
for s in SLUGS:
    urls.append("https://taigetag.com/blog/%s" % s)
    urls += ["https://taigetag.com/%s/blog/%s" % (l, s) for l in LANGS]
urls += ["https://taigetag.com/blog/index.html"] + \
        ["https://taigetag.com/%s/blog/index.html" % l for l in LANGS]

payload = json.dumps({
    "host": "taigetag.com",
    "key": KEY,
    "keyLocation": "https://taigetag.com/%s.txt" % KEY,
    "urlList": urls,
}).encode("utf-8")

req = urllib.request.Request("https://api.indexnow.org/indexnow", data=payload,
                             headers={"Content-Type": "application/json; charset=utf-8"})
try:
    with urllib.request.urlopen(req, timeout=60) as r:
        print("IndexNow HTTP %d，提交 %d 个 URL（200/202 为成功）" % (r.status, len(urls)))
except urllib.error.HTTPError as e:
    print("IndexNow HTTP %d：%s" % (e.code, e.read()[:200]))
for u in urls:
    print("  " + u)
