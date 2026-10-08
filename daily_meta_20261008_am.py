#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-08 上午批次（09:00）每日更新：2 篇新文章元数据（六语：zh-Hant 根 / en / ja / ko / fr / es）

选题说明（主题池 30 项与历次扩展均已上线，本次沿两个尚未独立成文的方向扩展，
已核对 blog/、en|ja|ko|fr|es/blog/ 与 sitemap.xml 无重复，并 grep 全站确认关键词覆盖情况：

- felt-fabric-patch-label-guide  vs leather-patch-labels（只讲皮革标）、
  silicone-pvc-labels-guide（只讲硅胶/PVC）、woven-label-embroidery-comparison（织唛与刺绣对比）；
  全站 grep「毛毡」仅 shoulder-pad 1 处（羊毛毡垫肩）、「毛巾绣」「terry」0 处、「贴布绣」0 处：
  本文讲清毛毡标 / 毛巾布标 / 帆布棉布标 / 贴布绣四类布艺标片的材质与风险对比、
  克重与厚度（200–400 g/m²、1–3 mm；8–12 盎司帆布）与边缘处理（激光/热切/包边/锁边）、
  车缝、烫贴与魔术贴背三种固定方式的取舍，洗后缩水（≤3%）、掉毛起球、脱线与掉色迁移的验证，
  以及克重、尺寸公差、色差、小部件与留样的验收口径。
- sun-protective-clothing-label-guide  vs functional-garment-trims-label-guide（功能面料的标签声明，
  仅一句提到 UPF）、care-label-wash-durability（只讲洗水标自身掉字）、
  clothing-label-compliance-eu（通用欧盟标签合规，不涉及防晒声明）；
  全站 grep「防晒」0 处、「UPF」仅 functional 1 处：
  本文讲清 UPF 15/25/40–50+ 的分级与 AATCC 183 / ASTM D6603 / EN 13758-1·2 / AS/NZS 4399 / GB/T 18830
  的方法差异、美欧澳新中的标注门槛（FTC 上限、UVA<5% 硬指标）、洗后 UPF 的保持与洗水标写法、
  防晒服的拉链缝线织带绳带选型与童装绳带安全（EN 14682），以及吊牌包装的传达与合规清单。
