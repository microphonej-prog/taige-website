#!/usr/bin/env bash
# 候选关键词覆盖体检：统计 blog/*.html 中各类关键词命中的文件数
cd /c/Users/micro/taige-website || exit 1
KW=(
"ZDHC" "Higg" "CBAM" "香片" "香氛" "sachet" "How2Recycle" "回收标识" "防静电" "antistatic"
"保质期" "shelf life" "仓[储存]条件" "仓储" "灰卡" "色差" "ΔE" "delta E" "光源" "对色灯箱"
"字号" "字体" "可读性" "洗涤符号" "尺码换算" "size chart" "size conversion" "尺码对照"
"偶氮" "甲醛" "邻苯" "pH 值" "pH值" "重金属" "镍释放" "锐利" "尖锐"
"VOID" "揭开留字" "防拆" "封条" "封口贴" "易碎纸"
"蜡光" "无溶剂" "水性覆膜" "触感油" "闪粉" "夜光" "香味油墨"
"吊粒" "吊绳" "打结" "蝴蝶结" "穿绳" "鸡眼" "气眼" "铆钉"
"拼接" "洗标缝制" "水洗唛" "织唛密度" "提花" "缎面"
"报关" "原产地证" "FORME" "CO" "海运" "空运" "拼箱"
"清关" "关税" "HS" "配额" "反倾销"
"质检报告" "第三方" "检测项目" "限值" "速查表"
"包装机" "自动" "吊挂" "挂装"
)
for k in "${KW[@]}"; do
  n=$(ls blog/*.html | while read -r f; do if grep -q "$k" "$f" 2>/dev/null; then echo "$f"; fi; done | wc -l)
  printf "%-16s %s\n" "$k" "$n"
done
