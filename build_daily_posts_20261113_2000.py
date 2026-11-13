#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-11-13 20:00 每日 FAQ：2 篇（英文主稿 + 六语属性），生成中文主文件 + blog/index.html 卡片。"""
import re, os, sys

SKEL = "blog/euro-hole-retail-hang-packaging-guide.html"
OLD_SLUG = "euro-hole-retail-hang-packaging-guide"
DATE_ZH = "2026年11月13日"
DATE_EN = "November 13, 2026"
DATE_FR = "13 novembre 2026"
DATE_ES = "13 de noviembre de 2026"
DATE_JA = "2026年11月13日"
DATE_KO = "2026년 11월 13일"

ARTICLES = [
    dict(
        slug="trim-crocking-perspiration-fastness-guide",
        body="F:/hermes/cache/scratch/body_fastness.html",
        tag_zh="检测标准", tag_en="Test Standards", tag_fr="Normes d'essai", tag_es="Normas de ensayo",
        tag_ja="試験規格", tag_ko="시험 규격",
        title_zh="耐摩擦与耐汗渍色牢度：辅料沾色的标准与整改 | TAGE",
        title_en="Crocking and Perspiration Fastness for Garment Trims | TAGE",
        title_fr="Solidité au frottement et à la sueur des accessoires | TAGE",
        title_es="Solidez al frote y a la transpiración en accesorios | TAGE",
        title_ja="摩擦・汗堅ろう度：衣料副資材の汚染試験と改善 | TAGE",
        title_ko="마찰·땀 견뢰도: 의류 부자재 이염 시험과 개선 | TAGE",
        desc_zh="耐摩擦与耐汗渍色牢度是辅料抽检最容易失分的两项。本文讲清 ISO 105-X12 与 AATCC 8/15 的干湿摩擦限值、酸碱汗渍评级读法、掉色的四个真实原因，以及不改色相的整改工艺与出货前清单。",
        desc_en="Crocking and perspiration fastness for garment trims: ISO 105-X12 and AATCC 8/15 limits, grey-scale grading, four real causes of bleeding and how to fix a lot.",
        desc_fr="Frottement et sueur sur les accessoires : limites ISO 105-X12 et AATCC 8/15, lecture de l'échelle de gris, quatre causes réelles de transfert et correction du lot.",
        desc_es="Frote y sudor en accesorios: límites ISO 105-X12 y AATCC 8/15, lectura de la escala de grises, cuatro causas reales del manchado y corrección del lote.",
        desc_ja="衣料副資材の摩擦・汗堅ろう度。ISO 105-X12 と AATCC 8/15 の規格値、グレースケールの読み方、汚染の四つの原因、色を変えない改善手順まで解説します。",
        desc_ko="의류 부자재의 마찰·땀 견뢰도. ISO 105-X12와 AATCC 8/15 한도, 그레이 스케일 읽는 법, 오염의 네 가지 원인, 색을 바꾸지 않는 개선 절차를 정리합니다.",
        crumb_zh="色牢度测试", crumb_en="Fastness Testing", crumb_fr="Essais de solidité", crumb_es="Ensayos de solidez",
        crumb_ja="堅ろう度試験", crumb_ko="견뢰도 시험",
        h1_zh="耐摩擦与耐汗渍色牢度：辅料沾色的标准、评级与整改",
        h1_en="Crocking and Perspiration Fastness for Garment Trims",
        h1_fr="Solidité au frottement et à la sueur des accessoires textiles",
        h1_es="Solidez al frote y a la transpiración en accesorios de confección",
        h1_ja="衣料副資材の摩擦・汗堅ろう度：汚染の規格と改善",
        h1_ko="의류 부자재의 마찰·땀 견뢰도: 오염 기준과 개선",
        sum_zh="沾色不是变色：ISO 105-X12 与 AATCC 8/15 的干湿摩擦与酸碱汗渍限值、灰色样卡评级、掉色的四个真实原因（染料、固色、油墨、柔软剂），以及不改色相的整改路径与出货前清单。",
        sum_en="Staining, not shade change: ISO 105-X12 and AATCC 8/15 limits for dry and wet rub and acid/alkaline perspiration, how to read the grey scale, four real causes of bleeding and a fix path that keeps the colour.",
        sum_fr="Transfert et non changement de teinte : limites ISO 105-X12 et AATCC 8/15 en frottement sec et humide et sueur acide/alcaline, lecture de l'échelle de gris, quatre causes réelles et correction sans changer la couleur.",
        sum_es="Manchado y no cambio de tono: límites ISO 105-X12 y AATCC 8/15 en frote seco y húmedo y sudor ácido/alcalino, lectura de la escala de grises, cuatro causas reales y corrección sin cambiar el color.",
        sum_ja="汚染であって変退色ではない——ISO 105-X12 と AATCC 8/15 の乾湿摩擦・酸性/アルカリ性汗の規格値、グレースケールの読み方、不合格の四つの原因、色相を変えない改善手順。",
        sum_ko="색 변화가 아닌 오염 — ISO 105-X12와 AATCC 8/15의 건식·습식 마찰과 산성/알칼리성 땀 한도, 그레이 스케일 읽는 법, 네 가지 원인, 색상을 바꾸지 않는 개선 절차.",
    ),
    dict(
        slug="garment-trims-small-parts-safety-guide",
        body="F:/hermes/cache/scratch/body_smallparts.html",
        tag_zh="安全合规", tag_en="Safety Compliance", tag_fr="Conformité sécurité", tag_es="Conformidad de seguridad",
        tag_ja="安全規制", tag_ko="안전 규제",
        title_zh="童装辅料小零件安全：圆筒判定、拉力与文件 | TAGE",
        title_en="Childrenswear Trims Small Parts Safety: 16 CFR 1501 and EN 71-1 | TAGE",
        title_fr="Sécurité des petites pièces sur les accessoires enfant | TAGE",
        title_es="Seguridad de piezas pequeñas en accesorios infantiles | TAGE",
        title_ja="子供服副資材の小さな部品安全：判定と引張試験 | TAGE",
        title_ko="아동복 부자재 작은 부품 안전: 판정과 인장 시험 | TAGE",
        desc_zh="童装辅料小零件安全：31.7 mm 圆筒怎么判、10/15 磅力拉力与 90 N 欧标、锐边与 EN 14682 绳带、CPC 与追踪标签要留什么，附不增加成本的五个设计动作。",
        desc_en="Childrenswear trims small parts safety: the 31.7 mm cylinder, 10/15 lbf and 90 N pull tests, sharp edges, EN 14682 cords, CPC tracking labels and design fixes.",
        desc_fr="Sécurité des petites pièces : cylindre de 31,7 mm, traction 10/15 lbf et 90 N, arêtes vives, cordons EN 14682, CPC et étiquette de traçabilité, solutions sans surcoût.",
        desc_es="Seguridad de piezas pequeñas: cilindro de 31,7 mm, tracción de 10/15 lbf y 90 N, bordes agudos, cordones EN 14682, CPC y etiqueta de trazabilidad.",
        desc_ja="子供服副資材の小さな部品安全。31.7 mm 円筒の判定、10/15 lbf と 90 N の引張試験、鋭い縁、EN 14682 の紐、CPC と追跡ラベル、コストを増やさない設計変更。",
        desc_ko="아동복 부자재 작은 부품 안전. 31.7 mm 원통 판정, 10/15 lbf와 90 N 인장 시험, 날카로운 모서리, EN 14682 끈, CPC와 추적 라벨, 무비용 설계 변경.",
        crumb_zh="小零件安全", crumb_en="Small Parts Safety", crumb_fr="Petites pièces", crumb_es="Piezas pequeñas",
        crumb_ja="小さな部品の安全", crumb_ko="작은 부품 안전",
        h1_zh="童装辅料小零件安全：圆筒判定、拉力测试与文件留存",
        h1_en="Childrenswear Trims Small Parts Safety: Cylinder, Pull Tests and Documentation",
        h1_fr="Sécurité des petites pièces sur les accessoires enfant : gabarit, essais et documents",
        h1_es="Seguridad de piezas pequeñas en accesorios infantiles: calibrador, ensayos y documentos",
        h1_ja="子供服副資材の小さな部品安全：円筒判定・引張試験・書類",
        h1_ko="아동복 부자재 작은 부품 안전: 원통 판정, 인장 시험, 서류",
        sum_zh="31.7 mm 圆筒怎么判、10/15 磅力与 90 N 拉力怎么做、锐边与绳带（EN 14682）怎么查、CPC 与追踪标签要留什么，以及不增加成本的五个设计动作。",
        sum_en="How the 31.7 mm cylinder decides, how 10/15 lbf and 90 N pull tests run, sharp edges and cords under EN 14682, what CPC and tracking labels must carry, and five no-cost design moves.",
        sum_fr="Le cylindre de 31,7 mm, les essais de traction de 10/15 lbf et 90 N, les arêtes vives et les cordons selon EN 14682, le CPC et l'étiquette de traçabilité, et cinq solutions sans surcoût.",
        sum_es="El cilindro de 31,7 mm, los ensayos de tracción de 10/15 lbf y 90 N, bordes agudos y cordones según EN 14682, el CPC y la etiqueta de trazabilidad, y cinco soluciones sin sobrecoste.",
        sum_ja="31.7 mm の円筒判定、10/15 lbf と 90 N の引張試験、鋭い縁と EN 14682 の紐、CPC と追跡ラベル、コストを増やさない五つの設計変更。",
        sum_ko="31.7 mm 원통 판정, 10/15 lbf와 90 N 인장 시험, 날카로운 모서리와 EN 14682 끈, CPC와 추적 라벨, 비용을 늘리지 않는 다섯 가지 설계 변경.",
    ),
]

