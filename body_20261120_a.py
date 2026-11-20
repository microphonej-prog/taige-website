# -*- coding: utf-8 -*-
"""2026-11-20 08:00 批次 A：吊牌改版三條路徑（重印 / 貼標覆蓋 / 換版號）——成本結構與合規紅線。"""

SLUG = "hang-tag-reprint-guide"
CATEGORY = {
    "zh": "標籤與吊牌", "en": "Labels & Hang Tags", "fr": "Étiquettes",
    "es": "Etiquetas", "ja": "ネーム・下げ札", "ko": "라벨·행택",
}
TITLE = {
    "zh": "吊牌改版：重印、貼標覆蓋還是換版號 | TAGE",
    "en": "Hang Tag Changes: Reprint, Over-Sticker or New Version? | TAGE",
    "fr": "Modifier une étiquette pendante : réimpression ou sur-étiquetage | TAGE",
    "es": "Cambiar una etiqueta colgante: reimpresión o sobre-etiquetado | TAGE",
    "ja": "下げ札の改版：再印刷・上貼り・版更新の選び方 | TAGE",
    "ko": "행택 변경: 재인쇄·덧붙이기·새 버전 선택 | TAGE",
}
DESC = {
    "zh": "吊牌印好後才要改：整批重印、貼紙覆蓋、換版號三條路徑的成本算法、起訂量影響，以及貼標覆蓋不能碰的四類法定信息。附版本管控欄位與決定前六問。",
    "en": "A price change or a compliance fix forces new hang tags. Compare reprint, over-stickering and a new version: cost per piece, tooling and legal limits.",
    "fr": "Un changement de prix ou une correction réglementaire impose de refaire les étiquettes : réimpression, sur-étiquetage, nouvelle version, coûts et limites légales.",
    "es": "Un cambio de precio o una corrección normativa obliga a rehacer las etiquetas: reimpresión, sobre-etiquetado, nueva versión, costes y límites legales.",
    "ja": "価格改定や法定表示の訂正で下げ札を作り直すとき、再印刷・上貼り・版更新のコストと法的限界を比較し、版管理の項目と決断前の 6 つの質問を整理します。",
    "ko": "가격 변경이나 법정 표시 정정으로 행택을 다시 만들어야 할 때, 재인쇄·덧붙이기·새 버전의 원가와 법적 한계를 비교하고 버전 관리 항목과 결정 전 여섯 질문을 정리합니다.",
}
H1 = {
    "zh": "吊牌改版：重印、貼標覆蓋還是換版號",
    "en": "Hang Tag Changes: Reprint, Over-Sticker or a New Version",
    "fr": "Modifier une étiquette pendante : réimpression, sur-étiquetage ou nouvelle version",
    "es": "Cambiar una etiqueta colgante: reimpresión, sobre-etiquetado o nueva versión",
    "ja": "下げ札の改版：再印刷・上貼り・版更新のどれを選ぶか",
    "ko": "행택 변경: 재인쇄·덧붙이기·새 버전 중 무엇을 고를까",
}

