#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-22 20:00 批次：手动 IndexNow 提交本批 12 个新 URL（Bing/Yandex/Seznam）"""
import json, urllib.request
from daily_meta_20261022_2000 import ARTICLES

KEY = "IMPLQzV8ZJL3XT7alCYPLLhxLidYNlkc"
LANGS = ["en", "ja", "ko", "fr", "es"]
urls = []
for a in ARTICLES:
    urls.append("https://taigetag.com/blog/" + a["slug"])
    urls += ["https://taigetag.com/%s/blog/%s" % (l, a["slug"]) for l in LANGS]

payload = {
    "host": "taigetag.com",
    "key": KEY,
    "keyLocation": "https://taigetag.com/%s.txt" % KEY,
    "urlList": urls,
}
req = urllib.request.Request(
    "https://api.indexnow.org/indexnow",
    data=json.dumps(payload).encode("utf-8"),
    headers={"Content-Type": "application/json; charset=utf-8"},
    method="POST",
)
print("提交 %d 个 URL" % len(urls))
for u in urls:
    print("  " + u)
try:
    with urllib.request.urlopen(req, timeout=60) as r:
        print("IndexNow HTTP %d %s" % (r.status, r.reason))
        print("响应体:", r.read().decode("utf-8", "replace")[:300] or "(空)")
except urllib.error.HTTPError as e:
    print("IndexNow HTTP %d %s" % (e.code, e.reason))
    print("响应体:", e.read().decode("utf-8", "replace")[:300])
except Exception as e:
    print("提交异常:", repr(e))
