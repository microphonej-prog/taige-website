#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-17 本日第一批（08:00）每日更新：2 篇新文章元数据（六语：zh-Hant 根 / en / ja / ko / fr / es）

选题说明（原 30 项主题池连同既有扩展均已上线，本次为全站关键词扫描后的空白点扩展）：

- gots-organic-cotton-label-guide.html：GOTS 有机棉认证与标签标注。
  关键词扫描：「GOTS / Global Organic Textile Standard / 有机棉认证 / 许可证号 / TC 交易证书」全站零命中
  （「有机棉」仅在 4 篇里作为选材场景顺带出现；证书类文章只有 OEKO-TEX、GRS、FSC 三条线）。
  既有文章分工：认证清单页讲「三张证书分别管什么」、认证标志页讲「标志怎么用不出错」、
  成分标注页讲纤维名称与百分比写法——没有一篇讲「GOTS 含量门槛、谁能挂标、TC 链条、吊牌与包装本身的材质限制」。
  本篇落点：GOTS 覆盖范围 → 两个标签等级（95% / 70%）对照表 → 许可证号与 TC 证书链 → 吊牌织唛油墨纸张要求
  → 与 OEKO-TEX、GRS 的分工 → 打样与出货文件六项核对。

- apparel-packaging-recyclability-guide.html：服装包装的可回收性设计与回收标识。
  关键词扫描：「可回收设计 / Recyclable by design / RecyClass / How2Recycle / OPRL / CEFLEX / 单一材质」
  中，RecyClass、How2Recycle、OPRL、CEFLEX 全站零命中；「单一材质、mono-material」只散见于 PPWR 页与纸袋页。
  既有文章分工：PPWR 页讲法规时间表与空置率，环保袋页讲可降解与再生料选材，
  覆膜页讲淋膜工艺——没有一篇从「设计决定可回收性」的角度讲结构、油墨、胶黏剂与回收标识体系。
  本篇落点：可回收性的两个前提（材质 + 当地设施）→ 四个设计杠杆 → 常见袋型可回收性对比表
  → RecyClass / How2Recycle / OPRL 的适用范围与授权要求 → 与 PPWR 的衔接准备 → 打样与验证清单。

