#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-19 08:00 批次本地校验：六语文件 / 标题 / 正文语言纯度 / canonical / sitemap / 列表卡片 / JSON-LD"""
import os, re, json, sys, html as htmlmod

os.chdir(os.path.dirname(os.path.abspath(__file__)))

LANGS = ["en", "ja", "ko", "fr", "es"]
SLUGS = ["garment-trims-bom-consumption-guide.html", "apparel-trims-price-adjustment-guide.html"]
EXPECT_TITLE = {
    "zh": ["服裝輔料單耗覈算指南", "輔料報價爲什麼會變"],
    "en": ["Trim Consumption and BOM Costing", "Why Trim Prices Change"],
    "ja": ["衣料副資材の単耗計算ガイド", "副資材の価格が変わる理由"],
    "ko": ["의류 부자재 소요량 산출 가이드", "부자재 가격이 변하는 이유"],
    "fr": ["Consommation d'accessoires et calcul BOM", "Pourquoi le prix des accessoires change"],
    "es": ["Consumo de accesorios y cálculo BOM", "Por qué cambia el precio de los accesorios"],
}
fails = []


def read(p):
    return open(p, encoding="utf-8").read()


print("== 1) 六语文件存在性 ==")
for s in SLUGS:
    for lang in ["zh"] + LANGS:
        p = ("blog/%s" % s) if lang == "zh" else ("%s/blog/%s" % (lang, s))
        if not os.path.exists(p):
            fails.append("缺失文件 %s" % p)
        else:
            print("  ok %-58s %d KB" % (p, len(read(p).encode()) // 1024))

print("\n== 2) 静态 title / canonical 一致性 ==")
for lang in ["zh"] + LANGS:
    for i, s in enumerate(SLUGS):
        p = ("blog/%s" % s) if lang == "zh" else ("%s/blog/%s" % (lang, s))
        s_html = read(p)
        t = (re.search(r"<title[^>]*>(.*?)</title>", s_html, re.S) or [None, ""])[1].strip()
        t_cmp = htmlmod.unescape(t)
        can = (re.search(r'<link rel="canonical" href="([^"]+)"', s_html) or [None, ""])[1]
        want = "https://taigetag.com/%sblog/%s" % ("" if lang == "zh" else lang + "/", s)
        ok_t = EXPECT_TITLE[lang][i] in t_cmp
        ok_c = can == want
        print("  %-3s %-46s title_ok=%s canon_ok=%s" % (lang, s[:44], ok_t, ok_c))
        if not ok_t:
            fails.append("title 不符 %s %s -> %s" % (lang, s, t[:60]))
        if not ok_c:
            fails.append("canonical 不符 %s %s -> %s" % (lang, s, can))

print("\n== 3) 正文语言纯度（en/fr/es 无汉字；ja 含假名） ==")
for i, s in enumerate(SLUGS):
    for lang in LANGS:
        p = "%s/blog/%s" % (lang, s)
        html = read(p)
        body = re.search(r'<section class="article-body">(.*?)</section>', html, re.S)
        if not body:
            fails.append("正文缺失 %s" % p)
            continue
        txt = re.sub(r"<[^>]+>", " ", body.group(1))
        cjk = len(re.findall(r"[\u4e00-\u9fff]", txt))
        kana = len(re.findall(r"[\u3040-\u30ff]", txt))
        hangul = len(re.findall(r"[\uac00-\ud7af]", txt))
        attr_left = body.group(1).count("data-zh=")
        print("  %-3s %-46s cjk=%-4d kana=%-4d hangul=%-4d data_zh_left=%d" % (lang, s[:44], cjk, kana, hangul, attr_left))
        if lang in ("en", "fr", "es") and cjk:
            fails.append("正文残留汉字 %s %s cjk=%d" % (lang, s, cjk))
        if lang == "ja" and kana < 100:
            fails.append("日文假名过少 %s kana=%d" % (s, kana))
        if lang == "ko" and hangul < 100:
            fails.append("韩文谚文过少 %s hangul=%d" % (s, hangul))
        if attr_left:
            fails.append("语言页残留 data-zh 属性 %s %s" % (lang, s))

print("\n== 4) 中文页六语属性完整性（data-zh 元素是否都带另外五语） ==")
from html.parser import HTMLParser


class Six(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.n = 0
        self.bad = []

    def handle_starttag(self, t, a):
        d = dict(a)
        if "data-zh" in d:
            self.n += 1
            miss = [k for k in ("data-en", "data-fr", "data-es", "data-ja", "data-ko") if not d.get(k, "").strip()]
            if miss:
                self.bad.append((t, miss))


for s in SLUGS:
    html = read("blog/%s" % s)
    body = re.search(r'<section class="article-body">(.*?)</section>', html, re.S).group(1)
    p = Six()
    p.feed(body)
    print("  %-46s data-zh 元素=%-3d 缺语种=%d %s" % (s, p.n, len(p.bad), p.bad[:3]))
    if p.bad:
        fails.append("六语属性缺失 %s %s" % (s, p.bad[:3]))

print("\n== 5) sitemap ==")
sm = read("sitemap.xml")
for s in SLUGS:
    for pre in ("blog/", "en/blog/", "ja/blog/", "ko/blog/", "fr/blog/", "es/blog/"):
        u = "https://taigetag.com/%s%s" % (pre, s)
        pat = r"<loc>%s</loc>\s*<lastmod>([^<]*)</lastmod>" % re.escape(u)
        m = re.search(pat, sm)
        print("  %-58s %s" % (u, m.group(1) if m else "缺失"))
        if not m:
            fails.append("sitemap 缺 %s" % u)
        elif m.group(1) != "2026-10-19":
            fails.append("sitemap lastmod 错 %s -> %s" % (u, m.group(1)))
for pre in ("blog/", "en/blog/", "ja/blog/", "ko/blog/", "fr/blog/", "es/blog/"):
    u = "https://taigetag.com/%sindex.html" % pre
    m = re.search(r"<loc>%s</loc>\s*<lastmod>([^<]*)</lastmod>" % re.escape(u), sm)
    print("  index %-50s lastmod=%s" % (pre, m.group(1) if m else "缺失"))
    if not m or m.group(1) != "2026-10-19":
        fails.append("blog index lastmod 未更新 %s" % u)
print("  <loc> 总数 =", sm.count("<loc>"))

print("\n== 6) 列表页卡片（六语） ==")
for lang in ["zh"] + LANGS:
    p = "blog/index.html" if lang == "zh" else "%s/blog/index.html" % lang
    html = read(p)
    for s in SLUGS:
        n = html.count('href="%s"' % s)
        print("  %-3s %-46s 链接数=%d" % (lang, s[:44], n))
        if n != 1:
            fails.append("卡片链接数异常 %s %s -> %d" % (lang, s, n))

print("\n== 7) JSON-LD 合法性 ==")
for lang in ["zh"] + LANGS:
    for s in SLUGS:
        p = ("blog/%s" % s) if lang == "zh" else ("%s/blog/%s" % (lang, s))
        html = read(p)
        blocks = re.findall(r'<script type="application/ld\+json">(.*?)</script>', html, re.S)
        ok = 0
        for b in blocks:
            try:
                json.loads(b)
                ok += 1
            except Exception as e:
                fails.append("JSON-LD 解析失败 %s: %s" % (p, e))
        if ok != len(blocks) or not blocks:
            fails.append("JSON-LD 数量异常 %s blocks=%d ok=%d" % (p, len(blocks), ok))
print("  JSON-LD 检查完成（12 页）")

print("\n== 8) 引号/软连字符/URL 编码异常扫描 ==")
for lang in ["zh"] + LANGS:
    for s in SLUGS:
        p = ("blog/%s" % s) if lang == "zh" else ("%s/blog/%s" % (lang, s))
        html = read(p)
        bad = re.findall(r'data-(?:zh|en|ja|ko|fr|es)=""', html)
        if bad:
            fails.append("空属性畸形 %s %d" % (p, len(bad)))
        if "\u00ad" in html:
            fails.append("软连字符 %s" % p)
print("  扫描完成")

print("\n结论：失败项 %d" % len(fails))
for f in fails:
    print("  !!", f)
sys.exit(1 if fails else 0)
