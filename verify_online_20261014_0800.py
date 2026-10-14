#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-14 08:00 批次线上校验（socket 直连 GitHub Pages IP，绕开本机 TUN 劫持）：
1) 线上 sitemap.xml 是否含 12 个新 URL，lastmod 是否为 2026-10-14
2) 线上各语言页面静态 HTML 的 title / h1 / canonical 是否正确
"""
import socket, ssl, re, sys, time

IP = "185.199.108.153"
HOST = "taigetag.com"
SLUGS = ["apron-trims-label-guide.html", "clothing-label-compliance-netherlands.html"]
LANGS = [("zh", ""), ("en", "en/"), ("ja", "ja/"), ("ko", "ko/"), ("fr", "fr/"), ("es", "es/")]
EXPECT = {
    "apron-trims-label-guide.html": {
        "zh": "圍裙與餐飲工作服輔料指南", "en": "Apron and Food-Service Workwear Trims Guide",
        "ja": "エプロン・飲食ユニフォーム副資材ガイド", "ko": "앞치마·요식업 유니폼 부자재 가이드",
        "fr": "Guide des accessoires pour tabliers", "es": "Guía de accesorios para delantales"},
    "clothing-label-compliance-netherlands.html": {
        "zh": "荷蘭服裝標籤與包裝合規指南", "en": "Netherlands Apparel Labelling and Packaging Compliance",
        "ja": "オランダの衣料ラベル・包装コンプライアンス", "ko": "네덜란드 의류 라벨·포장 컴플라이언스",
        "fr": "Conformité étiquetage et emballage aux Pays-Bas", "es": "Cumplimiento de etiquetado y embalaje en Países Bajos"},
}


def fetch(path):
    last = None
    for attempt in range(3):
        try:
            ctx = ssl.create_default_context()
            with socket.create_connection((IP, 443), timeout=25) as raw:
                with ctx.wrap_socket(raw, server_hostname=HOST) as s:
                    req = ("GET %s HTTP/1.1\r\nHost: %s\r\nUser-Agent: Mozilla/5.0 (TAGE verify)\r\n"
                           "Connection: close\r\nAccept: */*\r\n\r\n" % (path, HOST))
                    s.sendall(req.encode())
                    buf = b""
                    while True:
                        chunk = s.recv(65536)
                        if not chunk:
                            break
                        buf += chunk
            head, _, body = buf.partition(b"\r\n\r\n")
            status = head.split(b"\r\n")[0].decode("latin-1")
            return status, body.decode("utf-8", "replace")
        except Exception as e:   # 偶发 TLS EOF，重试
            last = e
            time.sleep(2)
    raise last


fails = []

# 1) sitemap
st, sm = fetch("/sitemap.xml")
print("sitemap:", st, "长度", len(sm))
if "200 OK" not in st:
    fails.append("sitemap 拉取失败: %s" % st)
for slug in SLUGS:
    for _, pre in LANGS:
        u = "https://taigetag.com/%sblog/%s" % (pre, slug)
        blk = re.search(r"<loc>%s</loc>\s*<lastmod>([^<]*)</lastmod>" % re.escape(u), sm)
        tag = "OK" if blk and blk.group(1) == "2026-10-14" else "!! 问题"
        if tag != "OK":
            fails.append("线上 sitemap: %s lastmod=%s" % (u, blk.group(1) if blk else "无此 URL"))
        print("  %s %s lastmod=%s" % (tag, u, blk.group(1) if blk else "-"))
for _, pre in LANGS:
    u = "https://taigetag.com/%sblog/index.html" % pre
    blk = re.search(r"<loc>%s</loc>\s*<lastmod>([^<]*)</lastmod>" % re.escape(u), sm)
    if not blk or blk.group(1) != "2026-10-14":
        fails.append("线上 blog index lastmod 未更新: %s" % u)
print("  blog/index.html 六语 lastmod 检查完毕")

# 2) 各语言页面 title / h1 / canonical
print("\n页面静态检查:")
for slug in SLUGS:
    for lang, pre in LANGS:
        path = "/%sblog/%s" % (pre, slug)
        st, html = fetch(path)
        title = re.search(r"<title[^>]*>(.*?)</title>", html, re.S)
        title = title.group(1).strip() if title else ""
        h1 = re.search(r"<h1[^>]*>(.*?)</h1>", html, re.S)
        h1 = re.sub(r"<[^>]+>", "", h1.group(1)).strip() if h1 else ""
        canon = re.search(r'<link rel="canonical" href="([^"]*)"', html)
        canon = canon.group(1) if canon else ""
        exp_c = "https://taigetag.com/%sblog/%s" % (pre, slug)
        ok_t = EXPECT[slug][lang] in title
        ok_h = len(h1) > 8
        ok_c = canon == exp_c
        if not (ok_t and ok_h and ok_c and "200 OK" in st):
            fails.append("%s %s title=%s h1=%s canon=%s" % (path, st, ok_t, ok_h, ok_c))
        print("  %-9s %s title✓=%s h1=%s canonical✓=%s  标题=%s"
              % (st.replace("HTTP/1.1 ", ""), path, ok_t, ok_h, ok_c, title[:60]))

print("\n线上校验结论:", "全部通过" if not fails else "%d 项问题" % len(fails))
for f in fails[:20]:
    print("  -", f)
sys.exit(0 if not fails else 1)
