#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-09-30 上午批次文章元数据（六语：zh-Hant 根 / en / ja / ko / fr / es）。

选题说明：任务主题池 30 个选题与历次扩展选题（国别合规、EUDR/PPWR、原产地标识、
产前样、出货方式、数量容差、数字化打样、编码标准化、供应连续性、采购沟通等）
均已上线，本次沿「颜色批核与放行（流程侧）」与「质量异常处理与纠正措施（8D）」
两个方向扩展新选题。写前已核对 blog/ 全量文件、en|ja|ko|fr|es/blog/ 与 sitemap.xml：

- 辅料颜色批核流程（trim-color-approval-process）：全站「批色」命中 0 篇、「批核」仅 1 篇。
  hang-tag-color-management 讲的是吊牌印刷色彩管理（专色 vs 四色、纸张覆膜影响），
  woven-label-color-matching 讲的是织唛对色技术（色纱、ΔE、色牢度），两篇都是「技术侧」；
  本文讲「流程侧」——批核要哪三份文件、对色的光源背景条件、ΔE 与目视怎么配合、
  批次放行单写什么、超差怎么走让步接收，与上述两篇互补而非重复。

- 质量异常处理与 8D 报告（trim-quality-8d-report-guide）：全站「8D」命中 0 篇。
  garment-trims-quality-inspection 讲验货（AQL、各品类要点），
  garment-trims-claims-liability-guide 讲索赔（责任界定、赔付方式），
  本文讲发现异常后的处置顺序（围堵→根因→纠正措施→验证关闭）与 8D 八步在辅料场景的
  落地写法，是上述两篇之间的「处理流程」环节，无专文。
