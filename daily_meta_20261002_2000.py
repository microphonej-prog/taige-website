#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-02 晚批次（20:00）每日更新：2 篇新文章元数据（六语：zh-Hant 根 / en / ja / ko / fr / es）

选题说明（30 项主题池与历次扩展选题均已上线，本次沿「弹性辅料」与「纽扣/金属扣件」两个
尚未覆盖的辅料品类扩展，已核对 blog/、en|ja|ko|fr|es/blog/ 与 sitemap.xml 无重复，
并 grep 全站确认 松紧带 / 包边带 / 罗纹 / 四合扣 / 气眼 / 铆钉 命中均为 0 或个别文章
一笔带过的清单式提及，无专文）：

- elastic-trims-selection-guide vs swimwear-activewear-trims-guide、underwear-label-guide、
  sock-hosiery-trims-guide、loungewear-pajama-trims-guide（品类指南，仅提及松紧带/罗纹，
  无宽度-倍率-回弹-耐洗的参数体系、五类结构对照表、领口罗纹裁片系数、预拉伸缝合 5–10%、
  波浪边与色迁移的成因表）、garment-trims-fabric-compatibility-guide（讲辅料与面料缩率色差，
  不涉及弹性件参数与缝制）。本文聚焦弹性辅料选型与缝制验收。
- garment-buttons-fasteners-guide vs smoke：全站无纽扣/金属扣件专文。hang-tag-metal-hardware-guide
  讲的是吊牌上的金属件（鸡眼、别针、吊粒），metal-trims-nickel-release-guide 专讲镍释放测试，
  garment-spare-button-bag-guide 讲备用扣袋配置，clothing-label-children-safety 讲标签安全；
  本文是扣件本体选型：材质对照表、按扣开合力与扣径匹配、镀层与牛仔后处理、儿童扣件安全、
  化学限值口径与询价清单。
