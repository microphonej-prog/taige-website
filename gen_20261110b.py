#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-11-10 20:00 批次：2 篇新文章（英文主稿 + 八语属性），从 8 语骨架生成。"""
import re, os, sys, io

SKEL = "blog/what-is-a-hang-tag.html"
OLD_H1 = "什麼是吊牌？定義、四個組成部分與買手驗收清單"
OLD_SLUG = "trim-material-substitution-guide.html"
DATE_ZH = "2026年11月10日"

ARTICLES = [
    dict(
        slug="label-stitch-density-spi-guide.html",
        body="blog/_body_stitch.html",
        title={
            "zh": "標籤縫紉密度（SPI）怎麼定：每英吋針數與耐洗實測 | TAIGE",
            "en": "Stitch Density (SPI) for Labels and Trims: What to Specify | TAIGE",
            "fr": "Densité de piqûre (SPI) des étiquettes : que spécifier | TAIGE",
            "es": "Densidad de puntada (SPI) en etiquetas: qué especificar | TAIGE",
            "ja": "ラベルの縫い目密度（SPI）の決め方：耐洗性の実測と指定 | TAIGE",
            "ko": "라벨 봉제 밀도(SPI) 정하기: 내세탁성 실측과 사양 | TAIGE",
            "de": "Stichdichte (SPI) für Etiketten: Was in die Spezifikation gehört | TAIGE",
            "pt": "Densidade de costura (SPI) em etiquetas: o que especificar | TAIGE",
        },
        desc={
            "zh": "同樣的洗水標，8 SPI 與 12 SPI 的差別是十次洗滌後還在不在。講清按固定位置的針數區間、三種失效模式、歐盟與中國的標示依據，以及打樣室能做完的四項驗收。東莞泰閣包裝。",
            "en": "Stitch density (SPI) decides whether a garment label survives 30 washes. Typical SPI by attachment point, stitch types and fold clearance to specify.",
            "fr": "La densité de piqûre décide si une étiquette tient 30 lavages. Densités par point de fixation, types de point et dégagement de pli à spécifier.",
            "es": "La densidad de puntada decide si una etiqueta aguanta 30 lavados. Densidades por punto de fijación, tipos de puntada y margen de doblez.",
            "ja": "縫い目密度（SPI）は、30回の洗濯にラベルが耐えるかを決めます。取付位置ごとの針数、縫い方、折り余裕の指定方法を整理します。",
            "ko": "봉제 밀도(SPI)는 30회 세탁 후 라벨이 남는지를 결정합니다. 고정 위치별 바늘 수, 박음 방식, 접힘 여유 지정법을 정리했습니다.",
            "de": "Die Stichdichte (SPI) entscheidet, ob ein Etikett 30 Wäschen übersteht: übliche Werte je Befestigungspunkt, Sticharten und Bruchabstand.",
            "pt": "A densidade de costura (SPI) decide se a etiqueta resiste a 30 lavagens: valores por ponto de fixação, tipos de ponto e folga da dobra.",
        },
        crumb={
            "zh": "縫紉密度", "en": "Stitch Density", "fr": "Densité de piqûre",
            "es": "Densidad de puntada", "ja": "縫い目密度", "ko": "봉제 밀도",
            "de": "Stichdichte", "pt": "Densidade de costura",
        },
        h1={
            "zh": "標籤與輔料的縫紉密度：SPI 決定它能不能撐過洗滌",
            "en": "Label and Trim Stitch Density: How SPI Decides If It Survives the Wash",
            "fr": "Densité de piqûre des étiquettes et accessoires : comment le SPI décide de la tenue au lavage",
            "es": "Densidad de puntada en etiquetas y aviamentos: cómo el SPI decide si resiste el lavado",
            "ja": "ラベルと副資材の縫い目密度：SPI が洗濯耐性を決める",
            "ko": "라벨과 부자재의 봉제 밀도: SPI가 세탁 내구성을 결정한다",
            "de": "Stichdichte bei Etiketten und Zutaten: Wie SPI über die Wäsche entscheidet",
            "pt": "Densidade de costura em etiquetas e aviamentos: como o SPI decide a resistência à lavagem",
        },
        meta={
            "zh": "泰閣包裝 · 更新於 " + DATE_ZH,
            "en": "By TAIGE Packaging &nbsp;·&nbsp; Updated November 10, 2026",
            "fr": "Par TAIGE Packaging &nbsp;·&nbsp; Mis à jour le 10 novembre 2026",
            "es": "Por TAIGE Packaging &nbsp;·&nbsp; Actualizado el 10 de noviembre de 2026",
            "ja": "泰閣包装 · 2026年11月10日更新",
            "ko": "TAIGE 패키징 · 2026년 11월 10일 업데이트",
            "de": "Von TAIGE Packaging &nbsp;·&nbsp; Aktualisiert am 10. November 2026",
            "pt": "Por TAIGE Packaging &nbsp;·&nbsp; Atualizado em 10 de novembro de 2026",
        },
        card_tag={
            "zh": "工藝", "en": "Craft", "fr": "Technique", "es": "Técnica",
            "ja": "加工", "ko": "공정", "de": "Verarbeitung", "pt": "Processo",
        },
        card_sum={
            "zh": "同樣的洗水標，8 SPI 與 12 SPI 的差別是十次洗滌後還在不在。按固定位置的針數區間、三種失效、合規依據與打樣室驗法。",
            "en": "The same care label lasts ten washes at 8 SPI and thirty at 12. SPI ranges by attachment point, three failure modes and the sample-room tests.",
            "fr": "La même étiquette tient dix lavages à 8 SPI et trente à 12. Densités par point de fixation, trois défauts et les essais en atelier.",
            "es": "La misma etiqueta aguanta diez lavados a 8 SPI y treinta a 12. Densidades por punto de fijación, tres fallos y los ensayos de taller.",
            "ja": "同じ洗濯表示ラベルでも、8 SPI と 12 SPI では10回と30回の差が出ます。位置別の針数、3つの不具合、サンプル室の試験方法。",
            "ko": "같은 취급 표시 라벨도 8 SPI와 12 SPI에서 열 번과 서른 번으로 갈립니다. 위치별 바늘 수, 세 가지 불량, 샘플실 시험법.",
            "de": "Dasselbe Pflegeetikett hält bei 8 SPI zehn Wäschen, bei 12 SPI dreißig. Werte je Befestigungspunkt, drei Fehlerbilder und die Prüfungen.",
            "pt": "A mesma etiqueta dura dez lavagens a 8 SPI e trinta a 12. Valores por ponto de fixação, três defeitos e os ensaios na sala de amostras.",
        },
    ),
    dict(
        slug="reusable-returnable-garment-packaging.html",
        body="blog/_body_reusable.html",
        title={
            "zh": "可重複使用與可寄回的服裝包裝：規格、標籤與往返次數 | TAIGE",
            "en": "Reusable &amp; Returnable Garment Packaging: Spec Guide 2026 | TAIGE",
            "fr": "Emballage textile réutilisable : spécifications 2026 | TAIGE",
            "es": "Embalaje textil reutilizable y retornable: guía 2026 | TAIGE",
            "ja": "再利用・返却型の衣料包装：2026年の仕様ガイド | TAIGE",
            "ko": "재사용·반납형 의류 포장: 2026 사양 가이드 | TAIGE",
            "de": "Mehrweg-Verpackung für Bekleidung: Spezifikationsleitfaden 2026 | TAIGE",
            "pt": "Embalagem têxtil reutilizável e retornável: guia 2026 | TAIGE",
        },
        desc={
            "zh": "可寄回袋不是環保版快遞袋：20–50 趟、洗滌、追蹤與回程都要算進規格。講清三種模式的取捨、布料與封口參數、標籤義務與損益平衡點。東莞泰閣包裝。",
            "en": "Reusable and returnable garment packaging: material spec, closure choice, label duties and the trip count that makes break-even work for e-commerce.",
            "fr": "Emballage réutilisable : spécification matière, choix de fermeture, obligations d’étiquetage et nombre de rotations pour atteindre l’équilibre.",
            "es": "Embalaje reutilizable: especificación de material, cierre, obligaciones de etiquetado y el número de viajes para alcanzar el equilibrio.",
            "ja": "再利用・返却型の衣料包装：材料規格、開閉部の選定、ラベルの義務、採算が合う往復回数を整理します。",
            "ko": "재사용·반납형 의류 포장: 소재 사양, 여밈 선택, 라벨 의무, 손익분기 왕복 횟수를 정리했습니다.",
            "de": "Mehrweg- und Rücksendeverpackung für Bekleidung: Materialspezifikation, Verschlusswahl, Etikettenpflichten und die nötige Umlaufzahl.",
            "pt": "Embalagem retornável para e-commerce: especificação de material, fechamento, obrigações de rotulagem e o número de viagens do ponto de equilíbrio.",
        },
        crumb={
            "zh": "可重用包裝", "en": "Reusable Packaging", "fr": "Emballage réutilisable",
            "es": "Embalaje reutilizable", "ja": "再利用包装", "ko": "재사용 포장",
            "de": "Mehrwegverpackung", "pt": "Embalagem reutilizável",
        },
        h1={
            "zh": "可重複使用與可寄回的服裝包裝：規格、標籤與往返次數",
            "en": "Reusable and Returnable Garment Packaging: A 2026 Specification Guide",
            "fr": "Emballage textile réutilisable et consigné : guide de spécification 2026",
            "es": "Embalaje textil reutilizable y retornable: guía de especificación 2026",
            "ja": "再利用・返却型の衣料包装：2026年の仕様ガイド",
            "ko": "재사용·반납형 의류 포장: 2026 사양 가이드",
            "de": "Mehrweg- und Rücksende-Verpackung für Bekleidung: Spezifikationsleitfaden 2026",
            "pt": "Embalagem têxtil reutilizável e retornável: guia de especificação 2026",
        },
        meta={
            "zh": "泰閣包裝 · 更新於 " + DATE_ZH,
            "en": "By TAIGE Packaging &nbsp;·&nbsp; Updated November 10, 2026",
            "fr": "Par TAIGE Packaging &nbsp;·&nbsp; Mis à jour le 10 novembre 2026",
            "es": "Por TAIGE Packaging &nbsp;·&nbsp; Actualizado el 10 de noviembre de 2026",
            "ja": "泰閣包装 · 2026年11月10日更新",
            "ko": "TAIGE 패키징 · 2026년 11월 10일 업데이트",
            "de": "Von TAIGE Packaging &nbsp;·&nbsp; Aktualisiert am 10. November 2026",
            "pt": "Por TAIGE Packaging &nbsp;·&nbsp; Atualizado em 10 de novembro de 2026",
        },
        card_tag={
            "zh": "包裝", "en": "Packaging", "fr": "Emballage", "es": "Embalaje",
            "ja": "包装", "ko": "포장", "de": "Verpackung", "pt": "Embalagem",
        },
        card_sum={
            "zh": "可寄回袋不是環保版快遞袋：20–50 趟、洗滌、追蹤、回程都要算。三種模式取捨、材料與封口規格、標籤義務與損益平衡點。",
            "en": "A returnable mailer is a system, not a greener poly bag: 20–50 trips, washing, tracking and a return leg. Three models, material specs and break-even.",
            "fr": "Un sac consigné est un système, pas un polybag plus vert : 20–50 rotations, lavage, traçabilité et retour. Trois modèles, matière et seuil de rentabilité.",
            "es": "Una bolsa retornable es un sistema, no una bolsa verde: 20–50 viajes, lavado, rastreo y retorno. Tres modelos, materiales y punto de equilibrio.",
            "ja": "返却袋は「環境に優しいポリ袋」ではなく仕組みです。20〜50往復、洗濯、追跡、復路まで含めた3モデル・材料仕様・損益分岐を整理。",
            "ko": "반납 백은 친환경 비닐봉투가 아니라 시스템입니다. 20~50회 왕복, 세탁, 추적, 복편까지 포함한 세 모델·소재 사양·손익분기.",
            "de": "Ein Mehrwegbeutel ist ein System, keine grünere Polybeutel-Folie: 20–50 Umläufe, Wäsche, Tracking, Rückweg. Drei Modelle, Materialspezifikation, Schwelle.",
            "pt": "O envelope retornável é um sistema, não um saco verde: 20–50 viagens, lavagem, rastreio e retorno. Três modelos, materiais e ponto de equilíbrio.",
        },
    ),
]

