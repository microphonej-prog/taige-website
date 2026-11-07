#!/usr/bin/env python
"""把 Cloudflare Web Analytics 的 beacon 脚本注入所有 HTML 页（幂等）。

用法：
    python add_cf_analytics.py --token <CF_TOKEN>          # 实际写入
    python add_cf_analytics.py --token <CF_TOKEN> --dry-run # 只统计
    python add_cf_analytics.py --remove                    # 撤掉（回滚用）

规则：
- 插在 </head> 之前；已含 cloudflareinsights 的文件跳过（幂等）。
- 中文源页与各语言生成页都会注入；gen_i18n.py 以中文页为源、head 原样带过去，
  所以以后新生成的语言页会自动继承这段脚本。
"""
import argparse
import glob
import os
import sys

SNIPPET_TMPL = (
    '<script defer src="https://static.cloudflareinsights.com/beacon.min.js" '
    "data-cf-beacon='{{\"token\": \"{token}\"}}'></script>\n"
)
MARK = "cloudflareinsights"


def html_files():
    files = []
    files += sorted(glob.glob("*.html"))
    for d in ("blog", "en", "fr", "es", "ja", "ko"):
        files += sorted(glob.glob(os.path.join(d, "*.html")))
        files += sorted(glob.glob(os.path.join(d, "blog", "*.html")))
    return [f for f in files if os.path.isfile(f)]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--token", default="")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--remove", action="store_true")
    a = ap.parse_args()

    if not a.remove and not a.token:
        sys.exit("需要 --token（或 --remove）")

    files = html_files()
    added = skipped = removed = nohead = 0
    for f in files:
        try:
            s = open(f, encoding="utf-8", errors="ignore").read()
        except OSError:
            continue
        if a.remove:
            if MARK in s:
                import re
                s2 = re.sub(r'<script[^>]*cloudflareinsights[^>]*></script>\s*\n?', "", s)
                if s2 != s:
                    removed += 1
                    if not a.dry_run:
                        open(f, "w", encoding="utf-8", newline="").write(s2)
            continue
        if MARK in s:
            skipped += 1
            continue
        if "</head>" not in s:
            nohead += 1
            continue
        snippet = SNIPPET_TMPL.format(token=a.token)
        s2 = s.replace("</head>", snippet + "</head>", 1)
        added += 1
        if not a.dry_run:
            open(f, "w", encoding="utf-8", newline="").write(s2)

    print("扫描 %d 个 HTML" % len(files))
    if a.remove:
        print("移除: %d" % removed)
    else:
        print("注入: %d  已存在跳过: %d  无 </head>: %d" % (added, skipped, nohead))
    if a.dry_run:
        print("（--dry-run，未写盘）")


if __name__ == "__main__":
    main()
