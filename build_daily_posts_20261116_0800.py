# -*- coding: utf-8 -*-
"""2026-11-16 08:00 每日 FAQ：2 篇（英文主稿 + zh/fr/es/ja/ko），生成中文主页 + blog/index.html 卡片。"""
import html
import os
import re

from body_20261116_0800_a import A1
from body_20261116_0800_b import A2

SKEL = "blog/trim-dry-cleaning-fastness-guide.html"
OLD_SLUG = "trim-dry-cleaning-fastness-guide"
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
        slug="bag-hardware-d-rings-swivel-hooks-guide",
        body=A1,
        related=[
            ("webbing-tape-selection-guide.html",
             dict(zh="織帶選型：材質、密度與拉力", en="Webbing selection: fibre, density and tensile",
                  fr="Sangles : matière, densité et traction", es="Cintas: fibra, densidad y tracción",
                  ja="織帯の選定：素材・密度・引張強さ", ko="웨빙 선택: 소재, 밀도, 인장 강도")),
            ("metal-trims-nickel-release-guide.html",
             dict(zh="金屬輔料鎳釋放：限值與對策", en="Nickel release from metal trims: limits and fixes",
                  fr="Libération de nickel des pièces métalliques : limites", es="Liberación de níquel en piezas metálicas: límites",
                  ja="金属部品のニッケル溶出：規制値と対策", ko="금속 부품 니켈 용출: 규제치와 대응")),
            ("eyelet-grommet-rivet-guide.html",
             dict(zh="雞眼、氣眼與鉚釘：規格與固定", en="Eyelets, grommets and rivets: sizes and setting",
                  fr="Œillets et rivets : dimensions et pose", es="Ojales y remaches: medidas y colocación",
                  ja="ハトメ・グロメット・リベット：寸法と固定", ko="아일릿, 그로밋, 리벳: 규격과 고정")),
        ],
        tag=dict(zh="五金與輔料", en="Hardware & Trims", fr="Quincaillerie et accessoires",
                 es="Herrajes y accesorios", ja="金具と副資材", ko="금속 부자재"),
        title=dict(
            zh="箱包五金：D 環、狗扣與調整扣的承重與驗收 | TAGE",
            en="Bag Hardware: D-Rings, Swivel Hooks and Adjusters | TAGE",
            fr="Quincaillerie de sac : anneaux D, mousquetons et bloqueurs | TAGE",
            es="Herrajes de bolso: anillas D, mosquetones y reguladores | TAGE",
            ja="バッグ金具：D カン・ナスカン・アジャスターの荷重と検収 | TAGE",
            ko="가방 금속 부자재: D링·스위블 후크·길이 조절기 | TAGE",
        ),
        desc=dict(
            zh="箱包五金採購指南：D 環與狗扣的承重三數值、織帶寬度與槽口配合、鹽霧小時數與鍍層厚度、REACH 鎳釋放限制，以及六項 AQL 驗收寫法。",
            en="How to specify bag hardware: D-rings, swivel hooks and strap adjusters, load ratings, salt spray, plating thickness, nickel release limits and AQL checks.",
            fr="Spécifier la quincaillerie de sac : anneaux D, mousquetons et bloqueurs, charges admissibles, brouillard salin, nickel et contrôles à inscrire au bon de commande.",
            es="Especificar herrajes de bolso: anillas D, mosquetones y reguladores, cargas admisibles, niebla salina, níquel y controles que van en el pedido.",
            ja="バッグ金具の仕様化。D カン・ナスカン・アジャスターの許容荷重、メッキと塩水噴霧時間、ニッケル溶出、AQL 検収の書き方をまとめます。",
            ko="가방 금속 부자재 사양 정리. D링·스위블 후크·길이 조절기의 허용 하중, 도금과 염수 분무 시간, 니켈 용출, AQL 검수 항목을 다룹니다.",
        ),
        crumb=dict(zh="五金與輔料", en="Hardware & Trims", fr="Quincaillerie et accessoires",
                   es="Herrajes y accesorios", ja="金具と副資材", ko="금속 부자재"),
        h1=dict(
            zh="箱包五金：D 環、狗扣與調整扣的承重、電鍍與驗收",
            en="Bag Hardware: D-Rings, Swivel Hooks and Strap Adjusters",
            fr="Quincaillerie de sac : anneaux D, mousquetons et bloqueurs de sangle",
            es="Herrajes de bolso: anillas D, mosquetones y reguladores de cinta",
            ja="バッグ金具：D カン・ナスカン・アジャスターの荷重・メッキ・検収",
            ko="가방 금속 부자재: D링, 스위블 후크, 길이 조절기의 하중·도금·검수",
        ),
        sum=dict(
            zh="同一個 20 mm D 環，破壞載荷能差三倍；同一張圖紙，掛鍍與滾鍍的鹽霧結果能差一倍。三個數字、兩道測試、六項抽樣，把箱包五金從「看著差不多」變成可驗收的規格。",
            en="The same 20 mm D-ring can differ threefold in breaking load, and one drawing can halve its salt-spray life between rack and barrel plating. Three numbers, two tests and six checks turn bag hardware into a specification.",
            fr="Un même anneau D de 20 mm peut varier du triple en rupture, et un même plan peut diviser par deux la tenue au brouillard salin selon le type de revêtement. Trois chiffres, deux essais, six contrôles.",
            es="Una misma anilla D de 20 mm puede triplicar su carga de rotura, y un mismo plano puede reducir a la mitad la niebla salina según el tipo de baño. Tres cifras, dos ensayos y seis controles.",
            ja="同じ 20 mm の D カンでも破断荷重は三倍まで差が出て、同じ図面でもメッキ方式で塩水噴霧の結果が半分になります。三つの数値、二つの試験、六つの検収項目で仕様化します。",
            ko="같은 20 mm D링도 파단 하중이 세 배까지 차이 나고, 같은 도면도 도금 방식에 따라 염수 분무 결과가 절반이 됩니다. 세 숫자, 두 시험, 여섯 검수 항목으로 사양화합니다.",
        ),
    ),
    dict(
        slug="snap-fastener-press-stud-guide",
        body=A2,
        related=[
            ("garment-buttons-fasteners-guide.html",
             dict(zh="紐扣與扣件：全品類選型", en="Buttons and fasteners: the full selection",
                  fr="Boutons et fermetures : la sélection complète", es="Botones y cierres: la selección completa",
                  ja="ボタンと留め具：全体の選定", ko="단추와 여밈 장치: 전체 선택")),
            ("metal-trims-nickel-release-guide.html",
             dict(zh="金屬輔料鎳釋放：限值與對策", en="Nickel release from metal trims: limits and fixes",
                  fr="Libération de nickel des pièces métalliques : limites", es="Liberación de níquel en piezas metálicas: límites",
                  ja="金属部品のニッケル溶出：規制値と対策", ko="금속 부품 니켈 용출: 규제치와 대응")),
            ("plastic-hardware-trims-guide.html",
             dict(zh="塑料五金：材質與耐溫", en="Plastic hardware: materials and heat resistance",
                  fr="Quincaillerie plastique : matières et tenue en température", es="Herrajes plásticos: materiales y temperatura",
                  ja="プラスチック金具：素材と耐熱性", ko="플라스틱 금속 부품: 소재와 내열성")),
        ],
        tag=dict(zh="五金與輔料", en="Hardware & Trims", fr="Quincaillerie et accessoires",
                 es="Herrajes y accesorios", ja="金具と副資材", ko="금속 부자재"),
        title=dict(
            zh="按扣與四合扣：尺寸、開合力與鎳釋放 | TAGE",
            en="Snap Fasteners & Press Studs: Sizes, Holding Force | TAGE",
            fr="Pressions et boutons à ressort : tailles et force | TAGE",
            es="Automáticos y botones de resorte: medidas y fuerza | TAGE",
            ja="スナップ・ジャンパーホック：サイズと保持力 | TAGE",
            ko="스냅·프레스 스터드: 사이즈와 체결력 | TAGE",
        ),
        desc=dict(
            zh="按扣選型指南：四類按扣的差別、ligne 與毫米換算、開合力的實測區間與洗後衰減、黃銅與 POM 取捨、REACH 鎳釋放限制，以及鉚合模具與五項驗收。",
            en="Snap fasteners and press studs: ligne sizing in millimetres, holding force in newtons, brass versus POM, nickel release limits, setting dies and five checks.",
            fr="Pressions et boutons à ressort : tailles en lignes et millimètres, force de maintien en newtons, laiton ou POM, limites de nickel, matrices de pose et cinq contrôles.",
            es="Automáticos y botones de resorte: medidas en líneas y milímetros, fuerza de sujeción en newtons, latón o POM, límites de níquel, troqueles y cinco controles.",
            ja="スナップの選定。ラインとミリの換算、保持力の実測レンジと洗濯後の低下、黄銅と POM の使い分け、ニッケル溶出規制、金型と五項目の検収をまとめます。",
            ko="스냅 선택 가이드. 리뉴와 밀리미터 환산, 체결력 실측 범위와 세탁 후 저하, 황동과 POM 선택, 니켈 용출 규제, 금형과 다섯 가지 검수를 정리합니다.",
        ),
        crumb=dict(zh="五金與輔料", en="Hardware & Trims", fr="Quincaillerie et accessoires",
                   es="Herrajes y accesorios", ja="金具と副資材", ko="금속 부자재"),
        h1=dict(
            zh="按扣與四合扣：尺寸、開合力、鉚合與驗收",
            en="Snap Fasteners and Press Studs: Sizing, Holding Force and Setting",
            fr="Pressions et boutons à ressort : tailles, force de maintien et pose",
            es="Automáticos y botones de resorte: medidas, fuerza de sujeción y colocación",
            ja="スナップ・ジャンパーホック：サイズ・保持力・打ち込み・検収",
            ko="스냅과 프레스 스터드: 사이즈, 체결력, 타격, 검수",
        ),
        sum=dict(
            zh="按扣鬆脫八成不是按扣壞，是鉚合錯：模具不配、爪長差 0.5 mm、面料厚度沒量。ligne 換算、開合力區間、洗後衰減、鎳釋放與三次試打，五件事寫進規格就不會再靠手感。",
            en="Loose snaps are mostly a setting failure, not a snap failure: mismatched die, prong length off by half a millimetre, thickness never measured. Ligne conversion, force ranges, wash decay, nickel and three trial strikes settle it.",
            fr="Une pression qui se desserre vient surtout de la pose : matrice inadaptée, griffe à 0,5 mm près, épaisseur jamais mesurée. Conversion des lignes, plages de force, perte au lavage, nickel et trois essais règlent la question.",
            es="Un automático flojo suele ser un fallo de colocación: troquel inadecuado, púa con medio milímetro de diferencia, espesor sin medir. Conversión de líneas, rangos de fuerza, pérdida en lavado, níquel y tres pruebas lo resuelven.",
            ja="スナップの緩みは八割が打ち込み不良です。金型の不一致、爪長 0.5 mm の差、素材厚の未測定。ライン換算、保持力レンジ、洗濯後の低下、ニッケル、三回の試打で解決します。",
            ko="스냅 풀림은 대부분 타격 불량입니다. 금형 불일치, 다리 길이 0.5 mm 차이, 소재 두께 미측정. 리뉴 환산, 체력 범위, 세탁 후 저하, 니켈, 세 번의 시타로 해결됩니다.",
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
    "bag-hardware-d-rings-swivel-hooks-guide": (
        dict(zh="把手上的織帶與五金寄一段過來，我們按實寬配對並做拉力實測？",
             en="Send a length of your webbing and the fitting, and we will match the slot and pull-test it?",
             fr="Envoyez un morceau de sangle et la pièce : nous assortirons la lumière et ferons l'essai de traction ?",
             es="¿Envía un tramo de cinta y la pieza, y ajustamos la ranura y hacemos el ensayo de tracción?",
             ja="織帯と金具を少しお送りいただければ、実幅に合わせて選定し引張試験を行います。",
             ko="웨빙과 금속 부품을 조금 보내주시면 실제 폭에 맞춰 선정하고 인장 시험을 진행하겠습니다."),
        dict(zh="索取樣品與報價 →", en="Request samples and a quote →", fr="Demander échantillons et devis →",
             es="Solicitar muestras y presupuesto →", ja="試作とお見積りを依頼 →", ko="시료와 견적 요청 →"),
    ),
    "snap-fastener-press-stud-guide": (
        dict(zh="把面料樣與現用按扣寄來，我們先試打三片再定爪長？",
             en="Send the fabric swatch and your current snap and we will strike three trials before fixing prong length?",
             fr="Envoyez le tissu et votre pression actuelle : nous ferons trois essais avant de fixer la griffe ?",
             es="¿Envía la muestra de tejido y tu automático actual y hacemos tres pruebas antes de fijar la púa?",
             ja="生地見本と現行スナップをお送りいただければ、三回試打してから爪長を決めます。",
             ko="원단 샘플과 현재 사용 중인 스냅을 보내주시면 세 번 시타한 뒤 다리 길이를 정하겠습니다."),
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
