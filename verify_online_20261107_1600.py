# -*- coding: utf-8 -*-
"""线上校验：两篇新文六语 title 渲染 + sitemap 收录 + BUST 生效。"""
import subprocess, re, sys, os, tempfile

CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
SLUGS = ["clothing-label-compliance-central-america.html",
         "clothing-label-compliance-morocco-tunisia.html"]
PREFIX = {"zh": "", "en": "en/", "ja": "ja/", "ko": "ko/", "fr": "fr/", "es": "es/"}
ok = True

for slug in SLUGS:
    for lang, pre in PREFIX.items():
        url = "https://taigetag.com/%sblog/%s?lang=%s&v=203" % (pre, slug, lang)
        r = subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-sandbox",
                            "--virtual-time-budget=12000", "--dump-dom", url],
                           capture_output=True, timeout=120)
        dom = r.stdout.decode("utf-8", "ignore")
        m = re.search(r"<title>(.*?)</title>", dom, re.S)
        h = re.search(r"<h1[^>]*>(.*?)</h1>", dom, re.S)
        title = m.group(1).strip() if m else "(无 title)"
        h1 = re.sub(r"<[^>]+>", "", h.group(1)).strip() if h else "(无 h1)"
        flag = "OK " if title and "TAGE" in title else "BAD"
        if flag == "BAD":
            ok = False
        print("%s %-46s %s" % (flag, "%s blog/%s" % (lang, slug[:34]), title[:64]))
        print("        h1:", h1[:60])

print("\n--- sitemap.xml 线上 ---")
r = subprocess.run(["curl", "-s", "--noproxy", "*", "--max-time", "30",
                    "https://taigetag.com/sitemap.xml"], capture_output=True)
sm = r.stdout.decode("utf-8", "ignore")
print("sitemap 大小:", len(sm), "字节, <loc> 数:", sm.count("<loc>"))
for slug in SLUGS:
    n = len(re.findall(r"<loc>([^<]*%s)</loc>" % re.escape(slug), sm))
    print("  %s -> %d 条 URL" % (slug, n))
    if n != 6:
        ok = False

print("\n--- 新文线上 HTTP ---")
for slug in SLUGS:
    for pre in ["", "en/", "ja/", "ko/", "fr/", "es/"]:
        u = "https://taigetag.com/%sblog/%s" % (pre, slug)
        c = subprocess.run(["curl", "-s", "-o", "NUL", "-w", "%{http_code}", "--noproxy", "*",
                            "--max-time", "30", u], capture_output=True).stdout.decode()
        if c.strip() != "200":
            ok = False
            print("  BAD", c, u)
print("HTTP 全 200" if ok else "存在非 200")
print("RESULT:", "PASS" if ok else "FAIL")
