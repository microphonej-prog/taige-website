import json, subprocess
KEY="IMPLQzV8ZJL3XT7alCYPLLhxLidYNlkc"
slugs=["magnetic-trims-air-freight-guide.html","trim-label-consistency-audit-guide.html"]
urls=[]
for s in slugs:
    urls.append("https://taigetag.com/blog/%s"%s)
    for l in ["en","ja","ko","fr","es"]:
        urls.append("https://taigetag.com/%s/blog/%s"%(l,s))
payload={"host":"taigetag.com","key":KEY,"keyLocation":"https://taigetag.com/%s.txt"%KEY,"urlList":urls}
open("indexnow_20261022.json","w",encoding="utf-8").write(json.dumps(payload))
r=subprocess.run(["curl","-sS","--noproxy","*","-m","40","-X","POST","https://api.indexnow.org/indexnow",
                  "-H","Content-Type: application/json; charset=utf-8","-d","@indexnow_20261022.json",
                  "-w","\nHTTP %{http_code}\n"],capture_output=True)
print(r.stdout.decode("utf-8","replace"), r.stderr.decode("utf-8","replace"))
print("提交 URL 数:", len(urls))
