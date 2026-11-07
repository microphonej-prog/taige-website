#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""批量给所有源页面加德语(de)/葡语(pt)语言切换按钮"""
import re, glob, os

DE_BTN = '<button class="lang-flag" data-lang="de" title="Deutsch" type="button"><svg viewBox="0 0 30 20" width="20" height="14" aria-hidden="true"><rect width="30" height="6.67" fill="#000000"/><rect y="6.67" width="30" height="6.67" fill="#DD0000"/><rect y="13.33" width="30" height="6.67" fill="#FFCE00"/></svg></button>'
PT_BTN = '<button class="lang-flag" data-lang="pt" title="Português" type="button"><svg viewBox="0 0 30 20" width="20" height="14" aria-hidden="true"><rect width="30" height="20" fill="#009C3B"/><polygon points="15,2.5 27,10 15,17.5 3,10" fill="#FFDF00"/><circle cx="15" cy="10" r="4.5" fill="#002776"/></svg></button>'

# es 按钮匹配（可能带 active class）
ES_PAT = re.compile(r'(<button class="lang-flag[^"]*" data-lang="es"[^>]*>.*?</button>)', re.S)

files = []
files += ['index.html', 'products.html', 'about.html', 'contact.html']
files += sorted(glob.glob('blog/*.html'))

changed = 0
skipped = 0
failed = []

for f in files:
    try:
        s = open(f, encoding='utf-8').read()
    except Exception as e:
        failed.append((f, str(e)))
        continue

    # 幂等：已有 de 按钮则跳过
    if 'data-lang="de"' in s:
        skipped += 1
        continue

    m = ES_PAT.search(s)
    if not m:
        failed.append((f, '未找到 es 按钮'))
        continue

    new_s = s[:m.end()] + DE_BTN + PT_BTN + s[m.end():]
    open(f, 'w', encoding='utf-8', newline='').write(new_s)
    changed += 1

print(f'处理文件总数: {len(files)}')
print(f'✅ 已添加 de/pt 按钮: {changed}')
print(f'⏭ 已存在跳过: {skipped}')
print(f'❌ 失败: {len(failed)}')
for f, e in failed[:10]:
    print(f'   {f}: {e}')
