# -*- coding: utf-8 -*-
"""2026-11-21 20:00 第二篇：袋布（Pocketing Fabric）（英文主稿，zh/fr/es/ja/ko 從英文翻譯）"""

SLUG = "pocketing-fabric-guide.html"
CAT = {"zh": "布料與裡布", "en": "Fabrics & Linings", "fr": "Tissus et doublures", "es": "Tejidos y forros",
       "ja": "生地・裏布", "ko": "원단·안감"}
TITLE = {
    "zh": "袋布選型：克重、縮水與色牢度 | TAGE",
    "en": "Pocketing Fabric: Weight, Shrinkage and Colorfastness | TAGE",
    "fr": "Tissu de poche : grammage, retrait et solidité | TAGE",
    "es": "Tela de bolsillo: gramaje, encogimiento y solidez | TAGE",
    "ja": "ポケット地の選定：目付・収縮・染色堅牢度 | TAGE",
    "ko": "포켓지 선정: 평량·수축·염색 견뢰도 | TAGE",
}
DESC = {
    "zh": "袋布決定口袋能不能撐過洗水：克重、縮水率、耐摩擦與耐汗色牢度，加上各市場的甲醛與偶氮限值。五種常見袋布的規格對照、縮水與色牢度測試條件、採購單寫法，一次講清。",
    "en": "Pocketing fabric decides if a pocket bag survives washing: weight in g/m², shrinkage, crocking fastness and the formaldehyde limits each market enforces.",
    "fr": "Le tissu de poche décide si le sac de poche survit au lavage : grammage en g/m², retrait, frottement, sueur, et les limites de formaldéhyde et d'azocolorants.",
    "es": "La tela de bolsillo decide si el forro del bolsillo sobrevive al lavado: gramaje en g/m², encogimiento, frote, sudor y los límites de formaldehído y azocolorantes.",
    "ja": "ポケット地は洗濯に耐えるかを決めます。g/m² の目付、収縮率、摩擦・汗の染色堅牢度、ホルムアルデヒドとアゾ染料の規制値まで。",
    "ko": "포켓지는 세탁 후에도 견디는지를 결정합니다. g/m² 평량, 수축률, 마찰·땀 견뢰도, 시장별 포름알데히드·아조 염료 기준까지 정리합니다.",
}
H1 = {
    "zh": "袋布：四個數字決定它撐不撐得住",
    "en": "Pocketing Fabric: Four Numbers Before You Choose",
    "fr": "Tissu de poche : quatre chiffres avant de choisir",
    "es": "Tela de bolsillo: cuatro cifras antes de elegir",
    "ja": "ポケット地：選ぶ前に確認する 4 つの数値",
    "ko": "포켓지: 고르기 전에 확인할 네 가지 수치",
}
DATE = {"zh": "泰閣包裝 · 更新於 2026年11月21日",
        "en": "By TAGE Packaging &nbsp;·&nbsp; Updated November 21, 2026",
        "fr": "Par TAGE Packaging &nbsp;·&nbsp; Mis à jour le 21 novembre 2026",
        "es": "Por TAGE Packaging &nbsp;·&nbsp; Actualizado el 21 de noviembre de 2026",
        "ja": "泰閣包装 · 2026年11月21日更新",
        "ko": "TAGE 패키징 · 2026년 11월 21일 업데이트"}

