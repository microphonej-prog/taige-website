#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-09-29 上午批次文章元数据（六语：zh-Hant 根 / en / ja / ko / fr / es）。

选题说明：任务主题池 30 个选题均已上线（含此前批次扩展的国别合规、EUDR/PPWR、
原产地标识、产前样、出货方式、数量容差等）。本次沿「打样确认方式」与「辅料资产化
管理」两个方向扩展新选题，已核对 blog/ 全量文件、en|ja|ko|fr|es/blog/ 与 sitemap.xml：

- 数字化打样（trim-digital-sampling-3d）：全站检索「数字化打样」「虚拟样衣」「CLO」
  命中 0 次；现有 trim-pre-production-sample-guide 讲打样/产前样/首件的区别，
  garment-trims-sampling-process 讲打样流程，均未涉及数码稿与 3D 渲染如何与实物样
  配合、渲染图不能替代实物样的六个参数。属明显空白。

- 编码与版库标准化（trim-coding-standardization）：检索「物料编码」「料号」「版库」
  命中 0 次；现有 apparel-trims-spec-sheet-guide 讲规格书字段，
  trim-tooling-ownership-guide 讲版费权属，garment-trims-inventory-management 讲库存，
  都没有讲「怎么给辅料编号、台账登什么、色卡库怎么建、编码怎么落进订单」，
  与上述三篇互补而非重复。
