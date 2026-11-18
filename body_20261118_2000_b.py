# -*- coding: utf-8 -*-
"""2026-11-18 20:00 批次 B：輔料與服裝防霉（回南天、集裝箱結露、乾燥劑用量）"""

SLUG = "apparel-trims-mold-prevention-shipping"
CATEGORY = {
    "zh": "包裝指南", "en": "Packaging Guide", "fr": "Guide emballage",
    "es": "Guía de embalaje", "ja": "包装ガイド", "ko": "포장 가이드",
}
TITLE = {
    "zh": "輔料與服裝防霉：回南天、集裝箱結露與乾燥劑用量 | TAGE",
    "en": "Mold Prevention for Apparel Trims: Container Rain and Desiccant Sizing | TAGE",
    "fr": "Moisissures sur accessoires : pluie de conteneur et dosage des dessiccants | TAGE",
    "es": "Moho en accesorios de confección: lluvia de contenedor y dosificación de desecantes | TAGE",
    "ja": "副資材のカビ対策：コンテナ結露と乾燥剤の量 | TAGE",
    "ko": "부자재 곰팡이 방지: 컨테이너 결로와 제습제 산정 | TAGE",
}
DESC = {
    "zh": "黴菌只認三個條件：濕度、溫度、養分。這篇講清楚哪些輔料最先發霉、集裝箱結露怎麼算、乾燥劑用量（DIN 55474）與防霉劑的 REACH 紅線，附來料檢驗與索賠證據。",
    "en": "Which trims mold first, how container rain forms, how to size desiccant by DIN 55474, the REACH ban on DMF sachets, plus inspection and claim evidence.",
    "fr": "Quels accessoires moisissent d'abord, comment se forme la pluie de conteneur, doser le dessiccant selon DIN 55474 et l'interdiction REACH du DMF.",
    "es": "Qué accesorios se enmohecen primero, cómo se forma la lluvia de contenedor, cómo dosificar desecante (método DIN 55474) y la prohibición REACH del DMF.",
    "ja": "どの副資材が先にカビるか、コンテナ結露の仕組み、DIN 55474 による乾燥剤の量、防カビ剤の REACH 規制、入荷検査とクレームの証拠まで整理します。",
    "ko": "어떤 부자재가 먼저 곰팡이가 나는지, 컨테이너 결로의 원리, DIN 55474 제습제 산정, 항곰팡이제의 REACH 규제, 입고 검사와 클레임 증거까지 정리합니다.",
}
H1 = {
    "zh": "輔料防霉：從回南天到集裝箱結露",
    "en": "Mold Prevention for Apparel Trims, from Humidity Season to Container Rain",
    "fr": "Moisissures sur accessoires : de la saison humide à la pluie de conteneur",
    "es": "Moho en accesorios: de la temporada húmeda a la lluvia de contenedor",
    "ja": "副資材のカビ対策：湿気の季節からコンテナ結露まで",
    "ko": "부자재 곰팡이 방지: 습한 계절에서 컨테이너 결로까지",
}

