#!/usr/bin/env python
"""统一 hreflang：按“目标页存在且可索引”动态生成语言互链，修掉单向/漏声明。

规则：
- zh-Hant → 中文页（根目录）
- en/de/ja/ko/fr/es/pt-BR → 仅当该语言版本文件真实存在、且不含 noindex 时声明
- x-default → 中文页
- 跳过本身是 noindex 的页面（它们不进索引，无需修正；待翻译任务重新生成时自然带对）

用法：
    python fix_hreflang.py --dry-run     # 只报告差异
    python fix_hreflang.py --apply       # 写入（可加 --limit N 分批）
"""
import argparse
import glob
import os
import re
import sys

ROOT = "C:/Users/micro/taige-website"
BASE = "https://taigetag.com/"
LANGS = ["en", "de", "ja", "ko", "fr", "es", "pt"]
HL_TAG = {"en": "en", "de": "de", "ja": "ja", "ko": "ko", "fr": "fr", "es": "es", "pt": "pt-BR"}

ALT_RE = re.compile(r'[ \t]*<link rel="alternate" hreflang="[^"]*"[^>]*>\n?')


def page_lang_and_rel(path):
    """返回 (lang or 'zh', rel_path like 'blog/x.html' or 'index.html')"""
    rel = path.replace(ROOT + "/", "")
    m = re.match(r'^(en|de|ja|ko|fr|es|pt)/(.+)$', rel)
    if m:
        return m.group(1), m.group(2)
    return "zh", rel


def url_for(lang, rel):
    if rel == "index.html":
        return BASE if lang == "zh" else BASE + lang + "/"
    return (BASE + rel) if lang == "zh" else BASE + lang + "/" + rel


def file_for(lang, rel):
    p = os.path.join(ROOT, rel) if lang == "zh" else os.path.join(ROOT, lang, rel)
    return p


def indexable(p):
    if not os.path.isfile(p):
        return False
    try:
        s = open(p, encoding="utf-8", errors="ignore").read()
    except OSError:
        return False
    return "noindex" not in s.lower()


def build_block(lang, rel):
    lines = ['<link rel="alternate" hreflang="zh-Hant" href="%s">' % url_for("zh", rel)]
    for l in LANGS:
        if indexable(file_for(l, rel)):
            lines.append('<link rel="alternate" hreflang="%s" href="%s">' % (HL_TAG[l], url_for(l, rel)))
    lines.append('<link rel="alternate" hreflang="x-default" href="%s">' % url_for("zh", rel))
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--limit", type=int, default=0)
    a = ap.parse_args()
    os.chdir(ROOT)

    files = sorted(glob.glob("*.html"))
    for d in ["blog"] + [l + "/" + sub for l in LANGS for sub in ("", "blog")]:
        files += sorted(glob.glob(os.path.join(d, "*.html")))
    files = [f.replace("\\", "/") for f in files]

    changed, skipped_noindex, missing_canon = [], 0, 0
    for rel in files:
        p = os.path.join(ROOT, rel)
        s = open(p, encoding="utf-8", errors="ignore").read()
        if "noindex" in s.lower():
            skipped_noindex += 1
            continue
        lang, relp = page_lang_and_rel(rel)
        block = build_block(lang, relp)

        existing = ALT_RE.findall(s)
        have = set(re.findall(r'hreflang="([^"]+)"', s))
        want = set(re.findall(r'hreflang="([^"]+)"', block))
        if have == want and "".join(existing).strip():
            continue
        if not existing:
            # 无 hreflang：插在 canonical 之后
            m = re.search(r'<link rel="canonical"[^>]*>', s)
            if not m:
                missing_canon += 1
                continue
            new = s[:m.end()] + "\n" + block + s[m.end():]
        else:
            # 用新块替换第一处，删除其余
            first = True
            def _rep(mm):
                nonlocal first
                if first:
                    first = False
                    return block + "\n"
                return ""
            new = ALT_RE.sub(_rep, s)
        changed.append(rel)
        if a.apply:
            open(p, "w", encoding="utf-8", newline="").write(new)
            if a.limit and len(changed) >= a.limit:
                break

    print("扫描 %d 页 | 需修 %d | 跳过 noindex %d | 无 canonical %d" %
          (len(files), len(changed), skipped_noindex, missing_canon))
    for r in changed[:15]:
        print("  ·", r)
    if len(changed) > 15:
        print("  … 共 %d 个" % len(changed))
    if not a.apply:
        print("（dry-run，未写盘）")


if __name__ == "__main__":
    main()