LANGS = ["zh", "en", "fr", "es", "ja", "ko", "de", "pt"]
HL = {"zh": "zh-Hant", "en": "en", "fr": "fr", "es": "es", "ja": "ja", "ko": "ko", "de": "de", "pt": "pt-BR"}

skel = open(SKEL, encoding="utf-8").read()

# 撞车安全闸
for a in ARTICLES:
    for l in LANGS:
        p = ("blog/%s" % a["slug"]) if l == "zh" else ("%s/blog/%s" % (l, a["slug"]))
        if os.path.exists(p):
            raise SystemExit("选题撞车：%s 已存在" % p)
    if ('/blog/%s</loc>' % a["slug"]) in open("sitemap.xml", encoding="utf-8").read():
        raise SystemExit("选题撞车：sitemap 已含 %s" % a["slug"])
print("选题全新，开始生成")

def esc(s):
    """属性值内的双引号必须转义；正文里用弯引号，这里只兜底。"""
    return s.replace('"', "&quot;")

for a in ARTICLES:
    slug = a["slug"]
    s = skel

    # 1) title（8 语属性 + 中文静态文本）
    t = a["title"]
    attrs = " ".join('data-%s="%s"' % (l, esc(t[l])) for l in LANGS)
    s = re.sub(r'<title[^>]*>.*?</title>',
               '<title %s>%s</title>' % (attrs, t["zh"]), s, count=1, flags=re.S)

    # 2) meta description（8 语属性 + content=中文）
    d = a["desc"]
    attr_lines = "\n      ".join('data-%s="%s"' % (l, esc(d[l])) for l in LANGS)
    desc_block = '<meta name="description" %s\n      content="%s">' % (attr_lines, esc(d["zh"]))
    s = re.sub(r'<meta name="description"[^>]*>', desc_block, s, count=1, flags=re.S)

    # 3) canonical + hreflang（9 条）
    lines = ['<link rel="canonical" href="https://taigetag.com/blog/%s">' % slug]
    for l in LANGS:
        url = "https://taigetag.com/blog/%s" % slug if l == "zh" else "https://taigetag.com/%s/blog/%s" % (l, slug)
        lines.append('<link rel="alternate" hreflang="%s" href="%s">' % (HL[l], url))
    lines.append('<link rel="alternate" hreflang="x-default" href="https://taigetag.com/blog/%s">' % slug)
    s, n = re.subn(r'<link rel="canonical"[^>]*>\s*(?:<link rel="alternate"[^\n]*>\s*)+',
                   "\n".join(lines) + "\n", s, count=1)
    assert n == 1, "hreflang 块替换失败"

    # 4) crumb
    c = a["crumb"]
    crumb = ('<div class="crumb"><a href="../index.html" data-zh="首頁" data-en="Home" data-fr="Accueil" data-es="Inicio" data-ja="ホーム" data-ko="홈" data-de="Startseite" data-pt="Início">首頁</a>'
             ' / <a href="index.html" data-zh="輔料 FAQ" data-en="Trims FAQ" data-fr="FAQ Accessoires" data-es="FAQ Accesorios" data-ja="副資材 FAQ" data-ko="부자재 FAQ" data-de="Accessoires-FAQ" data-pt="FAQ de aviamentos">輔料 FAQ</a>'
             ' / <span %s>%s</span></div>'
             % (" ".join('data-%s="%s"' % (l, esc(c[l])) for l in LANGS), c["zh"]))
    s, n = re.subn(r'<div class="crumb">.*?</div>', crumb, s, count=1, flags=re.S)
    assert n == 1, "crumb 替换失败"

    # 5) h1
    h = a["h1"]
    h1 = '<h1 %s>%s</h1>' % (" ".join('data-%s="%s"' % (l, esc(h[l])) for l in LANGS), h["zh"])
    s, n = re.subn(r'<h1 [^>]*>.*?</h1>', h1, s, count=1, flags=re.S)
    assert n == 1, "h1 替换失败"

    # 6) 日期行
    m = a["meta"]
    meta = '<p %s>%s</p>' % (" ".join('data-%s="%s"' % (l, esc(m[l])) for l in LANGS), m["zh"])
    s, n = re.subn(r'<p data-zh="泰閣包裝 · 更新於[^"]*"[^>]*>.*?</p>', meta, s, count=1, flags=re.S)
    assert n == 1, "meta 行替换失败"

    # 7) JSON-LD：旧 slug / 旧 h1 名
    s = s.replace(OLD_SLUG, slug)
    s = s.replace(OLD_H1, h["zh"])
    assert s.count('"headline": "%s"' % h["zh"]) == 1, "headline 替换失败"

    # 8) 正文（含 section 骨架与闭合标签）
    body = open(a["body"], encoding="utf-8").read().rstrip("\n")
    s, n = re.subn(r'  <section class="article-body">.*?</main>', body, s, count=1, flags=re.S)
    assert n == 1, "正文替换失败"

    out = "blog/%s" % slug
    with open(out, "w", encoding="utf-8", newline="") as f:
        f.write(s)
    print("写入 %s  %.1f KB  desc=zh%d en%d fr%d es%d ja%d ko%d de%d pt%d 字符"
          % (out, len(s.encode("utf-8")) / 1024,
             *[len(d[l]) for l in LANGS]))

