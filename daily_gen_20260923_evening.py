#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-09-23 晚间 每日更新：2 篇新文章（六语：zh-Hant 根 / en / ja / ko / fr / es）
- 袜子与针织小件辅料指南：袜标工艺、尺码按脚长、吊卡与成对包装
- 帽子围巾手套配饰辅料指南：成分标、头围与掌围尺码、长条标签缝位与礼盒
（主题池 30 个选题均已上线，本次为品类扩展新选题，不与既有文章重复）

用法: python daily_gen_20260923_evening.py
"""
import os, re, sys, subprocess, importlib.util

ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)
PY = sys.executable

SKEL = "blog/knitwear-sweater-trims-guide.html"
DATE_ZH = "2026年9月23日"
DATE_EN = "September 23, 2026"
DATE_JA = "2026年9月23日更新"
DATE_KO = "2026년 9월 23일 업데이트"
DATE_FR = "23 septembre 2026"
DATE_ES = "23 de septiembre de 2026"
SITEMAP_DATE = "2026-09-23"
BUST_OLD, BUST_NEW = "103", "104"
LANGS = ["en", "ja", "ko", "fr", "es"]

ARTICLES = [
    dict(
        slug="sock-hosiery-trims-guide.html",
        body="blog/_body_socks.html",
        title_zh="袜子与针织小件辅料指南：袜标工艺、尺码标与吊卡包装 | TAGE",
        title_en="Sock and Hosiery Trims Guide: Labels, Sizing and Card Packaging | TAGE",
        title_ja="靴下・ニット小物の副資材ガイド：ラベル仕様・サイズ・カード包装 | TAGE",
        title_ko="양말·니트 소품 부자재 가이드: 라벨 사양, 사이즈, 카드 포장 | TAGE",
        title_fr="Guide des accessoires pour chaussettes : labels, tailles et cartes | TAGE",
        title_es="Guía de accesorios para calcetines: etiquetas, tallas y tarjetas | TAGE",
        desc_zh="袜子与针织小件辅料指南：讲清袜标该选织唛还是热转印无感标、尺码按脚长与欧码怎么写、吊卡尺寸如何配合折叠方式、成对包装与多双礼盒怎么配比，附询价规格表与五步验收清单。来自东莞泰阁包装。",
        desc_en="Sock and small knitwear trims guide: woven or tagless heat-transfer labels, size labelling by foot length, sock card sizing, pair packaging and five acceptance checks.",
        desc_ja="靴下・ニット小物の副資材ガイド。織りラベルか熱転写の無感ラベルかの選び方、足長とEU番号の併記、カード寸法と折り方、ペア包装とギフト比率、仕様表と5つの検収項目を解説します。東莞泰閣包装。",
        desc_ko="양말·니트 소품 부자재 가이드. 직조 라벨과 열전사 무감 라벨 선택, 발 길이와 EU 호수 병기, 카드 치수와 접는 방식, 페어 포장과 선물 비율, 사양표와 5단계 검수를 정리했습니다. 둥관 TAGE 패키징.",
        desc_fr="Guide accessoires chaussettes et petites pièces maille : label tissé ou transfert, tailles par longueur de pied, format de carte, emballage par paire et cinq contrôles.",
        desc_es="Guía de accesorios para calcetines y pequeñas piezas de punto: etiqueta tejida o transferible, tallas por longitud de pie, formato de tarjeta y cinco controles.",
        crumb_zh="袜子辅料", crumb_en="Sock Trims", crumb_ja="靴下副資材",
        crumb_ko="양말 부자재", crumb_fr="Accessoires chaussettes", crumb_es="Accesorios calcetines",
        h1_zh="袜子与针织小件辅料指南：袜标工艺、尺码标与吊卡包装",
        h1_en="Sock and Hosiery Trims Guide: Labels, Sizing and Card Packaging",
        h1_ja="靴下・ニット小物の副資材ガイド：ラベル仕様・サイズ・カード包装",
        h1_ko="양말·니트 소품 부자재 가이드: 라벨 사양, 사이즈, 카드 포장",
        h1_fr="Guide des accessoires pour chaussettes : labels, tailles et cartes",
        h1_es="Guía de accesorios para calcetines: etiquetas, tallas y tarjetas",
        tag_zh="袜子品类", tag_en="Socks", tag_ja="靴下", tag_ko="양말",
        tag_fr="Chaussettes", tag_es="Calcetines",
        sum_zh="袜子辅料的逻辑和成衣不同：贴身穿、几乎每天洗、按脚长分尺码，标签要无感又要耐洗，还要挂得上货架、塞得进电商袋。本文讲清织唛、热转印与印刷布标怎么按袜型选，脚长与欧码怎么并写，吊卡尺寸怎么按折叠方式定，成对腰带与多双礼盒如何配比，并附一份可直接询价的规格表与五步验收清单。",
        sum_en="Sock trims follow different logic from garment trims: worn on skin, washed constantly, sized by foot length, the label must be tagless yet durable and ready for both a peg and a mailer bag. This guide covers choosing woven, heat-transfer or printed tape by sock type, writing foot length with EU numbering, sizing the card to the fold, and ratioing pairs and multi-pair gift boxes, with a specification table and a five-step acceptance list.",
        sum_ja="靴下の副資材は衣料とは論理が異なります。肌に直接触れ、ほぼ毎日洗い、足長でサイズを分けるため、ラベルは無感かつ耐洗で、店頭にもEC袋にも対応する必要があります。本記事は織りラベル・熱転写・印刷テープの選び方、足長とEU番号の併記、折り方に合わせたカード寸法、ペア包装と複数足ギフトの比率を解説し、仕様表と5ステップの検収リストを掲載します。",
        sum_ko="양말 부자재는 의류와 논리가 다릅니다. 피부에 닿고 거의 매일 세탁하며 발 길이로 사이즈를 나누기 때문에 라벨은 무감이면서 내세탁성이 있고 매장과 이커머스 봉투 모두에 맞아야 합니다. 이 글은 직조·열전사·인쇄 테이프 선택, 발 길이와 EU 호수 병기, 접는 방식에 맞춘 카드 치수, 페어 포장과 여러 켤레 선물 상자 비율을 다루고 사양표와 5단계 검수 목록을 제공합니다.",
        sum_fr="L'accessoire de chaussette suit une autre logique que le vêtement : porté à même la peau, lavé sans cesse, taillé par longueur de pied, le label doit être sans épaisseur, durable, et convenir au présentoir comme au sachet e-commerce. Ce guide traite le choix du tissé, du transfert ou du ruban imprimé selon le type de chaussette, l'écriture de la longueur de pied avec la numérotation EU, le format de carte selon le pliage, les paires et coffrets, avec un tableau de spécifications et cinq contrôles.",
        sum_es="El accesorio del calcetín sigue otra lógica: se lleva sobre la piel, se lava sin parar, se talla por longitud de pie, y la etiqueta debe ser sin relieve y duradera, válida para expositor y bolsa de e-commerce. Esta guía trata la elección de tejida, termotransferible o cinta impresa según el tipo, la escritura de la longitud con numeración EU, el formato de tarjeta según el plegado y las cajas de varios pares, con tabla de especificaciones y cinco comprobaciones.",
    ),
    dict(
        slug="hat-scarf-gloves-trims-guide.html",
        body="blog/_body_hats.html",
        title_zh="帽子围巾手套辅料指南：成分标、尺码与礼盒包装 | TAGE",
        title_en="Hat, Scarf and Glove Trims Guide: Fibre Labels, Sizing and Gift Boxes | TAGE",
        title_ja="帽子・マフラー・手袋の副資材ガイド：組成表示・サイズ・ギフト包装 | TAGE",
        title_ko="모자·머플러·장갑 부자재 가이드: 혼용률 표시, 사이즈, 선물 포장 | TAGE",
        title_fr="Guide des accessoires bonnets, écharpes et gants : composition et coffrets | TAGE",
        title_es="Guía de accesorios para gorros, bufandas y guantes: composición y cajas | TAGE",
        desc_zh="帽子、围巾与手套辅料指南：讲清成分比例怎么标才不违规、头围与掌围尺码怎么写、长条标签缝在哪不露边、吊卡吊粒与冬季三件套礼盒如何配比，附询价规格表与五步验收清单。来自东莞泰阁包装。",
        desc_en="Hat, scarf and glove trims guide: fibre content labelling, head and palm sizing, where to sew long labels, tags and three-piece gift box ratios, plus five checks.",
        desc_ja="帽子・マフラー・手袋の副資材ガイド。組成表示の書き方、頭囲と手囲みのサイズ表記、長いラベルの縫い位置、タグと3点セットのギフト比率、仕様表と5つの検収項目を解説します。東莞泰閣包装。",
        desc_ko="모자·머플러·장갑 부자재 가이드. 혼용률 표기 방법, 머리둘레와 손둘레 사이즈, 긴 라벨 봉제 위치, 행택과 3종 선물 세트 비율, 사양표와 5단계 검수를 정리했습니다. 둥관 TAGE 패키징.",
        desc_fr="Guide accessoires bonnets, écharpes et gants : composition des fibres, tailles tour de tête et de main, pose des labels longs, tags et coffrets, avec cinq contrôles.",
        desc_es="Guía de accesorios para gorros, bufandas y guantes: composición, tallas de contorno de cabeza y mano, colocación de etiquetas largas, colgantes y cajas.",
        crumb_zh="配饰辅料", crumb_en="Accessory Trims", crumb_ja="アクセサリー副資材",
        crumb_ko="액세서리 부자재", crumb_fr="Accessoires", crumb_es="Accesorios",
        h1_zh="帽子围巾手套辅料指南：成分标、尺码与礼盒包装",
        h1_en="Hat, Scarf and Glove Trims Guide: Fibre Labels, Sizing and Gift Boxes",
        h1_ja="帽子・マフラー・手袋の副資材ガイド：組成表示・サイズ・ギフト包装",
        h1_ko="모자·머플러·장갑 부자재 가이드: 혼용률 표시, 사이즈, 선물 포장",
        h1_fr="Guide des accessoires bonnets, écharpes et gants : composition et coffrets",
        h1_es="Guía de accesorios para gorros, bufandas y guantes: composición y cajas",
        tag_zh="配饰品类", tag_en="Accessories", tag_ja="アクセサリー", tag_ko="액세서리",
        tag_fr="Accessoires", tag_es="Accesorios",
        sum_zh="配饰类不能试穿，顾客只能靠成分标判断值不值，因此成分比例、头围与掌围尺码、标签缝位比成衣更不能出错。本文讲清帽子主唛与洗水标缝在哪、围巾长条标签如何缝在流苏之外、手套尺码与内里标签怎么处理、吊卡吊粒怎么选，以及冬季三件套礼盒的配比与装箱要点，并附询价规格表与五步验收清单。",
        sum_en="Accessories cannot be tried on, so the buyer judges value from the fibre label alone — which makes composition, head and palm sizing and label placement less forgiving than on garments. This guide covers where hat brand and care labels go, sewing scarf tape clear of the fringe, glove sizing and inner labels, tag fasteners, and how to ratio a winter three-piece gift box, with a specification table and a five-step acceptance list.",
        sum_ja="アクセサリーは試着できず、顧客は組成表示だけで価値を判断します。そのため組成比率、頭囲・手囲みのサイズ、縫い位置は衣料以上に正確さが求められます。本記事は帽子の主ラベルと洗濯表示の位置、マフラーの長いラベルをフリンジに掛からないよう縫う方法、手袋のサイズと内側ラベル、タグの止め具、冬の3点セットのギフト比率と梱包を解説し、仕様表と5ステップの検収リストを掲載します。",
        sum_ko="액세서리는 착용해볼 수 없어 고객이 혼용률 표기만으로 가치를 판단합니다. 그래서 혼용률, 머리둘레·손둘레 사이즈, 라벨 봉제 위치는 의류보다 더 정확해야 합니다. 이 글은 모자 주 라벨과 세탁 표시 위치, 머플러 긴 라벨을 프린지에 걸리지 않게 봉제하는 법, 장갑 사이즈와 내부 라벨, 행택 고정구, 겨울 3종 선물 세트 비율과 포장을 다루고 사양표와 5단계 검수 목록을 제공합니다.",
        sum_fr="Les accessoires ne s'essayant pas, le client juge la valeur sur la seule composition : ratios de fibres, tailles tour de tête et de main et pose des labels y sont donc moins pardonnés qu'en vêtement. Ce guide traite la position des labels sur un bonnet, la couture d'un ruban d'écharpe hors de la frange, les tailles et labels intérieurs des gants, les attaches de tag et les ratios d'un coffret trio, avec un tableau de spécifications et cinq contrôles.",
        sum_es="Los accesorios no se prueban, así que el cliente juzga el valor solo por la composición: ratios de fibras, tallas de contorno y colocación de etiquetas exigen más precisión que en prenda. Esta guía trata la posición de etiquetas en gorros, coser la cinta de bufanda fuera del fleco, tallas y etiquetas internas de guantes, fijadores de colgante y ratios de una caja trío, con tabla de especificaciones y cinco comprobaciones.",
    ),
]

skel = open(SKEL, encoding="utf-8").read()
old3 = re.search(r'"position": 3,\s*"name": "([^"]*)"', skel).group(1)
print("骨架 breadcrumb 名:", old3)

# ---------------- 撞车安全闸 ----------------
for a in ARTICLES:
    for p in [a["body"]]:
        if not os.path.exists(p):
            raise SystemExit("正文文件缺失：%s" % p)
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
    print("  %-34s desc_zh=%d字 desc_en=%d字符 desc_ja=%d desc_ko=%d desc_fr=%d desc_es=%d"
          % (a["slug"], len(a["desc_zh"]), len(a["desc_en"]), len(a["desc_ja"]),
             len(a["desc_ko"]), len(a["desc_fr"]), len(a["desc_es"])))

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

    crumb = ('<div class="crumb"><a href="../index.html" data-zh="首頁" data-fr="Accueil" data-es="Inicio" data-en="Home" data-ja="ホーム" data-ko="홈">首頁</a>'
             ' / <a href="index.html" data-zh="輔料 FAQ" data-fr="FAQ Accessoires" data-es="FAQ Accesorios" data-en="Trims FAQ" data-ja="副資材 FAQ" data-ko="부자재 FAQ">輔料 FAQ</a>'
             ' / <span data-zh="%s" data-en="%s" data-ja="%s" data-ko="%s" data-fr="%s" data-es="%s">%s</span></div>'
             % (a["crumb_zh"], a["crumb_en"], a["crumb_ja"], a["crumb_ko"],
                a["crumb_fr"], a["crumb_es"], a["crumb_zh"]))
    s, n = re.subn(r'<div class="crumb">.*?</div>', crumb, s, count=1, flags=re.S)
    assert n == 1, "crumb 替换失败"

    h1 = ('<h1 data-zh="%s" data-en="%s" data-ja="%s" data-ko="%s" data-fr="%s" data-es="%s">%s</h1>'
          % (a["h1_zh"], a["h1_en"], a["h1_ja"], a["h1_ko"], a["h1_fr"], a["h1_es"], a["h1_zh"]))
    s, n = re.subn(r'<h1 .*?</h1>', h1, s, count=1, flags=re.S)
    assert n == 1, "h1 替换失败"

    meta = ('<p data-zh="泰閣包裝 · 更新於 %s" data-en="By TAGE Packaging &nbsp;·&nbsp; Updated %s" '
            'data-ja="泰閣包装 · %s" data-ko="TAGE 패키징 · %s" '
            'data-fr="Par TAGE Packaging &nbsp;·&nbsp; Mis à jour le %s" '
            'data-es="Por TAGE Packaging &nbsp;·&nbsp; Actualizado el %s">泰閣包裝 · 更新於 %s</p>'
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
        <a class="more" href="{slug}" data-zh="閱讀全文 →" data-en="Read more →" data-ja="続きを読む →" data-ko="자세히 보기 →" data-fr="Lire la suite →" data-es="Leer más →">閱讀全文 →</a>
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
