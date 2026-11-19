# -*- coding: utf-8 -*-
"""2026-11-19 20:00 批次 A：吊牌內容清單（hang tag content checklist）——哪些欄位能印在吊牌、哪些必須在耐久標籤。"""

SLUG = "hang-tag-content-checklist"
CATEGORY = {
    "zh": "標籤與吊牌", "en": "Labels & Hang Tags", "fr": "Étiquettes",
    "es": "Etiquetas", "ja": "ネーム・下げ札", "ko": "라벨·행택",
}
TITLE = {
    "zh": "吊牌該印什麼：9 個欄位與各自的法律歸屬 | TAGE",
    "en": "Hang Tag Content Checklist: 9 Fields and Where They Belong | TAGE",
    "fr": "Contenu d'une étiquette : 9 champs et leur place légale | TAGE",
    "es": "Contenido de la etiqueta colgante: 9 campos y su lugar legal | TAGE",
    "ja": "下げ札に何を刷るか：9 項目と法的な置き場所 | TAGE",
    "ko": "행택에 무엇을 인쇄할까: 9개 항목과 법적 위치 | TAGE",
}
DESC = {
    "zh": "吊牌要印什麼不是設計問題：品牌、款號、尺碼、條碼、成分、產地九個欄位，哪些能印在吊牌上、哪些必須印在耐久洗水標，附字高、條碼等級與五項打樣驗收。",
    "en": "What to print on a hang tag: nine fields, which must sit on a durable care label instead, type size limits, barcode grading and five proof checks.",
    "fr": "Que faut-il imprimer sur une étiquette ? Neuf champs, ceux qui doivent figurer sur une étiquette durable, hauteurs de caractères et contrôles avant production.",
    "es": "Qué imprimir en una etiqueta colgante: nueve campos, cuáles deben ir en una etiqueta duradera, cuerpos de letra y controles antes de producir.",
    "ja": "下げ札に何を刷るか。9 項目のうち耐久ラベルに置くべきもの、文字高の下限、バーコード等級、量産前の確認 5 項目まで実務目線で整理します。",
    "ko": "행택에 무엇을 인쇄할까. 9개 항목 중 내구성 라벨로 가야 할 것, 글자 높이 기준, 바코드 등급, 양산 전 점검 5항목까지 정리합니다.",
}
H1 = {
    "zh": "吊牌上該印什麼：九個欄位與它們的法律歸屬",
    "en": "What to Print on a Hang Tag: Nine Fields and Where They Belong",
    "fr": "Que faut-il imprimer sur une étiquette : neuf champs et leur place",
    "es": "Qué imprimir en una etiqueta colgante: nueve campos y su lugar",
    "ja": "下げ札に何を刷るか：9 項目とその置き場所",
    "ko": "행택에 무엇을 인쇄할까: 9개 항목과 그 위치",
}

