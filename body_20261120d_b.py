# -*- coding: utf-8 -*-
"""2026-11-20 20:00 批次 B：吊牌下單數量規劃（每件張數、備品率、補印成本）。英文主稿。"""

SLUG = "hang-tag-quantity-planning-guide"
CATEGORY = {
    "zh": "採購與成本", "en": "Sourcing & Cost", "fr": "Achats et coûts",
    "es": "Compras y costes", "ja": "調達・コスト", "ko": "구매·원가",
}
TITLE = {
    "zh": "吊牌下單數量怎麼算：每件張數、備品率與補印成本 | TAGE",
    "en": "How Many Hang Tags to Order: Per-Garment Count, Spares and Reprints | TAGE",
    "fr": "Combien d'étiquettes pendantes commander : ratio, stock de sécurité, réimpression | TAGE",
    "es": "Cuántas etiquetas colgantes pedir: ratio por prenda, reserva y reimpresión | TAGE",
    "ja": "下げ札の発注数量の決め方：1 着あたり枚数・予備率・再印刷 | TAGE",
    "ko": "행택 발주 수량 계산: 착당 매수·예비율·재인쇄 | TAGE",
}
DESC = {
    "zh": "吊牌要下多少張？從服裝件數、尺碼配比與備品率算出基數，再加上打樣與拍攝用量，並用補印成本決定要不要湊下一個價格級距。",
    "en": "How many hang tags to order: build the count from garment quantity, size ratio and spare rate, add sampling, then use reprint cost to pick a price break.",
    "fr": "Combien d'étiquettes pendantes commander ? Base calculée sur les pièces, la répartition des tailles et un stock de sécurité, plus échantillons et shootings.",
    "es": "¿Cuántas etiquetas colgantes pedir? Base a partir de prendas, reparto de tallas y reserva, más muestras y sesiones, y el coste de reimpresión.",
    "ja": "下げ札は何枚発注するのか。縫製品の枚数・サイズ構成・予備率から基礎数を出し、サンプルと撮影分を加え、再印刷コストで単価区切りを判断します。",
    "ko": "행택을 몇 장 발주할까요? 의류 수량, 사이즈 구성, 예비율로 기준 수량을 만들고 샘플·촬영분을 더한 뒤 재인쇄 비용으로 가격 구간을 정합니다.",
}
H1 = {
    "zh": "吊牌下單數量怎麼算：每件張數、備品率與補印成本",
    "en": "How Many Hang Tags to Order: Per-Garment Count, Spares and Reprint Cost",
    "fr": "Combien d'étiquettes pendantes commander : ratio par pièce, stock de sécurité et coût de réimpression",
    "es": "Cuántas etiquetas colgantes pedir: ratio por prenda, reserva y coste de reimpresión",
    "ja": "下げ札の発注数量：1 着あたり枚数・予備率・再印刷コスト",
    "ko": "행택 발주 수량: 착당 매수·예비율·재인쇄 비용",
}

