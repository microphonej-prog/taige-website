#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-09 晚间批次 IndexNow 主动提交（12 个新 URL）+ 校验密钥文件可访问。"""
import json, urllib.request, urllib.error, time

KEY = "IMPLQzV8ZJL3XT7alCYPLLhxLidYNlkc"
SLUGS = ["plus-size-womenswear-trims-guide.html", "garment-hanger-types-guide.html"]
urls = []
for s in SLUGS:
    urls.append("https://taigetag.com/blog/%s" % s)
    for pre in ("en", "ja", "ko", "fr", "es"):
        urls.append("https://taigetag.com/%s/blog/%s" % (pre, s))

print("== 0) 密钥文件 ==")
try:
    req = urllib.request.Request("https://taigetag.com/%s.txt?nocache=%d" % (KEY, int(time.time())),
                                 headers={"User-Agent": "Mozilla/5.0"})
    body = urllib.request.urlopen(req, timeout=60).read().decode("utf-8", "replace").strip()
    print("  keyLocation 内容匹配: %s (%d 字节)" % (body == KEY, len(body)))
except Exception as e:
    print("  ERR %s" % e)

print("== 1) IndexNow 提交 %d 个 URL ==" % len(urls))
payload = json.dumps({"host": "taigetag.com", "key": KEY,
                      "keyLocation": "https://taigetag.com/%s.txt" % KEY,
                      "urlList": urls}).encode("utf-8")
req = urllib.request.Request("https://api.indexnow.org/indexnow", data=payload,
                             headers={"Content-Type": "application/json; charset=utf-8",
                                      "User-Agent": "Mozilla/5.0"})
try:
    r = urllib.request.urlopen(req, timeout=90)
    print("  IndexNow HTTP %d" % r.status)
except urllib.error.HTTPError as e:
    print("  IndexNow HTTP %d (200/202 = 成功)" % e.code)
print("  已提交: %s" % ", ".join(u.split("taigetag.com")[1] for u in urls))
