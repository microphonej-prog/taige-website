# -*- coding: utf-8 -*-
"""线上验证：12 个新 URL 的 HTTP 状态 + title + 关键串；sitemap 是否含新 URL。"""
import re
import subprocess

SLUGS = ["clothing-tagging-gun-swift-tack-guide", "garment-label-font-size-legibility-guide"]
PREF = [("", "blog/"), ("en", "en/blog/"), ("fr", "fr/blog/"), ("es", "es/blog/"),
        ("ja", "ja/blog/"), ("ko", "ko/blog/")]
EXPECT = {
    "zh": "吊牌槍", "en": "Tagging gun", "fr": "Pistolet", "es": "pistola",
    "ja": "タグガン", "ko": "태깅",
}
TMP = "C:/Users/micro/AppData/Local/Temp/live_check.html"

for s in SLUGS:
    for lang, pre in PREF:
        url = "https://taigetag.com/%s%s.html" % (pre, s)
        for attempt in (1, 2):
            p = subprocess.run(["curl", "-s", "--max-time", "45", "-o", TMP, "-w", "%{http_code}", url],
                               capture_output=True, text=True)
            code = p.stdout.strip()
            if code == "200":
                break
        html_text = open(TMP, encoding="utf-8", errors="ignore").read() if code == "200" else ""
        m = re.search(r"<title[^>]*>(.*?)</title>", html_text, re.S)
        title = (m.group(1).strip()[:70] if m else "NO-TITLE")
        key = (EXPECT[lang or "zh"] if s == SLUGS[0] else ("字高" if lang in ("", "zh") else
              {"en": "type height", "fr": "hauteur", "es": "altura", "ja": "字高", "ko": "글자 높이"}[lang]))
        has_key = key.lower() in html_text.lower()
        print("%s %-6s %-52s title=%s | 关键串 '%s' %s"
              % (code, lang or "zh", s, title, key, "OK" if has_key else "MISS"))

# sitemap
p = subprocess.run(["curl", "-s", "--max-time", "45", "-o", TMP, "-w", "%{http_code}",
                    "https://taigetag.com/sitemap.xml"], capture_output=True, text=True)
sm = open(TMP, encoding="utf-8", errors="ignore").read()
print("\nsitemap HTTP %s  loc 总数 %d" % (p.stdout.strip(), sm.count("<loc>")))
for s in SLUGS:
    n = len(re.findall(r"<loc>https://taigetag\.com/(?:[a-z]{2}/)?blog/%s\.html</loc>" % s, sm))
    print("  线上 sitemap 含 %-50s %d/6" % (s, n))
