# -*- coding: utf-8 -*-
"""诊断：找出 zh 根页中 <td>/<th> 元素默认文本与 data-zh 不一致的情况"""
import re, sys

for f in ["blog/apparel-relabeling-service-guide.html",
          "blog/secondhand-resale-apparel-label-guide.html",
          "en/blog/apparel-relabeling-service-guide.html"]:
    s = open(f, encoding="utf-8").read()
    print("=" * 70)
    print(f)
    n = 0
    for m in re.finditer(r'<t[dh]\b([^>]*?)>([^<]*)</t[dh]>', s, re.S):
        attrs, text = m.group(1), m.group(2)
        z = re.search(r'data-zh="([^"]*)"', attrs)
        if not z:
            continue
        n += 1
        if z.group(1) != text:
            print("   [不一致] data-zh=%s || 默认文本=%s" % (z.group(1)[:34], text[:34]))
    print("   带 data-zh 的 td/th 共 %d 个" % n)
