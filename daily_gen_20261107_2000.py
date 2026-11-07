#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-11-07 20:00 批次（六语：zh-Hant 根 / en / ja / ko / fr / es）
- 防尘袋与成衣罩（dust-bag-garment-cover-guide）
- 吊牌悬挂位置（hang-tag-hanging-position-guide）

用法: F:/hermes/venvs/tools/Scripts/python.exe daily_gen_20261107_2000.py [--check]
"""
import os, re, sys, subprocess, importlib.util

ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)
PY = sys.executable

SKEL = "blog/knitwear-sweater-trims-guide.html"
DATE_ZH = "2026年11月7日"
DATE_EN = "November 7, 2026"
DATE_JA = "2026年11月7日"
DATE_KO = "2026년 11월 7일 업데이트"
DATE_FR = "7 novembre 2026"
DATE_ES = "7 de noviembre de 2026"
SITEMAP_DATE = "2026-11-07"
BUST_OLD, BUST_NEW = "203", "204"
LANGS = ["en", "ja", "ko", "fr", "es"]

ARTICLES = [
    dict(
        slug="dust-bag-garment-cover-guide.html",
        body="blog/_body_dust.html",
        title_zh="防尘袋与成衣罩：法兰绒、无纺布、PEVA 怎么选 | TAGE",
        title_en="Dust Bags and Garment Covers: Flannel, Nonwoven or PEVA | TAGE",
        title_ja="ドレスカバーと衣類カバー：フランネル・不織布・PEVA の選び方 | TAGE",
        title_ko="더스트백과 의류 커버: 플란넬·부직포·PEVA 선택 | TAGE",
        title_fr="Housses de protection : flanelle, non-tissé ou PEVA | TAGE",
        title_es="Fundas protectoras: franela, non-woven o PEVA | TAGE",
        desc_zh="防尘袋与成衣罩选购指南：法兰绒、PP 无纺布、PEVA、棉帆布在克重、透气、防潮与成本上的差异，抽绳与拉链结构、按衣长反推的尺寸表、丝印与织唛呈现，以及海运霉变与 REACH 验收要点。附打样前六项清单。来自东莞泰阁包装。",
        desc_en="Dust bags and garment covers compared: flannel, PP nonwoven, PEVA and canvas by weight, breathability and cost, plus drawstring build, sizing and export checks.",
        desc_ja="ドレスカバーと衣類カバーの選び方。フランネル・PP 不織布・PEVA・綿キャンバスを目付・通気・防湿・コストで比較し、紐とファスナーの構造、着丈から逆算する寸法表、シルク印刷と織りラベルの見せ方、海上輸送の黴と REACH の検収まで整理します。",
        desc_ko="더스트백과 의류 커버 선택 가이드. 플란넬·PP 부직포·PEVA·코튼 캔버스를 평량, 통기, 방습, 원가로 비교하고 끈·지퍼 구조, 의류 길이에서 역산하는 치수표, 실크 인쇄와 직조 라벨 표현, 해상 운송 곰팡이와 REACH 검수까지 정리합니다.",
        desc_fr="Housses de protection comparées : flanelle, non-tissé PP, PEVA et canvas selon grammage, respirabilité et coût, plus cordon, dimensions et contrôles export.",
        desc_es="Fundas protectoras comparadas: franela, non-woven PP, PEVA y lona por gramaje, transpirabilidad y coste, más cordón, medidas y controles de exportación.",
        crumb_zh="防尘袋与成衣罩",
        crumb_en="Dust Bags and Covers",
        crumb_ja="ドレスカバーとカバー",
        crumb_ko="더스트백과 커버",
        crumb_fr="Housses de protection",
        crumb_es="Fundas protectoras",
        h1_zh="防尘袋与成衣罩：法兰绒、无纺布、PEVA 怎么选",
        h1_en="Dust Bags and Garment Covers: Flannel, Nonwoven or PEVA",
        h1_ja="ドレスカバーと衣類カバー：フランネル・不織布・PEVA の選び方",
        h1_ko="더스트백과 의류 커버: 플란넬·부직포·PEVA 선택 기준",
        h1_fr="Housses de protection : flanelle, non-tissé ou PEVA",
        h1_es="Fundas protectoras: franela, non-woven o PEVA",
        tag_zh="包装指南", tag_en="Packaging Guide", tag_ja="包装ガイド",
        tag_ko="포장 가이드", tag_fr="Guide emballage", tag_es="Guía de embalaje",
        sum_zh="防尘袋常被当成挂装胶袋的布料版来做，结果不是尺寸不合就是抽绳一拉就开线。这篇把防尘袋、挂装袋、手提袋三者的验收逻辑分开，给出四种材质对照、按衣长反推的尺寸表、丝印与织唛的呈现方式，以及海运霉变和 REACH 的五个必检项。",
        sum_en="Dust bags get made as a fabric version of the hanging polybag, and end up short at the hem or split at the drawstring. This separates dust bags, hanging bags and totes by inspection logic, then compares four materials, works sizes back from garment length, and lists five export checks.",
        sum_ja="ドレスカバーは吊り袋の布版として作られ、寸法が合わないか紐がすぐほつれます。ドレスカバー・吊り袋・トートの検収論理を分け、四素材の比較、着丈からの逆算寸法、シルク印刷と織りラベルの見せ方、海上輸送の黴と REACH の五項目を整理します。",
        sum_ko="더스트백은 행잉 폴리백의 원단 버전처럼 만들어져 길이가 맞지 않거나 끈이 터집니다. 더스트백·행잉백·토트의 검수 논리를 나누고, 네 소재 비교, 의류 길이 역산 치수표, 실크 인쇄와 직조 라벨 표현, 해상 곰팡이와 REACH 다섯 항목을 정리합니다.",
        sum_fr="La housse est souvent fabriquée comme un polybag en tissu : trop courte à l'ourlet ou lâche au cordon. On sépare housse, sac suspendu et tote par leur logique de contrôle, puis quatre matières, les dimensions calculées depuis la longueur, et cinq contrôles export.",
        sum_es="La funda se hace como un polybag de tela y acaba corta en el bajo o suelta en el cordón. Separamos funda, bolsa colgante y tote por su lógica de control, comparamos cuatro materiales, calculamos medidas desde el largo y damos cinco controles de exportación.",
    ),
    dict(
        slug="hang-tag-hanging-position-guide.html",
        body="blog/_body_hangpos.html",
        title_zh="吊牌挂在哪里：位置选择、打孔点与陈列规范 | TAGE",
        title_en="Where to Attach a Hang Tag: Position, Hole and Display | TAGE",
        title_ja="値札の取付位置：場所・穴位置・陳列ルール | TAGE",
        title_ko="행택 부착 위치: 자리·구멍·진열 규칙 | TAGE",
        title_fr="Où fixer un carton : position, perçage et présentation | TAGE",
        title_es="Dónde colgar la etiqueta: posición, troquel y exposición | TAGE",
        desc_zh="吊牌挂在哪里，决定顾客第一眼能否读到品牌、试穿会不会扯掉、退货时吊牌还在不在。本文按 T 恤、衬衫、裤装、裙装、外套、泳装、配饰给出首选挂位表，讲清孔位到边距离、重心与鸡眼加固、四样不能遮挡的东西、陈列朝向与防盗扣位置。来自东莞泰阁包装。",
        desc_en="Where a hang tag sits decides whether the brand is read, whether it survives trying on, and whether it is still there at return. Position table and hole rules.",
        desc_ja="値札の取付位置は、最初の一目でブランドが読めるか、試着で切れないか、返品時に残るかを決めます。Tシャツ・シャツ・パンツ・スカート・コート・水着・小物の位置表、穴の端距離と重心、ハトメ補強、隠してはいけない四つ、陳列の向きと防盗タグの位置を整理します。",
        desc_ko="행택 위치는 첫눈에 브랜드가 읽히는지, 입어볼 때 뜯기지 않는지, 반품 시 남아 있는지를 결정합니다. 티셔츠·셔츠·팬츠·스커트·코트·수영복·액세서리별 위치표, 구멍-가장자리 거리와 무게중심, 아일릿 보강, 가리면 안 되는 네 가지, 진열 방향과 도난 방지 태그 위치를 정리합니다.",
        desc_fr="L'emplacement du carton décide si la marque est lue, s'il survit à l'essayage et s'il est encore là au retour. Tableau par catégorie, distance du trou, œillets et présentation.",
        desc_es="La posición del colgante decide si se lee la marca, si sobrevive a la prueba y si sigue en una devolución. Tabla por categoría, distancia del agujero, ojales y exposición.",
        crumb_zh="吊牌悬挂位置",
        crumb_en="Hang Tag Position",
        crumb_ja="値札の取付位置",
        crumb_ko="행택 부착 위치",
        crumb_fr="Position du carton",
        crumb_es="Posición del colgante",
        h1_zh="吊牌挂在哪里：位置选择、打孔点与陈列规范",
        h1_en="Where to Attach a Hang Tag: Position, Hole and Display",
        h1_ja="値札の取付位置：場所・穴位置・陳列ルール",
        h1_ko="행택 부착 위치: 자리·구멍·진열 규칙",
        h1_fr="Où fixer un carton : position, perçage et présentation",
        h1_es="Dónde colgar la etiqueta: posición, troquel y exposición",
        tag_zh="吊牌指南", tag_en="Hangtag Guide", tag_ja="値札ガイド",
        tag_ko="행택 가이드", tag_fr="Guide carton", tag_es="Guía de colgantes",
        sum_zh="挂在领口还是腰头，看着是小事，却同时决定三件事：第一眼能不能读到品牌、试穿会不会被扯掉、退货时吊牌还在不在。这篇给出七个品类的首选挂位表、孔位到边距离与重心规则、四样不能被遮挡的东西，以及陈列朝向与防盗扣的正确位置。",
        sum_en="Neckline or waistband looks like a small choice and settles three things at once: whether the brand is read, whether the tag survives trying on, and whether it is still there at return. Position table for seven categories, hole distance and gravity rules, four things never to cover, and where the security tag belongs.",
        sum_ja="衿元か腰かは小さな選択に見えて、三つを同時に決めます。一目でブランドが読めるか、試着で切れないか、返品時に残るか。七品種の位置表、穴の端距離と重心の規則、隠してはいけない四つ、陳列の向きと防盗タグの正しい位置を整理します。",
        sum_ko="목선이냐 허리냐는 사소해 보이지만 세 가지를 동시에 정합니다. 첫눈에 브랜드가 읽히는지, 입어볼 때 뜯기지 않는지, 반품 시 남는지. 일곱 품목의 위치표, 구멍 거리와 무게중심 규칙, 가리면 안 되는 네 가지, 진열 방향과 도난 방지 태그 위치를 정리합니다.",
        sum_fr="Encolure ou ceinture : un choix minuscule qui règle trois choses — la marque lue, le carton qui survit à l'essayage, sa présence au retour. Tableau pour sept catégories, distance du trou, règles de gravité, quatre interdits et place de l'antivol.",
        sum_es="Escote o cintura parece menor y decide tres cosas: que se lea la marca, que la etiqueta sobreviva a la prueba y que siga en una devolución. Tabla de siete categorías, distancia del agujero, reglas de gravedad, cuatro cosas que no se tapan y dónde va la alarma.",
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

    crumb = ('<div class="crumb"><a href="../index.html" data-zh="首页" data-fr="Accueil" data-es="Inicio" data-en="Home" data-ja="ホーム" data-ko="홈">首页</a>'
             ' / <a href="index.html" data-zh="辅料 FAQ" data-fr="FAQ Accessoires" data-es="FAQ Accesorios" data-en="Trims FAQ" data-ja="副資材 FAQ" data-ko="부자재 FAQ">辅料 FAQ</a>'
             ' / <span data-zh="%s" data-en="%s" data-ja="%s" data-ko="%s" data-fr="%s" data-es="%s">%s</span></div>'
             % (a["crumb_zh"], a["crumb_en"], a["crumb_ja"], a["crumb_ko"],
                a["crumb_fr"], a["crumb_es"], a["crumb_zh"]))
    s, n = re.subn(r'<div class="crumb">.*?</div>', crumb, s, count=1, flags=re.S)
    assert n == 1, "crumb 替换失败"

    h1 = ('<h1 data-zh="%s" data-en="%s" data-ja="%s" data-ko="%s" data-fr="%s" data-es="%s">%s</h1>'
          % (a["h1_zh"], a["h1_en"], a["h1_ja"], a["h1_ko"], a["h1_fr"], a["h1_es"], a["h1_zh"]))
    s, n = re.subn(r'<h1 .*?</h1>', h1, s, count=1, flags=re.S)
    assert n == 1, "h1 替换失败"

    meta = ('<p data-zh="泰阁包装 · 更新于 %s" data-en="By TAGE Packaging &nbsp;·&nbsp; Updated %s" '
            'data-ja="泰閣包装 · %s更新" data-ko="TAGE 패키징 · %s" '
            'data-fr="Par TAGE Packaging &nbsp;·&nbsp; Mis à jour le %s" '
            'data-es="Por TAGE Packaging &nbsp;·&nbsp; Actualizado el %s">泰阁包装 · 更新于 %s</p>'
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
        <a class="more" href="{slug}" data-zh="阅读全文 →" data-en="Read more →" data-ja="続きを読む →" data-ko="자세히 보기 →" data-fr="Lire la suite →" data-es="Leer más →">阅读全文 →</a>
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
