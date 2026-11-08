#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-11-08 14:00 批次：2 篇文章（八語）+ 列表卡片 + 七語目錄 + 本地化閘門 + sitemap + BUST_VERSION。
必須用 OpenCC 環境執行：F:/hermes/venvs/tools/Scripts/python.exe daily_gen_20261108_1400.py
"""
import os, re, sys, subprocess, importlib.util

import content_symbols_20261108 as CF
import content_hardware_20261108 as CH

ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)
PY = sys.executable

SKEL = "blog/knitwear-sweater-trims-guide.html"
DATE = dict(zh="2026年11月8日", en="November 8, 2026", ja="2026年11月8日",
            ko="2026년 11월 8일", fr="8 novembre 2026", es="8 de noviembre de 2026",
            de="8. November 2026", pt="8 de novembro de 2026")
SITEMAP_DATE = "2026-11-08"
BUST_OLD, BUST_NEW = "208", "209"
LANGS = ["en", "fr", "es", "ja", "ko", "de", "pt"]
ORDER = ["zh", "en", "fr", "es", "ja", "ko", "de", "pt"]
HL = dict(zh="zh-Hant", en="en", fr="fr", es="es", ja="ja", ko="ko", de="de", pt="pt-BR")

BTN = {
    "care-label-symbols-chart.html": dict(
        zh="獲取洗水標報價 →", en="Request a care label quote →",
        fr="Demander un devis étiquettes →", es="Solicitar presupuesto de etiquetas →",
        ja="洗濯表示ラベルの見積りを依頼 →", ko="세탁 표시 라벨 견적 요청 →",
        de="Angebot für Pflegeetiketten anfragen →", pt="Solicitar orçamento de etiquetas →"),
    "eyelet-grommet-rivet-guide.html": dict(
        zh="諮詢五金輔料報價 →", en="Ask about metal trims →",
        fr="Demander un devis ferrures →", es="Consultar herrajes metálicos →",
        ja="金属副資材の見積りを相談 →", ko="금속 부자재 견적 상담 →",
        de="Metallbeschläge anfragen →", pt="Consultar ferragens metálicas →"),
}

MORE = dict(zh="閱讀全文 →", en="Read more →", fr="Lire la suite →", es="Leer más →",
            ja="続きを読む →", ko="자세히 보기 →", de="Weiterlesen →", pt="Ler mais →")


def attrs(d):
    return " ".join('data-%s="%s"' % (l, d[l]) for l in ORDER)


def build_blocks(blocks):
    out = ['  <section class="article-body">', '    <div class="container">', '']
    for b in blocks:
        kind, payload = b[0], b[1]
        if kind in ("p", "h2", "h3", "callout"):
            tag = "div" if kind == "callout" else kind
            cls = ' class="callout"' if kind == "callout" else ""
            out.append('      <%s%s %s>%s</%s>' % (tag, cls, attrs(payload), payload["zh"], tag))
            out.append('')
        elif kind in ("ul", "ol"):
            out.append('      <%s>' % kind)
            for li in payload:
                href = li.get("href")
                if href:
                    out.append('        <li><a href="%s" %s>%s</a></li>' % (href, attrs(li), li["zh"]))
                else:
                    out.append('        <li %s>%s</li>' % (attrs(li), li["zh"]))
            out.append('      </%s>' % kind)
            out.append('')
        elif kind == "table":
            head, rows = b[1], b[2]
            out.append('      <table>')
            out.append('        <thead>')
            out.append('          <tr>')
            for th in head:
                out.append('            <th %s>%s</th>' % (attrs(th), th["zh"]))
            out.append('          </tr>')
            out.append('        </thead>')
            out.append('        <tbody>')
            for row in rows:
                out.append('          <tr>')
                for td in row:
                    out.append('            <td %s>%s</td>' % (attrs(td), td["zh"]))
                out.append('          </tr>')
            out.append('        </tbody>')
            out.append('      </table>')
            out.append('')
        elif kind == "cta":
            btn = BTN[current_slug]
            out.append('      <div class="cta-box">')
            out.append('        <p %s>%s</p>' % (attrs(payload), payload["zh"]))
            out.append('        <a class="cta-btn" href="../contact.html" %s>%s</a>' % (attrs(btn), btn["zh"]))
            out.append('      </div>')
            out.append('')
        else:
            raise SystemExit("未知區塊類型 %s" % kind)
    out.append('    </div>')
    out.append('  </section>')
    return "\n".join(out)


def build_page(meta, blocks):
    slug = meta["slug"]
    s = open(SKEL, encoding="utf-8").read()
    s = s.replace(SKEL.replace("blog/", ""), slug)

    t = meta["title"]
    s = re.sub(r'<title[^>]*>.*?</title>',
               '<title %s>%s</title>' % (attrs(t), t["zh"]), s, count=1, flags=re.S)

    d = meta["desc"]
    new_desc = '<meta name="description" %s content="%s">' % (attrs(d), d["zh"])
    s, n = re.subn(r'<meta name="description".*?>', lambda m: new_desc, s, count=1, flags=re.S)
    assert n == 1, "description 替換失敗"

    lines = ['<link rel="canonical" href="https://taigetag.com/blog/%s">' % slug]
    for l in ORDER:
        href = "https://taigetag.com/blog/%s" % slug if l == "zh" else "https://taigetag.com/%s/blog/%s" % (l, slug)
        lines.append('<link rel="alternate" hreflang="%s" href="%s">' % (HL[l], href))
    lines.append('<link rel="alternate" hreflang="x-default" href="https://taigetag.com/blog/%s">' % slug)
    s, n = re.subn(r'<link rel="canonical" href="[^"]*">(?:\s*<link rel="alternate"[^\n]*>)+',
                   "\n".join(lines), s, count=1)
    assert n == 1, "canonical/hreflang 替換失敗"

    c = meta["crumb"]
    crumb = ('<div class="crumb">'
             '<a href="../index.html" data-zh="首頁" data-en="Home" data-fr="Accueil" data-es="Inicio" '
             'data-ja="ホーム" data-ko="홈" data-de="Startseite" data-pt="Início">首頁</a>'
             ' / <a href="index.html" data-zh="輔料 FAQ" data-en="Trims FAQ" data-fr="FAQ Accessoires" '
             'data-es="FAQ Accesorios" data-ja="副資材 FAQ" data-ko="부자재 FAQ" data-de="Accessoires-FAQ" '
             'data-pt="FAQ de aviamentos">輔料 FAQ</a>'
             ' / <span %s>%s</span></div>' % (attrs(c), c["zh"]))
    s, n = re.subn(r'<div class="crumb">.*?</div>', lambda m: crumb, s, count=1, flags=re.S)
    assert n == 1, "crumb 替換失敗"

    h = meta["h1"]
    s, n = re.subn(r'<h1 [^>]*>.*?</h1>', lambda m: '<h1 %s>%s</h1>' % (attrs(h), h["zh"]),
                   s, count=1, flags=re.S)
    assert n == 1, "h1 替換失敗"

    meta_line = ('<p data-zh="泰閣包裝 · 更新於 %(zh)s" data-en="By TAGE Packaging &nbsp;·&nbsp; Updated %(en)s" '
                 'data-ja="泰閣包装 · %(ja)s更新" data-ko="TAGE 패키징 · %(ko)s 업데이트" '
                 'data-fr="Par TAGE Packaging &nbsp;·&nbsp; Mis à jour le %(fr)s" '
                 'data-es="Por TAGE Packaging &nbsp;·&nbsp; Actualizado el %(es)s" '
                 'data-de="Von TAGE Packaging &nbsp;·&nbsp; Aktualisiert am %(de)s" '
                 'data-pt="Por TAGE Packaging &nbsp;·&nbsp; Atualizado em %(pt)s">'
                 '泰閣包裝 · 更新於 %(zh)s</p>' % DATE)
    s, n = re.subn(r'<p data-zh="泰[阁閣]包[装裝] · 更新[于於][^"]*".*?</p>',
                   lambda m: meta_line, s, count=1, flags=re.S)
    assert n == 1, "meta 行替換失敗"

    old3 = re.search(r'"position": 3,\s*"name": "([^"]*)"', s)
    if old3 and old3.group(1) != h["zh"]:
        s = s.replace('"%s"' % old3.group(1), '"%s"' % h["zh"])
    s, n = re.subn(r'"headline": "[^"]*"', lambda m: '"headline": "%s"' % h["zh"], s, count=1)
    assert n == 1, "headline 替換失敗"
    lang_list = ",\n".join('    "%s"' % HL[l] for l in ORDER)
    s, n = re.subn(r'"inLanguage": \[[^\]]*\]', lambda m: '"inLanguage": [\n%s\n   ]' % lang_list,
                   s, count=1, flags=re.S)
    if n != 1:
        print("  ! inLanguage 未替換，跳過")

    body = build_blocks(blocks)
    i0 = s.index('  <section class="article-body">')
    i1 = s.index('\n</main>')
    s = s[:i0] + body + s[i1:]

    out = "blog/%s" % slug
    open(out, "w", encoding="utf-8", newline="").write(s)
    print("寫入 %s (%d KB)" % (out, len(s.encode('utf-8')) // 1024))


# ---------------- 撞車安全閘 ----------------
SM0 = open("sitemap.xml", encoding="utf-8").read()
for meta in (CF.META, CH.META):
    slug = meta["slug"]
    for p in ["blog/%s" % slug] + ["%s/blog/%s" % (l, slug) for l in LANGS]:
        if os.path.exists(p):
            raise SystemExit("選題撞車：%s 已存在" % p)
    if "/blog/%s</loc>" % slug in SM0:
        raise SystemExit("選題撞車：sitemap 已含 %s" % slug)
print("選題全新，開始生成")

# ---------------- 1) 兩篇文章 ----------------
for meta, blocks in ((CF.META, CF.BLOCKS), (CH.META, CH.BLOCKS)):
    current_slug = meta["slug"]
    print("-- %s  desc_zh=%d字 desc_en=%d字符" % (current_slug, len(meta["desc"]["zh"]), len(meta["desc"]["en"])))
    build_page(meta, blocks)

# ---------------- 2) blog/index.html 卡片 ----------------
CARD = '''      <article class="post-card">
        <span class="tag" {tag}>{tag_zh}</span>
        <h3 {h3}>{h3_zh}</h3>
        <p {sum}>{sum_zh}</p>
        <a class="more" href="{slug}" {more}>閱讀全文 →</a>
      </article>
'''
cards = ""
for meta in (CF.META, CH.META):
    cards += CARD.format(tag=attrs(meta["tag"]), tag_zh=meta["tag"]["zh"],
                         h3=attrs(meta["h1"]), h3_zh=meta["h1"]["zh"],
                         sum=attrs(meta["summary"]), sum_zh=meta["summary"]["zh"],
                         more=attrs(MORE), slug=meta["slug"])

idx = "blog/index.html"
s = open(idx, encoding="utf-8").read()
marker = '<div class="post-grid">\n'
assert marker in s, "post-grid 未找到"
for meta in (CF.META, CH.META):
    assert meta["slug"] not in s, "卡片已存在：%s" % meta["slug"]
s = s.replace(marker, marker + "\n" + cards, 1)
open(idx, "w", encoding="utf-8", newline="").write(s)
print("blog/index.html 插入 2 張卡片完成")

# ---------------- 3) 簡體 -> 繁體 ----------------
spec = importlib.util.spec_from_file_location("to_traditional", os.path.join(ROOT, "to_traditional.py"))
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
changed = []
for p in ["blog/%s" % m["slug"] for m in (CF.META, CH.META)] + [idx]:
    s0 = open(p, encoding="utf-8").read()
    s1 = mod.convert_html(s0)
    if s1 != s0:
        open(p, "w", encoding="utf-8", newline="").write(s1)
        changed.append(os.path.basename(p))
print("繁體轉換改動：%d %s" % (len(changed), changed))

# ---------------- 4) gen_i18n 七語 ----------------
TARGETS = ["blog/%s" % m["slug"] for m in (CF.META, CH.META)] + [idx]
for lang in LANGS:
    r = subprocess.run([PY, "gen_i18n.py", lang] + TARGETS, capture_output=True, text=True, encoding="utf-8")
    if r.returncode != 0:
        print(r.stdout[-3000:], r.stderr[-3000:])
        raise SystemExit("gen_i18n %s 失敗" % lang)
    print("gen_i18n %s -> %d 文件 ok" % (lang, len(TARGETS)))

# ---------------- 5) 本地化閘門 ----------------
sys.path.insert(0, r"F:/hermes/scripts")
spec2 = importlib.util.spec_from_file_location("chk", r"F:/hermes/scripts/check_localization.py")
chk = importlib.util.module_from_spec(spec2)
spec2.loader.exec_module(chk)

MATRIX = {}
for meta in (CF.META, CH.META):
    slug = meta["slug"]
    f = "blog/%s" % slug
    row = {}
    for lang in ["fr", "es", "ja", "ko", "de", "pt"]:
        r = chk.analyze(f, lang)
        row[lang] = r
        print("%s %-34s [%s] 正文%d字 法規%d/標籤%d/計量%d 合計%d(需≥%d)" % (
            "PASS" if r["pass"] else "FAIL", slug, lang, r["chars"],
            r["hits"]["法规"], r["hits"]["标签"], r["hits"]["计量"],
            r["total"], r["min_required"]))
    MATRIX[slug] = row

FAILED = {s: [l for l, r in row.items() if not r["pass"]] for s, row in MATRIX.items()}
print("FAILED:", FAILED)

# 未過閘門的語種：回加 noindex（gen_i18n 因源頁含 data-de/pt 而不會自動加）
for slug, langs in FAILED.items():
    for lang in langs:
        p = "%s/blog/%s" % (lang, slug)
        t = open(p, encoding="utf-8").read()
        if 'name="robots"' in t:
            t = re.sub(r'<meta name="robots"[^>]*>',
                       '<meta name="robots" content="noindex,follow">', t)
        else:
            t = re.sub(r'</head>', '<meta name="robots" content="noindex,follow"></head>', t, count=1)
        open(p, "w", encoding="utf-8", newline="").write(t)
        print("  noindex 回加：%s" % p)

# ---------------- 6) sitemap ----------------
def block(url):
    return ("  <url>\r\n    <loc>%s</loc>\r\n    <lastmod>%s</lastmod>\r\n"
            "    <changefreq>monthly</changefreq>\r\n    <priority>0.7</priority>\r\n  </url>\r\n"
            % (url, SITEMAP_DATE))


sm = open("sitemap.xml", encoding="utf-8", newline="").read()
before = sm.count("<loc>")
blocks = []
for m in (CF.META, CH.META):
    slug = m["slug"]
    ok_langs = [l for l in LANGS if l not in FAILED[slug]]
    urls = ["https://taigetag.com/blog/%s" % slug] + \
           ["https://taigetag.com/%s/blog/%s" % (l, slug) for l in ok_langs]
    for u in urls:
        assert "<loc>%s</loc>" % u not in sm, "sitemap 已有 %s" % u
        blocks.append(block(u))
sm = sm.replace("</urlset>", "".join(blocks) + "</urlset>", 1)

for u in ["https://taigetag.com/blog/index.html"] + \
         ["https://taigetag.com/%s/blog/index.html" % l for l in LANGS]:
    pat = re.compile(r'(<loc>%s</loc>\r?\n\s*<lastmod>)[^<]*(</lastmod>)' % re.escape(u))
    sm, n = pat.subn(lambda m: m.group(1) + SITEMAP_DATE + m.group(2), sm, count=1)
    if n != 1:
        print("  ! blog index lastmod 未更新（sitemap 無此 URL）：%s" % u)

open("sitemap.xml", "w", encoding="utf-8", newline="").write(sm)
print("sitemap 新增 %d 個 URL，<loc> %d -> %d" % (len(blocks), before, sm.count("<loc>")))

# ---------------- 7) BUST_VERSION ----------------
mj = open("js/main.js", encoding="utf-8").read()
assert 'var BUST_VERSION = "%s";' % BUST_OLD in mj, "BUST_VERSION 不是 %s" % BUST_OLD
mj = mj.replace('var BUST_VERSION = "%s";' % BUST_OLD, 'var BUST_VERSION = "%s";' % BUST_NEW, 1)
open("js/main.js", "w", encoding="utf-8", newline="").write(mj)
print("BUST_VERSION %s -> %s" % (BUST_OLD, BUST_NEW))

# ---------------- 8) hreflang 規範化 ----------------
r = subprocess.run([PY, "fix_hreflang.py", "--apply"], capture_output=True, text=True, encoding="utf-8")
print("fix_hreflang rc=%d\n%s" % (r.returncode, (r.stdout or "")[-1500:]))
