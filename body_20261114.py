# -*- coding: utf-8 -*-
"""2026-11-14 08:00 每日 FAQ：两篇新文章的正文数据（英文主稿 + zh/fr/es/ja/ko 翻译）。
结构：("p"|"h2"|"callout", L(...)) / ("ul"|"ol", [L(),...]) / ("table", head[L], rows[[L,...]])
"""


def L(zh, en, fr, es, ja, ko):
    return {"zh": zh, "en": en, "fr": fr, "es": es, "ja": ja, "ko": ko}


ART1 = [
    ("p", L(
        "零售端正從一維條碼轉向二維碼，而承載它的正是輔料：洗水標、吊牌與膠袋貼紙。GS1 的 Sunrise 2027 計畫，加上美歐零售商已公布的時程，意味著這一季核可的標籤，下一季就可能必須印上內含 GS1 Digital Link 的二維碼。本文說明標籤上到底改了什麼、哪些印刷方式撐得住這個碼，以及現在就該與買家敲定的幾個數字。",
        "Retail is moving from the 1D barcode to 2D codes, and the carrier is a trim: the care label, the hang tag and the poly bag sticker. GS1's Sunrise 2027 initiative, together with deadlines already published by retailers in the US and Europe, means a label approved this season may have to carry a QR code containing a GS1 Digital Link by the next. This guide covers what changes on the label, which print methods can hold the code, and the numbers to settle with the buying team now.",
        "Le commerce de détail passe du code-barres 1D aux codes 2D, et le support, c'est l'accessoire : étiquette d'entretien, hangtag, sticker de sachet. L'initiative Sunrise 2027 de GS1, comme les échéances déjà publiées par des distributeurs américains et européens, signifie que l'étiquette validée cette saison devra peut-être porter un QR code contenant un GS1 Digital Link dès la suivante. Ce guide couvre ce qui change sur l'étiquetage, quels procédés d'impression tiennent le code, et les chiffres à arrêter avec l'acheteur dès maintenant.",
        "El comercio minorista pasa del código de barras 1D a los códigos 2D, y el soporte es un accesorio: la etiqueta de cuidado, el colgante y el sticker de la bolsa. La iniciativa Sunrise 2027 de GS1, junto con los plazos ya publicados por minoristas de EE. UU. y Europa, implica que la etiqueta aprobada esta temporada quizá deba llevar un QR con GS1 Digital Link en la siguiente. Esta guía cubre qué cambia en el etiquetado, qué métodos de impresión sostienen el código y los números que conviene cerrar ya con el comprador.",
        "小売の現場は1次元バーコードから2次元コードへ移り、その担い手は副資材です。洗濯表示ラベル、下げ札、ポリ袋のシールが該当します。GS1 の Sunrise 2027 と、米欧の小売が既に公表した期限により、今季承認したラベルが来季には GS1 Digital Link を格納した QR コードを必要とするかもしれません。本記事では表示の何が変わるのか、どの印刷方式ならコードを保持できるのか、今のうちに買い手と決めておく数値を整理します。",
        "소매 현장은 1차원 바코드에서 2차원 코드로 이동하고 있고, 그 매체는 부자재입니다. 케어 라벨, 행택, 비닐봉투 스티커가 해당합니다. GS1의 Sunrise 2027과 미국·유럽 유통사의 공개된 일정은 이번 시즌 승인한 라벨이 다음 시즌에는 GS1 Digital Link를 담은 QR 코드를 요구받을 수 있음을 뜻합니다. 이 글은 라벨에서 무엇이 바뀌는지, 어떤 인쇄 방식이 코드를 견디는지, 지금 구매팀과 확정해야 할 숫자를 정리합니다.",
    )),

    ("h2", L(
        "1. 到底改了什麼：從 13 位數字到一條鏈接",
        "1. What actually changes: from a 13-digit line to a link",
        "1. Ce qui change réellement : d'un code à 13 chiffres à un lien",
        "1. Qué cambia realmente: de un código de 13 dígitos a un enlace",
        "1. 実際に変わること：13桁の数字からリンクへ",
        "1. 실제로 바뀌는 것: 13자리 숫자에서 링크로",
    )),

    ("p", L(
        "一句話講完差別：一維 EAN-13 只帶 GTIN，二維碼除了同一個 GTIN，還能帶批號、序號與一條可解析的網址（https://id.gs1.org/01/{GTIN}/10/{批號}/21/{序號}）。結帳時它解析出價格與商品資料；售後，它是唯一能追回「哪一批洗水標洗後掉色」的實務路徑。對輔料廠的意義很直接：碼的載體、尺寸與驗收標準，從此屬於規格書的一部分，不再只是圖稿上的一塊黑白方塊。",
        "One sentence covers the difference: a 1D EAN-13 carries the GTIN and nothing else, while a 2D code carries the same GTIN plus lot, serial and a resolvable URL of the form https://id.gs1.org/01/{GTIN}/10/{lot}/21/{serial}. At the till that URL resolves to price and product data; after the sale it is the only practical route back to the batch whose care labels bled in the wash. For a trims supplier this is concrete: the carrier, the size and the acceptance grade of the code now belong in the specification, not just as a black square on the artwork.",
        "Une phrase suffit : un EAN-13 1D ne porte que le GTIN, alors qu'un code 2D porte le même GTIN plus le lot, le numéro de série et une URL résoluble de la forme https://id.gs1.org/01/{GTIN}/10/{lot}/21/{serie}. En caisse, cette URL donne le prix et la fiche produit ; après la vente, c'est le seul chemin concret pour remonter au lot d'étiquettes qui a déteint au lavage. Pour un fournisseur d'accessoires, la conséquence est directe : le support, la taille et la note d'acceptation du code entrent dans le cahier des charges.",
        "Una frase resume la diferencia: un EAN-13 1D solo lleva el GTIN, mientras que un código 2D lleva el mismo GTIN más el lote, el número de serie y una URL resoluble del tipo https://id.gs1.org/01/{GTIN}/10/{lote}/21/{serie}. En caja esa URL devuelve precio y ficha de producto; tras la venta es la única vía práctica para volver al lote cuyas etiquetas destiñeron en el lavado. Para un proveedor de accesorios es concreto: el soporte, el tamaño y la nota de aceptación del código pasan a la ficha técnica.",
        "要点は一行で足ります。1次元 EAN-13 は GTIN だけを持ち、2次元コードは同じ GTIN にロット、シリアル、解決可能な URL（https://id.gs1.org/01/{GTIN}/10/{ロット}/21/{シリアル}）を加えられます。レジでは価格と商品情報に、販売後は洗濯で色移りしたロットまで戻る唯一の実務的な経路になります。副資材メーカーにとっては、コードの媒体・寸法・合格基準が仕様書の一部になる、という意味です。",
        "한 문장으로 정리됩니다. 1차원 EAN-13은 GTIN만 담고, 2차원 코드는 같은 GTIN에 로트, 시리얼, 해석 가능한 URL(https://id.gs1.org/01/{GTIN}/10/{로트}/21/{시리얼})을 더합니다. 계산대에서는 가격과 상품 정보로, 판매 후에는 세탁에서 이염된 로트까지 되짚는 유일한 실무 경로가 됩니다. 부자재 업체에는 코드의 매체·크기·합격 기준이 사양서의 일부가 된다는 뜻입니다.",
    )),

    ("h2", L(
        "2. 決定版面的是三個數字：模組、靜區、標籤寬度",
        "2. Three numbers decide the layout: module, quiet zone, label width",
        "2. Trois chiffres décident de la mise en page : module, zone de silence, largeur d'étiquette",
        "2. Tres cifras deciden la maqueta: módulo, zona de silencio, ancho de etiqueta",
        "2. レイアウトを決める三つの数値：モジュール、余白（クワイエットゾーン）、ラベル幅",
        "2. 레이아웃을 정하는 세 숫자: 모듈, 여백(콰이어트 존), 라벨 폭",
    )),

    ("p", L(
        "GS1 以 X 尺寸（單一模組寬度）為基準。零售 POS 掃描一般規範在每模組 0,4 至 0,5 mm；只做物流追溯的碼可以細到約 0,25 mm。含批號與序號的 Digital Link 通常需要 29 至 33 個模組，以 0,5 mm 計，符號本身約 15 至 17 mm 見方，加上四周各 4 個模組的靜區（DataMatrix 只需 1 個模組），實際要佔 19 至 21 mm，才輪得到旁邊排文字。對折疊洗水標來說，這就是 20 mm 與 30 mm 的差別。",
        "GS1 works from the X-dimension, the width of one module. Retail POS scanning is normally specified at 0,4 to 0,5 mm per module; a logistics-only code can go thinner, around 0,25 mm. A Digital Link carrying lot and serial typically needs 29 to 33 modules, so at 0,5 mm the symbol alone is roughly 15 to 17 mm square, and a QR code needs a four-module quiet zone on all sides (a DataMatrix needs one) — about 19 to 21 mm before any text fits beside it. On a folded care label that is the difference between a 20 mm and a 30 mm label.",
        "GS1 raisonne en dimension X, la largeur d'un module. Le scan en caisse est généralement spécifié entre 0,4 et 0,5 mm par module ; un code destiné à la seule logistique descend vers 0,25 mm. Un Digital Link portant lot et série demande en pratique 29 à 33 modules : à 0,5 mm, le symbole fait 15 à 17 mm de côté, et un QR exige une zone de silence de quatre modules sur chaque côté (un seul pour un DataMatrix), soit 19 à 21 mm avant de loger du texte à côté. Sur une étiquette pliée, c'est la différence entre 20 mm et 30 mm.",
        "GS1 trabaja con la dimensión X, el ancho de un módulo. El escaneo en caja se especifica normalmente entre 0,4 y 0,5 mm por módulo; un código solo para logística baja a unos 0,25 mm. Un Digital Link con lote y serie suele necesitar 29 a 33 módulos: a 0,5 mm el símbolo mide 15 a 17 mm de lado, y un QR exige zona de silencio de cuatro módulos por lado (uno solo en DataMatrix), es decir 19 a 21 mm antes de colocar texto al lado. En una etiqueta doblada, esa es la diferencia entre 20 mm y 30 mm.",
        "GS1 は X 寸法（モジュール1個の幅）を基準にします。店頭 POS の読み取りは通常 0.4〜0.5 mm/モジュールで指定され、物流用途だけなら 0.25 mm 程度まで細くできます。ロットとシリアルを含む Digital Link は通常 29〜33 モジュールを要し、0.5 mm なら記号自体が 15〜17 mm 角、QR は四周に 4 モジュールの余白（DataMatrix は 1 モジュール）が必要なので、横に文字を置く前に 19〜21 mm を占めます。折り返しの洗濯表示ラベルでは、これが 20 mm と 30 mm の差になります。",
        "GS1은 X 치수(모듈 하나의 폭)를 기준으로 합니다. 매장 POS 판독은 보통 모듈당 0.4~0.5 mm로 지정되고, 물류용만이면 0.25 mm 정도까지 좁힐 수 있습니다. 로트와 시리얼을 담는 Digital Link는 보통 29~33개 모듈이 필요해, 0.5 mm 기준 기호 자체가 15~17 mm 정사각형이고, QR은 사방 4개 모듈(DataMatrix는 1개)의 여백이 필요해 옆에 문자를 넣기 전에 19~21 mm를 차지합니다. 접이식 케어 라벨에서는 이것이 20 mm와 30 mm의 차이입니다.",
    )),

    ("h2", L(
        "3. 哪種承載方式撐得住這個碼",
        "3. Which carrier and print method can hold it",
        "3. Quel support et quel procédé tiennent le code",
        "3. Qué soporte y qué método de impresión sostienen el código",
        "3. どの媒体・印刷方式ならコードを保持できるか",
        "3. 어떤 매체와 인쇄 방식이 코드를 견디는가",
    )),

    ("table",
     [L("承載方式／印刷", "Carrier and print", "Support et impression", "Soporte e impresión", "媒体・印刷", "매체·인쇄"),
      L("實務模組下限", "Practical minimum module", "Module minimal réel", "Módulo mínimo real", "実務上の最小モジュール", "실무 최소 모듈"),
      L("判斷", "Verdict", "Verdict", "Veredicto", "判断", "판단")],
     [[L("熱轉印洗水標 300 dpi", "Thermal transfer care label, 300 dpi", "Étiquette d'entretien transfert thermique 300 dpi", "Etiqueta de cuidado por transferencia térmica 300 dpi", "サーマル転写の洗濯表示 300 dpi", "열전사 케어 라벨 300 dpi"),
       L("0,25 mm", "0,25 mm", "0,25 mm", "0,25 mm", "0.25 mm", "0.25 mm"),
       L("首選：溫度與張力穩就能穩定出碼", "Default: stable heat and tension gives repeatable codes", "Choix par défaut : température et tension stables donnent des codes réguliers", "Opción por defecto: temperatura y tensión estables dan códigos repetibles", "第一候補。温度と張力を安定させれば安定して出せます", "우선 선택. 온도와 장력을 안정시키면 재현됩니다")],
      [L("膠印吊牌＋霧膜", "Offset hang tag with matte lamination", "Hangtag offset avec pelliculage mat", "Colgante offset con laminado mate", "オフセット下げ札＋マットラミ", "오프셋 행택 + 매트 라미네이팅"),
       L("0,30 mm", "0,30 mm", "0,30 mm", "0,30 mm", "0.30 mm", "0.30 mm"),
       L("可用：霧膜防反光，別壓亮膜", "Workable: matte kills glare, avoid gloss", "Utilisable : le mat tue le reflet, éviter le brillant", "Viable: el mate elimina el brillo, evite el brillante", "可。マットは反射を抑えます。グロスは避けます", "가능. 매트는 반사를 줄입니다. 광택은 피하십시오")],
      [L("織嘜", "Woven label", "Étiquette tissée", "Etiqueta tejida", "織りラベル", "직조 라벨"),
       L("0,60 mm 以上", "0,60 mm or more", "0,60 mm ou plus", "0,60 mm o más", "0.60 mm 以上", "0.60 mm 이상"),
       L("多數不可靠：起毛糊邊，改印刷標或放大", "Often unreliable: fuzz blurs modules; print instead", "Souvent peu fiable : le duvet brouille les modules ; imprimer plutôt", "A menudo poco fiable: la pelusa emborrona módulos; mejor imprimir", "多くは不安定。毛羽でモジュールが崩れるため印刷ラベルか大型化で対応", "대부분 불안정. 보풀로 모듈이 뭉개져 인쇄 라벨이나 확대 적용")],
      [L("膠袋熱轉貼紙", "Thermal transfer sticker on poly bag", "Sticker transfert thermique sur sachet", "Sticker por transferencia térmica en bolsa", "ポリ袋のサーマル転写シール", "비닐봉투 열전사 스티커"),
       L("0,30 mm", "0,30 mm", "0,30 mm", "0,30 mm", "0.30 mm", "0.30 mm"),
       L("可用：別用熱感紙，會褪色", "Workable: skip direct thermal, it fades", "Utilisable : éviter le thermique direct, il pâlit", "Viable: evite el térmico directo, se desvanece", "可。感熱紙は退色するので不可", "가능. 감열지는 퇴색하므로 사용 금지")]]),

    ("h2", L(
        "4. 對比度與驗碼：退貨幾乎都在這裡",
        "4. Contrast and verification: where lots fail",
        "4. Contraste et vérification : c'est là que les lots échouent",
        "4. Contraste y verificación: aquí fallan los lotes",
        "4. コントラストと検証：不合格はここで起きます",
        "4. 대비와 검증: 불합격은 여기서 나옵니다",
    )),

    ("p", L(
        "碼要黑墨白底、安靜無干擾。銀箔、燙金與亮膜壓在碼上，等於直接把可讀性交給了運氣。驗碼依 ISO/IEC 15415 評 A 至 F，零售端一般要求 C（1,5）以上，B（2,5）以上更穩；重要的是每批抽 5 至 10 個碼上機實測並留檔，因為打樣通過從來不等於大貨通過——熱轉印的溫度漂移與碳帶批次差異，往往在第三千米才出現。",
        "The code needs black on white and nothing touching it. Foil, hot stamping and gloss lamination over the code hand readability to luck. Verification follows ISO/IEC 15415, graded A to F; retail usually accepts C (1,5) and prefers B (2,5) or better. What matters is testing five to ten codes per lot and keeping the reports, because a passing proof never proves a passing production run — thermal transfer drifts with head temperature and ribbon batch, often three thousand metres in.",
        "Le code exige du noir sur blanc et rien qui le touche. Feuille métallisée, dorure à chaud et pelliculage brillant sur le code confient la lisibilité au hasard. La vérification suit ISO/IEC 15415, notée de A à F ; le commerce de détail accepte en général C (1,5) et préfère B (2,5). L'essentiel : tester cinq à dix codes par lot et conserver les rapports, car une épreuve réussie ne prouve jamais un tirage réussi — la dérive de température et les lots de ruban apparaissent souvent après trois mille mètres.",
        "El código necesita negro sobre blanco y nada encima. Foil, estampado en caliente y laminado brillante sobre el código dejan la legibilidad al azar. La verificación sigue ISO/IEC 15415, de A a F; el retail suele aceptar C (1,5) y prefiere B (2,5). Lo importante es medir cinco a diez códigos por lote y guardar los informes, porque una prueba aprobada nunca demuestra una producción aprobada: la deriva de temperatura y los lotes de cinta aparecen a los tres mil metros.",
        "コードは黒白で、上に何も重ねないことが前提です。箔、烫金、グロスラミネートをコードに重ねると読取性は運任せになります。検証は ISO/IEC 15415 で A〜F 評価、小売は通常 C（1.5）以上、B（2.5）以上が望ましい水準です。重要なのはロットごとに 5〜10 個を実測し記録を残すこと。試作の合格は量産の合格を証明しません。サーマル転写はヘッド温度とリボンのロット差で、3,000 m を過ぎてから崩れることがあります。",
        "코드는 검정 잉크에 흰 바탕, 위에 아무것도 겹치지 않아야 합니다. 포일, 박, 광택 라미네이팅이 코드를 덮으면 판독성은 운에 맡기는 셈입니다. 검증은 ISO/IEC 15415로 A~F 등급을 매기며, 유통은 보통 C(1.5) 이상을 요구하고 B(2.5) 이상을 선호합니다. 중요한 것은 로트마다 5~10개를 실측하고 성적서를 남기는 일입니다. 시험 인쇄 합격이 양산 합격을 뜻하지는 않습니다. 열전사는 헤드 온도와 리본 로트 차이로 3,000 m를 넘긴 뒤 무너지기도 합니다.",
    )),

    ("ul", [
        L("亮膜或燙金壓在碼上，掃描器直接讀不到", "Gloss lamination or foil over the code: the scanner simply cannot read it", "Pelliculage brillant ou dorure sur le code : le scanner ne lit pas", "Laminado brillante o foil sobre el código: el escáner no lee", "グロスや箔がコードに重なると読み取れません", "광택 라미네이팅이나 박이 코드를 덮으면 판독되지 않습니다"),
        L("靜區被裁切，或旁邊壓了文字與壓痕", "Quiet zone trimmed away, or text and creasing pressed beside it", "Zone de silence rognée, ou texte et pliure à côté", "Zona de silencio recortada, o texto y pliegue al lado", "余白が断裁で削られ、隣に文字や折り目が来ている", "여백이 재단되어 사라졌거나 옆에 문자와 접힘이 있습니다"),
        L("織嘜起毛、熱轉印溫度不足，模組邊緣糊在一起", "Woven fuzz or under-heated transfer blurs the module edges together", "Duvet de tissage ou transfert sous-chauffé : les bords de module se fondent", "Pelusa del tejido o transferencia fría: los bordes de módulo se funden", "織り毛羽や転写温度不足でモジュールの縁が溶けてつながる", "직조 보풀이나 전사 온도 부족으로 모듈 경계가 뭉개집니다"),
    ]),

    ("h2", L(
        "5. 法規要的是可查，不是好聽",
        "5. What the law asks for: traceability, not a slogan",
        "5. Ce que la loi demande : la traçabilité, pas un slogan",
        "5. Lo que exige la ley: trazabilidad, no un eslogan",
        "5. 法規が求めるのは「追えること」であり、聞こえの良さではありません",
        "5. 법규가 요구하는 것은 추적 가능성이며, 그럴듯한 문구가 아닙니다",
    )),

    ("p", L(
        "歐盟《通用產品安全條例》(EU) 2023/988 自 2024 年 12 月 13 日起適用，要求產品可識別、可追溯，並具名負責的經濟營運者。對輔料而言，一個能解析到批次資料的二維碼是最便宜的解法，因為標籤本來就縫在成衣上。日本《家庭用品品質表示法》規定的成分與洗護標示、韓國《品質管理及工業品安全管理法》下的品質標示，都要求「印在標籤上的資訊本身看得見」——二維碼是補充，不是替代。把這點寫進規格書，能省掉日後與買家爭執的一整輪。",
        "In the EU, Regulation (EU) 2023/988 on general product safety has applied since 13 December 2024 and expects a product to be identifiable and traceable, with a named responsible economic operator. For a trim, a 2D code that resolves to batch data is the cheapest way to satisfy that, because the label is already on the garment. Japan's Household Goods Quality Labelling Act governs composition and care marking, and Korea's Quality Management and Industrial Products Safety Control Act governs quality labelling; both require the printed information itself to be visible — a QR code supplements it, never replaces it. Writing that into the specification saves a whole round of argument later.",
        "Dans l'Union, le règlement (UE) 2023/988 sur la sécurité générale des produits s'applique depuis le 13 décembre 2024 : le produit doit être identifiable et traçable, avec un opérateur économique responsable désigné. Pour un accessoire, un code 2D qui résout vers les données de lot est la solution la moins chère, puisque l'étiquette est déjà cousue au vêtement. En France, la composition et l'entretien relèvent des mentions obligatoires du code de la consommation : le QR code complète le marquage imprimé, il ne le remplace pas. Écrire cette règle dans le cahier des charges évite un cycle complet de discussion avec l'acheteur.",
        "En la Unión, el Reglamento (UE) 2023/988 de seguridad general de los productos se aplica desde el 13 de diciembre de 2024: el producto debe ser identificable y trazable, con un operador económico responsable designado. Para un accesorio, un código 2D que resuelve a los datos de lote es la vía más barata, porque la etiqueta ya está cosida a la prenda. En España, la composición y el cuidado siguen sujetos a la información obligatoria de la normativa de consumo: el QR complementa el marcado impreso, no lo sustituye. Dejarlo escrito en la ficha técnica ahorra una ronda entera de discusión con el comprador.",
        "EU では製品安全に関する規則 (EU) 2023/988 が 2024年12月13日から適用され、製品の識別・追跡と、責任を負う事業者の明示が求められます。副資材では、既に縫い付けられたラベルにロット情報へ解決する2次元コードを載せるのが最も安価な方法です。日本では組成と取扱いの表示が家庭用品品質表示法にもとづく品質表示として義務づけられ、印刷された情報そのものが見えている必要があります。QR コードはそれを補うもので、置き換えにはなりません。この線引きを仕様書に書いておけば、買い手との議論を一巡節約できます。",
        "EU에서는 제품안전 규정 (EU) 2023/988이 2024년 12월 13일부터 적용되어 제품 식별·추적과 책임 있는 사업자 표시를 요구합니다. 부자재에서는 이미 봉제된 라벨에 로트 정보로 연결되는 2차원 코드를 얹는 것이 가장 저렴한 방법입니다. 한국에서는 섬유제품의 품질 표시와 취급 표시가 품질경영 및 공산품 안전관리법의 적용을 받고, 인쇄된 정보 자체가 보여야 합니다. QR 코드는 이를 보완할 뿐 대체하지 않습니다. 이 경계를 사양서에 적어 두면 구매팀과의 논의를 한 차례 줄일 수 있습니다.",
    )),

    ("callout", L(
        "買手只問一句話：掃這個碼，能不能分辨到批次與序號？答不出來，就還沒準備好。",
        "The buying team asks one question: does this code resolve to a batch and a serial? If the answer is no, the label is not ready.",
        "L'acheteur ne pose qu'une question : ce code résout-il un lot et un numéro de série ? Si non, l'étiquette n'est pas prête.",
        "El comprador hace una sola pregunta: ¿este código resuelve lote y número de serie? Si la respuesta es no, la etiqueta no está lista.",
        "買い手の質問は一つです。このコードはロットとシリアルまで解決できるか。できないなら、まだ準備できていません。",
        "구매팀의 질문은 하나입니다. 이 코드가 로트와 시리얼까지 연결되는가. 아니라면 아직 준비되지 않은 것입니다.",
    )),

    ("h2", L(
        "6. 2027 前的試點清單",
        "6. A pilot checklist before 2027",
        "6. Une liste de pilote avant 2027",
        "6. Lista de piloto antes de 2027",
        "6. 2027 年までのパイロットチェックリスト",
        "6. 2027년 전 파일럿 체크리스트",
    )),

    ("ol", [
        L("拿現有洗水標與吊牌，用買家的掃描器實測，不要用手機相機代替", "Test existing care labels and hang tags on the buyer's scanner, not a phone camera", "Tester les étiquettes existantes sur le scanner de l'acheteur, pas avec un téléphone", "Probar etiquetas existentes en el escáner del comprador, no con el móvil", "既存ラベルを買い手のスキャナで実測する（スマホのカメラで代用しない）", "기존 라벨을 구매팀 스캐너로 실측합니다(휴대폰 카메라로 대체 금지)"),
        L("定下模組尺寸與靜區，寫進規格書，連 GTIN 前綴一起交給供應商", "Fix module size and quiet zone in the spec, and pass the GTIN prefix to the supplier", "Fixer module et zone de silence au cahier des charges, et transmettre le préfixe GTIN", "Fijar módulo y zona de silencio en la ficha, y pasar el prefijo GTIN", "モジュール寸法と余白を仕様書に固定し、GTIN プレフィックスも渡す", "모듈 크기와 여백을 사양서에 확정하고 GTIN 프리픽스도 전달합니다"),
        L("打樣即上 ISO/IEC 15415 驗碼，要求 B（2,5）以上", "Verify at proof stage to ISO/IEC 15415, asking for B (2,5) or better", "Vérifier dès l'épreuve selon ISO/IEC 15415, en visant B (2,5)", "Verificar desde la prueba según ISO/IEC 15415, pidiendo B (2,5)", "試作段階で ISO/IEC 15415 検証を行い、B（2.5）以上を求める", "시험 단계에서 ISO/IEC 15415 검증, B(2.5) 이상 요구"),
        L("大貨每批抽 5 至 10 個碼留檔，出問題時這是唯一能自證的資料", "Keep five to ten verified codes per production lot; it is the only evidence you can show later", "Conserver cinq à dix codes vérifiés par lot : c'est la seule preuve opposable", "Guardar cinco a diez códigos verificados por lote: es la única prueba defendible", "量産ロットごとに 5〜10 個の検証記録を残す。問題時の唯一の証拠になります", "양산 로트마다 5~10개 검증 기록을 보관합니다. 문제 시 유일한 증거입니다"),
    ]),
]

