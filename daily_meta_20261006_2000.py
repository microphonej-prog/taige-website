#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-06 晚间批次（20:00）每日更新：2 篇新文章元数据（六语：zh-Hant 根 / en / ja / ko / fr / es）

选题说明（主题池 30 项与历次扩展均已上线，本次沿「五金辅料的防锈与盐雾测试」与
「功能性服装（抗菌/防螨/吸湿速干/防紫外）的辅料与标签声明」两个尚未独立成文的方向扩展，
已核对 blog/、en|ja|ko|fr|es/blog/ 与 sitemap.xml 无同名文件、无重复 <loc>，
并 grep 全站确认关键词覆盖情况：

- trim-metal-salt-spray-guide       vs metal-trims-nickel-release-guide（只讲镍释放合规，不讲腐蚀路径与盐雾时长）、
  garment-buttons-fasteners-guide（第4节只讲镀层与耐洗的选项，不讲测试与判定）、
  zipper-selection-guide（只在拉链语境提到盐雾）、garment-wash-dye-trims-guide（讲能跟着洗，不讲金属腐蚀）；
  全站 grep「盐雾」仅 zipper 等 1 处正文、无独立文章；grep「电镀/電鍍」11 处均为顺带提及：
  本文讲清汗液、洗水、海运高湿与含酸包装四类腐蚀来源，镀镍/镀锌镍/仿金/枪色/无镍电镀按用途怎么选，
  中性盐雾 24/48/96 小时（ASTM B117、GB/T 10125）与「无红锈/无白锈」判定口径，
  洗水后生锈的五步排查顺序，以及包装仓储与询价验收清单。
- functional-garment-trims-label-guide vs care-label-wash-durability（只讲洗水标自身掉字）、
  trim-third-party-testing-guide（讲送检流程与成本）、care-label-standards（讲洗涤符号）、
  clothing-label-compliance-eu（讲合规标签项目）；
  全站 grep「抗菌」仅 1 处、「防螨」0 处、「吸湿排汗」0 处、「荧光增白」0 处：
  本文讲清功能服装的辅料清单（主唛/洗水标/吊牌/包装各负责什么）、
  抗菌（GB/T 20944.3、ISO 20743、AATCC 100）与防螨（GB/T 24253，驱避率与抑制率不可混用）的证据要求、
  吸湿速干（GB/T 21655.1、AATCC 195）的写法边界、防紫外（GB/T 18830，UPF>40 且 UVA<5%）
  与无荧光纸品的连带要求，以及功能声明的红线与内部审核清单。
