#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-27 20:00 批次每日更新生成脚本（六语：zh-Hant 根 / en / ja / ko / fr / es）
- 联名与胶囊系列的辅料方案（collab-capsule-collection-trims-guide）
- 产能外迁下的辅料配套（offshore-sewing-trims-supply-guide）

用法: F:/hermes/venvs/tools/Scripts/python.exe daily_gen_20261027_2000.py [--check]
"""
import os, re, sys, subprocess, importlib.util

ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)
PY = sys.executable

SKEL = "blog/knitwear-sweater-trims-guide.html"
DATE_ZH = "2026年10月27日"
DATE_EN = "October 27, 2026"
DATE_JA = "2026年10月27日更新"
DATE_KO = "2026년 10월 27일 업데이트"
DATE_FR = "27 octobre 2026"
DATE_ES = "27 de octubre de 2026"
SITEMAP_DATE = "2026-10-27"
BUST_OLD, BUST_NEW = "186", "187"
LANGS = ["en", "ja", "ko", "fr", "es"]

ARTICLES = [
    dict(
        slug="collab-capsule-collection-trims-guide.html",
        body="blog/_body_collab.html",
        title_zh="联名与胶囊系列的辅料方案：双品牌吊牌、授权与限量标识 | TAGE",
        title_en="Collaboration Capsule Trims: Dual-Brand Hang Tags, Licensing and Limited Marks | TAGE",
        title_ja="コラボ・カプセルコレクションの副資材：2ブランドタグ、許諾、限定表示 | TAGE",
        title_ko="콜라보·캡슐 컬렉션 부자재: 두 브랜드 행택, 허가, 한정 표시 | TAGE",
        title_fr="Accessoires de capsule en collaboration : hangtags bicolores, licences et marquage limité | TAGE",
        title_es="Accesorios para cápsulas de colaboración: colgantes de dos marcas, licencias y series limitadas | TAGE",
        desc_zh="联名与胶囊系列的辅料方案：双 logo 怎么排、吊牌做一张还是两张、授权书与矢量文件要什么、洗水标与产地怎么标、限量编号放哪里、三周排产怎么压，附常被退回的写法。来自东莞泰阁包装，吊牌、织唛、洗水标与包装一站式配套。",
        desc_en="Collaboration capsule trims: two-logo layout, one hang tag or two, licence documents, care label and origin marking, limited numbering, three-week build.",
        desc_ja="コラボ・カプセルコレクションの副資材ガイド。2つのロゴの配置、タグを1枚か2枚か、許諾書とベクターデータ、洗濯表示と原産地、限定番号の置き場所、3週間での生産計画を解説します。東莞泰閣包装。",
        desc_ko="콜라보·캡슐 컬렉션 부자재 가이드. 두 로고 배치, 행택 한 장과 두 장의 선택, 허가서와 벡터 파일, 케어 라벨과 원산지, 한정 번호 위치, 3주 생산 계획을 정리했습니다. 둥관 TAGE 패키징.",
        desc_fr="Accessoires de capsule en collaboration : disposer deux logos, un ou deux hangtags, documents de licence, étiquette d'entretien et origine, numérotation limitée et production en trois semaines.",
        desc_es="Accesorios para cápsulas de colaboración: disposición de dos logotipos, uno o dos colgantes, documentos de licencia, etiqueta y origen, numeración limitada y producción en tres semanas.",
        crumb_zh="联名与胶囊系列辅料",
        crumb_en="Collaboration Capsule Trims",
        crumb_ja="コラボ・カプセル副資材",
        crumb_ko="콜라보·캡슐 부자재",
        crumb_fr="Accessoires de capsule",
        crumb_es="Accesorios de cápsula",
        h1_zh="联名与胶囊系列的辅料方案：双品牌吊牌、授权与限量标识",
        h1_en="Collaboration Capsule Trims: Dual-Brand Hang Tags, Licensing and Limited Marks",
        h1_ja="コラボ・カプセルコレクションの副資材：2ブランドタグ、許諾、限定表示",
        h1_ko="콜라보·캡슐 컬렉션 부자재: 두 브랜드 행택, 허가, 한정 표시",
        h1_fr="Accessoires pour capsule en collaboration : deux logos, licences et séries limitées",
        h1_es="Accesorios para cápsulas: dos logotipos, licencias y series limitadas",
        tag_zh="品牌配套", tag_en="Brand Programs", tag_ja="ブランド対応", tag_ko="브랜드 대응",
        tag_fr="Programme de marque", tag_es="Programa de marca",
        sum_zh="联名款看起来只是把两个 logo 印在一起，落到辅料上却是三件事同时变复杂：谁授权、谁的信息在前、什么时候必须到。本文拆六个问题：双 logo 怎么排、吊牌做几张、授权要哪些文件、洗水标与产地怎么写、限量与防伪放哪里，以及三周排产里哪些能压、哪些压不得。",
        sum_en="A collaboration looks like two logos side by side. On trims, three things get harder at once: who authorises what, whose information goes first, and when it has to arrive. Six questions: laying out two logos, how many hang tags, which licence documents, care label and origin, limited numbering, and what compresses in a three-week build.",
        sum_ja="コラボはロゴを2つ並べるだけに見えますが、副資材では同時に3つが難しくなります。誰が許諾するか、どちらの情報を先に出すか、いつまでに必要か。2つのロゴの配置、タグの枚数、必要な許諾書類、洗濯表示と原産地、限定番号の置き場所、3週間の生産で詰められる部分と詰められない部分を整理します。",
        sum_ko="콜라보는 로고 두 개를 나란히 인쇄하는 일처럼 보이지만, 부자재에서는 세 가지가 동시에 어려워집니다. 누가 허락하는지, 어느 쪽 정보가 먼저인지, 언제까지 도착해야 하는지. 두 로고 배치, 행택 장수, 허가 서류, 케어 라벨과 원산지, 한정 번호 위치, 3주 생산에서 줄일 수 있는 것과 없는 것을 정리합니다.",
        sum_fr="Une collaboration ressemble à deux logos côte à côte. Du côté des accessoires, trois choses se compliquent : qui autorise quoi, quelle information passe devant, et pour quelle date. Six questions : disposer deux logos, combien de hangtags, quels documents, étiquette et origine, numérotation limitée, et ce qui se comprime en trois semaines.",
        sum_es="Una colaboración parece dos logotipos uno al lado del otro. En accesorios se complican tres cosas: quién autoriza qué, qué información va primero y para cuándo. Seis cuestiones: disposición de dos logotipos, cuántos colgantes, documentos de licencia, etiqueta y origen, numeración limitada y qué se comprime en tres semanas.",
    ),
    dict(
        slug="offshore-sewing-trims-supply-guide.html",
        body="blog/_body_offshore.html",
        title_zh="产能外迁下的辅料配套：越南、柬埔寨、孟加拉怎么供料 | TAGE",
        title_en="Trims Supply for Offshore Sewing: Vietnam, Cambodia and Bangladesh | TAGE",
        title_ja="海外縫製への副資材供給：ベトナム・カンボジア・バングラデシュ | TAGE",
        title_ko="해외 봉제 부자재 공급: 베트남·캄보디아·방글라데시 | TAGE",
        title_fr="Fournir les accessoires pour une couture délocalisée : Vietnam, Cambodge, Bangladesh | TAGE",
        title_es="Suministro de accesorios para confección exterior: Vietnam, Camboya y Bangladés | TAGE",
        desc_zh="缝制搬到越南、柬埔寨、孟加拉后辅料怎么供：三条供料路径怎么选、按缝制上线日倒排交期、Made in 按缝制地而不是辅料产地、批次一致性的封样与远程验货、辅料单据与 HS 编码，以及三个常踩的坑。来自东莞泰阁包装。",
        desc_en="Offshore sewing in Vietnam, Cambodia or Bangladesh: three supply routes, back-scheduling from the line, origin by sewing country, batch checks and documents.",
        desc_ja="縫製がベトナム・カンボジア・バングラデシュへ移った後の副資材供給ガイド。3つの供給ルート、縫製稼働日からの逆算、縫製国に合わせた原産地表示、ロット一貫性と遠隔検品、書類とHSコード、よく踏む3つの落とし穴を解説します。東莞泰閣包装。",
        desc_ko="봉제가 베트남·캄보디아·방글라데시로 이동한 뒤의 부자재 공급 가이드. 세 가지 공급 경로, 봉제 투입일 역산, 봉제국 기준 원산지 표시, 로트 일관성과 원격 검사, 서류와 HS 코드, 자주 밟는 세 가지 함정을 정리했습니다. 둥관 TAGE 패키징.",
        desc_fr="Couture au Vietnam, au Cambodge ou au Bangladesh : trois voies d'approvisionnement, rétroplanning depuis la ligne, origine selon le pays de couture, cohérence des lots et documents.",
        desc_es="Confección en Vietnam, Camboya o Bangladés: tres rutas de suministro, planificación desde la línea, origen según el país de confección, consistencia de lote y documentos.",
        crumb_zh="跨国产能辅料配套",
        crumb_en="Offshore Trims Supply",
        crumb_ja="海外縫製の副資材供給",
        crumb_ko="해외 봉제 부자재 공급",
        crumb_fr="Accessoires pour couture délocalisée",
        crumb_es="Accesorios para confección exterior",
        h1_zh="产能外迁下的辅料配套：越南、柬埔寨、孟加拉工厂怎么供料",
        h1_en="Trims Supply for Offshore Sewing: Vietnam, Cambodia and Bangladesh",
        h1_ja="海外縫製への副資材供給：ベトナム・カンボジア・バングラデシュ工場への納入",
        h1_ko="해외 봉제 부자재 공급: 베트남·캄보디아·방글라데시 공장 대응",
        h1_fr="Fournir les accessoires à une couture délocalisée : Vietnam, Cambodge, Bangladesh",
        h1_es="Suministro de accesorios para confección exterior: Vietnam, Camboya y Bangladés",
        tag_zh="供应链", tag_en="Supply Chain", tag_ja="サプライチェーン", tag_ko="공급망",
        tag_fr="Chaîne d'approvisionnement", tag_es="Cadena de suministro",
        sum_zh="缝制搬到越南、柬埔寨、孟加拉之后，辅料并没有跟着搬。供料路径一变，交期、单证、产地标注与质量控制全都要重排。本文拆解：三条供料路径怎么选、按缝制上线日倒排交期、Made in 按缝制地写、批次一致性怎么远程管、辅料单据与 HS 编码，以及三个常踩的坑。",
        sum_en="When sewing moves to Vietnam, Cambodia or Bangladesh, trims do not follow. Once the route changes, lead times, documents, origin marking and quality control all need rebuilding: three supply routes, back-scheduling from the line, Made in by sewing country, remote batch consistency, paperwork and HS codes, and three common traps.",
        sum_ja="縫製がベトナム・カンボジア・バングラデシュへ移っても副資材は移りません。供給ルートが変われば、納期・書類・原産地表示・品質管理を組み直す必要があります。3つの供給ルート、縫製稼働日からの逆算、縫製国基準のMade in、ロット一貫性の遠隔管理、書類とHSコード、よく踏む3つの落とし穴を整理します。",
        sum_ko="봉제가 베트남·캄보디아·방글라데시로 옮겨도 부자재는 따라가지 않습니다. 공급 경로가 바뀌면 리드타임, 서류, 원산지 표시, 품질 관리를 다시 짜야 합니다. 세 가지 공급 경로, 봉제 투입일 역산, 봉제국 기준 Made in, 로트 일관성 원격 관리, 서류와 HS 코드, 자주 밟는 세 가지 함정을 정리합니다.",
        sum_fr="Quand la couture part au Vietnam, au Cambodge ou au Bangladesh, les accessoires ne suivent pas. Délais, documents, origine et contrôle qualité sont à reconstruire : trois voies d'approvisionnement, rétroplanning depuis la ligne, Made in selon le pays de couture, cohérence des lots, documents et codes SH, trois pièges.",
        sum_es="Cuando la confección se traslada a Vietnam, Camboya o Bangladés, los accesorios no la siguen. Plazos, documentos, origen y control de calidad deben rehacerse: tres rutas de suministro, planificación desde la línea, Made in según el país de confección, consistencia de lote, documentos y códigos HS, tres trampas.",
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
