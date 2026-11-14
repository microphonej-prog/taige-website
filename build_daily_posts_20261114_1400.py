# -*- coding: utf-8 -*-
"""2026-11-14 14:00 每日 FAQ：2 篇（英文主稿 + zh/fr/es/ja/ko），生成中文主页 + blog/index.html 卡片。"""
import html
import os
import re

from body_20261114_1400 import A1, A2

SKEL = "blog/gs1-digital-link-2d-barcode-labels.html"
OLD_SLUG = "gs1-digital-link-2d-barcode-labels"
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
        slug="apparel-size-designation-en-13402",
        body=A1,
        related=[
            ("clothing-size-label-guide.html",
             dict(zh="服装尺码标：S／M／L 还是号数", en="Clothing size labels: S, M, L or numbers",
                  fr="Étiquettes de taille : S, M, L ou chiffres", es="Etiquetas de talla: S, M, L o números",
                  ja="サイズ表示：S・M・L か号数か", ko="사이즈 라벨: S, M, L인가 호수인가")),
            ("care-label-standards.html",
             dict(zh="洗水标标准：各国必须标注什么", en="Care label standards: what each market requires",
                  fr="Normes d'étiquetage d'entretien : ce que chaque marché exige",
                  es="Normas de etiquetado de cuidado: qué exige cada mercado",
                  ja="洗濯表示の規格：市場ごとの義務", ko="케어 라벨 규격: 시장별 요구 사항")),
            ("garment-label-configuration-guide.html",
             dict(zh="一张衣服上要挂几张标", en="How many labels one garment needs",
                  fr="Combien d'étiquettes pour un vêtement", es="Cuántas etiquetas necesita una prenda",
                  ja="一着に何枚のラベルが必要か", ko="한 벌에 라벨이 몇 개 필요한가")),
        ],
        tag=dict(zh="尺碼與標示", en="Sizing & Labelling", fr="Tailles et marquage",
                 es="Tallas y marcado", ja="サイズと表示", ko="사이즈와 표시"),
        title=dict(
            zh="服裝尺碼標示：EN 13402 標準、身體尺寸與各國碼換算 | TAGE",
            en="Garment Size Labels: EN 13402, Body Sizes and Code Conversion | TAGE",
            fr="Étiquettes de taille : norme EN 13402 et conversion des codes | TAGE",
            es="Etiquetas de talla: norma EN 13402 y conversión de códigos | TAGE",
            ja="サイズ表示の規格：EN 13402 と身体寸法・各国コードの換算 | TAGE",
            ko="사이즈 라벨 규격: EN 13402와 신체 치수·국가별 코드 환산 | TAGE",
        ),
        desc=dict(
            zh="服裝尺碼標示指南：EN 13402 用身體圍度（cm）定義尺碼，主控尺寸決定代號、每檔 4 公分；講清日韓中換算、洗後判讀與各市場法定標示義務。",
            en="EN 13402 size labels explained: control dimensions in cm, four-centimetre code steps, JIS and KS conversions, and how to print a size label that lasts.",
            fr="Étiquettes de taille EN 13402 : dimension principale en cm, pas de 4 cm entre codes, conversions JIS et KS, et impression d'une étiquette durable.",
            es="Etiquetas de talla EN 13402: dimensión principal en cm, pasos de 4 cm, conversiones JIS y KS, e impresión de una etiqueta duradera.",
            ja="EN 13402 のサイズ表示。主寸法を cm で示す原則、コード一档 4 cm、JIS・KS の換算、洗濯後も読める表示の作り方まで。",
            ko="EN 13402 사이즈 표시. 주치수를 cm로 보는 원칙, 코드 한 단계 4 cm, JIS·KS 환산, 세탁 후에도 읽히는 라벨 제작까지.",
        ),
        crumb=dict(zh="尺碼與標示", en="Sizing & Labelling", fr="Tailles et marquage",
                   es="Tallas y marcado", ja="サイズと表示", ko="사이즈와 표시"),
        h1=dict(
            zh="服裝尺碼標示：EN 13402 的判定、代號與各國換算",
            en="Garment Size Labels: EN 13402 Rules, Size Codes and Conversion",
            fr="Étiquettes de taille : règles EN 13402, codes et conversions",
            es="Etiquetas de talla: reglas EN 13402, códigos y conversión",
            ja="サイズ表示の規格：EN 13402 の判定・コード・各国換算",
            ko="사이즈 라벨 규격: EN 13402 판정, 코드, 국가별 환산",
        ),
        sum=dict(
            zh="尺碼標描述的是身體圍度而不是成衣實寸：主控尺寸決定代號、每檔 4 公分，日 JIS 4005、韓 KS K 0050、中 GB/T 1335 各有算法，附下單前六項核對。",
            en="A size label describes the body, not the garment: the control dimension sets the code, one step is 4 cm, and JIS, KS and GB/T run their own codes. Six checks before ordering.",
            fr="Une étiquette de taille décrit le corps, pas le vêtement : la dimension principale fixe le code, un cran vaut 4 cm, et JIS, KS et GB/T ont leurs propres codes.",
            es="La etiqueta de talla describe el cuerpo, no la prenda: la dimensión principal fija el código, un escalón son 4 cm, y JIS, KS y GB/T usan sus propios códigos.",
            ja="サイズ表示が示すのは身体寸法であり製品実寸ではありません。主寸法がコードを決め、一档 4 cm。JIS・KS・GB/T の換算と発注前の確認項目をまとめます。",
            ko="사이즈 라벨은 제품 실측이 아니라 신체 치수를 나타냅니다. 주치수가 코드를 정하고 한 단계는 4 cm입니다. JIS·KS·GB/T 환산과 발주 전 확인 항목을 정리했습니다.",
        ),
    ),
    dict(
        slug="silicone-gripper-tape-guide",
        body=A2,
        related=[
            ("elastic-trims-selection-guide.html",
             dict(zh="弹性带选型：宽度、拉伸与回复", en="Elastic trims: width, stretch and recovery",
                  fr="Élastiques : largeur, allongement et reprise", es="Elásticos: ancho, estiramiento y recuperación",
                  ja="伸縮テープの選定：幅・伸長・回復", ko="신축 테이프 선정: 폭, 신장, 회복")),
            ("jacquard-elastic-waistband-guide.html",
             dict(zh="提花松紧腰头：结构与手感", en="Jacquard elastic waistbands: structure and hand feel",
                  fr="Ceintures élastiques jacquard : structure et toucher", es="Cinturas elásticas jacquard: estructura y tacto",
                  ja="ジャカードゴムウエスト：構造と風合い", ko="자카드 고무 허리 밴드: 구조와 촉감")),
            ("garment-drawcord-guide.html",
             dict(zh="抽绳与绳头：规格与测试", en="Drawcords and cord ends: spec and testing",
                  fr="Cordons et embouts : spécifications et essais", es="Cordones y terminales: especificación y ensayos",
                  ja="ドローコードとコードエンド：仕様と試験", ko="드로코드와 코드 엔드: 사양과 시험")),
        ],
        tag=dict(zh="彈性輔料", en="Elastic Trims", fr="Accessoires élastiques",
                 es="Accesorios elásticos", ja="伸縮副資材", ko="신축 부자재"),
        title=dict(
            zh="防滑矽膠帶（Gripper Tape）：規格、耐洗與選型 | TAGE",
            en="Silicone Gripper Tape: Specs, Wash Durability and Selection | TAGE",
            fr="Ruban antidérapant en silicone : specs et durabilité | TAGE",
            es="Cinta antideslizante de silicona: especificaciones y lavado | TAGE",
            ja="シリコングリッパーテープ：仕様・耐洗濯性・選定 | TAGE",
            ko="실리콘 그리퍼 테이프: 사양, 세탁 내구성, 선정 | TAGE",
        ),
        desc=dict(
            zh="防滑矽膠帶選型指南：三種結構、七個必談數字（寬度、塗布量、點距、硬度、剝離）、矽膠與 PVC 的法規差異，以及熱壓與洗滌的失效點。",
            en="Silicone gripper tape specs: base width, coating weight, dot pitch, peel adhesion and wash durability, plus why PVC is being phased out of trims today.",
            fr="Ruban antidérapant silicone : largeur, grammage, pas des points, pelage et tenue au lavage, et pourquoi le PVC disparaît des accessoires.",
            es="Cinta antideslizante de silicona: ancho, gramaje, paso de puntos, peladura y resistencia al lavado, y por qué el PVC sale de los accesorios.",
            ja="シリコングリッパーテープの仕様。基材幅・塗布量・ピッチ・硬度・剥離強度、PVC からの置き換え理由、熱圧着と洗濯での劣化要因を整理します。",
            ko="실리콘 그리퍼 테이프 사양. 기재 폭, 도포량, 간격, 경도, 박리 강도와 PVC 대체 이유, 열압착·세탁에서의 성능 저하 요인을 정리했습니다.",
        ),
        crumb=dict(zh="彈性輔料", en="Elastic Trims", fr="Accessoires élastiques",
                   es="Accesorios elásticos", ja="伸縮副資材", ko="신축 부자재"),
        h1=dict(
            zh="防滑矽膠帶（Gripper Tape）：結構、七個數字與耐洗判定",
            en="Silicone Gripper Tape: Structures, Seven Numbers and Wash Durability",
            fr="Ruban antidérapant en silicone : structures, sept chiffres et tenue au lavage",
            es="Cinta antideslizante de silicona: estructuras, siete cifras y lavado",
            ja="シリコングリッパーテープ：構造・七つの数値・耐洗濯性の判定",
            ko="실리콘 그리퍼 테이프: 구조, 일곱 가지 수치, 세탁 내구성 판정",
        ),
        sum=dict(
            zh="肩帶與腰頭裡那條發澀的帶子，失效點在第 15 次洗滌之後：三種結構、七個必須落筆的數字、矽膠與 PVC 的法規差異，以及熱壓後 24 小時再測的驗收方法。",
            en="The tacky strip inside a strap or waistband fails after the fifteenth wash, not at the factory: three constructions, seven numbers to write down, and the 24-hour rule before peel testing.",
            fr="La bande adhérente d'une bretelle ou d'une ceinture lâche au quinzième lavage, pas à l'usine : trois constructions, sept chiffres à écrire, et la règle des 24 heures avant l'essai de pelage.",
            es="La banda adherente de un tirante o una cintura falla en el lavado quince, no en fábrica: tres construcciones, siete cifras que hay que escribir y la regla de 24 horas antes del ensayo.",
            ja="肩ひもやウエストの内側の帯は、工場ではなく十五回目の洗濯後に劣化します。三つの構造、記載すべき七つの数値、熱圧着後 24 時間置いてから試験する原則をまとめます。",
            ko="어깨끈과 허리 밴드 안쪽의 띠는 공장이 아니라 열다섯 번째 세탁 후에 성능이 떨어집니다. 세 가지 구조, 반드시 적어야 할 일곱 수치, 열압착 후 24시간 방치 원칙을 정리했습니다.",
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


CTA = dict(zh="需要打樣、尺碼確認或防滑帶測試？", en="Need samples, size confirmation or gripper tape testing?",
           fr="Besoin d'échantillons, de confirmation de taille ou d'essais de ruban ?",
           es="¿Necesita muestras, confirmación de talla o ensayos de cinta?",
           ja="試作・サイズ確認・グリッパーテープの試験は。",
           ko="시료, 사이즈 확인, 그리퍼 테이프 시험이 필요하신가요?")
CTA_BTN = dict(zh="索取樣品與報價 →", en="Request samples and a quote →", fr="Demander échantillons et devis →",
               es="Solicitar muestras y presupuesto →", ja="試作とお見積りを依頼 →", ko="시료와 견적 요청 →")


def render_cta():
    return ('      <div class="cta-box">\n'
            '        <p %s>%s</p>\n'
            '        <a class="cta-btn" href="../contact.html" %s>%s</a>\n'
            '      </div>' % (A(CTA), html.escape(CTA["zh"]), A(CTA_BTN), html.escape(CTA_BTN["zh"])))


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
