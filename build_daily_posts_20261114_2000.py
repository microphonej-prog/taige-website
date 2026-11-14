# -*- coding: utf-8 -*-
"""2026-11-14 20:00 每日 FAQ：2 篇（英文主稿 + zh/fr/es/ja/ko），生成中文主页 + blog/index.html 卡片。"""
import html
import os
import re

from body_20261114_2000 import A1, A2

SKEL = "blog/silicone-gripper-tape-guide.html"
OLD_SLUG = "silicone-gripper-tape-guide"
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
        slug="trim-dry-cleaning-fastness-guide",
        body=A1,
        related=[
            ("care-label-standards.html",
             dict(zh="洗水標標準：各市場必須標什麼", en="Care label standards by market",
                  fr="Normes d'entretien par marché", es="Normas de cuidado por mercado",
                  ja="市場別の洗濯表示規格", ko="시장별 케어 라벨 규격")),
            ("trim-crocking-perspiration-fastness-guide.html",
             dict(zh="耐摩擦與耐汗漬色牢度", en="Rubbing and perspiration fastness",
                  fr="Solidité au frottement et à la sueur", es="Solidez al roce y al sudor",
                  ja="摩擦・汗に対する堅牢度", ko="마찰·땀 견뢰도")),
            ("industrial-laundry-care-label-guide.html",
             dict(zh="工業洗滌的洗護標要求", en="Care labels for industrial laundering",
                  fr="Étiquettes pour blanchisserie industrielle", es="Etiquetas para lavandería industrial",
                  ja="産業洗濯向けの洗濯表示", ko="산업 세탁용 케어 라벨")),
        ],
        tag=dict(zh="洗護與牢度", en="Care & Fastness", fr="Entretien et solidité",
                 es="Cuidado y solidez", ja="洗濯と堅牢度", ko="취급과 견뢰도"),
        title=dict(
            zh="服裝輔料耐乾洗色牢度：ISO 105-D01、溶劑與洗護符號 | TAGE",
            en="Dry Cleaning Fastness of Garment Trims: ISO 105-D01 Guide | TAGE",
            fr="Solidité des accessoires au nettoyage à sec : ISO 105-D01 | TAGE",
            es="Solidez de accesorios a la limpieza en seco: ISO 105-D01 | TAGE",
            ja="副資材のドライクリーニング堅牢度：ISO 105-D01 と洗濯表示 | TAGE",
            ko="부자재 드라이클리닝 견뢰도: ISO 105-D01과 취급 표시 | TAGE",
        ),
        desc=dict(
            zh="服裝輔料耐乾洗色牢度指南：ISO 105-D01 的四氯乙烯測試條件、七類輔料最先失效的位置、洗護符號在歐美日韓的差異，以及可寫進工藝單的驗收條款。",
            en="Trim dry cleaning fastness: ISO 105-D01 in perchloroethylene, the seven trims that fail first, and the spec wording that stops claims long after delivery.",
            fr="Solidité au nettoyage à sec : méthode ISO 105-D01 au perchloroéthylène, accessoires qui lâchent en premier et clauses à inscrire sur la fiche technique.",
            es="Solidez en limpieza en seco: método ISO 105-D01 con percloroetileno, qué accesorios fallan primero y qué cláusulas de aceptación escribir en la ficha técnica.",
            ja="ドライクリーニング堅牢度の実務。ISO 105-D01（パークロロエチレン）の条件、先に劣化する副資材、仕様書に書く合格基準、市場別の洗濯表示の違いを整理します。",
            ko="드라이클리닝 견뢰도 실무. ISO 105-D01(퍼클로로에틸렌) 조건, 먼저 망가지는 부자재, 사양서에 적을 합격 기준, 시장별 취급 표시 차이를 정리했습니다.",
        ),
        crumb=dict(zh="洗護與牢度", en="Care & Fastness", fr="Entretien et solidité",
                   es="Cuidado y solidez", ja="洗濯と堅牢度", ko="취급과 견뢰도"),
        h1=dict(
            zh="服裝輔料耐乾洗色牢度：溶劑、標準與驗收線",
            en="Dry Cleaning Fastness of Garment Trims: Solvents, Standard and Acceptance",
            fr="Solidité des accessoires au nettoyage à sec : solvants, norme et acceptation",
            es="Solidez de los accesorios a la limpieza en seco: disolventes, norma y aceptación",
            ja="副資材のドライクリーニング堅牢度：溶剤・試験法・合格基準",
            ko="부자재 드라이클리닝 견뢰도: 용제, 시험법, 합격 기준",
        ),
        sum=dict(
            zh="乾洗不是溫和的洗：四氯乙烯會抽走增塑劑、溶掉熱轉印墨水。七類輔料誰先壞、ISO 105-D01 怎麼判、工藝單該寫哪幾個數字，一次講清。",
            en="Dry cleaning is not the gentle option: perchloroethylene strips plasticiser and re-dissolves transfer ink. Which seven trims fail first, how ISO 105-D01 grades them, and what to write in the spec.",
            fr="Le nettoyage à sec n'est pas doux : le perchloroéthylène extrait les plastifiants et redissout les encres. Quels accessoires lâchent, comment l'ISO 105-D01 les note, et quoi écrire sur la fiche technique.",
            es="La limpieza en seco no es suave: el percloroetileno extrae plastificantes y redisuelve tintas. Qué accesorios fallan, cómo los valora la ISO 105-D01 y qué escribir en la ficha técnica.",
            ja="ドライクリーニングはやさしい洗い方ではありません。可塑剤が抜け、熱転写インクが再溶解します。先に壊れる七つの副資材、ISO 105-D01 の判定、仕様書に書く数値をまとめます。",
            ko="드라이클리닝은 순한 세탁이 아닙니다. 가소제가 빠지고 열전사 잉크가 다시 용해됩니다. 먼저 망가지는 일곱 가지 부자재, ISO 105-D01 판정, 사양서에 적을 수치를 정리했습니다.",
        ),
    ),
    dict(
        slug="back-neck-tape-guide",
        body=A2,
        related=[
            ("rib-knit-collar-cuff-guide.html",
             dict(zh="羅紋領口與袖口：結構與回彈", en="Rib collar and cuff: structure and recovery",
                  fr="Col et poignet côtelés : structure et reprise", es="Cuello y puño acanalados: estructura y recuperación",
                  ja="リブ襟・袖口：構造と回復性", ko="리브 칼라·커프: 구조와 회복성")),
            ("garment-label-sewing-thread-guide.html",
             dict(zh="標籤縫線：規格與針距", en="Label sewing thread: spec and stitch density",
                  fr="Fil de couture pour étiquettes : spec et densité", es="Hilo de costura para etiquetas: spec y densidad",
                  ja="ラベル縫い糸：仕様と縫い目密度", ko="라벨 봉제사: 사양과 봉제 밀도")),
            ("webbing-tape-selection-guide.html",
             dict(zh="織帶選型：材質、密度與拉伸", en="Webbing selection: material, density, stretch",
                  fr="Sangles : matière, densité, allongement", es="Cintas técnicas: material, densidad, estiramiento",
                  ja="ウェビングの選定：素材・密度・伸長", ko="웨빙 선정: 소재, 밀도, 신장")),
        ],
        tag=dict(zh="領口與結構輔料", en="Neckline & Structural Trims", fr="Encolure et structure",
                 es="Escote y estructura", ja="襟ぐりと構造副資材", ko="목선과 구조 부자재"),
        title=dict(
            zh="後領包邊帶：寬度、材質與車縫規格 | TAGE",
            en="Back Neck Tape: Width, Materials and Sewing Specs | TAGE",
            fr="Ruban d'encolure dos : largeur, matières et couture | TAGE",
            es="Cinta de escote trasero: ancho, materiales y costura | TAGE",
            ja="後ろ襟テープ：幅・素材・縫製仕様 | TAGE",
            ko="뒷목 테이프: 폭, 소재, 봉제 사양 | TAGE",
        ),
        desc=dict(
            zh="後領包邊帶選型與規格：12–20 mm 寬度、滌綸斜紋與針織帶的差別、縮水率 2% 以內、ΔE 與針距，以及三個最常見的退貨理由與合規要求。",
            en="Back neck tape specs: 12–20 mm width, twill versus knit tape, shrinkage, colour tolerance, stitch density and the compliance documents brands ask for first.",
            fr="Ruban d'encolure dos : largeur 12–20 mm, sergé ou tricot, retrait, tolérance de couleur, densité de piqûre et documents de conformité exigés par les marques.",
            es="Cinta de escote trasero: ancho de 12–20 mm, sarga o punto, merma, tolerancia de color, densidad de puntada y documentos de conformidad que piden las marcas.",
            ja="後ろ襟テープの仕様。幅 12〜20 mm、綾テープとニットテープの違い、収縮率、色差、縫い目密度、そしてブランドが最初に求める適合書類まで整理します。",
            ko="뒷목 테이프 사양. 폭 12~20 mm, 능직과 니트 테이프의 차이, 수축률, 색차, 봉제 밀도, 그리고 브랜드가 먼저 요구하는 적합성 서류까지 정리했습니다.",
        ),
        crumb=dict(zh="領口與結構輔料", en="Neckline & Structural", fr="Encolure et structure",
                   es="Escote y estructura", ja="襟ぐりと構造副資材", ko="목선과 구조 부자재"),
        h1=dict(
            zh="後領包邊帶：四個作用、八個數字與三種車縫做法",
            en="Back Neck Tape: Four Jobs, Eight Numbers and Three Sewing Methods",
            fr="Ruban d'encolure dos : quatre fonctions, huit chiffres et trois méthodes",
            es="Cinta de escote trasero: cuatro funciones, ocho cifras y tres métodos",
            ja="後ろ襟テープ：四つの役割・八つの数値・三つの縫い方",
            ko="뒷목 테이프: 네 가지 역할, 여덟 가지 수치, 세 가지 봉제 방식",
        ),
        sum=dict(
            zh="後領那道 15 mm 的帶子同時決定刺癢、變形、領標與品牌露出。八個必須寫成數字的參數、三種車縫做法的坑，以及三個最常見的退貨理由。",
            en="That 15 mm strip at the back neck decides itching, distortion, label comfort and brand visibility. Eight numbers to write down, three sewing methods and their traps, three rejection reasons.",
            fr="Cette bande de 15 mm décide des démangeaisons, de la déformation, du confort de l'étiquette et de la visibilité de la marque. Huit chiffres, trois méthodes de couture et trois motifs de refus.",
            es="Esa tira de 15 mm decide el picor, la deformación, el confort de la etiqueta y la visibilidad de marca. Ocho cifras, tres métodos de costura y tres motivos de rechazo.",
            ja="後ろ襟の 15 mm の帯が、ちくちく感・型崩れ・ラベルの快適さ・ブランドの見え方を同時に決めます。数値化すべき八項目、三つの縫い方の落とし穴、三つの返品理由。",
            ko="뒷목의 15 mm 띠가 따가움, 변형, 라벨 쾌적성, 브랜드 노출을 동시에 결정합니다. 숫자로 적어야 할 여덟 항목, 세 가지 봉제 방식의 함정, 세 가지 반품 사유.",
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
    "trim-dry-cleaning-fastness-guide": (
        dict(zh="需要做乾洗牢度測試，或指定耐溶劑的輔料？", en="Need dry cleaning fastness testing, or solvent-resistant trims specified?",
             fr="Besoin d'essais de solidité au nettoyage à sec ou d'accessoires résistants aux solvants ?",
             es="¿Necesita ensayos de solidez en seco o accesorios resistentes a disolventes?",
             ja="ドライ堅牢度の試験や、耐溶剤副資材の指定は。", ko="드라이 견뢰도 시험이나 내용제 부자재 지정이 필요하신가요?"),
        dict(zh="索取樣品與報價 →", en="Request samples and a quote →", fr="Demander échantillons et devis →",
             es="Solicitar muestras y presupuesto →", ja="試作とお見積りを依頼 →", ko="시료와 견적 요청 →"),
    ),
    "back-neck-tape-guide": (
        dict(zh="需要後領帶打樣、配色或縮率測試？", en="Need neck tape sampling, colour matching or shrinkage testing?",
             fr="Besoin d'échantillons de ruban d'encolure, d'accord couleur ou d'essais de retrait ?",
             es="¿Necesita muestras de cinta de escote, igualación de color o ensayos de merma?",
             ja="後ろ襟テープの試作・色合わせ・収縮試験は。", ko="뒷목 테이프 샘플, 색 맞춤, 수축 시험이 필요하신가요?"),
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
