#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-27 14:00 批次每日更新生成脚本（六语：zh-Hant 根 / en / ja / ko / fr / es）
- 亚马逊 FBA 服装包装与标签（amazon-fba-apparel-packaging-guide）
- 美国州级包装 EPR 法规（us-state-packaging-epr-laws）

用法: F:/hermes/venvs/tools/Scripts/python.exe daily_gen_20261027_1400.py [--check]
"""
import os, re, sys, subprocess, importlib.util

ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)
PY = sys.executable

SKEL = "blog/knitwear-sweater-trims-guide.html"
DATE_ZH = "2026年10月27日"
DATE_EN = "October 27, 2026"
DATE_JA = "2026年10月27日更新"
DATE_KO = "2026년 10월 27일 업데이트"
DATE_FR = "27 octobre 2026"
DATE_ES = "27 de octubre de 2026"
SITEMAP_DATE = "2026-10-27"
BUST_OLD, BUST_NEW = "185", "186"
LANGS = ["en", "ja", "ko", "fr", "es"]

ARTICLES = [
    dict(
        slug="amazon-fba-apparel-packaging-guide.html",
        body="blog/_body_fba.html",
        title_zh="亚马逊 FBA 服装包装指南：袋装、挂装与标签合规 | TAGE",
        title_en="Amazon FBA Apparel Packaging: Bags, Hangers and Label Rules | TAGE",
        title_ja="Amazon FBA向け衣料包装ガイド：袋詰め・ハンガー・ラベルの適合 | TAGE",
        title_ko="아마존 FBA 의류 포장 가이드: 비닐·행거·라벨 적합성 | TAGE",
        title_fr="Emballage textile pour Amazon FBA : sachets, cintres et étiquetage | TAGE",
        title_es="Embalaje textil para Amazon FBA: bolsas, perchas y etiquetado | TAGE",
        desc_zh="亚马逊 FBA 服装包装指南：平装袋装、挂装与盒装怎么选，塑料袋厚度与窒息警告的五条硬要求，FNSKU 与条码贴在哪里，吊牌价格与洗水标内容怎么处理，外箱重量、混装与防潮要求，以及怎么把 FBA 准备直接写进辅料订单。来自东莞泰阁包装。",
        desc_en="Amazon FBA apparel packaging: bagged, hung or boxed, poly bag gauge and suffocation warning, FNSKU placement, carton weight and prep inside the trims order.",
        desc_ja="Amazon FBA向け衣料包装のガイド。平袋・ハンガー・箱詰めの選び方、ポリ袋の厚みと窒息警告の5条件、FNSKUとバーコードの位置、タグ価格と洗濯表示の扱い、外箱重量・混載・防湿、そしてFBA準備を副資材発注に組み込む方法を解説します。東莞泰閣包装。",
        desc_ko="아마존 FBA 의류 포장 가이드. 평면 비닐·행거·박스 선택, 비닐 두께와 질식 경고 다섯 조건, FNSKU와 바코드 위치, 행택 가격과 케어 라벨 처리, 카톤 중량·혼적·방습, FBA 준비를 부자재 발주에 넣는 방법을 정리했습니다. 둥관 TAGE 패키징.",
        desc_fr="Emballage textile pour Amazon FBA : à plat, sur cintre ou en boîte, épaisseur et mention d'étouffement, pose du FNSKU, poids des cartons et préparation intégrée à la commande.",
        desc_es="Embalaje textil para Amazon FBA: plano, colgado o en caja, grosor y advertencia de asfixia, colocación del FNSKU, peso del cartón y preparación incluida en el pedido.",
        crumb_zh="亚马逊 FBA 服装包装",
        crumb_en="Amazon FBA Apparel Packaging",
        crumb_ja="Amazon FBA向け衣料包装",
        crumb_ko="아마존 FBA 의류 포장",
        crumb_fr="Emballage textile FBA",
        crumb_es="Embalaje textil FBA",
        h1_zh="亚马逊 FBA 服装包装与标签：袋装、挂装、套装怎么处理",
        h1_en="Amazon FBA Apparel Packaging: Bags, Hangers and Sets Done Right",
        h1_ja="Amazon FBA向け衣料包装とラベル：袋詰め・ハンガー・セット品の扱い",
        h1_ko="아마존 FBA 의류 포장과 라벨: 비닐, 행거, 세트 상품 처리",
        h1_fr="Emballage et étiquetage pour Amazon FBA : sachets, cintres et lots",
        h1_es="Embalaje y etiquetado para Amazon FBA: bolsas, perchas y conjuntos",
        tag_zh="电商包装", tag_en="E-commerce Packaging", tag_ja="EC包装", tag_ko="이커머스 포장",
        tag_fr="Emballage e-commerce", tag_es="Embalaje e-commerce",
        sum_zh="服装货进亚马逊仓库，被退回的原因往往不是质量，而是袋子太薄、缺窒息警告、FNSKU 贴错位置、套装没标不可拆分。本文拆六件事：三种入仓形态怎么选、塑料袋的五条硬要求、条码与标签的位置、吊牌价格与洗水标的两个坑、外箱重量与防潮，以及怎么把 FBA 准备并进辅料订单一次做完。",
        sum_en="What gets apparel shipments rejected at an Amazon warehouse is rarely quality: bags too thin, no suffocation warning, an FNSKU in the wrong place, a set with no do-not-separate marking. Six sections cover the three inbound formats, five hard rules for poly bags, barcode placement, the price and care label traps, carton weight and moisture, and folding FBA prep into the trims order.",
        sum_ja="アマゾン倉庫で返される理由は品質よりも、袋が薄い、窒息警告がない、FNSKUの位置が違う、セット品に分割不可表示がないといった点です。3つの入庫形態、ポリ袋の5条件、バーコードの位置、価格と洗濯表示の落とし穴、外箱重量と防湿、FBA準備を発注に組み込む方法の6点を整理します。",
        sum_ko="아마존 창고에서 반송되는 이유는 품질보다 비닐이 얇고, 질식 경고가 없고, FNSKU 위치가 틀리고, 세트 상품에 분리 금지 표시가 없는 경우가 많습니다. 세 가지 입고 형태, 비닐의 다섯 조건, 바코드 위치, 가격과 케어 라벨의 함정, 카톤 중량과 방습, FBA 준비를 발주에 넣는 방법을 정리합니다.",
        sum_fr="Ce qui fait refuser un envoi textile en entrepôt Amazon n'est pas la qualité : sachets trop fins, mention d'étouffement absente, FNSKU mal placé, lot sans marquage insécable. Six parties : les trois formats de réception, cinq règles pour les sachets, la pose des codes, les pièges prix et étiquette d'entretien, cartons et humidité, et la préparation intégrée à la commande.",
        sum_es="Lo que hace rechazar un envío textil en un almacén de Amazon casi nunca es la calidad: bolsas finas, sin advertencia de asfixia, FNSKU mal colocado, conjunto sin marca de no separar. Seis apartados: los tres formatos, cinco reglas de bolsa, colocación de códigos, las trampas de precio y etiqueta, cartones y humedad, y la preparación dentro del pedido.",
    ),
    dict(
        slug="us-state-packaging-epr-laws.html",
        body="blog/_body_us_epr.html",
        title_zh="美国州级包装 EPR 法规：加州 SB 54 与各州要求 | TAGE",
        title_en="US State Packaging EPR Laws: California SB 54 and What Follows | TAGE",
        title_ja="米国州レベルの包装EPR法：カリフォルニアSB 54と各州の要件 | TAGE",
        title_ko="미국 주별 포장 EPR 법: 캘리포니아 SB 54와 각 주 요건 | TAGE",
        title_fr="Lois EPR sur les emballages aux États-Unis : Californie SB 54 | TAGE",
        title_es="Leyes EPR de envases en EE. UU.: California SB 54 y otros estados | TAGE",
        desc_zh="美国州级包装 EPR 指南：加州 SB 54 的 2032 目标、俄勒冈回收现代化法、科罗拉多与缅因按吨计费、明尼苏达新法，谁算生产商、什么算包装、供应商要给的六项数据，以及采购端减重与单一材质化四步落地。来自东莞泰阁包装。",
        desc_en="US packaging EPR: California SB 54 targets, Oregon, Colorado, Maine and Minnesota, who is a producer, what is packaging, six data points, four buying steps.",
        desc_ja="米国州レベルの包装EPRガイド。カリフォルニアSB 54の2032年目標、オレゴンのリサイクル近代化法、コロラドとメインのトン課金、ミネソタ新法、誰が生産者か、何が包装か、6つのデータ項目、調達側の減量と単一素材化の4ステップを解説します。東莞泰閣包装。",
        desc_ko="미국 주별 포장 EPR 가이드. 캘리포니아 SB 54의 2032년 목표, 오리건 재활용 현대화법, 콜로라도와 메인의 톤 과금, 미네소타 신법, 누가 생산자인지, 무엇이 포장인지, 여섯 가지 데이터, 구매 측 감량과 단일 소재화 네 단계를 정리했습니다. 둥관 TAGE 패키징.",
        desc_fr="EPR packaging aux États-Unis : objectifs de la Californie SB 54, Oregon, Colorado, Maine et Minnesota, qui est producteur, ce qui est emballage, six données et quatre étapes.",
        desc_es="EPR de envases en EE. UU.: objetivos de California SB 54, Oregón, Colorado, Maine y Minnesota, quién es productor, qué es envase, seis datos y cuatro pasos.",
        crumb_zh="美国州级包装 EPR",
        crumb_en="US State Packaging EPR",
        crumb_ja="米国州レベルの包装EPR",
        crumb_ko="미국 주별 포장 EPR",
        crumb_fr="EPR packaging aux États-Unis",
        crumb_es="EPR de envases en EE. UU.",
        h1_zh="美国包装 EPR 来了：服装品牌与包装供应商要做的四件事",
        h1_en="US Packaging EPR Has Arrived: Four Things Brands and Suppliers Must Do",
        h1_ja="米国の包装EPRが始まる：ブランドと包装サプライヤーがやるべき4つ",
        h1_ko="미국 포장 EPR 시작: 브랜드와 포장 공급사가 해야 할 네 가지",
        h1_fr="L'EPR packaging arrive aux États-Unis : quatre choses à faire",
        h1_es="La EPR de envases llega a EE. UU.: cuatro cosas por hacer",
        tag_zh="包装合规", tag_en="Packaging Compliance", tag_ja="包装コンプライアンス", tag_ko="포장 규제 대응",
        tag_fr="Conformité emballage", tag_es="Cumplimiento de envases",
        sum_zh="包装合规过去只看欧盟，2026 年起美国也在名单上：加州 SB 54、俄勒冈回收现代化法、科罗拉多、缅因与明尼苏达都已立法。本文讲清谁算生产商、三层包装各是什么、供应商必须提供的六项数据，以及采购端减重、单一材质化、写进规格书的四步落地，并点出三个最常见的误判。",
        sum_en="Packaging compliance used to mean Europe; from 2026 the US is on the list too — California SB 54, Oregon's modernisation act, Colorado, Maine and Minnesota. This guide covers who counts as a producer, the three packaging layers, the six data points a supplier must provide, and four procurement steps, closing with three common misreadings.",
        sum_ja="包装対応はEUだけを見れば足りましたが、2026年以降は米国も対象です。カリフォルニアSB 54、オレゴンの近代化法、コロラド、メイン、ミネソタが既に立法しています。誰が生産者か、3層の包装、サプライヤーが渡すべき6項目、調達側の4ステップ、そしてよくある3つの誤解を整理します。",
        sum_ko="포장 규제는 EU만 보면 되었지만 2026년부터는 미국도 대상입니다. 캘리포니아 SB 54, 오리건 현대화법, 콜로라도, 메인, 미네소타가 이미 입법했습니다. 누가 생산자인지, 세 층의 포장, 공급사가 제공해야 할 여섯 항목, 구매 측 네 단계, 흔한 세 가지 오해를 정리합니다.",
        sum_fr="La conformité emballage se lisait en Europe ; depuis 2026, les États-Unis s'ajoutent : Californie SB 54, loi de modernisation de l'Oregon, Colorado, Maine et Minnesota. Qui est producteur, les trois couches d'emballage, six données à exiger, quatre étapes achats et trois contresens courants.",
        sum_es="La conformidad de envases se leía en Europa; desde 2026 EE. UU. entra en la lista: California SB 54, la ley de modernización de Oregón, Colorado, Maine y Minnesota. Quién es productor, las tres capas, seis datos exigibles, cuatro pasos de compras y tres lecturas erróneas.",
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
    print("  %-42s desc_zh=%d字 desc_en=%d字符 desc_ja=%d desc_ko=%d desc_fr=%d desc_es=%d"
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
