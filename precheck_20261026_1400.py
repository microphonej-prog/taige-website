import re
for lang, pat, name in (("ja", r"[\u3040-\u30ff]", "かな/カナ"), ("ko", r"[\uac00-\ud7af]", "ハングル")):
    for slug in ("care-label-fold-types.html", "hang-tag-multilingual-printing-guide.html"):
        s = open("%s/blog/%s" % (lang, slug), encoding="utf-8").read()
        body = s[s.index('class="article-body"'):s.index("\n</main>")]
        txt = re.sub(r"<script.*?</script>", "", body, flags=re.S)
        txt = re.sub(r"<[^>]+>", "", txt)
        print("%s %-42s %s=%d 汉字=%d" % (lang, slug[:40], name, len(re.findall(pat, txt)),
                                          len(re.findall(r"[\u4e00-\u9fff]", txt))))
