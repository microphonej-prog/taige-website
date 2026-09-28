#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-09-28 晚間批次：把結構化內容規格渲染成正文 HTML（六語）。

用生成而非手寫，保證三件事：
1) 每個元素的預設文本與 data-zh 完全一致（check_new_posts 會逐元素比對）
2) 屬性值裡沒有裸雙引號、沒有裸 &（移動端 WebKit 崩潰的元凶）
3) 六語屬性順序一致：data-zh / data-en / data-ja / data-ko / data-fr / data-es

輸出：blog/_body_freight.html（出貨方式與物流）、blog/_body_qtytol.html（數量容差與備損）
用法: <python> _build_bodies_20260928_evening.py
"""
import re

LANGS = ("zh", "en", "ja", "ko", "fr", "es")
ORDER = ("data-zh", "data-en", "data-ja", "data-ko", "data-fr", "data-es")


def T(zh, en, ja, ko, fr, es):
    return (zh, en, ja, ko, fr, es)


def esc(s):
    """裸 & → &amp;（已在实体里的不重复转义）"""
    return re.sub(r'&(?!amp;|nbsp;|quot;|lt;|gt;|#\d+;)', '&amp;', s)


def attrs(t, extra=""):
    assert len(t) == 6, t
    out = []
    for name, val in zip(ORDER, t):
        v = esc(val).strip()
        assert '"' not in v, "属性值含裸双引号: %s" % v[:60]
        assert v, "空属性值"
        out.append('%s="%s"' % (name, v))
    return (extra + " " if extra else "") + " ".join(out)


def el(tag, t, cls="", indent=6):
    ex = ' class="%s"' % cls if cls else ""
    pad = " " * indent
    return "%s<%s%s>%s</%s>" % (pad, tag, ex and "" or "", "", tag) if False else \
        "%s<%s%s %s>%s</%s>" % (pad, tag, ex, attrs(t), esc(t[0]).strip(), tag)


def render(items):
    out = []
    for it in items:
        kind = it[0]
        if kind in ("h2", "h3", "p"):
            out.append(el(kind, it[1]))
        elif kind in ("ul", "ol"):
            out.append("      <%s>" % kind)
            for li in it[1]:
                out.append(el("li", li, indent=8))
            out.append("      </%s>" % kind)
        elif kind == "table":
            heads, rows = it[1], it[2]
            out.append("      <table>")
            out.append("        <thead>")
            out.append("          <tr>")
            for h in heads:
                out.append(el("th", h, indent=12))
            out.append("          </tr>")
            out.append("        </thead>")
            out.append("        <tbody>")
            for r in rows:
                out.append("          <tr>")
                for c in r:
                    out.append(el("td", c, indent=12))
                out.append("          </tr>")
            out.append("        </tbody>")
            out.append("      </table>")
        elif kind == "callout":
            out.append(el("div", it[1], cls="callout"))
        elif kind == "related":
            t = T("相关文章", "Related reading", "関連記事", "관련 글",
                  "Articles liés", "Artículos relacionados")
            out.append(el("h2", t))
            out.append("      <ul>")
            for href, lab in it[1]:
                out.append('        <li><a href="%s" %s>%s</a></li>'
                           % (href, attrs(lab), esc(lab[0]).strip()))
            out.append("      </ul>")
        elif kind == "cta":
            p, btn = it[1], it[2]
            out.append('      <div class="cta-box">')
            out.append(el("p", p, indent=8))
            out.append('        <a class="cta-btn" href="../contact.html" %s>%s</a>'
                       % (attrs(btn), esc(btn[0]).strip()))
            out.append("      </div>")
        else:
            raise SystemExit("未知元素 %s" % kind)
    return ('<section class="article-body">\n'
            '    <div class="container">\n\n'
            + "\n\n".join(out) +
            '\n\n    </div>\n  </section>\n')


# =====================================================================
# 文章一：服裝輔料出貨方式與物流方案
# =====================================================================
A1 = [
    ("p", T("辅料的体积不大、货值也不算高，但运费与时效往往直接决定成衣厂能不能赶上船期。同样一批吊牌与织唛，走快递三天到门、走空运一周到港、走海运拼箱要三到五周，物流成本可能差出好几倍；方式选错，省下来的运费常常赔在交期上。这篇把快递、空运、海运拼箱与海运整柜四种方式放在一张表里对比，再讲清体积重怎么算、贸易术语差在哪、怎么跟成衣大货拼柜，以及出货文件与最常见的几个坑。",
      "Trims are small and rarely high in value, yet freight cost and transit time decide whether a garment factory catches its vessel. The same batch of hang tags and woven labels arrives in three days by courier, in about a week by air, or in three to five weeks by LCL sea freight - at several times the cost in the other direction. Choose wrong and the money saved on freight is usually lost on the delivery date. This guide compares courier, air, LCL and FCL in one table, then works through volumetric weight, Incoterms, consolidating with the garment shipment, and the documents and mistakes that cause delays.",
      "副資材は小さく、単価も高くありません。それでも運賃とリードタイムは、縫製工場が船に間に合うかどうかを左右します。同じタグと織りラベルの一箱でも、宅配便なら 3 日で到着、航空便なら 1 週間前後、海上混載（LCL）なら 3〜5 週間。物流コストは数倍違うこともあります。選び方を誤ると、浮いた運賃以上を通期で失います。本記事は宅配便・航空便・海上混載・海上コンテナ（FCL）の 4 方式を一つの表で比較し、容積重量の計算、インコタームズの違い、アパレル本体との混載、出荷書類とよくある落とし穴を整理します。",
      "부자재는 부피가 작고 단가도 높지 않습니다. 그래도 운임과 리드타임은 봉제 공장이 선적 일정을 맞출 수 있는지를 좌우합니다. 같은 행택·직조 라벨 한 상자도 특송이면 3일, 항공이면 일주일, 해상 LCL이면 3~5주가 걸리며 물류비는 몇 배 차이가 납니다. 방식을 잘못 고르면 아낀 운임을 납기에서 잃습니다. 이 글은 특송·항공·해상 LCL·해상 FCL 네 가지 방식을 한 표에서 비교하고, 용적 중량 계산, 인코텀즈 차이, 완성복 화물과의 혼적, 출하 서류와 흔한 실수를 정리합니다.",
      "Les accessoires sont petits et de faible valeur, mais le coût et le délai de transport décident si l'atelier attrape son navire. Un même lot d'étiquettes arrive en trois jours par express, en une semaine par avion ou en trois à cinq semaines en groupage maritime, pour un coût plusieurs fois supérieur. Mal choisi, l'économie de fret se perd dans le délai. Ce guide compare express, aérien, groupage et conteneur complet dans un tableau, puis traite le poids volumétrique, les Incoterms, la consolidation avec la marchandise et les documents.",
      "Los accesorios son pequeños y de poco valor, pero el coste y el plazo del transporte deciden si el taller alcanza su buque. Un mismo lote de etiquetas llega en tres días por exprés, en una semana por avión o en tres a cinco semanas en grupaje marítimo, con un coste varias veces mayor. Si se elige mal, el ahorro en flete se pierde en la fecha de entrega. Esta guía compara exprés, aéreo, grupaje y contenedor completo en una tabla, y aborda el peso volumétrico, los Incoterms, la consolidación y los documentos.")),

    ("h2", T("1. 四种出货方式放在一张表里对比",
             "1. Four Freight Modes in One Table",
             "1. 4 つの輸送手段を一つの表で比較",
             "1. 네 가지 운송 방식을 한 표로 비교",
             "1. Quatre modes de transport dans un tableau",
             "1. Cuatro modos de envío en una tabla")),

    ("table",
     [T("出货方式", "Mode", "輸送手段", "운송 방식", "Mode", "Modo"),
      T("参考时效", "Typical transit", "目安の日数", "예상 소요", "Délai indicatif", "Plazo típico"),
      T("适合的数量级", "Typical scale", "適した数量規模", "적합한 규모", "Volume adapté", "Escala adecuada"),
      T("成本特点", "Cost profile", "コストの特徴", "비용 특성", "Profil de coût", "Perfil de coste"),
      T("最容易踩的坑", "Usual pitfall", "よくある落とし穴", "흔한 실수", "Piège fréquent", "Error frecuente")],
     [[T("国际快递", "International courier", "国際宅配便", "국제 특송", "Express international", "Exprés internacional"),
       T("3–7 天到门", "3-7 days, door", "3〜7 日で戸口", "3~7일 도어", "3 à 7 jours, porte", "3-7 días, puerta"),
       T("几十公斤以内", "Up to tens of kg", "数十 kg まで", "수십 kg 이내", "Jusqu'à quelques dizaines de kg", "Hasta decenas de kg"),
       T("单价最高，但省事", "Highest rate, least work", "単価は最高だが手間が少ない", "단가 최고, 절차 최소", "Tarif le plus élevé, le plus simple", "Tarifa máxima, mínima gestión"),
       T("超长超重加收附加费", "Oversize or overweight surcharges", "長さ・重量超過の追加料金", "과길이·과중량 할증", "Suppléments hors gabarit", "Recargos por sobredimensión")],
      [T("空运", "Air freight", "航空便", "항공 운송", "Fret aérien", "Flete aéreo"),
       T("7–12 天到港或到门", "7-12 days to airport or door", "7〜12 日で空港・戸口", "7~12일 공항/도어", "7 à 12 jours, aéroport ou porte", "7-12 días a aeropuerto o puerta"),
       T("一百公斤到一吨", "100 kg to 1 tonne", "100 kg〜1 t", "100kg~1톤", "100 kg à 1 tonne", "100 kg a 1 tonelada"),
       T("单位运费约为海运数倍", "Several times sea rates", "海上の数倍の単価", "해상의 몇 배", "Plusieurs fois le maritime", "Varias veces el marítimo"),
       T("目的港杂费与清关资料不清", "Unclear destination charges and customs file", "現地費用と通関書類の不明確さ", "현지 비용·통관 서류 불명확", "Frais à destination et dossier douanier flous", "Cargos en destino y documentos poco claros")],
      [T("海运拼箱", "LCL sea freight", "海上混載（LCL）", "해상 LCL", "Groupage maritime", "Grupaje marítimo"),
       T("3–5 周", "3-5 weeks", "3〜5 週間", "3~5주", "3 à 5 semaines", "3-5 semanas"),
       T("一两方到十几方", "1-2 to about 15 CBM", "1〜2 m3 から十数 m3", "1~2 CBM에서 15 CBM 내외", "De 1-2 à une quinzaine de m3", "De 1-2 a unos 15 m3"),
       T("按体积计费，单价低", "Charged by volume, low rate", "容積課金で単価は低い", "용적 과금, 단가 낮음", "Facturé au volume, tarif bas", "Se factura por volumen, tarifa baja"),
       T("目的港杂费常高于预期", "Destination charges exceed expectations", "現地費用が想定を超えやすい", "현지 비용이 예상 초과", "Frais de destination supérieurs au prévu", "Cargos en destino mayores de lo previsto")],
      [T("海运整柜", "FCL sea freight", "海上コンテナ（FCL）", "해상 FCL", "Conteneur complet", "Contenedor completo"),
       T("3–5 周，与拼箱接近", "3-5 weeks, close to LCL", "3〜5 週間（LCL と同等）", "3~5주, LCL과 비슷", "3 à 5 semaines, proche du groupage", "3-5 semanas, similar al grupaje"),
       T("十几方以上，或与成衣同柜", "Over about 15 CBM, or with the garments", "十数 m3 以上、または衣料と同コンテナ", "15 CBM 이상 또는 완성복 동일 컨테이너", "Plus de 15 m3 ou avec les vêtements", "Más de 15 m3 o junto a la prenda"),
       T("单位运费最低", "Lowest unit cost", "単価は最も安い", "단가 최저", "Coût unitaire le plus bas", "Coste unitario más bajo"),
       T("装箱利用率低白付空间", "Poor fill wastes paid space", "積載率が低いと空間分を無駄に払う", "적재율이 낮으면 공간 비용 낭비", "Un mauvais remplissage se paie", "Un mal llenado se paga")]]),

    ("h2", T("2. 先算体积重，再谈运费", "2. Work Out Volumetric Weight First",
             "2. まず容積重量を計算する", "2. 먼저 용적 중량부터 계산", "2. Calculer le poids volumétrique", "2. Primero el peso volumétrico")),
    ("p", T("辅料大多属于抛货：吊牌是成叠的纸、织唛与洗水标是成卷的带、包装袋是一大包空气。快递与空运按实重和体积重取大者计费，公式是长 × 宽 × 高（厘米）÷ 5000，部分渠道用 6000；海运拼箱则直接按立方米计费。一箱吊牌实重 15 公斤、体积 0.12 方，按 5000 折算就是 24 公斤的体积重——这就是为什么压紧打包能直接省钱。",
            "Most trims ship as volumetric cargo: hang tags are stacks of paper, woven and care labels are rolls of tape, poly bags are largely air. Courier and air charge whichever is greater, actual or volumetric weight, using length x width x height in centimetres divided by 5000, with 6000 on some routes; LCL is charged straight by cubic metre. A carton of hang tags weighing 15 kg at 0.12 CBM becomes 24 kg volumetric - which is why compressing the packing saves money directly.",
            "副資材の多くは容積貨物です。タグは紙の束、織りラベルと洗濯表示ラベルはロール、ポリ袋はほとんど空気です。宅配便と航空便は実重量と容積重量の大きい方を適用し、計算は縦 × 横 × 高さ（cm）÷ 5000（ルートにより 6000）。海上混載は立方メートル課金です。0.12 m3・実重 15 kg のタグの箱は、容積重量 24 kg になります。圧縮梱包がそのままコスト削減になる理由です。",
            "부자재는 대부분 용적 화물입니다. 행택은 종이 묶음, 직조·세탁 라벨은 롤, 비닐봉투는 대부분 공기입니다. 특송과 항공은 실중량과 용적 중량 중 큰 값을 적용하며 계산식은 가로 x 세로 x 높이(cm) ÷ 5000(일부 노선은 6000), 해상 LCL은 입방미터 기준으로 과금합니다. 0.12 CBM, 실중량 15kg인 행택 상자는 용적 24kg이 됩니다. 압축 포장이 곧 비용 절감인 이유입니다.",
            "La plupart des accessoires voyagent en fret volumétrique : les étiquettes sont des piles de papier, les tissés et étiquettes d'entretien des rouleaux, les sacs surtout de l'air. Express et aérien facturent le plus élevé du poids réel ou volumétrique, soit longueur x largeur x hauteur en cm divisé par 5000, parfois 6000 ; le groupage se facture au mètre cube. Un carton de 15 kg à 0,12 m3 devient 24 kg volumétriques : comprimer l'emballage fait donc gagner directement.",
            "La mayoría de los accesorios viajan como carga volumétrica: los colgantes son pilas de papel, los tejidos y etiquetas de cuidado son rollos, las bolsas son casi todo aire. Exprés y aéreo cobran el mayor entre peso real y volumétrico, con la fórmula largo x ancho x alto en cm dividido entre 5000, o 6000 en algunas rutas; el grupaje se factura por metro cúbico. Un cartón de 15 kg y 0,12 m3 pasa a 24 kg volumétricos: comprimir el embalaje ahorra directamente.")),
    ("ul", [
        T("询价时先问清按实重还是体积重、除数是多少", "Ask up front whether weight or volume applies and which divisor", "見積時に実重量か容積重量か、除数を確認する", "견적 시 실중량인지 용적 중량인지, 제수 값을 확인", "Demandez si le poids réel ou volumétrique s'applique, et quel diviseur", "Pregunta si aplica peso real o volumétrico y con qué divisor"),
        T("卷装比平铺装箱更省空间，取用稍麻烦，可与工厂约定", "Rolls beat flat packing on space, slightly less handy to pick", "ロールは平積みより省スペース、取り出しはやや不便", "롤 포장이 평포장보다 공간 효율이 좋지만 취급이 불편", "Les rouleaux gagnent en volume, un peu moins pratiques", "Los rollos ahorran volumen, algo menos prácticos"),
        T("包装袋先排气再装袋，体积能明显压缩", "Expel air from bags before cartoning to cut volume", "袋の空気を抜いてから箱詰めすると容積が減る", "봉투 공기를 빼고 포장하면 부피가 줄어듦", "Videz l'air des sacs avant la mise en carton", "Expulsa el aire de las bolsas antes de encajar"),
        T("一次出货量越大，海运的单位成本优势越明显", "The larger the shipment, the stronger the sea cost advantage", "一度の出荷量が大きいほど海上の単価優位が増す", "한 번 출하량이 클수록 해상 단가 이점이 커짐", "Plus l'envoi est gros, plus le maritime gagne", "Cuanto mayor el envío, mayor la ventaja marítima"),
    ]),

    ("h2", T("3. 贸易术语：EXW、FOB、CIF、DDP 差在哪",
             "3. EXW, FOB, CIF, DDP: Where They Differ",
             "3. インコタームズ：EXW / FOB / CIF / DDP の違い",
             "3. 인코텀즈: EXW, FOB, CIF, DDP의 차이",
             "3. EXW, FOB, CIF, DDP : où est la différence",
             "3. EXW, FOB, CIF, DDP: diferencias")),
    ("p", T("贸易术语决定谁订舱、谁付主运费、风险在哪一刻转移。辅料订单常见这四种，下单前先确认目的国能不能顺利清关，再决定谁来承担那一段。",
            "The Incoterm decides who books, who pays the main freight and when risk passes. These four cover most trims orders; check first that the destination clears smoothly, then agree who carries that leg.",
            "インコタームズは、誰が手配し、誰が本運賃を払い、リスクがいつ移るかを決めます。副資材ではこの 4 つが中心です。まず仕向国で問題なく通関できるかを確認し、その区間の負担を決めます。",
            "인코텀즈는 누가 선적을 예약하고 주 운임을 지불하며 위험이 언제 이전되는지를 정합니다. 부자재 주문에서는 이 네 가지가 대부분입니다. 먼저 목적국 통관이 원활한지 확인하고 해당 구간의 부담 주체를 정하십시오.",
            "L'Incoterm décide qui réserve, qui paie le fret principal et quand le risque est transféré. Ces quatre couvrent l'essentiel des commandes d'accessoires : vérifiez d'abord que la destination dédouane bien, puis qui porte ce tronçon.",
            "El Incoterm decide quién reserva, quién paga el flete principal y cuándo se transfiere el riesgo. Estos cuatro cubren casi todos los pedidos: comprueba primero que el destino despache bien y luego quién asume ese tramo.")),
    ("table",
     [T("术语", "Term", "用語", "조건", "Terme", "Término"),
      T("谁订舱与付主运费", "Booking and main freight", "手配と本運賃", "예약과 주 운임", "Réservation et fret principal", "Reserva y flete principal"),
      T("风险转移点", "Risk passes", "リスク移転", "위험 이전", "Transfert du risque", "Transferencia de riesgo"),
      T("对辅料订单的提示", "What it means for trims", "副資材でのポイント", "부자재 주문 시 유의점", "Ce que cela implique", "Qué implica")],
     [[T("EXW 工厂交货", "EXW ex works", "EXW 工場渡し", "EXW 공장 인도", "EXW à l'usine", "EXW en fábrica"),
       T("买方负责", "Buyer", "買い手", "매수인", "L'acheteur", "El comprador"),
       T("货物在工厂交付时", "On delivery at the factory", "工場で引き渡した時点", "공장 인도 시점", "À la remise à l'usine", "En la entrega en fábrica"),
       T("买方需自找货代，国内提货容易出空档", "Buyer needs its own forwarder; domestic pickup can stall", "買い手がフォワーダーを手配、国内集荷が滞りやすい", "매수인이 포워더를 구해야 하며 국내 픽업이 지연되기 쉬움", "L'acheteur fournit le transitaire, l'enlèvement peut traîner", "El comprador busca transitario; la recogida puede atascarse")],
      [T("FOB 装运港船上交货", "FOB free on board", "FOB 本船渡し", "FOB 본선 인도", "FOB franco à bord", "FOB franco a bordo"),
       T("卖方订舱，买方付主运费", "Seller books, buyer pays the freight", "売り手が手配、買い手が運賃", "매도인 예약, 매수인 운임", "Le vendeur réserve, l'acheteur paie", "El vendedor reserva, el comprador paga"),
       T("货物装上船", "When goods are on board", "本船に積み込んだ時点", "본선 적재 시점", "À la mise à bord", "Al cargar a bordo"),
       T("整柜与拼箱都用得最多，出口报关归卖方", "The most common for both LCL and FCL; export clearance is the seller's", "LCL も FCL も最多、輸出通関は売り手", "LCL·FCL 모두 가장 흔하며 수출 통관은 매도인", "Le plus courant en LCL comme en FCL, dédouanement export vendeur", "El más común en LCL y FCL; el despacho de exportación es del vendedor")],
      [T("CIF 成本加保险费加运费", "CIF cost, insurance and freight", "CIF 運賃保険料込み", "CIF 운임·보험료 포함", "CIF coût, assurance et fret", "CIF coste, seguro y flete"),
       T("卖方", "Seller", "売り手", "매도인", "Le vendeur", "El vendedor"),
       T("货物装上船", "When goods are on board", "本船に積み込んだ時点", "본선 적재 시점", "À la mise à bord", "Al cargar a bordo"),
       T("卖方付到目的港的运费与保险，目的港杂费通常仍归买方", "Seller pays freight and insurance to destination; local charges usually remain with the buyer", "売り手は仕向港までの運賃と保険を負担、現地費用は通常買い手", "매도인이 목적항 운임·보험 부담, 현지 비용은 보통 매수인", "Le vendeur paie fret et assurance jusqu'à destination, les frais locaux restent à l'acheteur", "El vendedor paga flete y seguro hasta destino; los cargos locales suelen ser del comprador")],
      [T("DDP 完税后交货", "DDP delivered duty paid", "DDP 関税込み渡し", "DDP 관세 지급 인도", "DDP droits acquittés", "DDP derechos pagados"),
       T("卖方", "Seller", "売り手", "매도인", "Le vendeur", "El vendedor"),
       T("货物在目的地交付", "On delivery at destination", "仕向地で引き渡した時点", "목적지 인도 시점", "À la livraison à destination", "En la entrega en destino"),
       T("最省事，也最考验卖方对目的国关税与合规的把握", "Easiest for the buyer, hardest on the seller's duty and compliance knowledge", "最も楽だが、売り手の関税・法令理解が問われる", "가장 편리하지만 매도인의 관세·규정 이해가 관건", "Le plus simple pour l'acheteur, le plus exigeant pour le vendeur", "Lo más cómodo para el comprador y lo más exigente para el vendedor")]]),

    ("h2", T("4. 与成衣大货拼柜：辅料厂能配合的三件事",
             "4. Consolidating with the Garment Shipment",
             "4. アパレル本体との混載で協力できる三つのこと",
             "4. 완성복 화물과의 혼적: 공장이 협조할 수 있는 세 가지",
             "4. Consolider avec la marchandise : trois points",
             "4. Consolidar con la prenda: tres puntos")),
    ("ul", [
        T("按成衣厂的箱规与箱嘜要求装箱，箱号与装箱单提前对齐", "Pack to the garment factory's carton spec and marks, matching carton numbers to the packing list", "アパレル工場の箱規格と箱マークに合わせ、箱番号とパッキングリストを事前に揃える", "완성복 공장의 박스 규격·마킹에 맞추고 박스 번호와 패킹리스트를 미리 맞춤", "Respectez le carton et le marquage de l'atelier, numéros alignés sur le packing list", "Sigue la especificación y marcas del taller, con números alineados al packing list"),
        T("辅料只占柜内一角时，加托盘边角固定，避免被压变形", "If trims take a corner of the container, brace them to avoid crushing", "コンテナの一角のみの場合、角を固定して潰れを防ぐ", "컨테이너 한쪽만 차지하면 모서리 고정으로 압착 방지", "Si les accessoires n'occupent qu'un angle, calez-les contre l'écrasement", "Si ocupan un rincón, calza la carga para evitar aplastamiento"),
        T("出货时间倒排：辅料要在大货装柜前若干天到指定仓库", "Work backwards: trims must reach the warehouse days before loading", "逆算して、荷積みの数日前に指定倉庫へ納入する", "역산하여 선적 며칠 전 지정 창고에 입고", "À rebours : livrer l'entrepôt quelques jours avant le chargement", "A la inversa: entrega en almacén días antes de la carga"),
    ]),
    ("p", T("拼柜最怕时间不同步：成衣厂的柜子到了，辅料还在路上。倒排时间表时，给生产、验货与内陆运输各留缓冲，并提前确认仓库的收货时间与节假日安排。",
            "The real risk in consolidation is timing: the container arrives and the trims are still in transit. Build buffer into production, inspection and inland haulage, and confirm warehouse receiving hours and holidays in advance.",
            "混載で最も怖いのは時間のずれです。コンテナが来たのに副資材がまだ輸送中、という事態になります。逆算表では生産・検品・内陸輸送に余裕を置き、倉庫の受入時間と休業日を事前に確認します。",
            "혼적에서 가장 위험한 것은 시간 불일치입니다. 컨테이너는 도착했는데 부자재는 아직 이동 중인 상황입니다. 역산 일정에 생산·검품·내륙 운송 여유를 두고 창고 입고 시간과 휴무일을 미리 확인하십시오.",
            "Le vrai risque du groupage est le décalage : le conteneur arrive, les accessoires roulent encore. Prévoyez des marges en production, contrôle et acheminement, et confirmez horaires et jours fériés de l'entrepôt.",
            "El riesgo real es el desfase: llega el contenedor y los accesorios siguen viajando. Deja margen en producción, inspección y transporte terrestre, y confirma horarios y festivos del almacén.")),

    ("h2", T("5. 出货单证与交接", "5. Shipping Documents and Handover",
             "5. 出荷書類と引き継ぎ", "5. 출하 서류와 인수인계",
             "5. Documents d'expédition et transmission", "5. Documentos de envío y traspaso")),
    ("ul", [
        T("商业发票与装箱单：品名、材质、数量、单箱重量与体积要和实物对得上", "Invoice and packing list must match the goods: description, material, quantity, carton weight and volume", "インボイスとパッキングリストは品名・材質・数量・箱重量・容積を実物と一致させる", "인보이스와 패킹리스트의 품명·재질·수량·박스 중량·용적이 실물과 일치해야 함", "Facture et packing list doivent correspondre : désignation, matière, quantité, poids et volume", "Factura y packing list deben coincidir: descripción, material, cantidad, peso y volumen"),
        T("原产地与必要声明按目的国要求，不要临时在吊牌或箱嘜上手写补充", "Origin and required statements per destination, never hand-written onto tags or cartons at the last minute", "原産地と必要な表示は仕向国の要件どおり、タグや箱への手書き追記は不可", "원산지와 필요 표시는 목적국 요건대로, 행택·박스에 즉석 수기 보충 금지", "Origine et mentions selon le pays, jamais ajoutées à la main sur les étiquettes", "Origen y menciones según destino, nunca añadidos a mano"),
        T("走空运或快递时，提前确认到货通知人与清关联系人", "For air or courier, name the arrival notice and customs contacts in advance", "航空・宅配便では到着通知先と通関担当を事前に指定", "항공·특송은 도착 통지처와 통관 담당자를 미리 지정", "En aérien ou express, désignez à l'avance les contacts d'arrivée et de douane", "En aéreo o exprés, designa con antelación los contactos de llegada y aduana"),
        T("出货后把箱号、毛净重、提单号一并发给买方，减少来回确认", "Send carton numbers, gross and net weight and the bill number in one go", "出荷後に箱番号・毛重量・B/L 番号をまとめて送る", "출하 후 박스 번호·총중량·B/L 번호를 한 번에 전달", "Envoyez ensemble numéros de carton, poids et numéro de connaissement", "Envía juntos números de cartón, pesos y número de conocimiento"),
    ]),

    ("h2", T("6. 常见的五个坑", "6. Five Mistakes Worth Avoiding",
             "6. よくある五つの落とし穴", "6. 자주 발생하는 다섯 가지 실수",
             "6. Cinq pièges fréquents", "6. Cinco errores frecuentes")),
    ("ul", [
        T("为省税低报货值：一旦被查验，延误与罚款远高于税金", "Under-declaring value to save duty: a customs check costs far more than the duty", "関税を抑えるための低申告：検査になると税金以上の損失", "관세 절감을 위한 저가 신고: 검사 시 세금보다 큰 손실", "Sous-déclarer pour économiser : un contrôle coûte bien plus que les droits", "Declarar de menos para ahorrar: un control cuesta más que el arancel"),
        T("只看主运费，忽略目的港杂费与派送费", "Comparing only the main freight and ignoring destination and delivery charges", "本運賃だけで現地費用や配送費を見落とす", "주 운임만 보고 현지 비용·배송비를 놓침", "Ne comparer que le fret principal, oublier les frais à destination", "Mirar solo el flete principal y olvidar los cargos en destino"),
        T("旺季爆舱：长假与年底前舱位紧张，价格与时效都会跳", "Peak-season space: prices and transit jump before holidays and year-end", "繁忙期のスペース不足：連休前と年末は価格も日数も跳ねる", "성수기 선복 부족: 연휴·연말에는 가격과 일정이 급등", "Manque de place en haute saison : prix et délais sautent avant les fêtes", "Falta de espacio en temporada alta: precios y plazos se disparan"),
        T("样品与大货混装：样品被抽检会拖住整柜放行", "Samples inside the bulk carton: a sample inspection holds the whole container", "サンプルと量産品の混載：サンプル検査でコンテナ全体が止まる", "샘플과 양산품 혼적: 샘플 검사로 컨테이너 전체 지연", "Échantillons avec la série : leur contrôle bloque le conteneur", "Muestras junto al lote: su control retiene el contenedor"),
        T("快递渠道对含液体或带电池的物件有限制，需提前说明", "Courier channels restrict liquids or items with batteries; declare them early", "宅配便は液体や電池入りに制限があるため事前申告が必要", "특송은 액체·배터리 포함 물품에 제한이 있어 사전 신고 필요", "Les express restreignent liquides et piles : déclarez-les", "Los exprés restringen líquidos y baterías: decláralos"),
    ]),

    ("callout", T("💡 省事的做法：把「货值不高、体积偏大、交期紧」这三个特征一次讲给供应商，让对方在报价时就给出快递、空运与海运三种方案和预计到达时间，再按成衣厂的装柜日倒推。选方式比的不是单价，而是总成本加风险。",
                  "💡 A practical habit: describe the shipment once - modest value, bulky, tight deadline - and ask for courier, air and sea options with arrival dates in the quotation. Then work back from the garment factory's loading date. You are comparing total cost plus risk, not a rate per kilo.",
                  "💡 実務的な工夫：単価は低いが容積が大きく通期が厳しい、と一度伝えれば、見積時に宅配便・航空便・海上便の三案と到着予定日を出してもらえます。あとはアパレル工場の荷積み日から逆算するだけです。比べるのは単価ではなく、総コストとリスクです。",
                  "💡 실무 팁: 단가는 낮지만 부피가 크고 납기가 촉박하다는 점을 한 번에 전달하면 견적 시 특송·항공·해상 세 가지 안과 도착 예정일을 받을 수 있습니다. 이후 완성복 공장의 선적일에서 역산하십시오. 비교 대상은 단가가 아니라 총비용과 위험입니다.",
                  "💡 Bonne habitude : décrivez l'envoi une fois - valeur modérée, volumineux, délai serré - et demandez trois options express, aérien, maritime avec dates d'arrivée. Travaillez ensuite à rebours de la date de chargement. Comparez le coût total et le risque, pas un tarif au kilo.",
                  "💡 Una buena costumbre: describe el envío de una vez —valor moderado, voluminoso, plazo ajustado— y pide tres opciones exprés, aérea y marítima con fecha de llegada. Luego trabaja a la inversa desde la carga. Comparas coste total y riesgo, no una tarifa por kilo.")),

    ("related", [
        ("index.html", T("辅料 FAQ：全部文章", "Trims FAQ: all articles", "副資材 FAQ：すべての記事", "부자재 FAQ: 전체 글", "FAQ Accessoires : tous les articles", "FAQ Accesorios: todos los artículos")),
        ("garment-trims-sample-shipping-guide.html", T("样品寄送渠道怎么选：快递、包税专线还是邮政小包", "How to Send Samples: Courier, Duty-Paid Line or Post", "サンプル発送チャネルの選び方：宅配便・関税込みライン・郵便", "샘플 발송 채널 선택: 특송·관세 포함 라인·우편", "Envoyer des échantillons : express, ligne taxée ou poste", "Enviar muestras: exprés, línea con impuestos o correo")),
        ("garment-trunk-export-packaging.html", T("服装出口包装要求：内包装、外箱、托盘与装柜", "Export Packaging for Garments: Inner Packs, Cartons, Pallets", "衣料品の輸出梱包：内装・外箱・パレット・コンテナ詰め", "의류 수출 포장: 내포장·박스·팔레트·적재", "Emballage d'export : emballage intérieur, cartons, palettes", "Embalaje de exportación: interior, cartones, palés")),
        ("garment-trims-lead-time-guide.html", T("辅料交期指南：标准时间线与倒排计划", "Trims Lead Times: Standard Timeline and Working Backwards", "副資材の納期ガイド：標準スケジュールと逆算", "부자재 납기 가이드: 표준 일정과 역산 계획", "Délais des accessoires : calendrier type et rétroplanning", "Plazos de accesorios: calendario tipo y plan inverso")),
    ]),

    ("cta", T("需要按目的国与装柜日给出出货方案？把品类、预估体积与目的国发给我们，我们会同时给出快递、空运与海运的方案与预计到达时间；打样 3–7 天，大货 10–25 天，起订量灵活（吊牌 2000–3000 张试单、织唛 1000+、洗水标 300–500 起），可按色码分装并配合成衣厂的箱规装箱。",
              "Need a shipping plan built around destination and loading date? Send the item types, estimated volume and destination: we will quote courier, air and sea options with arrival dates. Samples in 3-7 days, bulk in 10-25 days, flexible minimums (hang tags from 2,000-3,000 for a trial run, woven labels from 1,000, care labels from 300-500), packed by colour and to the garment factory's carton spec.",
              "仕向国と荷積み日から輸送案が必要な場合は、品目・概算容積・仕向国をお送りください。宅配便・航空便・海上便の案と到着予定日をまとめて提示します。サンプル 3〜7 日、量産 10〜25 日、最小ロットは柔軟（タグは試験発注 2,000〜3,000 枚、織りラベル 1,000 枚〜、洗濯表示ラベル 300〜500 枚〜）。色別梱包と指定箱規格での箱詰めにも対応します。",
              "목적국과 선적일 기준의 운송안이 필요하면 품목·예상 용적·목적국을 보내주세요. 특송·항공·해상 안과 도착 예정일을 함께 제시합니다. 샘플 3~7일, 양산 10~25일, 최소 수량 유연(행택은 시험 발주 2,000~3,000장, 직조 라벨 1,000장~, 세탁 표시 라벨 300~500장~). 색상별 포장과 지정 박스 규격 포장도 가능합니다.",
              "Besoin d'un plan d'expédition selon la destination et la date de chargement ? Envoyez les articles, le volume estimé et la destination : nous proposons express, aérien et maritime avec dates d'arrivée. Échantillons en 3 à 7 jours, série en 10 à 25 jours, minimums souples (étiquettes dès 2 000-3 000 en essai, tissés dès 1 000, entretien dès 300-500), conditionnés par coloris et au format carton de l'atelier.",
              "¿Necesitas un plan de envío según destino y fecha de carga? Envía los artículos, el volumen estimado y el destino: proponemos exprés, aéreo y marítimo con fechas de llegada. Muestras en 3 a 7 días, producción en 10 a 25 días, mínimos flexibles (colgantes desde 2.000-3.000 en prueba, tejidos desde 1.000, cuidado desde 300-500), embalados por color y al formato de cartón del taller."),
     T("发送品类、体积与目的国，获取出货方案 →", "Send items, volume and destination for a shipping plan →", "品目・容積・仕向国を送り、輸送案を依頼 →", "품목·용적·목적국을 보내 운송안 요청 →", "Envoyez articles, volume et destination →", "Envía artículos, volumen y destino →")),
]

# =====================================================================
# 文章二：輔料訂單數量容差與備損率
# =====================================================================
A2 = [
    ("p", T("辅料订单最容易在「数量」上产生分歧：合同写 10000 张吊牌，交货 10300 张算不算超交？少了 200 张要不要补？印刷放数、织造损耗、裁切与抽检都会让实际数量与订单数不完全一致，行业里本来就有合理区间，但区间是多少、怎么写进合同、多出来或短掉的这部分谁承担，往往成了收货环节最费口舌的地方。这篇把数量差的来源、容差写法、备损率与补单规则一次讲清。",
      "Quantity is where trims orders most often disagree: the PO says 10,000 hang tags and 10,300 arrive - is that an over-run? Two hundred short - must they be replaced? Printing overs, weaving waste, cutting and sampling all make the delivered quantity differ from the order, and the industry works with sensible bands. What those bands are, how to write them into the contract, and who absorbs the excess or the shortfall is where receiving turns argumentative. This guide covers the sources of the gap, tolerance wording, spare rates and reorder rules.",
      "副資材の発注で最も揉めるのは数量です。注文書に 10,000 枚と書き、10,300 枚納品されたら過納なのか。200 枚不足したら補充が必要か。印刷の予備、織りのロス、断裁、抜き取り検査により、納品数量は発注数量と完全には一致しません。業界には妥当な範囲がありますが、その範囲、契約への書き方、超過分や不足分の負担を曖昧にすると、受入時に必ず揉めます。本記事は数量差の発生源、許容差の書き方、予備率、追加発注のルールを整理します。",
      "부자재 주문에서 가장 자주 다투는 부분은 수량입니다. 발주서에 10,000장이라 적고 10,300장이 오면 초과 납품인지, 200장이 부족하면 보충해야 하는지가 쟁점입니다. 인쇄 여유분, 직조 손실, 재단, 샘플링 때문에 실제 수량은 발주 수량과 정확히 일치하지 않으며 업계에는 합리적인 범위가 있습니다. 그 범위가 얼마인지, 계약서에 어떻게 쓰는지, 초과·부족분을 누가 부담하는지를 정하지 않으면 입고 단계에서 분쟁이 생깁니다. 이 글은 수량 차이의 원인, 허용 오차 표기, 예비율, 재발주 규칙을 정리합니다.",
      "C'est sur la quantité que les commandes d'accessoires se disputent le plus : le bon dit 10 000 étiquettes, il en arrive 10 300 - surplus ? Deux cents manquantes - à remplacer ? Les surplus d'impression, les pertes de tissage, la découpe et l'échantillonnage font toujours diverger la livraison de la commande, et le secteur travaille avec des plages raisonnables. Leur valeur, leur rédaction au contrat et la charge du surplus ou du manque sont les vraies sources de friction à la réception.",
      "Es en la cantidad donde más discrepan los pedidos de accesorios: el pedido dice 10.000 colgantes y llegan 10.300, ¿es un exceso? Faltan 200, ¿hay que reponerlos? Los sobrantes de impresión, las mermas de tejido, el corte y el muestreo hacen que lo entregado nunca coincida exactamente, y el sector trabaja con bandas razonables. Su valor, cómo redactarlas en el contrato y quién asume el exceso o el faltante son la verdadera fuente de fricción en la recepción.")),

    ("h2", T("1. 数量差从哪来：四个来源", "1. Where the Gap Comes From: Four Sources",
             "1. 数量差の発生源は四つ", "1. 수량 차이가 생기는 네 가지 원인",
             "1. D'où vient l'écart : quatre sources", "1. De dónde viene la diferencia: cuatro causas")),
    ("ul", [
        T("印刷与模切的放数：调机与走纸都有损耗，实际产出可能多于或少于下单量", "Printing and die-cutting overs: set-up and paper waste push actual output above or below the order", "印刷と抜き型の予備：段取りと紙のロスで実産数は上下する", "인쇄·타발 여유분: 세팅과 종이 손실로 실제 산출이 오르내림", "Surplus d'impression et de découpe : calage et gâche font varier la sortie", "Sobrantes de impresión y troquel: el ajuste y la merma hacen variar la salida"),
        T("织造与裁切损耗：织唛与洗水标在织造、染色、裁切、折边环节都会产生损耗", "Weaving and cutting waste: woven and care labels lose material at weaving, dyeing, cutting and folding", "織りと断裁のロス：織りラベルと洗濯表示ラベルは製織・染色・断裁・折りでロスが出る", "직조·재단 손실: 직조 라벨과 세탁 라벨은 제직·염색·재단·접힘에서 손실 발생", "Pertes de tissage et de découpe : tissés et étiquettes d'entretien perdent à chaque étape", "Mermas de tejido y corte: los tejidos y etiquetas pierden en cada paso"),
        T("抽检取样：AQL 抽检会取出样品，拆包后是否计入交货量要事先约定", "Sampling: AQL inspection removes pieces; agree whether opened cartons still count as delivered", "抜き取り検査：AQL で抜いた分を納品数に含めるか事前に決める", "샘플링: AQL 검사로 꺼낸 수량을 납품 수량에 포함할지 사전 합의", "Prélèvements : les pièces prélevées en AQL comptent-elles dans la livraison ?", "Muestreo: ¿las piezas extraídas en AQL cuentan como entregadas?"),
        T("分色分码与配件的点数误差：按色按码分装、成套配件时最容易漏计", "Counting errors by colour and size: sorting by colour-way and kitting is where counts slip", "色・サイズ別の仕分けと付属品の計数：最も数え間違いが起きやすい", "색상·사이즈 분류와 부속품 계수: 계산 착오가 가장 잦은 구간", "Comptage par coloris et taille, et assortiments : la source d'erreurs la plus fréquente", "Recuento por color y talla, y conjuntos: donde más se falla"),
    ]),

    ("h2", T("2. 容差写多少：常见区间与写法", "2. How Much Tolerance: Bands and Wording",
             "2. 許容差の目安と書き方", "2. 허용 오차 범위와 표기 방법",
             "2. Quelle tolérance : plages et rédaction", "2. Qué tolerancia: bandas y redacción")),
    ("p", T("容差不是供应商随口定的，而是围绕工艺损耗与设备最小批量谈出来的。下单前把每个品类的容差写进订单确认书，比到收货时再争论有效得多。下表是行业里常见的区间，具体仍要看工艺与分色数量。",
            "Tolerance is not something a supplier invents; it is negotiated around process waste and minimum machine batches. Writing the tolerance for each item type into the order confirmation beats arguing at receiving. The bands below are common in the trade, but the process and the number of colour-ways still decide.",
            "許容差は供給側が勝手に決めるものではなく、工程ロスと設備の最小ロットを前提に交渉して決めます。品目ごとに注文確認書へ明記するほうが、受入時の議論よりはるかに有効です。下表は業界でよく使われる範囲ですが、最終的には工程と色数によります。",
            "허용 오차는 공급자가 임의로 정하는 것이 아니라 공정 손실과 설비 최소 배치를 기준으로 협의해 정합니다. 품목별 허용 오차를 주문 확인서에 미리 명시하는 것이 입고 시 논쟁보다 훨씬 효과적입니다. 아래 범위는 업계에서 흔히 쓰이지만 공정과 색상 수에 따라 달라집니다.",
            "La tolérance ne s'invente pas : elle se négocie autour des pertes de fabrication et des lots minimaux machine. L'inscrire par article dans la confirmation de commande vaut mieux qu'en débattre à la réception. Les plages ci-dessous sont courantes, mais le procédé et le nombre de coloris décident.",
            "La tolerancia no se inventa: se negocia en función de las mermas del proceso y los lotes mínimos de máquina. Escribirla por artículo en la confirmación de pedido es mucho mejor que discutirla en la recepción. Las bandas siguientes son habituales, pero el proceso y los coloris mandan.")),
    ("table",
     [T("品类", "Item", "品目", "품목", "Article", "Artículo"),
      T("常见容差区间", "Usual tolerance", "一般的な範囲", "일반적 범위", "Plage usuelle", "Banda habitual"),
      T("说明", "Notes", "補足", "설명", "Remarques", "Notas")],
     [[T("吊牌（印刷加模切）", "Hang tags (print and die-cut)", "タグ（印刷＋抜き）", "행택(인쇄·타발)", "Étiquettes (impression et découpe)", "Colgantes (impresión y troquel)"),
       T("约 ±3% 到 ±5%", "about ±3% to ±5%", "おおむね ±3%〜±5%", "약 ±3%~±5%", "environ ±3% à ±5%", "aproximadamente ±3% a ±5%"),
       T("异形模切、烫金与压凹凸环节会再放数", "Shaped dies, foiling and embossing add their own overs", "異形抜き・箔押し・エンボスはさらに予備が増える", "이형 타발·박·엠보싱은 여유분이 더 필요", "Les formes spéciales, le dorage et le gaufrage ajoutent du surplus", "Las formas especiales, el dorado y el relieve añaden sobrantes")],
      [T("织唛（梭织与提花）", "Woven labels (woven and jacquard)", "織りラベル（製織・ジャカード）", "직조 라벨(제직·자카드)", "Tissés (tissé et jacquard)", "Tejidos (tejido y jacquard)"),
       T("约 ±5% 到 ±10%", "about ±5% to ±10%", "おおむね ±5%〜±10%", "약 ±5%~±10%", "environ ±5% à ±10%", "aproximadamente ±5% a ±10%"),
       T("织造与裁切损耗更高，色数多、灰度多时更明显", "Weaving and cutting waste is higher, worse with many colours or shades", "製織と断裁のロスが大きく、色数や階調が多いほど顕著", "제직·재단 손실이 크며 색상·음영이 많을수록 심함", "Pertes plus fortes, aggravées par le nombre de couleurs", "Mermas mayores, peores con muchos colores o matices")],
      [T("洗水标（织带与涂层）", "Care labels (tape and coated)", "洗濯表示ラベル（テープ・コーティング）", "세탁 표시 라벨(테이프·코팅)", "Étiquettes d'entretien (ruban et enduit)", "Etiquetas de cuidado (cinta y recubierta)"),
       T("约 ±5% 到 ±10%", "about ±5% to ±10%", "おおむね ±5%〜±10%", "약 ±5%~±10%", "environ ±5% à ±10%", "aproximadamente ±5% a ±10%"),
       T("按条或按卷交货时，按条数的误差通常略大", "Sold by piece or by roll, piece counts drift a little more", "枚数・ロール単位では計数の誤差がやや大きい", "장수·롤 단위는 계수 오차가 조금 더 큼", "À la pièce ou au rouleau, le comptage dérive un peu plus", "Por pieza o rollo, el recuento se desvía algo más")],
      [T("包装袋（胶袋与纸袋）", "Bags (poly and paper)", "袋（ポリ・紙）", "봉투(비닐·종이)", "Sacs (plastique et papier)", "Bolsas (plástico y papel)"),
       T("约 ±3% 到 ±5%", "about ±3% to ±5%", "おおむね ±3%〜±5%", "약 ±3%~±5%", "environ ±3% à ±5%", "aproximadamente ±3% a ±5%"),
       T("印刷与制袋同步放数，整箱计数便于核对", "Printing and bag-making overs run together; whole-carton counts are easy to check", "印刷と製袋は同時に予備を取る。箱単位の計数が最も確認しやすい", "인쇄·제대 여유분이 함께 발생, 박스 단위 계수가 확인에 유리", "Impression et fabrication vont ensemble ; le comptage par carton est facile", "Impresión y fabricación van juntas; contar por caja es sencillo")]]),
    ("p", T("写法上建议明确三点：容差按品类算还是按整单算；超出容差的部分怎么处理；以及是否允许分批交货凑数。这三点写清楚，验收就有依据。",
            "Three points are worth spelling out: whether tolerance applies per item or to the whole order; how the out-of-tolerance portion is handled; and whether split deliveries are allowed to make up the total. Get those in writing and receiving has a basis.",
            "書き方は三点を明確にします。許容差は品目単位か発注全体か。範囲を超えた分をどう扱うか。数量を合わせるための分割納入を認めるか。この三つが明確なら受入の根拠になります。",
            "표기 시 세 가지를 명확히 하십시오. 허용 오차가 품목별인지 전체 주문 기준인지, 범위를 벗어난 부분의 처리 방식, 수량을 채우기 위한 분할 납품 허용 여부입니다. 이 세 가지가 있으면 입고 근거가 됩니다.",
            "Trois points à préciser : la tolérance s'applique-t-elle par article ou à la commande entière, comment traiter le hors-tolérance, et les livraisons fractionnées sont-elles admises pour compléter. Écrits, ils fondent la réception.",
            "Conviene precisar tres puntos: si la tolerancia es por artículo o sobre el pedido completo, cómo se trata lo que excede la banda, y si se admiten entregas parciales para completar. Por escrito, la recepción tiene base.")),

    ("h2", T("3. 多交与少交分别怎么处理", "3. Handling Over-Runs and Shortfalls",
             "3. 過納と不足の扱い", "3. 초과 납품과 부족분 처리",
             "3. Traiter les surplus et les manquants", "3. Cómo tratar excesos y faltantes")),
    ("ul", [
        T("多交在容差内：通常照实验收结算，也可先约定多出部分按什么价格计价", "Over-run within tolerance: normally received and invoiced as delivered, with the unit price for the excess agreed up front", "範囲内の過納：通常は実数で検収・請求。超過分の単価を事前に決めておく", "범위 내 초과: 실수량으로 검수·정산, 초과분 단가를 미리 합의", "Surplus dans la tolérance : réceptionné et facturé au réel, prix de l'excédent convenu d'avance", "Exceso dentro de la banda: se recibe y factura al real, con precio del excedente pactado"),
        T("多交超出容差：买方有权只按订单量收货付款，超出部分由供应商自行处理", "Beyond tolerance: the buyer may receive and pay only the ordered quantity; the supplier handles the rest", "範囲を超える過納：発注数のみ検収・支払が可能で、超過分は供給側の負担", "범위 초과: 발주 수량만 검수·지급 가능하며 초과분은 공급자 부담", "Au-delà : l'acheteur peut ne réceptionner que la quantité commandée", "Más allá: el comprador puede recibir solo la cantidad pedida"),
        T("少交在容差内：一般不视为违约，按实收数量结算", "Shortfall within tolerance: not normally a breach, settled on the quantity received", "範囲内の不足：通常は契約違反とせず、実数で精算", "범위 내 부족: 보통 위반이 아니며 실수량 정산", "Manquant dans la tolérance : pas une faute, réglé sur le reçu", "Faltante dentro de la banda: no es incumplimiento, se liquida por lo recibido"),
        T("少交超出容差：先看是否影响成衣生产，能补则限期补足，无法补足按合同约定处理", "Beyond tolerance: check the impact on production first, top up within a deadline if possible, otherwise apply the contract remedy", "範囲を超える不足：生産への影響を確認し、可能なら期限付きで補充、不可なら契約に従う", "범위 초과 부족: 생산 영향 확인 후 기한 내 보충, 불가하면 계약 조항 적용", "Au-delà : vérifier l'impact sur la production, compléter sous délai si possible, sinon appliquer le contrat", "Más allá: ver el impacto en producción, completar con plazo si es posible o aplicar el contrato"),
        T("分批发货凑数：必须写明分批次数与每批到货时间，否则最后一批最容易扯皮", "Split deliveries: fix the number of shipments and each arrival date, or the last batch becomes the argument", "分割納入：回数と各回の納期を明記しないと最後の一回で揉める", "분할 납품: 횟수와 각 도착 시점을 명시하지 않으면 마지막 배치에서 분쟁", "Livraisons fractionnées : fixez le nombre et les dates, sinon la dernière tranche fait débat", "Entregas parciales: fija número y fechas, o el último lote se convierte en disputa"),
    ]),

    ("h2", T("4. 备损率怎么定：不是越多越好", "4. Setting the Spare Rate: More Is Not Better",
             "4. 予備率の決め方：多いほど良いわけではない", "4. 예비율 산정: 많을수록 좋은 것이 아님",
             "4. Fixer le taux de réserve : plus n'est pas mieux", "4. Fijar la reserva: más no es mejor")),
    ("p", T("备损率是给成衣生产留的保险，不是免费加量。按品类与工艺定比例，通常比一律加一成更省钱：常规印刷吊牌与洗水标一般在 1% 到 3%，织唛与需要手工装配的辅料一般在 2% 到 5%。备损部分建议单独包装并标注备品，收货时与主批分开点数，后续补件、查账都方便。",
            "A spare rate insures the sewing line; it is not free volume. Setting it by item and process usually costs less than adding a flat ten per cent: printed hang tags and care labels often sit at 1% to 3%, woven labels and hand-assembled trims at 2% to 5%. Pack spares separately and label them as spares so they can be counted apart from the main batch.",
            "予備率は縫製ラインのための保険であり、無料の増量ではありません。品目と工程ごとに決めるほうが、一律 1 割追加より安く済みます。通常の印刷タグと洗濯表示ラベルは 1%〜3%、織りラベルや手作業の多い副資材は 2%〜5% が目安です。予備分は別梱包し予備と明記すると、受入時に本体と分けて計数でき、後の補充や照合が楽になります。",
            "예비율은 봉제 라인의 보험이지 무료 증량이 아닙니다. 품목과 공정별로 정하는 편이 일률 10% 추가보다 비용이 적습니다. 일반 인쇄 행택과 세탁 라벨은 1%~3%, 직조 라벨과 수작업 조립 부자재는 2%~5%가 기준입니다. 예비분은 별도 포장하고 예비품으로 표기하면 입고 시 본 납품분과 분리 계수할 수 있어 보충과 대조가 쉽습니다.",
            "Le taux de réserve assure la ligne de couture ; ce n'est pas du volume gratuit. Le fixer par article et par procédé coûte souvent moins qu'un ajout uniforme de dix pour cent : 1% à 3% pour les étiquettes imprimées et d'entretien, 2% à 5% pour les tissés et les accessoires assemblés à la main. Emballez les réserves à part et étiquetez-les comme telles.",
            "La reserva asegura la línea de confección; no es volumen gratis. Fijarla por artículo y proceso suele costar menos que añadir un diez por ciento uniforme: 1% a 3% en colgantes impresos y etiquetas de cuidado, 2% a 5% en tejidos y accesorios armados a mano. Empaqueta la reserva aparte y márcala como tal.")),

    ("h2", T("5. 分色分码：真正的门槛在这里", "5. Colour-Ways and Size Break: The Real Threshold",
             "5. 色数とサイズ展開：本当のハードルはここ", "5. 색상·사이즈 분할: 실제 장벽은 여기",
             "5. Coloris et tailles : le vrai seuil", "5. Coloris y tallas: el umbral real")),
    ("p", T("整单 10000 张分四个颜色各 2500 张，与整单 10000 张单色，是两个完全不同的成本结构。印刷、烫金与织造的调机次数随颜色数量增加，因此每个颜色的最小量往往才是实际门槛。下单前先确认每个色码的最小量，再决定是否合并颜色或改用数码印刷。",
            "Ten thousand tags split into four colours of 2,500 is a different cost structure from ten thousand in one colour. Printing, foiling and weaving all need a new set-up per colour, so the minimum per colour-way is the real threshold. Confirm it before deciding whether to merge colour-ways or move to digital printing.",
            "10,000 枚を 4 色に各 2,500 枚と、10,000 枚 1 色ではコスト構造がまったく違います。印刷・箔押し・製織はいずれも色ごとに段取りが増えるため、実質的なハードルは色ごとの最小数量です。統合するかデジタル印刷に切り替えるかを決める前に、まず色別の最小量を確認します。",
            "10,000장을 네 색상 각 2,500장으로 나누는 것과 단색 10,000장은 비용 구조가 완전히 다릅니다. 인쇄·박·제직은 색상마다 세팅이 늘어나므로 실제 장벽은 색상별 최소 수량입니다. 색상을 합칠지 디지털 인쇄로 전환할지 결정하기 전에 색상별 최소량을 확인하십시오.",
            "Dix mille étiquettes en quatre coloris de 2 500 n'ont pas la même structure de coût que dix mille en une couleur. Impression, dorage et tissage ajoutent un calage par couleur : le minimum par coloris est le vrai seuil. Vérifiez-le avant de fusionner des coloris ou de passer au numérique.",
            "Diez mil colgantes en cuatro coloris de 2.500 no tienen la misma estructura que diez mil en un color. Impresión, dorado y tejido añaden un ajuste por color: el mínimo por coloris es el umbral real. Confírmalo antes de fusionar coloris o pasar a digital.")),
    ("ul", [
        T("每个色码的最小量越接近整体起订量，报价越接近量产价", "The closer each colour-way minimum is to the overall MOQ, the closer the price is to bulk", "色別の最小量が全体の MOQ に近いほど量産価格に近づく", "색상별 최소량이 전체 MOQ에 가까울수록 양산가에 근접", "Plus le minimum par coloris approche le MOQ global, plus le prix s'en approche", "Cuanto más cerca el mínimo por coloris del MOQ global, más cerca el precio"),
        T("颜色多而单色量少时，数码印刷或合理拼版有时更划算", "With many colours and small runs, digital printing or smart imposition can win", "色数が多く数量が少ない場合はデジタル印刷や適切な面付けが有利なことも", "색상이 많고 수량이 적으면 디지털 인쇄나 합리적 합판이 유리", "Beaucoup de coloris, petits volumes : numérique ou imposition judicieuse", "Muchos coloris y poco volumen: digital o imposición inteligente"),
        T("尺码标按码分装时，最小分装量也要一起确认", "If size labels are packed by size, agree the minimum per size too", "サイズラベルをサイズ別梱包する場合、サイズごとの最小量も確認", "사이즈 라벨을 사이즈별 포장하면 사이즈별 최소량도 확인", "Pour les étiquettes de taille conditionnées par taille, fixez aussi le minimum par taille", "Si las etiquetas de talla se embalan por talla, fija también el mínimo por talla"),
    ]),

    ("h2", T("6. 补单与翻单：什么情况可以少花版费", "6. Reorders: When You Can Skip the Plate Cost",
             "6. 追加発注：版代を抑えられる条件", "6. 재발주: 판 비용을 줄일 수 있는 조건",
             "6. Réassort : quand éviter les frais de forme", "6. Reposiciones: cuándo evitar el coste de plancha")),
    ("ul", [
        T("同一稿件、同一材质、同一工艺的翻单通常无需重新开版，但仍有最低起订量", "Same artwork, material and process usually need no new tooling, but a minimum still applies", "同じ版下・材質・工程の追加発注は通常、版の再作成は不要だが最小ロットは残る", "같은 시안·재질·공정의 재발주는 보통 판 재제작이 불필요하지만 최소 수량은 적용", "Même maquette, matière et procédé : pas de nouvelle forme, mais un minimum subsiste", "Mismo arte, material y proceso: sin plancha nueva, pero con mínimo"),
        T("补单数量过小时，供应商可能按最小起订量计价或加收开机费", "A very small top-up may be priced at the minimum or carry a set-up charge", "数量が少なすぎる追加は最小ロット価格や段取り費が付くことがある", "수량이 너무 적으면 최소 수량 가격 또는 세팅비가 붙음", "Un très petit complément peut être facturé au minimum ou avec un calage", "Un complemento muy pequeño puede ir al mínimo o llevar cargo de ajuste"),
        T("稿件或材质有改动就等于新单，容差与起订量都会重新计算", "Any change to artwork or material is a new order, with fresh tolerance and minimums", "版下や材質を変えれば新規発注となり、許容差も最小量も再計算", "시안·재질이 바뀌면 신규 주문이며 허용 오차와 최소 수량 재산정", "Toute modification devient une nouvelle commande, tolérance et minimum recalculés", "Cualquier cambio es un pedido nuevo, con tolerancia y mínimos recalculados"),
        T("需要长期备损件时，可在原订单里一次加定备品，比日后零散补单便宜", "If spares are needed long term, order them with the original PO rather than topping up piecemeal later", "長期的に予備が必要なら当初の発注にまとめて入れるほうが後日の小口追加より安い", "장기 예비품이 필요하면 최초 발주에 함께 넣는 편이 이후 소량 보충보다 저렴", "Pour des réserves durables, commandez-les avec la commande d'origine", "Si necesitas reserva a largo plazo, pídela con el pedido original"),
    ]),

    ("h2", T("7. 下单前一张数量表要写清的六项", "7. Six Things Your Quantity Sheet Should State",
             "7. 発注前の数量表に書くべき六項目", "7. 발주 전 수량표에 명시할 여섯 가지",
             "7. Six points à inscrire avant de commander", "7. Seis puntos antes de pedir")),
    ("ol", [
        T("每个品类的下单量与允许容差", "Ordered quantity and allowed tolerance per item", "品目ごとの発注数量と許容差", "품목별 발주 수량과 허용 오차", "Quantité commandée et tolérance par article", "Cantidad pedida y tolerancia por artículo"),
        T("是否分色分码，以及每个色码的最小量", "Whether colour-ways or sizes apply, and the minimum per combination", "色・サイズ展開の有無と組み合わせごとの最小量", "색상·사이즈 분할 여부와 조합별 최소량", "Coloris et tailles, avec minimum par combinaison", "Coloris y tallas, con mínimo por combinación"),
        T("备损率，以及备品是否单独包装标注", "Spare rate, and whether spares are packed and labelled separately", "予備率と、予備を別梱包・明記するか", "예비율과 예비품 별도 포장·표기 여부", "Taux de réserve et conditionnement séparé ou non", "Tasa de reserva y si se embala y marca aparte"),
        T("交货数量以哪一方的点数为准，如何复核", "Whose count governs delivery, and how it is verified", "納品数の計数はどちらを基準にし、どう確認するか", "납품 수량 기준 주체와 확인 방법", "Quel comptage fait foi et comment il est vérifié", "Qué recuento prevalece y cómo se verifica"),
        T("多交与少交的处理方式与结算口径", "How over-runs and shortfalls are handled and settled", "過納・不足の扱いと精算方法", "초과·부족 처리와 정산 기준", "Traitement et règlement des surplus et manquants", "Trato y liquidación de excesos y faltantes"),
        T("补单的最低数量，以及是否收取开机费或版费", "Minimum reorder quantity, and whether set-up or tooling is charged", "追加発注の最小数量と、段取り費・版代の有無", "재발주 최소 수량과 세팅비·판 비용 여부", "Minimum de réassort et frais de calage ou de forme", "Mínimo de reposición y cargos de ajuste o plancha"),
    ]),

    ("callout", T("💡 省事的做法：把「下单量、容差、分色最小量、备损率」四项写进同一张数量表，随稿件一起确认。数量口径提前说清，收货时就不需要靠人情解决。",
                  "💡 A practical habit: put ordered quantity, tolerance, minimum per colour-way and spare rate on a single quantity sheet confirmed with the artwork. Agree the counting rule up front and receiving needs no favours.",
                  "💡 実務的な工夫：発注数・許容差・色別最小量・予備率の四点を一枚の数量表にまとめ、版下と一緒に確認します。計数のルールを先に決めておけば、受入時に情状酌量は不要です。",
                  "💡 실무 팁: 발주 수량, 허용 오차, 색상별 최소량, 예비율 네 가지를 한 장의 수량표에 담아 시안과 함께 확인하십시오. 계수 기준을 미리 정하면 입고 시 사정에 기대지 않아도 됩니다.",
                  "💡 Bonne habitude : réunissez quantité, tolérance, minimum par coloris et taux de réserve sur une seule fiche validée avec la maquette. La règle de comptage étant fixée, la réception ne dépend plus des relations.",
                  "💡 Una buena costumbre: reúne cantidad, tolerancia, mínimo por coloris y reserva en una sola hoja validada con el arte. Con la regla de recuento fijada, la recepción no depende de favores.")),

    ("related", [
        ("index.html", T("辅料 FAQ：全部文章", "Trims FAQ: all articles", "副資材 FAQ：すべての記事", "부자재 FAQ: 전체 글", "FAQ Accessoires : tous les articles", "FAQ Accesorios: todos los artículos")),
        ("trim-order-quantity-unit-conversion.html", T("辅料订单数量单位换算：打、罗、个、套怎么算", "Trims Quantity Units: Dozens, Gross, Pieces and Sets", "副資材の発注数量単位：ダース・グロス・個・セット", "부자재 수량 단위: 다스·그로스·개·세트", "Unités de quantité : douzaine, grosse, pièce, lot", "Unidades de cantidad: docena, gruesa, pieza y juego")),
        ("hang-tag-moq-cost.html", T("吊牌起订量与成本解析：小批量试单怎么谈", "Hang Tag MOQ and Cost: Negotiating a Small Trial Run", "タグの最小ロットとコスト：小ロット試作の交渉", "행택 최소 수량과 비용: 소량 시험 발주 협상", "MOQ et coût des étiquettes : négocier un petit essai", "MOQ y coste de colgantes: negociar una prueba pequeña")),
        ("trim-order-contract-terms-guide.html", T("辅料订单合同条款指南：容易漏掉的几条", "Trims Order Contract Terms: The Clauses Buyers Miss", "副資材の契約条項：見落としやすい条項", "부자재 계약 조항: 놓치기 쉬운 항목", "Clauses de commande : celles que l'on oublie", "Cláusulas de pedido: las que se olvidan")),
    ]),

    ("cta", T("需要按分色与备损给出数量建议？把品类、每个颜色的数量与尺码分配发给我们，我们会给出容差与最小分色量的建议；打样 3–7 天，大货 10–25 天，起订量灵活（吊牌 2000–3000 张试单、织唛 1000+、洗水标 300–500 起），备品可单独包装标注，方便清点与补件。",
              "Need a quantity plan with colour-ways and spares? Send the item types, quantity per colour and size split: we will advise on tolerance and minimum per colour-way. Samples in 3-7 days, bulk in 10-25 days, flexible minimums (hang tags from 2,000-3,000 for a trial run, woven labels from 1,000, care labels from 300-500), spares packed and labelled for easy counting.",
              "色数と予備を踏まえた数量提案が必要な場合は、品目・色別数量・サイズ内訳をお送りください。許容差と色別最小量をご提案します。サンプル 3〜7 日、量産 10〜25 日、最小ロットは柔軟（タグは試験発注 2,000〜3,000 枚、織りラベル 1,000 枚〜、洗濯表示ラベル 300〜500 枚〜）。予備は別梱包・明記で計数と補充が容易です。",
              "색상과 예비를 반영한 수량 제안이 필요하면 품목, 색상별 수량, 사이즈 배분을 보내주세요. 허용 오차와 색상별 최소량을 제안합니다. 샘플 3~7일, 양산 10~25일, 최소 수량 유연(행택은 시험 발주 2,000~3,000장, 직조 라벨 1,000장~, 세탁 표시 라벨 300~500장~). 예비품은 별도 포장·표기로 계수와 보충이 쉽습니다.",
              "Besoin d'un plan de quantités avec coloris et réserves ? Envoyez les articles, la quantité par coloris et la répartition des tailles : nous conseillons tolérance et minimum par coloris. Échantillons en 3 à 7 jours, série en 10 à 25 jours, minimums souples (étiquettes dès 2 000-3 000 en essai, tissés dès 1 000, entretien dès 300-500), réserves emballées et étiquetées à part.",
              "¿Necesitas un plan de cantidades con coloris y reservas? Envía los artículos, la cantidad por color y el desglose de tallas: te asesoramos sobre tolerancia y mínimo por coloris. Muestras en 3 a 7 días, producción en 10 a 25 días, mínimos flexibles (colgantes desde 2.000-3.000 en prueba, tejidos desde 1.000, cuidado desde 300-500), reserva embalada y marcada aparte."),
     T("发送数量与分色方案，索取容差建议 →", "Send quantities and colour split for tolerance advice →", "数量と色内訳を送り、許容差の提案を依頼 →", "수량과 색상 구성을 보내 허용 오차 제안 요청 →", "Envoyez quantités et coloris pour un avis →", "Envía cantidades y coloris para asesoría →")),
]

if __name__ == "__main__":
    for path, items in (("blog/_body_freight.html", A1), ("blog/_body_qtytol.html", A2)):
        html = render(items)
        open(path, "w", encoding="utf-8", newline="").write(html)
        zh = re.sub(r"<[^>]+>", "", re.sub(r'data-(?:zh|en|ja|ko|fr|es)="[^"]*"', "", html))
        print("%-28s %6d 字节  正文汉字 %d"
              % (path, len(html.encode("utf-8")), len(re.findall(r"[\u4e00-\u9fff]", zh))))
