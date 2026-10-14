#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-14 下午批次：IndexNow 复核（提交 12 个新 URL + 校验密钥文件可达）"""
import json, ssl, urllib.request, sys

KEY = "IMPLQzV8ZJL3XT7alCYPLLhxLidYNlkc"
SLUGS = ["garment-trims-storage-conditions-guide.html", "home-textile-label-packaging-guide.html"]
LANGS = ["en", "ja", "ko", "fr", "es"]
urls = []
for s in SLUGS:
    urls.append("https://taigetag.com/blog/%s" % s)
    for l in LANGS:
        urls.append("https://taigetag.com/%s/blog/%s" % (l, s))
urls += ["https://taigetag.com/blog/index.html"] + ["https://taigetag.com/%s/blog/index.html" % l for l in LANGS]
print("待提交 URL 数:", len(urls))

ctx = ssl.create_default_context()
try:
    with urllib.request.urlopen("https://taigetag.com/%s.txt" % KEY, timeout=60, context=ctx) as r:
        body = r.read().decode().strip()
        print("密钥文件 HTTP %s，内容匹配=%s" % (r.status, body == KEY))
except Exception as e:
    print("密钥文件读取失败:", e)

payload = json.dumps({"host": "taigetag.com", "key": KEY,
                      "keyLocation": "https://taigetag.com/%s.txt" % KEY,
                      "urlList": urls}).encode("utf-8")
req = urllib.request.Request("https://api.indexnow.org/indexnow", data=payload,
                             headers={"Content-Type": "application/json; charset=utf-8"})
try:
    with urllib.request.urlopen(req, timeout=90, context=ctx) as r:
        print("IndexNow HTTP", r.status, "(200/202 = 成功)")
except urllib.error.HTTPError as e:
    print("IndexNow HTTP", e.code, e.read()[:200])
except Exception as e:
    print("IndexNow 请求异常:", e)