# ---------- blog/index.html 卡片 ----------
CARD = '''      <article class="post-card">
        <span class="tag" %(tag_attrs)s>%(tag_zh)s</span>
        <h3 %(h3_attrs)s>%(h3_zh)s</h3>
        <p %(sum_attrs)s>%(sum_zh)s</p>
        <a class="more" href="%(slug)s" data-zh="閱讀全文 →" data-en="Read more →" data-fr="Lire la suite →" data-es="Leer más →" data-ja="続きを読む →" data-ko="자세히 보기 →" data-de="Weiterlesen →" data-pt="Ler mais →">閱讀全文 →</a>
      </article>

'''

def attr(lang_map):
    return " ".join('data-%s="%s"' % (l, esc(lang_map[l])) for l in LANGS)

cards = ""
for a in ARTICLES:
    cards += CARD % dict(
        tag_attrs=attr(a["card_tag"]), tag_zh=a["card_tag"]["zh"],
        h3_attrs=attr(a["h1"]), h3_zh=a["h1"]["zh"],
        sum_attrs=attr(a["card_sum"]), sum_zh=a["card_sum"]["zh"],
        slug=a["slug"],
    )

idx = "blog/index.html"
s = open(idx, encoding="utf-8").read()
marker = '<div class="post-grid">\n'
assert marker in s, "post-grid 未找到"
for a in ARTICLES:
    assert a["slug"] not in s, "卡已存在：%s" % a["slug"]
s = s.replace(marker, marker + "\n" + cards, 1)
with open(idx, "w", encoding="utf-8", newline="") as f:
    f.write(s)
print("blog/index.html 插入 %d 张卡片" % len(ARTICLES))
