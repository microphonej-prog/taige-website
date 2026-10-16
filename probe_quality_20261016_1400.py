#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""针对性检查：ja 值中的简体字黑名单 + 结构完整性"""
import re
SIMPLIFIED_BLACK = "设计缝标签务难应图过这个时关键认语护纸张线记录备边处数板样顺试检运质量颜结构优势变更风险温湿贴牌额定数量编织袋胶类级设备项"


def vals(src, lang):
    return re.findall(r'data-%s="([^"]*)"' % lang, src)


for f in ["blog/adaptive-accessible-clothing-trims-guide.html",
          "blog/modest-wear-hijab-trims-guide.html"]:
    s = open(f, encoding="utf-8").read()
    print("=== %s ===" % f)
    for lang in ("ja", "ko", "fr", "es"):
        hit = {}
        for v in vals(s, lang):
            for ch in v:
                if ch in SIMPLIFIED_BLACK:
                    hit.setdefault(ch, 0)
                    hit[ch] += 1
        print("  %s 黑名单命中: %s" % (lang, hit or "无"))
    # 结构
    i0 = s.index('class="article-body"')
    body = s[i0:s.index("</main>")]
    print("  h2=%d h3=%d p=%d li=%d table=%d td/th=%d a=%d|cta=%s" % (
        body.count("<h2"), body.count("<h3"), body.count("<p "), body.count("<li"),
        body.count("<table"), body.count("<td"), body.count("<a "),
        "有" if "cta-box" in body else "无"))
    # 属性引号畸形检查
    bad = re.findall(r'data-(?:zh|en|ja|ko|fr|es)=""', body)
    print("  空/畸形属性:", len(bad))
    print("  中文正文（去标签）字数:", len(re.findall(r"[\u4e00-\u9fff]", re.sub(r"<[^>]+>", "", body))))
