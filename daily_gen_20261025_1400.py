#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-25 14:00 批次每日更新生成脚本（六语：zh-Hant 根 / en / ja / ko / fr / es）
- 杜邦纸（Tyvek）与水洗牛皮纸吊牌（tyvek-washable-paper-hang-tag-guide）
- 服装标签车缝缺陷排查（garment-label-sewing-defect-troubleshooting）

用法: F:/hermes/venvs/tools/Scripts/python.exe daily_gen_20261025_1400.py
"""
import os, re, sys, subprocess, importlib.util

ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)
PY = sys.executable

SKEL = "blog/knitwear-sweater-trims-guide.html"
DATE_ZH = "2026年10月25日"
DATE_EN = "October 25, 2026"
DATE_JA = "2026年10月25日更新"
DATE_KO = "2026년 10월 25일 업데이트"
DATE_FR = "25 octobre 2026"
DATE_ES = "25 de octubre de 2026"
SITEMAP_DATE = "2026-10-25"
BUST_OLD, BUST_NEW = "180", "181"
LANGS = ["en", "ja", "ko", "fr", "es"]

ARTICLES = [
    dict(
        slug="tyvek-washable-paper-hang-tag-guide.html",
        body="blog/_body_tyvek.html",
        title_zh="杜邦纸与水洗牛皮纸吊牌指南：耐撕、防水、可缝制怎么选 | TAGE",
        title_en="Tyvek and Washable Kraft Paper Hang Tags: A Buyer's Guide | TAGE",
        title_ja="タイベックとウォッシャブルクラフト紙のタグガイド：破れにくさ・防水・縫製 | TAGE",
        title_ko="타이벡·워셔블 크라프트지 행택 가이드: 인열·방수·재봉 | TAGE",
        title_fr="Étiquettes en Tyvek et papier kraft lavable : guide d'achat | TAGE",
        title_es="Colgantes de Tyvek y papel kraft lavable: guía de compra | TAGE",
        desc_zh="杜邦纸（Tyvek）与水洗牛皮纸吊牌耐撕、防水、可缝制，但印刷与后道和普通纸完全不同。本文对比两种材料的克重、抗撕、防水与印刷适配，讲清烫金脱落、折痕白化、孔位撕裂五个坑，并给出下单规格清单。来自东莞泰阁包装。",
        desc_en="Tyvek and washable kraft paper give tear-proof, waterproof, sewable hang tags. Compare weights, print methods, foil adhesion and five pitfalls before ordering.",
        desc_ja="タイベック（Tyvek）とウォッシャブルクラフト紙のタグは破れにくく防水で縫製も可能ですが、印刷と後加工は普通紙と大きく異なります。両素材の坪量・引裂強度・防水性・印刷適性を比較し、箔の剥がれ、折り白化、穴の裂けなど5つの落とし穴と発注前の確認項目を解説します。東莞泰閣包装。",
        desc_ko="타이벡(Tyvek)과 워셔블 크라프트지 행택은 잘 찢어지지 않고 방수·재봉이 가능하지만 인쇄와 후가공은 일반지와 크게 다릅니다. 두 소재의 평량·인열강도·방수성·인쇄 적성을 비교하고 박 탈락, 접힘 백화, 구멍 찢김 등 다섯 가지 함정과 발주 전 확인 항목을 정리했습니다. 둥관 TAGE 패키징.",
        desc_fr="Le Tyvek et le kraft lavable donnent des étiquettes indéchirables, imperméables et cousables. Grammages, impression, tenue du foil et cinq pièges avant commande.",
        desc_es="El Tyvek y el kraft lavable dan colgantes irrompibles, impermeables y cosibles. Compara gramajes, impresión, agarre del foil y cinco errores antes de pedir.",
        crumb_zh="杜邦纸与水洗纸吊牌",
        crumb_en="Tyvek and Washable Paper Tags",
        crumb_ja="タイベックとウォッシャブル紙タグ",
        crumb_ko="타이벡·워셔블지 행택",
        crumb_fr="Étiquettes Tyvek et kraft lavable",
        crumb_es="Colgantes Tyvek y kraft lavable",
        h1_zh="杜邦纸与水洗牛皮纸吊牌指南：耐撕、防水、可缝制怎么选",
        h1_en="Tyvek and Washable Kraft Paper Hang Tags: Which to Choose",
        h1_ja="タイベックとウォッシャブルクラフト紙のタグガイド：破れにくさ・防水・縫製で選ぶ",
        h1_ko="타이벡과 워셔블 크라프트지 행택 가이드: 인열·방수·재봉 기준 선택",
        h1_fr="Étiquettes en Tyvek et en papier kraft lavable : comment choisir",
        h1_es="Colgantes de Tyvek y papel kraft lavable: cómo elegir",
        tag_zh="吊牌材料", tag_en="Tag Materials", tag_ja="タグ素材", tag_ko="행택 소재",
        tag_fr="Matériaux", tag_es="Materiales",
        sum_zh="杜邦纸（Tyvek）与水洗牛皮纸是这两年最受关注的两类吊牌材料：撕不烂、不怕水、能缝在衣服上，摸起来又没有塑料感。本文讲清两者的成分与克重、抗撕与防水差异、印刷适配（UV 数码、丝印、胶印为什么容易掉墨）、烫金与模切的注意点，以及掉墨、烫金脱落、折痕白化、孔位撕裂、环保声明五个坑，最后给一份下单前要确认的规格清单。",
        sum_en="Tyvek and washable kraft paper are the two hang tag materials drawing the most attention: untearable, water-resistant, sewable and without a plastic feel. This guide sets out composition and weights, how tear strength and water resistance differ, why UV digital and screen work while offset ink lifts off, what to watch on foiling and die-cutting, five pitfalls from ink rub-off to green-claim failure, and a spec sheet to confirm before ordering.",
        sum_ja="タイベックとウォッシャブルクラフト紙は、近年最も注目されるタグ素材です。手で破れず、水に強く、衣類に縫い付けられ、プラスチック感もありません。両者の組成と坪量、引裂強度と防水性の違い、UVデジタルやスクリーンは定着しオフセットは剥がれやすい理由、箔押しと型抜きの注意点、インクのこすれ・箔剥がれ・折り白化・穴の裂け・環境表示の5つの落とし穴、発注前の確認仕様を整理します。",
        sum_ko="타이벡과 워셔블 크라프트지는 최근 가장 주목받는 행택 소재입니다. 손으로 찢기지 않고 물에 강하며 의류에 재봉할 수 있고 플라스틱 느낌도 없습니다. 두 소재의 조성과 평량, 인열강도·내수성 차이, UV 디지털과 스크린은 붙고 옵셋 잉크는 떨어지는 이유, 박압과 형압의 주의점, 잉크 묻어남·박 탈락·접힘 백화·구멍 찢김·친환경 표기 다섯 가지 함정, 발주 전 확인 사양을 정리합니다.",
        sum_fr="Le Tyvek et le kraft lavable sont les deux matériaux d'étiquettes les plus recherchés : indéchirables, résistants à l'eau, cousables et sans rendu plastique. Ce guide précise composition et grammages, les écarts de résistance à la déchirure et à l'eau, pourquoi le numérique UV et la sérigraphie tiennent quand l'encre offset se décolle, les points de vigilance en dorure et découpe, cinq pièges — encre qui s'enlève, foil qui se détache, plis blanchis, trous arrachés, allégation verte abusive — et une fiche de spécifications à valider avant commande.",
        sum_es="El Tyvek y el kraft lavable son los dos materiales de colgantes más buscados: irrompibles, resistentes al agua, cosibles y sin tacto plástico. Esta guía detalla composición y gramajes, las diferencias de desgarro e impermeabilidad, por qué el digital UV y la serigrafía agarran y la tinta offset se despega, qué vigilar en estampado y troquelado, cinco errores —tinta que se corre, foil que se despega, pliegues blanqueados, agujeros rasgados y alegación verde indebida— y una ficha de especificaciones para confirmar antes de pedir.",
    ),
    dict(
        slug="garment-label-sewing-defect-troubleshooting.html",
        body="blog/_body_sewdef.html",
        title_zh="服装标签车缝缺陷排查：起皱、歪斜、起拱的成因与对策 | TAGE",
        title_en="Label Sewing Defects: Wrinkling, Skew and Curling Fixed | TAGE",
        title_ja="衣料ラベル縫製の不良対策：しわ・傾き・反りの原因と処方 | TAGE",
        title_ko="의류 라벨 봉제 불량 대책: 주름·기울어짐·뜨는 원인과 해결 | TAGE",
        title_fr="Défauts de couture des étiquettes : plis, décalage et gondolement | TAGE",
        title_es="Defectos de costura en etiquetas: arrugas, desvío y abombamiento | TAGE",
        desc_zh="标签起皱、歪斜、两端翘起、洗后起拱，多数不是标签厂做坏了，而是标签规格与车缝工艺没对上。本文用一张表列出六种高频缺陷的成因与对策，讲清缩水率匹配、折法与缝份、验收标准怎么写。来自东莞泰阁包装。",
        desc_en="Wrinkled, skewed or lifting labels are usually a spec-versus-sewing mismatch, not a bad batch. A defect table, shrink matching and acceptance criteria.",
        desc_ja="ラベルのしわ・傾き・端の浮き・洗濯後の反りは、多くがラベル工場の不良ではなく仕様と縫製工程のミスマッチです。6つの頻出不具合の原因と処方を一表にまとめ、収縮率の整合、折り方と縫い代、受入基準の書き方を解説します。東莞泰閣包装。",
        desc_ko="라벨 주름·기울어짐·끝단 들뜸·세탁 후 휨은 대부분 라벨 공장 불량이 아니라 사양과 봉제 공정의 불일치입니다. 여섯 가지 빈발 불량의 원인과 대책을 한 표로 정리하고 수축률 매칭, 접기와 시접, 합격 기준 작성법을 설명합니다. 둥관 TAGE 패키징.",
        desc_fr="Plis, décalages et coins soulevés : rarement un lot défectueux, souvent une inadéquation entre spécification et couture. Tableau des défauts et critères.",
        desc_es="Etiquetas arrugadas, torcidas o levantadas casi nunca son un lote malo, sino un desajuste entre especificación y costura. Tabla de defectos y encogimiento.",
        crumb_zh="标签车缝缺陷排查",
        crumb_en="Label Sewing Defects",
        crumb_ja="ラベル縫製の不良対策",
        crumb_ko="라벨 봉제 불량 대책",
        crumb_fr="Défauts de couture des étiquettes",
        crumb_es="Defectos de costura de etiquetas",
        h1_zh="服装标签车缝缺陷排查手册：起皱、歪斜、起拱的成因与对策",
        h1_en="Label Sewing Defects: Causes and Fixes for Wrinkling, Skew and Curling",
        h1_ja="衣料ラベル縫製の不良対策：しわ・傾き・反りの原因と処方",
        h1_ko="의류 라벨 봉제 불량 대책: 주름·기울어짐·뜨는 원인과 해결",
        h1_fr="Défauts de couture des étiquettes : causes et corrections",
        h1_es="Defectos de costura en etiquetas: causas y correcciones",
        tag_zh="缝制工艺", tag_en="Sewing", tag_ja="縫製", tag_ko="봉제",
        tag_fr="Couture", tag_es="Costura",
        sum_zh="标签起皱、歪斜、两端翘起、洗后起拱，九成不是标签厂做坏了，而是标签规格与车缝工艺没对上。同一批织唛缝在薄针织上服帖，缝在厚卫衣上就翘边。本文用一张表给出六种高频缺陷的成因与对策，讲清缩水率匹配这一最容易被忽略的变量、四种折法对应的缝份与压线、和供应商沟通要说的四句话，以及可以直接写进技术包的 AQL 验收标准。",
        sum_en="Wrinkled labels, skewed rows, lifting corners and arching after wash are nine times out of ten a mismatch between label specification and sewing process, not a bad batch: the same woven label lies flat on fine jersey and lifts off a heavy hoodie. One table covers six frequent defects with cause and fix, then the most overlooked variable — shrink matching — the seam allowance and topstitch behind each fold type, four lines to put in every enquiry, and AQL acceptance criteria you can paste into a tech pack.",
        sum_ja="ラベルのしわ、傾き、端の浮き、洗濯後の反りは9割がラベル工場の不良ではなく、仕様と縫製工程のミスマッチです。同じ織りラベルでも薄手ニットでは収まり、厚手パーカでは浮きます。6つの頻出不具合の原因と処方を一表にまとめ、最も見落とされる収縮率の整合、4つの折り方ごとの縫い代と押さえ、仕入先に伝える4項目、仕様書にそのまま使える AQL 受入基準を解説します。",
        sum_ko="라벨 주름, 기울어짐, 끝단 들뜸, 세탁 후 휨은 90퍼센트가 라벨 공장 불량이 아니라 사양과 봉제 공정의 불일치입니다. 같은 직조 라벨도 얇은 니트에서는 붙고 두꺼운 후드에서는 뜹니다. 여섯 가지 빈발 불량의 원인과 대책을 한 표로 정리하고, 가장 놓치기 쉬운 수축률 매칭, 네 가지 접기별 시접과 겉박기, 공급사에 전달할 네 가지, 기술서에 그대로 쓸 수 있는 AQL 합격 기준을 설명합니다.",
        sum_fr="Étiquettes plissées, rangées de travers, coins qui se soulèvent, gondolement au lavage : neuf fois sur dix, c'est une inadéquation entre spécification et couture, pas un mauvais lot — le même label tissé pose à plat sur une maille fine et se soulève sur un sweat épais. Un tableau reprend six défauts fréquents avec cause et correction, puis la variable la plus négligée, l'accord de retrait, la couture et la surpiqûre propres à chaque type de pli, quatre lignes à mettre dans chaque demande et des critères AQL à copier dans le tech pack.",
        sum_es="Etiquetas arrugadas, filas torcidas, esquinas levantadas y abombamiento tras lavar son nueve de cada diez veces un desajuste entre especificación y costura, no un lote malo: la misma etiqueta tejida queda plana en un punto fino y se levanta en una sudadera gruesa. Una tabla recoge seis defectos frecuentes con causa y corrección, después la variable más olvidada —el ajuste de encogimiento—, el margen y el pespunte de cada tipo de doblez, cuatro frases para cada consulta y criterios AQL listos para el tech pack.",
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