BLOCKS = [
    ("p", {
        "zh": "袋布（pocketing）是整件衣服裡最容易被省掉、也最先被穿壞的一塊布。它每天貼著口袋內容物摩擦，被手插進插出，跟著整件衣服洗滌與烘乾；破洞、起毛球、掉色染到裡布，幾乎都從這裡開始。選袋布不需要憑手感，四個數字就夠：克重、縮水率、耐摩擦色牢度、耐汗色牢度。加上各市場的化學限值，就構成一份可驗收的規格。",
        "en": "Pocketing is the panel most often trimmed out of a cost sheet and the first one to wear through. It rubs against whatever is in the pocket, gets pushed in and out by a hand all day, and goes through every wash and dry the garment does. Holes, pilling and colour bleeding into the lining almost always start here. Choosing pocketing does not need a hand-feel argument: four numbers settle it, weight, shrinkage, crocking fastness and perspiration fastness, plus the chemical limits of each destination market.",
        "fr": "Le tissu de poche est le panneau que l'on rabote le plus vite dans un chiffrage et celui qui s'use le premier. Il frotte contre le contenu de la poche, il est poussé et retiré par la main toute la journée, il subit chaque lavage et chaque séchage du vêtement. Trous, bouloches et dégorgements sur la doublure commencent presque toujours ici. Choisir un tissu de poche ne relève pas du ressenti : quatre chiffres tranchent, le grammage, le retrait, la solidité au frottement et la solidité à la sueur, auxquels s'ajoutent les limites chimiques de chaque marché.",
        "es": "La tela de bolsillo es el panel que más se recorta en un desglose de costes y el primero que se agujerea. Roza contra lo que lleva el bolsillo, la mano la empuja y la saca todo el día, y pasa por cada lavado y secado de la prenda. Los agujeros, el pilling y el sangrado de color sobre el forro casi siempre empiezan aquí. Elegir tela de bolsillo no es cuestión de tacto: cuatro cifras lo resuelven, gramaje, encogimiento, solidez al frote y solidez al sudor, más los límites químicos de cada mercado.",
        "ja": "ポケット地は、原価計算で最も削られやすく、最初に傷むパーツです。中身と擦れ、手が一日に何度も出し入れし、洗濯と乾燥を本体と同じだけ受けます。穴、毛玉、裏地への色移りは、ほとんどここから始まります。ポケット地の選定は手触りの議論ではなく、目付、収縮率、摩擦堅牢度、汗堅牢度という 4 つの数値で決まります。これに各市場の化学物質規制値を加えれば、検収できる仕様になります。",
        "ko": "포켓지는 원가 산출에서 가장 먼저 깎이는 패널이자 가장 먼저 해지는 패널입니다. 안에 든 물건과 마찰하고, 손이 하루에도 여러 번 드나들며, 의류와 똑같이 세탁과 건조를 겪습니다. 구멍, 보풀, 안감으로의 이염은 대부분 여기서 시작합니다. 포켓지 선택은 촉감 논쟁이 아니라 평량, 수축률, 마찰 견뢰도, 땀 견뢰도라는 네 수치로 결정되며, 여기에 시장별 화학물질 기준을 더하면 검수 가능한 사양이 됩니다.",
    }),

    ("h2", {
        "zh": "一、五種袋布，五種用途",
        "en": "1. Five Pocketing Fabrics, Five Jobs",
        "fr": "1. Cinq tissus de poche, cinq usages",
        "es": "1. Cinco telas de bolsillo, cinco usos",
        "ja": "1. 5 種類のポケット地と用途",
        "ko": "1. 다섯 가지 포켓지와 쓰임",
    }),

    ("p", {
        "zh": "滌綸塔夫綢（190T／210T，55–75 g/m²）是西褲與外套袋布的主力：薄、滑、便宜，手插進去阻力小，缺點是容易靜電與勾絲。全棉府綢（110–130 g/m²）透氣、親膚，適合貼身穿的襯衫與童裝，但要先預縮。牛仔褲袋布用全棉斜紋或針織平布（150–220 g/m²），要耐磨、耐石洗。運動與內衣類用網眼布（80–120 g/m²），要求快乾與柔軟。高級西裝用銅氨絲或滌黏混紡，賣點是滑順與垂墜，成本也最高。",
        "en": "Polyester taffeta, 190T or 210T at 55 to 75 g/m², is the workhorse for trousers and outerwear: thin, slick, cheap, low drag on the hand, but prone to static and snagging. Cotton poplin at 110 to 130 g/m² breathes and feels good against skin, which suits shirts and childrenswear, though it must be pre-shrunk. Denim pocket bags use cotton twill or a knit jersey at 150 to 220 g/m² that has to survive stone washing. Sportswear and underwear take mesh at 80 to 120 g/m² for quick drying and softness. Tailored jackets use cupro or a polyester viscose blend for drape and slip, at the highest cost.",
        "fr": "Le taffetas polyester 190T ou 210T, à 55 à 75 g/m², est la base des pantalons et des vestes : fin, glissant, économique, peu de résistance au passage de la main, mais sujet à l'électricité statique et aux accrocs. La popeline de coton à 110 à 130 g/m² respire et reste agréable sur la peau, ce qui convient aux chemises et au prêt-à-porter enfant, à condition de la prérétrécir. Les sacs de poche de jean utilisent une sergé de coton ou une maille jersey de 150 à 220 g/m² qui doit résister au délavage aux pierres. Le sport et la lingerie prennent une maille filet de 80 à 120 g/m² pour le séchage rapide et la douceur. Le tailoring emploie cupro ou mélange polyester viscose pour le tombé et le glissant, au coût le plus élevé.",
        "es": "El tafetán de poliéster 190T o 210T, de 55 a 75 g/m², es la base de pantalones y prendas de abrigo: fino, deslizante, barato, poca resistencia al paso de la mano, pero propenso a la electricidad estática y a los enganches. La popelina de algodón de 110 a 130 g/m² transpira y resulta agradable en la piel, lo que sirve para camisas e infantil, siempre que esté preencogida. Los bolsillos del vaquero usan sarga de algodón o punto jersey de 150 a 220 g/m² que debe resistir el lavado a la piedra. El deporte y la lencería llevan malla de 80 a 120 g/m² por secado rápido y suavidad. La sastrería emplea cupro o mezcla poliéster viscosa por caída y deslizamiento, al coste más alto.",
        "ja": "ポリエステルタフタ（190T／210T、55〜75 g/m²）はスラックスとアウターの定番です。薄く、滑り、安価で、手の出し入れ抵抗が小さい反面、静電気と引っ掛けに弱い素材です。綿ポプリン（110〜130 g/m²）は通気性と肌触りが良く、シャツや子ども服に向きますが、事前に防縮が必要です。デニムのポケット地は綿ツイルや天竺編み（150〜220 g/m²）で、ストーンウォッシュに耐える必要があります。スポーツとインナーはメッシュ（80〜120 g/m²）で速乾性と柔らかさを取ります。紳士服はキュプラやポリエステル・レーヨン混でドレープと滑りを出し、コストは最も高くなります。",
        "ko": "폴리에스터 태프타(190T/210T, 55~75 g/m²)는 슬랙스와 아우터의 주력으로, 얇고 미끄럽고 저렴하며 손이 드나들 때 저항이 적지만 정전기와 올 뜯김에 약합니다. 면 포플린(110~130 g/m²)은 통기성과 피부 감촉이 좋아 셔츠와 아동복에 맞지만 사전 수축 처리가 필요합니다. 데님 포켓지는 면 트윌이나 저지 편물(150~220 g/m²)로 스톤 워싱을 견뎌야 합니다. 스포츠와 이너웨어는 메시(80~120 g/m²)로 속건성과 부드러움을 잡습니다. 정장은 큐프라나 폴리에스터·레이온 혼방으로 드레이프와 미끄러짐을 내며 원가가 가장 높습니다.",
    }),

    ("h2", {
        "zh": "二、克重與縮水：兩個數字先對",
        "en": "2. Weight and Shrinkage: Get These Two Right First",
        "fr": "2. Grammage et retrait : régler ces deux chiffres d'abord",
        "es": "2. Gramaje y encogimiento: primero estas dos cifras",
        "ja": "2. 目付と収縮：まずこの 2 つを合わせる",
        "ko": "2. 평량과 수축: 이 두 수치를 먼저 맞춘다",
    }),

    ("p", {
        "zh": "克重低於 55 g/m² 的塔夫綢在口袋轉角容易磨穿，高於 90 g/m² 則讓口袋顯得鼓脹、影響外觀平整。棉質袋布縮水率要控制在經向 3 % 以內、緯向 2 % 以內，否則洗完口袋會把側縫往外拉；測試按 60 °C 水洗一次、翻滾烘乾一次，量前後尺寸，這是買家最常要求的一組數字。袋布與本布的縮水率差異超過 2 %，水洗後就一定會出現口袋外露或布料堆積。",
        "en": "Taffeta below 55 g/m² wears through at the pocket corners; above 90 g/m² the pocket reads bulky and disturbs the line of the garment. Cotton pocketing should shrink no more than 3 percent warp and 2 percent weft, or the pocket pulls the side seam out after washing. Test it the way buyers ask: one wash at 60 °C and one tumble dry, then measure. If pocketing and shell differ by more than 2 percentage points in shrinkage, the pocket will either peek out or the shell will bunch, and no amount of pressing fixes it.",
        "fr": "Une taffetas sous 55 g/m² perce aux angles de poche ; au-dessus de 90 g/m², la poche paraît gonflante et casse la ligne du vêtement. Un tissu de poche coton doit rester sous 3 % de retrait en chaîne et 2 % en trame, sinon la poche tire la couture de côté après lavage. Testez comme le demandent les acheteurs : un lavage à 60 °C et un séchage en tambour, puis mesurez. Si l'écart de retrait entre poche et principal dépasse 2 points, la poche ressortira ou le tissu godera, et aucun repassage ne corrige cela.",
        "es": "Un tafetán por debajo de 55 g/m² se agujerea en las esquinas del bolsillo; por encima de 90 g/m² el bolsillo se ve abultado y rompe la línea de la prenda. La tela de bolsillo de algodón debe encoger como máximo un 3 % en urdimbre y un 2 % en trama, o el bolsillo tirará de la costura lateral tras el lavado. Pruébelo como piden los compradores: un lavado a 60 °C y un secado en tambor, y luego mida. Si la diferencia de encogimiento entre bolsillo y exterior supera 2 puntos, el bolsillo asomará o la tela se abolsará, y ningún planchado lo arregla.",
        "ja": "55 g/m² 未満のタフタはポケットの角から摩耗して穴が開き、90 g/m² を超えるとポケットが膨らんでシルエットを崩します。綿ポケット地は経方向 3 % 以内、緯方向 2 % 以内の収縮に抑えないと、洗濯後にポケットが脇線を引っ張ります。バイヤーの指定どおり、60 °C で 1 回洗濯しタンブラー乾燥 1 回の前後で寸法を測ります。ポケット地と表地の収縮差が 2 ポイントを超えると、洗濯後にポケットが出るか生地が余り、アイロンでは直りません。",
        "ko": "55 g/m² 미만의 태프타는 포켓 모서리에서 구멍이 나고, 90 g/m²를 넘으면 포켓이 부풀어 실루엣을 흐트립니다. 면 포켓지는 경사 3 % 이내, 위사 2 % 이내로 수축을 억제하지 않으면 세탁 후 포켓이 옆 솔기를 잡아당깁니다. 바이어가 요구하는 방식대로 60 °C 세탁 1회와 텀블 건조 1회 전후 치수를 측정합니다. 포켓지와 겉감의 수축 차이가 2포인트를 넘으면 세탁 후 포켓이 삐져나오거나 원단이 남아 다림질로도 해결되지 않습니다.",
    }),

    ("table", {
        "head": [
            {"zh": "袋布類型", "en": "Pocketing type", "fr": "Type de tissu de poche", "es": "Tipo de tela", "ja": "ポケット地の種類", "ko": "포켓지 종류"},
            {"zh": "克重", "en": "Weight", "fr": "Grammage", "es": "Gramaje", "ja": "目付", "ko": "평량"},
            {"zh": "適用", "en": "Best for", "fr": "Usage", "es": "Uso", "ja": "用途", "ko": "용도"},
        ],
        "rows": [
            [
                {"zh": "滌綸塔夫綢 190T", "en": "Polyester taffeta 190T", "fr": "Taffetas polyester 190T", "es": "Tafetán poliéster 190T", "ja": "ポリエステルタフタ 190T", "ko": "폴리에스터 태프타 190T"},
                {"zh": "55–65 g/m²", "en": "55 to 65 g/m²", "fr": "55 à 65 g/m²", "es": "55 a 65 g/m²", "ja": "55〜65 g/m²", "ko": "55~65 g/m²"},
                {"zh": "西褲、休閒褲、外套", "en": "Trousers, chinos, outerwear", "fr": "Pantalons, chinos, vestes", "es": "Pantalones, chinos, abrigo", "ja": "スラックス、チノ、アウター", "ko": "슬랙스, 치노, 아우터"},
            ],
            [
                {"zh": "全棉府綢（預縮）", "en": "Cotton poplin, pre-shrunk", "fr": "Popeline coton prérétrécie", "es": "Popelina algodón preencogida", "ja": "綿ポプリン（防縮加工）", "ko": "면 포플린(사전 수축)"},
                {"zh": "110–130 g/m²", "en": "110 to 130 g/m²", "fr": "110 à 130 g/m²", "es": "110 a 130 g/m²", "ja": "110〜130 g/m²", "ko": "110~130 g/m²"},
                {"zh": "襯衫、童裝、貼身衣物", "en": "Shirts, childrenswear, next to skin", "fr": "Chemises, enfant, au contact", "es": "Camisas, infantil, contacto", "ja": "シャツ、子ども服、肌着", "ko": "셔츠, 아동복, 속옷"},
            ],
            [
                {"zh": "全棉斜紋", "en": "Cotton twill", "fr": "Sergé de coton", "es": "Sarga de algodón", "ja": "綿ツイル", "ko": "면 트윌"},
                {"zh": "150–180 g/m²", "en": "150 to 180 g/m²", "fr": "150 à 180 g/m²", "es": "150 a 180 g/m²", "ja": "150〜180 g/m²", "ko": "150~180 g/m²"},
                {"zh": "牛仔褲、工裝褲", "en": "Denim, workwear", "fr": "Jean, vêtement de travail", "es": "Vaquero, laboral", "ja": "デニム、ワークウェア", "ko": "데님, 워크웨어"},
            ],
            [
                {"zh": "針織平布", "en": "Knit jersey", "fr": "Maille jersey", "es": "Punto jersey", "ja": "天竺編み", "ko": "저지 편물"},
                {"zh": "180–220 g/m²", "en": "180 to 220 g/m²", "fr": "180 à 220 g/m²", "es": "180 a 220 g/m²", "ja": "180〜220 g/m²", "ko": "180~220 g/m²"},
                {"zh": "牛仔褲、彈力褲", "en": "Denim, stretch trousers", "fr": "Jean, pantalon stretch", "es": "Vaquero, pantalón elástico", "ja": "デニム、ストレッチパンツ", "ko": "데님, 스트레치 팬츠"},
            ],
            [
                {"zh": "網眼布", "en": "Mesh", "fr": "Maille filet", "es": "Malla", "ja": "メッシュ", "ko": "메시"},
                {"zh": "80–120 g/m²", "en": "80 to 120 g/m²", "fr": "80 à 120 g/m²", "es": "80 a 120 g/m²", "ja": "80〜120 g/m²", "ko": "80~120 g/m²"},
                {"zh": "運動服、內衣、泳裝", "en": "Sportswear, underwear, swim", "fr": "Sport, lingerie, bain", "es": "Deporte, lencería, baño", "ja": "スポーツ、下着、水着", "ko": "스포츠, 속옷, 수영복"},
            ],
        ],
    }),

    ("h2", {
        "zh": "三、色牢度：袋布是貼著皮膚摩擦的那一面",
        "en": "3. Colorfastness: The Side That Rubs Against Skin",
        "fr": "3. Solidité des couleurs : la face qui frotte la peau",
        "es": "3. Solidez del color: la cara que roza la piel",
        "ja": "3. 染色堅牢度：肌と擦れる面",
        "ko": "3. 염색 견뢰도: 피부와 마찰하는 면",
    }),

    ("p", {
        "zh": "袋布的要求常被低估計：深色袋布掉色，染到淺色裡布或本布，是成衣廠最常見的索賠項之一。驗收三項：耐摩擦色牢度乾摩 ≥ 4 級、濕摩 ≥ 3 級；耐汗（酸、鹼各一）≥ 3–4 級；耐水洗（40 °C，5 次）變色 ≥ 4 級、沾色 ≥ 3–4 級。深藍、黑色、大紅這三個顏色最容易不合格，打樣階段就要做，不要等到大貨抽檢。",
        "en": "The demands on pocketing are routinely underestimated. A dark pocket bag that bleeds onto a pale lining or shell is one of the most common claims a garment factory faces. Three test items settle it: crocking fastness at grade 4 or better dry and grade 3 or better wet; perspiration fastness, acidic and alkaline, at grade 3 to 4 or better; and wash fastness at 40 °C for five cycles with colour change at grade 4 and staining at grade 3 to 4. Navy, black and deep red are the three colours that fail most, so test at sampling, not at final inspection.",
        "fr": "Les exigences sur le tissu de poche sont systématiquement sous-estimées. Une poche foncée qui dégorge sur une doublure ou un principal clair est l'une des réclamations les plus fréquentes en confection. Trois essais tranchent : la solidité au frottement, note 4 ou plus à sec et 3 ou plus à l'humide ; la solidité à la sueur, acide et alcaline, note 3 à 4 ou plus ; et la solidité au lavage à 40 °C sur cinq cycles, avec changement de teinte note 4 et dégorgement note 3 à 4. Le marine, le noir et le rouge profond sont les trois couleurs qui échouent le plus : testez à l'échantillon, pas au contrôle final.",
        "es": "Las exigencias sobre la tela de bolsillo se subestiman de forma sistemática. Un bolsillo oscuro que sangra sobre un forro o un exterior claro es una de las reclamaciones más frecuentes en confección. Tres ensayos lo resuelven: solidez al frote, nota 4 o más en seco y 3 o más en húmedo; solidez al sudor, ácido y alcalino, nota 3 a 4 o más; y solidez al lavado a 40 °C durante cinco ciclos, con cambio de color nota 4 y sangrado nota 3 a 4. El azul marino, el negro y el rojo profundo son los tres colores que más fallan, así que pruebe en muestra, no en la inspección final.",
        "ja": "ポケット地への要求は往々にして過小評価されます。濃色のポケット地が淡色の裏地や表地に色移りするのは、縫製工場で最も多いクレームのひとつです。検収は 3 項目で、摩擦堅牢度が乾燥 4 級以上・湿潤 3 級以上、汗堅牢度（酸性・アルカリ性）が 3〜4 級以上、40 °C 洗濯 5 回で変退色 4 級・汚染 3〜4 級以上です。濃紺、黒、深紅の 3 色が最も不合格になりやすく、量産検査ではなくサンプル段階で試験してください。",
        "ko": "포켓지에 대한 요구는 흔히 과소평가됩니다. 진한 색 포켓지가 밝은 안감이나 겉감으로 이염되는 것은 봉제 공장에서 가장 흔한 클레임 중 하나입니다. 검수는 세 항목으로, 마찰 견뢰도가 건조 4급 이상·습윤 3급 이상, 땀 견뢰도(산성·알칼리성) 3~4급 이상, 40 °C 세탁 5회에서 변퇴색 4급·오염 3~4급 이상입니다. 네이비, 블랙, 진홍 세 색이 가장 자주 부적합이 나오므로 양산 검사가 아니라 샘플 단계에서 시험하십시오.",
    }),

    ("h2", {
        "zh": "四、化學限值：各市場的門檻不一樣",
        "en": "4. Chemical Limits: Every Market Draws a Different Line",
        "fr": "4. Limites chimiques : chaque marché a sa ligne",
        "es": "4. Límites químicos: cada mercado marca su línea",
        "ja": "4. 化学物質の規制値：市場ごとに線が違う",
        "ko": "4. 화학물질 기준: 시장마다 선이 다르다",
    }),

    ("p", {
        "zh": "中國 GB 18401 的 B 類（直接接觸皮膚）要求甲醛 ≤ 75 mg/kg、pH 4.0–8.5、可分解芳香胺染料禁用；歐盟走 REACH 法規，偶氮染料 ≤ 30 mg/kg，SVHC 超過 0.1 % 需通報；美國兒童產品受 CPSIA 管，成人服裝多靠買家自訂 RSList。日本依家庭用品品質表示法要求標示組成（混用率）與洗濯表示，有害物質另受「有害物質を含有する家庭用品の規制に関する法律」約束。韓國則要求標示混用率與 취급 표시，兒童產品另需 KC 安全確認。同一批袋布發往三個市場，就要準備三套測試報告。",
        "en": "China s GB 18401 class B, for direct skin contact, caps formaldehyde at 75 mg/kg, requires pH between 4.0 and 8.5, and bans cleavable aromatic amine dyes. In the EU, REACH limits azo dyes to 30 mg/kg and requires notification above 0.1 percent for SVHCs. In the United States, children s products fall under CPSIA while adult apparel relies on buyer restricted substance lists. Japan requires fibre composition and care labelling under the Household Goods Quality Labelling Act, with hazardous substances governed separately. Korea requires fibre content and care instructions, plus KC safety confirmation for children s products. One lot of pocketing shipped to three markets needs three test reports.",
        "fr": "En Chine, la classe B de la norme GB 18401, celle du contact direct avec la peau, plafonne le formaldéhyde à 75 mg/kg, impose un pH entre 4,0 et 8,5 et interdit les colorants à amines aromatiques clivables. Dans l'UE, REACH limite les colorants azoïques à 30 mg/kg et impose une notification au-delà de 0,1 % pour les SVHC. Aux États-Unis, les produits enfants relèvent du CPSIA, tandis que le prêt-à-porter adulte dépend des listes de substances restreintes des acheteurs. Le Japon impose la composition et l'entretien via la loi sur l'étiquetage de qualité des biens de consommation. La Corée exige la composition et les instructions d'entretien, plus une confirmation KC pour les produits enfants. Un lot expédié sur trois marchés demande trois rapports d'essai.",
        "es": "En China, la clase B de GB 18401, la de contacto directo con la piel, limita el formaldehído a 75 mg/kg, exige pH entre 4,0 y 8,5 y prohíbe los colorantes de aminas aromáticas escindibles. En la UE, REACH limita los colorantes azoicos a 30 mg/kg y exige notificación por encima del 0,1 % para las SVHC. En Estados Unidos, los productos infantiles dependen de CPSIA y el adulto de las listas de sustancias restringidas del comprador. Japón exige composición y cuidado mediante la ley de etiquetado de calidad de bienes de consumo. Corea pide composición e instrucciones de cuidado, más confirmación KC en infantil. Un lote para tres mercados exige tres informes de ensayo.",
        "ja": "中国の GB 18401 は B 類（直接皮膚接触）でホルムアルデヒド 75 mg/kg 以下、pH 4.0〜8.5、分解性芳香族アミン染料の使用禁止を求めます。EU は REACH で偶氮染料 30 mg/kg 以下、SVHC は 0.1 % 超で届出が必要です。米国の子ども用品は CPSIA、大人服はバイヤーの制限物質リストに依ります。日本は家庭用品品質表示法により組成（混用率）と洗濯表示を義務づけ、有害物質は別法で規制されます。韓国は混用率と 취급 표시（取扱表示）を求め、子ども用品は KC 安全確認も必要です。1 ロットを 3 市場へ出荷するなら、試験報告書も 3 セット必要です。",
        "ko": "중국 GB 18401 B급(피부 직접 접촉)은 포름알데히드 75 mg/kg 이하, pH 4.0~8.5, 분해성 방향족 아민 염료 사용을 금지합니다. EU는 REACH로 아조 염료 30 mg/kg 이하, SVHC 0.1 % 초과 시 신고를 요구합니다. 미국은 어린이제품이 CPSIA, 성인복은 바이어 제한물질목록을 따릅니다. 일본은 「가정용품 품질표시법」으로 조성(혼용률)과 세탁 표시를 의무화하고 유해물질은 별도 법령으로 규제합니다. 한국은 품질경영 및 공산품 안전관리법에 따라 혼용률과 취급 표시 등 품질 표시를 요구하며, 어린이제품은 KC 인증(안전 확인)이 추가됩니다. 한 로트를 세 시장에 보낸다면 시험 성적서도 세 세트가 필요합니다.",
    }),

    ("h2", {
        "zh": "五、採購單與驗收清單",
        "en": "5. Purchase Order and Inspection List",
        "fr": "5. Bon de commande et liste de contrôle",
        "es": "5. Pedido y lista de inspección",
        "ja": "5. 発注書と検収チェックリスト",
        "ko": "5. 발주서와 검수 체크리스트",
    }),

    ("ul", [
        {"zh": "成分與克重寫死：例「100 % 滌綸，65 g/m² ± 3 %」，不要只寫「滌綸布」",
         "en": "Fix fibre and weight: 100 percent polyester at 65 g/m² plus or minus 3 percent, not just polyester fabric",
         "fr": "Figer la composition et le grammage : 100 % polyester à 65 g/m² plus ou moins 3 %, pas simplement tissu polyester",
         "es": "Fijar composición y gramaje: 100 % poliéster a 65 g/m² más o menos 3 %, no solo tela de poliéster",
         "ja": "組成と目付を数値で指定：例「ポリエステル 100 %、65 g/m² ±3 %」。単に「ポリエステル生地」と書かない",
         "ko": "조성과 평량을 수치로 명시: 예 '폴리에스터 100 %, 65 g/m² ±3 %'. '폴리에스터 원단'이라고만 쓰지 않습니다"},
        {"zh": "幅寬與有效門幅分開寫（如 150 cm 門幅，可用 148 cm）",
         "en": "State width and usable width separately, for example 150 cm width with 148 cm usable",
         "fr": "Indiquer la laize et la laize utile séparément, par exemple 150 cm de laize, 148 cm utiles",
         "es": "Indicar ancho total y ancho útil por separado, por ejemplo 150 cm de ancho y 148 cm útiles",
         "ja": "原反幅と有効幅を分けて記載（例：幅 150 cm、有効 148 cm）",
         "ko": "원단 폭과 유효 폭을 구분해 기재(예: 폭 150 cm, 유효 148 cm)"},
        {"zh": "縮水率與測試條件（60 °C 水洗 + 烘乾各一次）",
         "en": "Shrinkage and the test method: one wash at 60 °C and one tumble dry",
         "fr": "Retrait et méthode d'essai : un lavage à 60 °C et un séchage en tambour",
         "es": "Encogimiento y método: un lavado a 60 °C y un secado en tambor",
         "ja": "収縮率と試験条件（60 °C 洗濯 1 回＋タンブラー乾燥 1 回）",
         "ko": "수축률과 시험 조건(60 °C 세탁 1회 + 텀블 건조 1회)"},
        {"zh": "色牢度三項等級與色差 ΔE ≤ 1.0（同批不同缸）",
         "en": "The three fastness grades plus colour difference within Delta E 1.0 across dye lots",
         "fr": "Les trois notes de solidité et un écart de teinte dans Delta E 1,0 entre bains",
         "es": "Las tres notas de solidez y diferencia de color dentro de Delta E 1,0 entre baños",
         "ja": "3 つの堅牢度等級と、ロット間の色差 ΔE 1.0 以下",
         "ko": "세 가지 견뢰도 등급과 로트 간 색차 ΔE 1.0 이하"},
        {"zh": "每批附測試報告（甲醛、偶氮、pH），批號與卷標對應",
         "en": "A test report per lot covering formaldehyde, azo dyes and pH, with lot number matching the roll label",
         "fr": "Un rapport par lot couvrant formaldéhyde, azoïques et pH, numéro de lot concordant avec l'étiquette",
         "es": "Un informe por lote con formaldehído, azoicos y pH, con número de lote coincidente con la etiqueta",
         "ja": "ロットごとにホルムアルデヒド・偶氮染料・pH の試験報告書、ロット番号と巻ラベルの一致",
         "ko": "로트별 포름알데히드·아조 염료·pH 시험 성적서, 로트 번호와 롤 라벨 일치"},
    ]),

    ("callout", {
        "zh": "四個數字：克重 65 g/m² ±3 %、縮水 ≤ 3 %、乾摩 ≥ 4 級、甲醛 ≤ 75 mg/kg。四項都寫進採購單，袋布才算定義完成。",
        "en": "Four numbers: 65 g/m² within 3 percent, shrinkage at or below 3 percent, dry crocking at grade 4, formaldehyde at or below 75 mg/kg. Put all four on the purchase order and the pocketing is actually specified.",
        "fr": "Quatre chiffres : 65 g/m² à 3 % près, retrait jusqu à 3 %, frottement à sec note 4, formaldéhyde à 75 mg/kg. Inscrivez les quatre : le tissu de poche est alors vraiment spécifié.",
        "es": "Cuatro cifras: 65 g/m² con 3 % de tolerancia, encogimiento hasta 3 %, frote en seco nota 4, formaldehído hasta 75 mg/kg. Con las cuatro en el pedido, la tela de bolsillo queda especificada.",
        "ja": "4 つの数値：65 g/m² ±3 %、収縮 3 % 以下、乾燥摩擦 4 級以上、ホルムアルデヒド 75 mg/kg 以下。4 つとも発注書に入れて初めて仕様になります。",
        "ko": "네 수치: 65 g/m² ±3 %, 수축 3 % 이하, 건조 마찰 4급 이상, 포름알데히드 75 mg/kg 이하. 네 가지를 모두 발주서에 넣어야 사양이 완성됩니다.",
    }),

    ("p", {
        "zh": "袋布在一件衣服的物料清單裡通常只佔 1–2 % 的金額，但它決定口袋能否用兩年、決定洗後口袋會不會露出來、也決定深色款會不會把裡布染花。把克重、縮水、色牢度、化學限值四項固定下來，採購與成衣廠就有一致的判定基礎；省下的不是那 1 % 的布料錢，而是索賠與返修的工時。",
        "en": "Pocketing usually accounts for 1 to 2 percent of a garment bill of materials, yet it decides whether a pocket lasts two years, whether the bag peeks out after washing, and whether a dark colour ruins the lining. Fix the four items, weight, shrinkage, fastness and chemical limits, and purchasing and the garment factory judge to the same standard. What you save is not the 1 percent of fabric cost but the labour hours that go into claims and rework.",
        "fr": "Le tissu de poche représente en général 1 à 2 % du coût matière d'un vêtement, mais il décide si une poche tient deux ans, si le sac ressort après lavage et si une couleur foncée abîme la doublure. Figez les quatre points, grammage, retrait, solidité et limites chimiques : achats et confection jugent alors selon le même référentiel. L économie ne porte pas sur 1 % de tissu, mais sur les heures de réclamation et de reprise.",
        "es": "La tela de bolsillo suele ser el 1 o 2 % del coste de materiales de una prenda, pero decide si un bolsillo dura dos años, si el forro del bolsillo asoma tras el lavado y si un color oscuro arruina el forro. Fije los cuatro puntos, gramaje, encogimiento, solidez y límites químicos, y compras y confección juzgarán con el mismo criterio. Lo que se ahorra no es el 1 % de tela, sino las horas de reclamación y reproceso.",
        "ja": "ポケット地は 1 着の資材費の 1〜2 % に過ぎませんが、ポケットが 2 年持つか、洗濯後に袋が出るか、濃色が裏地を染めるかを決めます。目付、収縮、堅牢度、化学規制値の 4 点を固定すれば、購買と縫製工場が同じ基準で判定できます。削れるのは生地代の 1 % ではなく、クレームと手直しの工数です。",
        "ko": "포켓지는 한 벌의 자재비에서 1~2 %에 불과하지만, 포켓이 2년을 버티는지, 세탁 후 주머니가 삐져나오는지, 진한 색이 안감을 망가뜨리는지를 결정합니다. 평량, 수축, 견뢰도, 화학물질 기준 네 가지를 고정하면 구매와 봉제 공장이 같은 기준으로 판정할 수 있습니다. 아끼는 것은 원단비 1 %가 아니라 클레임과 재작업에 드는 공수입니다.",
    }),
]

