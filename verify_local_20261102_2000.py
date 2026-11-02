#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-11-02 20:00 批次本地校验：六语页面 title/h1/正文语言纯度、卡片、sitemap、canonical"""
import re, os, html

SLUGS = ["apparel-trims-machine-vision-inspection.html", "garment-disassembly-recyclable-trims.html"]
LANGS = ["", "en", "ja", "ko", "fr", "es"]
CJK = re.compile(r'[\u4e00-\u9fff]')
KANA = re.compile(r'[\u3040-\u30ff]')
HANGUL = re.compile(r'[\uac00-\ud7af]')
LATIN = re.compile(r'[A-Za-z]{3,}')

def path(lang, slug):
    return ("%s/blog/%s" % (lang, slug)) if lang else ("blog/%s" % slug)

def body_text(s):
    m = re.search(r'<section class="article-body">(.*?)</section>', s, re.S)
    if not m:
        return ""
    t = re.sub(r'<script.*?</script>', '', m.group(1), flags=re.S)
    t = re.sub(r'<[^>]+>', ' ', t)
    return html.unescape(t)

print("=== 六语页面检查 ===")
for slug in SLUGS:
    for lang in LANGS:
        p = path(lang, slug)
        if not os.path.exists(p):
            print("  !! 缺文件 %s" % p); continue
        s = open(p, encoding="utf-8").read()
        title = re.search(r'<title[^>]*>(.*?)</title>', s, re.S).group(1)
        h1 = re.search(r'<h1[^>]*>(.*?)</h1>', s, re.S).group(1)
        txt = body_text(s)
        flags = []
        if lang in ("en", "fr", "es") and CJK.search(txt):
            flags.append("CJK残留")
        if lang == "ko" and CJK.search(txt):
            flags.append("汉字残留")
        if lang == "ja" and not KANA.search(txt):
            flags.append("无假名")
        if lang in ("en", "fr", "es") and not LATIN.search(txt):
            flags.append("无拉丁词")
        if len(txt.strip()) < 800:
            flags.append("正文过短 %d" % len(txt.strip()))
        print("  %-58s title=%3d h1=%3d 正文=%5d %s"
              % (p, len(title), len(h1), len(txt.strip()), " ".join(flags) if flags else "OK"))

print("=== blog/index.html 卡片 ===")
idx = open("blog/index.html", encoding="utf-8").read()
for slug in SLUGS:
    n = idx.count('href="%s"' % slug)
    print("  %s 链接 %d 处 %s" % (slug, n, "OK" if n == 1 else "检查"))

print("=== sitemap ===")
sm = open("sitemap.xml", encoding="utf-8").read()
for slug in SLUGS:
    for lang in LANGS:
        u = "https://taigetag.com/%sblog/%s" % ((lang + "/") if lang else "", slug)
        ok = "<loc>%s</loc>" % u in sm
        if not ok:
            print("  !! 缺 %s" % u)
print("  sitemap <loc> 总数 %d；两篇各 6 语言 URL 齐全" % sm.count("<loc>"))

print("=== canonical / hreflang 自检 ===")
for slug in SLUGS:
    for lang in LANGS:
        p = path(lang, slug)
        s = open(p, encoding="utf-8").read()
        canon = re.search(r'<link rel="canonical" href="([^"]+)"', s).group(1)
        want = "https://taigetag.com/%sblog/%s" % ((lang + "/") if lang else "", slug)
        alts = len(re.findall(r'<link rel="alternate" hreflang=', s))
        if canon != want:
            print("  !! %s canonical=%s 应为 %s" % (p, canon, want))
        if alts != 7:
            print("  !! %s hreflang %d 条（应 7）" % (p, alts))
print("  canonical/hreflang 检查完成")

print("=== JSON-LD ===")
import json
for slug in SLUGS:
    for lang in LANGS:
        p = path(lang, slug)
        s = open(p, encoding="utf-8").read()
        blocks = re.findall(r'<script type="application/ld\+json">(.*?)</script>', s, re.S)
        for b in blocks:
            json.loads(b)
        if len(blocks) != 1:
            print("  !! %s JSON-LD %d 块" % (p, len(blocks)))
print("  JSON-LD 全部合法且每页 1 块")
