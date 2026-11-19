# -*- coding: utf-8 -*-
"""2026-11-19 14:00 批次 A：牛皮紙吊牌（kraft hang tags）克重 / 印刷 / 環保聲明"""

SLUG = "kraft-hang-tags-guide"
CATEGORY = {
    "zh": "標籤與吊牌", "en": "Labels & Hang Tags", "fr": "Étiquettes",
    "es": "Etiquetas", "ja": "ネーム・下げ札", "ko": "라벨·행택",
}
TITLE = {
    "zh": "牛皮紙吊牌：克重、印刷與環保聲明 | TAGE",
    "en": "Kraft Hang Tags: GSM, Printing and Eco Claims | TAGE",
    "fr": "Étiquettes kraft : grammage, impression, allégations | TAGE",
    "es": "Etiquetas kraft: gramaje, impresión y alegaciones | TAGE",
    "ja": "クラフト紙の下げ札：坪量・印刷・環境表示 | TAGE",
    "ko": "크라프트 행택: 평량·인쇄·환경 표시 | TAGE",
}
DESC = {
    "zh": "牛皮紙吊牌怎麼定規格：300–450 g/m² 克重與挺度、本色紙上的發色與白墨打底、ΔE 控色、環保聲明能寫與不能寫，附採購單五欄位與四項驗收。",
    "en": "Specifying kraft hang tags: 300–450 g/m² GSM and stiffness, printing on unbleached stock, colour control, and the green claims that hold up under audit.",
    "fr": "Étiquettes kraft bien spécifiées : grammage 300–450 g/m², rigidité, impression sur papier écru, contrôle de teinte et allégations environnementales recevables.",
    "es": "Etiquetas kraft bien especificadas: gramaje 300–450 g/m², rigidez, impresión sobre papel crudo, control de color y alegaciones ambientales defendibles.",
    "ja": "クラフト紙の下げ札の仕様：坪量 300〜450 g/m² と剛度、生成り紙への印刷発色、ΔE による色管理、景品表示法を踏まえた環境表示まで整理します。",
    "ko": "크라프트 행택 사양 정리: 평량 300~450 g/m²와 강성, 미표백지 인쇄 발색, ΔE 색 관리, 표시광고법을 고려한 환경 표시까지 다룹니다.",
}
H1 = {
    "zh": "牛皮紙吊牌：克重、印刷與環保聲明",
    "en": "Kraft Paper Hang Tags: GSM, Print and Green Claims",
    "fr": "Étiquettes kraft : grammage, impression et allégations",
    "es": "Etiquetas kraft: gramaje, impresión y alegaciones",
    "ja": "クラフト紙の下げ札：坪量・印刷・環境表示",
    "ko": "크라프트 행택: 평량·인쇄·환경 표시",
}

