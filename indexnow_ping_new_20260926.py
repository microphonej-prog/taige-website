#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""独立复核：向 IndexNow 提交本次新增的 12 个文章 URL + 6 个列表页，打印 HTTP 状态。"""
import json, urllib.request, ssl

KEY = "IMPLQzV8ZJL3XT7alCYPLLhxLidYNlkc"
SLUGS = ["trim-order-quantity-unit-conversion.html", "trim-ironing-heat-resistance-guide.html"]
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
                             headers={"Content-Type": "application/json; charset=utf-8",
                                      "User-Agent": "taige-verify/1.0"})
try:
    r = urllib.request.urlopen(req, timeout=45, context=ssl.create_default_context())
    print("IndexNow HTTP %s  (已提交 %d 个 URL；200/202 = 接受)" % (r.status, len(urls)))
except urllib.error.HTTPError as e:
    body = e.read().decode("utf-8", "replace")[:200]
    print("IndexNow HTTP %s  body=%s" % (e.code, body))
except Exception as e:
    print("IndexNow 提交异常：%s" % e)
