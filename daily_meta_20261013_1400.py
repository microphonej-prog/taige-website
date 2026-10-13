#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-13 下午批次（14:00）每日更新：2 篇新文章元数据（六语：zh-Hant 根 / en / ja / ko / fr / es）

选题说明（主题池 30 项连同既有扩展均已上线，本次沿两条尚未独立成文的线索扩展，
已核对 blog/、en|ja|ko|fr|es/blog/ 与 sitemap.xml 无重复 slug，并做全站关键词扫描确认空白）：

- garment-embroidery-decoration-guide.html：服装绣花（刺绣）装饰与绣花标。
  全站扫描：「毛巾绣」0 处、「立体绣」0 处、「绣花章」0 处、「绣花」仅 8 处（散见于
  _body_lace 讲水溶蕾丝/刺绣花边、_body_thread 讲绣花线、_body_dress 顺带举例）、
  「贴布绣」10 处（集中在 felt 贴布标一篇），没有把「绣花」作为一种服装装饰工艺单独成文。
  既有相关文章分工：woven-label-embroidery-comparison 只对比「织唛 vs 刺绣标」两种标签；
  lace-trimming-guide 讲蕾丝本体；heat-transfer-labels 讲热转印标。
  本文落点是「绣花与织唛、印花的边界 → 五种绣花工艺（平绣/毛巾绣/立体绣/贴布绣/亮片绳绣）
  → 绣花线、衬料、底线三样看不见的辅料 → 与洗水标、吊牌、包装的配合 → 打样验收六项」，
  与上述文章互补而非重叠，且不涉及成衣印花设备与产线，仅作工艺对比。
  全文为工艺与验收内容，未出现具体价格数字。

- animal-derived-material-certification-guide.html：辅料中的动物源材料与认证追溯。
  全站扫描：「RDS」0 处、「RWS」0 处、「LWG」0 处、「动物福利」0 处、「善待动物」0 处、
  「GOTS」0 处；仅「皮革」42 处、「皮标」14 处（均为产品选型与工艺内容）。
  既有相关文章分工：garment-trims-certifications 讲 OEKO-TEX / GRS / FSC（不含动物源）；
  leather-patch-labels 讲皮牌本体材质与工艺；leather-garment-trims-guide 讲皮革服装的辅料配置；
  certification-claims-label-guide 讲宣称用词；trim-supplier-social-compliance-audit 讲社会责任审核。
  本文落点是「哪些辅料涉及动物源材料（皮革/角质贝壳/动物纤维/羽绒毛饰）→ LWG、RWS、RDS、GRS
  各自覆盖什么、买家常查什么 → 素皮与再生替代的代价 → 标签与吊牌宣称怎么写才不出事 →
  向供应商索取的分子/P 以及动物福利政策的书面确认」，与上述文章互补。
  认证描述只写证书性质与核查要点，不引用具体法规编号、不编造限值与比例，价格一律不出现。
