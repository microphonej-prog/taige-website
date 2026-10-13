#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-13 第三批（20:00 时段）每日更新：2 篇新文章元数据（六语：zh-Hant 根 / en / ja / ko / fr / es）

选题说明（主题池 30 项连同既有扩展均已上线；本次沿两条全站扫描确认的空白品类线索扩展，
已核对 blog/、en|ja|ko|fr|es/blog/ 与 sitemap.xml 无重复 slug）：

- neckwear-trims-label-guide.html：领带、领结与领巾（颈饰）辅料与标签指南。
  全站扫描：「领带」0 处、「领结」0 处、「necktie」0 处、「bow tie」0 处。既有的品类文章覆盖了
  针织、衬衫、牛仔、泳装、内衣、童装、校服、财务装/礼服、汉服、舞蹈服、鞋包、家纺边角等，
  唯独「颈饰」这一服装品类从未成文（帽子围巾手套由 hat-scarf-gloves-trims-guide 覆盖，不含领带领结）。
  本文落点是「颈饰六类辅料构成表 → 领带/预打结领结/自打领结/方巾的标签位置 → 成分与材质标注口径
  （真丝涤丝混纺、皮革部件、多语言）→ 尺码与长度信息如何与库存系统一致 → 礼盒衬板与出口包装
  → 童装颈饰的绳带与小部件安全」，不涉及价格数字。

- belts-suspenders-trims-guide.html：腰带与背带辅料与标签指南。
  全站扫描：「腰带」0 处、「皮带」0 处、「背带」0 处、「suspender」0 处；「belt」仅出现在服装类文章
  的顺带提及（如裙装、牛仔）。既有金属件文章（metal-trims-nickel-release-guide、trim-metal-salt-spray-guide）
  讲限值与测试方法，leather-garment-trims-guide 讲皮革服装辅料，clothing-size-label-guide 讲号型体系，
  但没有把「腰带/背带这种五金+皮革+织带的组合件」单独成篇。
  本文落点是「六类辅料构成表 → 尺码标注三种口径（数字腰围/英寸/字母）与退货关系 → 真皮与二层皮、
  再生皮、PU 的标识边界 → 扣头镍释放与盐雾、颜色一致性 → 包装出口与抽查验收」，法规只写方向与口径，
  不引用具体限值数字与价格。
