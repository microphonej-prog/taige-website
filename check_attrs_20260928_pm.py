#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""校验每日文章正文的六语 data-* 覆盖度与属性安全（2026-09-28 下午批次）。

用 HTMLParser 解析（属性值里含 <strong> 等标签，正则不可靠），检查：
1) .article-body 容器内每个带 data-zh 的元素，是否同时有 data-en/ja/ko/fr/es
2) 是否有非法属性形态（data-xx="" 空值、属性值内裸双引号导致的解析异常）
3) 正文中文可见字数（data-zh 合计）
用法: <python> check_attrs_20260928_pm.py
"""
import sys, re
from html.parser import HTMLParser

sys.stdout.reconfigure(encoding="utf-8")
FILES = ["blog/_body_origin.html", "blog/_body_pp.html"]
LANGS = ["en", "ja", "ko", "fr", "es"]


class Collector(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.tags = []          # (tagname, dict(attrs))
        self.bad_quotes = []

    def handle_starttag(self, tag, attrs):
        d = {}
        for k, v in attrs:
            d[k] = v
            if v is None:
                self.bad_quotes.append((tag, k))
        self.tags.append((tag, d))

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)


ok = True
for f in FILES:
    s = open(f, encoding="utf-8").read()
    # 属性值里的裸双引号 / 引号嵌套异常（移动端 WebKit 崩溃元凶）
    nest = re.findall(r'data-(?:zh|en|ja|ko|fr|es)="[^"]*"[^"\s=/>]+"', s)
    empty = re.findall(r'data-(?:zh|en|ja|ko|fr|es)=""', s)
    c = Collector()
    c.feed(s)
    zh_tags = [(t, d) for t, d in c.tags if "data-zh" in d]
    missing = []
    for t, d in zh_tags:
        lack = [l for l in LANGS if ("data-%s" % l) not in d]
        if lack:
            missing.append((t, lack, (d.get("data-zh") or "")[:30]))
    zh_chars = sum(len(re.findall(r"[\u4e00-\u9fff]", d.get("data-zh") or "")) for _, d in zh_tags)
    # data-zh 值里出现繁体特有字（说明正文误写繁体，简体源应为简体）
    trad = sum(1 for _, d in zh_tags if re.search(r"[們這說個麼與體標籤產樣]",
                                                   d.get("data-zh") or ""))
    print("%s：含 data-zh 元素 %d 个，缺语言属性 %d 处，中文正文字数(近似) %d"
          % (f, len(zh_tags), len(missing), zh_chars))
    if nest:
        print("  !! 引号嵌套可疑 %d 处：%s" % (len(nest), nest[:3]))
        ok = False
    if empty:
        print("  !! 空属性值 %d 处" % len(empty))
        ok = False
    for t, lack, txt in missing[:12]:
        print("  !! <%s> 缺 %s — %s" % (t, ",".join(lack), txt))
    if missing:
        ok = False
    if trad:
        print("  ~ 疑似繁体字符元素 %d 处（data-zh 源应为简体，root 页由脚本转繁）" % trad)

print("结果：%s" % ("全部通过" if ok else "存在问题，需修复"))
