import re, os
files = ["blog/vacuum-compression-apparel-packaging.html", "blog/stone-paper-hang-tags-guide.html",
         "blog/heat-transfer-labels.html", "blog/woven-label-density-guide.html"]
for f in files:
    if not os.path.exists(f):
        print("missing", f); continue
    s = open(f, encoding='utf-8').read()
    m = re.search(r'<meta name="description"[^>]*>', s, re.S)
    d = m.group(0)
    vals = re.findall(r'(data-[a-z]{2})="([^"]*)"', d)
    print(f)
    for k, v in vals:
        print("   %s=%d" % (k, len(v)))
