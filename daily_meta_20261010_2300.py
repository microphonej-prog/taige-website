#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-10 晚间批次（23:00）每日更新：2 篇新文章元数据（六语：zh-Hant 根 / en / ja / ko / fr / es）

选题说明（任务给定主题池 30 项连同既有扩展均已上线；本次沿两个尚未独立成文的方向扩展，
已核对 blog/、en|ja|ko|fr|es/blog/ 与 sitemap.xml 无重复 slug，并 grep 全站确认关键词覆盖情况）：

- uflpa-apparel-trims-traceability-guide：全站 grep「UFLPA / 涉疆 / 强迫劳动 / 新疆 / 劳工 / 美国海关 / CBP」= 0 命中。
  HS 编码与报关文章讲的是归类与关税，社会责任审核文章讲的是 Sedex/BSCI 验厂，均未涉及美国溯源执法。
  本文按「UFLPA 管什么 → 进口商最常索要的七类文件对照表 → 溯源台账五步建法 →
  四种最容易出问题的做法 → 出货前预检五件事」展开，落点是辅料厂能实际交付的文件。

- corrugated-carton-strength-guide：全站 grep「楞型 / ECT / 纸箱选型 / 钉箱 / 粘箱 / 单一材质」= 0，
  「耐破」仅 4 处顺带提及；garment-trims-carton-loading-guide 讲装箱与装柜数量，
  carton-shipping-mark-guide 讲唛头，均未讲箱体本身的选型与强度。
  本文按「三层/五层/七层对照表 → 用耐破与边压指标对齐 → 堆码强度不等于纸箱强度 →
  海运环境的凝露与挤压 → 封箱方式对照表 → 询价必给的六个参数」展开。
