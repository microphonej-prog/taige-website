#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-10 晚间批次：正文文件（六语属性）预检
- 每个带 data-zh 的元素必须同时有 data-en / data-ja / data-ko / data-fr / data-es
- 属性值不得为空、首尾不得残留引号（移动端 WebKit 崩溃元凶 = 引号嵌套）
用法: F:/hermes/venvs/tools/Scripts/python.exe precheck_bodies_20261010_2300.py
"""
import sys
from html.parser import HTMLParser

LANGS = ["en", "ja", "ko", "fr", "es"]
FILES = ["blog/_body_uflpa.html", "blog/_body_carton.html"]


class Collector(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.tags = []
        self.attrs_seen = []

    def handle_starttag(self, tag, attrs):
        d = {}
        for k, v in attrs:
            if k.startswith("data-"):
                self.attrs_seen.append((k, v, self.getpos()[0]))
            d[k] = v
        self.tags.append((tag, d, self.getpos()[0]))


def main():
    problems = 0
    for path in FILES:
        src = open(path, encoding="utf-8").read()
        p = Collector()
        p.feed(src)
        p.close()

        for k, v, ln in p.attrs_seen:
            if v is None:
                print("  [空属性] %s:%d %s=None" % (path, ln, k))
                problems += 1
            elif v == "" or v.startswith('"') or v.endswith('"'):
                print("  [可疑引号] %s:%d %s=%r" % (path, ln, k, v[:40]))
                problems += 1

        n_zh = n_missing = 0
        for tag, d, ln in p.tags:
            if "data-zh" not in d:
                continue
            n_zh += 1
            miss = [l for l in LANGS if ("data-%s" % l) not in d]
            if miss:
                n_missing += 1
                print("  [缺语] %s:%d <%s> 缺 %s | %s" % (path, ln, tag, ",".join(miss), (d["data-zh"] or "")[:40]))
                problems += 1
        if '=""' in src:
            print("  [空值双引号] %s 存在 =\"\" " % path)
            problems += 1

        # 表格列数一致性
        import re
        for ti, tb in enumerate(re.findall(r'<table.*?</table>', src, re.S), 1):
            rows = re.findall(r'<tr>(.*?)</tr>', tb, re.S)
            counts = [len(re.findall(r'<(?:th|td)\b', r)) for r in rows]
            print("  表 %d：%d 行，各行列数 %s %s" % (ti, len(rows), counts, "OK" if len(set(counts)) == 1 else "!! 列数不一致"))
            if len(set(counts)) != 1:
                problems += 1

        # 正文中文元素数 & 中文正文规模
        zh_chars = 0
        for tag, d, ln in p.tags:
            if "data-zh" in d and d.get("data-zh"):
                zh_chars += len(d["data-zh"])
        print("%s: 正文元素 %d，缺语 %d，中文可见文本约 %d 字" % (path, n_zh, n_missing, zh_chars))

    print("体检结束，问题数 =", problems)
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
