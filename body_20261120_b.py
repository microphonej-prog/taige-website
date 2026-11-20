# -*- coding: utf-8 -*-
"""2026-11-20 08:00 批次 B：取消款輔料庫存的四條處理路徑——回收率、法規邊界與倉儲成本。"""

SLUG = "trim-dead-stock-guide"
CATEGORY = {
    "zh": "採購與成本", "en": "Sourcing & Cost", "fr": "Achats et coûts",
    "es": "Compras y costes", "ja": "調達・コスト", "ko": "소싱·원가",
}
TITLE = {
    "zh": "取消款的輔料庫存：四條處理路徑與代價 | TAGE",
    "en": "Leftover Trims After a Cancelled Style: Four Routes | TAGE",
    "fr": "Accessoires d'une collection annulée : quatre voies | TAGE",
    "es": "Accesorios de una colección cancelada: cuatro vías | TAGE",
    "ja": "企画中止で余った副資材：4 つの処理ルートとコスト | TAGE",
    "ko": "시즌 취소로 남은 부자재: 네 가지 처리 경로 | TAGE",
}
DESC = {
    "zh": "款式取消但輔料已到貨：留用、改造、轉讓、銷毀四條路徑的回收率與代價，三件絕對不能做的事，以及舊庫存再上市時重新觸發的法規義務。",
    "en": "A style is cancelled but the trims have landed. Four routes compared by recovery rate and risk, three things never to do, and rules that re-trigger on reuse.",
    "fr": "Une collection est annulée mais les accessoires sont livrés. Quatre voies comparées en taux de récupération et en risque, trois interdits et les obligations réactivées en cas de réemploi.",
    "es": "Una colección se cancela pero los accesorios ya llegaron. Cuatro vías comparadas por recuperación y riesgo, tres prohibiciones y las obligaciones que se reactivan al reutilizar.",
    "ja": "企画が中止になっても副資材は納品済み。再利用・改造・譲渡・廃棄の 4 ルートを回収率とリスクで比較し、やってはいけない 3 つと再出荷時に発生する義務を整理します。",
    "ko": "기획이 취소돼도 부자재는 이미 입고됩니다. 재사용·개조·양도·폐기 네 경로를 회수율과 리스크로 비교하고, 하면 안 되는 세 가지와 재출고 시 다시 발생하는 의무를 정리합니다.",
}
H1 = {
    "zh": "取消款的輔料庫存：四條路徑與各自的代價",
    "en": "Leftover Trims After a Cancelled Style: Four Routes and What Each Costs",
    "fr": "Accessoires restants d'une collection annulée : quatre voies et leur coût",
    "es": "Accesorios sobrantes de una colección cancelada: cuatro vías y su coste",
    "ja": "企画中止で余った副資材：4 つの処理ルートとそのコスト",
    "ko": "시즌 취소로 남은 부자재: 네 가지 처리 경로와 비용",
}

