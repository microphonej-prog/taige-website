#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-09-26 早间 每日更新：2 篇新文章（六语：zh-Hant 根 / en / ja / ko / fr / es）
- 服装辅料订购数量与单位换算指南：码/米/卷/打/张怎么算，损耗率留多少
- 服装辅料耐热与整烫适配指南：压烫温度下标签怎么不变形
（主题池 30 个选题均已上线，本次为运营/工艺扩展新选题，已核对 blog/ 与 sitemap 无重复）

用法: <python> daily_gen_20260926_am.py
"""
import os, re, sys, subprocess, importlib.util

ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)
PY = sys.executable

SKEL = "blog/knitwear-sweater-trims-guide.html"
DATE_ZH = "2026年9月26日"
DATE_EN = "September 26, 2026"
DATE_JA = "2026年9月26日更新"
DATE_KO = "2026년 9월 26일 업데이트"
DATE_FR = "26 septembre 2026"
DATE_ES = "26 de septiembre de 2026"
SITEMAP_DATE = "2026-09-26"
BUST_OLD, BUST_NEW = "110", "111"
LANGS = ["en", "ja", "ko", "fr", "es"]

ARTICLES = [
    dict(
        slug="trim-order-quantity-unit-conversion.html",
        body="blog/_body_qty.html",
        title_zh="服装辅料订购数量与单位换算指南：码/米/卷/打怎么算 | TAGE",
        title_en="Trim Order Quantities &amp; Unit Conversion: Yards, Metres, Dozens, Rolls | TAGE",
        title_ja="衣料副資材の発注数量と単位換算ガイド：ヤード・メートル・ダース・ロールの計算 | TAGE",
        title_ko="의류 부자재 발주 수량과 단위 환산 가이드: 야드·미터·다스·롤 계산 | TAGE",
        title_fr="Quantités et conversion d'unités pour les accessoires : yards, mètres, douzaines | TAGE",
        title_es="Cantidades y conversión de unidades en accesorios: yardas, metros, docenas | TAGE",
        desc_zh="服装辅料订购数量与单位换算指南：从 BOM 单耗算出下单量，讲清码与米、打、卷、张的换算关系，四类辅料的损耗率区间、起订量与整数倍、溢短装验收口径，附可直接抄进询价邮件的数量确认表。来自东莞泰阁包装。",
        desc_en="Trim order quantities and unit conversion: work out usage per garment from the BOM, convert yards, metres, dozens and rolls, set waste rates and tolerance.",
        desc_ja="衣料副資材の発注数量と単位換算ガイド。BOMから1着あたりの使用量を算出し、ヤード・メートル・ダース・ロールの換算、品目別ロス率、最小ロットと倍数、過不足納入の検収基準、そのまま見積りメールに使える数量確認シートを解説します。東莞泰閣包装。",
        desc_ko="의류 부자재 발주 수량과 단위 환산 가이드. BOM에서 착장당 사용량을 계산하고 야드·미터·다스·롤 환산, 품목별 로스율, 최소 수량과 배수, 과부족 납품 검수 기준, 견적 메일에 바로 쓰는 수량 확인 시트를 정리했습니다. 둥관 TAGE 패키징.",
        desc_fr="Quantités et conversion d'unités pour les accessoires : consommation par vêtement depuis la nomenclature, yards et mètres, pertes, minimums et tolérance de livraison.",
        desc_es="Cantidades y conversión de unidades en accesorios: consumo por prenda desde la lista de materiales, yardas y metros, merma, mínimos y tolerancia de entrega.",
        crumb_zh="订购数量与单位换算", crumb_en="Order Quantities &amp; Units", crumb_ja="発注数量と単位換算",
        crumb_ko="발주 수량과 단위 환산", crumb_fr="Quantités et unités", crumb_es="Cantidades y unidades",
        h1_zh="服装辅料订购数量与单位换算指南：码/米/卷/打怎么算，损耗率留多少",
        h1_en="Trim Order Quantities and Unit Conversion: Yards, Metres, Dozens and Rolls",
        h1_ja="衣料副資材の発注数量と単位換算ガイド：ヤード・メートル・ダース・ロールの計算",
        h1_ko="의류 부자재 발주 수량과 단위 환산 가이드: 야드·미터·다스·롤 계산",
        h1_fr="Quantités et conversion d'unités pour les accessoires : yards, mètres, douzaines",
        h1_es="Cantidades y conversión de unidades en accesorios: yardas, metros, docenas",
        tag_zh="采购指南", tag_en="Sourcing Guide", tag_ja="調達ガイド", tag_ko="소싱 가이드",
        tag_fr="Guide d'achat", tag_es="Guía de compra",
        sum_zh="辅料下单最常错在数量而不是价格：织唛按 3000 个订给 3000 件成衣，剪标补片一用就短；把「码」当「米」报给工厂，到货少 8%。本文把单耗计算、单位换算表、四类辅料的损耗率区间、起订量与整数倍、溢短装验收口径讲清，并给出一张可以直接抄进询价邮件的数量确认表。",
        sum_en="Trims are more often wrong on quantity than on price: 3,000 labels for 3,000 garments runs short after a single re-cut, and quoting yards to a mill that prices in metres loses 8%. This guide covers consumption maths, a conversion table, waste ranges by family, minimums and multiples, and acceptance tolerance, with a quantity sheet to copy into your enquiry.",
        sum_ja="副資材の発注は価格より数量で失敗します。3,000着に織りラベル3,000枚では裁ち直し一回で不足し、ヤードで伝えた数量は8%少なくなります。本記事は単耗の計算、単位換算表、品目別ロス率、最小ロットと倍数、過不足納入の検収基準を整理し、見積りメールにそのまま使える数量確認シートを掲載します。",
        sum_ko="부자재 발주는 가격보다 수량에서 실수가 많습니다. 3,000장에 직조 라벨 3,000개면 재단 한 번에 부족해지고, 야드로 전달한 수량은 8% 모자랍니다. 이 글은 소요량 계산, 단위 환산표, 품목별 로스율, 최소 수량과 배수, 과부족 납품 검수 기준을 정리하고 견적 메일에 바로 쓰는 수량 확인 시트를 제공합니다.",
        sum_fr="Sur les accessoires, les erreurs portent plus souvent sur la quantité que sur le prix : 3 000 tissés pour 3 000 pièces deviennent insuffisants après une reprise, et annoncer des yards à un atelier qui chiffre en mètres fait perdre 8 %. Ce guide couvre consommation, table de conversion, pertes par famille, minimums et tolérance de livraison.",
        sum_es="En accesorios se falla más en la cantidad que en el precio: 3.000 tejidas para 3.000 prendas quedan cortas tras un solo recorte, y dar yardas a un taller que cotiza en metros pierde un 8 %. Esta guía cubre consumo, tabla de conversión, merma por familia, mínimos y tolerancia de entrega.",
    ),
    dict(
        slug="trim-ironing-heat-resistance-guide.html",
        body="blog/_body_iron.html",
        title_zh="服装辅料耐热与整烫适配指南：标签在压烫下怎么不变形 | TAGE",
        title_en="Heat Resistance &amp; Ironing Compatibility for Garment Trims | TAGE",
        title_ja="衣料副資材の耐熱とプレス適性ガイド：ラベルが変形しない条件 | TAGE",
        title_ko="의류 부자재 내열과 프레스 적합성 가이드: 라벨 변형을 막는 조건 | TAGE",
        title_fr="Tenue à la chaleur et compatibilité au repassage des accessoires | TAGE",
        title_es="Resistencia al calor y compatibilidad con el planchado de accesorios | TAGE",
        desc_zh="服装辅料耐热与整烫适配指南：洗水测试通过却在整烫翻车的原因，织唛、涂层洗水标、热转印标与吊牌的耐热参考，发硬卷曲、色迁移泛黄、脱边起泡三类事故的处理，以及温度阶梯试样与整烫参数申报表。来自东莞泰阁包装。",
        desc_en="Heat resistance and ironing compatibility for trims: why labels pass washing but fail pressing, temperature ceilings by material, and how to run a test ladder.",
        desc_ja="衣料副資材の耐熱とプレス適性ガイド。洗濯は通るのにプレスで失敗する理由、材質別の耐熱目安、硬化・カール・色移り・剥離の対処、温度段階サンプルとプレス条件の申告シートを解説します。東莞泰閣包装。",
        desc_ko="의류 부자재 내열과 프레스 적합성 가이드. 세탁은 통과하지만 프레스에서 실패하는 이유, 소재별 내열 기준, 경화·말림·이염·박리 대처, 온도 단계 샘플과 프레스 조건 신고서를 정리했습니다. 둥관 TAGE 패키징.",
        desc_fr="Tenue à la chaleur des accessoires : pourquoi les étiquettes passent le lavage mais échouent à la presse, repères par matière, escalier thermique et contrôle après lavage.",
        desc_es="Resistencia al calor de los accesorios: por qué la etiqueta pasa el lavado y falla en la prensa, referencias por material, escalera térmica y revisión tras el lavado.",
        crumb_zh="耐热与整烫适配", crumb_en="Heat &amp; Ironing", crumb_ja="耐熱とプレス適性",
        crumb_ko="내열과 프레스 적합성", crumb_fr="Chaleur et repassage", crumb_es="Calor y planchado",
        h1_zh="服装辅料耐热与整烫适配指南：标签在压烫下怎么不变形、不脱边",
        h1_en="Heat Resistance and Ironing Compatibility for Garment Trims",
        h1_ja="衣料副資材の耐熱とプレス適性ガイド：ラベルが変形・剥離しない条件",
        h1_ko="의류 부자재 내열과 프레스 적합성 가이드: 라벨이 변형·박리되지 않는 조건",
        h1_fr="Tenue à la chaleur et compatibilité au repassage des accessoires",
        h1_es="Resistencia al calor y compatibilidad con el planchado de los accesorios",
        tag_zh="工艺指南", tag_en="Process Guide", tag_ja="加工ガイド", tag_ko="공정 가이드",
        tag_fr="Guide technique", tag_es="Guía técnica",
        sum_zh="辅料在洗水测试里正常，却在大货整烫时发硬卷曲、印层起泡、烫金被压出亮痕、热转印边缘发白脱落。原因通常不是质量差，而是标签的耐热上限与成衣厂整烫参数不匹配。本文按材质给出温度参考、讲清三类典型事故的处理，并附温度阶梯试样方法与整烫参数申报表。",
        sum_en="Trims pass every wash test and then fail at the ironing station: stiff curled edges, blistered print, press marks on foil, whitened transfer edges. The cause is usually a mismatch between the label's heat ceiling and the factory's pressing settings, not poor quality. This guide gives material-based references, three typical failures and a temperature-ladder test method.",
        sum_ja="洗濯テストは通ったのに量産プレスで硬化・カール、印刷の膨れ、箔の押し跡、熱転写端の白化が起きます。原因は品質不良ではなく、ラベルの耐熱上限と縫製工場のプレス条件の不一致がほとんどです。材質別の温度目安、3つの典型不具合、温度段階サンプルとプレス条件シートを解説します。",
        sum_ko="세탁 테스트는 통과했는데 양산 프레스에서 경화와 말림, 인쇄 부풀음, 박 눌림 자국, 열전사 가장자리 백화가 생깁니다. 원인은 품질 불량보다 라벨 내열 한계와 봉제 공장 프레스 조건의 불일치입니다. 소재별 온도 기준, 세 가지 대표 불량, 온도 단계 샘플과 프레스 조건 시트를 정리합니다.",
        sum_fr="Les accessoires passent le lavage puis échouent à la presse : bords durcis et enroulés, impression qui cloque, marques sur la dorure, bords de transfert blanchis. La cause est rarement la qualité : c'est un décalage entre limite thermique et réglages de presse. Repères par matière, trois défaillances, escalier thermique et fiche de déclaration.",
        sum_es="Los accesorios pasan el lavado y fallan en la prensa: bordes endurecidos y enrollados, impresión ampollada, marcas en el dorado, bordes transferidos blanqueados. La causa rara vez es la calidad: es un desajuste entre el límite térmico y los ajustes de prensa. Referencias por material, tres fallos y escalera térmica.",
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