"""

ARTICLES = [
    dict(
        slug="elastic-trims-selection-guide.html",
        body="blog/_body_elastic.html",
        title_zh="弹性辅料选型指南：松紧带、罗纹、包边带与弹力织带怎么选 | TAGE",
        title_en="Elastic Trims Guide: Elastic Band, Rib, Binding Tape and Webbing | TAGE",
        title_ja="伸縮性副資材ガイド：ゴムテープ・リブ・パイピング・伸縮テープの選び方 | TAGE",
        title_ko="신축성 부자재 가이드: 고무밴드·리브·바이어스·스트레치 웨빙 선택 | TAGE",
        title_fr="Guide des accessoires élastiques : élastique, côtes et biais | TAGE",
        title_es="Guía de accesorios elásticos: elástico, canalé y bies | TAGE",
        desc_zh="弹性辅料选型指南：讲清松紧带、罗纹、包边带与弹力织带的宽度、拉伸倍率、回弹率与耐洗要求，用对照表列出五类松紧带的适用部位，分析领口罗纹裁片系数、预拉伸缝合、波浪边与色迁移等问题的成因与处理，并附可直接填写的询价清单。东莞泰阁包装。",
        desc_en="Elastic trims guide: width, stretch ratio, recovery and wash life for elastic band, rib, binding tape and webbing, plus common faults. TAGE Packaging.",
        desc_ja="伸縮性副資材の選び方ガイド。ゴムテープ・リブ・パイピング・伸縮テープの幅、伸長倍率、回復率、耐洗濯性を整理し、五つのゴム構造の用途比較表、襟リブの裁断係数、予備伸長の縫製、波打ちや色移りの原因と対処、見積りチェックリストを掲載。東莞泰閣包装。",
        desc_ko="신축성 부자재 선택 가이드. 고무밴드, 리브, 바이어스 테이프, 스트레치 웨빙의 폭·신장 배율·회복률·세탁 내구성을 정리하고, 다섯 가지 고무 구조의 용도 비교표, 목 리브 재단 계수, 예비 신장 봉제, 물결과 이염의 원인과 대응, 견적 체크리스트를 담았습니다. 둥관 TAGE 패키징.",
        desc_fr="Guide des accessoires élastiques : largeur, allongement, récupération et tenue au lavage de l'élastique, des côtes, du biais et de la sangle stretch, avec les défauts courants et leurs solutions.",
        desc_es="Guía de accesorios elásticos: ancho, alargamiento, recuperación y lavado del elástico, canalé, bies y cinta stretch, con los defectos habituales y su corrección.",
        crumb_zh="弹性辅料选型指南",
        crumb_en="Elastic Trims Guide",
        crumb_ja="伸縮性副資材ガイド",
        crumb_ko="신축성 부자재 가이드",
        crumb_fr="Accessoires élastiques",
        crumb_es="Accesorios elásticos",
        h1_zh="弹性辅料选型指南：松紧带、罗纹、包边带与弹力织带怎么选",
        h1_en="Elastic Trims Selection Guide: Elastic Band, Rib, Binding Tape and Stretch Webbing",
        h1_ja="伸縮性副資材の選び方ガイド：ゴムテープ・リブ・パイピング・伸縮テープ",
        h1_ko="신축성 부자재 선택 가이드: 고무밴드, 리브, 바이어스 테이프, 스트레치 웨빙",
        h1_fr="Guide de choix des accessoires élastiques : élastique, côtes, biais et sangle stretch",
        h1_es="Guía de selección de accesorios elásticos: elástico, canalé, bies y cinta stretch",
        tag_zh="弹性辅料", tag_en="Elastic Trims", tag_ja="伸縮副資材", tag_ko="신축성 부자재",
        tag_fr="Élastiques", tag_es="Elásticos",
        sum_zh="腰头松了、领口大了、包边起了波浪——弹性辅料的问题几乎都在洗后暴露。本文给出五个关键参数（宽度、拉伸倍率、回弹率、耐洗与耐氯、材质手感）的取值逻辑，用对照表比较勾编、梭织、提花、包边与弹力圆绳五类结构的手感与适用部位，讲清罗纹的组织结构、氨纶含量与领口裁片系数，说明斜裁与直裁包边的选择、缝线匹配与 5–10% 预拉伸量，最后列出五类常见问题的成因与处理，并附可直接填写的询价清单。",
        sum_en="A slack waistband, a stretched neckline, a wavy edge — elastic faults nearly always show up after washing. This guide sets out the logic behind five key parameters (width, stretch ratio, recovery, wash and chlorine resistance, material feel), compares crochet-knit, woven, jacquard, bound and round-cord constructions in a table, explains rib structure, spandex content and the neckline cutting factor, covers bias versus straight binding, thread choice and 5-10% pre-stretch, and lists the causes and fixes for five common faults with an enquiry checklist.",
        sum_ja="ウエストの伸び、襟ぐりの開き、縁の波打ち。伸縮性副資材の不具合はほぼ洗濯後に出ます。本記事は幅・伸長倍率・回復率・耐洗濯性・素材風合いという五つのパラメータの考え方を示し、かぎ編み・織り・ジャカード・パイピング・丸ゴムの五構造を用途表で比較し、リブの組織・スパンデックス率・襟の裁断係数、バイアスと直裁ちの使い分け、糸の選定と 5〜10% の予備伸長を解説。五つの不具合の原因と対処、そして見積りチェックリストまで整理します。",
        sum_ko="허리가 늘어나고, 목선이 벌어지고, 가장자리가 물결칩니다. 신축성 부자재의 문제는 거의 세탁 후에 드러납니다. 이 글은 폭·신장 배율·회복률·세탁 내성·소재 촉감이라는 다섯 파라미터의 판단 기준을 제시하고, 크로셰·직조·자카드·바이어스·원형 고무 다섯 구조를 용도표로 비교합니다. 리브 조직과 스판덱스 함량, 목둘레 재단 계수, 바이어스와 직선 재단의 선택, 실 선택과 5~10% 예비 신장, 다섯 가지 불량의 원인과 대응, 견적 체크리스트까지 정리합니다.",
        sum_fr="Une ceinture détendue, une encolure élargie, un bord ondulé : les défauts d'élastique apparaissent presque toujours après lavage. Ce guide expose la logique de cinq paramètres clés (largeur, taux d'allongement, récupération, tenue au lavage et au chlore, toucher), compare en tableau les constructions tricotées, tissées, jacquard, bordées et cordons ronds, détaille la structure des côtes, le taux d'élasthanne et le facteur de coupe d'encolure, puis le choix du biais, du fil et du pré-étirement de 5 à 10 %, avant cinq défauts avec leurs causes et remèdes.",
        sum_es="Cintura floja, escote agrandado, borde ondulado: los fallos de los elásticos casi siempre aparecen tras el lavado. Esta guía expone la lógica de cinco parámetros clave (ancho, alargamiento, recuperación, resistencia a lavado y cloro, tacto del material), compara en tabla las construcciones de punto, tejidas, jacquard, forradas y cordón redondo, detalla la estructura del canalé, el contenido de elastano y el factor de corte del escote, y cubre el bies, el hilo y un pretensado del 5-10 % antes de listar cinco defectos con causas y soluciones.",
    ),
    dict(
        slug="garment-buttons-fasteners-guide.html",
        body="blog/_body_buttons.html",
        title_zh="服装纽扣与金属扣件选型指南：树脂、金属、按扣与气眼怎么选 | TAGE",
        title_en="Buttons and Metal Fasteners Guide: Resin, Metal, Snaps, Eyelets | TAGE",
        title_ja="ボタンと金属金具の選び方ガイド：樹脂・金属・スナップ・ハトメ | TAGE",
        title_ko="단추와 금속 잠금구 선택 가이드: 수지·금속·스냅·아일렛 | TAGE",
        title_fr="Guide des boutons et fermetures métalliques : résine, métal, pressions | TAGE",
        title_es="Guía de botones y herrajes metálicos: resina, metal, automáticos | TAGE",
        desc_zh="服装纽扣与金属扣件选型指南：对比树脂、仿贝壳、金属与包布扣的手感与洗护差异，说明按扣四合扣的开合力与扣径如何匹配面料，讲清气眼铆钉的镀层与耐洗要求、镍释与重金属的合规口径，并给出童装扣件安全要点与询价清单。东莞泰阁包装。",
        desc_en="Garment buttons and metal fasteners: resin, metal, snaps and eyelets compared on feel, care, holding force, plating, nickel release and child safety. TAGE Packaging.",
        desc_ja="ボタンと金属金具の選び方ガイド。樹脂・貝調・金属・布張りボタンの風合いと洗濯適性を比較し、スナップの保持力とサイズの合わせ方、ハトメ・リベットのメッキと耐洗性、ニッケル溶出と重金属の適合、子供服の安全要件、見積りチェックリストを整理。東莞泰閣包装。",
        desc_ko="단추와 금속 잠금구 선택 가이드. 수지·모조 조개·금속·원단 감싼 단추의 촉감과 세탁 적성을 비교하고, 스냅 체결력과 크기 매칭, 아일렛·리벳의 도금과 세탁 내성, 니켈 용출과 중금속 적합성, 아동복 안전 요건, 견적 체크리스트를 정리했습니다. 둥관 TAGE 패키징.",
        desc_fr="Guide des boutons et fermetures métalliques : résine, métal, pressions et œillets comparés sur le toucher, l'entretien, la force de maintien, le revêtement et le relargage du nickel.",
        desc_es="Guía de botones y herrajes metálicos: resina, metal, automáticos y ojales comparados en tacto, cuidado, fuerza de sujeción, baño y liberación de níquel.",
        crumb_zh="纽扣与金属扣件指南",
        crumb_en="Buttons &amp; Fasteners Guide",
        crumb_ja="ボタン・金具ガイド",
        crumb_ko="단추·잠금구 가이드",
        crumb_fr="Boutons et fermetures",
        crumb_es="Botones y herrajes",
        h1_zh="服装纽扣与金属扣件选型指南：树脂、金属、按扣与气眼怎么选",
        h1_en="Garment Buttons and Metal Fasteners: Resin, Metal, Snaps and Eyelets",
        h1_ja="ボタンと金属金具の選び方ガイド：樹脂・金属・スナップ・ハトメ",
        h1_ko="단추와 금속 잠금구 선택 가이드: 수지, 금속, 스냅, 아일렛",
        h1_fr="Guide des boutons et fermetures métalliques : résine, métal, pressions et œillets",
        h1_es="Guía de botones y herrajes metálicos: resina, metal, automáticos y ojales metálicos",
        tag_zh="纽扣与扣件", tag_en="Buttons &amp; Fasteners", tag_ja="ボタン・金具", tag_ko="단추·잠금구",
        tag_fr="Boutons", tag_es="Botones",
        sum_zh="扣件是成衣上最小的部件，却常常是投诉的起点：扣子掉了、按扣开不牢、气眼拉脱、镀层洗后发黑。本文先列出成衣上五类扣件各自的失效点，用对照表比较树脂、仿贝壳、金属、天然材质与包布扣的手感、洗护与合规差异，讲清按扣四合扣按用途定开合力、按面料厚度定扣径的逻辑，说明气眼铆钉的镀层选择、安装工艺与牛仔后处理顺序，梳理童装扣件的抗拉、抗扭与小零件要求，最后给出六项询价清单。",
        sum_en="Fasteners are the smallest parts on a garment and often where complaints start: a button falls off, a snap will not hold, an eyelet pulls out, plating darkens after washing. This guide lists where each of five fastener families fails, compares resin, imitation shell, metal, natural and fabric-covered buttons in a table, sets out how application decides holding force and fabric weight decides stud size, covers plating choice, setting process and denim finishing order, reviews pull, torque and small-parts rules for kidswear, and closes with a six-item enquiry checklist.",
        sum_ja="金具は衣類で最も小さな部品でありながら、クレームの起点になりがちです。ボタンが外れる、スナップが留まらない、ハトメが抜ける、洗濯後にメッキが黒ずむ。本記事は五系統の金具ごとの不具合箇所を整理し、樹脂・貝調・金属・天然素材・布張りボタンを風合い・洗濯・適合の面で表にまとめます。用途で保持力を、生地厚でサイズを決める考え方、メッキの選択、取り付け工程、デニム後加工の順序、子供服の引張・トルク・小物要件、そして六項目の見積りチェックリストまでを扱います。",
        sum_ko="잠금구는 의류에서 가장 작은 부품이지만 클레임의 출발점이 되곤 합니다. 단추가 떨어지고, 스냅이 잠기지 않고, 아일렛이 빠지고, 세탁 후 도금이 검게 변합니다. 이 글은 다섯 계열 잠금구의 취약 지점을 정리하고, 수지·모조 조개·금속·천연·원단 감싼 단추를 촉감·세탁·적합성 면에서 표로 비교합니다. 용도로 체결력을, 원단 두께로 크기를 정하는 기준, 도금 선택과 부착 공정, 데님 후가공 순서, 아동복의 인장·토크·소형 부품 요건, 여섯 항목 견적 체크리스트까지 다룹니다.",
        sum_fr="Les fermetures sont les plus petites pièces d'un vêtement et souvent l'origine des litiges : bouton qui tombe, pression qui ne tient pas, œillet qui s'arrache, revêtement qui noircit. Ce guide recense les points de défaillance des cinq familles, compare en tableau boutons résine, imitation nacre, métal, matières naturelles et recouverts, explique comment l'usage fixe la force de maintien et l'épaisseur du tissu le diamètre, traite le choix du revêtement, la pose et l'ordre de finition du denim, puis les exigences enfant et une liste de six points.",
        sum_es="Los cierres son las piezas más pequeñas de una prenda y a menudo el origen de las reclamaciones: botón que se cae, automático que no sujeta, ojal que se arranca, baño que se oscurece. Esta guía recoge los puntos de fallo de las cinco familias, compara en tabla botones de resina, imitación nácar, metal, materiales naturales y forrados, explica cómo el uso fija la fuerza de sujeción y el grosor del tejido el diámetro, cubre el baño, la colocación y el orden de acabado del denim, y cierra con los requisitos infantiles y una lista de seis puntos.",
    ),
]
