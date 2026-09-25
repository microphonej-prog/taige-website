#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-09-25 晚间 每日更新：2 篇新文章（六语：zh-Hant 根 / en / ja / ko / fr / es）
- 服装辅料与面料配伍性指南：缩水率、色牢度与洗水测试怎么匹配（技术长尾：标签缩率/沾色/ISO 洗涤测试）
- 服装辅料酚黄变（BHT）防治指南：白色织唛与胶袋怎么选（行业痛点：无酚包装、ISO 105-X18）
用法: python daily_gen_20260925_evening.py
"""
import os, re, sys, subprocess, importlib.util

ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)
PY = sys.executable

SKEL = "blog/knitwear-sweater-trims-guide.html"
DATE_ZH = "2026年9月25日"
DATE_EN = "September 25, 2026"
DATE_JA = "2026年9月25日更新"
DATE_KO = "2026년 9월 25일 업데이트"
DATE_FR = "25 septembre 2026"
DATE_ES = "25 de septiembre de 2026"
SITEMAP_DATE = "2026-09-25"
BUST_OLD, BUST_NEW = "109", "110"
LANGS = ["en", "ja", "ko", "fr", "es"]

ARTICLES = [
    dict(
        slug="garment-trims-fabric-compatibility-guide.html",
        body="blog/_body_compat.html",
        title_zh="服装辅料与面料配伍性指南：缩水率、色牢度与洗水测试怎么匹配 | TAGE",
        title_en="Fabric and Trim Compatibility: Shrinkage, Colour Fastness, Wash Testing | TAGE",
        title_ja="副資材と生地の相性ガイド：収縮率・堅牢度・洗濯試験の合わせ方 | TAGE",
        title_ko="부자재와 원단 궁합 가이드: 수축률, 견뢰도, 세탁 시험 맞추기 | TAGE",
        title_fr="Compatibilité tissu et accessoires : retrait, solidité et essais de lavage | TAGE",
        title_es="Compatibilidad entre tela y accesorios: encogimiento, solidez y ensayos | TAGE",
        desc_zh="服装辅料与面料配伍性指南：织唛与洗水标缩率怎么和面料对齐、深色掉色串色怎么防，ISO 6330 洗涤、ISO 105-C06 耐洗色牢度与 ISO 105-E04 耐汗渍怎么选用，附洗前洗后对比验证与配伍确认清单。来自东莞泰阁包装。",
        desc_en="How to match trims to fabric: align woven label and care label shrinkage, prevent cross-staining, and choose ISO 6330, ISO 105-C06 and ISO 105-E04 tests.",
        desc_ja="副資材と生地の相性ガイド。織りラベル・洗濯表示ラベルの収縮率を生地と合わせる方法、濃色からの色移り対策、ISO 6330の洗濯、ISO 105-C06の洗濯堅牢度、ISO 105-E04の汗堅牢度の使い分けと発注前の検証を解説します。東莞泰閣包装。",
        desc_ko="부자재와 원단의 궁합 가이드. 직조 라벨·세탁 표시 라벨의 수축률을 원단과 맞추는 방법, 농색에서의 색 이동 대책, ISO 6330 세탁, ISO 105-C06 세탁 견뢰도, ISO 105-E04 땀 견뢰도의 선택과 발주 전 검증 절차를 정리했습니다. 둥관 TAGE 패키징.",
        desc_fr="Compatibilité tissu/accessoires : aligner les retraits des tissés et étiquettes d'entretien, éviter la déteinture, choisir ISO 6330, 105-C06 et 105-E04.",
        desc_es="Compatibilidad tela/accesorios: alinear encogimientos de tejidas y etiquetas, evitar el manchado y elegir los ensayos ISO 6330, 105-C06 y 105-E04.",
        crumb_zh="辅料与面料配伍", crumb_en="Fabric Trim Compatibility", crumb_ja="副資材と生地の相性",
        crumb_ko="부자재와 원단 궁합", crumb_fr="Compatibilité tissu/accessoires", crumb_es="Compatibilidad tela/accesorios",
        h1_zh="服装辅料与面料配伍性指南：缩水率、色牢度与洗水测试怎么匹配",
        h1_en="Fabric and Trim Compatibility: Shrinkage, Colour Fastness and Wash Testing",
        h1_ja="副資材と生地の相性ガイド：収縮率・堅牢度・洗濯試験の合わせ方",
        h1_ko="부자재와 원단 궁합 가이드: 수축률, 견뢰도, 세탁 시험 맞추기",
        h1_fr="Compatibilité tissu et accessoires : retrait, solidité et essais de lavage",
        h1_es="Compatibilidad entre tela y accesorios: encogimiento, solidez y ensayos",
        tag_zh="技术指南", tag_en="Technical Guide", tag_ja="技術ガイド", tag_ko="기술 가이드",
        tag_fr="Guide technique", tag_es="Guía técnica",
        sum_zh="辅料本身做得再好，也要和面料一起过洗水这一关：缩率不同步就起皱鼓包，深色配浅色标就串色，涂层标遇高温熨烫就卷边。本文把配伍讲成三件事——缩率怎么对齐（ISO 6330 洗涤、ISO 3759 量尺寸）、色牢度按哪些项目测（ISO 105-C06 耐洗、ISO 105-E04 耐汗渍、ISO 105-X11 耐熨烫）、洗护方式怎么决定测试矩阵，附带一张下单前必须跑完的配伍验证清单。",
        sum_en="A trim can be perfectly made and still fail once it goes through the wash with the garment: mismatched shrinkage puckers, dark-on-pale combinations bleed, coated labels curl under a hot iron. This guide reduces compatibility to three jobs — aligning shrinkage (ISO 6330 wash, ISO 3759 measurement), choosing the right fastness tests (ISO 105-C06 washing, ISO 105-E04 perspiration, ISO 105-X11 ironing) and letting the care method set the test matrix — and closes with the checks to finish before you order.",
        sum_ja="副資材が良くできていても、生地と一緒に洗濯を通過できなければ意味がありません。収縮率がずれればしわや浮き、濃色と淡色の組み合わせでは色移り、コーティングラベルは高温アイロンでカールします。本記事は相性を3点に整理します。収縮率の合わせ方（ISO 6330の洗濯、ISO 3759の寸法測定）、確認すべき堅牢度項目（ISO 105-C06の洗濯、ISO 105-E04の汗、ISO 105-X11のアイロン）、洗濯方法から試験マトリクスを決める考え方、そして発注前に済ませる検証チェックリストです。",
        sum_ko="부자재가 잘 만들어져도 원단과 함께 세탁을 통과하지 못하면 소용이 없습니다. 수축률이 어긋나면 주름과 들뜸이, 어두운 색과 연한 색 조합에서는 색 이동이, 코팅 라벨은 고온 다림질에서 말림이 생깁니다. 이 글은 궁합을 세 가지로 정리합니다. 수축률 맞추기(ISO 6330 세탁, ISO 3759 치수 측정), 확인해야 할 견뢰도 항목(ISO 105-C06 세탁, ISO 105-E04 땀, ISO 105-X11 다림질), 세탁 방식이 시험 매트릭스를 정하는 논리, 그리고 발주 전 끝내야 할 검증 체크리스트입니다.",
        sum_fr="Un accessoire peut être parfaitement exécuté et échouer au premier lavage avec le vêtement : retraits désaccordés, godage ; foncé sur clair, déteinture ; étiquette enduite, enroulement au fer chaud. Ce guide ramène la compatibilité à trois tâches — aligner les retraits (lavage ISO 6330, mesure ISO 3759), choisir les essais de solidité (ISO 105-C06 lavage, ISO 105-E04 transpiration, ISO 105-X11 repassage) et laisser le mode d'entretien définir la matrice d'essais — et se termine par la liste à vérifier avant commande.",
        sum_es="Un accesorio puede estar perfectamente hecho y fallar en el primer lavado con la prenda: encogimientos desalineados producen arrugas, las combinaciones oscuro sobre claro destiñen, las etiquetas recubiertas se enrollan con la plancha. Esta guía reduce la compatibilidad a tres tareas —alinear encogimientos (lavado ISO 6330, medición ISO 3759), elegir los ensayos de solidez (ISO 105-C06 lavado, ISO 105-E04 sudor, ISO 105-X11 planchado) y dejar que el tipo de cuidado defina la matriz— y termina con la lista previa al pedido.",
    ),
    dict(
        slug="textile-phenolic-yellowing-guide.html",
        body="blog/_body_yellowing.html",
        title_zh="服装辅料酚黄变（BHT）防治指南：白色织唛与胶袋怎么选 | TAGE",
        title_en="Phenolic Yellowing in Apparel Trims: BHT, Packaging and Storage | TAGE",
        title_ja="副資材のフェノール黄変ガイド：BHT・包装・保管の対策 | TAGE",
        title_ko="부자재 페놀 황변 가이드: BHT, 포장, 보관 대책 | TAGE",
        title_fr="Jaunissement phénolique des accessoires : BHT, emballage et stockage | TAGE",
        title_es="Amarilleamiento fenólico en accesorios: BHT, embalaje y almacenaje | TAGE",
        desc_zh="服装辅料酚黄变（BHT 黄变）防治指南：白色织唛、洗水标与棉绳在仓库放几周就发黄的原因，无酚胶袋与纸包装怎么选、仓储温湿度与 NOx 来源怎么避，ISO 105-X18 酚黄变测试与 4 级验收口径怎么定，附整改复测清单。来自东莞泰阁包装。",
        desc_en="Why white woven labels and care labels yellow in the warehouse: BHT in packaging film, NOx, storage conditions, BHT-free bags and ISO 105-X18 testing.",
        desc_ja="白い織りラベルや洗濯表示ラベルが倉庫で黄ばむ原因を解説。包装フィルムのBHTと窒素酸化物の反応、BHTフリー袋と紙包装の選び方、温湿度とNOx源の避け方、ISO 105-X18による試験と4級以上の検収目安、是正後の再試験までまとめました。東莞泰閣包装。",
        desc_ko="흰색 직조 라벨과 세탁 표시 라벨이 창고에서 노래지는 이유를 정리했습니다. 포장 필름의 BHT와 질소산화물 반응, BHT-free 비닐과 종이 포장 선택, 온습도와 NOx 발생원 회피, ISO 105-X18 시험과 4급 이상 기준, 시정 후 재시험까지 다룹니다. 둥관 TAGE 패키징.",
        desc_fr="Pourquoi les tissés et étiquettes blanches jaunissent en entrepôt : BHT des films, NOx, conditions de stockage, sacs sans BHT et essai ISO 105-X18.",
        desc_es="Por qué amarillean en almacén las tejidas y etiquetas blancas: BHT del film, NOx, condiciones de almacenaje, bolsas sin BHT y ensayo ISO 105-X18.",
        crumb_zh="酚黄变防治", crumb_en="Phenolic Yellowing", crumb_ja="フェノール黄変",
        crumb_ko="페놀 황변", crumb_fr="Jaunissement phénolique", crumb_es="Amarilleamiento fenólico",
        h1_zh="服装辅料酚黄变（BHT）防治指南：白色织唛与胶袋怎么选",
        h1_en="Phenolic Yellowing in Apparel Trims: BHT, Packaging and Storage",
        h1_ja="副資材のフェノール黄変ガイド：BHT・包装・保管の対策",
        h1_ko="부자재 페놀 황변 가이드: BHT, 포장, 보관 대책",
        h1_fr="Jaunissement phénolique des accessoires : BHT, emballage et stockage",
        h1_es="Amarilleamiento fenólico en accesorios: BHT, embalaje y almacenaje",
        tag_zh="质量指南", tag_en="Quality Guide", tag_ja="品質ガイド", tag_ko="품질 가이드",
        tag_fr="Guide qualité", tag_es="Guía de calidad",
        sum_zh="白色织唛、洗水标、棉绳在仓库放几周就泛黄，多半不是脏也不是霉，而是酚黄变：包装胶袋里的抗氧剂 BHT 迁移到织物上，与空气中的氮氧化物反应生成黄色物质。本文讲清三个必要条件、哪些材料最脆弱（尼龙、氨纶、白色与浅色、荧光增白白）、无酚胶袋与纸包装怎么选、仓储温湿度与 NOx 源怎么避、ISO 105-X18 的测试与 4 级验收口径，以及已经黄了之后的来源定位与整改复测。",
        sum_en="White woven labels, care labels and cotton cord that yellow after weeks in the warehouse are usually neither dirty nor mouldy: it is phenolic yellowing, where the antioxidant BHT in packaging film migrates onto the textile and reacts with airborne nitrogen oxides. This guide covers the three conditions required, the most vulnerable materials (nylon, elastane, whites and pales, optically brightened whites), how to specify BHT-free bags or paper, how to keep storage humidity and NOx sources under control, ISO 105-X18 testing against a grade 4 limit, and what to do once goods have yellowed.",
        sum_ja="白い織りラベルや洗濯表示ラベル、綿ひもが倉庫で数週間置くと黄ばむのは、汚れでもカビでもなくフェノール黄変であることが多いです。包装フィルムの酸化防止剤BHTが繊維に移行し、空気中の窒素酸化物と反応して黄色物質が生成します。本記事は3つの必要条件、最も脆弱な材料（ナイロン・ポリウレタン・白と淡色・蛍光増白白）、BHTフリー袋と紙包装の選び方、温湿度とNOx源の管理、ISO 105-X18試験と4級以上の検収目安、黄変発生後の原因特定と是正後の再試験を解説します。",
        sum_ko="흰색 직조 라벨, 세탁 표시 라벨, 면 끈이 창고에서 몇 주 만에 노래지는 것은 대개 오염이나 곰팡이가 아니라 페놀 황변입니다. 포장 필름의 산화방지제 BHT가 섬유로 이동해 공기 중 질소산화물과 반응하여 노란 물질을 만듭니다. 이 글은 세 가지 필수 조건, 가장 취약한 소재(나일론, 스판덱스, 흰색과 연한 색, 형광증백 흰색), BHT-free 비닐과 종이 포장 선택, 온습도와 NOx 발생원 관리, ISO 105-X18 시험과 4급 이상 기준, 황변 발생 후 원인 규명과 시정 후 재시험을 다룹니다.",
        sum_fr="Des tissés, étiquettes d'entretien et cordons coton blancs qui jaunissent en quelques semaines d'entrepôt ne sont en général ni sales ni moisis : c'est un jaunissement phénolique, où l'antioxydant BHT du film d'emballage migre sur le textile et réagit avec les oxydes d'azote. Ce guide couvre les trois conditions nécessaires, les matières les plus fragiles (nylon, élasthanne, blancs et clairs, blancs azurés), le choix de sacs sans BHT ou du papier, la maîtrise de l'humidité et des sources de NOx, l'essai ISO 105-X18 avec un seuil de 4, et la conduite à tenir après un jaunissement.",
        sum_es="Las tejidas, etiquetas de cuidado y cordones de algodón blancos que amarillean tras semanas de almacén no suelen estar sucios ni con moho: es amarilleamiento fenólico, donde el antioxidante BHT del film de embalaje migra al textil y reacciona con los óxidos de nitrógeno del aire. Esta guía cubre las tres condiciones necesarias, los materiales más frágiles (nailon, elastano, blancos y claros, blancos abrillantados), cómo especificar bolsas sin BHT o papel, el control de humedad y de fuentes de NOx, el ensayo ISO 105-X18 con límite de grado 4 y qué hacer cuando ya ha amarilleado.",
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
for wrong in ["garment-trims-fabric-compatibility-guide", "textile-phenolic-yellowing-guide"]:
    pass
print("选题全新，开始生成")

# ---------------- desc 长度体检 ----------------
for a in ARTICLES:
    print("  %-46s desc_zh=%d字 desc_en=%d字符 desc_ja=%d desc_ko=%d desc_fr=%d desc_es=%d"
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
