#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-09-22 晚间 每日更新：2 篇新文章（六语：zh-Hant 根 / en / ja / ko / fr / es）
- 欧盟数字产品护照（DPP）与服装辅料：标签与数据准备
- 服装辅料碳足迹核算：品牌 PCF 问卷怎么答
+ 列表页卡片 + gen_i18n 五语生成 + sitemap + BUST_VERSION 升级 + 简体转繁。

用法: python daily_gen_20260922_evening.py
"""
import os, re, sys, subprocess, importlib.util

ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)
PY = sys.executable

SKEL = "blog/knitwear-sweater-trims-guide.html"
DATE_ZH = "2026年9月22日"
DATE_EN = "September 22, 2026"
DATE_JA = "2026年9月22日更新"
DATE_KO = "2026년 9월 22일 업데이트"
DATE_FR = "22 septembre 2026"
DATE_ES = "22 de septiembre de 2026"
SITEMAP_DATE = "2026-09-22"
BUST_OLD, BUST_NEW = "100", "101"
LANGS = ["en", "ja", "ko", "fr", "es"]

ARTICLES = [
    dict(
        slug="eu-digital-product-passport-trims.html",
        body="blog/_body_dpp.html",
        title_zh="欧盟数字产品护照（DPP）与服装辅料指南：标签与数据准备 | TAGE",
        title_en="EU Digital Product Passport (DPP) for Apparel Trims &amp; Labels | TAGE",
        title_ja="EUデジタル製品パスポート（DPP）と衣料副資材：ラベルとデータ準備ガイド | TAGE",
        title_ko="EU 디지털 제품 여권(DPP)과 의류 부자재: 라벨과 데이터 준비 가이드 | TAGE",
        title_fr="Passeport numérique de produit (DPP) de l'UE et accessoires textiles : étiquettes et données | TAGE",
        title_es="Pasaporte digital de producto (DPP) de la UE y accesorios textiles: etiquetas y datos | TAGE",
        desc_zh="欧盟数字产品护照（DPP）与服装辅料指南：讲清 ESPR 法规要求、DPP 需要的数据字段、二维码与 NFC 等数据载体如何配合吊牌、织唛与洗水标，以及辅料厂现在就该归拢的材料与批次数据。来自东莞泰阁包装。",
        desc_en="EU Digital Product Passport (DPP) for apparel trims: what ESPR requires, the data fields, where QR and NFC carriers go on labels, and what to prepare now.",
        desc_ja="EU デジタル製品パスポート（DPP）と衣料副資材のガイド。ESPR の要件、必要なデータ項目、QR コードや NFC をタグ・織りラベル・洗濯表示ラベルにどう載せるか、今から整理すべき材料とロット情報を解説します。東莞泰閣包装。",
        desc_ko="EU 디지털 제품 여권(DPP)과 의류 부자재 가이드. ESPR 요구사항, 필요한 데이터 항목, QR과 NFC를 행택·직조 라벨·세탁 표시 라벨에 어떻게 적용하는지, 지금 정리해야 할 소재와 로트 정보를 정리했습니다. 둥관 TAGE 패키징.",
        desc_fr="Passeport numérique de produit (DPP) et accessoires textiles : exigences ESPR, champs de données, intégration des codes QR et NFC sur les étiquettes, et les données à préparer dès maintenant.",
        desc_es="Pasaporte digital de producto (DPP) y accesorios textiles: requisitos ESPR, campos de datos, códigos QR y NFC en las etiquetas, y los datos que conviene preparar desde ahora.",
        crumb_zh="数字产品护照", crumb_en="Digital Product Passport", crumb_ja="デジタル製品パスポート",
        crumb_ko="디지털 제품 여권", crumb_fr="Passeport numérique", crumb_es="Pasaporte digital",
        h1_zh="欧盟数字产品护照（DPP）与服装辅料指南：标签与数据准备",
        h1_en="EU Digital Product Passport (DPP) for Apparel Trims and Labels",
        h1_ja="EUデジタル製品パスポート（DPP）と衣料副資材：ラベルとデータ準備ガイド",
        h1_ko="EU 디지털 제품 여권(DPP)과 의류 부자재: 라벨과 데이터 준비 가이드",
        h1_fr="Passeport numérique de produit (DPP) et accessoires textiles : étiquettes et données",
        h1_es="Pasaporte digital de producto (DPP) y accesorios textiles: etiquetas y datos",
        tag_zh="合规法规", tag_en="Compliance", tag_ja="法令対応", tag_ko="규정 대응",
        tag_fr="Conformité", tag_es="Cumplimiento",
        sum_zh="DPP 正在把吊牌、织唛与洗水标从印刷品变成数据入口。本文讲清 ESPR 的时间表与不确定性、需要归拢的数据字段、二维码与 NFC 分别该放在吊牌、耐久标还是包装袋上，以及辅料厂现在就能做的四项准备，并给出可直接回复客户问卷的说法。",
        sum_en="The DPP is turning hang tags, woven labels and care labels into data entry points. This guide covers the ESPR timeline and its uncertainties, the data fields to organise, where QR and NFC carriers belong, four preparations a factory can start now, and a ready answer to buyer questionnaires.",
        sum_ja="DPP はタグ・織りラベル・洗濯表示ラベルを印刷物からデータの入口へ変えつつあります。本記事は ESPR のスケジュールと不確実性、整理すべきデータ項目、QR と NFC をタグ・永久表示・包装のどこに置くか、今すぐできる4つの準備、質問票への回答案を示します。",
        sum_ko="DPP는 행택, 직조 라벨, 세탁 표시 라벨을 인쇄물에서 데이터 진입점으로 바꾸고 있습니다. 이 글은 ESPR 일정과 불확실성, 정리해야 할 데이터 항목, QR과 NFC를 행택·영구 표시·포장 중 어디에 둘지, 지금 가능한 네 가지 준비와 설문 답변 예시를 제시합니다.",
        sum_fr="Le DPP transforme les étiquettes suspendues, tissées et d'entretien en points d'accès aux données. Ce guide couvre le calendrier ESPR et ses incertitudes, les champs à organiser, la place des supports QR et NFC, quatre préparations immédiates et une réponse type aux questionnaires.",
        sum_es="El DPP convierte las etiquetas colgantes, tejidas y de cuidado en puntos de acceso a datos. Esta guía cubre el calendario ESPR y sus incertidumbres, los campos a organizar, dónde van los soportes QR y NFC, cuatro preparaciones inmediatas y una respuesta tipo a los cuestionarios.",
    ),
    dict(
        slug="trims-carbon-footprint-guide.html",
        body="blog/_body_carbon.html",
        title_zh="服装辅料碳足迹核算指南：品牌问卷怎么答 | TAGE",
        title_en="Trim Carbon Footprint: Answering Brand PCF Questionnaires | TAGE",
        title_ja="衣料副資材のカーボンフットプリント：ブランド質問票への回答ガイド | TAGE",
        title_ko="의류 부자재 탄소발자국: 브랜드 설문 대응 가이드 | TAGE",
        title_fr="Empreinte carbone des accessoires : répondre aux questionnaires des marques | TAGE",
        title_es="Huella de carbono de accesorios: responder a los cuestionarios de las marcas | TAGE",
        desc_zh="服装辅料碳足迹指南：讲清品牌问卷的三种口径、辅料排放的四个热点、从物料重量到第三方验证的三级可信度做法、功能单位与分摊要点，并给出一张可直接并入生产记录的碳数据采集表。来自东莞泰阁包装。",
        desc_en="Trim carbon footprint: three accounting bases buyers use, four emission hot spots, three data tiers, and a data sheet to fold into your production records.",
        desc_ja="衣料副資材のカーボンフットプリント。バイヤー質問票の3つの口径、排出の4つの要点、材料重量から第三者検証までの3段階、機能単位と配分、生産記録に組み込める収集表を解説します。東莞泰閣包装。",
        desc_ko="의류 부자재 탄소발자국 가이드: 바이어 설문의 세 가지 기준, 배출 핵심 네 영역, 소재 중량부터 제3자 검증까지 세 단계, 기능 단위와 배분, 생산 기록에 통합할 데이터 수집표를 정리했습니다. 둥관 TAGE 패키징.",
        desc_fr="Empreinte carbone des accessoires : trois bases de calcul, quatre postes d'émission, trois niveaux de données, unité fonctionnelle et allocation, et une fiche de collecte à intégrer aux relevés.",
        desc_es="Huella de carbono de accesorios: tres bases de cálculo, cuatro focos de emisión, tres niveles de datos, unidad funcional y asignación, y una ficha de recogida integrable.",
        crumb_zh="辅料碳足迹", crumb_en="Trim Carbon Footprint", crumb_ja="副資材の炭素排出",
        crumb_ko="부자재 탄소발자국", crumb_fr="Empreinte carbone", crumb_es="Huella de carbono",
        h1_zh="服装辅料碳足迹核算指南：品牌问卷怎么答",
        h1_en="Trim Carbon Footprint: Answering Brand PCF Questionnaires",
        h1_ja="衣料副資材のカーボンフットプリント：ブランド質問票への回答ガイド",
        h1_ko="의류 부자재 탄소발자국: 브랜드 설문 대응 가이드",
        h1_fr="Empreinte carbone des accessoires : répondre aux questionnaires des marques",
        h1_es="Huella de carbono de accesorios: responder a los cuestionarios de las marcas",
        tag_zh="可持续发展", tag_en="Sustainability", tag_ja="サステナビリティ", tag_ko="지속가능성",
        tag_fr="Durabilité", tag_es="Sostenibilidad",
        sum_zh="品牌问卷里的碳足迹条目越来越多，辅料往往是最容易漏算的一块。本文讲清三种核算口径的区别、辅料排放的四个热点、从物料重量到第三方验证的三级可信度做法、功能单位与分摊的要点，并给出一张能直接并入现有生产记录的碳数据采集表。",
        sum_en="Carbon items keep multiplying in brand questionnaires, and trims are the block most often left out. This guide separates the three accounting bases, marks the four emission hot spots, ranks three data tiers from material mass to verified factors, covers functional units and allocation, and ends with a data sheet you can fold into existing records.",
        sum_ja="ブランドの質問票でカーボン項目は増え続け、副資材は最も漏れやすい部分です。本記事は3つの口径の違い、排出の4つの要点、材料重量から第三者検証までの3段階、機能単位と配分の注意点を整理し、既存の生産記録に組み込める収集表を提示します。",
        sum_ko="브랜드 설문의 탄소 항목은 계속 늘고 부자재는 가장 자주 빠지는 부분입니다. 이 글은 세 가지 산정 기준의 차이, 배출 핵심 네 영역, 소재 중량부터 제3자 검증까지 세 단계, 기능 단위와 배분의 요점을 정리하고 기존 생산 기록에 통합할 수 있는 수집표를 제시합니다.",
        sum_fr="Les items carbone se multiplient dans les questionnaires et les accessoires sont le bloc le plus souvent oublié. Ce guide distingue trois bases de calcul, marque quatre postes d'émission, classe trois niveaux de données et se termine par une fiche à intégrer aux relevés existants.",
        sum_es="Las partidas de carbono se multiplican en los cuestionarios y los accesorios son el bloque que más se omite. Esta guía distingue tres bases de cálculo, señala cuatro focos de emisión, ordena tres niveles de datos y termina con una ficha integrable en los registros actuales.",
    ),
]

skel = open(SKEL, encoding="utf-8").read()
old3 = re.search(r'"position": 3,\s*"name": "([^"]*)"', skel).group(1)
print("骨架 breadcrumb 名:", old3)

# ---------------- 撞车安全闸 ----------------
sm0 = open("sitemap.xml", encoding="utf-8").read()
for a in ARTICLES:
    for p in ["blog/%s" % a["slug"]] + ["%s/blog/%s" % (l, a["slug"]) for l in LANGS]:
        if os.path.exists(p):
            raise SystemExit("选题撞车：%s 已存在，换选题！" % p)
    if ("/blog/%s</loc>" % a["slug"]) in sm0:
        raise SystemExit("选题撞车：sitemap 已含 %s" % a["slug"])
print("选题全新，开始生成")

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
    s, n = re.subn(r'<p data-zh="泰[阁閣]包[装裝] · 更新[于於][^"]*".*?</p>', meta, s, count=1, flags=re.S)
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
    print("写入 %s (%d KB) desc_zh=%d字 desc_en=%d字符 desc_ja=%d desc_ko=%d desc_fr=%d desc_es=%d"
          % (out, len(s.encode("utf-8")) // 1024, len(a["desc_zh"]), len(a["desc_en"]),
             len(a["desc_ja"]), len(a["desc_ko"]), len(a["desc_fr"]), len(a["desc_es"])))

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
mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
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