RELATED = [
    {"slug": "lining-fabric-selection-guide.html",
     "zh": "裡布選型：克重、滑度與透氣", "en": "Lining selection: weight, slip and breathability",
     "fr": "Choix de doublure : grammage, glissant, respirabilité", "es": "Elección de forro: gramaje, deslizamiento, transpirabilidad",
     "ja": "裏地の選定：目付・滑り・通気性", "ko": "안감 선정: 평량·미끄러짐·통기성"},
    {"slug": "trim-color-migration-staining-guide.html",
     "zh": "輔料色移：深色染到淺色怎麼防", "en": "Colour migration: stopping dark trims bleeding into pale fabric",
     "fr": "Migration de couleur : éviter qu'un élément foncé dégorge", "es": "Migración de color: evitar que lo oscuro sangre",
     "ja": "色移り：濃色から淡色への移染を防ぐ", "ko": "이염: 진한 색이 밝은 색으로 번지는 것을 막기"},
    {"slug": "trousers-pants-trims-guide.html",
     "zh": "西褲輔料全解：腰頭、口袋與拉鍊", "en": "Trouser trims: waistband, pockets and zips",
     "fr": "Accessoires de pantalon : ceinture, poches, zips", "es": "Accesorios de pantalón: cinturilla, bolsillos, cremalleras",
     "ja": "スラックスの資材：腰・ポケット・ファスナー", "ko": "슬랙스 부자재: 허리·포켓·지퍼"},
    {"slug": "care-label-fiber-content-tolerance-guide.html",
     "zh": "纖維含量允差：標示與實測差多少", "en": "Fibre content tolerance: how far the label can drift",
     "fr": "Tolérance de composition : l'écart admis", "es": "Tolerancia de composición: el margen admitido",
     "ja": "混用率の許容差：表示と実測の差", "ko": "혼용률 허용 오차: 표시와 실측의 차이"},
]

