#!/usr/bin/env python3
# -*- coding: utf-8 -*-
idx = open("blog/index.html", encoding="utf-8", newline="").read()
print("文件长度", len(idx))
g = idx.find('<div class="post-grid">')
print("grid 位置", g)
print("grid 后 160 字符:", repr(idx[g:g + 160]))
p = idx.find("woven-label-shrinkage-guide.html")
print("首个 slug 位置", p)
print("该处上下文:", repr(idx[p - 200:p + 60]))
print("第二个 slug 位置", idx.find("trim-measurement-tolerance-guide.html"))
print("窗口内是否都有:", "woven-label-shrinkage-guide.html" in idx[g:g + 6000],
      "trim-measurement-tolerance-guide.html" in idx[g:g + 6000])
print("两卡之间距离:", idx.find("trim-measurement-tolerance-guide.html") - p)
