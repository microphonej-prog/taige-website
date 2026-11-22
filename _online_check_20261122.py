# -*- coding: utf-8 -*-
"""线上校验：中文根页 title/description 与 blog 首页卡片。"""
import re
import urllib.request

def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read().decode("utf-8", "ignore")

for slug in ("button-size-ligne-buttonhole-guide.html", "embroidery-backing-stabilizer-guide.html"):
    s = get("https://taigetag.com/blog/%s?t=1" % slug)
    m = re.search(r"<title[^>]*>(.*?)</title>", s, re.S)
    d = re.search(r'<meta name="description"[^>]*content="([^"]*)"', s, re.S)
    print(slug)
    print("  TITLE:", m.group(1).strip()[:90])
    print("  DESC len:", len(d.group(1)), "| data-en 数:", s.count("data-en="))

idx = get("https://taigetag.com/blog/index.html?t=1")
print("blog/index.html 新卡计数:", idx.count("embroidery-backing-stabilizer-guide") + idx.count("button-size-ligne-buttonhole-guide"))
sm = get("https://taigetag.com/sitemap.xml?t=1")
print("线上 sitemap loc 数:", sm.count("<loc>"), "| 新 slug 计数:",
      sm.count("embroidery-backing-stabilizer-guide"), sm.count("button-size-ligne-buttonhole-guide"))
