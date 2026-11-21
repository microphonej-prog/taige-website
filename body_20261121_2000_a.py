# -*- coding: utf-8 -*-
"""2026-11-21 20:00 第一篇：鉤扣帶（Hook and Eye Tape）（英文主稿，zh/fr/es/ja/ko 從英文翻譯）"""

SLUG = "hook-and-eye-tape-guide.html"
CAT = {"zh": "五金配件", "en": "Hardware", "fr": "Quincaillerie", "es": "Herrajes",
       "ja": "金具", "ko": "금속 부자재"}
TITLE = {
    "zh": "鉤扣帶選型：鉤數、拉力與鎳釋放 | TAGE",
    "en": "Hook and Eye Tape: Types, Strength and Nickel Release | TAGE",
    "fr": "Ruban agrafe-crochet : types, résistance et nickel | TAGE",
    "es": "Cinta de corchetes: tipos, resistencia y níquel | TAGE",
    "ja": "ホックテープの選定：フック数・引張強度・ニッケル溶出 | TAGE",
    "ko": "후크앤아이 테이프: 후크 수·인장 강도·니켈 용출 | TAGE",
}
DESC = {
    "zh": "鉤扣帶是服裝裡最便宜也最受力的零件：內衣後扣、褲腰鉤條、裙門襟小鉤各自承受不同張力。本文講清鉤數與帶寬選法、鍍層與鎳釋放合規線、縫製參數，以及寫進採購單的五個驗收數字。",
    "en": "Hook and eye tape for bras, waistbands and skirts: hook count, tape width, coating, pull strength and the nickel release limits that decide clearance.",
    "fr": "Ruban agrafe-crochet pour dos de soutien-gorge, ceintures de pantalon et pattes de jupe : nombre d'agrafes, largeur, revêtement, résistance et limites de nickel.",
    "es": "Cinta de corchetes para espaldas de sujetador, cinturillas de pantalón y tapetas de falda: número de corchetes, ancho, recubrimiento, resistencia y límites de níquel.",
    "ja": "ブラジャー後ろ、スラックス腰、スカート前立てのホックテープ。フック数、テープ幅、めっき、引張強度、ニッケル溶出の合否線まで。",
    "ko": "브라 후크, 바지 허리, 스커트 앞여밈용 후크앤아이 테이프. 후크 수, 테이프 폭, 도금, 인장 강도, 니켈 용출 기준까지 정리합니다.",
}
H1 = {
    "zh": "鉤扣帶：受力最大的那兩平方公分",
    "en": "Hook and Eye Tape: The Two Square Centimetres That Take the Load",
    "fr": "Ruban agrafe-crochet : les deux centimètres carrés qui portent la charge",
    "es": "Cinta de corchetes: los dos centímetros cuadrados que soportan la carga",
    "ja": "ホックテープ：荷重を受ける 2 平方センチ",
    "ko": "후크앤아이 테이프: 하중을 받는 2제곱센티미터",
}
DATE = {"zh": "泰閣包裝 · 更新於 2026年11月21日",
        "en": "By TAGE Packaging &nbsp;·&nbsp; Updated November 21, 2026",
        "fr": "Par TAGE Packaging &nbsp;·&nbsp; Mis à jour le 21 novembre 2026",
        "es": "Por TAGE Packaging &nbsp;·&nbsp; Actualizado el 21 de noviembre de 2026",
        "ja": "泰閣包装 · 2026年11月21日更新",
        "ko": "TAGE 패키징 · 2026년 11월 21일 업데이트"}

