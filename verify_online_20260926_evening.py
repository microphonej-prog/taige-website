#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-09-26 晚间批次线上验证：
1) 轮询线上 sitemap.xml 直到含 2 篇新文章的全部 12 个 URL；
2) 无头 Chrome dump DOM → 校验 2 篇新文章 × 6 语言（zh/en/ja/ko/fr/es）title / h1 渲染；
3) curl 线上 js/main.js → BUST_VERSION = 113。
"""
import os, re, subprocess, sys, time

sys.stdout.reconfigure(encoding="utf-8")
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
TMP = os.path.join(os.environ["LOCALAPPDATA"], "Temp")
UDD = os.path.join(TMP, "chrome_evening_20260926")
os.chdir(TMP)

SLUGS = ["trim-tooling-ownership-guide.html", "trim-limit-sample-inspection-guide.html"]
LANGS = ["zh", "en", "ja", "ko", "fr", "es"]
BASE = "https://taigetag.com"
V = "113"

EXPECT = {
    ("trim-tooling-ownership-guide.html", "zh"): "版費",
    ("trim-tooling-ownership-guide.html", "en"): "Tooling Ownership",
    ("trim-tooling-ownership-guide.html", "ja"): "所有権",
    ("trim-tooling-ownership-guide.html", "ko"): "소유권",
    ("trim-tooling-ownership-guide.html", "fr"): "outillages",
    ("trim-tooling-ownership-guide.html", "es"): "utillajes",
    ("trim-limit-sample-inspection-guide.html", "zh"): "界限樣品",
    ("trim-limit-sample-inspection-guide.html", "en"): "Limit Samples",
    ("trim-limit-sample-inspection-guide.html", "ja"): "限界見本",
    ("trim-limit-sample-inspection-guide.html", "ko"): "한계 견본",
    ("trim-limit-sample-inspection-guide.html", "fr"): "Échantillons limites",
    ("trim-limit-sample-inspection-guide.html", "es"): "Muestras límite",
}


def url(slug, lang):
    return "%s/%sblog/%s?lang=%s&v=%s" % (BASE, "" if lang == "zh" else lang + "/", slug, lang, V)


sp = os.path.join(TMP, "sitemap_evening_20260926.xml")
sm = ""
deadline = time.time() + 300
while time.time() < deadline:
    subprocess.run(["curl", "-s", "--noproxy", "*", "-o", sp,
                    "%s/sitemap.xml?cb=%d" % (BASE, int(time.time()))], timeout=90)
    sm = open(sp, encoding="utf-8", errors="replace").read()
    if all(("<loc>%s/blog/%s</loc>" % (BASE, s)) in sm for s in SLUGS):
        print("线上 sitemap 已含 2 篇新文章（等待 %ds）" % int(300 - (deadline - time.time())))
        break
    time.sleep(15)
else:
    print("XX 等待超时：线上 sitemap 仍未见新文章")

print("== 1) 线上 sitemap.xml ==")
print("  行数 %d, <loc> 总数 %d" % (sm.count("\n"), sm.count("<loc>")))
miss = 0
for slug in SLUGS:
    for pre in ["blog/"] + ["%s/blog/" % l for l in ["en", "ja", "ko", "fr", "es"]]:
        u = "%s/%s%s" % (BASE, pre, slug)
        if "<loc>%s</loc>" % u not in sm:
            print("  XX 缺 %s" % u)
            miss += 1
print("  新 URL 缺失数 = %d（应为 0）" % miss)

print("== 2) 线上 DOM 渲染（无头 Chrome，六语） ==")
bad = 0
for slug in SLUGS:
    for lang in LANGS:
        out = "dom_evening_20260926_%s_%s.html" % (lang, slug.replace(".html", ""))
        if os.path.exists(out):
            os.remove(out)
        with open(out, "w", encoding="utf-8") as fh:
            subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-sandbox",
                            "--user-data-dir=" + UDD,
                            "--virtual-time-budget=15000", "--dump-dom", url(slug, lang)],
                           stdout=fh, stderr=subprocess.DEVNULL, timeout=120)
        s = open(out, encoding="utf-8", errors="replace").read()
        t = re.search(r"<title[^>]*>(.*?)</title>", s, re.S)
        h1 = re.search(r"<h1[^>]*>(.*?)</h1>", s, re.S)
        title = t.group(1).strip() if t else "-"
        h1v = re.sub(r"\s+", " ", h1.group(1)).strip() if h1 else "-"
        exp = EXPECT[(slug, lang)]
        hit = exp.lower() in (title + " " + h1v).lower()
        desc = re.search(r'<meta name="description" content="([^"]*)"', s)
        h2s = re.findall(r"<h2[^>]*>(.*?)</h2>", s, re.S)
        print("  %-38s %-3s 命中=%s h2数=%d desc=%d" %
              (slug.replace("-guide.html", ""), lang, "OK" if hit else "XX", len(h2s),
               len(desc.group(1)) if desc else -1))
        print("      title: %s" % title[:100])
        print("      h1   : %s" % h1v[:100])
        if not hit:
            bad += 1

print("== 3) 线上 js/main.js BUST_VERSION ==")
mj = os.path.join(TMP, "main_evening_20260926.js")
subprocess.run(["curl", "-s", "--noproxy", "*", "-o", mj,
                "%s/js/main.js?cb=%d" % (BASE, int(time.time()))], timeout=120)
js = open(mj, encoding="utf-8", errors="replace").read()
m = re.search(r'var BUST_VERSION = "([^"]*)"', js)
print("  线上 BUST_VERSION = %s %s" % (m.group(1) if m else "?", "OK" if (m and m.group(1) == V) else "XX"))

print("\n结论: DOM 未命中 %d，sitemap 缺失 %d，BUST_VERSION=%s"
      % (bad, miss, m.group(1) if m else "?"))
sys.exit(1 if (bad or miss or not (m and m.group(1) == V)) else 0)
