#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-11-02 20:00 批次每日更新生成脚本（六语：zh-Hant 根 / en / ja / ko / fr / es）
- 服装辅料机器视觉质检（apparel-trims-machine-vision-inspection）
- 服装可拆解设计与可回收辅料（garment-disassembly-recyclable-trims）

用法: F:/hermes/venvs/tools/Scripts/python.exe daily_gen_20261102_2000.py [--check]
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
BUST_OLD, BUST_NEW = "192", "193"
LANGS = ["en", "ja", "ko", "fr", "es"]

ARTICLES = [
    dict(
        slug="apparel-trims-machine-vision-inspection.html",
        body="blog/_body_vision.html",
        title_zh="服装辅料机器视觉质检指南：能查什么、怎么落地 | TAGE",
        title_en="Machine Vision Inspection for Apparel Trims: What It Can Check | TAGE",
        title_ja="衣料副資材のマシンビジョン検査：検査できる範囲と導入の進め方 | TAGE",
        title_ko="의류 부자재 머신 비전 검사: 검사 범위와 도입 방법 | TAGE",
        title_fr="Contrôle par vision des accessoires : ce qu'il peut vraiment vérifier | TAGE",
        title_es="Inspección por visión de accesorios: qué puede controlar y qué no | TAGE",
        desc_zh="服装辅料机器视觉质检的落地指南：织唛字符、吊牌套印色差与胶袋封口分别用什么光源与阈值，ΔE 公差怎么和客户约定，人机对比怎么做，多大的订单规模才值得上设备。来自东莞泰阁包装。",
        desc_en="Machine vision for apparel trims: which defects are detectable, the lighting and thresholds for woven-label characters and hang-tag ΔE, and when the ROI works.",
        desc_ja="衣料副資材のマシンビジョン検査ガイド。織りネームの文字、下げ札の見当・色差、ポリ袋の封口に必要な光源としきい値、ΔE 公差の取り決め、人と機械の比較方法、設備投資に見合う受注規模を解説します。東莞泰閣包装。",
        desc_ko="의류 부자재 머신 비전 검사 가이드. 직조 라벨 문자, 행택 정합·색차, 폴리백 밀봉에 필요한 광원과 임계값, ΔE 공차 합의, 사람과 기계 비교 방법, 설비 투자에 맞는 주문 규모를 정리했습니다. 둥관 TAGE 패키징.",
        desc_fr="Vision artificielle sur accessoires : défauts détectables, éclairage et seuils pour labels tissés et étiquettes, tolérances ΔE, comparaison homme-machine et seuil de rentabilité.",
        desc_es="Visión artificial en accesorios: defectos detectables, iluminación y umbrales para etiquetas tejidas y colgantes, tolerancias ΔE, comparación hombre-máquina y cuándo es rentable.",
        crumb_zh="机器视觉质检",
        crumb_en="Machine Vision Inspection",
        crumb_ja="マシンビジョン検査",
        crumb_ko="머신 비전 검사",
        crumb_fr="Contrôle par vision",
        crumb_es="Inspección por visión",
        h1_zh="服装辅料机器视觉质检指南：能查什么、怎么落地",
        h1_en="Machine Vision Inspection for Apparel Trims: What It Can Check and How to Roll It Out",
        h1_ja="衣料副資材のマシンビジョン検査：検査できる範囲と導入の進め方",
        h1_ko="의류 부자재 머신 비전 검사: 검사 범위와 도입 방법",
        h1_fr="Contrôle par vision des accessoires : ce qu'il peut vérifier et comment le déployer",
        h1_es="Inspección por visión de accesorios: qué puede controlar y cómo implantarla",
        tag_zh="品质管理", tag_en="Quality Control", tag_ja="品質管理", tag_ko="품질 관리",
        tag_fr="Contrôle qualité", tag_es="Control de calidad",
        sum_zh="相机的价格早就不是门槛，门槛在光源与阈值。本文按织唛字符、吊牌套印色差、胶袋封口三类场景，说明各自需要什么光源与分辨率、ΔE 公差怎么定、哪些缺陷视觉永远查不了，并给出「离线抽检—工位辅助—在线全检」的三步落地顺序与判断投资是否值得的三个条件。",
        sum_en="Camera price stopped being the barrier years ago; lighting and thresholds are. This guide works through three scenarios — woven-label characters, hang-tag registration and colour, poly-bag seals — showing the lighting and resolution each needs, how to fix ΔE tolerances, what vision will never catch, plus a three-step rollout and three tests for whether the investment pays.",
        sum_ja="カメラの価格はもう障壁ではありません。障壁は光源としきい値です。本記事は織りネームの文字、下げ札の見当と色差、ポリ袋の封口という3つの場面ごとに、必要な光源と解像度、ΔE 公差の決め方、画像検査が原理的に検出できない欠点を示し、オフライン抜き取り→工程補助→インライン全数という3段階の導入順序と、投資判断の3条件を解説します。",
        sum_ko="카메라 가격은 이미 장벽이 아닙니다. 장벽은 광원과 임계값입니다. 이 글은 직조 라벨 문자, 행택 정합과 색차, 폴리백 밀봉 세 가지 상황별로 필요한 광원과 해상도, ΔE 공차 설정법, 비전이 원리적으로 잡지 못하는 결함을 설명하고, 오프라인 샘플링→공정 보조→인라인 전수라는 3단계 도입 순서와 투자 판단 세 가지 조건을 제시합니다.",
        sum_fr="Le prix des caméras n'est plus l'obstacle : ce sont l'éclairage et les seuils. Ce guide traite trois cas — caractères de labels tissés, repérage et couleur d'étiquettes, soudures de sacs poly — avec l'éclairage et la résolution requis, la fixation des tolérances ΔE, les défauts que la vision ne verra jamais, un déploiement en trois étapes et trois tests de rentabilité.",
        sum_es="El precio de las cámaras dejó de ser la barrera: lo son la iluminación y los umbrales. Esta guía recorre tres casos —caracteres de etiquetas tejidas, registro y color de colgantes, sellado de bolsas— con la luz y resolución necesarias, cómo fijar tolerancias ΔE, los defectos que la visión nunca verá, un despliegue en tres pasos y tres pruebas de rentabilidad.",
    ),
    dict(
        slug="garment-disassembly-recyclable-trims.html",
        body="blog/_body_disassembly.html",
        title_zh="服装可拆解设计与可回收辅料指南：单材质化与易拆标 | TAGE",
        title_en="Disassembly Design for Garments: Recyclable Trims and Mono-materials | TAGE",
        title_ja="服の分解設計と再生素材の副資材：単一素材化と外しやすいラベル | TAGE",
        title_ko="의류 분해 설계와 재활용 부자재: 단일 소재화와 분리형 라벨 | TAGE",
        title_fr="Conception démontable : accessoires recyclables et mono-matériaux | TAGE",
        title_es="Diseño desmontable: accesorios reciclables y monomaterial | TAGE",
        desc_zh="服装可拆解设计与可回收辅料指南：哪些辅料在阻碍回收、单材质化怎么做、点缝与易撕标哪种更易落地、法规信息不能让步的底线，以及用 BOM 与可拆解声明向品牌客户证明的方法。来自东莞泰阁包装。",
        desc_en="Disassembly-friendly trims: which accessories block recycling, mono-material options, tack or tear-away labels, legal text that stays, and how to document it.",
        desc_ja="服の分解設計と副資材ガイド。リサイクルを妨げる副資材、単一素材化の選択肢、タック縫いと引き剥がしラベルの使い分け、譲れない法規情報、BOM と分解宣言でブランド客先に示す方法を解説します。東莞泰閣包装。",
        desc_ko="의류 분해 설계와 부자재 가이드. 재활용을 방해하는 부자재, 단일 소재화 선택지, 태킹 봉제와 뜯김 라벨의 구분, 양보할 수 없는 법규 정보, BOM과 분해 선언으로 브랜드 고객에게 제시하는 방법을 정리했습니다. 둥관 TAGE 패키징.",
        desc_fr="Accessoires démontables : ceux qui bloquent le recyclage, choix mono-matériau, couture tack ou détachable, information légale à conserver et preuves documentaires.",
        desc_es="Accesorios desmontables: cuáles bloquean el reciclaje, opciones monomaterial, pespunte o etiqueta desprendible, información legal obligatoria y cómo documentarlo.",
        crumb_zh="可拆解设计与可回收辅料",
        crumb_en="Disassembly and Recyclable Trims",
        crumb_ja="分解設計と再生素材",
        crumb_ko="분해 설계와 재활용 부자재",
        crumb_fr="Démontabilité et recyclabilité",
        crumb_es="Desmontaje y reciclabilidad",
        h1_zh="服装可拆解设计与可回收辅料指南：单材质化与易拆标",
        h1_en="Disassembly Design for Garments: Mono-material Trims and Labels That Come Off",
        h1_ja="服の分解設計と再生素材の副資材：単一素材化と外しやすいラベル",
        h1_ko="의류 분해 설계와 재활용 부자재: 단일 소재화와 분리형 라벨",
        h1_fr="Conception démontable : accessoires mono-matériau et labels qui se retirent",
        h1_es="Diseño desmontable: accesorios monomaterial y etiquetas que se retiran",
        tag_zh="可持续与合规", tag_en="Sustainability", tag_ja="サステナビリティ", tag_ko="지속가능성",
        tag_fr="Durabilité", tag_es="Sostenibilidad",
        sum_zh="重量占比不到 5% 的辅料，常常决定一件衣服能不能被回收。本文列出五类最常阻碍回收的辅料与对应的可拆解替代，讲清单材质化的三个可操作选择、点缝与易撕标等四种拆解方式的代价、法规信息不能让步的底线，并给出向品牌客户交付的 BOM 与可拆解声明格式。",
        sum_en="Trims that weigh under five percent often decide whether a garment can be recycled at all. This guide lists the five accessories that most often block recycling with their disassembly-friendly alternatives, sets out three workable mono-material choices, the cost of four removal methods from tack stitching to tear-away labels, the legal content that cannot be traded away, and the BOM and disassembly statement a brand customer will ask for.",
        sum_ja="重量比 5% 未満の副資材が、その服をリサイクルできるかどうかを決めることがあります。本記事はリサイクルを妨げやすい5種類の副資材と分解しやすい代替案、実行可能な単一素材化の3つの選択、タック縫いから引き剥がしラベルまでの4つの取り外し方法とそのコスト、譲れない法規情報、ブランド客先が求める BOM と分解宣言の形式を示します。",
        sum_ko="무게 비중 5% 미만의 부자재가 그 옷의 재활용 가능성을 결정하는 경우가 많습니다. 이 글은 재활용을 방해하는 다섯 가지 부자재와 분해하기 쉬운 대안, 실행 가능한 단일 소재화 세 가지 선택, 태킹 봉제부터 뜯김 라벨까지 네 가지 제거 방식의 비용, 양보할 수 없는 법규 정보, 브랜드 고객이 요구하는 BOM과 분해 선언 형식을 제시합니다.",
        sum_fr="Des accessoires sous 5 % du poids décident souvent si un vêtement peut être recyclé. Ce guide liste les cinq qui bloquent le plus le recyclage avec leurs alternatives démontables, trois choix mono-matériau praticables, le coût de quatre méthodes de retrait — du point de tack au label détachable —, l'information légale non négociable, et le format de BOM et de déclaration de démontage attendu par une marque.",
        sum_es="Accesorios que pesan menos del 5 % deciden a menudo si una prenda puede reciclarse. Esta guía enumera los cinco que más bloquean el reciclaje con sus alternativas desmontables, tres opciones monomaterial practicables, el coste de cuatro métodos de retirada —del pespunte a la etiqueta desprendible—, la información legal que no se negocia y el formato de BOM y declaración de desmontaje que pide una marca.",
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
    print("  %-48s desc_zh=%d字 desc_en=%d字符 desc_ja=%d desc_ko=%d desc_fr=%d desc_es=%d"
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
