#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-11 上午批次（08:00）每日更新：2 篇新文章元数据（六语：zh-Hant 根 / en / ja / ko / fr / es）

选题说明（主题池 30 项连同既有扩展均已上线；本次沿两个尚未独立成文的方向扩展，
已核对 blog/、en|ja|ko|fr|es/blog/ 与 sitemap.xml 无重复 slug，并 grep 全站确认关键词覆盖情况）：

- pfas-restrictions-apparel-trims-guide：全站 grep「PFAS / PFHxA / AB 1817 / 總有機氟 / TOF」= 0 命中，
  仅在 reach-svhc-apparel-trims-guide、trim-third-party-testing-guide 中顺带提及；
  雨衣防水辅料文章讲的是拉链与贴合工艺，未涉及含氟限制与替代。
  本文按「PFAS 定义与辅料被牵连原因 → 辅料含氟七个位置对照表 → 欧盟 PFHxA 与美国各州时点表 →
  客户索要的三类文件 → 测试方法（靶向分析与总有机氟）与避坑 → 无氟替代路线与成本感」展开，
  事实依据为 REACH 附件 XVII PFHxA 限制（2026-10-10 适用）、ECHA 通用限制评估进程（RAC 2026-03 意见）、
  加州 AB 1817 与纽约州 ECL §37-0121 等公开法规文本，正文已加「以官方最新文本为准」免责说明。

- eu-forced-labour-regulation-apparel-trims：全站 grep「強制労働 / 强迫劳动 / EUFLR / 2024/3015」= 0 命中
  （仅 uflpa 一文提到美国法）。本文讲欧盟条例本身：管产品不管企业规模、调查—禁令机制与 30 个工作日执行期、
  与 UFLPA／CSDDD／社会责任审核的分工对照表、辅料供应商被问到的四个原因、客户资料清单与常见缺口、
  以及到 2027 年前的六项准备动作。关键日期（2024-12-13 生效、2027-12-14 适用）来自委员会官方页面与条例文本。
