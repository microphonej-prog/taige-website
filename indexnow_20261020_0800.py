#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-20 08:00 批次：手动 IndexNow 提交本批 12 个新 URL，打印 HTTP 状态"""
import json, sys, urllib.request, urllib.error

KEY = "IMPLQzV8ZJL3XT7alCYPLLhxLidYNlkc"
SLUGS = ["vendor-labeling-manual-compliance.html", "garment-trims-repeat-order-consistency.html"]
urls = []
for s in SLUGS:
    urls.append("https://taigetag.com/blog/%s" % s)
    for l in ("en", "ja", "ko", "fr", "es"):
        urls.append("https://taigetag.com/%s/blog/%s" % (l, s))
urls += ["https://taigetag.com/blog/index.html"] + [
    "https://taigetag.com/%s/blog/index.html" % l for l in ("en", "ja", "ko", "fr", "es")]

payload = json.dumps({"host": "taigetag.com", "key": KEY,
                      "keyLocation": "https://taigetag.com/%s.txt" % KEY,
                      "urlList": urls}).encode("utf-8")
req = urllib.request.Request("https://api.indexnow.org/indexnow", data=payload, method="POST",
                             headers={"Content-Type": "application/json; charset=utf-8"})
try:
    r = urllib.request.urlopen(req, timeout=60)
    code, body = r.getcode(), r.read().decode("utf-8", "replace")
except urllib.error.HTTPError as e:
    code, body = e.code, e.read().decode("utf-8", "replace")
print("提交 URL 数 =", len(urls))
print("IndexNow HTTP =", code, "body=", body[:200])
for u in [urls[0], urls[6], "https://taigetag.com/%s.txt" % KEY]:
    try:
        c = urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0"}), timeout=45).getcode()
    except urllib.error.HTTPError as e:
        c = e.code
    print("  %-70s HTTP %s" % (u, c))
sys.exit(0 if code in (200, 202) else 1)
