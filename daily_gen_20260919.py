#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-09-19 每日两篇：生成六语（zh/en/ja/ko/fr/es）文章页 + 列表页卡片 + sitemap 条目。

data-zh 先写简体，随后由 to_traditional.py --apply 统一转繁（全站当前为 zh-Hant），
再由 gen_i18n.py 生成 en/ja/ko/fr/es 静态页。
"""
import re
import os

SKEL = "blog/knitwear-sweater-trims-guide.html"
DATE_ISO = "2026-09-19"
L6 = ["zh", "en", "ja", "ko", "fr", "es"]

DATE_EN = "September 19, 2026"
DATE_ZH = "2026年9月19日"
DATE_JA = "2026年9月19日"
DATE_KO = "2026년 9월 19일"
DATE_FR = "19 septembre 2026"
DATE_ES = "19 de septiembre de 2026"

REL_ALL = D_ALL = None


def D(zh, en, ja, ko, fr, es):
    d = {"zh": zh, "en": en, "ja": ja, "ko": ko, "fr": fr, "es": es}
    for k, v in d.items():
        assert '"' not in v, "裸双引号：%s" % v[:60]
        bad = re.search(r'&(?!amp;|nbsp;|quot;|lt;|gt;|#\d+;)', v)
        assert not bad, "裸 & ：%s" % v[:60]
    return d


def attrs_line(d, indent):
    return " ".join('data-%s="%s"' % (k, d[k]) for k in L6)


def attrs_multiline(d, indent, tag):
    """属性分行，续行与首行属性对齐（与站内既有文章一致）"""
    head = "%s<%s " % (indent, tag)
    pad = " " * len(head)
    out = []
    for i, k in enumerate(L6):
        pre = head if i == 0 else pad
        out.append('%sdata-%s="%s"' % (pre, k, d[k]))
    return "\n".join(out)


def P(d, indent="      "):
    return "%s>%s</p>\n" % (attrs_multiline(d, indent, "p"), d["zh"])


def H2(d, indent="      "):
    return '%s<h2 %s>%s</h2>\n' % (indent, attrs_line(d, indent), d["zh"])


def H3(d, indent="      "):
    return '%s<h3 %s>%s</h3>\n' % (indent, attrs_line(d, indent), d["zh"])


def LI(d, indent="        "):
    return '%s<li %s>%s</li>\n' % (indent, attrs_line(d, indent), d["zh"])


def UL(items, tag="ul", indent="      "):
    s = "%s<%s>\n" % (indent, tag)
    for it in items:
        s += LI(it, indent + "  ")
    s += "%s</%s>\n" % (indent, tag)
    return s


def CALLOUT(d, indent="      "):
    return "%s>%s</div>\n" % (attrs_multiline(d, indent, 'div class="callout"').replace(
        'div class="callout" ', 'div class="callout" '), d["zh"])


def TABLE(head, rows, indent="      "):
    s = "%s<table>\n" % indent
    cells = "".join('<th %s>%s</th>' % (attrs_line(c, ""), c["zh"]) for c in head)
    s += "%s  <tr>%s</tr>\n" % (indent, cells)
    for r in rows:
        cells = "".join('<td %s>%s</td>' % (attrs_line(c, ""), c["zh"]) for c in r)
        s += "%s  <tr>%s</tr>\n" % (indent, cells)
    s += "%s</table>\n" % indent
    return s


# ---------------------------------------------------------------- 文章一
ART1_BLOCKS = [
    ("p", D(
        "辅料订单出问题，很少是工厂做不出来，而是规格书没说清。同样一句「白色棉绳吊牌」，对方可以理解成三种纸张、两种绳子、两种打孔位置。规格书（Spec Sheet，也叫辅料技术资料）的作用，就是在打样前把「我们要什么」变成可以核对、可以追溯的文字与数字。",
        "Trims orders rarely go wrong because a factory cannot make the part — they go wrong because the specification was never pinned down. The same phrase, a white hang tag with a cotton string, can mean three papers, two strings and two hole positions. A spec sheet exists to turn what you want into text and numbers your supplier can check against, before sampling starts.",
        "副資材のトラブルは、工場が作れないことより、仕様が伝わっていないことが原因です。「白い綿ひも付きタグ」という一文でも、紙3種・ひも2種・穴位置2通りに解釈できます。仕様書（Spec Sheet）の役割は、サンプル作成前に「何が欲しいか」を、照合できて追跡できる文字と数値に変えることです。",
        "부자재 주문 문제는 공장이 만들지 못해서보다 사양이 명확히 전달되지 않아서 생깁니다. '흰색 면끈 행택'이라는 한 문장도 종이 3가지, 끈 2가지, 타공 위치 2가지로 해석될 수 있습니다. 사양서(Spec Sheet)의 역할은 샘플 제작 전에 '무엇이 필요한지'를 확인하고 추적할 수 있는 문자와 숫자로 바꾸는 것입니다.",
        "Un accessoire rate rarement parce que l'usine ne sait pas le fabriquer, mais parce que la spécification n'a jamais été fixée. La même phrase, une étiquette suspendue blanche à cordon coton, peut désigner trois papiers, deux cordons et deux positions de perçage. Une fiche de spécifications sert à transformer ce que vous voulez en textes et en chiffres vérifiables avant l'échantillon.",
        "Un accesorio casi nunca falla porque la fábrica no sepa hacerlo, sino porque la especificación no se fijó. La misma frase, una etiqueta colgante blanca con cordón de algodón, puede significar tres papeles, dos cordones y dos posiciones de taladro. La ficha de especificaciones convierte lo que quieres en textos y cifras verificables antes de la muestra.",
    )),
    ("p", D(
        "下面的字段顺序与供应商排产顺序一致：材质、尺寸、颜色、工艺、文字、数量与包装、交期。照这个顺序填写，报价更快，打样一次通过率也更高。",
        "The field order below follows the way a supplier actually schedules production: material, size, colour, finishing, text, quantity and packing, lead time. Fill it in that order and quotations come back faster with fewer sampling rounds.",
        "以下の項目順は、サプライヤーが実際に生産を手配する順序（素材→寸法→色→加工→文字→数量と包装→納期）に対応しています。この順で記入すると、見積りが早く、サンプルの一発承認率も上がります。",
        "아래 항목 순서는 공급업체가 실제로 생산을 배정하는 순서(소재 → 치수 → 색상 → 가공 → 문자 → 수량과 포장 → 납기)와 같습니다. 이 순서대로 기재하면 견적이 빨리 오고 샘플 1차 승인율도 높아집니다.",
        "L'ordre des champs ci-dessous suit la façon dont un fournisseur planifie réellement : matière, dimensions, couleur, finitions, textes, quantité et conditionnement, délai. Remplissez-le dans cet ordre : les devis reviennent plus vite et l'échantillon est validé du premier coup plus souvent.",
        "El orden de los campos sigue el modo en que el proveedor planifica de verdad: material, medidas, color, acabados, textos, cantidad y embalaje, plazo. Rellénalo en ese orden y los presupuestos llegan antes y la muestra se aprueba a la primera más a menudo.",
    )),

    ("h2", D("1. 规格书、辅料手册、订单三者分工", "1. Spec Sheet, Trim Book, Purchase Order: Who Does What",
             "1. 仕様書・副資材ブック・発注書の役割分担", "1. 사양서·부자재 북·발주서의 역할 분담",
             "1. Fiche, trim book et bon de commande : qui fait quoi", "1. Ficha, trim book y pedido: quién hace qué")),
    ("p", D(
        "很多品牌把这三件事混在一封邮件里，最后谁也说不清哪句话是最终版本。分工其实很清楚：规格书管单件、辅料手册管成套、订单管商务。",
        "Many brands mix all three into one email and then nobody can tell which line is the final version. The division is simple: the spec sheet covers one item, the trim book covers the whole family, the purchase order carries the commercial terms.",
        "多くのブランドはこの3つを1通のメールに混ぜてしまい、どれが最終版か分からなくなります。役割は明確です。仕様書は単品、副資材ブックはシリーズ全体、発注書は商務条件を扱います。",
        "많은 브랜드가 이 세 가지를 한 통의 메일에 섞어 두었다가 어느 문장이 최종본인지 알 수 없게 됩니다. 역할은 분명합니다. 사양서는 단일 품목, 부자재 북은 시리즈 전체, 발주서는 상업 조건을 다룹니다.",
        "Beaucoup de marques mélangent les trois dans un seul e-mail et plus personne ne sait quelle ligne fait foi. La répartition est simple : la fiche décrit un article, le trim book décrit toute la famille, le bon de commande porte les conditions commerciales.",
        "Muchas marcas mezclan los tres en un solo correo y luego nadie sabe qué línea es la versión final. El reparto es claro: la ficha describe un artículo, el trim book toda la familia y el pedido las condiciones comerciales.",
    )),
    ("table", (
        [D("文件", "Document", "文書", "문서", "Document", "Documento"),
         D("主要作用", "What it does", "主な役割", "주요 역할", "Rôle principal", "Función principal")],
        [
            [D("规格书 Spec Sheet", "Spec sheet", "仕様書", "사양서", "Fiche de spécifications", "Ficha de especificaciones"),
             D("描述单件辅料的技术要求，随询价与打样需求发出", "Technical requirements for one item, sent with the RFQ and sample request",
               "単品の技術要件を記述し、見積依頼とサンプル依頼に添付", "단일 품목의 기술 요건을 기재해 견적·샘플 요청과 함께 발송",
               "Exigences techniques d'un article, envoyées avec la demande de prix et d'échantillon", "Requisitos técnicos de un artículo, junto a la solicitud de precio y muestra")],
            [D("辅料手册 Trim Book", "Trim book", "副資材ブック", "부자재 북", "Trim book", "Trim book"),
             D("汇总全系列编号、规格与封样，品牌内部与供应商共用", "All item numbers, specifications and sealed samples for the whole family",
               "シリーズ全体の品番・仕様・封入見本をまとめ、社内と取引先で共有", "시리즈 전체의 품번·사양·봉인 샘플을 정리해 내부와 공급업체가 공유",
               "Numéros, spécifications et échantillons scellés de toute la famille", "Números, especificaciones y muestras selladas de toda la familia")],
            [D("订单 PO", "Purchase order", "発注書", "발주서", "Bon de commande", "Pedido"),
             D("数量、单价、交期、付款与验收条款", "Quantity, unit price, lead time, payment and inspection terms",
               "数量・単価・納期・支払条件・検収条件", "수량·단가·납기·결제·검수 조건",
               "Quantité, prix unitaire, délai, paiement et conditions de contrôle", "Cantidad, precio unitario, plazo, pago y condiciones de inspección")],
        ])),
    ("p", D(
        "三份文件共用同一套编号，改动只在规格书里发生，订单只引用编号与版本号。这样任何时候都能回答一个问题：这批货是按哪一版做的。",
        "All three share one numbering system. Changes happen only in the spec sheet, and the PO merely cites the number and version. That way you can always answer one question: which version was this batch made to?",
        "3つの文書は同じ品番体系を共有します。変更は仕様書だけで行い、発注書は品番と版だけを引用します。これで「このロットはどの版で作られたか」に常に答えられます。",
        "세 문서는 같은 품번 체계를 공유합니다. 변경은 사양서에서만 하고, 발주서는 품번과 버전만 인용합니다. 그러면 언제든 '이 로트는 어느 버전으로 만들었는가'에 답할 수 있습니다.",
        "Les trois partagent une même numérotation. Seule la fiche évolue et le bon de commande ne cite que le numéro et la version. Vous saurez donc toujours à quelle version un lot a été fabriqué.",
        "Los tres comparten una misma numeración. Los cambios solo ocurren en la ficha y el pedido solo cita el número y la versión. Así siempre podrás responder a una pregunta: ¿según qué versión se hizo este lote?",
    )),

    ("h2", D("2. 所有辅料都要写清的八个通用字段", "2. Eight Fields Every Trim Needs",
             "2. すべての副資材に必要な8つの共通項目", "2. 모든 부자재에 필요한 8가지 공통 항목",
             "2. Les huit champs communs à tout accessoire", "2. Los ocho campos comunes a todo accesorio")),
    ("ul", [
        D("<strong>品名与用途：</strong>写「主唛 · 领口」或「包装袋 · 内袋」，避免同名不同用途",
          "<strong>Item name and use:</strong> write neck label, collar or poly bag, inner — not just the generic name",
          "<strong>品名と用途：</strong>「メインラベル・衿」のように用途まで書き、同名別用途を防ぎます",
          "<strong>품명과 용도:</strong> '메인 라벨·목선'처럼 용도까지 적어 같은 이름의 다른 용도를 구분합니다",
          "<strong>Désignation et usage :</strong> écrivez label de col, encolure ou sac, usage interne, pas seulement le nom générique",
          "<strong>Nombre y uso:</strong> escribe etiqueta de cuello, cuello o bolsa, uso interno, no solo el nombre genérico"),
        D("<strong>材质与规格：</strong>纸张克重或纱线与织法、袋材厚度、织带宽度",
          "<strong>Material and spec:</strong> paper weight, or yarn and weave; film thickness; tape width",
          "<strong>素材と仕様：</strong>紙の坪量、または糸と織り方、フィルム厚み、テープ幅",
          "<strong>소재와 사양:</strong> 종이 평량 또는 원사와 직조 방식, 필름 두께, 테이프 폭",
          "<strong>Matière et spécification :</strong> grammage papier, ou fil et armure, épaisseur du film, largeur de ruban",
          "<strong>Material y especificación:</strong> gramaje del papel, o hilo y ligamento, espesor del film, ancho de cinta"),
        D("<strong>成品尺寸与公差：</strong>成品尺寸加上公差（如 ±1mm），并注明测量方法与裁切边",
          "<strong>Finished size and tolerance:</strong> size plus tolerance, such as ±1 mm, with measuring method and cut edge defined",
          "<strong>仕上がり寸法と公差：</strong>寸法に公差（例 ±1mm）を添え、測定方法と裁断エッジも明記",
          "<strong>완성 치수와 공차:</strong> 치수에 공차(예 ±1mm)를 더하고 측정 방법과 재단 가장자리도 명시",
          "<strong>Dimensions finies et tolérance :</strong> cote plus tolérance, par exemple ±1 mm, avec méthode de mesure et bord de coupe",
          "<strong>Medidas finales y tolerancia:</strong> medida más tolerancia, por ejemplo ±1 mm, con método de medición y borde de corte"),
        D("<strong>颜色与色样：</strong>Pantone 或实样封样，并写清批次色差容忍范围",
          "<strong>Colour and standard:</strong> Pantone or a sealed physical sample, plus the batch colour deviation you accept",
          "<strong>色と色見本：</strong>Pantone または封入実見本、さらに許容できるロット色差の範囲",
          "<strong>색상과 색상 견본:</strong> Pantone 또는 봉인 실물 샘플, 그리고 허용하는 로트 색차 범위",
          "<strong>Couleur et référence :</strong> Pantone ou échantillon physique scellé, plus la dérive de lot acceptée",
          "<strong>Color y referencia:</strong> Pantone o muestra física sellada, más la desviación de lote admitida"),
        D("<strong>工艺组合：</strong>印刷方式加上后道工艺（烫金、压凹凸、上光、模切、超声波）",
          "<strong>Finishing set:</strong> printing method plus post-press steps such as foil, embossing, varnish, die-cutting, ultrasonic",
          "<strong>加工の組み合わせ：</strong>印刷方式に加え、箔押し・エンボス・ニス・型抜き・超音波などの後加工",
          "<strong>가공 조합:</strong> 인쇄 방식에 박, 엠보싱, 니스, 타공, 초음파 등 후가공을 더함",
          "<strong>Ensemble de finitions :</strong> procédé d'impression plus dorure, gaufrage, vernis, découpe, ultrason",
          "<strong>Conjunto de acabados:</strong> impresión más dorado, relieve, barniz, troquelado, ultrasonidos"),
        D("<strong>文字与语言版本：</strong>中英法西日韩各版本对应哪个市场，由谁终审",
          "<strong>Text and languages:</strong> which market each language version serves, and who signs it off",
          "<strong>文字と言語版：</strong>各言語版がどの市場向けか、最終承認者は誰か",
          "<strong>문자와 언어 버전:</strong> 각 언어 버전이 어느 시장을 대상으로 하는지, 최종 승인자는 누구인지",
          "<strong>Textes et langues :</strong> à quel marché correspond chaque version, et qui valide",
          "<strong>Textos e idiomas:</strong> a qué mercado sirve cada versión y quién la valida"),
        D("<strong>数量与包装：</strong>箱装数量、每捆数量、是否单件装袋、混码方式",
          "<strong>Quantity and packing:</strong> per carton, per bundle, whether each piece is bagged, and size mix",
          "<strong>数量と包装：</strong>箱入数、束数、単品袋入れの有無、サイズ混載の方法",
          "<strong>수량과 포장:</strong> 박스 입수량, 묶음 수, 단품 봉투 포장 여부, 사이즈 혼합 방식",
          "<strong>Quantité et conditionnement :</strong> par carton, par liasse, sac individuel ou non, mix des tailles",
          "<strong>Cantidad y embalaje:</strong> por caja, por fajo, bolsa individual sí o no, mezcla de tallas"),
        D("<strong>文件版本与日期：</strong>规格书编号、版本号与生效日期，改动留痕",
          "<strong>Document control:</strong> spec number, version and effective date, with a change log",
          "<strong>文書の版と日付：</strong>仕様書番号・版数・発効日、変更履歴の記録",
          "<strong>문서 버전과 날짜:</strong> 사양서 번호, 버전, 시행일, 변경 이력 기록",
          "<strong>Version et date :</strong> numéro, indice et date d'application, avec historique des modifications",
          "<strong>Versión y fecha:</strong> número, versión y fecha de vigencia, con historial de cambios"),
    ]),

    ("h2", D("3. 分品类字段清单与最容易漏的项", "3. Field Checklist by Product Family",
             "3. 品種別の項目リストと最も見落としやすい点", "3. 품목별 항목 리스트와 가장 놓치기 쉬운 점",
             "3. Liste de champs par famille et oublis fréquents", "3. Lista de campos por familia y omisiones frecuentes")),
    ("p", D(
        "通用字段之外，每类辅料都有自己最容易漏的字段。下表是打样前至少要确认的内容；首次合作建议连封样一起寄，让供应商按实样确认。",
        "Beyond the common fields, each family has its own trap. The table lists what to confirm before sampling; on a first order, send sealed samples too so your supplier confirms against the real thing.",
        "共通項目以外に、品種ごとに見落としやすい項目があります。下表はサンプル作成前に最低限確認したい内容です。初回は封入見本も一緒に送り、現物で確認してもらいましょう。",
        "공통 항목 외에 품목별로 놓치기 쉬운 항목이 있습니다. 아래 표는 샘플 제작 전에 최소한 확인할 내용이며, 첫 거래에서는 봉인 샘플도 함께 보내 실물로 확인받으십시오.",
        "Au-delà des champs communs, chaque famille a son piège. Le tableau liste ce qu'il faut confirmer avant l'échantillon ; à la première commande, joignez aussi des échantillons scellés.",
        "Además de los campos comunes, cada familia tiene su trampa. La tabla recoge lo que conviene confirmar antes de la muestra; en el primer pedido, envía también muestras selladas.",
    )),
    ("table", (
        [D("品类", "Family", "品種", "품목", "Famille", "Familia"),
         D("必填字段", "Must-have fields", "必須項目", "필수 항목", "Champs obligatoires", "Campos obligatorios"),
         D("最容易漏的", "Most often missed", "最も漏れやすい", "가장 자주 빠지는", "Le plus souvent oublié", "Lo que más se omite")],
        [
            [D("吊牌", "Hang tag", "タグ", "행택", "Étiquette suspendue", "Etiqueta colgante"),
             D("纸张与克重、成品尺寸与公差、孔位与孔径、吊绳与吊粒、印刷面数、烫金部位",
               "Paper and weight, size with tolerance, hole position and diameter, string and fastener, number of printed sides, foil areas",
               "用紙と坪量、仕上がり寸法と公差、穴位置と穴径、吊りひもと留め具、印刷面数、箔押し範囲",
               "용지와 평량, 완성 치수와 공차, 구멍 위치와 직경, 끈과 체결구, 인쇄 면수, 박 부위",
               "Papier et grammage, dimensions avec tolérance, perçage et diamètre, cordon et fixation, nombre de faces imprimées, zones dorées",
               "Papel y gramaje, medidas con tolerancia, taladro y diámetro, cordón y remache, caras impresas, zonas doradas"),
             D("孔位到边距离与吊绳长度", "Hole distance to edge and string length", "穴の端からの距離とひも長", "구멍의 가장자리 거리와 끈 길이",
               "Distance du perçage au bord et longueur du cordon", "Distancia del taladro al borde y largo del cordón")],
            [D("织唛", "Woven label", "織りラベル", "직조 라벨", "Label tissé", "Etiqueta tejida"),
             D("织法（缎面 / 平纹 / 提花）、宽度与折法、切边方式、缝制方式、经纬密度",
               "Weave such as satin, plain or jacquard, width and fold, cut method, stitching method, thread density",
               "織り方（サテン・平織り・ジャカード）、幅と折り、裁断方法、縫い付け方法、密度",
               "직조 방식(새틴·평직·자카드), 폭과 접힘, 재단 방식, 봉제 방식, 밀도",
               "Armure satin, toile ou jacquard, largeur et pliage, coupe, couture, densité",
               "Ligamento satén, tafetán o jacquard, ancho y plegado, corte, cosido, densidad"),
             D("折法与切边方式", "Fold and cut method", "折りと裁断方法", "접힘과 재단 방식", "Pliage et méthode de coupe", "Plegado y método de corte")],
            [D("洗水标", "Care label", "洗濯表示ラベル", "세탁 표시 라벨", "Étiquette d'entretien", "Etiqueta de cuidado"),
             D("材质（织带 / 涂层 / 印刷）、洗涤符号版本、成分标注、语言组合、耐洗等级",
               "Material such as tape, coated or printed, care symbol version, fibre content, language set, wash grade",
               "素材（テープ・コーティング・印刷）、洗濯記号の版、組成表示、言語構成、耐洗濯等級",
               "소재(테이프·코팅·인쇄), 세탁 기호 버전, 성분 표시, 언어 구성, 세탁 등급",
               "Support ruban, enduit ou imprimé, version des symboles, composition, langues, tenue au lavage",
               "Soporte cinta, recubierto o impreso, versión de símbolos, composición, idiomas, resistencia al lavado"),
             D("洗涤符号版本与语言组合", "Symbol version and language set", "洗濯記号の版と言語構成", "세탁 기호 버전과 언어 구성",
               "Version des symboles et langues", "Versión de símbolos e idiomas")],
            [D("包装袋", "Poly bag", "包装袋", "포장백", "Sac d'emballage", "Bolsa de embalaje"),
             D("材质（OPP / PE / CPE）、厚度、袋型与封口、印刷油墨、透气孔与警示语",
               "Film such as OPP, PE or CPE, thickness, style and seal, ink, vent holes and warning wording",
               "素材（OPP・PE・CPE）、厚み、袋型と封口、インキ、通気孔と警告文",
               "소재(OPP·PE·CPE), 두께, 형태와 밀봉, 잉크, 통기 구멍과 경고 문구",
               "Film OPP, PE ou CPE, épaisseur, format et soudure, encre, trous d'aération et avertissements",
               "Film OPP, PE o CPE, espesor, formato y sellado, tinta, orificios de ventilación y advertencias"),
             D("警示语与透气孔", "Warning wording and vent holes", "警告文と通気孔", "경고 문구와 통기 구멍",
               "Avertissements et trous d'aération", "Advertencias y orificios de ventilación")],
        ])),

    ("h2", D("4. 颜色与公差：把「差不多」写成数字", "4. Colour and Tolerance: Turn Roughly into Numbers",
             "4. 色と公差：「だいたい」を数値にする", "4. 색상과 공차: '대충'을 숫자로",
             "4. Couleur et tolérance : transformer à peu près en chiffres", "4. Color y tolerancia: convertir el casi en cifras")),
    ("p", D(
        "颜色是辅料返工的头号原因。吊牌纸张、织唛纱线、纸袋面纸的上色原理完全不同，同一个 Pantone 号在三种材质上必然有差别。可行的做法是按品类分别封样，并把允许色差写进规格书：织唛以封样为基准、参考灰卡四级到五级；纸品承认批次间轻微色差，但不得影响品牌主色识别。尺寸公差同样要落到数字：吊牌成品尺寸按 ±0.5 到 1mm，织唛按 ±1mm，织带宽度按 ±0.5mm，异形模切要另外约定刀模公差。",
        "Colour causes more trims rework than anything else. Paper, woven yarn and bag film colour up in completely different ways, so the same Pantone number will differ across the three. The workable approach: seal a sample per family and write the accepted deviation into the spec sheet, keeping the sealed sample as master for woven labels at grey scale grade four to five, and accepting slight batch variation on paper as long as the brand colour stays recognisable. Tolerances must be numeric too: ±0.5 to 1 mm on cut hang tags, ±1 mm on woven labels, ±0.5 mm on tape width, plus a separate die-cutting tolerance for shaped tags.",
        "色は副資材の手直しで最も多い原因です。紙・織り糸・袋のフィルムでは発色の仕組みが全く異なるため、同じ Pantone 番号でも三者で必ず差が出ます。現実的な方法は、品種ごとに封入見本（マスター）を作り、許容できる色差を仕様書に明記することです。織りラベルは封入見本を基準にグレースケール4〜5級を目安とし、紙製品はブランド色の識別に影響しない範囲でロット差を許容します。寸法公差も数値化が必須で、タグの仕上がりは±0.5〜1mm、織りラベルは±1mm、テープ幅は±0.5mm、型抜きは別途金型公差を定めます。",
        "색상은 부자재 재작업의 최대 원인입니다. 종이, 직조 원사, 포장 필름은 발색 원리가 전혀 달라 같은 Pantone 번호도 세 가지 소재에서 반드시 차이가 납니다. 현실적인 방법은 품목별로 봉인 샘플을 만들어 허용 색차를 사양서에 명시하는 것입니다. 직조 라벨은 봉인 샘플을 기준으로 그레이 스케일 4~5급을 참고하고, 종이 제품은 브랜드 색상 식별에 영향을 주지 않는 범위에서 로트 차이를 허용합니다. 치수 공차도 숫자로 정해야 하며, 행택 완성 치수는 ±0.5~1mm, 직조 라벨은 ±1mm, 테이프 폭은 ±0.5mm, 이형 타공은 별도의 금형 공차를 정합니다.",
        "La couleur est la première cause de reprise. Papier, fil tissé et film de sac colorent selon des principes totalement différents : un même Pantone donnera trois résultats. La méthode praticable : sceller un échantillon par famille et inscrire la dérive admise dans la fiche, l'échantillon scellé servant de référence pour le tissé avec une échelle de gris de niveau quatre à cinq, et une légère variation de lot étant admise sur le papier tant que la couleur de marque reste identifiable. Les tolérances doivent aussi être chiffrées : ±0,5 à 1 mm sur une étiquette découpée, ±1 mm sur le tissé, ±0,5 mm sur la largeur de ruban, et une tolérance de découpe distincte pour les formes.",
        "El color provoca más reprocesos que nada. El papel, el hilo tejido y el film de las bolsas se colorean de formas totalmente distintas, así que un mismo Pantone dará tres resultados. Lo práctico: sellar una muestra por familia e inscribir la desviación admitida en la ficha, con la muestra sellada como referencia en tejidos con escala de grises de nivel cuatro a cinco, y variación leve de lote admitida en papel mientras el color de marca siga siendo reconocible. Las tolerancias también van en cifras: ±0,5 a 1 mm en colgantes troquelados, ±1 mm en tejidos, ±0,5 mm en ancho de cinta y una tolerancia de cuchilla aparte para formas.",
    )),

    ("h2", D("5. 语言版本与文件版本控制", "5. Language Versions and Document Control",
             "5. 言語版と文書の版管理", "5. 언어 버전과 문서 버전 관리",
             "5. Versions linguistiques et gestion des indices", "5. Versiones de idioma y control de versiones")),
    ("p", D(
        "洗水标的多语言组合、吊牌上的品牌故事、包装袋上的警示语，都需要指定「市场、语言、文案」的对应关系。建议在规格书里用三列写清，并注明文案由谁终审：品牌方审校，还是供应商按既有模板翻译。不同市场的强制语言与洗涤符号版本不同，文案定稿前不要开印版，否则改版要按新印版计费。",
        "Care-label language sets, the brand story on a hang tag and the warnings on a bag all need an explicit market-to-language-to-copy mapping. Use three columns in the spec sheet and state who signs the copy off, the brand or the supplier translating from an approved template. Mandatory languages and care symbol versions differ by market, so do not commit printing plates before the copy is final: a later text change is charged as a new plate.",
        "洗濯表示ラベルの言語セット、タグのブランドストーリー、袋の警告文は、「市場・言語・文案」の対応を明記する必要があります。仕様書では3列で整理し、文案の最終承認者（ブランド側の校閲か、承認済みテンプレートからのサプライヤー翻訳か）を明記します。必須言語と洗濯記号の版は市場ごとに異なるため、文案確定前に刷版を起こさないでください。後の文言変更は新版として費用が発生します。",
        "세탁 표시 라벨의 언어 세트, 행택의 브랜드 스토리, 포장백의 경고 문구는 모두 '시장·언어·문안' 대응 관계를 명시해야 합니다. 사양서에 세 열로 정리하고 문안 최종 승인 주체(브랜드 검수인지, 승인된 템플릿을 번역하는 공급업체인지)를 적습니다. 시장별 필수 언어와 세탁 기호 버전이 다르므로 문안 확정 전에 인쇄판을 만들지 마십시오. 이후 문구 변경은 신규 판으로 비용이 발생합니다.",
        "Les jeux de langues d'une étiquette d'entretien, l'histoire de marque d'une étiquette suspendue et les avertissements d'un sac exigent une correspondance explicite marché, langue, texte. Prévoyez trois colonnes dans la fiche et précisez qui valide : la marque ou le fournisseur traduisant depuis un modèle approuvé. Les langues obligatoires et les versions de symboles varient selon le marché : ne lancez pas les clichés avant validation du texte, une modification ultérieure est facturée comme un nouveau cliché.",
        "Los juegos de idiomas de la etiqueta de cuidado, la historia de marca de un colgante y los avisos de una bolsa exigen una correspondencia explícita mercado, idioma, texto. Usa tres columnas en la ficha e indica quién valida: la marca o el proveedor traduciendo desde una plantilla aprobada. Los idiomas obligatorios y las versiones de símbolos varían por mercado, así que no hagas planchas antes de cerrar el texto: un cambio posterior se cobra como plancha nueva.",
    )),
    ("ul", [
        D("<strong>命名统一：</strong>品牌 - 品类 - 编号 - 版本 - 日期，例如 TAGE-HANGTAG-HT104-V3-20260919",
          "<strong>One naming rule:</strong> brand - family - item number - version - date, for example TAGE-HANGTAG-HT104-V3-20260919",
          "<strong>命名の統一：</strong>ブランド - 品種 - 品番 - 版 - 日付（例 TAGE-HANGTAG-HT104-V3-20260919）",
          "<strong>명명 규칙 통일:</strong> 브랜드 - 품목 - 품번 - 버전 - 날짜, 예: TAGE-HANGTAG-HT104-V3-20260919",
          "<strong>Nommage unique :</strong> marque - famille - référence - indice - date, par exemple TAGE-HANGTAG-HT104-V3-20260919",
          "<strong>Nomenclatura única:</strong> marca - familia - referencia - versión - fecha, por ejemplo TAGE-HANGTAG-HT104-V3-20260919"),
        D("<strong>改动升版：</strong>每次修改升版本号，并在变更记录里写清改了什么、为什么、影响哪些批次",
          "<strong>Bump on change:</strong> raise the version on every edit and log what changed, why, and which batches are affected",
          "<strong>変更で版上げ：</strong>修正のたびに版数を上げ、変更内容・理由・影響ロットを履歴に記載",
          "<strong>변경 시 버전 상향:</strong> 수정할 때마다 버전을 올리고 변경 내용, 사유, 영향 로트를 기록",
          "<strong>Incrémenter à chaque changement :</strong> montez l'indice et consignez quoi, pourquoi et quels lots sont concernés",
          "<strong>Subir versión al cambiar:</strong> eleva la versión en cada edición y registra qué cambió, por qué y qué lotes afecta"),
        D("<strong>封样同步：</strong>封样袋上贴版本标签，避免「样是新版、单是旧版」",
          "<strong>Samples in step:</strong> label sealed samples with the version so you never sample the new one and order the old one",
          "<strong>封入見本の同期：</strong>見本袋に版ラベルを貼り、「見本は新版・注文は旧版」を防ぎます",
          "<strong>봉인 샘플 동기화:</strong> 봉인 샘플 봉투에 버전 라벨을 붙여 '샘플은 신판, 발주는 구판'을 막습니다",
          "<strong>Échantillons synchronisés :</strong> étiquetez les échantillons scellés par indice pour éviter l'échantillon neuf commandé à l'ancien indice",
          "<strong>Muestras sincronizadas:</strong> etiqueta las muestras selladas con la versión para no aprobar la nueva y pedir la antigua"),
        D("<strong>批次隔离：</strong>已下单批次仍按原版本生产，改版从下一批生效，不混批",
          "<strong>Batch isolation:</strong> orders already placed run to the old version; the new one starts with the next batch, never mixed",
          "<strong>ロット分離：</strong>発注済みロットは旧版で生産し、改版は次ロットから適用、混在させない",
          "<strong>로트 분리:</strong> 이미 발주한 로트는 구버전으로 생산하고, 신버전은 다음 로트부터 적용해 혼합하지 않습니다",
          "<strong>Isolation des lots :</strong> les commandes en cours restent à l'ancien indice, le nouveau démarre au lot suivant, sans mélange",
          "<strong>Aislamiento de lotes:</strong> los pedidos ya cursados siguen con la versión anterior y la nueva empieza en el lote siguiente, sin mezclar"),
        D("<strong>回执确认：</strong>发出新版时写明「本版替代 V2」，并要求供应商回复确认",
          "<strong>Written acknowledgement:</strong> send the new version marked as replacing V2 and ask your supplier to confirm in writing",
          "<strong>受領確認：</strong>新版送付時に「本版は V2 を置き換える」と明記し、サプライヤーの回答確認を求めます",
          "<strong>수령 확인:</strong> 신버전 발송 시 '본 버전이 V2를 대체함'을 명시하고 공급업체의 회신 확인을 받습니다",
          "<strong>Accusé de réception :</strong> envoyez la nouvelle version en indiquant qu'elle remplace la V2 et demandez confirmation écrite",
          "<strong>Acuse de recibo:</strong> envía la nueva versión indicando que sustituye a la V2 y pide confirmación por escrito"),
    ]),

    ("h2", D("6. 四个最常见的漏填事故与打样前核对", "6. Four Costly Omissions and a Pre-Sampling Check",
             "6. 最も多い4つの記載漏れとサンプル前チェック", "6. 가장 흔한 4가지 누락 사례와 샘플 전 점검",
             "6. Quatre oublis coûteux et une vérification avant échantillon", "6. Cuatro omisiones costosas y una comprobación antes de la muestra")),
    ("callout", D(
        "<strong>💡 最容易踩的四个坑：</strong>只写「白色」，没写克重与色号，首批偏黄；没写折法与切边方式，织唛装不上领口、缝制工时翻倍；没写洗涤符号的语言组合，到货后重新订标，最快也要七到十天；没写包装方式，一捆压出折痕，客户仓库收货时会判次品。",
        "<strong>💡 The four costliest traps:</strong> writing only white without paper weight or colour reference, so the first batch arrives yellow; no fold or cut method, so the woven label will not sit in the neckline and sewing time doubles; no care symbol language set, forcing a re-order that takes seven to ten days even at best; no packing method, so a bundle arrives creased and is rejected at the customer warehouse.",
        "<strong>💡 最も費用のかかる4つの落とし穴：</strong>「白」とだけ書き坪量と色番を書かないと初回ロットが黄ばみます。折りと裁断方法を書かないと織りラベルが衿に収まらず縫製工数が倍になります。洗濯記号の言語構成を書かないと、納品後に再発注となり最短でも7〜10日かかります。包装方法を書かないと束の折り目がつき、客先倉庫で不良判定されます。",
        "<strong>💡 비용이 가장 큰 네 가지 함정:</strong> '흰색'만 쓰고 평량과 색상 번호를 쓰지 않으면 첫 로트가 누렇게 나옵니다. 접힘과 재단 방식을 쓰지 않으면 직조 라벨이 목선에 맞지 않아 봉제 공수가 두 배가 됩니다. 세탁 기호 언어 구성을 쓰지 않으면 입고 후 재발주로 최소 7~10일이 걸립니다. 포장 방식을 쓰지 않으면 묶음에 접힘 자국이 생겨 고객 창고에서 불량 판정을 받습니다.",
        "<strong>💡 Les quatre pièges les plus coûteux :</strong> écrire seulement blanc sans grammage ni référence, et le premier lot arrive jaune ; pas de pliage ni de coupe, le label ne tient pas dans l'encolure et le temps de couture double ; pas de jeu de langues pour les symboles, ce qui impose une réimpression en sept à dix jours au mieux ; pas de mode de conditionnement, la liasse arrive marquée et est refusée en entrepôt.",
        "<strong>💡 Las cuatro trampas más caras:</strong> escribir solo blanco sin gramaje ni referencia y recibir el primer lote amarillento; sin plegado ni corte, la etiqueta no encaja en el cuello y el cosido se duplica; sin juego de idiomas para los símbolos, toca reimprimir en siete a diez días como mínimo; sin método de embalaje, el fajo llega marcado y se rechaza en el almacén del cliente.",
    )),
    ("ol", [
        D("规格书是否已升到最新版本，并附变更说明", "Is the spec sheet at its latest version, with a change note",
          "仕様書が最新版に更新され、変更説明が添付されているか", "사양서가 최신 버전으로 갱신되고 변경 설명이 첨부되었는가",
          "La fiche est-elle au dernier indice, avec une note de modification", "¿La ficha está en su última versión, con nota de cambio"),
        D("是否附封样或色样，包括纸张、纱线与袋材小样", "Are sealed or colour samples attached, including paper, yarn and film swatches",
          "封入見本や色見本（紙・糸・フィルムの小片）が添付されているか", "봉인 샘플 또는 색상 견본(종이, 원사, 필름 소재)이 첨부되었는가",
          "Les échantillons scellés ou de couleur sont-ils joints, papier, fil et film inclus", "¿Se adjuntan muestras selladas o de color, incluidas las de papel, hilo y film"),
        D("数量与包装方式是否与订单一致，含单件装袋与混码", "Do quantity and packing match the order, including individual bagging and size mix",
          "数量と包装方法が発注と一致しているか（単品袋入れ・サイズ混載を含む）", "수량과 포장 방식이 발주와 일치하는가(단품 봉투, 사이즈 혼합 포함)",
          "Quantité et conditionnement correspondent-ils à la commande, sac individuel et mix de tailles inclus", "¿Cantidad y embalaje coinciden con el pedido, incluida la bolsa individual y la mezcla de tallas"),
        D("洗涤符号版本与语言组合是否与目标市场匹配", "Do the care symbol version and language set match the target market",
          "洗濯記号の版と言語構成が対象市場に合っているか", "세탁 기호 버전과 언어 구성이 목표 시장에 맞는가",
          "Version des symboles et langues correspondent-elles au marché visé", "¿La versión de símbolos e idiomas encaja con el mercado destinatario"),
        D("打样费与交期是否已确认，以及大货可退与否", "Are the sampling fee and lead time confirmed, and is the fee credited against bulk",
          "サンプル費用と納期、量産時に相殺されるかが確認済みか", "샘플 비용과 납기, 양산 시 상계 여부가 확인되었는가",
          "Frais d'échantillon et délai sont-ils confirmés, et le montant est-il déduit du volume", "¿Están confirmados el coste de muestra y el plazo, y se deduce del volumen"),
        D("谁做最终签样确认，品牌签字还是书面邮件确认", "Who gives final sample approval, a signed sheet or a written email confirmation",
          "最終サンプル承認者は誰か、署名かメール確認か", "최종 샘플 승인 주체는 누구이며, 서명인지 메일 확인인지",
          "Qui valide l'échantillon final, signature ou confirmation écrite", "¿Quién aprueba la muestra final, firma o confirmación escrita"),
    ]),
]

# ---------------------------------------------------------------- 文章二
ART2_BLOCKS = [
    ("p", D(
        "西装、西服外套、大衣和礼服这类正装，辅料用量不大，要求却最苛刻：面料娇贵怕勾丝，运输必须挂装，干洗符号与成分标注容错率极低，而顾客对高级感的判断，往往就来自后领标签的手感和吊牌的分量。",
        "Suits, blazers, coats and eveningwear use little trim but demand the most: delicate fabric that snags easily, shipping that must hang, and almost no tolerance on dry-clean symbols or fibre content. What customers read as quality often comes down to how the back-neck label feels and how the hang tag weighs in the hand.",
        "スーツ、ジャケット、コート、礼服といったフォーマル衣料は、副資材の使用量は少ない一方で要求が最も厳しい分野です。生地は引っかけに弱く、輸送は掛け姿が前提、ドライ記号や組成表示の許容度はほぼゼロ。そして上質さの印象は、衿裏のラベルの手触りとタグの重みから伝わります。",
        "수트, 재킷, 코트, 예복 같은 포멀 의류는 부자재 사용량은 적지만 요구 조건이 가장 까다롭습니다. 원단은 올이 나가기 쉽고, 운송은 걸이 상태가 기본이며, 드라이 기호와 성분 표기의 허용 오차는 거의 없습니다. 고급스러움에 대한 고객의 판단은 목 뒤 라벨의 촉감과 행택의 무게에서 나옵니다.",
        "Costume, veste, manteau et tenue de soirée utilisent peu d'accessoires mais en exigent le plus : tissu fragile qui s'accroche, expédition obligatoirement sur cintre, et presque aucune marge sur les symboles de nettoyage à sec ou la composition. La perception de qualité vient souvent du toucher du label de col et du poids de l'étiquette suspendue.",
        "Trajes, americanas, abrigos y ropa de ceremonia usan pocos accesorios pero exigen lo máximo: tejido delicado que se engancha, envío obligatoriamente colgado y casi nulo margen en los símbolos de limpieza en seco o la composición. La percepción de calidad suele venir del tacto de la etiqueta del cuello y del peso del colgante.",
    )),
    ("p", D(
        "本文按主唛与尺码标、洗水标、吊牌、包装四个部分展开，最后对比职业装、校服与礼服在辅料上的差异，并给出打样前的核对清单。",
        "This guide works through four parts, neck and size labels, care labels, hang tags and packaging, then compares uniforms, schoolwear and eveningwear, and closes with a pre-sampling checklist.",
        "本ガイドはメインラベルとサイズラベル、洗濯表示ラベル、タグ、包装の4部構成で解説し、最後に制服・学校服・礼服の違いを比較して、サンプル前のチェックリストを掲載します。",
        "이 가이드는 메인 라벨과 사이즈 라벨, 세탁 표시 라벨, 행택, 포장의 네 부분으로 구성되며, 마지막에 유니폼·교복·예복의 차이를 비교하고 샘플 전 점검 리스트를 제공합니다.",
        "Ce guide aborde quatre parties, labels de col et de taille, étiquettes d'entretien, étiquettes suspendues et emballage, puis compare uniforme, scolaire et soirée, et se termine par une liste de contrôle avant échantillon.",
        "Esta guía repasa cuatro partes, etiquetas de cuello y de talla, etiquetas de cuidado, colgantes y embalaje, compara uniforme, escolar y ceremonia, y cierra con una lista de comprobación antes de la muestra.",
    )),

    ("h2", D("1. 正装辅料的三个特殊要求", "1. Three Demands Formalwear Places on Trims",
             "1. フォーマル衣料が副資材に求める3つの要件", "1. 포멀 의류가 부자재에 요구하는 세 가지 조건",
             "1. Trois exigences du formel envers les accessoires", "1. Tres exigencias de la ropa formal a los accesorios")),
    ("ul", [
        D("<strong>耐干洗：</strong>多数正装只能干洗，四氯乙烯与石油溶剂对油墨和胶粘剂的侵蚀远大于水洗，印刷类洗标与不干胶必须按干洗条件选材并测试",
          "<strong>Dry-clean resistance:</strong> most formalwear is dry-clean only, and perchloroethylene or petroleum solvent attacks ink and adhesive far more than water does, so printed care labels and stickers must be chosen and tested for dry-clean conditions",
          "<strong>ドライ耐性：</strong>多くのフォーマル衣料はドライクリーニングのみです。パークロロエチレンや石油系溶剤は、水洗よりはるかに強くインキと粘着剤を侵すため、印刷洗濯表示ラベルと粘着ラベルはドライ条件で選定・試験する必要があります",
          "<strong>드라이클리닝 내구성:</strong> 대부분의 포멀 의류는 드라이 전용이며, 퍼클로로에틸렌과 석유계 용제는 물보다 훨씬 강하게 잉크와 점착제를 침식하므로 인쇄 세탁 라벨과 스티커는 드라이 조건에서 소재를 선정하고 시험해야 합니다",
          "<strong>Tenue au nettoyage à sec :</strong> la plupart des pièces formelles se nettoient à sec, et le perchloroéthylène ou les solvants pétroliers attaquent l'encre et l'adhésif bien plus que l'eau : étiquettes imprimées et autocollants doivent être choisis et testés pour ces conditions",
          "<strong>Resistencia a la limpieza en seco:</strong> casi toda la ropa formal es de limpieza en seco, y el percloroetileno o los disolventes petrolíferos atacan la tinta y el adhesivo mucho más que el agua, así que las etiquetas impresas y los adhesivos deben elegirse y ensayarse en esas condiciones"),
        D("<strong>低调的高级感：</strong>领标以深色缎面、哑光处理为主，烫印建议哑金或哑银，避免高反光的塑料感",
          "<strong>Quiet premium feel:</strong> neck labels lean to dark satin and matte finishing, with matte gold or matte silver foil rather than the glossy plastic look",
          "<strong>控えめな上質感：</strong>衿ラベルは濃色サテンやマット仕上げが中心で、箔はマットゴールドやマットシルバーを選び、強い光沢のプラスチック感を避けます",
          "<strong>절제된 고급감:</strong> 목 라벨은 어두운 새틴과 무광 처리가 중심이며, 박은 무광 골드나 무광 실버를 선택해 강한 광택의 플라스틱 느낌을 피합니다",
          "<strong>Luxe discret :</strong> les labels de col privilégient le satin foncé et les finitions mates, avec dorure ou argenture mate plutôt qu'un brillant plastique",
          "<strong>Lujo discreto:</strong> las etiquetas de cuello tienden a satén oscuro y acabado mate, con dorado o plateado mate en vez de un brillo plástico"),
        D("<strong>尺码与法规双重严格：</strong>羊毛含量与原产国在多国属强制标注项，尺码标还要对应西装号型（如 48R、50R）与内销外销体系差异",
          "<strong>Tight on size and rules:</strong> wool content and country of origin are mandatory in many markets, and size labels must follow suiting size systems such as 48R or 50R",
          "<strong>サイズと法規の両面で厳格：</strong>ウール含有率と原産国は多くの市場で義務表示であり、サイズラベルは 48R・50R などのスーツ号型体系に合わせる必要があります",
          "<strong>사이즈와 규정 모두 엄격:</strong> 울 함량과 원산국은 많은 시장에서 의무 표시이며, 사이즈 라벨은 48R·50R 같은 수트 호수 체계를 따라야 합니다",
          "<strong>Tailles et règles strictes :</strong> la teneur en laine et le pays d'origine sont obligatoires sur de nombreux marchés, et les tailles doivent suivre les systèmes de costume comme 48R ou 50R",
          "<strong>Estrictos en talla y normativa:</strong> el contenido de lana y el país de origen son obligatorios en muchos mercados, y las tallas deben seguir sistemas como 48R o 50R"),
    ]),

    ("h2", D("2. 主唛与尺码标：位置比工艺更影响穿着感受", "2. Neck and Size Labels: Position Matters More Than Finishing",
             "2. メインラベルとサイズラベル：位置が着心地を左右する", "2. 메인 라벨과 사이즈 라벨: 위치가 착용감을 좌우합니다",
             "2. Label de col et de taille : la position compte plus que la finition", "2. Etiquetas de cuello y talla: la posición importa más que el acabado")),
    ("p", D(
        "正装主唛通常缝在后领里布或内袋上方，宽度受领里限制，常见 25 到 35 毫米；尺码标与产地标多与主唛同排缝制，或缝在内袋侧。缎面织唛一定要热切收边，硬边会摩擦后颈；缝线颜色尽量与里布同色。内袋标不要落在手插袋的摩擦区，否则半年就会起毛。",
        "On formalwear the neck label usually sits on the back-neck lining or above the inside pocket, and its width is limited by the lining, commonly 25 to 35 mm. Size and origin labels are usually sewn on the same line, or into the side of the inside pocket. Satin woven labels must be hot-cut, since a hard edge rubs the nape; stitching should match the lining colour. Keep inside-pocket labels clear of the hand-entry wear zone, or they will fuzz within six months.",
        "フォーマルのメインラベルは通常、衿裏の裏地または内ポケットの上に縫い付けられ、幅は裏地に制約され、一般的に25〜35mmです。サイズラベルと原産国ラベルは同じ行に縫うか、内ポケットの側に縫います。サテンの織りラベルは必ず熱裁断で端を処理してください。硬い端はうなじを擦ります。縫い糸は裏地と同系色に。内ポケットのラベルは手を入れる摩擦域を避けないと、半年で毛羽立ちます。",
        "포멀 의류의 메인 라벨은 보통 목 뒤 안감이나 안주머니 위에 달며, 폭은 안감에 제한되어 일반적으로 25~35mm입니다. 사이즈 라벨과 원산지 라벨은 같은 줄에 봉제하거나 안주머니 측면에 달며, 새틴 직조 라벨은 반드시 열 절단으로 마감해야 합니다. 딱딱한 가장자리는 목덜미를 문지릅니다. 봉제사는 안감과 같은 색으로 맞추고, 안주머니 라벨은 손이 드나드는 마찰 구역을 피해야 6개월 만에 보풀이 생기지 않습니다.",
        "Sur une pièce formelle, le label de col se pose sur la doublure d'encolure ou au-dessus de la poche intérieure, sa largeur étant limitée par la doublure, souvent 25 à 35 mm. Les labels de taille et d'origine sont cousus sur la même ligne, ou dans le côté de la poche. Un label tissé satin doit être coupé à chaud : un bord dur irrite la nuque. Le fil doit s'accorder à la doublure. Évitez la zone de frottement de la main dans la poche, sinon le label s'effiloche en six mois.",
        "En ropa formal, la etiqueta de cuello va sobre el forro del escote o encima del bolsillo interior, con un ancho limitado por el forro, normalmente de 25 a 35 mm. Las etiquetas de talla y origen suelen ir en la misma línea, o en el lateral del bolsillo. Las etiquetas tejidas de satén deben cortarse en caliente, porque un borde duro roza la nuca; el hilo debe igualar el forro. Mantén la etiqueta del bolsillo fuera de la zona de roce de la mano, o se pelará en seis meses.",
    )),
    ("ul", [
        D("后领里布宽度决定主唛的最大宽度，先量里布再定尺寸",
          "The back-neck lining width caps the label width: measure the lining before fixing the size",
          "衿裏の裏地幅がメインラベルの最大幅を決めます。裏地を測ってから寸法を決めましょう",
          "목 뒤 안감 폭이 메인 라벨 최대 폭을 결정합니다. 안감을 먼저 재고 치수를 정하십시오",
          "La largeur de la doublure d'encolure plafonne celle du label : mesurez avant de figer la taille",
          "El ancho del forro del escote limita el de la etiqueta: mide antes de fijar la medida"),
        D("尺码标与主唛同排缝制，洗水标单独缝在侧缝或内袋，避免三标叠缝起硬块",
          "Sew size and neck labels on one line and keep the care label separate on the side seam or pocket to avoid a stacked hard lump",
          "サイズラベルとメインラベルは同じ行に、洗濯表示ラベルは脇縫いか内ポケットに分けて縫い、3枚重ねの硬い塊を避けます",
          "사이즈 라벨과 메인 라벨은 같은 줄에, 세탁 표시 라벨은 옆선이나 안주머니에 따로 달아 세 장이 겹친 딱딱한 덩어리를 피하십시오",
          "Cousez taille et col sur une ligne et placez l'étiquette d'entretien à part, couture latérale ou poche, pour éviter un paquet rigide",
          "Cose talla y cuello en una línea y deja la etiqueta de cuidado aparte, en costura lateral o bolsillo, para evitar un bulto rígido"),
        D("小批量定制单可以在内袋加手缝标，仪式感来自细节而不是厚度",
          "On small custom runs, a hand-sewn label inside the pocket adds ceremony through detail rather than bulk",
          "小ロットの別注では内ポケットに手縫いラベルを加えると、厚みではなく細部で特別感を出せます",
          "소량 맞춤 주문은 안주머니에 손바느질 라벨을 더하면 두께가 아니라 디테일로 특별함을 줍니다",
          "Sur les petites séries sur mesure, un label cousu main dans la poche apporte du caractère par le détail, pas par l'épaisseur",
          "En series cortas a medida, una etiqueta cosida a mano en el bolsillo aporta distinción por el detalle, no por el grosor"),
    ]),

    ("h2", D("3. 洗水标：干洗符号、羊毛成分与语言", "3. Care Labels: Dry-Clean Symbols, Wool Content and Languages",
             "3. 洗濯表示ラベル：ドライ記号、ウール組成、言語", "3. 세탁 표시 라벨: 드라이 기호, 울 성분, 언어",
             "3. Étiquettes d'entretien : symboles à sec, laine et langues", "3. Etiquetas de cuidado: símbolos en seco, lana e idiomas")),
    ("table", (
        [D("场景", "Topic", "項目", "항목", "Sujet", "Tema"),
         D("要点", "What to get right", "押さえるべき点", "핵심 포인트", "Points clés", "Puntos clave")],
        [
            [D("干洗符号", "Dry-clean symbols", "ドライ記号", "드라이 기호", "Symboles à sec", "Símbolos en seco"),
             D("使用 ISO 3758 现行版本，「仅干洗」与「可水洗」不可并存，P 与 F 溶剂符号要分清",
               "Use the current ISO 3758 version, never combine dry-clean only with washable, and keep the P and F solvent symbols distinct",
               "現行の ISO 3758 版を使用し、「ドライのみ」と「水洗可」は併記しない、P と F の溶剤記号を区別する",
               "현행 ISO 3758 버전을 사용하고, '드라이 전용'과 '물세탁 가능'을 함께 표기하지 않으며, P와 F 용제 기호를 구분합니다",
               "Utilisez la version en vigueur de l'ISO 3758, ne combinez jamais sec uniquement et lavable, et distinguez les solvants P et F",
               "Usa la versión vigente de ISO 3758, no combines solo seco con lavable y distingue los disolventes P y F")],
            [D("羊毛与真丝", "Wool and silk", "ウールとシルク", "울과 실크", "Laine et soie", "Lana y seda"),
             D("标注动物纤维名称与含量，欧盟市场对羊毛标注有专门规则，混纺要写清各成分比例",
               "Name the animal fibre and its content; the EU has dedicated wool labelling rules, and blends need every share stated",
               "動物繊維の名称と含有率を表示し、EU にはウール表示の専用規則があります。混紡は各成分の比率を明記します",
               "동물 섬유 명칭과 함량을 표시하고, EU에는 울 표시 전용 규칙이 있으며, 혼방은 각 성분 비율을 명시합니다",
               "Nommez la fibre animale et sa teneur ; l'UE a des règles spécifiques pour la laine, et les mélanges exigent toutes les parts",
               "Indica la fibra animal y su contenido; la UE tiene reglas específicas para la lana y las mezclas exigen todas las proporciones")],
            [D("多语言", "Languages", "多言語", "다국어", "Langues", "Idiomas"),
             D("按目标市场组合：欧美常配英法双语，拉美配西语，日韩另有本地表示习惯",
               "Match the target market: English and French for Europe and North America, Spanish for Latin America, local wording conventions for Japan and Korea",
               "対象市場に合わせて構成します。欧米は英語とフランス語の二言語、中南米はスペイン語、日本と韓国は現地の表示慣行に従います",
               "목표 시장에 맞춰 구성합니다. 유럽과 북미는 영어·프랑스어, 중남미는 스페인어, 일본과 한국은 현지 표기 관행을 따릅니다",
               "Selon le marché : anglais et français pour l'Europe et l'Amérique du Nord, espagnol pour l'Amérique latine, usages locaux au Japon et en Corée",
               "Según el mercado: inglés y francés para Europa y Norteamérica, español para Latinoamérica, usos locales en Japón y Corea")],
            [D("材质选择", "Material choice", "素材の選択", "소재 선택", "Choix du support", "Elección del soporte"),
             D("深色正装优先织带洗标，柔软耐磨；说明文字较多时改用涂层或印刷洗标",
               "Dark formalwear favours soft, durable tape care labels; when there is a lot of text, switch to coated or printed labels",
               "濃色フォーマルは柔らかく丈夫なテープ洗濯表示ラベルを優先し、説明文が多い場合はコーティングまたは印刷ラベルに切り替えます",
               "어두운 포멀 의류는 부드럽고 튼튼한 테이프 세탁 라벨을 우선하고, 설명이 많으면 코팅 또는 인쇄 라벨로 바꿉니다",
               "Le formel foncé privilégie le ruban souple et résistant ; avec beaucoup de texte, passez au support enduit ou imprimé",
               "La ropa formal oscura prefiere cinta suave y resistente; con mucho texto, cambia a soporte recubierto o impreso")],
        ])),

    ("h2", D("4. 吊牌：克重、工艺与悬挂方式", "4. Hang Tags: Weight, Finishing and How They Hang",
             "4. タグ：坪量、加工、掛け方", "4. 행택: 평량, 가공, 거는 방식",
             "4. Étiquettes suspendues : grammage, finition et suspension", "4. Colgantes: gramaje, acabado y forma de colgar")),
    ("p", D(
        "正装吊牌讲究「有分量但不招摇」：纸张多用 350 到 450 克特种纸或棉纸，配哑金或哑银烫印、压凹凸；竖版长方形配圆角刀模最常见。悬挂方式直接影响面料安全：西装多把吊绳穿过袖口扣眼或门襟扣眼，避免金属吊粒直接压住羊毛；大衣与礼服可用棉绳加吊粒穿过门襟扣眼，但要控制吊牌重量。价格牌与尺码贴优先贴在袖口或内袋上方，用可移除不干胶，撕后不留胶痕。",
        "Formalwear hang tags aim at weighty but understated: 350 to 450 gsm specialty or cotton paper, matte gold or silver foil, embossing, and most often a vertical rectangle with rounded corners. How it hangs decides whether the fabric survives: on suits the string goes through a cuff or placket buttonhole rather than letting a metal fastener press directly on wool; on coats and eveningwear a cotton string with a fastener through the placket works, provided the tag stays light. Put price tickets and size stickers on the cuff or above the inside pocket, using removable adhesive that leaves no residue.",
        "フォーマル用タグは「重みはあるが誇張しない」が基本です。用紙は350〜450gの特殊紙や綿紙、加工はマットゴールドやマットシルバーの箔押し、エンボス、形状は縦長の角丸型が最も一般的です。掛け方は生地の安全に直結します。スーツは袖口や前立てのボタンホールにひもを通し、金属留め具をウールに直接当てないようにします。コートや礼服は綿ひもと留め具を前立てのボタンホールに通せますが、タグの重量は抑えます。値札とサイズシールは袖口か内ポケットの上に、跡が残らない再剥離粘着で貼ります。",
        "포멀용 행택은 '무게감은 있되 과하지 않게'가 기본입니다. 용지는 350~450g 특수지나 면지를 쓰고, 무광 골드·실버 박, 엠보싱을 더하며, 세로형 직사각형에 둥근 모서리 금형이 가장 흔합니다. 거는 방식은 원단 안전에 직결됩니다. 수트는 소매 끝이나 앞여밈 단추 구멍에 끈을 걸어 금속 체결구가 울에 직접 닿지 않게 합니다. 코트와 예복은 면끈과 체결구를 앞여밈 단추 구멍에 걸 수 있지만 행택 무게를 줄여야 합니다. 가격표와 사이즈 스티커는 소매 끝이나 안주머니 위에 자국이 남지 않는 재박리 점착제로 붙입니다.",
        "L'étiquette suspendue formelle vise le poids sans l'ostentation : papier spécial ou coton de 350 à 450 g/m², dorure ou argenture mate, gaufrage, et le plus souvent un rectangle vertical à coins arrondis. La suspension conditionne la survie du tissu : sur un costume, le cordon passe par une boutonnière de manchette ou de patte plutôt qu'une fixation métallique posée sur la laine ; sur un manteau ou une tenue de soirée, un cordon coton avec fixation est acceptable si l'étiquette reste légère. Posez prix et tailles sur la manchette ou au-dessus de la poche, avec un adhésif amovible sans résidu.",
        "El colgante formal busca peso sin ostentación: papel especial o de algodón de 350 a 450 g/m², dorado o plateado mate, relieve y, casi siempre, rectángulo vertical de esquinas redondeadas. Cómo cuelga decide si el tejido sobrevive: en trajes, el cordón pasa por un ojal del puño o de la tapeta en lugar de dejar que un remache metálico presione la lana; en abrigos y ceremonia, un cordón de algodón con remache es válido si el colgante pesa poco. Coloca la etiqueta de precio y la talla en el puño o sobre el bolsillo interior, con adhesivo removible sin residuo.",
    )),
    ("callout", D(
        "<strong>💡 提示：</strong>正装面料一旦被吊牌压出光痕或钩出丝，基本无法修复。打样时把吊牌按最终悬挂方式挂在面料小样上放 24 小时，再确认克重与吊绳长度，比在电脑上看效果图可靠得多。",
        "<strong>💡 Tip:</strong> once formalwear fabric is marked by a tag or snagged, it rarely recovers. During sampling, hang the tag on a fabric swatch in its final position for 24 hours before confirming weight and string length; it beats any on-screen mock-up.",
        "<strong>💡 ヒント：</strong>フォーマル生地は、タグの押し跡や引っかけが付くとほぼ修復できません。サンプル時に最終の掛け方で生地小片にタグを掛けて24時間置き、そのうえで坪量とひも長を確認すると、画面上のイメージよりはるかに確実です。",
        "<strong>💡 팁:</strong> 포멀 원단은 행택 눌린 자국이나 올이 나간 흔적이 생기면 거의 복구되지 않습니다. 샘플 단계에서 최종 거는 방식으로 원단 조각에 행택을 걸어 24시간 둔 뒤 평량과 끈 길이를 확정하는 편이 화면 시안보다 훨씬 확실합니다.",
        "<strong>💡 Conseil :</strong> un tissu formel marqué par une étiquette ou accroché ne se rattrape guère. Pendant l'échantillon, suspendez l'étiquette sur un carré de tissu dans sa position finale pendant 24 heures avant de figer grammage et longueur de cordon : plus fiable qu'un visuel à l'écran.",
        "<strong>💡 Consejo:</strong> un tejido formal marcado por el colgante o enganchado casi nunca se recupera. En la muestra, cuelga el colgante sobre un recorte de tejido en su posición final durante 24 horas antes de fijar gramaje y largo del cordón: mucho más fiable que un montaje en pantalla.",
    )),

    ("h2", D("5. 包装：挂装、防皱与防潮", "5. Packaging: Hanging, Crease-Free and Moisture-Safe",
             "5. 包装：掛け姿、防皺、防湿", "5. 포장: 걸이, 주름 방지, 습기 방지",
             "5. Emballage : sur cintre, sans plis, à l'abri de l'humidité", "5. Embalaje: colgado, sin arrugas y protegido de la humedad")),
    ("ul", [
        D("<strong>挂装为主：</strong>挂衣袋配衣架与防滑肩垫，外箱建议用挂装纸箱，肩部不被压",
          "<strong>Hanging as standard:</strong> a garment bag on a hanger with anti-slip shoulder pads, shipped in hanging cartons so shoulders are never compressed",
          "<strong>掛け姿が基本：</strong>ハンガーと滑り止め肩パッド付きのガーメントバッグを使い、外箱は掛け姿用のカートンにして肩を圧迫しないようにします",
          "<strong>걸이 상태가 기본:</strong> 옷걸이와 미끄럼 방지 어깨 패드를 갖춘 가먼트 백을 사용하고, 걸이용 카톤으로 포장해 어깨가 눌리지 않게 합니다",
          "<strong>Sur cintre avant tout :</strong> housse sur cintre avec pattes d'épaule antidérapantes, expédiée en carton sur cintre pour ne jamais comprimer les épaules",
          "<strong>Colgado como norma:</strong> funda sobre percha con hombreras antideslizantes, en caja de colgado para que los hombros no se compriman"),
        D("<strong>折装场景：</strong>衬衫与礼服可选折装，用薄纸包裹并加硬纸托，减少折痕",
          "<strong>Folded options:</strong> shirts and some eveningwear can travel folded, wrapped in tissue with a cardboard insert to limit creasing",
          "<strong>折り畳みの場合：</strong>シャツや礼服は折り畳みも可能で、薄紙で包み厚紙の芯を入れて折り目を抑えます",
          "<strong>접힘 포장:</strong> 셔츠와 일부 예복은 접어서 보낼 수 있으며, 얇은 종이로 감싸고 두꺼운 종이 받침을 넣어 주름을 줄입니다",
          "<strong>Version pliée :</strong> chemises et certaines tenues de soirée voyagent pliées, enveloppées de papier de soie avec un renfort carton",
          "<strong>Opción plegada:</strong> camisas y algo de ceremonia viajan plegadas, envueltas en papel de seda con refuerzo de cartón"),
        D("<strong>防潮防蛀：</strong>羊毛易吸潮、易虫蛀，长途海运建议每件配干燥剂，箱内加防潮纸",
          "<strong>Moisture and moths:</strong> wool absorbs humidity and attracts moths, so long sea freight benefits from a desiccant per piece and moisture-barrier paper in the carton",
          "<strong>防湿・防虫：</strong>ウールは湿気を吸いやすく虫害も受けやすいため、長距離海上輸送では1着ごとに乾燥剤を入れ、箱内に防湿紙を敷きます",
          "<strong>방습·방충:</strong> 울은 습기를 잘 흡수하고 좀벌레 피해를 받기 쉬워, 장거리 해상 운송에는 개당 건조제를 넣고 박스 안에 방습지를 깝니다",
          "<strong>Humidité et mites :</strong> la laine absorbe l'humidité et attire les mites : en maritime longue distance, prévoyez un dessiccant par pièce et un papier barrière dans le carton",
          "<strong>Humedad y polillas:</strong> la lana absorbe humedad y atrae polillas, así que en marítimo largo conviene un desecante por pieza y papel barrera en la caja"),
        D("<strong>开箱体验：</strong>吊牌、腰封与包装袋同色系成套，开箱顺序按「袋、腰封、吊牌」设计",
          "<strong>Unboxing:</strong> keep tag, belly band and bag in one colour family, and design the unboxing order as bag, band, tag",
          "<strong>開梱体験：</strong>タグ・帯・包装袋を同系色で揃え、開梱の順序は「袋→帯→タグ」を意識して設計します",
          "<strong>개봉 경험:</strong> 행택, 밴드, 포장백을 같은 색 계열로 맞추고 개봉 순서를 '백→밴드→행택'으로 설계합니다",
          "<strong>Déballage :</strong> gardez étiquette, bandeau et sac dans la même famille de couleurs et concevez l'ordre sac, bandeau, étiquette",
          "<strong>Desembalaje:</strong> mantén colgante, fajín y bolsa en la misma gama y diseña el orden bolsa, fajín, colgante"),
    ]),

    ("h2", D("6. 职业装、校服与礼服的差异与打样核对", "6. Uniforms, Schoolwear and Eveningwear, Plus a Sampling Check",
             "6. 制服・学校服・礼服の違いとサンプル確認", "6. 유니폼·교복·예복의 차이와 샘플 점검",
             "6. Uniforme, scolaire et soirée, et la vérification d'échantillon", "6. Uniforme, escolar y ceremonia, y la comprobación de muestra")),
    ("table", (
        [D("品类", "Category", "品種", "품목", "Catégorie", "Categoría"),
         D("辅料重点", "Trim priority", "副資材の重点", "부자재 중점", "Priorité accessoires", "Prioridad de accesorios"),
         D("常见做法", "Common practice", "一般的な方法", "일반적인 방식", "Pratique courante", "Práctica habitual")],
        [
            [D("职业装与制服", "Uniforms and workwear", "制服・ユニフォーム", "유니폼·제복", "Uniformes et vêtements pro", "Uniformes y ropa laboral"),
             D("用量大、洗涤频繁，标签要经得起多次洗涤", "High volume and frequent washing, so labels must survive many cycles",
               "数量が多く洗濯も頻繁なため、ラベルは多数回の洗濯に耐える必要があります",
               "수량이 많고 세탁이 잦아 라벨이 여러 번의 세탁을 견뎌야 합니다",
               "Volume élevé et lavages fréquents : les labels doivent tenir de nombreux cycles",
               "Gran volumen y lavados frecuentes: las etiquetas deben aguantar muchos ciclos"),
             D("优先可机洗的印刷洗标与低成本主唛，锁定洗涤次数指标", "Favour machine-washable printed care labels and economical neck labels, with a stated wash-cycle target",
               "家庭洗濯可能な印刷洗濯ラベルと低コストのメインラベルを優先し、洗濯回数の目標を定めます",
               "가정용 세탁이 가능한 인쇄 세탁 라벨과 저비용 메인 라벨을 우선하고 세탁 횟수 목표를 정합니다",
               "Privilégiez les étiquettes imprimées lavables en machine et des labels de col économiques, avec un objectif de cycles",
               "Prioriza etiquetas impresas lavables a máquina y etiquetas de cuello económicas, con un objetivo de ciclos")],
            [D("校服", "Schoolwear", "学校服", "교복", "Scolaire", "Escolar"),
             D("需要可写姓名与班级的区域，同时满足儿童安全要求", "Needs a writable area for name and class, plus childrenswear safety rules",
               "記名欄（氏名とクラス）が必要で、子供向け安全要件も満たす必要があります",
               "이름과 반을 적을 수 있는 영역이 필요하고 아동복 안전 요건도 충족해야 합니다",
               "Besoin d'une zone inscriptible pour nom et classe, et respect des règles enfants",
               "Necesita zona escribible para nombre y clase, además de las normas de seguridad infantil"),
             D("预留空白标或空白卡吊牌，配耐洗洗标与圆角设计", "Leave a blank label or blank card tag, with wash-resistant care labels and rounded edges",
               "空白ラベルや白紙タグを用意し、耐洗濯の洗濯表示ラベルと角丸形状を組み合わせます",
               "공백 라벨이나 백지 행택을 두고 세탁에 강한 세탁 라벨과 둥근 모서리를 적용합니다",
               "Prévoyez un label ou une carte vierge, avec étiquettes d'entretien résistantes et coins arrondis",
               "Deja una etiqueta o tarjeta en blanco, con etiquetas de cuidado resistentes y esquinas redondeadas")],
            [D("礼服与定制", "Eveningwear and made-to-measure", "礼服・別注", "예복·맞춤", "Soirée et sur mesure", "Ceremonia y a medida"),
             D("单件小批量，重工艺细节与品牌仪式感", "Small and single-piece runs where craft detail and brand ritual matter",
               "単品・小ロットで、工芸的な細部とブランドの特別感が重視されます",
               "단품·소량 주문으로 공예적 디테일과 브랜드 의식이 중요합니다",
               "Petites séries et pièces uniques, où le détail artisanal et le rituel de marque comptent",
               "Series cortas y piezas únicas, donde importan el detalle artesanal y el ritual de marca"),
             D("烫金、压印、手缝标，允许规格灵活度高于成本控制", "Foil, embossing and hand-sewn labels, with specification flexibility ranked above cost",
               "箔押し・エンボス・手縫いラベルを採用し、コストより仕様の柔軟性を優先します",
               "박, 엠보싱, 손바느질 라벨을 적용하고 비용보다 사양 유연성을 우선합니다",
               "Dorure, gaufrage et labels cousus main, la souplesse de spécification primant sur le coût",
               "Dorado, relieve y etiquetas cosidas a mano, con la flexibilidad de especificación por encima del coste")],
        ])),
    ("ol", [
        D("主唛宽度是否与后领里布匹配，折法与切边是否确认", "Does the neck label width match the back lining, and are fold and cut confirmed",
          "メインラベルの幅が衿裏の裏地に合っているか、折りと裁断は確定しているか", "메인 라벨 폭이 목 뒤 안감과 맞는가, 접힘과 재단이 확정되었는가",
          "La largeur du label correspond-elle à la doublure, pliage et coupe validés", "¿El ancho de la etiqueta encaja con el forro y están confirmados plegado y corte"),
        D("洗水标的干洗符号版本、语言组合与成分比例是否与目标市场一致", "Do the dry-clean symbol version, language set and fibre percentages match the target market",
          "洗濯表示ラベルのドライ記号の版、言語構成、組成比率が対象市場と一致しているか", "세탁 표시 라벨의 드라이 기호 버전, 언어 구성, 성분 비율이 목표 시장과 일치하는가",
          "Version des symboles, langues et pourcentages correspondent-ils au marché visé", "¿La versión de símbolos, los idiomas y los porcentajes coinciden con el mercado"),
        D("吊牌克重、烫印颜色与吊绳长度是否用面料小样验证过", "Were tag weight, foil colour and string length verified on an actual fabric swatch",
          "タグの坪量、箔の色、ひも長を生地小片で検証したか", "행택 평량, 박 색상, 끈 길이를 원단 조각으로 검증했는가",
          "Grammage, couleur de dorure et longueur de cordon ont-ils été vérifiés sur un carré de tissu", "¿Se verificaron gramaje, color de dorado y largo del cordón sobre un recorte de tejido"),
        D("包装方式、箱规与防潮方案是否确认，挂装纸箱高度是否够", "Are packing method, carton size and moisture plan confirmed, and is the hanging carton tall enough",
          "包装方法・箱規・防湿対策は確認済みか、掛け姿カートンの高さは足りるか", "포장 방식, 박스 규격, 방습 대책이 확인되었는가, 걸이 카톤 높이가 충분한가",
          "Mode de conditionnement, carton et protection humidité sont-ils validés, la hauteur du carton sur cintre suffit-elle", "¿Están confirmados embalaje, caja y protección antihumedad, y basta la altura del cartón colgado"),
        D("尺码标的号型体系与内销外销标识是否对齐", "Do size labels align with the sizing system and domestic versus export marking rules",
          "サイズラベルの号型体系が内販・輸出の表示ルールと一致しているか", "사이즈 라벨의 호수 체계가 내수·수출 표시 규칙과 일치하는가",
          "Les labels de taille suivent-ils le système et les règles d'étiquetage domestique ou export", "¿Las etiquetas de talla siguen el sistema y las reglas de marcado nacional o exportación"),
    ]),
]

ARTICLES = [
    dict(
        slug="apparel-trims-spec-sheet-guide.html",
        title=D("服装辅料规格书怎么写：吊牌、织唛、洗水标与包装袋字段清单 | TAGE",
                "How to Write a Garment Trims Spec Sheet: Fields for Tags, Labels &amp; Bags | TAGE",
                "衣料副資材の仕様書の書き方：タグ・織りラベル・洗濯表示ラベル・包装袋の項目リスト | TAGE",
                "의류 부자재 사양서 작성법: 행택·직조 라벨·세탁 표시 라벨·포장백 항목 정리 | TAGE",
                "Comment rédiger une fiche de spécifications d'accessoires : étiquettes, labels et sacs | TAGE",
                "Cómo redactar una ficha de especificaciones de accesorios: colgantes, etiquetas y bolsas | TAGE"),
        desc=D("服装辅料规格书怎么写？本文给出吊牌、织唛、洗水标、包装袋四类辅料的必填字段清单：材质克重、成品尺寸与公差、颜色色样、工艺组合、语言版本、数量包装与文件版本控制，并附四个漏填事故与打样前核对清单。来自东莞泰阁包装。",
               "How to write a garment trims spec sheet: the fields that prevent rework — material and weight, size and tolerance, colour, finishing, text versions and packing.",
               "衣料副資材の仕様書に書くべき項目を、タグ・織りラベル・洗濯表示ラベル・包装袋ごとに整理。素材と坪量、仕上がり寸法と公差、色基準、加工の組み合わせ、言語版、数量と包装、版管理までを解説します。東莞泰閣包装。",
               "의류 부자재 사양서에 기재할 항목을 행택·직조 라벨·세탁 표시 라벨·포장백별로 정리했습니다. 소재와 평량, 완성 치수와 공차, 색상 기준, 가공 조합, 언어 버전, 수량과 포장, 버전 관리까지 설명합니다. 둥관 TAGE 패키징.",
               "Fiche de spécifications d'accessoires : les champs à renseigner, matière et grammage, dimensions et tolérances, couleur, finitions, versions linguistiques et conditionnement.",
               "Ficha de especificaciones de accesorios: los campos que evitan reprocesos, material y gramaje, medidas y tolerancias, color, acabados, versiones de idioma y embalaje."),
        crumb=D("辅料规格书编写", "Trims Spec Sheet", "副資材仕様書の書き方", "부자재 사양서 작성",
                "Rédiger une fiche de spécifications", "Redactar una ficha de especificaciones"),
        h1=D("服装辅料规格书怎么写：吊牌、织唛、洗水标与包装袋字段清单",
             "How to Write a Garment Trims Spec Sheet: Fields for Tags, Labels and Bags",
             "衣料副資材の仕様書の書き方：タグ・織りラベル・洗濯表示ラベル・包装袋の項目リスト",
             "의류 부자재 사양서 작성법: 행택·직조 라벨·세탁 표시 라벨·포장백 항목 정리",
             "Comment rédiger une fiche de spécifications d'accessoires : étiquettes, labels et sacs",
             "Cómo redactar una ficha de especificaciones de accesorios: colgantes, etiquetas y bolsas"),
        tag=D("采购实务", "Sourcing", "調達実務", "소싱 실무", "Approvisionnement", "Compras"),
        sum=D("辅料返工很少是工厂做不出来，而是规格书没说清：同一句「白色棉绳吊牌」可以对应三种纸张、两种绳子。本文给出一份可以直接抄用的字段清单，吊牌、织唛、洗水标、包装袋各自必填什么，颜色与公差怎么写进文件，语言版本怎么排队，版本如何控，并附最常见的四个漏填事故与打样前核对清单。",
              "Trims rework rarely comes from a factory that cannot deliver; it comes from a spec sheet that never said it. Here is a field-by-field checklist for hang tags, woven labels, care labels and bags, what to write for colour and tolerance, how to queue language versions and control document versions.",
              "副資材の手直しは、工場が作れないからではなく仕様が書かれていないから起こります。「白い綿ひも付きタグ」の一文が紙3種・ひも2種を意味し得ます。タグ、織りラベル、洗濯表示ラベル、包装袋ごとの必須項目、色と公差の数値化、言語版の整理、版管理、最も多い4つの記載漏れとサンプル前チェックリストをまとめました。",
              "부자재 재작업은 공장이 못 만들어서가 아니라 사양서에 적혀 있지 않아서 생깁니다. '흰색 면끈 행택' 한 문장이 종이 3가지, 끈 2가지를 뜻할 수 있습니다. 행택, 직조 라벨, 세탁 표시 라벨, 포장백별 필수 항목, 색상과 공차의 수치화, 언어 버전 정리, 버전 관리, 그리고 가장 흔한 네 가지 누락 사례와 샘플 전 점검 리스트를 정리했습니다.",
              "Une reprise d'accessoire vient rarement d'une usine incapable, mais d'une fiche qui n'a rien dit. Voici une liste de champs par famille, étiquettes suspendues, labels tissés, étiquettes d'entretien et sacs, avec couleur et tolérances chiffrées, gestion des langues et des versions, et les quatre oublis les plus fréquents.",
              "Un reproceso de accesorios rara vez viene de una fábrica incapaz, sino de una ficha que no dijo nada. Aquí tienes la lista de campos por familia, colgantes, etiquetas tejidas, etiquetas de cuidado y bolsas, con color y tolerancias en cifras, gestión de idiomas y versiones, y las cuatro omisiones más habituales."),
        cta=D("准备把吊牌、织唛、洗水标或包装袋的规格整理成一份可以直接下单的文件？把现有草稿或样品照片发给我们，我们按字段帮你补齐缺口，三到七天寄出实物样品确认。",
              "Turning trims specifications into a document your supplier can quote from? Send us your draft or sample photos: we fill the gaps field by field and ship physical samples in three to seven days.",
              "タグ・織りラベル・洗濯表示ラベル・包装袋の仕様を、そのまま発注できる文書にまとめませんか。現行のドラフトや見本写真をお送りいただければ、項目ごとに不足を補い、3〜7日で実物サンプルをお届けします。",
              "행택·직조 라벨·세탁 표시 라벨·포장백 사양을 바로 발주할 수 있는 문서로 정리하시겠습니까? 기존 초안이나 샘플 사진을 보내주시면 항목별로 빠진 부분을 채우고 3~7일 내에 실물 샘플을 발송합니다.",
              "Vous transformez vos spécifications en document exploitable par votre fournisseur ? Envoyez-nous votre projet ou des photos d'échantillons : nous complétons les champs manquants et expédions les échantillons en trois à sept jours.",
              "¿Estás convirtiendo tus especificaciones en un documento que tu proveedor pueda presupuestar? Envíanos tu borrador o fotos de muestras: completamos los campos que faltan y enviamos muestras físicas en tres a siete días."),
        cta_btn=D("获取辅料报价 →", "Request a trims quote →", "副資材のお見積りを依頼 →", "부자재 견적 요청 →",
                  "Demander un devis accessoires →", "Solicitar presupuesto de accesorios →"),
        blocks=ART1_BLOCKS,
        related=["garment-trims-order-guide.html", "woven-label-folding-finishing.html", "care-label-multilingual-guide.html"],
    ),
    dict(
        slug="suiting-formalwear-trims-guide.html",
        title=D("西装与正装类服装辅料指南：羊毛面料标签、干洗标识与吊牌搭配 | TAGE",
                "Suiting &amp; Formalwear Trims Guide: Wool Labels, Dry-Clean Care Tags and Hang Tags | TAGE",
                "スーツ・フォーマル衣料の副資材ガイド：ウール素材のラベル、ドライ表示、タグの組み合わせ | TAGE",
                "수트·정장 의류 부자재 가이드: 울 소재 라벨, 드라이클리닝 표시, 행택 조합 | TAGE",
                "Guide des accessoires pour costume et tenue formelle : labels laine, entretien à sec, étiquettes suspendues | TAGE",
                "Guía de accesorios para traje y ropa formal: etiquetas de lana, cuidado en seco y colgantes | TAGE"),
        desc=D("西装、大衣与礼服类正装辅料选型指南：缎面主唛与尺码标的位置与折法、干洗符号与羊毛成分标注要求、吊牌克重与烫印工艺搭配、挂装防皱防潮包装方案，并对比职业装、校服与礼服的差异。附打样前核对清单。来自东莞泰阁包装。",
               "Suiting and formalwear trims: satin neck and size labels, dry-clean symbols, wool content rules, weighted foil hang tags, and hanging, crease-free packaging.",
               "スーツ・大衣・礼服などフォーマル衣料の副資材ガイド。サテンのメインラベルとサイズラベルの位置と折り、ドライ記号とウール組成の表示要件、タグの坪量と箔加工、掛け姿の防皺・防湿包装、制服・学校服・礼服の違い、サンプル前チェックリストを解説。東莞泰閣包装。",
               "수트·코트·예복 등 포멀 의류 부자재 가이드. 새틴 메인 라벨과 사이즈 라벨의 위치와 접힘, 드라이 기호와 울 성분 표시 요건, 행택 평량과 박 가공, 걸이 포장의 주름·습기 방지, 유니폼·교복·예복 차이, 샘플 전 점검 리스트를 다룹니다. 둥관 TAGE 패키징.",
               "Accessoires pour costume et formel : labels satin et de taille, symboles de nettoyage à sec, règles sur la laine, étiquettes suspendues dorées et emballage sur cintre sans plis.",
               "Accesorios para traje y ropa formal: etiquetas de satén y de talla, símbolos de limpieza en seco, reglas sobre la lana, colgantes con dorado y embalaje colgado sin arrugas."),
        crumb=D("正装辅料指南", "Formalwear Trims", "フォーマル副資材", "정장 부자재",
                "Accessoires du formel", "Accesorios formales"),
        h1=D("西装与正装类服装辅料指南：羊毛面料标签、干洗标识与吊牌搭配",
             "Suiting and Formalwear Trims: Wool Labels, Dry-Clean Care Tags and Hang Tags",
             "スーツ・フォーマル衣料の副資材ガイド：ウール素材のラベル、ドライ表示、タグの組み合わせ",
             "수트·정장 의류 부자재 가이드: 울 소재 라벨, 드라이클리닝 표시, 행택 조합",
             "Accessoires pour costume et tenue formelle : labels laine, entretien à sec et étiquettes suspendues",
             "Accesorios para traje y ropa formal: etiquetas de lana, cuidado en seco y colgantes"),
        tag=D("品类指南", "Category Guide", "品種ガイド", "품목 가이드", "Guide par catégorie", "Guía por categoría"),
        sum=D("西装、大衣与礼服的正装辅料用量不大，要求却最苛刻：面料怕勾丝、必须挂装运输，干洗符号与羊毛成分标注容错率极低。本文讲清缎面主唛与尺码标的位置与折法、干洗符号与语言组合、吊牌克重与烫印搭配、挂装防皱防潮包装，并对比职业装、校服与礼服的差异，附打样核对清单。",
              "Formalwear uses little trim but demands the most: fabric that snags, shipping that must hang, and almost no tolerance on dry-clean symbols or wool content. This guide covers satin neck and size labels, dry-clean symbols and language sets, tag weight with foil finishing, hanging and crease-free packaging, and how uniforms, schoolwear and eveningwear differ.",
              "スーツ・コート・フォーマルの副資材は使用量が少ない一方で要求が最も厳しく、生地は引っかけに弱く、輸送は掛け姿が前提、ドライ記号やウール組成の許容度はほぼゼロです。サテンのメインラベルとサイズラベルの位置と折り、ドライ記号と言語セット、タグの坪量と箔加工、掛け姿の防皺・防湿包装、制服・学校服・礼服の違い、サンプル前チェックリストを解説します。",
              "수트, 코트, 포멀 의류는 부자재 사용량은 적지만 요구 조건이 가장 까다롭습니다. 원단은 올이 나가기 쉽고, 운송은 걸이 상태가 기본이며, 드라이 기호와 울 성분 표기의 허용 오차는 거의 없습니다. 새틴 메인 라벨과 사이즈 라벨의 위치와 접힘, 드라이 기호와 언어 세트, 행택 평량과 박 가공, 걸이 포장의 주름·습기 방지, 유니폼·교복·예복의 차이, 샘플 전 점검 리스트를 다룹니다.",
              "Le formel utilise peu d'accessoires mais en exige le plus : tissu qui s'accroche, expédition sur cintre, et presque aucune marge sur les symboles de nettoyage à sec ou la laine. Ce guide traite labels satin et de taille, symboles et langues, grammage et dorure, emballage sur cintre sans plis, et les différences uniforme, scolaire, soirée.",
              "La ropa formal usa pocos accesorios pero exige lo máximo: tejido que se engancha, envío colgado y casi nulo margen en símbolos de limpieza en seco o contenido de lana. Esta guía cubre etiquetas de satén y de talla, símbolos e idiomas, gramaje y dorado, embalaje colgado sin arrugas y las diferencias entre uniforme, escolar y ceremonia."),
        cta=D("正在为西装、大衣或礼服系列定做主唛、洗水标、吊牌与挂装包装？把面料成分、干洗要求与目标市场发给我们，三到七天寄出实物样品确认。",
              "Specifying neck labels, care labels, hang tags and hanging packaging for a suit, coat or formalwear line? Send us the fibre content, dry-clean requirements and target markets: samples ship in three to seven days.",
              "スーツ・コート・フォーマルのメインラベル、洗濯表示ラベル、タグ、掛け姿包装をご検討ですか。生地組成、ドライ条件、対象市場をお送りいただければ、3〜7日で実物サンプルをお届けします。",
              "수트, 코트, 포멀 라인의 메인 라벨, 세탁 표시 라벨, 행택, 걸이 포장을 준비 중이십니까? 원단 조성, 드라이클리닝 조건, 목표 시장을 보내주시면 3~7일 내에 실물 샘플을 발송합니다.",
              "Vous définissez labels de col, étiquettes d'entretien, étiquettes suspendues et emballage sur cintre pour une ligne costume, manteau ou formelle ? Envoyez composition, exigences de nettoyage à sec et marchés cibles : échantillons en trois à sept jours.",
              "¿Defines etiquetas de cuello, de cuidado, colgantes y embalaje colgado para una línea de trajes, abrigos o formal? Envíanos composición, requisitos de limpieza en seco y mercados destino: muestras en tres a siete días."),
        cta_btn=D("获取正装辅料报价 →", "Request a formalwear trims quote →", "フォーマル副資材のお見積りを依頼 →",
                  "포멀 부자재 견적 요청 →", "Demander un devis accessoires formels →", "Solicitar presupuesto de accesorios formales →"),
        blocks=ART2_BLOCKS,
        related=["care-label-standards.html", "poly-bag-types.html", "woven-label-material-guide.html"],
    ),
]


# ---------------------------------------------------------------- 渲染
def render_body(a):
    s = '  <section class="article-body">\n    <div class="container">\n\n'
    blocks = []
    for b in a["blocks"]:
        blocks.append(b)
    for kind, payload in blocks:
        if kind == "p":
            s += P(payload) + "\n"
        elif kind == "h2":
            s += H2(payload) + "\n"
        elif kind == "h3":
            s += H3(payload) + "\n"
        elif kind == "ul":
            s += UL(payload, "ul") + "\n"
        elif kind == "ol":
            s += UL(payload, "ol") + "\n"
        elif kind == "callout":
            s += CALLOUT(payload) + "\n"
        elif kind == "table":
            s += TABLE(payload[0], payload[1]) + "\n"
        else:
            raise SystemExit("未知块类型 %s" % kind)

    # 相关文章（链接文字取目标文章 h1 的六语属性，保持一致）
    s += H2(D("相关文章", "Related Articles", "関連記事", "관련 기사", "Articles connexes", "Artículos relacionados")) + "\n"
    items = [("index.html", D("辅料 FAQ：全部文章", "Trims FAQ: all articles", "副資材 FAQ：すべての記事",
                              "부자재 FAQ: 전체 글", "FAQ Accessoires : tous les articles",
                              "FAQ Accesorios: todos los artículos"))]
    for rel in a["related"]:
        path = os.path.join("blog", rel)
        src = open(path, encoding="utf-8").read()
        m = re.search(r"<h1 ((?:data-(?:zh|en|ja|ko|fr|es)=\"[^\"]*\"\s*)+)>", src)
        assert m, "取不到 %s 的 h1 属性" % path
        d = {}
        for k, v in re.findall(r'data-(zh|en|ja|ko|fr|es)="([^"]*)"', m.group(1)):
            d[k] = v
        assert set(d) == set(L6), "%s h1 缺语种：%s" % (path, sorted(d))
        items.append((rel, d))
    s += "      <ul>\n"
    for href, d in items:
        s += '        <li><a href="%s" %s>%s</a></li>\n' % (href, attrs_line(d, ""), d["zh"])
    s += "      </ul>\n\n"

    # CTA
    s += '      <div class="cta-box">\n'
    s += P(a["cta"], "        ")
    s += '        <a class="cta-btn" href="../contact.html" %s>%s</a>\n' % (attrs_line(a["cta_btn"], ""), a["cta_btn"]["zh"])
    s += "      </div>\n\n    </div>\n  </section>\n"
    return s


def build_articles():
    skel = open(SKEL, encoding="utf-8").read()
    meta_line = D("泰阁包装 · 更新于 %s" % DATE_ZH,
                  "By TAGE Packaging &nbsp;·&nbsp; Updated %s" % DATE_EN,
                  "泰閣包裝 · %s更新" % DATE_JA,
                  "TAGE 패키징 · %s 업데이트" % DATE_KO,
                  "Par TAGE Packaging &nbsp;·&nbsp; Mis à jour le %s" % DATE_FR,
                  "Por TAGE Packaging &nbsp;·&nbsp; Actualizado el %s" % DATE_ES)

    for a in ARTICLES:
        # 安全闸
        for p in ("blog/%s" % a["slug"], "en/blog/%s" % a["slug"], "ja/blog/%s" % a["slug"],
                  "ko/blog/%s" % a["slug"], "fr/blog/%s" % a["slug"], "es/blog/%s" % a["slug"]):
            assert not os.path.exists(p), "选题撞车：%s 已存在" % p
        assert ("/blog/%s</loc>" % a["slug"]) not in open("sitemap.xml", encoding="utf-8").read(), \
            "sitemap 已含 %s" % a["slug"]

        s = skel.replace("knitwear-sweater-trims-guide.html", a["slug"])

        # title（六语属性 + 中文静态内容）
        s = re.sub(r"<title[^>]*>.*?</title>",
                   '<title %s>%s</title>' % (attrs_line(a["title"], ""), a["title"]["zh"]), s, count=1, flags=re.S)

        # description（六语属性，全量替换）
        desc_block = '<meta name="description"\n' + "".join(
            '      data-%s="%s"\n' % (k, a["desc"][k]) for k in L6) + '      content="%s">' % a["desc"]["zh"]
        s, n = re.subn(r'<meta name="description".*?content="[^"]*">', lambda m: desc_block, s, count=1, flags=re.S)
        assert n == 1, "description 替换失败"

        # hreflang 六语（骨架已含 ja/ko，只需保留即可，slug 已换）
        assert 'hreflang="ja"' in s and 'hreflang="ko"' in s

        # crumb
        crumb = ('<div class="crumb"><a href="../index.html" %s>首页</a> / <a href="index.html" %s>辅料 FAQ</a>'
                 ' / <span %s>%s</span></div>'
                 % (attrs_line(D("首页", "Home", "ホーム", "홈", "Accueil", "Inicio"), ""),
                    attrs_line(D("辅料 FAQ", "Trims FAQ", "副資材 FAQ", "부자재 FAQ", "FAQ Accessoires", "FAQ Accesorios"), ""),
                    attrs_line(a["crumb"], ""), a["crumb"]["zh"]))
        s, n = re.subn(r'<div class="crumb">.*?</div>', lambda m: crumb, s, count=1, flags=re.S)
        assert n == 1, "crumb 替换失败"

        # h1
        s, n = re.subn(r"<h1 .*?</h1>", lambda m: '<h1 %s>%s</h1>' % (attrs_line(a["h1"], ""), a["h1"]["zh"]),
                       s, count=1, flags=re.S)
        assert n == 1, "h1 替换失败"

        # meta 行（日期）
        s, n = re.subn(r'<p data-zh="泰閣包裝 · 更新於[^"]*".*?</p>',
                       lambda m: P(meta_line), s, count=1, flags=re.S)
        assert n == 1, "meta 行替换失败"

        # JSON-LD breadcrumb（第三项）与 headline
        old_h1 = re.search(r'<h1 [^>]*data-zh="([^"]*)"', skel).group(1)
        s = s.replace('"name": "%s"' % old_h1, '"name": "%s"' % a["h1"]["zh"])
        s, n = re.subn(r'"headline": "[^"]*"', lambda m: '"headline": "%s"' % a["h1"]["zh"], s, count=1)
        assert n == 1, "headline 替换失败"

        # 正文
        body = render_body(a)
        i0 = s.index('  <section class="article-body">')
        i1 = s.index("\n</main>")
        s = s[:i0] + body + s[i1:]

        out = "blog/%s" % a["slug"]
        with open(out, "w", encoding="utf-8", newline="") as f:
            f.write(s)
        with open("blog/_body_%s" % a["slug"], "w", encoding="utf-8", newline="") as f:
            f.write(body)
        print("写入 %s（%d 字节）zh_desc=%d字 en_desc=%d字符" %
              (out, len(s.encode("utf-8")), len(a["desc"]["zh"]), len(a["desc"]["en"])))

    # ---------------- 列表页卡片 ----------------
    CARD = '''      <article class="post-card">
        <span class="tag" %(tag)s>%(tag_zh)s</span>
        <h3 %(h3)s>%(h3_zh)s</h3>
        <p %(sum)s>%(sum_zh)s</p>
        <a class="more" href="%(slug)s" %(more)s>阅读全文 →</a>
      </article>

'''
    more = D("阅读全文 →", "Read more →", "続きを読む →", "자세히 보기 →", "Lire la suite →", "Leer más →")
    idx = "blog/index.html"
    s = open(idx, encoding="utf-8").read()
    marker = '<div class="post-grid">\n'
    assert marker in s, "post-grid 未找到"
    cards = ""
    for a in ARTICLES:
        assert a["slug"] not in s, "卡片已存在：%s" % a["slug"]
        cards += CARD % dict(tag=attrs_line(a["tag"], ""), tag_zh=a["tag"]["zh"],
                             h3=attrs_line(a["h1"], ""), h3_zh=a["h1"]["zh"],
                             sum=attrs_line(a["sum"], ""), sum_zh=a["sum"]["zh"],
                             slug=a["slug"], more=attrs_line(more, ""))
    s = s.replace(marker, marker + "\n" + cards, 1)
    with open(idx, "w", encoding="utf-8", newline="") as f:
        f.write(s)
    print("blog/index.html 插入 %d 张卡片" % len(ARTICLES))

    # ---------------- sitemap ----------------
    PREF = [("blog/", "monthly", "0.7"), ("en/blog/", "monthly", "0.7"), ("ja/blog/", "monthly", "0.7"),
            ("ko/blog/", "monthly", "0.7"), ("fr/blog/", "monthly", "0.7"), ("es/blog/", "monthly", "0.7")]
    sp = "sitemap.xml"
    s = open(sp, encoding="utf-8", newline="").read()
    for loc in ["https://taigetag.com/blog/index.html", "https://taigetag.com/en/blog/index.html",
                "https://taigetag.com/ja/blog/index.html", "https://taigetag.com/ko/blog/index.html",
                "https://taigetag.com/fr/blog/index.html", "https://taigetag.com/es/blog/index.html"]:
        pat = re.compile(r"(<loc>%s</loc>\r?\n\s*<lastmod>)[^<]*(</lastmod>)" % re.escape(loc))
        s, n = pat.subn(r"\g<1>%s\g<2>" % DATE_ISO, s, count=1)
        assert n == 1, "blog index lastmod 未更新：%s" % loc
    blocks = []
    for a in ARTICLES:
        for pre, freq, pri in PREF:
            loc = "https://taigetag.com/%s%s" % (pre, a["slug"])
            assert ("<loc>%s</loc>" % loc) not in s, "sitemap 已有 %s" % loc
            blocks.append("  <url>\r\n    <loc>%s</loc>\r\n    <lastmod>%s</lastmod>\r\n"
                          "    <changefreq>%s</changefreq>\r\n    <priority>%s</priority>\r\n  </url>\r\n"
                          % (loc, DATE_ISO, freq, pri))
    s = s.replace("</urlset>", "".join(blocks) + "</urlset>", 1)
    with open(sp, "w", encoding="utf-8", newline="") as f:
        f.write(s)
    print("sitemap 新增 %d 条 URL" % len(blocks))


if __name__ == "__main__":
    build_articles()
