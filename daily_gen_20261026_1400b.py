#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-26 14:00 批次每日更新生成脚本（六语：zh-Hant 根 / en / ja / ko / fr / es）
- 服装包装洁净度与异物控制（garment-packaging-cleanliness-contamination-control）
- 服装包装成本结构与预算分配（garment-packaging-budget-allocation）

用法: F:/hermes/venvs/tools/Scripts/python.exe daily_gen_20261026_1400b.py [--check]
"""
import os, re, sys, subprocess, importlib.util

ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)
PY = sys.executable

SKEL = "blog/knitwear-sweater-trims-guide.html"
DATE_ZH = "2026年10月26日"
DATE_EN = "October 26, 2026"
DATE_JA = "2026年10月26日更新"
DATE_KO = "2026년 10월 26일 업데이트"
DATE_FR = "26 octobre 2026"
DATE_ES = "26 de octubre de 2026"
SITEMAP_DATE = "2026-10-26"
BUST_OLD, BUST_NEW = "183", "184"
LANGS = ["en", "ja", "ko", "fr", "es"]

ARTICLES = [
    dict(
        slug="garment-packaging-cleanliness-contamination-control.html",
        body="blog/_body_cleanpack.html",
        title_zh="服装包装洁净度与异物控制指南：绒毛、硬物与毛发怎么管 | TAGE",
        title_en="Garment Packaging Cleanliness: Fibre, Hard Objects and Hair | TAGE",
        title_ja="衣料品包装の清浄度と異物管理：繊維くず・硬質物・毛髪 | TAGE",
        title_ko="의류 포장 청결도와 이물 관리: 섬유 부스러기·경질물·머리카락 | TAGE",
        title_fr="Propreté de l'emballage textile : fibres, objets durs et cheveux | TAGE",
        title_es="Limpieza del embalaje textil: fibras, objetos duros y pelos | TAGE",
        desc_zh="服装包装洁净度指南：纤维绒毛、硬物与毛发三类污染分别怎么控制，包装材料自身带出的纸屑与粉尘怎么排查，什么订单要什么等级的车间，灯检、粘尘辊、AQL 抽检与验针机四种手段怎么组合，附规格书四条验收约定。来自东莞泰阁包装。",
        desc_en="Garment packaging cleanliness: controlling fibre dust, hard objects and hair, cutting contamination from packaging material and four detection methods.",
        desc_ja="衣料品包装の清浄度ガイド。繊維くず・硬質物・毛髪の3種類の汚染対策、包装資材由来の紙粉の見つけ方、注文別の作業環境等級、ライト検品・粘着ローラー・AQL抜取・検針機の組み合わせ、仕様書に書く4つの検収条件を解説します。東莞泰閣包装。",
        desc_ko="의류 포장 청결도 가이드. 섬유 부스러기·경질 이물·머리카락 세 가지 오염 대응, 포장 자재에서 나오는 종이 가루 점검, 주문별 작업 구역 등급, 조명 검사·점착 롤러·AQL 샘플링·검침기 조합, 사양서에 적을 네 가지 검수 조건을 정리했습니다. 둥관 TAGE 패키징.",
        desc_fr="Propreté de l'emballage textile : maîtriser fibres, objets durs et cheveux, couper la contamination venue de l'emballage, quatre méthodes de détection.",
        desc_es="Limpieza del embalaje textil: controlar fibras, objetos duros y pelos, cortar la contaminación del propio embalaje y aplicar cuatro métodos de detección.",
        crumb_zh="包装洁净度与异物控制",
        crumb_en="Packaging Cleanliness",
        crumb_ja="包装の清浄度と異物",
        crumb_ko="포장 청결도와 이물",
        crumb_fr="Propreté de l'emballage",
        crumb_es="Limpieza del embalaje",
        h1_zh="服装包装洁净度与异物控制指南：绒毛、硬物与毛发怎么管",
        h1_en="Garment Packaging Cleanliness: Controlling Fibre, Hard Objects and Hair",
        h1_ja="衣料品包装の清浄度と異物管理：繊維くず・硬質物・毛髪の対策",
        h1_ko="의류 포장 청결도와 이물 관리: 섬유 부스러기·경질물·머리카락",
        h1_fr="Propreté de l'emballage textile : fibres, objets durs et cheveux",
        h1_es="Limpieza del embalaje textil: fibras, objetos duros y pelos",
        tag_zh="包装品质", tag_en="Packaging Quality", tag_ja="包装品質", tag_ko="포장 품질",
        tag_fr="Qualité d'emballage", tag_es="Calidad de embalaje",
        sum_zh="客户开箱抽检，在成衣上发现一根毛发或一层纤维绒，整箱就被判不合格——异物投诉最麻烦的地方是它不可量化。本文把污染源拆成纤维绒毛、硬物与油污三类，讲清包装材料本身（模切纸屑、编织袋短纤维、再生料袋内粉尘、破损干燥剂）怎么会成为污染源，按客户要求把车间分三档，给出灯检、粘尘辊、AQL 抽检与验针机四种能落地的检出手段，并说清封口、装箱与仓储的二次污染怎么切断，最后给四条可直接写进规格书的验收约定。",
        sum_en="A buyer opens a carton, finds a hair or a bloom of fibre dust, and rejects the lot — foreign-matter complaints are awkward because they are not measurable. This guide splits contamination into fibre, hard objects and oil marks, shows how packaging material itself (die-cutting chips, sack fibres, dust in recycled bags, a broken desiccant) becomes the source, sets three work-area tiers by order type, and details four practical detection methods — light inspection, tack rollers, AQL sampling and needle detection — plus how to cut secondary contamination at sealing and storage, closing with four acceptance terms you can paste into a spec sheet.",
        sum_ja="バイヤーが箱を開け、衣料に髪の毛一本や繊維くずを見つけてロット不合格——異物クレームの厄介さは数値化できない点にあります。本稿は汚染源を繊維くず・硬質物・油汚れの3つに分け、包装資材そのもの（抜き紙粉、織り袋の短繊維、再生袋の粉塵、破れた乾燥剤）が汚染源になる経路、注文に応じた作業環境の3等級、ライト検品・粘着ローラー・AQL抜取・検針機という実行可能な4つの検出方法、封口・梱包・保管での二次汚染の断ち方、仕様書にそのまま書ける4つの検収条件までを整理します。",
        sum_ko="바이어가 상자를 열어 의류에서 머리카락 한 올이나 섬유 부스러기를 발견하면 로트가 불합격됩니다. 이물 클레임이 까다로운 이유는 수치화가 안 된다는 점입니다. 이 글은 오염원을 섬유 부스러기·경질물·기름때로 나누고, 포장 자재 자체(타발 종이 가루, 직조 자루 섬유, 재생 비닐 먼지, 파손된 제습제)가 오염원이 되는 경로, 주문별 작업 구역 세 등급, 조명 검사·점착 롤러·AQL 샘플링·검침기 네 가지 실행 가능한 검출 방법, 봉함·포장·보관의 2차 오염 차단, 사양서에 그대로 쓸 수 있는 네 가지 검수 조건을 정리합니다.",
        sum_fr="L'acheteur ouvre le carton, trouve un cheveu ou un voile de fibres, et refuse le lot : une réclamation pour corps étranger est délicate parce qu'elle n'est pas mesurable. Ce guide répartit la pollution en fibres, objets durs et traces d'huile, montre comment l'emballage lui-même (copeaux de découpe, fibres de sacs tissés, poussière des sachets recyclés, dessiccant percé) en devient la source, fixe trois niveaux d'atelier selon la commande et détaille quatre méthodes de détection applicables — contrôle sous lumière, rouleaux adhésifs, échantillonnage AQL et détection d'aiguilles — puis la contamination secondaire au scellage et au stockage, avec quatre conditions de réception à recopier au cahier des charges.",
        sum_es="El comprador abre el cartón, encuentra un pelo o una capa de fibras y rechaza el lote: una reclamación por cuerpo extraño es delicada porque no es medible. Esta guía reparte la contaminación en fibras, objetos duros y manchas de aceite, explica cómo el propio embalaje (restos de troquelado, fibras de sacos tejidos, polvo de bolsas recicladas, desecante roto) se convierte en la fuente, fija tres niveles de área según el pedido y detalla cuatro métodos aplicables —inspección con luz, rodillos adhesivos, muestreo AQL y detección de agujas—, además de la contaminación secundaria en sellado y almacén, cerrando con cuatro condiciones de recepción para la ficha técnica.",
    ),
    dict(
        slug="garment-packaging-budget-allocation.html",
        body="blog/_body_packbudget.html",
        title_zh="服装包装成本结构与预算分配：六项物料怎么算 | TAGE",
        title_en="Garment Packaging Cost Structure and Budget Allocation | TAGE",
        title_ja="衣料品包装のコスト構造と予算配分：6つの資材の考え方 | TAGE",
        title_ko="의류 포장 원가 구조와 예산 배분: 여섯 자재 계산법 | TAGE",
        title_fr="Structure de coût et budget d'emballage textile : six postes | TAGE",
        title_es="Estructura de coste y presupuesto del embalaje textil | TAGE",
        desc_zh="服装包装成本结构怎么算：吊牌、主唛与洗水标、内袋、纸袋、辅材、打样物流六项物料的成本驱动因素，一次性版费与变动成本怎么分开，按零售价格带定预算比例，报价口径五个必查字段，以及什么时候该把预算从吊牌转到包装袋。来自东莞泰阁包装。",
        desc_en="Garment packaging cost structure: what drives hang tag, label, bag and paper bag prices, one-off tooling vs variable cost, and budget ratios by price band.",
        desc_ja="衣料品包装のコスト構造：タグ・主表示と洗濯表示・内袋・紙袋・付属資材・サンプル物流の6項目のコスト要因、一時費用と変動費の分け方、小売価格帯別の予算比率、見積条件の確認5項目、予算をタグから袋へ移す判断基準を解説します。東莞泰閣包装。",
        desc_ko="의류 포장 원가 구조: 행택·주라벨과 케어 라벨·내포장 비닐·종이백·부자재·샘플 물류 여섯 항목의 원가 요인, 일회성 판비와 변동비 분리, 소매 가격대별 예산 비율, 견적 기준 다섯 항목, 예산을 행택에서 비닐로 옮기는 판단 기준을 정리했습니다. 둥관 TAGE 패키징.",
        desc_fr="Structure de coût de l'emballage textile : facteurs de prix des étiquettes, labels, sachets et sacs papier, outillage vs variable, ratios par gamme.",
        desc_es="Estructura de coste del embalaje textil: factores de precio de etiquetas, labels, bolsas y sacos, utillaje frente a coste variable y ratios por gama.",
        crumb_zh="包装成本与预算",
        crumb_en="Packaging Cost & Budget",
        crumb_ja="包装コストと予算",
        crumb_ko="포장 원가와 예산",
        crumb_fr="Coût et budget d'emballage",
        crumb_es="Coste y presupuesto",
        h1_zh="服装包装成本结构与预算分配：六项物料怎么算",
        h1_en="Garment Packaging Cost Structure and Budget Allocation",
        h1_ja="衣料品包装のコスト構造と予算配分：6つの資材の考え方",
        h1_ko="의류 포장 원가 구조와 예산 배분: 여섯 자재 계산법",
        h1_fr="Structure de coût et budget d'emballage textile : six postes à maîtriser",
        h1_es="Estructura de coste y presupuesto del embalaje textil: seis partidas",
        tag_zh="成本管控", tag_en="Cost Control", tag_ja="コスト管理", tag_ko="원가 관리",
        tag_fr="Maîtrise des coûts", tag_es="Control de costes",
        sum_zh="多数品牌分头询价：吊牌一家、袋子一家、纸袋再一家，各自砍几个点，却从没算过包装总额占零售价多少、版费摊在多少件上。本文把包装拆成六项物料，逐项列出成本驱动因素与一次性投入，按大众、中端、轻奢三个价格带给出预算分配思路，讲清为什么版费与变动成本必须分开算（同额版费在三千件与三万件上单价差十倍），列出报价口径五个必查字段，并说明吊牌与包装袋之间该在什么阶段转移预算。",
        sum_en="Most brands quote piece by piece — tags from one supplier, bags from another — squeeze a few points off each, and never work out what packaging costs as a share of retail or how tooling amortises. This guide breaks packaging into six material groups with their cost drivers and one-off investment, gives allocation logic for mass, mid-market and premium price bands, explains why tooling must sit apart from variable cost (the same plate charge differs tenfold per unit between 3,000 and 30,000 pieces), lists five fields that must match before comparing quotes, and shows when to shift budget from hang tags to bags.",
        sum_ja="多くのブランドはタグをA社、袋をB社と個別に見積り、それぞれ数ポイントを削るだけで、小売価格に占める包装総額や版代の償却を計算していません。本稿は包装を6つの資材に分け、コスト要因と一時費用を整理し、量販・中価格帯・高価格帯の3つの価格帯別に予算配分の考え方を示します。版代と変動費を分けるべき理由（同額の版代でも3,000枚と30,000枚で単価が10倍違う）、見積条件で必ず揃える5項目、タグと袋の間で予算を移すタイミングまで解説します。",
        sum_ko="대부분의 브랜드는 행택은 A사, 비닐은 B사에서 따로 견적을 받아 각각 몇 프로씩 깎을 뿐, 소매가 대비 포장 총액이나 판비 상각을 계산하지 않습니다. 이 글은 포장을 여섯 자재로 나눠 원가 요인과 일회성 투자를 정리하고, 대중·중가·프리미엄 세 가격대별 예산 배분 논리를 제시합니다. 판비와 변동비를 분리해야 하는 이유(같은 판비라도 3,000개와 30,000개에서 개당 열 배 차이), 견적 비교 전 반드시 맞출 다섯 항목, 행택과 비닐 사이에서 예산을 옮기는 시점까지 다룹니다.",
        sum_fr="La plupart des marques demandent des prix séparément — étiquettes chez l'un, sachets chez l'autre — grattent quelques points sur chacun, sans jamais calculer le poids de l'emballage dans le prix de vente ni l'amortissement de l'outillage. Ce guide décompose l'emballage en six familles avec leurs facteurs de coût et leur investissement ponctuel, propose une logique de répartition pour trois tranches de prix, explique pourquoi l'outillage doit être isolé du variable (la même gravure diffère d'un facteur dix entre 3 000 et 30 000 pièces), liste cinq champs à aligner avant de comparer des devis et indique quand déplacer le budget des étiquettes vers les sachets.",
        sum_es="La mayoría de marcas piden precios por separado —etiquetas a uno, bolsas a otro—, recortan unos puntos en cada uno y nunca calculan el peso del embalaje sobre el precio de venta ni la amortización del utillaje. Esta guía descompone el embalaje en seis familias con sus factores de coste e inversión puntual, propone lógica de reparto para tres tramos de precio, explica por qué el utillaje debe ir aparte del coste variable (la misma plancha difiere diez veces entre 3.000 y 30.000 piezas), enumera cinco campos que deben coincidir antes de comparar cotizaciones e indica cuándo mover presupuesto de etiquetas a bolsas.",
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
    print("  %-48s desc_zh=%d字 desc_en=%d字符 desc_ja=%d desc_ko=%d desc_fr=%d desc_es=%d"
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

# ---------------- 2) blog/index.html 顶部插入两张卡片 ---------------- 2) blog/index.html 顶部插入两张卡片 ----------------
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
