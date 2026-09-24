#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-09-24 早间 每日更新：2 篇新文章（六语：zh-Hant 根 / en / ja / ko / fr / es）
- 婚纱与晚礼服辅料指南：缎面主唛、烫金吊牌与礼盒包装
- 瑞士服装标签合规指南：成分、语言与责任方要求
（主题池 30 个选题均已上线，本次为品类/市场扩展新选题，不与既有文章重复）

用法: python daily_gen_20260924_am.py
"""
import os, re, sys, subprocess, importlib.util

ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)
PY = sys.executable

SKEL = "blog/knitwear-sweater-trims-guide.html"
DATE_ZH = "2026年9月24日"
DATE_EN = "September 24, 2026"
DATE_JA = "2026年9月24日更新"
DATE_KO = "2026년 9월 24일 업데이트"
DATE_FR = "24 septembre 2026"
DATE_ES = "24 de septiembre de 2026"
SITEMAP_DATE = "2026-09-24"
BUST_OLD, BUST_NEW = "104", "105"
LANGS = ["en", "ja", "ko", "fr", "es"]

ARTICLES = [
    dict(
        slug="bridal-eveningwear-trims-guide.html",
        body="blog/_body_bridal.html",
        title_zh="婚纱与晚礼服辅料指南：缎面主唛、烫金吊牌与礼盒包装 | TAGE",
        title_en="Bridal and Eveningwear Trims Guide: Satin Labels, Foil Tags, Gift Boxes | TAGE",
        title_ja="ウェディング・イブニングドレスの副資材ガイド：サテン主ラベル・箔押しタグ・ギフトボックス | TAGE",
        title_ko="웨딩·이브닝웨어 부자재 가이드: 새틴 주 라벨, 금박 행택, 선물 상자 | TAGE",
        title_fr="Guide des accessoires de mariée et de soirée : labels satin, tags dorés, coffrets | TAGE",
        title_es="Guía de accesorios nupciales y de fiesta: etiquetas de satén, colgantes dorados, cajas | TAGE",
        desc_zh="婚纱与晚礼服辅料定制指南：讲清缎面主唛怎么选、干洗与珠片款洗水标怎么写、烫金吊牌与缎带吊粒怎么配、礼盒与防尘袋如何防黄变，附询价规格表与七项核对清单。来自东莞泰阁包装。",
        desc_en="Bridal and eveningwear trims guide: how to choose satin neck labels, care labels for dry-clean-only and beaded styles, foil tags, ribbon hardware and gift boxes.",
        desc_ja="ウェディング・イブニングドレスの副資材ガイド。サテン主ラベルの選び方、ドライ専用やビーズ仕様の洗濯表示、箔押しタグとリボン、ギフトボックスと黄変防止、仕様表と7項目チェックを解説します。東莞泰閣包装。",
        desc_ko="웨딩·이브닝웨어 부자재 가이드. 새틴 주 라벨 선택, 드라이 전용·비즈 사양의 세탁 표시, 금박 행택과 리본, 선물 상자와 황변 방지, 사양표와 7가지 체크를 정리했습니다. 둥관 TAGE 패키징.",
        desc_fr="Guide accessoires mariée et soirée : choix du label satin, entretien pour le sec et les modèles perlés, tags dorés, rubans et attaches, coffrets et anti-jaunissement.",
        desc_es="Guía de accesorios nupciales y de fiesta: elección de etiqueta de satén, cuidado para seco y pedrería, colgantes dorados, cintas y cierres, cajas y antiamarilleo.",
        crumb_zh="婚纱礼服辅料", crumb_en="Bridal Trims", crumb_ja="ウェディング副資材",
        crumb_ko="웨딩웨어 부자재", crumb_fr="Accessoires mariée", crumb_es="Accesorios nupciales",
        h1_zh="婚纱与晚礼服辅料指南：缎面主唛、烫金吊牌与礼盒包装",
        h1_en="Bridal and Eveningwear Trims Guide: Satin Labels, Foil Tags and Gift Boxes",
        h1_ja="ウェディング・イブニングドレスの副資材ガイド：サテン主ラベル・箔押しタグ・ギフトボックス",
        h1_ko="웨딩·이브닝웨어 부자재 가이드: 새틴 주 라벨, 금박 행택, 선물 상자",
        h1_fr="Guide des accessoires de mariée et de soirée : labels satin, tags dorés et coffrets",
        h1_es="Guía de accesorios nupciales y de fiesta: etiquetas de satén, colgantes dorados y cajas",
        tag_zh="婚纱礼服", tag_en="Bridal", tag_ja="ウェディング", tag_ko="웨딩웨어",
        tag_fr="Mariée et soirée", tag_es="Nupcial y fiesta",
        sum_zh="婚纱与晚礼服的单件价值最高、批量最小、对面料最挑。本文讲清缎面、平纹、提花与无感内标在真丝和蕾丝上怎么选，干洗符号与珠片款的洗水标怎么写，烫金吊牌、缎带与金属吊粒怎么配，礼盒与防尘袋如何防黄变，以及限用物质与镍释出的注意点，并附可直接询价的七项规格表。",
        sum_en="Bridal and eveningwear carry the highest unit value, the smallest runs and the least tolerance for the wrong label. This guide covers choosing satin, plain, jacquard or tagless neck labels for silk and lace, wording care labels for dry-clean-only and beaded styles, pairing foil tags with ribbon and metal fasteners, keeping gift boxes and dust bags from yellowing, and the restricted-substance and nickel-release points to watch — plus a seven-line specification table you can quote from.",
        sum_ja="ウェディングとイブニングは単価が最も高く、ロットが最も小さく、生地への要求が最も厳しい分野です。本記事はシルクやレースに対するサテン・平織り・ジャカード・無感ラベルの選び方、ドライ専用やビーズ仕様の洗濯表示の書き方、箔押しタグとリボン・金属止め具の組み合わせ、ギフトボックスと保存袋の黄変防止、規制物質とニッケル溶出の注意点、そしてそのまま見積りに使える7項目の仕様表をまとめます。",
        sum_ko="웨딩과 이브닝웨어는 단가가 가장 높고 로트가 가장 작으며 원단에 대한 요구가 가장 까다롭습니다. 이 글은 실크와 레이스에 맞는 새틴·평직·자카드·무감 라벨 선택, 드라이 전용과 비즈 사양의 세탁 표시 문구, 금박 행택과 리본·금속 고정구 조합, 선물 상자와 방진백의 황변 방지, 규제 물질과 니켈 용출 주의점, 그리고 바로 견적에 쓸 수 있는 7항목 사양표를 정리합니다.",
        sum_fr="La tenue de mariée et de soirée cumule la plus forte valeur unitaire, les plus petites séries et la plus faible tolérance à un label inadapté. Ce guide traite le choix des labels satin, toile plate, jacquard ou sans couture pour la soie et la dentelle, la rédaction du label d'entretien pour le sec et les modèles perlés, l'accord entre tag doré, ruban et attaches métalliques, la prévention du jaunissement des coffrets et housses, les substances restreintes et la libération de nickel, avec un tableau de spécifications en sept lignes.",
        sum_es="La moda nupcial y de fiesta reúne el mayor valor unitario, las series más cortas y la menor tolerancia a una etiqueta inadecuada. Esta guía trata la elección de etiquetas de satén, tafetán, jacquard o sin costura para seda y encaje, la redacción del cuidado para seco y pedrería, la combinación de colgante dorado con cinta y cierres metálicos, cómo evitar el amarilleo de cajas y fundas, las sustancias restringidas y la liberación de níquel, con una tabla de especificaciones de siete líneas.",
    ),
    dict(
        slug="clothing-label-compliance-switzerland.html",
        body="blog/_body_swiss.html",
        title_zh="瑞士服装标签合规指南：成分、语言与责任方要求 | TAGE",
        title_en="Switzerland Clothing Label Requirements: Fibre Content, Language and Responsible Party | TAGE",
        title_ja="スイスの衣料ラベル要件：繊維組成・言語・責任者 | TAGE",
        title_ko="스위스 의류 라벨 요건: 섬유 조성·언어·책임자 | TAGE",
        title_fr="Étiquetage des vêtements en Suisse : fibres, langues et responsable | TAGE",
        title_es="Etiquetado de ropa en Suiza: fibras, idiomas y responsable | TAGE",
        desc_zh="瑞士服装标签合规指南：瑞士不属于欧盟，本文讲清纤维成分与德法意三种语言怎么写、护理符号与洗涤说明口径、进口商责任方与瑞士地址如何留位、GS1 760 条码与原产地标注，以及限用物质与儿童绳带要求，附打样前六项核对清单。来自东莞泰阁包装。",
        desc_en="Switzerland clothing label rules: Swiss fibre labelling compared with the EU, German and French wording, care symbols, the importer as responsible party, GS1 760 barcodes.",
        desc_ja="スイスの衣料ラベル要件。EU との違い、繊維組成と独仏伊の言語表記、洗濯記号、輸入者の責任者表示とスイス住所、GS1 760 バーコード、規制物質と子供服の紐の要件を整理します。東莞泰閣包装。",
        desc_ko="스위스 의류 라벨 요건. EU와의 차이, 섬유 조성과 독일어·프랑스어·이탈리아어 표기, 세탁 기호, 수입업체 책임자 표시와 스위스 주소, GS1 760 바코드, 규제 물질과 아동복 끈 요건을 정리했습니다. 둥관 TAGE 패키징.",
        desc_fr="Étiquetage textile en Suisse : différences avec l'UE, composition et langues allemand-français-italien, symboles d'entretien, importateur responsable et code-barres GS1 760.",
        desc_es="Etiquetado textil en Suiza: diferencias con la UE, composición y idiomas alemán-francés-italiano, símbolos de cuidado, importador responsable y códigos GS1 760.",
        crumb_zh="瑞士标签合规", crumb_en="Switzerland Label Rules", crumb_ja="スイスのラベル要件",
        crumb_ko="스위스 라벨 요건", crumb_fr="Étiquetage en Suisse", crumb_es="Etiquetado en Suiza",
        h1_zh="瑞士服装标签合规指南：成分、语言与责任方要求",
        h1_en="Switzerland Clothing Label Requirements: Fibre Content, Language and Responsible Party",
        h1_ja="スイスの衣料ラベル要件：繊維組成・言語・責任者",
        h1_ko="스위스 의류 라벨 요건: 섬유 조성·언어·책임자",
        h1_fr="Étiquetage des vêtements en Suisse : fibres, langues et responsable",
        h1_es="Etiquetado de ropa en Suiza: fibras, idiomas y responsable",
        tag_zh="合规指南", tag_en="Compliance", tag_ja="コンプライアンス", tag_ko="컴플라이언스",
        tag_fr="Conformité", tag_es="Cumplimiento",
        sum_zh="瑞士常被误以为「欧盟标签直接能用」。本文讲清瑞士的适用规则范围、纤维成分与±3% 公差口径、德法意三种官方语言怎么排（瑞士德语不写 ß）、护理说明与 ISO 3758 符号的实际要求、进口商作为责任方如何留位、GS1 760 条码与原产地标注、海关与报价术语，以及限用物质与儿童绳带两块抽查重点，附打样前六项核对清单。",
        sum_en="Switzerland is often assumed to accept an EU label as it stands. This guide sets out which rules actually apply, fibre content with the roughly three-point tolerance, how to lay out the three official languages (no ß in Swiss German), what care information and ISO 3758 symbols are really required, how the importer takes the responsible-party role, GS1 760 barcodes and origin marking, customs and price terms, and the restricted-substance and childrenswear cord points inspections focus on — with six checks before sampling.",
        sum_ja="スイスは「EU のラベルがそのまま通る」と誤解されがちです。本記事は適用されるルールの範囲、繊維組成と約3ポイントの許容差、公用語3言語の組み方（スイスドイツ語は ß を使わない）、洗濯情報と ISO 3758 記号の実務要件、輸入者の責任者表示、GS1 760 バーコードと原産地表示、通関と見積り条件、そして検査で重視される規制物質と子供服の紐の要件を整理し、サンプル前の6項目チェックを掲載します。",
        sum_ko="스위스는 'EU 라벨이 그대로 통한다'고 오해되곤 합니다. 이 글은 실제 적용 규칙의 범위, 섬유 조성과 약 3%p 허용 오차, 공용어 세 가지 배열(스위스 독일어는 ß를 쓰지 않음), 세탁 정보와 ISO 3758 기호의 실무 요건, 수입업체의 책임자 표시, GS1 760 바코드와 원산지 표기, 통관과 견적 조건, 그리고 검사에서 중시하는 규제 물질과 아동복 끈 요건을 정리하고 샘플 전 6가지 체크를 제공합니다.",
        sum_fr="On croit souvent qu'une étiquette UE suffit pour la Suisse. Ce guide précise les règles réellement applicables, la composition avec une tolérance d'environ trois points, la mise en page des trois langues officielles (pas de ß en Suisse), les exigences réelles d'entretien et les symboles ISO 3758, le rôle de responsable porté par l'importateur, les codes-barres GS1 760 et le marquage d'origine, la douane et les conditions de prix, ainsi que les substances restreintes et les cordons enfant, avec six contrôles avant échantillon.",
        sum_es="A menudo se supone que una etiqueta de la UE sirve tal cual para Suiza. Esta guía precisa qué normas aplican de verdad, la composición con una tolerancia de unos tres puntos, cómo maquetar las tres lenguas oficiales (sin ß en Suiza), los requisitos reales de cuidado y los símbolos ISO 3758, el papel de responsable del importador, los códigos GS1 760 y el marcado de origen, aduana y condiciones de precio, y los puntos de sustancias restringidas y cordones infantiles, con seis comprobaciones antes de muestrear.",
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

# ---------------- desc 长度体检 ----------------
for a in ARTICLES:
    print("  %-38s desc_zh=%d字 desc_en=%d字符 desc_ja=%d desc_ko=%d desc_fr=%d desc_es=%d"
          % (a["slug"], len(a["desc_zh"]), len(a["desc_en"]), len(a["desc_ja"]),
             len(a["desc_ko"]), len(a["desc_fr"]), len(a["desc_es"])))

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
