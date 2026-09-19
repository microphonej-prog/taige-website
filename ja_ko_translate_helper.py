#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""日语/韩语翻译批处理的辅助工具（给子代理喂上下文 + 回收校验）

用法：
  python ja_ko_translate_helper.py extract <file...>        # 导出待译元素清单 JSON（zh + en 参考）
  python ja_ko_translate_helper.py verify  <file...>        # 校验：计数/引号/还原测试
  python ja_ko_translate_helper.py stats   <file...>        # 只打印完成度

extract 输出结构（每个文件一块）：
  [{"tag":"p","zh":"…","en":"…","html":true/false}, …]
"""
import re, sys, json, subprocess, os

ATTRS = ('zh', 'en', 'fr', 'es', 'ja', 'ko')
TAGPAT = re.compile(r'<([a-z0-9]+)\b((?:"[^"]*"|\'[^\']*\'|[^>"\'])*)>', re.S)


def elements(s):
    """产出 (tag, attrs, zh, en, ja, ko) —— 引号感知，避免属性值里的 > 截断"""
    for m in TAGPAT.finditer(s):
        attrs = m.group(2)
        def get(a):
            mm = re.search(r'data-%s="([^"]*)"' % a, attrs, re.S)
            return mm.group(1) if mm else None
        zh, en = get('zh'), get('en')
        if zh is None and en is None:
            continue
        yield m.group(1), attrs, zh, en, get('ja'), get('ko')


def cmd_extract(files):
    out = {}
    for f in files:
        s = open(f, encoding='utf-8').read()
        items = []
        for tag, attrs, zh, en, ja, ko in elements(s):
            if zh and (ja is None or ko is None):
                items.append({"tag": tag, "zh": zh,
                              "en": en or "",
                              "has_html": bool(re.search(r'<[a-zA-Z]', zh))})
        out[f] = items
        print(f"{f}: 待补元素 {len(items)}")
    print(json.dumps(out, ensure_ascii=False, indent=1))


def cmd_stats(files):
    tot = miss = 0
    for f in files:
        s = open(f, encoding='utf-8').read()
        for tag, attrs, zh, en, ja, ko in elements(s):
            if zh:
                tot += 1
                if ja is None or ko is None:
                    miss += 1
        print(f"{f}: 有 data-zh {tot} / 缺 ja或ko {miss}")
    print(f"合计 有zh {tot}，缺 ja或ko {miss}")


def cmd_verify(files):
    bad = 0
    for f in files:
        s = open(f, encoding='utf-8').read()
        c = {a: len(re.findall(r'data-%s="' % a, s)) for a in ATTRS}
        quotes = [v for v in re.findall(r'data-(?:ja|ko)="([^"]*)"', s, re.S) if '"' in v or "'" in v]
        # 还原测试：剥掉 ja/ko 属性应与 HEAD 一致（仅对已提交文件有效）
        same = None
        try:
            head = subprocess.check_output(['git', 'show', 'HEAD:' + f.replace('\\', '/')]).decode('utf-8')
            t = re.sub(r'\s*data-(?:ja|ko)="[^"]*"', '', s)
            same = t.replace('\r\n', '\n') == head.replace('\r\n', '\n')
        except Exception:
            pass
        flag = 'OK' if c['zh'] == c['ja'] == c['ko'] and not quotes else '!! 异常'
        if flag != 'OK':
            bad += 1
        print(f"{flag} {f}: zh={c['zh']} ja={c['ja']} ko={c['ko']} | 引号异常={len(quotes)} | 还原==HEAD={same}")
    return bad


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)
    mode, files = sys.argv[1], sys.argv[2:]
    if mode == 'extract':
        cmd_extract(files)
    elif mode == 'verify':
        sys.exit(1 if cmd_verify(files) else 0)
    elif mode == 'stats':
        cmd_stats(files)
    else:
        print(__doc__)
