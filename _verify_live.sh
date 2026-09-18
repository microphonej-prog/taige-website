#!/usr/bin/env bash
# 线上验证：2 篇新文章 × 4 语言 title 渲染 + sitemap 含新 URL
CHROME="/c/Program Files/Google/Chrome/Application/chrome.exe"
SLUGS=("clothing-label-compliance-colombia" "clothing-label-compliance-chile")
LANGS=("zh" "en" "fr" "es")

echo "== 线上 4 语 title（headless Chrome，?lang=xx&v=1 防缓存）=="
for S in "${SLUGS[@]}"; do
  for L in "${LANGS[@]}"; do
    URL="https://taigetag.com/blog/${S}.html?lang=${L}&v=1"
    T=$("$CHROME" --headless=new --disable-gpu --no-sandbox --virtual-time-budget=12000 --dump-dom "$URL" 2>/dev/null | grep -o "<title>[^<]*</title>" | head -1)
    echo "  [$L] ${S}.html"
    echo "      $T"
  done
done

echo "== 线上 sitemap 新 URL =="
SM=$(curl -s --max-time 40 "https://taigetag.com/sitemap.xml")
for S in "${SLUGS[@]}"; do
  for PRE in "blog/" "en/blog/" "fr/blog/" "es/blog/"; do
    U="https://taigetag.com/${PRE}${S}.html"
    if echo "$SM" | grep -q "<loc>${U}</loc>"; then echo "  OK   $U"; else echo "  MISS $U"; fi
  done
done
echo "  sitemap <loc> 总数: $(echo "$SM" | grep -c '<loc>')"
echo "  sitemap blog/index lastmod: $(echo "$SM" | grep -A1 'blog/index.html</loc>' | grep lastmod | head -1)"

echo "== 线上 HTTP 状态 =="
for S in "${SLUGS[@]}"; do
  for PRE in "blog/" "en/blog/" "fr/blog/" "es/blog/"; do
    CODE=$(curl -s -o /dev/null -w "%{http_code}" --max-time 30 "https://taigetag.com/${PRE}${S}.html")
    echo "  $CODE  https://taigetag.com/${PRE}${S}.html"
  done
done
echo "== 线上列表页含新卡片 =="
for PRE in "blog/" "en/blog/" "fr/blog/" "es/blog/"; do
  N=$(curl -s --max-time 30 "https://taigetag.com/${PRE}index.html" | grep -c "clothing-label-compliance-")
  echo "  ${PRE}index.html 命中新卡片链接数: $N"
done
