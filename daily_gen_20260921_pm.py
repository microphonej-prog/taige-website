#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-09-21 下午 每日更新：2 篇新文章（六语：zh-Hant 根 / en / ja / ko / fr / es）
- 吊牌金属配件指南（鸡眼/金属吊粒/珠链/别针）
- 服装辅料检针（金属检测）指南
+ 列表页卡片 + gen_i18n 五语生成 + sitemap + BUST_VERSION 升级 + 繁体转换。

用法: python daily_gen_20260921_pm.py
"""
import os, re, sys, subprocess, importlib.util

ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)
PY = sys.executable

SKEL = "blog/knitwear-sweater-trims-guide.html"
DATE_ZH = "2026年9月21日"
DATE_EN = "September 21, 2026"
DATE_JA = "2026年9月21日更新"
DATE_KO = "2026년 9월 21일 업데이트"
DATE_FR = "21 septembre 2026"
DATE_ES = "21 de septiembre de 2026"
SITEMAP_DATE = "2026-09-21"
BUST_OLD, BUST_NEW = "96", "97"
LANGS = ["en", "ja", "ko", "fr", "es"]

ARTICLES = [
    dict(
        slug="hang-tag-metal-hardware-guide.html",
        body="blog/_body_hang_tag_metal_hardware.html",
        title_zh="吊牌金属配件指南：鸡眼、金属吊粒与别针怎么选 | TAGE",
        title_en="Hang Tag Metal Hardware Guide: Eyelets, Fasteners &amp; Pins | TAGE",
        title_ja="タグの金属パーツガイド：ハトメ・金属留め具・ピンの選び方 | TAGE",
        title_ko="행택 금속 부품 가이드: 아일릿, 체결구, 핀 선택법 | TAGE",
        title_fr="Quincaillerie d'étiquette : œillets, attaches et épingles | TAGE",
        title_es="Herrajes para etiquetas: ojales, cierres y alfileres | TAGE",
        desc_zh="吊牌金属配件指南：鸡眼（气眼）的内径、材质与电镀怎么选，金属吊粒、珠链与夹扣的装配差异，安全别针与防盗件，镍释放、铅含量与盐雾测试等合规要求，附可直接抄进询价邮件的配件规格对照表与打样验收五步。来自东莞泰阁包装。",
        desc_en="Hang tag metal hardware guide: eyelet bore, material and plating, metal fasteners, ball chains and pins, load notes, nickel release and salt spray tests.",
        desc_ja="タグの金属パーツガイド。ハトメの内径・材質・メッキの選び方、金属留め具・チェーン・クリップの取付、ピンと防盗パーツ、ニッケル溶出・鉛・塩水噴霧の適合要件、見積りに使える仕様表と検収5ステップを解説します。東莞泰閣包装。",
        desc_ko="행택 금속 부품 가이드: 아일릿 내경·소재·도금 선택, 금속 체결구·체인·클립 장착, 핀과 보안 부품, 니켈 용출·납·염수 분무 요건, 견적용 사양표와 검수 5단계를 정리했습니다. 둥관 TAGE 패키징.",
        desc_fr="Guide de la quincaillerie d'étiquette : diamètre, matière et placage des œillets, attaches et chaînettes, épingles, charges, nickel, brouillard salin et fiche de spécifications.",
        desc_es="Guía de herrajes para etiquetas: diámetro, material y baño de los ojales, cierres y cadenas, alfileres, cargas, níquel, niebla salina y ficha de especificaciones.",
        crumb_zh="吊牌金属配件指南", crumb_en="Hang Tag Hardware", crumb_ja="タグの金属パーツ",
        crumb_ko="행택 금속 부품", crumb_fr="Quincaillerie d'étiquette", crumb_es="Herrajes de etiqueta",
        h1_zh="吊牌金属配件指南：鸡眼、金属吊粒与别针怎么选",
        h1_en="Hang Tag Metal Hardware: Eyelets, Metal Fasteners and Pins",
        h1_ja="タグの金属パーツガイド：ハトメ・金属留め具・ピンの選び方",
        h1_ko="행택 금속 부품 가이드: 아일릿, 금속 체결구, 핀 선택법",
        h1_fr="Quincaillerie d'étiquette : choisir œillets, attaches et épingles",
        h1_es="Herrajes para etiquetas: elegir ojales, cierres y alfileres",
        tag_zh="吊牌指南", tag_en="Hang Tag Guide", tag_ja="タグガイド", tag_ko="행택 가이드",
        tag_fr="Guide étiquettes", tag_es="Guía de etiquetas",
        sum_zh="金属配件是吊牌上唯一承力的部位：纸张和印刷决定好不好看，配件决定挂不挂得住。本文按鸡眼（气眼）的内径、材质与电镀选择，金属吊粒、珠链与夹扣的装配差异，别针与防盗件，镍释放、铅含量与盐雾测试要求，以及打样验收五步展开，并给出一张可直接抄进询价邮件的配件规格对照表。",
        sum_en="Metal hardware is the only load-bearing part of a hang tag: paper and print make it look good, hardware makes it stay on the rail. This guide covers eyelet bore, material and plating, metal fasteners and ball chains, pins and security parts, nickel release, lead and salt spray, five sampling checks and a selection table to copy into your enquiry.",
        sum_ja="金属パーツはタグの中で唯一荷重を受ける部分です。紙と印刷は見た目を、金具は掛けられるかどうかを決めます。本記事はハトメの内径・材質・メッキ、金属留め具・ボールチェーン・クリップの取付、ピンと防盗パーツ、ニッケル溶出・鉛・塩水噴霧の要件、検収5ステップを整理し、見積りにそのまま使える選定比較表を添えます。",
        sum_ko="금속 부품은 행택에서 유일하게 하중을 받는 부분입니다. 종이와 인쇄는 외관을, 부품은 걸 수 있는지를 결정합니다. 이 글은 아일릿 내경·소재·도금, 금속 체결구·볼체인·클립 장착, 핀과 보안 부품, 니켈 용출·납·염수 분무 요건, 검수 5단계를 정리하고 견적에 바로 쓸 수 있는 선정 비교표를 제공합니다.",
        sum_fr="La quincaillerie est la seule partie portante d'une étiquette : le papier et l'impression font l'aspect, la quincaillerie décide de la tenue. Ce guide couvre diamètre, matière et placage de l'œillet, attaches, chaînettes et pinces, épingles et sécurité, nickel, plomb, brouillard salin, cinq contrôles d'échantillon et un tableau de sélection à copier dans votre demande.",
        sum_es="El herraje es la única parte que soporta carga en una etiqueta: el papel y la impresión dan el aspecto, el herraje decide si aguanta. Esta guía cubre diámetro, material y baño del ojal, cierres, cadenas y pinzas, alfileres y seguridad, níquel, plomo, niebla salina, cinco controles de muestra y una tabla de selección para tu consulta.",
    ),
    dict(
        slug="garment-trims-needle-detection-guide.html",
        body="blog/_body_garment_trims_needle_detection.html",
        title_zh="服装辅料检针指南：哪些辅件会被检出、怎么避免停机 | TAGE",
        title_en="Needle Detection for Garment Trims: Metal Parts and Alternatives | TAGE",
        title_ja="衣料副資材の検針ガイド：検出される部材とライン停止の防ぎ方 | TAGE",
        title_ko="의류 부자재 검침 가이드: 검출되는 부품과 라인 정지 방지 | TAGE",
        title_fr="Détection métallique des accessoires : pièces détectées et alternatives | TAGE",
        title_es="Detección metálica en accesorios: piezas detectadas y alternativas | TAGE",
        desc_zh="服装辅料检针指南：磁感应检针机与平衡线圈式金属检测机分别检出什么，铁质鸡眼、金属吊粒、钢制别针、烫金吊牌、金银线织唛等七类辅料的实际表现，必须保留金属件时的分段检测与灵敏度分档办法，检针标签与记录要求，附询价确认清单。来自东莞泰阁包装。",
        desc_en="Needle detection for garment trims: what magnetic and coil detectors catch, how seven common trims behave, split-stage detection and sensitivity grading.",
        desc_ja="衣料副資材の検針ガイド。磁気式とコイル式が検出するもの、鉄ハトメ・金属留め具・箔押しタグ・金属糸ラベルなど7種類の反応、金属を残す場合の分割検針と感度設定、検針シールと記録、見積り確認チェックリストを解説します。東莞泰閣包装。",
        desc_ko="의류 부자재 검침 가이드: 자기식과 코일식 검출기의 차이, 철 아일릿·금속 체결구·박 인쇄 행택·금속사 라벨 등 7종의 반응, 금속을 유지할 때의 분할 검침과 감도 설정, 검침 라벨과 기록, 견적 확인 체크리스트를 정리했습니다. 둥관 TAGE 패키징.",
        desc_fr="Détection métallique des accessoires : ce que captent les détecteurs magnétiques et à bobines, la réaction de sept accessoires, le contrôle par étapes, la sensibilité, les étiquettes et une liste de vérification.",
        desc_es="Detección metálica en accesorios: qué captan los detectores magnéticos y de bobinas, la reacción de siete accesorios, control por etapas, sensibilidad, etiquetas y lista de verificación.",
        crumb_zh="服装辅料检针指南", crumb_en="Needle Detection", crumb_ja="副資材の検針",
        crumb_ko="부자재 검침", crumb_fr="Détection métallique", crumb_es="Detección metálica",
        h1_zh="服装辅料检针指南：哪些辅件会被检出，怎么避免停机",
        h1_en="Needle Detection for Garment Trims: Which Parts Get Flagged and How to Avoid Stoppages",
        h1_ja="衣料副資材の検針ガイド：検出される部材とライン停止の防ぎ方",
        h1_ko="의류 부자재 검침 가이드: 검출되는 부품과 라인 정지 방지",
        h1_fr="Détection métallique des accessoires : quelles pièces sont détectées et comment éviter les arrêts",
        h1_es="Detección metálica en accesorios: qué piezas se detectan y cómo evitar paradas",
        tag_zh="合規指南", tag_en="Compliance", tag_ja="コンプライアンス", tag_ko="컴플라이언스",
        tag_fr="Conformité", tag_es="Cumplimiento",
        sum_zh="客户要求整批过检针，吊牌上却装了铁质鸡眼、金属吊粒或钢制别针，验针机一直报警，货卡在包装线——这类停机几乎都不是设备问题。本文讲清两类检针设备各自检出什么、七类常见辅料在设备前的表现、必须保留金属件时的分段检测与灵敏度分档办法、检针标签与记录要求，并给出询价确认清单。",
        sum_en="The buyer wants the whole shipment detected, but the tags carry iron eyelets, metal fasteners or steel pins and the machine keeps alarming — almost never a machine fault. This guide explains what magnetic and coil detectors catch, how seven common trims behave, split-stage detection and sensitivity grading when metal must stay, detection labels and records, plus an enquiry checklist.",
        sum_ja="全数検針を求められているのに、タグに鉄ハトメ・金属留め具・スチールピンが付いていて検針機が鳴り続ける。これはほぼ設備の問題ではありません。本記事は磁気式とコイル式が何を検出するか、よく使う7種類の副資材の反応、金属を残す場合の分割検針と感度設定、検針シールと記録の要件、見積り確認チェックリストを解説します。",
        sum_ko="전량 검침을 요구받았는데 행택에 철 아일릿, 금속 체결구, 스틸 핀이 달려 검침기가 계속 울립니다. 이는 거의 장비 문제가 아닙니다. 이 글은 자기식과 코일식이 무엇을 검출하는지, 흔한 부자재 7종의 반응, 금속을 유지할 때의 분할 검침과 감도 설정, 검침 라벨과 기록 요건, 견적 확인 체크리스트를 정리합니다.",
        sum_fr="L'acheteur exige un contrôle sur tout le lot, mais les étiquettes portent des œillets en fer, des attaches métalliques ou des épingles en acier et la machine sonne : rarement une panne. Ce guide explique ce que captent les détecteurs magnétiques et à bobines, la réaction de sept accessoires, la détection par étapes, le réglage de sensibilité, les étiquettes et registres, et une liste de vérification.",
        sum_es="El cliente exige detección en todo el lote, pero las etiquetas llevan ojales de hierro, cierres metálicos o alfileres de acero y la máquina no deja de avisar: casi nunca es la máquina. Esta guía explica qué captan los detectores magnéticos y de bobinas, la reacción de siete accesorios, la detección por etapas, el ajuste de sensibilidad, las etiquetas y registros, y una lista de verificación.",
    ),
]

skel = open(SKEL, encoding="utf-8").read()
old3 = re.search(r'"position": 3,\s*"name": "([^"]*)"', skel).group(1)
print("骨架 breadcrumb 名:", old3)

# ---------------- 撞车安全闸 ----------------
sm0 = open("sitemap.xml", encoding="utf-8").read()
for a in ARTICLES:
    for p in ["blog/%s" % a["slug"]] + ["%s/blog/%s" % (l, a["slug"]) for l in LANGS]:
        if os.path.exists(p):
            raise SystemExit("选题撞车：%s 已存在，换选题！" % p)
    if ("/blog/%s</loc>" % a["slug"]) in sm0:
        raise SystemExit("选题撞车：sitemap 已含 %s" % a["slug"])
print("选题全新，开始生成")

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
    s, n = re.subn(r'<p data-zh="泰閣包裝 · 更新於[^"]*".*?</p>', meta, s, count=1, flags=re.S)
    if n != 1:  # 简体骨架兜底
        s, n = re.subn(r'<p data-zh="泰阁包装 · 更新于[^"]*".*?</p>', meta, s, count=1, flags=re.S)
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
    print("写入 %s (%d KB) desc_zh=%d字 desc_en=%d字符 desc_fr=%d desc_es=%d"
          % (out, len(s.encode("utf-8")) // 1024, len(a["desc_zh"]), len(a["desc_en"]),
             len(a["desc_fr"]), len(a["desc_es"])))

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
