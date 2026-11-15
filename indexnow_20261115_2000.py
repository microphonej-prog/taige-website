# -*- coding: utf-8 -*-
"""对 2026-11-15 20:00 新增的 12 个 URL 主动提交 IndexNow，并预热 CDN。"""
import json
import subprocess
import urllib.error
import urllib.request

KEY = "IMPLQzV8ZJL3XT7alCYPLLhxLidYNlkc"
SLUGS = ["fringe-tassel-pom-pom-trims-guide", "cord-locks-toggles-drawstring-hardware-guide"]
PREF = ["blog/", "en/blog/", "fr/blog/", "es/blog/", "ja/blog/", "ko/blog/"]
urls = ["https://taigetag.com/%s%s.html" % (p, s) for s in SLUGS for p in PREF]

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
        print("IndexNow HTTP %d  (%d URLs)" % (r.status, len(urls)))
except urllib.error.HTTPError as e:
    print("IndexNow HTTP %d  body=%s" % (e.code, e.read()[:200]))

for u in urls + ["https://taigetag.com/sitemap.xml"]:
    p = subprocess.run(["curl", "-s", "-o", "C:/Users/micro/AppData/Local/Temp/warm.html",
                        "-w", "%{http_code}", u], capture_output=True, text=True)
    print("%s  %s" % (p.stdout.strip(), u))
