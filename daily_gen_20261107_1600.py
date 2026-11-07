#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-11-07 16:00 批次（六语：zh-Hant 根 / en / ja / ko / fr / es）
- 中美洲服装标签合规（clothing-label-compliance-central-america）
- 摩洛哥与突尼斯服装标签合规（clothing-label-compliance-morocco-tunisia）

用法: F:/hermes/venvs/tools/Scripts/python.exe daily_gen_20261107_1600.py [--check]
"""
import os, re, sys, subprocess, importlib.util

ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)
PY = sys.executable

SKEL = "blog/knitwear-sweater-trims-guide.html"
DATE_ZH = "2026年11月7日"
DATE_EN = "November 7, 2026"
DATE_JA = "2026年11月7日"
DATE_KO = "2026년 11월 7일 업데이트"
DATE_FR = "7 novembre 2026"
DATE_ES = "7 de noviembre de 2026"
SITEMAP_DATE = "2026-11-07"
BUST_OLD, BUST_NEW = "202", "203"
LANGS = ["en", "ja", "ko", "fr", "es"]

ARTICLES = [
    dict(
        slug="clothing-label-compliance-central-america.html",
        body="blog/_body_ca.html",
        title_zh="中美洲服装标签合规：CAFTA-DR 六国的西语标注要求 | TAGE",
        title_en="Central America Clothing Labels: Spanish Text, CAFTA-DR &amp; US Rules | TAGE",
        title_ja="中米の衣料ラベル規制：CAFTA-DR 6か国のスペイン語表示と米国要件 | TAGE",
        title_ko="중미 의류 라벨 규정: CAFTA-DR 6개국 스페인어 표기와 미국 요건 | TAGE",
        title_fr="Étiquetage textile en Amérique centrale : espagnol, CAFTA-DR et règles américaines | TAGE",
        title_es="Etiquetado textil en Centroamérica: español, CAFTA-DR y normas de EE. UU. | TAGE",
        desc_zh="中美洲服装标签合规：六国要求西班牙语标注成分、护理、Hecho en 原产地与进口商地址，回销美国还要叠加 FTC 要求。讲清六国执行差异、CAFTA-DR 下中国产吊牌是否影响免税、西语版面与织唛密度，附打样前六项清单。来自东莞泰阁包装。",
        desc_en="Central America clothing labels: Spanish fibre content, care symbols, Hecho en origin and importer details, plus the US FTC rules garments need on the way back.",
        desc_ja="中米6か国の衣料ラベル規制。スペイン語の繊維組成・取扱い表示・Hecho en 原産地・輸入者情報に、米国 FTC と 16 CFR 423 の要件が重なります。各国の運用差、CAFTA-DR における中国製値札の扱い、スペイン語の版面と織り密度、サンプル前の六項目を整理します。",
        desc_ko="중미 6개국 의류 라벨 규정. 스페인어 섬유 조성·취급 표시·Hecho en 원산지·수입자 정보에 미국 FTC와 16 CFR 423 요건이 겹칩니다. 국가별 집행 차이, CAFTA-DR에서 중국산 행택의 처리, 스페인어 레이아웃과 직조 밀도, 샘플 전 여섯 항목을 정리합니다.",
        desc_fr="Étiquetage en Amérique centrale : composition en espagnol, entretien, origine Hecho en et coordonnées de l'importateur, plus les règles FTC côté américain.",
        desc_es="Etiquetado en Centroamérica: composición en español, cuidado, origen Hecho en y datos del importador, más las reglas FTC del lado estadounidense.",
        crumb_zh="中美洲标签合规",
        crumb_en="Central America Label Rules",
        crumb_ja="中米のラベル規制",
        crumb_ko="중미 라벨 규정",
        crumb_fr="Conformité Amérique centrale",
        crumb_es="Cumplimiento Centroamérica",
        h1_zh="中美洲服装标签合规：CAFTA-DR 六国的西语标注要求",
        h1_en="Central America Clothing Labels: Spanish Text, CAFTA-DR and US Rules",
        h1_ja="中米の衣料ラベル規制：CAFTA-DR 6か国のスペイン語表示と米国要件",
        h1_ko="중미 의류 라벨 규정: CAFTA-DR 6개국 스페인어 표기와 미국 요건",
        h1_fr="Étiquetage textile en Amérique centrale : espagnol, CAFTA-DR et règles américaines",
        h1_es="Etiquetado textil en Centroamérica: español, CAFTA-DR y normas de EE. UU.",
        tag_zh="合规与出口", tag_en="Compliance &amp; Export", tag_ja="コンプライアンス・輸出",
        tag_ko="컴플라이언스·수출", tag_fr="Conformité et export", tag_es="Cumplimiento y exportación",
        sum_zh="订单搬到中美洲，标签却还按美国模板印：西语成分、护理、Hecho en 与进口商地址少一样就可能被零售仓退回。这篇拆开两套规则的交集、六国执行差异、CAFTA-DR 下中国产吊牌是否影响免税，以及西语版面为什么总比英语长两成。",
        sum_en="Orders moved to Central America, labels stayed on a US template: miss Spanish composition, care, Hecho en or the importer address and the retail warehouse sends it back. Two rule sets, six enforcement styles, CAFTA-DR treatment of Chinese tags, and why Spanish copy runs a fifth longer.",
        sum_ja="発注先は中米に移っても、ラベルは米国テンプレートのまま。スペイン語の組成・取扱い・Hecho en・輸入者住所のどれか一つ欠けると小売倉庫で返品されます。二つの規則の重なり、6か国の運用差、CAFTA-DR での中国製値札の扱い、スペイン語が二割長くなる理由を整理します。",
        sum_ko="오더는 중미로 옮겼는데 라벨은 미국 템플릿 그대로. 스페인어 조성·취급·Hecho en·수입자 주소 중 하나만 빠져도 물류창고에서 반송됩니다. 두 규정의 교집합, 6개국 집행 차이, CAFTA-DR에서 중국산 행택 처리, 스페인어가 20% 길어지는 이유를 정리합니다.",
        sum_fr="Les commandes sont parties en Amérique centrale, les étiquettes sont restées sur un gabarit américain : une mention espagnole manquante et l'entrepôt refuse. Deux corpus, six applications nationales, le sort des cartons chinois sous CAFTA-DR et la longueur de l'espagnol.",
        sum_es="Los pedidos se mudaron a Centroamérica y las etiquetas se quedaron en la plantilla estadounidense: si falta la composición en español, el cuidado, el Hecho en o la dirección del importador, el almacén devuelve. Dos marcos, seis aplicaciones y el largo del español.",
    ),
    dict(
        slug="clothing-label-compliance-morocco-tunisia.html",
        body="blog/_body_ma.html",
        title_zh="摩洛哥与突尼斯服装标签合规：阿拉伯语、法语与欧盟 GPSR 要求 | TAGE",
        title_en="Morocco and Tunisia Clothing Labels: Arabic, French and EU GPSR | TAGE",
        title_ja="モロッコ・チュニジアの衣料ラベル：アラビア語・仏語と EU GPSR の要件 | TAGE",
        title_ko="모로코·튀니지 의류 라벨: 아랍어·프랑스어와 EU GPSR 요건 | TAGE",
        title_fr="Étiquetage au Maroc et en Tunisie : arabe, français et GPSR européen | TAGE",
        title_es="Etiquetado en Marruecos y Túnez: árabe, francés y GPSR europeo | TAGE",
        desc_zh="摩洛哥与突尼斯服装标签合规：当地要求阿拉伯语标注（可并法语），卖到欧盟还要满足 1007/2011 纤维名称与 GPSR 欧盟责任人。讲清阿语在织唛与洗标上的可行字号、右到左排版、三国要求对照与三个最常见错误。来自东莞泰阁包装。",
        desc_en="Morocco and Tunisia clothing labels: Arabic at origin, plus EU 1007/2011 fibre names and the GPSR responsible person, with Arabic type limits on woven labels.",
        desc_ja="モロッコ・チュニジアの衣料ラベル。現地はアラビア語表示（仏語併記可）、EU 販売には 1007/2011 の繊維名と GPSR の域内責任者が加わります。織りラベルで可能なアラビア語の字高、右から左の版面、3要件の対照、よくある三つの誤りを整理します。",
        desc_ko="모로코·튀니지 의류 라벨. 현지는 아랍어 표기(프랑스어 병기 가능), EU 판매에는 1007/2011 섬유 명칭과 GPSR 역내 책임자가 더해집니다. 직조 라벨에서 가능한 아랍어 글자 크기, 오른쪽에서 왼쪽 레이아웃, 세 요건 대조와 흔한 실수 세 가지를 정리합니다.",
        desc_fr="Étiquetage au Maroc et en Tunisie : arabe à l'origine, plus 1007/2011 et le responsable GPSR côté UE, avec les limites de corps de texte en tissé.",
        desc_es="Etiquetado en Marruecos y Túnez: árabe en origen, más 1007/2011 y el responsable GPSR en la UE, con los límites de cuerpo en etiqueta tejida.",
        crumb_zh="摩洛哥与突尼斯标签",
        crumb_en="Morocco and Tunisia Labels",
        crumb_ja="モロッコ・チュニジアのラベル",
        crumb_ko="모로코·튀니지 라벨",
        crumb_fr="Maroc et Tunisie",
        crumb_es="Marruecos y Túnez",
        h1_zh="摩洛哥与突尼斯服装标签合规：阿拉伯语、法语与欧盟 GPSR 要求",
        h1_en="Morocco and Tunisia Clothing Labels: Arabic, French and EU GPSR",
        h1_ja="モロッコ・チュニジアの衣料ラベル：アラビア語・フランス語と EU GPSR",
        h1_ko="모로코·튀니지 의류 라벨: 아랍어·프랑스어와 EU GPSR",
        h1_fr="Étiquetage au Maroc et en Tunisie : arabe, français et GPSR européen",
        h1_es="Etiquetado en Marruecos y Túnez: árabe, francés y GPSR europeo",
        tag_zh="合规与出口", tag_en="Compliance &amp; Export", tag_ja="コンプライアンス・輸出",
        tag_ko="컴플라이언스·수출", tag_fr="Conformité et export", tag_es="Cumplimiento y exportación",
        sum_zh="摩洛哥、突尼斯是欧盟近岸车间，标签却常被两套要求夹住：当地要阿拉伯语，欧盟要 1007/2011 的成分与 GPSR 的欧盟责任人。这篇讲清阿语在织唛与洗标上能做到多小、右到左怎么排、三国要求对照，以及三个最容易被零售拒收的错误。",
        sum_en="Morocco and Tunisia are Europe's nearshore rooms, and labels get caught between two demands: Arabic locally, 1007/2011 fibre names and a GPSR responsible person for the EU. How small Arabic can go on woven and care labels, right-to-left layout, a three-column comparison and three rejection triggers.",
        sum_ja="モロッコとチュニジアは欧州のニアショア縫製拠点。ラベルは現地のアラビア語と、EU 向けの 1007/2011・GPSR 域内責任者の間で挟まれます。織りラベルと洗濯表示で実現できるアラビア語の最小字高、右から左の版面、3要件の対照、小売で拒否されやすい三つの誤りを整理します。",
        sum_ko="모로코와 튀니지는 유럽의 니어쇼어 봉제 기지로, 라벨은 현지 아랍어와 EU용 1007/2011·GPSR 역내 책임자 사이에서 갈등합니다. 직조 라벨과 세탁 표시에서 가능한 아랍어 최소 글자 높이, 오른쪽에서 왼쪽 레이아웃, 세 요건 대조, 소매에서 반려되기 쉬운 세 가지 실수를 정리합니다.",
        sum_fr="Maroc et Tunisie, ateliers de proximité de l'Europe, où l'étiquette est prise entre deux exigences : l'arabe local, et pour l'UE les noms 1007/2011 et un responsable GPSR. Corps minimal en tissé, mise en page de droite à gauche, comparaison et trois motifs de refus.",
        sum_es="Marruecos y Túnez, talleres de proximidad de Europa, con la etiqueta entre dos exigencias: árabe local y, para la UE, los nombres del 1007/2011 y un responsable GPSR. Cuerpo mínimo en tejido, maquetación de derecha a izquierda, comparativa y tres motivos de rechazo.",
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
    print("  %-46s desc_zh=%d字 desc_en=%d字符 desc_ja=%d desc_ko=%d desc_fr=%d desc_es=%d"
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
