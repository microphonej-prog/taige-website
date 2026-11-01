#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-11-01 14:00 批次每日更新生成脚本（六语：zh-Hant 根 / en / ja / ko / fr / es）
- 邻苯二甲酸酯限制与无 PVC 服装包装方案（phthalate-free-apparel-packaging）
- 服装电商退货包装方案：可重封与二次销售复原（garment-packaging-for-returns）

用法: F:/hermes/venvs/tools/Scripts/python.exe daily_gen_20261101_1400.py [--check]
"""
import os, re, sys, subprocess, importlib.util

ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)
PY = sys.executable

SKEL = "blog/knitwear-sweater-trims-guide.html"
DATE_ZH = "2026年11月1日"
DATE_EN = "November 1, 2026"
DATE_JA = "2026年11月1日更新"
DATE_KO = "2026년 11월 1일 업데이트"
DATE_FR = "1 novembre 2026"
DATE_ES = "1 de noviembre de 2026"
SITEMAP_DATE = "2026-11-01"
BUST_OLD, BUST_NEW = "190", "191"
LANGS = ["en", "ja", "ko", "fr", "es"]

ARTICLES = [
    dict(
        slug="phthalate-free-apparel-packaging.html",
        body="blog/_body_phthalate.html",
        title_zh="邻苯二甲酸酯限制与无 PVC 服装包装方案 | TAGE",
        title_en="Phthalate Limits and PVC-Free Garment Packaging | TAGE",
        title_ja="フタル酸エステル規制と PVC フリーの衣料包装 | TAGE",
        title_ko="프탈레이트 규제와 PVC 프리 의류 포장 | TAGE",
        title_fr="Limites sur les phtalates et emballage sans PVC | TAGE",
        title_es="Límites de ftalatos y embalaje sin PVC | TAGE",
        desc_zh="服装包装塑化剂合规：软质 PVC 为何要加 20-40% 增塑剂，欧盟 REACH 第 51 条、美国 CPSIA 与加州 Prop 65 怎么分，五类部位的无 PVC 替代，以及用 GC-MS 报告把「无邻苯」做成可核对事实。泰阁包装。",
        desc_en="Phthalate limits in garment packaging: why soft PVC carries 20-40% plasticiser, how REACH entry 51, CPSIA and Prop 65 differ, PVC-free routes, and GC-MS proof.",
        desc_ja="衣料包装の可塑剤規制ガイド。軟質 PVC に 20〜40% の可塑剤が必要な理由、EU REACH 第 51 項・米国 CPSIA・カリフォルニア Prop 65 の違い、部位別の PVC フリー代替、GC-MS 報告書での証明方法を解説します。東莞泰閣包装。",
        desc_ko="의류 포장 가소제 규제 가이드. 연질 PVC에 20~40% 가소제가 필요한 이유, EU REACH 제51항·미국 CPSIA·캘리포니아 Prop 65의 차이, 부위별 PVC 프리 대체, GC-MS 성적서로 입증하는 방법을 정리했습니다. 둥관 TAGE 패키징.",
        desc_fr="Phtalates et emballage textile : pourquoi le PVC souple contient 20 à 40 % de plastifiant, REACH entrée 51, CPSIA et Prop 65, substitutions et preuve GC-MS.",
        desc_es="Guía de ftalatos en el embalaje textil: por qué el PVC flexible lleva 20-40 % de plastificante, REACH entrada 51, CPSIA y Prop 65, alternativas y prueba GC-MS.",
        crumb_zh="塑化剂与无 PVC",
        crumb_en="Phthalates and PVC",
        crumb_ja="可塑剤と PVC",
        crumb_ko="가소제와 PVC",
        crumb_fr="Phtalates et PVC",
        crumb_es="Ftalatos y PVC",
        h1_zh="邻苯二甲酸酯限制与无 PVC 服装包装方案",
        h1_en="Phthalate Limits and PVC-Free Garment Packaging",
        h1_ja="フタル酸エステル規制と PVC フリーの衣料包装",
        h1_ko="프탈레이트 규제와 PVC 프리 의류 포장",
        h1_fr="Limites sur les phtalates et emballage sans PVC",
        h1_es="Límites de ftalatos y embalaje sin PVC",
        tag_zh="材料合规", tag_en="Material Compliance", tag_ja="材料コンプライアンス", tag_ko="소재 컴플라이언스",
        tag_fr="Conformité matière", tag_es="Cumplimiento de material",
        sum_zh="服装包装最容易被拦下的不是纸箱，而是那只透明软胶袋——问题在塑化剂。本文分开讲欧盟 REACH 第 51 条、美国 CPSIA 与加州 Prop 65 三条线，给出袋体、窗口、挂绳、软标四类部位的无 PVC 替代路径，算清换料后的封口、透明度与印刷三笔技术账，并说明怎么用 GC-MS 报告与留样把「无邻苯」做成可核对的事实。",
        sum_en="The item most often stopped at inspection is the clear soft bag, and the issue is plasticiser. This guide separates EU REACH entry 51, US CPSIA and Prop 65, maps PVC-free routes for bag body, windows, strings and soft badges, prices the sealing, clarity and print penalties of switching, and shows how GC-MS reports and retained samples make phthalate-free checkable.",
        sum_ja="検品で最も止まりやすいのは透明の軟質袋で、論点は可塑剤です。EU REACH 第 51 項、米国 CPSIA、カリフォルニア Prop 65 を切り分け、袋本体・窓・紐・軟質バッジの PVC フリー代替、切替に伴うシール・透明性・印刷のコスト、GC-MS 報告書と保管サンプルで検証可能にする方法を整理します。",
        sum_ko="검품에서 가장 자주 걸리는 것은 투명 연질 봉투이며 쟁점은 가소제입니다. EU REACH 제51항, 미국 CPSIA, 캘리포니아 Prop 65를 구분하고, 봉투 본체·창·끈·연질 배지의 PVC 프리 대체 경로, 전환 시 봉합·투명도·인쇄 비용, GC-MS 성적서와 보관 시료로 확인 가능하게 만드는 방법을 다룹니다.",
        sum_fr="Ce qui bloque le plus souvent, c'est le sachet souple transparent, et le sujet est le plastifiant. Le guide sépare REACH entrée 51, CPSIA et Prop 65, propose des substitutions sans PVC pour corps, fenêtres, cordons et écussons, chiffre les pénalités de scellage, clarté et impression, et montre comment un rapport GC-MS rend la promesse vérifiable.",
        sum_es="Lo que más se detiene en inspección es la bolsa flexible transparente, y el tema es el plastificante. La guía separa REACH entrada 51, CPSIA y Prop 65, propone alternativas sin PVC para cuerpo, ventanas, cordones y parches, cuantifica las penalizaciones de sellado, claridad e impresión y explica cómo un informe GC-MS lo hace comprobable.",
    ),
    dict(
        slug="garment-packaging-for-returns.html",
        body="blog/_body_returns.html",
        title_zh="服装电商退货包装方案：可重封与二次销售复原 | TAGE",
        title_en="Apparel Returns Packaging: Resealable Bags and Resale Recovery | TAGE",
        title_ja="衣料 EC の返品対応包装：再封と再販復元 | TAGE",
        title_ko="의류 이커머스 반품 포장: 재밀봉과 재판매 복원 | TAGE",
        title_fr="Emballage retour mode en ligne : refermable et remise en vente | TAGE",
        title_es="Embalaje para devoluciones de moda online: resellable y recuperación | TAGE",
        desc_zh="服装电商退货包装方案：退货率 20-40% 下包材预算要上浮多少，拉链袋、可重封胶条与自锁纸盒三种结构怎么选，退货卡与外袋地址怎么预置，除皱除味补件重封四步复原，以及包材单价与降级折价怎么一起算。来自东莞泰阁包装。",
        desc_en="Returns packaging for apparel e-commerce: what a 20-40% return rate adds to the packaging budget, zip bags vs adhesive strips, return cards and resale recovery.",
        desc_ja="衣料 EC の返品対応包装。返品率 20〜40% が包材予算に与える影響、チャック袋・再封テープ・セルフロック箱の選び分け、返品カードと外袋住所の設計、シワ・臭い・付属品・再封の 4 ステップ復元を解説します。東莞泰閣包装。",
        desc_ko="의류 이커머스 반품 포장. 반품률 20~40%가 포장 예산에 미치는 영향, 지퍼백·재밀봉 테이프·자동 잠금 상자의 선택, 반품 카드와 겉봉투 주소 설계, 구김·냄새·부속·재봉합 4단계 복원을 정리했습니다. 둥관 TAGE 패키징.",
        desc_fr="Emballage retour pour la mode en ligne : ce qu'un taux de 20 à 40 % ajoute au budget, sachet zip ou bande refermable, et remise en vente.",
        desc_es="Embalaje para devoluciones de moda online: qué suma un 20-40 % de retornos al presupuesto, bolsa zip, tira resellable o caja autoblocante, tarjeta de retorno y recuperación.",
        crumb_zh="退货包装",
        crumb_en="Returns Packaging",
        crumb_ja="返品対応包装",
        crumb_ko="반품 포장",
        crumb_fr="Emballage retour",
        crumb_es="Embalaje de devoluciones",
        h1_zh="服装电商退货包装方案：可重复封口与二次销售复原",
        h1_en="Apparel Returns Packaging: Resealable Bags and Resale Recovery",
        h1_ja="衣料 EC の返品対応包装：再封構造と再販のための復元",
        h1_ko="의류 이커머스 반품 포장: 재밀봉과 재판매 복원",
        h1_fr="Emballage retour pour la mode en ligne : refermable et remise en vente",
        h1_es="Embalaje para devoluciones de moda online: resellable y recuperación",
        tag_zh="电商包装", tag_en="E-commerce Packaging", tag_ja="EC 包装", tag_ko="이커머스 포장",
        tag_fr="Emballage e-commerce", tag_es="Embalaje e-commerce",
        sum_zh="退货率 30% 意味着每 100 单有 30 单要二次包装，这笔钱不写在报价单上却真实存在于损益里。本文算清退货率对包材预算的影响，比较拉链袋、可重封胶条与自锁盒三种结构，讲透退货卡与外袋地址怎么预置、除皱除味补件重封四步复原，以及单价、工时、降级折价与体积重怎么一起算。",
        sum_en="A 30% return rate means 30 of every 100 orders need a second pack, a cost that never appears on the quotation. This guide sizes its effect on the packaging budget, compares zip bags, resealable strips and self-lock boxes, sets out return cards and outer-bag addressing, the four recovery steps, and how price, labour, markdown and volumetric weight add up.",
        sum_ja="返品率 30% なら 100 注文のうち 30 件が再梱包となり、見積書に出ないコストが損益に残ります。包材予算への影響を計算し、チャック袋・再封テープ・セルフロック箱を比較、返品カードと外袋住所の設計、シワ・臭い・付属品・再封の 4 ステップ、単価・工数・値引き・容積重量の合算を整理します。",
        sum_ko="반품률 30%면 100건 중 30건이 재포장 대상이며 견적서에 없는 비용이 손익에 남습니다. 포장 예산에 미치는 영향을 계산하고, 지퍼백·재밀봉 스트립·자동 잠금 상자를 비교하며, 반품 카드와 겉봉투 주소 설계, 4단계 복원, 단가·공수·할인·부피 무게 합산을 다룹니다.",
        sum_fr="Un taux de retour de 30 % signifie 30 commandes sur 100 à remballer, un coût absent du devis mais bien présent au résultat. Le guide chiffre l'effet sur le budget, compare sachet zip, bande refermable et coffret auto-bloquant, détaille carte retour, adressage, les quatre étapes de récupération et l'addition prix, main-d'œuvre, décote et poids volumétrique.",
        sum_es="Un 30 % de devoluciones implica 30 de cada 100 pedidos con segundo embalaje, un coste que no está en la cotización. La guía mide el efecto en el presupuesto, compara bolsa zip, tira resellable y caja autoblocante, detalla tarjeta de retorno, direccionado, los cuatro pasos de recuperación y la suma de precio, mano de obra, descuento y peso volumétrico.",
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
