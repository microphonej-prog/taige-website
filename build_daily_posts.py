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
        slug="clothing-label-compliance-colombia.html",
        body="blog/_body_col.html",
        title_zh="哥伦比亚服装标签合规指南：西语标签、成分与进口商信息 | TAGE",
        title_en="Colombia Clothing Label Requirements: Spanish Text, Fibre Content &amp; Importer Info | TAGE",
        title_fr="Étiquetage des vêtements en Colombie : espagnol, composition et importateur | TAGE",
        title_es="Requisitos de etiquetado de ropa en Colombia: español, composición e importador | TAGE",
        desc_zh="哥伦比亚服装标签合规指南：西班牙语永久标签、纤维成分百分比、原产国与进口商 NIT 信息、洗护说明要求，附童装安全要点、常见错误与打样验收清单，帮您在工厂端一次做对。来自东莞泰阁包装。",
        desc_en="Colombia clothing label rules: Spanish permanent labels, fibre content percentages, country of origin, importer NIT and care text, with a sampling checklist.",
        desc_fr="Etiquetage des vêtements en Colombie : étiquettes permanentes en espagnol, composition, origine, NIT de l'importateur et entretien, avec liste de contrôle.",
        desc_es="Etiquetado de ropa en Colombia: etiquetas permanentes en español, composición, origen, NIT del importador y cuidado, con lista de verificación.",
        crumb_zh="哥伦比亚标签合规",
        crumb_en="Colombia Label Rules",
        crumb_fr="Réglementation Colombie",
        crumb_es="Normativa Colombia",
        h1_zh="哥伦比亚服装标签合规指南：西语标签、成分与进口商信息",
        h1_en="Colombia Clothing Label Compliance: Spanish Text, Fibre Content and Importer Details",
        h1_fr="Conformité de l'étiquetage en Colombie : espagnol, composition et importateur",
        h1_es="Cumplimiento del etiquetado en Colombia: español, composición e importador",
        tag_zh="合规指南", tag_en="Compliance", tag_fr="Conformité", tag_es="Cumplimiento",
        sum_zh="哥伦比亚要求服装信息用西班牙语、永久附着，成分与洗护不能只写在吊牌上。本文梳理强制标注项目、纤维成分的降序写法与允许误差、洗护符号加西语短句的组合、童装绳带与小部件要求，并给出可抄进询价邮件的七步核对清单，帮您在工厂端把标签一次做对。",
        sum_en="Colombia requires Spanish, permanently attached information — composition and care cannot live on the hang tag alone. This guide covers mandatory items, descending fibre percentages and tolerances, symbols paired with Spanish wording, childrenswear cord and small-part rules, plus a seven-step checklist you can paste into a quotation request.",
        sum_fr="La Colombie exige des informations en espagnol fixées durablement : composition et entretien ne peuvent pas figurer uniquement sur l'étiquette suspendue. Ce guide couvre les mentions obligatoires, les pourcentages décroissants et tolérances, symboles et texte espagnol, exigences pour l'enfant, et une liste de contrôle en sept points.",
        sum_es="Colombia exige información en español y fijada de forma duradera: composición y cuidado no pueden ir solo en la etiqueta colgante. Esta guía cubre los datos obligatorios, porcentajes decrecientes y tolerancias, símbolos con texto en español, requisitos infantiles y una lista de verificación de siete pasos.",
    ),
    dict(
        slug="clothing-label-compliance-chile.html",
        body="blog/_body_chi.html",
        title_zh="智利服装标签合规指南：西语标注、耐久性与进口文件 | TAGE",
        title_en="Chile Clothing Label Requirements: Spanish Text, Durability &amp; Import Docs | TAGE",
        title_fr="Étiquetage des vêtements au Chili : espagnol, durabilité et import | TAGE",
        title_es="Requisitos de etiquetado de ropa en Chile: español, durabilidad e importación | TAGE",
        desc_zh="智利服装标签合规指南：西班牙语标注、进口商 RUT、三次家洗耐久性测试、Talla 尺码双标、洗护西语表述与报关文件一致性，附泳装童装要点与打样核对清单。来自东莞泰阁包装。",
        desc_en="Chile clothing label rules: Spanish text, importer RUT, three-wash durability, Talla sizing, care wording and customs consistency, plus a sampling checklist.",
        desc_fr="Etiquetage au Chili : texte espagnol, RUT de l'importateur, durabilité sur trois lavages, tailles Talla, entretien et cohérence douanière, avec liste de contrôle.",
        desc_es="Etiquetado en Chile: texto en español, RUT del importador, durabilidad a tres lavados, tallas Talla, cuidado y coherencia aduanera, con lista de verificación.",
        crumb_zh="智利标签合规",
        crumb_en="Chile Label Rules",
        crumb_fr="Réglementation Chili",
        crumb_es="Normativa Chile",
        h1_zh="智利服装标签合规指南：西语标注、耐久性与进口文件",
        h1_en="Chile Clothing Label Compliance: Spanish Text, Durability and Import Paperwork",
        h1_fr="Conformité de l'étiquetage au Chili : espagnol, durabilité et documents douaniers",
        h1_es="Cumplimiento del etiquetado en Chile: español, durabilidad y documentos de importación",
        tag_zh="合规指南", tag_en="Compliance", tag_fr="Conformité", tag_es="Cumplimiento",
        sum_zh="智利看的是「洗过还能读懂」：西班牙语标注、永久附着、信息与实物一致。本文说明进口商 RUT 与进口商标识怎么写、如何用三次家洗验证标签耐久性、Talla 本地码与国际码的双标做法，以及标签、吊牌、箱唛、发票四处一致性与原产地证配合，附泳装与童装要点。",
        sum_en="Chile asks one practical question: is the label still readable after washing? This guide explains importer RUT lines, how to prove durability with a three-wash test, how to mark Talla alongside international sizes, and how to keep label, hang tag, carton marks and invoice consistent — plus swimwear and childrenswear notes.",
        sum_fr="Le Chili pose une question pratique : l'étiquette reste-t-elle lisible après lavage ? Ce guide détaille la ligne RUT de l'importateur, la preuve de durabilité par trois lavages, le marquage Talla avec les tailles internationales, la cohérence étiquette / suspendue / cartons / facture, plus maillots et enfant.",
        sum_es="Chile plantea una pregunta práctica: ¿sigue legible la etiqueta tras lavar? Esta guía explica la línea con el RUT del importador, cómo probar la durabilidad con tres lavados, el marcado Talla junto a tallas internacionales y la coherencia etiqueta / colgante / caja / factura, además de baño e infantil.",
    ),
]

skel = open(SKEL, encoding="utf-8").read()
old3 = re.search(r'"position": 3,\s*"name": "([^"]*)"', skel).group(1)
print("骨架 breadcrumb 名:", old3)

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
assert ARTICLES[0]["slug"] not in s
s = s.replace(marker, marker + "\n" + cards, 1)
with open(idx, "w", encoding="utf-8", newline="") as f:
    f.write(s)
print("blog/index.html 插入 2 张卡片完成")
