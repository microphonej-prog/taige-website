#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""线上 meta description 复核（确认修正后的 desc 已生效，不含旧串）"""
import re, urllib.request, time

OLD_EN = "size labels up to 5XL, reinforced waistband"
NEW_EN = "size labels to 5XL, reinforced waistband"
TARGETS = [
    ("zh", "https://taigetag.com/blog/plus-size-womenswear-trims-guide.html"),
    ("en", "https://taigetag.com/en/blog/plus-size-womenswear-trims-guide.html"),
    ("fr", "https://taigetag.com/fr/blog/plus-size-womenswear-trims-guide.html"),
    ("es", "https://taigetag.com/es/blog/plus-size-womenswear-trims-guide.html"),
    ("en2", "https://taigetag.com/en/blog/garment-hanger-types-guide.html"),
]
for tag, u in TARGETS:
    url = "%s?nocache=%d" % (u, int(time.time()))
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    s = urllib.request.urlopen(req, timeout=60).read().decode("utf-8", "replace")
    m = re.search(r'<meta name="description"[^>]*content="([^"]*)"', s, re.S)
    d = m.group(1) if m else "NONE"
    print("%-4s %-3d字符 %s" % (tag, len(d), d[:120]))
    assert OLD_EN not in s, "旧 desc 仍在线: %s" % u
print("desc 复核通过（旧串已不在线上）")
