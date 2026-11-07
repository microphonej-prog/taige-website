#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把德语(de)语言按钮移到英语(en)后面，顺序变为 zh/en/de/ja/ko/fr/es/pt"""
import re, glob

files = ['index.html', 'products.html', 'about.html', 'contact.html']
files += sorted(glob.glob('blog/*.html'))

changed = 0
skipped = 0
failed = []

# 匹配任意 lang-flag 按钮（含 svg 内部内容）
BTN_PAT = re.compile(r'<button class="lang-flag[^"]*" data-lang="(\w+)"[^>]*>.*?</button>', re.S)

for f in files:
    try:
        s = open(f, encoding='utf-8').read()
    except Exception as e:
        failed.append((f, str(e)))
        continue

    btns = BTN_PAT.findall(s)
    if 'de' not in btns:
        skipped += 1
        continue

    # 已经是目标顺序？
    if btns == ['zh', 'en', 'de', 'ja', 'ko', 'fr', 'es', 'pt']:
        skipped += 1
        continue

    # 提取 de 按钮原文
    m_de = re.search(r'<button class="lang-flag[^"]*" data-lang="de"[^>]*>.*?</button>', s, re.S)
    m_en = re.search(r'<button class="lang-flag[^"]*" data-lang="en"[^>]*>.*?</button>', s, re.S)
    if not m_de or not m_en:
        failed.append((f, '找不到 de 或 en 按钮'))
        continue

    de_btn = m_de.group(0)
    # 1) 先删除 de 按钮
    s2 = s.replace(de_btn, '', 1)
    # 2) 重新定位 en 按钮（删除后位置可能不变，但重新匹配更稳）
    m_en2 = re.search(r'<button class="lang-flag[^"]*" data-lang="en"[^>]*>.*?</button>', s2, re.S)
    if not m_en2:
        failed.append((f, '删除后找不到 en 按钮'))
        continue
    # 3) 在 en 按钮后插入 de 按钮
    s2 = s2[:m_en2.end()] + de_btn + s2[m_en2.end():]

    open(f, 'w', encoding='utf-8', newline='').write(s2)
    changed += 1

print(f'处理: {len(files)} 个文件')
print(f'✅ 已调整顺序: {changed}')
print(f'⏭ 跳过(已正确/无de): {skipped}')
print(f'❌ 失败: {len(failed)}')
for x in failed[:8]:
    print('  ', x)
