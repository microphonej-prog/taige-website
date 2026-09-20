#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-09-20 每日更新：生成 2 篇新文章（六语：zh-Hant 根 / en / ja / ko / fr / es）
+ 列表页卡片 + gen_i18n 五语生成 + sitemap + BUST_VERSION 升级 + 繁体转换。

用法: python daily_gen_20260920.py
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
BUST_OLD, BUST_NEW = "92", "93"
LANGS = ["en", "ja", "ko", "fr", "es"]

ARTICLES = [
    dict(
        slug="hang-tag-double-sided-printing.html",
        body="blog/_body_hangtag_2sided.html",
        title_zh="吊牌双面印刷指南：正反面内容分配、套准与纸张怎么选 | TAGE",
        title_en="Double-Sided Hang Tags: Front &amp; Back Content, Registration &amp; Paper | TAGE",
        title_ja="タグの両面印刷ガイド：表裏の内容配分・見当精度・用紙の選び方 | TAGE",
        title_ko="행택 양면 인쇄 가이드: 앞뒷면 내용 배분, 정합, 용지 선택 | TAGE",
        title_fr="Étiquettes suspendues recto-verso : contenu, repérage et papier | TAGE",
        title_es="Etiquetas colgantes a doble cara: contenido, registro y papel | TAGE",
        desc_zh="吊牌双面印刷指南：正面放品牌与视觉、背面放成分洗护与条码，讲清套准公差怎么定、纸张克重与透印的关系、覆膜与表面处理的取舍、双面工艺的成本增量，以及下单前要写清的六项参数。来自东莞泰阁包装。",
        desc_en="Double-sided hang tags: splitting front and back content, registration tolerance, paper weight versus show-through, lamination and the extra cost involved.",
        desc_ja="タグの両面印刷ガイド。表裏の内容配分、見当公差の決め方、用紙の目付と裏写りの関係、ラミネートと表面加工の取舍、両面加工のコスト増、発注前に明記すべき6項目を解説します。東莞泰閣包装。",
        desc_ko="행택 양면 인쇄 가이드: 앞뒷면 내용 배분, 정합 공차 설정, 용지 평량과 비침의 관계, 라미네이팅과 표면 가공의 선택, 양면 가공의 비용 증가, 발주 전 명시할 6가지 항목을 정리했습니다. 둥관 TAGE 패키징.",
        desc_fr="Étiquettes suspendues recto-verso : répartition des contenus, tolérance de repérage, grammage et transparence, pelliculage et surcoût du recto-verso.",
        desc_es="Etiquetas colgantes a doble cara: reparto de contenido, tolerancia de registro, gramaje y transparencia, laminado y sobrecoste de la doble cara.",
        crumb_zh="吊牌双面印刷", crumb_en="Double-Sided Hang Tags", crumb_ja="タグの両面印刷",
        crumb_ko="행택 양면 인쇄", crumb_fr="Recto-verso des étiquettes", crumb_es="Etiquetas a doble cara",
        h1_zh="吊牌双面印刷指南：正反面内容分配、套准与纸张选择",
        h1_en="Double-Sided Hang Tags: Splitting Content, Registration and Paper Choice",
        h1_ja="タグの両面印刷ガイド：表裏の内容配分、見当精度、用紙の選び方",
        h1_ko="행택 양면 인쇄 가이드: 앞뒷면 내용 배분, 정합, 용지 선택",
        h1_fr="Étiquettes suspendues recto-verso : partage du contenu, repérage et papier",
        h1_es="Etiquetas colgantes a doble cara: reparto de contenido, registro y papel",
        tag_zh="工艺指南", tag_en="Printing", tag_ja="加工ガイド", tag_ko="가공 가이드",
        tag_fr="Impression", tag_es="Impresión",
        sum_zh="双面印刷不等于把单面内容印两遍：第二次上机要再走一遍印刷、干燥与套准，色彩叠加与纸张形变都会变。本文讲清什么情况该做双面、正反面内容怎么分工、套准公差按 ±1.0 mm 还是 ±0.5 mm 提要求、克重与透印的关系、覆膜与背面过油怎么取舍，以及双面比单面贵在哪、下单前六项确认清单。",
        sum_en="Double-sided printing is not running the front artwork twice: a second pass re-runs printing, drying and registration. This guide covers when a tag needs two sides, how to split front and back, whether to ask ±1.0 mm or ±0.5 mm, grammage versus show-through, lamination choices, where the extra cost comes from and a six-point order checklist.",
        sum_ja="両面印刷は片面データを2回刷ることではありません。2度目の印刷ではインキの重なりや用紙の伸縮が変わります。両面にすべきケース、表裏の内容分担、見当公差を±1.0mmと±0.5mmのどちらで指定するか、目付と裏写りの関係、ラミネートと裏面ニスの取舍、片面とのコスト差、発注前の6項目チェックリストを解説します。",
        sum_ko="양면 인쇄는 단면 데이터를 두 번 찍는 것이 아닙니다. 두 번째 인쇄는 잉크 겹침과 용지 변형을 다시 만듭니다. 양면이 필요한 경우, 앞뒤 내용 배분, 정합 공차를 ±1.0mm와 ±0.5mm 중 무엇으로 요구할지, 평량과 비침의 관계, 라미네이팅과 뒷면 바니시의 선택, 단면 대비 비용 차이, 발주 전 6가지 확인 리스트를 정리했습니다.",
        sum_fr="Le recto-verso n'est pas l'impression du visuel recto deux fois : un second passage refait impression, séchage et repérage. Ce guide traite les cas qui justifient deux faces, la répartition recto/verso, le choix entre ±1,0 mm et ±0,5 mm de repérage, le grammage et la transparence, le pelliculage, le surcoût et une liste en six points.",
        sum_es="La doble cara no es imprimir el arte de una cara dos veces: una segunda pasada rehace impresión, secado y registro. Esta guía trata cuándo hacen falta dos caras, cómo repartir el contenido, si pedir ±1,0 mm o ±0,5 mm, gramaje y transparencia, laminado, de dónde viene el sobrecoste y una lista de seis puntos.",
    ),
    dict(
        slug="trim-quotation-comparison-guide.html",
        body="blog/_body_rfq.html",
        title_zh="服装辅料报价单怎么比对：8 个必问项与隐藏成本清单 | TAGE",
        title_en="Comparing Trim Quotations: 8 Must-Ask Questions &amp; Hidden Costs | TAGE",
        title_ja="副資材の見積書の比較方法：必須質問8項目と隠れコスト | TAGE",
        title_ko="부자재 견적서 비교 방법: 필수 질문 8가지와 숨은 비용 | TAGE",
        title_fr="Comparer les devis d'accessoires : 8 questions et coûts cachés | TAGE",
        title_es="Comparar presupuestos de accesorios: 8 preguntas y costes ocultos | TAGE",
        desc_zh="服装辅料报价单比对指南：同一份规格三家报价差 30% 往往不是价格问题而是口径不同。讲清按张与按千张、含税与不含税、含运费与出厂价的换算方式，八个必问项、隐藏成本清单、打样费大货抵扣怎么问，以及收到报价后的四步比对法。来自东莞泰阁包装。",
        desc_en="How to compare apparel trim quotations: align the pricing basis first, then close the gaps with eight must-ask questions, amortise one-off costs and catch hidden charges.",
        desc_ja="副資材の見積書の比較ガイド。3社で30%以上の差が出るのは価格ではなく見積条件の違いが原因です。1枚／1,000枚単位、税込／税別、運賃込み／工場渡しの換算、必須質問8項目、隠れコスト一覧、サンプル代の相殺、4ステップの比較法を解説します。東莞泰閣包装。",
        desc_ko="부자재 견적서 비교 가이드. 세 곳의 견적이 30% 이상 차이 나는 이유는 가격이 아니라 기준이 다르기 때문입니다. 장당/천 장, 세금 포함/별도, 운임 포함/공장도 환산법, 필수 질문 8가지, 숨은 비용 목록, 샘플비 상계, 4단계 비교법을 정리했습니다. 둥관 TAGE 패키징.",
        desc_fr="Comparer les devis d'accessoires : aligner la base de prix, poser huit questions incontournables, amortir les frais ponctuels et repérer les coûts cachés.",
        desc_es="Comparar presupuestos de accesorios: alinear la base de precio, hacer ocho preguntas imprescindibles, amortizar costes puntuales y detectar cargos ocultos.",
        crumb_zh="报价单比对", crumb_en="Quote Comparison", crumb_ja="見積書の比較",
        crumb_ko="견적 비교", crumb_fr="Comparaison des devis", crumb_es="Comparación de presupuestos",
        h1_zh="服装辅料报价单怎么比对：八个必问项与隐藏成本清单",
        h1_en="How to Compare Apparel Trim Quotations: Eight Must-Ask Questions and Hidden Costs",
        h1_ja="副資材の見積書の比較方法：8つの必須質問と隠れコスト一覧",
        h1_ko="부자재 견적서 비교 방법: 8가지 필수 질문과 숨은 비용 목록",
        h1_fr="Comparer les devis d'accessoires : huit questions et coûts cachés",
        h1_es="Cómo comparar presupuestos de accesorios: ocho preguntas y costes ocultos",
        tag_zh="采购实务", tag_en="Sourcing", tag_ja="調達実務", tag_ko="소싱 실무",
        tag_fr="Approvisionnement", tag_es="Compras",
        sum_zh="同一份辅料规格发给三家供应商，报价差经常超过 30%，多数时候差的是口径而不是价格：按张还是按千张、含不含税、含不含运费、打样费算不算在单价里。本文给出一套可复用的比对方法——先统一口径，再用八个必问项补齐报价，把一次性费用按年用量摊进单价，并列出六项隐藏成本与打样费抵扣的问法。",
        sum_en="Send one trim specification to three suppliers and the quotes can differ by more than 30% — usually because the basis differs, not the price. This guide gives a reusable method: align the basis, close every gap with eight must-ask questions, amortise one-off charges over annual volume, plus six hidden costs and how to ask about sampling credits.",
        sum_ja="同じ副資材仕様を3社に見積依頼すると30%以上違うことがあります。差の多くは価格ではなく条件です。1枚か1,000枚か、税込か税別か、運賃込みか別か、サンプル代が単価に含まれるか。条件を揃え、8つの必須質問で見積を埋め、一時費用を年間使用量で単価に按分する再利用可能な比較手順と、6つの隠れコスト、サンプル代相殺の聞き方を示します。",
        sum_ko="같은 부자재 사양을 세 곳에 보내면 견적이 30% 이상 차이 나는 경우가 흔합니다. 대부분 가격이 아니라 기준의 차이입니다. 장당인지 천 장인지, 세금 포함인지, 운임 포함인지, 샘플비가 단가에 포함되는지. 기준을 맞추고 8가지 필수 질문으로 견적을 채우고 일회성 비용을 연간 사용량으로 배분하는 비교 방법과 6가지 숨은 비용, 샘플비 상계 질문법을 제시합니다.",
        sum_fr="Trois fournisseurs, une même spécification, plus de 30 % d'écart : la différence vient souvent de la base, pas du prix. Ce guide propose une méthode réutilisable — aligner la base, combler chaque devis par huit questions incontournables, amortir les frais ponctuels — avec six coûts cachés et comment négocier l'avoir sur échantillon.",
        sum_es="Tres proveedores y una misma especificación pueden dar más de un 30 % de diferencia, casi siempre por la base, no por el precio. Esta guía ofrece un método reutilizable: alinear la base, cerrar cada presupuesto con ocho preguntas imprescindibles, amortizar los costes puntuales, más seis costes ocultos y cómo negociar el abono de la muestra.",
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
                  % (a["title_zh"], a["title_en"], a["title_ja"], a["title_ko"], a["title_fr"], a["title_es"], a["title_zh"]))
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
             % (a["crumb_zh"], a["crumb_en"], a["crumb_ja"], a["crumb_ko"], a["crumb_fr"], a["crumb_es"], a["crumb_zh"]))
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
    if n != 1:  # 繁体转换后的骨架
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
    print("写入 %s (%d KB) desc_en=%d desc_fr=%d desc_es=%d desc_zh=%d"
          % (out, len(s.encode("utf-8")) // 1024, len(a["desc_en"]), len(a["desc_fr"]), len(a["desc_es"]), len(a["desc_zh"])))

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
        tag_zh=a["tag_zh"], tag_en=a["tag_en"], tag_ja=a["tag_ja"], tag_ko=a["tag_ko"], tag_fr=a["tag_fr"], tag_es=a["tag_es"],
        h3_zh=a["h1_zh"], h3_en=a["h1_en"], h3_ja=a["h1_ja"], h3_ko=a["h1_ko"], h3_fr=a["h1_fr"], h3_es=a["h1_es"],
        sum_zh=a["sum_zh"], sum_en=a["sum_en"], sum_ja=a["sum_ja"], sum_ko=a["sum_ko"], sum_fr=a["sum_fr"], sum_es=a["sum_es"],
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
             ["https://taigetag.com/%s/blog/%s" % (l, slug) for l in ["en", "ja", "ko", "fr", "es"]]:
        assert "<loc>%s</loc>" % u not in sm, "sitemap 已有 %s" % u
        blocks.append(block(u))
sm = sm.replace("</urlset>", "".join(blocks) + "</urlset>", 1)

# blog 首页 lastmod 更新（六语）
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