BLOCKS = [
    ("p", {
        "zh": "牛皮紙吊牌看起來是最簡單的一種輔料：一張沒漂白的棕色紙，打一個孔，掛上去。實際上它是最容易在三個地方出錯的輔料——克重選低了，吊牌在貨架上兩天就捲邊；本色紙上直接印品牌色，紅色變磚紅、藍色變灰綠；把「環保」寫成一句沒有依據的宣傳語，遇到平台核查或客戶稽核時反而成了風險。本篇按克重、印刷、環保聲明三段講清楚，最後給採購單欄位與可量化的驗收項目。",
        "en": "A kraft hang tag looks like the simplest trim there is: unbleached brown board, one hole, hang it. In practice it is the trim where three things go wrong most often. GSM is chosen too low, so the tag curls on the rail within two days. Brand colours are printed straight onto brown stock, and red turns brick while blue turns grey-green. And eco credentials are written as a slogan with nothing behind them, which becomes a liability the moment a marketplace or a customer runs an audit. This guide covers GSM, printing and green claims, then gives the PO fields and the acceptance checks you can measure.",
        "fr": "Une étiquette kraft semble l'accessoire le plus simple qui soit : un carton brun non blanchi, un trou, on suspend. C'est en réalité celui où l'on se trompe le plus souvent, sur trois points. Un grammage trop faible et l'étiquette gondole sur le présentoir en deux jours. Des couleurs de marque imprimées à même le papier écru : le rouge vire brique, le bleu vire au gris-vert. Et des arguments écologiques rédigés comme un slogan sans preuve, qui deviennent un risque dès qu'une place de marché ou un client audite. Cet article traite grammage, impression et allégations, puis donne les champs du bon de commande et des contrôles mesurables.",
        "es": "Una etiqueta kraft parece el accesorio más simple: un cartón marrón sin blanquear, un ojal y a colgar. En la práctica es donde más se falla, y en tres puntos. Se elige un gramaje bajo y la etiqueta se comba en el expositor en dos días. Se imprime el color de marca directamente sobre papel crudo: el rojo se vuelve ladrillo y el azul, gris verdoso. Y se escriben credenciales ecológicas como eslogan sin respaldo, lo que se convierte en riesgo en cuanto un marketplace o un cliente audita. Esta guía cubre gramaje, impresión y alegaciones, y cierra con los campos del pedido y controles medibles.",
        "ja": "クラフト紙の下げ札は最も簡単な副資材に見えます。未晒しの茶色い板紙に穴を開けて掛けるだけ。しかし実際には、最も失敗しやすい副資材でもあります。坪量を低くすると、店頭で 2 日と持たずに反り返ります。生成りの紙にブランドカラーをそのまま刷ると、赤はレンガ色に、青は灰緑色になります。根拠のない「環境に優しい」というコピーは、モールや取引先の監査で一気にリスクになります。本稿では坪量・印刷・環境表示の 3 点を整理し、発注書の記載欄と数値で判定できる受入項目まで示します。",
        "ko": "크라프트 행택은 가장 단순한 부자재처럼 보입니다. 미표백 갈색 판지에 구멍 하나, 걸면 끝. 실제로는 가장 자주 실패하는 부자재입니다. 평량을 낮게 잡으면 매장에서 이틀 만에 말려 올라가고, 생성지에 브랜드 색을 그대로 인쇄하면 빨강은 벽돌색, 파랑은 회녹색이 됩니다. 근거 없는 '친환경' 문구는 마켓플레이스나 고객 감사에서 곧바로 리스크가 됩니다. 이 글은 평량·인쇄·환경 표시를 정리하고 발주서 기재 항목과 수치로 판정하는 검사 항목까지 제시합니다.",
    }),

    ("h2", {
        "zh": "一、克重與挺度：300 到 450 g/m² 的實際差別",
        "en": "1. GSM and Stiffness: What 300 to 450 g/m² Actually Feels Like",
        "fr": "1. Grammage et rigidité : ce que 300 à 450 g/m² change vraiment",
        "es": "1. Gramaje y rigidez: qué cambia de verdad entre 300 y 450 g/m²",
        "ja": "1. 坪量と剛度：300〜450 g/m² の実際の違い",
        "ko": "1. 평량과 강성: 300~450 g/m²의 실제 차이",
    }),

    ("table", (
        [
            {"zh": "克重", "en": "GSM", "fr": "Grammage", "es": "Gramaje", "ja": "坪量", "ko": "평량"},
            {"zh": "手感與挺度", "en": "Feel and stiffness", "fr": "Toucher et rigidité", "es": "Tacto y rigidez", "ja": "風合いと剛度", "ko": "촉감과 강성"},
            {"zh": "適用", "en": "Where it works", "fr": "Usage", "es": "Uso", "ja": "用途", "ko": "적용"},
            {"zh": "注意", "en": "The catch", "fr": "Limite", "es": "Objeción", "ja": "注意点", "ko": "주의점"},
        ],
        [
            [
                {"zh": "300 g/m²", "en": "300 g/m²", "fr": "300 g/m²", "es": "300 g/m²", "ja": "300 g/m²", "ko": "300 g/m²"},
                {"zh": "偏軟，可彎折", "en": "Soft, bends easily", "fr": "Souple, se plie", "es": "Blando, se dobla", "ja": "柔らかく折れやすい", "ko": "무르고 잘 휘어짐"},
                {"zh": "快時尚、電商內包裝吊牌", "en": "Fast fashion, e-commerce inner tags", "fr": "Mode rapide, étiquettes internes e-commerce", "es": "Moda rápida, etiquetas internas de e-commerce", "ja": "ファストファッション、EC 同梱の下げ札", "ko": "패스트패션, 이커머스 동봉 행택"},
                {"zh": "易捲邊，孔位需加強", "en": "Curls; reinforce the hole", "fr": "Gondole ; renforcer le trou", "es": "Se comba; refuerza el ojal", "ja": "反りやすい。穴を補強", "ko": "말림 발생, 구멍 보강 필요"},
            ],
            [
                {"zh": "350 g/m²", "en": "350 g/m²", "fr": "350 g/m²", "es": "350 g/m²", "ja": "350 g/m²", "ko": "350 g/m²"},
                {"zh": "通用，站得住", "en": "The default, holds shape", "fr": "Standard, tient sa forme", "es": "Estándar, mantiene forma", "ja": "汎用。形を保つ", "ko": "범용, 형태 유지"},
                {"zh": "大多數服裝吊牌", "en": "Most apparel hang tags", "fr": "La plupart des étiquettes suspendues", "es": "La mayoría de etiquetas colgantes", "ja": "大半の衣料用下げ札", "ko": "대부분의 의류 행택"},
                {"zh": "深色滿版印刷易見紙紋", "en": "Heavy dark ink shows the paper grain", "fr": "Les aplats foncés révèlent le grain", "es": "Los fondos oscuros muestran la fibra", "ja": "濃色ベタは紙の地合いが出る", "ko": "진한 전면 인쇄는 지질이 드러남"},
            ],
            [
                {"zh": "400 g/m²", "en": "400 g/m²", "fr": "400 g/m²", "es": "400 g/m²", "ja": "400 g/m²", "ko": "400 g/m²"},
                {"zh": "明顯硬挺，有份量", "en": "Clearly stiff, has weight", "fr": "Nettement rigide, de la tenue", "es": "Claramente rígido, con cuerpo", "ja": "明確に硬く、重量感がある", "ko": "확실히 뻣뻣하고 묵직함"},
                {"zh": "外貿客戶、百貨、禮盒吊牌", "en": "Export buyers, department stores, gift-box tags", "fr": "Acheteurs export, grands magasins, coffrets", "es": "Compradores de exportación, tiendas, cajas de regalo", "ja": "輸出バイヤー、百貨店、ギフトボックス", "ko": "수출 바이어, 백화점, 기프트박스"},
                {"zh": "模切邊緣易爆線，刀模要新", "en": "Edges crack on die-cutting; use a fresh die", "fr": "Bords qui éclatent à la découpe ; forme neuve", "es": "Bordes que se rompen al troquelar; cuchilla nueva", "ja": "抜き加工で端が割れる。型は新しいもの", "ko": "타발 모서리 갈라짐, 새 칼형 필요"},
            ],
            [
                {"zh": "450 g/m² 以上", "en": "450 g/m² and up", "fr": "450 g/m² et plus", "es": "450 g/m² o más", "ja": "450 g/m² 以上", "ko": "450 g/m² 이상"},
                {"zh": "接近薄卡紙，硬", "en": "Close to light card, hard", "fr": "Proche du carton léger, dur", "es": "Cerca del cartón ligero, duro", "ja": "薄手のカードに近い硬さ", "ko": "얇은 카드지에 가까운 경도"},
                {"zh": "精品主吊牌、牛皮紙禮盒配套", "en": "Premium main tags, gift-box sets", "fr": "Étiquettes premium, coffrets", "es": "Etiquetas premium, sets de regalo", "ja": "高級主札、ギフトボックス用", "ko": "프리미엄 메인 태그, 기프트박스 세트"},
                {"zh": "孔位必須打雞眼，否則撕孔", "en": "An eyelet is mandatory or the hole tears", "fr": "Œillet obligatoire, sinon le trou déchire", "es": "Ojal obligatorio o el agujero rompe", "ja": "ハトメ必須。なければ穴が破れる", "ko": "아일렛 필수, 없으면 구멍 찢어짐"},
            ],
        ],
    )),

    ("p", {
        "zh": "同樣標 350 g/m²，兩家供應商的挺度可以差一級，因為挺度取決於三件事：漿料（未漂白硫酸鹽漿比回收漿硬）、壓光程度、以及纖維方向。所以採購單上只寫克重不夠，要連紙種一起寫清楚；驗收時用 ISO 2493 彎曲挺度測試，取同一方向連續十張的離散度，比單張數值更能反映批次穩定性。",
        "en": "Two suppliers can both quote 350 g/m² and still deliver a full grade apart in stiffness, because stiffness depends on three things: pulp (unbleached kraft pulp is stiffer than recycled fibre), calendering, and fibre direction. Writing only GSM on the PO is not enough — name the paper grade too. At goods-in, run an ISO 2493 bending stiffness test and look at the spread across ten consecutive sheets in the same direction; scatter tells you more about batch consistency than any single reading.",
        "fr": "Deux fournisseurs peuvent annoncer 350 g/m² et livrer un cran de rigidité différent : celle-ci dépend de trois facteurs, la pâte (une pâte kraft non blanchie est plus rigide qu'une fibre recyclée), le calandrage et le sens des fibres. Indiquer seulement le grammage sur le bon de commande ne suffit pas : nommez aussi la qualité de papier. À la réception, mesurez la rigidité en flexion selon l'ISO 2493 et regardez la dispersion sur dix feuilles consécutives dans le même sens ; elle en dit plus que n'importe quelle valeur isolée.",
        "es": "Dos proveedores pueden cotizar 350 g/m² y entregar rigideces de un grado distinto: la rigidez depende de la pasta (la pasta kraft sin blanquear es más rígida que la fibra reciclada), del calandrado y de la dirección de la fibra. Poner solo el gramaje en el pedido no basta: nombra también la calidad del papel. En recepción, mide la rigidez al doblado según ISO 2493 y revisa la dispersión en diez hojas consecutivas en la misma dirección; dice más que una lectura aislada.",
        "ja": "同じ 350 g/m² でも、供給元によって剛度は 1 段階違うことがあります。剛度はパルプ（未晒しクラフトパルプは古紙パルプより硬い）、カレンダー処理、繊維方向の 3 つで決まるからです。発注書に坪量だけを書くのでは不十分で、紙質まで明記します。受入では ISO 2493 の曲げ剛性を測り、同方向の連続 10 枚のばらつきを見ます。ばらつきのほうが 1 枚の数値より批次の安定性を示します。",
        "ko": "같은 350 g/m²라도 공급사에 따라 강성이 한 단계 다를 수 있습니다. 강성은 펄프(미표백 크라프트 펄프가 재생 펄프보다 단단함), 캘린더링, 섬유 방향 세 가지로 결정됩니다. 발주서에 평량만 적으면 부족하고 지종까지 명기해야 합니다. 수입 검사에서는 ISO 2493 굽힘 강성을 측정하고 동일 방향 연속 10장의 산포를 봅니다. 산포가 단일 측정값보다 배치 안정성을 잘 보여줍니다.",
    }),

    ("h2", {
        "zh": "二、本色紙上的印刷：顏色為什麼會偏",
        "en": "2. Printing on Unbleached Stock: Why Colours Drift",
        "fr": "2. Impression sur papier écru : pourquoi les couleurs dérivent",
        "es": "2. Imprimir sobre papel crudo: por qué el color se desvía",
        "ja": "2. 生成り紙への印刷：色がずれる理由",
        "ko": "2. 생성지 인쇄: 색이 어긋나는 이유",
    }),

    ("p", {
        "zh": "沒漂白的牛皮紙底色本身就帶黃相與灰相，明度比白卡低一大截，油墨印上去等於隔著一層茶色玻璃看顏色：四色疊印的品牌紅會偏磚、品牌藍會偏灰綠、淺灰會直接消失。三種做法可以處理，選哪一種取決於品牌對顏色的容忍度與預算。",
        "en": "Unbleached kraft carries its own yellow-grey cast and sits well below white board in lightness, so ink behaves as if it were read through a sheet of brown glass: a four-colour brand red drifts brick, a brand blue drifts grey-green, and light greys disappear outright. There are three workable answers, and which one you choose depends on how tight the brand is on colour and on budget.",
        "fr": "Le kraft non blanchi a déjà sa propre dominante jaune-grise et une clarté bien inférieure au carton blanc : l'encre se comporte comme si on la regardait à travers une feuille ambrée. Un rouge de marque en quadrichromie dérive vers la brique, un bleu vers le gris-vert, et les gris clairs disparaissent purement et simplement. Trois solutions existent, le choix dépend de la tolérance de la marque et du budget.",
        "es": "El kraft sin blanquear ya trae su propio matiz amarillo-grisáceo y una luminosidad muy inferior al cartón blanco: la tinta se comporta como si se mirara a través de un cristal ambarino. Un rojo de marca en cuatricromía se va a ladrillo, un azul a gris verdoso y los grises claros desaparecen. Hay tres soluciones y la elección depende de la tolerancia de la marca al color y del presupuesto.",
        "ja": "未晒しクラフト紙はもともと黄味と灰味を持ち、白カードに比べて明度が大きく低いため、インキは茶色のガラス越しに見るのと同じ挙動になります。4 色プロセスのブランド赤はレンガ色に、青は灰緑に寄り、淡いグレーは消えます。対策は 3 通りで、どれを選ぶかはブランドの色許容度と予算で決まります。",
        "ko": "미표백 크라프트지는 자체적으로 황회색 기운이 있고 백판지보다 명도가 크게 낮아, 잉크가 갈색 유리를 통해 보는 것처럼 발색됩니다. 4도 브랜드 빨강은 벽돌색으로, 파랑은 회녹색으로 치우치고 연한 회색은 사라집니다. 세 가지 해법이 있고 브랜드의 색 허용도와 예산에 따라 선택합니다.",
    }),

    ("ul", [
        {
            "zh": "白墨打底＋四色：先印一到兩層白墨把底色蓋住，再上四色。成本增加約一到兩成，顏色最接近品牌稿，但白墨層厚時折線容易開裂。",
            "en": "White underprint plus CMYK: one or two hits of white to block the base, then process colour. Costs roughly 10–20% more and gets closest to the brand artwork, but a thick white layer cracks along folds.",
            "fr": "Sous-couche de blanc puis quadrichromie : une ou deux passes de blanc pour masquer le fond, puis la couleur. Surcoût d'environ 10 à 20 % et rendu le plus proche du fichier de marque, mais une couche de blanc épaisse fissure sur les plis.",
            "es": "Blanco de fondo más cuatricromía: una o dos pasadas de blanco para tapar el fondo y luego el color. Cuesta un 10–20 % más y es lo más cercano al arte de marca, pero una capa gruesa de blanco se agrieta en los pliegues.",
            "ja": "白下地＋プロセス 4 色：白を 1〜2 度刷って地色を隠してから 4 色を重ねます。コストは 1〜2 割増、ブランド原稿に最も近い発色ですが、白が厚いと折り目でひび割れます。",
            "ko": "백색 언더프린트+4도: 백색을 1~2회 인쇄해 바탕을 가린 뒤 4도를 올립니다. 비용은 10~20% 증가하고 브랜드 원안에 가장 가깝지만, 백색이 두꺼우면 접힌 선에서 갈라집니다.",
        },
        {
            "zh": "專色絲網印刷：一個顏色一個網版，墨層厚、遮蓋力強，深色底上的白與金特別穩。適合 1–2 色的簡約吊牌，色數一多成本上升很快。",
            "en": "Spot-colour screen printing: one screen per colour, a thick ink film and strong opacity — white and gold on brown are especially reliable. Ideal for one- or two-colour minimal tags; cost climbs fast beyond that.",
            "fr": "Sérigraphie en couleurs directes : un écran par couleur, film d'encre épais et fort pouvoir couvrant — blanc et or sur brun sont particulièrement fiables. Idéal pour une étiquette minimaliste à 1 ou 2 couleurs ; au-delà, le coût grimpe vite.",
            "es": "Serigrafía en colores directos: una pantalla por color, película gruesa y buen cubrimiento; el blanco y el oro sobre marrón son muy fiables. Ideal para etiquetas minimalistas de 1 o 2 colores; con más colores el costo sube rápido.",
            "ja": "特色インキのスクリーン印刷：色ごとに版を作り、インキ膜が厚く隠蔽力が高い。茶地の白や金が特に安定します。1〜2 色のミニマルな下げ札に向き、色数が増えるとコストが急に上がります。",
            "ko": "별색 스크린 인쇄: 색상별로 판을 만들어 잉크막이 두껍고 은폐력이 강합니다. 갈색 바탕의 흰색과 금색이 특히 안정적입니다. 1~2색 미니멀 행택에 적합하며 색수가 늘면 원가가 급격히 오릅니다.",
        },
        {
            "zh": "順色設計：不試圖遮住底色，改用深棕、墨黑、米白或金屬色，讓紙的顏色成為設計的一部分。成本最低、最耐看，也是目前精品線最常用的做法。",
            "en": "Design with the stock: stop fighting the base and use deep brown, ink black, off-white or metallics so the paper becomes part of the design. Cheapest, most durable look, and the current default for premium lines.",
            "fr": "Jouer avec le support : plutôt que de masquer le fond, utiliser brun profond, noir d'encre, blanc cassé ou métallisé pour que le papier fasse partie du dessin. Le moins cher, le plus durable dans le temps, et le choix courant des gammes premium.",
            "es": "Diseñar con el soporte: en vez de tapar el fondo, usar marrón profundo, negro tinta, blanco roto o metalizados para que el papel forme parte del diseño. Lo más barato, lo más duradero y el criterio habitual en líneas premium.",
            "ja": "地色を活かす設計：地を隠すのをやめ、濃茶・墨黒・生成り・金属色で組んで紙の色をデザインの一部にします。最も低コストで経年で見劣りせず、現在の高級ラインの定番です。",
            "ko": "바탕색을 살린 디자인: 바탕을 가리는 대신 진한 갈색, 먹색, 미색, 금속색으로 구성해 종이색을 디자인의 일부로 씁니다. 가장 저렴하고 오래 보기 좋으며, 현재 프리미엄 라인의 기본 방식입니다.",
        },
    ]),

    ("callout", {
        "zh": "打樣規則：牛皮紙的色樣必須用同一批紙打，且在標準光源下對色。品牌色允差 ΔE ≤ 1.5、一般色 ΔE ≤ 2.0；同時要求供應商留存批次紙樣，因為牛皮紙批次之間的底色差本身就可能有 ΔE 1 左右，換批不重新對色就會出現「同一款吊牌兩個顏色」。",
        "en": "Proofing rule: kraft must be proofed on the same paper batch and judged under a standard light source. Hold brand colours to ΔE ≤ 1.5 and general colours to ΔE ≤ 2.0, and have the supplier keep a retained sheet per batch — kraft base colour alone can vary by around ΔE 1 between lots, so skipping re-approval gives you two colours of the same tag.",
        "fr": "Règle d'épreuve : le kraft se valide sur le même lot de papier et sous une source lumineuse normalisée. Tolérance ΔE ≤ 1,5 pour les couleurs de marque, ΔE ≤ 2,0 pour les autres, et conservation d'une feuille témoin par lot — la teinte du support varie d'environ ΔE 1 d'un lot à l'autre : sans nouvelle validation, on obtient deux couleurs pour une même étiquette.",
        "es": "Regla de prueba: el kraft se aprueba sobre el mismo lote de papel y bajo fuente de luz normalizada. Tolerancia ΔE ≤ 1,5 para colores de marca y ΔE ≤ 2,0 para el resto, y guardar una hoja testigo por lote — el tono del soporte varía alrededor de ΔE 1 entre lotes, así que sin reaprobar salen dos colores de la misma etiqueta.",
        "ja": "校正の原則：クラフト紙は同一ロットの紙で校正し、標準光源で判定します。ブランド色は ΔE ≤ 1.5、一般色は ΔE ≤ 2.0 を許容し、ロットごとに見本紙を保管します。クラフト紙はロット間で地色が ΔE 1 程度変わるため、再承認を省くと「同じ下げ札が 2 色」になります。",
        "ko": "교정 원칙: 크라프트지는 같은 로트의 종이로 교정하고 표준 광원에서 판정합니다. 브랜드 색은 ΔE ≤ 1.5, 일반 색은 ΔE ≤ 2.0을 허용하고 로트별 견본지를 보관합니다. 크라프트지는 로트 간 바탕색이 ΔE 1 정도 달라져 재승인을 생략하면 같은 행택이 두 색이 됩니다.",
    }),

    ("h2", {
        "zh": "三、環保聲明：能寫與不能寫",
        "en": "3. Green Claims: What You Can and Cannot Print",
        "fr": "3. Allégations environnementales : ce qui passe et ce qui ne passe pas",
        "es": "3. Alegaciones ambientales: lo que se puede imprimir y lo que no",
        "ja": "3. 環境表示：書けること・書けないこと",
        "ko": "3. 환경 표시: 쓸 수 있는 것과 없는 것",
    }),

    ("p", {
        "zh": "吊牌是最容易被寫上環保口號的地方，也是審核時最先被翻出來看的地方。歐洲市場目前按兩條線看：一是誤導性宣傳（各國消費者法，法國由 Code de la consommation 規範，西班牙由 Ley 7/2022 與消費者保護法規規範），二是包裝與產品的具體義務（Règlement (UE) 2025/40 即 PPWR、GPSR (EU) 2023/988 的責任主體與可追溯資訊）。原則很簡單：每一句環保聲明，都要能指回一張證書、一個測試報告或一個可計算的數字。",
        "en": "The hang tag is where green slogans get printed, and it is the first thing an auditor reads. Europe currently looks at two lines: misleading claims (consumer law — in France the Code de la consommation, in Spain Ley 7/2022 and consumer protection rules) and concrete packaging/product duties (Regulation (EU) 2025/40, the PPWR, plus GPSR (EU) 2023/988 on the responsible operator and traceability). The principle is simple: every environmental statement must point back to a certificate, a test report or a number you can calculate.",
        "fr": "L'étiquette suspendue est l'endroit où l'on imprime les slogans verts, et le premier document qu'un auditeur lit. L'Europe regarde aujourd'hui deux axes : les allégations trompeuses (droit de la consommation — en France le Code de la consommation, en Espagne la Ley 7/2022 et les règles de protection des consommateurs) et les obligations concrètes sur les emballages et produits (règlement (UE) 2025/40, le PPWR, ainsi que le GPSR (UE) 2023/988 sur le responsable et la traçabilité). Le principe est simple : chaque allégation doit renvoyer à un certificat, un rapport d'essai ou un chiffre calculable.",
        "es": "La etiqueta colgante es donde se imprimen los eslóganes verdes y lo primero que lee un auditor. Europa mira hoy dos frentes: la publicidad engañosa (derecho de consumo — en Francia el Code de la consommation, en España la Ley 7/2022 y la normativa de protección de consumidores) y las obligaciones concretas de envases y producto (Reglamento (UE) 2025/40, el PPWR, y el GPSR (UE) 2023/988 sobre responsable y trazabilidad). El principio es simple: cada alegación debe remitir a un certificado, un informe de ensayo o un número calculable.",
        "ja": "下げ札は環境コピーを刷る場所であり、監査で最初に読まれる文書でもあります。欧州は現在 2 つの軸で見ます。1 つは誤認を招く表示（各国の消費者法。フランスは Code de la consommation、スペインは Ley 7/2022 と消費者保護法規）、もう 1 つは包装・製品の具体的義務（規則 (EU) 2025/40＝PPWR、GPSR (EU) 2023/988 の責任者とトレーサビリティ）。原則は単純で、あらゆる環境表示は証明書・試験報告・計算できる数値に紐づく必要があります。日本では景品表示法が優良誤認を禁じており、紙の配合率や古紙率を示す場合は品質表示として裏付けが求められます。",
        "ko": "행택은 친환경 문구를 인쇄하는 자리이자 감사에서 가장 먼저 읽히는 문서입니다. 유럽은 현재 두 축으로 봅니다. 하나는 오인 표시(각국 소비자법)이고, 다른 하나는 포장·제품의 구체적 의무(규정 (EU) 2025/40, PPWR, 그리고 GPSR (EU) 2023/988의 책임자·추적 정보)입니다. 원칙은 단순합니다. 모든 환경 표시는 인증서, 시험 성적서, 계산 가능한 수치로 되돌아가야 합니다. 한국에서는 표시광고법이 사실과 다른 환경 표시를 금지하며, 재생 원료 비율을 적을 때는 그 근거를 함께 보관해야 합니다.",
    }),

    ("table", (
        [
            {"zh": "想寫的聲明", "en": "Claim you want", "fr": "Allégation visée", "es": "Alegación deseada", "ja": "書きたい表示", "ko": "쓰고 싶은 표시"},
            {"zh": "站得住的前提", "en": "What makes it defensible", "fr": "Ce qui la rend défendable", "es": "Qué la hace defendible", "ja": "成立させる条件", "ko": "성립 조건"},
            {"zh": "不建議的寫法", "en": "Wording to avoid", "fr": "Formulation à éviter", "es": "Redacción a evitar", "ja": "避けたい書き方", "ko": "피해야 할 표현"},
        ],
        [
            [
                {"zh": "含回收成分", "en": "Contains recycled content", "fr": "Contient des matières recyclées", "es": "Contiene material reciclado", "ja": "再生原料を使用", "ko": "재생 원료 사용"},
                {"zh": "寫出具體比例與依據（供應商聲明＋批次）", "en": "State the percentage and its basis — supplier declaration plus batch record", "fr": "Indiquer le pourcentage et sa base : déclaration fournisseur + traçabilité du lot", "es": "Indicar porcentaje y base: declaración del proveedor más registro de lote", "ja": "比率と根拠（供給元の宣言＋ロット記録）を併記", "ko": "비율과 근거(공급사 선언+로트 기록)를 함께 표기"},
                {"zh": "只寫「環保紙」", "en": "Just writing eco paper", "fr": "Écrire simplement papier écologique", "es": "Escribir solo papel ecológico", "ja": "「エコ紙」だけを書く", "ko": "'친환경지'만 표기"},
            ],
            [
                {"zh": "FSC 認證", "en": "FSC certified", "fr": "Certifié FSC", "es": "Certificado FSC", "ja": "FSC 認証", "ko": "FSC 인증"},
                {"zh": "有效的證書號與 CoC 範圍內，且吊牌本身在範圍內", "en": "A valid licence code, within the CoC scope, covering this product", "fr": "Licence valide, dans le périmètre CoC couvrant ce produit", "es": "Licencia válida, dentro del alcance CoC que cubre este producto", "ja": "有効なライセンス番号と、本製品を対象とする CoC 範囲", "ko": "유효 라이선스 번호와 본 제품을 포함하는 CoC 범위"},
                {"zh": "貼別家供應商的 FSC 標", "en": "Borrowing another supplier's FSC mark", "fr": "Emprunter la marque FSC d'un autre fournisseur", "es": "Usar el sello FSC de otro proveedor", "ja": "他社の FSC マークを流用", "ko": "다른 공급사 FSC 마크 차용"},
            ],
            [
                {"zh": "可回收", "en": "Recyclable", "fr": "Recyclable", "es": "Reciclable", "ja": "リサイクル可能", "ko": "재활용 가능"},
                {"zh": "說明實際回收路徑與處理方式（例如與紙板一起回收，不含塑膠膜）", "en": "Name the real collection route — e.g. with cardboard, no plastic film", "fr": "Nommer la filière réelle : avec le carton, sans film plastique", "es": "Nombrar la vía real: con cartón, sin film plástico", "ja": "実際の回収経路（段ボールと一緒、プラなし）を示す", "ko": "실제 수거 경로(골판지와 함께, 플라스틱 필름 없음)를 명시"},
                {"zh": "整張吊牌覆膜後仍寫「100% 可回收」", "en": "Laminating the whole tag and still claiming 100% recyclable", "fr": "Pelliculer toute l'étiquette et écrire 100 % recyclable", "es": "Laminar toda la etiqueta y escribir 100 % reciclable", "ja": "全体をラミネートして「100% リサイクル可能」と書く", "ko": "전체 라미네이트 후 '100% 재활용 가능' 표기"},
            ],
            [
                {"zh": "可分解 / 可堆肥", "en": "Biodegradable or compostable", "fr": "Biodégradable ou compostable", "es": "Biodegradable o compostable", "ja": "生分解性・堆肥化可能", "ko": "생분해·퇴비화 가능"},
                {"zh": "有相應標準的測試報告與認證（如工業堆肥認證），並註明條件", "en": "A test report and certificate against the relevant standard, with conditions stated", "fr": "Rapport d'essai et certificat selon la norme applicable, conditions précisées", "es": "Informe y certificado según la norma aplicable, con condiciones indicadas", "ja": "該当規格の試験報告と認証、条件の明記", "ko": "해당 규격 시험 성적서와 인증, 조건 명기"},
                {"zh": "對紙張隨口寫「可分解」", "en": "Dropping biodegradable on paper without evidence", "fr": "Écrire biodégradable sur du papier sans preuve", "es": "Poner biodegradable en papel sin prueba", "ja": "根拠なく紙に「生分解性」と書く", "ko": "근거 없이 종이에 '생분해' 표기"},
            ],
        ],
    )),

    ("p", {
        "zh": "還有一條容易漏的：吊牌上的法定資訊本身就要佔位置。出口歐盟的服裝吊牌通常要放進口商或責任主體、原產地；法國市場的消費者資訊須以法語呈現（Code de la consommation 的要求），西班牙語市場同理。把這些欄位在刀模階段就排在背面的下方，不要等到印前才發現正面已經沒有地方，最後縮到 6 pt 以下沒人看得清。",
        "en": "One more point that gets missed: the mandatory information on the tag needs space of its own. Tags for the EU usually have to carry the importer or responsible operator and the country of origin; consumer information for the French market must appear in French, as the Code de la consommation requires, and Spanish-language markets expect the same treatment. Reserve those fields at the die-line stage on the back, low down — otherwise you discover at pre-press that the front has no room and end up at 6 pt, which nobody can read.",
        "fr": "Un point souvent oublié : les mentions obligatoires occupent de la place. Une étiquette destinée à l'UE porte généralement l'importateur ou le responsable et l'origine ; pour le marché français, l'information du consommateur doit être en français (exigence du Code de la consommation), et les marchés hispanophones attendent la même chose. Réservez ces zones dès le tracé de découpe, en bas du verso : sinon vous découvrez avant impression que le recto n'a plus de place et vous finissez à 6 pt, illisible.",
        "es": "Un punto que se olvida: la información obligatoria ocupa espacio propio. Una etiqueta para la UE suele llevar el importador o responsable y el país de origen; para el mercado francés la información al consumidor debe estar en francés (exigencia del Code de la consommation) y los mercados hispanohablantes esperan lo mismo. Reserva esos campos desde el trazado de troquel, en la parte baja del reverso; si no, en preprensa descubres que el frente no tiene sitio y acabas en 6 pt, ilegible.",
        "ja": "見落としやすい点がもう 1 つあります。法定情報には専用の場所が必要です。EU 向けの下げ札には通常、輸入者または責任者と原産地を入れます。フランス市場では消費者向け情報をフランス語で示す必要があり（Code de la consommation の要求）、スペイン語圏も同様です。これらの欄は抜き型の段階で裏面下部に確保してください。印刷直前になって表面に余白がないと気づき、6 pt まで縮めて誰も読めない、という事故になります。",
        "ko": "놓치기 쉬운 점이 하나 더 있습니다. 법정 정보는 전용 공간이 필요합니다. EU향 행택에는 보통 수입자 또는 책임자와 원산지를 넣습니다. 프랑스 시장은 소비자 정보를 프랑스어로 표시해야 하고(Code de la consommation 요구), 스페인어권도 같습니다. 이 항목은 칼선 단계에서 뒷면 하단에 확보하세요. 인쇄 직전에 앞면 여백이 없다는 걸 알게 되면 6 pt로 줄여 아무도 읽지 못하게 됩니다.",
    }),

    ("h2", {
        "zh": "四、採購單要寫的五個欄位",
        "en": "4. Five Fields for the Purchase Order",
        "fr": "4. Cinq champs à inscrire au bon de commande",
        "es": "4. Cinco campos para el pedido",
        "ja": "4. 発注書に書くべき 5 項目",
        "ko": "4. 발주서에 적어야 할 5개 항목",
    }),

    ("ul", [
        {
            "zh": "克重與紙種：例如「350 g/m² 未漂白牛皮紙，原生漿，單面壓光」，不要只寫「牛皮紙」。",
            "en": "GSM plus paper grade, e.g. 350 g/m² unbleached kraft, virgin pulp, one-side calendered — not simply kraft paper.",
            "fr": "Grammage et qualité : par exemple 350 g/m² kraft non blanchi, pâte vierge, calandré une face — pas seulement « papier kraft ».",
            "es": "Gramaje y calidad: por ejemplo 350 g/m² kraft sin blanquear, pasta virgen, calandrado una cara; no solo papel kraft.",
            "ja": "坪量と紙質：例「350 g/m² 未晒しクラフト、バージンパルプ、片面カレンダー」。単に「クラフト紙」と書かない。",
            "ko": "평량과 지종: 예 '350 g/m² 미표백 크라프트, 천연 펄프, 단면 캘린더'. '크라프트지'만 적지 않습니다.",
        },
        {
            "zh": "底色基準：提供紙樣或指定 L*a*b* 範圍，並註明允差與換批重新確認的規則。",
            "en": "Base colour reference: supply a paper swatch or an L*a*b* window, with tolerance and a re-approval rule for lot changes.",
            "fr": "Référence de teinte du support : fournir un échantillon ou une fenêtre L*a*b*, avec tolérance et règle de revalidation à chaque changement de lot.",
            "es": "Referencia de tono del soporte: muestra de papel o ventana L*a*b*, con tolerancia y regla de reaprobación por cambio de lote.",
            "ja": "地色基準：紙見本か L*a*b* の範囲を指定し、許容差とロット変更時の再承認ルールを明記。",
            "ko": "바탕색 기준: 지견본 또는 L*a*b* 범위를 지정하고 허용차와 로트 변경 시 재승인 규칙을 명기.",
        },
        {
            "zh": "印刷方式與色數：寫清是白墨打底的四色、專色絲印，或單色順色，並附色號（Pantone 或 ΔE 目標）。",
            "en": "Print method and colour count: white-underprint CMYK, spot screen, or single-colour printing, with the colour reference (Pantone or ΔE target).",
            "fr": "Mode d'impression et nombre de couleurs : quadri sur sous-couche blanche, sérigraphie directe ou monochrome, avec la référence (Pantone ou cible ΔE).",
            "es": "Método de impresión y número de colores: cuatricromía sobre blanco, serigrafía directa o monocromo, con referencia (Pantone u objetivo ΔE).",
            "ja": "印刷方式と色数：白下地の 4 色か、特色スクリーンか、単色か。色番（Pantone または ΔE 目標）を併記。",
            "ko": "인쇄 방식과 색수: 백색 바탕 4도, 별색 스크린, 단색 중 무엇인지와 색 기준(Pantone 또는 ΔE 목표)을 함께 기재.",
        },
        {
            "zh": "表面處理：本項目常被漏寫。無處理、水性上光、局部 UV、燙金、覆膜，五種手感與回收性都不同，價格也不同。",
            "en": "Surface finish, the field most often omitted: none, aqueous coating, spot UV, foil, lamination — five different feels, five different recyclability stories, five prices.",
            "fr": "Finition de surface, le champ le plus souvent oublié : aucune, vernis aqueux, UV sélectif, dorure, pelliculage — cinq touchers, cinq profils de recyclabilité, cinq prix.",
            "es": "Acabado superficial, el campo que más se omite: ninguno, barniz acuoso, UV selectivo, foil, laminado; cinco tactos, cinco perfiles de reciclabilidad y cinco precios.",
            "ja": "表面処理：最も抜けやすい欄です。なし、水系ニス、部分 UV、箔押し、ラミネートの 5 種で、風合い・リサイクル性・価格がそれぞれ違います。",
            "ko": "표면 처리: 가장 자주 빠지는 항목입니다. 무처리, 수성 코팅, 부분 UV, 박, 라미네이트 — 촉감과 재활용성, 가격이 모두 다릅니다.",
        },
        {
            "zh": "孔位與配件：孔徑、位置、是否加雞眼、配什麼掛繩。孔位距邊至少 8 mm，否則拉力一大就從邊緣撕開。",
            "en": "Hole and hardware: diameter, position, whether an eyelet is used, and which cord. Keep the hole at least 8 mm from the edge or the first hard pull tears through.",
            "fr": "Trou et accessoires : diamètre, position, œillet ou non, type de cordon. Laissez au moins 8 mm entre le trou et le bord, sinon la première traction déchire.",
            "es": "Ojal y accesorios: diámetro, posición, si lleva ojal metálico y qué cordón. Deja al menos 8 mm del borde o el primer tirón rompe.",
            "ja": "穴と付属品：穴径・位置・ハトメの有無・紐の種類。穴は端から最低 8 mm 離します。さもないと強い引張りで端から破れます。",
            "ko": "구멍과 부속: 구멍 지름, 위치, 아일렛 여부, 끈 종류. 구멍은 가장자리에서 최소 8 mm 띄우세요. 그렇지 않으면 강한 인장에 가장자리가 찢어집니다.",
        },
    ]),

    ("h2", {
        "zh": "五、驗收：四個可以量化的項目",
        "en": "5. Acceptance: Four Measurable Checks",
        "fr": "5. Réception : quatre contrôles mesurables",
        "es": "5. Recepción: cuatro controles medibles",
        "ja": "5. 受入：数値で判定できる 4 項目",
        "ko": "5. 수입 검사: 수치로 판정하는 4개 항목",
    }),

    ("ul", [
        {
            "zh": "克重：隨機取 10 張稱重換算，允差一般 ±5%；超出就說明紙廠或供應商換了紙。",
            "en": "GSM: weigh ten random tags and convert; ±5% is the normal tolerance, and anything beyond it means the paper changed.",
            "fr": "Grammage : peser dix étiquettes au hasard et convertir ; la tolérance usuelle est de ±5 %, au-delà le papier a changé.",
            "es": "Gramaje: pesar diez etiquetas al azar y convertir; la tolerancia habitual es ±5 %, más allá significa que cambió el papel.",
            "ja": "坪量：無作為に 10 枚を計量して換算。通常 ±5 % を許容し、超えたら紙が変わっています。",
            "ko": "평량: 무작위 10장을 계량해 환산합니다. 보통 ±5%를 허용하며 초과하면 종이가 바뀐 것입니다.",
        },
        {
            "zh": "挺度：同方向連續 10 張做彎曲測試，看平均與離散度；離散度大於 10% 說明批次混料。",
            "en": "Stiffness: bend ten consecutive pieces in the same direction and look at the mean and the spread; a spread above 10% means mixed stock.",
            "fr": "Rigidité : essai de flexion sur dix pièces consécutives dans le même sens, moyenne et dispersion ; au-delà de 10 % de dispersion, les lots sont mélangés.",
            "es": "Rigidez: ensayo de doblado en diez piezas consecutivas en la misma dirección, media y dispersión; más de 10 % indica lotes mezclados.",
            "ja": "剛度：同方向の連続 10 枚で曲げ試験。平均とばらつきを見て、ばらつきが 10 % を超えたら混批です。",
            "ko": "강성: 동일 방향 연속 10장으로 굽힘 시험. 평균과 산포를 보며 산포가 10%를 넘으면 혼합 로트입니다.",
        },
        {
            "zh": "色差：與批核樣比對，品牌色 ΔE ≤ 1.5、一般色 ΔE ≤ 2.0；深色滿版另做摩擦測試。",
            "en": "Colour: compare against the approved sample — ΔE ≤ 1.5 for brand colours, ΔE ≤ 2.0 for the rest; run a rub test on heavy dark solids.",
            "fr": "Couleur : comparer à l'échantillon approuvé — ΔE ≤ 1,5 pour les couleurs de marque, ΔE ≤ 2,0 sinon ; test de frottement sur les aplats foncés.",
            "es": "Color: comparar con la muestra aprobada — ΔE ≤ 1,5 para colores de marca y ΔE ≤ 2,0 para el resto; ensayo de frote en fondos oscuros.",
            "ja": "色差：承認見本と比較し、ブランド色 ΔE ≤ 1.5、一般色 ΔE ≤ 2.0。濃色ベタは摩擦試験も実施。",
            "ko": "색차: 승인 견본과 비교해 브랜드 색 ΔE ≤ 1.5, 일반 색 ΔE ≤ 2.0. 진한 전면 인쇄는 마찰 시험도 실시.",
        },
        {
            "zh": "捲曲與含水率：在 38 ℃／90% RH 放置 24 小時後看邊緣翹起高度，超過 3 mm 就說明紙張含水率或壓光不足。",
            "en": "Curl and moisture: condition at 38 °C / 90% RH for 24 hours and measure edge lift; above 3 mm points to moisture content or insufficient calendering.",
            "fr": "Gondolement et humidité : conditionner 24 h à 38 °C / 90 % HR et mesurer le relevé des bords ; au-delà de 3 mm, teneur en eau ou calandrage insuffisant.",
            "es": "Comba y humedad: acondicionar 24 h a 38 °C / 90 % HR y medir el levantamiento del borde; más de 3 mm indica humedad o calandrado insuficiente.",
            "ja": "反りと含水率：38 ℃／90 % RH で 24 時間養生し、端の浮きを測定。3 mm を超えたら含水率かカレンダー不足です。",
            "ko": "말림과 함수율: 38 ℃/90% RH에서 24시간 조습 후 가장자리 들뜸을 측정합니다. 3 mm를 넘으면 함수율이나 캘린더링 부족입니다.",
        },
    ]),

    ("p", {
        "zh": "把這四項寫進採購單的驗收欄，牛皮紙吊牌就從「憑感覺收貨」變成可以對話的規格。順帶一個常被忽略的成本點：牛皮紙的紙價波動比白卡小，但單價低不代表總價低——挺度不足時要靠加厚或覆膜補救，兩者都會把省下來的錢吃回去。",
        "en": "Put these four items in the acceptance block of the PO and kraft tags stop being a goods-in judgement call. One cost point that is easy to miss: kraft board prices move less than white board, but a lower unit price is not a lower total — if stiffness falls short you fix it with a heavier grade or lamination, and both eat the saving.",
        "fr": "Inscrits dans le bloc réception du bon de commande, ces quatre points transforment l'étiquette kraft en spécification discutable. Un point de coût souvent oublié : le cours du kraft bouge moins que celui du carton blanc, mais un prix unitaire plus bas n'est pas un coût total plus bas — si la rigidité manque, on compense par un grammage supérieur ou un pelliculage, et l'économie disparaît.",
        "es": "Con estos cuatro puntos en el bloque de recepción, la etiqueta kraft deja de ser un criterio de olfato. Un punto de costo que se olvida: el precio del kraft se mueve menos que el del cartón blanco, pero un precio unitario menor no es un costo total menor — si falta rigidez se compensa con más gramaje o laminado, y el ahorro se esfuma.",
        "ja": "この 4 項目を発注書の受入欄に書けば、クラフト紙の下げ札は「勘で受ける」対象ではなく話し合える仕様になります。見落としやすいコスト点も 1 つ。クラフト紙は白カードより市況の振れが小さいものの、単価が安い＝総コストが安いではありません。剛度が足りなければ坪量を上げるかラミネートで補い、その分で差額は消えます。",
        "ko": "이 네 항목을 발주서 검사란에 적으면 크라프트 행택은 '감으로 받는' 품목이 아니라 협의 가능한 사양이 됩니다. 놓치기 쉬운 원가 포인트도 있습니다. 크라프트지는 백판지보다 시세 변동이 작지만 단가가 낮다고 총원가가 낮은 것은 아닙니다. 강성이 부족하면 평량을 올리거나 라미네이트로 보강해야 하고, 그 비용이 절감분을 상쇄합니다.",
    }),

    ("related", [
        ("hang-tag-paper-types.html", {
            "zh": "吊牌紙張怎麼選：白卡、銅版、牛皮與特種紙",
            "en": "Hang tag paper types: white card, art paper, kraft and specialty stocks",
            "fr": "Papiers pour étiquettes : carte blanche, couché, kraft, spéciaux",
            "es": "Papeles para etiquetas: cartulina, estucado, kraft y especiales",
            "ja": "下げ札の用紙選び：白カード・コート・クラフト・特殊紙",
            "ko": "행택 용지 선택: 백판지·아트지·크라프트·특수지",
        }),
        ("fsc-certified-hang-tags.html", {
            "zh": "FSC 認證吊牌：證書範圍、CoC 與實際做法",
            "en": "FSC certified hang tags: licence scope, CoC and how it actually works",
            "fr": "Étiquettes FSC : périmètre de licence, CoC et pratique réelle",
            "es": "Etiquetas FSC: alcance de licencia, CoC y práctica real",
            "ja": "FSC 認証の下げ札：ライセンス範囲・CoC・実際の運用",
            "ko": "FSC 인증 행택: 라이선스 범위·CoC·실무",
        }),
        ("hang-tag-lamination-guide.html", {
            "zh": "吊牌覆膜：亮膜、霧膜與觸感膜的差別",
            "en": "Hang tag lamination: gloss, matt and soft-touch film compared",
            "fr": "Pelliculage d'étiquettes : brillant, mat et soft touch",
            "es": "Laminado de etiquetas: brillo, mate y soft touch",
            "ja": "下げ札のラミネート：光沢・マット・ソフトタッチ",
            "ko": "행택 라미네이트: 광택·무광·소프트터치",
        }),
    ]),

    ("cta", (
        {
            "zh": "正在做牛皮紙吊牌，但不確定克重夠不夠、品牌色在棕紙上會偏到什麼程度？把尺寸、克重與品牌色號發給我們，我們用同一批紙打一份實物樣並附對色數據。",
            "en": "Working on kraft tags and unsure whether the GSM is enough, or how far the brand colour will drift on brown stock? Send the size, GSM and colour reference and we will proof on the same paper batch with colour data attached.",
            "fr": "Vous travaillez sur des étiquettes kraft sans savoir si le grammage suffit, ni à quel point la couleur de marque dérive sur papier brun ? Envoyez dimensions, grammage et référence couleur : nous validons sur le même lot avec les données colorimétriques.",
            "es": "¿Estás haciendo etiquetas kraft sin saber si el gramaje alcanza, ni cuánto derivará el color de marca sobre papel marrón? Envíanos medida, gramaje y referencia de color: probamos sobre el mismo lote con datos colorimétricos.",
            "ja": "クラフト紙の下げ札で、坪量が足りるか、ブランド色が茶紙でどれだけ動くか不安な場合。サイズ・坪量・色番をご連絡ください。同一ロットで実物校正し、測色データを添えてお返しします。",
            "ko": "크라프트 행택을 준비 중인데 평량이 충분한지, 브랜드 색이 갈색 종이에서 얼마나 달라질지 불확실하신가요? 크기, 평량, 색 기준을 보내주시면 동일 로트로 실물 교정하고 측색 데이터를 함께 드립니다.",
        },
        {
            "zh": "索取牛皮紙吊牌打樣 →", "en": "Request a kraft tag proof →",
            "fr": "Demander une épreuve kraft →", "es": "Solicitar prueba kraft →",
            "ja": "クラフト下げ札の校正を依頼 →", "ko": "크라프트 행택 교정 요청 →",
        },
    )),
]
