#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-03 上午批次（8:00）每日更新：2 篇新文章元数据（六语：zh-Hant 根 / en / ja / ko / fr / es）

选题说明（30 项主题池与历次扩展选题均已上线，本次沿「皮革类服装」与「童装」两个尚未覆盖的
服装品类扩展，已核对 blog/、en|ja|ko|fr|es/blog/ 与 sitemap.xml 无重复，并 grep 全站确认：

- leather-garment-trims-guide vs leather-patch-labels（只讲皮牌本体的材质/工艺/验收）、
  clothing-label-compliance-*（合规清单，皮革仅一笔带过）、denim/footwear（品类指南，不涉皮革）；
  全站无「皮革服装辅料」专文：本文是皮衣/皮裙/皮裤的干洗耐受、针孔不可修复、与鞣剂相容性、
  增塑剂迁移、镍释放、包装防压防潮的选型与验证体系。
- childrenswear-trims-guide vs clothing-label-children-safety（讲 CPSIA/EN 14682 合规与
  吊牌油墨安全，属法规视角）、clothing-size-label-guide（尺码标识）、elastic/buttons
  （成人向辅料参数）；全站无「童装辅料选型」专文：本文给分龄（0–3/3–8/8–14）配置表、
  标签柔软度与热压温度窗口、小件拉脱力与绳长、分档包装与洗护信息可读性。
