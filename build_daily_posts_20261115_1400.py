# -*- coding: utf-8 -*-
"""2026-11-15 14:00 每日 FAQ：2 篇（英文主稿 + zh/fr/es/ja/ko），生成中文主页 + blog/index.html 卡片。"""
import html
import os
import re

from body_20261115_1400_a import A1
from body_20261115_1400_b import A2

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
        slug="clothing-tagging-gun-swift-tack-guide",
        body=A1,
        related=[
            ("hang-tag-hole-punching-guide.html",
             dict(zh="吊牌打孔：孔徑與位置", en="Hang tag hole punching: diameter and position",
                  fr="Perçage du hangtag : diamètre et position", es="Perforado de la colgante: diámetro y posición",
                  ja="吊り下げタグの穴あけ：径と位置", ko="행택 천공: 구경과 위치")),
            ("garment-trims-needle-detection-guide.html",
             dict(zh="檢針作業：金屬異物管控", en="Needle detection: controlling metal contamination",
                  fr="Détection d'aiguilles : maîtriser la contamination métallique", es="Detección de agujas: controlar la contaminación metálica",
                  ja="検針：金属異物の管理", ko="검침: 금속 이물 관리")),
            ("care-label-attachment-guide.html",
             dict(zh="洗水標固定方式：車縫、熱壓與黏合", en="Care label attachment: sewn, bonded and heat set",
                  fr="Fixation de l'étiquette d'entretien : cousue, collée, thermosoudée", es="Fijación de la etiqueta de cuidado: cosida, adhesiva y termosellada",
                  ja="洗濯表示の取付：縫い付け・接着・熱圧着", ko="케어 라벨 부착: 봉제, 접착, 열압착")),
        ],
        tag=dict(zh="吊牌與懸掛", en="Hang Tag & Attachment", fr="Hangtag et fixation",
                 es="Colgante y sujeción", ja="タグと取付", ko="행택과 부착"),
        title=dict(
            zh="服裝吊牌槍與膠針：規格、面料安全與斷針管控 | TAGE",
            en="Clothing Tagging Gun and Swift Tacks: Sizes and Fabric Safety | TAGE",
            fr="Pistolet à étiquettes et attaches : formats et sécurité tissu | TAGE",
            es="Pistola etiquetadora y grapas: formatos y seguridad del tejido | TAGE",
            ja="タグガンとスイフトタック：仕様・生地適性・折れ針管理 | TAGE",
            ko="태깅 건과 스위프트택: 규격·원단 적합성·파손 관리 | TAGE",
        ),
        desc=dict(
            zh="吊牌槍與膠針指南：長度、針徑與針型怎麼配，哪五類面料不能打孔，斷針登記與檢針記錄怎麼做，以及歐美日韓對吊牌與隨件標示的要求。",
            en="Tagging gun and swift tack guide: pin lengths, needle gauges, five fabrics that should never be pierced, breakage control and hang tag rules by market.",
            fr="Pistolet à étiquettes et attaches : longueurs, diamètres, cinq tissus à ne jamais percer, contrôle des ruptures et obligations du hangtag par marché.",
            es="Guía de pistola etiquetadora y grapas: longitudes, calibres, cinco tejidos que no deben perforarse, control de roturas y requisitos por mercado.",
            ja="タグガンとスイフトタックの実務。ピンの長さ・針径・形状の選び方、穴を開けてはいけない五つの生地、折れ針管理と検針記録、市場別のタグ表示要件をまとめます。",
            ko="태깅 건과 스위프트택 실무. 핀 길이·바늘 굵기·형태 선택, 구멍을 내면 안 되는 다섯 가지 원단, 부러진 바늘 관리와 검침 기록, 시장별 행택 요건을 정리했습니다.",
        ),
        crumb=dict(zh="吊牌與懸掛", en="Hang Tag & Attachment", fr="Hangtag et fixation",
                   es="Colgante y sujeción", ja="タグと取付", ko="행택과 부착"),
        h1=dict(
            zh="服裝吊牌槍與膠針：規格、面料安全與斷針管控",
            en="Clothing Tagging Guns and Swift Tacks: Sizes, Fabric Safety and Breakage Control",
            fr="Pistolet à étiquettes et attaches : formats, sécurité tissu et contrôle des ruptures",
            es="Pistolas etiquetadoras y grapas: formatos, seguridad del tejido y control de roturas",
            ja="タグガンとスイフトタック：仕様・生地適性・折れ針管理",
            ko="태깅 건과 스위프트택: 규격, 원단 적합성, 바늘 파손 관리",
        ),
        sum=dict(
            zh="一支 25 mm 膠針就能決定吊牌會不會在運輸中掉落、真絲會不會留下永久針洞。長度、針徑與針型的搭配，五類不能打孔的面料，以及那張最便宜的保險：斷針登記表。",
            en="A 25 mm pin decides whether a tag falls off in transit and whether silk keeps a permanent hole. Length, gauge and pin type, five fabrics that should never be pierced, and the cheapest insurance there is: the breakage log.",
            fr="Une attache de 25 mm décide si le hangtag tombe en transport et si la soie garde un trou définitif. Longueur, diamètre, type, cinq tissus à ne jamais percer, et l'assurance la moins chère : le registre des casses.",
            es="Una grapa de 25 mm decide si la etiqueta cae en el transporte y si la seda conserva un agujero permanente. Longitud, calibre y tipo, cinco tejidos que no deben perforarse y el seguro más barato: el registro de roturas.",
            ja="25 mm のピン一つで、輸送中にタグが外れるか、シルクに永久の穴が残るかが決まります。長さ・針径・形状の組み合わせ、穴を開けてはいけない五つの生地、最も安い保険である折れ針記録をまとめました。",
            ko="25 mm 핀 하나가 운송 중 태그 낙하와 실크의 영구 구멍을 좌우합니다. 길이·바늘 굵기·형태 조합, 구멍을 내면 안 되는 다섯 원단, 가장 값싼 보험인 파손 기록을 정리했습니다.",
        ),
    ),
    dict(
        slug="garment-label-font-size-legibility-guide",
        body=A2,
        related=[
            ("care-label-printing-requirements.html",
             dict(zh="洗水標印刷要求：內容與符號", en="Care label printing requirements: content and symbols",
                  fr="Exigences d'impression des étiquettes d'entretien", es="Requisitos de impresión de etiquetas de cuidado",
                  ja="洗濯表示の印刷要件：内容と記号", ko="케어 라벨 인쇄 요건: 내용과 기호")),
            ("care-label-size-guide.html",
             dict(zh="洗水標尺寸：幾乘幾公分夠不夠", en="Care label size: how many centimetres is enough",
                  fr="Dimensions d'étiquette d'entretien : combien de centimètres", es="Tamaño de etiqueta de cuidado: cuántos centímetros",
                  ja="洗濯表示のサイズ：何 cm 必要か", ko="케어 라벨 크기: 몇 cm 가 필요한가")),
            ("care-label-symbols-chart.html",
             dict(zh="洗護符號對照表：五類符號怎麼讀", en="Care symbol chart: reading the five groups",
                  fr="Tableau des symboles d'entretien : lire les cinq groupes", es="Tabla de símbolos de cuidado: leer los cinco grupos",
                  ja="洗濯絵表示の一覧：五つの記号群の読み方", ko="취급 기호 도표: 다섯 기호군 읽기")),
        ],
        tag=dict(zh="標籤與可讀性", en="Labels & Legibility", fr="Étiquettes et lisibilité",
                 es="Etiquetas y legibilidad", ja="表示と判読性", ko="표시와 판독성"),
        title=dict(
            zh="服裝標籤字號與可讀性：最小字高、對比度與法定語言 | TAGE",
            en="Care Label Font Size and Legibility: Minimum Type Heights | TAGE",
            fr="Taille de police des étiquettes : hauteur minimale et lisibilité | TAGE",
            es="Tamaño de letra en etiquetas: altura mínima y legibilidad | TAGE",
            ja="洗濯表示の文字サイズ：最小字高と判読性 | TAGE",
            ko="케어 라벨 글자 크기: 최소 글자 높이와 판독성 | TAGE",
        ),
        desc=dict(
            zh="標籤字號與可讀性指南：六種工藝的最小字高與線寬、洗護符號的間距、法西語比英語長兩三成的寬度預算，以及法、西、日、韓的法定語言要求。",
            en="Care label font size and legibility: minimum type heights by process, care symbol spacing, a multilingual width budget and the legal language per market.",
            fr="Taille de caractère et lisibilité des étiquettes : hauteurs minimales par procédé, espacement des symboles, budget de largeur multilingue et langue légale par marché.",
            es="Tamaño de letra y legibilidad de etiquetas: alturas mínimas por proceso, espaciado de símbolos, presupuesto de ancho multilingüe e idioma legal por mercado.",
            ja="洗濯表示の文字サイズと判読性。工法別の最小字高と線幅、洗濯絵表示の間隔、フランス語・スペイン語が英語より 20〜35% 長い前提の幅計算、市場別の法定言語を整理します。",
            ko="케어 라벨 글자 크기와 판독성. 공법별 최소 글자 높이와 선 굵기, 취급 기호 간격, 프랑스어·스페인어가 영어보다 20~35% 긴 폭 계산, 시장별 법정 언어를 정리했습니다.",
        ),
        crumb=dict(zh="標籤與可讀性", en="Labels & Legibility", fr="Étiquettes et lisibilité",
                   es="Etiquetas y legibilidad", ja="表示と判読性", ko="표시와 판독성"),
        h1=dict(
            zh="服裝標籤字號：最小字高、對比度與法定語言",
            en="Care Label Font Size: Minimum Type Heights, Contrast and Legal Language",
            fr="Taille des caractères sur étiquette : hauteur minimale, contraste et langue légale",
            es="Tamaño de letra en etiquetas: altura mínima, contraste e idioma legal",
            ja="洗濯表示の文字サイズ：最小字高・コントラスト・法定言語",
            ko="케어 라벨 글자 크기: 최소 글자 높이, 대비, 법정 언어",
        ),
        sum=dict(
            zh="法規只寫「清晰可讀」，生產線上卻是三個數字：字高、線寬、對比度。同一個字換工藝差三倍，法語比英語多出一行，而這些都要在開稿前算完。",
            en="Regulation says only clearly legible; the line needs three numbers — type height, stroke width, contrast. The same word varies threefold by process, French needs one line more, and all of it should be settled before artwork sign-off.",
            fr="La réglementation dit seulement clairement lisible ; l'atelier a besoin de trois chiffres : hauteur, trait, contraste. Le même mot varie du simple au triple selon le procédé, le français réclame une ligne de plus, et tout cela se calcule avant validation.",
            es="La norma dice solo claramente legible; la línea necesita tres números: altura, trazo, contraste. La misma palabra varía al triple según el proceso, el francés pide una línea más, y todo eso se calcula antes de aprobar el arte.",
            ja="規制は「判読できること」しか書きませんが、現場には三つの数値が要ります。字高、線幅、コントラスト。同じ文字でも工法で三倍変わり、フランス語は一行増える。すべて原稿確定前に計算する話です。",
            ko="규정은 '판독 가능'만 말하지만 현장에는 세 수치가 필요합니다. 글자 높이, 선 굵기, 대비. 같은 글자도 공법에 따라 세 배 차이 나고 프랑스어는 한 줄이 더 필요하며, 이 모두를 아트워크 확정 전에 계산해야 합니다.",
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
    "clothing-tagging-gun-swift-tack-guide": (
        dict(zh="需要按面料分開建議膠針規格，或先寄一組樣品試針？",
             en="Need pin specs matched to your fabrics, or a sample set to test the gun?",
             fr="Besoin d'attaches adaptées à vos tissus, ou d'un jeu d'échantillons ?",
             es="¿Necesita grapas ajustadas a sus tejidos o un juego de muestras?",
             ja="生地に合わせたピン仕様や、試し打ち用サンプルが必要ですか。",
             ko="원단에 맞는 핀 사양이나 시험용 샘플이 필요하신가요?"),
        dict(zh="索取樣品與報價 →", en="Request samples and a quote →", fr="Demander échantillons et devis →",
             es="Solicitar muestras y presupuesto →", ja="試作とお見積りを依頼 →", ko="시료와 견적 요청 →"),
    ),
    "garment-label-font-size-legibility-guide": (
        dict(zh="想先看一版 1:1 打樣，確認最小字高讀不讀得出來？",
             en="Want a 1:1 sample first, to check whether the minimum type height actually reads?",
             fr="Envie d'un échantillon 1:1 pour vérifier la lisibilité de la hauteur minimale ?",
             es="¿Prefiere una muestra 1:1 para comprobar si la altura mínima se lee?",
             ja="最小字高が読めるか、1:1 のサンプルで先に確認しますか。",
             ko="최소 글자 높이가 읽히는지 1:1 샘플로 먼저 확인하시겠어요?"),
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


# ---------------- 简体字自检 ----------------
SIMP = "语标质图时这发对说产业务记号东南亚国际经营销务须应术许体简单导际专视规划标准标签织唛辅料报关价钱费运达设备厂检验记录纸设计图档"


def check_traditional(art):
    bad = []
    for lang, d in art.items():
        if not isinstance(d, dict):
            continue
        for k, v in d.items():
            for ch in v:
                if ch in SIMP:
                    bad.append((lang, k, ch))
    return bad


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
    bad = check_traditional(dict(title=t, desc=d, h1=h, crumb=c, tag=art["tag"], sum=art["sum"]))
    print("  简体字可疑：", bad if bad else "无")

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
