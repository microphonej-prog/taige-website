#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""线上验证（六语）：无头 Chrome 渲染 title/h1 + sitemap 包含新 URL。"""
import subprocess, re, sys, os, tempfile, urllib.request, ssl

CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
SLUGS = ["garment-gift-box-packaging.html", "poly-bag-cost-guide.html"]
LANGS = ["zh", "en", "ja", "ko", "fr", "es"]
V = "95"

def url_for(lang, slug):
    if lang == "zh":
        return "https://taigetag.com/blog/%s?lang=zh&v=%s" % (slug, V)
    return "https://taigetag.com/%s/blog/%s?lang=%s&v=%s" % (lang, slug, lang, V)

def render(url):
    out = subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-sandbox",
                          "--virtual-time-budget=9000", "--dump-dom", url],
                         capture_output=True, text=True, encoding="utf-8", errors="replace",
                         timeout=120)
    return out.stdout or ""

# 每语言正文特征词（用于确认该语言的正文真的渲染出来了）
MARKERS = {
    "zh": ["禮盒", "膠袋"],
    "en": ["greyboard", "raw material"],
    "ja": ["グレーボール紙", "原材料"],
    "ko": ["회색 판지", "원재료"],
    "fr": ["carton gris", "matière première"],
    "es": ["cartón gris", "materia prima"],
}

print("== 1) 无头 Chrome 六语渲染 ==")
fails = []
for slug in SLUGS:
    print("-- %s" % slug)
    for lang in LANGS:
        u = url_for(lang, slug)
        dom = render(u)
        t = re.search(r"<title[^>]*>(.*?)</title>", dom, re.S)
        h1 = re.search(r"<h1[^>]*>(.*?)</h1>", dom, re.S)
        title = re.sub(r"\s+", " ", t.group(1)).strip() if t else "(无 title)"
        h1v = re.sub(r"<[^>]+>", "", h1.group(1)).strip() if h1 else "(无 h1)"
        cjk = len(re.findall(r"[\u4e00-\u9fff]", h1v))
        body_ok = any(m.lower() in dom.lower() for m in MARKERS[lang])
        data_residue = len(re.findall(r'data-(?:zh|en|fr|es|ja|ko)=', dom))
        # 中文根目录页本就用 data-* 属性驱动，只有语言子目录的生成页应为 0
        residue_ok = (data_residue == 0) if lang != "zh" else True
        ok = bool(t) and bool(h1) and body_ok and residue_ok
        if lang in ("en", "fr", "es") and cjk:
            ok = False
        print("   [%s] %s" % ("OK " if ok else "FAIL", lang))
        print("        title: %s" % title[:95])
        print("        h1   : %s" % h1v[:80])
        print("        正文特征词命中=%s  data-* 残留=%d  DOM=%d 字符"
              % (body_ok, data_residue, len(dom)))
        if not ok:
            fails.append((lang, slug, title, h1v, len(dom)))

print("== 2) 线上 sitemap 校验 ==")
ctx = ssl.create_default_context()
req = urllib.request.Request("https://taigetag.com/sitemap.xml",
                             headers={"User-Agent": "Mozilla/5.0 (verify)"})
try:
    sm = urllib.request.urlopen(req, timeout=45, context=ctx).read().decode("utf-8", "replace")
except Exception as e:
    sm = ""
    print("   直连失败，改用 curl：%s" % e)
    r = subprocess.run(["curl", "-s", "--noproxy", "*", "-A", "Mozilla/5.0 (verify)",
                        "https://taigetag.com/sitemap.xml"], capture_output=True, text=True,
                       encoding="utf-8", errors="replace")
    sm = r.stdout or ""
print("   线上 sitemap 长度: %d，<loc> 总数: %d" % (len(sm), sm.count("<loc>")))
for slug in SLUGS:
    for pre in ["blog/", "en/blog/", "ja/blog/", "ko/blog/", "fr/blog/", "es/blog/"]:
        u = "https://taigetag.com/%s%s" % (pre, slug)
        hit = ("<loc>%s</loc>" % u) in sm
        print("   %s %s" % ("OK  " if hit else "MISS", u))
        if not hit:
            fails.append(("sitemap", u, "", "", 0))

print("\n结论: 失败项 %d" % len(fails))
for f in fails:
    print("  ", f)
sys.exit(1 if fails else 0)
