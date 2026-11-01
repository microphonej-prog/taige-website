#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-11-01 08:00 批次每日更新生成脚本（六语：zh-Hant 根 / en / ja / ko / fr / es）
- 电商飞机盒（自锁底瓦楞纸箱）选型与定制（ecommerce-mailer-box-guide）
- 封箱胶带与印字胶带选型（packaging-tape-guide）

用法: F:/hermes/venvs/tools/Scripts/python.exe daily_gen_20261101_0800.py [--check]
"""
import os, re, sys, subprocess, importlib.util

ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)
PY = sys.executable

SKEL = "blog/knitwear-sweater-trims-guide.html"
DATE_ZH = "2026年11月1日"
DATE_EN = "November 1, 2026"
DATE_JA = "2026年11月1日更新"
DATE_KO = "2026년 11월 1일 업데이트"
DATE_FR = "1 novembre 2026"
DATE_ES = "1 de noviembre de 2026"
SITEMAP_DATE = "2026-11-01"
BUST_OLD, BUST_NEW = "189", "190"
LANGS = ["en", "ja", "ko", "fr", "es"]

ARTICLES = [
    dict(
        slug="ecommerce-mailer-box-guide.html",
        body="blog/_body_mailerbox.html",
        title_zh="电商飞机盒选型与定制指南：楞型、尺寸与印刷 | TAGE",
        title_en="E-commerce Mailer Boxes: Flute, Sizing and Printing Guide | TAGE",
        title_ja="EC用メーラーボックスの選び方：段・サイズ・印刷 | TAGE",
        title_ko="이커머스 메일러 박스 선택과 제작: 골, 치수, 인쇄 | TAGE",
        title_fr="Mailer box e-commerce : cannelure, dimensions et impression | TAGE",
        title_es="Mailer box para e-commerce: corrugado, medidas e impresión | TAGE",
        desc_zh="电商服装飞机盒选型指南：自锁底、插卡式与分格款三种结构怎么选，E 楞 B 楞 BC 楞的厚度与抗压差异，内尺寸余量与体积重算法，单色与四色裱瓦的适用场景，附白样、色样、跌落测试三步验收清单。来自东莞泰阁包装。",
        desc_en="E-commerce mailer box guide: auto-lock, tuck-top or compartmented structures, E, B and BC flute choice, size allowance, volumetric weight and sampling steps.",
        desc_ja="EC用メーラーボックスのガイド。自動底・差込式・仕切り付きの3構造、E段・B段・BC段の厚みと圧縮強度、内寸の余裕と容積重量の計算、単色と4色貼り合せの使い分け、白サンプル・色サンプル・落下試験の3段階検収を解説します。東莞泰閣包装。",
        desc_ko="이커머스 메일러 박스 가이드. 자동 바닥·턱 삽입·칸막이 세 구조, E골·B골·BC골 두께와 압축 강도, 내치수 여유와 부피 무게 계산, 단색과 4도 합지 활용, 백 샘플·색상 샘플·낙하 시험 3단계 검수를 정리했습니다. 둥관 TAGE 패키징.",
        desc_fr="Guide de la mailer box e-commerce : fond auto-bloquant, rabats à enfoncer ou cloisons, cannelures E, B et BC, marges de mesure, poids volumétrique et échantillons.",
        desc_es="Guía de la mailer box de e-commerce: fondo autoblocante, solapas o compartimentos, corrugados E, B y BC, márgenes de medida, peso volumétrico y muestras.",
        crumb_zh="飞机盒选型",
        crumb_en="Mailer Boxes",
        crumb_ja="メーラーボックス",
        crumb_ko="메일러 박스",
        crumb_fr="Mailer box",
        crumb_es="Mailer box",
        h1_zh="电商飞机盒选型与定制指南：楞型、尺寸与印刷",
        h1_en="E-commerce Mailer Boxes: Flute, Sizing and Printing",
        h1_ja="EC用メーラーボックスの選び方：段・サイズ・印刷",
        h1_ko="이커머스 메일러 박스 선택과 제작: 골, 치수, 인쇄",
        h1_fr="Mailer box e-commerce : cannelure, dimensions et impression",
        h1_es="Mailer box para e-commerce: corrugado, medidas e impresión",
        tag_zh="包装结构", tag_en="Packaging Structure", tag_ja="包装構造", tag_ko="포장 구조",
        tag_fr="Structure", tag_es="Estructura",
        sum_zh="飞机盒看起来只是一只纸箱，但楞型、尺寸、油墨和刀模任何一项没对上，最后都会变成运费、破损率或开箱体验上的成本。本文讲清三种结构、E/B/BC 楞怎么选、内尺寸与体积重怎么算、四种印刷后道的取舍，以及白样、色样、运输测试三步验收。",
        sum_en="A mailer box looks like a plain carton, yet the flute, size, ink and die each turn into freight cost, damage rate or unboxing experience. Covers three structures, choosing E, B or BC flute, inside size and volumetric weight, four print routes, and the white sample, colour sample, transit test sequence.",
        sum_ja="メーラーボックスは単なる箱に見えますが、段、サイズ、インキ、型のどれかが合わないと送料・破損率・開梱体験のコストになります。3つの構造、E/B/BC段の選び方、内寸と容積重量の計算、4つの印刷方式の使い分け、白サンプル・色サンプル・輸送試験の3段階検収を整理します。",
        sum_ko="메일러 박스는 평범한 상자처럼 보이지만 골, 치수, 잉크, 칼선 중 하나만 어긋나도 운임·파손률·개봉 경험의 비용이 됩니다. 세 가지 구조, E/B/BC골 선택, 내치수와 부피 무게 계산, 네 가지 인쇄 방식의 선택, 백 샘플·색상 샘플·운송 시험 3단계 검수를 다룹니다.",
        sum_fr="Une mailer box ressemble à un simple carton, mais cannelure, dimension, encre et forme se traduisent en coût de transport, taux de casse ou expérience d'ouverture. Au programme : trois structures, le choix E/B/BC, la dimension intérieure et le poids volumétrique, quatre voies d'impression, puis blanc, échantillon couleur et essai transport.",
        sum_es="Una mailer box parece un cartón simple, pero corrugado, medida, tinta y troquel se convierten en coste de envío, tasa de daños o experiencia de apertura. Cubre tres estructuras, la elección E/B/BC, la medida interior y el peso volumétrico, cuatro vías de impresión y la secuencia blanco, muestra de color y ensayo de transporte.",
    ),
    dict(
        slug="packaging-tape-guide.html",
        body="blog/_body_tape.html",
        title_zh="封箱胶带怎么选：BOPP、水性、牛皮纸与印字定制 | TAGE",
        title_en="Packing Tape Guide: BOPP, Acrylic, Kraft and Printed Tape | TAGE",
        title_ja="封緘テープの選び方：BOPP・水性・クラフト・印刷 | TAGE",
        title_ko="포장 테이프 선택: BOPP, 수성, 크라프트, 인쇄 | TAGE",
        title_fr="Adhésif d'emballage : BOPP, acrylique, kraft et impression | TAGE",
        title_es="Cinta de embalaje: BOPP, acrílica, kraft e impresa | TAGE",
        desc_zh="封箱胶带选型指南：BOPP 透明与印字、水性丙烯酸、牛皮纸、纤维胶带四种怎么选，厚度 40-50μm、初粘与持粘怎么读，印字定制的字高、版长与对比色要点，梅雨季与低温翘边的原因和工字形封箱法。来自东莞泰阁包装。",
        desc_en="Packing tape guide: BOPP, water-based acrylic, kraft and filament tape; thickness, tack and holding power; printed tape layout and cold-room fixes.",
        desc_ja="封緘テープの選び方。BOPP 透明・印刷、水性アクリル、クラフト、フィラメントの4種類、厚み40〜50μm・初期タック・保持力の読み方、印刷の文字高と版長、梅雨や低温での浮きの原因とH字封緘を解説します。東莞泰閣包装。",
        desc_ko="포장 테이프 선택 가이드. BOPP 투명·인쇄, 수성 아크릴, 크라프트, 필라멘트 네 종류, 두께 40~50μm·초기 점착·유지력 읽는 법, 인쇄 글자 높이와 판 길이, 장마·저온 들뜸 원인과 H자 봉인을 정리했습니다. 둥관 TAGE 패키징.",
        desc_fr="Guide de l'adhésif d'emballage : BOPP, acrylique à l'eau, kraft et filamentaire ; lire l'épaisseur, le tack initial et le pouvoir tenant ; impression et froid.",
        desc_es="Guía de la cinta de embalaje: BOPP, acrílica al agua, kraft y filamentosa; leer espesor, tack inicial y sujeción; cinta impresa y fallos por frío y humedad.",
        crumb_zh="封箱胶带",
        crumb_en="Packing Tape",
        crumb_ja="封緘テープ",
        crumb_ko="포장 테이프",
        crumb_fr="Adhésif d'emballage",
        crumb_es="Cinta de embalaje",
        h1_zh="封箱胶带怎么选：BOPP、水性、牛皮纸与印字定制",
        h1_en="Packing Tape Guide: BOPP, Acrylic, Kraft and Printed Tape",
        h1_ja="封緘テープの選び方：BOPP・水性・クラフト・印刷",
        h1_ko="포장 테이프 선택: BOPP, 수성, 크라프트, 인쇄",
        h1_fr="Adhésif d'emballage : BOPP, acrylique, kraft et impression",
        h1_es="Cinta de embalaje: BOPP, acrílica, kraft e impresa",
        tag_zh="包装耗材", tag_en="Packaging Consumables", tag_ja="包装資材", tag_ko="포장 자재",
        tag_fr="Consommables", tag_es="Consumibles",
        sum_zh="胶带是包装清单上最便宜的一项，却是唯一全程受力的部件。本文讲四种常用胶带的差别、厚度与初粘持粘怎么读、印字胶带的字高与版长怎么定，以及梅雨季、冷库与工字形封箱法的实际做法，最后给出四条常见问题的排查顺序。",
        sum_en="Tape is the cheapest line on the packing list and the only part loaded for the whole journey. Covers four tapes, reading thickness, tack and holding power, setting logo height and repeat length, what to do in humid and cold conditions, the H sealing pattern and a four-step troubleshooting order.",
        sum_ja="テープは包装リストで最も安い項目でありながら、輸送中ずっと荷重を受ける唯一の部材です。4種類の違い、厚みと初期タック・保持力の読み方、印刷の文字高と版長の決め方、梅雨・冷蔵・H字封緘の実際、そして4つの不具合の切り分け順を整理します。",
        sum_ko="테이프는 포장 목록에서 가장 저렴하지만 운송 내내 하중을 받는 유일한 부품입니다. 네 가지 테이프의 차이, 두께와 초기 점착·유지력 읽는 법, 인쇄 글자 높이와 판 길이 결정, 장마·냉장 환경과 H자 봉인 실무, 네 가지 문제의 점검 순서를 정리합니다.",
        sum_fr="L'adhésif est le poste le moins cher de la liste et la seule pièce sollicitée durant tout le trajet. Au programme : quatre adhésifs, lecture de l'épaisseur, du tack et du pouvoir tenant, hauteur de logo et pas de répétition, conditions humides et froides, montage en H et ordre de diagnostic.",
        sum_es="La cinta es el rubro más barato de la lista y la única pieza bajo carga durante todo el trayecto. Cubre cuatro cintas, cómo leer espesor, tack y sujeción, la altura de logo y la repetición, qué hacer con humedad y frío, el montaje en H y el orden de diagnóstico.",
    ),
]

skel = open(SKEL, encoding="utf-8").read()
old3 = re.search(r'"position": 3,\s*"name": "([^"]*)"', skel).group(1)
print("骨架 breadcrumb 名:", old3)

# ---------------- 撞车安全闸 ----------------
for a in ARTICLES:
    if not os.path.exists(a["body"]):
        raise SystemExit("正文文件缺失：%s" % a["body"])
    for p in ["blog/%s" % a["slug"]] + ["%s/blog/%s" % (l, a["slug"]) for l in LANGS]:
        if os.path.exists(p):
            raise SystemExit("选题撞车：%s 已存在，换选题！" % p)
sm0 = open("sitemap.xml", encoding="utf-8").read()
for a in ARTICLES:
    if ("/blog/%s</loc>" % a["slug"]) in sm0:
        raise SystemExit("选题撞车：sitemap 已含 %s" % a["slug"])
print("选题全新，开始生成")

for a in ARTICLES:
    print("  %-40s desc_zh=%d字 desc_en=%d字符 desc_ja=%d desc_ko=%d desc_fr=%d desc_es=%d"
          % (a["slug"], len(a["desc_zh"]), len(a["desc_en"]), len(a["desc_ja"]),
             len(a["desc_ko"]), len(a["desc_fr"]), len(a["desc_es"])))
if "--check" in sys.argv:
    sys.exit(0)

# ---------------- 1) 生成两篇文章（六语属性） ----------------
for a in ARTICLES:
    slug = a["slug"]
    s = skel.replace(SKEL.replace("blog/", ""), slug)

    title_line = ('<title data-zh="%s" data-en="%s" data-ja="%s" data-ko="%s" data-fr="%s" data-es="%s">%s</title>'
                  % (a["title_zh"], a["title_en"], a["title_ja"], a["title_ko"],
                     a["title_fr"], a["title_es"], a["title_zh"]))
    s = re.sub(r'<title[^>]*>.*?</title>', title_line, s, count=1, flags=re.S)

    s = re.sub(r'<meta name="description".*?content="[^"]*">', 'DESC_PLACEHOLDER', s, count=1, flags=re.S)
    desc_block = ('<meta name="description" data-zh="%s"\n'
                  '      data-en="%s" data-ja="%s" data-ko="%s"\n'
                  '      data-fr="%s"\n'
                  '      data-es="%s"\n'
                  '      content="%s">' % (a["desc_zh"], a["desc_en"], a["desc_ja"], a["desc_ko"],
                                           a["desc_fr"], a["desc_es"], a["desc_zh"]))
    s = s.replace('DESC_PLACEHOLDER', desc_block, 1)

    new_canon = ('<link rel="canonical" href="https://taigetag.com/blog/%s">\n'
                 '<link rel="alternate" hreflang="zh-Hant" href="https://taigetag.com/blog/%s">\n'
                 '<link rel="alternate" hreflang="en" href="https://taigetag.com/en/blog/%s">\n'
                 '<link rel="alternate" hreflang="fr" href="https://taigetag.com/fr/blog/%s">\n'
                 '<link rel="alternate" hreflang="es" href="https://taigetag.com/es/blog/%s">\n'
                 '<link rel="alternate" hreflang="ja" href="https://taigetag.com/ja/blog/%s">\n'
                 '<link rel="alternate" hreflang="ko" href="https://taigetag.com/ko/blog/%s">\n'
                 '<link rel="alternate" hreflang="x-default" href="https://taigetag.com/blog/%s">'
                 % ((slug,) * 8))
    s, n_href = re.subn(r'<link rel="canonical" href="[^"]*">(?:\n<link rel="alternate"[^\n]*>)+',
                        new_canon, s, count=1)
    assert n_href == 1, "hreflang 替换失败"

    crumb = ('<div class="crumb"><a href="../index.html" data-zh="首页" data-fr="Accueil" data-es="Inicio" data-en="Home" data-ja="ホーム" data-ko="홈">首页</a>'
             ' / <a href="index.html" data-zh="辅料 FAQ" data-fr="FAQ Accessoires" data-es="FAQ Accesorios" data-en="Trims FAQ" data-ja="副資材 FAQ" data-ko="부자재 FAQ">辅料 FAQ</a>'
             ' / <span data-zh="%s" data-en="%s" data-ja="%s" data-ko="%s" data-fr="%s" data-es="%s">%s</span></div>'
             % (a["crumb_zh"], a["crumb_en"], a["crumb_ja"], a["crumb_ko"],
                a["crumb_fr"], a["crumb_es"], a["crumb_zh"]))
    s, n = re.subn(r'<div class="crumb">.*?</div>', crumb, s, count=1, flags=re.S)
    assert n == 1, "crumb 替换失败"

    h1 = ('<h1 data-zh="%s" data-en="%s" data-ja="%s" data-ko="%s" data-fr="%s" data-es="%s">%s</h1>'
          % (a["h1_zh"], a["h1_en"], a["h1_ja"], a["h1_ko"], a["h1_fr"], a["h1_es"], a["h1_zh"]))
    s, n = re.subn(r'<h1 .*?</h1>', h1, s, count=1, flags=re.S)
    assert n == 1, "h1 替换失败"

    meta = ('<p data-zh="泰阁包装 · 更新于 %s" data-en="By TAGE Packaging &nbsp;·&nbsp; Updated %s" '
            'data-ja="泰閣包装 · %s" data-ko="TAGE 패키징 · %s" '
            'data-fr="Par TAGE Packaging &nbsp;·&nbsp; Mis à jour le %s" '
            'data-es="Por TAGE Packaging &nbsp;·&nbsp; Actualizado el %s">泰阁包装 · 更新于 %s</p>'
            % (DATE_ZH, DATE_EN, DATE_JA, DATE_KO, DATE_FR, DATE_ES, DATE_ZH))
    s, n = re.subn(r'<p data-zh="泰[阁閣]包[装裝] · 更新[于於][^\"]*\".*?</p>', meta, s, count=1, flags=re.S)
    assert n == 1, "meta 行替换失败"

    s = s.replace('"%s"' % old3, '"%s"' % a["h1_zh"])
    s, n = re.subn(r'"headline": "[^"]*"', '"headline": "%s"' % a["h1_zh"], s, count=1)
    assert n == 1, "headline 替换失败"

    body = open(a["body"], encoding="utf-8").read().rstrip("\n")
    i0 = s.index('  <section class="article-body">')
    i1 = s.index('\n</main>')
    s = s[:i0] + body + s[i1:]

    out = "blog/%s" % slug
    open(out, "w", encoding="utf-8", newline="").write(s)
    print("写入 %s (%d KB)" % (out, len(s.encode("utf-8")) // 1024))

# ---------------- 2) blog/index.html 顶部插入两张卡片 ----------------
CARD = '''      <article class="post-card">
        <span class="tag" data-zh="{tag_zh}" data-en="{tag_en}" data-ja="{tag_ja}" data-ko="{tag_ko}" data-fr="{tag_fr}" data-es="{tag_es}">{tag_zh}</span>
        <h3 data-zh="{h3_zh}" data-en="{h3_en}" data-ja="{h3_ja}" data-ko="{h3_ko}" data-fr="{h3_fr}" data-es="{h3_es}">{h3_zh}</h3>
        <p data-zh="{sum_zh}" data-en="{sum_en}" data-ja="{sum_ja}" data-ko="{sum_ko}" data-fr="{sum_fr}" data-es="{sum_es}">{sum_zh}</p>
        <a class="more" href="{slug}" data-zh="阅读全文 →" data-en="Read more →" data-ja="続きを読む →" data-ko="자세히 보기 →" data-fr="Lire la suite →" data-es="Leer más →">阅读全文 →</a>
      </article>
'''

cards = ""
for a in ARTICLES:
    cards += CARD.format(
        tag_zh=a["tag_zh"], tag_en=a["tag_en"], tag_ja=a["tag_ja"], tag_ko=a["tag_ko"],
        tag_fr=a["tag_fr"], tag_es=a["tag_es"],
        h3_zh=a["h1_zh"], h3_en=a["h1_en"], h3_ja=a["h1_ja"], h3_ko=a["h1_ko"],
        h3_fr=a["h1_fr"], h3_es=a["h1_es"],
        sum_zh=a["sum_zh"], sum_en=a["sum_en"], sum_ja=a["sum_ja"], sum_ko=a["sum_ko"],
        sum_fr=a["sum_fr"], sum_es=a["sum_es"],
        slug=a["slug"])

idx = "blog/index.html"
s = open(idx, encoding="utf-8").read()
marker = '<div class="post-grid">\n'
assert marker in s, "post-grid 未找到"
for a in ARTICLES:
    assert a["slug"] not in s, "卡已存在：%s" % a["slug"]
s = s.replace(marker, marker + "\n" + cards, 1)
open(idx, "w", encoding="utf-8", newline="").write(s)
print("blog/index.html 插入 2 张卡片完成")

# ---------------- 3) 简体 → 繁体（幂等） ----------------
spec = importlib.util.spec_from_file_location("to_traditional", os.path.join(ROOT, "to_traditional.py"))
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
changed = []
for p in ["blog/%s" % a["slug"] for a in ARTICLES] + [idx]:
    s0 = open(p, encoding="utf-8").read()
    s1 = mod.convert_html(s0)
    if s1 != s0:
        open(p, "w", encoding="utf-8", newline="").write(s1)
        changed.append(os.path.basename(p))
print("繁体转换改动: %d %s" % (len(changed), changed))

# ---------------- 4) gen_i18n 生成五语版本 ----------------
TARGETS = ["blog/%s" % a["slug"] for a in ARTICLES] + [idx]
for lang in LANGS:
    r = subprocess.run([PY, "gen_i18n.py", lang] + TARGETS, capture_output=True, text=True, encoding="utf-8")
    if r.returncode != 0:
        print(r.stdout[-3000:], r.stderr[-3000:])
        raise SystemExit("gen_i18n %s 失败" % lang)
    print("gen_i18n %s -> %d 文件 ok" % (lang, len(TARGETS)))

# ---------------- 5) sitemap ----------------
sm = open("sitemap.xml", encoding="utf-8", newline="").read()
before_lines = sm.count("\n")


def block(url):
    return ("  <url>\r\n    <loc>%s</loc>\r\n    <lastmod>%s</lastmod>\r\n"
            "    <changefreq>monthly</changefreq>\r\n    <priority>0.7</priority>\r\n  </url>\r\n"
            % (url, SITEMAP_DATE))


blocks = []
for a in ARTICLES:
    slug = a["slug"]
    for u in ["https://taigetag.com/blog/%s" % slug] + \
             ["https://taigetag.com/%s/blog/%s" % (l, slug) for l in LANGS]:
        assert "<loc>%s</loc>" % u not in sm, "sitemap 已有 %s" % u
        blocks.append(block(u))
sm = sm.replace("</urlset>", "".join(blocks) + "</urlset>", 1)

for u in ["https://taigetag.com/blog/index.html"] + \
         ["https://taigetag.com/%s/blog/index.html" % l for l in LANGS]:
    pat = re.compile(r'(<loc>%s</loc>\r?\n\s*<lastmod>)[^<]*(</lastmod>)' % re.escape(u))
    sm, n = pat.subn(r'\g<1>%s\g<2>' % SITEMAP_DATE, sm, count=1)
    assert n == 1, "blog index lastmod 未更新: %s" % u

open("sitemap.xml", "w", encoding="utf-8", newline="").write(sm)
print("sitemap 新增 %d 个 URL，行数 %d -> %d，<loc> 总数 %d"
      % (len(blocks), before_lines, sm.count("\n"), sm.count("<loc>")))

# ---------------- 6) BUST_VERSION 升级 ----------------
mj = open("js/main.js", encoding="utf-8").read()
assert 'var BUST_VERSION = "%s";' % BUST_OLD in mj, "BUST_VERSION 不是 %s" % BUST_OLD
mj = mj.replace('var BUST_VERSION = "%s";' % BUST_OLD, 'var BUST_VERSION = "%s";' % BUST_NEW, 1)
open("js/main.js", "w", encoding="utf-8", newline="").write(mj)
print("BUST_VERSION %s -> %s" % (BUST_OLD, BUST_NEW))
