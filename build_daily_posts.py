#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""按既有骨架生成当日两篇新文章（中文主文件）+ 在 blog/index.html 顶部插入两张卡片。"""
import re

SKEL = "blog/knitwear-sweater-trims-guide.html"
DATE_ZH = "2026年9月19日"
DATE_EN = "September 19, 2026"
DATE_FR = "19 septembre 2026"
DATE_ES = "19 de septiembre de 2026"

ARTICLES = [
    dict(
        slug="carton-shipping-mark-guide.html",
        body="blog/_body_cm.html",
        title_zh="服装出口外箱唛头与箱贴指南：正唛、侧唛与标记规范 | TAGE",
        title_en="Carton Shipping Marks for Garment Export: Main Mark &amp; Side Mark | TAGE",
        title_fr="Marques d'expédition des cartons à l'export textile : guide pratique | TAGE",
        title_es="Marcas de envío en cartones para exportar prendas: guía práctica | TAGE",
        desc_zh="出口外箱唛头与箱贴指南：正唛、侧唛与副唛的字段和位置，箱规与毛净重怎么填才不被客户仓库打回，直接印刷与不干胶贴标的成本对比，条码、运输图示与原产地标记规范，附下单前要确认的六个箱标细节。来自东莞泰阁包装。",
        desc_en="Carton shipping marks for garment export: main and side mark fields, carton sizes, direct print vs labels, barcodes and origin marks, plus a checklist.",
        desc_fr="Marques d'expédition des cartons à l'export textile : champs des marques principale et latérale, dimensions et poids, impression directe ou étiquettes, codes-barres et symboles de manutention.",
        desc_es="Marcas de envío en cartones para exportar prendas: campos de la marca principal y lateral, medidas y peso, impresión directa o etiquetas, códigos de barras y símbolos de manipulación.",
        crumb_zh="外箱唛头与箱贴",
        crumb_en="Carton Marking",
        crumb_fr="Marquage des cartons",
        crumb_es="Marcado de cartones",
        h1_zh="服装出口外箱唛头与箱贴指南：正唛、侧唛与标记规范",
        h1_en="Carton Shipping Marks for Garment Export: Main Mark, Side Mark and Labels",
        h1_fr="Marques d'expédition des cartons : marque principale, marque latérale et étiquettes",
        h1_es="Marcas de envío en cartones: marca principal, marca lateral y etiquetas",
        tag_zh="出口实务", tag_en="Export", tag_fr="Export", tag_es="Exportación",
        sum_zh="外箱唛头写错一个字段，可能让整批纸箱报废、被客户仓库拒收或在目的港重新贴标。本文讲清正唛、侧唛、副唛分别承载什么信息，箱规与毛净重为什么必须实测，直接印刷与不干胶箱贴怎么选，条码位置、原产地标记与运输图示的常见要求，并附下单前要确认的六个箱标细节。",
        sum_en="One wrong carton mark field can scrap an entire carton run, trigger a warehouse rejection or force repacking at destination. This guide covers what the main, side and additional marks carry, why carton size and gross weight must be measured, direct print versus self-adhesive labels, barcode placement, origin and handling symbols, and six details to confirm before ordering.",
        sum_fr="Un champ erroné sur la marque d'expédition peut faire mettre au rebut une série de cartons, provoquer un refus en entrepôt ou un ré-étiquetage au port. Ce guide couvre le contenu des marques principale, latérale et additionnelle, la nécessité de mesurer dimensions et poids, le choix entre impression directe et étiquettes adhésives, les codes-barres, l'origine et les symboles, avec six points à valider avant commande.",
        sum_es="Un campo erróneo en la marca de envío puede desechar una serie completa de cajas, provocar un rechazo en el almacén del cliente o un reetiquetado en destino. Esta guía explica qué llevan las marcas principal, lateral y adicional, por qué hay que medir medidas y pesos, impresión directa frente a etiquetas adhesivas, códigos de barras, origen y símbolos de manipulación, con seis detalles a confirmar antes de pedir.",
    ),
    dict(
        slug="prop65-apparel-trims-guide.html",
        body="blog/_body_p65.html",
        title_zh="加州 65 号提案与服装辅料：警示标签与风险物质怎么处理 | TAGE",
        title_en="California Prop 65 for Apparel and Trims: Warnings &amp; Risk Points | TAGE",
        title_fr="Proposition 65 de Californie et accessoires textiles : avertissements et risques | TAGE",
        title_es="Proposición 65 de California y accesorios de ropa: advertencias y riesgos | TAGE",
        desc_zh="加州 65 号提案与服装辅料合规：警示义务与安全港（NSRL/MADL）怎么理解，PVC 胶袋、电镀金属件、印刷油墨与铬鞣皮革的风险点与替换方向，标准与短式警示的写法，以及网购页面必须展示警示这一常被漏掉的要点。来自东莞泰阁包装。",
        desc_en="California Prop 65 for apparel and trims: the warning duty, safe harbour levels, PVC, metal, ink and leather risks, online sales rules, plus a checklist.",
        desc_fr="Proposition 65 et accessoires textiles : obligation d'avertissement et seuils de référence, risques liés au PVC, métaux plaqués, encres et cuir, formulation de l'avertissement et règles de vente en ligne.",
        desc_es="Proposición 65 y accesorios de ropa: deber de advertencia y niveles de referencia, riesgos en PVC, metales con baño, tintas y cuero, redacción de la advertencia y reglas de venta online.",
        crumb_zh="加州 Prop 65",
        crumb_en="California Prop 65",
        crumb_fr="Prop 65 Californie",
        crumb_es="Prop 65 California",
        h1_zh="加州 65 号提案与服装辅料：警示标签与风险物质怎么处理",
        h1_en="California Prop 65 for Apparel and Trims: Warning Labels and Risk Points",
        h1_fr="Proposition 65 de Californie et accessoires textiles : avertissements et points de risque",
        h1_es="Proposición 65 de California y accesorios de ropa: advertencias y puntos de riesgo",
        tag_zh="合规指南", tag_en="Compliance", tag_fr="Conformité", tag_es="Cumplimiento",
        sum_zh="加州 65 号提案不禁止产品销售，而是要求在消费者接触之前给出清晰合理的警示：不存在「Prop 65 认证」，只有检测报告与警示标签本身。本文讲清警示义务与安全港水平的判定逻辑、服装辅料常见的五类风险部位与替换方向、标准与短式警示的写法与位置、网购页面必须展示警示这一最容易漏掉的要求，以及采购端五步行动清单。",
        sum_en="California Prop 65 does not ban products; it requires a clear and reasonable warning before consumer exposure, and there is no such thing as a Prop 65 certificate — only test reports and the warning itself. This guide covers the warning duty and safe harbour levels, five risk points in apparel trims and how to substitute them, standard versus short-form warnings and where they go, the online-sales rule sellers most often miss, and a five-step buyer checklist.",
        sum_fr="La Proposition 65 n'interdit pas les produits : elle impose un avertissement clair et raisonnable avant l'exposition, et il n'existe pas de « certificat Prop 65 » — seulement des rapports d'essai et l'avertissement lui-même. Ce guide traite l'obligation et les seuils de référence, cinq points de risque dans les accessoires et leurs alternatives, l'avertissement standard ou court et son emplacement, la règle en ligne la plus souvent oubliée et une liste d'actions en cinq étapes.",
        sum_es="La Proposición 65 no prohíbe productos: exige una advertencia clara y razonable antes de la exposición, y no existe un «certificado Prop 65», solo informes de ensayo y la propia advertencia. Esta guía cubre el deber de advertencia y los niveles de referencia, cinco puntos de riesgo en accesorios y sus alternativas, la advertencia estándar o corta y su ubicación, la regla de venta online que más se olvida y una lista de cinco pasos para el comprador.",
    ),
]

