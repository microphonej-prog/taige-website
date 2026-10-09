#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-09 下午批次（14:00）每日更新：2 篇新文章元数据（六语：zh-Hant 根 / en / ja / ko / fr / es）

选题说明（主题池 30 项与既有扩展均已上线，本次沿两个尚未独立成文的方向扩展，
已核对 blog/、en|ja|ko|fr|es/blog/ 与 sitemap.xml 无重复 slug，并 grep 全站确认关键词覆盖情况）：

- garment-label-itch-free-guide：全站 grep「无感标签 / tagless 专文 / 超柔织嘜」，现有仅
  heat-transfer-labels（热转印工艺专文）、print-on-demand-apparel-labels（按需印花耐洗）、
  underwear-label-guide 与 sock-hosiery-trims-guide 中一两句「标签比袜子还扎人」的提醒，
  无一篇把「标签扎人」当主题的解决方案文章。本文按定位（四个来源）→ 四条材质路线对比表 →
  切边/形状/缝制位置/洗标宽度工艺细节 → 婴童·内衣·羊毛羊绒·贴身运动分品类重点 →
  四条可写进合同的验收指标 → 询价清单，讲完标签手感问题的完整闭环。

- wooden-packaging-ippc-export-guide：全站 grep「IPPC / ISPM 15 / 熏蒸 / fumigation / 木质包装」0 处；
  garment-trunk-export-packaging、garment-trims-carton-loading-guide、garment-trims-freight-mode-guide
  均只讲纸箱、箱唛与运输方式，未涉及实木托盘与木箱的 ISPM 15 与 IPPC 标识。本文讲清适用范围
  （实木 vs 深加工板材豁免）、IPPC 标识五要素解读、热处理/溴甲烷熏蒸/介电加热对比表、
  胶合板托盘·塑料托盘·纸滑托板等免熏蒸替代、责任划分与合同条款、发货前后核对清单。