"""

ARTICLES = [
    dict(
        slug="trim-digital-sampling-3d.html",
        body="blog/_body_digital.html",
        title_zh="服装辅料数字化打样：3D 虚拟样衣与数码稿怎么确认 | TAGE",
        title_en="Digital Sampling for Trims: 3D Virtual Garments and Digital Proofs | TAGE",
        title_ja="副資材のデジタルサンプリング：3Dバーチャル衣料とデジタル校正稿の使い方 | TAGE",
        title_ko="부자재 디지털 샘플링: 3D 가상 의류와 디지털 교정본 확인법 | TAGE",
        title_fr="Échantillonnage numérique des accessoires : 3D et maquettes | TAGE",
        title_es="Muestreo digital de accesorios: prenda 3D y proof digital | TAGE",
        desc_zh="打样最贵的往往不是样品费，而是来回寄样耗掉的两三周。本文讲清数码稿、3D 虚拟样衣与实物样各自能确认什么，颜色与批注怎么写才算可执行，渲染里的厚度、位置公差与金属反光为什么必须回到实物验证，并给出一套四步混合流程与三个常见误区。来自东莞泰阁包装。",
        desc_en="Digital sampling for trims: what a 3D virtual garment and a digital proof can confirm, and why hand feel, foil sheen and wash fastness still need real samples.",
        desc_ja="副資材のデジタルサンプリング入門。デジタル校正稿・3Dバーチャル衣料・実物サンプルで確認できる範囲、色とコメントの伝え方、厚み・位置公差・金属反射が実物検証を要する理由、4ステップの運用フローと三つの誤解を解説。東莞泰閣包装。",
        desc_ko="부자재 디지털 샘플링 안내. 디지털 교정본·3D 가상 의류·실물 샘플이 확인하는 범위, 색상과 코멘트 전달법, 두께·위치 공차·금속 반사가 실물 검증을 필요로 하는 이유, 4단계 운영 흐름과 세 가지 오해를 정리합니다. 둥관 TAGE 패키징.",
        desc_fr="Échantillonnage numérique : ce qu'une maquette et un vêtement virtuel 3D valident, et pourquoi le toucher, l'éclat du foil et la tenue au lavage exigent un échantillon réel.",
        desc_es="Muestreo digital: qué confirman un proof y una prenda virtual 3D, y por qué el tacto, el brillo del foil y la resistencia al lavado exigen muestra física.",
        crumb_zh="数字化打样",
        crumb_en="Digital Sampling",
        crumb_ja="デジタルサンプリング",
        crumb_ko="디지털 샘플링",
        crumb_fr="Échantillonnage numérique",
        crumb_es="Muestreo digital",
        h1_zh="服装辅料数字化打样指南：数码稿、3D 虚拟样衣与实物样怎么配合",
        h1_en="Digital Sampling for Trims: Digital Proofs and 3D Garments",
        h1_ja="副資材のデジタルサンプリング：校正稿と3Dバーチャル衣料の使い方",
        h1_ko="부자재 디지털 샘플링: 교정본과 3D 가상 의류 활용",
        h1_fr="Échantillonnage numérique : maquettes et vêtements virtuels 3D",
        h1_es="Muestreo digital: proofs y prendas virtuales 3D",
        tag_zh="打样与工艺", tag_en="Sampling &amp; Process", tag_ja="サンプルと加工", tag_ko="샘플·공정",
        tag_fr="Échantillonnage et procédé", tag_es="Muestreo y proceso",
        sum_zh="打样阶段最贵的不是样品费，而是来回寄样耗掉的两三周。本文先把数码稿、3D 虚拟样衣与实物样放进同一张表，逐项对照各自能确认什么、确认不了什么、典型周期多久；再讲数码稿阶段怎么把颜色写成可执行口径（色号与屏幕分开）、一条批注只对一个点、文件名带版本，以及虚拟样衣里最容易被忽略的三个参数：厚度与体积、缝制位置公差、金属反光。随后列出必须回到实物样的六个参数，给出数码稿加渲染加实物样的四步混合流程与时间安排，最后点出拿渲染图直接下单、把数码稿确认当颜色确认、一件样品要验三个配色这三个常见误区。",
        sum_en="The expensive part of sampling is rarely the fee — it is the two or three weeks lost to samples travelling back and forth. One table places digital proofs, 3D virtual garments and physical samples side by side: what each confirms, what it cannot, and how long it takes. The article then covers writing colour as an executable reference, one annotation per point, versioned filenames, and the three parameters virtual garments quietly lose — thickness, placement tolerance and metallic reflection. It lists the six items that force a physical sample, sets out a four-step hybrid workflow with timings, and closes on three familiar mistakes: ordering from a render, treating a proof approval as a colour approval, and asking one sample to prove three colourways.",
        sum_ja="サンプル段階で最も高くつくのはサンプル代ではなく、往復郵送で失う2〜3週間です。デジタル校正稿・3Dバーチャル衣料・実物サンプルを一つの表に並べ、確認できること、できないこと、標準的な所要日数を比較します。続いて、色を実行可能な口径で示す方法（色番と画面を分ける）、1件1コメント、版番号付きファイル名、そしてバーチャル衣料で失われがちな三つのパラメータ（厚み、縫製位置公差、金属反射）を解説。実物サンプルが必須となる6項目、4ステップのハイブリッド工程と日程、最後にありがちな三つの誤解（レンダリングで直接発注、校正稿の確認＝色の確認、1点で3配色の確認）を整理します。",
        sum_ko="샘플 단계에서 가장 비싼 것은 샘플 비용이 아니라 왕복 택배로 잃는 2~3주입니다. 디지털 교정본·3D 가상 의류·실물 샘플을 한 표에 놓고 확인 가능 항목, 불가 항목, 일반 소요 기간을 비교합니다. 이어서 색상을 실행 가능한 기준으로 쓰는 법(색상 코드와 화면 분리), 코멘트 하나에 한 가지, 버전이 표기된 파일명, 그리고 가상 의류에서 흐려지는 세 가지 변수(두께, 봉제 위치 공차, 금속 반사)를 다룹니다. 실물 샘플이 필수인 여섯 항목, 4단계 하이브리드 흐름과 일정, 마지막으로 렌더링으로 바로 발주, 교정본 승인을 색상 승인으로 착각, 한 점으로 세 배색 확인이라는 세 가지 오해를 정리합니다.",
        sum_fr="Le coût réel du sampling n'est pas la facture mais les deux ou trois semaines perdues en allers-retours. Un tableau met côte à côte maquette numérique, vêtement virtuel 3D et échantillon physique : ce que chacun valide, ce qu'il ne valide pas, et son délai. L'article traite ensuite la couleur écrite en référence exploitable, une annotation par point, les noms de fichiers versionnés, et les trois paramètres que le virtuel fait oublier : épaisseur, tolérance de position, reflet métallique. Il liste les six points qui imposent un échantillon physique, propose un processus hybride en quatre étapes avec son calendrier, et conclut sur trois erreurs courantes : commander sur un rendu, confondre validation de maquette et validation de couleur, demander à une pièce de valider trois coloris.",
        sum_es="Lo caro del muestreo no es la factura, sino las dos o tres semanas perdidas en envíos de ida y vuelta. Una tabla pone frente a frente proof digital, prenda virtual 3D y muestra física: qué confirma cada uno, qué no y cuánto tarda. Después aborda el color escrito como referencia ejecutable, un comentario por punto, nombres de archivo con versión y los tres parámetros que el virtual difumina: grosor, tolerancia de posición y reflejo metálico. Enumera los seis puntos que obligan a una muestra física, propone un flujo híbrido en cuatro pasos con calendario y cierra con tres errores habituales: pedir desde un render, confundir aprobar un proof con aprobar el color y exigir a una sola pieza tres combinaciones de color.",
    ),
    dict(
        slug="trim-coding-standardization.html",
        body="blog/_body_coding.html",
        title_zh="服装辅料编码与版库标准化：吊牌、织唛、洗水标可复用 | TAGE",
        title_en="Trims Coding and Tooling Library: Reusable, Reorderable Parts | TAGE",
        title_ja="副資材のコード化と版ライブラリ標準化：再利用できる標準部品にする | TAGE",
        title_ko="부자재 코딩과 판 라이브러리 표준화: 재사용 가능한 표준 부품 | TAGE",
        title_fr="Codification et bibliothèque de formes : des accessoires réutilisables | TAGE",
        title_es="Codificación y biblioteca de troqueles: accesorios reutilizables | TAGE",
        desc_zh="同一张吊牌开了四套版、同一个主唛三个色号、翻单找不到签样，根源是没有编码与版库台账。本文给出一套可直接抄的五段式编码规则（品类—材质—规格—颜色—版本）、版库与模具台账必须登记的六个字段、色卡库的管理方式，以及怎么把编码写进规格书、订单与仓库标签。来自东莞泰阁包装。",
        desc_en="A five-segment trims code (category, material, size, colour, version), the tooling ledger fields that end re-cutting, and how to run a colour-card library.",
        desc_ja="副資材コードの5セグメント規則（カテゴリ・素材・サイズ・色・版）、版を起こし直さずに済む台帳項目、色見本庫の運用、仕様書と注文書・倉庫ラベルへの書き込み方を解説します。東莞泰閣包装。",
        desc_ko="부자재 코드 5단계 규칙(카테고리·소재·규격·색상·버전), 판 재제작을 막는 대장 항목, 색상 카드 라이브러리 운영, 사양서·발주서·창고 라벨 반영법을 정리합니다. 둥관 TAGE 패키징.",
        desc_fr="Un code accessoire en cinq segments (catégorie, matière, format, couleur, version), les champs de registre qui évitent de refaire les formes, et la gestion d'un nuancier.",
        desc_es="Un código de accesorio en cinco segmentos (categoría, material, medida, color, versión), los campos de registro que evitan rehacer troqueles y la gestión de cartas de color.",
        crumb_zh="编码与版库标准化",
        crumb_en="Coding &amp; Tooling Library",
        crumb_ja="コード化と版ライブラリ",
        crumb_ko="코딩·판 라이브러리",
        crumb_fr="Codification et bibliothèque",
        crumb_es="Codificación y troqueles",
        h1_zh="服装辅料编码与版库标准化指南：让吊牌、织唛与洗水标可复用、可翻单",
        h1_en="Trims Coding and Tooling Library: Making Every Trim Reusable",
        h1_ja="副資材のコード化と版ライブラリ標準化ガイド：吊り札・織ラベル・洗濯表示ラベルを再利用可能に",
        h1_ko="부자재 코딩과 판 라이브러리 표준화: 행택·직조 라벨·세탁 표시 라벨 재사용",
        h1_fr="Codification et bibliothèque de formes : rendre chaque accessoire réutilisable",
        h1_es="Codificación y biblioteca de troqueles: hacer reutilizable cada accesorio",
        tag_zh="管理与标准化", tag_en="Trims Management", tag_ja="管理と標準化", tag_ko="관리·표준화",
        tag_fr="Gestion et standardisation", tag_es="Gestión y estandarización",
        sum_zh="辅料数量少金额小，最容易没人管，两三年后就成了同一张吊牌开了四套版、同一个主唛三个色号、翻单找不到签样。本文先把「没有唯一编号、没有版库归属、颜色没有编号」三个根源讲透，再给出一套可直接抄的五段式编码规则：品类（HT/WL/CL/PB/PBG）—材质或工艺（KRA/ART/SAT/FOIL）—规格（毫米数字，如 9054、30F）—颜色（BLK/WHT/NAT/PNT123）—版本（01 起递增），并以 HT-KRA-9054-BLK-01 举例。随后列出模具台账必须登记的六个字段（编码与名称、版种与数量、保管位置、权属与费用、状态与寿命、签样照片与实物）、色卡库的一色一卡与跨材质对照做法、编码写进规格书与订单的方式，最后给出落地三步与一个季度对照的推行建议。",
        sum_en="Trims are small and cheap, so nobody owns them — and two or three years later one hang tag exists as four sets of tooling, one neck label carries three colour references and a reorder cannot find the signed sample. The article names the three root causes (no unique code, no tooling ownership, colours without codes), then gives a five-segment code you can copy: category (HT, WL, CL, PB, PBG), material or process (KRA, ART, SAT, FOIL), size in millimetres (9054, 30F), colour (BLK, WHT, NAT, PNT123) and version (from 01), with HT-KRA-9054-BLK-01 as the worked example. It then lists the six fields a tooling ledger must hold, how to run one physical colour card per colour with a cross-substrate table, and how to put codes into spec sheets, POs and warehouse labels — closing with a three-step rollout and a one-season baseline to argue the case internally.",
        sum_ja="副資材は数量も金額も小さく、誰も管理しないため、数年後には同じタグに4セットの版、同じメインラベルに3つの色番、追加発注時に承認サンプルが見つからない状態になります。本記事はまず三つの根本原因（一意の番号がない、版の帰属がない、色に番号がない）を整理し、そのまま使える5セグメントのコード規則を示します。カテゴリ（HT/WL/CL/PB/PBG）、素材・加工（KRA/ART/SAT/FOIL）、サイズ（mmの数字、9054や30F）、色（BLK/WHT/NAT/PNT123）、版（01から）。例は HT-KRA-9054-BLK-01。次に版台帳に必須の6項目、1色1カードと素材間対応表による色見本庫の運用、仕様書・注文書・倉庫ラベルへの記載方法、最後に導入3ステップと一季分の比較で社内を説得する方法を示します。",
        sum_ko="부자재는 수량과 금액이 작아 관리 주체가 없고, 몇 년 뒤에는 같은 행택에 네 세트의 판, 같은 메인 라벨에 세 개의 색상 번호, 재발주 시 승인 샘플을 찾지 못하는 상황이 됩니다. 이 글은 먼저 세 가지 원인(고유 번호 없음, 판 소유권 없음, 색상 번호 없음)을 정리하고, 바로 쓸 수 있는 5단계 코드 규칙을 제시합니다. 카테고리(HT/WL/CL/PB/PBG), 소재·공정(KRA/ART/SAT/FOIL), 규격(mm 숫자, 9054·30F), 색상(BLK/WHT/NAT/PNT123), 버전(01부터). 예시는 HT-KRA-9054-BLK-01. 이어서 판 대장 필수 여섯 항목, 색상별 실물 카드와 소재 간 대조표로 색상 라이브러리를 운영하는 법, 사양서·발주서·창고 라벨 반영법, 마지막으로 도입 3단계와 한 시즌 비교로 설득하는 방법을 제시합니다.",
        sum_fr="Les accessoires sont petits et bon marché, donc personne ne s'en occupe : quelques années plus tard, une même étiquette existe en quatre jeux de formes, un label de col porte trois références couleur et un réassort ne retrouve plus l'échantillon signé. L'article nomme les trois causes (aucun code unique, aucune propriété des formes, couleurs sans code), puis propose un code en cinq segments directement réutilisable : catégorie (HT, WL, CL, PB, PBG), matière ou procédé (KRA, ART, SAT, FOIL), format en millimètres (9054, 30F), couleur (BLK, WHT, NAT, PNT123) et version (à partir de 01), avec HT-KRA-9054-BLK-01 en exemple. Il liste ensuite les six champs indispensables au registre des formes, la gestion d'un nuancier physique avec table de correspondance entre supports, et l'inscription des codes dans les fiches, les commandes et les étiquettes d'entrepôt.",
        sum_es="Los accesorios son pequeños y baratos, así que nadie los gestiona: pocos años después una misma etiqueta existe en cuatro juegos de troqueles, una etiqueta de cuello lleva tres referencias de color y una reposición no encuentra la muestra firmada. El artículo nombra las tres causas (sin código único, sin propiedad de troqueles, colores sin código) y propone un código de cinco segmentos listo para copiar: categoría (HT, WL, CL, PB, PBG), material o proceso (KRA, ART, SAT, FOIL), medida en milímetros (9054, 30F), color (BLK, WHT, NAT, PNT123) y versión (desde 01), con HT-KRA-9054-BLK-01 como ejemplo. Después enumera los seis campos que debe tener el registro de troqueles, cómo gestionar una carta física por color con tabla entre soportes y cómo llevar los códigos a fichas, pedidos y etiquetas de almacén.",
    ),
]
