#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-02 晚批次：手动向 IndexNow 补提交 12 个新 URL（Bing/Yandex/Seznam）"""
import json, subprocess

KEY = "IMPLQzV8ZJL3XT7alCYPLLhxLidYNlkc"
SLUGS = ["elastic-trims-selection-guide.html", "garment-buttons-fasteners-guide.html"]
PRE = ["blog/", "en/blog/", "ja/blog/", "ko/blog/", "fr/blog/", "es/blog/"]
urls = ["https://taigetag.com/%s%s" % (p, s) for s in SLUGS for p in PRE]

payload = {
    "host": "taigetag.com",
    "key": KEY,
    "keyLocation": "https://taigetag.com/%s.txt" % KEY,
    "urlList": urls,
}
tmp = r"C:\Users\micro\taige-website\_indexnow_20261002_2000.json"
with open(tmp, "w", encoding="utf-8") as f:
    json.dump(payload, f, ensure_ascii=False)
print("提交 %d 个 URL" % len(urls))

r = subprocess.run(["curl", "-s", "--noproxy", "*", "-m", "60", "-X", "POST",
                    "https://api.indexnow.org/indexnow",
                    "-H", "Content-Type: application/json; charset=utf-8",
                    "-d", "@" + tmp, "-o", "-", "-w", "\nIndexNow HTTP %{http_code}\n"],
                   capture_output=True, text=True)
print(r.stdout.strip())
print(r.stderr.strip()[:300])
