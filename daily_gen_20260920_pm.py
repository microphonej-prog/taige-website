#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-09-20 第三批（20:00）每日更新：2 篇新文章（六语：zh-Hant 根 / en / ja / ko / fr / es）
+ 列表页卡片 + gen_i18n 五语生成 + sitemap + BUST_VERSION 升级 + 繁体转换。

用法: python daily_gen_20260920_pm.py
"""
import os, re, sys, subprocess, importlib.util

ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)
PY = sys.executable

SKEL = "blog/knitwear-sweater-trims-guide.html"
DATE_ZH = "2026年9月20日"
DATE_EN = "September 20, 2026"
DATE_JA = "2026年9月20日更新"
DATE_KO = "2026년 9월 20일 업데이트"
DATE_FR = "20 septembre 2026"
DATE_ES = "20 de septiembre de 2026"
SITEMAP_DATE = "2026-09-20"
BUST_OLD, BUST_NEW = "93", "94"
LANGS = ["en", "ja", "ko", "fr", "es"]

ARTICLES = [
    dict(
        slug="hang-tag-edge-painting-guide.html",
        body="blog/_body_edge_painting.html",
        title_zh="吊牌刷边工艺指南：金边、银边与彩色边怎么做怎么选 | TAGE",
        title_en="Hang Tag Edge Painting: Gold, Silver &amp; Coloured Edges | TAGE",
        title_ja="タグの小口加工ガイド：金・銀・カラー小口の選び方と作り方 | TAGE",
        title_ko="행택 테두리 도색 가이드: 금·은·컬러 엣지의 선택과 제작 | TAGE",
        title_fr="Dorure sur tranche des étiquettes : or, argent et couleurs | TAGE",
        title_es="Pintado de cantos en etiquetas: oro, plata y color | TAGE",
        desc_zh="吊牌刷边工艺指南：金边、银边与品牌专色边怎么做——丝网刷边、喷涂与烫箔边三种方式的效果与风险对比，什么场景值得做，文件与边宽公差怎么给，折弯、摩擦、堆叠三项验收测试，以及夹具费用与起订量怎么算。来自东莞泰阁包装。",
        desc_en="Hang tag edge painting: screen, spray and foil edges compared, when a painted edge pays off, tolerances, three acceptance tests and how the cost is built.",
        desc_ja="タグの小口加工ガイド。スクリーン塗り・スプレー・箔押しの比較、向く用途、見当公差の指定、折り曲げ・摩擦・重ねの3検査、治具費用と最小ロットの考え方を解説します。東莞泰閣包装。",
        desc_ko="행택 테두리 도색 가이드: 스크린, 스프레이, 박 테두리 비교와 적합한 용도, 공차 지정, 세 가지 검사 방법, 지그 비용과 최소 수량까지 정리했습니다. 둥관 TAGE 패키징.",
        desc_fr="Dorure sur tranche des étiquettes : sérigraphie, pulvérisation et foil comparés, cas d'usage, tolérances, trois tests de réception et structure de coût.",
        desc_es="Pintado de cantos en etiquetas: serigrafía, pulverizado y foil comparados, casos de uso, tolerancias, tres pruebas de recepción y estructura de coste.",
        crumb_zh="吊牌刷边工艺", crumb_en="Hang Tag Edge Painting", crumb_ja="タグの小口加工",
        crumb_ko="행택 테두리 도색", crumb_fr="Dorure sur tranche", crumb_es="Pintado de cantos",
        h1_zh="吊牌刷边工艺指南：金边、银边与彩色边怎么做怎么选",
        h1_en="Hang Tag Edge Painting: Gold, Silver and Coloured Edges Explained",
        h1_ja="タグの小口加工ガイド：金・銀・カラー小口の選び方と作り方",
        h1_ko="행택 테두리 도색 가이드: 금·은·컬러 엣지의 선택과 제작",
        h1_fr="Dorure sur tranche des étiquettes : or, argent et couleurs",
        h1_es="Pintado de cantos en etiquetas colgantes: oro, plata y color",
        tag_zh="工艺指南", tag_en="Finishing", tag_ja="加工ガイド", tag_ko="가공 가이드",
        tag_fr="Finition", tag_es="Acabados",
        sum_zh="刷边是在吊牌切好的四条边上加一道颜色，金银边对质感的提升往往比在同一面多烫一块金更明显；但它也是返工率偏高的一道工序——边油开裂、颜色不匀、堆叠互粘多来自参数没讲清。本文对比丝网刷边、喷涂刷边与烫箔边三种方式，讲清什么场景值得做、边宽与套准公差怎么给、收货做哪三个测试、夹具一次性费用与起订量怎么算。",
        sum_en="Edge painting adds a band of colour to the cut edges of a tag, and a gold or silver edge often lifts perceived quality more than one more foil block on the face. It is also a higher-rework step: cracking, patchy colour and sticking trace back to loose parameters. This guide compares screen, spray and foil edges, covers file handover and tolerances, three acceptance tests, and how jigs and volume drive cost.",
        sum_ja="小口加工は断裁された四辺に色の帯を付ける加工で、金銀の小口は面にもう一段箔を足すよりも質感を高めやすい一方、ひび割れ・色ムラ・密着など手直しの多い工程でもあります。スクリーン・スプレー・箔押しの3方式を比較し、向く用途、小口幅と見当公差の指定、受入時の3検査、治具の一時費用と最小ロットの考え方を解説します。",
        sum_ko="테두리 도색은 재단된 네 변에 색 띠를 넣는 가공으로, 금·은 테두리는 같은 면에 금박을 한 번 더 넣는 것보다 질감을 살리기 쉽지만 갈라짐·색 불균일·겹침 같은 재작업이 많은 공정이기도 합니다. 스크린, 스프레이, 박 테두리 세 방식을 비교하고 적합한 용도, 폭과 정합 공차 지정, 입고 시 세 가지 검사, 지그 일회성 비용과 최소 수량을 정리합니다.",
        sum_fr="La dorure sur tranche ajoute un filet de couleur aux bords coupés d'une étiquette : un filet or ou argent rehausse souvent plus la qualité perçue qu'un bloc de foil supplémentaire. C'est aussi une étape génératrice de reprises. Ce guide compare sérigraphie, pulvérisation et foil, la remise de fichier, trois tests de réception et la structure de coût.",
        sum_es="El pintado de cantos añade una banda de color a los bordes cortados de la etiqueta: un canto oro o plata eleva más la calidad percibida que otro bloque de foil en la cara. También es un paso con más retrabajo. Esta guía compara serigrafía, pulverizado y foil, la entrega de archivo, tres pruebas de recepción y el coste.",
    ),
    dict(
        slug="clothing-label-compliance-south-korea.html",
        body="blog/_body_korea_compliance.html",
        title_zh="韩国服装标签合规指南：KC 标志、混用率与韩文洗护标示 | TAGE",
        title_en="South Korea Clothing Label Compliance: KC Mark &amp; Care Symbols | TAGE",
        title_ja="韓国の衣料ラベル規制ガイド：KCマーク・混用率・韓国語の洗濯表示 | TAGE",
        title_ko="한국 의류 라벨 규정 가이드: KC 마크, 혼용률, 한글 세탁 표시 | TAGE",
        title_fr="Conformité des étiquettes en Corée du Sud : KC et composition | TAGE",
        title_es="Cumplimiento de etiquetas en Corea del Sur: KC y composición | TAGE",
        desc_zh="韩国服装标签合规指南：讲清《电器用品及生活用品安全管理法》下的品质标示项目、安全确认与供应商适合性确认两条 KC 路径、纤维混用率公差、KS K 0021 洗护符号与韩文字号要求，以及中国工厂最常漏掉制造年月与消费者咨询电话的五个错误。来自东莞泰阁包装。",
        desc_en="South Korea clothing label compliance: KC mark routes, quality labelling items, fibre content tolerance and Korean care symbols for apparel imports.",
        desc_ja="韓国の衣料ラベル規制ガイド。生活用品安全管理法に基づく品質表示項目、KC の安全確認と供給者適合性確認、混用率の許容差、KS K 0021 の洗濯記号、韓国語の文字サイズ、製造年月の欠落など中国工場がよく犯す誤りを解説します。東莞泰閣包装。",
        desc_ko="한국 의류 라벨 규정 가이드: 생활용품 안전관리법상 품질표시 항목, KC 안전확인과 공급자적합성확인, 혼용률 허용 오차, KS K 0021 세탁 기호, 한글 표시 요건과 자주 하는 실수를 정리했습니다. 둥관 TAGE 패키징.",
        desc_fr="Conformité des étiquettes de vêtements en Corée du Sud : parcours KC, mentions de qualité, tolérance de composition et symboles d'entretien en coréen.",
        desc_es="Cumplimiento de etiquetas de ropa en Corea del Sur: vías del KC, menciones de calidad, tolerancia de composición y símbolos de cuidado en coreano.",
        crumb_zh="韩国服装标签合规", crumb_en="South Korea Label Compliance", crumb_ja="韓国向け衣料ラベル規制",
        crumb_ko="한국 의류 라벨 규정", crumb_fr="Conformité Corée du Sud", crumb_es="Cumplimiento Corea del Sur",
        h1_zh="韩国服装标签合规指南：KC 标志、混用率与韩文洗护标示",
        h1_en="South Korea Clothing Label Compliance: KC Mark, Fibre Content and Korean Care Symbols",
        h1_ja="韓国の衣料ラベル規制ガイド：KCマーク・混用率・韓国語の洗濯表示",
        h1_ko="한국 의류 라벨 규정 가이드: KC 마크, 혼용률, 한글 세탁 표시",
        h1_fr="Conformité des étiquettes de vêtements en Corée du Sud : KC, composition et symboles",
        h1_es="Cumplimiento de etiquetas de ropa en Corea del Sur: KC, composición y símbolos",
        tag_zh="合规指南", tag_en="Compliance", tag_ja="コンプライアンス", tag_ko="컴플라이언스",
        tag_fr="Conformité", tag_es="Cumplimiento",
        sum_zh="韩国服装标签的要求和欧美并不通用：除了混用率、制造国与洗涤方法，还必须标示制造年月和品质保证基准或消费者咨询电话，并加施 KC 体系下的安全确认或供应商适合性确认信息。本文梳理法规依据、八项必标信息、两条 KC 路径、KS K 0021 韩文洗护符号，以及中国工厂最常犯的五个错误与吊牌／主唛／洗水标的项目分工。",
        sum_en="Korea does not accept an EU- or US-style label set: alongside fibre content, origin and care instructions it requires the month and year of manufacture and either a quality warranty standard or a consumer enquiry number, plus KC safety confirmation or supplier declaration information. This guide covers the legal basis, the eight mandatory items, the two KC routes, KS K 0021 Korean care symbols, five common mistakes and how to split items across tag, neck label and care label.",
        sum_ja="韓国の衣料ラベルは欧米の仕様をそのまま流用できません。混用率・原産国・洗濯方法に加え、製造年月と品質保証基準または消費者相談電話番号の表示、KC 制度上の安全確認または供給者適合性確認情報が必要です。法規の根拠、必須8項目、KC の2ルート、KS K 0021 の韓国語洗濯記号、よくある5つの誤り、タグ・メインラベル・洗濯表示ラベルの役割分担を整理します。",
        sum_ko="한국 의류 라벨은 미국·유럽 기준을 그대로 쓸 수 없습니다. 혼용률, 제조국, 세탁 방법과 함께 제조연월, 품질보증기준 또는 소비자 상담 전화번호, KC 안전확인 또는 공급자적합성확인 정보가 필요합니다. 법적 근거, 필수 8개 항목, KC 두 경로, KS K 0021 한글 세탁 기호, 자주 하는 다섯 가지 실수, 행택·메인 라벨·세탁 표시 라벨의 역할 분담을 정리합니다.",
        sum_fr="La Corée du Sud n'accepte pas un jeu d'étiquettes de type UE ou US : outre la composition, l'origine et l'entretien, elle exige le mois et l'année de fabrication et une norme de garantie qualité ou un numéro consommateur, ainsi que les mentions KC. Ce guide couvre la base légale, les huit mentions obligatoires, les deux parcours KC, les symboles coréens KS K 0021, cinq erreurs fréquentes et la répartition entre les trois supports.",
        sum_es="Corea del Sur no acepta etiquetas de estilo UE o EE. UU.: además de composición, origen y cuidado exige mes y año de fabricación y una norma de garantía o un teléfono de consumidor, más las menciones del KC. Esta guía cubre la base legal, las ocho menciones obligatorias, las dos vías del KC, los símbolos coreanos KS K 0021, cinco errores frecuentes y el reparto entre los tres soportes.",
    ),
]

skel = open(SKEL, encoding="utf-8").read()
old3 = re.search(r'"position": 3,\s*"name": "([^"]*)"', skel).group(1)
print("骨架 breadcrumb 名:", old3)

# ---------------- 撞车安全闸 ----------------
sm0 = open("sitemap.xml", encoding="utf-8").read()
for a in ARTICLES:
    for p in ["blog/%s" % a["slug"]] + ["%s/blog/%s" % (l, a["slug"]) for l in LANGS]:
        if os.path.exists(p):
            raise SystemExit("选题撞车：%s 已存在，换选题！" % p)
    if ("/blog/%s</loc>" % a["slug"]) in sm0:
        raise SystemExit("选题撞车：sitemap 已含 %s" % a["slug"])
print("选题全新，开始生成")

# ---------------- 1) 生成两篇文章（六语属性） ----------------
for a in ARTICLES:
    slug = a["slug"]
    s = skel.replace(SKEL.replace("blog/", ""), slug)

    title_line = ('<title data-zh="%s" data-en="%s" data-ja="%s" data-ko="%s" data-fr="%s" data-es="%s">%s</title>'
                  % (a["title_zh"], a["title_en"], a["title_ja"], a["title_ko"], a["title_fr"], a["title_es"], a["title_zh"]))
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
             % (a["crumb_zh"], a["crumb_en"], a["crumb_ja"], a["crumb_ko"], a["crumb_fr"], a["crumb_es"], a["crumb_zh"]))
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
    s, n = re.subn(r'<p data-zh="泰閣包裝 · 更新於[^"]*".*?</p>', meta, s, count=1, flags=re.S)
    if n != 1:  # 简体骨架兜底
        s, n = re.subn(r'<p data-zh="泰阁包装 · 更新于[^"]*".*?</p>', meta, s, count=1, flags=re.S)
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
    print("写入 %s (%d KB) desc_en=%d desc_fr=%d desc_es=%d desc_zh=%d"
          % (out, len(s.encode("utf-8")) // 1024, len(a["desc_en"]), len(a["desc_fr"]), len(a["desc_es"]), len(a["desc_zh"])))

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
        tag_zh=a["tag_zh"], tag_en=a["tag_en"], tag_ja=a["tag_ja"], tag_ko=a["tag_ko"], tag_fr=a["tag_fr"], tag_es=a["tag_es"],
        h3_zh=a["h1_zh"], h3_en=a["h1_en"], h3_ja=a["h1_ja"], h3_ko=a["h1_ko"], h3_fr=a["h1_fr"], h3_es=a["h1_es"],
        sum_zh=a["sum_zh"], sum_en=a["sum_en"], sum_ja=a["sum_ja"], sum_ko=a["sum_ko"], sum_fr=a["sum_fr"], sum_es=a["sum_es"],
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
mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
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
             ["https://taigetag.com/%s/blog/%s" % (l, slug) for l in ["en", "ja", "ko", "fr", "es"]]:
        assert "<loc>%s</loc>" % u not in sm, "sitemap 已有 %s" % u
        blocks.append(block(u))
sm = sm.replace("</urlset>", "".join(blocks) + "</urlset>", 1)

# blog 首页 lastmod 更新（六语）
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
