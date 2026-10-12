#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""修正两篇新文章的英文 description 长度到 150-160 字符（Google 显示长度）
同步更新：daily_meta 记录 / blog 根页 data-en / en/blog 页 meta content
"""
import os, re, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)

NEW = {
    "trousers-pants-trims-guide.html":
        "A trousers trims guide: waistband interlining and lining, belt loops, fly zippers and hooks, back-waist and size label positions, packing and a five-step check.",
    "tshirt-hoodie-trims-guide.html":
        "A T-shirt and hoodie trims guide: neck label options from satin woven to tagless, position tolerance, drawcord ends, size stickers, rib and a five-step check.",
}

sys.path.insert(0, ROOT)
import importlib.util
spec = importlib.util.spec_from_file_location("dm", os.path.join(ROOT, "daily_meta_20261012_1400.py"))
dm = importlib.util.module_from_spec(spec)
spec.loader.exec_module(dm)
OLD = {a["slug"]: a["desc_en"] for a in dm.ARTICLES}

for slug, new in NEW.items():
    old = OLD[slug]
    print("== %s  旧 %d 字符 -> 新 %d 字符" % (slug, len(old), len(new)))
    assert old != new
    # 1) 根目录页 data-en
    p = "blog/%s" % slug
    s = open(p, encoding="utf-8").read()
    assert 'data-en="%s"' % old in s, "根页未找到旧 desc_en"
    s = s.replace('data-en="%s"' % old, 'data-en="%s"' % new, 1)
    open(p, "w", encoding="utf-8", newline="").write(s)
    # 2) en/blog 页 meta content
    p2 = "en/blog/%s" % slug
    s2 = open(p2, encoding="utf-8").read()
    pat = r'(<meta name="description" content=")%s(">)' % re.escape(old)
    s2, n = re.subn(pat, r'\g<1>%s\g<2>' % new.replace("\\", "\\\\"), s2, count=1)
    assert n == 1, "en 页 meta 未替换"
    open(p2, "w", encoding="utf-8", newline="").write(s2)
    print("   已更新 blog/ 与 en/blog/")

# 3) 同步 meta 脚本记录
mp = "daily_meta_20261012_1400.py"
ms = open(mp, encoding="utf-8").read()
for slug, new in NEW.items():
    ms = ms.replace('desc_en="%s",' % OLD[slug], 'desc_en="%s",' % new, 1)
open(mp, "w", encoding="utf-8", newline="").write(ms)
print("daily_meta 记录已同步")
