# -*- coding: utf-8 -*-
"""2026-11-22 08:00 第一篇：刺繡襯紙選型（Embroidery Backing & Stabilizer）（英文主稿，zh/fr/es/ja/ko 從英文翻譯）"""

SLUG = "embroidery-backing-stabilizer-guide.html"
CAT = {"zh": "工藝技術", "en": "Decoration", "fr": "Décoration", "es": "Decoración",
       "ja": "加飾", "ko": "장식 공정"}
TITLE = {
    "zh": "刺繡襯紙選型：切邊、撕裂、水溶與克重 | TAGE",
    "en": "Embroidery Backing and Stabilizer: Cutaway, Tearaway, Wash-Away | TAGE",
    "fr": "Support de broderie : arrachage, découpe, soluble et grammage | TAGE",
    "es": "Entretela para bordado: desgarrable, recortable y soluble | TAGE",
    "ja": "刺繍裏地（バッキング）の選定：カットアウェイ・ティアアウェイ・水溶性 | TAGE",
    "ko": "자수 받침지 선택: 컷어웨이·티어어웨이·수용성 | TAGE",
}
DESC = {
    "zh": "刺繡圖案變形、起皺、發硬，八成問題出在襯紙而不是針法。本文講清切邊／撕裂／水溶／熱熔四種襯紙的克重與適用針數、毛巾布與針織布的貼面選擇、甲醛與纖維標示的合規線，以及五項驗收數字。",
    "en": "Embroidery backing and stabilizer: cutaway, tearaway and wash-away weights by stitch count, toppings for loop fabrics, compliance and acceptance tests.",
    "fr": "Choisir le support de broderie : arrachage, découpe, soluble, grammages selon le nombre de points, film de dessus pour les mailles bouclées et contrôles de conformité.",
    "es": "Cómo elegir entretela de bordado: desgarrable, recortable o soluble, gramajes según puntadas, film superior para tejidos con bucle y controles de conformidad.",
    "ja": "刺繍裏地の選び方。カットアウェイ・ティアアウェイ・水溶性の目付と針数の対応、パイル地の上面フィルム、法令対応と検収項目まで。",
    "ko": "자수 받침지 선택 가이드. 컷어테이·티어어테이·수용성의 평량과 바늘 수 대응, 파일 원단용 상면 필름, 규제 대응과 검수 항목까지 정리합니다.",
}
H1 = {
    "zh": "刺繡襯紙：看不見，但決定圖案會不會變形",
    "en": "Embroidery Backing: You Never See It, and It Decides Everything",
    "fr": "Le support de broderie : invisible, et pourtant décisif",
    "es": "La entretela de bordado: no se ve, pero lo decide todo",
    "ja": "刺繍裏地：見えないのに、すべてを決める",
    "ko": "자수 받침지: 보이지 않지만 모든 것을 결정합니다",
}
DATE = {"zh": "泰閣包裝 · 更新於 2026年11月22日",
        "en": "By TAGE Packaging &nbsp;·&nbsp; Updated November 22, 2026",
        "fr": "Par TAGE Packaging &nbsp;·&nbsp; Mis à jour le 22 novembre 2026",
        "es": "Por TAGE Packaging &nbsp;·&nbsp; Actualizado el 22 de noviembre de 2026",
        "ja": "泰閣包装 · 2026年11月22日更新",
        "ko": "TAGE 패키징 · 2026년 11월 22일 업데이트"}

