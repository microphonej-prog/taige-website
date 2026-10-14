#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""修掉正文文件里混进 ja 属性的中文词（授权/方案）。"""
import io

FIX = [
    ('オランダ国内に授权代表者を指定する必要があります', 'オランダ国内に権限を有する代表者を指定する必要があります'),
    ('オランダでの登録または授权代表者の情報', 'オランダでの登録または権限を有する代表者の情報'),
    ('授权代表者の委任状', '権限を有する代表者の委任状'),
    ('オランダの授权代表者', 'オランダの権限を有する代表者'),
    ('エプロンの表示方案は通常数十回', 'エプロンの表示設計は通常数十回'),
    ('表示方案', '表示設計'),
]

for f in ['blog/_body_apron.html', 'blog/_body_nlcomp.html']:
    s = io.open(f, encoding='utf-8').read()
    for a, b in FIX:
        s = s.replace(a, b)
    io.open(f, 'w', encoding='utf-8', newline='').write(s)
    print(f, '授权:', s.count('授权'), ' 方案:', s.count('方案'))
