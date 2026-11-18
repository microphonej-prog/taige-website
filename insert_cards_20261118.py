# -*- coding: utf-8 -*-
"""把两篇新文章卡片插到 blog/index.html 的 post-grid 顶部。"""
import html

def A(d):
    return " ".join('data-%s="%s"' % (l, html.escape(d[l], quote=True)) for l in ["zh", "en", "fr", "es", "ja", "ko"])

def card(tag, h3, p, href):
    return (
        '      <article class="post-card">\n'
        '        <span class="tag" %s>%s</span>\n'
        '        <h3 %s>%s</h3>\n'
        '        <p %s>%s</p>\n'
        '        <a class="more" href="%s" data-zh="閱讀全文 →" data-en="Read more →" data-fr="Lire la suite →" data-es="Leer más →" data-ja="続きを読む →" data-ko="자세히 보기 →">閱讀全文 →</a>\n'
        '      </article>\n' % (
            A(tag), tag["zh"], A(h3), h3["zh"], A(p), p["zh"], href))

CARDS = []

CARDS.append(card(
    {"zh": "洗水標與合規", "en": "Care Labels & Compliance", "fr": "Étiquetage et conformité",
     "es": "Etiquetado y cumplimiento", "ja": "洗濯表示・コンプライアンス", "ko": "세탁 표시·컴플라이언스"},
    {"zh": "洗水標纖維成分容差：3% 容許與「其他纖維」", "en": "Care Label Fibre Tolerance: the 3% Rule",
     "fr": "Tolérance de composition : la règle des 3 %", "es": "Tolerancia de composición: la regla del 3 %",
     "ja": "混用率の許容範囲と「その他繊維」", "ko": "혼용률 허용 오차와 '기타 섬유'"},
    {"zh": "標上寫的成分能差多少：歐盟 3% 容差、美國 5% 其他纖維門檻、整數取整規則，附 62/33/5 實例、四市場法源對照與實驗室判定方式。",
     "en": "How far a stated composition may drift: the 3% tolerance, the 5% other-fibre threshold, whole-percent rounding, a 62/33/5 example and a four-market table.",
     "fr": "Jusqu'où une composition déclarée peut dériver : tolérance de 3 %, seuil de 5 %, arrondi entier, exemple 62/33/5 et tableau de quatre marchés.",
     "es": "Cuánto puede desviarse la composición declarada: tolerancia del 3 %, umbral del 5 %, redondeo entero, ejemplo 62/33/5 y tabla de cuatro mercados.",
     "ja": "表示した混用率はどこまでずれてよいか。3 % の許容、5 % 未満の「その他繊維」、整数への丸め、62/33/5 の実例、4 市場の根拠対照。",
     "ko": "표시한 혼용률이 어디까지 허용되는가. 3% 허용, 5% 미만 기타 섬유, 정수 반올림, 62/33/5 예시, 4개 시장 근거 대조."},
    "care-label-fiber-content-tolerance-guide.html"))

CARDS.append(card(
    {"zh": "品質與檢測", "en": "Quality & Testing", "fr": "Qualité et essais",
     "es": "Calidad y ensayos", "ja": "品質・試験", "ko": "품질·시험"},
    {"zh": "輔料測試報告怎麼讀：方法、級數與門檻", "en": "How to Read a Trim Test Report",
     "fr": "Lire un rapport d'essai d'accessoires", "es": "Cómo leer un informe de ensayo",
     "ja": "副資材の試験報告書の読み方", "ko": "부자재 시험 성적서 읽는 법"},
    {"zh": "方法編號先於結論：灰卡 1–5 級與半級、耐洗與耐摩擦的常見門檻、最常被跳過的四欄，以及報告不能替代的三件事。",
     "en": "Method codes come before results: grey scale grades 1 to 5, typical wash and rub thresholds, the four skipped fields and three things a report cannot replace.",
     "fr": "Le code méthode prime : échelle de gris 1 à 5, seuils usuels, quatre champs oubliés et trois limites du rapport.",
     "es": "El código de método manda: escala de grises 1 a 5, umbrales habituales, cuatro campos olvidados y tres límites del informe.",
     "ja": "方法番号が結論より先。グレースケール 1〜5 級、洗濯・摩擦のしきい値、見落とす 4 欄、報告書で代替できない 3 点。",
     "ko": "결론보다 방법 번호가 먼저. 그레이 스케일 1~5급, 세탁·마찰 기준, 놓치기 쉬운 네 항목, 성적서로 대체할 수 없는 세 가지."},
    "trim-test-report-reading-guide.html"))

p = "blog/index.html"
s = open(p, encoding="utf-8", newline="").read()
marker = '<div class="post-grid">\n'
assert s.count(marker) == 1, s.count(marker)
assert "care-label-fiber-content-tolerance-guide" not in s, "卡片已存在"
s = s.replace(marker, marker + "\n" + "".join(CARDS), 1)
open(p, "w", encoding="utf-8", newline="").write(s)
print("插入卡片 2 张，文件大小", len(s.encode("utf-8")))
