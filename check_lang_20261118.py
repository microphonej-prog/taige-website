# -*- coding: utf-8 -*-
"""语言页检查：hreflang 条数、noindex、canonical、中文残留、内链与路径。"""
import glob
import os
import re

SLUGS = ["care-label-fiber-content-tolerance-guide", "trim-test-report-reading-guide"]
FILES = []
for s in SLUGS:
    FILES.append("blog/%s.html" % s)
    for l in ["en", "fr", "es", "ja", "ko"]:
        FILES.append("%s/blog/%s.html" % (l, s))

CJK = re.compile(r"[\u4e00-\u9fff]")
OK_CJK = ("江磊", "吳文潘", "陳清港", "繁體中文", "日本語", "한국어", "台灣", "虎門", "東莞", "泰閣", "原産国：中国")

for f in FILES:
    if not os.path.isfile(f):
        print("MISSING", f)
        continue
    s = open(f, encoding="utf-8").read()
    hl = re.findall(r'hreflang="([^"]+)"', s)
    noidx = "noindex" in s.lower()
    canon = re.search(r'<link rel="canonical" href="([^"]*)"', s).group(1)
    title = re.search(r"<title[^>]*>(.*?)</title>", s, re.S).group(1)
    # 正文中文残留（去 script/style/注释、去 data-* 属性与 JSON-LD）
    body = re.search(r'<section class="article-body">(.*?)</main>', s, re.S).group(1)
    body = re.sub(r"<script.*?</script>|<style.*?</style>", " ", body, flags=re.S)
    body = re.sub(r'data-(?:zh|en|fr|es|ja|ko)="[^"]*"', " ", body)
    body = re.sub(r"<[^>]+>", " ", body)
    cn = [m.group(0) for m in CJK.finditer(body)]
    print("%-58s hl=%d noindex=%s canon=%s" % (f, len(hl), noidx, canon.replace("https://taigetag.com", "")))
    print("   title: %s" % title[:70])
    if cn:
        ctx = body[max(0, body.find("".join(cn[:3])) - 30):body.find("".join(cn[:3])) + 40]
        print("   正文中文残留 %d 字: ...%s..." % (len(cn), ctx.strip().replace("\n", " ")))
