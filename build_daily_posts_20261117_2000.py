# -*- coding: utf-8 -*-
"""2026-11-17 20:00 每日 FAQ：2 篇（英文主稿 + zh/fr/es/ja/ko），生成主页 + blog/index.html 卡片。"""
import html
import os
import re

from body_20261117_2000_a import A1
from body_20261117_2000_b import A2

SKEL = "blog/hang-tag-barcode-guide.html"
OLD_SLUG = "hang-tag-barcode-guide"
DATE = "2026-11-17"
DATE_ZH = "2026年11月17日"
DATE_EN = "November 17, 2026"
DATE_FR = "17 novembre 2026"
DATE_ES = "17 de noviembre de 2026"
DATE_JA = "2026年11月17日"
DATE_KO = "2026년 11월 17일"

LANGS = ["zh", "en", "fr", "es", "ja", "ko"]

ARTICLES = [
    dict(
        slug="hang-tag-back-printing-guide",
        body=A1,
        related=[
            ("hang-tag-barcode-guide.html",
             dict(zh="吊牌條碼怎麼印才掃得到", en="Hang tag barcodes that scan", fr="Codes-barres d'étiquette qui scannent",
                  es="Códigos de barras que se leen", ja="読める下げ札バーコード", ko="읽히는 행택 바코드")),
            ("clothing-origin-marking-guide.html",
             dict(zh="原產國標示怎麼判", en="How country of origin is decided", fr="Comment l'origine est déterminée",
                  es="Cómo se determina el origen", ja="原産国の判定方法", ko="원산지 판정 방법")),
            ("care-label-standards.html",
             dict(zh="洗水標要符合哪些標準", en="Care label standards", fr="Normes des étiquettes d'entretien",
                  es="Normas de etiquetado de cuidado", ja="洗濯表示の基準", ko="세탁 표시 기준")),
        ],
        tag=dict(zh="織嘜與吊牌", en="Labels & Hang Tags", fr="Étiquettes", es="Etiquetas", ja="ネーム・下げ札", ko="라벨·행택"),
        title=dict(
            zh="吊牌背面印什麼：條碼、原產國與法定文字怎麼排 | TAGE",
            en="What to Print on the Back of a Hang Tag: Barcode, Origin, Legal Text | TAGE",
            fr="Quoi imprimer au dos d'une étiquette : code-barres, origine, mentions légales | TAGE",
            es="Qué imprimir en el reverso de una etiqueta colgante: código, origen y textos legales | TAGE",
            ja="下げ札の裏面に何を印刷するか：バーコード・原産国・法定表示 | TAGE",
            ko="행택 뒷면에 무엇을 인쇄할까: 바코드·원산지·법정 표시 | TAGE",
        ),
        desc=dict(
            zh="吊牌背面怎麼排：EAN 條碼留白 37.3 × 25.9 mm、法定文字 1.5 mm 字高、原產國與歐盟責任方，逐市場對照歐、法、西、日、韓、美的必印項目與紙張克重。",
            en="What goes on the back of a hang tag: EAN barcode and quiet zones, country of origin, EU responsible person, price and size fields, and the millimetre minimums.",
            fr="Ce qui figure au dos d'une étiquette : code-barres EAN et zones de silence, origine, responsable UE, zone de prix, avec les minima en millimètres.",
            es="Qué lleva el reverso de una etiqueta: código EAN y zonas de silencio, origen, responsable UE, zona de precio, con los mínimos en milímetros.",
            ja="下げ札の裏面設計。EAN バーコードの余白 37.3 × 25.9 mm、法定表示の文字高 1.5 mm、原産国と EU 責任事業者、市場別の必須項目と紙の坪量を整理します。",
            ko="행택 뒷면 설계. EAN 바코드 여백 37.3 × 25.9 mm, 법정 문구 글자 높이 1.5 mm, 원산지와 EU 책임자, 시장별 필수 항목과 종이 평량을 정리합니다.",
        ),
        crumb=dict(zh="織嘜與吊牌", en="Labels & Hang Tags", fr="Étiquettes", es="Etiquetas", ja="ネーム・下げ札", ko="라벨·행택"),
        h1=dict(
            zh="吊牌背面：條碼、原產國與法定文字怎麼排",
            en="What to Print on the Back of a Hang Tag",
            fr="Le dos d'une étiquette : ce qu'il faut y imprimer",
            es="El reverso de una etiqueta colgante: qué imprimir",
            ja="下げ札の裏面に印刷するもの",
            ko="행택 뒷면에 인쇄할 것",
        ),
        sum=dict(
            zh="吊牌背面才是條碼、價格欄、原產國與歐盟責任方真正裝得下的位置。附六個市場的必印對照表、五個元素的毫米最小值，以及背面滿版要付的三個工藝代價。",
            en="The back of a hang tag is where the barcode, price field, origin statement and EU responsible person actually fit. Includes a six-market table, millimetre minimums and three costs of a solid back.",
            fr="C'est au dos que tiennent le code-barres, la zone de prix, l'origine et le responsable UE. Tableau de six marchés, minima en millimètres et trois coûts d'un dos en aplat.",
            es="El reverso es donde caben el código de barras, la zona de precio, el origen y el responsable UE. Tabla de seis mercados, mínimos en milímetros y tres costes del pleno.",
            ja="バーコード・価格欄・原産国・EU 責任事業者が実際に収まるのは裏面です。6 市場の必須項目表、要素ごとのミリ最小値、ベタ刷りの 3 つのコストを掲載。",
            ko="바코드·가격란·원산지·EU 책임자가 실제로 들어가는 곳은 뒷면입니다. 6개 시장 필수 항목표, 요소별 밀리미터 최소값, 풀 커버리지의 세 가지 비용을 담았습니다.",
        ),
    ),
    dict(
        slug="apparel-trims-chargeback-guide",
        body=A2,
        related=[
            ("vendor-labeling-manual-compliance.html",
             dict(zh="品牌標示手冊怎麼落地", en="Vendor labelling manuals", fr="Manuels d'étiquetage fournisseur",
                  es="Manuales de etiquetado de proveedor", ja="ベンダー表示マニュアル対応", ko="벤더 표시 매뉴얼 대응")),
            ("apparel-trims-aql-inspection-guide.html",
             dict(zh="AQL 抽檢怎麼判", en="AQL inspection for trims", fr="Contrôle AQL des accessoires",
                  es="Inspección AQL de accesorios", ja="副資材の AQL 検査", ko="부자재 AQL 검사")),
            ("garment-trims-claims-liability-guide.html",
             dict(zh="索賠與責任怎麼劃分", en="Claims and liability", fr="Réclamations et responsabilité",
                  es="Reclamaciones y responsabilidad", ja="クレームと責任分担", ko="클레임과 책임 분담")),
        ],
        tag=dict(zh="採購與成本", en="Sourcing & Cost", fr="Achats et coûts", es="Compras y coste", ja="調達・コスト", ko="구매·원가"),
        title=dict(
            zh="輔料扣款：五個觸發點、金額怎麼算、出貨前該備什麼 | TAGE",
            en="Apparel Trim Chargebacks: Five Triggers and the Documents That Prevent Them | TAGE",
            fr="Débits sur accessoires : cinq déclencheurs et les documents qui les évitent | TAGE",
            es="Cargos por accesorios: cinco detonantes y los documentos que los evitan | TAGE",
            ja="副資材の請求減額：5 つの引き金と、それを防ぐ書類 | TAGE",
            ko="부자재 차감: 다섯 가지 유발 요인과 이를 막는 문서 | TAGE",
        ),
        desc=dict(
            zh="輔料扣款從哪來：標籤文字、AQL、交期、嘜頭、測試報告五個觸發點，品牌怎麼算金額，以及出貨前該備的六份文件與申訴的三個要件。",
            en="Where trim chargebacks come from: label wording, AQL failure, late delivery, carton marks and test reports, how the amount is built, and six documents to keep.",
            fr="D'où viennent les débits : mentions, AQL, retard, marquage, rapports d'essai, comment le montant se construit et les six documents à conserver.",
            es="De dónde vienen los cargos: textos, AQL, retraso, marcado, informes de ensayo, cómo se calcula el importe y los seis documentos a conservar.",
            ja="副資材の請求減額はどこから来るのか。表示・AQL・納期・外箱マーク・試験報告の 5 つの引き金、金額の算定、備えるべき 6 書類と異議申立ての 3 要件。",
            ko="부자재 차감은 어디서 오는가. 표시·AQL·납기·외箱 마킹·시험 성적서 다섯 요인, 금액 산정, 준비할 여섯 문서와 이의 제기 세 요건.",
        ),
        crumb=dict(zh="採購與成本", en="Sourcing & Cost", fr="Achats et coûts", es="Compras y coste", ja="調達・コスト", ko="구매·원가"),
        h1=dict(
            zh="輔料扣款：五個觸發點與出貨前的六份文件",
            en="Trim Chargebacks: Five Triggers and Six Documents",
            fr="Débits sur accessoires : cinq déclencheurs, six documents",
            es="Cargos por accesorios: cinco detonantes, seis documentos",
            ja="副資材の請求減額：5 つの引き金と 6 つの書類",
            ko="부자재 차감: 다섯 유발 요인과 여섯 문서",
        ),
        sum=dict(
            zh="扣款金額不是重點，時點才是：貨到港才來的扣款單，任何補救都按件計價。附五個觸發點對照表、金額算法、出貨前六份文件與申訴三要件。",
            en="The amount is not the problem, the timing is: a debit note that lands after the goods do prices every remedy per piece. Five triggers, the maths, six documents and three dispute rules.",
            fr="Le montant n'est pas le problème, le moment l'est : une note arrivée après la marchandise fait payer chaque remède à la pièce. Cinq déclencheurs, calcul, six documents, trois règles.",
            es="El importe no es el problema, el momento sí: una nota que llega tras la mercancía hace pagar cada remedio por pieza. Cinco detonantes, cálculo, seis documentos y tres reglas.",
            ja="問題は金額ではなく時機。入港後に届く減額は、あらゆる補修を枚数単価にします。5 つの引き金、算定方法、6 書類、異議申立ての 3 要件を掲載。",
            ko="문제는 금액이 아니라 시점입니다. 입항 후 도착하는 차감은 모든 보완을 개당 단가로 만듭니다. 다섯 요인, 산정 방식, 여섯 문서, 이의 제기 세 요건을 담았습니다.",
        ),
    ),
]


