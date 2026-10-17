#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-17 本日第三批（14:00）每日更新：2 篇新文章元数据（六语：zh-Hant 根 / en / ja / ko / fr / es）

选题说明（原 30 项主题池连同既有扩展均已上线，本次为全站关键词扫描后的空白点扩展）：

- saree-ethnic-wear-trims-guide.html：纱丽与南亚民族服饰辅料指南。
  关键词扫描：「saree / 纱丽 / fall tape / pico / blouse piece」全站零命中（仅 India 合规页提到 MRP，未讲品类辅料）。
  既有文章分工：印度标签合规页讲法规条目；民族服饰类只有汉服、头巾长袍、校服三篇，
  没有一篇讲纱丽这类「成套+配件」结构下的辅料配置。
  本篇落点：四类辅料清单 → fall 与 pico 两道工序 → blouse piece 标签组套（含规格表）→ 印度/孟加拉/海湾标注重点
  → 折叠、成套与防潮包装 → 相关文章与 CTA。

- garment-trims-trade-show-sourcing-guide.html：服装辅料展会采购（Intertextile/广交会/Texworld）。
  关键词扫描：「Intertextile / Canton Fair / Texworld / Première Vision / Sourcing at MAGIC」全站零命中。
  既有文章分工：采购指南页讲「怎么选供应商」的评估维度，验厂页讲现场看什么；
  没有一篇讲展会这条具体渠道怎么用（三类展会的分工、进馆准备、展位必问清单、展后 30 天跟进）。
  本篇落点：三类展会用途对照表 → 七件必带 → 八个必问问题 → 拿样与报价结构化 → 展后 30 天节奏
  → 线上开发与来厂验厂（虎门厂址，呼应客户逛展顺路验厂）→ CTA。

