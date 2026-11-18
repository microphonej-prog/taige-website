# -*- coding: utf-8 -*-
"""2026-11-18 08:00 批次 A：洗水标纤维成分容差（3% 规则 / other fibre / 整数量取）"""

SLUG = "care-label-fiber-content-tolerance-guide"
CATEGORY = {
    "zh": "洗水標與合規", "en": "Care Labels & Compliance", "fr": "Étiquetage et conformité",
    "es": "Etiquetado y cumplimiento", "ja": "洗濯表示・コンプライアンス", "ko": "세탁 표시·컴플라이언스",
}
TITLE = {
    "zh": "洗水標纖維成分容差：3% 容許與「其他纖維」怎麼寫 | TAGE",
    "en": "Fiber Content Tolerance on Care Labels: The 3% Rule and Other Fibre | TAGE",
    "fr": "Tolérance de composition sur l'étiquette d'entretien : la règle des 3 % | TAGE",
    "es": "Tolerancia de composición en la etiqueta de cuidado: la regla del 3 % | TAGE",
    "ja": "洗濯表示の混用率の許容範囲：3 % と「その他繊維」の書き方 | TAGE",
    "ko": "세탁 표시 혼용률 허용 오차: 3%와 '기타 섬유' 표기 | TAGE",
}
DESC = {
    "zh": "洗水標上的纖維成分能差多少：歐盟 1007/2011 的 3% 容差、美國 16 CFR Part 303 的 5% 其他纖維門檻、整數取整規則，附 62/33/5 實例與 ISO 1833、JIS L 1030、KS K 0210 的檢測判定。",
    "en": "Care label fibre tolerance: the 3% rule, the 5% other-fibre threshold, whole-percent rounding, a 62/33/5 worked example and how ISO 1833 testing decides.",
    "fr": "Quel écart de composition une étiquette d'entretien peut porter : tolérance de 3 %, seuil de 5 % pour les autres fibres, arrondi au pourcent entier et essai ISO 1833.",
    "es": "Qué desviación de composición admite una etiqueta de cuidado: tolerancia del 3 %, umbral del 5 % para otras fibras, redondeo entero y ensayo ISO 1833.",
    "ja": "洗濯表示の混用率はどこまでずれてよいのか。3 % の許容、5 % 未満の「その他繊維」、整数への丸め、62/33/5 の実例、ISO 1833・JIS L 1030 による判定を整理します。",
    "ko": "세탁 표시 혼용률은 어디까지 허용되는가. 3% 허용 오차, 5% 미만 '기타 섬유' 처리, 정수 반올림, 62/33/5 실제 예시와 ISO 1833·KS K 0210 판정 기준을 정리합니다.",
}
H1 = {
    "zh": "洗水標纖維成分容差：3% 容許與「其他纖維」怎麼寫",
    "en": "Fiber Content Tolerance on Care Labels",
    "fr": "Tolérance de composition sur l'étiquette d'entretien",
    "es": "Tolerancia de composición en la etiqueta de cuidado",
    "ja": "洗濯表示の混用率の許容範囲",
    "ko": "세탁 표시 혼용률 허용 오차",
}

