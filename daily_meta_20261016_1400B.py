#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-16 本日第二批每日更新：2 篇新文章元数据（六语：zh-Hant 根 / en / ja / ko / fr / es）

选题说明（主题池 30 项连同既有扩展均已上线，本次为全站六语关键词扫描后的空白点扩展）：

- lingerie-bra-trims-guide.html：内衣与文胸辅料（五金 + 弹力件 + 结构件）。
  关键词扫描：「文胸」「钢圈」「罩杯」「钩扣」在 380+ 篇文章中仅 17 处命中，
  且全部是吊牌挂绳、衣架、纽扣页里的顺带提及；内衣标签页（underwear-label-guide）
  只讲标签本身，弹性辅料页（elastic-trims-selection-guide）讲的是通用松紧带，
  没有一篇处理「钩扣带、肩带调节、钢圈包裹、骨条端头」这条五金与结构件的选型路径。
  本篇落点：四个差别（薄料放大厚度重量、汗渍氯漂、毫米级公差、耗材属性）→
  闭合件三方案对照表（背扣带 / 前扣 / 无痕胶合）与加长背扣的缩率陷阱 →
  弹力件四项（肩带调节扣持力、围带回弹与残余变形、包边厚度、汗渍与氯水色牢度）→
  结构件（钢圈包裹与端头保护、骨条刺穿测试、衬垫与模杯、金属件镍释放）→
  标签标识四项（无感印标优先、双尺码体系、成分准确、柔软剂条件下验证）→
  打样验收四项（多次洗护循环、逐项量尺寸、真人试穿、留样与变更）。

- client-supplied-trim-materials-guide.html：客供料与指定物料管理。
  关键词扫描：「来料加工」「客供」「consigned」「client-supplied」在 380+ 篇文章中
  仅 2 处命中（均在版权/知识产权页顺带提及）；模具归属页只讲刀模所有权，
  数量公差页只讲超交短交，合同条款页不涉及来料责任边界，
  没有一篇处理「客户提供实物 / 指定品牌 / 客供模具」这三种情形下的责任、损耗与验收。
  本篇落点：三种情形对照表（责任差异）→ 来料验收当场做完的六件事 →
  损耗率与补料（按工艺定损耗、来料不足即停工、区分不良损耗与调试损耗、建议备料量）→
  专库隔离与双向批次追溯 → 结算与条款（不计价部分单列、余料退回、知识产权与保密）→
  打样与变更（小样先行、换来源需重新确认、留样记批号）。