"""

ARTICLES = [
    dict(
        slug="trim-metal-salt-spray-guide.html",
        body="blog/_body_saltspray.html",
        title_zh="五金辅料防锈与盐雾测试指南：电镀选型、耐洗与验收 | TAGE",
        title_en="Metal Trim Rust and Salt-Spray Guide: Plating, Washing, Acceptance | TAGE",
        title_ja="金属副資材の錆と塩水噴霧ガイド：めっき選定・耐洗性・検収 | TAGE",
        title_ko="금속 부자재 녹과 염수분무 가이드: 도금 선정·내세탁·검수 | TAGE",
        title_fr="Rouille et brouillard salin des accessoires métalliques : dépôt et réception | TAGE",
        title_es="Óxido y niebla salina en accesorios metálicos: recubrimiento y recepción | TAGE",
        desc_zh="五金辅料防锈指南：讲清纽扣、四合扣、拉头与扣具的腐蚀来源，镀镍、镀锌镍、仿金与无镍电镀怎么按用途选，盐雾 24/48/96 小时与无红锈判定口径怎么写，洗水后生锈的五步排查顺序，以及包装、仓储与询价验收清单。来自东莞泰阁包装。",
        desc_en="Metal trim rust guide: corrosion sources on buttons, snaps and sliders, plating choice by use, salt-spray 24/48/96 hours with pass criteria, plus wash troubleshooting.",
        desc_ja="金属副資材の錆・防食ガイド。ボタン、スナップ、スライダーなど金具の腐食要因、用途別のめっき選定、塩水噴霧24・48・96時間と赤錆なしの判定基準、洗濯後の錆の切り分け手順、包装・保管・見積のチェックリストを解説。東莞泰閣包装。",
        desc_ko="금속 부자재 녹·방청 가이드. 단추, 스냅, 슬라이더 등 금구의 부식 원인, 용도별 도금 선택, 염수분무 24·48·96시간과 적청 없음 판정 기준, 세탁 후 녹 점검 순서, 포장·보관·견적 체크리스트를 정리했습니다. 둥관 TAGE 패키징.",
        desc_fr="Guide rouille des accessoires métalliques : sources de corrosion, choix du dépôt selon l'usage, brouillard salin 24/48/96 heures et critères, diagnostic après lavage.",
        desc_es="Guía de óxido en accesorios metálicos: fuentes de corrosión, elección de recubrimiento, niebla salina 24/48/96 horas y criterios, diagnóstico tras el lavado.",
        crumb_zh="五金防锈指南",
        crumb_en="Metal Trim Rust",
        crumb_ja="金具の防錆",
        crumb_ko="금속 부자재 방청",
        crumb_fr="Rouille des métaux",
        crumb_es="Óxido en metales",
        h1_zh="五金辅料防锈与盐雾测试指南：电镀选型、耐洗与验收",
        h1_en="Metal Trim Rust and Salt-Spray Guide: Plating, Washing and Acceptance",
        h1_ja="金属副資材の錆と塩水噴霧ガイド：めっき選定・耐洗性・検収",
        h1_ko="금속 부자재 녹과 염수분무 가이드: 도금 선정·내세탁·검수",
        h1_fr="Rouille des accessoires métalliques : dépôt, lavage et réception",
        h1_es="Óxido en accesorios metálicos: recubrimiento, lavado y recepción",
        tag_zh="工艺指南",
        tag_en="Process Guide",
        tag_ja="加工ガイド",
        tag_ko="공정 가이드",
        tag_fr="Guide des procédés",
        tag_es="Guía de procesos",
        sum_zh="五金件是成衣上最容易生锈的部分，锈点出现在成品或门店样衣上就是返工或索赔，根因往往在镀层厚度、洗水条件与包装防护。本文讲清汗液、洗水、海运高湿与含酸包装四类腐蚀来源，给出镀镍、镀锌镍、仿金、枪色与无镍电镀按用途的选型逻辑，说明中性盐雾 24/48/96 小时该按什么场景约定、判定要写清无红锈还是无白锈，并给出洗水后生锈的五步排查顺序与可直接写进询价单的验收清单。",
        sum_en="Metal trims are the parts of a garment most likely to rust, and a rust spot on a finished garment or showroom sample means rework or a claim. This guide covers the four corrosive environments — sweat, garment washing, humid sea freight and acidic packaging — then the selection logic for nickel, zinc-nickel, imitation gold, gunmetal and nickel-free plating, how to agree 24/48/96 hours of neutral salt spray by use case, why the criterion must state red or white rust, and the five-step troubleshooting order after washing with an acceptance checklist for your quotation request.",
        sum_ja="金属副資材は衣料で最も錆びやすい部分であり、製品や店頭サンプルに錆が出れば手直しかクレームになります。原因は生地ではなく、めっき厚・洗い条件・包装保護にあります。本記事は汗、製品洗い、海上輸送の高湿度、酸性包装という4つの腐食環境を整理し、ニッケル、亜鉛ニッケル、金調、ガンメタル、ニッケルフリーめっきの用途別選定、中性塩水噴霧24・48・96時間の使い分けと赤錆・白錆の判定、洗濯後の錆の5段階の切り分け手順、見積にそのまま書ける検収リストをまとめます。",
        sum_ko="금속 부자재는 의류에서 녹이 가장 잘 슬기 쉬운 부분이며, 완성품이나 매장 샘플에 녹점이 생기면 재작업이나 클레임으로 이어집니다. 원인은 원단이 아니라 도금 두께, 세탁 조건, 포장 보호입니다. 이 글은 땀, 제품 세탁, 해상 운송의 고습도, 산성 포장이라는 네 가지 부식 환경을 정리하고, 니켈·아연-니켈·모조 골드·건메탈·무니켈 도금의 용도별 선택, 중성 염수분무 24·48·96시간의 적용 기준과 적청·백청 판정, 세탁 후 녹 발생 시 다섯 단계 점검 순서, 견적서에 바로 쓸 수 있는 검수 목록을 제공합니다.",
        sum_fr="Les accessoires métalliques sont les pièces les plus sujettes à la rouille, et une tache sur un produit fini ou un modèle de showroom signifie reprise ou réclamation : la cause est rarement le tissu mais l'épaisseur du dépôt, le lavage et la protection d'emballage. Ce guide couvre les quatre milieux corrosifs — sueur, lavage en pièce, transport maritime humide et emballage acide — puis la logique de choix entre nickel, zinc-nickel, imitation or, gunmetal et dépôt sans nickel, comment convenir de 24/48/96 heures de brouillard salin selon l'usage, pourquoi le critère doit préciser rouille rouge ou blanche, l'ordre de diagnostic en cinq étapes après lavage et une liste de réception à recopier dans votre demande de prix.",
        sum_es="Los accesorios metálicos son las piezas con más riesgo de óxido en una prenda, y una mancha en un producto acabado o una muestra de showroom significa retrabajo o reclamación: la causa rara vez es el tejido, sino el espesor del recubrimiento, el lavado y la protección del embalaje. Esta guía repasa los cuatro medios corrosivos —sudor, lavado en prenda, transporte marítimo húmedo y embalaje ácido—, la lógica de elección entre níquel, zinc-níquel, imitación oro, gunmetal y recubrimiento sin níquel, cómo acordar 24/48/96 horas de niebla salina según el uso, por qué el criterio debe indicar óxido rojo o blanco, el orden de diagnóstico en cinco pasos tras el lavado y una lista de recepción para copiar en tu solicitud de precio.",
    ),
    dict(
        slug="functional-garment-trims-label-guide.html",
        body="blog/_body_functional.html",
        title_zh="功能性服装辅料与标签声明指南：抗菌、防螨、吸湿排汗 | TAGE",
        title_en="Functional Apparel Trims and Label Claims: Antibacterial, Wicking | TAGE",
        title_ja="機能衣料の副資材と表示ガイド：抗菌・防ダニ・吸湿速乾 | TAGE",
        title_ko="기능성 의류 부자재와 표기 가이드: 항균·방진드기·흡습속건 | TAGE",
        title_fr="Accessoires techniques et allégations : antibactérien, évacuation | TAGE",
        title_es="Accesorios técnicos y alegaciones: antibacteriano, evacuación | TAGE",
        desc_zh="功能性服装辅料指南：讲清主唛、洗水标、吊牌与包装各自承担什么，抗菌（GB/T 20944.3）与防螨（GB/T 24253）声明需要哪些检测支撑，吸湿速干（GB/T 21655.1）怎么写不越界，防紫外（UPF 40 以上）与无荧光纸品的连带要求，以及功能声明的红线与询价验收清单。来自东莞泰阁包装。",
        desc_en="Functional apparel trims guide: what each label and bag must do, the tests behind antibacterial and anti-mite claims, wicking and UV wording, and brightener-free paper.",
        desc_ja="機能衣料の副資材ガイド。メインラベル・洗濯表示・タグ・包装の役割、抗菌（GB/T 20944.3）と防ダニ（GB/T 24253）表示に必要な試験、吸湿速乾（GB/T 21655.1）の書き方、UVカットと無蛍光紙の要件、機能表示のレッドラインと見積チェックリストを解説。東莞泰閣包装。",
        desc_ko="기능성 의류 부자재 가이드. 메인 라벨·세탁 라벨·행택·포장의 역할, 항균(GB/T 20944.3)과 방진드기(GB/T 24253) 표기에 필요한 시험, 흡습속건(GB/T 21655.1) 문구 작성법, 자외선 차단과 무형광지 요건, 기능 표기의 레드라인과 견적 체크리스트를 정리했습니다. 둥관 TAGE 패키징.",
        desc_fr="Guide des accessoires techniques : rôle de chaque label et sachet, essais derrière les allégations antibactériennes et anti-acariens, rédaction évacuation et UV, papier sans azurant.",
        desc_es="Guía de accesorios técnicos: función de cada etiqueta y bolsa, ensayos tras las alegaciones antibacterianas y antiácaros, redacción de evacuación y UV, papel sin blanqueador.",
        crumb_zh="功能服装辅料",
        crumb_en="Functional Apparel Trims",
        crumb_ja="機能衣料の副資材",
        crumb_ko="기능성 의류 부자재",
        crumb_fr="Accessoires techniques",
        crumb_es="Accesorios técnicos",
        h1_zh="功能性服装辅料与标签声明指南：抗菌、防螨、吸湿排汗",
        h1_en="Functional Apparel Trims and Label Claims: Antibacterial, Wicking and UV",
        h1_ja="機能衣料の副資材と表示ガイド：抗菌・防ダニ・吸湿速乾とUV",
        h1_ko="기능성 의류 부자재와 표기 가이드: 항균·방진드기·흡습속건",
        h1_fr="Accessoires et allégations pour vêtements techniques : antibactérien, évacuation, UV",
        h1_es="Accesorios y alegaciones para prendas técnicas: antibacteriano, evacuación, UV",
        tag_zh="合规指南",
        tag_en="Compliance Guide",
        tag_ja="コンプライアンス",
        tag_ko="컴플라이언스",
        tag_fr="Guide conformité",
        tag_es="Guía de cumplimiento",
        sum_zh="抗菌、防螨、吸湿排汗、防紫外这些功能词，问题往往不出在面料，而出在最后一步：吊牌写得比检测报告更满，或洗水标用了不耐洗的涂层材质，验货时被判虚假宣传。本文讲清功能服装的辅料清单与各自职责，抗菌与防螨声明需要的方法编号、菌种与洗涤次数，吸湿速干与防紫外的写法边界（UPF 40 以上、UVA 小于 5%），无荧光纸品与防紫外线面料的连带要求，以及把功能声明纳入辅料规格书审核的清单。",
        sum_en="With functional apparel, the failure usually comes at the last step rather than from the fabric: a hang tag that promises more than the test report, or a care label in a coated material that cannot survive repeated washing, and the lot is stopped at inspection for misleading claims. This guide sets out the trim list for a functional garment and what each item carries, the method numbers, strains and wash counts behind antibacterial and anti-mite claims, the wording limits for wicking and UV (UPF above 40, UVA under 5%), the knock-on requirement for brightener-free paper, and a checklist to fold functional claims into the trims spec sheet.",
        sum_ja="機能衣料では、問題は生地ではなく最後の工程で起こります。タグが試験報告書以上の機能をうたい、洗濯表示が耐久性の低いコーティング素材で、検品時に不当表示と判定されるケースです。本記事は機能衣料の副資材リストと各々の役割、抗菌・防ダニ表示に必要な方法番号・菌種・洗濯回数、吸湿速乾とUVカットの書き方の限界（UPF40超、UVA5%未満）、無蛍光紙の連帯要件、機能表示を副資材規格書の審査に組み込むチェックリストを示します。",
        sum_ko="기능성 의류에서는 문제가 원단이 아니라 마지막 단계에서 생깁니다. 행택이 시험 성적서보다 과한 기능을 표기하거나, 세탁 라벨이 반복 세탁에 약한 코팅 소재여서 검품에서 허위 표시로 판정되는 경우입니다. 이 글은 기능성 의류의 부자재 목록과 각 품목의 역할, 항균·방진드기 표기에 필요한 방법 번호·균종·세탁 횟수, 흡습속건과 자외선 차단의 문구 한계(UPF 40 초과, UVA 5% 미만), 무형광지의 연쇄 요건, 기능 표기를 부자재 사양서 검토에 포함하는 체크리스트를 제시합니다.",
        sum_fr="Sur un vêtement technique, l'échec vient rarement du tissu mais de la dernière étape : une étiquette suspendue qui promet plus que le rapport d'essai, ou une étiquette d'entretien enduite qui ne supporte pas les lavages répétés — et le lot est bloqué en inspection. Ce guide présente la liste d'accessoires et le rôle de chacun, les numéros de méthode, souches et lavages derrière les allégations antibactériennes et anti-acariens, les limites de rédaction pour l'évacuation et l'UV (UPF supérieur à 40, UVA sous 5 %), l'exigence induite d'un papier sans azurant, et une liste pour intégrer ces allégations à la fiche technique des accessoires.",
        sum_es="En una prenda técnica, el fallo suele llegar en el último paso y no en el tejido: una etiqueta colgante que promete más que el informe de ensayo, o una etiqueta de cuidado con recubrimiento que no soporta lavados repetidos, y el lote se detiene en inspección. Esta guía presenta la lista de accesorios y la función de cada uno, los números de método, cepas y lavados tras las alegaciones antibacterianas y antiácaros, los límites de redacción para evacuación y UV (UPF superior a 40, UVA por debajo del 5 %), el requisito derivado de papel sin blanqueador y una lista para integrar estas alegaciones en la ficha técnica.",
    ),
]