"""

ARTICLES = [
    dict(
        slug="felt-fabric-patch-label-guide.html",
        body="blog/_body_felt.html",
        title_zh="毛毡标与布艺贴片指南：材质、固定方式与洗护验收 | TAGE",
        title_en="Felt and Fabric Patch Label Guide: Materials, Fixing and Washing | TAGE",
        title_ja="フェルト・布製ワッペンガイド：素材・固定方法・洗濯検収 | TAGE",
        title_ko="펠트·패브릭 패치 라벨 가이드: 소재·고정·세탁 검수 | TAGE",
        title_fr="Guide des badges en feutre et pièces en tissu : matières et fixation | TAGE",
        title_es="Guía de badges de fieltro y parches de tela: materiales y fijación | TAGE",
        desc_zh="毛毡标与布艺贴片指南：分清毛毡、毛巾布、帆布与贴布绣四类标片的材质与风险，讲清克重、厚度与边缘处理怎么定，车缝、烫贴与魔术贴背三种固定方式的取舍，洗后缩水、掉毛与脱线的验证，以及克重、尺寸公差、色差与留样的验收口径。来自东莞泰阁包装。",
        desc_en="Felt badges, terry patches, canvas labels and appliqué compared: material and weight, edge finishing, sewing versus heat-sealing and acceptance criteria.",
        desc_ja="フェルトバッジ・パイルワッペン・キャンバスラベル・アップリケの4種類を比較し、素材と目付、縁の加工、縫製と熱接着の使い分け、洗濯後の収縮・毛抜け・ほつれの検証、目付・寸法公差・色差・サンプル保管の検収基準を解説。東莞泰閣包装。",
        desc_ko="펠트 배지·테리 패치·캔버스 라벨·아플리케 네 가지를 비교하고, 소재와 중량, 가장자리 가공, 봉제와 열접착의 선택, 세탁 후 수축·털 빠짐·풀림 검증, 중량·치수 공차·색차·샘플 보관 검수 기준을 정리했습니다. 둥관 TAGE 패키징.",
        desc_fr="Guide des badges en feutre et pièces en tissu : feutre, éponge, toile et appliqué comparés, grammage et finition des bords, couture ou thermocollage, tenue au lavage et critères de réception.",
        desc_es="Guía de badges de fieltro y parches de tela: fieltro, rizo, lona y aplique comparados, gramaje y acabado de bordes, cosido o termoadhesivo, resistencia al lavado y criterios de recepción.",
        crumb_zh="布艺贴片指南",
        crumb_en="Fabric Patch Labels",
        crumb_ja="布製ワッペン",
        crumb_ko="패브릭 패치",
        crumb_fr="Pièces en tissu",
        crumb_es="Parches de tela",
        h1_zh="毛毡标与布艺贴片指南：材质、固定方式与洗护验收",
        h1_en="Felt and Fabric Patch Guide: Material, Fixing and Wash Acceptance",
        h1_ja="フェルト・布製ワッペンガイド：素材・固定方法・洗濯検収",
        h1_ko="펠트·패브릭 패치 가이드: 소재·고정 방식·세탁 검수",
        h1_fr="Badges en feutre et pièces en tissu : matière, fixation et tenue",
        h1_es="Badges de fieltro y parches de tela: material, fijación y lavado",
        tag_zh="材质指南",
        tag_en="Material Guide",
        tag_ja="素材ガイド",
        tag_ko="소재 가이드",
        tag_fr="Guide des matières",
        tag_es="Guía de materiales",
        sum_zh="毛毡标、毛巾布标、帆布标与贴布绣同属布艺贴片，却各有各的脾气：毛毡切边不处理就掉毛，毛巾布洗后毛圈倒伏，帆布克重选错显笨重，贴布绣边缘针距不够就脱线。本文用一张表分清四类标片的材质与风险，讲清克重、厚度与边缘处理怎么定规格，车缝、烫贴与魔术贴背三种固定方式的取舍，以及洗后缩水、掉毛与脱线的牢度验证和可直接写进询价单的验收口径。",
        sum_en="Felt badges, terry patches, canvas labels and appliqué belong to the same family of fabric patches yet each behaves differently: felt sheds if the cut edge is untreated, terry loops flatten after washing, canvas looks heavy at the wrong weight, and appliqué frays when edge stitching is too open. This guide separates the four families with a comparison table, sets out weight, thickness and edge finishing, weighs sewing against heat-sealing and hook-and-loop, and closes with wash-durability tests and acceptance criteria you can paste into a quotation request.",
        sum_ja="フェルトバッジ、パイルワッペン、キャンバスラベル、アップリケは同じ布製ワッペンの仲間ですが、性質はそれぞれ異なります。フェルトは裁断端を処理しないと毛が抜け、パイルは洗濯後にループが倒れ、キャンバスは目付を誤ると重く見え、アップリケは縁の針数が足りないとほつれます。本記事は比較表で4系統を整理し、目付・厚み・縁の加工の決め方、縫製・熱接着・面ファスナーの使い分け、洗濯後の収縮・毛抜け・ほつれの検証、見積依頼に書ける検収基準を示します。",
        sum_ko="펠트 배지, 테리 패치, 캔버스 라벨, 아플리케는 같은 패브릭 패치류지만 성격이 각각 다릅니다. 펠트는 재단 단면을 처리하지 않으면 털이 빠지고, 테리는 세탁 후 루프가 눌리며, 캔버스는 중량을 잘못 고르면 무거워 보이고, 아플리케는 가장자리 박음질이 성글면 실이 풀립니다. 이 글은 비교표로 네 가지를 정리하고, 중량·두께·가장자리 가공의 사양 설정, 봉제·열접착·벨크로의 선택, 세탁 후 수축·털 빠짐·풀림 검증, 견적 요청서에 쓸 수 있는 검수 기준을 제시합니다.",
        sum_fr="Les badges en feutre, écussons en éponge, étiquettes en toile et appliqués appartiennent à la même famille de pièces en tissu, mais chacun se comporte différemment : le feutre perd ses poils si la coupe n'est pas traitée, les boucles de l'éponge s'aplatissent au lavage, la toile paraît lourde au mauvais grammage et l'appliqué s'effiloche quand les points de bord sont trop espacés. Ce guide distingue les quatre familles dans un tableau, fixe le grammage, l'épaisseur et la finition des bords, compare couture, thermocollage et velcro, et se termine par les essais de tenue au lavage et les critères de réception.",
        sum_es="Los badges de fieltro, parches de rizo, etiquetas de lona y apliques pertenecen a la misma familia de piezas de tela, pero cada uno se comporta distinto: el fieltro suelta pelo si el corte no se trata, los bucles del rizo se aplastan al lavar, la lona parece pesada con el gramaje erróneo y el aplique se deshilacha si las puntadas del borde son escasas. Esta guía separa las cuatro familias con una tabla, fija gramaje, espesor y acabado de bordes, compara cosido, termoadhesivo y velcro, y cierra con los ensayos de lavado y los criterios de recepción.",
    ),
    dict(
        slug="sun-protective-clothing-label-guide.html",
        body="blog/_body_upf.html",
        title_zh="防晒服装标签与辅料指南：UPF 分级、洗后保持与合规标注 | TAGE",
        title_en="UV-Protective Clothing Label Guide: UPF Ratings and Labelling | TAGE",
        title_ja="UVカット衣料のラベル副資材ガイド：UPF等級と洗濯後の保持 | TAGE",
        title_ko="자외선 차단 의류 라벨 부자재 가이드: UPF 등급과 세탁 후 유지 | TAGE",
        title_fr="Guide des étiquettes anti-UV : grades UPF et étiquetage | TAGE",
        title_es="Guía de etiquetas anti-UV: grados UPF y etiquetado | TAGE",
        desc_zh="防晒服装标签与辅料指南：讲清 UPF 分级与 AATCC 183、EN 13758、GB/T 18830 等测试方法，防晒声明怎么标，洗后 UPF 如何保持与洗水标怎么写，防晒服的辅料怎么选，以及吊牌与包装的合规清单。来自东莞泰阁包装。",
        desc_en="UV-protective clothing labels: UPF grades and test methods, labelling rules by market, how UPF holds up after washing, trims, and a compliance checklist.",
        desc_ja="UVカット衣料のラベル副資材ガイド。UPF 15～50+ の等級と AATCC 183・EN 13758・AS/NZS 4399・GB/T 18830 などの試験方法、市場ごとの表示ルール、洗濯後の UPF 保持と洗濯表示の書き方、ファスナー・縫い糸・ひもの選び方、タグと包装での伝え方とコンプライアンスチェックリストを解説。東莞泰閣包装。",
        desc_ko="자외선 차단 의류 라벨 부자재 가이드. UPF 15~50+ 등급과 AATCC 183·EN 13758·AS/NZS 4399·GB/T 18830 등 시험 방법, 시장별 표기 규칙, 세탁 후 UPF 유지와 세탁 라벨 작성법, 지퍼·봉제사·끈 선택, 행택과 포장 전달 방식과 컴플라이언스 체크리스트를 정리했습니다. 둥관 TAGE 패키징.",
        desc_fr="Guide des étiquettes anti-UV : grades UPF et méthodes d'essai, règles d'étiquetage par marché, tenue de l'UPF au lavage, choix des accessoires et liste de conformité.",
        desc_es="Guía de etiquetas anti-UV: grados UPF y métodos de ensayo, etiquetado por mercado, mantenimiento del UPF al lavar, elección de accesorios y lista de cumplimiento.",
        crumb_zh="防晒服装标签指南",
        crumb_en="UV-Protective Clothing Labels",
        crumb_ja="UVカット衣料ラベル",
        crumb_ko="자외선 차단 의류 라벨",
        crumb_fr="Étiquettes anti-UV",
        crumb_es="Etiquetas anti-UV",
        h1_zh="防晒服装标签与辅料指南：UPF 分级、洗后保持与合规标注",
        h1_en="UV-Protective Clothing Labels: UPF Grades, Retention and Compliance",
        h1_ja="UVカット衣料のラベルガイド：UPF等級・洗濯後の保持・適正表示",
        h1_ko="자외선 차단 의류 라벨 가이드: UPF 등급·세탁 후 유지·적정 표기",
        h1_fr="Étiquettes anti-UV : grades UPF, tenue au lavage et conformité",
        h1_es="Etiquetas anti-UV: grados UPF, lavado y cumplimiento",
        tag_zh="合规指南",
        tag_en="Compliance Guide",
        tag_ja="コンプライアンス",
        tag_ko="컴플라이언스",
        tag_fr="Guide de conformité",
        tag_es="Guía de cumplimiento",
        sum_zh="防晒服装的卖点最终落在一张标签上：UPF 标多高要满足目标市场的测试方法、分级门槛与标注规则，标了 UPF 50+ 却拿不出报告，在欧美平台很容易被下架。本文讲清 UPF 15 到 50+ 的分级与 AATCC 183、EN 13758、AS/NZS 4399、GB/T 18830 的方法差异，各市场怎么标，洗后 UPF 怎么保持与洗水标怎么写，防晒服的拉链缝线绳带怎么选，以及吊牌包装的传达方式与合规清单。",
        sum_en="The selling point of UV-protective clothing ends up on a label: the UPF figure must meet the target market's test method, threshold and labelling rules, and claiming UPF 50+ without a report gets a listing pulled on Western marketplaces. This guide sets out the UPF 15 to 50+ grades and the differences between AATCC 183, EN 13758, AS/NZS 4399 and GB/T 18830, how each market labels the claim, how UPF is retained after washing and how to word the care label, how to choose zips, thread and cords, and how to convey the claim on tags and packaging with a compliance checklist.",
        sum_ja="UV カット衣料の売りは最終的に1枚のラベルに集約されます。UPF をどの高さで表示するかは、対象市場の試験方法・等級のしきい値・表示ルールを満たす必要があり、レポートなしに UPF 50+ を表示すると欧米のプラットフォームで削除されがちです。本記事は UPF 15～50+ の等級と AATCC 183・EN 13758・AS/NZS 4399・GB/T 18830 の方法差、市場ごとの表示、洗濯後の UPF 保持と洗濯表示の書き方、ファスナー・縫い糸・ひもの選び方、タグと包装での伝え方とコンプライアンスチェックリストを解説します。",
        sum_ko="자외선 차단 의류의 셀링 포인트는 결국 한 장의 라벨로 귀결됩니다. UPF를 어느 높이로 표기할지는 대상 시장의 시험 방법, 등급 기준, 표기 규칙을 충족해야 하며, 성적서 없이 UPF 50+를 표기하면 유럽·북미 플랫폼에서 삭제되기 쉽습니다. 이 글은 UPF 15~50+ 등급과 AATCC 183·EN 13758·AS/NZS 4399·GB/T 18830의 방법 차이, 시장별 표기, 세탁 후 UPF 유지와 세탁 라벨 작성법, 지퍼·봉제사·끈 선택, 행택과 포장 전달 방식과 컴플라이언스 체크리스트를 다룹니다.",
        sum_fr="L'argument d'un vêtement anti-UV finit sur une étiquette : la valeur d'UPF doit satisfaire la méthode d'essai, le seuil et les règles d'étiquetage du marché cible, et revendiquer UPF 50+ sans rapport fait retirer l'annonce sur les places de marché occidentales. Ce guide présente les grades UPF 15 à 50+ et les écarts entre AATCC 183, EN 13758, AS/NZS 4399 et GB/T 18830, l'étiquetage selon les marchés, la tenue de l'UPF au lavage et la rédaction de l'étiquette d'entretien, le choix des fermetures, fils et cordons, puis la façon de porter l'allégation sur l'étiquette et l'emballage avec une liste de conformité.",
        sum_es="El argumento de una prenda anti-UV acaba en una etiqueta: el valor de UPF debe cumplir el método de ensayo, el umbral y las reglas de etiquetado del mercado destino, y reclamar UPF 50+ sin informe hace que retiren la ficha en los marketplaces occidentales. Esta guía presenta los grados UPF 15 a 50+ y las diferencias entre AATCC 183, EN 13758, AS/NZS 4399 y GB/T 18830, el etiquetado por mercado, el mantenimiento del UPF al lavar y cómo redactar la etiqueta de cuidado, la elección de cremalleras, hilos y cordones, y cómo trasladar la alegación a etiquetas y embalaje con una lista de cumplimiento.",
    ),
]
