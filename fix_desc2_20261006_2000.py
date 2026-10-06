#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-06 晚间批次：en desc 长度微调（150-160 字符）——直接改写根页 data-en 与 en/ 页 content。"""
import re

FIX = {
    "trim-metal-salt-spray-guide.html":
        "Metal trim rust and salt-spray guide: where corrosion starts on buttons, snaps and sliders, plating choice by use, 24/48/96 hours and packaging.",
    "functional-garment-trims-label-guide.html":
        "Functional trims guide: what each label and bag does, the tests behind antibacterial and anti-mite claims, wicking and UV wording, brightener-free paper.",
}

for slug, en in FIX.items():
    print("%-46s new_en=%d" % (slug, len(en)))
    root = "blog/" + slug
    s = open(root, encoding="utf-8").read()

    def repl(m):
        return re.sub(r'(data-en=")[^"]*(")', lambda x: x.group(1) + en + x.group(2), m.group(0), count=1)
    s2, n = re.subn(r'<meta name="description".*?>', repl, s, count=1, flags=re.S)
    assert n == 1, "根页 meta 未找到: " + root
    open(root, "w", encoding="utf-8", newline="").write(s2)

    p = "en/blog/" + slug
    s = open(p, encoding="utf-8").read()
    s2, n = re.subn(r'(<meta name="description" content=")[^"]*(")',
                    lambda m: m.group(1) + en + m.group(2), s, count=1)
    assert n == 1, "en 页 meta 未找到: " + p
    open(p, "w", encoding="utf-8", newline="").write(s2)
print("完成")