BLOCKS = [
    ("p", {
        "zh": "每年三到四月，珠三角的輔料倉庫就開始「出汗」：紙吊牌邊緣起波紋、皮標背面長白斑、棉織帶一打開就有霉味。這不是衛生問題，而是黴菌的三個條件同時達標——相對濕度過線、溫度落在適宜區間、材料本身帶著澱粉漿料或油脂當養分。本文把防霉拆成可檢查的三段：源頭（倉庫與生產）、載體（紙、布、皮、木）與運輸（集裝箱結露），並給出乾燥劑用量的算法與防霉劑的法規紅線。",
        "en": "Mold is not a hygiene problem. It is the result of three conditions being met at the same time: relative humidity above the threshold, temperature in the growth band, and a nutrient — starch sizing, leather fat, paper coating. This guide splits prevention into three checkable stages: the source (warehouse and production), the carrier (paper, fabric, leather, wood) and transit (container rain), then gives a desiccant sizing method and the regulatory limits on mold sachets.",
        "fr": "La moisissure n'est pas un problème d'hygiène. C'est la conjonction de trois conditions : humidité relative au-dessus du seuil, température dans la plage de croissance, et un nutriment — apprêt amidonné, graisse du cuir, couchage du papier. Ce guide découpe la prévention en trois étapes vérifiables : la source (entrepôt et production), le support (papier, tissu, cuir, bois) et le transport (pluie de conteneur), avant de donner une méthode de dimensionnement du desséchant et les limites réglementaires des sachets antimoisissure.",
        "es": "El moho no es un problema de higiene. Es la coincidencia de tres condiciones: humedad relativa por encima del umbral, temperatura dentro de la franja de crecimiento y un nutriente: apresto de almidón, grasa del cuero, estucado del papel. Esta guía divide la prevención en tres etapas verificables: el origen (almacén y producción), el soporte (papel, tejido, cuero, madera) y el transporte (lluvia de contenedor), y añade un método de dosificación de desecante y los límites reglamentarios de las bolsas antimoho.",
        "ja": "カビは衛生問題ではなく、3 つの条件が同時に揃った結果です。相対湿度がしきい値を超え、温度が生育域に入り、材料そのものが養分（澱粉の糊料、革の油脂、紙の塗工層）を持つこと。本稿は防カビを検査できる 3 段階に分けます。発生源（倉庫・生産）、担体（紙・布・革・木）、輸送（コンテナ結露）です。あわせて乾燥剤の量の求め方と、防カビ剤に課される法規制の線を整理します。",
        "ko": "곰팡이는 위생 문제가 아니라 세 조건이 동시에 충족된 결과입니다. 상대습도가 기준을 넘고, 온도가 생육 구간에 들고, 소재 자체가 영양분(전분 호료, 가죽 유지, 종이 도공층)을 가진 경우입니다. 이 글은 방곰팡이를 점검 가능한 세 단계로 나눕니다. 발생원(창고·생산), 담체(종이·직물·가죽·목재), 운송(컨테이너 결로)이며, 제습제 산정법과 항곰팡이제의 규제 한계도 정리합니다.",
    }),
    ("h2", {
        "zh": "一、先分清哪些輔料最危險",
        "en": "1. Know Which Trims Are at Risk First",
        "fr": "1. Identifier d'abord les accessoires les plus exposés",
        "es": "1. Saber primero qué accesorios son más vulnerables",
        "ja": "1. まず危険な副資材を特定する",
        "ko": "1. 먼저 위험한 부자재를 구분하기",
    }),
    ("table", ([
        {"zh": "材料", "en": "Material", "fr": "Matériau", "es": "Material", "ja": "材料", "ko": "소재"},
        {"zh": "風險來源", "en": "Why it molds", "fr": "Pourquoi", "es": "Por qué", "ja": "リスク要因", "ko": "위험 요인"},
        {"zh": "實務臨界", "en": "Practical threshold", "fr": "Seuil pratique", "es": "Umbral práctico", "ja": "実務の目安", "ko": "실무 기준"},
    ], [
        [
            {"zh": "紙吊牌、紙卡、紙袋", "en": "Paper hang tags, cards, bags", "fr": "Étiquettes et sacs papier", "es": "Etiquetas y bolsas de papel", "ja": "紙の下げ札・カード・袋", "ko": "종이 행택·카드·봉투"},
            {"zh": "纖維吸濕、塗布層與澱粉膠提供養分", "en": "Fibre absorbs moisture; coating and starch glue feed mold", "fr": "la fibre absorbe l'humidité, le couchage et la colle amidon nourrissent", "es": "la fibra absorbe humedad; el estucado y la cola de almidón alimentan", "ja": "吸湿＋塗工層・澱粉糊が養分", "ko": "흡습 + 도공층·전분 풀이 영양분"},
            {"zh": "含水率 >8% 即開始有風險", "en": "Moisture content above 8% starts the risk", "fr": "au-delà de 8 % d'humidité", "es": "por encima del 8 % de humedad", "ja": "含水率 8 % 超で危険域", "ko": "함수율 8% 초과부터 위험"},
        ],
        [
            {"zh": "皮標、麂皮絨、皮革吊牌", "en": "Leather patches, suede, leather tags", "fr": "patches cuir, suédine, étiquettes cuir", "es": "parches de cuero, ante, etiquetas de piel", "ja": "革パッチ・スエード・革タグ", "ko": "가죽 패치·스웨이드·가죽 태그"},
            {"zh": "油脂與蛋白質是黴菌最愛的基質", "en": "Fat and protein are prime substrate", "fr": "graisses et protéines, substrat idéal", "es": "grasas y proteínas, sustrato ideal", "ja": "油脂・タンパク質が最良の基質", "ko": "유지·단백질이 최적 기질"},
            {"zh": "RH 65% 以上 3–5 天即可見斑", "en": "Spots within 3 to 5 days above 65% RH", "fr": "taches en 3 à 5 jours au-dessus de 65 % HR", "es": "manchas en 3 a 5 días por encima del 65 % HR", "ja": "RH 65 % 超で 3〜5 日で斑点", "ko": "RH 65% 초과 시 3~5일 내 반점"},
        ],
        [
            {"zh": "棉織帶、棉繩、帆布", "en": "Cotton webbing, cord, canvas", "fr": "sangle coton, cordon, toile", "es": "cinta de algodón, cordón, lona", "ja": "綿テープ・綿紐・帆布", "ko": "면 테이프·면 끈·캔버스"},
            {"zh": "天然纖維含果膠與漿料，未完全退漿時最易發霉", "en": "Natural fibre with pectin and sizing molds fastest if not fully desized", "fr": "fibre naturelle avec pectine et apprêt", "es": "fibra natural con pectina y apresto", "ja": "ペクチン・糊料が残ると最も早い", "ko": "펙틴·호료가 남으면 가장 빠름"},
            {"zh": "打包後內部凝水，48 小時可見霉味", "en": "Condensation inside the pack shows as smell in 48 hours", "fr": "condensation interne, odeur en 48 h", "es": "condensación interna, olor en 48 h", "ja": "梱包内結露で 48 時間で匂い", "ko": "포장 내부 결로 시 48시간 내 냄새"},
        ],
        [
            {"zh": "瓦楞紙箱、木棧板", "en": "Corrugated cartons, wooden pallets", "fr": "cartons ondulés, palettes bois", "es": "cartones ondulados, palés de madera", "ja": "段ボール・木パレット", "ko": "골판지·목재 팔레트"},
            {"zh": "紙箱含水率是整櫃發霉的放大器", "en": "Carton moisture multiplies mold across the load", "fr": "l'humidité du carton amplifie tout le chargement", "es": "la humedad del cartón amplifica toda la carga", "ja": "段ボールの含水率が荷全体を増幅", "ko": "골판지 함수율이 전체 화물을 증폭"},
            {"zh": ">12% 必須先烘乾再裝櫃", "en": "Above 12%, dry before loading", "fr": "au-delà de 12 %, sécher avant chargement", "es": "por encima del 12 %, secar antes de cargar", "ja": "12 % 超は乾燥してから積む", "ko": "12% 초과는 건조 후 적재"},
        ],
    ])),
    ("h2", {
        "zh": "二、集裝箱結露：不是漏水，是「下露水」",
        "en": "2. Container Rain: Not a Leak, Condensation",
        "fr": "2. La pluie de conteneur : de la condensation, pas une fuite",
        "es": "2. Lluvia de contenedor: condensación, no una fuga",
        "ja": "2. コンテナ結露：漏水ではなく結露",
        "ko": "2. 컨테이너 결로: 누수가 아니라 결로",
    }),
    ("p", {
        "zh": "很多索賠最後查出來不是櫃子漏水，而是「集裝箱雨」：貨物白天在碼頭被曬到 45–50 °C，艙內空氣吸飽水氣；夜間或北上高緯度航線艙溫掉到 15 °C 以下，水氣就在櫃頂與紙箱表面凝結，順著箱壁往下滴。溫差 10–15 °C 就足以發生，東南亞到歐洲、到美東的航線都是高風險段。判定方法很簡單：霉斑集中在櫃頂那一側、紙箱上緣有水痕而下緣乾燥，就是結露而不是滲水。",
        "en": "Many claims turn out not to be a leaking container but container rain. Cargo sits on the quay at 45 to 50 °C by day and the air inside the box loads up with moisture; at night, or on a northbound leg into higher latitudes, the air drops below 15 °C and the moisture condenses on the roof and carton tops, then drips down. A swing of 10 to 15 °C is enough, which makes South-East Asia to Europe and to the US East Coast high-risk legs. The diagnosis is simple: mold concentrated on the roof side, water marks on the top edge of cartons with dry bottoms — condensation, not seepage.",
        "fr": "Beaucoup de litiges ne viennent pas d'un conteneur qui fuit mais de la pluie de conteneur : la marchandise est à 45–50 °C sur le quai le jour, l'air intérieur se charge d'humidité ; la nuit, ou sur une jambe nordique, il descend sous 15 °C et la vapeur condense sur le toit et le haut des cartons, puis goutte. Un écart de 10 à 15 °C suffit, ce qui rend les liaisons Asie du Sud-Est–Europe et côte Est américaine critiques. Diagnostic : moisissure côté toit, traces sur le bord supérieur des cartons et fonds secs — condensation, pas infiltration.",
        "es": "Muchas reclamaciones no son por un contenedor que gotea sino por lluvia de contenedor: la carga está a 45–50 °C en el muelle de día y el aire interior se carga de humedad; de noche, o en un tramo hacia el norte, baja de 15 °C y el vapor condensa en el techo y en la parte alta de las cajas, y luego gotea. Basta un salto de 10 a 15 °C, lo que convierte el Sudeste Asiático–Europa y la costa este de EE. UU. en tramos críticos. El diagnóstico es simple: moho del lado del techo, marcas en el borde superior y fondos secos.",
        "ja": "クレームの多くはコンテナの漏水ではなく「コンテナレイン」です。日中に埠頭で荷が 45〜50 °C まで上がり、庫内の空気が水分を含みます。夜間や北方航路で庫内が 15 °C を下回ると、天井や段ボール上面に結露して滴ります。10〜15 °C の温度差で起こり、東南アジア→欧州、米東岸は高危険区間です。見分け方は簡単で、カビが天井側に集中し、箱の上縁に水染みがあって底面が乾いていれば結露です。",
        "ko": "클레임의 상당수는 컨테이너 누수가 아니라 컨테이너 레인입니다. 낮에 부두에서 화물이 45~50 °C까지 올라가 내부 공기가 수분을 머금고, 야간이나 북방 항로에서 15 °C 아래로 떨어지면 천장과 골판지 상면에 결로가 생겨 떨어집니다. 10~15 °C 차이로 발생하며 동남아→유럽, 미국 동부 항로가 고위험 구간입니다. 판별은 간단합니다. 곰팡이가 천장 쪽에 몰리고 상자 상단에 물자국이 있으며 바닥은 건조하면 결로입니다.",
    }),
    ("h2", {
        "zh": "三、乾燥劑用量：用算法，不靠經驗",
        "en": "3. Sizing Desiccant by Calculation, Not Habit",
        "fr": "3. Dosage du dessiccant : calcul, pas habitude",
        "es": "3. Dosificación del desecante: cálculo, no costumbre",
        "ja": "3. 乾燥剤の量は計算で決める",
        "ko": "3. 제습제는 계산으로 정한다",
    }),
    ("p", {
        "zh": "德國標準 DIN 55474 給的是「包裝內乾燥劑用量計算」的方法：先算包裝內剩餘空氣的水量、包裝材料自身的含水量與運輸週期內的透濕量，再按乾燥劑的吸附能力換算成克數。實務上很少有人真去算，但這套方法正是買方要求「提供用量依據」時能交得出去的東西。以一個 20 呎櫃約 33 m³ 計，掛式乾燥劑的常見配置落在 10–30 kg，差距來自航線天數、紙箱含水率與是否用 PE 袋密封；密封袋內更要放，否則袋內濕氣無處可去。",
        "en": "German standard DIN 55474 sets out how to calculate the desiccant quantity in a pack: the water in the residual air, the moisture already in the packaging materials, and the vapour transmission over the transit period, converted through the desiccant's absorption capacity into grams. Few suppliers actually run the numbers, yet this is exactly what a buyer means by “show us the basis for the quantity”. For a 20 ft container of roughly 33 m³, hanging desiccant commonly lands between 10 and 30 kg, the spread coming from voyage length, carton moisture and whether loads are sealed in PE bags — and a sealed bag needs desiccant inside, or the trapped moisture has nowhere to go.",
        "fr": "La norme DIN 55474 décrit le calcul de la quantité de dessiccant dans un emballage : eau contenue dans l'air résiduel, humidité des matériaux d'emballage, transmission de vapeur sur la durée du transport, converties en grammes via la capacité d'absorption. Peu de fournisseurs font réellement le calcul, or c'est précisément ce que demande un acheteur. Pour un 20 pieds d'environ 33 m³, on retombe souvent entre 10 et 30 kg de dessiccant suspendu, l'écart venant de la durée du trajet, de l'humidité des cartons et du scellage en sacs PE — un sac scellé doit contenir du dessiccant, sinon l'humidité reste piégée.",
        "es": "La norma DIN 55474 describe cómo calcular la cantidad de desecante en un embalaje: el agua del aire residual, la humedad de los materiales de embalaje y la transmisión de vapor durante el transporte, convertidas en gramos según la capacidad de absorción. Pocos proveedores hacen el cálculo, y es justo lo que pide un comprador. En un contenedor de 20 pies, unos 33 m³, el desecante colgado suele quedar entre 10 y 30 kg, con la variación explicada por la duración del viaje, la humedad de las cajas y el sellado en bolsas de PE; una bolsa sellada necesita desecante dentro.",
        "ja": "ドイツ規格 DIN 55474 は、包装内の乾燥剤量の計算方法を示しています。残留空気中の水分、包装材料自体の含水率、輸送期間中の透湿量を求め、乾燥剤の吸着能力でグラム数に換算します。実際に計算する供給者は少ないのですが、購買側が「量の根拠」を求める時に出すべきものはこれです。20 フィート（約 33 m³）なら吊り下げ型で 10〜30 kg が実務レンジで、差は航海日数・段ボール含水率・PE 袋密封の有無によります。密封袋の中にも入れないと湿気の行き場がありません。",
        "ko": "독일 규격 DIN 55474는 포장 내 제습제량 계산법을 제시합니다. 잔류 공기 중 수분, 포장재 자체 함수율, 운송 기간 중 투습량을 구해 제습제 흡착 능력으로 그램수로 환산합니다. 실제로 계산하는 공급자는 드물지만, 구매팀이 '수량 근거'를 요구할 때 제시해야 하는 것이 바로 이것입니다. 20피트(약 33 m³) 기준 걸이형 제습제는 실무에서 10~30 kg이며, 차이는 항해 일수·골판지 함수율·PE 봉투 밀봉 여부에서 나옵니다. 밀봉 봉투 안에도 넣어야 습기가 갈 곳이 생깁니다.",
    }),
    ("h2", {
        "zh": "四、防霉劑的法規紅線：富馬酸二甲酯",
        "en": "4. The Red Line on Mold Sachets: Dimethyl Fumarate",
        "fr": "4. La ligne rouge des sachets antimoisissure : le DMF",
        "es": "4. La línea roja de las bolsas antimoho: el DMF",
        "ja": "4. 防カビ剤の規制線：ジメチルフマレート",
        "ko": "4. 항곰팡이제의 규제선: 디메틸푸마레이트",
    }),
    ("p", {
        "zh": "最便宜也最危險的防霉手段是富馬酸二甲酯（DMF）防霉片。它在歐盟已被 REACH 法規 (EC) No 1907/2006 附錄 XVII 第 61 條全面禁止用於成品及其部件，限量 0.1 mg/kg；中國 GB 21550 對人造革中的 DMF 也設同樣的 0.1 mg/kg 限量。實務要點有三：防霉片不得與產品直接接觸（必須有隔離層）、防霉片的包裝要有中文或當地語言標示（成分、警示、不得食用）、以及每批要能提供不含 DMF 的聲明或檢測報告——歐盟海關與電商平台都會查這一項。",
        "en": "The cheapest and most dangerous mold control is a dimethyl fumarate (DMF) sachet. In the EU it is banned in articles and parts by REACH Regulation (EC) No 1907/2006, Annex XVII, entry 61, at a limit of 0.1 mg/kg; China's GB 21550 applies the same 0.1 mg/kg limit to DMF in artificial leather. Three practical rules follow: the sachet must never touch the product (a barrier layer is mandatory), the sachet's own packaging must carry a label naming the active substance plus handling and ingestion warnings, and every lot needs a DMF-free declaration or test report — both EU customs and e-commerce platforms check this.",
        "fr": "Le contrôle le moins cher et le plus dangereux est le sachet au diméthylfumarate (DMF), interdit dans les articles et leurs parties par le règlement REACH (CE) n° 1907/2006, annexe XVII, entrée 61, à 0,1 mg/kg. Trois règles : le sachet ne doit jamais toucher le produit (barrière obligatoire), son emballage doit porter un étiquetage indiquant la substance active et les avertissements (ne pas ingérer), et chaque lot doit fournir une déclaration sans DMF ou un rapport d'essai — les douanes et les places de marché le contrôlent.",
        "es": "El control más barato y más peligroso es la bolsa de dimetilfumarato (DMF), prohibida en artículos y sus partes por el Reglamento REACH (CE) n.º 1907/2006, anexo XVII, entrada 61, con un límite de 0,1 mg/kg. Tres reglas: la bolsa nunca debe tocar el producto (barrera obligatoria), su propio envase debe llevar etiquetado con la sustancia activa y advertencias (no ingerir), y cada lote necesita declaración libre de DMF o informe de ensayo; aduanas y marketplaces lo comprueban.",
        "ja": "最も安価で最も危険な防カビ手段がジメチルフマレート（DMF）の防カビシートです。EU では REACH 規則 (EC) No 1907/2006 附属書 XVII 第 61 項により成形品およびその部品での使用が禁止され、限度は 0.1 mg/kg です。中国の GB 21550 も人工皮革中の DMF に同じ 0.1 mg/kg を課しています。実務は 3 点：防カビシートを製品に直接接触させない（隔離層必須）、シート自体の包装に成分と警告（誤食注意）の表示を行う、ロットごとに DMF 不含宣言か試験報告書を用意する。税関も EC モールも確認します。",
        "ko": "가장 저렴하고 가장 위험한 방곰팡이 수단이 디메틸푸마레이트(DMF) 시트입니다. EU에서는 REACH 규정 (EC) No 1907/2006 부속서 XVII 제61항으로 완제품과 부품에 사용이 전면 금지되며 한도는 0.1 mg/kg입니다. 중국 GB 21550도 인조가죽의 DMF에 같은 0.1 mg/kg을 적용합니다. 실무 원칙은 세 가지입니다. 시트가 제품에 직접 닿지 않게 하고(격리층 필수), 시트 자체 포장에 성분과 경고(섭취 금지)를 표시하고, 로트마다 DMF 불검출 선언이나 시험 성적서를 준비합니다. 세관과 이커머스 플랫폼 모두 확인합니다.",
    }),
    ("h2", {
        "zh": "五、來料與出貨前怎麼檢：三個動作",
        "en": "5. Three Checks Before and After Production",
        "fr": "5. Trois contrôles avant expédition",
        "es": "5. Tres controles antes del envío",
        "ja": "5. 出荷前の 3 つの検査",
        "ko": "5. 출하 전 세 가지 검사",
    }),
    ("ul", [
        {
            "zh": "含水率：紙箱、紙吊牌用針式水分計量 3 點取平均，超過 8%（紙品）或 12%（紙箱）就先烘或換批次。",
            "en": "Moisture content: take three pin-meter readings on cartons and paper tags and average them; above 8% for paper goods or 12% for cartons, dry the lot or switch batches.",
            "fr": "Humidité : trois mesures au duromètre à pointes sur cartons et étiquettes, moyenne ; au-delà de 8 % (papier) ou 12 % (carton), sécher ou changer de lot.",
            "es": "Humedad: tres lecturas con higrómetro de agujas en cajas y etiquetas, promedio; por encima de 8 % (papel) o 12 % (cartón), secar o cambiar de lote.",
            "ja": "含水率：段ボール・紙タグを針式水分計で 3 点測定し平均。紙製品 8 %、段ボール 12 % を超えたら乾燥またはロット変更。",
            "ko": "함수율: 골판지와 종이 태그를 침식 수분계로 3점 측정해 평균. 종이 제품 8%, 골판지 12%를 넘으면 건조하거나 로트를 교체합니다.",
        },
        {
            "zh": "黴菌抵抗性：對塗層布、人造革、紙品可要求 ASTM G21、ISO 846 或 JIS Z 2911 的黴菌抵抗性試驗，報告要寫明菌種與判定級數。",
            "en": "Fungal resistance: for coated fabric, artificial leather and paper, ask for ASTM G21, ISO 846 or JIS Z 2911 testing with the species list and pass grade stated.",
            "fr": "Résistance fongique : pour tissu enduit, cuir synthétique et papier, demander ASTM G21, ISO 846 ou JIS Z 2911, avec espèces testées et note obtenue.",
            "es": "Resistencia fúngica: para tejido recubierto, cuero sintético y papel, pedir ASTM G21, ISO 846 o JIS Z 2911, con especies y calificación.",
            "ja": "カビ抵抗性：コーティング生地・人工皮革・紙は ASTM G21、ISO 846、JIS Z 2911 の試験を依頼し、菌種と判定を明記させます。",
            "ko": "곰팡이 저항성: 코팅 원단·인조가죽·종이는 ASTM G21, ISO 846, JIS Z 2911 시험을 요청하고 균종과 판정을 명기합니다.",
        },
        {
            "zh": "目視與嗅覺：抽 5 箱開箱即聞，霉味比霉斑早出現 1–2 天；發現白斑、綠斑或紙邊起波，整批隔離不要只挑壞的。",
            "en": "Sight and smell: open five cartons and smell on opening — odor appears one or two days before visible spots. If white or green spots or wavy paper edges show, isolate the whole lot instead of picking out the bad pieces.",
            "fr": "Vue et odorat : ouvrir cinq cartons et sentir immédiatement — l'odeur précède les taches de un à deux jours. Taches blanches ou vertes, bords ondulés : isoler tout le lot.",
            "es": "Vista y olfato: abrir cinco cajas y oler al abrir; el olor aparece uno o dos días antes que las manchas. Si hay manchas blancas o verdes o bordes ondulados, aislar todo el lote.",
            "ja": "目視と嗅覚：5 箱を開封して臭いを確認。においは斑点より 1〜2 日早く出ます。白斑・緑斑・紙端の波打ちがあればロット全体を隔離します。",
            "ko": "육안과 후각: 5상자를 열어 냄새를 확인합니다. 냄새는 반점보다 1~2일 먼저 나타납니다. 흰 반점·녹색 반점·종이 끝 물결이 보이면 로트 전체를 격리합니다.",
        },
    ]),
    ("callout", {
        "zh": "索賠時最常輸在證據：發現霉變當天就要拍照（含櫃號、箱號、溫濕度記錄器讀數）、保留未開箱樣品、並在 48 小時內以書面通知貨代與供應商。拖到清關後才提，保險與責任很難成立。",
        "en": "Claims are usually lost on evidence. Photograph the day you find it — container number, carton number, logger readings — keep unopened samples, and notify the forwarder and supplier in writing within 48 hours. Raising it after customs clearance makes both insurance and liability hard to establish.",
        "fr": "Un litige se perd sur les preuves. Photographier le jour même (numéro de conteneur, de carton, relevés d'enregistreur), conserver des échantillons non ouverts et notifier par écrit sous 48 heures. Après dédouanement, assurance et responsabilité deviennent difficiles à établir.",
        "es": "Un reclamo se pierde por falta de pruebas. Fotografiar el mismo día (número de contenedor, de caja, lecturas del registrador), conservar muestras sin abrir y notificar por escrito en 48 horas. Después del despacho, el seguro y la responsabilidad son difíciles de sostener.",
        "ja": "クレームで負けるのは証拠です。発見当日に撮影（コンテナ番号・箱番号・温湿度ロガーの値）、未開封サンプルを保管し、48 時間以内に書面で通知します。通関後に持ち出すと保険も責任も通りません。",
        "ko": "클레임에서 지는 이유는 증거입니다. 발견 당일 촬영(컨테이너 번호, 상자 번호, 온습도 로거 값), 미개봉 샘플 보관, 48시간 내 서면 통지를 해야 합니다. 통관 후에 제기하면 보험도 책임도 인정되기 어렵습니다.",
    }),
    ("h2", {
        "zh": "六、包裝規格怎麼寫進採購單",
        "en": "6. Writing It into the Purchase Order",
        "fr": "6. L'inscrire dans la commande",
        "es": "6. Cómo incluirlo en la orden de compra",
        "ja": "6. 発注書への書き込み方",
        "ko": "6. 발주서에 기재하는 방법",
    }),
    ("p", {
        "zh": "把防霉變成可驗收的條款，只需要四行：① 內包裝用 0.05 mm 以上 PE 袋並置入乾燥劑，用量依 DIN 55474 計算並標明克數；② 紙箱含水率 ≤12%、紙吊牌 ≤8%，出貨前抽測並附記錄；③ 外箱標示「Keep Dry」與堆碼方向，櫃內掛式乾燥劑數量與位置寫明；④ 防霉劑須提供不含 DMF 聲明，包裝標示成分與警語。四行寫進採購單，糾紛時就不必靠回憶。",
        "en": "Four lines turn mold control into something you can accept or reject: inner packaging in PE bags of 0.05 mm or thicker with desiccant sized by DIN 55474 and the gram figure stated; carton moisture at or below 12% and paper tags at or below 8%, sampled before shipment with records kept; “Keep Dry” and stacking arrows on the outer carton plus the number and position of hanging desiccant units in the container; and a DMF-free declaration with the sachet's own label carrying active substance and warnings. Written into the purchase order, none of it depends on memory in a dispute.",
        "fr": "Quatre lignes rendent le contrôle vérifiable : emballage intérieur en sacs PE de 0,05 mm minimum avec dessiccant dosé selon DIN 55474 et grammage indiqué ; humidité du carton ≤12 % et des étiquettes papier ≤8 %, contrôlée avant expédition ; mention « Keep Dry » et flèches de gerbage sur le carton, nombre et position des dessiccants suspendus dans le conteneur ; déclaration sans DMF avec étiquetage du sachet (substance active et avertissements).",
        "es": "Cuatro líneas convierten el control en algo verificable: embalaje interior en bolsas de PE de 0,05 mm o más con desecante dosificado según DIN 55474 y gramos indicados; humedad del cartón ≤12 % y de etiquetas de papel ≤8 %, muestreada antes del envío; « Keep Dry » y flechas de apilado en la caja, más número y posición de desecantes colgados en el contenedor; y declaración libre de DMF con etiquetado del propio sobre (sustancia activa y advertencias).",
        "ja": "4 行で検査可能になります。① 内装は 0.05 mm 以上の PE 袋と DIN 55474 で算出した乾燥剤（グラム数を明記）、② 段ボール含水率 12 % 以下・紙タグ 8 % 以下を出荷前に抽測し記録、③ 外箱に Keep Dry と積み重ね矢印、コンテナ内の吊り下げ乾燥剤の数と位置を明記、④ DMF 不含宣言と、シート包装への成分・警告表示。",
        "ko": "네 줄이면 검수 가능한 조항이 됩니다. ① 내포장은 0.05 mm 이상 PE 봉투와 DIN 55474로 산정한 제습제(그램수 명기), ② 골판지 함수율 12% 이하·종이 태그 8% 이하를 출하 전 측정해 기록, ③ 외부 상자에 Keep Dry와 적재 방향 표시, 컨테이너 내 걸이형 제습제 수량과 위치 명기, ④ DMF 불검출 선언과 시트 포장의 성분·경고 표시.",
    }),
    ("h2", {
        "zh": "七、日本與韓國：防霉要接到當地標籤義務上",
        "en": "7. Japan and Korea: Tie Mold Control to Local Labelling Duties",
        "fr": "7. Japon et Corée : rattacher la prévention à l'étiquetage local",
        "es": "7. Japón y Corea: vincular la prevención al etiquetado local",
        "ja": "7. 日韓：防カビ対策を現地の表示義務につなぐ",
        "ko": "7. 한·일: 방곰팡이 조치를 현지 표시 의무와 연결하기",
    }),
    ("p", {
        "zh": "同一批輔料賣到日本或韓國，防霉措施最後會落在標籤上。日本依家庭用品品質表示法必須標示纖維組成、洗濯表示與原産国，乾燥劑與防霉片本身另須標示成分與誤食警示；黴菌抵抗性可委託 JIS Z 2911 試驗，報告要寫菌種與判定。韓國則依 전기용품 및 생활용품 안전관리법 完成生活用品安全基準與 표시 의무，纖維 혼용률、취급 표시 與 원산지 是基本欄位，黴菌抵抗性多依 KS M ISO 846 或 KS K 0693 委託檢測。包裝上的 Keep Dry、乾燥劑克數與生產批號，兩地買方都會要求印在外箱。",
        "en": "When the same trims are sold into Japan or Korea, mold control ends up on a label. In Japan the Household Goods Quality Labelling Act requires fibre composition, care labelling and country of origin, and desiccant or mold sachets must carry their own composition and ingestion warnings; fungal resistance is usually commissioned to JIS Z 2911 with species and grade stated. In Korea the Electrical Appliances and Consumer Products Safety Control Act sets the safety criteria and labelling duties, with fibre content, care marking and origin as standard fields, and fungal resistance is tested to KS M ISO 846 or KS K 0693. Both markets expect Keep Dry, the desiccant gram figure and the lot number printed on the outer carton.",
        "fr": "Vendus au Japon ou en Corée, les mêmes accessoires finissent sur une étiquette. Au Japon, la loi sur l'étiquetage de qualité impose composition, entretien et origine, et le sachet de dessiccant doit porter sa propre composition et un avertissement d'ingestion ; la résistance fongique se commande selon JIS Z 2911. En Corée s'appliquent la loi sur la sécurité des appareils électriques et produits de consommation (critères et mentions obligatoires : composition, entretien, origine) et les essais KS M ISO 846 ou KS K 0693. En France, l'étiquetage reste la pièce opposable : composition, entretien et origine doivent correspondre au lot livré, et un essai selon NF EN ISO 846 sert de preuve en cas de litige.",
        "es": "Vendidos en Japón o Corea, los mismos accesorios acaban en una etiqueta. En Japón la ley de etiquetado de calidad exige composición, cuidado y origen, y el sobre desecante debe llevar su propia composición y advertencia de ingestión; la resistencia fúngica se encarga según JIS Z 2911. En Corea aplican la ley de seguridad de aparatos eléctricos y productos de consumo (criterios y menciones obligatorias: composición, cuidado, origen) y ensayos KS M ISO 846 o KS K 0693. En España el etiquetado es la prueba oponible: composición, cuidado y origen deben coincidir con el lote entregado, y un ensayo UNE-EN ISO 846 sostiene la posición en caso de reclamación.",
        "ja": "同じ副資材を日本や韓国へ販売する場合、防カビ対策は最終的に表示に落ちます。日本では家庭用品品質表示法により組成・洗濯表示・原産国の表示が義務づけられ、乾燥剤や防カビシート自体にも成分表示と誤食注意が必要です。カビ抵抗性は JIS Z 2911 で委託試験し、菌種と判定を報告書に明記させます。韓国では 전기용품 및 생활용품 안전관리법 による安全基準と 표시 의무 がかかり、混用率・취급 표시・원산지 が基本欄です。外箱には Keep Dry、乾燥剤のグラム数、製造ロット番号を両市場とも求めます。",
        "ko": "같은 부자재를 한국이나 일본에 판매하면 방곰팡이 조치는 결국 표시로 귀결됩니다. 한국은 전기용품 및 생활용품 안전관리법에 따른 안전기준과 표시 의무가 적용되어 섬유 혼용률, 취급 표시, 원산지가 기본 항목이고, 곰팡이 저항성은 KS M ISO 846 또는 KS K 0693으로 시험합니다. 일본은 家庭用品品質表示法에 따라 組成·洗濯表示·原産国 표시가 의무이며, 제습제와 항곰팡이 시트 자체에도 성분과 섭취 금지 경고를 표시해야 합니다. 두 시장 모두 외부 상자에 Keep Dry, 제습제 그램수, 제조 로트 번호를 요구합니다.",
    }),
    ("related", [
        ("index.html", {"zh": "輔料 FAQ 全部文章", "en": "All trims FAQ articles", "fr": "Tous les articles FAQ", "es": "Todos los artículos", "ja": "副資材 FAQ 一覧", "ko": "부자재 FAQ 전체"}),
        ("garment-moisture-proof-packaging.html", {"zh": "防潮包裝：材料、密封與乾燥劑", "en": "Moisture-proof packaging: materials, sealing and desiccant", "fr": "Emballage étanche : matériaux, scellage, dessiccant", "es": "Embalaje antihumedad: materiales, sellado y desecante", "ja": "防湿包装：材料・密封・乾燥剤", "ko": "방습 포장: 소재·밀봉·제습제"}),
        ("silica-gel-desiccant-apparel-packaging.html", {"zh": "乾燥劑怎麼選：矽膠、蒙脫石與用量", "en": "Choosing desiccant: silica gel, montmorillonite and quantity", "fr": "Choisir un dessiccant : gel de silice, montmorillonite, quantité", "es": "Elegir desecante: gel de sílice, montmorillonita y cantidad", "ja": "乾燥剤の選び方：シリカゲル・モンモリロナイトと量", "ko": "제습제 선택: 실리카겔·몬모릴로나이트와 사용량"}),
        ("garment-trims-storage-conditions-guide.html", {"zh": "輔料倉儲條件：溫濕度與堆碼", "en": "Trim storage conditions: temperature, humidity, stacking", "fr": "Stockage des accessoires : température, humidité, gerbage", "es": "Almacenaje de accesorios: temperatura, humedad, apilado", "ja": "副資材の保管条件：温湿度と積み方", "ko": "부자재 보관 조건: 온습도와 적재"}),
    ]),
    ("cta", (
        {
            "zh": "要往潮濕市場或長航線出貨？把包裝方式、航線與櫃型告訴我們，我們按 DIN 55474 算出乾燥劑克數，並把含水率、防霉與 DMF 聲明寫進出貨規格與檢驗表。",
            "en": "Shipping into humid markets or on long routes? Tell us the packaging format, route and container type and we will size the desiccant to DIN 55474, then write moisture, mold and DMF requirements into your shipping spec and inspection sheet.",
            "fr": "Vous expédiez vers des marchés humides ou sur de longues liaisons ? Indiquez emballage, trajet et type de conteneur : nous dimensionnons le dessiccant selon DIN 55474 et intégrons humidité, moisissure et DMF dans votre cahier des charges.",
            "es": "¿Envía a mercados húmedos o en rutas largas? Indique embalaje, ruta y tipo de contenedor: dimensionamos el desecante según DIN 55474 e incluimos humedad, moho y DMF en su especificación y hoja de inspección.",
            "ja": "湿潤市場や長距離航路への出荷をお考えなら、包装形態・航路・コンテナ種をお知らせください。DIN 55474 で乾燥剤量を算出し、含水率・カビ・DMF の条項を出荷仕様と検査表に落とします。",
            "ko": "습한 시장이나 장거리 항로로 출하하십니까? 포장 형태·항로·컨테이너 종류를 알려주시면 DIN 55474로 제습제량을 산정하고 함수율·곰팡이·DMF 조항을 출하 사양과 검사표에 반영합니다.",
        },
        {
            "zh": "索取防潮防霉包裝規格", "en": "Request the moisture and mold control spec", "fr": "Demander le cahier des charges anti-humidité", "es": "Solicitar la especificación antihumedad", "ja": "防湿・防カビ仕様を依頼", "ko": "방습·방곰팡이 사양 요청",
        },
    )),
]