# ---------------- 渲染 ----------------
def A(d):
    return " ".join('data-%s="%s"' % (l, html.escape(d[l], quote=True)) for l in LANGS)


def render_blocks(blocks):
    out = []
    for blk in blocks:
        kind = blk[0]
        if kind == "table":
            head, rows = (blk[1], blk[2]) if len(blk) > 2 else blk[1]
            out.append("      <table>\n        <thead>\n          <tr>")
            for th in head:
                out.append("            <th %s>%s</th>" % (A(th), html.escape(th["zh"])))
            out.append("          </tr>\n        </thead>\n        <tbody>")
            for row in rows:
                out.append("          <tr>")
                for td in row:
                    out.append("            <td %s>%s</td>" % (A(td), html.escape(td["zh"])))
                out.append("          </tr>")
            out.append("        </tbody>\n      </table>")
            out.append("")
            continue
        payload = blk[1]
        if kind in ("p", "h2", "callout"):
            tag = "h2" if kind == "h2" else ("div" if kind == "callout" else "p")
            cls = ' class="callout"' if kind == "callout" else ""
            out.append('      <%s%s %s>%s</%s>' % (tag, cls, A(payload), html.escape(payload["zh"]), tag))
        elif kind in ("ul", "ol"):
            out.append("      <%s>" % kind)
            for it in payload:
                out.append("        <li %s>%s</li>" % (A(it), html.escape(it["zh"])))
            out.append("      </%s>" % kind)
        out.append("")
    return "\n".join(out)


