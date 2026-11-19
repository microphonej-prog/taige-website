# -*- coding: utf-8 -*-
"""2026-11-19 08:00 批次 A：技術包裡的輔料規格書怎麼寫（trim spec / tech pack）"""

SLUG = "tech-pack-trim-spec-guide"
CATEGORY = {
    "zh": "採購與規格", "en": "Sourcing & Specs", "fr": "Sourcing & specs",
    "es": "Compras y fichas", "ja": "調達・仕様", "ko": "소싱·사양",
}
TITLE = {
    "zh": "輔料規格書怎麼寫：技術包裡的六個欄位 | TAGE",
    "en": "Tech Pack Trim Specs: How to Write Them Properly | TAGE",
    "fr": "Fiche technique accessoires : six champs à renseigner | TAGE",
    "es": "Ficha técnica de accesorios: los seis campos | TAGE",
    "ja": "仕様書の副資材欄：6 つの必須項目 | TAGE",
    "ko": "테크팩 부자재 사양서 6개 항목 | TAGE",
}
DESC = {
    "zh": "輔料規格書為什麼總被打樣打回：技術包裡缺的六個欄位——輔料編號、結構、尺寸與允差、顏色基準、位置與用量、合規欄位，附四種輔料寫法與允差口徑。",
    "en": "Six fields every trim spec in a tech pack needs: trim code, construction, dimensions and tolerance, colour reference, placement and compliance fields.",
    "fr": "Six champs indispensables dans une fiche produit d'accessoires : code, construction, dimensions et tolérances, référence couleur, pose et conformité.",
    "es": "Los seis campos que toda ficha de producto de accesorios necesita: código, construcción, dimensiones y tolerancias, referencia de color, posición y conformidad.",
    "ja": "仕様書の副資材欄に必要な 6 項目。品番、構造、寸法と許容差、色基準、取付位置、法令表示を、実際の書き方つきで整理します。",
    "ko": "테크팩 부자재 사양서에 반드시 있어야 할 6개 항목. 품번, 구조, 치수와 허용차, 색 기준, 부착 위치, 법정 표시를 실제 표기 예시와 함께 정리합니다.",
}
H1 = {
    "zh": "輔料規格書怎麼寫：技術包裡的六個欄位",
    "en": "How to Write Trim Specifications in a Tech Pack",
    "fr": "Rédiger les spécifications d'accessoires dans une fiche technique",
    "es": "Cómo redactar especificaciones de accesorios en una ficha técnica",
    "ja": "仕様書（テックパック）の副資材欄の書き方",
    "ko": "테크팩 부자재 사양서 작성법",
}

