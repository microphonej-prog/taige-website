#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-06 上午批次（08:00）每日更新：2 篇新文章元数据（六语：zh-Hant 根 / en / ja / ko / fr / es）

选题说明（主题池 30 项与历次扩展均已上线；本次沿「零售防损」与「成衣染色/后水洗」两个
尚未独立成文的方向扩展，已核对 blog/、en|ja|ko|fr|es/blog/ 与 sitemap.xml 无重复，并 grep 全站确认：

- garment-security-tag-guide  vs rfid-garment-labels（只在一段里点出 EAS 与 RFID 是两套系统）、
  hang-tag-metal-hardware-guide（第 4 节只讲别针与防盗件的位置）、hang-tag-anti-counterfeiting（讲防伪不报警）；
  全站无「EAS / 防盗标签 / 声磁 / 墨水标」专文（grep 防盗 仅 2 处、声磁 0 处、防损 0 处）：
  本文讲清 EAS 与 RFID 的分工、硬标/软标/墨水标三类对比、58 kHz 声磁与 8.2 MHz 射频与门店防盗门的匹配、
  源标签在工厂端的安装位置与固定方式（避开压烫与涂层、童装与内衣注意点），并给出检测距离、耐久、
  镍释放与点数留样等验收口径与询价清单。
- garment-wash-dye-trims-guide  vs denim-garment-trims-guide（专讲牛仔石磨/酵素洗与皮标）、
  care-label-wash-durability（只讲洗水标自身耐久）、woven-label-material-guide（材质本身）、
  trim-ironing-heat-resistance-guide（熨烫耐热）；
  全站无「成衣染色（garment dye）挂牌时机」专文（成衣染色 0 处、水洗工艺 0 处）：
  本文面向针织、棉麻与真丝的成衣染色与柔软洗，讲清工艺的四种破坏方式、洗前/洗中/洗后三个挂牌
  时机的取舍、六类材质耐受对照表、深色面料缝线不上色与洗后缝标位置等要点，并给出随洗测试、
  工艺参数、备品与交期联动的验收口径。
