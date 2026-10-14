#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-14 第一批（08:00 时段）每日更新：2 篇新文章元数据（六语：zh-Hant 根 / en / ja / ko / fr / es）

选题说明（主题池 30 项连同既有扩展均已上线；本次沿全站六语关键词扫描确认的两条空白线索扩展，
已核对 blog/、en|ja|ko|fr|es/blog/ 与 sitemap.xml 无重复 slug）：

- apron-trims-label-guide.html：围裙与餐饮/食品服务工作服辅料标签指南。
  全站扫描：「围裙」0 处、「apron」0 处、「エプロン」0 处、「앞치마」0 处、「厨师服」0 处。
  既有 uniform-workwear-labeling-guide 讲工装标签的工业洗涤与标识，
  hat-scarf-gloves 覆盖帽围手套，唯独「围裙/餐饮工作服」这一品类从未成文。
  本文落点是「一条围裙的六类辅料构成表 → 餐饮场景四条硬约束（洗涤强度、防泼水对上墨的影响、
  食品接触与卫生、标识磨损）→ 织唛/丝印/热转印/绣花的选择与位置 → 尺码与多门店信息 →
  包装出口与抽查验收」，不涉及价格数字。

- clothing-label-compliance-netherlands.html：荷兰服装标签与包装合规指南。
  全站扫描：「Netherlands」0 处、「荷蘭」0 处、「Dutch」0 处、「Nederland」0 处；
  既有 20 国合规篇与国家无关的 EU/UK/瑞士篇（EU 篇讲 FTC 洗水标 + EU 1007/2011 通用口径），
  荷兰的本地义务（荷兰语标识、纺织品 EPR 与包装 EPR）从未出现。
  事实来源（2026-10-14 联网核对）：荷兰纺织品生产者责任 UPV Textiel 自 2023-07-01 生效，
  覆盖首次投放荷兰市场的服装/工装/家用纺织品，含远程销售的境外卖家（须指定荷兰授权代表），
  登记走 Rijkswaterstaat 体系，每年 8 月 1 日前申报上一日历年投放量与履约结果，
  主要生产者责任组织为 Stichting UPV Textiel，管理费按公斤计、逐年公布（2025 年公布量级为每公斤十几欧分）。
  文中费用与时间表一律写成「以主管机构与生产者责任组织当年公告为准」，不写死数字。