skel = open(SKEL, encoding="utf-8").read()
old_name = re.search(r'"position": 3,\s*\n?\s*"name": "([^"]*)"', skel)
if not old_name:
    old_name = re.search(r'"position": 3, "name": "([^"]*)"', skel)
OLD_BREADCRUMB = old_name.group(1)

# 撞车安全闸
sm = open("sitemap.xml", encoding="utf-8").read()
for a in ARTICLES:
    for p in ["blog/%s.html" % a["slug"], "en/blog/%s.html" % a["slug"], "ja/blog/%s.html" % a["slug"]]:
        if os.path.exists(p):
            raise SystemExit("选题撞车：%s 已存在" % p)
    if "/blog/%s.html</loc>" % a["slug"] in sm:
        raise SystemExit("选题撞车：sitemap 已含 %s" % a["slug"])
print("选题全新，骨架 breadcrumb =", OLD_BREADCRUMB)

for a in ARTICLES:
    slug = a["slug"]
    s = skel.replace(OLD_SLUG, slug)

    # title
    title_line = ('<title data-zh="%s" data-en="%s" data-fr="%s" data-es="%s" data-ja="%s" data-ko="%s">%s</title>'
                  % (a["title_zh"], a["title_en"], a["title_fr"], a["title_es"], a["title_ja"], a["title_ko"], a["title_zh"]))
    s, n = re.subn(r'<title[^>]*>.*?</title>', title_line, s, count=1, flags=re.S)
    assert n == 1, "title 替换失败"

    # description
    s = re.sub(r'<meta name="description".*?content="[^"]*">', 'DESC_PLACEHOLDER', s, count=1, flags=re.S)
    desc_block = ('<meta name="description" data-zh="%s"\n'
                  '      data-en="%s"\n'
                  '      data-fr="%s"\n'
                  '      data-es="%s"\n'
                  '      data-ja="%s"\n'
                  '      data-ko="%s"\n'
                  '      content="%s">'
                  % (a["desc_zh"], a["desc_en"], a["desc_fr"], a["desc_es"], a["desc_ja"], a["desc_ko"], a["desc_zh"]))
    assert 'DESC_PLACEHOLDER' in s, "description 占位失败"
    s = s.replace('DESC_PLACEHOLDER', desc_block, 1)

    # crumb
    crumb = ('<div class="crumb"><a href="../index.html" data-zh="首页" data-en="Home" data-fr="Accueil" data-es="Inicio" data-ja="ホーム" data-ko="홈">首页</a>'
             ' / <a href="index.html" data-zh="辅料 FAQ" data-en="Trims FAQ" data-fr="FAQ Accessoires" data-es="FAQ Accesorios" data-ja="副資材 FAQ" data-ko="부자재 FAQ">辅料 FAQ</a>'
             ' / <span data-zh="%s" data-en="%s" data-fr="%s" data-es="%s" data-ja="%s" data-ko="%s">%s</span></div>'
             % (a["crumb_zh"], a["crumb_en"], a["crumb_fr"], a["crumb_es"], a["crumb_ja"], a["crumb_ko"], a["crumb_zh"]))
    s, n = re.subn(r'<div class="crumb">.*?</div>', crumb, s, count=1, flags=re.S)
    assert n == 1, "crumb 替换失败"

    # h1
    h1 = ('<h1 data-zh="%s" data-en="%s" data-fr="%s" data-es="%s" data-ja="%s" data-ko="%s">%s</h1>'
          % (a["h1_zh"], a["h1_en"], a["h1_fr"], a["h1_es"], a["h1_ja"], a["h1_ko"], a["h1_zh"]))
    s, n = re.subn(r'<h1 .*?</h1>', h1, s, count=1, flags=re.S)
    assert n == 1, "h1 替换失败"

    # meta 行
    meta = ('<p data-zh="泰阁包装 · 更新于 %s" data-en="By TAGE Packaging &nbsp;·&nbsp; Updated %s" '
            'data-fr="Par TAGE Packaging &nbsp;·&nbsp; Mis à jour le %s" '
            'data-es="Por TAGE Packaging &nbsp;·&nbsp; Actualizado el %s" '
            'data-ja="泰閣包装 · %s更新" data-ko="TAGE 패키징 · %s 업데이트">泰阁包装 · 更新于 %s</p>'
            % (DATE_ZH, DATE_EN, DATE_FR, DATE_ES, DATE_JA, DATE_KO, DATE_ZH))
    s, n = re.subn(r'<p data-zh="[^"]*更新[^"]*"[^>]*>[^<]*</p>', meta, s, count=1, flags=re.S)
    assert n == 1, "meta 行替换失败"

    # JSON-LD
    s = s.replace('"%s"' % OLD_BREADCRUMB, '"%s"' % a["h1_zh"])
    s, n = re.subn(r'"headline": "[^"]*"', '"headline": "%s"' % a["h1_zh"], s, count=1)
    assert n == 1, "headline 替换失败"

    # 正文
    body = open(a["body"], encoding="utf-8").read().rstrip("\n")
    i0 = s.index('  <section class="article-body">')
    i1 = s.index('\n</main>')
    s = s[:i0] + body + s[i1:]

    out = "blog/%s.html" % slug
    with open(out, "w", encoding="utf-8", newline="") as f:
        f.write(s)
    print("写入 %s  desc_en=%d 字符  desc_fr=%d  desc_es=%d  desc_zh=%d 字节=%d"
          % (out, len(a["desc_en"]), len(a["desc_fr"]), len(a["desc_es"]), len(a["desc_zh"]), len(s.encode("utf-8"))))

