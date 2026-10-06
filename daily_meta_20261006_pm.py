#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-06 下午批次（14:00）每日更新：2 篇新文章元数据（六语：zh-Hant 根 / en / ja / ko / fr / es）

选题说明（主题池 30 项与历次扩展均已上线，本次沿「珠钻工艺辅料」与「罗纹领口/袖口」
两个尚未独立成文的方向扩展，已核对 blog/、en|ja|ko|fr|es/blog/ 与 sitemap.xml 无重复，
并 grep 全站确认关键词覆盖情况：

- sequin-rhinestone-trims-guide  vs bridal-eveningwear-trims-guide（只在礼服语境里提到珠片亮片，未讲工艺）、
  hang-tag-special-effects-guide（讲吊牌烫金压纹，不是服装上的珠钻）、
  care-label-wash-durability（只讲洗水标自身掉字）；
  全站 grep「珠片」仅 bridal 1 处、「亮片」仅 1 处、「烫钻」「水钻」「烫片膜」0 处：
  本文讲清缝制珠片 / 烫片膜 / 烫钻 / 玻璃珠管四类的材质与固定方式差别、
  缝制与烫贴按面料与洗护方式的取舍（含童装小部件安全）、130–170 °C 烫压三件套与冷却、
  水洗（ISO 6330 40 °C）与干洗牢度验证，以及掉片率、位置图、材质书面化、验针留样的验收清单。
- rib-knit-collar-cuff-guide   vs knitwear-sweater-trims-guide（讲主唛/洗水标/包装，不讲罗纹本体）、
  elastic-trims-selection-guide（讲松紧带与弹力辅料，不是针织罗纹）、lace-trimming-guide（蕾丝）；
  全站 grep「罗纹」0 处、word-boundary「rib knit / ribbed」仅 lace 与 loungewear 各一处顺带提及：
  本文讲清 1×1 / 2×2 罗纹与横机、圆机罗纹的分型、成分与 3–8% 氨纶含量如何决定寿命、
  克重门幅缩水率与弹性回复率的写法、拉量与缝型与定型的关键动作，并给出对色、交货形态与留样验收口径。
