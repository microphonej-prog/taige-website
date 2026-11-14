# -*- coding: utf-8 -*-
"""2026-11-14 08:00 每日 FAQ：2 篇（英文主稿 + zh/fr/es/ja/ko），生成中文主页 + blog/index.html 卡片。"""
import html
import os
import re

from body_20261114 import ART1, ART2

SKEL = "blog/euro-hole-retail-hang-packaging-guide.html"
OLD_SLUG = "euro-hole-retail-hang-packaging-guide"
DATE = "2026-11-14"
DATE_ZH = "2026年11月14日"
DATE_EN = "November 14, 2026"
DATE_FR = "14 novembre 2026"
DATE_ES = "14 de noviembre de 2026"
DATE_JA = "2026年11月14日"
DATE_KO = "2026년 11월 14일"

LANGS = ["zh", "en", "fr", "es", "ja", "ko"]

ARTICLES = [
    dict(
        slug="gs1-digital-link-2d-barcode-labels",
        body=ART1,
        related=[
            ("hang-tag-barcode-guide.html",
             dict(zh="吊牌條碼：位置、靜區與印刷公差", en="Hang tag barcodes: placement, quiet zone and print tolerance",
                  fr="Codes-barres sur hangtag : position, zone de silence et tolérance",
                  es="Códigos de barras en colgantes: posición, zona de silencio y tolerancia",
                  ja="下げ札のバーコード：位置・余白・印刷公差",
                  ko="행택 바코드: 위치, 여백, 인쇄 공차")),
            ("barcode-verification-grade-guide.html",
             dict(zh="條碼驗證等級：A 到 F 怎麼讀", en="Barcode verification grades: how to read A to F",
                  fr="Notes de vérification des codes-barres : lire de A à F",
                  es="Notas de verificación de códigos: cómo leer de A a F",
                  ja="バーコード検証等級：A〜F の読み方",
                  ko="바코드 검증 등급: A~F 읽는 법")),
            ("care-label-printing-requirements.html",
             dict(zh="洗水標印刷要求：解析度、碳帶與對比", en="Care label print requirements: resolution, ribbon and contrast",
                  fr="Exigences d'impression des étiquettes d'entretien : résolution, ruban, contraste",
                  es="Requisitos de impresión de etiquetas de cuidado: resolución, cinta y contraste",
                  ja="洗濯表示ラベルの印刷要件：解像度・リボン・コントラスト",
                  ko="케어 라벨 인쇄 요건: 해상도, 리본, 대비")),
        ],
        tag=dict(zh="條碼與追溯", en="Barcode & Traceability", fr="Codes-barres et traçabilité",
                 es="Códigos y trazabilidad", ja="バーコードとトレーサビリティ", ko="바코드와 추적성"),
        title=dict(
            zh="GS1 Digital Link：洗水標與吊牌的二維碼規格與驗碼 | TAGE",
            en="GS1 Digital Link: 2D Barcodes on Apparel Labels and Hang Tags | TAGE",
            fr="GS1 Digital Link : le code 2D sur les étiquettes et hangtags | TAGE",
            es="GS1 Digital Link: el código 2D en etiquetas y colgantes | TAGE",
            ja="GS1 Digital Link：洗濯表示と下げ札の2次元コード | TAGE",
            ko="GS1 Digital Link: 케어 라벨과 행택의 2차원 코드 | TAGE"),
        desc=dict(
            zh="洗水標與吊牌轉用 GS1 Digital Link 二維碼的實務指南：模組 0,4–0,5 mm 與靜區算法、四種承載方式的模組下限、ISO/IEC 15415 驗碼門檻，以及 2027 年前的試點清單。",
            en="Moving care labels and hang tags to GS1 Digital Link 2D codes: module and quiet zone numbers, print method limits, ISO/IEC 15415 grading, 2027 pilot steps.",
            fr="Passer les étiquettes et hangtags au code 2D GS1 Digital Link : modules de 0,4 à 0,5 mm, zone de silence, limites par support, vérification ISO/IEC 15415.",
            es="Pasar etiquetas y colgantes al código 2D GS1 Digital Link: módulos de 0,4 a 0,5 mm, zona de silencio, límites por soporte, verificación ISO/IEC 15415.",
            ja="洗濯表示ラベルと下げ札を GS1 Digital Link の2次元コードへ。モジュール 0.4〜0.5 mm、余白の設計、媒体ごとの限界、ISO/IEC 15415 検証、2027 年までの進め方。",
            ko="케어 라벨과 행택을 GS1 Digital Link 2차원 코드로 전환. 모듈 0.4~0.5 mm, 여백 설계, 매체별 한계, ISO/IEC 15415 검증, 2027년까지의 절차."),
        crumb=dict(zh="條碼與追溯", en="Barcode & Traceability", fr="Codes-barres et traçabilité",
                   es="Códigos y trazabilidad", ja="バーコードとトレーサビリティ", ko="바코드와 추적성"),
        h1=dict(
            zh="GS1 Digital Link：洗水標與吊牌的二維碼規格與驗碼",
            en="GS1 Digital Link: 2D Barcode Specs for Care Labels and Hang Tags",
            fr="GS1 Digital Link : spécifications du code 2D sur étiquettes et hangtags",
            es="GS1 Digital Link: especificaciones del código 2D en etiquetas y colgantes",
            ja="GS1 Digital Link：洗濯表示と下げ札における2次元コードの仕様と検証",
            ko="GS1 Digital Link: 케어 라벨과 행택의 2차원 코드 사양과 검증"),
        sum=dict(
            zh="從 13 位數字到一條鏈接：模組、靜區與標籤寬度怎麼算，四種承載方式的模組下限，ISO/IEC 15415 驗碼門檻，以及 2027 年前的試點清單。",
            en="From a 13-digit line to a link: module, quiet zone and label width, the minimum module per carrier, ISO/IEC 15415 grading, and a pilot checklist before 2027.",
            fr="D'un code à 13 chiffres à un lien : module, zone de silence et largeur, minimum par support, note ISO/IEC 15415 et liste de pilote avant 2027.",
            es="De un código de 13 dígitos a un enlace: módulo, zona de silencio y ancho, mínimo por soporte, nota ISO/IEC 15415 y lista de piloto antes de 2027.",
            ja="13桁からリンクへ。モジュール・余白・ラベル幅の計算、媒体ごとの最小モジュール、ISO/IEC 15415 の合格水準、2027 年までの確認項目。",
            ko="13자리에서 링크로. 모듈·여백·라벨 폭 계산, 매체별 최소 모듈, ISO/IEC 15415 합격 기준, 2027년 전 점검 항목."),
    ),
    dict(
        slug="certificate-of-origin-apparel-trims",
        body=ART2,
        related=[
            ("apparel-trims-hs-code-customs.html",
             dict(zh="輔料 HS 歸類與通關：常見爭議點", en="Trims HS classification and clearance: common disputes",
                  fr="Classement SH des accessoires et dédouanement : litiges courants",
                  es="Clasificación SA de accesorios y despacho: disputas habituales",
                  ja="副資材の HS 分類と通関：よくある争点",
                  ko="부자재 HS 분류와 통관: 흔한 쟁점")),
            ("clothing-origin-marking-guide.html",
             dict(zh="服裝原產地標示：Made in 怎麼寫才合規", en="Clothing origin marking: how 'Made in' stays compliant",
                  fr="Marquage d'origine des vêtements : un 'Made in' conforme",
                  es="Marcado de origen en prendas: un 'Made in' conforme",
                  ja="衣料の原産国表示：'Made in' を適正に保つ書き方",
                  ko="의류 원산지 표시: 'Made in'을 적법하게 쓰는 법")),
            ("trim-export-incoterms-guide.html",
             dict(zh="輔料出口 Incoterms：DDP 與 DAP 的責任分界", en="Trims export Incoterms: where DDP and DAP split responsibility",
                  fr="Incoterms à l'export d'accessoires : la frontière DDP / DAP",
                  es="Incoterms en exportación de accesorios: el límite DDP / DAP",
                  ja="副資材輸出の Incoterms：DDP と DAP の責任分界",
                  ko="부자재 수출 Incoterms: DDP와 DAP의 책임 경계")),
        ],
        tag=dict(zh="原產地與關稅", en="Origin & Duty", fr="Origine et douane",
                 es="Origen y arancel", ja="原産地と関税", ko="원산지와 관세"),
        title=dict(
            zh="服裝輔料的原產地證明：CO、FORM E 與 RCEP 關稅 | TAGE",
            en="Certificate of Origin for Garment Trims: CO, Form E, RCEP | TAGE",
            fr="Certificat d'origine des accessoires : CO, Form E, RCEP | TAGE",
            es="Certificado de origen de accesorios: CO, Form E y RCEP | TAGE",
            ja="副資材の原産地証明：CO・FORM E・RCEP の関税 | TAGE",
            ko="부자재 원산지증명: CO, FORM E, RCEP 관세 | TAGE"),
        desc=dict(
            zh="服裝輔料原產地證明指南：CO、FORM E、RCEP 與出口商自我聲明怎麼選、進口原料下的實質改變判定（CTH／40% 區域價值）、供應商該交的四份資料，以及退證的四個原因。",
            en="Certificate of origin for garment trims: CO, Form E, RCEP and self-declaration, substantial transformation on imported board, and four rejection causes.",
            fr="Certificat d'origine des accessoires : CO, Form E, RCEP, auto-déclaration REX, transformation substantielle (CTH, 40 %), pièces à exiger et motifs de rejet.",
            es="Certificado de origen de accesorios: CO, Form E, RCEP, autodeclaración REX, transformación sustancial (CTH, 40 %), documentos y motivos de rechazo.",
            ja="副資材の原産地証明。CO・FORM E・RCEP・自己申告の使い分け、輸入板紙での実質的変更（CTH・40 %）、提出書類、却下される四つの原因。",
            ko="부자재 원산지증명. CO, FORM E, RCEP, 자체 선언의 선택, 수입 판지의 실질적 변형(CTH·40%), 제출 서류, 반려되는 네 가지 이유."),
        crumb=dict(zh="原產地與關稅", en="Origin & Duty", fr="Origine et douane",
                   es="Origen y arancel", ja="原産地と関税", ko="원산지와 관세"),
        h1=dict(
            zh="服裝輔料的原產地證明：CO、FORM E 與 RCEP 的判定與文件",
            en="Certificate of Origin for Garment Trims: CO, Form E and RCEP Rules",
            fr="Certificat d'origine des accessoires : CO, Form E et règles RCEP",
            es="Certificado de origen de accesorios: CO, Form E y reglas RCEP",
            ja="副資材の原産地証明：CO・FORM E・RCEP の判定と書類",
            ko="부자재 원산지증명: CO, FORM E, RCEP 판정과 서류"),
        sum=dict(
            zh="三種稅率與五種文件：進口原料下的實質改變判定（CTH／40% 區域價值）、供應商該交的四份資料、原產地標示的獨立義務，以及退證的四個原因。",
            en="Three duty rates and five documents: substantial transformation on imported board (CTH or 40 % regional value), the four items a supplier must hand over, and four rejection causes.",
            fr="Trois taux et cinq documents : transformation substantielle du carton importé (CTH ou 40 % de valeur régionale), les quatre pièces à exiger, et quatre motifs de rejet.",
            es="Tres tipos y cinco documentos: transformación sustancial del cartón importado (CTH o 40 % de valor regional), las cuatro piezas a exigir y cuatro motivos de rechazo.",
            ja="三つの税率と五つの書類。輸入板紙での実質的変更（CTH または域内付加価値 40 %）、提出すべき四つの資料、却下される四つの原因。",
            ko="세 가지 세율과 다섯 가지 서류. 수입 판지의 실질적 변형(CTH 또는 역내 부가가치 40%), 제출할 네 가지 자료, 반려되는 네 가지 이유."),
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
                out.append("            <th %s>%s</th>" % (A(th), th["zh"]))
            out.append("          </tr>\n        </thead>\n        <tbody>")
            for row in rows:
                out.append("          <tr>")
                for td in row:
                    out.append("            <td %s>%s</td>" % (A(td), td["zh"]))
                out.append("          </tr>")
            out.append("        </tbody>\n      </table>")
            out.append("")
            continue
        payload = blk[1]
        if kind in ("p", "h2", "callout"):
            tag = "h2" if kind == "h2" else ("div" if kind == "callout" else "p")
            cls = ' class="callout"' if kind == "callout" else ""
            out.append('      <%s%s %s>%s</%s>' % (tag, cls, A(payload), payload["zh"], tag))
        elif kind in ("ul", "ol"):
            out.append("      <%s>" % kind)
            for it in payload:
                out.append("        <li %s>%s</li>" % (A(it), it["zh"]))
            out.append("      </%s>" % kind)
        elif kind == "table":
            head, rows = payload
            out.append("      <table>\n        <thead>\n          <tr>")
            for th in head:
                out.append("            <th %s>%s</th>" % (A(th), th["zh"]))
            out.append("          </tr>\n        </thead>\n        <tbody>")
            for row in rows:
                out.append("          <tr>")
                for td in row:
                    out.append("            <td %s>%s</td>" % (A(td), td["zh"]))
                out.append("          </tr>")
            out.append("        </tbody>\n      </table>")
        out.append("")
    return "\n".join(out)


def render_related(art):
    lines = ['      <h2 %s>%s</h2>' % (A(dict(zh="相關文章", en="Related Articles", fr="Articles connexes",
                                              es="Artículos relacionados", ja="関連記事", ko="관련 글")), "相關文章"),
             "", "      <ul>"]
    for href, d in art["related"]:
        lines.append('        <li><a href="%s" %s>%s</a></li>' % (href, A(d), d["zh"]))
    lines.append("      </ul>")
    return "\n".join(lines)


CTA = dict(zh="需要打樣、驗碼或原產地文件協助？", en="Need samples, barcode verification or origin paperwork?",
           fr="Besoin d'échantillons, de vérification de code ou de documents d'origine ?",
           es="¿Necesita muestras, verificación de códigos o documentos de origen?",
           ja="試作・コード検証・原産地書類のご相談は。",
           ko="시료, 코드 검증, 원산지 서류 지원이 필요하신가요?")
CTA_BTN = dict(zh="索取樣品與報價 →", en="Request samples and a quote →", fr="Demander échantillons et devis →",
               es="Solicitar muestras y presupuesto →", ja="試作とお見積りを依頼 →", ko="시료와 견적 요청 →")


def render_cta():
    return ('      <div class="cta-box">\n'
            '        <p %s>%s</p>\n'
            '        <a class="cta-btn" href="../contact.html" %s>%s</a>\n'
            '      </div>' % (A(CTA), CTA["zh"], A(CTA_BTN), CTA_BTN["zh"]))


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
    title_line = '<title %s>%s</title>' % (A(t), t["zh"])
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
             ' / <span %s>%s</span></div>' % (A(c), c["zh"]))
    s, n = re.subn(r'<div class="crumb">.*?</div>', lambda _: crumb, s, count=1, flags=re.S)
    assert n == 1, "crumb 替换失败"

    h = art["h1"]
    s, n = re.subn(r"<h1 .*?</h1>", lambda _: "<h1 %s>%s</h1>" % (A(h), h["zh"]), s, count=1, flags=re.S)
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
            + render_blocks(art["body"]) + "\n" + render_related(art) + "\n\n" + render_cta())
    body += "\n\n    </div>\n  </section>\n"

    i0 = s.index('  <section class="article-body">')
    i1 = s.index("\n</main>")
    s = s[:i0] + body + s[i1:]

    out = "blog/%s.html" % slug
    with open(out, "w", encoding="utf-8", newline="") as f:
        f.write(s)
    print("写入 %s  desc_en=%d 字符 desc_fr=%d desc_es=%d 大小=%d"
          % (out, len(d["en"]), len(d["fr"]), len(d["es"]), len(s.encode("utf-8"))))

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
