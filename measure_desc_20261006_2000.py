import re, glob, os
def desc(path, attr="zh"):
    s = open(path, encoding="utf-8").read()
    m = re.search(r'<meta name="description"[^>]*data-%s="([^"]*)"' % attr, s, re.S)
    if m: return len(m.group(1))
    m = re.search(r'<meta name="description" content="([^"]*)"', s, re.S)
    return len(m.group(1)) if m else -1
files = sorted(glob.glob("blog/*.html"), key=os.path.getmtime)[-19:]
zhs=[]; ens=[]
for f in files:
    if "_body" in f or f.endswith("index.html"): continue
    z=desc(f,"zh"); zhs.append(z)
    ens.append(desc("en/"+f,"en") if os.path.exists("en/"+f) else -1)
    print("%-50s zh=%s en=%s" % (os.path.basename(f), z, ens[-1]))
zhs=[z for z in zhs if z>0]; ens=[e for e in ens if e>0]
print("zh 长度范围 %d-%d 均值 %.0f ; en 范围 %d-%d 均值 %.0f" % (min(zhs),max(zhs),sum(zhs)/len(zhs),min(ens),max(ens),sum(ens)/len(ens)))