CTA_P = {
    "zh": "要找袋布？把用途、克重、色號與目標市場發給我們，我們會回一份含縮水與色牢度測試條件、化學限值對應的規格，並附同缸樣布。",
    "en": "Sourcing pocketing? Send the application, weight, colour and destination markets and we will return a specification with shrinkage and fastness test conditions, matching chemical limits, plus a same-dye-lot swatch.",
    "fr": "Vous cherchez un tissu de poche ? Indiquez l'usage, le grammage, le coloris et les marchés : nous renverrons une spécification avec conditions d'essai de retrait et de solidité, limites chimiques et un échantillon du même bain.",
    "es": "¿Busca tela de bolsillo? Envíe el uso, el gramaje, el color y los mercados destino: devolveremos una especificación con condiciones de ensayo de encogimiento y solidez, límites químicos y una muestra del mismo baño.",
    "ja": "ポケット地をお探しですか。用途、目付、色番、対象市場をお送りください。収縮・堅牢度の試験条件、化学規制値の対応を含む仕様と、同ロットの見本をご提案します。",
    "ko": "포켓지를 찾고 계신가요? 용도, 평량, 색상 번호, 대상 시장을 보내주시면 수축·견뢰도 시험 조건과 화학물질 기준 대응을 담은 사양서, 동일 로트 샘플을 제안합니다.",
}
CTA_BTN = {
    "zh": "索取袋布規格 →", "en": "Request a pocketing spec →", "fr": "Demander une spécification →",
    "es": "Solicitar una especificación →", "ja": "ポケット地の仕様を依頼 →", "ko": "포켓지 사양 요청 →",
}