事实口径（不编造）：不写具体价格；不写 RecyClass、CEFLEX 等体系的量化门槛（只写「以各自最新设计指南为准」）；
GOTS 的比例、材料清单与包装条款一律写「以现行标准文本与认证机构解释为准」；
PPWR 只写方向与「按材料给出时间表」，不写具体条文号与日期；各国回收流差异一律强调需按目标市场确认。
"""

ARTICLES = [
    dict(
        slug="gots-organic-cotton-label-guide.html",
        body="blog/_body_gots.html",
        title_zh="GOTS 有机棉认证与标签标注指南：含量门槛与许可证号 | TAGE",
        title_en="GOTS Organic Cotton Labelling Guide: Content Thresholds and Licence Numbers | TAGE",
        title_ja="GOTS オーガニックコットンのラベル表示ガイド：含有率基準とライセンス番号 | TAGE",
        title_ko="GOTS 유기농 코튼 라벨 가이드: 함유량 기준과 라이선스 번호 | TAGE",
        title_fr="Guide d'étiquetage GOTS : seuils de contenu et numéro de licence | TAGE",
        title_es="Guía de etiquetado GOTS: umbrales de contenido y número de licencia | TAGE",
        desc_zh="GOTS 有机棉标签怎么标才合规：两个标签等级与 95%、70% 的含量门槛，谁能挂 GOTS 标、许可证号怎么写，TC 交易证书链怎么走，吊牌织唛与包装本身的材质油墨限制，以及它与 OEKO-TEX、GRS 的分工。附打样六项核对清单。来自东莞泰阁包装。",
        desc_en="How to label GOTS certified organic cotton: the two label grades and 95% or 70% thresholds, licence numbers, the TC chain and material limits for tags.",
        desc_ja="GOTS 認証オーガニックコットンの表示ガイド。2つのラベル等級と95%・70%の基準、ライセンス番号、TC 証明書チェーン、タグと包装の素材制限を整理します。東莞泰閣包装。",
        desc_ko="GOTS 인증 유기농 코튼 라벨 가이드. 두 라벨 등급과 95%·70% 기준, 라이선스 번호, TC 체인, 행택과 포장의 소재 제한을 정리했습니다. 둥관 TAGE 패키징.",
        desc_fr="Étiqueter un produit GOTS : les deux grades et les seuils de 95 % et 70 %, le numéro de licence, la chaîne des TC et les limites de matière des étiquettes.",
        desc_es="Etiquetar un producto GOTS: los dos grados y los umbrales del 95 % y 70 %, el número de licencia, la cadena de TC y los límites de material de las etiquetas.",
        crumb_zh="GOTS 有机棉标签",
        crumb_en="GOTS Organic Cotton Labels",
        crumb_ja="GOTS オーガニック表示",
        crumb_ko="GOTS 유기농 라벨",
        crumb_fr="Étiquetage GOTS",
        crumb_es="Etiquetado GOTS",
        h1_zh="GOTS 有机棉认证与标签标注指南：含量门槛与许可证号",
        h1_en="GOTS Organic Cotton Labelling Guide: Content Thresholds and Licence Numbers",
        h1_ja="GOTS オーガニックコットンのラベル表示ガイド：含有率基準とライセンス番号",
        h1_ko="GOTS 유기농 코튼 라벨 가이드: 함유량 기준과 라이선스 번호",
        h1_fr="Guide d'étiquetage GOTS : seuils de contenu et numéro de licence",
        h1_es="Guía de etiquetado GOTS: umbrales de contenido y número de licencia",
        tag_zh="认证与合规",
        tag_en="Certification",
        tag_ja="認証と適合",
        tag_ko="인증과 적합성",
        tag_fr="Certification",
        tag_es="Certificación",
        sum_zh="GOTS 覆盖棉田到吊牌的整条链，标签端也有硬性规则：95% 与 70% 两个等级怎么区分，许可证号与 TC 交易证书由谁提供，吊牌、织唛、油墨与包装本身受哪些材质限制，以及它和 OEKO-TEX、GRS 各自管什么。",
        sum_en="GOTS covers the whole chain from field to hang tag and imposes rules on the label too: how the 95% and 70% grades differ, who provides the licence number and the TC, which material limits apply to tags, inks and packaging, and what it does not cover.",
        sum_ja="GOTS は綿花畑からハングタグまでの全工程を対象とし、ラベル側にも規則があります。95% と 70% の等級の違い、ライセンス番号と TC 証明書を誰が発行するか、タグ・インキ・包装の素材制限、OEKO-TEX や GRS との役割分担を整理します。",
        sum_ko="GOTS는 면밭에서 행택까지 전 과정을 대상으로 하며 라벨 규칙도 정합니다. 95%와 70% 등급의 차이, 라이선스 번호와 TC 증명서 발급 주체, 행택·잉크·포장의 소재 제한, OEKO-TEX와 GRS의 역할 구분을 정리했습니다.",
        sum_fr="GOTS couvre toute la chaîne, du champ à l'étiquette, et impose des règles au moment de l'étiquetage : différence entre les grades 95 % et 70 %, qui fournit la licence et le TC, limites de matière pour étiquettes, encres et emballages, et partage avec OEKO-TEX et GRS.",
        sum_es="GOTS cubre toda la cadena, del campo al colgante, e impone reglas al etiquetar: diferencia entre los grados del 95 % y 70 %, quién aporta la licencia y el TC, límites de material de etiquetas, tintas y envases, y reparto con OEKO-TEX y GRS.",
    ),
    dict(
        slug="apparel-packaging-recyclability-guide.html",
        body="blog/_body_recycle.html",
        title_zh="服装包装可回收性设计指南：单材质、回收标识与 PPWR | TAGE",
        title_en="Recyclable Garment Packaging Design: Mono-Material, Recycling Labels, PPWR | TAGE",
        title_ja="衣料包装のリサイクル設計ガイド：単一素材・リサイクル表示・PPWR | TAGE",
        title_ko="의류 포장 재활용 설계 가이드: 단일 소재, 재활용 표시, PPWR | TAGE",
        title_fr="Conception d'emballage textile recyclable : monomatériau, logos de tri, PPWR | TAGE",
        title_es="Diseño de envases textiles reciclables: monomaterial, etiquetas de reciclaje, PPWR | TAGE",
        desc_zh="服装包装的可回收性不是一句声明：它取决于材质与目标市场的回收设施。讲清判断逻辑、单材质与去复合等四个设计杠杆、常见袋型可回收性对比、RecyClass／How2Recycle／OPRL 回收标识怎么用，以及为欧盟 PPWR 提前做哪些准备。来自东莞泰阁包装。",
        desc_en="Recyclable packaging is judged by material and local collection, not by a claim: four design levers, bag format comparisons, recycling labels and EU PPWR.",
        desc_ja="衣料包装のリサイクル性は文言ではなく素材と回収体制で決まります。判断の考え方、4つの設計レバー、袋形状の比較、RecyClass などの表示スキーム、PPWR への備えを整理します。東莞泰閣包装。",
        desc_ko="의류 포장 재활용성은 문구가 아니라 소재와 회수 인프라로 결정됩니다. 판단 기준, 네 가지 설계 레버, 봉투 형태 비교, RecyClass 등 표시 제도, PPWR 대비를 정리했습니다. 둥관 TAGE 패키징.",
        desc_fr="La recyclabilité d'un emballage textile dépend de la matière et de la collecte locale : quatre leviers de conception, comparaison des formats, systèmes de tri et préparation au PPWR.",
        desc_es="La reciclabilidad del envase textil depende del material y de la recogida local: cuatro palancas de diseño, comparación de formatos, sistemas de etiquetado y preparación del PPWR.",
        crumb_zh="包装可回收性设计",
        crumb_en="Recyclable Packaging Design",
        crumb_ja="包装のリサイクル設計",
        crumb_ko="포장 재활용 설계",
        crumb_fr="Conception recyclable",
        crumb_es="Diseño reciclable",
        h1_zh="服装包装可回收性设计指南：单材质、回收标识与 PPWR",
        h1_en="Recyclable Garment Packaging Design: Mono-Material, Recycling Labels and PPWR",
        h1_ja="衣料包装のリサイクル設計ガイド：単一素材・リサイクル表示・PPWR",
        h1_ko="의류 포장 재활용 설계 가이드: 단일 소재, 재활용 표시, PPWR",
        h1_fr="Conception d'emballage textile recyclable : monomatériau, logos de tri et PPWR",
        h1_es="Diseño de envases textiles reciclables: monomaterial, etiquetas de reciclaje y PPWR",
        tag_zh="环保与法规",
        tag_en="Sustainability",
        tag_ja="環境と法規",
        tag_ko="환경과 규제",
        tag_fr="Environnement",
        tag_es="Sostenibilidad",
        sum_zh="把「可回收」落到设计上：材质与当地回收设施两条前提、单材质与去复合等四个杠杆、常见服装包装的可回收性对比表、RecyClass 与 How2Recycle 等标识体系的适用范围，以及与欧盟 PPWR 的衔接与验证清单。",
        sum_en="Turning recyclable into a design decision: material plus local infrastructure, four levers from mono-material to separability, a comparison of common garment packaging, the recycling label schemes and PPWR preparation.",
        sum_ja="「リサイクル可能」を設計の話に落とし込みます。素材と現地回収体制という2つの前提、単一素材から分離性までの4つのレバー、代表的な衣料包装の比較表、RecyClass などの表示スキーム、PPWR への備えと検証項目を整理します。",
        sum_ko="'재활용 가능'을 설계 문제로 다룹니다. 소재와 현지 회수 인프라라는 두 전제, 단일 소재부터 분리성까지 네 가지 레버, 대표 의류 포장 비교표, RecyClass 등 표시 제도, PPWR 대비와 검증 항목을 정리했습니다.",
        sum_fr="Faire de la recyclabilité un choix de conception : matière et collecte locale, quatre leviers du monomatériau à la séparabilité, comparaison des emballages courants, systèmes de tri et préparation au PPWR.",
        sum_es="Convertir la reciclabilidad en una decisión de diseño: material y recogida local, cuatro palancas del monomaterial a la separabilidad, comparación de envases habituales, sistemas de etiquetado y preparación del PPWR.",
    ),
]
