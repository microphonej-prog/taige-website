#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-09-29 晚间批次文章元数据（六语：zh-Hant 根 / en / ja / ko / fr / es）。

选题说明：任务主题池 30 个选题与此前批次扩展的国别合规、EUDR/PPWR、原产地标识、
产前样、出货方式、数量容差、数字化打样、编码标准化、供应连续性、采购沟通等均已上线。
本次沿「尺寸与缩率控制」方向扩展两个新选题，写前已核对：
- blog/ 全量 .html（192 篇正文 + 38 个 _body_ 片段）
- en|ja|ko|fr|es/blog/ 目录
- sitemap.xml（1188 个 <loc>）

本次两篇：

1. 织唛与洗水标缩水率（woven-label-shrinkage-guide）
   全站检索「缩率 / 收缩率」仅命中 garment-trims-fabric-compatibility-guide（第 2 节「缩率匹配：
   先测面料，再定辅料」）、garment-label-sewing-thread-guide、woven-label-material-guide 的
   零星提及，无专文。配伍指南讲的是「先测面料再定辅料」的整体匹配思路，本文讲辅料这一侧的缩率
   从哪来（织造张力回缩 / 热切与热定型的热收缩 / 洗水湿热收缩）、材质与切边方式的缩率差异、
   洗后测量的标准做法与留量换算，与其互补而非重复。

2. 辅料尺寸测量与公差（trim-measurement-tolerance-guide）
   「测量」全站仅命中 1 篇、「量具」0 篇。现有 apparel-trims-spec-sheet-guide 讲规格书字段、
   garment-trims-quality-inspection 讲 AQL 抽检流程、trim-order-quantity-unit-conversion 讲数量口径，
   都没有讲「量什么、用哪个量具、在什么状态下量、允差给多少、超差怎么判」。本文填补该空白，
   与上篇（数值本身）互为配套：一篇讲尺寸会怎么变，一篇讲尺寸怎么量、怎么判。