BLOCKS = [
    ("p", {
        "zh": "吊牌印好之後才收到改動通知，是輔料採購最常見的一種返工。第一反應通常是「全部重印最保險」，第二反應是「貼一張貼紙就好」，兩個反應都要付代價：重印把製版與打樣的一次性成本再付一遍，貼紙覆蓋則可能直接把法定信息蓋在膠水底下。這篇把改版拆成三條路徑，逐條算成本，劃出貼標的法律紅線，最後給決定前的六個問題。",
        "en": "Learning that the hang tag has to change after it has been printed is the most common rework in trims procurement. The first instinct is to reprint everything; the second is to cover the old panel with a sticker. Both carry a price: a reprint pays the one-off tooling and proofing again, and an over-sticker can bury mandatory information under adhesive. This guide splits the decision into three routes, costs each one out, draws the legal line for stickering, and ends with six questions to settle first.",
        "fr": "Apprendre que l'étiquette pendante doit changer une fois imprimée est la reprise la plus fréquente en achats d'accessoires. Le premier réflexe est de tout réimprimer, le second de coller un autocollant sur l'ancien panneau. Les deux coûtent : la réimpression repaie les frais de forme et d'épreuve, et le sur-étiquetage peut enfouir des mentions obligatoires sous l'adhésif. Cet article sépare la décision en trois voies, chiffre chacune, fixe la limite légale du sur-étiquetage et termine par six questions à trancher avant de lancer.",
        "es": "Descubrir que la etiqueta colgante debe cambiar cuando ya está impresa es el retrabajo más habitual al comprar accesorios. El primer reflejo es reimprimir todo; el segundo, tapar el panel antiguo con una pegatina. Ambos cuestan: la reimpresión vuelve a pagar la plancha y la prueba, y el sobre-etiquetado puede enterrar información obligatoria bajo el adhesivo. Esta guía divide la decisión en tres vías, cifra cada una, marca el límite legal del etiquetado encima y cierra con seis preguntas que conviene resolver antes de lanzar.",
        "ja": "下げ札を刷った後に変更が決まるのは、副資材調達でもっとも多い手戻りです。まず全部刷り直す、次に古い面へシールを貼る。どちらも代償があります。再印刷は製版と校正の初期費用をもう一度払い、上貼りは法定情報を粘着剤の下に埋めかねません。本稿は判断を 3 つのルートに分けてコストを算出し、上貼りの法的限界を線引きし、最後に決断前の 6 つの質問を挙げます。",
        "ko": "행택을 인쇄한 뒤에 변경 통보를 받는 것이 부자재 구매에서 가장 흔한 재작업입니다. 첫 반응은 전부 다시 인쇄하는 것, 두 번째는 기존 면에 스티커를 붙이는 것입니다. 둘 다 대가가 있습니다. 재인쇄는 판과 교정 비용을 다시 지불하고, 덧붙이기는 법정 정보를 접착제 아래에 묻을 수 있습니다. 이 글은 결정을 세 경로로 나누어 원가를 계산하고, 덧붙이기의 법적 한계를 긋고, 마지막에 결정 전 여섯 가지 질문을 제시합니다.",
    }),

    ("h2", {
        "zh": "一、四種會觸發改版的原因",
        "en": "1. Four Triggers That Force a Change",
        "fr": "1. Quatre déclencheurs qui imposent un changement",
        "es": "1. Cuatro desencadenantes que obligan a cambiar",
        "ja": "1. 改版が必要になる 4 つの引き金",
        "ko": "1. 변경을 부르는 네 가지 계기",
    }),

    ("p", {
        "zh": "實務上幾乎所有改版都落在這四類：價格調整、品牌主體變更（公司英文名或註冊地址改了）、法規信息更正（成分比例寫錯、護理符號用錯版本、歐盟責任主體換人）、以及同一款賣到多個市場需要不同語言組合。前兩類是商業決定，後兩類是合規問題——合規問題不能用貼紙拖時間，因為抽檢看的是成品上的信息，不是採購的計劃。",
        "en": "In practice almost every change falls into four buckets: a price adjustment, a change of the legal entity behind the brand (English company name or registered address), a correction to compliance content (a fibre percentage entered wrongly, care symbols from an outdated edition, a new EU responsible person), and one style sold into several markets needing different language sets. The first two are commercial calls. The last two are compliance, and compliance cannot be postponed with a sticker, because an inspection reads the finished product, not the purchasing plan.",
        "fr": "En pratique, presque tout changement relève de quatre catégories : un ajustement de prix, un changement d'entité juridique derrière la marque (raison sociale ou adresse enregistrée), une correction de contenu réglementaire (pourcentage de fibre erroné, symboles d'entretien d'une édition périmée, nouveau responsable dans l'UE), et un modèle vendu sur plusieurs marchés exigeant des jeux de langues différents. Les deux premières relèvent du commercial, les deux dernières de la conformité : un contrôle lit le produit fini, pas le plan d'achat.",
        "es": "En la práctica casi todo cambio cae en cuatro grupos: un ajuste de precio, un cambio de la entidad jurídica tras la marca (razón social o domicilio registrado), una corrección de contenido normativo (porcentaje de fibra erróneo, símbolos de cuidado de una edición obsoleta, nuevo responsable en la UE) y un modelo vendido en varios mercados con combinaciones de idiomas distintas. Los dos primeros son decisiones comerciales; los dos últimos, conformidad, y la conformidad no se aplaza con una pegatina porque la inspección lee el producto acabado.",
        "ja": "実際の変更はほぼ 4 種類に収まります。価格改定、ブランドの法的主体の変更（英文社名や登記住所）、法定情報の訂正（混用率の誤記、旧版の洗濯表示記号、EU 責任者の交代）、そして 1 型を複数市場で売るための言語構成の違いです。前半 2 つは商業判断、後半 2 つはコンプライアンスです。コンプライアンスはシールで先送りできません。検査が見るのは完成品の表示であり、調達計画ではないからです。",
        "ko": "실무에서 변경은 거의 네 가지로 모입니다. 가격 조정, 브랜드의 법적 주체 변경(영문 상호나 등록 주소), 법정 정보 정정(혼용률 오기, 구판 세탁 표시 기호, EU 책임자 교체), 그리고 한 스타일을 여러 시장에 팔기 위한 언어 구성 차이입니다. 앞의 두 가지는 상업적 판단이고 뒤의 두 가지는 컴플라이언스이며, 컴플라이언스는 스티커로 미룰 수 없습니다. 검사가 보는 것은 완제품의 표시이지 구매 계획이 아닙니다.",
    }),

    ("h2", {
        "zh": "二、三條路徑的成本結構",
        "en": "2. What Each of the Three Routes Costs",
        "fr": "2. Ce que coûte chacune des trois voies",
        "es": "2. Lo que cuesta cada una de las tres vías",
        "ja": "2. 3 つのルートのコスト構造",
        "ko": "2. 세 경로의 원가 구조",
    }),

    ("table", (
        [
            {"zh": "路徑", "en": "Route", "fr": "Voie", "es": "Vía", "ja": "ルート", "ko": "경로"},
            {"zh": "一次性成本", "en": "One-off cost", "fr": "Frais ponctuels", "es": "Coste puntual", "ja": "初期費用", "ko": "초기 비용"},
            {"zh": "單件成本", "en": "Per piece", "fr": "Par pièce", "es": "Por pieza", "ja": "1 枚あたり", "ko": "장당 비용"},
            {"zh": "什麼時候選它", "en": "When to choose it", "fr": "Quand la choisir", "es": "Cuándo elegirla", "ja": "選ぶ条件", "ko": "선택 조건"},
        ],
        [
            [
                {"zh": "整批重印", "en": "Full reprint", "fr": "Réimpression complète", "es": "Reimpresión completa", "ja": "全数再印刷", "ko": "전량 재인쇄"},
                {"zh": "製版與打樣", "en": "Plate and proof", "fr": "Forme et épreuve", "es": "Plancha y prueba", "ja": "製版・校正", "ko": "판과 교정"},
                {"zh": "原單價，另加 3–5% 損耗", "en": "Base price plus 3–5% spoilage", "fr": "Prix de base plus 3 à 5 % de rebut", "es": "Precio base más 3–5 % de merma", "ja": "元単価＋3〜5 % の損耗", "ko": "기본 단가 + 3~5% 손실"},
                {"zh": "改動涉及法定信息，或舊庫存不足三個月用量", "en": "The change touches mandatory information, or old stock is under three months of use", "fr": "Le changement touche des mentions obligatoires, ou le stock restant couvre moins de trois mois", "es": "El cambio afecta información obligatoria o el stock cubre menos de tres meses", "ja": "法定情報の変更、または在庫が 3 か月分未満", "ko": "법정 정보 변경, 또는 재고가 3개월분 미만"},
            ],
            [
                {"zh": "貼紙覆蓋", "en": "Over-sticker", "fr": "Sur-étiquetage", "es": "Sobre-etiquetado", "ja": "上貼りシール", "ko": "덧붙이기 스티커"},
                {"zh": "貼紙製版費低，可拼版", "en": "Low sticker tooling, gang-run friendly", "fr": "Forme d'autocollant peu coûteuse, tirage groupé possible", "es": "Plancha de pegatina barata, se puede agrupar", "ja": "シールの製版費は安く、まとめ刷りが可能", "ko": "스티커 판 비용이 낮고 합판 가능"},
                {"zh": "貼紙成本加 4–6 秒人工", "en": "Sticker cost plus 4–6 seconds of labour", "fr": "Coût de l'autocollant plus 4 à 6 secondes de main-d'œuvre", "es": "Coste de la pegatina más 4–6 segundos de mano de obra", "ja": "シール代＋4〜6 秒の工数", "ko": "스티커 비용 + 4~6초 작업 시간"},
                {"zh": "只改非法定信息：價格、內部款號、活動語", "en": "Only non-mandatory content: price, internal style code, campaign wording", "fr": "Uniquement du contenu non obligatoire : prix, référence interne, message de campagne", "es": "Solo contenido no obligatorio: precio, referencia interna, mensaje de campaña", "ja": "価格・社内品番・キャンペーン文言など非法定項目のみ", "ko": "가격, 내부 품번, 캠페인 문구 등 비법정 항목만"},
            ],
            [
                {"zh": "換版號重做，舊版清點或銷毀", "en": "New version, old stock counted or destroyed", "fr": "Nouvelle version, ancien stock compté ou détruit", "es": "Nueva versión, stock antiguo contado o destruido", "ja": "版更新で作り直し、旧版は棚卸しまたは廃棄", "ko": "새 버전 제작, 구버전 재고 확인 또는 폐기"},
                {"zh": "製版費加銷毀見證", "en": "Tooling plus destruction witness", "fr": "Forme plus attestation de destruction", "es": "Plancha más acta de destrucción", "ja": "製版費＋廃棄の立会い", "ko": "판 비용 + 폐기 입회"},
                {"zh": "原單價", "en": "Base price", "fr": "Prix de base", "es": "Precio base", "ja": "元単価", "ko": "기본 단가"},
                {"zh": "多市場並行、需要可追溯的版本號", "en": "Several markets at once, needing a traceable version number", "fr": "Plusieurs marchés en parallèle, avec un numéro de version traçable", "es": "Varios mercados a la vez y número de versión trazable", "ja": "複数市場の同時展開、版番号の追跡が必要", "ko": "여러 시장 동시 전개, 추적 가능한 버전 번호 필요"},
            ],
        ],
    )),

    ("p", {
        "zh": "用一組常見數字比較：5,000 張 350 g/m² 塗佈卡紙吊牌，單價 0.05 美元，製版與打樣 40 美元。整批重印的一次性成本攤到每張是 0.008 美元，加損耗後整批約 300 美元。同樣 5,000 張改用貼紙覆蓋：貼紙每張 0.006 美元，人工每張 5 秒、按每小時 6 美元折算約 0.008 美元，合計約 70 美元，便宜四倍——但前提是改動的內容本來就不在法定清單上。",
        "en": "Run the numbers on a typical job: 5,000 tags in 350 g/m² coated board at 0.05 dollars each, with 40 dollars for plate and proof. Allocating the one-off over 5,000 pieces adds 0.008 dollars per tag, so the full reprint lands near 300 dollars including spoilage. The same 5,000 tags covered by stickers cost 0.006 dollars per sticker plus about 5 seconds of labour each, which at 6 dollars an hour works out near 0.008 dollars, roughly 70 dollars in total. Four times cheaper, provided that what changed was never on the mandatory list to begin with.",
        "fr": "Prenons un cas courant : 5 000 étiquettes en carton couché 350 g/m² à 0,05 dollar, avec 40 dollars de forme et d'épreuve. Répartir ce montant sur 5 000 pièces ajoute 0,008 dollar par étiquette, donc la réimpression complète approche 300 dollars avec le rebut. Les mêmes 5 000 étiquettes recouvertes d'autocollants coûtent 0,006 dollar par autocollant plus environ 5 secondes de main-d'œuvre, soit près de 0,008 dollar à 6 dollars de l'heure : environ 70 dollars au total. Quatre fois moins cher, à condition que la modification ne porte pas sur une mention obligatoire.",
        "es": "Con un caso típico: 5.000 etiquetas en cartulina estucada de 350 g/m² a 0,05 dólares, con 40 dólares de plancha y prueba. Repartir ese importe entre 5.000 piezas añade 0,008 dólares por etiqueta, así que la reimpresión completa ronda 300 dólares con la merma. Las mismas 5.000 etiquetas cubiertas con pegatinas cuestan 0,006 dólares por unidad más unos 5 segundos de mano de obra, cerca de 0,008 dólares a 6 dólares por hora: unos 70 dólares en total. Cuatro veces menos, siempre que lo modificado no fuera información obligatoria.",
        "ja": "よくある条件で比べます。350 g/m² のコートボール 5,000 枚、単価 0.05 ドル、製版と校正 40 ドル。初期費用を 5,000 枚で割ると 1 枚 0.008 ドル、損耗を含めた全数再印刷は約 300 ドルです。同じ 5,000 枚をシールで上貼りすると、シール 1 枚 0.006 ドルに 5 秒の工数、時給 6 ドル換算で約 0.008 ドル、合計およそ 70 ドル。4 倍安いのですが、変更内容がもともと法定項目でない場合に限ります。",
        "ko": "흔한 조건으로 비교해 봅니다. 350 g/m² 코팅 보드 5,000장, 장당 0.05달러, 판과 교정 40달러. 초기 비용을 5,000장으로 나누면 장당 0.008달러가 더해져 손실을 포함한 전량 재인쇄는 약 300달러입니다. 같은 5,000장을 스티커로 덧붙이면 장당 0.006달러에 5초 작업 시간, 시급 6달러로 환산해 약 0.008달러, 합계 약 70달러입니다. 네 배 저렴하지만, 바뀐 내용이 원래 법정 항목이 아니어야 합니다.",
    }),

    ("h2", {
        "zh": "三、貼標覆蓋的三條紅線",
        "en": "3. Three Red Lines for Over-Stickering",
        "fr": "3. Trois lignes rouges du sur-étiquetage",
        "es": "3. Tres líneas rojas del sobre-etiquetado",
        "ja": "3. 上貼りシールの 3 つの赤線",
        "ko": "3. 덧붙이기의 세 가지 금지선",
    }),

    ("p", {
        "zh": "第一條：不能覆蓋法定信息。歐盟 (EU) No 1007/2011 要求紡織品的纖維成分標示在產品上並在流通環節保持可見，把成分貼紙貼在會被撕走的吊牌上，等同沒有標示；美國 16 CFR 423 要求護理說明永久附著於服裝；歐盟 GPSR (EU) 2023/988 要求製造商與責任主體信息可追溯。這三類內容只能重印或重做耐久標籤，吊牌上的貼紙無法補救。第二條：不能降低可讀性——貼紙邊緣要留 2 mm 以上餘量，字高不得小於原版面，重疊印刷會讓掃描器讀不出條碼。第三條：貼紙的耐久性不得低於吊牌本身，洗滌或摩擦後先掉的是貼紙，等於回到舊信息。",
        "en": "The first red line: never cover mandatory information. Regulation (EU) No 1007/2011 requires fibre composition to be indicated on the product and to stay visible through the chain, so a composition sticker on a tag that gets torn off is the same as no label; the FTC rule at 16 CFR 423 requires care instructions permanently attached to the garment; and the GPSR, (EU) 2023/988, requires manufacturer and responsible-person details to be traceable. Those three can only be fixed by reprinting or by remaking the durable label. The second: do not reduce legibility. Keep at least a 2 mm margin around the sticker, never shrink the type below the original size, and remember that a double layer over a barcode is unreadable to a scanner. The third: the sticker must not be less durable than the tag, or the first wash or rub takes you back to the old information.",
        "fr": "Première ligne rouge : ne jamais recouvrir une mention obligatoire. Le règlement (UE) n° 1007/2011 impose d'indiquer la composition des fibres sur le produit et de la garder visible tout au long de la chaîne : un autocollant de composition sur une étiquette qui s'arrache équivaut à une absence d'étiquetage. Aux États-Unis, la règle 16 CFR 423 exige un entretien attaché de façon permanente au vêtement. Le GPSR, règlement (UE) 2023/988, exige la traçabilité du fabricant et du responsable. Ces trois catégories ne se corrigent que par réimpression ou par une nouvelle étiquette durable. Deuxième : ne pas dégrader la lisibilité. Laissez au moins 2 mm de marge autour de l'autocollant, ne réduisez pas les caractères sous la taille d'origine, et notez qu'une double épaisseur sur un code-barres le rend illisible au scanner. Troisième : la durabilité de l'autocollant ne doit pas être inférieure à celle de l'étiquette, sinon le premier lavage ramène l'ancienne information.",
        "es": "Primera línea roja: no cubrir nunca información obligatoria. El Reglamento (UE) n.º 1007/2011 exige indicar la composición de las fibras en el producto y mantenerla visible en toda la cadena, así que una pegatina de composición sobre una etiqueta que se arranca equivale a no etiquetar. En Estados Unidos, la regla 16 CFR 423 exige instrucciones de cuidado unidas de forma permanente a la prenda. El GPSR, Reglamento (UE) 2023/988, exige trazabilidad del fabricante y del responsable. Esas tres categorías solo se corrigen reimprimiendo o rehaciendo la etiqueta duradera. Segunda: no reducir la legibilidad. Deja al menos 2 mm de margen alrededor de la pegatina, no disminuyas el cuerpo de letra y recuerda que una doble capa sobre un código de barras lo vuelve ilegible para el escáner. Tercera: la durabilidad de la pegatina no puede ser menor que la de la etiqueta, o el primer lavado devuelve la información antigua.",
        "ja": "第 1 の赤線は法定情報を覆わないこと。EU 規則 (EU) No 1007/2011 は繊維組成を製品に表示し、流通過程で見える状態に保つことを求めており、剥がされる下げ札に組成シールを貼るのは未表示と同じです。米国は FTC の 16 CFR 423 が取扱表示を衣類に恒久的に添付することを要求し、EU の GPSR（規則 (EU) 2023/988）は製造者と責任者の追跡可能性を求めます。この 3 種は再印刷か耐久ラベルの作り直しでしか直せません。第 2 は可読性を落とさないこと。シールの周囲に 2 mm 以上の余白を取り、文字高を元より小さくせず、バーコードの二重貼りはスキャナで読めないと覚えておきます。第 3 はシールの耐久性を下げないこと。洗濯や摩擦で先に剥がれれば、古い情報に戻るだけです。",
        "ko": "첫째 금지선은 법정 정보를 덮지 않는 것입니다. 규정 (EU) No 1007/2011은 섬유 혼용률을 제품에 표시하고 유통 전 과정에서 보이도록 요구하므로, 떼어지는 행택에 혼용률 스티커를 붙이는 것은 미표시와 같습니다. 미국은 FTC의 16 CFR 423이 취급 표시를 의류에 영구 부착하도록 하고, EU의 GPSR(규정 (EU) 2023/988)은 제조사와 책임자의 추적 가능성을 요구합니다. 이 세 가지는 재인쇄나 내구성 라벨 재제작으로만 고칠 수 있습니다. 둘째는 가독성을 떨어뜨리지 않는 것입니다. 스티커 주위에 2 mm 이상 여백을 두고 글자 높이를 원래보다 줄이지 않으며, 바코드 위 이중 부착은 스캐너가 읽지 못합니다. 셋째는 스티커의 내구성을 행택보다 낮추지 않는 것입니다. 세탁이나 마찰에서 먼저 떨어지면 옛 정보로 돌아갈 뿐입니다.",
    }),

    ("callout", {
        "zh": "一句話分界：價格、內部款號、活動標語可以貼；成分、護理方式、原產地、責任主體只能重印或重做耐久標籤。",
        "en": "One line divides them: price, internal style code and campaign wording can be stickered; composition, care, origin and responsible person must be reprinted or moved to a durable label.",
        "fr": "Une ligne sépare les deux : prix, référence interne et message de campagne peuvent être autocollés ; composition, entretien, origine et responsable exigent une réimpression ou une étiquette durable.",
        "es": "Una línea los separa: precio, referencia interna y mensaje de campaña admiten pegatina; composición, cuidado, origen y responsable exigen reimpresión o etiqueta duradera.",
        "ja": "線引きは 1 つ。価格・社内品番・キャンペーン文言は上貼り可、組成・取扱表示・原産国・責任者は再印刷か耐久ラベルへの移動しかありません。",
        "ko": "구분은 하나입니다. 가격, 내부 품번, 캠페인 문구는 덧붙이기가 가능하고, 혼용률, 취급 표시, 원산지, 책임자는 재인쇄나 내구성 라벨로 옮겨야 합니다.",
    }),

    ("h2", {
        "zh": "四、四個市場的差別：同一批貨不能共用一套貼紙",
        "en": "4. Four Markets, Four Different Answers",
        "fr": "4. Quatre marchés, quatre réponses différentes",
        "es": "4. Cuatro mercados, cuatro respuestas distintas",
        "ja": "4. 4 つの市場で答えは変わる",
        "ko": "4. 네 시장, 네 가지 다른 답",
    }),

    ("p", {
        "zh": "法國除了歐盟規則，還要看《消費法典》對標示與語言的規定，法文標示不是可選項；西班牙以 Real Decreto 928/1987 規範紡織品成分標示，誤導性標示另由《反不正當競爭法》處理；日本《家庭用品品質表示法》把組成、洗濯表示與表示者列為義務項目，廣告用語受《景品表示法》約束；韓國由《品質經營及工業品安全管理法》要求品質標示與原產地，宣傳用語受《表示廣告法》規範。同一批貨賣到四個市場，貼紙方案不能共用——尤其「原產地」與「責任主體」這兩欄，各市場要求的位置與寫法都不同。",
        "en": "France layers the Code de la consommation on top of the EU rules, and French-language marking is not optional. Spain regulates textile composition marking through Real Decreto 928/1987 and handles misleading marks under its unfair competition law. Japan's Household Goods Quality Labelling Act makes composition, care symbols and the labeller mandatory items, while advertising wording falls under the Act against Unjustifiable Premiums and Misleading Representations. Korea requires quality marking and country of origin under its Quality Management and Safety Control of Industrial Products Act, with promotional wording governed by the Act on Fair Labelling and Advertising. One shipment going to four markets cannot share one sticker set, least of all for origin and responsible person, where the required position and wording differ.",
        "fr": "La France superpose le Code de la consommation aux règles de l'Union, et le marquage en français n'est pas optionnel. L'Espagne encadre le marquage de composition par le Real Decreto 928/1987 et traite les marquages trompeurs par le droit de la concurrence déloyale. Au Japon, la loi sur l'étiquetage de qualité des articles ménagers rend obligatoires la composition, les symboles d'entretien et le nom du responsable du marquage, la formulation publicitaire relevant de la loi contre les primes injustifiables et les représentations trompeuses. La Corée impose le marquage de qualité et l'origine via sa loi sur la gestion de la qualité et la sécurité des produits industriels, les mentions promotionnelles étant régies par la loi sur la publicité et l'étiquetage. Une expédition vers quatre marchés ne peut pas partager un seul jeu d'autocollants, surtout pour l'origine et le responsable.",
        "es": "Francia superpone el Code de la consommation a las normas de la Unión, y el marcado en francés no es opcional. España regula el marcado de composición mediante el Real Decreto 928/1987 y trata el marcado engañoso con la Ley 3/1991 de competencia desleal. Japón obliga a indicar composición, símbolos de cuidado y responsable del marcado por su ley de etiquetado de calidad de bienes de consumo, y la publicidad se rige por su ley contra representaciones engañosas. Corea exige marcado de calidad y origen según su ley de gestión de calidad y seguridad de productos industriales, con la publicidad sujeta a su ley de publicidad y etiquetado. Un envío a cuatro mercados no puede compartir un solo juego de pegatinas, sobre todo en origen y responsable.",
        "ja": "フランスは EU 規則に消費法典を重ね、フランス語表示は任意ではありません。スペインは繊維組成の表示を Real Decreto 928/1987 で定め、誤解を招く表示は不公正競争法で処理します。日本は家庭用品品質表示法が組成・洗濯表示・表示者を義務項目とし、広告文言は景品表示法の対象です。韓国は品質経営及び工業品安全管理法により品質表示と原産国を求め、宣伝文言は表示広告法が規律します。4 市場へ同一出荷する場合、シール一式の共用はできません。とくに原産国と責任者は、求められる位置も書き方も違います。",
        "ko": "프랑스는 EU 규정 위에 소비자법을 겹치며 프랑스어 표시는 선택이 아닙니다. 스페인은 섬유 혼용률 표시를 Real Decreto 928/1987로 정하고 오인 표시는 부정경쟁법으로 다룹니다. 일본은 가정용품 품질 표시법이 조성·세탁 표시·표시자를 의무 항목으로 두고 광고 문구는 경품표시법이 규율합니다. 한국은 품질경영 및 공산품 안전관리법으로 품질 표시와 원산지를 요구하고 홍보 문구는 표시광고법이 규율합니다. 네 시장에 같은 선적을 보낼 때 스티커 한 세트를 공유할 수 없으며, 특히 원산지와 책임자는 요구 위치와 표기 방식이 다릅니다.",
    }),

    ("h2", {
        "zh": "五、版本管控：讓舊版不再流出",
        "en": "5. Version Control: Stop the Old Edition Leaving the Warehouse",
        "fr": "5. Gestion des versions : empêcher l'ancienne de sortir",
        "es": "5. Control de versiones: que la antigua no salga",
        "ja": "5. 版管理：旧版を出荷させない",
        "ko": "5. 버전 관리: 구버전이 나가지 않게",
    }),

    ("ul", [
        {
            "zh": "版號印在背面或條碼下方，字高 1.5 mm 以上，與採購單上的號碼一致。",
            "en": "Print the version number on the back or under the barcode at 1.5 mm or larger, matching the number on the purchase order.",
            "fr": "Imprimez le numéro de version au dos ou sous le code-barres, à 1,5 mm minimum, identique à celui du bon de commande.",
            "es": "Imprime el número de versión en el dorso o bajo el código de barras, de 1,5 mm como mínimo, igual al del pedido.",
            "ja": "版番号は裏面かバーコードの下に 1.5 mm 以上の文字高で印刷し、発注書の番号と一致させます。",
            "ko": "버전 번호는 뒷면이나 바코드 아래에 1.5 mm 이상으로 인쇄하고 발주서 번호와 일치시킵니다.",
        },
        {
            "zh": "採購單寫明版號、語言組合、對應市場與失效日期，不要只寫「吊牌一批」。",
            "en": "The PO should name the version, the language set, the target market and an expiry date, not just one batch of tags.",
            "fr": "Le bon de commande précise la version, le jeu de langues, le marché visé et une date de péremption, pas seulement un lot d'étiquettes.",
            "es": "El pedido debe indicar versión, combinación de idiomas, mercado destino y fecha de caducidad, no solo un lote de etiquetas.",
            "ja": "発注書には版番号・言語構成・対象市場・失効日を明記します。「下げ札一式」だけでは足りません。",
            "ko": "발주서에는 버전, 언어 구성, 대상 시장, 만료일을 명기합니다. 행택 일괄로는 부족합니다.",
        },
        {
            "zh": "舊版庫存用不同顏色的膠帶或料架隔離，並在料卡上寫清「不可出貨」。",
            "en": "Segregate old stock with a different tape colour or a separate rack, and mark the bin card as do not ship.",
            "fr": "Isolez l'ancien stock avec une couleur d'adhésif différente ou un rayon séparé, et marquez la fiche de casier comme non expédiable.",
            "es": "Separa el stock antiguo con otro color de cinta o una estantería aparte y marca la ficha como no expedible.",
            "ja": "旧版在庫は色違いのテープや別棚で区分けし、棚札に「出荷不可」と明記します。",
            "ko": "구버전 재고는 다른 색 테이프나 별도 선반으로 분리하고 재고 카드에 출고 금지를 적습니다.",
        },
        {
            "zh": "貼紙方案要留記錄：哪一版、哪個欄位、貼了什麼、由誰貼，否則兩年後無法回答客戶的追溯提問。",
            "en": "Keep a record of every sticker decision: which version, which field, what was applied, and who applied it. Two years later that record is the only answer to a traceability question.",
            "fr": "Conservez la trace de chaque décision d'autocollant : quelle version, quel champ, quel contenu, appliqué par qui. Deux ans plus tard, c'est la seule réponse à une question de traçabilité.",
            "es": "Deja registro de cada decisión de pegatina: qué versión, qué campo, qué se aplicó y quién. Dos años después es la única respuesta a una pregunta de trazabilidad.",
            "ja": "上貼りの記録を残します。どの版、どの欄、何を貼り、誰が貼ったか。2 年後のトレーサビリティ照会に答えられるのはこの記録だけです。",
            "ko": "덧붙이기 기록을 남깁니다. 어느 버전, 어느 항목, 무엇을 붙였고 누가 붙였는지. 2년 뒤 추적성 질의에 답할 수 있는 유일한 근거입니다.",
        },
    ]),

    ("h2", {
        "zh": "六、決定前的六個問題",
        "en": "6. Six Questions Before You Commit",
        "fr": "6. Six questions avant de décider",
        "es": "6. Seis preguntas antes de decidir",
        "ja": "6. 決断前の 6 つの質問",
        "ko": "6. 결정 전 여섯 가지 질문",
    }),

    ("ul", [
        {
            "zh": "改的是法定信息還是商業信息？法定信息直接排除貼紙方案。",
            "en": "Is the change mandatory or commercial? Mandatory content rules out stickers immediately.",
            "fr": "Le changement est-il obligatoire ou commercial ? Une mention obligatoire exclut d'emblée l'autocollant.",
            "es": "¿El cambio es obligatorio o comercial? Si es obligatorio, la pegatina queda descartada.",
            "ja": "変更は法定情報か商業情報か。法定情報なら上貼りは即除外です。",
            "ko": "변경이 법정 정보인가 상업 정보인가. 법정 정보라면 덧붙이기는 즉시 제외입니다.",
        },
        {
            "zh": "舊庫存還能用幾個月？不足三個月用量時，重印的攤提成本其實很低。",
            "en": "How many months of old stock remain? Under three months of use, the amortised cost of a reprint is small.",
            "fr": "Combien de mois d'ancien stock reste-t-il ? Sous trois mois de consommation, le coût amorti d'une réimpression devient faible.",
            "es": "¿Cuántos meses de stock antiguo quedan? Por debajo de tres meses de consumo, el coste amortizado de reimprimir es bajo.",
            "ja": "旧版在庫は何か月分か。3 か月分未満なら再印刷の償却コストは小さいです。",
            "ko": "구버전 재고가 몇 개월분인가. 3개월분 미만이면 재인쇄의 분할 비용은 작습니다.",
        },
        {
            "zh": "市場是一個還是多個？多市場版本要用版號區分，不能靠記憶。",
            "en": "One market or several? Multi-market versions need version numbers, not memory.",
            "fr": "Un marché ou plusieurs ? Les versions multi-marchés exigent des numéros, pas la mémoire.",
            "es": "¿Un mercado o varios? Las versiones multi-mercado necesitan números, no memoria.",
            "ja": "市場は 1 つか複数か。複数なら版番号で区別し、記憶に頼りません。",
            "ko": "시장이 하나인가 여럿인가. 여러 시장이면 버전 번호로 구분하고 기억에 의존하지 않습니다.",
        },
        {
            "zh": "貼紙能撐過洗滌與摩擦嗎？不能就先排除。",
            "en": "Will the sticker survive washing and rubbing? If not, it is out.",
            "fr": "L'autocollant résistera-t-il au lavage et au frottement ? Sinon, il est éliminé.",
            "es": "¿Resistirá la pegatina el lavado y el roce? Si no, queda fuera.",
            "ja": "シールは洗濯と摩擦に耐えるか。耐えないなら除外です。",
            "ko": "스티커가 세탁과 마찰을 견디는가. 못 견디면 제외입니다.",
        },
        {
            "zh": "條碼會被貼紙壓到嗎？壓到就必須改版面，不是換貼紙位置。",
            "en": "Will the sticker sit over the barcode? If so the layout changes, not just the sticker position.",
            "fr": "L'autocollant recouvrira-t-il le code-barres ? Dans ce cas, c'est la maquette qui change.",
            "es": "¿La pegatina tapará el código de barras? Entonces cambia la maqueta, no solo la posición.",
            "ja": "シールがバーコードにかかるか。かかるなら貼り位置ではなく版面を変えます。",
            "ko": "스티커가 바코드를 덮는가. 덮으면 위치가 아니라 판면을 바꿔야 합니다.",
        },
        {
            "zh": "誰負責確認舊版已停用？沒有指定人，舊版一定會在半年內出現在產線上。",
            "en": "Who signs off that the old version is retired? Without a named person, the old stock reappears on the line within six months.",
            "fr": "Qui valide la mise hors service de l'ancienne version ? Sans responsable nommé, l'ancien stock réapparaît en production sous six mois.",
            "es": "¿Quién firma la retirada de la versión antigua? Sin responsable nombrado, el stock viejo reaparece en línea en seis meses.",
            "ja": "旧版の停止を誰が確認するか。担当を決めないと半年以内に旧版がラインに戻ります。",
            "ko": "구버전 중지를 누가 확인하는가. 담당자를 정하지 않으면 반년 안에 구버전이 라인에 다시 나타납니다.",
        },
    ]),

    ("p", {
        "zh": "吊牌改版不是設計問題，而是成本與合規的取捨。把改動歸類、把三條路的成本算出來、把法定信息排除在貼紙之外，最後指定一個人負責舊版停用——四步做完，一次改版就不會拖成兩次返工。",
        "en": "A tag change is not a design question but a trade between cost and compliance. Classify the change, cost the three routes, keep mandatory content off the sticker, and name one person to retire the old version. Do those four things and one revision stops turning into two rounds of rework.",
        "fr": "Modifier une étiquette n'est pas une question de design mais d'arbitrage entre coût et conformité. Classez le changement, chiffrez les trois voies, tenez les mentions obligatoires hors de l'autocollant et nommez une personne chargée de retirer l'ancienne version. Ces quatre gestes évitent qu'une révision devienne deux reprises.",
        "es": "Cambiar una etiqueta no es una cuestión de diseño sino un equilibrio entre coste y conformidad. Clasifica el cambio, cifra las tres vías, mantén la información obligatoria fuera de la pegatina y nombra a una persona responsable de retirar la versión antigua. Con esos cuatro pasos una revisión deja de convertirse en dos retrabajos.",
        "ja": "下げ札の改版はデザインの問題ではなく、コストとコンプライアンスの取り合いです。変更を分類し、3 ルートのコストを出し、法定情報を上貼りから外し、旧版停止の担当者を 1 名決める。この 4 つで、1 回の改版が 2 度の手戻りになるのを防げます。",
        "ko": "행택 변경은 디자인 문제가 아니라 원가와 컴플라이언스의 맞교환입니다. 변경을 분류하고, 세 경로의 원가를 계산하고, 법정 정보를 덧붙이기에서 제외하고, 구버전 중지 담당자를 한 명 지정하십시오. 이 네 단계면 한 번의 개정이 두 번의 재작업으로 번지지 않습니다.",
    }),

    ("related", [
        ("hang-tag-printing-methods.html", {
            "zh": "吊牌印刷方式：膠印、數碼與絲網的選擇",
            "en": "Hang tag printing methods: offset, digital and screen",
            "fr": "Méthodes d'impression des étiquettes : offset, numérique, sérigraphie",
            "es": "Métodos de impresión de etiquetas: offset, digital y serigrafía",
            "ja": "下げ札の印刷方式：オフセット・デジタル・スクリーン",
            "ko": "행택 인쇄 방식: 오프셋·디지털·스크린",
        }),
        ("clothing-price-ticket-guide.html", {
            "zh": "價格標與吊牌：類型、條碼與起訂量",
            "en": "Price tickets vs hang tags: types, barcode and MOQ",
            "fr": "Étiquettes de prix et étiquettes pendantes : types et quantités",
            "es": "Tickets de precio y etiquetas colgantes: tipos y pedido mínimo",
            "ja": "価格ラベルと下げ札：種類・バーコード・MOQ",
            "ko": "가격표와 행택: 종류·바코드·최소 주문량",
        }),
        ("trim-order-change-cancellation-guide.html", {
            "zh": "輔料訂單變更與取消：可以改到哪一步",
            "en": "Trim order changes and cancellations: how late is too late",
            "fr": "Modification et annulation de commande d'accessoires : jusqu'à quand",
            "es": "Cambios y cancelaciones de pedidos de accesorios: hasta cuándo",
            "ja": "副資材の発注変更・キャンセル：どこまで可能か",
            "ko": "부자재 발주 변경·취소: 어디까지 가능한가",
        }),
    ]),

    ("cta", (
        {
            "zh": "手上有一批印錯或要改版的吊牌？把現有版面、要改的欄位與目標市場發給我們，我們判斷哪些能貼、哪些必須重印，並出一版含版號與失效日期的規格。",
            "en": "Sitting on a batch of tags that need changing? Send the current layout, the fields to change and the target markets, and we will separate what can be stickered from what must be reprinted, with a specification carrying version number and expiry date.",
            "fr": "Vous avez un lot d'étiquettes à modifier ? Envoyez la maquette actuelle, les champs concernés et les marchés visés : nous distinguons ce qui peut être autocollé de ce qui doit être réimprimé, avec une spécification portant numéro de version et date de péremption.",
            "es": "¿Tienes un lote de etiquetas que hay que cambiar? Envía la maqueta actual, los campos afectados y los mercados destino: separamos lo que admite pegatina de lo que exige reimpresión, con una especificación con número de versión y fecha de caducidad.",
            "ja": "刷り直しや変更が必要な下げ札をお持ちですか。現行版面・変更する項目・対象市場をお送りいただければ、上貼りで済む項目と再印刷が必要な項目を分け、版番号と失効日を入れた仕様をご提案します。",
            "ko": "재인쇄나 변경이 필요한 행택이 있으신가요? 현재 판면, 변경할 항목, 대상 시장을 보내주시면 덧붙이기로 가능한 항목과 재인쇄가 필요한 항목을 구분해 버전 번호와 만료일이 있는 사양서를 제안합니다.",
        },
        {
            "zh": "索取吊牌改版評估 →",
            "en": "Request a tag revision review →",
            "fr": "Demander une revue de révision →",
            "es": "Solicitar revisión de cambio →",
            "ja": "下げ札改版の評価を依頼 →",
            "ko": "행택 변경 검토 요청 →",
        },
    )),
]