"""

ARTICLES = [
    dict(
        slug="garment-label-itch-free-guide.html",
        body="blog/_body_itch.html",
        title_zh="服装标签扎人怎么办：无感标签与超柔织嘜方案 | TAGE",
        title_en="Itchy Garment Labels: Tagless and Soft Woven Label Solutions | TAGE",
        title_ja="衣類ラベルがチクチクする時の対策：タグレスと柔らかい織りラベル | TAGE",
        title_ko="의류 라벨이 따가울 때: 태그리스와 부드러운 직조 라벨 | TAGE",
        title_fr="Étiquettes qui grattent : tagless et labels tissés doux | TAGE",
        title_es="Etiquetas que pican: soluciones tagless y tejidas suaves | TAGE",
        desc_zh="服装标签扎人怎么办？本文按定位、选材、工艺、验收四步，对比超柔织嘜、热转印无感标签、缎面洗标与印刷唛的手感、耐洗与成本，讲清切边、圆角、缝制位置与洗标宽度的处理办法，并给出可直接写进合同的四条验收指标。来自东莞泰阁包装。",
        desc_en="Itchy garment labels: compare soft woven, tagless, satin and printed labels by hand feel, wash results and cost, plus edge, position and acceptance criteria.",
        desc_ja="衣類ラベルがチクチクする問題の解決ガイド。ソフト織りラベル・タグレス熱転写・サテン洗濯表示・印刷ラベルの肌触りと耐洗濯性を比較し、超音波カット、丸角、縫い位置、洗濯表示の幅の処理方法、ベビー・下着・ウール・インナー別の優先案、契約に書ける4つの検収基準を解説。東莞泰閣包装。",
        desc_ko="의류 라벨이 따가운 문제 해결 가이드. 소프트 직조·태그리스 열전사·새틴 세탁·인쇄 라벨을 촉감과 세탁 내구성으로 비교하고, 초음파 절단, 둥근 모서리, 봉제 위치, 세탁 라벨 폭 관리법과 유아·속옷·울·베이스레이어별 우선안, 계약서에 쓸 수 있는 네 가지 검수 기준을 정리했습니다. 둥관 TAGE 패키징.",
        desc_fr="Étiquettes qui grattent : comparer labels tissés doux, tagless, satin et imprimés par toucher, tenue au lavage et coût, avec bords, position de couture et critères de réception.",
        desc_es="Etiquetas que pican: comparar tejidas suaves, tagless, satén e impresas por tacto, lavado y coste, con bordes, posición de costura y criterios de recepción.",
        crumb_zh="标签手感与无感标签",
        crumb_en="Label Hand Feel and Tagless",
        crumb_ja="ラベルの肌触りとタグレス",
        crumb_ko="라벨 촉감과 태그리스",
        crumb_fr="Toucher des étiquettes et tagless",
        crumb_es="Tacto de etiquetas y tagless",
        h1_zh="服装标签扎人怎么办：材质、工艺与无感标签四条路线",
        h1_en="Itchy Garment Labels: Four Routes from Material to Process",
        h1_ja="衣類ラベルがチクチクする時の対策：素材・加工・タグレスの4つのルート",
        h1_ko="의류 라벨이 따가울 때: 소재·가공·태그리스 네 가지 경로",
        h1_fr="Étiquettes qui grattent : matière, fabrication et quatre voies tagless",
        h1_es="Etiquetas que pican: material, proceso y cuatro vías tagless",
        tag_zh="工艺指南",
        tag_en="Process Guide",
        tag_ja="加工ガイド",
        tag_ko="가공 가이드",
        tag_fr="Guide de fabrication",
        tag_es="Guía de proceso",
        sum_zh="标签扎人很少是单一原因：织嘜底纱太粗、热切留下硬化熔边、缝制位置正压脊柱、洗水标用了硬涂层。本文先教三步定位（扎的是哪个标、新的就扎还是洗后变硬、持续摩擦还是走动才明显），再用一张表把超柔织嘜、热转印无感标签、缎面洗标、印刷唛与自粘标的手感、耐洗表现、成本与适合品类并排比清楚；随后讲切边优先级、圆角与泪滴形、折边藏硬边、缝在领标位而非脊柱、洗标分段缩小宽度五条具体做法，并给出婴童、内衣、羊毛羊绒、贴身运动与工装各自的重点与客诉分类办法，最后是洗后边缘硬度、缝制强度、耐洗字迹、小部件拉力四条可写进合同的标准，以及一页式询价清单。",
        sum_en="Label itch is rarely one cause: coarse warp yarn, a hardened heat-cut edge, a seam over the spine, a stiff coated care label. Three questions locate it first, then a table compares soft woven, tagless heat transfer, satin, printed and self-adhesive labels by feel, wash performance, cost and category. The guide then sets out cutting priority, rounded and teardrop shapes, hiding the hard edge in a fold, stitching to the neck-label position rather than the spine and splitting a care label to cut its width, followed by what matters for babywear, underwear, wool, base layers and workwear, and four contract-ready standards: edge hardness after washing, stitching strength, wash legibility and small-parts pull.",
        sum_ja="ラベルのチクチクは原因が一つではありません。タテ糸の太さ、熱カットの硬化した耳、背骨の真上に来る縫い位置、硬いコーティングの洗濯表示。まず3つの質問で切り分け、次に1つの表でソフト織りラベル・タグレス熱転写・サテン・印刷ラベル・粘着ラベルを肌触り、耐洗濯性、コスト、向く品目で比較します。続いて切り方の優先順位、丸角と涙型、折りで硬い耳を隠す、背骨ではなくネーム位置に縫う、洗濯表示を2分割して幅を狭めるという5つの具体策、ベビー・下着・ウール・インナー・ワーク別の要点とクレームの分け方、そして洗濯後の耳の硬さ・縫製強度・印字の耐洗濯・小部品の引張という契約に書ける4基準と1ページの見積りチェックリストを掲載します。",
        sum_ko="라벨 따가움은 원인이 하나가 아닙니다. 굵은 경사, 열절단으로 굳은 가장자리, 척추 위 봉제, 뻣뻣한 코팅 세탁 라벨. 먼저 세 가지 질문으로 원인을 좁히고, 한 표에서 소프트 직조·태그리스 열전사·새틴·인쇄·점착 라벨을 촉감, 세탁 내구성, 비용, 적합 품목으로 비교합니다. 이어 절단 우선순위, 둥근 모서리와 물방울 형태, 접기로 굳은 가장자리 숨기기, 척추 대신 넥라벨 위치 봉제, 세탁 라벨을 두 블록으로 나눠 폭 줄이기 다섯 가지 방법과 유아·속옷·울·베이스레이어·작업복별 중점, 클레임 구분법, 그리고 세탁 후 가장자리 경도·봉제 강도·인쇄 내구성·소부품 인장 네 가지 계약 기준과 한 장짜리 견적 체크리스트를 담았습니다.",
        sum_fr="Le grattage a rarement une seule cause : chaîne épaisse, bord thermocoupé durci, couture sur la colonne, étiquette d'entretien enduite. Trois questions le localisent, puis un tableau compare labels tissés doux, tagless, satin, imprimés et autocollants par toucher, tenue au lavage, coût et catégorie. Suivent la priorité de coupe, les formes arrondies et en goutte, le bord dur caché dans un pli, la couture au label de col plutôt que sur la colonne et le dédoublement de l'étiquette d'entretien pour réduire sa largeur, puis les priorités bébé, lingerie, laine, première peau et workwear, et quatre critères contractuels : dureté du bord après lavage, résistance de couture, lisibilité après lavage et traction des petites pièces.",
        sum_es="El picor rara vez tiene una sola causa: urdimbre gruesa, borde cortado en caliente endurecido, costura sobre la columna, etiqueta de cuidado rígida. Tres preguntas lo localizan y luego una tabla compara tejidas suaves, tagless, satén, impresas y autoadhesivas por tacto, lavado, coste y categoría. Siguen la prioridad de corte, formas redondeadas y en gota, el borde duro escondido en el pliegue, coser a la posición de etiqueta de cuello en lugar de la columna y dividir la etiqueta de cuidado para reducir su ancho, además de las prioridades en infantil, lencería, lana, primera piel y workwear, y cuatro criterios contractuales: dureza del borde tras lavado, resistencia de costura, legibilidad tras lavado y tracción de piezas pequeñas.",
    ),
    dict(
        slug="wooden-packaging-ippc-export-guide.html",
        body="blog/_body_ippc.html",
        title_zh="出口木质包装与托盘指南：IPPC 标识与免熏蒸替代 | TAGE",
        title_en="Wood Packaging and Pallets for Export: IPPC and Alternatives | TAGE",
        title_ja="輸出用の木質包装とパレット：IPPC 表示と燻蒸不要の代替案 | TAGE",
        title_ko="수출용 목재 포장과 팔레트: IPPC 표시와 훈증 불필요 대안 | TAGE",
        title_fr="Emballages bois et palettes à l'export : IPPC et alternatives | TAGE",
        title_es="Embalaje de madera y palés en exportación: IPPC y alternativas | TAGE",
        desc_zh="出口木质包装与托盘指南：哪些木件必须带 IPPC 标识、热处理与溴甲烷熏蒸怎么选、旧托盘为何在口岸被视同未处理，以及胶合板托盘、塑料托盘与纸滑托板等免熏蒸替代方案；附标识五要素解读、责任划分与合同费用条款、发货前后核对清单。来自东莞泰阁包装。",
        desc_en="Wood packaging and pallets for export: which parts need IPPC marks, heat treatment versus methyl bromide, used pallets, and fumigation-free alternatives.",
        desc_ja="輸出用の木質包装とパレットのガイド。IPPC 表示が必要な部材、熱処理と臭化メチル燻蒸の選び方、中古パレットが未処理扱いになる理由、合板・プラスチック・紙パレットなどの燻蒸不要案、表示5要素の読み方、責任分担と費用条項、出荷前後のチェックリストを解説。東莞泰閣包装。",
        desc_ko="수출용 목재 포장과 팔레트 가이드. IPPC 표시가 필요한 부재, 열처리와 메틸브로마이드 훈증 선택, 중고 팔레트가 미처리로 간주되는 이유, 합판·플라스틱·종이 팔레트 등 훈증 불필요 대안, 표시 다섯 요소, 책임 분담과 비용 조항, 출하 전후 점검 리스트를 정리했습니다. 둥관 TAGE 패키징.",
        desc_fr="Emballages bois et palettes à l'export : quelles pièces exigent le marquage IPPC, traitement thermique ou bromure de méthyle, palettes d'occasion et alternatives sans fumigation.",
        desc_es="Embalaje de madera y palés para exportación: qué piezas exigen marcado IPPC, tratamiento térmico o bromuro de metilo, palés usados y alternativas sin fumigación.",
        crumb_zh="出口木质包装与托盘",
        crumb_en="Export Wood Packaging and Pallets",
        crumb_ja="輸出用の木質包装とパレット",
        crumb_ko="수출용 목재 포장과 팔레트",
        crumb_fr="Emballages bois et palettes à l'export",
        crumb_es="Embalaje de madera y palés",
        h1_zh="出口木质包装与托盘指南：IPPC 标识怎么读、怎么选、怎么替代",
        h1_en="Wood Packaging and Pallets for Export: Reading IPPC Marks and Choosing Alternatives",
        h1_ja="輸出用の木質包装とパレット：IPPC 表示の読み方・処理の選び方・代替案",
        h1_ko="수출용 목재 포장과 팔레트: IPPC 표시 읽기, 처리 선택, 대안",
        h1_fr="Emballages bois et palettes à l'export : lire l'IPPC, choisir, remplacer",
        h1_es="Embalaje de madera y palés para exportación: leer el IPPC, elegir y sustituir",
        tag_zh="出口合规",
        tag_en="Export Compliance",
        tag_ja="輸出コンプライアンス",
        tag_ko="수출 컴플라이언스",
        tag_fr="Conformité export",
        tag_es="Cumplimiento de exportación",
        sum_zh="服装辅料大多走纸箱，但托盘、木箱与支撑木一旦出现就牵出 ISPM 15：没有合格 IPPC 标识的实木包装，可能在目的港被拒收、销毁或退运，费用落在发货方。本文讲清适用边界（实木要管，胶合板、刨花板、密度板与 OSB 豁免）、辅料出口里实木真正出现的四类场景，用一张表拆解 IPPC 标识五要素（符号、国家代码、处理方注册号、处理方式代码、批次日期），再用一张表对比热处理 HT、溴甲烷熏蒸 MB 与介电加热 DH 的做法、周期成本、目的国接受度与注意事项，重点提示旧托盘与加固木条这两个高频踩坑点；随后给出胶合板托盘、塑料托盘、纸滑托板与纸质护角四条免熏蒸路线与选择逻辑，最后落到责任划分、合同费用条款与发货前后的核对清单。",
        sum_en="Most trims ship in cartons, but a pallet, crate or piece of dunnage brings ISPM 15 into play: solid wood packaging without a valid IPPC mark can be refused, destroyed or returned at destination, with the cost falling on the shipper. The guide sets the boundary — solid wood is in scope, plywood, particleboard, MDF and OSB are exempt — and the four places solid wood actually appears in trims exports, then breaks the IPPC mark into five elements and compares heat treatment, methyl bromide and dielectric heating by method, lead time, cost and destination acceptance, flagging used pallets and bracing strips as the two most common traps. It closes with four fumigation-free routes — plywood, plastic, slip sheets, paper corner boards — plus responsibility, contract cost clauses and a pre-shipment checklist.",
        sum_ja="副資材の多くは段ボール輸送ですが、パレット・木箱・当て木が出ると ISPM 15 が適用され、有効な IPPC 表示のない無垢材包装は仕向港で拒否・廃棄・返送となり費用は出荷者負担です。適用範囲（無垢材は対象、合板・パーティクルボード・MDF・OSB は除外）と、副資材輸出で無垢材が出る4つの場面を示し、IPPC 表示を5要素に分解。熱処理 HT・臭化メチル MB・誘電加熱 DH を方法・期間・コスト・受容性・注意点で比較し、中古パレットと補強材という2つの落とし穴を指摘します。最後に合板・プラスチック・スリップシート・紙コーナーという燻蒸不要の4案、責任分担、契約の費用条項、出荷前後のチェックリストを示します。",
        sum_ko="부자재는 대부분 골판지로 운송되지만 팔레트·목재 상자·받침목이 들어가면 ISPM 15가 적용됩니다. 유효한 IPPC 표시가 없는 원목 포장은 도착항에서 거부·폐기·반송될 수 있고 비용은 출하자 부담입니다. 적용 범위(원목은 대상, 합판·파티클보드·MDF·OSB는 제외)와 부자재 수출에서 원목이 등장하는 네 장면을 정리하고, IPPC 표시를 다섯 요소로 분해합니다. 열처리 HT·메틸브로마이드 MB·유전가열 DH를 방법, 기간, 비용, 수용도, 주의사항으로 비교하고 중고 팔레트와 보강 목재라는 두 함정을 짚습니다. 마지막으로 합판·플라스틱·슬립시트·종이 코너보드 네 가지 훈증 불필요 대안과 책임 분담, 계약 비용 조항, 출하 전후 점검 리스트를 제시합니다.",
        sum_fr="La plupart des accessoires partent en carton, mais une palette, une caisse ou un calage déclenche l'ISPM 15 : sans marquage IPPC valide, l'emballage bois peut être refusé, détruit ou renvoyé, aux frais de l'expéditeur. Le guide fixe le périmètre — bois massif concerné, contreplaqué, particules, MDF et OSB exemptés — et les quatre cas où le bois apparaît réellement, décompose le marquage en cinq éléments et compare traitement thermique, bromure de méthyle et chauffage diélectrique par procédé, délai, coût et acceptation, en signalant les palettes d'occasion et les renforts comme les deux pièges courants. Puis quatre solutions sans fumigation — contreplaqué, plastique, feuilles de glissement, cornières carton —, les responsabilités, les clauses de coûts et la check-list avant expédition.",
        sum_es="La mayoría de los accesorios viaja en cartón, pero un palé, un cajón o un calzo activa la ISPM 15: sin marcado IPPC válido, el embalaje de madera puede rechazarse, destruirse o devolverse a costa del expedidor. La guía fija el alcance —madera maciza incluida; contrachapado, aglomerado, MDF y OSB exentos— y los cuatro casos en que aparece la madera, descompone el marcado en cinco elementos y compara tratamiento térmico, bromuro de metilo y dieléctrico por procedimiento, plazo, coste y aceptación, señalando los palés usados y los refuerzos como los dos fallos más comunes. Cierra con cuatro vías sin fumigación —contrachapado, plástico, hojas deslizantes, perfiles de cartón—, responsabilidades, cláusulas de coste y lista de control antes del envío.",
    ),
]
