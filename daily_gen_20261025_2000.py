#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-25 20:00 批次每日更新生成脚本（六语：zh-Hant 根 / en / ja / ko / fr / es）
- 球衣与运动队服辅料（sports-team-jersey-trims-guide）
- 服装租赁与共享衣橱标签（garment-rental-label-guide）

用法: F:/hermes/venvs/tools/Scripts/python.exe daily_gen_20261025_2000.py
"""
import os, re, sys, subprocess, importlib.util

ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)
PY = sys.executable

SKEL = "blog/knitwear-sweater-trims-guide.html"
DATE_ZH = "2026年10月25日"
DATE_EN = "October 25, 2026"
DATE_JA = "2026年10月25日更新"
DATE_KO = "2026년 10월 25일 업데이트"
DATE_FR = "25 octobre 2026"
DATE_ES = "25 de octubre de 2026"
SITEMAP_DATE = "2026-10-25"
BUST_OLD, BUST_NEW = "181", "182"
LANGS = ["en", "ja", "ko", "fr", "es"]

ARTICLES = [
    dict(
        slug="sports-team-jersey-trims-guide.html",
        body="blog/_body_jersey.html",
        title_zh="球衣与队服辅料指南：号码工艺、领标与洗水标怎么选 | TAGE",
        title_en="Sports Jersey and Team Kit Trims: Numbers, Neck and Care Labels | TAGE",
        title_ja="ユニフォーム・スポーツジャージの副資材：番号工程・ネーム・洗濯表示の選び方 | TAGE",
        title_ko="유니폼·스포츠 저지 부자재: 번호 공정·넥 라벨·케어 라벨 선택 | TAGE",
        title_fr="Accessoires de maillots et tenues d'équipe : numéros, étiquettes et entretien | TAGE",
        title_es="Accesorios para camisetas y equipaciones: números, etiquetas y cuidado | TAGE",
        desc_zh="球衣与队服辅料指南：领标、洗水标与号码姓名三类标识的材料与工艺，热转印、刺绣、硅胶怎么选，耐洗与耐氯测试按什么口径做，以及领标扎颈、号码开裂等五个常见翻车点。来自东莞泰阁包装。",
        desc_en="Sports jersey trims for team kits: neck labels, care labels and numbers, choosing heat transfer, embroidery or silicone, plus wash and chlorine test criteria.",
        desc_ja="ユニフォームの副資材ガイド。ネーム・洗濯表示・背番号の素材と工程、熱転写・刺繍・シリコーンの選び分け、耐洗・耐塩素試験の基準、よくある5つの失敗を解説します。東莞泰閣包装。",
        desc_ko="유니폼 부자재 가이드. 넥 라벨·케어 라벨·등번호의 소재와 공정, 열전사·자수·실리콘 선택, 내세탁·내염소 시험 기준, 흔한 다섯 가지 실패를 정리했습니다. 둥관 TAGE 패키징.",
        desc_fr="Accessoires de maillots : étiquettes de nuque, d'entretien et numéros, choix entre transfert, broderie et silicone, tests de lavage et de chlore.",
        desc_es="Accesorios de camisetas: etiquetas de cuello, de cuidado y números, elección entre transfer, bordado y silicona, ensayos de lavado y cloro.",
        crumb_zh="球衣与队服辅料",
        crumb_en="Jersey and Kit Trims",
        crumb_ja="ユニフォーム副資材",
        crumb_ko="유니폼 부자재",
        crumb_fr="Accessoires de maillots",
        crumb_es="Accesorios de equipaciones",
        h1_zh="球衣与队服辅料指南：号码工艺、领标与洗水标怎么选",
        h1_en="Sports Jersey and Team Kit Trims: Numbers, Neck Labels and Care Labels",
        h1_ja="ユニフォーム・スポーツジャージの副資材：番号工程・ネーム・洗濯表示の選び方",
        h1_ko="유니폼·스포츠 저지 부자재: 번호 공정·넥 라벨·케어 라벨 선택",
        h1_fr="Accessoires de maillots et tenues d'équipe : numéros, étiquettes et entretien",
        h1_es="Accesorios para camisetas y equipaciones: números, etiquetas y cuidado",
        tag_zh="运动服装", tag_en="Sportswear", tag_ja="スポーツウェア", tag_ko="스포츠웨어",
        tag_fr="Sportswear", tag_es="Ropa deportiva",
        sum_zh="球衣是辅料要求最苛刻的一类：一件比赛服一个赛季洗几十次，还要承受汗液、氯水、摩擦与拉伸。本文拆解球衣上的三类标识——领标、洗水标、号码与姓名，讲清热转印膜与面料的匹配、刺绣与硅胶的适用边界、按 ISO 6330 与 AATCC 135 做 30 次与 50 次洗涤测试的口径、耐氯与人工汗的单独验证，以及领标扎颈、号码洗后开裂、赛事标位置错、洗水标做成一块板等五个高频翻车点，最后给一份可直接发给工厂的六项下单清单。",
        sum_en="A jersey is the harshest assignment in trims: one match shirt is washed dozens of times a season and still has to survive sweat, chlorine, abrasion and stretch. This guide breaks down the three markings — neck label, care label and numbers — explaining how transfer film must match the fabric, where embroidery and silicone stop making sense, how to run 30 and 50 cycle tests to ISO 6330 and AATCC 135, why chlorine and artificial perspiration need their own checks, and five high-frequency failures from a scratching neck label to numbers that crack after washing. It closes with a six-item spec list you can send straight to a factory.",
        sum_ja="ジャージは副資材の中で最も厳しい案件です。試合用シャツ1着はシーズンに何十回も洗われ、汗・塩素・摩擦・伸縮に耐えねばなりません。本稿はネーム・洗濯表示・背番号という3種類の表示を分解し、熱転写フィルムと生地の整合、刺繍とシリコーンの適用範囲、ISO 6330・AATCC 135 による30回・50回洗濯試験の基準、耐塩素と人工汗の個別検証、ネームの肌当たり・洗濯後の番号割れ・大会マークの位置ずれ・洗濯表示が板になるなどの頻出失敗5つ、工場にそのまま送れる6項目の発注仕様をまとめます。",
        sum_ko="저지는 부자재 가운데 가장 까다로운 과제입니다. 경기용 셔츠 한 벌은 시즌에 수십 번 세탁되며 땀·염소·마찰·신축을 견뎌야 합니다. 이 글은 넥 라벨·케어 라벨·등번호 세 가지 표시를 해부하고, 열전사 필름과 원단의 매칭, 자수와 실리콘의 적용 범위, ISO 6330·AATCC 135에 따른 30회·50회 세탁 시험 기준, 내염소와 인공 땀의 개별 검증, 넥 라벨 자극·세탁 후 번호 갈라짐·대회 마크 위치 오류·케어 라벨이 판처럼 되는 문제 등 빈발 실패 다섯 가지, 공장에 그대로 보낼 여섯 항목 발주 사양을 정리합니다.",
        sum_fr="Un maillot est le dossier le plus exigeant des accessoires : une chemise de match est lavée des dizaines de fois par saison et doit encore résister à la sueur, au chlore, à l'abrasion et à l'étirement. Ce guide décompose les trois marquages — étiquette de nuque, étiquette d'entretien, numéros — en expliquant l'accord film/tissu, les limites de la broderie et du silicone, la conduite des tests à 30 et 50 cycles selon ISO 6330 et AATCC 135, la nécessité de vérifier séparément chlore et sueur artificielle, et cinq défauts fréquents, de l'étiquette qui gratte aux numéros qui craquent. Il se termine par une fiche de six points à envoyer à l'usine.",
        sum_es="Una camiseta es el encargo más exigente en accesorios: una camiseta de partido se lava decenas de veces por temporada y debe resistir sudor, cloro, abrasión y estiramiento. Esta guía desglosa los tres marcados —etiqueta de cuello, de cuidado y números— y explica el ajuste entre film y tejido, dónde dejan de tener sentido el bordado y la silicona, cómo ejecutar ensayos de 30 y 50 ciclos según ISO 6330 y AATCC 135, por qué cloro y sudor artificial requieren verificación aparte, y cinco fallos frecuentes, desde la etiqueta que rasca hasta los números que se agrietan. Cierra con una ficha de seis puntos para enviar a fábrica.",
    ),
    dict(
        slug="garment-rental-label-guide.html",
        body="blog/_body_rental.html",
        title_zh="服装租赁标签方案：耐洗标识、可复用吊牌与追溯设计 | TAGE",
        title_en="Clothing Rental Labels: Durable Marking, Reusable Tags and Traceability | TAGE",
        title_ja="衣料レンタルのラベル設計：耐洗表示・再利用タグ・トレーサビリティ | TAGE",
        title_ko="의류 렌털 라벨 설계: 내세탁 표시·재사용 태그·추적성 | TAGE",
        title_fr="Étiquettes de location : marquage durable, étiquettes réutilisables, traçabilité | TAGE",
        title_es="Etiquetas para alquiler de ropa: marcado duradero, colgantes reutilizables y trazabilidad | TAGE",
        desc_zh="服装租赁与共享衣橱的标签指南：款号尺码识别、耐洗与耐氯材料、可复用硬吊牌与可擦写运营标，以及 RFID、二维码追溯与欧盟数字产品护照的落地做法。来自东莞泰阁包装。",
        desc_en="Clothing rental labels: style and size identification, wash-durable materials, reusable hang tags, and RFID or QR traceability that matches your asset system.",
        desc_ja="衣料レンタル・シェアワードローブのラベルガイド。型番とサイズの識別、耐洗素材、再利用硬質タグと書き換え可能な運用ラベル、RFID・QRによるトレーサビリティとEUデジタル製品パスポートへの備えを解説します。東莞泰閣包装。",
        desc_ko="의류 렌털·공유 옷장 라벨 가이드. 스타일과 사이즈 식별, 내세탁 소재, 재사용 경질 행택과 재기록 운영 라벨, RFID·QR 추적성과 EU 디지털 제품 여권 대비를 정리했습니다. 둥관 TAGE 패키징.",
        desc_fr="Étiquettes de location : identification référence et taille, matières résistantes au lavage, étiquettes réutilisables, traçabilité RFID ou QR.",
        desc_es="Etiquetas de alquiler: identificación de referencia y talla, materiales resistentes al lavado, colgantes reutilizables y trazabilidad RFID o QR.",
        crumb_zh="服装租赁标签",
        crumb_en="Rental Labelling",
        crumb_ja="レンタル衣料のラベル",
        crumb_ko="렌털 의류 라벨",
        crumb_fr="Étiquetage de location",
        crumb_es="Etiquetado de alquiler",
        h1_zh="服装租赁标签方案：耐洗标识、可复用吊牌与追溯设计",
        h1_en="Clothing Rental Labels: Durable Marking, Reusable Tags and Traceability",
        h1_ja="衣料レンタルのラベル設計：耐洗表示・再利用タグ・トレーサビリティ",
        h1_ko="의류 렌털 라벨 설계: 내세탁 표시·재사용 태그·추적성",
        h1_fr="Étiquettes de location : marquage durable, étiquettes réutilisables et traçabilité",
        h1_es="Etiquetas para alquiler de ropa: marcado duradero, colgantes reutilizables y trazabilidad",
        tag_zh="循环时尚", tag_en="Circular Fashion", tag_ja="サーキュラーファッション", tag_ko="순환 패션",
        tag_fr="Mode circulaire", tag_es="Moda circular",
        sum_zh="服装租赁与共享衣橱的标签逻辑和零售完全不同：一件衣服要经历几十次穿着、洗涤与归还，标签不能褪色磨破，款号与尺码必须让仓库一眼识别，品牌露出要能拆换而不影响下一次出租。本文拆解租赁标签的四项功能，给出礼服 5–15 次、通勤与童装订阅 30–50 次的循环目标与对应材料选择，讲清可复用硬吊牌、可擦写运营标与临时尺码贴的用法，以及 RFID 读取率、洗护符号与实际工艺一致、欧盟数字产品护照等追溯与合规要点，附三个常见坑。",
        sum_en="Rental and shared-wardrobe labelling obeys a different logic from retail: one garment goes through dozens of wear, wash and return cycles, labels must not fade or fray, style and size must be readable at a glance in the warehouse, and branding has to be swappable without spoiling the next rental. This guide sets out the four functions of a rental label, cycle targets of 5 to 15 wears for occasion wear and 30 to 50 for workwear or childrenswear subscriptions with matching materials, how reusable rigid tags, rewritable operational labels and temporary size stickers are used, and what matters on RFID read rates, care symbols that match the real process and the EU Digital Product Passport — plus three traps.",
        sum_ja="レンタルやシェアワードローブの表示は小売と論理が異なります。1着が何十回もの着用・洗濯・返却を経るため、ラベルは退色やほつれがなく、型番とサイズは倉庫で一目で判別でき、ブランド表示は次のレンタルを妨げず交換できる必要があります。本稿はレンタルラベルの4機能、礼服5〜15回・通勤服や子供服の定額制30〜50回という循環目標と素材選び、再利用硬質タグ・書き換え可能な運用ラベル・一時サイズシールの使い方、RFIDの読取率、洗濯絵表示と実工程の一致、EUデジタル製品パスポートなどの要点と3つの落とし穴を整理します。",
        sum_ko="렌털과 공유 옷장의 라벨 논리는 소매와 다릅니다. 한 벌이 수십 번의 착용·세탁·반납을 거치므로 라벨은 퇴색·마모가 없어야 하고, 스타일과 사이즈는 창고에서 즉시 식별되어야 하며, 브랜드 노출은 다음 대여에 지장 없이 교체 가능해야 합니다. 이 글은 렌털 라벨의 네 가지 기능, 예복 5~15회·출퇴근복과 아동복 구독 30~50회라는 순환 목표와 소재 선택, 재사용 경질 행택·재기록 운영 라벨·임시 사이즈 스티커의 활용, RFID 판독률, 세탁 기호와 실제 공정의 일치, EU 디지털 제품 여권 등 추적성과 법규 요점, 세 가지 함정을 정리합니다.",
        sum_fr="L'étiquetage locatif obéit à une autre logique que le détail : un vêtement enchaîne des dizaines de ports, lavages et retours, l'étiquette ne doit ni pâlir ni s'effilocher, la référence et la taille doivent être lisibles d'un coup d'œil en entrepôt, et la marque doit être échangeable sans gêner la location suivante. Ce guide expose les quatre fonctions d'une étiquette de location, des cibles de 5 à 15 ports pour la cérémonie et de 30 à 50 pour le prêt-à-travailler ou l'abonnement enfant avec les matériaux correspondants, l'usage des étiquettes rigides réutilisables, des marquages réinscriptibles et des stickers de taille temporaires, puis les taux de lecture RFID, la cohérence des symboles avec le process réel et le passeport numérique européen — avec trois pièges.",
        sum_es="El etiquetado de alquiler obedece a otra lógica que el retail: una prenda encadena decenas de usos, lavados y devoluciones, la etiqueta no debe decolorarse ni deshilacharse, la referencia y la talla deben leerse de un vistazo en el almacén, y la marca tiene que poder cambiarse sin arruinar el siguiente alquiler. Esta guía expone las cuatro funciones de la etiqueta de alquiler, objetivos de 5 a 15 usos para ocasión y de 30 a 50 para prêt-à-travailler o suscripción infantil con los materiales correspondientes, el uso de colgantes rígidos reutilizables, marcados reescribibles y pegatinas temporales de talla, y qué importa en tasas de lectura RFID, símbolos coherentes con el proceso real y el pasaporte digital europeo, con tres trampas.",
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
