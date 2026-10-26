#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-26 20:00 批次每日更新生成脚本（六语：zh-Hant 根 / en / ja / ko / fr / es）
- 抗菌辅料与卫生包装（apparel-trims-antibacterial-hygiene-packaging）
- 服装辅料与包装静电控制（apparel-trims-static-dust-control）

用法: F:/hermes/venvs/tools/Scripts/python.exe daily_gen_20261026_2000.py [--check]
"""
import os, re, sys, subprocess, importlib.util

ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)
PY = sys.executable

SKEL = "blog/knitwear-sweater-trims-guide.html"
DATE_ZH = "2026年10月26日"
DATE_EN = "October 26, 2026"
DATE_JA = "2026年10月26日更新"
DATE_KO = "2026년 10월 26일 업데이트"
DATE_FR = "26 octobre 2026"
DATE_ES = "26 de octubre de 2026"
SITEMAP_DATE = "2026-10-26"
BUST_OLD, BUST_NEW = "184", "185"
LANGS = ["en", "ja", "ko", "fr", "es"]

ARTICLES = [
    dict(
        slug="apparel-trims-antibacterial-hygiene-packaging.html",
        body="blog/_body_antibac.html",
        title_zh="抗菌辅料与卫生包装指南：银离子、抑菌袋与声明合规 | TAGE",
        title_en="Antibacterial Trims and Hygiene Packaging: Claims That Hold Up | TAGE",
        title_ja="抗菌副資材と衛生包装ガイド：銀イオン・抗菌袋・表示の適法性 | TAGE",
        title_ko="항균 부자재와 위생 포장 가이드: 은이온·항균 비닐·표시 적법성 | TAGE",
        title_fr="Accessoires antibactériens et emballage hygiénique : allégations défendables | TAGE",
        title_es="Accesorios antibacterianos y embalaje higiénico: alegaciones defendibles | TAGE",
        desc_zh="抗菌辅料与卫生包装指南：哪些品类真的需要抗菌，银系、锌系与后整理三条路线怎么选，洗水标与吊牌上的抗菌宣称怎么写才经得住审查，欧盟 BPR 与美国 FTC 的红线在哪，抑菌袋与干燥剂怎么配，抗菌率报告必看的四个要点。来自东莞泰阁包装。",
        desc_en="Antibacterial trims and hygiene packaging: which categories need it, silver and zinc routes, wording that survives EU and US rules, reading test reports.",
        desc_ja="抗菌副資材と衛生包装のガイド。本当に必要な品種、銀系・亜鉛系・後加工の3つのルート、洗濯表示とタグに書ける表示の範囲、EUのBPRと米国FTCの境界、抗菌袋と乾燥剤の組み方、抗菌率報告書で見るべき4点を解説します。東莞泰閣包装。",
        desc_ko="항균 부자재와 위생 포장 가이드. 실제로 필요한 품목, 은계·아연계·후가공 세 가지 경로, 케어 라벨과 행택에 쓸 수 있는 표시 범위, EU BPR과 미국 FTC의 경계, 항균 비닐과 제습제 구성, 항균율 성적서에서 볼 네 가지를 정리했습니다. 둥관 TAGE 패키징.",
        desc_fr="Accessoires antibactériens et emballage hygiénique : quelles catégories en ont besoin, voies argent et zinc, formulation conforme aux règles UE et US, lecture des rapports.",
        desc_es="Accesorios antibacterianos y embalaje higiénico: qué categorías lo necesitan, vías de plata y zinc, redacción conforme a las normas UE y EE. UU., y lectura de informes.",
        crumb_zh="抗菌辅料与卫生包装",
        crumb_en="Antibacterial Trims & Hygiene Packaging",
        crumb_ja="抗菌副資材と衛生包装",
        crumb_ko="항균 부자재와 위생 포장",
        crumb_fr="Accessoires antibactériens",
        crumb_es="Accesorios antibacterianos",
        h1_zh="抗菌辅料与卫生包装指南：银离子、抑菌袋与声明合规",
        h1_en="Antibacterial Trims and Hygiene Packaging: What You Can Actually Claim",
        h1_ja="抗菌副資材と衛生包装ガイド：銀イオン、抗菌袋、表示の適法性",
        h1_ko="항균 부자재와 위생 포장 가이드: 은이온, 항균 비닐, 표시 적법성",
        h1_fr="Accessoires antibactériens et emballage hygiénique : ce que l'on peut réellement alléguer",
        h1_es="Accesorios antibacterianos y embalaje higiénico: qué se puede alegar de verdad",
        tag_zh="功能辅料", tag_en="Functional Trims", tag_ja="機能副資材", tag_ko="기능성 부자재",
        tag_fr="Accessoires techniques", tag_es="Accesorios técnicos",
        sum_zh="「抗菌」已经成了内衣、袜品与婴童装询盘里的常客，但它同时是功效宣称：写在吊牌上要有报告支撑，写在洗水标上不能暗示医疗效果。本文分五步拆开——什么品类真的需要、纤维母粒与后整理两条技术路线的耐久性与成本、欧盟 BPR 与美国 FTC 的红线、抑菌袋加干燥剂加封口贴的五件套配置，以及抗菌率报告必须对齐的菌种、洗涤次数与方法四件事，最后给出可以直接抄进规格书的七条。",
        sum_en="Antibacterial has become a routine line in underwear, hosiery and kidswear inquiries — and it is a performance claim, so a hang tag needs a report behind it and a care label must not hint at a medical effect. This guide works through five steps: which categories genuinely need it, the durability and cost of fibre masterbatch versus after-finish, the EU and US red lines, the five-piece hygiene set of treated bag, desiccant and seal, and the organism, wash count and method that a report must match — closing with seven clauses for your spec sheet.",
        sum_ja="抗菌は下着・靴下・子供服の引き合いで定番になりましたが、同時に効能表示です。タグには報告書の裏付けが必要で、洗濯表示は医療的効果を示唆できません。本稿は5段階で整理します。本当に必要な品種、繊維マスターバッチと後加工の耐久性とコスト、EUのBPRと米国FTCの境界、抗菌袋・乾燥剤・封緘シールの5点セット、報告書で菌種・洗濯回数・方法を揃えるべき4点、最後に仕様書へ転記できる7項目。",
        sum_ko="항균은 속옷·양말·아동복 문의에서 상투적인 항목이 되었지만 동시에 효능 표시입니다. 행택에는 성적서가 뒷받침해야 하고, 케어 라벨은 의료적 효능을 암시해서는 안 됩니다. 이 글은 다섯 단계로 정리합니다. 실제로 필요한 품목, 섬유 마스터배치와 후가공의 내구성·원가, EU BPR과 미국 FTC의 경계, 항균 비닐·제습제·봉인 스티커 다섯 가지 세트, 성적서에서 균종·세탁 횟수·방법을 맞춰야 하는 네 가지, 마지막으로 사양서에 옮길 일곱 항목.",
        sum_fr="L'antibactérien est devenu une ligne habituelle des demandes en lingerie, chaussetterie et enfant — et c'est une allégation de performance : un hangtag exige un rapport, une étiquette d'entretien ne doit pas suggérer un effet médical. Ce guide avance en cinq étapes : les catégories réellement concernées, la durabilité et le coût du masterbatch en fibre face au finissage, les lignes rouges UE et américaines, le jeu hygiénique de cinq pièces, et les quatre points qu'un rapport doit aligner — pour finir sur sept clauses à recopier.",
        sum_es="Lo antibacteriano se ha vuelto una línea habitual en consultas de ropa interior, calcetería y moda infantil, y a la vez es una alegación de prestación: el colgante exige un informe y la etiqueta de cuidado no debe insinuar un efecto médico. Esta guía avanza en cinco pasos: qué categorías lo necesitan, durabilidad y coste del masterbatch en fibra frente al acabado, las líneas rojas de la UE y EE. UU., el juego higiénico de cinco piezas y los cuatro puntos que un informe debe alinear, cerrando con siete cláusulas.",
    ),
    dict(
        slug="apparel-trims-static-dust-control.html",
        body="blog/_body_static.html",
        title_zh="服装辅料与包装静电控制指南：深色成衣吸尘与袋口吸附 | TAGE",
        title_en="Static Control in Garment Packaging: Dark Garments and Bag Mouths | TAGE",
        title_ja="衣料品包装の静電気対策：濃色衣料の埃付着と袋口の密着 | TAGE",
        title_ko="의류 포장 정전기 대책: 어두운 의류 먼지와 비닐 입구 밀착 | TAGE",
        title_fr="Maîtrise de l'électricité statique : vêtements foncés et sachets | TAGE",
        title_es="Control de la estática en embalaje textil: prendas oscuras y bolsas | TAGE",
        desc_zh="服装包装静电控制指南：深色成衣为什么会吸尘、OPP 袋为什么打不开，母粒型、涂布型与材料替代怎么选，车间控湿 45% 到 55% 与离子风机怎么落地，表面电阻与静电衰减怎么验收，抗静电袋与 ESD 屏蔽袋有何区别。来自东莞泰阁包装。",
        desc_en="Static in garment packaging: why dark garments pick up lint and OPP bags stay shut, four material routes, humidity and ionising fixes, plus three tests.",
        desc_ja="衣料品包装の静電気対策ガイド。濃色衣料が埃を吸う理由、OPP袋が開かない理由、シールが飛ぶ理由、マスターバッチ型・塗布型・材料代替の4つの道、湿度45〜55%とイオンファンの運用、表面抵抗と電荷減衰の検収、帯電防止袋とESD遮蔽袋の違いを解説します。東莞泰閣包装。",
        desc_ko="의류 포장 정전기 대책 가이드. 어두운 의류가 먼지를 끌어당기는 이유, OPP 비닐이 열리지 않는 이유, 스티커가 날리는 이유, 마스터배치형·코팅형·소재 대체 네 가지 경로, 습도 45~55%와 이온 팬 운용, 표면 저항과 전하 감쇠 검수, 대전방지 비닐과 ESD 차폐 비닐의 차이를 정리했습니다. 둥관 TAGE 패키징.",
        desc_fr="Maîtrise de la statique en emballage textile : pourquoi les vêtements foncés attirent la poussière et les sachets OPP ne s'ouvrent pas, quatre voies matière, humidité et ionisation, et vérification.",
        desc_es="Control de la estática en embalaje textil: por qué las prendas oscuras atraen polvo y las bolsas OPP no se abren, cuatro vías de material, humedad e ionización, y cómo verificarlo.",
        crumb_zh="静电与吸尘控制",
        crumb_en="Static & Dust Control",
        crumb_ja="静電気と埃の対策",
        crumb_ko="정전기와 먼지 관리",
        crumb_fr="Statique et poussière",
        crumb_es="Estática y polvo",
        h1_zh="服装辅料与包装的静电控制：深色成衣吸尘与袋口吸附怎么治",
        h1_en="Static Control in Apparel Packaging: Dust on Dark Garments and Clinging Bags",
        h1_ja="衣料品包装の静電気対策：濃色衣料の埃付着と袋口の密着をどう抑えるか",
        h1_ko="의류 포장 정전기 대책: 어두운 의류 먼지와 비닐 입구 밀착 해결",
        h1_fr="Maîtriser la statique en emballage textile : poussière sur vêtements foncés et sachets collants",
        h1_es="Controlar la estática en el embalaje textil: polvo en prendas oscuras y bolsas pegadas",
        tag_zh="包装技术", tag_en="Packaging Engineering", tag_ja="包装技術", tag_ko="포장 기술",
        tag_fr="Ingénierie d'emballage", tag_es="Ingeniería de embalaje",
        sum_zh="深色成衣在验货台擦一下就一道白、OPP 袋撕不开、小贴纸不肯落到工位——这些多半不是品质缺陷，而是静电，而且它永远不会出现在检验报告里。本文把成因拆成摩擦剥离、材料与环境三条件，列出四种现场表现与后果，给出母粒型、涂布型、材料替代与控湿四条路径，讲清 45% 到 55% 湿度与离子风机的落地位置，并提供表面电阻、电荷衰减与现场对比三种可验收的测法，最后点出抗静电袋与 ESD 屏蔽袋混淆等三个常见坑。",
        sum_en="A dark garment wipes a white smear on the inspection table, an OPP bag refuses to open, small stickers will not drop to the station — usually not defects but static, and static never appears in an inspection report. This guide splits the cause into friction, material and humidity, lists four floor symptoms with their consequences, sets out four routes from masterbatch film to substitution, places humidity control and ionisers where they work, and gives three verifiable tests — surface resistance, charge decay, bench comparison — closing on three traps including confusing anti-static with ESD shielding.",
        sum_ja="濃色衣料を検品台で拭くと白い筋が出る、OPP袋が開かない、小さなシールが所定位置に落ちない——多くは品質不良ではなく静電気で、しかも検査報告書には現れません。本稿は原因を摩擦・剥離、材料、環境の3条件に分け、現場で起きる4つの症状と結果、マスターバッチ型・塗布型・材料代替・湿度管理の4つの道、湿度45〜55%とイオンファンの配置、表面抵抗・電荷減衰・現場比較という検収可能な3つの試験、帯電防止袋とESD遮蔽袋の混同など3つの落とし穴を整理します。",
        sum_ko="어두운 의류를 검품대에서 닦으면 흰 줄이 생기고, OPP 비닐이 열리지 않고, 작은 스티커가 제자리에 떨어지지 않습니다. 대부분 품질 결함이 아니라 정전기이며, 정전기는 검사 성적서에 나오지 않습니다. 이 글은 원인을 마찰·박리, 소재, 환경 세 조건으로 나누고, 현장의 네 가지 증상과 결과, 마스터배치형·코팅형·소재 대체·습도 관리 네 가지 경로, 습도 45~55%와 이온 팬 배치, 표면 저항·전하 감쇠·현장 비교라는 검수 가능한 세 가지 시험, 대전방지 비닐과 ESD 차폐 비닐 혼동 등 세 가지 함정을 정리합니다.",
        sum_fr="Un vêtement foncé essuyé sur la table de contrôle laisse une traînée blanche, un sachet OPP refuse de s'ouvrir, de petites étiquettes ne tombent pas au poste : rarement un défaut, souvent de la statique — et la statique n'apparaît jamais dans un rapport. Ce guide sépare frottement, matière et humidité, décrit quatre symptômes d'atelier et leurs conséquences, propose quatre voies du film masterbatch à la substitution, place l'hygrométrie et l'ionisation là où elles agissent, et donne trois essais vérifiables, avant trois pièges dont la confusion antistatique / blindage ESD.",
        sum_es="Una prenda oscura deja una marca blanca en la mesa de inspección, una bolsa OPP no se abre, las pegatinas no caen al puesto: casi nunca es un defecto, es estática, y la estática no aparece en ningún informe. Esta guía separa fricción, material y humedad, describe cuatro síntomas de planta y sus consecuencias, plantea cuatro vías del film con masterbatch a la sustitución, sitúa la humedad y la ionización donde actúan y ofrece tres ensayos verificables, cerrando con tres trampas, entre ellas confundir antiestático con blindaje ESD.",
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
