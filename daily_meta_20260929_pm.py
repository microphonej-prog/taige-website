#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-09-29 下午批次文章元数据（六语：zh-Hant 根 / en / ja / ko / fr / es）。

选题说明：任务主题池 30 个选题（含此前批次扩展的国别合规、EUDR/PPWR、原产地标识、
产前样、出货方式、数量容差、数字化打样、编码标准化等）均已上线，本次沿
「供应连续性/双源」与「采购沟通与书面确认」两个方向扩展新选题。写前已核对
blog/ 全量文件（192 篇）、en|ja|ko|fr|es/blog/ 与 sitemap.xml（1176 个 <loc>）：

- 供应中断与备选供应商（trim-supply-continuity-guide）：全站检索「备选供应商 / 双源 /
  供应中断 / BCP」命中 ≤1 次（仅 garment-trim-book-guide 提及一次），无专文。
  现有 garment-trims-supplier-audit 讲验厂、garment-trims-sourcing-guide 讲怎么选供应商、
  garment-trims-inventory-management 讲安全库存、trim-tooling-ownership-guide 讲版费权属，
  都没有讲「四类断供的差别、怎么低成本养第二家、替代料验什么、三级应急与合同条款」。
  与其为互补而非重复。

- 采购沟通与书面确认（trim-supplier-communication-guide）：无任何专文讲询价/催货/
  质量反馈的写法。现有 apparel-trims-spec-sheet-guide 讲规格书字段、
  garment-trims-order-tracking-guide 讲进度跟踪、trim-quotation-comparison-guide 讲报价比对，
  本文聚焦「口头确认怎么书面化、批注与版本、催货三段式、质量反馈的证据与诉求、
  跨语言单位歧义」，与上述三篇互补。
