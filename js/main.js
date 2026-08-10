/* Dongguan Taige Packaging — 语言切换(中/英/法/西) / 移动菜单 / 询盘表单 */
(function () {
  "use strict";

  /* ---------- 语言切换（zh/en/fr/es） ---------- */
  var LANG_KEY = "taige_lang";
  var LANGS = ["zh", "en", "fr", "es"];
  var current = localStorage.getItem(LANG_KEY) || "zh";
  if (LANGS.indexOf(current) < 0) current = "zh";

  var LANG_HTML = { zh: "zh-CN", en: "en", fr: "fr", es: "es" };

  function applyLang(lang) {
    current = lang;
    document.documentElement.lang = LANG_HTML[lang];
    document.querySelectorAll("[data-zh]").forEach(function (el) {
      // innerHTML：data 属性内容为站内自有文案，允许 <em> 等行内标签
      var v = el.getAttribute("data-" + lang);
      el.innerHTML = v != null ? v : el.getAttribute("data-zh");
    });
    document.querySelectorAll("[data-zh-ph]").forEach(function (el) {
      var p = el.getAttribute("data-" + lang + "-ph");
      el.setAttribute("placeholder", p != null ? p : el.getAttribute("data-zh-ph"));
    });
    document.querySelectorAll(".lang-flag").forEach(function (f) {
      f.classList.toggle("active", f.getAttribute("data-lang") === lang);
    });
    localStorage.setItem(LANG_KEY, lang);
  }

  var sw = document.getElementById("langSwitch");
  if (sw) sw.addEventListener("click", function (e) {
    var f = e.target.closest(".lang-flag");
    if (f) applyLang(f.getAttribute("data-lang"));
  });
  applyLang(current);

  /* ---------- 移动端菜单 ---------- */
  var toggle = document.getElementById("navToggle");
  var links = document.getElementById("navLinks");
  if (toggle && links) {
    toggle.addEventListener("click", function () { links.classList.toggle("open"); });
    links.querySelectorAll("a").forEach(function (a) {
      a.addEventListener("click", function () { links.classList.remove("open"); });
    });
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