BLOCKS = [
    ("p", {
        "zh": "刺繡出問題時，多數人先懷疑針法、密度或機器張力，但真正決定圖案會不會變形、洗後會不會起皺、穿起來會不會刺癢的，往往是夾在布料下面那層沒人拍板的刺繡襯紙（backing / stabilizer）。它只佔一件衣服成本的一小部分，卻同時決定外觀、手感與退貨率。本文把選襯紙拆成三件事：它要做什麼、克重怎麼配針數、合規與標示怎麼寫。",
        "en": "When an embroidery job goes wrong, most people blame the stitch path, the density or the machine tension. What actually decides whether the design distorts, whether it ripples after the first wash and whether it scratches the wearer is the layer underneath that nobody signs off: the embroidery backing, also called stabilizer. It is a small part of the garment cost and it settles appearance, hand feel and return rate at the same time. Selection comes down to three questions: what the backing has to do, how its weight matches the stitch count, and how compliance and labelling are written down.",
        "fr": "Quand une broderie rate, on accuse d'abord le chemin de points, la densité ou la tension machine. Ce qui décide vraiment de la déformation du motif, des vagues au premier lavage et de la sensation de grattage sur la peau, c'est la couche située sous le tissu et que personne ne valide : le support de broderie (stabilisateur). Il pèse peu dans le prix de revient et arbitre pourtant l'aspect, le toucher et le taux de retour. Le choix se résume à trois questions : ce que le support doit faire, la correspondance entre grammage et nombre de points, et la façon de documenter conformité et étiquetage.",
        "es": "Cuando un bordado sale mal, casi siempre se culpa al recorrido de puntadas, a la densidad o a la tensión de la máquina. Lo que de verdad decide si el motivo se deforma, si ondula tras el primer lavado y si raspa al usuario es la capa que va debajo y que nadie aprueba: la entretela de bordado (estabilizador). Representa una parte pequeña del coste de la prenda y al mismo tiempo fija el aspecto, el tacto y la tasa de devoluciones. La elección se reduce a tres preguntas: qué debe hacer la entretela, cómo se ajusta el gramaje al número de puntadas y cómo se documentan conformidad y etiquetado.",
        "ja": "刺繍が失敗すると、まず針路・密度・ミシンの糸調子を疑います。しかし柄の歪み、初回洗濯後の波打ち、肌へのチクつきを実際に決めているのは、生地の下に入っていて誰も承認していない層、刺繍裏地（バッキング／スタビライザー）です。原価に占める割合は小さいのに、外観・風合い・返品率を同時に左右します。選定は 3 つの問いに集約されます。裏地が果たす役割、目付と針数の対応、そして法令対応と表示の書き方です。",
        "ko": "자수가 잘못되면 대개 바늘 경로, 밀도, 재봉기 장력을 먼저 의심합니다. 그러나 무늬 변형, 첫 세탁 후 물결, 착용 시 따가움을 실제로 결정하는 것은 원단 아래에 들어가는, 아무도 승인하지 않는 층인 자수 받침지(백킹, 스태빌라이저)입니다. 원가에서 차지하는 비중은 작지만 외관, 촉감, 반품률을 동시에 좌우합니다. 선택은 세 가지 질문으로 정리됩니다. 받침지가 해야 할 역할, 평량과 바늘 수의 대응, 그리고 규제 대응과 표기 방법입니다.",
    }),

    ("h2", {
        "zh": "一、它其實同時做三件事",
        "en": "1. It Does Three Jobs at Once",
        "fr": "1. Il assure trois fonctions à la fois",
        "es": "1. Cumple tres funciones a la vez",
        "ja": "1. 実は 3 つの役割を同時に担う",
        "ko": "1. 실제로 세 가지 역할을 동시에 합니다",
    }),

    ("p", {
        "zh": "第一是承載針跡。刺繡是把幾千針高張力的線壓進布料，沒有襯紙托著，布料會被拉長、圖案兩側會收緊。第二是抑制起皺：針數越密，布料越薄，需要越硬的支撐面，否則洗完一圈波浪。第三是保護皮膚：貼身衣物與童裝的背面若留著硬邊或粗糙的撕裂殘邊，穿十分鐘就會癢。三件事分別由「支撐力、尺寸穩定性、邊緣處理」負責，這就是選襯紙的三個參數。",
        "en": "First, it carries the stitches. Embroidery drives thousands of high-tension stitches into cloth, and without a backing underneath, the cloth stretches and the design pulls in at both sides. Second, it suppresses puckering: the denser the stitching and the lighter the fabric, the firmer the support surface needed, otherwise you get a ripple after the first wash. Third, it protects skin: on intimate apparel and childrenswear, a hard edge or a rough torn residue at the back will itch within ten minutes. Those three jobs map onto three selection parameters: support, dimensional stability and edge treatment.",
        "fr": "Premièrement, il porte les points. La broderie enfonce des milliers de points très tendus dans le tissu ; sans support, le tissu s'allonge et le motif se resserre sur les côtés. Deuxièmement, il limite le gondolement : plus la broderie est dense et le tissu léger, plus la surface d'appui doit être ferme, sinon une vague apparaît dès le premier lavage. Troisièmement, il protège la peau : sur la lingerie et le prêt-à-porter enfant, un bord dur ou un reste d'arrachage rêche gratte en dix minutes. Ces trois fonctions correspondent à trois paramètres : maintien, stabilité dimensionnelle et traitement du bord.",
        "es": "Primero, soporta las puntadas. El bordado introduce miles de puntadas de alta tensión en la tela; sin entretela debajo, la tela se estira y el motivo se frunce a ambos lados. Segundo, frena el ondulado: cuanto más densa es la puntada y más ligera la tela, más firme debe ser la superficie de apoyo, o aparece una onda tras el primer lavado. Tercero, protege la piel: en lencería y ropa infantil, un borde duro o un resto de desgarro áspero por el revés pica en diez minutos. Esas tres funciones se traducen en tres parámetros: soporte, estabilidad dimensional y tratamiento del borde.",
        "ja": "第一に針跡を支えること。刺繍は高張力の針を何千針も布に打ち込むため、裏地がないと布が伸び、柄の両側がつります。第二に波打ちの抑制です。針数が密で生地が薄いほど硬い支持面が必要で、不足すると初回の洗濯で波打ちます。第三に肌の保護。インナーや子供服では、裏側に硬い端やティアアウェイの粗い残りがあると 10 分でチクチクします。この 3 つは「支持力・寸法安定性・端の処理」という 3 つの選定パラメータに対応します。",
        "ko": "첫째, 바늘땀을 지지합니다. 자수는 고장력 바늘땀을 수천 개 원단에 밀어 넣기 때문에 받침지가 없으면 원단이 늘어나고 무늬 양쪽이 당깁니다. 둘째, 물결을 억제합니다. 바늘 수가 촘촘하고 원단이 얇을수록 단단한 지지면이 필요하며, 부족하면 첫 세탁 후 물결이 생깁니다. 셋째, 피부를 보호합니다. 속옷과 아동복은 안쪽에 딱딱한 끝단이나 거친 티어어테이 잔여물이 남으면 10분 만에 따갑습니다. 이 세 역할은 지지력, 치수 안정성, 끝단 처리라는 세 가지 선정 변수로 이어집니다.",
    }),

    ("h2", {
        "zh": "二、四種襯紙，四種失效方式",
        "en": "2. Four Backing Families, Four Ways to Fail",
        "fr": "2. Quatre familles de supports, quatre modes de défaillance",
        "es": "2. Cuatro familias de entretela, cuatro formas de fallar",
        "ja": "2. 4 種類の裏地、4 つの失敗の仕方",
        "ko": "2. 네 가지 받침지, 네 가지 실패 방식",
    }),

    ("ul", [
        {
            "zh": "切邊襯（cutaway）：最穩，洗後不易變形，代價是洗完仍留在衣服裡，成品較厚。適合針數 8,000 以上、需要反覆洗滌的圖案（胸前大圖、背部主圖）。",
            "en": "Cutaway: the most stable and the least likely to distort after washing, at the cost of staying in the garment, which makes the finished piece thicker. Right for designs above 8,000 stitches that will be washed repeatedly, such as a large chest or back panel.",
            "fr": "Découpe (cutaway) : le plus stable, le moins sujet à la déformation après lavage, au prix d'un maintien dans le vêtement qui épaissit le rendu. Indiqué au-delà de 8 000 points et pour les motifs lavés souvent, grands panneaux poitrine ou dos.",
            "es": "Recortable (cutaway): la más estable y la que menos se deforma tras el lavado, a cambio de quedarse en la prenda y engrosar el resultado. Adecuada por encima de 8.000 puntadas y en motivos de lavado frecuente, como un panel grande de pecho o espalda.",
            "ja": "カットアウェイ：最も安定し、洗濯後の変形が少ない反面、製品内に残るため厚みが出ます。8,000 針以上、洗濯回数の多い柄（胸・背中の大きな図案）に向きます。",
            "ko": "컷어테이: 가장 안정적이고 세탁 후 변형이 적지만 제품 안에 남아 두께가 늘어납니다. 8,000바늘 이상, 세탁이 잦은 큰 무늬(가슴·등판)에 적합합니다.",
        },
        {
            "zh": "撕裂襯（tearaway）：成品輕、手感好，代價是邊緣有殘邊，支撐力比切邊襯低約三成。適合 3,000–8,000 針的裝飾小圖，以及洗滌要求不高的款式。",
            "en": "Tearaway: light finished hand feel, at the cost of a residual edge and roughly thirty per cent less support than cutaway. Right for decorative marks of 3,000 to 8,000 stitches and for garments with modest wash requirements.",
            "fr": "Arrachage (tearaway) : rendu léger, au prix d'un bord résiduel et d'environ 30 % de maintien en moins que la découpe. Indiqué pour les petites marques décoratives de 3 000 à 8 000 points et les pièces peu lavées.",
            "es": "Desgarrable (tearaway): tacto ligero, a cambio de un borde residual y un 30 % menos de soporte que la recortable. Adecuada para marcas decorativas de 3.000 a 8.000 puntadas y prendas de lavado moderado.",
            "ja": "ティアアウェイ：仕上がりが軽く風合いが良い反面、端に残りが出て、カットアウェイより支持力が約 3 割低くなります。3,000〜8,000 針の装飾マークや洗濯条件が緩い用途に向きます。",
            "ko": "티어어테이: 완성 촉감이 가볍지만 끝단 잔여물이 남고 컷어테이보다 지지력이 약 30% 낮습니다. 3,000~8,000바늘 장식 마크와 세탁 조건이 완만한 제품에 적합합니다.",
        },
        {
            "zh": "水溶襯（wash-away）：刺繡時做支撐，遇水完全消失，適合鏤空刺繡、薄紗、蕾絲與需要完全透明的部位；不耐長時間浸洗的布料要縮短時間。",
            "en": "Wash-away: supports during stitching and disappears completely in water, which is what openwork embroidery, tulle, lace and any area that must stay fully transparent need. On fabrics that cannot take a long soak, shorten the dwell time.",
            "fr": "Soluble (wash-away) : soutient pendant la broderie et disparaît totalement à l'eau, indispensable aux broderies ajourées, au tulle, à la dentelle et à toute zone qui doit rester transparente. Sur les tissus qui supportent mal le trempage, réduisez le temps.",
            "es": "Soluble (wash-away): sostiene durante el bordado y desaparece por completo en agua, imprescindible en bordado calado, tul, encaje y cualquier zona que deba quedar transparente. En tejidos que no aguantan remojo, acorte el tiempo.",
            "ja": "水溶性（ウォッシュアウェイ）：刺繍中は支え、水で完全に消えます。透かし刺繍、チュール、レース、透明感を保つ必要がある部位に不可欠です。長時間の浸漬に耐えない生地では時間を短縮します。",
            "ko": "수용성(워시어웨이): 자수 중에는 지지하고 물에서 완전히 사라집니다. 개방 자수, 튤, 레이스, 투명도를 유지해야 하는 부위에 필수입니다. 장시간 침수를 견디지 못하는 원단은 시간을 줄이십시오.",
        },
        {
            "zh": "熱熔襯（fusible / heat-away）：用熨斗貼合，適合小面積標誌與難固定的彈性布料，但貼合溫度與壓力沒控好就會留下亮痕或使布面硬化，返工幾乎不可能。",
            "en": "Fusible or heat-away: bonded with an iron, useful for small logos and for elastic fabrics that are hard to hoop, but if bonding temperature and pressure are not controlled it leaves a shine or stiffens the face, and rework is almost impossible.",
            "fr": "Thermocollant (fusible) : collé au fer, utile pour les petits logos et les tissus élastiques difficiles à tender, mais sans maîtrise de la température et de la pression il laisse un lustre ou durcit l'endroit, et la reprise est presque impossible.",
            "es": "Termoadhesiva (fusible): se fija con plancha, útil para logos pequeños y tejidos elásticos difíciles de tensar, pero sin control de temperatura y presión deja brillo o endurece el derecho, y la recuperación es casi imposible.",
            "ja": "接着（ヒートアウェイ）：アイロンで貼り、小さなロゴや枠張りしにくい伸縮素材に向きますが、温度と圧力を管理しないとテカリや硬化が残り、やり直しはほぼ不可能です。",
            "ko": "접착형(퓨저블): 다리미로 부착하며 작은 로고와 고정이 어려운 신축성 원단에 유용하지만, 온도와 압력을 제어하지 않으면 광택이나 경화가 남고 재작업이 거의 불가능합니다.",
        },
    ]),

    ("p", {
        "zh": "毛巾布、毛圈布、刷毛布這類有絨毛的面料還要加一層貼面薄膜（topping film），厚度常見 25–40 μm。沒有這層膜，絨毛會從針跡之間冒出來，圖案邊緣毛躁，遠看像糊掉。貼面膜是消耗品，不要為了省它而在這類布料上硬做。",
        "en": "Loop fabrics such as terry, fleece and brushed knits also need a topping film, commonly 25 to 40 micrometres thick. Without it, the pile pushes up between the stitches, the edge of the design looks fuzzy and at a distance the whole mark smears. The topping is a consumable; do not skip it to save cost on these fabrics.",
        "fr": "Les tissus bouclés type éponge, molleton ou maille grattée exigent en plus un film de dessus, généralement de 25 à 40 micromètres. Sans lui, les boucles remontent entre les points, le bord du motif devient flou et, à distance, la marque se brouille. C'est un consommable : ne l'économisez pas sur ces tissus.",
        "es": "Los tejidos con bucle como rizo, fleece o punto perchado necesitan además un film superior, de 25 a 40 micrómetros. Sin él, el bucle asoma entre las puntadas, el borde del motivo queda difuso y a distancia la marca se emborrona. Es un consumible: no lo ahorre en estos tejidos.",
        "ja": "パイル地（タオル、フリース、起毛ニット）には上面フィルム（トッピング）が別途必要で、厚みは 25〜40 µm が一般的です。これがないとパイルが針目の間から出て、柄の輪郭がぼやけ、離れて見ると全体がにじみます。消耗品なので、この素材で省略してはいけません。",
        "ko": "테리, 플리스, 기모 니트 같은 파일 원단에는 상면 필름(토핑)이 추가로 필요하며 두께는 보통 25~40 µm입니다. 이것이 없으면 파일이 바늘땀 사이로 솟아 무늬 윤곽이 흐려지고 멀리서 보면 번져 보입니다. 소모품이므로 이 원단에서 생략하면 안 됩니다.",
    }),

    ("h2", {
        "zh": "三、克重與針數要對得上",
        "en": "3. Match the Weight to the Stitch Count",
        "fr": "3. Accorder le grammage au nombre de points",
        "es": "3. Ajustar el gramaje al número de puntadas",
        "ja": "3. 目付と針数を対応させる",
        "ko": "3. 평량과 바늘 수를 맞추십시오",
    }),

    ("table", {
        "head": [
            {"zh": "針數", "en": "Stitch count", "fr": "Nombre de points", "es": "Número de puntadas", "ja": "針数", "ko": "바늘 수"},
            {"zh": "襯紙類型", "en": "Backing type", "fr": "Type de support", "es": "Tipo de entretela", "ja": "裏地の種類", "ko": "받침지 종류"},
            {"zh": "克重參考", "en": "Weight guide", "fr": "Grammage indicatif", "es": "Gramaje orientativo", "ja": "目付の目安", "ko": "평량 기준"},
            {"zh": "常見失效", "en": "Typical failure", "fr": "Défaut typique", "es": "Fallo típico", "ja": "よくある不具合", "ko": "흔한 문제"},
        ],
        "rows": [
            [
                {"zh": "3,000 以下", "en": "Under 3,000", "fr": "Moins de 3 000", "es": "Menos de 3.000", "ja": "3,000 未満", "ko": "3,000 미만"},
                {"zh": "撕裂襯或水溶襯", "en": "Tearaway or wash-away", "fr": "Arrachage ou soluble", "es": "Desgarrable o soluble", "ja": "ティアアウェイまたは水溶性", "ko": "티어어테이 또는 수용성"},
                {"zh": "40–50 g/m²", "en": "40 to 50 g/m²", "fr": "40 à 50 g/m²", "es": "40 a 50 g/m²", "ja": "40〜50 g/m²", "ko": "40~50 g/m²"},
                {"zh": "不需支撐，布料被拉長", "en": "No support, cloth stretches", "fr": "Pas de maintien, tissu étiré", "es": "Sin soporte, tela estirada", "ja": "支持不足で布が伸びる", "ko": "지지 부족으로 원단 늘어남"},
            ],
            [
                {"zh": "3,000–8,000", "en": "3,000 to 8,000", "fr": "3 000 à 8 000", "es": "3.000 a 8.000", "ja": "3,000〜8,000", "ko": "3,000~8,000"},
                {"zh": "撕裂襯（雙層可加硬）", "en": "Tearaway, doubled if needed", "fr": "Arrachage, doublé si besoin", "es": "Desgarrable, doble si hace falta", "ja": "ティアアウェイ（必要なら二枚重ね）", "ko": "티어어테이(필요 시 2장)"},
                {"zh": "50–65 g/m²", "en": "50 to 65 g/m²", "fr": "50 à 65 g/m²", "es": "50 a 65 g/m²", "ja": "50〜65 g/m²", "ko": "50~65 g/m²"},
                {"zh": "四角起皺", "en": "Corner puckering", "fr": "Gondolement aux angles", "es": "Ondulado en las esquinas", "ja": "四隅の波打ち", "ko": "모서리 물결"},
            ],
            [
                {"zh": "8,000–15,000", "en": "8,000 to 15,000", "fr": "8 000 à 15 000", "es": "8.000 a 15.000", "ja": "8,000〜15,000", "ko": "8,000~15,000"},
                {"zh": "切邊襯", "en": "Cutaway", "fr": "Découpe", "es": "Recortable", "ja": "カットアウェイ", "ko": "컷어테이"},
                {"zh": "65–80 g/m²", "en": "65 to 80 g/m²", "fr": "65 à 80 g/m²", "es": "65 a 80 g/m²", "ja": "65〜80 g/m²", "ko": "65~80 g/m²"},
                {"zh": "洗後邊緣捲曲", "en": "Edge curl after washing", "fr": "Bord roulotté après lavage", "es": "Borde enrollado tras lavar", "ja": "洗濯後の端の巻き", "ko": "세탁 후 끝단 말림"},
            ],
            [
                {"zh": "15,000 以上", "en": "Above 15,000", "fr": "Plus de 15 000", "es": "Más de 15.000", "ja": "15,000 超", "ko": "15,000 초과"},
                {"zh": "切邊襯雙層", "en": "Cutaway, doubled", "fr": "Découpe doublée", "es": "Recortable doble", "ja": "カットアウェイ二枚重ね", "ko": "컷어테이 2장"},
                {"zh": "80 g/m² 以上", "en": "80 g/m² and up", "fr": "80 g/m² et plus", "es": "80 g/m² o más", "ja": "80 g/m² 以上", "ko": "80 g/m² 이상"},
                {"zh": "圖案整體收縮", "en": "Whole design contracts", "fr": "Motif qui se rétracte", "es": "El motivo se contrae", "ja": "柄全体の収縮", "ko": "무늬 전체 수축"},
            ],
        ],
    }),

    ("h2", {
        "zh": "四、合規線：甲醛、纖維標示與兒童安全",
        "en": "4. The Compliance Line: Formaldehyde, Fibre Labelling, Children",
        "fr": "4. La ligne réglementaire : formaldéhyde, étiquetage, enfants",
        "es": "4. La línea normativa: formaldehído, etiquetado, infantil",
        "ja": "4. 合规ライン：ホルムアルデヒド・組成表示・子供安全",
        "ko": "4. 규제선: 포름알데히드·혼용률 표시·어린이 안전",
    }),

    ("p", {
        "zh": "襯紙是化學品，不是布。多數切邊與撕裂襯用甲醛系樹脂做硬挺處理，歐盟 REACH 法規（EC）1907/2006 附件 XVII 第 72 項對紡織品甲醛設了三級限值：一般貼膚類 75 mg/kg、外套類 300 mg/kg、三歲以下嬰幼兒用品 30 mg/kg。選襯紙時要供應商直接給這組數據的測試報告，而不是給一張「環保」聲明。OEKO-TEX Standard 100 的嬰兒級（Product Class I）是業界最常被引用的可查證憑證。",
        "en": "Backing is a chemical product, not just cloth. Most cutaway and tearaway backings are stiffened with formaldehyde-based resins, and REACH (EC) 1907/2006, Annex XVII, entry 72 sets three formaldehyde limits for textiles: 75 mg/kg for products in direct skin contact, 300 mg/kg for jackets and coats, and 30 mg/kg for articles for children under three. Ask the supplier for a test report carrying those numbers, not a statement that the material is eco-friendly. OEKO-TEX Standard 100 Product Class I for baby articles is the most widely accepted verifiable certificate in the trade.",
        "fr": "Un support est un produit chimique autant qu'un textile. La plupart des supports découpe et arrachage sont rigidifiés par des résines à base de formaldéhyde, et le règlement REACH (CE) 1907/2006, annexe XVII, entrée 72 fixe trois limites pour les textiles : 75 mg/kg pour les articles en contact direct avec la peau, 300 mg/kg pour les vestes et manteaux, 30 mg/kg pour les articles destinés aux enfants de moins de trois ans. Demandez un rapport d'essai portant ces valeurs, pas une déclaration d'innocuité. L'OEKO-TEX Standard 100 classe I, pour articles pour bébés, est le certificat vérifiable le plus admis du secteur.",
        "es": "La entretela es un producto químico además de un textil. La mayoría de las entretelas recortables y desgarrables se rigidizan con resinas de formaldehído, y el Reglamento REACH (CE) 1907/2006, anexo XVII, entrada 72 fija tres límites para textiles: 75 mg/kg en artículos de contacto directo con la piel, 300 mg/kg en chaquetas y abrigos, y 30 mg/kg en artículos para menores de tres años. Pida un informe de ensayo con esas cifras, no una declaración de que el material es ecológico. El OEKO-TEX Standard 100 clase I para artículos de bebé es el certificado verificable más aceptado del sector.",
        "ja": "裏地は布であると同時に化学品です。カットアウェイやティアアウェイの多くはホルムアルデヒド系樹脂で硬さを出しており、EU の REACH 規則 (EC) 1907/2006 附属書 XVII 第 72 項は繊維製品のホルムアルデヒドに 3 段階の限度を定めています。直接皮膚に触れる製品は 75 mg/kg、ジャケット・コート類は 300 mg/kg、3 歳未満の子供向けは 30 mg/kg です。エコ声明ではなく、この数値を載せた試験報告書を求めましょう。業界で最も通用する検証可能な証明は、OEKO-TEX Standard 100 の製品分類 I（ベビー用品）です。",
        "ko": "받침지는 원단이면서 화학 제품입니다. 컷어테이와 티어어테이 대부분은 포름알데히드계 수지로 형태를 잡으며, EU REACH 규정 (EC) 1907/2006 부속서 XVII 제72항은 섬유 제품 포름알데히드에 세 단계 한도를 둡니다. 피부에 직접 닿는 제품 75 mg/kg, 재킷·코트류 300 mg/kg, 만 3세 미만 아동용 30 mg/kg입니다. 친환경이라는 선언문이 아니라 이 수치가 담긴 시험 성적서를 요구하십시오. 업계에서 가장 통용되는 검증 가능한 증빙은 OEKO-TEX Standard 100 제품 분류 I(유아용)입니다.",
    }),

    ("p", {
        "zh": "纖維成分標示同樣要處理。依歐盟法規（EU）No 1007/2011，標籤上的纖維成分以布料主體計算，裝飾性刺繡線與裁切後留下的襯布屬於輔助材料，一般不列入百分比，但買家的技術文件（tech pack）應註明襯紙材質與克重——這既是溯源資料，也是洗滌符號（依 EN ISO 3758）選擇的依據：留著切邊襯的圖案，洗滌溫度與烘乾方式要按襯紙而不是按布料設定，否則襯紙先收縮，圖案就起皺。",
        "en": "Fibre labelling needs handling too. Under (EU) No 1007/2011 the fibre composition on the label is calculated on the main fabric; decorative embroidery thread and backing left after cutting count as ancillary materials and normally stay out of the percentages. The buyer's tech pack should still record the backing material and weight, both as traceability data and as the basis for choosing care symbols under EN ISO 3758: a panel that keeps its cutaway has to be washed and dried to the backing's limits, not the shell fabric's, or the backing shrinks first and the design puckers.",
        "fr": "L'étiquetage de composition demande aussi un arbitrage. Selon le règlement (UE) n° 1007/2011, la composition indiquée est calculée sur le tissu principal ; le fil de broderie décoratif et le support restant après découpe sont des matières accessoires et n'entrent normalement pas dans les pourcentages. Le dossier technique de l'acheteur doit néanmoins consigner matière et grammage du support : c'est une donnée de traçabilité et la base du choix des symboles d'entretien selon EN ISO 3758. Un panneau qui conserve sa découpe se lave et se sèche selon les limites du support, pas celles du tissu, sinon le support rétrécit en premier et le motif gondole. Ajoutez les mentions obligatoires d'entretien sur l'étiquette et non seulement dans la fiche produit.",
        "es": "El etiquetado de composición también exige criterio. Según el Reglamento (UE) n.º 1007/2011, la composición de la etiqueta se calcula sobre el tejido principal; el hilo de bordado decorativo y la entretela que queda tras el recorte son materiales auxiliares y normalmente no entran en los porcentajes. Aun así, la ficha técnica del comprador debe registrar material y gramaje de la entretela: es dato de trazabilidad y base para elegir los símbolos de cuidado según EN ISO 3758. Un panel que conserva su recortable se lava y seca según los límites de la entretela, no de la tela, o la entretela encoge primero y el motivo ondula. La información obligatoria de cuidado va en la etiqueta, no solo en la ficha de producto.",
        "ja": "組成表示も整理が必要です。EU 規則 (EU) No 1007/2011 では、表示する混用率は身頃の主素材で計算し、装飾用の刺繍糸や裁断後に残る裏地は付属材料として通常は百分比に含めません。ただし購買側の仕様書（テックパック）には裏地の材質と目付を記載してください。トレーサビリティの資料であり、EN ISO 3758 に基づく洗濯表示を選ぶ根拠でもあります。カットアウェイを残した図案は、表地ではなく裏地の限界に合わせて洗濯・乾燥しないと、裏地が先に縮んで柄が波打ちます。日本では家庭用品品質表示法により、組成（混用率）と取扱表示を製品のラベルに日本語で示す義務があるため、裏地の耐洗性は表示した洗濯方法で確認してください。",
        "ko": "혼용률 표시도 정리가 필요합니다. EU 규정 (EU) No 1007/2011에 따르면 라벨의 섬유 조성은 본체 원단을 기준으로 계산하며, 장식용 자수사와 재단 후 남는 받침지는 부자재로 보아 보통 백분율에 넣지 않습니다. 그래도 구매처의 테크팩에는 받침지 재질과 평량을 기록해야 합니다. 추적성 자료이자 EN ISO 3758에 따른 취급 표시를 고르는 근거입니다. 컷어테이를 남긴 무늬는 겉감이 아니라 받침지 한도에 맞춰 세탁·건조해야 하며, 그렇지 않으면 받침지가 먼저 줄어 무늬가 물결칩니다. 한국에서는 품질경영 및 공산품 안전관리법에 따라 혼용률과 취급 표시를 제품에 표시해야 하므로, 받침지의 내세탁성은 표시된 세탁 방법으로 검증하십시오.",
    }),

    ("h2", {
        "zh": "五、車間參數：針、密度、速度",
        "en": "5. Shop Floor Parameters: Needle, Density, Speed",
        "fr": "5. Paramètres d'atelier : aiguille, densité, vitesse",
        "es": "5. Parámetros de taller: aguja, densidad, velocidad",
        "ja": "5. 現場パラメータ：針・密度・速度",
        "ko": "5. 현장 파라미터: 바늘·밀도·속도",
    }),

    ("p", {
        "zh": "針織布與薄料用 70/10 或 75/11 圓頭針，避免切斷紗線造成破洞；梭織布可用 80/12 尖頭針。密度以每公分針數計，一般圖案 5–7 針/公分，細線條 6–8 針/公分；密度加一級，襯紙也要加一級，兩者不能只調一項。針織布轉速建議 700–850 針/分鐘，梭織可到 850–1,000；轉速過高時針的衝擊力把布料往下壓，襯紙支撐不足就會出現針孔周圍的「釘孔圈」。",
        "en": "Use a 70/10 or 75/11 ballpoint needle on knits and lightweight fabrics so the yarns are pushed apart rather than cut; a 80/12 sharp works on wovens. Density is measured in stitches per centimetre, typically 5 to 7 for solid fills and 6 to 8 for fine outlines. Raise the density by one step and the backing must go up one step as well; adjusting only one of the two is where trouble starts. Run knits at 700 to 850 stitches per minute and wovens up to 850 to 1,000. Push the speed higher and the needle impact drives the fabric down; with insufficient backing you get a ring of needle holes around the mark.",
        "fr": "Sur maille et tissus légers, utilisez une aiguille à pointe boule 70/10 ou 75/11 pour écarter les fils au lieu de les couper ; le 80/12 pointu convient aux tissés. La densité se compte en points par centimètre : 5 à 7 pour les aplats, 6 à 8 pour les contours fins. Montez la densité d'un cran et le support doit monter d'un cran aussi : n'ajuster qu'un seul des deux est la source des défauts. Réglez la maille à 700-850 points par minute, le tissé jusqu'à 850-1 000. Au-delà, l'impact de l'aiguille enfonce le tissu et, si le support est insuffisant, un cerne de trous apparaît autour du motif.",
        "es": "En punto y tejidos ligeros use aguja de punta bola 70/10 o 75/11 para separar los hilos en lugar de cortarlos; la 80/12 de punta afilada sirve para tejidos planos. La densidad se cuenta en puntadas por centímetro: 5 a 7 en rellenos y 6 a 8 en contornos finos. Suba la densidad un paso y la entretela debe subir otro; ajustar solo uno de los dos es el origen del problema. En punto, 700 a 850 puntadas por minuto; en plano, hasta 850 a 1.000. Si acelera más, el impacto de la aguja hunde la tela y, con entretela insuficiente, aparece un cerco de agujeros alrededor del motivo.",
        "ja": "ニットや薄地には 70/10 または 75/11 の丸針を使い、糸を切らずに押し分けます。織物には 80/12 の先針で構いません。密度は 1 cm あたりの針数で、塗り面は 5〜7 針/cm、細い輪郭は 6〜8 針/cm が目安です。密度を 1 段上げたら裏地も 1 段上げる必要があり、片方だけ変えると不具合になります。ニットは 700〜850 針/分、織物は 850〜1,000 針/分。これ以上速くすると針の衝撃で生地が沈み、裏地が不足していると柄の周囲に針穴の輪ができます。",
        "ko": "니트와 얇은 원단에는 70/10 또는 75/11 볼포인트 바늘을 사용해 실을 끊지 않고 밀어냅니다. 직물에는 80/12 예침이 맞습니다. 밀도는 1 cm당 바늘 수로, 채움은 5~7, 가는 윤곽은 6~8이 기준입니다. 밀도를 한 단계 올리면 받침지도 한 단계 올려야 하며, 한쪽만 바꾸면 문제가 생깁니다. 니트는 분당 700~850바늘, 직물은 850~1,000바늘입니다. 더 빠르게 하면 바늘 충격으로 원단이 눌리고, 받침지가 부족하면 무늬 주위에 바늘 구멍 고리가 생깁니다.",
    }),

    ("h2", {
        "zh": "六、驗收：五個可以量的數字",
        "en": "6. Acceptance: Five Numbers You Can Measure",
        "fr": "6. Réception : cinq chiffres mesurables",
        "es": "6. Aceptación: cinco cifras medibles",
        "ja": "6. 検収：測定できる 5 つの数値",
        "ko": "6. 검수: 측정 가능한 다섯 수치",
    }),

    ("table", {
        "head": [
            {"zh": "項目", "en": "Item", "fr": "Élément", "es": "Elemento", "ja": "項目", "ko": "항목"},
            {"zh": "要求", "en": "Requirement", "fr": "Exigence", "es": "Requisito", "ja": "要求", "ko": "요구 사항"},
            {"zh": "怎麼驗", "en": "How to verify", "fr": "Vérification", "es": "Verificación", "ja": "確認方法", "ko": "확인 방법"},
        ],
        "rows": [
            [
                {"zh": "洗後尺寸變化", "en": "Shrinkage after wash", "fr": "Retrait après lavage", "es": "Encogimiento tras lavado", "ja": "洗濯後の寸法変化", "ko": "세탁 후 치수 변화"},
                {"zh": "圖案長寬變化 ≤ 2 mm", "en": "Design dimension change 2 mm or less", "fr": "Variation du motif ≤ 2 mm", "es": "Variación del motivo ≤ 2 mm", "ja": "柄の縦横変化 2 mm 以下", "ko": "무늬 가로·세로 변화 2 mm 이하"},
                {"zh": "40 °C 洗 3 次、平放乾燥後量測", "en": "Wash three times at 40 °C, dry flat and measure", "fr": "Trois lavages à 40 °C, séchage à plat puis mesure", "es": "Tres lavados a 40 °C, secado en plano y medición", "ja": "40 °C で 3 回洗濯、平干し後に測定", "ko": "40 °C에서 3회 세탁, 평건조 후 측정"},
            ],
            [
                {"zh": "起皺", "en": "Puckering", "fr": "Gondolement", "es": "Ondulado", "ja": "波打ち", "ko": "물결"},
                {"zh": "圖案四周無波浪，邊緣不起翹", "en": "No wave around the mark, no lifted edge", "fr": "Aucune vague autour du motif, bord non relevé", "es": "Sin onda alrededor, borde sin levantar", "ja": "柄周囲に波がなく、端が浮かない", "ko": "무늬 주위 물결 없음, 끝단 들뜸 없음"},
                {"zh": "熨燙後目視 + 側光拍照留檔", "en": "Visual check after pressing, photograph under raking light", "fr": "Contrôle visuel après repassage, photo en lumière rasante", "es": "Revisión visual tras planchar, foto con luz rasante", "ja": "プレス後の目視と斜光での撮影記録", "ko": "프레스 후 육안 확인 및 사광 촬영 기록"},
            ],
            [
                {"zh": "殘邊手感", "en": "Residual edge feel", "fr": "Toucher du bord résiduel", "es": "Tacto del borde residual", "ja": "残りの端の肌触り", "ko": "잔여 끝단 촉감"},
                {"zh": "貼膚面無硬邊，殘邊 ≤ 1 mm 且已壓平", "en": "No hard edge on the skin side, residue 1 mm or less and flattened", "fr": "Aucun bord dur côté peau, résidu ≤ 1 mm aplati", "es": "Sin borde duro en el lado piel, residuo ≤ 1 mm aplanado", "ja": "肌側に硬い端がなく、残り 1 mm 以下で押さえられている", "ko": "피부 쪽 딱딱한 끝단 없음, 잔여 1 mm 이하로 눌림"},
                {"zh": "手背沿邊滑過三遍，同一件由兩人各驗一次", "en": "Slide the back of a hand along the edge three times; two inspectors per piece", "fr": "Passer le dos de la main trois fois sur le bord ; deux contrôleurs par pièce", "es": "Pasar el dorso de la mano tres veces por el borde; dos inspectores por pieza", "ja": "手の甲で端を 3 回なぞり、1 枚を 2 名で確認", "ko": "손등으로 끝단을 3회 쓸어보고 1장당 2명이 확인"},
            ],
            [
                {"zh": "甲醛", "en": "Formaldehyde", "fr": "Formaldéhyde", "es": "Formaldehído", "ja": "ホルムアルデヒド", "ko": "포름알데히드"},
                {"zh": "貼膚類 ≤ 75 mg/kg，嬰幼兒 ≤ 30 mg/kg", "en": "75 mg/kg or less for skin contact, 30 mg/kg or less for infants", "fr": "≤ 75 mg/kg en contact peau, ≤ 30 mg/kg pour le bébé", "es": "≤ 75 mg/kg en contacto con piel, ≤ 30 mg/kg en bebé", "ja": "肌着類 75 mg/kg 以下、乳幼児 30 mg/kg 以下", "ko": "피부 접촉 75 mg/kg 이하, 유아 30 mg/kg 이하"},
                {"zh": "第三方報告（EN ISO 14184 方法）", "en": "Third-party report using an EN ISO 14184 method", "fr": "Rapport tiers selon une méthode EN ISO 14184", "es": "Informe de tercero con método EN ISO 14184", "ja": "第三者報告書（EN ISO 14184 法）", "ko": "제3자 성적서(EN ISO 14184 방법)"},
            ],
            [
                {"zh": "剝離與毛邊", "en": "Fraying and lift", "fr": "Effilochage et décollement", "es": "Deshilachado y despegue", "ja": "ほつれ・浮き", "ko": "올 풀림·들뜸"},
                {"zh": "邊緣無毛邊，襯紙不與布面分離", "en": "No fray at the edge, backing does not separate from the cloth", "fr": "Pas d'effilochage, support non décollé", "es": "Sin hilos sueltos, entretela sin despegarse", "ja": "端にほつれがなく、裏地が布から浮かない", "ko": "끝단 올 없음, 받침지가 원단에서 분리되지 않음"},
                {"zh": "每批抽 10 件，用 500 g 砝碼掛邊 30 秒", "en": "Ten pieces per lot, hang a 500 g weight on the edge for 30 seconds", "fr": "Dix pièces par lot, suspendre 500 g sur le bord 30 s", "es": "Diez piezas por lote, colgar 500 g del borde 30 s", "ja": "ロットごと 10 枚、端に 500 g の錘を 30 秒", "ko": "로트당 10장, 끝단에 500 g 추를 30초"},
            ],
        ],
    }),

    ("callout", {
        "zh": "選襯紙的三個判斷：針數定類型（≤8,000 撕裂、>8,000 切邊）、絨毛面料必加貼面膜、貼膚件甲醛按 75/30 mg/kg 兩級要求並要測試報告。",
        "en": "Three tests for backing selection: stitch count sets the family (tearaway up to 8,000, cutaway above), loop fabrics always get a topping film, and skin-contact pieces need 75 or 30 mg/kg formaldehyde with a test report to match.",
        "fr": "Trois réflexes de choix : le nombre de points fixe la famille (arrachage jusqu'à 8 000, découpe au-delà), les tissus bouclés exigent un film de dessus, et les pièces en contact peau demandent 75 ou 30 mg/kg de formaldéhyde avec rapport à l'appui.",
        "es": "Tres criterios de elección: el número de puntadas define la familia (desgarrable hasta 8.000, recortable por encima), los tejidos con bucle siempre llevan film superior y las piezas en contacto con la piel exigen 75 o 30 mg/kg de formaldehído con informe.",
        "ja": "裏地選定の 3 つの判断：針数で種類を決め（8,000 以下はティアアウェイ、超えるならカットアウェイ）、パイル地は上面フィルム必須、肌に触れる製品はホルムアルデヒド 75／30 mg/kg の二段階で試験報告書を求める。",
        "ko": "받침지 선택의 세 가지 판단: 바늘 수가 종류를 정하고(8,000 이하는 티어어테이, 초과는 컷어테이), 파일 원단은 상면 필름이 필수이며, 피부 접촉 제품은 포름알데히드 75/30 mg/kg 두 단계로 시험 성적서를 요구합니다.",
    }),

    ("p", {
        "zh": "把襯紙寫進技術文件之後，刺繡就從「打樣看效果」變成可複製的工序：同一款補單、換廠、換批，只要襯紙類型、克重與上面五個數字不變，圖案就不會無故變形。這也是為什麼我們在報價單上把襯紙單獨列一行——它最便宜，也最不該被省。",
        "en": "Once the backing is written into the tech pack, embroidery stops being a matter of judging a sample by eye and becomes a reproducible process. On a repeat order, at a different plant or from a different lot, as long as the backing family, weight and those five numbers stay the same, the design will not drift. That is why we list the backing as its own line on the quotation: it is the cheapest item and the last one that should be trimmed.",
        "fr": "Une fois le support inscrit au dossier technique, la broderie cesse de se juger à l'oeil sur un échantillon pour devenir un procédé reproductible. En réassort, dans un autre atelier ou sur un autre lot, tant que la famille, le grammage et ces cinq valeurs restent identiques, le motif ne dérive pas. C'est pourquoi le support figure sur une ligne distincte du devis : c'est le poste le moins cher et le dernier qu'il faut rogner.",
        "es": "Cuando la entretela queda en la ficha técnica, el bordado deja de juzgarse a ojo sobre una muestra y pasa a ser un proceso reproducible. En una reposición, en otra planta o con otro lote, mientras se mantengan la familia, el gramaje y esas cinco cifras, el motivo no se mueve. Por eso figura como línea propia en el presupuesto: es el artículo más barato y el último que conviene recortar.",
        "ja": "裏地を仕様書に書き込めば、刺繍は「サンプルを目で見る」工程から再現できる工程になります。追加発注でも、別工場でも、別ロットでも、裏地の種類・目付・この 5 つの数値が同じなら柄は狂いません。見積書で裏地を独立した行にしているのは、最も安い項目であり、最も削ってはいけない項目だからです。",
        "ko": "받침지를 테크팩에 기록하면 자수는 샘플을 눈으로 보는 공정에서 재현 가능한 공정이 됩니다. 재주문, 다른 공장, 다른 로트에서도 받침지 종류와 평량, 이 다섯 수치가 같으면 무늬는 흐트러지지 않습니다. 견적서에서 받침지를 별도 항목으로 두는 이유는 가장 저렴한 항목이자 가장 줄여서는 안 되는 항목이기 때문입니다.",
    }),
]

