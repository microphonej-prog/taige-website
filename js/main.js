/* Dongguan Tage Packaging — 语言切换(中/英/法/西) / 移动菜单 / 询盘表单 */
(function () {
  "use strict";

  /* ---------- 语言切换（zh/en/fr/es） ---------- */
  var LANG_KEY = "taige_lang";
  var LANGS = ["zh", "en", "fr", "es"];
  var urlLang = null;
  try {
    urlLang = new URLSearchParams(location.search).get("lang");
  } catch (e) { /* 老浏览器无 URLSearchParams 时忽略 */ }
  var current = (urlLang && LANGS.indexOf(urlLang) >= 0) ? urlLang : "zh";
  try {
    current = (localStorage.getItem(LANG_KEY) && LANGS.indexOf(localStorage.getItem(LANG_KEY)) >= 0)
      ? localStorage.getItem(LANG_KEY) : current;
  } catch (e) { /* localStorage 不可用时忽略 */ }
  if (LANGS.indexOf(current) < 0) current = "zh";

  var LANG_HTML = { zh: "zh-CN", en: "en", fr: "fr", es: "es" };

  /* 只处理内容元素：跳过 title/meta/link/script/style/br/hr/img/input 等
     void 元素或头部元素——对它们设 innerHTML 在部分移动 WebView 会抛异常 */
  var SKIP_TAGS = { TITLE: 1, META: 1, LINK: 1, SCRIPT: 1, STYLE: 1, BR: 1, HR: 1, IMG: 1, INPUT: 1, SOURCE: 1, TRACK: 1, WBR: 1, AREA: 1, BASE: 1, COL: 1, EMBED: 1, PARAM: 1 };

  function applyLang(lang) {
    /* 切换前：记住滚动位置 + 暂停所有视频（防止切换时视频重载卡顿） */
    var scrollPos = 0;
    try { scrollPos = window.pageYOffset || document.documentElement.scrollTop || 0; } catch (e) {}
    var vids = document.querySelectorAll("video");
    for (var vi = 0; vi < vids.length; vi++) {
      try { vids[vi].pause(); } catch (e) {}
    }

    current = lang;
    document.documentElement.lang = LANG_HTML[lang];
    var nodes = document.querySelectorAll("[data-zh]");
    for (var i = 0; i < nodes.length; i++) {
      var el = nodes[i];
      if (SKIP_TAGS[el.tagName]) continue;
      try {
        var v = el.getAttribute("data-" + lang);
        /* 用 textContent 而非 innerHTML：data 值均为纯文本，
           innerHTML 会把撇号/特殊字符当 HTML 解析，在移动端
           (iOS Safari / 安卓 WebView) 会触发渲染崩溃 */
        el.textContent = v != null ? v : el.getAttribute("data-zh");
      } catch (e) {
        /* 单个元素失败不影响其余语言切换 */
      }
    }
    /* 单独处理 <title>：改标题是安全的 */
    var titleEl = document.querySelector("title[data-zh]");
    if (titleEl) {
      var tv = titleEl.getAttribute("data-" + lang) || titleEl.getAttribute("data-zh");
      try { document.title = tv; } catch (e) {}
    }
    /* 单独处理 meta description（用 content 属性，而不是 innerHTML） */
    var metaEl = document.querySelector('meta[name="description"][data-zh]');
    if (metaEl) {
      var mv = metaEl.getAttribute("data-" + lang) || metaEl.getAttribute("data-zh");
      try { metaEl.setAttribute("content", mv); } catch (e) {}
    }
    /* 占位符（表单输入） */
    var phs = document.querySelectorAll("[data-zh-ph]");
    for (var j = 0; j < phs.length; j++) {
      var phEl = phs[j];
      try {
        var p = phEl.getAttribute("data-" + lang + "-ph");
        phEl.setAttribute("placeholder", p != null ? p : phEl.getAttribute("data-zh-ph"));
      } catch (e) {}
    }
    /* 语言按钮高亮 */
    var flags = document.querySelectorAll(".lang-flag");
    for (var k = 0; k < flags.length; k++) {
      try {
        flags[k].classList.toggle("active", flags[k].getAttribute("data-lang") === lang);
      } catch (e) {}
    }
    try { localStorage.setItem(LANG_KEY, lang); } catch (e) {}

    /* 切换后：恢复滚动位置（放在 requestAnimationFrame 里确保布局已更新） */
    try {
      window.scrollTo(0, scrollPos);
    } catch (e) {}
  }

  var sw = document.getElementById("langSwitch");
  if (sw) sw.addEventListener("click", function (e) {
    var t = e.target;
    /* 兼容：点击 SVG 内部元素时向上查找 .lang-flag */
    while (t && !(t.classList && t.classList.contains("lang-flag"))) {
      t = t.parentNode;
    }
    if (t) applyLang(t.getAttribute("data-lang"));
  });
  applyLang(current);

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
      // 组装询盘文本 → 微信 + 邮箱
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

      // 复制询盘内容（供微信粘贴发送）
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

      // 打开邮箱草稿
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
