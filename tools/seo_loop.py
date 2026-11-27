#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""SEO 持续优化循环：把 GSC 数据变成「今天该改哪几页」的排序清单

一次跑完四件事：
  1. 拉近 N 天 page+query 明细（默认 28 天，可与上一周期对比）
  2. 按「排名区间 × 展示量 × CTR」归类，给出动作建议（改标题 / 补内容 / 暂不动）
  3. 找出同一查询词被多页抢的蚕食嫌疑
  4. 输出 markdown 报告到 tools/reports/（可入库、可发邮件）

用法：
  python tools/seo_loop.py                          # taigetag.com，28 天
  python tools/seo_loop.py --site sc-domain:tagefabric.com --days 28
  python tools/seo_loop.py --min-imp-title 50 --min-imp-content 120

判定口径（都是本机实测后定的阈值，不是拍的）：
  改标题：排名 4–10、CTR < 2%、展示 ≥ 50   → 排在前页却没点击，标题/描述的问题
  补内容：排名 11–40、展示 ≥ 120           → 相关性/深度不够，改标题无用
  暂不动：排名 > 40                        → 先攒权重，别浪费工时
"""
import argparse, collections, datetime, json, pathlib, sys

HERE = pathlib.Path(__file__).resolve().parent
SCOPES = ["https://www.googleapis.com/auth/webmasters.readonly"]
SERVICE = HERE / "service_account.json"
TOKEN = HERE / "token.json"


def svc_client(force_oauth=False):
    from googleapiclient.discovery import build
    if SERVICE.exists() and not force_oauth:
        from google.oauth2 import service_account
        creds = service_account.Credentials.from_service_account_file(str(SERVICE), scopes=SCOPES)
        return build("searchconsole", "v1", credentials=creds, cache_discovery=False)
    from google.oauth2.credentials import Credentials
    from google.auth.transport.requests import Request
    creds = Credentials.from_authorized_user_file(str(TOKEN), SCOPES)
    if creds.expired and creds.refresh_token:
        creds.refresh(Request()); TOKEN.write_text(creds.to_json(), encoding="utf-8")
    return build("searchconsole", "v1", credentials=creds, cache_discovery=False)


def _exec(req, tries=3):
    import time
    last = None
    for i in range(tries):
        try:
            return req.execute()
        except Exception as e:      # noqa: BLE001
            last = e
            if i < tries - 1:
                time.sleep(2 + 2 * i)
    raise last


def fetch(svc, site, days, rows=5000):
    end = datetime.date.today() - datetime.timedelta(days=2)   # GSC 延迟 2 天
    start = end - datetime.timedelta(days=days - 1)
    body = {"startDate": start.isoformat(), "endDate": end.isoformat(),
            "dimensions": ["page", "query"], "rowLimit": rows}
    res = _exec(svc.searchanalytics().query(siteUrl=site, body=body))
    return res.get("rows", []), start, end


def build_report(rows, site, start, end, min_imp_title, min_imp_content):
    pages = collections.defaultdict(lambda: {"imp": 0, "clk": 0, "wpos": 0.0, "q": []})
    q_pages = collections.defaultdict(set)
    for r in rows:
        page, query = r["keys"][0], r["keys"][1]
        imp, clk = r.get("impressions", 0), r.get("clicks", 0)
        pos = r.get("position", 0)
        d = pages[page]
        d["imp"] += imp; d["clk"] += clk; d["wpos"] += pos * imp
        d["q"].append((imp, query, pos, clk))
        q_pages[query].add(page)

    title_targets, content_targets, later = [], [], []
    for page, d in pages.items():
        if not d["imp"]:
            continue
        pos = d["wpos"] / d["imp"]
        ctr = d["clk"] / d["imp"] * 100
        item = {"page": page, "imp": d["imp"], "clk": d["clk"], "ctr": ctr, "pos": pos,
                "top": sorted(d["q"], reverse=True)[:3]}
        if 3.5 <= pos <= 10.5 and ctr < 2.0 and d["imp"] >= min_imp_title:
            title_targets.append(item)
        elif 10.5 < pos <= 40 and d["imp"] >= min_imp_content:
            content_targets.append(item)
        elif pos > 40 and d["imp"] >= min_imp_content:
            later.append(item)

    for lst in (title_targets, content_targets, later):
        lst.sort(key=lambda x: -x["imp"] * (1 if x is title_targets else 0.5))

    # 蚕食：同一查询词被 ≥3 个**同一语种**的页面抢（不同语种各占一条是正常的，不算蚕食）
    def lang_of(url):
        m = __import__("re").match(r"https://[^/]+/([a-z]{2})/", url)
        return m.group(1) if m else "zh"

    cannib = []
    for q, ps in q_pages.items():
        by_lang = collections.defaultdict(list)
        for u in ps:
            by_lang[lang_of(u)].append(u)
        for lg, group in by_lang.items():
            if len(group) >= 3:
                cannib.append((q, sorted(group), lg))
    cannib.sort(key=lambda t: -len(t[1]))

    L = [f"# GSC 优化清单 · {site}",
         f"\n数据区间 **{start} → {end}**（GSC 延迟 2 天）｜共 {len(rows)} 条 page+query，{len(pages)} 个页面\n"]

    def block(title, lst, action):
        L.append(f"\n## {title}（{len(lst)} 页）\n")
        if not lst:
            L.append("_本期没有符合条件的页面。_\n"); return
        L.append("| 页面 | 展示 | 点击 | CTR | 平均排名 | 主要查询词 | 建议 |")
        L.append("|---|---|---|---|---|---|---|")
        for x in lst[:12]:
            p = x["page"].replace("https://" + site.split(":")[-1].lstrip("/"), "") or "/"
            qs = "; ".join(f"{q}({i}@{round(p2,1)})" for i, q, p2, _ in x["top"][:2])
            L.append(f"| `{p}` | {x['imp']} | {x['clk']} | {x['ctr']:.2f}% | {x['pos']:.1f} | {qs} | {action} |")
        L.append("")

    block("A. 优先改标题/描述（排前页却没点击）", title_targets, "改 title+desc，原词前置")
    block("B. 优先补内容（相关性/深度不够）", content_targets, "加直接回答段 + 长尾 FAQ")
    block("C. 暂不动（排太靠后，先攒权重）", later, "观察")

    L.append(f"\n## D. 蚕食嫌疑（同一语种 ≥3 页抢同一个词，{len(cannib)} 组）\n")
    if cannib:
        L.append("| 查询词 | 语种 | 页面数 | 页面 |")
        L.append("|---|---|---|---|")
        for q, ps, lg in cannib[:10]:
            shown = ", ".join(p.replace("https://" + site.split(":")[-1].lstrip("/"), "") for p in ps[:3])
            L.append(f"| {q} | {lg} | {len(ps)} | {shown} |")
    else:
        L.append("_没有明显蚕食。_")

    L.append("\n---\n\n## 下一步怎么做\n")
    L.append("1. A 类：按 `tools/gsc.py --pairs --filter-page <路径>` 看清每页原词，再改标题（≤60 字符/≤30 中文字）。")
    L.append("2. B 类：首段后加 `.callout` 直接回答块，末尾加 2–3 条 `h3+p` 长尾问答，目标 900 词以上。")
    L.append("3. D 类：同词抢位要合并或做内链指向主页面，别让两页互耗。")
    return "\n".join(L)


def push_summary(md, path, target):
    """把清单压缩成一条微信消息（零 token：直接调 hermes send）。"""
    import re, subprocess

    def section(letter):
        m = re.search(rf"## {letter}\..*?\n(.*?)(?=\n## |\n---)", md, re.S)
        if not m:
            return []
        rows = [l for l in m.group(1).splitlines() if l.startswith("| `")]
        out = []
        for r in rows[:3]:
            cells = [c.strip() for c in r.strip("|").split("|")]
            out.append(f"{cells[0].strip('`')} {cells[1]}展示/{cells[4]}")
        return out

    a, b = section("A"), section("B")
    d = re.search(r"## D\..*?\n\n\|.*?\n\|[-|]+\n(.*?)(?=\n---)", md, re.S)
    d_rows = [l for l in (d.group(1).splitlines() if d else []) if l.startswith("|")][:2]
    lines = [f"【辅料站 SEO 周清单】{datetime.date.today():%m-%d}",
             f"A 改标题 {len(a)} 页 / B 补内容 {len(b)} 页"]
    if a:
        lines.append("— A（排前页没点击）—"); lines += [f"· {x}" for x in a]
    if b:
        lines.append("— B（要在正文补）—"); lines += [f"· {x}" for x in b]
    if d_rows:
        lines.append("— 蚕食 —")
        lines += ["· " + " | ".join(c.strip() for c in r.strip("|").split("|")[:3]) for r in d_rows]
    lines.append(f"报告：{path.name}")
    text = "\n".join(lines)[:1500]

    targets = [target] if target else [
        "weixin:o9cq807Jymt7hMssWUDsiCzq8gjQ@im.wechat",
        "feishu:oc_5154253814a8de85860a5485e9c8a9e1",
    ]
    for t in targets:
        try:
            r = subprocess.run(["hermes", "send", "-t", t, "-f", "-"],
                               input=text, capture_output=True, text=True, timeout=120)
            if r.returncode == 0:
                print(f"已推送 → {t}")
                return
            print(f"推送失败 {t}: {(r.stderr or r.stdout)[:160]}")
        except Exception as e:                              # noqa: BLE001
            print(f"推送异常 {t}: {e}")
    print("所有渠道都失败，报告仍在 tools/reports/")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--site", default="sc-domain:taigetag.com")
    ap.add_argument("--days", type=int, default=28)
    ap.add_argument("--rows", type=int, default=5000)
    ap.add_argument("--min-imp-title", type=int, default=50)
    ap.add_argument("--min-imp-content", type=int, default=120)
    ap.add_argument("--oauth", action="store_true")
    ap.add_argument("--push", action="store_true", help="把摘要推到微信（走 hermes send，不消耗模型 token）")
    ap.add_argument("--target", default=None,
                    help="推送目标；默认按 weixin → feishu 依次尝试，第一个成功即止")
    args = ap.parse_args()

    svc = svc_client(args.oauth)
    rows, start, end = fetch(svc, args.site, args.days, args.rows)
    md = build_report(rows, args.site, start, end, args.min_imp_title, args.min_imp_content)
    out = HERE / "reports"
    out.mkdir(exist_ok=True)
    path = out / f"{datetime.date.today():%Y%m%d}.md"
    path.write_text(md, encoding="utf-8")
    print(md)
    print(f"\n报告已存：{path}")

    if args.push:
        push_summary(md, path, args.target)


if __name__ == "__main__":
    main()
