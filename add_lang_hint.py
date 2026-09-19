#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""A+ 语言建议条 + 记住访客选择（改 js/main.js + css/style.css）

- main.js：根目录在“访客此前选过别的语言”时跳转到该语言同页面（localStorage，爬虫不受影响）；
  其余情况不跳转，只在系统语言≠当前页面语言时显示顶部建议条；爬虫一律不显示、不跳转
- 去掉原来那段永远不会执行的“按浏览器语言自动匹配”死代码
用法: python add_lang_hint.py [--dry]
"""
import re, sys, os

DRY = '--dry' in sys.argv
os.chdir(os.path.dirname(os.path.abspath(__file__)))

JS = 'js/main.js'
CSS = 'css/style.css'

NEW_DETECT = '''  var current = null;
  /* 爬蟲/無頭瀏覽器一律不做任何語言跳轉與提示（避免 Googlebot 渲染與 hreflang 信號衝突） */
  var IS_BOT = false;
  try {
    IS_BOT = /bot|crawl|spider|slurp|bingpreview|baidu|yandex|duckduck|facebookexternalhit|headless|puppeteer|playwright|lighthouse|gtmetrix/i
      .test(navigator.userAgent || "") || navigator.webdriver === true;
  } catch (e) {}
  /* 訪客上次的語言選擇（localStorage；爬蟲不讀，因此不影響收錄） */
  var stored = null;
  try { stored = localStorage.getItem(LANG_KEY); } catch (e) {}
  if (!stored || LANGS.indexOf(stored) < 0) stored = null;

  if (DIR_LANG) {
    current = DIR_LANG;
  } else if (urlLang && LANGS.indexOf(urlLang) >= 0 && urlLang !== "zh") {
    /* 舊式 ?lang=fr 鏈接：升級跳轉到「同一頁面」的獨立語言目錄版
       （舊寫法 location.replace("../" + urlLang + "/") 在內頁會把 /blog/xxx.html 解析成 /fr/ 首頁，
       丟失原文章路徑；此處改爲按 pathname 拼接，保留內頁路徑） */
    var _rel = "";
    try { _rel = location.pathname.replace(/^\\/+/, ""); } catch (e) {}
    if (!_rel || _rel === "index.html") {
      location.replace("/" + urlLang + "/?v=" + BUST_VERSION);
    } else {
      location.replace("/" + urlLang + "/" + _rel + "?v=" + BUST_VERSION);
    }
    return;
  } else if (stored && stored !== "zh" && !IS_BOT) {
    /* 回訪者：上次選過其他語言 → 直接進該語言的同一頁面（爬蟲不讀 localStorage，故不受影響） */
    var _rel2 = "";
    try { _rel2 = location.pathname.replace(/^\\/+/, ""); } catch (e) {}
    if (_rel2 === "index.html") _rel2 = "";
    location.replace("/" + stored + "/" + _rel2 + "?v=" + BUST_VERSION);
    return;
  } else {
    /* 根目錄固定繁體中文（不做「按瀏覽器語言自動跳轉」，只在語言不同時顯示建議條） */
    current = "zh";
  }
  if (LANGS.indexOf(current) < 0) current = "zh";
'''

HINT_BLOCK = '''
  /* ---------- 語言建議條（A+）：不強制跳轉，只提示 + 記住訪客選擇 ---------- */
  var HINT = {
    zh: { text: "本站提供繁體中文版", btn: "看中文版" },
    en: { text: "This site is available in English", btn: "View in English" },
    ja: { text: "日本語版をご用意しています", btn: "日本語で見る" },
    ko: { text: "한국어 버전을 제공하고 있습니다", btn: "한국어로 보기" },
    fr: { text: "Ce site est disponible en français", btn: "Voir en français" },
    es: { text: "Este sitio está disponible en español", btn: "Ver en español" }
  };
  var HINT_OFF_KEY = "taige_lang_hint_off";

  function sysLang() {
    var s = "";
    try { s = (navigator.language || navigator.userLanguage || "").toLowerCase(); } catch (e) {}
    var p = s.split("-")[0];
    if (p === "zh") return "zh";
    return LANGS.indexOf(p) >= 0 ? p : "en";   /* 其他語言（德/阿/泰…）→ 建議英文版 */
  }

  function samePathIn(lang) {
    var rel = location.pathname.replace(/^\\/(en|ja|ko|fr|es)\\//, "").replace(/^\\/+/, "");
    if (rel === "index.html") rel = "";
    return (lang === "zh" ? "/" : "/" + lang + "/") + rel;
  }

  function maybeShowHint() {
    if (IS_BOT) return;
    var target = sysLang();
    if (target === current) return;                       /* 已是訪客語言，不提示 */
    var off = "";
    try { off = localStorage.getItem(HINT_OFF_KEY) || ""; } catch (e) {}
    if (off.split(",").indexOf(target) >= 0) return;      /* 已被訪客關掉過 */
    var t = HINT[target] || HINT.en;
    var bar = document.createElement("div");
    bar.className = "lang-hint";
    bar.setAttribute("role", "region");
    bar.innerHTML = '<span class="lh-text"></span>' +
      '<a class="lh-btn" href="' + samePathIn(target) + '"></a>' +
      '<button class="lh-close" type="button" aria-label="Close">&#10005;</button>';
    bar.querySelector(".lh-text").textContent = t.text;
    bar.querySelector(".lh-btn").textContent = t.btn;
    document.body.insertBefore(bar, document.body.firstChild);
    bar.querySelector(".lh-btn").addEventListener("click", function () {
      try { localStorage.setItem(LANG_KEY, target); } catch (e) {}   /* 記住選擇，回訪直接進該語言 */
    });
    bar.querySelector(".lh-close").addEventListener("click", function () {
      try {
        var d = (localStorage.getItem(HINT_OFF_KEY) || "").split(",").filter(Boolean);
        if (d.indexOf(target) < 0) { d.push(target); localStorage.setItem(HINT_OFF_KEY, d.join(",")); }
      } catch (e) {}
      if (bar.parentNode) bar.parentNode.removeChild(bar);
    });
  }
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", maybeShowHint);
  } else {
    maybeShowHint();
  }
'''

CSS_BLOCK = '''

/* ============================================================
   語言建議條（A+）：系統語言 ≠ 當前頁面語言時，頂部細條提示，不強制跳轉
   ============================================================ */
.lang-hint {
  display: flex; align-items: center; justify-content: center; gap: 12px; flex-wrap: wrap;
  position: relative; padding: 9px 46px 9px 16px;
  background: var(--ink); color: #fff; font-size: 13.5px; line-height: 1.5;
  border-bottom: 2px solid var(--amber);
}
.lang-hint .lh-text { color: rgba(255, 255, 255, .9); }
.lang-hint .lh-btn {
  display: inline-block; padding: 4px 14px; border-radius: 999px;
  background: var(--amber); color: #22190a; font-weight: 600; white-space: nowrap;
  transition: background .15s ease;
}
.lang-hint .lh-btn:hover { background: #e8ab3c; }
.lang-hint .lh-close {
  position: absolute; right: 10px; top: 50%; transform: translateY(-50%);
  background: none; border: 0; color: rgba(255, 255, 255, .7);
  font-size: 14px; line-height: 1; cursor: pointer; padding: 6px 8px;
}
.lang-hint .lh-close:hover { color: #fff; }
@media (max-width: 600px) {
  .lang-hint { font-size: 12.5px; gap: 8px; padding: 8px 42px 8px 12px; justify-content: flex-start; }
}
'''

if __name__ == '__main__':
    s = open(JS, encoding='utf-8').read()
    start = s.index('  var current = null;')
    end_marker = '  if (LANGS.indexOf(current) < 0) current = "zh";'
    end = s.index(end_marker) + len(end_marker) + 1
    if '語言建議條（A+' in s:
        print('main.js 已包含建議條，跳過')
    else:
        s2 = s[:start] + NEW_DETECT + s[end:]
        anchor = '\n})();\n\n/* ---------- blog 文章頁頭部隨機背景圖'
        assert anchor in s2, '未找到 IIFE 結束錨點'
        s2 = s2.replace(anchor, '\n' + HINT_BLOCK + '})();\n\n/* ---------- blog 文章頁頭部隨機背景圖', 1)
        assert 'maybeShowHint' in s2 and 'IS_BOT' in s2
        if not DRY:
            open(JS, 'w', encoding='utf-8', newline='').write(s2)
        print('main.js 更新完成')

    c = open(CSS, encoding='utf-8').read()
    if '.lang-hint' in c:
        print('style.css 已包含 .lang-hint，跳過')
    else:
        if not DRY:
            open(CSS, 'w', encoding='utf-8', newline='').write(c.rstrip() + '\n' + CSS_BLOCK)
        print('style.css 更新完成')

    # 版本號
    import glob
    n = 0
    for p in glob.glob('**/*.html', recursive=True):
        t0 = t = open(p, encoding='utf-8').read()
        t = re.sub(r'js/main\.js\?v=[0-9.]+', 'js/main.js?v=64', t)
        t = re.sub(r'css/style\.css\?v=[0-9.]+', 'css/style.css?v=10', t)
        if t != t0:
            if not DRY:
                open(p, 'w', encoding='utf-8', newline='').write(t)
            n += 1
    print('HTML 版本號更新:', n)
    j = open(JS, encoding='utf-8').read()
    if not DRY:
        j = re.sub(r'var BUST_VERSION = "(\d+)";', lambda m: 'var BUST_VERSION = "%d";' % (int(m.group(1)) + 1), j, count=1)
        open(JS, 'w', encoding='utf-8', newline='').write(j)
    print('BUST_VERSION:', re.search(r'BUST_VERSION = "(\d+)"', j).group(1))
