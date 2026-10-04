#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-04 上午批次（11:00）每日更新：2 篇新文章元数据（六语：zh-Hant 根 / en / ja / ko / fr / es）

选题说明（主题池 30 项与历次扩展选题均已上线，本次沿「视觉安全类辅料」与「扣合类辅料」两个
尚未覆盖的品类扩展，已核对 blog/、en|ja|ko|fr|es/blog/ 与 sitemap.xml 无重复，并 grep 全站确认：

- reflective-safety-trims-guide  vs hang-tag-special-effects-guide（吊牌夜光油墨，属吊牌工艺）、
  heat-transfer-labels（热转印标工艺，含反光膜一句）、elastic-trims-selection-guide（弹性带类）、
  metal-trims-nickel-release-guide（金属五金）；全站无「反光辅料/安全高可见度辅料」专文：
  本文区分反光（回射）、荧光（高可见度）、夜光（蓄光）三套原理，给玻璃微珠 vs 微棱镜、
  缝制 vs 贴合的取舍、EN ISO 20471 / ANSI-ISEA 107 的面积与逆反射要求、洗涤后保持率、
  反光印花的线宽红线与童装安全测试要点。
- hook-and-loop-tape-guide      vs garment-buttons-fasteners-guide（纽扣/按扣/气眼铆钉）、
  zipper-selection-guide（拉链）、maternity-nursing-wear-trims-guide（哺乳口仅顺带提魔术贴）；
  全站无「魔术贴/粘扣带」专文：本文按勾毛结构、四类产品（标准/蘑菇头/射出勾/背胶）、
  尼龙 vs 涤纶、宽度与剥离剪切强度、开合循环次数、洗后失效与勾伤面料对策展开。
