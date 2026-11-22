# -*- coding: utf-8 -*-
"""2026-11-22 14:00 第一篇：印尼服裝標籤合規（Indonesia label compliance）（英文主稿，zh/fr/es/ja/ko 從英文翻譯）"""

SLUG = "clothing-label-compliance-indonesia.html"
CAT = {"zh": "合規指南", "en": "Compliance", "fr": "Conformité", "es": "Conformidad",
       "ja": "コンプライアンス", "ko": "컴플라이언스"}
TITLE = {
    "zh": "印尼服裝標籤合規：SNI、印尼語標示與進口要件 | TAGE",
    "en": "Clothing Label Compliance in Indonesia: SNI, Bahasa Indonesia | TAGE",
    "fr": "Étiquetage textile en Indonésie : SNI et mentions en indonésien | TAGE",
    "es": "Etiquetado textil en Indonesia: SNI y menciones en indonesio | TAGE",
    "ja": "インドネシアの衣料ラベル規制：SNI・インドネシア語表示 | TAGE",
    "ko": "인도네시아 의류 라벨 규정: SNI·인도네시아어 표시 | TAGE",
}
DESC = {
    "zh": "出口印尼的服裝標籤要過三關：海關看進口商、監管看 SNI 是否強制、門店看印尼語洗護說明。本文講清 SNI 適用範圍、印尼語必標項目、成分與洗護寫法、cm 與 g/m² 的規格寫法，以及一張可直接發給工廠的標籤清單。",
    "en": "Indonesia label compliance for apparel: when SNI is mandatory, the Indonesian lines customs and stores expect, importer details, care symbols and sizes in cm.",
    "fr": "Étiquetage textile pour l'Indonésie : champ d'application du SNI, mentions obligatoires en indonésien, importateur, symboles d'entretien et tailles en cm.",
    "es": "Etiquetado textil para Indonesia: cuándo el SNI es obligatorio, menciones obligatorias en indonesio, importador, símbolos de cuidado y tallas en cm.",
    "ja": "インドネシア向け衣料ラベルの要点。SNI が義務となる範囲、インドネシア語の必須表示、輸入者情報、洗濯表示、cm 表記のサイズまで整理します。",
    "ko": "인도네시아 의류 라벨 규정 정리. SNI 의무 적용 범위, 인도네시아어 필수 표시, 수입자 정보, 취급 표시, cm 단위 사이즈까지 확인합니다.",
}
H1 = {
    "zh": "印尼標籤合規：海關、監管與門店，三張不同的考卷",
    "en": "Indonesia Label Compliance: Customs, Regulator and Shelf Ask Different Questions",
    "fr": "Conformité en Indonésie : douane, autorité et rayon posent trois questions différentes",
    "es": "Conformidad en Indonesia: aduana, autoridad y tienda preguntan cosas distintas",
    "ja": "インドネシアの表示規制：税関・監督官庁・店頭は別々の問いを投げる",
    "ko": "인도네시아 라벨 규정: 세관, 감독기관, 매장은 서로 다른 것을 묻습니다",
}
DATE = {"zh": "泰閣包裝 · 更新於 2026年11月22日",
        "en": "By TAGE Packaging &nbsp;·&nbsp; Updated November 22, 2026",
        "fr": "Par TAGE Packaging &nbsp;·&nbsp; Mis à jour le 22 novembre 2026",
        "es": "Por TAGE Packaging &nbsp;·&nbsp; Actualizado el 22 de noviembre de 2026",
        "ja": "泰閣包装 · 2026年11月22日更新",
        "ko": "TAGE 패키징 · 2026년 11월 22일 업데이트"}

