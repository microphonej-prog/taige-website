# -*- coding: utf-8 -*-
"""2026-10-23 14:00 批次校验：六语属性、生成页残留、canonical、sitemap、卡片、JSON-LD、BUST_VERSION。"""
import re, json, os, importlib.util
from html.parser import HTMLParser

spec = importlib.util.spec_from_file_location("m", "daily_meta_20261023_1400.py")
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
ARTICLES = m.ARTICLES
LANGS = ["en", "ja", "ko", "fr", "es"]
NEED = ["data-en", "data-fr", "data-es", "data-ja", "data-ko"]


class Body(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.in_body = False
        self.tags = []

    def handle_starttag(self, tag, attrs):
        d = {k.lower(): (v or "") for k, v in attrs}
        if tag == "section" and d.get("class", "").startswith("article-body"):
            self.in_body = True
            return
        if self.in_body:
            self.tags.append((tag, d))

    def handle_endtag(self, tag):
        if self.in_body and tag == "section":
            self.in_body = False


fails = 0

print("== 1) 中文根页 article-body 六语属性完整性 ==")
for a in ARTICLES:
    f = "blog/" + a["slug"]
    s = open(f, encoding="utf-8").read()
    p = Body(); p.feed(s)
    dzh = [(t, x) for t, x in p.tags if "data-zh" in x]
    miss = [(t, k) for t, x in dzh for k in NEED if not x.get(k, "").strip()]
    empty = len(re.findall(r'data-(?:zh|en|fr|es|ja|ko)=""', s))
    print("  %-42s 标签%d 带data-zh %d 缺失 %d 空引号 %d" % (a["slug"], len(p.tags), len(dzh), len(miss), empty))
    if miss or empty:
        fails += 1
        print("     缺失:", miss[:8])
    # 正文简体字数（用于确认信息量）
    cjk = len(re.findall(r"[\u4e00-\u9fff]", " ".join(v for v in re.findall(r'data-zh="([^"]*)"', s))))
    print("     data-zh 汉字数 ≈ %d" % cjk)
    # JSON-LD
    lds = re.findall(r'<script type="application/ld\+json">(.*?)</script>', s, re.S)
    for x in lds:
        json.loads(x)
    print("     JSON-LD %d 处合法" % len(lds))
    # 骨架残留
    for bad in ("knitwear-sweater-trims-guide", "針織與毛衣", "针织与毛衣",
                "clothing-label-compliance-peru", "fsc-certified-hang-tags"):
        if bad in s:
            print("     ！骨架/旧文残留:", bad); fails += 1

print("== 2) 五语生成页：title / desc / canonical / 残留 ==")
for a in ARTICLES:
    slug = a["slug"]
    for lang in LANGS:
        path = "%s/blog/%s" % (lang, slug)
        assert os.path.exists(path), path
        s = open(path, encoding="utf-8").read()
        title = re.search(r"<title[^>]*>(.*?)</title>", s, re.S).group(1).strip()
        exp_title = html_unescape = a["title_" + lang].replace("&amp;", "&")
        desc = re.search(r'<meta name="description"[^>]*content="([^"]*)"', s, re.S)
        desc = desc.group(1) if desc else ""
        canon = re.search(r'<link rel="canonical" href="([^"]*)"', s).group(1)
        exp_canon = "https://taigetag.com/%s/blog/%s" % (lang, slug)
        p = Body(); p.feed(s)
        residue = sum(1 for t, x in p.tags if any(k.startswith("data-") for k in x))
        body_txt = re.sub(r"<script.*?</script>", "", s, flags=re.S)
        cjk = len(re.findall(r"[\u4e00-\u9fff]", body_txt))
        ok_t = (title.replace("&#x27;", "'") == exp_title.replace("&#x27;", "'")) or title == exp_title
        ok_d = desc.strip() == a["desc_" + lang].strip()
        ok_c = canon == exp_canon
        flag = "ok" if (ok_t and ok_d and ok_c and residue == 0) else "FAIL"
        if flag == "FAIL":
            fails += 1
        print("  %-46s title=%s desc=%s canon=%s data残留=%d 汉字=%d  %s"
              % (path, ok_t, ok_d, ok_c, residue, cjk, flag))
        if not ok_t:
            print("     实得:", title[:90], "\n     期望:", exp_title[:90])
        if not ok_d:
            print("     实得desc:", desc[:90], "\n     期望desc:", a["desc_" + lang][:90])
        if not ok_c:
            print("     实得canon:", canon, "期望:", exp_canon)

print("== 3) 英文/法文/西文页中文残留（应为 0） ==")
for a in ARTICLES:
    for lang in ("en", "fr", "es"):
        s = open("%s/blog/%s" % (lang, a["slug"]), encoding="utf-8").read()
        body = s[s.index('class="article-body"'):s.index("</main>")]
        cjk = len(re.findall(r"[\u4e00-\u9fff]", body))
        print("  %-46s 正文汉字 %d %s" % ("%s/blog/%s" % (lang, a["slug"]), cjk, "ok" if cjk == 0 else "FAIL"))
        if cjk:
            fails += 1

print("== 4) 日/韩页中文简体残留抽查 ==")
for a in ARTICLES:
    for lang in ("ja", "ko"):
        s = open("%s/blog/%s" % (lang, a["slug"]), encoding="utf-8").read()
        body = s[s.index('class="article-body"'):s.index("</main>")]
        # 简体专用字（繁体/日文都不使用这些字形）
        simp = re.findall(r"[个们为说这时对开实现发应开关门问题经验应该让给还从会能动过样种当经与]", body)
        print("  %-46s 简体嫌疑字 %d %s" % ("%s/blog/%s" % (lang, a["slug"]), len(simp), "ok" if not simp else "查"))
        if simp:
            print("     ", "".join(sorted(set(simp)))[:60])

print("== 5) sitemap ==")
sm = open("sitemap.xml", encoding="utf-8").read()
urls = re.findall(r"<loc>([^<]*)</loc>", sm)
for a in ARTICLES:
    for pre in ["blog/"] + ["%s/blog/" % l for l in LANGS]:
        u = "https://taigetag.com/%s%s" % (pre, a["slug"])
        ok = u in urls
        if not ok:
            fails += 1
            print("  ！缺 URL:", u)
print("  <loc> 总数 %d；12 个新 URL %s" % (len(urls), "全部在位" if all(
    "https://taigetag.com/blog/%s" % a["slug"] in urls for a in ARTICLES) else "有缺失"))
for u in ["https://taigetag.com/blog/index.html"] + ["https://taigetag.com/%s/blog/index.html" % l for l in LANGS]:
    mm = re.search(r"<loc>%s</loc>\s*<lastmod>([^<]*)</lastmod>" % re.escape(u), sm)
    print("  blog index lastmod %-58s %s" % (u, mm.group(1) if mm else "？"))

print("== 6) 列表页卡片 ==")
for p in ["blog/index.html"] + ["%s/blog/index.html" % l for l in LANGS]:
    s = open(p, encoding="utf-8").read()
    cardpos = {}
    for a in ARTICLES:
        i = s.find('href="%s"' % a["slug"])
        cardpos[a["slug"][:28]] = i
    first = min([i for i in cardpos.values() if i >= 0], default=-1)
    grid = s.find('<div class="post-grid">')
    print("  %-28s 卡片位置 %s；首个新卡在 grid 后偏移 %s" % (p, cardpos, first - grid if first >= 0 else "缺失"))
    if any(i < 0 for i in cardpos.values()):
        fails += 1

print("== 7) BUST_VERSION ==")
mj = open("js/main.js", encoding="utf-8").read()
v = re.search(r'var BUST_VERSION = "(\d+)"', mj).group(1)
print("  BUST_VERSION =", v, "ok" if v == "179" else "FAIL")
if v != "179":
    fails += 1

print("\n结论: 失败项 =", fails)
raise SystemExit(1 if fails else 0)
