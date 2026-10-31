#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re, urllib.request, ssl
ctx = ssl.create_default_context()
for url in ["https://taigetag.com/en/blog/medical-ppe-garment-labeling-guide.html?lang=en&v=1",
            "https://taigetag.com/en/blog/trim-supplier-switchover-guide.html?lang=en&v=1"]:
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    raw = urllib.request.urlopen(req, timeout=40, context=ctx).read().decode("utf-8", "replace")
    print(url, len(raw), "含在線發送:", "在線發送" in raw, "含在线发送:", "在线发送" in raw)
    for m in re.finditer(r"在[線线]發送|在[線线]发送", raw):
        print("   ctx:", repr(raw[max(0, m.start() - 120):m.end() + 60]))