"""

ARTICLES = [
    dict(
        slug="woven-label-shrinkage-guide.html",
        body="blog/_body_shrinkage.html",
        title_zh="织唛与洗水标缩水率指南：洗后尺寸稳定性与留量设计 | TAGE",
        title_en="Woven Label Shrinkage Guide: Stability After Washing | TAGE",
        title_ja="織りラベルと洗濯表示ラベルの収縮率ガイド：洗濯後の寸法安定性 | TAGE",
        title_ko="직조 라벨·세탁 표시 라벨 수축률 가이드: 세탁 후 치수 안정성 | TAGE",
        title_fr="Retrait des labels tissés : stabilité après lavage | TAGE",
        title_es="Encogimiento de etiquetas tejidas: estabilidad tras lavar | TAGE",
        desc_zh="织唛洗后缩水、起皱、字位偏移，是验收最容易漏、售后最容易爆的问题。本文拆解三类收缩机制，对比材质与切边方式的缩率差异，讲清 ISO 6330 与 AATCC 135 洗后测量做法与织造尺寸留量换算，并列清下单前必写的六项规格约定。来自东莞泰阁包装。",
        desc_en="Woven label shrinkage explained: why labels shrink, rate differences by material and edge cut, how to measure after washing, and the allowance to weave in.",
        desc_ja="織りラベルの収縮率ガイド。洗濯後に縮む3つのメカニズム、素材と裁断方法による収縮率の違い、ISO 6330・AATCC 135に基づく洗濯後の測定方法、織り寸法に織り込む余裕の考え方、仕様書に書く6項目を解説します。東莞泰閣包装。",
        desc_ko="직조 라벨 수축률 가이드. 세탁 후 수축하는 세 가지 원인, 소재와 재단 방식에 따른 수축률 차이, ISO 6330·AATCC 135 기준 세탁 후 측정법, 제직 치수 여유 설계, 사양서에 넣을 여섯 항목을 정리합니다. 둥관 TAGE 패키징.",
        desc_fr="Retrait des labels tissés : les trois mécanismes en jeu, les écarts selon matière et coupe, la mesure après lavage et les marges de tissage à prévoir.",
        desc_es="Encogimiento de etiquetas tejidas: los tres mecanismos, diferencias según material y corte, cómo medir tras el lavado y el margen de tejido necesario.",
        crumb_zh="织唛缩水率与尺寸稳定性",
        crumb_en="Label Shrinkage and Stability",
        crumb_ja="ラベルの収縮率と寸法安定性",
        crumb_ko="라벨 수축률과 치수 안정성",
        crumb_fr="Retrait et stabilité des labels",
        crumb_es="Encogimiento y estabilidad",
        h1_zh="织唛与洗水标缩水率指南：洗后尺寸稳定性与留量设计",
        h1_en="Woven Label Shrinkage: Dimensional Stability After Washing",
        h1_ja="織りラベルと洗濯表示ラベルの収縮率ガイド：洗濯後の寸法安定性と余裕の設計",
        h1_ko="직조 라벨·세탁 표시 라벨 수축률 가이드: 세탁 후 치수 안정성과 여유 설계",
        h1_fr="Retrait des labels tissés et étiquettes d'entretien : stabilité dimensionnelle",
        h1_es="Encogimiento de etiquetas tejidas y de cuidado: estabilidad dimensional",
        tag_zh="尺寸与缩率控制", tag_en="Shrinkage and Fit", tag_ja="収縮率と寸法管理",
        tag_ko="수축률·치수 관리", tag_fr="Retrait et dimensions", tag_es="Encogimiento y medidas",
        sum_zh="织唛洗后缩水、起皱、字位偏移，是验收时最容易被忽略、售后最容易爆发的问题。本文先把缩率来源拆成三类：织造张力回升带来的自然回缩、热切与热定型引入的热收缩、洗水烘干带来的湿热收缩，说明三者叠加方式不同、缓解手段也不同。第二节给出一张材质与切边方式的缩率对照表，解释为什么同为 30mm 宽的缎面织唛与厚提花织唛，洗后可能差出 2mm 以上。第三节给出可执行的洗后测量做法：同批取三片、按 ISO 6330 或 AATCC 135 洗三次、洗前洗后对同一基准点各测一次、吊干与转筒烘干分开记录。第四节讲留量设计的换算思路，强调不要把缩率补偿悄悄塞进成品尺寸，而要同时标清「织造尺寸」与「洗净后尺寸」。第五节讲主唛与洗水标同件却缩率不同步导致的起皱与鼓包，以及组合下单时怎么避坑。第六节列出下单前必须写进规格书的六项约定与到货验收的抽查口径。",
        sum_en="Shrinkage, wrinkling and drifting print are the defects that pass inspection and then blow up after the first wash. The article separates the three mechanisms at work — natural relaxation of weaving tension, thermal contraction from hot cutting and heat setting, and wet-heat shrinkage in washing and drying — and shows why each needs a different remedy. A comparison table of materials and edge finishes explains how a 30mm satin label and a heavy jacquard of the same nominal width can differ by more than 2mm after washing. The measurement section gives a method you can run: three pieces from the same batch, three washes to ISO 6330 or AATCC 135, the same datum measured before and after, line drying and tumble drying reported separately. The allowance section explains how to convert a washed dimension into a weaving size, and why the shrinkage factor should never be hidden inside the finished dimension rather than stated as a washed-and-measured figure. It closes with the creasing that appears when a neck label and a care label shrink at different rates on the same garment, and the six clauses worth writing into the specification before the order is placed.",
        sum_ja="洗濯後の収縮、しわ、印字位置のずれは、検品では見逃されやすく、販売後に顕在化しやすい不良です。本記事はまず収縮の要因を3つに分けます。製織張力の戻りによる自然収縮、熱カットや熱セットによる熱収縮、洗濯と乾燥による湿熱収縮です。それぞれ重なり方も緩和策も異なります。第2節では素材と裁断方法ごとの収縮率対照表を示し、同じ30mm幅でもサテン織りと厚手ジャカードで洗濯後に2mm以上の差が出る理由を説明します。第3節は実行可能な洗濯後の測定手順です。同一ロットから3枚、ISO 6330またはAATCC 135で3回洗濯、洗濯前後で同一基準点を測定、吊り干しとタンブラー乾燥は分けて記録します。第4節は余裕の設計と換算で、収縮補正を完成寸法に隠さず、「製織寸法」と「洗濯後寸法」を明記する考え方を示します。第5節はメインラベルと洗濯表示ラベルの収縮差によるしわ・浮きと、同時発注時の回避策を扱います。",
        sum_ko="세탁 후 수축, 주름, 인쇄 위치 이동은 검수에서는 놓치기 쉽고 판매 후에 터지기 쉬운 결함입니다. 이 글은 먼저 수축 원인을 세 가지로 나눕니다. 제직 장력 회복에 따른 자연 수축, 열절단과 열고정에 의한 열수축, 세탁과 건조에 의한 습열 수축입니다. 각각 겹치는 방식과 대응이 다릅니다. 2절은 소재와 재단 방식별 수축률 대조표를 제시하고, 같은 30mm 폭이라도 새틴 직조와 두꺼운 자카드가 세탁 후 2mm 이상 차이 나는 이유를 설명합니다. 3절은 실행 가능한 세탁 후 측정 절차입니다. 같은 로트에서 3장, ISO 6330 또는 AATCC 135로 3회 세탁, 세탁 전후 동일 기준점 측정, 걸이 건조와 텀블러 건조는 따로 기록합니다. 4절은 여유 설계와 환산으로, 수축 보정을 완성 치수에 숨기지 말고 '제직 치수'와 '세탁 후 치수'를 함께 명시하는 방법을 다룹니다. 5절은 메인 라벨과 세탁 표시 라벨의 수축 차이로 생기는 주름과 들뜸, 동시 발주 시 회피책을 정리합니다.",
        sum_fr="Rétrécissement, plissement et décalage d'impression : des défauts qui passent le contrôle et se révèlent après le premier lavage. L'article distingue trois mécanismes — relâchement de la tension de tissage, contraction thermique liée à la coupe à chaud et au thermofixage, retrait hydrothermique au lavage et au séchage — chacun appelant une réponse différente. Un tableau compare matières et finitions de bords et explique comment un label satin et un jacquard épais de même largeur nominale peuvent différer de plus de 2 mm après lavage. La partie mesure propose une méthode applicable : trois pièces du même lot, trois lavages selon ISO 6330 ou AATCC 135, un même repère mesuré avant et après, séchage à plat et séchage en tambour consignés séparément. La partie marges montre comment convertir une dimension lavée en dimension de tissage, sans jamais dissimuler la compensation de retrait dans la cote finie. L'article traite enfin le froissement lorsque label de col et étiquette d'entretien ne se rétractent pas au même rythme, et les six clauses à inscrire au cahier des charges.",
        sum_es="Encogimiento, arrugas y desplazamiento de la impresión: defectos que pasan el control y estallan después del primer lavado. El artículo separa tres mecanismos —relajación de la tensión de tejido, contracción térmica por corte en caliente y termofijado, y retracción hidrotérmica en lavado y secado—, cada uno con una respuesta distinta. Una tabla compara materiales y acabados de borde y explica cómo una etiqueta de satén y un jacquard grueso de la misma anchura nominal pueden diferir más de 2 mm tras el lavado. La parte de medición propone un método aplicable: tres piezas del mismo lote, tres lavados según ISO 6330 o AATCC 135, la misma referencia medida antes y después, secado al aire y en secadora registrados por separado. La parte de márgenes explica cómo convertir una medida lavada en medida de tejido, sin esconder nunca la compensación dentro de la cota final. Cierra con el arrugado que aparece cuando la etiqueta de cuello y la de cuidado encogen a ritmos distintos, y las seis cláusulas que conviene fijar antes del pedido.",
    ),
    dict(
        slug="trim-measurement-tolerance-guide.html",
        body="blog/_body_measure.html",
        title_zh="服装辅料尺寸测量与公差指南：量什么、用什么量具、允差给多少 | TAGE",
        title_en="Trims Measurement and Tolerance Guide: How to Measure | TAGE",
        title_ja="副資材の寸法測定と公差ガイド：何を、どの器具で、どの許容差で | TAGE",
        title_ko="부자재 치수 측정과 공차 가이드: 무엇을, 어떤 기구로, 얼마나 | TAGE",
        title_fr="Mesure et tolérance des accessoires : quoi et avec quoi | TAGE",
        title_es="Medición y tolerancia de accesorios: qué y con qué medir | TAGE",
        desc_zh="辅料尺寸争议多半不是质量问题，而是基准、量具和测量状态不一致。本文按品类列出该量的字段与常见允差区间，讲清量具选择与精度、测量条件、抽检判定与超差处理，并给出一份可以直接抄进规格书的测量约定。来自东莞泰阁包装。",
        desc_en="Trims measurement guide: which gauges to use, how to define the datum, typical tolerance ranges by trim type, and how to get it all into the spec sheet.",
        desc_ja="副資材の寸法測定と公差ガイド。基準の取り方、ノギスやマイクロメータなどの器具選定、温湿度・張力などの測定条件、品目別の許容差の目安、抜き取り判定と外れ品の扱い、仕様書に書く測定の約束事を解説します。東莞泰閣包装。",
        desc_ko="부자재 치수 측정과 공차 가이드. 기준점 설정, 캘리퍼스·마이크로미터 등 기구 선택, 온습도와 장력 등 측정 조건, 품목별 허용치 기준, 샘플링 판정과 초과품 처리, 사양서에 넣을 측정 약속을 정리합니다. 둥관 TAGE 패키징.",
        desc_fr="Mesurer les accessoires : instruments, définition du repère, plages de tolérance par pièce et règles de mesure à inscrire dans la fiche technique.",
        desc_es="Medir accesorios: elección de instrumentos, definición de la referencia, rangos de tolerancia por pieza y cómo redactar las reglas de medición en la ficha.",
        crumb_zh="辅料尺寸测量与公差",
        crumb_en="Trims Measurement and Tolerance",
        crumb_ja="副資材の寸法測定と公差",
        crumb_ko="부자재 치수 측정과 공차",
        crumb_fr="Mesure et tolérance des accessoires",
        crumb_es="Medición y tolerancia",
        h1_zh="服装辅料尺寸测量与公差指南：量什么、用什么量具、允差给多少",
        h1_en="Trims Measurement and Tolerance: What to Measure, With What, and How Much",
        h1_ja="副資材の寸法測定と公差ガイド：何を、どの器具で、どれだけ許容するか",
        h1_ko="부자재 치수 측정과 공차: 무엇을, 어떤 기구로, 얼마까지 허용할까",
        h1_fr="Mesure et tolérance des accessoires : quoi mesurer, avec quoi, et dans quelle marge",
        h1_es="Medición y tolerancia de accesorios: qué medir, con qué y cuánto admitir",
        tag_zh="尺寸公差与验收", tag_en="Measurement and Tolerance", tag_ja="寸法公差と検収",
        tag_ko="치수 공차·검수", tag_fr="Mesure et tolérance", tag_es="Medición y tolerancia",
        sum_zh="辅料尺寸的争议，大多不是做坏了，而是双方量的不是同一个东西：基准点不同、量具精度不同、测量时的状态不同。本文第一节先把三类分歧拆开，说明为什么「差 1mm」的争论里往往有一半是方法问题。第二节给出量具选择表：钢尺与卷尺适合长边粗测、游标卡尺适合厚度与孔位、测厚仪与电子天平用于克重与厚度、光源箱与色差仪用于颜色判定，并说明各自的最小读数与适用边界。第三节讲测量条件：温湿度平衡、成品需回潮静置、布料类要平铺不拉伸、洗前洗后要分开标注状态。第四节按品类列出要量的字段与常见允差区间，涵盖吊牌、织唛、洗水标、包装袋与纸袋。第五节讲抽检与判定：抽多少、按 AQL 怎么判、超差之后是让步接收还是返工补货、留样与复测怎么走。第六节给出一份可以直接抄进规格书的测量约定，把基准、量具、状态、允差与判定口径一次写清。",
        sum_en="Most arguments about trim dimensions are not about bad parts — they are about two parties measuring different things: a different datum, a different instrument, a different state of the material. The first section splits the three sources of disagreement and shows why half of a one-millimetre dispute is usually a method problem. The second gives a gauge selection table: steel rule and tape for long edges, vernier calipers for thickness and hole position, thickness gauge and balance for calliper and grammage, light booth and spectrophotometer for colour, each with its minimum reading and limits of use. The third covers the conditions of measurement: temperature and humidity equilibrium, resting time for finished goods, laying fabric flat without stretching, and labelling the state as before or after washing. The fourth lists the fields worth measuring and typical tolerance ranges by product family — hang tags, woven labels, care labels, poly bags and paper bags. The fifth covers sampling and judgement: how many pieces, how to apply AQL, and whether an out-of-tolerance lot is accepted by concession, reworked or replaced, plus retention samples and re-testing. It closes with a measurement clause you can copy straight into the specification.",
        sum_ja="副資材の寸法トラブルは、作りの不良より「測っているものが違う」ことが原因です。基準点、測定器具の精度、測定時の状態がずれています。第1節では3つの食い違いを分解し、1mmの議論の半分は方法の問題であると説明します。第2節は器具の選定表です。長辺の概測はスケールとメジャー、厚みと穴位置はノギス、目付と厚みはマイクロメータと電子天秤、色判定は光源ボックスと分光測色計。それぞれの最小目盛りと適用範囲を示します。第3節は測定条件で、温湿度の平衡、完成品のなじませ、生地を伸ばさず平置き、洗濯前後の状態表示を扱います。第4節は品目別に測る項目と許容差の目安（タグ、織りラベル、洗濯表示ラベル、ポリ袋、紙袋）を整理。第5節は抜き取りと判定（数量、AQL、外れ品の concession・手直し・補充、保存見本と再測定）。第6節は仕様書にそのまま使える測定の約束事です。",
        sum_ko="부자재 치수 분쟁은 대부분 제작 불량이 아니라 서로 다른 것을 측정하기 때문에 생깁니다. 기준점, 기구 정밀도, 측정 상태가 다릅니다. 1절은 세 가지 불일치를 분해하고, 1mm 논쟁의 절반은 방법 문제임을 설명합니다. 2절은 기구 선택표입니다. 긴 변의 개략 측정은 스케일과 줄자, 두께와 타공 위치는 버니어 캘리퍼스, 평량과 두께는 마이크로미터와 전자저울, 색상 판정은 광원 박스와 분광측색계를 사용하며 각각의 최소 눈금과 적용 범위를 제시합니다. 3절은 측정 조건으로 온습도 평형, 완제품 안정화, 원단을 늘리지 않고 평평하게 놓기, 세탁 전후 상태 표기를 다룹니다. 4절은 품목별로 측정할 항목과 허용치 기준(행택, 직조 라벨, 세탁 표시 라벨, 비닐백, 종이백)을 정리합니다. 5절은 샘플링과 판정(수량, AQL, 초과품의 조건부 수용·재작업·보충, 보관 샘플과 재측정), 6절은 사양서에 그대로 쓸 측정 약속입니다.",
        sum_fr="La plupart des litiges de dimensions ne viennent pas d'une pièce ratée mais de deux mesures différentes : repère différent, instrument différent, état différent. La première partie sépare ces trois sources et montre pourquoi la moitié d'un écart d'un millimètre relève de la méthode. La deuxième propose un tableau de choix d'instruments : règle et mètre ruban pour les grands côtés, pied à coulisse pour l'épaisseur et la position des trous, micromètre et balance pour l'épaisseur et le grammage, cabine lumière et spectrocolorimètre pour la couleur, avec leur lecture minimale. La troisième traite les conditions : équilibre en température et humidité, temps de repos, tissu à plat sans tension, état avant ou après lavage clairement indiqué. La quatrième liste les champs à mesurer et les tolérances usuelles par famille — étiquettes suspendues, labels tissés, étiquettes d'entretien, sachets et sacs papier. La cinquième couvre l'échantillonnage et le jugement : combien de pièces, l'AQL, l'acceptation par dérogation, la reprise, le remplacement, les témoins conservés. Elle se termine par une clause de mesure à recopier dans la fiche technique.",
        sum_es="Casi todas las discusiones de medidas vienen de medir cosas distintas: otra referencia, otro instrumento, otro estado del material. La primera parte separa esas tres fuentes y muestra por qué la mitad de una discrepancia de un milímetro es un problema de método. La segunda ofrece una tabla de elección de instrumentos: regla y cinta para lados largos, calibre para grosor y posición de taladros, micrómetro y balanza para grosor y gramaje, cabina de luz y espectrofotómetro para color, con su lectura mínima. La tercera trata las condiciones: equilibrio de temperatura y humedad, reposo del producto, tejido plano sin tensión y estado antes o después del lavado indicado. La cuarta enumera los campos a medir y las tolerancias habituales por familia —etiquetas colgantes, tejidas, de cuidado, bolsas y bolsas de papel—. La quinta cubre muestreo y criterio: cuántas piezas, AQL, aceptación por concesión, retrabajo, reposición y muestras testigo. Cierra con una cláusula de medición lista para copiar en la ficha técnica.",
    ),
]
