#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-09-21 晚间 每日更新：2 篇新文章（六语：zh-Hant 根 / en / ja / ko / fr / es）
- 沙特阿拉伯服装标签合规指南（阿拉伯语标注 / SABER）
- 土耳其服装标签合规指南（土耳其语标注 / TAREKS）
+ 列表页卡片 + gen_i18n 五语生成 + sitemap + BUST_VERSION 升级 + 繁体转换。

用法: python daily_gen_20260921_evening.py
"""
import os, re, sys, subprocess, importlib.util

ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)
PY = sys.executable

SKEL = "blog/knitwear-sweater-trims-guide.html"
DATE_ZH = "2026年9月21日"
DATE_EN = "September 21, 2026"
DATE_JA = "2026年9月21日更新"
DATE_KO = "2026년 9월 21일 업데이트"
DATE_FR = "21 septembre 2026"
DATE_ES = "21 de septiembre de 2026"
SITEMAP_DATE = "2026-09-21"
BUST_OLD, BUST_NEW = "97", "98"
LANGS = ["en", "ja", "ko", "fr", "es"]

ARTICLES = [
    dict(
        slug="clothing-label-compliance-saudi-arabia.html",
        body="blog/_body_saudi.html",
        title_zh="沙特阿拉伯服装标签合规指南：阿拉伯语标注、SABER 与洗护符号 | TAGE",
        title_en="Saudi Arabia Clothing Label Requirements: Arabic Text, SABER &amp; Care Symbols | TAGE",
        title_ja="サウジアラビアの衣料ラベル規制ガイド：アラビア語表記・SABER・洗濯表示記号 | TAGE",
        title_ko="사우디아라비아 의류 라벨 규정 가이드: 아랍어 표기, SABER, 세탁 표시 기호 | TAGE",
        title_fr="Étiquetage des vêtements en Arabie saoudite : arabe, SABER et entretien | TAGE",
        title_es="Etiquetado de ropa en Arabia Saudita: árabe, SABER y símbolos de cuidado | TAGE",
        desc_zh="沙特阿拉伯服装标签合规指南：纺织产品技术法规要求标签以阿拉伯语标注纤维成分、洗护说明、原产地与责任方信息，进口清关走 SASO 的 SABER 平台，需产品与批次符合性证书。讲清七项必标信息、阿拉伯语排版与字号、ISO 3758 洗护符号对齐、吊牌织唛洗水标分工，附打样核对清单。来自东莞泰阁包装。",
        desc_en="Saudi Arabia clothing label rules: Arabic fibre content, care instructions, origin and importer details, plus SASO's SABER product and shipment certificates for customs clearance.",
        desc_ja="サウジアラビアの衣料ラベル規制ガイド。アラビア語での繊維組成・洗濯表示・原産地・責任者表記、SASO の SABER による製品・船積み適合証明、必須記載7項目、アラビア語の組版と文字サイズ、ISO 3758 記号との整合、サンプル前チェックリストを解説します。東莞泰閣包装。",
        desc_ko="사우디아라비아 의류 라벨 규정 가이드: 아랍어 섬유 조성·세탁 표시·원산지·책임자 표기, SASO의 SABER 제품·선적 적합성 인증, 필수 기재 7항목, 아랍어 조판과 글자 크기, ISO 3758 기호 정합, 샘플 전 체크리스트를 정리했습니다. 둥관 TAGE 패키징.",
        desc_fr="Étiquetage en Arabie saoudite : composition, entretien, origine et importateur en arabe, certificats SABER de la SASO, sept mentions obligatoires, mise en page arabe et symboles ISO 3758.",
        desc_es="Etiquetado en Arabia Saudita: composición, cuidado, origen e importador en árabe, certificados SABER de SASO, siete menciones obligatorias, maquetación árabe y símbolos ISO 3758.",
        crumb_zh="沙特标签合规", crumb_en="Saudi Label Rules", crumb_ja="サウジのラベル規制",
        crumb_ko="사우디 라벨 규정", crumb_fr="Étiquetage en Arabie saoudite", crumb_es="Etiquetado en Arabia Saudita",
        h1_zh="沙特阿拉伯服装标签合规指南：阿拉伯语标注、SABER 与洗护符号",
        h1_en="Saudi Arabia Clothing Label Requirements: Arabic Text, SABER and Care Symbols",
        h1_ja="サウジアラビアの衣料ラベル規制ガイド：アラビア語表記・SABER・洗濯表示記号",
        h1_ko="사우디아라비아 의류 라벨 규정 가이드: 아랍어 표기, SABER, 세탁 표시 기호",
        h1_fr="Étiquetage des vêtements en Arabie saoudite : arabe, SABER et symboles d'entretien",
        h1_es="Etiquetado de ropa en Arabia Saudita: árabe, SABER y símbolos de cuidado",
        tag_zh="合规指南", tag_en="Compliance", tag_ja="コンプライアンス", tag_ko="컴플라이언스",
        tag_fr="Conformité", tag_es="Cumplimiento",
        sum_zh="沙特市场的服装标签有两个硬门槛：文字必须用阿拉伯语，进口清关必须在 SASO 的 SABER 平台取得产品与批次符合性证书。本文讲清三层规则（技术法规、符合性评定、市场监督）、标签上不能少的七项信息、阿拉伯语的书写与排版要点（字号、数字写法、双向混排、连字断行）、ISO 3758 洗护符号与阿拉伯语文字的对齐、吊牌织唛洗水标包装袋的分工，并给出打样前六项核对清单。",
        sum_en="Two hard gates apply in Saudi Arabia: the label text must be in Arabic, and clearance needs SABER product and shipment certificates from SASO. This guide covers the three layers of rules, the seven mandatory label items, Arabic typesetting essentials, aligning ISO 3758 symbols with Arabic wording, how hang tags, woven labels, care labels and bags share the load, and a six-point pre-sampling checklist.",
        sum_ja="サウジ市場の衣料ラベルには二つの必須条件があります。表記はアラビア語であること、通関には SASO の SABER で製品・船積み適合証明を取得することです。本記事は三層の規制、必須記載7項目、アラビア語の組版要点（文字サイズ・数字・双方向テキスト・連字と改行）、ISO 3758 記号とアラビア語の整合、タグ・織りラベル・洗濯表示ラベル・包装袋の役割分担、サンプル前6項目チェックリストを解説します。",
        sum_ko="사우디 시장의 의류 라벨에는 두 가지 필수 조건이 있습니다. 표기는 아랍어여야 하고, 통관에는 SASO의 SABER에서 제품·선적 적합성 인증을 받아야 합니다. 이 글은 세 가지 규제 층, 필수 기재 7항목, 아랍어 조판 요점(글자 크기, 숫자, 양방향 텍스트, 연결 글자와 줄바꿈), ISO 3758 기호와 아랍어 문구의 정합, 행택·직조 라벨·세탁 표시 라벨·포장백의 역할 분담, 샘플 전 6항목 체크리스트를 정리합니다.",
        sum_fr="Deux conditions incontournables en Arabie saoudite : un texte en arabe et des certificats produit et d'expédition SABER de la SASO. Ce guide couvre les trois niveaux de règles, les sept mentions obligatoires, les points clés de la composition arabe, l'alignement des symboles ISO 3758, la répartition entre étiquettes et une liste de contrôle avant échantillon.",
        sum_es="Dos condiciones ineludibles en Arabia Saudita: texto en árabe y certificados de producto y embarque SABER de SASO. Esta guía cubre los tres niveles de normas, las siete menciones obligatorias, las claves de la maquetación árabe, la alineación de los símbolos ISO 3758, el reparto entre etiquetas y una lista de verificación previa a la muestra.",
    ),
    dict(
        slug="clothing-label-compliance-turkey.html",
        body="blog/_body_turkey.html",
        title_zh="土耳其服装标签合规指南：土耳其语标注、纤维成分与 TAREKS | TAGE",
        title_en="Turkey Clothing Label Requirements: Turkish Text, Fibre Content &amp; TAREKS | TAGE",
        title_ja="トルコの衣料ラベル規制ガイド：トルコ語表記・繊維組成・TAREKS | TAGE",
        title_ko="튀르키예 의류 라벨 규정 가이드: 터키어 표기, 섬유 조성, TAREKS | TAGE",
        title_fr="Étiquetage des vêtements en Turquie : turc, composition et TAREKS | TAGE",
        title_es="Etiquetado de ropa en Turquía: turco, composición y TAREKS | TAGE",
        desc_zh="土耳其服装标签合规指南：纺织与皮革产品标签条例以欧盟 1007/2011 为蓝本，消费者信息必须用土耳其语标注纤维成分、洗护说明、原产地与责任方，进口经 TAREKS 系统风险抽检。讲清术语对照表、成分公差与合并标注口径、TS EN ISO 3758 洗护符号、违规后果与打样核对清单。来自东莞泰阁包装。",
        desc_en="Turkey clothing label rules: Turkish-language fibre content, care and origin, a regulation modelled on EU 1007/2011, and TAREKS risk inspection at import, with a terminology table and checklist.",
        desc_ja="トルコの衣料ラベル規制ガイド。EU 1007/2011 を範とした繊維・皮革製品の表示規則、トルコ語での繊維組成・洗濯表示・原産地・責任者表記、輸入時の TAREKS リスク抽検、用語対照表、組成公差と一括表示、TS EN ISO 3758 記号、サンプル前チェックリストを解説します。東莞泰閣包装。",
        desc_ko="튀르키예 의류 라벨 규정 가이드: EU 1007/2011을 바탕으로 한 섬유·가죽 제품 표시 규정, 터키어 섬유 조성·세탁 표시·원산지·책임자 표기, 수입 시 TAREKS 위험 검사, 용어 대조표, 조성 공차와 통합 표기, TS EN ISO 3758 기호, 샘플 전 체크리스트를 정리했습니다. 둥관 TAGE 패키징.",
        desc_fr="Étiquetage en Turquie : texte turc obligatoire (composition, entretien, origine, responsable), règlement inspiré du UE 1007/2011, contrôle TAREKS à l'import, tableau terminologique et liste de contrôle.",
        desc_es="Etiquetado en Turquía: texto en turco obligatorio (composición, cuidado, origen, responsable), reglamento inspirado en el UE 1007/2011, inspección TAREKS y lista de verificación.",
        crumb_zh="土耳其标签合规", crumb_en="Turkey Label Rules", crumb_ja="トルコのラベル規制",
        crumb_ko="튀르키예 라벨 규정", crumb_fr="Étiquetage en Turquie", crumb_es="Etiquetado en Turquía",
        h1_zh="土耳其服装标签合规指南：土耳其语标注、纤维成分与 TAREKS",
        h1_en="Turkey Clothing Label Requirements: Turkish Text, Fibre Content and TAREKS",
        h1_ja="トルコの衣料ラベル規制ガイド：トルコ語表記・繊維組成・TAREKS",
        h1_ko="튀르키예 의류 라벨 규정 가이드: 터키어 표기, 섬유 조성, TAREKS",
        h1_fr="Étiquetage des vêtements en Turquie : turc, composition et TAREKS",
        h1_es="Etiquetado de ropa en Turquía: turco, composición y TAREKS",
        tag_zh="合规指南", tag_en="Compliance", tag_ja="コンプライアンス", tag_ko="컴플라이언스",
        tag_fr="Conformité", tag_es="Cumplimiento",
        sum_zh="土耳其的标签规则几乎与欧盟同源：消费者信息必须用土耳其语，纤维成分、洗护说明、原产地与责任方信息缺一不可，进口还要经贸易部的 TAREKS 系统风险抽检。本文给出标签常用土耳其语术语对照表、成分百分比与 ±3% 公差口径、低含量纤维合并标注的边界、TS EN ISO 3758 洗护符号与土耳其语文字的一致性要求、责任方必须是土耳其实体与违规后果，以及打样前六项核对清单。",
        sum_en="Turkey's labelling rules are almost EU-identical: consumer information must be in Turkish, composition, care, origin and the responsible party are all mandatory, and imports pass through the Ministry of Trade's TAREKS risk inspection. This guide gives a Turkish terminology table, the ±3 % composition tolerance, the limits of grouping minor fibres, symbol and Turkish-wording alignment, the Turkish-entity requirement and a six-point checklist.",
        sum_ja="トルコの表示規則は EU とほぼ同源です。消費者情報はトルコ語が必須で、繊維組成・洗濯表示・原産地・責任者情報はすべて必要、輸入時は貿易省の TAREKS によるリスク抽検も受けます。本記事はトルコ語の用語対照表、組成の ±3% 公差、低含有繊維の一括表示の境界、TS EN ISO 3758 記号とトルコ語の一致、責任者がトルコ法人である要件、サンプル前6項目チェックリストをまとめます。",
        sum_ko="튀르키예의 표시 규칙은 EU와 거의 같습니다. 소비자 정보는 터키어가 필수이고, 섬유 조성·세탁 표시·원산지·책임자 정보가 모두 필요하며, 수입 시 통상부 TAREKS 위험 검사도 받습니다. 이 글은 터키어 용어 대조표, ±3% 조성 공차, 저함량 섬유 통합 표기의 경계, TS EN ISO 3758 기호와 터키어 문구의 일치, 책임자가 튀르키예 법인이어야 하는 요건, 샘플 전 6항목 체크리스트를 정리합니다.",
        sum_fr="Les règles turques sont quasi identiques à celles de l'UE : informations en turc, composition, entretien, origine et responsable obligatoires, et contrôle TAREKS à l'import. Ce guide propose un tableau terminologique turc, la tolérance de composition de ±3 %, les limites du regroupement des fibres mineures, l'alignement des symboles, l'exigence d'un responsable turc et une liste de contrôle.",
        sum_es="Las reglas turcas son casi idénticas a las de la UE: información en turco, composición, cuidado, origen y responsable obligatorios, e inspección TAREKS en la importación. Esta guía ofrece una tabla terminológica turca, la tolerancia de composición de ±3 %, los límites de agrupar fibras minoritarias, la alineación de símbolos, la exigencia de un responsable turco y una lista de verificación.",
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
