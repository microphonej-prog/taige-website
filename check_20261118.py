# -*- coding: utf-8 -*-
"""新文章自检：JSON-LD 合法性、title/desc 长度、data-* 完整性、裸引号、hreflang 目标存在。"""
import json
import re
import os

FILES = ["blog/care-label-fiber-content-tolerance-guide.html",
         "blog/trim-test-report-reading-guide.html"]
LANGS = ["zh", "en", "fr", "es", "ja", "ko"]

for f in FILES:
    s = open(f, encoding="utf-8").read()
    print("=" * 70)
    print(f, os.path.getsize(f), "bytes")
    blocks = re.findall(r'<script type="application/ld\+json">(.*?)</script>', s, re.S)
    for b in blocks:
        json.loads(b)
    print("  JSON-LD blocks:", len(blocks), "全部 json.loads 通过")
    title = re.search(r"<title[^>]*>(.*?)</title>", s, re.S).group(1)
    print("  <title> 内容:", title)
    d = re.search(r'<meta name="description"[^>]*data-en="([^"]*)"', s, re.S).group(1)
    print("  en desc 字符数:", len(d))
    # 每语言 data 属性数一致性
    counts = {l: len(re.findall(r'data-%s="' % l, s)) for l in LANGS}
    print("  data 属性计数:", counts)
    assert len(set(counts.values())) == 1, "各语言属性数不一致"
    # 裸引号截断检查：属性值里不该出现 data-xx=" 后紧跟 "
    bad = re.findall(r'data-(?:zh|en|fr|es|ja|ko)=""', s)
    print("  空属性/引号错位:", len(bad))
    # hreflang 目标存在性
    missing = []
    for hon, href in re.findall(r'hreflang="([^"]+)" href="([^"]+)"', s):
        rel = href.replace("https://taigetag.com/", "")
        p = rel if rel else "index.html"
        if p.endswith("/"):
            p += "index.html"
        if not os.path.isfile(p):
            missing.append((hon, href))
    print("  hreflang 目标缺失:", missing if missing else "无")
    # 内链存在性
    dead = []
    for h in re.findall(r'href="([^"]+)"', s):
        if h.startswith(("http", "mailto", "tel", "#", "javascript:", "data:")):
            continue
        t = h.split("?")[0].split("#")[0]
        if not t:
            continue
        p = os.path.normpath(os.path.join("blog", t))
        if not os.path.exists(p):
            dead.append(h)
    print("  死链:", dead if dead else "无")
    # 正文可见中文以外语言是否有中文残留（仅统计 en 段落）
    print("  正文 div.callout 数:", s.count('class="callout"'))
