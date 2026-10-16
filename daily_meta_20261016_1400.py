#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-16 第二批（14:00 时段）每日更新：2 篇新文章元数据（六语：zh-Hant 根 / en / ja / ko / fr / es）

选题说明（主题池 30 项连同既有扩展均已上线，本次为全站六语关键词扫描后的空白品类扩展）：

- adaptive-accessible-clothing-trims-guide.html：适老与无障碍服装（adaptive / accessible clothing）辅料指南。
  全站扫描确认这是真空白：「适老」「适老服装」「银发」「中老年」「照护者」「护理院」「养老」「术后」
  「病人服」「医护」「医院」「手术」「磁吸扣」「磁铁扣」「易穿脱」「拉链拉手」「拉环」「弹性腰头」
  在 272 篇文章里出现 0 次；「无障碍」仅 2 篇（盲文标签页）附带提及，
  纽扣与扣件页、魔术贴页、刺痒页讲的都是常规成衣场景，没有一篇处理「手部不灵活 / 照护者协助穿脱」
  这条使用路径。
  本篇落点：三类使用场景（自理但手不灵活 / 照护者协助 / 术后临时失能）→ 五种闭合方式对照表
  （磁吸扣、粘扣、按扣、拉链＋加长拉环、系带）与假门襟折中方案 → 标签可读性四项
  （字号行距、对比度、双通道表达、盲文与触觉）→ 接触舒适（无感标签、缝制位置、包装开法）→
  洗护与耐久（耐洗与外观、金属件磁力衰减、柔软剂与漂白误区）→ 打样验收三项硬指标与变更管理。

- modest-wear-hijab-trims-guide.html：头巾与长袍（modest wear）辅料指南。
  全站扫描：「头巾」「长袍」「礼袍」「罩袍」「穆斯林」「hijab」「阿巴亚」「斋月」「朝觐」「开斋节」
  「宰牲节」「Eid」「赠礼」出现 0 次；「阿拉伯语」仅在沙特 / 阿联酋 / 土耳其等合规页出现（讲的是
  法定标识要求），没有一篇讲这类产品本身的辅料做法。
  本篇落点：三类特殊要求（轻薄面料钩丝与拉扯、半透面料透色、贴身体感）→ 主唛与洗水标的位置 / 材质 / 缝制
  三件事一起定 → 阿拉伯语双语标签的排版与信息顺序 → 头巾与内衬帽专属细节（尺码标、松紧与包边、
  长袍暗扣与流苏）→ 市场合规与斋月旺季备货 → 礼赠包装与透色勾挂防护。

