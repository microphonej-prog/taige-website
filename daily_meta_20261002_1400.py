#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-02 下午（14:00）每日更新：2 篇新文章元数据（六语：zh-Hant 根 / en / ja / ko / fr / es）

选题说明（30 项主题池与历次扩展选题均已上线，本次沿「吊牌印刷生产工程」与
「汉服／新中式」两个尚未覆盖的方向扩展，已核对 blog/、en|ja|ko|fr|es/blog/ 与 sitemap.xml 无重复）：

- hang-tag-imposition-yield-guide vs hang-tag-die-cutting-guide（后者讲刀模与异形外形本身）、
  hang-tag-moq-cost（起订量与成本构成）、garment-trims-cost-saving-guide（降本八方向，仅在
  「方向三：拼版与套版」一段提到拼版概念，无开纸/咬口/出血/纹向/利用率计算/孔位留边等内容）。
  本文聚焦印刷生产工程：开纸与咬口、出血与安全线、纹向、净面积利用率算例、混拼套版边界、
  异形刀模与孔位限制、拼版如何决定起订量与交期。
- hanfu-new-chinese-style-trims-guide vs suiting-formalwear-trims-guide、bridal-eveningwear-trims-guide、
  woven-label-material-guide、care-label-fabric-content（均为通用或其它品类）。全站此前 0 篇涉及
  汉服／新中式（grep 汉服/新中式/旗袍/盘扣/立领/国风 均无命中）。本文聚焦系带规格与色牢度、
  盘扣手工与机制的成本与验证、标签隐藏式做法、形制+尺码标注、电商礼盒与出口合规。
