#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""就地生成 daily_gen_20261107_2000.py：复用 2026-11-07 16:00 批次脚本的流程尾部。"""
import os

ROOT = os.path.dirname(os.path.abspath(__file__))
OLD = os.path.join(ROOT, "daily_gen_20261107_1600.py")
NEW = os.path.join(ROOT, "daily_gen_20261107_2000.py")

src = open(OLD, encoding="utf-8").read()
i = src.index("skel = open(SKEL")
tail = src[i:]

HEADER = '''#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-11-07 20:00 批次（六语：zh-Hant 根 / en / ja / ko / fr / es）
- 防尘袋与成衣罩（dust-bag-garment-cover-guide）
- 吊牌悬挂位置（hang-tag-hanging-position-guide）

用法: F:/hermes/venvs/tools/Scripts/python.exe daily_gen_20261107_2000.py [--check]
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
BUST_OLD, BUST_NEW = "203", "204"
LANGS = ["en", "ja", "ko", "fr", "es"]

'''

ARTICLES = '''ARTICLES = [
    dict(
        slug="dust-bag-garment-cover-guide.html",
        body="blog/_body_dust.html",
        title_zh="防尘袋与成衣罩：法兰绒、无纺布、PEVA 怎么选 | TAGE",
        title_en="Dust Bags and Garment Covers: Flannel, Nonwoven or PEVA | TAGE",
        title_ja="ドレスカバーと衣類カバー：フランネル・不織布・PEVA の選び方 | TAGE",
        title_ko="더스트백과 의류 커버: 플란넬·부직포·PEVA 선택 | TAGE",
        title_fr="Housses de protection : flanelle, non-tissé ou PEVA | TAGE",
        title_es="Fundas protectoras: franela, non-woven o PEVA | TAGE",
        desc_zh="防尘袋与成衣罩选购指南：法兰绒、PP 无纺布、PEVA、棉帆布在克重、透气、防潮与成本上的差异，抽绳与拉链结构、按衣长反推的尺寸表、丝印与织唛呈现，以及海运霉变与 REACH 验收要点。附打样前六项清单。来自东莞泰阁包装。",
        desc_en="Dust bags and garment covers compared: flannel, PP nonwoven, PEVA and canvas by weight, breathability and cost, plus drawstring build, sizing and export checks.",
        desc_ja="ドレスカバーと衣類カバーの選び方。フランネル・PP 不織布・PEVA・綿キャンバスを目付・通気・防湿・コストで比較し、紐とファスナーの構造、着丈から逆算する寸法表、シルク印刷と織りラベルの見せ方、海上輸送の黴と REACH の検収まで整理します。",
        desc_ko="더스트백과 의류 커버 선택 가이드. 플란넬·PP 부직포·PEVA·코튼 캔버스를 평량, 통기, 방습, 원가로 비교하고 끈·지퍼 구조, 의류 길이에서 역산하는 치수표, 실크 인쇄와 직조 라벨 표현, 해상 운송 곰팡이와 REACH 검수까지 정리합니다.",
        desc_fr="Housses de protection comparées : flanelle, non-tissé PP, PEVA et canvas selon grammage, respirabilité et coût, plus cordon, dimensions et contrôles export.",
        desc_es="Fundas protectoras comparadas: franela, non-woven PP, PEVA y lona por gramaje, transpirabilidad y coste, más cordón, medidas y controles de exportación.",
        crumb_zh="防尘袋与成衣罩",
        crumb_en="Dust Bags and Covers",
        crumb_ja="ドレスカバーとカバー",
        crumb_ko="더스트백과 커버",
        crumb_fr="Housses de protection",
        crumb_es="Fundas protectoras",
        h1_zh="防尘袋与成衣罩：法兰绒、无纺布、PEVA 怎么选",
        h1_en="Dust Bags and Garment Covers: Flannel, Nonwoven or PEVA",
        h1_ja="ドレスカバーと衣類カバー：フランネル・不織布・PEVA の選び方",
        h1_ko="더스트백과 의류 커버: 플란넬·부직포·PEVA 선택 기준",
        h1_fr="Housses de protection : flanelle, non-tissé ou PEVA",
        h1_es="Fundas protectoras: franela, non-woven o PEVA",
        tag_zh="包装指南", tag_en="Packaging Guide", tag_ja="包装ガイド",
        tag_ko="포장 가이드", tag_fr="Guide emballage", tag_es="Guía de embalaje",
        sum_zh="防尘袋常被当成挂装胶袋的布料版来做，结果不是尺寸不合就是抽绳一拉就开线。这篇把防尘袋、挂装袋、手提袋三者的验收逻辑分开，给出四种材质对照、按衣长反推的尺寸表、丝印与织唛的呈现方式，以及海运霉变和 REACH 的五个必检项。",
        sum_en="Dust bags get made as a fabric version of the hanging polybag, and end up short at the hem or split at the drawstring. This separates dust bags, hanging bags and totes by inspection logic, then compares four materials, works sizes back from garment length, and lists five export checks.",
        sum_ja="ドレスカバーは吊り袋の布版として作られ、寸法が合わないか紐がすぐほつれます。ドレスカバー・吊り袋・トートの検収論理を分け、四素材の比較、着丈からの逆算寸法、シルク印刷と織りラベルの見せ方、海上輸送の黴と REACH の五項目を整理します。",
        sum_ko="더스트백은 행잉 폴리백의 원단 버전처럼 만들어져 길이가 맞지 않거나 끈이 터집니다. 더스트백·행잉백·토트의 검수 논리를 나누고, 네 소재 비교, 의류 길이 역산 치수표, 실크 인쇄와 직조 라벨 표현, 해상 곰팡이와 REACH 다섯 항목을 정리합니다.",
        sum_fr="La housse est souvent fabriquée comme un polybag en tissu : trop courte à l'ourlet ou lâche au cordon. On sépare housse, sac suspendu et tote par leur logique de contrôle, puis quatre matières, les dimensions calculées depuis la longueur, et cinq contrôles export.",
        sum_es="La funda se hace como un polybag de tela y acaba corta en el bajo o suelta en el cordón. Separamos funda, bolsa colgante y tote por su lógica de control, comparamos cuatro materiales, calculamos medidas desde el largo y damos cinco controles de exportación.",
    ),
    dict(
        slug="hang-tag-hanging-position-guide.html",
        body="blog/_body_hangpos.html",
        title_zh="吊牌挂在哪里：位置选择、打孔点与陈列规范 | TAGE",
        title_en="Where to Attach a Hang Tag: Position, Hole and Display | TAGE",
        title_ja="値札の取付位置：場所・穴位置・陳列ルール | TAGE",
        title_ko="행택 부착 위치: 자리·구멍·진열 규칙 | TAGE",
        title_fr="Où fixer un carton : position, perçage et présentation | TAGE",
        title_es="Dónde colgar la etiqueta: posición, troquel y exposición | TAGE",
        desc_zh="吊牌挂在哪里，决定顾客第一眼能否读到品牌、试穿会不会扯掉、退货时吊牌还在不在。本文按 T 恤、衬衫、裤装、裙装、外套、泳装、配饰给出首选挂位表，讲清孔位到边距离、重心与鸡眼加固、四样不能遮挡的东西、陈列朝向与防盗扣位置。来自东莞泰阁包装。",
        desc_en="Where a hang tag sits decides whether the brand is read, whether it survives trying on, and whether it is still there at return. Position table by category, hole distance, eyelets.",
        desc_ja="値札の取付位置は、最初の一目でブランドが読めるか、試着で切れないか、返品時に残るかを決めます。Tシャツ・シャツ・パンツ・スカート・コート・水着・小物の位置表、穴の端距離と重心、ハトメ補強、隠してはいけない四つ、陳列の向きと防盗タグの位置を整理します。",
        desc_ko="행택 위치는 첫눈에 브랜드가 읽히는지, 입어볼 때 뜯기지 않는지, 반품 시 남아 있는지를 결정합니다. 티셔츠·셔츠·팬츠·스커트·코트·수영복·액세서리별 위치표, 구멍-가장자리 거리와 무게중심, 아일릿 보강, 가리면 안 되는 네 가지, 진열 방향과 도난 방지 태그 위치를 정리합니다.",
        desc_fr="L'emplacement du carton décide si la marque est lue, s'il survit à l'essayage et s'il est encore là au retour. Tableau par catégorie, distance du trou, œillets et présentation.",
        desc_es="La posición del colgante decide si se lee la marca, si sobrevive a la prueba y si sigue en una devolución. Tabla por categoría, distancia del agujero, ojales y exposición.",
        crumb_zh="吊牌悬挂位置",
        crumb_en="Hang Tag Position",
        crumb_ja="値札の取付位置",
        crumb_ko="행택 부착 위치",
        crumb_fr="Position du carton",
        crumb_es="Posición del colgante",
        h1_zh="吊牌挂在哪里：位置选择、打孔点与陈列规范",
        h1_en="Where to Attach a Hang Tag: Position, Hole and Display",
        h1_ja="値札の取付位置：場所・穴位置・陳列ルール",
        h1_ko="행택 부착 위치: 자리·구멍·진열 규칙",
        h1_fr="Où fixer un carton : position, perçage et présentation",
        h1_es="Dónde colgar la etiqueta: posición, troquel y exposición",
        tag_zh="吊牌指南", tag_en="Hangtag Guide", tag_ja="値札ガイド",
        tag_ko="행택 가이드", tag_fr="Guide carton", tag_es="Guía de colgantes",
        sum_zh="挂在领口还是腰头，看着是小事，却同时决定三件事：第一眼能不能读到品牌、试穿会不会被扯掉、退货时吊牌还在不在。这篇给出七个品类的首选挂位表、孔位到边距离与重心规则、四样不能被遮挡的东西，以及陈列朝向与防盗扣的正确位置。",
        sum_en="Neckline or waistband looks like a small choice and settles three things at once: whether the brand is read, whether the tag survives trying on, and whether it is still there at return. Position table for seven categories, hole distance and gravity rules, four things never to cover, and where the security tag belongs.",
        sum_ja="衿元か腰かは小さな選択に見えて、三つを同時に決めます。一目でブランドが読めるか、試着で切れないか、返品時に残るか。七品種の位置表、穴の端距離と重心の規則、隠してはいけない四つ、陳列の向きと防盗タグの正しい位置を整理します。",
        sum_ko="목선이냐 허리냐는 사소해 보이지만 세 가지를 동시에 정합니다. 첫눈에 브랜드가 읽히는지, 입어볼 때 뜯기지 않는지, 반품 시 남는지. 일곱 품목의 위치표, 구멍 거리와 무게중심 규칙, 가리면 안 되는 네 가지, 진열 방향과 도난 방지 태그 위치를 정리합니다.",
        sum_fr="Encolure ou ceinture : un choix minuscule qui règle trois choses — la marque lue, le carton qui survit à l'essayage, sa présence au retour. Tableau pour sept catégories, distance du trou, règles de gravité, quatre interdits et place de l'antivol.",
        sum_es="Escote o cintura parece menor y decide tres cosas: que se lea la marca, que la etiqueta sobreviva a la prueba y que siga en una devolución. Tabla de siete categorías, distancia del agujero, reglas de gravedad, cuatro cosas que no se tapan y dónde va la alarma.",
    ),
]

'''

out = HEADER + ARTICLES + tail
open(NEW, "w", encoding="utf-8", newline="\n").write(out)
print("生成 %s (%d 行)" % (NEW, out.count("\n") + 1))
