#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-01 下午批次：desc_en 微调（≤160 字符）+ 六语生成页 desc 同步"""
import re

FIX = {
    "garment-trims-carton-loading-guide.html": (
        "Cartons, pallets and container loading for garment trims: board grade, pallet sizes, stacking limits, 20GP/40GP/40HQ estimates and moisture protection.",
    ),
}

for slug, (new_en,) in FIX.items():
    print("%s new desc_en = %d 字符" % (slug, len(new_en)))
    # 根目录页：替换 description 里的 data-en
    root = "blog/%s" % slug
    s = open(root, encoding="utf-8").read()
    m = re.search(r'(<meta name="description" data-zh="[^"]*"\s*\n\s*data-en=")([^"]*)(")', s)
    assert m, "根页 desc data-en 未找到"
    old_en = m.group(2)
    s = s.replace(old_en, new_en, 1)
    open(root, "w", encoding="utf-8", newline="").write(s)
    print("  根页已替换（旧 %d 字符）" % len(old_en))
    # en 生成页：content="旧英文"
    en = "en/blog/%s" % slug
    e = open(en, encoding="utf-8").read()
    assert old_en in e, "en 页未找到旧 desc"
    e = e.replace(old_en, new_en, 1)
    open(en, "w", encoding="utf-8", newline="").write(e)
    print("  en 页已替换")

# 复核所有语言页 desc 长度
for slug in ["trim-vmi-consignment-stock-guide.html", "garment-trims-carton-loading-guide.html"]:
    print("== %s" % slug)
    for pre in ("blog/", "en/blog/", "ja/blog/", "ko/blog/", "fr/blog/", "es/blog/"):
        s = open("%s%s" % (pre, slug), encoding="utf-8").read()
        d = re.search(r'<meta name="description" content="([^"]*)"', s)
        t = re.search(r'<title>(.*?)</title>', s, re.S)
        print("   %-12s desc=%3d  title=%s" % (pre, len(d.group(1)), t.group(1)[:58]))