def render_related(art):
    lines = ['      <h2 %s>%s</h2>' % (A(dict(zh="相關文章", en="Related Articles", fr="Articles connexes",
                                              es="Artículos relacionados", ja="関連記事", ko="관련 글")), "相關文章"),
             "", "      <ul>"]
    for href, d in art["related"]:
        lines.append('        <li><a href="%s" %s>%s</a></li>' % (href, A(d), html.escape(d["zh"])))
    lines.append("      </ul>")
    return "\n".join(lines)


CTAS = {
    "hang-tag-back-printing-guide": (
        dict(zh="把圖稿、銷售市場清單與預計數量寄給我們，我們回一份背面分區稿：法定文字、條碼留白、價格欄各自的位置與字高，附逐市場校對表。",
             en="Send the artwork, the list of selling markets and the quantity; we return a zoned back-side layout with the position and cap height of legal text, barcode quiet zone and price field, plus a per-market checklist.",
             fr="Envoyez le fichier, la liste des marchés et la quantité : nous renvoyons une maquette de dos en zones avec position et hauteur des mentions, zone de silence et zone de prix, plus une liste de contrôle par marché.",
             es="Envíe el arte, la lista de mercados y la cantidad: devolvemos una maqueta del reverso por zonas con posición y altura del texto legal, zona de silencio y zona de precio, más una lista de control por mercado.",
             ja="図案・販売市場の一覧・予定数量をお送りください。法定表示・バーコード余白・価格欄の位置と文字高を示した裏面割付と、市場別チェック表をお返しします。",
             ko="원고, 판매 시장 목록, 예상 수량을 보내주세요. 법정 문구·바코드 여백·가격란의 위치와 글자 높이를 표시한 뒷면 배치도와 시장별 점검표를 회신합니다."),
        dict(zh="索取吊牌背面排版與報價 →", en="Request a back-side layout and quote →", fr="Demander une maquette de dos et un devis →",
             es="Solicitar maqueta del reverso y presupuesto →", ja="裏面割付とお見積りを依頼 →", ko="뒷면 배치도와 견적 요청 →"),
    ),
    "apparel-trims-chargeback-guide": (
        dict(zh="把品牌的標示手冊與目標市場寄給我們，我們回一份「法定欄位 + 語言 + 測試項目」對照表，並在報價單上註明誰負責校對哪一項。",
             en="Send the brand's labelling manual and the target markets; we return a mapping of required fields, language and test items, and mark on the quote who proofreads what.",
             fr="Envoyez le manuel d'étiquetage de la marque et les marchés visés : nous renvoyons une correspondance champs obligatoires, langue et essais, en indiquant au devis qui relit quoi.",
             es="Envíe el manual de etiquetado de la marca y los mercados destino: devolvemos un mapeo de campos obligatorios, idioma y ensayos, señalando en la oferta quién revisa cada punto.",
             ja="ブランドの表示マニュアルと対象市場をお送りください。必須項目・言語・試験項目の対応表をお返しし、見積書に誰が何を校正するかを明記します。",
             ko="브랜드 표시 매뉴얼과 대상 시장을 보내주세요. 필수 항목·언어·시험 항목 대응표를 회신하고, 견적서에 누가 무엇을 교정하는지 명시합니다."),
        dict(zh="索取標示合規對照表 →", en="Request a labelling compliance mapping →", fr="Demander la correspondance de conformité →",
             es="Solicitar el mapeo de conformidad →", ja="表示コンプライアンス対応表を依頼 →", ko="표시 컴플라이언스 대응표 요청 →"),
    ),
}