"""

ARTICLES = [
    dict(
        slug="apron-trims-label-guide.html",
        body="blog/_body_apron.html",
        title_zh="围裙与餐饮工作服辅料指南：带身、标识与包装怎么配 | TAGE",
        title_en="Apron and Food-Service Workwear Trims Guide: Straps, Marking and Packaging | TAGE",
        title_ja="エプロン・飲食ユニフォーム副資材ガイド：ひも・表示・包装の決め方 | TAGE",
        title_ko="앞치마·요식업 유니폼 부자재 가이드: 끈, 표시, 포장 정하기 | TAGE",
        title_fr="Guide des accessoires pour tabliers et tenues de restauration : sangles, marquage et emballage | TAGE",
        title_es="Guía de accesorios para delantales y ropa de hostelería: cintas, marcado y embalaje | TAGE",
        desc_zh="围裙与餐饮工作服辅料指南：颈带腰带怎么选、扣件能否扛住高温工业洗涤、品牌标与洗水标缝在哪里、尺码与多门店信息怎么标、包装与抽查验收要点，附六类辅料对照表。来自东莞泰阁包装。",
        desc_en="Apron and food-service workwear trims guide: neck and waist straps, adjusters, wash-resistant marking, care label placement, practical sizing and inspection.",
        desc_ja="エプロン・飲食ユニフォームの副資材ガイド。首ひもと腰ひもの選び方、調整金具の耐洗性、ブランドラベルと洗濯表示の位置、サイズと多店舗情報の表示、包装と抜き取り検収の要点を6種類の副資材対照表とともに解説します。東莞泰閣包装。",
        desc_ko="앞치마·요식업 유니폼 부자재 가이드. 목끈과 허리끈 선택, 조절 부품의 내세탁성, 브랜드 라벨과 세탁 라벨 위치, 사이즈와 다지점 정보 표시, 포장과 샘플링 검수 요점을 여섯 가지 부자재 대조표와 함께 정리했습니다. 둥관 TAGE 패키징.",
        desc_fr="Guide des accessoires pour tabliers et tenues de restauration : sangles de cou et de taille, boucles, marquage résistant au lavage, tailles et emballage.",
        desc_es="Guía de accesorios para delantales y ropa de hostelería: cintas de cuello y cintura, reguladores, marcado resistente al lavado, tallas y embalaje.",
        crumb_zh="围裙与餐饮工作服辅料",
        crumb_en="Apron and Food-Service Trims",
        crumb_ja="エプロン・飲食ユニフォームの副資材",
        crumb_ko="앞치마·요식업 부자재",
        crumb_fr="Accessoires pour tabliers et restauration",
        crumb_es="Accesorios para delantales y hostelería",
        h1_zh="围裙与餐饮工作服辅料指南：带身、标识与包装怎么配",
        h1_en="Apron and Food-Service Workwear Trims: Straps, Marking and Packing",
        h1_ja="エプロンと飲食ユニフォームの副資材ガイド：ひも・表示・包装の決め方",
        h1_ko="앞치마·요식업 유니폼 부자재 가이드: 끈, 표시, 포장 정하기",
        h1_fr="Guide des accessoires pour tabliers et tenues de restauration : sangles, marquage et emballage",
        h1_es="Guía de accesorios para delantales y ropa de hostelería: cintas, marcado y embalaje",
        tag_zh="品类指南",
        tag_en="Category Guide",
        tag_ja="カテゴリガイド",
        tag_ko="카테고리 가이드",
        tag_fr="Guide par catégorie",
        tag_es="Guía por categoría",
        sum_zh="围裙是带身、扣件、标识与包装的组合件：颈带腰带怎么选、扣件能否扛住高温洗涤、品牌标与洗水标缝在哪里、尺码与多门店信息怎么标，一次讲清。",
        sum_en="An apron is a set of straps, adjusters, marking and packing: choosing straps, surviving hot washing, label placement, sizing and multi-site information.",
        sum_ja="エプロンはひも・金具・表示・包装の組み合わせです。ひもの選び方、高温洗濯への耐性、ラベルの位置、サイズと多店舗情報の表示を整理します。",
        sum_ko="앞치마는 끈, 부품, 표시, 포장의 조합입니다. 끈 선택, 고온 세탁 내성, 라벨 위치, 사이즈와 다지점 정보 표시를 정리했습니다.",
        sum_fr="Un tablier, c'est un ensemble de sangles, boucles, marquage et emballage : choix des sangles, tenue au lavage chaud, position des étiquettes, tailles et multi-sites.",
        sum_es="Un delantal es un conjunto de cintas, reguladores, marcado y embalaje: elección de cintas, resistencia al lavado caliente, posición de etiquetas, tallas y varias tiendas.",
    ),
    dict(
        slug="clothing-label-compliance-netherlands.html",
        body="blog/_body_nlcomp.html",
        title_zh="荷兰服装标签与包装合规指南：荷兰语标识与纺织品 EPR | TAGE",
        title_en="Netherlands Apparel Labelling and Packaging Compliance: Dutch Marking and Textile EPR | TAGE",
        title_ja="オランダの衣料ラベル・包装コンプライアンス：オランダ語表示と繊維 EPR | TAGE",
        title_ko="네덜란드 의류 라벨·포장 컴플라이언스: 네덜란드어 표시와 섬유 EPR | TAGE",
        title_fr="Conformité étiquetage et emballage aux Pays-Bas : marquage néerlandais et REP textile | TAGE",
        title_es="Cumplimiento de etiquetado y embalaje en Países Bajos: marcado neerlandés y REP textil | TAGE",
        desc_zh="荷兰服装标签与包装合规指南：纤维成分为何必须用荷兰语标注、纺织品生产者责任 UPV Textiel 谁有义务怎么申报、包装生产者责任与包装标识、辅料采购的五步落地清单。来自东莞泰阁包装。",
        desc_en="Netherlands apparel labelling and packaging compliance guide: why fibre composition must be in Dutch, who reports under textile EPR, and the packaging duties.",
        desc_ja="オランダの衣料ラベルと包装のコンプライアンスガイド。繊維組成をオランダ語で示す必要がある理由、繊維 EPR（UPV Textiel）の義務者と報告方法、包装の生産者責任と表示、副資材調達の5ステップを解説します。東莞泰閣包装。",
        desc_ko="네덜란드 의류 라벨과 포장 컴플라이언스 가이드. 섬유 조성을 네덜란드어로 표시해야 하는 이유, 섬유 EPR(UPV Textiel)의 의무자와 보고 방법, 포장 생산자책임과 표시, 부자재 구매 5단계를 정리했습니다. 둥관 TAGE 패키징.",
        desc_fr="Conformité étiquetage et emballage aux Pays-Bas : composition fibreuse en néerlandais, REP textile (UPV Textiel), obligations emballage et checklist.",
        desc_es="Cumplimiento de etiquetado y embalaje en Países Bajos: composición de fibras en neerlandés, REP textil (UPV Textiel), obligaciones de envase y lista de pasos.",
        crumb_zh="荷兰标签与包装合规",
        crumb_en="Netherlands Labelling and Packaging",
        crumb_ja="オランダのラベルと包装の適合",
        crumb_ko="네덜란드 라벨·포장 규정",
        crumb_fr="Étiquetage et emballage aux Pays-Bas",
        crumb_es="Etiquetado y embalaje en Países Bajos",
        h1_zh="荷兰服装标签与包装合规指南：荷兰语标识、纺织品 EPR 与包装申报",
        h1_en="Netherlands Apparel Labelling and Packaging Compliance: Dutch Marking, Textile EPR and Reporting",
        h1_ja="オランダの衣料ラベル・包装コンプライアンス：オランダ語表示・繊維 EPR・報告",
        h1_ko="네덜란드 의류 라벨·포장 컴플라이언스: 네덜란드어 표시, 섬유 EPR, 신고",
        h1_fr="Conformité étiquetage et emballage aux Pays-Bas : marquage néerlandais, REP textile et déclarations",
        h1_es="Cumplimiento de etiquetado y embalaje en Países Bajos: marcado neerlandés, REP textil y declaraciones",
        tag_zh="合规指南",
        tag_en="Compliance Guide",
        tag_ja="コンプライアンスガイド",
        tag_ko="컴플라이언스 가이드",
        tag_fr="Guide de conformité",
        tag_es="Guía de cumplimiento",
        sum_zh="荷兰市场的两套本地义务最容易被漏掉：纤维成分必须用荷兰语，纺织品生产者责任 UPV Textiel 需登记并按年申报，境外卖家还要指定荷兰授权代表。",
        sum_en="Two Dutch duties get missed most: fibre composition in Dutch, and textile EPR (UPV Textiel) registration plus annual reporting — foreign sellers also need a Dutch representative.",
        sum_ja="オランダで見落とされやすい二つの義務：繊維組成のオランダ語表示と、繊維 EPR（UPV Textiel）の登録・年次報告です。海外セラーはオランダの代表者指定も必要です。",
        sum_ko="네덜란드에서 가장 자주 빠지는 두 가지 의무: 섬유 조성의 네덜란드어 표시와 섬유 EPR(UPV Textiel) 등록·연차 보고입니다. 해외 셀러는 네덜란드 대리인 지정도 필요합니다.",
        sum_fr="Deux obligations néerlandaises souvent oubliées : composition fibreuse en néerlandais, et REP textile (UPV Textiel) avec enregistrement et déclaration annuelle — représentant requis pour les vendeurs étrangers.",
        sum_es="Dos obligaciones neerlandesas que más se omiten: composición de fibras en neerlandés y REP textil (UPV Textiel) con registro y declaración anual; los vendedores extranjeros necesitan representante.",
    ),
]
