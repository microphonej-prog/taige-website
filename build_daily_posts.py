#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""按既有骨架生成当日两篇新文章（中文主文件）+ 在 blog/index.html 顶部插入两张卡片。"""
import re

SKEL = "blog/knitwear-sweater-trims-guide.html"
DATE_ZH = "2026年9月18日"
DATE_EN = "September 18, 2026"
DATE_FR = "18 septembre 2026"
DATE_ES = "18 de septiembre de 2026"

ARTICLES = [
    dict(
        slug="metal-trims-nickel-release-guide.html",
        body="blog/_body_ni.html",
        title_zh="金属辅料镍释放合规指南：金属扣、撞钉与鸡眼怎么选 | TAGE",
        title_en="Nickel Release in Metal Trims: Buckles, Rivets &amp; Eyelets | TAGE",
        title_fr="Libération de nickel des accessoires métalliques : boucles, rivets et œillets | TAGE",
        title_es="Liberación de níquel en accesorios metálicos: hebillas, remaches y ojales | TAGE",
        desc_zh="金属辅料镍释放合规指南：金属扣、撞钉、鸡眼与金属吊粒的镍风险来源，无镍电镀与材质替代方案，EN 1811 与 EN 12472 测试逻辑，以及采购端要写进规格书的五件事。来自东莞泰阁包装。",
        desc_en="Nickel release in metal trims: which buckles, rivets and eyelets fall under REACH limits, nickel-free plating options, test methods and spec-sheet advice.",
        desc_fr="Libération de nickel dans les accessoires métalliques : quelles pièces entrent dans le champ REACH, placage sans nickel, essais et cahier des charges.",
        desc_es="Liberación de níquel en accesorios metálicos: qué piezas entran en REACH, baños sin níquel, ensayos y ficha técnica.",
        crumb_zh="镍释放合规",
        crumb_en="Nickel Release Rules",
        crumb_fr="Réglementation nickel",
        crumb_es="Normativa del níquel",
        h1_zh="金属辅料镍释放合规指南：金属扣、撞钉与鸡眼怎么选",
        h1_en="Nickel Release in Metal Trims: Choosing Buckles, Rivets and Eyelets",
        h1_fr="Libération de nickel : choisir boucles, rivets et œillets métalliques",
        h1_es="Liberación de níquel: elegir hebillas, remaches y ojales metálicos",
        tag_zh="合规指南", tag_en="Compliance", tag_fr="Conformité", tag_es="Cumplimiento",
        sum_zh="法规不禁止含镍，只限制长期接触皮肤部件的镍析出量（常见表述为 0.2 µg/cm² 每周）。本文讲清哪些金属辅料在范围内、锌合金电镀件与黄铜件的风险来源、无镍电镀与塑料替代方案，以及 EN 1811 与 EN 12472 的测试逻辑和采购端要写进规格书的五件事。",
        sum_en="The rules do not ban nickel, they cap release from parts in prolonged skin contact (commonly 0.2 µg/cm² per week). This guide shows which metal trims are in scope, where plated zinc alloy and brass create risk, how nickel-free plating and plastic alternatives work, and what to write into the spec sheet.",
        sum_fr="La règle n'interdit pas le nickel, elle limite sa libération pour les pièces en contact prolongé avec la peau (souvent 0,2 µg/cm² par semaine). Ce guide indique les accessoires concernés, l'origine du risque sur zinc allié plaqué et laiton, les solutions sans nickel et les essais EN 1811 et EN 12472.",
        sum_es="La norma no prohíbe el níquel, limita su liberación en piezas en contacto prolongado con la piel (habitualmente 0,2 µg/cm² por semana). Esta guía indica qué accesorios están dentro del alcance, el origen del riesgo en zinc aleado y latón, las alternativas sin níquel y los ensayos EN 1811 y EN 12472.",
    ),
    dict(
        slug="tissue-paper-wrapping-guide.html",
        body="blog/_body_tp.html",
        title_zh="服装薄纸包装指南：雪梨纸、拷贝纸的克重与印刷选择 | TAGE",
        title_en="Tissue Paper Wrapping Guide for Apparel: Weights &amp; Printing | TAGE",
        title_fr="Papier de soie pour vêtements : grammages, impression et fermeture | TAGE",
        title_es="Papel de seda para ropa: gramajes, impresión y sellado | TAGE",
        desc_zh="服装薄纸包装指南：雪梨纸、拷贝纸、牛皮薄纸与无酸纸的克重（14-30g）与用途对比，无酸与色牢度风险、印刷与封口搭配，以及询价时要写明的六个规格。来自东莞泰阁包装。",
        desc_en="Tissue paper wrapping for apparel: 14-30gsm options compared, acid-free and colour fastness risks, printing and sealing choices, plus six specs to quote on.",
        desc_fr="Papier de soie pour vêtements : options de 14 à 30 g/m² comparées, sans-acide et solidité des teintes, impression, fermeture et six spécifications.",
        desc_es="Papel de seda para ropa: opciones de 14 a 30 g/m², libre de ácido y solidez del color, impresión, sellado y seis especificaciones clave.",
        crumb_zh="薄纸包装",
        crumb_en="Tissue Wrapping",
        crumb_fr="Papier de soie",
        crumb_es="Papel de seda",
        h1_zh="服装薄纸包装指南：雪梨纸、拷贝纸的克重与印刷选择",
        h1_en="Tissue Paper Wrapping for Apparel: Grammage, Printing and Sealing",
        h1_fr="Papier de soie pour vêtements : grammage, impression et fermeture",
        h1_es="Papel de seda para ropa: gramaje, impresión y sellado",
        tag_zh="包装指南", tag_en="Packaging", tag_fr="Emballage", tag_es="Embalaje",
        sum_zh="薄纸是服装包装里感知成本比最高的一层：14-17g 用于隔层填充，22-30g 用于外露包裹与礼盒内衬，浅色与真丝类长期存放建议无酸纸。本文对比四种薄纸的克重与用途，讲清色牢度风险、压印与封口贴的搭配，并列出询价时必须写明的六个规格。",
        sum_en="Tissue is the best perceived-value layer in apparel packaging: 14-17 gsm for interleaving and filling, 22-30 gsm for visible wrapping and gift liners, acid-free for light and silk garments in long storage. This guide compares the four papers and lists the six specs to state on a quote request.",
        sum_fr="Le papier de soie offre le meilleur rapport valeur perçue : 14-17 g/m² pour l'intercalaire et le garnissage, 22-30 g/m² pour l'emballage visible et les boîtes, sans acide pour les pièces claires et la soie. Ce guide compare les quatre papiers et liste les six spécifications à indiquer.",
        sum_es="El papel de seda ofrece la mejor relación valor percibido: 14-17 g/m² para intercalado y relleno, 22-30 g/m² para envoltura visible y cajas, libre de ácido para prendas claras y seda. Esta guía compara los cuatro papeles y enumera las seis especificaciones a indicar.",
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

# 安全闸已在生成前执行（见文件开头）
s = s.replace(marker, marker + "\n" + cards, 1)
with open(idx, "w", encoding="utf-8", newline="") as f:
    f.write(s)
print("blog/index.html 插入 2 张卡片完成")
