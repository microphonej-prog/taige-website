#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""手动补提交本批次 12 个新 URL 到 IndexNow，并校验密钥文件在线可访问。"""
import json, subprocess, os

os.chdir(os.path.dirname(os.path.abspath(__file__)))
KEY = "IMPLQzV8ZJL3XT7alCYPLLhxLidYNlkc"
SLUGS = ["pfas-restrictions-apparel-trims-guide.html", "eu-forced-labour-regulation-apparel-trims.html"]
urls = []
for s in SLUGS:
    urls.append("https://taigetag.com/blog/%s" % s)
    for l in ("en", "ja", "ko", "fr", "es"):
        urls.append("https://taigetag.com/%s/blog/%s" % (l, s))
payload = {"host": "taigetag.com", "key": KEY,
           "keyLocation": "https://taigetag.com/%s.txt" % KEY, "urlList": urls}
p = os.path.join(os.environ.get("TEMP", "."), "indexnow_20261011.json")
open(p, "w", encoding="utf-8").write(json.dumps(payload))
print("提交 %d 个 URL" % len(urls))
r = subprocess.run(["curl", "-s", "-m", "60", "--noproxy", "*", "-X", "POST",
                    "https://api.indexnow.org/indexnow",
                    "-H", "Content-Type: application/json; charset=utf-8",
                    "-d", "@%s" % p, "-o", "/dev/null", "-w", "IndexNow HTTP %{http_code}"],
                   capture_output=True, text=True)
print(r.stdout.strip())
k = subprocess.run(["curl", "-s", "-m", "30", "--noproxy", "*", "-o", "/dev/null",
                    "-w", "keyfile HTTP %{http_code}",
                    "https://taigetag.com/%s.txt" % KEY], capture_output=True, text=True)
print(k.stdout.strip())
