#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""向 IndexNow 单独提交本批次 12 个新 URL，确认搜索引擎接受（202 = 已接受，200 = OK）。
同时确认密钥文件在线可访问。"""
import json, ssl, sys, urllib.request

LANGS = ["en", "ja", "ko", "fr", "es"]
SLUGS = ["woven-label-density-guide.html", "garment-trims-development-calendar.html"]
KEY = "IMPLQzV8ZJL3XT7alCYPLLhxLidYNlkc"

urls = []
for s in SLUGS:
    urls.append("https://taigetag.com/blog/%s" % s)
    for l in LANGS:
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
    with urllib.request.urlopen(req, timeout=60) as r:
        print("IndexNow POST -> HTTP %d（200/202 = 已接受），提交 %d 个 URL" % (r.status, len(urls)))
except urllib.error.HTTPError as e:
    print("IndexNow POST -> HTTP %d %s（400=格式错误 403=密钥校验失败 422=URL 不属于该 host）" % (e.code, e.reason))

kreq = urllib.request.Request("https://taigetag.com/%s.txt" % KEY,
                              headers={"User-Agent": "Mozilla/5.0 TAGE-verify"})
try:
    with urllib.request.urlopen(kreq, timeout=60) as r:
        body = r.read().decode("utf-8", "replace").strip()
    print("密钥文件 HTTP %d，内容匹配=%s" % (r.status, body == KEY))
except urllib.error.HTTPError as e:
    print("密钥文件 HTTP %d %s" % (e.code, e.reason))

print("\n提交清单:")
for u in urls:
    print("  " + u)
