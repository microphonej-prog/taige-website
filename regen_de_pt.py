#!/usr/bin/env python
"""把 de/pt 全部语言页重新生成一遍（缺译文时回退英文，彻底清掉页面上的中文）。

用法：
  python regen_de_pt.py            # 全量
  python regen_de_pt.py --limit 90 # 只做前 N 篇（分批用）
"""
import argparse
import glob
import os
import sys

REPO = r"C:/Users/micro/taige-website"
os.chdir(REPO)
sys.path.insert(0, REPO)
import gen_i18n as G  # noqa: E402


def targets():
    arts = [f for f in sorted(glob.glob("blog/*.html"))
            if "index" not in os.path.basename(f) and not os.path.basename(f).startswith("_")]
    files = ["index.html", "about.html", "products.html", "contact.html", "blog/index.html"] + arts
    return [f.replace("\\", "/") for f in files]


def abs_url(lang, src):
    """blog/x.html -> https://taigetag.com/<lang>/blog/x.html；index.html -> /<lang>/index.html"""
    if src == "index.html":
        return "https://taigetag.com/%s/index.html" % lang
    return "https://taigetag.com/%s/%s" % (lang, src)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--langs", default="de,pt")
    ap.add_argument("--start", type=int, default=0)
    a = ap.parse_args()
    langs = [x.strip() for x in a.langs.split(",") if x.strip()]

    fs = targets()
    if a.start:
        fs = fs[a.start:]
    if a.limit:
        fs = fs[:a.limit]

    done = 0
    for src in fs:
        for lang in langs:
            out = os.path.join(lang, src)
            try:
                G.convert(lang, src, out, abs_url(lang, src))
                done += 1
            except Exception as e:
                print("✗ %s [%s] %s" % (src, lang, e))
        if done % 60 == 0 and done:
            print("  … 已完成 %d 个页面" % done)
    print("总完成: %d 个页面（%d 个源文件 × %d 语）" % (done, len(fs), len(langs)))


if __name__ == "__main__":
    main()
