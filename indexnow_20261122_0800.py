# -*- coding: utf-8 -*-
"""IndexNow 提交 2026-11-22 08:00 新增的 12 个 URL。"""
import json
import urllib.request

KEY = "IMPLQzV8ZJL3XT7alCYPLLhxLidYNlkc"
SLUGS = ["embroidery-backing-stabilizer-guide.html", "button-size-ligne-buttonhole-guide.html"]
PRE = ["blog/", "en/blog/", "fr/blog/", "es/blog/", "ja/blog/", "ko/blog/"]
urls = ["https://taigetag.com/%s%s" % (p, s) for s in SLUGS for p in PRE]

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
try:
    with urllib.request.urlopen(req, timeout=45) as r:
        print("IndexNow HTTP", r.status, "| URLs", len(urls))
except urllib.error.HTTPError as e:
    print("IndexNow HTTP", e.code, e.read()[:300])
