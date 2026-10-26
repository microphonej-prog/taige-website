#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-26 20:00 批次本地全量校验"""
import os, re, json, sys, html, importlib.util

ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)

SLUGS = ["apparel-trims-antibacterial-hygiene-packaging.html",
         "apparel-trims-static-dust-control.html"]
TITLES = {
 "apparel-trims-antibacterial-hygiene-packaging.html": {
   "en": "Antibacterial Trims and Hygiene Packaging: Claims That Hold Up | TAGE",
   "ja": "抗菌副資材と衛生包装ガイド：銀イオン・抗菌袋・表示の適法性 | TAGE",
   "ko": "항균 부자재와 위생 포장 가이드: 은이온·항균 비닐·표시 적법성 | TAGE",
   "fr": "Accessoires antibactériens et emballage hygiénique : allégations défendables | TAGE",
   "es": "Accesorios antibacterianos y embalaje higiénico: alegaciones defendibles | TAGE"},
 "apparel-trims-static-dust-control.html": {
   "en": "Static Control in Garment Packaging: Dark Garments and Bag Mouths | TAGE",
   "ja": "衣料品包装の静電気対策：濃色衣料の埃付着と袋口の密着 | TAGE",
   "ko": "의류 포장 정전기 대책: 어두운 의류 먼지와 비닐 입구 밀착 | TAGE",
   "fr": "Maîtrise de l'électricité statique : vêtements foncés et sachets | TAGE",
   "es": "Control de la estática en embalaje textil: prendas oscuras y bolsas | TAGE"},
}
LANGS = ["en", "ja", "ko", "fr", "es"]
fail = []


def path(lang, slug):
    return ("blog/%s" % slug) if lang == "zh" else ("%s/blog/%s" % (lang, slug))


def cjk_ratio_ok(txt, lang):
    # 只检查可见文本：en/fr/es/ko 不允许出现汉字（ja 允许，zh 本来就是汉字）
    if lang in ("ja", "zh"):
        return True, 0
    han = re.findall(r"[\u4e00-\u9fff]", txt)
    return len(han) == 0, len(han)


for slug in SLUGS:
    for lang in ["zh"] + LANGS:
        p = path(lang, slug)
        if not os.path.exists(p):
            fail.append("缺失文件 %s" % p)
            continue
        s = open(p, encoding="utf-8").read()
        m = re.search(r"<title[^>]*>(.*?)</title>", s, re.S)
        title = m.group(1).strip() if m else ""
        if lang == "zh":
            if "TAGE" not in title:
                fail.append("%s 中文 title 异常: %s" % (p, title))
        else:
            if html.unescape(title) != TITLES[slug][lang]:
                fail.append("%s title 不符: %s" % (p, title))
        m = re.search(r'<meta name="description"[^>]*content="([^"]*)"', s)
        desc = m.group(1) if m else ""
        if len(desc) < 60:
            fail.append("%s description 过短(%d): %s" % (p, len(desc), desc[:60]))
        if 'data-zh=' in desc or 'content="data-' in s:
            fail.append("%s description 仍是占位" % p)
        canon = re.search(r'<link rel="canonical" href="([^"]*)"', s).group(1)
        want = ("https://taigetag.com/blog/%s" % slug) if lang == "zh" else \
               ("https://taigetag.com/%s/blog/%s" % (lang, slug))
        if canon != want:
            fail.append("%s canonical 不符: %s != %s" % (p, canon, want))
        if s.count('rel="alternate" hreflang') != 7:
            fail.append("%s hreflang 数量 %d != 7" % (p, s.count('rel="alternate" hreflang')))
        h1 = re.search(r"<h1[^>]*>(.*?)</h1>", s, re.S).group(1)
        if len(h1.strip()) < 8:
            fail.append("%s h1 异常: %s" % (p, h1))
        # JSON-LD
        for blk in re.findall(r'<script type="application/ld\+json">(.*?)</script>', s, re.S):
            try:
                json.loads(blk)
            except Exception as e:
                fail.append("%s JSON-LD 非法: %s" % (p, e))
        # 正文可见文本检查
        body = s[s.index('<section class="article-body">'):s.index("</main>")]
        vis = re.sub(r"<[^>]+>", " ", body)
        ok, n = cjk_ratio_ok(vis, lang)
        if not ok:
            fail.append("%s 可见文本含 %d 个汉字（语言污染）" % (p, n))
        # data-* 残留（生成页应已烘焙）
        if lang != "zh" and "data-zh=" in body:
            fail.append("%s 正文仍残留 data-zh" % p)
        # 内部链接存在性
        for h in re.findall(r'href="([a-z0-9\-]+\.html)"', body):
            if h in ("index.html",):
                continue
            if not os.path.exists("blog/%s" % h):
                fail.append("%s 内部链接指向不存在文件 blog/%s" % (p, h))
        print("ok %-60s title=%d desc=%d" % (p, len(title), len(desc)))

# 列表页卡片
for lang in ["zh"] + LANGS:
    p = "blog/index.html" if lang == "zh" else "%s/blog/index.html" % lang
    s = open(p, encoding="utf-8").read()
    for slug in SLUGS:
        if ('href="%s"' % slug) not in s:
            fail.append("%s 缺卡片链接 %s" % (p, slug))
    head = s[s.index('<div class="post-grid">'):s.index('<div class="post-grid">') + 9000]
    order = re.findall(r'class="more" href="([^"]+)"', head)
    if order[:2] != SLUGS:
        fail.append("%s 卡片不在 post-grid 顶部，实际顺序 %s" % (p, order[:3]))
    print("ok cards %s" % p)

# sitemap
sm = open("sitemap.xml", encoding="utf-8").read()
for slug in SLUGS:
    for u in ["https://taigetag.com/blog/%s" % slug] + \
             ["https://taigetag.com/%s/blog/%s" % (l, slug) for l in LANGS]:
        if "<loc>%s</loc>" % u not in sm:
            fail.append("sitemap 缺 %s" % u)
for u in ["https://taigetag.com/blog/index.html"] + \
         ["https://taigetag.com/%s/blog/index.html" % l for l in LANGS]:
    m = re.search(r"<loc>%s</loc>\r?\n\s*<lastmod>([^<]*)</lastmod>" % re.escape(u), sm)
    if not m or m.group(1) != "2026-10-26":
        fail.append("blog index lastmod 未更新 %s" % u)
print("sitemap <loc> 总数 %d" % sm.count("<loc>"))

# BUST_VERSION
mj = open("js/main.js", encoding="utf-8").read()
if 'var BUST_VERSION = "185";' not in mj:
    fail.append("BUST_VERSION 未升级到 185")

print()
if fail:
    print("!!! 失败 %d 项" % len(fail))
    for f in fail:
        print("  -", f)
    sys.exit(1)
print("全部通过")
