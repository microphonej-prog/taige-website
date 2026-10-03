#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-03 下午批次（14:00）每日更新：2 篇新文章元数据（六语：zh-Hant 根 / en / ja / ko / fr / es）

选题说明（30 项主题池与历次扩展选题均已上线，本次沿「扣合类辅料」与「黏合衬」两个尚未覆盖的
技术品类扩展，已核对 blog/、en|ja|ko|fr|es/blog/ 与 sitemap.xml 无重复，并 grep 全站确认：

- zipper-selection-guide vs garment-buttons-fasteners-guide（只讲纽扣、按扣、气眼铆钉，全站
  "拉链" 0 次出现在该文，也没有任何拉链专文）、poly-bag-*-zip（讲的是包装袋拉链袋与滑块袋，
  非服装拉链）、outerwear/denim（品类指南，拉链一笔带过）；本文是拉链的五变量体系：
  齿材（尼龙/树脂/金属）、号型（#3/#5/#8/#10）、布带缩率匹配、拉头与结构、以及镍释放
  与盐雾等合规测试。
- fusible-interlining-guide vs trim-ironing-heat-resistance-guide（讲辅料耐熨烫温度，
  不涉压烫工艺与剥离强度）、garment-trims-fabric-compatibility-guide（讲辅料与面料的
  色移/收缩/勾丝相容性，不专讲衬布）、elastic-trims-selection-guide（弹性带类）；
  全站无「黏合衬/热熔胶衬」专文：本文给三类基布、四种涂层（PA/PES/PE/专用胶）、
  压烫三参数窗口、缩率匹配与起泡根因，以及五个常见缺陷的改法。