def render_cta(art):
    cta, btn = CTAS[art["slug"]]
    return ('      <div class="cta-box">\n'
            '        <p %s>%s</p>\n'
            '        <a class="cta-btn" href="../contact.html" %s>%s</a>\n'
            '      </div>' % (A(cta), html.escape(cta["zh"]), A(btn), html.escape(btn["zh"])))


# ---------------- 主流程 ----------------
skel = open(SKEL, encoding="utf-8").read()
m = re.search(r'"position": 3,\s*\n?\s*"name": "([^"]*)"', skel) or re.search(r'"position": 3, "name": "([^"]*)"', skel)
assert m, "骨架 breadcrumb 未找到"
OLD_BREADCRUMB = m.group(1)

sm = open("sitemap.xml", encoding="utf-8").read()
for art in ARTICLES:
    for p in ["blog/%s.html" % art["slug"], "en/blog/%s.html" % art["slug"]]:
        if os.path.exists(p):
            raise SystemExit("选题撞车：%s 已存在" % p)
    if "/blog/%s.html</loc>" % art["slug"] in sm:
        raise SystemExit("选题撞车：sitemap 已含 %s" % art["slug"])
print("选题全新；骨架 breadcrumb =", OLD_BREADCRUMB)

for art in ARTICLES:
    slug = art["slug"]
    s = skel.replace(OLD_SLUG, slug)

    t = art["title"]
    title_line = '<title %s>%s</title>' % (A(t), html.escape(t["zh"]))
    s, n = re.subn(r"<title[^>]*>.*?</title>", lambda _: title_line, s, count=1, flags=re.S)
    assert n == 1, "title 替换失败"

    d = art["desc"]
    s = re.sub(r'<meta name="description".*?content="[^"]*">', "DESC_PLACEHOLDER", s, count=1, flags=re.S)
    desc_block = ('<meta name="description" %s\n      content="%s">'
                  % (A(d), html.escape(d["zh"], quote=True)))
    assert "DESC_PLACEHOLDER" in s, "description 占位失败"
    s = s.replace("DESC_PLACEHOLDER", desc_block, 1)

    c = art["crumb"]
    crumb = ('<div class="crumb"><a href="../index.html" data-zh="首頁" data-en="Home" data-fr="Accueil" '
             'data-es="Inicio" data-ja="ホーム" data-ko="홈">首頁</a>'
             ' / <a href="index.html" data-zh="輔料 FAQ" data-en="Trims FAQ" data-fr="FAQ Accessoires" '
             'data-es="FAQ Accesorios" data-ja="副資材 FAQ" data-ko="부자재 FAQ">輔料 FAQ</a>'
             ' / <span %s>%s</span></div>' % (A(c), html.escape(c["zh"])))
    s, n = re.subn(r'<div class="crumb">.*?</div>', lambda _: crumb, s, count=1, flags=re.S)
    assert n == 1, "crumb 替换失败"

    h = art["h1"]
    s, n = re.subn(r"<h1 .*?</h1>", lambda _: "<h1 %s>%s</h1>" % (A(h), html.escape(h["zh"])), s, count=1, flags=re.S)
    assert n == 1, "h1 替换失败"

    meta = ('<p data-zh="泰閣包裝 · 更新於 %s" data-en="By TAGE Packaging &nbsp;·&nbsp; Updated %s" '
            'data-fr="Par TAGE Packaging &nbsp;·&nbsp; Mis à jour le %s" '
            'data-es="Por TAGE Packaging &nbsp;·&nbsp; Actualizado el %s" '
            'data-ja="泰閣包装 · %s更新" data-ko="TAGE 패키징 · %s 업데이트">泰閣包裝 · 更新於 %s</p>'
            % (DATE_ZH, DATE_EN, DATE_FR, DATE_ES, DATE_JA, DATE_KO, DATE_ZH))
    s, n = re.subn(r'<p data-zh="[^"]*更新[^"]*"[^>]*>[^<]*</p>', lambda _: meta, s, count=1, flags=re.S)
    assert n == 1, "meta 行替换失败"

    s = s.replace('"%s"' % OLD_BREADCRUMB, '"%s"' % h["zh"])
    s, n = re.subn(r'"headline": "[^"]*"', lambda _: '"headline": "%s"' % h["zh"], s, count=1)
    assert n == 1, "headline 替换失败"

    body = ('  <section class="article-body">\n    <div class="container">\n\n'
            + render_blocks(art["body"]) + "\n" + render_related(art) + "\n\n" + render_cta(art))
    body += "\n\n    </div>\n  </section>\n"

    i0 = s.index('  <section class="article-body">')
    i1 = s.index("\n</main>")
    s = s[:i0] + body + s[i1:]

    out = "blog/%s.html" % slug
    with open(out, "w", encoding="utf-8", newline="") as f:
        f.write(s)
    print("写入 %s  desc_en=%d desc_fr=%d desc_es=%d desc_zh=%d 大小=%d"
          % (out, len(d["en"]), len(d["fr"]), len(d["es"]), len(d["zh"]), len(s.encode("utf-8"))))