"""

ARTICLES = [
    dict(
        slug="garment-embroidery-decoration-guide.html",
        body="blog/_body_embroidery.html",
        title_zh="服装绣花（刺绣）辅料指南：平绣、毛巾绣、立体绣怎么选 | TAGE",
        title_en="Garment Embroidery Guide: Flat, Chenille, 3D Puff and Appliqué | TAGE",
        title_ja="衣料刺繍の副資材ガイド：平刺繍・パイル・立体刺繍の選び方 | TAGE",
        title_ko="의류 자수 부자재 가이드: 평수, 파일, 입체 자수 선택법 | TAGE",
        title_fr="Guide de la broderie : plate, chenille, 3D et appliquée | TAGE",
        title_es="Guía del bordado: plano, chenille, 3D y aplicado | TAGE",
        desc_zh="服装绣花辅料指南：平绣、毛巾绣、立体绣、贴布绣与亮片绣五种工艺怎么选，绣花线、衬料与底线这三样看不见的辅料怎么配，绣花与洗水标、吊牌、包装的配合要点，附打样验收六项清单。来自东莞泰阁包装。",
        desc_en="Garment embroidery guide: flat, chenille, 3D puff, appliqué and sequin embroidery compared, plus thread, backing, care labels, packing and six sample checks.",
        desc_ja="衣料刺繍の副資材ガイド。平刺繍・パイル・立体刺繍・アップリケ・スパンコールの5技法の比較、刺繍糸・芯・下糸の選び方、洗濯表示ラベル・タグ・包装との組み合わせ、6項目のサンプル検収までを解説します。東莞泰閣包装。",
        desc_ko="의류 자수 부자재 가이드. 평수, 파일, 입체, 아플리케, 스팽글 다섯 기법 비교와 자수사·심지·밑실 선택, 세탁 라벨·행택·포장 조합, 6단계 샘플 검수를 정리했습니다. 둥관 TAGE 패키징.",
        desc_fr="Guide de la broderie : plate, chenille, 3D, appliquée et sequins comparées, fil, renfort et canette, articulation avec l'étiquette d'entretien et six contrôles.",
        desc_es="Guía del bordado: plano, chenille, 3D, aplicado y lentejuelas comparados, hilo, refuerzo y canilla, etiquetas de cuidado y seis comprobaciones.",
        crumb_zh="绣花与刺绣辅料",
        crumb_en="Embroidery Trims",
        crumb_ja="刺繍の副資材",
        crumb_ko="자수 부자재",
        crumb_fr="Accessoires de broderie",
        crumb_es="Accesorios de bordado",
        h1_zh="服装绣花（刺绣）辅料指南：平绣、毛巾绣、立体绣怎么选",
        h1_en="Garment Embroidery Guide: Flat, Chenille, 3D Puff and Appliqué",
        h1_ja="衣料刺繍の副資材ガイド：平刺繍・パイル・立体刺繍の選び方",
        h1_ko="의류 자수 부자재 가이드: 평수, 파일, 입체 자수 선택법",
        h1_fr="Guide de la broderie : plate, chenille, 3D et appliquée",
        h1_es="Guía del bordado: plano, chenille, 3D y aplicado",
        tag_zh="技术指南",
        tag_en="Technical Guide",
        tag_ja="技術ガイド",
        tag_ko="기술 가이드",
        tag_fr="Guide technique",
        tag_es="Guía técnica",
        sum_zh="绣花和织唛、印花常被当成同一件事，其实计价口径、视觉风格与耐久性是三条完全不同的路线。文章先用一张对照表把三者分开：织唛按千枚加宽度计价、颜色数有限；印花按面积加色数、洗后易裂；绣花按千针数加色数、立体耐洗但细节受限。第二部分对比五种主流工艺——平绣能表现小字与细线，毛巾绣手感最好但厚度大，立体绣靠发泡衬做出 3D 冲击力，贴布绣用色块换效率，亮片与绳绣装饰性最强但必须做洗后测试。第三部分讲绣花线、衬料与底线这三样看不见的辅料：人造丝光泽好但湿强低、薄面料必须加衬否则针孔扎破、底线颜色与正面要接近、贴身部位要加软贴衬封住线头。第四部分讲绣花与洗水标、吊牌、包装的配合：熨烫温度要按绣花线与衬料下调、缩率要按预缩后状态确认位置、绣花区与尺码标留 5–8mm 间距、包装防压防钩。最后是打样验收六项：针数与颜色数、位置公差、线色对色、洗后与摩擦、背面手感、小件拉力。",
        sum_en="Embroidery, woven labels and print are often treated as the same thing, yet their pricing logic, visual character and durability are three different routes. The article separates them in a comparison table: woven is quoted per thousand pieces plus width with a limited colour count; print is quoted by area plus colours and cracks after washing; embroidery is quoted by thousand stitches plus colours, builds relief and survives washing but limits fine detail. Part two compares five mainstream techniques — flat renders small lettering and fine lines, chenille gives the best hand feel at greater thickness, 3D puff uses a foam layer for impact, appliqué trades colour blocks for efficiency, and sequin or cord embroidery decorates hardest but always needs a wash test. Part three covers the three invisible trims: rayon has lustre but low wet strength, thin fabric must be backed or needle holes perforate it, bobbin colour should sit close to the face, and skin-contact areas need a soft cover backing over the thread ends. Part four lines embroidery up with care labels, hang tags and packing: lower the pressing temperature to what thread and backing tolerate, confirm motif placement in the pre-shrunk state, leave 5–8 mm between embroidery and size label, and protect against crush and snag. It closes with six sample checks: stitch and colour count, placement tolerance, thread shade, wash and rub, reverse and hand feel, and small-part tension.",
        sum_ja="刺繍と織りネームとプリントは同じものとして扱われがちですが、見積り基準・見た目・耐久性はまったく別の道筋です。まず対照表で3つを分けます。織りネームは千枚＋幅で色数に制限、プリントは面積＋色数で洗濯後にひび割れ、刺繍は千針＋色数で立体感と耐洗濯に優れるが細部は苦手。第2部では5つの主要技法を比較します。平刺繍は小さな文字と細線、パイルは風合いが最良だが厚みが出る、立体刺繍は発泡芯でインパクト、アップリケは色塊で効率を稼ぎ、スパンコールとコード刺繍は装飾性が最も高いが洗濯試験が必須です。第3部は見えない3つの副資材。レーヨンは光沢があるが湿潤強度が低く、薄地は芯を入れないと針穴で破れ、下糸は表側に近い色を選び、肌に当たる部分は柔らかな裏当てで糸端を覆います。第4部は洗濯表示ラベル・タグ・包装との組み合わせ。プレス温度は糸と芯の耐熱に合わせて下げ、収縮後の状態で図案位置を確認し、刺繍範囲とサイズ表示の間に5〜8mmの余白を取り、圧縮と引っかけを防ぎます。最後に針数と色数、位置公差、糸色、洗濯と摩擦、裏面の風合い、小部品の引張の6項目を示します。",
        sum_ko="자수와 직조 라벨, 프린트는 같은 것으로 취급되곤 하지만 견적 기준과 시각적 성격, 내구성은 전혀 다른 길입니다. 먼저 대조표로 세 가지를 구분합니다. 직조 라벨은 천 장과 폭 기준에 색상 수 제한, 프린트는 면적과 색수 기준에 세탁 후 갈라짐, 자수는 천 바늘과 색수 기준으로 입체감과 세탁 내구성이 좋지만 세밀한 표현은 어렵습니다. 두 번째 부분은 다섯 기법 비교입니다. 평수는 작은 글자와 가는 선, 파일은 촉감이 가장 좋지만 두껍고, 입체 자수는 발포 심지로 임팩트를 내며, 아플리케는 색면으로 효율을 얻고, 스팽글과 코드 자수는 장식성이 가장 높지만 세탁 시험이 필수입니다. 세 번째는 보이지 않는 세 가지 부자재입니다. 레이온은 광택이 좋지만 습윤 강도가 낮고, 얇은 원단은 심지가 없으면 바늘 구멍으로 찢어지며, 밑실은 앞면과 비슷한 색을 고르고 피부 접촉 부위는 부드러운 덧댐으로 실 끝을 덮습니다. 네 번째는 세탁 라벨, 행택, 포장과의 조합입니다. 다림질 온도는 실과 심지가 견디는 범위로 낮추고, 수축 후 상태로 도안 위치를 확인하며, 자수 영역과 사이즈 라벨 사이에 5~8mm 여백을 두고 압박과 걸림을 막습니다. 마지막으로 바늘 수와 색수, 위치 공차, 실 색상, 세탁과 마찰, 뒷면 촉감, 소형 부품 인장의 6가지를 제시합니다.",
        sum_fr="Broderie, label tissé et impression passent souvent pour la même chose, alors que leur logique de prix, leur rendu et leur durabilité suivent trois voies distinctes. L'article les sépare dans un tableau : le tissé se chiffre au millier plus la largeur avec peu de couleurs ; l'impression à la surface plus les couleurs et craquelle au lavage ; la broderie au millier de points plus les couleurs, gagne en relief et au lavage mais limite le détail fin. La deuxième partie compare cinq techniques : la plate rend les petits textes, la chenille offre le meilleur toucher au prix de l'épaisseur, la 3D puff utilise une mousse pour l'impact, l'appliquée gagne en efficacité par aplats, et sequins ou cordon décorent le plus mais exigent un essai de lavage. La troisième traite les trois accessoires invisibles : la viscose brille mais résiste peu mouillée, un tissu fin doit être renforcé sinon les points le percent, le fil de canette doit rester proche du dessus et les zones en contact avec la peau exigent un support doux couvrant les fils. La quatrième articule broderie, étiquette d'entretien, étiquette pendante et emballage : abaisser la température de repassage, valider la position à l'état pré-rétréci, laisser 5 à 8 mm entre broderie et étiquette de taille, protéger du tassement et de l'accroche. Six contrôles closent le guide : points et couleurs, tolérance de position, teinte de fil, lavage et frottement, envers et toucher, traction des petites pièces.",
        sum_es="Bordado, etiqueta tejida y estampado se tratan como lo mismo, aunque su lógica de precio, su carácter visual y su durabilidad son tres caminos distintos. El artículo los separa en una tabla: la tejida se presupuesta por millar más anchura con pocos colores; el estampado por superficie más colores y se agrieta al lavar; el bordado por millar de puntadas más colores, gana en relieve y lavado pero limita el detalle fino. La segunda parte compara cinco técnicas: el plano rinde textos pequeños y líneas finas, el chenille da el mejor tacto a cambio de grosor, el 3D puff usa espuma para el impacto, el aplicado gana eficiencia con manchas de color y lentejuelas o cordón decoran más pero exigen ensayo de lavado. La tercera trata los tres accesorios invisibles: la viscosa brilla pero resiste poco en húmedo, un tejido fino debe reforzarse o las puntadas lo perforan, el hilo de canilla debe acercarse a la cara y las zonas de contacto con la piel necesitan soporte suave sobre los hilos. La cuarta combina bordado, etiqueta de cuidado, colgante y empaque: bajar la temperatura de planchado, validar la posición en estado preencogido, dejar 5–8 mm entre bordado y etiqueta de talla y proteger de presión y enganches. Cierra con seis controles: puntadas y colores, tolerancia de posición, tono del hilo, lavado y frote, revés y tacto, y tracción de piezas pequeñas.",
    ),
    dict(
        slug="animal-derived-material-certification-guide.html",
        body="blog/_body_animalcert.html",
        title_zh="服装辅料动物源材料认证指南：皮革、羊毛、羽绒怎么追溯 | TAGE",
        title_en="Animal-Derived Trims Certification: Leather, Wool, Down, Shell | TAGE",
        title_ja="動物由来副資材の認証ガイド：レザー・ウール・ダウンの追跡 | TAGE",
        title_ko="동물 유래 부자재 인증 가이드: 가죽, 울, 다운 추적 | TAGE",
        title_fr="Accessoires d'origine animale : cuir, laine, duvet et nacre | TAGE",
        title_es="Accesorios de origen animal: cuero, lana, plumón y nácar | TAGE",
        desc_zh="服装辅料动物源材料认证指南：皮牌、牛角扣、贝母扣、真丝缎带、羊毛织带与羽绒分别对应哪些认证，LWG、RWS、RDS、GRS 各自覆盖什么，素皮替代的代价，以及标签与吊牌宣称怎么写才不出事，附供应商凭证清单。来自东莞泰阁包装。",
        desc_en="Animal-derived trims guide: leather, horn, shell, silk, wool and down, what LWG, RWS, RDS and GRS actually cover, vegan substitutes and safe label claims.",
        desc_ja="動物由来副資材の認証ガイド。レザーパッチ・角ボタン・貝ボタン・シルク・ウール・ダウンの対応認証、LWG・RWS・RDS・GRS が何をカバーするか、ヴィーガン代替の限界、ラベル表示の注意点、確認すべき書類を解説します。東莞泰閣包装。",
        desc_ko="동물 유래 부자재 인증 가이드. 가죽 패치, 뿔·조개 단추, 실크, 울, 다운의 해당 인증과 LWG·RWS·RDS·GRS의 보증 범위, 비건 대체의 한계, 라벨 표기 주의점, 요구할 서류를 정리했습니다. 둥관 TAGE 패키징.",
        desc_fr="Guide des accessoires d'origine animale : cuir, corne, nacre, soie, laine et duvet, ce que couvrent LWG, RWS, RDS et GRS, substituts végans et allégations sûres.",
        desc_es="Guía de accesorios de origen animal: cuero, cuerno, nácar, seda, lana y plumón, qué cubren LWG, RWS, RDS y GRS, sustitutos veganos y alegaciones seguras.",
        crumb_zh="动物源辅料与认证",
        crumb_en="Animal-Derived Trims",
        crumb_ja="動物由来の副資材",
        crumb_ko="동물 유래 부자재",
        crumb_fr="Accessoires d'origine animale",
        crumb_es="Accesorios de origen animal",
        h1_zh="服装辅料动物源材料认证指南：皮革、羊毛、羽绒怎么追溯",
        h1_en="Animal-Derived Trims Certification: Leather, Wool, Down and Shell",
        h1_ja="動物由来副資材の認証ガイド：レザー・ウール・ダウンの追跡",
        h1_ko="동물 유래 부자재 인증 가이드: 가죽, 울, 다운 추적",
        h1_fr="Accessoires d'origine animale : cuir, laine, duvet et nacre",
        h1_es="Accesorios de origen animal: cuero, lana, plumón y nácar",
        tag_zh="合规指南",
        tag_en="Compliance Guide",
        tag_ja="コンプライアンスガイド",
        tag_ko="컴플라이언스 가이드",
        tag_fr="Guide conformité",
        tag_es="Guía de cumplimiento",
        sum_zh="辅料里的动物源材料比想象中多：皮牌与皮拉手、牛角扣与贝母扣、真丝缎带与滚边、羊毛织带与毛条、羽绒标签。欧美买家在询价阶段就开始追问来源，问的不是价格而是动物福利与可追溯性，答不上来往往不是被砍价，而是直接被排除在供应商名单之外。文章先列清四类涉及动物源材料的辅料，再用一张表对照主流认证各自覆盖什么：皮革看 LWG 皮革厂审核的等级与批号能否对应订单，羊毛看 RWS 从农场到纺纱的链条文件与交易证书数量、以及割臀状态，羽绒看 RDS 是否禁止活拔与强制喂食、能否按批追溯，再生材料看 GRS 的回收含量与生产环节要求，而真丝、角质与贝壳目前没有像 RDS 那样被广泛采用的国际动物福利认证，只能提供产地与加工说明并遵守客户自有政策。第三部分讲素皮与再生替代的适用边界——素皮外观接近但耐久略低，植物基与菌丝体材料单价高、产能有限，再生织带回弹与保暖不同必须重测洗后表现，换料后吊牌与洗水标文字要同步更新。第四部分讲宣称合规：能证明才写、写清覆盖范围、标志图形需授权、按目标市场最新规则更新。最后是向供应商索取的清单：认证证书与交易证书、材料声明、批号对应表、物理与洗护测试、以及动物福利政策的书面确认。",
        sum_en="Animal-derived material in trims is more common than assumed: leather patches and pullers, horn and shell buttons, silk ribbons and piping, wool tapes and trims, and down labels. Buyers in Europe and North America start asking about origin at quotation stage — testing animal welfare and traceability rather than price, and failing to answer removes you from the vendor list rather than costing you a discount. The article lists four groups of trims that carry animal-derived material, then compares what each certification actually covers: leather rests on the LWG tannery audit rating and whether the batch ties to your order; wool on RWS chain-of-custody documents from farm to spinning, transaction certificate volumes and mulesing status; down on RDS bans of live-plucking and force-feeding plus batch traceability; recycled material on GRS recycled content and production requirements; while silk, horn and shell have no international animal-welfare certification as widely adopted as RDS, so suppliers can only provide origin and processing statements and follow the buyer's own policy. Part three covers the limits of vegan and recycled substitutes — vegan leather looks close but wears faster, plant-based and mycelium materials carry high unit prices and limited capacity, recycled tapes differ in rebound and warmth so wash results must be retested, and label wording has to be updated after any switch. Part four deals with claims: only claim what you can prove, state the scope, get permission for certifier marks and refresh wording to the target market's latest rules. It closes with five documents to request, including certificates with transaction certificates, material declarations, batch mapping, physical and care testing, and written confirmation of the buyer's animal-welfare policy.",
        sum_ja="副資材に含まれる動物由来素材は想像以上に多いものです。レザーパッチとプル、角ボタンと貝ボタン、シルクリボンとパイピング、ウールテープとトリム、ダウン表示など。欧米のバイヤーは見積りの段階から由来を尋ね、問われるのは価格ではなく動物福祉とトレーサビリティです。答えられないと値引きではなく取引先リストから外れます。記事はまず4つの分類を示し、次に対照表で各認証のカバー範囲を整理します。レザーはLWG皮なめし工場監査の等級とロット対応、ウールはRWSの農場から紡績までの管理文書と取引証明書の数量およびミュールジングの有無、ダウンはRDSの生きたままの抜羽と強制給餌の禁止とロット追跡、再生素材はGRSの再生素材比率と生産要件です。シルク・角・貝にはRDSほど広く採用された国際的な動物福祉認証がなく、産地と加工の説明および顧客独自ポリシーの順守で対応します。第3部はヴィーガンレザーと再生素材の限界で、見た目は近いが耐久はやや低く、植物由来・菌糸体は単価が高く生産能力が限られ、再生テープは回復性と保温が異なるため洗濯結果の再試験が必須、切替後はタグと洗濯表示の文言を同時更新します。第4部は表示の書き方で、証明できることだけ記載し、範囲を限定し、ロゴは許諾を取り、対象市場の最新規則に更新します。最後に認証証明書と取引証明書、素材申告書、ロット対応表、物理・手入れ試験、動物福祉ポリシーの書面確認という確認すべき書類を示します。",
        sum_ko="부자재의 동물 유래 소재는 생각보다 많습니다. 가죽 패치와 풀러, 뿔 단추와 조개 단추, 실크 리본과 파이핑, 울 테이프와 트림, 다운 라벨 등입니다. 유럽과 북미 바이어는 견적 단계부터 출처를 묻고, 묻는 것은 가격이 아니라 동물 복지와 추적성입니다. 답하지 못하면 가격 인하가 아니라 공급업체 명단에서 제외됩니다. 글은 먼저 네 가지 분류를 정리하고, 대조표로 각 인증의 보증 범위를 비교합니다. 가죽은 LWG 제혁 공장 심사 등급과 로트 대응, 울은 RWS의 농장에서 방적까지 관리 문서와 거래 인증서 수량 및 뮬싱 여부, 다운은 RDS의 생체 채취와 강제 급식 금지 및 로트 추적, 재생 소재는 GRS의 재생 함량과 생산 요건입니다. 실크·뿔·조개는 RDS처럼 널리 채택된 국제 동물 복지 인증이 없어 원산지와 가공 설명, 고객 자체 정책 준수로 대응합니다. 세 번째 부분은 비건 레더와 재생 소재의 한계로, 외관은 비슷하나 내구성이 다소 낮고 식물 기반·균사체는 단가가 높고 생산 능력이 제한적이며 재생 테이프는 회복성과 보온이 달라 세탁 결과를 재시험해야 하고, 전환 후 행택과 세탁 라벨 문구를 함께 갱신해야 합니다. 네 번째는 표기 방법으로 증명 가능한 것만 쓰고 범위를 한정하며 로고는 승인을 받고 대상 시장 최신 규정에 맞춥니다. 마지막으로 인증 증명서와 거래 인증서, 소재 신고서, 로트 대응표, 물리·관리 시험, 동물 복지 정책 서면 확인을 요구할 서류로 제시합니다.",
        sum_fr="Les matières d'origine animale sont plus fréquentes qu'on ne le croit : patchettes et tirettes en cuir, boutons en corne ou en nacre, rubans et biais de soie, sangles et trims de laine, étiquettes de duvet. En Europe et en Amérique du Nord, l'acheteur interroge l'origine dès le devis : il teste le bien-être animal et la traçabilité, pas le prix, et ne pas répondre vous retire de la liste des fournisseurs au lieu de vous coûter une remise. L'article recense quatre familles d'accessoires concernés, puis compare ce que couvre chaque certification : le cuir repose sur la note d'audit de tannerie LWG et la correspondance du lot avec la commande ; la laine sur les documents de traçabilité RWS de la ferme à la filature, les volumes du certificat de transaction et le statut du mulesing ; le duvet sur les interdictions RDS d'arrachage à vif et de gavage et la traçabilité par lot ; le recyclé sur le contenu GRS et les exigences de production ; la soie, la corne et la nacre n'ayant pas de certification internationale aussi largement adoptée que la RDS, il reste les attestations d'origine et la politique du client. La troisième partie traite les limites des substituts : le cuir végan y ressemble mais s'use plus vite, les matières végétales et mycélium coûtent cher à capacités limitées, les sangles recyclées diffèrent en reprise et en chaleur et exigent de retester le lavage, et tout changement impose de mettre à jour les étiquettes. La quatrième porte sur les allégations : ne claimer que le prouvable, préciser la portée, faire autoriser les logos et actualiser selon les règles du marché visé. Cinq documents à demander closent le guide.",
        sum_es="Los materiales de origen animal son más frecuentes de lo que se supone: parches y tiradores de cuero, botones de cuerno y nácar, cintas y bies de seda, cintas y trims de lana, etiquetas de plumón. En Europa y Norteamérica el comprador pregunta el origen desde el presupuesto: evalúa bienestar animal y trazabilidad, no precio, y no responder te saca de la lista de proveedores en lugar de costarte un descuento. El artículo enumera cuatro familias de accesorios afectados y compara después qué cubre cada certificación: el cuero depende de la nota de auditoría de curtiduría LWG y de que el lote cuadre con el pedido; la lana de los documentos RWS de granja a hilatura, los volúmenes del certificado de transacción y la situación del mulesing; el plumón de las prohibiciones RDS de arranque en vivo y alimentación forzada y de la trazabilidad por lote; el reciclado del contenido GRS y los requisitos de producción; y la seda, el cuerno y el nácar no tienen una certificación internacional tan extendida como la RDS, así que quedan las declaraciones de origen y la política del cliente. La tercera parte trata los límites de los sustitutos: el cuero vegano se parece pero se desgasta antes, los materiales vegetales y de micelio tienen precio alto y capacidad limitada, las cintas recicladas difieren en recuperación y abrigo y obligan a reensayar el lavado, y todo cambio exige actualizar etiquetas. La cuarta aborda las alegaciones: solo lo demostrable, delimitar el alcance, autorizar logotipos y actualizar según el mercado. Cierra con cinco documentos a pedir.",
    ),
]