"""

ARTICLES = [
    dict(
        slug="uflpa-apparel-trims-traceability-guide.html",
        body="blog/_body_uflpa.html",
        title_zh="美国 UFLPA 服装辅料溯源指南：进口商要什么文件、供应商怎么配合 | TAGE",
        title_en="US UFLPA Guide for Apparel Trims: Documents Importers Need &amp; How Suppliers Comply | TAGE",
        title_ja="米国 UFLPA 衣料副資材トレーサビリティガイド：輸入者が求める書類とサプライヤーの対応 | TAGE",
        title_ko="미국 UFLPA 의류 부자재 추적 가이드: 수입자가 요구하는 서류와 공급업체 대응 | TAGE",
        title_fr="Guide UFLPA pour les accessoires textiles : documents exigés et réponse fournisseur | TAGE",
        title_es="Guía UFLPA para accesorios textiles: documentos exigidos y respuesta del proveedor | TAGE",
        desc_zh="美国 UFLPA 溯源指南：进口商最常索要的七类文件、辅料供应链地图怎么建、分包商与纸浆纱线产地为何必须说清，并附溯源台账五步建法与出货前预检清单。来自东莞泰阁包装。",
        desc_en="UFLPA traceability guide for apparel trims: the seven document sets US importers request, how to map the supply chain and a practical pre-shipment checklist.",
        desc_ja="米国 UFLPA 対応ガイド。輸入者が最もよく求める 7 種類の書類、副資材のサプライチェーンマップの作り方、外注先とパルプ・糸の産地を明示すべき理由、出荷前チェック 5 項目を解説。東莞泰閣包装。",
        desc_ko="미국 UFLPA 대응 가이드. 수입자가 가장 자주 요구하는 일곱 가지 서류, 부자재 공급망 맵 구축법, 외주 업체와 펄프·원사 산지를 밝혀야 하는 이유, 출하 전 점검 다섯 항목을 정리했습니다. 둥관 TAGE 패키징.",
        desc_fr="Guide UFLPA : les sept dossiers les plus demandés par les importateurs américains, comment cartographier la chaîne d'approvisionnement, pourquoi déclarer sous-traitants et origine du fil, et un contrôle avant expédition.",
        desc_es="Guía UFLPA: los siete documentos que más piden los importadores estadounidenses, cómo mapear la cadena de suministro, por qué declarar subcontratistas y origen del hilo, y un control previo al envío.",
        crumb_zh="UFLPA 溯源",
        crumb_en="UFLPA Traceability",
        crumb_ja="UFLPA トレーサビリティ",
        crumb_ko="UFLPA 추적",
        crumb_fr="Traçabilité UFLPA",
        crumb_es="Trazabilidad UFLPA",
        h1_zh="美国 UFLPA 服装辅料溯源指南：要什么文件、怎么准备",
        h1_en="US UFLPA Guide for Apparel Trims: What Documents Are Needed and How to Prepare",
        h1_ja="米国 UFLPA 衣料副資材トレーサビリティガイド：必要書類と準備の進め方",
        h1_ko="미국 UFLPA 의류 부자재 추적 가이드: 필요한 서류와 준비 방법",
        h1_fr="Guide UFLPA des accessoires textiles : quels documents et comment se préparer",
        h1_es="Guía UFLPA para accesorios textiles: qué documentos y cómo prepararse",
        tag_zh="合规指南",
        tag_en="Compliance Guide",
        tag_ja="コンプライアンスガイド",
        tag_ko="컴플라이언스 가이드",
        tag_fr="Guide conformité",
        tag_es="Guía de cumplimiento",
        sum_zh="美国《维吾尔强迫劳动预防法》(UFLPA) 自 2022 年 6 月起实施，对涉疆或与实体清单企业相关的货物实行「可反驳推定」——海关可以直接扣货，举证责任却在进口商身上。服装与纺织品是执法重点，哪怕一票货里只有吊牌、织唛、洗水标和包装袋，美国买家也会要求你出具原料溯源文件。本文先讲清 UFLPA 管什么、辅料为什么会被连带问到，再用一张表列出美国买家最常索要的七类文件（原料溯源表、产地声明、采购发票与合同、生产领料记录、分包商清单、第三方证书、供应商承诺书）及各自出具方；随后是溯源台账的五步建法：成品号固定批次、领料单写清批次与供应商、采购发票与送货单入库单三单一致、二级供应商单独建账、每季度更新；再讲四种最容易出问题的做法（通用模板声明、台账与发票对不上、分包商没披露、只写中国产），最后给出出货前必须做完的五项预检与给美国客户建共享文件夹的实操建议。",
        sum_en="The US Uyghur Forced Labor Prevention Act has applied since June 2022 and creates a rebuttable presumption against goods tied to Xinjiang or to entities on the UFLPA Entity List: customs can detain the shipment while the burden of proof sits with the importer. Apparel and textiles are an enforcement priority, so even a shipment containing nothing but hang tags, woven labels, care labels and bags will draw a request for raw material traceability documents. The guide sets out what UFLPA covers and why trims get caught up, then a table lists the seven document sets US buyers ask for most — raw material traceability sheet, origin declaration, purchase invoices and contracts, production and material issue records, subcontractor list, third-party certificates and the supplier declaration — with the party that issues each. It then walks through a five-step traceability file: fix one batch per item code, record batch and supplier on issue slips, keep invoice, delivery note and goods receipt consistent, register tier-two suppliers separately and refresh quarterly. Four practices that fail most often follow — generic template declarations, a register that does not reconcile with invoices, undisclosed subcontractors and saying only made in China — before the closing five-point pre-shipment check and the shared-folder routine for US customers.",
        sum_ja="米国のウイグル強制労働防止法（UFLPA）は 2022 年 6 月から施行され、新疆や実体リスト掲載企業に関連する貨物に「反証可能な推定」を適用します。税関は貨物を留置でき、立証責任は輸入者にあります。衣料・繊維は取締りの重点で、タグ、織りラベル、洗濯表示ラベル、袋だけの貨物でも原料トレーサビリティ書類が求められます。本記事はまず UFLPA の範囲と副資材が問われる理由を整理し、米国バイヤーが最もよく求める 7 種類の書類（原料トレーサビリティ表、原産地宣言、購入請求書と契約書、製造・払出記録、外注先リスト、第三者証明書、サプライヤー宣言書）と発行主体を一覧にします。続いて台帳の 5 ステップ（品番ごとの批次固定、払出票への記載、請求書・納品書・入庫票の一致、二次サプライヤーの別台帳、四半期更新）、問題になりやすい 4 つのやり方（テンプレート宣言、不整合、外注先の未申告、中国製のみの記載）、最後に出荷前チェック 5 項目と米国顧客向けの共有フォルダ運用を提示します。",
        sum_ko="미국 위구르 강제노동방지법(UFLPA)은 2022년 6월부터 시행되어 신장이나 실체 목록 기업과 관련된 화물에 '반박 가능한 추정'을 적용합니다. 세관은 화물을 억류할 수 있고 입증 책임은 수입자에게 있습니다. 의류·섬유는 단속 중점이어서 행택, 직조 라벨, 세탁 표시 라벨, 봉투만 든 화물도 원재료 추적 서류를 요구받습니다. 이 글은 UFLPA의 범위와 부자재가 함께 문제되는 이유를 정리하고, 미국 바이어가 가장 자주 요구하는 일곱 가지 서류(원재료 추적표, 원산지 선언, 구매 인보이스와 계약서, 생산·불출 기록, 외주 목록, 제3자 인증서, 공급업체 확약서)와 발행 주체를 표로 제시합니다. 이어 추적 대장의 다섯 단계(품목별 배치 고정, 불출표 기재, 인보이스·납품서·입고 전표 일치, 2차 공급사 별도 관리, 분기 갱신), 문제가 되는 네 가지 관행, 출하 전 점검 다섯 항목과 미국 고객용 공유 폴더 운영을 다룹니다.",
        sum_fr="L'UFLPA américain s'applique depuis juin 2022 et instaure une présomption réfutable contre les marchandises liées au Xinjiang ou à une entité de sa liste : la douane peut retenir l'envoi et la charge de la preuve pèse sur l'importateur. L'habillement est prioritaire, donc même un envoi ne contenant que des étiquettes suspendues, labels tissés, étiquettes d'entretien et sacs déclenche une demande de traçabilité des matières. Le guide expose le périmètre de l'UFLPA et la raison pour laquelle les accessoires sont concernés, puis un tableau recense les sept dossiers les plus demandés — fiche de traçabilité, déclaration d'origine, factures et contrats, dossiers de production et de sortie, liste des sous-traitants, certificats tiers, attestation fournisseur — avec l'émetteur de chacun. Suit la construction du dossier en cinq étapes : un lot fixe par code article, lots et fournisseurs sur les bons de sortie, facture, bon de livraison et bon de réception cohérents, registre séparé des fournisseurs de rang deux et mise à jour trimestrielle. Quatre pratiques fautives sont détaillées, avant les cinq contrôles avant expédition et la routine de dossier partagé par client américain.",
        sum_es="La ley estadounidense UFLPA se aplica desde junio de 2022 y crea una presunción refutable contra la mercancía vinculada a Xinjiang o a entidades de su lista: la aduana puede retener el envío y la carga de la prueba recae en el importador. La confección es prioridad, así que incluso un envío con solo etiquetas colgantes, tejidas, de cuidado y bolsas provoca una petición de trazabilidad de materias. La guía explica el ámbito de la UFLPA y por qué los accesorios se ven implicados, y una tabla recoge los siete documentos más pedidos —ficha de trazabilidad, declaración de origen, facturas y contratos, registros de producción y consumo, lista de subcontratistas, certificados de terceros y declaración del proveedor— con quién emite cada uno. Después llega el archivo de trazabilidad en cinco pasos: un lote fijo por código, lote y proveedor en los vales de salida, factura, albarán y entrada coherentes, registro aparte de proveedores de segundo nivel y actualización trimestral. Se detallan cuatro prácticas que fallan, los cinco controles previos al envío y la carpeta compartida por cliente estadounidense.",
    ),
    dict(
        slug="corrugated-carton-strength-guide.html",
        body="blog/_body_carton.html",
        title_zh="瓦楞外箱选型指南：三层、五层怎么选与强度怎么定 | TAGE",
        title_en="Corrugated Carton Selection Guide: Wall Grades, Strength &amp; Stacking | TAGE",
        title_ja="段ボール外箱の選定ガイド：三層・五層の選び方と強度の決め方 | TAGE",
        title_ko="골판지 상자 선정 가이드: 3층·5층 선택과 강도 결정 | TAGE",
        title_fr="Guide de choix des cartons ondulés : cannelures, résistance et gerbage | TAGE",
        title_es="Guía de cajas de cartón ondulado: paredes, resistencia y apilado | TAGE",
        desc_zh="瓦楞外箱选型指南：三层、五层与七层怎么选，耐破与边压强度指标怎么约定，堆码与海运湿度下的强度衰减，封箱方式对比与询价必给的六个参数，附打样确认内径的建议。来自东莞泰阁包装。",
        desc_en="Corrugated carton guide for apparel trims: choosing single, double or triple wall, burst and edge crush specs, stacking derating and carton closing methods.",
        desc_ja="段ボール外箱の選定ガイド。三層・五層・七層の選び方、破裂強度と圧縮強度の指定方法、積載と海上輸送の湿度による強度低下、封函方法の比較、見積依頼に必要な 6 項目を解説。東莞泰閣包装。",
        desc_ko="골판지 상자 선정 가이드. 3층·5층·7층 선택 기준, 파열 강도와 압축 강도 지정법, 적재와 해상 습도에 따른 강도 저하, 봉함 방식 비교, 견적 요청에 필요한 여섯 항목을 정리했습니다. 둥관 TAGE 패키징.",
        desc_fr="Guide des cartons ondulés pour accessoires : simple, double ou triple cannelure, éclatement et compression verticale, gerbage, humidité et modes de fermeture.",
        desc_es="Guía de cajas onduladas para accesorios: simple, doble o triple pared, estallido y compresión vertical, apilado, humedad y métodos de cierre.",
        crumb_zh="瓦楞外箱选型",
        crumb_en="Corrugated Cartons",
        crumb_ja="段ボール外箱の選定",
        crumb_ko="골판지 상자 선정",
        crumb_fr="Cartons ondulés",
        crumb_es="Cajas de cartón",
        h1_zh="瓦楞外箱选型指南：三层、五层怎么选，强度怎么定",
        h1_en="Corrugated Carton Selection Guide: Choosing Wall Grade and Strength",
        h1_ja="段ボール外箱の選定ガイド：三層・五層の選び方と強度の決め方",
        h1_ko="골판지 상자 선정 가이드: 3층·5층 선택과 강도 결정",
        h1_fr="Guide de choix des cartons ondulés : cannelures et résistance",
        h1_es="Guía de cajas de cartón ondulado: paredes y resistencia",
        tag_zh="包装指南",
        tag_en="Packaging Guide",
        tag_ja="包装ガイド",
        tag_ko="포장 가이드",
        tag_fr="Guide emballage",
        tag_es="Guía de embalaje",
        sum_zh="外箱是辅料包装里最便宜、也最容易被忽略的一项：箱体选薄了，海运 30 多天的湿度加上堆码，底层纸箱会塌角，吊牌折角、织唛卷边、纸袋压痕全在开箱那一刻暴露；选厚了，每箱成本多几毛，整柜还多出几百公斤体积重。本文先给出单瓦三层、双瓦五层与三瓦七层的楞型、厚度与典型用途对照表，说明 E 楞适合吊牌这类需要正面印刷的外箱、B 楞最通用；再讲为什么不能只写「五层加硬」，而要用耐破强度与边压强度对齐，并要求纸板检测报告，同时提醒大面积印刷、开孔与模切会让强度下降 10–20%；接着解释堆码强度不等于纸箱强度——湿度升到 90% 左右抗压可能只剩一半、长时间堆码需要 0.5–0.6 的安全系数、错缝堆放优于柱状堆放；随后是海运柜内的凝露与挤压两个隐性损耗，以及钉箱、粘箱、打带与纸胶带封箱四种方式的优点与注意点，最后列出询价时必须提供的六个参数与打样确认内径的实操建议。",
        sum_en="The shipping carton is the cheapest part of trims packaging and the easiest to neglect: a board that is too light will see bottom cartons collapse after thirty days at sea with humidity and stacking, so bent hang tags, curled woven labels and dented paper bags appear the moment the box opens; too heavy a board adds cost per carton and hundreds of kilos of chargeable volume to the container. The guide opens with a table of single, double and triple wall structures covering common flutes, thickness ranges and typical uses — E flute for hang tag cartons that need sharp front-panel printing, B flute as the general-purpose choice. It explains why saying extra strong five ply is not enough and why burst strength and edge crush values, backed by a board test report, are what to agree on, noting that large print coverage, hand holes and die cuts cut strength by 10–20 percent. Stacking strength is then separated from carton strength: at around 90 percent relative humidity a carton may keep only half its compression strength, sustained loads call for a safety factor of 0.5–0.6, and interlocked stacking beats column stacking. Two hidden losses inside a sea container — condensation and rubbing — follow, then stapling, hot melt, strapping and paper tape compared, and the six parameters to send with any enquiry.",
        sum_ja="外箱は副資材包装で最も安く、最も見落とされやすい部分です。段ボールが薄いと、30 日以上の海上輸送の湿度と積み重ねで下段がつぶれ、開梱した瞬間にタグの折れ、織りラベルの巻き、紙袋の圧痕が現れます。厚すぎると 1 箱あたりのコストが上がり、コンテナは数百 kg の容積重量を余分に抱えます。本記事はまず片面三層・両面五層・三層段七層のフルート、厚み、用途を表で整理し、E フルートは正面印刷が必要なタグ用外箱、B フルートは汎用と説明します。次に「五層で強化」だけでは不十分な理由と、破裂強度・圧縮強度を数値で指定し試験報告を求める方法、大面積印刷・手穴・型抜きで強度が 10〜20% 低下する点を解説。積載強度と段ボール強度は別物で、湿度 90% 前後では圧縮強度が半分程度になり、長期積載には安全率 0.5〜0.6、レンガ積みが柱積みより有利であることを示します。最後にコンテナ内の結露と擦れ、4 つの封函方法の比較、見積依頼に必要な 6 項目を掲載します。",
        sum_ko="외부 상자는 부자재 포장에서 가장 저렴하고 가장 소홀해지기 쉬운 부분입니다. 골판지가 얇으면 30일이 넘는 해상 운송의 습도와 적재로 하단 상자가 눌려 개봉 순간 행택 꺾임, 직조 라벨 말림, 종이백 눌린 자국이 드러납니다. 너무 두꺼우면 상자당 비용이 오르고 컨테이너는 수백 kg의 용적 중량을 떠안습니다. 이 글은 단면 3층·양면 5층·3중 7층의 골, 두께, 용도를 표로 정리하고 E 골은 전면 인쇄가 필요한 행택 상자, B 골은 범용이라고 설명합니다. 이어 '5층 강화'만으로 부족한 이유, 파열·압축 강도를 수치로 지정하고 시험 성적서를 요구하는 방법, 대면적 인쇄·손잡이 구멍·타발로 강도가 10–20% 떨어지는 점을 다룹니다. 적재 강도는 상자 강도와 다르며 습도 90%에서 압축 강도가 절반으로 줄고 장기 적재에는 안전율 0.5–0.6, 교차 적재가 기둥 적재보다 유리함을 보여줍니다. 마지막으로 컨테이너 내부 결로와 마찰, 네 가지 봉함 방식 비교, 견적 요청에 필요한 여섯 항목을 제공합니다.",
        sum_fr="Le carton d'expédition est l'élément le moins cher et le plus négligé de l'emballage d'accessoires : trop léger, il s'écrase après trente jours de mer avec l'humidité et le gerbage, et étiquettes pliées, labels roulés et sacs marqués apparaissent à l'ouverture ; trop lourd, il coûte plus cher par boîte et ajoute des centaines de kilos de volume taxable au conteneur. Le guide ouvre sur un tableau des structures simple, double et triple cannelure avec flutes, épaisseurs et usages — cannelure E pour les cartons d'étiquettes à impression soignée, B comme choix généraliste. Il explique pourquoi cinq plis renforcé ne suffit pas, pourquoi il faut fixer éclatement et compression verticale avec un rapport d'essai, et comment une grande surface imprimée, des poignées ou des découpes réduisent la résistance de 10 à 20 pour cent. La résistance au gerbage est ensuite distinguée de celle du carton : à 90 pour cent d'humidité relative la compression peut tomber de moitié, une charge permanente exige un coefficient de 0,5–0,6 et le gerbage croisé vaut mieux que le gerbage en colonne. Suivent condensation et frottement en conteneur, la comparaison agrafage, collage, cerclage et ruban papier, et les six paramètres à joindre à toute demande.",
        sum_es="La caja de expedición es la parte más barata y más descuidada del embalaje de accesorios: si el cartón es ligero, treinta días de mar con humedad y apilado aplastan las cajas de abajo y etiquetas dobladas, etiquetas tejidas enrolladas y bolsas marcadas aparecen al abrir; si es pesado, cada caja cuesta más y el contenedor suma cientos de kilos de volumen facturable. La guía abre con una tabla de pared simple, doble y triple con ondas, grosores y usos: onda E para cajas de etiquetas con impresión cuidada y onda B como opción general. Explica por qué cinco capas reforzado no basta y por qué conviene fijar estallido y compresión vertical con informe de ensayo, advirtiendo que una gran superficie impresa, asas o troquelados reducen la resistencia un 10–20 %. Después separa la resistencia al apilado de la resistencia de la caja: con un 90 % de humedad relativa la compresión puede caer a la mitad, la carga sostenida exige un factor de 0,5–0,6 y el apilado cruzado supera al de columna. Siguen la condensación y el roce en contenedor, la comparación de grapado, pegado, flejado y cinta de papel, y los seis parámetros de cualquier consulta.",
    ),
]