"""

ARTICLES = [
    dict(
        slug="zipper-selection-guide.html",
        body="blog/_body_zipper.html",
        title_zh="服装拉链选型指南：齿材、号型与拉头怎么选 | TAGE",
        title_en="Garment Zipper Guide: Teeth, Size Numbers &amp; Sliders | TAGE",
        title_ja="衣料用ファスナーの選定ガイド：務歯素材・号数・スライダーの選び方 | TAGE",
        title_ko="의류 지퍼 선택 가이드: 이빨 소재, 호수, 슬라이더 | TAGE",
        title_fr="Guide de la fermeture à glissière : dents, numéro et curseur | TAGE",
        title_es="Guía de la cremallera: dientes, número de talla y cursor | TAGE",
        desc_zh="服装拉链选型指南：讲清齿材（尼龙、树脂、金属）、号型（#3/#5/#8）与拉头结构的搭配逻辑，给出布带缩率匹配、水洗与盐雾镍释放测试要点，并附可直接抄进询价邮件的六项询价验收清单。东莞泰阁包装。",
        desc_en="Garment zipper guide: nylon, resin and metal teeth, size numbers from #3 to #8, slider and structure types, tape shrinkage matching, wash and nickel release testing, plus a quote checklist.",
        desc_ja="衣料用ファスナーの選定ガイド。ナイロン・樹脂・金属の務歯、#3〜#8 の号数とスライダー・構造の選び方、テープ収縮率の整合、洗濯・塩水噴霧・ニッケル溶出の試験、見積りに使えるチェックリストを掲載。東莞泰閣包装。",
        desc_ko="의류 지퍼 선택 가이드. 나일론·수지·금속 이빨, #3~#8 호수, 슬라이더와 구조 선택, 테이프 수축률 정합, 세탁·염수 분무·니켈 용출 시험, 견적용 체크리스트를 담았습니다. 둥관 TAGE 패키징.",
        desc_fr="Guide de la fermeture à glissière : dents nylon, résine et métal, numéros #3 à #8, curseurs et structures, retrait du ruban, essais de lavage et de nickel, avec liste de devis.",
        desc_es="Guía de la cremallera: dientes de nailon, resina y metal, números #3 a #8, cursores y estructuras, encogimiento de la cinta, ensayos de lavado y níquel, con lista para presupuestar.",
        crumb_zh="拉链选型指南",
        crumb_en="Zipper Selection Guide",
        crumb_ja="ファスナー選定ガイド",
        crumb_ko="지퍼 선택 가이드",
        crumb_fr="Guide fermeture à glissière",
        crumb_es="Guía de la cremallera",
        h1_zh="服装拉链选型指南：齿材、号型与拉头怎么选",
        h1_en="Garment Zipper Selection: Teeth, Size Numbers and Sliders",
        h1_ja="衣料用ファスナーの選定：務歯素材・号数・スライダー",
        h1_ko="의류 지퍼 선택: 이빨 소재, 호수, 슬라이더",
        h1_fr="Choisir une fermeture à glissière : dents, numéro et curseur",
        h1_es="Elegir una cremallera: dientes, número de talla y cursor",
        tag_zh="辅料选型",
        tag_en="Trims Selection",
        tag_ja="副資材選定",
        tag_ko="부자재 선택",
        tag_fr="Choix d'accessoires",
        tag_es="Selección de accesorios",
        sum_zh="拉链的选型只有五个变量：齿材、号型、布带、拉头与结构。本文给出尼龙/树脂/金属三种齿材的对比、号型与面料克重的对应关系、布带缩率匹配、镍释放与盐雾测试要点，并附可直接使用的询价验收清单。",
        sum_en="Zipper selection comes down to five variables: teeth, size number, tape, slider and structure. Compare nylon, resin and metal teeth, match the number to fabric weight, align tape shrinkage, and cover nickel and salt spray testing with a ready quote checklist.",
        sum_ja="ファスナーの選定は務歯・号数・テープ・スライダー・構造の五つです。ナイロン・樹脂・金属の比較、生地目付と号数の対応、テープ収縮率の整合、ニッケル溶出と塩水噴霧の試験、そのまま使える見積りチェックリストを掲載します。",
        sum_ko="지퍼 선택은 이빨, 호수, 테이프, 슬라이더, 구조의 다섯 가지입니다. 나일론·수지·금속 비교, 원단 평량과 호수 대응, 테이프 수축률 정합, 니켈 용출과 염수 분무 시험, 바로 쓰는 견적 체크리스트를 정리했습니다.",
        sum_fr="Cinq variables décident du choix : dents, numéro, ruban, curseur et structure. Comparez nylon, résine et métal, accordez le numéro au grammage, alignez le retrait du ruban et couvrez nickel et brouillard salin.",
        sum_es="Cinco variables deciden la elección: dientes, número, cinta, cursor y estructura. Compara nailon, resina y metal, ajusta el número al gramaje, alinea el encogimiento de la cinta y cubre níquel y niebla salina.",
    ),
    dict(
        slug="fusible-interlining-guide.html",
        body="blog/_body_interlining.html",
        title_zh="黏合衬选型指南：基布、涂层与压烫参数 | TAGE",
        title_en="Fusible Interlining Guide: Base, Coating &amp; Fusing | TAGE",
        title_ja="接着芯地の選定ガイド：基布・樹脂・プレス3条件 | TAGE",
        title_ko="접착 심지 선택 가이드: 기포지, 수지, 프레스 조건 | TAGE",
        title_fr="Guide du thermocollant : support, enduction et paramètres | TAGE",
        title_es="Guía de la entretela termoadhesiva: base y parámetros | TAGE",
        desc_zh="黏合衬（热熔胶衬）选型指南：对比有纺、无纺、针织三类基布与 PA/PES/PE 四种涂层，给出压烫温度、压力、时间的三参数窗口、缩率匹配与起泡根因，并附衬布询价与验收清单。东莞泰阁包装。",
        desc_en="Fusible interlining guide: woven, non-woven and knitted bases, PA/PES/PE coatings, the fusing temperature, pressure and time window, shrinkage matching and why blistering happens.",
        desc_ja="接着芯地の選定ガイド。織物・不織布・ニットの基布と PA/PES/PE の樹脂、プレス温度・圧力・時間の条件幅、収縮率の整合と膨れの原因、芯地の見積りと検収チェックリストを掲載。東莞泰閣包装。",
        desc_ko="접착 심지 선택 가이드. 직물·부직포·니트 기포지와 PA/PES/PE 수지, 프레스 온도·압력·시간 조건, 수축률 정합과 부풀음 원인, 심지 견적과 검수 체크리스트를 담았습니다. 둥관 TAGE 패키징.",
        desc_fr="Guide du thermocollant : supports tissé, non-tissé et maille, enductions PA/PES/PE, fenêtre de température, pression et temps, accord des retraits et causes du cloquage.",
        desc_es="Guía de la entretela termoadhesiva: bases tejida, no tejida y de punto, recubrimientos PA/PES/PE, ventana de temperatura, presión y tiempo, encogimiento y causas del ampollado.",
        crumb_zh="黏合衬选型指南",
        crumb_en="Fusible Interlining Guide",
        crumb_ja="接着芯地の選定ガイド",
        crumb_ko="접착 심지 선택 가이드",
        crumb_fr="Guide du thermocollant",
        crumb_es="Guía de la entretela",
        h1_zh="黏合衬选型指南：基布、涂层与压烫参数怎么定",
        h1_en="Fusible Interlining: Base Fabric, Coating and Fusing Parameters",
        h1_ja="接着芯地の選定：基布・樹脂・プレス条件の決め方",
        h1_ko="접착 심지 선택: 기포지, 수지, 프레스 조건 정하기",
        h1_fr="Thermocollant : support, enduction et paramètres de thermocollage",
        h1_es="Entretela termoadhesiva: base, recubrimiento y parámetros",
        tag_zh="辅料选型",
        tag_en="Trims Selection",
        tag_ja="副資材選定",
        tag_ko="부자재 선택",
        tag_fr="Choix d'accessoires",
        tag_es="Selección de accesorios",
        sum_zh="衬的问题九成出在匹配，而不是衬本身的档次。本文讲清有纺/无纺/针织三类基布、PA/PES/PE 四种涂层的耐洗差异、压烫三参数窗口与缩率匹配，并给出起泡、渗胶、泛黄、干洗脱层五个常见缺陷的改法。",
        sum_en="Nine interlining problems in ten come from mismatching, not grade. Work through woven, non-woven and knitted bases, the wash behaviour of PA, PES and PE coatings, the three fusing parameters and shrinkage matching, then fix blistering, strike-through and yellowing.",
        sum_ja="芯地の不具合は九割が「合っていないこと」に起因します。織物・不織布・ニットの基布、PA・PES・PE の耐洗濯性、プレスの3条件と収縮率の整合、そして膨れ・染み出し・黄変・ドライ後の剥がれの対策を整理します。",
        sum_ko="심지 문제의 90%는 등급이 아니라 불일치에서 생깁니다. 직물·부직포·니트 기포지, PA·PES·PE 수지의 세탁 내구성, 프레스 세 조건과 수축률 정합, 그리고 부풀음·배어 나옴·황변·드라이 후 박리 대책을 정리했습니다.",
        sum_fr="Neuf problèmes de renfort sur dix viennent d'une inadéquation, pas du grade. Supports tissé, non-tissé et maille, tenue au lavage des enductions PA, PES et PE, trois paramètres et accord des retraits, puis cloquage, traversée et jaunissement.",
        sum_es="Nueve de cada diez problemas de entretela vienen de un desajuste, no de la calidad. Bases tejida, no tejida y de punto, resistencia al lavado de PA, PES y PE, los tres parámetros y el encogimiento, y soluciones a ampollado, migración y amarilleo.",
    ),
]
