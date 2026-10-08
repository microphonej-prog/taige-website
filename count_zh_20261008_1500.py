#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""统计两篇新文章中文正文规模（可见文本汉字数）与四/六语属性元素数。"""
import os, re
os.chdir(os.path.dirname(os.path.abspath(__file__)))
for s in ["wooden-bamboo-hang-tags.html", "print-on-demand-apparel-labels.html"]:
    html = open("blog/%s" % s, encoding="utf-8").read()
    body = html[html.index('<section class="article-body">'):html.index("</main>")]
    vis = re.sub(r"<[^>]+>", "", re.sub(r'data-[a-z]+="[^"]*"', "", body))
    zh = len(re.findall(r"[\u4e00-\u9fff]", vis))
    print("%-42s 正文汉字 %d 字 ; h2 %d ; table %d ; li %d ; 六语属性元素 %d"
          % (s, zh, body.count("<h2 "), body.count("<table>"),
             body.count("<li"), len(re.findall(r'data-zh="', body))))
