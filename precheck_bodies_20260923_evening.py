#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-09-23 晚间批次：正文文件体检（引号感知的标签扫描）
- 标签内 data-zh/en/fr/es/ja/ko 六语完整性
- 属性引号是否成对闭合（移动端 WebKit 崩溃元凶）
- 内部链接目标存在性
"""
import os, re, sys

FILES = ["blog/_body_socks.html", "blog/_body_hats.html"]
LANGS = ["zh", "en", "fr", "es", "ja", "ko"]


def split_tags(s):
    """按引号状态切分标签：返回 (tag_text, closed_bool) 列表"""
    out, i, n = [], 0, len(s)
    while i < n:
        if s[i] == '<':
            j, in_q = i + 1, False
            while j < n:
                c = s[j]
                if c == '"':
                    in_q = not in_q
                elif c == '>' and not in_q:
                    break
                j += 1
            out.append((s[i:j + 1], j < n and not in_q))
            i = j + 1
        else:
            i += 1
    return out


bad = 0
for f in FILES:
    s = open(f, encoding="utf-8").read()
    tags = split_tags(s)
    print("=== %s (%d KB) 标签 %d ===" % (f, len(s.encode("utf-8")) // 1024, len(tags)))

    unclosed = [t[:80] for t, ok in tags if not ok]
    print("  引号未闭合标签: %d" % len(unclosed))
    for t in unclosed[:5]:
        print("   !! %s" % t)
    bad += len(unclosed)

    miss = {}
    n_data = 0
    for t, ok in tags:
        if re.match(r'<(p|h2|h3|li|td|th|div|a|span)\b', t) and 'data-zh=' in t:
            n_data += 1
            for L in LANGS:
                if (' data-%s=' % L) not in t:
                    miss.setdefault(L, []).append(t[:70])
    print("  已带 data-zh 的正文元素: %d；缺语种: %s"
          % (n_data, {k: len(v) for k, v in miss.items()}))
    for L, v in miss.items():
        for x in v[:3]:
            print("   !! 缺 %s -> %s" % (L, x))
        bad += len(v)

    for href in sorted(set(re.findall(r'href="([^"]*)"', s))):
        if href.startswith(("http", "mailto:", "#", "tel:")):
            continue
        if not os.path.exists(os.path.join("blog", href)):
            print("   !! 断链 %s" % href)
            bad += 1

    # 裸 & 检查（非实体）
    raw_amp = [m for m in re.findall(r'&(?!(?:amp|nbsp|lt|gt|quot|#\d+);)', s)]
    print("  裸 & 数量: %d" % len(raw_amp))
    bad += len(raw_amp)

    # 属性值内裸双引号（会造成 WebKit 崩溃）
    print("  中文正文字数(去标签): %d" % len(re.findall(
        r'[\u4e00-\u9fff]', re.sub(r'<[^>]*>', '', s))))
    print("  h2=%d table=%d li=%d callout=%d cta=%d"
          % (s.count("<h2 "), s.count("<table>"), s.count("<li"),
             s.count('class="callout"'), s.count('class="cta-btn"')))

print("\n问题总数 = %d" % bad)
sys.exit(1 if bad else 0)
