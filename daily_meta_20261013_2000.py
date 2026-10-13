#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-13 晚间批次（20:00）每日更新：2 篇新文章元数据（六语：zh-Hant 根 / en / ja / ko / fr / es）

选题说明（主题池 30 项连同既有扩展均已上线，本次沿两条尚未成文、且全站扫描确认为空白的线索扩展，
已核对 blog/、en|ja|ko|fr|es/blog/ 与 sitemap.xml 无重复 slug）：

- apparel-relabeling-service-guide.html：服装换标（改标）服务指南。
  全站扫描：「换标服务」0 处、「改标服务」0 处、「标签替换」0 处、「重贴」仅 4 处（全在
  _body_retail.html 讲门店贴标）、「换标」8 处（_body_epr 讲换标识版本、_body_functional 讲换标签重做、
  _body_itch 讲临时尺码标，均为顺带提及），没有把「把成品上的吊牌/洗标/条码按新市场渠道换掉」
  这种作业单独成文。既有相关文章分工：retail-floor-ready-apparel-packaging 讲零售上架包装与箱唛、
  hang-tag-barcode-guide 讲条码格式本体、care-label-attachment-guide 讲洗标缝制方式、
  clothing-label-compliance-eu 讲欧盟标签合规要求。
  本文落点是「六种触发换标的场景 → 换标牵动的六类辅料与漏点对照表 → 拆旧换新/覆盖贴标/整件重做三种作业方式
  → 最容易出事的六处（旧标残留、拆标伤面料、缝回不一致、条码与系统脱节、合规信息半做、授权与责任）
  → 报价两条线与抽查验收」。不涉及价格数字，只讲报价结构与作业口径。

- secondhand-resale-apparel-label-guide.html：二手与转售服装的标签辅料指南。
  全站扫描：「二手服装」0 处、「二手衣」0 处、「旧衣」0 处、「翻新」0 处、「转售」0 处、「寄卖」0 处、
  「服装回收」0 处、「以旧换新」0 处、「二手」仅 2 处（eu-digital-product-passport-trims 顺带举例）、
  「租赁」14 处（_body_bridal 讲租赁洗护、_body_socialaudit 讲劳务）；「Vinted / Depop / ThredUp」0 处。
  既有相关文章分工：eu-digital-product-passport-trims 讲 DPP 数据准备、care-label-wash-durability 讲洗标耐洗次数、
  clothing-size-label-guide 讲尺码体系、bridal-eveningwear-trims-guide 只覆盖婚纱礼服。
  本文落点是「转售与租赁的三个标签痛点 → 需要补齐的六种辅料对照表 → 按洗护次数而非新品标准选材
  → 合规与平台要求的边界（真实性、翻新如实标注、DPP 方向、平台规则比法规更细）
  → 翻新分级六步流程」。法规只写方向与做法，不引用具体编号与限值，不编造价格。
