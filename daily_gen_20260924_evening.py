#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-09-24 晚间 每日更新：2 篇新文章（六语：zh-Hant 根 / en / ja / ko / fr / es）
- 春节排产与辅料交期规划：海外买家怎么提前锁定旺季产能
- 阿联酋与海湾市场服装标签合规指南：阿拉伯语标签与 GSO 要求
（主题池 30 个选题均已上线，本次为品类扩展新选题，不与既有文章重复）

用法: python daily_gen_20260924_evening.py
"""
import os, re, sys, subprocess, importlib.util

ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)
PY = sys.executable

SKEL = "blog/knitwear-sweater-trims-guide.html"
DATE_ZH = "2026年9月24日"
DATE_EN = "September 24, 2026"
DATE_JA = "2026年9月24日更新"
DATE_KO = "2026년 9월 24일 업데이트"
DATE_FR = "24 septembre 2026"
DATE_ES = "24 de septiembre de 2026"
SITEMAP_DATE = "2026-09-24"
BUST_OLD, BUST_NEW = "106", "107"
LANGS = ["en", "ja", "ko", "fr", "es"]

ARTICLES = [
    dict(
        slug="chinese-new-year-trims-order-planning.html",
        body="blog/_body_cny.html",
        title_zh="春节排产与辅料交期规划：海外买家怎么提前锁定旺季产能 | TAGE",
        title_en="Chinese New Year Trim Lead Times: How to Lock In Capacity Before the Shutdown | TAGE",
        title_ja="春節と副資材の納期計画：休業前に生産枠を確保する方法 | TAGE",
        title_ko="춘절과 부자재 납기 계획: 휴무 전에 생산 물량을 확보하는 방법 | TAGE",
        title_fr="Nouvel An chinois et délais d'accessoires : réserver sa capacité avant l'arrêt | TAGE",
        title_es="Año Nuevo chino y plazos de accesorios: reservar capacidad antes del cierre | TAGE",
        desc_zh="春节前后服装辅料交期规划指南：讲清节前赶单、停工与复工爬坡三段节奏，海运与空运的运价与舱位变化，从到货日倒排的六个关键节点，四类风险的对策，以及哪些辅料适合节前囤货和一份下单前核对清单。来自东莞泰阁包装。",
        desc_en="Plan trim orders around Chinese New Year: three shutdown phases, backward-planned lead times, freight risks, what to stockpile and a pre-order checklist.",
        desc_ja="春節前後の副資材納期計画ガイド。追い込み・休業・立ち上げの3段階、海上・航空運賃とスペースの動き、入荷日からの逆算6ステップ、4つのリスク対策、休業前に備蓄すべき品目と発注前チェックリストを解説します。東莞泰閣包装。",
        desc_ko="춘절 전후 부자재 납기 계획 가이드. 마감·휴무·재가동 세 단계, 해상·항공 운임과 선복 변화, 입고일에서 역산한 6단계, 네 가지 리스크 대응, 휴무 전 재고 확보 품목과 발주 전 체크리스트를 정리했습니다. 둥관 TAGE 패키징.",
        desc_fr="Planifier ses commandes d'accessoires autour du Nouvel An chinois : trois phases d'arrêt, rétroplanning, risques de fret, quoi stocker et liste de contrôle avant commande.",
        desc_es="Planifica los pedidos de accesorios en el Año Nuevo chino: tres fases de parada, cronograma inverso, riesgos de flete, qué almacenar y lista de comprobación previa al pedido.",
        crumb_zh="春节排产规划", crumb_en="Chinese New Year Planning", crumb_ja="春節の生産計画",
        crumb_ko="춘절 생산 계획", crumb_fr="Planification Nouvel An", crumb_es="Planificación Año Nuevo",
        h1_zh="春节排产与辅料交期规划：海外买家怎么提前锁定旺季产能",
        h1_en="Chinese New Year Trim Lead Times: How to Lock In Capacity Before the Shutdown",
        h1_ja="春節と副資材の納期計画：休業前に生産枠を確保する方法",
        h1_ko="춘절과 부자재 납기 계획: 휴무 전에 생산 물량을 확보하는 방법",
        h1_fr="Nouvel An chinois et délais d'accessoires : réserver sa capacité avant l'arrêt",
        h1_es="Año Nuevo chino y plazos de accesorios: reservar capacidad antes del cierre",
        tag_zh="交期管理", tag_en="Lead Time Planning", tag_ja="納期管理", tag_ko="납기 관리",
        tag_fr="Délais et planning", tag_es="Plazos y planificación",
        sum_zh="春节前后的辅料交期不是「多等几天」，而是整条链在同一个时点收紧。本文拆解节前赶单、停工与复工爬坡三段节奏，给出从到货日倒排的六个关键节点，四类风险的应对，以及哪些辅料适合节前囤货、哪些只能锁档期，并附一份下单前核对清单。",
        sum_en="Around Chinese New Year the trim chain does not simply run a few days late — it tightens all at once. This guide breaks the holiday into three phases, gives six milestones counted back from your arrival date, covers four risks, sorts which trims to stockpile from which to slot-book, and adds a pre-order checklist.",
        sum_ja="春節前後の副資材は「数日遅れる」のではなく、サプライチェーン全体が同じ時期に詰まります。本記事は追い込み・休業・立ち上げの三段階に分け、入荷日から逆算した6つの節目、4つのリスクと対策、備蓄向きと枠確保向きの品目、発注前チェックリストをまとめます。",
        sum_ko="춘절 전후 부자재는 '며칠 늦는 것'이 아니라 공급망 전체가 같은 시점에 조여집니다. 이 글은 마감·휴무·재가동 세 단계로 나누고, 입고일에서 역산한 여섯 단계, 네 가지 리스크 대응, 재고 확보가 유리한 품목과 일정만 잡을 품목, 발주 전 체크리스트를 정리합니다.",
        sum_fr="Autour du Nouvel An chinois, la chaîne des accessoires ne prend pas quelques jours de retard : elle se tend d'un coup. Ce guide décompose les fêtes en trois phases, donne six jalons comptés à rebours de votre date d'arrivée, traite quatre risques, trie ce qu'il faut stocker et ce qu'il faut simplement réserver, et ajoute une liste de contrôle.",
        sum_es="En el Año Nuevo chino la cadena de accesorios no se retrasa unos días: se tensa de golpe. Esta guía divide las fiestas en tres fases, da seis hitos contados hacia atrás desde la fecha de llegada, cubre cuatro riesgos, separa lo que conviene almacenar de lo que solo hay que reservar y añade una lista de comprobación.",
    ),
    dict(
        slug="clothing-label-compliance-uae.html",
        body="blog/_body_uae.html",
        title_zh="阿联酋与海湾市场服装标签合规指南：阿拉伯语标签与 GSO 要求 | TAGE",
        title_en="UAE and Gulf Clothing Label Compliance: Arabic Labels and GSO Rules | TAGE",
        title_ja="UAE・湾岸市場の衣料ラベル適合ガイド：アラビア語表記とGSO要件 | TAGE",
        title_ko="UAE·걸프 시장 의류 라벨 컴플라이언스: 아랍어 표기와 GSO 요건 | TAGE",
        title_fr="Étiquettes pour les Émirats et le Golfe : mentions en arabe et exigences GSO | TAGE",
        title_es="Etiquetas para Emiratos y el Golfo: textos en árabe y requisitos GSO | TAGE",
        desc_zh="阿联酋与海湾市场服装标签合规指南：阿拉伯语为什么是硬要求，纤维成分、洗涤说明、原产地、进口商信息等必备项怎么标，阿拉伯语在织唛上的排版与字号限制，洗涤符号与文字双轨，阿联酋与邻国的执行差异，以及清关检查最常见的六个问题和一份打样核对清单。来自东莞泰阁包装。",
        desc_en="UAE and Gulf clothing label compliance: why Arabic is mandatory, the information a garment needs, Arabic layout limits on woven labels, care symbols and import checks.",
        desc_ja="UAE・湾岸市場の衣料ラベル適合ガイド。アラビア語が必須となる理由、繊維組成・洗濯表示・原産国・輸入業者情報などの必須項目、織りラベルでのアラビア語の割り付けと文字サイズの限界、洗濯記号と文言の併用、近隣国との運用差、通関で多い6つの問題とサンプル検収チェックリストを解説します。東莞泰閣包装。",
        desc_ko="UAE·걸프 시장 의류 라벨 컴플라이언스 가이드. 아랍어가 필수인 이유, 섬유 조성·세탁 표시·원산지·수입업자 정보 등 필수 항목, 직조 라벨에서 아랍어 편집과 글자 크기 한계, 세탁 기호와 문구 병행, 인접국과의 시행 차이, 통관에서 흔한 여섯 가지 문제와 샘플 체크리스트를 정리했습니다. 둥관 TAGE 패키징.",
        desc_fr="Conformité des étiquettes pour les Émirats et le Golfe : pourquoi l'arabe est obligatoire, mentions requises, contraintes de mise en page sur tissé, symboles d'entretien et contrôles.",
        desc_es="Conformidad de etiquetas para Emiratos y el Golfo: por qué el árabe es obligatorio, menciones necesarias, límites de maquetación en tejido, símbolos de cuidado y controles.",
        crumb_zh="阿联酋标签合规", crumb_en="UAE Label Compliance", crumb_ja="UAEラベル適合",
        crumb_ko="UAE 라벨 컴플라이언스", crumb_fr="Conformité Émirats", crumb_es="Conformidad Emiratos",
        h1_zh="阿联酋与海湾市场服装标签合规指南：阿拉伯语标签与 GSO 要求",
        h1_en="UAE and Gulf Clothing Label Compliance: Arabic Labels and GSO Rules",
        h1_ja="UAE・湾岸市場の衣料ラベル適合ガイド：アラビア語表記とGSO要件",
        h1_ko="UAE·걸프 시장 의류 라벨 컴플라이언스: 아랍어 표기와 GSO 요건",
        h1_fr="Étiquettes pour les Émirats et le Golfe : mentions en arabe et exigences GSO",
        h1_es="Etiquetas para Emiratos y el Golfo: textos en árabe y requisitos GSO",
        tag_zh="合规指南", tag_en="Compliance Guide", tag_ja="適合ガイド", tag_ko="컴플라이언스 가이드",
        tag_fr="Guide conformité", tag_es="Guía de conformidad",
        sum_zh="阿联酋是中东服装进口与转口的主要门户，阿拉伯语在这里不是加分项而是硬门槛。本文梳理必备信息项、阿拉伯语在织唛上的排版与字号限制、洗涤符号与文字双轨、阿联酋与邻国的执行差异，以及清关与零售检查最常见的六个问题，并附打样核对清单。",
        sum_en="The UAE is the Middle East gateway for apparel imports and re-exports, and Arabic there is a hard requirement, not a bonus. This guide covers the mandatory information, the layout and size limits of Arabic on woven labels, symbols plus wording, differences from neighbouring markets and the six most common clearance problems.",
        sum_ja="UAEは中東の衣料品輸入・再輸出の主要ゲートウェイであり、アラビア語は加点要素ではなく必須要件です。本記事は必須表示項目、織りラベルでのアラビア語の割り付けと文字サイズの限界、洗濯記号と文言の併用、近隣国との運用差、通関・小売検査で最も多い6つの問題とサンプルチェックリストをまとめます。",
        sum_ko="UAE는 중동 의류 수입·재수출의 주요 관문이며 아랍어는 가점이 아니라 필수 요건입니다. 이 글은 필수 표시 항목, 직조 라벨에서 아랍어 편집과 글자 크기 한계, 세탁 기호와 문구 병행, 인접국과의 시행 차이, 통관·소매 검사에서 가장 흔한 여섯 가지 문제와 샘플 체크리스트를 정리합니다.",
        sum_fr="Les Émirats sont la porte d'entrée du Moyen-Orient pour l'import-export d'habillement, et l'arabe y est une exigence ferme, pas un bonus. Ce guide couvre les mentions obligatoires, les limites de mise en page de l'arabe sur tissé, symboles et textes, les écarts avec les marchés voisins et les six problèmes de dédouanement les plus fréquents.",
        sum_es="Emiratos es la puerta de Oriente Medio para la importación y reexportación de prendas, y el árabe es allí un requisito firme, no un extra. Esta guía cubre las menciones obligatorias, los límites de maquetación del árabe en tejido, símbolos y textos, las diferencias con los mercados vecinos y los seis problemas de despacho más frecuentes.",
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
    print("  %-42s desc_zh=%d字 desc_en=%d字符 desc_ja=%d desc_ko=%d desc_fr=%d desc_es=%d"
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
