#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-09-24 下午批次：正文文件体检（引号感知的标签扫描）
- 标签内 data-zh/en/fr/es/ja/ko 六语完整性
- 属性引号是否成对闭合（移动端 WebKit 崩溃元凶）
- 内部链接目标存在性
- 韩语/法语/西语属性里是否残留中日汉字（翻译兜底检测）
"""
import os, re, sys

FILES = ["blog/_body_transit.html", "blog/_body_shirt.html"]
LANGS = ["zh", "en", "fr", "es", "ja", "ko"]
CJK = re.compile(r'[\u4e00-\u9fff\u3040-\u30ff]')


def split_tags(s):
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

    # 韩语属性里不应出现汉字/假名
    ko_vals = re.findall(r'data-ko="([^"]*)"', s)
    ko_hits = [v[:60] for v in ko_vals if CJK.search(v)]
    print("  韩语属性含汉字/假名: %d (共 %d 条)" % (len(ko_hits), len(ko_vals)))
    for v in ko_hits[:5]:
        print("   !! %s" % v)
    bad += len(ko_hits)

    # 日语属性不应含简体中文专用字形（粗略：简体独有字）
    ja_vals = re.findall(r'data-ja="([^"]*)"', s)
    # 简体独有字形（日文不使用的字）：纸样说签码烫尔东们这为
    SIMP = re.compile(r'[纸样说签码烫尔东们这为]')
    ja_bad = [v[:60] for v in ja_vals if SIMP.search(v)]
    print("  日语属性含可疑简体字: %d" % len(ja_bad))
    for v in ja_bad[:3]:
        print("   !! %s" % v)
    bad += len(ja_bad)

    # 法语/西语/英语属性里的大段中文兜底检测（>=4 连续汉字视为未翻译）
    for L in ["fr", "es", "en"]:
        badv = [v[:60] for v in re.findall(r'data-%s="([^"]*)"' % L, s) if re.search(r'[\u4e00-\u9fff]{4,}', v)]
        print("  %s 属性含连续中文: %d" % (L, len(badv)))
        for v in badv[:3]:
            print("   !! %s" % v)
        bad += len(badv)

    for href in sorted(set(re.findall(r'href="([^"]*)"', s))):
        if href.startswith(("http", "mailto:", "#", "tel:", "..")):
            continue
        if not os.path.exists(os.path.join("blog", href)):
            print("   !! 断链 %s" % href)
            bad += 1

    raw_amp = re.findall(r'&(?!(?:amp|nbsp|lt|gt|quot|#\d+);)', s)
    print("  裸 & 数量: %d" % len(raw_amp))
    bad += len(raw_amp)

    # 属性值里出现直双引号（会截断属性）——用转义序列检测
    dq = len(re.findall(r'="[^"]*\\"', s))
    print("  属性内转义引号: %d" % dq)

    print("  h2=%d table=%d li=%d callout=%d cta=%d ol=%d"
          % (s.count("<h2 "), s.count("<table>"), s.count("<li"),
             s.count('class="callout"'), s.count('class="cta-btn"'), s.count("<ol>")))
    zh_len = len(re.sub(r'\s+', '', ' '.join(re.findall(r'data-zh="([^"]*)"', s))))
    print("  data-zh 正文字符数（含标签文本）: %d" % zh_len)

print("\n问题总数 = %d" % bad)
sys.exit(1 if bad else 0)
