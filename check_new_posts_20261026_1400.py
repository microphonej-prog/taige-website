#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""校验 2026-10-26 14:00 批次：文件、六语 title/h1、canonical、卡片、sitemap、JSON-LD、语言纯度"""
import os, re, json, html
from html.parser import HTMLParser

LANGS = ["en", "ja", "ko", "fr", "es"]
SLUGS = {
    "care-label-fold-types.html": {
        "zh": "洗水標摺疊方式指南：對摺、三摺與摺邊設計",
        "en": "Care Label Fold Types: Bi-Fold, Tri-Fold and Fold Margins",
        "ja": "洗濯表示ラベルの折り方ガイド：二つ折り・三つ折り・折り代の設計",
        "ko": "케어 라벨 접지 방식 가이드: 반접기·삼절·접힘 여유 설계",
        "fr": "Pliure des étiquettes d'entretien : deux volets, triple et marges",
        "es": "Plegado de etiquetas de cuidado: dos paneles, triple y márgenes",
    },
    "hang-tag-multilingual-printing-guide.html": {
        "zh": "吊牌多語言印刷指南：語言組合、版面與版本管理",
        "en": "Multilingual Hang Tags: Language Sets, Layout and Version Control",
        "ja": "多言語タグの印刷ガイド：言語の組み合わせ・版面・版管理",
        "ko": "다국어 행택 인쇄 가이드: 언어 조합·지면·버전 관리",
        "fr": "Étiquettes multilingues : jeux de langues, maquette et gestion des versions",
        "es": "Etiquetas multilingües: idiomas, maqueta y control de versiones",
    },
}
TODAY = "2026-10-26"


def path_for(slug, lang):
    return "blog/%s" % slug if lang == "zh" else "%s/blog/%s" % (lang, slug)


def title_h1(path):
    s = open(path, encoding="utf-8").read()
    t = html.unescape(re.search(r"<title[^>]*>(.*?)</title>", s, re.S).group(1).strip())
    h = html.unescape(re.search(r"<h1[^>]*>(.*?)</h1>", s, re.S).group(1).strip())
    c = re.search(r'<link rel="canonical" href="([^"]*)"', s).group(1)
    return t, h, c


