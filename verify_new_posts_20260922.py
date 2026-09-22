#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""校验 2026-09-22 上午新增的 2 篇六语文章：正文六语完整性、引号畸形、JSON-LD、
生成页残留与语言真实渲染、hreflang/canonical、静态 title/description、sitemap、
列表页卡片、BUST_VERSION。"""
import re, json, os, sys
from html.parser import HTMLParser

NEW = ["blog/clothing-label-compliance-russia.html", "blog/garment-trims-claims-liability-guide.html"]
LANGS = ["en", "ja", "ko", "fr", "es"]
DATE = "2026-09-22"
BUST = "99"
fails = []


class Collector(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.in_body = False
        self.tags = []

    def handle_starttag(self, tag, attrs):
        d = {k.lower(): (v or "") for k, v in attrs}
        if tag == "section" and d.get("class", "").startswith("article-body"):
            self.in_body = True
            return
        if self.in_body:
            self.tags.append((tag, d))

    def handle_endtag(self, tag):
        if self.in_body and tag == "section":
            self.in_body = False


print("== 1) 根文件：正文六语属性完整性 / 引号畸形 / JSON-LD / 静态 SEO 字段 ==")
total_missing = 0
for f in NEW:
    s = open(f, encoding="utf-8").read()
    p = Collector(); p.feed(s)
    dzh = [(t, a) for t, a in p.tags if "data-zh" in a]
    missing = [(t, need) for t, a in dzh for need in ("data-en", "data-ja", "data-ko", "data-fr", "data-es")
               if not a.get(need, "").strip()]
    total_missing += len(missing)
    q1 = len(re.findall(r'data-(?:zh|en|fr|es|ja|ko)=""', s))
    q2 = len(re.findall(r'data-(?:zh|en|fr|es|ja|ko)="[^"]*"[a-zA-Z]', s))
    am = len(re.findall(r'&(?!amp;|nbsp;|quot;|#|<)', s))
    lds = re.findall(r'<script type="application/ld\+json">(.*?)</script>', s, re.S)
    for x in lds:
        json.loads(x)
    tattr = re.search(r'<title[^>]*data-zh="([^"]*)"[^>]*>(.*?)</title>', s, re.S)
    dattr = re.search(r'<meta name="description" data-zh="([^"]*)"', s)
    dcont = re.search(r'<meta name="description".*?content="([^"]*)"', s, re.S)
    static_mismatch = []
    if tattr and tattr.group(1) != tattr.group(2):
        static_mismatch.append("title静态文本!=data-zh")
    if dattr and dcont and dattr.group(1) != dcont.group(1):
        static_mismatch.append("desc content!=data-zh")
    print("  %s" % f)
    print("    正文标签 %d，带 data-zh %d，缺 en/ja/ko/fr/es %d %s" % (len(p.tags), len(dzh), len(missing), missing[:6]))
    print("    引号畸形=%d 属性值后裸字符=%d 裸&=%d JSON-LD=%d 处" % (q1, q2, am, len(lds)))
    print("    静态字段: %s  <html lang>=%s" % (static_mismatch or "OK",
                                              re.search(r'<html lang="([^"]+)"', s).group(1)))
    if q1 or q2 or am or len(lds) != 1 or static_mismatch:
        fails.append("根文件异常 %s" % f)

print("== 2) 生成页（en/ja/ko/fr/es）残留 / 语言真实性 / 标题 / canonical ==")
for f in NEW:
    slug = os.path.basename(f)
    for lang in LANGS:
        path = os.path.join(lang, f)
        s = open(path, encoding="utf-8").read()
        m0 = re.search(r'<section class="article-body">', s)
        m1 = re.search(r'</section>', s[m0.end():])
        body = s[m0.end():m0.end() + m1.start()]
        body_ns = re.sub(r'<script.*?</script>', '', body, flags=re.S)
        cjk = len(re.findall(r'[\u4e00-\u9fff]', body_ns))
        kana = len(re.findall(r'[\u3040-\u30ff]', body_ns))
        hangul = len(re.findall(r'[\uac00-\ud7af]', body_ns))
        q = Collector(); q.feed(s)
        residue = sum(1 for t, a in q.tags if any(k.startswith("data-") and k[5:] in
                      ("zh", "en", "fr", "es", "ja", "ko") for k in a))
        title = re.search(r'<title>(.*?)</title>', s, re.S).group(1)
        desc = re.search(r'<meta name="description" content="([^"]*)"', s)
        can = re.search(r'<link rel="canonical" href="([^"]*)"', s).group(1)
        hl = len(re.findall(r'<link rel="alternate" hreflang="', s))
        ok = residue == 0 and can.endswith("/%s/blog/%s" % (lang, slug)) and hl == 7
        if lang in ("en", "fr", "es") and cjk:
            ok = False
        if lang in ("fr", "es", "en") and cjk == 0:
            pass
        if lang == "ja" and kana < 50:
            ok = False
        if lang == "ko" and hangul < 50:
            ok = False
        print("  %-42s residue=%d 汉字=%d 假名=%d 韩文=%d desc=%d hreflang=%d %s"
              % (lang + "/blog/" + slug, residue, cjk, kana, hangul,
                 len(desc.group(1)) if desc else -1, hl, "OK" if ok else "!! 异常"))
        print("         desc: %s" % (desc.group(1)[:100] if desc else "-"))
        if not ok:
            fails.append("生成页异常 %s" % path)

print("== 3) sitemap ==")
sm = open("sitemap.xml", encoding="utf-8").read()
for f in NEW:
    slug = os.path.basename(f)
    for pre in ["blog/"] + ["%s/blog/" % l for l in LANGS]:
        u = "https://taigetag.com/%s%s" % (pre, slug)
        if "<loc>%s</loc>" % u not in sm:
            fails.append("sitemap 缺 %s" % u)
    z = re.search(r'<loc>https://taigetag.com/blog/%s</loc>\r?\n\s*<lastmod>([^<]*)</lastmod>' % re.escape(slug), sm)
    print("  %-48s lastmod=%s" % (slug, z.group(1) if z else "缺失"))
    if not z or z.group(1) != DATE:
        fails.append("sitemap lastmod 异常 %s" % slug)
for p in ["blog/index.html"] + ["%s/blog/index.html" % l for l in LANGS]:
    z = re.search(r'<loc>https://taigetag.com/%s</loc>\r?\n\s*<lastmod>([^<]*)</lastmod>' % re.escape(p), sm)
    print("  %-48s lastmod=%s" % (p, z.group(1) if z else "缺失"))
    if not z or z.group(1) != DATE:
        fails.append("blog index lastmod 未更新 %s" % p)
print("  <loc> 总数=%d" % sm.count("<loc>"))

print("== 4) 列表页卡片 ==")
for p in ["blog/index.html"] + ["%s/blog/index.html" % l for l in LANGS]:
    s = open(p, encoding="utf-8").read()
    hit = [os.path.basename(f) for f in NEW if os.path.basename(f) in s]
    print("  %-26s 命中=%s" % (p, hit))
    if len(hit) != 2:
        fails.append("卡片缺失 %s" % p)

print("== 5) BUST_VERSION ==")
mj = open("js/main.js", encoding="utf-8").read()
nb = re.search(r'var BUST_VERSION = "(\d+)"', mj).group(1)
print("  BUST_VERSION=%s" % nb)
if nb != BUST:
    fails.append("BUST_VERSION 未升级")

print("\n缺失总数=%d 失败项=%d %s" % (total_missing, len(fails), fails))
sys.exit(1 if (total_missing or fails) else 0)
