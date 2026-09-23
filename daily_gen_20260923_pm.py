#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-09-23 下午 每日更新：2 篇新文章（六语：zh-Hant 根 / en / ja / ko / fr / es）
- 宠物服装辅料与标签指南：主唛、洗水标、尺码与包装
- 家居服与睡衣辅料指南：绒面掉毛、套装配比与礼品包装
（主题池 30 个选题均已上线，本次为品类扩展新选题，不与既有文章重复）

用法: python daily_gen_20260923_pm.py
"""
import os, re, sys, subprocess, importlib.util

ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)
PY = sys.executable

SKEL = "blog/knitwear-sweater-trims-guide.html"
DATE_ZH = "2026年9月23日"
DATE_EN = "September 23, 2026"
DATE_JA = "2026年9月23日更新"
DATE_KO = "2026년 9월 23일 업데이트"
DATE_FR = "23 septembre 2026"
DATE_ES = "23 de septiembre de 2026"
SITEMAP_DATE = "2026-09-23"
BUST_OLD, BUST_NEW = "102", "103"
LANGS = ["en", "ja", "ko", "fr", "es"]

ARTICLES = [
    dict(
        slug="pet-apparel-trims-guide.html",
        body="blog/_body_petapparel.html",
        title_zh="宠物服装辅料与标签指南：主唛、洗水标、尺码与包装 | TAGE",
        title_en="Pet Apparel Trims Guide: Labels, Care Tags, Sizing and Packaging | TAGE",
        title_ja="ペットウェア副資材ガイド：主ラベル・洗濯表示・サイズ・包装 | TAGE",
        title_ko="펫웨어 부자재 가이드: 주 라벨, 세탁 표시, 사이즈, 포장 | TAGE",
        title_fr="Guide des accessoires pour vêtements d'animaux : labels et emballage | TAGE",
        title_es="Guía de accesorios para ropa de mascotas: etiquetas y embalaje | TAGE",
        desc_zh="宠物服装辅料定制指南：讲清犬猫尺码标怎么写、主唛材质如何按绒面与贴身款选择、洗水标要标哪些内容、反光与限用物质要求，附挂卡与自封袋包装方案和可直接询价的规格表。来自东莞泰阁包装。",
        desc_en="Pet apparel trims guide: size labels for dogs and cats, neck label materials, care label content, reflective trim, restricted substances, hang cards and zip bags for buyers.",
        desc_ja="ペットウェアの副資材ガイド。犬猫のサイズラベル、主ラベルの素材、洗濯表示ラベルの内容、反射テープ、規制物質、ハンガーカードとチャック袋の包装、見積り用の仕様表をまとめました。東莞泰閣包装。",
        desc_ko="펫웨어 부자재 가이드. 견종·고양이 사이즈 라벨, 주 라벨 소재, 세탁 표시 라벨 내용, 반사 테이프, 규제 물질, 행 카드와 지퍼백 포장, 견적용 사양표를 정리했습니다. 둥관 TAGE 패키징.",
        desc_fr="Guide accessoires vêtements d'animaux : labels de taille chien et chat, matières des labels, étiquettes d'entretien, bandes réfléchissantes, substances réglementées et emballage.",
        desc_es="Guía de accesorios para ropa de mascotas: etiquetas de talla para perros y gatos, materiales, etiquetas de cuidado, tiras reflectantes, sustancias reguladas y embalaje.",
        crumb_zh="宠物服装辅料", crumb_en="Pet Apparel Trims", crumb_ja="ペットウェア副資材",
        crumb_ko="펫웨어 부자재", crumb_fr="Accessoires animaux", crumb_es="Accesorios mascotas",
        h1_zh="宠物服装辅料与标签指南：主唛、洗水标、尺码与包装",
        h1_en="Pet Apparel Trims Guide: Labels, Care Tags, Sizing and Packaging",
        h1_ja="ペットウェア副資材ガイド：主ラベル・洗濯表示・サイズ・包装",
        h1_ko="펫웨어 부자재 가이드: 주 라벨, 세탁 표시, 사이즈, 포장",
        h1_fr="Guide des accessoires pour vêtements d'animaux : labels et emballage",
        h1_es="Guía de accesorios para ropa de mascotas: etiquetas y embalaje",
        tag_zh="宠物服装", tag_en="Pet Apparel", tag_ja="ペットウェア", tag_ko="펫웨어",
        tag_fr="Vêtements pour animaux", tag_es="Ropa para mascotas",
        sum_zh="宠物服装的辅料逻辑和人衣不同：穿着者是宠物、买单的是主人，尺码要跨犬种和猫的体长。本文讲清主唛按绒面与贴身款怎么选、洗水标该写全哪四项内容、尺码标从 XS 到 XXL 怎么换算、啃咬与皮肤接触的安全要求，以及挂卡与自封袋的包装方案，并附一份询价规格表与五步验收清单。",
        sum_en="Pet apparel follows different trims logic from human clothing: the wearer is the pet, the buyer is the owner, and sizing spans every breed plus cats. This guide covers how to choose neck labels for fleece and close-fitting styles, the four items a care label must state, converting XS to XXL with chest and back measurements, chew and skin-contact safety, plus hang cards and zip bag packaging — with a specification table and a five-step acceptance list.",
        sum_ja="ペットウェアの副資材は人用衣料とは考え方が異なります。着るのはペット、買うのは飼い主、サイズは犬種と猫の体長をまたぎます。本記事はフリースや密着スタイルに合う主ラベルの選び方、洗濯表示ラベルに必要な4項目、XS〜XXL の胸囲・背丈換算、噛みぐせと皮膚接触の安全、ハンガーカードやチャック袋の包装を解説し、仕様表と5ステップの検収リストを掲載します。",
        sum_ko="펫웨어의 부자재 논리는 사람 옷과 다릅니다. 입는 주체는 반려동물, 구매자는 보호자이며 사이즈는 견종과 고양이 체장을 아우릅니다. 이 글은 플리스와 밀착 스타일에 맞는 주 라벨 선택, 세탁 표시 라벨의 4개 필수 항목, XS~XXL 가슴둘레·등 길이 환산, 씹기와 피부 접촉 안전, 행 카드와 지퍼백 포장을 다루고 사양표와 5단계 검수 목록을 제공합니다.",
        sum_fr="Le vêtement pour animal suit une autre logique que le vêtement humain : le porteur est l'animal, l'acheteur le maître, et les tailles couvrent toutes les races et les chats. Ce guide traite le choix des labels pour la polaire et les coupes ajustées, les quatre mentions obligatoires du label d'entretien, la conversion XS à XXL en tour de poitrine et longueur de dos, la sécurité au mâchement et au contact cutané, ainsi que les cartes à suspendre et sachets zip, avec un tableau de spécifications et cinq contrôles.",
        sum_es="La ropa para mascotas sigue una lógica distinta a la humana: quien la lleva es la mascota, quien compra el dueño, y las tallas cubren todas las razas y los gatos. Esta guía trata la elección de etiquetas para polar y cortes ajustados, las cuatro menciones obligatorias de la etiqueta de cuidado, la conversión de XS a XXL en contorno de pecho y largo de espalda, la seguridad frente a mordiscos y contacto con la piel, además de tarjetas colgantes y bolsas zip, con tabla de especificaciones y cinco comprobaciones.",
    ),
    dict(
        slug="loungewear-pajama-trims-guide.html",
        body="blog/_body_loungewear.html",
        title_zh="家居服与睡衣辅料指南：绒面掉毛、套装配比与礼品包装 | TAGE",
        title_en="Loungewear and Sleepwear Trims Guide: Fleece, Set Ratios, Gift Boxes | TAGE",
        title_ja="ルームウェア・パジャマの副資材ガイド：フリース・セット比率・ギフト包装 | TAGE",
        title_ko="라운지웨어·파자마 부자재 가이드: 플리스, 세트 비율, 선물 포장 | TAGE",
        title_fr="Guide des accessoires de vêtements d'intérieur : polaire, ratios, coffrets | TAGE",
        title_es="Guía de accesorios para ropa de casa: polar, ratios y cajas de regalo | TAGE",
        desc_zh="家居服与睡衣辅料定制指南：绒类面料的主唛怎么选才不沾毛、洗水标与尺码标在套装上怎么配、吊牌与礼盒包装怎么设计，附询价规格表与五步验收清单。来自东莞泰阁包装。",
        desc_en="Loungewear and sleepwear trims guide: fleece-friendly neck labels, care and size labels for sets, hang tags, gift box packaging and a five-step sampling check.",
        desc_ja="ルームウェア・パジャマの副資材ガイド。フリースに毛が付きにくい主ラベル、セットの洗濯表示とサイズラベル、タグ、ギフト包装、5ステップの検収を解説します。東莞泰閣包装。",
        desc_ko="라운지웨어·파자마 부자재 가이드. 플리스에 보풀이 붙지 않는 주 라벨, 세트의 세탁 표시와 사이즈 라벨, 행택, 선물 포장, 5단계 검수를 정리했습니다. 둥관 TAGE 패키징.",
        desc_fr="Guide accessoires de vêtements d'intérieur : labels adaptés à la polaire, entretien et tailles en ensemble, tags, emballage coffret et contrôle d'échantillon.",
        desc_es="Guía de accesorios para ropa de casa: etiquetas para polar, cuidado y tallas en conjunto, colgantes, embalaje de regalo y control de la muestra.",
        crumb_zh="家居服辅料", crumb_en="Loungewear Trims", crumb_ja="ルームウェア副資材",
        crumb_ko="라운지웨어 부자재", crumb_fr="Accessoires vêtements d'intérieur", crumb_es="Accesorios ropa de casa",
        h1_zh="家居服与睡衣辅料指南：绒面掉毛、套装配比与礼品包装",
        h1_en="Loungewear and Sleepwear Trims Guide: Fleece, Set Ratios, Gift Boxes",
        h1_ja="ルームウェア・パジャマの副資材ガイド：フリース・セット比率・ギフト包装",
        h1_ko="라운지웨어·파자마 부자재 가이드: 플리스, 세트 비율, 선물 포장",
        h1_fr="Guide des accessoires de vêtements d'intérieur : polaire, ratios, coffrets",
        h1_es="Guía de accesorios para ropa de casa: polar, ratios y cajas de regalo",
        tag_zh="家居服品类", tag_en="Loungewear", tag_ja="ルームウェア", tag_ko="라운지웨어",
        tag_fr="Vêtements d'intérieur", tag_es="Ropa de casa",
        sum_zh="家居服成套卖，辅料最容易出问题的不是印刷而是配比与沾毛。本文讲清绒类面料怎么选主唛才不沾毛、套装两处尺码标与配比怎么对、洗水标按耐洗 20 次以上怎么选材质、吊牌与礼盒包装怎么设计，并给出可直接抄进询价邮件的规格表与五步验收清单。",
        sum_en="Loungewear sells as a set, and the trims that fail are rarely about printing — they are about ratios and lint. This guide covers choosing neck labels that do not attract fleece, placing and reconciling two size labels per set, specifying care labels for more than 20 washes, and designing tags and gift box packaging, with a specification table and a five-step acceptance list.",
        sum_ja="ルームウェアはセット販売が中心で、副資材のトラブルは印刷よりも比率と毛の付着に起因します。本記事はフリースに毛が付きにくい主ラベルの選び方、上下2か所のサイズラベルと比率の合わせ方、20回以上の耐洗を前提にした洗濯表示ラベルの選定、タグとギフトボックス包装の設計を解説し、仕様表と5ステップの検収リストを掲載します。",
        sum_ko="라운지웨어는 세트 판매가 중심이고 부자재 문제는 인쇄보다 비율과 보풀 부착에서 발생합니다. 이 글은 플리스에 보풀이 붙지 않는 주 라벨 선택, 상하 두 곳의 사이즈 라벨과 비율 맞추기, 20회 이상 세탁을 전제로 한 세탁 표시 라벨 소재 선정, 행택과 선물 상자 포장 설계를 설명하고 사양표와 5단계 검수 목록을 제공합니다.",
        sum_fr="Le vêtement d'intérieur se vend en ensemble, et les incidents d'accessoires tiennent rarement à l'impression : ils viennent des ratios et des fibres. Ce guide traite le choix de labels qui n'attirent pas la polaire, la pose et la réconciliation de deux labels de taille par ensemble, la spécification d'étiquettes d'entretien tenant plus de 20 lavages, ainsi que les tags et l'emballage coffret, avec un tableau de spécifications et cinq contrôles.",
        sum_es="La ropa de casa se vende como conjunto, y los fallos de accesorios rara vez son de impresión: son de ratios y de pelo adherido. Esta guía trata la elección de etiquetas que no atraigan el polar, la colocación y el cuadre de dos etiquetas de talla por conjunto, la especificación de etiquetas de cuidado para más de 20 lavados y el diseño de colgantes y caja de regalo, con tabla de especificaciones y cinco comprobaciones.",
    ),
]

skel = open(SKEL, encoding="utf-8").read()
old3 = re.search(r'"position": 3,\s*"name": "([^"]*)"', skel).group(1)
print("骨架 breadcrumb 名:", old3)

# ---------------- 撞车安全闸 ----------------
for a in ARTICLES:
    for p in [a["body"]]:
        if not os.path.exists(p):
            raise SystemExit("正文文件缺失：%s" % p)
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
    print("  %-34s desc_zh=%d字 desc_en=%d字符 desc_ja=%d desc_ko=%d desc_fr=%d desc_es=%d"
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
