#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""生成页内链与 canonical/hreflang 复核（六语）。"""
import os, re

ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)
SLUGS = ["pfas-restrictions-apparel-trims-guide.html", "eu-forced-labour-regulation-apparel-trims.html"]
fails = 0
for slug in SLUGS:
    for pre in ("", "en/", "ja/", "ko/", "fr/", "es/"):
        p = "%sblog/%s" % (pre, slug)
        s = open(p, encoding="utf-8").read()
        base = os.path.dirname(p)
        bad = []
        for href in sorted(set(re.findall(r'<a href="([^"#?]+)"', s))):
            if href.startswith(("http", "mailto", "tel")):
                continue
            if not os.path.exists(os.path.join(base, href)):
                bad.append(href)
        can = re.search(r'<link rel="canonical" href="([^"]*)"', s).group(1)
        exp_can = "https://taigetag.com/%sblog/%s" % (pre, slug)
        ok_can = can == exp_can
        if bad or not ok_can:
            fails += 1
        print("%-58s 内链死链=%d %s canonical=%s %s"
              % (p, len(bad), bad[:3], can, "OK" if ok_can else "!! 期望 %s" % exp_can))
        # 抽查列表页链接
    for pre in ("", "en/", "ja/", "ko/", "fr/", "es/"):
        p = "%sblog/index.html" % pre
        s = open(p, encoding="utf-8").read()
        grid = s.index('<div class="post-grid">')
        links = re.findall(r'<a class="more" href="([^"]*)"', s[grid:grid + 20000])
        miss = [h for h in links[:20] if not os.path.exists(os.path.join(pre + "blog", h))]
        print("  %-30s 前20张卡片缺文件: %d %s" % (p, len(miss), miss))
        fails += len(miss)
print("\n失败项 = %d" % fails)
raise SystemExit(1 if fails else 0)
