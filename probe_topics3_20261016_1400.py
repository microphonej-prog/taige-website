#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""重叠关键词核查：适老无障碍 / 中东头巾长袍"""
import glob, os
from opencc import OpenCC

t2s = OpenCC('t2s')
files = sorted(p for p in glob.glob('blog/*.html') if '_body_' not in os.path.basename(p))
KEYS = ["拉链拉手", "拉环", "单手", "前开", "侧开", "高对比", "大字号", "大字",
        "阿拉伯语", "阿语", "斋月", "朝觐", "垂坠", "透视", "礼袍", "头巾", "长袍",
        "无障碍", "老化", "人口老龄化", "照护者", "护理院", "养老",
        "磁扣", "磁铁扣", "按扣", "搭扣", "魔术贴", "粘扣",
        "弹性腰头", "松紧腰", "免系", "易拉",
        "SASO", "SABER", "G-mark", "GCC", "海湾",
        "赠礼", "送礼", "开斋节", "宰牲节", "Eid"]
files_s = {}
for p in files:
    try:
        files_s[p] = t2s.convert(open(p, encoding='utf-8').read())
    except Exception as e:
        print("读失败", p, e)
print("扫描文件数:", len(files))
for k in KEYS:
    hit = [os.path.basename(p) for p, s in files_s.items() if k in s]
    cnt = sum(s.count(k) for s in files_s.values())
    flag = "  <== 空白" if cnt == 0 else ""
    print("%-12s 篇数=%-4d 次数=%-5d %s%s" % (k, len(hit), cnt, ("|".join(hit[:5]) if len(hit) <= 6 else ""), flag))

print()
print("=== 骨架文件结构 ===")
s = open('blog/knitwear-sweater-trims-guide.html', encoding='utf-8').read()
i0 = s.index('  <section class="article-body">')
i1 = s.index('\n</main>')
print("head+hero 长度 %d, body 长度 %d, 尾部长度 %d" % (i0, i1 - i0, len(s) - i1))
print('--- head 片段 ---')
print(s[:i0][:2600])