"""

ARTICLES = [
    dict(
        slug="reflective-safety-trims-guide.html",
        body="blog/_body_reflective.html",
        title_zh="反光辅料选用指南：反光条、反光印花与夜光标识怎么选 | TAGE",
        title_en="Reflective Trims Guide: Tape, Print &amp; Glow Marking | TAGE",
        title_ja="反射・蛍光・蓄光副資材ガイド：テープ・印刷・蓄光表示の選び方 | TAGE",
        title_ko="반사·형광·축광 부자재 가이드: 테이프, 인쇄, 축광 표시 | TAGE",
        title_fr="Guide des accessoires réfléchissants : ruban, impression et phosphorescent | TAGE",
        title_es="Guía de accesorios reflectantes: cinta, impresión y luminiscente | TAGE",
        desc_zh="反光辅料选用指南：讲清反光（回射）、荧光高可见度与夜光蓄光三类材料的原理差别，对比玻璃微珠与微棱镜、缝制与贴合、家洗与工业洗的取舍，给出逆反射系数、洗涤后保持率与童装安全测试要点，并附可直接使用的询价验收清单。东莞泰阁包装。",
        desc_en="Reflective trims guide: retro-reflective tape, fluorescent and glow materials, glass bead vs microprismatic, sew-on vs adhesive, wash retention and checks.",
        desc_ja="反射・蛍光・蓄光副資材の選定ガイド。再帰反射テープ、蛍光高視認素材、蓄光素材の原理の違い、ガラスビーズとマイクロプリズム、縫い付けと接着、家庭洗濯と工業洗濯の比較、再帰反射係数、洗濯後の保持率、子供服の安全試験、見積りチェックリストを掲載。東莞泰閣包装。",
        desc_ko="반사·형광·축광 부자재 선택 가이드. 재귀반사 테이프, 형광 고시인성 소재, 축광 소재의 원리 차이, 유리 비드와 마이크로프리즘, 봉제와 접착, 가정 세탁과 산업 세탁 비교, 재귀반사 계수, 세탁 후 유지율, 아동복 안전 시험, 견적 체크리스트를 담았습니다. 둥관 TAGE 패키징.",
        desc_fr="Guide des accessoires réfléchissants : ruban rétro-réfléchissant, matière fluorescente haute visibilité et phosphorescente, billes de verre ou microprismes, cousu ou adhésif, tenue au lavage et liste de demande.",
        desc_es="Guía de accesorios reflectantes: cinta retrorreflectante, material fluorescente de alta visibilidad y luminiscente, microesferas o microprismas, cosido o adhesivo, conservación al lavado y lista de consulta.",
        crumb_zh="反光辅料选用指南",
        crumb_en="Reflective Trims Guide",
        crumb_ja="反射副資材ガイド",
        crumb_ko="반사 부자재 가이드",
        crumb_fr="Guide des accessoires réfléchissants",
        crumb_es="Guía de accesorios reflectantes",
        h1_zh="反光辅料选用指南：反光条、反光印花与夜光标识怎么选",
        h1_en="Reflective Trims Guide: Tape, Reflective Print and Glow Marking",
        h1_ja="反射副資材の選定：反射テープ・反射印刷・蓄光表示の選び方",
        h1_ko="반사 부자재 선택: 반사 테이프, 반사 인쇄, 축광 표시",
        h1_fr="Choisir ses accessoires réfléchissants : ruban, impression et phosphorescent",
        h1_es="Elegir accesorios reflectantes: cinta, impresión y luminiscente",
        tag_zh="辅料选型",
        tag_en="Trims Selection",
        tag_ja="副資材選定",
        tag_ko="부자재 선택",
        tag_fr="Choix d'accessoires",
        tag_es="Selección de accesorios",
        sum_zh="反光、荧光与夜光常被当成一回事，其实是三套不同原理。本文对比玻璃微珠与微棱镜、缝制与贴合、家洗与工业洗的取舍，讲清反光印花的线宽红线，并给出逆反射系数、洗涤后保持率与童装安全测试要点。",
        sum_en="Reflective, fluorescent and glow-in-the-dark are three different principles. Compare glass bead with microprismatic, sew-on with adhesive and domestic with industrial washing, respect the minimum line width for reflective print, and cover wash retention and childrenswear testing.",
        sum_ja="反射・蛍光・蓄光は三つの異なる原理です。ガラスビーズとマイクロプリズム、縫い付けと接着、家庭洗濯と工業洗濯の比較、反射印刷の最小線幅、再帰反射係数、洗濯後の保持率、子供服の試験要点を整理します。",
        sum_ko="반사·형광·축광은 서로 다른 세 원리입니다. 유리 비드와 마이크로프리즘, 봉제와 접착, 가정 세탁과 산업 세탁 비교, 반사 인쇄의 최소 선폭, 재귀반사 계수, 세탁 후 유지율, 아동복 시험 요점을 정리했습니다.",
        sum_fr="Réfléchissant, fluorescent et phosphorescent sont trois principes distincts. Comparez billes de verre et microprismes, cousu et adhésif, lavage domestique et industriel ; respectez la largeur de trait minimale en impression et couvrez tenue au lavage et essais enfant.",
        sum_es="Reflectante, fluorescente y luminiscente son tres principios distintos. Compara microesferas y microprismas, cosido y adhesivo, lavado doméstico e industrial; respeta el ancho de línea mínimo en impresión y cubre conservación al lavado y ensayos infantiles.",
    ),
    dict(
        slug="hook-and-loop-tape-guide.html",
        body="blog/_body_hookloop.html",
        title_zh="魔术贴（粘扣带）选型指南：勾毛类型、材质与耐洗 | TAGE",
        title_en="Hook-and-Loop Tape Guide: Types, Materials &amp; Washability | TAGE",
        title_ja="面ファスナー選定ガイド：タイプ・素材・耐洗濯性 | TAGE",
        title_ko="벨크로(후크 앤 루프) 선택 가이드: 유형, 소재, 세탁성 | TAGE",
        title_fr="Guide du velcro : types, matières et tenue au lavage | TAGE",
        title_es="Guía del velcro: tipos, materiales y resistencia al lavado | TAGE",
        desc_zh="魔术贴（粘扣带）选型指南：对比标准勾毛、蘑菇头、射出勾与背胶型的强度、噪音与耐洗差异，讲清尼龙与涤纶、宽度与剥离剪切强度、开合循环次数，给出洗后失效、卷边、勾伤面料与背胶脱落的改法，并附询价验收清单。东莞泰阁包装。",
        desc_en="Hook-and-loop tape guide: types compared on strength, noise and washability, nylon vs polyester, width, peel and shear strength, plus a quote checklist.",
        desc_ja="面ファスナーの選定ガイド。標準・マッシュルーム・射出・粘着タイプを強度・騒音・耐洗濯性で比較し、ナイロンとポリエステル、幅、剥離と剪断強度、開閉回数を解説。係合低下・端の巻き・生地の引っかけ・粘着剥がれの対策と見積りチェックリストを掲載。東莞泰閣包装。",
        desc_ko="벨크로(후크 앤 루프) 선택 가이드. 표준·머시룸·사출·점착 타입을 강도·소음·세탁 내구성으로 비교하고 나일론과 폴리에스터, 폭, 박리·전단 강도, 개폐 횟수를 설명합니다. 결합력 저하·말림·원단 긁힘·점착 박리 대책과 견적 체크리스트를 담았습니다. 둥관 TAGE 패키징.",
        desc_fr="Guide du velcro : types standard, champignon, injecté et auto-adhésif comparés sur la résistance, le bruit et la tenue au lavage, nylon ou polyester, largeur, pelage et cisaillement, avec listes de devis.",
        desc_es="Guía del velcro: tipos estándar, seta, inyectado y autoadhesivo comparados en resistencia, ruido y lavado, nailon o poliéster, ancho, pelado y cizalladura, con lista de consulta y recepción.",
        crumb_zh="魔术贴选型指南",
        crumb_en="Hook-and-Loop Tape Guide",
        crumb_ja="面ファスナー選定ガイド",
        crumb_ko="벨크로 선택 가이드",
        crumb_fr="Guide du velcro",
        crumb_es="Guía del velcro",
        h1_zh="魔术贴（粘扣带）选型指南：勾毛类型、材质与耐洗",
        h1_en="Hook-and-Loop Tape: Types, Materials and Washability",
        h1_ja="面ファスナーの選定：タイプ・素材・耐洗濯性",
        h1_ko="벨크로 선택: 유형, 소재, 세탁 내구성",
        h1_fr="Velcro : types, matières et tenue au lavage",
        h1_es="Velcro: tipos, materiales y resistencia al lavado",
        tag_zh="辅料选型",
        tag_en="Trims Selection",
        tag_ja="副資材選定",
        tag_ko="부자재 선택",
        tag_fr="Choix d'accessoires",
        tag_es="Selección de accesorios",
        sum_zh="魔术贴选错，洗两次就失效。本文对比标准勾毛、蘑菇头、射出勾与背胶型的强度、噪音与耐洗差异，讲清尼龙与涤纶、宽度与剥离剪切强度、开合循环次数，并给出洗后失效、卷边、勾伤面料与背胶脱落的改法。",
        sum_en="Choose the wrong hook-and-loop tape and the grip dies after two washes. Compare standard, mushroom, moulded and self-adhesive types on strength, noise and washability, work through nylon versus polyester, width, peel and shear strength and cycle counts, then fix grip loss, curling and snagging.",
        sum_ja="面ファスナーを誤ると二回の洗濯で係合が死にます。標準・マッシュルーム・射出・粘着タイプを強度・騒音・耐洗濯性で比較し、ナイロンとポリエステル、幅、剥離と剪断強度、開閉回数を整理し、係合低下・端の巻き・生地の引っかけ・粘着剥がれの対策を示します。",
        sum_ko="벨크로를 잘못 고르면 두 번 세탁에 결합력이 죽습니다. 표준·머시룸·사출·점착 타입을 강도·소음·세탁 내구성으로 비교하고, 나일론과 폴리에스터, 폭, 박리·전단 강도, 개폐 횟수를 정리하며 결합력 저하·말림·원단 긁힘·점착 박리 대책을 제시합니다.",
        sum_fr="Mal choisi, le velcro perd son accroche en deux lavages. Comparez standard, champignon, injecté et auto-adhésif sur la résistance, le bruit et la tenue au lavage ; traitez nylon contre polyester, largeur, pelage et cisaillement, cycles, puis corrigez perte d'accroche, bords roulés et accroches.",
        sum_es="Un velcro mal elegido muere a los dos lavados. Compara estándar, seta, inyectado y autoadhesivo en resistencia, ruido y lavado; repasa nailon frente a poliéster, ancho, pelado y cizalladura, ciclos, y corrige pérdida de agarre, bordes enrollados y enganches.",
    ),
]
