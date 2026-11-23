# -*- coding: utf-8 -*-
"""对比新页与既有页的中文残留，并扫描简体字专有字符（ja 页防简体兜底）。"""
import re

NEW = ["blog/garment-label-adhesive-types-guide.html",
       "blog/label-printer-printhead-maintenance-guide.html"]
OLD = ["en/blog/vellum-translucent-hang-tags.html", "ja/blog/vellum-translucent-hang-tags.html",
       "fr/blog/vellum-translucent-hang-tags.html"]

SIMP = "为这发说时们电东国内对开关门问题实际经济义务认证标签纸术语质价费买卖货设备应该还从与产业务个样样"


def scan(f, only_simp=False):
    s = open(f, encoding="utf-8").read()
    body = re.sub(r'<script.*?</script>|<style.*?</style>|<!--.*?-->', ' ', s, flags=re.S)
    out = []
    for m in re.finditer(r'>([^<>]+)<', body):
        t = m.group(1).strip()
        if not t or len(t) < 2:
            continue
        hits = [c for c in t if c in SIMP]
        if hits and (only_simp or re.search(r'[\u4e00-\u9fff]', t)):
            out.append((t[:60], ''.join(hits)))
    return out


for f in NEW + OLD:
    print("=" * 60)
    print(f)
    for t, h in scan(f):
        print("   ", repr(t), "简:", h)
