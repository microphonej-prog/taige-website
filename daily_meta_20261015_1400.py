#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-15 第二批（14:00 时段）每日更新：2 篇新文章元数据（六语：zh-Hant 根 / en / ja / ko / fr / es）

选题说明（主题池 30 项连同既有扩展均已上线，本次为全站六语关键词扫描后的空白扩展）：

- ribbon-trims-guide.html：服装丝带与缎带辅料指南。
  全站扫描：「丝带」54 处、「缎带」66 处，散落在礼盒、汉服、婚纱、纸袋提手等文章里作为配角提及，
  「grosgrain」全站仅 8 处（集中在 luxury-hang-tag-guide 的吊牌挂绳句）、「velvet ribbon」0 处、
  h1 从无一篇以丝带/缎带为主角；纸袋提手、汉服系带、花边蕾丝三篇各覆盖一个侧面。
  本篇落点：四种用途的验收指标对照表 → 五种材质织法 → 宽度厚度与缩水换算 → 上色与印字工艺
  → 热切冷切与固定收边 → 洗护测试验收 → 询价清单，与上述三篇互补并内链。

- eu-green-claims-apparel-labels.html：欧盟绿色声明新规（ECGT / Directive (EU) 2024/825）与服装标签。
  全站扫描：「漂綠」2 处、「greenwashing」6 处（均在 paper-bag-window-guide 的回收设计段），
  「2024/825」0 处、「green claims directive」提案状态 0 处；既有 certification-claims-label-guide
  讲「认证标志能不能印」，garment-packaging-ecofriendly 讲包装环保趋势，trims-carbon-footprint-guide
  讲碳足迹问卷，均未覆盖 2026-09-27 起适用的禁止性规则。
  事实核对（2026-10-15 联网检索：欧委会消费者专题页、欧洲议会立法进展、多家律所简报）：
  ① 指令 2024/825（ECGT）2024-02-28 通过，成员国 2026-03-27 前完成国内法转化，2026-09-27 起适用；
  ② 禁止泛泛环保声明（eco-friendly / green / climate neutral / biodegradable 等，除非能证明公认的优良环境表现）、
     自创或自我认证的可持续标签、仅覆盖局部却暗示整体的声明、以碳抵消支撑的中和类声明；
  ③ 原拟的《绿色声明指令》提案：欧委会 2025-06-20 宣布撤回意向，并列入 2026 年工作计划（COM(2025)870）的撤回清单。
  文中合规口径一律写成「以主管机构当年公告为准」，不写死费用与罚则数字。