"""

ARTICLES = [
    dict(
        slug="sequin-rhinestone-trims-guide.html",
        body="blog/_body_sequin.html",
        title_zh="珠片、亮片与烫钻辅料指南：缝制、烫贴与牢度验收 | TAGE",
        title_en="Sequins and Rhinestones Trim Guide: Sewn or Heat-Pressed | TAGE",
        title_ja="スパンコール・ラインストーン副資材ガイド：縫製と熱圧着の選び方 | TAGE",
        title_ko="시퀸·라인스톤 부자재 가이드: 봉제와 열압착, 내구 검수 | TAGE",
        title_fr="Guide sequins et strass : couture ou thermocollage | TAGE",
        title_es="Guía de sequins y pedrería: cosido o termoadhesivo | TAGE",
        desc_zh="珠片、亮片与烫钻辅料指南：分清缝制珠片、烫片膜、烫钻与玻璃珠管的工艺差别，讲清按面料与洗护方式在缝制、烫贴之间的取舍、130–170 °C 烫压三要素与冷却要求、水洗与干洗牢度验证，以及掉片率、位置图、验针留样的验收口径。来自东莞泰阁包装。",
        desc_en="Sequins and rhinestone trims: sewn sequins, hot-fix film, pressed stones and beads compared, chosen by fabric and care, press settings and wash testing.",
        desc_ja="スパンコール・ラインストーンの副資材ガイド。縫製スパンコール、ホットフィックスフィルム、熱圧着ストーン、ガラスビーズの違い、生地と洗濯方法による縫製と圧着の選択、130～170 °C のプレス条件、洗濯とドライの耐久検証、脱落率と検収基準を解説。東莞泰閣包装。",
        desc_ko="시퀸·라인스톤 부자재 가이드. 봉제 시퀸, 핫픽스 필름, 열압착 스톤, 유리 비즈의 차이와 원단·세탁 방식에 따른 봉제와 압착 선택, 130~170°C 프레스 조건, 세탁·드라이 내구 검증, 탈락률과 검수 기준을 정리했습니다. 둥관 TAGE 패키징.",
        desc_fr="Guide des sequins et strass : sequins cousus, film thermocollant, strass pressés et perles de verre comparés, choix selon le tissu et l'entretien, réglages de presse et tenue au lavage.",
        desc_es="Guía de sequins y pedrería: sequins cosidos, film termoadhesivo, piezas prensadas y cuentas de vidrio, elección según tejido y cuidado, ajustes de prensa y resistencia al lavado.",
        crumb_zh="珠钻辅料指南",
        crumb_en="Bead and Stone Trims",
        crumb_ja="ビーズ・ストーン副資材",
        crumb_ko="비즈·스톤 부자재",
        crumb_fr="Perles et strass",
        crumb_es="Cuentas y pedrería",
        h1_zh="珠片、亮片与烫钻辅料指南：缝制、烫贴与牢度验收",
        h1_en="Sequins and Rhinestones Guide: Sewing, Heat-Press and Durability",
        h1_ja="スパンコール・ラインストーンの副資材ガイド：縫製・熱圧着・耐久検証",
        h1_ko="시퀸·라인스톤 부자재 가이드: 봉제·열압착·내구 검수",
        h1_fr="Sequins, paillettes et strass : couture, thermocollage et tenue",
        h1_es="Sequins, lentejuelas y pedrería: cosido, termoadhesivo y resistencia",
        tag_zh="工艺指南",
        tag_en="Process Guide",
        tag_ja="加工ガイド",
        tag_ko="공정 가이드",
        tag_fr="Guide des procédés",
        tag_es="Guía de procesos",
        sum_zh="珠片、亮片与烫钻的固定方式其实是三套工艺：珠片靠线缝或预排在热熔胶膜上烫贴，烫钻靠胶背烫压，玻璃珠管多数要手工钉。本文讲清四类材质的差别与各自风险，给出按面料与洗护方式在缝制、烫贴之间的判断顺序，说明 130–170 °C 的烫压温度、压力、时间与冷却要求，并给出水洗与干洗牢度的验证方法、掉片率与位置图等可直接写进询价单的验收口径。",
        sum_en="Sequins, glitter film and rhinestones are fixed by three different processes: sewing or hot-fix film, glue-backed pressing, and hand beading. This guide separates the four material families and their risks, gives a decision order between sewing and pressing based on fabric and care, covers the 130–170 °C heat, pressure, time and cooling trio, then the wash and dry-clean durability tests and the acceptance criteria you can paste into a quotation request.",
        sum_ja="スパンコール、グリッター、ラインストーンの固定方法は大きく3系統です。縫製またはホットフィックスフィルム、接着剤背面の熱圧着、そして手縫いのビーズ。本記事は4素材の違いとリスクを整理し、生地と洗濯方法から縫製と圧着を選ぶ判断順序、130～170 °C の温度・圧力・時間・冷却、洗濯とドライの耐久試験、脱落率や位置図など見積依頼に書ける検収基準を示します。",
        sum_ko="시퀸, 글리터, 라인스톤의 고정 방식은 크게 세 가지입니다. 봉제 또는 핫픽스 필름, 접착제 백 열압착, 그리고 수작업 비즈. 이 글은 네 가지 소재의 차이와 리스크를 정리하고, 원단과 세탁 방식에 따른 봉제·압착 선택 순서, 130~170°C의 온도·압력·시간·냉각, 세탁과 드라이 내구 시험, 탈락률과 위치 도면 등 견적 요청서에 쓸 수 있는 검수 기준을 제시합니다.",
        sum_fr="La fixation des sequins, paillettes et strass relève de trois procédés : couture ou film thermocollant, pressage sur dos encollé, et perlage main. Ce guide distingue les quatre familles et leurs risques, donne un ordre de décision entre couture et thermocollage selon le tissu et l'entretien, détaille le trio 130–170 °C (température, pression, temps) et le refroidissement, puis les essais de tenue au lavage et au nettoyage à sec et les critères de réception.",
        sum_es="La fijación de sequins, lentejuelas y pedrería responde a tres procesos: cosido o film termoadhesivo, prensado sobre respaldo encolado y bordado a mano. Esta guía distingue las cuatro familias y sus riesgos, ofrece un orden de decisión entre cosido y termoadhesivo según tejido y cuidado, detalla el trío de 130–170 °C (temperatura, presión y tiempo) con el enfriado, y los ensayos de lavado y limpieza en seco y los criterios de recepción.",
    ),
    dict(
        slug="rib-knit-collar-cuff-guide.html",
        body="blog/_body_ribknit.html",
        title_zh="罗纹领口与袖口辅料指南：1×1、2×2、弹性回复与验收 | TAGE",
        title_en="Rib Knit Collar, Cuff and Hem Guide: 1x1, 2x2 and Recovery | TAGE",
        title_ja="リブ衿・袖口・裾の副資材ガイド：1×1・2×2・伸び回復と検収 | TAGE",
        title_ko="리브 목선·소매끝·밑단 부자재 가이드: 1×1, 2×2, 회복 검수 | TAGE",
        title_fr="Guide des côtes : encolure, poignets et bas, 1x1 et 2x2 | TAGE",
        title_es="Guía del canalé: escote, puños y bajo, 1x1 y 2x2 | TAGE",
        desc_zh="罗纹领口与袖口辅料指南：讲清 1×1、2×2 与横机、圆机罗纹的分型，成分与 3–8% 氨纶含量如何决定领口寿命，克重、门幅、缩水率与弹性回复率怎么写，拉量、缝型与定型的关键动作，以及对色、交货形态与留样的验收口径。来自东莞泰阁包装。",
        desc_en="Rib knit collar and cuff guide: 1x1 versus 2x2, flat-bed versus circular, elastane content, weight and shrinkage, take-up and setting, and acceptance criteria.",
        desc_ja="リブ衿・袖口・裾の副資材ガイド。1×1 と 2×2、横編みと丸編みの違い、組成と3～8% のスパンデックス率が衿の寿命を決める理由、目付・幅・収縮率・伸び回復率の書き方、縫い込み量と縫い形式とセットの要点、対色と納入形態とサンプル保管の基準を解説。東莞泰閣包装。",
        desc_ko="리브 목선·소매끝·밑단 부자재 가이드. 1×1과 2×2, 횡편과 환편의 차이, 조성과 3~8% 스판덱스 함량이 목선 수명을 결정하는 이유, 중량·폭·수축률·신축 회복률 표기, 이입량과 솔기와 세팅의 핵심, 대조 색상과 납품 형태와 샘플 보관 기준을 정리했습니다. 둥관 TAGE 패키징.",
        desc_fr="Guide des côtes d'encolure, poignets et bas : 1x1 contre 2x2, rectiligne ou circulaire, taux d'élasthanne, grammage et retrait, entraînement et fixation, critères de réception.",
        desc_es="Guía del canalé de escote, puños y bajo: 1x1 frente a 2x2, rectilínea o circular, contenido de elastano, gramaje y encogimiento, embebido y fijación, criterios de recepción.",
        crumb_zh="罗纹辅料指南",
        crumb_en="Rib Knit Trims",
        crumb_ja="リブ副資材",
        crumb_ko="리브 부자재",
        crumb_fr="Côtes et bords",
        crumb_es="Canalé y bordes",
        h1_zh="罗纹领口与袖口辅料指南：1×1、2×2、弹性回复与验收",
        h1_en="Rib Knit Collar and Cuff Guide: 1x1, 2x2, Recovery and Tolerances",
        h1_ja="リブ衿・袖口・裾の副資材ガイド：1×1・2×2・伸び回復と検収",
        h1_ko="리브 목선·소매끝·밑단 부자재 가이드: 1×1, 2×2, 신축 회복과 검수",
        h1_fr="Côtes d'encolure et poignets : 1x1, 2x2, reprise élastique et réception",
        h1_es="Canalé de escote y puños: 1x1, 2x2, recuperación elástica y recepción",
        tag_zh="工艺指南",
        tag_en="Process Guide",
        tag_ja="加工ガイド",
        tag_ko="공정 가이드",
        tag_fr="Guide des procédés",
        tag_es="Guía de procesos",
        sum_zh="罗纹是针织服装的骨架，领口会不会越穿越松、袖口能不能回弹、下摆会不会变喇叭形都由它决定。本文讲清 1×1、2×2 与横机、圆机罗纹的分型与取舍，说明决定寿命的是氨纶含量与织造张力而不是克重，给出 3–8% 氨纶的分配逻辑，并讲透克重、门幅、缩水率、弹性回复率的写法，以及拉量、缝型、定型三处最容易做错的地方，附对色、交货形态与留样的验收清单。",
        sum_en="Rib is the skeleton of a knitted garment: it decides whether the neckline opens with wear, whether cuffs recover and whether a hem flares. This guide sets out 1x1 and 2x2 rib against flat-bed and circular knitting, explains why elastane content and knitting tension — not weight — govern service life, gives the logic behind 3–8% elastane, covers how to write weight, width, shrinkage and elastic recovery, and the three places where sewing goes wrong: take-up, seam type and setting, closing with colour matching, delivery form and retained samples.",
        sum_ja="リブはニット衣料の骨格であり、衿が伸びるか、袖口が戻るか、裾がフレアになるかを決めます。本記事は 1×1・2×2 と横編み・丸編みの違いと使い分け、寿命を決めるのが目付ではなくスパンデックス率と編み立て張力である理由、3～8% の配分の考え方、目付・幅・収縮率・伸び回復率の書き方、そして縫い込み量・縫い形式・セットという失敗しやすい3点を解説し、対色と納入形態とサンプル保管の検収リストを添えます。",
        sum_ko="리브는 니트 의류의 골격으로 목선이 늘어나는지, 소매끝이 돌아오는지, 밑단이 플레어가 되는지를 결정합니다. 이 글은 1×1·2×2와 횡편·환편의 차이와 선택, 수명을 결정하는 것이 중량이 아니라 스판덱스 함량과 편성 장력이라는 점, 3~8% 배분 논리, 중량·폭·수축률·신축 회복률 표기법, 그리고 이입량·솔기·세팅 세 가지 실수 지점을 다루고 대조 색상·납품 형태·샘플 보관 검수 목록을 제공합니다.",
        sum_fr="La côte est la charpente du tricot : elle décide si l'encolure s'ouvre, si les poignets reprennent et si le bas s'évase. Ce guide compare la côte 1x1 et 2x2, le tricotage rectiligne et circulaire, explique pourquoi le taux d'élasthanne et la tension — et non le grammage — gouvernent la durée de vie, donne la logique du 3–8 %, la rédaction du grammage, de la largeur, du retrait et de la reprise, et les trois points où la couture échoue : entraînement, type de point et fixation, avec l'appariement couleur, la forme de livraison et les échantillons.",
        sum_es="El canalé es el esqueleto de la prenda de punto: decide si el escote se abre, si los puños recuperan y si el bajo se convierte en vuelo. Esta guía compara el canalé 1x1 y 2x2 con la tricotosa rectilínea y circular, explica por qué el elastano y la tensión —no el gramaje— rigen la vida útil, da la lógica del 3–8 %, cómo redactar gramaje, ancho, encogimiento y recuperación, y los tres puntos donde falla la confección: embebido, tipo de puntada y fijación, cerrando con igualado de color, forma de entrega y muestras conservadas.",
    ),
]
