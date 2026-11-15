# -*- coding: utf-8 -*-
"""2026-11-15 20:00 每日 FAQ：2 篇（英文主稿 + zh/fr/es/ja/ko），生成中文主页 + blog/index.html 卡片。"""
import html
import os
import re

from body_20261115_2000_a import A1
from body_20261115_2000_b import A2

SKEL = "blog/trim-dry-cleaning-fastness-guide.html"
OLD_SLUG = "trim-dry-cleaning-fastness-guide"
DATE = "2026-11-15"
DATE_ZH = "2026年11月15日"
DATE_EN = "November 15, 2026"
DATE_FR = "15 novembre 2026"
DATE_ES = "15 de noviembre de 2026"
DATE_JA = "2026年11月15日"
DATE_KO = "2026년 11월 15일"

LANGS = ["zh", "en", "fr", "es", "ja", "ko"]

ARTICLES = [
    dict(
        slug="fringe-tassel-pom-pom-trims-guide",
        body=A1,
        related=[
            ("ribbon-trims-guide.html",
             dict(zh="緞帶飾邊：寬度、材質與用途", en="Ribbon trims: widths, fibres and uses",
                  fr="Galons et rubans : largeurs, fibres et usages", es="Cintas y galones: anchos, fibras y usos",
                  ja="リボン飾り：幅・素材・用途", ko="리본 트림: 폭, 소재, 용도")),
            ("lace-trimming-guide.html",
             dict(zh="蕾絲飾邊：種類與選型", en="Lace trimming: types and selection",
                  fr="Dentelle : types et sélection", es="Encaje: tipos y selección",
                  ja="レース飾り：種類と選び方", ko="레이스 트림: 종류와 선택")),
            ("trim-attachment-strength-pull-test-guide.html",
             dict(zh="輔料附著力：拉力測試怎麼做", en="Trim attachment: how to run the pull test",
                  fr="Fixation des accessoires : réaliser l'essai de traction", es="Fijación de accesorios: cómo hacer el ensayo de tracción",
                  ja="副資材の取付強度：引張試験の進め方", ko="부자재 부착 강도: 인장 시험 진행 방법")),
        ],
        tag=dict(zh="飾邊與工藝", en="Trims & Craft", fr="Garnitures et façonnage",
                 es="Remates y confección", ja="飾りと加工", ko="장식과 공정"),
        title=dict(
            zh="流蘇、絨球與毛邊飾條：結構、固定與耐洗 | TAGE",
            en="Fringe, Tassel & Pom-Pom Trims: Structure and Care | TAGE",
            fr="Franges, pompons et glands : structure et entretien | TAGE",
            es="Flecos, pompones y borlas: estructura y cuidado | TAGE",
            ja="フリンジ・タッセル・ポンポン：構造と洗濯耐久性 | TAGE",
            ko="프린지·태슬·폼폼 트림: 구조와 세탁 내구성 | TAGE",
        ),
        desc=dict(
            zh="流蘇、絨球與毛邊飾條全指南：剪絨與環絨的差別、材質取捨、四種固定方式的拉力比較、洗後纏結與掉絨的驗收標準，以及兒童服的細小零件與燃燒性判定。",
            en="Fringe, tassel and pom-pom trims: cut versus loop construction, fibre choice, four attachment methods, wash durability and the small-parts limits for kidswear.",
            fr="Franges, pompons et glands : frange coupée ou bouclée, choix de fibre, quatre modes de fixation, tenue au lavage et limites petites pièces pour l'enfant.",
            es="Flecos, pompones y borlas: fleco cortado o en bucle, elección de fibra, cuatro modos de fijación, resistencia al lavado y límites de piezas pequeñas.",
            ja="フリンジ・タッセル・ポンポンの実務。カットとループの違い、素材選び、四つの取付方法、洗濯後の絡みと抜け毛の検収基準、子ども服の小部品と燃焼性の判定をまとめます。",
            ko="프린지·태슬·폼폼 트림 실무. 컷과 루프 구조 차이, 소재 선택, 네 가지 부착 방식, 세탁 후 엉킴과 섬유 탈락 검수 기준, 아동복 소부품과 연소성 판정을 정리했습니다.",
        ),
        crumb=dict(zh="飾邊與工藝", en="Trims & Craft", fr="Garnitures et façonnage",
                   es="Remates y confección", ja="飾りと加工", ko="장식과 공정"),
        h1=dict(
            zh="流蘇、絨球與毛邊飾條：結構、固定方式與耐洗",
            en="Fringe, Tassel and Pom-Pom Trims: Structure, Attachment and Wash Care",
            fr="Franges, pompons et glands : structure, fixation et tenue au lavage",
            es="Flecos, pompones y borlas: estructura, fijación y cuidado en lavado",
            ja="フリンジ・タッセル・ポンポン：構造・取付方法・洗濯耐久性",
            ko="프린지·태슬·폼폼 트림: 구조, 부착 방식, 세탁 내구성",
        ),
        sum=dict(
            zh="一條 5 cm 寬的毛邊，剪絨與環絨的成本能差四成；而它掉不掉，八成不在材質，在一次洗滌後的樣子。結構、固定、耐洗與兒童安全，四件事在開單前就該定好。",
            en="A 5 cm fringe tape differs forty percent in cost between cut and loop, and whether it stays on is eighty percent about attachment, not fibre. Structure, fixing, wash and child safety are settled before the order, not after.",
            fr="Un galon de 5 cm varie de quarante pour cent entre coupé et bouclé, et sa tenue tient à quatre-vingts pour cent à la fixation. Structure, fixation, lavage et sécurité enfant se décident avant la commande.",
            es="Un fleco de 5 cm varía un cuarenta por ciento entre cortado y en bucle, y su aguante depende un ochenta por ciento de la fijación. Estructura, fijación, lavado y seguridad infantil se deciden antes de pedir.",
            ja="幅 5 cm のフリンジはカットとループでコストが四割変わり、外れるかどうかは八割が取付方法で決まります。構造・固定・洗濯・子ども安全は発注前に決める四項目です。",
            ko="폭 5 cm 프린지는 컷과 루프에서 원가가 40% 차이 나고, 떨어지는지는 80%가 부착 방식에서 결정됩니다. 구조, 고정, 세탁, 아동 안전은 발주 전에 정할 네 가지입니다.",
        ),
    ),
    dict(
        slug="cord-locks-toggles-drawstring-hardware-guide",
        body=A2,
        related=[
            ("garment-drawcord-guide.html",
             dict(zh="抽繩：材質、規格與穿法", en="Drawcords: materials, specs and threading",
                  fr="Cordons de serrage : matières, spécifications et enfilage", es="Cordones: materiales, especificaciones e hilado",
                  ja="ドローコード：素材・仕様・通し方", ko="드로코드: 소재, 규격, 삽입 방법")),
            ("metal-trims-nickel-release-guide.html",
             dict(zh="金屬輔料鎳釋放：限值與對策", en="Nickel release from metal trims: limits and fixes",
                  fr="Libération de nickel des accessoires métalliques : limites", es="Liberación de níquel en accesorios metálicos: límites",
                  ja="金属副資材のニッケル溶出：規制値と対策", ko="금속 부자재 니켈 용출: 규제치와 대응")),
            ("eyelet-grommet-rivet-guide.html",
             dict(zh="雞眼、氣眼與鉚釘：規格與固定", en="Eyelets, grommets and rivets: sizes and setting",
                  fr="Œillets et rivets : dimensions et pose", es="Ojales y remaches: medidas y colocación",
                  ja="ハトメ・グロメット・リベット：寸法と固定", ko="아일릿, 그로밋, 리벳: 규격과 고정")),
        ],
        tag=dict(zh="五金與輔料", en="Hardware & Trims", fr="Quincaillerie et accessoires",
                 es="Herrajes y accesorios", ja="金具と副資材", ko="금속 부자재"),
        title=dict(
            zh="繩扣、豬鼻扣與抽繩五金：繩徑搭配與兒童安全 | TAGE",
            en="Cord Locks, Toggles and Drawstring Hardware: Sizing | TAGE",
            fr="Bloqueurs, toggles et cordons : dimensionnement | TAGE",
            es="Bloqueadores, toggles y cordones: guía de medidas | TAGE",
            ja="コードロック・トグル・コードエンド：径の合わせ方 | TAGE",
            ko="코드락·토글·드로스트링 하드웨어: 직경 선택 가이드 | TAGE",
        ),
        desc=dict(
            zh="抽繩五金選型指南：繩扣、豬鼻扣、繩尾與雞眼的搭配尺寸，POM 與尼龍的低溫差異，EN 14682 與 16 CFR 1120 的繩帶限制，鎳釋放測試與驗收判據。",
            en="Cord locks, toggles and cord ends: matching cord diameter, shell materials, EN 14682 and 16 CFR 1120 drawstring limits, nickel release and inspection criteria.",
            fr="Bloqueurs, toggles et embouts : correspondance des diamètres, matières de coque, limites EN 14682 et 16 CFR 1120, nickel et critères de contrôle.",
            es="Bloqueadores, toggles y terminales: diámetros, materiales de carcasa, límites EN 14682 y 16 CFR 1120, níquel y criterios de inspección.",
            ja="コードロック・トグル・コードエンドの選定。対応コード径、外殻材質の低温特性、EN 14682 と 16 CFR 1120 の紐規制、ニッケル溶出と検収基準をまとめます。",
            ko="코드락·토글·코드 엔드 선택. 대응 코드 직경, 외피 소재의 저온 특성, EN 14682와 16 CFR 1120 끈 규정, 니켈 용출과 검수 기준을 정리했습니다.",
        ),
        crumb=dict(zh="五金與輔料", en="Hardware & Trims", fr="Quincaillerie et accessoires",
                   es="Herrajes y accesorios", ja="金具と副資材", ko="금속 부자재"),
        h1=dict(
            zh="繩扣、豬鼻扣與抽繩五金：繩徑、兒童安全與驗收",
            en="Cord Locks, Toggles and Drawstring Hardware: Diameter, Safety and Inspection",
            fr="Bloqueurs, toggles et cordons : diamètre, sécurité et contrôle",
            es="Bloqueadores, toggles y cordones: diámetro, seguridad e inspección",
            ja="コードロック・トグル・コードエンド：径・子ども安全・検収",
            ko="코드락·토글·드로스트링 하드웨어: 직경, 아동 안전, 검수",
        ),
        sum=dict(
            zh="抽繩五金佔整件成本不到 1%，卻是客訴最多、事後最難補救的一環。繩徑公差 0.2 mm、腰部外露 14 cm、鎳釋放與 3,000 次按壓，四個數字定生死。",
            en="Drawstring hardware is under one percent of garment cost and produces most of the complaints. A 0.2 mm diameter tolerance, 14 cm of exposed waist cord, nickel release and 3,000 presses: four numbers decide it.",
            fr="Moins de 1 % du coût du vêtement, mais le plus de réclamations. Tolérance de 0,2 mm sur le diamètre, 14 cm de cordon exposé, nickel et 3 000 pressions : quatre chiffres décident.",
            es="Menos del 1% del coste de la prenda y la mayoría de las reclamaciones. Tolerancia de 0,2 mm, 14 cm de cordón expuesto, níquel y 3.000 pulsaciones: cuatro cifras deciden.",
            ja="製品原価の 1% 未満でありながら、苦情が最も多い部分です。径公差 0.2 mm、ウエスト外露 14 cm、ニッケル溶出、3,000 回押圧。四つの数字で決まります。",
            ko="의류 원가의 1% 미만이지만 클레임이 가장 많은 부분입니다. 직경 공차 0.2 mm, 허리 노출 14 cm, 니켈 용출, 3,000회 누름. 네 숫자가 결정합니다.",
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
            head, rows = blk[1], blk[2]
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
    "fringe-tassel-pom-pom-trims-guide": (
        dict(zh="想先看剪絨與環絨的實物對比，再決定用哪一種？",
             en="Want the cut and loop samples side by side before you choose?",
             fr="Envie de comparer frange coupée et bouclée sur échantillons avant de choisir ?",
             es="¿Quiere comparar fleco cortado y en bucle en muestra antes de elegir?",
             ja="カットとループの実物を並べて比べてから決めますか。",
             ko="컷과 루프 실물을 나란히 비교한 뒤 결정하시겠어요?"),
        dict(zh="索取樣品與報價 →", en="Request samples and a quote →", fr="Demander échantillons et devis →",
             es="Solicitar muestras y presupuesto →", ja="試作とお見積りを依頼 →", ko="시료와 견적 요청 →"),
    ),
    "cord-locks-toggles-drawstring-hardware-guide": (
        dict(zh="把手上的繩子寄一段過來，我們按實際繩徑配對繩扣？",
             en="Send a length of your cord and we will match the lock to the real diameter?",
             fr="Envoyez un échantillon de cordon, nous assortirons le bloqueur au diamètre réel ?",
             es="¿Envía un tramo de cordón y ajustamos el bloqueador al diámetro real?",
             ja="お手持ちのコードを少しお送りいただければ、実径に合わせてロックを選定します。",
             ko="보유하신 코드를 조금 보내주시면 실제 직경에 맞춰 락을 선정하겠습니다."),
        dict(zh="索取樣品與報價 →", en="Request samples and a quote →", fr="Demander échantillons et devis →",
             es="Solicitar muestras y presupuesto →", ja="試作とお見積りを依頼 →", ko="시료와 견적 요청 →"),
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

    # JSON-LD
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
        sum_zh=art["sum"]["zh"], sum_en=art["sum"]["en"], sum_fr=art["sum"]["fr"],
        sum_es=art["sum"]["es"], sum_ja=art["sum"]["ja"], sum_ko=art["sum"]["ko"],
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
