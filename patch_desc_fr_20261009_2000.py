#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""fr 页面 desc 为 HTML 转义形式（&#x27;），单独按转义串替换"""
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

f = "fr/blog/plus-size-womenswear-trims-guide.html"
OLD = ("Guide des accessoires grande taille : étiquettes de taille jusqu&#x27;au 5XL, ceinture et couture "
       "latérale renforcées, entretien des tissus extensibles, mesures sur l&#x27;étiquette suspendue et emballages plus grands.")
NEW = ("Guide des accessoires grande taille : étiquettes jusqu&#x27;au 5XL, ceinture et couture latérale "
       "renforcées, entretien des tissus extensibles et emballages plus grands.")

s = open(f, encoding="utf-8").read()
assert s.count(OLD) == 1, "未命中 fr desc（%d 次）" % s.count(OLD)
s = s.replace(OLD, NEW)
open(f, "w", encoding="utf-8", newline="").write(s)
print("fr desc 已更新 -> %d 字符（转义后）" % len(NEW))

# 复核四个新 desc 在六语页面中的落点
import re
SLUG = "plus-size-womenswear-trims-guide.html"
for p in ["blog/%s" % SLUG] + ["%s/blog/%s" % (l, SLUG) for l in ("en", "ja", "ko", "fr", "es")]:
    s = open(p, encoding="utf-8").read()
    m = re.search(r'<meta name="description"[^>]*content="([^"]*)"', s, re.S)
    print("%-52s content=%d 字符" % (p, len(m.group(1))))