BLOCKS = [
    ("p", {
        "zh": "印尼是東南亞成長最快的服裝市場之一，也是對「歐洲版標籤直接搬過來賣」最不寬容的市場之一。海關只看進口商與產地那一行，監管部門只看受管制商品有沒有 SNI 標識，百貨與電商平台只看洗護說明能不能用印尼語讀懂。這三關沒有一關在意吊牌好不好看。本文按買家實際提問的順序，把一套印尼標籤該有的內容列清楚。",
        "en": "Indonesia is one of the fastest-growing apparel markets in Southeast Asia, and one of the least forgiving for a label that was designed for Europe and shipped unchanged. Customs reads the importer and origin lines. The regulator checks whether a regulated product carries SNI marking. Department stores and marketplaces check whether the care instructions can be understood in Bahasa Indonesia. None of the three cares how the hang tag looks. This guide lists what a label set for Indonesia has to contain, in the order a buyer will ask for it.",
        "fr": "L'Indonésie est l'un des marchés du vêtement qui progressent le plus vite en Asie du Sud-Est, et l'un des moins tolérants envers une étiquette conçue pour l'Europe et expédiée telle quelle. La douane lit la ligne de l'importateur et l'origine. L'autorité vérifie si un produit réglementé porte le marquage SNI. Les grands magasins et les places de marché vérifient si l'entretien est compréhensible en indonésien. Aucun des trois ne regarde la beauté de l'étiquette pendante. Ce guide donne le contenu attendu, dans l'ordre où l'acheteur le demande.",
        "es": "Indonesia es uno de los mercados de moda que más crece en el Sudeste Asiático y uno de los menos tolerantes con una etiqueta diseñada para Europa y enviada tal cual. La aduana lee la línea del importador y el origen. La autoridad comprueba si un producto regulado lleva marcado SNI. Los grandes almacenes y los marketplaces comprueban si el cuidado se entiende en indonesio. A ninguno de los tres le importa lo bonita que sea la etiqueta colgante. Esta guía ordena el contenido exigible tal como lo pedirá el comprador.",
        "ja": "インドネシアは東南アジアで最も成長している衣料市場のひとつであり、欧州向けに作ったラベルをそのまま送って最も通用しにくい市場でもあります。税関は輸入者と原産国の行を見ます。監督官庁は規制対象品に SNI マークがあるかを見ます。百貨店や EC モールは洗濯表示がインドネシア語で理解できるかを見ます。3 つのどれも、ハングタグの見栄えは見ていません。本稿はバイヤーが尋ねる順に、必要な表示内容を整理します。",
        "ko": "인도네시아는 동남아에서 가장 빠르게 성장하는 의류 시장 중 하나이며, 유럽용으로 만든 라벨을 그대로 보내면 가장 통하기 어려운 시장이기도 합니다. 세관은 수입자와 원산지 항목을 봅니다. 감독기관은 규제 대상 제품에 SNI 표시가 있는지 봅니다. 백화점과 이커머스 플랫폼은 취급 설명을 인도네시아어로 이해할 수 있는지 봅니다. 세 곳 모두 행택이 예쁜지는 보지 않습니다. 이 글은 바이어가 묻는 순서대로 필요한 표시 항목을 정리합니다.",
    }),

    ("h2", {
        "zh": "一、三張考卷，三份不同的文件",
        "en": "1. Three Checks, Three Sets of Documents",
        "fr": "1. Trois contrôles, trois jeux de documents",
        "es": "1. Tres controles, tres juegos de documentos",
        "ja": "1. 3 つの審査、3 種類の書類",
        "ko": "1. 세 가지 심사, 세 가지 서류",
    }),

    ("p", {
        "zh": "最常見的錯誤，是以為縫在領口的那一張洗水標能同時解決三件事。實際上印尼的一套標籤通常由三部分組成：縫入式洗水標（成分、洗護、產地）、吊牌（品牌、型號、條碼）、以及隨貨文件（裝箱單、進口商資料、必要的 SNI 證書影本）。百貨公司驗貨時會把三者對齊，任何一處不一致都會被要求整批重貼。",
        "en": "The most common mistake is expecting the single sewn-in care label to satisfy all three parties. An Indonesian label set normally has three parts: the sewn-in care label with composition, care and origin; the hang tag with brand, style and barcode; and the shipping documents with packing list, importer details and, where applicable, a copy of the SNI certificate. When a department store inspects, it cross-checks all three, and any mismatch means relabelling the lot.",
        "fr": "L'erreur la plus fréquente est de croire que l'étiquette d'entretien cousue suffit aux trois interlocuteurs. Un jeu indonésien comporte en général trois pièces : l'étiquette d'entretien cousue (composition, entretien, origine), l'étiquette pendante (marque, référence, code-barres) et les documents d'expédition (liste de colisage, coordonnées de l'importateur, copie du certificat SNI le cas échéant). Lors d'un contrôle, le grand magasin recoupe les trois : toute divergence impose de réétiqueter le lot.",
        "es": "El error más habitual es suponer que la etiqueta de cuidado cosida satisface a las tres partes. Un juego indonesio suele tener tres piezas: la etiqueta de cuidado cosida (composición, cuidado, origen), la etiqueta colgante (marca, referencia, código de barras) y los documentos de envío (lista de empaque, datos del importador y copia del certificado SNI cuando proceda). En la inspección, el gran almacén cruza las tres: cualquier discrepancia obliga a reetiquetar el lote.",
        "ja": "最も多い誤解は、襟元に縫い付けた洗濯表示 1 枚で 3 者すべてを満たせるというものです。インドネシア向けは通常 3 点で構成します。縫い込みの取扱表示（組成・洗濯方法・原産国）、ハングタグ（ブランド・品番・バーコード）、そして船積書類（パッキングリスト、輸入者情報、必要に応じ SNI 証明書の写し）です。百貨店の検品では 3 点を突き合わせ、不一致があればロット全数の貼り替えを求められます。",
        "ko": "가장 흔한 실수는 목에 봉제한 취급 표시 한 장이 세 곳을 모두 만족한다고 믿는 것입니다. 인도네시아용 라벨 세트는 보통 세 부분입니다. 봉제형 취급 표시(혼용률, 취급 방법, 원산지), 행택(브랜드, 품번, 바코드), 그리고 선적 서류(패킹리스트, 수입자 정보, 필요 시 SNI 인증서 사본)입니다. 백화점 검품에서는 세 가지를 대조하며, 하나라도 어긋나면 로트 전체 재부착을 요구합니다.",
    }),

    ("h2", {
        "zh": "二、SNI：只在法規點名時才是強制",
        "en": "2. SNI: Mandatory Only Where the Regulation Names It",
        "fr": "2. SNI : obligatoire seulement là où le règlement le nomme",
        "es": "2. SNI: obligatorio solo donde el reglamento lo nombra",
        "ja": "2. SNI は法規が指定した範囲でのみ義務",
        "ko": "2. SNI는 법규가 지정한 범위에서만 의무",
    }),

    ("p", {
        "zh": "SNI 是印尼國家標準（Standar Nasional Indonesia）。對多數服裝與輔料而言它是自願性標準，但對列入強制清單的類別（部分兒童用品、部分紡織品與鞋類等）屬於「SNI wajib」，必須完成認證並在產品或包裝上標示 SNI 標誌與證書號。判斷方法只有一個：拿 HS 編碼與品名去問進口商或報關行，確認這條產品線是否在強制清單內。切勿「先印上去再說」——未經認證就標 SNI 標誌，比不標更嚴重。",
        "en": "SNI is the Indonesian National Standard (Standar Nasional Indonesia). For most apparel and trims it is voluntary, but for categories placed on the mandatory list, such as certain children's items, textiles and footwear, it becomes SNI wajib: the product must be certified and marked with the SNI logo and certificate number. There is only one reliable way to find out, and it is not a search engine: give the HS code and product description to your importer or customs broker and ask whether that line sits on the mandatory list. Never print the mark speculatively. An uncertified SNI logo is a worse finding than no logo at all.",
        "fr": "Le SNI est la norme nationale indonésienne (Standar Nasional Indonesia). Pour la plupart des vêtements et accessoires, elle reste volontaire ; pour les catégories inscrites sur la liste obligatoire — certains articles enfant, certains textiles, la chaussure — elle devient SNI wajib : certification et apposition du logo SNI avec numéro de certificat. Une seule méthode fiable : transmettre le code SH et la description à l'importateur ou au commissionnaire en douane et demander si la ligne figure sur la liste. Ne jamais imprimer la marque par précaution : un logo SNI sans certificat est un constat plus grave que l'absence de logo.",
        "es": "El SNI es la norma nacional indonesia (Standar Nasional Indonesia). Para la mayoría de prendas y accesorios es voluntaria; para las categorías incluidas en la lista obligatoria —ciertos artículos infantiles, ciertos textiles, el calzado— pasa a ser SNI wajib: certificación y marcado con el logo SNI y el número de certificado. Solo hay un método fiable: entregar el código HS y la descripción al importador o al agente de aduanas y preguntar si esa línea está en la lista. Nunca imprima la marca por precaución: un logo SNI sin certificado es un hallazgo más grave que su ausencia.",
        "ja": "SNI はインドネシア国家規格（Standar Nasional Indonesia）です。多くの衣料・資材では任意規格ですが、強制リストに載る区分（一部の子供用品、一部の繊維製品、履物など）では SNI wajib となり、認証取得と SNI マーク・証明書番号の表示が必須になります。確認方法は 1 つだけです。HS コードと品名を輸入者または通関業者に渡し、その品目が強制リストに入っているか尋ねること。推測で印刷してはいけません。未認証の SNI マークは、表示しないよりも重い指摘になります。",
        "ko": "SNI는 인도네시아 국가표준(Standar Nasional Indonesia)입니다. 대부분의 의류와 부자재에서는 자율 표준이지만, 강제 목록에 오른 품목(일부 아동용품, 일부 섬유제품, 신발 등)은 SNI wajib가 되어 인증 취득과 SNI 마크·인증서 번호 표시가 필수가 됩니다. 확인 방법은 하나입니다. HS 코드와 품명을 수입자나 관세사에게 보내 해당 품목이 강제 목록에 있는지 물어보십시오. 추측으로 인쇄해서는 안 됩니다. 인증 없이 붙인 SNI 마크는 표시하지 않는 것보다 더 무거운 지적입니다.",
    }),

    ("ul", [
        {
            "zh": "下單前確認 HS 編碼所屬產品線是否在強制 SNI 清單內，並把答覆寫進採購單備註。",
            "en": "Before the order, confirm with the importer whether the HS line is on the mandatory SNI list, and write the answer into the purchase order notes.",
            "fr": "Avant commande, faites confirmer par l'importateur si la ligne SH relève de la liste SNI obligatoire et consignez la réponse dans le bon de commande.",
            "es": "Antes del pedido, confirme con el importador si la línea HS está en la lista SNI obligatoria y deje la respuesta en las notas del pedido.",
            "ja": "発注前に、その HS 品目が SNI 強制リストに該当するか輸入者に確認し、回答を発注書の備考に残します。",
            "ko": "발주 전에 해당 HS 품목이 SNI 강제 목록에 있는지 수입자에게 확인하고, 답변을 발주서 비고에 남깁니다.",
        },
        {
            "zh": "需要認證的品類，把證書號碼的印刷位置預留在洗水標背面或吊牌背面，不要臨時用貼紙補。",
            "en": "For certified categories, reserve a fixed print position for the certificate number on the care label reverse or hang tag back instead of adding a sticker later.",
            "fr": "Pour les catégories certifiées, réservez une zone d'impression fixe pour le numéro de certificat au verso de l'étiquette d'entretien ou de l'étiquette pendante, plutôt qu'un autocollant ajouté après coup.",
            "es": "En categorías certificadas, reserve una zona de impresión fija para el número de certificado al reverso de la etiqueta de cuidado o de la colgante, en lugar de añadir un adhesivo después.",
            "ja": "認証が必要な区分では、証明書番号の印刷位置を取扱表示の裏面またはハングタグ裏面にあらかじめ確保し、後からシールで補わないようにします。",
            "ko": "인증이 필요한 품목은 인증서 번호 인쇄 위치를 취급 표시 뒷면이나 행택 뒷면에 미리 확보하고, 나중에 스티커로 보충하지 않도록 합니다.",
        },
        {
            "zh": "把「不含 SNI 標誌」寫進規格，是對工廠與買家雙方的保護：印了又不能用，等於整批報廢。",
            "en": "Writing 'no SNI mark' into the spec protects both sides: a mark you cannot legally use turns the lot into scrap.",
            "fr": "Inscrire « sans marque SNI » dans la spécification protège les deux parties : une marque inutilisable transforme le lot en rebut.",
            "es": "Escribir 'sin marca SNI' en la especificación protege a ambas partes: una marca que no se puede usar convierte el lote en desecho.",
            "ja": "仕様書に「SNI マークなし」と明記することは双方の保護になります。使えないマークはロット全体を廃棄にします。",
            "ko": "사양서에 'SNI 마크 없음'을 명시하는 것은 양측을 보호합니다. 사용할 수 없는 마크는 로트 전체를 폐기로 만듭니다.",
        },
    ]),

    ("h2", {
        "zh": "三、印尼語標示：哪幾行必須讓消費者讀懂",
        "en": "3. Bahasa Indonesia: Which Lines the Consumer Must Understand",
        "fr": "3. Indonésien : quelles mentions le consommateur doit comprendre",
        "es": "3. Indonesio: qué líneas debe entender el consumidor",
        "ja": "3. インドネシア語表示：消費者が読めるべき行",
        "ko": "3. 인도네시아어 표시: 소비자가 이해해야 하는 항목",
    }),

    ("p", {
        "zh": "印尼消費者保護法（UU No. 8/1999）要求商品資訊以印尼語、且以消費者能理解的方式提供。實務上被要求翻譯的是這五行：成分（Komposisi）、洗護方式（Cara pencucian）、產地（Negara asal）、進口商（Diimpor oleh）、尺碼（Ukuran）。雙語（印尼語＋英語）可以接受，但只寫英語在門店與平台審核時經常被退回。中文、日文或韓文單獨出現，等於沒有標示。",
        "en": "Indonesia's consumer protection law, UU No. 8/1999, requires product information to be provided in Indonesian and in a way the consumer can understand. In practice five lines get translated: composition (Komposisi), care (Cara pencucian), country of origin (Negara asal), importer (Diimpor oleh) and size (Ukuran). Bilingual Indonesian plus English is accepted. English alone is regularly rejected by store and marketplace reviewers, and Chinese, Japanese or Korean on their own count as no labelling at all.",
        "fr": "La loi indonésienne de protection du consommateur (UU No. 8/1999) impose une information produit en indonésien et compréhensible par le consommateur. En pratique, cinq lignes sont traduites : composition (Komposisi), entretien (Cara pencucian), origine (Negara asal), importateur (Diimpor oleh) et taille (Ukuran). Le bilingue indonésien + anglais est accepté ; l'anglais seul est régulièrement refusé par les enseignes et les plateformes, et du chinois, du japonais ou du coréen seuls équivalent à une absence d'étiquetage.",
        "es": "La ley indonesia de protección al consumidor (UU No. 8/1999) exige información del producto en indonesio y comprensible para el consumidor. En la práctica se traducen cinco líneas: composición (Komposisi), cuidado (Cara pencucian), origen (Negara asal), importador (Diimpor oleh) y talla (Ukuran). Se acepta el bilingüe indonesio + inglés; el inglés solo se rechaza con frecuencia en tiendas y marketplaces, y el chino, japonés o coreano por sí solos equivalen a no etiquetar.",
        "ja": "インドネシアの消費者保護法（UU No. 8/1999）は、製品情報をインドネシア語で、消費者が理解できる形で提供することを求めています。実際に翻訳を求められるのは 5 行です。組成（Komposisi）、洗濯方法（Cara pencucian）、原産国（Negara asal）、輸入者（Diimpor oleh）、サイズ（Ukuran）。インドネシア語＋英語の二言語は許容されますが、英語のみは店頭・モール審査で差し戻されることが多く、中国語・日本語・韓国語だけでは未表示と同等と見なされます。",
        "ko": "인도네시아 소비자보호법(UU No. 8/1999)은 제품 정보를 인도네시아어로, 소비자가 이해할 수 있는 방식으로 제공할 것을 요구합니다. 실제로 번역이 요구되는 항목은 다섯 줄입니다. 혼용률(Komposisi), 취급 방법(Cara pencucian), 원산지(Negara asal), 수입자(Diimpor oleh), 사이즈(Ukuran). 인도네시아어와 영어 병기는 허용되지만 영어만 있으면 매장·플랫폼 심사에서 반려되는 일이 많고, 중국어·일본어·한국어만 있으면 미표시와 같습니다.",
    }),

    ("callout", {
        "zh": "把印尼語那五行當成「第二套正文」來排版，不要塞進吊牌邊緣的小字：門店審核看的是洗水標，字高小於 1.5 mm 會被判為不可讀。",
        "en": "Treat the five Indonesian lines as a second body text, not as small print on the hang tag edge. Store reviewers read the care label, and anything below about 1.5 mm cap height is judged unreadable.",
        "fr": "Traitez ces cinq lignes indonésiennes comme un second texte courant, pas comme des mentions en marge de l'étiquette pendante. Le contrôle en magasin lit l'étiquette d'entretien : en dessous d'environ 1,5 mm de hauteur de capitale, le texte est jugé illisible.",
        "es": "Trate esas cinco líneas indonesias como un segundo cuerpo de texto, no como letra pequeña al borde de la colgante. La tienda revisa la etiqueta de cuidado: por debajo de unos 1,5 mm de altura de mayúscula, el texto se considera ilegible.",
        "ja": "インドネシア語の 5 行は「第 2 の本文」として組んでください。ハングタグの端の小さな注記にしてはいけません。店頭審査が見るのは取扱表示で、文字の高さが約 1.5 mm 未満だと判読不可と判定されます。",
        "ko": "인도네시아어 다섯 줄은 두 번째 본문으로 조판하십시오. 행택 가장자리의 작은 글씨로 넣지 마십시오. 매장 심사는 취급 표시를 보며, 글자 높이가 약 1.5 mm 미만이면 판독 불가로 판정됩니다.",
    }),

    ("h2", {
        "zh": "四、成分與洗護：退貨最集中的兩行",
        "en": "4. Composition and Care: the Two Lines Behind Most Returns",
        "fr": "4. Composition et entretien : les deux lignes qui provoquent le plus de retours",
        "es": "4. Composición y cuidado: las dos líneas detrás de la mayoría de devoluciones",
        "ja": "4. 組成と洗濯表示：返品が最も集中する 2 行",
        "ko": "4. 혼용률과 취급 표시: 반품이 가장 몰리는 두 줄",
    }),

    ("p", {
        "zh": "成分要按纖維逐項列出，並用當地讀得懂的名稱：Cotton 寫 Katun、Polyester 寫 Poliester、Elastane 寫 Spandex 或 Elastane，並註明百分比。混紡容差建議按 ±3% 寫進規格（各市場容許值不同，出口歐盟時對應法規為 Regulation (EU) No 1007/2011 的纖維標示要求）。洗護部分，符號與文字必須同時出現：只有符號，印尼消費者不熟悉；只有文字，工廠與洗滌廠不好執行。",
        "en": "List fibres one by one with names a local reader recognises: cotton as Katun, polyester as Poliester, elastane as Spandex or Elastane, each with a percentage. Put the blend tolerance into the spec, typically plus or minus 3 percent, and note that the permitted tolerance differs by market: for the European Union the fibre labelling rules sit in Regulation (EU) No 1007/2011. On care, print symbols and words together. Symbols alone are unfamiliar to many Indonesian shoppers, and words alone are hard to execute on the factory floor.",
        "fr": "Listez les fibres une à une avec des noms lisibles localement : coton = Katun, polyester = Poliester, élasthanne = Spandex ou Elastane, chacune avec son pourcentage. Inscrivez la tolérance de mélange dans la spécification, souvent plus ou moins 3 %, en rappelant qu'elle varie selon le marché : dans l'Union européenne, l'étiquetage des fibres relève du règlement (UE) n° 1007/2011. Pour l'entretien, imprimez symboles et texte ensemble : les symboles seuls sont méconnus de nombreux acheteurs indonésiens, le texte seul est difficile à appliquer en atelier.",
        "es": "Enumere las fibras una a una con nombres que el lector local reconozca: algodón como Katun, poliéster como Poliester, elastano como Spandex o Elastane, cada una con su porcentaje. Incluya la tolerancia de mezcla en la especificación, habitualmente más o menos 3 %, recordando que varía por mercado: en la Unión Europea el etiquetado de fibras se rige por el Reglamento (UE) n.º 1007/2011. En el cuidado, imprima símbolos y palabras juntos: los símbolos solos resultan poco conocidos para muchos compradores indonesios y el texto solo es difícil de ejecutar en planta.",
        "ja": "繊維は現地で通じる名称で 1 つずつ割合とともに記載します。綿は Katun、ポリエステルは Poliester、伸縮性繊維は Spandex または Elastane と書き、混率を併記します。混紡の許容差は仕様書に入れ（目安は ±3 %、市場ごとに異なります。EU 向けの繊維表示は Regulation (EU) No 1007/2011 が根拠です）。洗濯表示は記号と文字を併記してください。記号だけではインドネシアの消費者に伝わりにくく、文字だけでは工場・洗濯業者が運用しづらくなります。なお日本国内向けは家庭用品品質表示法により組成と取扱表示が義務づけられ、洗濯記号は JIS L 0001（ISO 3758 準拠）に従います。インドネシア向けも同じ記号体系（SNI ISO 3758）なので、記号の設計は 1 回で共用できます。",
        "ko": "섬유는 현지에서 통하는 명칭으로 비율과 함께 하나씩 기재합니다. 면은 Katun, 폴리에스터는 Poliester, 탄성섬유는 Spandex 또는 Elastane으로 쓰고 혼용률을 병기합니다. 혼용 허용 오차는 사양서에 넣습니다(기준 ±3 %, 시장별로 다릅니다. EU 수출 시 섬유 표시는 Regulation (EU) No 1007/2011이 근거입니다). 취급 표시는 기호와 문구를 함께 넣으십시오. 기호만으로는 인도네시아 소비자가 이해하기 어렵고, 문구만으로는 공장과 세탁업체가 운용하기 어렵습니다. 국내 판매분은 전기용품 및 생활용품 안전관리법에 따른 표시 의무와 혼용률 기재가 필요하며, 과장된 기능성 문구는 표시광고법 위반이 될 수 있으므로 수출용 라벨에도 검증되지 않은 표현은 넣지 마십시오.",
    }),

    ("ul", [
        {
            "zh": "纖維名稱用印尼語慣用詞，不要只寫英文縮寫（PE、PA、PU 在當地執法檢查時常被要求展開）。",
            "en": "Use the Indonesian fibre names rather than English abbreviations alone; PE, PA and PU are routinely challenged in local inspections.",
            "fr": "Employez les noms de fibres indonésiens plutôt que des abréviations anglaises seules : PE, PA et PU sont souvent contestés en contrôle local.",
            "es": "Use los nombres indonesios de las fibras en lugar de siglas inglesas solas: PE, PA y PU se cuestionan con frecuencia en inspecciones locales.",
            "ja": "英語の略号だけにせず、インドネシア語の繊維名を使ってください。PE・PA・PU は現地検査で展開を求められることがよくあります。",
            "ko": "영문 약어만 쓰지 말고 인도네시아어 섬유 명칭을 사용하십시오. PE, PA, PU는 현지 검사에서 풀어서 표기하라는 요구를 자주 받습니다.",
        },
        {
            "zh": "洗護符號按 ISO 3758 體系（印尼採用為 SNI ISO 3758），並在符號下加一行印尼語說明。",
            "en": "Base the care symbols on the ISO 3758 system, adopted in Indonesia as SNI ISO 3758, and add one Indonesian line under the symbols.",
            "fr": "Fondez les symboles sur le système ISO 3758, repris en Indonésie sous le nom SNI ISO 3758, et ajoutez une ligne indonésienne sous les symboles.",
            "es": "Base los símbolos en el sistema ISO 3758, adoptado en Indonesia como SNI ISO 3758, y añada una línea en indonesio bajo los símbolos.",
            "ja": "洗濯記号は ISO 3758 体系（インドネシアでは SNI ISO 3758 として採用）に合わせ、記号の下にインドネシア語の説明を 1 行入れます。",
            "ko": "취급 기호는 ISO 3758 체계(인도네시아에서는 SNI ISO 3758로 채택)를 따르고, 기호 아래에 인도네시아어 설명 한 줄을 넣습니다.",
        },
        {
            "zh": "熱帶市場的洗護要寫得比歐洲保守：水溫 30 °C、陰乾、避免滾筒烘乾，能明顯降低洗後縮水與印花開裂的投訴。",
            "en": "Write care more conservatively than for Europe: 30 °C, line dry in shade, no tumble drying. It visibly reduces complaints about shrinkage and cracked prints after washing.",
            "fr": "Rédigez l'entretien plus prudemment que pour l'Europe : 30 °C, séchage à l'ombre sur fil, pas de sèche-linge. Cela réduit nettement les réclamations de retrait et de motifs fissurés.",
            "es": "Redacte el cuidado con más prudencia que para Europa: 30 °C, secado a la sombra en tendedero, sin secadora. Reduce de forma visible las reclamaciones por encogimiento y estampados agrietados.",
            "ja": "熱帯市場では欧州向けより保守的に書きます。30 °C、陰干し、タンブラー乾燥禁止。洗濯後の縮みやプリントひび割れのクレームが明らかに減ります。",
            "ko": "열대 시장에서는 유럽보다 보수적으로 작성하십시오. 30 °C, 그늘 건조, 텀블러 건조 금지. 세탁 후 수축과 프린트 갈라짐 클레임이 눈에 띄게 줄어듭니다.",
        },
    ]),

    ("h2", {
        "zh": "五、尺碼與克重：「All Size」的風險",
        "en": "5. Sizes and Weight: the 'All Size' Risk",
        "fr": "5. Tailles et grammage : le risque du « All Size »",
        "es": "5. Tallas y gramaje: el riesgo del «All Size»",
        "ja": "5. サイズと目付：「All Size」のリスク",
        "ko": "5. 사이즈와 평량: 'All Size'의 위험",
    }),

    ("p", {
        "zh": "印尼零售大量使用 S–XXL，也有品牌以「All Size」販售版型寬鬆的單品。出口或跨境電商時，尺碼標上只寫 S/M/L 不夠：請同時在規格與吊牌背面列出實測尺寸，例如胸寬 52 cm、衣長 70 cm、容差 ±1 cm；布料克重寫成 180 g/m² 或 220 g/m²，不要只寫 gsm。對頭巾、長袍這類版型，衣長與袖長必須標 cm，這是當地退貨率最高的兩個尺寸。",
        "en": "Indonesian retail runs heavily on S to XXL, and many brands sell loose styles as All Size. For export and cross-border e-commerce, S/M/L on the size label is not enough: list measured dimensions in the spec and on the hang tag back, for example chest width 52 cm and body length 70 cm with a tolerance of plus or minus 1 cm. State fabric weight as 180 g/m² or 220 g/m² rather than gsm alone. For hijabs and long tunics, body and sleeve length must be given in cm; those are the two dimensions that drive the highest return rates locally.",
        "fr": "Le commerce indonésien fonctionne beaucoup en S à XXL, et de nombreuses marques vendent des coupes amples en All Size. À l'export et en e-commerce transfrontalier, S/M/L sur l'étiquette de taille ne suffit pas : indiquez les mesures dans la spécification et au verso de l'étiquette pendante, par exemple largeur de poitrine 52 cm et longueur 70 cm avec une tolérance de plus ou moins 1 cm. Exprimez le grammage en 180 g/m² ou 220 g/m², pas seulement en gsm. Pour les hijabs et tuniques longues, longueur et manche doivent être en cm : ce sont les deux dimensions qui génèrent le plus de retours.",
        "es": "El retail indonesio trabaja mucho en S a XXL, y muchas marcas venden cortes holgados como All Size. Para exportación y e-commerce transfronterizo, S/M/L en la etiqueta de talla no basta: incluya medidas en la especificación y al reverso de la colgante, por ejemplo ancho de pecho 52 cm y largo 70 cm con tolerancia de más o menos 1 cm. Exprese el gramaje como 180 g/m² o 220 g/m², no solo como gsm. En hiyabs y túnicas largas, largo y manga deben ir en cm: son las dos dimensiones que generan más devoluciones.",
        "ja": "インドネシアの小売は S〜XXL が中心で、ゆったりした型を All Size として売るブランドも多くあります。輸出や越境 EC では、サイズラベルの S/M/L だけでは足りません。仕様書とハングタグ裏面に実寸を記載します。例：身幅 52 cm、着丈 70 cm、許容差 ±1 cm。生地目付は 180 g/m²、220 g/m² のように書き、gsm だけにしません。ヒジャブやロング丈では着丈と袖丈を cm で明記してください。現地で返品が最も多い 2 項目です。",
        "ko": "인도네시아 소매는 S~XXL 중심이며, 여유 있는 핏을 All Size로 판매하는 브랜드도 많습니다. 수출과 크로스보더 이커머스에서는 사이즈 라벨의 S/M/L만으로 부족합니다. 사양서와 행택 뒷면에 실측 치수를 적으십시오. 예: 가슴단면 52 cm, 총장 70 cm, 허용 오차 ±1 cm. 원단 평량은 180 g/m², 220 g/m²처럼 쓰고 gsm만 쓰지 마십시오. 히잡과 롱 원피스는 총장과 소매 길이를 cm로 명기해야 하며, 현지 반품이 가장 많은 두 항목입니다.",
    }),

    ("h2", {
        "zh": "六、一張可以直接發給工廠的標籤清單",
        "en": "6. A Label Table You Can Send to the Factory Today",
        "fr": "6. Un tableau d'étiquetage à envoyer tel quel à l'usine",
        "es": "6. Una tabla de etiquetado que puede enviar hoy a la fábrica",
        "ja": "6. そのまま工場に送れるラベル一覧表",
        "ko": "6. 공장에 바로 보낼 수 있는 라벨 표",
    }),

    ("table", {
        "head": [
            {"zh": "項目", "en": "Item", "fr": "Élément", "es": "Elemento", "ja": "項目", "ko": "항목"},
            {"zh": "印尼語寫法", "en": "Indonesian wording", "fr": "Formulation indonésienne", "es": "Redacción en indonesio", "ja": "インドネシア語表記", "ko": "인도네시아어 표기"},
            {"zh": "放在哪裡", "en": "Where it goes", "fr": "Où l'apposer", "es": "Dónde va", "ja": "表示位置", "ko": "표시 위치"},
        ],
        "rows": [
            [
                {"zh": "產地", "en": "Country of origin", "fr": "Origine", "es": "Origen", "ja": "原産国", "ko": "원산지"},
                {"zh": "Negara asal: Tiongkok", "en": "Negara asal: Tiongkok", "fr": "Negara asal : Tiongkok", "es": "Negara asal: Tiongkok", "ja": "Negara asal: Tiongkok", "ko": "Negara asal: Tiongkok"},
                {"zh": "洗水標正反面均可，外箱必須同寫", "en": "Care label front or back; the carton must match", "fr": "Étiquette d'entretien recto ou verso ; le carton doit concorder", "es": "Etiqueta de cuidado anverso o reverso; el cartón debe coincidir", "ja": "取扱表示の表裏いずれか、外箱にも同じ表記", "ko": "취급 표시 앞뒷면 중 한 곳, 외장에도 동일 표기"},
            ],
            [
                {"zh": "進口商", "en": "Importer", "fr": "Importateur", "es": "Importador", "ja": "輸入者", "ko": "수입자"},
                {"zh": "Diimpor oleh: PT ...", "en": "Diimpor oleh: PT ...", "fr": "Diimpor oleh : PT ...", "es": "Diimpor oleh: PT ...", "ja": "Diimpor oleh: PT ...", "ko": "Diimpor oleh: PT ..."},
                {"zh": "洗水標背面或吊牌背面", "en": "Care label reverse or hang tag back", "fr": "Verso de l'étiquette d'entretien ou de l'étiquette pendante", "es": "Reverso de la etiqueta de cuidado o de la colgante", "ja": "取扱表示の裏面またはハングタグ裏面", "ko": "취급 표시 뒷면 또는 행택 뒷면"},
            ],
            [
                {"zh": "成分", "en": "Composition", "fr": "Composition", "es": "Composición", "ja": "組成", "ko": "혼용률"},
                {"zh": "Komposisi: 95% Katun, 5% Spandex", "en": "Komposisi: 95% Katun, 5% Spandex", "fr": "Komposisi : 95% Katun, 5% Spandex", "es": "Komposisi: 95% Katun, 5% Spandex", "ja": "Komposisi: 95% Katun, 5% Spandex", "ko": "Komposisi: 95% Katun, 5% Spandex"},
                {"zh": "洗水標正面，字高 ≥1.5 mm", "en": "Care label front, cap height 1.5 mm or more", "fr": "Recto de l'étiquette d'entretien, hauteur de capitale ≥ 1,5 mm", "es": "Anverso de la etiqueta, altura de mayúscula ≥ 1,5 mm", "ja": "取扱表示の表面、文字高 1.5 mm 以上", "ko": "취급 표시 앞면, 글자 높이 1.5 mm 이상"},
            ],
            [
                {"zh": "洗護", "en": "Care", "fr": "Entretien", "es": "Cuidado", "ja": "洗濯方法", "ko": "취급 방법"},
                {"zh": "Cara pencucian: 30 °C, jangan diperas", "en": "Cara pencucian: 30 °C, jangan diperas", "fr": "Cara pencucian : 30 °C, jangan diperas", "es": "Cara pencucian: 30 °C, jangan diperas", "ja": "Cara pencucian: 30 °C, jangan diperas", "ko": "Cara pencucian: 30 °C, jangan diperas"},
                {"zh": "洗水標，符號＋文字並列", "en": "Care label, symbols plus words", "fr": "Étiquette d'entretien, symboles et texte", "es": "Etiqueta de cuidado, símbolos y texto", "ja": "取扱表示、記号と文字を併記", "ko": "취급 표시, 기호와 문구 병기"},
            ],
            [
                {"zh": "尺碼", "en": "Size", "fr": "Taille", "es": "Talla", "ja": "サイズ", "ko": "사이즈"},
                {"zh": "Ukuran: M (chest 52 cm / length 70 cm)", "en": "Ukuran: M (chest 52 cm / length 70 cm)", "fr": "Ukuran : M (poitrine 52 cm / longueur 70 cm)", "es": "Ukuran: M (pecho 52 cm / largo 70 cm)", "ja": "Ukuran: M（身幅 52 cm／着丈 70 cm）", "ko": "Ukuran: M (가슴 52 cm / 총장 70 cm)"},
                {"zh": "尺碼標＋吊牌背面", "en": "Size label plus hang tag back", "fr": "Étiquette de taille et verso de l'étiquette pendante", "es": "Etiqueta de talla y reverso de la colgante", "ja": "サイズラベルとハングタグ裏面", "ko": "사이즈 라벨과 행택 뒷면"},
            ],
        ],
    }),

    ("h2", {
        "zh": "七、下單前確認的五個數字",
        "en": "7. Five Numbers to Fix Before the Order",
        "fr": "7. Cinq chiffres à figer avant la commande",
        "es": "7. Cinco cifras que fijar antes del pedido",
        "ja": "7. 発注前に固定する 5 つの数値",
        "ko": "7. 발주 전에 확정할 다섯 가지 수치",
    }),

    ("ul", [
        {
            "zh": "纖維比例與容差（例如 ±3%），寫進規格而不是只留在郵件裡。",
            "en": "Fibre percentages and tolerance, for example plus or minus 3 percent, written into the spec rather than left in an email.",
            "fr": "Pourcentages de fibres et tolérance, par exemple plus ou moins 3 %, inscrits dans la spécification et non laissés dans un e-mail.",
            "es": "Porcentajes de fibras y tolerancia, por ejemplo más o menos 3 %, escritos en la especificación y no solo en un correo.",
            "ja": "繊維混率と許容差（例：±3 %）は、メールではなく仕様書に記載します。",
            "ko": "섬유 혼용률과 허용 오차(예: ±3 %)는 메일이 아니라 사양서에 기록합니다.",
        },
        {
            "zh": "洗水標尺寸與字高：常用 20 × 50 mm 或 25 × 60 mm，字高 ≥1.5 mm，八種符號一排。",
            "en": "Care label size and type height: 20 × 50 mm or 25 × 60 mm are common, with at least 1.5 mm text and one row of symbols.",
            "fr": "Format et hauteur de texte de l'étiquette d'entretien : 20 × 50 mm ou 25 × 60 mm sont courants, avec un texte d'au moins 1,5 mm et une rangée de symboles.",
            "es": "Tamaño y altura de texto de la etiqueta: 20 × 50 mm o 25 × 60 mm son habituales, con texto de al menos 1,5 mm y una fila de símbolos.",
            "ja": "取扱表示の寸法と文字高：20 × 50 mm か 25 × 60 mm が一般的で、文字高 1.5 mm 以上、記号は 1 列に。",
            "ko": "취급 표시 크기와 글자 높이: 20 × 50 mm 또는 25 × 60 mm가 일반적이며, 글자 높이 1.5 mm 이상, 기호는 한 줄로.",
        },
        {
            "zh": "吊牌紙張克重：一般 300–350 g/m²，需燙金或壓凹時提高到 350–400 g/m² 才不會變形。",
            "en": "Hang tag board weight: 300 to 350 g/m² normally, raised to 350 to 400 g/m² when foil stamping or embossing is used so the tag does not warp.",
            "fr": "Grammage du carton de l'étiquette pendante : 300 à 350 g/m² en standard, porté à 350 à 400 g/m² en cas de dorure ou de gaufrage pour éviter la déformation.",
            "es": "Gramaje del cartón de la colgante: 300 a 350 g/m² de serie, elevado a 350 a 400 g/m² con dorado o relieve para que no se deforme.",
            "ja": "ハングタグの板紙目付：通常 300〜350 g/m²、箔押しやエンボスがある場合は反りを防ぐため 350〜400 g/m² に上げます。",
            "ko": "행택 지질 평량: 보통 300~350 g/m², 금박이나 엠보싱이 있으면 변형 방지를 위해 350~400 g/m²로 올립니다.",
        },
        {
            "zh": "印尼語文案必須由進口商書面確認，尤其進口商名稱與地址——拼錯一個字母就可能卡在海關。",
            "en": "The Indonesian copy must be confirmed in writing by the importer, especially the importer name and address; one wrong letter can hold the shipment at customs.",
            "fr": "Le texte indonésien doit être validé par écrit par l'importateur, en particulier sa raison sociale et son adresse : une lettre erronée peut bloquer l'envoi en douane.",
            "es": "El texto indonesio debe confirmarlo por escrito el importador, sobre todo nombre y dirección: una letra equivocada puede retener el envío en aduana.",
            "ja": "インドネシア語の文案は輸入者が書面で確認してください。特に輸入者名と住所は、1 文字の誤りで通関が止まることがあります。",
            "ko": "인도네시아어 문안은 수입자가 서면으로 확인해야 하며, 특히 수입자 명칭과 주소는 한 글자 오류로 통관이 지체될 수 있습니다.",
        },
        {
            "zh": "交期：把標籤打樣與進口商確認各留 5–7 天，別把這兩段算進生產期。",
            "en": "Lead time: allow five to seven days each for label proofing and importer sign-off, and do not bury them inside the production window.",
            "fr": "Délais : prévoyez cinq à sept jours pour la maquette d'étiquette et autant pour la validation de l'importateur, sans les fondre dans le délai de production.",
            "es": "Plazo: reserve de cinco a siete días para la prueba de etiqueta y otros tantos para la aprobación del importador, sin esconderlos dentro de la producción.",
            "ja": "納期：ラベルの校正と輸入者確認にそれぞれ 5〜7 日を見込み、生産期間に埋め込まないでください。",
            "ko": "납기: 라벨 교정과 수입자 확인에 각각 5~7일을 두고, 생산 기간에 숨기지 마십시오.",
        },
    ]),

    ("p", {
        "zh": "印尼市場的回報屬於準備充分的人：同一款衣服，標籤寫對的供應商可以連續補單，寫錯的供應商會卡在第一批。把上面三份文件、五行印尼語與五個數字固定下來，標籤就從風險變成可複製的工序。",
        "en": "Indonesia rewards preparation. On the same garment, a supplier whose labels are right keeps earning repeat orders, while one whose labels are wrong stalls at the first shipment. Fix the three documents, the five Indonesian lines and the five numbers, and labelling stops being a risk and becomes a repeatable process.",
        "fr": "L'Indonésie récompense la préparation. Sur un même vêtement, le fournisseur dont les étiquettes sont justes enchaîne les réassorts, celui dont les étiquettes sont fausses s'arrête à la première expédition. Figez les trois documents, les cinq lignes indonésiennes et les cinq chiffres : l'étiquetage cesse d'être un risque pour devenir un processus reproductible.",
        "es": "Indonesia premia la preparación. Con la misma prenda, el proveedor cuyas etiquetas son correctas encadena reposiciones y el que se equivoca se detiene en el primer envío. Fije los tres documentos, las cinco líneas en indonesio y las cinco cifras: el etiquetado deja de ser un riesgo y pasa a ser un proceso repetible.",
        "ja": "インドネシアは準備した者に報いる市場です。同じ服でも、表示が正しい供給者は追加発注が続き、誤った供給者は初回出荷で止まります。3 種類の書類、インドネシア語 5 行、5 つの数値を固定すれば、表示はリスクではなく再現できる工程になります。",
        "ko": "인도네시아는 준비한 쪽에 보상하는 시장입니다. 같은 의류라도 표시가 정확한 공급자는 재주문이 이어지고, 틀린 공급자는 첫 선적에서 멈춥니다. 세 가지 서류, 인도네시아어 다섯 줄, 다섯 가지 수치를 고정하면 라벨은 위험이 아니라 재현 가능한 공정이 됩니다.",
    }),
]

