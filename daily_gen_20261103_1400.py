#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-11-03 14:00 批次（六语：zh-Hant 根 / en / ja / ko / fr / es）
- 刮刮卡吊牌：促销抽奖与验真编码（hang-tag-scratch-off-guide）
- 织唛特种纱线：金银丝、反光、蓄光与感温（woven-label-special-yarn-guide）

用法: F:/hermes/venvs/tools/Scripts/python.exe daily_gen_20261103_1400.py [--check]
"""
import os, re, sys, subprocess, importlib.util

ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)
PY = sys.executable

SKEL = "blog/knitwear-sweater-trims-guide.html"
DATE_ZH = "2026年11月3日"
DATE_EN = "November 3, 2026"
DATE_JA = "2026年11月3日"
DATE_KO = "2026년 11월 3일 업데이트"
DATE_FR = "3 novembre 2026"
DATE_ES = "3 de noviembre de 2026"
SITEMAP_DATE = "2026-11-03"
BUST_OLD, BUST_NEW = "195", "196"
LANGS = ["en", "ja", "ko", "fr", "es"]

ARTICLES = [
    dict(
        slug="hang-tag-scratch-off-guide.html",
        body="blog/_body_scratch.html",
        title_zh="刮刮卡吊牌：促销抽奖与验真编码的工艺与合规 | TAGE",
        title_en="Scratch-Off Hang Tags: Promotions, Codes and Compliance | TAGE",
        title_ja="スクラッチ付きタグ：販促抽選と認証コードの加工と法令対応 | TAGE",
        title_ko="스크래치 행택: 판촉 추첨과 인증 코드의 공정과 규정 | TAGE",
        title_fr="Étiquettes à gratter : jeu promotionnel, codes et conformité | TAGE",
        title_es="Etiquetas rascables: sorteo promocional, códigos y normativa | TAGE",
        desc_zh="刮刮卡吊牌怎么做：五层结构（面纸、隔离底油、可变数据、刮刮墨、保护层）、刮开区最小尺寸与位置、覆膜必须镂空、促销规则必须印在吊牌上的合规要点，以及刮不开、刮穿、重号、仓储粘连等五个翻车点。来自东莞泰阁包装。",
        desc_en="Scratch-off hang tags explained: layer build, minimum panel size, lamination knock-out, mandatory promotion wording, five common failures and quote details.",
        desc_ja="スクラッチ付きタグの作り方：表紙・下地ニス・可変データ・スクラッチインキ・保護層の5層、削り部の最小寸法と位置、ラミネートの抜き、販促表示の法令要件、削れない・突き抜ける・重複コード・保管時の癒着という5つの失敗を解説。東莞泰閣包装。",
        desc_ko="스크래치 행택 제작: 표면지·배리어 프라이머·가변 데이터·스크래치 잉크·보호층 5층 구조, 긁는 부분 최소 크기와 위치, 라미네이팅 녹아웃, 판촉 표기 규정, 긁히지 않음·뚫림·중복 코드·적재 점착 등 다섯 가지 실패를 정리했습니다. 둥관 TAGE 패키징.",
        desc_fr="Étiquettes à gratter : cinq couches, dimensions minimales de la pastille, réserve de pelliculage, mentions promotionnelles obligatoires et cinq échecs.",
        desc_es="Etiquetas rascables: cinco capas, tamaño mínimo de la pastilla, reserva en el laminado, menciones promocionales obligatorias y cinco fallos.",
        crumb_zh="刮刮卡吊牌",
        crumb_en="Scratch-Off Hang Tags",
        crumb_ja="スクラッチ付きタグ",
        crumb_ko="스크래치 행택",
        crumb_fr="Étiquettes à gratter",
        crumb_es="Etiquetas rascables",
        h1_zh="刮刮卡吊牌：促销抽奖与验真编码的工艺与合规",
        h1_en="Scratch-Off Hang Tags: Promotions, Verification Codes and Compliance",
        h1_ja="スクラッチ付きタグ：販促抽選と認証コードの加工と法令対応",
        h1_ko="스크래치 행택: 판촉 추첨과 인증 코드의 공정과 규정",
        h1_fr="Étiquettes à gratter : jeu promotionnel, codes et conformité",
        h1_es="Etiquetas rascables: sorteo promocional, códigos y normativa",
        tag_zh="工艺细节", tag_en="Production Detail", tag_ja="工程詳細", tag_ko="공정 디테일",
        tag_fr="Détail technique", tag_es="Detalle técnico",
        sum_zh="刮开吊牌上的一块涂层，顾客看到的是奖品或一组验真编码——品牌看到的是结构、工艺与合规三道关卡。这篇讲五层结构与丝印顺序、刮开区的最小尺寸和位置、覆膜必须镂空、促销规则哪些话必须印上去，以及刮不开、刮穿、码被盖住、重号、仓储粘连五个真实翻车点，附询价六项。",
        sum_en="Under the scratch panel the customer finds a prize or a verification code; the brand finds three gates — structure, process and compliance. Five layers and their screen-printing order, minimum panel size and placement, why lamination must be knocked out, the promotion wording that has to be printed, and five failures we see: it will not scratch, it scratches through, the code is buried, codes duplicate, stacks stick. Plus six details for a quotation.",
        sum_ja="削った下に当たりくじ、あるいは認証コード。ブランド側には構造・加工・法令という三つの関門があります。5層構造とスクリーン印刷の順序、削り部の最小寸法と位置、ラミネートの抜きが必要な理由、必ず記載する販促表示、そして削れない・突き抜ける・コードが覆われる・重複・積み重ねの癒着という実際の失敗5つと、見積の6項目をまとめました。",
        sum_ko="긁은 아래에서 고객은 경품이나 인증 코드를 보고, 브랜드는 구조·공정·규정이라는 세 관문을 봅니다. 다섯 층 구조와 스크린 인쇄 순서, 긁는 부분의 최소 크기와 위치, 라미네이팅 녹아웃이 필요한 이유, 반드시 인쇄해야 하는 판촉 표기, 그리고 긁히지 않음·뚫림·코드 가림·중복·적재 점착이라는 실제 실패 다섯 가지와 견적 여섯 항목을 정리했습니다.",
        sum_fr="Sous la pastille, le client trouve un lot ou un code d'authentification ; la marque, elle, voit trois verrous : structure, process et conformité. Cinq couches et l'ordre de sérigraphie, dimensions et placement minimaux, pourquoi le pelliculage doit être en réserve, les mentions promotionnelles obligatoires, et cinq échecs réels : ne se gratte pas, se perce, code noyé, codes en double, piles qui collent. Plus six points pour le devis.",
        sum_es="Bajo la pastilla el cliente encuentra un premio o un código de verificación; la marca encuentra tres cerrojos: estructura, proceso y cumplimiento. Cinco capas y su orden de serigrafía, tamaño y colocación mínimos, por qué el laminado debe ir en reserva, las menciones promocionales obligatorias y cinco fallos reales: no rasca, se perfora, código enterrado, códigos duplicados, pilas que se pegan. Más seis datos para el presupuesto.",
    ),
    dict(
        slug="woven-label-special-yarn-guide.html",
        body="blog/_body_yarn.html",
        title_zh="织唛特种纱线：金银丝、反光、蓄光与感温纱怎么用 | TAGE",
        title_en="Special Yarns in Woven Labels: Metallic, Reflective, Glow | TAGE",
        title_ja="織りラベルの特殊糸：金属・反射・蓄光・感温の使い方 | TAGE",
        title_ko="직조 라벨 특수 사: 금은사·반사·축광·감온 활용법 | TAGE",
        title_fr="Fils spéciaux en labels tissés : métallique, réfléchissant, phosphorescent | TAGE",
        title_es="Hilos especiales en etiquetas tejidas: metálico, reflectante, fosforescente | TAGE",
        desc_zh="织唛特种纱线怎么选：金银丝、反光纱、蓄光纱、荧光纱与感温纱的效果与物理限制，最细线宽 0.6–0.8 毫米、不可渐变、最小字号，洗水整烫后的真实寿命，EN ISO 20471 宣称边界与检针机报警，附五种场景组合与询价六项。",
        desc_en="Special yarns in woven labels: metallic, reflective, glow and thermochromic. Line width limits, wash life, EN ISO 20471 claims and needle detector issues.",
        desc_ja="織りラベルの特殊糸：金属糸・反射糸・蓄光糸・蛍光糸・感温糸の効果と物理的限界、最細線幅0.6〜0.8mm、階調不可、最小字号、洗濯とプレス後の実際の寿命、EN ISO 20471の表示範囲と検針機の反応、用途別5例と見積6項目。東莞泰閣包装。",
        desc_ko="직조 라벨 특수 사: 금은사·반사사·축광사·형광사·감온사의 효과와 물리적 한계, 최세 선 0.6~0.8mm, 계조 불가, 최소 글자 크기, 세탁·다림질 후 실제 수명, EN ISO 20471 표시 범위와 침검기 반응, 용도별 다섯 조합과 견적 여섯 항목. 둥관 TAGE 패키징.",
        desc_fr="Fils spéciaux en labels tissés : métallique, réfléchissant, phosphorescent et thermochrome. Limites de trait, tenue au lavage, EN ISO 20471 et détection d'aiguilles.",
        desc_es="Hilos especiales en etiquetas tejidas: metálico, reflectante, fosforescente y termocromo. Límites de trazo, lavado, EN ISO 20471 y detección de agujas.",
        crumb_zh="织唛特种纱线",
        crumb_en="Special Yarns in Woven Labels",
        crumb_ja="織りラベルの特殊糸",
        crumb_ko="직조 라벨 특수 사",
        crumb_fr="Fils spéciaux tissés",
        crumb_es="Hilos especiales tejidos",
        h1_zh="织唛特种纱线：金银丝、反光、蓄光与感温纱怎么用",
        h1_en="Special Yarns in Woven Labels: Metallic, Reflective, Glow and Thermochromic",
        h1_ja="織りラベルの特殊糸：金属・反射・蓄光・感温の使い方",
        h1_ko="직조 라벨 특수 사: 금은사·반사·축광·감온 활용법",
        h1_fr="Fils spéciaux en labels tissés : métallique, réfléchissant, phosphorescent et thermochrome",
        h1_es="Hilos especiales en etiquetas tejidas: metálico, reflectante, fosforescente y termocromo",
        tag_zh="材质选型", tag_en="Material Choice", tag_ja="素材選定", tag_ko="소재 선택",
        tag_fr="Choix de matière", tag_es="Selección de material",
        sum_zh="金银丝能让主唛在货架上被一眼认出，反光纱能让夜跑外套在车灯下亮起来——但换个纱不等于能上机。这篇讲五类特种纱的视觉效果与物理边界，最细线宽 0.6–0.8 毫米、织唛做不了渐变、最小字号 6 磅，四十次工业水洗后的真实衰减，EN ISO 20471 的宣称红线与检针机报警，附五种场景组合与询价六项。",
        sum_en="Metallic yarn makes a neck label readable across the shop floor; reflective yarn makes a night-running jacket catch the headlights. But a special yarn is not a drop-in swap. Five families and their physical limits, the 0.6–0.8 mm minimum line, why woven labels cannot hold a gradient, 6 pt minimum type, real decay after forty industrial washes, the EN ISO 20471 claim line and needle detection. Plus five end-use combinations and six quote details.",
        sum_ja="金属糸はメインラベルを売場で一瞬で伝え、反射糸はナイトラン用の上着をヘッドライトに浮かび上がらせます。ただし糸を替えるだけでは織れません。5系統の糸の効果と物理的限界、最細線幅0.6〜0.8mm、グラデーション不可、最小6pt、工業洗濯40回後の実際の低下、EN ISO 20471の表示の線引きと検針機の反応、用途別5例と見積6項目をまとめました。",
        sum_ko="금은사는 메인 라벨을 매장에서 단번에 알아보게 하고, 반사사는 야간 러닝 재킷을 헤드라이트에 띄웁니다. 다만 실만 바꿔서는 짤 수 없습니다. 다섯 계열 사의 효과와 물리적 한계, 최세 선 0.6~0.8mm, 그라데이션 불가, 최소 6pt, 산업 세탁 40회 후 실제 저하, EN ISO 20471 표시의 경계와 침검기 반응, 용도별 다섯 조합과 견적 여섯 항목을 정리했습니다.",
        sum_fr="Le fil métallique rend un label de col lisible en rayon, le fil réfléchissant fait ressortir une veste de running dans les phares. Mais un fil spécial ne se substitue pas sans réflexion. Cinq familles et leurs limites physiques, le trait minimal de 0,6 à 0,8 mm, l'impossibilité de dégradé, 6 pt minimum, la perte réelle après quarante lavages industriels, la ligne rouge EN ISO 20471 et la détection d'aiguilles. Plus cinq combinaisons d'usage et six points de devis.",
        sum_es="El hilo metálico hace legible una etiqueta de cuello en la tienda; el reflectante hace que una chaqueta de running aparezca en los faros. Pero un hilo especial no se sustituye sin más. Cinco familias y sus límites físicos, el trazo mínimo de 0,6 a 0,8 mm, la imposibilidad de degradados, 6 pt mínimo, la pérdida real tras cuarenta lavados industriales, la línea roja de EN ISO 20471 y la detección de agujas. Más cinco combinaciones de uso y seis datos de presupuesto.",
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
            'data-ja="泰閣包装 · %s更新" data-ko="TAGE 패키징 · %s" '
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
