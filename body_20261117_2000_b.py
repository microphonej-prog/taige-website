# -*- coding: utf-8 -*-
"""2026-11-17 20:00 文章 B：辅料扣款（trim chargeback，英文主稿 + 五语翻译）"""


def d(zh, en, fr, es, ja, ko):
    return {"zh": zh, "en": en, "fr": fr, "es": es, "ja": ja, "ko": ko}


A2 = [
    ("p", d(
        "輔料扣款（trim chargeback）不是品質事故的同義詞，而是一套已經寫在採購合同裡的錢的動作：品牌先付貨款，再從下一張發票或保證金裡扣回來。對輔料廠來說，最難受的不是金額，而是扣款單往往在貨到港之後才出現，此時標籤已經縫在衣服上、吊牌已經掛在架上，任何補救都要按件計價。本文拆開扣款的五個觸發點、品牌怎麼算金額、以及出貨前該準備哪六份文件才能把錢守住。",
        "A trim chargeback is not a synonym for a quality incident. It is a money mechanism already written into the purchase contract: the brand pays the invoice, then takes part of it back from the next payment or from the deposit. What hurts a trim supplier is not the amount but the timing — the debit note usually arrives after the goods have landed, when the labels are already sewn into garments and the tags are already on the rail, so every remedy is priced per piece. This guide breaks down the five triggers, how brands build the number, and the six documents that protect your margin if they are ready before shipment.",
        "Un débit sur accessoires (trim chargeback) n'est pas synonyme d'incident qualité : c'est un mécanisme financier déjà inscrit au contrat. La marque paie la facture, puis en reprend une partie sur le paiement suivant ou sur le dépôt de garantie. Ce qui coûte cher au fournisseur, ce n'est pas le montant mais le moment : la note de débit arrive souvent après l'arrivée de la marchandise, quand les étiquettes sont déjà cousues et les étiquettes volantes déjà en rayon. Chaque remède se paie alors à la pièce. Ce guide détaille cinq déclencheurs, la façon dont la marque construit le montant, et les six documents à préparer avant expédition.",
        "Un cargo por accesorios (trim chargeback) no es sinónimo de incidente de calidad: es un mecanismo financiero ya escrito en el contrato. La marca paga la factura y luego recupera una parte del siguiente pago o del depósito. Lo que duele al proveedor no es el importe sino el momento: la nota de cargo suele llegar cuando la mercancía ya llegó, con las etiquetas cosidas y las etiquetas colgantes en el expositor, así que cualquier remedio se paga por pieza. Esta guía desglosa cinco detonantes, cómo se construye el importe y los seis documentos que conviene tener antes de embarcar.",
        "副資材の請求減額（trim chargeback）は品質事故の同義語ではありません。契約にすでに書き込まれた金銭の仕組みで、ブランドはいったん支払い、次の支払いや保証金から一部を取り戻します。サプライヤーにとって厳しいのは金額よりタイミングです。デビットノートは多くが入港後に届き、その時点でラベルは縫い込まれ、下げ札は売り場に掛かっています。補修はすべて枚数単価になります。本記事では 5 つの引き金、金額の組み立て方、出荷前に用意すべき 6 つの書類を整理します。",
        "부자재 차감(trim chargeback)은 품질 사고의 동의어가 아닙니다. 계약서에 이미 적혀 있는 금전 메커니즘으로, 브랜드가 대금을 지급한 뒤 다음 결제나 보증금에서 일부를 되가져갑니다. 공급사에게 괴로운 것은 금액이 아니라 시점입니다. 차감서는 대개 화물이 도착한 뒤에 오고, 그때는 라벨이 이미 봉제되어 있고 행택은 매장에 걸려 있어 어떤 보완도 개당 단가로 계산됩니다. 이 글은 다섯 가지 유발 요인, 브랜드의 금액 산정 방식, 출하 전에 준비해야 할 여섯 가지 문서를 정리합니다.",
    )),

    ("h2", d(
        "一、扣款的本質：一張有證據的借項通知",
        "1. What a Chargeback Really Is: A Debit Note With Evidence Behind It",
        "1. Ce qu'est vraiment un débit : une note de débit adossée à des preuves",
        "1. Qué es realmente un cargo: una nota de débito con pruebas",
        "1. 請求減額の実体：証拠を伴うデビットノート",
        "1. 차감의 실체: 증거가 붙은 차변표",
    )),
    ("p", d(
        "流程通常是這樣：品牌品保或合規部門在收貨檢驗、門店抽檢、或第三方報告中發現問題，發出一個索賠通知（claim notice），附照片、AQL 檢驗報告、裝箱單與條碼掃描紀錄；輔料廠有 5–10 個工作日回覆；回覆不被接受，品牌就開一張借項通知，從應付帳款或下一單訂金裡扣除，並在系統裡備註扣款原因碼。關鍵在於：扣款不需要經過你同意，但每一筆都掛著一個原因碼，而原因碼決定了能不能申訴。看不到原因碼的扣款單，幾乎一定可以要求重開。",
        "The sequence is usually this: QA or compliance finds the problem at goods-in, at a store audit or in a third-party report, and issues a claim notice with photos, an AQL inspection report, the packing list and barcode scan records. The supplier has five to ten working days to respond. If the response is not accepted, the brand raises a debit note, offsets it against payables or the next deposit, and records a reason code in its system. The key point: a chargeback does not need your consent, but every line carries a reason code, and the code decides whether it can be disputed. A debit note without a reason code is almost always worth asking to be reissued.",
        "La séquence est presque toujours la même : le service qualité ou conformité constate le problème à la réception, lors d'un audit en magasin ou dans un rapport tiers, et émet une réclamation avec photos, rapport AQL, liste de colisage et relevés de scan. Le fournisseur dispose de cinq à dix jours ouvrés pour répondre. Si la réponse n'est pas acceptée, la marque émet une note de débit, la compense sur les sommes dues ou sur l'acompte suivant, et enregistre un code motif. L'essentiel : le débit ne requiert pas votre accord, mais chaque ligne porte un code motif, et c'est ce code qui décide de la contestation possible. Une note sans code motif mérite presque toujours d'être redemandée.",
        "La secuencia suele ser esta: calidad o cumplimiento detecta el problema en la recepción, en una auditoría de tienda o en un informe de terceros, y emite un aviso de reclamación con fotos, informe AQL, lista de empaque y registros de escaneo. El proveedor tiene de cinco a diez días hábiles para responder. Si la respuesta no se acepta, la marca emite una nota de débito, la compensa contra las cuentas por pagar o el siguiente anticipo y registra un código de motivo. La clave: el cargo no necesita tu consentimiento, pero cada línea lleva un código de motivo, y ese código decide si se puede reclamar. Una nota sin código de motivo casi siempre conviene pedirla de nuevo.",
        "流れは概ね決まっています。品質保証またはコンプライアンスが入荷検査・店頭監査・第三者報告で問題を捉え、写真・AQL 検査報告・パッキングリスト・バーコード読取記録を添えてクレーム通知を出します。サプライヤーは 5〜10 営業日で回答します。回答が受理されなければ、ブランドはデビットノートを発行し、買掛金や次回の手付金から相殺し、理由コードをシステムに記録します。要点は、減額にあなたの同意は不要だが、各行には理由コードが付き、そのコードが異議申立ての可否を決めるということです。理由コードのないデビットノートは、再発行を求める価値がほぼ常にあります。",
        "보통 흐름은 이렇습니다. 품질보증 또는 컴플라이언스가 입고 검사·매장 감사·제3자 보고서에서 문제를 확인하고 사진, AQL 검사 보고서, 패킹리스트, 바코드 스캔 기록을 붙여 클레임 통지를 보냅니다. 공급사는 영업일 기준 5~10일 안에 답변합니다. 답변이 수용되지 않으면 브랜드는 차변표를 발행하고 매입채무나 다음 계약금에서 상계하며 사유 코드를 시스템에 남깁니다. 핵심은 차감에 귀사의 동의가 필요 없다는 점, 그러나 모든 항목에 사유 코드가 붙고 그 코드가 이의 제기 가능 여부를 결정한다는 점입니다. 사유 코드가 없는 차변표는 거의 항상 재발행을 요구할 가치가 있습니다.",
    )),

    ("h2", d(
        "二、五個觸發點與金額怎麼算",
        "2. The Five Triggers and How the Number Is Built",
        "2. Les cinq déclencheurs et la construction du montant",
        "2. Los cinco detonantes y cómo se construye el importe",
        "2. 5 つの引き金と金額の作り方",
        "2. 다섯 가지 유발 요인과 금액 산정",
    )),
    ("table", (
        [
            d("觸發點", "Trigger", "Déclencheur", "Detonante", "引き金", "유발 요인"),
            d("品牌查什麼", "What the brand checks", "Ce que la marque vérifie", "Qué comprueba la marca", "ブランドが確認する内容", "브랜드가 확인하는 항목"),
            d("扣款通常怎麼算", "How the deduction is usually built", "Comment le débit est calculé", "Cómo se suele calcular", "減額の算定方法", "차감 산정 방식"),
        ],
        [
            [
                d("標籤與吊牌文字錯誤", "Wording error on labels or tags", "Erreur de mention sur étiquettes ou étiquettes volantes", "Error de texto en etiquetas o colgantes", "ラベル・下げ札の表示誤り", "라벨·행택 문구 오류"),
                d("成分、原產國、尺碼、洗護符號、當地語言是否齊全", "Composition, origin, size, care symbols and local language all present", "Composition, origine, taille, symboles et langue locale", "Composición, origen, talla, símbolos e idioma local", "組成・原産国・サイズ・取扱記号・現地語の有無", "혼용률·원산지·사이즈·취급 기호·현지어 여부"),
                d("按件計罰，常見 0.5–3 美元/件，或整批重工的實際工時", "Per-piece penalty, often 0.5–3 USD per piece, or the actual rework hours for the batch", "Pénalité à la pièce, souvent 0,5 à 3 USD, ou heures de reprise réelles", "Penalización por pieza, a menudo 0,5–3 USD, o las horas reales de retrabajo", "枚数単価の違約金（多くの場合 0.5〜3 USD/枚）、または全数手直しの実工数", "개당 페널티(흔히 0.5~3 USD), 또는 전량 재작업 실공수"),
            ],
            [
                d("AQL 抽檢不合格", "AQL inspection failure", "Échec au contrôle AQL", "Fallo en la inspección AQL", "AQL 検査の不合格", "AQL 검사 불합격"),
                d("外觀、尺寸公差、色差（與核准樣比對）", "Appearance, dimensional tolerance, colour against the approved standard", "Aspect, tolérance dimensionnelle, écart de teinte vs témoin", "Aspecto, tolerancia dimensional, desviación de color vs patrón", "外観・寸法公差・承認見本との色差", "외관·치수 공차·승인 견본 대비 색차"),
                d("整批返工費＋延誤的物流費；AQL 2.5 抽樣下 1 件致命缺陷即可整批退回", "Rework of the lot plus expedited freight; under AQL 2.5 one critical defect can reject the lot", "Reprise du lot et fret express ; en AQL 2.5, un défaut critique suffit à refuser le lot", "Retrabajo del lote más flete urgente; con AQL 2.5 un defecto crítico basta para rechazar el lote", "ロット全数手直し＋特急运费。AQL 2.5 では致命欠陥 1 件でロット返品があり得る", "로트 전체 재작업 + 특급 운송비. AQL 2.5에서는 치명 결함 1건으로 로트 반품 가능"),
            ],
            [
                d("交期延誤", "Late delivery", "Retard de livraison", "Entrega tardía", "納期遅延", "납기 지연"),
                d("是否落在合同艙期內；是否影響上市日", "Whether it falls inside the contracted shipping window and hits the launch date", "Respect de la fenêtre d'embarquement et impact sur la date de lancement", "Si cae dentro de la ventana de embarque y afecta el lanzamiento", "契約の船積み期間内か、発売日に影響するか", "계약 선적 기간 내인지, 출시일에 영향이 있는지"),
                d("空運與海運差價＋門店缺貨損失，通常以整單金額百分比計", "Air-versus-sea freight difference plus lost sales, usually a percentage of the order value", "Écart fret aérien/maritime et pertes de vente, souvent un pourcentage de la commande", "Diferencia flete aéreo/marítimo y ventas perdidas, a menudo un porcentaje del pedido", "航空／海上運賃の差額＋欠品による機会損失。多くは受注額の百分比", "항공/해상 운임 차액 + 결품 손실. 대개 발주액 대비 비율"),
            ],
            [
                d("外箱嘜頭與裝箱單不符", "Carton marks that do not match the packing list", "Marquage carton non conforme au colisage", "Marcado de cajas que no coincide con el packing list", "外箱マークとパッキングリストの不一致", "외부 박스 마킹과 패킹리스트 불일치"),
                d("箱號、件數、淨重毛重、SKU 混裝順序", "Carton number, piece count, net and gross weight, SKU mixing order", "Numéro de carton, quantité, poids net et brut, ordre de mélange des SKU", "Número de caja, cantidad, peso neto y bruto, orden de mezcla de SKU", "箱番号・入数・正味／総重量・SKU の混載順", "박스 번호·입수·순중량/총중량·SKU 혼적 순서"),
                d("配送中心重新分揀的人工費，按箱計", "Recount and re-sort labour at the DC, charged per carton", "Main-d'oeuvre de recomptage au centre de distribution, facturée au carton", "Mano de obra de recuento en el centro de distribución, facturada por caja", "物流センターでの数え直し・仕分け直しの人件費（箱単価）", "물류센터 재검수·재분류 인건비(박스당)"),
            ],
            [
                d("測試報告缺失或過期", "Missing or expired test report", "Rapport d'essai manquant ou périmé", "Informe de ensayo ausente o caducado", "試験報告書の欠落・期限切れ", "시험 성적서 누락 또는 만료"),
                d("重金屬、偶氮染料、甲醛、鎳釋放、色牢度是否在有效期內", "Heavy metals, azo dyes, formaldehyde, nickel release, colour fastness within validity", "Métaux lourds, colorants azoïques, formaldéhyde, libération de nickel, solidité des couleurs", "Metales pesados, colorantes azoicos, formaldehído, liberación de níquel, solidez del color", "重金属・アゾ染料・ホルムアルデヒド・ニッケル溶出・染色堅牢度の有効性", "중금속·아조 염료·포름알데히드·니켈 용출·염색 견뢰도 유효성"),
                d("補測費用＋行政處理費；若已上架則含下架與銷毀成本", "Retest cost plus an admin fee; if already on the rail, delisting and destruction costs", "Coût de réessai et frais administratifs ; si déjà en rayon, dépose et destruction", "Coste de reensayo y gastos administrativos; si ya está en tienda, retirada y destrucción", "再試験費＋事務手数料。陳列後は撤去・廃棄費用も加算", "재시험 비용 + 행정 수수료. 진열 후에는 철수·폐기 비용 추가"),
            ],
        ],
    )),

    ("h2", d(
        "三、標籤錯誤佔最多，也最容易提前防住",
        "3. Labelling Causes the Largest Share — and It Is Preventable",
        "3. L'étiquetage pèse le plus lourd, et il se prévient",
        "3. El etiquetado pesa más que nada, y se puede prevenir",
        "3. 表示の誤りが最も多く、最も防げる",
        "3. 표시 오류가 가장 많고, 가장 예방 가능합니다",
    )),
    ("p", d(
        "在我們處理過的扣款案例裡，與標籤、吊牌文字相關的佔比最高，原因很單純：一個 SKU 出貨幾千件，每一件都帶著同一處錯誤，錯誤被複製了幾千次；而布料的色差只有部分批次受影響。最容易踩的坑有三類：第一類是成分比例與實際不符（例如標 100% 棉，實際混了 5% 彈性纖維），這在各市場都屬虛假標示；第二類是原產國判錯，面料與縫製分屬兩國時按縫製地認定；第三類是市場語言缺失——法國要求法定資訊以法語表述、西班牙要求西語、日本要求日語並載明混用率與原産国、韓國要求韓語並標原產地，只印英文的吊牌在這四個市場都算不合規。",
        "In the chargeback cases we have handled, labelling and tag wording account for the largest share, for a simple reason: one SKU ships in thousands of pieces and every piece carries the same error, so the mistake is replicated thousands of times, while a shade deviation only affects part of a lot. Three traps dominate. First, a fibre declaration that does not match reality, for example 100% cotton declared on a blend with 5% elastane, which counts as a false declaration in every market. Second, origin judged wrongly: when fabric and sewing sit in two countries, origin follows the sewing country. Third, the missing local language — France requires legal information in French, Spain in Spanish, Japan in Japanese with the fibre mix ratio and country of origin, Korea in Korean with origin marking, so an English-only tag is non-compliant in all four.",
        "Dans les dossiers que nous avons traités, l'étiquetage et les mentions des étiquettes volantes pèsent le plus lourd, pour une raison simple : un SKU part à plusieurs milliers de pièces et chaque pièce porte la même erreur, répétée des milliers de fois, alors qu'un écart de teinte n'affecte qu'une partie du lot. Trois pièges dominent. D'abord une composition déclarée fausse, par exemple 100 % coton sur un mélange contenant 5 % d'élasthanne : c'est une fausse déclaration sur tous les marchés. Ensuite une origine mal établie : quand tissu et confection sont dans deux pays, l'origine suit le pays de confection. Enfin la langue absente — la France exige les mentions obligatoires en français, l'Espagne en espagnol, le Japon en japonais avec le taux de mélange et le pays d'origine, la Corée en coréen avec marquage de l'origine. Une étiquette uniquement en anglais est non conforme dans ces quatre marchés.",
        "En los casos que hemos gestionado, el etiquetado y los textos de la etiqueta colgante son la partida más grande, por una razón simple: un SKU sale en miles de piezas y cada pieza lleva el mismo error, repetido miles de veces, mientras que una desviación de tono afecta solo a parte del lote. Dominan tres trampas. Primera, una composición declarada que no coincide con la realidad, por ejemplo 100 % algodón en una mezcla con 5 % elastano: es declaración falsa en todos los mercados. Segunda, origen mal determinado: si tejido y confección están en dos países, el origen sigue al país de confección. Tercera, el idioma ausente: Francia exige la información obligatoria en francés, España en español, Japón en japonés con el porcentaje de mezcla y el país de origen, Corea en coreano con marcado de origen; una etiqueta solo en inglés es no conforme en esos cuatro mercados.",
        "当社が扱った減額案件では、ラベル・下げ札の表示に関するものが最も多い。理由は単純で、1 SKU が数千枚出荷され、全枚に同じ誤りが載るため、誤りが数千回複製されるからです。色差はロットの一部にとどまります。つまずきやすいのは 3 類型です。第一に、実際と異なる混用率（例：エラスタン 5 % を含む混紡にコットン 100 % と表示）は、どの市場でも虚偽表示になります。第二に、原産国の判断誤り。生地と縫製が別国の場合、原産国は縫製国で判断されます。第三に、現地語の欠落。フランスは法定表示をフランス語で、スペインはスペイン語で、日本は日本語で混用率と原産国を、韓国は韓国語で原産地表示を求めます。英語だけの下げ札は、この 4 市場では不適合です。",
        "저희가 처리한 차감 사례에서 라벨·행택 문구 관련 비중이 가장 큽니다. 이유는 단순합니다. 한 SKU가 수천 장 출하되면 전량에 같은 오류가 실려 오류가 수천 번 복제됩니다. 색차는 로트 일부에만 영향을 줍니다. 세 가지 함정이 지배적입니다. 첫째, 실제와 다른 혼용률(예: 엘라스테인 5% 혼방에 면 100% 표시)은 어느 시장에서나 허위 표시입니다. 둘째, 원산지 판단 오류. 원단과 봉제가 다른 나라면 원산지는 봉제국 기준입니다. 셋째, 현지어 누락. 프랑스는 법정 정보를 프랑스어로, 스페인은 스페인어로, 일본은 일본어로 혼용률과 원산지를, 한국은 한국어로 원산지 표시를 요구합니다. 영어만 있는 행택은 이 네 시장에서 부적합입니다.",
    )),
    ("table", (
        [
            d("市場", "Market", "Marché", "Mercado", "市場", "시장"),
            d("法規或標準", "Rule or standard", "Règle ou norme", "Norma o regla", "法令・規格", "법규·표준"),
            d("對標籤與吊牌的具體要求", "What it forces onto the label or tag", "Ce que cela impose à l'étiquette", "Lo que impone a la etiqueta", "ラベル・下げ札への具体的な要求", "라벨·행택에 요구되는 구체 사항"),
        ],
        [
            [
                d("歐盟", "European Union", "Union européenne", "Unión Europea", "EU", "EU"),
                d("Règlement (UE) 1007/2011；GPSR (UE) 2023/988", "Regulation (EU) 1007/2011; GPSR (EU) 2023/988", "Règlement (UE) 1007/2011 ; GPSR (UE) 2023/988", "Reglamento (UE) 1007/2011; GPSR (UE) 2023/988", "規則 (EU) 1007/2011、GPSR (EU) 2023/988", "규정 (EU) 1007/2011, GPSR (EU) 2023/988"),
                d("成分、原產國、責任方名稱與可聯絡地址；只有品牌名沒有地址，視同未標。", "Composition, origin, and the responsible person's name with a reachable address; a brand name without an address counts as missing.", "Composition, origine, nom et adresse joignable du responsable ; un nom sans adresse équivaut à une absence.", "Composición, origen y nombre con dirección localizable del responsable; un nombre sin dirección equivale a no declararlo.", "組成・原産国・責任者の名称と連絡可能な住所。名称のみで住所がない場合は未表示とみなされます。", "혼용률·원산지·책임자 명칭과 연락 가능한 주소. 명칭만 있고 주소가 없으면 미표시로 간주됩니다."),
            ],
            [
                d("法國", "France", "France", "Francia", "フランス", "프랑스"),
                d("Code de la consommation；loi AGEC", "Code de la consommation; loi AGEC", "Code de la consommation ; loi AGEC", "Code de la consommation; loi AGEC (Francia)", "フランス消費法典、AGEC 法", "프랑스 소비자법전, AGEC법"),
                d("法定資訊以法語表述，字高不小於 1.5 mm；分類標識依品類適用。", "Legal information in French with a cap height of at least 1.5 mm; sorting marks apply by category.", "Mentions en français avec une hauteur de capitale d'au moins 1,5 mm ; signalétique de tri selon la catégorie.", "Información en francés con altura de mayúscula mínima de 1,5 mm; señalización de clasificación según categoría.", "法定表示はフランス語、文字高 1.5 mm 以上。分別表示は品目に応じて必要です。", "법정 정보는 프랑스어, 글자 높이 1.5 mm 이상. 분리배출 표시는 품목에 따라 적용됩니다."),
            ],
            [
                d("西班牙", "Spain", "Espagne", "España", "スペイン", "스페인"),
                d("Real Decreto Legislativo 1/2007；Reglamento (UE) 1007/2011", "Real Decreto Legislativo 1/2007; Regulation (UE) 1007/2011", "Real Decreto Legislativo 1/2007 ; Règlement (UE) 1007/2011", "Real Decreto Legislativo 1/2007; Reglamento (UE) 1007/2011", "Real Decreto Legislativo 1/2007、規則 (EU) 1007/2011", "Real Decreto Legislativo 1/2007, 규정 (EU) 1007/2011"),
                d("西語資訊；吊牌兼作價籤時須標單位價格，價格欄不小於 12 × 8 mm。", "Spanish wording; where the tag doubles as a price ticket the unit price is required and the price field needs at least 12 × 8 mm.", "Mentions en espagnol ; si l'étiquette sert de prix, le prix unitaire est exigé et la zone de prix doit faire au moins 12 × 8 mm.", "Texto en español; si la etiqueta hace de precio, se exige el precio por unidad y la zona de precio necesita al menos 12 × 8 mm.", "スペイン語表記。下げ札が値札を兼ねる場合は単位価格が必要で、価格欄は 12 × 8 mm 以上。", "스페인어 표기. 행택이 가격표를 겸하면 단위 가격이 필요하고 가격란은 12 × 8 mm 이상."),
            ],
            [
                d("日本", "Japan", "Japon", "Japón", "日本", "일본"),
                d("家庭用品品質表示法；JIS L 0001", "家庭用品品質表示法 (Household Goods Quality Labeling Act); JIS L 0001", "家庭用品品質表示法 (loi japonaise sur les mentions obligatoires) ; JIS L 0001", "家庭用品品質表示法 (ley japonesa de etiquetado); JIS L 0001", "家庭用品品質表示法、JIS L 0001", "家庭用品品質表示法(일본 가정용품 품질표시법), JIS L 0001"),
                d("混用率、取扱表示、事業者名、原産国；実務上文字高 1.5 mm 以上。", "Fibre mix ratio, care symbols, operator name and country of origin; 1.5 mm cap height in practice.", "Taux de mélange, symboles d'entretien, nom de l'opérateur et pays d'origine ; 1,5 mm de hauteur en pratique.", "Porcentaje de mezcla, símbolos, nombre del operador y país de origen; 1,5 mm de altura en la práctica.", "混用率・取扱表示・事業者名・原産国。実務では文字高 1.5 mm 以上。", "혼용률·취급 표시·사업자명·원산지. 실무상 글자 높이 1.5 mm 이상."),
            ],
            [
                d("韓國", "Korea", "Corée", "Corea", "韓国", "한국"),
                d("KS K 0021；표시광고법", "KS K 0021; 표시광고법 (Act on Fair Labeling and Advertising)", "KS K 0021 ; 표시광고법 (loi coréenne sur la publicité)", "KS K 0021; 표시광고법 (ley coreana de etiquetado y publicidad)", "KS K 0021、표시광고법（韓国表示広告法）", "KS K 0021, 표시광고법"),
                d("取扱記号、混用率、原産地；표시가 오인을 유발하면 표시광고법 위반이 됩니다.", "Care symbols, fibre mix and origin marking; wording that misleads becomes an infringement of 표시광고법.", "Symboles d'entretien, composition et marquage de l'origine ; une mention trompeuse constitue une infraction à 표시광고법.", "Símbolos de cuidado, composición y marcado de origen; un texto engañoso infringe 표시광고법.", "取扱記号・混用率・原産地。誤認を招く表示は 표시광고법 違反になります。", "취급 기호·혼용률·원산지. 오인을 유발하는 표시는 표시광고법 위반입니다."),
            ],
            [
                d("美國", "United States", "États-Unis", "Estados Unidos", "米国", "미국"),
                d("16 CFR Part 303", "16 CFR Part 303", "16 CFR Part 303", "16 CFR Part 303", "16 CFR Part 303", "16 CFR Part 303"),
                d("纖維含量、原產國、進口商或製造商身分；吊牌建議 300 g/m² 以上以免透印。", "Fibre content, origin and importer or manufacturer identity; use at least 300 g/m² stock to avoid show-through.", "Teneur en fibres, origine, identité de l'importateur ou du fabricant ; prévoir au moins 300 g/m² pour éviter la transparence.", "Contenido de fibras, origen e identidad del importador o fabricante; use al menos 300 g/m² para evitar transparencia.", "繊維含有率・原産国・輸入者または製造者の表示。透け防止に 300 g/m² 以上を推奨。", "섬유 함유율·원산지·수입자 또는 제조자 표시. 비침 방지를 위해 300 g/m² 이상 권장."),
            ],
        ],
    )),

    ("callout", d(
        "合規自查的順序：先確認銷售市場清單，再逐市場核對「語言 + 成分 + 原產國 + 責任方」四項，最後才處理價格欄與條碼。順序顛倒的結果是畫面排好了、法定文字放不下，只能重排一次——打樣費與交期都是這樣燒掉的。",
        "Order matters in a compliance check: confirm the list of selling markets first, verify the four items — language, composition, origin, responsible person — market by market, and only then place the price field and barcode. Do it the other way round and the layout is finished before the legal text is discovered not to fit, which means a second layout, a second proof and a lost week.",
        "L'ordre compte : confirmez d'abord la liste des marchés, vérifiez les quatre points — langue, composition, origine, responsable — marché par marché, et seulement ensuite placez la zone de prix et le code-barres. Dans l'autre sens, la maquette est terminée avant de découvrir que les mentions ne tiennent pas : deuxième maquette, deuxième épreuve, une semaine perdue.",
        "El orden importa: confirme primero la lista de mercados, verifique los cuatro puntos — idioma, composición, origen, responsable — mercado por mercado, y solo después coloque la zona de precio y el código de barras. Al revés, la maqueta está terminada antes de descubrir que el texto legal no cabe: segunda maqueta, segunda prueba, una semana perdida.",
        "順序が重要です。まず販売市場の一覧を確定し、次に「言語・組成・原産国・責任者」の 4 項目を市場ごとに確認し、最後に価格欄とバーコードを配置します。逆にすると、法定表示が入らないことに気づく前に組版が完成してしまい、再組版・再校正で 1 週間失います。",
        "순서가 중요합니다. 먼저 판매 시장 목록을 확정하고, 다음으로 언어·혼용률·원산지·책임자 네 항목을 시장별로 확인한 뒤, 마지막에 가격란과 바코드를 배치하십시오. 반대로 하면 법정 문구가 들어가지 않는다는 사실을 늦게 발견해 재조판과 재교정으로 일주일을 잃습니다.",
    )),

    ("h2", d(
        "四、出貨前就該備好的六份文件",
        "4. Six Documents to Have Ready Before Shipment",
        "4. Six documents à préparer avant expédition",
        "4. Seis documentos que deben estar listos antes de embarcar",
        "4. 出荷前に用意すべき 6 つの書類",
        "4. 출하 전에 준비해야 할 여섯 가지 문서",
    )),
    ("ul", [
        d("核准樣與簽字稿：客戶簽回的打樣實物 + 最終圖稿 PDF，註明核准日期與版本號。沒有這一項，任何「顏色不對」的指控都無法反駁。",
          "Approved sample and signed artwork: the physical proof the client signed back plus the final PDF, stamped with approval date and revision number. Without it, any claim of wrong colour cannot be rebutted.",
          "Épreuve approuvée et fichier signé : l'exemplaire physique retourné signé et le PDF final, avec date d'approbation et numéro de révision. Sans cela, aucune contestation de teinte ne peut être réfutée.",
          "Muestra aprobada y arte firmado: el ejemplar físico devuelto firmado y el PDF final, con fecha de aprobación y número de revisión. Sin esto no se puede rebatir ninguna objeción de color.",
          "承認見本と署名済み図案：客先が署名返却した現物と最終 PDF。承認日と版番号を明記します。これがないと色の指摘を反論できません。",
          "승인 견본과 서명 원고: 고객이 서명해 반송한 실물과 최종 PDF. 승인일과 버전 번호를 명기합니다. 이것이 없으면 색상 지적을 반박할 수 없습니다."),
        d("檢驗報告：AQL 抽檢紀錄（含抽樣數、缺陷分類、判定），以及該批的尺寸量測表；色差以 ΔE 數值附上，比「看起來差不多」有力得多。",
          "Inspection record: the AQL report with sample size, defect classification and verdict, plus the dimensional measurement sheet for the lot. Attach a delta E figure for colour; it carries far more weight than looking close enough.",
          "Rapport de contrôle : AQL avec taille d'échantillon, classification des défauts et décision, plus le relevé dimensionnel du lot. Joignez un écart delta E pour la teinte : c'est bien plus solide qu'un jugement visuel.",
          "Registro de inspección: informe AQL con tamaño de muestra, clasificación de defectos y veredicto, más la hoja de medición dimensional del lote. Añada un valor delta E para el color: pesa mucho más que un juicio visual.",
          "検査記録：AQL の抜取数・欠陥分類・判定に加え、ロットの寸法測定表。色は delta E の数値を添えます。目視の判断よりはるかに強い証拠になります。",
          "검사 기록: AQL 보고서(샘플 수, 결함 분류, 판정)와 로트 치수 측정표. 색상은 delta E 수치를 첨부하십시오. 육안 판단보다 훨씬 강한 증거입니다."),
        d("法定文字校對表：逐市場列出必須出現的欄位與其字高（例如 1.5 mm），並記錄由誰在何時確認。這張表就是將來爭議時的責任分界線。",
          "Legal wording checklist: per market, the fields that must appear and their minimum cap height, for example 1.5 mm, with who confirmed it and when. That sheet becomes the liability boundary in any later dispute.",
          "Liste de contrôle des mentions : par marché, les champs obligatoires et leur hauteur minimale, par exemple 1,5 mm, avec le nom de qui a validé et la date. Cette fiche devient la frontière de responsabilité en cas de litige.",
          "Lista de control de textos legales: por mercado, los campos obligatorios y su altura mínima, por ejemplo 1,5 mm, con quién lo confirmó y cuándo. Esa hoja se convierte en el límite de responsabilidad en cualquier disputa.",
          "法定表示チェック表：市場ごとに必須項目と最小文字高（例 1.5 mm）を列記し、誰がいつ確認したかを記録します。この表が後の紛争での責任分界になります。",
          "법정 문구 점검표: 시장별 필수 항목과 최소 글자 높이(예: 1.5 mm), 확인자와 확인 시점을 기록합니다. 이 표가 이후 분쟁의 책임 경계가 됩니다."),
        d("測試報告與有效期：重金屬、偶氮、甲醛、鎳釋放、色牢度。報告通常有效期 12 個月，跨年度訂單要提前確認能否沿用。",
          "Test reports with validity dates: heavy metals, azo dyes, formaldehyde, nickel release, colour fastness. Reports usually run twelve months, so a repeat order across the year boundary needs confirming early.",
          "Rapports d'essai et validité : métaux lourds, azoïques, formaldéhyde, nickel, solidité. La validité est souvent de douze mois : une commande à cheval sur deux exercices doit être vérifiée tôt.",
          "Informes de ensayo y validez: metales pesados, azoicos, formaldehído, níquel, solidez. Suelen valer doce meses, así que un pedido a caballo entre dos años debe confirmarse con tiempo.",
          "試験報告書と有効期限：重金属・アゾ染料・ホルムアルデヒド・ニッケル溶出・染色堅牢度。多くは有効期間 12 個月（1 年）で、年をまたぐ再注文は早めに確認が必要です。",
          "시험 성적서와 유효 기간: 중금속·아조 염료·포름알데히드·니켈 용출·염색 견뢰도. 대개 12개월 유효이므로 연도를 넘는 재주문은 미리 확인해야 합니다."),
        d("裝箱照片：外箱六面、嘜頭特寫、混裝分層照。這一項專治「嘜頭不符」的扣款，成本幾乎為零。",
          "Packing photos: all six faces of the carton, a close-up of the marks, and the layer-by-layer mixed packing. This one kills mark-mismatch chargebacks at almost no cost.",
          "Photos de colisage : les six faces du carton, un gros plan du marquage et le mélange couche par couche. Cela neutralise les débits pour marquage non conforme à coût quasi nul.",
          "Fotos de empaque: las seis caras de la caja, primer plano del marcado y la mezcla por capas. Esto neutraliza los cargos por marcado no conforme a coste casi nulo.",
          "梱包写真：外箱 6 面、マークの拡大、混載の層ごとの写真。マーク不一致の減額をほぼ無コストで防げます。",
          "포장 사진: 외부 박스 6면, 마킹 근접 촬영, 혼적 층별 사진. 마킹 불일치 차감을 거의 무비용으로 막습니다."),
        d("出貨前通知：把提單日期、箱數、毛重、預計到港日主動發給品牌，讓對方不必用「延誤」推定違約。",
          "Pre-shipment notice: send the bill of lading date, carton count, gross weight and ETA proactively, so the brand cannot infer a delay default.",
          "Avis avant expédition : transmettez spontanément la date du connaissement, le nombre de cartons, le poids brut et l'ETA, pour que la marque ne puisse pas présumer un retard.",
          "Aviso previo al embarque: envíe de forma proactiva la fecha del conocimiento de embarque, el número de cajas, el peso bruto y la ETA, para que la marca no presuma un incumplimiento.",
          "出荷前通知：B/L 日付・箱数・総重量・到着予定日を先方に送ります。遅延を推定される余地をなくせます。",
          "출하 전 통지: 선하증권 일자, 박스 수, 총중량, 도착 예정일을 먼저 보내십시오. 지연 위반으로 추정될 여지를 없앱니다."),
    ]),

    ("h2", d(
        "五、被扣款之後，什麼才有用",
        "5. After the Debit Note Lands: What Actually Works",
        "5. Une fois la note reçue : ce qui fonctionne vraiment",
        "5. Cuando llega la nota: qué funciona de verdad",
        "5. デビットノートが届いた後に効くこと",
        "5. 차변표가 도착한 뒤 실제로 통하는 것",
    )),
    ("p", d(
        "有效的申訴建立在三件事上：時間、對照、量化。時間指在合同規定的異議期內回覆（多數是收貨後 7–15 天），逾期即視為接受；對照指把爭議點拉回共同承認的基準——核准樣、簽字稿、合同附件；量化指給出可核算的數字，例如「這批 4,200 件中抽檢 200 件，缺陷 3 件，AQL 判定允收」，而不是「我們覺得沒問題」。實務上，能把這三件事在一封郵件裡講完的供應商，扣款被撤銷或折半的比例明顯更高；反之，只回一句「這不是我們的問題」幾乎一定失敗。",
        "An effective dispute rests on three things: timing, reference and quantity. Timing means replying inside the contractual objection window, usually seven to fifteen days from receipt; silence is acceptance. Reference means pulling the argument back to a jointly approved baseline — the signed sample, the signed artwork, the contract annex. Quantity means giving a number that can be recomputed, for example two hundred pieces sampled from a four-thousand-two-hundred-piece lot with three defects, which AQL accepts, rather than a statement that it looks fine to us. In practice, suppliers who put all three in one email recover far more of the deduction than those who reply that the problem is not theirs.",
        "Une contestation efficace tient à trois choses : le délai, la référence, la mesure. Le délai, c'est répondre dans la fenêtre contractuelle d'objection, souvent sept à quinze jours après réception ; le silence vaut acceptation. La référence, c'est ramener le débat à une base approuvée en commun — épreuve signée, fichier signé, annexe du contrat. La mesure, c'est un chiffre recomputable : deux cents pièces prélevées sur un lot de quatre mille deux cents, trois défauts, lot accepté selon l'AQL, plutôt qu'un jugement personnel. En pratique, les fournisseurs qui réunissent ces trois points dans un seul courriel récupèrent bien plus que ceux qui répondent que le problème n'est pas le leur.",
        "Una reclamación eficaz se apoya en tres cosas: plazo, referencia y medida. El plazo es responder dentro de la ventana contractual de objeción, a menudo siete a quince días desde la recepción; el silencio equivale a aceptación. La referencia es llevar el debate a una base aprobada en común: muestra firmada, arte firmado, anexo del contrato. La medida es un número recalculable: doscientas piezas muestreadas de un lote de cuatro mil doscientas, tres defectos, lote aceptado según AQL, en lugar de una opinión. En la práctica, los proveedores que reúnen los tres puntos en un solo correo recuperan mucho más que quienes responden que el problema no es suyo.",
        "有効な異議申立ては 3 点で決まります。時期・基準・数量です。時期は契約上の異議期間（多くは受領後 7〜15 日）内に回答すること。沈黙は承諾とみなされます。基準は、共通に承認した基準——署名済み見本、署名済み図案、契約別紙——に議論を戻すこと。数量は再計算できる数字を示すこと。たとえば 4,200 枚のロットから 200 枚を抜取り、欠陥 3 件で AQL 判定は合格、という形です。「問題ないと思う」では足りません。3 点を 1 通のメールにまとめられるサプライヤーは、そうでない場合より減額の取消・半減が明らかに多くなります。",
        "효과적인 이의 제기는 세 가지에 달려 있습니다. 시점, 기준, 수치입니다. 시점은 계약상 이의 기간(대개 수령 후 7~15일) 안에 답변하는 것이며, 침묵은 수용으로 간주됩니다. 기준은 공동 승인된 기준 — 서명 견본, 서명 원고, 계약 부속서 — 으로 논의를 되돌리는 것입니다. 수치는 재계산 가능한 숫자를 제시하는 것으로, 예컨대 4,200장 로트에서 200장을 표본 검사해 결함 3건, AQL 판정 합격이라는 형태입니다. '문제없다고 생각합니다'로는 부족합니다. 세 가지를 한 통의 메일로 정리하는 공급사가 그렇지 않은 경우보다 차감 취소·반감 비율이 뚜렷하게 높습니다.",
    )),
    ("callout", d(
        "把扣款風險前置到報價單：我們在報價時就把「法定文字校對由誰負責」「市場語言由誰提供」「測試報告由誰負擔」寫成三行備註。這三行不是法律條文，但能讓扣款單在發出前先被討論一次——被討論過的扣款，金額通常小一半。",
        "Move chargeback risk up into the quotation: we put three lines on every quote — who proofreads the legal wording, who supplies the market language, who pays for the test report. They are not contract clauses, but they force the debit note to be discussed before it is issued, and a discussed deduction usually shrinks by half.",
        "Faites remonter le risque au devis : nous inscrivons trois lignes sur chaque devis — qui relit les mentions légales, qui fournit la langue du marché, qui paie les essais. Ce ne sont pas des clauses, mais elles obligent à discuter le débit avant son émission, et un débit discuté diminue souvent de moitié.",
        "Suba el riesgo al presupuesto: incluimos tres líneas en cada oferta — quién revisa los textos legales, quién aporta el idioma del mercado, quién paga los ensayos. No son cláusulas, pero obligan a discutir el cargo antes de emitirlo, y un cargo discutido suele reducirse a la mitad.",
        "減額リスクを見積書の段階に前倒しします。当社は見積に 3 行を明記します。法定表示の校正は誰が行うか、市場言語は誰が用意するか、試験報告書は誰が負担するか。契約条項ではありませんが、デビットノートが発行される前に一度議論させる効果があり、議論された減額は多くの場合半減します。",
        "차감 위험을 견적 단계로 끌어올립니다. 저희는 견적서에 세 줄을 명시합니다. 법정 문구 교정을 누가 하는지, 시장 언어를 누가 제공하는지, 시험 성적서를 누가 부담하는지. 계약 조항은 아니지만 차변표가 발행되기 전에 한 번 논의하게 만들고, 논의된 차감은 대개 절반으로 줄어듭니다.",
    )),
]
