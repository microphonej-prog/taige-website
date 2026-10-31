#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-31 20:00 批次每日更新生成脚本（六语：zh-Hant 根 / en / ja / ko / fr / es）
- 医用与防护类服装的标签与包装（medical-ppe-garment-labeling-guide）
- 唛头与吊牌上的商标符号（trademark-symbols-garment-labels）

用法: F:/hermes/venvs/tools/Scripts/python.exe daily_gen_20261031_2000.py [--check]
"""
import os, re, sys, subprocess, importlib.util

ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)
PY = sys.executable

SKEL = "blog/knitwear-sweater-trims-guide.html"
DATE_ZH = "2026年10月31日"
DATE_EN = "October 31, 2026"
DATE_JA = "2026年10月31日更新"
DATE_KO = "2026년 10월 31일 업데이트"
DATE_FR = "31 octobre 2026"
DATE_ES = "31 de octubre de 2026"
SITEMAP_DATE = "2026-10-31"
BUST_OLD, BUST_NEW = "188", "189"
LANGS = ["en", "ja", "ko", "fr", "es"]

ARTICLES = [
    dict(
        slug="medical-ppe-garment-labeling-guide.html",
        body="blog/_body_medicalppe.html",
        title_zh="医用与防护类服装的标签与包装：CE、EN 13795 与灭菌兼容 | TAGE",
        title_en="Labels and Packaging for Medical and Protective Garments: CE, EN 13795 and Sterilisation | TAGE",
        title_ja="医療・防護服のラベルと包装：CE、EN 13795、滅菌適合 | TAGE",
        title_ko="의료·보호복 라벨과 포장: CE, EN 13795, 멸균 적합성 | TAGE",
        title_fr="Étiquettes et emballages des vêtements médicaux : CE, EN 13795 et stérilisation | TAGE",
        title_es="Etiquetas y embalaje de prendas médicas y de protección: CE, EN 13795 y esterilización | TAGE",
        desc_zh="医用与防护服标签指南：先分清普通服装、防护用品与医疗器械的监管身份，标签必写的五类信息，环氧乙烷与辐照灭菌下的标签包装成套验证，洗涤次数如何用辅料数据支撑，性能声称怎么不越界，附下单前确认清单。来自东莞泰阁包装。",
        desc_en="Medical and protective garment labels: regulatory status, mandatory information, sterilisation compatibility, wash claims and a pre-order checklist.",
        desc_ja="医療・防護服のラベルガイド。一般衣料・防護具・医療機器の規制上の区分、必須記載5項目、EO・放射線滅菌でのラベルと包装のセット検証、洗濯回数の裏づけ、性能表示の範囲、発注前チェックリストを解説します。東莞泰閣包装。",
        desc_ko="의료·보호복 라벨 가이드. 일반 의류·보호구·의료기기 구분, 필수 기재 다섯 항목, EO·방사선 멸균 시 라벨과 포장 세트 검증, 세탁 횟수 근거, 성능 표시 범위, 발주 전 체크리스트를 정리했습니다. 둥관 TAGE 패키징.",
        desc_fr="Étiquettes des vêtements médicaux et de protection : statut réglementaire, cinq informations obligatoires, compatibilité de stérilisation, preuves de lavage, liste avant commande.",
        desc_es="Etiquetas de prendas médicas y de protección: estatus regulatorio, cinco informaciones obligatorias, compatibilidad de esterilización, lavados y lista previa al pedido.",
        crumb_zh="医用防护标签",
        crumb_en="Medical and PPE Labels",
        crumb_ja="医療・防護ラベル",
        crumb_ko="의료·보호 라벨",
        crumb_fr="Étiquettes médicales",
        crumb_es="Etiquetas médicas",
        h1_zh="医用与防护类服装的标签与包装：CE、EN 13795 与灭菌兼容",
        h1_en="Labels and Packaging for Medical and Protective Garments: CE, EN 13795 and Sterilisation",
        h1_ja="医療・防護服のラベルと包装：CE、EN 13795、滅菌適合",
        h1_ko="의료·보호복 라벨과 포장: CE, EN 13795, 멸균 적합성",
        h1_fr="Étiquettes et emballages des vêtements médicaux : CE, EN 13795 et stérilisation",
        h1_es="Etiquetas y embalaje de prendas médicas y de protección: CE, EN 13795 y esterilización",
        tag_zh="医用与防护", tag_en="Medical and PPE", tag_ja="医療・防護", tag_ko="의료·보호",
        tag_fr="Médical et EPI", tag_es="Médico y EPI",
        sum_zh="医用防护服装的标签不只是成分和尺码，它要承担监管身份、性能等级和可追溯性。本文讲清普通服装、防护用品与医疗器械三种身份的区别，标签必写的五类信息，环氧乙烷与辐照灭菌下为什么要把标签和包装袋成套验证，洗涤次数怎么用辅料实测数据支撑，以及性能声称写到哪一步就越界。",
        sum_en="A medical or protective garment label is not just fibre content and size: it carries regulatory identity, performance class and traceability. Covers the three statuses, five mandatory information groups, why labels and pouches are validated together for EO and irradiation, how wash-cycle claims need trim test data, and where performance claims overreach.",
        sum_ja="医療・防護服のラベルは組成やサイズだけではありません。規制上の位置づけ、性能クラス、トレーサビリティを担います。3つの区分の違い、必須記載5項目、EO・放射線滅菌でラベルと包装袋をセット検証する理由、洗濯回数を副資材の実測データで裏づける方法、性能表示が越境する境界を整理します。",
        sum_ko="의료·보호복 라벨은 소재와 사이즈만이 아니라 규제상 정체성, 성능 등급, 추적성을 담습니다. 세 가지 구분의 차이, 필수 기재 다섯 항목, EO·방사선 멸균에서 라벨과 포장 봉투를 함께 검증하는 이유, 세탁 횟수를 부자재 실측 데이터로 뒷받침하는 방법, 성능 표시의 한계를 정리합니다.",
        sum_fr="Une étiquette de vêtement médical ou de protection ne se limite pas à la composition et à la taille : elle porte l'identité réglementaire, la classe de performance et la traçabilité. Au programme : les trois statuts, cinq informations obligatoires, la validation conjointe étiquette et sachet en OE et irradiation, les preuves de lavage et les limites des allégations.",
        sum_es="Una etiqueta de prenda médica o de protección no es solo composición y talla: lleva identidad regulatoria, clase de prestación y trazabilidad. Incluye los tres estatus, cinco informaciones obligatorias, por qué etiqueta y bolsa se validan juntas en EO e irradiación, las pruebas de lavado y los límites de las declaraciones.",
    ),
    dict(
        slug="trademark-symbols-garment-labels.html",
        body="blog/_body_tmsymbol.html",
        title_zh="唛头与吊牌上的商标符号怎么用：™、®、© 与注册信息 | TAGE",
        title_en="Trademark Symbols on Labels and Hang Tags: TM, (R), Copyright and Registration | TAGE",
        title_ja="ネームと下げ札の商標表示：™・®・© と登録情報 | TAGE",
        title_ko="라벨과 행택의 상표 표기: ™, ®, ©와 등록 정보 | TAGE",
        title_fr="Symboles de marque sur labels et hangtags : ™, ®, © et mentions d'enregistrement | TAGE",
        title_es="Símbolos de marca en etiquetas y colgantes: ™, ®, © y datos de registro | TAGE",
        desc_zh="唛头与吊牌上的商标符号指南：™、®、©、℠ 四个符号的准确含义，注册前用 ® 在中美欧的法律风险，四个主要市场的标注惯例，织唛上符号的可读性下限与排版位置，OEM 订单里客户商标的授权与海关备案，附七个常见错误。",
        desc_en="Trademark symbols on labels and hang tags: what TM, (R), copyright and service marks mean, using R before registration, market practice and OEM licensing.",
        desc_ja="ネームと下げ札の商標記号ガイド。™・®・©・℠ の正確な意味、登録前に ® を使うリスク、主要4市場の慣行、織りネームでの判読性の下限と位置、OEM での客先商標のライセンスと税関登録、よくある7つの誤りを解説します。",
        desc_ko="라벨·행택 상표 기호 가이드. ™·®·©·℠의 정확한 의미, 등록 전 ® 사용 위험, 주요 4개 시장 관행, 직조 라벨에서 판독 최소 기준과 위치, OEM 고객 상표 허가와 세관 등록, 흔한 실수 일곱 가지를 정리했습니다.",
        desc_fr="Symboles de marque sur labels et hangtags : sens exact de ™, ®, © et ℠, risque d'utiliser ® avant enregistrement, usages par marché, lisibilité sur tissé et licences OEM.",
        desc_es="Símbolos de marca en etiquetas y colgantes: significado de ™, ®, © y ℠, riesgo de usar ® antes del registro, práctica por mercado, legibilidad en tejido y licencias OEM.",
        crumb_zh="商标符号规范",
        crumb_en="Trademark Symbols",
        crumb_ja="商標記号のルール",
        crumb_ko="상표 기호 규칙",
        crumb_fr="Symboles de marque",
        crumb_es="Símbolos de marca",
        h1_zh="唛头与吊牌上的商标符号怎么用：™、®、© 与注册信息",
        h1_en="Trademark Symbols on Labels and Hang Tags: TM, (R), Copyright and Registration",
        h1_ja="ネームと下げ札の商標表示：™・®・© と登録情報",
        h1_ko="라벨과 행택의 상표 표기: ™, ®, ©와 등록 정보",
        h1_fr="Symboles de marque sur labels et hangtags : ™, ®, © et mentions d'enregistrement",
        h1_es="Símbolos de marca en etiquetas y colgantes: ™, ®, © y datos de registro",
        tag_zh="标签合规", tag_en="Label Compliance", tag_ja="ラベル基準", tag_ko="라벨 컴플라이언스",
        tag_fr="Conformité", tag_es="Cumplimiento",
        sum_zh="唛头、吊牌、包装袋上印哪个符号，是品牌资产在实物上唯一的法律声明。® 用错地方，在部分国家构成虚假标记；™ 用错地方等于什么都没说。本文讲清四个符号的含义、注册前后的差别、四个主要市场的惯例、织唛排版的可读性下限，以及 OEM 订单里客户商标的授权与海关备案。",
        sum_en="Which symbol goes on a neck label or hang tag is the only legal statement of brand ownership on the product. ® in the wrong place is false marking in some countries; ™ in the wrong place says nothing. Covers the four symbols, practice before and after registration, four markets, the legibility floor on woven labels and OEM licensing.",
        sum_ja="ネームや下げ札、包装袋にどの記号を入れるかは、ブランド資産が現物上で示す唯一の法的表示です。® を誤れば国によっては虚偽表示、™ を誤れば何も言っていないのと同じ。4つの記号の意味、登録前後の違い、主要4市場の慣行、織りネームの判読性の下限、OEM での授权と税関登録を整理します。",
        sum_ko="라벨과 행택, 포장 봉투에 어떤 기호를 넣느냐는 브랜드 자산이 실물에서 표시되는 유일한 법적 선언입니다. ®를 잘못 쓰면 일부 국가에서 허위 표시이고, ™를 잘못 쓰면 아무 말도 하지 않은 것과 같습니다. 네 기호의 의미, 등록 전후 차이, 주요 4개 시장 관행, 직조 라벨의 판독 기준, OEM 허가와 세관 등록을 정리합니다.",
        sum_fr="Le symbole imprimé sur un label, un hangtag ou un sachet est la seule mention juridique de propriété de marque portée par le produit. Un ® mal placé est un faux marquage dans certains pays ; un ™ hors de propos n'énonce rien. Au programme : les quatre symboles, avant et après enregistrement, quatre marchés, la lisibilité sur tissé et les licences OEM.",
        sum_es="Qué símbolo va en la etiqueta, el colgante o la bolsa es la única declaración jurídica de titularidad sobre el producto. Un ® mal puesto es falso marcado en algunos países; un ™ fuera de lugar no dice nada. Cubre los cuatro símbolos, antes y después del registro, cuatro mercados, la legibilidad en tejido y las licencias OEM.",
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
    s, n = re.subn(r'<p data-zh="泰[阁閣]包[装裝] · 更新[于於][^\"]*\".*?</p>', meta, s, count=1, flags=re.S)
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
