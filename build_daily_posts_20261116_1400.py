# -*- coding: utf-8 -*-
"""2026-11-16 14:00 每日 FAQ：2 篇（英文主稿 + zh/fr/es/ja/ko），生成主页 + blog/index.html 卡片。"""
import html
import os
import re

from body_20261116_1400_a import A1
from body_20261116_1400_b import A2

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
        slug="goh-vs-flat-pack-apparel-shipping-guide",
        body=A1,
        related=[
            ("hang-tag-moisture-curl-guide.html",
             dict(zh="吊牌受潮捲曲：成因與對策", en="Hang tag curl: causes and fixes",
                  fr="Étiquettes qui gondolent : causes et remèdes", es="Etiquetas que se curvan: causas y soluciones",
                  ja="タグの反り：原因と対策", ko="행택 휨: 원인과 대책")),
            ("garment-packaging-transit-testing.html",
             dict(zh="包裝運輸測試：項目與判定", en="Packaging transit testing: tests and pass criteria",
                  fr="Essais de transport : protocoles et critères", es="Ensayos de transporte: pruebas y criterios",
                  ja="包装の輸送試験：項目と合否基準", ko="포장 운송 시험: 항목과 합격 기준")),
            ("garment-hanger-types-guide.html",
             dict(zh="衣架種類與選型", en="Hanger types and selection",
                  fr="Types de cintres et choix", es="Tipos de perchas y elección",
                  ja="ハンガーの種類と選定", ko="행거 종류와 선택")),
        ],
        tag=dict(zh="包裝與出運", en="Packaging & Shipping", fr="Emballage et expédition",
                 es="Embalaje y envío", ja="包装と輸送", ko="포장·운송"),
        title=dict(
            zh="GOH 掛裝 vs 平裝：服裝出運與輔料保護 | TAGE",
            en="GOH vs Flat Pack: Apparel Shipping and Trim Protection | TAGE",
            fr="GOH ou à plat : expédition et protection des accessoires | TAGE",
            es="GOH o plano: envío de prendas y protección de fornituras | TAGE",
            ja="GOH と平積み：衣料輸送と副資材の保護 | TAGE",
            ko="GOH와 평포장: 의류 운송과 부자재 보호 | TAGE",
        ),
        desc=dict(
            zh="掛裝與平裝出運的取捨：貨櫃容積差 30–40%、掛衣帶與吊牌孔受力、紙吊牌受潮捲曲、以及訂櫃前的五項驗收寫法。",
            en="GOH and flat pack apparel shipping compared: container volume, hanger loop and poly bag specs, humidity control, tag visibility and five trim acceptance checks.",
            fr="GOH ou colisage à plat : volume conteneur, bande de suspension, sachet, humidité, visibilité de l'étiquette et cinq contrôles avant réservation.",
            es="GOH o envío plano: volumen del contenedor, cinta de colgado, bolsa, humedad, visibilidad de la etiqueta y cinco controles antes de reservar.",
            ja="GOH と平積みの比較。コンテナ容積の差 30〜40%、ハンガーループとタグ穴の負荷、紙タグの反り、予約前の五項目検収を整理します。",
            ko="GOH와 평포장 비교. 컨테이너 부피 차이 30~40%, 행거 루프와 행택 구멍의 하중, 종이 행택 휨, 예약 전 다섯 가지 검수를 정리합니다.",
        ),
        crumb=dict(zh="包裝與出運", en="Packaging & Shipping", fr="Emballage et expédition",
                   es="Embalaje y envío", ja="包装と輸送", ko="포장·운송"),
        h1=dict(
            zh="GOH 掛裝與平裝出運：哪種方式對輔料更安全",
            en="GOH vs Flat Pack Shipping: Which Protects Your Trims Better",
            fr="Expédition en GOH ou à plat : laquelle protège mieux vos accessoires",
            es="Envío en GOH o plano: cuál protege mejor las fornituras",
            ja="GOH と平積み、副資材に安全なのはどちらか",
            ko="GOH와 평포장, 부자재에 더 안전한 방식은",
        ),
        sum=dict(
            zh="同一個 40 呎高櫃，掛裝比平裝少裝 30–40% 的件數，但省掉目的地的整燙與掛衣。真正決定退貨率的不是運費，而是掛衣帶的針密與紙吊牌的受潮捲曲。",
            en="One 40 ft high-cube holds 30–40% fewer garments in GOH than flat packed, but skips pressing and re-hanging at the destination. Freight is not what drives returns; stitch density on the hanger loop and tag curl are.",
            fr="Un 40 pieds high-cube charge 30 à 40 % de vêtements en moins en GOH, mais évite le repassage et la remise sur cintre. Le taux de retour dépend surtout de la piqûre de la bande et du gondolement de l'étiquette.",
            es="Un 40 pies high-cube carga 30–40% menos prendas en GOH, pero se evita planchar y recolgar. Las devoluciones dependen de la puntada de la cinta y de la curvatura de la etiqueta, no del flete.",
            ja="同じ 40 フィートでも GOH は 30〜40% しか入りませんが、仕向地でのプレスと掛け直しが不要になります。返品率を決めるのは運賃ではなく、ループの縫い目密度と紙タグの反りです。",
            ko="같은 40피트 컨테이너에 GOH는 30~40% 적게 들어가지만 도착지에서 다림질과 재걸이를 생략할 수 있습니다. 반품률을 결정하는 것은 운임이 아니라 루프 박음질 밀도와 종이 행택의 휨입니다.",
        ),
    ),
    dict(
        slug="clothing-label-compliance-new-zealand",
        body=A2,
        related=[
            ("clothing-label-compliance-australia.html",
             dict(zh="澳洲服裝標籤合規", en="Australian clothing label compliance",
                  fr="Étiquetage des vêtements en Australie", es="Etiquetado de ropa en Australia",
                  ja="オーストラリアの衣料ラベル規制", ko="호주 의류 라벨 규제")),
            ("care-label-standards.html",
             dict(zh="洗水標標準：各國對照", en="Care label standards by country",
                  fr="Normes d'étiquetage d'entretien par pays", es="Normas de etiquetado de cuidado por país",
                  ja="洗濯表示ラベルの規格：国別対照", ko="세탁 라벨 규격: 국가별 비교")),
            ("clothing-label-compliance-uk.html",
             dict(zh="英國服裝標籤合規", en="UK clothing label compliance",
                  fr="Étiquetage des vêtements au Royaume-Uni", es="Etiquetado de ropa en el Reino Unido",
                  ja="英国の衣料ラベル規制", ko="영국 의류 라벨 규제")),
        ],
        tag=dict(zh="合規與標準", en="Compliance & Standards", fr="Conformité et normes",
                 es="Cumplimiento y normas", ja="法令と規格", ko="규제·규격"),
        title=dict(
            zh="紐西蘭服裝標籤要求：纖維、洗護與原產地 | TAGE",
            en="Clothing Label Requirements New Zealand: Fibre, Care, Origin | TAGE",
            fr="Étiquetage des vêtements en Nouvelle-Zélande | TAGE",
            es="Etiquetado de ropa en Nueva Zelanda: fibra, cuidado, origen | TAGE",
            ja="ニュージーランドの衣料ラベル表示要件 | TAGE",
            ko="뉴질랜드 의류 라벨 표시 요건: 혼용률·취급·원산지 | TAGE",
        ),
        desc=dict(
            zh="紐西蘭沒有單一服裝標籤法：義務分散在公平交易法、消費者保障法與 AS/NZS 1957；含成分、洗護符號、原產地與木質包裝檢疫要求。",
            en="New Zealand clothing label rules: the Fair Trading Act, Consumer Guarantees Act, AS/NZS 1957 care symbols, fibre content, origin claims and biosecurity.",
            fr="Règles d'étiquetage en Nouvelle-Zélande : Fair Trading Act, Consumer Guarantees Act, symboles AS/NZS 1957, composition, origine et biosécurité.",
            es="Reglas de etiquetado en Nueva Zelanda: Fair Trading Act, Consumer Guarantees Act, símbolos AS/NZS 1957, composición, origen y bioseguridad.",
            ja="NZ の衣料ラベル要件。公正取引法、消費者保証法、AS/NZS 1957 の取扱記号、組成、原産地、木質包装の検疫までを整理します。",
            ko="뉴질랜드 의류 라벨 요건. 공정거래법, 소비자보장법, AS/NZS 1957 취급 기호, 혼용률, 원산지, 목재 포장 검역까지 정리합니다.",
        ),
        crumb=dict(zh="合規與標準", en="Compliance & Standards", fr="Conformité et normes",
                   es="Cumplimiento y normas", ja="法令と規格", ko="규제·규격"),
        h1=dict(
            zh="紐西蘭服裝標籤要求：成分、洗護、原產地與包裝檢疫",
            en="Clothing Label Requirements in New Zealand: What Must Be on the Label",
            fr="Étiquetage des vêtements en Nouvelle-Zélande : ce qui doit figurer",
            es="Etiquetado de ropa en Nueva Zelanda: qué debe llevar la etiqueta",
            ja="ニュージーランドの衣料ラベル：表示すべき項目",
            ko="뉴질랜드 의류 라벨: 무엇을 표시해야 하는가",
        ),
        sum=dict(
            zh="紐西蘭沒有單一條文列出服裝標籤該寫什麼，義務分散在公平交易法、消費者保障法與 AS/NZS 1957，最後由零售商的供應商手冊把要求寫死。附歐盟、日本、韓國對照表。",
            en="No single New Zealand statute lists what a clothing label must say. Obligations sit across the Fair Trading Act, the Consumer Guarantees Act and AS/NZS 1957, with supplier manuals doing the final enforcement. Includes an EU, Japan and Korea comparison.",
            fr="Aucun texte unique n'énumère le contenu d'une étiquette. Les obligations se répartissent entre Fair Trading Act, Consumer Guarantees Act et AS/NZS 1957, les manuels fournisseurs tranchant en dernier. Avec un comparatif UE, Japon, Corée.",
            es="Ninguna norma única enumera el contenido de la etiqueta. Las obligaciones están en la Fair Trading Act, la Consumer Guarantees Act y la AS/NZS 1957, y los manuales de proveedores deciden al final. Incluye comparativa UE, Japón y Corea.",
            ja="表示内容を列挙した単一法はありません。義務は公正取引法・消費者保証法・AS/NZS 1957 に分かれ、最後は仕入先マニュアルが決めます。EU・日本・韓国との対照表付き。",
            ko="표시 내용을 열거한 단일 법은 없습니다. 의무는 공정거래법, 소비자보장법, AS/NZS 1957에 나뉘고 최종적으로 공급업체 매뉴얼이 결정합니다. EU·일본·한국 비교표 포함.",
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
    "goh-vs-flat-pack-apparel-shipping-guide": (
        dict(zh="要不要先做一次掛裝 vs 平裝的對照試裝？我們用一箱一軌、兩端拍照對比輔料狀態。",
             en="Want a side-by-side GOH and flat pack trial? We will pack one carton and one rail set and photograph the trims at both ends.",
             fr="Un essai comparatif GOH et à plat ? Nous préparons un carton et un jeu de tringles et photographions les accessoires aux deux bouts.",
             es="¿Un ensayo comparativo GOH y plano? Preparamos una caja y un juego de rieles y fotografiamos las fornituras en ambos extremos.",
             ja="GOH と平積みの比較試装はいかがですか。1 箱と 1 ラックを用意し、両端で副資材の状態を撮影します。",
             ko="GOH와 평포장 비교 시험을 해보시겠습니까? 카톤 한 개와 레일 한 세트로 양쪽에서 부자재 상태를 촬영해 비교합니다."),
        dict(zh="索取試裝方案與報價 →", en="Request a trial and a quote →", fr="Demander un essai et un devis →",
             es="Solicitar un ensayo y presupuesto →", ja="試装方案とお見積り →", ko="시험 포장과 견적 요청 →"),
    ),
    "clothing-label-compliance-new-zealand": (
        dict(zh="同一個貨櫃要發紐西蘭與歐盟？把目的地清單給我們，一張標籤過兩個市場。",
             en="One container going to New Zealand and the EU? Send us the destination list and we will build one label that passes both.",
             fr="Un conteneur pour la Nouvelle-Zélande et l'UE ? Envoyez la liste des destinations, nous concevons une étiquette conforme aux deux.",
             es="¿Un contenedor a Nueva Zelanda y la UE? Envíenos la lista de destinos y hacemos una etiqueta válida en ambos.",
             ja="同じコンテナを NZ と EU に？仕向地リストをお送りいただければ、両方に通るラベルを設計します。",
             ko="같은 컨테이너를 뉴질랜드와 EU로 보내시나요? 목적지 목록을 주시면 두 시장을 모두 통과하는 라벨을 설계합니다."),
        dict(zh="索取標籤方案與報價 →", en="Request a label plan and a quote →", fr="Demander un plan d'étiquetage et un devis →",
             es="Solicitar un plan de etiquetado y presupuesto →", ja="ラベル案とお見積り →", ko="라벨 설계와 견적 요청 →"),
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
