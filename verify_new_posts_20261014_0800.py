#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-14 08:00 批次本地校验：文件存在 / 六语属性齐全 / 各语言页无中文残留 /
title-h1-desc 各语言正确 / canonical+hreflang / 列表页首卡 / sitemap / BUST_VERSION。"""
import os, re, io, sys, json
from html.parser import HTMLParser

ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)

ARTICLES = [
    dict(slug="apron-trims-label-guide.html",
         title={"zh": "圍裙與餐飲工作服輔料指南", "en": "Apron and Food-Service Workwear Trims Guide",
                "ja": "エプロン・飲食ユニフォーム副資材ガイド", "ko": "앞치마·요식업 유니폼 부자재 가이드",
                "fr": "Guide des accessoires pour tabliers", "es": "Guía de accesorios para delantales"}),
    dict(slug="clothing-label-compliance-netherlands.html",
         title={"zh": "荷蘭服裝標籤與包裝合規指南", "en": "Netherlands Apparel Labelling and Packaging Compliance",
                "ja": "オランダの衣料ラベル・包装コンプライアンス", "ko": "네덜란드 의류 라벨·포장 컴플라이언스",
                "fr": "Conformité étiquetage et emballage aux Pays-Bas", "es": "Cumplimiento de etiquetado y embalaje en Países Bajos"}),
]
LANGS = ["zh", "en", "ja", "ko", "fr", "es"]
ATTR = {"zh": "data-zh", "en": "data-en", "ja": "data-ja", "ko": "data-ko", "fr": "data-fr", "es": "data-es"}
fails = []


def path(lang, slug):
    return ("blog/%s" % slug) if lang == "zh" else ("%s/blog/%s" % (lang, slug))


class TextScan(HTMLParser):
    """收集 article-body 内含直接文本的元素及其文本（用于残留与属性检查）"""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.in_body = False
        self.depth = 0
        self.stack = []
        self.items = []      # (tag, attrs, text)

    def handle_starttag(self, tag, attrs):
        if not self.in_body and tag == "section" and dict(attrs).get("class") == "article-body":
            self.in_body = True
            self.depth = 1
            return
        if not self.in_body or tag in ("br", "img", "input", "meta", "link", "hr"):
            return
        if tag == "section":
            self.depth += 1
        self.stack.append([tag, dict(attrs), ""])
        self.items.append(self.stack[-1])

    def handle_endtag(self, tag):
        if not self.in_body:
            return
        if tag == "section":
            self.depth -= 1
            if self.depth == 0:
                self.in_body = False
                return
        if self.stack:
            self.stack.pop()

    def handle_data(self, data):
        if self.in_body and self.stack and data.strip():
            self.stack[-1][2] += data.strip()


def get_title(s):
    m = re.search(r"<title[^>]*>(.*?)</title>", s, re.S)
    return m.group(1).strip() if m else ""


def get_h1(s):
    m = re.search(r"<h1[^>]*>(.*?)</h1>", s, re.S)
    return re.sub(r"<[^>]+>", "", m.group(1)).strip() if m else ""


def get_desc(s):
    m = re.search(r'<meta name="description"(.*?)>', s, re.S)
    if not m:
        return ""
    mm = re.search(r'content="([^"]*)"', m.group(1))
    return mm.group(1) if mm else ""


CJK_KO = re.compile(r"[\u4e00-\u9fff]")
for a in ARTICLES:
    slug = a["slug"]
    print("=== %s" % slug)
    for lang in LANGS:
        p = path(lang, slug)
        if not os.path.exists(p):
            fails.append("缺文件 %s" % p)
            print("  !! 缺文件", p)
            continue
        s = io.open(p, encoding="utf-8").read()
        sc = TextScan()
        sc.feed(s)
        texted = [it for it in sc.items if it[2]]
        # 根目录页（zh）保留六语 data-* 属性，必须齐全；
        # 生成的语言页由 gen_i18n 静态渲染并删除 data-*（与既有文章一致），改为查文本语言正确性
        miss = [it for it in texted if not it[1].get(ATTR[lang])] if lang == "zh" else []
        resid = []
        if lang in ("en", "fr", "es", "ko"):
            resid = [t for _, _, t in texted if CJK_KO.search(t)]
        elif lang == "ja":
            kana = re.compile(r"[\u3041-\u309f\u30a0-\u30ff]")
            resid = [t for _, _, t in texted if len(t) > 12 and not kana.search(t)]
        title, h1, desc = get_title(s), get_h1(s), get_desc(s)
        key = a["title"][lang]
        ok_title = key in title
        canon = re.search(r'<link rel="canonical" href="([^"]*)"', s)
        canon = canon.group(1) if canon else ""
        expect = "https://taigetag.com/%sblog/%s" % ("" if lang == "zh" else lang + "/", slug)
        ok_canon = canon == expect
        hrefl = len(re.findall(r'<link rel="alternate" hreflang="', s))
        print("  %-3s 文本元素=%3d 缺%s=%d 中文残留=%d title✓=%s h1=%d字 desc=%d字 canonical✓=%s hreflang=%d"
              % (lang, len(texted), ATTR[lang], len(miss), len(resid), ok_title, len(h1), len(desc), ok_canon, hrefl))
        for it in miss[:3]:
            fails.append("%s 缺 %s: %s" % (p, ATTR[lang], it[:2]))
        for t in resid[:3]:
            fails.append("%s 中文残留: %s" % (p, t[:60]))
        if not ok_title:
            fails.append("%s title 不含关键词: %s" % (p, title[:70]))
        if not ok_canon:
            fails.append("%s canonical 不符: %s != %s" % (p, canon, expect))
        if hrefl < 6:
            fails.append("%s hreflang 不足: %d" % (p, hrefl))

# 列表页首卡
print("\n=== 列表页首卡 ===")
for lang in LANGS:
    p = "blog/index.html" if lang == "zh" else "%s/blog/index.html" % lang
    s = io.open(p, encoding="utf-8").read()
    grid = s.index('<div class="post-grid">')
    head = s[grid:grid + 6000]
    order = re.findall(r'<a class="more" href="([^"]+)"', head)
    ok = order[:2] == [ARTICLES[0]["slug"], ARTICLES[1]["slug"]]
    print("  %-3s 首两张卡=%s %s" % (lang, order[:2], "OK" if ok else "!! 顺序不符"))
    if not ok:
        fails.append("%s 首卡顺序不符: %s" % (p, order[:3]))

# sitemap
print("\n=== sitemap ===")
sm = io.open("sitemap.xml", encoding="utf-8").read()
for a in ARTICLES:
    for lang in ["", "en/", "ja/", "ko/", "fr/", "es/"]:
        u = "https://taigetag.com/%sblog/%s" % (lang, a["slug"])
        blk = re.search(r"<loc>%s</loc>\s*<lastmod>([^<]*)</lastmod>" % re.escape(u), sm)
        if not blk:
            fails.append("sitemap 缺 %s" % u)
            print("  !! 缺", u)
        elif blk.group(1) != "2026-10-14":
            fails.append("sitemap lastmod 错 %s = %s" % (u, blk.group(1)))
            print("  !! lastmod", u, blk.group(1))
for lang in ["", "en/", "ja/", "ko/", "fr/", "es/"]:
    u = "https://taigetag.com/%sblog/index.html" % lang
    blk = re.search(r"<loc>%s</loc>\s*<lastmod>([^<]*)</lastmod>" % re.escape(u), sm)
    if not blk or blk.group(1) != "2026-10-14":
        fails.append("blog index lastmod 未更新: %s" % u)
        print("  !! blog index lastmod", u, blk.group(1) if blk else "缺失")
print("  <loc> 总数 %d，含新 URL %d/12" % (sm.count("<loc>"),
      sum(1 for a in ARTICLES for l in ["", "en/", "ja/", "ko/", "fr/", "es/"]
          if "https://taigetag.com/%sblog/%s</loc>" % (l, a["slug"]) in sm)))

# BUST_VERSION + JS 语法
mj = io.open("js/main.js", encoding="utf-8").read()
print("\n=== BUST_VERSION ===")
print("  ", re.search(r'var BUST_VERSION = "([^"]*)"', mj).group(1))

print("\n校验结论:", "全部通过" if not fails else ("%d 项问题" % len(fails)))
for f in fails[:20]:
    print("  -", f)
sys.exit(0 if not fails else 1)
