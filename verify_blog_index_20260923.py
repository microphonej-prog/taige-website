import subprocess, os, time, re, sys
sys.stdout.reconfigure(encoding='utf-8')
TMP = os.path.join(os.environ["LOCALAPPDATA"], "Temp")
out = os.path.join(TMP, "idx_20260923.html")
for lang in ["zh", "en", "ja", "ko", "fr", "es"]:
    u = "https://taigetag.com/%sblog/index.html?lang=%s&v=102" % ("" if lang == "zh" else lang + "/", lang)
    subprocess.run(["curl", "-s", "--noproxy", "*", "-o", out, u], timeout=90)
    s = open(out, encoding="utf-8", errors="replace").read()
    hit = [x for x in ("paper-bag-window-guide.html", "trims-kitting-guide.html") if x in s]
    print("%-3s blog/index.html 新卡片命中 %d/2 %s  (字节 %d)" % (lang, len(hit), hit, len(s)))
