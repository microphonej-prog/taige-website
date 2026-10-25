#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""校验 2026-10-25 20:00 批次：文件、六语 title/h1、canonical、卡片、sitemap、JSON-LD、语言纯度"""
import os, re, json, html
from html.parser import HTMLParser

LANGS = ["en", "ja", "ko", "fr", "es"]
SLUGS = {
    "sports-team-jersey-trims-guide.html": {
        "zh": "球衣與隊服輔料指南：號碼工藝、領標與洗水標怎麼選",
        "en": "Sports Jersey and Team Kit Trims: Numbers, Neck and Care Labels",
        "ja": "ユニフォーム・スポーツジャージの副資材：番号工程・ネーム・洗濯表示の選び方",
        "ko": "유니폼·스포츠 저지 부자재: 번호 공정·넥 라벨·케어 라벨 선택",
        "fr": "Accessoires de maillots et tenues d'équipe : numéros, étiquettes et entretien",
        "es": "Accesorios para camisetas y equipaciones: números, etiquetas y cuidado",
    },
    "garment-rental-label-guide.html": {
        "zh": "服裝租賃標籤方案：耐洗標識、可複用吊牌與追溯設計",
        "en": "Clothing Rental Labels: Durable Marking, Reusable Tags and Traceability",
        "ja": "衣料レンタルのラベル設計：耐洗表示・再利用タグ・トレーサビリティ",
        "ko": "의류 렌털 라벨 설계: 내세탁 표시·재사용 태그·추적성",
        "fr": "Étiquettes de location : marquage durable, étiquettes réutilisables, traçabilité",
        "es": "Etiquetas para alquiler de ropa: marcado duradero, colgantes reutilizables y trazabilidad",
    },
}
TODAY = "2026-10-25"

# h1 独立期望值（h1 与 title 允许措辞不同）
H1S = {
    ("sports-team-jersey-trims-guide.html", "en"): "Sports Jersey and Team Kit Trims: Numbers, Neck Labels and Care Labels",
    ("garment-rental-label-guide.html", "fr"): "Étiquettes de location : marquage durable, étiquettes réutilisables et traçabilité",
}


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
        exp_h1 = H1S.get((slug, lang), exp)
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

print("\n=== 4) 五语页语言纯度（en/fr/es 正文不得残留汉字）===")
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

print("\n=== 8) 版本与 JS 语法 ===")
mj = open("js/main.js", encoding="utf-8").read()
print(" ", re.search(r'var BUST_VERSION = "[^"]*";', mj).group(0))
for a in ["sports-team-jersey-trims-guide.html", "garment-rental-label-guide.html"]:
    s = open("blog/" + a, encoding="utf-8").read()
    print("  %-42s js引用: %s %s" % (a[:40], bool(re.search(r"main\.js\?v=\d+", s)), bool(re.search(r"assist\.js\?v=\d+", s))))

print("\n总判定:", "全部通过" if ok else "存在失败项")
