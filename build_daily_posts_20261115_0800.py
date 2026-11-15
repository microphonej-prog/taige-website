# -*- coding: utf-8 -*-
"""2026-11-15 08:00 每日 FAQ：2 篇（英文主稿 + zh/fr/es/ja/ko），生成中文主页 + blog/index.html 卡片。"""
import html
import os
import re

from body_20261115_a import A1
from body_20261115_b import A2

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
        slug="woven-label-loom-types-guide",
        body=A1,
        related=[
            ("woven-label-density-guide.html",
             dict(zh="織嘜密度：每公分根數怎麼定", en="Woven label density: threads per cm",
                  fr="Densité du label tissé : fils par cm", es="Densidad de etiqueta tejida: hilos por cm",
                  ja="織りラベルの密度：1 cm あたりの本数", ko="직조 라벨 밀도: 1 cm 당 올 수")),
            ("woven-label-width-guide.html",
             dict(zh="織嘜寬度：10–50 mm 怎麼選", en="Woven label width: choosing 10–50 mm",
                  fr="Largeur du label tissé : choisir 10–50 mm", es="Ancho de etiqueta: elegir 10–50 mm",
                  ja="織りラベルの幅：10〜50 mm の選び方", ko="직조 라벨 폭: 10~50 mm 선택")),
            ("woven-label-artwork-guide.html",
             dict(zh="織嘜圖稿：線寬與字高的下限", en="Woven label artwork: line width and type height",
                  fr="Maquette de label tissé : trait et hauteur de texte", es="Arte de etiqueta tejida: trazo y altura",
                  ja="織りラベルの原稿：線幅と字高の下限", ko="직조 라벨 원고: 선폭과 글자 높이")),
        ],
        tag=dict(zh="織嘜工藝", en="Woven Label Craft", fr="Fabrication des labels",
                 es="Fabricación de etiquetas", ja="織りラベルの製造", ko="직조 라벨 제작"),
        title=dict(
            zh="織嘜織機怎麼選：針織機與梭織機的細節、成本與起訂量 | TAGE",
            en="Woven Label Looms: Needle Loom vs Shuttle Loom | TAGE",
            fr="Métiers à tisser pour labels : aiguilles ou navette | TAGE",
            es="Telares para etiquetas tejidas: agujas o lanzadera | TAGE",
            ja="織りラベルの織機選び：ニードルとシャトルの違い | TAGE",
            ko="직조 라벨 직기 선택: 니들룸과 셔틀룸의 차이 | TAGE",
        ),
        desc=dict(
            zh="織嘜織機選型指南：針織機與梭織機在最小線寬、織邊、起訂量與單價上的差異，20 × 50 mm 布面怎麼算法規字數，以及打樣前必須定下來的五件事。",
            en="Needle loom or shuttle loom sets woven label detail, minimum line width and MOQ. See how each loom type changes cost, selvage, lead time and legal text space.",
            fr="Métier à aiguilles ou à navette : ce qui change sur la largeur de trait, la lisière, la quantité minimale et le prix. Comment compter les mentions légales sur 20 × 50 mm, et les cinq points à figer avant l'échantillon.",
            es="Telar de agujas o de lanzadera cambia el ancho de línea mínimo, el orillo, el pedido mínimo y el precio. Cómo contar el texto legal en 20 × 50 mm y los cinco puntos a fijar antes de la muestra.",
            ja="ニードル織機とシャトル織機で、最小線幅・耳・MOQ・単価はどう変わるか。20 × 50 mm に収まる法定表示の字数の数え方と、サンプル前に決める五項目を整理します。",
            ko="니들룸과 셔틀룸이 최소 선폭, 셀비지, MOQ, 단가를 어떻게 바꾸는지 정리합니다. 20 × 50 mm 안에 들어갈 법정 표시 글자 수 계산법과 샘플 전에 확정할 다섯 항목까지.",
        ),
        crumb=dict(zh="織嘜工藝", en="Woven Label Craft", fr="Fabrication des labels",
                   es="Fabricación de etiquetas", ja="織りラベルの製造", ko="직조 라벨 제작"),
        h1=dict(
            zh="織嘜織機怎麼選：針織機與梭織機的細節、成本與起訂量",
            en="Woven Label Looms: How Needle and Shuttle Looms Change Detail, Cost and MOQ",
            fr="Métiers à tisser pour labels : ce que change l'aiguille ou la navette",
            es="Telares para etiquetas tejidas: qué cambia entre agujas y lanzadera",
            ja="織りラベルの織機選び：ニードルとシャトルで何が変わるか",
            ko="직조 라벨 직기 선택: 니들룸과 셔틀룸은 무엇이 다른가",
        ),
        sum=dict(
            zh="同一張稿子，換一台織機就從細線變成粗塊。最小線寬、織邊、起訂量與單價怎麼互相牽制，20 × 50 mm 上要放多少法規字，一次講清。",
            en="The same artwork turns from hairline to chunk the moment the loom changes. How line width, selvage, MOQ and price trade against each other, and how much legal text fits on 20 × 50 mm.",
            fr="La même maquette passe du trait fin au pâté dès que le métier change. Comment trait, lisière, quantité minimale et prix s'arbitrent, et combien de mentions légales tiennent sur 20 × 50 mm.",
            es="El mismo arte pasa de filete a borrón cuando cambia el telar. Cómo se canjean trazo, orillo, mínimo y precio, y cuánto texto legal cabe en 20 × 50 mm.",
            ja="同じ原稿でも、織機が変われば細線は塊になります。線幅・耳・MOQ・単価の関係と、20 × 50 mm に収まる法定表示の量を整理します。",
            ko="같은 원고도 직기가 바뀌면 가는 선이 덩어리가 됩니다. 선폭, 셀비지, MOQ, 단가의 상충 관계와 20 × 50 mm 에 들어가는 법정 표시 분량을 정리했습니다.",
        ),
    ),
    dict(
        slug="trim-attachment-strength-pull-test-guide",
        body=A2,
        related=[
            ("garment-label-sewing-thread-guide.html",
             dict(zh="標籤縫線：規格與針距", en="Label sewing thread: spec and stitch density",
                  fr="Fil de couture pour étiquettes : spec et densité", es="Hilo de costura para etiquetas: spec y densidad",
                  ja="ラベル縫い糸：仕様と縫い目密度", ko="라벨 봉제사: 사양과 봉제 밀도")),
            ("garment-trims-quality-inspection.html",
             dict(zh="輔料品質檢驗：抽樣與判定", en="Trim quality inspection: sampling and decisions",
                  fr="Contrôle qualité des accessoires : échantillonnage", es="Inspección de calidad de accesorios: muestreo",
                  ja="副資材の品質検査：抜取と判定", ko="부자재 품질 검사: 샘플링과 판정")),
            ("garment-trims-small-parts-safety-guide.html",
             dict(zh="小零件安全：誤吞風險與測試", en="Small parts safety: ingestion risk and testing",
                  fr="Petites pièces : risque d'ingestion et essais", es="Piezas pequeñas: riesgo de ingestión y ensayos",
                  ja="小部品の安全：誤飲リスクと試験", ko="소형 부품 안전: 삼킴 위험과 시험")),
        ],
        tag=dict(zh="品質與驗收", en="Quality & Inspection", fr="Qualité et contrôle",
                 es="Calidad e inspección", ja="品質と検査", ko="품질과 검사"),
        title=dict(
            zh="輔料附著力拉力測試：織嘜、四合扣與鉚釘的驗收值 | TAGE",
            en="Trim Attachment Strength: Pull Testing Labels and Hardware | TAGE",
            fr="Résistance d'attache des accessoires : essais de traction | TAGE",
            es="Resistencia de fijación de accesorios: ensayos de tracción | TAGE",
            ja="副資材の取付強度：引張試験と合格値 | TAGE",
            ko="부자재 부착 강도: 인장 시험과 합격값 | TAGE",
        ),
        desc=dict(
            zh="輔料附著力怎麼測、怎麼驗：織嘜與洗水標的縫口拉力、四合扣與鉚釘的 EN 71-1 拉力扭力、不乾膠標剝離值，以及五個必須寫進工藝單的欄位。",
            en="Pull test values for woven labels, care labels, snaps and rivets: how attachment strength is measured, why trims fail at seams, and what to write in the spec.",
            fr="Valeurs d'essai de traction pour labels tissés, étiquettes d'entretien, pressions et rivets : comment se mesure la résistance d'attache, pourquoi ça lâche à la couture, et quoi écrire sur la fiche technique.",
            es="Valores de tracción para etiquetas tejidas, de cuidado, broches y remaches: cómo se mide la resistencia de fijación, por qué falla en la costura y qué escribir en la ficha técnica.",
            ja="織りラベル・洗濯表示・スナップ・リベットの引張試験。取付強度の測り方、縫い目で壊れる理由、仕様書に書く五つの欄をまとめます。",
            ko="직조 라벨, 케어 라벨, 스냅, 리벳의 인장 시험값. 부착 강도를 어떻게 측정하고 왜 봉제선에서 실패하는지, 사양서에 적을 다섯 항목을 정리했습니다.",
        ),
        crumb=dict(zh="品質與驗收", en="Quality & Inspection", fr="Qualité et contrôle",
                   es="Calidad e inspección", ja="品質と検査", ko="품질과 검사"),
        h1=dict(
            zh="輔料附著力：織嘜、四合扣與鉚釘的拉力測試與驗收值",
            en="Trim Attachment Strength: Pull Testing Woven Labels, Snaps and Rivets",
            fr="Résistance d'attache : essais de traction sur labels, pressions et rivets",
            es="Resistencia de fijación: tracción en etiquetas, broches y remaches",
            ja="副資材の取付強度：織りラベル・スナップ・リベットの引張試験",
            ko="부자재 부착 강도: 직조 라벨, 스냅, 리벳의 인장 시험",
        ),
        sum=dict(
            zh="洗水標 12 N 剝離就是整批重工，四合扣 40 N 張開就是一次召回。三種測試、五類輔料的驗收值，以及為什麼裂口總在車縫線而不是輔料。",
            en="A care label peeling at 12 N is rework; a snap opening at 40 N is a recall. Three test methods, acceptance values for five trims, and why the seam fails before the trim does.",
            fr="Une étiquette qui se décolle à 12 N, c'est une reprise ; une pression qui s'ouvre à 40 N, un rappel. Trois méthodes, cinq accessoires chiffrés, et pourquoi c'est la couture qui lâche.",
            es="Una etiqueta que se despega a 12 N es reproceso; un broche que se abre a 40 N es retirada. Tres métodos, cinco accesorios con valores y por qué falla la costura.",
            ja="12 N で剥がれる洗濯表示は全数手直し、40 N で外れるスナップはリコール。三つの試験法、五つの副資材の合格値、縫い目から壊れる理由。",
            ko="12 N 에서 떨어지는 케어 라벨은 전량 재작업, 40 N 에서 열리는 스냅은 리콜입니다. 세 가지 시험법, 다섯 부자재의 합격값, 봉제선에서 실패하는 이유.",
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
    "woven-label-loom-types-guide": (
        dict(zh="需要按織機分開報價，或先打一版 1:1 主嘜樣？",
             en="Need loom-specific pricing, or a 1:1 face label sample first?",
             fr="Besoin d'un chiffrage par métier, ou d'un échantillon de label 1:1 ?",
             es="¿Necesita precio por telar o una muestra 1:1 de etiqueta frontal?",
             ja="織機別の見積や、1:1 のメインラベル試作が必要ですか。",
             ko="직기별 견적이나 1:1 메인 라벨 샘플이 필요하신가요?"),
        dict(zh="索取樣品與報價 →", en="Request samples and a quote →", fr="Demander échantillons et devis →",
             es="Solicitar muestras y presupuesto →", ja="試作とお見積りを依頼 →", ko="시료와 견적 요청 →"),
    ),
    "trim-attachment-strength-pull-test-guide": (
        dict(zh="需要做拉力測試，或把驗收值寫進工藝單？",
             en="Need pull testing, or the acceptance values written into your spec?",
             fr="Besoin d'essais de traction ou des valeurs inscrites sur votre fiche technique ?",
             es="¿Necesita ensayos de tracción o fijar los valores en su ficha técnica?",
             ja="引張試験や、合格値を仕様書に落とす作業が必要ですか。",
             ko="인장 시험이나 합격값 사양서 반영이 필요하신가요?"),
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
    print("写入 %s  desc_en=%d 字符 desc_fr=%d desc_es=%d desc_zh=%d 大小=%d"
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
