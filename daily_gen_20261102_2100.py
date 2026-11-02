#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-11-02 21:00 补跑批次（六语：zh-Hant 根 / en / ja / ko / fr / es）
- 服装标签自打印还是外发预印（garment-label-inhouse-printing-vs-outsourcing）
- 服装辅料出口报价的币种与汇率条款（trim-order-currency-exchange-guide）

用法: F:/hermes/venvs/tools/Scripts/python.exe daily_gen_20261102_2100.py [--check]
"""
import os, re, sys, subprocess, importlib.util

ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)
PY = sys.executable

SKEL = "blog/knitwear-sweater-trims-guide.html"
DATE_ZH = "2026年11月2日"
DATE_EN = "November 2, 2026"
DATE_JA = "2026年11月2日"
DATE_KO = "2026년 11월 2일 업데이트"
DATE_FR = "2 novembre 2026"
DATE_ES = "2 de noviembre de 2026"
SITEMAP_DATE = "2026-11-02"
BUST_OLD, BUST_NEW = "193", "194"
LANGS = ["en", "ja", "ko", "fr", "es"]

ARTICLES = [
    dict(
        slug="garment-label-inhouse-printing-vs-outsourcing.html",
        body="blog/_body_inhouse.html",
        title_zh="服装标签自打印还是外发预印：成本、耐洗与合规对比 | TAGE",
        title_en="In-House Label Printing or Pre-Printed Labels: Cost and Wash Comparison | TAGE",
        title_ja="タグの内製印刷と外注プレ印刷：コスト・耐洗・コンプライアンスの比較 | TAGE",
        title_ko="라벨 자체 인쇄와 외주 사전 인쇄: 비용·세탁·컴플라이언스 비교 | TAGE",
        title_fr="Imprimer ses étiquettes ou les acheter pré-imprimées : coût et lavage | TAGE",
        title_es="Imprimir etiquetas en casa o comprarlas preimpresas: coste y lavado | TAGE",
        desc_zh="服装标签自打印与外发预印的取舍指南：碳带与基材的耐洗边界、四项隐性成本、成分与语言版本的合规风险，以及主力外发、长尾自打的混合方案与决策清单。来自东莞泰阁包装。",
        desc_en="In-house label printing vs pre-printed labels: cost structure, ribbon and stock wash limits, compliance risk, and a hybrid model that fits small batches.",
        desc_ja="タグの内製印刷と外注プレ印刷の比較ガイド。リボンと素材による耐洗の限界、4つの隠れコスト、混用率と言語版のコンプライアンスリスク、主力は外注・ロングテールは内製というハイブリッド運用と判断チェックリストを解説します。東莞泰閣包装。",
        desc_ko="라벨 자체 인쇄와 외주 사전 인쇄 비교 가이드. 리본과 소재에 따른 세탁 한계, 네 가지 숨은 비용, 혼용률·언어판 컴플라이언스 리스크, 주력은 외주·롱테일은 자체 인쇄라는 하이브리드 운영과 판단 체크리스트를 정리했습니다. 둥관 TAGE 패키징.",
        desc_fr="Imprimer ses étiquettes ou les acheter pré-imprimées : structure de coût, limites au lavage des rubans et supports, risque de conformité et modèle hybride.",
        desc_es="Imprimir etiquetas en casa o comprarlas preimpresas: estructura de coste, límites de lavado de cintas y soportes, riesgo de cumplimiento y modelo híbrido.",
        crumb_zh="自打与外发预印",
        crumb_en="In-House vs Pre-Printed",
        crumb_ja="内製と外注",
        crumb_ko="자체 인쇄와 외주",
        crumb_fr="Interne ou pré-imprimé",
        crumb_es="Interno o preimpreso",
        h1_zh="服装标签自打印还是外发预印：成本、耐洗与合规对比",
        h1_en="In-House Label Printing or Pre-Printed Labels: Cost, Wash and Compliance",
        h1_ja="タグの内製印刷と外注プレ印刷：コスト・耐洗・コンプライアンスの比較",
        h1_ko="라벨 자체 인쇄와 외주 사전 인쇄: 비용·세탁·컴플라이언스 비교",
        h1_fr="Imprimer ses étiquettes ou les acheter pré-imprimées : coût, lavage et conformité",
        h1_es="Imprimir etiquetas en casa o comprarlas preimpresas: coste, lavado y cumplimiento",
        tag_zh="标签对比", tag_en="Label Comparison", tag_ja="ラベル比較", tag_ko="라벨 비교",
        tag_fr="Comparatif labels", tag_es="Comparativa de etiquetas",
        sum_zh="自打印与外发预印的取舍，关键不在设备价格。本文对比两种交付形态在单件成本、换版速度与质感上限上的差别，列出容易被忽略的四项隐性成本，讲清蜡基与树脂基碳带的耐洗边界、成分与语言版本的合规风险，并给出主力外发、长尾自打的混合模式与一张决策清单。",
        sum_en="The choice between in-house and pre-printed labels is not about printer price. This guide compares unit cost, changeover speed and finish ceiling, lists four hidden costs, sets out the wash limits of wax versus resin ribbons, the compliance risk in fibre content and language versions, and a hybrid model with a decision checklist.",
        sum_ja="内製か外注かは設備価格では決まりません。単価、版替えの速さ、質感の上限を比較し、見落としやすい4つの隠れコスト、ワックスとレジンの耐洗限界、混用率と言語版のリスク、主力は外注・ロングテールは内製というハイブリッド運用と判断チェックリストを示します。",
        sum_ko="자체 인쇄와 외주 사전 인쇄의 선택은 설비 가격이 아닙니다. 단가, 판 교체 속도, 질감 상한을 비교하고 놓치기 쉬운 네 가지 숨은 비용, 왁스와 레진 리본의 세탁 한계, 혼용률·언어판 리스크, 주력 외주·롱테일 자체 인쇄라는 하이브리드 운영과 판단 체크리스트를 제시합니다.",
        sum_fr="Le choix entre interne et pré-imprimé ne dépend pas du prix de l'imprimante. Ce guide compare coût unitaire, vitesse de changement et plafond de rendu, liste quatre coûts cachés, précise les limites au lavage des rubans cire et résine, le risque de conformité et un modèle hybride avec liste de décision.",
        sum_es="La elección entre imprimir en casa y comprar preimpreso no depende del precio de la impresora. Esta guía compara coste unitario, velocidad de cambio y techo de acabado, enumera cuatro costes ocultos, fija los límites de lavado de cintas de cera y resina, el riesgo de cumplimiento y un modelo híbrido con lista de decisión.",
    ),
    dict(
        slug="trim-order-currency-exchange-guide.html",
        body="blog/_body_fx.html",
        title_zh="服装辅料出口报价的币种与汇率条款指南 | TAGE",
        title_en="Currency and Exchange Rate Clauses for Trim Export Quotations | TAGE",
        title_ja="副資材輸出見積の通貨と為替条項ガイド | TAGE",
        title_ko="부자재 수출 견적의 통화와 환율 조항 가이드 | TAGE",
        title_fr="Devise et clause de change dans les devis d'export d'accessoires | TAGE",
        title_es="Divisa y cláusula de cambio en presupuestos de exportación de accesorios | TAGE",
        desc_zh="辅料出口报价的币种与汇率条款指南：美元、欧元与本币报价的代价，四种汇率风险分担方式，基准汇率与取值日怎么写，付款方式的结汇成本，附可直接照抄的条款清单。来自东莞泰阁包装。",
        desc_en="Currency and exchange clauses for trim quotations: what USD, EUR and local pricing cost, four ways to share FX risk, reference rates and payment costs.",
        desc_ja="副資材輸出見積の通貨と為替条項ガイド。ドル・ユーロ・現地通貨建てのコスト、為替リスク分担の4方式、基準レートと適用日の書き方、決済方法ごとの両替コスト、そのまま使える条項リストを解説します。東莞泰閣包装。",
        desc_ko="부자재 수출 견적의 통화와 환율 조항 가이드. 달러·유로·현지 통화 표기의 대가, 환율 리스크 분담 네 가지 방식, 기준 환율과 적용일 표기, 결제 방식별 환전 비용, 바로 쓸 수 있는 조항 목록을 정리했습니다. 둥관 TAGE 패키징.",
        desc_fr="Devise et clause de change dans les devis : coût réel d'une cotation en dollars, euros ou monnaie locale, quatre partages du risque et taux de référence.",
        desc_es="Divisa y cláusula de cambio en presupuestos: coste de cotizar en dólares, euros o moneda local, cuatro formas de repartir el riesgo y tipo de referencia.",
        crumb_zh="币种与汇率条款",
        crumb_en="Currency and FX Clauses",
        crumb_ja="通貨と為替条項",
        crumb_ko="통화와 환율 조항",
        crumb_fr="Devise et clause de change",
        crumb_es="Divisa y cláusula de cambio",
        h1_zh="服装辅料出口报价的币种与汇率条款指南",
        h1_en="Currency and Exchange Rate Clauses for Trim Export Quotations",
        h1_ja="副資材輸出見積の通貨と為替条項ガイド",
        h1_ko="부자재 수출 견적의 통화와 환율 조항 가이드",
        h1_fr="Devise et clause de change dans les devis d'export d'accessoires",
        h1_es="Divisa y cláusula de cambio en presupuestos de exportación de accesorios",
        tag_zh="采购实务", tag_en="Sourcing Practice", tag_ja="購買実務", tag_ko="구매 실무",
        tag_fr="Pratique d'achat", tag_es="Práctica de compra",
        sum_zh="辅料单价谈定、结算金额却对不上，多数时候不是数量问题，而是币种与汇率。本文讲清美元、欧元、人民币与买方本币报价各自的代价，四种汇率风险分担方式，基准汇率与取值日怎么写才不吵，付款方式带来的结汇成本，并附一份可以直接照着写的条款清单。",
        sum_en="When the trim price is agreed but the settlement does not match, the gap is usually currency, not quantity. This guide covers what USD, EUR, CNY and buyer-currency pricing each cost, four ways to share FX risk, how to write the reference rate and fixing date so nobody argues, the conversion cost of each payment method, and a clause list to copy.",
        sum_ja="単価は合意したのに決済額が合わない。多くは数量ではなく通貨と為替です。ドル・ユーロ・人民元・買い手通貨それぞれのコスト、為替リスク分担の4方式、揉めない基準レートと適用日の書き方、決済方法ごとの両替コスト、そのまま使える条項リストをまとめます。",
        sum_ko="단가는 합의했는데 결제 금액이 맞지 않을 때, 대개 수량이 아니라 통화와 환율 문제입니다. 달러·유로·위안·구매자 통화 표기의 각 비용, 환율 리스크 분담 네 가지 방식, 다투지 않는 기준 환율과 적용일 표기, 결제 방식별 환전 비용, 바로 쓸 조항 목록을 정리합니다.",
        sum_fr="Le prix est validé mais le règlement ne colle pas : l'écart vient de la devise, pas des quantités. Ce guide traite le coût réel d'une cotation en dollars, euros, yuans ou monnaie locale, quatre partages du risque de change, la rédaction du taux et de la date de fixation, le coût de conversion par mode de paiement et une liste de clauses à recopier.",
        sum_es="El precio se pacta pero la liquidación no cuadra: la diferencia suele ser de moneda, no de cantidad. Esta guía trata el coste real de cotizar en dólares, euros, yuanes o moneda del comprador, cuatro formas de repartir el riesgo, cómo redactar tipo y fecha de aplicación sin discutir, el coste de conversión de cada pago y una lista de cláusulas.",
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
    print("  %-50s desc_zh=%d字 desc_en=%d字符 desc_ja=%d desc_ko=%d desc_fr=%d desc_es=%d"
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


def block(url):
    return ("  <url>\r\n    <loc>%s</loc>\r\n    <lastmod>%s</lastmod>\r\n"
            "    <changefreq>monthly</changefreq>\r\n    <priority>0.7</priority>\r\n  </url>\r\n"
            % (url, SITEMAP_DATE))


sm = open("sitemap.xml", encoding="utf-8", newline="").read()
before = sm.count("<loc>")
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
print("sitemap 新增 %d 个 URL，<loc> %d -> %d" % (len(blocks), before, sm.count("<loc>")))

# ---------------- 6) BUST_VERSION 升级 ----------------
mj = open("js/main.js", encoding="utf-8").read()
assert 'var BUST_VERSION = "%s";' % BUST_OLD in mj, "BUST_VERSION 不是 %s" % BUST_OLD
mj = mj.replace('var BUST_VERSION = "%s";' % BUST_OLD, 'var BUST_VERSION = "%s";' % BUST_NEW, 1)
open("js/main.js", "w", encoding="utf-8", newline="").write(mj)
print("BUST_VERSION %s -> %s" % (BUST_OLD, BUST_NEW))
