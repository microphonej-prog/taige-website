#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-09-28 晚间批次文章元数据（六语：zh-Hant 根 / en / ja / ko / fr / es）。

选题说明：任务主题池 30 个选题均已上线（含此前批次扩展的国别合规、EUDR/PPWR、
原产地标识、产前样等）。本次继续沿「辅料大货如何走出去」与「订单数量口径」两个
方向扩展新选题，已核对 blog/ 全量文件、en|ja|ko|fr|es/blog/ 与 sitemap.xml：

- 出货方式与物流（garment-trims-freight-mode-guide）：现有文章里
  garment-trims-sample-shipping-guide 只讲「样品」寄送渠道与 DDP/DDU，
  garment-trunk-export-packaging 讲「包装与装柜」本身，garment-trims-lead-time-guide
  讲交期倒排，都没有专文讲大货该走快递/空运/海运拼箱/整柜、体积重怎么算、
  EXW/FOB/CIF/DDP 对辅料订单的实际影响与跟成衣大货拼柜的配合；全文用关键词
  检索过「拼箱/整柜」在 187 篇文章中仅出现 1 次，属明显空白，与上述三篇互补。

- 数量容差与备损率（trim-order-quantity-tolerance-guide）：现有
  trim-order-quantity-unit-conversion 只讲单位换算（打/罗/个/套），
  hang-tag-moq-cost 讲起订量与成本，trim-order-contract-terms-guide 讲合同条款清单，
  都没有专文讲「多交/少交容差、备损率、分色最小量、补单不重开版的条件」；
  关键词「多交/少交/交货数量」在全站 187 篇中出现 0 次。