BLOCKS = [
    ("p", {
        "zh": "吊牌數量算錯，兩種後果都很貴。算少了，生產尾段沒有吊牌可掛，服裝要嘛延後出貨，要嘛無吊牌出貨——後者是合規問題，不是成本問題。算多了，季節結束剩下一堆印著舊系列名的吊牌，只能報廢。這篇把數量拆成四個加項、一個乘項，並給一個可以直接套的算例：10,000 件的訂單，最後下單 12,000 張。",
        "en": "Getting the hang tag quantity wrong is expensive in both directions. Too few and the last production days have nothing to attach: the shipment either waits or leaves unlabelled, and an unlabelled shipment is a compliance problem rather than a cost problem. Too many and a stack of tags printed with last season's collection name goes to scrap. This breaks the number into four additions and one multiplier, and works one example end to end: a 10,000-piece order that ends up at 12,000 tags.",
        "fr": "Se tromper sur la quantité d'étiquettes pendantes coûte cher dans les deux sens. Trop peu, et les derniers jours de production n'ont rien à attacher : l'expédition attend ou part sans étiquette, ce qui est un problème de conformité et non de coût. Trop, et une pile d'étiquettes portant le nom de la collection précédente part au rebut. Cet article décompose le calcul en quatre ajouts et un multiplicateur, avec un exemple complet : une commande de 10 000 pièces qui aboutit à 12 000 étiquettes.",
        "es": "Equivocarse con la cantidad de etiquetas colgantes sale caro en ambos sentidos. Si faltan, los últimos días de producción no tienen qué colgar: el envío espera o sale sin etiquetar, y un envío sin etiquetar es un problema de cumplimiento, no de coste. Si sobran, una pila con el nombre de la colección anterior se va al desecho. Aquí el cálculo se divide en cuatro sumandos y un multiplicador, con un ejemplo completo: un pedido de 10.000 piezas que termina en 12.000 etiquetas.",
        "ja": "下げ札の数量を間違えると、どちらに転んでも高くつきます。少なければ生産終盤に付ける札がなく、出荷を遅らせるか、札なしで出すかになります。後者はコストではなくコンプライアンスの問題です。多ければ、前シーズンのコレクション名が入った札が残って廃棄になります。本稿では数量を 4 つの加算と 1 つの乗算に分解し、10,000 着の注文が最終的に 12,000 枚になる例を最後まで計算します。",
        "ko": "행택 수량을 잘못 잡으면 양쪽 모두 비쌉니다. 부족하면 생산 막바지에 달 행택이 없어 출하를 미루거나 라벨 없이 내보내야 하는데, 후자는 원가가 아니라 컴플라이언스 문제입니다. 남으면 지난 시즌 컬렉션명이 찍힌 행택이 폐기됩니다. 이 글은 수량을 네 개의 가산과 한 개의 승산으로 나누고, 10,000장 주문이 최종 12,000장이 되는 예를 끝까지 계산합니다.",
    }),

    ("h2", {
        "zh": "一、基數從服裝件數來，不從吊牌單價來",
        "en": "1. Start From Garment Pieces, Not From the Tag Price",
        "fr": "1. Partir du nombre de pièces, pas du prix de l'étiquette",
        "es": "1. Partir de las prendas, no del precio de la etiqueta",
        "ja": "1. 起点は縫製品の枚数、札の単価ではない",
        "ko": "1. 기준은 의류 수량이지 행택 단가가 아니다",
    }),
    ("p", {
        "zh": "最常見的算法錯誤是「先看吊牌單價，湊到最低起訂量」。吊牌是服裝的配件，它的數量上限由服裝件數決定，不由印刷廠的價格階梯決定。正確的順序是：先算服裝件數乘以每件張數，加上備品與固定用量，得到需求總量；再把這個總量和供應商的價格級距比對，決定要不要往上湊一級。順序顛倒，就會出現「買了 20,000 張吊牌，服裝只做了 8,000 件」的庫存。",
        "en": "The usual mistake is to look at the tag price first and buy up to the minimum order quantity. A hang tag is a component of a garment: its ceiling is set by how many garments you are making, not by the printer's price ladder. The right order is to multiply garment pieces by tags per garment, add spares and fixed uses to get total demand, and only then compare that total against the supplier's price breaks to decide whether to step up one level. Reverse the order and you buy 20,000 tags for 8,000 garments.",
        "fr": "L'erreur courante est de regarder d'abord le prix unitaire et d'acheter jusqu'au minimum de commande. Une étiquette pendante est un composant du vêtement : son plafond est fixé par le nombre de pièces produites, pas par l'échelle de prix de l'imprimeur. Le bon ordre est de multiplier les pièces par le nombre d'étiquettes, d'ajouter le stock de sécurité et les usages fixes pour obtenir le besoin total, puis seulement de comparer ce total aux paliers du fournisseur pour décider de monter d'un cran. Inversé, on achète 20 000 étiquettes pour 8 000 pièces.",
        "es": "El error habitual es mirar primero el precio unitario y comprar hasta el mínimo de pedido. Una etiqueta colgante es un componente de la prenda: su techo lo fija el número de prendas, no la escala de precios del impresor. El orden correcto es multiplicar prendas por etiquetas, sumar reserva y usos fijos para obtener la necesidad total, y solo entonces comparar ese total con los tramos del proveedor para decidir si subir un nivel. Al revés, se compran 20.000 etiquetas para 8.000 prendas.",
        "ja": "よくある間違いは、先に札の単価を見て最低ロットまで数量を積むことです。下げ札は縫製品の部品であり、上限は生産する着数で決まり、印刷会社の価格階段では決まりません。正しい順序は、着数 × 1 着あたり枚数に予備と固定使用量を足して必要総量を出し、その総量をサプライヤーの価格区分と比べて 1 段上げるか判断することです。逆にすると 8,000 着に対して 20,000 枚の札を買うことになります。",
        "ko": "흔한 실수는 행택 단가를 먼저 보고 최소 주문 수량까지 수량을 채우는 것입니다. 행택은 의류의 부품이고, 상한은 생산 수량으로 정해지며 인쇄소의 가격 구간으로 정해지지 않습니다. 올바른 순서는 착수 × 착당 매수에 예비와 고정 사용량을 더해 필요 총량을 만들고, 그 총량을 공급사 가격 구간과 비교해 한 단계 올릴지 판단하는 것입니다. 순서를 뒤집으면 8,000착에 20,000장 행택을 사게 됩니다.",
    }),

    ("h2", {
        "zh": "二、每件幾張：單張、套裝與多語版本",
        "en": "2. Tags per Garment: Single, Sets and Language Versions",
        "fr": "2. Nombre d'étiquettes par pièce : simple, jeu, versions linguistiques",
        "es": "2. Etiquetas por prenda: simple, juego y versiones de idioma",
        "ja": "2. 1 着あたり枚数：単票・セット・言語版",
        "ko": "2. 착당 매수: 단일·세트·언어판",
    }),
    ("table", (
        [
            {"zh": "做法", "en": "Arrangement", "fr": "Formule", "es": "Formato", "ja": "構成", "ko": "구성"},
            {"zh": "每件張數", "en": "Tags per piece", "fr": "Étiquettes par pièce", "es": "Etiquetas por prenda", "ja": "1 着あたり", "ko": "착당 매수"},
            {"zh": "說明", "en": "Notes", "fr": "Remarques", "es": "Notas", "ja": "補足", "ko": "비고"},
        ],
        [
            [
                {"zh": "單張主吊牌", "en": "Single main tag", "fr": "Étiquette principale seule", "es": "Etiqueta principal sola", "ja": "メイン札 1 枚", "ko": "메인 행택 1장"},
                {"zh": "1", "en": "1", "fr": "1", "es": "1", "ja": "1", "ko": "1"},
                {"zh": "最常見，適合基本款與快返單", "en": "Most common; basics and quick reorders", "fr": "Le plus courant, basiques et réassorts rapides", "es": "Lo habitual, básicos y reposiciones rápidas", "ja": "最も一般的。ベーシックと短納期リピート向け", "ko": "가장 흔함. 베이직과 단납기 리오더"},
            ],
            [
                {"zh": "吊牌 + 成分卡 + 價格牌", "en": "Tag + content card + price ticket", "fr": "Étiquette + carte composition + prix", "es": "Etiqueta + tarjeta de composición + precio", "ja": "札＋組成カード＋値札", "ko": "행택+혼용률 카드+가격표"},
                {"zh": "2–3", "en": "2–3", "fr": "2–3", "es": "2–3", "ja": "2〜3", "ko": "2~3"},
                {"zh": "多層次品牌或百貨要求，穿繩一次掛齊", "en": "For layered branding or department stores; strung together in one pass", "fr": "Marque à plusieurs niveaux ou grands magasins, enfilés ensemble", "es": "Marca por capas o grandes almacenes, enhebrados juntos", "ja": "多層ブランドや百貨店向け。一度に紐通し", "ko": "다층 브랜드나 백화점 요구. 한 번에 끈 통과"},
            ],
            [
                {"zh": "多語版本，一市場一張", "en": "One tag per language market", "fr": "Une étiquette par marché linguistique", "es": "Una etiqueta por mercado lingüístico", "ja": "言語市場ごとに 1 枚", "ko": "언어 시장별 1장"},
                {"zh": "按市場分別下單", "en": "Ordered separately per market", "fr": "Commandées séparément", "es": "Pedidas por separado", "ja": "市場ごとに発注", "ko": "시장별로 발주"},
                {"zh": "歐盟可一版多語；日韓須單語，別混版", "en": "One multi-language tag works in the EU; Japan and Korea expect single-language tags", "fr": "Une étiquette multilingue convient dans l'UE ; Japon et Corée attendent une langue unique", "es": "En la UE vale una multilingüe; Japón y Corea esperan una sola lengua", "ja": "EU は多言語 1 枚で可。日韓は単言語で分ける", "ko": "EU는 다국어 1장 가능. 일본·한국은 단일 언어로 분리"},
            ],
        ],
    )),
    ("p", {
        "zh": "尺碼配比會影響的不是總張數，而是分箱與分碼：同一個款做 2,000 件，S/M/L/XL 按 2:4:3:1 拆，吊牌本身不分碼（除非你印了尺碼），但你要確保每個尺碼箱裡都有對應數量的吊牌。實務上把吊牌按「總件數 × 1.02」裝進主箱，再按尺碼比例分小包，比每箱精算更省事，也不會出現某個尺碼缺牌。",
        "en": "The size ratio does not change the total count, it changes how you split cartons and sizes. For 2,000 pieces split S to XL at 2:4:3:1, the tags themselves are usually size-agnostic unless the size is printed on them, but every size carton still needs its own count. In practice, pack tags at total pieces times 1.02 into the master carton and split them by size ratio into the inner bags: simpler than counting per carton, and no size ends up short.",
        "fr": "La répartition des tailles ne change pas le total, elle change la façon de répartir cartons et tailles. Pour 2 000 pièces en S à XL selon 2:4:3:1, les étiquettes sont en général indépendantes de la taille, sauf si celle-ci est imprimée, mais chaque carton de taille a besoin de son compte. En pratique, mettez pièces totales × 1,02 dans le carton maître et répartissez par ratio dans les sachets : plus simple que de compter par carton, et aucune taille ne manque.",
        "es": "El reparto de tallas no cambia el total, cambia cómo divides cajas y tallas. Para 2.000 piezas en S a XL según 2:4:3:1, las etiquetas suelen ser independientes de la talla salvo que esta vaya impresa, pero cada caja de talla necesita su cuenta. En la práctica, meta piezas totales × 1,02 en la caja máster y reparta por ratio en las bolsas interiores: más simple que contar por caja y ninguna talla queda corta.",
        "ja": "サイズ構成が変えるのは総枚数ではなく、箱とサイズへの振り分けです。2,000 着を S〜XL に 2:4:3:1 で分ける場合、札自体はサイズを印刷しない限り共通ですが、サイズ別の箱ごとに枚数が必要です。実務では総着数 × 1.02 をマスターカートンに入れ、内袋にサイズ比で分けます。箱ごとに数えるより簡単で、サイズ欠けも起きません。",
        "ko": "사이즈 구성이 바꾸는 것은 총수량이 아니라 박스와 사이즈 배분입니다. 2,000착을 S~XL로 2:4:3:1로 나눌 때 행택은 사이즈를 인쇄하지 않는 한 공통이지만, 사이즈별 박스마다 수량이 필요합니다. 실무에서는 총착수 × 1.02를 마스터 카톤에 넣고 사이즈 비율로 내포에 나눕니다. 박스마다 세는 것보다 간단하고 특정 사이즈가 부족하지도 않습니다.",
    }),

    ("h2", {
        "zh": "三、備品率：3%、5%、8% 各自對應什麼",
        "en": "3. Spare Rate: What 3, 5 and 8 Percent Actually Cover",
        "fr": "3. Stock de sécurité : ce que couvrent 3, 5 et 8 %",
        "es": "3. Reserva: qué cubren realmente 3, 5 y 8 %",
        "ja": "3. 予備率：3 %・5 %・8 % がそれぞれ何をカバーするか",
        "ko": "3. 예비율: 3 %, 5 %, 8 %가 각각 무엇을 덮는가",
    }),
    ("ul", [
        {
            "zh": "3%：只補生產損耗。吊牌穿繩時拉裂、打孔處撕壞、包裝時壓折、廠內重掛。適合單價低、可補印、款式穩定的基本款。",
            "en": "3 percent: production loss only. Tags torn while stringing, split at the hole, creased in packing or re-attached at the factory. Fine for low-cost basics on stable styles where a small reprint is acceptable.",
            "fr": "3 % : uniquement les pertes de production. Étiquettes déchirées à l'enfilage, fendues au trou, pliées à l'emballage ou réattachées en usine. Convient aux basiques bon marché, styles stables, où une petite réimpression reste acceptable.",
            "es": "3 %: solo merma de producción. Etiquetas rasgadas al enhebrar, abiertas en el troquel, marcadas al embolsar o recolocadas en fábrica. Vale para básicos baratos de estilo estable donde una pequeña reimpresión es aceptable.",
            "ja": "3 %：生産ロス分のみ。紐通しで切れる、穴で破れる、梱包で折れる、工場で付け替える。低単価で再印刷が許容される安定定番向けです。",
            "ko": "3 %: 생산 손실만. 끈 통과 중 찢어짐, 구멍 갈라짐, 포장 중 접힘, 공장 내 재부착. 단가가 낮고 소량 재인쇄가 가능한 안정적 베이직에 적합합니다.",
        },
        {
            "zh": "5%：加上換標與返工。展會樣衣、買手改款重掛、QC 挑出的瑕疵件換牌。這是出口訂單的常用值，也是我們建議的默認值。",
            "en": "5 percent: adds re-labelling and rework. Showroom samples, buyer changes that need re-tagging, rejects picked out at QC and re-labelled. This is the usual value for export orders and the default we recommend.",
            "fr": "5 % : ajoute le réétiquetage et les reprises. Échantillons de showroom, changements acheteur à réétiqueter, pièces écartées au contrôle et réétiquetées. C'est la valeur usuelle à l'export et notre recommandation par défaut.",
            "es": "5 %: añade reetiquetado y retrabajo. Muestras de showroom, cambios de comprador que exigen recolocar, piezas rechazadas en QC y reetiquetadas. Es el valor habitual en exportación y nuestro valor por defecto.",
            "ja": "5 %：付け替えと手直し分を追加。ショールーム用サンプル、買い手都合の付け替え、QC で外した不良品の再ラベル。輸出案件の標準値で、当社の推奨既定値です。",
            "ko": "5 %: 재부착과 재작업 포함. 쇼룸 샘플, 바이어 변경으로 인한 재부착, QC에서 걸러진 불량의 재라벨. 수출 주문의 통상 값이며 저희 기본 권장값입니다.",
        },
        {
            "zh": "8–10%：多倉、電商、直播退換。每次退換都要重掛，門店與倉庫之間調貨也會消耗吊牌；退貨率高於 20% 的品類建議直接取 10%。",
            "en": "8 to 10 percent: multi-warehouse, e-commerce and live-selling returns. Every return means re-tagging, and transfers between stores and warehouses consume tags too. Above a 20 percent return rate, take the full 10 percent.",
            "fr": "8 à 10 % : multi-entrepôts, e-commerce et retours de vente en direct. Chaque retour se réétiquette, et les transferts entre boutiques et entrepôts consomment aussi des étiquettes. Au-delà de 20 % de retours, prenez les 10 %.",
            "es": "8 a 10 %: varios almacenes, comercio electrónico y devoluciones de venta en directo. Cada devolución exige recolocar la etiqueta y los traslados entre tiendas y almacenes también consumen. Con más de 20 % de devoluciones, tome el 10 % completo.",
            "ja": "8〜10 %：複数倉庫・EC・ライブ販売の返品対応。返品のたびに付け替えが必要で、店舗と倉庫の移動でも消費します。返品率が 20 % を超える品種は 10 % を取ってください。",
            "ko": "8~10 %: 다창고, 이커머스, 라이브 판매 반품. 반품마다 재부착이 필요하고 매장과 창고 간 이동도 소모합니다. 반품률이 20 %를 넘는 품목은 10 %를 잡으십시오.",
        },
        {
            "zh": "另加固定用量 100–500 張：打樣、拍攝、直播展示、媒體寄送、門店陳列與備查留樣，這部分與件數無關，按活動數量估。",
            "en": "Plus a fixed 100 to 500 tags that have nothing to do with piece count: sampling, photo shoots, live-stream sets, press mailings, store display and retained reference samples. Estimate these by activity, not by order size.",
            "fr": "Plus un forfait de 100 à 500 étiquettes sans lien avec le nombre de pièces : échantillons, shootings, plateaux de live, envois presse, présentation en boutique et références conservées. À estimer par activité.",
            "es": "Más un fijo de 100 a 500 etiquetas ajeno al número de piezas: muestras, sesiones de fotos, sets de directo, envíos a prensa, exhibición en tienda y muestras de referencia. Estímelo por actividad.",
            "ja": "さらに着数と無関係な固定 100〜500 枚：サンプル、撮影、ライブ配信用、プレス送付、店頭陳列、保管見本。これは案件数で見積もります。",
            "ko": "여기에 착수와 무관한 고정 100~500장: 샘플, 촬영, 라이브 방송용, 언론 발송, 매장 진열, 보관 견본. 이는 활동 수로 산정합니다.",
        },
    ]),

    ("h2", {
        "zh": "四、短少的代價：吊牌是法定信息的載體",
        "en": "4. The Cost of Running Short: The Tag Carries Mandatory Information",
        "fr": "4. Le coût du manque : l'étiquette porte les mentions obligatoires",
        "es": "4. El coste de quedarse corto: la etiqueta lleva información obligatoria",
        "ja": "4. 不足の代償：下げ札は法定表示の媒体",
        "ko": "4. 부족의 대가: 행택은 법정 표시의 매체",
    }),
    ("p", {
        "zh": "備品率不是「多買一點比較安心」，而是合規緩衝。吊牌上通常印著品牌、系列、成分、產地、條碼，其中多數是法定資訊：歐盟市場的纖維成分依 Règlement (UE) n° 1007/2011 標示，通用產品安全依 GPSR (EU) 2023/988 要求可追溯與歐盟責任主體；美國紡織品依 FTC 的 16 CFR Part 303 標示纖維成分與原產國；日本依家庭用品品質表示法標示組成（混用率）與取扱表示；韓國依전기용품 및 생활용품 안전관리법要求在附著標籤上標示混用率與 원산지。缺吊牌的服裝不能合規出貨，只能延遲——延遲一週的倉儲與違約成本，遠高於 5% 的吊牌。",
        "en": "The spare rate is not a comfort margin, it is a compliance buffer. A hang tag usually carries the brand, the collection, the fibre composition, the country of origin and a barcode, and much of that is mandatory information. In the EU the fibre composition is declared under Regulation (EU) No 1007/2011, and the General Product Safety Regulation (EU) 2023/988 requires traceability and an economic operator established in the Union. In the United States, FTC rules at 16 CFR Part 303 require fibre content and country of origin. Japan requires composition and handling instructions under the Household Goods Quality Labelling Act, and Korea requires composition and origin on an attached label under its safety control act for household textiles. A garment without its tag cannot ship compliantly; it waits. One week of storage and penalty costs far more than 5 percent of the tags.",
        "fr": "Le stock de sécurité n'est pas une marge de confort, c'est une réserve de conformité. Une étiquette pendante porte en général la marque, la collection, la composition, l'origine et un code-barres, dont une bonne part est obligatoire. Dans l'UE, la composition est déclarée selon le règlement (UE) n° 1007/2011 et le règlement (UE) 2023/988 sur la sécurité générale des produits exige une traçabilité et un opérateur économique établi dans l'Union. Aux États-Unis, les règles FTC du 16 CFR Part 303 imposent composition et pays d'origine. Le Japon exige composition et instructions d'entretien au titre de la loi sur l'étiquetage de qualité, et la Corée impose composition et origine sur une étiquette attachée. Un vêtement sans son étiquette ne peut pas partir conformément : il attend. Une semaine de stockage et de pénalités coûte bien plus que 5 % des étiquettes.",
        "es": "La reserva no es un margen de comodidad, es un colchón de cumplimiento. La etiqueta colgante suele llevar marca, colección, composición, origen y código de barras, y buena parte es información obligatoria. En la UE la composición se declara según el Reglamento (UE) n.º 1007/2011 y el Reglamento (UE) 2023/988 de seguridad general exige trazabilidad y un operador económico establecido en la Unión. En Estados Unidos, las reglas FTC del 16 CFR Part 303 exigen composición y país de origen. Japón exige composición e instrucciones de cuidado según su ley de etiquetado de calidad, y Corea exige composición y origen en una etiqueta adherida. Una prenda sin su etiqueta no puede salir conforme: espera. Una semana de almacenaje y penalizaciones cuesta mucho más que el 5 % de las etiquetas.",
        "ja": "予備率は安心のための余裕ではなく、コンプライアンスの緩衝です。下げ札には通常、ブランド、コレクション、組成、原産国、バーコードが入り、その多くが法定表示です。EU では繊維組成を規則 (EU) No 1007/2011 に従って表示し、GPSR (EU) 2023/988 はトレーサビリティと EU 域内の責任事業者を求めます。米国は FTC の 16 CFR Part 303 が繊維組成と原産国の表示を義務づけます。日本は家庭用品品質表示法により組成（混用率）と取扱表示、韓国は전기용품 및 생활용품 안전관리법により付属ラベルへの混用率と原産国の表示が必要です。札のない衣料は適合した状態で出荷できず、待つしかありません。1 週間の保管料と違約金は、札の 5 % よりはるかに高くつきます。",
        "ko": "예비율은 안심용 여유가 아니라 컴플라이언스 완충입니다. 행택에는 보통 브랜드, 컬렉션, 혼용률, 원산지, 바코드가 들어가고 상당 부분이 법정 표시입니다. EU에서는 섬유 혼용률을 규정 (EU) No 1007/2011에 따라 표시하고, GPSR (EU) 2023/988은 추적성과 EU 역내 책임 사업자를 요구합니다. 미국은 FTC의 16 CFR Part 303이 섬유 혼용률과 원산지 표시를 요구합니다. 일본은 가정용품품질표시법에 따라 혼용률과 취급 표시를, 한국은 전기용품 및 생활용품 안전관리법에 따라 부착 라벨에 혼용률과 원산지를 표시해야 합니다. 행택이 없는 의류는 적합한 상태로 출하할 수 없고 기다려야 합니다. 일주일의 보관료와 위약금은 행택 5 %보다 훨씬 큽니다.",
    }),
    ("callout", {
        "zh": "重量也要算進運費：55 × 90 mm、350 g/m² 的吊牌單張約 1.7 g，10,000 張約 17 kg，含掛繩與內袋約 21 kg，通常裝兩箱。空運按體積重計費時，這個重量級別的運費差異足以吃掉半個價格級距的折扣。",
        "en": "Weight belongs in the freight quote. A 55 × 90 mm tag at 350 g/m² weighs about 1.7 g, so 10,000 tags are roughly 17 kg, or 21 kg with strings and inner bags, usually two cartons. On air freight charged by volumetric weight, a difference of that size can eat half the discount from stepping up a price break.",
        "fr": "Le poids entre dans le fret. Une étiquette de 55 × 90 mm à 350 g/m² pèse environ 1,7 g : 10 000 étiquettes font quelque 17 kg, 21 kg avec fils et sachets, soit deux cartons. En aérien facturé au poids volumétrique, un tel écart peut absorber la moitié de la remise obtenue en montant d'un palier.",
        "es": "El peso entra en el flete. Una etiqueta de 55 × 90 mm a 350 g/m² pesa unos 1,7 g: 10.000 etiquetas son unos 17 kg, 21 kg con cordones y bolsas, normalmente dos cajas. En aéreo facturado por peso volumétrico, esa diferencia puede comerse la mitad del descuento de subir un tramo.",
        "ja": "重量も運賃に入ります。55 × 90 mm、350 g/m² の札は 1 枚約 1.7 g。10,000 枚で約 17 kg、紐と内袋を含めると約 21 kg で通常 2 カートンです。容積重量で請求される航空便では、この差が価格区分を 1 段上げて得た値引きの半分を消すことがあります。",
        "ko": "중량도 운임에 들어갑니다. 55 × 90 mm, 350 g/m² 행택은 장당 약 1.7 g으로 10,000장이 약 17 kg, 끈과 내포를 포함하면 약 21 kg이며 보통 2카톤입니다. 용적 중량으로 청구되는 항공 운송에서는 이 차이가 가격 구간을 한 단계 올려 받은 할인의 절반을 없앨 수 있습니다.",
    }),

    ("h2", {
        "zh": "五、多印還是補印：三個數字算一次就明白",
        "en": "5. Over-Order or Reprint: Three Numbers Settle It",
        "fr": "5. Surcommander ou réimprimer : trois chiffres tranchent",
        "es": "5. ¿Comprar de más o reimprimir? Tres números lo resuelven",
        "ja": "5. 多めに刷るか再印刷か：3 つの数字で決まる",
        "ko": "5. 더 인쇄할까 재인쇄할까: 숫자 세 개면 정리된다",
    }),
    ("p", {
        "zh": "補印的隱性成本常被低估。它包含四項：一是版費與刀模，若刀模還在，只收印刷版；二是最低起印量，多數供應商每款最低 3,000–5,000 張，補 300 張和補 3,000 張的單價差距可能到三倍；三是交期，7–12 個工作日加上運輸；四是色差風險，新批次的紙張與油墨批次不同，ΔE 落在 1.5–2.5 很常見，精品客戶會看出來。所以決策規則很簡單：如果預期需要補印的機率超過三成，就往上湊一個價格級距，但多買的量不要超過 15%，超過就是庫存而不是保險。",
        "en": "The hidden cost of a reprint is usually underestimated. It has four parts: plates and the die, where a surviving die means only the printing plates are charged; the minimum run, which at most suppliers is 3,000 to 5,000 pieces per design, so topping up 300 pieces can cost up to three times the unit price of 3,000; lead time, seven to twelve working days plus freight; and colour drift, because a new paper and ink lot commonly lands at a Delta E of 1.5 to 2.5, which a premium buyer will see. The decision rule is therefore simple: if the probability of needing a reprint is above about 30 percent, step up one price break, but keep the extra quantity under 15 percent. Beyond that it is inventory, not insurance.",
        "fr": "Le coût caché d'une réimpression est sous-estimé. Il a quatre composantes : les plaques et la forme, une forme encore disponible ne facturant que les plaques ; le tirage minimum, de 3 000 à 5 000 pièces par référence chez la plupart des fournisseurs, si bien que compléter 300 pièces peut coûter jusqu'à trois fois le prix unitaire de 3 000 ; le délai, sept à douze jours ouvrés plus le transport ; et la dérive colorimétrique, un nouveau lot de papier et d'encre tombant couramment à un Delta E de 1,5 à 2,5, ce qu'un acheteur haut de gamme verra. La règle est donc simple : au-delà de 30 % de probabilité de réimpression, montez d'un palier, mais gardez l'excédent sous 15 %. Au-delà, c'est du stock, pas de l'assurance.",
        "es": "El coste oculto de una reimpresión se subestima. Tiene cuatro partes: planchas y cuchilla, donde una cuchilla conservada solo factura planchas; el tiraje mínimo, de 3.000 a 5.000 piezas por referencia en la mayoría de proveedores, así que reponer 300 puede costar hasta el triple del unitario de 3.000; el plazo, de siete a doce días hábiles más transporte; y la deriva de color, porque un lote nuevo de papel y tinta suele caer en un Delta E de 1,5 a 2,5, y un comprador premium lo verá. La regla es simple: si la probabilidad de reimprimir supera el 30 %, suba un tramo, pero mantenga el excedente por debajo del 15 %. Más allá es inventario, no seguro.",
        "ja": "再印刷の隠れコストは過小評価されがちです。要素は 4 つ。版と木型（木型が残っていれば印刷版のみ）、最低ロット（多くのサプライヤーで 1 品番 3,000〜5,000 枚、300 枚の追加は 3,000 枚の単価の 3 倍になり得ます）、納期（7〜12 営業日＋輸送）、そして色差（新しい紙とインキのロットで ΔE 1.5〜2.5 は珍しくなく、高級ブランドの買い手は気づきます）。判断は単純です。再印刷が必要になる確率が 3 割を超えるなら価格区分を 1 段上げ、ただし増やす量は 15 % 未満に抑えます。それを超えると保険ではなく在庫です。",
        "ko": "재인쇄의 숨은 비용은 대개 과소평가됩니다. 네 가지입니다. 판과 목형(목형이 남아 있으면 인쇄 판만 청구), 최소 인쇄 수량(대부분 공급사가 품번당 3,000~5,000장이라 300장 보충은 3,000장 단가의 세 배까지 나옵니다), 납기(영업일 7~12일 더하기 운송), 그리고 색차(새 종이와 잉크 로트에서 ΔE 1.5~2.5는 흔하고 프리미엄 바이어는 알아봅니다). 그래서 판단은 단순합니다. 재인쇄가 필요할 확률이 30 %를 넘으면 가격 구간을 한 단계 올리되, 늘리는 수량은 15 % 미만으로 유지하십시오. 그 이상은 보험이 아니라 재고입니다.",
    }),
    ("table", (
        [
            {"zh": "情境", "en": "Situation", "fr": "Situation", "es": "Situación", "ja": "状況", "ko": "상황"},
            {"zh": "建議", "en": "Recommendation", "fr": "Recommandation", "es": "Recomendación", "ja": "推奨", "ko": "권장"},
        ],
        [
            [
                {"zh": "基本款、款式已定、供應商留刀模", "en": "Basics, artwork frozen, supplier keeps the die", "fr": "Basiques, maquette figée, forme conservée", "es": "Básicos, arte fijo, cuchilla guardada", "ja": "定番・デザイン確定・木型保管あり", "ko": "베이직, 디자인 확정, 목형 보관"},
                {"zh": "取 3%，不必湊級距", "en": "Take 3 percent; do not chase a price break", "fr": "Prenez 3 %, sans viser un palier", "es": "Tome 3 %, sin buscar un tramo", "ja": "3 % で十分。区分は狙わない", "ko": "3 %면 충분. 구간은 좇지 않음"},
            ],
            [
                {"zh": "出口訂單、有 QC 與換標流程", "en": "Export orders with QC and re-tagging", "fr": "Export avec contrôle et réétiquetage", "es": "Exportación con QC y reetiquetado", "ja": "輸出案件・QC と付け替えあり", "ko": "수출 주문, QC와 재부착 있음"},
                {"zh": "取 5%，並湊到最近級距但 ≤ +15%", "en": "Take 5 percent and step to the nearest break, capped at plus 15 percent", "fr": "Prenez 5 % et montez au palier le plus proche, plafonné à +15 %", "es": "Tome 5 % y suba al tramo más cercano con tope de +15 %", "ja": "5 % とし、直近の区分まで（+15 % 以内）", "ko": "5 %에 가장 가까운 구간까지(+15 % 이내)"},
            ],
            [
                {"zh": "多倉電商、直播、退貨率高", "en": "Multi-warehouse e-commerce, live selling, high returns", "fr": "E-commerce multi-entrepôts, live, retours élevés", "es": "E-commerce multi-almacén, directo, muchas devoluciones", "ja": "複数倉庫 EC・ライブ・返品多", "ko": "다창고 이커머스, 라이브, 반품 많음"},
                {"zh": "取 10%，不湊級距（款式可能提前改版）", "en": "Take 10 percent and do not step up; the artwork may change first", "fr": "Prenez 10 % sans monter de palier : la maquette peut changer", "es": "Tome 10 % sin subir tramo: el arte puede cambiar", "ja": "10 %、区分は狙わない（先に改版があり得る）", "ko": "10 %, 구간은 올리지 않음(디자인이 먼저 바뀔 수 있음)"},
            ],
        ],
    )),

    ("h2", {
        "zh": "六、排期與倉儲：春節、海運與濕度",
        "en": "6. Scheduling and Storage: New Year, Sea Freight and Humidity",
        "fr": "6. Planning et stockage : Nouvel An, maritime, humidité",
        "es": "6. Planificación y almacenaje: Año Nuevo, marítimo, humedad",
        "ja": "6. 段取りと保管：旧正月・海上輸送・湿度",
        "ko": "6. 일정과 보관: 설 연휴·해상 운송·습도",
    }),
    ("p", {
        "zh": "吊牌看起來是小事，但它是掛在服裝上的最後一道工序，缺它就出不了貨。排期上要抓三個節點：工廠春節停產通常 2–3 週，節前 4 週是印刷與物流最擠的窗口，吊牌最晚要在服裝交期前 45–60 天到位；海運到歐美再加 30–35 天，如果吊牌與服裝不同地，還要留出國內轉運 3–5 天。倉儲端，吊牌怕濕不怕冷：建議 20 ± 5 °C、相對濕度 50 ± 10%，整箱離地 100 mm 存放，開箱後沒用完的用乾燥劑密封，先進先出。受潮的吊牌會翹曲、穿繩處變軟，這與紙張絲流方向一起決定最終的平整度。",
        "en": "A hang tag looks like a small item, but it is the last operation before a garment can ship, and without it nothing leaves. Three dates matter. Chinese New Year shuts factories for two to three weeks and the four weeks before it are the busiest window for printing and logistics, so tags should be in hand 45 to 60 days before the garment delivery date. Sea freight to Europe or the Americas adds another 30 to 35 days, and if tags and garments are made in different places, allow three to five days of domestic transfer. In storage, tags fear moisture rather than cold: keep them at 20 ± 5 °C and 50 ± 10 percent relative humidity, on pallets 100 mm off the floor, reseal opened cartons with desiccant and work first in, first out. Damp tags curl and soften at the string hole, and together with grain direction that decides how flat they finally sit.",
        "fr": "Une étiquette pendante semble un détail, mais c'est la dernière opération avant l'expédition : sans elle, rien ne part. Trois dates comptent. Le Nouvel An chinois arrête les usines deux à trois semaines et les quatre semaines précédentes sont la fenêtre la plus chargée pour l'impression et la logistique : les étiquettes doivent être là 45 à 60 jours avant la date de livraison. Le maritime vers l'Europe ou les Amériques ajoute 30 à 35 jours, et si étiquettes et vêtements sont produits à des endroits différents, prévoyez trois à cinq jours de transfert intérieur. En stockage, l'étiquette craint l'humidité plus que le froid : 20 ± 5 °C, 50 ± 10 % d'humidité relative, palettes à 100 mm du sol, cartons ouverts refermés avec dessiccant, premier entré premier sorti. Une étiquette humide tuile et se ramollit au trou, et avec le sens du grain, cela décide de sa planéité finale.",
        "es": "Una etiqueta colgante parece un detalle, pero es la última operación antes de embarcar: sin ella no sale nada. Importan tres fechas. El Año Nuevo chino para las fábricas de dos a tres semanas y las cuatro semanas previas son la ventana más cargada para impresión y logística, así que las etiquetas deben estar 45 a 60 días antes de la fecha de entrega de la prenda. El marítimo a Europa o América añade 30 a 35 días, y si etiquetas y prendas se fabrican en lugares distintos, reserve tres a cinco días de traslado interno. En almacén, la etiqueta teme la humedad más que el frío: 20 ± 5 °C y 50 ± 10 % de humedad relativa, palés a 100 mm del suelo, cajas abiertas reselladas con desecante y primero entrado, primero salido. Una etiqueta húmeda se alabea y se ablanda en el troquel, y junto con la dirección de fibra eso decide su planitud final.",
        "ja": "下げ札は小さな部品に見えますが、出荷前の最後の工程であり、なければ何も出せません。押さえるべき日付は 3 つ。旧正月で工場は 2〜3 週間止まり、その前 4 週間は印刷と物流が最も混みます。札は縫製品の納期の 45〜60 日前に手元に置いてください。欧米向け海上輸送はさらに 30〜35 日、札と縫製品の生産地が違う場合は国内輸送に 3〜5 日を見ます。保管では寒さより湿気が大敵です。20 ± 5 °C、相対湿度 50 ± 10 %、パレットで床から 100 mm、開封後は乾燥剤とともに密封し、先入れ先出しを守ります。湿った札は反り、紐穴が柔らかくなり、紙の目と合わせて最終的な平坦さが決まります。",
        "ko": "행택은 작은 부품 같지만 출하 전 마지막 공정이고, 없으면 아무것도 나가지 못합니다. 챙길 날짜는 세 가지입니다. 설 연휴로 공장이 2~3주 멈추고 그 전 4주가 인쇄와 물류가 가장 붐비므로, 행택은 의류 납기 45~60일 전에 손에 있어야 합니다. 유럽·미주행 해상 운송은 30~35일이 더 걸리고, 행택과 의류 생산지가 다르면 국내 운송 3~5일을 봐야 합니다. 보관에서는 추위보다 습기가 문제입니다. 20 ± 5 °C, 상대습도 50 ± 10 %, 파렛트로 바닥에서 100 mm, 개봉 후에는 건조제와 함께 밀봉하고 선입선출을 지킵니다. 습기를 먹은 행택은 휘고 끈 구멍이 물러지며, 종이 결 방향과 함께 최종 평탄도를 결정합니다.",
    }),

    ("h2", {
        "zh": "七、一個可以直接套的算例",
        "en": "7. One Worked Example You Can Copy",
        "fr": "7. Un exemple complet à recopier",
        "es": "7. Un ejemplo completo para copiar",
        "ja": "7. そのまま使える計算例",
        "ko": "7. 그대로 쓸 수 있는 계산 예",
    }),
    ("table", (
        [
            {"zh": "項目", "en": "Item", "fr": "Poste", "es": "Concepto", "ja": "項目", "ko": "항목"},
            {"zh": "數量", "en": "Quantity", "fr": "Quantité", "es": "Cantidad", "ja": "数量", "ko": "수량"},
            {"zh": "算法", "en": "How", "fr": "Calcul", "es": "Cálculo", "ja": "算出", "ko": "산출"},
        ],
        [
            [
                {"zh": "服裝件數", "en": "Garment pieces", "fr": "Pièces", "es": "Prendas", "ja": "縫製品枚数", "ko": "의류 착수"},
                {"zh": "10,000", "en": "10,000", "fr": "10 000", "es": "10.000", "ja": "10,000", "ko": "10,000"},
                {"zh": "訂單量", "en": "Order quantity", "fr": "Quantité commandée", "es": "Cantidad del pedido", "ja": "受注数", "ko": "주문 수량"},
            ],
            [
                {"zh": "每件張數", "en": "Tags per piece", "fr": "Étiquettes par pièce", "es": "Etiquetas por prenda", "ja": "1 着あたり枚数", "ko": "착당 매수"},
                {"zh": "1", "en": "1", "fr": "1", "es": "1", "ja": "1", "ko": "1"},
                {"zh": "單張主吊牌", "en": "Single main tag", "fr": "Étiquette principale", "es": "Etiqueta principal", "ja": "メイン札 1 枚", "ko": "메인 행택 1장"},
            ],
            [
                {"zh": "備品 5%", "en": "Spares at 5 percent", "fr": "Sécurité 5 %", "es": "Reserva 5 %", "ja": "予備 5 %", "ko": "예비 5 %"},
                {"zh": "500", "en": "500", "fr": "500", "es": "500", "ja": "500", "ko": "500"},
                {"zh": "10,000 × 5%", "en": "10,000 × 5 percent", "fr": "10 000 × 5 %", "es": "10.000 × 5 %", "ja": "10,000 × 5 %", "ko": "10,000 × 5 %"},
            ],
            [
                {"zh": "固定用量", "en": "Fixed uses", "fr": "Usages fixes", "es": "Usos fijos", "ja": "固定使用量", "ko": "고정 사용량"},
                {"zh": "100", "en": "100", "fr": "100", "es": "100", "ja": "100", "ko": "100"},
                {"zh": "打樣 60 + 拍攝與陳列 40", "en": "60 samples plus 40 for shoot and display", "fr": "60 échantillons + 40 shooting/vitrine", "es": "60 muestras + 40 para sesión y tienda", "ja": "サンプル 60＋撮影・陳列 40", "ko": "샘플 60 + 촬영·진열 40"},
            ],
            [
                {"zh": "需求合計", "en": "Total demand", "fr": "Besoin total", "es": "Necesidad total", "ja": "必要総量", "ko": "필요 총량"},
                {"zh": "10,600", "en": "10,600", "fr": "10 600", "es": "10.600", "ja": "10,600", "ko": "10,600"},
                {"zh": "再加 1% 廠內損耗 → 10,700", "en": "Plus 1 percent in-plant loss, 10,700", "fr": "Plus 1 % de perte interne, 10 700", "es": "Más 1 % de merma interna, 10.700", "ja": "社内ロス 1 % を加え 10,700", "ko": "사내 손실 1 % 추가해 10,700"},
            ],
            [
                {"zh": "實際下單", "en": "Actually order", "fr": "Commande réelle", "es": "Pedido real", "ja": "実際の発注", "ko": "실제 발주"},
                {"zh": "12,000", "en": "12,000", "fr": "12 000", "es": "12.000", "ja": "12,000", "ko": "12,000"},
                {"zh": "最近級距為 12,000，多 11% 在 15% 內", "en": "Nearest break is 12,000, an 11 percent overshoot inside the 15 percent cap", "fr": "Palier le plus proche à 12 000, soit +11 % sous le plafond de 15 %", "es": "El tramo más cercano es 12.000, un +11 % dentro del tope del 15 %", "ja": "直近の区分が 12,000、+11 % で 15 % 以内", "ko": "가장 가까운 구간이 12,000, +11 %로 15 % 이내"},
            ],
        ],
    )),
    ("p", {
        "zh": "算到這裡，還有一個常被忽略的檢查：吊牌上的法定資訊是否與最終服裝一致。改了成分、換了供應商、換了產地，吊牌就要改版——這也是為什麼備品率不要盲目拉到 20%。款式改版頻繁的品牌，寧可每次少備一點、把補印當常規動作，把刀模留好、把紙張與油墨批次記在規格裡，補印的色差風險就降下來了。",
        "en": "One last check that gets skipped: whether the mandatory information on the tag still matches the finished garment. A changed fibre content, a new fabric mill or a new country of origin means new artwork, which is why the spare rate should not be pushed to 20 percent by reflex. Brands that revise styles often are better off keeping spares lean, treating reprints as routine, keeping the die on file and recording paper and ink lots in the specification so the colour drift risk on a reprint comes down.",
        "fr": "Un dernier contrôle souvent oublié : les mentions obligatoires de l'étiquette correspondent-elles encore au vêtement fini ? Un changement de composition, de fournisseur de tissu ou d'origine impose une nouvelle maquette, et c'est pourquoi il ne faut pas pousser la sécurité à 20 % par réflexe. Les marques qui révisent souvent leurs modèles gagnent à garder des stocks légers, à traiter la réimpression comme une routine, à conserver la forme et à noter les lots de papier et d'encre dans la spécification, ce qui réduit le risque de dérive colorimétrique.",
        "es": "Un último control que se suele saltar: si la información obligatoria de la etiqueta sigue coincidiendo con la prenda acabada. Cambiar la composición, el proveedor de tejido o el origen obliga a nuevo arte, y por eso la reserva no debe llevarse al 20 % por reflejo. Las marcas que revisan estilos a menudo hacen mejor en mantener reservas ajustadas, tratar la reimpresión como rutina, guardar la cuchilla y anotar los lotes de papel y tinta en la especificación, con lo que baja el riesgo de deriva de color.",
        "ja": "最後に見落とされがちな確認が 1 つあります。札の法定表示が最終的な縫製品と一致しているか。混用率の変更、生地サプライヤーの変更、原産国の変更は改版を意味します。だからこそ予備率を反射的に 20 % まで上げるべきではありません。デザイン改版の多いブランドは、予備を絞り、再印刷を日常業務とし、木型を保管し、紙とインキのロットを仕様に記録するほうが、再印刷時の色差リスクを下げられます。",
        "ko": "마지막으로 자주 건너뛰는 확인이 하나 있습니다. 행택의 법정 표시가 최종 의류와 여전히 일치하는지입니다. 혼용률 변경, 원단 공급사 변경, 원산지 변경은 디자인 수정을 뜻하므로 예비율을 습관적으로 20 %까지 올리면 안 됩니다. 디자인 수정이 잦은 브랜드는 예비를 줄이고 재인쇄를 일상 업무로 삼으며, 목형을 보관하고 종이·잉크 로트를 사양서에 기록하는 편이 재인쇄 시 색차 위험을 낮춥니다.",
    }),

    ("related", [
        ("hang-tag-moq-cost.html", {
            "zh": "吊牌起訂量與單價：為什麼 1,000 張比 3,000 張貴",
            "en": "Hang tag MOQ and unit price: why 1,000 tags cost more than 3,000",
            "fr": "MOQ et prix unitaire : pourquoi 1 000 coûte plus que 3 000",
            "es": "MOQ y precio unitario: por qué 1.000 cuesta más que 3.000",
            "ja": "下げ札の MOQ と単価：1,000 枚が 3,000 枚より高い理由",
            "ko": "행택 MOQ와 단가: 1,000장이 3,000장보다 비싼 이유",
        }),
        ("trim-order-quantity-tolerance-guide.html", {
            "zh": "輔料交貨數量公差：±3% 還是 ±5% 該怎麼約定",
            "en": "Trim delivery quantity tolerance: agreeing plus or minus 3 or 5 percent",
            "fr": "Tolérance de quantité : convenir de ±3 % ou ±5 %",
            "es": "Tolerancia de cantidad: acordar ±3 % o ±5 %",
            "ja": "副資材の数量公差：±3 % か ±5 % か",
            "ko": "부자재 수량 공차: ±3 % vs ±5 %",
        }),
        ("hang-tag-imposition-yield-guide.html", {
            "zh": "吊牌拼版與出紙率：一張大紙能出幾個",
            "en": "Hang tag imposition and yield: how many fit on a sheet",
            "fr": "Imposition et rendement : combien par feuille",
            "es": "Imposición y rendimiento: cuántas por hoja",
            "ja": "下げ札の面付けと取り数",
            "ko": "행택 판걸이와 수율",
        }),
        ("trim-dead-stock-guide.html", {
            "zh": "輔料呆滯庫存：怎麼定義、怎麼處理",
            "en": "Trim dead stock: how to define it and what to do",
            "fr": "Stock dormant : définition et traitement",
            "es": "Stock muerto: definición y tratamiento",
            "ja": "副資材の死蔵在庫：定義と処理",
            "ko": "부자재 사장 재고: 정의와 처리",
        }),
    ]),

    ("cta", (
        {
            "zh": "正在算這一季的吊牌數量？把服裝件數、尺碼配比、銷售渠道與目標市場發給我們，我們會算出含備品與固定用量的建議下單量，並標出補印的版費與起印量風險。",
            "en": "Working out this season's tag quantity? Send the garment pieces, size ratio, sales channels and destination markets, and we will return a recommended order quantity with spares and fixed uses included, plus the plate cost and minimum-run risk of a reprint.",
            "fr": "Vous calculez les quantités de la saison ? Envoyez pièces, répartition des tailles, canaux et marchés de destination : nous renvoyons une quantité recommandée avec sécurité et usages fixes, plus le coût de forme et le risque de tirage minimum.",
            "es": "¿Está calculando las etiquetas de la temporada? Envíe prendas, reparto de tallas, canales y mercados destino: devolveremos una cantidad recomendada con reserva y usos fijos, más el coste de plancha y el riesgo de tiraje mínimo.",
            "ja": "今季の札の数量を検討中ですか。縫製品枚数、サイズ構成、販売チャネル、対象市場をお送りください。予備と固定使用量を含む推奨発注数量と、再印刷の版代・最低ロットのリスクを算出します。",
            "ko": "이번 시즌 행택 수량을 계산 중이신가요? 의류 착수, 사이즈 구성, 판매 채널, 대상 시장을 보내주시면 예비와 고정 사용량을 포함한 권장 발주 수량과 재인쇄의 판 비용·최소 수량 위험을 계산해 드립니다.",
        },
        {
            "zh": "索取吊牌數量建議 →",
            "en": "Request a tag quantity plan →",
            "fr": "Demander un plan de quantités →",
            "es": "Solicitar un plan de cantidades →",
            "ja": "下げ札数量の提案を依頼 →",
            "ko": "행택 수량 제안 요청 →",
        },
    )),
]