"""

ARTICLES = [
    dict(
        slug="pfas-restrictions-apparel-trims-guide.html",
        body="blog/_body_pfas.html",
        title_zh="PFAS 限制与服装辅料合规指南：欧盟 PFHxA 限值与美国各州禁令 | TAGE",
        title_en="PFAS Restrictions for Apparel Trims: EU PFHxA Limits &amp; US State Bans | TAGE",
        title_ja="PFAS 規制と衣料副資材の対応ガイド：EU PFHxA 制限値と米国各州の禁止 | TAGE",
        title_ko="PFAS 규제와 의류 부자재 대응 가이드: EU PFHxA 한도와 미국 주별 금지 | TAGE",
        title_fr="Restrictions PFAS et accessoires textiles : limites PFHxA de l'UE et interdictions américaines | TAGE",
        title_es="Restricciones PFAS y accesorios textiles: límites PFHxA de la UE y prohibiciones en EE. UU. | TAGE",
        desc_zh="PFAS 限制与服装辅料合规指南：欧盟 PFHxA 限值 2026 年 10 月起适用于服装配件鞋类、美国加州 AB 1817 与纽约州法门槛怎么算、辅料含氟的七个位置、总有机氟与靶向分析怎么选、无氟替代路线与成本，附客户文件清单。来自东莞泰阁包装。",
        desc_en="PFAS guide for apparel trims: EU PFHxA limits from October 2026, California and New York state thresholds, where fluorine hides, and fluorine-free options.",
        desc_ja="衣料副資材の PFAS 対応ガイド。2026 年 10 月からの EU PFHxA 制限、米国カリフォルニア AB 1817 とニューヨーク州の基準、副資材でフッ素が潜む 7 か所、総有機フッ素とターゲット分析の使い分け、フッ素フリー代替とコストを解説。東莞泰閣包装。",
        desc_ko="의류 부자재 PFAS 대응 가이드. 2026년 10월부터 시행되는 EU PFHxA 한도, 미국 캘리포니아 AB 1817과 뉴욕주 기준, 부자재에서 불소가 숨는 일곱 곳, 총 유기불소와 표적 분석 선택법, 무불소 대안과 비용을 정리했습니다. 둥관 TAGE 패키징.",
        desc_fr="Guide PFAS des accessoires textiles : limites PFHxA de l'UE dès octobre 2026, seuils californiens et new-yorkais, où le fluor se cache, méthodes d'essai et alternatives sans fluor.",
        desc_es="Guía PFAS para accesorios textiles: límites PFHxA de la UE desde octubre de 2026, umbrales de California y Nueva York, dónde se esconde el flúor, métodos de ensayo y alternativas sin flúor.",
        crumb_zh="PFAS 限制与辅料合规",
        crumb_en="PFAS Restrictions &amp; Trims",
        crumb_ja="PFAS 規制と副資材対応",
        crumb_ko="PFAS 규제와 부자재 대응",
        crumb_fr="Restrictions PFAS et accessoires",
        crumb_es="Restricciones PFAS y accesorios",
        h1_zh="PFAS 限制与服装辅料合规指南：从法规时点到无氟替代",
        h1_en="PFAS Restrictions and Apparel Trims: From Deadlines to Fluorine-Free Options",
        h1_ja="PFAS 規制と衣料副資材の対応：規制スケジュールからフッ素フリー代替まで",
        h1_ko="PFAS 규제와 의류 부자재 대응: 규제 시점부터 무불소 대안까지",
        h1_fr="Restrictions PFAS et accessoires textiles : du calendrier aux solutions sans fluor",
        h1_es="Restricciones PFAS y accesorios textiles: del calendario a las alternativas sin flúor",
        tag_zh="合规指南",
        tag_en="Compliance Guide",
        tag_ja="コンプライアンスガイド",
        tag_ko="컴플라이언스 가이드",
        tag_fr="Guide conformité",
        tag_es="Guía de cumplimiento",
        sum_zh="PFAS 是当下纺织供应链里变化最快的限制：欧盟对 PFHxA 的浓度限值自 2026 年 10 月 10 日起适用于面向公众的服装、配件与鞋类（PFHxA 及其盐类 25 ppb、相关物质 1,000 ppb，按均质材料计），2027 年 10 月 10 日扩展到其他纺织品；美国加州 AB 1817 与纽约州法早在 2025 年 1 月 1 日就已生效，加州按总有机氟判定（100 ppm，2027 年起 50 ppm），极端湿况户外服装延至 2028 年。文章先解释辅料为什么会被牵连，再用一张表列出辅料最容易含氟的七个位置（防泼水与防污整理、防水拉链贴膜、合成革与皮饰涂饰、热转印膜与不干胶离型纸、防油纸袋涂层、硅胶 pvc 橡胶配件、脱模剂等加工助剂残留），随后是欧盟与美国各州的时点门槛对照、客户索要的三类文件（BOM 物料声明、测试报告、替代方案说明）、靶向分析与总有机氟两种测试的用法与四个常见坑，最后给出无氟替代路线与成本时间的现实判断。",
        sum_en="PFAS is the fastest-moving restriction in textile supply chains. EU concentration limits for PFHxA apply to clothing, accessories and footwear for the general public from 10 October 2026 — 25 ppb for PFHxA and its salts, 1,000 ppb for related substances measured in homogeneous material — extending to other textiles on 10 October 2027. California AB 1817 and New York law have applied since 1 January 2025, with California judging on total organic fluorine (100 ppm, dropping to 50 ppm in 2027) and severe-wet outdoor apparel deferred to 2028. The guide explains why trims get pulled in, then lists the seven places fluorine most often hides — water and stain repellent finishes, waterproof zip membranes, synthetic leather and leather finishes, heat transfer films and adhesive release liners, grease barriers on paper bags, silicone pvc and rubber parts, and processing aid residues from mould release agents. A timeline table for the EU and US states follows, then the three document sets customers request (BOM material declarations, test reports, substitution notes), how targeted analysis and total organic fluorine testing divide the work with four common pitfalls, and a realistic view of fluorine-free alternatives, cost and timing.",
        sum_ja="PFAS は現在の繊維サプライチェーンで最も動きの速い規制です。EU の PFHxA 濃度制限は 2026 年 10 月 10 日から一般向けの衣類・付属品・履物に適用され（PFHxA とその塩 25 ppb、関連物質 1,000 ppb、均質材料基準）、2027 年 10 月 10 日にその他の繊維製品へ拡大します。米国カリフォルニア AB 1817 とニューヨーク州法は 2025 年 1 月 1 日から施行中で、カリフォルニアは総有機フッ素で判定（100 ppm、2027 年から 50 ppm）、厳しい湿潤環境向けアウトドア衣料は 2028 年まで猶予です。本記事は副資材が対象になる理由を説明し、フッ素が潜みやすい 7 か所（撥水・防汚加工、撥水ファスナーの膜、合成皮革と皮革仕上げ、熱転写フィルムと粘着離型紙、紙袋の防油コート、シリコン・PVC・ゴム部材、離型剤など加工助剤の残留）を一覧化。続いて EU と米国各州の時期・基準の対照表、顧客が求める 3 種類の書類（BOM 材料宣言、試験報告、代替案の説明）、ターゲット分析と総有機フッ素の使い分けと 4 つの落とし穴、フッ素フリー代替の現実的なコストと時間を示します。",
        sum_ko="PFAS는 현재 섬유 공급망에서 가장 빠르게 변하는 규제입니다. EU의 PFHxA 농도 한도는 2026년 10월 10일부터 일반 소비자용 의류·부속품·신발에 적용되며(PFHxA와 그 염 25 ppb, 관련 물질 1,000 ppb, 균질 재료 기준), 2027년 10월 10일 기타 섬유로 확대됩니다. 미국 캘리포니아 AB 1817과 뉴욕주 법은 2025년 1월 1일부터 시행 중이고, 캘리포니아는 총 유기불소로 판정(100 ppm, 2027년부터 50 ppm), 혹독한 습윤 환경용 아웃도어 의류는 2028년까지 유예됩니다. 이 글은 부자재가 대상이 되는 이유를 설명하고 불소가 숨기 쉬운 일곱 곳(발수·방오 가공, 발수 지퍼 멤브레인, 합성피혁과 가죽 마감, 열전사 필름과 점착 이형지, 종이백 방유 코팅, 실리콘·PVC·고무 부품, 이형제 등 가공 조제 잔류)을 표로 정리합니다. 이어 EU와 미국 주별 시점·기준 대조표, 고객이 요구하는 세 가지 서류(BOM 자재 선언, 시험 성적서, 대체안 설명), 표적 분석과 총 유기불소의 역할 분담과 네 가지 함정, 무불소 대안의 비용과 시간에 대한 현실적 판단을 제시합니다.",
        sum_fr="Les PFAS sont la restriction la plus mouvante des chaînes textiles. Les limites de PFHxA s'appliquent dans l'UE aux vêtements, accessoires et chaussures grand public depuis le 10 octobre 2026 — 25 ppb pour le PFHxA et ses sels, 1 000 ppb pour les substances apparentées, sur matériau homogène — et s'étendent aux autres textiles le 10 octobre 2027. L'AB 1817 californien et la loi de New York s'appliquent depuis le 1er janvier 2025, la Californie jugeant sur le fluor organique total (100 ppm, 50 ppm en 2027), l'outdoor pour conditions très humides étant reporté à 2028. Le guide explique pourquoi les accessoires sont concernés, puis liste les sept endroits où le fluor se cache : finitions déperlantes et antitache, membranes de fermetures étanches, cuir synthétique et finitions du cuir, films de transfert et papier siliconé, barrières anti-graisse des sacs papier, pièces silicone, PVC et caoutchouc, résidus d'agents de démoulage. Suivent un tableau de calendrier UE et États-Unis, les trois dossiers demandés par les clients (déclarations matière, rapports d'essai, notes de substitution), la répartition entre analyse ciblée et fluor organique total avec quatre pièges fréquents, et une vision réaliste des alternatives sans fluor, de leur coût et de leur délai.",
        sum_es="Los PFAS son la restricción que más rápido cambia en las cadenas textiles. Los límites de PFHxA se aplican en la UE a prendas, accesorios y calzado de uso general desde el 10 de octubre de 2026 —25 ppb para PFHxA y sus sales, 1.000 ppb para sustancias relacionadas, en material homogéneo— y se amplían a otros textiles el 10 de octubre de 2027. La AB 1817 de California y la ley de Nueva York rigen desde el 1 de enero de 2025, con California juzgando por flúor orgánico total (100 ppm, 50 ppm desde 2027) y la ropa de exterior para condiciones muy húmedas aplazada a 2028. La guía explica por qué se ven implicados los accesorios y enumera los siete puntos donde se esconde el flúor: acabados hidrófugos y antimanchas, membranas de cremalleras estancas, cuero sintético y acabados de piel, films de transferencia y papel siliconado, barreras antigrasa de bolsas de papel, piezas de silicona, PVC y caucho, y residuos de desmoldantes. Siguen una tabla de calendario UE y EE. UU., los tres documentos que piden los clientes (declaraciones de material, informes de ensayo, notas de sustitución), el reparto entre análisis dirigido y flúor orgánico total con cuatro trampas frecuentes, y una visión realista de las alternativas sin flúor, su coste y sus plazos.",
    ),
    dict(
        slug="eu-forced-labour-regulation-apparel-trims.html",
        body="blog/_body_flr.html",
        title_zh="欧盟强迫劳动条例与服装辅料供应链指南：2027 年禁令前要准备什么 | TAGE",
        title_en="EU Forced Labour Regulation for Apparel Trims: Preparing Before 2027 | TAGE",
        title_ja="EU 強制労働規則と衣料副資材のサプライチェーン対応：2027 年までに準備すること | TAGE",
        title_ko="EU 강제노동 규정과 의류 부자재 공급망 대응: 2027년 금지 전에 준비할 것 | TAGE",
        title_fr="Règlement européen sur le travail forcé et accessoires textiles : se préparer avant 2027 | TAGE",
        title_es="Reglamento europeo sobre trabajo forzoso y accesorios textiles: prepararse antes de 2027 | TAGE",
        desc_zh="欧盟强迫劳动条例 (EU) 2024/3015 指南：2027 年 12 月 14 日起产品禁令怎么执行、主管机关调查与 30 个工作日下架期限、与 UFLPA 和 CSDDD 的分工、辅料供应商为何被问、客户资料清单与常见缺口，以及 2027 年前可以落地的六项准备。来自东莞泰阁包装。",
        desc_en="EU Forced Labour Regulation guide for apparel trims: the 14 December 2027 product ban, how national authorities investigate, and the documents to prepare.",
        desc_ja="EU 強制労働規則（2024/3015）ガイド。2027 年 12 月 14 日からの製品禁止の仕組み、主管機関の調査と 30 営業日の対応期限、UFLPA・CSDDD・社会監査との役割分担、副資材サプライヤーが問われる理由、顧客が求める資料と不足しがちな点、2027 年までの 6 つの準備を解説。東莞泰閣包装。",
        desc_ko="EU 강제노동 규정(2024/3015) 가이드. 2027년 12월 14일부터 적용되는 제품 금지 구조, 당국 조사와 30영업일 이행 기한, UFLPA·CSDDD·사회 감사와의 역할 분담, 부자재 공급업체가 요구받는 이유, 고객 요구 서류와 흔한 결함, 2027년 전 여섯 가지 준비를 정리했습니다. 둥관 TAGE 패키징.",
        desc_fr="Guide du règlement européen sur le travail forcé pour les accessoires textiles : interdiction dès le 14 décembre 2027, enquêtes des autorités et six documents à préparer.",
        desc_es="Guía del Reglamento europeo sobre trabajo forzoso para accesorios textiles: prohibición desde el 14 de diciembre de 2027, investigaciones y seis documentos a preparar.",
        crumb_zh="欧盟强迫劳动条例",
        crumb_en="EU Forced Labour Regulation",
        crumb_ja="EU 強制労働規則",
        crumb_ko="EU 강제노동 규정",
        crumb_fr="Règlement travail forcé UE",
        crumb_es="Reglamento trabajo forzoso UE",
        h1_zh="欧盟强迫劳动条例与服装辅料供应链指南：2027 年前要准备什么",
        h1_en="The EU Forced Labour Regulation and Apparel Trims: What to Prepare Before 2027",
        h1_ja="EU 強制労働規則と衣料副資材サプライチェーン：2027 年までに準備すべきこと",
        h1_ko="EU 강제노동 규정과 의류 부자재 공급망: 2027년 전에 준비할 것",
        h1_fr="Règlement européen sur le travail forcé et accessoires textiles : quoi préparer avant 2027",
        h1_es="Reglamento europeo sobre trabajo forzoso y accesorios textiles: qué preparar antes de 2027",
        tag_zh="合规指南",
        tag_en="Compliance Guide",
        tag_ja="コンプライアンスガイド",
        tag_ko="컴플라이언스 가이드",
        tag_fr="Guide conformité",
        tag_es="Guía de cumplimiento",
        sum_zh="欧盟《禁止强迫劳动产品条例》(EU) 2024/3015 已于 2024 年 12 月 13 日生效，产品禁令自 2027 年 12 月 14 日起适用：全部或部分以强迫劳动制造的产品不得投放欧盟市场、不得在欧盟提供、也不得从欧盟出口。它与美国 UFLPA 的边境推定不同，走的是「风险数据库＋主管机关调查＋对具体产品下达禁令」的路径，企业需在决定规定期限内执行（一般 30 个工作日），处罚由成员国设定，且不区分企业规模。文章先梳理条例的禁止范围与机制，再用一张表区分它与 UFLPA、CSDDD、BSCI 社会责任审核各自管什么；随后解释辅料供应商为什么会被问到（订单按成衣评估、纺纱织造染整印刷电镀等外包工序、临时工与劳务派遣、纸浆棉纱等原料产地），列出客户常要的供应链地图、产地声明、用工工时记录与审核证书及各自的常见缺口，最后给出 2027 年前可以落地的六项准备：按产品建供应链地图、登记派遣用工、让考勤工资工时三表对上、向上游索取产地声明、保持审核在有效期内覆盖实际厂区、出货文件按批次归档并与 UFLPA 台账共用编号。",
        sum_en="The EU Forced Labour Regulation, Regulation (EU) 2024/3015, entered into force on 13 December 2024 and its product ban applies from 14 December 2027: goods made wholly or partly with forced labour may not be placed on the EU market, made available there or exported from it. Unlike the US UFLPA border presumption, it works through a risk database, investigations by national authorities and bans on specific products, which companies must implement within the period set in the decision — generally 30 working days — with penalties set by member states and no size threshold. The article sets out the prohibitions and the mechanism, then a table separating its role from UFLPA, the CSDDD and BSCI social audits. It explains why trims suppliers get asked: the order is assessed as a garment, spinning weaving dyeing printing and plating may be outsourced, temporary and agency labour is common, and pulp or cotton yarn origin is part of the review. It lists the supply chain map, origin declarations, working hour records and audit certificates customers request with the gaps each usually has, before six practical steps for 2027: one map per product, registering agency labour, reconciling attendance payroll and hours, collecting upstream origin declarations, keeping audits valid and covering the real site, and filing shipment documents by batch under one numbering system shared with your UFLPA file.",
        sum_ja="EU の強制労働製品規則（2024/3015）は 2024 年 12 月 13 日に発効し、製品の禁止は 2027 年 12 月 14 日から適用されます。全部または一部が強制労働で製造された製品は、EU 市場への投入・提供・輸出ができません。米国 UFLPA の国境推定とは異なり、「リスクデータベース＋主管機関の調査＋特定製品への禁止」という経路をとり、企業は決定で定められた期間（通常 30 営業日）内に対応する必要があります。制裁は加盟国が定め、企業規模による区別はありません。本記事は禁止範囲と仕組みを整理し、UFLPA・CSDDD・BSCI 社会監査との役割分担を表で示します。続いて副資材サプライヤーが問われる理由（製品単位の評価、紡糸・製織・染色・印刷・めっきなど外注工程、臨時・派遣労働、パルプや綿糸の産地）を説明し、顧客が求めるサプライチェーンマップ、原産地宣言、労務・労働時間記録、監査証明とそれぞれのよくある不足を整理。最後に 2027 年までに実行できる 6 項目（製品別マップ作成、派遣労働の登録、勤怠・賃金・労働時間の整合、上流への原産地宣言依頼、監査の有効性維持と実工場のカバー、批次別の出荷書類保管と UFLPA 台帳との採番共通化）を示します。",
        sum_ko="EU 강제노동 제품 규정(2024/3015)은 2024년 12월 13일 발효되었고 제품 금지는 2027년 12월 14일부터 적용됩니다. 전부 또는 일부가 강제노동으로 만들어진 제품은 EU 시장 출시·제공·수출이 금지됩니다. 미국 UFLPA의 국경 추정과 달리 '리스크 데이터베이스 + 당국 조사 + 특정 제품 금지' 경로를 따르며, 기업은 결정에서 정한 기간(보통 30영업일) 내에 이행해야 합니다. 제재는 회원국이 정하고 기업 규모 구분은 없습니다. 이 글은 금지 범위와 구조를 정리하고 UFLPA, CSDDD, BSCI 사회 감사와의 역할 분담을 표로 제시합니다. 이어 부자재 공급업체가 요구받는 이유(제품 단위 평가, 방적·직조·염색·인쇄·도금 등 외주 공정, 임시·파견 근로, 펄프와 면사 산지)를 설명하고, 고객이 요구하는 공급망 맵, 원산지 선언, 노무·근로시간 기록, 감사 인증서와 각각의 흔한 결함을 정리합니다. 마지막으로 2027년 전에 실행할 여섯 항목(제품별 맵 작성, 파견 근로 등록, 근태·급여·근로시간 정합, 상류 원산지 선언 확보, 감사 유효성 유지와 실제 사업장 포함, 배치별 출하 서류 보관과 UFLPA 대장 번호 체계 공유)을 제시합니다.",
        sum_fr="Le règlement européen sur le travail forcé (2024/3015) est entré en vigueur le 13 décembre 2024 et son interdiction s'applique à partir du 14 décembre 2027 : un produit fabriqué en tout ou partie par du travail forcé ne peut être mis sur le marché de l'UE, y être proposé ni exporté. Contrairement à la présomption frontalière de l'UFLPA, il repose sur une base de risques, des enquêtes d'autorités nationales et des interdictions visant des produits précis, à exécuter dans le délai fixé — en principe 30 jours ouvrables — avec des sanctions fixées par les États membres et sans distinction de taille. L'article expose les interdictions et le mécanisme, puis un tableau sépare son rôle de celui de l'UFLPA, de la CSDDD et des audits sociaux BSCI. Il explique pourquoi les fournisseurs d'accessoires sont interrogés : évaluation par produit fini, filature tissage teinture impression et galvanoplastie externalisés, intérim fréquent, origine de la pâte et du fil de coton. Il recense la cartographie, les déclarations d'origine, les registres de temps de travail et les certificats d'audit demandés avec leurs lacunes habituelles, avant six actions pour 2027 : une cartographie par produit, l'enregistrement de l'intérim, la concordance pointage paie heures, la collecte des déclarations amont, le maintien d'audits valides couvrant le site réel, et l'archivage par lot sous une numérotation partagée avec le dossier UFLPA.",
        sum_es="El Reglamento europeo sobre el trabajo forzoso (2024/3015) entró en vigor el 13 de diciembre de 2024 y su prohibición se aplica desde el 14 de diciembre de 2027: los productos fabricados total o parcialmente con trabajo forzoso no pueden introducirse, ofrecerse ni exportarse desde el mercado de la UE. A diferencia de la presunción fronteriza de la UFLPA, funciona con una base de riesgos, investigaciones de autoridades nacionales y prohibiciones de productos concretos, que deben ejecutarse en el plazo fijado —en principio 30 días hábiles— con sanciones definidas por los Estados miembros y sin distinción de tamaño. El artículo expone las prohibiciones y el mecanismo y una tabla separa su papel del de la UFLPA, la CSDDD y las auditorías sociales BSCI. Explica por qué preguntan a los proveedores de accesorios: evaluación como prenda, hilatura tejido tintura impresión y galvanizado subcontratados, empleo temporal y de ETT, y origen de pasta e hilo de algodón. Recoge el mapa de cadena, declaraciones de origen, registros de horario y certificados de auditoría que piden los clientes con sus carencias habituales, y seis acciones para 2027: un mapa por producto, registrar el empleo de ETT, cuadrar control nómina y horas, recabar declaraciones de origen, mantener auditorías vigentes que cubran la planta real y archivar por lote con una numeración compartida con el archivo UFLPA.",
    ),
]
