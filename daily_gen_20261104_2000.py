#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-11-04 20:00 批次（六语：zh-Hant 根 / en / ja / ko / fr / es）
- 德国服装标签合规：TKG 成分标识、包装注册与德语要求（clothing-label-compliance-germany）
- 西班牙服装标签合规：西语成分标识、地区语言与塑料税（clothing-label-compliance-spain）

用法: F:/hermes/venvs/tools/Scripts/python.exe daily_gen_20261104_2000.py [--check]
"""
import os, re, sys, subprocess, importlib.util

ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)
PY = sys.executable

SKEL = "blog/knitwear-sweater-trims-guide.html"
DATE_ZH = "2026年11月4日"
DATE_EN = "November 4, 2026"
DATE_JA = "2026年11月4日"
DATE_KO = "2026년 11월 4일 업데이트"
DATE_FR = "4 novembre 2026"
DATE_ES = "4 de noviembre de 2026"
SITEMAP_DATE = "2026-11-04"
BUST_OLD, BUST_NEW = "198", "199"
LANGS = ["en", "ja", "ko", "fr", "es"]

ARTICLES = [
    dict(
        slug="clothing-label-compliance-germany.html",
        body="blog/_body_de.html",
        title_zh="德国服装标签合规：TKG 成分标识、包装注册与德语要求 | TAGE",
        title_en="Germany Apparel Labelling: TKG Fibre Names, LUCID and Language | TAGE",
        title_ja="ドイツの衣料ラベル規制：TKG の繊維表示・LUCID 登録・ドイツ語要件 | TAGE",
        title_ko="독일 의류 라벨 규정: TKG 섬유 표시·LUCID 등록·독일어 요건 | TAGE",
        title_fr="Étiquetage textile en Allemagne : TKG, enregistrement LUCID et langue | TAGE",
        title_es="Etiquetado textil en Alemania: TKG, registro LUCID y idioma | TAGE",
        desc_zh="德国服装标签合规：TKG 要求纤维名称用德语法定名称，洗护符号须与工艺一致；包装要在 LUCID 注册并按材质重量申报，GPSR 责任人信息要可读。附纤维名称对照表、包装数据口径与出货前八项检查。",
        desc_en="Germany apparel labelling: TKG German fibre names, care symbols that match the garment, LUCID packaging registration, GPSR details and a pre-shipment checklist.",
        desc_ja="ドイツの衣料ラベル規制を整理。TKG のドイツ語法定繊維名称、洗濯記号と加工の一致、包装の LUCID 登録と材質別重量申告、GPSR の責任者表示、繊維名称対照表と出荷前8項目チェックを掲載します。東莞泰閣包装。",
        desc_ko="독일 의류 라벨 규정 정리. TKG의 독일어 법정 섬유 명칭, 실제 공정과 일치하는 세탁 기호, 포장 LUCID 등록과 재질별 중량 신고, GPSR 책임자 표시, 섬유 명칭 대조표와 출하 전 여덟 가지 점검을 담았습니다. 둥관 TAGE 패키징.",
        desc_fr="Étiquetage textile en Allemagne : dénominations légales allemandes des fibres, symboles d'entretien cohérents, enregistrement LUCID, mentions GPSR et liste de contrôle avant expédition.",
        desc_es="Etiquetado textil en Alemania: denominaciones legales alemanas, símbolos de cuidado coherentes, registro LUCID, datos del GPSR y lista de control previa al envío.",
        crumb_zh="德國服裝標籤合規",
        crumb_en="Germany Labelling Compliance",
        crumb_ja="ドイツのラベル規制",
        crumb_ko="독일 라벨 규정",
        crumb_fr="Conformité en Allemagne",
        crumb_es="Cumplimiento en Alemania",
        h1_zh="德国服装标签合规：TKG 成分标识、包装注册与德语要求",
        h1_en="Germany Apparel Labelling: TKG Composition, Packaging Registration and the German Language",
        h1_ja="ドイツの衣料ラベル規制：TKG の組成表示・包装登録・ドイツ語要件",
        h1_ko="독일 의류 라벨 규정: TKG 조성 표시, 포장 등록, 독일어 요건",
        h1_fr="Étiquetage textile en Allemagne : composition TKG, enregistrement des emballages et langue",
        h1_es="Etiquetado textil en Alemania: composición TKG, registro de envases e idioma",
        tag_zh="合規與出口", tag_en="Compliance &amp; Export", tag_ja="コンプライアンス・輸出",
        tag_ko="컴플라이언스·수출", tag_fr="Conformité et export", tag_es="Cumplimiento y exportación",
        sum_zh="德国市场的退单，八成不是印刷质量问题，而是纤维名称写了英文、护理符号按国内习惯画、包装没在 LUCID 注册。这篇把 TKG 的德语名称、洗护与尺码的零售惯例、VerpackG 的注册申报、GPSR 责任人四项拆开讲，最后给八条出货前检查。",
        sum_en="Most German rejections are not print quality: they are English fibre names, care symbols drawn to domestic habit, and packaging never registered in LUCID. This covers TKG German names, retail care and sizing practice, VerpackG reporting, GPSR details, and eight pre-shipment checks.",
        sum_ja="ドイツでの返品は印刷品質より、繊維名称の英語表記、国内慣行の洗濯記号、LUCID 未登録の包装が原因です。TKG のドイツ語名称、洗濯とサイズの小売慣行、VerpackG の登録申告、GPSR の責任者表示を整理し、出荷前8項目チェックを添えます。",
        sum_ko="독일 반품은 인쇄 품질보다 영어 섬유 명칭, 국내 관행의 세탁 기호, LUCID 미등록 포장 때문입니다. TKG 독일어 명칭, 세탁과 사이즈 유통 관행, VerpackG 등록 신고, GPSR 책임자 표시를 정리하고 출하 전 여덟 가지 점검을 붙였습니다.",
        sum_fr="Les refus allemands tiennent rarement à l'impression : noms de fibres en anglais, symboles d'entretien dessinés selon l'habitude locale, emballages non enregistrés dans LUCID. TKG, pratique des tailles, déclaration VerpackG, mentions GPSR et huit contrôles avant expédition.",
        sum_es="Los rechazos alemanes rara vez son de impresión: fibras en inglés, símbolos de cuidado según la costumbre local y envases sin registrar en LUCID. TKG, práctica de tallas, declaración VerpackG, datos del GPSR y ocho controles previos al envío.",
    ),
    dict(
        slug="clothing-label-compliance-spain.html",
        body="blog/_body_es.html",
        title_zh="西班牙服装标签合规：RD 928/1987、地区语言与塑料税 | TAGE",
        title_en="Spain Apparel Labelling: RD 928/1987, Regional Language, Plastic Tax | TAGE",
        title_ja="スペインの衣料ラベル規制：RD 928/1987・地域言語・プラスチック税 | TAGE",
        title_ko="스페인 의류 라벨 규정: RD 928/1987·지역 언어·플라스틱세 | TAGE",
        title_fr="Étiquetage textile en Espagne : RD 928/1987, langues régionales, taxe plastique | TAGE",
        title_es="Etiquetado textil en España: RD 928/1987, lenguas cooficiales y tasa de plástico | TAGE",
        desc_zh="西班牙服装标签合规：RD 928/1987 要求西语标注纤维成分，地区语言另有要求；Ley 7/2022 对非再生塑料包装按每公斤 0.45 欧元征税，包装生产者还须注册并加入责任组织。附西语纤维名称表与出货前八项检查。",
        desc_en="Spain apparel labelling: RD 928/1987 fibre names, regional language, the EUR 0.45/kg plastic tax under Ley 7/2022, packaging EPR and a pre-shipment checklist.",
        desc_ja="スペインの衣料ラベル規制。RD 928/1987 によるスペイン語の繊維表示、地域言語の要件、Ley 7/2022 の非再生プラスチック包装への課税（1 kg あたり 0.45 ユーロ）、包装 EPR 登録、スペイン語の繊維名称表と出荷前8項目チェックを解説します。東莞泰閣包装。",
        desc_ko="스페인 의류 라벨 규정. RD 928/1987의 스페인어 섬유 표시, 지역 언어 요건, Ley 7/2022의 비재생 플라스틱 포장 과세(kg당 0.45유로), 포장 EPR 등록, 스페인어 섬유 명칭표와 출하 전 여덟 가지 점검을 정리합니다. 둥관 TAGE 패키징.",
        desc_fr="Étiquetage textile en Espagne : dénominations espagnoles (RD 928/1987), langues régionales, taxe plastique de la Ley 7/2022 à 0,45 EUR/kg, REP emballages et liste de contrôle.",
        desc_es="Etiquetado textil en España: denominaciones españolas (RD 928/1987), lenguas cooficiales, impuesto al plástico de la Ley 7/2022 a 0,45 EUR/kg, REP de envases y lista de control.",
        crumb_zh="西班牙服裝標籤合規",
        crumb_en="Spain Labelling Compliance",
        crumb_ja="スペインのラベル規制",
        crumb_ko="스페인 라벨 규정",
        crumb_fr="Conformité en Espagne",
        crumb_es="Cumplimiento en España",
        h1_zh="西班牙服装标签合规：西语成分标识、地区语言与塑料税",
        h1_en="Spain Apparel Labelling: Spanish Composition, Regional Language and the Plastic Tax",
        h1_ja="スペインの衣料ラベル規制：スペイン語の組成表示・地域言語・プラスチック税",
        h1_ko="스페인 의류 라벨 규정: 스페인어 조성 표시, 지역 언어, 플라스틱세",
        h1_fr="Étiquetage textile en Espagne : composition en espagnol, langues régionales et taxe plastique",
        h1_es="Etiquetado textil en España: composición en español, lenguas cooficiales y tasa de plástico",
        tag_zh="合規與出口", tag_en="Compliance &amp; Export", tag_ja="コンプライアンス・輸出",
        tag_ko="컴플라이언스·수출", tag_fr="Conformité et export", tag_es="Cumplimiento y exportación",
        sum_zh="西班牙是西语市场的门户，规则却叠了三层：欧盟条例、RD 928/1987 与 Ley 7/2022 的包装税。这篇讲西语纤维名称怎么写、地区语言什么时候要、塑料包装按重量怎么申报、纺织品 EPR 会带来什么，最后给八条出货前检查。",
        sum_en="Spain is the gateway to the Spanish-speaking market, with three stacked layers: the EU regulation, RD 928/1987 and the Ley 7/2022 packaging tax. Spanish fibre names, when regional language applies, how plastic packaging is declared by weight, what textile EPR will change, and eight checks before shipment.",
        sum_ja="スペインはスペイン語市場の入口であり、規則は三層です。EU 規則、RD 928/1987、Ley 7/2022 の包装税。スペイン語の繊維名称、地域言語が必要な場面、プラスチック包装の重量申告、繊維 EPR の影響、出荷前8項目チェックをまとめます。",
        sum_ko="스페인은 스페인어권 시장의 관문이며 규칙은 세 층입니다. EU 규정, RD 928/1987, Ley 7/2022 포장세. 스페인어 섬유 명칭, 지역 언어가 필요한 경우, 플라스틱 포장의 중량 신고, 섬유 EPR의 영향, 출하 전 여덟 가지 점검을 정리합니다.",
        sum_fr="L'Espagne est la porte du marché hispanophone, avec trois couches : règlement UE, RD 928/1987 et taxe emballages Ley 7/2022. Noms de fibres en espagnol, langues régionales, déclaration au poids, REP textile et huit contrôles avant expédition.",
        sum_es="España es la puerta del mercado hispano con tres capas: reglamento UE, RD 928/1987 y el impuesto al envase de la Ley 7/2022. Nombres de fibra en español, cuándo aplica la lengua cooficial, declaración por peso, REP textil y ocho controles previos al envío.",
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

    crumb = ('<div class="crumb"><a href="../index.html" data-zh="首頁" data-fr="Accueil" data-es="Inicio" data-en="Home" data-ja="ホーム" data-ko="홈">首頁</a>'
             ' / <a href="index.html" data-zh="輔料 FAQ" data-fr="FAQ Accessoires" data-es="FAQ Accesorios" data-en="Trims FAQ" data-ja="副資材 FAQ" data-ko="부자재 FAQ">輔料 FAQ</a>'
             ' / <span data-zh="%s" data-en="%s" data-ja="%s" data-ko="%s" data-fr="%s" data-es="%s">%s</span></div>'
             % (a["crumb_zh"], a["crumb_en"], a["crumb_ja"], a["crumb_ko"],
                a["crumb_fr"], a["crumb_es"], a["crumb_zh"]))
    s, n = re.subn(r'<div class="crumb">.*?</div>', crumb, s, count=1, flags=re.S)
    assert n == 1, "crumb 替换失败"

    h1 = ('<h1 data-zh="%s" data-en="%s" data-ja="%s" data-ko="%s" data-fr="%s" data-es="%s">%s</h1>'
          % (a["h1_zh"], a["h1_en"], a["h1_ja"], a["h1_ko"], a["h1_fr"], a["h1_es"], a["h1_zh"]))
    s, n = re.subn(r'<h1 .*?</h1>', h1, s, count=1, flags=re.S)
    assert n == 1, "h1 替换失败"

    meta = ('<p data-zh="泰閣包裝 · 更新於 %s" data-en="By TAGE Packaging &nbsp;·&nbsp; Updated %s" '
            'data-ja="泰閣包装 · %s更新" data-ko="TAGE 패키징 · %s" '
            'data-fr="Par TAGE Packaging &nbsp;·&nbsp; Mis à jour le %s" '
            'data-es="Por TAGE Packaging &nbsp;·&nbsp; Actualizado el %s">泰閣包裝 · 更新於 %s</p>'
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
    print("写入 %s (%d KB)" % (out, len(s.encode("utf-8")) // 1024))

# ---------------- 2) blog/index.html 顶部插入两张卡片 ----------------
CARD = '''      <article class="post-card">
        <span class="tag" data-zh="{tag_zh}" data-en="{tag_en}" data-ja="{tag_ja}" data-ko="{tag_ko}" data-fr="{tag_fr}" data-es="{tag_es}">{tag_zh}</span>
        <h3 data-zh="{h3_zh}" data-en="{h3_en}" data-ja="{h3_ja}" data-ko="{h3_ko}" data-fr="{h3_fr}" data-es="{h3_es}">{h3_zh}</h3>
        <p data-zh="{sum_zh}" data-en="{sum_en}" data-ja="{sum_ja}" data-ko="{sum_ko}" data-fr="{sum_fr}" data-es="{sum_es}">{sum_zh}</p>
        <a class="more" href="{slug}" data-zh="閱讀全文 →" data-en="Read more →" data-ja="続きを読む →" data-ko="자세히 보기 →" data-fr="Lire la suite →" data-es="Leer más →">閱讀全文 →</a>
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


def block(url):
    return ("  <url>\r\n    <loc>%s</loc>\r\n    <lastmod>%s</lastmod>\r\n"
            "    <changefreq>monthly</changefreq>\r\n    <priority>0.7</priority>\r\n  </url>\r\n"
            % (url, SITEMAP_DATE))


sm = open("sitemap.xml", encoding="utf-8", newline="").read()
before = sm.count("<loc>")
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
print("sitemap 新增 %d 个 URL，<loc> %d -> %d" % (len(blocks), before, sm.count("<loc>")))

# ---------------- 6) BUST_VERSION 升级 ----------------
mj = open("js/main.js", encoding="utf-8").read()
assert 'var BUST_VERSION = "%s";' % BUST_OLD in mj, "BUST_VERSION 不是 %s" % BUST_OLD
mj = mj.replace('var BUST_VERSION = "%s";' % BUST_OLD, 'var BUST_VERSION = "%s";' % BUST_NEW, 1)
open("js/main.js", "w", encoding="utf-8", newline="").write(mj)
print("BUST_VERSION %s -> %s" % (BUST_OLD, BUST_NEW))
