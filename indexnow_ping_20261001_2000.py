#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-01 晚上（20:00）批次：手动补提交 12 个新 URL 到 IndexNow（本地直连，绕过 TUN 代理）"""
import json, subprocess, sys

KEY = "IMPLQzV8ZJL3XT7alCYPLLhxLidYNlkc"
SLUGS = ["hang-tag-special-effects-guide.html", "rainwear-waterproof-garment-trims-guide.html"]
PRE = ["blog/", "en/blog/", "ja/blog/", "ko/blog/", "fr/blog/", "es/blog/"]
urls = ["https://taigetag.com/%s%s" % (p, s) for s in SLUGS for p in PRE]
print("提交 %d 个 URL" % len(urls))

payload = json.dumps({
    "host": "taigetag.com",
    "key": KEY,
    "keyLocation": "https://taigetag.com/%s.txt" % KEY,
    "urlList": urls,
})

tmp = r"C:\Users\micro\taige-website\_indexnow_20261001_2000.json"
open(tmp, "w", encoding="utf-8").write(payload)

r = subprocess.run(["curl", "-s", "--noproxy", "*", "-m", "60", "-X", "POST",
                    "https://api.indexnow.org/indexnow",
                    "-H", "Content-Type: application/json; charset=utf-8",
                    "-d", "@%s" % tmp,
                    "-o", r"C:\Users\micro\taige-website\_indexnow_resp.txt",
                    "-w", "IndexNow HTTP %{http_code}\n"], capture_output=True, text=True)
print(r.stdout.strip(), r.stderr.strip())
resp = open(r"C:\Users\micro\taige-website\_indexnow_resp.txt", encoding="utf-8", errors="replace").read().strip()
print("响应体: %r" % resp[:200])
sys.exit(0 if ("200" in r.stdout or "202" in r.stdout) else 1)
