#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-09-20 第四批（20:00）每日更新：2 篇新文章（六语：zh-Hant 根 / en / ja / ko / fr / es）
+ 列表页卡片 + gen_i18n 五语生成 + sitemap + BUST_VERSION 升级 + 繁体转换。

用法: python daily_gen_20260920_2000.py
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
BUST_OLD, BUST_NEW = "94", "95"
LANGS = ["en", "ja", "ko", "fr", "es"]

ARTICLES = [
    dict(
        slug="garment-gift-box-packaging.html",
        body="blog/_body_gift_box.html",
        title_zh="服装礼盒包装定制指南：精装硬盒、磁吸盒与内衬怎么做 | TAGE",
        title_en="Apparel Gift Box Packaging Guide: Rigid, Magnetic &amp; Drawer Boxes | TAGE",
        title_ja="衣料用ギフトボックス（化粧箱）ガイド：箱型・内装・コストの考え方 | TAGE",
        title_ko="의류 선물 상자(하드 박스) 가이드: 구조, 내장재, 비용 | TAGE",
        title_fr="Guide des coffrets rigides pour vêtements : structure, calage et coût | TAGE",
        title_es="Guía de cajas rígidas para ropa: estructura, interior y coste | TAGE",
        desc_zh="服装礼盒包装定制指南：精装硬盒的三种盒型（天地盖、磁吸翻盖、抽屉盒）怎么选，内衬怎么固定衣服又能撑出立体感，裱纸与烫金工艺如何取舍，盒内径怎么从衣服尺寸反推，以及起订量、成本构成与出口运输的两种做法，附打样确认清单。来自东莞泰阁包装。",
        desc_en="Apparel gift box guide: lid-and-base, magnetic and drawer structures, inserts that hold the garment, wrapping and finishing choices, sizing maths, MOQ, cost and two export shipping models.",
        desc_ja="衣料用ギフトボックスのガイド。天蓋式・マグネット式・スライド式の選び方、商品を固定する内装、貼り紙と箔押しの取捨、商品から内寸を逆算する方法、最小ロット・コスト・輸出時の2つの輸送方法を解説します。東莞泰閣包装。",
        desc_ko="의류 선물 상자 가이드: 뚜껑 분리형, 자석식, 슬라이드식 구조 선택, 제품을 고정하는 내장재, 감싸는 종이와 박 가공, 치수 산출, 최소 주문량, 원가와 수출 운송 두 방식을 정리했습니다. 둥관 TAGE 패키징.",
        desc_fr="Guide des coffrets rigides : structures à couvercle, magnétique et tiroir, calages qui maintiennent le vêtement, habillage et finitions, calcul des dimensions, minimum, coût et deux modèles d'expédition.",
        desc_es="Guía de cajas rígidas: estructuras de tapa y base, magnética y de cajón, interiores que sujetan la prenda, forrado y acabados, cálculo de medidas, mínimo, coste y dos modelos de envío.",
        crumb_zh="服装礼盒包装", crumb_en="Apparel Gift Boxes", crumb_ja="衣料用ギフトボックス",
        crumb_ko="의류 선물 상자", crumb_fr="Coffrets pour vêtements", crumb_es="Cajas para ropa",
        h1_zh="服装礼盒包装定制指南：精装硬盒、磁吸盒与内衬怎么做",
        h1_en="Apparel Gift Box Packaging: Rigid, Magnetic and Drawer Boxes Explained",
        h1_ja="衣料用ギフトボックスの作り方：箱型・内装・コストの考え方",
        h1_ko="의류 선물 상자 제작 가이드: 구조, 내장재, 비용",
        h1_fr="Coffrets rigides pour vêtements : structure, calage et coût",
        h1_es="Cajas rígidas para ropa: estructura, interior y coste",
        tag_zh="包装指南", tag_en="Packaging Guide", tag_ja="包装ガイド", tag_ko="포장 가이드",
        tag_fr="Guide emballage", tag_es="Guía de embalaje",
        sum_zh="礼盒是辅料里“结构决定成本”最明显的品类：同样尺寸，天地盖与磁吸翻盖的差价可能过半；内衬从纸托换成 EVA 又要再上一层。本文按是否需要礼盒、三种盒型与风险、内衬固定方式、裱纸与表面工艺、从衣服反推盒内径、成本起订量与出口运输两部分展开，并给出打样时必做的装配测试。",
        sum_en="Rigid boxes are where structure drives cost most visibly: at the same footprint a lid-and-base and a magnetic box can differ by more than half, and upgrading the insert from folded card to EVA adds another step. This guide covers when a rigid box pays off, three structures and their risks, inserts, wrapping and finishing, sizing back from the garment, MOQ and cost, and two export shipping models — with the fit test to run on every sample.",
        sum_ja="化粧箱は「構造がコストを決める」典型で、同じ寸法でも天蓋式とマグネット式では価格が倍近く違うことがあり、内装を紙トレーから EVA に変えるとさらに一段上がります。導入判断、3つの箱型とリスク、内装の固定方法、貼り紙と表面加工、商品から内寸を逆算する方法、コストと最小ロット、輸出時の2つの輸送方法を整理し、サンプル時に必ず行う組付けテストも示します。",
        sum_ko="하드 박스는 ‘구조가 비용을 결정하는’ 대표 품목으로, 같은 크기라도 뚜껑 분리형과 자석식은 가격이 절반 이상 차이 날 수 있고 내부를 종이 트레이에서 EVA로 바꾸면 한 단계 더 오릅니다. 도입 판단, 세 가지 구조와 리스크, 내장재 고정 방식, 감싸는 종이와 표면 가공, 제품에서 내부 치수를 역산하는 방법, 최소 주문량과 원가, 수출 운송 두 방식을 정리하고 샘플마다 해야 할 조립 테스트를 제시합니다.",
        sum_fr="Le coffret est la catégorie où la structure pèse le plus sur le coût : à surface égale, un couvercle séparé et une fermeture magnétique peuvent varier de plus de moitié, et passer d'un calage carton à un calage EVA ajoute un cran. Ce guide couvre le choix, trois structures et leurs risques, les calages, l'habillage et les finitions, le calcul des dimensions à partir du vêtement, le minimum et le coût, et deux modèles d'expédition, avec le test de montage à faire sur chaque échantillon.",
        sum_es="Es la categoría donde la estructura pesa más en el coste: a igual tamaño, una caja de tapa y base y una magnética pueden diferir más de la mitad, y pasar de un soporte de cartón a uno de EVA sube otro escalón. Esta guía cubre cuándo conviene, tres estructuras y sus riesgos, los interiores, el forrado y los acabados, el cálculo de medidas desde la prenda, el mínimo y el coste, y dos modelos de envío, con la prueba de montaje para cada muestra.",
    ),
    dict(
        slug="poly-bag-cost-guide.html",
        body="blog/_body_polybag_cost.html",
        title_zh="服装胶袋成本指南：一张报价背后的六个成本项与降本方法 | TAGE",
        title_en="Garment Poly Bag Cost Guide: Six Cost Elements and How to Cut Them | TAGE",
        title_ja="衣料用ポリ袋のコストガイド：見積りの6項目と削減方法 | TAGE",
        title_ko="의류 비닐봉투 원가 가이드: 견적의 여섯 항목과 절감 방법 | TAGE",
        title_fr="Guide des coûts de sachet pour vêtements : six postes et réductions | TAGE",
        title_es="Guía de costes de bolsas para ropa: seis partidas y cómo rebajarlas | TAGE",
        desc_zh="服装胶袋成本指南：拆解一张报价背后的六个成本项，讲清材质与厚度、尺寸与标准膜宽开料、印刷色数与满版、数量与版费分摊如何影响单价，给出六个不降品质的降本做法，并列出询价前必须问清的七个问题与无印刷区等技术细节。来自东莞泰阁包装。",
        desc_en="Garment poly bag cost guide: the six cost elements behind one quote, how material, thickness, cutting, printing and volume move the price, six ways to cut cost without cutting quality, and seven questions to ask.",
        desc_ja="衣料用ポリ袋のコストガイド。見積り1枚の裏にある6つのコスト項目、素材と厚み、寸法と標準フィルム幅、色数・ベタ、数量と版代の按分が単価に与える影響、品質を落とさない6つの削減策、発注前に確認すべき7つの質問を解説します。東莞泰閣包装。",
        desc_ko="의류 비닐봉투 원가 가이드: 견적 한 장 뒤의 여섯 가지 비용 항목, 재질과 두께, 치수와 표준 필름 폭, 색 수와 전체 인쇄, 수량과 인쇄판 분담이 단가에 미치는 영향, 품질을 낮추지 않는 여섯 가지 절감 방법, 발주 전 확인할 일곱 가지 질문을 정리했습니다. 둥관 TAGE 패키징.",
        desc_fr="Guide des coûts de sachet : les six postes derrière un devis, l'effet de la matière, de l'épaisseur, de la découpe, de l'impression et du volume sur le prix, six leviers d'économie et sept questions à poser.",
        desc_es="Guía de costes de bolsas: las seis partidas detrás de un presupuesto, el efecto de material, grosor, corte, impresión y volumen en el precio, seis vías de ahorro y siete preguntas antes de pedir.",
        crumb_zh="胶袋成本结构", crumb_en="Poly Bag Costs", crumb_ja="ポリ袋のコスト",
        crumb_ko="비닐봉투 원가", crumb_fr="Coûts des sachets", crumb_es="Costes de bolsas",
        h1_zh="服装胶袋成本指南：一张报价背后的六个成本项与降本方法",
        h1_en="Garment Poly Bag Cost Guide: What Is Behind One Quote",
        h1_ja="衣料用ポリ袋のコストガイド：見積り1枚の裏側と削減方法",
        h1_ko="의류 비닐봉투 원가 가이드: 견적 한 장의 구성과 절감 방법",
        h1_fr="Coûts des sachets pour vêtements : ce qui se cache derrière un devis",
        h1_es="Coste de las bolsas para ropa: qué hay detrás de un presupuesto",
        tag_zh="成本指南", tag_en="Cost Guide", tag_ja="コストガイド", tag_ko="원가 가이드",
        tag_fr="Guide de coûts", tag_es="Guía de costes",
        sum_zh="同样尺寸的服装胶袋，不同供应商报价可以差一倍以上——差价很少来自利润，而是材质、厚度、尺寸、印刷、数量五个参数，加上版费有没有被分摊。本文把一张报价拆成六个成本项，讲清厚度与开料的钱花在哪里、印刷色数的台阶、数量如何摊薄固定成本，给出六个不降品质的降本做法，以及询价时的七个必问问题（含无印刷区与旧版沿用）。",
        sum_en="Two suppliers can quote more than double for the same garment poly bag. The gap rarely comes from margin: it comes from five parameters — material, thickness, size, printing and quantity — plus whether plate costs are amortised. This guide splits one quote into six cost elements, shows where thickness and cutting actually cost money, how printing steps up and how volume dilutes fixed costs, then gives six ways to cut cost without cutting quality and seven questions to ask before ordering.",
        sum_ja="同じ寸法の衣料用ポリ袋でも見積りが2倍以上違うことがあります。差額は利益ではなく、素材・厚み・寸法・印刷・数量の5条件と版代の按分で生まれます。本記事では見積りを6つのコスト項目に分解し、厚みと材料取りで費用がどこに発生するか、印刷の色数による段差、数量が固定費を薄める仕組みを示し、品質を落とさない6つの削減策と発注前の7つの質問（非印刷領域や既存版の流用を含む）を整理します。",
        sum_ko="같은 크기의 의류 비닐봉투라도 견적이 두 배 이상 차이 날 수 있습니다. 차이는 이윤이 아니라 재질, 두께, 크기, 인쇄, 수량이라는 다섯 조건과 인쇄판 비용 분담에서 나옵니다. 이 글은 견적을 여섯 가지 비용 항목으로 나누고, 두께와 재단에서 비용이 어디서 발생하는지, 인쇄 색 수의 단계, 수량이 고정비를 희석하는 구조를 설명한 뒤 품질을 낮추지 않는 여섯 가지 절감 방법과 발주 전 일곱 가지 질문(비인쇄 영역과 기존 판 재사용 포함)을 정리합니다.",
        sum_fr="Pour un sachet de même dimension, deux fournisseurs peuvent afficher plus du double. L'écart vient rarement de la marge : il vient de cinq paramètres — matière, épaisseur, dimensions, impression, quantité — et de l'amortissement des formes. Ce guide décompose un devis en six postes, montre où l'épaisseur et la découpe coûtent vraiment, comment l'impression monte par paliers et comment le volume dilue les frais fixes, puis donne six leviers d'économie et sept questions à poser avant commande.",
        sum_es="Dos proveedores pueden cotizar más del doble la misma bolsa. La diferencia rara vez es margen: viene de cinco parámetros —material, grosor, tamaño, impresión y cantidad— y de si los clichés están amortizados. Esta guía desglosa un presupuesto en seis partidas, muestra dónde cuestan dinero el grosor y el corte, cómo escala la impresión y cómo el volumen diluye los costes fijos, y ofrece seis vías de ahorro y siete preguntas antes de pedir.",
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
    print("写入 %s (%d KB) desc_zh=%d字 desc_en=%d desc_fr=%d desc_es=%d"
          % (out, len(s.encode("utf-8")) // 1024, len(a["desc_zh"]), len(a["desc_en"]),
             len(a["desc_fr"]), len(a["desc_es"])))

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