BLOCKS = [
    ("p", {
        "zh": "鉤扣帶是服裝裡單價最低、受力最集中的零件之一。內衣後扣一天開合幾次，連續幾年；褲腰鉤扣每次坐下都承接整條腰頭的張力。帶子是載體，鉤與眼是金屬，縫線是把兩者綁住的環節——三者都要定義、都要驗收。漏掉任何一項，先壞的通常是縫線或鍍層，而不是布料。",
        "en": "Hook and eye tape is one of the cheapest components in a garment and one of the most stressed. A bra back closes and opens several times a day for years. A trouser waistband hook takes the entire tension of the waistband every time the wearer sits down. The tape is the carrier, the hook and eye are the metal, and the stitch is the link that binds them. Define and verify all three, because the part that fails first is almost never the fabric.",
        "fr": "Le ruban agrafe-crochet est l'un des composants les moins chers du vêtement et l'un des plus sollicités. Un dos de soutien-gorge s'ouvre et se ferme plusieurs fois par jour pendant des années. Un crochet de ceinture encaisse toute la tension de la taille à chaque fois que la personne s'assoit. Le ruban porte, l'agrafe et le crochet sont le métal, la couture est le lien : les trois se définissent et se contrôlent. Ce qui lâche en premier n'est presque jamais le tissu.",
        "es": "La cinta de corchetes es uno de los componentes más baratos de la prenda y uno de los más solicitados. La espalda de un sujetador se abre y se cierra varias veces al día durante años. El corchete de una cinturilla recibe toda la tensión de la cintura cada vez que la persona se sienta. La cinta soporta, el corchete es el metal y la costura es el vínculo: los tres se definen y se controlan. Lo que falla primero casi nunca es la tela.",
        "ja": "ホックテープは衣料の中で最も安価な部品のひとつであり、最も荷重を受ける部品でもあります。ブラジャーの後ろは毎日何度も開閉され、それが何年も続きます。スラックスの腰ホックは、座るたびに腰回り全体の張力を一点で受けます。テープは支持体、フックとアイは金属、縫い糸は両者を結ぶ環です。この 3 つすべてを仕様化し、検収しなければ、最初に壊れるのは生地ではなく縫い目かめっきです。",
        "ko": "후크앤아이 테이프는 의류에서 가장 저렴한 부품 중 하나이면서 가장 큰 하중을 받는 부품입니다. 브라 후면은 하루에도 몇 번씩 수년간 여닫히고, 바지 허리 후크는 앉을 때마다 허리 전체의 장력을 한 점에서 받습니다. 테이프는 지지체, 후크와 아이는 금속, 봉제사는 둘을 묶는 고리입니다. 세 가지를 모두 규정하고 검수해야 하며, 가장 먼저 망가지는 것은 원단이 아니라 봉제선이나 도금입니다.",
    }),

    ("h2", {
        "zh": "一、四個位置，四種受力",
        "en": "1. Four Positions, Four Different Loads",
        "fr": "1. Quatre positions, quatre charges",
        "es": "1. Cuatro posiciones, cuatro cargas",
        "ja": "1. 4 つの位置、4 つの荷重",
        "ko": "1. 네 위치, 네 가지 하중",
    }),

    ("p", {
        "zh": "內衣後扣用 2×3 或 3×3 鉤，帶寬 25–38 mm，張力平均分攤在兩到三個鉤上，單鉤靜態受力常見設計值 20–30 N。褲腰鉤扣條寬約 20 mm，只有一個鉤，坐姿時全部張力集中在一處，常見設計值 60–90 N，是四者中最吃力的。裙裝隱形拉鍊門襟的小鉤幾乎不承重，要求的是薄（總厚不超過 1.2 mm）與貼平。可調肩帶的 8 字扣與滑扣反覆摩擦，鍍層耐磨比拉力更關鍵。同一件衣服上四種鉤扣，不能共用一個採購規格。",
        "en": "A bra back uses 2 by 3 or 3 by 3 hooks on a 25 to 38 mm tape, so the load spreads over two or three hooks and a single hook sees a typical design value of 20 to 30 N. A trouser waistband hook and bar is about 20 mm wide with one hook, and it takes the whole waist tension in one place when the wearer sits: 60 to 90 N is the usual design value, the hardest working of the four. A skirt placket hook under an invisible zip carries almost nothing; what matters is thinness, 1.2 mm total or less, and lying flat. Sliders and figure-eight sliders on adjustable straps rub constantly, so coating abrasion matters more than pull strength. Four closures on one garment should not share one purchasing spec.",
        "fr": "Un dos de soutien-gorge utilise des agrafes 2 par 3 ou 3 par 3 sur un ruban de 25 à 38 mm : la charge se répartit sur deux ou trois agrafes et une seule agrafe travaille autour de 20 à 30 N. Un crochet de ceinture mesure environ 20 mm de large avec un seul crochet ; assis, il prend toute la tension en un point, 60 à 90 N en valeur de conception, le plus sollicité des quatre. Un crochet de patte de jupe sous une fermeture invisible ne porte presque rien : ce qui compte est la finesse, 1,2 mm d'épaisseur totale ou moins, et la tenue à plat. Les coulisseaux de bretelles frottent en permanence : l'abrasion du revêtement compte plus que la résistance à la traction. Quatre fermetures sur un vêtement ne doivent pas partager une seule spécification d'achat.",
        "es": "La espalda de un sujetador usa corchetes de 2 por 3 o 3 por 3 sobre una cinta de 25 a 38 mm: la carga se reparte entre dos o tres corchetes y uno solo trabaja en torno a 20 a 30 N. Un corchete de cinturilla mide unos 20 mm con un solo corchete y, sentado, recibe toda la tensión en un punto: 60 a 90 N como valor habitual de diseño, el más exigido de los cuatro. Un corchete de tapeta de falda bajo cremallera invisible casi no carga: importan la delgadez, 1,2 mm de espesor total o menos, y que quede plano. Los pasadores de tirantes rozan sin parar, así que la abrasión del recubrimiento pesa más que la resistencia a la tracción. Cuatro cierres en una prenda no deben compartir una sola especificación de compra.",
        "ja": "ブラジャー後ろは 2×3 または 3×3 のフックを幅 25〜38 mm のテープに載せ、荷重を 2〜3 個に分散します。1 個あたりの静的設計値は 20〜30 N が目安です。スラックスの腰ホックは幅約 20 mm でフックは 1 個、座ったときに腰回りの張力が一点に集中し、設計値 60〜90 N と 4 つの中で最も厳しい条件になります。スカートのコンシールファスナー下の小ホックはほとんど荷重を受けず、総厚 1.2 mm 以下という薄さと平らさが要件です。肩ひものアジャスターは常に擦れるため、引張強度よりもめっきの耐摩耗性が効きます。同じ 1 着の中で 4 種類のホックを 1 つの購買仕様で済ませてはいけません。",
        "ko": "브라 후면은 폭 25~38 mm 테이프에 2×3 또는 3×3 후크를 올려 하중을 2~3개로 나눕니다. 후크 1개당 정적 설계값은 20~30 N이 기준입니다. 바지 허리 후크는 폭 약 20 mm에 후크 1개로, 앉을 때 허리 장력이 한 점에 집중되어 설계값 60~90 N으로 네 가지 중 가장 가혹합니다. 스커트 인비저블 지퍼 아래의 작은 후크는 하중이 거의 없고, 총 두께 1.2 mm 이하의 얇음과 평평함이 요건입니다. 어깨끈 슬라이더는 계속 마찰되므로 인장 강도보다 도금의 내마모성이 중요합니다. 한 벌의 옷에 있는 네 가지 여밈을 하나의 구매 사양으로 묶으면 안 됩니다.",
    }),

    ("h2", {
        "zh": "二、拆開看：鉤、眼、帶、線",
        "en": "2. Take It Apart: Hook, Eye, Tape, Stitch",
        "fr": "2. Démonter : agrafe, crochet, ruban, couture",
        "es": "2. Desmontar: corchete, cinta y costura",
        "ja": "2. 分解して見る：フック、アイ、テープ、縫い糸",
        "ko": "2. 분해해서 보기: 후크, 아이, 테이프, 봉제사",
    }),

    ("p", {
        "zh": "鉤與眼由 0.6–0.8 mm 金屬線成型，線徑偏細在反覆開合後容易開口，偏粗則讓帶子起拱。帶子多為滌綸織帶，橫向要挺、不捲邊，緯向密度不足的帶子在洗水兩三次後就會波浪。縫線用滌綸包芯線 40/2，25 mm 內 8–10 針，兩端起止回針。鍍層有四種：鍍鎳（最便宜、鎳釋放風險最高）、鍍白鎳、無鎳電鍍、尼龍包覆。尼龍包覆最抗汗液腐蝕，代價是總厚增加 0.1–0.2 mm，內衣這種貼身件要事先確認手感。",
        "en": "Hooks and eyes are formed from 0.6 to 0.8 mm wire. Too thin and the hook opens up after repeated cycles; too thick and the tape buckles. The tape is usually a polyester woven tape that has to stay firm across its width and not curl at the edges; under-wefted tape goes wavy after two or three washes. Use a 40/2 polyester core thread, 8 to 10 stitches per 25 mm, with backstitching at both ends. There are four coatings: nickel plated, the cheapest with the highest release risk; white nickel; nickel-free electroplating; and nylon coated. Nylon coating resists perspiration best and adds 0.1 to 0.2 mm of thickness, so for intimate apparel confirm the hand feel before committing.",
        "fr": "Les agrafes et crochets sont formés dans un fil de 0,6 à 0,8 mm. Trop fin, le crochet s'ouvre après des cycles répétés ; trop épais, le ruban gondole. Le ruban est généralement un ruban tissé polyester qui doit rester ferme sur sa largeur et ne pas roulotter : un ruban sous-tissé en trame ondulera après deux ou trois lavages. Utilisez un fil polyester gainé 40/2, 8 à 10 points au 25 mm, avec arrêt sur les deux extrémités. Quatre revêtements existent : nickelé, le moins cher et le plus risqué en migration ; nickel blanc ; électrolyse sans nickel ; et nylon. Le nylon résiste le mieux à la sueur et ajoute 0,1 à 0,2 mm d'épaisseur : sur la lingerie, validez le toucher avant de figer la spécification.",
        "es": "Los corchetes se forman con alambre de 0,6 a 0,8 mm. Si es demasiado fino, el corchete se abre tras ciclos repetidos; si es demasiado grueso, la cinta se comba. La cinta suele ser tejida de poliéster, debe quedar firme en su ancho y no enrollarse en los bordes: una cinta con poca trama se ondula tras dos o tres lavados. Use hilo poliéster con alma 40/2, de 8 a 10 puntadas por 25 mm, con remate en ambos extremos. Hay cuatro recubrimientos: niquelado, el más barato y de mayor riesgo de migración; níquel blanco; galvanizado sin níquel; y recubierto de nailon. El nailon resiste mejor el sudor y suma 0,1 a 0,2 mm de espesor, así que en lencería conviene validar el tacto antes de fijar la especificación.",
        "ja": "フックとアイは 0.6〜0.8 mm の線材で成型します。細すぎると開閉を繰り返すうちに口が開き、太すぎるとテープが波打ちます。テープはポリエステルの織テープが一般的で、横方向に腰があり、端が巻かないことが条件です。緯密度が不足したテープは 2〜3 回の洗濯で波打ちます。縫い糸はポリエステル芯地糸 40/2、25 mm あたり 8〜10 針、両端は返し縫い。めっきは 4 種類で、ニッケルめっき（最も安価で溶出リスクが高い）、ホワイトニッケル、ニッケルフリー電気めっき、ナイロンコーティングです。ナイロンは汗に対する耐食性が最も高く、その代わり総厚が 0.1〜0.2 mm 増えるため、下着では風合いを事前に確認してください。",
        "ko": "후크와 아이는 0.6~0.8 mm 철선으로 성형합니다. 너무 가늘면 반복 개폐 후 벌어지고, 너무 두꺼우면 테이프가 뜹니다. 테이프는 폴리에스터 직조 테이프가 일반적이며 폭 방향으로 뻣뻣하고 끝단이 말리지 않아야 합니다. 위사 밀도가 부족한 테이프는 세탁 2~3회면 물결처럼 뜹니다. 봉제사는 폴리에스터 심사 40/2, 25 mm당 8~10바늘, 양 끝은 되박기하십시오. 도금은 네 가지로 니켈 도금(가장 저렴하고 용출 위험이 가장 큼), 화이트 니켈, 무니켈 전기도금, 나일론 코팅입니다. 나일론 코팅은 땀 부식에 가장 강하지만 총 두께가 0.1~0.2 mm 늘어나므로 속옷은 촉감을 먼저 확인해야 합니다.",
    }),

    ("h2", {
        "zh": "三、鎳釋放才是真正的合規紅線",
        "en": "3. Nickel Release Is the Real Compliance Line",
        "fr": "3. Le nickel est la vraie ligne rouge",
        "es": "3. El níquel es la verdadera línea roja",
        "ja": "3. ニッケル溶出こそが本当の合规ライン",
        "ko": "3. 니켈 용출이 진짜 규제선",
    }),

    ("p", {
        "zh": "歐盟 REACH 法規（EC）1907/2006 附件 XVII 第 27 條規定：與皮膚長時間直接接觸的金屬部件，鎳釋放速率不得超過 0.5 µg/cm²/週。測試走 EN 1811 篩查法；有鍍層的部件要先按 EN 12472 做磨耗與腐蝕模擬再測，所以「鍍了鎳但外面有漆」並不豁免。美國市場另看 CPSIA（兒童產品可觸及基材總鉛 ≤ 100 ppm）與加州 Prop 65；日本沒有法定鎳釋放限值，但日本買家普遍直接引用 EN 1811 作為規格。韓國兒童產品還要走 어린이제품 안전특별법 的安全確認。",
        "en": "REACH (EC) 1907/2006, Annex XVII, entry 27 sets the limit: metal parts in prolonged direct skin contact must not release nickel faster than 0.5 micrograms per square centimetre per week. Screening runs to EN 1811, and coated parts must first be worn and corroded per EN 12472, so a nickel layer under a lacquer is not exempt. For the United States, CPSIA caps total lead in accessible substrate of children s products at 100 ppm, and California adds Prop 65. Japan has no statutory nickel release limit, but Japanese buyers routinely cite EN 1811 in the specification. Korean children s products also go through safety confirmation under the Special Act on Safety of Children s Products.",
        "fr": "Le règlement REACH (CE) 1907/2006, annexe XVII, entrée 27 fixe la limite : les pièces métalliques en contact prolongé avec la peau ne doivent pas libérer plus de 0,5 microgramme par centimètre carré et par semaine. Le dépistage suit EN 1811, et les pièces revêtues doivent d'abord subir l'usure et la corrosion selon EN 12472 : une couche de nickel sous un vernis n'est donc pas exemptée. Aux États-Unis, le CPSIA limite le plomb total à 100 ppm dans les substrats accessibles des produits enfants, et la Californie ajoute la Prop 65. Le Japon n'a pas de limite légale de migration du nickel, mais les acheteurs japonais citent couramment EN 1811 dans leurs cahiers des charges. En Corée, les produits enfants passent par une confirmation de sécurité au titre de la loi spéciale sur la sécurité des produits pour enfants.",
        "es": "El Reglamento REACH (CE) 1907/2006, anexo XVII, entrada 27 fija el límite: las piezas metálicas en contacto prolongado con la piel no deben liberar más de 0,5 microgramos por centímetro cuadrado por semana. El cribado se hace según EN 1811, y las piezas recubiertas deben someterse antes a desgaste y corrosión según EN 12472, de modo que una capa de níquel bajo laca no queda exenta. En Estados Unidos, CPSIA limita el plomo total a 100 ppm en sustratos accesibles de productos infantiles, y California suma la Prop 65. Japón no tiene límite legal de migración de níquel, pero los compradores japoneses citan habitualmente EN 1811 en sus especificaciones. En Corea, los productos infantiles pasan por una confirmación de seguridad bajo la ley especial de seguridad de productos infantiles.",
        "ja": "EU の REACH 規則 (EC) 1907/2006 附属書 XVII 第 27 項は、皮膚に長時間直接接触する金属部品からのニッケル溶出を 0.5 µg/cm²/週 以下と定めています。スクリーニングは EN 1811 で行い、めっき部品は EN 12472 で摩耗・腐食を模擬した後に測定します。したがってニッケル層の上に塗装があっても免除されません。米国は CPSIA（子ども用品の触知可能な基材の総鉛 100 ppm 以下）とカリフォルニア州 Prop 65 も見ます。日本にはニッケル溶出の法定限度はありませんが、日本のバイヤーは EN 1811 を仕様に引用するのが一般的です。完成した衣料品は家庭用品品質表示法により組成（混用率）と洗濯表示が義務づけられるため、ホックの耐洗性は表示された洗濯方法で検証してください。韓国の子ども用品は「子ども用品の安全性に関する特別法」による安全確認も必要です。",
        "ko": "EU REACH 규정 (EC) 1907/2006 부속서 XVII 제27항은 피부에 장시간 직접 접촉하는 금속 부품의 니켈 용출을 주당 0.5 µg/cm² 이하로 규정합니다. 스크리닝은 EN 1811로 하며, 도금 부품은 EN 12472로 마모·부식을 모사한 뒤 측정합니다. 따라서 니켈 층 위에 도료가 있어도 면제되지 않습니다. 미국은 CPSIA(어린이제품 접촉 가능 기재의 총 납 100 ppm 이하)와 캘리포니아 Prop 65를 함께 봅니다. 일본에는 니켈 용출 법정 한도가 없지만 일본 바이어는 EN 1811을 사양서에 인용하는 것이 일반적입니다. 한국에서는 완성된 의류에 품질경영 및 공산품 안전관리법에 따른 혼용률·취급 표시 등 품질 표시가 필요하고, 어린이제품은 KC 인증(안전 확인) 대상입니다.",
    }),

    ("h2", {
        "zh": "四、縫製參數決定它會不會掉",
        "en": "4. The Sewing Parameters That Decide Whether It Holds",
        "fr": "4. Les réglages de couture qui décident de la tenue",
        "es": "4. Los parámetros de costura que deciden si aguanta",
        "ja": "4. 外れるかどうかを決める縫製パラメータ",
        "ko": "4. 떨어질지를 결정하는 봉제 파라미터",
    }),

    ("p", {
        "zh": "機針 80/12 到 90/14，針距 3.0–3.5 mm，眼帶兩端各回針 12–15 mm 並在帶頭打一道橫向固定；鉤條用 box-X 縫法，四角各回針一次。驗收用三組數字：扣合拉力（鉤眼互相扣住後拉開所需的力）內衣件常見要求 ≥ 60 N，褲腰鉤條縫合強力 ≥ 90 N；開合疲勞 3,000–5,000 次後仍能扣合且無永久變形；洗水 5 次後鉤口不張開、帶子不捲邊。這三組數字寫進規格，掉扣就不再是運氣問題。",
        "en": "Use an 80/12 to 90/14 needle, 3.0 to 3.5 mm stitch length, backstitch 12 to 15 mm at both ends of the eye tape and a crosswise bar at the tape head. Sew the hook bar with a box-X and backstitch each corner. Three numbers do the acceptance work: closure pull, the force needed to open a mated hook and eye, commonly specified at 60 N or more for intimate apparel; seam strength on a waistband hook bar at 90 N or more; and cycle fatigue, where the closure must still mate after 3,000 to 5,000 openings with no permanent deformation. Add five washes with no hook opening or tape curl. Put those numbers in the spec and a lost hook stops being a matter of luck.",
        "fr": "Aiguille 80/12 à 90/14, longueur de point 3,0 à 3,5 mm, arrêt de 12 à 15 mm aux deux extrémités du ruban d'agrafes et une barre transversale en tête de ruban. Cousez le crochet en box-X avec un arrêt à chaque angle. Trois chiffres font le contrôle : la force d'ouverture d'une agrafe fermée, souvent spécifiée à 60 N ou plus en lingerie ; la résistance de couture du crochet de ceinture, 90 N ou plus ; et la fatigue, l'agrafe devant encore fermer après 3 000 à 5 000 cycles sans déformation permanente. Ajoutez cinq lavages sans ouverture ni roulottage. Mettez ces chiffres au cahier des charges et un crochet perdu cesse d'être une question de chance.",
        "es": "Aguja 80/12 a 90/14, longitud de puntada 3,0 a 3,5 mm, remate de 12 a 15 mm en ambos extremos de la cinta de corchetes y una barra transversal en la cabecera. Cosa el corchete en box-X con remate en cada esquina. Tres cifras hacen la aceptación: la fuerza de apertura de un corchete cerrado, a menudo especificada en 60 N o más para lencería; la resistencia de costura del corchete de cinturilla, 90 N o más; y la fatiga, donde el cierre debe seguir abrochando tras 3.000 a 5.000 ciclos sin deformación permanente. Sume cinco lavados sin que el corchete se abra ni la cinta se enrolle. Ponga esas cifras en la especificación y un corchete perdido deja de ser cuestión de suerte.",
        "ja": "針は 80/12〜90/14、針目は 3.0〜3.5 mm、アイテープの両端は 12〜15 mm の返し縫いとテープ頭の横止め、フックバーは box-X で四隅を返し縫いします。検収は 3 つの数値で行います。係合したホックを引き離す力は下着で 60 N 以上が一般的、腰ホックの縫合強度は 90 N 以上、開閉疲労は 3,000〜5,000 回後も係合し永久変形がないこと。さらに 5 回の洗濯後もフックが開かず、テープが巻かないことを確認します。この数値を仕様に入れれば、ホック外れは偶然ではなく管理対象になります。",
        "ko": "바늘은 80/12~90/14, 바늘땀은 3.0~3.5 mm, 아이 테이프 양 끝은 12~15 mm 되박기와 테이프 머리 부분 가로 고정, 후크 바는 box-X로 네 모서리를 되박기합니다. 검수는 세 수치로 합니다. 결합된 후크를 떼는 힘은 속옷 기준 60 N 이상이 일반적이고, 허리 후크 봉제 강도는 90 N 이상, 개폐 피로는 3,000~5,000회 후에도 결합되고 영구 변형이 없어야 합니다. 여기에 세탁 5회 후 후크가 벌어지지 않고 테이프가 말리지 않는 항목을 더합니다. 이 수치를 사양서에 넣으면 후크 탈락은 운의 문제가 아니게 됩니다.",
    }),

    ("h2", {
        "zh": "五、採購單上要寫的五項",
        "en": "5. Five Lines for the Purchase Order",
        "fr": "5. Cinq lignes pour le bon de commande",
        "es": "5. Cinco líneas para el pedido",
        "ja": "5. 発注書に書く 5 項目",
        "ko": "5. 발주서에 넣을 다섯 항목",
    }),

    ("table", {
        "head": [
            {"zh": "項目", "en": "Item", "fr": "Élément", "es": "Elemento", "ja": "項目", "ko": "항목"},
            {"zh": "規格寫法", "en": "How to write it", "fr": "Formulation", "es": "Cómo redactarlo", "ja": "仕様の書き方", "ko": "사양 표기"},
            {"zh": "驗收方法", "en": "How to verify", "fr": "Contrôle", "es": "Verificación", "ja": "検収方法", "ko": "검수 방법"},
        ],
        "rows": [
            [
                {"zh": "鉤數與帶寬", "en": "Hook count and tape width", "fr": "Nombre d'agrafes et largeur", "es": "Número de corchetes y ancho", "ja": "フック数とテープ幅", "ko": "후크 수와 테이프 폭"},
                {"zh": "3×3 鉤，帶寬 30 mm ±0.5 mm", "en": "3 by 3 hooks, tape 30 mm plus or minus 0.5 mm", "fr": "3 par 3 agrafes, ruban 30 mm plus ou moins 0,5 mm", "es": "3 por 3 corchetes, cinta de 30 mm más o menos 0,5 mm", "ja": "3×3 フック、テープ幅 30 mm ±0.5 mm", "ko": "3×3 후크, 테이프 폭 30 mm ±0.5 mm"},
                {"zh": "每批抽 10 件量鉤距，公差 ±1 mm", "en": "Ten pieces per lot, hook spacing within 1 mm", "fr": "Dix pièces par lot, écart entre agrafes à 1 mm", "es": "Diez piezas por lote, separación entre corchetes en 1 mm", "ja": "ロットごと 10 枚でフック間隔 ±1 mm", "ko": "로트당 10개, 후크 간격 ±1 mm"},
            ],
            [
                {"zh": "鍍層", "en": "Coating", "fr": "Revêtement", "es": "Recubrimiento", "ja": "めっき", "ko": "도금"},
                {"zh": "無鎳電鍍或尼龍包覆，附測試報告", "en": "Nickel-free plating or nylon coated, with test report", "fr": "Électrolyse sans nickel ou nylon, avec rapport", "es": "Galvanizado sin níquel o nailon, con informe", "ja": "ニッケルフリーめっきまたはナイロン、試験報告書付き", "ko": "무니켈 도금 또는 나일론 코팅, 시험 성적서 첨부"},
                {"zh": "EN 1811 鎳釋放 ≤ 0.5 µg/cm²/週（有鍍層先做 EN 12472）", "en": "EN 1811 nickel release at or below 0.5 micrograms per square centimetre per week, after EN 12472 if coated", "fr": "EN 1811 : migration du nickel à 0,5 microgramme par centimètre carré par semaine, après EN 12472 si revêtu", "es": "EN 1811: migración de níquel a 0,5 microgramos por centímetro cuadrado por semana, tras EN 12472 si hay recubrimiento", "ja": "EN 1811 で 0.5 µg/cm²/週 以下（めっき品は EN 12472 後）", "ko": "EN 1811 니켈 용출 0.5 µg/cm²/주 이하(도금품은 EN 12472 후)"},
            ],
            [
                {"zh": "拉力", "en": "Pull strength", "fr": "Résistance à la traction", "es": "Resistencia a la tracción", "ja": "引張強度", "ko": "인장 강도"},
                {"zh": "扣合拉力 ≥ 60 N，鉤條縫合 ≥ 90 N", "en": "Closure pull 60 N or more, hook bar seam 90 N or more", "fr": "Ouverture 60 N ou plus, couture du crochet 90 N ou plus", "es": "Apertura 60 N o más, costura del corchete 90 N o más", "ja": "係合力 60 N 以上、腰ホック縫合 90 N 以上", "ko": "결합 인장 60 N 이상, 허리 후크 봉제 90 N 이상"},
                {"zh": "拉力機每批抽 5 件，記錄峰值", "en": "Five pieces per lot on a tensile tester, record the peak", "fr": "Cinq pièces par lot au dynamomètre, relevé du pic", "es": "Cinco piezas por lote en dinamómetro, registrar el pico", "ja": "引張試験機でロットごと 5 枚、最大値を記録", "ko": "인장 시험기로 로트당 5개, 최대값 기록"},
            ],
            [
                {"zh": "疲勞", "en": "Fatigue", "fr": "Fatigue", "es": "Fatiga", "ja": "疲労", "ko": "피로"},
                {"zh": "3,000 次開合仍可扣合、無永久變形", "en": "3,000 cycles, still mates with no permanent set", "fr": "3 000 cycles, fermeture encore fonctionnelle, sans déformation", "es": "3.000 ciclos, sigue abrochando sin deformación permanente", "ja": "3,000 回開閉後も係合し、永久変形なし", "ko": "3,000회 개폐 후에도 결합되고 영구 변형 없음"},
                {"zh": "開合試驗機，附前後尺寸量測", "en": "Cycle tester with before and after measurement", "fr": "Banc de cycles avec mesure avant et après", "es": "Banco de ciclos con medición antes y después", "ja": "開閉試験機、試験前後の寸法測定付き", "ko": "개폐 시험기, 시험 전후 치수 측정 포함"},
            ],
            [
                {"zh": "包裝", "en": "Packing", "fr": "Conditionnement", "es": "Embalaje", "ja": "包装", "ko": "포장"},
                {"zh": "每卷 25 m，卷標印批號與色號", "en": "25 m per roll, label printed with lot and colour", "fr": "25 m par rouleau, étiquette avec lot et coloris", "es": "25 m por rollo, etiqueta con lote y color", "ja": "1 巻 25 m、巻ラベルにロットと色番", "ko": "롤당 25 m, 롤 라벨에 로트·색상 번호"},
                {"zh": "卷標與實物一致，抽 3 卷核對", "en": "Label matches contents, check three rolls", "fr": "Étiquette conforme au contenu, trois rouleaux vérifiés", "es": "Etiqueta conforme al contenido, revisar tres rollos", "ja": "巻ラベルと中身の一致を 3 巻で確認", "ko": "롤 라벨과 내용물 일치 여부 3롤 확인"},
            ],
        ],
    }),

    ("callout", {
        "zh": "寫進規格書的五個數字：鉤距 ±1 mm、帶寬 ±0.5 mm、針距 3.0–3.5 mm、鎳釋放 0.5 µg/cm²/週、開合 3,000 次。",
        "en": "Five numbers for the specification: hook spacing within 1 mm, tape width within 0.5 mm, stitch length 3.0 to 3.5 mm, nickel release 0.5 micrograms per square centimetre per week, and 3,000 opening cycles.",
        "fr": "Cinq chiffres à inscrire : écart entre agrafes à 1 mm, largeur de ruban à 0,5 mm, point de 3,0 à 3,5 mm, nickel à 0,5 microgramme par centimètre carré par semaine, 3 000 cycles.",
        "es": "Cinco cifras para la especificación: separación entre corchetes en 1 mm, ancho de cinta en 0,5 mm, puntada de 3,0 a 3,5 mm, níquel a 0,5 microgramos por centímetro cuadrado por semana, 3.000 ciclos.",
        "ja": "仕様書に入れる 5 つの数値：フック間隔 ±1 mm、テープ幅 ±0.5 mm、針目 3.0〜3.5 mm、ニッケル溶出 0.5 µg/cm²/週、開閉 3,000 回。",
        "ko": "사양서에 넣을 다섯 수치: 후크 간격 ±1 mm, 테이프 폭 ±0.5 mm, 바늘땀 3.0~3.5 mm, 니켈 용출 0.5 µg/cm²/주, 개폐 3,000회.",
    }),

    ("p", {
        "zh": "鉤扣帶的單價通常不到吊牌的三分之一，但它決定的問題性質完全不同：掉扣是功能性缺陷，要召回或補償；掉色是外觀爭議，溝通即可。兩者的處理成本差一個數量級。把上面五個數字寫進採購單，這片金屬就從「配件」變成可控的零件；採購、QC 與供應商三方對同一組數字負責，索賠時也才有依據。",
        "en": "A hook and eye costs less than a third of what a hang tag does, yet it decides a completely different class of problem. A closure that fails is a functional defect, and functional defects mean recalls or credits. A colour shift is an appearance dispute you can talk through. The difference in cost of handling is an order of magnitude. Put those five numbers in the purchase order and the metal stops being an accessory and becomes a controlled part, with purchasing, QC and the supplier all answerable to the same figures.",
        "fr": "Un ruban agrafe-crochet coûte moins du tiers d'un pendant, mais il décide d'une toute autre catégorie de problème. Une fermeture qui lâche est un défaut fonctionnel : rappel ou avoir. Un décalage de teinte est un litige d'aspect qui se règle par la discussion. Le coût de traitement diffère d'un ordre de grandeur. Inscrivez ces cinq chiffres au bon de commande : le métal cesse d'être un accessoire pour devenir une pièce maîtrisée, avec achats, contrôle qualité et fournisseur responsables des mêmes valeurs.",
        "es": "Una cinta de corchetes cuesta menos de un tercio de lo que cuesta una etiqueta colgante, pero decide una clase de problema completamente distinta. Un cierre que falla es un defecto funcional: retirada o abono. Un desvío de color es una discrepancia de aspecto que se resuelve hablando. El coste de gestión difiere en un orden de magnitud. Incluya esas cinco cifras en el pedido y el metal deja de ser un accesorio para convertirse en una pieza controlada, con compras, calidad y proveedor respondiendo a los mismos valores.",
        "ja": "ホックテープの単価は下げ札の 3 分の 1 以下ですが、引き起こす問題の性質はまったく違います。外れたホックは機能不良で、回収や補償につながります。色ずれは外観上の協議で済みます。処理コストは桁が 1 つ違います。この 5 つの数値を発注書に入れれば、金属は「付属品」ではなく管理された部品になり、購買・QC・サプライヤーが同じ数値に責任を持てます。",
        "ko": "후크앤아이 테이프의 단가는 행택의 3분의 1도 되지 않지만, 야기하는 문제의 성격은 전혀 다릅니다. 후크 탈락은 기능 불량으로 회수나 보상으로 이어지고, 색차는 외관 협의로 끝납니다. 처리 비용은 자릿수가 다릅니다. 이 다섯 수치를 발주서에 넣으면 금속 부품은 '부자재'가 아니라 관리되는 부품이 되고, 구매·QC·공급자가 같은 수치에 책임을 질 수 있습니다.",
    }),
]