skel = open(SKEL, encoding="utf-8").read()
old3 = re.search(r'"position": 3,\s*"name": "([^"]*)"', skel).group(1)
print("骨架 breadcrumb 名:", old3)

# 安全闸：同名 slug 若已存在（含各语言版本与 sitemap），说明选题撞车，直接报错
import os
for a in ARTICLES:
    for p in ("blog/%s" % a["slug"], "en/blog/%s" % a["slug"], "fr/blog/%s" % a["slug"], "es/blog/%s" % a["slug"]):
        if os.path.exists(p):
            raise SystemExit("选题撞车：%s 已存在，换选题！" % p)
    if ("/blog/%s</loc>" % a["slug"]) in open("sitemap.xml", encoding="utf-8").read():
        raise SystemExit("选题撞车：sitemap 已含 %s" % a["slug"])
print("选题全新，开始生成")

for a in ARTICLES:
    slug = a["slug"]
    s = skel.replace(SKEL.replace("blog/", ""), slug)

    # title（四语属性 + 中文静态内容）
    title_line = ('<title data-zh="%s" data-en="%s" data-fr="%s" data-es="%s">%s</title>'
                  % (a["title_zh"], a["title_en"], a["title_fr"], a["title_es"], a["title_zh"]))
    s = re.sub(r'<title[^>]*>.*?</title>', title_line, s, count=1, flags=re.S)

    # description（先清掉骨架的 data-en/fr/es 行，再整块替换）
    s = re.sub(r'<meta name="description".*?content="[^"]*">', 'DESC_PLACEHOLDER', s, count=1, flags=re.S)
    desc_block = ('<meta name="description" data-zh="%s"\n'
                  '      data-en="%s"\n'
                  '      data-fr="%s"\n'
                  '      data-es="%s"\n'
                  '      content="%s">' % (a["desc_zh"], a["desc_en"], a["desc_fr"], a["desc_es"], a["desc_zh"]))
    s = s.replace('DESC_PLACEHOLDER', desc_block, 1)

    # canonical + hreflang
    new_canon = ('<link rel="canonical" href="https://taigetag.com/blog/%s">\n'
                 '<link rel="alternate" hreflang="zh-CN" href="https://taigetag.com/blog/%s">\n'
                 '<link rel="alternate" hreflang="en" href="https://taigetag.com/en/blog/%s">\n'
                 '<link rel="alternate" hreflang="fr" href="https://taigetag.com/fr/blog/%s">\n'
                 '<link rel="alternate" hreflang="es" href="https://taigetag.com/es/blog/%s">\n'
                 '<link rel="alternate" hreflang="x-default" href="https://taigetag.com/blog/%s">'
                 % (slug, slug, slug, slug, slug, slug))
    s, n_href = re.subn(r'<link rel="canonical" href="[^"]*">(?:\n<link rel="alternate"[^\n]*>)+',
                        new_canon, s, count=1)
    assert n_href == 1, "hreflang 替换失败"

    # crumb
    crumb = ('<div class="crumb"><a href="../index.html" data-zh="首页" data-fr="Accueil" data-es="Inicio" data-en="Home">首页</a>'
             ' / <a href="index.html" data-zh="辅料 FAQ" data-fr="FAQ Accessoires" data-es="FAQ Accesorios" data-en="Trims FAQ">辅料 FAQ</a>'
             ' / <span data-zh="%s" data-en="%s" data-fr="%s" data-es="%s">%s</span></div>'
             % (a["crumb_zh"], a["crumb_en"], a["crumb_fr"], a["crumb_es"], a["crumb_zh"]))
    s, n = re.subn(r'<div class="crumb">.*?</div>', crumb, s, count=1, flags=re.S)
    assert n == 1, "crumb 替换失败"

    # h1
    h1 = ('<h1 data-zh="%s" data-en="%s" data-fr="%s" data-es="%s">%s</h1>'
          % (a["h1_zh"], a["h1_en"], a["h1_fr"], a["h1_es"], a["h1_zh"]))
    s, n = re.subn(r'<h1 .*?</h1>', h1, s, count=1, flags=re.S)
    assert n == 1, "h1 替换失败"

    # meta 行（日期）
    meta = ('<p data-zh="泰阁包装 · 更新于 %s" data-en="By TAGE Packaging &nbsp;·&nbsp; Updated %s" '
            'data-fr="Par TAGE Packaging &nbsp;·&nbsp; Mis à jour le %s" '
            'data-es="Por TAGE Packaging &nbsp;·&nbsp; Actualizado el %s">泰阁包装 · 更新于 %s</p>'
            % (DATE_ZH, DATE_EN, DATE_FR, DATE_ES, DATE_ZH))
    s, n = re.subn(r'<p data-zh="泰阁包装 · 更新于[^"]*".*?</p>', meta, s, count=1, flags=re.S)
    assert n == 1, "meta 行替换失败"

    # JSON-LD：breadcrumb 名与 headline
    s = s.replace('"%s"' % old3, '"%s"' % a["h1_zh"])
    s, n = re.subn(r'"headline": "[^"]*"', '"headline": "%s"' % a["h1_zh"], s, count=1)
    assert n == 1, "headline 替换失败"

    # 正文整段替换
    body = open(a["body"], encoding="utf-8").read().rstrip("\n")
    i0 = s.index('  <section class="article-body">')
    i1 = s.index('\n</main>')
    s = s[:i0] + body + s[i1:]

    out = "blog/%s" % slug
    with open(out, "w", encoding="utf-8", newline="") as f:
        f.write(s)
    print("写入 %s (%d 字节)  desc_en=%d 字符  desc_fr=%d  desc_es=%d  desc_zh=%d 字符"
          % (out, len(s.encode("utf-8")), len(a["desc_en"]), len(a["desc_fr"]), len(a["desc_es"]), len(a["desc_zh"])))

