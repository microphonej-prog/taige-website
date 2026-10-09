#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-09 晚间批次（20:00）每日更新：2 篇新文章元数据（六语：zh-Hant 根 / en / ja / ko / fr / es）

选题说明（任务给定主题池 30 项连同既有扩展均已上线，本次沿两个尚未独立成文的方向扩展，
已核对 blog/、en|ja|ko|fr|es/blog/ 与 sitemap.xml 无重复 slug，并 grep 全站确认关键词覆盖情况）：

- plus-size-womenswear-trims-guide：全站 grep「大码 / plus size / talla grande」仅
  clothing-size-label-guide、woven-label-placement-guide 等 3 处顺带提一句，无专文。
  本文按「四个特殊要求 → 尺码标注四方案对照表 → 织嘜/洗标/缝制加固 → 弹力面料洗护标识 →
  吊牌尺寸表与二维码 → 包装与挂装放大规格 → 询价验收清单」讲完大码品类的辅料闭环。

- garment-hanger-types-guide：全站无衣架专文（hanger-bag-guide 只讲挂装胶袋，
  其余均为顺带提及）。本文按「衣架承担的四个角色 → 五种材质对照表 → 类型与服装匹配 →
  表面处理与 LOGO 与气味控制 → 挂装出货（衣架＋衣架袋＋挂装纸箱）→ 验收询价清单」展开。
