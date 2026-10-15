#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-15 第三批（20:00 时段）每日更新：2 篇新文章元数据（六语：zh-Hant 根 / en / ja / ko / fr / es）

选题说明（主题池 30 项连同既有扩展均已上线，本次为全站六语关键词扫描后的空白扩展）：

- trim-light-fastness-fading-guide.html：服装辅料耐光色牢度与褪色防治。
  全站扫描后确认这是真空白：「耐光色牢度」「蓝色羊毛」「氙弧 / 氙灯」在 270 篇文章里出现 0 次，
  「耐光」仅 10 篇作为附带提及（仓储、功能性服装、特殊效果、防伪那几篇），
  woven-label-colorfastness-guide 讲耐洗与耐摩擦、care-label-wash-durability 讲印刷耐洗，
  均未覆盖「洗过没事、挂到店里就褪色」这一类投诉。
  本篇落点：四种褪色成因 → ISO 105-B02 / GB/T 8427 / AATCC 16 三套方法的等级与曝光量 →
  六类辅料耐光表现对照表 → 设计与涂层端对策 → 规格书与验收写法 → 五个常见误区。

- trim-color-migration-staining-guide.html：服装辅料沾色与色迁移防治。
  全站扫描：「交叉染色」0 次、「沾色」仅 7 篇作为附带提及（面料兼容、里布、家纺等），
  既有文章讲的是吊牌与衣物的颜色「如何对齐」，没有一篇讲「深色辅料把浅色衣身染了」这条失败路径。
  本篇落点：三条迁移路径（湿态 / 摩擦 / 高温升华）与对应测试 → 五种高危组合 →
  设计与采购端预防（改用色纱、加隔离层、控制干燥、摆放顺序）→ 海运与仓储对策 →
  验收条款与客诉复现方法。

