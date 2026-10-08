#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-08 下午批次（14:00）每日更新：2 篇新文章元数据（六语：zh-Hant 根 / en / ja / ko / fr / es）

选题说明（主题池 30 项与既有扩展均已上线，本次沿两个尚未独立成文的方向扩展，
已核对 blog/、en|ja|ko|fr|es/blog/ 与 sitemap.xml 无重复 slug，并 grep 全站确认关键词覆盖情况：

- wooden-bamboo-hang-tags：全站 grep「木质吊牌 / 木牌 / 桦木」0 处（仅 compare 表里出现过一次
  「木质、牛角与天然材质」），「bamboo」7 处均为竹纤维纸/竹纤维混纺，无一篇讲木竹吊牌本身。
  本文讲清桦木多层板 / 原木片 / 竹片与重组竹 / 密度板贴木纹四类材质的厚度与风险、
  含水率（8–12%）与纹理方向对开裂翘曲的影响、激光雕刻 / 激光镂空 / 丝印与烫印 / UV 打印的取舍、
  边缘倒角与木蜡油·清漆·UV 油三种表面处理、打孔公差与鸡眼·腰扣·吊绳搭配、MOQ 与成本构成，
  以及可直接抄进询价单的验收口径。

- print-on-demand-apparel-labels：全站 grep「DTG / print-on-demand / dropship / sublimation / 按需印花」
  0 处；heat-transfer-labels 讲的是热转印「标」这一品类本身，care-label-wash-durability 讲洗水标
  自身掉字，均不涉及印花图案的耐洗边界与洗护声明的匹配。本文讲清 DTG 直喷、DTF 热转印膜、
  热升华、丝印胶浆与刺绣的耐洗边界，洗护声明如何跟着印料走（洗涤符号、烘干与熨烫条件），
  耐洗测试的次数·项目·判定（AATCC 61/135、ISO 6330 + 105-C06、GB/T 3921/8629）与洗后尺寸的单独约定，
  热转印标 / 自粘洗标 / 空白标打印三种落地方式与缝制·烫贴取舍，FTC 16 CFR 423、EU 1007/2011、
  GPSR 与亚马逊·TikTok Shop 的平台要求，以及验收与询价清单。
