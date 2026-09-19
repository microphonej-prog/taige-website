/* Dongguan Tage Packaging — 語言切換(中/英/法/西) / 移動菜單 / 詢盤表單
   v4.0 終極方案：語言切換改爲整頁跳轉(?lang=xx)，頁面加載時一次性應用語言。
   徹底消除移動端(iOS Safari/安卓WebView)動態改DOM導致的渲染崩潰。 */
(function () {
  "use strict";

  /* ---------- 語言檢測（?lang= 參數 > localStorage > 默認zh） ---------- */
  var LANG_KEY = "taige_lang";
  var LANGS = ["zh", "en", "ja", "ko", "fr", "es"];
  /* 獨立語言目錄 /en/ /fr/ /es/：固定對應語言，忽略 ?lang/localStorage/瀏覽器語言，
     語言切換按鈕跳回根目錄對應語言版本 */
  var DIR_LANG = null;
  try {
    var _p = location.pathname;
    if (_p.indexOf("/en/") >= 0) DIR_LANG = "en";
    else if (_p.indexOf("/fr/") >= 0) DIR_LANG = "fr";
    else if (_p.indexOf("/es/") >= 0) DIR_LANG = "es";
    else if (_p.indexOf("/ja/") >= 0) DIR_LANG = "ja";
    else if (_p.indexOf("/ko/") >= 0) DIR_LANG = "ko";
  } catch (e) {}
  /* 緩存擊穿版本號：每次部署升級此值，語言跳轉 URL 帶 &v= 強制繞過 GitHub Pages 緩存 */
  var BUST_VERSION = "90";
  var urlLang = null;
  try {
    urlLang = new URLSearchParams(location.search).get("lang");
  } catch (e) { /* 老瀏覽器無 URLSearchParams 時忽略 */ }
  var current = null;
  if (DIR_LANG) {
    current = DIR_LANG;
  } else if (urlLang && LANGS.indexOf(urlLang) >= 0 && urlLang !== "zh") {
    /* 舊式 ?lang=fr 鏈接：升級跳轉到「同一頁面」的獨立語言目錄版
       （舊寫法 location.replace("../" + urlLang + "/") 在內頁會把 /blog/xxx.html 解析成 /fr/ 首頁，
       丟失原文章路徑；此處改爲按 pathname 拼接，保留內頁路徑） */
    var _rel = "";
    try { _rel = location.pathname.replace(/^\/+/, ""); } catch (e) {}
    if (!_rel || _rel === "index.html") {
      location.replace("/" + urlLang + "/?v=" + BUST_VERSION);
    } else {
      location.replace("/" + urlLang + "/" + _rel + "?v=" + BUST_VERSION);
    }
    return;
  } else {
    /* 根目錄固定中文：獨立語言目錄已上線，根目錄不再按瀏覽器語言自動切換
       （避免 Googlebot(en-US) 把中文版渲染成英文，導致 hreflang 信號衝突） */
    current = "zh";
  }
  /* 首次訪問（無 URL 參數、無歷史偏好）：按訪客系統/瀏覽器語言自動匹配。
     中文系統→中文，法/西→對應語言，其餘語言(日韓德等)→英文(國際通用)。 */
  if (!current) {
    var sys = "";
    try { sys = (navigator.language || navigator.userLanguage || "").toLowerCase(); } catch (e) {}
    if (sys.indexOf("zh") === 0) current = "zh";
    else if (sys.indexOf("fr") === 0) current = "fr";
    else if (sys.indexOf("es") === 0) current = "es";
    else if (sys.indexOf("ja") === 0) current = "ja";
    else if (sys.indexOf("ko") === 0) current = "ko";
    else if (sys.indexOf("en") === 0) current = "en";
    else current = "en";
  }
  if (LANGS.indexOf(current) < 0) current = "zh";

  var LANG_HTML = { zh: "zh-Hant", en: "en", ja: "ja", ko: "ko", fr: "fr", es: "es" };

  /* 只處理內容元素：跳過 void 元素與頭部元素 */
  var SKIP_TAGS = { TITLE: 1, META: 1, LINK: 1, SCRIPT: 1, STYLE: 1, BR: 1, HR: 1, IMG: 1, INPUT: 1, SOURCE: 1, TRACK: 1, WBR: 1, AREA: 1, BASE: 1, COL: 1, EMBED: 1, PARAM: 1 };

  /* 頁面加載時一次性應用語言（無動態切換，安全） */
  function applyLang(lang) {
    current = lang;
    try { document.documentElement.lang = LANG_HTML[lang]; } catch (e) {}
    var nodes = document.querySelectorAll("[data-zh]");
    for (var i = 0; i < nodes.length; i++) {
      var el = nodes[i];
      if (SKIP_TAGS[el.tagName]) continue;
      try {
        var v = el.getAttribute("data-" + lang);
        if (v == null) v = el.getAttribute("data-zh");
        /* 值含 HTML 標籤(<em>等)用 innerHTML 保留樣式；純文本用 textContent */
        if (/<[a-zA-Z]/.test(v)) {
          el.innerHTML = v;
        } else {
          el.textContent = v;
        }
      } catch (e) { /* 單個元素失敗不影響整體 */ }
    }
    /* <title> 安全更新 */
    var titleEl = document.querySelector("title[data-zh]");
    if (titleEl) {
      try { document.title = titleEl.getAttribute("data-" + lang) || titleEl.getAttribute("data-zh"); } catch (e) {}
    }
    /* meta description 用 content 屬性更新 */
    var metaEl = document.querySelector('meta[name="description"][data-zh]');
    if (metaEl) {
      try { metaEl.setAttribute("content", metaEl.getAttribute("data-" + lang) || metaEl.getAttribute("data-zh")); } catch (e) {}
    }
    /* 表單佔位符 */
    var phs = document.querySelectorAll("[data-zh-ph]");
    for (var j = 0; j < phs.length; j++) {
      try {
        var p = phs[j].getAttribute("data-" + lang + "-ph");
        phs[j].setAttribute("placeholder", p != null ? p : phs[j].getAttribute("data-zh-ph"));
      } catch (e) {}
    }
    /* 語言按鈕高亮 */
    var flags = document.querySelectorAll(".lang-flag");
    for (var k = 0; k < flags.length; k++) {
      try {
        flags[k].classList.toggle("active", flags[k].getAttribute("data-lang") === lang);
      } catch (e) {}
    }
  }

  /* ---------- 語言切換：跳到目標語言的獨立目錄（同頁面相對路徑） ----------
     /fr/blog/xxx.html 點 en → /en/blog/xxx.html；點 zh → /blog/xxx.html
     根目錄點 fr → /fr/（首頁）。v= 參數繞過 GitHub Pages 緩存。 */
  var sw = document.getElementById("langSwitch");
  if (sw) {
    sw.addEventListener("click", function (e) {
      var t = e.target;
      while (t && !(t.classList && t.classList.contains("lang-flag"))) {
        t = t.parentNode;
      }
      if (!t) return;
      var lang = t.getAttribute("data-lang");
      if (!lang || lang === current) return;
      var rel = location.pathname.replace(/^\/(en|ja|ko|fr|es)\//, "").replace(/^\/+|\/+$/g, "");
      if (!rel || rel === "index.html") {
        /* 首頁：根目錄 zh 用 /，語言目錄用 /xx/ */
        location.href = (lang === "zh" ? "/" : "/" + lang + "/") + "?v=" + BUST_VERSION;
      } else if (lang === "zh") {
        /* 非首頁點中文：中文版在根目錄，無 /zh/ 目錄 */
        location.href = "/" + rel + "?v=" + BUST_VERSION;
      } else {
        location.href = "/" + lang + "/" + rel + "?v=" + BUST_VERSION;
      }
      try { localStorage.setItem(LANG_KEY, lang); } catch (e) {}
    });
  }

  /* 首次渲染應用語言（DOMContentLoaded 後執行，確保 DOM 完整） */
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", function () { applyLang(current); });
  } else {
    applyLang(current);
  }

  /* ---------- 移動端菜單 ---------- */
  var toggle = document.getElementById("navToggle");
  var links = document.getElementById("navLinks");
  if (toggle && links) {
    toggle.addEventListener("click", function () { links.classList.toggle("open"); });
    var linkAs = links.querySelectorAll("a");
    for (var li = 0; li < linkAs.length; li++) {
      linkAs[li].addEventListener("click", function () { links.classList.remove("open"); });
    }
  }

  /* ---------- 詢盤表單 ---------- */
  var MSG = {
    email: {
      zh: "請輸入有效的郵箱地址。",
      en: "Please enter a valid email address.",
      fr: "Veuillez saisir une adresse e-mail valide.",
      es: "Por favor, introduzca un correo electrónico válido."
    },
    need: {
      zh: "請填寫您的需求描述。",
      en: "Please tell us what you need.",
      fr: "Veuillez décrire votre besoin.",
      es: "Por favor, descríbanos su necesidad."
    },
    subject: {
      zh: "官網詢盤",
      en: "Website Inquiry",
      fr: "Demande de renseignements (site web)",
      es: "Consulta desde el sitio web"
    },
    title: {
      zh: "官網新詢盤",
      en: "New Inquiry from Website",
      fr: "Nouvelle demande du site web",
      es: "Nueva consulta del sitio web"
    },
    note: {
      zh: "✓ 詢盤內容已複製，並打開郵箱草稿。也可添加微信 ",
      en: "✓ Copied & email draft opened. Or send via WeChat: ",
      fr: "✓ Copié et brouillon d'e-mail ouvert. Ou envoyez via WeChat : ",
      es: "✓ Copiado y borrador de correo abierto. O envíe por WeChat: "
    }
  };

  var form = document.getElementById("inquiryForm");
  if (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var data = {};
      ["name", "company", "email", "phone", "country", "product", "message"].forEach(function (k) {
        var el = form.querySelector("[name=" + k + "]");
        data[k] = el ? el.value.trim() : "";
      });
      if (!data.email || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(data.email)) {
        alert(MSG.email[current]);
        return;
      }
      if (!data.message) {
        alert(MSG.need[current]);
        return;
      }
      var lines = [];
      lines.push(MSG.title[current]);
      lines.push("Name: " + data.name);
      if (data.company) lines.push("Company: " + data.company);
      lines.push("Email: " + data.email);
      if (data.phone) lines.push("Phone/WeChat: " + data.phone);
      if (data.country) lines.push("Country: " + data.country);
      if (data.product) lines.push("Product: " + data.product);
      lines.push("Message: " + data.message);
      var plain = lines.join("\n");
      var text = encodeURIComponent(plain);

      var wechat = form.getAttribute("data-wechat") || "";
      var mail = form.getAttribute("data-mail") || "";

      function copyText(t) {
        if (navigator.clipboard && navigator.clipboard.writeText) {
          navigator.clipboard.writeText(t).then(function(){}, function(){});
        } else {
          var ta = document.createElement("textarea");
          ta.value = t;
          ta.style.position = "fixed"; ta.style.opacity = "0";
          document.body.appendChild(ta); ta.select();
          try { document.execCommand("copy"); } catch (e) {}
          document.body.removeChild(ta);
        }
      }
      copyText(plain);

      if (mail) {
        window.location.href = "mailto:" + mail + "?subject=" + encodeURIComponent(MSG.subject[current]) + "&body=" + text;
      }

      var note = document.getElementById("formNote");
      if (note) {
        note.style.color = "#2e7d4f";
        note.textContent = MSG.note[current] + (wechat || "13128118931") + ".";
      }
    });
  }
})();

/* ---------- blog 文章頁頭部隨機背景圖 ----------
   頁面 header 帶 class="random-bg" + data-bg="圖1,圖2,..."（相對路徑）時，
   每次加載隨機選一張作爲背景，疊加紅色半透明層保證文字可讀。 */
(function () {
  "use strict";
  var h = document.querySelector(".random-bg");
  if (!h) return;
  var bg = h.getAttribute("data-bg");
  if (!bg) return;
  var list = bg.split(",").map(function (s) { return s.trim(); });
  if (!list.length) return;
  var pick = list[Math.floor(Math.random() * list.length)];
  h.style.backgroundImage = "url('" + pick + "')";
  h.style.backgroundSize = "cover";
  h.style.backgroundPosition = "center";
})();
