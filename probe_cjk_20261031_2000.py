#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re, urllib.request, ssl
ctx = ssl.create_default_context()
url = "https://taigetag.com/en/blog/medical-ppe-garment-labeling-guide.html?lang=en&v=1"
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
raw = urllib.request.urlopen(req, timeout=40, context=ctx).read().decode("utf-8", "replace")
print("bytes", len(raw))
for m in re.finditer(r"[\u4e00-\u9fff][\u4e00-\u9fff\s]{0,20}", raw):
    print("RUN:", repr(raw[max(0, m.start() - 70):m.end() + 40]))
