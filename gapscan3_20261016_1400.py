#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""选题空白扫描 第三轮"""
import glob, re, os
from opencc import OpenCC

t2s = OpenCC('t2s')
files = sorted(p for p in glob.glob('blog/*.html') if '_body_' not in os.path.basename(p))
KEYS = ["承重", "撕裂", "挺度", "卷装", "切张", "超声波", "圆角", "装箱单", "展会",
        "汇率", "首件确认", "触感", "冷烫", "夜光", "温变", "香味", "刮刮", "可变数据",
        "白墨", "数码烫金", "局部UV", "磁吸", "领标", "吊牌贴纸", "价格牌",
        "标签软化", "卷边", "边缘发硬", "刺痒", "水洗后标签", "洗标脱落",
        "领口标", "侧缝标", "内里标", "口袋标", "裤腰标",
        "吊牌 位置", "挂牌位置", "吊牌 陈列", "模特 吊牌",
        "纸袋 承重", "提手强度", "提绳", "棉绳提手", "纸绳", "三股绳",
        "胶袋 承重", "封口强度", "热封强度", "跌落测试", "振动",
        "雾化", "雾度", "透光", "防雾", "抗静电", "静电",
        "色差仪", "分光", "灯箱", "对色灯箱", "同色异谱",
        "水洗 收缩", "缩水", "蒸汽", "熨烫", "热压",
        "吊牌 挂绳 颜色", "吊牌 绳子 材质", "麻绳", "棉线",
        "包装 开窗", "开窗袋", "自封袋", "拉链袋", "文件袋",
        "打样 室", "版房", "裁床", "车位", "后道",
        "质检 报告", "自检", "巡检", "首件", "末件",
        "供应商 培训", "技术 交流", "联合 开发", "共同 研发"]
files_s = {}
for p in files:
    try:
        files_s[p] = t2s.convert(open(p, encoding='utf-8').read())
    except Exception as e:
        print("读失败", p, e)
for k in KEYS:
    hit = [os.path.basename(p) for p, s in files_s.items() if k in s]
    cnt = sum(s.count(k) for s in files_s.values())
    flag = "  <== 空白" if cnt == 0 else ""
    print("%-12s 篇数=%-4d 次数=%-5d %s%s" % (k, len(hit), cnt, ("|".join(hit[:5]) if len(hit) <= 8 else ""), flag))
