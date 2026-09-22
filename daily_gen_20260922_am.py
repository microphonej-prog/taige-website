#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-09-22 上午 每日更新：2 篇新文章（六语：zh-Hant 根 / en / ja / ko / fr / es）
- 俄罗斯 / 欧亚经济联盟服装标签合规指南（俄语标注 / EAC / 诚实标识）
- 服装辅料质量索赔与责任划分指南
+ 列表页卡片 + gen_i18n 五语生成 + sitemap + BUST_VERSION 升级 + 简体转繁。

用法: python daily_gen_20260922_am.py
"""
import os, re, sys, subprocess, importlib.util

ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)
PY = sys.executable

SKEL = "blog/knitwear-sweater-trims-guide.html"
DATE_ZH = "2026年9月22日"
DATE_EN = "September 22, 2026"
DATE_JA = "2026年9月22日更新"
DATE_KO = "2026년 9월 22일 업데이트"
DATE_FR = "22 septembre 2026"
DATE_ES = "22 de septiembre de 2026"
SITEMAP_DATE = "2026-09-22"
BUST_OLD, BUST_NEW = "98", "99"
LANGS = ["en", "ja", "ko", "fr", "es"]

ARTICLES = [
    dict(
        slug="clothing-label-compliance-russia.html",
        body="blog/_body_russia.html",
        title_zh="俄罗斯服装标签合规指南：俄语标注、EAC 标志与诚实标识 | TAGE",
        title_en="Russia Clothing Label Requirements: Russian Text, EAC &amp; Chestny ZNAK | TAGE",
        title_ja="ロシアの衣料ラベル規制ガイド：ロシア語表記・EAC・チェストヌイズナク | TAGE",
        title_ko="러시아 의류 라벨 규정 가이드: 러시아어 표기, EAC, 체스니 즈낙 | TAGE",
        title_fr="Étiquetage des vêtements en Russie : russe, EAC et Chestny ZNAK | TAGE",
        title_es="Etiquetado de ropa en Rusia: ruso, EAC y Chestny ZNAK | TAGE",
        desc_zh="俄罗斯服装标签合规指南：标签须用俄语标注成分、洗护符号、尺码、原产国与责任方，产品须持 EAEU 符合性文件与 EAC 标志，服装类还分阶段纳入诚实标识数字码。讲清必标信息与西里尔字母排版要点。来自东莞泰阁包装。",
        desc_en="Russia clothing label requirements: Russian fibre content, care symbols, size and origin, EAEU conformity, the EAC mark and Chestny ZNAK Data Matrix codes.",
        desc_ja="ロシアの衣料ラベル規制ガイド。ロシア語での繊維組成・洗濯表示・サイズ・原産国・責任者表記、EAEU の適合文書と EAC マーク、チェストヌイズナクの Data Matrix コード、TR CU 017/2011 と 007/2011 の区分、必須記載7項目、キリル文字の組版、サンプル前チェックリストを解説します。東莞泰閣包装。",
        desc_ko="러시아 의류 라벨 규정 가이드: 러시아어 섬유 조성·세탁 표시·사이즈·원산지·책임자 표기, EAEU 적합성 문서와 EAC 마크, 체스니 즈낙 Data Matrix 코드, TR CU 017/2011과 007/2011 구분, 필수 기재 7항목, 키릴 문자 조판, 샘플 전 체크리스트를 정리했습니다. 둥관 TAGE 패키징.",
        desc_fr="Étiquetage en Russie : composition, symboles d'entretien, taille, origine et responsable en russe, documents EAEU, marquage EAC, codes Chestny ZNAK et composition en cyrillique.",
        desc_es="Etiquetado en Rusia: composición, símbolos, talla, origen y responsable en ruso, documentos de la EAEU, marcado EAC, códigos Chestny ZNAK y maquetación cirílica.",
        crumb_zh="俄罗斯标签合规", crumb_en="Russia Label Rules", crumb_ja="ロシアのラベル規制",
        crumb_ko="러시아 라벨 규정", crumb_fr="Étiquetage en Russie", crumb_es="Etiquetado en Rusia",
        h1_zh="俄罗斯服装标签合规指南：俄语标注、EAC 标志与诚实标识",
        h1_en="Russia Clothing Label Requirements: Russian Text, EAC and Chestny ZNAK",
        h1_ja="ロシアの衣料ラベル規制ガイド：ロシア語表記・EAC・チェストヌイズナク",
        h1_ko="러시아 의류 라벨 규정 가이드: 러시아어 표기, EAC, 체스니 즈낙",
        h1_fr="Étiquetage des vêtements en Russie : russe, EAC et Chestny ZNAK",
        h1_es="Etiquetado de ropa en Rusia: ruso, EAC y Chestny ZNAK",
        tag_zh="合规指南", tag_en="Compliance", tag_ja="コンプライアンス", tag_ko="컴플라이언스",
        tag_fr="Conformité", tag_es="Cumplimiento",
        sum_zh="俄罗斯与欧亚经济联盟的服装标签有两条硬线：文字必须是俄语，产品必须持有联盟符合性文件并加施 EAC 标志。本文讲清 TR CU 017/2011 与 007/2011 的分工、标签上不能少的七项信息、GOST ISO 3758 洗护符号与俄语文字的对齐、诚实标识（Честный ЗНАК）Data Matrix 数字码与实体标签的分工、西里尔字母排版三个典型坑，以及打样前六项核对清单。",
        sum_en="Two hard lines apply in Russia and the EAEU: the label text must be in Russian, and the product needs an EAEU conformity document with the EAC mark. This guide covers TR CU 017/2011 versus 007/2011, the seven mandatory label items, aligning GOST ISO 3758 symbols with Russian wording, how Chestny ZNAK Data Matrix codes share the load with the physical label, three Cyrillic typesetting traps and a six-point pre-sampling checklist.",
        sum_ja="ロシアと EAEU の衣料ラベルには二つの必須条件があります。表記はロシア語であること、製品に EAEU の適合文書と EAC マークが必要なことです。本記事は TR CU 017/2011 と 007/2011 の区分、必須記載7項目、GOST ISO 3758 記号とロシア語の整合、チェストヌイズナクの Data Matrix コードと物理ラベルの役割分担、キリル文字組版の3つの落とし穴、サンプル前6項目チェックリストを解説します。",
        sum_ko="러시아와 EAEU의 의류 라벨에는 두 가지 필수 조건이 있습니다. 표기는 러시아어여야 하고, 제품에는 EAEU 적합성 문서와 EAC 마크가 있어야 합니다. 이 글은 TR CU 017/2011과 007/2011의 구분, 필수 기재 7항목, GOST ISO 3758 기호와 러시아어 문구의 정합, 체스니 즈낙 Data Matrix 코드와 물리적 라벨의 역할 분담, 키릴 문자 조판의 세 가지 함정, 샘플 전 6항목 체크리스트를 정리합니다.",
        sum_fr="En Russie et dans l'EAEU, deux exigences fermes : texte en russe et document de conformité EAEU avec marquage EAC. Ce guide couvre TR CU 017/2011 et 007/2011, les sept mentions obligatoires, l'alignement des symboles GOST ISO 3758 avec le russe, le partage entre codes Chestny ZNAK et étiquette physique, trois pièges de composition cyrillique et une liste de contrôle avant échantillon.",
        sum_es="En Rusia y la EAEU rigen dos condiciones firmes: texto en ruso y documento de conformidad de la EAEU con marcado EAC. Esta guía cubre TR CU 017/2011 y 007/2011, las siete menciones obligatorias, la alineación de los símbolos GOST ISO 3758 con el ruso, el reparto entre códigos Chestny ZNAK y la etiqueta física, tres trampas de maquetación cirílica y una lista de verificación previa a la muestra.",
    ),
    dict(
        slug="garment-trims-claims-liability-guide.html",
        body="blog/_body_claims.html",
        title_zh="服装辅料质量索赔指南：责任怎么定、损失怎么算 | TAGE",
        title_en="Apparel Trims Quality Claims: Fixing Liability &amp; Settling Losses | TAGE",
        title_ja="衣料副資材の品質クレームガイド：責任の切り分けと賠償の進め方 | TAGE",
        title_ko="의류 부자재 품질 클레임 가이드: 책임 구분과 보상 협의 | TAGE",
        title_fr="Réclamations qualité sur les accessoires : responsabilité et règlement | TAGE",
        title_es="Reclamaciones de calidad en accesorios: responsabilidad y compensación | TAGE",
        desc_zh="服装辅料质量索赔指南：辅料问题金额小影响大，关键在发现早、留样全、责任界定清楚。讲清 72 小时处置顺序与证据链、五类情形的责任判定、四类高频投诉的判定口径与赔付优先级。来自东莞泰阁包装。",
        desc_en="Apparel trims claims: the 72-hour detection window, the evidence to keep, how liability is split, settlement options and the prevention that stops claims early.",
        desc_ja="衣料副資材の品質クレームガイド。72時間以内の初動と証拠の保全、材料・工程・版下・数量・輸送・使用の5つのケースの責任判定、色差・色落ち・強度・数量と湿気という頻出4クレームの判定基準、賠償の優先順位、未然防止策を解説します。東莞泰閣包装。",
        desc_ko="의류 부자재 품질 클레임 가이드: 72시간 이내 초동 대응과 증거 보존, 소재·공정·도안·수량·운송·사용 다섯 가지 상황의 책임 판단, 색차·이염·강도·수량·습기 네 가지 클레임 기준, 보상 우선순위와 예방 조치를 정리했습니다. 둥관 TAGE 패키징.",
        desc_fr="Réclamations sur les accessoires : la fenêtre des 72 heures, les preuves à conserver, la répartition des responsabilités, les modes de règlement et la prévention des litiges.",
        desc_es="Reclamaciones de accesorios: la ventana de 72 horas, las pruebas que conservar, el reparto de responsabilidades, las formas de compensación y la prevención.",
        crumb_zh="辅料质量索赔", crumb_en="Trims Claims", crumb_ja="副資材のクレーム",
        crumb_ko="부자재 클레임", crumb_fr="Réclamations accessoires", crumb_es="Reclamaciones de accesorios",
        h1_zh="服装辅料质量索赔指南：责任怎么定、损失怎么算",
        h1_en="Apparel Trims Quality Claims: Fixing Liability and Settling Losses",
        h1_ja="衣料副資材の品質クレームガイド：責任の切り分けと賠償の進め方",
        h1_ko="의류 부자재 품질 클레임 가이드: 책임 구분과 보상 협의",
        h1_fr="Réclamations qualité sur les accessoires : responsabilité et règlement",
        h1_es="Reclamaciones de calidad en accesorios: responsabilidad y compensación",
        tag_zh="采购实务", tag_en="Sourcing", tag_ja="調達実務", tag_ko="소싱 실무",
        tag_fr="Achats", tag_es="Compras",
        sum_zh="辅料出问题时金额不大，影响却很大：一批掉色的洗水标、断裂的吊绳，可能让整批成衣卡在仓库。索赔能否谈到合理结果，取决于发现够早、留样够全、责任界定够清楚。本文给出 72 小时处置顺序与证据链、五类情形的责任判定表、四类高频投诉（色差、耐洗掉色、断绳脱扣、短装受潮）的判定口径、赔付优先级，以及让索赔不发生的预防清单。",
        sum_en="When trims fail, the sums are small but the damage is not. Whether a claim ends fairly depends on early detection, complete reference samples and clear liability. This guide gives the 72-hour sequence and evidence chain, a five-scenario liability table, positions on four frequent complaints (colour difference, wash fastness, cord and fastener failure, shortages and moisture), settlement priority and a prevention checklist.",
        sum_ja="副資材のトラブルは金額が小さくても影響は大きくなります。クレームが妥当な着地点に収まるかは、発見の早さ、見本の保全、責任の切り分けで決まります。本記事は 72 時間の初動手順と証拠の連鎖、5つのケース別責任判定表、頻出4クレーム（色差・洗濯堅牢度・ひもと留め具・数量不足と湿気）の判定基準、賠償の優先順位、クレームを起こさない予防リストをまとめます。",
        sum_ko="부자재 문제는 금액은 작아도 영향은 큽니다. 클레임이 합리적으로 마무리되는지는 발견 시점, 견본 보존, 책임 구분에 달려 있습니다. 이 글은 72시간 처리 순서와 증거 사슬, 다섯 가지 상황별 책임 판단표, 네 가지 빈발 클레임(색차, 세탁 견뢰도, 끈·잠금구, 수량 부족·습기) 기준, 보상 우선순위, 클레임을 예방하는 체크리스트를 제공합니다.",
        sum_fr="Quand un accessoire dérape, les montants sont faibles mais les dégâts sont grands. L'issue dépend d'une détection rapide, de témoins complets et d'une responsabilité claire. Ce guide donne la séquence des 72 heures et la chaîne de preuves, un tableau de responsabilité en cinq cas, des positions sur quatre litiges fréquents, la priorité des règlements et une liste de prévention.",
        sum_es="Cuando un accesorio falla, el importe es pequeño pero el daño no. El resultado depende de detectar pronto, conservar muestras testigo y delimitar responsabilidades. Esta guía ofrece la secuencia de 72 horas y la cadena de pruebas, una tabla de responsabilidad en cinco casos, criterios para cuatro reclamaciones frecuentes, la prioridad de compensación y una lista de prevención.",
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
    print("写入 %s (%d KB) desc_zh=%d字 desc_en=%d字符 desc_ja=%d desc_ko=%d desc_fr=%d desc_es=%d"
          % (out, len(s.encode("utf-8")) // 1024, len(a["desc_zh"]), len(a["desc_en"]),
             len(a["desc_ja"]), len(a["desc_ko"]), len(a["desc_fr"]), len(a["desc_es"])))

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
