#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-09-23 上午 每日更新：2 篇新文章（六语：zh-Hant 根 / en / ja / ko / fr / es）
- 纸袋开窗工艺指南：窗口膜选择、结构与回收友好设计
- 服装辅料齐套配送（trim kitting）指南：按色码成套与配比发货
+ 列表页卡片 + gen_i18n 五语生成 + sitemap + BUST_VERSION 升级 + 简体转繁。

用法: python daily_gen_20260923_am.py
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
BUST_OLD, BUST_NEW = "101", "102"
LANGS = ["en", "ja", "ko", "fr", "es"]

ARTICLES = [
    dict(
        slug="paper-bag-window-guide.html",
        body="blog/_body_bagwindow.html",
        title_zh="纸袋开窗工艺指南：窗口膜选择、结构与回收友好设计 | TAGE",
        title_en="Paper Bag Window Guide: PET, PP or PLA Film and Structure | TAGE",
        title_ja="紙袋の窓加工ガイド：窓フィルムの選び方・構造・リサイクル設計 | TAGE",
        title_ko="종이백 창 가공 가이드: 창 필름 선택, 구조, 재활용 설계 | TAGE",
        title_fr="Guide de la fenêtre sur sac papier : film, structure et recyclabilité | TAGE",
        title_es="Guía de ventana en bolsas de papel: film, estructura y reciclabilidad | TAGE",
        desc_zh="纸袋开窗定制指南：对比 PET、PP、PLA、PVC 四种窗口膜的透明度、耐折性与回收表现，讲清窗口位置与提手承重的关系、圆角与内贴外贴的取舍、纸张克重匹配与回收合规要点，附打样验收五步与询价规格清单。来自东莞泰阁包装。",
        desc_en="Window paper bags: choosing PET, PP, PLA or PVC film, window position and handle load, paper grammage, recyclability, and a five-step sampling check.",
        desc_ja="窓付き紙袋のガイド。PET・PP・PLA・PVC の窓フィルム比較、窓位置と持ち手の荷重、角の丸みと内貼り・外貼り、坪量の選定、リサイクル適合、5ステップの検収を解説します。東莞泰閣包装。",
        desc_ko="창이 있는 종이백 가이드. PET·PP·PLA·PVC 창 필름 비교, 창 위치와 손잡이 하중, 모서리 라운딩과 내부·외부 패치, 평량 선택, 재활용 규정, 5단계 검수를 정리했습니다. 둥관 TAGE 패키징.",
        desc_fr="Sacs papier à fenêtre : choisir un film PET, PP, PLA ou PVC, position de fenêtre et charge de l'anse, grammage, recyclabilité et cinq contrôles d'échantillon.",
        desc_es="Bolsas de papel con ventana: elegir film PET, PP, PLA o PVC, posición de la ventana y carga del asa, gramaje, reciclabilidad y cinco controles.",
        crumb_zh="纸袋开窗工艺", crumb_en="Paper Bag Windows", crumb_ja="紙袋の窓加工",
        crumb_ko="종이백 창 가공", crumb_fr="Fenêtre sur sac papier", crumb_es="Ventana en bolsa de papel",
        h1_zh="纸袋开窗工艺指南：窗口膜选择、结构与回收友好设计",
        h1_en="Paper Bag Window Guide: Film Choice, Structure and Recyclability",
        h1_ja="紙袋の窓加工ガイド：窓フィルムの選び方・構造・リサイクル設計",
        h1_ko="종이백 창 가공 가이드: 창 필름 선택, 구조, 재활용 설계",
        h1_fr="Guide de la fenêtre sur sac papier : film, structure et recyclabilité",
        h1_es="Guía de la ventana en bolsas de papel: film, estructura y reciclabilidad",
        tag_zh="包装工艺", tag_en="Packaging", tag_ja="包装加工", tag_ko="포장 공정",
        tag_fr="Emballage", tag_es="Embalaje",
        sum_zh="开窗纸袋看起来只是挖个洞贴张膜，真正的决定项有四个：窗口膜材质、窗口位置与形状、纸张克重、以及回收合规。本文对比 PET、PP、PLA、PVC 四种窗口膜的透明度、耐折性与回收表现，讲清窗口与提手承重的关系、圆角与内贴外贴的取舍、牛皮纸切口起毛的风险，并给出打样验收五步与可直接抄进询价邮件的规格清单。",
        sum_en="A window bag looks like a hole with film glued over it, but four decisions carry it: film material, window position and shape, paper grammage and recyclability. This guide compares PET, PP, PLA and PVC on clarity, fold life and recycling, covers the load path between window and handle, rounded corners, inside versus outside patching and the fuzzing risk on kraft, then closes with a five-step sampling check and a specification list for your enquiry.",
        sum_ja="窓付き紙袋は「穴を開けてフィルムを貼るだけ」に見えますが、成否を分けるのは4つの要素です。窓フィルムの素材、窓の位置と形状、紙の坪量、リサイクル適合。本記事は PET・PP・PLA・PVC の透明感・耐折性・リサイクル性を比較し、窓と持ち手の荷重経路、角の丸み、内貼りと外貼りの選択、クラフト紙の切り口の毛羽立ちリスクを解説し、5ステップの検収と見積りに使える仕様リストを掲載します。",
        sum_ko="창이 있는 종이백은 구멍을 뚫고 필름을 붙이는 것처럼 보이지만 성패를 가르는 요소는 네 가지입니다. 창 필름 소재, 창의 위치와 형태, 종이 평량, 재활용 적합성입니다. 이 글은 PET·PP·PLA·PVC의 투명도, 내절성, 재활용성을 비교하고 창과 손잡이의 하중 경로, 모서리 라운딩, 내부·외부 패치 선택, 크라프트 절단면의 보풀 리스크를 다루며 5단계 검수와 견적용 사양 목록을 제시합니다.",
        sum_fr="Un sac à fenêtre ressemble à un trou recouvert d'un film, mais quatre décisions le déterminent : la matière du film, la position et la forme de la fenêtre, le grammage du papier et la recyclabilité. Ce guide compare PET, PP, PLA et PVC (clarté, tenue au pli, recyclage), traite le chemin de charge entre fenêtre et anse, les coins arrondis, le patch intérieur ou extérieur et le risque d'effilochage du kraft, puis propose cinq contrôles et une liste de spécifications.",
        sum_es="Una bolsa con ventana parece un agujero con un film pegado, pero cuatro decisiones la determinan: el material del film, la posición y forma de la ventana, el gramaje del papel y la reciclabilidad. Esta guía compara PET, PP, PLA y PVC en claridad, plegado y reciclaje, cubre el camino de carga entre ventana y asa, las esquinas redondeadas, el parche interior o exterior y el riesgo de deshilachado del kraft, y cierra con cinco comprobaciones y una lista de especificaciones.",
    ),
    dict(
        slug="trims-kitting-guide.html",
        body="blog/_body_kitting.html",
        title_zh="服装辅料齐套配送指南：按色码成套与配比发货 | TAGE",
        title_en="Trim Kitting Guide: Set Packing by Colour and Size | TAGE",
        title_ja="衣料副資材のキッティングガイド：色・サイズ別セット納入 | TAGE",
        title_ko="의류 부자재 키팅 가이드: 색상·사이즈별 세트 납품 | TAGE",
        title_fr="Guide du kitting d'accessoires : sets par couleur et taille | TAGE",
        title_es="Guía de kitting de accesorios: conjuntos por color y talla | TAGE",
        desc_zh="服装辅料齐套（trim kitting）指南：讲清按色码分包、成套与按件配比三种层级，齐套能省掉的分拣工时与错配返工，齐套率与缺件补数规则、配比表核对方法，附包装标识规范与报价口径，来自东莞泰阁包装。",
        desc_en="Trim kitting guide: sub-packing and sets by colour and size, the factory costs it removes, set completeness rates, shortage rules and how kitting is priced.",
        desc_ja="衣料副資材のキッティングガイド。色・サイズ別の分包とセット化、削減できる仕分け工数と誤組み手直し、セット充足率と欠品補充のルール、比率表の確認方法、包装表示と見積りの考え方を解説します。東莞泰閣包装。",
        desc_ko="의류 부자재 키팅 가이드. 색상·사이즈별 소분과 세트화, 절감되는 분류 공수와 오조립 재작업, 세트 충족률과 결품 보충 규칙, 비율표 확인 방법, 포장 표시와 견적 기준을 정리했습니다. 둥관 TAGE 패키징.",
        desc_fr="Guide du kitting d'accessoires : sous-emballage et sets par couleur et taille, coûts d'usine évités, taux de complétude, règles de manquants et chiffrage.",
        desc_es="Guía de kitting de accesorios: subempaque y conjuntos por color y talla, costes que evita, tasa de completitud, reglas de faltantes y precio.",
        crumb_zh="辅料齐套配送", crumb_en="Trim Kitting", crumb_ja="副資材キッティング",
        crumb_ko="부자재 키팅", crumb_fr="Kitting accessoires", crumb_es="Kitting de accesorios",
        h1_zh="服装辅料齐套配送指南：按色码成套与配比发货",
        h1_en="Trim Kitting Guide: Set Packing by Colour and Size",
        h1_ja="衣料副資材のキッティングガイド：色・サイズ別セット納入",
        h1_ko="의류 부자재 키팅 가이드: 색상·사이즈별 세트 납품",
        h1_fr="Guide du kitting d'accessoires : sets par couleur et taille",
        h1_es="Guía de kitting de accesorios: conjuntos por color y talla",
        tag_zh="供应流程", tag_en="Supply Chain", tag_ja="供給プロセス", tag_ko="공급 프로세스",
        tag_fr="Chaîne d'approvisionnement", tag_es="Cadena de suministro",
        sum_zh="齐套指的是把吊牌、织唛、洗水标、尺码标与包装按颜色尺码配齐成套发货，而不是按品类分箱。本文讲清分包、成套、按件配比三个层级，齐套能省掉的分拣工时与错配返工、齐套率与缺件补数规则、配比表必须与裁床单对齐的原因，并给出包装标识规范与报价口径。",
        sum_en="Kitting means shipping tags, woven labels, care labels, size labels and packaging bundled by colour and size instead of in cartons per trim type. This guide sets out the three levels — sub-packing, sets, piece-level ratios — the sorting hours and mismatch rework it removes, completeness rates and shortage rules, why the ratio table must match the cutting ticket, plus packing marks and how it is priced.",
        sum_ja="キッティングとは、タグ・織りラベル・洗濯表示ラベル・サイズラベル・包装を色とサイズごとに揃えてセット納入する方式で、品目ごとの箱納めとは異なります。本記事は分包・セット化・枚数比率の3段階、削減できる仕分け工数と誤組み手直し、セット充足率と欠品補充のルール、比率表を裁断伝票と一致させる理由、包装表示と見積りの考え方を解説します。",
        sum_ko="키팅은 행택, 직조 라벨, 세탁 표시 라벨, 사이즈 라벨, 포장을 색상과 사이즈별로 맞춰 세트로 납품하는 방식이며 품목별 상자 납품과 다릅니다. 이 글은 소분, 세트화, 벌 수 비율의 세 단계, 절감되는 분류 공수와 오조립 재작업, 세트 충족률과 결품 보충 규칙, 비율표를 재단 지시서와 일치시켜야 하는 이유, 포장 표시와 견적 기준을 설명합니다.",
        sum_fr="Le kitting consiste à livrer étiquettes, labels tissés, étiquettes d'entretien et de taille ainsi que l'emballage regroupés par couleur et par taille, et non en cartons par type. Ce guide décrit les trois niveaux — sous-emballage, sets, ratios à la pièce — les heures de tri et reprises évitées, les taux de complétude et règles de manquants, la nécessité d'aligner le tableau des ratios sur la fiche de coupe, le marquage carton et le chiffrage.",
        sum_es="El kitting consiste en entregar etiquetas, tejidas, de cuidado, de talla y embalaje agrupados por color y talla en lugar de en cajas por tipo. Esta guía describe los tres niveles —subempaque, conjuntos, ratios por pieza—, las horas de clasificación y reprocesos que evita, las tasas de completitud y reglas de faltantes, por qué la tabla de ratios debe coincidir con la ficha de corte, el marcado y el precio.",
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
    print("  %-28s desc_zh=%d字 desc_en=%d字符 desc_ja=%d desc_ko=%d desc_fr=%d desc_es=%d"
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
