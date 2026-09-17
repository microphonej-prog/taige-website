#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""按既有骨架生成当日两篇新文章（中文主文件）+ 在 blog/index.html 顶部插入两张卡片。"""
import re

SKEL = "blog/uniform-workwear-labeling-guide.html"
DATE_ZH = "2026年9月17日"
DATE_EN = "September 17, 2026"
DATE_FR = "17 septembre 2026"
DATE_ES = "17 de septiembre de 2026"

ARTICLES = [
    dict(
        slug="garment-trims-supplier-audit.html",
        body="blog/_body_a1.html",
        title_zh="服装辅料供应商验厂指南：现场该看什么、该问什么 | TAGE",
        title_en="How to Audit a Garment Trims Supplier: On-Site Checklist &amp; Red Flags | TAGE",
        title_fr="Auditer un fournisseur d'accessoires de vêtements : que vérifier sur place | TAGE",
        title_es="Cómo auditar a un proveedor de accesorios de confección: qué revisar | TAGE",
        desc_zh="服装辅料供应商验厂指南：从主体资质、设备产能、工序自制率、QC 体系到仓储留样与环保合规，说明现场要看什么、该问哪十个问题、七条危险信号，并给出远程验厂三步法与可复用评分表。来自东莞泰阁包装。",
        desc_en="Garment trims supplier audit guide: what to inspect in a factory, which questions to ask, red flags to watch, and how to run a remote audit with a scorecard.",
        desc_fr="Guide d'audit d'un fournisseur d'accessoires : ce qu'il faut vérifier en usine, les questions à poser, les signaux d'alerte et l'audit à distance avec grille d'évaluation.",
        desc_es="Guía para auditar a un proveedor de accesorios de confección: qué verificar en fábrica, qué preguntar, señales de alarma y auditoría remota con plantilla de evaluación.",
        crumb_zh="辅料供应商验厂指南",
        crumb_en="Trims Supplier Audit",
        crumb_fr="Audit de fournisseur d'accessoires",
        crumb_es="Auditoría de proveedores de accesorios",
        h1_zh="服装辅料供应商验厂指南：现场该看什么、该问什么",
        h1_en="How to Audit a Garment Trims Supplier: What to Check On-Site",
        h1_fr="Auditer un fournisseur d'accessoires : que vérifier sur place",
        h1_es="Cómo auditar a un proveedor de accesorios: qué revisar en planta",
        tag_zh="供应链管理", tag_en="Supply Chain", tag_fr="Chaîne d'approvisionnement", tag_es="Cadena de suministro",
        sum_zh="验厂不是参观样板间。本文给出一份可以直接带去工厂的清单：主体资质、设备与产能、工序自制率、QC 与检测、仓储留样、合规环保六个维度，十个该当面问的问题，七条危险信号，以及无法到场时的远程验厂三步法和可复用评分表。",
        sum_en="An audit is more than a showroom tour. This guide gives you a checklist to take to the factory: six dimensions to inspect (entity, equipment, in-house processes, QC, storage, compliance), ten questions to ask face to face, seven red flags, and a three-step remote audit with a scorecard.",
        sum_fr="Un audit n'est pas une visite de showroom. Ce guide fournit une liste à emporter en usine : six dimensions à vérifier (entité, machines, intégration, contrôle qualité, stockage, conformité), dix questions à poser, sept signaux d'alerte et un audit à distance en trois étapes avec grille d'évaluation.",
        sum_es="Una auditoría no es visitar un showroom. Esta guía ofrece una lista para llevar a la fábrica: seis dimensiones que revisar (entidad, máquinas, integración, control de calidad, almacén, cumplimiento), diez preguntas que hacer, siete señales de alarma y una auditoría remota en tres pasos con plantilla.",
    ),
    dict(
        slug="garment-trims-cost-saving-guide.html",
        body="blog/_body_a2.html",
        title_zh="服装辅料降本指南：不牺牲品质的 8 个方向 | TAGE",
        title_en="Garment Trims Cost Reduction: 8 Ways to Save Without Losing Quality | TAGE",
        title_fr="Réduire le coût des accessoires de vêtements : 8 leviers sans perdre en qualité | TAGE",
        title_es="Reducir el coste de accesorios de confección: 8 vías sin perder calidad | TAGE",
        desc_zh="服装辅料降本指南：从规格合理化、工艺替代、拼版套版、数量与排期、SKU 精简到包装物流，整理八个不牺牲品质的降本方向，并列出五种会在售后加倍还回来的伪降本。来自东莞泰阁包装。",
        desc_en="Garment trims cost reduction guide: eight levers that cut cost without losing quality — specification, process substitution, imposition, volumes and SKU pruning.",
        desc_fr="Guide de réduction des coûts des accessoires : huit leviers qui réduisent le coût sans sacrifier la qualité — spécifications, procédés, imposition, quantités et références.",
        desc_es="Guía para reducir el coste de los accesorios: ocho palancas que recortan costes sin perder calidad — especificaciones, procesos, imposición, cantidades y referencias.",
        crumb_zh="辅料降本指南",
        crumb_en="Trims Cost Reduction",
        crumb_fr="Réduction des coûts accessoires",
        crumb_es="Reducción de costes de accesorios",
        h1_zh="服装辅料降本指南：不牺牲品质的 8 个方向",
        h1_en="Garment Trims Cost Reduction: 8 Levers That Keep Quality",
        h1_fr="Réduire le coût des accessoires : 8 leviers sans perdre en qualité",
        h1_es="Reducir el coste de los accesorios: 8 palancas sin perder calidad",
        tag_zh="成本优化", tag_en="Cost Control", tag_fr="Maîtrise des coûts", tag_es="Control de costes",
        sum_zh="辅料降本不等于压价。本文从规格合理化、工艺替代、拼版套版、数量与排期、SKU 精简到包装物流，整理八个真实可行的降本方向，并列出五种会在售后加倍还回来的伪降本，附一次 30 分钟的规格复盘步骤。",
        sum_en="Cost reduction is not price pressure. This guide sets out eight workable levers — specification review, process substitution, imposition, volumes and scheduling, SKU pruning, packing and logistics — plus five false economies that return doubled in after-sales.",
        sum_fr="Réduire les coûts n'est pas écraser les prix. Ce guide présente huit leviers applicables — spécifications, substitution de procédés, imposition, quantités, réduction des références, emballage et logistique — et cinq fausses économies qui reviennent multipliées après-vente.",
        sum_es="Reducir costes no es apretar el precio. Esta guía recoge ocho palancas aplicables — especificaciones, sustitución de procesos, imposición, cantidades, reducción de referencias, embalaje y logística — y cinco falsos ahorros que vuelven multiplicados en posventa.",
    ),
]

skel = open(SKEL, encoding="utf-8").read()
old3 = re.search(r'"position": 3,\s*"name": "([^"]*)"', skel).group(1)
print("骨架 breadcrumb 名:", old3)

for a in ARTICLES:
    slug = a["slug"]
    s = skel.replace("uniform-workwear-labeling-guide.html", slug)

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
    print("写入 %s (%d 字节)  desc_en=%d 字符  desc_zh=%d 字符"
          % (out, len(s.encode("utf-8")), len(a["desc_en"]), len(a["desc_zh"])))

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
s = open(idx, encoding="utf-8", newline="").read()
marker = '<div class="post-grid">\n'
assert marker in s, "post-grid 未找到"
assert ARTICLES[0]["slug"] not in s
s = s.replace(marker, marker + "\n" + cards, 1)
with open(idx, "w", encoding="utf-8", newline="") as f:
    f.write(s)
print("blog/index.html 插入 2 张卡片完成")
