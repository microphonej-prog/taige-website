#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""排查：zh 根目录新页面在无头 Chrome 下 title 缺失的原因（打印 DOM 头部 + 统计）"""
import subprocess, re, os

CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
urls = [
    "https://taigetag.com/blog/hang-tag-folding-types.html?lang=zh&v=1",
    "https://taigetag.com/blog/hang-tag-folding-types.html?v=152",
]
out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "F:/hermes/cache/scratch")
for url in urls:
    r = subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-sandbox",
                        "--virtual-time-budget=12000", "--dump-dom", url],
                       capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=120)
    dom = r.stdout or ""
    print("URL:", url)
    print("  dom 长度:", len(dom), "| <title 出现次数:", dom.count("<title"), "| <h1 次数:", dom.count("<h1"))
    m = re.search(r"<title[^>]*>(.*?)</title>", dom, re.S)
    print("  title 正则:", (m.group(1)[:80] if m else "NONE"))
    print("  head 片段:", re.sub(r"\s+", " ", dom[:400]))
    if dom:
        p = "F:/hermes/cache/scratch/dom_zh_probe.html"
        open(p, "w", encoding="utf-8").write(dom)
        print("  已保存:", p)
    print()
