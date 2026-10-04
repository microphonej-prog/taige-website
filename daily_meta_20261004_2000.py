#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-04 晚间批次（20:00）每日更新：2 篇新文章元数据（六语：zh-Hant 根 / en / ja / ko / fr / es）

选题说明（主题池 30 项与历次扩展（抽绳、花边、拉链、黏合衬、皮革、反光、魔术贴、纽扣、弹性、
童装等）均已上线，本次沿「里布/内衬类」与「织带类」两个尚未覆盖的品类扩展，已核对 blog/、
en|ja|ko|fr|es/blog/ 与 sitemap.xml 无重复，并 grep 全站确认：）

- lining-fabric-selection-guide  vs fusible-interlining-guide（黏合衬，是衬不是里布）、
  garment-trims-fabric-compatibility-guide（辅料与面料配伍，仅顺带提里布）、
  suitings/outerwear 指南（各提一句里布）；全站无「里布（lining）」专文：
  本文对比涤塔夫、尼龙塔夫、醋酸、铜氨、针织里布与色丁六类，按品类倒推选型，
  并给出克重/密度、缩水、色牢度、抗静电、脱散纰裂与批差六项验收口径。
- webbing-tape-selection-guide  vs elastic-trims-selection-guide（含弹力织带，主打弹伸）、
  garment-drawcord-guide（绳而非带）、garment-belly-band-guide（纸腰封，非织物）；
  全站无「织带（webbing / 非弹力带）」专文：
  本文区分织带与松紧带，对比平纹、斜纹、人字纹、双层与提花五种结构，
  讲清涤纶、尼龙、丙纶、棉与再生涤纶的取舍，并给出规格五项与三项必做测试。
