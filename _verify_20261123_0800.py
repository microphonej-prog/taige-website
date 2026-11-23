# -*- coding: utf-8 -*-
"""校验两篇新文章：六语文件存在、hreflang 条数、noindex、中文残留、data-* 完整性。"""
import glob
import re

SLUGS = ["garment-label-adhesive-types-guide.html", "label-printer-printhead-maintenance-guide.html"]
PATHS = [""] + ["en/", "fr/", "es/", "ja/", "ko/"]

for slug in SLUGS:
    print("=" * 70)
    print(slug)
    for p in PATHS:
        f = "blog/" + slug if p == "" else p + "blog/" + slug
        try:
            s = open(f, encoding="utf-8").read()
        except FileNotFoundError:
            print("  MISSING", f)
            continue
        hl = len(re.findall(r'hreflang="[^"]+"', s))
        noidx = "noindex" in s
        # 可见中文残留（排除 title/meta 的 data-zh、JSON-LD、语言按钮、团队名）
        body = re.sub(r'<script.*?</script>|<style.*?</style>|<!--.*?-->', ' ', s, flags=re.S)
        cjk = [m.group(1).strip() for m in re.finditer(r'>([^<>]+)<', body)
               if re.search(r'[\u4e00-\u9fff]', m.group(1))]
        cjk = [c for c in cjk if len(c) > 1]
        langs = {}
        for l in ["zh", "en", "fr", "es", "ja", "ko"]:
            langs[l] = len(re.findall(r'data-%s="' % l, s))
        print("  %-4s %6d bytes  hreflang=%d noindex=%s  可见中文=%d  %s" %
              (p or "zh", len(s.encode("utf-8")), hl, noidx, len(cjk), langs))
        if cjk and p:
            print("      样例:", cjk[:4])