RELATED = [
    {"slug": "garment-embroidery-decoration-guide.html",
     "zh": "服裝刺繡裝飾：工藝選型與驗收", "en": "Garment embroidery: process selection and acceptance",
     "fr": "Broderie sur vêtement : procédés et réception", "es": "Bordado en prenda: procesos y aceptación",
     "ja": "衣料の刺繍加飾：工法選定と検収", "ko": "의류 자수 장식: 공정 선택과 검수"},
    {"slug": "tshirt-hoodie-trims-guide.html",
     "zh": "T 恤與衛衣輔料：領口、羅紋與刺繡位置", "en": "T-shirt and hoodie trims: neck, rib and embroidery placement",
     "fr": "Accessoires de t-shirt et sweat : col, bord-côte, placement", "es": "Accesorios de camiseta y sudadera: cuello, canalé, colocación",
     "ja": "Tシャツ・パーカーの資材：襟・リブ・刺繍位置", "ko": "티셔츠·후드 부자재: 넥·리브·자수 위치"},
    {"slug": "knitwear-sweater-trims-guide.html",
     "zh": "針織毛衣輔料：標籤、羅紋與洗水標", "en": "Knitwear trims: labels, ribs and care labels",
     "fr": "Accessoires de maille : étiquettes, bords-côtes, entretien", "es": "Accesorios de punto: etiquetas, canalé, cuidado",
     "ja": "ニット資材：ラベル・リブ・洗濯表示", "ko": "니트 부자재: 라벨·리브·취급 표시"},
    {"slug": "formaldehyde-apparel-trims-guide.html",
     "zh": "甲醛與服裝輔料：限值、測試與對策", "en": "Formaldehyde in apparel trims: limits, testing, fixes",
     "fr": "Formaldéhyde dans les accessoires : limites et essais", "es": "Formaldehído en accesorios: límites y ensayos",
     "ja": "ホルムアルデヒドと衣料資材：限度・試験・対策", "ko": "포름알데히드와 의류 부자재: 한도·시험·대책"},
]