"""

ARTICLES = [
    dict(
        slug="trim-supply-continuity-guide.html",
        body="blog/_body_continuity.html",
        title_zh="服装辅料供应中断与备选供应商指南：双源、替代料与应急预案 | TAGE",
        title_en="Trims Supply Continuity: Second Sourcing and Substitutes | TAGE",
        title_ja="副資材の供給継続ガイド：第二供給先・代替素材・緊急対応 | TAGE",
        title_ko="부자재 공급 연속성 가이드: 2차 공급사·대체 소재·비상 대응 | TAGE",
        title_fr="Continuité d'approvisionnement : seconde source et substitution | TAGE",
        title_es="Continuidad de suministro: segunda fuente y sustitutos | TAGE",
        desc_zh="辅料断供往往不是价格问题，而是只有一家能做。本文拆解断料、断产能、断工艺与断物流四类风险的差别，列出吊牌、织唛、洗水标与包装袋最容易单点依赖的环节，讲清低成本养备选供应商的四个动作、替代料必须实测的五项与三级应急响应。来自东莞泰阁包装。",
        desc_en="Trims supply continuity: four kinds of supply failure, which trims depend on a single source, how to keep a second supplier and what to test on substitutes.",
        desc_ja="副資材の供給継続ガイド。材料切れ・能力不足・加工途絶・物流遅延という4種類の供給停止の違い、一社依存になりやすい副資材、低コストで第二供給先を維持する4つの行動、代替素材で実測すべき5項目、3段階の緊急対応と契約条項を解説します。東莞泰閣包装。",
        desc_ko="부자재 공급 연속성 가이드. 자재 부족·생산 능력 부족·공정 중단·물류 지연 네 가지 유형의 차이, 단일 공급에 취약한 부자재, 낮은 비용으로 2차 공급사를 유지하는 네 가지 방법, 대체 소재에서 실측할 다섯 항목, 3단계 비상 대응과 계약 조항을 정리합니다. 둥관 TAGE 패키징.",
        desc_fr="Continuité d'approvisionnement des accessoires : quatre types de rupture, les pièces les plus exposées au mono-sourcing et comment entretenir une seconde source à faible coût.",
        desc_es="Continuidad de suministro: cuatro tipos de ruptura, los accesorios más expuestos al proveedor único y cómo mantener una segunda fuente viable.",
        crumb_zh="供应中断与备选供应商",
        crumb_en="Supply Continuity",
        crumb_ja="供給継続と第二供給先",
        crumb_ko="공급 연속성·2차 공급사",
        crumb_fr="Continuité d'approvisionnement",
        crumb_es="Continuidad de suministro",
        h1_zh="服装辅料供应中断风险指南：备选供应商、替代料与应急预案",
        h1_en="Trims Supply Continuity: Second Sourcing, Substitutes and Contingency Plans",
        h1_ja="副資材の供給中断リスクガイド：第二供給先・代替素材・緊急対応",
        h1_ko="부자재 공급 중단 리스크 가이드: 2차 공급사·대체 소재·비상 대응",
        h1_fr="Risque de rupture d'approvisionnement : seconde source et substituts",
        h1_es="Riesgo de ruptura de suministro: segunda fuente y sustitutos",
        tag_zh="供应风险与双源", tag_en="Supply Risk &amp; Sourcing", tag_ja="供給リスクと複数購買", tag_ko="공급 리스크·복수 구매",
        tag_fr="Risque d'approvisionnement", tag_es="Riesgo de suministro",
        sum_zh="辅料在成衣成本里占比不高，却卡在交付链最后一道：缺一张吊牌，成衣做好了也出不了货。本文先把断料、断产能、断工艺、断物流四类风险分开讲，指出各自的缓解手段完全不同；再用一张表列出吊牌、提花织唛、洗水标、包装袋与环保纸袋最常见的单点依赖原因与优先缓解手段。随后给出低成本养备选供应商的四个动作：每季跑一次小单、两家共用一份规格书与编码、标准实样双方各留一套、刀模与源文件归自己；替代料上大货前必须实测的五项：颜色允差写数字、手感与厚度、耐洗与耐摩擦、合规声明、上机适配。最后给出一级到三级的应急响应分档，以及产能预留、变更通知、不可抗力与双源份额四条合同条款。",
        sum_en="Trims are a small share of garment cost but sit at the very end of the delivery chain: one missing tag and finished garments cannot ship. The article separates four kinds of supply failure — material, capacity, process and logistics — each with a different remedy, then tabulates where hang tags, jacquard labels, care labels, bags and eco paper bags are most likely to depend on a single source and how to reduce the exposure. It sets out four low-cost ways to keep a second supplier alive (a small order each season, one shared spec and part code, two sets of physical standards, tooling and files owned by the brand), the five things to test before a substitute goes to bulk (colour tolerance in numbers, hand feel and thickness, wash and rub resistance, compliance claims, machine compatibility), a three-tier response plan, and four contract clauses covering capacity reservation, change notification, force majeure and split share.",
        sum_ja="副資材はコスト比率こそ小さいものの納品チェーンの最後尾にあり、タグ1枚が欠けるだけで製品を出荷できません。本記事はまず材料切れ・能力不足・加工途絶・物流遅延の4類型を分け、緩和策がそれぞれ異なることを示します。続いてタグ、ジャカード織りラベル、洗濯表示ラベル、包装袋、エコ紙袋について、一社依存になりやすい原因と優先緩和策を表で整理。低コストで第二供給先を維持する4つの行動（季節ごとの小ロット、共通の仕様書とコード、実物見本の双方保管、型とデータの自社所有）、代替素材を量産前に実測すべき5項目（色許容差の数値化、風合いと厚み、耐洗濯・耐摩擦、法規表示、機械適合性）、3段階の緊急対応、能力確保・変更通知・不可抗力・シェア配分の4条項を掲載します。",
        sum_ko="부자재는 원가 비중이 작지만 납품 체인의 맨 끝에 있어, 행택 한 장이 없으면 완성된 의류도 출고할 수 없습니다. 이 글은 자재 부족·생산 능력 부족·공정 중단·물류 지연 네 유형을 구분하고 각각의 대응이 다르다는 점을 설명합니다. 이어서 행택, 자카드 라벨, 세탁 표시 라벨, 포장 백, 친환경 종이백의 단일 공급 의존 원인과 우선 완화 수단을 표로 정리합니다. 낮은 비용으로 2차 공급사를 유지하는 네 가지 행동(시즌별 소량 발주, 공통 사양서와 코드, 실물 기준 양측 보관, 금형과 파일 자사 소유), 대체 소재 양산 전 실측할 다섯 항목(색차 허용치 수치화, 촉감과 두께, 세탁·마찰 내구성, 규정 표시, 설비 적합성), 3단계 비상 대응, 생산 능력 예약·변경 통지·불가항력·물량 배분 네 조항을 제시합니다.",
        sum_fr="Les accessoires pèsent peu dans le coût du vêtement mais se trouvent en bout de chaîne : une seule étiquette manquante et le produit fini ne part pas. L'article distingue quatre types de rupture — matière, capacité, procédé, logistique — chacune appelant une réponse différente, puis présente sous forme de tableau l'origine du mono-sourcing pour les étiquettes suspendues, labels jacquard, étiquettes d'entretien, sacs et sacs papier, avec la mesure prioritaire. Il détaille quatre moyens peu coûteux d'entretenir une seconde source, les cinq points à tester avant de lancer un substitut en production (tolérance couleur chiffrée, toucher et épaisseur, tenue au lavage et à l'abrasion, allégations, compatibilité machine), un plan de réponse en trois niveaux et quatre clauses contractuelles : capacité réservée, notification de changement, force majeure et répartition des volumes.",
        sum_es="Los accesorios pesan poco en el coste de la prenda pero están al final de la cadena: falta una etiqueta y el producto terminado no sale. El artículo distingue cuatro tipos de ruptura —material, capacidad, proceso y logística—, cada uno con una respuesta distinta, y presenta en una tabla el origen de la dependencia de fuente única en etiquetas troqueladas, tejidas jacquard, de cuidado, bolsas y bolsas de papel, con la medida prioritaria. Detalla cuatro formas económicas de mantener una segunda fuente, los cinco puntos que hay que ensayar antes de producir con un sustituto (tolerancia de color en cifras, tacto y grosor, resistencia a lavado y roce, declaraciones, compatibilidad con máquina), un plan de respuesta en tres niveles y cuatro cláusulas: capacidad reservada, notificación de cambios, fuerza mayor y reparto de volumen.",
    ),
    dict(
        slug="trim-supplier-communication-guide.html",
        body="blog/_body_comm.html",
        title_zh="服装辅料沟通指南：询价、催货与质量反馈怎么写 | TAGE",
        title_en="Trims Supplier Communication: Enquiries, Chasing, Complaints | TAGE",
        title_ja="副資材サプライヤーとのやり取り：見積・督促・品質連絡の書き方 | TAGE",
        title_ko="부자재 공급사 커뮤니케이션: 견적·독촉·품질 피드백 작성법 | TAGE",
        title_fr="Communication fournisseur : demandes, relances, réclamations | TAGE",
        title_es="Comunicación con proveedores: consultas, plazos, reclamaciones | TAGE",
        desc_zh="辅料确认大多在微信和电话里完成，等到大货到仓才发现颜色不像、孔位偏了。本文讲清三类必须书面化的确认、询价一次问清的六个字段与漏写后果、批注与版本怎么给才可执行、催货的三段式写法、质量反馈的证据与诉求，以及跨语言的口径统一。来自东莞泰阁包装。",
        desc_en="How to write trims enquiries, chase-ups and quality complaints: what must be confirmed in writing, and how to cut ambiguity across languages and time zones.",
        desc_ja="副資材のやり取り実務。書面化すべき3つの確認（色許容差・寸法位置・納期ロット）、見積メールで一度に聞く6項目と書き漏らしの影響、実行可能な注記の出し方、督促の3段落構成、品質連絡の証拠と要求、言語をまたぐ単位・用語の統一を解説します。東莞泰閣包装。",
        desc_ko="부자재 커뮤니케이션 실무. 서면화해야 할 세 가지 확인(색차 허용치·치수 위치·납기 로트), 견적 메일에서 한 번에 묻는 여섯 항목과 누락 시 결과, 실행 가능한 주석 작성법, 3단 구성 독촉, 품질 피드백의 증거와 요구, 언어 간 단위·용어 통일을 다룹니다. 둥관 TAGE 패키징.",
        desc_fr="Écrire des demandes, relances et réclamations efficaces : ce qui doit être confirmé par écrit, annotations et versions, et comment réduire l'ambiguïté.",
        desc_es="Cómo redactar consultas, recordatorios y reclamaciones que funcionan: qué confirmar por escrito, anotaciones y versiones, y cómo reducir la ambigüedad.",
        crumb_zh="采购沟通与书面确认",
        crumb_en="Buyer-Supplier Communication",
        crumb_ja="発注コミュニケーション",
        crumb_ko="발주 커뮤니케이션",
        crumb_fr="Communication d'achat",
        crumb_es="Comunicación de compra",
        h1_zh="服装辅料沟通指南：询价一次问清、催货与质量反馈怎么写",
        h1_en="Trims Communication Guide: Ask Once, Chase Delivery, Report Quality",
        h1_ja="副資材コミュニケーションガイド：見積りを一度で聞き、納期を促し、品質を伝える",
        h1_ko="부자재 커뮤니케이션 가이드: 한 번에 묻고, 납기를 관리하고, 품질을 전달하기",
        h1_fr="Guide de communication : demander une fois, relancer, signaler la qualité",
        h1_es="Guía de comunicación: preguntar una vez, reclamar plazo, reportar calidad",
        tag_zh="采购沟通与跟单", tag_en="Buyer Communication", tag_ja="発注コミュニケーション", tag_ko="발주·진행 관리",
        tag_fr="Communication acheteur", tag_es="Comunicación de compra",
        sum_zh="辅料单价低、金额小，很多确认就在微信和电话里完成，等到大货到仓才发现颜色不像、孔位偏了、交期晚了。本文第一节先把三类必须书面化的确认说清：颜色要色号加允差加观察光源，尺寸位置要有毫米数字与标注图，交期批次要有数量、容差与最晚到货日。第二节用一张表列出询价最常漏写的六个字段（用途款式、尺寸公差、材质工艺、数量损耗、交期地点、合规文件）与各自的后果和推荐写法，说明一封完整询价通常能省掉三轮来回。第三节讲批注与版本：一条批注只对一个点、文件名带版本与日期、改动超过三处就重新出图、电话后补一封确认信。第四节给出催货的三段式——事实、影响、请求，并用 T-7、T-3 进度节点替代天天追问。第五节讲质量反馈的三件事：附证据（批次号与抽检数量）、给范围（全检还是抽检）、提具体诉求与期限，并保留邮件与照片。最后讲跨语言跨时区的口径统一：单位术语先定、短句编号、约定响应时限、避开春节长假。",
        sum_en="Trims are cheap, so most confirmations happen in a chat or a call — and the mismatch only surfaces when the bulk lands with the wrong shade, a decentred hole or a late date. Section one names the three confirmations that must be written: colour with shade reference, tolerance and viewing light; size and placement in millimetres with an annotated drawing; lead time with quantity, tolerance and latest arrival date. Section two tabulates the six items most often missing from an enquiry — use and style, size and tolerance, material and process, quantity and waste, date and destination, compliance and documents — with the consequence of each omission and how to write it, because one complete enquiry usually saves three rounds. Section three covers annotations and versions: one annotation per point, version and date in filenames, a redraw after three changes, and a written recap after every call. Section four gives the three-line chase-up — facts, impact, request — with T-7 and T-3 checkpoints instead of daily nagging. Section five covers evidence with batch numbers, scope of inspection, and a specific remedy with deadlines, filed by email. The close handles units, numbered short lines, agreed response times and planning around Chinese New Year.",
        sum_ja="副資材は単価も金額も小さく、確認はチャットや電話で済みがちです。色が合わない、穴位置がずれた、納期が遅れたと気づくのは現物到着後になります。第1節では書面化が必須の3つの確認（色は色番・許容差・観察光源、寸法と位置はmmと注記図、納期とロットは数量・許容差・最遅着日）を示します。第2節では見積依頼で最も書き漏らしやすい6項目（用途と型、サイズと公差、素材と加工、数量とロス、納期と納入先、法規と書類）を、書き漏らした結果と推奨表現とともに表に整理。完全な依頼1通で往復3回分を省けます。第3節は注記と版管理（1注記1ポイント、ファイル名に版と日付、3点超の修正は図の出し直し、電話後の確認メール）。第4節は督促の3段落（事実・影響・依頼）とT-7・T-3の進捗報告。第5節は品質連絡の証拠・範囲・要求と記録の保管。最後に単位と用語の統一、短い番号付き文、回答期限、春節前の計画を扱います。",
        sum_ko="부자재는 단가와 금액이 작아 대부분의 확인이 채팅과 전화로 끝나고, 색이 다르거나 타공 위치가 어긋나거나 납기가 늦었다는 사실은 실물이 도착한 뒤에 드러납니다. 1절은 서면화가 필수인 세 가지 확인(색상은 색상 번호·허용치·관찰 광원, 치수와 위치는 mm 수치와 주석 도면, 납기와 로트는 수량·허용치·최종 도착일)을 제시합니다. 2절은 견적 문의에서 가장 자주 빠지는 여섯 항목(용도와 스타일, 치수와 공차, 소재와 공정, 수량과 손실, 납기와 납품지, 규정과 서류)을 누락 시 결과와 권장 작성법으로 표에 정리합니다. 3절은 주석과 버전(주석 하나에 한 가지, 파일명에 버전과 날짜, 세 곳 초과 수정 시 도면 재작성, 통화 후 확인 메일), 4절은 독촉 3단 구성(사실·영향·요청)과 T-7·T-3 보고 시점, 5절은 품질 피드백의 증거·범위·요구와 기록 보관, 마지막으로 단위와 용어 통일, 짧은 번호 문장, 회신 기한, 춘절 전 계획을 다룹니다.",
        sum_fr="Les accessoires sont petits et bon marché : les validations se font par message ou au téléphone, et l'écart n'apparaît qu'à l'arrivée du lot. La première partie nomme les trois validations écrites indispensables : couleur avec référence, tolérance et lumière d'observation ; dimensions et positions en millimètres avec plan annoté ; délai avec quantité, tolérance et date d'arrivée au plus tard. La deuxième présente les six éléments les plus souvent oubliés dans une demande — usage et modèle, dimensions, matière et procédé, quantité et pertes, délai et destination, conformité et documents — avec la conséquence de chaque oubli, car une demande complète économise trois allers-retours. La troisième traite annotations et versions : une annotation par point, version et date dans le nom de fichier, redessin après trois corrections, récapitulatif écrit après chaque appel. La quatrième propose la relance en trois temps — faits, impact, demande — avec des points d'étape à J-7 et J-3. La cinquième couvre preuves, périmètre et demande chiffrée. La conclusion traite unités, phrases courtes numérotées, délais de réponse et anticipation du Nouvel An chinois.",
        sum_es="Los accesorios son baratos, así que casi todo se confirma por chat o teléfono, y el desajuste aparece al llegar el lote. La primera parte nombra las tres confirmaciones que deben ser escritas: color con referencia, tolerancia y luz de observación; medidas y posiciones en milímetros con plano anotado; plazo con cantidad, tolerancia y fecha límite. La segunda recoge los seis puntos que más se olvidan en una consulta —uso y modelo, medidas y tolerancia, material y proceso, cantidad y merma, plazo y destino, cumplimiento y documentos— con la consecuencia de cada omisión, porque una consulta completa ahorra tres rondas. La tercera trata anotaciones y versiones: una anotación por punto, versión y fecha en el nombre, redibujar tras tres cambios y resumen escrito tras cada llamada. La cuarta ofrece el recordatorio en tres partes —hechos, impacto, petición— con hitos a T-7 y T-3. La quinta cubre pruebas, alcance y petición concreta. Cierra con unidades, frases numeradas, tiempos de respuesta y planificación del Año Nuevo chino.",
    ),
]
