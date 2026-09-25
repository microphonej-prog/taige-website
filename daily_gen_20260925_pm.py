#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-09-25 下午 每日更新：2 篇新文章（六语：zh-Hant 根 / en / ja / ko / fr / es）
- 鞋类与箱包辅料标签指南：鞋标、织唛与吊牌怎么配（新品类角度：鞋类/箱包，主题池 30 个选题均已上线）
- 吊牌与辅料印刷的版权与商标授权指南：logo、字体与图案怎么印
用法: <python> daily_gen_20260925_pm.py
"""
import os, re, sys, subprocess, importlib.util

ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)
PY = sys.executable

SKEL = "blog/knitwear-sweater-trims-guide.html"
DATE_ZH = "2026年9月25日"
DATE_EN = "September 25, 2026"
DATE_JA = "2026年9月25日更新"
DATE_KO = "2026년 9월 25일 업데이트"
DATE_FR = "25 septembre 2026"
DATE_ES = "25 de septiembre de 2026"
SITEMAP_DATE = "2026-09-25"
BUST_OLD, BUST_NEW = "108", "109"
LANGS = ["en", "ja", "ko", "fr", "es"]

ARTICLES = [
    dict(
        slug="footwear-luggage-trims-guide.html",
        body="blog/_body_footwear.html",
        title_zh="鞋类与箱包辅料标签指南：鞋标、织唛与吊牌怎么配 | TAGE",
        title_en="Footwear &amp; Bag Trim Labels: Shoe Labels, Woven Tags and Hang Tags | TAGE",
        title_ja="靴・バッグ副資材ラベルガイド：靴ラベル・織りラベル・タグの組み合わせ | TAGE",
        title_ko="신발·가방 부자재 라벨 가이드: 슈즈 라벨, 직조 라벨, 행택 구성 | TAGE",
        title_fr="Guide des accessoires pour chaussures et sacs : étiquettes, tissés et étiquettes suspendues | TAGE",
        title_es="Guía de accesorios para calzado y bolsos: etiquetas, tejidas y colgantes | TAGE",
        desc_zh="鞋类与箱包辅料标签指南：欧盟 94/11/EC 要求标注鞋面、衬里与内垫、外底四个部位的材质，本文讲清鞋舌织唛、鞋垫标、皮标与鞋盒贴标的选型与工艺，附材质工艺对照表与打样验收清单。来自东莞泰阁包装。",
        desc_en="Custom footwear and bag trim labels: EU 94/11/EC material marking for upper, lining and sole, tongue woven labels, insole marks, leather patches and box labels.",
        desc_ja="靴・バッグの副資材ラベルガイド。EU指令94/11/ECの素材表示（アッパー・ライニング・ソール）、タン・中敷き・レザーパッチ・靴箱ラベルの選定と加工、素材対照表とサンプル検収チェックリストを解説します。東莞泰閣包装。",
        desc_ko="신발·가방 부자재 라벨 가이드. EU 지침 94/11/EC 소재 표시(갑피·안감·창), 텅·인솔·가죽 패치·상자 라벨 선택과 공정, 소재 대조표와 샘플 검수 체크리스트를 정리했습니다. 둥관 TAGE 패키징.",
        desc_fr="Étiquettes pour chaussures et sacs : marquage des matières selon la directive 94/11/EC, tissés de languette, premières, patchs cuir et étiquettes de boîte.",
        desc_es="Etiquetas para calzado y bolsos: marcado de materiales (Directiva 94/11/EC), tejidas de lengüeta, plantillas, parches de piel y etiquetas de caja.",
        crumb_zh="鞋类与箱包辅料", crumb_en="Footwear &amp; Bag Trims", crumb_ja="靴・バッグ副資材",
        crumb_ko="신발·가방 부자재", crumb_fr="Chaussures et sacs", crumb_es="Calzado y bolsos",
        h1_zh="鞋类与箱包辅料标签指南：鞋标、织唛与吊牌怎么配",
        h1_en="Footwear &amp; Bag Trim Labels: Shoe Labels, Woven Tags and Hang Tags",
        h1_ja="靴・バッグ副資材ラベルガイド：靴ラベル・織りラベル・タグの組み合わせ",
        h1_ko="신발·가방 부자재 라벨 가이드: 슈즈 라벨, 직조 라벨, 행택 구성",
        h1_fr="Guide des accessoires pour chaussures et sacs : étiquettes, tissés et étiquettes suspendues",
        h1_es="Guía de accesorios para calzado y bolsos: etiquetas, tejidas y colgantes",
        tag_zh="品类指南", tag_en="Category Guide", tag_ja="カテゴリガイド", tag_ko="카테고리 가이드",
        tag_fr="Guide par produit", tag_es="Guía por producto",
        sum_zh="鞋类的辅料比服装更苛刻：要弯折、要摩擦、要遇汗渍与雨水。本文把鞋类与箱包标签分成法规层（材质、产地、尺码）、品牌层（鞋舌织唛、鞋垫标、皮标）与零售层（吊牌、鞋盒贴标）三层，讲清欧盟 94/11/EC 的四个部位材质标注、五种常用工艺的耐久要点，以及一份打样验收清单。",
        sum_en="Footwear trims face harsher conditions than apparel: flexing, rubbing, sweat and rain. This guide splits footwear and bag labelling into a regulatory layer (material, origin, size), a brand layer (tongue woven labels, insole marks, leather patches) and a retail layer (hang tags, box labels), covering the four material parts under EU 94/11/EC and durability points for five common processes.",
        sum_ja="靴の副資材は衣料より過酷な条件に耐える必要があります。本記事は靴とバッグの表示を、法規層（素材・原産地・サイズ）、ブランド層（タンの織りラベル・中敷きマーク・レザーパッチ）、小売層（タグ・靴箱ラベル）の3層に分け、EU指令94/11/ECの4部位の素材表示と5つの加工の耐久ポイント、サンプル検収チェックリストを解説します。",
        sum_ko="신발 부자재는 의류보다 가혹한 조건을 견뎌야 합니다. 이 글은 신발과 가방 표시를 법규 층(소재·원산지·사이즈), 브랜드 층(텅 직조 라벨·인솔 마크·가죽 패치), 소매 층(행택·상자 라벨)으로 나누고, EU 지침 94/11/EC의 네 부위 소재 표시와 다섯 가지 공정의 내구 포인트, 샘플 검수 체크리스트를 정리합니다.",
        sum_fr="Les accessoires de chaussure subissent plus que ceux du vêtement : pliage, frottement, sueur et pluie. Ce guide sépare le marquage en trois niveaux — réglementaire (matière, origine, taille), marque (tissés de languette, premières, patchs cuir) et vente (étiquettes suspendues, boîtes) — et détaille les quatre parties de la directive 94/11/EC.",
        sum_es="Los accesorios de calzado sufren más que los de ropa: doblado, roce, sudor y lluvia. Esta guía separa el marcado en tres niveles — normativo (material, origen, talla), de marca (tejidas de lengüeta, plantillas, parches de piel) y de venta (colgantes, cajas) — y detalla las cuatro partes de la Directiva 94/11/EC.",
    ),
    dict(
        slug="trim-artwork-copyright-guide.html",
        body="blog/_body_ip.html",
        title_zh="吊牌与辅料印刷的版权与商标授权指南：logo、字体、图案怎么印 | TAGE",
        title_en="Copyright and Trademark Clearance for Hang Tags and Trims | TAGE",
        title_ja="タグ・副資材印刷の著作権と商標ガイド：ロゴ・フォント・図案をどう印刷するか | TAGE",
        title_ko="행택·부자재 인쇄의 저작권과 상표 가이드: 로고·폰트·도안 인쇄 조건 | TAGE",
        title_fr="Droits d'auteur et marques pour l'impression d'étiquettes et d'accessoires | TAGE",
        title_es="Derechos de autor y marcas para imprimir etiquetas y accesorios | TAGE",
        desc_zh="吊牌与辅料印刷的版权与商标授权指南：自有商标、客户代工图案与第三方授权 IP 各需要什么文件，字体商用授权与图库扩展授权的边界，AI 生成图的版权现状，以及侵权后平台下架、海关扣货的现实后果，附打样前授权核对清单。来自东莞泰阁包装。",
        desc_en="Copyright and trademark clearance for trims: documents needed by own brands, contract manufacturing and licensed IP, font and image licences and a checklist.",
        desc_ja="タグ・副資材印刷の著作権と商標ガイド。自社商標・受託生産・第三者ライセンスIPに必要な書類、フォントと素材サイトのライセンス範囲、AI生成物、侵害時の影響とサンプル前チェックリストを解説します。東莞泰閣包装。",
        desc_ko="행택·부자재 인쇄의 저작권과 상표 가이드. 자사 상표·OEM·제3자 라이선스 IP에 필요한 서류, 폰트·스톡 이미지 라이선스 범위, AI 생성물, 침해 시 영향과 샘플 전 체크리스트를 정리했습니다. 둥관 TAGE 패키징.",
        desc_fr="Droits d'auteur et marques pour l'impression d'accessoires : documents exigés par situation, licences de polices, images IA et contrôle avant échantillon.",
        desc_es="Derechos de autor y marcas al imprimir accesorios: documentos según cada situación, licencias de fuentes, imágenes IA y control previo a la muestra.",
        crumb_zh="版权与商标授权", crumb_en="Copyright &amp; Trademarks", crumb_ja="著作権と商標",
        crumb_ko="저작권과 상표", crumb_fr="Droits et marques", crumb_es="Derechos y marcas",
        h1_zh="吊牌与辅料印刷的版权与商标授权指南：logo、字体、图案怎么印",
        h1_en="Copyright and Trademark Clearance for Hang Tags and Trims",
        h1_ja="タグ・副資材印刷の著作権と商標ガイド：ロゴ・フォント・図案をどう印刷するか",
        h1_ko="행택·부자재 인쇄의 저작권과 상표 가이드: 로고·폰트·도안 인쇄 조건",
        h1_fr="Droits d'auteur et marques pour l'impression d'étiquettes et d'accessoires",
        h1_es="Derechos de autor y marcas para imprimir etiquetas y accesorios",
        tag_zh="合规指南", tag_en="Compliance Guide", tag_ja="適合ガイド", tag_ko="컴플라이언스 가이드",
        tag_fr="Guide conformité", tag_es="Guía de conformidad",
        sum_zh="印厂在法律上属于复制与发行的一方，所以正规工厂开工前一定会问：这个图案你有授权吗。本文把授权场景分成自有商标、代工贴牌与第三方授权 IP 三类，讲清字体商用授权与图库扩展授权的边界、AI 生成图的版权现状、侵权后平台下架与海关扣货的现实后果，并给出打样前可以直接照抄的核对清单。",
        sum_en="A printer is, in law, the party that reproduces and distributes, which is why serious factories ask about rights before running a job. This guide splits licensing into own trademark, contract manufacturing and licensed IP, explains font and stock-image licence limits, the uncertain status of AI-generated art, and what infringement really costs.",
        sum_ja="印刷会社は法的に複製・頒布の当事者であるため、きちんとした工場は着手前に権利確認を行います。本記事は自社商標・受託生産・第三者ライセンスIPの3場面に分け、フォントと素材サイトのライセンス範囲、AI生成物の著作権の現状、侵害時の影響、サンプル前のチェックリストをまとめます。",
        sum_ko="인쇄사는 법적으로 복제·배포의 당사자이므로 제대로 된 공장은 작업 전에 권리를 확인합니다. 이 글은 자사 상표·OEM·제3자 라이선스 IP의 세 상황으로 나누고, 폰트와 스톡 이미지 라이선스 범위, AI 생성물의 저작권 현황, 침해 시 영향, 샘플 전 체크리스트를 정리합니다.",
        sum_fr="L'imprimeur est, en droit, la partie qui reproduit et diffuse : tout atelier sérieux vérifie donc les droits avant de lancer. Ce guide distingue marque propre, fabrication pour compte et PI sous licence, précise les limites des licences de polices et d'images, et le coût réel d'une contrefaçon.",
        sum_es="El impresor es, en derecho, la parte que reproduce y distribuye, y por eso todo taller serio comprueba los derechos antes de arrancar. Esta guía distingue marca propia, fabricación para terceros y PI con licencia, aclara los límites de fuentes e imágenes y el coste real de una infracción.",
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
    print("  %-40s desc_zh=%d字 desc_en=%d字符 desc_ja=%d desc_ko=%d desc_fr=%d desc_es=%d"
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
