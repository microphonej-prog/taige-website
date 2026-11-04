#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-11-04 08:00 批次（六语：zh-Hant 根 / en / ja / ko / fr / es）
- 辅料近岸采购：产能外移后的供应对齐（apparel-trims-nearshoring-sourcing-guide）
- 电商开箱体验设计：五个触点与三档预算（apparel-unboxing-packaging-design-guide）

用法: F:/hermes/venvs/tools/Scripts/python.exe daily_gen_20261104_0800.py [--check]
"""
import os, re, sys, subprocess, importlib.util

ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)
PY = sys.executable

SKEL = "blog/knitwear-sweater-trims-guide.html"
DATE_ZH = "2026年11月4日"
DATE_EN = "November 4, 2026"
DATE_JA = "2026年11月4日"
DATE_KO = "2026년 11월 4일 업데이트"
DATE_FR = "4 novembre 2026"
DATE_ES = "4 de noviembre de 2026"
SITEMAP_DATE = "2026-11-04"
BUST_OLD, BUST_NEW = "196", "197"
LANGS = ["en", "ja", "ko", "fr", "es"]

ARTICLES = [
    dict(
        slug="apparel-trims-nearshoring-sourcing-guide.html",
        body="blog/_body_nearshore.html",
        title_zh="服装辅料近岸采购：产能外移后如何稳住辅料供应 | TAGE",
        title_en="Nearshoring Apparel Trims: Keeping Supply Stable | TAGE",
        title_ja="衣料副資材のニアショア調達：生産移管後も供給を安定させる | TAGE",
        title_ko="의류 부자재 니어쇼어링: 생산 이전 후 공급 안정화 | TAGE",
        title_fr="Accessoires et nearshoring : sécuriser l'approvisionnement | TAGE",
        title_es="Accesorios de moda y nearshoring: asegurar el suministro | TAGE",
        desc_zh="服装辅料近岸采购指南：成衣产能外移后，辅料仍集中在珠三角与长三角。讲清时间、规格、模具、颜色四个断点，集中采购加前置集拼、关键件双源、辅料包前置三种组织方式，交期缓冲的算法，原产地与关税要点，附六项落地清单。来自东莞泰阁包装。",
        desc_en="Nearshoring moved the garment, not the trim. Four break points, three supply models, a lead-time buffer formula, duty and origin, and a six-point checklist.",
        desc_ja="ニアショア化で服は動いても副資材は動かない。時間・仕様・型・色の4つの断絶点、集中購買＋事前混載・重要品のデュアルソース・キット化の3方式、緩衝日数の計算式、原産地と関税、6項目のチェックリスト。東莞泰閣包装。",
        desc_ko="니어쇼어링으로 의류는 옮겨졌지만 부자재는 그대로입니다. 시간·사양·금형·색상 네 가지 단절 지점, 세 가지 공급 방식, 리드타임 버퍼 계산식, 원산지와 관세, 여섯 항목 체크리스트. 둥관 TAGE 패키징.",
        desc_fr="Le nearshoring a déplacé le vêtement, pas l'accessoire. Quatre points de rupture, trois modèles d'approvisionnement, une formule de tampon, codes SH et origine, six points de contrôle.",
        desc_es="El nearshoring movió la prenda, no el accesorio. Cuatro puntos de fallo, tres modelos de suministro, una fórmula de colchón, códigos HS y origen, y seis puntos de control.",
        crumb_zh="近岸采购与辅料供应",
        crumb_en="Nearshoring and Trim Supply",
        crumb_ja="ニアショア調達と副資材供給",
        crumb_ko="니어쇼어링과 부자재 공급",
        crumb_fr="Nearshoring et accessoires",
        crumb_es="Nearshoring y accesorios",
        h1_zh="服装辅料近岸采购：产能外移后如何稳住辅料供应",
        h1_en="Nearshoring Apparel Trims: Keeping Trim Supply Stable After the Move",
        h1_ja="衣料副資材のニアショア調達：生産移管後も供給を安定させる方法",
        h1_ko="의류 부자재 니어쇼어링: 생산 이전 후 공급을 안정시키는 방법",
        h1_fr="Accessoires et nearshoring : sécuriser l'approvisionnement après le transfert",
        h1_es="Accesorios de moda y nearshoring: asegurar el suministro tras el traslado",
        tag_zh="供应链", tag_en="Supply Chain", tag_ja="サプライチェーン", tag_ko="공급망",
        tag_fr="Chaîne d'approvisionnement", tag_es="Cadena de suministro",
        sum_zh="成衣产能搬到了越南、土耳其、墨西哥，辅料却仍然集中在珠三角与长三角。这篇讲清四个断点（时间、规格、模具、颜色）、三种可执行的组织方式（集中采购加前置集拼、关键件双源、辅料包前置）、交期缓冲的计算公式、原产地与关税要点，最后给一张能直接抄进采购手册的六项清单。",
        sum_en="Sewing moved to Vietnam, Turkey or Mexico; the trims stayed in the Pearl River and Yangtze deltas. Four break points — time, specification, tooling and colour — three workable models, a buffer formula you can apply today, the origin and duty points, and a six-item checklist for the purchasing manual.",
        sum_ja="縫製はベトナム、トルコ、メキシコへ移り、副資材は珠江・長江デルタに残ったまま。時間・仕様・型・色という4つの断絶点、実行可能な3つの方式（集中購買＋事前混載、重要品のデュアルソース、キット化）、今日から使える緩衝日数の式、原産地と関税の要点、購買マニュアルに貼れる6項目のチェックリストをまとめました。",
        sum_ko="봉제는 베트남·터키·멕시코로 옮겨졌지만 부자재는 주강·양쯔강 델타에 남아 있습니다. 시간·사양·금형·색상 네 가지 단절 지점, 실행 가능한 세 가지 방식(중앙 구매+사전 혼재, 핵심 품목 이중 공급, 키트 사전 구성), 바로 쓸 수 있는 버퍼 계산식, 원산지와 관세 요점, 구매 매뉴얼에 넣을 여섯 항목 체크리스트를 정리했습니다.",
        sum_fr="La confection est partie au Vietnam, en Turquie ou au Mexique ; les accessoires sont restés dans les deltas. Quatre points de rupture — temps, spécification, outillage, couleur —, trois modèles applicables, une formule de tampon utilisable tout de suite, les points d'origine et de douane, et six points à recopier dans le manuel achats.",
        sum_es="La confección se trasladó a Vietnam, Turquía o México; los accesorios se quedaron en los deltas. Cuatro puntos de fallo —tiempo, especificación, utillaje y color—, tres modelos aplicables, una fórmula de colchón que se puede usar hoy, los puntos de origen y arancel, y seis puntos para el manual de compras.",
    ),
    dict(
        slug="apparel-unboxing-packaging-design-guide.html",
        body="blog/_body_unboxing.html",
        title_zh="服装电商开箱体验设计：五个触点与三档预算 | TAGE",
        title_en="Apparel Unboxing Experience: Design from First Touch | TAGE",
        title_ja="アパレルECの開封体験デザイン：5つの接点と3段階の予算 | TAGE",
        title_ko="의류 이커머스 언박싱 디자인: 다섯 접점과 세 단계 예산 | TAGE",
        title_fr="Expérience d'ouverture en mode : cinq contacts, trois budgets | TAGE",
        title_es="Experiencia de unboxing en moda: cinco contactos y tres presupuestos | TAGE",
        desc_zh="服装电商开箱体验怎么设计：外袋封口、内层包装袋、吊牌主唛、内衬卡薄纸、售后卡五个触点的顺序，每件 1 元、3–5 元、8 元以上三档预算怎么配，让顾客愿意拍的四个做法，吊牌挂法对第一触感的影响，以及欧盟减量与退货复原。来自东莞泰阁包装。",
        desc_en="Apparel unboxing design: five touchpoints in order, three budget tiers, four ways to make customers film it, how tag attachment changes feel, and returns.",
        desc_ja="アパレルECの開封体験設計：外袋・内袋・タグ・カード・アフターカードの5接点の順序、1元／3〜5元／8元以上の3段階の予算、撮影したくなる4つの工夫、タグの取り付け方が第一触感に与える差、EUの減量と返品再梱包。東莞泰閣包装。",
        desc_ko="의류 이커머스 언박싱 설계: 겉봉투·내부 봉투·행택·카드·사후 카드 다섯 접점의 순서, 1위안/3~5위안/8위안 이상 세 단계 예산, 촬영하고 싶게 만드는 네 가지, 행택 부착 방식이 첫 촉감에 주는 차이, EU 감량과 반품 재포장. 둥관 TAGE 패키징.",
        desc_fr="Design d'unboxing : cinq points de contact dans l'ordre, trois paliers de budget, quatre leviers pour donner envie de filmer, l'effet de la fixation d'étiquette, retours et réduction.",
        desc_es="Diseño de unboxing: cinco puntos de contacto en orden, tres niveles de presupuesto, cuatro palancas para que el cliente grabe, el efecto de la sujeción y las devoluciones.",
        crumb_zh="开箱体验设计",
        crumb_en="Unboxing Design",
        crumb_ja="開封体験の設計",
        crumb_ko="언박싱 디자인",
        crumb_fr="Design d'ouverture",
        crumb_es="Diseño de unboxing",
        h1_zh="服装电商开箱体验设计：五个触点与三档预算",
        h1_en="Apparel Unboxing Experience: Five Touchpoints and Three Budget Tiers",
        h1_ja="アパレルECの開封体験デザイン：5つの接点と3段階の予算",
        h1_ko="의류 이커머스 언박싱 디자인: 다섯 접점과 세 단계 예산",
        h1_fr="Expérience d'ouverture en mode : cinq points de contact et trois paliers de budget",
        h1_es="Experiencia de unboxing en moda: cinco puntos de contacto y tres niveles de presupuesto",
        tag_zh="包装方案", tag_en="Packaging", tag_ja="包装設計", tag_ko="포장 설계",
        tag_fr="Emballage", tag_es="Embalaje",
        sum_zh="顾客拆开快递只给品牌三秒钟。这篇把开箱拆成五个触点（外袋封口、内层袋、吊牌主唛、内衬卡薄纸、售后卡），给出每件 1 元以内、3–5 元、8 元以上三档预算的配法，讲让顾客愿意拍的四个做法、挂法如何改变第一触感，以及欧盟减量与退货复原这两个最容易被漏算的环节。",
        sum_en="The customer gives the brand three seconds. This guide splits unboxing into five touchpoints — outer bag and seal, inner bag, tag and neck label, insert and tissue, after-sales card — then sets out three budget tiers, four ways to earn a video, how attachment changes first feel, and the two costs e-commerce forgets: EU-driven reduction and re-packable returns.",
        sum_ja="顧客がブランドに与えるのは3秒。開封を5つの接点（外袋と封、内袋、タグとメインラベル、カードと薄葉紙、アフターカード）に分け、1元未満／3〜5元／8元以上の3段階の組み方、撮影したくなる4つの工夫、取り付け方で変わる第一触感、そしてEUの減量と返品再梱包という見落としやすい2つのコストを整理します。",
        sum_ko="고객이 브랜드에 주는 시간은 3초입니다. 언박싱을 다섯 접점(겉봉투와 봉인, 내부 봉투, 행택과 메인 라벨, 카드와 박엽지, 사후 카드)으로 나누고, 1위안 이내·3~5위안·8위안 이상 세 단계 구성, 촬영하고 싶게 만드는 네 가지, 부착 방식이 바꾸는 첫 촉감, 그리고 이커머스가 놓치는 두 비용(EU 감량과 반품 재포장)을 정리합니다.",
        sum_fr="Le client accorde trois secondes à la marque. Ce guide découpe l'ouverture en cinq points de contact — sac et sceau, sachet intérieur, étiquette et label de col, carte et papier de soie, carte SAV —, propose trois paliers de budget, quatre leviers pour mériter une vidéo, l'effet de la fixation, et les deux coûts oubliés : réduction européenne et retours reconditionnables.",
        sum_es="El cliente concede tres segundos a la marca. Esta guía divide el unboxing en cinco puntos de contacto —bolsa y precinto, bolsa interior, etiqueta y cuello, tarjeta y papel de seda, tarjeta posventa—, plantea tres niveles de presupuesto, cuatro palancas para ganarse un vídeo, el efecto de la sujeción y los dos costes que se olvidan: reducción europea y retornos reempaquetables.",
    ),
]

skel = open(SKEL, encoding="utf-8").read()
old3 = re.search(r'"position": 3,\s*"name": "([^"]*)"', skel).group(1)
print("骨架 breadcrumb 名:", old3)

# ---------------- 撞车安全闸 ----------------
for a in ARTICLES:
    if not os.path.exists(a["body"]):
        raise SystemExit("正文文件缺失：%s" % a["body"])
    for p in ["blog/%s" % a["slug"]] + ["%s/blog/%s" % (l, a["slug"]) for l in LANGS]:
        if os.path.exists(p):
            raise SystemExit("选题撞车：%s 已存在，换选题！" % p)
sm0 = open("sitemap.xml", encoding="utf-8").read()
for a in ARTICLES:
    if ("/blog/%s</loc>" % a["slug"]) in sm0:
        raise SystemExit("选题撞车：sitemap 已含 %s" % a["slug"])
print("选题全新，开始生成")

for a in ARTICLES:
    print("  %-46s desc_zh=%d字 desc_en=%d字符 desc_ja=%d desc_ko=%d desc_fr=%d desc_es=%d"
          % (a["slug"], len(a["desc_zh"]), len(a["desc_en"]), len(a["desc_ja"]),
             len(a["desc_ko"]), len(a["desc_fr"]), len(a["desc_es"])))
if "--check" in sys.argv:
    sys.exit(0)

# ---------------- 1) 生成两篇文章（六语属性） ----------------
for a in ARTICLES:
    slug = a["slug"]
    s = skel.replace(SKEL.replace("blog/", ""), slug)

    title_line = ('<title data-zh="%s" data-en="%s" data-ja="%s" data-ko="%s" data-fr="%s" data-es="%s">%s</title>'
                  % (a["title_zh"], a["title_en"], a["title_ja"], a["title_ko"],
                     a["title_fr"], a["title_es"], a["title_zh"]))
    s = re.sub(r'<title[^>]*>.*?</title>', title_line, s, count=1, flags=re.S)

    s = re.sub(r'<meta name="description".*?content="[^"]*">', 'DESC_PLACEHOLDER', s, count=1, flags=re.S)
    desc_block = ('<meta name="description" data-zh="%s"\n'
                  '      data-en="%s" data-ja="%s" data-ko="%s"\n'
                  '      data-fr="%s"\n'
                  '      data-es="%s"\n'
                  '      content="%s">' % (a["desc_zh"], a["desc_en"], a["desc_ja"], a["desc_ko"],
                                           a["desc_fr"], a["desc_es"], a["desc_zh"]))
    s = s.replace('DESC_PLACEHOLDER', desc_block, 1)

    new_canon = ('<link rel="canonical" href="https://taigetag.com/blog/%s">\n'
                 '<link rel="alternate" hreflang="zh-Hant" href="https://taigetag.com/blog/%s">\n'
                 '<link rel="alternate" hreflang="en" href="https://taigetag.com/en/blog/%s">\n'
                 '<link rel="alternate" hreflang="fr" href="https://taigetag.com/fr/blog/%s">\n'
                 '<link rel="alternate" hreflang="es" href="https://taigetag.com/es/blog/%s">\n'
                 '<link rel="alternate" hreflang="ja" href="https://taigetag.com/ja/blog/%s">\n'
                 '<link rel="alternate" hreflang="ko" href="https://taigetag.com/ko/blog/%s">\n'
                 '<link rel="alternate" hreflang="x-default" href="https://taigetag.com/blog/%s">'
                 % ((slug,) * 8))
    s, n_href = re.subn(r'<link rel="canonical" href="[^"]*">(?:\n<link rel="alternate"[^\n]*>)+',
                        new_canon, s, count=1)
    assert n_href == 1, "hreflang 替换失败"

    crumb = ('<div class="crumb"><a href="../index.html" data-zh="首頁" data-fr="Accueil" data-es="Inicio" data-en="Home" data-ja="ホーム" data-ko="홈">首頁</a>'
             ' / <a href="index.html" data-zh="輔料 FAQ" data-fr="FAQ Accessoires" data-es="FAQ Accesorios" data-en="Trims FAQ" data-ja="副資材 FAQ" data-ko="부자재 FAQ">輔料 FAQ</a>'
             ' / <span data-zh="%s" data-en="%s" data-ja="%s" data-ko="%s" data-fr="%s" data-es="%s">%s</span></div>'
             % (a["crumb_zh"], a["crumb_en"], a["crumb_ja"], a["crumb_ko"],
                a["crumb_fr"], a["crumb_es"], a["crumb_zh"]))
    s, n = re.subn(r'<div class="crumb">.*?</div>', crumb, s, count=1, flags=re.S)
    assert n == 1, "crumb 替换失败"

    h1 = ('<h1 data-zh="%s" data-en="%s" data-ja="%s" data-ko="%s" data-fr="%s" data-es="%s">%s</h1>'
          % (a["h1_zh"], a["h1_en"], a["h1_ja"], a["h1_ko"], a["h1_fr"], a["h1_es"], a["h1_zh"]))
    s, n = re.subn(r'<h1 .*?</h1>', h1, s, count=1, flags=re.S)
    assert n == 1, "h1 替换失败"

    meta = ('<p data-zh="泰閣包裝 · 更新於 %s" data-en="By TAGE Packaging &nbsp;·&nbsp; Updated %s" '
            'data-ja="泰閣包装 · %s更新" data-ko="TAGE 패키징 · %s" '
            'data-fr="Par TAGE Packaging &nbsp;·&nbsp; Mis à jour le %s" '
            'data-es="Por TAGE Packaging &nbsp;·&nbsp; Actualizado el %s">泰閣包裝 · 更新於 %s</p>'
            % (DATE_ZH, DATE_EN, DATE_JA, DATE_KO, DATE_FR, DATE_ES, DATE_ZH))
    s, n = re.subn(r'<p data-zh="泰[阁閣]包[装裝] · 更新[于於][^"]*".*?</p>', meta, s, count=1, flags=re.S)
    assert n == 1, "meta 行替换失败"

    s = s.replace('"%s"' % old3, '"%s"' % a["h1_zh"])
    s, n = re.subn(r'"headline": "[^"]*"', '"headline": "%s"' % a["h1_zh"], s, count=1)
    assert n == 1, "headline 替换失败"

    body = open(a["body"], encoding="utf-8").read().rstrip("\n")
    i0 = s.index('  <section class="article-body">')
    i1 = s.index('\n</main>')
    s = s[:i0] + body + s[i1:]

    out = "blog/%s" % slug
    open(out, "w", encoding="utf-8", newline="").write(s)
    print("写入 %s (%d KB)" % (out, len(s.encode("utf-8")) // 1024))

# ---------------- 2) blog/index.html 顶部插入两张卡片 ----------------
CARD = '''      <article class="post-card">
        <span class="tag" data-zh="{tag_zh}" data-en="{tag_en}" data-ja="{tag_ja}" data-ko="{tag_ko}" data-fr="{tag_fr}" data-es="{tag_es}">{tag_zh}</span>
        <h3 data-zh="{h3_zh}" data-en="{h3_en}" data-ja="{h3_ja}" data-ko="{h3_ko}" data-fr="{h3_fr}" data-es="{h3_es}">{h3_zh}</h3>
        <p data-zh="{sum_zh}" data-en="{sum_en}" data-ja="{sum_ja}" data-ko="{sum_ko}" data-fr="{sum_fr}" data-es="{sum_es}">{sum_zh}</p>
        <a class="more" href="{slug}" data-zh="閱讀全文 →" data-en="Read more →" data-ja="続きを読む →" data-ko="자세히 보기 →" data-fr="Lire la suite →" data-es="Leer más →">閱讀全文 →</a>
      </article>
'''

cards = ""
for a in ARTICLES:
    cards += CARD.format(
        tag_zh=a["tag_zh"], tag_en=a["tag_en"], tag_ja=a["tag_ja"], tag_ko=a["tag_ko"],
        tag_fr=a["tag_fr"], tag_es=a["tag_es"],
        h3_zh=a["h1_zh"], h3_en=a["h1_en"], h3_ja=a["h1_ja"], h3_ko=a["h1_ko"],
        h3_fr=a["h1_fr"], h3_es=a["h1_es"],
        sum_zh=a["sum_zh"], sum_en=a["sum_en"], sum_ja=a["sum_ja"], sum_ko=a["sum_ko"],
        sum_fr=a["sum_fr"], sum_es=a["sum_es"],
        slug=a["slug"])

idx = "blog/index.html"
s = open(idx, encoding="utf-8").read()
marker = '<div class="post-grid">\n'
assert marker in s, "post-grid 未找到"
for a in ARTICLES:
    assert a["slug"] not in s, "卡已存在：%s" % a["slug"]
s = s.replace(marker, marker + "\n" + cards, 1)
open(idx, "w", encoding="utf-8", newline="").write(s)
print("blog/index.html 插入 2 张卡片完成")

# ---------------- 3) 简体 → 繁体（幂等） ----------------
spec = importlib.util.spec_from_file_location("to_traditional", os.path.join(ROOT, "to_traditional.py"))
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
changed = []
for p in ["blog/%s" % a["slug"] for a in ARTICLES] + [idx]:
    s0 = open(p, encoding="utf-8").read()
    s1 = mod.convert_html(s0)
    if s1 != s0:
        open(p, "w", encoding="utf-8", newline="").write(s1)
        changed.append(os.path.basename(p))
print("繁体转换改动: %d %s" % (len(changed), changed))

# ---------------- 4) gen_i18n 生成五语版本 ----------------
TARGETS = ["blog/%s" % a["slug"] for a in ARTICLES] + [idx]
for lang in LANGS:
    r = subprocess.run([PY, "gen_i18n.py", lang] + TARGETS, capture_output=True, text=True, encoding="utf-8")
    if r.returncode != 0:
        print(r.stdout[-3000:], r.stderr[-3000:])
        raise SystemExit("gen_i18n %s 失败" % lang)
    print("gen_i18n %s -> %d 文件 ok" % (lang, len(TARGETS)))

# ---------------- 5) sitemap ----------------


def block(url):
    return ("  <url>\r\n    <loc>%s</loc>\r\n    <lastmod>%s</lastmod>\r\n"
            "    <changefreq>monthly</changefreq>\r\n    <priority>0.7</priority>\r\n  </url>\r\n"
            % (url, SITEMAP_DATE))


sm = open("sitemap.xml", encoding="utf-8", newline="").read()
before = sm.count("<loc>")
blocks = []
for a in ARTICLES:
    slug = a["slug"]
    for u in ["https://taigetag.com/blog/%s" % slug] + \
             ["https://taigetag.com/%s/blog/%s" % (l, slug) for l in LANGS]:
        assert "<loc>%s</loc>" % u not in sm, "sitemap 已有 %s" % u
        blocks.append(block(u))
sm = sm.replace("</urlset>", "".join(blocks) + "</urlset>", 1)

for u in ["https://taigetag.com/blog/index.html"] + \
         ["https://taigetag.com/%s/blog/index.html" % l for l in LANGS]:
    pat = re.compile(r'(<loc>%s</loc>\r?\n\s*<lastmod>)[^<]*(</lastmod>)' % re.escape(u))
    sm, n = pat.subn(r'\g<1>%s\g<2>' % SITEMAP_DATE, sm, count=1)
    assert n == 1, "blog index lastmod 未更新: %s" % u

open("sitemap.xml", "w", encoding="utf-8", newline="").write(sm)
print("sitemap 新增 %d 个 URL，<loc> %d -> %d" % (len(blocks), before, sm.count("<loc>")))

# ---------------- 6) BUST_VERSION 升级 ----------------
mj = open("js/main.js", encoding="utf-8").read()
assert 'var BUST_VERSION = "%s";' % BUST_OLD in mj, "BUST_VERSION 不是 %s" % BUST_OLD
mj = mj.replace('var BUST_VERSION = "%s";' % BUST_OLD, 'var BUST_VERSION = "%s";' % BUST_NEW, 1)
open("js/main.js", "w", encoding="utf-8", newline="").write(mj)
print("BUST_VERSION %s -> %s" % (BUST_OLD, BUST_NEW))
