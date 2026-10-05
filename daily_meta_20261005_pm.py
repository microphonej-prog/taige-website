#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-05 下午批次每日更新：2 篇新文章元数据（六语：zh-Hant 根 / en / ja / ko / fr / es）

选题说明（主题池 30 项与历次扩展（抽绳、花边、拉链、黏合衬、皮革、反光、魔术贴、纽扣、
弹性、里布、织带、滚边、垫肩等）均已上线，本次沿「缝制用线」与「阻燃防护辅料」两个
尚未独立成文的方向扩展，已核对 blog/、en|ja|ko|fr|es/blog/ 与 sitemap.xml 无重复，并 grep 全站确认：

- sewing-thread-selection-guide  vs garment-label-sewing-thread-guide（只讲主嘜/洗水标缝制用线）、
  zipper-selection-guide（仅一句顺带提到缝纫线同色）、rainwear 指南（只提「缝线要低吸水」）；
  全站无「缝纫线选型 / 线号 / 捻向 / 包芯线」专文（grep「缝纫线」仅 1 处顺带提及）：
  本文对比涤纶包芯线、涤纶短纤线、尼龙线、棉线、丝线五类材质，讲清 40/2、20/2、60/3 线号
  与 Z/S 捻向、针号匹配，按牛仔/针织/西装/羽绒防水/童装/箱包六类品类给出选线建议，
  并覆盖对色、色牢度、缩率同步与六项验收口径。
- flame-retardant-trims-guide  vs uniform-workwear-labeling-guide（只讲工作服标签耐久）、
  reflective-safety-trims-guide（反光条单列）、rainwear/outerwear（防水方向）、
  garment-trims-certifications（认证清单）；全站无「阻燃 / 防火辅料」专文
  （grep「阻燃」仅出现在 HS 编码、各国合规、牛仔三处顺带提及）：
  本文讲清辅料成为短板的四种典型失效，对比芳纶缝纫线、阻燃织带、阻燃魔术贴、
  阻燃反光条、芳纶商标洗水标、金属与塑料件六类方案，梳理垂直燃烧、熔滴、热收缩、
  工业洗后保持率、LOI 等测试口径，并覆盖 EN ISO 11611/11612、NFPA 2112、IEC 61482-2、
  EN 469、16 CFR 1615/1616 与标签追踪、认证路径与六项验收口径。