# ---------- blog/index.html 顶部插入两张卡片 ----------
CARD = '''      <article class="post-card">
        <span class="tag" data-zh="{tag_zh}" data-en="{tag_en}" data-fr="{tag_fr}" data-es="{tag_es}">{tag_zh}</span>
        <h3 data-zh="{h3_zh}" data-en="{h3_en}" data-fr="{h3_fr}" data-es="{h3_es}">{h3_zh}</h3>
        <p data-zh="{sum_zh}" data-en="{sum_en}" data-fr="{sum_fr}" data-es="{sum_es}">{sum_zh}</p>
        <a class="more" href="{slug}" data-zh="阅读全文 →" data-en="Read more →" data-fr="Lire la suite →" data-es="Leer más →">阅读全文 →</a>
      </article>

'''

cards = ""
for a in ARTICLES:
    cards += CARD.format(
        tag_zh=a["tag_zh"], tag_en=a["tag_en"], tag_fr=a["tag_fr"], tag_es=a["tag_es"],
        h3_zh=a["h1_zh"], h3_en=a["h1_en"], h3_fr=a["h1_fr"], h3_es=a["h1_es"],
        sum_zh=a["sum_zh"], sum_en=a["sum_en"], sum_fr=a["sum_fr"], sum_es=a["sum_es"],
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
