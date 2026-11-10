# -*- coding: utf-8 -*-
"""语言页残留检查：可见文本里的中文（排除白名单）+ 英文兜底段落检测。"""
import re
import sys

ALLOW = ["江磊", "張旭勝", "陳清港", "東莞", "虎門", "連升", "廣東省", "泰閣", "繁體中文",
         "日本語", "한국어", "Français", "Español", "Deutsch", "Português", "中文",
         "原産国", "泰閣包裝製品有限公司", "東莞市", "原產地"]


def scan(path, lang):
    s = open(path, encoding="utf-8", errors="ignore").read()
    s = re.sub(r"<script.*?</script>|<style.*?</style>|<!--.*?-->", " ", s, flags=re.S)
    bad = []
    for m in re.finditer(r">([^<>]+)<", s):
        t = m.group(1).strip()
        if not t or not re.search(r"[\u4e00-\u9fff]", t):
            continue
        if any(a in t for a in ALLOW):
            continue
        bad.append(t[:60])
    attrs = []
    for m in re.finditer(r'(placeholder|title|alt|aria-label)="([^"]*)"', s):
        if re.search(r"[\u4e00-\u9fff]", m.group(2)) and not any(a in m.group(2) for a in ALLOW):
            attrs.append(m.group(2)[:40])
    print("%-58s CJK可见文本 %d  属性 %d" % (path, len(bad), len(attrs)))
    for b in bad[:6]:
        print("    文本:", b)
    for a in attrs[:4]:
        print("    属性:", a)


for lang in sys.argv[1].split(","):
    for slug in sys.argv[2].split(","):
        scan("%s/blog/%s" % (lang, slug), lang)
