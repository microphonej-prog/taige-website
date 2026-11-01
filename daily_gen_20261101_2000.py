#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-11-01 20:00 批次每日更新生成脚本（六语：zh-Hant 根 / en / ja / ko / fr / es）
- 服装辅料打样费与样品政策（trim-sample-fee-refund-guide）
- 吊牌易撕线与双联吊牌设计（hang-tag-perforation-tear-off-guide）

用法: F:/hermes/venvs/tools/Scripts/python.exe daily_gen_20261101_2000.py [--check]
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
BUST_OLD, BUST_NEW = "191", "192"
LANGS = ["en", "ja", "ko", "fr", "es"]

ARTICLES = [
    dict(
        slug="trim-sample-fee-refund-guide.html",
        body="blog/_body_samplefee.html",
        title_zh="服装辅料打样费与样品政策：费用构成、可退条件与免费样规则 | TAGE",
        title_en="Trim Sampling Fees and Sample Policy: What Is Refundable | TAGE",
        title_ja="衣料副資材のサンプル代と返金ルール：費用内訳・無償サンプルの条件 | TAGE",
        title_ko="의류 부자재 샘플비와 반품 정책: 비용 구성과 무상 샘플 조건 | TAGE",
        title_fr="Frais d'échantillon et politique de retour : coûts, conditions, gratuité | TAGE",
        title_es="Coste de muestras y política de devolución: qué se cobra y qué se devuelve | TAGE",
        desc_zh="服装辅料打样费怎么算、能不能退：拆开刀模、材料、工时、运费四项，讲清大货折抵条件、免费样品真正适用的三种情形、样品与留样归属，以及报价单上必须写清的五句话。来自东莞泰阁包装。",
        desc_en="What a trim sampling fee actually covers, which parts are credited on the bulk order, when a sample is genuinely free, and the five lines a quote must state.",
        desc_ja="衣料副資材のサンプル代を型・材料・工数・送料に分解し、量産時の相殺条件、無償サンプルが成立する3つの場合、サンプルと保管見本の帰属、見積書に書くべき5項目を解説します。東莞泰閣包装。",
        desc_ko="의류 부자재 샘플비를 금형·재료·공수·운송비로 나누고, 양산 시 상계 조건, 무상 샘플이 성립하는 세 경우, 샘플과 보관 견본의 귀속, 견적서에 적어야 할 다섯 항목을 정리했습니다. 둥관 TAGE 패키징.",
        desc_fr="Frais d'échantillon : ce que couvrent forme, matière, main-d'œuvre et fret, ce qui est crédité en série, quand l'échantillon est vraiment gratuit et les cinq mentions du devis.",
        desc_es="Coste de muestra: qué cubren troquel, material, mano de obra y transporte, qué se abona en producción, cuándo es realmente gratuita y las cinco líneas del presupuesto.",
        crumb_zh="打样费与样品政策",
        crumb_en="Sampling Fees",
        crumb_ja="サンプル代と返金",
        crumb_ko="샘플비와 반품",
        crumb_fr="Frais d'échantillon",
        crumb_es="Coste de muestras",
        h1_zh="服装辅料打样费与样品政策：费用构成、可退条件与免费样规则",
        h1_en="Trim Sampling Fees and Sample Policy: What You Pay and What Comes Back",
        h1_ja="衣料副資材のサンプル代と返金ルール：費用の内訳と無償サンプルの条件",
        h1_ko="의류 부자재 샘플비와 반품 정책: 비용 구성과 무상 샘플 조건",
        h1_fr="Frais d'échantillon : ce que vous payez et ce qui revient en série",
        h1_es="Coste de muestras: qué se paga y qué se recupera en producción",
        tag_zh="采购实务", tag_en="Sourcing Practice", tag_ja="購買実務", tag_ko="구매 실무",
        tag_fr="Pratique d'achat", tag_es="Práctica de compra",
        sum_zh="打样费不是一笔糊涂账：刀模与版费属于可折抵的资产，材料、工时与运费属于已消耗的成本，混成一个总额后面必然扯皮。本文拆开四项构成，讲清大货折抵的门槛怎么写、免费样品真正成立的三种情形、样品与留样的归属，并给出报价单上必须写清的五句话。",
        sum_en="A sampling fee is not a single opaque number: dies and plates are reusable assets, while material, labour and freight are consumed cost, and lumping them together guarantees an argument. This guide splits the four components, sets out how to word the bulk credit threshold, the three cases where a sample is genuinely free, who owns the sample and the reference piece, and the five lines a quotation must state.",
        sum_ja="サンプル代は一括りの不明瞭な数字ではありません。型・版は相殺できる資産、材料・工数・送料は消費済みコストで、両者をまとめると必ず揉めます。本記事は 4 つの内訳を分け、量産時の相殺条件の書き方、無償サンプルが本当に成立する 3 つの場合、サンプルと保管見本の帰属、見積書に書くべき 5 項目を示します。",
        sum_ko="샘플비는 하나로 뭉뚱그릴 숫자가 아닙니다. 금형과 판은 상계 가능한 자산이고 재료·공수·운송비는 소모된 원가이므로, 둘을 합치면 반드시 분쟁이 생깁니다. 이 글은 네 가지 구성을 나누고, 양산 상계 조건 문구, 무상 샘플이 실제로 성립하는 세 경우, 샘플과 보관 견본의 귀속, 견적서에 적어야 할 다섯 항목을 제시합니다.",
        sum_fr="Des frais d'échantillon ne sont pas un chiffre opaque : la forme et le cliché sont des actifs réutilisables, matière, main-d'œuvre et fret sont des coûts consommés, et tout mélanger garantit la discussion. Le guide sépare les quatre postes, formule le seuil de crédit en série, expose les trois cas d'un échantillon vraiment gratuit, la propriété de l'échantillon et de la référence, et les cinq mentions du devis.",
        sum_es="El coste de muestra no es una cifra opaca: el troquel y la plancha son activos reutilizables, mientras material, mano de obra y transporte son coste consumido, y mezclarlos garantiza la discusión. La guía separa los cuatro conceptos, redacta el umbral de abono en producción, expone los tres casos de muestra realmente gratuita, la propiedad de la muestra y del patrón, y las cinco líneas del presupuesto.",
    ),
    dict(
        slug="hang-tag-perforation-tear-off-guide.html",
        body="blog/_body_perforation.html",
        title_zh="吊牌易撕线与双联吊牌设计指南：结构、撕裂力与刀模 | TAGE",
        title_en="Hang Tag Perforations and Two-Part Tags: Structure and Tear Force | TAGE",
        title_ja="下げ札のミシン目と2連タグ設計：構造・切り離し強度・型 | TAGE",
        title_ko="행택 절취선과 2연 행택 설계: 구조, 인열 강도, 금형 | TAGE",
        title_fr="Perforations et étiquettes à deux volets : structure et force | TAGE",
        title_es="Perforaciones y etiquetas de dos cuerpos: estructura y fuerza | TAGE",
        desc_zh="吊牌易撕线设计指南：打孔线、齿刀半切与微连点三种断口怎么选，撕裂手感怎么定，双联与三联吊牌的信息分工，纸张克重与覆膜对断口的影响，以及打样必须亲手验证的四件事。来自东莞泰阁包装。",
        desc_en="Hang tag perforations: round-hole, tooth-blade and micro-tie structures, setting tear force, two-part tag information split, and paper effects.",
        desc_ja="下げ札のミシン目設計ガイド。丸穴・歯刃ハーフカット・マイクロ連結の3構造、切り離し強度の決め方、2連・3連タグの情報分担、紙厚とラミネートの影響、サンプルで確かめる4項目を解説。東莞泰閣包装。",
        desc_ko="행택 절취선 설계 가이드. 원형 타공·톱니날 하프컷·미세 연결점 세 구조, 인열 강도 설정, 2연·3연 행택의 정보 분담, 종이 두께와 라미네이팅 영향, 샘플 확인 네 가지를 정리했습니다. 둥관 TAGE 패키징.",
        desc_fr="Perforations d'étiquettes : trois structures de rupture, réglage de la force, répartition de l'information sur deux volets, effet du papier et du pelliculage.",
        desc_es="Perforaciones de etiquetas: tres estructuras de rotura, cómo fijar la fuerza, reparto de información en dos cuerpos y efecto del papel y laminado.",
        crumb_zh="吊牌易撕线",
        crumb_en="Tear-off Perforations",
        crumb_ja="ミシン目と2連",
        crumb_ko="절취선과 2연",
        crumb_fr="Perforations",
        crumb_es="Perforaciones",
        h1_zh="吊牌易撕线与双联吊牌设计指南：结构、撕裂力与刀模",
        h1_en="Hang Tag Perforations and Two-Part Tags: Structure, Tear Force and Dies",
        h1_ja="下げ札のミシン目と2連タグ設計：構造・切り離し強度・型",
        h1_ko="행택 절취선과 2연 행택 설계: 구조, 인열 강도, 금형",
        h1_fr="Perforations et étiquettes à deux volets : structure, force et forme",
        h1_es="Perforaciones y etiquetas de dos cuerpos: estructura, fuerza y troquel",
        tag_zh="吊牌工艺", tag_en="Tag Engineering", tag_ja="タグ加工", tag_ko="행택 가공",
        tag_fr="Fabrication d'étiquettes", tag_es="Fabricación de etiquetas",
        sum_zh="易撕线的成败不在设计，而在孔距、刀模与纸厚的配合。本文比较打孔线、齿刀半切与微连点三种断口，给出可复现的撕裂手感标准，讲清双联与三联吊牌的信息分工、覆膜与再生纸对断口的影响，以及打样时必须亲手验证的四件事。",
        sum_en="A perforation succeeds or fails not on the design but on the fit between hole pitch, die and paper thickness. This guide compares round-hole, tooth-blade and micro-tie structures, gives a reproducible tear standard, explains how two- and three-part tags divide information, what lamination and recycled paper do to the edge, and the four checks to run by hand on a sample.",
        sum_ja="ミシン目の成否は意匠ではなく、穴ピッチ・型・紙厚の組み合わせで決まります。本記事は丸穴・歯刃ハーフカット・マイクロ連結の 3 構造を比較し、再現できる切り離し基準を示し、2 連・3 連タグの情報分担、ラミネートや再生紙が断口に与える影響、サンプルで手で確かめる 4 項目を解説します。",
        sum_ko="절취선의 성패는 디자인이 아니라 구멍 간격, 금형, 종이 두께의 조합에서 갈립니다. 이 글은 원형 타공·톱니날 하프컷·미세 연결점 세 구조를 비교하고, 재현 가능한 절취 기준을 제시하며, 2연·3연 행택의 정보 분담, 라미네이팅과 재생지가 절단면에 미치는 영향, 샘플에서 손으로 확인할 네 가지를 설명합니다.",
        sum_fr="La réussite d'une perforation ne tient pas au dessin mais à l'accord entre pas de perçage, forme et épaisseur de papier. Le guide compare trous ronds, lame dentée et micro-attaches, donne une norme de déchirure reproductible, explique le partage d'information sur deux ou trois volets, l'effet du pelliculage et du papier recyclé, et les quatre vérifications manuelles.",
        sum_es="El éxito de una perforación no depende del diseño sino del ajuste entre paso de agujeros, troquel y grosor del papel. La guía compara agujeros redondos, cuchilla dentada y micro-uniones, da un estándar de rasgado reproducible, explica el reparto de información en dos o tres cuerpos, el efecto del laminado y del papel reciclado, y las cuatro comprobaciones manuales.",
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
    print("  %-46s desc_zh=%d字 desc_en=%d字符 desc_ja=%d desc_ko=%d desc_fr=%d desc_es=%d"
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