BLOCKS = [
    ("p", {
        "zh": "每當品牌方問「吊牌要印什麼」，真正的問題其實有三層：買家在貨架前要找什麼、法規要求什麼信息必須隨產品走、平台與零售商又要掃什麼。九個最常見的欄位裡，只有六個適合印在吊牌上，另外三個的正確位置是耐久標籤。位置放錯，吊牌做得再漂亮，仍然是一張帶著合規風險的卡片。本篇按這三層拆開，最後給字高、條碼等級與打樣驗收的清單。",
        "en": "When a brand asks what to print on the hang tag, there are really three questions underneath: what the shopper looks for on the rail, what the law requires to travel with the product, and what a retailer or marketplace needs to scan. Of the nine fields that come up most often, six belong on the tag and three belong on a durable label. Put them in the wrong place and a beautifully printed tag is still a card with a compliance risk attached. This guide separates the three layers, then gives the type sizes, barcode grades and proof checks.",
        "fr": "Quand une marque demande ce qu'il faut imprimer sur l'étiquette pendante, il y a en réalité trois questions : ce que le client cherche sur le présentoir, ce que la loi exige de joindre au produit, et ce qu'un distributeur ou une place de marché doit scanner. Sur les neuf champs les plus fréquents, six ont leur place sur l'étiquette et trois sur une étiquette durable. Mal placés, une étiquette parfaitement imprimée reste une carte accompagnée d'un risque de conformité. Cet article sépare ces trois niveaux, puis donne les hauteurs de caractères, la classe de code-barres et les contrôles avant production.",
        "es": "Cuando una marca pregunta qué imprimir en la etiqueta colgante, en realidad hay tres preguntas: qué busca el cliente en el expositor, qué exige la ley que acompañe al producto y qué necesita escanear un minorista o un marketplace. De los nueve campos más habituales, seis van en la etiqueta y tres en una etiqueta duradera. Mal colocados, una etiqueta impecable sigue siendo una tarjeta con un riesgo de conformidad encima. Esta guía separa los tres niveles y después da cuerpos de letra, clase de código de barras y controles previos a producción.",
        "ja": "ブランドから「下げ札に何を刷ればいいか」と聞かれたとき、実際には 3 つの問いが重なっています。店頭でお客様が探す情報、法令が製品に添えることを求める情報、小売やモールがスキャンする情報です。よく挙がる 9 項目のうち、下げ札に載せるべきは 6 項目、残り 3 項目は耐久性のある縫い付けラベルが正しい置き場所です。置き場所を誤れば、どれだけ美しく刷ってもコンプライアンス上のリスクを抱えた紙片になります。本稿はこの 3 層を分け、文字高・バーコード等級・量産前の確認項目まで示します。",
        "ko": "브랜드가 행택에 무엇을 인쇄할지 물으면 실제로는 세 가지 질문이 겹쳐 있습니다. 매장에서 고객이 찾는 정보, 법규가 제품에 붙이도록 요구하는 정보, 유통사와 마켓플레이스가 스캔하는 정보입니다. 자주 거론되는 9개 항목 중 6개는 행택에, 나머지 3개는 봉제된 내구성 라벨이 정답입니다. 위치를 잘못 잡으면 아무리 잘 인쇄해도 컴플라이언스 리스크를 안은 종이 조각이 됩니다. 이 글은 세 층을 나눠 정리하고 글자 높이, 바코드 등급, 양산 전 점검 항목까지 제시합니다.",
    }),

    ("h2", {
        "zh": "一、買家與店員最先看的四個欄位",
        "en": "1. Four Fields the Shopper and the Sales Assistant Look For First",
        "fr": "1. Quatre champs que le client et le vendeur cherchent en premier",
        "es": "1. Cuatro campos que el cliente y el vendedor buscan primero",
        "ja": "1. お客様と販売員が最初に見る 4 項目",
        "ko": "1. 고객과 판매원이 가장 먼저 찾는 4개 항목",
    }),

    ("p", {
        "zh": "零售現場的第一個動作是找尺碼，第二個是確認款號與顏色。這四項沒有法律強制，卻決定吊牌好不好用：品牌與系列名放在主視覺面，款號與色號放在條碼面並與條碼文字對齊，尺碼用全牌最大字級。",
        "en": "On the shop floor the first move is to find the size, the second is to confirm the style and the colour. None of these four is legally mandated, but together they decide whether the tag works: brand and collection on the hero side, style and colour code on the barcode side aligned with the barcode text, size at the largest type size on the tag.",
        "fr": "En boutique, le premier geste est de chercher la taille, le second de vérifier la référence et la couleur. Aucun de ces quatre champs n'est imposé par la loi, mais ensemble ils décident de l'utilité de l'étiquette : marque et collection sur la face principale, référence et code couleur sur la face du code-barres alignés avec le texte imprimé, taille en plus gros caractères.",
        "es": "En tienda, el primer gesto es buscar la talla; el segundo, confirmar referencia y color. Ninguno de los cuatro campos es obligatorio por ley, pero juntos deciden si la etiqueta sirve: marca y colección en la cara principal, referencia y código de color en la cara del código de barras alineados con su texto, y la talla en el mayor cuerpo de letra.",
        "ja": "店頭での最初の動作はサイズ探し、次に品番と色の確認です。この 4 項目は法令で必須ではありませんが、下げ札が使えるかどうかを決めます。ブランド名とシーズン名はメイン面、品番と色番はバーコード面でバーコード数字と揃え、サイズは札の中で最大の文字高にします。",
        "ko": "매장에서 첫 동작은 사이즈 찾기, 두 번째는 품번과 색상 확인입니다. 이 네 항목은 법적 필수가 아니지만 행택의 쓸모를 결정합니다. 브랜드와 시즌명은 메인 면, 품번과 색상 코드는 바코드 면에서 바코드 숫자와 정렬하고, 사이즈는 행택에서 가장 큰 글자 높이로 배치합니다.",
    }),

    ("table", (
        [
            {"zh": "欄位", "en": "Field", "fr": "Champ", "es": "Campo", "ja": "項目", "ko": "항목"},
            {"zh": "放哪一面", "en": "Where it goes", "fr": "Emplacement", "es": "Dónde va", "ja": "配置する面", "ko": "위치"},
            {"zh": "實務要點", "en": "What to watch", "fr": "Point de vigilance", "es": "Qué vigilar", "ja": "実務の要点", "ko": "실무 포인트"},
        ],
        [
            [
                {"zh": "品牌與系列名", "en": "Brand and collection", "fr": "Marque et collection", "es": "Marca y colección", "ja": "ブランド名・シーズン名", "ko": "브랜드·시즌명"},
                {"zh": "正面主視覺", "en": "Hero side", "fr": "Face principale", "es": "Cara principal", "ja": "メイン面", "ko": "메인 면"},
                {"zh": "與 LOGO 同組，字高 5–8 mm", "en": "Grouped with the logo, 5–8 mm type", "fr": "Regroupés avec le logo, 5–8 mm", "es": "Junto al logo, cuerpo de 5–8 mm", "ja": "ロゴと同組、文字高 5〜8 mm", "ko": "로고와 함께, 5~8 mm"},
            ],
            [
                {"zh": "款號與色號", "en": "Style and colour code", "fr": "Référence et code couleur", "es": "Referencia y código de color", "ja": "品番・色番", "ko": "품번·색상 코드"},
                {"zh": "背面或條碼上方", "en": "Back, or above the barcode", "fr": "Dos ou au-dessus du code-barres", "es": "Dorso o sobre el código de barras", "ja": "裏面またはバーコード上", "ko": "뒷면 또는 바코드 위"},
                {"zh": "與條碼文字對齊，掃描時可交叉核對", "en": "Aligned with the barcode text so both can be cross-checked", "fr": "Alignés avec le texte du code-barres pour recoupement", "es": "Alineados con el texto del código para poder cotejar", "ja": "数字と揃え、照合できるように", "ko": "숫자와 정렬해 대조 가능하게"},
            ],
            [
                {"zh": "尺碼", "en": "Size", "fr": "Taille", "es": "Talla", "ja": "サイズ", "ko": "사이즈"},
                {"zh": "正面或背面大字", "en": "Large type, front or back", "fr": "Gros caractères, recto ou verso", "es": "Cuerpo grande, anverso o dorso", "ja": "表裏いずれかの大きな文字", "ko": "앞면 또는 뒷면 큰 글자"},
                {"zh": "4–6 mm，店員第一眼要找的資訊", "en": "4–6 mm; the first thing staff look for", "fr": "4–6 mm ; ce que le vendeur cherche en premier", "es": "4–6 mm; lo primero que busca el personal", "ja": "4〜6 mm。販売員が最初に探す情報", "ko": "4~6 mm, 판매원이 가장 먼저 찾는 정보"},
            ],
            [
                {"zh": "零售價（可選）", "en": "Retail price (optional)", "fr": "Prix de vente (facultatif)", "es": "Precio de venta (opcional)", "ja": "売価（任意）", "ko": "판매가(선택)"},
                {"zh": "建議改放價格標", "en": "Better on a price ticket", "fr": "Mieux vaut une étiquette de prix", "es": "Mejor en un ticket de precio", "ja": "価格ラベルを推奨", "ko": "가격표 사용 권장"},
                {"zh": "印在吊牌上等於把每次調價綁在一張紙上", "en": "Printing it ties every markdown to one sheet of paper", "fr": "L'imprimer lie chaque démarque à un seul support", "es": "Imprimirlo ata cada rebaja a un solo papel", "ja": "値下げのたびに紙を刷り直すことになる", "ko": "가격 인하 때마다 종이를 다시 찍어야 함"},
            ],
        ],
    )),

    ("h2", {
        "zh": "二、法規看的四個欄位：為什麼不能只印在吊牌上",
        "en": "2. Four Fields the Law Cares About, and Why the Tag Cannot Carry Them Alone",
        "fr": "2. Quatre champs encadrés par la loi, et pourquoi l'étiquette ne peut pas les porter seule",
        "es": "2. Cuatro campos que la ley vigila, y por qué la etiqueta no puede llevarlos sola",
        "ja": "2. 法令が見る 4 項目：下げ札だけで済ませられない理由",
        "ko": "2. 법규가 보는 4개 항목: 행택만으로는 안 되는 이유",
    }),

    ("p", {
        "zh": "纖維成分、洗護方式、原產地與歐盟責任主體，是四個真正有法源依據的欄位。歐盟 (EU) No 1007/2011 要求紡織品的纖維成分標示附在產品上，並在整個流通環節保持可見；美國 FTC 的 16 CFR 423 要求洗護說明永久附著於服裝；日本《家庭用品品質表示法》把組成、洗濯表示與表示者列為強制項目；韓國則以品質表示與原產地標示為核心。這些要求的共同點是耐久：吊牌可以撕掉，所以不能作為唯一載體。",
        "en": "Fibre composition, care instructions, country of origin and, in the EU, the responsible person are the four fields with a real legal basis. Regulation (EU) No 1007/2011 requires textile fibre composition to be indicated on the product and to remain visible through the whole chain. In the United States, the FTC rule at 16 CFR 423 requires care instructions to be permanently attached to the garment. Japan's Household Goods Quality Labelling Act makes composition, care symbols and the labeller mandatory items. Korea centres on quality labelling and country of origin. What they share is durability: a hang tag can be removed, so it cannot be the only carrier.",
        "fr": "Composition des fibres, entretien, pays d'origine et, dans l'UE, responsable établi : ce sont les quatre champs à base légale réelle. Le règlement (UE) n° 1007/2011 impose d'indiquer la composition des fibres sur le produit, de manière visible tout au long de la chaîne. Aux États-Unis, la règle 16 CFR 423 de la FTC impose un entretien attaché de façon permanente au vêtement. Au Japon, la loi sur l'étiquetage de qualité des articles ménagers rend obligatoires la composition, les symboles de lavage et le nom du responsable du marquage. La Corée s'appuie sur l'étiquetage de qualité et l'origine. Point commun : la durabilité, car une étiquette pendante s'enlève et ne peut donc pas être le seul support.",
        "es": "Composición de fibras, instrucciones de cuidado, país de origen y, en la UE, la persona responsable establecida son los cuatro campos con base legal real. El Reglamento (UE) n.º 1007/2011 exige indicar la composición de las fibras en el producto y mantenerla visible en toda la cadena. En Estados Unidos, la regla 16 CFR 423 de la FTC exige las instrucciones de cuidado unidas de forma permanente a la prenda. En Japón, la Ley de Etiquetado de Calidad de Bienes de Consumo hace obligatorios la composición, los símbolos de lavado y el responsable. Corea se apoya en el etiquetado de calidad y el origen. El punto común es la durabilidad: una etiqueta colgante se quita, así que no puede ser el único soporte.",
        "ja": "繊維組成・取扱表示・原産国、そして EU では責任者。この 4 項目が実際に法的根拠を持つ情報です。EU の規則 (EU) No 1007/2011 は繊維組成を製品に表示し、流通過程で見える状態に保つことを求めます。米国では FTC の 16 CFR 423 が取扱表示を衣類に恒久的に添付するよう定めています。日本では家庭用品品質表示法が組成・洗濯表示・表示者を義務項目とし、韓国は品質表示と原産地を中心に据えています。共通するのは耐久性です。下げ札は取り外せるため、唯一の媒体にはできません。",
        "ko": "섬유 혼용률, 취급 표시, 원산지, 그리고 EU에서는 책임자. 이 네 항목이 실제 법적 근거를 가진 정보입니다. 규정 (EU) No 1007/2011은 섬유 혼용률을 제품에 표시하고 유통 전 과정에서 보이도록 요구합니다. 미국은 FTC의 16 CFR 423이 취급 표시를 의류에 영구 부착하도록 정합니다. 일본은 가정용품 품질 표시법이 조성·세탁 표시·표시자를 의무 항목으로 두고, 한국은 품질경영 및 공산품 안전관리법에 따른 품질 표시와 원산지 표시, 표시광고법상의 광고 규정을 함께 봐야 합니다. 공통점은 내구성입니다. 행택은 떼어낼 수 있으므로 유일한 매체가 될 수 없습니다.",
    }),

    ("p", {
        "zh": "實務做法是把吊牌當「重複一次」的位置，而不是唯一位置：吊牌印一句「詳見洗水標」，完整信息放進耐久標籤。這樣不增加成本，也把版面留給品牌故事。",
        "en": "The practical answer is to treat the tag as a second copy rather than the only copy: one line saying see the care label, with the complete information on the durable label. It costs nothing extra and leaves the layout free for the brand story.",
        "fr": "La réponse pratique : considérer l'étiquette pendante comme une seconde copie et non comme l'unique support. Une ligne du type « voir étiquette d'entretien », et l'information complète sur l'étiquette durable. Cela ne coûte rien et libère la surface pour l'histoire de marque.",
        "es": "La respuesta práctica es tratar la etiqueta colgante como segunda copia y no como único soporte: una línea que remita a la etiqueta de cuidado y la información completa en la etiqueta duradera. No cuesta más y deja la superficie libre para la historia de marca.",
        "ja": "実務的には、下げ札を「二重化」の位置づけにします。「洗濯表示をご覧ください」の一行を置き、完全な情報は耐久ラベルに入れます。追加コストはなく、面はブランドストーリーに使えます。",
        "ko": "실무 해법은 행택을 두 번째 사본으로 두는 것입니다. 세탁 표시를 보라는 한 줄을 넣고 완전한 정보는 내구성 라벨에 담습니다. 추가 비용이 없고 면은 브랜드 스토리에 쓸 수 있습니다.",
    }),

    ("table", (
        [
            {"zh": "信息", "en": "Information", "fr": "Information", "es": "Información", "ja": "情報", "ko": "정보"},
            {"zh": "吊牌可否承載", "en": "Allowed on the tag", "fr": "Admise sur l'étiquette", "es": "Admisible en la etiqueta", "ja": "下げ札への記載", "ko": "행택 기재"},
            {"zh": "法規要求的位置", "en": "Required location", "fr": "Emplacement exigé", "es": "Ubicación exigida", "ja": "法令上の位置", "ko": "법정 위치"},
        ],
        [
            [
                {"zh": "纖維成分", "en": "Fibre composition", "fr": "Composition des fibres", "es": "Composición de fibras", "ja": "繊維組成", "ko": "섬유 혼용률"},
                {"zh": "只能重複", "en": "Duplicate only", "fr": "En doublon seulement", "es": "Solo como duplicado", "ja": "重複記載のみ", "ko": "중복 기재만"},
                {"zh": "耐久標籤（(EU) 1007/2011、日本家庭用品品質表示法）", "en": "Durable label (Regulation (EU) No 1007/2011; Japan's Household Goods Quality Labelling Act)", "fr": "Étiquette durable (règlement (UE) n° 1007/2011 ; loi japonaise sur l'étiquetage de qualité)", "es": "Etiqueta duradera (Reglamento (UE) n.º 1007/2011; ley japonesa de etiquetado de calidad)", "ja": "耐久ラベル（規則 (EU) No 1007/2011、家庭用品品質表示法）", "ko": "내구성 라벨(규정 (EU) No 1007/2011, 일본 가정용품 품질 표시법)"},
            ],
            [
                {"zh": "洗護方式", "en": "Care instructions", "fr": "Entretien", "es": "Cuidado", "ja": "取扱表示", "ko": "취급 표시"},
                {"zh": "只能重複", "en": "Duplicate only", "fr": "En doublon seulement", "es": "Solo como duplicado", "ja": "重複記載のみ", "ko": "중복 기재만"},
                {"zh": "耐久標籤（16 CFR 423、EN ISO 3758 符號）", "en": "Durable label (16 CFR 423; EN ISO 3758 symbols)", "fr": "Étiquette durable (16 CFR 423 ; symboles EN ISO 3758)", "es": "Etiqueta duradera (16 CFR 423; símbolos EN ISO 3758)", "ja": "耐久ラベル（16 CFR 423、EN ISO 3758 の記号）", "ko": "내구성 라벨(16 CFR 423, EN ISO 3758 기호)"},
            ],
            [
                {"zh": "原產地", "en": "Country of origin", "fr": "Pays d'origine", "es": "País de origen", "ja": "原産国", "ko": "원산지"},
                {"zh": "可以", "en": "Yes", "fr": "Oui", "es": "Sí", "ja": "可", "ko": "가능"},
                {"zh": "產品或包裝，按各市場規定", "en": "Product or packaging, per market rules", "fr": "Produit ou emballage, selon le marché", "es": "Producto o envase, según el mercado", "ja": "製品または包装（市場ごとの表示義務）", "ko": "제품 또는 포장(시장별 표시 의무)"},
            ],
            [
                {"zh": "歐盟責任主體", "en": "EU responsible person", "fr": "Responsable dans l'UE", "es": "Responsable en la UE", "ja": "EU 責任者", "ko": "EU 책임자"},
                {"zh": "可以", "en": "Yes", "fr": "Oui", "es": "Sí", "ja": "可", "ko": "가능"},
                {"zh": "產品或包裝（GPSR (EU) 2023/988）", "en": "Product or packaging (GPSR (EU) 2023/988)", "fr": "Produit ou emballage (GPSR (UE) 2023/988)", "es": "Producto o envase (GPSR (UE) 2023/988)", "ja": "製品または包装（GPSR (EU) 2023/988）", "ko": "제품 또는 포장(GPSR (EU) 2023/988)"},
            ],
        ],
    )),

    ("ul", [
        {
            "zh": "只印在吊牌上：吊牌一撕信息就消失，歐洲海關與平台抽檢會直接判不合格。",
            "en": "Printing it only on the tag: the moment the tag comes off the information is gone, and EU customs or a marketplace spot check will treat it as non-compliant.",
            "fr": "Ne l'imprimer que sur l'étiquette pendante : une fois celle-ci retirée, l'information disparaît et un contrôle douanier ou de place de marché conclut à la non-conformité.",
            "es": "Imprimirlo solo en la etiqueta colgante: al quitarla desaparece la información y una inspección de aduana o de marketplace lo considera no conforme.",
            "ja": "下げ札だけに記載する：外した時点で情報が消え、EU 税関やモールの抜き取り検査では不適合になります。",
            "ko": "행택에만 인쇄하기: 행택을 떼는 순간 정보가 사라지고 EU 세관이나 마켓플레이스 점검에서 부적합 판정을 받습니다.",
        },
        {
            "zh": "用可撕的副牌承載法定信息：副牌同樣會被撕掉，不具耐久性。",
            "en": "Using a tear-off secondary card for mandatory information: a tear-off card comes off just as easily and is not durable.",
            "fr": "Confier les mentions obligatoires à une contre-étiquette détachable : elle s'arrache aussi facilement et n'est pas durable.",
            "es": "Usar una contraetiqueta desprendible para la información legal: también se arranca y no es duradera.",
            "ja": "切り取り式の副札に法定情報を載せる：副札も同様に切られ、耐久性を満たしません。",
            "ko": "뜯어내는 보조 태그에 법정 정보를 싣기: 보조 태그도 뜯기므로 내구성을 충족하지 못합니다.",
        },
        {
            "zh": "多語只印英文：語言要求按銷售地判定，英文不是萬能通行證。",
            "en": "Printing English only: language requirements follow the place of sale, and English is not a universal pass.",
            "fr": "N'imprimer qu'en anglais : les exigences linguistiques dépendent du lieu de vente, l'anglais n'est pas un laissez-passer.",
            "es": "Imprimir solo en inglés: los requisitos de idioma dependen del lugar de venta y el inglés no es un salvoconducto.",
            "ja": "英語だけを刷る：言語要件は販売地の規定に従い、英語が万能ではありません。",
            "ko": "영어만 인쇄하기: 언어 요건은 판매 지역 규정을 따르며 영어가 만능 통행증은 아닙니다.",
        },
    ]),

    ("h2", {
        "zh": "三、條碼與價格：最常引發罰款與退貨的兩個欄位",
        "en": "3. Barcode and Price: the Two Fields That Trigger Chargebacks",
        "fr": "3. Code-barres et prix : les deux champs qui déclenchent des pénalités",
        "es": "3. Código de barras y precio: los dos campos que generan penalizaciones",
        "ja": "3. バーコードと価格：違約金・返品の原因になる 2 項目",
        "ko": "3. 바코드와 가격: 페널티와 반품을 부르는 두 항목",
    }),

    ("p", {
        "zh": "條碼是掃描入口，不是裝飾。GTIN 必須與品牌在 GS1 登記的一致，印後要做 ANSI 等級驗證，零售商一般要求 C 級（2.5）以上。碼高不足、反差太低、覆膜反光，任何一項都會讓收貨掃描變成「無法讀取」，這類問題在零售端幾乎必然產生罰款。",
        "en": "The barcode is a scanning interface, not decoration. The GTIN must match what the brand registered with GS1, and the print should be graded afterwards: retailers typically demand ANSI grade C, or 2.5, or better. Insufficient bar height, low contrast or a reflective laminate will each turn goods-in scanning into unreadable, and that category of defect almost always ends in a chargeback.",
        "fr": "Le code-barres est une interface de scan, pas un ornement. Le GTIN doit correspondre à l'enregistrement GS1 de la marque et l'impression doit être notée : les distributeurs exigent en général une classe ANSI C (2,5) ou mieux. Hauteur de barres insuffisante, contraste faible ou pelliculage réfléchissant transforment le scan à réception en « illisible », et ce type de défaut finit presque toujours en pénalité.",
        "es": "El código de barras es una interfaz de escaneo, no un adorno. El GTIN debe coincidir con el registrado por la marca en GS1 y la impresión debe graduarse: los minoristas suelen exigir clase ANSI C (2,5) o mejor. Altura de barras insuficiente, poco contraste o laminado brillante convierten la recepción en ilegible, y ese defecto casi siempre acaba en penalización.",
        "ja": "バーコードはスキャンのインターフェースであり、装飾ではありません。GTIN はブランドが GS1 に登録した値と一致させ、印刷後に ANSI 等級で検証します。小売は通常 C 級（2.5）以上を要求します。バーの高さ不足、コントラスト不足、ラミネートの反射はいずれも入荷検品で「読み取り不可」になり、この種の不具合はほぼ確実に違約金につながります。",
        "ko": "바코드는 스캔 인터페이스이지 장식이 아닙니다. GTIN은 브랜드가 GS1에 등록한 값과 일치해야 하고 인쇄 후 ANSI 등급 검증을 합니다. 유통사는 보통 C등급(2.5) 이상을 요구합니다. 바 높이 부족, 낮은 대비, 라미네이트 반사는 모두 입고 검수에서 판독 불가가 되고 이런 결함은 거의 항상 페널티로 이어집니다.",
    }),

    ("p", {
        "zh": "價格相反：把零售價直接印在吊牌上，等於把每一次調價、每一個市場的價差都綁在一張紙上。跨境與多平台銷售的常規做法是吊牌不印價，價格放在可撕的價格標或系統裡，改價時只換價格標。",
        "en": "Price works the other way. Printing the retail price on the tag ties every markdown, and every market's price difference, to one sheet of paper. In cross-border and multi-channel selling, the usual approach is to keep the price off the tag and put it on a tear-off price ticket or in the system, so a price change costs one small label.",
        "fr": "Le prix fonctionne à l'inverse. Imprimer le prix de vente sur l'étiquette pendante lie chaque démarque, et chaque écart de prix entre marchés, à un seul support. En vente transfrontalière et multicanal, la pratique courante consiste à ne pas imprimer le prix sur l'étiquette et à le placer sur une étiquette de prix détachable, ou dans le système.",
        "es": "El precio funciona al revés. Imprimirlo en la etiqueta colgante ata cada rebaja y cada diferencia de precio entre mercados a un solo papel. En venta transfronteriza y multicanal lo habitual es no imprimir precio y llevarlo a un ticket desprendible o al sistema.",
        "ja": "価格は逆です。売価を下げ札に直接刷ると、値下げのたびに、市場ごとの価格差のたびに紙を刷り直すことになります。越境・複数チャネル販売では、下げ札に価格を載せず、切り取り式の価格ラベルかシステム側に持たせるのが標準です。",
        "ko": "가격은 반대입니다. 판매가를 행택에 인쇄하면 모든 가격 인하와 시장별 가격차를 종이 한 장에 묶어 두는 셈입니다. 해외·멀티채널 판매에서는 행택에 가격을 넣지 않고 뜯어내는 가격표나 시스템에 두는 것이 일반적입니다.",
    }),

    ("callout", {
        "zh": "一句可以記住的規則：條碼與款號印在吊牌上，價格印在價格標上，成分與洗護印在洗水標上。",
        "en": "One rule worth remembering: barcode and style code on the tag, price on the price ticket, composition and care on the care label.",
        "fr": "Une règle à retenir : code-barres et référence sur l'étiquette pendante, prix sur l'étiquette de prix, composition et entretien sur l'étiquette d'entretien.",
        "es": "Una regla para recordar: código de barras y referencia en la etiqueta colgante, precio en el ticket, composición y cuidado en la etiqueta de cuidado.",
        "ja": "覚えておきたい原則は 1 つ。バーコードと品番は下げ札、価格は価格ラベル、組成と取扱表示は洗濯表示ラベルへ。",
        "ko": "기억할 원칙 하나. 바코드와 품번은 행택, 가격은 가격표, 혼용률과 취급 표시는 세탁 라벨에.",
    }),

    ("h2", {
        "zh": "四、版面層級與字高：可讀性可以量化",
        "en": "4. Layout Hierarchy and Type Size: Legibility Is Measurable",
        "fr": "4. Hiérarchie et hauteur de caractères : la lisibilité se mesure",
        "es": "4. Jerarquía y cuerpo de letra: la legibilidad se mide",
        "ja": "4. レイアウトの階層と文字高：可読性は数値で測れる",
        "ko": "4. 레이아웃 위계와 글자 높이: 가독성은 측정 가능하다",
    }),

    ("p", {
        "zh": "吊牌面積小，信息一多只能靠字高與留白分層。實務基準：品牌名 5–8 mm 字高、尺碼 4–6 mm、款號與條碼文字 1.5–2 mm，其餘說明不低於 1.2 mm。低於 1 mm 的字在 300 dpi 下仍印得出來，但 30 cm 距離已經讀不清。",
        "en": "Tag area is small, so hierarchy has to come from type size and white space. Workable baselines: brand name 5–8 mm, size 4–6 mm, style code and barcode text 1.5–2 mm, other copy no smaller than 1.2 mm. Anything under 1 mm still prints at 300 dpi, but nobody reads it at 30 cm.",
        "fr": "La surface est réduite : la hiérarchie ne peut venir que de la hauteur de caractères et des blancs. Repères praticables : marque 5–8 mm, taille 4–6 mm, référence et texte du code-barres 1,5–2 mm, autres mentions pas moins de 1,2 mm. En dessous de 1 mm, l'impression à 300 dpi reste possible, mais la lecture à 30 cm ne l'est plus.",
        "es": "La superficie es pequeña, así que la jerarquía solo puede venir del cuerpo de letra y de los espacios en blanco. Referencias prácticas: marca 5–8 mm, talla 4–6 mm, referencia y texto del código 1,5–2 mm, demás textos no menos de 1,2 mm. Por debajo de 1 mm se sigue imprimiendo a 300 dpi, pero ya no se lee a 30 cm.",
        "ja": "下げ札は面積が小さいため、階層は文字高と余白でしか作れません。実務の目安は、ブランド名 5〜8 mm、サイズ 4〜6 mm、品番とバーコード数字 1.5〜2 mm、その他の説明は 1.2 mm 以上です。1 mm 未満でも 300 dpi なら印刷はできますが、30 cm の距離では読めません。",
        "ko": "행택은 면적이 작아 위계를 글자 높이와 여백으로만 만들 수 있습니다. 실무 기준은 브랜드명 5~8 mm, 사이즈 4~6 mm, 품번과 바코드 숫자 1.5~2 mm, 기타 설명 1.2 mm 이상입니다. 1 mm 미만도 300 dpi에서는 인쇄되지만 30 cm 거리에서는 읽히지 않습니다.",
    }),

    ("p", {
        "zh": "二維碼有另一套限制：模組尺寸小於 0.3 mm 或整體小於 12 mm 時，中低階手機在店內燈光下的掃描成功率明顯下降；放在背面時要留至少 2 mm 的靜區，否則邊緣對比會被吃掉。",
        "en": "QR codes carry their own limits. Below roughly 0.3 mm per module, or below 12 mm overall, scan rates on mid-range phones under shop lighting drop sharply. On the back panel, leave at least a 2 mm quiet zone or the contrast at the edges gets eaten.",
        "fr": "Le QR code a ses propres limites. En dessous d'environ 0,3 mm par module, ou de 12 mm au total, le taux de lecture sur un téléphone de milieu de gamme sous éclairage de magasin chute nettement. Au verso, laissez une zone de silence d'au moins 2 mm, sinon le contraste des bords disparaît.",
        "es": "El código QR tiene sus propios límites. Por debajo de unos 0,3 mm por módulo, o de 12 mm en total, la tasa de lectura en móviles de gama media con luz de tienda cae en picado. En el dorso deja al menos 2 mm de zona de silencio o el contraste de los bordes se pierde.",
        "ja": "二次元コードには別の制約があります。モジュール 0.3 mm 未満、または全体 12 mm 未満になると、店頭照明下でのミドルレンジ端末の読み取り率が大きく落ちます。裏面に置く場合は 2 mm 以上の余白（クワイエットゾーン）を確保しないと、端のコントラストが潰れます。",
        "ko": "2차원 코드는 제약이 다릅니다. 모듈 0.3 mm 미만 또는 전체 12 mm 미만이면 매장 조명 아래 중급 단말의 판독률이 크게 떨어집니다. 뒷면에 배치할 때는 최소 2 mm의 여백(콰이어트 존)을 두지 않으면 가장자리 대비가 사라집니다.",
    }),

    ("h2", {
        "zh": "五、語言組合與版本管控",
        "en": "5. Language Sets and Version Control",
        "fr": "5. Combinaisons de langues et gestion des versions",
        "es": "5. Combinaciones de idiomas y control de versiones",
        "ja": "5. 言語の組み合わせと版管理",
        "ko": "5. 언어 조합과 버전 관리",
    }),

    ("p", {
        "zh": "語言不是越多越好。歐盟有 24 種官方語言，一張吊牌塞不進 24 種；常見做法是「英語加當地語言」的雙語組合，必要時在括號裡補第三語言。真正需要管控的是版本：同一款產品賣到三個市場，就是三個吊牌版本，每個都要有可追溯的版本號。",
        "en": "More languages is not automatically better. The EU has 24 official languages and a hang tag cannot hold 24; the usual answer is a two-language set of English plus the local language, with a third in brackets where it matters. What actually needs control is versioning: one product sold into three markets is three tag versions, and each needs a traceable version number.",
        "fr": "Plus de langues n'est pas automatiquement mieux. L'Union compte 24 langues officielles et une étiquette n'en tient pas 24 ; la solution habituelle est un jeu bilingue anglais plus langue locale, avec une troisième entre parenthèses si nécessaire. Ce qu'il faut vraiment piloter, c'est la version : un produit vendu sur trois marchés, c'est trois versions d'étiquette, chacune avec un numéro traçable.",
        "es": "Más idiomas no es automáticamente mejor. La UE tiene 24 lenguas oficiales y una etiqueta no admite 24; lo habitual es un juego bilingüe de inglés más idioma local, con un tercero entre paréntesis si hace falta. Lo que hay que controlar es la versión: un producto vendido en tres mercados son tres versiones de etiqueta, cada una con número trazable.",
        "ja": "言語は多ければ良いわけではありません。EU の公用語は 24 言語あり、下げ札に 24 言語は入りません。通常は英語＋現地語の 2 言語構成とし、必要なら括弧書きで第 3 言語を足します。管理すべきは版です。1 製品を 3 市場で売るなら下げ札も 3 版になり、それぞれに追跡できる版番号が必要です。",
        "ko": "언어는 많다고 좋은 것이 아닙니다. EU 공용어는 24개이고 행택에 24개를 담을 수 없습니다. 보통 영어+현지어 2개 언어 구성으로 하고 필요하면 괄호로 세 번째 언어를 더합니다. 실제로 관리할 것은 버전입니다. 한 제품을 세 시장에 팔면 행택도 세 버전이고 각각 추적 가능한 버전 번호가 필요합니다.",
    }),

    ("ul", [
        {
            "zh": "版本號印在背面或條碼下方，與採購單上的號碼一致。",
            "en": "Print the version number on the back or under the barcode, matching the number on the purchase order.",
            "fr": "Imprimer le numéro de version au dos ou sous le code-barres, identique à celui du bon de commande.",
            "es": "Imprime el número de versión en el dorso o bajo el código de barras, igual al del pedido.",
            "ja": "版番号は裏面かバーコードの下に印刷し、発注書の番号と一致させます。",
            "ko": "버전 번호는 뒷면이나 바코드 아래에 인쇄하고 발주서 번호와 일치시킵니다.",
        },
        {
            "zh": "採購單寫明版本、語言組合與對應市場，不要只寫「吊牌一批」。",
            "en": "The PO should name the version, the language set and the target market, not just one batch of hang tags.",
            "fr": "Le bon de commande précise la version, la combinaison de langues et le marché visé, pas seulement « un lot d'étiquettes ».",
            "es": "El pedido debe indicar versión, combinación de idiomas y mercado destino, no solo un lote de etiquetas.",
            "ja": "発注書には版・言語構成・対象市場を明記します。「下げ札一式」だけでは足りません。",
            "ko": "발주서에는 버전, 언어 조합, 대상 시장을 명기합니다. 행택 일괄로는 부족합니다.",
        },
        {
            "zh": "改版時舊版庫存要隔離掛牌，避免兩版混裝出貨。",
            "en": "When a version changes, segregate the old stock with a label so two versions never ship in one carton.",
            "fr": "En cas de changement de version, isoler le stock ancien avec un repère pour que deux versions ne partent jamais dans un même carton.",
            "es": "Al cambiar de versión, separa el stock antiguo con una etiqueta para que nunca salgan dos versiones en la misma caja.",
            "ja": "版が変わったら旧版在庫を区分けし、1 箱に 2 版が混ざらないようにします。",
            "ko": "버전이 바뀌면 이전 재고를 표시해 분리하고 한 상자에 두 버전이 섞이지 않게 합니다.",
        },
        {
            "zh": "不要用同一塊印版同時生產不同市場的版本，混版是「打樣通過、量產出錯」最常見的原因。",
            "en": "Do not run different market versions from one plate; mixed plates are the most common reason a proof passes and production fails.",
            "fr": "Ne pas produire plusieurs versions de marché avec une seule forme imprimante : c'est la première cause de validation en épreuve et d'échec en production.",
            "es": "No produzcas versiones de distintos mercados con la misma plancha: es la causa más común de que la prueba se apruebe y la producción falle.",
            "ja": "同一刷版で複数市場の版を同時に生産しないこと。版の混在は、校正は通ったのに量産で崩れる最大の原因です。",
            "ko": "하나의 판으로 여러 시장 버전을 동시에 생산하지 마십시오. 판 혼용은 교정은 통과하고 양산에서 실패하는 가장 흔한 원인입니다.",
        },
    ]),

    ("h2", {
        "zh": "六、打樣驗收：五項可以當場查的項目",
        "en": "6. Proof Checks: Five Items You Can Verify on the Spot",
        "fr": "6. Contrôles avant production : cinq points vérifiables sur place",
        "es": "6. Controles previos: cinco puntos verificables en el momento",
        "ja": "6. 量産前の確認：その場で判定できる 5 項目",
        "ko": "6. 양산 전 검사: 현장에서 확인 가능한 다섯 항목",
    }),

    ("ul", [
        {
            "zh": "文字校對：逐字對照定稿，含標點與外語重音符號，這是最容易漏的一項。",
            "en": "Copy proof: check against the approved text character by character, punctuation and accents included. This is the one that slips.",
            "fr": "Relecture : comparer caractère par caractère au texte approuvé, ponctuation et accents compris. C'est le point qui échappe le plus souvent.",
            "es": "Corrección de textos: compara carácter por carácter con el texto aprobado, incluida puntuación y acentos. Es lo que más se escapa.",
            "ja": "文字校正：承認原稿と 1 文字ずつ照合。句読点やアクセント記号まで確認します。最も漏れやすい項目です。",
            "ko": "문안 교정: 승인 원고와 글자 단위로 대조하고 문장부호와 악센트까지 확인합니다. 가장 자주 빠지는 항목입니다.",
        },
        {
            "zh": "條碼：實掃三次以上，並附 ANSI 等級報告，C 級以下不接受。",
            "en": "Barcode: scan it at least three times and ask for the ANSI grade report; reject anything below grade C.",
            "fr": "Code-barres : le scanner au moins trois fois et exiger le rapport de classe ANSI ; refuser en dessous de C.",
            "es": "Código de barras: escanéalo al menos tres veces y pide el informe de clase ANSI; rechaza por debajo de C.",
            "ja": "バーコード：実機で 3 回以上スキャンし、ANSI 等級のレポートを取ります。C 級未満は受入れ不可。",
            "ko": "바코드: 3회 이상 실물 스캔하고 ANSI 등급 리포트를 요구합니다. C등급 미만은 불합격입니다.",
        },
        {
            "zh": "色差：品牌色 ΔE ≤ 1.5、一般色 ΔE ≤ 2.0，深色滿版另做摩擦測試。",
            "en": "Colour: ΔE ≤ 1.5 for brand colours and ≤ 2.0 for the rest, with a rub test on heavy dark solids.",
            "fr": "Couleur : ΔE ≤ 1,5 pour les couleurs de marque et ≤ 2,0 sinon, avec un test de frottement sur les aplats foncés.",
            "es": "Color: ΔE ≤ 1,5 para colores de marca y ≤ 2,0 para el resto, con ensayo de frote en fondos oscuros.",
            "ja": "色差：ブランド色 ΔE ≤ 1.5、一般色 ΔE ≤ 2.0。濃色ベタは摩擦試験も行います。",
            "ko": "색차: 브랜드 색 ΔE ≤ 1.5, 일반 색 ΔE ≤ 2.0. 진한 전면 인쇄는 마찰 시험도 합니다.",
        },
        {
            "zh": "孔位：距邊至少 8 mm，孔徑與掛繩或膠針匹配，孔邊無毛邊。",
            "en": "Hole: at least 8 mm from the edge, diameter matched to the cord or fastener, no burr on the rim.",
            "fr": "Trou : à au moins 8 mm du bord, diamètre adapté au cordon ou à l'attache, sans bavure.",
            "es": "Ojal: a 8 mm del borde como mínimo, diámetro acorde al cordón o la grapa y sin rebabas.",
            "ja": "穴：端から 8 mm 以上、穴径は紐やピンに適合、バリがないこと。",
            "ko": "구멍: 가장자리에서 최소 8 mm, 지름은 끈이나 고정핀에 맞추고 버가 없어야 합니다.",
        },
        {
            "zh": "材質與克重：實測落在 300–400 g/m² 區間且 ±5% 以內，紙種與批核樣一致。",
            "en": "Material and GSM: measured within the 300–400 g/m² band and inside ±5%, on the paper grade that was approved.",
            "fr": "Matière et grammage : mesurés dans la plage 300–400 g/m² et à ±5 %, sur la qualité de papier approuvée.",
            "es": "Material y gramaje: medidos dentro de la banda 300–400 g/m² y en ±5 %, sobre el papel aprobado.",
            "ja": "材質と坪量：実測が 300〜400 g/m² の範囲かつ ±5 % 以内で、承認した紙質であること。",
            "ko": "재질과 평량: 실측이 300~400 g/m² 범위이고 ±5% 이내이며 승인한 지종이어야 합니다.",
        },
    ]),

    ("p", {
        "zh": "一張吊牌的信息量其實不大：九個欄位裡真正必須印上去的只有六個，另外三個的正確位置是耐久標籤。把位置放對、把字高與條碼等級寫進規格，吊牌就從一張設計稿變成一份可以驗收的輔料。",
        "en": "A hang tag does not carry much information. Of the nine fields, six genuinely need to be printed and three belong on a durable label. Get the placement right, put type sizes and barcode grades into the specification, and the tag stops being a design file and becomes a trims item you can inspect on arrival.",
        "fr": "Une étiquette pendante ne porte pas beaucoup d'informations. Sur les neuf champs, six doivent réellement être imprimés et trois relèvent de l'étiquette durable. Bien placer, puis inscrire hauteurs de caractères et classe de code-barres dans la spécification, transforme l'étiquette en accessoire contrôlable à réception.",
        "es": "Una etiqueta colgante no lleva mucha información. De los nueve campos, seis deben imprimirse realmente y tres pertenecen a la etiqueta duradera. Con la ubicación correcta y los cuerpos de letra y la clase de código en la especificación, la etiqueta deja de ser un archivo de diseño y pasa a ser un accesorio verificable.",
        "ja": "下げ札が載せる情報は多くありません。9 項目のうち実際に印刷が必要なのは 6 項目、残り 3 項目は耐久ラベルが正解です。置き場所を正し、文字高とバーコード等級を仕様に書き込めば、下げ札はデザインデータではなく受入検査できる副資材になります。",
        "ko": "행택에 담기는 정보는 많지 않습니다. 9개 항목 중 실제로 인쇄가 필요한 것은 6개, 나머지 3개는 내구성 라벨이 정답입니다. 위치를 바로잡고 글자 높이와 바코드 등급을 사양에 넣으면 행택은 디자인 파일이 아니라 입고 검사가 가능한 부자재가 됩니다.",
    }),

    ("related", [
        ("clothing-price-ticket-guide.html", {
            "zh": "價格標與吊牌：類型、條碼與起訂量",
            "en": "Price tickets vs hang tags: types, barcode and MOQ",
            "fr": "Étiquettes de prix et étiquettes pendantes : types, code-barres, quantités",
            "es": "Tickets de precio y etiquetas colgantes: tipos, código y pedido mínimo",
            "ja": "価格ラベルと下げ札：種類・バーコード・MOQ",
            "ko": "가격표와 행택: 종류·바코드·최소 주문량",
        }),
        ("hang-tag-multilingual-printing-guide.html", {
            "zh": "多語吊牌：語言組合、版面與版本管控",
            "en": "Multilingual hang tags: language sets, layout and version control",
            "fr": "Étiquettes multilingues : jeux de langues, mise en page, versions",
            "es": "Etiquetas multilingües: idiomas, maquetación y versiones",
            "ja": "多言語の下げ札：言語構成・レイアウト・版管理",
            "ko": "다국어 행택: 언어 구성·레이아웃·버전 관리",
        }),
        ("care-label-placement-guide.html", {
            "zh": "洗水標位置：縫在哪、怎麼縫才不被退貨",
            "en": "Care label placement: where to sew it and how",
            "fr": "Position de l'étiquette d'entretien : où et comment la coudre",
            "es": "Ubicación de la etiqueta de cuidado: dónde y cómo coserla",
            "ja": "洗濯表示ラベルの位置：どこに、どう縫うか",
            "ko": "세탁 라벨 위치: 어디에 어떻게 봉제할까",
        }),
        ("what-is-a-hang-tag.html", {
            "zh": "吊牌是什麼：結構、材料與採購入門",
            "en": "What is a hang tag: structure, materials and buying basics",
            "fr": "Qu'est-ce qu'une étiquette pendante : structure et matériaux",
            "es": "Qué es una etiqueta colgante: estructura y materiales",
            "ja": "下げ札とは：構造・材料・発注の基本",
            "ko": "행택이란: 구조·재료·발주 기초",
        }),
    ]),

    ("cta", (
        {
            "zh": "正在定吊牌版面，不確定九個欄位怎麼分到正反面與洗水標？把產品類別、目標市場與現有洗水標發給我們，我們出一版標注欄位、字高與條碼等級的版面建議。",
            "en": "Locking down a tag layout and unsure how the nine fields split between the two sides and the care label? Send the product category, target markets and your current care label, and we will return a layout marked with fields, type sizes and barcode grade.",
            "fr": "Vous arrêtez la maquette d'une étiquette sans savoir comment répartir les neuf champs entre recto, verso et étiquette d'entretien ? Envoyez la catégorie de produit, les marchés visés et votre étiquette d'entretien : nous renvoyons une maquette annotée avec champs, hauteurs et classe de code-barres.",
            "es": "¿Estás cerrando la maqueta de una etiqueta y no sabes cómo repartir los nueve campos entre anverso, dorso y etiqueta de cuidado? Envíanos la categoría de producto, los mercados destino y tu etiqueta actual: devolvemos una maqueta anotada con campos, cuerpos de letra y clase de código.",
            "ja": "下げ札のレイアウトを決める段階で、9 項目を表裏と洗濯表示ラベルにどう振るか迷っていませんか。製品カテゴリ・対象市場・現在の洗濯表示をお送りいただければ、項目・文字高・バーコード等級を書き込んだ版面をご提案します。",
            "ko": "행택 레이아웃을 확정 중인데 9개 항목을 앞뒤 면과 세탁 라벨에 어떻게 나눌지 고민이신가요? 제품 카테고리, 대상 시장, 현재 세탁 라벨을 보내주시면 항목·글자 높이·바코드 등급을 표기한 시안을 보내드립니다.",
        },
        {
            "zh": "索取吊牌版面建議 →",
            "en": "Request a tag layout review →",
            "fr": "Demander une revue de maquette →",
            "es": "Solicitar revisión de maqueta →",
            "ja": "下げ札版面の提案を依頼 →",
            "ko": "행택 시안 검토 요청 →",
        },
    )),
]