RELATED = [
    {"slug": "clothing-label-requirements-southeast-asia.html",
     "zh": "東南亞服裝標籤要求：五國對照", "en": "Southeast Asia label requirements: five markets compared",
     "fr": "Exigences d'étiquetage en Asie du Sud-Est : cinq marchés", "es": "Requisitos de etiquetado en el Sudeste Asiático: cinco mercados",
     "ja": "東南亞の衣料ラベル要件：5 か国比較", "ko": "동남아 의류 라벨 요건: 5개국 비교"},
    {"slug": "clothing-label-compliance-vietnam.html",
     "zh": "越南服裝標籤合規要點", "en": "Vietnam label compliance essentials",
     "fr": "Étiquetage textile au Vietnam : l'essentiel", "es": "Etiquetado textil en Vietnam: lo esencial",
     "ja": "ベトナムの衣料ラベル規制の要点", "ko": "베트남 의류 라벨 규정 핵심"},
    {"slug": "care-label-symbols-chart.html",
     "zh": "洗護符號對照表：一次看懂", "en": "Care symbol chart: read it at a glance",
     "fr": "Tableau des symboles d'entretien", "es": "Tabla de símbolos de cuidado",
     "ja": "洗濯表示記号の一覧表", "ko": "취급 기호 도표"},
    {"slug": "care-label-multilingual-guide.html",
     "zh": "多語洗水標：幾種語言才夠", "en": "Multilingual care labels: how many languages are enough",
     "fr": "Étiquettes multilingues : combien de langues", "es": "Etiquetas multilingües: cuántos idiomas bastan",
     "ja": "多言語の洗濯表示：何言語必要か", "ko": "다국어 취급 표시: 몇 개 언어가 필요한가"},
]

