/* TAGE Assist — 悬浮客服窗口（Tesla Assist 风格，四语规则匹配自动回复）
   挂载：index.html 的 #assistFab / #assistPanel；语言与 main.js 一致（?lang > localStorage > html lang） */
(function () {
  "use strict";
  var FAB = document.getElementById("assistFab");
  var PANEL = document.getElementById("assistPanel");
  var BODY = document.getElementById("assistBody");
  var QUICK = document.getElementById("assistQuick");
  var INPUT = document.getElementById("assistInput");
  var SEND = document.getElementById("assistSend");
  if (!FAB || !PANEL || !BODY || !QUICK || !INPUT || !SEND) return;

  /* ---------- 语言检测：?lang 参数 > localStorage > html lang 兜底 ---------- */
  var LANGS = ["zh", "en", "fr", "es"];
  var LANG = "zh", fromUrl = null, fromStore = null;
  try {
    var u = new URLSearchParams(location.search).get("lang");
    if (u && LANGS.indexOf(u) >= 0) fromUrl = u;
  } catch (e) {}
  try {
    var s = localStorage.getItem("taige_lang");
    if (s && LANGS.indexOf(s) >= 0) fromStore = s;
  } catch (e) {}
  LANG = fromUrl || fromStore || "zh";
  /* 仅当 URL/localStorage 都无偏好时，用 html lang 兜底 */
  if (!fromUrl && !fromStore) {
    var dl = (document.documentElement.lang || "").toLowerCase();
    if (dl.indexOf("zh") === 0) LANG = "zh";
    else if (dl.indexOf("fr") === 0) LANG = "fr";
    else if (dl.indexOf("es") === 0) LANG = "es";
    else if (dl.indexOf("en") === 0) LANG = "en";
  }

  /* ---------- 四语文案 ---------- */
  var T = {
    zh: {
      online: "在线", hello: "您好！今天有什么可以帮到您的吗？",
      ph: "输入新消息…", send: "发送",
      quick: ["你们生产哪些产品？", "最小起订量是多少？", "可以打样吗？", "怎么报价？"],
      fallback: "收到您的问题！为给您准确回复，请把详细需求发到 sales@taigetag.com 或加微信 13128118931，我们 24 小时内回复。您也可以点击页面底部「联系我们」直接询盘。",
      rules: [
        [["产品", "吊牌", "织唛", "洗水标", "包装袋", "纸袋", "画册", "生产什么"],
         "我们生产六大产品线：服装吊牌、织唛/主唛、洗水标、包装袋（胶袋/自封袋）、环保纸袋、宣传手册，全部支持定制印刷与 OEM。可浏览「产品中心」查看详情。"],
        [["起订", "moq", "最小", "数量", "多少起"],
         "起订量因产品而异：吊牌 2,000–3,000 张可试单；织唛通常 1,000 张以上；洗水标 300–500 张起。把需求发给我们，按具体产品给您准确报价。"],
        [["打样", "样品", "样板", "样版"],
         "可以！一般 1 周内寄出实物样品，并提供免费打样建议。批量下单前建议先确认印刷质量和材质手感。"],
        [["报价", "价格", "多少钱", "费用", "成本", "询价"],
         "请把设计稿或需求发到 sales@taigetag.com，我们 24 小时内回复专业报价与打样建议。也可以点击页面底部「联系我们」直接询盘。"],
        [["交期", "货期", "多久", "时间", "什么时候"],
         "打样约 3–7 天；大货交期视数量与工艺而定，通常 10–25 天。下单前会给您明确交期。"],
        [["联系", "电话", "微信", "邮箱", "地址", "怎么联系", "whatsapp"],
         "邮箱 sales@taigetag.com｜电话/微信 +86 131 2811 8931｜地址：广东省东莞市虎门镇。随时联系我们！"]
      ]
    },
    en: {
      online: "Online", hello: "Hello! How can I help you today?",
      ph: "Type a message…", send: "Send",
      quick: ["What products do you make?", "What is the MOQ?", "Can I get samples?", "How do I get a quote?"],
      fallback: "Thanks for your message! For an accurate reply, please email your requirements to sales@taigetag.com or add us on WeChat: 13128118931. We respond within 24 hours. You can also use the 'Contact' form at the bottom of the page.",
      rules: [
        [["product", "hang tag", "woven", "care label", "bag", "paper", "brochure", "make"],
         "We produce six product lines: hang tags, woven labels, care labels, packaging bags (poly/ziplock), eco paper bags and brochures — all with custom printing & OEM. Browse the Products page for details."],
        [["moq", "minimum", "quantity", "small", "order"],
         "MOQ varies by product: hang tags from 2,000–3,000 pcs for a trial order; woven labels usually 1,000+ pcs; care labels from 300–500 pcs. Send us your needs for an accurate quote."],
        [["sample", "sampling", "prototype"],
         "Yes! Physical samples are usually sent within a week, with free sampling advice. We recommend confirming print quality and material feel before bulk ordering."],
        [["quote", "price", "cost", "how much", "pricing"],
         "Please email your artwork or requirements to sales@taigetag.com — we reply with a professional quote and sampling advice within 24 hours."],
        [["lead", "delivery", "time", "long", "when"],
         "Sampling takes 3–7 days; bulk delivery is usually 10–25 days depending on quantity and finish. You'll get a confirmed schedule before ordering."],
        [["contact", "phone", "wechat", "email", "address", "reach"],
         "Email: sales@taigetag.com | Phone/WeChat: +86 131 2811 8931 | Address: Humen, Dongguan, Guangdong. Contact us anytime!"]
      ]
    },
    fr: {
      online: "En ligne", hello: "Bonjour ! Comment puis-je vous aider aujourd'hui ?",
      ph: "Écrivez votre message…", send: "Envoyer",
      quick: ["Quels produits fabriquez-vous ?", "Quelle est la quantité minimale ?", "Puis-je obtenir des échantillons ?", "Comment obtenir un devis ?"],
      fallback: "Merci pour votre message ! Pour une réponse précise, envoyez vos besoins à sales@taigetag.com ou ajoutez-nous sur WeChat : 13128118931. Nous répondons sous 24 h. Vous pouvez aussi utiliser le formulaire « Contact » en bas de page.",
      rules: [
        [["produit", "étiquette", "label", "sac", "brochure", "fabrique"],
         "Nous produisons six gammes : étiquettes suspendues, labels tissés, étiquettes d'entretien, sacs d'emballage (poly/zip), sacs papier écologiques et brochures — impression personnalisée et OEM. Voir la page Produits."],
        [["quantité", "minimum", "moq", "petite", "commande"],
         "La quantité minimale varie : étiquettes suspendues dès 2 000–3 000 pièces pour un essai ; labels tissés généralement 1 000+ ; étiquettes d'entretien dès 300–500. Envoyez-nous vos besoins pour un devis précis."],
        [["échantillon", "prototype"],
         "Oui ! Les échantillons physiques sont généralement envoyés sous une semaine, avec des conseils gratuits. Nous recommandons de vérifier la qualité d'impression avant la production en série."],
        [["devis", "prix", "coût", "combien"],
         "Envoyez votre design ou vos besoins à sales@taigetag.com — devis professionnel et conseils d'échantillonnage sous 24 h."],
        [["délai", "livraison", "temps", "quand"],
         "L'échantillonnage prend 3–7 jours ; la production 10–25 jours selon la quantité et la finition. Calendrier confirmé avant commande."],
        [["contact", "téléphone", "wechat", "email", "adresse"],
         "Email : sales@taigetag.com | Tél./WeChat : +86 131 2811 8931 | Adresse : Humen, Dongguan, Guangdong. Contactez-nous !"]
      ]
    },
    es: {
      online: "En línea", hello: "¡Hola! ¿En qué puedo ayudarte hoy?",
      ph: "Escribe un mensaje…", send: "Enviar",
      quick: ["¿Qué productos fabricáis?", "¿Cuál es el pedido mínimo?", "¿Puedo obtener muestras?", "¿Cómo obtengo un presupuesto?"],
      fallback: "¡Gracias por tu mensaje! Para una respuesta precisa, envía tus necesidades a sales@taigetag.com o agréganos en WeChat: 13128118931. Respondemos en 24 horas. También puedes usar el formulario «Contacto» al final de la página.",
      rules: [
        [["producto", "etiqueta", "tejida", "bolsa", "folleto", "fabrica"],
         "Producimos seis líneas: etiquetas colgantes, etiquetas tejidas, etiquetas de cuidado, bolsas de embalaje (polietileno/cremallera), bolsas de papel ecológicas y folletos — impresión personalizada y OEM. Ver la página de Productos."],
        [["mínimo", "moq", "cantidad", "pequeño", "pedido"],
         "El pedido mínimo varía: etiquetas colgantes desde 2.000–3.000 unidades para prueba; tejidas normalmente 1.000+; de cuidado desde 300–500. Envíanos tus necesidades para un presupuesto exacto."],
        [["muestra", "muestreo", "prototipo"],
         "¡Sí! Las muestras físicas se envían normalmente en menos de una semana, con asesoría gratuita. Recomendamos confirmar la calidad de impresión antes de la producción en masa."],
        [["presupuesto", "precio", "coste", "cuánto"],
         "Envía tu diseño o requisitos a sales@taigetag.com — presupuesto profesional y consejos de muestreo en 24 horas."],
        [["plazo", "entrega", "tiempo", "cuándo"],
         "El muestreo tarda 3–7 días; la producción 10–25 días según cantidad y acabado. Calendario confirmado antes de pedir."],
        [["contacto", "teléfono", "wechat", "email", "dirección"],
         "Email: sales@taigetag.com | Teléfono/WeChat: +86 131 2811 8931 | Dirección: Humen, Dongguan, Guangdong. ¡Contáctanos!"]
      ]
    }
  };
  var t = T[LANG];

  /* ---------- UI 初始化 ---------- */
  var headSt = document.getElementById("assistStatus");
  if (headSt) headSt.textContent = t.online;
  INPUT.placeholder = t.ph;
  SEND.textContent = t.send;

  function appendMsg(text, who) {
    var d = document.createElement("div");
    d.className = "msg " + who;
    d.textContent = text;
    BODY.appendChild(d);
    BODY.scrollTop = BODY.scrollHeight;
  }

  function renderQuick() {
    QUICK.innerHTML = "";
    t.quick.forEach(function (q) {
      var b = document.createElement("button");
      b.type = "button";
      b.textContent = q;
      b.addEventListener("click", function () { ask(q); });
      QUICK.appendChild(b);
    });
  }

  function matchReply(q) {
    var ql = q.toLowerCase();
    var rules = t.rules;
    for (var i = 0; i < rules.length; i++) {
      var kws = rules[i][0];
      for (var j = 0; j < kws.length; j++) {
        if (ql.indexOf(kws[j]) >= 0) return rules[i][1];
      }
    }
    return t.fallback;
  }

  function ask(q) {
    if (!q.trim()) return;
    appendMsg(q, "user");
    INPUT.value = "";
    setTimeout(function () { appendMsg(matchReply(q), "ai"); }, 450);
  }

  /* ---------- 事件 ---------- */
  FAB.addEventListener("click", function () {
    var open = PANEL.classList.toggle("open");
    FAB.classList.toggle("hidden", open);
    if (open) { BODY.scrollTop = BODY.scrollHeight; INPUT.focus(); }
  });
  SEND.addEventListener("click", function () { ask(INPUT.value); });
  INPUT.addEventListener("keydown", function (e) {
    if (e.key === "Enter") { e.preventDefault(); ask(INPUT.value); }
  });
  /* 点外部关闭 */
  document.addEventListener("click", function (e) {
    if (!PANEL.classList.contains("open")) return;
    if (!PANEL.contains(e.target) && e.target !== FAB && !FAB.contains(e.target)) {
      PANEL.classList.remove("open");
      FAB.classList.remove("hidden");
    }
  });

  appendMsg(t.hello, "ai");
  renderQuick();
})();
