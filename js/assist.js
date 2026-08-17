/* TAGE Assist — 悬浮客服窗口 v2（智能多轮对话引擎）
   实现：意图识别 + 对话上下文 + 追问引导，四语。
   说明：静态站前端无法直连 LLM（密钥泄露风险），此引擎用规则+上下文模拟智能客服。
   挂载：各页面 #assistFab / #assistPanel；语言与 main.js 一致。 */
(function () {
  "use strict";
  var FAB = document.getElementById("assistFab");
  var PANEL = document.getElementById("assistPanel");
  var BODY = document.getElementById("assistBody");
  var QUICK = document.getElementById("assistQuick");
  var INPUT = document.getElementById("assistInput");
  var SEND = document.getElementById("assistSend");
  if (!FAB || !PANEL || !BODY || !QUICK || !INPUT || !SEND) return;

  /* ---------- 语言检测：?lang > localStorage > html lang ---------- */
  var LANGS = ["zh", "en", "fr", "es"];
  /* 独立语言目录 /en/ /fr/ /es/：固定对应语言（该目录页面已静态渲染） */
  var DIR_LANG = null;
  try {
    var _p = location.pathname;
    if (_p.indexOf("/en/") >= 0) DIR_LANG = "en";
    else if (_p.indexOf("/fr/") >= 0) DIR_LANG = "fr";
    else if (_p.indexOf("/es/") >= 0) DIR_LANG = "es";
  } catch (e) {}
  var LANG = "zh", fromUrl = null, fromStore = null;
  if (DIR_LANG) {
    LANG = DIR_LANG;
  } else {
  try {
    var u = new URLSearchParams(location.search).get("lang");
    if (u && LANGS.indexOf(u) >= 0) fromUrl = u;
  } catch (e) {}
  try {
    var s = localStorage.getItem("taige_lang");
    if (s && LANGS.indexOf(s) >= 0) fromStore = s;
  } catch (e) {}
  LANG = fromUrl || fromStore || "zh";
  if (!fromUrl && !fromStore) {
    var dl = (document.documentElement.lang || "").toLowerCase();
    if (dl.indexOf("zh") === 0) LANG = "zh";
    else if (dl.indexOf("fr") === 0) LANG = "fr";
    else if (dl.indexOf("es") === 0) LANG = "es";
    else if (dl.indexOf("en") === 0) LANG = "en";
  }
  }
  /* ================= 四语知识库 ================= */
  function T() {}
  T.zh = {
    online: "在线", hello: "您好！我是泰阁智能客服 🐓 关于吊牌、织唛、洗水标、包装袋的任何问题都可以问我，也可以直接告诉我您的需求～",
    ph: "输入您的问题…", send: "发送",
    quick: ["你们有哪些产品？", "最小起订量是多少？", "可以打样吗？", "怎么报价？"],
    followupQuote: "💡 提示：把设计稿或数量发到 sales@taigetag.com，24 小时内给您精确报价；加微信 13128118931 沟通更快～",
    fallback: "这个问题我需要确认一下 🤔 建议把具体需求发到 sales@taigetag.com 或加微信 13128118931，我们专业同事 24 小时内给您准确答复。也可以点页面底部「联系方式」直接留言。",
    intents: [
      { id: "hello", kws: ["你好", "您好", "嗨", "哈喽", "hello", "hi", "在吗", "在不在"], reply: "您好！有什么可以帮您？😊 可以问产品、起订量、打样、报价，也可以直接说您的需求。" },
      { id: "thanks", kws: ["谢谢", "感谢", "thank", "merci", "gracias", "3q", "thx"], reply: "不客气！随时找我 😄 有样品或报价需求，随时发我。" },
      { id: "bye", kws: ["再见", "拜拜", "bye", "88", "goodbye"], reply: "再见！祝您生意兴隆 🚀 需要时随时来问～" },
      { id: "product", kws: ["产品", "什么", "有哪些", "做什么", "品类", "product", "produce", "offre", "productos"], reply: "我们有六大产品线：\n① 服装吊牌（铜版纸/牛皮纸/PVC，烫金 UV 哑膜）\n② 织唛/主唛（缎面/提花/双层织边）\n③ 洗水标（织带/涂层/印刷）\n④ 包装袋（PE 胶袋/自封袋/防静电袋）\n⑤ 环保纸袋（牛皮纸/白卡纸）\n⑥ 宣传手册（画册/折页）\n全部支持定制和 OEM。您对哪一类感兴趣？" },
      { id: "hangtag", kws: ["吊牌", "挂卡", "hangtag", "hang tag", "étiquette suspendue", "etiqueta colgante", "标签卡"], reply: "吊牌是我们主打产品 👍 材质有铜版纸（300-400克）、牛皮纸、棉纸、PVC 防水等；工艺支持烫金、压凹凸、UV 局部上光、覆膜；尺寸常规 35×70 / 40×90 / 50×90mm，也能异形模切。需要我帮您看看材质怎么选吗？" },
      { id: "woven", kws: ["织唛", "主唛", "缎面", "提花", "woven", "tissé", "tejida", "商标"], reply: "织唛/主唛有缎面、平纹、提花、双层织边等织法，图案细腻、耐水洗不褪色。建议：主唛用缎面/提花显高档，尺码唛用塔夫绸。您需要主唛还是尺码唛？" },
      { id: "carelabel", kws: ["洗水标", "洗标", "水洗标", "care label", "entretien", "de cuidado"], reply: "洗水标有三种：织带洗标、涂层洗标、印刷洗标，符合各国洗涤标准，信息清晰持久。常见组合是「织唛主唛 + 印刷洗水标」，兼顾档次和成本。需要按您的洗涤要求推荐吗？" },
      { id: "bags", kws: ["包装袋", "胶袋", "自封袋", "拉链袋", "包装袋", "poly bag", "ziplock", "sac", "bolsa"], reply: "包装袋有 PE/CPE 胶袋、拉链袋、自封袋、防静电袋，可印刷品牌 LOGO，尺寸厚度按需定制。服装出口常用的 OPP 透明袋性价比很高 👍" },
      { id: "paperbag", kws: ["纸袋", "牛皮纸袋", "环保袋", "paper bag", "kraft", "sac papier", "bolsa de papel"], reply: "环保纸袋用牛皮纸或白卡纸，可降解环保，支持品牌印刷和定制提手——欧盟客户很看重这个 🌱 需要看环保选项吗？" },
      { id: "brochure", kws: ["画册", "手册", "折页", "目录", "brochure", "catalogue", "folleto"], reply: "宣传手册/画册/产品目录都可以做，从纸张选型到装订全程把控品质。把您的品牌 VI 发我们，设计部免费出排版建议。" },
      { id: "moq", kws: ["起订", "moq", "最小", "多少起", "数量", "minimum", "quantité", "mínimo"], reply: function (st) {
        if (st.topic === "hangtag") return "吊牌起订量：2,000–3,000 张可试单，10,000+ 张单价更划算。您计划要多少？";
        if (st.topic === "woven") return "织唛一般 1,000 张以上起做，提花/双层织边工艺价格略有不同。需要精确数量吗？";
        if (st.topic === "carelabel") return "洗水标 300–500 张就能起做，成本很友好 👍 您需要哪种（织带/涂层/印刷）？";
        if (st.topic === "bags" || st.topic === "paperbag") return "包装袋起订量比较灵活，按尺寸和印刷谈，几百个样品袋也可以做。您要多大的？";
        return "起订量因产品不同：吊牌 2,000–3,000 张试单；织唛 1,000 张以上；洗水标 300–500 张起；包装袋灵活。您做哪类产品？";
      } },
      { id: "sample", kws: ["打样", "样品", "样板", "样版", "sample", "échantillon", "muestra", "打版"], reply: "可以打样！一般 3–7 天内寄出实物样品，并提供免费打样建议。批量下单前先确认印刷质量和材质手感，是我们给所有客户的建议 😊 您方便发个设计稿或参考图吗？" },
      { id: "quote", kws: ["报价", "价格", "多少钱", "费用", "成本", "怎么算", "询价", "quote", "price", "cost", "devis", "prix", "presupuesto", "precio"], reply: function (st, tt) {
        if (st.topic === "hangtag") return "吊牌的话，价格主要看材质、尺寸、印色数和工艺：铜版纸常规款千张级单价很友好，烫金/异形模切会高一些。您大概要多少数量？把设计发到 sales@taigetag.com 我们能报精确价 😊";
        if (st.topic === "woven") return "织唛报价要看织法（缎面/提花/双层）和尺寸，一般 1,000 张以上起做。发设计稿给我们，24 小时内出精确报价～";
        if (st.topic === "carelabel") return "洗水标价格按材质（织带/涂层/印刷）和数量算，300–500 张就能做，价格很友好。需要报哪种？";
        if (st.topic === "bags" || st.topic === "paperbag") return "包装袋报价要看尺寸、厚度、印刷和数量。发需求给我们（尺寸+数量+要不要印 LOGO），24 小时内出报价 👍";
        return "好的！为了报得准，需要知道：① 产品类型 ② 数量 ③ 设计/尺寸。您先告诉我哪种产品，其余的发到 sales@taigetag.com 就行 😊";
      } },
      { id: "leadtime", kws: ["交期", "货期", "多久", "多长时间", "什么时候", "lead", "delivery", "délai", "plazo", "几天"], reply: "打样一般 3–7 天；大货交期看数量和工艺，通常 10–25 天。下单前会给您书面确认的交期，不用担心 😊" },
      { id: "payment", kws: ["付款", "怎么付", "定金", "tt", "信用证", "l/c", "payment", "paiement", "pago"], reply: "常规合作：30% 定金 + 70% 尾款发货前付清；支持 T/T 银行转账，大单也可谈信用证。新客户首次合作我们会给详细的付款条款。" },
      { id: "shipping", kws: ["运费", "物流", "快递", "海运", "空运", "fob", "exw", "shipping", "freight", "expédition", "envío"], reply: "支持多种出货方式：FOB 深圳/广州、EXW 工厂，或我们帮您安排海运/空运/快递（DHL、FedEx、UPS 等）。小批量样品走快递最划算 📦" },
      { id: "oem", kws: ["定制", "oem", "odm", "来样", "设计", "logo", "custom", "personnalisé", "personalizado"], reply: "支持 OEM/ODM 和来样定制！设计部可帮您优化稿件，颜色、材质、工艺灵活组合，从打样到量产一条龙。您有自己的设计稿还是需要我们设计？" },
      { id: "quality", kws: ["质量", "质检", "品控", "合格", "quality", "qc", "qualité", "calidad", "认证"], reply: "我们执行完整品控流程：原材料检验 → 印刷过程抽检 → 成品全检 → 出货前复检。公司持有营业执照及各类资质，可提供检测报告 📋" },
      { id: "company", kws: ["公司", "工厂", "介绍", "泰阁", "tage", "哪里", "地址", "company", "factory", "entreprise", "empresa"], reply: "东莞泰阁包装制品有限公司（Dongguan Tage Packaging Products Co., Ltd.）位于广东东莞虎门，专注服装辅料 20 年：吊牌、织唛、洗水标、包装袋一站式生产，出口全球 40+ 国家 🇨🇳🌍" },
      { id: "contact", kws: ["联系", "电话", "微信", "邮箱", "email", "电话", "whatsapp", "contact", "téléphone", "wechat", "contacto"], reply: "随时联系！📧 sales@taigetag.com ｜📱 电话/WhatsApp/微信：+86 131 2811 8931 ｜📍 广东省东莞市虎门镇。发需求一般 24 小时内回复（工作时间更快）😊" },
      { id: "order", kws: ["下单", "订购", "买", "怎么合作", "流程", "order", "commande", "pedido"], reply: "合作流程很简单：① 发需求/设计稿 → ② 我们 24 小时内报价 → ③ 确认打样 → ④ 样品确认后量产 → ⑤ 验货出货。您可以从任意一步开始！" },
      { id: "faq", kws: ["常见问题", "faq", "问题", "help", "aide"], reply: "常见问题速答：\n📦 起订量：吊牌 2,000+、织唛 1,000+、洗水标 300+ \n🧪 打样：3–7 天寄样\n💰 报价：24 小时内\n🚚 交期：10–25 天\n更多细节直接问我～" }
    ]
  };
  T.en = {
    online: "Online", hello: "Hi! I'm TAGE's smart assistant 🐓 Ask me anything about hang tags, woven labels, care labels or packaging bags — or just tell me your needs.",
    ph: "Type your message…", send: "Send",
    quick: ["What products do you make?", "What is the MOQ?", "Can I get samples?", "How do I get a quote?"],
    followupQuote: "💡 Tip: email your artwork or quantities to sales@taigetag.com for an exact quote within 24h. WeChat: 13128118931 is even faster.",
    fallback: "Let me check on that 🤔 Please email your specific requirements to sales@taigetag.com or add us on WeChat 13128118931 — our team replies within 24 hours. You can also use the Contact form at the bottom of the page.",
    intents: [
      { id: "hello", kws: ["hello", "hi", "hey", "你好", "在吗"], reply: "Hello! How can I help? 😊 Ask about products, MOQ, sampling or quotes — or just describe your needs." },
      { id: "thanks", kws: ["thanks", "thank", "thx", "merci", "gracias"], reply: "You're welcome! 😄 Feel free to reach out anytime for samples or quotes." },
      { id: "bye", kws: ["bye", "goodbye", "see you"], reply: "Goodbye! Wishing you great business 🚀 Come back anytime." },
      { id: "product", kws: ["product", "what do you make", "range", "offer", "品类", "产品"], reply: "We produce six lines:\n① Hang tags (art/kraft/PVC paper, foil/UV/matte)\n② Woven labels (satin/jacquard/double-layer)\n③ Care labels (woven/coated/printed)\n④ Packaging bags (PE/ziplock/anti-static)\n⑤ Eco paper bags (kraft/art card)\n⑥ Brochures & catalogs\nAll custom & OEM. Which one interests you?" },
      { id: "hangtag", kws: ["hangtag", "hang tag", "tag", "吊牌"], reply: "Hang tags are our specialty 👍 Materials: art paper (300-400gsm), kraft, cotton, waterproof PVC. Finishes: hot foil, embossing, spot UV, lamination. Sizes 35×70 / 40×90 / 50×90mm or custom die-cut. Need material advice?" },
      { id: "woven", kws: ["woven", "satin", "jacquard", "主唛", "织唛"], reply: "Woven labels: satin, plain, jacquard, double-layer edge — fine detail, wash-resistant. Satin/jacquard for main labels, taffeta for size labels. Main label or size label?" },
      { id: "carelabel", kws: ["care label", "washing", "洗水标"], reply: "Care labels: woven tape, coated or printed — meeting international care standards, clear and durable. A common combo: woven main label + printed care label. Need a recommendation?" },
      { id: "bags", kws: ["bag", "poly", "ziplock", "包装袋"], reply: "Bags: PE/CPE poly, zipper, self-seal, anti-static — printable with your logo, custom size & thickness. Clear OPP bags are great value for apparel export 👍" },
      { id: "paperbag", kws: ["paper bag", "kraft", "eco bag", "纸袋"], reply: "Eco paper bags in kraft or art card — biodegradable, printable, custom handles. EU buyers love these 🌱" },
      { id: "brochure", kws: ["brochure", "catalog", "flyer", "画册"], reply: "Brochures, catalogs and flyers — full quality control from paper to binding. Send your brand VI and our design team will advise for free." },
      { id: "moq", kws: ["moq", "minimum", "quantity", "起订"], reply: function (st) {
        if (st.topic === "hangtag") return "Hang tag MOQ: 2,000–3,000 pcs trial; unit price drops significantly at 10,000+. How many do you need?";
        if (st.topic === "woven") return "Woven labels usually start at 1,000+ pcs; jacquard/double-layer vary slightly. Need an exact quantity?";
        if (st.topic === "carelabel") return "Care labels from 300–500 pcs — very budget-friendly 👍 Which type (woven/coated/printed)?";
        if (st.topic === "bags" || st.topic === "paperbag") return "Bag MOQ is flexible by size and printing — even a few hundred sample bags. What size?";
        return "MOQ varies: hang tags 2,000–3,000 trial; woven 1,000+; care labels 300–500; bags flexible. Which product?";
      } },
      { id: "sample", kws: ["sample", "prototype", "打样"], reply: "Yes, we sample! Physical samples within 3–7 days, with free sampling advice. We always recommend confirming print quality before bulk orders 😊 Can you share an artwork or reference?" },
      { id: "quote", kws: ["quote", "price", "cost", "how much", "报价"], reply: function (st) {
        if (st.topic === "hangtag") return "For hang tags, price depends on material, size, colors and finish — standard art paper is very friendly at thousand-pc levels; foil or die-cut costs a bit more. What quantity do you need? Email artwork to sales@taigetag.com for an exact quote 😊";
        if (st.topic === "woven") return "Woven label quotes depend on weave (satin/jacquard/double) and size, usually 1,000+ pcs. Send your artwork and we'll quote within 24h!";
        if (st.topic === "carelabel") return "Care labels are priced by material (woven/coated/printed) and quantity — from 300–500 pcs, very budget-friendly. Which type?";
        if (st.topic === "bags" || st.topic === "paperbag") return "Bag quotes depend on size, thickness, printing and quantity. Send us size + qty + logo requirement, quote within 24h 👍";
        return "To quote accurately we need: ① product type ② quantity ③ artwork/size. Tell me the product first, then email the rest to sales@taigetag.com 😊";
      } },
      { id: "leadtime", kws: ["lead time", "delivery", "how long", "交期"], reply: "Sampling: 3–7 days. Bulk delivery: usually 10–25 days depending on quantity and finish. Written confirmation before you order 😊" },
      { id: "payment", kws: ["payment", "deposit", "tt", "l/c", "付款"], reply: "Standard terms: 30% deposit, 70% balance before shipment. Bank T/T accepted; L/C negotiable for large orders. Full payment terms for first orders." },
      { id: "shipping", kws: ["shipping", "freight", "fob", "exw", "dhl", "物流"], reply: "FOB Shenzhen/Guangzhou, EXW factory, or we arrange sea/air/express (DHL, FedEx, UPS). Express is most economical for small sample parcels 📦" },
      { id: "oem", kws: ["oem", "odm", "custom", "logo", "design", "定制"], reply: "OEM/ODM and sample-based customization supported! Our design team helps optimize artwork — colors, materials, finishes all flexible, from sampling to mass production. Do you have artwork or need design help?" },
      { id: "quality", kws: ["quality", "qc", "certification", "质量"], reply: "Full QC process: raw material inspection → in-process checks → final inspection → pre-shipment review. Business license and certificates available; test reports on request 📋" },
      { id: "company", kws: ["company", "factory", "where", "about", "tage"], reply: "Dongguan Tage Packaging Products Co., Ltd. — Humen, Dongguan, Guangdong. 20 years in garment trims: hang tags, woven labels, care labels, bags — one-stop, exporting to 40+ countries 🇨🇳🌍" },
      { id: "contact", kws: ["contact", "phone", "email", "wechat", "whatsapp"], reply: "Contact us anytime! 📧 sales@taigetag.com ｜ 📱 Phone/WhatsApp/WeChat: +86 131 2811 8931 ｜ 📍 Humen, Dongguan, Guangdong. Replies within 24h (faster during work hours) 😊" },
      { id: "order", kws: ["order", "process", "how to buy", "下单"], reply: "Simple process: ① send requirements/artwork → ② quote within 24h → ③ sampling → ④ mass production after approval → ⑤ QC & shipping. Start from any step!" },
      { id: "faq", kws: ["faq", "help", "question"], reply: "Quick answers:\n📦 MOQ: hang tags 2,000+, woven 1,000+, care labels 300+\n🧪 Sampling: 3–7 days\n💰 Quote: within 24h\n🚚 Delivery: 10–25 days\nAsk me anything else!" }
    ]
  };
  T.fr = {
    online: "En ligne", hello: "Bonjour ! Je suis l'assistant intelligent de TAGE 🐓 Posez-moi toutes vos questions sur les étiquettes, labels, sacs… ou décrivez simplement votre besoin.",
    ph: "Écrivez votre message…", send: "Envoyer",
    quick: ["Quels produits fabriquez-vous ?", "Quelle est la quantité minimale ?", "Puis-je obtenir des échantillons ?", "Comment obtenir un devis ?"],
    followupQuote: "💡 Astuce : envoyez votre design ou vos quantités à sales@taigetag.com — devis précis sous 24 h. WeChat : 13128118931 encore plus rapide.",
    fallback: "Je vérifie 🤔 Envoyez vos besoins précis à sales@taigetag.com ou ajoutez-nous sur WeChat 13128118931 — réponse sous 24 h. Vous pouvez aussi utiliser le formulaire de contact en bas de page.",
    intents: [
      { id: "hello", kws: ["bonjour", "salut", "hello", "bonsoir"], reply: "Bonjour ! Comment puis-je vous aider ? 😊 Produits, quantités, échantillons, devis — ou décrivez votre besoin." },
      { id: "thanks", kws: ["merci", "thank"], reply: "Avec plaisir ! 😄 N'hésitez pas à revenir pour des échantillons ou devis." },
      { id: "bye", kws: ["au revoir", "bye", "bonne journée"], reply: "Au revoir ! Très bonne affaire 🚀 Revenez quand vous voulez." },
      { id: "product", kws: ["produit", "fabriquez", "gamme", "offre"], reply: "Six gammes : ① étiquettes suspendues (papier/PVC, dorure/UV) ② labels tissés (satin/jacquard) ③ étiquettes d'entretien ④ sacs d'emballage (PE/zip) ⑤ sacs papier écologiques ⑥ brochures. Tout en personnalisé & OEM. Laquelle vous intéresse ?" },
      { id: "hangtag", kws: ["étiquette suspendue", "étiquette", "hangtag"], reply: "Les étiquettes suspendues sont notre spécialité 👍 Papier couché (300-400 g/m²), kraft, coton, PVC. Dorure, gaufrage, UV, pelliculage. Tailles 35×70 / 40×90 / 50×90 mm ou découpe personnalisée. Besoin de conseils matériaux ?" },
      { id: "woven", kws: ["tissé", "satin", "jacquard", "label"], reply: "Labels tissés : satin, toile, jacquard, double lisière — détails fins, résistants au lavage. Satin/jacquard pour le label principal, taffetas pour la taille. Principal ou taille ?" },
      { id: "carelabel", kws: ["entretien", "lavage", "composition"], reply: "Étiquettes d'entretien : tissées, enduites ou imprimées — conformes aux normes internationales. Combo courant : label principal tissé + étiquette d'entretien imprimée." },
      { id: "bags", kws: ["sac", "polyéthylène", "zip", "emballage"], reply: "Sacs : PE/CPE, à zip, auto-adhésifs, antistatiques — imprimables, tailles et épaisseurs sur mesure. Les sacs OPP transparents sont très économiques pour l'export 👍" },
      { id: "paperbag", kws: ["sac papier", "kraft", "écologique"], reply: "Sacs papier kraft ou couché — biodégradables, imprimables, anses personnalisées. Les clients européens apprécient 🌱" },
      { id: "brochure", kws: ["brochure", "catalogue", "dépliant"], reply: "Brochures, catalogues, dépliants — contrôle qualité complet du papier à la reliure. Envoyez votre charte graphique, conseils gratuits." },
      { id: "moq", kws: ["quantité", "minimum", "moq"], reply: function (st) {
        if (st.topic === "hangtag") return "Étiquettes suspendues : 2 000–3 000 pièces pour un essai ; le prix unitaire baisse nettement à 10 000+. Combien vous en faut-il ?";
        if (st.topic === "woven") return "Labels tissés : généralement 1 000+ pièces ; jacquard/double lisière varie un peu. Quantité exacte ?";
        if (st.topic === "carelabel") return "Étiquettes d'entretien dès 300–500 pièces — très économique 👍 Quel type (tissée/enduite/imprimée) ?";
        if (st.topic === "bags" || st.topic === "paperbag") return "Quantité flexible selon taille et impression — même quelques centaines pour des échantillons. Quelle taille ?";
        return "Quantités minimales : étiquettes 2 000–3 000 essai ; tissés 1 000+ ; entretien 300–500 ; sacs flexibles. Quel produit ?";
      } },
      { id: "sample", kws: ["échantillon", "prototype", "essai"], reply: "Oui ! Échantillons physiques sous 3–7 jours, conseils gratuits. Vérifiez toujours la qualité d'impression avant la production 😊 Un design à nous envoyer ?" },
      { id: "quote", kws: ["devis", "prix", "coût", "combien"], reply: function (st) {
        if (st.topic === "hangtag") return "Pour les étiquettes, le prix dépend du matériau, de la taille, des couleurs et de la finition — le papier couché standard est très accessible dès 1 000 pièces. Quelle quantité ? Envoyez le design à sales@taigetag.com pour un devis exact 😊";
        if (st.topic === "woven") return "Le devis tissé dépend du tissage et de la taille, généralement 1 000+ pièces. Envoyez votre design, devis sous 24 h !";
        if (st.topic === "carelabel") return "Prix selon le matériau (tissé/enduite/imprimée) et la quantité — dès 300–500 pièces. Quel type ?";
        if (st.topic === "bags" || st.topic === "paperbag") return "Le devis dépend de la taille, de l'épaisseur, de l'impression et de la quantité. Envoyez dimensions + quantité + logo, devis sous 24 h 👍";
        return "Pour un devis précis : ① type de produit ② quantité ③ design/taille. Dites-moi le produit d'abord, puis envoyez le reste à sales@taigetag.com 😊";
      } },
      { id: "leadtime", kws: ["délai", "livraison", "temps"], reply: "Échantillonnage : 3–7 jours. Production : généralement 10–25 jours selon quantité et finition. Confirmation écrite avant commande 😊" },
      { id: "payment", kws: ["paiement", "acompte", "tt", "l/c"], reply: "Conditions : 30 % d'acompte, 70 % avant expédition. Virement bancaire accepté ; L/C négociable pour les grosses commandes." },
      { id: "shipping", kws: ["expédition", "fret", "fob", "exw", "dhl"], reply: "FOB Shenzhen/Guangzhou, EXW usine, ou nous organisons maritime/aérien/express (DHL, FedEx, UPS). L'express est idéal pour les petits échantillons 📦" },
      { id: "oem", kws: ["oem", "odm", "personnalisé", "logo", "design"], reply: "OEM/ODM et fabrication sur échantillon ! Notre équipe design optimise vos visuels — couleurs, matériaux, finitions flexibles, du prototype à la série. Vous avez un design ou besoin d'aide ?" },
      { id: "quality", kws: ["qualité", "qc", "certification"], reply: "Contrôle qualité complet : inspection matières premières → contrôles en cours → inspection finale → revue avant expédition. Licence et certificats disponibles 📋" },
      { id: "company", kws: ["entreprise", "usine", "tage", "où"], reply: "Dongguan Tage Packaging Products Co., Ltd. — Humen, Dongguan, Guangdong. 20 ans d'expérience : étiquettes, labels, sacs — production intégrée, export vers 40+ pays 🇨🇳🌍" },
      { id: "contact", kws: ["contact", "téléphone", "email", "wechat", "whatsapp"], reply: "Contactez-nous ! 📧 sales@taigetag.com ｜ 📱 Tél./WhatsApp/WeChat : +86 131 2811 8931 ｜ 📍 Humen, Dongguan, Guangdong. Réponse sous 24 h 😊" },
      { id: "order", kws: ["commande", "processus", "acheter"], reply: "Processus simple : ① envoyez vos besoins → ② devis sous 24 h → ③ échantillonnage → ④ production après validation → ⑤ contrôle et expédition. Commencez à n'importe quelle étape !" },
      { id: "faq", kws: ["faq", "aide", "question"], reply: "Réponses rapides : 📦 Quantités : étiquettes 2 000+, tissés 1 000+, entretien 300+ ｜ 🧪 Échantillons : 3–7 jours ｜ 💰 Devis : sous 24 h ｜ 🚚 Délai : 10–25 jours. Autres questions ?" }
    ]
  };
  T.es = {
    online: "En línea", hello: "¡Hola! Soy el asistente inteligente de TAGE 🐓 Pregúntame sobre etiquetas, tejidas, bolsas… o cuéntame tu necesidad.",
    ph: "Escribe un mensaje…", send: "Enviar",
    quick: ["¿Qué productos fabricáis?", "¿Cuál es el pedido mínimo?", "¿Puedo obtener muestras?", "¿Cómo obtengo un presupuesto?"],
    followupQuote: "💡 Consejo: envía tu diseño o cantidades a sales@taigetag.com — presupuesto exacto en 24 h. WeChat: 13128118931 aún más rápido.",
    fallback: "Déjame comprobarlo 🤔 Envía tus requisitos a sales@taigetag.com o agréganos en WeChat 13128118931 — respondemos en 24 h. También puedes usar el formulario de contacto al final de la página.",
    intents: [
      { id: "hello", kws: ["hola", "buenos días", "hello", "hi"], reply: "¡Hola! ¿En qué puedo ayudarte? 😊 Productos, cantidades, muestras, presupuesto — o cuéntame tu necesidad." },
      { id: "thanks", kws: ["gracias", "thank"], reply: "¡De nada! 😄 Vuelve cuando quieras muestras o presupuestos." },
      { id: "bye", kws: ["adiós", "bye", "hasta luego"], reply: "¡Adiós! Mucho éxito en tu negocio 🚀 Vuelve cuando quieras." },
      { id: "product", kws: ["producto", "fabrica", "gama", "ofrece"], reply: "Seis líneas: ① etiquetas colgantes (papel/PVC, dorado/UV) ② tejidas (satén/jacquard) ③ de cuidado ④ bolsas (PE/cremallera) ⑤ bolsas de papel ecológicas ⑥ folletos. Todo personalizado y OEM. ¿Cuál te interesa?" },
      { id: "hangtag", kws: ["etiqueta colgante", "etiqueta", "hangtag"], reply: "Las etiquetas colgantes son nuestra especialidad 👍 Papel estucado (300-400 g/m²), kraft, algodón, PVC. Estampado, relieve, UV, laminado. Tamaños 35×70 / 40×90 / 50×90 mm o troquelado. ¿Consejos de material?" },
      { id: "woven", kws: ["tejida", "satén", "jacquard", "rótulo"], reply: "Tejidas: satén, tafetán, jacquard, doble orillo — detalles finos, resistentes al lavado. Satén/jacquard para el principal, tafetán para talla. ¿Principal o talla?" },
      { id: "carelabel", kws: ["cuidado", "lavado", "composición"], reply: "Etiquetas de cuidado: tejidas, recubiertas o impresas — conformes a normas internacionales. Combo común: principal tejida + cuidado impresa." },
      { id: "bags", kws: ["bolsa", "polietileno", "cremallera", "embalaje"], reply: "Bolsas: PE/CPE, con cremallera, autosellantes, antiestáticas — imprimibles, tamaños a medida. Las OPP transparentes son muy económicas para exportar 👍" },
      { id: "paperbag", kws: ["bolsa de papel", "kraft", "ecológica"], reply: "Bolsas de papel kraft o estucado — biodegradables, imprimibles, asas personalizadas. A los clientes europeos les encantan 🌱" },
      { id: "brochure", kws: ["folleto", "catálogo", "tríptico"], reply: "Folletos, catálogos, trípticos — control de calidad total del papel al encuadernado. Envía tu identidad visual, asesoría gratuita." },
      { id: "moq", kws: ["mínimo", "moq", "cantidad", "pedido"], reply: function (st) {
        if (st.topic === "hangtag") return "Etiquetas colgantes: 2.000–3.000 unidades para prueba; el precio baja mucho a partir de 10.000. ¿Cuántas necesitas?";
        if (st.topic === "woven") return "Tejidas: normalmente 1.000+ unidades; jacquard/doble orillo varía un poco. ¿Cantidad exacta?";
        if (st.topic === "carelabel") return "De cuidado desde 300–500 unidades — muy económico 👍 ¿Qué tipo (tejida/recubierta/impresa)?";
        if (st.topic === "bags" || st.topic === "paperbag") return "Mínimo flexible según tamaño e impresión — incluso unos cientos de bolsas de muestra. ¿Qué tamaño?";
        return "Mínimos: etiquetas 2.000–3.000 prueba; tejidas 1.000+; cuidado 300–500; bolsas flexibles. ¿Qué producto?";
      } },
      { id: "sample", kws: ["muestra", "muestreo", "prototipo"], reply: "¡Sí! Muestras físicas en 3–7 días, con asesoría gratuita. Recomendamos confirmar la calidad antes de producir 😊 ¿Nos envías un diseño?" },
      { id: "quote", kws: ["presupuesto", "precio", "coste", "cuánto"], reply: function (st) {
        if (st.topic === "hangtag") return "Para etiquetas, el precio depende del material, tamaño, colores y acabado — el papel estucado estándar es muy accesible desde 1.000 unidades. ¿Qué cantidad? Envía el diseño a sales@taigetag.com para un presupuesto exacto 😊";
        if (st.topic === "woven") return "El presupuesto de tejidas depende del tejido y tamaño, normalmente 1.000+ unidades. ¡Envía tu diseño, presupuesto en 24 h!";
        if (st.topic === "carelabel") return "Precio según material (tejida/recubierta/impresa) y cantidad — desde 300–500 unidades. ¿Qué tipo?";
        if (st.topic === "bags" || st.topic === "paperbag") return "El presupuesto depende de tamaño, grosor, impresión y cantidad. Envía dimensiones + cantidad + logo, presupuesto en 24 h 👍";
        return "Para presupuestar bien: ① tipo de producto ② cantidad ③ diseño/tamaño. Dime primero el producto y envía el resto a sales@taigetag.com 😊";
      } },
      { id: "leadtime", kws: ["plazo", "entrega", "tiempo"], reply: "Muestreo: 3–7 días. Producción: normalmente 10–25 días según cantidad y acabado. Confirmación escrita antes de pedir 😊" },
      { id: "payment", kws: ["pago", "depósito", "tt", "l/c"], reply: "Condiciones: 30% de depósito, 70% antes del envío. Transferencia bancaria; L/C negociable para pedidos grandes." },
      { id: "shipping", kws: ["envío", "flete", "fob", "exw", "dhl"], reply: "FOB Shenzhen/Guangzhou, EXW fábrica, o gestionamos marítimo/aéreo/exprés (DHL, FedEx, UPS). El exprés es ideal para muestras pequeñas 📦" },
      { id: "oem", kws: ["oem", "odm", "personalizado", "logo", "diseño"], reply: "¡OEM/ODM y producción según muestra! Nuestro equipo de diseño optimiza tus artes — colores, materiales, acabados flexibles, del muestreo a la serie. ¿Tienes diseño o necesitas ayuda?" },
      { id: "quality", kws: ["calidad", "qc", "certificación"], reply: "Control de calidad completo: inspección de materias primas → controles en proceso → inspección final → revisión antes del envío. Licencia y certificados disponibles 📋" },
      { id: "company", kws: ["empresa", "fábrica", "tage", "dónde"], reply: "Dongguan Tage Packaging Products Co., Ltd. — Humen, Dongguan, Guangdong. 20 años en accesorios de vestir: etiquetas, tejidas, bolsas — producción integrada, exportación a 40+ países 🇨🇳🌍" },
      { id: "contact", kws: ["contacto", "teléfono", "email", "wechat", "whatsapp"], reply: "¡Contáctanos! 📧 sales@taigetag.com ｜ 📱 Tel./WhatsApp/WeChat: +86 131 2811 8931 ｜ 📍 Humen, Dongguan, Guangdong. Respuesta en 24 h 😊" },
      { id: "order", kws: ["pedido", "proceso", "comprar"], reply: "Proceso simple: ① envía tus necesidades → ② presupuesto en 24 h → ③ muestreo → ④ producción tras aprobación → ⑤ control y envío. ¡Empieza en cualquier paso!" },
      { id: "faq", kws: ["faq", "ayuda", "pregunta"], reply: "Respuestas rápidas: 📦 Mínimos: etiquetas 2.000+, tejidas 1.000+, cuidado 300+ ｜ 🧪 Muestras: 3–7 días ｜ 💰 Presupuesto: 24 h ｜ 🚚 Plazo: 10–25 días. ¿Más preguntas?" }
    ]
  };

  var t = T[LANG];

  /* ---------- 对话状态（多轮上下文） ---------- */
  var state = { topic: null, quoted: false };

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

  /* ---------- 意图匹配引擎（返回最优+次优，支持多词 AND） ---------- */
  function matchIntent(q) {
    var ql = q.toLowerCase();
    var best = null, bestLen = 0, second = null, secondLen = 0;
    var intents = t.intents;
    for (var i = 0; i < intents.length; i++) {
      var it = intents[i];
      var hitLen = 0;
      for (var j = 0; j < it.kws.length; j++) {
        var kw = it.kws[j];
        if (kw.charAt(0) === "!" && ql === kw.slice(1)) { hitLen = 999; break; }
        if (kw.indexOf("|") > 0) {
          var parts = kw.split("|");
          var sub = 0;
          for (var k = 0; k < parts.length; k++) {
            if (ql.indexOf(parts[k]) >= 0) sub += parts[k].length;
          }
          if (sub > 0 && sub >= hitLen) hitLen = sub;
        } else if (ql.indexOf(kw) >= 0) {
          hitLen = Math.max(hitLen, kw.length);
        }
      }
      if (hitLen > bestLen) { second = best; secondLen = bestLen; best = it; bestLen = hitLen; }
      else if (hitLen > secondLen && hitLen > 0) { second = it; secondLen = hitLen; }
    }
    return { best: best, second: second };
  }

  function resolveReply(intent) {
    var r = intent.reply;
    if (typeof r === "function") return r(state, t);
    return r;
  }

  /* ---------- 处理用户输入 ---------- */
  function ask(q) {
    if (!q.trim()) return;
    appendMsg(q, "user");
    INPUT.value = "";
    setTimeout(function () {
      var res = matchIntent(q);
      if (res.best) {
        var it = res.best;
        var CONSULT = ["quote", "moq", "sample", "leadtime"];
        var PRODUCTS = ["hangtag", "woven", "carelabel", "bags", "paperbag", "brochure"];
        /* 双向上下文提升：产品词+咨询词同时命中 → 回复用咨询意图，产品记为主题 */
        if (res.second && CONSULT.indexOf(res.second.id) >= 0 && PRODUCTS.indexOf(it.id) >= 0) {
          state.topic = it.id;
          it = res.second;
        } else if (res.second && CONSULT.indexOf(it.id) >= 0 && PRODUCTS.indexOf(res.second.id) >= 0) {
          state.topic = res.second.id;
        } else {
          state.topic = it.id;
        }
        appendMsg(resolveReply(it), "ai");
        /* 追问：报价流程且还没引导过 */
        if (it.id === "quote" && !state.quoted) {
          setTimeout(function () { appendMsg(t.followupQuote, "ai"); }, 500);
          state.quoted = true;
        }
      } else {
        appendMsg(t.fallback, "ai");
      }
    }, 450);
  }

  /* 触屏设备不自动聚焦（避免 iOS 键盘顶起面板） */
  function focusInput() {
    try {
      if (window.matchMedia && window.matchMedia("(hover: hover)").matches) {
        INPUT.focus();
      }
    } catch (e) {}
  }

  /* ---------- 事件 ---------- */
  FAB.addEventListener("click", function () {
    var open = PANEL.classList.toggle("open");
    FAB.classList.toggle("hidden", open);
    if (open) { BODY.scrollTop = BODY.scrollHeight; focusInput(); }
  });
  var OPEN = document.getElementById("assistOpen");
  if (OPEN) {
    OPEN.addEventListener("click", function (e) {
      e.stopPropagation();
      PANEL.classList.add("open");
      FAB.classList.add("hidden");
      BODY.scrollTop = BODY.scrollHeight;
      focusInput();
    });
  }
  var CLOSE = document.getElementById("assistClose");
  if (CLOSE) {
    CLOSE.addEventListener("click", function () {
      PANEL.classList.remove("open");
      FAB.classList.remove("hidden");
    });
  }
  SEND.addEventListener("click", function () { ask(INPUT.value); });
  INPUT.addEventListener("keydown", function (e) {
    if (e.key === "Enter") { e.preventDefault(); ask(INPUT.value); }
  });
  document.addEventListener("click", function (e) {
    if (!PANEL.classList.contains("open")) return;
    if (!PANEL.contains(e.target) && e.target !== FAB && !FAB.contains(e.target)) {
      PANEL.classList.remove("open");
      FAB.classList.remove("hidden");
    }
  });

  appendMsg(t.hello, "ai");
  renderQuick();

  window.TAGEAssist = {
    open: function () {
      PANEL.classList.add("open");
      FAB.classList.add("hidden");
      BODY.scrollTop = BODY.scrollHeight;
      focusInput();
    }
  };

})();