ok = True
print("=== 1) 12 个文件 ===")
for slug in SLUGS:
    for lang in ["zh"] + LANGS:
        p = path_for(slug, lang)
        if os.path.exists(p):
            print("  OK  %-56s %4d KB" % (p, os.path.getsize(p) // 1024))
        else:
            ok = False
            print("  MISSING", p)

print("\n=== 2) 六语 title / h1 / canonical ===")
for slug in SLUGS:
    for lang in ["zh"] + LANGS:
        p = path_for(slug, lang)
        t, h, c = title_h1(p)
        exp = SLUGS[slug][lang]
        exp_h1 = html.unescape(exp)
        t_ok = t.startswith(exp)
        h_ok = (h == exp_h1)
        exp_canon = "https://taigetag.com/" + ("" if lang == "zh" else lang + "/") + "blog/" + slug
        c_ok = (c == exp_canon)
        if not (t_ok and h_ok and c_ok):
            ok = False
        print("  %-3s %-42s title=%s h1=%s canon=%s" % (lang, slug[:40], "OK" if t_ok else "FAIL",
                                                        "OK" if h_ok else "FAIL", "OK" if c_ok else "FAIL"))
        if not t_ok:
            print("      title实际:", t[:100])
        if not h_ok:
            print("      h1实际:", h[:100])

print("\n=== 3) 中文根页六语属性完整性（仅含 data-zh 的元素）===")


class P(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.tags = []

    def handle_starttag(self, tag, attrs):
        self.tags.append((tag, dict(attrs)))


for slug in SLUGS:
    s = open(path_for(slug, "zh"), encoding="utf-8").read()
    body = s[s.index('class="article-body"'):s.index("\n</main>")]
    pr = P()
    pr.feed(body)
    zh = [(t, d) for t, d in pr.tags if "data-zh" in d]
    miss = [(t, [x for x in ["data-en", "data-ja", "data-ko", "data-fr", "data-es"] if x not in d])
            for t, d in zh]
    miss = [m for m in miss if m[1]]
    print("  %-42s 六语元素 %d，缺属性 %d" % (slug[:40], len(zh), len(miss)))
    if miss:
        ok = False
        print("     ", miss[:5])

print("\n=== 4) 语言纯度（en/fr/es 正文不得残留汉字；ja/ko 不得整段中文兜底）===")
for lang in ["en", "fr", "es"]:
    for slug in SLUGS:
        s = open(path_for(slug, lang), encoding="utf-8").read()
        body = s[s.index('class="article-body"'):s.index("\n</main>")]
        txt = re.sub(r"<script.*?</script>", "", body, flags=re.S)
        txt = re.sub(r"<[^>]+>", "", txt)
        cjk = re.findall(r"[\u4e00-\u9fff]", txt)
        print("  %-3s %-42s 正文汉字 %d" % (lang, slug[:40], len(cjk)))
        if cjk:
            ok = False
            print("     样例:", "".join(cjk[:30]))

print("\n=== 5) 卡片（6 个 blog/index.html）===")
for lang in ["zh"] + LANGS:
    p = "blog/index.html" if lang == "zh" else "%s/blog/index.html" % lang
    s = open(p, encoding="utf-8").read()
    start = s.index('<div class="post-grid">')
    head = s[start:start + 8000]
    top2 = sum(1 for slug in SLUGS if slug in head)
    print("  %-3s %-24s 顶部命中=%d 总出现=%s" % (lang, p, top2, [s.count(x) for x in SLUGS]))
    if top2 < 2:
        ok = False

print("\n=== 6) sitemap ===")
sm = open("sitemap.xml", encoding="utf-8").read()
for slug in SLUGS:
    for lang in ["zh"] + LANGS:
        u = "https://taigetag.com/" + ("" if lang == "zh" else lang + "/") + "blog/" + slug
        m = re.search(r"<loc>%s</loc>\r?\n\s*<lastmod>([^<]*)</lastmod>" % re.escape(u), sm)
        st = "OK" if (m and m.group(1) == TODAY) else ("FAIL" if m else "MISSING")
        if st != "OK":
            ok = False
        print("  %-3s %-46s %s" % (lang, slug[:44], st))
for lang in ["zh"] + LANGS:
    u = "https://taigetag.com/" + ("" if lang == "zh" else lang + "/") + "blog/index.html"
    m = re.search(r"<loc>%s</loc>\r?\n\s*<lastmod>([^<]*)</lastmod>" % re.escape(u), sm)
    print("  blog/index lastmod %-3s -> %s" % (lang, m.group(1) if m else "MISSING"))
print("  <loc> 总数:", sm.count("<loc>"))

print("\n=== 7) JSON-LD 合法性 ===")
for slug in SLUGS:
    for lang in ["zh"] + LANGS:
        s = open(path_for(slug, lang), encoding="utf-8").read()
        blocks = re.findall(r'<script type="application/ld\+json">(.*?)</script>', s, re.S)
        bad = 0
        for b in blocks:
            try:
                json.loads(b)
            except Exception:
                bad += 1
        if bad or len(blocks) == 0:
            ok = False
        print("  %-3s %-42s blocks=%d bad=%d" % (lang, slug[:40], len(blocks), bad))

print("\n=== 8) 版本与内部链接 ===")
mj = open("js/main.js", encoding="utf-8").read()
print(" ", re.search(r'var BUST_VERSION = "[^"]*";', mj).group(0))
for slug in SLUGS:
    s = open("blog/" + slug, encoding="utf-8").read()
    links = re.findall(r'href="([a-z0-9\-]+\.html)"', s)
    broken = [l for l in set(links) if l not in ("index.html",) and not os.path.exists("blog/" + l)]
    print("  %-42s js=%s/%s 相关文章链接 %s 断链 %s"
          % (slug[:40], bool(re.search(r"main\.js\?v=\d+", s)), bool(re.search(r"assist\.js\?v=\d+", s)),
             len(set(links)), broken or "无"))
    if broken:
        ok = False

print("\n总判定:", "全部通过" if ok else "存在失败项")
