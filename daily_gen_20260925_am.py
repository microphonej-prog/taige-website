#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-09-25 早间 每日更新：2 篇新文章（六语：zh-Hant 根 / en / ja / ko / fr / es）
- 不织布袋与帆布袋定制：服装品牌购物袋的材质、克重、尺寸与印刷
- 吊牌与标签上的认证标志与环保声明：谁授权、怎么印才合规
（主题池 30 个选题均已上线 + 品类扩展已多批，本次为新的品类/合规角度选题，不与既有文章重复）

用法: python daily_gen_20260925_am.py
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
BUST_OLD, BUST_NEW = "107", "108"
LANGS = ["en", "ja", "ko", "fr", "es"]

ARTICLES = [
    dict(
        slug="nonwoven-canvas-bag-guide.html",
        body="blog/_body_nonwoven.html",
        title_zh="不织布袋与帆布袋定制指南：服装品牌购物袋怎么选 | TAGE",
        title_en="Nonwoven &amp; Canvas Bag Guide: Custom Tote Bags for Clothing Brands | TAGE",
        title_ja="不織布バッグとキャンバスバッグ製作ガイド：衣料ブランドのショッパー選び | TAGE",
        title_ko="부직포·캔버스 가방 제작 가이드: 의류 브랜드 쇼퍼백 선택 | TAGE",
        title_fr="Guide des sacs non tissés et en toile : le sac shopping d'une marque de vêtements | TAGE",
        title_es="Guía de bolsas de non tejido y lona: la bolsa de compra para marcas de ropa | TAGE",
        desc_zh="不织布袋与帆布袋定制指南：四种主流材质与克重怎么选，门店、展会与电商三个场景的尺寸与结构，丝印、热转印与覆膜彩印的适用差别，环保声明与欧盟 PPWR 的合规边界，以及起订量、交期与验收六要点。来自东莞泰阁包装。",
        desc_en="Custom nonwoven and canvas bags for clothing brands: materials, grammage, sizes, print methods, EU packaging claims, MOQ, lead time and inspection.",
        desc_ja="衣料ブランド向けの不織布・キャンバスバッグ製作ガイド。主要4素材と目付の選び方、店舗・展示会・ECの3用途別サイズと構造、シルク・熱転写・ラミネートフルカラーの使い分け、環境訴求とEU PPWRの境界、最小ロット・納期・検収6項目を解説します。東莞泰閣包装。",
        desc_ko="의류 브랜드용 부직포·캔버스 가방 제작 가이드. 주요 소재 4가지와 평량 선택, 매장·전시회·이커머스 용도별 크기와 구조, 실크·열전사·라미네이트 풀컬러 구분, 환경 문구와 EU PPWR 경계, 최소 수량·납기·검수 6가지를 정리했습니다. 둥관 TAGE 패키징.",
        desc_fr="Sacs non tissés et en toile sur mesure pour marques de vêtements : matières, grammages, formats, procédés d'impression, allégations vertes et exigences PPWR.",
        desc_es="Bolsas de non tejido y lona a medida para marcas de ropa: materiales, gramajes, formatos, impresión, declaraciones verdes y requisitos PPWR.",
        crumb_zh="不织布袋定制", crumb_en="Custom Bags", crumb_ja="バッグ製作",
        crumb_ko="가방 제작", crumb_fr="Sacs personnalisés", crumb_es="Bolsas personalizadas",
        h1_zh="不织布袋与帆布袋定制指南：服装品牌购物袋怎么选",
        h1_en="Nonwoven and Canvas Bag Guide: Custom Tote Bags for Clothing Brands",
        h1_ja="不織布バッグとキャンバスバッグ製作ガイド：衣料ブランドのショッパー選び",
        h1_ko="부직포·캔버스 가방 제작 가이드: 의류 브랜드 쇼퍼백 선택",
        h1_fr="Guide des sacs non tissés et en toile : le sac shopping d'une marque de vêtements",
        h1_es="Guía de bolsas de non tejido y lona: la bolsa de compra para marcas de ropa",
        tag_zh="包装定制", tag_en="Custom Packaging", tag_ja="包装製作", tag_ko="포장 제작",
        tag_fr="Emballage sur mesure", tag_es="Embalaje a medida",
        sum_zh="袋子不像吊牌，拆下就被丢掉——它会被顾客留着、重复使用。本文对比不织布、棉布、帆布与 RPET 四种材质的克重与印刷适性，给出门店、展会、电商三个场景的尺寸与结构建议，讲清丝印、热转印与覆膜彩印的差别，以及环保声明与欧盟 PPWR 的边界和一份打样验收清单。",
        sum_en="A bag, unlike a hang tag, gets kept and reused. This guide compares nonwoven, cotton, canvas and RPET by grammage and printability, gives size and construction advice for store, trade show and e-commerce, explains screen print versus transfer and lamination, and covers environmental claims, EU PPWR limits and a sample approval checklist.",
        sum_ja="袋はタグと違い、捨てられず再利用されます。本記事は不織布・コットン・キャンバス・RPETの4素材を目付と印刷適性で比較し、店舗・展示会・ECの3用途別にサイズと構造を提案。シルク・熱転写・ラミネートの違い、環境訴求とEU PPWRの境界、サンプル検収チェックリストまでまとめます。",
        sum_ko="가방은 행택과 달리 버려지지 않고 재사용됩니다. 이 글은 부직포·면·캔버스·RPET 네 가지 소재를 평량과 인쇄 적성으로 비교하고, 매장·전시회·이커머스 용도별 크기와 구조를 제안하며, 실크·열전사·라미네이트 차이와 환경 문구·EU PPWR 경계, 샘플 검수 체크리스트를 정리합니다.",
        sum_fr="Un sac, contrairement à une étiquette, est conservé et réutilisé. Ce guide compare non tissé, coton, toile et RPET selon le grammage et l'impression, propose formats et structures pour boutique, salon et e-commerce, distingue sérigraphie, transfert et lamination, et couvre allégations vertes, PPWR et contrôle d'échantillon.",
        sum_es="Una bolsa, a diferencia de una etiqueta, se guarda y se reutiliza. Esta guía compara non tejido, algodón, lona y RPET por gramaje e imprimibilidad, propone medidas y estructuras para tienda, feria y e-commerce, distingue serigrafía, transferencia y laminado, y cubre declaraciones verdes, PPWR y control de muestra.",
    ),
    dict(
        slug="certification-claims-label-guide.html",
        body="blog/_body_certclaims.html",
        title_zh="吊牌认证标志与环保声明指南：OEKO-TEX、GRS、FSC 能不能印 | TAGE",
        title_en="Certification Logos and Green Claims on Hang Tags: What You May Print | TAGE",
        title_ja="タグの認証ロゴと環境訴求ガイド：OEKO-TEX・GRS・FSCは印刷できるか | TAGE",
        title_ko="행택 인증 로고와 친환경 문구 가이드: OEKO-TEX·GRS·FSC 인쇄 조건 | TAGE",
        title_fr="Logos de certification et allégations vertes sur les étiquettes : ce qui est permis | TAGE",
        title_es="Logos de certificación y declaraciones verdes en etiquetas: qué se puede imprimir | TAGE",
        desc_zh="吊牌与标签上的认证标志与环保声明指南：OEKO-TEX、GRS、FSC 标志由谁授权才能印，交易证书与授权文件怎么索要，绿色声明怎么写才经得起欧盟《绿色声明指令》、PPWR 与电商平台审核，并附上机前的六项核对清单。来自东莞泰阁包装。",
        desc_en="Certification logos and green claims on hang tags: who may print OEKO-TEX, GRS and FSC marks, which documents authorise it, and how to word claims that survive audit.",
        desc_ja="タグとラベルの認証ロゴ・環境訴求ガイド。OEKO-TEX・GRS・FSCを印刷できるのは誰か、必要な許諾書類と取引証明書の取り方、EUグリーンクレーム指令・PPWR・ECモール審査に耐える訴求文の書き方、印刷前チェックリスト6項目を解説します。東莞泰閣包装。",
        desc_ko="행택과 라벨의 인증 로고·친환경 문구 가이드. OEKO-TEX·GRS·FSC를 인쇄할 수 있는 주체, 필요한 허가 서류와 거래 인증서 확보 방법, EU 그린 클레임 지침·PPWR·이커머스 심사를 통과하는 문구 작성법, 인쇄 전 체크리스트 6가지를 정리했습니다. 둥관 TAGE 패키징.",
        desc_fr="Logos de certification et allégations vertes sur les étiquettes : qui peut imprimer OEKO-TEX, GRS et FSC, quels documents l'autorisent et comment formuler une allégation vérifiable.",
        desc_es="Logos de certificación y declaraciones verdes en etiquetas: quién puede imprimir OEKO-TEX, GRS y FSC, qué documentos lo autorizan y cómo redactar una declaración verificable.",
        crumb_zh="认证标志与声明", crumb_en="Certification Logos", crumb_ja="認証ロゴと訴求",
        crumb_ko="인증 로고와 문구", crumb_fr="Logos et allégations", crumb_es="Logos y declaraciones",
        h1_zh="吊牌认证标志与环保声明指南：OEKO-TEX、GRS、FSC 能不能印",
        h1_en="Certification Logos and Green Claims on Hang Tags: What You May Print",
        h1_ja="タグの認証ロゴと環境訴求ガイド：OEKO-TEX・GRS・FSCは印刷できるか",
        h1_ko="행택 인증 로고와 친환경 문구 가이드: OEKO-TEX·GRS·FSC 인쇄 조건",
        h1_fr="Logos de certification et allégations vertes sur les étiquettes : ce qui est permis",
        h1_es="Logos de certificación y declaraciones verdes en etiquetas: qué se puede imprimir",
        tag_zh="合规指南", tag_en="Compliance Guide", tag_ja="適合ガイド", tag_ko="컴플라이언스 가이드",
        tag_fr="Guide conformité", tag_es="Guía de conformidad",
        sum_zh="认证标志是受管理的商标，环保声明是可被抽查的声明，两者印错都要付出代价。本文说明 OEKO-TEX、GRS、FSC 分别只能由谁印、需要哪些授权与交易文件，环保声明怎么写才具体可核实，责任在品牌、供应商与印厂之间怎么分，并附上机前核对清单。",
        sum_en="A certification logo is a managed trademark and a green claim is an auditable statement — both are costly to get wrong. This guide explains who may print OEKO-TEX, GRS and FSC marks, which authorisation and transaction documents are needed, how to word claims so they stay specific and verifiable, and how responsibility splits between brand, supplier and printer.",
        sum_ja="認証ロゴは管理された商標、環境訴求は監査対象の声明であり、誤れば代償を伴います。本記事はOEKO-TEX・GRS・FSCを印刷できる主体と必要な許諾・取引書類、具体的で検証可能な訴求文の書き方、ブランド・サプライヤー・印刷会社の責任分担、印刷前チェックリストをまとめます。",
        sum_ko="인증 로고는 관리되는 상표이고 환경 문구는 감사 대상 선언이므로 잘못 쓰면 대가가 따릅니다. 이 글은 OEKO-TEX·GRS·FSC를 인쇄할 수 있는 주체와 필요한 허가·거래 서류, 구체적이고 검증 가능한 문구 작성법, 브랜드·공급사·인쇄사 간 책임 분담, 인쇄 전 체크리스트를 정리합니다.",
        sum_fr="Un logo de certification est une marque gérée et une allégation verte une déclaration auditable : se tromper coûte cher. Ce guide explique qui peut imprimer OEKO-TEX, GRS et FSC, quels documents sont nécessaires, comment formuler des allégations vérifiables et comment se répartissent les responsabilités.",
        sum_es="Un logo de certificación es una marca gestionada y una declaración verde es una afirmación auditable: equivocarse sale caro. Esta guía explica quién puede imprimir OEKO-TEX, GRS y FSC, qué documentos hacen falta, cómo redactar declaraciones verificables y cómo se reparten las responsabilidades.",
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

# ---------------- 2) blog/index.html 顶部插入两张卡片 ----------------nb
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
