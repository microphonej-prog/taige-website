#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-09-21 上午 每日更新：2 篇新文章（六语：zh-Hant 根 / en / ja / ko / fr / es）
+ 列表页卡片 + gen_i18n 五语生成 + sitemap + BUST_VERSION 升级 + 繁体转换。

用法: python daily_gen_20260921_am.py
"""
import os, re, sys, subprocess, importlib.util

ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)
PY = sys.executable

SKEL = "blog/knitwear-sweater-trims-guide.html"
DATE_ZH = "2026年9月21日"
DATE_EN = "September 21, 2026"
DATE_JA = "2026年9月21日更新"
DATE_KO = "2026년 9월 21일 업데이트"
DATE_FR = "21 septembre 2026"
DATE_ES = "21 de septiembre de 2026"
SITEMAP_DATE = "2026-09-21"
BUST_OLD, BUST_NEW = "95", "96"
LANGS = ["en", "ja", "ko", "fr", "es"]

ARTICLES = [
    dict(
        slug="hanger-bag-guide.html",
        body="blog/_body_hanger_bag.html",
        title_zh="服装挂装胶袋指南：挂衣袋、西装套袋与零售挂钩袋怎么选 | TAGE",
        title_en="Garment Hanger Bags Guide: Hanging Poly Bags &amp; Suit Covers | TAGE",
        title_ja="ハンガー袋ガイド：掛け袋・スーツカバーの選び方と寸法 | TAGE",
        title_ko="걸이 비닐봉투 가이드: 행거백, 수트 커버 선택과 치수 | TAGE",
        title_fr="Guide des housses à suspendre : sacs, tailles et fixations | TAGE",
        title_es="Guía de bolsas colgantes para ropa: tipos, medidas y gancho | TAGE",
        desc_zh="服装挂装胶袋指南：挂装袋与平装袋怎么取舍，开孔透明袋、自粘挂钩袋、拉链西装套袋与无纺布防尘袋四种袋型的适用场景，袋宽袋长如何从肩宽衣长反推，挂钩开孔与承重加固，材质厚度与防雾膜选择，印刷标识与出口要求，附打样验收清单。来自东莞泰阁包装。",
        desc_en="Hanger bag guide: hanging versus flat packing, four bag types, sizing from shoulder width and garment length, hook holes, load bearing, anti-fog film and export marks.",
        desc_ja="ハンガー袋のガイド。掛け包装と平積みの使い分け、4タイプの袋、肩幅と着丈からの寸法逆算、フック穴と耐荷重、素材と厚み、防曇フィルム、印刷・輸出表示、サンプル検収までを解説します。東莞泰閣包装。",
        desc_ko="걸이 비닐봉투 가이드: 걸이 포장과 평면 포장의 선택, 네 가지 봉투 형태, 어깨너비와 옷 길이에서 치수 역산, 고리 구멍과 하중, 소재와 두께, 김서림 방지 필름, 인쇄와 수출 표시까지 정리했습니다. 둥관 TAGE 패키징.",
        desc_fr="Guide des housses à suspendre : suspension ou emballage à plat, quatre types de sacs, dimensions calculées depuis le vêtement, trous et charge, film anti-buée et marquage export.",
        desc_es="Guía de bolsas colgantes: colgar o empaquetar en plano, cuatro tipos, medidas desde la prenda, orificios y carga, film antivaho y marcado de exportación.",
        crumb_zh="挂装胶袋指南", crumb_en="Hanger Bags", crumb_ja="ハンガー袋",
        crumb_ko="걸이 비닐봉투", crumb_fr="Housses à suspendre", crumb_es="Bolsas colgantes",
        h1_zh="服装挂装胶袋指南：挂衣袋、西装套袋与门店吊挂包装怎么选",
        h1_en="Garment Hanger Bags: Hanging Poly Bags, Suit Covers and Retail Packs",
        h1_ja="ハンガー袋の選び方：掛け袋・スーツカバー・店頭吊り下げ包装",
        h1_ko="걸이 비닐봉투 선택 가이드: 행거백, 수트 커버, 매장 걸이 포장",
        h1_fr="Housses à suspendre : choisir sacs, housses de costume et packs retail",
        h1_es="Bolsas colgantes para ropa: elegir bolsas, fundas de traje y packs de tienda",
        tag_zh="包装指南", tag_en="Packaging Guide", tag_ja="包装ガイド", tag_ko="포장 가이드",
        tag_fr="Guide emballage", tag_es="Guía de embalaje",
        sum_zh="挂装袋和普通平装袋最大的差别是承重：袋子要跟着衣服一起挂在挂杆上，还要在门店直接当展示包装。本文按挂装与平装的取舍、四种常见袋型、从肩宽衣长反推袋宽袋长、挂钩开孔形式与孔位加固、材质厚度与防雾膜、印刷与出口标识、打样验收七个部分展开，并给出一张可以直接抄进询价邮件的规格清单。",
        sum_en="The decisive difference between a hanger bag and an ordinary flat bag is load: the bag hangs on a rail with the garment inside and doubles as the shop-floor display pack. This guide covers when hanging beats flat packing, four bag types, working bag width and length back from shoulder width and garment length, hole styles and reinforcement, material, thickness and anti-fog film, printing and export marking, and a sampling checklist.",
        sum_ja="ハンガー袋と普通の平袋の決定的な違いは耐荷重です。袋は商品ごとレールに掛かり、店頭ではそのまま展示包装になります。本記事では、掛け包装と平積みの使い分け、4タイプの袋、肩幅と着丈からの袋幅・袋丈の逆算、フック穴の形式と補強、素材・厚み・防曇フィルム、印刷と輸出表示、サンプル検収までを整理し、そのまま見積り依頼に使える仕様リストを添えます。",
        sum_ko="걸이 봉투와 일반 평면 봉투의 결정적 차이는 하중입니다. 봉투는 옷과 함께 레일에 걸리고 매장에서는 그대로 진열 포장이 됩니다. 이 글은 걸이 포장과 평면 포장의 선택, 네 가지 봉투 형태, 어깨너비와 옷 길이에서 봉투 폭과 길이를 역산하는 방법, 구멍 형태와 보강, 소재·두께·김서림 방지 필름, 인쇄와 수출 표시, 샘플 검수까지 정리하고 견적 요청에 바로 쓸 수 있는 사양 목록을 제시합니다.",
        sum_fr="La différence décisive entre une housse et un sachet à plat, c'est la charge : la housse pend sur un rail avec le vêtement et sert de support en boutique. Ce guide couvre suspension ou emballage à plat, quatre types de sacs, le calcul des dimensions à partir du vêtement, les trous et renforts, matière, épaisseur et film anti-buée, impression et marquage export, et la liste de contrôle d'échantillon.",
        sum_es="La diferencia decisiva entre una bolsa colgante y una bolsa plana es la carga: cuelga del riel con la prenda dentro y sirve de expositor en tienda. Esta guía cubre colgar o empaquetar en plano, cuatro tipos de bolsa, el cálculo de medidas desde la prenda, orificios y refuerzos, material, grosor y film antivaho, impresión y marcado de exportación, y la lista de comprobación de muestras.",
    ),
    dict(
        slug="shrink-film-packaging-guide.html",
        body="blog/_body_shrink_film.html",
        title_zh="服装热收缩膜包装指南：PE/POF/交联膜怎么选与收缩率控制 | TAGE",
        title_en="Shrink Film Packaging for Apparel: PE, POF &amp; Cross-Linked | TAGE",
        title_ja="衣料品のシュリンク包装ガイド：PE・POF・架橋フィルムの選び方 | TAGE",
        title_ko="의류 수축 필름 포장 가이드: PE·POF·가교 필름 선택 | TAGE",
        title_fr="Film rétractable pour vêtements : PE, POF et réticulé | TAGE",
        title_es="Film retráctil para ropa: PE, POF y reticulado | TAGE",
        desc_zh="服装热收缩膜包装指南：PE、POF 与交联 PE 三种膜在透明度、收缩温度与成本上的差异，收缩率与方向如何造成变形，15μm 到 25μm 厚度的实际差别，封口与排气打孔的设备参数，收缩膜与胶袋的成本口径与拆包体验对比，印刷标识与打样验收清单。来自东莞泰阁包装。",
        desc_en="Shrink film guide for apparel: PE, POF and cross-linked PE compared, how shrinkage rate and direction distort a pack, thickness from 15 to 25μm, sealing and venting, and shrink film versus bags.",
        desc_ja="衣料品のシュリンク包装ガイド。PE・POF・架橋PEの透明性と収縮温度・コストの違い、収縮率と方向による歪み、15〜25μmの厚みの差、シールとベント穴の設定、ポリ袋との比較、印刷・表示、サンプル検収を解説します。東莞泰閣包装。",
        desc_ko="의류 수축 필름 포장 가이드: PE, POF, 가교 PE의 투명도와 수축 온도, 비용 차이, 수축률과 방향에 따른 변형, 15~25μm 두께의 실제 차이, 실링과 에어 벤트 설정, 비닐봉투와의 비교, 인쇄와 표시까지 정리했습니다. 둥관 TAGE 패키징.",
        desc_fr="Guide du film rétractable : comparaison PE, POF et PE réticulé, effet du taux et du sens de retrait, épaisseurs de 15 à 25 μm, soudure et évents, film ou sachet, et liste de contrôle.",
        desc_es="Guía del film retráctil: comparación de PE, POF y PE reticulado, efecto de la tasa y dirección de retracción, grosores de 15 a 25 μm, sellado y venteo, film o bolsa y lista de comprobación.",
        crumb_zh="热收缩膜包装", crumb_en="Shrink Film", crumb_ja="シュリンク包装",
        crumb_ko="수축 필름 포장", crumb_fr="Film rétractable", crumb_es="Film retráctil",
        h1_zh="服装热收缩膜包装指南：PE、POF 与交联膜怎么选，收缩率怎么控",
        h1_en="Shrink Film Packaging for Apparel: PE, POF and Cross-Linked Options",
        h1_ja="衣料品のシュリンク包装ガイド：フィルム選びと収縮率の管理",
        h1_ko="의류 수축 필름 포장 가이드: 필름 선택과 수축률 관리",
        h1_fr="Film rétractable pour vêtements : choisir le film et maîtriser le retrait",
        h1_es="Film retráctil para ropa: elegir el film y controlar la retracción",
        tag_zh="包装指南", tag_en="Packaging Guide", tag_ja="包装ガイド", tag_ko="포장 가이드",
        tag_fr="Guide emballage", tag_es="Guía de embalaje",
        sum_zh="收缩膜包装把折叠好的衣服包成一层紧致、开封即留痕的透明外衣，适合 T 恤、内衣、袜子与组合装；但膜料或通道温度选错，毛感面料会被压出硬折痕。本文对比 PE、POF 与交联 PE 的透明度、收缩温度与成本，讲清收缩率与方向造成的变形、15μm 到 25μm 厚度的实际差别、封口与排气打孔的参数，以及什么时候该改用胶袋，附打样验收清单。",
        sum_en="Shrink film seals a folded garment into a tight, transparent pack that shows if it has been opened — ideal for T-shirts, underwear, socks and multi-packs. Choose the wrong film or tunnel temperature, though, and napped fabrics come out with hard creases. This guide compares PE, POF and cross-linked PE on clarity, shrink temperature and cost, explains distortion caused by shrinkage rate and direction, the real difference between 15μm and 25μm, sealing and venting settings, when a poly bag wins instead, and a sampling checklist.",
        sum_ja="シュリンク包装は、折りたたんだ衣料品をタイトで透明、開封跡が残る外装に仕上げます。Tシャツ・インナー・靴下・セット商品に適しますが、フィルムやトンネル温度を誤ると毛羽立った生地に硬い折りジワが残ります。本記事ではPE・POF・架橋PEの透明性・収縮温度・コストを比較し、収縮率と方向による歪み、15〜25μmの厚みの実際の差、シールとベント穴の設定、ポリ袋へ切り替える判断、サンプル検収までを整理します。",
        sum_ko="수축 필름 포장은 접힌 옷을 타이트하고 투명하며 개봉 흔적이 남는 외포장으로 마무리합니다. 티셔츠, 속옷, 양말, 세트 상품에 적합하지만 필름이나 터널 온도를 잘못 고르면 기모 소재에 딱딱한 접힘 자국이 남습니다. 이 글은 PE, POF, 가교 PE의 투명도, 수축 온도, 비용을 비교하고 수축률과 방향에 따른 변형, 15~25μm 두께의 실제 차이, 실링과 에어 벤트 설정, 비닐봉투로 바꿔야 하는 기준, 샘플 검수까지 정리합니다.",
        sum_fr="Le film rétractable scelle un vêtement plié dans un emballage serré, transparent et inviolable — idéal pour t-shirts, sous-vêtements, chaussettes et lots. Un film ou une température de tunnel mal choisis laissent toutefois des plis marqués sur les matières grattées. Ce guide compare PE, POF et PE réticulé (transparence, température, coût), explique les déformations liées au taux et au sens de retrait, la différence réelle entre 15 et 25 μm, les réglages de soudure et d'évents, le choix du sachet et la liste de contrôle.",
        sum_es="El film retráctil sella la prenda plegada en un envase ceñido, transparente y con evidencia de apertura: ideal para camisetas, ropa interior, calcetines y conjuntos. Pero un film o una temperatura equivocados dejan pliegues duros en tejidos con pelo. Esta guía compara PE, POF y PE reticulado en transparencia, temperatura y coste, explica las deformaciones por tasa y dirección de retracción, la diferencia real entre 15 y 25 μm, los ajustes de sellado y venteo, cuándo conviene una bolsa y la lista de comprobación.",
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