"""

ARTICLES = [
    dict(
        slug="hang-tag-imposition-yield-guide.html",
        body="blog/_body_imposition.html",
        title_zh="吊牌拼版与纸张利用率指南：开纸、咬口与混拼怎么算 | TAGE",
        title_en="Hang Tag Imposition &amp; Paper Yield Guide: Sheet Layout, Gripper, Mixed Runs | TAGE",
        title_ja="タグの面付けと紙取り歩留まりガイド：くわえ・塗り足し・混在面付け | TAGE",
        title_ko="행택 판걸이·용지 수율 가이드: 재단 규격, 그리퍼, 혼합 판걸이 | TAGE",
        title_fr="Imposition et rendement papier des étiquettes suspendues : calage et mélange | TAGE",
        title_es="Imposición y rendimiento de papel en etiquetas colgantes: calado y mezcla | TAGE",
        desc_zh="吊牌拼版与纸张利用率指南：讲清开纸尺寸、咬口、出血、安全线与纸张纹向如何影响单价，用两组数据算清净面积利用率，说明混拼套版省钱的边界、异形刀模与孔位的限制，以及起订量与交期怎么被一版拼数决定，附可直接填写的询价清单。东莞泰阁包装。",
        desc_en="How hang tag imposition drives unit price: sheet formats, gripper, bleed, grain, yield maths, mixed runs, die limits, MOQ and lead time. TAGE Packaging.",
        desc_ja="タグの面付けと歩留まりガイド。紙取り、くわえ代、塗り足し、安全余白、紙の目が単価に与える影響、2 通りの紙取りによる歩留まり計算、混在面付けの限界、異形抜きと穴位置の制約、最低発注量と納期の決まり方、見積り用チェックリスト。東莞泰閣包装。",
        desc_ko="행택 판걸이와 용지 수율 가이드. 재단 규격, 그리퍼, 도련, 안전 여백, 종이 결이 단가에 미치는 영향, 두 규격 비교 수율 계산, 혼합 판걸이의 한계, 이형 도형과 구멍 위치 제약, 최소 주문량과 납기 결정 방식, 견적 체크리스트 정리. 둥관 TAGE 패키징.",
        desc_fr="Imposition des étiquettes suspendues : formats de feuille, taquet de prise, fond perdu, sens du papier, calcul du rendement, imposition mixte et limites de découpe.",
        desc_es="Imposición de etiquetas colgantes: formatos de hoja, pinza, sangrado, dirección de fibra, cálculo del rendimiento, imposición mixta y límites del troquel.",
        crumb_zh="吊牌拼版与利用率",
        crumb_en="Tag Imposition &amp; Yield",
        crumb_ja="タグの面付けと歩留まり",
        crumb_ko="행택 판걸이와 수율",
        crumb_fr="Imposition et rendement",
        crumb_es="Imposición y rendimiento",
        h1_zh="吊牌拼版与纸张利用率指南：开纸、咬口与混拼怎么算",
        h1_en="Hang Tag Imposition and Paper Yield: Sheet Format, Gripper and Mixed Runs",
        h1_ja="タグの面付けと紙取り歩留まりガイド：くわえ・塗り足し・混在面付けの考え方",
        h1_ko="행택 판걸이와 용지 수율 가이드: 재단 규격, 그리퍼, 혼합 판걸이 계산",
        h1_fr="Imposition et rendement papier des étiquettes suspendues : format, calage et mélange",
        h1_es="Imposición y rendimiento de papel en etiquetas colgantes: formato, calado y mezcla",
        tag_zh="吊牌印刷", tag_en="Tag Printing", tag_ja="タグ印刷", tag_ko="행택 인쇄",
        tag_fr="Impression", tag_es="Impresión",
        sum_zh="同一款吊牌，换一种开纸或排版方向，纸耗可能差一成以上。本文把拼版怎么决定单价讲透：开纸尺寸、咬口、出血、安全线与纸张纹向各自占用多少，净面积利用率怎么用两组数据算出来，为什么大纸不一定更省，异形的外接矩形为什么要多留 5–15%，混拼套版能摊薄开机费与制版费但有哪三个前提，刀线间距、圆角与孔位留边对模切的限制，以及起订量下限、补单交期怎么被一版拼数决定。最后给出一张可直接填写的询价清单。",
        sum_en="Change the sheet format or layout direction on the same hang tag and paper consumption can shift by more than ten per cent. This guide explains how imposition sets the unit price: what sheet format, gripper margin, bleed, safety margin and grain each cost you, how to compute net yield from two sets of numbers, why a bigger sheet is not automatically cheaper, why shaped tags cost 5-15% more than their bounding rectangle suggests, the three conditions for mixing versions on one sheet, how rule spacing, corner radius and hole distance limit die-cutting, and how MOQ and reorder lead time follow from pieces per sheet.",
        sum_ja="同じタグでも紙取りや並べる向きを変えるだけで紙の使用量が一割以上変わります。本記事は面付けが単価をどう決めるかを解説します。紙取り、くわえ代、塗り足し、安全余白、紙の目がそれぞれ何を消費するか、二つの数字から正味歩留まりを出す方法、紙が大きいほど得とは限らない理由、異形が外接矩形比で 5〜15% 不利になる理由、混在面付けの三つの条件、刃間隔・角の丸み・穴位置が抜き加工に与える制約、最低発注量と追加発注の納期が 1 版の個数で決まる仕組み、そして記入できる見積りチェックリストまでを整理します。",
        sum_ko="같은 행택이라도 재단 규격이나 배열 방향을 바꾸면 종이 사용량이 10% 이상 달라집니다. 이 글은 판걸이가 단가를 어떻게 결정하는지 설명합니다. 재단 규격, 그리퍼 여유, 도련, 안전 여백, 종이 결이 각각 무엇을 소모하는지, 두 가지 수치로 순 수율을 계산하는 방법, 종이가 크다고 유리하지 않은 이유, 이형이 외접 사각형보다 5~15% 불리한 이유, 혼합 판걸이의 세 가지 조건, 칼선 간격·라운드·구멍 위치가 도형에 주는 제약, 최소 주문량과 추가 주문 납기가 판당 개수로 결정되는 구조, 그리고 바로 작성할 수 있는 견적 체크리스트를 정리합니다.",
        sum_fr="Pour une même étiquette, changer le format de feuille ou le sens de calage peut faire varier la consommation de papier de plus de dix pour cent. Ce guide explique comment l'imposition fixe le prix unitaire : ce que coûtent format, taquet de prise, fond perdu, marge de sécurité et sens du papier, le calcul du rendement net à partir de deux jeux de chiffres, pourquoi une feuille plus grande n'est pas forcément plus économique, pourquoi une forme coûte 5 à 15 % de plus que son rectangle, les trois conditions d'une imposition mixte et l'effet de l'espacement des règles et des trous.",
        sum_es="En la misma etiqueta, cambiar el formato de hoja o el sentido de maquetación puede variar el consumo de papel más de un diez por ciento. Esta guía explica cómo la imposición fija el precio unitario: qué cuestan el formato, la pinza, el sangrado, el margen de seguridad y la fibra, cómo calcular el rendimiento neto con dos juegos de cifras, por qué una hoja mayor no siempre es más económica, por qué una forma cuesta un 5-15 % más que su rectángulo y las tres condiciones de la imposición mixta.",
    ),
    dict(
        slug="hanfu-new-chinese-style-trims-guide.html",
        body="blog/_body_hanfu.html",
        title_zh="汉服与新中式服装辅料指南：盘扣、系带、织唛与吊牌 | TAGE",
        title_en="Hanfu &amp; New Chinese Style Trims Guide: Frog Buttons, Ties, Labels | TAGE",
        title_ja="漢服・新中式の副資材ガイド：盤扣・組みひも・織ラベル・タグ | TAGE",
        title_ko="한푸·뉴차이니즈 부자재 가이드: 매듭단추·끈·직조 라벨·행택 | TAGE",
        title_fr="Accessoires hanfu et style néo-chinois : boutons cordelière, liens, labels | TAGE",
        title_es="Accesorios para hanfu y estilo neochino: botones de nudo, cordones y etiquetas | TAGE",
        desc_zh="汉服与新中式服装辅料指南：真丝、提花缎与织锦的系带宽度与色牢度怎么定，盘扣手工与机制的成本差别、扣脚与扣眼的验证要点，主嘜与洗水标怎么藏在里衬里，尺码标要不要同时标形制与通袖长，以及电商礼盒包装与出口合规要求。东莞泰阁包装。",
        desc_en="Hanfu and new-Chinese trims: tie width and colourfastness, hand vs machine frog buttons, hidden labels, silhouette sizing, gift packing and export rules.",
        desc_ja="漢服・新中式の副資材ガイド。シルク・ジャカード・ブロケードの組みひも幅と染色堅牢度、手作りと機械製の盤扣のコスト差、首とループの検証、裏地に隠すラベル設計、形制と袖丈のサイズ表記、ギフト包装と輸出コンプライアンスを整理。東莞泰閣包装。",
        desc_ko="한푸·뉴차이니즈 부자재 가이드. 실크·자카드·브로케이드의 끈 폭과 염색 견뢰도, 수작업과 기계 제작 매듭단추의 비용 차이, 목과 고리 검증, 안감에 숨기는 라벨 설계, 형식과 소매 총장 사이즈 표기, 선물 포장과 수출 규제를 정리했습니다. 둥관 TAGE 패키징.",
        desc_fr="Accessoires hanfu et néo-chinois : largeur et solidité des liens, boutons cordelière main ou machine, labels cachés, tailles avec coupe, coffret et conformité export.",
        desc_es="Accesorios hanfu y neochinos: ancho y solidez de cordones, botones de nudo a mano o a máquina, etiquetas ocultas, tallas con corte, empaque de regalo y cumplimiento de exportación.",
        crumb_zh="汉服与新中式辅料",
        crumb_en="Hanfu &amp; New Chinese Trims",
        crumb_ja="漢服・新中式の副資材",
        crumb_ko="한푸·뉴차이니즈 부자재",
        crumb_fr="Hanfu et néo-chinois",
        crumb_es="Hanfu y neochino",
        h1_zh="汉服与新中式服装辅料指南：盘扣、系带、织唛与吊牌怎么选",
        h1_en="Hanfu and New Chinese Style Trims: Frog Buttons, Ties, Woven Labels and Hang Tags",
        h1_ja="漢服・新中式の副資材ガイド：盤扣・組みひも・織ラベル・タグの選び方",
        h1_ko="한푸·뉴차이니즈 의류 부자재 가이드: 매듭단추, 끈, 직조 라벨, 행택 선택",
        h1_fr="Accessoires pour hanfu et style néo-chinois : boutons cordelière, liens, labels et étiquettes",
        h1_es="Accesorios para hanfu y estilo neochino: botones de nudo, cordones, etiquetas tejidas y colgantes",
        tag_zh="汉服与新中式", tag_en="Hanfu &amp; New Chinese", tag_ja="漢服・新中式", tag_ko="한푸·뉴차이니즈",
        tag_fr="Hanfu", tag_es="Hanfu",
        sum_zh="汉服与新中式的辅料不能用常规时装的做法：真丝、提花缎与织锦怕刮怕压，盘扣与系带大量依赖手工，标签还得藏进里衬。本文给出系带的宽度、材质、配对长度与色牢度对照表，讲清深色系带染到浅色中衣这个最高频投诉怎么防；分析手工盘扣与机制扣的成本与交期差别，扣脚高度与扣眼开合的验证方法；说明主嘜、洗水标怎么藏、必须标什么、多语言怎么组合；解释为什么尺码要形制与通袖长一起标，吊牌为何不宜大面积覆膜；最后给出电商礼盒的分层顺序与出口合规、询价清单。",
        sum_en="Hanfu and new-Chinese garments cannot use ordinary fashion practice for their trims: silk, jacquard satin and brocade are easily marked, frog buttons and ties rely on hand-work, and labels must disappear into the lining. This guide tabulates tie width, material, paired length and colourfastness, and shows how to prevent the most common complaint — a dark tie staining a pale inner layer. It compares hand-made and machine frog buttons on cost and lead time, explains how to validate shank height and loop opening, covers how neck and care labels stay hidden and what they must state, why size labels should carry silhouette and sleeve span together, and closes with gift-box layering, export compliance and an enquiry checklist.",
        sum_ja="漢服・新中式の副資材は一般ファッションのやり方では通用しません。シルクやジャカードサテン、ブロケードは擦れや圧迫に弱く、盤扣や組みひもは手作業に依存し、ラベルは裏地に隠す必要があります。本記事は組みひもの幅・素材・左右の長さ・染色堅牢度を表にまとめ、濃色のひもが淡色の中衣に色移りする最多のクレームをどう防ぐかを解説します。手作りと機械製の盤扣をコストと納期で比較し、首の高さとループの検証方法、ラベルの隠し方と必須表示、サイズに形制と袖丈を併記する理由、ギフト包装の層構成と輸出要件、見積りチェックリストまでを整理します。",
        sum_ko="한푸와 뉴차이니즈 부자재는 일반 패션 방식으로 접근할 수 없습니다. 실크, 자카드 새틴, 브로케이드는 눌림과 긁힘에 약하고, 매듭단추와 끈은 수작업 의존도가 높으며, 라벨은 안감에 숨겨야 합니다. 이 글은 끈의 폭·소재·좌우 길이·염색 견뢰도를 표로 정리하고, 어두운 끈이 밝은 속옷에 이염되는 가장 흔한 클레임을 막는 방법을 설명합니다. 수작업과 기계 제작 매듭단추를 비용과 납기로 비교하고, 목 높이와 고리 개폐 검증, 라벨을 숨기는 방법과 필수 표기, 사이즈에 형식과 소매 총장을 함께 적는 이유, 선물 상자 층 구성과 수출 요건, 견적 체크리스트까지 다룹니다.",
        sum_fr="Le hanfu et le néo-chinois n'acceptent pas les pratiques de la mode classique : soie, satin jacquard et brocart se marquent, boutons cordelière et liens dépendent de la main, et les étiquettes doivent disparaître dans la doublure. Ce guide met en tableau largeur, matière, longueur appariée et solidité des liens, et montre comment éviter le litige le plus fréquent : un lien foncé qui tache une sous-couche claire. Il compare boutons faits main et mécaniques en coût et délai, détaille la validation du pied et de la boucle, la dissimulation et le contenu obligatoire des étiquettes, la mention conjointe de la coupe et de l'envergure, puis l'emballage cadeau et la conformité export.",
        sum_es="El hanfu y el estilo neochino no admiten las prácticas de la moda convencional: la seda, el satén jacquard y el brocado se marcan, los botones de nudo y los cordones dependen de la mano y las etiquetas deben desaparecer en el forro. Esta guía tabula ancho, material, largo parejo y solidez de los cordones, y muestra cómo evitar la reclamación más frecuente: un cordón oscuro que mancha una capa interior clara. Compara botones hechos a mano y a máquina en coste y plazo, detalla la validación del pie y la presilla, el ocultamiento y contenido obligatorio de las etiquetas, la mención conjunta de corte y envergadura, y cierra con el empaque de regalo y el cumplimiento de exportación.",
    ),
]
