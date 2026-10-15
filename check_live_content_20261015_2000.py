import subprocess, re, os
LANGS=["","en/","ja/","ko/","fr/","es/"]
for slug in ["trim-color-migration-staining-guide.html","trim-light-fastness-fading-guide.html"]:
    for l in LANGS:
        lp="%sblog/%s"%(l,slug)
        local=open(lp,encoding='utf-8').read()
        loc_h2=len(re.findall(r'<h2',local)); loc_cta='cta-btn' in local
        loc_end=re.search(r'<a class="cta-btn"[^>]*>([^<]*)',local)
        r=subprocess.run(["curl","-sS","--noproxy","*","-o","-","https://taigetag.com/%sblog/%s?v=161"%(l,slug)],capture_output=True,text=True,encoding='utf-8',errors='replace',timeout=120)
        on=r.stdout
        on_h2=len(re.findall(r'<h2',on)); on_cta='cta-btn' in on
        on_end=re.search(r'<a class="cta-btn"[^>]*>([^<]*)',on)
        print("%-58s 本地 %6d / 线上 %6d  h2 %d/%d  cta %s/%s  %s" % (
            l+slug, len(local.encode()), len(on.encode()), loc_h2, on_h2, loc_cta, on_cta,
            "OK" if (on_h2==loc_h2 and on_cta==loc_cta and (on_end.group(1).strip() if on_end else "")==(loc_end.group(1).strip() if loc_end else "")) else "MISMATCH"))
        if on_end and loc_end and on_end.group(1).strip()!=loc_end.group(1).strip():
            print("      线上CTA:",on_end.group(1).strip()[:60],"| 本地CTA:",loc_end.group(1).strip()[:60])
