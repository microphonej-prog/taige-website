#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-11-05 08:00 批次（六语：zh-Hant 根 / en / ja / ko / fr / es）
- 波兰服装标签合规：波兰语标注、BDO 注册与包装 EPR（clothing-label-compliance-poland）
- 葡萄牙服装标签合规：葡语标注、包装 EPR 与环保声明（clothing-label-compliance-portugal）

用法: F:/hermes/venvs/tools/Scripts/python.exe daily_gen_20261105_0800.py [--check]
"""
import os, re, sys, subprocess, importlib.util

ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)
PY = sys.executable

SKEL = "blog/knitwear-sweater-trims-guide.html"
DATE_ZH = "2026年11月5日"
DATE_EN = "November 5, 2026"
DATE_JA = "2026年11月5日"
DATE_KO = "2026년 11월 5일 업데이트"
DATE_FR = "5 novembre 2026"
DATE_ES = "5 de noviembre de 2026"
SITEMAP_DATE = "2026-11-05"
BUST_OLD, BUST_NEW = "199", "200"
LANGS = ["en", "ja", "ko", "fr", "es"]

ARTICLES = [
    dict(
        slug="clothing-label-compliance-poland.html",
        body="blog/_body_pl.html",
        title_zh="波兰服装标签合规：波兰语标注、BDO 注册与包装 EPR | TAGE",
        title_en="Poland Apparel Labelling: Polish Text, BDO Registration and Packaging EPR | TAGE",
        title_ja="ポーランドの衣料ラベル規制：ポーランド語表示・BDO 登録・包装 EPR | TAGE",
        title_ko="폴란드 의류 라벨 규정: 폴란드어 표시·BDO 등록·포장 EPR | TAGE",
        title_fr="Étiquetage textile en Pologne : mentions en polonais, BDO et REP emballages | TAGE",
        title_es="Etiquetado textil en Polonia: menciones en polaco, registro BDO y REP de envases | TAGE",
        desc_zh="波兰服装标签合规：除欧盟 1007/2011 的纤维成分与洗涤符号，波兰语言法要求消费者信息用波兰语，包装还须在 BDO 系统登记并按材质重量申报 EPR。附波兰语纤维名称对照表、常见误写与出货前七项检查。",
        desc_en="Poland apparel labelling: EU 1007/2011 fibre names written in Polish, the Language Act, BDO packaging registration, EPR reporting and seven pre-shipment checks.",
        desc_ja="ポーランドの衣料ラベル規制を整理。EU 規則 1007/2011 の繊維組成と洗濯記号に加え、言語法によるポーランド語表示、包装の BDO 登録と EPR 申告、繊維名称の対照表と出荷前7項目チェックを掲載します。東莞泰閣包装。",
        desc_ko="폴란드 의류 라벨 규정 정리. EU 규정 1007/2011의 섬유 조성과 세탁 기호에 더해 폴란드 언어법상 폴란드어 표시, 포장 BDO 등록과 EPR 신고, 섬유 명칭 대조표와 출하 전 일곱 가지 점검을 담았습니다. 둥관 TAGE 패키징.",
        desc_fr="Étiquetage textile en Pologne : dénominations de fibres en polonais, loi linguistique, enregistrement BDO des emballages, déclaration REP et sept contrôles avant expédition.",
        desc_es="Etiquetado textil en Polonia: fibras en polaco, ley del idioma, registro BDO de envases, declaración REP y siete controles previos al envío.",
        crumb_zh="波兰服装标签合规",
        crumb_en="Poland Labelling Compliance",
        crumb_ja="ポーランドのラベル規制",
        crumb_ko="폴란드 라벨 규정",
        crumb_fr="Conformité en Pologne",
        crumb_es="Cumplimiento en Polonia",
        h1_zh="波兰服装标签合规：波兰语标注、BDO 注册与包装 EPR",
        h1_en="Poland Apparel Labelling: Polish Text, BDO Registration and Packaging EPR",
        h1_ja="ポーランドの衣料ラベル規制：ポーランド語表示・BDO 登録・包装 EPR",
        h1_ko="폴란드 의류 라벨 규정: 폴란드어 표시, BDO 등록, 포장 EPR",
        h1_fr="Étiquetage textile en Pologne : mentions en polonais, enregistrement BDO et REP emballages",
        h1_es="Etiquetado textil en Polonia: menciones en polaco, registro BDO y REP de envases",
        tag_zh="合规与出口", tag_en="Compliance &amp; Export", tag_ja="コンプライアンス・輸出",
        tag_ko="컴플라이언스·수출", tag_fr="Conformité et export", tag_es="Cumplimiento y exportación",
        sum_zh="波兰是中东欧最大的服装消费市场，退单往往不是印刷问题，而是纤维名称写了英文、消费者信息没有波兰语、包装没在 BDO 注册。这篇讲清三套规则的叠加，附波兰语纤维名称对照表与出货前七项检查。",
        sum_en="Poland is the largest apparel market in Central and Eastern Europe, and rejections rarely come from print quality: English fibre names, consumer information without Polish, packaging never registered in BDO. Three rule sets, a Polish fibre-name table and seven pre-shipment checks.",
        sum_ja="ポーランドは中東欧最大の衣料消費市場。返品は印刷品質より、繊維名称の英語表記、ポーランド語のない消費者情報、BDO 未登録の包装が原因です。三つの規制の重なり、繊維名称の対照表、出荷前7項目チェックをまとめます。",
        sum_ko="폴란드는 중동부 유럽 최대 의류 시장이며 반품은 인쇄 품질보다 영어 섬유 명칭, 폴란드어가 없는 소비자 정보, BDO 미등록 포장 때문입니다. 세 가지 규정의 중첩, 섬유 명칭 대조표, 출하 전 일곱 가지 점검을 정리합니다.",
        sum_fr="La Pologne est le premier marché textile d'Europe centrale. Les refus tiennent rarement à l'impression : noms de fibres en anglais, informations sans polonais, emballages non enregistrés dans BDO. Trois corpus, un tableau des fibres et sept contrôles.",
        sum_es="Polonia es el mayor mercado textil de Europa Central. Los rechazos rara vez son de impresión: fibras en inglés, información sin polaco y envases sin registrar en BDO. Tres corpus, tabla de fibras y siete controles.",
    ),
    dict(
        slug="clothing-label-compliance-portugal.html",
        body="blog/_body_pt.html",
        title_zh="葡萄牙服装标签合规：葡语标注、包装 EPR 与环保声明 | TAGE",
        title_en="Portugal Apparel Labelling: Portuguese Text, Packaging EPR and Green Claims | TAGE",
        title_ja="ポルトガルの衣料ラベル規制：ポルトガル語表示・包装 EPR・環境表示 | TAGE",
        title_ko="포르투갈 의류 라벨 규정: 포르투갈어 표시·포장 EPR·환경 표시 | TAGE",
        title_fr="Étiquetage textile au Portugal : portugais, REP emballages et allégations vertes | TAGE",
        title_es="Etiquetado textil en Portugal: portugués, REP de envases y declaraciones verdes | TAGE",
        desc_zh="葡萄牙服装标签合规：先分清责任主体是本地生产商、进口商还是欧盟责任人，再处理葡语纤维名称的重音、Ponto Verde 的包装 EPR 申报与欧盟 2024/825 的绿色声明边界。附主体分工表与出货前六项检查。",
        desc_en="Portugal apparel labelling: Portuguese fibre names, producer versus importer details, Ponto Verde packaging EPR and the limits of recycled-content claims.",
        desc_ja="ポルトガルの衣料ラベル規制を整理。責任主体の切り分け、ポルトガル語の繊維名称とアクセント、Ponto Verde による包装 EPR 申告、EU 2024/825 の環境表示の境界、出荷前6項目チェックを掲載します。東莞泰閣包装。",
        desc_ko="포르투갈 의류 라벨 규정 정리. 책임 주체 구분, 포르투갈어 섬유 명칭과 악센트, Ponto Verde 포장 EPR 신고, EU 2024/825 환경 표시의 경계, 출하 전 여섯 가지 점검을 담았습니다. 둥관 TAGE 패키징.",
        desc_fr="Étiquetage textile au Portugal : dénominations portugaises, responsable selon la voie d'entrée, REP emballages Ponto Verde et limites des allégations de contenu recyclé.",
        desc_es="Etiquetado textil en Portugal: denominaciones portuguesas, responsable según la vía de entrada, REP de envases Ponto Verde y límites de las declaraciones de reciclado.",
        crumb_zh="葡萄牙服装标签合规",
        crumb_en="Portugal Labelling Compliance",
        crumb_ja="ポルトガルのラベル規制",
        crumb_ko="포르투갈 라벨 규정",
        crumb_fr="Conformité au Portugal",
        crumb_es="Cumplimiento en Portugal",
        h1_zh="葡萄牙服装标签合规：葡语标注、包装 EPR 与环保声明",
        h1_en="Portugal Apparel Labelling: Portuguese Text, Packaging EPR and Green Claims",
        h1_ja="ポルトガルの衣料ラベル規制：ポルトガル語表示・包装 EPR・環境表示",
        h1_ko="포르투갈 의류 라벨 규정: 포르투갈어 표시, 포장 EPR, 환경 표시",
        h1_fr="Étiquetage textile au Portugal : mentions en portugais, REP emballages et allégations vertes",
        h1_es="Etiquetado textil en Portugal: menciones en portugués, REP de envases y declaraciones verdes",
        tag_zh="合规与出口", tag_en="Compliance &amp; Export", tag_ja="コンプライアンス・輸出",
        tag_ko="컴플라이언스·수출", tag_fr="Conformité et export", tag_es="Cumplimiento y exportación",
        sum_zh="葡萄牙既生产又消费，标签上写谁当责任主体取决于货怎么进入市场；葡语纤维名称的重音不能省，包装走 Ponto Verde 的绿点费率，环保声明还受欧盟 2024/825 约束。附主体分工表与出货前六项检查。",
        sum_en="Portugal both produces and consumes, so the responsible party depends on how the goods enter the market. Portuguese accents are mandatory, packaging runs through Ponto Verde, and green claims answer to EU 2024/825. A responsibility table and six pre-shipment checks.",
        sum_ja="ポルトガルは生産と消費の両方を持ち、責任主体は市場への入り方で変わります。ポルトガル語のアクセントは必須、包装は Ponto Verde の料率、環境表示は EU 2024/825 の枠内です。責任分担表と出荷前6項目チェックを掲載します。",
        sum_ko="포르투갈은 생산과 소비를 함께 가져 책임 주체가 시장 진입 방식에 따라 달라집니다. 포르투갈어 악센트는 필수이고 포장은 Ponto Verde 요율을 따르며 환경 표시는 EU 2024/825의 틀 안에 있습니다. 책임 구분표와 출하 전 여섯 가지 점검을 담았습니다.",
        sum_fr="Le Portugal produit et consomme : le responsable dépend de la voie d'entrée. Les accents portugais sont obligatoires, l'emballage passe par Ponto Verde et les allégations vertes relèvent de l'UE 2024/825. Tableau des responsabilités et six contrôles.",
        sum_es="Portugal produce y consume: el responsable depende de la vía de entrada. Los acentos portugueses son obligatorios, el envase pasa por Ponto Verde y las declaraciones verdes responden a la UE 2024/825. Tabla de responsables y seis controles.",
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
            'data-ja="泰閣包装 · %s更新" data-ko="TAGE 패키징 · %s" '
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
