# -*- coding: utf-8 -*-
import re, io, os, glob
d = "F:/hermes/cache/scratch/live1026"
for f in sorted(glob.glob(d + "/*.html")):
    s = io.open(f, encoding="utf-8", errors="replace").read()
    t = re.search(r"<title[^>]*>(.*?)</title>", s, re.S)
    title = t.group(1).strip() if t else "(no title)"
    h1 = re.search(r"<h1[^>]*>(.*?)</h1>", s, re.S)
    h1t = re.sub(r"<[^>]+>", "", h1.group(1)).strip() if h1 else "(no h1)"
    body = s[s.index('class="article-body"'):] if 'class="article-body"' in s else ""
    txt = re.sub(r"<script.*?</script>", " ", body, flags=re.S)
    txt = re.sub(r"<[^>]+>", " ", txt)
    cjk = len(re.findall(r"[\u4e00-\u9fff]", txt))
    kana = len(re.findall(r"[\u3040-\u30ff]", txt))
    han = len(re.findall(r"[\uac00-\ud7af]", txt))
    print("%-58s\n   title: %s\n   h1   : %s\n   汉字=%d かな=%d 한글=%d 长度=%d"
          % (os.path.basename(f)[:-5], title[:95], h1t[:95], cjk, kana, han, len(txt)))
