#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-06 晚间批次：把两篇新文章的 meta description 收敛到规范长度
（中文 80-120 字、英文 150-160 字符），同步更新中文根页（繁体）与 en/ 语言页。
用法: F:/hermes/venvs/tools/Scripts/python.exe fix_desc_20261006_2000.py
"""
import re
from opencc import OpenCC

CC = OpenCC('s2t')

NEW = {
    "trim-metal-salt-spray-guide.html": dict(
        en="Metal trim rust guide: corrosion sources on buttons, snaps and sliders, plating choice by use, salt-spray 24/48/96 hours and its pass criteria.",
    ),
    "functional-garment-trims-label-guide.html": dict(
        zh="功能性服装辅料指南：讲清主唛、洗水标、吊牌与包装各自承担什么，抗菌（GB/T 20944.3）与防螨（GB/T 24253）声明需要哪些检测支撑，吸湿速干怎么写不越界，防紫外与无荧光纸品的要求，附询价验收清单。来自东莞泰阁包装。",
        en="Functional apparel trims guide: what each label and bag does, the tests behind antibacterial and anti-mite claims, wicking and UV wording, brightener-free paper.",
    ),
}


def fix_meta(s, zh=None, en=None):
    def repl(m):
        tag = m.group(0)
        if zh:
            tag = re.sub(r'(data-zh=")[^"]*(")', lambda x: x.group(1) + zh + x.group(2), tag, count=1)
            tag = re.sub(r'(content=")[^"]*(")', lambda x: x.group(1) + zh + x.group(2), tag, count=1)
        if en:
            tag = re.sub(r'(data-en=")[^"]*(")', lambda x: x.group(1) + en + x.group(2), tag, count=1)
        return tag
    return re.sub(r'<meta name="description".*?>', repl, s, count=1, flags=re.S)


for slug, v in NEW.items():
    zh_t = CC.convert(v["zh"]) if v.get("zh") else None
    root = "blog/" + slug
    s = open(root, encoding="utf-8").read()
    s2 = fix_meta(s, zh=zh_t, en=v.get("en"))
    open(root, "w", encoding="utf-8", newline="").write(s2)
    print("%-46s 根页 desc_zh=%s desc_en=%s" % (slug, len(zh_t) if zh_t else "-", len(v.get("en", "")) or "-"))

    en_path = "en/blog/" + slug
    if v.get("en"):
        s = open(en_path, encoding="utf-8").read()
        pat = re.compile(r'(<meta name="description" content=")[^"]*(")')
        s2, n = pat.subn(lambda m: m.group(1) + v["en"] + m.group(2), s, count=1)
        assert n == 1, "en 页面 desc 替换失败: %s" % en_path
        open(en_path, "w", encoding="utf-8", newline="").write(s2)
        print("%-46s en 页 desc 长度 %d" % (slug, len(v["en"])))
print("完成")
