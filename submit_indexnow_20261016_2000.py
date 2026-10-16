import json, subprocess
SLUGS = ["trim-shipment-insurance-claims-guide.html", "conflict-minerals-trims-guide.html"]
LANGS = ["", "en/", "ja/", "ko/", "fr/", "es/"]
urls = ["https://taigetag.com/%sblog/%s" % (l, s) for s in SLUGS for l in LANGS]
urls += ["https://taigetag.com/%sblog/index.html" % l for l in LANGS]
body = {"host": "taigetag.com", "key": "IMPLQzV8ZJL3XT7alCYPLLhxLidYNlkc",
        "keyLocation": "https://taigetag.com/IMPLQzV8ZJL3XT7alCYPLLhxLidYNlkc.txt", "urlList": urls}
p = "C:/Users/micro/taige-website/_indexnow_2000.json"
open(p, "w", encoding="utf-8").write(json.dumps(body))
r = subprocess.run(["curl", "-sS", "--noproxy", "*", "-X", "POST", "https://api.indexnow.org/indexnow",
                    "-H", "Content-Type: application/json; charset=utf-8", "-d", "@" + p,
                    "-o", "-", "-w", "\nIndexNow HTTP %{http_code}"], capture_output=True, text=True, timeout=120)
print("提交 URL 数:", len(urls))
for u in urls:
    print("  ", u)
print(r.stdout.strip()[-600:])
print(r.stderr.strip()[:200])
