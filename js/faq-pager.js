/* FAQ / 文章列表分页：只显示最新 9 篇，其余用数字页码 + 上一页/下一页翻页
   设计要点：
   - 卡片全部保留在 DOM 里（爬虫照旧能看到全部 459 条内链），分页纯前端表现层
   - 每日文章 cron 往 .post-grid 里插新卡片时不需要改任何东西，页数自动重算
   - 文案按 <html lang> 取，语言切换是整页跳转（?lang=xx），所以每次加载都能取对
*/
(function () {
  var grid = document.querySelector('.post-grid');
  if (!grid) return;

  var PER = 9;                       /* 每页条数：改这里即可 */
  var cards = [].slice.call(grid.children).filter(function (el) {
    return el.nodeType === 1 && el.classList.contains('post-card');
  });
  var total = cards.length;
  var pages = Math.ceil(total / PER);
  if (pages <= 1) return;

  /* ---------- 文案 ---------- */
  var L = {
    'zh-hant': { prev: '‹ 上一頁', next: '下一頁 ›', of: '第 %n / %m 頁' },
    'zh':      { prev: '‹ 上一页', next: '下一页 ›', of: '第 %n / %m 页' },
    'en':      { prev: '‹ Previous', next: 'Next ›', of: 'Page %n of %m' },
    'fr':      { prev: '‹ Précédent', next: 'Suivant ›', of: 'Page %n sur %m' },
    'es':      { prev: '‹ Anterior', next: 'Siguiente ›', of: 'Página %n de %m' },
    'ja':      { prev: '‹ 前へ', next: '次へ ›', of: '%n / %m ページ' },
    'ko':      { prev: '‹ 이전', next: '다음 ›', of: '%n / %m 페이지' }
  };
  var lang = (document.documentElement.getAttribute('lang') || 'zh-Hant').toLowerCase();
  var T = L[lang] || L['zh-hant'];

  /* ---------- 样式（只注入一次，保证 6 个语言页表现一致） ---------- */
  if (!document.getElementById('faqPagerCss')) {
    var st = document.createElement('style');
    st.id = 'faqPagerCss';
    st.textContent = [
      '.faq-pager{display:flex;flex-wrap:wrap;align-items:center;justify-content:center;gap:8px;margin:44px 0 8px}',
      '.faq-pager button{font:inherit;font-size:14px;line-height:1;padding:11px 15px;border:1px solid var(--line);background:var(--white);color:var(--ink);border-radius:10px;cursor:pointer;transition:all .18s}',
      '.faq-pager button:hover:not(:disabled){border-color:var(--amber);color:var(--amber)}',
      '.faq-pager button[aria-current="page"]{background:var(--amber);border-color:var(--amber);color:#fff;font-weight:700}',
      '.faq-pager button:disabled{opacity:.35;cursor:not-allowed}',
      '.faq-pager .dots{padding:0 4px;color:var(--text-muted);font-size:14px}',
      '.faq-pager-info{text-align:center;font-size:13px;color:var(--text-muted);margin-top:10px}',
      '@media(max-width:560px){.faq-pager{gap:6px}.faq-pager button{padding:10px 12px;font-size:13px}}'
    ].join('');
    document.head.appendChild(st);
  }

  /* ---------- 翻页 ---------- */
  function show(n, scroll) {
    n = Math.min(Math.max(1, n), pages);
    var from = (n - 1) * PER, to = from + PER;
    cards.forEach(function (c, i) {
      c.style.display = (i >= from && i < to) ? '' : 'none';
    });
    render(n);
    if (scroll !== false) {
      var top = grid.getBoundingClientRect().top + window.pageYOffset - 90;
      window.scrollTo({ top: top < 0 ? 0 : top, behavior: 'smooth' });
    }
    var u = new URL(location.href);
    if (n === 1) u.searchParams.delete('page'); else u.searchParams.set('page', n);
    try { history.replaceState(null, '', u.toString()); } catch (e) {}
  }

  var nav = document.createElement('nav');
  nav.className = 'faq-pager';
  nav.setAttribute('aria-label', 'Pagination');
  var info = document.createElement('p');
  info.className = 'faq-pager-info';
  grid.parentNode.insertBefore(nav, grid.nextSibling);
  grid.parentNode.insertBefore(info, nav.nextSibling);

  function btn(label, page, aria, isCurrent) {
    var b = document.createElement('button');
    b.type = 'button';
    b.textContent = label;
    if (isCurrent) b.setAttribute('aria-current', 'page');
    if (aria) b.setAttribute('aria-label', aria);
    b.addEventListener('click', function () { show(page); });
    return b;
  }

  function render(cur) {
    nav.innerHTML = '';
    var prev = btn(T.prev, cur - 1, 'Previous page');
    prev.disabled = cur === 1;
    nav.appendChild(prev);

    /* 窗口化页码：1 … cur-1 cur cur+1 … last */
    var list = [];
    for (var i = 1; i <= pages; i++) {
      if (i === 1 || i === pages || Math.abs(i - cur) <= 1) list.push(i);
    }
    var prevN = 0;
    list.forEach(function (n) {
      if (prevN && n - prevN > 1) {
        var d = document.createElement('span');
        d.className = 'dots';
        d.textContent = '…';
        nav.appendChild(d);
      }
      nav.appendChild(btn(String(n), n, 'Page ' + n, n === cur));
      prevN = n;
    });

    var next = btn(T.next, cur + 1, 'Next page');
    next.disabled = cur === pages;
    nav.appendChild(next);

    info.textContent = T.of.replace('%n', cur).replace('%m', pages);
  }

  var start = parseInt((new URL(location.href)).searchParams.get('page') || '1', 10) || 1;
  show(start, false);
})();
