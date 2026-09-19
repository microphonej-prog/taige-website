/* TAGE Assist — 懸浮客服窗口 v2（智能多輪對話引擎）
   實現：意圖識別 + 對話上下文 + 追問引導，四語。
   說明：靜態站前端無法直連 LLM（密鑰泄露風險），此引擎用規則+上下文模擬智能客服。
   掛載：各頁面 #assistFab / #assistPanel；語言與 main.js 一致。 */
(function () {
  "use strict";
  var FAB = document.getElementById("assistFab");
  var PANEL = document.getElementById("assistPanel");
  var BODY = document.getElementById("assistBody");
  var QUICK = document.getElementById("assistQuick");
  var INPUT = document.getElementById("assistInput");
  var SEND = document.getElementById("assistSend");
  if (!FAB || !PANEL || !BODY || !QUICK || !INPUT || !SEND) return;

  /* ---------- 語言檢測：?lang > localStorage > html lang ---------- */
  var LANGS = ["zh", "en", "ja", "ko", "fr", "es"];
  /* 獨立語言目錄 /en/ /ja/ /ko/ /fr/ /es/：固定對應語言（該目錄頁面已靜態渲染） */
  var DIR_LANG = null;
  try {
    var _p = location.pathname;
    if (_p.indexOf("/en/") >= 0) DIR_LANG = "en";
    else if (_p.indexOf("/ja/") >= 0) DIR_LANG = "ja";
    else if (_p.indexOf("/ko/") >= 0) DIR_LANG = "ko";
    else if (_p.indexOf("/fr/") >= 0) DIR_LANG = "fr";
    else if (_p.indexOf("/es/") >= 0) DIR_LANG = "es";
  } catch (e) {}
  var LANG = "zh", fromUrl = null, fromStore = null;
  if (DIR_LANG) {
    LANG = DIR_LANG;
  } else {
    /* 根目錄固定中文（與 main.js 一致：獨立目錄已上線，根目錄不再切換語言，
       避免 Googlebot 渲染與 localStorage 殘留偏好造成語言不一致） */
    LANG = "zh";
  }
  /* ================= 四語知識庫 ================= */
  function T() {}
  T.zh = {
    online: "在線", hello: "您好！我是泰閣智能客服 🐓 關於吊牌、織嘜、洗水標、包裝袋的任何問題都可以問我，也可以直接告訴我您的需求～",
    ph: "輸入您的問題…", send: "發送",
    quick: ["你們有哪些產品？", "最小起訂量是多少？", "可以打樣嗎？", "怎麼報價？"],
    followupQuote: "💡 提示：把設計稿或數量發到 sales@taigetag.com，24 小時內給您精確報價；加微信 13128118931 溝通更快～",
    fallback: "這個問題我需要確認一下 🤔 建議把具體需求發到 sales@taigetag.com 或加微信 13128118931，我們專業同事 24 小時內給您準確答覆。也可以點頁面底部「聯繫方式」直接留言。",
    intents: [
      { id: "hello", kws: ["你好", "您好", "嗨", "哈嘍", "hello", "hi", "在嗎", "在不在", "哈喽", "在吗"], reply: "您好！有什麼可以幫您？😊 可以問產品、起訂量、打樣、報價，也可以直接說您的需求。" },
      { id: "thanks", kws: ["謝謝", "感謝", "thank", "merci", "gracias", "3q", "thx", "谢谢", "感谢"], reply: "不客氣！隨時找我 😄 有樣品或報價需求，隨時發我。" },
      { id: "bye", kws: ["再見", "拜拜", "bye", "88", "goodbye", "再见"], reply: "再見！祝您生意興隆 🚀 需要時隨時來問～" },
      { id: "product", kws: ["產品", "什麼", "有哪些", "做什麼", "品類", "product", "produce", "offre", "productos", "产品", "什么", "做什么", "品类"], reply: "我們有六大產品線：\n① 服裝吊牌（銅版紙/牛皮紙/PVC，燙金 UV 啞膜）\n② 織嘜/主嘜（緞面/提花/雙層織邊）\n③ 洗水標（織帶/塗層/印刷）\n④ 包裝袋（PE 膠袋/自封袋/防靜電袋）\n⑤ 環保紙袋（牛皮紙/白卡紙）\n⑥ 宣傳手冊（畫冊/摺頁）\n全部支持定製和 OEM。您對哪一類感興趣？" },
      { id: "hangtag", kws: ["吊牌", "掛卡", "hangtag", "hang tag", "étiquette suspendue", "etiqueta colgante", "標籤卡", "挂卡", "标签卡"], reply: "吊牌是我們主打產品 👍 材質有銅版紙（300-400克）、牛皮紙、棉紙、PVC 防水等；工藝支持燙金、壓凹凸、UV 局部上光、覆膜；尺寸常規 35×70 / 40×90 / 50×90mm，也能異形模切。需要我幫您看看材質怎麼選嗎？" },
      { id: "woven", kws: ["織嘜", "主嘜", "緞面", "提花", "woven", "tissé", "tejida", "商標", "织唛", "主唛", "缎面", "商标"], reply: "織嘜/主嘜有緞面、平紋、提花、雙層織邊等織法，圖案細膩、耐水洗不褪色。建議：主嘜用緞面/提花顯高檔，尺碼嘜用塔夫綢。您需要主嘜還是尺碼嘜？" },
      { id: "carelabel", kws: ["洗水標", "洗標", "水洗標", "care label", "entretien", "de cuidado", "洗水标", "洗标", "水洗标"], reply: "洗水標有三種：織帶洗標、塗層洗標、印刷洗標，符合各國洗滌標準，信息清晰持久。常見組合是「織嘜主嘜 + 印刷洗水標」，兼顧檔次和成本。需要按您的洗滌要求推薦嗎？" },
      { id: "bags", kws: ["包裝袋", "膠袋", "自封袋", "拉鍊袋", "poly bag", "ziplock", "sac", "bolsa", "包装袋", "胶袋", "拉链袋"], reply: "包裝袋有 PE/CPE 膠袋、拉鍊袋、自封袋、防靜電袋，可印刷品牌 LOGO，尺寸厚度按需定製。服裝出口常用的 OPP 透明袋性價比很高 👍" },
      { id: "paperbag", kws: ["紙袋", "牛皮紙袋", "環保袋", "paper bag", "kraft", "sac papier", "bolsa de papel", "纸袋", "牛皮纸袋", "环保袋"], reply: "環保紙袋用牛皮紙或白卡紙，可降解環保，支持品牌印刷和定製提手——歐盟客戶很看重這個 🌱 需要看環保選項嗎？" },
      { id: "brochure", kws: ["畫冊", "手冊", "摺頁", "目錄", "brochure", "catalogue", "folleto", "画册", "手册", "折页", "目录"], reply: "宣傳手冊/畫冊/產品目錄都可以做，從紙張選型到裝訂全程把控品質。把您的品牌 VI 發我們，設計部免費出排版建議。" },
      { id: "moq", kws: ["起訂", "moq", "最小", "多少起", "數量", "minimum", "quantité", "mínimo", "起订", "数量"], reply: function (st) {
        if (st.topic === "hangtag") return "吊牌起訂量：2,000–3,000 張可試單，10,000+ 張單價更划算。您計劃要多少？";
        if (st.topic === "woven") return "織嘜一般 1,000 張以上起做，提花/雙層織邊工藝價格略有不同。需要精確數量嗎？";
        if (st.topic === "carelabel") return "洗水標 300–500 張就能起做，成本很友好 👍 您需要哪種（織帶/塗層/印刷）？";
        if (st.topic === "bags" || st.topic === "paperbag") return "包裝袋起訂量比較靈活，按尺寸和印刷談，幾百個樣品袋也可以做。您要多大的？";
        return "起訂量因產品不同：吊牌 2,000–3,000 張試單；織嘜 1,000 張以上；洗水標 300–500 張起；包裝袋靈活。您做哪類產品？";
      } },
      { id: "sample", kws: ["打樣", "樣品", "樣板", "樣版", "sample", "échantillon", "muestra", "打版", "打样", "样品", "样板", "样版"], reply: "可以打樣！一般 3–7 天內寄出實物樣品，並提供免費打樣建議。批量下單前先確認印刷質量和材質手感，是我們給所有客戶的建議 😊 您方便發個設計稿或參考圖嗎？" },
      { id: "quote", kws: ["報價", "價格", "多少錢", "費用", "成本", "怎麼算", "詢價", "quote", "price", "cost", "devis", "prix", "presupuesto", "precio", "报价", "价格", "多少钱", "费用", "怎么算", "询价"], reply: function (st, tt) {
        if (st.topic === "hangtag") return "吊牌的話，價格主要看材質、尺寸、印色數和工藝：銅版紙常規款千張級單價很友好，燙金/異形模切會高一些。您大概要多少數量？把設計發到 sales@taigetag.com 我們能報精確價 😊";
        if (st.topic === "woven") return "織嘜報價要看織法（緞面/提花/雙層）和尺寸，一般 1,000 張以上起做。發設計稿給我們，24 小時內出精確報價～";
        if (st.topic === "carelabel") return "洗水標價格按材質（織帶/塗層/印刷）和數量算，300–500 張就能做，價格很友好。需要報哪種？";
        if (st.topic === "bags" || st.topic === "paperbag") return "包裝袋報價要看尺寸、厚度、印刷和數量。發需求給我們（尺寸+數量+要不要印 LOGO），24 小時內出報價 👍";
        return "好的！爲了報得準，需要知道：① 產品類型 ② 數量 ③ 設計/尺寸。您先告訴我哪種產品，其餘的發到 sales@taigetag.com 就行 😊";
      } },
      { id: "leadtime", kws: ["交期", "貨期", "多久", "多長時間", "什麼時候", "lead", "delivery", "délai", "plazo", "幾天", "货期", "多长时间", "什么时候", "几天"], reply: "打樣一般 3–7 天；大貨交期看數量和工藝，通常 10–25 天。下單前會給您書面確認的交期，不用擔心 😊" },
      { id: "payment", kws: ["付款", "怎麼付", "定金", "tt", "信用證", "l/c", "payment", "paiement", "pago", "怎么付", "信用证"], reply: "常規合作：30% 定金 + 70% 尾款發貨前付清；支持 T/T 銀行轉賬，大單也可談信用證。新客戶首次合作我們會給詳細的付款條款。" },
      { id: "shipping", kws: ["運費", "物流", "快遞", "海運", "空運", "fob", "exw", "shipping", "freight", "expédition", "envío", "运费", "快递", "海运", "空运"], reply: "支持多種出貨方式：FOB 深圳/廣州、EXW 工廠，或我們幫您安排海運/空運/快遞（DHL、FedEx、UPS 等）。小批量樣品走快遞最划算 📦" },
      { id: "oem", kws: ["定製", "oem", "odm", "來樣", "設計", "logo", "custom", "personnalisé", "personalizado", "定制", "来样", "设计"], reply: "支持 OEM/ODM 和來樣定製！設計部可幫您優化稿件，顏色、材質、工藝靈活組合，從打樣到量產一條龍。您有自己的設計稿還是需要我們設計？" },
      { id: "quality", kws: ["質量", "質檢", "品控", "合格", "quality", "qc", "qualité", "calidad", "認證", "质量", "质检", "认证"], reply: "我們執行完整品控流程：原材料檢驗 → 印刷過程抽檢 → 成品全檢 → 出貨前複檢。公司持有營業執照及各類資質，可提供檢測報告 📋" },
      { id: "company", kws: ["公司", "工廠", "介紹", "泰閣", "tage", "哪裏", "地址", "company", "factory", "entreprise", "empresa", "工厂", "介绍", "泰阁", "哪里"], reply: "東莞泰閣包裝製品有限公司（Dongguan Tage Packaging Products Co., Ltd.）位於廣東東莞虎門，專注服裝輔料 20 年：吊牌、織嘜、洗水標、包裝袋一站式生產，出口全球 40+ 國家 🇨🇳🌍" },
      { id: "contact", kws: ["聯繫", "電話", "微信", "郵箱", "email", "whatsapp", "contact", "téléphone", "wechat", "contacto", "联系", "电话", "邮箱"], reply: "隨時聯繫！📧 sales@taigetag.com ｜📱 電話/WhatsApp/微信：+86 131 2811 8931 ｜📍 廣東省東莞市虎門鎮。發需求一般 24 小時內回覆（工作時間更快）😊" },
      { id: "order", kws: ["下單", "訂購", "買", "怎麼合作", "流程", "order", "commande", "pedido", "下单", "订购", "买", "怎么合作"], reply: "合作流程很簡單：① 發需求/設計稿 → ② 我們 24 小時內報價 → ③ 確認打樣 → ④ 樣品確認後量產 → ⑤ 驗貨出貨。您可以從任意一步開始！" },
      { id: "faq", kws: ["常見問題", "faq", "問題", "help", "aide", "常见问题", "问题"], reply: "常見問題速答：\n📦 起訂量：吊牌 2,000+、織嘜 1,000+、洗水標 300+ \n🧪 打樣：3–7 天寄樣\n💰 報價：24 小時內\n🚚 交期：10–25 天\n更多細節直接問我～" }
    ]
  };
  T.en = {
    online: "Online", hello: "Hi! I'm TAGE's smart assistant 🐓 Ask me anything about hang tags, woven labels, care labels or packaging bags — or just tell me your needs.",
    ph: "Type your message…", send: "Send",
    quick: ["What products do you make?", "What is the MOQ?", "Can I get samples?", "How do I get a quote?"],
    followupQuote: "💡 Tip: email your artwork or quantities to sales@taigetag.com for an exact quote within 24h. WeChat: 13128118931 is even faster.",
    fallback: "Let me check on that 🤔 Please email your specific requirements to sales@taigetag.com or add us on WeChat 13128118931 — our team replies within 24 hours. You can also use the Contact form at the bottom of the page.",
    intents: [
      { id: "hello", kws: ["hello", "hi", "hey", "你好", "在嗎"], reply: "Hello! How can I help? 😊 Ask about products, MOQ, sampling or quotes — or just describe your needs." },
      { id: "thanks", kws: ["thanks", "thank", "thx", "merci", "gracias"], reply: "You're welcome! 😄 Feel free to reach out anytime for samples or quotes." },
      { id: "bye", kws: ["bye", "goodbye", "see you"], reply: "Goodbye! Wishing you great business 🚀 Come back anytime." },
      { id: "product", kws: ["product", "what do you make", "range", "offer", "品類", "產品"], reply: "We produce six lines:\n① Hang tags (art/kraft/PVC paper, foil/UV/matte)\n② Woven labels (satin/jacquard/double-layer)\n③ Care labels (woven/coated/printed)\n④ Packaging bags (PE/ziplock/anti-static)\n⑤ Eco paper bags (kraft/art card)\n⑥ Brochures & catalogs\nAll custom & OEM. Which one interests you?" },
      { id: "hangtag", kws: ["hangtag", "hang tag", "tag", "吊牌"], reply: "Hang tags are our specialty 👍 Materials: art paper (300-400gsm), kraft, cotton, waterproof PVC. Finishes: hot foil, embossing, spot UV, lamination. Sizes 35×70 / 40×90 / 50×90mm or custom die-cut. Need material advice?" },
      { id: "woven", kws: ["woven", "satin", "jacquard", "主嘜", "織嘜"], reply: "Woven labels: satin, plain, jacquard, double-layer edge — fine detail, wash-resistant. Satin/jacquard for main labels, taffeta for size labels. Main label or size label?" },
      { id: "carelabel", kws: ["care label", "washing", "洗水標"], reply: "Care labels: woven tape, coated or printed — meeting international care standards, clear and durable. A common combo: woven main label + printed care label. Need a recommendation?" },
      { id: "bags", kws: ["bag", "poly", "ziplock", "包裝袋"], reply: "Bags: PE/CPE poly, zipper, self-seal, anti-static — printable with your logo, custom size & thickness. Clear OPP bags are great value for apparel export 👍" },
      { id: "paperbag", kws: ["paper bag", "kraft", "eco bag", "紙袋"], reply: "Eco paper bags in kraft or art card — biodegradable, printable, custom handles. EU buyers love these 🌱" },
      { id: "brochure", kws: ["brochure", "catalog", "flyer", "畫冊"], reply: "Brochures, catalogs and flyers — full quality control from paper to binding. Send your brand VI and our design team will advise for free." },
      { id: "moq", kws: ["moq", "minimum", "quantity", "起訂"], reply: function (st) {
        if (st.topic === "hangtag") return "Hang tag MOQ: 2,000–3,000 pcs trial; unit price drops significantly at 10,000+. How many do you need?";
        if (st.topic === "woven") return "Woven labels usually start at 1,000+ pcs; jacquard/double-layer vary slightly. Need an exact quantity?";
        if (st.topic === "carelabel") return "Care labels from 300–500 pcs — very budget-friendly 👍 Which type (woven/coated/printed)?";
        if (st.topic === "bags" || st.topic === "paperbag") return "Bag MOQ is flexible by size and printing — even a few hundred sample bags. What size?";
        return "MOQ varies: hang tags 2,000–3,000 trial; woven 1,000+; care labels 300–500; bags flexible. Which product?";
      } },
      { id: "sample", kws: ["sample", "prototype", "打樣"], reply: "Yes, we sample! Physical samples within 3–7 days, with free sampling advice. We always recommend confirming print quality before bulk orders 😊 Can you share an artwork or reference?" },
      { id: "quote", kws: ["quote", "price", "cost", "how much", "報價"], reply: function (st) {
        if (st.topic === "hangtag") return "For hang tags, price depends on material, size, colors and finish — standard art paper is very friendly at thousand-pc levels; foil or die-cut costs a bit more. What quantity do you need? Email artwork to sales@taigetag.com for an exact quote 😊";
        if (st.topic === "woven") return "Woven label quotes depend on weave (satin/jacquard/double) and size, usually 1,000+ pcs. Send your artwork and we'll quote within 24h!";
        if (st.topic === "carelabel") return "Care labels are priced by material (woven/coated/printed) and quantity — from 300–500 pcs, very budget-friendly. Which type?";
        if (st.topic === "bags" || st.topic === "paperbag") return "Bag quotes depend on size, thickness, printing and quantity. Send us size + qty + logo requirement, quote within 24h 👍";
        return "To quote accurately we need: ① product type ② quantity ③ artwork/size. Tell me the product first, then email the rest to sales@taigetag.com 😊";
      } },
      { id: "leadtime", kws: ["lead time", "delivery", "how long", "交期"], reply: "Sampling: 3–7 days. Bulk delivery: usually 10–25 days depending on quantity and finish. Written confirmation before you order 😊" },
      { id: "payment", kws: ["payment", "deposit", "tt", "l/c", "付款"], reply: "Standard terms: 30% deposit, 70% balance before shipment. Bank T/T accepted; L/C negotiable for large orders. Full payment terms for first orders." },
      { id: "shipping", kws: ["shipping", "freight", "fob", "exw", "dhl", "物流"], reply: "FOB Shenzhen/Guangzhou, EXW factory, or we arrange sea/air/express (DHL, FedEx, UPS). Express is most economical for small sample parcels 📦" },
      { id: "oem", kws: ["oem", "odm", "custom", "logo", "design", "定製"], reply: "OEM/ODM and sample-based customization supported! Our design team helps optimize artwork — colors, materials, finishes all flexible, from sampling to mass production. Do you have artwork or need design help?" },
      { id: "quality", kws: ["quality", "qc", "certification", "質量"], reply: "Full QC process: raw material inspection → in-process checks → final inspection → pre-shipment review. Business license and certificates available; test reports on request 📋" },
      { id: "company", kws: ["company", "factory", "where", "about", "tage"], reply: "Dongguan Tage Packaging Products Co., Ltd. — Humen, Dongguan, Guangdong. 20 years in garment trims: hang tags, woven labels, care labels, bags — one-stop, exporting to 40+ countries 🇨🇳🌍" },
      { id: "contact", kws: ["contact", "phone", "email", "wechat", "whatsapp"], reply: "Contact us anytime! 📧 sales@taigetag.com ｜ 📱 Phone/WhatsApp/WeChat: +86 131 2811 8931 ｜ 📍 Humen, Dongguan, Guangdong. Replies within 24h (faster during work hours) 😊" },
      { id: "order", kws: ["order", "process", "how to buy", "下單"], reply: "Simple process: ① send requirements/artwork → ② quote within 24h → ③ sampling → ④ mass production after approval → ⑤ QC & shipping. Start from any step!" },
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

  /* ---------- 日語（/ja/ 目錄） ---------- */
  T.ja = {
    online: "オンライン", hello: "こんにちは！泰閣（TAGE）のスマートアシスタントです 🐓 タグ、織りラベル、洗濯表示ラベル、包裝袋について何でもお尋ねください。ご要望をそのままお知らせいただいても構いません。",
    ph: "ご質問を入力してください…", send: "送信",
    quick: ["どのような製品がありますか？", "最小ロットはいくつですか？", "サンプル作成はできますか？", "お見積りはどうすればいいですか？"],
    followupQuote: "💡 ヒント：デザインデータまたは數量を sales@taigetag.com までお送りいただければ、24時間以內に正確なお見積りをご提示いたします。WeChat 13128118931 でのご連絡がより速いです。",
    fallback: "この件は確認が必要です 🤔 具體的なご要望を sales@taigetag.com までお送りいただくか、WeChat 13128118931 までご連絡ください。擔當者より 24時間以內に正確にご回答いたします。ページ下部の「お問い合わせ」からも直接ご連絡いただけます。",
    intents: [
      { id: "hello", kws: ["你好", "您好", "嗨", "哈嘍", "hello", "hi", "hey", "在嗎", "在不在", "こんにちは", "こんばんは", "おはようございます", "はじめまして", "もしもし"], reply: "こんにちは！どのようなご用件でしょうか？😊 製品、最小ロット、サンプル作成、お見積りなど、何でもお尋ねください。ご要望をそのままお知らせいただいても構いません。" },
      { id: "thanks", kws: ["謝謝", "感謝", "thank", "thanks", "thx", "3q", "merci", "gracias", "ありがとう", "ありがとうございます", "どうも", "感謝"], reply: "どういたしまして！😄 サンプルやお見積りのご依頼は、いつでもお気軽にご連絡ください。" },
      { id: "bye", kws: ["再見", "拜拜", "bye", "88", "goodbye", "see you", "さようなら", "失禮します", "またね"], reply: "失禮いたします。ご商売のご発展をお祈り申し上げます 🚀 いつでもお気軽にお問い合わせください。" },
      { id: "product", kws: ["產品", "什麼", "有哪些", "做什麼", "品類", "product", "produce", "offre", "productos", "range", "offer", "what do you make", "製品", "商品", "取り扱い", "ラインナップ", "どんな製品"], reply: "當社は 6 つの製品ラインを展開しております。\n① 衣料用タグ（コート紙／クラフト紙／PVC、箔押し・UV・マット加工）\n② 織りラベル／メインラベル（サテン／ジャカード／二重織端）\n③ 洗濯表示ラベル（織りテープ／コーティング／印刷）\n④ 包裝袋（PE 袋／チャック袋／帯電防止袋）\n⑤ エコ紙袋（クラフト紙／白カード紙）\n⑥ パンフレット（カタログ／リーフレット）\nすべてカスタマイズ・OEM に対応しております。どれにご興味がおありですか？" },
      { id: "hangtag", kws: ["吊牌", "掛卡", "hangtag", "hang tag", "tag", "étiquette suspendue", "etiqueta colgante", "標籤卡", "タグ", "ハングタグ", "値札"], reply: "タグは當社の主力製品です 👍 素材はコート紙（300-400 g）、クラフト紙、コットン紙、防水 PVC などがございます。加工は箔押し、エンボス、部分 UV、ラミネートに対応しております。サイズは通常 35×70 / 40×90 / 50×90mm で、異形型抜きも承ります。素材選びをお手伝いいたしましょうか？" },
      { id: "woven", kws: ["織嘜", "主嘜", "緞面", "提花", "woven", "satin", "jacquard", "tissé", "tejida", "商標", "織りラベル", "織ネーム", "メインラベル", "サテン", "ジャカード", "織り"], reply: "織りラベル／メインラベルは、サテン、平織り、ジャカード、二重織端などの織り方がございます。柄が繊細で洗濯にも色落ちしません。メインラベルにはサテンやジャカード、サイズラベルにはタフタがおすすめです。メインラベルとサイズラベル、どちらが必要でしょうか？" },
      { id: "carelabel", kws: ["洗水標", "洗標", "水洗標", "care label", "washing", "entretien", "de cuidado", "洗濯表示", "洗濯ラベル", "洗濯ネーム", "ケアラベル"], reply: "洗濯表示ラベルは 3 種類ございます。織りテープ、コーティング、印刷タイプで、各國の洗濯表示規格に適合し、情報が明確で長持ちします。一般的な組み合わせは「織りラベル＋印刷洗濯表示ラベル」で、品質とコストのバランスに優れております。お客様の洗濯條件に合わせてご提案いたしましょうか？" },
      { id: "bags", kws: ["包裝袋", "膠袋", "自封袋", "拉鍊袋", "poly bag", "ziplock", "bag", "poly", "sac", "bolsa", "ポリ袋", "ビニール袋", "チャック袋", "梱包袋", "袋"], reply: "包裝袋は PE／CPE 袋、チャック袋、粘着テープ袋、帯電防止袋を取り扱っております。ブランドロゴの印刷が可能で、サイズと厚みはご要望に合わせて製造いたします。衣料品の輸出では透明 OPP 袋のコストパフォーマンスが非常に良好です 👍" },
      { id: "paperbag", kws: ["紙袋", "牛皮紙袋", "環保袋", "paper bag", "kraft", "eco bag", "sac papier", "bolsa de papel", "エコ紙袋", "クラフト紙袋", "ペーパーバッグ", "紙袋"], reply: "エコ紙袋はクラフト紙または白カード紙を使用し、生分解性で環境に優しく、ブランド印刷や取っ手のカスタマイズにも対応しております。歐州のお客様はこの點を特に重視されております 🌱 環境対応の選択肢をご覧になりますか？" },
      { id: "brochure", kws: ["畫冊", "手冊", "摺頁", "目錄", "brochure", "catalog", "catalogue", "flyer", "folleto", "パンフレット", "カタログ", "リーフレット", "冊子"], reply: "パンフレット、カタログ、リーフレットはいずれも承っております。用紙の選定から製本まで一貫して品質を管理いたします。ブランドの VI データをお送りいただければ、デザイン部が無料でレイアウトをご提案いたします。" },
      { id: "moq", kws: ["起訂", "moq", "最小", "多少起", "數量", "quantity", "minimum", "quantité", "mínimo", "最小ロット", "ロット", "最小注文", "最低數量", "何枚から", "いくつから"], reply: function (st) {
        if (st.topic === "hangtag") return "タグの最小ロットは 2,000–3,000 枚から試験発注が可能で、10,000 枚以上になりますと単価がよりお得です。數量はどのくらいをお考えですか？";
        if (st.topic === "woven") return "織りラベルは通常 1,000 枚以上から承っております。ジャカードや二重織端は価格が多少異なります。正確な數量を教えていただけますか？";
        if (st.topic === "carelabel") return "洗濯表示ラベルは 300–500 枚から承っており、コスト面でも大変お得です 👍 どのタイプ（織りテープ／コーティング／印刷）をご希望ですか？";
        if (st.topic === "bags" || st.topic === "paperbag") return "包裝袋の最小ロットは柔軟です。サイズと印刷內容によって異なり、數百枚のサンプル袋からも承ります。ご希望のサイズはどのくらいですか？";
        return "最小ロットは製品によって異なります。タグは 2,000–3,000 枚の試験発注、織りラベルは 1,000 枚以上、洗濯表示ラベルは 300–500 枚から、包裝袋は柔軟に対応しております。どの製品をお考えですか？";
      } },
      { id: "sample", kws: ["打樣", "樣品", "樣板", "樣版", "sample", "prototype", "échantillon", "muestra", "打版", "サンプル", "サンプル作成", "見本", "試作"], reply: "サンプル作成は可能です！通常 3–7 日以內に現物サンプルをお送りし、無料でサンプル作成のご提案もいたします。量産前に印刷品質と素材の質感をご確認いただくことを、すべてのお客様におすすめしております 😊 デザインデータまたは參考畫像をお送りいただけますか？" },
      { id: "quote", kws: ["報價", "價格", "多少錢", "費用", "成本", "怎麼算", "詢價", "quote", "price", "cost", "how much", "devis", "prix", "presupuesto", "precio", "お見積り", "見積", "価格", "値段", "いくら", "単価"], reply: function (st) {
        if (st.topic === "hangtag") return "タグの場合、価格は主に素材、サイズ、印刷色數、加工によって決まります。コート紙の標準タイプは千枚単位で大変お求めやすい価格で、箔押しや異形型抜きは少し高くなります。おおよその數量を教えていただけますか？デザインを sales@taigetag.com までお送りいただければ正確なお見積りが可能です 😊";
        if (st.topic === "woven") return "織りラベルのお見積りは織り方（サテン／ジャカード／二重）とサイズによって異なり、通常 1,000 枚以上から承っております。デザインデータをお送りいただければ、24時間以內に正確なお見積りをご提示いたします。";
        if (st.topic === "carelabel") return "洗濯表示ラベルの価格は素材（織りテープ／コーティング／印刷）と數量で計算し、300–500 枚から承っております。大変お求めやすい価格です。どのタイプのお見積りが必要ですか？";
        if (st.topic === "bags" || st.topic === "paperbag") return "包裝袋のお見積りはサイズ、厚み、印刷、數量によって異なります。ご要望（サイズ＋數量＋ロゴ印刷の有無）をお送りいただければ、24時間以內にお見積りをご提示いたします 👍";
        return "かしこまりました。正確にお見積りするために、① 製品タイプ ② 數量 ③ デザイン／サイズをお知らせください。まずはどの製品かをお伝えいただき、殘りの情報は sales@taigetag.com までお送りください 😊";
      } },
      { id: "leadtime", kws: ["交期", "貨期", "多久", "多長時間", "什麼時候", "lead", "lead time", "delivery", "how long", "délai", "plazo", "幾天", "納期", "リードタイム", "生産期間", "何日"], reply: "サンプル作成は通常 3–7 日、量産の納期は數量と加工によって通常 10–25 日です。ご註文前に書面で納期を確認いたしますのでご安心ください 😊" },
      { id: "payment", kws: ["付款", "怎麼付", "定金", "信用證", "tt", "l/c", "payment", "deposit", "paiement", "pago", "支払", "支払い", "決済", "手付金", "前払い"], reply: "通常のお取引條件は、30% の手付金と、出荷前に殘り 70% をお支払いいただく形です。T/T の銀行送金に対応しており、大口のご註文では L/C もご相談いただけます。初めてのお取引のお客様には、詳細な支払條件をご案內いたします。" },
      { id: "shipping", kws: ["運費", "物流", "快遞", "海運", "空運", "fob", "exw", "dhl", "shipping", "freight", "expédition", "envío", "輸送", "送料", "船便", "航空便", "発送", "宅配"], reply: "出荷方法は複數ご用意しております。FOB 深セン／広州、EXW 工場渡し、または當社が船便・航空便・宅配便（DHL、FedEx、UPS など）を手配いたします。小口のサンプルは宅配便が最もお得です 📦" },
      { id: "oem", kws: ["定製", "oem", "odm", "來樣", "設計", "logo", "custom", "design", "personnalisé", "personalizado", "カスタマイズ", "特注", "オーダー", "デザイン", "ロゴ"], reply: "OEM／ODM およびサンプルベースのカスタマイズに対応しております。デザイン部がデータの最適化をお手伝いし、色、素材、加工を柔軟に組み合わせて、サンプル作成から量産まで一貫対応いたします。デザインデータはお持ちですか、それともデザインからご依頼ですか？" },
      { id: "quality", kws: ["質量", "質檢", "品控", "合格", "quality", "qc", "certification", "qualité", "calidad", "認證", "品質", "検品", "品質管理", "認証"], reply: "原材料検査 → 印刷工程の抜き取り検査 → 完成品の全數検査 → 出荷前の再検査という、完全な品質管理體制を実施しております。営業許可証および各種資格を保有しており、検査報告書のご提供も可能です 📋" },
      { id: "company", kws: ["公司", "工廠", "介紹", "泰閣", "tage", "哪裏", "地址", "company", "factory", "where", "about", "entreprise", "empresa", "會社", "工場", "會社概要", "所在", "どこ", "紹介"], reply: "東莞泰閣包裝製品有限公司（Dongguan Tage Packaging Products Co., Ltd.）は広東省東莞市虎門に位置し、衣料副資材一筋 20 年：タグ、織りラベル、洗濯表示ラベル、包裝袋をワンストップで生産し、世界 40+ の國と地域へ輸出しております 🇨🇳🌍" },
      { id: "contact", kws: ["聯繫", "電話", "微信", "郵箱", "email", "wechat", "whatsapp", "phone", "contact", "téléphone", "contacto", "連絡", "電話", "メール", "お問い合わせ", "問い合わせ"], reply: "いつでもご連絡ください！📧 sales@taigetag.com ｜📱 電話／WhatsApp／WeChat：+86 131 2811 8931 ｜📍 中國広東省東莞市虎門鎮。ご要望には通常 24時間以內に返信いたします（営業時間內はより早く対応できます）😊" },
      { id: "order", kws: ["下單", "訂購", "買", "怎麼合作", "流程", "order", "process", "how to buy", "commande", "pedido", "註文", "発注", "取引", "流れ", "手順"], reply: "お取引の流れは簡単です。① ご要望・デザインデータをお送りいただく → ② 24時間以內にお見積り → ③ サンプル作成 → ④ サンプル確認後に量産 → ⑤ 検品・出荷。どのステップからでも開始できます！" },
      { id: "faq", kws: ["常見問題", "faq", "問題", "help", "aide", "question", "よくある質問", "質問", "ヘルプ", "疑問"], reply: "よくあるご質問への回答です。\n📦 最小ロット：タグ 2,000+、織りラベル 1,000+、洗濯表示ラベル 300+ \n🧪 サンプル：3–7 日で発送\n💰 お見積り：24時間以內\n🚚 納期：10–25 日\nその他のご質問もお気軽にお尋ねください。" }
    ]
  };
  /* ---------- 韓語（/ko/ 目錄） ---------- */
  T.ko = {
    online: "온라인", hello: "안녕하세요! TAGE(泰閣) 스마트 상담원입니다 🐓 행택, 직조 라벨, 세탁 표시 라벨, 포장백에 대해 무엇이든 물어보세요. 원하시는 내용을 그대로 말씀해 주셔도 됩니다.",
    ph: "질문을 입력해 주세요…", send: "보내기",
    quick: ["어떤 제품이 있나요?", "최소 주문량은 얼마인가요?", "샘플 제작이 가능한가요?", "견적은 어떻게 받나요?"],
    followupQuote: "💡 안내: 디자인 파일이나 수량을 sales@taigetag.com 으로 보내주시면 24시간 이내에 정확한 견적을 드립니다. 위챗 13128118931 으로 연락하시면 더 빠릅니다.",
    fallback: "이 부분은 확인이 필요합니다 🤔 구체적인 요구사항을 sales@taigetag.com 으로 보내주시거나 위챗 13128118931 으로 연락해 주세요. 담당자가 24시간 이내에 정확하게 답변드립니다. 페이지 하단의 문의하기 양식을 이용하셔도 됩니다.",
    intents: [
      { id: "hello", kws: ["你好", "您好", "嗨", "哈嘍", "hello", "hi", "hey", "在嗎", "在不在", "안녕하세요", "안녕", "반갑습니다", "여보세요"], reply: "안녕하세요! 무엇을 도와드릴까요? 😊 제품, 최소 주문량, 샘플 제작, 견적 등 무엇이든 물어보세요. 원하시는 내용을 그대로 말씀해 주셔도 됩니다." },
      { id: "thanks", kws: ["謝謝", "感謝", "thank", "thanks", "thx", "3q", "merci", "gracias", "감사", "고맙", "감사합니다"], reply: "천만에요! 😄 샘플이나 견적이 필요하시면 언제든지 연락 주세요." },
      { id: "bye", kws: ["再見", "拜拜", "bye", "88", "goodbye", "see you", "안녕히", "잘 가", "바이바이"], reply: "안녕히 가세요! 사업 번창하시길 바랍니다 🚀 필요하실 때 언제든 찾아주세요." },
      { id: "product", kws: ["產品", "什麼", "有哪些", "做什麼", "品類", "product", "produce", "range", "offer", "what do you make", "offre", "productos", "제품", "상품", "품목", "제품군", "종류"], reply: "저희는 6개 제품 라인을 생산합니다.\n① 의류 행택(아트지/크라프트지/PVC, 금박 UV 무광 코팅)\n② 직조 라벨/메인 라벨(새틴/자카드/이중 직조 가장자리)\n③ 세탁 표시 라벨(직조 테이프/코팅/인쇄)\n④ 포장백(PE 비닐백/지퍼백/정전기 방지백)\n⑤ 친환경 종이백(크라프트지/백색 카드지)\n⑥ 브로슈어(카탈로그/리플렛)\n모두 맞춤 제작과 OEM이 가능합니다. 어느 제품에 관심이 있으신가요?" },
      { id: "hangtag", kws: ["吊牌", "掛卡", "hangtag", "hang tag", "tag", "étiquette suspendue", "etiqueta colgante", "標籤卡", "행택", "태그", "가격표"], reply: "행택은 저희 주력 제품입니다 👍 소재는 아트지(300-400g), 크라프트지, 면지, 방수 PVC 등이 있습니다. 가공은 금박, 엠보싱, 부분 UV, 라미네이팅을 지원하며, 크기는 일반적으로 35×70 / 40×90 / 50×90mm 이고 이형 재단도 가능합니다. 소재 선택을 도와드릴까요?" },
      { id: "woven", kws: ["織嘜", "主嘜", "緞面", "提花", "woven", "satin", "jacquard", "tissé", "tejida", "商標", "직조 라벨", "직조라벨", "직조", "메인 라벨", "새틴", "자카드"], reply: "직조 라벨/메인 라벨은 새틴, 평직, 자카드, 이중 직조 가장자리 등의 직조 방식이 있으며 무늬가 정교하고 세탁에도 변색되지 않습니다. 메인 라벨에는 새틴이나 자카드, 사이즈 라벨에는 태피터를 권장합니다. 메인 라벨과 사이즈 라벨 중 어느 것이 필요하신가요?" },
      { id: "carelabel", kws: ["洗水標", "洗標", "水洗標", "care label", "washing", "entretien", "de cuidado", "세탁 표시 라벨", "세탁표시라벨", "세탁 라벨", "세탁", "케어 라벨"], reply: "세탁 표시 라벨은 세 가지가 있습니다. 직조 테이프, 코팅, 인쇄 타입으로 각국의 세탁 표시 규격에 적합하며 정보가 선명하고 오래갑니다. 일반적인 조합은 직조 메인 라벨과 인쇄 세탁 표시 라벨로, 품질과 비용을 모두 만족합니다. 세탁 조건에 맞춰 추천해 드릴까요?" },
      { id: "bags", kws: ["包裝袋", "膠袋", "自封袋", "拉鍊袋", "poly bag", "ziplock", "bag", "poly", "sac", "bolsa", "포장백", "비닐백", "지퍼백", "폴리백", "봉투", "자루"], reply: "포장백은 PE/CPE 비닐백, 지퍼백, 접착 테이프백, 정전기 방지백을 취급합니다. 브랜드 로고 인쇄가 가능하며 크기와 두께는 요구사항에 맞춰 제작합니다. 의류 수출에는 투명 OPP 백의 가성비가 매우 좋습니다 👍" },
      { id: "paperbag", kws: ["紙袋", "牛皮紙袋", "環保袋", "paper bag", "kraft", "eco bag", "sac papier", "bolsa de papel", "친환경 종이백", "종이백", "종이 봉투", "크라프트", "에코백"], reply: "친환경 종이백은 크라프트지 또는 백색 카드지를 사용하며, 생분해되어 환경에 좋고 브랜드 인쇄와 손잡이 맞춤 제작도 지원합니다. 유럽 고객님들이 특히 중요하게 여기시는 부분입니다 🌱 친환경 옵션을 보시겠어요?" },
      { id: "brochure", kws: ["畫冊", "手冊", "摺頁", "目錄", "brochure", "catalog", "catalogue", "flyer", "folleto", "브로슈어", "카탈로그", "리플렛", "팸플릿", "책자"], reply: "브로슈어, 카탈로그, 리플렛 모두 제작 가능하며 용지 선정부터 제본까지 전 과정의 품질을 관리합니다. 브랜드 VI 파일을 보내주시면 디자인팀이 무료로 편집 제안을 드립니다." },
      { id: "moq", kws: ["起訂", "moq", "最小", "多少起", "數量", "quantity", "minimum", "quantité", "mínimo", "최소 주문량", "최소주문량", "최소 주문", "최소 로트", "주문량", "최소 수량", "몇 개부터"], reply: function (st) {
        if (st.topic === "hangtag") return "행택 최소 주문량은 2,000–3,000 장부터 시험 주문이 가능하며, 10,000 장 이상이면 단가가 더 유리합니다. 몇 장 정도 계획하고 계신가요?";
        if (st.topic === "woven") return "직조 라벨은 일반적으로 1,000 장 이상부터 제작하며, 자카드와 이중 직조 가장자리는 가격이 조금 다릅니다. 정확한 수량이 필요하신가요?";
        if (st.topic === "carelabel") return "세탁 표시 라벨은 300–500 장부터 제작 가능하며 비용 부담이 적습니다 👍 어떤 타입(직조 테이프/코팅/인쇄)을 원하시나요?";
        if (st.topic === "bags" || st.topic === "paperbag") return "포장백 최소 주문량은 유연합니다. 크기와 인쇄 내용에 따라 다르며 수백 장의 샘플백도 제작 가능합니다. 어떤 크기를 원하시나요?";
        return "최소 주문량은 제품에 따라 다릅니다. 행택은 2,000–3,000 장 시험 주문, 직조 라벨은 1,000 장 이상, 세탁 표시 라벨은 300–500 장부터, 포장백은 유연하게 대응합니다. 어떤 제품을 계획하고 계신가요?";
      } },
      { id: "sample", kws: ["打樣", "樣品", "樣板", "樣版", "sample", "prototype", "échantillon", "muestra", "打版", "샘플 제작", "샘플", "견본", "시제품"], reply: "샘플 제작이 가능합니다! 보통 3–7일 이내에 실물 샘플을 발송해 드리며 무료 샘플 제작 제안도 드립니다. 대량 주문 전에 인쇄 품질과 소재 감촉을 먼저 확인하시는 것을 모든 고객님께 권장합니다 😊 디자인 파일이나 참고 이미지를 보내주실 수 있나요?" },
      { id: "quote", kws: ["報價", "價格", "多少錢", "費用", "成本", "怎麼算", "詢價", "quote", "price", "cost", "how much", "devis", "prix", "presupuesto", "precio", "견적", "가격", "단가", "얼마", "비용", "원가"], reply: function (st) {
        if (st.topic === "hangtag") return "행택의 경우 가격은 주로 소재, 크기, 인쇄 색수, 가공에 따라 결정됩니다. 아트지 표준 타입은 천 장 단위에서 단가가 매우 합리적이며, 금박이나 이형 재단은 조금 더 높습니다. 대략 몇 장이 필요하신가요? 디자인을 sales@taigetag.com 으로 보내주시면 정확한 견적을 드릴 수 있습니다 😊";
        if (st.topic === "woven") return "직조 라벨 견적은 직조 방식(새틴/자카드/이중)과 크기에 따라 다르며 일반적으로 1,000 장 이상부터 제작합니다. 디자인 파일을 보내주시면 24시간 이내에 정확한 견적을 드립니다.";
        if (st.topic === "carelabel") return "세탁 표시 라벨 가격은 소재(직조 테이프/코팅/인쇄)와 수량으로 계산하며 300–500 장부터 제작 가능하고 가격이 매우 합리적입니다. 어떤 타입의 견적이 필요하신가요?";
        if (st.topic === "bags" || st.topic === "paperbag") return "포장백 견적은 크기, 두께, 인쇄, 수량에 따라 다릅니다. 요구사항(크기+수량+로고 인쇄 여부)을 보내주시면 24시간 이내에 견적을 드립니다 👍";
        return "네, 알겠습니다! 정확한 견적을 위해 ① 제품 종류 ② 수량 ③ 디자인/크기를 알려주세요. 먼저 어떤 제품인지 말씀해 주시고 나머지 내용은 sales@taigetag.com 으로 보내주시면 됩니다 😊";
      } },
      { id: "leadtime", kws: ["交期", "貨期", "多久", "多長時間", "什麼時候", "lead", "lead time", "delivery", "how long", "délai", "plazo", "幾天", "납기", "리드타임", "생산 기간", "며칠", "얼마나 걸"], reply: "샘플 제작은 보통 3–7일, 양산 납기는 수량과 가공에 따라 보통 10–25일입니다. 주문 전에 납기를 서면으로 확인해 드리니 걱정하지 마세요 😊" },
      { id: "payment", kws: ["付款", "怎麼付", "定金", "信用證", "tt", "l/c", "payment", "deposit", "paiement", "pago", "결제", "지불", "계약금", "선금", "송금"], reply: "일반적인 거래 조건은 30% 계약금과 출하 전 잔액 70% 지불입니다. T/T 은행 송금을 지원하며 대량 주문은 L/C 도 협의 가능합니다. 첫 거래 고객님께는 자세한 결제 조건을 안내해 드립니다." },
      { id: "shipping", kws: ["運費", "物流", "快遞", "海運", "空運", "fob", "exw", "dhl", "shipping", "freight", "expédition", "envío", "배송", "운송", "선적", "해상", "항공", "택배", "운임"], reply: "다양한 출하 방식을 지원합니다. FOB 선전/광저우, EXW 공장 인도, 또는 저희가 해상/항공/특송(DHL, FedEx, UPS 등)을 주선해 드립니다. 소량 샘플은 특송이 가장 경제적입니다 📦" },
      { id: "oem", kws: ["定製", "oem", "odm", "來樣", "設計", "logo", "custom", "design", "personnalisé", "personalizado", "맞춤", "주문 제작", "커스텀", "디자인", "로고", "도안"], reply: "OEM/ODM 및 샘플 기반 맞춤 제작을 지원합니다. 디자인팀이 시안 최적화를 도와드리며 색상, 소재, 가공을 유연하게 조합하여 샘플 제작부터 양산까지 원스톱으로 대응합니다. 디자인 파일을 가지고 계신가요, 아니면 디자인도 필요하신가요?" },
      { id: "quality", kws: ["質量", "質檢", "品控", "合格", "quality", "qc", "certification", "qualité", "calidad", "認證", "품질", "검품", "품질 관리", "인증", "합격"], reply: "원자재 검사 → 인쇄 공정 샘플링 검사 → 완제품 전수 검사 → 출하 전 재검사로 이어지는 완전한 품질 관리 프로세스를 운영합니다. 사업자등록증과 각종 자격을 보유하고 있으며 시험 성적서도 제공해 드립니다 📋" },
      { id: "company", kws: ["公司", "工廠", "介紹", "泰閣", "tage", "哪裏", "地址", "company", "factory", "where", "about", "entreprise", "empresa", "회사", "공장", "소개", "어디", "주소", "회사 소개"], reply: "둥관 TAGE 패키징 유한공사(Dongguan Tage Packaging Products Co., Ltd.)는 광둥성 둥관시 후먼에 위치하며 의류 부자재 20년 전문 기업입니다. 행택, 직조 라벨, 세탁 표시 라벨, 포장백을 원스톱으로 생산하고 전 세계 40+ 개국에 수출합니다 🇨🇳🌍" },
      { id: "contact", kws: ["聯繫", "電話", "微信", "郵箱", "email", "wechat", "whatsapp", "phone", "contact", "téléphone", "contacto", "연락", "전화", "이메일", "위챗", "문의", "연락처"], reply: "언제든 연락 주세요! 📧 sales@taigetag.com ｜📱 전화/WhatsApp/위챗: +86 131 2811 8931 ｜📍 중국 광둥성 둥관시 후먼진. 문의는 보통 24시간 이내에 답변드립니다(근무 시간에는 더 빠릅니다) 😊" },
      { id: "order", kws: ["下單", "訂購", "買", "怎麼合作", "流程", "order", "process", "how to buy", "commande", "pedido", "주문", "발주", "구매", "거래", "절차", "진행"], reply: "거래 절차는 간단합니다. ① 요구사항/디자인 파일 전송 → ② 24시간 이내 견적 → ③ 샘플 제작 → ④ 샘플 확인 후 양산 → ⑤ 검품 및 출하. 어느 단계에서든 시작하실 수 있습니다!" },
      { id: "faq", kws: ["常見問題", "faq", "問題", "help", "aide", "question", "자주 묻는 질문", "질문", "도움말", "문의 사항"], reply: "자주 묻는 질문 답변입니다.\n📦 최소 주문량: 행택 2,000+, 직조 라벨 1,000+, 세탁 표시 라벨 300+ \n🧪 샘플: 3–7일 발송\n💰 견적: 24시간 이내\n🚚 납기: 10–25일\n더 자세한 내용은 언제든 물어보세요." }
    ]
  };

  var t = T[LANG];

  /* ---------- 對話狀態（多輪上下文） ---------- */
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

  /* ---------- 意圖匹配引擎（返回最優+次優，支持多詞 AND） ---------- */
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

  /* ---------- 處理用戶輸入 ---------- */
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
        /* 雙向上下文提升：產品詞+諮詢詞同時命中 → 回覆用諮詢意圖，產品記爲主題 */
        if (res.second && CONSULT.indexOf(res.second.id) >= 0 && PRODUCTS.indexOf(it.id) >= 0) {
          state.topic = it.id;
          it = res.second;
        } else if (res.second && CONSULT.indexOf(it.id) >= 0 && PRODUCTS.indexOf(res.second.id) >= 0) {
          state.topic = res.second.id;
        } else {
          state.topic = it.id;
        }
        appendMsg(resolveReply(it), "ai");
        /* 追問：報價流程且還沒引導過 */
        if (it.id === "quote" && !state.quoted) {
          setTimeout(function () { appendMsg(t.followupQuote, "ai"); }, 500);
          state.quoted = true;
        }
      } else {
        appendMsg(t.fallback, "ai");
      }
    }, 450);
  }

  /* 觸屏設備不自動聚焦（避免 iOS 鍵盤頂起面板） */
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
