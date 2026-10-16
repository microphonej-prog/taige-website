#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""选题空白扫描 第四轮"""
import glob, os
from opencc import OpenCC

t2s = OpenCC('t2s')
files = sorted(p for p in glob.glob('blog/*.html') if '_body_' not in os.path.basename(p))
KEYS = ["呆滞", "尾料", "余料", "边角料", "报废", "损耗", "补料", "备损",
        "ESG", "CSRD", "EcoVadis", "Sedex", "BSCI", "SMETA", "问卷", "行为准则",
        "How2Recycle", "绿点", "回收标志", "树脂识别码", "垃圾分类", "回收指引", "分选标识",
        "电子价签", "智能标签", "温度记录", "记录仪", "数据记录",
        "拉线", "铅封", "封条", "防盗扣", "防调包",
        "促销吊牌", "换季", "季末", "清仓", "折扣牌",
        "吊牌 归档", "留样 柜", "样品 库", "数字化 留样",
        "客户 拜访", "展会 样品", "样卡 制作", "辅料 展示",
        "洗涤 说明 图标", "GINETEX", "洗涤 符号 版权",
        "跨境 独立站", "DTC", "自建站",
        "打样 通知", "确认 单", "大货 确认",
        "供应商 变更 通知", "变更 管理", "工程 变更", "ECN",
        "对账", "结账", "月结", "付款 周期",
        "紧急 订单", "加急", "赶货", "插单",
        "返单", "翻单", "复购",
        "水性 胶", "热熔胶", "胶水", "粘合",
        "车缝 线", "缝纫线", "走线",
        "刺绣 线", "绣花 线",
        "标签 厚度", "胶带 厚度",
        "吊牌 硬度", "纸板 厚度", "克重 换算",
        "服装 辅料 检测 项目", "检测 项目", "送检"]
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
    print("%-14s 篇数=%-4d 次数=%-5d %s%s" % (k, len(hit), cnt, ("|".join(hit[:5]) if len(hit) <= 8 else ""), flag))
