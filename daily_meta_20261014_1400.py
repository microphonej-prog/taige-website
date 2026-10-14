#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-14 第二批（14:00 时段）每日更新：2 篇新文章元数据（六语：zh-Hant 根 / en / ja / ko / fr / es）

选题说明（主题池 30 项连同既有扩展均已上线，本次为全站六语关键词扫描后的空白扩展）：

- garment-trims-storage-conditions-guide.html：服装辅料仓储与保管条件指南。
  全站扫描：「仓储」仅散见于其它文章，「库存保管」0 处，「胶水老化 / adhesive aging」0 处，
  「除湿 / dehumidifi」0 处，「保存期限」「stock rotation」0 处，且全站 h1 无一篇讲仓储保管。
  既有 garment-trims-inventory-management 讲库存水位与补货点（仓储只是其中一节），
  garment-moisture-proof-packaging 讲成品运输防潮，trim-vmi-consignment-stock-guide 讲寄售模式，
  本篇落点是「六类材料的失效方式对照表 → 温湿度光照三个环境数字 → 摆放与标识让先进先出可执行
  → 批次保鲜期与超期复检 → 发霉虫害异味处置顺序 → 留样色卡与巡查清单」，与上述三篇互补并内链。

- home-textile-label-packaging-guide.html：家纺（毛巾/床品/浴袍）标签与包装辅料指南。
  全站扫描：「床品」0 处、「home textile」仅 19 处（均在合规文章的品类列举中）、「medical」类的家纺品类
  h1 从未出现；毛巾仅出现在「毛巾绣」语境。既有的品类指南覆盖牛仔、针织、泳装、童装、宠物、
  婚纱等 30+ 成衣品类，唯独家纺（非穿着类纺织品）从未成文。
  事实核对（2026-10-14 联网）：
  ① 美国家用纺织品属《纺织纤维产品标识法》TFPIA 覆盖范围（FTC 官方指南，二手/明显使用过的家纺除外）；
  ② 法国家纺与服装、鞋同属 TLC 生产者责任延伸品类（源于 2007 年法规，由经认可的生态组织履约）；
  ③ 美国自 2022-11-12 起，婴儿床围与倾斜式婴儿睡床为禁用危险产品（CPSC Safe Sleep for Babies Act）。
  文中合规口径一律写成「以目标市场法规与主管机构当年公告为准」，不写死费用与期限数字。
