#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-11-05 14:00 批次（六语：zh-Hant 根 / en / ja / ko / fr / es）
- 北欧四国服装标签合规（nordic-apparel-labelling-compliance）
- 低温环境下的服装辅料性能（garment-trims-low-temperature-performance）

用法: F:/hermes/venvs/tools/Scripts/python.exe daily_gen_20261105_1400.py [--check]
"""
import os, re, sys, subprocess, importlib.util

ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)
PY = sys.executable

SKEL = "blog/knitwear-sweater-trims-guide.html"
DATE_ZH = "2026年11月5日"
DATE_EN = "November 5, 2026"
DATE_JA = "2026年11月5日"
DATE_KO = "2026년 11월 5일 업데이트"
DATE_FR = "5 novembre 2026"
DATE_ES = "5 de noviembre de 2026"
SITEMAP_DATE = "2026-11-05"
BUST_OLD, BUST_NEW = "200", "201"
LANGS = ["en", "ja", "ko", "fr", "es"]

ARTICLES = [
    dict(
        slug="nordic-apparel-labelling-compliance.html",
        body="blog/_body_nordic.html",
        title_zh="北欧服装标签合规：瑞典语、丹麦语、芬兰语标注与天鹅生态标签 | TAGE",
        title_en="Nordic Apparel Labelling: Swedish, Danish, Finnish and Norwegian Text plus the Nordic Swan | TAGE",
        title_ja="北欧の衣料ラベル規制：スウェーデン語・デンマーク語・フィンランド語表示とノルディックスワン | TAGE",
        title_ko="북유럽 의류 라벨 규정: 스웨덴어·덴마크어·핀란드어 표시와 노르딕 스완 | TAGE",
        title_fr="Étiquetage textile dans les pays nordiques : suédois, danois, finnois et Écolabel nordique | TAGE",
        title_es="Etiquetado textil en los países nórdicos: sueco, danés, finés y Etiqueta Ecológica Nórdica | TAGE",
        desc_zh="北欧四国服装标签合规：瑞典、丹麦、芬兰属欧盟，挪威只在 EEA；标签须用当地语言，芬兰常需芬兰语与瑞典语双语，包装分别走四套生产者责任体系，天鹅生态标签另有化学品门槛。附四语标签用词对照表与出货前七项检查。",
        desc_en="Nordic apparel labelling: Swedish, Danish, Finnish and Norwegian wording, four national packaging EPR schemes, and what the Nordic Swan Ecolabel adds.",
        desc_ja="北欧4か国の衣料ラベル規制を整理。スウェーデン・デンマーク・フィンランドは EU、ノルウェーは EEA のみで法定言語はノルウェー語。包装は4か国それぞれの生産者責任制度、ノルディックスワンの化学物質要件、4言語の用語対照表と出荷前7項目チェックを掲載します。",
        desc_ko="북유럽 4개국 의류 라벨 규정 정리. 스웨덴·덴마크·핀란드는 EU, 노르웨이는 EEA로 법정 언어는 노르웨이어입니다. 포장은 4개국 각자의 생산자 책임 제도, 노르딕 스완의 화학물질 요건, 4개 언어 용어 대조표와 출하 전 일곱 가지 점검을 담았습니다.",
        desc_fr="Étiquetage textile nordique : mentions en suédois, danois, finnois et norvégien, quatre régimes REP emballages, et ce qu'ajoute l'Écolabel nordique.",
        desc_es="Etiquetado textil nórdico: menciones en sueco, danés, finés y noruego, cuatro regímenes REP de envases y lo que añade la Etiqueta Ecológica Nórdica.",
        crumb_zh="北欧服装标签合规",
        crumb_en="Nordic Labelling Compliance",
        crumb_ja="北欧のラベル規制",
        crumb_ko="북유럽 라벨 규정",
        crumb_fr="Conformité nordique",
        crumb_es="Cumplimiento nórdico",
        h1_zh="北欧服装标签合规：瑞典语、丹麦语、芬兰语标注与天鹅生态标签",
        h1_en="Nordic Apparel Labelling: Swedish, Danish, Finnish and Norwegian Text plus the Nordic Swan",
        h1_ja="北欧の衣料ラベル規制：スウェーデン語・デンマーク語・フィンランド語表示とノルディックスワン",
        h1_ko="북유럽 의류 라벨 규정: 스웨덴어·덴마크어·핀란드어 표시와 노르딕 스완",
        h1_fr="Étiquetage textile dans les pays nordiques : suédois, danois, finnois et Écolabel nordique",
        h1_es="Etiquetado textil en los países nórdicos: sueco, danés, finés y Etiqueta Ecológica Nórdica",
        tag_zh="合规与出口", tag_en="Compliance &amp; Export", tag_ja="コンプライアンス・輸出",
        tag_ko="컴플라이언스·수출", tag_fr="Conformité et export", tag_es="Cumplimiento y exportación",
        sum_zh="北欧人口不到三千万，客单价却是欧洲最高的一档。退单多不是因为印刷差，而是消费者信息没有当地语言、包装没在所在国注册生产者责任、客户拿了天鹅标而辅料拿不出化学品声明。附四语标签用词对照表与出货前七项检查。",
        sum_en="Fewer than thirty million people, some of Europe's highest tickets. Rejections come from consumer information without a local language, packaging never registered under the national EPR scheme, and Swan-labelled clients whose trims carry no chemical declaration. A four-language wording table and seven pre-shipment checks.",
        sum_ja="人口は3,000万人弱でも客単価は欧州最高水準。返品は印刷品質より、現地語のない消費者情報、各国 EPR に未登録の包装、スワン取得客先に提出できない化学物質宣言が原因です。4言語の用語対照表と出荷前7項目チェックを掲載します。",
        sum_ko="인구는 3천만 명이 안 되지만 객단가는 유럽 최고 수준입니다. 반품은 인쇄 품질보다 현지어 없는 소비자 정보, 각국 EPR에 미등록된 포장, 스완 인증 고객에게 제출 못 하는 화학물질 신고서 때문입니다. 4개 언어 용어 대조표와 출하 전 일곱 가지 점검을 담았습니다.",
        sum_fr="Moins de trente millions d'habitants, des paniers parmi les plus élevés d'Europe. Les refus tiennent aux informations sans langue locale, aux emballages non enregistrés en REP nationale et aux clients Cygne sans déclaration chimique des accessoires. Tableau en quatre langues et sept contrôles.",
        sum_es="Menos de treinta millones de habitantes y tickets entre los más altos de Europa. Los rechazos vienen de información sin idioma local, envases no registrados en la REP nacional y clientes con el Cisne sin declaración química de accesorios. Tabla en cuatro idiomas y siete controles.",
    ),
    dict(
        slug="garment-trims-low-temperature-performance.html",
        body="blog/_body_lowtemp.html",
        title_zh="低温环境下的服装辅料：脆化、脱胶与冬季选型指南 | TAGE",
        title_en="Trims in Cold Weather: Brittleness, Adhesive Failure and Winter Material Selection | TAGE",
        title_ja="低温環境の衣料副資材：脆化・接着不良と冬物の選材ガイド | TAGE",
        title_ko="저온 환경의 의류 부자재: 취화·접착 불량과 겨울 소재 선택 | TAGE",
        title_fr="Accessoires par temps froid : fragilisation, décollage et choix des matériaux | TAGE",
        title_es="Accesorios en clima frío: fragilización, despegue y selección de materiales | TAGE",
        desc_zh="低温环境下的服装辅料：软 PVC 胶袋在 -15℃ 变脆、自粘标翘边、洗水标涂层开裂、纸吊牌曲翘。讲清玻璃化转变、胶层初粘与含水率的影响，给出冷折与回温两个测试方法、七个位置的选材对照表，以及该写进规格书的条件。",
        desc_en="Cold-weather trims: why PVC bags crack at -15°C, self-adhesive labels lift, care-label coatings fail and paper tags warp, plus two tests and a selection table.",
        desc_ja="低温環境の衣料副資材を整理。軟質 PVC 袋の -15℃ 脆化、粘着ラベルの浮き、洗濯表示のコーティング割れ、紙の値札の反りを取り上げ、ガラス転移・初期粘着・含水率の影響、冷間折りと常温復帰の二試験、七つの位置の選材表を掲載します。",
        desc_ko="저온 환경의 의류 부자재 정리. 연질 PVC 봉투의 -15℃ 취화, 점착 라벨 들뜸, 세탁 표시 코팅 갈라짐, 종이 행택 휨을 다루고 유리전이·초기 점착·함수율의 영향, 저온 굽힘과 상온 복귀 두 시험, 일곱 위치의 소재 선택표를 담았습니다.",
        desc_fr="Accessoires par temps froid : sachets PVC cassants à -15 °C, autocollants qui se décollent, enductions d'entretien qui craquent, cartons qui gondolent. Deux essais et un tableau de choix.",
        desc_es="Accesorios en clima frío: bolsas de PVC frágiles a -15 °C, autoadhesivos que se despegan, recubrimientos de cuidado agrietados y colgantes alabeados. Dos ensayos y tabla de selección.",
        crumb_zh="低温辅料性能",
        crumb_en="Trims in Cold Weather",
        crumb_ja="低温の副資材性能",
        crumb_ko="저온 부자재 성능",
        crumb_fr="Accessoires au froid",
        crumb_es="Accesorios en frío",
        h1_zh="低温环境下的服装辅料：脆化、脱胶与冬季选型指南",
        h1_en="Trims in Cold Weather: Brittleness, Adhesive Failure and Winter Material Selection",
        h1_ja="低温環境の衣料副資材：脆化・接着不良と冬物の選材ガイド",
        h1_ko="저온 환경의 의류 부자재: 취화·접착 불량과 겨울 소재 선택",
        h1_fr="Accessoires par temps froid : fragilisation, décollage et choix des matériaux",
        h1_es="Accesorios en clima frío: fragilización, despegue y selección de materiales",
        tag_zh="材料与工艺", tag_en="Materials &amp; Craft", tag_ja="素材と加工",
        tag_ko="소재와 공정", tag_fr="Matières et façonnage", tag_es="Materiales y procesos",
        sum_zh="冬季订单的辅料问题，一半在常温验货时看不出来：-15℃ 胶袋一折发白、自粘标几天后翘边、洗水标弯折掉墨、纸吊牌吸湿后曲翘。讲清低温改变的三参数、六种失效、两个够用的测试与七个位置的选材对照。",
        sum_en="Half of winter trim problems are invisible at room temperature: bags whitening at the fold at -15°C, labels lifting after a few days, care-label ink lost on folding, paper tags warping once damp. Three parameters, six failures, two tests and a seven-position selection table.",
        sum_ja="冬物案件の副資材トラブルの半分は常温検品では見えません。-15℃ で折ると白化する袋、数日後に浮く粘着ラベル、折るとインキが落ちる洗濯表示、吸湿後に反る紙の値札。三つのパラメータ、六つの不良、二つの試験、七つの位置の選材表を整理します。",
        sum_ko="겨울 주문 부자재 문제의 절반은 상온 검품에서 보이지 않습니다. -15℃에서 접으면 하얗게 되는 봉투, 며칠 뒤 들뜨는 점착 라벨, 접으면 잉크가 떨어지는 세탁 표시, 습기를 먹고 휘는 종이 행택. 세 가지 파라미터, 여섯 가지 불량, 두 가지 시험, 일곱 위치의 소재 선택표를 정리합니다.",
        sum_fr="La moitié des problèmes d'accessoires d'hiver échappe au contrôle à température ambiante : sachets qui blanchissent au pli à -15 °C, autocollants qui se relèvent, encre perdue au pliage, cartons qui gondolent. Trois paramètres, six défaillances, deux essais et un tableau de choix.",
        sum_es="La mitad de los problemas de accesorios de invierno no se ve a temperatura ambiente: bolsas que blanquean al doblar a -15 °C, autoadhesivos que se levantan, tinta perdida al plegar, cartones que se alabean. Tres parámetros, seis fallos, dos ensayos y una tabla de selección.",
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
            'data-ja="泰閣包装 · %s更新" data-ko="TAGE 패키징 · %s" '
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
