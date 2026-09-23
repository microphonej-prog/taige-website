#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""晚间批次：手动把 12 个新 URL 提交 IndexNow（验证 POST 返回码）"""
import json, subprocess, os, sys
sys.stdout.reconfigure(encoding='utf-8')
TMP = os.path.join(os.environ["LOCALAPPDATA"], "Temp")
slugs = ["sock-hosiery-trims-guide.html", "hat-scarf-gloves-trims-guide.html"]
urls = ["https://taigetag.com/blog/%s" % s for s in slugs] + \
       ["https://taigetag.com/%s/blog/%s" % (l, s) for l in ["en", "ja", "ko", "fr", "es"] for s in slugs]
payload = {"host": "taigetag.com",
           "key": "IMPLQzV8ZJL3XT7alCYPLLhxLidYNlkc",
           "keyLocation": "https://taigetag.com/IMPLQzV8ZJL3XT7alCYPLLhxLidYNlkc.txt",
           "urlList": urls}
p = os.path.join(TMP, "indexnow_evening.json")
open(p, "w", encoding="utf-8").write(json.dumps(payload))
r = subprocess.run(["curl", "-s", "--noproxy", "*",
                    "-o", os.path.join(TMP, "indexnow_evening_resp.txt"),
                    "-w", "IndexNow POST HTTP %{http_code}", "-X", "POST",
                    "https://api.indexnow.org/indexnow",
                    "-H", "Content-Type: application/json; charset=utf-8",
                    "-d", "@" + p], capture_output=True, text=True, timeout=120)
print(r.stdout.strip(), "| urls =", len(urls))
resp = open(os.path.join(TMP, "indexnow_evening_resp.txt"), encoding="utf-8", errors="replace").read().strip()
print("响应体:", resp[:200] if resp else "(空)")