RELATED = [
    {"slug": "garment-buttons-fasteners-guide.html",
     "zh": "鈕扣與扣件：材質、尺寸與拉力", "en": "Buttons and fasteners: material, size and strength",
     "fr": "Boutons et fermetures : matière, taille, résistance", "es": "Botones y cierres: material, tamaño y resistencia",
     "ja": "ボタンと留め具：材質・サイズ・強度", "ko": "버튼과 여밈: 재질·사이즈·강도"},
    {"slug": "metal-trims-nickel-release-guide.html",
     "zh": "金屬輔料的鎳釋放：怎麼測、怎麼過", "en": "Nickel release on metal trims: testing and clearance",
     "fr": "Migration du nickel sur les accessoires métalliques", "es": "Migración de níquel en herrajes metálicos",
     "ja": "金属付属品のニッケル溶出：試験と合否", "ko": "금속 부자재 니켈 용출: 시험과 판정"},
    {"slug": "lingerie-bra-trims-guide.html",
     "zh": "內衣輔料：鉤扣、肩帶與背扣的選型", "en": "Lingerie trims: hooks, straps and back closures",
     "fr": "Accessoires de lingerie : agrafes, bretelles, dos", "es": "Accesorios de lencería: corchetes, tirantes, espalda",
     "ja": "ランジェリー資材：ホック・肩ひも・背扣", "ko": "란제리 부자재: 후크·어깨끈·후면 여밈"},
    {"slug": "trim-attachment-strength-pull-test-guide.html",
     "zh": "輔料接著強力：拉力測試怎麼做", "en": "Trim attachment strength: how to run the pull test",
     "fr": "Résistance d'assemblage : conduire l'essai de traction", "es": "Resistencia de unión: cómo hacer el ensayo de tracción",
     "ja": "付属品の取付強度：引張試験の進め方", "ko": "부자재 부착 강도: 인장 시험 방법"},
]