"""

ARTICLES = [
    dict(
        slug="garment-trims-freight-mode-guide.html",
        body="blog/_body_freight.html",
        title_zh="服装辅料出货方式指南：快递、空运、海运拼箱与整柜怎么选 | TAGE",
        title_en="Shipping Trims by Courier, Air, LCL or FCL: How to Choose | TAGE",
        title_ja="副資材の輸送手段ガイド：宅配便・航空便・海上混載 LCL・FCL の選び方 | TAGE",
        title_ko="부자재 운송 방식 가이드: 특송·항공·해상 LCL·FCL 선택 | TAGE",
        title_fr="Expédier des accessoires : express, aérien, groupage ou conteneur | TAGE",
        title_es="Enviar accesorios: exprés, aéreo, grupaje o contenedor completo | TAGE",
        desc_zh="辅料体积小、货值低，运费与时效却常常决定成衣厂能否赶上船期。本文对比快递、空运、海运拼箱与整柜在时效、成本与起运量上的差异，讲清体积重怎么算、EXW/FOB/CIF/DDP 对辅料订单的影响、与成衣大货拼柜的配合，以及出货单证与常见踩坑。来自东莞泰阁包装。",
        desc_en="Courier, air, LCL or FCL: how trims buyers choose a freight mode, work out volumetric weight, use Incoterms and consolidate with the garment shipment.",
        desc_ja="副資材の輸送手段（宅配便・航空便・海上混載 LCL・海上コンテナ FCL）を比較。容積重量の計算、インコタームズ、アパレル本体との混載、出荷書類とよくある落とし穴を解説します。東莞泰閣包装。",
        desc_ko="부자재 운송 방식(특송·항공·해상 LCL·해상 FCL)을 비교합니다. 용적 중량 계산, 인코텀즈 차이, 완성복 화물과의 혼적, 출하 서류와 흔한 실수를 정리합니다. 둥관 TAGE 패키징.",
        desc_fr="Express, aérien, groupage ou conteneur : comment choisir le mode d'expédition des accessoires, calculer le poids volumétrique et utiliser les Incoterms.",
        desc_es="Exprés, aéreo, grupaje o contenedor completo: cómo elegir el modo de envío, calcular el peso volumétrico, usar los Incoterms y consolidar con la prenda.",
        crumb_zh="出货方式与物流",
        crumb_en="Freight &amp; Logistics",
        crumb_ja="輸送と物流",
        crumb_ko="운송·물류",
        crumb_fr="Transport et logistique",
        crumb_es="Transporte y logística",
        h1_zh="服装辅料出货方式指南：快递、空运、海运拼箱与整柜怎么选",
        h1_en="Shipping Trims: Choosing Between Courier, Air, LCL and FCL",
        h1_ja="副資材の輸送手段ガイド：宅配便・航空便・海上混載・海上コンテナの選び方",
        h1_ko="부자재 운송 방식 가이드: 특송·항공·해상 LCL·해상 FCL 선택",
        h1_fr="Expédier des accessoires : choisir entre express, aérien, groupage et complet",
        h1_es="Enviar accesorios: elegir entre exprés, aéreo, grupaje y contenedor completo",
        tag_zh="物流与出货", tag_en="Freight &amp; Shipping", tag_ja="物流・出荷", tag_ko="물류·출하",
        tag_fr="Transport et expédition", tag_es="Transporte y envíos",
        sum_zh="辅料体积小、货值低，运费与时效却常常决定成衣厂能不能赶上船期。本文把快递、空运、海运拼箱与海运整柜放在一张表里，按时效、适合的数量级、成本特点与最容易踩的坑逐项对照；随后讲清抛货与体积重的算法（含 0.12 方实重 15 公斤为何按 24 公斤计费）、EXW 与 FOB、CIF、DDP 在订舱、运费与风险转移上的差别，辅料厂与成衣大货拼柜时能配合的三件事与时间倒排，出货运单与交接文件要对的字段，最后列出低报货值、只看主运费、旺季爆舱、样品与大货混装、快递渠道限制五个常见坑与一条省事做法。",
        sum_en="Trims are small and rarely high in value, yet freight cost and transit time decide whether the garment factory catches its vessel. One table compares courier, air, LCL and FCL by transit time, workable scale, cost profile and the pitfall each brings. The article then explains volumetric weight (why a 15 kg carton at 0.12 CBM is billed at 24 kg), how EXW, FOB, CIF and DDP split booking, freight and risk, the three things a trims factory can do to ride along with the garment shipment, which fields invoice and packing list must reconcile, and the five mistakes that delay clearance, from under-declared value to samples packed inside the bulk carton.",
        sum_ja="副資材は小さく単価も高くありませんが、運賃とリードタイムが縫製工場の船積みに間に合うかを決めます。宅配便・航空便・海上混載（LCL）・海上コンテナ（FCL）を、日数・適した数量・コスト特性・落とし穴の四項目で一つの表にまとめて比較。続いて容積重量の計算（0.12 m3・実重 15 kg がなぜ 24 kg 課金になるか）、EXW・FOB・CIF・DDP の手配と運賃とリスク移転の違い、アパレル本体との混載で協力できる三つのこと、出荷書類で揃えるべき項目、低申告・現地費用の見落とし・繁忙期のスペース不足・サンプル混載・宅配便の制限という五つの失敗を整理します。",
        sum_ko="부자재는 작고 단가도 높지 않지만 운임과 리드타임이 봉제 공장의 선적 일정을 좌우합니다. 특송·항공·해상 LCL·해상 FCL을 소요 일수, 적합한 규모, 비용 특성, 흔한 실수 네 항목으로 한 표에서 비교합니다. 이어서 용적 중량 계산(0.12 CBM, 실중량 15kg이 왜 24kg으로 과금되는지), EXW·FOB·CIF·DDP의 예약·운임·위험 이전 차이, 완성복 화물과 혼적할 때 협조할 세 가지, 출하 서류에서 맞출 항목, 저가 신고·현지 비용 간과·성수기 선복 부족·샘플 혼적·특송 제한이라는 다섯 가지 실수를 정리합니다.",
        sum_fr="Les accessoires sont petits et de faible valeur, mais le fret et le délai décident si l'atelier attrape son navire. Un tableau compare express, aérien, groupage et conteneur complet selon le délai, l'échelle adaptée, le profil de coût et le piège propre à chacun. L'article explique ensuite le poids volumétrique (pourquoi un carton de 15 kg à 0,12 m3 est facturé 24 kg), la répartition des rôles entre EXW, FOB, CIF et DDP, les trois points sur lesquels une usine d'accessoires peut s'aligner sur la marchandise, les champs à réconcilier entre facture et packing list, et cinq erreurs qui retardent le dédouanement.",
        sum_es="Los accesorios son pequeños y de poco valor, pero el flete y el plazo deciden si el taller alcanza su buque. Una tabla compara exprés, aéreo, grupaje y contenedor completo por plazo, escala adecuada, perfil de coste y su error típico. Después explica el peso volumétrico (por qué un cartón de 15 kg y 0,12 m3 se factura como 24 kg), cómo reparten reserva, flete y riesgo EXW, FOB, CIF y DDP, los tres puntos en que una fábrica de accesorios puede alinearse con la prenda, los campos que deben cuadrar factura y packing list, y cinco errores que retrasan el despacho.",
    ),
    dict(
        slug="trim-order-quantity-tolerance-guide.html",
        body="blog/_body_qtytol.html",
        title_zh="辅料订单数量容差指南：多交、少交、备损率与补单怎么约定 | TAGE",
        title_en="Trims Order Quantity Tolerance: Over-Runs, Shortfalls and Spares | TAGE",
        title_ja="副資材の発注数量許容差ガイド：過納・不足・予備率・追加発注 | TAGE",
        title_ko="부자재 발주 수량 허용 오차 가이드: 초과 납품·부족·예비율 | TAGE",
        title_fr="Tolérance de quantité sur les accessoires : surplus, manquants, réserve | TAGE",
        title_es="Tolerancia de cantidad en accesorios: excesos, faltantes y reserva | TAGE",
        desc_zh="合同写 10000 张吊牌、交货 10300 张算超交吗？少了 200 张要不要补？本文讲清辅料数量差的四个来源、各品类常见容差区间与合同写法、多交少交的处理与结算口径、备损率怎么定、分色分码的最小量，以及补单与翻单的规则。来自东莞泰阁包装。",
        desc_en="Why trims quantities never match the order: tolerance bands by category, how to write them into the PO, over-runs, shortfalls, spares and reorder minimums.",
        desc_ja="注文 10,000 枚に対し 10,300 枚の納品は過納か。200 枚不足は補充すべきか。数量差の四つの発生源、品目別の許容差の目安と契約への書き方、過納・不足の扱いと精算、予備率の決め方、色・サイズ別の最小量、追加発注の条件を解説します。東莞泰閣包装。",
        desc_ko="10,000장 발주에 10,300장이 오면 초과 납품인지, 200장 부족은 보충해야 하는지. 수량 차이의 네 가지 원인, 품목별 허용 오차와 계약 표기, 초과·부족 처리와 정산, 예비율 설정, 색상·사이즈별 최소량, 재발주 조건을 정리합니다. 둥관 TAGE 패키징.",
        desc_fr="Tolérance de quantité : pourquoi le bon dit 10 000 et la livraison 10 300. Sources de l'écart, plages par article, rédaction au contrat, surplus et manquants, réserve, réassort.",
        desc_es="El pedido dice 10.000 colgantes y llegan 10.300, ¿exceso o faltante? Causas del desfase, bandas de tolerancia por artículo, redacción en el contrato, reserva y reposición.",
        crumb_zh="数量容差与备损率",
        crumb_en="Quantity Tolerance",
        crumb_ja="数量許容差と予備率",
        crumb_ko="수량 허용 오차·예비율",
        crumb_fr="Tolérance de quantité",
        crumb_es="Tolerancia de cantidad",
        h1_zh="辅料订单数量容差指南：多交、少交、备损率与补单怎么约定",
        h1_en="Trims Order Quantity Tolerance: Over-Runs, Shortfalls, Spares and Reorders",
        h1_ja="副資材の発注数量許容差ガイド：過納・不足・予備率・追加発注の決め方",
        h1_ko="부자재 발주 수량 허용 오차 가이드: 초과 납품·부족·예비율·재발주",
        h1_fr="Tolérance de quantité des accessoires : surplus, manquants, réserve et réassort",
        h1_es="Tolerancia de cantidad en accesorios: excesos, faltantes, reserva y reposición",
        tag_zh="订单与合同", tag_en="Ordering &amp; Contracts", tag_ja="発注・契約", tag_ko="발주·계약",
        tag_fr="Commande et contrat", tag_es="Pedidos y contratos",
        sum_zh="辅料订单最容易在「数量」上产生分歧：合同写 10000 张，交货 10300 张算不算超交，少 200 张要不要补。本文先拆出数量差的四个来源——印刷与模切放数、织造与裁切损耗、AQL 抽检取样、分色分码点数误差；再用一张表给出吊牌、织唛、洗水标、包装袋的常见容差区间与写法要点；随后讲清多交与少交分别在容差内外如何处理与结算、分批发货凑数为什么必须写明次数与时间；备损率按品类定（常规印刷件与织造件比例不同）而不是一律加量；分色分码的最小量为什么才是真正的成本门槛；最后给出补单与翻单不重开版的条件，以及下单前数量表要写清的六项与一条省事做法。",
        sum_en="Trims orders disagree most often about quantity: the PO says 10,000 and 10,300 arrive. This article first breaks the gap into four sources — printing and die-cutting overs, weaving and cutting waste, AQL samples removed, and counting errors across colour-ways; then gives tolerance bands and wording points for tags, woven labels, care labels and bags in one table; explains how over-runs and shortfalls are handled and invoiced inside and outside tolerance, and why split deliveries must fix their number and dates; sets spare rates by item rather than a flat percentage; shows why the minimum per colour-way is the real cost threshold; and closes with the conditions for a reorder without new tooling and the six points a quantity sheet should state.",
        sum_ja="副資材の発注で最も揉めるのは数量です。注文 10,000 枚に対し 10,300 枚の納品、200 枚の不足。本記事はまず数量差を四つの発生源——印刷・抜き型の予備、製織・断裁のロス、AQL 抜き取り、色・サイズ別の計数誤差——に分解し、タグ・織りラベル・洗濯表示ラベル・袋の許容差の目安と書き方の要点を一つの表で示します。次に範囲内・範囲外それぞれの過納と不足の扱いと精算、分割納入で回数と期日を明記すべき理由、品目別に決める予備率、色別最小量が実質的なコスト障壁である理由、版を作り直さずに追加発注できる条件、発注前の数量表に書くべき六項目をまとめます。",
        sum_ko="부자재 발주에서 가장 자주 다투는 것은 수량입니다. 발주 10,000장에 10,300장이 도착하거나 200장이 부족할 때의 기준이 필요합니다. 이 글은 먼저 수량 차이를 네 가지 원인—인쇄·타발 여유분, 제직·재단 손실, AQL 샘플링, 색상·사이즈별 계수 오차—으로 나누고, 행택·직조 라벨·세탁 라벨·봉투의 허용 오차 범위와 표기 요점을 한 표로 제시합니다. 이어서 범위 안팎의 초과·부족 처리와 정산, 분할 납품 시 횟수와 시점을 명시해야 하는 이유, 품목별 예비율 설정, 색상별 최소량이 실제 비용 장벽인 이유, 판 재제작 없이 재발주할 수 있는 조건과 발주 전 수량표에 적을 여섯 항목을 정리합니다.",
        sum_fr="C'est sur la quantité que les commandes d'accessoires se disputent le plus : 10 000 annoncées, 10 300 livrées. L'article décompose d'abord l'écart en quatre sources — surplus d'impression et de découpe, pertes de tissage et de coupe, prélèvements AQL, erreurs de comptage par coloris — puis donne en un tableau les plages de tolérance et la rédaction pour étiquettes, tissés, étiquettes d'entretien et sacs. Il précise le traitement et le règlement des surplus et manquants dans et hors tolérance, pourquoi une livraison fractionnée doit fixer nombre et dates, comment fixer la réserve par article, pourquoi le minimum par coloris est le vrai seuil, et les conditions d'un réassort sans nouvelle forme.",
        sum_es="Es en la cantidad donde más discrepan los pedidos: el bon dice 10.000 y llegan 10.300. El artículo descompone el desfase en cuatro causas —sobrantes de impresión y troquel, mermas de tejido y corte, muestras retiradas por AQL y errores de recuento por coloris—, y ofrece en una tabla las bandas de tolerancia y su redacción para colgantes, tejidos, etiquetas de cuidado y bolsas. Explica el tratamiento y la liquidación de excesos y faltantes dentro y fuera de banda, por qué una entrega parcial debe fijar número y fechas, cómo fijar la reserva por artículo, por qué el mínimo por coloris es el umbral real y las condiciones para reponer sin plancha nueva.",
    ),
]