BLOCKS = [
    ("p", {
        "zh": "洗水標上有兩個數字會決定它能不能過關：標上寫的成分，和實驗室測出來的成分。兩者之間的差距就是容差——而容差恰好是最多人憑記憶寫的一項。本文把實際會被引用的三道門檻講清楚：歐盟對製造上不可避免偏差的 3% 容差、美國讓 5% 以下纖維併入「其他纖維」的門檻、以及整數百分比的取整規則；再給一個能同時通過化學分析與市場監管的寫法。",
        "en": "Two numbers decide whether a care label survives a compliance check: the composition printed on it, and the composition a laboratory measures. Everything between them is tolerance, and tolerance is the part most brands write from memory. This guide sets out the three thresholds that actually get applied: the 3% allowance for unavoidable manufacturing variance, the 5% threshold below which a fibre may be folded into other fibre, and the rule of whole-percent rounding. It then shows a blend written to pass both a chemical analysis and a market surveillance check.",
        "fr": "Deux chiffres décident si une étiquette d'entretien résiste à un contrôle : la composition imprimée et celle que le laboratoire mesure. Entre les deux se trouve la tolérance, et c'est justement la partie que la plupart des marques rédigent de mémoire. Ce guide pose les trois seuils réellement appliqués : la tolérance de 3 % pour les écarts inévitables de fabrication, le seuil de 5 % en dessous duquel une fibre peut être regroupée en autres fibres, et l'arrondi au pourcent entier.",
        "es": "Dos cifras deciden si una etiqueta de cuidado supera un control: la composición impresa y la que mide el laboratorio. Entre ambas está la tolerancia, y la tolerancia es justo la parte que casi todas las marcas escriben de memoria. Esta guía fija los tres umbrales que de verdad se aplican: la tolerancia del 3 % para desviaciones inevitables de fabricación, el umbral del 5 % por debajo del cual una fibra puede agruparse como otras fibras y el redondeo al porcentaje entero.",
        "ja": "表示ラベルが検査を通るかどうかは、2 つの数字で決まります。ラベルに書いた混用率と、試験室が測った混用率です。その差が許容範囲であり、多くのブランドが記憶で書いてしまう部分でもあります。本稿では実際に適用される 3 つの基準を整理します。製造上避けられないばらつきに対する 3 % の許容、5 % 未満の繊維を「その他繊維」にまとめられるしきい値、そして整数パーセントへの丸めです。",
        "ko": "관리 라벨이 검사를 통과할지는 두 숫자로 결정됩니다. 라벨에 적은 혼용률과 시험실이 측정한 혼용률입니다. 그 사이의 차이가 허용 오차이며, 대부분의 브랜드가 기억에 의존해 적는 부분이기도 합니다. 이 글은 실제로 적용되는 세 가지 기준을 정리합니다. 제조상 불가피한 편차에 대한 3% 허용, 5% 미만 섬유를 기타 섬유로 묶을 수 있는 기준, 그리고 정수 퍼센트 반올림입니다.",
    }),
    ("h2", {
        "zh": "一、容差管的是「不可避免」，不是「可以寫錯」",
        "en": "1. Tolerance Covers the Unavoidable, Not the Careless",
        "fr": "1. La tolérance couvre l'inévitable, pas la négligence",
        "es": "1. La tolerancia cubre lo inevitable, no el descuido",
        "ja": "1. 許容は「避けられないばらつき」のためであり、書き間違いの免罪符ではない",
        "ko": "1. 허용 오차는 불가피한 편차를 위한 것이지 오기를 위한 것이 아니다",
    }),
    ("p", {
        "zh": "容差的立法目的，是讓纺紗混料、織造損耗、後整理重量變化這些沒人能精確控制的環節不被當成違規。它不覆蓋你自己做的變更：品牌從 60/40 改成 65/35 卻沒重印標籤，不論差距看起來多小，標籤就是錯的。洗水標是車在衣服上、不能撕掉的永久載體，市場監管人員第一個翻的就是它，而吊牌已經隨包裝丟掉了。",
        "en": "Tolerance exists for processes nobody can control exactly: fibre mixing at the spinning mill, yarn loss at weaving, weight change in finishing. It does not cover a change you made yourself. If a brand moves from 60/40 to 65/35 without reprinting, the label is wrong however small the gap looks. The care label is the permanent carrier sewn into the garment, so it is the first thing a market surveillance officer reads, long after the hang tag has gone in the bin.",
        "fr": "La tolérance existe pour des opérations que personne ne maîtrise au pourcent près : le mélange à la filature, la perte de fil au tissage, la variation de poids en finition. Elle ne couvre pas une modification décidée par la marque. Passer de 60/40 à 65/35 sans réimprimer rend l'étiquette fausse, quel que soit l'écart apparent. L'étiquette d'entretien est le support permanent cousu au vêtement : c'est elle que lit le contrôle du marché, bien après que l'étiquette volante est partie à la poubelle.",
        "es": "La tolerancia existe para operaciones que nadie controla al porcentaje exacto: la mezcla en la hilatura, la pérdida de hilo en el tejido, la variación de peso en el acabado. No cubre un cambio decidido por la marca. Pasar de 60/40 a 65/35 sin reimprimir deja la etiqueta mal, por pequeño que parezca el desfase. La etiqueta de cuidado es el soporte permanente cosido a la prenda: es la que lee la inspección de mercado, mucho después de que la etiqueta colgante haya ido a la basura.",
        "ja": "許容範囲が設けられているのは、紡績の混綿、製織での糸ロス、仕上げでの重量変化など、誰も正確には制御できない工程のためです。ブランド自身が決めた変更は対象外です。60/40 を 65/35 に変えて表示を刷り直さなければ、差がどれほど小さく見えても表示は誤りです。洗濯表示ラベルは製品に縫い付けられた恒久的な媒体であり、下げ札が捨てられた後も市場監視当局が最初に読むものです。",
        "ko": "허용 오차는 방적 혼합, 제직 손실, 가공 중 중량 변화처럼 누구도 정확히 통제할 수 없는 공정을 위한 제도입니다. 브랜드가 스스로 한 변경은 대상이 아닙니다. 60/40을 65/35로 바꾸고 라벨을 다시 찍지 않으면 차이가 작아 보여도 표시는 틀린 것입니다. 관리 라벨은 의류에 봉제된 영구 부착물이라 행택이 버려진 뒤에도 시장 감독 당국이 가장 먼저 읽는 항목입니다.",
    }),
    ("h2", {
        "zh": "二、三個數字：3%、5%、整數",
        "en": "2. The Three Numbers: 3%, 5%, Whole Percent",
        "fr": "2. Les trois chiffres : 3 %, 5 %, pourcent entier",
        "es": "2. Las tres cifras: 3 %, 5 %, porcentaje entero",
        "ja": "2. 押さえるべき 3 つの数字：3 %・5 %・整数",
        "ko": "2. 세 가지 숫자: 3%·5%·정수",
    }),
    ("p", {
        "zh": "第一，歐盟法規 (EU) 1007/2011 要求以重量百分比標示纖維組成，執法實務上對製造上無法排除的纖維容許約 3% 的偏差；這條容差是為了不讓好工廠為難，不是讓你宣告另一種配方。第二，美國 16 CFR Part 303 允許含量低於 5% 的纖維以「其他纖維」統稱，這條留給微量雜質與裝飾纖維，不能用來藏掉決定功能的纖維。第三，所有市場都要求整數百分比，且相加必須等於 100。",
        "en": "First, Regulation (EU) No 1007/2011 requires the fibre composition as a percentage by weight, and enforcement practice accepts roughly 3% of variance for fibres that production cannot exclude. That allowance exists so a well-run mill is not punished for physics; it is not a licence to declare a different recipe. Second, 16 CFR Part 303 in the United States lets a fibre below 5% be disclosed as other fiber, which is intended for trace contamination and decorative yarns, not for the fibre that gives the garment its function. Third, every market wants whole percentages, and they must add up to 100.",
        "fr": "Premièrement, le règlement (UE) 1007/2011 impose la composition en pourcentage du poids, et la pratique de contrôle admet environ 3 % d'écart pour les fibres que la production ne peut exclure. Cette tolérance évite de sanctionner une filature bien tenue pour des raisons physiques ; ce n'est pas une autorisation de déclarer une autre recette. Deuxièmement, aux États-Unis, 16 CFR Part 303 permet de déclarer en autres fibres toute fibre inférieure à 5 %, ce qui vise les contaminations infimes et les fils décoratifs, pas la fibre qui fait la fonction du vêtement. Troisièmement, partout, les pourcentages sont entiers et leur somme doit faire 100.",
        "es": "Primero, el Reglamento (UE) 1007/2011 exige la composición en porcentaje de peso y la práctica de control admite alrededor del 3 % de desviación para fibras que la producción no puede excluir. Ese margen evita sancionar a una hilatura bien gestionada por razones físicas; no autoriza a declarar otra receta. Segundo, en EE. UU., 16 CFR Part 303 permite declarar como otras fibras cualquiera por debajo del 5 %, previsto para contaminaciones mínimas y hilos decorativos, no para la fibra que da función a la prenda. Tercero, en todos los mercados los porcentajes son enteros y deben sumar 100.",
        "ja": "第一に、(EU) 1007/2011 は混用率を重量パーセントで表示することを求めており、製造上排除できない繊維については実務上およそ 3 % のばらつきが許容されます。これは健全な紡績工場を物理現象で罰しないためのもので、別の配合を宣言する権利ではありません。第二に、米国の 16 CFR Part 303 は 5 % 未満の繊維を「その他繊維」として表示することを認めていますが、これは微量の混入や装飾糸のためのもので、機能を決める繊維を隠すためのものではありません。第三に、どの市場でも整数パーセントで、合計が 100 になる必要があります。",
        "ko": "첫째, (EU) 1007/2011은 혼용률을 중량 퍼센트로 표시하도록 요구하며, 생산 과정에서 배제할 수 없는 섬유에 대해 실무상 약 3%의 편차를 인정합니다. 이는 물리적 한계로 정상 공장을 처벌하지 않기 위한 것이지 다른 배합을 선언할 권리가 아닙니다. 둘째, 미국 16 CFR Part 303은 5% 미만 섬유를 '기타 섬유'로 표시할 수 있게 하지만, 이는 미량 혼입과 장식사에 해당하며 기능을 결정하는 섬유를 숨기는 수단이 아닙니다. 셋째, 모든 시장에서 정수 퍼센트로 표기하고 합계가 100이어야 합니다.",
    }),
    ("h2", {
        "zh": "三、一個實例：62/33/5 怎麼寫",
        "en": "3. A Worked Example: 62/33/5",
        "fr": "3. Un exemple concret : 62/33/5",
        "es": "3. Un ejemplo concreto: 62/33/5",
        "ja": "3. 実例：62/33/5 をどう書くか",
        "ko": "3. 실제 예시: 62/33/5를 어떻게 적을까",
    }),
    ("p", {
        "zh": "一件針織上衣測出 62% 棉、33% 聚酯纖維、5% 彈性纖維。正確寫法是三者全部列出：62% 棉 / 33% 聚酯纖維 / 5% 彈性纖維。即使規則允許，也不要把彈性纖維併進「其他纖維」——彈性是顧客買這件衣服的理由，把它藏進統稱，是把功能性資訊從消費者眼前拿走，這類省略最後常以「誤導性標示」的形式回到品牌手上。",
        "en": "A jersey measures 62% cotton, 33% polyester and 5% elastane. The correct label lists all three: 62% cotton, 33% polyester, 5% elastane. Even where the rule would allow it, do not fold the elastane into other fibre. Stretch is the reason the customer buys the garment; hiding it behind a general term removes functional information from the buyer, and omissions of this kind tend to come back as misleading-labelling complaints.",
        "fr": "Un jersey mesure 62 % coton, 33 % polyester et 5 % élasthanne. La bonne étiquette liste les trois : 62 % coton, 33 % polyester, 5 % élasthanne. Même lorsque la règle l'autorise, ne regroupez pas l'élasthanne en autres fibres. L'élasticité est la raison d'achat du vêtement ; la cacher derrière un terme générique prive l'acheteur d'une information fonctionnelle, et ce type d'omission revient souvent sous forme de plainte pour étiquetage trompeur.",
        "es": "Un punto mide 62 % algodón, 33 % poliéster y 5 % elastano. La etiqueta correcta enumera los tres: 62 % algodón, 33 % poliéster, 5 % elastano. Aunque la norma lo permita, no agrupe el elastano como otras fibras. La elasticidad es la razón por la que se compra la prenda; esconderla tras un término genérico priva al comprador de una información funcional, y esa omisión suele volver como reclamación por etiquetado engañoso.",
        "ja": "あるニットが綿 62 %、ポリエステル 33 %、ポリウレタン 5 % と測定されたとします。正しい表示は 3 つとも列記する形です。規則が認める場合でも、ポリウレタンを「その他繊維」にまとめてはいけません。伸縮性はこの製品を選ぶ理由であり、包括表記の裏に隠すことは機能情報を消費者から奪う行為です。こうした省略は最終的に「誤認表示」として返ってきます。",
        "ko": "한 니트가 면 62%, 폴리에스터 33%, 엘라스테인 5%로 측정되었습니다. 올바른 표기는 셋을 모두 적는 것입니다. 규정이 허용하더라도 엘라스테인을 '기타 섬유'로 묶지 마십시오. 신축성은 고객이 이 제품을 사는 이유이며, 포괄 표기 뒤에 숨기는 것은 기능 정보를 빼앗는 일입니다. 이런 누락은 결국 '오인 표시' 민원으로 돌아옵니다.",
    }),
    ("ul", [
        {
            "zh": "含量 ≥5% 的纖維必須單獨列出，不可合併。",
            "en": "Any fibre at or above 5% must be listed on its own and cannot be merged.",
            "fr": "Toute fibre à 5 % ou plus doit être listée séparément, sans regroupement.",
            "es": "Toda fibra del 5 % o más debe figurar por separado, sin agrupar.",
            "ja": "5 % 以上の繊維は単独で表示し、まとめてはいけません。",
            "ko": "5% 이상 섬유는 단독으로 표시해야 하며 묶을 수 없습니다.",
        },
        {
            "zh": "百分比相加必須等於 100，里布、填充與飾邊要另外列或註明不計入。",
            "en": "The percentages must total 100; lining, filling and trims are listed separately or excluded with a note.",
            "fr": "La somme doit faire 100 ; doublure, garnissage et accessoires sont listés à part ou exclus avec une mention.",
            "es": "Los porcentajes deben sumar 100; forro, relleno y adornos se listan aparte o se excluyen con una nota.",
            "ja": "合計は 100 にする。裏地・中綿・装飾は別記するか、除外する旨を明記します。",
            "ko": "합계는 100이어야 하며, 안감·충전재·장식은 별도로 적거나 제외 문구를 넣습니다.",
        },
        {
            "zh": "大貨重測若落在 58/36/6，這已經不是容差而是不同產品，必須重印標籤。",
            "en": "If the bulk re-test comes back at 58/36/6, that is no longer variance but a different product: reprint.",
            "fr": "Si le re-test de la production donne 58/36/6, ce n'est plus une tolérance mais un autre produit : réimprimez.",
            "es": "Si el reensayo de producción da 58/36/6, ya no es tolerancia sino otro producto: reimprima.",
            "ja": "量産の再試験が 58/36/6 なら、もはや許容範囲ではなく別製品です。表示を刷り直します。",
            "ko": "양산 재시험이 58/36/6이라면 허용 오차가 아니라 다른 제품이므로 라벨을 다시 찍어야 합니다.",
        },
    ]),
    ("h2", {
        "zh": "四、逐市場：法源、語言與容差怎麼處理",
        "en": "4. Market by Market: Legal Basis, Language, Tolerance",
        "fr": "4. Marché par marché : base légale, langue, tolérance",
        "es": "4. Mercado por mercado: base legal, idioma y tolerancia",
        "ja": "4. 市場別：根拠法・言語・許容の扱い",
        "ko": "4. 시장별: 근거 법규·언어·허용 오차 처리",
    }),
    ("table", (
        [
            {"zh": "市場", "en": "Market", "fr": "Marché", "es": "Mercado", "ja": "市場", "ko": "시장"},
            {"zh": "法源與語言", "en": "Legal basis and language", "fr": "Base légale et langue", "es": "Base legal e idioma", "ja": "根拠法と言語", "ko": "근거 법규와 언어"},
            {"zh": "容差怎麼處理", "en": "How tolerance is handled", "fr": "Traitement de la tolérance", "es": "Cómo se trata la tolerancia", "ja": "許容の扱い", "ko": "허용 오차 처리"},
        ],
        [
            [
                {"zh": "歐盟", "en": "European Union", "fr": "Union européenne", "es": "Unión Europea", "ja": "EU", "ko": "EU"},
                {"zh": "(EU) 1007/2011；成員國語言，另需 GPSR 責任方", "en": "(EU) 1007/2011; member-state language; GPSR responsible person also required", "fr": "règlement (UE) 1007/2011 ; langue de l'État membre ; responsable GPSR", "es": "Reglamento (UE) 1007/2011; idioma del Estado miembro; responsable GPSR", "ja": "(EU) 1007/2011、加盟国語、GPSR の責任事業者", "ko": "(EU) 1007/2011, 회원국 언어, GPSR 책임자"},
                {"zh": "約 3% 製造偏差可接受，且非標註纖維不得構成另一種配方", "en": "Around 3% manufacturing variance accepted; undeclared fibre must not amount to another recipe", "fr": "Environ 3 % d'écart de fabrication admis ; la fibre non déclarée ne doit pas constituer une autre recette", "es": "Se admite en torno al 3 % de variación de fabricación; la fibra no declarada no puede constituir otra receta", "ja": "製造ばらつきは約 3 % まで許容。ただし未表示繊維が別配合と言える量になってはいけません", "ko": "제조 편차 약 3% 허용. 다만 미표시 섬유가 다른 배합 수준이면 안 됩니다"},
            ],
            [
                {"zh": "美國", "en": "United States", "fr": "États-Unis", "es": "Estados Unidos", "ja": "米国", "ko": "미국"},
                {"zh": "16 CFR Part 303；英文，另需 16 CFR Part 423 洗護指示", "en": "16 CFR Part 303; English; 16 CFR Part 423 care instructions also required", "fr": "16 CFR Part 303 ; anglais ; instructions d'entretien 16 CFR Part 423", "es": "16 CFR Part 303; inglés; instrucciones de cuidado 16 CFR Part 423", "ja": "16 CFR Part 303、英語、16 CFR Part 423 の取扱い指示", "ko": "16 CFR Part 303, 영어, 16 CFR Part 423 취급 지침"},
                {"zh": "5% 以下可寫「其他纖維」，但功能纖維不可藏", "en": "Under 5% may be other fiber, but functional fibres cannot be hidden", "fr": "Moins de 5 % peut être autres fibres, sauf fibre fonctionnelle", "es": "Menos del 5 % puede ser otras fibras, salvo fibra funcional", "ja": "5 % 未満は「その他繊維」可。ただし機能繊維は隠せません", "ko": "5% 미만은 '기타 섬유' 가능하나 기능성 섬유는 숨길 수 없음"},
            ],
            [
                {"zh": "日本", "en": "Japan", "fr": "Japon", "es": "Japón", "ja": "日本", "ko": "일본"},
                {"zh": "家庭用品品質表示法；日語；混用率與洗濯表示（JIS L 0001）", "en": "家庭用品品質表示法 (Household Goods Quality Labeling Act); Japanese; mix ratio and care symbols to JIS L 0001", "fr": "家庭用品品質表示法 (loi japonaise) ; japonais ; taux de mélange et symboles JIS L 0001", "es": "家庭用品品質表示法 (ley japonesa); japonés; porcentaje de mezcla y símbolos JIS L 0001", "ja": "家庭用品品質表示法、日本語、混用率と洗濯表示（JIS L 0001）", "ko": "家庭用品品質表示法(일본), 일본어, 혼용률과 JIS L 0001 취급 기호"},
                {"zh": "以試驗值判定，混用率誤差超出測量範圍即屬表示不符", "en": "Judged against the measured value; a gap beyond measurement scatter is a labelling failure", "fr": "Jugé sur la valeur mesurée ; un écart au-delà de la dispersion de mesure est un défaut", "es": "Se juzga contra el valor medido; una diferencia más allá de la dispersión es un defecto", "ja": "試験値との比較で判定。測定ばらつきを超える差は表示不適合", "ko": "시험값과 비교해 판정. 측정 오차를 넘는 차이는 표시 부적합"},
            ],
            [
                {"zh": "韓國", "en": "Korea", "fr": "Corée", "es": "Corea", "ja": "韓国", "ko": "한국"},
                {"zh": "품질경영 및 공산품안전관리법；韓語；混用率、取扱表示、原產地", "en": "품질경영 및 공산품안전관리법; Korean; mix ratio, care symbols, origin", "fr": "품질경영 및 공산품안전관리법 ; coréen ; composition, symboles, origine", "es": "품질경영 및 공산품안전관리법; coreano; composición, símbolos, origen", "ja": "품질경영 및 공산품안전관리법、韓国語、混用率・取扱表示・原産地", "ko": "품질경영 및 공산품안전관리법, 한국어, 혼용률·취급 표시·원산지"},
                {"zh": "進口商須能提供試驗報告，標示值須與報告一致", "en": "The importer must hold test reports and the label must match them", "fr": "L'importateur doit détenir les rapports d'essai, cohérents avec l'étiquette", "es": "El importador debe disponer de informes de ensayo coherentes con la etiqueta", "ja": "輸入者が試験報告を保管し、表示と一致している必要あり", "ko": "수입자가 시험 성적서를 보유하고 표시와 일치해야 함"},
            ],
        ],
    )),
    ("p", {
        "zh": "同一件衣服賣到四個市場，通常需要兩種語言的洗水標加一張雙面標：一面歐盟法規文字加 GPSR 責任方，一面日韓文字。這時標籤寬度是硬約束——常見的 2 cm 與 3 cm 緞帶，2 cm 只排得下三行字加一排洗護符號，四種纖維加兩種語言的法定文字往往要 3 cm 或改用折疊標。排不下就別擠，把字高壓到 1.5 mm 以下，門店和消費者都讀不清。",
        "en": "One garment sold into four markets usually needs care labels in two languages plus a folded label: one face for the EU wording with the GPSR responsible person, one face for Japanese and Korean. Label width then becomes a hard constraint. On the common 2 cm and 3 cm tapes, 2 cm holds about three lines plus one row of care symbols; four fibres in two languages generally needs 3 cm or a folded label. Do not squeeze it: below roughly 1.5 mm cap height neither a store assistant nor a customer can read it.",
        "fr": "Un vêtement vendu sur quatre marchés demande en général des étiquettes en deux langues, souvent sous forme d'étiquette pliée : une face pour les mentions UE avec le responsable GPSR, une face pour le japonais et le coréen. La largeur devient alors une contrainte dure. Sur les rubans courants de 2 cm et 3 cm, 2 cm tient environ trois lignes plus une rangée de symboles ; quatre fibres en deux langues exigent 3 cm ou une étiquette pliée. Ne comprimez pas : sous environ 1,5 mm de hauteur de capitale, personne ne lit.",
        "es": "Una prenda vendida en cuatro mercados suele necesitar etiquetas en dos idiomas, a menudo plegadas: una cara con el texto UE y el responsable GPSR, otra con japonés y coreano. El ancho pasa a ser un límite duro. En las cintas habituales de 2 cm y 3 cm, 2 cm admite unas tres líneas más una fila de símbolos; cuatro fibras en dos idiomas piden 3 cm o etiqueta plegada. No lo comprima: por debajo de unos 1,5 mm de altura de mayúscula nadie lo lee.",
        "ja": "1 着を 4 市場で売る場合、多くの場合 2 言語の洗濯表示に折り返しラベルを組み合わせます。片面に EU 表示と GPSR 責任事業者、もう片面に日本語と韓国語です。ここで幅が厳しい制約になります。一般的な 2 cm と 3 cm のテープでは、2 cm に収まるのは 3 行程度と記号 1 列。4 繊維を 2 言語で載せるなら 3 cm か折り返しラベルが必要です。無理に詰めると文字高が 1.5 mm を下回り、誰も読めません。",
        "ko": "한 제품을 네 개 시장에 팔면 보통 두 언어의 관리 라벨과 접이 라벨이 필요합니다. 한 면에는 EU 문구와 GPSR 책임자, 다른 면에는 일본어와 한국어를 넣습니다. 이때 폭이 결정적 제약이 됩니다. 흔한 2 cm와 3 cm 테이프에서 2 cm에는 세 줄과 기호 한 줄이 한계이며, 네 가지 섬유를 두 언어로 담으려면 3 cm나 접이 라벨이 필요합니다. 글자 높이를 1.5 mm 아래로 눌러 넣으면 아무도 읽지 못합니다.",
    }),
    ("h2", {
        "zh": "五、實驗室怎麼測，為什麼會差一到兩個百分點",
        "en": "5. How the Lab Tests, and Why Results Drift One or Two Points",
        "fr": "5. Comment le laboratoire mesure, et pourquoi l'écart atteint 1 à 2 points",
        "es": "5. Cómo mide el laboratorio y por qué varía uno o dos puntos",
        "ja": "5. 試験室の測り方と、1〜2 ポイントずれる理由",
        "ko": "5. 시험실 측정 방식과 1~2포인트 차이가 나는 이유",
    }),
    ("p", {
        "zh": "纖維定量最常用的是化學溶解法：ISO 1833 系列逐種溶掉纖維再稱重，美國常用 AATCC 20A，日本對應 JIS L 1030，韓國對應 KS K 0210。取樣面積通常是 10 cm × 4 cm 的小塊，布重 180 g/m² 的針織與 320 g/m² 的衛衣取到的纖維量差別很大，這也是小樣與大貨結果不同的原因之一。實務判斷：先在開發樣上定標，再用大貨批次複測，兩次都過才印標。",
        "en": "Quantitative fibre analysis is mostly chemical dissolution: the ISO 1833 series dissolves one fibre at a time and weighs what is left. The United States works to AATCC 20A, Japan to JIS L 1030, Korea to KS K 0210. A specimen is typically a 10 cm × 4 cm piece, so a 180 g/m² jersey and a 320 g/m² sweatshirt yield very different amounts of fibre — one reason a development sample and a bulk lot disagree. The practical sequence is to fix the claim on the development sample, re-test the bulk lot, and only print when both agree.",
        "fr": "L'analyse quantitative des fibres est surtout une dissolution chimique : la série ISO 1833 dissout une fibre à la fois et pèse le reste. Les États-Unis travaillent selon AATCC 20A, le Japon selon JIS L 1030, la Corée selon KS K 0210. L'éprouvette fait typiquement 10 cm × 4 cm : un jersey de 180 g/m² et un sweat de 320 g/m² ne livrent donc pas la même masse de fibre, ce qui explique en partie l'écart entre échantillon de développement et lot de production. La séquence fiable : figer la mention sur l'échantillon, re-tester le lot, puis imprimer.",
        "es": "El análisis cuantitativo de fibras es sobre todo disolución química: la serie ISO 1833 disuelve una fibra cada vez y pesa el resto. En EE. UU. se trabaja con AATCC 20A, en Japón con JIS L 1030, en Corea con KS K 0210. La probeta suele ser de 10 cm × 4 cm, así que un punto de 180 g/m² y una sudadera de 320 g/m² no aportan la misma masa de fibra: una razón de que la muestra de desarrollo y el lote de producción discrepen. La secuencia fiable es fijar la mención en la muestra, reensayar el lote y solo entonces imprimir.",
        "ja": "繊維の定量は主に化学溶解法です。ISO 1833 シリーズは繊維を 1 種類ずつ溶かして残量を量ります。米国は AATCC 20A、日本は JIS L 1030、韓国は KS K 0210 を用います。試験片は通常 10 cm × 4 cm で、180 g/m² の天竺と 320 g/m² のスウェットでは得られる繊維量が大きく異なります。開発サンプルと量産ロットの結果がずれる理由の 1 つです。実務手順は、開発サンプルで表示を固め、量産ロットで再試験し、両方が一致してから印刷することです。",
        "ko": "섬유 정량은 주로 화학 용해법입니다. ISO 1833 시리즈는 섬유를 하나씩 용해하고 남은 양을 측정합니다. 미국은 AATCC 20A, 일본은 JIS L 1030, 한국은 KS K 0210을 사용합니다. 시험편은 보통 10 cm × 4 cm이며, 180 g/m² 저지와 320 g/m² 맨투맨은 얻어지는 섬유량이 크게 다릅니다. 개발 샘플과 양산 로트 결과가 어긋나는 이유 중 하나입니다. 실무 순서는 개발 샘플에서 표기를 확정하고, 양산 로트로 재시험한 뒤 두 값이 맞을 때 인쇄하는 것입니다.",
    }),
    ("callout", {
        "zh": "三條能省下一次重印的習慣：① 換紗線供應商、換染廠、換織造廠，就算配方沒變也要重測一次；② 把測試報告、標籤稿與大貨批號存在同一個檔案夾，監管來問時五分鐘就能拿出；③ 標籤稿上寫明「萬一重測不符，重印費用由誰承擔」，這一句在報價階段談比在扣款單來時談有用。",
        "en": "Three habits that save a reprint. Re-test whenever the yarn supplier, dyehouse or knitting mill changes, even if the recipe did not. Keep the test report, the label artwork and the bulk lot number in one folder so a surveillance request takes five minutes. And settle in writing who pays for a reprint if the bulk re-test disagrees — that clause is cheaper to agree at quotation stage than after a debit note arrives.",
        "fr": "Trois habitudes qui évitent une réimpression. Re-tester à chaque changement de filature, de teinturerie ou de tricotage, même à recette identique. Conserver rapport d'essai, maquette d'étiquette et numéro de lot dans un seul dossier, pour répondre en cinq minutes à un contrôle. Et écrire qui paie la réimpression si le re-test du lot diverge : cette clause se négocie mieux au devis qu'après une note de débit.",
        "es": "Tres hábitos que ahorran una reimpresión. Reensayar cada vez que cambie el proveedor de hilo, la tintorería o el taller de tejido, aunque la receta sea la misma. Guardar informe, arte de etiqueta y número de lote en una sola carpeta, para responder en cinco minutos a una inspección. Y dejar por escrito quién paga la reimpresión si el reensayo del lote discrepa: esa cláusula se negocia mejor en el presupuesto que tras un cargo.",
        "ja": "刷り直しを 1 回減らす 3 つの習慣。糸の仕入先・染色工場・編立工場が変わったら、配合が同じでも再試験する。試験報告・表示ラベルの版・量産ロット番号を同じフォルダにまとめ、監査時に 5 分で出せるようにする。そして、量産の再試験が合わなかった場合の刷り直し費用の負担者を見積段階で文書化しておく。請求減額の後で話すより安く済みます。",
        "ko": "재인쇄 한 번을 아끼는 세 가지 습관. 원사 공급사, 염색 공장, 편직 공장이 바뀌면 배합이 같아도 다시 시험합니다. 시험 성적서, 라벨 시안, 양산 로트 번호를 한 폴더에 모아 감독 요청에 5분 안에 대응합니다. 그리고 양산 재시험이 어긋날 때 재인쇄 비용을 누가 부담하는지 견적 단계에서 문서로 정합니다. 차감 통보 후에 협의하는 것보다 훨씬 저렴합니다.",
    }),
    ("h2", {
        "zh": "六、印前五項檢查",
        "en": "6. Five Checks Before You Print",
        "fr": "6. Cinq vérifications avant impression",
        "es": "6. Cinco comprobaciones antes de imprimir",
        "ja": "6. 印刷前の 5 項目チェック",
        "ko": "6. 인쇄 전 다섯 가지 점검",
    }),
    ("ul", [
        {
            "zh": "標示值是否與最新一份大貨測試報告一致（不是開發樣報告）。",
            "en": "Does the stated value match the latest bulk report rather than the development sample?",
            "fr": "La valeur annoncée correspond-elle au dernier rapport de production, pas à l'échantillon ?",
            "es": "¿El valor declarado coincide con el último informe de producción y no con la muestra?",
            "ja": "表示値は開発サンプルではなく最新の量産試験報告と一致していますか。",
            "ko": "표시값이 개발 샘플이 아니라 최신 양산 시험 성적서와 일치합니까?",
        },
        {
            "zh": "百分比相加是否為 100，里布與填充是否另行標示。",
            "en": "Do the percentages total 100, and are lining and filling declared separately?",
            "fr": "La somme fait-elle 100, et doublure et garnissage sont-ils déclarés à part ?",
            "es": "¿Suman 100 y están forro y relleno declarados aparte?",
            "ja": "合計は 100 で、裏地と中綿は別記されていますか。",
            "ko": "합계가 100이며 안감과 충전재가 별도로 표시되어 있습니까?",
        },
        {
            "zh": "目標市場的語言、單位與法定項目是否齊全（GPSR 責任方、原產地、取扱表示）。",
            "en": "Are language, units and mandatory items complete for each target market, including the GPSR responsible person and origin?",
            "fr": "Langue, unités et mentions obligatoires sont-elles complètes par marché, responsable GPSR et origine compris ?",
            "es": "¿Están completos idioma, unidades y menciones por mercado, incluido el responsable GPSR y el origen?",
            "ja": "市場ごとの言語・単位・法定項目（GPSR 責任事業者、原産地、取扱表示）は揃っていますか。",
            "ko": "시장별 언어, 단위, 법정 항목(GPSR 책임자, 원산지, 취급 표시)이 모두 갖추어졌습니까?",
        },
    ]),
    ("related", [
        ("care-label-fabric-content.html", {
            "zh": "洗水標纖維成分怎麼寫", "en": "How to write care label fibre content",
            "fr": "Rédiger la composition d'une étiquette", "es": "Redactar la composición de la etiqueta",
            "ja": "洗濯表示の混用率の書き方", "ko": "세탁 표시 혼용률 표기법",
        }),
        ("care-label-standards.html", {
            "zh": "洗水標要符合哪些標準", "en": "Which standards a care label must meet",
            "fr": "Les normes applicables à l'étiquette d'entretien", "es": "Normas que debe cumplir la etiqueta",
            "ja": "洗濯表示が満たすべき基準", "ko": "관리 라벨이 충족해야 할 기준",
        }),
        ("trim-third-party-testing-guide.html", {
            "zh": "輔料第三方測試怎麼安排", "en": "How to arrange third-party trim testing",
            "fr": "Organiser les essais tiers sur accessoires", "es": "Cómo organizar ensayos de terceros",
            "ja": "副資材の第三者試験の進め方", "ko": "부자재 제3자 시험 진행 방법",
        }),
    ]),
    ("cta", (
        {
            "zh": "把目標市場、現有標籤稿與最近一份測試報告寄給我們，我們回一份逐市場的標示對照：成分寫法、容差風險點、標籤寬度與折法，以及需要重測的項目。",
            "en": "Send the target markets, the current label artwork and the latest test report; we return a per-market table covering composition wording, tolerance risk, label width and fold, and what needs re-testing.",
            "fr": "Envoyez les marchés visés, la maquette actuelle et le dernier rapport d'essai : nous renvoyons un tableau par marché (formulation, risque de tolérance, largeur et pliage, essais à refaire).",
            "es": "Envíe los mercados de destino, el arte actual y el último informe de ensayo: devolvemos una tabla por mercado con redacción, riesgo de tolerancia, ancho y plegado, y ensayos pendientes.",
            "ja": "対象市場・現行の表示ラベル版・最新の試験報告をお送りください。市場別に、混用率の書き方、許容リスク、ラベル幅と折り、再試験項目をまとめてお返しします。",
            "ko": "대상 시장, 현재 라벨 시안, 최신 시험 성적서를 보내주세요. 시장별로 혼용률 표기, 허용 오차 위험, 라벨 폭과 접힘, 재시험 항목을 정리해 회신합니다.",
        },
        {
            "zh": "索取標示對照與報價 →", "en": "Request a labelling review and quote →",
            "fr": "Demander une revue d'étiquetage et un devis →", "es": "Solicitar revisión de etiquetado y presupuesto →",
            "ja": "表示レビューとお見積りを依頼 →", "ko": "표시 검토와 견적 요청 →",
        },
    )),
]
