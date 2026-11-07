# -*- coding: utf-8 -*-
"""扫描 ja 页面正文中残留的简体字（日语不使用简体字形）并给出上下文。"""
import os, re
os.chdir(os.path.dirname(os.path.abspath(__file__)))
SIMP = set("语说时间发现标签证货单价质纸带丝织卫读请让认识规则术专业务东车马鸟鱼龙长门问关组对个别么为与从来里后头买卖学习见观电话编号转输边页显发达运进连结选适应该")
SLUGS = ["clothing-label-compliance-central-america.html",
         "clothing-label-compliance-morocco-tunisia.html"]
for slug in SLUGS:
    s = open("ja/blog/" + slug, encoding="utf-8").read()
    body = s[s.index('<section class="article-body">'):]
    found = []
    for m in re.finditer(r"[^<>\n]{0,22}[%s][^<>\n]{0,22}" % "".join(sorted(SIMP)), body):
        found.append(m.group(0).strip())
    print("%s: %d 处" % (slug, len(found)))
    for f in found[:12]:
        print("   ", f[:90])