# ---------- blog/index.html 卡片 ----------
CARD = '''      <article class="post-card">
        <span class="tag" data-zh="{tag_zh}" data-en="{tag_en}" data-fr="{tag_fr}" data-es="{tag_es}" data-ja="{tag_ja}" data-ko="{tag_ko}">{tag_zh}</span>
        <h3 data-zh="{h3_zh}" data-en="{h3_en}" data-fr="{h3_fr}" data-es="{h3_es}" data-ja="{h3_ja}" data-ko="{h3_ko}">{h3_zh}</h3>
        <p data-zh="{sum_zh}" data-en="{sum_en}" data-fr="{sum_fr}" data-es="{sum_es}" data-ja="{sum_ja}" data-ko="{sum_ko}">{sum_zh}</p>
        <a class="more" href="{slug}.html" data-zh="阅读全文 →" data-en="Read more →" data-fr="Lire la suite →" data-es="Leer más →" data-ja="続きを読む →" data-ko="자세히 보기 →">阅读全文 →</a>
      </article>
'''
cards = ""
for a in ARTICLES:
    cards += CARD.format(
        tag_zh=a["tag_zh"], tag_en=a["tag_en"], tag_fr=a["tag_fr"], tag_es=a["tag_es"], tag_ja=a["tag_ja"], tag_ko=a["tag_ko"],
        h3_zh=a["h1_zh"], h3_en=a["h1_en"], h3_fr=a["h1_fr"], h3_es=a["h1_es"], h3_ja=a["h1_ja"], h3_ko=a["h1_ko"],
        sum_zh=a["sum_zh"], sum_en=a["sum_en"], sum_fr=a["sum_fr"], sum_es=a["sum_es"], sum_ja=a["sum_ja"], sum_ko=a["sum_ko"],
        slug=a["slug"])

idx = "blog/index.html"
s = open(idx, encoding="utf-8").read()
marker = '<div class="post-grid">\n'
assert marker in s, "post-grid 未找到"
for a in ARTICLES:
    assert a["slug"] not in s, "卡已存在：%s" % a["slug"]
s = s.replace(marker, marker + "\n" + cards, 1)
with open(idx, "w", encoding="utf-8", newline="") as f:
    f.write(s)
print("blog/index.html 插入 2 张卡片完成")
