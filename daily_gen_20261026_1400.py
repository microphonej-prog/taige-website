#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-26 14:00 批次每日更新生成脚本（六语：zh-Hant 根 / en / ja / ko / fr / es）
- 洗水标折叠方式（care-label-fold-types）
- 吊牌多语言印刷与版本管理（hang-tag-multilingual-printing-guide）

用法: F:/hermes/venvs/tools/Scripts/python.exe daily_gen_20261026_1400.py [--check]
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
BUST_OLD, BUST_NEW = "182", "183"
LANGS = ["en", "ja", "ko", "fr", "es"]

ARTICLES = [
    dict(
        slug="care-label-fold-types.html",
        body="blog/_body_carefold.html",
        title_zh="洗水標摺疊方式指南：對摺、三摺與摺邊設計 | TAGE",
        title_en="Care Label Fold Types: Bi-Fold, Tri-Fold and Fold Margins | TAGE",
        title_ja="洗濯表示ラベルの折り方ガイド：二つ折り・三つ折り・折り代の設計 | TAGE",
        title_ko="케어 라벨 접지 방식 가이드: 반접기·삼절·접힘 여유 설계 | TAGE",
        title_fr="Pliure des étiquettes d'entretien : deux volets, triple et marges | TAGE",
        title_es="Plegado de etiquetas de cuidado: dos paneles, triple y márgenes | TAGE",
        desc_zh="洗水標摺疊方式指南：平張、對摺、三摺與四摺各自能用多少版面，法規資訊該放哪一面、材料與摺痕怎麼匹配、車縫位置與摺疊方向怎麼定，附可直接照做的打樣驗收清單。來自東莞泰閣包裝。",
        desc_en="Care label fold types compared: flat, bi-fold, tri-fold and four-fold, which face must carry regulatory text, material choice at the crease and seam position.",
        desc_ja="洗濯表示ラベルの折り方を比較。平張り・二つ折り・三つ折り・四つ折りで使える面、法規情報を置く面、折り筋と素材の相性、縫い位置と折り方向、検収チェックリストを解説します。東莞泰閣包装。",
        desc_ko="케어 라벨 접지 방식 비교. 평면·반접기·삼절·네 접기별 사용 면, 법정 정보를 두는 면, 접힘선과 소재의 궁합, 봉제 위치와 접는 방향, 검수 체크리스트를 정리했습니다. 둥관 TAGE 패키징.",
        desc_fr="Comparaison des pliures d'étiquettes d'entretien : à plat, deux volets, triple et quatre plis, face réglementaire, matière au pli, couture et contrôle.",
        desc_es="Comparación de plegados de etiquetas de cuidado: plana, dos paneles, triple y cuatro pliegues, cara reglamentaria, material en el pliegue y costura.",
        crumb_zh="洗水標摺疊方式",
        crumb_en="Care Label Folds",
        crumb_ja="洗濯表示の折り方",
        crumb_ko="케어 라벨 접지",
        crumb_fr="Pliure des étiquettes",
        crumb_es="Plegado de etiquetas",
        h1_zh="洗水標摺疊方式指南：對摺、三摺與摺邊設計",
        h1_en="Care Label Fold Types: Bi-Fold, Tri-Fold and Fold Margins",
        h1_ja="洗濯表示ラベルの折り方ガイド：二つ折り・三つ折り・折り代の設計",
        h1_ko="케어 라벨 접지 방식 가이드: 반접기·삼절·접힘 여유 설계",
        h1_fr="Pliure des étiquettes d'entretien : deux volets, triple et marges",
        h1_es="Plegado de etiquetas de cuidado: dos paneles, triple y márgenes",
        tag_zh="洗水标", tag_en="Care Labels", tag_ja="洗濯表示", tag_ko="케어 라벨",
        tag_fr="Étiquettes d'entretien", tag_es="Etiquetas de cuidado",
        sum_zh="洗水標的摺疊方式決定同一塊標籤能裝多少資訊、縫在哪裡、顧客翻看順不順手。很多返單問題不是印錯，而是摺疊方向或車縫邊選錯：法規資訊被摺進內側，縫完根本翻不開。本文比較平張、對摺、三摺與四摺的可用版面，講清第一面該放什麼、摺邊吃掉多少寬度、塗層與織帶在摺痕處的表現差異、後領中與側縫的摺向怎麼定，最後給一份五項打樣驗收清單。",
        sum_en="How a care label is folded decides how much information it carries, where it can be sewn and whether a shopper can read it. Plenty of reorders fail not on printing but on fold direction: regulatory text ends up folded inside. This guide compares flat, bi-fold, tri-fold and four-fold in usable panel area, sets out what belongs on face one, how much width fold margins eat, how coatings and woven tape behave at the crease, and how to fix fold direction at the centre back and side seam — closing with a five-point sampling check.",
        sum_ja="洗濯表示ラベルの折り方は、同じ一片に載せられる情報量、縫い位置、めくりやすさを決めます。再発注の失敗は印刷ではなく折り方向にあることが多く、法規情報が内側に折り込まれます。本稿は平張り・二つ折り・三つ折り・四つ折りの使える面を比較し、1面目に置く情報、折り代が奪う幅、コーティングと織りテープの折り筋での挙動、後ろ襟ぐりと脇縫いの折り方向、最後に5項目の検収チェックリストを示します。",
        sum_ko="케어 라벨의 접는 방식은 같은 조각에 담을 수 있는 정보량, 봉제 위치, 소비자가 넘겨보기 쉬운지를 결정합니다. 재발주 실패는 인쇄가 아니라 접는 방향에서 생기며 법정 정보가 안쪽으로 접혀 들어갑니다. 이 글은 평면·반접기·삼절·네 접기의 사용 면을 비교하고, 첫 면에 둘 정보, 접힘 여유가 잡아먹는 폭, 코팅과 직조 테이프의 접힘선 거동, 뒤목 중앙과 옆선의 접는 방향, 다섯 항목 검수 체크리스트를 정리합니다.",
        sum_fr="Le mode de pliage d'une étiquette d'entretien décide de la quantité d'informations, de l'endroit de couture et de la lisibilité. Beaucoup de réassorts ratent non sur l'impression mais sur le sens du pli : le texte réglementaire finit replié à l'intérieur. Ce guide compare à plat, deux volets, triple et quatre plis en surface utile, précise ce qui va sur la face un, la largeur mangée par les marges, le comportement des enductions et du ruban tissé au pli, et le sens du pli au milieu dos et en couture latérale — avec cinq contrôles d'échantillon.",
        sum_es="La forma de plegar una etiqueta de cuidado decide cuánta información lleva, dónde se cose y si el cliente puede leerla. Muchos pedidos repetidos fallan no por la impresión sino por el sentido del pliegue: el texto reglamentario queda doblado hacia dentro. Esta guía compara plana, dos paneles, triple y cuatro pliegues en superficie útil, fija qué va en la cara uno, cuánto ancho comen los márgenes, cómo se comportan recubrimientos y cinta tejida en el pliegue, y cómo fijar el sentido en el centro de la espalda y la costura lateral, con cinco comprobaciones.",
    ),
    dict(
        slug="hang-tag-multilingual-printing-guide.html",
        body="blog/_body_hglang.html",
        title_zh="吊牌多語言印刷指南：語言組合、版面與版本管理 | TAGE",
        title_en="Multilingual Hang Tags: Language Sets, Layout and Version Control | TAGE",
        title_ja="多言語タグの印刷ガイド：言語の組み合わせ・版面・版管理 | TAGE",
        title_ko="다국어 행택 인쇄 가이드: 언어 조합·지면·버전 관리 | TAGE",
        title_fr="Étiquettes multilingues : jeux de langues, maquette et gestion des versions | TAGE",
        title_es="Etiquetas multilingües: idiomas, maqueta y control de versiones | TAGE",
        desc_zh="吊牌多語言印刷指南：語言要求從法規、零售商規範、海關與品牌四個方向來，常見組合怎麼選，德語西語拉長三成後版面怎麼排，SKU 與語言版本怎麼管住不配錯貨，拼版如何攤薄成本，附打樣驗收清單。來自東莞泰閣包裝。",
        desc_en="Multilingual hang tags: where language requirements come from, common language sets, laying out German and Spanish text that runs longer, and version control.",
        desc_ja="多言語タグの実務ガイド。言語要件の出どころ、一般的な言語の組み合わせ、ドイツ語・スペイン語で長くなるテキストの版面、SKUと言語版の管理、面付けとコスト、検収チェックリストを解説します。東莞泰閣包装。",
        desc_ko="다국어 행택 실무 가이드. 언어 요건의 출처, 일반적인 언어 조합, 독일어·스페인어처럼 길어지는 텍스트의 지면 처리, SKU와 언어 버전 관리, 판걸이와 원가, 검수 체크리스트를 정리했습니다. 둥관 TAGE 패키징.",
        desc_fr="Étiquettes multilingues : origine de l'exigence linguistique, jeux de langues courants, mise en page de l'allemand et de l'espagnol plus longs, gestion des versions.",
        desc_es="Etiquetas multilingües: origen del requisito de idiomas, conjuntos habituales, maquetación de alemán y español más largos, y control de versiones por SKU.",
        crumb_zh="吊牌多語言印刷",
        crumb_en="Multilingual Tags",
        crumb_ja="多言語タグ",
        crumb_ko="다국어 행택",
        crumb_fr="Étiquettes multilingues",
        crumb_es="Etiquetas multilingües",
        h1_zh="吊牌多語言印刷指南：語言組合、版面與版本管理",
        h1_en="Multilingual Hang Tags: Language Sets, Layout and Version Control",
        h1_ja="多言語タグの印刷ガイド：言語の組み合わせ・版面・版管理",
        h1_ko="다국어 행택 인쇄 가이드: 언어 조합·지면·버전 관리",
        h1_fr="Étiquettes multilingues : jeux de langues, maquette et gestion des versions",
        h1_es="Etiquetas multilingües: idiomas, maqueta y control de versiones",
        tag_zh="出口实务", tag_en="Export Practice", tag_ja="輸出実務", tag_ko="수출 실무",
        tag_fr="Pratique export", tag_es="Práctica de exportación",
        sum_zh="同一款衣服賣到德國、法國、西班牙和墨西哥，吊牌上到底要印幾種語言？難點從來不是翻譯，而是版面裝不裝得下、版本管不管得住、能不能一次印完。本文拆解語言要求的四個來源，給出英文單語到英德法義五種常見組合的適用市場與風險，講清德語長三成、西語長兩成時該按哪一版先排版，以及用 SKU 乘市場矩陣、獨立料號、文件命名規則把版本管住，最後說明拼版如何攤薄成本與五項驗收清單。",
        sum_en="One style sold in Germany, France, Spain and Mexico: how many languages should the tag carry? The difficulty is never translation but whether the layout holds, whether versions stay controlled and whether it prints in one pass. This guide breaks down the four sources of a language requirement, compares five common sets from English-only to EN/DE/FR/IT with their markets and risks, explains laying out German (30% longer) and Spanish (20% longer) first, and how a SKU-by-market matrix, separate part numbers and file naming keep versions in check — plus imposition economics and a five-point acceptance check.",
        sum_ja="同じ型をドイツ・フランス・スペイン・メキシコで売るとき、タグに何言語を載せるか。難点は翻訳ではなく、版面に収まるか、版管理が効くか、一度で印刷できるかです。本稿は言語要件の4つの出どころ、英語のみから英独仏伊までの5つの組み合わせと市場・リスク、ドイツ語（3割長い）とスペイン語（2割長い）を先に組む理由、SKU×市場マトリクス・品番分割・ファイル命名による版管理、面付けのコスト論と5項目の検収を示します。",
        sum_ko="같은 스타일을 독일·프랑스·스페인·멕시코에 판매할 때 행택에 몇 개 언어를 넣어야 할까요. 어려움은 번역이 아니라 지면에 담기는지, 버전 관리가 되는지, 한 번에 인쇄되는지입니다. 이 글은 언어 요건의 네 출처, 영어 단일부터 영·독·불·이탈리아어까지 다섯 조합의 시장과 리스크, 독일어(30% 길다)와 스페인어(20% 길다)를 먼저 조판하는 이유, SKU×시장 매트릭스·품번 분리·파일 명명으로 버전을 관리하는 법, 판걸이 원가와 다섯 항목 검수를 정리합니다.",
        sum_fr="Un modèle vendu en Allemagne, en France, en Espagne et au Mexique : combien de langues sur l'étiquette ? La difficulté n'est jamais la traduction mais la tenue de la maquette, le contrôle des versions et l'impression en une passe. Ce guide décompose les quatre sources de l'exigence, compare cinq jeux courants de l'anglais seul à EN/DE/FR/IT avec marchés et risques, explique pourquoi composer d'abord l'allemand (30 % plus long) et l'espagnol (20 %), et comment une matrice SKU × marché, des références distinctes et un nommage de fichiers maîtrisent les versions — avec l'économie d'imposition et cinq contrôles.",
        sum_es="Un modelo vendido en Alemania, Francia, España y México: ¿cuántos idiomas en la etiqueta? La dificultad nunca es la traducción, sino si la maqueta aguanta, si las versiones se controlan y si se imprime de una vez. Esta guía desglosa las cuatro fuentes del requisito, compara cinco conjuntos desde solo inglés hasta EN/DE/FR/IT con sus mercados y riesgos, explica por qué maquetar primero el alemán (30% más largo) y el español (20%), y cómo una matriz SKU × mercado, referencias separadas y un nombrado de archivos controlan las versiones, con la economía de imposición y cinco comprobaciones.",
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
