# -*- coding: utf-8 -*-
"""只把指定 HTML 的 data-zh / 中文文本转繁（不动 js/main.js，避免 s2t 反复改写已有繁体）。"""
import sys

sys.argv = ["conv"]

import to_traditional as TT  # noqa: E402

for f in ["blog/apparel-size-designation-en-13402.html", "blog/silicone-gripper-tape-guide.html"]:
    s0 = open(f, encoding="utf-8").read()
    s = TT.convert_html(s0)
    if s != s0:
        open(f, "w", encoding="utf-8", newline="").write(s)
        print("转换繁体:", f, "变化", len(s) - len(s0))
    else:
        print("无需转换:", f)
print("统计:", TT.STATS)