CTA_P = {
    "zh": "要做鉤扣帶？把用途（內衣／褲腰／裙裝）、鉤數、目標市場與年用量發給我們，我們會回一份含鍍層選項、鎳釋放測試與拉力數值的規格，並附可縫樣品。",
    "en": "Working on a hook and eye? Send the application, hook count, destination markets and annual volume, and we will return a specification with coating options, nickel release testing and pull values, plus a sewable sample.",
    "fr": "Un ruban agrafe-crochet en projet ? Indiquez l'usage, le nombre d'agrafes, les marchés et le volume annuel : nous renverrons une spécification avec options de revêtement, essai de nickel et valeurs de traction, plus un échantillon cousable.",
    "es": "¿Está trabajando una cinta de corchetes? Envíe el uso, el número de corchetes, los mercados destino y el volumen anual: devolveremos una especificación con opciones de recubrimiento, ensayo de níquel y valores de tracción, más una muestra cosible.",
    "ja": "ホックテープをご検討ですか。用途（下着・腰・スカート）、フック数、対象市場、年間数量をお送りください。めっきの選択肢、ニッケル溶出試験、引張数値を含む仕様と縫製可能なサンプルをご提案します。",
    "ko": "후크앤아이 테이프를 준비 중이신가요? 용도(속옷·허리·스커트), 후크 수, 대상 시장, 연간 수량을 보내주시면 도금 옵션·니켈 용출 시험·인장 수치를 담은 사양서와 봉제 가능한 샘플을 제안합니다.",
}
CTA_BTN = {
    "zh": "索取鉤扣帶規格 →", "en": "Request a hook and eye spec →", "fr": "Demander une spécification →",
    "es": "Solicitar una especificación →", "ja": "ホックテープの仕様を依頼 →", "ko": "후크앤아이 사양 요청 →",
}