CTA_P = {
    "zh": "要為刺繡圖案定襯紙？把布料成分、針數、洗滌方式與目標市場發給我們，我們會回一份含襯紙類型、克重、貼面方案與甲醛測試要求的規格，並附可縫樣品。",
    "en": "Defining a backing for an embroidery program? Send the fabric composition, stitch count, wash care and destination markets, and we will return a specification with backing family, weight, topping and formaldehyde test requirements, plus a sewable sample.",
    "fr": "Un support à définir pour un programme de broderie ? Indiquez la composition, le nombre de points, l'entretien et les marchés : nous renverrons une spécification avec famille, grammage, film de dessus et exigences d'essai formaldéhyde, plus un échantillon cousable.",
    "es": "¿Definiendo entretela para un programa de bordado? Envíe composición, número de puntadas, cuidado y mercados: devolveremos una especificación con familia, gramaje, film superior y requisitos de ensayo de formaldehído, más una muestra cosible.",
    "ja": "刺繍用の裏地を決めたいときは、素材組成・針数・洗濯方法・対象市場をお送りください。裏地の種類、目付、上面フィルム、ホルムアルデヒド試験要件を含む仕様と縫製可能なサンプルをご提案します。",
    "ko": "자수용 받침지를 정하시려면 원단 조성, 바늘 수, 세탁 방법, 대상 시장을 보내주십시오. 받침지 종류, 평량, 상면 필름, 포름알데히드 시험 요건을 담은 사양서와 봉제 가능한 샘플을 제안합니다.",
}
CTA_BTN = {
    "zh": "索取刺繡襯紙規格 →", "en": "Request an embroidery backing spec →", "fr": "Demander une spécification →",
    "es": "Solicitar una especificación →", "ja": "刺繍裏地の仕様を依頼 →", "ko": "자수 받침지 사양 요청 →",
}