事实口径（不编造）：不写具体价格与具体展会日期/展馆；纱丽长度写「5.5 米上下、6.3 米长款」这类行业通行区间；
各国标注要求一律写「以目的国现行法规与客户要求为准」；不承诺 MOQ 与打样天数以外的条件（沿用公司口径 3–7 天打样、10–25 天大货）。
"""

ARTICLES = [
    dict(
        slug="saree-ethnic-wear-trims-guide.html",
        body="blog/_body_saree.html",
        title_zh="纱丽与南亚民族服饰辅料指南：fall、pico 与 blouse 标签组套 | TAGE",
        title_en="Saree and South Asian Ethnic Wear Trims Guide: Fall, Pico and Blouse Label Sets | TAGE",
        title_ja="サリーと南アジア民族衣料の副資材ガイド：fall・pico・ブラウス用ラベル | TAGE",
        title_ko="사리·남아시아 민족 의류 부자재 가이드: fall, pico, 블라우스 라벨 | TAGE",
        title_fr="Guide des accessoires de saree et de vêtements ethniques d'Asie du Sud | TAGE",
        title_es="Guía de accesorios para saree y ropa étnica del sur de Asia | TAGE",
        desc_zh="纱丽辅料怎么配才不出退货：fall 衬带的预缩与颜色、pico 包边线与缝线选择、blouse piece 的主嘜洗水标尺码标组套、印度与海湾市场的 MRP 与原产国标注，以及一套一袋的折叠与防潮包装。来自东莞泰阁包装。",
        desc_en="Saree trims guide: fall tape pre-shrinking, pico thread, the blouse label set, MRP and origin marking for India and the Gulf, plus folding and packing.",
        desc_ja="サリー副資材の実務ガイド。fall テープのプリシュランクと色、pico の縫い糸、ブラウスピースのラベル一式、インドと湾岸の MRP・原産地表示、1セット1袋の折り畳みと防湿包装を整理します。東莞泰閣包装。",
        desc_ko="사리 부자재 실무 가이드. fall 테이프 예비 수축과 색상, pico 봉제사, 블라우스 피스 라벨 세트, 인도와 걸프의 MRP·원산지 표시, 한 세트 한 봉투 포장을 정리했습니다. 둥관 TAGE 패키징.",
        desc_fr="Guide des accessoires de saree : prérétrécissement du fall, fil du pico, jeu d'étiquettes de la pièce de blouse, MRP et origine pour l'Inde et le Golfe.",
        desc_es="Guía de accesorios de saree: preencogido del fall, hilo del pico, juego de etiquetas de la blusa, MRP y origen para India y el Golfo, plegado y embalaje.",
        crumb_zh="纱丽辅料指南",
        crumb_en="Saree Trims Guide",
        crumb_ja="サリー副資材ガイド",
        crumb_ko="사리 부자재 가이드",
        crumb_fr="Guide accessoires saree",
        crumb_es="Guía accesorios saree",
        h1_zh="纱丽与南亚民族服饰辅料指南：fall、pico 与 blouse 标签组套",
        h1_en="Saree and South Asian Ethnic Wear Trims: Fall, Pico and Blouse Label Sets",
        h1_ja="サリーと南アジア民族衣料の副資材：fall・pico・ブラウス用ラベル一式",
        h1_ko="사리·남아시아 민족 의류 부자재: fall, pico, 블라우스 라벨 세트",
        h1_fr="Accessoires de saree et de vêtements ethniques d'Asie du Sud",
        h1_es="Accesorios para saree y ropa étnica del sur de Asia",
        tag_zh="品类指南",
        tag_en="Category Guide",
        tag_ja="品目ガイド",
        tag_ko="품목 가이드",
        tag_fr="Guide produit",
        tag_es="Guía de producto",
        sum_zh="一套纱丽要配四类辅料：fall 衬带与 pico 包边决定下摆是否起皱，blouse piece 上的主嘜、洗水标、尺码标与吊牌决定能否上架，MRP 与原产国要三处一致。附规格对照表与成套包装清单。",
        sum_en="A saree set needs four trim families: fall tape and pico decide whether the hem puckers, the blouse label set and hang tag decide shelf-readiness, and MRP plus origin must match in three places.",
        sum_ja="サリー1セットには4種類の副資材が要ります。fall テープと pico が裾の仕上がりを決め、ブラウスピースの主ラベル・洗濯表示・サイズ表示・ハングタグが店頭に並べられるかを決め、MRP と原産地は3か所で一致させます。",
        sum_ko="사리 한 세트에는 네 가지 부자재가 필요합니다. fall 테이프와 pico가 밑단 상태를 좌우하고, 블라우스 피스의 메인 라벨·세탁 라벨·사이즈 라벨·행택이 진열 가능 여부를 결정하며, MRP와 원산지는 세 곳에서 일치해야 합니다.",
        sum_fr="Un ensemble saree exige quatre familles d'accessoires : le fall et le pico décident du tombé du bas, le jeu d'étiquettes et l'étiquette suspendue décident de la mise en rayon, et MRP et origine doivent concorder en trois endroits.",
        sum_es="Un conjunto de saree necesita cuatro familias de accesorios: fall y pico deciden el bajo, el juego de etiquetas y el colgante deciden si se puede poner en tienda, y MRP y origen deben coincidir en tres sitios.",
    ),
    dict(
        slug="garment-trims-trade-show-sourcing-guide.html",
        body="blog/_body_tradeshow.html",
        title_zh="服装辅料展会采购指南：Intertextile、广交会与 Texworld 怎么逛 | TAGE",
        title_en="Trims Trade Show Sourcing Guide: Intertextile, Canton Fair and Texworld | TAGE",
        title_ja="副資材の見本市活用ガイド：Intertextile・Canton Fair・Texworld の歩き方 | TAGE",
        title_ko="부자재 전시회 소싱 가이드: Intertextile, 캔톤페어, 텍스월드 활용법 | TAGE",
        title_fr="Guide des salons d'accessoires : Intertextile, Foire de Canton, Texworld | TAGE",
        title_es="Guía de ferias de accesorios: Intertextile, Feria de Cantón y Texworld | TAGE",
        desc_zh="逛服装辅料展会怎么不白跑：三类展会各自的用途、进馆前必带的七样东西、展位上的八个必问问题、拿样与报价的结构化记录法、展后 30 天跟进节奏，以及线上开发与来厂验厂的配合。含展会类型对照表与虎门看厂路线。来自东莞泰阁包装。",
        desc_en="How to work a trims trade show: what each show type is for, seven things to bring, eight booth questions, sampling notes and a 30-day follow-up rhythm.",
        desc_ja="副資材の見本市を無駄にしないための実務ガイド。3種類の見本市の役割、持ち物7点、ブースでの質問8つ、サンプルと見積の記録法、終了後30日のフォロー、オンライン開拓と工場訪問までを整理します。東莞泰閣包装。",
        desc_ko="부자재 전시회를 헛걸음하지 않는 방법. 세 가지 전시회 유형의 역할, 챙길 일곱 가지, 부스에서 물어야 할 여덟 가지, 샘플·견적 기록법, 전시 후 30일 팔로업, 온라인 소싱과 공장 방문까지 정리했습니다.",
        desc_fr="Réussir un salon d'accessoires : usage de chaque type de salon, sept choses à emporter, huit questions sur le stand, prise de notes et relance sur 30 jours.",
        desc_es="Aprovechar una feria de accesorios: para qué sirve cada tipo, siete cosas que llevar, ocho preguntas en el stand, registro de muestras y 30 días de seguimiento.",
        crumb_zh="辅料展会采购",
        crumb_en="Trims Trade Show Sourcing",
        crumb_ja="見本市での副資材調達",
        crumb_ko="전시회 부자재 소싱",
        crumb_fr="Sourcing en salon",
        crumb_es="Compras en feria",
        h1_zh="服装辅料展会采购指南：Intertextile、广交会与 Texworld 怎么逛、怎么谈、怎么跟进",
        h1_en="Trims Trade Show Sourcing: How to Walk Intertextile, Canton Fair and Texworld",
        h1_ja="副資材の見本市活用ガイド：Intertextile・Canton Fair・Texworld の歩き方と交渉",
        h1_ko="부자재 전시회 소싱 가이드: Intertextile·캔톤페어·텍스월드를 걷는 법",
        h1_fr="Sourcing d'accessoires en salon : parcourir Intertextile, la Foire de Canton et Texworld",
        h1_es="Compras de accesorios en feria: recorrer Intertextile, Feria de Cantón y Texworld",
        tag_zh="采购实务",
        tag_en="Sourcing Practice",
        tag_ja="調達実務",
        tag_ko="소싱 실무",
        tag_fr="Pratique d'achat",
        tag_es="Práctica de compra",
        sum_zh="展会不是拿报价的地方，而是筛供应商的第一轮：三类展会各解决什么问题、进馆带什么、展位上必须问清哪八件事、样品与报价怎么结构化记录、展后 30 天怎么跟，以及逛完展顺路来虎门看产线。",
        sum_en="A show is round one of supplier screening, not a place to collect quotes: what each show type solves, what to bring, eight questions to ask, how to record samples and quotes, and a 30-day follow-up rhythm.",
        sum_ja="見本市は見積を集める場ではなく、取引先ふるい分けの第一輪です。3種類の役割、持ち物、ブースで聞く8項目、サンプルと見積の記録法、終了後30日のフォロー、そして見学後に虎門で産線を見る段取りまで。",
        sum_ko="전시회는 견적을 모으는 곳이 아니라 공급사 1차 필터입니다. 세 유형의 역할, 챙길 것, 부스에서 물을 여덟 항목, 샘플·견적 기록법, 전시 후 30일 팔로업, 그리고 후먼 공장 방문까지.",
        sum_fr="Un salon est le premier tour de sélection, pas une collecte de devis : usage de chaque type, quoi emporter, huit questions, prise de notes structurée et relance sur 30 jours.",
        sum_es="Una feria es la primera ronda de selección, no una colecta de cotizaciones: uso de cada tipo, qué llevar, ocho preguntas, registro estructurado y 30 días de seguimiento.",
    ),
]
