#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-08 晚批次（20:00）每日更新：2 篇新文章元数据（六语：zh-Hant 根 / en / ja / ko / fr / es）

选题说明（主题池 30 项与既有扩展均已上线，本次沿两个尚未独立成文的方向扩展，
已核对 blog/、en|ja|ko|fr|es/blog/ 与 sitemap.xml 无重复 slug，并 grep 全站确认关键词覆盖情况：

- vacuum-compression-apparel-packaging：全站 grep「真空压缩 / vacuum compression / compression sous vide」
  仅命中 knitwear-sweater-trims-guide、outerwear-down-jacket-trims-guide、shirt-blouse-trims-guide
  三处「少压缩 / 慎用真空压缩 / 避免过度真空压缩」的注意事项，均为一句话提醒，无一篇讲压缩方式、
  压缩率、气阀与封口参数、堆码承压与回弹期的独立文章。本文把压缩方式对比、可压与不可压品类、
  设备参数与残余体积比、袋材选择、吊牌与皮标的连带损伤、到仓回弹时间与验收口径讲完整。

- stone-paper-hang-tags-guide：全站 grep「石头纸 / 矿物纸 / 石灰石 / stone paper / mineral paper」
  0 处；eco-friendly-hangtag-materials 讲的是再生牛皮纸、棉纸、种子纸与竹纤维纸，
  不含矿物纸（碳酸钙＋树脂复合）这一材质。本文讲清成分与密度、耐水耐撕与折痕开裂的机理、
  与铜版纸和 PP 合成纸的三方对比、印刷与后道工艺的能做与禁忌、打孔与鸡眼加工要点、
  适用与不适用场景，以及环保话术与 FSC / 可回收声明的合规边界。
