# -*- coding: utf-8 -*-
"""2026-10-13 下午批次：正文装配文件预检（六语属性完整性 + 引号/实体 + 非目标语言残留）"""
import re, sys
from html.parser import HTMLParser

FILES = ["blog/_body_embroidery.html", "blog/_body_animalcert.html"]
LANGS = ["zh", "en", "ja", "ko", "fr", "es"]


class P(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.tags = []          # (tag, dict(attrs), 行号)
        self.stack = []

    def handle_starttag(self, tag, attrs):
        self.tags.append((tag, dict(attrs), self.getpos()[0]))


def cjk(s):
    return len(re.findall(r'[\u4e00-\u9fff]', s))


ok = True
for f in FILES:
    s = open(f, encoding="utf-8").read()
    print("=" * 70)
    print("文件:", f, " 字节:", len(s.encode('utf-8')))

    # --- 1) 引号嵌套错误：data-xx="" 或 ="text" ---
    bad = re.findall(r'data-(?:zh|en|ja|ko|fr|es)=""', s)
    print("  引号空值/畸形 data-xx=\"\" :", len(bad))
    if bad:
        ok = False
    bad2 = re.findall(r'data-(?:zh|en|ja|ko|fr|es)="[^"]*"[a-zA-Z]', s)
    print("  属性后紧跟非法字符:", len(bad2))
    if bad2:
        ok = False

    # --- 2) HTMLParser 遍历，检查带 data-* 的元素是否六语齐全 ---
    p = P()
    p.feed(s)
    total = miss = 0
    miss_fr = miss_es = miss_ja = miss_ko = 0
    for tag, a, line in p.tags:
        has = [k for k in a if k.startswith("data-")]
        if not has:
            continue
        total += 1
        lack = [l for l in LANGS if ("data-" + l) not in a]
        if lack:
            miss += 1
            print("  [缺语言] 行%d <%s> 缺 %s" % (line, tag, lack))
            if "fr" in lack: miss_fr += 1
            if "es" in lack: miss_es += 1
            if "ja" in lack: miss_ja += 1
            if "ko" in lack: miss_ko += 1
    print("  带 data-* 元素: %d，缺任一语言: %d（缺fr=%d, 缺es=%d, 缺ja=%d, 缺ko=%d）"
          % (total, miss, miss_fr, miss_es, miss_ja, miss_ko))
    if miss:
        ok = False

    # --- 3) en/fr/es 里的中日韩残留 ---
    for lang in ("en", "fr", "es"):
        vals = re.findall(r'data-%s="([^"]*)"' % lang, s)
        res = [(i, cjk(v)) for i, v in enumerate(vals) if cjk(v)]
        if res:
            print("  [CJK残留] data-%s 有 %d 处含汉字: %s" % (lang, len(res), res[:6]))
            ok = False

    # --- 4) 裸 & 未转义 ---
    raw_amp = re.findall(r'&(?!amp;|lt;|gt;|quot;|nbsp;|#\d+;|#x[0-9a-fA-F]+;)[a-zA-Z]{0,6}', s)
    print("  可疑裸 & :", len(raw_amp), sorted(set(raw_amp))[:8])
    if raw_amp:
        ok = False

    # --- 5) 裸双引号出现在中文正文（属性值内的直引号） ---
    inner = re.findall(r'>[^<]*"', s)
    print("  文本节点内直双引号:", len(inner), inner[:3])

    # --- 6) 中文正文规模 + 关键词 ---
    zh = re.findall(r'data-zh="([^"]*)"', s)
    zh_all = " ".join(zh)
    zh_all = re.sub(r'<[^>]+>', '', zh_all)
    print("  data-zh 条数: %d，中文字符总数: %d" % (len(zh), cjk(zh_all)))
    for kw in (["绣花", "刺绣", "毛巾绣", "立体绣", "贴布绣", "针数", "衬料", "水溶膜"] if "emb" in f
               else ["动物源", "认证", "皮革", "羊毛", "羽绒", "LWG", "RWS", "RDS", "素皮"]):
        print("    关键词 %-6s -> %d 次" % (kw, zh_all.count(kw)))

    # --- 7) 结构要素 ---
    for need in ['class="cta-box"', 'class="cta-btn"', 'href="../contact.html"',
                 'href="index.html"', "<h2"]:
        print("  含 %-24s : %s" % (need, need in s))

print()
print("预检结论:", "通过" if ok else "存在问题，需修复")
sys.exit(0 if ok else 1)
