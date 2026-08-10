/* Dongguan Tage Packaging — 语言切换(中/英/法/西) / 移动菜单 / 询盘表单
   v4.0 终极方案：语言切换改为整页跳转(?lang=xx)，页面加载时一次性应用语言。
   彻底消除移动端(iOS Safari/安卓WebView)动态改DOM导致的渲染崩溃。 */
(function () {
  "use strict";

  /* ---------- 语言检测（?lang= 参数 > localStorage > 默认zh） ---------- */
  var LANG_KEY = "taige_lang";
  var LANGS = ["zh", "en", "fr", "es"];
  /* 缓存击穿版本号：每次部署升级此值，语言跳转 URL 带 &v= 强制绕过 GitHub Pages 缓存 */
  var BUST_VERSION = "42";
  var urlLang = null;
  try {
    urlLang = new URLSearchParams(location.search).get("lang");
  } catch (e) { /* 老浏览器无 URLSearchParams 时忽略 */ }
  var current = (urlLang && LANGS.indexOf(urlLang) >= 0) ? urlLang : "zh";
  try {
    var saved = localStorage.getItem(LANG_KEY);
    if (saved && LANGS.indexOf(saved) >= 0) current = saved;
  } catch (e) { /* localStorage 不可用时忽略 */ }
  if (LANGS.indexOf(current) < 0) current = "zh";
  /* URL 参数优先，并把选择存入 localStorage 供下次访问记忆 */
  if (urlLang && LANGS.indexOf(urlLang) >= 0) {
    current = urlLang;
    try { localStorage.setItem(LANG_KEY, urlLang); } catch (e) {}
  }

  var LANG_HTML = { zh: "zh-CN", en: "en", fr: "fr", es: "es" };

  /* 只处理内容元素：跳过 void 元素与头部元素 */
  var SKIP_TAGS = { TITLE: 1, META: 1, LINK: 1, SCRIPT: 1, STYLE: 1, BR: 1, HR: 1, IMG: 1, INPUT: 1, SOURCE: 1, TRACK: 1, WBR: 1, AREA: 1, BASE: 1, COL: 1, EMBED: 1, PARAM: 1 };

  /* 页面加载时一次性应用语言（无动态切换，安全） */
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
        /* 值含 HTML 标签(<em>等)用 innerHTML 保留样式；纯文本用 textContent */
        if (/<[a-zA-Z]/.test(v)) {
          el.innerHTML = v;
        } else {
          el.textContent = v;
        }
      } catch (e) { /* 单个元素失败不影响整体 */ }
    }
    /* <title> 安全更新 */
    var titleEl = document.querySelector("title[data-zh]");
    if (titleEl) {
      try { document.title = titleEl.getAttribute("data-" + lang) || titleEl.getAttribute("data-zh"); } catch (e) {}
    }
    /* meta description 用 content 属性更新 */
    var metaEl = document.querySelector('meta[name="description"][data-zh]');
    if (metaEl) {
      try { metaEl.setAttribute("content", metaEl.getAttribute("data-" + lang) || metaEl.getAttribute("data-zh")); } catch (e) {}
    }
    /* 表单占位符 */
    var phs = document.querySelectorAll("[data-zh-ph]");
    for (var j = 0; j < phs.length; j++) {
      try {
        var p = phs[j].getAttribute("data-" + lang + "-ph");
        phs[j].setAttribute("placeholder", p != null ? p : phs[j].getAttribute("data-zh-ph"));
      } catch (e) {}
    }
    /* 语言按钮高亮 */
    var flags = document.querySelectorAll(".lang-flag");
    for (var k = 0; k < flags.length; k++) {
      try {
        flags[k].classList.toggle("active", flags[k].getAttribute("data-lang") === lang);
      } catch (e) {}
    }
  }

  /* ---------- 语言切换：整页跳转（终极方案，零动态DOM） ---------- */
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
      /* 跳转到同页面 + ?lang=xx，浏览器整页加载
         v= 参数用于绕过 GitHub Pages 的 max-age=600 缓存，
         每次部署升级 BUST_VERSION 强制所有用户加载最新 HTML */
      var path = location.pathname.split("/").pop() || "index.html";
      try { localStorage.setItem(LANG_KEY, lang); } catch (e) {}
      location.href = path + "?lang=" + lang + "&v=" + BUST_VERSION;
    });
  }

  /* 首次渲染应用语言（DOMContentLoaded 后执行，确保 DOM 完整） */
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", function () { applyLang(current); });
  } else {
    applyLang(current);
  }

  /* ---------- 移动端菜单 ---------- */
  var toggle = document.getElementById("navToggle");
  var links = document.getElementById("navLinks");
  if (toggle && links) {
    toggle.addEventListener("click", function () { links.classList.toggle("open"); });
    var linkAs = links.querySelectorAll("a");
    for (var li = 0; li < linkAs.length; li++) {
      linkAs[li].addEventListener("click", function () { links.classList.remove("open"); });
    }
  }

  /* ---------- 询盘表单 ---------- */
  var MSG = {
    email: {
      zh: "请输入有效的邮箱地址。",
      en: "Please enter a valid email address.",
      fr: "Veuillez saisir une adresse e-mail valide.",
      es: "Por favor, introduzca un correo electrónico válido."
    },
    need: {
      zh: "请填写您的需求描述。",
      en: "Please tell us what you need.",
      fr: "Veuillez décrire votre besoin.",
      es: "Por favor, descríbanos su necesidad."
    },
    subject: {
      zh: "官网询盘",
      en: "Website Inquiry",
      fr: "Demande de renseignements (site web)",
      es: "Consulta desde el sitio web"
    },
    title: {
      zh: "官网新询盘",
      en: "New Inquiry from Website",
      fr: "Nouvelle demande du site web",
      es: "Nueva consulta del sitio web"
    },
    note: {
      zh: "✓ 询盘内容已复制，并打开邮箱草稿。也可添加微信 ",
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