"""

ARTICLES = [
    dict(
        slug="wooden-bamboo-hang-tags.html",
        body="blog/_body_wood.html",
        title_zh="木质与竹质吊牌指南：材质、雕刻工艺与成本 | TAGE",
        title_en="Wooden and Bamboo Hang Tag Guide: Material and Engraving | TAGE",
        title_ja="木製・竹製タグガイド：素材・彫刻加工・コスト | TAGE",
        title_ko="목재·대나무 행택 가이드: 소재·각인 공정·비용 | TAGE",
        title_fr="Guide des étiquettes suspendues en bois et bambou | TAGE",
        title_es="Guía de etiquetas colgantes de madera y bambú | TAGE",
        desc_zh="木质与竹质吊牌指南：分清桦木多层板、原木片、竹片与密度板四类材质的厚度与风险，讲清含水率、纹理方向与开裂翘曲的关系，激光雕刻、丝印、烫印与 UV 打印怎么选，以及打孔、五金、吊绳搭配与可直接写进询价单的验收口径。来自东莞泰阁包装。",
        desc_en="Wooden and bamboo hang tags: birch plywood, solid wood, bamboo and MDF compared, moisture and grain control, laser engraving versus print, and acceptance.",
        desc_ja="木製・竹製タグガイド。バーチ合板・無垢材・竹・MDF化粧板の厚みとリスク、含水率と木目の方向が割れ・反りに与える影響、レーザー彫刻・スクリーン・箔・UVプリントの使い分け、穴・金具・ひもの組み合わせ、そのまま見積書に使える検収基準を解説。東莞泰閣包装。",
        desc_ko="목재·대나무 행택 가이드. 자작나무 합판·원목·대나무·MDF의 두께와 리스크, 함수율과 결 방향이 갈라짐·휨에 미치는 영향, 레이저 각인·스크린·박·UV 프린트 선택, 구멍·금속 부자재·끈 조합과 검수 기준을 정리했습니다. 둥관 TAGE 패키징.",
        desc_fr="Guide des étiquettes bois et bambou : contreplaqué de bouleau, bois massif, bambou et MDF comparés, humidité et sens du fil, gravure laser ou impression, accessoires et réception.",
        desc_es="Guía de etiquetas de madera y bambú: contrachapado de abedul, madera maciza, bambú y MDF comparados, humedad y veta, grabado láser o impresión, herrajes y recepción.",
        crumb_zh="木质与竹质吊牌",
        crumb_en="Wooden and Bamboo Hang Tags",
        crumb_ja="木製・竹製タグ",
        crumb_ko="목재·대나무 행택",
        crumb_fr="Étiquettes bois et bambou",
        crumb_es="Etiquetas de madera y bambú",
        h1_zh="木质与竹质吊牌指南：材质、厚度与雕刻工艺",
        h1_en="Wooden and Bamboo Hang Tags: Material, Thickness and Engraving",
        h1_ja="木製・竹製タグガイド：素材・厚み・彫刻加工",
        h1_ko="목재·대나무 행택 가이드: 소재·두께·각인 공정",
        h1_fr="Étiquettes suspendues en bois et bambou : matière, épaisseur et gravure",
        h1_es="Etiquetas colgantes de madera y bambú: material, espesor y grabado",
        tag_zh="材质指南",
        tag_en="Material Guide",
        tag_ja="素材ガイド",
        tag_ko="소재 가이드",
        tag_fr="Guide des matières",
        tag_es="Guía de materiales",
        sum_zh="木质与竹质吊牌把材质本身变成了信息，但木竹不是纸：厚度按毫米算，含水率偏高交货后会翘曲开裂，纹理方向决定吊孔会不会撕裂，雕刻深浅直接暴露工艺水平。本文用一张对比表分清桦木多层板、原木片、竹片与密度板贴木纹四类材质，讲清厚度公差、含水率与纹理方向的写法，激光雕刻、丝网印刷、烫印与 UV 打印怎么选，边缘倒角与表面防护怎么做，打孔、五金与吊绳怎么搭，以及起订量、成本构成与可直接抄进询价单的验收口径。",
        sum_en="Wooden and bamboo hang tags turn the material itself into information, but wood is not paper: thickness is measured in millimetres, moisture that is too high means warping and cracks after delivery, grain direction decides whether the hang hole tears and engraving depth exposes the level of the workshop. This guide separates birch plywood, solid wood, bamboo and MDF with one comparison table, sets out thickness tolerances, moisture content and grain direction, weighs laser engraving against screen printing, foil and UV print, covers edge chamfering and surface protection, pairs holes with eyelets, swivel hooks and cords, and closes with MOQ, cost structure and acceptance criteria you can paste into a quotation request.",
        sum_ja="木製・竹製タグは素材そのものを情報に変えますが、木と竹は紙ではありません。厚みはミリ単位、含水率が高ければ納品後に反りや割れが出て、木目の方向が吊り穴の裂けを決め、彫刻の深さが工房の実力を露呈します。本記事は比較表でバーチ合板・無垢材・竹・MDF化粧板を整理し、厚み公差・含水率・木目の書き方、レーザー彫刻・スクリーン印刷・箔押し・UVプリントの選び方、面取りと表面保護、穴・金具・ひもの組み合わせ、最低ロットとコスト構成、見積依頼にそのまま使える検収基準を示します。",
        sum_ko="목재·대나무 행택은 소재 자체를 정보로 바꾸지만 목재는 종이가 아닙니다. 두께는 밀리미터 단위이고 함수율이 높으면 납품 후 휨과 갈라짐이 생기며, 결 방향이 구멍의 찢어짐을, 각인 깊이가 작업장의 실력을 드러냅니다. 이 글은 비교표로 자작나무 합판·원목·대나무·MDF를 정리하고 두께 공차·함수율·결 방향 표기법, 레이저 각인·스크린 인쇄·박·UV 프린트의 선택, 모따기와 표면 보호, 구멍·금속 부자재·끈 조합, 최소 주문량과 원가 구성, 견적 요청서에 바로 쓸 수 있는 검수 기준을 제시합니다.",
        sum_fr="L'étiquette bois ou bambou fait de la matière un message, mais le bois n'est pas du papier : l'épaisseur se compte en millimètres, une humidité trop élevée signifie gauchissement et fissures après livraison, le sens du fil décide si le trou se déchire et la profondeur de gravure révèle le niveau de l'atelier. Ce guide distingue contreplaqué de bouleau, bois massif, bambou et MDF dans un tableau, fixe les tolérances d'épaisseur, l'humidité et le sens du fil, compare gravure laser, sérigraphie, dorure et impression UV, traite le chanfrein et la protection de surface, associe trous, œillets, crochets et cordons, puis conclut sur la quantité minimale, la structure de coût et les critères de réception.",
        sum_es="La etiqueta de madera o bambú convierte el material en mensaje, pero la madera no es papel: el espesor se mide en milímetros, una humedad alta implica alabeo y grietas tras la entrega, la dirección de la veta decide si el agujero se rasga y la profundidad del grabado expone el nivel del taller. Esta guía separa contrachapado de abedul, madera maciza, bambú y MDF en una tabla, fija tolerancias de espesor, humedad y veta, compara grabado láser, serigrafía, estampación e impresión UV, cubre chaflán y protección de superficie, combina agujeros, ojales, ganchos y cordones, y cierra con cantidad mínima, estructura de coste y criterios de recepción.",
    ),
    dict(
        slug="print-on-demand-apparel-labels.html",
        body="blog/_body_pod.html",
        title_zh="按需印花服装的洗水标与吊牌指南：DTG/DTF 与洗护声明 | TAGE",
        title_en="Print-on-Demand Apparel Labels: DTG and DTF Care Claims | TAGE",
        title_ja="オンデマンドプリント衣料の洗濯表示とタグ：DTG/DTF | TAGE",
        title_ko="온디맨드 프린트 의류의 세탁 라벨과 행택: DTG/DTF | TAGE",
        title_fr="Étiquettes pour vêtements imprimés à la demande : DTG et DTF | TAGE",
        title_es="Etiquetas para prendas estampadas bajo demanda: DTG y DTF | TAGE",
        desc_zh="按需印花服装的洗水标与吊牌指南：分清 DTG、DTF、热升华与丝印的耐洗边界，讲清洗护声明怎么跟着印料走、耐洗测试的次数与判定口径、热转印标与自粘洗标的落地方式，以及 FTC、欧盟与电商平台的标签要求。来自东莞泰阁包装。",
        desc_en="Print-on-demand apparel labels: DTG, DTF, sublimation and screen print wash limits, how to word care claims, wash test criteria, transfer and adhesive labels.",
        desc_ja="オンデマンドプリント衣料の洗濯表示とタグ。DTG・DTF・昇華・スクリーンの耐洗濯限界、洗濯表示の書き方、耐洗濯試験の回数と判定、熱転写ラベルと粘着ラベルの実装、FTC・EU・ECプラットフォームの要件を解説。東莞泰閣包装。",
        desc_ko="온디맨드 프린트 의류의 세탁 라벨과 행택. DTG·DTF·승화·스크린의 세탁 한계, 세탁 표시 작성법, 세탁 시험 횟수와 판정, 열전사·점착 라벨 적용, FTC·EU·이커머스 플랫폼 요건을 정리했습니다. 둥관 TAGE 패키징.",
        desc_fr="Étiquettes pour vêtements imprimés à la demande : limites de lavage du DTG, DTF, sublimation et sérigraphie, rédaction des mentions d'entretien, essais de lavage et étiquettes transfert.",
        desc_es="Etiquetas para prendas estampadas bajo demanda: límites de lavado de DTG, DTF, sublimación y serigrafía, redacción del cuidado, ensayos de lavado y etiquetas de transferencia.",
        crumb_zh="按需印花服装标签",
        crumb_en="Print-on-Demand Apparel Labels",
        crumb_ja="オンデマンドプリントのラベル",
        crumb_ko="온디맨드 프린트 라벨",
        crumb_fr="Étiquettes impression à la demande",
        crumb_es="Etiquetas de impresión bajo demanda",
        h1_zh="按需印花服装的洗水标与吊牌指南：DTG/DTF 与洗护声明",
        h1_en="Print-on-Demand Apparel Labels: Care Claims for DTG and DTF",
        h1_ja="オンデマンドプリント衣料の洗濯表示とタグ：DTG/DTFと洗濯表示",
        h1_ko="온디맨드 프린트 의류의 세탁 라벨과 행택: DTG/DTF와 세탁 표시",
        h1_fr="Étiquettes pour vêtements imprimés à la demande : DTG, DTF et entretien",
        h1_es="Etiquetas para prendas estampadas bajo demanda: DTG, DTF y cuidado",
        tag_zh="电商指南",
        tag_en="E-commerce Guide",
        tag_ja="ECガイド",
        tag_ko="이커머스 가이드",
        tag_fr="Guide e-commerce",
        tag_es="Guía de e-commerce",
        sum_zh="按需印花与一件代发让上新极快，但印花是卖点，洗水标往往才是投诉源头：图案洗后开裂、褪色、发硬，标签上却写着可机洗可烘干。本文用一张表分清 DTG 直喷、DTF 热转印膜、热升华、丝印胶浆与刺绣的耐洗边界，讲清洗护声明必须跟着印料走的四条硬逻辑、洗涤符号的固定顺序，耐洗测试的次数·项目·判定口径（AATCC 61/135、ISO 6330、GB/T 3921/8629）与洗后尺寸的单独约定，热转印标、自粘洗标与空白标打印三种落地方式，以及 FTC、欧盟 GPSR 与电商平台的标签要求与验收清单。",
        sum_en="Print-on-demand and dropshipping make launches fast, but the print is the selling point while the care label is often where complaints start: artwork cracks, fades or stiffens after washing while the label promises machine wash and tumble dry. One table separates the wash limits of DTG, DTF transfer film, sublimation, screen print and embroidery; the guide then sets out the four hard rules that tie a care claim to the decoration, the fixed order of care symbols, wash test cycles and criteria (AATCC 61 and 135, ISO 6330, GB/T 3921 and 8629) with shrinkage agreed separately, the three practical label routes — heat transfer, self-adhesive and blank labels printed in house — plus FTC, EU GPSR and marketplace requirements and an acceptance checklist.",
        sum_ja="オンデマンドプリントと一件代行は新作投入を速くしますが、プリントが売りである一方、クレームの起点は洗濯表示ラベルです。洗濯後に図案が割れ・色褪せ・硬化するのに、ラベルには洗濯機と乾燥機が可能と書かれている。本記事は1つの表でDTG・DTF転写フィルム・昇華・スクリーン・刺繍の耐洗濯限界を整理し、洗濯表示を加飾に合わせる4つの原則、記号の固定順序、耐洗濯試験の回数・項目・判定（AATCC 61/135、ISO 6330、GB/T 3921/8629）と収縮の別途合意、熱転写・粘着・空ラベル印刷という3つの実装方法、FTC・EU GPSR・ECプラットフォームの要件と検収チェックリストを示します。",
        sum_ko="온디맨드 프린트와 드롭시핑은 출시를 빠르게 하지만 프린트가 셀링 포인트인 반면 클레임의 출발점은 세탁 라벨입니다. 세탁 후 도안이 갈라지고 색이 바래고 뻣뻣해지는데 라벨은 세탁기와 건조기 사용이 가능하다고 적혀 있습니다. 이 글은 한 표로 DTG·DTF 전사 필름·승화·스크린·자수의 세탁 한계를 정리하고, 세탁 표시를 가공에 맞추는 네 가지 원칙, 기호의 고정 순서, 세탁 시험 횟수·항목·판정(AATCC 61/135, ISO 6330, GB/T 3921/8629)과 수축 별도 합의, 열전사·점착·빈 라벨 인쇄 세 가지 적용 방식, FTC·EU GPSR·이커머스 플랫폼 요건과 검수 체크리스트를 제시합니다.",
        sum_fr="L'impression à la demande et le dropshipping accélèrent les lancements, mais l'impression est l'argument tandis que l'étiquette d'entretien déclenche souvent la réclamation : le motif craquelle, pâlit ou durcit au lavage alors que l'étiquette promet machine et sèche-linge. Un tableau sépare les limites de lavage du DTG, du film DTF, de la sublimation, de la sérigraphie et de la broderie ; le guide expose ensuite les quatre règles qui lient l'entretien annoncé au procédé, l'ordre fixe des symboles, les cycles et critères d'essai (AATCC 61 et 135, ISO 6330, GB/T 3921 et 8629) avec le retrait convenu à part, les trois voies pratiques — transfert, autocollant et vierges imprimés en interne — puis les exigences FTC, GPSR et plateformes avec une liste de réception.",
        sum_es="La impresión bajo demanda y el dropshipping aceleran los lanzamientos, pero el estampado es el argumento mientras la etiqueta de cuidado origina la reclamación: el motivo se agrieta, se apaga o se endurece al lavar mientras la etiqueta promete máquina y secadora. Una tabla separa los límites de lavado del DTG, el film DTF, la sublimación, la serigrafía y el bordado; la guía expone las cuatro reglas que ligan el cuidado declarado a la técnica, el orden fijo de los símbolos, los ciclos y criterios de ensayo (AATCC 61 y 135, ISO 6330, GB/T 3921 y 8629) con la merma acordada aparte, las tres vías prácticas —transferencia, autoadhesivo y blancos impresos en casa— y los requisitos FTC, GPSR y de plataforma con una lista de recepción.",
    ),
]
