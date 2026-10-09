#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-09 晚间批次：正文文件（六语属性）预检
- 每个带 data-zh 的元素必须同时有 data-en / data-ja / data-ko / data-fr / data-es
- 属性值不得为空、首尾不得残留引号（移动端 WebKit 崩溃元凶 = 引号嵌套）
- 统计正文元素数，报告缺失清单
用法: F:/hermes/venvs/tools/Scripts/python.exe precheck_bodies_20261009_2000.py
"""
import sys
from html.parser import HTMLParser

LANGS = ["en", "ja", "ko", "fr", "es"]
FILES = ["blog/_body_plus.html", "blog/_body_hanger.html"]


class Collector(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.tags = []      # (tag, attrs dict, lineno)
        self.attrs_seen = []  # all data-* values with line numbers

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

        # 1) 空属性 / 残留引号
        for k, v, ln in p.attrs_seen:
            if v is None:
                print("  [空属性] %s:%d %s=None" % (path, ln, k))
                problems += 1
            elif v == "" or v.startswith('"') or v.endswith('"'):
                print("  [可疑引号] %s:%d %s=%r" % (path, ln, k, v[:40]))
                problems += 1

        # 2) 六语属性完整性（只针对正文元素）
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
        # 相邻双引号（data-x="" 的经典崩溃形态）
        if '=""' in src:
            print("  [空值双引号] %s 存在 =\"\" " % path)
            problems += 1

        print("%s: 正文元素 %d，缺语 %d" % (path, n_zh, n_missing))

    print("体检结束，问题数 =", problems)
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
