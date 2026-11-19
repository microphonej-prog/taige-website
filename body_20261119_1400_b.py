# -*- coding: utf-8 -*-
"""2026-11-19 14:00 批次 B：天然纖維洗水標（wool / silk / cashmere / linen care labels）"""

SLUG = "natural-fiber-care-label-guide"
CATEGORY = {
    "zh": "洗水標與合規", "en": "Care Labels & Compliance", "fr": "Étiquettes & conformité",
    "es": "Etiquetas y normativa", "ja": "洗濯表示・法令", "ko": "세탁 표시·규정",
}
TITLE = {
    "zh": "羊毛、蠶絲、喀什米爾、亞麻的洗水標怎麼寫 | TAGE",
    "en": "Care Labels for Wool, Silk, Cashmere and Linen | TAGE",
    "fr": "Étiquettes d'entretien : laine, soie, cachemire, lin | TAGE",
    "es": "Etiquetas de cuidado: lana, seda, cachemir y lino | TAGE",
    "ja": "ウール・シルク・カシミヤ・リネンの洗濯表示 | TAGE",
    "ko": "울·실크·캐시미어·리넨 세탁 표시 라벨 | TAGE",
}
DESC = {
    "zh": "天然纖維洗水標怎麼寫：四種纖維的洗滌溫度與乾洗代號、ISO 3758 符號順序、混紡成分允差與 5% 規則、三次洗滌後的縮率驗收，附標材與字高。",
    "en": "How to write care labels for wool, silk, cashmere and linen: wash temperatures, ISO 3758 symbol order, blend tolerances and shrinkage limits after three washes.",
    "fr": "Rédiger les étiquettes d'entretien laine, soie, cachemire et lin : températures, ordre des symboles ISO 3758, tolérances de mélange et retrait après trois lavages.",
    "es": "Cómo redactar etiquetas de cuidado de lana, seda, cachemir y lino: temperaturas, orden de símbolos ISO 3758, tolerancias de mezcla y encogimiento tras tres lavados.",
    "ja": "ウール・シルク・カシミヤ・リネンの洗濯表示の書き方。洗濯温度、ISO 3758 の記号順序、混用率の許容差、3 回洗濯後の収縮許容まで整理します。",
    "ko": "울·실크·캐시미어·리넨 세탁 표시 작성법. 세탁 온도, ISO 3758 기호 순서, 혼용률 허용차, 3회 세탁 후 수축 허용 범위까지 정리합니다.",
}
H1 = {
    "zh": "天然纖維洗水標：羊毛、蠶絲、喀什米爾與亞麻",
    "en": "Care Labels for Wool, Silk, Cashmere and Linen",
    "fr": "Étiquettes d'entretien : laine, soie, cachemire et lin",
    "es": "Etiquetas de cuidado: lana, seda, cachemir y lino",
    "ja": "天然繊維の洗濯表示：ウール・シルク・カシミヤ・リネン",
    "ko": "천연 섬유 세탁 표시: 울·실크·캐시미어·리넨",
}

