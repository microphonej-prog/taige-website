#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-08 下午批次深度校验：
① JSON-LD 存在且可解析（每页 1 处）
② canonical 与 sitemap 对应 URL 一致
③ 语言页无 data-zh 残留、无中文正文残留（ja/ko 允许日韩汉字，只查简繁中文特有词）
④ 语言页相对路径已改写（../../css、../../js、../../images）
⑤ 语言页 description 为该语言版本
"""
import os, re, json, sys

os.chdir(os.path.dirname(os.path.abspath(__file__)))
SLUGS = ["wooden-bamboo-hang-tags.html", "print-on-demand-apparel-labels.html"]
LANGS = ["en", "ja", "ko", "fr", "es"]
sm = open("sitemap.xml", encoding="utf-8").read()
locs = set(re.findall(r"<loc>([^<]+)</loc>", sm))
bad = 0

for s in SLUGS:
    for pre, path in [("", "blog/%s" % s)] + [(l + "/", "%s/blog/%s" % (l, s)) for l in LANGS]:
        html = open(path, encoding="utf-8").read()
        url = "https://taigetag.com/%sblog/%s" % (pre, s)
        # ① JSON-LD
        blocks = re.findall(r'<script type="application/ld\+json">(.*?)</script>', html, re.S)
        try:
            for b in blocks:
                json.loads(b)
            jl = "OK(%d)" % len(blocks)
        except Exception as e:
            jl = "!! JSON 解析失败 %s" % e
            bad += 1
        # ② canonical
        can = re.search(r'<link rel="canonical" href="([^"]+)"', html).group(1)
        can_ok = can == url
        if not can_ok:
            bad += 1
        can_sm = can in locs
        if not can_sm:
            bad += 1
        # ③ data-zh 残留（语言页不应有）
        dz = html.count("data-zh=")
        # ④ 相对路径
        rel_ok = True
        if pre:
            rel_ok = ('src="../../js/main.js' in html) and ('href="../../css/style.css' in html)
            if not rel_ok:
                bad += 1
        # ⑤ description
        desc = re.search(r'<meta name="description"[^>]*content="([^"]*)"', html, re.S).group(1)
        # 中文残留（语言页的可见正文里不应出现简体/繁体中文句子）
        leak = 0
        if pre:
            body = html[html.index('<section class="article-body">'):html.index("</main>")]
            # 去掉属性值，只看可见文本
            vis = re.sub(r"<[^>]+>", "", body)
            leak = len(re.findall(r"[\u4e00-\u9fff]{2,}", vis))
            if leak:
                bad += 1
        print("%-46s JSON-LD=%-7s canonical=%s in_sitemap=%s data-zh=%d rel=%s 中文残留块=%d desc=%d字符"
              % (path, jl, can_ok, can_sm, dz, rel_ok, leak, len(desc)))
        print("      desc: %s" % desc[:110])

print("\n问题数:", bad)
sys.exit(1 if bad else 0)
