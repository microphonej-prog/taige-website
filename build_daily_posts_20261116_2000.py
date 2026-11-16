# -*- coding: utf-8 -*-
"""2026-11-16 20:00 每日 FAQ：2 篇（英文主稿 + zh/fr/es/ja/ko），生成主页 + blog/index.html 卡片。"""
import html
import os
import re

from body_20261116_2000_a import A1
from body_20261116_2000_b import A2

SKEL = "blog/snap-fastener-press-stud-guide.html"
OLD_SLUG = "snap-fastener-press-stud-guide"
DATE = "2026-11-16"
DATE_ZH = "2026年11月16日"
DATE_EN = "November 16, 2026"
DATE_FR = "16 novembre 2026"
DATE_ES = "16 de noviembre de 2026"
DATE_JA = "2026年11月16日"
DATE_KO = "2026년 11월 16일"

LANGS = ["zh", "en", "fr", "es", "ja", "ko"]

ARTICLES = [
    dict(
        slug="woven-label-qr-code-guide",
        body=A1,
        related=[
            ("hang-tag-qr-code-guide.html",
             dict(zh="吊牌 QR 碼：尺寸與印刷", en="QR codes on hang tags: size and printing",
                  fr="QR codes sur étiquettes volantes", es="Códigos QR en colgantes",
                  ja="下げ札の QR コード：サイズと印刷", ko="행택 QR 코드: 크기와 인쇄")),
            ("apparel-label-barcode-printing-guide.html",
             dict(zh="服裝標籤條碼印刷指南", en="Apparel label barcode printing",
                  fr="Impression de codes-barres sur étiquettes", es="Impresión de códigos de barras en etiquetas",
                  ja="衣料ラベルのバーコード印刷", ko="의류 라벨 바코드 인쇄")),
            ("woven-label-density-guide.html",
             dict(zh="織嘜密度：經緯紗與手感", en="Woven label density: ends, picks and hand feel",
                  fr="Densité d'une étiquette tissée", es="Densidad de etiqueta tejida",
                  ja="織りネームの密度：経糸・緯糸", ko="직조 라벨 밀도: 경사·위사")),
        ],
        tag=dict(zh="織嘜與吊牌", en="Labels & Hang Tags", fr="Étiquettes", es="Etiquetas", ja="ネーム・下げ札", ko="라벨·행택"),
        title=dict(
            zh="織嘜 QR 碼：提花能織出可掃的二維碼嗎 | TAGE",
            en="Woven QR Code Labels: Can Jacquard Weave a Scannable Code? | TAGE",
            fr="QR code tissé : un jacquard peut-il produire un code lisible ? | TAGE",
            es="Etiqueta tejida con QR: ¿puede un jacquard hacer un código legible? | TAGE",
            ja="織りネームの QR コード：ジャカードで読めるか | TAGE",
            ko="직조 QR 코드 라벨: 자카드로 판독 가능한 코드를 짤 수 있나 | TAGE",
        ),
        desc=dict(
            zh="織嘜 QR 碼的解析度天花板：每公分 25–40 根經紗、模組 0.4–0.6 mm、靜區 4 個模組、洗後掃描成功率與 ISO/IEC 15415 驗收寫法。",
            en="Woven QR code labels: module size limits at 25–40 ends per cm, contrast pairing, quiet zones, post-wash scan testing and ISO/IEC 15415 symbol grading.",
            fr="QR code tissé : limite de module à 25–40 fils/cm, contraste, zone de silence, test après lavage et notation ISO/IEC 15415.",
            es="Etiqueta tejida con QR: límite de módulo a 25–40 hilos/cm, contraste, zona de silencio, prueba tras lavado y clasificación ISO/IEC 15415.",
            ja="織りネームの QR コード。1 cm あたり 25〜40 本の経糸で決まるモジュール下限、配色、余白、洗濯後の読取試験と ISO/IEC 15415 の等級を整理します。",
            ko="직조 QR 코드 라벨. 1 cm당 경사 25~40올에서 결정되는 모듈 하한, 배색, 여백, 세탁 후 판독 시험과 ISO/IEC 15415 등급을 정리합니다.",
        ),
        crumb=dict(zh="織嘜與吊牌", en="Labels & Hang Tags", fr="Étiquettes", es="Etiquetas", ja="ネーム・下げ札", ko="라벨·행택"),
        h1=dict(
            zh="織嘜 QR 碼：提花織機到底能織出多細的二維碼",
            en="Woven QR Code Labels: What a Jacquard Loom Can Really Weave",
            fr="QR code tissé : ce qu'un métier jacquard peut réellement produire",
            es="Etiqueta tejida con QR: qué puede tejer de verdad un jacquard",
            ja="織りネームの QR コード：ジャカード織機が出せる限界",
            ko="직조 QR 코드 라벨: 자카드 직기가 실제로 낼 수 있는 한계",
        ),
        sum=dict(
            zh="織嘜是唯一跟著衣服走到回收的輔料，因此最適合放永久連結；但提花的解析度由經紗密度決定，模組低於 0.4 mm 就只剩灰塊。附模組換算表、四種常見失效、洗後驗收程序。",
            en="A woven label is the only trim that survives to recycling, which makes it the right home for a permanent link. But jacquard resolution is set by warp density, and below a 0.4 mm module you get a grey blur. Includes a module sizing table, four failure modes and a post-wash test.",
            fr="L'étiquette tissée est le seul accessoire qui survit jusqu'au recyclage : l'endroit idéal pour un lien permanent. Mais la résolution jacquard dépend de la densité de chaîne, et sous 0,4 mm le module devient une tache. Tableau de conversion, quatre défaillances et protocole après lavage.",
            es="La etiqueta tejida es el único accesorio que llega al reciclaje, el lugar idóneo para un enlace permanente. Pero la resolución jacquard la fija la densidad de urdimbre, y por debajo de 0,4 mm el módulo es una mancha. Incluye tabla, cuatro fallos y protocolo tras lavado.",
            ja="織りネームは再生素まで残る唯一の副資材で、恒久リンクを載せるのに最適です。ただしジャカードの解像度は経糸密度で決まり、モジュールが 0.4 mm を下回ると灰色の塊になります。換算表、四つの破綻、洗濯後の検証手順付き。",
            ko="직조 라벨은 재활용까지 남는 유일한 부자재라 영구 링크에 적합합니다. 다만 자카드 해상도는 경사 밀도가 정하고 모듈이 0.4 mm 이하이면 회색 덩어리가 됩니다. 환산표, 네 가지 실패, 세탁 후 검증 절차 포함.",
        ),
    ),
    dict(
        slug="eu-textiles-epr-brand-registration-guide",
        body=A2,
        related=[
            ("eu-packaging-epr-triman-guide.html",
             dict(zh="歐盟包裝 EPR：TrimMan 註冊", en="EU packaging EPR: TrimMan registration",
                  fr="REP emballages UE : enregistrement TrimMan", es="REP de envases UE: registro TrimMan",
                  ja="EU 包装 EPR：TrimMan 登録", ko="EU 포장 EPR: TrimMan 등록")),
            ("apparel-packaging-recyclability-guide.html",
             dict(zh="包裝可回收性設計", en="Packaging recyclability by design",
                  fr="Recyclabilité des emballages", es="Reciclabilidad de embalajes",
                  ja="包装のリサイクル設計", ko="포장 재활용 설계")),
            ("eu-digital-product-passport-trims.html",
             dict(zh="歐盟數位產品護照與輔料", en="EU digital product passport and trims",
                  fr="Passeport numérique européen et accessoires", es="Pasaporte digital europeo y fornituras",
                  ja="EU デジタル製品パスポートと副資材", ko="EU 디지털 제품 여권과 부자재")),
        ],
        tag=dict(zh="合規與標準", en="Compliance & Standards", fr="Conformité et normes",
                 es="Cumplimiento y normas", ja="法令と規格", ko="규제·규격"),
        title=dict(
            zh="歐盟紡織品 EPR：品牌註冊與輔料資料要求 | TAGE",
            en="EU Textile EPR: Brand Registration and Trim Data | TAGE",
            fr="REP textile UE : enregistrement et données accessoires | TAGE",
            es="REP textil UE: registro de marca y datos de fornituras | TAGE",
            ja="EU 繊維 EPR：ブランド登録と副資材データ | TAGE",
            ko="EU 섬유 EPR: 브랜드 등록과 부자재 데이터 | TAGE",
        ),
        desc=dict(
            zh="法國 Refashion 與荷蘭 UPV Textiel 的生產者註冊義務：誰是生產者、申報哪些件數與重量、輔料材質如何影響回收判定與費用，附五組必備資料清單。",
            en="Textile EPR in France and the Netherlands: who counts as producer, what units and weights to declare, and how trim materials change recyclability and fees.",
            fr="REP textile en France et aux Pays-Bas : qui est producteur, quelles unités et poids déclarer, et comment les matières changent recyclabilité et contribution.",
            es="REP textil en Francia y Países Bajos: quién es productor, qué unidades y pesos declarar, y cómo los materiales de fornituras cambian reciclabilidad y tasas.",
            ja="フランスとオランダの繊維 EPR。生産者の定義、申告する点数と重量、副資材の材質がリサイクル判定と負担金をどう変えるか、必要な五点のデータを整理します。",
            ko="프랑스와 네덜란드 섬유 EPR. 생산자 정의, 신고할 수량과 중량, 부자재 재질이 재활용 판정과 분담금을 어떻게 바꾸는지, 필요한 다섯 가지 데이터를 정리합니다.",
        ),
        crumb=dict(zh="合規與標準", en="Compliance & Standards", fr="Conformité et normes",
                   es="Cumplimiento y normas", ja="法令と規格", ko="규제·규격"),
        h1=dict(
            zh="歐盟紡織品 EPR：誰要註冊、輔料商要交出什麼資料",
            en="EU Textile EPR: Who Registers and What Your Trim Supplier Must Hand Over",
            fr="REP textile européenne : qui s'enregistre et ce que doit fournir le fournisseur d'accessoires",
            es="REP textil europea: quién se registra y qué debe aportar el proveedor de fornituras",
            ja="EU 繊維 EPR：誰が登録し、副資材サプライヤーは何を出すのか",
            ko="EU 섬유 EPR: 누가 등록하고 부자재 공급사는 무엇을 내야 하나",
        ),
        sum=dict(
            zh="註冊義務在「首次投放市場的品牌或進口商」，工廠沒有；但申報需要的每件材質與重量，只有輔料商拿得出來。含法國與荷蘭制度對照、五組必備資料、以及材質選錯如何讓整件衣服在分揀線被降級。",
            en="The registration duty sits with the brand or importer that first places the goods on the market, not the factory. But the per-item material and weight the declaration needs can only come from the trim supplier. Includes a France and Netherlands comparison and five data sets to collect.",
            fr="L'obligation incombe à la marque ou à l'importateur qui met le produit sur le marché, pas à l'usine. Or les matières et poids par article exigés ne peuvent venir que du fournisseur d'accessoires. Comparatif France/Pays-Bas et cinq jeux de données.",
            es="La obligación recae en la marca o importador que introduce el producto en el mercado, no en la fábrica. Pero los materiales y pesos por artículo solo puede darlos el proveedor de fornituras. Incluye comparativa Francia/Países Bajos y cinco datos.",
            ja="登録義務は市場に最初に投入するブランドまたは輸入者にあり、工場にはありません。ただし申告に必要な一点ごとの材質と重量は副資材サプライヤーしか出せません。フランスとオランダの対照、必要な五点のデータ、材質選択の影響を含みます。",
            ko="등록 의무는 시장에 최초로 출시하는 브랜드나 수입업자에게 있고 공장에는 없습니다. 다만 신고에 필요한 개당 재질과 중량은 부자재 공급사만 낼 수 있습니다. 프랑스·네덜란드 비교, 다섯 가지 데이터, 재질 선택의 영향을 담았습니다.",
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
    "woven-label-qr-code-guide": (
        dict(zh="要先把碼織出來測一輪嗎？把網址與標面尺寸給我們，我們回一份含模組尺寸的規格與洗後對照片。",
             en="Want to weave a test run first? Send us the URL and label dimensions and we will return a module-level spec with post-wash photos.",
             fr="Un essai de tissage d'abord ? Envoyez l'URL et les dimensions, nous renvoyons un cahier des charges au module près avec photos après lavage.",
             es="¿Quiere un tejido de prueba primero? Envíe la URL y las medidas y devolvemos una especificación al módulo con fotos tras lavado.",
             ja="まず試織で確認しませんか。URL とラベル寸法をお送りいただければ、モジュール単位の仕様と洗濯後の写真をお返しします。",
             ko="먼저 시험 직조로 확인하시겠습니까? URL과 라벨 치수를 보내주시면 모듈 단위 사양과 세탁 후 사진을 회신합니다."),
        dict(zh="索取織嘜 QR 規格與報價 →", en="Request a woven QR spec and quote →", fr="Demander un cahier des charges et un devis →",
             es="Solicitar especificación y presupuesto →", ja="織り QR の仕様とお見積り →", ko="직조 QR 사양과 견적 요청 →"),
    ),
    "eu-textiles-epr-brand-registration-guide": (
        dict(zh="正在備 EPR 申報？把輔料清單發來，我們按材質與克重給一份可直接填表的 BOM。",
             en="Preparing a textile EPR declaration? Send your trim list and we will return a material-and-weight BOM you can type straight into the form.",
             fr="Vous préparez une déclaration REP ? Envoyez la liste d'accessoires, nous renvoyons un BOM matière et poids utilisable tel quel.",
             es="¿Prepara una declaración REP? Envíe la lista de fornituras y devolvemos un BOM de material y peso listo para el formulario.",
             ja="EPR 申告の準備中ですか。副資材リストをお送りいただければ、そのまま記入できる材質・重量の BOM をお返しします。",
             ko="EPR 신고를 준비 중이신가요? 부자재 목록을 보내주시면 그대로 기입할 수 있는 재질·중량 BOM을 회신합니다."),
        dict(zh="索取 EPR 輔料 BOM 範本 →", en="Request the trim BOM template →", fr="Demander le modèle de BOM accessoires →",
             es="Solicitar la plantilla de BOM →", ja="副資材 BOM テンプレート →", ko="부자재 BOM 템플릿 요청 →"),
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