"""

ARTICLES = [
    dict(
        slug="sewing-thread-selection-guide.html",
        body="blog/_body_thread.html",
        title_zh="服装缝纫线选型指南：材质、线号与面料匹配怎么定 | TAGE",
        title_en="Sewing Thread Selection Guide: Fibre, Size and Fabric Matching | TAGE",
        title_ja="縫い糸の選定ガイド：素材・番手・生地との相性 | TAGE",
        title_ko="봉제사 선택 가이드: 소재·번수·원단 매칭 | TAGE",
        title_fr="Guide du fil de couture : fibre, numéro et tissu | TAGE",
        title_es="Guía del hilo de coser: fibra, número y tejido | TAGE",
        desc_zh="服装缝纫线选型指南：对比涤纶包芯线、涤纶短纤线、尼龙线、棉线与绣花线五类材质，讲清 40/2、20/2、60/3 线号写法与 Z/S 捻向、针号匹配，按牛仔、针织、西装、羽绒防水、童装与箱包六类给出选线建议，并附对色、色牢度、缩率同步与验收口径。东莞泰阁包装。",
        desc_en="Sewing thread guide: core-spun vs spun polyester, nylon, cotton and embroidery thread compared, how to read 40/2 and Z or S twist, matching thread to fabric.",
        desc_ja="縫い糸の選定ガイド。ポリエステル・コアスパン糸、スパン糸、ナイロン糸、綿糸、刺繍糸の比較、40/2 などの番手とZ撚・S撚の読み方、針番の整合、デニム・ニット・スーツ・ダウン・子供服・バッグ別の選定、色合わせと堅牢度、収縮率の同調、検収基準を解説。東莞泰閣包装。",
        desc_ko="봉제사 선택 가이드. 폴리에스터 코어스펀사, 스펀사, 나일론사, 면사, 자수사 비교와 40/2 번수·Z연·S연 읽는 법, 바늘 호수 매칭, 데님·니트·정장·다운·아동복·가방별 선정, 색상과 견뢰도, 수축률 일치, 검수 기준을 정리했습니다. 둥관 TAGE 패키징.",
        desc_fr="Guide du fil de couture : core-spun, filé polyester, nylon, coton et fil à broder comparés, lecture du 40/2 et des torsions Z et S, accord avec le tissu et critères de réception.",
        desc_es="Guía del hilo de coser: core-spun, poliéster hilado, nailon, algodón y seda comparados, lectura del 40/2 y de las torsiones Z y S, ajuste al tejido y criterios de recepción.",
        crumb_zh="缝纫线选型指南",
        crumb_en="Sewing Thread Guide",
        crumb_ja="縫い糸の選定ガイド",
        crumb_ko="봉제사 선택 가이드",
        crumb_fr="Guide du fil de couture",
        crumb_es="Guía del hilo de coser",
        h1_zh="服装缝纫线选型指南：材质、线号与面料匹配怎么定",
        h1_en="Sewing Thread Selection Guide: Fibre, Size and Fabric Matching",
        h1_ja="縫い糸の選定ガイド：素材・番手・生地との相性の決め方",
        h1_ko="봉제사 선택 가이드: 소재, 번수, 원단 매칭",
        h1_fr="Choisir son fil de couture : fibre, numéro et accord avec le tissu",
        h1_es="Elegir el hilo de coser: fibra, número y ajuste al tejido",
        tag_zh="辅料选型",
        tag_en="Trims Selection",
        tag_ja="副資材選定",
        tag_ko="부자재 선택",
        tag_fr="Choix d'accessoires",
        tag_es="Selección de accesorios",
        sum_zh="缝纫线成本占比不到 2%，却是断线、跳线、起皱、针孔渗水与洗后线迹发白的第一嫌疑。本文对比涤纶包芯线、涤纶短纤线、尼龙线、棉线与绣花线五类材质，讲清 40/2、20/2、60/3 线号写法与 Z/S 捻向、针号匹配，按牛仔、针织、西装、羽绒防水、童装与箱包六类品类给出选线建议，最后落到对色、色牢度、缩率同步与六项采购验收口径。",
        sum_en="Thread is under 2% of garment cost but the first suspect when stitches break, skip, pucker, leak through needle holes or turn pale in the wash. This guide compares five fibre types, explains 40/2 numbering and Z or S twist, matches needle size, recommends thread by category, and closes with colour, fastness, shrinkage and acceptance criteria.",
        sum_ja="縫い糸は原価の2%未満でありながら、糸切れ・目飛び・縫い縮み・針穴からの浸水・洗濯後の白化の第一容疑者です。5つの素材を比較し、40/2などの番手とZ撚・S撚、針番の整合、品種別の選定を整理し、最後に色合わせ・堅牢度・収縮率と6つの検収基準を示します。",
        sum_ko="봉제사는 원가의 2% 미만이지만 실 끊김, 뜀뜀, 당김 주름, 바늘구멍 누수, 세탁 후 실색 바램의 첫 번째 원인입니다. 다섯 소재를 비교하고 40/2 번수와 Z연·S연, 바늘 호수 매칭, 품목별 선정을 정리한 뒤 색상·견뢰도·수축률과 여섯 가지 검수 기준으로 마무리합니다.",
        sum_fr="Le fil pèse moins de 2 % du coût mais c'est le premier suspect en cas de rupture, point sauté, fronce, fuite par les trous d'aiguille ou couture qui blanchit. Ce guide compare cinq fibres, explique le 40/2 et les torsions Z et S, l'aiguille, le choix par catégorie, puis couleur, solidité, retrait et critères de réception.",
        sum_es="El hilo supone menos del 2 % del coste, pero es el primer sospechoso cuando la puntada rompe, salta, frunce, filtra por los agujeros o se aclara al lavar. Esta guía compara cinco fibras, explica el 40/2 y las torsiones Z y S, la aguja, la elección por categoría, y cierra con color, solidez, encogimiento y criterios de recepción.",
    ),
    dict(
        slug="flame-retardant-trims-guide.html",
        body="blog/_body_frtrims.html",
        title_zh="阻燃与防护服装辅料指南：缝纫线、织带、拉链与标签合规 | TAGE",
        title_en="Flame-Resistant Trims Guide: Thread, Tape, Zips and Labelling | TAGE",
        title_ja="難燃・防護衣料の副資材ガイド：縫い糸・テープ・ファスナー・表示 | TAGE",
        title_ko="난연·방호 의류 부자재 가이드: 봉제사·테이프·지퍼·표시 | TAGE",
        title_fr="Guide des accessoires ignifugés : fil, rubans, zips et étiquetage | TAGE",
        title_es="Guía de accesorios ignífugos: hilo, cintas, cremalleras y etiquetado | TAGE",
        desc_zh="阻燃与防护服装辅料指南：讲清为什么非阻燃的缝纫线、织带与标签会成为整件衣服的短板，对比芳纶缝纫线、阻燃织带、阻燃魔术贴、阻燃反光条、芳纶商标与金属件六类方案，梳理垂直燃烧、熔滴、热收缩、工业洗后保持率等测试口径，并覆盖 EN ISO 11612、NFPA 2112、IEC 61482-2 与标签追踪要点。东莞泰阁包装。",
        desc_en="FR trims guide: why non-FR thread, tape and labels become the weak link, aramid and FR polyester options, flame test figures, and EU and NFPA labelling duties.",
        desc_ja="難燃・防護衣料の副資材ガイド。非難燃の縫い糸やテープ、ラベルが弱点になる理由、アラミド糸・難燃テープ・難燃面ファスナー・難燃反射テープ・アラミドネーム・金属部品の比較、垂直燃焼・溶融滴下・熱収縮・工業洗濯後の保持率、EN ISO 11612・NFPA 2112・IEC 61482-2 と追跡表示の要点を解説。東莞泰閣包装。",
        desc_ko="난연·방호 의류 부자재 가이드. 난연이 아닌 봉제사·테이프·라벨이 약한 고리가 되는 이유, 아라미드사·난연 테이프·난연 벨크로·난연 반사 테이프·아라미드 라벨·금속 부품 비교, 수직 연소·용융 낙하·열수축·산업 세탁 후 유지율, EN ISO 11612·NFPA 2112·IEC 61482-2와 추적 표시 요점을 정리했습니다. 둥관 TAGE 패키징.",
        desc_fr="Guide des accessoires ignifugés : pourquoi un fil, un ruban ou une étiquette non FR devient le point faible, options aramide et polyester FR, essais flamme, étiquetage EU et NFPA.",
        desc_es="Guía de accesorios ignífugos: por qué un hilo, una cinta o una etiqueta no FR se vuelve el punto débil, opciones de aramida y poliéster FR, ensayos de llama y etiquetado UE y NFPA.",
        crumb_zh="阻燃辅料指南",
        crumb_en="FR Trims Guide",
        crumb_ja="難燃副資材ガイド",
        crumb_ko="난연 부자재 가이드",
        crumb_fr="Guide des accessoires ignifugés",
        crumb_es="Guía de accesorios ignífugos",
        h1_zh="阻燃与防护服装辅料指南：缝纫线、织带、拉链与标签合规",
        h1_en="Flame-Resistant Trims Guide: Thread, Tape, Zips and Labelling",
        h1_ja="難燃・防護衣料の副資材ガイド：縫い糸・テープ・ファスナー・表示",
        h1_ko="난연·방호 의류 부자재 가이드: 봉제사·테이프·지퍼·표시",
        h1_fr="Accessoires ignifugés : fil, rubans, zips et étiquetage",
        h1_es="Accesorios ignífugos: hilo, cintas, cremalleras y etiquetado",
        tag_zh="合规指南",
        tag_en="Compliance",
        tag_ja="コンプライアンス",
        tag_ko="컴플라이언스",
        tag_fr="Conformité",
        tag_es="Cumplimiento",
        sum_zh="防护服的面料达标并不等于成衣达标。非阻燃的缝纫线会熔断、普通松紧带会熔滴烫伤、金属拉链会导热、普通商标碳化脱落——本文把四种典型失效讲透，再对比芳纶缝纫线、阻燃织带、阻燃魔术贴、阻燃反光条、芳纶商标与金属塑料件六类方案，梳理垂直燃烧、熔滴、热收缩与工业洗后保持率的测试口径，并覆盖 EN ISO 11611/11612、NFPA 2112、IEC 61482-2、EN 469 与 16 CFR 1615/1616 的标签与认证要点，最后给出六项采购验收口径。",
        sum_en="A compliant fabric does not make a compliant garment. Non-FR thread melts and breaks, ordinary elastic drips and burns, metal zips conduct heat, standard labels char and fall off. This guide sets out those four failures, compares six trim families, explains vertical flame, melt-drip, heat shrinkage and retention after industrial laundering, and covers the labelling and certification points behind EN ISO 11611/11612, NFPA 2112, IEC 61482-2, EN 469 and 16 CFR 1615/1616.",
        sum_ja="生地が基準を満たしても、服全体が満たすことにはなりません。非難燃の縫い糸は溶断し、通常のゴムは溶融滴下してやけどを招き、金属ファスナーは熱を伝え、通常のラベルは炭化して脱落します。本記事はこの4つの典型的な弱点を示し、6種類の副資材を比較、垂直燃焼・溶融滴下・熱収縮・工業洗濯後の保持率の試験方法を整理し、EN ISO 11611/11612、NFPA 2112、IEC 61482-2、EN 469、16 CFR 1615/1616 の表示と認証、そして6つの検収基準まで扱います。",
        sum_ko="원단이 기준을 통과해도 옷 전체가 통과하는 것은 아닙니다. 난연이 아닌 봉제사는 녹아 끊어지고, 일반 고무밴드는 녹아 흘러 화상을 유발하며, 금속 지퍼는 열을 전달하고, 일반 라벨은 탄화되어 떨어집니다. 이 글은 네 가지 약점을 짚고 여섯 가지 부자재를 비교하며, 수직 연소·용융 낙하·열수축·산업 세탁 후 유지율 시험을 정리하고 EN ISO 11611/11612, NFPA 2112, IEC 61482-2, EN 469, 16 CFR 1615/1616의 표시와 인증, 여섯 가지 검수 기준까지 다룹니다.",
        sum_fr="Un tissu conforme ne fait pas un vêtement conforme. Un fil non FR fond et casse, un élastique ordinaire goutte et brûle, un zip métallique conduit la chaleur, une étiquette standard carbonise et tombe. Ce guide détaille ces quatre défaillances, compare six familles d'accessoires, explique combustion verticale, gouttes, retrait thermique et maintien après lavages industriels, puis l'étiquetage et la certification EN ISO 11611/11612, NFPA 2112, IEC 61482-2, EN 469 et 16 CFR 1615/1616.",
        sum_es="Un tejido conforme no hace una prenda conforme. Un hilo no FR funde y rompe, un elástico corriente gotea y quema, una cremallera metálica conduce el calor y una etiqueta estándar carboniza y se cae. Esta guía expone esos cuatro fallos, compara seis familias de accesorios, explica combustión vertical, goteo, encogimiento térmico y retención tras lavados industriales, y cubre el etiquetado y la certificación EN ISO 11611/11612, NFPA 2112, IEC 61482-2, EN 469 y 16 CFR 1615/1616.",
    ),
]
