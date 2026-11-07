#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""就地生成 daily_gen_20261107_1600.py：复用 2026-11-05 14:00 批次脚本的流程尾部。"""
import os

ROOT = os.path.dirname(os.path.abspath(__file__))
OLD = os.path.join(ROOT, "daily_gen_20261105_1400.py")
NEW = os.path.join(ROOT, "daily_gen_20261107_1600.py")

src = open(OLD, encoding="utf-8").read()
i = src.index("skel = open(SKEL")
tail = src[i:]

HEADER = '''#!/usr/bin/env python3
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
BUST_OLD, BUST_NEW = "201", "202"
LANGS = ["en", "ja", "ko", "fr", "es"]

'''

ARTICLES = '''ARTICLES = [
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

'''

out = HEADER + ARTICLES + tail
open(NEW, "w", encoding="utf-8", newline="\n").write(out)
print("生成 %s (%d 行)" % (NEW, out.count("\n") + 1))
