#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-05 上午批次每日更新：2 篇新文章元数据（六语：zh-Hant 根 / en / ja / ko / fr / es）

选题说明（主题池 30 项与历次扩展（抽绳、花边、拉链、黏合衬、皮革、反光、魔术贴、纽扣、弹性、
里布、织带等）均已上线，本次沿「边缘工艺辅料」与「结构造型辅料」两个尚未覆盖的方向扩展，
已核对 blog/、en|ja|ko|fr|es/blog/ 与 sitemap.xml 无重复，并 grep 全站确认：

- garment-piping-bias-binding-guide  vs elastic-trims-selection-guide（含弹力包边，主打弹伸）、
  webbing-tape-selection-guide（织带结构为主）、hanfu 指南（顺带一句滚边）；
  全站无「滚边条 / 嵌线 / 贴边」专文（grep「滚边」仅 3 处顺带提及、「嵌条」0 处）：
  本文区分 binding / piping / facing 三种工艺，对比涤棉、纯棉、真丝色丁、针织罗纹、织带、
  弹力嵌线六类，讲清斜裁 45°、成品宽度与损耗余量、张力与缩率同步，并给出六项验收口径。
- shoulder-pad-structure-trims-guide  vs suiting-formalwear-trims-guide（仅一处 shoulder pad 顺带提及）、
  fusible-interlining-guide（黏合衬是衬不是结构垫肩）、outerwear-down-jacket-trims-guide（品类指南）；
  全站无「垫肩 / 肩棉 / 胸衬 / 领底呢」专文（grep「垫肩」0 处、「肩棉」「胸衬」「hair canvas」0 处）：
  本文对比海绵、针刺棉、复合、针织包覆与薄型五类垫肩，按品类倒推厚度与形状，
  并覆盖胸衬、领底呢、袖山条、牵条等配套结构件与六项验收口径。
