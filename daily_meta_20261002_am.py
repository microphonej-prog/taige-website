#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-02 早上（08:00）每日更新：2 篇新文章元数据（六语：zh-Hant 根 / en / ja / ko / fr / es）

选题说明（30 项主题池与历次扩展选题均已上线，本次沿「校服/幼儿园/团体定制」与
「孕妇装/哺乳装」两个尚未覆盖的品类方向扩展，已核对 blog/、en|ja|ko|fr|es/blog/ 与 sitemap.xml 无重复）：

- school-uniform-trims-label-guide vs uniform-workwear-labeling-guide（后者聚焦工业洗涤与工装耐洗标识）、
  suiting-formalwear-trims-guide（仅在对比表中顺带提到校服一行）、clothing-label-children-safety（儿童安全法规）。
  本文聚焦校服特有的三件事：姓名标方案、校徽织嘜工艺、团体订单的尺码/班级编码与分拣交付。
- maternity-nursing-wear-trims-guide vs underwear-label-guide（内衣贴肤标签通用做法）、
  heat-transfer-labels（热转印工艺本身）、garment-gift-box-packaging（礼盒结构）。
  本文聚焦孕期到产后的尺码跨度、单手操作的功能辅料（哺乳扣/隐藏拉链/调节件行程）与贴肤位置避让。
