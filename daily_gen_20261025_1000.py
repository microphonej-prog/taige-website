#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-25 10:00 批次每日更新生成脚本（六语：zh-Hant 根 / en / ja / ko / fr / es）
- 德国供应链尽职调查法（LkSG）与辅料供应商（german-supply-chain-act-trims-suppliers）
- 辅料出口贸易术语 EXW/FCA/FOB/CIF/DDP（trim-export-incoterms-guide）

用法: F:/hermes/venvs/tools/Scripts/python.exe daily_gen_20261025_1000.py
"""
import os, re, sys, subprocess, importlib.util

ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)
PY = sys.executable

SKEL = "blog/knitwear-sweater-trims-guide.html"
DATE_ZH = "2026年10月25日"
DATE_EN = "October 25, 2026"
DATE_JA = "2026年10月25日更新"
DATE_KO = "2026년 10월 25일 업데이트"
DATE_FR = "25 octobre 2026"
DATE_ES = "25 de octubre de 2026"
SITEMAP_DATE = "2026-10-25"
BUST_OLD, BUST_NEW = "179", "180"
LANGS = ["en", "ja", "ko", "fr", "es"]

ARTICLES = [
    dict(
        slug="german-supply-chain-act-trims-suppliers.html",
        body="blog/_body_lksg.html",
        title_zh="德国供应链尽职调查法（LkSG）指南：服装辅料供应商要准备什么 | TAGE",
        title_en="German Supply Chain Act (LkSG): What Trims Suppliers Must Prepare | TAGE",
        title_ja="ドイツ供給網デューデリジェンス法（LkSG）ガイド：副資材サプライヤーの準備 | TAGE",
        title_ko="독일 공급망 실사법(LkSG) 가이드: 부자재 공급사가 준비할 것 | TAGE",
        title_fr="Loi allemande sur la chaîne d'approvisionnement (LkSG) : ce qu'un accessoiriste doit préparer | TAGE",
        title_es="Ley alemana de cadena de suministro (LkSG): qué debe preparar un proveedor de accesorios | TAGE",
        desc_zh="德国《供应链尽职调查法》LkSG 要求德国客户把防止强迫劳动、化学品与废水管理义务传给供应商。本文列出辅料厂被索要的五类文件、审核最易失分的三处、如何用 BSCI 或 SMETA 报告补齐，附 12 个月准备清单。来自东莞泰阁包装。",
        desc_en="Germany's LkSG pushes human rights and environmental duties onto trims suppliers: the five documents buyers demand, three audit failures and a 12-month plan.",
        desc_ja="ドイツの LkSG により、人権・環境のデューデリジェンス義務は副資材サプライヤーまで及びます。顧客が求める5種類の書類、監査で最も多い3つの失点、BSCI や SMETA を活用した低コストの整え方、12か月の準備計画を解説します。東莞泰閣包装。",
        desc_ko="독일 LkSG로 인권·환경 실사 의무가 부자재 공급사까지 전달됩니다. 고객이 요구하는 다섯 가지 자료, 감사에서 가장 흔한 세 가지 실점, BSCI·SMETA를 활용한 저비용 보완, 12개월 준비 계획을 정리했습니다. 둥관 TAGE 패키징.",
        desc_fr="La LkSG allemande fait descendre les obligations droits humains et environnement jusqu'aux accessoiristes : cinq documents demandés, trois échecs d'audit fréquents et un plan sur douze mois.",
        desc_es="La LkSG alemana traslada las obligaciones de derechos humanos y medio ambiente a los proveedores de accesorios: cinco documentos, tres fallos de auditoría y un plan de doce meses.",
        crumb_zh="德国供应链尽职调查法",
        crumb_en="German Supply Chain Act",
        crumb_ja="ドイツ供給網デューデリジェンス法",
        crumb_ko="독일 공급망 실사법",
        crumb_fr="Loi allemande sur la chaîne d'approvisionnement",
        crumb_es="Ley alemana de cadena de suministro",
        h1_zh="德国供应链尽职调查法（LkSG）指南：服装辅料供应商要准备什么",
        h1_en="German Supply Chain Act (LkSG): What Trims Suppliers Must Prepare",
        h1_ja="ドイツ供給網デューデリジェンス法（LkSG）ガイド：副資材サプライヤーが準備すべきこと",
        h1_ko="독일 공급망 실사법(LkSG) 가이드: 부자재 공급사가 준비해야 할 것",
        h1_fr="Loi allemande sur la chaîne d'approvisionnement (LkSG) : ce qu'un accessoiriste doit préparer",
        h1_es="Ley alemana de cadena de suministro (LkSG): qué debe preparar un proveedor de accesorios",
        tag_zh="合规指南", tag_en="Compliance", tag_ja="コンプライアンス", tag_ko="컴플라이언스",
        tag_fr="Conformité", tag_es="Cumplimiento",
        sum_zh="德国《供应链企业尽职调查法》的义务主体是德国企业，但压力会跟着订单传到辅料厂：客户会索要人权与环保政策、供应商自查问卷、社会责任审核报告、化学品记录和申诉渠道说明。本文讲清这五类文件各自要写什么、外发工序漏报与三套数据不一致为什么最容易被判不通过，以及怎样用现有 BSCI 或 SMETA 报告补齐缺口，最后给一份 12 个月、不需要额外雇人的准备清单。",
        sum_en="The duty holder under Germany's LkSG is the German company, but the pressure arrives with the order: buyers ask for human rights and environmental policies, self-assessment questionnaires, social audit reports, chemical records and a grievance channel. This guide explains what each of the five documents must contain, why undeclared outsourcing and contradicting time-wage-production records fail most often, and how to close the gaps with an existing BSCI or SMETA report. It closes with a twelve-month plan that needs no extra headcount.",
        sum_ja="ドイツの LkSG の義務主体はドイツ企業ですが、圧力は注文とともに副資材工場へ届きます。顧客は人権・環境方針、自己評価質問票、社会的責任監査報告書、化学物質記録、苦情窓口の説明を求めます。5種類の書類に何を書くべきか、外注工程の未申告や勤怠・給与・生産記録の不一致がなぜ最も不合格になりやすいのか、既存の BSCI や SMETA 報告書でどう穴を埋めるかを解説し、増員不要の12か月準備計画で締めくくります。",
        sum_ko="독일 LkSG의 의무 주체는 독일 기업이지만 압력은 주문과 함께 부자재 공장으로 옵니다. 고객은 인권·환경 방침, 자체 평가 설문, 사회적 책임 감사 보고서, 화학물질 기록, 고충 창구 안내를 요구합니다. 다섯 가지 자료에 무엇을 담아야 하는지, 외주 공정 미신고와 근태·급여·생산 기록 불일치가 왜 가장 자주 부적합이 되는지, 기존 BSCI·SMETA 보고서로 어떻게 보완하는지, 그리고 인력 충원 없이 실행하는 12개월 계획을 정리했습니다.",
        sum_fr="Le débiteur d'obligations au titre de la LkSG est l'entreprise allemande, mais la pression arrive avec la commande : politiques droits humains et environnement, questionnaires d'auto-évaluation, rapports d'audit social, registres chimiques et canal de réclamation. Ce guide précise le contenu attendu de chacun des cinq documents, explique pourquoi la sous-traitance non déclarée et des registres de pointage, de paie et de production incohérents sont les motifs d'échec les plus fréquents, et comment combler les écarts avec un rapport BSCI ou SMETA existant. Il se termine par un plan de douze mois sans embauche supplémentaire.",
        sum_es="El sujeto obligado por la LkSG es la empresa alemana, pero la presión llega con el pedido: políticas de derechos humanos y medio ambiente, cuestionarios de autoevaluación, informes de auditoría social, registros químicos y canal de reclamaciones. Esta guía detalla qué debe contener cada uno de los cinco documentos, explica por qué la subcontratación no declarada y los registros de horario, nómina y producción incoherentes son los fallos más frecuentes, y cómo cerrar brechas con un informe BSCI o SMETA existente. Termina con un plan de doce meses sin contratar más personal.",
    ),
    dict(
        slug="trim-export-incoterms-guide.html",
        body="blog/_body_incoterms.html",
        title_zh="辅料出口贸易术语指南：EXW、FCA、FOB、CIF、DDP 谁承担费用与风险 | TAGE",
        title_en="Incoterms for Trims Export: EXW, FCA, FOB, CIF and DDP Explained | TAGE",
        title_ja="副資材輸出の貿易条件ガイド：EXW・FCA・FOB・CIF・DDP の費用と危険 | TAGE",
        title_ko="부자재 수출 무역조건 가이드: EXW·FCA·FOB·CIF·DDP 비용과 위험 | TAGE",
        title_fr="Incoterms à l'export d'accessoires : EXW, FCA, FOB, CIF et DDP | TAGE",
        title_es="Incoterms en la exportación de accesorios: EXW, FCA, FOB, CIF y DDP | TAGE",
        desc_zh="辅料是轻货，贸易术语选错会把整单利润吃掉。本文拆解 EXW、FCA、FOB、CIF、DDP 的费用与风险分界、轻货按体积重计费的陷阱、DDP 的税号与拒收成本三个坑，附不易扯皮的报价格式。来自东莞泰阁包装。",
        desc_en="Trims are light cargo, so the wrong Incoterm eats the margin. Where cost and risk divide under EXW, FCA, FOB, CIF and DDP, plus a quote format that holds.",
        desc_ja="副資材は軽貨物で、貿易条件を誤ると利益が消えます。EXW・FCA・FOB・CIF・DDP の費用と危険の分岐、容積重量の落とし穴、DDP の税番・拒否コストの3つの罠、見積書の書式を解説します。東莞泰閣包装。",
        desc_ko="부자재는 경량 화물이라 무역 조건을 잘못 고르면 이익이 사라집니다. EXW·FCA·FOB·CIF·DDP의 비용과 위험 분기, 용적 중량 함정, DDP의 세 번·거부 비용 세 가지 함정, 견적서 형식을 정리했습니다. 둥관 TAGE 패키징.",
        desc_fr="Les accessoires sont légers : un Incoterm mal choisi mange la marge. Coûts et risques en EXW, FCA, FOB, CIF et DDP, piège du poids volumétrique et format de devis.",
        desc_es="Los accesorios son carga ligera: un Incoterm mal elegido se come el margen. Costes y riesgos en EXW, FCA, FOB, CIF y DDP, la trampa del peso volumétrico y un formato de presupuesto.",
        crumb_zh="辅料出口贸易术语",
        crumb_en="Export Incoterms",
        crumb_ja="輸出貿易条件",
        crumb_ko="수출 무역조건",
        crumb_fr="Incoterms à l'export",
        crumb_es="Incoterms de exportación",
        h1_zh="辅料出口贸易术语指南：EXW、FCA、FOB、CIF、DDP 谁承担费用与风险",
        h1_en="Incoterms for Trims Export: Who Pays and Who Carries the Risk",
        h1_ja="副資材輸出の貿易条件ガイド：EXW・FCA・FOB・CIF・DDP で費用と危険は誰が負うか",
        h1_ko="부자재 수출 무역조건 가이드: EXW·FCA·FOB·CIF·DDP에서 비용과 위험은 누가 지는가",
        h1_fr="Incoterms à l'export d'accessoires : qui paie et qui porte le risque",
        h1_es="Incoterms en la exportación de accesorios: quién paga y quién asume el riesgo",
        tag_zh="外贸实务", tag_en="Export", tag_ja="貿易実務", tag_ko="무역 실무",
        tag_fr="Export", tag_es="Exportación",
        sum_zh="吊牌、织唛、洗水标、包装袋单价低、体积大、重量轻，贸易术语用错，运费与关税的差额经常吃掉整单利润。本文用一张表讲清 EXW、FCA、FOB、CIF、DDP 五种术语谁报关、谁付运费、谁买保险、风险在哪一刻转移，再讲轻货按体积重计费的陷阱、DDP 下税号与拒收成本的三个坑，以及一份不容易扯皮的报价格式。面向做欧洲与美洲市场的服装品牌与采购代理。",
        sum_en="Hang tags, woven labels, care labels and packaging bags are cheap, bulky and light, so the wrong trade term lets freight and duty differences swallow the margin. One table sets out who clears export, pays freight, insures and when risk passes under EXW, FCA, FOB, CIF and DDP; then the volumetric-weight trap on light cargo, the three DDP pitfalls around tax numbers and refused goods, and a quotation format that avoids arguments. Written for brands and sourcing agents selling into Europe and the Americas.",
        sum_ja="タグ、織りラベル、洗濯表示ラベル、包装袋は単価が低く、かさばって軽いため、貿易条件を誤ると送料と関税の差額が利益を消します。EXW・FCA・FOB・CIF・DDP について、通関・運賃・保険を誰が担い、危険がいつ移るのかを一表で整理。さらに軽貨物の容積重量の落とし穴、DDP における税番と受取拒否の3つの罠、トラブルになりにくい見積書の書式を解説します。欧州・米州向けのブランドと購買代理店向け。",
        sum_ko="행택, 직조 라벨, 세탁 표시 라벨, 포장백은 단가가 낮고 부피가 크며 가벼워, 무역 조건을 잘못 고르면 운임과 관세 차액이 이익을 잠식합니다. EXW·FCA·FOB·CIF·DDP에서 누가 통관·운임·보험을 맡고 위험이 언제 이전되는지를 한 표로 정리하고, 경량 화물의 용적 중량 함정, DDP의 세 번과 수취 거부 관련 세 가지 함정, 분쟁이 적은 견적서 형식을 설명합니다. 유럽·미주 시장 브랜드와 소싱 에이전트용.",
        sum_fr="Étiquettes, labels tissés, étiquettes d'entretien et sacs sont bon marché, volumineux et légers : un Incoterm mal choisi laisse l'écart de fret et de droits absorber la marge. Un tableau précise, pour EXW, FCA, FOB, CIF et DDP, qui dédouane, qui paie le fret, qui assure et quand le risque se transfère ; puis le piège du poids volumétrique, les trois écueils du DDP autour des numéros fiscaux et des marchandises refusées, et un format de devis sans litige. Pour les marques et agents d'achat vendant en Europe et aux Amériques.",
        sum_es="Colgantes, etiquetas tejidas, etiquetas de cuidado y bolsas son baratos, voluminosos y ligeros: un Incoterm mal elegido deja que la diferencia de flete y aranceles absorba el margen. Una tabla aclara, para EXW, FCA, FOB, CIF y DDP, quién despacha, quién paga el flete, quién asegura y cuándo se transmite el riesgo; después, la trampa del peso volumétrico, los tres escollos del DDP con números fiscales y mercancía rechazada, y un formato de presupuesto sin discusiones. Para marcas y agentes de compras que venden en Europa y América.",
    ),
]

skel = open(SKEL, encoding="utf-8").read()
old3 = re.search(r'"position": 3,\s*"name": "([^"]*)"', skel).group(1)
print("骨架 breadcrumb 名:", old3)

# ---------------- 撞车安全闸 ----------------
for a in ARTICLES:
    if not os.path.exists(a["body"]):
        raise SystemExit("正文文件缺失：%s" % a["body"])
    for p in ["blog/%s" % a["slug"]] + ["%s/blog/%s" % (l, a["slug"]) for l in LANGS]:
        if os.path.exists(p):
            raise SystemExit("选题撞车：%s 已存在，换选题！" % p)
sm0 = open("sitemap.xml", encoding="utf-8").read()
for a in ARTICLES:
    if ("/blog/%s</loc>" % a["slug"]) in sm0:
        raise SystemExit("选题撞车：sitemap 已含 %s" % a["slug"])
print("选题全新，开始生成")

# ---------------- desc 长度体检 ----------------
for a in ARTICLES:
    print("  %-40s desc_zh=%d字 desc_en=%d字符 desc_ja=%d desc_ko=%d desc_fr=%d desc_es=%d"
          % (a["slug"], len(a["desc_zh"]), len(a["desc_en"]), len(a["desc_ja"]),
             len(a["desc_ko"]), len(a["desc_fr"]), len(a["desc_es"])))
if "--check" in sys.argv:
    sys.exit(0)

# ---------------- 1) 生成两篇文章（六语属性） ----------------
for a in ARTICLES:
    slug = a["slug"]
    s = skel.replace(SKEL.replace("blog/", ""), slug)

    title_line = ('<title data-zh="%s" data-en="%s" data-ja="%s" data-ko="%s" data-fr="%s" data-es="%s">%s</title>'
                  % (a["title_zh"], a["title_en"], a["title_ja"], a["title_ko"],
                     a["title_fr"], a["title_es"], a["title_zh"]))
    s = re.sub(r'<title[^>]*>.*?</title>', title_line, s, count=1, flags=re.S)

    s = re.sub(r'<meta name="description".*?content="[^"]*">', 'DESC_PLACEHOLDER', s, count=1, flags=re.S)
    desc_block = ('<meta name="description" data-zh="%s"\n'
                  '      data-en="%s" data-ja="%s" data-ko="%s"\n'
                  '      data-fr="%s"\n'
                  '      data-es="%s"\n'
                  '      content="%s">' % (a["desc_zh"], a["desc_en"], a["desc_ja"], a["desc_ko"],
                                           a["desc_fr"], a["desc_es"], a["desc_zh"]))
    s = s.replace('DESC_PLACEHOLDER', desc_block, 1)

    new_canon = ('<link rel="canonical" href="https://taigetag.com/blog/%s">\n'
                 '<link rel="alternate" hreflang="zh-Hant" href="https://taigetag.com/blog/%s">\n'
                 '<link rel="alternate" hreflang="en" href="https://taigetag.com/en/blog/%s">\n'
                 '<link rel="alternate" hreflang="fr" href="https://taigetag.com/fr/blog/%s">\n'
                 '<link rel="alternate" hreflang="es" href="https://taigetag.com/es/blog/%s">\n'
                 '<link rel="alternate" hreflang="ja" href="https://taigetag.com/ja/blog/%s">\n'
                 '<link rel="alternate" hreflang="ko" href="https://taigetag.com/ko/blog/%s">\n'
                 '<link rel="alternate" hreflang="x-default" href="https://taigetag.com/blog/%s">'
                 % ((slug,) * 8))
    s, n_href = re.subn(r'<link rel="canonical" href="[^"]*">(?:\n<link rel="alternate"[^\n]*>)+',
                        new_canon, s, count=1)
    assert n_href == 1, "hreflang 替换失败"

    crumb = ('<div class="crumb"><a href="../index.html" data-zh="首页" data-fr="Accueil" data-es="Inicio" data-en="Home" data-ja="ホーム" data-ko="홈">首页</a>'
             ' / <a href="index.html" data-zh="辅料 FAQ" data-fr="FAQ Accessoires" data-es="FAQ Accesorios" data-en="Trims FAQ" data-ja="副資材 FAQ" data-ko="부자재 FAQ">辅料 FAQ</a>'
             ' / <span data-zh="%s" data-en="%s" data-ja="%s" data-ko="%s" data-fr="%s" data-es="%s">%s</span></div>'
             % (a["crumb_zh"], a["crumb_en"], a["crumb_ja"], a["crumb_ko"],
                a["crumb_fr"], a["crumb_es"], a["crumb_zh"]))
    s, n = re.subn(r'<div class="crumb">.*?</div>', crumb, s, count=1, flags=re.S)
    assert n == 1, "crumb 替换失败"

    h1 = ('<h1 data-zh="%s" data-en="%s" data-ja="%s" data-ko="%s" data-fr="%s" data-es="%s">%s</h1>'
          % (a["h1_zh"], a["h1_en"], a["h1_ja"], a["h1_ko"], a["h1_fr"], a["h1_es"], a["h1_zh"]))
    s, n = re.subn(r'<h1 .*?</h1>', h1, s, count=1, flags=re.S)
    assert n == 1, "h1 替换失败"

    meta = ('<p data-zh="泰阁包装 · 更新于 %s" data-en="By TAGE Packaging &nbsp;·&nbsp; Updated %s" '
            'data-ja="泰閣包装 · %s" data-ko="TAGE 패키징 · %s" '
            'data-fr="Par TAGE Packaging &nbsp;·&nbsp; Mis à jour le %s" '
            'data-es="Por TAGE Packaging &nbsp;·&nbsp; Actualizado el %s">泰阁包装 · 更新于 %s</p>'
            % (DATE_ZH, DATE_EN, DATE_JA, DATE_KO, DATE_FR, DATE_ES, DATE_ZH))
    s, n = re.subn(r'<p data-zh="泰[阁閣]包[装裝] · 更新[于於][^"]*".*?</p>', meta, s, count=1, flags=re.S)
    assert n == 1, "meta 行替换失败"

    s = s.replace('"%s"' % old3, '"%s"' % a["h1_zh"])
    s, n = re.subn(r'"headline": "[^"]*"', '"headline": "%s"' % a["h1_zh"], s, count=1)
    assert n == 1, "headline 替换失败"

    body = open(a["body"], encoding="utf-8").read().rstrip("\n")
    i0 = s.index('  <section class="article-body">')
    i1 = s.index('\n</main>')
    s = s[:i0] + body + s[i1:]

    out = "blog/%s" % slug
    open(out, "w", encoding="utf-8", newline="").write(s)
    print("写入 %s (%d KB)" % (out, len(s.encode("utf-8")) // 1024))

# ---------------- 2) blog/index.html 顶部插入两张卡片 ----------------
CARD = '''      <article class="post-card">
        <span class="tag" data-zh="{tag_zh}" data-en="{tag_en}" data-ja="{tag_ja}" data-ko="{tag_ko}" data-fr="{tag_fr}" data-es="{tag_es}">{tag_zh}</span>
        <h3 data-zh="{h3_zh}" data-en="{h3_en}" data-ja="{h3_ja}" data-ko="{h3_ko}" data-fr="{h3_fr}" data-es="{h3_es}">{h3_zh}</h3>
        <p data-zh="{sum_zh}" data-en="{sum_en}" data-ja="{sum_ja}" data-ko="{sum_ko}" data-fr="{sum_fr}" data-es="{sum_es}">{sum_zh}</p>
        <a class="more" href="{slug}" data-zh="阅读全文 →" data-en="Read more →" data-ja="続きを読む →" data-ko="자세히 보기 →" data-fr="Lire la suite →" data-es="Leer más →">阅读全文 →</a>
      </article>
'''

cards = ""
for a in ARTICLES:
    cards += CARD.format(
        tag_zh=a["tag_zh"], tag_en=a["tag_en"], tag_ja=a["tag_ja"], tag_ko=a["tag_ko"],
        tag_fr=a["tag_fr"], tag_es=a["tag_es"],
        h3_zh=a["h1_zh"], h3_en=a["h1_en"], h3_ja=a["h1_ja"], h3_ko=a["h1_ko"],
        h3_fr=a["h1_fr"], h3_es=a["h1_es"],
        sum_zh=a["sum_zh"], sum_en=a["sum_en"], sum_ja=a["sum_ja"], sum_ko=a["sum_ko"],
        sum_fr=a["sum_fr"], sum_es=a["sum_es"],
        slug=a["slug"])

idx = "blog/index.html"
s = open(idx, encoding="utf-8").read()
marker = '<div class="post-grid">\n'
assert marker in s, "post-grid 未找到"
for a in ARTICLES:
    assert a["slug"] not in s, "卡已存在：%s" % a["slug"]
s = s.replace(marker, marker + "\n" + cards, 1)
open(idx, "w", encoding="utf-8", newline="").write(s)
print("blog/index.html 插入 2 张卡片完成")

# ---------------- 3) 简体 → 繁体（幂等） ----------------
spec = importlib.util.spec_from_file_location("to_traditional", os.path.join(ROOT, "to_traditional.py"))
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
changed = []
for p in ["blog/%s" % a["slug"] for a in ARTICLES] + [idx]:
    s0 = open(p, encoding="utf-8").read()
    s1 = mod.convert_html(s0)
    if s1 != s0:
        open(p, "w", encoding="utf-8", newline="").write(s1)
        changed.append(os.path.basename(p))
print("繁体转换改动: %d %s" % (len(changed), changed))

# ---------------- 4) gen_i18n 生成五语版本 ----------------
TARGETS = ["blog/%s" % a["slug"] for a in ARTICLES] + [idx]
for lang in LANGS:
    r = subprocess.run([PY, "gen_i18n.py", lang] + TARGETS, capture_output=True, text=True, encoding="utf-8")
    if r.returncode != 0:
        print(r.stdout[-3000:], r.stderr[-3000:])
        raise SystemExit("gen_i18n %s 失败" % lang)
    print("gen_i18n %s -> %d 文件 ok" % (lang, len(TARGETS)))

# ---------------- 5) sitemap ----------------
sm = open("sitemap.xml", encoding="utf-8", newline="").read()
before_lines = sm.count("\n")


def block(url):
    return ("  <url>\r\n    <loc>%s</loc>\r\n    <lastmod>%s</lastmod>\r\n"
            "    <changefreq>monthly</changefreq>\r\n    <priority>0.7</priority>\r\n  </url>\r\n"
            % (url, SITEMAP_DATE))


blocks = []
for a in ARTICLES:
    slug = a["slug"]
    for u in ["https://taigetag.com/blog/%s" % slug] + \
             ["https://taigetag.com/%s/blog/%s" % (l, slug) for l in LANGS]:
        assert "<loc>%s</loc>" % u not in sm, "sitemap 已有 %s" % u
        blocks.append(block(u))
sm = sm.replace("</urlset>", "".join(blocks) + "</urlset>", 1)

for u in ["https://taigetag.com/blog/index.html"] + \
         ["https://taigetag.com/%s/blog/index.html" % l for l in LANGS]:
    pat = re.compile(r'(<loc>%s</loc>\r?\n\s*<lastmod>)[^<]*(</lastmod>)' % re.escape(u))
    sm, n = pat.subn(r'\g<1>%s\g<2>' % SITEMAP_DATE, sm, count=1)
    assert n == 1, "blog index lastmod 未更新: %s" % u

open("sitemap.xml", "w", encoding="utf-8", newline="").write(sm)
print("sitemap 新增 %d 个 URL，行数 %d -> %d，<loc> 总数 %d"
      % (len(blocks), before_lines, sm.count("\n"), sm.count("<loc>")))

# ---------------- 6) BUST_VERSION 升级 ----------------
mj = open("js/main.js", encoding="utf-8").read()
assert 'var BUST_VERSION = "%s";' % BUST_OLD in mj, "BUST_VERSION 不是 %s" % BUST_OLD
mj = mj.replace('var BUST_VERSION = "%s";' % BUST_OLD, 'var BUST_VERSION = "%s";' % BUST_NEW, 1)
open("js/main.js", "w", encoding="utf-8", newline="").write(mj)
print("BUST_VERSION %s -> %s" % (BUST_OLD, BUST_NEW))
