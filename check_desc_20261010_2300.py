#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""仅体检：desc 长度 + 撞车检查（不写盘）。用法: F:/hermes/venvs/tools/Scripts/python.exe check_desc_20261010_2300.py"""
import os, sys
ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)
sys.path.insert(0, ROOT)
from daily_meta_20261010_2300 import ARTICLES

print("gen_i18n.py 存在:", os.path.exists("gen_i18n.py"), "| to_traditional.py 存在:", os.path.exists("to_traditional.py"))
print("骨架存在:", os.path.exists("blog/knitwear-sweater-trims-guide.html"))
sm = open("sitemap.xml", encoding="utf-8").read()
LANGS = ["en", "ja", "ko", "fr", "es"]
ok = True
for a in ARTICLES:
    print("-" * 70)
    print(a["slug"])
    for l in ("zh", "en", "ja", "ko", "fr", "es"):
        k = "desc_%s" % l
        n = len(a[k])
        flag = ""
        if l == "zh" and not (80 <= n <= 120):
            flag = "  <<< 中文应 80-120 字"
            ok = False
        if l == "en" and not (150 <= n <= 160):
            flag = "  <<< 英文应 150-160 字符"
            ok = False
        print("   %-8s %3d %s" % (l, n, flag))
    for k in ("title_zh", "title_en", "title_ja", "title_ko", "title_fr", "title_es"):
        print("   %-9s %s" % (k, a[k]))
    # 撞车
    hit = [p for p in ["blog/%s" % a["slug"]] + ["%s/blog/%s" % (l, a["slug"]) for l in LANGS] if os.path.exists(p)]
    in_sm = ("/blog/%s</loc>" % a["slug"]) in sm
    print("   文件撞车:", hit or "无", "| sitemap 撞车:", in_sm)
    if hit or in_sm:
        ok = False
    # 引号畸形
    for m in ("title_zh", "title_en", "title_ja", "title_ko", "title_fr", "title_es",
              "desc_zh", "desc_en", "desc_ja", "desc_ko", "desc_fr", "desc_es",
              "h1_zh", "h1_en", "h1_ja", "h1_ko", "h1_fr", "h1_es",
              "crumb_zh", "crumb_en", "crumb_ja", "crumb_ko", "crumb_fr", "crumb_es",
              "tag_zh", "tag_en", "tag_ja", "tag_ko", "tag_fr", "tag_es"):
        v = a[m]
        if '"' in v:
            print("   !! 属性含裸双引号:", m)
            ok = False
        if "&" in v and "&amp;" not in v and "&nbsp;" not in v:
            print("   !! 属性含裸 &:", m)
            ok = False
print("=" * 70)
print("体检结论:", "通过" if ok else "有问题，先修正")
sys.exit(0 if ok else 1)
