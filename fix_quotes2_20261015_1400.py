#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把中文语境里的裸 ASCII 双引号（属性值内 / 文本节点内）替换为中文引号 “ ”
判定规则：紧邻中日韩字符或中文标点的 " 视为引号本体，按出现顺序奇偶配对。
属性分隔用的 " 前一位是 = 或空格/换行，后一位是空格/> 或换行，不会命中。
另：属性值内出现裸 ASCII 引号会被浏览器截断（移动端崩溃元凶），必须清零。
"""
import os, re, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)

HZ = r"[\u4e00-\u9fff\u3000-\u303f\uff00-\uffef]"
pat = re.compile(r'(?<=%s)"|"(?=%s)' % (HZ, HZ))


def fix(path):
    s = open(path, encoding="utf-8").read()
    pos = [m.start() for m in pat.finditer(s)]
    cnt = 0
    out = list(s)
    for p in pos:
        cnt += 1
        out[p] = "\u201c" if cnt % 2 else "\u201d"
    s2 = "".join(out)
    print("%s 命中裸引号 %d 个" % (os.path.basename(path), cnt))
    if cnt:
        open(path, "w", encoding="utf-8", newline="").write(s2)


for p in sys.argv[1:]:
    fix(p)