"""

ARTICLES = [
    dict(
        slug="vacuum-compression-apparel-packaging.html",
        body="blog/_body_vacuum.html",
        title_zh="服装真空压缩包装指南：羽绒、毛衫与家纺 | TAGE",
        title_en="Vacuum Compression Packaging for Apparel: Down and Knitwear | TAGE",
        title_ja="衣料品の真空圧縮包装ガイド：ダウン・ニット・ホームテキスタイル | TAGE",
        title_ko="의류 진공 압축 포장 가이드: 다운·니트·홈텍스타일 | TAGE",
        title_fr="Emballage compressé sous vide pour vêtements : duvet et maille | TAGE",
        title_es="Embalaje comprimido al vacío para prendas: plumón y punto | TAGE",
        desc_zh="服装真空压缩包装指南：一张表分清真空袋、腔体机、卷压与外箱适配四种方式的压缩率与风险，讲清羽绒、毛衫、衬衫与涂层功能面料的可压上限，气阀与封口参数、吊牌与皮标在压缩下的损伤、堆码承压与到仓回弹时间，附可直接抄进询价单的验收口径。来自东莞泰阁包装。",
        desc_en="Vacuum compression packaging for apparel: down, knitwear and home textiles — compression methods, ratios, bag and valve choice, tag damage and recovery times.",
        desc_ja="衣料品の真空圧縮包装ガイド。真空袋・チャンバー機・巻き圧縮・外箱適合の4方式と圧縮率、ダウン・ニット・シャツ・コーティング生地の圧縮上限、弁とシールのパラメータ、タグや革パッチの損傷、積み重ね耐圧と入庫後の復元時間、見積書にそのまま使える検収基準を解説。東莞泰閣包装。",
        desc_ko="의류 진공 압축 포장 가이드. 진공백·챔버기·롤 압축·외부 상자 맞춤 네 방식과 압축률, 다운·니트·셔츠·코팅 원단의 압축 상한, 밸브와 실링 파라미터, 행택과 가죽 패치 손상, 적재 내압과 입고 후 복원 시간, 견적서에 바로 쓸 수 있는 검수 기준을 정리했습니다. 둥관 TAGE 패키징.",
        desc_fr="Emballage compressé sous vide pour vêtements : quatre méthodes et leurs taux, limites pour duvet, maille, chemises et tissus enduits, réglages de valve et de soudure, dégâts sur étiquettes et cuir, reprise de volume.",
        desc_es="Embalaje comprimido al vacío para prendas: cuatro métodos y sus tasas, límites para plumón, punto, camisas y tejidos con recubrimiento, ajustes de válvula y sellado, daños en etiquetas y piel, recuperación de volumen.",
        crumb_zh="服装真空压缩包装",
        crumb_en="Vacuum Compression Packaging",
        crumb_ja="真空圧縮包装",
        crumb_ko="진공 압축 포장",
        crumb_fr="Emballage compressé sous vide",
        crumb_es="Embalaje comprimido al vacío",
        h1_zh="服装真空压缩包装指南：压多少、怎么压、压完怎么回弹",
        h1_en="Vacuum Compression Packaging: How Much, How, and How It Recovers",
        h1_ja="衣料品の真空圧縮包装ガイド：どこまで、どう圧縮し、どう復元させるか",
        h1_ko="의류 진공 압축 포장 가이드: 얼마나, 어떻게, 복원은 어떻게",
        h1_fr="Emballage compressé sous vide : combien, comment et la reprise de volume",
        h1_es="Embalaje comprimido al vacío: cuánto, cómo y cómo recupera",
        tag_zh="包装指南",
        tag_en="Packaging Guide",
        tag_ja="包装ガイド",
        tag_ko="포장 가이드",
        tag_fr="Guide emballage",
        tag_es="Guía de embalaje",
        sum_zh="真空压缩是出口与电商仓储最直接的降运费手段，也是投诉高发区：羽绒压成薄片回不了弹、针织衫留下死褶、木竹吊牌被压断。本文用两张表分清真空袋、腔体机、卷压与外箱适配四种方式的压缩率与风险，列出六类品类各自的可压上限与禁忌，讲清抽气时间、封口温度、残余体积比与开箱 24／48 小时回弹测量四项必须记录的参数，共挤 PA/PE 袋与气阀怎么选，吊牌、皮标、堆码承压、集装箱装载与防潮的连带风险，以及可直接抄进询价单的七条验收口径。",
        sum_en="Vacuum compression is the most direct way to cut freight in export and e-commerce storage, and a frequent source of claims: down that never recovers, knitwear with set creases, wooden tags snapped in the pack. Two tables separate vacuum bags, chamber machines, roll compression and carton-only fitting by volume cut and risk; the guide then lists the ceiling and the taboos for six categories, the four parameters to record on every trial — vacuum time, sealing temperature, residual volume ratio and recovery at 24 and 48 hours — how to choose co-extruded PA/PE bags and valves, and the knock-on risks for hang tags, leather patches, stacking strength, container loading and moisture, closing with seven acceptance points you can paste into a quotation request.",
        sum_ja="真空圧縮は輸出とEC倉庫で最も直接的な運賃削減策である一方、クレームの多発地帯でもあります。ダウンは復元せず、ニットには折り癖が残り、木・竹タグは割れます。本記事は2つの表で真空袋・チャンバー機・巻き圧縮・外箱適合の4方式を圧縮率とリスクで整理し、6品目の圧縮上限と禁忌、試作時に必ず記録する4項目（真空引き秒数・シール温度・残存体積比・開封後24／48時間の復元）、共押出PA/PE袋と弁の選び方、タグ・革パッチ・積み重ね耐圧・コンテナ積載・防湿の連鎖リスク、見積書に貼れる7つの検収項目を示します。",
        sum_ko="진공 압축은 수출과 이커머스 창고에서 가장 직접적인 운임 절감 수단인 동시에 클레임 다발 지점입니다. 다운은 복원되지 않고, 니트에는 주름이 남고, 목재 행택은 부러집니다. 이 글은 두 개의 표로 진공백·챔버기·롤 압축·외부 상자 맞춤 네 방식을 압축률과 리스크로 정리하고, 여섯 품목의 압축 상한과 금기, 시험 시 반드시 기록할 네 항목(진공 시간, 실링 온도, 잔여 부피비, 개봉 후 24·48시간 복원), 공압출 PA/PE 백과 밸브 선택, 행택·가죽 패치·적재 내압·컨테이너 적재·방습의 연쇄 리스크, 견적서에 붙일 수 있는 일곱 가지 검수 항목을 제시합니다.",
        sum_fr="La compression sous vide est le moyen le plus direct de réduire le fret à l'export et en entrepôt, et une source fréquente de réclamations : duvet qui ne reprend pas, maille marquée, étiquettes bois cassées. Deux tableaux classent sachets sous vide, machines à cloche, compression par roulage et ajustement carton par taux et par risque ; le guide donne ensuite le plafond et les interdits pour six catégories, les quatre paramètres à consigner à chaque essai — temps d'aspiration, température de soudure, taux de volume résiduel, récupération à 24 et 48 heures —, le choix des sachets PA/PE coextrudés et des valves, puis les risques induits sur étiquettes, pièces en cuir, résistance à l'empilage, chargement et humidité, avec sept points de réception à coller dans une demande de prix.",
        sum_es="La compresión al vacío es el medio más directo de reducir el flete en exportación y almacén, y un foco frecuente de reclamaciones: plumón que no recupera, punto con marcas, etiquetas de madera rotas. Dos tablas clasifican bolsas de vacío, máquinas de cámara, compresión por enrollado y ajuste de caja por tasa y riesgo; la guía da el techo y las prohibiciones de seis categorías, los cuatro parámetros a registrar en cada ensayo —tiempo de aspiración, temperatura de sellado, ratio de volumen residual y recuperación a 24 y 48 horas—, la elección de bolsas PA/PE coextruidas y válvulas, y los riesgos asociados en etiquetas, piezas de piel, resistencia al apilado, carga y humedad, con siete puntos de recepción para copiar en una solicitud de presupuesto.",
    ),
    dict(
        slug="stone-paper-hang-tags-guide.html",
        body="blog/_body_stone.html",
        title_zh="石头纸吊牌指南：防水耐撕的矿物纸材质与工艺 | TAGE",
        title_en="Stone Paper Hang Tag Guide: Waterproof Mineral Paper | TAGE",
        title_ja="ストーンペーパータグガイド：防水・耐引き裂きの鉱物紙 | TAGE",
        title_ko="스톤 페이퍼 행택 가이드: 방수·내인열 미네랄 페이퍼 | TAGE",
        title_fr="Guide des étiquettes en papier de pierre (papier minéral) | TAGE",
        title_es="Guía de etiquetas de papel de piedra (papel mineral) | TAGE",
        desc_zh="石头纸吊牌指南：讲清矿物纸的成分与密度、耐水耐撕指标，与铜版纸和 PP 合成纸的三方对比，胶印、数码、UV 喷墨、烫金与压凹凸的能做与禁忌，打孔、吊绳与鸡眼加工要点，适用与不适用场景，以及环保话术与 FSC、可回收声明的合规边界。来自东莞泰阁包装。",
        desc_en="Stone paper hang tags: mineral paper composition and density, waterproof and tear-resistant behaviour, comparison with coated and PP synthetic paper, printing limits, holes and eyelets.",
        desc_ja="ストーンペーパータグガイド。鉱物紙の組成と密度、耐水・耐引き裂き性、コート紙・PP合成紙との3者比較、オフセット・デジタル・UV・箔・エンボスの可否、穴あけとハトメ加工、向く用途と向かない用途、環境訴求とFSC・リサイクル表示の線引きを解説。東莞泰閣包装。",
        desc_ko="스톤 페이퍼 행택 가이드. 미네랄 페이퍼의 조성과 밀도, 내수·내인열 성능, 코트지·PP 합성지와의 3자 비교, 옵셋·디지털·UV·박·엠보싱의 가능과 금기, 구멍과 아일렛 가공, 적합·부적합 용도, 친환경 소구와 FSC·재활용 표시의 한계를 정리했습니다. 둥관 TAGE 패키징.",
        desc_fr="Étiquettes en papier de pierre : composition et densité du papier minéral, résistance à l'eau et à la déchirure, comparaison avec couché et synthétique PP, limites d'impression, perçage et œillets.",
        desc_es="Etiquetas de papel de piedra: composición y densidad del papel mineral, resistencia al agua y al desgarro, comparación con estucado y sintético PP, límites de impresión, taladrado y ojales.",
        crumb_zh="石头纸吊牌",
        crumb_en="Stone Paper Hang Tags",
        crumb_ja="ストーンペーパータグ",
        crumb_ko="스톤 페이퍼 행택",
        crumb_fr="Étiquettes en papier de pierre",
        crumb_es="Etiquetas de papel de piedra",
        h1_zh="石头纸吊牌指南：防水耐撕的矿物纸怎么选与怎么印",
        h1_en="Stone Paper Hang Tags: Choosing and Printing Waterproof Mineral Paper",
        h1_ja="ストーンペーパータグガイド：防水・耐引き裂き鉱物紙の選び方と印刷",
        h1_ko="스톤 페이퍼 행택 가이드: 방수·내인열 미네랄 페이퍼 선택과 인쇄",
        h1_fr="Étiquettes en papier de pierre : choisir et imprimer le papier minéral",
        h1_es="Etiquetas de papel de piedra: elegir e imprimir el papel mineral",
        tag_zh="材质指南",
        tag_en="Material Guide",
        tag_ja="素材ガイド",
        tag_ko="소재 가이드",
        tag_fr="Guide des matières",
        tag_es="Guía de materiales",
        sum_zh="石头纸（矿物纸）防水、耐撕、生产不用木浆也不用什么水，因此在户外、泳装与工装类目里成了吊牌备选；但它更像一张很薄的塑料片而不是纸，密度远高于纸、折痕处容易开裂、烫金必须低温短时、回收时也未必进纸类回收桶。本文用两张表给出成分与密度、耐水性与耐温的常见值，与铜版纸、PP 合成纸做三方对比，逐条说明胶印、数码、UV 喷墨、烫金、压凹凸与覆膜能做与要避的地方，讲清打孔离边距离、鸡眼低温压装与吊绳选型，列出适用与不适用场景、不要拿纸的克重直接换算的常见错误，以及环保话术与 FSC 声明的合规边界，最后附七条询价与验收清单。",
        sum_en="Stone paper is waterproof, tear-resistant and made without wood pulp or much water, which is why it appears on outdoor, swim and workwear tags; yet it behaves more like a thin plastic sheet than paper — far higher density, cracking along a fold, foil only at low temperature and short dwell, and a sheet that may not belong in the paper recycling bin. Two tables give composition, density, water and heat figures and compare it with coated and PP synthetic paper; the guide then works through offset, digital, UV inkjet, foil, embossing and lamination one by one, sets out hole distance from the edge, cold eyelet pressing and cord selection, lists where it fits and where it does not, flags the common error of carrying paper grammage across, and draws the line on sustainability and FSC claims, closing with seven quotation and acceptance points.",
        sum_ja="ストーンペーパー（鉱物紙）は防水・耐引き裂きで、パルプも水もほとんど使わないため、アウトドア・水着・ワークのタグ候補になります。ただし紙というより薄いプラスチックシートに近く、密度は紙よりはるかに高く、折り目は割れ、箔は低温短時間、紙リサイクルに回せない地域もあります。本記事は2つの表で組成・密度・耐水・耐熱の目安を与え、コート紙とPP合成紙との3者比較を行い、オフセット・デジタル・UV・箔・エンボス・ラミネートの可否を個別に示し、穴位置の縁からの距離、ハトメの低温圧着、ひもの選定、向く用途と向かない用途、紙の目付をそのまま換算する誤り、環境訴求とFSC表示の線引きを整理し、最後に7つの見積り・検収項目を掲載します。",
        sum_ko="스톤 페이퍼(미네랄 페이퍼)는 방수·내인열이고 펄프와 물을 거의 쓰지 않아 아웃도어, 수영복, 작업복 행택 후보가 됩니다. 다만 종이보다 얇은 플라스틱 시트에 가깝고, 밀도가 훨씬 높고, 접힌 선은 갈라지고, 박은 저온 단시간, 종이 재활용으로 보낼 수 없는 지역도 있습니다. 이 글은 두 표로 조성·밀도·내수·내열 기준값을 주고 코트지와 PP 합성지 삼자 비교를 하며, 옵셋·디지털·UV·박·엠보싱·라미네이팅의 가능과 금기를 하나씩 짚고, 구멍 위치와 가장자리 거리, 아일렛 저온 압착, 끈 선택, 적합·부적합 용도, 종이 평량을 그대로 환산하는 흔한 오류, 친환경 소구와 FSC 표시의 한계를 정리하고 마지막에 일곱 가지 견적·검수 항목을 실었습니다.",
        sum_fr="Le papier de pierre est imperméable, résistant à la déchirure et fabriqué sans pâte ni beaucoup d'eau, d'où sa présence sur les étiquettes outdoor, bain et workwear ; il se comporte pourtant comme une fine feuille plastique : densité bien plus élevée, craquelure le long du pli, dorure à basse température et temps court, et une matière qui n'entre pas toujours dans la collecte papier. Deux tableaux donnent composition, densité, résistance à l'eau et à la chaleur, et comparent avec le couché et le synthétique PP ; le guide détaille ensuite offset, numérique, jet d'encre UV, dorure, gaufrage et pelliculage, la distance du trou au bord, le sertissage à froid des œillets et le choix du cordon, les usages adaptés ou non, l'erreur courante de transposer le grammage papier, et la limite des arguments écologiques et FSC, avant sept points de devis et de réception.",
        sum_es="El papel de piedra es impermeable, resistente al desgarro y se fabrica sin pasta y con muy poca agua, de ahí su uso en etiquetas de outdoor, baño y workwear; sin embargo se comporta como una lámina plástica fina: densidad mucho mayor, grietas en el pliegue, estampación solo a baja temperatura y tiempo corto, y un material que no siempre entra en el contenedor de papel. Dos tablas dan composición, densidad, resistencia al agua y al calor y lo comparan con estucado y sintético PP; la guía repasa offset, digital, inyección UV, estampación, relieve y laminado, la distancia del agujero al borde, el prensado en frío de ojales y la elección de cordón, los usos que encajan y los que no, el error habitual de trasladar el gramaje del papel y el límite de los argumentos ecológicos y FSC, y cierra con siete puntos de presupuesto y recepción.",
    ),
]