"""

ARTICLES = [
    dict(
        slug="ribbon-trims-guide.html",
        body="blog/_body_ribbon.html",
        title_zh="服装丝带与缎带辅料指南：材质、宽度、印刷与固定方式 | TAGE",
        title_en="Ribbon Trims Guide: Satin, Grosgrain, Widths, Printing and Fixing | TAGE",
        title_ja="衣料用リボン・テープ副資材ガイド：素材・幅・印刷・固定方法 | TAGE",
        title_ko="의류 리본·테이프 부자재 가이드: 소재, 폭, 인쇄, 고정 방법 | TAGE",
        title_fr="Guide des rubans et galons pour l'habillement : matière, largeur, impression et fixation | TAGE",
        title_es="Guía de lazos y cintas para prendas: material, ancho, impresión y fijación | TAGE",
        desc_zh="服装丝带与缎带辅料指南：四种用途的验收指标、缎带与罗纹带等五种材质织法对比、宽度厚度与洗后缩水换算、印字工艺与耐洗要求、热切冷切与固定收边要点，附可直接复制的询价清单。来自东莞泰阁包装。",
        desc_en="Ribbon trims guide: satin, grosgrain, organza, velvet and cotton tape, fixing width and shrinkage, printing, edge cutting, wash testing and an enquiry list.",
        desc_ja="衣料用リボン・テープの副資材ガイド。4つの用途別の検収指標、サテンやグログランなど5素材の比較、幅と厚みと洗濯収縮の換算、印刷方法と耐洗濯性、熱カットと冷間カット・固定と端始末の要点、そのまま使える見積り依頼リストをまとめます。東莞泰閣包装。",
        desc_ko="의류 리본·테이프 부자재 가이드. 용도별 검수 지표, 새틴과 그로스그레인 등 다섯 소재 비교, 폭과 두께 및 세탁 수축 환산, 인쇄 방식과 내세탁성, 열 절단과 냉간 절단 및 고정 마감의 요점, 견적 요청 리스트를 정리했습니다. 둥관 TAGE 패키징.",
        desc_fr="Guide des rubans et galons : critères par usage, satin, gros-grain, organza, velours et coton, largeur, impression, coupe à chaud ou à froid, essais de lavage et liste de demande de prix.",
        desc_es="Guía de lazos y cintas: criterios según el uso, satén, grosgrain, organza, terciopelo y algodón, ancho, impresión, corte en caliente o en frío, ensayos de lavado y lista de cotización.",
        crumb_zh="丝带与缎带辅料",
        crumb_en="Ribbon Trims",
        crumb_ja="リボン・テープ副資材",
        crumb_ko="리본·테이프 부자재",
        crumb_fr="Rubans et galons",
        crumb_es="Lazos y cintas",
        h1_zh="服装丝带与缎带辅料指南：材质、宽度、印刷与固定方式",
        h1_en="Ribbon Trims Guide: Material, Width, Printing and Fixing",
        h1_ja="衣料用リボン・テープ副資材ガイド：素材、幅、印刷、固定方法",
        h1_ko="의류 리본·테이프 부자재 가이드: 소재, 폭, 인쇄, 고정 방법",
        h1_fr="Guide des rubans et galons : matière, largeur, impression et fixation",
        h1_es="Guía de lazos y cintas: material, ancho, impresión y fijación",
        tag_zh="丝带与织带",
        tag_en="Ribbon & Tape",
        tag_ja="リボンとテープ",
        tag_ko="리본과 테이프",
        tag_fr="Rubans et galons",
        tag_es="Lazos y cintas",
        sum_zh="四种用途各自的验收指标、五种材质织法对比、宽度与厚度的定法、上色与印字工艺、固定与收边，以及一份可直接复制的询价清单。",
        sum_en="Inspection criteria by end use, five materials compared, how to fix width and thickness, colouring and printing, fixing and edge finish, plus a copy-and-send enquiry list.",
        sum_ja="用途別の検収指標、5素材の比較、幅と厚みの決め方、着色と印刷、固定と端始末、そのまま使える見積り依頼リスト。",
        sum_ko="용도별 검수 지표, 다섯 소재 비교, 폭과 두께 설정, 착색과 인쇄, 고정과 마감, 그대로 쓸 수 있는 견적 요청 리스트.",
        sum_fr="Critères par usage, cinq matières comparées, largeur et épaisseur, coloration et impression, fixation et finition, plus une liste de demande de prix.",
        sum_es="Criterios por uso, cinco materiales comparados, ancho y grosor, color e impresión, fijación y acabado, y una lista de cotización.",
    ),
    dict(
        slug="eu-green-claims-apparel-labels.html",
        body="blog/_body_greenclaims.html",
        title_zh="欧盟绿色声明新规与服装标签：2026 年 9 月起哪些环保说法不能印 | TAGE",
        title_en="EU Green Claims Rules for Apparel Labels and Packaging: What You Cannot Print | TAGE",
        title_ja="EUグリーンクレーム新規則と衣料ラベル：印刷できなくなった環境表現 | TAGE",
        title_ko="EU 그린 클레임 신규 규정과 의류 라벨: 인쇄할 수 없게 된 친환경 표현 | TAGE",
        title_fr="Allégations vertes et étiquettes textiles : ce que l'UE interdit depuis septembre 2026 | TAGE",
        title_es="Alegaciones verdes y etiquetas de prendas: lo que la UE prohíbe desde septiembre de 2026 | TAGE",
        desc_zh="欧盟《赋能消费者绿色转型指令》（2024/825，ECGT）自 2026 年 9 月 27 日起适用：泛泛环保声明、自创绿色标签与抵消型碳中和表述被禁。本文给出吊牌与包装的改写对照表、认证标志要点与出口前自查八项。来自东莞泰阁包装。",
        desc_en="From 27 September 2026 EU rules ban generic green claims, self-made eco labels and offset-based neutrality. Rewrite guide for apparel tags and packaging.",
        desc_ja="EUのグリーンクレーム新規則（2024/825・ECGT）が2026年9月27日から適用。一般化した環境訴求、自作エコラベル、オフセット型カーボンニュートラルは禁止です。タグと包装の言い換え表、認証マークの使い方、証拠チェーンの分担、出荷前チェック8項目を整理します。東莞泰閣包装。",
        desc_ko="EU 그린 클레임 신규 규정(2024/825, ECGT)이 2026년 9월 27일부터 적용됩니다. 포괄적 친환경 표현, 자체 제작 에코 라벨, 상쇄형 탄소중립은 금지입니다. 행택과 포장 문구 수정표, 인증 마크 사용법, 증거 체계 분담, 출하 전 점검 여덟 항목을 정리했습니다. 둥관 TAGE 패키징.",
        desc_fr="Depuis le 27 septembre 2026, l'UE interdit les allégations vertes génériques, les écolabels auto-créés et la neutralité fondée sur la compensation : tableau de réécriture et contrôles.",
        desc_es="Desde el 27 de septiembre de 2026 la UE prohíbe alegaciones verdes genéricas, sellos autocreados y neutralidad por compensación: tabla de reescritura y comprobaciones.",
        crumb_zh="欧盟绿色声明新规",
        crumb_en="EU Green Claims Rules",
        crumb_ja="EUグリーンクレーム規則",
        crumb_ko="EU 그린 클레임 규정",
        crumb_fr="Allégations vertes UE",
        crumb_es="Alegaciones verdes UE",
        h1_zh="欧盟绿色声明新规与服装标签：2026 年 9 月起哪些环保说法不能印",
        h1_en="EU Green Claims Rules for Apparel Labels: What You Cannot Print",
        h1_ja="EUグリーンクレーム新規則と衣料ラベル：印刷できなくなった環境表現",
        h1_ko="EU 그린 클레임 신규 규정과 의류 라벨: 인쇄할 수 없게 된 친환경 표현",
        h1_fr="Allégations vertes et étiquettes textiles : ce que l'UE interdit depuis septembre 2026",
        h1_es="Alegaciones verdes y etiquetas de prendas: lo que la UE prohíbe desde septiembre de 2026",
        tag_zh="合规与法规",
        tag_en="Compliance",
        tag_ja="コンプライアンス",
        tag_ko="컴플라이언스",
        tag_fr="Conformité",
        tag_es="Cumplimiento",
        sum_zh="禁令覆盖哪些写法、吊牌与包装上最常见的五组表述怎么改、认证标志的使用边界、品牌与供应商的证据链分工，以及出口前自查八项。",
        sum_en="Which wordings the ban reaches, how to rewrite the five most common claims, the limits of certification marks, who holds the evidence, and eight pre-shipment checks.",
        sum_ja="禁止される文言、よくある5表現の書き換え、認証マークの使用範囲、ブランドとサプライヤーの証拠分担、出荷前チェック8項目。",
        sum_ko="금지되는 문구, 흔한 다섯 표현의 수정, 인증 마크 사용 범위, 브랜드와 공급사의 증거 분담, 출하 전 점검 여덟 항목.",
        sum_fr="Les formulations visées, la réécriture des cinq mentions les plus courantes, les limites des marques, le partage des preuves et huit contrôles avant expédition.",
        sum_es="Qué formulaciones quedan afectadas, cómo reescribir las cinco menciones más comunes, límites de las marcas, reparto de pruebas y ocho comprobaciones previas.",
    ),
]