"""

ARTICLES = [
    dict(
        slug="lining-fabric-selection-guide.html",
        body="blog/_body_lining.html",
        title_zh="服装里布选型指南：涤塔夫、醋酸、铜氨与针织里布怎么选 | TAGE",
        title_en="Garment Lining Guide: Taffeta, Acetate, Cupro &amp; Knit | TAGE",
        title_ja="裏地の選定ガイド：タフタ・アセテート・キュプラ・ニット裏地 | TAGE",
        title_ko="안감 선택 가이드: 태피터, 아세테이트, 큐프라, 니트 안감 | TAGE",
        title_fr="Guide de la doublure : taffetas, acétate, cupro et maille | TAGE",
        title_es="Guía del forro: tafetán, acetato, cupro y punto | TAGE",
        desc_zh="服装里布选型指南：对比涤塔夫、尼龙塔夫、醋酸、铜氨、针织里布与色丁六类材质的手感、透气、静电与洗后表现，讲清西装、风衣、裙装、运动与童装的倒推选型思路，给出克重、缩水率、色牢度与纰裂等验收口径。东莞泰阁包装。",
        desc_en="Garment lining guide: compare taffeta, nylon, acetate, cupro, knit and satin linings, match them to garment types, and set weight, shrinkage and fastness specs.",
        desc_ja="裏地の選定ガイド。ポリエステルタフタ・ナイロン・アセテート・キュプラ・ニット裏地・サテンの風合い、通気性、静電気、洗濯後の挙動を比較し、スーツ・コート・ドレス・スポーツ・子供服からの逆算選定、目付・収縮率・堅牢度・目ずれの検収基準を解説。東莞泰閣包装。",
        desc_ko="안감 선택 가이드. 폴리에스터 태피터·나일론·아세테이트·큐프라·니트 안감·새틴의 촉감, 통기성, 정전기, 세탁 후 상태를 비교하고 정장·코트·드레스·스포츠·아동복에서 거꾸로 하는 선택과 중량·수축률·견뢰도·봉제 미끄러짐 기준을 정리했습니다. 둥관 TAGE 패키징.",
        desc_fr="Guide de la doublure : taffetas, nylon, acétate, cupro, maille et satin comparés (toucher, respirabilité, statique, lavage), choix par type de vêtement et spécifications de retrait et de solidité.",
        desc_es="Guía del forro: tafetán, nailon, acetato, cupro, punto y satén comparados, elección según el tipo de prenda y especificaciones de encogimiento y solidez.",
        crumb_zh="服装里布选型指南",
        crumb_en="Garment Lining Guide",
        crumb_ja="裏地の選定ガイド",
        crumb_ko="안감 선택 가이드",
        crumb_fr="Guide de la doublure",
        crumb_es="Guía del forro",
        h1_zh="服装里布选型指南：涤塔夫、醋酸、铜氨与针织里布怎么选",
        h1_en="Garment Lining Guide: Taffeta, Acetate, Cupro and Knit Linings",
        h1_ja="裏地の選定：タフタ・アセテート・キュプラ・ニット裏地の選び方",
        h1_ko="안감 선택: 태피터, 아세테이트, 큐프라, 니트 안감 고르기",
        h1_fr="Choisir sa doublure : taffetas, acétate, cupro et maille",
        h1_es="Elegir el forro: tafetán, acetato, cupro y punto",
        tag_zh="辅料选型",
        tag_en="Trims Selection",
        tag_ja="副資材選定",
        tag_ko="부자재 선택",
        tag_fr="Choix d'accessoires",
        tag_es="Selección de accesorios",
        sum_zh="里布夹在面料与人体之间，决定滑穿、遮覆、定型与保护四项功能。本文对比涤塔夫、尼龙塔夫、醋酸、铜氨、针织里布与色丁的手感、透气、静电与洗后表现，给出按品类倒推的选型思路，以及克重与密度、缩水率、色牢度、脱散纰裂与批差六项验收口径。",
        sum_en="The lining sits between shell and body, delivering slip, coverage, structure and protection. Compare taffeta, nylon, acetate, cupro, knit and satin by handle, breathability, static and wash behaviour, then work backwards from the garment type and lock six acceptance specs.",
        sum_ja="裏地は表地と身体の間にあり、滑り・遮蔽・形の保持・保護を担います。タフタ・ナイロン・アセテート・キュプラ・ニット裏地・サテンを風合い、通気性、静電気、洗濯後の挙動で比較し、品種からの逆算選定と、目付・収縮率・堅牢度・ほつれ・ロット差の6つの検収基準を示します。",
        sum_ko="안감은 겉감과 인체 사이에서 미끄럼, 가림, 형태 유지, 보호를 담당합니다. 태피터, 나일론, 아세테이트, 큐프라, 니트 안감, 새틴을 촉감·통기성·정전기·세탁 후 상태로 비교하고 품목에서 거꾸로 하는 선택과 중량·수축률·견뢰도·올 풀림·로트차 여섯 가지 검수 기준을 제시합니다.",
        sum_fr="La doublure se place entre tissu et corps : glisse, couvrance, tenue, protection. Comparez taffetas, nylon, acétate, cupro, maille et satin (toucher, respirabilité, statique, lavage), puis partez du type de vêtement et fixez six critères de réception.",
        sum_es="El forro va entre tejido y cuerpo: deslizamiento, cobertura, estructura y protección. Compara tafetán, nailon, acetato, cupro, punto y satén por tacto, transpirabilidad, estática y lavado, y fija seis criterios de recepción desde el tipo de prenda.",
    ),
    dict(
        slug="webbing-tape-selection-guide.html",
        body="blog/_body_webbing.html",
        title_zh="服装织带选型指南：平纹、斜纹、人字纹与材质怎么选 | TAGE",
        title_en="Webbing &amp; Tape Guide: Plain, Twill, Herringbone &amp; Materials | TAGE",
        title_ja="ウェビングテープ選定ガイド：平織・綾織・ヘリンボーンと素材 | TAGE",
        title_ko="웨빙 테이프 선택 가이드: 평직, 능직, 헤링본과 소재 | TAGE",
        title_fr="Guide des sangles : toile, sergé, chevrons et matières | TAGE",
        title_es="Guía de cintas: plano, sarga, espiga y materiales | TAGE",
        desc_zh="服装织带选型指南：先分清织带与松紧带的边界，再对比平纹、斜纹、人字纹、双层与提花五种结构，讲清涤纶、尼龙、丙纶、棉与再生涤纶的取舍，给出宽度、厚度、克重、断裂强力与色牢度等规格口径。东莞泰阁包装。",
        desc_en="Webbing guide: plain, twill, herringbone and jacquard structures, polyester, nylon, PP and rPET choices, plus width, weight and strength specs.",
        desc_ja="ウェビングテープ選定ガイド。平織・綾織・ヘリンボーン・二重織・ジャカードの構造比較、ポリエステル・ナイロン・PP・綿・再生ポリエステルの選び方、幅・厚み・目付・引張強度・堅牢度の仕様、発注前の3つの試験を掲載。東莞泰閣包装。",
        desc_ko="웨빙 테이프 선택 가이드. 평직·능직·헤링본·이중직·자카드 구조 비교와 폴리에스터·나일론·PP·면·재생 폴리에스터 선택, 폭·두께·중량·인장 강도·견뢰도 사양과 발주 전 세 가지 시험을 담았습니다. 둥관 TAGE 패키징.",
        desc_fr="Guide des sangles : toile, sergé, chevrons, double épaisseur et jacquard, choix polyester, nylon, PP, coton et rPET, avec largeur, épaisseur, grammage et résistance.",
        desc_es="Guía de cintas: plano, sarga, espiga, doble capa y jacquard, elección de poliéster, nailon, PP, algodón y rPET, con ancho, gramaje y resistencia a la rotura.",
        crumb_zh="服装织带选型指南",
        crumb_en="Webbing and Tape Guide",
        crumb_ja="ウェビングテープ選定ガイド",
        crumb_ko="웨빙 테이프 선택 가이드",
        crumb_fr="Guide des sangles",
        crumb_es="Guía de cintas",
        h1_zh="服装织带选型指南：平纹、斜纹、人字纹与材质怎么选",
        h1_en="Webbing and Tape Guide: Weaves, Materials and Quality Control",
        h1_ja="織りテープの選定：平織・綾織・ヘリンボーンと素材の選び方",
        h1_ko="웨빙 테이프 선택: 평직, 능직, 헤링본과 소재 고르기",
        h1_fr="Choisir ses sangles : toile, sergé, chevrons et matières",
        h1_es="Elegir cintas: plano, sarga, espiga y materiales",
        tag_zh="辅料选型",
        tag_en="Trims Selection",
        tag_ja="副資材選定",
        tag_ko="부자재 선택",
        tag_fr="Choix d'accessoires",
        tag_es="Selección de accesorios",
        sum_zh="织带不含弹性，靠织法与经纬密度提供强力与挺度，直接决定受力部位能不能扛住。本文区分织带与松紧带，对比平纹、斜纹、人字纹、双层与提花五种结构，讲清涤纶、尼龙、丙纶、棉与再生涤纶的取舍，并列出规格五项与采购前必做的三项测试。",
        sum_en="Webbing carries no elastic: weave and thread density give it strength and body, which decides whether load-bearing areas hold. This guide separates webbing from elastic, compares plain, twill, herringbone, double-layer and jacquard, weighs polyester against nylon, PP, cotton and rPET, and lists five specs plus three pre-order tests.",
        sum_ja="織りテープは伸縮せず、織り組織と経緯密度が強度と腰を作り、荷重部位の耐久を左右します。本記事はテープとゴムの違いを整理し、平織・綾織・ヘリンボーン・二重織・ジャカードを比較、ポリエステル・ナイロン・PP・綿・再生ポリエステルの選択、仕様5項目と発注前の3試験を掲載します。",
        sum_ko="웨빙은 신축성이 없고 조직과 경위 밀도가 강도와 형태를 만들어 하중 부위의 내구성을 좌우합니다. 이 글은 웨빙과 고무밴드를 구분하고 평직·능직·헤링본·이중직·자카드를 비교하며 폴리에스터·나일론·PP·면·재생 폴리에스터 선택, 다섯 가지 사양과 발주 전 세 가지 시험을 정리합니다.",
        sum_fr="La sangle n'est pas élastique : armure et densité de fils font sa solidité et sa tenue, donc la résistance des zones porteuses. Ce guide sépare sangle et élastique, compare toile, sergé, chevrons, double épaisseur et jacquard, arbitre polyester, nylon, PP, coton et rPET, et liste cinq spécifications et trois essais.",
        sum_es="La cinta no es elástica: el ligamento y la densidad de hilos le dan resistencia y cuerpo, y eso decide si las zonas de carga aguantan. Esta guía separa cinta y elástico, compara plano, sarga, espiga, doble capa y jacquard, pondera poliéster, nailon, PP, algodón y rPET, y lista cinco especificaciones y tres ensayos.",
    ),
]