CTA_P = {
    "zh": "要為印尼市場做一套標籤？把款式、HS 編碼、目標渠道（百貨／電商／批發）與進口商資料發給我們，我們會回一份含印尼語文案、成分與洗護寫法、cm 實測尺寸與紙張克重的規格稿，並附樣品。",
    "en": "Building a label set for Indonesia? Send the style, HS code, sales channel and importer details, and we will return a specification with the Indonesian copy, composition and care wording, measured sizes in cm and board weight, plus a sample.",
    "fr": "Un jeu d'étiquettes pour l'Indonésie ? Envoyez le modèle, le code SH, le canal de vente et les données de l'importateur : nous renverrons une spécification avec texte indonésien, composition, entretien, mesures en cm et grammage, plus un échantillon.",
    "es": "¿Preparando etiquetas para Indonesia? Envíe el modelo, el código HS, el canal de venta y los datos del importador: devolveremos una especificación con texto en indonesio, composición, cuidado, medidas en cm y gramaje, más una muestra.",
    "ja": "インドネシア向けのラベル一式をお考えですか。型番、HS コード、販売チャネル、輸入者情報をお送りください。インドネシア語文案、組成・洗濯表示、cm 実寸、板紙目付を含む仕様とサンプルをご提案します。",
    "ko": "인도네시아용 라벨 세트를 준비하시나요? 스타일, HS 코드, 판매 채널, 수입자 정보를 보내주십시오. 인도네시아어 문안, 혼용률·취급 표시, cm 실측 치수, 지질 평량을 담은 사양서와 샘플을 제안합니다.",
}
CTA_BTN = {
    "zh": "索取印尼標籤規格 →", "en": "Request an Indonesia label spec →",
    "fr": "Demander une spécification →", "es": "Solicitar una especificación →",
    "ja": "インドネシア向け仕様を依頼 →", "ko": "인도네시아 라벨 사양 요청 →",
}
