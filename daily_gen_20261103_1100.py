#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-11-03 11:00 批次（六语：zh-Hant 根 / en / ja / ko / fr / es）
- 标签对色的光源与同色异谱（label-color-metamerism-guide）
- 吊牌受潮起翘：含水率、覆膜应力与仓储（hang-tag-moisture-curl-guide）

用法: F:/hermes/venvs/tools/Scripts/python.exe daily_gen_20261103_1100.py [--check]
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
BUST_OLD, BUST_NEW = "194", "195"
LANGS = ["en", "ja", "ko", "fr", "es"]

ARTICLES = [
    dict(
        slug="label-color-metamerism-guide.html",
        body="blog/_body_metamerism.html",
        title_zh="标签对色的光源与同色异谱：为什么客户说颜色不对 | TAGE",
        title_en="Label Colour Under Different Lights: Metamerism Explained | TAGE",
        title_ja="ラベルの色合わせと光源：メタメリズムで色が違って見える理由 | TAGE",
        title_ko="라벨 색상과 광원: 메타메리즘 때문에 색이 달라 보이는 이유 | TAGE",
        title_fr="Couleur des étiquettes et sources lumineuses : le métamérisme | TAGE",
        title_es="Color de etiquetas y fuentes de luz: el metamerismo | TAGE",
        desc_zh="标签对色为什么总在客户那里出问题：同色异谱的成因、D65 与 TL84 等四种光源各自对应的卖场、ΔE00 容差怎么定、验收记录写什么，以及六条减少跨材质色差的实操。来自东莞泰阁包装。",
        desc_en="Labels that match in the pressroom and fail in store: what metamerism is, which light sources to check under, Delta E tolerances and six fixes for drift.",
        desc_ja="ラベルの色が工場では合うのに店頭で違う——メタメリズムの原因、D65・TL84 など4つの光源と売場の対応、ΔE00 許容差の決め方、承認記録の項目、素材間の色ずれを減らす6つの実務を解説します。東莞泰閣包装。",
        desc_ko="공장에서는 맞던 라벨 색이 매장에서 다르다면: 메타메리즘의 원인, D65·TL84 등 네 가지 광원과 매장 대응, ΔE00 허용 범위 설정, 승인 기록 항목, 소재 간 색 편차를 줄이는 여섯 가지 실무를 정리했습니다. 둥관 TAGE 패키징.",
        desc_fr="Étiquettes conformes en atelier et fausses en boutique : métamérisme, sources à contrôler, tolérances Delta E et six pratiques contre la dérive de couleur.",
        desc_es="Etiquetas correctas en taller y falsas en tienda: metamerismo, fuentes de control, tolerancias Delta E y seis prácticas contra la deriva de color.",
        crumb_zh="标签对色与同色异谱",
        crumb_en="Label Colour and Metamerism",
        crumb_ja="ラベルの色とメタメリズム",
        crumb_ko="라벨 색과 메타메리즘",
        crumb_fr="Couleur et métamérisme",
        crumb_es="Color y metamerismo",
        h1_zh="标签对色的光源与同色异谱：为什么客户说颜色不对",
        h1_en="Label Colour Under Different Lights: Why the Buyer Says It Is Wrong",
        h1_ja="ラベルの色合わせと光源：客先が色違いと言う理由",
        h1_ko="라벨 색상과 광원: 고객이 색이 다르다고 하는 이유",
        h1_fr="Couleur des étiquettes et sources lumineuses : pourquoi le client dit que c'est faux",
        h1_es="Color de etiquetas y fuentes de luz: por qué el cliente dice que está mal",
        tag_zh="工艺细节", tag_en="Production Detail", tag_ja="工程詳細", tag_ko="공정 디테일",
        tag_fr="Détail technique", tag_es="Detalle técnico",
        sum_zh="工厂灯下看过、客户也确认了色号，货到门店却被说颜色不对——多数不是印错，而是换了光源。本文讲同色异谱的成因、四种对色光源各自对应的卖场、ΔE00 容差怎么定才可执行，以及六条减少跨材质色差的实操。",
        sum_en="Checked under the factory lamp and approved by the buyer, then judged wrong in store: usually not a printing error but a different light source. What causes metamerism, which lamp matches which market, how to set a Delta E tolerance people follow, and six ways to cut colour drift across materials.",
        sum_ja="工場のライトで確認し、客先も色番を承認したのに、店頭で色が違うと言われる。多くは印刷ミスではなく光源の違いです。メタメリズムの原因、4つの光源と売場の対応、実行できるΔE00許容差の決め方、素材間の色ずれを減らす6つの実務を解説します。",
        sum_ko="공장 조명에서 확인하고 고객도 색 번호를 승인했는데 매장에서 색이 다르다는 말이 돌아옵니다. 대개 인쇄 오류가 아니라 광원 차이입니다. 메타메리즘의 원인, 네 가지 광원과 매장 대응, 실제로 지킬 수 있는 ΔE00 허용 범위, 소재 간 색 편차를 줄이는 여섯 가지 방법을 정리합니다.",
        sum_fr="Contrôlée sous la lampe de l'atelier et validée par l'acheteur, puis jugée fausse en boutique : rarement une erreur d'impression, souvent une autre lumière. Causes du métamérisme, sources par marché, tolérance Delta E applicable et six façons de réduire la dérive entre supports.",
        sum_es="Revisada bajo la lámpara del taller y aprobada por el cliente, y luego juzgada mal en tienda: casi nunca es un error de impresión sino otra luz. Causas del metamerismo, fuentes por mercado, tolerancia Delta E aplicable y seis formas de reducir la deriva entre sustratos.",
    ),
    dict(
        slug="hang-tag-moisture-curl-guide.html",
        body="blog/_body_curl.html",
        title_zh="吊牌受潮起翘怎么办：含水率、覆膜应力与仓储防翘 | TAGE",
        title_en="Hang Tags That Curl: Moisture, Lamination Stress and Storage | TAGE",
        title_ja="タグの反り返り対策：含水率・ラミネート応力・保管の湿度管理 | TAGE",
        title_ko="행택 말림 대책: 함수율·라미네이팅 응력·보관 습도 관리 | TAGE",
        title_fr="Étiquettes qui tuilent : humidité, contrainte de pelliculage et stockage | TAGE",
        title_es="Etiquetas que se curvan: humedad, tensión de laminado y almacenaje | TAGE",
        desc_zh="吊牌到货就起翘、整叠码不齐、挂上衣服歪一边：从纸张含水率、单面覆膜应力、模切堆叠到集装箱雨，讲清五个环节的控制点，附已经翘了的补救办法与询价必说的四项信息。来自东莞泰阁包装。",
        desc_en="Why hang tags curl: paper moisture, single-sided lamination stress, die-cut stacks and container rain, with recovery steps and what to state in a quote.",
        desc_ja="タグが届いた時点で反り返る理由：紙の含水率、片面ラミネートの応力、抜き加工と積み重ね、コンテナレイン。5つの工程の管理点と、反った後の対処、見積依頼で伝える4項目を解説します。東莞泰閣包装。",
        desc_ko="행택이 도착하자마자 말리는 이유: 종이 함수율, 단면 라미네이팅 응력, 도무와 적재, 컨테이너 레인. 다섯 단계의 관리점과 말린 뒤 대처, 견적 요청 시 밝혀야 할 네 가지 정보를 정리했습니다. 둥관 TAGE 패키징.",
        desc_fr="Pourquoi les étiquettes tuilent : humidité du papier, contrainte de pelliculage simple face, piles de découpe et pluie de conteneur, avec les remèdes.",
        desc_es="Por qué se curvan las etiquetas: humedad del papel, tensión del laminado a una cara, pilas de troquel y lluvia de contenedor, con soluciones.",
        crumb_zh="吊牌受潮起翘",
        crumb_en="Hang Tag Curl",
        crumb_ja="タグの反り返り",
        crumb_ko="행택 말림",
        crumb_fr="Tuilage des étiquettes",
        crumb_es="Curvado de etiquetas",
        h1_zh="吊牌受潮起翘怎么办：含水率、覆膜应力与仓储防翘",
        h1_en="Hang Tags That Curl: Moisture Content, Lamination Stress and Storage",
        h1_ja="タグの反り返り対策：含水率・ラミネート応力・保管時の湿度",
        h1_ko="행택 말림 대책: 함수율·라미네이팅 응력·보관 습도",
        h1_fr="Étiquettes qui tuilent : humidité, contrainte de pelliculage et stockage",
        h1_es="Etiquetas que se curvan: humedad, tensión de laminado y almacenaje",
        tag_zh="工艺细节", tag_en="Production Detail", tag_ja="工程詳細", tag_ko="공정 디테일",
        tag_fr="Détail technique", tag_es="Detalle técnico",
        sum_zh="拆箱就发现吊牌边缘上卷、整叠码不齐、挂上衣服歪一边。原因多半不在印刷，而在含水率与覆膜应力。本文按成因、含水率区间、印刷后道、仓储海运、事后补救五部分讲，并给出询价该说清的四项信息。",
        sum_en="Open the carton and the tags are curled at the edges, the stack no longer flat, the garment hanging crooked. Usually not printing but moisture and lamination stress. Causes, moisture ranges, press and finishing control, storage and sea freight, plus how to recover.",
        sum_ja="開梱するとタグの縁が反り返り、束が揃わず、服に付けると傾く。原因は多くが印刷ではなく含水率とラミネート応力です。原因、含水率の範囲、印刷・加工の管理、倉庫と海上輸送、事後の対処の5部構成で解説します。",
        sum_ko="상자를 열면 행택 가장자리가 말려 있고, 묶음이 가지런하지 않고, 옷에 달면 기웁니다. 원인은 대개 인쇄가 아니라 함수율과 라미네이팅 응력입니다. 원인, 함수율 구간, 인쇄·후가공 관리, 창고와 해상 운송, 사후 대처를 다섯 부분으로 정리합니다.",
        sum_fr="À l'ouverture, les étiquettes sont tuilées, la pile ne reste plus plane, la pièce pend de travers. Rarement l'impression : plutôt l'humidité et la contrainte de pelliculage. Causes, plages d'humidité, contrôle en presse, stockage et maritime, puis remèdes.",
        sum_es="Al abrir la caja las etiquetas están curvadas, la pila ya no queda plana, la prenda cuelga torcida. Casi nunca es la impresión: son la humedad y la tensión del laminado. Causas, rangos de humedad, control en prensa, almacén y marítimo, y soluciones.",
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
    print("  %-45s desc_zh=%d字 desc_en=%d字符 desc_ja=%d desc_ko=%d desc_fr=%d desc_es=%d"
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
