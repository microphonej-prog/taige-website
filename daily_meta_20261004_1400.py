#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-04 下午批次（14:00）每日更新：2 篇新文章元数据（六语：zh-Hant 根 / en / ja / ko / fr / es）

选题说明（主题池 30 项与历次扩展选题均已上线，本次沿「绳带类辅料」与「花边类辅料」两个
尚未覆盖的品类扩展，已核对 blog/、en|ja|ko|fr|es/blog/ 与 sitemap.xml 无重复，并 grep 全站确认：）

- garment-drawcord-guide  vs elastic-trims-selection-guide（松紧带/罗纹/包边带/弹力织带）、
  hook-and-loop-tape-guide（魔术贴）、outerwear-down-jacket-trims-guide（羽绒服辅料，仅顺带提抽绳）、
  hang-tag-* 系列（吊牌与吊绳）；全站无「抽绳/绳带（drawcord）」专文：
  本文区分圆绳、扁带、编织绳、弹力绳四类结构，给涤纶/棉/尼龙/rPET 的取舍、金属与塑料绳头、
  锁眼与鸡眼、通道宽度与固定绊的配合口径，并给出 EN 14682 与 ASTM F1816 的儿童抽绳强制要求。
- lace-trimming-guide     vs woven-label-*（织唛/主唛）、self-adhesive-woven-labels（背胶织唛）、
  leather-patch-labels（皮标）、underwear-label-guide（内衣标签，含缎面织唛）、
  bridal-eveningwear-trims-guide（婚纱晚装辅料，以标签吊牌为主）；全站无「花边/蕾丝」专文：
  本文对比经编（拉舍尔）、水溶（绣花）、网布刺绣、针织罗纹与钩编五类结构，讲清涤纶/棉/尼龙/
  氨纶/真丝的取舍、按用途倒推选型、蕾丝成分对洗水标标示的影响，以及幅宽、花型循环、色牢度、
  缩水与起球的采购验收口径。
