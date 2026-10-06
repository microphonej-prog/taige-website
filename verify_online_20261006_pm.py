#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-06 下午批次线上验证：无头 Chrome 抽 DOM 标题（六语）+ 线上 sitemap 含新 URL。"""
import re, subprocess, os, sys, time, urllib.request, socket

CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
SLUGS = ["sequin-rhinestone-trims-guide.html", "rib-knit-collar-cuff-guide.html"]
LANGS = ["zh", "en", "ja", "ko", "fr", "es"]

TMP = os.environ.get("TMPDIR", r"F:\hermes\cache\scratch").replace("\\", "/")
os.makedirs(TMP, exist_ok=True)


def dump(url, out):
    cmd = [CHROME, "--headless=new", "--disable-gpu", "--no-sandbox",
           "--virtual-time-budget=12000", "--dump-dom", url]
    with open(out, "w", encoding="utf-8", errors="replace") as f:
        subprocess.run(cmd, stdout=f, stderr=subprocess.DEVNULL, timeout=180)
    return open(out, encoding="utf-8", errors="replace").read()


print("== A) 线上页面六语标题（无头 Chrome 渲染后 DOM） ==")
bad = 0
for slug in SLUGS:
    for lang in LANGS:
        if lang == "zh":
            url = "https://taigetag.com/blog/%s?lang=zh&v=1" % slug
        else:
            url = "https://taigetag.com/%s/blog/%s?lang=%s&v=1" % (lang, slug, lang)
        out = os.path.join(TMP, "dom_%s_%s.html" % (slug.split(".")[0][:18], lang))
        try:
            html = dump(url, out)
        except Exception as e:
            print("  ERR  %-58s %s" % (url, e)); bad += 1; continue
        m = re.search(r'<title[^>]*>(.*?)</title>', html, re.S)
        title = m.group(1).strip() if m else "NONE"
        h1 = re.search(r'<h1[^>]*>(.*?)</h1>', html, re.S)
        h1t = re.sub(r'<[^>]+>', '', h1.group(1)).strip() if h1 else "NONE"
        b = re.search(r'<section class="article-body">', html)
        ok = (title != "NONE") and (h1t != "NONE") and b
        if not ok:
            bad += 1
        print("  %-4s %-44s ok=%s" % (lang, slug, ok))
        print("       title: %s" % title[:88])
        print("       h1   : %s" % h1t[:88])

print("\n== B) 线上 sitemap.xml 含 2 个新 URL（六语各 1 条） ==")
sm = ""
for attempt in range(3):
    try:
        req = urllib.request.Request("https://taigetag.com/sitemap.xml?nocache=%d" % int(time.time()),
                                    headers={"User-Agent": "Mozilla/5.0"})
        sm = urllib.request.urlopen(req, timeout=60).read().decode("utf-8", "replace")
        break
    except Exception as e:
        print("  重试 %d: %s" % (attempt + 1, e)); time.sleep(10)
if not sm:
    print("  FAIL 无法获取线上 sitemap"); bad += 1
else:
    print("  线上 sitemap 字节数 %d ; <loc> 总数 %d" % (len(sm.encode("utf-8")), sm.count("<loc>")))
    for slug in SLUGS:
        for pre in ("blog/", "en/blog/", "ja/blog/", "ko/blog/", "fr/blog/", "es/blog/"):
            u = "https://taigetag.com/%s%s" % (pre, slug)
            hit = ("<loc>%s</loc>" % u) in sm
            if not hit:
                bad += 1
            print("  %-6s %s %s" % (pre, "OK " if hit else "MISS", u))

print("\n结论: %s" % ("有 %d 处异常" % bad if bad else "线上验证全部通过"))
sys.exit(1 if bad else 0)