事实口径：涉及标准一律写方法名与等级体系（ISO 105-B02 / GB/T 8427 蓝色羊毛 1–8 级、
AATCC 16 灰卡 1–5 级、耐水 / 耐汗渍 / 耐摩擦 / 耐升华单项），不写死检测费用与交期数字，
容器温度写「常可达 50–60℃」区间，测试时长强调按曝光量而非小时数记录。
"""

ARTICLES = [
    dict(
        slug="trim-light-fastness-fading-guide.html",
        body="blog/_body_lightfast.html",
        title_zh="服装辅料耐光色牢度与褪色防治指南：吊牌、织唛与包装怎么抗晒 | TAGE",
        title_en="Trim Light Fastness Guide: Keep Hang Tags, Labels and Packaging From Fading | TAGE",
        title_ja="衣料副資材の耐光堅牢度と退色対策ガイド：タグ・織ラベル・包装を褪色から守る | TAGE",
        title_ko="의류 부자재 내광 견뢰도와 퇴색 대책 가이드: 행택, 직조 라벨, 포장을 지키는 법 | TAGE",
        title_fr="Guide de solidité à la lumière : éviter la décoloration des étiquettes et emballages | TAGE",
        title_es="Guía de solidez a la luz: evitar el desteñido de etiquetas y envases | TAGE",
        desc_zh="服装辅料耐光色牢度与褪色防治指南：四种褪色成因怎么区分、ISO 105-B02 与 AATCC 16 的蓝色羊毛评级怎么看、织唛吊牌织带包装的耐光表现对照，以及设计涂层与规格书要点。来自东莞泰阁包装。",
        desc_en="Trim light fastness guide: four causes of fading, how ISO 105-B02 and AATCC 16 blue wool grades work, material comparison and coatings that stop tags fading.",
        desc_ja="副資材の耐光堅牢度ガイド。退色の4原因の見分け方、ISO 105-B02 と AATCC 16 のブルースケール判定の読み方、タグ・織ラベル・テープ・包装の耐光性比較、コート選定と仕様書への書き方までまとめます。東莞泰閣包装。",
        desc_ko="부자재 내광 견뢰도 가이드. 퇴색의 네 가지 원인 구분, ISO 105-B02와 AATCC 16 블루 울 등급 읽는 법, 행택·직조 라벨·테이프·포장의 내광성 비교, 코팅 선택과 사양서 기재 방법을 정리했습니다. 둥관 TAGE 패키징.",
        desc_fr="Guide de solidité à la lumière : quatre causes de décoloration, notation laine bleue ISO 105-B02 et AATCC 16, comparaison des supports et vernis, rédaction du cahier des charges.",
        desc_es="Guía de solidez a la luz: cuatro causas del desteñido, notación lana azul ISO 105-B02 y AATCC 16, comparación de soportes y barnices, y redacción de la especificación.",
        crumb_zh="耐光色牢度与褪色",
        crumb_en="Light Fastness",
        crumb_ja="耐光堅牢度と退色",
        crumb_ko="내광 견뢰도와 퇴색",
        crumb_fr="Solidité à la lumière",
        crumb_es="Solidez a la luz",
        h1_zh="服装辅料耐光色牢度与褪色防治指南",
        h1_en="Trim Light Fastness and Fading Guide",
        h1_ja="衣料副資材の耐光堅牢度と退色対策ガイド",
        h1_ko="의류 부자재 내광 견뢰도와 퇴색 대책 가이드",
        h1_fr="Guide de solidité à la lumière des accessoires textiles",
        h1_es="Guía de solidez a la luz de los accesorios de confección",
        tag_zh="材质与工艺",
        tag_en="Material & Process",
        tag_ja="素材と工程",
        tag_ko="소재와 공정",
        tag_fr="Matière et procédé",
        tag_es="Material y proceso",
        sum_zh="四种褪色成因怎么区分、三套耐光标准的等级怎么读、六类辅料的耐光表现对照、设计涂层与展示端的防褪色做法，以及规格书与验收条款怎么写。",
        sum_en="How to tell the four causes of fading apart, how to read the three standards, a comparison across six trim types, coatings and display fixes, and spec wording.",
        sum_ja="退色の4原因の見分け方、3規格の等級の読み方、6種の副資材の耐光比較、コートと陳列側の対策、仕様書と検収の書き方。",
        sum_ko="퇴색의 네 가지 원인 구분, 세 표준의 등급 읽는 법, 여섯 가지 부자재 비교, 코팅과 진열 단계 대책, 사양서와 검수 기재 방법.",
        sum_fr="Distinguer les quatre causes, lire les trois référentiels, comparer six familles d'accessoires, vernis et exposition, et rédiger le cahier des charges.",
        sum_es="Distinguir las cuatro causas, leer las tres normas, comparar seis familias de accesorios, barnices y exposición, y redactar la especificación.",
    ),
    dict(
        slug="trim-color-migration-staining-guide.html",
        body="blog/_body_migration.html",
        title_zh="服装辅料沾色与色迁移防治指南：深色吊牌染到浅色衣服怎么办 | TAGE",
        title_en="Colour Migration Guide: Stop Dark Tags and Packaging Staining Garments | TAGE",
        title_ja="副資材の色移り対策ガイド：濃色タグが淡色衣料を染めるときの実務 | TAGE",
        title_ko="부자재 이염·색 이동 대책 가이드: 진한 행택이 연한 의류를 물들일 때 | TAGE",
        title_fr="Guide de migration de colorant : quand une étiquette foncée teinte un vêtement clair | TAGE",
        title_es="Guía de migración de colorante: cuando una etiqueta oscura tiñe una prenda clara | TAGE",
        desc_zh="深色吊牌、织唛或纸袋染到浅色衣服怎么办？本文拆解沾色与色迁移的三条路径（湿态、摩擦、高温升华）、五种高危组合、隔离与干燥的预防做法，以及海运仓储对策与客诉复现方法。来自东莞泰阁包装。",
        desc_en="Dark tags, labels or bags staining pale garments? Three migration routes, five risk combinations, barrier and drying fixes, shipping advice and complaint tests.",
        desc_ja="濃色のタグ・織ラベル・紙袋が淡色衣料を染めるときの実務ガイド。湿潤・摩擦・昇華の3経路、危険な5つの組み合わせ、隔離と乾燥の対策、海上輸送と保管、クレームの再現方法を整理します。東莞泰閣包装。",
        desc_ko="진한 행택·직조 라벨·종이백이 연한 의류를 물들일 때의 실무 가이드. 습윤·마찰·승화 세 경로, 위험한 다섯 조합, 차단과 건조 대책, 해상 운송과 보관, 클레임 재현 방법을 정리했습니다. 둥관 TAGE 패키징.",
        desc_fr="Étiquettes, labels ou sacs foncés qui teintent les vêtements clairs : trois voies de migration, cinq combinaisons à risque, barrières et séchage, transport et réclamations.",
        desc_es="Etiquetas, labels o bolsas oscuras que tiñen prendas claras: tres vías de migración, cinco combinaciones de riesgo, barreras y secado, transporte y reclamaciones.",
        crumb_zh="沾色与色迁移",
        crumb_en="Colour Migration",
        crumb_ja="色移り対策",
        crumb_ko="이염과 색 이동",
        crumb_fr="Migration de colorant",
        crumb_es="Migración de colorante",
        h1_zh="服装辅料沾色与色迁移防治指南",
        h1_en="Trim Colour Migration and Staining Guide",
        h1_ja="衣料副資材の色移り対策ガイド",
        h1_ko="의류 부자재 이염·색 이동 대책 가이드",
        h1_fr="Guide de migration de colorant des accessoires textiles",
        h1_es="Guía de migración de colorante en accesorios de confección",
        tag_zh="品质与检测",
        tag_en="Quality & Testing",
        tag_ja="品質と検査",
        tag_ko="품질과 검사",
        tag_fr="Qualité et essais",
        tag_es="Calidad y ensayos",
        sum_zh="三条迁移路径与对应测试、五种高危组合、隔离层与干燥控制、海运仓储对策，以及把沾色要求写进规格书和客诉复现的实操做法。",
        sum_en="The three migration routes and their tests, five risk combinations, barriers and drying control, sea freight and storage countermeasures, plus spec clauses and complaint testing.",
        sum_ja="3つの移行経路と対応試験、危険な5つの組み合わせ、隔離層と乾燥管理、海上輸送と保管の対策、仕様書への記載とクレーム再現の進め方。",
        sum_ko="세 가지 이동 경로와 대응 시험, 위험한 다섯 조합, 차단층과 건조 관리, 해상 운송과 보관 대책, 사양서 기재와 클레임 재현 방법.",
        sum_fr="Les trois voies de migration et leurs essais, cinq combinaisons à risque, barrières et maîtrise du séchage, transport et stockage, clauses et reproduction des réclamations.",
        sum_es="Las tres vías de migración y sus ensayos, cinco combinaciones de riesgo, barreras y control del secado, transporte y almacén, cláusulas y reproducción de quejas.",
    ),
]