"""

ARTICLES = [
    dict(
        slug="garment-trims-storage-conditions-guide.html",
        body="blog/_body_storage.html",
        title_zh="服装辅料仓储与保管指南：防潮、防黄变、防虫与先进先出 | TAGE",
        title_en="Garment Trims Storage Guide: Moisture, Yellowing, Pests and FIFO | TAGE",
        title_ja="衣料副資材の保管ガイド：防湿・黄変・虫害・先入れ先出し | TAGE",
        title_ko="의류 부자재 보관 가이드: 방습·황변·해충·선입선출 | TAGE",
        title_fr="Guide de stockage des accessoires textiles : humidité, jaunissement, nuisibles et FIFO | TAGE",
        title_es="Guía de almacenamiento de accesorios: humedad, amarilleo, plagas y FIFO | TAGE",
        desc_zh="服装辅料仓储与保管指南：纸类吊牌、织唛、洗水标、弹力带、胶粘料与金属件各自的失效方式，温度湿度与光照三个环境数字，摆放标识与先进先出执行，批次保鲜期与超期复检，发霉虫害异味的处置顺序，附巡查清单。来自东莞泰阁包装。",
        desc_en="How to store garment trims and labels: what paper tags, woven labels, elastic, adhesives and metal each suffer from, with humidity, FIFO and mould control.",
        desc_ja="衣料副資材の保管ガイド。紙もの・織りラベル・洗濯表示・ゴムテープ・粘着材・金属部品の劣化パターン、温度と湿度と光の3つの数字、棚表示と先入れ先出し、ロット別の使用期限、カビ・害虫・臭気の対処順序と点検リストを整理します。東莞泰閣包装。",
        desc_ko="의류 부자재 보관 가이드. 종이류·직조 라벨·세탁 라벨·고무 테이프·점착제·금속 부품의 열화 양상, 온도·습도·광량 세 가지 숫자, 선반 표시와 선입선출, 로트별 사용 기한, 곰팡이·해충·냄새 대응 순서와 점검표를 정리했습니다. 둥관 TAGE 패키징.",
        desc_fr="Guide de stockage des accessoires : défaillances du papier, des labels tissés, des élastiques, des adhésifs et du métal, température, humidité, lumière, FIFO et moisissures.",
        desc_es="Guía de almacenamiento de accesorios: cómo fallan papel, etiquetas tejidas, elásticos, adhesivos y metal, más humedad, luz, FIFO y control de moho.",
        crumb_zh="辅料仓储与保管",
        crumb_en="Trims Storage",
        crumb_ja="副資材の保管",
        crumb_ko="부자재 보관",
        crumb_fr="Stockage des accessoires",
        crumb_es="Almacenaje de accesorios",
        h1_zh="服装辅料仓储与保管指南：防潮、防黄变、防虫与先进先出",
        h1_en="Garment Trims Storage Guide: Moisture, Yellowing, Pests and FIFO",
        h1_ja="衣料副資材の保管ガイド：防湿・黄変・虫害・先入れ先出し",
        h1_ko="의류 부자재 보관 가이드: 방습, 황변, 해충, 선입선출",
        h1_fr="Guide de stockage des accessoires textiles : humidité, jaunissement, nuisibles et FIFO",
        h1_es="Guía de almacenamiento de accesorios: humedad, amarilleo, plagas y FIFO",
        tag_zh="仓储与品控",
        tag_en="Storage & QC",
        tag_ja="保管と品質管理",
        tag_ko="보관과 품질관리",
        tag_fr="Stockage et qualité",
        tag_es="Almacenaje y calidad",
        sum_zh="六类辅料各自的失效方式、温湿度与光照三个环境数字、货架标识与先进先出、批次保鲜期与超期复检、发霉虫害异味的处置顺序，附巡查清单。",
        sum_en="How six trim groups fail, the three environmental numbers, rack labelling and FIFO, batch shelf life, and the order to handle mould, pests and odour.",
        sum_ja="6系統の副資材の劣化パターン、温湿度と光の3つの数字、棚表示と先入れ先出し、ロット別の使用期限、カビ・害虫・臭気の対処順序と点検リスト。",
        sum_ko="여섯 가지 부자재의 열화 양상, 온도·습도·광량 세 가지 숫자, 선반 표시와 선입선출, 로트별 사용 기한, 곰팡이·해충·냄새 대응 순서와 점검표.",
        sum_fr="Les six familles d'accessoires et leurs défaillances, les trois chiffres d'environnement, rangement et FIFO, durée de vie par lot, moisissures et nuisibles.",
        sum_es="Cómo fallan las seis familias de accesorios, los tres números ambientales, colocación y FIFO, vida útil por lote, moho, plagas y olores.",
    ),
    dict(
        slug="home-textile-label-packaging-guide.html",
        body="blog/_body_hometextile.html",
        title_zh="家纺标签与包装辅料指南：毛巾、床品、浴袍怎么标怎么包 | TAGE",
        title_en="Home Textile Label and Packaging Guide: Towels, Bedding and Bathrobes | TAGE",
        title_ja="ホームテキスタイルのラベルと包装ガイド：タオル・寝具・バスローブ | TAGE",
        title_ko="홈텍스타일 라벨·포장 가이드: 타월, 침구, 목욕 가운 | TAGE",
        title_fr="Guide étiquettes et emballage pour le linge de maison : serviettes, literie et peignoirs | TAGE",
        title_es="Guía de etiquetas y embalaje para textil hogar: toallas, ropa de cama y albornoces | TAGE",
        desc_zh="家纺标签与包装辅料指南：纤维成分、产地与厂商身份怎么标，尺寸与克重怎么写，洗后稳定性与掉毛耐氯测试，酒店民宿与婴童家纺的额外要求，法国与荷兰生产者责任，吊牌腰封与包装形式怎么配。来自东莞泰阁包装。",
        desc_en="Home textile label and packaging guide: fibre content, origin, dimensions and weight, after-wash stability, hospitality and infant rules, tags and bands.",
        desc_ja="ホームテキスタイルのラベルと包装ガイド。繊維組成・原産地・事業者表示、寸法と目付の書き方、洗濯後の安定性、ホテル・民泊と乳幼児向けの追加要件、生産者責任、タグと帯紙の構成を解説します。東莞泰閣包装。",
        desc_ko="홈텍스타일 라벨·포장 가이드. 섬유 조성, 원산지, 제조자 표시, 치수와 중량 표기, 세탁 후 안정성, 호텔·민박과 유아용 추가 요건, 생산자 책임, 행택과 띠지 구성을 정리했습니다. 둥관 TAGE 패키징.",
        desc_fr="Guide étiquettes et emballage du linge de maison : composition, origine, fabricant, dimensions et grammage, stabilité au lavage, hôtellerie, bébés, étiquettes et bandeaux.",
        desc_es="Guía de etiquetas y embalaje para textil hogar: composición, origen, fabricante, medidas y gramaje, estabilidad tras lavado, hostelería, bebés, colgantes y fajas.",
        crumb_zh="家纺标签与包装",
        crumb_en="Home Textile Labels",
        crumb_ja="ホームテキスタイルのラベル",
        crumb_ko="홈텍스타일 라벨",
        crumb_fr="Linge de maison",
        crumb_es="Textil hogar",
        h1_zh="家纺标签与包装辅料指南：毛巾、床品、浴袍怎么标怎么包",
        h1_en="Home Textile Label and Packaging Guide: Towels, Bedding and Bathrobes",
        h1_ja="ホームテキスタイルのラベルと包装ガイド：タオル・寝具・バスローブ",
        h1_ko="홈텍스타일 라벨·포장 가이드: 타월, 침구, 목욕 가운",
        h1_fr="Guide étiquettes et emballage pour le linge de maison : serviettes, literie et peignoirs",
        h1_es="Guía de etiquetas y embalaje para textil hogar: toallas, ropa de cama y albornoces",
        tag_zh="品类指南",
        tag_en="Category Guide",
        tag_ja="カテゴリガイド",
        tag_ko="카테고리 가이드",
        tag_fr="Guide par catégorie",
        tag_es="Guía por categoría",
        sum_zh="家纺与服装标识的三处差别、成分产地与厂商身份四个必标项、尺寸与克重怎么写、酒店民宿与婴童家纺的额外要求、生产者责任与包装合规、吊牌腰封与包装形式。",
        sum_en="Three ways home textile marking differs from apparel, the four mandatory fields, dimensions and weight, hospitality and infant requirements, producer responsibility, tags and packing.",
        sum_ja="衣料との表示の違い3点、必須4項目、寸法と目付の書き方、ホテル・民泊と乳幼児向けの追加要件、生産者責任と包装規制、タグ・帯紙・包装形態。",
        sum_ko="의류와의 표시 차이 세 가지, 필수 네 항목, 치수와 중량 표기, 호텔·민박과 유아용 추가 요건, 생산자 책임과 포장 규제, 행택·띠지·포장 형태.",
        sum_fr="Trois différences avec l'habillement, quatre mentions obligatoires, dimensions et grammage, hôtellerie et bébés, responsabilité du producteur, étiquettes et emballage.",
        sum_es="Tres diferencias con la prenda, cuatro campos obligatorios, medidas y gramaje, hostelería e infantil, responsabilidad del productor, colgantes y embalaje.",
    ),
]
