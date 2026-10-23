# -*- coding: utf-8 -*-
"""检查各语言版本正文是否残留中文（兜底翻译检查）。"""
import re
SLUGS = ["fsc-certified-hang-tags.html", "apparel-trims-rush-order-guide.html"]
CJK = re.compile(r"[\u4e00-\u9fff]")
for slug in SLUGS:
    for lang in ["en", "ja", "ko", "fr", "es"]:
        p = "%s/blog/%s" % (lang, slug)
        s = open(p, encoding="utf-8").read()
        i0 = s.index('<section class="article-body">')
        i1 = s.index("\n</main>")
        body = s[i0:i1]
        cjk = CJK.findall(body)
        # 允许的品牌/地址中文（JSON-LD 不在 body 内）
        print("%-6s %-42s CJK 字符 %d %s" % (lang, slug, len(cjk), "".join(cjk[:12])))
        # 抽一段正文首句
        m = re.search(r"<p>(.{0,90})", body, re.S)
        print("        首句:", m.group(1).replace("\n", " ")[:88])
