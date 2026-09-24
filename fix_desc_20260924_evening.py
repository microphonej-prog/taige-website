#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""缩短 desc_en 至 160 字符内（UAE 篇）"""
old = "UAE and Gulf clothing label compliance: why Arabic is mandatory, the information a garment needs, Arabic layout limits on woven labels, care symbols and import checks."
new = "UAE and Gulf clothing label compliance: why Arabic is mandatory, what a garment must carry, Arabic limits on woven labels, care symbols and import checks."
print("new desc_en len:", len(new))
files = ["blog/clothing-label-compliance-uae.html"] + \
        ["%s/blog/clothing-label-compliance-uae.html" % l for l in ("en", "ja", "ko", "fr", "es")] + \
        ["blog/index.html"] + ["%s/blog/index.html" % l for l in ("en", "ja", "ko", "fr", "es")]
tot = 0
for f in files:
    s = open(f, encoding="utf-8").read()
    if old in s:
        n = s.count(old)
        s = s.replace(old, new)
        open(f, "w", encoding="utf-8", newline="").write(s)
        tot += n
        print("  %-56s x%d" % (f, n))
print("替换总数:", tot)
