#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-09-24 下午 每日更新：2 篇新文章（六语：zh-Hant 根 / en / ja / ko / fr / es）
- 服装包装运输测试指南：跌落、堆码、振动与温湿怎么验
- 衬衫与女衫辅料指南：领标、尺码标与包装板怎么定
（主题池 30 个选题均已上线，本次为品类扩展新选题，不与既有文章重复）

用法: python daily_gen_20260924_pm.py
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
BUST_OLD, BUST_NEW = "105", "106"
LANGS = ["en", "ja", "ko", "fr", "es"]

ARTICLES = [
    dict(
        slug="garment-packaging-transit-testing.html",
        body="blog/_body_transit.html",
        title_zh="服装包装运输测试指南：跌落、堆码、振动与温湿 | TAGE",
        title_en="Apparel Packaging Transit Testing: Drop, Stacking, Vibration and Humidity | TAGE",
        title_ja="衣料包装の輸送テストガイド：落下・積み重ね・振動・温湿度 | TAGE",
        title_ko="의류 포장 운송 테스트 가이드: 낙하·적재·진동·온습도 | TAGE",
        title_fr="Tests de transport d'emballage : chute, empilage, vibration et humidité | TAGE",
        title_es="Pruebas de transporte de embalaje: caída, apilado, vibración y humedad | TAGE",
        desc_zh="服装包装运输测试指南：讲清跌落、堆码、振动、温湿四类测试怎么为服装包装设定参数，袋口爆开、纸袋提手脱落、外箱塌陷、吊牌磨花与霉变五种破损模式的对策，以及不用实验室的五步自测和出运前核对清单。来自东莞泰阁包装。",
        desc_en="Apparel packaging transit testing: set drop, stacking, vibration and humidity parameters, fix five common packaging failures, and run a five-step in-house test.",
        desc_ja="衣料包装の輸送テストガイド。落下・積み重ね・振動・温湿度のパラメータ設定、封口破れや紙袋の手提げ外れなど五つの破損パターンと対策、実験室なしでできる5ステップの自主テスト、出荷前チェックを解説します。東莞泰閣包装。",
        desc_ko="의류 포장 운송 테스트 가이드. 낙하·적재·진동·온습도 파라미터 설정, 봉합부 터짐·종이백 손잡이 탈락 등 다섯 가지 파손 유형과 대책, 실험실 없이 하는 5단계 자체 테스트, 출하 전 체크를 정리했습니다. 둥관 TAGE 패키징.",
        desc_fr="Tests de transport d'emballage : régler chute, empilage, vibration et humidité, corriger cinq avaries fréquentes et réaliser un autotest en cinq étapes.",
        desc_es="Pruebas de transporte del embalaje: fijar caída, apilado, vibración y humedad, corregir cinco fallos frecuentes y hacer un autotest de cinco pasos.",
        crumb_zh="包装运输测试", crumb_en="Transit Testing", crumb_ja="輸送テスト",
        crumb_ko="운송 테스트", crumb_fr="Tests de transport", crumb_es="Pruebas de transporte",
        h1_zh="服装包装运输测试指南：跌落、堆码、振动与温湿怎么验",
        h1_en="Apparel Packaging Transit Testing: Drop, Stacking, Vibration and Humidity",
        h1_ja="衣料包装の輸送テストガイド：落下・積み重ね・振動・温湿度の検証方法",
        h1_ko="의류 포장 운송 테스트 가이드: 낙하·적재·진동·온습도 검증 방법",
        h1_fr="Tests de transport d'emballage : chute, empilage, vibration et humidité",
        h1_es="Pruebas de transporte de embalaje: caída, apilado, vibración y humedad",
        tag_zh="包装测试", tag_en="Packaging Testing", tag_ja="包装試験", tag_ko="포장 시험",
        tag_fr="Test d'emballage", tag_es="Prueba de embalaje",
        sum_zh="同一条国际线路、同一件衣服，包装形式不同，破损率可以差好几倍。本文讲清跌落、堆码、振动、温湿四类运输测试在服装包装上怎么设参数，袋口爆开、纸袋提手脱落、外箱塌陷、吊牌磨花与潮湿霉变五种破损模式的对策，以及不用实验室就能做的五步自测与出运前核对清单。",
        sum_en="On the same lane and the same garment, packaging format can change the damage rate several times over. This guide shows how to set parameters for drop, stacking, vibration and climate tests on apparel packaging, how to fix five common failures — burst seals, torn bag handles, collapsing cartons, scuffed tags and mould — and adds a five-step in-house test plus a pre-shipment checklist.",
        sum_ja="同じ国際ルート、同じ製品でも、包装形態が違えば破損率は数倍変わります。本記事は、落下・積み重ね・振動・温湿度の四つの輸送テストを衣料包装でどう設計するか、封口破れ・紙袋手提げ外れ・外箱つぶれ・タグの擦り傷・カビという五つの破損パターンと対策、実験室なしでできる5ステップの自主テスト、出荷前チェックリストをまとめます。",
        sum_ko="같은 국제 노선, 같은 제품이라도 포장 형태에 따라 파손률은 몇 배까지 차이 납니다. 이 글은 낙하·적재·진동·온습도 네 가지 운송 테스트를 의류 포장에 어떻게 설계할지, 봉합부 터짐·종이백 손잡이 탈락·외박스 눌림·행택 스크래치·곰팡이 다섯 가지 파손 유형과 대책, 실험실 없이 하는 5단계 자체 테스트, 출하 전 체크리스트를 정리합니다.",
        sum_fr="Sur une même liaison et pour une même pièce, le format d'emballage peut multiplier le taux d'avarie. Ce guide montre comment paramétrer les tests de chute, d'empilage, de vibration et de climat sur l'emballage de vêtements, comment corriger cinq avaries fréquentes — soudures qui cèdent, poignées arrachées, cartons écrasés, étiquettes rayées, moisissures — et propose un autotest en cinq étapes avec une liste de contrôle avant expédition.",
        sum_es="En la misma ruta y con la misma prenda, el formato de embalaje puede multiplicar la tasa de daños. Esta guía explica cómo parametrizar las pruebas de caída, apilado, vibración y clima en el embalaje de prendas, cómo corregir cinco fallos frecuentes — sellos que revientan, asas arrancadas, cajas aplastadas, colgantes rozados y moho — y añade un autotest de cinco pasos con lista de comprobación previa al envío.",
    ),
    dict(
        slug="shirt-blouse-trims-guide.html",
        body="blog/_body_shirt.html",
        title_zh="衬衫与女衫辅料指南：领标、尺码标与包装板怎么定 | TAGE",
        title_en="Shirt and Blouse Trims Guide: Neck Labels, Collar Sizes and Packing Boards | TAGE",
        title_ja="シャツ・ブラウスの副資材ガイド：衿ラベル・サイズラベル・包装台紙の決め方 | TAGE",
        title_ko="셔츠·블라우스 부자재 가이드: 목 라벨, 사이즈 라벨, 포장 받침대 | TAGE",
        title_fr="Guide des accessoires de chemise : label de col, taille de col et carton de pliage | TAGE",
        title_es="Guía de accesorios para camisa: etiqueta de cuello, talla de cuello y cartón de plegado | TAGE",
        desc_zh="衬衫与女衫辅料指南：讲清主唛与领围尺码标的尺寸、位置与写法，洗水标在机洗与免熨整理下怎么写，吊牌与吊粒的轻量化选择，包装板、领撑与折法，并附可直接抄进询价邮件的规格确认表与五步打样验收方法。来自东莞泰阁包装。",
        desc_en="Shirt trims guide: neck and collar-size labels, care labels for machine wash and wrinkle-free finishes, light hang tags, packing boards and a spec sheet.",
        desc_ja="シャツ・ブラウスの副資材ガイド。衿ラベルと衿囲サイズラベルの寸法・位置・表記、洗濯と形態安定加工に合う洗濯表示、タグとタグ止めの軽量化、包装台紙と衿芯、見積りに使える仕様確認表と5ステップ検収を解説します。東莞泰閣包装。",
        desc_ko="셔츠·블라우스 부자재 가이드. 목 라벨과 목둘레 사이즈 라벨의 치수·위치·표기, 세탁과 노아이언 가공에 맞는 세탁 표시, 행택과 고정구의 경량화, 포장 받침대와 깃 지지, 견적용 사양표와 5단계 검수를 정리했습니다. 둥관 TAGE 패키징.",
        desc_fr="Accessoires de chemise : label de col et de taille, étiquette d'entretien pour machine et finition sans repassage, étiquettes légères, cartons de pliage et fiche de spécifications.",
        desc_es="Accesorios para camisa: etiqueta de cuello y de talla, etiqueta de cuidado para lavado a máquina y acabado sin plancha, colgantes ligeros y cartones de plegado.",
        crumb_zh="衬衫辅料指南", crumb_en="Shirt Trims", crumb_ja="シャツ副資材",
        crumb_ko="셔츠 부자재", crumb_fr="Accessoires chemise", crumb_es="Accesorios camisa",
        h1_zh="衬衫与女衫辅料指南：领标、尺码标与包装板怎么定",
        h1_en="Shirt and Blouse Trims Guide: Neck Labels, Collar Sizes and Packing Boards",
        h1_ja="シャツ・ブラウスの副資材ガイド：衿ラベル・サイズラベル・包装台紙の決め方",
        h1_ko="셔츠·블라우스 부자재 가이드: 목 라벨, 사이즈 라벨, 포장 받침대 정하는 법",
        h1_fr="Guide des accessoires de chemise : label de col, taille de col et carton de pliage",
        h1_es="Guía de accesorios para camisa: etiqueta de cuello, talla de cuello y cartón de plegado",
        tag_zh="品类指南", tag_en="Category Guide", tag_ja="カテゴリガイド", tag_ko="카테고리 가이드",
        tag_fr="Guide catégorie", tag_es="Guía de categoría",
        sum_zh="衬衫是最考验辅料细节的品类：领标厚一点就鼓包，吊粒重一点就压痕，尺码标还要承载领围体系。本文讲清主唛与领围尺码标的尺寸、位置与写法，洗水标在机洗与免熨整理下怎么写，吊牌与吊粒的轻量化选择，包装板、领撑与折法，并附可直接询价的规格确认表与五步打样验收。",
        sum_en="Shirts are the most trim-sensitive category: a label a fraction too thick bulges, a fastener a few grams too heavy leaves a mark, and the size label must carry a collar-size system. This guide covers neck and collar-size labels in detail, care wording for machine wash and wrinkle-free finishes, light hang tags, packing boards, collar stays and folding, with a spec sheet and a five-step sample approval.",
        sum_ja="シャツは副資材の細部が最も問われる品種です。ラベルが少し厚いだけで膨らみ、タグ止めが少し重いだけで圧痕が残り、サイズラベルは衿囲体系を載せる必要があります。本記事は衿ラベルと衿囲サイズラベルの寸法・位置・表記、洗濯と形態安定加工に合う洗濯表示、タグと止め具の軽量化、包装台紙・衿芯・畳み方を解説し、仕様確認表と5ステップのサンプル検収を掲載します。",
        sum_ko="셔츠는 부자재 디테일이 가장 중요한 품목입니다. 라벨이 조금만 두꺼워도 부풀고, 고정구가 조금만 무거워도 압흔이 남으며, 사이즈 라벨은 목둘레 체계를 담아야 합니다. 이 글은 목 라벨과 목둘레 사이즈 라벨의 치수·위치·표기, 세탁과 노아이언 가공에 맞는 세탁 표시, 행택과 고정구의 경량화, 포장 받침대·깃 지지·접기 방식을 다루고 사양 확인표와 5단계 승인 절차를 제공합니다.",
        sum_fr="La chemise est la catégorie la plus exigeante en détail : un label un peu épais gonfle, une attache un peu lourde marque, et le label de taille doit porter un système de col. Ce guide détaille labels de col et de taille, texte d'entretien pour machine et finition sans repassage, étiquettes légères, cartons de pliage, baleines et pliage, avec fiche de spécifications et validation d'échantillon en cinq étapes.",
        sum_es="La camisa es la categoría más exigente en detalle: una etiqueta algo gruesa abomba, un cierre algo pesado marca, y la etiqueta de talla debe soportar un sistema de cuello. Esta guía detalla etiqueta de cuello y de talla, texto de cuidado para lavado a máquina y acabado sin plancha, colgantes ligeros, cartones de plegado, ballenas y plegado, con ficha de especificaciones y aprobación de muestra en cinco pasos.",
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
    print("  %-38s desc_zh=%d字 desc_en=%d字符 desc_ja=%d desc_ko=%d desc_fr=%d desc_es=%d"
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
