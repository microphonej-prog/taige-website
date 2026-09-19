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
        slug="clothing-label-compliance-peru.html",
        body="blog/_body_peru.html",
        title_zh="秘鲁服装标签合规指南：西语标注、成分与 RUC 要求 | TAGE",
        title_en="Peru Clothing Label Requirements: Spanish Text, Fibre Content &amp; RUC | TAGE",
        title_fr="Étiquetage des vêtements au Pérou : espagnol, composition et RUC | TAGE",
        title_es="Requisitos de etiquetado de ropa en Perú: español, composición y RUC | TAGE",
        desc_zh="秘鲁服装标签合规指南：永久标须标注纤维成分、洗护说明与原产地，责任方还要写明法定地址与 RUC 税号。讲清 5% 与 15% 成分分组线、±3% 公差、ISO 3758 洗涤符号与 Hecho en 产地写法，附打样清单。来自东莞泰阁包装。",
        desc_en="Peru clothing label rules: fibre content on the permanent label, ISO 3758 care symbols, origin wording, and the responsible party's RUC and legal domicile.",
        desc_fr="Étiquetage au Pérou : composition, symboles ISO 3758, origine, RUC et domicile légal du responsable, groupement des fibres à 5 % et 15 %, avec liste de contrôle.",
        desc_es="Etiquetado en Perú: composición, símbolos ISO 3758, origen, RUC y domicilio legal del responsable, agrupación de fibras al 5 % y 15 %, con lista de verificación.",
        crumb_zh="秘鲁标签合规",
        crumb_en="Peru Label Rules",
        crumb_fr="Étiquetage au Pérou",
        crumb_es="Etiquetado en Perú",
        h1_zh="秘鲁服装标签合规指南：西语标注、成分与 RUC 要求",
        h1_en="Peru Clothing Label Requirements: Spanish Text, Fibre Content and RUC",
        h1_fr="Étiquetage des vêtements au Pérou : espagnol, composition et RUC",
        h1_es="Requisitos de etiquetado de ropa en Perú: español, composición y RUC",
        tag_zh="合规指南", tag_en="Compliance", tag_fr="Conformité", tag_es="Cumplimiento",
        sum_zh="秘鲁的服装标签是两套规则的叠加：安第斯成衣标签法规管成分、洗护说明与原产地，秘鲁本国标签法要求把责任方的名称、法定地址与 RUC 税号写进标签。本文讲清永久标与可拆标的分工、5% 与 15% 的成分分组线、±3% 混纺公差、ISO 3758:2012 洗涤符号对齐、Hecho en 产地写法，以及不设前置认证但由 INDECOPI 在市场端查处的逻辑，附打样前六项核对清单。",
        sum_en="Peru layers two rules on one label: the Andean garment labelling rule covers fibre content, care and origin, while Peru's industrial labelling law requires the responsible party's name, legal domicile and RUC tax number. This guide sets out permanent versus removable label duties, the 5% and 15% composition lines and ±3% blend tolerance, ISO 3758:2012 symbol alignment, Hecho en origin wording, the no-pre-certification but INDECOPI-enforced model, and a six-point sampling checklist.",
        sum_fr="Le Pérou superpose deux règles sur une même étiquette : la règle andine couvre composition, entretien et origine, tandis que la loi péruvienne exige nom, domicile légal et RUC du responsable. Ce guide détaille étiquette permanente et amovible, seuils de composition à 5 % et 15 %, tolérance de ±3 %, symboles ISO 3758:2012, formulation de l'origine Hecho en, l'absence de certification préalable mais le contrôle de l'INDECOPI, et six points à vérifier avant échantillon.",
        sum_es="Perú superpone dos normas en una etiqueta: la norma andina cubre composición, cuidado y origen, y la ley peruana exige nombre, domicilio legal y RUC del responsable. Esta guía detalla etiqueta permanente y removible, los umbrales del 5 % y 15 % y la tolerancia de ±3 %, los símbolos ISO 3758:2012, la redacción Hecho en, el modelo sin certificación previa pero con control de INDECOPI y seis puntos a verificar antes de la muestra.",
    ),
    dict(
        slug="clothing-label-compliance-argentina.html",
        body="blog/_body_arg.html",
        title_zh="阿根廷服装标签合规指南：西语标注、CUIT 与 Mercosur 要求 | TAGE",
        title_en="Argentina Clothing Label Requirements: Spanish, CUIT &amp; Mercosur | TAGE",
        title_fr="Étiquetage des vêtements en Argentine : espagnol, CUIT et Mercosur | TAGE",
        title_es="Requisitos de etiquetado de ropa en Argentina: español, CUIT y Mercosur | TAGE",
        desc_zh="阿根廷服装标签合规指南：2024 年新规取消上市前的成分申报，出口商信息变为可选、进口商可用 CUIT 代替名称，但 Mercosur 法规要求的成分、原产地、护理说明与进口商信息仍在。讲清西语术语与打样核对清单。来自东莞泰阁包装。",
        desc_en="Argentina clothing label rules: what Resolución 49/2024 changed, CUIT in place of the importer name, and the Mercosur fibre, origin and care requirements.",
        desc_fr="Étiquetage en Argentine : ce que change la Resolución 49/2024, CUIT à la place du nom de l'importateur, et les exigences Mercosur sur composition, origine et entretien.",
        desc_es="Etiquetado en Argentina: qué cambia la Resolución 49/2024, el CUIT en lugar del nombre del importador y las exigencias Mercosur de composición, origen y cuidado.",
        crumb_zh="阿根廷标签合规",
        crumb_en="Argentina Label Rules",
        crumb_fr="Étiquetage en Argentine",
        crumb_es="Etiquetado en Argentina",
        h1_zh="阿根廷服装标签合规指南：西语标注、CUIT 与 Mercosur 要求",
        h1_en="Argentina Clothing Label Requirements: Spanish Text, CUIT and Mercosur",
        h1_fr="Étiquetage des vêtements en Argentine : espagnol, CUIT et Mercosur",
        h1_es="Requisitos de etiquetado de ropa en Argentina: español, CUIT y Mercosur",
        tag_zh="合规指南", tag_en="Compliance", tag_fr="Conformité", tag_es="Cumplimiento",
        sum_zh="阿根廷 2024 年的新规把进口纺织服装上市前的成分申报（DJCP）取消了，出口商信息变成可选，进口商名称也可以用 CUIT 税号代替——但 Mercosur 纺织标签技术法规要求的纤维成分、原产地、护理说明与国内进口商信息都没变，且文字必须是西班牙语。本文讲清西语术语与标签写法、成分一致性的把控口径、到货前贴标与报关资料一致性，以及打样核对清单。",
        sum_en="Argentina's 2024 revision dropped the pre-market composition filing (DJCP), made exporter identification optional and allowed the importer's CUIT tax number in place of its name — but the Mercosur technical regulation still requires fibre composition, origin, care instructions and the domestic importer details, in Spanish. This guide covers Spanish terminology and label wording, keeping composition consistent, labelling before arrival with matching customs documents, and a sampling checklist.",
        sum_fr="La révision argentine de 2024 a supprimé la déclaration de composition (DJCP) avant commercialisation, rendu l'exportateur facultatif et permis le CUIT à la place du nom de l'importateur — mais le règlement Mercosur impose toujours composition, origine, entretien et coordonnées de l'importateur local, en espagnol. Ce guide traite la terminologie espagnole, la cohérence de composition, l'étiquetage avant arrivée, la cohérence douanière et la liste de contrôle.",
        sum_es="La revisión argentina de 2024 eliminó la declaración jurada de composición (DJCP) previa a la comercialización, hizo opcional la identificación del exportador y permitió el CUIT en lugar del nombre del importador, pero el reglamento Mercosur sigue exigiendo composición, origen, cuidado y datos del importador local, en español. Esta guía trata la terminología, la coherencia de composición, el etiquetado antes de la llegada, la coherencia aduanera y la lista de verificación.",
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