"""

ARTICLES = [
    dict(
        slug="neckwear-trims-label-guide.html",
        body="blog/_body_neckwear.html",
        title_zh="领带与领结辅料标签指南：主唛、成分标与礼盒怎么配 | TAGE",
        title_en="Necktie and Bow Tie Trims Guide: Neck Labels, Composition and Gift Packaging | TAGE",
        title_ja="ネクタイ・蝶ネクタイの副資材ガイド：メインラベル・組成表示・ギフト包装 | TAGE",
        title_ko="넥타이·보타이 부자재 가이드: 메인 라벨, 조성 라벨, 선물 포장 | TAGE",
        title_fr="Guide des accessoires pour cravates et noeuds papillon : labels, composition et emballage cadeau | TAGE",
        title_es="Guía de accesorios para corbatas y pajaritas: etiquetas, composición y embalaje de regalo | TAGE",
        desc_zh="领带与领结辅料标签指南：主唛与成分标缝在哪里、真丝与涤丝的成分标注口径、尺码与长度信息怎么标、礼盒衬板包装以及童装颈饰的绳带安全注意点，附规格确认清单。来自东莞泰阁包装。",
        desc_en="Necktie and bow tie trims guide: where neck and composition labels are sewn, silk versus polyester marking, sizing, gift boxes and children's neckwear safety.",
        desc_ja="ネクタイ・蝶ネクタイの副資材ガイド。メインラベルと組成表示の縫い付け位置、シルクとポリエステルの表示、サイズと長さ情報、ギフトボックスと台紙の包装、子ども用ネックウェアのひも安全まで解説します。東莞泰閣包装。",
        desc_ko="넥타이·보타이 부자재 가이드. 메인 라벨과 조성 라벨의 봉제 위치, 실크와 폴리에스터 표시, 사이즈와 길이 정보, 선물 상자와 받침 카드 포장, 아동용 넥웨어 끈 안전까지 정리했습니다. 둥관 TAGE 패키징.",
        desc_fr="Guide des accessoires pour cravates et noeuds papillon : où coudre les étiquettes, marquage de la soie et du polyester, tailles, coffrets et sécurité du neckwear enfant.",
        desc_es="Guía de accesorios para corbatas y pajaritas: dónde coser las etiquetas, marcado de seda y poliéster, tallas, estuches y seguridad del neckwear infantil.",
        crumb_zh="领带与领结辅料",
        crumb_en="Necktie and Bow Tie Trims",
        crumb_ja="ネクタイ・蝶ネクタイの副資材",
        crumb_ko="넥타이·보타이 부자재",
        crumb_fr="Accessoires pour cravates et noeuds papillon",
        crumb_es="Accesorios para corbatas y pajaritas",
        h1_zh="领带与领结辅料指南：主唛、成分标与包装怎么配",
        h1_en="Necktie and Bow Tie Trims: Where Labels Go and How to Pack Them",
        h1_ja="ネクタイと蝶ネクタイの副資材ガイド：ラベルの位置と包装の選び方",
        h1_ko="넥타이·보타이 부자재 가이드: 라벨 위치와 포장 선택법",
        h1_fr="Guide des accessoires pour cravates et noeuds papillon : où placer les étiquettes et comment emballer",
        h1_es="Guía de accesorios para corbatas y pajaritas: dónde van las etiquetas y cómo embalar",
        tag_zh="品类指南",
        tag_en="Category Guide",
        tag_ja="カテゴリガイド",
        tag_ko="카테고리 가이드",
        tag_fr="Guide par catégorie",
        tag_es="Guía por categoría",
        sum_zh="领带、领结与领巾的辅料不止一张主唛：标签缝在哪里、真丝与涤丝怎么标、尺码与长度信息、礼盒衬板包装、童装颈饰的绳带安全，一次讲清。",
        sum_en="Neckties, bow ties and scarves need more than a neck label: placement, silk versus polyester marking, sizing, gift-box packing and children's neckwear safety.",
        sum_ja="ネクタイ・蝶ネクタイ・スカーフに必要なのはメインラベルだけではありません。ラベル位置、シルクとポリエステルの表示、サイズ、ギフト包装、子ども用の安全まで整理します。",
        sum_ko="넥타이, 보타이, 스카프에 필요한 것은 메인 라벨만이 아닙니다. 라벨 위치, 실크와 폴리에스터 표시, 사이즈, 선물 포장, 아동용 안전까지 정리했습니다.",
        sum_fr="Cravates, noeuds papillon et foulards exigent plus qu'un label : placement, marquage soie et polyester, tailles, emballage cadeau et sécurité enfant.",
        sum_es="Corbatas, pajaritas y pañuelos necesitan más que una etiqueta: colocación, marcado de seda y poliéster, tallas, embalaje de regalo y seguridad infantil.",
    ),
    dict(
        slug="belts-suspenders-trims-guide.html",
        body="blog/_body_belts.html",
        title_zh="腰带与背带辅料指南：尺码标、材质标与包装怎么配 | TAGE",
        title_en="Belt and Suspender Trims Guide: Size Labels, Material Marking and Packaging | TAGE",
        title_ja="ベルト・サスペンダーの副資材ガイド：サイズ表示・素材表示・包装 | TAGE",
        title_ko="벨트·서스펜더 부자재 가이드: 사이즈 라벨, 소재 표시, 포장 | TAGE",
        title_fr="Guide des accessoires pour ceintures et bretelles : taille, matière et emballage | TAGE",
        title_es="Guía de accesorios para cinturones y tirantes: talla, material y embalaje | TAGE",
        desc_zh="腰带与背带辅料指南：尺码标注口径怎么定才不退货、真皮与二层皮再生皮的标识边界、扣头镍释放与盐雾要求、织带与弹性件成分标注、包装出口与抽查验收方法。来自东莞泰阁包装。",
        desc_en="Belts and suspenders trims guide: size conventions that cause returns, genuine versus bonded leather marking, buckle nickel release and salt spray, and export packing.",
        desc_ja="ベルトとサスペンダーの副資材ガイド。返品を招くサイズ表記、本革・二層革・再生革の表示境界、バックルのニッケル溶出と塩水噴霧、織帯の組成表示、包装と抜き取り検収まで解説します。東莞泰閣包装。",
        desc_ko="벨트와 서스펜더 부자재 가이드. 반품을 부르는 사이즈 표기, 천연 가죽·스플릿·재생 가죽 표시 경계, 버클 니켈 용출과 염수 분무, 웨빙 조성 표시, 포장과 샘플링 검수까지 정리했습니다. 둥관 TAGE 패키징.",
        desc_fr="Guide des accessoires pour ceintures et bretelles : conventions de taille, cuir véritable ou reconstitué, nickel et brouillard salin, emballage export.",
        desc_es="Guía de accesorios para cinturones y tirantes: convenciones de talla, piel genuina o regenerada, níquel y niebla salina, embalaje de exportación.",
        crumb_zh="腰带与背带辅料",
        crumb_en="Belt and Suspender Trims",
        crumb_ja="ベルト・サスペンダーの副資材",
        crumb_ko="벨트·서스펜더 부자재",
        crumb_fr="Accessoires pour ceintures et bretelles",
        crumb_es="Accesorios para cinturones y tirantes",
        h1_zh="腰带与背带辅料指南：尺码标、材质标与包装怎么配",
        h1_en="Belt and Suspender Trims: Getting Size, Material Marking and Packing Right",
        h1_ja="ベルトとサスペンダーの副資材ガイド：サイズ・素材表示と包装の決め方",
        h1_ko="벨트와 서스펜더 부자재 가이드: 사이즈·소재 표시와 포장 정하기",
        h1_fr="Guide des accessoires pour ceintures et bretelles : taille, marquage matière et emballage",
        h1_es="Guía de accesorios para cinturones y tirantes: talla, marcado de material y embalaje",
        tag_zh="品类指南",
        tag_en="Category Guide",
        tag_ja="カテゴリガイド",
        tag_ko="카테고리 가이드",
        tag_fr="Guide par catégorie",
        tag_es="Guía por categoría",
        sum_zh="腰带与背带是五金、皮革与标签的组合件：尺码口径怎么定、真皮与再生皮怎么标、扣头镍释放与盐雾、包装与抽查验收，一次讲清。",
        sum_en="Belts and suspenders combine hardware, leather and labels: size conventions, genuine versus bonded leather, buckle nickel and salt spray, packing and sampling.",
        sum_ja="ベルトとサスペンダーは金具・皮革・ラベルの組み合わせです。サイズ基準、本革と再生革の表示、ニッケルと塩水噴霧、包装と抜き取り検収を整理します。",
        sum_ko="벨트와 서스펜더는 금속 부품, 가죽, 라벨의 조합입니다. 사이즈 기준, 천연 가죽과 재생 가죽 표시, 니켈과 염수 분무, 포장과 샘플링 검수를 정리했습니다.",
        sum_fr="Ceintures et bretelles mêlent quincaillerie, cuir et étiquettes : conventions de taille, cuir véritable ou reconstitué, nickel, emballage et contrôle.",
        sum_es="Cinturones y tirantes combinan quincallería, cuero y etiquetas: convenciones de talla, piel genuina o regenerada, níquel, embalaje y control.",
    ),
]