"""

ARTICLES = [
    dict(
        slug="leather-garment-trims-guide.html",
        body="blog/_body_leather.html",
        title_zh="皮革与仿皮服装辅料指南：皮牌、吊牌、洗水标与五金怎么选 | TAGE",
        title_en="Leather Garment Trims Guide: Leather Patches, Hang Tags, Care Labels &amp; Hardware | TAGE",
        title_ja="レザー・合皮衣料の副資材ガイド：レザーパッチ・タグ・洗濯表示ラベル・金具の選び方 | TAGE",
        title_ko="가죽·인조가죽 의류 부자재 가이드: 가죽 패치, 행택, 세탁 표시 라벨, 금속 부자재 | TAGE",
        title_fr="Guide des accessoires pour cuir et simili : patchs, étiquettes et quincaillerie | TAGE",
        title_es="Guía de accesorios para cuero y simil: parches, etiquetas y herrajes | TAGE",
        desc_zh="皮革服装辅料指南：讲清皮牌、主唛、洗水标与吊牌五金在干洗耐受、针孔不可修复与色迁移上的特殊要求，用对照表比较真皮皮牌、再生皮、缎面织唛与低温热压无感标的耐干洗表现，并给出缝制位置、镍释放测试与包装防压防潮要点，附可直接使用的询价清单。东莞泰阁包装。",
        desc_en="Leather garment trims guide: leather patches, neck and care labels, hang tags and hardware — dry-clean resistance, needle holes, nickel release and packing.",
        desc_ja="レザー・合皮衣料の副資材ガイド。レザーパッチ、メインラベル、洗濯表示ラベル、タグと金具について、ドライ耐性・針穴が戻らないこと・色移りの三つの要件を整理し、本革・再生皮革・サテン織り・低温熱圧着の比較表、縫い位置、ニッケル溶出試験、防圧・防湿の包装、そのまま使える見積りチェックリストを掲載。東莞泰閣包装。",
        desc_ko="가죽·인조가죽 의류 부자재 가이드. 가죽 패치, 메인 라벨, 세탁 표시 라벨, 행택과 금속 부자재를 드라이 내성·바늘 구멍·이염의 세 가지 요건으로 정리하고, 천연가죽·재생가죽·새틴 직조·저온 열전사 비교표, 부착 위치, 니켈 용출 시험, 방압·방습 포장, 바로 쓰는 견적 체크리스트를 담았습니다. 둥관 TAGE 패키징.",
        desc_fr="Guide des accessoires pour cuir : patchs, labels de col et d'entretien, étiquettes suspendues et quincaillerie — tenue au nettoyage à sec, trous d'aiguille, nickel et emballage.",
        desc_es="Guía de accesorios para cuero: parches, etiquetas de cuello y cuidado, colgantes y herrajes — limpieza en seco, agujeros de aguja, níquel y embalaje.",
        crumb_zh="皮革服装辅料指南",
        crumb_en="Leather Garment Trims Guide",
        crumb_ja="レザー衣料の副資材ガイド",
        crumb_ko="가죽 의류 부자재 가이드",
        crumb_fr="Guide accessoires cuir",
        crumb_es="Guía de accesorios de cuero",
        h1_zh="皮革与仿皮服装辅料指南：标签、吊牌与五金的选型要点",
        h1_en="Leather and Faux-Leather Garment Trims: Labels, Tags and Hardware",
        h1_ja="レザー・合皮衣料の副資材ガイド：ラベル・タグ・金具の選定ポイント",
        h1_ko="가죽·인조가죽 의류 부자재 가이드: 라벨, 행택, 금속 부자재 선택 기준",
        h1_fr="Accessoires pour cuir et simili : labels, étiquettes et quincaillerie",
        h1_es="Accesorios para cuero y simil: etiquetas, colgantes y herrajes",
        tag_zh="皮革辅料",
        tag_en="Leather Trims",
        tag_ja="レザー副資材",
        tag_ko="가죽 부자재",
        tag_fr="Accessoires cuir",
        tag_es="Accesorios de cuero",
        sum_zh="皮衣、皮裙、皮裤的辅料要过干洗、不在皮面留针孔、不掉色不刮面。本文给出皮牌与主唛四种方案的耐干洗对照、洗水标符号与缝制位置、吊绳与五金的安全要点，以及防压防潮的包装做法。",
        sum_en="Leather trims must survive dry cleaning, leave no needle holes and never bleed or scratch. Compare four patch options, care-label symbols and placement, cord and hardware safety, plus packing that resists pressure and damp.",
        sum_ja="レザー・合皮の副資材はドライ耐性、針穴を残さないこと、色落ちと擦り傷の防止が要点です。パッチ4方式の比較、洗濯表示の記号と縫い位置、ひもと金具の安全、防圧・防湿の包装をまとめました。",
        sum_ko="가죽·인조가죽 부자재는 드라이 내성, 바늘 구멍 방지, 이염과 긁힘 방지가 핵심입니다. 패치 네 가지 방식 비교, 세탁 표시 기호와 부착 위치, 끈과 금속 부자재 안전, 방압·방습 포장을 정리했습니다.",
        sum_fr="Les accessoires cuir doivent tenir au nettoyage à sec, ne pas percer la matière et ne jamais déteindre. Comparaison de quatre patchs, symboles et placement, sécurité des cordons et emballage anti-pression.",
        sum_es="Los accesorios de cuero deben resistir la limpieza en seco, no dejar agujeros y no desteñir ni rayar. Comparativa de cuatro parches, símbolos y posición, seguridad de cordones y embalaje anti-presión.",
    ),
    dict(
        slug="childrenswear-trims-guide.html",
        body="blog/_body_children.html",
        title_zh="童装辅料选型指南：分龄配置、无感标签与小件安全 | TAGE",
        title_en="Childrenswear Trims Guide: Age-Tiered Labels, Soft Tags &amp; Small-Part Safety | TAGE",
        title_ja="子供服の副資材ガイド：年齢別構成・無感ラベル・小部品の安全 | TAGE",
        title_ko="아동복 부자재 가이드: 연령별 구성, 무감 라벨, 소부품 안전 | TAGE",
        title_fr="Guide des accessoires enfant : par âge, étiquettes douces et sécurité | TAGE",
        title_es="Guía de accesorios infantiles: por edades, etiquetas suaves y seguridad | TAGE",
        desc_zh="童装辅料选型指南：按 0–3 岁、3–8 岁、8–14 岁给出主唛、洗水标与吊牌的配置表，讲清标签柔软度与热压温度窗口、小件拉脱力与绳带长度要求、备用扣与分档包装做法，并附可复用的询价与验收清单。东莞泰阁包装。",
        desc_en="Childrenswear trims guide: age-tiered label and tag configuration, soft and tear-away labels, small-part pull strength, cord lengths and tiered packing.",
        desc_ja="子供服の副資材ガイド。0〜3歳・3〜8歳・8〜14歳の年齢別にメインラベル・洗濯表示ラベル・タグの構成表を示し、ラベルの柔らかさと熱圧着の温度管理、小部品の引張強度とひも長、予備ボタン、サイズ別梱包、見積りと検収のチェックリストを掲載。東莞泰閣包装。",
        desc_ko="아동복 부자재 가이드. 0~3세·3~8세·8~14세 연령대별로 메인 라벨, 세탁 표시 라벨, 행택 구성을 제시하고 라벨 부드러움과 열압착 온도 관리, 소부품 인장 강도와 끈 길이, 여분 단추, 사이즈별 포장, 견적과 검수 체크리스트를 담았습니다. 둥관 TAGE 패키징.",
        desc_fr="Guide des accessoires enfant : configuration par tranche d'âge, étiquettes douces ou détachables, résistance des petites pièces, longueur de cordons et emballage par taille.",
        desc_es="Guía de accesorios infantiles: configuración por edades, etiquetas suaves o desprendibles, resistencia de piezas pequeñas, largo de cordones y embalaje por talla.",
        crumb_zh="童装辅料指南",
        crumb_en="Childrenswear Trims Guide",
        crumb_ja="子供服の副資材ガイド",
        crumb_ko="아동복 부자재 가이드",
        crumb_fr="Guide accessoires enfant",
        crumb_es="Guía de accesorios infantiles",
        h1_zh="童装辅料选型指南：分龄配置、无感标签与小件安全",
        h1_en="Childrenswear Trims: Age-Tiered Labels, Soft Options and Small-Part Safety",
        h1_ja="子供服の副資材ガイド：年齢別構成・無感ラベル・小部品の安全",
        h1_ko="아동복 부자재 가이드: 연령별 구성, 무감 라벨, 소부품 안전",
        h1_fr="Accessoires enfant : par âge, étiquettes douces et sécurité des petites pièces",
        h1_es="Accesorios infantiles: por edades, etiquetas suaves y seguridad de piezas pequeñas",
        tag_zh="童装辅料",
        tag_en="Kids Trims",
        tag_ja="子供服副資材",
        tag_ko="아동복 부자재",
        tag_fr="Accessoires enfant",
        tag_es="Accesorios infantiles",
        sum_zh="童装辅料的底线是柔软不刺痒、牢固不易脱、信息清楚可读。本文给出 0–3、3–8、8–14 岁三档配置表、标签热压温度与边缘处理要点、小件拉脱力与绳带长度检查线，以及分档包装与洗护信息写法。",
        sum_en="Childrenswear trims must be soft, stay attached and read clearly. Three age tiers, heat-setting and edge treatment, small-part and cord checks, plus tiered packing and readable care information.",
        sum_ja="子供服の副資材は柔らかさ、外れにくさ、読みやすさが基本です。0〜3・3〜8・8〜14歳の構成表、熱圧着温度と端処理、小部品とひもの確認、サイズ別梱包とケア情報の書き方をまとめました。",
        sum_ko="아동복 부자재는 부드러움, 견고함, 읽기 쉬운 정보가 기본입니다. 0~3·3~8·8~14세 구성표, 열압착 온도와 가장자리 처리, 소부품과 끈 점검, 사이즈별 포장과 관리 정보 표기법을 정리했습니다.",
        sum_fr="Les accessoires enfant doivent être doux, solides et lisibles. Trois tranches d'âge, pose à chaud et bords, contrôle des petites pièces et cordons, emballage par taille.",
        sum_es="Los accesorios infantiles deben ser suaves, firmes y legibles. Tres franjas de edad, termosellado y bordes, control de piezas pequeñas y cordones, y embalaje por talla.",
    ),
]
