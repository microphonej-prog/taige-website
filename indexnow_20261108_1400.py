# -*- coding: utf-8 -*-
"""手动向 IndexNow 提交本次新增的 16 个 URL（幂等，返回 200/202 即成功）。"""
import json, sys, io, urllib.request
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

KEY = "IMPLQzV8ZJL3XT7alCYPLLhxLidYNlkc"
SLUGS = ["care-label-symbols-chart.html", "eyelet-grommet-rivet-guide.html"]
LANGS = ["", "en/", "fr/", "es/", "ja/", "ko/", "de/", "pt/"]
urls = ["https://taigetag.com/%sblog/%s" % (l, s) for s in SLUGS for l in LANGS]
payload = {"host": "taigetag.com", "key": KEY,
           "keyLocation": "https://taigetag.com/%s.txt" % KEY, "urlList": urls}
req = urllib.request.Request(
    "https://api.indexnow.org/indexnow",
    data=json.dumps(payload).encode("utf-8"),
    headers={"Content-Type": "application/json; charset=utf-8"})
try:
    with urllib.request.urlopen(req, timeout=30) as r:
        print("IndexNow HTTP", r.status, "| URLs:", len(urls))
except urllib.error.HTTPError as e:
    print("IndexNow HTTP", e.code, e.read()[:200])
