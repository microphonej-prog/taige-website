# -*- coding: utf-8 -*-
"""把 2026-11-20 08:00 两篇新文章卡片插到 blog/index.html 的 post-grid 顶部。"""
import html

LANGS = ["zh", "en", "fr", "es", "ja", "ko"]


def A(d):
    return " ".join('data-%s="%s"' % (l, html.escape(d[l], quote=True)) for l in LANGS)


def card(tag, h3, p, href):
    return (
        '      <article class="post-card">\n'
        '        <span class="tag" %s>%s</span>\n'
        '        <h3 %s>%s</h3>\n'
        '        <p %s>%s</p>\n'
        '        <a class="more" href="%s" data-zh="閱讀全文 →" data-en="Read more →" data-fr="Lire la suite →" data-es="Leer más →" data-ja="続きを読む →" data-ko="자세히 보기 →">閱讀全文 →</a>\n'
        '      </article>\n' % (
            A(tag), html.escape(tag["zh"], quote=True),
            A(h3), html.escape(h3["zh"], quote=True),
            A(p), html.escape(p["zh"], quote=True), href))


CARDS = []

CARDS.append(card(
    {"zh": "標籤與吊牌", "en": "Labels & Hang Tags", "fr": "Étiquettes",
     "es": "Etiquetas", "ja": "ネーム・下げ札", "ko": "라벨·행택"},
    {"zh": "吊牌改版：重印、貼標覆蓋還是換版號",
     "en": "Hang Tag Changes: Reprint, Over-Sticker or a New Version",
     "fr": "Modifier une étiquette pendante : réimpression, sur-étiquetage ou nouvelle version",
     "es": "Cambiar una etiqueta colgante: reimpresión, sobre-etiquetado o nueva versión",
     "ja": "下げ札の改版：再印刷・上貼り・版更新のどれを選ぶか",
     "ko": "행택 변경: 재인쇄·덧붙이기·새 버전 중 무엇을 고를까"},
    {"zh": "三條路徑的成本算法與起訂量影響，加上貼標覆蓋不能碰的四類法定信息、版本管控欄位與決定前六問。",
     "en": "Three routes costed out, the four fields a sticker must never cover, version-control fields and six questions before you commit.",
     "fr": "Trois voies chiffrées, les quatre champs qu'un autocollant ne doit jamais couvrir, le contrôle des versions et six questions à trancher.",
     "es": "Tres vías con cifras, los cuatro campos que una pegatina nunca debe cubrir, control de versiones y seis preguntas antes de decidir.",
     "ja": "3 ルートのコスト計算、シールで絶対に覆ってはいけない 4 項目、版管理の項目、決断前の 6 つの質問。",
     "ko": "세 경로의 원가 계산, 스티커로 절대 덮으면 안 되는 네 항목, 버전 관리 항목, 결정 전 여섯 질문."},
    "hang-tag-reprint-guide.html"))

CARDS.append(card(
    {"zh": "採購與成本", "en": "Sourcing & Cost", "fr": "Achats et coûts",
     "es": "Compras y costes", "ja": "調達・コスト", "ko": "소싱·원가"},
    {"zh": "取消款的輔料庫存：四條路徑與各自的代價",
     "en": "Leftover Trims After a Cancelled Style: Four Routes and What Each Costs",
     "fr": "Accessoires restants d'une collection annulée : quatre voies et leur coût",
     "es": "Accesorios sobrantes de una colección cancelada: cuatro vías y su coste",
     "ja": "企画中止で余った副資材：4 つの処理ルートとそのコスト",
     "ko": "시즌 취소로 남은 부자재: 네 가지 처리 경로와 비용"},
    {"zh": "留用、改造、轉讓、銷毀的回收率與風險對比，三件絕對不能做的事，以及舊庫存再出貨時重新觸發的法規義務。",
     "en": "Hold, rework, transfer or destroy: recovery and risk compared, three things never to do, and the rules that re-trigger on reuse.",
     "fr": "Conserver, transformer, céder ou détruire : récupération et risque comparés, trois interdits et les obligations réactivées au réemploi.",
     "es": "Guardar, transformar, ceder o destruir: recuperación y riesgo comparados, tres prohibiciones y obligaciones que se reactivan.",
     "ja": "保管・改造・譲渡・廃棄を回収率とリスクで比較。やってはいけない 3 つと、再出荷で再発動する法規義務。",
     "ko": "보관·개조·양도·폐기를 회수율과 리스크로 비교. 하면 안 되는 세 가지와 재출고 시 다시 발생하는 규제 의무."},
    "trim-dead-stock-guide.html"))

p = "blog/index.html"
s = open(p, encoding="utf-8", newline="").read()
marker = '<div class="post-grid">'
assert s.count(marker) == 1, s.count(marker)
assert "hang-tag-reprint-guide" not in s, "卡片已存在"
s = s.replace(marker, marker + "\n" + "\n" + "".join(CARDS), 1)

n_fix = s.count("&amp;amp;")
s = s.replace("&amp;amp;", "&amp;")

open(p, "w", encoding="utf-8", newline="").write(s)
print("插入卡片 2 张；修复双重转义 %d 处；文件大小 %d" % (n_fix, len(s.encode("utf-8"))))
