#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-09-28 下午批次文章元数据（六语：zh-Hant 根 / en / ja / ko / fr / es）。

选题说明：任务主题池 30 个选题均已上线，本次为「辅料端可控的印面信息」与
「打样到大货之间的确认环节」两个方向扩展新选题。已核对 blog/ 全量文件、
en|ja|ko|fr|es/blog/ 与 sitemap.xml：
- 原产地标识（country of origin marking）此前只在国别合规文章里作为一个小节出现
  （clothing-label-compliance-usa 第 3 节、eu 第 3 节），没有专文；本篇聚焦辅料
  工厂能控制的三处印面（吊牌/洗水标/包装袋）的一致性、写法与工艺，与国别合规
  文章互补而非重复。
- 产前样（PP 样 / 首件确认）在现有 200+ 篇文章中无专文；garment-trims-sampling-process
  讲开发打样流程，trim-limit-sample-inspection-guide 讲界限样品，本篇讲「量产条件下
  的首件确认」这一中间环节，并在文中显式链接上述两篇做分工切分。
"""

ARTICLES = [
    dict(
        slug="clothing-origin-marking-guide.html",
        body="blog/_body_origin.html",
        title_zh="服裝原產地標識指南：吊牌、洗水標、包裝袋怎麼標 Made in China | TAGE",
        title_en="Country of Origin Marking for Clothing: Tags, Labels &amp; Bags | TAGE",
        title_ja="衣料品の原産地表示ガイド：タグ・洗濯表示ラベル・包装袋への記載 | TAGE",
        title_ko="의류 원산지 표시 가이드: 행택·세탁 표시 라벨·포장 봉투 표기 | TAGE",
        title_fr="Marquage d'origine des vêtements : étiquettes, labels et sacs | TAGE",
        title_es="Marcado de origen de la ropa: colgantes, etiquetas y bolsas | TAGE",
        desc_zh="原产地标识到底该印在吊牌、洗水标还是包装袋上？本文讲清原产地标识与优惠原产地证的区别、美国与欧盟、中东、拉美的标注差异，写法与工艺要点，并附下单前核对清单与五个常见印错。来自东莞泰阁包装。",
        desc_en="Where does country of origin belong: hang tag, care label or poly bag? Marking rules, wording and common mistakes across US, EU and Gulf markets.",
        desc_ja="原産地表示はタグ・洗濯表示ラベル・包装袋のどこに印字するのか。原産地表示と特恵原産地証明の違い、米国・EU・中東・中南米での要件差、表記と加工の要点、発注前チェックリストとよくある 5 つの印字ミスを解説します。東莞泰閣包装。",
        desc_ko="원산지 표시는 행택, 세탁 표시 라벨, 포장 봉투 중 어디에 인쇄할까요. 원산지 표시와 특혜 원산지 증명의 차이, 미국·EU·중동·중남미 요건 차이, 표기와 가공 요점, 발주 전 체크리스트와 흔한 다섯 가지 인쇄 오류를 정리합니다. 둥관 TAGE 패키징.",
        desc_fr="Où placer le marquage d'origine : étiquette suspendue, étiquette d'entretien ou sac ? Règles, formulation et erreurs fréquentes aux États-Unis, dans l'UE et au Moyen-Orient.",
        desc_es="¿Dónde va el marcado de origen: colgante, etiqueta de cuidado o bolsa? Reglas, redacción y errores frecuentes en EE. UU., la UE y Oriente Medio.",
        crumb_zh="原產地標識",
        crumb_en="Origin Marking",
        crumb_ja="原産地表示",
        crumb_ko="원산지 표시",
        crumb_fr="Marquage d'origine",
        crumb_es="Marcado de origen",
        h1_zh="服裝原產地標識指南：吊牌、洗水標、包裝袋三處怎麼標才一致",
        h1_en="Country of Origin Marking for Clothing: Getting Tag, Label and Bag to Agree",
        h1_ja="衣料品の原産地表示ガイド：タグ・洗濯表示ラベル・包装袋の三か所を揃える",
        h1_ko="의류 원산지 표시 가이드: 행택·세탁 표시 라벨·포장 봉투 세 곳을 맞추는 방법",
        h1_fr="Marquage d'origine des vêtements : aligner étiquette, label et sac",
        h1_es="Marcado de origen de la ropa: alinear colgante, etiqueta y bolsa",
        tag_zh="合规法规", tag_en="Compliance", tag_ja="コンプライアンス", tag_ko="컴플라이언스",
        tag_fr="Conformité", tag_es="Cumplimiento",
        sum_zh="买家一句「能不能印 Made in China」，实际要回答三个问题：写在哪、怎么写、谁在下单前核对。本文先分清原产地标识（标注义务）与优惠原产地证（关税优惠）这两条互不替代的通道，再把辅料工厂能控制的三处印面——吊牌、洗水标、包装袋——放在一张表里对照常见做法与注意点，随后梳理美国、欧盟与英国、中东、拉美、日韩以及电商平台的要求差异，给出标准写法与耐洗工艺要点，列出五个最常见的印错案例（三处不一致、漏改旧版、被裁切线切掉、语言不符、转口要求），最后附下单前的六项核对清单与一条省事做法。",
        sum_en="One buyer question — can you print Made in China — really asks three: where, how, and who checks. This article separates origin marking (a duty) from certificates of origin (a duty-rate track), then puts the three surfaces a trims factory controls — hang tag, care label and packaging bag — into one comparison table, reviews how the US, EU and UK, the Gulf, Latin America, Japan and Korea and the marketplaces differ, sets out wording and wash-durability points, and lists the five mistakes seen most often, from three surfaces disagreeing to text lost to the trim line. It closes with a six-point pre-order checklist.",
        sum_ja="バイヤーの「Made in China を入れられますか」という一言は、実は三つの問いです。どこに、どう書くか、誰が発注前に確認するか。本記事は原産地表示（申告義務）と特恵原産地証明（税率の別ルート）を切り分け、副資材工場が管理できる三つの面——タグ・洗濯表示ラベル・包装袋——を一つの表で比較します。さらに米国・EU と英国・中東・中南米・日韓・EC プラットフォームの要件差、標準的な表記と耐洗加工の要点、よくある 5 つの印字ミス、発注前の 6 項目チェックリストをまとめます。",
        sum_ko="바이어의 'Made in China를 넣을 수 있습니까'라는 한마디는 사실 세 가지 질문입니다. 어디에, 어떻게, 누가 발주 전에 확인하는가. 이 글은 원산지 표시(신고 의무)와 특혜 원산지 증명(세율 경로)을 구분하고, 부자재 공장이 관리하는 세 인쇄면—행택·세탁 표시 라벨·포장 봉투—을 한 표로 비교합니다. 이어서 미국·EU와 영국·중동·중남미·일본과 한국·전자상거래 플랫폼의 요건 차이, 표준 표기와 내세탁 가공 요점, 자주 발생하는 다섯 가지 오류, 발주 전 여섯 가지 체크리스트를 정리합니다.",
        sum_fr="La question d'un acheteur — pouvez-vous imprimer Made in China — en cache trois : où, comment, et qui vérifie. Cet article distingue le marquage d'origine (une obligation) du certificat d'origine (un circuit de droits), puis compare dans un seul tableau les trois surfaces maîtrisées par l'usine d'accessoires : étiquette suspendue, étiquette d'entretien et sac. Il détaille les différences entre États-Unis, UE et Royaume-Uni, Moyen-Orient, Amérique latine, Japon et Corée et places de marché, la formulation et la tenue au lavage, les cinq erreurs les plus fréquentes, et finit par une liste de six vérifications avant commande.",
        sum_es="Una pregunta del comprador —¿puedes imprimir Made in China?— esconde tres: dónde, cómo y quién lo revisa. Este artículo separa el marcado de origen (una obligación) del certificado de origen (otro circuito, el de aranceles), y compara en una tabla las tres superficies que controla la fábrica de accesorios: colgante, etiqueta de cuidado y bolsa. Repasa las diferencias entre EE. UU., UE y Reino Unido, Oriente Medio, Latinoamérica, Japón y Corea y las plataformas, fija la redacción y la resistencia al lavado, enumera los cinco errores más frecuentes y cierra con seis comprobaciones antes de pedir.",
    ),
    dict(
        slug="trim-pre-production-sample-guide.html",
        body="blog/_body_pp.html",
        title_zh="輔料產前樣（PP 樣）與首件確認指南：和打樣有什麼不同 | TAGE",
        title_en="Pre-Production Samples for Trims: PP Approval Without Delays | TAGE",
        title_ja="副資材の産前サンプル（PP）ガイド：開発サンプルとの違いと確認項目 | TAGE",
        title_ko="부자재 산전 샘플(PP) 가이드: 개발 샘플과의 차이와 확인 항목 | TAGE",
        title_fr="Échantillon de pré-production d'accessoires : valider sans retarder | TAGE",
        title_es="Muestra de preproducción de accesorios: validar sin retrasar | TAGE",
        desc_zh="打样确认了，大货为什么还是不一样？产前样（PP 样）正是补上这一环。本文讲清打样、产前样与大货首件的分工，产前样要确认的八项内容、允收边界与界限样品如何配合、签样留样与翻单一致性、时间安排，以及三个最常见的摩擦点。来自东莞泰阁包装。",
        desc_en="Why bulk drifts from the approved sample, and how a pre-production sample fixes it: eight checks, acceptance limits and a schedule that protects lead times.",
        desc_ja="サンプルを承認したのに量産品が違う理由と、産前サンプル（PP）による解決策を解説。確認すべき 8 項目、合格範囲の設定、署名承認と保管、納期を守るスケジュール、よくある摩擦を整理します。東莞泰閣包装。",
        desc_ko="샘플 승인 후에도 양산품이 달라지는 이유와 산전 샘플(PP)의 해결책을 정리합니다. 확인할 여덟 가지 항목, 허용 범위 설정, 서명 승인과 보관, 납기를 지키는 일정, 자주 발생하는 마찰을 다룹니다. 둥관 TAGE 패키징.",
        desc_fr="Pourquoi la série diffère de l'échantillon validé, et comment l'échantillon de pré-production règle la question : huit contrôles, limites et calendrier.",
        desc_es="Por qué el lote difiere de la muestra aprobada y cómo lo resuelve la muestra de preproducción: ocho controles, límites y calendario.",
        crumb_zh="產前樣與首件確認",
        crumb_en="Pre-Production Sample",
        crumb_ja="産前サンプルと初品確認",
        crumb_ko="산전 샘플과 초품 확인",
        crumb_fr="Échantillon de pré-production",
        crumb_es="Muestra de preproducción",
        h1_zh="輔料產前樣（PP 樣）與首件確認指南：大貨為什麼和打樣不一樣",
        h1_en="Pre-Production Samples for Trims: Why Bulk Differs From the Sample",
        h1_ja="副資材の産前サンプル（PP）ガイド：量産品がサンプルと違う理由",
        h1_ko="부자재 산전 샘플(PP) 가이드: 양산품이 샘플과 다른 이유",
        h1_fr="Échantillon de pré-production : pourquoi la série diffère de l'échantillon",
        h1_es="Muestra de preproducción: por qué el lote difiere de la muestra",
        tag_zh="采购流程", tag_en="Sourcing", tag_ja="調達プロセス", tag_ko="조달 절차",
        tag_fr="Achats", tag_es="Compras",
        sum_zh="打样回答「好不好看」，产前样回答「能不能稳定做出来」，大货首件回答「这一批有没有走样」——三件事常被混为一谈，于是就有了「确认过还是一样出问题」。本文用一张表切分三个阶段的职责与典型时间，把产前样要确认的八项（材质、颜色、印刷工艺、形态裁切、配件、耐洗牢度、包装、数量与配套）逐条说明，讲清允收边界如何与界限样品配合定下来，签样留样与翻单一致性怎么做，时间怎么排才不压大货，并给出寄了不看、标准含糊、多头确认这三个最常见摩擦的对策。",
        sum_en="The development sample answers does it look right, the pre-production sample answers can we repeat it, and the first off answers has this batch drifted — three questions often rolled into one, which is why approved orders still go wrong. A table splits the stages and their timing; eight items are then set out for PP approval (material, colour, printing effects, form and cutting, accessories, wash durability, packing, quantities and combination), followed by how to fix acceptance limits with limit samples, how to sign off and keep references for reorders, how to schedule it without delaying the run, and counters to the three frictions that recur most.",
        sum_ja="開発サンプルは「見栄えが良いか」、産前サンプルは「安定して作れるか」、量産初品は「このロットがずれていないか」に答えます。三つを混同すると「承認したのに問題が出る」が起きます。本記事は段階と時期を一表に整理し、産前サンプルで確認する 8 項目（素材・色・印刷加工・形状と断裁・付属品・耐洗堅牢度・包装・数量と組み合わせ）を解説。合格範囲と限界サンプルの併用、署名承認と追加注文の一貫性、量産を遅らせない日程、よくある三つの摩擦への対策を示します。",
        sum_ko="개발 샘플은 '보기 좋은가', 산전 샘플은 '안정적으로 만들 수 있는가', 양산 초품은 '이 로트가 흐트러지지 않았는가'에 답합니다. 세 가지를 혼동하면 '승인했는데 문제가 생기는' 상황이 됩니다. 이 글은 단계와 시점을 한 표로 정리하고, 산전 샘플에서 확인할 여덟 항목(소재·색상·인쇄 가공·형태와 재단·부속품·내세탁 견뢰도·포장·수량과 조합)을 설명합니다. 허용 범위와 한계 샘플의 병행, 서명 승인과 재주문 일관성, 양산을 늦추지 않는 일정, 자주 생기는 세 가지 마찰의 대응책을 제시합니다.",
        sum_fr="L'échantillon de développement répond à est-ce beau, le PP à peut-on le reproduire, la première pièce de série à ce lot a-t-il dérivé : trois questions souvent confondues, d'où les commandes validées qui dérapent. Un tableau sépare les étapes et leur calendrier ; huit points sont ensuite détaillés pour la validation du PP (matière, couleur, finitions, forme et découpe, accessoires, tenue au lavage, emballage, quantités et combinaison), puis la fixation des limites avec des échantillons de référence, la signature et la conservation des témoins, un planning qui ne retarde pas la série, et des réponses aux trois frictions les plus fréquentes.",
        sum_es="La muestra de desarrollo responde si se ve bien, la de preproducción si se puede repetir y la primera pieza si este lote se ha desviado: tres preguntas que suelen mezclarse, de ahí los pedidos aprobados que fallan. Una tabla separa las etapas y sus plazos; después se detallan los ocho puntos de la aprobación del PP (material, color, acabados, forma y corte, accesorios, resistencia al lavado, embalaje, cantidades y combinación), cómo fijar límites con muestras de referencia, cómo firmar y conservar patrones para reposiciones, cómo planificar sin retrasar el lote y respuestas a las tres fricciones más habituales.",
    ),
]
