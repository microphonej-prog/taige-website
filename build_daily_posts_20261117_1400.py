# -*- coding: utf-8 -*-
"""2026-11-17 14:00 每日 FAQ：2 篇（英文主稿 + zh/fr/es/ja/ko），生成主页 + blog/index.html 卡片。"""
import html
import os
import re

from body_20261117_1400_a import A1
from body_20261117_1400_b import A2

SKEL = "blog/laser-engraved-hang-tags-guide.html"
OLD_SLUG = "laser-engraved-hang-tags-guide"
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
        slug="printed-fabric-label-guide",
        body=A1,
        related=[
            ("woven-vs-printed-labels.html",
             dict(zh="織嘜與印刷標的差別", en="Woven vs printed labels", fr="Tissé ou imprimé",
                  es="Tejido o impreso", ja="織りとプリントの違い", ko="직조와 프린트의 차이")),
            ("care-label-materials.html",
             dict(zh="洗水標材質怎麼選", en="Care label materials", fr="Matériaux d'étiquette d'entretien",
                  es="Materiales de etiqueta de cuidado", ja="洗濯表示ラベルの素材", ko="세탁 라벨 소재")),
            ("heat-transfer-labels.html",
             dict(zh="熱轉印標：牢度與應用", en="Heat transfer labels: durability and use", fr="Étiquettes par transfert thermique",
                  es="Etiquetas por transferencia térmica", ja="熱転写ラベル：堅牢度と用途", ko="열전사 라벨: 견뢰도와 용도")),
        ],
        tag=dict(zh="織嘜與吊牌", en="Labels & Hang Tags", fr="Étiquettes", es="Etiquetas", ja="ネーム・下げ札", ko="라벨·행택"),
        title=dict(
            zh="印刷布標：緞帶、塔夫綢、羅紋帶與棉帶怎麼選 | TAGE",
            en="Printed Fabric Labels: Satin, Taffeta, Grosgrain and Cotton | TAGE",
            fr="Étiquettes imprimées : satin, taffetas, gros-grain et coton | TAGE",
            es="Etiquetas impresas: satén, tafetán, grosgrain y algodón | TAGE",
            ja="プリント生地ラベル：サテン・タフタ・グログラン・コットン | TAGE",
            ko="프린트 원단 라벨: 새틴·태피터·그로스그레인·코튼 | TAGE",
        ),
        desc=dict(
            zh="印刷布標怎麼選：緞帶、塔夫綢、羅紋帶、棉帶的表面與常用寬度，網版／熱轉印／數位三種方式的分界，字高與線寬門檻，切邊摺法，以及歐盟、日本、韓國的必印內容。",
            en="Printed fabric labels compared: satin, taffeta, grosgrain and cotton tape, screen vs thermal transfer printing, edge finishing, fold options and wash tests.",
            fr="Étiquettes imprimées : satin, taffetas, gros-grain et coton, sérigraphie ou transfert thermique, finition des bords, plis et tenue au lavage.",
            es="Etiquetas impresas: satén, tafetán, grosgrain y algodón, serigrafía o transferencia térmica, acabado de bordes, dobleces y resistencia al lavado.",
            ja="プリント生地ラベルの選び方。サテン・タフタ・グログラン・コットンの幅と表現限界、スクリーン／熱転写／デジタルの分岐、文字高と線幅、断裁と折り、洗濯堅牢度と市場別の必須表示。",
            ko="프린트 원단 라벨 선택. 새틴·태피터·그로스그레인·코튼의 폭과 표현 한계, 스크린·열전사·디지털 분기, 글자 높이와 선 굵기, 재단과 접힘, 세탁 견뢰도와 시장별 필수 표시.",
        ),
        crumb=dict(zh="織嘜與吊牌", en="Labels & Hang Tags", fr="Étiquettes", es="Etiquetas", ja="ネーム・下げ札", ko="라벨·행택"),
        h1=dict(
            zh="印刷布標：四種布帶、三種印刷方式，怎麼選",
            en="Printed Fabric Labels: Which Tape, Which Printing Method",
            fr="Étiquettes imprimées : quel ruban, quel procédé",
            es="Etiquetas impresas: qué cinta, qué método",
            ja="プリント生地ラベル：テープと印刷方式の選び方",
            ko="프린트 원단 라벨: 테이프와 인쇄 방식 선택",
        ),
        sum=dict(
            zh="印刷布標在現成布帶上印，能出 1 mm 字與六色，但油墨在表面、要撐過洗滌。附四種布帶對照表、三種印刷方式的分界、字高與線寬門檻、切邊摺法與各市場必印內容。",
            en="A printed label can hold 1 mm type and six colours, but the ink sits on the surface and must survive washing. Includes a four-tape comparison, method thresholds, edge and fold rules, and per-market wording.",
            fr="Une étiquette imprimée accepte un texte de 1 mm et six couleurs, mais l'encre est en surface et doit tenir au lavage. Tableau des quatre rubans, seuils de procédé, bords, plis et mentions par marché.",
            es="Una etiqueta impresa admite texto de 1 mm y seis colores, pero la tinta está en la superficie y debe resistir el lavado. Incluye tabla de cuatro cintas, umbrales, bordes, dobleces y menciones por mercado.",
            ja="プリント生地ラベルは 1 mm の文字と 6 色を載せられますが、インクは表面にあり洗濯に耐える必要があります。4 テープ比較、方式の分岐、文字高、断裁と折り、市場別表示を掲載。",
            ko="프린트 원단 라벨은 1 mm 글자와 6색까지 담을 수 있지만 잉크가 표면에 있어 세탁을 견뎌야 합니다. 네 가지 테이프 비교, 방식 분기, 글자 높이, 재단·접힘, 시장별 표시를 담았습니다.",
        ),
    ),
    dict(
        slug="stock-vs-custom-garment-labels",
        body=A2,
        related=[
            ("care-label-materials.html",
             dict(zh="洗水標材質怎麼選", en="Care label materials", fr="Matériaux d'étiquette d'entretien",
                  es="Materiales de etiqueta de cuidado", ja="洗濯表示ラベルの素材", ko="세탁 라벨 소재")),
            ("woven-vs-printed-labels.html",
             dict(zh="織嘜與印刷標的差別", en="Woven vs printed labels", fr="Tissé ou imprimé",
                  es="Tejido o impreso", ja="織りとプリントの違い", ko="직조와 프린트의 차이")),
            ("garment-label-configuration-guide.html",
             dict(zh="一件衣服要幾個標", en="How many labels a garment needs", fr="Combien d'étiquettes par vêtement",
                  es="Cuántas etiquetas por prenda", ja="1 着に必要なラベル数", ko="의류 1장에 필요한 라벨 수")),
        ],
        tag=dict(zh="採購與成本", en="Sourcing & Cost", fr="Achats et coûts", es="Compras y coste", ja="調達・コスト", ko="구매·원가"),
        title=dict(
            zh="現貨標籤還是訂製標籤：成本、交期與混用時機 | TAGE",
            en="Stock vs Custom Garment Labels: Cost, Lead Time, When to Mix | TAGE",
            fr="Étiquettes de stock ou sur mesure : coût, délai, quand mixer | TAGE",
            es="Etiquetas de stock o a medida: coste, plazo y cuándo mezclar | TAGE",
            ja="既製ラベルか別注か：コスト・納期・併用の判断 | TAGE",
            ko="기성 라벨 vs 맞춤 라벨: 비용·납기·혼용 시점 | TAGE",
        ),
        desc=dict(
            zh="現貨標籤便宜快，但沒有品牌、成分固定、沒有市場語言。附四種失守情境、每件落地成本的損益平衡算法、情境對照表，以及空白帶加二次列印的混合路線。",
            en="Stock or custom garment labels? What off-the-shelf tape covers, where it breaks on care text and market rules, the break-even maths and the hybrid route.",
            fr="Stock ou sur mesure ? Ce qu'un rouleau couvre, où il cède sur l'entretien et les règles de marché, le calcul du point mort et la voie hybride.",
            es="¿Stock o a medida? Qué cubre un rollo, dónde falla en cuidado y normas de mercado, el cálculo del punto de equilibrio y la vía híbrida.",
            ja="既製か別注か。巻きテープで足りる範囲、洗濯表示や市場ルールで破綻する場面、損益分岐の計算、無地テープ＋追い刷りの併用案を整理します。",
            ko="기성인가 맞춤인가. 롤 테이프로 충분한 범위, 세탁 표시와 시장 규칙에서 무너지는 지점, 손익분기 계산, 무지 테이프 추가 인쇄 혼합안을 정리합니다.",
        ),
        crumb=dict(zh="採購與成本", en="Sourcing & Cost", fr="Achats et coûts", es="Compras y coste", ja="調達・コスト", ko="구매·원가"),
        h1=dict(
            zh="現貨標籤還是訂製標籤：哪些能買現成的，哪些不能",
            en="Stock or Custom Garment Labels: What You Can and Cannot Buy Off the Shelf",
            fr="Étiquettes de stock ou sur mesure : ce qui s'achète en rouleau",
            es="Etiquetas de stock o a medida: qué se puede comprar en rollo",
            ja="既製ラベルと別注ラベル：巻き売りで済む範囲",
            ko="기성 라벨과 맞춤 라벨: 롤 구매로 끝나는 범위",
        ),
        sum=dict(
            zh="現貨帶省的是版費與交期，代價是沒有品牌、成分固定、沒有市場語言。附四種失守情境、每件落地成本與損益平衡量算法、五種情境對照表，以及空白帶加熱轉印的混合路線。",
            en="Stock tape saves setup cost and lead time but carries no brand, a fixed composition and no market language. Four failure points, the landed-cost break-even, a scenario table and the blank-tape hybrid.",
            fr="Le rouleau économise calage et délai, mais n'a ni marque, ni composition juste, ni langue du marché. Quatre points de rupture, point mort, tableau de cas et voie hybride.",
            es="El rollo ahorra preparación y plazo, pero no tiene marca, ni composición correcta, ni idioma del mercado. Cuatro fallos, punto de equilibrio, tabla de casos y vía híbrida.",
            ja="巻きテープは版代と納期を節約しますが、ブランドも正しい組成も市場言語もありません。4 つの破綻点、着地コストの損益分岐、ケース表、無地テープ併用案を掲載。",
            ko="롤 테이프는 판 비용과 납기를 아끼지만 브랜드도, 정확한 조성도, 시장 언어도 없습니다. 네 가지 실패 지점, 착지 원가 손익분기, 사례표, 무지 테이프 혼합안을 담았습니다.",
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
    "printed-fabric-label-guide": (
        dict(zh="把圖稿與想用的布帶寄給我們，我們在兩種布帶上各印 15 mm 與 25 mm 校樣，附 10 倍放大掃描與實測字高。",
             en="Send the artwork and the tape you have in mind; we print 15 mm and 25 mm proofs on two substrates and return a 10× scan with the measured type height.",
             fr="Envoyez le fichier et le ruban envisagé : nous imprimons des épreuves en 15 mm et 25 mm sur deux supports et renvoyons un scan à 10× avec la hauteur de texte mesurée.",
             es="Envíe el arte y la cinta que tiene en mente: imprimimos pruebas de 15 mm y 25 mm sobre dos soportes y devolvemos un escaneo a 10× con la altura de texto medida.",
             ja="図案と希望テープをお送りください。2 種類のテープに 15 mm と 25 mm で校正印刷し、10 倍スキャンと実測文字高をお返しします。",
             ko="원고와 원하는 테이프를 보내주세요. 두 가지 테이프에 15 mm와 25 mm 교정 인쇄를 하고 10배 스캔과 실측 글자 높이를 회신합니다."),
        dict(zh="索取印刷布標校樣與報價 →", en="Request printed label proofs and a quote →", fr="Demander épreuves et devis →",
             es="Solicitar pruebas y presupuesto →", ja="校正見本とお見積り →", ko="교정 샘플과 견적 요청 →"),
    ),
    "stock-vs-custom-garment-labels": (
        dict(zh="把 BOM 與銷售市場給我們，我們回一份標籤配置表：哪些買現貨、哪些要訂製、每個市場要印什麼。",
             en="Send your BOM and the markets you sell into; we return a label configuration sheet showing what can be stock, what must be custom, and what each market needs printed.",
             fr="Envoyez la nomenclature et les marchés visés : nous renvoyons une fiche de configuration indiquant ce qui peut rester en stock, ce qui doit être sur mesure et ce que chaque marché exige.",
             es="Envíe el BOM y los mercados de venta: devolvemos una ficha de configuración con lo que puede ser stock, lo que debe ser a medida y lo que exige cada mercado.",
             ja="BOM と販売市場をお送りください。既製で足りる品目、別注が必要な品目、市場ごとの必須表示をまとめたラベル構成表をお返しします。",
             ko="BOM과 판매 시장을 보내주세요. 기성으로 가능한 품목, 맞춤이 필요한 품목, 시장별 필수 표시를 정리한 라벨 구성표를 회신합니다."),
        dict(zh="索取標籤配置表 →", en="Request a label configuration sheet →", fr="Demander la fiche de configuration →",
             es="Solicitar la ficha de configuración →", ja="ラベル構成表を依頼 →", ko="라벨 구성표 요청 →"),
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
