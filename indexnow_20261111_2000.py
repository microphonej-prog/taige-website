import json, urllib.request
KEY = "IMPLQzV8ZJL3XT7alCYPLLhxLidYNlkc"
SL = ["plastic-hardware-trims-guide.html", "industrial-laundry-care-label-guide.html"]
LANGS = ["en","fr","es","ja","ko","de","pt"]
urls = ["https://taigetag.com/blog/%s" % s for s in SL] + \
       ["https://taigetag.com/%s/blog/%s" % (l, s) for s in SL for l in LANGS] + \
       ["https://taigetag.com/blog/index.html"] + \
       ["https://taigetag.com/%s/blog/index.html" % l for l in LANGS]
payload = {"host": "taigetag.com", "key": KEY,
           "keyLocation": "https://taigetag.com/%s.txt" % KEY, "urlList": urls}
req = urllib.request.Request("https://api.indexnow.org/indexnow",
    data=json.dumps(payload).encode(), headers={"Content-Type": "application/json; charset=utf-8"})
try:
    r = urllib.request.urlopen(req, timeout=60)
    print("IndexNow HTTP", r.status, "| URL 数", len(urls))
except Exception as e:
    print("IndexNow 失败:", e)
