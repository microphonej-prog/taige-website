#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-28 10:00 批次每日更新生成脚本（六语：zh-Hant 根 / en / ja / ko / fr / es）
- 换辅料供应商的过渡管理（trim-supplier-switchover-guide）
- AI 设计稿上机印刷的印前处理（ai-generated-artwork-trim-printing-guide）

用法: F:/hermes/venvs/tools/Scripts/python.exe daily_gen_20261028_1000.py [--check]
"""
import os, re, sys, subprocess, importlib.util

ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)
PY = sys.executable

SKEL = "blog/knitwear-sweater-trims-guide.html"
DATE_ZH = "2026年10月28日"
DATE_EN = "October 28, 2026"
DATE_JA = "2026年10月28日更新"
DATE_KO = "2026년 10월 28일 업데이트"
DATE_FR = "28 octobre 2026"
DATE_ES = "28 de octubre de 2026"
SITEMAP_DATE = "2026-10-28"
BUST_OLD, BUST_NEW = "187", "188"
LANGS = ["en", "ja", "ko", "fr", "es"]

ARTICLES = [
    dict(
        slug="trim-supplier-switchover-guide.html",
        body="blog/_body_switchover.html",
        title_zh="换辅料供应商怎么不翻车：双轨过渡与封样移植 | TAGE",
        title_en="Switching Trims Suppliers Without a Quality Gap: Parallel Runs and Sample Transfer | TAGE",
        title_ja="副資材サプライヤーの切替を失敗させない：並行生産と基準サンプルの移管 | TAGE",
        title_ko="부자재 공급사 교체를 실패 없이: 병행 생산과 골든 샘플 이전 | TAGE",
        title_fr="Changer de fournisseur d'accessoires sans rupture de qualité : production parallèle et transfert de références | TAGE",
        title_es="Cambiar de proveedor de accesorios sin perder calidad: producción paralela y traspaso de muestras | TAGE",
        desc_zh="换辅料供应商的过渡管理：什么情况该换、六样标准必须移交、首批全检与双轨供应怎么排、颜色手感排版模切包装五处翻车点、切换期对外信息一致性，以及八周切换时间表。来自东莞泰阁包装，吊牌、织唛、洗水标与包装一站式配套。",
        desc_en="Switching trims suppliers: six standards to transfer, parallel runs and inspection, five failure points, external consistency and an eight-week switchover plan.",
        desc_ja="副資材サプライヤー切替の進め方。移管すべき6つの基準、初回全数検査と並行供給の組み方、色・風合い・組版・抜き・梱包の5つの失敗点、对外情報の一貫性、8週間のスケジュールを解説します。東莞泰閣包装。",
        desc_ko="부자재 공급사 교체 가이드. 이전해야 할 여섯 가지 기준, 첫 로트 전수 검사와 병행 공급 설계, 색·촉감·조판·커팅·포장의 다섯 실패 지점, 대외 정보 일관성, 8주 일정을 정리했습니다. 둥관 TAGE 패키징.",
        desc_fr="Changer de fournisseur d'accessoires : six standards à transférer, production parallèle et inspection, cinq points de défaillance et un plan de huit semaines.",
        desc_es="Cambiar de proveedor de accesorios: seis estándares a transferir, producción paralela e inspección, cinco puntos de fallo y un plan de ocho semanas.",
        crumb_zh="辅料供应商切换",
        crumb_en="Supplier Switchover",
        crumb_ja="サプライヤー切替",
        crumb_ko="공급사 교체",
        crumb_fr="Changement de fournisseur",
        crumb_es="Cambio de proveedor",
        h1_zh="换辅料供应商怎么不翻车：双轨过渡与封样移植",
        h1_en="Switching Trims Suppliers Without a Quality Gap: Parallel Runs and Sample Transfer",
        h1_ja="副資材サプライヤーの切替を失敗させない：並行生産と基準サンプルの移管",
        h1_ko="부자재 공급사 교체를 실패 없이: 병행 생산과 골든 샘플 이전",
        h1_fr="Changer de fournisseur d'accessoires sans rupture de qualité : production parallèle et transfert de références",
        h1_es="Cambiar de proveedor de accesorios sin perder calidad: producción paralela y traspaso de muestras",
        tag_zh="供应链", tag_en="Supply Chain", tag_ja="サプライチェーン", tag_ko="공급망",
        tag_fr="Chaîne d'approvisionnement", tag_es="Cadena de suministro",
        sum_zh="换供应商最难的不是拿到第二份报价，而是让第二家做出的吊牌和第一家看起来是同一批。本文拆六件事：什么情况该换、六样标准必须移交、双轨并行期怎么排、最容易翻车的五处、切换期对外信息怎么守住，以及一张八周切换时间表。",
        sum_en="The hard part of switching suppliers is not the second quotation, but making the second supplier's hang tags read as the same batch as the first. Six parts: when to switch, the six standards to transfer, how to run both in parallel, the five points that fail first, external consistency, and an eight-week plan.",
        sum_ja="サプライヤー切替で難しいのは2社目の見積りではなく、2社目が作るタグを1社目と同じロットに見せることです。切替の判断、移管すべき6つの基準、並行生産の組み方、最も失敗しやすい5点、对外情報の一貫性、8週間のスケジュールを整理します。",
        sum_ko="공급사 교체에서 어려운 것은 두 번째 견적이 아니라, 두 번째 공급사가 만든 행택을 첫 번째와 같은 로트처럼 보이게 하는 일입니다. 교체 판단, 이전해야 할 여섯 기준, 병행 생산 설계, 가장 자주 무너지는 다섯 지점, 대외 정보 일관성, 8주 일정을 정리합니다.",
        sum_fr="Le plus difficile n'est pas le deuxième devis, mais de faire ressembler les hangtags du second fournisseur au même lot que ceux du premier. Six volets : quand changer, les six standards à transférer, la production parallèle, les cinq points qui lâchent, la cohérence extérieure et un plan de huit semaines.",
        sum_es="Lo difícil no es el segundo presupuesto, sino que los colgantes del segundo proveedor parezcan del mismo lote que los del primero. Seis partes: cuándo cambiar, los seis estándares a transferir, la producción paralela, los cinco puntos que fallan, la coherencia externa y un plan de ocho semanas.",
    ),
    dict(
        slug="ai-generated-artwork-trim-printing-guide.html",
        body="blog/_body_aidesign.html",
        title_zh="AI 生成的吊牌设计稿能直接印刷吗：分辨率、矢量与色彩 | TAGE",
        title_en="Can AI-Generated Hang Tag Artwork Go Straight to Print? Resolution, Vectors and Colour | TAGE",
        title_ja="AI生成のタグ図稿はそのまま印刷できるか：解像度・ベクター・色 | TAGE",
        title_ko="AI로 만든 행택 도안을 바로 인쇄할 수 있을까: 해상도, 벡터, 색 | TAGE",
        title_fr="Un visuel de hangtag généré par IA peut-il partir directement en impression ? Résolution, vecteurs et couleur | TAGE",
        title_es="¿Se puede imprimir directamente un colgante diseñado con IA? Resolución, vectores y color | TAGE",
        desc_zh="AI 设计稿上机印刷前的必做处理：位图与矢量之别、成品尺寸下的 300dpi 怎么算、文字为什么必须重排、RGB 与 CMYK 的色域差、烫金凹凸 UV 与织唛的专版要求，附交付清单与版权风险提示。来自东莞泰阁包装。",
        desc_en="AI artwork before the press: pixels versus vectors, 300 dpi at final size, why type must be reset, RGB versus CMYK, colour accuracy and a delivery checklist.",
        desc_ja="AI図稿を印刷に載せる前の必須処理。ビットマップとベクターの違い、仕上がり寸法での300dpiの計算、文字を組み直す理由、RGBとCMYKの色域差、箔・エンボス・UV・織りの版要件、納品チェックリストを解説します。東莞泰閣包装。",
        desc_ko="AI 도안을 인쇄에 올리기 전 필수 처리. 비트맵과 벡터의 차이, 완성 치수 기준 300dpi 계산, 문자 재조판 이유, RGB와 CMYK 색역 차이, 박·엠보·UV·직조판 요건, 납품 체크리스트를 정리했습니다. 둥관 TAGE 패키징.",
        desc_fr="Un visuel IA avant l'impression : pixels contre vecteurs, 300 dpi à la taille finale, recomposition du texte, RVB contre CMJN, plaques de dorure et gaufrage, liste de livraison.",
        desc_es="Un artístico de IA antes de imprimir: píxeles frente a vectores, 300 ppp al tamaño final, recomposición del texto, RGB frente a CMYK, planchas de estampado y gofrado, lista de entrega.",
        crumb_zh="AI 设计稿与印刷",
        crumb_en="AI Artwork and Print",
        crumb_ja="AI図稿と印刷",
        crumb_ko="AI 도안과 인쇄",
        crumb_fr="Visuels IA et impression",
        crumb_es="Artísticos de IA e impresión",
        h1_zh="AI 生成的吊牌设计稿能直接印刷吗：分辨率、矢量与色彩",
        h1_en="Can AI-Generated Hang Tag Artwork Go Straight to Print? Resolution, Vectors and Colour",
        h1_ja="AI生成のタグ図稿はそのまま印刷できるか：解像度・ベクター・色",
        h1_ko="AI로 만든 행택 도안을 바로 인쇄할 수 있을까: 해상도, 벡터, 색",
        h1_fr="Un visuel de hangtag généré par IA peut-il partir directement en impression ? Résolution, vecteurs et couleur",
        h1_es="¿Se puede imprimir directamente un colgante diseñado con IA? Resolución, vectores y color",
        tag_zh="印前技术", tag_en="Prepress", tag_ja="プリプレス", tag_ko="프리프레스",
        tag_fr="Prépresse", tag_es="Preimpresión",
        sum_zh="AI 出图快，但印刷这一端仍然由文件决定成品。屏幕上的漂亮图可能没有一处能直接上机：像素不是矢量、文字是画出来的、颜色是发光的 RGB。本文讲清分辨率怎么按成品尺寸算、文字为什么必须重排、颜色怎么换算、烫金凹凸 UV 与织唛要什么专版，并给一份交付清单。",
        sum_en="AI generates fast, but at the printing end the file still decides the product. A handsome screen image may contain nothing printable: pixels are not vectors, type is drawn rather than set, colour is emissive RGB. Covers resolution at final size, why type must be reset, colour conversion, plates for foil, emboss, UV and woven labels, and a delivery checklist.",
        sum_ja="AIの出図は速いですが、印刷側では依然としてファイルが製品を決めます。画面の美しい画像に、そのまま印刷できる部分がないことがあります。ピクセルはベクターでなく、文字は描かれたもので、色は発光するRGBだからです。仕上がり寸法での解像度計算、文字を組み直す理由、色変換、箔・エンボス・UV・織りの版要件、納品チェックリストを整理します。",
        sum_ko="AI는 빠르지만 인쇄 쪽에서는 여전히 파일이 제품을 결정합니다. 화면의 예쁜 이미지에 바로 인쇄할 수 있는 부분이 하나도 없을 수 있습니다. 픽셀은 벡터가 아니고 문자는 그려진 것이며 색은 발광 RGB이기 때문입니다. 완성 치수 기준 해상도 계산, 문자 재조판 이유, 색 변환, 박·엠보·UV·직조판 요건, 납품 체크리스트를 정리합니다.",
        sum_fr="L'IA produit vite, mais côté imprimerie c'est toujours le fichier qui décide. Une belle image d'écran peut ne rien contenir d'imprimable : des pixels et non des vecteurs, un texte dessiné et non composé, du RVB émissif. Au programme : résolution à la taille finale, recomposition du texte, conversion couleur, plaques de dorure, gaufrage, UV et tissé, et une liste de livraison.",
        sum_es="La IA produce rápido, pero en la imprenta sigue siendo el archivo el que decide. Una bella imagen de pantalla puede no contener nada imprimible: píxeles que no son vectores, texto dibujado y no compuesto, RGB emisivo. Incluye resolución al tamaño final, recomposición del texto, conversión de color, planchas de estampado, gofrado, UV y tejido, y una lista de entrega.",
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

# ---------------- desc 长度体检 ----------------
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
            'data-ja="泰閣包装 · %s" data-ko="TAGE 패키징 · %s" '
            'data-fr="Par TAGE Packaging &nbsp;·&nbsp; Mis à jour le %s" '
            'data-es="Por TAGE Packaging &nbsp;·&nbsp; Actualizado el %s">泰阁包装 · 更新于 %s</p>'
            % (DATE_ZH, DATE_EN, DATE_JA, DATE_KO, DATE_FR, DATE_ES, DATE_ZH))
    s, n = re.subn(r'<p data-zh="泰[阁閣]包[装裝] · 更新[于於][^\"]*\".*?</p>', meta, s, count=1, flags=re.S)
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
sm = open("sitemap.xml", encoding="utf-8", newline="").read()
before_lines = sm.count("\n")


def block(url):
    return ("  <url>\r\n    <loc>%s</loc>\r\n    <lastmod>%s</lastmod>\r\n"
            "    <changefreq>monthly</changefreq>\r\n    <priority>0.7</priority>\r\n  </url>\r\n"
            % (url, SITEMAP_DATE))


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
print("sitemap 新增 %d 个 URL，行数 %d -> %d，<loc> 总数 %d"
      % (len(blocks), before_lines, sm.count("\n"), sm.count("<loc>")))

# ---------------- 6) BUST_VERSION 升级 ----------------
mj = open("js/main.js", encoding="utf-8").read()
assert 'var BUST_VERSION = "%s";' % BUST_OLD in mj, "BUST_VERSION 不是 %s" % BUST_OLD
mj = mj.replace('var BUST_VERSION = "%s";' % BUST_OLD, 'var BUST_VERSION = "%s";' % BUST_NEW, 1)
open("js/main.js", "w", encoding="utf-8", newline="").write(mj)
print("BUST_VERSION %s -> %s" % (BUST_OLD, BUST_NEW))
