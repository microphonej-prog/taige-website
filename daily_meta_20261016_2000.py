#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-16 本日第三批（20:00）每日更新：2 篇新文章元数据（六语：zh-Hant 根 / en / ja / ko / fr / es）

选题说明（原 30 项主题池连同既有扩展均已上线，本次为全站六语关键词扫描后的空白点扩展）：

- trim-shipment-insurance-claims-guide.html：辅料运输保险与货损索赔。
  关键词扫描：「货物保险 / cargo insurance / 一切险 / 货损索赔 / survey report」全站零命中；
  「货损=6、理赔=4」仅出现在出货方式页与合同条款页的顺带一句。
  既有文章的分工：出货方式页讲怎么选渠道与 Incoterms，付款条款页讲谁付钱与风险边界，
  外箱装柜页讲怎么装，合同条款页讲索赔期限怎么写——没有一篇讲「保单怎么买、货损当天怎么取证、
  索赔单据与拒赔原因」。本篇落点：贸易术语与投保责任对照表 → 辅料为什么最容易投保不足 →
  基本险与附加险怎么选 → 单证与背书转让 → 货损当天六步动作顺序 → 索赔单据、时限与五个常见拒赔原因。

- conflict-minerals-trims-guide.html：冲突矿产（3TG）与金属辅料尽责调查。
  关键词扫描：「冲突矿产 / conflict mineral / 3TG / CMRT / 冶炼厂 / smelter / OECD」全站零命中；
  既有 20 余篇合规文章覆盖 REACH、SVHC、PFAS、UFLPA、EUDR、EPR、PPWR、GPSR、DPP、碳足迹，
  唯独缺「品牌年度表格要你回答锡钽钨金来自哪里」这一条供应链尽责调查路径。
  本篇落点：表格是谁下推来的 → 3TG 与辅料部位对照表（电镀锡、钨钢模具、智能芯片、
  烫金箔通常不含）→ 三类答案与举证层级 → 拿不到上游数据的四条路径 → 文件与追溯 → 五个误区与准备清单。

