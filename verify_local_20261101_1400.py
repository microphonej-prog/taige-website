#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-11-01 14:00 批次本地校验：文件、六语属性、语言纯净度、卡片、sitemap、坏链、JSON-LD。"""
import os, re, json, sys

LANGS = ["en", "ja", "ko", "fr", "es"]
SLUGS = ["phthalate-free-apparel-packaging.html", "garment-packaging-for-returns.html"]
CJK = re.compile(r'[\u4e00-\u9fff]')
KANA = re.compile(r'[\u3040-\u30ff]')
HANGUL = re.compile(r'[\uac00-\ud7af]')
fails = []
# 站点公共元素（CSS 注释、语言按钮 title、微信字样、assist 控件）自带 40 个汉字，作为基线
_base = open("en/blog/packaging-tape-guide.html", encoding="utf-8").read()
BASE_CJK = len(CJK.findall(re.sub(r'<script.*?</script>', '', _base, flags=re.S)))
print("基线汉字数（上一批 en 文章）:", BASE_CJK)

for slug in SLUGS:
    print("\n===== %s =====" % slug)
    paths = ["blog/" + slug] + ["%s/blog/%s" % (l, slug) for l in LANGS]
    for p in paths:
        if not os.path.exists(p):
            fails.append("缺文件 " + p)
            continue
        s = open(p, encoding="utf-8").read()
        t = re.search(r'<title[^>]*>(.*?)</title>', s, re.S)
        left = len(re.findall(r'data-(?:zh|en|ja|ko|fr|es)=', s))
        cjk = len(CJK.findall(re.sub(r'<script.*?</script>', '', s, flags=re.S)))
        print("  %-42s %5.1fKB title=%s | 残留data属性=%d 汉字=%d"
              % (p, len(s.encode()) / 1024, (t.group(1)[:58] if t else "NONE"), left, cjk))
        if t is None:
            fails.append("无 title " + p)
        if left and not p.startswith("blog/") or (left and "/blog/" in p and not p.startswith("blog/")):
            fails.append("残留 data 属性 " + p)
        # JSON-LD
        ld = re.findall(r'<script type="application/ld\+json">(.*?)</script>', s, re.S)
        for j in ld:
            try:
                json.loads(j)
            except Exception as e:
                fails.append("JSON-LD 非法 %s: %s" % (p, e))
        # 语言纯净度
        if p.startswith(("en/", "fr/", "es/")):
            if cjk > BASE_CJK:
                fails.append("%s 含汉字 %d 个（基线 %d）" % (p, cjk, BASE_CJK))
        if p.startswith("ja/"):
            if not KANA.search(s):
                fails.append("%s 无假名" % p)
            if len(CJK.findall(s)) < 50:
                fails.append("%s 汉字过少（可能未翻译）" % p)
        if p.startswith("ko/"):
            if not HANGUL.search(s):
                fails.append("%s 无谚文" % p)
            han = len(CJK.findall(re.sub(r'<script.*?</script>', '', s, flags=re.S)))
            print("      ko 汉字残留=%d" % han)
            if han > BASE_CJK:
                fails.append("%s 含汉字 %d（基线 %d）" % (p, han, BASE_CJK))

    # 坏链（中文根目录文章内链）
    s = open("blog/" + slug, encoding="utf-8").read()
    for h in set(re.findall(r'href="([^"#:]+\.html)"', s)):
        target = os.path.normpath(os.path.join("blog", h))
        if not os.path.exists(target):
            fails.append("坏链 %s -> %s" % (slug, h))

# 卡片
idx = open("blog/index.html", encoding="utf-8").read()
for slug in SLUGS:
    n = idx.count('href="%s"' % slug)
    print("\n卡 href=%s 次数=%d" % (slug, n))
    if n != 1:
        fails.append("卡片数异常 %s=%d" % (slug, n))

# sitemap
sm = open("sitemap.xml", encoding="utf-8").read()
for slug in SLUGS:
    for u in ["https://taigetag.com/blog/%s" % slug] + ["https://taigetag.com/%s/blog/%s" % (l, slug) for l in LANGS]:
        if "<loc>%s</loc>" % u not in sm:
            fails.append("sitemap 缺 " + u)
print("\nsitemap 新 URL 检查完成；<loc> 总数 %d" % sm.count("<loc>"))
for l in ["blog", "en/blog", "ja/blog", "ko/blog", "fr/blog", "es/blog"]:
    m = re.search(r'<loc>https://taigetag.com/%s/index.html</loc>\s*<lastmod>([^<]*)</lastmod>' % l, sm)
    print("  %-9s lastmod=%s" % (l, m.group(1) if m else "MISSING"))

# 生成页六语属性数（zh 文件里应有 6 个属性/元素）
zh = open("blog/" + SLUGS[0], encoding="utf-8").read()
print("\nzh 文章 data-zh=%d data-en=%d data-ja=%d data-ko=%d data-fr=%d data-es=%d"
      % tuple(len(re.findall(r'data-%s="' % l, zh)) for l in ["zh", "en", "ja", "ko", "fr", "es"]))
mj = open("js/main.js", encoding="utf-8").read()
print("BUST_VERSION =", re.search(r'BUST_VERSION = "(\d+)"', mj).group(1))

print("\n失败项：%d" % len(fails))
for f in fails:
    print("  [X]", f)
sys.exit(1 if fails else 0)
