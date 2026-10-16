#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""修正韩语正文中误用的汉字「袋」→ 순수 한글（포장 봉투）"""
import os
ROOT = os.path.dirname(os.path.abspath(__file__)); os.chdir(ROOT)
OLD = "행택, 직조 라벨, 케어 라벨, 포장袋를 만드는 공장은"
NEW = "행택, 직조 라벨, 케어 라벨, 포장 봉투를 만드는 공장은"
for p in ["blog/_body_minerals.html", "blog/conflict-minerals-trims-guide.html",
          "ko/blog/conflict-minerals-trims-guide.html"]:
    s = open(p, encoding="utf-8").read()
    n = s.count(OLD)
    if n != 1:
        print("!! %s 匹配 %d 次，跳过" % (p, n)); continue
    open(p, "w", encoding="utf-8", newline="").write(s.replace(OLD, NEW))
    print("已修正 %s" % p)
