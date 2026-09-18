#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""按既有骨架生成当日两篇新文章（中文主文件）+ 在 blog/index.html 顶部插入两张卡片。"""
import re

SKEL = "blog/garment-trims-cost-saving-guide.html"
DATE_ZH = "2026年9月18日"
DATE_EN = "September 18, 2026"
DATE_FR = "18 septembre 2026"
DATE_ES = "18 de septiembre de 2026"

ARTICLES = [
    dict(
        slug="knitwear-sweater-trims-guide.html",
        body="blog/_body_a1.html",
        title_zh="针织毛衣类服装辅料指南：主唛、洗水标与包装怎么选 | TAGE",
        title_en="Knitwear Trims Guide: Neck Labels, Care Labels &amp; Packaging | TAGE",
        title_fr="Accessoires pour maille et pull : label de col, étiquette d'entretien et emballage | TAGE",
        title_es="Accesorios para punto y jerséis: etiqueta de cuello, de cuidado y embalaje | TAGE",
        desc_zh="针织毛衣辅料指南：主唛怎么选才不刮皮肤、洗水标四种材质与耐洗表现对比、吊牌吊绳如何避免钩丝，以及防潮防压防蛀的包装要求，附可直接抄进询价邮件的规格确认表与五步打样验收清单。来自东莞泰阁包装。",
        desc_en="Knitwear trims: soft neck labels that do not scratch, care label materials and wash performance, hang tags without snagging, packing tips and a spec sheet.",
        desc_fr="Guide des accessoires pour maille : labels de col doux, matériaux d'étiquettes d'entretien et tenue au lavage, étiquettes suspendues sans accroche, emballage et fiche de spécifications.",
        desc_es="Guía de accesorios para punto: etiquetas de cuello suaves, materiales de etiquetas de cuidado y lavado, etiquetas colgantes sin enganches, embalaje y ficha de especificaciones.",
        crumb_zh="针织毛衣辅料指南",
        crumb_en="Knitwear Trims Guide",
        crumb_fr="Guide accessoires maille",
        crumb_es="Guía de accesorios para punto",
        h1_zh="针织与毛衣类服装辅料指南：柔软、耐洗、不钩丝",
        h1_en="Knitwear Trims: Soft Labels That Survive Washing Without Snagging",
        h1_fr="Accessoires de maille : souples, résistants au lavage, sans accroche",
        h1_es="Accesorios de punto: suaves, resistentes al lavado y sin enganches",
        tag_zh="针织品类", tag_en="Knitwear", tag_fr="Maille", tag_es="Punto",
        sum_zh="针织面料由线圈构成，怕硬边、怕钩丝，洗后还会收缩起绒。本文按主唛、洗水标、吊牌吊绳、包装四部分拆解针织款辅料要求：材质与边缘处理、缩率匹配、四种洗水标材质对比、吊绳与扣件选型，并给出可直接抄进询价邮件的规格确认表和五步打样验收清单。",
        sum_en="Knitted fabric is built from loops that snag on hard edges and shrink after washing. This guide breaks knitwear trims into four parts — neck label, care label, hang tag and string, packing — covering material and edge treatment, shrinkage matching, four care label types compared, and string and fastener selection, with a spec sheet and a five-step sampling check.",
        sum_fr="La maille est faite de boucles qui s'accrochent aux bords rigides et se rétractent au lavage. Ce guide décompose les accessoires de maille en quatre parties — label de col, étiquette d'entretien, étiquette suspendue et cordon, emballage — avec matières et bords, retrait assorti, comparaison de quatre types d'étiquettes d'entretien, choix du cordon et de la fixation, fiche de spécifications et contrôle d'échantillon.",
        sum_es="El punto se forma con bucles que se enganchan en bordes rígidos y encogen al lavar. Esta guía divide los accesorios de punto en cuatro partes — etiqueta de cuello, de cuidado, colgante con cordón y embalaje — con materiales y bordes, encogimiento compatible, comparativa de cuatro tipos de etiqueta de cuidado, elección de cordón y cierre, ficha de especificaciones y control de muestra.",
    ),
    dict(
        slug="outerwear-down-jacket-trims-guide.html",
        body="blog/_body_a2.html",
        title_zh="外套与羽绒服辅料指南：洗水警示、吊粒承重与防钻绒包装 | TAGE",
        title_en="Outerwear &amp; Down Jacket Trims: Care Warnings, Tag Load &amp; Packing | TAGE",
        title_fr="Accessoires pour vestes et doudounes : avertissements, fixation et emballage | TAGE",
        title_es="Accesorios para abrigos y plumíferos: avisos, sujeción y embalaje | TAGE",
        desc_zh="外套与羽绒服辅料指南：洗水标警示语怎么与面料测试对齐、主唛缝在里布而非涂层、吊牌吊粒按整件重量选型、包装如何防钻绒防潮少压缩，并附出口外箱与唛头要点、规格确认表和验收清单。来自东莞泰阁包装。",
        desc_en="Outerwear trims guide: care label warnings matched to fabric tests, neck labels on linings, hang tag load, and packing that prevents down leakage and moisture.",
        desc_fr="Guide des accessoires pour vestes et doudounes : avertissements d'entretien alignés sur les tests, labels de col sur doublure, résistance de l'étiquette suspendue, emballage anti-fuite et anti-humidité.",
        desc_es="Guía de accesorios para abrigos y plumíferos: avisos de cuidado según ensayos, etiquetas de cuello en el forro, carga de la etiqueta colgante, embalaje sin fugas de plumón ni humedad.",
        crumb_zh="外套羽绒辅料指南",
        crumb_en="Outerwear Trims Guide",
        crumb_fr="Guide accessoires veste",
        crumb_es="Guía de accesorios para abrigos",
        h1_zh="外套与羽绒服辅料指南：警示、承重与包装",
        h1_en="Outerwear and Down Jacket Trims: Warnings, Load and Packing",
        h1_fr="Accessoires de veste et doudoune : avertissements, résistance, emballage",
        h1_es="Accesorios para abrigos y plumíferos: avisos, carga y embalaje",
        tag_zh="外套品类", tag_en="Outerwear", tag_fr="Veste", tag_es="Abrigos",
        sum_zh="外套与羽绒服辅料的第一诉求是耐洗、警示与承重。本文说明主唛为何缝在里布而非涂层、四类面料的洗水警示语方向、吊牌吊粒如何按整件重量选型、包装怎样防钻绒防潮又不过度压缩，并附出口外箱与唛头要点、规格确认表与验收清单。",
        sum_en="For outerwear the trims must wash, warn and bear load. This guide explains why neck labels go on the lining rather than the coating, how care warnings differ across four fabric types, how to size hang tag strings and fasteners against garment weight, and how to pack against down leakage and moisture without over-compressing — plus export carton and marking notes, a spec sheet and acceptance checks.",
        sum_fr="Pour la veste, l'accessoire doit tenir au lavage, avertir et résister. Ce guide explique pourquoi le label de col se coud sur la doublure, comment les avertissements varient selon quatre types de tissu, comment dimensionner cordon et fixation au poids de la pièce, et comment emballer contre la fuite de duvet et l'humidité sans sur-comprimer — avec cartons export, fiche de spécifications et contrôles de réception.",
        sum_es="En abrigos, el accesorio debe lavarse bien, avisar y soportar carga. Esta guía explica por qué la etiqueta de cuello va en el forro, cómo cambian los avisos según cuatro tipos de tejido, cómo elegir cordón y cierre por el peso de la prenda y cómo embalar contra fugas de plumón y humedad sin comprimir en exceso, con cajas de exportación, ficha de especificaciones y controles de recepción.",
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
s = open(idx, encoding="utf-8").read()
marker = '<div class="post-grid">\n'
assert marker in s, "post-grid 未找到"
assert ARTICLES[0]["slug"] not in s
s = s.replace(marker, marker + "\n" + cards, 1)
with open(idx, "w", encoding="utf-8", newline="") as f:
    f.write(s)
print("blog/index.html 插入 2 张卡片完成")