# ---------- blog/index.html 卡片 ----------
CARD = '''      <article class="post-card">
        <span class="tag" data-zh="{tag_zh}" data-en="{tag_en}" data-fr="{tag_fr}" data-es="{tag_es}" data-ja="{tag_ja}" data-ko="{tag_ko}">{tag_zh}</span>
        <h3 data-zh="{zh}" data-en="{en}" data-fr="{fr}" data-es="{es}" data-ja="{ja}" data-ko="{ko}">{zh}</h3>
        <p data-zh="{sum_zh}" data-en="{sum_en}" data-fr="{sum_fr}" data-es="{sum_es}" data-ja="{sum_ja}" data-ko="{sum_ko}">{sum_zh}</p>
        <a class="more" href="{slug}.html" data-zh="閱讀全文 →" data-en="Read more →" data-fr="Lire la suite →" data-es="Leer más →" data-ja="続きを読む →" data-ko="자세히 보기 →">閱讀全文 →</a>
      </article>
'''
cards = ""
for art in ARTICLES:
    cards += CARD.format(
        tag_zh=art["tag"]["zh"], tag_en=art["tag"]["en"], tag_fr=art["tag"]["fr"],
        tag_es=art["tag"]["es"], tag_ja=art["tag"]["ja"], tag_ko=art["tag"]["ko"],
        zh=art["h1"]["zh"], en=art["h1"]["en"], fr=art["h1"]["fr"], es=art["h1"]["es"],
        ja=art["h1"]["ja"], ko=art["h1"]["ko"],
        sum_zh=html.escape(art["sum"]["zh"], quote=True), sum_en=html.escape(art["sum"]["en"], quote=True),
        sum_fr=html.escape(art["sum"]["fr"], quote=True), sum_es=html.escape(art["sum"]["es"], quote=True),
        sum_ja=html.escape(art["sum"]["ja"], quote=True), sum_ko=html.escape(art["sum"]["ko"], quote=True),
        slug=art["slug"])

idx = "blog/index.html"
s = open(idx, encoding="utf-8").read()
marker = '<div class="post-grid">\n'
assert marker in s, "post-grid 未找到"
for art in ARTICLES:
    assert art["slug"] not in s, "卡片已存在：%s" % art["slug"]
s = s.replace(marker, marker + "\n" + cards, 1)
with open(idx, "w", encoding="utf-8", newline="") as f:
    f.write(s)
print("blog/index.html 插入 %d 张卡片完成" % len(ARTICLES))