"""

ARTICLES = [
    dict(
        slug="garment-security-tag-guide.html",
        body="blog/_body_secutag.html",
        title_zh="服装零售防盗标签指南：EAS 硬标、软标与墨水标怎么选 | TAGE",
        title_en="Garment Security Tag Guide: EAS Hard Tags, Soft Labels and Ink Tags | TAGE",
        title_ja="衣料品の万引き防止タグガイド：EAS ハードタグ・ソフトタグ・インクタグの選び方 | TAGE",
        title_ko="의류 도난 방지 태그 가이드: EAS 하드 태그·소프트 라벨·잉크 태그 선택 | TAGE",
        title_fr="Guide des étiquettes antivol EAS : pastille dure, souple ou à encre | TAGE",
        title_es="Guía de etiquetas antirrobo EAS: placa dura, blanda o de tinta | TAGE",
        desc_zh="服装零售防盗标签（EAS）指南：讲清防盗报警与 RFID 盘库为何是两套系统，对比声磁硬标、射频软标与墨水标的适用品类与限制，说明 58 kHz 与 8.2 MHz 如何匹配门店防盗门、源标签在工厂端的安装位置，并给出检测距离与验收口径。",
        desc_en="EAS security tag guide: anti-theft alarms and RFID counting differ, AM hard tags vs RF soft labels vs ink tags, 58 kHz gate matching and factory source tagging.",
        desc_ja="衣料品の万引き防止タグ（EAS）ガイド。盗難警報と RFID 棚卸が別系統である理由、音響磁気式ハードタグ・RF ソフトタグ・インクタグの比較、58 kHz と 8.2 MHz のゲート整合、工場でのソースタギングの取付位置、検出距離と適合性の検収基準を解説。東莞泰閣包装。",
        desc_ko="의류 도난 방지 태그(EAS) 가이드. 도난 경보와 RFID 재고 실사가 다른 시스템인 이유, 음향자기식 하드 태그·RF 소프트 라벨·잉크 태그 비교, 58kHz와 8.2MHz 게이트 매칭, 공장 소스 태깅 위치, 검출 거리와 규정 검수 기준을 정리했습니다. 둥관 TAGE 패키징.",
        desc_fr="Guide des étiquettes antivol EAS : alarme et inventaire RFID sont deux systèmes distincts, pastille dure AM, étiquette souple RF et pastille à encre, accord 58 kHz et pose en usine.",
        desc_es="Guía de etiquetas antirrobo EAS: la alarma y el inventario RFID son dos sistemas, placa dura AM, etiqueta blanda RF y placa de tinta, ajuste a 58 kHz y colocación en fábrica.",
        crumb_zh="防盗标签指南",
        crumb_en="Security Tag Guide",
        crumb_ja="防盗タグガイド",
        crumb_ko="보안 태그 가이드",
        crumb_fr="Guide antivol",
        crumb_es="Guía antirrobo",
        h1_zh="服装零售防盗标签指南：EAS 硬标、软标与墨水标怎么选",
        h1_en="Garment Security Tag Guide: EAS Hard Tags, Soft Labels and Ink Tags",
        h1_ja="衣料品の万引き防止タグガイド：EAS ハードタグ・ソフトタグ・インクタグの選び方",
        h1_ko="의류 도난 방지 태그 가이드: EAS 하드 태그, 소프트 라벨, 잉크 태그 선택",
        h1_fr="Étiquettes antivol EAS : pastille dure, étiquette souple ou pastille à encre",
        h1_es="Etiquetas antirrobo EAS: placa dura, etiqueta blanda o placa de tinta",
        tag_zh="零售防损",
        tag_en="Loss Prevention",
        tag_ja="店舗ロス対策",
        tag_ko="매장 손실 방지",
        tag_fr="Antivol",
        tag_es="Antirrobo",
        sum_zh="门店损耗里最容易被忽略、又最直接决定失窃率的一环，就是防盗标签（EAS）。本文讲清 EAS 与 RFID 的分工，对比声磁硬标、射频软标与墨水标的工作原理、适用品类与限制，说明 58 kHz 声磁与 8.2 MHz 射频如何与门店防盗门匹配、源标签在工厂端的安装位置与固定方式，并给出检测距离、耐久、金属件合规、点数留样等验收口径与一份可直接复制进询价邮件的清单。",
        sum_en="EAS tags are the most overlooked part of store loss prevention and they move shrinkage directly. This guide separates EAS from RFID, compares AM hard tags, RF soft labels and ink tags, explains 58 kHz and 8.2 MHz gate matching and factory source tagging, then closes with detection distance, durability, metal compliance and acceptance criteria you can paste into a quotation request.",
        sum_ja="EAS タグは店舗ロス対策で最も見落とされやすく、盗難率を直接左右します。本記事は EAS と RFID の役割を分け、音響磁気式ハードタグ・RF ソフトタグ・インクタグを比較、58 kHz と 8.2 MHz のゲート整合と工場でのソースタギングを解説し、最後に検出距離・耐久性・金属部品の適合性・数量確認の検収基準と見積依頼に使えるリストを示します。",
        sum_ko="EAS 태그는 매장 손실 방지에서 가장 간과되면서 도난률을 직접 좌우합니다. 이 글은 EAS와 RFID의 역할을 구분하고 음향자기식 하드 태그, RF 소프트 라벨, 잉크 태그를 비교하며, 58kHz와 8.2MHz 게이트 매칭과 공장 소스 태깅을 설명한 뒤 검출 거리, 내구성, 금속 부품 규정, 수량 확인 등 검수 기준과 견적 요청서용 목록을 제시합니다.",
        sum_fr="Les pastilles EAS sont le maillon le plus négligé de la lutte contre la démarque et pèsent directement dessus. Ce guide sépare EAS et RFID, compare pastille dure AM, étiquette souple RF et pastille à encre, explique l'accord 58 kHz et 8,2 MHz et le source tagging en usine, puis les critères de distance, durabilité, conformité métal et réception.",
        sum_es="Las placas EAS son el eslabón más olvidado de la prevención de pérdidas y mueven la merma directamente. Esta guía separa EAS de RFID, compara placa dura AM, etiqueta blanda RF y placa de tinta, explica el ajuste a 58 kHz y 8,2 MHz y el source tagging en fábrica, y cierra con distancia, durabilidad, cumplimiento del metal y recepción.",
    ),
    dict(
        slug="garment-wash-dye-trims-guide.html",
        body="blog/_body_washdye.html",
        title_zh="成衣染色与水洗工艺下的辅料指南：挂牌时机与材质耐受 | TAGE",
        title_en="Garment Dye and Wash Trims Guide: When to Attach Tags, Which Materials Survive | TAGE",
        title_ja="製品染色・ウォッシュ工程の副資材ガイド：取付タイミングと素材耐性 | TAGE",
        title_ko="제품 염색·워시 공정 부자재 가이드: 부착 시기와 소재 내성 | TAGE",
        title_fr="Guide des accessoires en teinture en pièce et lavage : quand poser les étiquettes | TAGE",
        title_es="Guía de accesorios en teñido en prenda y lavado: cuándo colocar las etiquetas | TAGE",
        desc_zh="成衣染色与水洗工艺下的辅料指南：讲清 60–95 °C 水温、酸碱酶与滚筒摩擦如何破坏吊牌、织唛与洗水标，对比洗前、洗中临时标与洗后挂牌三种时机的取舍，并给出六类材质的耐受对照与随洗测试的验收口径。",
        desc_en="Garment dye and wash trims guide: how 60–95 °C water, pH, enzymes and tumbling damage tags and labels, with three attachment timings and a tolerance table.",
        desc_ja="製品染色・ウォッシュ工程の副資材ガイド。60～95 °C の水温・薬剤・酵素・ドラム摩擦がタグやネーム、洗濯表示に与える影響、洗濯前・洗濯中の仮タグ・洗濯後の3つの取付タイミングの比較、素材別の耐性一覧と検収基準を解説。東莞泰閣包装。",
        desc_ko="제품 염색·워시 공정 부자재 가이드. 60~95°C 수온과 약제·효소·드럼 마찰이 행택·직조 라벨·세탁 라벨에 미치는 영향, 세탁 전·세탁 중 임시 라벨·세탁 후의 세 가지 부착 시기 비교, 소재별 내성표와 검수 기준을 정리했습니다. 둥관 TAGE 패키징.",
        desc_fr="Guide des accessoires en teinture en pièce et lavage : comment 60–95 °C, pH, enzymes et tambour abîment étiquettes et labels, comparaison des trois moments de pose et tableau de tenue des matières.",
        desc_es="Guía de accesorios en teñido en prenda y lavado: cómo 60–95 °C, pH, enzimas y tambor dañan etiquetas, comparación de los tres momentos de colocación y tabla de tolerancia por material.",
        crumb_zh="成衣染色与水洗辅料",
        crumb_en="Garment Dye and Wash Trims",
        crumb_ja="製品染色・ウォッシュ副資材",
        crumb_ko="제품 염색·워시 부자재",
        crumb_fr="Accessoires teinture et lavage",
        crumb_es="Accesorios teñido y lavado",
        h1_zh="成衣染色与水洗工艺下的辅料指南：挂牌时机与材质耐受",
        h1_en="Garment Dye and Wash Trims Guide: Attachment Timing and Material Tolerance",
        h1_ja="製品染色・ウォッシュ工程の副資材ガイド：取付タイミングと素材耐性",
        h1_ko="제품 염색·워시 공정 부자재 가이드: 부착 시기와 소재 내성",
        h1_fr="Accessoires en teinture en pièce et lavage : moment de pose et tenue des matières",
        h1_es="Accesorios en teñido en prenda y lavado: momento de colocación y tolerancia de materiales",
        tag_zh="工艺指南",
        tag_en="Process Guide",
        tag_ja="加工ガイド",
        tag_ko="공정 가이드",
        tag_fr="Guide des procédés",
        tag_es="Guía de procesos",
        sum_zh="成衣染色与后水洗把吊牌、织唛与洗水标推进了一个比家用洗涤苛刻得多的环境：60–95 °C 水温、酸碱与酶、滚筒摩擦与高速脱水。本文讲清工艺的四种破坏方式，对比洗前挂牌、洗中临时标与洗后挂牌三种时机的取舍，给出六类材质的耐受对照表，说明深色面料缝线不上色、洗后缝标位置等要点，并给出随洗测试、工艺参数、备品与交期联动的验收口径。",
        sum_en="Garment dyeing and post-wash push hang tags, woven labels and care labels into a far harsher environment than a home wash: 60–95 °C water, acids and alkalis, enzymes, tumbling and fast spinning. This guide sets out four failure modes, compares attaching before, during and after the bath, gives a six-material tolerance table, covers white stitching on dark fabric and post-wash label placement, and closes with test, parameter and spare-stock criteria.",
        sum_ja="製品染色と後加工のウォッシュは、タグ・ネーム・洗濯表示ラベルを家庭洗濯よりはるかに過酷な環境に置きます。60～95 °C の水温、酸とアルカリ、酵素、ドラム摩擦と高速脱水です。本記事は4つの破壊要因、洗濯前・洗濯中・洗濯後という3つの取付タイミングの比較、6素材の耐性一覧、濃色生地の白い縫い糸や縫い直し位置の注意、実浴試験と検収基準までを扱います。",
        sum_ko="제품 염색과 후가공 워시는 행택, 직조 라벨, 세탁 라벨을 가정 세탁보다 훨씬 가혹한 환경에 놓습니다. 60~95°C 수온, 산과 알칼리, 효소, 드럼 마찰과 고속 탈수입니다. 이 글은 네 가지 파괴 요인, 세탁 전·중·후 부착 시기 비교, 여섯 소재 내성표, 진한 원단의 흰 봉제선과 재봉 위치 주의, 실배스 시험과 검수 기준을 다룹니다.",
        sum_fr="La teinture en pièce et les lavages de finition placent étiquettes et labels dans un milieu bien plus dur qu'un lavage domestique : 60–95 °C, acides et bases, enzymes, tambour et essorage. Ce guide expose quatre modes de défaillance, compare la pose avant, pendant et après le bain, fournit un tableau de six matières, traite du fil blanc sur tissu foncé et de la repose des labels, puis les critères d'essai et de réception.",
        sum_es="El teñido en prenda y los lavados de acabado sitúan etiquetas y labels en un entorno mucho más duro que un lavado doméstico: 60–95 °C, ácidos y álcalis, enzimas, tambor y centrifugado. Esta guía expone cuatro modos de fallo, compara colocar antes, durante y después del baño, ofrece una tabla de seis materiales, trata el hilo blanco en tejido oscuro y la recolocación, y cierra con ensayos y recepción.",
    ),
]
