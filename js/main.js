/* Dongguan Taige Packaging — 语言切换 / 移动菜单 / 询盘表单 */
(function () {
  "use strict";

  /* ---------- 语言切换 ---------- */
  var LANG_KEY = "taige_lang";
  var current = localStorage.getItem(LANG_KEY) || "zh";

  function applyLang(lang) {
    current = lang;
    document.documentElement.lang = lang === "zh" ? "zh-CN" : "en";
    document.querySelectorAll("[data-zh]").forEach(function (el) {
      // innerHTML：data 属性内容为站内自有文案，允许 <em> 等行内标签
      el.innerHTML = lang === "zh" ? el.getAttribute("data-zh") : el.getAttribute("data-en");
    });
    document.querySelectorAll("[data-zh-ph]").forEach(function (el) {
      el.setAttribute("placeholder", lang === "zh" ? el.getAttribute("data-zh-ph") : el.getAttribute("data-en-ph"));
    });
    var btn = document.getElementById("langBtn");
    if (btn) btn.textContent = lang === "zh" ? "EN" : "中文";
    localStorage.setItem(LANG_KEY, lang);
  }

  var btn = document.getElementById("langBtn");
  if (btn) btn.addEventListener("click", function () {
    applyLang(current === "zh" ? "en" : "zh");
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
  var form = document.getElementById("inquiryForm");
  if (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var data = {};
      ["name", "company", "email", "phone", "country", "product", "message"].forEach(function (k) {
        var el = form.querySelector("[name=" + k + "]");
        data[k] = el ? el.value.trim() : "";
      });
      var isEn = current === "en";
      if (!data.email || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(data.email)) {
        alert(isEn ? "Please enter a valid email address." : "请输入有效的邮箱地址。");
        return;
      }
      if (!data.message) {
        alert(isEn ? "Please tell us what you need." : "请填写您的需求描述。");
        return;
      }
      // 组装询盘文本 → 微信 + 邮箱
      var lines = [];
      lines.push(isEn ? "New Inquiry from Website" : "官网新询盘");
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
        window.location.href = "mailto:" + mail + "?subject=" + encodeURIComponent(isEn ? "Website Inquiry" : "官网询盘") + "&body=" + text;
      }

      var note = document.getElementById("formNote");
      if (note) {
        note.style.color = "#2e7d4f";
        note.textContent = isEn
          ? "\u2713 Copied & email draft opened. Or send via WeChat: " + (wechat || "13128118931") + "."
          : "\u2713 询盘内容已复制，并打开邮箱草稿。也可添加微信 " + (wechat || "13128118931") + " 发送。";
      }
    });
  }
})();