"""

ARTICLES = [
    dict(
        slug="plus-size-womenswear-trims-guide.html",
        body="blog/_body_plus.html",
        title_zh="大码女装辅料指南：尺码标、织嘜与包装怎么选 | TAGE",
        title_en="Plus-Size Womenswear Trims Guide: Size Labels, Woven Labels &amp; Packaging | TAGE",
        title_ja="プラスサイズ衣料の副資材ガイド：サイズラベル・織りラベル・包装の選び方 | TAGE",
        title_ko="플러스 사이즈 의류 부자재 가이드: 사이즈 라벨·직조 라벨·포장 선택법 | TAGE",
        title_fr="Guide des accessoires grande taille : tailles, labels tissés et emballage | TAGE",
        title_es="Guía de accesorios de talla grande: tallas, etiquetas tejidas y embalaje | TAGE",
        desc_zh="大码女装辅料指南：尺码标怎么排到 5XL、腰头与侧缝如何加固、弹力面料的洗护标示、吊牌尺寸表与二维码怎么写、包装袋与衣架袋该放大多少，并附可直接抄进询价邮件的确认清单。来自东莞泰阁包装。",
        desc_en="Plus-size womenswear trims: size labels to 5XL, reinforced waistband and side-seam care labels, stretch care marks, hang tag size charts and larger bags.",
        desc_ja="プラスサイズ衣料の副資材ガイド。サイズラベルを 5XL まで展開する方法、ウエストと脇縫いの補強、ストレッチ生地のケア表示、タグの寸法表と QR コード、袋とハンガーバッグの拡大サイズ、そのまま見積りメールに使える確認リストを解説。東莞泰閣包装。",
        desc_ko="플러스 사이즈 의류 부자재 가이드. 사이즈 라벨을 5XL까지 전개하는 방법, 허리 밴드와 옆선 보강, 스트레치 원단 관리 표시, 행택 치수표와 QR코드, 봉투와 행거백 확대 규격, 견적 메일에 쓸 수 있는 확인 리스트를 정리했습니다. 둥관 TAGE 패키징.",
        desc_fr="Guide des accessoires grande taille : étiquettes de taille jusqu'au 5XL, ceinture et couture latérale renforcées, entretien des tissus extensibles, mesures sur l'étiquette suspendue et emballages plus grands.",
        desc_es="Guía de accesorios de talla grande: etiquetas de talla hasta la 5XL, cinturilla y costura lateral reforzadas, cuidado de tejidos elásticos, medidas en la etiqueta colgante y embalajes mayores.",
        crumb_zh="大码女装辅料",
        crumb_en="Plus-Size Trims",
        crumb_ja="プラスサイズ副資材",
        crumb_ko="플러스 사이즈 부자재",
        crumb_fr="Accessoires grande taille",
        crumb_es="Accesorios talla grande",
        h1_zh="大码女装辅料与标签指南：尺码、加固与包装尺寸",
        h1_en="Plus-Size Womenswear Trims: Sizing, Reinforcement and Packaging",
        h1_ja="プラスサイズ衣料の副資材とラベル：サイズ・補強・包装寸法",
        h1_ko="플러스 사이즈 의류 부자재와 라벨: 사이즈·보강·포장 치수",
        h1_fr="Accessoires grande taille : tailles, renforts et dimensions d'emballage",
        h1_es="Accesorios de talla grande: tallas, refuerzos y medidas de embalaje",
        tag_zh="品类指南",
        tag_en="Category Guide",
        tag_ja="品目ガイド",
        tag_ko="품목 가이드",
        tag_fr="Guide par catégorie",
        tag_es="Guía por categoría",
        sum_zh="大码女装的辅料要求与标准码完全不同：尺码标要排到 5XL、腰头与侧缝要加固、洗水标必须说明氨纶混纺的洗护方式、吊牌要给出真实的成衣尺寸表，包装袋也要跟着放大。本文先讲大码对辅料的四个特殊要求（尺码跨度、承重与加固、侧缝洗标的触感、包装尺寸），再用一张表对比字母码、数字码、实测尺寸表与弹力单一码四种标注方案的适用场景与风险；随后具体到织嘜位置、侧缝洗标 25–30 mm 宽度与两端回针加固、腰头与吊绳受力点的双针打枣，再讲弹力面料的低温洗涤、不可漂白与耐洗字迹验证，以及吊牌背面该印的三围尺寸、适穿身高体重区间与二维码；最后是包装袋、衣架袋与纸袋在大码规格下的袋宽袋深与承重要点，附一页式询价与验收清单。",
        sum_en="Plus-size trims are nothing like standard sizes: size labels run to 5XL, waistbands and side seams need reinforcement, care labels must explain elastane blends, hang tags need a real garment measurement chart and bags must grow with the garment. The guide opens with four requirements plus size places on trims — size range, load and reinforcement, side-seam care label comfort, packaging size — then a table compares letter sizes, numeric sizes, a measured size chart and stretch one-size by use case and risk. It moves on to neck label position, keeping a side-seam care label within 25–30 mm with bar-tacked ends, double-needle work at the waistband and cord attachment points, low-temperature washing and no bleach for stretch fabrics, wash-legibility testing, and what belongs on the back of the hang tag: flat measurements, a height and weight range and a QR code. It closes with bag width, depth and load for plus-size packaging and a one-page quote and acceptance checklist.",
        sum_ja="プラスサイズの副資材要件は標準サイズとは別物です。サイズラベルは 5XL まで、ウエストと脇縫いは補強、洗濯表示はスパンデックス混紡の扱いを説明し、タグには実寸表を載せ、袋も拡大する必要があります。本記事はまず副資材に求められる 4 要件（サイズ展開・荷重と補強・脇の洗濯表示の肌触り・包装サイズ）を示し、次にアルファベット・数字・実寸表・ストレッチワンサイズの 4 方式を用途とリスクで比較。続いてメインラベル位置、脇の洗濯表示を幅 25〜30mm に収めて両端を返し縫いする方法、ウエストと吊りひも取付点の二本針とカンヌキ、ストレッチ生地の低温洗濯・漂白不可と耐洗濯検証、タグ裏面に載せる三围寸法・対応身長体重・QR コードを解説。最後に大サイズの包装における袋幅・奥行き・荷重と、1 ページの見積り・検収チェックリストを掲載します。",
        sum_ko="플러스 사이즈 부자재 요건은 표준 사이즈와 완전히 다릅니다. 사이즈 라벨은 5XL까지, 허리 밴드와 옆선은 보강, 세탁 라벨은 스판덱스 혼방 관리법을 설명해야 하고, 행택에는 실제 치수표를 넣고 봉투도 커져야 합니다. 이 글은 먼저 부자재에 요구되는 네 조건(사이즈 범위·하중과 보강·옆선 세탁 라벨 촉감·포장 크기)을 제시하고, 알파벳·숫자·실측 치수표·스트레치 원사이즈 네 가지 표기 방식을 용도와 위험으로 비교합니다. 이어 메인 라벨 위치, 옆선 세탁 라벨을 폭 25~30mm로 유지하고 양끝을 되박기로 보강하는 방법, 허리 밴드와 끈 부착점의 두 바늘·바택, 스트레치 원단의 저온 세탁·표백 금지와 세탁 내구 검증, 행택 뒷면에 넣을 평면 치수·권장 키와 몸무게·QR코드를 다룹니다. 마지막으로 대형 포장의 봉투 폭·깊이·하중과 한 장짜리 견적·검수 체크리스트를 제공합니다.",
        sum_fr="Les exigences de la grande taille n'ont rien de commun avec les tailles standard : étiquettes jusqu'au 5XL, ceinture et coutures latérales renforcées, entretien des mélanges élasthanne à expliquer, vrai tableau de mesures sur l'étiquette suspendue et emballages qui grandissent. Le guide commence par quatre exigences — amplitude de tailles, charge et renforts, confort de l'étiquette latérale, taille d'emballage — puis un tableau compare tailles lettres, tailles numériques, tableau de mesures et taille unique extensible par usage et par risque. Suivent la position du label de col, une étiquette d'entretien latérale tenue sous 25–30 mm avec arrêts aux extrémités, le double aiguille sur ceinture et attaches, le lavage à basse température sans javel pour les tissus extensibles, le test de lisibilité après lavage et le contenu du verso de l'étiquette suspendue : mesures à plat, plage de taille et de poids, QR code. Il se termine par largeur, profondeur et charge des emballages grande taille et une check-list de devis et de réception.",
        sum_es="Las exigencias de la talla grande no tienen nada que ver con las tallas estándar: etiquetas hasta la 5XL, cinturilla y costuras laterales reforzadas, cuidado de mezclas con elastano por explicar, tabla real de medidas en la etiqueta colgante y embalajes que crecen. La guía abre con cuatro exigencias —amplitud de tallas, carga y refuerzos, confort de la etiqueta lateral y tamaño de embalaje— y luego una tabla compara tallas por letra, numéricas, tabla de medidas y talla única elástica por uso y riesgo. Sigue la posición de la etiqueta de cuello, mantener la etiqueta de cuidado lateral por debajo de 25–30 mm con remaches en los extremos, doble aguja en cinturilla y puntos de cordón, lavado a baja temperatura sin blanqueo en tejidos elásticos, ensayo de legibilidad tras lavado y el contenido del reverso de la etiqueta colgante: medidas en plano, rango de altura y peso y código QR. Cierra con ancho, fondo y carga de los embalajes en tallas grandes y una lista de presupuesto y recepción.",
    ),
    dict(
        slug="garment-hanger-types-guide.html",
        body="blog/_body_hanger.html",
        title_zh="服装衣架选型指南：材质、规格与挂装出货配套 | TAGE",
        title_en="Garment Hanger Guide: Materials, Sizes and Hanging Shipment Setup | TAGE",
        title_ja="衣類ハンガー選定ガイド：素材・サイズ・掛装出荷の組み合わせ | TAGE",
        title_ko="의류 행거 가이드: 소재·규격·걸이 출하 구성 | TAGE",
        title_fr="Guide des cintres : matières, tailles et expédition sur cintre | TAGE",
        title_es="Guía de perchas: materiales, medidas y envío colgado | TAGE",
        desc_zh="服装衣架选型指南：PP／ABS／木质／植绒／金属五类材质的档次与成本对比，上衣架、裤夹架、西服架与童装架怎么匹配，LOGO 工艺与气味控制，以及衣架、衣架袋与挂装纸箱的配套逻辑与验收清单。来自东莞泰阁包装。",
        desc_en="Garment hanger guide: PP, ABS, wood, flocked and metal compared, hanger types matched to garments, logo finishing, odour control and hanging shipment setup.",
        desc_ja="衣類ハンガー選定ガイド。PP・ABS・木製・植毛・金属の 5 素材を比較し、トップ・ズボン・スーツ・子供用ハンガーの使い分け、ロゴ加工とにおい対策、ハンガーバッグと掛装カートンの組み合わせ、検収チェックリストを解説。東莞泰閣包装。",
        desc_ko="의류 행거 가이드. PP·ABS·목재·플로킹·금속 다섯 소재를 비교하고, 상의·바지·정장·아동용 행거 매칭, 로고 공정과 냄새 관리, 행거백·걸이 카톤 구성, 검수 체크리스트를 정리했습니다. 둥관 TAGE 패키징.",
        desc_fr="Guide des cintres : PP, ABS, bois, flocké et métal comparés, types adaptés aux vêtements, marquage, maîtrise des odeurs et expédition sur cintre.",
        desc_es="Guía de perchas: PP, ABS, madera, flocado y metal comparados, tipos según la prenda, marcado, control de olores y envío colgado.",
        crumb_zh="服装衣架选型",
        crumb_en="Choosing Garment Hangers",
        crumb_ja="ハンガーの選定",
        crumb_ko="행거 선택",
        crumb_fr="Choisir ses cintres",
        crumb_es="Elegir perchas",
        h1_zh="服装衣架选型指南：材质、类型、LOGO 与挂装出货",
        h1_en="Garment Hanger Guide: Materials, Types, Logos and Hanging Shipments",
        h1_ja="ハンガー選定ガイド：素材・種類・ロゴ・掛装出荷",
        h1_ko="행거 선택 가이드: 소재·종류·로고·걸이 출하",
        h1_fr="Guide des cintres : matières, types, marquage et expédition",
        h1_es="Guía de perchas: materiales, tipos, marcado y envío colgado",
        tag_zh="包装配件",
        tag_en="Packaging Accessory",
        tag_ja="包装アクセサリー",
        tag_ko="포장 액세서리",
        tag_fr="Accessoire d'emballage",
        tag_es="Accesorio de embalaje",
        sum_zh="衣架是服装出厂前最后一个被顾客看见的辅件，也是最容易失控的一项成本：材质选错会让肩部鼓包变形，承重不够大衣挂两天就断，LOGO 工艺选薄了到门店已经掉色；更关键的是衣架决定了整批货是平装还是挂装出货。本文先讲衣架要同时承担的四个角色（肩型、承重、品牌标识、挂装保护），用一张表对比 PP／PS、ABS、木质、植绒与金属五类材质的手感档次、成本起订与适用场景，再讲挂钩形式与肩部结构这两个容易忽略的参数，以及上衣架、裤夹架、西服架、童装架与内衣架各自与服装的匹配要点；随后是丝印、烫金、热转印、激光雕刻与软胶标五种 LOGO 工艺的耐磨掉色与气味控制，最后落到衣架、衣架袋与挂装纸箱的配套逻辑、平装与挂装的选择依据，以及承重、外观、标识、气味四条验收与询价清单。",
        sum_en="A hanger is the last accessory a customer sees and the easiest cost line to lose control of: the wrong material bulges the shoulder, too little load capacity snaps a coat hanger in two days, a thin logo fades before the shop floor — and above all, the hanger decides whether the shipment goes flat-packed or on hangers. The guide opens with the four jobs a hanger does at once (shoulder shape, load, brand mark, hanging protection), then a table compares PP/PS, ABS, wood, flocked and metal by feel, cost, MOQ and use case. It covers the two overlooked parameters, hook type and shoulder construction, and how top, trouser-clip, suit, children's and lingerie hangers each match a garment. Five logo processes — silk screen, hot foil, heat transfer, laser engraving and soft badges — are judged on abrasion, colour loss and odour, before the piece closes on the hanger, hanger bag and hanging carton system, how to choose between flat and hanging shipments, and a four-point acceptance and quote checklist covering load, appearance, marking and odour.",
        sum_ja="ハンガーは商品が出荷される前に顧客が最後に目にする副資材であり、最も管理しにくいコスト項目でもあります。素材を間違えると肩が盛り上がり、耐荷重が足りないとコートが 2 日で折れ、薄いロゴ加工は店頭に着く前に色落ちします。さらに、ハンガーは平置きか掛装かを決めます。本記事はまずハンガーが同時に担う 4 つの役割（肩線・荷重・ブランド表示・掛装保護）を示し、PP／PS・ABS・木製・植毛・金属の 5 素材を質感・コスト・ロット・用途で比較。見落としやすいフック形式と肩構造の 2 点、トップ・ズボン・スーツ・子供用・下着用ハンガーの使い分けを解説します。続いてシルク印刷・箔押し・熱転写・レーザー彫刻・軟質標の 5 つのロゴ加工を耐摩耗・色落ち・においで評価し、最後にハンガー・ハンガーバッグ・掛装カートンの体系、平置きと掛装の選び方、荷重・外観・表示・においの 4 項目の検収と見積りチェックリストをまとめます。",
        sum_ko="행거는 제품이 출하되기 전 고객이 마지막으로 보는 부자재이며 관리가 가장 어려운 원가 항목입니다. 소재를 잘못 고르면 어깨가 부풀고, 하중이 부족하면 코트가 이틀 만에 부러지며, 얇은 로고 공정은 매장에 도착하기 전에 색이 빠집니다. 더욱이 행거는 평면 포장인지 걸이 출하인지를 결정합니다. 이 글은 먼저 행거가 동시에 하는 네 역할(어깨선·하중·브랜드 표시·걸이 보호)을 설명하고, PP/PS·ABS·목재·플로킹·금속 다섯 소재를 촉감·비용·최소 수량·용도로 비교합니다. 놓치기 쉬운 걸이 형식과 어깨 구조, 상의·바지·정장·아동·속옷 행거의 매칭을 다룹니다. 이어 실크 인쇄·금박·열전사·레이저 각인·소프트 배지 다섯 로고 공정을 내마모·색 빠짐·냄새로 평가하고, 마지막으로 행거·행거백·걸이 카톤 체계, 평면과 걸이 선택 기준, 하중·외관·표시·냄새 네 항목의 검수와 견적 체크리스트를 정리합니다.",
        sum_fr="Le cintre est le dernier accessoire vu par le client et la ligne de coût la plus difficile à maîtriser : une matière inadaptée bombe l'épaule, une charge insuffisante casse un cintre en deux jours, un marquage fin pâlit avant le magasin — et surtout, le cintre décide entre expédition à plat et sur cintre. Le guide présente les quatre missions simultanées du cintre (ligne d'épaule, charge, marque, protection en suspendu), puis un tableau compare PP/PS, ABS, bois, flocké et métal par toucher, coût, quantité mini et usage. Il traite deux paramètres oubliés, le type de crochet et la construction d'épaule, et l'accord entre cintres haut, pince, costume, enfant et lingerie. Cinq procédés de marquage — sérigraphie, dorure, transfert, gravure laser et pastille souple — sont jugés sur l'abrasion, la perte de couleur et l'odeur, avant de conclure sur le système cintre, housse et carton suspendu, le choix entre plat et suspendu, et une check-list de réception à quatre points : charge, aspect, marquage et odeur.",
        sum_es="La percha es el último accesorio que ve el cliente y la partida de coste más difícil de controlar: un material inadecuado abomba el hombro, una carga insuficiente rompe un perchero en dos días, un marcado fino se decolora antes de llegar a tienda y, sobre todo, la percha decide entre envío plano y colgado. La guía presenta las cuatro misiones simultáneas de la percha (línea de hombro, carga, marca y protección en colgado) y una tabla compara PP/PS, ABS, madera, flocado y metal por tacto, coste, mínimo y uso. Trata dos parámetros olvidados, el tipo de gancho y la construcción del hombro, y el encaje de perchas de parte superior, pinza, traje, infantil y lencería. Cinco procesos de marcado —serigrafía, dorado, transferencia, grabado láser y placa blanda— se juzgan por abrasión, pérdida de color y olor, antes de cerrar con el sistema percha, funda y caja colgada, la elección entre plano y colgado, y una lista de recepción de cuatro puntos: carga, aspecto, marcado y olor.",
    ),
]