"""

ARTICLES = [
    dict(
        slug="apparel-relabeling-service-guide.html",
        body="blog/_body_relabel.html",
        title_zh="服装换标服务指南：吊牌、洗水标与条码更换流程 | TAGE",
        title_en="Apparel Relabeling Guide: Hang Tags, Care Labels and Barcodes | TAGE",
        title_ja="衣料のラベル張り替えガイド：タグ・洗濯表示・バーコードの交換 | TAGE",
        title_ko="의류 리라벨링 가이드: 행택·세탁 라벨·바코드 교체 | TAGE",
        title_fr="Guide du réétiquetage : étiquettes pendantes, d'entretien et codes-barres | TAGE",
        title_es="Guía del reetiquetado: colgantes, etiquetas de cuidado y códigos de barras | TAGE",
        desc_zh="服装换标服务指南：六种必须换标的场景、吊牌主唛洗水标尺码标条码贴六类辅料怎么处理、拆旧换新与覆盖贴标如何取舍、最容易出事的六处细节，以及换标报价结构与验收抽查方法。来自东莞泰阁包装。",
        desc_en="Apparel relabeling guide: when a relabel is unavoidable, the six trim items involved, unpicking versus overlabelling, six risks and how to quote and inspect.",
        desc_ja="衣料のラベル張り替えガイド。張り替えが必要な6つの場面、関わる6種類の副資材、旧ラベル撤去と上貼りの比較、事故になりやすい6つの細部、見積り構造と検収のやり方までを解説します。東莞泰閣包装。",
        desc_ko="의류 리라벨링 가이드. 리라벨링이 필요한 여섯 상황, 관련된 여섯 가지 부자재, 떼고 교체하기와 덧붙이기 비교, 사고가 잦은 여섯 가지 세부, 견적 구조와 검수 방법을 정리했습니다. 둥관 TAGE 패키징.",
        desc_fr="Guide du réétiquetage : quand il est inévitable, les six accessoires concernés, découdre ou superposer, six risques et comment chiffrer et contrôler.",
        desc_es="Guía del reetiquetado: cuándo es inevitable, los seis accesorios implicados, descoser o sobreetiquetar, seis riesgos y cómo presupuestar e inspeccionar.",
        crumb_zh="服装换标服务",
        crumb_en="Apparel Relabeling",
        crumb_ja="衣料のラベル張り替え",
        crumb_ko="의류 리라벨링",
        crumb_fr="Réétiquetage de vêtements",
        crumb_es="Reetiquetado de prendas",
        h1_zh="服装换标服务指南：吊牌、洗水标与条码怎么换",
        h1_en="Apparel Relabeling Guide: Swapping Hang Tags, Care Labels and Barcodes",
        h1_ja="衣料のラベル張り替えガイド：タグ・洗濯表示ラベル・バーコードの交換",
        h1_ko="의류 리라벨링 가이드: 행택, 세탁 라벨, 바코드 교체",
        h1_fr="Guide du réétiquetage : étiquettes pendantes, d'entretien et codes-barres",
        h1_es="Guía del reetiquetado: colgantes, etiquetas de cuidado y códigos de barras",
        tag_zh="服务指南",
        tag_en="Service Guide",
        tag_ja="サービスガイド",
        tag_ko="서비스 가이드",
        tag_fr="Guide service",
        tag_es="Guía de servicio",
        sum_zh="换标看起来只是换一张吊牌，实际同时牵动面料、线迹、库存系统与合规责任四件事。文章先列出六种必须换标的场景：目标市场法规更新、渠道从正价转折扣或跨境平台、代工转自有品牌、尺码体系切换、电商仓与零售客户的条码与箱唛要求、以及吊牌洗标自然损耗。第二部分用一张对照表把换标真正牵动的六类辅料摊开——吊牌、主唛、洗水标、尺码标、条码与价格贴、包装与封口贴，并列出各自最容易漏的点，例如吊绳新旧混装、拆主唛后领口留针孔、洗标语言版本少一种、条码与库存系统不同步、旧渠道电话残留在袋上。第三部分对比三种作业方式：拆旧换新外观最干净但人工与损耗最高，覆盖贴标快而省但要先确认目标市场允许且须查厚度与洗后脱落，整件重做只在皮标压印、烫印、激光刻字这类无法处理时使用，按新单排产。第四部分列六处最容易出事的细节：旧标没清干净、拆标伤面料、缝回位置与针距不一致、条码与系统脱节、合规信息只做一半、授权与责任没写清。最后给出报价结构——辅料成本加按件作业费，并说明要问清换标数量与分箱、旧标类型、目标市场与语言清单、交期与作业地点四件事，验收按箱数与件数双重抽样并留标准样存档。",
        sum_en="A relabel looks like swapping one hang tag, yet it moves fabric, stitching, inventory systems and compliance liability at once. The article opens with six situations that force a relabel: changed market rules, a channel move from full price to off-price or cross-border, contract manufacturing turning into an own brand, a size-system switch, e-commerce and retail barcode and carton demands, and plain wear on the labels themselves. Part two spreads the six trim items a relabel really touches across a comparison table — hang tag, neck label, care label, size label, barcode and price ticket, packing and seal labels — with the point most often missed for each: old and new strings mixed, needle holes left at the neckline after unpicking, one language version short on the care label, a barcode out of sync with the stock system, the old hotline still printed on the bag. Part three compares three methods: unpicking gives the cleanest look at the highest labour and damage cost; overlabelling is fast and cheap but must be accepted by the target market and checked for thickness and wash loss; full rework is reserved for debossed leather, heat transfer or laser marking that cannot be removed, and is scheduled as a new order. Part four lists the six details that go wrong most: old labels left behind, fabric damaged while unpicking, inconsistent resewing position and stitch, barcodes out of step with the system, compliance done by halves, and vague authorization and liability. It closes with the quote structure — trim cost plus a per-piece processing fee — the four questions to answer before pricing, and a double sampling inspection by carton and by piece with an archived reference.",
        sum_ja="張り替えはタグ一枚の交換に見えますが、生地・縫い目・在庫システム・コンプライアンス責任の四つが同時に動きます。まず張り替えが必要になる6つの場面を示します。市場規則の改正、定価からアウトレットや越境プラットフォームへのチャネル移動、OEM から自社ブランドへの転換、サイズ体系の切り替え、EC 倉庫や小売のバーコードと外装表示の要件、ラベル自体の消耗です。第2部では、張り替えが実際に関わる6種類の副資材（タグ・メインラベル・洗濯表示・サイズラベル・バーコードと値札・包装と封緘シール）を対照表にまとめ、それぞれの抜けやすい点を並べます。旧ひもと新ひもの混在、解いた後の衿ぐりの針穴、洗濯表示の言語版不足、在庫システムとの不一致、袋に残る旧問い合わせ先などです。第3部は三方式の比較で、旧ラベルを外す方式は最もきれいですが手間と損耗が最大、上貼りは速く安いものの対象市場が認める方式かを確認し厚みと洗濯後の脱落を検証する必要があり、作り直しは型押しレザー・熱転写・レーザー刻印など処理不能な場合に限り新規注文として生産します。第4部は事故になりやすい6つの細部（旧ラベルの取り残し、解く際の生地傷、縫い直しの位置と縫い目の不一致、バーコードとシステムのずれ、適合情報が中途半端、権限と責任の不明確）です。最後に、副資材費と1枚あたり作業費という見積り構造、価格提示前に明確にすべき4点、箱数と枚数の二重抜き取りと基準見本の保管を示します。",
        sum_ko="리라벨링은 행택 한 장을 바꾸는 일처럼 보이지만 원단, 봉제선, 재고 시스템, 컴플라이언스 책임 네 가지가 동시에 움직입니다. 글은 먼저 리라벨링이 필요한 여섯 상황을 제시합니다. 시장 규정 변경, 정가에서 아울렛이나 크로스보더 플랫폼으로의 채널 이동, OEM에서 자체 브랜드 전환, 사이즈 체계 전환, 이커머스 창고와 리테일의 바코드·박스 마크 요건, 라벨 자체의 마모입니다. 두 번째 부분은 리라벨링이 실제로 건드리는 여섯 가지 부자재(행택, 메인 라벨, 세탁 라벨, 사이즈 라벨, 바코드와 가격표, 포장과 봉인 라벨)를 대조표로 정리하고 각 항목에서 자주 빠지는 점을 짚습니다. 옛 끈과 새 끈 혼용, 뜯은 뒤 목선의 바늘 구멍, 세탁 라벨 언어판 누락, 재고 시스템과의 불일치, 봉투에 남은 옛 고객센터 번호 등입니다. 세 번째 부분은 세 방식 비교로, 떼고 교체하는 방식은 가장 깔끔하지만 인건비와 손실이 최대이고, 덧붙이기는 빠르고 저렴하지만 대상 시장 허용 여부와 두께·세탁 후 탈락을 확인해야 하며, 전면 재작업은 가죽 엠보싱·열전사·레이저 각인처럼 처리 불가능한 경우에만 신규 주문으로 생산합니다. 네 번째 부분은 사고가 잦은 여섯 세부(기존 라벨 미제거, 뜯을 때 원단 손상, 재봉 위치와 간격 불일치, 바코드와 시스템 불일치, 컴플라이언스 정보 반쪽 작성, 권한과 책임 불명확)입니다. 마지막으로 부자재 비용과 장당 작업비라는 견적 구조, 가격 제시 전에 명확히 할 네 가지, 박스 수와 장수 이중 샘플링과 기준 샘플 보관을 제시합니다.",
        sum_fr="Un réétiquetage ressemble au remplacement d'une étiquette pendante, mais il déplace à la fois le tissu, les coutures, le système de stock et la responsabilité de conformité. L'article ouvre sur six situations qui l'imposent : évolution de la réglementation, passage du plein tarif au déstockage ou au transfrontalier, bascule du façonnage vers une marque propre, changement de système de tailles, exigences code-barres et carton de l'e-commerce et du retail, et usure des étiquettes elles-mêmes. La deuxième partie déploie les six accessoires réellement concernés — étiquette pendante, label de col, étiquette d'entretien, étiquette de taille, code-barres et ticket de prix, emballage et scellés — dans un tableau, avec le point le plus souvent oublié pour chacun : ficelles anciennes et neuves mélangées, trous d'aiguille à l'encolure après décousage, une version linguistique manquante, un code-barres désynchronisé du stock, l'ancienne hotline encore imprimée sur le sachet. La troisième partie compare trois méthodes : découdre donne le rendu le plus propre au coût le plus élevé en main-d'oeuvre et en casse ; la superposition est rapide et économique mais doit être acceptée par le marché cible et contrôlée en épaisseur et tenue au lavage ; refaire entièrement est réservé au cuir gaufré, au transfert à chaud ou au marquage laser, planifié comme une commande neuve. La quatrième partie liste les six détails qui tournent mal : étiquettes oubliées, tissu abîmé, position et piqûre irrégulières, codes-barres désynchronisés, conformité à moitié faite, autorisation et responsabilité floues. Elle se clôt sur la structure du devis — coût des accessoires plus façon à la pièce — les quatre questions à trancher avant de chiffrer, et un double échantillonnage cartons et pièces avec pièce de référence archivée.",
        sum_es="Un reetiquetado parece cambiar un colgante, pero mueve a la vez tejido, costuras, sistema de inventario y responsabilidad de cumplimiento. El artículo abre con seis situaciones que lo obligan: cambio normativo, paso de precio completo a descuento o transfronterizo, giro de la maquila a marca propia, cambio de sistema de tallas, exigencias de códigos de barras y cartón del comercio electrónico y el retail, y desgaste de las propias etiquetas. La segunda parte despliega en una tabla los seis accesorios realmente implicados — colgante, etiqueta de cuello, de cuidado, de talla, código de barras y ticket de precio, embalaje y precintos — con el punto que más se olvida en cada uno: cordones viejos y nuevos mezclados, agujeros de aguja en el escote tras descoser, una versión de idioma de menos, un código desincronizado del stock, el antiguo teléfono aún impreso en la bolsa. La tercera compara tres métodos: descoser da el acabado más limpio al mayor coste en mano de obra y merma; sobreetiquetar es rápido y barato pero exige que el mercado destino lo acepte y un control de grosor y pérdida al lavar; rehacer por completo se reserva al cuero grabado, la transferencia térmica o el marcado láser y se planifica como pedido nuevo. La cuarta lista los seis detalles que más fallan: etiquetas antiguas sin retirar, tejido dañado al descoser, posición y puntada irregulares, códigos desincronizados, conformidad a medias y autorización y responsabilidad difusas. Cierra con la estructura del presupuesto — coste de accesorios más mano de obra por pieza — las cuatro preguntas a aclarar antes de cotizar y un doble muestreo por caja y por pieza con pieza de referencia archivada.",
    ),
    dict(
        slug="secondhand-resale-apparel-label-guide.html",
        body="blog/_body_resale.html",
        title_zh="二手与转售服装标签指南：洗水标、尺码标与分级挂牌 | TAGE",
        title_en="Second-Hand and Resale Apparel Labels Guide: Care, Size and Grade Tags | TAGE",
        title_ja="中古・リセール衣料のラベルガイド：洗濯表示・サイズ・等級タグ | TAGE",
        title_ko="중고·리셀 의류 라벨 가이드: 세탁·사이즈·등급표 | TAGE",
        title_fr="Guide des étiquettes seconde main : entretien, taille et grades | TAGE",
        title_es="Guía de etiquetas para segunda mano: cuidado, talla y grados | TAGE",
        desc_zh="二手与转售服装标签指南：洗水标模糊、尺码标不符、缺身份信息三个痛点，需要补齐的六类辅料，按洗护次数选材的方法，合规与平台规则的边界，以及翻新分级六步流程。来自东莞泰阁包装。",
        desc_en="Second-hand and resale apparel labels guide: faded care labels, size mismatches, six trims to restore, wash-cycle material choices and a six-step grading flow.",
        desc_ja="中古・リセール衣料のラベルガイド。洗濯表示の色あせ、サイズ不一致、識別情報の欠如という3つの課題、補うべき6種類の副資材、洗濯回数基準の選材、適合とプラットフォーム要件の境界、6段階の格付けフローを解説します。東莞泰閣包装。",
        desc_ko="중고·리셀 의류 라벨 가이드. 세탁 라벨 흐림, 사이즈 불일치, 식별 정보 부재 세 가지 문제와 보완할 여섯 가지 부자재, 세탁 횟수 기준 소재 선택, 컴플라이언스와 플랫폼 요건, 6단계 등급 작업 흐름을 정리했습니다. 둥관 TAGE 패키징.",
        desc_fr="Guide des étiquettes seconde main : entretien délavé, tailles incohérentes, six accessoires à restaurer, choix selon les cycles de lavage et flux de grading.",
        desc_es="Guía de etiquetas de segunda mano: cuidado descolorido, tallas incoherentes, seis accesorios a reponer, elección por ciclos de lavado y flujo de grados.",
        crumb_zh="二手与转售服装标签",
        crumb_en="Second-Hand and Resale Labels",
        crumb_ja="中古・リセールのラベル",
        crumb_ko="중고·리셀 라벨",
        crumb_fr="Étiquettes seconde main",
        crumb_es="Etiquetas de segunda mano",
        h1_zh="二手与转售服装标签指南：洗水标、尺码标与分级挂牌",
        h1_en="Second-Hand and Resale Apparel Labels Guide: Care, Size and Grade Tags",
        h1_ja="中古・リセール衣料のラベルガイド：洗濯表示・サイズ・等級タグ",
        h1_ko="중고·리셀 의류 라벨 가이드: 세탁 라벨, 사이즈 라벨, 등급표",
        h1_fr="Guide des étiquettes pour la seconde main : entretien, taille et grades",
        h1_es="Guía de etiquetas para segunda mano: cuidado, talla y grados",
        tag_zh="趋势与合规",
        tag_en="Trends and Compliance",
        tag_ja="トレンドと適合",
        tag_ko="트렌드와 컴플라이언스",
        tag_fr="Tendances et conformité",
        tag_es="Tendencias y cumplimiento",
        sum_zh="二手与转售生意的第一道门槛不是货源，而是标签。文章先讲三个最容易卡住的痛点：反复洗涤与干洗把涂层洗标的字迹磨掉，买家看不到成分与洗护方式；旧标脱落、改过或成衣缩水后，标称尺码已经不可信，而尺码争议是转售最怕的事；缺少可追溯的身份信息，货号、成色等级、洗护记录只能靠人工登记，规模一大就乱。第二部分用对照表列出要补齐的六类辅料：洗水标说明仍然有效的成分与洗护、尺码标统一筛选口径、吊牌与分级牌承载品牌与成色、内码与身份标签串起货号与批次、包装袋兼顾防尘防潮与开箱体验、安全与防伪件服务高价值品类，并逐一给出补做时的重点。第三部分讲选材要按洗护次数而不是新品标准：织带类洗标靠纤维显色最耐洗，涂层印刷洗标信息量大但要做洗护老化实测，租赁礼服与西装要选耐干洗与耐熨烫的材质，缝制用两端回针比胶粘与热压耐久，深色面料配浅色标签要防染色与渗色。第四部分划清合规与平台要求的边界：二手与翻新商品在多数市场并不享有旧货豁免，纤维成分、洗护方式、原产地与进口商信息仍需可提供；真实性高于一切，翻新与修复要如实标注，欧盟数字产品护照方向要求信息可查询，而平台规则在成色用词、尺码填写与旧标可否露出上往往比法规更细。最后给出翻新分级六步流程：收件查验、清洁整理、检修换标、按标准分级、挂牌拍照上架、包装发运。",
        sum_en="In second-hand and resale apparel the first barrier is rarely sourcing — it is labelling. The article opens with the three pain points that block most often: repeated washing and dry cleaning wearing the print off coated care labels until composition and care are invisible; size labels fallen off, altered, or invalidated by shrinkage, while size disputes are what resale fears most; and no traceable identity, leaving item number, condition grade and care history to manual logging that collapses at volume. Part two uses a comparison table for the six items to restore: care labels that state which composition and care still apply, size labels that unify the filtering logic, hang tags and grade tags carrying brand and condition, internal ID labels tying item number and batch together, packaging that handles dust, moisture and unboxing, and security or authenticity parts for high-value categories — each with the point that matters when it is remade. Part three argues that materials should be chosen by number of wash cycles rather than new-garment standards: woven labels colour through the fibre and last longest, coated printed labels hold more information but need a real wash-ageing test, rental gowns and suits need dry-clean and ironing resistance, backstitching both ends outlasts glue or heat pressing, and a pale label on dark fabric needs a dye-bleed check. Part four draws the line between compliance and platform rules: used and refurbished goods rarely enjoy a blanket exemption, authenticity outranks everything, refurbishment must be disclosed honestly, the EU digital product passport direction points to retrievable data, and platform rules on grade wording, size entry and visible old labels are often finer than the law. It closes with a six-step refurbishment and grading flow from intake inspection to packing and shipping.",
        sum_ja="中古とリセール事業の最初の壁は仕入れではなくラベルです。まず最も止まりやすい3つの課題を示します。洗濯とドライを重ねてコーティング洗濯表示の印字が摩耗し組成と手入れが見えなくなること、旧ラベルの脱落・書き換え・縮みで表示サイズが信用できなくなること（リセールが最も避けたいサイズ紛争につながります）、そして追跡可能な識別情報がなく品番・状態等級・手入れ履歴が手作業記録に頼り規模拡大で破綻することです。第2部は補うべき6種類の副資材を対照表にまとめます。有効な組成と手入れを示す洗濯表示、絞り込み基準を統一するサイズラベル、ブランドと状態を担うタグと等級札、品番とロットを結ぶ社内 ID ラベル、防塵と防湿と開封体験を担う包装袋、高額品向けのセキュリティと真贋パーツで、それぞれ作り直す際の要点を添えます。第3部は新品基準ではなく洗濯回数で選材すべきだと説きます。織りテープは繊維発色で最も耐洗、コーティング印刷は情報量が多いが実際の洗濯劣化試験が必要、レンタルのドレスとスーツはドライとアイロン耐性が必要、縫い付けは両端の返し縫いが接着や熱圧着より長持ち、濃色生地に淡色ラベルは染色と移染の確認が必要です。第4部は適合とプラットフォーム要件の線引きです。中古とリフレッシュ品は多くの市場で一括免除とならず、繊維組成・手入れ・原産地・輸入者情報は提示できる必要があります。真贋が最優先で、リフレッシュは正直に表示し、EU のデジタル製品パスポートは情報照会の方向を示し、プラットフォーム規約は等級用語・サイズ入力・旧ラベルの写り込みで法規より細かいことが多いです。最後に受入検品から包装発送までの6段階フローを示します。",
        sum_ko="중고와 리셀 사업의 첫 장벽은 매입이 아니라 라벨입니다. 글은 가장 자주 막히는 세 가지를 먼저 다룹니다. 반복 세탁과 드라이클리닝으로 코팅 세탁 라벨의 인쇄가 닳아 조성과 관리 방법이 보이지 않는 문제, 기존 라벨이 떨어지거나 수정되거나 원단이 줄어 표기 사이즈를 믿을 수 없게 되는 문제(리셀이 가장 두려워하는 사이즈 분쟁으로 이어집니다), 그리고 추적 가능한 식별 정보가 없어 품번·상태 등급·관리 이력이 수기 기록에 의존하다 규모가 커지면 무너지는 문제입니다. 두 번째 부분은 보완해야 할 여섯 가지 부자재를 대조표로 정리합니다. 유효한 조성과 관리를 알리는 세탁 라벨, 필터 기준을 통일하는 사이즈 라벨, 브랜드와 상태를 담는 행택과 등급표, 품번과 배치를 연결하는 내부 ID 라벨, 방진·방습과 개봉 경험을 담당하는 포장 봉투, 고가 품목용 보안·정품 부품이며 각각 재제작 시 핵심을 덧붙입니다. 세 번째 부분은 신품 기준이 아니라 세탁 횟수로 소재를 골라야 한다고 설명합니다. 직조 테이프는 섬유 발색으로 가장 오래가고, 코팅 인쇄는 정보량이 많지만 실제 세탁 노화 시험이 필요하며, 렌탈 드레스와 정장은 드라이와 다림질 내성이 필요하고, 봉제는 양끝 되박기가 접착이나 열압착보다 오래가며, 어두운 원단에 밝은 라벨은 이염과 착색을 확인해야 합니다. 네 번째 부분은 컴플라이언스와 플랫폼 요건의 경계입니다. 중고와 리퍼비시 제품은 대부분 시장에서 일괄 면제되지 않고 섬유 조성·관리·원산지·수입자 정보를 제시할 수 있어야 합니다. 진위가 최우선이며 리퍼비시는 정직하게 표시하고, EU 디지털 제품 여권은 정보 조회 방향을 보여주며, 플랫폼 규정은 등급 용어·사이즈 입력·옛 라벨 노출에서 법규보다 세밀한 경우가 많습니다. 마지막으로 입고 검수부터 포장 발송까지 여섯 단계 흐름을 제시합니다.",
        sum_fr="Dans la seconde main et la revente, le premier obstacle n'est pas l'approvisionnement : c'est l'étiquetage. L'article ouvre sur trois points de blocage récurrents : lavages et nettoyages à sec répétés effaçant l'impression des étiquettes enduites jusqu'à rendre composition et entretien invisibles ; étiquettes de taille tombées, modifiées ou invalidées par le retrait, alors que le litige de taille est ce que la revente redoute le plus ; et absence d'identité traçable, qui laisse référence, grade et historique d'entretien à un enregistrement manuel s'effondrant avec le volume. La deuxième partie présente dans un tableau les six accessoires à restaurer : étiquette d'entretien indiquant composition et entretien encore valables, étiquette de taille unifiant le filtrage, étiquette pendante et grade portant marque et état, identifiant interne reliant référence et lot, emballage gérant poussière, humidité et ouverture, et éléments de sécurité ou d'authenticité pour les catégories de valeur — avec pour chacun le point clé à la refabrication. La troisième partie soutient un choix de matière fondé sur les cycles de lavage, non sur la norme du neuf : les étiquettes tissées colorent par la fibre et tiennent le plus longtemps, les étiquettes imprimées enduites portent plus d'information mais exigent un vrai essai de vieillissement, robes et costumes de location demandent une résistance au nettoyage à sec et au repassage, un point d'arrêt aux deux extrémités dure plus longtemps que la colle, et une étiquette claire sur tissu foncé impose un contrôle de dégorgement. La quatrième partie trace la frontière entre conformité et règles de plateforme : les articles d'occasion bénéficient rarement d'une exemption générale, l'authenticité prime, la remise en état doit être déclarée, le passeport numérique européen pointe vers des données consultables, et les règles de plateforme sur le vocabulaire des grades, la saisie des tailles et la visibilité des anciennes étiquettes sont souvent plus fines que la loi. Le guide se clôt sur un flux de remise en état et de grading en six étapes.",
        sum_es="En la segunda mano y la reventa de prendas, la primera barrera no es el abastecimiento: es el etiquetado. El artículo abre con tres puntos que bloquean con más frecuencia: lavados y limpiezas en seco repetidos que borran la impresión de las etiquetas recubiertas hasta dejar invisible la composición y el cuidado; etiquetas de talla caídas, alteradas o invalidadas por el encogimiento, cuando la disputa de talla es lo que la reventa más teme; y ausencia de identidad trazable, que deja referencia, grado e historial de cuidado al registro manual, que se rompe al escalar. La segunda parte presenta en una tabla los seis accesorios a reponer: etiqueta de cuidado que declara composición y cuidado aún válidos, etiqueta de talla que unifica el filtrado, colgante y etiqueta de grado con marca y estado, identificación interna que une referencia y lote, embalaje que atiende polvo, humedad y apertura, y elementos de seguridad o autenticidad para categorías de valor, cada uno con su clave al rehacerse. La tercera parte defiende elegir material por ciclos de lavado, no por norma de prenda nueva: las etiquetas tejidas se colorean por la fibra y duran más, las impresas recubiertas llevan más información pero exigen un ensayo real de envejecimiento, los vestidos y trajes de alquiler requieren resistencia a limpieza en seco y planchado, rematar ambos extremos dura más que el pegamento, y una etiqueta clara sobre tejido oscuro obliga a comprobar sangrado. La cuarta parte traza la frontera entre conformidad y reglas de plataforma: los artículos usados rara vez gozan de exención general, la autenticidad manda, el reacondicionamiento debe declararse, el pasaporte digital europeo apunta a datos consultables y las reglas de plataforma sobre grados, tallas y etiquetas antiguas visibles suelen ser más finas que la ley. Cierra con un flujo de reacondicionamiento y grados en seis pasos.",
    ),
]