BLOCKS = [
    ("p", {
        "zh": "天然纖維的洗水標，是全站最容易被「通用模板」害到的一類：同樣寫「30 ℃ 輕柔洗、不可漂白、低溫熨燙」，放在棉 T 上完全正確，放在羊毛衫上就是把一件售價四位數的衣服送進縮水與氈化的流程。本篇按四種纖維（羊毛、蠶絲、喀什米爾、亞麻）給出各自的洗護底線、ISO 3758 符號的落法、混紡成分允差與可量化的驗收標準，最後講標材與字高——因為符號寫對了但沒人看得清，等於白寫。",
        "en": "Care labels for natural fibres are the category most often damaged by a generic template. The same line — machine wash 30 °C gentle, do not bleach, low iron — is correct on a cotton tee and ruinous on a wool sweater, sending a four-figure garment straight into shrinkage and felting. This guide sets the care floor for wool, silk, cashmere and linen, shows how ISO 3758 symbols land on the label, covers blend tolerances and measurable acceptance, and closes with label material and type height, because symbols nobody can read are symbols that do not exist.",
        "fr": "Les étiquettes d'entretien des fibres naturelles sont la catégorie que les modèles génériques abîment le plus. La même ligne — lavage machine 30 °C délicat, pas de blanchiment, repassage doux — est juste sur un tee-shirt de coton et destructrice sur une maille de laine : elle envoie une pièce à quatre chiffres droit vers le feutrage. Cet article fixe le plancher d'entretien de la laine, de la soie, du cachemire et du lin, montre comment les symboles ISO 3758 se posent sur l'étiquette, traite les tolérances de mélange et la réception mesurable, puis le support et la hauteur de caractères — un symbole illisible n'existe pas.",
        "es": "Las etiquetas de cuidado de fibras naturales son la categoría que más daño recibe de una plantilla genérica. La misma línea — lavado a máquina 30 °C suave, no blanquear, plancha baja — es correcta en una camiseta de algodón y destructiva en un suéter de lana: manda una prenda de cuatro cifras directa al afieltrado. Esta guía fija el mínimo de cuidado de lana, seda, cachemir y lino, explica cómo se colocan los símbolos ISO 3758, cubre tolerancias de mezcla y recepción medible, y cierra con el material de la etiqueta y la altura de letra, porque un símbolo ilegible no existe.",
        "ja": "天然繊維の洗濯表示は、汎用テンプレートの被害が最も大きい分野です。「30 ℃ 弱い洗濯、漂白不可、低温アイロン」という同じ一行が、綿 T シャツでは正しく、ウールのセーターでは四位の価格の製品を収縮とフェルト化へ直行させます。本稿はウール・シルク・カシミヤ・リネンの最低限のケア基準、ISO 3758 記号の入れ方、混用率の許容差、数値で判定できる受入、そしてラベルの素材と文字高までを整理します。読めない記号は存在しないのと同じだからです。",
        "ko": "천연 섬유 세탁 표시는 범용 템플릿에 가장 크게 다치는 분류입니다. '30 ℃ 약한 세탁, 표백 금지, 저온 다림질'이라는 같은 한 줄이 면 티셔츠에는 맞고 울 스웨터에는 네 자리 가격의 제품을 수축과 펠트화로 몰아넣습니다. 이 글은 울·실크·캐시미어·리넨의 최소 관리 기준, ISO 3758 기호 표기 방식, 혼용률 허용차, 수치로 판정하는 검사 기준을 정리하고, 마지막으로 라벨 소재와 글자 높이를 다룹니다. 읽을 수 없는 기호는 없는 기호이기 때문입니다.",
    }),

    ("h2", {
        "zh": "一、四種纖維的洗護底線",
        "en": "1. The Care Floor for Four Fibres",
        "fr": "1. Le plancher d'entretien des quatre fibres",
        "es": "1. El mínimo de cuidado de cuatro fibras",
        "ja": "1. 4 つの繊維の最低限のケア基準",
        "ko": "1. 네 가지 섬유의 최소 관리 기준",
    }),

    ("table", (
        [
            {"zh": "纖維", "en": "Fibre", "fr": "Fibre", "es": "Fibra", "ja": "繊維", "ko": "섬유"},
            {"zh": "洗滌上限", "en": "Wash limit", "fr": "Limite de lavage", "es": "Límite de lavado", "ja": "洗濯の上限", "ko": "세탁 상한"},
            {"zh": "乾洗代號", "en": "Dry-clean code", "fr": "Code nettoyage à sec", "es": "Código de limpieza en seco", "ja": "ドライ表示", "ko": "드라이 표시"},
            {"zh": "主要風險", "en": "Main risk", "fr": "Risque principal", "es": "Riesgo principal", "ja": "主なリスク", "ko": "주요 리스크"},
        ],
        [
            [
                {"zh": "羊毛 / 美麗諾", "en": "Wool, merino", "fr": "Laine, mérinos", "es": "Lana, merino", "ja": "ウール・メリノ", "ko": "울·메리노"},
                {"zh": "30 ℃ 羊毛程序或手洗", "en": "30 °C wool cycle or hand wash", "fr": "30 °C cycle laine ou à la main", "es": "30 °C ciclo lana o a mano", "ja": "30 ℃ ウールコースまたは手洗い", "ko": "30 ℃ 울 코스 또는 손세탁"},
                {"zh": "P（四氯乙烯）", "en": "P (perchloroethylene)", "fr": "P (perchloroéthylène)", "es": "P (percloroetileno)", "ja": "P（パークロロエチレン）", "ko": "P(퍼클로로에틸렌)"},
                {"zh": "氈化、起球、肩部變形", "en": "Felting, pilling, shoulder distortion", "fr": "Feutrage, bouloches, épaules déformées", "es": "Afieltrado, bolitas, hombros deformados", "ja": "フェルト化・毛玉・肩の型崩れ", "ko": "펠트화, 보풀, 어깨 변형"},
            ],
            [
                {"zh": "蠶絲 / 桑蠶絲", "en": "Silk, mulberry", "fr": "Soie, mûrier", "es": "Seda, morera", "ja": "シルク・桑蚕", "ko": "실크·멀버리"},
                {"zh": "手洗 30 ℃，不可擰", "en": "Hand wash 30 °C, do not wring", "fr": "Main 30 °C, ne pas essorer", "es": "A mano 30 °C, no retorcer", "ja": "30 ℃ 手洗い、絞らない", "ko": "30 ℃ 손세탁, 짜지 않기"},
                {"zh": "P 或 F（石油溶劑）", "en": "P or F (petroleum solvent)", "fr": "P ou F (solvant pétrolier)", "es": "P o F (disolvente mineral)", "ja": "P または F（石油系）", "ko": "P 또는 F(석유계)"},
                {"zh": "水痕、光澤受損、緯向滑移", "en": "Water marks, loss of lustre, seam slippage", "fr": "Traces d'eau, lustre perdu, glissement de couture", "es": "Marcas de agua, pérdida de brillo, deslizamiento", "ja": "水ジミ・光沢低下・目ずれ", "ko": "물얼룩, 광택 손상, 실밥 벌어짐"},
            ],
            [
                {"zh": "喀什米爾 / 羊絨", "en": "Cashmere", "fr": "Cachemire", "es": "Cachemir", "ja": "カシミヤ", "ko": "캐시미어"},
                {"zh": "手洗 30 ℃，平攤陰乾", "en": "Hand wash 30 °C, dry flat in shade", "fr": "Main 30 °C, séchage à plat à l'ombre", "es": "A mano 30 °C, secar en plano a la sombra", "ja": "30 ℃ 手洗い、平干し陰干し", "ko": "30 ℃ 손세탁, 평평하게 그늘 건조"},
                {"zh": "P", "en": "P", "fr": "P", "es": "P", "ja": "P", "ko": "P"},
                {"zh": "纖維遷移、拉長、起球", "en": "Fibre migration, stretching, pilling", "fr": "Migration de fibres, étirement, bouloches", "es": "Migración de fibra, estiramiento, bolitas", "ja": "繊維移動・伸び・毛玉", "ko": "섬유 이동, 늘어남, 보풀"},
            ],
            [
                {"zh": "亞麻 / 麻混紡", "en": "Linen and linen blends", "fr": "Lin et mélanges", "es": "Lino y mezclas", "ja": "リネン・混紡", "ko": "리넨·혼방"},
                {"zh": "40 ℃ 一般程序（未經防縮處理者 30 ℃）", "en": "40 °C normal, or 30 °C if not pre-shrunk", "fr": "40 °C normal, ou 30 °C sans prétraitement", "es": "40 °C normal, o 30 °C sin preencogido", "ja": "40 ℃ 標準、防縮加工なしは 30 ℃", "ko": "40 ℃ 일반, 방축 가공 없으면 30 ℃"},
                {"zh": "F 或可水洗（視後整理）", "en": "F, or washable depending on finish", "fr": "F, ou lavable selon la finition", "es": "F, o lavable según acabado", "ja": "F、仕上げにより水洗い可", "ko": "F, 가공에 따라 세탁 가능"},
                {"zh": "初次縮水 3–5%、折痕處發白", "en": "First-wash shrinkage 3–5%, white lines on creases", "fr": "Retrait 3–5 % au premier lavage, plis qui blanchissent", "es": "Encogimiento 3–5 % al primer lavado, pliegues blanquecinos", "ja": "初回 3〜5 % 収縮、折り目が白化", "ko": "첫 세탁 3~5% 수축, 접힌 선 백화"},
            ],
        ],
    )),

    ("p", {
        "zh": "這張表最容易被違反的一行是羊毛。工廠照棉的程序寫「30 ℃ 輕柔」，但羊毛需要的不是低溫，而是低機械作用：水量要多、脫水要慢、不能與其他衣物摩擦。實務上把羊毛程序寫成「30 ℃ 羊毛程序，400 轉以下脫水，平攤乾燥」，退貨率會明顯下降；如果供應商無法保證機洗，就老實寫手洗，不要用「可機洗」換一時的賣點。",
        "en": "The line most often broken in that table is wool. Factories write 30 °C gentle because that is the cotton answer, but wool needs low mechanical action more than low temperature: plenty of water, a slow spin, and no rubbing against other garments. Write it as 30 °C wool cycle, spin at 400 rpm or less, dry flat, and returns drop noticeably. If the mill cannot guarantee machine washing, say hand wash — do not trade a claim for a feature.",
        "fr": "La ligne la plus souvent violée est celle de la laine. Les usines écrivent 30 °C délicat parce que c'est la réponse coton, alors que la laine a surtout besoin d'une action mécanique faible : beaucoup d'eau, un essorage lent, aucun frottement contre d'autres pièces. Écrivez 30 °C cycle laine, essorage à 400 tr/min maximum, séchage à plat : les retours baissent nettement. Si le moulin ne peut pas garantir le lavage machine, indiquez main — n'échangez pas une allégation contre un argument de vente.",
        "es": "La línea que más se incumple es la de la lana. Las fábricas escriben 30 °C suave porque es la respuesta del algodón, pero la lana necesita acción mecánica baja más que temperatura baja: mucha agua, centrifugado lento y ningún roce con otras prendas. Escríbelo como 30 °C ciclo lana, centrifugado a 400 rpm o menos, secado en plano, y las devoluciones bajan de forma visible. Si el proveedor no puede garantizar lavado a máquina, indique a mano: no cambies una alegación por un argumento de venta.",
        "ja": "この表で最も破られやすいのがウールの行です。工場は綿の答えである「30 ℃ 弱い洗濯」と書きますが、ウールに必要なのは低温より低い機械作用です。水量を多く、脱水は低速、他の衣類との摩擦なし。実務では「30 ℃ ウールコース、脱水 400 回転以下、平干し」と書き、返品率が明確に下がります。機洗いを保証できないなら手洗いと明記し、「洗濯機で洗える」という訴求と引き換えにしないことです。",
        "ko": "이 표에서 가장 자주 위반되는 줄이 울입니다. 공장은 면의 답인 '30 ℃ 약한 세탁'을 적지만, 울에 필요한 것은 낮은 온도보다 낮은 기계 작용입니다. 물은 넉넉히, 탈수는 저속으로, 다른 의류와 마찰 없이. 실무에서는 '30 ℃ 울 코스, 탈수 400 rpm 이하, 평평하게 건조'로 적으면 반품률이 뚜렷이 내려갑니다. 공급사가 기계 세탁을 보장할 수 없다면 손세탁으로 정직하게 적으세요. 세탁기 세탁이라는 판매 포인트와 바꾸지 마세요.",
    }),

    ("h2", {
        "zh": "二、ISO 3758 符號怎麼落到標上",
        "en": "2. Putting ISO 3758 Symbols on the Label",
        "fr": "2. Poser les symboles ISO 3758 sur l'étiquette",
        "es": "2. Colocar los símbolos ISO 3758 en la etiqueta",
        "ja": "2. ISO 3758 の記号をラベルに落とす",
        "ko": "2. ISO 3758 기호를 라벨에 넣는 방법",
    }),

    ("p", {
        "zh": "ISO 3758 的體系是以洗滌槽為核心的五個符號：洗滌、漂白、乾燥、熨燙、專業乾洗，順序固定，最後一個符號代表最嚴格的限制。台灣與中國市場的 GB/T 8685 與日本 JIS L 0001 與 ISO 3758 基本相容，但日本的洗濯表示在 2016 年改版後改用新的五符號體系，舊的四符號圖示已不能再印——出口日本卻沿用舊圖，是這幾年最常見的退貨原因之一。",
        "en": "ISO 3758 is a five-symbol system built around the washtub: washing, bleaching, drying, ironing and professional dry cleaning, always in that order, with the last symbol carrying the strictest limit. China's GB/T 8685 and Japan's JIS L 0001 are broadly compatible, but Japan replaced its four-symbol care labelling with the five-symbol system, so the old pictograms can no longer be printed — shipping to Japan with the old set is one of the most common reasons a care label comes back.",
        "fr": "L'ISO 3758 est un système de cinq symboles autour de la cuve : lavage, blanchiment, séchage, repassage, nettoyage professionnel à sec, toujours dans cet ordre, le dernier portant la limite la plus stricte. Le GB/T 8685 chinois et le JIS L 0001 japonais sont largement compatibles, mais le Japon a remplacé ses quatre pictogrammes par le système à cinq symboles : les anciens ne peuvent plus être imprimés. Expédier au Japon avec l'ancien jeu est l'une des causes de retour les plus fréquentes.",
        "es": "ISO 3758 es un sistema de cinco símbolos alrededor de la cubeta: lavado, blanqueo, secado, planchado y limpieza profesional en seco, siempre en ese orden, y el último símbolo lleva el límite más estricto. La GB/T 8685 china y la JIS L 0001 japonesa son en gran medida compatibles, pero Japón sustituyó sus cuatro pictogramas por el sistema de cinco símbolos y los antiguos ya no pueden imprimirse: enviar a Japón con el juego antiguo es una de las causas de devolución más frecuentes.",
        "ja": "ISO 3758 は洗濯槽を中心とした 5 記号の体系です。洗濯・漂白・乾燥・アイロン・専門ドライの順序は固定で、最後の記号が最も厳しい制限を表します。中国の GB/T 8685、日本の JIS L 0001 も概ね整合しますが、日本は 2016 年の改正で 4 記号から 5 記号体系に移行し、旧ピクトグラムは表示できなくなりました。日本向けに旧図を残すのは、洗濯表示で返品になる最も多い原因の 1 つです。",
        "ko": "ISO 3758은 세탁조를 중심으로 한 5개 기호 체계입니다. 세탁·표백·건조·다림질·전문 드라이 순서가 고정이며 마지막 기호가 가장 엄격한 제한을 뜻합니다. 중국 GB/T 8685와 일본 JIS L 0001은 대체로 호환되지만, 일본은 2016년 개정으로 4개 기호에서 5개 기호 체계로 바뀌어 옛 픽토그램은 더 이상 표시할 수 없습니다. 일본 수출분에 옛 도안을 남기는 것은 세탁 표시 관련 반품의 가장 흔한 원인 중 하나입니다.",
    }),

    ("ul", [
        {
            "zh": "洗滌：槽內數字是最高溫度（30、40、60），下方一條橫線表示緩和程序，兩條表示非常緩和，一隻手表示只能手洗。",
            "en": "Washing: the number in the tub is the maximum temperature (30, 40, 60), one bar underneath means a mild cycle, two bars a very mild cycle, and a hand means hand wash only.",
            "fr": "Lavage : le chiffre dans la cuve est la température maximale (30, 40, 60), une barre dessous signifie cycle modéré, deux barres cycle très modéré, une main signifie lavage à la main uniquement.",
            "es": "Lavado: el número en la cubeta es la temperatura máxima (30, 40, 60), una barra debajo indica ciclo suave, dos barras ciclo muy suave y una mano significa solo a mano.",
            "ja": "洗濯：槽内の数字が上限温度（30・40・60）。下の 1 本線は弱い処理、2 本線は非常に弱い処理、手の記号は手洗いのみを表します。",
            "ko": "세탁: 세탁조 안 숫자가 최고 온도(30, 40, 60)이고, 아래 한 줄은 약한 처리, 두 줄은 매우 약한 처리, 손 기호는 손세탁만 가능하다는 뜻입니다.",
        },
        {
            "zh": "漂白：三角形空白表示可任何漂白，帶兩條斜線表示只可氧系（不含氯），打叉表示不可漂白。毛與蠶絲一律打叉。",
            "en": "Bleaching: an empty triangle allows any bleach, two diagonal lines mean oxygen bleach only, a cross means no bleaching. Wool and silk are always crossed.",
            "fr": "Blanchiment : triangle vide, tout agent autorisé ; deux diagonales, oxygène uniquement ; croix, pas de blanchiment. Laine et soie portent toujours la croix.",
            "es": "Blanqueo: triángulo vacío permite cualquier blanqueador, dos diagonales solo oxígeno, una cruz prohíbe el blanqueo. Lana y seda siempre llevan cruz.",
            "ja": "漂白：白三角はすべて可、斜線 2 本は酸素系のみ、×は漂白不可。ウールとシルクは必ず×です。",
            "ko": "표백: 빈 삼각형은 모든 표백 가능, 사선 두 줄은 산소계만, X는 표백 금지. 울과 실크는 항상 X입니다.",
        },
        {
            "zh": "乾燥：正方形內畫圓表示可滾筒烘乾，圓點數對應溫度（一點低溫、兩點中溫）；正方形內一條橫線表示懸掛晾乾，兩條表示平攤晾乾。喀什米爾正確的圖示是平攤。",
            "en": "Drying: a circle inside a square means tumble dry, with dots for heat (one low, two medium); a horizontal line inside a square means line dry, two lines mean dry flat. For cashmere the correct pictogram is dry flat.",
            "fr": "Séchage : un cercle dans un carré signifie sèche-linge, avec des points pour la chaleur (un doux, deux modéré) ; une ligne dans un carré signifie séchage sur fil, deux lignes séchage à plat. Pour le cachemire, le pictogramme correct est à plat.",
            "es": "Secado: un círculo dentro de un cuadrado significa secadora, con puntos de calor (uno bajo, dos medio); una línea horizontal dentro del cuadrado es secado en línea y dos líneas, secado en plano. Para cachemir el pictograma correcto es en plano.",
            "ja": "乾燥：四角の中の円はタンブラー乾燥可、点の数が温度（1 点低温、2 点中温）。四角の中の横 1 本線はつり干し、2 本線は平干し。カシミヤの正しい記号は平干しです。",
            "ko": "건조: 사각형 안의 원은 텀블 건조 가능, 점 개수가 온도(1점 저온, 2점 중온)입니다. 사각형 안 가로 한 줄은 걸어서 건조, 두 줄은 평평하게 건조. 캐시미어의 올바른 기호는 평건조입니다.",
        },
        {
            "zh": "熨燙：熨斗內一點＝110 ℃ 以下、兩點＝150 ℃ 以下、三點＝200 ℃ 以下。羊毛與蠶絲標一點並註明墊布，或不標熨燙只標蒸氣整燙。",
            "en": "Ironing: one dot means up to 110 °C, two dots 150 °C, three dots 200 °C. Wool and silk take one dot with a pressing cloth, or steam only.",
            "fr": "Repassage : un point jusqu'à 110 °C, deux points 150 °C, trois points 200 °C. Laine et soie : un point avec pattemouille, ou vapeur seule.",
            "es": "Planchado: un punto hasta 110 °C, dos puntos 150 °C, tres puntos 200 °C. Lana y seda, un punto con paño o solo vapor.",
            "ja": "アイロン：1 点は 110 ℃ 以下、2 点は 150 ℃ 以下、3 点は 200 ℃ 以下。ウールとシルクは 1 点＋当て布、またはスチームのみ。",
            "ko": "다림질: 1점은 110 ℃ 이하, 2점은 150 ℃ 이하, 3점은 200 ℃ 이하. 울과 실크는 1점에 받침천을 쓰거나 스팀만 사용합니다.",
        },
        {
            "zh": "專業乾洗：圓圈內 P 為四氯乙烯，F 為石油溶劑，A 為任何溶劑；下方加橫線代表緩和處理。這一個符號最容易與水洗衝突，寫之前先確認面料實際做過什麼測試。",
            "en": "Professional dry cleaning: P in a circle is perchloroethylene, F is petroleum solvent, A is any solvent; a bar underneath means mild treatment. This is the symbol most likely to contradict the wash instruction, so confirm what the fabric was actually tested against.",
            "fr": "Nettoyage à sec professionnel : P dans un cercle pour le perchloroéthylène, F pour les solvants pétroliers, A pour tout solvant ; une barre dessous indique un traitement modéré. C'est le symbole qui contredit le plus souvent le lavage : vérifiez ce qui a réellement été testé.",
            "es": "Limpieza en seco profesional: P en círculo es percloroetileno, F disolvente mineral, A cualquier disolvente; una barra debajo indica tratamiento suave. Es el símbolo que más contradice el lavado: confirma contra qué se ensayó realmente.",
            "ja": "専門ドライ：円の中の P はパークロロエチレン、F は石油系、A はすべての溶剤。下の横線は弱い処理を表します。水洗いと最も矛盾しやすい記号なので、実際に何で試験したかを確認してから書きます。",
            "ko": "전문 드라이: 원 안의 P는 퍼클로로에틸렌, F는 석유계, A는 모든 용제이며 아래 가로줄은 약한 처리를 뜻합니다. 세탁 지시와 가장 충돌하기 쉬운 기호이므로 실제로 어떤 용제로 시험했는지 확인한 뒤 표기하세요.",
        },
    ]),

    ("callout", {
        "zh": "符號順序不要自創。常有供應商為了版面把乾洗符號放到最後一行並加框強調，結果整組符號被解讀成「只有乾洗」——符號本身沒有強調的概念，順序就是語法。",
        "en": "Do not invent your own symbol order. Suppliers often move the dry-clean symbol to a final line with a box around it for emphasis, and the whole set then reads as dry-clean only. Symbols have no emphasis; order is the grammar.",
        "fr": "N'inventez pas l'ordre des symboles. Des fournisseurs déplacent le symbole de nettoyage à sec sur une dernière ligne encadrée pour le mettre en avant : l'ensemble se lit alors comme « nettoyage à sec uniquement ». Un symbole n'a pas d'emphase ; l'ordre est la grammaire.",
        "es": "No inventes el orden de los símbolos. Muchos proveedores mueven el símbolo de limpieza en seco a una última línea enmarcada para destacarlo, y el conjunto se lee como «solo limpieza en seco». Los símbolos no tienen énfasis: el orden es la gramática.",
        "ja": "記号の順序を独自に変えないこと。ドライの記号だけを最終行に移して枠で強調する供給元がありますが、その場合の全体は「ドライのみ」と読まれます。記号に強調の概念はなく、順序そのものが文法です。",
        "ko": "기호 순서를 임의로 바꾸지 마세요. 드라이 기호만 마지막 줄로 옮기고 테두리로 강조하는 공급사가 있는데, 그러면 전체가 '드라이만 가능'으로 읽힙니다. 기호에는 강조 개념이 없고 순서가 문법입니다.",
    }),

    ("h2", {
        "zh": "三、混紡與成分標註：5% 規則",
        "en": "3. Blends and Fibre Content: The 5% Rule",
        "fr": "3. Mélanges et composition : la règle des 5 %",
        "es": "3. Mezclas y composición: la regla del 5 %",
        "ja": "3. 混紡と混用率：5 % ルール",
        "ko": "3. 혼방과 혼용률: 5% 규칙",
    }),

    ("p", {
        "zh": "歐盟與多數市場對混紡成分的容忍度是 ±3 個百分點，但有一條常被忽略的豁免：含量低於 5% 的纖維可以標「其他纖維」而不寫名稱（羊毛與蠶絲混紡另有更嚴的規則）。成分標註義務本身來自法規：歐盟以 Reglamento (UE) 1007/2011 規範紡織品名稱與成分，西班牙的消費者法規要求標示以西班牙語呈現，法國則由 Code de la consommation 要求法語標示。",
        "en": "Most markets allow ±3 percentage points on declared fibre content, but there is an exemption that gets missed: a fibre below 5% may be declared as other fibres without naming it, with a stricter rule for wool and silk blends. The labelling duty itself comes from law — Reglamento (UE) 1007/2011 governs textile names and composition in the EU, Spanish consumer rules require the information in Spanish, and French law, via the Code de la consommation, requires French.",
        "fr": "La plupart des marchés tolèrent ±3 points sur la composition déclarée, avec une exemption souvent oubliée : une fibre sous 5 % peut être déclarée « autres fibres » sans être nommée (règle plus stricte pour les mélanges laine et soie). L'obligation d'étiquetage vient du droit : le Reglamento (UE) 1007/2011 encadre les dénominations et la composition dans l'UE, les règles espagnoles exigent l'espagnol, et en France le Code de la consommation impose le français.",
        "es": "La mayoría de mercados tolera ±3 puntos sobre la composición declarada, con una exención que se olvida: una fibra por debajo del 5 % puede declararse como «otras fibras» sin nombrarla (regla más estricta para mezclas de lana y seda). La obligación de etiquetado viene de la norma: el Reglamento (UE) 1007/2011 regula denominaciones y composición en la UE, la normativa española exige la información en español y en Francia el Code de la consommation impone el francés.",
        "ja": "多くの市場で混用率の許容差は ±3 ポイントですが、見落とされやすい例外があります。5 % 未満の繊維は名称を書かず「その他の繊維」と表示できます（ウールとシルクの混紡はより厳しい規則）。表示義務自体は法令に基づきます。EU は Reglamento (UE) 1007/2011 が繊維名称と組成を定め、日本では家庭用品品質表示法により組成（混用率）と取扱表示の表示義務があります。",
        "ko": "대부분 시장에서 혼용률 허용차는 ±3%p이지만 자주 놓치는 예외가 있습니다. 5% 미만 섬유는 명칭 없이 '기타 섬유'로 표시할 수 있습니다(울·실크 혼방은 더 엄격). 표시 의무 자체는 법령에서 나옵니다. EU는 규정 (EU) 1007/2011이 섬유 명칭과 조성을 정하고, 한국은 품질경영 및 공산품안전관리법에 따라 혼용률과 취급 표시 의무가 적용됩니다.",
    }),

    ("ul", [
        {
            "zh": "主纖維按含量由高到低排列，名稱用標準術語，不要自創「羊毛感」「蠶絲觸感」這類容易構成誤導的寫法。",
            "en": "List fibres from highest to lowest content using standard names — never invented wording like wool-feel or silk-touch, which reads as misleading.",
            "fr": "Classer les fibres de la plus forte à la plus faible avec les dénominations normalisées — jamais « toucher laine » ou « effet soie », qui induisent en erreur.",
            "es": "Ordena las fibras de mayor a menor con denominaciones normalizadas, nunca «tacto lana» o «efecto seda», que resultan engañosos.",
            "ja": "混用率の高い順に標準名称で記載します。「ウール感」「シルクタッチ」のような独自表現は誤認を招くため使いません。",
            "ko": "혼용률이 높은 순서로 표준 명칭을 사용합니다. '울 감촉', '실크 터치' 같은 임의 표현은 오인을 유발하므로 쓰지 않습니다.",
        },
        {
            "zh": "羊毛混紡的 5% 規則更嚴：羊毛含量低於 5% 時，若標「羊毛」須能證明其確實影響產品特性，否則不得作為賣點。",
            "en": "The 5% rule is stricter for wool: below 5%, calling it wool requires evidence that it genuinely affects the product's character, otherwise it cannot be a selling point.",
            "fr": "La règle des 5 % est plus stricte pour la laine : sous 5 %, la mention laine exige la preuve qu'elle affecte réellement le produit, sinon elle ne peut pas être un argument.",
            "es": "La regla del 5 % es más estricta para la lana: por debajo, llamarla lana exige probar que afecta de verdad al producto; si no, no puede ser argumento de venta.",
            "ja": "ウールの 5 % ルールはより厳格です。5 % 未満で「ウール」と表示するには、製品特性に実際に寄与することを示す必要があり、根拠がなければ訴求できません。",
            "ko": "울의 5% 규칙은 더 엄격합니다. 5% 미만에서 '울'로 표시하려면 제품 특성에 실제로 기여함을 입증해야 하며, 근거가 없으면 판매 포인트로 쓸 수 없습니다.",
        },
        {
            "zh": "裝飾性輔料（如 2% 彈性纖維）雖低於 5%，若影響洗護方式就仍應標示，否則消費者按錯誤方式洗滌，責任回到品牌。",
            "en": "A trim fibre such as 2% elastane may fall under 5%, but if it changes how the garment is washed it should still be declared — otherwise the customer washes it wrongly and liability returns to the brand.",
            "fr": "Une fibre accessoire comme 2 % d'élasthanne est sous 5 %, mais si elle change l'entretien elle doit être déclarée, sinon le client lave mal et la responsabilité revient à la marque.",
            "es": "Una fibra accesoria como 2 % de elastano está bajo el 5 %, pero si cambia el cuidado debe declararse; si no, el cliente lava mal y la responsabilidad vuelve a la marca.",
            "ja": "2 % のエラスタンなど副次的な繊維は 5 % 未満でも、手入れ方法を変えるなら表示すべきです。さもないと消費者が誤った方法で洗い、責任はブランドに戻ります。",
            "ko": "2% 엘라스테인 같은 부차적 섬유가 5% 미만이어도 관리 방법을 바꾼다면 표시해야 합니다. 그렇지 않으면 소비자가 잘못 세탁하고 책임은 브랜드로 돌아옵니다.",
        },
    ]),

    ("h2", {
        "zh": "四、尺寸穩定性：三次洗滌之後",
        "en": "4. Dimensional Stability: After Three Washes",
        "fr": "4. Stabilité dimensionnelle : après trois lavages",
        "es": "4. Estabilidad dimensional: después de tres lavados",
        "ja": "4. 寸法安定性：3 回洗濯した後",
        "ko": "4. 치수 안정성: 3회 세탁 후",
    }),

    ("p", {
        "zh": "洗水標上寫的縮率承諾，應該對應一次真實測試，而不是供應商的口頭保證。家用洗滌的標準做法是 ISO 6330（或美標 AATCC 135），量測點固定為胸寬、衣長、袖長，洗三次後回量。針織羊毛與喀什米爾的長度變化允差一般放 ±3%，亞麻首次洗滌 ±5%，超過就要在標上寫「初次洗滌可能輕微縮水」或改工藝（預縮、樹脂整理）。",
        "en": "A shrinkage promise on the care label should map to a real test, not a supplier's verbal assurance. The standard route for domestic washing is ISO 6330, or AATCC 135 in the US, with fixed measuring points — chest width, body length, sleeve length — re-measured after three cycles. Knitted wool and cashmere usually carry ±3% on length; linen takes ±5% on the first wash. Beyond that, either print a first-wash shrinkage note or change the process with pre-shrinking or resin finishing.",
        "fr": "Une promesse de retrait sur l'étiquette doit correspondre à un essai réel, pas à une assurance verbale. La voie normalisée pour le lavage domestique est l'ISO 6330, ou l'AATCC 135 aux États-Unis, avec des points de mesure fixes — largeur poitrine, longueur dos, longueur manche — remesurés après trois cycles. La maille laine et cachemire tient généralement ±3 % en longueur, le lin ±5 % au premier lavage. Au-delà, imprimez une mention de retrait au premier lavage ou changez le procédé (préretrait, finition résine).",
        "es": "Una promesa de encogimiento en la etiqueta debe corresponder a un ensayo real, no a una garantía verbal. La vía normalizada para lavado doméstico es ISO 6330, o AATCC 135 en EE. UU., con puntos de medida fijos — ancho de pecho, largo de cuerpo, largo de manga — remedidos tras tres ciclos. El punto de lana y cachemir suele tolerar ±3 % en largo; el lino, ±5 % en el primer lavado. Más allá, imprime una nota de encogimiento inicial o cambia el proceso (preencogido, acabado con resina).",
        "ja": "洗濯表示の収縮の約束は、供給元の口約束ではなく実際の試験に対応すべきです。家庭洗濯の標準は ISO 6330（米国は AATCC 135）で、胸幅・着丈・袖丈の測定点を固定し、3 回洗濯後に再測定します。ニットのウールとカシミヤは丈で ±3 %、リネンは初回 ±5 % を目安に許容し、超える場合は「初回洗濯で多少縮む」と表示するか、防縮加工・樹脂加工に変更します。",
        "ko": "세탁 표시의 수축 약속은 공급사 구두 보증이 아니라 실제 시험에 대응해야 합니다. 가정 세탁의 표준은 ISO 6330(미국은 AATCC 135)이며, 가슴너비·총장·소매길이 측정점을 고정해 3회 세탁 후 다시 측정합니다. 니트 울과 캐시미어는 길이 ±3%, 리넨은 첫 세탁 ±5%를 보통 허용하며, 초과하면 '첫 세탁 시 약간 수축' 문구를 넣거나 방축·수지 가공으로 공정을 바꿉니다.",
    }),

    ("h2", {
        "zh": "五、標材與可讀性：寫對了也要看得清",
        "en": "5. Label Material and Legibility: Right Symbols, Readable Print",
        "fr": "5. Support et lisibilité : des symboles justes, une impression lisible",
        "es": "5. Material y legibilidad: símbolos correctos, impresión legible",
        "ja": "5. 素材と可読性：正しい記号を、読める大きさで",
        "ko": "5. 소재와 가독성: 맞는 기호를 읽을 수 있게",
    }),

    ("ul", [
        {
            "zh": "標材：羊毛與喀什米爾建議用軟緞帶或尼龍塔夫綢洗水標，邊緣熱切，避免硬邊摩擦扎人；深色衣物用白色標底印黑字，比同色標更清楚。",
            "en": "Material: for wool and cashmere use a soft satin or nylon taffeta care label with heat-cut edges so the border does not scratch. On dark garments, white label stock with black print reads better than a matched dark label.",
            "fr": "Support : pour la laine et le cachemire, préférez un satin doux ou un taffetas nylon aux bords thermocoupés, pour éviter le grattage. Sur les pièces foncées, un support blanc imprimé noir se lit mieux qu'une étiquette assortie.",
            "es": "Material: para lana y cachemir, usa satén suave o tafetán de nailon con borde termosellado para que no raspe. En prendas oscuras, un soporte blanco con impresión negra se lee mejor que una etiqueta del mismo tono.",
            "ja": "素材：ウールとカシミヤは柔らかいサテンまたはナイロンタフタの洗濯表示を使い、端は熱カットで肌当たりを避けます。濃色製品では白地に黒印刷のほうが同色ラベルより読みやすいです。",
            "ko": "소재: 울과 캐시미어는 부드러운 새틴이나 나일론 태피터 세탁 표시를 쓰고 가장자리는 열처리해 피부 자극을 줄입니다. 어두운 제품은 흰 바탕에 검정 인쇄가 동색 라벨보다 잘 읽힙니다.",
        },
        {
            "zh": "字高：符號最小邊長建議 5 mm，警示文字建議 2 mm 以上；日本市場的取扱表示與混用率要求能清楚辨識，實務上以 1.5 mm 以上字高為底線。",
            "en": "Size: keep symbol height at 5 mm minimum and warning text at 2 mm or more. Japanese care and composition marking has to be legible, and in practice 1.5 mm is the floor for character height.",
            "fr": "Taille : hauteur de symbole 5 mm minimum, texte d'avertissement 2 mm ou plus. Au Japon, l'entretien et la composition doivent rester lisibles : en pratique 1,5 mm est le plancher.",
            "es": "Tamaño: símbolo de 5 mm mínimo y texto de advertencia de 2 mm o más. En Japón el cuidado y la composición deben ser legibles; en la práctica 1,5 mm es el mínimo.",
            "ja": "サイズ：記号は一辺 5 mm 以上、注意文言は 2 mm 以上が目安。日本の取扱表示と混用率は判読できる必要があり、実務では 1.5 mm 以上を下限とします。",
            "ko": "크기: 기호는 한 변 5 mm 이상, 주의 문구는 2 mm 이상을 권장합니다. 일본의 취급 표시와 혼용률은 판독 가능해야 하며 실무에서는 1.5 mm 이상을 하한으로 봅니다.",
        },
        {
            "zh": "位置：後領中下 1–2 cm 為國際慣例，長版外套可改放側縫；同一件衣服若有多張標（主嘜、洗水標、成分標），洗護符號只出現一次，避免互相矛盾。",
            "en": "Placement: centre back neck, 1–2 cm below the seam, is the convention; long coats can move it to the side seam. If a garment carries several labels, the care symbols appear once only, so they cannot contradict each other.",
            "fr": "Pose : au milieu du dos, 1–2 cm sous la couture d'encolure, est la convention ; les manteaux longs peuvent la placer au côté. Si la pièce porte plusieurs étiquettes, les symboles d'entretien n'apparaissent qu'une fois, pour éviter toute contradiction.",
            "es": "Posición: centro de la espalda, 1–2 cm bajo la costura, es la convención; los abrigos largos pueden llevarla a la costura lateral. Si la prenda lleva varias etiquetas, los símbolos de cuidado aparecen una sola vez para no contradecirse.",
            "ja": "位置：後ろ衿ぐりの中央、縫い目から 1〜2 cm 下が国際的な慣例です。ロングコートは脇縫いへ移せます。複数のラベルが付く場合も、取扱記号は 1 か所だけにして矛盾を避けます。",
            "ko": "위치: 뒤목 중앙, 솔기 아래 1~2 cm가 국제 관례입니다. 롱코트는 옆 솔기로 옮길 수 있습니다. 라벨이 여러 개면 취급 기호는 한 곳에만 표시해 서로 모순되지 않게 합니다.",
        },
        {
            "zh": "耐久：洗三次後符號仍須可讀。熱轉印標在羊毛這類高摩擦面料上容易掉字，優先選織嘜或印刷緞帶；出貨前抽 3 件做一次實洗確認。",
            "en": "Durability: symbols must still read after three washes. Heat-transfer labels lose print on high-friction wool; prefer woven or printed satin, and wash three sample garments before shipping.",
            "fr": "Durabilité : les symboles doivent rester lisibles après trois lavages. Le transfert thermique perd de l'encre sur la laine ; préférez le tissé ou le satin imprimé, et lavez trois pièces avant expédition.",
            "es": "Durabilidad: los símbolos deben leerse tras tres lavados. La transferencia térmica pierde tinta en lana; prefiere tejido o satén impreso y lava tres prendas antes de embarcar.",
            "ja": "耐久性：3 回洗濯後も記号が読めること。熱転写はウールのような高摩擦素材で文字が欠けやすいため、織りラベルか印刷サテンを優先し、出荷前に 3 着を実洗い確認します。",
            "ko": "내구성: 3회 세탁 후에도 기호가 읽혀야 합니다. 열전사 라벨은 마찰이 큰 울에서 인쇄가 벗겨지므로 직조나 인쇄 새틴을 우선하고, 출하 전 3벌을 실제 세탁해 확인합니다.",
        },
    ]),

    ("p", {
        "zh": "最後一個實務提醒：天然纖維的洗護建議會隨後整理改變。同一塊羊毛料，做過防縮處理與沒做過，洗水標可以完全不同；採購換了染廠或整理廠，舊標就要重新確認。把「面料測試報告編號」寫進輔料檔案，比在標上多加一行免責聲明有用。",
        "en": "One last practical note: care advice for natural fibres changes with finishing. The same wool can take completely different symbols depending on whether it was pre-shrunk, and when a dyehouse or finisher changes, old labels must be re-confirmed. Recording the fabric test report number in the trim file is worth more than adding another disclaimer line to the label.",
        "fr": "Dernier point pratique : les conseils d'entretien des fibres naturelles changent avec la finition. Une même laine supporte des symboles très différents selon qu'elle a été préretraitée ou non, et un changement de teinturerie ou d'apprêt impose de revérifier les anciennes étiquettes. Noter le numéro du rapport d'essai dans le dossier accessoire vaut mieux qu'ajouter une ligne de décharge sur l'étiquette.",
        "es": "Último apunte práctico: el consejo de cuidado de las fibras naturales cambia con el acabado. La misma lana admite símbolos muy distintos según se haya preencogido o no, y al cambiar de tintorería o acabador hay que reconfirmar las etiquetas antiguas. Anotar el número del informe de ensayo en el expediente del accesorio vale más que añadir otra línea de descargo.",
        "ja": "最後に実務的な注意点です。天然繊維のケア表示は仕上げで変わります。同じウールでも防縮加工の有無で記号はまったく変わり、染色工場や整理工場が変われば旧表示を再確認する必要があります。ラベルに免責文を 1 行足すより、生地試験報告の番号を副資材ファイルに残すほうが有効です。",
        "ko": "마지막 실무 주의점입니다. 천연 섬유의 관리 지침은 가공에 따라 달라집니다. 같은 울도 방축 가공 여부에 따라 기호가 완전히 달라지고, 염색공장이나 가공공장이 바뀌면 기존 라벨을 다시 확인해야 합니다. 라벨에 면책 문구를 한 줄 더 넣는 것보다 원단 시험 성적서 번호를 부자재 파일에 남기는 편이 낫습니다.",
    }),

    ("related", [
        ("care-label-standards.html", {
            "zh": "洗水標標準總覽：ISO 3758、EN 與各國要求",
            "en": "Care label standards: ISO 3758, EN and national requirements",
            "fr": "Normes d'étiquetage d'entretien : ISO 3758, EN et exigences nationales",
            "es": "Normas de etiquetado de cuidado: ISO 3758, EN y requisitos nacionales",
            "ja": "洗濯表示の規格：ISO 3758・EN・各国要件",
            "ko": "세탁 표시 규격: ISO 3758·EN·각국 요건",
        }),
        ("care-label-symbols-chart.html", {
            "zh": "洗滌符號對照表：五個符號的完整圖解",
            "en": "Care symbol chart: the five symbols explained",
            "fr": "Tableau des symboles d'entretien : les cinq symboles expliqués",
            "es": "Tabla de símbolos de cuidado: los cinco símbolos explicados",
            "ja": "洗濯記号一覧：5 記号の完全図解",
            "ko": "세탁 기호 도표: 5개 기호 완전 해설",
        }),
        ("care-label-fabric-content.html", {
            "zh": "洗水標上的成分標註：允差與常見錯誤",
            "en": "Fibre content on care labels: tolerances and common errors",
            "fr": "Composition sur l'étiquette d'entretien : tolérances et erreurs",
            "es": "Composición en la etiqueta de cuidado: tolerancias y errores",
            "ja": "洗濯表示の組成表記：許容差とよくある誤り",
            "ko": "세탁 표시의 조성 표기: 허용차와 흔한 오류",
        }),
    ]),

    ("cta", (
        {
            "zh": "手上有羊毛、蠶絲或亞麻的洗水標要定稿，但不確定符號與縮率允差怎麼寫？把面料成分、後整理與目標市場告訴我們，我們回一份含符號組合、成分允差與洗後允收標準的洗水標規格。",
            "en": "Finalising a care label for wool, silk or linen and unsure which symbols and shrinkage allowances to use? Send the fibre content, finishing and target markets, and we will return a care label spec with symbol set, composition tolerance and post-wash acceptance limits.",
            "fr": "Vous finalisez une étiquette d'entretien laine, soie ou lin sans savoir quels symboles et quelles tolérances de retrait retenir ? Envoyez composition, finition et marchés cibles : nous renvoyons une spécification avec jeu de symboles, tolérance de composition et limites de retrait.",
            "es": "¿Estás cerrando una etiqueta de cuidado de lana, seda o lino sin saber qué símbolos y tolerancias de encogimiento usar? Envía composición, acabado y mercados destino, y devolvemos una especificación con juego de símbolos, tolerancia de composición y límites de encogimiento.",
            "ja": "ウール・シルク・リネンの洗濯表示を確定したいが、記号と収縮許容の書き方が不明な場合。組成・仕上げ・対象市場をご連絡ください。記号の組み合わせ、組成許容差、洗濯後の合格基準をまとめた仕様案をお返しします。",
            "ko": "울·실크·리넨 세탁 표시를 확정해야 하는데 기호와 수축 허용치가 불확실한가요? 조성, 가공, 목표 시장을 보내주시면 기호 조합, 조성 허용차, 세탁 후 합격 기준을 담은 세탁 표시 사양안을 회신합니다.",
        },
        {
            "zh": "索取天然纖維洗水標規格 →", "en": "Request a natural-fibre care label spec →",
            "fr": "Demander une spécification d'étiquetage →", "es": "Solicitar especificación de etiqueta →",
            "ja": "天然繊維の洗濯表示仕様を依頼 →", "ko": "천연 섬유 세탁 표시 사양 요청 →",
        },
    )),
]