BLOCKS = [
    ("p", {
        "zh": "服裝主料有布卡、克重、縮率測試，輔料卻常常只有一句話——「織嘜，黑色，40 mm」。工廠照自己的常規做，買方按自己的想像驗，打樣打回三次才發現雙方從沒對過同一件事。本文把技術包（tech pack）裡輔料那一欄拆成六個欄位，並給出吊牌、織嘜、洗水標、掛繩四種常用輔料的實際寫法與允差口徑。",
        "en": "Main fabric arrives with a swatch card, a g/m² figure and a shrinkage test. Trims often arrive as one line of text: 'woven label, black, 40 mm'. The factory builds to its own house standard, the buyer inspects against an imagined one, and the sample comes back three times before anyone notices the two were never describing the same thing. This guide breaks the trim block of a tech pack into six fields and shows what to actually write for hang tags, woven labels, care labels and cords.",
        "fr": "L'étoffe principale arrive avec une carte de coloris, un grammage et un test de retrait. L'accessoire, lui, tient souvent en une ligne : « label tissé, noir, 40 mm ». L'usine fabrique selon son standard maison, l'acheteur contrôle selon celui qu'il imagine, et l'échantillon revient trois fois avant que l'on comprenne que les deux ne parlaient pas du même produit. Cet article découpe le bloc accessoires de la fiche produit en six champs et donne la rédaction réelle pour étiquettes suspendues, labels tissés, étiquettes d'entretien et cordons.",
        "es": "La tela principal llega con carta de colores, gramaje y test de encogimiento. El accesorio suele llegar con una línea: «etiqueta tejida, negra, 40 mm». La fábrica produce según su estándar interno, el comprador inspecciona según el que imagina, y la muestra vuelve tres veces antes de que alguien note que no hablaban de lo mismo. Este artículo divide el bloque de accesorios de la ficha técnica en seis campos y muestra cómo redactar etiquetas colgantes, etiquetas tejidas, etiquetas de cuidado y cordones.",
        "ja": "主素材には色見本、坪量、収縮試験が付いてきますが、副資材は「織りラベル、黒、40 mm」の一行で済まされることが少なくありません。工場は自社標準で作り、バイヤーは頭の中の基準で検品し、サンプルが 3 回戻ってから「同じものを説明していなかった」と気づきます。本稿は仕様書（テックパック）の副資材欄を 6 項目に分解し、下げ札・織りラベル・洗濯表示ラベル・紐の実際の書き方と許容差の考え方を示します。",
        "ko": "본원단은 색상 카드, 평량, 수축 시험 결과와 함께 옵니다. 반면 부자재는 '직조 라벨, 검정, 40 mm' 한 줄로 끝나는 경우가 많습니다. 공장은 자기 표준대로 만들고, 바이어는 머릿속 기준으로 검사하며, 샘플이 세 번 반려된 뒤에야 서로 같은 것을 말하지 않았다는 걸 알게 됩니다. 이 글은 테크팩의 부자재 항목을 6개 칸으로 나누고, 행택·직조 라벨·세탁 표시 라벨·끈의 실제 표기법과 허용차 기준을 정리합니다.",
    }),
    ("h2", {
        "zh": "一、六個欄位：缺一個就打樣",
        "en": "1. Six Fields: Miss One and the Sample Comes Back",
        "fr": "1. Six champs : il en manque un, l'échantillon revient",
        "es": "1. Seis campos: si falta uno, la muestra vuelve",
        "ja": "1. 6 項目：1 つ欠けるとサンプルは戻る",
        "ko": "1. 6개 항목: 하나만 빠져도 샘플은 반려된다",
    }),
    ("table", (
        [
            {"zh": "欄位", "en": "Field", "fr": "Champ", "es": "Campo", "ja": "項目", "ko": "항목"},
            {"zh": "要寫什麼", "en": "What to write", "fr": "À renseigner", "es": "Qué escribir", "ja": "記載内容", "ko": "기재 내용"},
            {"zh": "最常漏", "en": "Most often missing", "fr": "Le plus souvent absent", "es": "Lo que más falta", "ja": "最も抜けやすい", "ko": "가장 자주 빠짐"},
        ],
        [
            [
                {"zh": "輔料編號", "en": "Trim code", "fr": "Code accessoire", "es": "Código de accesorio", "ja": "品番", "ko": "품번"},
                {"zh": "可回溯到採購單的唯一編號", "en": "A unique code that traces back to the PO", "fr": "Un code unique traçable jusqu'au bon de commande", "es": "Un código único trazable hasta el pedido", "ja": "発注書まで追える一意の番号", "ko": "발주서까지 추적되는 고유 번호"},
                {"zh": "只寫名稱，沒編號", "en": "Name only, no code", "fr": "Le nom seul, sans code", "es": "Solo el nombre, sin código", "ja": "名称だけで番号なし", "ko": "이름만 있고 번호 없음"},
            ],
            [
                {"zh": "結構與材質", "en": "Construction and material", "fr": "Construction et matière", "es": "Construcción y material", "ja": "構造と素材", "ko": "구조와 소재"},
                {"zh": "紗線、基材、織法、折邊、厚度", "en": "Yarn, substrate, weave, folded ends, thickness", "fr": "Fil, support, armure, extrémités pliées, épaisseur", "es": "Hilo, soporte, ligamento, puntas dobladas, espesor", "ja": "糸、基材、織組織、折り返し、厚み", "ko": "원사, 기재, 직조 조직, 절첩, 두께"},
                {"zh": "「聚酯纖維」這種等於沒說", "en": "'Polyester' tells nobody anything", "fr": "« Polyester » n'informe de rien", "es": "«Poliéster» no dice nada", "ja": "「ポリエステル」だけでは情報にならない", "ko": "'폴리에스터'만으로는 정보가 없음"},
            ],
            [
                {"zh": "尺寸與允差", "en": "Dimensions with tolerance", "fr": "Dimensions et tolérances", "es": "Dimensiones y tolerancias", "ja": "寸法と許容差", "ko": "치수와 허용차"},
                {"zh": "成品尺寸加 ± 允差，並說明量什麼", "en": "Finished size plus a ± tolerance, and what is measured", "fr": "Cote finie, ± tolérance, et ce qui est mesuré", "es": "Medida final, ± tolerancia y qué se mide", "ja": "仕上がり寸法＋±許容差、そして測定対象", "ko": "완성 치수와 ± 허용차, 측정 대상"},
                {"zh": "寫刀模尺寸、寫切邊寬", "en": "Die size instead of finished size", "fr": "La cote du gabarit au lieu de la cote finie", "es": "La medida del troquel en vez de la final", "ja": "抜き型寸法や裁ち幅で書いてしまう", "ko": "다이 치수나 재단 폭으로 표기"},
            ],
            [
                {"zh": "顏色基準", "en": "Colour reference", "fr": "Référence couleur", "es": "Referencia de color", "ja": "色基準", "ko": "색 기준"},
                {"zh": "色號＋ΔE 容差＋光源", "en": "Colour code, ΔE tolerance, light source", "fr": "Code couleur, tolérance ΔE, source lumineuse", "es": "Código de color, tolerancia ΔE, fuente de luz", "ja": "色番＋ΔE 許容差＋光源", "ko": "색번호 + ΔE 허용차 + 광원"},
                {"zh": "「深灰」兩個字", "en": "'Dark grey', two words", "fr": "« Gris foncé », deux mots", "es": "«Gris oscuro», dos palabras", "ja": "「濃いグレー」の一言", "ko": "'진회색' 한 마디"},
            ],
            [
                {"zh": "位置與用量", "en": "Placement and quantity", "fr": "Pose et quantité", "es": "Posición y cantidad", "ja": "取付位置と数量", "ko": "부착 위치와 수량"},
                {"zh": "距哪條縫、哪個部位、每件幾條", "en": "Which seam, which part, how many per garment", "fr": "Quelle couture, quel emplacement, combien par pièce", "es": "Qué costura, qué parte, cuántos por prenda", "ja": "どの縫い目・部位に、1 着あたり何本", "ko": "어느 솔기·부위에, 한 벌당 몇 개"},
                {"zh": "只寫「領口」", "en": "'At the neck' and nothing else", "fr": "« Au col », sans plus", "es": "«En el cuello», sin más", "ja": "「衿ぐり」だけで終わる", "ko": "'목둘레'라고만 표기"},
            ],
            [
                {"zh": "合規欄位", "en": "Compliance fields", "fr": "Champs réglementaires", "es": "Campos reglamentarios", "ja": "法令表示", "ko": "법정 표시"},
                {"zh": "依市場填：成分、洗護、原產國、責任方", "en": "Per market: fibre content, care, origin, responsible party", "fr": "Selon le marché : composition, entretien, origine, responsable", "es": "Según mercado: composición, cuidado, origen, responsable", "ja": "市場別に組成・取扱い・原産国・責任者", "ko": "시장별 혼용률·취급·원산지·책임자"},
                {"zh": "把合規寫成「客人提供」", "en": "Deferring compliance to 'the customer will provide'", "fr": "Renvoyer la conformité au client", "es": "Dejarlo en «lo aporta el cliente»", "ja": "「客先が用意」で済ませる", "ko": "'고객이 제공'으로 미루기"},
            ],
        ],
    )),
    ("h2", {
        "zh": "二、編號規則：讓採購單、裝箱單、標籤說同一種語言",
        "en": "2. Trim Codes That Survive a Purchase Order",
        "fr": "2. Des codes qui survivent au bon de commande",
        "es": "2. Códigos que sobreviven al pedido",
        "ja": "2. 発注書・梱包明細・現物が同じ言葉で話す番号",
        "ko": "2. 발주서·포장 명세·실물이 같은 언어를 쓰게 하는 품번",
    }),
    ("p", {
        "zh": "建議的編號結構是「類型-顏色-關鍵尺寸-結構-版本」，例如 WL-BLK-40-F2 代表織嘜、黑色、40 mm 寬、雙端折、第二版。長度不重要，重要的是同一個編號會同時出現在技術包、採購單、裝箱單與出貨標籤上；倉庫混料、產線貼錯標，八成是兩個環節用了不同的叫法。",
        "en": "A workable structure is type-colour-key dimension-construction-revision, so WL-BLK-40-F2 means woven label, black, 40 mm wide, folded at both ends, revision 2. The length does not matter. What matters is that the same string appears on the tech pack, the purchase order, the packing list and the carton label. Mixed stock in the warehouse and mislabelled garments on the line are usually two departments using two names for one thing.",
        "fr": "Une structure qui tient : type-couleur-dimension clé-construction-révision, par exemple WL-BLK-40-F2 pour un label tissé, noir, 40 mm de large, plié aux deux extrémités, révision 2. La longueur importe peu ; l'essentiel est que la même chaîne figure sur la fiche produit, le bon de commande, la liste de colisage et l'étiquette carton. Les mélanges en stock et les pièces mal étiquetées viennent presque toujours de deux services qui nomment différemment la même chose.",
        "es": "Una estructura que funciona es tipo-color-medida clave-construcción-revisión: WL-BLK-40-F2 significa etiqueta tejida, negra, 40 mm de ancho, doblada en ambos extremos, revisión 2. La longitud importa poco; lo esencial es que la misma cadena aparezca en la ficha técnica, el pedido, el packing list y la etiqueta del cartón. Las mezclas en almacén y las prendas mal etiquetadas casi siempre vienen de dos departamentos que nombran distinto lo mismo.",
        "ja": "実用的なのは「種類-色-主要寸法-構造-版」の並びで、WL-BLK-40-F2 なら織りラベル・黒・幅 40 mm・両端折り返し・第 2 版を意味します。長さは問題ではなく、同じ文字列が仕様書・発注書・梱包明細・カートンラベルに揃って出ることが重要です。倉庫での混在や縫製ラインでの貼り間違いは、たいてい 2 つの部署が同じものを別の名前で呼んでいるだけです。",
        "ko": "실무적인 구조는 '종류-색상-주요 치수-구조-차수'입니다. WL-BLK-40-F2는 직조 라벨, 검정, 폭 40 mm, 양단 절첩, 2차 개정을 뜻합니다. 길이는 중요하지 않고, 같은 문자열이 테크팩·발주서·포장 명세·카톤 라벨에 모두 같게 나오는 것이 중요합니다. 창고 혼입과 라인 오부착은 대개 두 부서가 같은 것을 다른 이름으로 부르는 데서 시작합니다.",
    }),
    ("h2", {
        "zh": "三、四種常用輔料的實際寫法",
        "en": "3. What to Actually Write for Four Common Trims",
        "fr": "3. Ce qu'il faut écrire pour quatre accessoires courants",
        "es": "3. Qué escribir para cuatro accesorios habituales",
        "ja": "3. よく使う 4 種の副資材の実際の記載",
        "ko": "3. 자주 쓰는 부자재 4종의 실제 표기",
    }),
    ("table", (
        [
            {"zh": "輔料", "en": "Trim", "fr": "Accessoire", "es": "Accesorio", "ja": "副資材", "ko": "부자재"},
            {"zh": "必寫參數", "en": "Parameters to state", "fr": "Paramètres à indiquer", "es": "Parámetros a indicar", "ja": "記載必須のパラメータ", "ko": "필수 기재 항목"},
            {"zh": "量測口徑", "en": "How it is measured", "fr": "Comment on mesure", "es": "Cómo se mide", "ja": "測り方", "ko": "측정 기준"},
        ],
        [
            [
                {"zh": "吊牌", "en": "Hang tag", "fr": "Étiquette suspendue", "es": "Etiqueta colgante", "ja": "下げ札", "ko": "행택"},
                {"zh": "紙張 350 g/m²、厚度 0.45 mm、覆膜、孔徑 3 mm、掛繩 120 mm 圈長", "en": "350 g/m² board, 0.45 mm caliper, lamination, 3 mm hole, 120 mm cord loop", "fr": "carton 350 g/m², épaisseur 0,45 mm, pelliculage, trou de 3 mm, cordon boucle 120 mm", "es": "cartón 350 g/m², espesor 0,45 mm, laminado, ojal de 3 mm, cordón de 120 mm", "ja": "台紙 350 g/m²、厚み 0.45 mm、ラミネート、穴 3 mm、紐ループ 120 mm", "ko": "지질 350 g/m², 두께 0.45 mm, 라미네이팅, 구멍 3 mm, 끈 루프 120 mm"},
                {"zh": "成品尺寸，不含刀模出血", "en": "Finished size, excluding die bleed", "fr": "Cote finie, hors fonds perdus", "es": "Medida final, sin sangrado", "ja": "仕上がり寸法（塗り足しを除く）", "ko": "완성 치수(도련 제외)"},
            ],
            [
                {"zh": "織嘜", "en": "Woven label", "fr": "Label tissé", "es": "Etiqueta tejida", "ja": "織りラベル", "ko": "직조 라벨"},
                {"zh": "經緯紗、組織、密度、寬 40 mm、切邊或折邊、耐洗 60 ℃", "en": "Warp and weft yarn, weave, density, 40 mm width, cut or folded edge, 60 °C wash", "fr": "chaîne et trame, armure, densité, largeur 40 mm, bord coupé ou plié, lavage 60 °C", "es": "urdimbre y trama, ligamento, densidad, ancho 40 mm, borde cortado o doblado, lavado 60 °C", "ja": "経糸・緯糸、組織、密度、幅 40 mm、裁ち切り／折り返し、60 ℃ 洗濯", "ko": "경사·위사, 조직, 밀도, 폭 40 mm, 재단 또는 절첩, 60 ℃ 세탁"},
                {"zh": "切邊寬（不含折邊）", "en": "Cut width, excluding the fold", "fr": "Largeur coupée, hors pli", "es": "Ancho cortado, sin el doblez", "ja": "裁ち幅（折り返しを除く）", "ko": "재단 폭(절첩 제외)"},
            ],
            [
                {"zh": "洗水標", "en": "Care label", "fr": "Étiquette d'entretien", "es": "Etiqueta de cuidado", "ja": "洗濯表示ラベル", "ko": "세탁 표시 라벨"},
                {"zh": "尼龍塔夫綢、寬 20 mm、印刷方式、洗護符號依 ISO 3758、耐洗 40 次", "en": "Nylon taffeta, 20 mm width, print method, care symbols per ISO 3758, 40 washes", "fr": "taffetas nylon, largeur 20 mm, procédé d'impression, symboles selon ISO 3758, 40 lavages", "es": "tafetán de nailon, ancho 20 mm, método de impresión, símbolos según ISO 3758, 40 lavados", "ja": "ナイロンタフタ、幅 20 mm、印刷方式、ISO 3758 の取扱い記号、40 回洗濯", "ko": "나일론 태피터, 폭 20 mm, 인쇄 방식, ISO 3758 취급 기호, 40회 세탁"},
                {"zh": "標面字高與符號高度", "en": "Text and symbol height on the face", "fr": "Hauteur des textes et symboles", "es": "Altura de textos y símbolos", "ja": "文字高と記号の高さ", "ko": "문자 높이와 기호 높이"},
            ],
            [
                {"zh": "掛繩", "en": "Cord", "fr": "Cordon", "es": "Cordón", "ja": "紐", "ko": "끈"},
                {"zh": "材質、線徑 1.5 mm、切長 150 mm、結型、有色迁移測試要求", "en": "Material, 1.5 mm diameter, 150 mm cut length, knot type, migration test", "fr": "matière, diamètre 1,5 mm, longueur coupée 150 mm, type de nœud, test de migration", "es": "material, diámetro 1,5 mm, largo cortado 150 mm, tipo de nudo, test de migración", "ja": "材質、太さ 1.5 mm、カット長 150 mm、結び方、移行試験の要否", "ko": "소재, 굵기 1.5 mm, 재단 길이 150 mm, 매듭 방식, 이행 시험 요구"},
                {"zh": "切長而非圈長", "en": "Cut length, not loop length", "fr": "Longueur coupée, pas la boucle", "es": "Largo cortado, no el lazo", "ja": "ループ長ではなくカット長", "ko": "루프 길이가 아닌 재단 길이"},
            ],
        ],
    )),
    ("callout", {
        "zh": "同一個尺寸寫錯口徑，比不寫更貴：吊牌寫刀模尺寸，成品會小 6 mm；織嘜寫含折邊寬，裝到領口會多出 10 mm。每條尺寸後面補一句「量什麼」，能省掉一輪打樣。",
        "en": "A dimension stated in the wrong convention costs more than a missing one: die size on a hang tag yields a tag 6 mm smaller than expected, and a woven label width that includes the fold adds 10 mm at the neck. One clause after each number — what exactly is measured — usually saves an entire sampling round.",
        "fr": "Une cote donnée dans la mauvaise convention coûte plus cher qu'une cote absente : la dimension du gabarit donne une étiquette 6 mm plus petite, et une largeur de label tissé pli inclus ajoute 10 mm au col. Une précision après chaque chiffre — ce qui est mesuré — économise souvent un cycle d'échantillonnage.",
        "es": "Una medida con la convención equivocada cuesta más que una ausente: la medida del troquel deja la etiqueta 6 mm más pequeña, y un ancho de etiqueta tejida con doblez añade 10 mm en el cuello. Una aclaración tras cada cifra —qué se mide— ahorra normalmente una ronda de muestras.",
        "ja": "寸法の測り方を間違えるほうが、書かないより高くつきます。下げ札を抜き型寸法で書くと仕上がりが 6 mm 小さくなり、織りラベルの幅に折り返しを含めると衿ぐりで 10 mm オーバーします。数字の後ろに「何を測るか」を一言添えるだけで、サンプル 1 巡を節約できます。",
        "ko": "치수 기준을 틀리게 적는 것이 안 적는 것보다 비쌉니다. 행택을 다이 치수로 적으면 완성품이 6 mm 작아지고, 직조 라벨 폭에 절첩을 포함하면 목둘레에서 10 mm 초과합니다. 숫자 뒤에 '무엇을 재는지' 한 줄만 붙여도 샘플 한 차례를 아낄 수 있습니다.",
    }),
    ("h2", {
        "zh": "四、允差與量測方法",
        "en": "4. Tolerances and Measurement Method",
        "fr": "4. Tolérances et méthode de mesure",
        "es": "4. Tolerancias y método de medición",
        "ja": "4. 許容差と測定方法",
        "ko": "4. 허용차와 측정 방법",
    }),
    ("p", {
        "zh": "允差要照輔料自身的工藝能力給，不是照服裝主料抄。印刷類吊牌的成品尺寸給 ±1 mm、克重給 ±5%；織嘜的寬度給 ±2 mm、長度給 ±3 mm；洗水標裁切給 ±2 mm；掛繩切長給 ±5 mm。同時寫明取樣方式：每批抽 5 件、平鋪 5 分鐘後量、用什麼量具。沒有量測方法的允差，等於沒有允差。",
        "en": "Tolerances should follow what the trim process can actually hold, not what the garment spec says about fabric. Printed hang tags: ±1 mm on finished size and ±5% on g/m². Woven labels: ±2 mm on width, ±3 mm on length. Care labels: ±2 mm on the cut. Cords: ±5 mm on cut length. State the sampling method alongside — five pieces per lot, laid flat for five minutes, measured with a stated instrument. A tolerance without a measurement method is not a tolerance.",
        "fr": "Les tolérances doivent refléter la capacité réelle du procédé de l'accessoire, pas être recopiées de la spécification tissu. Étiquette imprimée : ±1 mm sur la cote finie, ±5 % sur le grammage. Label tissé : ±2 mm en largeur, ±3 mm en longueur. Étiquette d'entretien : ±2 mm à la coupe. Cordon : ±5 mm sur la longueur coupée. Ajoutez la méthode d'échantillonnage — cinq pièces par lot, à plat pendant cinq minutes, instrument précisé. Une tolérance sans méthode de mesure n'est pas une tolérance.",
        "es": "Las tolerancias deben reflejar la capacidad real del proceso del accesorio, no copiarse de la especificación de tela. Etiqueta impresa: ±1 mm en medida final y ±5 % en gramaje. Etiqueta tejida: ±2 mm de ancho, ±3 mm de largo. Etiqueta de cuidado: ±2 mm en el corte. Cordón: ±5 mm en largo cortado. Indique además el método de muestreo: cinco piezas por lote, en plano cinco minutos, instrumento definido. Una tolerancia sin método de medición no es una tolerancia.",
        "ja": "許容差は生地の仕様を写すのではなく、その副資材の工程能力に合わせます。印刷下げ札は仕上がり寸法 ±1 mm、坪量 ±5 %。織りラベルは幅 ±2 mm、長さ ±3 mm。洗濯表示ラベルは裁断 ±2 mm。紐はカット長 ±5 mm。あわせて抜取方法も明記します。ロットごとに 5 枚、平置き 5 分後に、指定の測定具で測る。測り方のない許容差は許容差ではありません。",
        "ko": "허용차는 원단 사양을 그대로 옮기지 말고 해당 부자재 공정 능력에 맞춥니다. 인쇄 행택은 완성 치수 ±1 mm, 평량 ±5 %. 직조 라벨은 폭 ±2 mm, 길이 ±3 mm. 세탁 표시 라벨은 재단 ±2 mm. 끈은 재단 길이 ±5 mm. 샘플링 방법도 함께 적습니다. 로트당 5개, 5분 평치 후 지정 측정기로 측정. 측정 방법이 없는 허용차는 허용차가 아닙니다.",
    }),
    ("h2", {
        "zh": "五、合規欄位：一個市場一行",
        "en": "5. Compliance Fields: One Row per Market",
        "fr": "5. Champs réglementaires : une ligne par marché",
        "es": "5. Campos reglamentarios: una fila por mercado",
        "ja": "5. 法令表示：市場ごとに 1 行",
        "ko": "5. 법정 표시: 시장별 한 줄",
    }),
    ("p", {
        "zh": "合規欄位不是「客人給」，而是規格書的一部分。歐盟市場：纖維成分依 Règlement (UE) 1007/2011 標註，洗護符號用 ISO 3758 體系；自 GPSR (EU) 2023/988 適用後，還要在標籤或包裝上給出歐盟責任方與可追溯資訊。美國：洗護標示依 16 CFR 423，纖維成分依 FTC 紡織品標示規則，童裝需 CPSIA 追溯標。日本：家庭用品品質表示法要求混用率、取扱表示與原産国。韓國：依 전기용품 및 생활용품 안전관리법 標示 품질 표시（섬유 혼용률、취급 표시、원산지）。",
        "en": "Compliance is not a field to defer to the customer; it is part of the specification. European Union: fibre composition under Regulation (EU) 1007/2011, care symbols following ISO 3758, and since GPSR (EU) 2023/988 an EU responsible party plus traceability information on the label or packaging. United States: care labelling under 16 CFR 423, fibre content under the FTC textile rules, and a CPSIA tracking label on children's items. Japan: 家庭用品品質表示法 requires 混用率, 取扱表示 and 原産国. Korea: 전기용품 및 생활용품 안전관리법 requires 품질 표시 — 섬유 혼용률, 취급 표시 and 원산지.",
        "fr": "La conformité ne se délègue pas au client : elle fait partie de la spécification. Union européenne : composition selon le règlement (UE) 1007/2011, symboles d'entretien selon ISO 3758, et depuis le GPSR (UE) 2023/988 un responsable établi dans l'Union plus des informations de traçabilité sur l'étiquette ou l'emballage. États-Unis : étiquetage d'entretien selon 16 CFR 423, composition selon les règles FTC, marquage de traçabilité CPSIA pour l'enfant. Japon : la loi 家庭用品品質表示法 impose 混用率, 取扱表示 et 原産国. Corée : 전기용품 및 생활용품 안전관리법 impose 품질 표시, 즉 섬유 혼용률, 취급 표시 et 원산지.",
        "es": "La conformidad no se delega al cliente: forma parte de la especificación. Unión Europea: composición según el Reglamento (UE) 1007/2011, símbolos de cuidado según ISO 3758 y, desde el GPSR (UE) 2023/988, un responsable establecido en la UE e información de trazabilidad en la etiqueta o el envase. Estados Unidos: etiquetado de cuidado según 16 CFR 423, composición según las reglas FTC y etiqueta de trazabilidad CPSIA en infantil. Japón: la ley 家庭用品品質表示法 exige 混用率, 取扱表示 y 原産国. Corea: 전기용품 및 생활용품 안전관리법 exige 품질 표시 — 섬유 혼용률, 취급 표시 y 원산지.",
        "ja": "法令表示は「客先が用意するもの」ではなく、仕様書の一部です。EU は繊維組成を Règlement (UE) 1007/2011 に従って表示し、取扱い記号は ISO 3758 の体系を使います。GPSR (EU) 2023/988 の適用開始後は、EU 域内の責任者とトレーサビリティ情報をラベルまたは包装に記載する必要があります。米国は 16 CFR 423 の取扱い表示、FTC の繊維表示規則、子ども向けは CPSIA の追跡ラベル。日本は家庭用品品質表示法により混用率・取扱表示・原産国が必要です。韓国は 전기용품 및 생활용품 안전관리법 により 품질 표시（섬유 혼용률・취급 표시・원산지）が求められます。",
        "ko": "법정 표시는 '고객이 준비'할 항목이 아니라 사양서의 일부입니다. EU는 섬유 혼용률을 Règlement (UE) 1007/2011에 따라 표시하고 취급 기호는 ISO 3758 체계를 씁니다. GPSR (EU) 2023/988 시행 이후에는 EU 역내 책임자와 추적 정보를 라벨이나 포장에 기재해야 합니다. 미국은 16 CFR 423 취급 표시, FTC 섬유 표시 규칙, 아동복은 CPSIA 추적 라벨이 필요합니다. 일본은 家庭用品品質表示法에 따라 混用率·取扱表示·原産国을 표시합니다. 한국은 전기용품 및 생활용품 안전관리법에 따라 품질 표시(섬유 혼용률·취급 표시·원산지)를 기재합니다.",
    }),
    ("h2", {
        "zh": "六、版本控制：一張規格書只能有一個版本號",
        "en": "6. Revision Control: One Spec, One Revision Letter",
        "fr": "6. Gestion des versions : une fiche, une révision",
        "es": "6. Control de versiones: una ficha, una revisión",
        "ja": "6. 版管理：仕様書に版は 1 つだけ",
        "ko": "6. 차수 관리: 사양서에는 차수 하나만",
    }),
    ("p", {
        "zh": "改規格的做法是「加版不改版」：舊版作廢但樣品保留，新版加一個字母並在變更處標記，只有買方書面確認後才切換。實務上最省事的做法，是讓每一版都附一片簽名極限樣（limit sample）——供應商照樣品做，驗貨照樣品判，文字只負責說明差異。",
        "en": "Change a spec by adding a revision, never by editing the old one: void the previous revision but keep its sample, add a letter to the new one, mark what changed, and switch only after written buyer approval. The cheapest practice in the real world is a signed limit sample with every revision — the supplier builds to it, inspection judges against it, and the text only explains the delta.",
        "fr": "On modifie une spécification en ajoutant une révision, jamais en réécrivant l'ancienne : l'ancienne est annulée mais son échantillon conservé, la nouvelle reçoit une lettre, les changements sont surlignés, et le basculement n'a lieu qu'après accord écrit de l'acheteur. Le plus efficace reste un échantillon limite signé par révision : le fournisseur produit dessus, le contrôle juge dessus, le texte ne fait qu'expliquer l'écart.",
        "es": "Una especificación se cambia añadiendo revisión, nunca reescribiendo la anterior: se anula la vieja pero se conserva su muestra, la nueva lleva una letra, se marcan los cambios y solo se cambia tras aprobación escrita del comprador. Lo más eficaz en la práctica es una muestra límite firmada por revisión: el proveedor produce sobre ella, la inspección juzga contra ella y el texto solo explica la diferencia.",
        "ja": "仕様変更は版を追加して行い、旧版を書き換えません。旧版は無効にしますが現物サンプルは保管し、新版に英字を付け、変更点に印を付け、買い手の書面承認後に切り替えます。実務で最も効くのは版ごとの署名入り限界見本です。供給側は見本に合わせて作り、検品は見本で判定し、文章は差分の説明に徹します。",
        "ko": "사양 변경은 차수를 추가해서 하고 기존 차수를 고쳐 쓰지 않습니다. 이전 차수는 무효로 하되 실물 샘플은 보관하고, 새 차수에 알파벳을 붙이고 변경점을 표시하며, 바이어 서면 승인 후에만 전환합니다. 실무에서 가장 효과적인 것은 차수별 서명된 한계 견본입니다. 공급자는 견본대로 만들고, 검사는 견본으로 판정하며, 문서는 차이 설명만 담당합니다.",
    }),
    ("callout", {
        "zh": "最常見的打樣返工原因不是工藝做不出來，而是同一份規格書裡有兩個版本號——報價用的、下單用的、驗貨用的各一份。把版本號寫進檔名與採購單，這個問題就消失了。",
        "en": "The most common cause of resampling is not an impossible process; it is one spec carrying two revision letters — one quoted from, one ordered from, one inspected against. Put the revision letter in the filename and in the PO and the problem disappears.",
        "fr": "La première cause de rééchantillonnage n'est pas un procédé impossible, mais une fiche portant deux révisions : une pour le devis, une pour la commande, une pour le contrôle. Mettez la lettre de révision dans le nom de fichier et dans le bon de commande, et le problème disparaît.",
        "es": "La causa más común de repetir muestras no es un proceso imposible, sino una ficha con dos revisiones: una para cotizar, otra para pedir y otra para inspeccionar. Pon la letra de revisión en el nombre del archivo y en el pedido, y el problema desaparece.",
        "ja": "サンプルやり直しの最大の原因は、できない加工ではなく、1 つの仕様書に 2 つの版が混在することです。見積用・発注用・検品用が別々になっている。版をファイル名と発注書に明記すれば、この問題は消えます。",
        "ko": "샘플 재작업의 가장 흔한 원인은 불가능한 공정이 아니라 한 사양서에 두 개의 차수가 섞여 있는 것입니다. 견적용·발주용·검사용이 따로 존재합니다. 차수를 파일명과 발주서에 넣으면 문제가 사라집니다.",
    }),
    ("related", [
        ("garment-trims-bom-consumption-guide.html", {
            "zh": "輔料 BOM 與用量計算：一件衣服到底用多少",
            "en": "Trim BOM and consumption: how much each garment really uses",
            "fr": "Nomenclature et consommation d'accessoires",
            "es": "BOM y consumo de accesorios",
            "ja": "副資材 BOM と使用量計算",
            "ko": "부자재 BOM과 소요량 계산",
        }),
        ("sample-room-trims-checklist.html", {
            "zh": "樣品室輔料清單：打樣前該備齊的 12 項",
            "en": "Sample room trims checklist: 12 items before sampling",
            "fr": "Checklist accessoires du sample room",
            "es": "Checklist de accesorios para muestras",
            "ja": "サンプル室の副資材チェックリスト",
            "ko": "샘플실 부자재 체크리스트",
        }),
        ("care-label-standards.html", {
            "zh": "洗水標標準：各市場該標什麼",
            "en": "Care label standards by market",
            "fr": "Normes d'étiquetage d'entretien par marché",
            "es": "Normas de etiquetado de cuidado por mercado",
            "ja": "洗濯表示ラベルの各国規格",
            "ko": "세탁 표시 라벨 국가별 규격",
        }),
    ]),
    ("cta", (
        {
            "zh": "手上有一份技術包，卻不確定輔料那幾行寫得夠不夠下單？把規格頁發給我們，我們按這六個欄位逐條標出缺項與允差建議，並對照你目標市場的標示要求給一份可下單的版本。",
            "en": "Have a tech pack but not sure the trim lines are orderable? Send us the spec page and we will mark missing fields, suggest tolerances and return a version your factory can build from, checked against your target market's labelling rules.",
            "fr": "Vous avez une fiche technique mais doutez que les lignes accessoires soient commandables ? Envoyez-nous la page de spécifications : nous signalons les champs manquants, proposons les tolérances et renvoyons une version exploitable en production, vérifiée contre les obligations d'étiquetage de votre marché.",
            "es": "¿Tienes una ficha técnica pero dudas de que las líneas de accesorios permitan producir? Envíanos la página de especificaciones y marcamos los campos que faltan, proponemos tolerancias y devolvemos una versión fabricable, revisada contra el etiquetado de tu mercado.",
            "ja": "仕様書はあるけれど、副資材の行が発注できる水準か不安な場合。仕様ページをお送りください。6 項目に沿って不足を指摘し、許容差の案を添え、対象市場の表示義務と突き合わせた発注可能な版をお返しします。",
            "ko": "테크팩은 있지만 부자재 항목이 발주 가능한 수준인지 확신이 없으신가요? 사양 페이지를 보내주시면 6개 항목 기준으로 빠진 부분을 표시하고 허용차 안을 제시하며, 목표 시장 표시 규정과 대조한 발주 가능 버전을 돌려드립니다.",
        },
        {
            "zh": "索取輔料規格書範本 →",
            "en": "Request the trim spec template →",
            "fr": "Demander le modèle de spécification →",
            "es": "Solicitar la plantilla de especificaciones →",
            "ja": "副資材仕様書テンプレートを依頼 →",
            "ko": "부자재 사양서 템플릿 요청 →",
        },
    )),
]