事实口径：不写具体价格与损耗百分比数字（一律写「按工艺定」「报价阶段写明」）；
不写死合同条款号与法定罚则；镍释放、盐雾等一律写「按目标市场要求确认」。
"""

ARTICLES = [
    dict(
        slug="lingerie-bra-trims-guide.html",
        body="blog/_body_lingerie.html",
        title_zh="内衣与文胸辅料指南：钩扣、肩带弹力与钢圈包裹怎么选 | TAGE",
        title_en="Lingerie and Bra Trims Guide: Hooks, Strap Elastic and Underwire Casing | TAGE",
        title_ja="下着・ブラジャーの副資材ガイド：ホック・肩ひもゴム・ワイヤーカバーの選び方 | TAGE",
        title_ko="속옷·브래지어 부자재 가이드: 후크, 어깨끈 고무, 와이어 커버 선택법 | TAGE",
        title_fr="Guide des accessoires de lingerie : agrafes, élastiques et gaine d'armature | TAGE",
        title_es="Guía de accesorios de lencería: corchetes, elásticos y funda de aro | TAGE",
        desc_zh="内衣与文胸辅料怎么选？背扣带与前扣的取舍、无痕胶合工艺、肩带与围带弹力件的回弹与色牢度、钢圈包裹与骨条的端头处理、无感印标与双尺码体系，以及五次洗护循环的打样验收清单。来自东莞泰阁包装。",
        desc_en="Lingerie and bra trims guide: hook-and-eye versus front closures, bonded seams, strap and underband elastic recovery, underwire casing and tagless labels.",
        desc_ja="下着・ブラジャーの副資材ガイド。背中のホックテープと前ホックの使い分け、ボンディング、肩ひもとアンダーバンドの戻りと色堅牢度、ワイヤーカバーとボーンの端部処理、無感印字ラベルと二重サイズ表記まで整理します。東莞泰閣包装。",
        desc_ko="속옷·브래지어 부자재 가이드. 등 후크 테이프와 앞 후크의 선택, 본딩, 어깨끈과 밑둘레 밴드의 회복성과 색 견뢰도, 와이어 커버와 본 끝단 처리, 무감 인쇄 라벨과 이중 사이즈 표기까지 정리했습니다. 둥관 TAGE 패키징.",
        desc_fr="Guide des accessoires de lingerie : agrafes, assemblage collé, reprise des élastiques, gaine d'armature et marquage sans étiquette, avec tenue au lavage.",
        desc_es="Guía de accesorios de lencería: corchetes o cierre frontal, unión sin costura, recuperación de elásticos, funda de aro, marcado sin etiqueta y doble talla.",
        crumb_zh="内衣与文胸辅料",
        crumb_en="Lingerie and Bra Trims",
        crumb_ja="下着・ブラの副資材",
        crumb_ko="속옷·브래지어 부자재",
        crumb_fr="Accessoires de lingerie",
        crumb_es="Accesorios de lencería",
        h1_zh="内衣与文胸辅料指南：钩扣、肩带弹力与钢圈包裹怎么选",
        h1_en="Lingerie and Bra Trims Guide: Hooks, Strap Elastic and Underwire Casing",
        h1_ja="下着・ブラジャーの副資材ガイド：ホック、肩ひものゴム、ワイヤーカバー",
        h1_ko="속옷·브래지어 부자재 가이드: 후크, 어깨끈 고무, 와이어 커버",
        h1_fr="Guide des accessoires de lingerie : agrafes, élastiques et gaine d'armature",
        h1_es="Guía de accesorios de lencería: corchetes, elásticos y funda de aro",
        tag_zh="品类指南",
        tag_en="Category Guide",
        tag_ja="カテゴリガイド",
        tag_ko="카테고리 가이드",
        tag_fr="Guide par catégorie",
        tag_es="Guía por categoría",
        sum_zh="闭合件、弹力件、结构件与标签四组辅料的取舍要点，含背扣带与前扣对照表、肩带回弹与色牢度验证、钢圈包裹与骨条端头处理，以及五次洗护循环的验收清单。",
        sum_en="Closure, elastic, structural and labelling choices for lingerie, with a closure comparison table, strap recovery and fastness checks, underwire finishing and a five-wash acceptance list.",
        sum_ja="開閉部品・伸縮部品・構造部品・ラベルの4グループの選定要点。ホック比較表、肩ひもの戻りと堅牢度の検証、ワイヤーとボーンの端部処理、5回洗濯の検収リストを含みます。",
        sum_ko="여밈 부품, 신축 부품, 구조 부품, 라벨 네 그룹의 선택 요점. 후크 비교표, 어깨끈 회복성과 견뢰도 검증, 와이어·본 끝단 처리, 다섯 번 세탁 검수 리스트를 포함합니다.",
        sum_fr="Choix de fermetures, élastiques, pièces structurelles et marquage, avec tableau comparatif, contrôle de reprise et de solidité, finition d'armature et de baleines, et liste de réception après cinq lavages.",
        sum_es="Selección de cierres, elásticos, piezas estructurales y marcado, con tabla comparativa, control de recuperación y solidez, acabado de aros y ballenas, y lista de recepción tras cinco lavados.",
    ),
    dict(
        slug="client-supplied-trim-materials-guide.html",
        body="blog/_body_consigned.html",
        title_zh="服装辅料客供料管理指南：责任划分、损耗与来料验收 | TAGE",
        title_en="Client-Supplied Trim Materials: Responsibility, Loss Rates and Inspection | TAGE",
        title_ja="客先支給材と指定材料の副資材管理ガイド：責任分担・ロス率・受入検査 | TAGE",
        title_ko="고객 지급·지정 자재 부자재 관리 가이드: 책임 구분, 로스율, 입고 검사 | TAGE",
        title_fr="Matières fournies par le client : responsabilités, pertes et contrôle à réception | TAGE",
        title_es="Materiales aportados por el cliente: responsabilidades, mermas y recepción | TAGE",
        desc_zh="客供料与指定物料怎么管？客供实物、指定品牌与客供模具三种情形的责任划分，来料验收六项动作，损耗率与补料规则的约定方式，专库隔离与双向批次追溯，以及余料退回、开票与保密条款要点。来自东莞泰阁包装。",
        desc_en="Client-supplied and brand-specified trim materials: responsibility split, six incoming inspections, loss and replenishment rules, segregation and traceability.",
        desc_ja="客先支給材と指定材料の管理ガイド。現物支給・指定ブランド・支給金型の3ケースの責任分担、受入検査6項目、ロス率と追加支給のルール、専用保管と双方向トレース、余剰材の返却と請求の要点を整理します。東莞泰閣包装。",
        desc_ko="고객 지급·지정 자재 관리 가이드. 실물 지급, 지정 브랜드, 지급 금형 세 가지 상황의 책임 구분, 입고 검사 여섯 항목, 로스율과 보충 규칙, 전용 보관과 양방향 추적, 잔여 자재 반환과 청구 요점을 정리했습니다. 둥관 TAGE 패키징.",
        desc_fr="Matières fournies ou imposées : responsabilités, six contrôles à réception, pertes et réapprovisionnement, stockage séparé, traçabilité et retour du surplus.",
        desc_es="Materiales aportados o impuestos: responsabilidades, seis controles de recepción, mermas y reposición, almacenamiento separado y trazabilidad.",
        crumb_zh="客供料与指定物料",
        crumb_en="Client-Supplied Materials",
        crumb_ja="支給材と指定材料",
        crumb_ko="지급 자재와 지정 자재",
        crumb_fr="Matières fournies",
        crumb_es="Material aportado",
        h1_zh="服装辅料客供料与指定物料管理指南：责任、损耗与验收",
        h1_en="Client-Supplied and Brand-Specified Trim Materials Guide",
        h1_ja="客先支給材と指定材料の副資材管理ガイド",
        h1_ko="고객 지급·지정 자재 부자재 관리 가이드",
        h1_fr="Guide de gestion des matières fournies et imposées",
        h1_es="Guía de materiales aportados e impuestos",
        tag_zh="采购管理",
        tag_en="Sourcing Management",
        tag_ja="調達管理",
        tag_ko="구매 관리",
        tag_fr="Gestion des achats",
        tag_es="Gestión de compras",
        sum_zh="客供实物、指定物料与客供模具三种情形的责任划分，来料验收六项动作、损耗率与补料规则的约定方式、隔离存放与双向追溯，以及结算与保密条款要点。",
        sum_en="How responsibility differs across client-supplied goods, brand-specified material and client tooling, plus six incoming checks, loss and replenishment rules, segregation, traceability and settlement terms.",
        sum_ja="現物支給・指定材料・支給金型の3ケースで異なる責任分担、受入検査6項目、ロス率と追加支給の取り決め方、区分保管と双方向トレース、決済と守秘の条項要点。",
        sum_ko="실물 지급·지정 자재·지급 금형 세 가지 상황의 책임 구분, 입고 검사 여섯 항목, 로스율과 보충 규칙 합의 방식, 구분 보관과 양방향 추적, 결제와 비밀유지 조항 요점.",
        sum_fr="Responsabilités selon marchandise fournie, matière imposée ou outillage client, six contrôles à réception, règles de perte et de réapprovisionnement, séparation, traçabilité et clauses de règlement.",
        sum_es="Responsabilidades según material aportado, material impuesto o utillaje del cliente, seis controles de recepción, reglas de merma y reposición, separación, trazabilidad y cláusulas de liquidación.",
    ),
]
