#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-11-04 14:00 批次（六语：zh-Hant 根 / en / ja / ko / fr / es）
- 服装辅料 pH 值与皮肤安全（trims-ph-value-skin-safety）
- 辅料缝制设备与附件配置（garment-trims-sewing-equipment-guide）

用法: F:/hermes/venvs/tools/Scripts/python.exe daily_gen_20261104_1400.py [--check]
"""
import os, re, sys, subprocess, importlib.util

ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)
PY = sys.executable

SKEL = "blog/knitwear-sweater-trims-guide.html"
DATE_ZH = "2026年11月4日"
DATE_EN = "November 4, 2026"
DATE_JA = "2026年11月4日"
DATE_KO = "2026년 11월 4일 업데이트"
DATE_FR = "4 novembre 2026"
DATE_ES = "4 de noviembre de 2026"
SITEMAP_DATE = "2026-11-04"
BUST_OLD, BUST_NEW = "197", "198"
LANGS = ["en", "ja", "ko", "fr", "es"]

ARTICLES = [
    dict(
        slug="trims-ph-value-skin-safety.html",
        body="blog/_body_ph.html",
        title_zh="服裝輔料 pH 值與皮膚安全：織嘜、洗水標、吊牌為什麼都要測 | TAGE",
        title_en="Trim pH and Skin Safety: Why Woven Labels and Tags Need Testing | TAGE",
        title_ja="衣料副資材の pH と皮膚安全性：織りラベル・洗濯表示・値札を測る理由 | TAGE",
        title_ko="의류 부자재 pH와 피부 안전성: 직조 라벨·세탁 표시·행택을 측정하는 이유 | TAGE",
        title_fr="pH des accessoires et sécurité cutanée : pourquoi tester labels et étiquettes | TAGE",
        title_es="pH de los accesorios y seguridad cutánea: por qué analizar etiquetas | TAGE",
        desc_zh="服装辅料也要测 pH：纱线浆料、洗水标涂层、纸吊牌填料与胶袋助剂都可能偏碱。讲清 GB 18401 的 A/B/C 三类限值、GB/T 7573 测试口径、五类辅料的偏碱来源、超标后的四条改善路径与五条验收条款。来自东莞泰阁包装。",
        desc_en="Trim pH explained: GB 18401 class A, B and C limits, where alkalinity comes from in woven labels, care labels and tags, the test method, and five acceptance clauses.",
        desc_ja="衣料副資材も pH 測定が必要です。糸の糊剤、洗濯表示のコーティング、紙の填料、袋の添加剤はアルカリ残留の源になります。GB 18401 の A・B・C 類の限度値と GB/T 7573 の試験方法、5種類の副資材別の発生源、規格外時の4つの改善経路、購買文書にそのまま書ける5つの検収条項を解説します。東莞泰閣包装。",
        desc_ko="의류 부자재도 pH 측정이 필요합니다. 실 사이징, 세탁 표시 코팅, 종이 충전제, 봉투 첨가제가 알칼리 잔류 원인입니다. GB 18401 A/B/C 등급 한도와 GB/T 7573 시험 방법, 다섯 부자재별 발생원, 규격 미달 시 네 가지 개선 경로, 구매 문서에 바로 쓸 다섯 가지 검수 조항을 정리합니다. 둥관 TAGE 패키징.",
        desc_fr="Le pH des accessoires : limites des classes A, B et C de la GB 18401, sources d'alcalinité dans labels tissés, étiquettes d'entretien et pendantes, méthode d'essai et cinq clauses de réception.",
        desc_es="El pH de los accesorios: límites de las clases A, B y C de la GB 18401, fuentes de alcalinidad en etiquetas y colgantes, método de ensayo y cinco cláusulas de recepción.",
        crumb_zh="pH 與皮膚安全",
        crumb_en="pH and Skin Safety",
        crumb_ja="pH と皮膚安全性",
        crumb_ko="pH와 피부 안전성",
        crumb_fr="pH et sécurité cutanée",
        crumb_es="pH y seguridad cutánea",
        h1_zh="服裝輔料 pH 值與皮膚安全：織嘜、洗水標、吊牌為什麼都要測",
        h1_en="Trim pH and Skin Safety: Why Woven Labels, Care Labels and Tags All Need Testing",
        h1_ja="衣料副資材の pH と皮膚安全性：織りラベル・洗濯表示・値札を測る理由",
        h1_ko="의류 부자재 pH와 피부 안전성: 직조 라벨·세탁 표시·행택을 모두 측정해야 하는 이유",
        h1_fr="pH des accessoires et sécurité cutanée : pourquoi tester labels tissés, étiquettes et pendantes",
        h1_es="pH de los accesorios y seguridad cutánea: por qué analizar etiquetas tejidas, de cuidado y colgantes",
        tag_zh="品質與合規", tag_en="Quality and Compliance", tag_ja="品質・コンプライアンス",
        tag_ko="품질·컴플라이언스", tag_fr="Qualité et conformité", tag_es="Calidad y cumplimiento",
        sum_zh="贴身穿的那一层，pH 比手感更早说话。这篇讲清 GB 18401 的 A/B/C 三类限值、五类辅料各自的偏碱来源（纱线浆料、涂层中和剂、纸张碳酸钙填料、薄膜助剂、自粘胶）、GB/T 7573 与 ISO 3071 的测试口径与误差来源，超标后的四条改善路径，最后给五条可以直接抄进采购文件的验收条款。",
        sum_en="The layer against the skin speaks through pH before it speaks through hand-feel. This covers the class A, B and C limits of GB 18401, where alkalinity comes from in five trim families, how GB/T 7573 and ISO 3071 actually run and where the error hides, four routes to fix a fail, and five acceptance clauses for the purchasing file.",
        sum_ja="肌に接する層は、風合いより先に pH で語ります。GB 18401 の A・B・C 類の限度値、5種類の副資材それぞれのアルカリ源（糸の糊剤、コーティング中和剤、紙の炭酸カルシウム填料、フィルム添加剤、粘着剤）、GB/T 7573 と ISO 3071 の試験口径と誤差、規格外時の4つの改善経路、購買文書にそのまま書ける5つの検収条項をまとめます。",
        sum_ko="피부에 닿는 층은 촉감보다 pH로 먼저 말합니다. GB 18401의 A/B/C 등급 한도, 다섯 부자재별 알칼리 발생원(실 사이징, 코팅 중화제, 종이 탄산칼슘 충전제, 필름 첨가제, 점착제), GB/T 7573과 ISO 3071의 시험 기준과 오차, 규격 미달 시 네 가지 개선 경로, 구매 문서에 바로 쓸 다섯 가지 검수 조항을 정리합니다.",
        sum_fr="La couche contre la peau parle par le pH avant de parler par le toucher. Limites des classes A, B et C de la GB 18401, sources d'alcalinité dans cinq familles d'accessoires, déroulé réel des essais GB/T 7573 et ISO 3071 avec leurs sources d'erreur, quatre voies de correction et cinq clauses de réception.",
        sum_es="La capa que toca la piel habla antes por el pH que por el tacto. Límites de las clases A, B y C de la GB 18401, fuentes de alcalinidad en cinco familias de accesorios, cómo se ejecutan GB/T 7573 e ISO 3071 y dónde se esconde el error, cuatro vías de corrección y cinco cláusulas de recepción.",
    ),
    dict(
        slug="garment-trims-sewing-equipment-guide.html",
        body="blog/_body_sewequip.html",
        title_zh="服裝輔料縫製設備與附件配置：縫標機、壓腳與針板怎麼配 | TAGE",
        title_en="Sewing Equipment for Trims: Label Machines, Presser Feet, Needle Plates | TAGE",
        title_ja="副資材の縫製設備と付属品：ラベル縫い機・押え金・針板の選び方 | TAGE",
        title_ko="부자재 봉제 설비와 부속품: 라벨 재봉기·노루발·바늘판 구성 | TAGE",
        title_fr="Machines et accessoires de couture pour étiquettes : pieds, plaques, réglages | TAGE",
        title_es="Máquinas y accesorios de costura para etiquetas: prensatelas y placas | TAGE",
        desc_zh="主唛、洗水标、尺码标在车间怎么缝得平、缝得快：单针、双针、缝标机、包缝与同步机的分工，压脚、针板、送布牙、折边器的选配，针号针尖与张力，按品类配置对照表，以及换款必调的六个参数与首件调试卡。来自东莞泰阁包装。",
        desc_en="How to sew neck labels, care labels and size labels flat and fast: machine types, presser feet, needle plates, feed dogs, folders, needles and changeover settings.",
        desc_ja="メインラベル、洗濯表示、サイズ表示を平らに速く縫うには。単針・2本針・ラベル縫い機・オーバーロック・複合送りの使い分け、押え金・針板・送り歯・フォルダーの選定、針番と張力、品目別の対応表、品番切替で調整する6つのパラメータと初物カードを解説します。東莞泰閣包装。",
        desc_ko="메인 라벨, 세탁 표시, 사이즈 표시를 평평하고 빠르게 봉제하는 방법. 단침·두 바늘·라벨 재봉기·오버록·복합 이송의 구분, 노루발·바늘판·이송 톱니·폴더 선택, 바늘 호수와 장력, 품목별 대응표, 품번 전환 시 조정할 여섯 파라미터와 초물 카드를 정리합니다. 둥관 TAGE 패키징.",
        desc_fr="Coudre labels de col, étiquettes d'entretien et de taille à plat et vite : types de machines, pieds presseurs, plaques, griffes, guides-plis, aiguilles et fiche de réglage.",
        desc_es="Coser etiquetas de cuello, de cuidado y de talla planas y rápido: tipos de máquina, prensatelas, placas, dientes, plegadores, agujas y ficha de ajuste.",
        crumb_zh="輔料縫製設備",
        crumb_en="Trim Sewing Equipment",
        crumb_ja="副資材の縫製設備",
        crumb_ko="부자재 봉제 설비",
        crumb_fr="Équipement de couture",
        crumb_es="Equipo de costura",
        h1_zh="服裝輔料縫製設備與附件配置：縫標機、壓腳與針板怎麼配",
        h1_en="Sewing Equipment and Attachments for Trims: Machines, Feet and Needle Plates",
        h1_ja="副資材の縫製設備と付属品：ラベル縫い機・押え金・針板の構成",
        h1_ko="부자재 봉제 설비와 부속품: 라벨 재봉기·노루발·바늘판 구성",
        h1_fr="Équipement et accessoires de couture pour étiquettes : machines, pieds et plaques",
        h1_es="Equipo y accesorios de costura para etiquetas: máquinas, prensatelas y placas",
        tag_zh="生產工藝", tag_en="Production", tag_ja="生産工程",
        tag_ko="생산 공정", tag_fr="Production", tag_es="Producción",
        sum_zh="标签缝得平不平、一件多花几秒、洗五次后还在不在原位，取决于机台与附件是否配对。这篇按五种机型的分工、压脚与针板的选配、针号线与张力、按品类配置对照表、换款六参数与首件调试卡五部分讲，全部是车间里能直接照着调的东西。",
        sum_en="Whether a label lies flat, how many seconds each garment costs, and whether it survives five washes all come down to machine and attachment matching. Five machine types and their limits, presser feet and needle plates, needles, thread and tension, a table by category, and the six parameters plus a setup card for changeover.",
        sum_ja="ラベルが平らに縫えるか、1着あたり何秒かかるか、5回洗って残るかは、機械と付属品の組み合わせで決まります。5種類の機械の役割と限界、押え金と針板の選定、針・糸・張力、品目別の対応表、品番切替の6パラメータと初物カードという5部構成で、現場でそのまま調整できる内容をまとめました。",
        sum_ko="라벨이 평평하게 봉제되는지, 한 벌에 몇 초가 드는지, 다섯 번 세탁 후에도 남는지는 기계와 부속품의 조합에 달려 있습니다. 다섯 가지 기계의 역할과 한계, 노루발과 바늘판 선택, 바늘·실·장력, 품목별 대응표, 품번 전환의 여섯 파라미터와 초물 카드를 정리했습니다.",
        sum_fr="Qu'une étiquette soit plate, le temps par pièce et sa survie après cinq lavages tiennent à l'appariement machine-accessoires. Cinq types de machines et leurs limites, pieds et plaques, aiguilles, fils et tension, un tableau par catégorie, et six paramètres avec une fiche de réglage.",
        sum_es="Que una etiqueta quede plana, cuántos segundos cuesta cada prenda y si sobrevive a cinco lavados depende del emparejamiento máquina-accesorios. Cinco tipos de máquina y sus límites, prensatelas y placas, agujas, hilo y tensión, tabla por categoría, y seis parámetros con ficha de ajuste.",
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