ART2 = [
    ("p", L(
        "原產地文件是輔料訂單裡最便宜的一項，也是最貴的錯誤：一張有效的優惠原產地證，可以讓織嘜或吊牌的關稅率差上好幾個百分點；一個申報錯誤，就足以讓整個貨櫃在邊境壓上一週。本文講清哪種證書適用、原料是進口紗或進口紙時原產地怎麼判、供應商該交哪些資料，以及退證最常見的四個原因。",
        "Origin paperwork is the cheapest line in a trims order and the most expensive thing to get wrong: a valid preferential certificate of origin can move the duty rate on woven labels or hang tags by several percentage points, and one mis-declaration can hold a container at the border for a week. This guide covers which certificate applies, how origin is judged when the yarn or paper is imported, what your trims supplier must hand over, and the four reasons certificates get rejected.",
        "Les documents d'origine sont la ligne la moins chère d'une commande d'accessoires et l'erreur la plus coûteuse : un certificat d'origine préférentiel valide déplace le taux de douane sur les étiquettes tissées ou les hangtags de plusieurs points, et une déclaration erronée immobilise un conteneur une semaine. Ce guide couvre le certificat applicable, la détermination de l'origine quand le fil ou le papier est importé, les pièces à fournir et les quatre motifs de rejet.",
        "Los documentos de origen son la línea más barata de un pedido de accesorios y el error más caro: un certificado de origen preferencial válido mueve el arancel de etiquetas tejidas o colgantes varios puntos, y una declaración errónea retiene un contenedor una semana en frontera. Esta guía cubre qué certificado aplica, cómo se determina el origen cuando el hilo o el papel son importados, qué debe entregar el proveedor y los cuatro motivos de rechazo.",
        "原産地書類は副資材の発注で最も安い項目であり、最も高くつく誤りです。有効な特恵原産地証明書は織りラベルや下げ札の関税率を数ポイント動かし、申告ミス一つでコンテナが国境で一週間止まります。本記事ではどの証明書が当てはまるか、糸や紙が輸入品のときに原産地をどう判定するか、供應商が何を提出すべきか、そして却下される四つの原因を整理します。",
        "원산지 서류는 부자재 주문에서 가장 싼 항목이자 가장 비싼 실수입니다. 유효한 특혜 원산지증명서는 직조 라벨이나 행택의 관세율을 몇 퍼센트포인트 움직이고, 신고 오류 하나로 컨테이너가 국경에서 일주일 멈춥니다. 이 글은 어떤 증명서가 적용되는지, 원사나 종이가 수입품일 때 원산지를 어떻게 판정하는지, 공급사가 무엇을 제출해야 하는지, 반려되는 네 가지 이유를 정리합니다.",
    )),

    ("h2", L(
        "1. 三種稅率，一張紙決定",
        "1. Three duty rates, one piece of paper",
        "1. Trois taux de douane, une feuille de papier",
        "1. Tres tipos arancelarios, un papel",
        "1. 三つの税率を分ける一枚の紙",
        "1. 세 가지 관세율을 가르는 한 장의 서류",
    )),

    ("p", L(
        "同一箱吊牌進入同一市場，可能適用三種稅率：最惠國稅率、自由貿易協定下的優惠稅率，以及貿易救濟措施帶來的加徵稅率。把它們分開的是文件，不是產品本身——HS 歸類加上原產地證據。輔料單價低，所以買家往往最後才查，然後被延誤嚇到：一張 30 × 60 mm、350 g/m² 的吊牌，稅金本身微不足道，壓在港口的倉租與缺貨才是真成本。",
        "The same carton of hang tags can enter the same market at three different rates: MFN, a preferential rate under a free trade agreement, and an additional rate when a trade measure applies. What separates them is documentary — HS classification plus origin evidence — not the product itself. Trims are low-value, so buyers check them last and are then surprised by the delay: the duty on a 30 × 60 mm hang tag in 350 g/m² board at 0,10 USD is trivial, the detention and the stock-out are not.",
        "Le même carton de hangtags peut entrer sur un marché à trois taux : NPF, taux préférentiel d'un accord de libre-échange, et taux additionnel en cas de mesure commerciale. Ce qui les sépare est documentaire — classement SH et preuve d'origine — pas le produit. Les accessoires sont de faible valeur, donc l'acheteur vérifie en dernier et découvre le retard : la douane sur un hangtag de 30 × 60 mm en carton 350 g/m² à 0,10 USD est dérisoire, l'immobilisation et la rupture non.",
        "El mismo cartón de colgantes puede entrar en un mercado con tres tipos: NMF, tipo preferencial de un acuerdo de libre comercio y tipo adicional si hay una medida comercial. Lo que los separa es documental — clasificación SA y prueba de origen — no el producto. Los accesorios son de bajo valor, así que el comprador lo revisa al final y descubre el retraso: el arancel de un colgante de 30 × 60 mm en cartón de 350 g/m² a 0,10 USD es trivial, la retención y la rotura de stock no.",
        "同じ段ボール箱の下げ札でも、同じ市場に三つの税率で入ります。MFN 税率、自由貿易協定による特恵税率、貿易措置による追加税率です。これを分けるのは製品ではなく書類——HS 分類と原産地の証拠です。副資材は単価が低いため買い手は最後に確認し、遅延に驚きます。30 × 60 mm、350 g/m² の下げ札の関税は 0.10 米ドルで取るに足りませんが、滞留と欠品は違います。",
        "같은 박스의 행택이 같은 시장에 세 가지 세율로 들어갈 수 있습니다. MFN 세율, 자유무역협정 특혜 세율, 무역조치에 따른 추가 세율입니다. 이를 가르는 것은 제품이 아니라 서류, 즉 HS 분류와 원산지 증빙입니다. 부자재는 단가가 낮아 구매팀이 마지막에 확인하고 지연에 놀랍니다. 30 × 60 mm, 350 g/m² 판지 행택의 관세는 0.10 USD로 미미하지만 체류와 결품은 그렇지 않습니다.",
    )),

    ("h2", L(
        "2. 常見的五種原產地文件",
        "2. Five documents you will be asked for",
        "2. Cinq documents que l'on vous demandera",
        "2. Cinco documentos que le pedirán",
        "2. 求められる五つの原産地書類",
        "2. 요구받는 다섯 가지 원산지 서류",
    )),

    ("ul", [
        L("一般原產地證（CO）：在中國由海關或貿促會簽發，只證明原產地，不帶優惠稅率", "Non-preferential CO: issued in China by Customs or CCPIT; it certifies origin but carries no preferential rate", "CO non préférentiel : délivré en Chine par la douane ou le CCPIT ; il atteste l'origine sans taux préférentiel", "CO no preferencial: emitido en China por la aduana o el CCPIT; acredita origen sin tipo preferencial", "一般原産地証明（CO）：中国では税関または CCPIT が発給。原産地を証明しますが特恵税率は伴いません", "일반 원산지증명서(CO): 중국에서는 세관 또는 CCPIT이 발급하며, 원산지만 증명하고 특혜 세율은 없습니다"),
        L("FORM E：中國—東盟自貿協定用，出口東南亞時最常被要求", "Form E: the ASEAN–China FTA certificate, most often requested for South-East Asia", "Form E : certificat ALE ASEAN–Chine, le plus souvent demandé pour l'Asie du Sud-Est", "Form E: certificado del ALC ASEAN–China, el más pedido para el Sudeste Asiático", "FORM E：ASEAN・中国 FTA 用。東南アジア向けで最も要求されます", "FORM E: ASEAN-중국 FTA용. 동남아 수출에서 가장 많이 요구됩니다"),
        L("RCEP 原產地證：區域全面經濟夥伴協定，同一票貨可對不同成員國擇優適用", "RCEP certificate: under the Regional Comprehensive Economic Partnership, one shipment can pick the best rate per member state", "Certificat RCEP : un même envoi peut choisir le meilleur taux par État membre", "Certificado RCEP: un mismo envío puede elegir el mejor tipo por Estado miembro", "RCEP 原産地証明：同一出荷で加盟国ごとに有利な税率を選べます", "RCEP 원산지증명서: 같은 선적에 대해 회원국별로 유리한 세율을 선택할 수 있습니다"),
        L("FORM A：普惠制證書；中國已被歐盟於 2015 年畢業，美國 GSP 亦已失效，現在用得很少", "Form A: the GSP certificate; the EU graduated China in 2015 and the US GSP has lapsed, so it is rarely used now", "Form A : certificat SPG ; l'UE a gradué la Chine en 2015 et le SPG américain a expiré, donc rarement utilisé", "Form A: certificado SGP; la UE graduó a China en 2015 y el SGP de EE. UU. expiró, por lo que apenas se usa", "FORM A：一般特恵（GSP）証明書。EU は 2015 年に中国を卒業扱い、米国の GSP も失効し、現在はほとんど使いません", "FORM A: 일반특혜(GSP) 증명서. EU는 2015년 중국을 졸업 처리했고 미국 GSP도 실효되어 지금은 거의 쓰지 않습니다"),
        L("出口商自我聲明：歐盟 REX 制度下的 origin statement，不必逐票簽證，但要備註冊號", "Exporter self-declaration: an origin statement under the EU REX system, no per-shipment certification, but a registration number is required", "Auto-déclaration de l'exportateur : sous le régime REX, pas de visa par envoi, mais un numéro d'enregistrement", "Autodeclaración del exportador: bajo el sistema REX, sin visado por envío, pero con número de registro", "輸出者による自己申告：EU の REX 制度では船ごとの査証は不要ですが登録番号が必要です", "수출자 자체 선언: EU REX 제도에서는 선적별 인증이 없지만 등록번호가 필요합니다"),
    ]),

    ("h2", L(
        "3. 原料進口時，輔料的原產地怎麼判",
        "3. When the yarn or paper is imported: how origin is judged",
        "3. Quand le fil ou le papier est importé : comment l'origine est déterminée",
        "3. Cuando el hilo o el papel son importados: cómo se determina el origen",
        "3. 糸や紙が輸入品のとき、原産地をどう判定するか",
        "3. 원사나 종이가 수입품일 때 원산지 판정",
    )),

    ("p", L(
        "兩條路徑：完全取得（輔料幾乎用不到）與實質改變（常態）。實質改變看三件事之一——稅則號列改變（CTH）、區域價值成分達標（RCEP 常見門檻為 40%），或符合產品特定加工規則。把進口紙裁成吊牌，單靠裁切通常不夠；但從進口卡紙印刷、上膜、模切成吊牌，在滿足產品特定規則的前提下通常成立。報優惠價之前，先要一份寫明規則的文件；假設 CTH 卻沒查產品特定規則的供應商，最後是在海關而不是在打樣階段輸掉這場爭論。",
        "Two routes: wholly obtained, which trims almost never are, and substantial transformation, which is the normal one. Substantial transformation is met by one of three things — a change of tariff heading (CTH), a regional value content threshold (40 % is the usual RCEP figure), or a product-specific process rule. Cutting imported board into hang tags is normally not enough on its own; printing, laminating and die-cutting a tag from imported board usually is, provided the specific rule is met. Ask for the rule in writing before quoting a preferential price: a supplier who assumes CTH without checking the product-specific rule loses that argument at Customs, not at the sample stage.",
        "Deux voies : entièrement obtenu, ce que les accessoires ne sont presque jamais, et transformation substantielle, la voie normale. Celle-ci est remplie par l'un des trois critères : changement de position tarifaire (CTH), seuil de valeur régionale (40 % est le chiffre courant en RCEP), ou règle de processus spécifique au produit. Découper du carton importé en hangtags ne suffit généralement pas ; imprimer, pelliculer et découper à l'emporte-pièce à partir de carton importé suffit en général, si la règle est respectée. Exigez la règle par écrit avant de coter un prix préférentiel : un fournisseur qui suppose le CTH sans vérifier la règle spécifique perd le débat en douane, pas à l'épreuve.",
        "Dos vías: totalmente obtenido, lo que los accesorios casi nunca son, y transformación sustancial, la normal. Esta se cumple por uno de tres criterios: cambio de partida arancelaria (CTH), umbral de valor regional (40 % es la cifra habitual en RCEP) o una regla de proceso específica del producto. Cortar cartón importado en colgantes no suele bastar; imprimir, laminar y troquelar a partir de cartón importado normalmente sí, si se cumple la regla. Pida la regla por escrito antes de cotizar un precio preferencial: quien supone CTH sin revisar la regla específica pierde el debate en la aduana, no en la muestra.",
        "二つの経路があります。完全取得（副資材ではほぼ該当しません）と実質的変更（通常はこちら）です。実質的変更は三つのいずれかで満たします——関税分類番号の変更（CTH）、域内付加価値の基準（RCEP では 40 % が一般的）、製品別の加工要件です。輸入した板紙を下げ札に断裁するだけでは通常不十分ですが、輸入板紙から印刷・ラミネート・型抜きする場合は、製品別要件を満たせば成立します。特恵価格を提示する前に、要件を書面で求めてください。CTH を前提にしたまま製品別要件を確認しない供應商は、試作ではなく通関で負けます。",
        "경로는 두 가지입니다. 완전 획득(부자재에는 거의 해당하지 않음)과 실질적 변형(보통 이쪽)입니다. 실질적 변형은 세 가지 중 하나로 충족합니다. 관세분류번호 변경(CTH), 역내 부가가치 기준(RCEP에서 흔히 40%), 제품별 가공 요건입니다. 수입 판지를 행택으로 재단하는 것만으로는 대개 부족하고, 수입 판지에서 인쇄·라미네이팅·타발까지 하면 제품별 요건을 충족할 때 성립합니다. 특혜 가격을 제시하기 전에 요건을 서면으로 요구하십시오. CTH만 가정하고 제품별 요건을 확인하지 않은 공급사는 시험 단계가 아니라 통관에서 집니다.",
    )),

    ("h2", L(
        "4. 供應商要交的四份資料",
        "4. What your trims supplier must hand over",
        "4. Ce que le fournisseur doit remettre",
        "4. Lo que debe entregar el proveedor",
        "4. 供應商が提出すべき四つの資料",
        "4. 공급사가 제출해야 할 네 가지 자료",
    )),

    ("ul", [
        L("帶材料原產地的 BOM：紗線、紙張、薄膜的來源與 HS 前六位", "A BOM with material origin: source and first six HS digits for yarn, paper and film", "Une nomenclature avec l'origine des matières : source et six premiers chiffres SH du fil, du papier, du film", "Una lista de materiales con origen: fuente y primeros seis dígitos SA de hilo, papel y film", "材料原産地つきの BOM：糸・紙・フィルムの出所と HS 上6桁", "자재 원산지가 포함된 BOM: 원사·종이·필름의 출처와 HS 앞 6자리"),
        L("生產成本明細：用於區域價值成分計算，需能對上發票金額", "A production cost breakdown for the regional value calculation, reconcilable with the invoice", "Un détail des coûts de production pour le calcul de la valeur régionale, rapprochable de la facture", "Un desglose de costes de producción para el valor regional, conciliable con la factura", "生産コスト明細：域内付加価値の計算用で、請求金額と突合できること", "생산원가 명세: 역내 부가가치 계산용이며 인보이스 금액과 맞아야 합니다"),
        L("原材料證明：上游發票、供應商聲明或原產地證", "Material evidence: upstream invoices, supplier declarations or origin certificates", "Preuves matières : factures amont, déclarations fournisseur ou certificats d'origine", "Pruebas de material: facturas de origen, declaraciones de proveedor o certificados de origen", "原材料の証拠：上流の請求書、供應商の宣言書、原産地証明", "원자재 증빙: 상위 인보이스, 공급사 선언서, 원산지증명서"),
        L("加工記錄：工序、日期與工廠，必要時含外發加工", "Process records: operations, dates and plant, including subcontracting where used", "Records de fabrication : opérations, dates et usine, sous-traitance incluse", "Registros de proceso: operaciones, fechas y planta, incluida la subcontratación", "加工記録：工程、日付、工場。外注がある場合はその記録も", "가공 기록: 공정, 일자, 공장. 외주가 있으면 그 기록도 포함"),
    ]),

    ("h2", L(
        "5. 原產地標示是另一項義務",
        "5. Origin marking is a separate obligation",
        "5. Le marquage d'origine est une obligation distincte",
        "5. El marcado de origen es una obligación distinta",
        "5. 原産国表示は別個の義務です",
        "5. 원산지 표시는 별개의 의무입니다",
    )),

    ("p", L(
        "有證書不等於標示合格。美國 19 CFR 134 要求最終購買者能看到清楚、牢固的國別標示；歐盟的非優惠原產地依《(EU) 2015/2446 授權條例》判定，成員國對進口貨物的原產地標示各有執行細則（法國同時受海關法典與消費法典約束）。日本一般不強制原產國標示，但一旦標示，就受《景品表示法》拘束，不得誤導；組成與洗護仍是《家庭用品品質表示法》下的獨立義務。韓國則由《對外貿易法》要求進口品標示原產地，《表示廣告法》禁止虛偽或引人誤認的原產地表示。輔料最常見的做法是在吊牌上印 Made in China——因為把標縫在吊牌上並不實際——但要確保它與證書一致，且說的是輔料的原產地，不是成衣的原產地。",
        "A certificate is not a marking. Under US 19 CFR 134 the ultimate purchaser must see the country of origin marked legibly and permanently; in the EU non-preferential origin follows Delegated Regulation (EU) 2015/2446, and member states enforce origin marking on imports under their own rules. A printed 'Made in China' on the hang tag is the usual carrier for trims, because sewing a label into a tag is not practical. Two mistakes recur: a mark that contradicts the certificate, and a mark that states the garment's origin rather than the trim's.",
        "Un certificat n'est pas un marquage. Aux États-Unis, le 19 CFR 134 impose une mention d'origine lisible et durable visible de l'acheteur final ; dans l'Union, l'origine non préférentielle suit le règlement (UE) 952/2013 et son règlement délégué (UE) 2015/2446, et chaque État membre applique son propre contrôle du marquage d'origine à l'importation — en France, le marquage relève aussi du code de la consommation. Pour un accessoire, la mention 'Made in China' imprimée sur le hangtag est le support habituel, car coudre une étiquette dans un carton n'est pas praticable. Deux erreurs reviennent : une mention qui contredit le certificat, et une mention qui donne l'origine du vêtement au lieu de celle de l'accessoire.",
        "Un certificado no es un marcado. En EE. UU., el 19 CFR 134 exige que el comprador final vea el país de origen de forma legible y permanente; en la UE el origen no preferencial se determina conforme al Reglamento (UE) 2015/2446 (acto delegado) y al código aduanero de la Unión, Reglamento (UE) 952/2013, y cada Estado miembro aplica su control de marcado de origen en importación — en España, junto con la información obligatoria de etiquetado de la normativa de consumo. En accesorios lo habitual es imprimir 'Made in China' en el colgante, porque coser una etiqueta en un cartón no es práctico. Dos errores se repiten: un marcado que contradice el certificado, y uno que indica el origen de la prenda en lugar del accesorio.",
        "証明書があっても表示が適切とは限りません。米国は 19 CFR 134 により最終購入者が読める恒久的な原産国表示を求めます。EU の非特恵原産地は委任規則 (EU) 2015/2446 に従い、加盟国がそれぞれ輸入時の原産国表示を執行します。日本では原産国表示は一般に義務ではありませんが、表示する場合は景品表示法にもとづき誤認を招かない正確な表示が必要です。組成や取扱いは家庭用品品質表示法にもとづく別個の義務で、原産国表示がこれを代替しません。副資材では下げ札への 'Made in China' 印刷が通例です。注意すべきは、証明書と矛盾する表示と、成品の原産国を書いてしまう誤りです。",
        "증명서가 있다고 표시가 적합한 것은 아닙니다. 미국은 19 CFR 134에 따라 최종 구매자가 읽을 수 있는 영구적 원산지 표시를 요구합니다. EU의 비특혜 원산지는 위임규정 (EU) 2015/2446을 따르고, 회원국이 각자 수입품 원산지 표시를 집행합니다. 한국에서는 대외무역법이 수입품의 원산지 표시를 요구하고, 표시광고법이 원산지 허위·오인 표시를 금지합니다. 섬유제품의 품질 표시와 취급 표시는 별개의 의무이며 원산지 표시가 이를 대체하지 않습니다. 부자재에서는 행택에 'Made in China'를 인쇄하는 것이 관행입니다. 반복되는 오류는 증명서와 모순되는 표시, 그리고 완제품의 원산지를 적는 것입니다.",
    )),

    ("h2", L(
        "6. 四個最常見的退證原因",
        "6. Four reasons certificates get rejected",
        "6. Quatre motifs de rejet",
        "6. Cuatro motivos de rechazo",
        "6. 却下される四つの原因",
        "6. 반려되는 네 가지 이유",
    )),

    ("ol", [
        L("發票金額與成本明細對不上，海關要求補件", "Invoice value does not reconcile with the cost breakdown, and Customs asks for more", "La facture ne se rapproche pas du détail de coûts : la douane demande des pièces", "La factura no cuadra con el desglose de costes y la aduana pide más papeles", "請求金額とコスト明細が合わず、税関が追加資料を要求", "인보이스 금액과 원가 명세가 맞지 않아 세관이 보완을 요구"),
        L("後發證手續沒走完，或超過允許期限", "Retroactive issuance was never completed, or the allowed window closed", "L'émission rétroactive n'a pas été finalisée ou le délai est dépassé", "La emisión retroactiva no se completó o el plazo venció", "後発発行の手続きが未完、または期限超過", "사후 발급 절차가 끝나지 않았거나 기한이 지남"),
        L("把成衣的原產地當成輔料的原產地（成衣在越南縫製，不代表吊牌原產越南）", "Treating the garment's origin as the trim's: sewing in Vietnam does not make the hang tag Vietnamese", "Confondre l'origine du vêtement et celle de l'accessoire : coudre au Vietnam ne rend pas le hangtag vietnamien", "Confundir el origen de la prenda con el del accesorio: coser en Vietnam no hace vietnamita el colgante", "成品の原産国を副資材の原産国と混同する（ベトナム縫製でも下げ札がベトナム製になるわけではありません）", "완제품 원산지를 부자재 원산지로 착각(베트남 봉제가 행택을 베트남산으로 만들지 않습니다)"),
        L("HS 歸類與證書不一致，海關退件重判", "HS classification and certificate disagree, and Customs re-classifies the file", "Classement SH et certificat divergent : la douane reclasse le dossier", "Clasificación SA y certificado no coinciden: la aduana reclasifica", "HS 分類と証明書が不一致で、税関が再分類", "HS 분류와 증명서가 불일치해 세관이 재분류"),
    ]),

    ("callout", L(
        "一張 CO 的成本低於一小時的海關滯留費——前提是產品特定原產地規則在報價前就查清楚，而不是在櫃子到港後。",
        "A certificate of origin costs less than an hour of customs detention — provided the product-specific rule was checked before the quote, not after the container landed.",
        "Un certificat d'origine coûte moins qu'une heure d'immobilisation douanière — à condition de vérifier la règle spécifique avant le devis, pas après l'arrivée du conteneur.",
        "Un certificado de origen cuesta menos que una hora de retención aduanera, siempre que la regla específica se revise antes de cotizar y no al llegar el contenedor.",
        "原産地証明書のコストは通関滞留一時間より安い——ただし製品別原産地規則を、コンテナ到着後ではなく見積前に確認した場合に限ります。",
        "원산지증명서 비용은 통관 체류 한 시간보다 쌉니다. 단, 컨테이너 도착 후가 아니라 견적 전에 제품별 원산지 요건을 확인했을 때입니다.",
    )),
]