BLOCKS = [
    ("p", {
        "zh": "一款衣服在開季前被砍掉，輔料通常已經到貨：吊牌、織唛、洗水標、包裝袋整批躺在倉庫裡。帳面價值也許只有幾千元，處理方式錯了卻會變成品牌風險——把 A 品牌的織唛縫進 B 品牌的衣服是偽造，把品牌物料當廢紙賣掉是資訊外流。留用、改造、轉讓、銷毀四條路徑各有回收率與代價，選錯往往比報廢更貴。",
        "en": "When a style is cancelled before the season, the trims have usually already landed: hang tags, woven labels, care labels and bags sitting in the warehouse. On paper the stock may be worth a few thousand dollars, but handled the wrong way it becomes brand risk. Sewing brand A's woven label into brand B's garment is counterfeiting; selling branded material as paper waste is a leak. Keep, rework, transfer or destroy: each route has its own recovery rate and cost, and choosing wrong usually costs more than scrapping.",
        "fr": "Quand un modèle est annulé avant la saison, les accessoires sont en général déjà livrés : étiquettes pendantes, étiquettes tissées, étiquettes d'entretien et sacs stockés à l'entrepôt. Sur le papier, le stock vaut quelques milliers de dollars, mais mal traité il devient un risque de marque. Coudre l'étiquette tissée de la marque A dans un vêtement de la marque B est une contrefaçon ; vendre du matériel de marque comme vieux papier est une fuite. Conserver, transformer, céder ou détruire : chaque voie a son taux de récupération et son coût, et se tromper coûte souvent plus cher que de mettre au rebut.",
        "es": "Cuando un modelo se cancela antes de temporada, los accesorios ya suelen haber llegado: etiquetas colgantes, etiquetas tejidas, etiquetas de cuidado y bolsas en el almacén. En el papel el stock vale unos miles de dólares, pero mal gestionado se convierte en riesgo de marca. Coser la etiqueta tejida de la marca A en una prenda de la marca B es falsificación; vender material de marca como papel viejo es una fuga. Conservar, transformar, ceder o destruir: cada vía tiene su tasa de recuperación y su coste, y equivocarse suele costar más que desechar.",
        "ja": "シーズン前に企画が中止されても、副資材はすでに納品済みということがほとんどです。下げ札、織りネーム、洗濯表示ラベル、袋が倉庫に残ります。帳簿上は数千ドルでも、扱いを誤るとブランドリスクになります。A ブランドの織りネームを B ブランドの衣類に縫い付けるのは偽造であり、ブランド資材を古紙として売るのは情報漏えいです。保管・改造・譲渡・廃棄の 4 ルートにはそれぞれ回収率とコストがあり、選び間違えると廃棄より高くつきます。",
        "ko": "시즌 전에 스타일이 취소되어도 부자재는 이미 입고된 경우가 많습니다. 행택, 직조 라벨, 세탁 라벨, 봉투가 창고에 남습니다. 장부상 수천 달러일 수 있지만 잘못 처리하면 브랜드 리스크가 됩니다. A 브랜드 직조 라벨을 B 브랜드 의류에 봉제하는 것은 위조이고, 브랜드 자재를 고지로 파는 것은 정보 유출입니다. 보관·개조·양도·폐기 네 경로에는 각각 회수율과 비용이 있으며, 잘못 고르면 폐기보다 비쌉니다.",
    }),

    ("h2", {
        "zh": "一、庫存是怎麼留下來的",
        "en": "1. How the Stock Appears in the First Place",
        "fr": "1. Comment ce stock apparaît",
        "es": "1. Cómo aparece ese stock",
        "ja": "1. 在庫はどう生まれるか",
        "ko": "1. 재고는 어떻게 생기는가",
    }),

    ("ul", [
        {
            "zh": "款式在投產前取消，但輔料按開發日曆已下單並交貨。",
            "en": "The style is cancelled before production, but trims were ordered on the development calendar and have been delivered.",
            "fr": "Le modèle est annulé avant production, mais les accessoires commandés selon le calendrier de développement ont été livrés.",
            "es": "El modelo se cancela antes de producir, pero los accesorios pedidos según el calendario ya se entregaron.",
            "ja": "量産前に企画が中止。ただし開発カレンダーに沿って発注済みの副資材は納品済みです。",
            "ko": "양산 전에 기획이 취소되었지만 개발 일정에 따라 발주한 부자재는 이미 납품되었습니다.",
        },
        {
            "zh": "起訂量與實際用量落差：實際只用 8,000 個，起訂量是 10,000 個。",
            "en": "MOQ against actual consumption: the order needed 8,000 pieces but the minimum run was 10,000.",
            "fr": "Décalage entre quantité minimale et consommation réelle : 8 000 pièces nécessaires, 10 000 imposées.",
            "es": "Desajuste entre pedido mínimo y consumo real: se necesitaban 8.000 piezas y el mínimo era 10.000.",
            "ja": "MOQ と実使用量の差。必要 8,000 個に対して最小ロットが 10,000 個。",
            "ko": "MOQ와 실제 소요량 차이. 필요 8,000개인데 최소 주문이 10,000개.",
        },
        {
            "zh": "改版後的舊版：顏色、版號或語言組合換了，舊版全部作廢。",
            "en": "The previous version after a revision: colour, version code or language set changed, retiring the whole old run.",
            "fr": "L'ancienne version après révision : couleur, numéro de version ou jeu de langues modifié, tout le lot devient obsolète.",
            "es": "La versión anterior tras una revisión: cambian color, número de versión o idiomas y todo el lote queda obsoleto.",
            "ja": "改版後の旧版。色・版番号・言語構成が変わり、旧ロットがすべて不要になります。",
            "ko": "개정 후 구버전. 색상, 버전 번호, 언어 구성이 바뀌어 이전 로트가 모두 불용이 됩니다.",
        },
        {
            "zh": "為損耗多訂的 3–5%，實際良率比預期好，多出來的留在架上。",
            "en": "The 3–5% ordered for spoilage, where the actual yield beat the estimate and the surplus stays on the shelf.",
            "fr": "Les 3 à 5 % commandés pour le rebut, alors que le rendement réel a dépassé l'estimation et le surplus reste en stock.",
            "es": "El 3–5 % pedido por merma, cuando el rendimiento real superó la estimación y el sobrante queda en estantería.",
            "ja": "損耗分として多めに発注した 3〜5 % が、実収率が上振れして棚に残る。",
            "ko": "손실 대비 3~5% 더 발주했는데 실제 수율이 좋아 남은 재고.",
        },
        {
            "zh": "供應商的超交：約定 ±10% 交貨公差，供應商交到上限。",
            "en": "Supplier over-delivery: with a ±10% delivery tolerance agreed, the supplier ships the upper limit.",
            "fr": "La livraison excédentaire du fournisseur : avec une tolérance de ±10 %, il livre la limite haute.",
            "es": "La entrega excedente del proveedor: con tolerancia de ±10 %, entrega el límite superior.",
            "ja": "サプライヤーの過納。±10 % の納入公差の上限まで納品される。",
            "ko": "공급사 과납. ±10% 납품 공차의 상한까지 납품됩니다.",
        },
    ]),

    ("h2", {
        "zh": "二、四條路徑與各自的回收率",
        "en": "2. Four Routes and What Each Recovers",
        "fr": "2. Quatre voies et ce que chacune récupère",
        "es": "2. Cuatro vías y lo que recupera cada una",
        "ja": "2. 4 つのルートと回収率",
        "ko": "2. 네 경로와 각각의 회수율",
    }),

    ("table", (
        [
            {"zh": "路徑", "en": "Route", "fr": "Voie", "es": "Vía", "ja": "ルート", "ko": "경로"},
            {"zh": "一次性成本", "en": "One-off cost", "fr": "Frais ponctuels", "es": "Coste puntual", "ja": "初期費用", "ko": "초기 비용"},
            {"zh": "回收帳面價值", "en": "Book value recovered", "fr": "Valeur récupérée", "es": "Valor recuperado", "ja": "回収できる帳簿価額", "ko": "회수 장부가"},
            {"zh": "主要風險", "en": "Main risk", "fr": "Risque principal", "es": "Riesgo principal", "ja": "主なリスク", "ko": "주요 리스크"},
        ],
        [
            [
                {"zh": "留用到下一季", "en": "Hold for next season", "fr": "Conserver pour la saison suivante", "es": "Guardar para la próxima temporada", "ja": "次シーズンへ保管", "ko": "다음 시즌 보관"},
                {"zh": "倉儲與盤點", "en": "Storage and stock count", "fr": "Stockage et inventaire", "es": "Almacenaje e inventario", "ja": "保管と棚卸し", "ko": "보관과 재고 조사"},
                {"zh": "70–100%", "en": "70–100%", "fr": "70 à 100 %", "es": "70–100 %", "ja": "70〜100 %", "ko": "70~100%"},
                {"zh": "設計延續但成分或法規已變，留用變成二次浪費", "en": "The design continues but composition or rules changed, so holding becomes a second waste", "fr": "Le design continue mais composition ou règles ont changé : conserver devient un second gaspillage", "es": "El diseño continúa pero cambian composición o normas: guardar se vuelve un segundo desperdicio", "ja": "デザインは継続でも組成や法規が変わり、保管が二次的な無駄になる", "ko": "디자인은 이어지지만 혼용률이나 규정이 바뀌어 보관이 두 번째 낭비가 됨"},
            ],
            [
                {"zh": "改造再用", "en": "Rework and reuse", "fr": "Transformer et réutiliser", "es": "Transformar y reutilizar", "ja": "改造して再利用", "ko": "개조 후 재사용"},
                {"zh": "拆標、換洗水標、改包裝的人工", "en": "Labour to unpick, replace care labels, re-bag", "fr": "Main-d'œuvre pour découdre, remplacer les étiquettes d'entretien, reconditionner", "es": "Mano de obra para descoser, sustituir etiquetas y reembalar", "ja": "解き外し・洗濯表示の差し替え・袋替えの工数", "ko": "뜯기, 세탁 라벨 교체, 재포장 작업"},
                {"zh": "40–60%", "en": "40–60%", "fr": "40 à 60 %", "es": "40–60 %", "ja": "40〜60 %", "ko": "40~60%"},
                {"zh": "拆標損傷布料，殘膠讓新標貼不牢", "en": "Unpicking damages fabric and residue stops the new label adhering", "fr": "Le décousu abîme le tissu et les résidus empêchent la nouvelle étiquette d'adhérer", "es": "Descoser daña el tejido y los residuos impiden que pegue la nueva etiqueta", "ja": "解くと生地を傷め、残膠で新しいラベルが密着しない", "ko": "뜯으면 원단이 손상되고 잔여 접착제가 새 라벨 부착을 방해"},
            ],
            [
                {"zh": "轉讓或折價", "en": "Transfer or sell at a discount", "fr": "Céder ou vendre à prix réduit", "es": "Ceder o vender con descuento", "ja": "譲渡・割引販売", "ko": "양도 또는 할인 판매"},
                {"zh": "商談、運輸、重新包裝", "en": "Negotiation, freight, re-packing", "fr": "Négociation, transport, réemballage", "es": "Negociación, transporte, reembalaje", "ja": "交渉・輸送・再梱包", "ko": "협상, 운송, 재포장"},
                {"zh": "10–40%", "en": "10–40%", "fr": "10 à 40 %", "es": "10–40 %", "ja": "10〜40 %", "ko": "10~40%"},
                {"zh": "品牌物料外流，含商標的輔料不得轉售給第三方", "en": "Branded material leaking out; items carrying a trademark cannot be resold to third parties", "fr": "Fuite de matériel de marque : les articles portant une marque ne peuvent être revendus à des tiers", "es": "Fuga de material de marca: los artículos con marca registrada no se revenden a terceros", "ja": "ブランド資材の流出。商標入りの副資材は第三者へ転売できません", "ko": "브랜드 자재 유출. 상표가 있는 부자재는 제3자에게 재판매할 수 없음"},
            ],
            [
                {"zh": "銷毀並取證", "en": "Destroy with certification", "fr": "Détruire avec attestation", "es": "Destruir con certificado", "ja": "廃棄して証明を取る", "ko": "폐기 후 증명 확보"},
                {"zh": "銷毀費與見證人工", "en": "Destruction fee and witness time", "fr": "Frais de destruction et temps de témoin", "es": "Coste de destrucción y tiempo de testigo", "ja": "廃棄費用と立会い工数", "ko": "폐기 비용과 입회 인력"},
                {"zh": "0%", "en": "0%", "fr": "0 %", "es": "0 %", "ja": "0 %", "ko": "0%"},
                {"zh": "無回收；但客戶審核時，沒有證書等於無法證明已銷毀", "en": "No recovery, yet without a certificate you cannot prove destruction during a customer audit", "fr": "Aucune récupération ; sans attestation, impossible de prouver la destruction lors d'un audit client", "es": "Sin recuperación; sin certificado no puedes probar la destrucción en una auditoría", "ja": "回収なし。ただし証明がなければ顧客監査で廃棄を立証できません", "ko": "회수 없음. 다만 증명이 없으면 고객 감사에서 폐기를 입증할 수 없음"},
            ],
        ],
    )),

    ("p", {
        "zh": "用一組數字看規模：10,000 個織唛（單價 0.03 美元）加 10,000 張吊牌（0.05 美元），帳面 800 美元。留用一季的倉儲按每立方米每月 8 美元計，兩箱貨佔 0.3 立方米，一季約 7 美元，幾乎可以忽略；但如果下一季把吊牌克重從 350 g/m² 換成 400 g/m²、織唛密度也升級，留用就變成二次浪費——帳面 800 美元全部歸零，還要再付一次倉儲。",
        "en": "Scale it with numbers: 10,000 woven labels at 0.03 dollars and 10,000 hang tags at 0.05 dollars come to 800 dollars on paper. Holding them one season costs about 8 dollars per cubic metre per month, and two cartons occupy roughly 0.3 cubic metres, so a season is about 7 dollars, close to nothing. But if next season moves the tag from 350 g/m² to 400 g/m² and upgrades the label density, the hold becomes a second waste: the 800 dollars goes to zero and the storage was paid twice.",
        "fr": "Mettons des chiffres : 10 000 étiquettes tissées à 0,03 dollar et 10 000 étiquettes pendantes à 0,05 dollar représentent 800 dollars en valeur comptable. Conserver une saison coûte environ 8 dollars par mètre cube et par mois ; deux cartons occupent 0,3 mètre cube, soit environ 7 dollars par saison, presque rien. Mais si la saison suivante fait passer le grammage de 350 g/m² à 400 g/m² et augmente la densité des tissées, la conservation devient un second gaspillage : les 800 dollars tombent à zéro et le stockage est payé deux fois.",
        "es": "Pongámoslo en cifras: 10.000 etiquetas tejidas a 0,03 dólares y 10.000 etiquetas colgantes a 0,05 dólares suman 800 dólares en libros. Guardarlas una temporada cuesta unos 8 dólares por metro cúbico al mes; dos cajas ocupan 0,3 metros cúbicos, así que la temporada sale por unos 7 dólares, casi nada. Pero si la temporada siguiente pasa el gramaje de 350 g/m² a 400 g/m² y sube la densidad de las tejidas, guardar se vuelve un segundo desperdicio: los 800 dólares caen a cero y el almacenaje se paga dos veces.",
        "ja": "数字で見ます。織りネーム 10,000 枚（0.03 ドル）と下げ札 10,000 枚（0.05 ドル）で帳簿上 800 ドル。1 シーズン保管すると 1 立方メートルあたり月 8 ドル、段ボール 2 箱で 0.3 立方メートルなので、1 シーズン約 7 ドルでほぼ無視できます。しかし翌シーズンに下げ札を 350 g/m² から 400 g/m² へ変え、織り密度も上げるなら、保管は二次的な無駄になります。帳簿の 800 ドルはゼロになり、保管料を二度払うことになります。",
        "ko": "숫자로 보면, 직조 라벨 10,000장(0.03달러)과 행택 10,000장(0.05달러)은 장부상 800달러입니다. 한 시즌 보관은 세제곱미터당 월 8달러이고 두 상자가 약 0.3세제곱미터이므로 시즌당 약 7달러로 거의 무시할 수준입니다. 그러나 다음 시즌에 행택 평량을 350 g/m²에서 400 g/m²로 올리고 직조 밀도까지 높인다면 보관은 두 번째 낭비가 됩니다. 장부상 800달러는 0이 되고 보관료를 두 번 내게 됩니다.",
    }),

    ("h2", {
        "zh": "三、三件絕對不能做的事",
        "en": "3. Three Things You Must Never Do",
        "fr": "3. Trois choses à ne jamais faire",
        "es": "3. Tres cosas que nunca hay que hacer",
        "ja": "3. 絶対にやってはいけない 3 つ",
        "ko": "3. 절대 해서는 안 되는 세 가지",
    }),

    ("ul", [
        {
            "zh": "把 A 品牌的織唛或吊牌用到 B 品牌的貨上。這不是「廢物利用」，而是偽造與商標侵權，客戶查廠與海關都可能直接判定。",
            "en": "Using brand A's woven label or hang tag on brand B's goods. That is not waste avoidance, it is counterfeiting and trademark infringement, and both a factory audit and customs can call it.",
            "fr": "Utiliser l'étiquette tissée ou pendante de la marque A sur des articles de la marque B. Ce n'est pas de la récupération, mais de la contrefaçon et une atteinte à la marque, sanctionnables en audit comme en douane.",
            "es": "Usar la etiqueta tejida o colgante de la marca A en artículos de la marca B. No es aprovechamiento, es falsificación e infracción de marca, y lo pueden sancionar tanto una auditoría como la aduana.",
            "ja": "A ブランドの織りネームや下げ札を B ブランドの製品に使うこと。廃物利用ではなく偽造・商標侵害であり、工場監査でも税関でも指摘されます。",
            "ko": "A 브랜드의 직조 라벨이나 행택을 B 브랜드 제품에 사용하는 것. 재활용이 아니라 위조와 상표 침해이며 공장 감사와 세관 모두에서 문제가 됩니다.",
        },
        {
            "zh": "未經品牌方書面同意，把帶商標的物料轉賣、當廢紙賣或以「庫存清理」名義流出。品牌方在意的是控制權，不是那幾百元。",
            "en": "Selling, pulping or quietly clearing trademarked material without written consent. The brand is protecting control, not the few hundred dollars.",
            "fr": "Revendre, mettre au pilon ou écouler discrètement du matériel marqué sans accord écrit. La marque protège le contrôle, pas les quelques centaines de dollars.",
            "es": "Revender, triturar o dar salida discreta a material con marca sin consentimiento escrito. La marca protege el control, no los cientos de dólares.",
            "ja": "ブランドの書面同意なく、商標入り資材を転売・古紙化・在庫処分として流出させること。ブランドが守るのは管理権であり、数百ドルではありません。",
            "ko": "브랜드의 서면 동의 없이 상표가 있는 자재를 재판매, 고지화, 재고 정리 명목으로 유출하는 것. 브랜드가 지키려는 것은 통제권이지 수백 달러가 아닙니다.",
        },
        {
            "zh": "把超過背膠或熱熔膠保質期的輔料直接上線。貼紙與自黏標籤常見保質期 12–24 個月，30 °C 以上老化明顯加速，過期料上線就是半年後的客訴。",
            "en": "Running trims past their adhesive shelf life. Pressure-sensitive labels and stickers commonly carry 12–24 months, ageing accelerates noticeably above 30 °C, and expired stock becomes a complaint six months later.",
            "fr": "Mettre en production des accessoires au-delà de la durée de vie de l'adhésif. Les étiquettes autocollantes tiennent souvent 12 à 24 mois, le vieillissement s'accélère nettement au-delà de 30 °C, et le stock périmé devient une réclamation six mois plus tard.",
            "es": "Poner en línea accesorios con el adhesivo caducado. Las etiquetas autoadhesivas suelen durar 12–24 meses, el envejecimiento se acelera por encima de 30 °C y el stock caducado se convierte en una reclamación seis meses después.",
            "ja": "粘着剤の寿命を過ぎた副資材をそのままラインに投入すること。粘着ラベルは 12〜24 か月が目安で、30 °C を超えると劣化が加速し、期限切れは半年後のクレームになります。",
            "ko": "점착제 수명이 지난 부자재를 그대로 라인에 투입하는 것. 점착 라벨은 보통 12~24개월이며 30 °C 이상에서 노화가 빨라지고, 기한 지난 재고는 반년 뒤 클레임이 됩니다.",
        },
    ]),

    ("h2", {
        "zh": "四、留用不等於免責：法規義務會重新觸發",
        "en": "4. Holding Is Not a Waiver: the Rules Re-Trigger",
        "fr": "4. Conserver n'est pas une dispense : les obligations rejouent",
        "es": "4. Guardar no exime: las obligaciones vuelven",
        "ja": "4. 保管は免責ではない：義務は再発動する",
        "ko": "4. 보관은 면책이 아니다: 의무가 다시 발생한다",
    }),

    ("p", {
        "zh": "舊輔料再次出貨，等於重新投放市場，法規義務全部重新觸發。歐盟 REACH (EC) No 1907/2006 對 SVHC 的資訊與通報義務、GPSR (EU) 2023/988 對製造商與責任主體的追溯要求、(EU) No 1007/2011 對纖維成分的標示要求，都要按當下版本重新核對；美國 16 CFR 423 要求的護理說明必須永久附著；法國除歐盟規則外還適用《消費法典》的標示與語言規定；西班牙以 Real Decreto 928/1987 規範成分標示；日本《家庭用品品質表示法》要求組成、洗濯表示與表示者，韓國依《品質經營及工業品安全管理法》要求品質標示與原產地。三年前的舊庫存放三年不會自動合規。",
        "en": "Shipping old trims puts them back on the market, and the obligations re-trigger in full. Under REACH, (EC) No 1907/2006, SVHC information and notification duties apply; the GPSR, (EU) 2023/988, requires manufacturer and responsible-person traceability; Regulation (EU) No 1007/2011 governs fibre composition marking. In the United States, 16 CFR 423 requires care instructions permanently attached. France adds the Code de la consommation on marking and language, Spain marks composition under Real Decreto 928/1987, Japan requires composition, care symbols and the labeller under its Household Goods Quality Labelling Act, and Korea requires quality marking and origin under its Quality Management and Safety Control of Industrial Products Act. Three years in a rack does not make old stock compliant.",
        "fr": "Réexpédier d'anciens accessoires les remet sur le marché et réactive intégralement les obligations. REACH, (CE) n° 1907/2006, impose l'information et la notification sur les SVHC ; le GPSR, (UE) 2023/988, exige la traçabilité du fabricant et du responsable ; le règlement (UE) n° 1007/2011 encadre le marquage de composition. Aux États-Unis, la règle 16 CFR 423 impose un entretien attaché en permanence. La France ajoute le Code de la consommation sur le marquage et la langue, l'Espagne applique le Real Decreto 928/1987, le Japon exige composition, symboles d'entretien et nom du responsable selon sa loi sur l'étiquetage de qualité, la Corée impose marquage de qualité et origine. Trois ans en rayon ne rendent pas un stock conforme.",
        "es": "Reexpedir accesorios antiguos los devuelve al mercado y reactiva todas las obligaciones. REACH, (CE) n.º 1907/2006, impone información y notificación de SVHC; el GPSR, (UE) 2023/988, exige trazabilidad del fabricante y del responsable; el Reglamento (UE) n.º 1007/2011 regula el marcado de composición. En Estados Unidos, la regla 16 CFR 423 exige instrucciones de cuidado unidas de forma permanente. Francia suma el Code de la consommation sobre marcado e idioma, España aplica el Real Decreto 928/1987, Japón exige composición, símbolos de cuidado y responsable, y Corea exige marcado de calidad y origen. Tres años en estantería no hacen conforme un stock.",
        "ja": "古い副資材を再出荷することは市場への再投入であり、義務がすべて再発動します。EU の REACH（(EC) No 1907/2006）は SVHC の情報提供と届出を求め、GPSR（(EU) 2023/988）は製造者と責任者の追跡可能性を要求し、規則 (EU) No 1007/2011 は繊維組成の表示を定めます。米国は 16 CFR 423 で取扱表示の恒久添付を要求します。フランスは消費法典の表示・言語規定を重ね、スペインは Real Decreto 928/1987、日本は家庭用品品質表示法により組成・洗濯表示・表示者、韓国は品質経営及び工業品安全管理法により品質表示と原産国を求めます。棚に 3 年置いても適合にはなりません。",
        "ko": "오래된 부자재를 다시 출고하는 것은 시장에 재투입하는 것이며 의무가 모두 다시 발생합니다. EU REACH((EC) No 1907/2006)는 SVHC 정보 제공과 신고를 요구하고, GPSR((EU) 2023/988)은 제조사와 책임자의 추적 가능성을, 규정 (EU) No 1007/2011은 섬유 혼용률 표시를 정합니다. 미국은 16 CFR 423으로 취급 표시의 영구 부착을 요구합니다. 프랑스는 소비자법의 표시·언어 규정을 더하고, 스페인은 Real Decreto 928/1987, 일본은 가정용품 품질 표시법으로 조성·세탁 표시·표시자를, 한국은 품질경영 및 공산품 안전관리법으로 품질 표시와 원산지를 요구합니다. 선반에 3년 둔다고 적합해지지 않습니다.",
    }),

    ("callout", {
        "zh": "一句話原則：留用前先做一次合規重檢——成分、洗護符號、原產地、責任主體四項只要有一項變了，這批料就該走銷毀或改造，而不是回倉。",
        "en": "The rule in one line: re-check compliance before you hold anything. If composition, care symbols, origin or responsible person has changed, the stock goes to destruction or rework, not back to the rack.",
        "fr": "La règle en une ligne : revérifiez la conformité avant de conserver. Si composition, symboles d'entretien, origine ou responsable ont changé, le stock part en destruction ou en transformation, pas au rayon.",
        "es": "La regla en una línea: revisa la conformidad antes de guardar. Si cambian composición, símbolos de cuidado, origen o responsable, el stock va a destrucción o transformación, no a la estantería.",
        "ja": "原則は 1 行。保管前にコンプライアンスを再確認すること。組成・洗濯表示・原産国・責任者のどれかが変わったら、棚に戻さず廃棄か改造へ回します。",
        "ko": "원칙은 한 줄입니다. 보관 전에 컴플라이언스를 다시 확인하십시오. 혼용률, 세탁 표시, 원산지, 책임자 중 하나라도 바뀌었다면 선반이 아니라 폐기나 개조로 보냅니다.",
    }),

    ("h2", {
        "zh": "五、倉儲成本與失效期：留多久才不划算",
        "en": "5. Storage Cost and Shelf Life: When Holding Stops Paying",
        "fr": "5. Stockage et durée de vie : quand conserver ne paie plus",
        "es": "5. Almacenaje y vida útil: cuándo deja de compensar",
        "ja": "5. 保管コストと寿命：いつ保管が不利になるか",
        "ko": "5. 보관 비용과 수명: 언제 보관이 손해인가",
    }),

    ("p", {
        "zh": "倉儲不是免費的。一般第三方倉每立方米每月 6–10 美元，加上盤點與搬運工時；更重要的是環境：紙製品在相對濕度 60% 以上容易起波浪與霉斑，金屬件在潮濕環境下 3–6 個月就出現鏽點，背膠與熱熔膠超過 30 °C 老化明顯加快。所以留用的成本應該這樣算：倉儲費加兩次盤點工時，再加上「這批料有幾成機率真的會被用到」。機率低於 50% 時，改造或銷毀通常比留用便宜。",
        "en": "Storage is not free. Third-party warehousing runs about 6–10 dollars per cubic metre per month, plus counting and handling time. The environment matters more: paper cockles and mildews above 60% relative humidity, metal parts show rust within 3–6 months in damp conditions, and pressure-sensitive adhesive ages markedly above 30 °C. Cost the hold as storage plus two stock counts plus the probability that the stock is actually used again. Below roughly 50%, rework or destruction is usually cheaper.",
        "fr": "Le stockage n'est pas gratuit. Un entrepôt tiers coûte 6 à 10 dollars par mètre cube et par mois, plus le temps de comptage et de manutention. L'environnement pèse davantage : le papier gondole et moisit au-delà de 60 % d'humidité relative, le métal rouille en 3 à 6 mois en milieu humide, et l'adhésif vieillit nettement au-delà de 30 °C. Chiffrez la conservation comme stockage plus deux inventaires plus la probabilité réelle de réemploi. Sous 50 %, transformation ou destruction reviennent généralement moins cher.",
        "es": "Almacenar no es gratis. Un almacén externo cuesta 6–10 dólares por metro cúbico al mes, más tiempo de inventario y manipulación. El entorno pesa más: el papel se ondula y enmohece por encima del 60 % de humedad relativa, el metal muestra óxido en 3–6 meses en ambiente húmedo y el adhesivo envejece de forma notable por encima de 30 °C. Calcula el guardado como almacenaje más dos inventarios más la probabilidad real de reutilización. Por debajo del 50 %, transformar o destruir suele salir más barato.",
        "ja": "保管は無料ではありません。外部倉庫は 1 立方メートルあたり月 6〜10 ドル、加えて棚卸しと荷役の工数がかかります。環境の影響はもっと大きく、紙は相対湿度 60 % を超えると波打ちとカビが出やすく、金属は湿気下で 3〜6 か月で錆が出て、粘着剤は 30 °C を超えると劣化が加速します。保管コストは、保管料＋棚卸し 2 回＋実際に使う確率で見積もります。確率が 5 割を下回るなら、改造か廃棄のほうが安いことが多いです。",
        "ko": "보관은 무료가 아닙니다. 외부 창고는 세제곱미터당 월 6~10달러에 재고 조사와 하역 작업이 더해집니다. 환경 영향이 더 큽니다. 종이는 상대습도 60%를 넘으면 물결과 곰팡이가 생기고, 금속은 습한 환경에서 3~6개월이면 녹이 피며, 점착제는 30 °C를 넘으면 노화가 빨라집니다. 보관 비용은 보관료 + 재고 조사 2회 + 실제 사용 확률로 계산합니다. 확률이 50%를 밑돌면 개조나 폐기가 더 저렴합니다.",
    }),

    ("p", {
        "zh": "實務折衷：把庫存分成三堆。A 堆是下一季確定復用的款式（設計沒改、法規沒變），留；B 堆是設計延續但顏色或版號變了，走改造；C 堆是客戶已取消且無復用計劃的，走銷毀並取第三方證書。三堆用不同顏色標籤，並在 ERP 或料卡上寫明處置狀態，半年後才不會有人從架上拿錯。",
        "en": "A workable compromise is to split the stock three ways. Stack A is confirmed for next season with no design or rule change, so hold it. Stack B kept the design but changed colour or version, so it goes to rework. Stack C is cancelled with no reuse plan, so it goes to destruction with a third-party certificate. Label the three with different colours and record the disposition in the ERP or bin card, or somebody pulls the wrong carton six months later.",
        "fr": "Le compromis praticable est de diviser le stock en trois. Lot A confirmé pour la saison suivante, sans changement de design ni de règle : on conserve. Lot B dont le design continue mais la couleur ou la version a changé : transformation. Lot C annulé sans projet de réemploi : destruction avec attestation d'un tiers. Étiquetez les trois avec des couleurs différentes et consignez la décision dans l'ERP ou la fiche de casier, sinon quelqu'un prendra le mauvais carton six mois plus tard.",
        "es": "El compromiso práctico es dividir el stock en tres. El lote A está confirmado para la próxima temporada sin cambios de diseño ni de normas: se guarda. El lote B mantiene el diseño pero cambió color o versión: a transformación. El lote C está cancelado sin plan de reutilización: a destrucción con certificado de tercero. Etiqueta los tres con colores distintos y registra la decisión en el ERP o la ficha de estantería, o alguien cogerá la caja equivocada seis meses después.",
        "ja": "実務的な落としどころは 3 分割です。A はデザインも法規も変わらず来季の復用が確定した分で、保管します。B はデザインは継続だが色や版番号が変わった分で、改造へ回します。C は中止済みで復用予定がない分で、第三者証明を取って廃棄します。3 つを色分けし、処分状況を ERP や棚札に記録しないと、半年後に誰かが違う箱を取ります。",
        "ko": "실무적 타협은 세 갈래로 나누는 것입니다. A는 디자인과 규정 변화 없이 다음 시즌 재사용이 확정된 재고로 보관합니다. B는 디자인은 이어지지만 색상이나 버전이 바뀐 재고로 개조로 보냅니다. C는 취소되어 재사용 계획이 없는 재고로 제3자 증명을 받아 폐기합니다. 세 갈래를 다른 색으로 표시하고 ERP나 재고 카드에 처분 상태를 기록하지 않으면 반년 뒤 누군가 다른 상자를 꺼냅니다.",
    }),

    ("h2", {
        "zh": "六、決策清單",
        "en": "6. Decision Checklist",
        "fr": "6. Liste de décision",
        "es": "6. Lista de decisión",
        "ja": "6. 判断チェックリスト",
        "ko": "6. 결정 체크리스트",
    }),

    ("ul", [
        {
            "zh": "這批料帶不帶客戶商標？帶商標就只能留用或銷毀，不能轉售。",
            "en": "Does the stock carry a customer trademark? If yes, it is hold or destroy, never resale.",
            "fr": "Le stock porte-t-il une marque client ? Si oui, conservation ou destruction, jamais revente.",
            "es": "¿El stock lleva marca del cliente? Si sí, guardar o destruir, nunca revender.",
            "ja": "顧客商標が入っているか。入っていれば保管か廃棄のみで、転売はできません。",
            "ko": "고객 상표가 들어 있는가. 있으면 보관이나 폐기만 가능하고 재판매는 안 됩니다.",
        },
        {
            "zh": "下一季的設計會不會改？改了克重、寬度或顏色，留用價值立刻下降。",
            "en": "Will next season's design change? A change of GSM, width or colour drops the value of holding immediately.",
            "fr": "Le design de la saison suivante change-t-il ? Un changement de grammage, de largeur ou de couleur fait chuter la valeur de la conservation.",
            "es": "¿Cambiará el diseño la próxima temporada? Un cambio de gramaje, ancho o color reduce de inmediato el valor de guardar.",
            "ja": "来季のデザインが変わるか。坪量・幅・色が変われば、保管の価値はすぐ下がります。",
            "ko": "다음 시즌 디자인이 바뀌는가. 평량, 폭, 색상이 바뀌면 보관 가치가 즉시 떨어집니다.",
        },
        {
            "zh": "成分與洗護符號還符合當前法規嗎？不合規的庫存不能出貨。",
            "en": "Do composition and care symbols still meet current rules? Non-compliant stock cannot ship.",
            "fr": "Composition et symboles d'entretien sont-ils encore conformes ? Un stock non conforme ne peut pas partir.",
            "es": "¿Composición y símbolos de cuidado siguen cumpliendo la norma? El stock no conforme no puede salir.",
            "ja": "組成と洗濯表示は現行法規に合うか。不適合の在庫は出荷できません。",
            "ko": "혼용률과 세탁 표시가 현행 규정에 맞는가. 부적합 재고는 출고할 수 없습니다.",
        },
        {
            "zh": "背膠或熱熔膠還有多久保質期？低於 6 個月就不要再留。",
            "en": "How much adhesive shelf life is left? Under six months, stop holding.",
            "fr": "Quelle durée de vie reste-t-il à l'adhésif ? Sous six mois, arrêtez de conserver.",
            "es": "¿Cuánta vida útil le queda al adhesivo? Por debajo de seis meses, deja de guardar.",
            "ja": "粘着剤の残り寿命はどれくらいか。6 か月を切ったら保管をやめます。",
            "ko": "점착제 잔여 수명이 얼마인가. 6개월 미만이면 보관을 중단합니다.",
        },
        {
            "zh": "客戶要求銷毀證明嗎？品牌類客戶幾乎都要，事先問清楚再決定處理方式。",
            "en": "Does the customer require a destruction certificate? Branded clients almost always do, so ask before choosing the route.",
            "fr": "Le client exige-t-il une attestation de destruction ? Les clients de marque le demandent presque toujours : à vérifier avant de choisir.",
            "es": "¿El cliente exige certificado de destrucción? Las marcas casi siempre lo piden: pregúntalo antes de elegir la vía.",
            "ja": "顧客が廃棄証明を求めるか。ブランド系はほぼ必須なので、処理方法を決める前に確認します。",
            "ko": "고객이 폐기 증명을 요구하는가. 브랜드 고객은 거의 항상 요구하므로 처리 방법을 정하기 전에 확인합니다.",
        },
        {
            "zh": "處置決策有書面記錄嗎？沒有記錄，一年後同一批料會被當成新問題再討論一次。",
            "en": "Is the disposition written down? Without a record, the same carton is re-debated as a new problem a year later.",
            "fr": "La décision est-elle écrite ? Sans trace, le même carton sera rediscuté comme un nouveau problème un an plus tard.",
            "es": "¿La decisión está por escrito? Sin registro, la misma caja se debatirá como un problema nuevo un año después.",
            "ja": "処分の決定を書面に残したか。記録がないと 1 年後に同じ箱が新しい問題として再燃します。",
            "ko": "처분 결정이 문서로 남았는가. 기록이 없으면 1년 뒤 같은 상자가 새 문제로 다시 논의됩니다.",
        },
    ]),

    ("p", {
        "zh": "取消款的輔料庫存不是財務問題，而是流程問題：訂貨時寫清版號與用量、改版時同步清點、取消時立刻分類並記錄。做到這三點，庫存只會是「少量尾數」，不會變成一批需要開會討論的資產。",
        "en": "Leftover trims are a process problem before they are a finance problem: specify version and consumption when ordering, count when a revision happens, and classify and record the moment a style is cancelled. Do those three and the leftover stays a small tail, never a batch that needs a meeting.",
        "fr": "Les accessoires restants sont un problème de processus avant d'être un problème financier : spécifier version et consommation à la commande, compter lors d'une révision, classer et consigner dès l'annulation. Avec ces trois gestes, le reliquat reste une petite queue, jamais un lot qui exige une réunion.",
        "es": "Los accesorios sobrantes son un problema de proceso antes que financiero: especificar versión y consumo al pedir, contar cuando hay revisión y clasificar y registrar en cuanto se cancela. Con esos tres pasos el sobrante es una cola pequeña, nunca un lote que exige una reunión.",
        "ja": "余った副資材は財務の問題である前に、プロセスの問題です。発注時に版番号と使用量を明記し、改版時に棚卸しし、中止が決まった時点で分類して記録する。この 3 つで、余剰は小さな端数にとどまり、会議が必要な資産にはなりません。",
        "ko": "남은 부자재는 재무 문제이기 전에 프로세스 문제입니다. 발주 시 버전과 소요량을 명기하고, 개정 시 재고를 세고, 취소가 결정되는 즉시 분류해 기록하십시오. 이 세 가지면 잔량은 작은 꼬리로 남고 회의가 필요한 자산이 되지 않습니다.",
    }),

    ("related", [
        ("trim-scrap-destruction-certificate-guide.html", {
            "zh": "輔料報廢與銷毀證明：客戶審核要的那張紙",
            "en": "Trim scrap and destruction certificates: the paper an audit asks for",
            "fr": "Rebuts d'accessoires et attestations de destruction : le document exigé en audit",
            "es": "Desechos de accesorios y certificados de destrucción: el papel que pide una auditoría",
            "ja": "副資材の廃棄と破棄証明：監査で求められる書類",
            "ko": "부자재 폐기와 폐기 증명: 감사에서 요구하는 서류",
        }),
        ("garment-trims-inventory-management.html", {
            "zh": "輔料庫存管理：安全庫存與周轉",
            "en": "Trims inventory management: safety stock and turns",
            "fr": "Gestion des stocks d'accessoires : stock de sécurité et rotation",
            "es": "Gestión de inventario de accesorios: stock de seguridad y rotación",
            "ja": "副資材在庫管理：安全在庫と回転率",
            "ko": "부자재 재고 관리: 안전 재고와 회전율",
        }),
        ("trim-material-substitution-guide.html", {
            "zh": "輔料替代：換料前要驗的五件事",
            "en": "Trim substitution: five checks before you switch material",
            "fr": "Substitution d'accessoires : cinq contrôles avant de changer",
            "es": "Sustitución de accesorios: cinco controles antes de cambiar",
            "ja": "副資材の代替：切り替え前の 5 つの確認",
            "ko": "부자재 대체: 교체 전 다섯 가지 확인",
        }),
    ]),

    ("cta", (
        {
            "zh": "倉庫裡有一批取消款的吊牌、織唛或包裝袋？把品項、數量、是否帶客戶商標與下一季計劃發給我們，我們按四條路徑給一版回收率與風險評估，並列明哪些必須走銷毀取證。",
            "en": "Holding a cancelled style's tags, labels or bags? Send the items, quantities, whether they carry a customer trademark and next season's plan, and we will assess all four routes by recovery and risk, flagging what must go to certified destruction.",
            "fr": "Vous stockez les étiquettes ou sacs d'un modèle annulé ? Envoyez les articles, quantités, la présence d'une marque client et le plan de la saison suivante : nous évaluons les quatre voies en récupération et en risque, en signalant ce qui doit passer par une destruction attestée.",
            "es": "¿Guardas etiquetas o bolsas de un modelo cancelado? Envía artículos, cantidades, si llevan marca del cliente y el plan de la próxima temporada: evaluamos las cuatro vías por recuperación y riesgo y señalamos lo que debe ir a destrucción certificada.",
            "ja": "中止になった企画の下げ札・ネーム・袋が倉庫に残っていませんか。品目・数量・顧客商標の有無・来季の計画をお送りいただければ、4 ルートを回収率とリスクで評価し、証明付き廃棄が必要な品を明示します。",
            "ko": "취소된 스타일의 행택, 라벨, 봉투가 창고에 남아 있나요? 품목, 수량, 고객 상표 포함 여부, 다음 시즌 계획을 보내주시면 네 경로를 회수율과 리스크로 평가하고 증명 폐기가 필요한 품목을 표시해 드립니다.",
        },
        {
            "zh": "索取庫存處置評估 →",
            "en": "Request a stock disposition review →",
            "fr": "Demander une évaluation de sortie de stock →",
            "es": "Solicitar evaluación de disposición de stock →",
            "ja": "在庫処分の評価を依頼 →",
            "ko": "재고 처분 검토 요청 →",
        },
    )),
]