"""

ARTICLES = [
    dict(
        slug="school-uniform-trims-label-guide.html",
        body="blog/_body_school.html",
        title_zh="校服与幼儿园服装标签指南：姓名标、校徽织嘜与团体分拣 | TAGE",
        title_en="School Uniform Label Guide: Name Tags, Crest Woven Labels &amp; Sorting | TAGE",
        title_ja="学校制服のラベルガイド：名前ラベル・校章織ラベル・団体仕分け | TAGE",
        title_ko="교복 라벨 가이드: 이름표·교표 직조 라벨·단체 분류 | TAGE",
        title_fr="Guide des étiquettes pour uniformes scolaires : nom, écusson tissé et tri | TAGE",
        title_es="Guía de etiquetas para uniformes escolares: nombre, escudo tejido y clasificación | TAGE",
        desc_zh="校服与幼儿园服装标签指南：姓名标、校徽织嘜怎么选，尺码与班级标识怎么编码，耐洗与色牢度按 ISO 6330 写到 60 次，团体订单按班级分拣交付，并附询价要交代的六项信息。东莞泰阁包装。",
        desc_en="Trims for school uniforms and teamwear: name labels, crest woven labels, size and class coding, ISO 6330 wash targets and group-order sorting for OEM brands.",
        desc_ja="学校制服・幼稚園制服・団体カスタム衣料のラベルガイド。名前ラベル、校章織ラベル、サイズとクラスの識別コード設計、ISO 6330 による60回洗濯の耐久目標、団体注文の仕分けと納品、見積り時の6項目を整理しました。東莞泰閣包装。",
        desc_ko="학교 교복과 단체 맞춤 의류 라벨 가이드. 이름표, 교표 직조 라벨, 사이즈와 반 식별 코드 설계, ISO 6330 기준 60회 세탁 내구 목표, 단체 주문 분류와 납품, 견적 6항목을 정리했습니다. 둥관 TAGE 패키징.",
        desc_fr="Guide des étiquettes pour uniformes scolaires : étiquettes nominatives, écussons tissés, codage des tailles et classes, objectif de lavage ISO 6330 et tri des commandes de groupe.",
        desc_es="Guía de etiquetas para uniformes escolares: etiquetas nominativas, escudos tejidos, codificación de tallas y clases, objetivo de lavado ISO 6330 y clasificación de pedidos de grupo.",
        crumb_zh="校服辅料与标签",
        crumb_en="School Uniform Labels",
        crumb_ja="学校制服のラベル",
        crumb_ko="교복 라벨",
        crumb_fr="Étiquettes scolaire",
        crumb_es="Etiquetas escolares",
        h1_zh="校服与幼儿园服装标签指南：姓名标、校徽织嘜与团体分拣",
        h1_en="School Uniform and Kindergarten Labels: Name Tags, Crest Woven Labels and Group Sorting",
        h1_ja="学校制服・幼稚園服のラベルガイド：名前ラベル・校章織ラベル・団体仕分け",
        h1_ko="교복과 유치원복 라벨 가이드: 이름표, 교표 직조 라벨, 단체 분류",
        h1_fr="Étiquettes pour uniformes scolaires et blouses de crèche : nom, écusson tissé et tri de groupe",
        h1_es="Etiquetas para uniformes escolares y batas de guardería: nombre, escudo tejido y clasificación",
        tag_zh="校服与团体", tag_en="Schoolwear", tag_ja="学校制服", tag_ko="교복",
        tag_fr="Scolaire", tag_es="Escolar",
        sum_zh="校服一件一年要洗几十次，还要在几十件同款里认出是谁的。本文把姓名标的三条路线（缝制织嘜、热转印、空白手写）按耐洗、手感与注意事项列成对照表，讲清校徽织嘜的颜色数与细节代价、尺码与班级标识怎么编码、耐洗按 ISO 6330 写到 60 次并附判定标准、团体订单按班级和尺码分拣交付的做法，以及打包前必须确认的补数与同批材料要求。",
        sum_en="A school garment is washed dozens of times a year and has to be identifiable among dozens of identical pieces. This guide tabulates three name-label routes — sewn woven labels, heat transfer and blank write-on tape — by wash life, hand feel and pitfalls, explains what colour count and detail cost on a crest, how to code sizes and class groups, how to state ISO 6330 wash targets to 60 cycles with pass criteria, and how to sort and deliver a group order by class and size.",
        sum_ja="学校制服は年に何十回も洗濯し、同じ型が何十枚も並ぶなかで識別が必要です。本記事は名前ラベルの三方式（縫い付け織ラベル・熱転写・無地手書き）を耐洗濯・風合い・注意点で比較表にし、校章織ラベルの色数と細部のコスト、サイズとクラス識別のコード設計、ISO 6330 で60回までの耐久目標と合否基準、団体注文のクラス別・サイズ別仕分け納品、予備数と同一ロット材の要件をまとめます。",
        sum_ko="교복은 1년에 수십 번 세탁하고, 같은 디자인 수십 장 중에서 누구 것인지 구별해야 합니다. 이 글은 이름표 세 가지 방식(봉제 직조 라벨, 열전사, 공란 필기 테이프)을 세탁 내구성·촉감·주의점으로 비교하고, 교표 직조 라벨의 색상 수와 디테일 비용, 사이즈와 반 식별 코드 설계, ISO 6330 기준 60회 내구 목표와 판정 기준, 단체 주문의 반별·사이즈별 분류 납품, 여유분과 동일 로트 자재 요건을 정리합니다.",
        sum_fr="Un vêtement d'école se lave des dizaines de fois par an et doit rester identifiable parmi des dizaines de pièces identiques. Ce guide compare trois voies d'étiquetage — ruban tissé cousu, transfert thermique, ruban vierge à écrire — en tenue au lavage, toucher et pièges, et traite le coût du nombre de couleurs d'un écusson, la codification des tailles et des classes, les objectifs ISO 6330 jusqu'à 60 cycles, et le tri des commandes de groupe.",
        sum_es="Una prenda escolar se lava decenas de veces al año y debe identificarse entre decenas de piezas idénticas. Esta guía compara tres vías de etiquetado —cinta tejida cosida, transferencia térmica y cinta en blanco para escribir— por resistencia al lavado, tacto y riesgos, y trata el coste del número de colores de un escudo, la codificación de tallas y clases, los objetivos ISO 6330 hasta 60 ciclos y la clasificación de pedidos de grupo.",
    ),
    dict(
        slug="maternity-nursing-wear-trims-guide.html",
        body="blog/_body_maternity.html",
        title_zh="孕妇装与哺乳装辅料指南：无感标签、哺乳扣与尺码设计 | TAGE",
        title_en="Maternity &amp; Nursing Wear Trims: Tagless Labels, Nursing Clips &amp; Sizing | TAGE",
        title_ja="マタニティ・授乳服の副資材ガイド：タグレス・授乳クリップ・サイズ設計 | TAGE",
        title_ko="임부복·수유복 부자재 가이드: 태그리스 라벨·수유 클립·사이즈 설계 | TAGE",
        title_fr="Accessoires maternité et allaitement : sans étiquette, clips et tailles | TAGE",
        title_es="Accesorios de maternidad y lactancia: sin etiqueta, clips y tallas | TAGE",
        desc_zh="孕妇装与哺乳装辅料指南：无感标签与贴肤位置怎么选，哺乳扣、隐藏拉链与调节件的单手操作验证要点，洗涤与残留要求、孕期尺码标注与礼盒细节，并附询价六项。东莞泰阁包装。",
        desc_en="Maternity and nursing wear trims: tagless labels, nursing clips and hidden zips, one-handed testing, wash requirements and gift box details for OEM brands.",
        desc_ja="マタニティ・授乳服の副資材ガイド。タグレス仕様と肌に当たる位置の選び方、授乳クリップ・隠しファスナー・調節具の片手操作検証、洗濯と残留への配慮、マタニティサイズ表記、ギフト包装の要点、見積り時の6項目をまとめました。東莞泰閣包装。",
        desc_ko="임부복·수유복 부자재 가이드. 태그리스 구성과 피부 접촉 위치 선택, 수유 클립·숨은 지퍼·조절구의 한 손 조작 검증, 세탁과 잔류 배려, 임부 사이즈 표기, 선물 포장 요점, 견적 6항목을 정리했습니다. 둥관 TAGE 패키징.",
        desc_fr="Accessoires de maternité et d'allaitement : montages sans étiquette, clips et zips cachés, validation à une main, exigences de lavage, tailles de maternité et emballage cadeau.",
        desc_es="Accesorios de maternidad y lactancia: montajes sin etiqueta, clips y cremalleras ocultas, validación con una mano, requisitos de lavado, tallas y envase de regalo.",
        crumb_zh="孕妇与哺乳装辅料",
        crumb_en="Maternity &amp; Nursing Trims",
        crumb_ja="マタニティ・授乳服",
        crumb_ko="임부복·수유복",
        crumb_fr="Maternité et allaitement",
        crumb_es="Maternidad y lactancia",
        h1_zh="孕妇装与哺乳装辅料指南：无感标签、哺乳扣与尺码设计",
        h1_en="Maternity and Nursing Wear Trims: Tagless Labels, Nursing Clips and Size Design",
        h1_ja="マタニティ・授乳服の副資材ガイド：タグレス、授乳クリップ、サイズ設計",
        h1_ko="임부복·수유복 부자재 가이드: 태그리스 라벨, 수유 클립, 사이즈 설계",
        h1_fr="Accessoires de maternité et d'allaitement : sans étiquette, clips et conception des tailles",
        h1_es="Accesorios de maternidad y lactancia: sin etiqueta, clips de lactancia y diseño de tallas",
        tag_zh="孕妇与哺乳", tag_en="Maternity Wear", tag_ja="マタニティ", tag_ko="임부복",
        tag_fr="Maternité", tag_es="Maternidad",
        sum_zh="孕期到产后的腰围变化可以超过二十厘米，皮肤耐受度下降，还要能单手穿脱——这三点决定了孕妇装与哺乳装辅料的选型。本文给出贴肤标签四种方案的手感与耐洗对照表，讲清哺乳扣的开合力与噪音、隐藏拉链的拉头与齿型、磁扣的磁力衰减与运输限制、调节件要预留的行程，并说明洗涤频率与残留的提醒怎么写、孕期尺码怎么标、礼盒里不该用金属钉的原因。",
        sum_en="A waist that changes by more than twenty centimetres from pregnancy to postnatal, lower skin tolerance and fastening that must work one-handed: those three points decide the trims on maternity and nursing wear. This guide tabulates four skin-contact label options by hand feel and wash life, and covers clip opening force and noise, zip pulls and tooth, magnet decay and transport restrictions, how much travel adjusters need, how to word washing and residue advice, how to mark maternity sizes and why no metal pins belong in a gift box.",
        sum_ja="妊娠期から産後まで20センチ以上変化するウエスト、低下する肌の耐性、片手で着脱できること。この三つがマタニティ・授乳服の副資材選びを決めます。本記事は肌に当たるラベル4方式を風合いと耐洗濯で比較し、授乳クリップの開閉力と音、隠しファスナーの引き手と歯型、マグネットの磁力低下と輸送制限、調節具に必要なストローク、洗濯頻度と残留の注意書き、マタニティサイズの付け方、ギフトボックスに金属ピンを使わない理由をまとめます。",
        sum_ko="임신기부터 산후까지 20cm 이상 변하는 허리둘레, 낮아진 피부 내성, 한 손으로 여닫아야 하는 조건. 이 세 가지가 임부복·수유복 부자재 선택을 결정합니다. 이 글은 피부 접촉 라벨 네 가지를 촉감과 세탁 내구성으로 비교하고, 수유 클립의 개폐 힘과 소음, 숨은 지퍼의 손잡이와 이빨, 자석 단추의 자력 저하와 운송 제한, 조절구에 필요한 가동 범위, 세탁 빈도와 잔류 안내 작성, 임부 사이즈 표기, 선물 상자에 금속 핀을 쓰지 않는 이유를 정리합니다.",
        sum_fr="Une taille qui varie de plus de vingt centimètres entre la grossesse et le post-partum, une tolérance cutanée réduite et une fermeture à manipuler d'une main : ces trois points décident des accessoires. Ce guide compare quatre options d'étiquettes au contact de la peau, et traite la force et le bruit des clips, le tireur et la denture d'un zip, la perte d'aimantation et les restrictions de transport, la course des réglages, la rédaction des consignes de lavage et de résidus, le marquage des tailles et l'absence d'épingles métalliques en coffret.",
        sum_es="Una cintura que varía más de veinte centímetros del embarazo al posparto, menor tolerancia cutánea y un cierre que debe manejarse con una mano: esos tres puntos deciden los accesorios. Esta guía compara cuatro opciones de etiqueta en contacto con la piel y trata la fuerza y el ruido de los clips, el tirador y el diente de la cremallera, la pérdida de magnetismo y las restricciones de transporte, el recorrido de los reguladores, las consignas de lavado y residuos, la marcación de tallas y la ausencia de alfileres metálicos en la caja.",
    ),
]