事实口径：涉及法规一律写「以客户与目标市场现行规定为准」并指向站内合规页，不写死条款号与罚则；
涉及洗护一律写方法名与等级体系（ISO 6330 洗涤程序、ISO 105-C06 耐洗、灰卡评级），不写死次数与费用数字；
磁吸扣与心脏起搏器的禁忌写「需谨慎 / 部分机构有内部限制」，不写成绝对禁令。
"""

ARTICLES = [
    dict(
        slug="adaptive-accessible-clothing-trims-guide.html",
        body="blog/_body_adaptive.html",
        title_zh="适老与无障碍服装辅料指南：磁吸扣、易穿脱结构与可读标签 | TAGE",
        title_en="Adaptive &amp; Accessible Clothing Trims Guide: Magnetic Closures and Readable Labels | TAGE",
        title_ja="アダプティブ衣料の副資材ガイド：磁気スナップ・着脱しやすい構造・読みやすいラベル | TAGE",
        title_ko="적응형·무장애 의류 부자재 가이드: 자석 스냅, 손쉬운 착탈 구조, 읽기 쉬운 라벨 | TAGE",
        title_fr="Accessoires pour vêtements adaptés : aimants, fermetures faciles et étiquettes lisibles | TAGE",
        title_es="Accesorios para ropa adaptada: imanes, cierres fáciles y etiquetas legibles | TAGE",
        desc_zh="适老与无障碍服装辅料怎么选？磁吸扣与粘扣替代纽扣、前开侧开与加长拉环、高对比大字号的洗水标与吊牌、无感标签与盲文标识，以及照护场景的耐高温洗护要求、三项真人验收指标与留样变更要点。来自东莞泰阁包装。",
        desc_en="Adaptive clothing trims guide: magnetic snaps versus hook-and-loop, one-handed closures, large-print care labels, tagless comfort and wash durability testing.",
        desc_ja="アダプティブ衣料の副資材ガイド。磁気スナップと面ファスナーの使い分け、片手で使える開閉、高コントラストで大きな文字の洗濯表示ラベル、タグレス仕様と耐洗濯性の検証、介護現場の高温洗濯への対応、サンプル検収の必須基準まで整理します。東莞泰閣包装。",
        desc_ko="적응형·무장애 의류 부자재 가이드. 자석 스냅과 벨크로 선택, 한 손으로 쓰는 여밈, 고대비 큰 글자 세탁 표시 라벨, 무감 라벨과 세탁 내구성 검증, 요양 현장의 고온 세탁 대응, 샘플 검수 필수 기준을 정리했습니다. 둥관 TAGE 패키징.",
        desc_fr="Guide des accessoires pour vêtements adaptés : aimants ou velcro, fermetures d'une seule main, étiquettes lisibles à fort contraste, confort sans couture et tenue au lavage.",
        desc_es="Guía de accesorios para ropa adaptada: imanes o velcro, cierres con una sola mano, etiquetas legibles de alto contraste, confort sin costura y resistencia al lavado.",
        crumb_zh="适老与无障碍辅料",
        crumb_en="Adaptive Clothing Trims",
        crumb_ja="アダプティブ衣料の副資材",
        crumb_ko="적응형 의류 부자재",
        crumb_fr="Accessoires adaptés",
        crumb_es="Accesorios adaptados",
        h1_zh="适老与无障碍服装辅料指南：磁吸扣、易穿脱结构与可读标签",
        h1_en="Adaptive and Accessible Clothing Trims Guide",
        h1_ja="アダプティブ衣料の副資材ガイド",
        h1_ko="적응형·무장애 의류 부자재 가이드",
        h1_fr="Guide des accessoires pour vêtements adaptés",
        h1_es="Guía de accesorios para ropa adaptada",
        tag_zh="品类指南",
        tag_en="Category Guide",
        tag_ja="カテゴリガイド",
        tag_ko="카테고리 가이드",
        tag_fr="Guide par catégorie",
        tag_es="Guía por categoría",
        sum_zh="三类使用场景对应的辅料取舍、五种闭合方式对照（含假门襟折中）、标签可读性四项、无感标签与缝制位置、洗护耐久与磁力衰减，以及打样验收的三项硬指标。",
        sum_en="Trims by user scenario, five closure options including the false placket, four rules for readable labels, tagless comfort and placement, wash durability and magnet decay, plus three hard acceptance criteria.",
        sum_ja="3つの使用場面ごとの副資材の考え方、5種の開閉方式（飾り前立てを含む）、読みやすいラベルの4条件、タグレスと縫い付け位置、耐洗濯性と磁力低下、サンプル検収の必須3基準。",
        sum_ko="세 가지 사용 상황별 부자재 선택, 다섯 가지 여밈 방식(가짜 앞여밈 포함), 읽기 쉬운 라벨 네 가지 조건, 무감 라벨과 봉제 위치, 세탁 내구성과 자력 저하, 샘플 검수 세 가지 필수 기준.",
        sum_fr="Accessoires selon trois contextes d'usage, cinq fermetures dont la fausse patte, quatre règles de lisibilité, confort sans couture, tenue au lavage et perte d'aimantation, et trois critères de réception.",
        sum_es="Accesorios según tres escenarios de uso, cinco cierres incluida la falsa tapeta, cuatro reglas de legibilidad, confort sin costura, resistencia al lavado y pérdida de magnetismo, y tres criterios de recepción.",
    ),
    dict(
        slug="modest-wear-hijab-trims-guide.html",
        body="blog/_body_modest.html",
        title_zh="头巾与长袍（Hijab &amp; Abaya）辅料指南：主唛、洗水标与包装怎么选 | TAGE",
        title_en="Modest Wear Trims Guide: Hijab, Abaya, Neck Labels, Care Labels and Packaging | TAGE",
        title_ja="ヒジャブ・アバヤ（モデストウェア）の副資材ガイド：メインラベル・洗濯表示ラベル・包装 | TAGE",
        title_ko="히잡·아바야(모데스트 웨어) 부자재 가이드: 메인 라벨, 세탁 표시 라벨, 포장 | TAGE",
        title_fr="Accessoires modest wear : hijab, abaya, labels et emballages | TAGE",
        title_es="Accesorios para modest wear: hiyab, abaya, etiquetas y embalaje | TAGE",
        desc_zh="头巾与长袍（modest wear）辅料指南：轻薄垂坠面料上主唛与洗水标怎么缝才不透色不钩丝、阿拉伯语双语标签的排版与信息顺序、内衬帽松紧与包边细节、市场合规与斋月旺季备货，以及礼赠包装要点。来自东莞泰阁包装。",
        desc_en="Modest wear trims guide: labelling hijabs and abayas without show-through or snagging, Arabic bilingual care labels, undercap elastics and peak-season planning.",
        desc_ja="ヒジャブ・アバヤなどモデストウェアの副資材ガイド。薄手ドレープ生地で透けや引っかけを出さない縫い付け、アラビア語併記ラベルの組みと情報順、アンダーキャップのゴムとパイピング、市場適合と繁忙期の計画、ギフト包装まで整理します。東莞泰閣包装。",
        desc_ko="히잡·아바야 등 모데스트 웨어 부자재 가이드. 얇고 흐르는 원단에서 비침과 올 나감 없이 봉제하는 방법, 아랍어 병기 라벨의 조판과 정보 순서, 언더캡 밴드와 바인딩, 시장 적합성과 성수기 계획, 선물 포장을 정리했습니다. 둥관 TAGE 패키징.",
        desc_fr="Guide des accessoires pour hijab et abaya : coudre sans transparence ni accroc, étiquettes bilingues en arabe, élastiques de sous-bonnet, conformité et saisonnalité.",
        desc_es="Guía de accesorios para hiyab y abaya: coser sin transparencia ni enganches, etiquetas bilingües en árabe, elásticos de gorro interior, conformidad y temporada alta.",
        crumb_zh="头巾与长袍辅料",
        crumb_en="Modest Wear Trims",
        crumb_ja="ヒジャブ・アバヤの副資材",
        crumb_ko="히잡·아바야 부자재",
        crumb_fr="Accessoires modest wear",
        crumb_es="Accesorios modest wear",
        h1_zh="头巾与长袍（适度着装）服装辅料指南",
        h1_en="Modest Wear Trims Guide for Hijab and Abaya",
        h1_ja="ヒジャブ・アバヤ（モデストウェア）の副資材ガイド",
        h1_ko="히잡·아바야(모데스트 웨어) 의류 부자재 가이드",
        h1_fr="Guide des accessoires pour hijab et abaya",
        h1_es="Guía de accesorios para hiyab y abaya",
        tag_zh="品类指南",
        tag_en="Category Guide",
        tag_ja="カテゴリガイド",
        tag_ko="카테고리 가이드",
        tag_fr="Guide par catégorie",
        tag_es="Guía por categoría",
        sum_zh="轻薄垂坠面料的三大辅料难点、主唛与洗水标的位置材质缝制怎么一起定、阿拉伯语双语标签的排版与信息顺序、头巾与内衬帽专属细节、市场合规与旺季备货，以及礼赠包装要点。",
        sum_en="Three trim challenges on light flowing fabric, deciding position, material and stitching together, Arabic bilingual label layout and order, hijab and undercap details, compliance and seasonal planning.",
        sum_ja="薄手ドレープ生地の3つの難所、位置・素材・縫製を同時に決める進め方、アラビア語併記の組みと情報順、ヒジャブとアンダーキャップの細部、市場適合と繁忙期の計画。",
        sum_ko="얇고 흐르는 원단의 세 가지 난점, 위치·소재·봉제를 함께 정하는 방법, 아랍어 병기 조판과 정보 순서, 히잡과 언더캡 디테일, 시장 적합성과 성수기 계획.",
        sum_fr="Trois difficultés du tissu fluide, décider position, matière et couture ensemble, composition bilingue arabe, détails hijab et sous-bonnet, conformité et planification saisonnière.",
        sum_es="Tres dificultades del tejido fluido, decidir posición, material y costura a la vez, composición bilingüe en árabe, detalles de hiyab y gorro interior, conformidad y planificación estacional.",
    ),
]