"""

ARTICLES = [
    dict(
        slug="garment-piping-bias-binding-guide.html",
        body="blog/_body_piping.html",
        title_zh="服装滚边条与嵌线选型指南：斜裁、宽度与牢度怎么定 | TAGE",
        title_en="Garment Binding &amp; Piping Guide: Bias Cut, Width and Durability | TAGE",
        title_ja="バイアスとパイピングの選定ガイド：斜め裁断・幅・耐久性 | TAGE",
        title_ko="바인딩·파이핑 선택 가이드: 바이어스 재단, 폭, 내구성 | TAGE",
        title_fr="Guide du biais et du passepoil : coupe, largeur et tenue | TAGE",
        title_es="Guía de bies y ribete: corte al bies, anchura y resistencia | TAGE",
        desc_zh="服装滚边条与嵌线选型指南：先分清滚边、嵌线与贴边三种工艺，再对比涤棉、纯棉、真丝色丁、针织罗纹与织带六类材质，讲清斜裁45°与成品宽度、缩率同步与张力控制，并给出色牢度、色差与卷装米数等六项验收口径。东莞泰阁包装。",
        desc_en="Binding and piping guide: binding vs piping vs facing, five materials compared, bias cut and width specs, and the key acceptance criteria that matter.",
        desc_ja="バイアスとパイピングの選定ガイド。バインディング・パイピング・見返しの違い、ポリ綿・綿・シルクサテン・ニットリブ・綾テープ・伸縮パイピングの比較、45°バイアスと仕上がり幅、収縮率とテンション管理、堅牢度・色差・正味メートルの検収基準を解説。東莞泰閣包装。",
        desc_ko="바인딩과 파이핑 선택 가이드. 바인딩·파이핑·안단의 차이, 폴리코튼·면·실크새틴·니트골지·능직테이프·신축 파이핑 비교, 45도 바이어스와 완성 폭, 수축률과 장력 관리, 견뢰도·색차·순 미터수 검수 기준을 정리했습니다. 둥관 TAGE 패키징.",
        desc_fr="Guide du biais et du passepoil : biais, passepoil et parementure distingués, six matières comparées, coupe à 45°, largeurs finies, retrait, tension et critères de réception.",
        desc_es="Guía de bies y ribete: bies, ribete y vistas diferenciados, seis materiales comparados, corte a 45°, anchuras acabadas, encogimiento, tensión y criterios de recepción.",
        crumb_zh="滚边与嵌线选型指南",
        crumb_en="Binding and Piping Guide",
        crumb_ja="バイアスとパイピングの選定ガイド",
        crumb_ko="바인딩·파이핑 선택 가이드",
        crumb_fr="Guide du biais et du passepoil",
        crumb_es="Guía de bies y ribete",
        h1_zh="服装滚边条与嵌线选型指南：斜裁、宽度与牢度怎么定",
        h1_en="Garment Binding and Piping Guide: Bias Cut, Width and Durability",
        h1_ja="バイアスとパイピングの選定：斜め裁断・幅・耐久性の決め方",
        h1_ko="바인딩과 파이핑 선택: 바이어스 재단, 폭, 내구성 정하기",
        h1_fr="Choisir son biais et son passepoil : coupe, largeur et tenue",
        h1_es="Elegir bies y ribete: corte, anchura y resistencia",
        tag_zh="辅料选型",
        tag_en="Trims Selection",
        tag_ja="副資材選定",
        tag_ko="부자재 선택",
        tag_fr="Choix d'accessoires",
        tag_es="Selección de accesorios",
        sum_zh="滚边条与嵌线用量小，却是成衣工艺水平最直观的体现。本文先分清滚边、嵌线与贴边三种容易混淆的工艺与计价口径，再对比六类材质，讲清斜裁45°、成品宽度与损耗余量、缩率同步与张力控制，最后给出色牢度、色差、卷装米数与环保测试等六项验收口径。",
        sum_en="Binding and piping are a tiny share of the bill of materials but the clearest sign of workmanship. This guide separates binding, piping and facing — including how each is priced — compares six materials, and covers the 45° bias cut, finished width and loss allowance, matching shrinkage and stitch tension, closing with six acceptance criteria.",
        sum_ja="バイアスとパイピングは使用量が少ないながら、縫製レベルが最も正直に出る部分です。本記事はバインディング・パイピング・見返しの違いと見積り方法を整理し、6素材を比較、45°バイアス、仕上がり幅とロス、収縮率の同調とテンション管理を解説し、最後に6つの検収基準を示します。",
        sum_ko="바인딩과 파이핑은 사용량이 적지만 봉제 수준이 가장 여실히 드러나는 부분입니다. 이 글은 바인딩·파이핑·안단의 차이와 견적 방식을 구분하고 여섯 소재를 비교하며, 45도 바이어스, 완성 폭과 손실 여유, 수축률 일치와 장력 관리를 다루고 여섯 가지 검수 기준을 제시합니다.",
        sum_fr="Le biais et le passepoil pèsent peu dans le coût mais révèlent le plus nettement la confection. Ce guide distingue biais, passepoil et parementure — y compris leur chiffrage — compare six matières, et traite la coupe à 45°, les largeurs finies et pertes, l'accord des retraits et la tension, avant six critères de réception.",
        sum_es="El bies y el ribete pesan poco en el coste, pero revelan con más claridad la confección. Esta guía distingue bies, ribete y vistas —incluido su modo de presupuestar—, compara seis materiales y trata el corte a 45°, las anchuras acabadas y mermas, el encogimiento y la tensión, con seis criterios de recepción.",
    ),
    dict(
        slug="shoulder-pad-structure-trims-guide.html",
        body="blog/_body_shoulderpad.html",
        title_zh="垫肩与结构辅料选型指南：垫肩、胸衬与领底呢怎么选 | TAGE",
        title_en="Shoulder Pad &amp; Structure Trims Guide: Pads, Canvas, Collar Felt | TAGE",
        title_ja="肩パッド・構造副資材ガイド：肩パッド・胸芯・衿芯の選び方 | TAGE",
        title_ko="숄더 패드·구조 부자재 가이드: 패드, 심지, 칼라 펠트 | TAGE",
        title_fr="Guide des épaulières et accessoires de structure | TAGE",
        title_es="Guía de hombrillos y accesorios estructurales | TAGE",
        desc_zh="垫肩与结构辅料选型指南：对比海绵、针刺棉、复合、针织包覆与薄型五类垫肩，按西装、大衣、针织、连衣裙与童装倒推厚度与形状，讲清胸衬、领底呢、袖山条与牵条等配套结构件，并给出回弹、厚度公差与环保测试等验收口径。东莞泰阁包装。",
        desc_en="Shoulder pad guide: foam, needle-punch, composite, knit-covered and thin pads compared, thickness by garment type, plus chest canvas and collar felt specs.",
        desc_ja="肩パッドと構造副資材の選定ガイド。フォーム・ニードルパンチ・複合・生地巻き・薄型の5種類を比較し、スーツ・コート・ニット・ワンピース・子供服から厚みと形状を逆算、胸芯・衿芯・袖山テープの関連部材と検収基準を解説。東莞泰閣包装。",
        desc_ko="숄더 패드와 구조 부자재 선택 가이드. 폼·니들펀치·복합·원단 감쌈·박형 다섯 종류를 비교하고 정장·코트·니트·원피스·아동복에서 두께와 형태를 역산하며 가슴 심지·칼라 펠트·소매산 테이프와 검수 기준을 정리했습니다. 둥관 TAGE 패키징.",
        desc_fr="Guide des épaulières et accessoires de structure : cinq constructions comparées, épaisseur et forme selon le vêtement, plus toile de poitrine et feutre de col.",
        desc_es="Guía de hombrillos y accesorios estructurales: cinco construcciones comparadas, grosor y forma según la prenda, más tela de pecho y fieltro de cuello.",
        crumb_zh="垫肩与结构辅料选型指南",
        crumb_en="Shoulder Pad and Structure Trims Guide",
        crumb_ja="肩パッド・構造副資材ガイド",
        crumb_ko="숄더 패드·구조 부자재 가이드",
        crumb_fr="Guide des épaulières et accessoires de structure",
        crumb_es="Guía de hombrillos y accesorios estructurales",
        h1_zh="垫肩与结构辅料选型指南：垫肩、胸衬与领底呢怎么选",
        h1_en="Shoulder Pad and Structure Trims Guide: Pads, Chest Canvas and Collar Felt",
        h1_ja="肩パッドと構造副資材の選定：肩パッド・胸芯・衿芯の選び方",
        h1_ko="숄더 패드와 구조 부자재 선택: 패드, 가슴 심지, 칼라 펠트 고르기",
        h1_fr="Choisir ses épaulières et accessoires de structure : épaulière, toile de poitrine, feutre de col",
        h1_es="Elegir hombrillos y accesorios estructurales: hombrillo, tela de pecho y fieltro de cuello",
        tag_zh="辅料选型",
        tag_en="Trims Selection",
        tag_ja="副資材選定",
        tag_ko="부자재 선택",
        tag_fr="Choix d'accessoires",
        tag_es="Selección de accesorios",
        sum_zh="垫肩、胸衬与领底呢在成衣里几乎看不见，却决定肩线形状、版型寿命与穿着舒适度。本文对比海绵、针刺棉、复合、针织包覆与薄型五类垫肩，按西装、大衣、针织、连衣裙与童装倒推厚度与形状，讲清胸衬、领底呢、袖山条与牵条等配套结构件，并给出回弹、厚度公差与环保测试等验收口径。",
        sum_en="Shoulder pads, chest canvas and collar felt are invisible inside the garment yet decide the shoulder line, how long the shape holds and how it wears. This guide compares five pad constructions and works backwards from garment type to thickness and shape, covers the companion structural pieces, and sets out recovery, tolerance and compliance criteria.",
        sum_ja="肩パッド・胸芯・衿芯は完成した服の中では見えませんが、肩線の形、シルエットの持ち、着心地を決めます。本記事は5種類の肩パッドを比較し、品種から厚みと形状を逆算、関連する構造部材を整理し、反発性・厚み公差・環境試験などの検収基準を示します。",
        sum_ko="숄더 패드, 가슴 심지, 칼라 펠트는 완성된 옷 안에서 보이지 않지만 어깨선 형태, 실루엣 유지, 착용감을 결정합니다. 이 글은 다섯 가지 패드 구조를 비교하고 품목에서 두께와 형태를 역산하며 관련 구조 부품을 정리하고 복원력·두께 공차·환경 시험 등 검수 기준을 제시합니다.",
        sum_fr="Épaulières, toile de poitrine et feutre de col sont invisibles mais décident la ligne d'épaule, la tenue et le confort. Ce guide compare cinq constructions d'épaulières, part du type de vêtement pour l'épaisseur et la forme, couvre les pièces de structure associées et fixe les critères de retour, tolérance et conformité.",
        sum_es="Los hombrillos, la tela de pecho y el fieltro de cuello son invisibles, pero deciden la línea de hombro, la permanencia de la forma y el confort. Esta guía compara cinco construcciones de hombrillo, parte del tipo de prenda para grosor y forma, cubre las piezas de estructura asociadas y fija criterios de recuperación, tolerancia y cumplimiento.",
    ),
]