"""

ARTICLES = [
    dict(
        slug="garment-drawcord-guide.html",
        body="blog/_body_drawcord.html",
        title_zh="服装抽绳选型指南：绳体结构、绳头与儿童安全要求 | TAGE",
        title_en="Drawcord Guide: Cord Types, Ends &amp; Child Safety Rules | TAGE",
        title_ja="ドローコード選定ガイド：構造・エンド金具・子供服の安全規制 | TAGE",
        title_ko="드로코드 선택 가이드: 구조, 끝 마감, 아동복 안전 규정 | TAGE",
        title_fr="Guide des cordons : structures, embouts et sécurité enfant | TAGE",
        title_es="Guía de cordones: estructuras, remates y seguridad infantil | TAGE",
        desc_zh="服装抽绳选型指南：对比圆绳、扁带、编织绳与弹力绳的手感与用途，讲清涤纶、棉、尼龙与再生涤纶的取舍，拆解金属与塑料绳头、锁眼鸡眼与通道宽度的配合口径，并给出 EN 14682 与 ASTM F1816 的儿童抽绳强制要求及询价清单。东莞泰阁包装。",
        desc_en="Drawcord guide: round, flat, braided and elastic cords, materials, metal vs plastic ends, eyelets, casing widths, child-safety rules and a quote checklist.",
        desc_ja="ドローコード選定ガイド。丸コード・平テープ・編みコード・ゴムコードの違い、ポリエステル・綿・ナイロン・再生ポリエステルの選び方、金属と樹脂のエンド、ハトメと通し幅、EN 14682 と ASTM F1816 の子供服規制、見積りチェックリストを掲載。東莞泰閣包装。",
        desc_ko="드로코드 선택 가이드. 원형 코드, 평직 테이프, 편조 코드, 신축 코드의 차이와 폴리에스터·면·나일론·재생 폴리에스터 선택, 금속과 플라스틱 엔드, 아일릿과 통로 폭, EN 14682와 ASTM F1816 아동복 규정, 견적 체크리스트를 담았습니다. 둥관 TAGE 패키징.",
        desc_fr="Guide des cordons : rond, plat, tressé et élastique, matières, embouts métal ou plastique, oeillets, largeur de coulisse, sécurité enfant et liste de demande.",
        desc_es="Guía de cordones: redondo, plano, trenzado y elástico, materiales, remates metálicos o plásticos, ojales, ancho del túnel, seguridad infantil y lista de consulta.",
        crumb_zh="服装抽绳选型指南",
        crumb_en="Drawcord Guide",
        crumb_ja="ドローコード選定ガイド",
        crumb_ko="드로코드 선택 가이드",
        crumb_fr="Guide des cordons",
        crumb_es="Guía de cordones",
        h1_zh="服装抽绳选型指南：绳体结构、绳头与儿童安全要求",
        h1_en="Drawcord Guide: Cord Types, Ends and Child Safety Rules",
        h1_ja="ドローコードの選定：構造・エンド金具・子供服の安全規制",
        h1_ko="드로코드 선택: 구조, 끝 마감, 아동복 안전 규정",
        h1_fr="Choisir ses cordons : structures, embouts et sécurité enfant",
        h1_es="Elegir cordones: estructuras, remates y seguridad infantil",
        tag_zh="辅料选型",
        tag_en="Trims Selection",
        tag_ja="副資材選定",
        tag_ko="부자재 선택",
        tag_fr="Choix d'accessoires",
        tag_es="Selección de accesorios",
        sum_zh="抽绳由绳体、绳头与穿绳结构三部分组成，任何一处选错都会滑脱、断裂或洗后缩水。本文对比圆绳、扁带、编织绳与弹力绳，讲清涤纶、棉、尼龙与再生涤纶的取舍，拆解金属与塑料绳头、锁眼鸡眼与通道宽度的配合口径，并给出 EN 14682 与 ASTM F1816 的儿童抽绳强制要求。",
        sum_en="A drawcord is the cord, the end and the structure it passes through — get any one wrong and it slips, breaks or shrinks. Compare round, flat, braided and elastic cords, work through polyester, cotton, nylon and rPET, then cover cord ends, eyelets, casing width and the mandatory child-safety rules.",
        sum_ja="ドローコードはコード本体・エンド金具・通し構造の三つでできており、どれか一つを間違えると抜け・破断・洗濯後の縮みが起こります。丸コード・平テープ・編みコード・ゴムコードを比較し、ポリエステル・綿・ナイロン・再生ポリエステルの選び方、エンド金具、ハトメ、通し幅、子供服の安全規制まで整理します。",
        sum_ko="드로코드는 코드 본체, 끝 마감, 통과 구조의 세 부분으로 이루어지며 하나라도 잘못 고르면 빠짐, 파손, 세탁 후 수축이 생깁니다. 원형 코드, 평직 테이프, 편조 코드, 신축 코드를 비교하고 폴리에스터·면·나일론·재생 폴리에스터 선택, 엔드 마감, 아일릿, 통로 폭, 아동복 안전 규정까지 다룹니다.",
        sum_fr="Un cordon, c'est le cordon, l'embout et la structure qui le guide : une erreur et il glisse, casse ou se rétracte. Comparez rond, plat, tressé et élastique, passez en revue polyester, coton, nylon et rPET, puis embouts, oeillets, largeur de coulisse et règles enfant obligatoires.",
        sum_es="Un cordón es el cordón, el remate y la estructura por la que pasa: si falla uno, se desliza, se rompe o encoge. Compara redondo, plano, trenzado y elástico, repasa poliéster, algodón, nailon y rPET, y cubre remates, ojales, ancho del túnel y las normas infantiles obligatorias.",
    ),
    dict(
        slug="lace-trimming-guide.html",
        body="blog/_body_lace.html",
        title_zh="服装花边与蕾丝选型指南：结构、材质与验收要点 | TAGE",
        title_en="Lace &amp; Trim Guide: Constructions, Materials &amp; QC | TAGE",
        title_ja="レース・花辺の選定ガイド：構造・素材・検収の要点 | TAGE",
        title_ko="레이스·장식 테이프 선택 가이드: 구조, 소재, 검수 요점 | TAGE",
        title_fr="Guide dentelle et galon : structures, matières et contrôle | TAGE",
        title_es="Guía de encaje y galón: estructuras, materiales y control | TAGE",
        desc_zh="服装花边与蕾丝选型指南：对比经编、水溶、网布刺绣、针织罗纹与钩编五种结构的用途差异，讲清涤纶、棉、尼龙、氨纶与真丝的取舍，说明蕾丝成分对洗水标标注的影响，并给出幅宽、花型循环、色牢度、缩水与起球等采购验收要点。东莞泰阁包装。",
        desc_en="Lace and trim guide: warp-knit, water-soluble, embroidered, rib and crochet constructions, fibre choices, care-label content, plus a sampling and QC checklist.",
        desc_ja="レース・花辺の選定ガイド。経編・水溶性・刺しゅう・ニットリブ・かぎ編みの構造比較、ポリエステル・綿・ナイロン・ポリウレタン・シルクの選び方、組成表示への影響、幅・柄リピート・堅牢度・収縮・毛玉の検収要点を掲載。東莞泰閣包装。",
        desc_ko="레이스·장식 테이프 선택 가이드. 경편·수용성·자수·니트 리브·코바늘 구조 비교와 폴리에스터·면·나일론·스판덱스·실크 선택, 혼용률 표시 영향, 폭·패턴 리핏·견뢰도·수축·보풀 검수 요점을 담았습니다. 둥관 TAGE 패키징.",
        desc_fr="Guide dentelle et galon : tricot chaîne, hydrosoluble, brodée, côtes et crochet, choix de matière, contenu de l'étiquette d'entretien et liste de contrôle à réception.",
        desc_es="Guía de encaje y galón: urdimbre, hidrosoluble, bordado, canalé y ganchillo, elección de material, contenido de la etiqueta de cuidado y lista de verificación.",
        crumb_zh="花边与蕾丝选型指南",
        crumb_en="Lace and Trim Guide",
        crumb_ja="レース・花辺ガイド",
        crumb_ko="레이스·장식 테이프 가이드",
        crumb_fr="Guide dentelle et galon",
        crumb_es="Guía de encaje y galón",
        h1_zh="服装花边与蕾丝选型指南：结构、材质与验收要点",
        h1_en="Lace and Trim Guide: Constructions, Materials and Quality Control",
        h1_ja="レース・花辺の選定：構造・素材・検収の要点",
        h1_ko="레이스·장식 테이프 선택: 구조, 소재, 검수 요점",
        h1_fr="Choisir dentelle et galon : structures, matières et contrôle",
        h1_es="Elegir encaje y galón: estructuras, materiales y control",
        tag_zh="辅料选型",
        tag_en="Trims Selection",
        tag_ja="副資材選定",
        tag_ko="부자재 선택",
        tag_fr="Choix d'accessoires",
        tag_es="Selección de accesorios",
        sum_zh="蕾丝选错，洗一次就卷边、勾丝、变形。本文对比经编、水溶、网布刺绣、针织罗纹与钩编五种结构，讲清涤纶、棉、尼龙、氨纶与真丝的取舍，说明蕾丝成分对洗水标的标注影响，并给出幅宽、花型循环、色牢度、缩水与起球等采购验收口径。",
        sum_en="Choose the wrong lace and it curls, snags and distorts at the first wash. Compare warp-knit, water-soluble, embroidered, rib and crochet constructions, weigh polyester against cotton, nylon, spandex and silk, see how lace changes care-label content, then set width, pattern repeat, fastness and shrinkage criteria.",
        sum_ja="レースを間違えると一度の洗濯でカール・糸引き・型崩れが起こります。経編・水溶性・刺しゅう・ニットリブ・かぎ編みの構造を比較し、ポリエステルと綿・ナイロン・ポリウレタン・シルクの選び方を整理し、組成表示への影響と、幅・柄リピート・堅牢度・収縮・毛玉の検収基準を示します。",
        sum_ko="레이스를 잘못 고르면 한 번 세탁에 말림, 올 나감, 변형이 생깁니다. 경편, 수용성, 자수, 니트 리브, 코바늘 구조를 비교하고 폴리에스터와 면·나일론·스판덱스·실크의 선택을 정리하며 혼용률 표시에 미치는 영향과 폭, 패턴 리핏, 견뢰도, 수축, 보풀 검수 기준을 제시합니다.",
        sum_fr="Mal choisie, la dentelle s'enroule, s'accroche et se déforme dès le premier lavage. Comparez tricot chaîne, hydrosoluble, brodée, côtes et crochet, arbitrez polyester, coton, nylon, élasthanne et soie, mesurez l'impact sur l'étiquette, puis fixez largeur, raccord, solidité et retrait.",
        sum_es="Un encaje mal elegido se enrolla, se engancha y se deforma al primer lavado. Compara urdimbre, hidrosoluble, bordado, canalé y ganchillo, pondera poliéster, algodón, nailon, elastano y seda, revisa el impacto en la etiqueta y fija ancho, rapport, solidez y encogimiento.",
    ),
]
