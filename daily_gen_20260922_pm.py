#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-09-22 下午 每日更新：2 篇新文章（六语：zh-Hant 根 / en / ja / ko / fr / es）
- 服装辅料跟单指南：生产进度跟踪与延期预警
- 吊牌油墨安全指南：迁移、气味与 EN 71-3 合规
+ 列表页卡片 + gen_i18n 五语生成 + sitemap + BUST_VERSION 升级 + 简体转繁。

用法: python daily_gen_20260922_pm.py
"""
import os, re, sys, subprocess, importlib.util

ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)
PY = sys.executable

SKEL = "blog/knitwear-sweater-trims-guide.html"
DATE_ZH = "2026年9月22日"
DATE_EN = "September 22, 2026"
DATE_JA = "2026年9月22日更新"
DATE_KO = "2026년 9월 22일 업데이트"
DATE_FR = "22 septembre 2026"
DATE_ES = "22 de septiembre de 2026"
SITEMAP_DATE = "2026-09-22"
BUST_OLD, BUST_NEW = "99", "100"
LANGS = ["en", "ja", "ko", "fr", "es"]

ARTICLES = [
    dict(
        slug="garment-trims-order-tracking-guide.html",
        body="blog/_body_ordertrack.html",
        title_zh="服装辅料跟单指南：生产进度跟踪与延期预警 | TAGE",
        title_en="Apparel Trims Order Tracking: Milestones, Reports &amp; Delay Alerts | TAGE",
        title_ja="衣料副資材の受発注管理ガイド：進捗の節目と遅延アラート | TAGE",
        title_ko="의류 부자재 수주 관리 가이드: 진행 단계와 지연 경보 | TAGE",
        title_fr="Suivi de commande d'accessoires : jalons, reports et alertes de retard | TAGE",
        title_es="Seguimiento de pedidos de accesorios: hitos, reportes y alertas de retraso | TAGE",
        desc_zh="服装辅料跟单指南：把下单到交货拆成订单确认、材料到位、首件确认与出货检验四个可见节点，附进度表字段、每周汇报节奏、三级延期预警与出货前48小时清单，可直接写进订单确认单。来自东莞泰阁包装。",
        desc_en="Apparel trims order tracking: four visible milestones, tracking-sheet fields, weekly reports, a three-level delay alert and the 48-hour pre-shipment checklist.",
        desc_ja="衣料副資材の受発注管理ガイド。注文確認・材料入荷・初品承認・出荷検査という4つの節目、進捗表の項目、週2回の報告リズム、3段階の遅延アラート、出荷48時間前チェックリストを解説します。東莞泰閣包装。",
        desc_ko="의류 부자재 수주 관리 가이드: 주문 확인·자재 입고·초품 승인·출하 검사의 네 단계, 진행표 항목, 주 2회 보고 주기, 3단계 지연 경보, 출하 48시간 전 체크리스트를 정리했습니다. 둥관 TAGE 패키징.",
        desc_fr="Suivi de commande d'accessoires : quatre jalons visibles, champs du tableau de suivi, cadence de reporting, alerte de retard à trois niveaux et liste des 48 heures avant expédition.",
        desc_es="Seguimiento de pedidos de accesorios: cuatro hitos visibles, campos de la hoja de seguimiento, ritmo de reporte, alerta de retraso en tres niveles y lista de 48 horas.",
        crumb_zh="辅料跟单", crumb_en="Trims Order Tracking", crumb_ja="受発注管理",
        crumb_ko="수주 관리", crumb_fr="Suivi de commande", crumb_es="Seguimiento de pedidos",
        h1_zh="服装辅料跟单指南：生产进度跟踪与延期预警",
        h1_en="Apparel Trims Order Tracking: Milestones, Reports and Delay Alerts",
        h1_ja="衣料副資材の受発注管理ガイド：進捗の節目と遅延アラート",
        h1_ko="의류 부자재 수주 관리 가이드: 진행 단계와 지연 경보",
        h1_fr="Suivi de commande d'accessoires : jalons, reports et alertes de retard",
        h1_es="Seguimiento de pedidos de accesorios: hitos, reportes y alertas de retraso",
        tag_zh="采购实务", tag_en="Sourcing", tag_ja="調達実務", tag_ko="소싱 실무",
        tag_fr="Achats", tag_es="Compras",
        sum_zh="辅料单笔金额不大，可一旦延期，成衣出货、门店上挂与电商备货会一起推后。本文把下单到交货拆成订单确认、材料到位、首件确认、出货检验四个可见节点，给出进度表该有的字段、每周固定汇报节奏、三级延期预警（黄/橙/红）与对应动作，以及出货前48小时清单，模板可直接写进订单确认单。",
        sum_en="Trim orders are small in value but a delay pushes back garment shipping, store hanging and e-commerce restocking at once. This guide splits order-to-delivery into four visible milestones, lists the fields a tracking sheet needs, sets a fixed weekly reporting rhythm, defines a three-level delay alert with actions, and ends with a 48-hour pre-shipment checklist.",
        sum_ja="副資材は金額が小さくても、遅れれば衣料の出荷、店頭への掛け込み、EC の在庫補充が同時に後ろへずれます。本記事は発注から納品までを4つの節目に分け、進捗表の項目、週2回の定時報告、3段階の遅延アラートと対応、出荷48時間前チェックリストを示します。",
        sum_ko="부자재는 금액이 작아도 지연되면 의류 출하와 매장 진열, 이커머스 재고 보충이 함께 밀립니다. 이 글은 발주부터 납품까지를 네 단계로 나누고 진행표 항목, 주 2회 정기 보고, 3단계 지연 경보와 대응, 출하 48시간 전 체크리스트를 제시합니다.",
        sum_fr="Les commandes d'accessoires sont modestes, mais un retard décale à la fois les expéditions, la mise en rayon et le réassort. Ce guide découpe la commande en quatre jalons, détaille le tableau de suivi, la cadence de reporting, une alerte de retard à trois niveaux et la liste des 48 heures.",
        sum_es="Los pedidos de accesorios son pequeños, pero un retraso desplaza a la vez envíos, colocación en tienda y reabastecimiento. Esta guía divide el pedido en cuatro hitos y detalla la hoja de seguimiento, el ritmo de reporte, la alerta de retraso en tres niveles y la lista de 48 horas.",
    ),
    dict(
        slug="hang-tag-ink-safety-guide.html",
        body="blog/_body_inksafety.html",
        title_zh="吊牌油墨安全指南：迁移、气味与 EN 71-3 合规 | TAGE",
        title_en="Hang Tag Ink Safety: Migration, Odour &amp; EN 71-3 Compliance | TAGE",
        title_ja="タグのインキ安全ガイド：移行・においと EN 71-3 対応 | TAGE",
        title_ko="행택 잉크 안전 가이드: 이행, 냄새, EN 71-3 대응 | TAGE",
        title_fr="Sécurité des encres d'étiquettes : migration, odeur et EN 71-3 | TAGE",
        title_es="Seguridad de la tinta en etiquetas: migración, olor y EN 71-3 | TAGE",
        desc_zh="吊牌油墨安全指南：对比植物基、UV、水性、溶剂型四类油墨，讲清油墨向成衣迁移的四条路径，REACH 附录 XVII、EN 71-3、CPSIA 与 Prop 65 的关注点，以及低迁移油墨搭配与打样送检清单。来自东莞泰阁包装。",
        desc_en="Hang tag ink safety: offset, UV, water-based or solvent inks compared, four migration routes to garments, REACH Annex XVII, EN 71-3 and low-migration setups.",
        desc_ja="タグのインキ安全ガイド。植物性・UV・水性・溶剤の4系統の比較、衣料への移行4経路、REACH 附属書 XVII・EN 71-3・CPSIA・Prop 65 の着眼点、低移行インキの組み方、サンプル試験のチェックリストを解説。東莞泰閣包装。",
        desc_ko="행택 잉크 안전 가이드: 식물성·UV·수성·용제 잉크 비교, 의류로의 이행 네 경로, REACH 부속서 XVII·EN 71-3·CPSIA·Prop 65 쟁점, 저이행 잉크 구성과 샘플 시험 체크리스트를 정리했습니다. 둥관 TAGE 패키징.",
        desc_fr="Sécurité des encres d'étiquettes : offset, UV, aqueuse ou solvant, quatre voies de migration, REACH annexe XVII et EN 71-3, et une configuration à faible migration.",
        desc_es="Seguridad de la tinta de etiquetas: offset, UV, al agua o disolvente, cuatro vías de migración, REACH anexo XVII y EN 71-3, y una configuración de baja migración.",
        crumb_zh="吊牌油墨安全", crumb_en="Hang Tag Ink Safety", crumb_ja="タグのインキ安全",
        crumb_ko="행택 잉크 안전", crumb_fr="Sécurité des encres", crumb_es="Seguridad de la tinta",
        h1_zh="吊牌油墨安全指南：迁移、气味与 EN 71-3 合规",
        h1_en="Hang Tag Ink Safety: Migration, Odour and EN 71-3 Compliance",
        h1_ja="タグのインキ安全ガイド：移行・においと EN 71-3 対応",
        h1_ko="행택 잉크 안전 가이드: 이행, 냄새, EN 71-3 대응",
        h1_fr="Sécurité des encres d'étiquettes : migration, odeur et EN 71-3",
        h1_es="Seguridad de la tinta en etiquetas: migración, olor y EN 71-3",
        tag_zh="合规指南", tag_en="Compliance", tag_ja="コンプライアンス", tag_ko="컴플라이언스",
        tag_fr="Conformité", tag_es="Cumplimiento",
        sum_zh="客户审吊牌时常常只看纸张与工艺，很少追问油墨体系，而颜料中的重金属、偶氮着色剂、增塑剂与残留溶剂正是抽查最容易踩的短板。本文对比四类油墨的取舍，拆解油墨向成衣迁移的四条路径，梳理 REACH 附录 XVII、EN 71-3、CPSIA、Prop 65 与客户 RSL 的关注点，给出低迁移方案与打样前的六项信息清单。",
        sum_en="Buyers audit the paper and finishing of a hang tag, rarely the ink system — yet pigments, azo colorants, plasticisers and residual solvents are where compliance audits bite. This guide compares four ink systems, breaks down the four migration routes onto garments, maps REACH Annex XVII, EN 71-3, CPSIA, Prop 65 and buyer RSLs, and sets out low-migration options and a six-point pre-sampling brief.",
        sum_ja="バイヤーはタグの紙と加工を見ても、インキ系統まではあまり確認しません。しかし顔料の重金属、アゾ着色剤、可塑剤、残留溶剤こそ検査で最も弱い部分です。本記事は4系統のインキの比較、衣料への移行4経路、REACH 附属書 XVII・EN 71-3・CPSIA・Prop 65・顧客 RSL の着眼点、低移行の組み方とサンプル前の6項目を整理します。",
        sum_ko="바이어는 행택의 종이와 후가공은 점검하지만 잉크 계통은 거의 묻지 않습니다. 그러나 안료 중금속, 아조 착색제, 가소제, 잔류 용제가 바로 점검의 취약점입니다. 이 글은 네 가지 잉크 비교, 의류로의 이행 네 경로, REACH 부속서 XVII·EN 71-3·CPSIA·Prop 65·RSL 쟁점, 저이행 방안과 샘플 전 여섯 항목을 정리합니다.",
        sum_fr="L'acheteur contrôle le papier et les finitions, rarement l'encre : pigments, colorants azoïques, plastifiants et solvants résiduels sont pourtant le point faible des audits. Ce guide compare quatre systèmes d'encre, décrit quatre voies de migration, cartographie REACH annexe XVII, EN 71-3, CPSIA, Prop 65 et les RSL clients.",
        sum_es="El comprador audita el papel y los acabados, rara vez la tinta: pigmentos, colorantes azoicos, plastificantes y disolventes residuales son el punto débil de las auditorías. Esta guía compara cuatro sistemas de tinta, describe cuatro vías de migración, mapea REACH anexo XVII, EN 71-3, CPSIA, Prop 65 y los RSL del cliente.",
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
    print("写入 %s (%d KB) desc_zh=%d字 desc_en=%d字符 desc_ja=%d desc_ko=%d desc_fr=%d desc_es=%d"
          % (out, len(s.encode("utf-8")) // 1024, len(a["desc_zh"]), len(a["desc_en"]),
             len(a["desc_ja"]), len(a["desc_ko"]), len(a["desc_fr"]), len(a["desc_es"])))

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