事实口径（不编造）：不写具体价格、不写法定罚则与具体年限数字；
保险险别与时限一律写「以保单条款为准」，海运书面异议期限写「通常在卸货后数日内」；
冲突矿产法规只写「欧盟冲突矿产条例要求欧盟进口商对锡、钽、钨、金做尽责调查」，
美国规则写「几经调整，如今更多由品牌自愿承诺与投资人要求推动」，不写具体条文号与日期。
"""

ARTICLES = [
    dict(
        slug="trim-shipment-insurance-claims-guide.html",
        body="blog/_body_transins.html",
        title_zh="服装辅料运输保险与货损索赔指南：险别、保额与单据 | TAGE",
        title_en="Trim Shipment Insurance and Cargo Damage Claims: Cover, Value, Documents | TAGE",
        title_ja="副資材の貨物保険と損害賠償請求ガイド：保険種類・保険金額・書類 | TAGE",
        title_ko="부자재 적하보험과 화물 손상 청구 가이드: 담보, 보험금액, 서류 | TAGE",
        title_fr="Assurance transport et réclamation de dommages : garanties et documents | TAGE",
        title_es="Seguro de transporte y reclamación por daños: cobertura y documentos | TAGE",
        desc_zh="服装辅料出运的运输保险怎么投？各贸易术语下谁投保、投保金额按发票金额还是按重量、基本险与附加险怎么选、保单背书转让、货损当天的取证顺序、索赔单据与时限，以及五个最常见的拒赔原因。来自东莞泰阁包装。",
        desc_en="Cargo insurance for trim shipments: who insures under each trade term, insured value, cover levels, policy endorsement, damage evidence and claim refusals.",
        desc_ja="副資材の貨物保険と損害賠償請求の要点。貿易条件ごとの保険手配、保険金額の基準、基本危険と追加危険の選び方、証券の裏書譲渡、損害当日の証拠固め、請求書類と期限、よくある支払拒否の理由まで整理します。東莞泰閣包装。",
        desc_ko="부자재 적하보험과 화물 손상 청구의 요점. 무역 조건별 보험 가입 주체, 보험 금액 기준, 기본 담보와 특별 담보 선택, 증권 배서 양도, 손상 당일 증거 확보, 청구 서류와 기한, 흔한 거절 사유까지 정리했습니다. 둥관 TAGE 패키징.",
        desc_fr="Assurance transport des accessoires : qui assure selon l'Incoterm, valeur assurée, garanties de base et additionnelles, endossement, preuves en cas de dommage et motifs de refus.",
        desc_es="Seguro de transporte de accesorios: quién asegura según el Incoterm, valor asegurado, coberturas, endoso, pruebas tras el daño y motivos de rechazo.",
        crumb_zh="运输保险与货损索赔",
        crumb_en="Shipment Insurance and Claims",
        crumb_ja="貨物保険と損害請求",
        crumb_ko="적하보험과 손상 청구",
        crumb_fr="Assurance et réclamations",
        crumb_es="Seguro y reclamaciones",
        h1_zh="服装辅料运输保险与货损索赔指南：险别、保额与单据",
        h1_en="Trim Shipment Insurance and Cargo Damage Claims: Cover, Value and Documents",
        h1_ja="副資材の貨物保険と損害賠償請求ガイド：保険種類・保険金額・書類",
        h1_ko="부자재 적하보험과 화물 손상 청구 가이드: 담보, 보험금액, 서류",
        h1_fr="Assurance transport et réclamation de dommages pour accessoires",
        h1_es="Seguro de transporte y reclamación por daños en accesorios",
        tag_zh="物流与单证",
        tag_en="Logistics & Documents",
        tag_ja="物流と書類",
        tag_ko="물류와 서류",
        tag_fr="Logistique et documents",
        tag_es="Logística y documentos",
        sum_zh="贸易术语与投保责任对照表、辅料投保不足的五个原因、基本险与附加险的取舍、保单背书转让、货损当天的六步取证顺序，以及索赔单据、时限与五个常见拒赔原因。",
        sum_en="A trade-term table showing who insures, five reasons trims end up under-insured, how to choose cover, policy endorsement, six steps to secure evidence on the day of damage, claim documents, deadlines and five refusals.",
        sum_ja="貿易条件ごとの保険手配の対照表、副資材が過少保険になりやすい5つの理由、基本危険と追加危険の使い分け、証券の裏書譲渡、損害当日の6段階の証拠固め、請求書類と期限、よくある支払拒否5例。",
        sum_ko="무역 조건별 보험 가입 주체 대조표, 부자재가 부보 부족이 되는 다섯 가지 이유, 기본·특별 담보 선택, 증권 배서 양도, 손상 당일 여섯 단계 증거 확보, 청구 서류와 기한, 흔한 거절 사유 다섯 가지.",
        sum_fr="Tableau des Incoterms et de l'obligation d'assurance, cinq raisons de sous-assurance, choix des garanties, endossement, six étapes de preuve le jour du dommage, pièces et délais, cinq refus fréquents.",
        sum_es="Tabla de Incoterms y obligación de asegurar, cinco motivos de infraseguro, elección de coberturas, endoso, seis pasos de prueba el día del daño, piezas y plazos, cinco rechazos frecuentes.",
    ),
    dict(
        slug="conflict-minerals-trims-guide.html",
        body="blog/_body_minerals.html",
        title_zh="冲突矿产与金属辅料尽责调查指南：3TG、CMRT 与举证 | TAGE",
        title_en="Conflict Minerals Due Diligence for Metal Trims: 3TG, CMRT and Evidence | TAGE",
        title_ja="紛争鉱物と金属副資材のデューデリジェンス：3TG・CMRT・証拠 | TAGE",
        title_ko="분쟁 광물과 금속 부자재 실사: 3TG, CMRT, 증빙 | TAGE",
        title_fr="Minerais de conflit et accessoires métalliques : 3TG, CMRT et preuves | TAGE",
        title_es="Minerales de conflicto y accesorios metálicos: 3TG, CMRT y pruebas | TAGE",
        desc_zh="客户发来的冲突矿产表格怎么填？3TG 与辅料部件的对照（电镀锡、钨钢模具、智能芯片、烫金箔）、三类答案与举证层级、拿不到上游数据的四条路径、文件与追溯要求，以及五个常见误区。来自东莞泰阁包装。",
        desc_en="Conflict minerals due diligence for trim suppliers: which parts touch 3TG, how to complete a CMRT, evidence levels, upstream data routes and common mistakes.",
        desc_ja="副資材サプライヤーの紛争鉱物デューデリジェンス。3TG と部位の対照、CMRT の記入方法、証拠の階層、上流データが取れない場合の4つの道筋、書類とトレーサビリティ、よくある誤りまで整理します。東莞泰閣包装。",
        desc_ko="부자재 공급사의 분쟁 광물 실사. 3TG와 부위 대조, CMRT 기재 방법, 증거 단계, 상류 데이터가 없을 때의 네 가지 경로, 서류와 추적성, 흔한 오류까지 정리했습니다. 둥관 TAGE 패키징.",
        desc_fr="Diligence raisonnable minerais de conflit pour les accessoires : quelles pièces touchent les 3TG, comment remplir un CMRT, niveaux de preuve et erreurs courantes.",
        desc_es="Diligencia debida de minerales de conflicto para accesorios: qué piezas tocan los 3TG, cómo cumplimentar un CMRT, niveles de prueba y errores habituales.",
        crumb_zh="冲突矿产与尽责调查",
        crumb_en="Conflict Minerals Due Diligence",
        crumb_ja="紛争鉱物デューデリジェンス",
        crumb_ko="분쟁 광물 실사",
        crumb_fr="Minerais de conflit",
        crumb_es="Minerales de conflicto",
        h1_zh="冲突矿产与金属辅料尽责调查指南：3TG、CMRT 与举证",
        h1_en="Conflict Minerals Due Diligence for Metal Trims: 3TG, CMRT and Evidence",
        h1_ja="紛争鉱物と金属副資材のデューデリジェンス：3TG・CMRT・証拠",
        h1_ko="분쟁 광물과 금속 부자재 실사: 3TG, CMRT, 증빙",
        h1_fr="Minerais de conflit et accessoires métalliques : 3TG, CMRT et preuves",
        h1_es="Minerales de conflicto y accesorios metálicos: 3TG, CMRT y pruebas",
        tag_zh="合规与认证",
        tag_en="Compliance",
        tag_ja="コンプライアンス",
        tag_ko="컴플라이언스",
        tag_fr="Conformité",
        tag_es="Cumplimiento",
        sum_zh="表格顺着供应链下推的路径、3TG 与辅料部件对照表（电镀锡、钨钢模具、智能芯片、烫金箔通常不含）、三类答案与举证层级、四务实的补数据路径、文件追溯与五个常见误区。",
        sum_en="How the form travels down the chain, a 3TG-to-component table covering plating, tungsten tooling, smart chips and foil, three answer types with evidence levels, four routes to obtain data, and five common mistakes.",
        sum_ja="表がサプライチェーンを下る経路、3TG と部位の対照表（めっき錫・超硬工具・スマートチップ・箔）、3つの回答と証拠の階層、データ入手の4つの道筋、書類管理と5つの誤り。",
        sum_ko="표가 공급망을 따라 내려오는 경로, 3TG와 부위 대조표(도금 주석, 초경 공구, 스마트 칩, 박), 세 가지 답변과 증거 단계, 데이터 확보 네 가지 경로, 서류 관리와 다섯 가지 오류.",
        sum_fr="Le parcours du formulaire, un tableau 3TG par composant (revêtement, outillage carbure, puce, dorure), trois types de réponse avec niveaux de preuve, quatre voies de collecte et cinq erreurs.",
        sum_es="El recorrido de la hoja, tabla de 3TG por componente (recubrimiento, utillaje de carburo, chip, foil), tres tipos de respuesta con niveles de prueba, cuatro vías de recogida y cinco errores.",
    ),
]
