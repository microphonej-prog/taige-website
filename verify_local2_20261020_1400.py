#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-20 14:00 批次本地全量校验（六语，v2：修正实体转义/页脚误报/繁体期望）"""
import re, os, json, sys, html
sys.path.insert(0, ".")
from daily_meta_20261020_1400 import ARTICLES

try:
    from opencc import OpenCC
    CC = OpenCC("s2t")
except Exception:
    CC = None

LANGS = ["en", "ja", "ko", "fr", "es"]
LANGS_ALL = ["zh"] + LANGS
fail = []


def path_for(slug, lang):
    return "blog/" + slug if lang == "zh" else "%s/blog/%s" % (lang, slug)


def trad(s):
    return CC.convert(s) if CC else s


for a in ARTICLES:
    slug = a["slug"]
    print("\n===== %s =====" % slug)
    for lang in LANGS_ALL:
        p = path_for(slug, lang)
        if not os.path.exists(p):
            fail.append("缺文件 " + p)
            continue
        s = open(p, encoding="utf-8").read()
        key = "title_zh" if lang == "zh" else "title_" + lang
        dkey = "desc_zh" if lang == "zh" else "desc_" + lang
        exp_t = trad(a[key]) if lang == "zh" else a[key]
        exp_d = trad(a[dkey]) if lang == "zh" else a[dkey]

        m = re.search(r"<title[^>]*>(.*?)</title>", s, re.S)
        got_t = html.unescape(m.group(1).strip()) if m else ""
        ok_t = exp_t == got_t

        m = re.search(r'<meta name="description"[^>]*content="([^"]*)"', s, re.S)
        got_d = html.unescape(m.group(1).strip()) if m else ""
        ok_d = got_d == exp_d

        jl = re.findall(r'<script type="application/ld\+json">(.*?)</script>', s, re.S)
        ok_j = True
        try:
            for j in jl:
                json.loads(j)
        except Exception as e:
            ok_j = False
            fail.append("%s JSON-LD 解析失败: %s" % (p, e))

        # 正文中文残留：只截取 <section class="article-body"> ... </section>
        cjk = 0
        if lang in ("en", "fr", "es"):
            i0 = s.index('class="article-body"')
            i1 = s.index("</section>", i0)
            body = re.sub(r"<[^>]+>", " ", s[i0:i1])
            cjk = len(re.findall(r"[\u4e00-\u9fff]", body))

        if not ok_t:
            fail.append("%s title 不符 -> %s" % (p, got_t[:60]))
        if not ok_d:
            fail.append("%s desc 不符 -> %s" % (p, got_d[:60]))
        if cjk:
            fail.append("%s 正文残留中文 %d 字" % (p, cjk))
        if not ok_j:
            fail.append("%s JSON-LD 非法" % p)

        print("  %-4s %s title=%s desc=%s(%d) jsonld=%d 正文CJK=%d"
              % (lang, "OK " if (ok_t and ok_d and ok_j and cjk == 0) else "FAIL",
                 "○" if ok_t else "×", "○" if ok_d else "×", len(got_d), len(jl), cjk))

    s = open(path_for(slug, "zh"), encoding="utf-8").read()
    can = re.search(r'<link rel="canonical" href="([^"]+)"', s).group(1)
    exp_can = "https://taigetag.com/blog/" + slug
    hl = re.findall(r'hreflang="([a-zA-Z\-]+)" href="([^"]+)"', s)
    print("  canonical=%s hreflang=%d %s" % (can, len(hl), [h[0] for h in hl]))
    if can != exp_can:
        fail.append("%s canonical=%s" % (slug, can))
    if len(hl) != 7:
        fail.append("%s hreflang 数量 %d" % (slug, len(hl)))

    miss_card = []
    for lang in LANGS_ALL:
        ip = "blog/index.html" if lang == "zh" else "%s/blog/index.html" % lang
        if slug not in open(ip, encoding="utf-8").read():
            miss_card.append(ip)
    print("  列表页卡片: %d/6" % (6 - len(miss_card)))
    for ip in miss_card:
        fail.append("%s 缺卡片 %s" % (ip, slug))

sm = open("sitemap.xml", encoding="utf-8").read()
for a in ARTICLES:
    for u in ["https://taigetag.com/blog/" + a["slug"]] + \
             ["https://taigetag.com/%s/blog/%s" % (l, a["slug"]) for l in LANGS]:
        if "<loc>%s</loc>" % u not in sm:
            fail.append("sitemap 缺 " + u)
print("\nsitemap <loc> 总数: %d" % sm.count("<loc>"))
for l in LANGS_ALL:
    u = "https://taigetag.com/blog/index.html" if l == "zh" else "https://taigetag.com/%s/blog/index.html" % l
    m = re.search(r"<loc>%s</loc>\s*<lastmod>([^<]*)</lastmod>" % re.escape(u), sm)
    print("  blog index lastmod[%s] = %s" % (l, m.group(1) if m else "缺失"))
    if not m or m.group(1) != "2026-10-20":
        fail.append("blog index lastmod 未更新: " + u)

print("\nBUST_VERSION: %s" % re.search(r'var BUST_VERSION = "([0-9]+)"', open("js/main.js", encoding="utf-8").read()).group(1))

print("\n===== 结果 =====")
if fail:
    print("失败 %d 项：" % len(fail))
    for f in fail:
        print("  - " + f)
    sys.exit(1)
print("全部通过")