"""

ARTICLES = [
    dict(
        slug="trim-color-approval-process.html",
        body="blog/_body_colorapprove.html",
        title_zh="服装辅料颜色批核流程指南：批色单、对色灯箱与批次放行 | TAGE",
        title_en="Trims Colour Approval Process: Shade Card, Light Box, Batch Release | TAGE",
        title_ja="副資材の色承認プロセス：色番確認・色評価光源・ロット放行 | TAGE",
        title_ko="부자재 색상 승인 프로세스: 색상 번호·검사 광원·로트 출하 승인 | TAGE",
        title_fr="Validation des couleurs d'accessoires : référence, cabine lumière, libération de lot | TAGE",
        title_es="Aprobación de color de accesorios: referencia, cabina de luz y liberación de lote | TAGE",
        desc_zh="辅料颜色批核不是看一眼像不像，而是把判断变成可存档的证据。本文讲清批核要的三份文件、对色时最易出错的光源与背景条件、ΔE 与目视怎么配合、不同材质允差为何不能一刀切，以及批次放行怎么签、超差怎么办。来自东莞泰阁包装。",
        desc_en="How trims colour approval really works: the three documents to keep, light box and background conditions, ΔE versus visual judgement, and batch release notes.",
        desc_ja="副資材の色承認プロセスの解説。押さえるべき3つの書類（色番確認書・色見本・初回封入見本）、色評価の光源と背景条件、ΔEと目視の併用、素材別に許容差を変える理由、ロット放行書の記載事項、外れた場合の特別採用の手順までを整理します。東莞泰閣包装。",
        desc_ko="부자재 색상 승인 프로세스 안내. 반드시 남길 세 가지 서류(색상 확인서·색상 견본·초물 봉인 견본), 색 평가 시 광원과 배경 조건, ΔE 수치와 육안 판정의 병행, 소재별 허용치를 달리해야 하는 이유, 로트 출하 승인서 기재 사항, 초과 시 특채 절차까지 정리합니다. 둥관 TAGE 패키징.",
        desc_fr="Comment valider une couleur d'accessoire : les trois documents à conserver, les conditions de cabine lumière, ΔE et jugement visuel, et la libération de lot.",
        desc_es="Cómo aprobar el color de un accesorio: los tres documentos a conservar, condiciones de cabina de luz, ΔE frente a la vista y liberación de lote.",
        crumb_zh="颜色批核与放行",
        crumb_en="Colour Approval",
        crumb_ja="色承認と放行",
        crumb_ko="색상 승인과 출하",
        crumb_fr="Validation couleur",
        crumb_es="Aprobación de color",
        h1_zh="服装辅料颜色批核与放行流程：从色卡确认单到批次放行",
        h1_en="Trims Colour Approval Process: From Shade Card to Batch Release",
        h1_ja="副資材の色承認と放行プロセス：色番確認書からロット放行まで",
        h1_ko="부자재 색상 승인과 출하 프로세스: 색상 확인서부터 로트 승인까지",
        h1_fr="Processus de validation couleur : de la fiche de référence à la libération du lot",
        h1_es="Proceso de aprobación de color: de la ficha de referencia a la liberación del lote",
        tag_zh="颜色批核与放行", tag_en="Colour Approval", tag_ja="色承認と放行", tag_ko="색상 승인·출하",
        tag_fr="Validation couleur", tag_es="Aprobación de color",
        sum_zh="辅料颜色出问题，往往不是供应商做不好，而是双方对「合格」没有一个说清楚的判定条件：在哪盏灯下看、允差多少、谁签字放行、超差后怎么办。本文第一节把批核要留的三份文件说清：色卡确认单（色号＋允差＋观察光源＋材质工艺）、批色样（用真实材料在真实工艺下做出、标明生产条件）、首件封样（双方签字盖章，之后所有批次都对照它实物比对）。第二节用一张表列出对色最容易出错的五个条件——光源、角度、背景、样品与标准的可比性、观察者——并给出建议做法。第三节讲数字与目视怎么配合：ΔE 适合量化同材质同工艺的比较，但不能跨材质一刀切，深色和荧光色另有口径，织唛色纱、纸张吸墨、覆膜与烫金各有自己的允差。第四节给出一张批次放行单该写什么，以及超差时的让步接收流程。最后讲三类高频颜色纠纷的预防。",
        sum_en="Colour problems with trims are rarely about a supplier who cannot do the job — they come from never agreeing what acceptable means: under which light, with what tolerance, who signs off, and what happens when a batch drifts. The first section sets out the three documents worth keeping: a shade card confirmation listing reference, tolerance, viewing light and material, a dyed sample made with real material on the real process, and a first-article sealed standard signed by both sides. The second tabulates the five conditions that most often break a colour check — light source, angle, background, comparability of sample and standard, observer — with the recommended practice for each. The third explains how numbers and eyes work together: ΔE quantifies comparisons within one material and process but cannot be applied across materials, dark and fluorescent shades have their own rules, and woven yarn, paper ink absorption, lamination and foil each carry their own tolerance. The fourth gives the fields of a batch release note and the deviation route for out-of-tolerance lots, closing with prevention for the three most common colour disputes.",
        sum_ja="副資材の色トラブルの原因は、作れないことよりも「合格」の判定条件を決めていないことにあります。どの光源で見るのか、許容差はいくらか、誰が放行するのか、外れたらどうするのか。第1節では残すべき3つの書類を示します。色番確認書（色番＋許容差＋観察光源＋素材と加工）、実素材・実工程で作る色見本、双方が署名した初回封入見本です。第2節では色評価で最も失敗しやすい5条件（光源・角度・背景・見本と基準の比較可能性・観察者）を表にまとめ、推奨方法を添えます。第3節は数値と目視の併用を解説：ΔEは同一素材・同一工程の比較には有効ですが素材をまたぐ一律適用はできず、濃色や蛍光色には別の基準があり、織り糸・紙の吸インク・ラミネート・箔押しもそれぞれ固有の許容差を持ちます。第4節はロット放行書の記載事項と、許容差を外れた場合の特別採用の流れを示し、最後に頻出する3つの色トラブルの予防を扱います。",
        sum_ko="부자재 색상 문제는 공급사가 못 만드는 경우보다, '합격'의 판정 조건을 정하지 않은 데서 생깁니다. 어느 광원에서 볼지, 허용치는 얼마인지, 누가 승인할지, 초과하면 어떻게 할지입니다. 1절은 남겨야 할 세 서류를 정리합니다. 색상 확인서(색상 번호+허용치+관찰 광원+소재와 공정), 실제 소재와 실제 공정으로 만든 색상 견본, 양측이 서명한 초물 봉인 견본입니다. 2절은 색 평가에서 가장 자주 실패하는 다섯 조건(광원, 각도, 배경, 견본과 기준의 비교 가능성, 관찰자)을 표로 정리하고 권장 방법을 제시합니다. 3절은 수치와 육안의 병행 사용을 다룹니다. ΔE는 동일 소재·동일 공정 비교에는 유효하지만 소재를 넘어 일률 적용할 수 없고, 진한 색과 형광 색은 별도 기준이며, 직조 사(絲)·종이 잉크 흡수·라미네이팅·박압은 각각 고유의 허용치를 가집니다. 4절은 로트 출하 승인서 기재 사항과 허용치 초과 시 특채 절차, 마지막으로 자주 발생하는 세 가지 색상 분쟁의 예방을 다룹니다.",
        sum_fr="Les problèmes de couleur viennent rarement d'un fournisseur incapable : ils naissent de ne jamais définir ce qu'est acceptable — sous quelle lumière, avec quelle tolérance, qui valide, et que faire en cas de dérive. La première partie présente les trois documents à conserver : fiche de référence (référence, tolérance, lumière d'observation, matière et procédé), échantillon teint sur matière et procédé réels, et étalon de première pièce signé par les deux parties. La deuxième réunit dans un tableau les cinq conditions qui font échouer un contrôle couleur — source lumineuse, angle, fond, comparabilité échantillon/étalon, observateur — avec la pratique recommandée. La troisième explique l'usage combiné du chiffre et de l'œil : le ΔE quantifie une comparaison à matière et procédé identiques mais ne se transpose pas d'une matière à l'autre, les teintes foncées et fluorescentes ont d'autres règles, et fil teint, absorption du papier, lamination et dorure ont chacune leur tolérance. La quatrième détaille la fiche de libération de lot et la dérogation, avant la prévention des trois litiges les plus fréquents.",
        sum_es="Los problemas de color rara vez se deben a un proveedor incapaz: nacen de no definir qué es aceptable —bajo qué luz, con qué tolerancia, quién firma y qué se hace cuando el lote se desvía—. La primera parte presenta los tres documentos que conviene conservar: ficha de referencia (referencia, tolerancia, luz de observación, material y proceso), muestra teñida con material y proceso reales, y patrón de primera pieza firmado por ambas partes. La segunda reúne en una tabla las cinco condiciones que más hacen fallar un control de color —fuente de luz, ángulo, fondo, comparabilidad entre muestra y patrón, observador— con la práctica recomendada. La tercera explica el uso combinado de cifra y vista: el ΔE cuantifica comparaciones dentro de un mismo material y proceso, pero no se traslada entre materiales; los tonos oscuros y fluorescentes tienen otras reglas, y el hilo teñido, la absorción del papel, el laminado y el estampado en caliente tienen su propia tolerancia. La cuarta detalla la nota de liberación de lote y la desviación, y cierra con la prevención de los tres litigios más frecuentes.",
    ),
    dict(
        slug="trim-quality-8d-report-guide.html",
        body="blog/_body_8d.html",
        title_zh="服装辅料质量异常处理指南：围堵、8D 报告与整改跟踪 | TAGE",
        title_en="Trims Quality Failure Handling: Containment, 8D Reports, Follow-up | TAGE",
        title_ja="副資材の品質異常対応ガイド：封じ込め・8Dレポート・是正の追跡 | TAGE",
        title_ko="부자재 품질 이상 대응 가이드: 봉쇄·8D 보고서·시정 조치 추적 | TAGE",
        title_fr="Non-conformité d'accessoires : confinement, rapport 8D, suivi | TAGE",
        title_es="No conformidad de accesorios: contención, informe 8D, seguimiento | TAGE",
        desc_zh="辅料出问题时，最贵的不是赔一批，而是原因没查清、下批再犯。本文给出发现异常后的处置顺序、8D 八步在辅料场景怎么落地、问题描述怎么写才可查证、常见根因方向，以及用什么数据验证整改才算关闭。来自东莞泰阁包装。",
        desc_en="When trims fail, the real cost is not the claim but a root cause nobody found. A practical order of response, the 8D steps for trims, and how to verify fixes.",
        desc_ja="副資材の品質異常対応ガイド。異常発見後の手順（隔離・棚卸・通知・証拠保全・納期の巻き返し）、8Dの8ステップを副資材にどう当てはめるか、検証可能な問題記述の書き方、5Whyと特性要因図で見るべき典型的な根本原因、是正をデータで検証して完了とする基準を整理します。東莞泰閣包装。",
        desc_ko="부자재 품질 이상 대응 가이드. 이상 발견 후 조치 순서(격리·실물 파악·통보·증거 확보·납기 만회), 8D 여덟 단계를 부자재에 적용하는 방법, 검증 가능한 문제 기술 작성법, 5Why와 특성 요인도로 확인할 대표적 근본 원인, 시정 조치를 데이터로 검증해 종결하는 기준을 정리합니다. 둥관 TAGE 패키징.",
        desc_fr="Traiter un défaut d'accessoire : ordre des actions, les huit étapes du 8D appliquées aux accessoires, rédaction vérifiable du problème et clôture sur preuves.",
        desc_es="Cómo tratar un defecto de accesorios: orden de actuación, las ocho etapas del 8D aplicadas, redacción verificable del problema y cierre con pruebas.",
        crumb_zh="质量异常与整改",
        crumb_en="Quality Failures &amp; 8D",
        crumb_ja="品質異常と是正",
        crumb_ko="품질 이상과 시정",
        crumb_fr="Non-conformité et 8D",
        crumb_es="No conformidad y 8D",
        h1_zh="服装辅料质量异常处理指南：围堵、8D 报告与整改跟踪",
        h1_en="Trims Quality Failure Handling: Containment, 8D Report and Follow-up",
        h1_ja="副資材の品質異常対応ガイド：封じ込め、8Dレポート、是正の追跡",
        h1_ko="부자재 품질 이상 대응 가이드: 봉쇄, 8D 보고서, 시정 추적",
        h1_fr="Guide de traitement des non-conformités : confinement, rapport 8D, suivi des actions",
        h1_es="Guía de tratamiento de no conformidades: contención, informe 8D y seguimiento",
        tag_zh="质量异常与整改", tag_en="Quality &amp; 8D", tag_ja="品質異常と是正", tag_ko="품질 이상·시정",
        tag_fr="Qualité et 8D", tag_es="Calidad y 8D",
        sum_zh="辅料质量异常真正贵的地方不是赔一批货，而是问题没弄清、下批还会再犯。本文第一节给发现异常后的 72 小时处置顺序：先隔离停用并清点受影响批次与在制品，再通知供应商与内部相关方、拍清证据，最后判断是否需要补货抢交期——顺序颠倒会让现场证据消失。第二节把 8D 八步落到辅料场景，用一张表列出每一步该产出什么、常见的走形式做法与可查证的替代要求。第三节讲问题描述怎么量化：用 5W2H 加上缺陷位置、比例、尺寸或色差数值，才经得起双方核对。第四节给根因分析的三个常用工具——5Why、鱼骨图、好批与坏批对比——并列出辅料常见的根因方向：色纱或纸批号更换、油墨与胶水参数、刀模磨损、缝制张力、储存污染。第五节讲整改验证与关闭：连续三批数据、留样复检、书面关闭并把改进写进来料检验标准，才算真正结束。",
        sum_en="The expensive part of a trims defect is not the claim — it is an unidentified cause that comes back on the next order. The first section sets out the 72 hours after detection: isolate and stop use, count affected batches and work in progress, notify the supplier and internal stakeholders, record evidence, then decide whether a replacement run is needed to protect the delivery date. Doing those in the wrong order destroys the evidence. The second maps the eight 8D steps onto trims with a table of what each step must produce, the box-ticking version, and the verifiable alternative. The third shows how to quantify a problem statement: 5W2H plus defect location, proportion, and the measured size or colour deviation, so both sides can check it. The fourth covers three root-cause tools — 5Why, fishbone, and good-batch versus bad-batch comparison — and the directions that cause most trims failures: a changed yarn or paper lot, ink and adhesive settings, worn dies, stitching tension, storage contamination. The fifth explains closure: three consecutive batches of data, re-testing retained samples, written closure, and folding the change into the incoming inspection standard.",
        sum_ja="副資材の品質異常で本当に高くつくのは賠償ではなく、原因が分からないまま次ロットで再発することです。第1節は発見後72時間の手順を示します。まず隔離して使用を止め、影響ロットと仕掛品を棚卸し、次にサプライヤーと社内関係者へ通知して証拠を記録し、最後に納期を守るための追加生産の要否を判断します。順序を誤ると現物証拠が失われます。第2節は8Dの8ステップを副資材に当てはめ、各段階の成果物・形骸化しやすいやり方・検証可能な代替要求を表にまとめます。第3節は問題記述の定量化：5W2H に欠陥位置・発生比率・寸法や色差の数値を加えることで双方が確認できます。第4節は根本原因分析の3手法（5Why・特性要因図・良ロットと不良ロットの比較）と、副資材で多い原因の方向（色糸や紙のロット変更、インクと接着剤の条件、金型摩耗、縫製テンション、保管時の汚染）を示します。第5節は是正の検証と完了：連続3ロットのデータ、保管見本の再検査、文書での完了、受入検査基準への反映までを行って終了とします。",
        sum_ko="부자재 품질 이상에서 정말 비싼 것은 보상금이 아니라 원인을 모른 채 다음 로트에서 재발하는 일입니다. 1절은 발견 후 72시간의 조치 순서를 제시합니다. 먼저 격리하고 사용을 중단한 뒤 영향 로트와 재공품을 파악하고, 다음으로 공급사와 내부 관계자에게 통보하고 증거를 기록하며, 마지막으로 납기를 지키기 위한 추가 생산 필요 여부를 판단합니다. 순서를 바꾸면 현장 증거가 사라집니다. 2절은 8D 여덟 단계를 부자재에 적용해 각 단계의 산출물, 형식적 처리, 검증 가능한 대안 요구를 표로 정리합니다. 3절은 문제 기술의 정량화를 다룹니다. 5W2H에 결함 위치, 발생 비율, 치수나 색차 수치를 더해야 양측이 확인할 수 있습니다. 4절은 근본 원인 분석의 세 도구(5Why, 특성 요인도, 양품 로트와 불량 로트 비교)와 부자재에서 흔한 원인 방향(색사·종이 로트 변경, 잉크·접착제 조건, 금형 마모, 봉제 장력, 보관 오염)을 제시합니다. 5절은 시정 검증과 종결: 연속 세 로트 데이터, 보관 견본 재검사, 문서 종결, 수입 검사 기준 반영까지 마쳐야 끝납니다.",
        sum_fr="Ce qui coûte cher dans un défaut d'accessoire, ce n'est pas la réclamation mais une cause non identifiée qui revient à la commande suivante. La première partie détaille les 72 heures suivant la détection : isoler et arrêter l'usage, recenser les lots et en-cours touchés, informer le fournisseur et les services internes, conserver les preuves, puis décider d'une relance de production pour tenir le délai. Inverser cet ordre détruit les preuves. La deuxième applique les huit étapes du 8D aux accessoires, avec un tableau du livrable attendu, de la version purement formelle et de l'exigence vérifiable. La troisième montre comment quantifier l'énoncé du problème : 5W2H plus position du défaut, proportion et écart mesuré, pour que les deux parties puissent vérifier. La quatrième présente trois outils d'analyse — 5 pourquoi, diagramme causes-effets, comparaison bon lot / mauvais lot — et les causes les plus fréquentes : changement de lot de fil ou de papier, réglages d'encre et de colle, usure de forme, tension de couture, contamination au stockage. La cinquième traite la clôture : trois lots consécutifs de données, réessai des échantillons conservés, clôture écrite et mise à jour du contrôle réception.",
        sum_es="Lo caro de un defecto de accesorios no es la reclamación, sino una causa sin identificar que reaparece en el siguiente pedido. La primera parte detalla las 72 horas posteriores a la detección: aislar y detener el uso, contar lotes afectados y producto en curso, avisar al proveedor y a las áreas internas, registrar pruebas y decidir si hace falta una reposición para salvar la fecha. Alterar ese orden destruye las pruebas. La segunda aplica las ocho etapas del 8D a los accesorios con una tabla del entregable de cada etapa, la versión puramente formal y el requisito verificable. La tercera muestra cómo cuantificar el enunciado del problema: 5W2H más posición del defecto, proporción y desviación medida, para que ambas partes puedan comprobarlo. La cuarta cubre tres herramientas de causa raíz —5 porqués, diagrama causa-efecto y comparación lote bueno/malo— y las causas más habituales: cambio de lote de hilo o papel, ajustes de tinta y adhesivo, desgaste del troquel, tensión de costura y contaminación en almacén. La quinta trata el cierre: tres lotes consecutivos de datos, reensayo de muestras conservadas, cierre por escrito y actualización del control de recepción.",
    ),
]
