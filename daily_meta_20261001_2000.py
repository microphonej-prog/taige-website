#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-01 晚上（20:00）每日更新：2 篇新文章元数据（六语：zh-Hant 根 / en / ja / ko / fr / es）

选题：主题池 30 项与历次扩展选题均已上线，本次沿「吊牌印刷特殊效果工艺」与
「防水/防雨服装辅料配置」两个方向扩展。已核对 blog/、en|ja|ko|fr|es/blog/ 与 sitemap.xml 无重复，
并与既有文章主题区分明确：
- hang-tag-special-effects-guide vs hang-tag-lamination-guide / hang-tag-ink-safety-guide /
  hang-tag-foil-stamping-guide / hang-tag-embossing-guide（既有四篇分别讲覆膜、油墨安全、
  烫金、压凹凸，均不涉及蓄光/温变/紫外荧光/香味/触感等特殊效果油墨与实现路径）
- rainwear-waterproof-garment-trims-guide vs outerwear-down-jacket-trims-guide（羽绒/保暖外套的
  承重与警示）、swimwear-activewear-trims-guide（泳装耐氯与运动弹力标）
"""

ARTICLES = [
    dict(
        slug="hang-tag-special-effects-guide.html",
        body="blog/_body_effects.html",
        title_zh="吊牌特殊效果工艺指南：夜光、温变、光变与香味油墨怎么选 | TAGE",
        title_en="Special-Effect Hang Tags: Glow, Thermochromic, UV and Scented Inks | TAGE",
        title_ja="ハンガータグの特殊効果ガイド：蓄光・感温・紫外蛍光・香りインキの選び方 | TAGE",
        title_ko="행택 특수 효과 가이드: 축광·온도 변색·자외선·향 잉크 선택 | TAGE",
        title_fr="Étiquettes suspendues à effets spéciaux : phosphorescent, thermochrome, UV, parfumé | TAGE",
        title_es="Etiquetas colgantes con efectos especiales: fosforescente, termocromático, UV y perfumado | TAGE",
        desc_zh="吊牌特殊效果工艺指南：对比夜光蓄光、温变热敏、紫外荧光、香味微胶囊与触感局部光油五类效果的触发方式、寿命与成本；讲清丝印专色、胶印连线、数码三条实现路径的边界，纸张与覆膜配合、套准留量与迁移合规检查，附询价六项。来自东莞泰阁包装。",
        desc_en="Special-effect hang tags compared: glow in the dark, thermochromic, UV-reactive, scented and soft touch, with screen, offset and digital routes and print tests.",
        desc_ja="ハンガータグの特殊効果ガイド。蓄光・感温変色・紫外蛍光・香り・触感と部分ニスの5種を、反応条件・寿命・コストで比較。シルク特色・オフセット・デジタルの使い分け、紙とラミネートの組み合わせ、見当余裕、移行とコンプライアンス、見積り時の6項目をまとめました。東莞泰閣包装。",
        desc_ko="행택 특수 효과 가이드. 축광, 온도 변색, 자외선 형광, 향 마이크로캡슐, 촉각과 부분 바니시 다섯 가지를 반응 조건·수명·비용으로 비교하고, 실크 별색·옵셋·디지털 경로, 종이와 라미네이트 조합, 겹침 여유, 이동과 규제, 견적 6항목을 정리했습니다. 둥관 TAGE 패키징.",
        desc_fr="Effets spéciaux sur étiquettes suspendues : phosphorescent, thermochrome, UV, parfumé et soft touch comparés en déclencheur, durée et coût, avec les voies sérigraphie, offset et numérique.",
        desc_es="Efectos especiales en etiquetas colgantes: fosforescente, termocromático, UV, perfumado y soft touch comparados por activación, duración y coste, con las vías de serigrafía, offset y digital.",
        crumb_zh="吊牌特殊效果工艺",
        crumb_en="Special Effect Hang Tags",
        crumb_ja="ハンガータグの特殊効果",
        crumb_ko="행택 특수 효과",
        crumb_fr="Effets spéciaux sur étiquettes",
        crumb_es="Efectos especiales en etiquetas",
        h1_zh="吊牌特殊效果工艺指南：夜光、温变、光变与香味怎么选",
        h1_en="Special-Effect Hang Tags: Choosing Between Glow, Thermochromic, UV and Scented Finishes",
        h1_ja="ハンガータグの特殊効果ガイド：蓄光・感温変色・紫外蛍光・香りの選び方",
        h1_ko="행택 특수 효과 가이드: 축광·온도 변색·자외선·향 중 선택",
        h1_fr="Étiquettes suspendues à effets spéciaux : choisir entre phosphorescent, thermochrome, UV et parfumé",
        h1_es="Etiquetas colgantes con efectos especiales: elegir entre fosforescente, termocromático, UV y perfumado",
        tag_zh="吊牌工艺", tag_en="Hang Tag Printing", tag_ja="タグ印刷", tag_ko="행택 인쇄",
        tag_fr="Impression d'étiquettes", tag_es="Impresión de etiquetas",
        sum_zh="夜光、温变、紫外荧光、香味与触感五类特殊效果，卖的是被记住的两秒，代价是版费、工序与效果衰减。本文把五类效果的触发方式、寿命与适用场景列成对照表，讲清丝印专色、胶印连线与数码三条路径各自能做与不能做，深色底打白、覆膜顺序、效果避开折线与孔位等配合要点，并给出摩擦、日晒、迁移与儿童品合规的检查清单和询价必须交代的六项信息。",
        sum_en="Glow, thermochromic, UV, scented and tactile finishes sell two memorable seconds and cost plate charges, extra passes and decay. This guide tabulates the trigger, lifetime and best use of each of the five effects, explains what screen, offset and digital can and cannot do, and covers white underlays, lamination order, keeping effects off folds and holes, plus rub, light, migration and children's-product checks with six items to bring to a quote.",
        sum_ja="蓄光・感温・紫外蛍光・香り・触感の5種は「記憶に残る2秒」を買うもので、製版代・追い刷り・効果の劣化が代償です。本記事は5種の反応条件・寿命・用途を表で比較し、シルク特色・オフセット・デジタルの可否、白下地、ラミネート順、折り線と穴の回避、摩擦・日光・移行・子供向けコンプライアンスの確認項目、見積り時の6項目をまとめます。",
        sum_ko="축광, 온도 변색, 자외선 형광, 향, 촉각 다섯 가지는 기억되는 2초를 사는 대신 제판비, 추가 공정, 효과 열화를 치릅니다. 이 글은 다섯 효과의 반응 조건·수명·용도를 표로 비교하고 실크 별색·옵셋·디지털의 가능과 한계, 흰색 하지, 라미네이트 순서, 접힘선과 구멍 회피, 마찰·햇빛·이동·아동 제품 점검, 견적 6항목을 정리합니다.",
        sum_fr="Phosphorescent, thermochrome, UV, parfumé et tactile achètent deux secondes mémorables et coûtent gravures, passes et dégradation. Ce guide compare déclencheur, durée et usage des cinq effets, précise ce que sérigraphie, offset et numérique savent faire, et traite blanc de fond, ordre de lamination, évitement des plis et des trous, essais de frottement, de lumière, de migration et conformité enfants.",
        sum_es="Fosforescente, termocromático, UV, perfumado y táctil compran dos segundos memorables y cuestan planchas, pasadas y degradación. Esta guía compara activación, duración y uso de los cinco efectos, aclara qué pueden hacer serigrafía, offset y digital, y cubre blanco de fondo, orden de laminado, evitar pliegues y agujeros, ensayos de roce, luz, migración y cumplimiento infantil.",
    ),
    dict(
        slug="rainwear-waterproof-garment-trims-guide.html",
        body="blog/_body_rainwear.html",
        title_zh="防水与防雨服装辅料指南：洗水标、主唛与吊牌怎么配 | TAGE",
        title_en="Waterproof and Rainwear Garment Trims: Care Labels, Neck Labels and Tags | TAGE",
        title_ja="防水・防雨衣料の副資材ガイド：洗濯ラベル・メインラベル・タグの選び方 | TAGE",
        title_ko="방수·방우 의류 부자재 가이드: 세탁 라벨·메인 라벨·행택 선택 | TAGE",
        title_fr="Accessoires pour vêtements imperméables et de pluie : étiquettes et tags | TAGE",
        title_es="Accesorios para prendas impermeables y de lluvia: etiquetas y colgantes | TAGE",
        desc_zh="防水服装辅料指南：涂层与层压面料下洗水标、主唛怎么选，五类载体的吸水性与压胶相容性对比，避开压胶条与针孔渗水的缝制要点，洗护符号与拒水保养文案、吊牌功能宣称的依据、防潮包装与询价六项。东莞泰阁包装。",
        desc_en="Trims for waterproof and rainwear garments: care and neck label materials, needle-free attachment, seam tape avoidance, care symbols and tag claims.",
        desc_ja="防水・防雨衣料の副資材ガイド。コーティング・ラミネート生地での洗濯ラベルとメインラベルの選び方、5種媒体の吸水性とシームテープ相性、針穴とシーム破りを避ける縫製、ケア表示と撥水ケアの文案、機能表示の根拠、防湿包装、見積り時の6項目をまとめました。東莞泰閣包装。",
        desc_ko="방수·방우 의류 부자재 가이드. 코팅·라미네이트 원단에서 세탁 라벨과 메인 라벨 선택, 다섯 매체의 흡수성과 심 테이프 궁합, 바늘 구멍 회피 봉제, 세탁 표시와 발수 관리 문구, 기능 표시 근거, 방습 포장, 견적 6항목을 정리했습니다. 둥관 TAGE 패키징.",
        desc_fr="Accessoires de vêtements imperméables : choix des étiquettes d'entretien et de col, compatibilité avec les rubans thermocollés, couture sans perforation, symboles et allégations.",
        desc_es="Accesorios para prendas impermeables: elección de etiquetas de cuidado y cuello, compatibilidad con cintas de sellado, costura sin perforación, símbolos y alegaciones.",
        crumb_zh="防水服装辅料",
        crumb_en="Waterproof Garment Trims",
        crumb_ja="防水衣料の副資材",
        crumb_ko="방수 의류 부자재",
        crumb_fr="Accessoires imperméables",
        crumb_es="Accesorios impermeables",
        h1_zh="防水与防雨服装辅料指南：洗水标、主唛与吊牌怎么配",
        h1_en="Waterproof and Rainwear Garment Trims: Care Labels, Neck Labels and Hang Tags",
        h1_ja="防水・防雨衣料の副資材ガイド：洗濯ラベル・メインラベル・タグの選び方",
        h1_ko="방수·방우 의류 부자재 가이드: 세탁 라벨, 메인 라벨, 행택 구성",
        h1_fr="Accessoires pour vêtements imperméables et de pluie : étiquettes d'entretien, de col et suspendues",
        h1_es="Accesorios para prendas impermeables y de lluvia: etiquetas de cuidado, de cuello y colgantes",
        tag_zh="户外品类", tag_en="Outdoor Category", tag_ja="アウトドアカテゴリ", tag_ko="아웃도어 카테고리",
        tag_fr="Catégorie outdoor", tag_es="Categoría outdoor",
        sum_zh="防水服装的辅料要在三件事上过关：标签不吸水、缝制不留针孔、压胶条不被扎破。本文把涂层织带、涤纶缎面、热转印、无纺与纸质五类载体的吸水性与压胶相容性列成对照表，给出标签位置与非针孔固定方案，说明洗护符号与拒水保养文案怎么写、吊牌上的静水压与透湿宣称怎样用测试方法支撑，以及防潮包装与询价六项。",
        sum_en="Waterproof garment trims have to pass three tests: the label must not absorb water, stitching must not leave needle holes, and seam tape must not be pierced. This guide tabulates five carriers by absorption and tape compatibility, sets out placement and needle-free attachment, explains how to word care symbols and water-repellent maintenance, how to back a hydrostatic head or breathability claim with a test method, and how to pack and enquire.",
        sum_ja="防水衣料の副資材は三つの条件を満たす必要があります。ラベルが水を吸わないこと、縫製が針穴を残さないこと、シームテープを破らないことです。本記事はコーティング織テープ・サテン・熱転写・不織布・紙の5種を吸水性とテープ相性で比較し、位置と針穴なし固定、ケア表示と撥水ケアの文案、耐水圧・透湿表示の根拠づけ、防湿包装と見積り時の6項目をまとめます。",
        sum_ko="방수 의류 부자재는 세 가지를 통과해야 합니다. 라벨이 물을 먹지 않고, 봉제가 바늘 구멍을 남기지 않으며, 심 테이프가 뚫리지 않아야 합니다. 이 글은 코팅 직조 테이프, 새틴, 열전사, 부직포, 종이 다섯 매체를 흡수성과 테이프 궁합으로 비교하고, 위치와 무바늘 고정, 세탁 표시와 발수 관리 문구, 내수압·투습 표시의 근거, 방습 포장과 견적 6항목을 정리합니다.",
        sum_fr="Les accessoires d'un vêtement imperméable doivent réussir trois épreuves : une étiquette qui n'absorbe pas, une couture sans trou d'aiguille et un ruban d'étanchéité intact. Ce guide compare cinq supports par absorption et compatibilité, détaille position et fixation sans aiguille, la rédaction des symboles et de l'entretien déperlant, la justification d'une allégation de colonne d'eau ou de respirabilité, et l'emballage anti-humidité.",
        sum_es="Los accesorios de una prenda impermeable deben pasar tres pruebas: etiqueta que no absorba agua, costura sin agujeros de aguja y cinta de sellado intacta. Esta guía compara cinco soportes por absorción y compatibilidad, detalla posición y fijación sin aguja, la redacción de símbolos y del mantenimiento repelente, cómo respaldar una alegación de columna de agua o transpirabilidad y el embalaje antihumedad.",
    ),
]
