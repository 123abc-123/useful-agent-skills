/* Task routing is explicit keyword matching, not an LLM recommendation claim. */
(() => {
  const data = JSON.parse(document.querySelector('#discovery-data').textContent);
  const group = data.groups.find(g => g.id === data.current_group);
  const query = document.querySelector('#need-search');
  const searchResults = document.querySelector('#search-results');
  const escape = value => String(value).replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
  const number = value => value.toLocaleString('en-US');
  const tokens = value => (value.toLowerCase().match(/[a-z0-9]+|[\u4e00-\u9fff]+/g) || []).filter(x => /[\u4e00-\u9fff]/.test(x) || x.length >= 3);
  let selected;
  let mode = 'quality';
  const allTasks = data.groups.flatMap(g => g.tasks.map(t => ({g, t})));

  function search() {
    const text = query.value.trim().toLowerCase();
    searchResults.hidden = !text;
    if (!text) return;
    const found = allTasks.map(({g,t}) => {
      const names = t.picks.map(p => `${p.name} ${p.source}`).join(' ').toLowerCase();
      const haystack = `${t.title} ${t.description} ${t.keywords.join(' ')} ${names}`.toLowerCase();
      const score = t.keywords.reduce((n,k) => n + (text.includes(k.toLowerCase()) ? 3 : 0), 0)
        + tokens(text).reduce((n,k) => n + (haystack.includes(k) ? 2 : 0), 0)
        + (names.includes(text) ? 5 : 0);
      return {g,t,score};
    }).filter(x => x.score > 0).sort((a,b) => b.score-a.score).slice(0,6);
    searchResults.innerHTML = found.length ? '<span class="muted">匹配到这些需求场景，点击查看推荐：</span>' + found.map(({g,t}) =>
      `<a class="search-result" href="${data.prefix}${g.page}?task=${t.id}#results"><strong>${escape(t.title)}</strong><span>${escape(g.title)} · ${escape(t.description)}</span></a>`).join('')
      : '<strong>暂时没有匹配到具体场景</strong><p class="muted">可以换成“修 Bug”“微调”“HTML 报告”等关键词，或从下面的需求组开始。</p>';
  }
  query?.addEventListener('input', search);
  document.querySelectorAll('[data-search]').forEach(button => button.addEventListener('click', () => {query.value=button.dataset.search; search(); query.focus();}));

  const runtime = x => x === 'passed' ? '实机通过' : x === 'failed' ? '实机失败' : x === 'needs-adaptation' ? '需适配' : '未实测';
  function card(p, index) {
    const status = p.status === 'recommended' ? '推荐候选' : p.status === 'trial' ? '小范围试用' : '需要适配';
    const badge = mode === 'quality' ? (index === 0 ? '先试这个' : '按需补充 / 备选') : status;
    const compatibility = p.compatibility || `按上游说明准备环境；${p.risk === 'high' ? '涉及高影响操作，需单独审查。' : '安装前检查脚本、依赖和项目权限。'}`;
    return `<article class="recommendation ${index === 0 ? 'primary' : 'secondary'}"><div class="rec-top"><span class="rec-tag">${index+1 < 10 ? '0' : ''}${index+1} / ${badge}</span><a class="repo" href="https://github.com/${escape(p.source)}">${escape(p.source)} ↗</a></div><h3>${escape(p.name)}</h3><p class="reason">${escape(p.reason)}</p><div class="metrics"><a class="metric" href="https://github.com/123abc-123/useful-agent-skills/blob/main/SCORING.md">编辑评分 <strong>${p.score}</strong>/100</a><a class="metric" title="GitHub API 采集于 ${escape(p.stars_checked)}；仓库总 Star，不是该 Skill 的安装量" href="https://github.com/${escape(p.source)}/stargazers">仓库 ★ <strong>${number(p.stars)}</strong></a><span class="runtime">Pi ${runtime(p.runtime_pi)} · OpenCode ${runtime(p.runtime_opencode)}</span></div><div class="actions"><a class="source-action" href="${escape(p.source_url)}">${p.pinning_status === 'verified' ? '查看已固定的 Skill 源码' : '查看 Skill 源码（版本待核验）'} ↗</a>${index === 0 ? `<button class="copy quick-copy" data-copy="${escape(p.install)}">复制安装命令</button><span class="copy-status" role="status"></span>` : ''}<span class="muted">${{low:'低',medium:'中',high:'高'}[p.risk]}风险${p.archived ? ' · 仓库已归档' : ''}</span></div><details class="install"><summary class="install-toggle">适配说明与安装命令</summary><p>${escape(compatibility)}</p><p>许可证：${escape(p.license)} · 内容核验：${escape(p.last_verified)} · Star 采集：${escape(p.stars_checked.slice(0,10))}</p><p>命令安装上游当前版本；上面的固定源码用于审查，不代表此命令锁定了该提交。</p><pre><code>${escape(p.install)}</code></pre><button class="copy" data-copy="${escape(p.install)}">复制安装命令</button><span class="copy-status" role="status"></span></details></article>`;
  }

  function render() {
    const task = group.tasks.find(t => t.id === selected);
    document.querySelector('#task-title').textContent = task.title;
    document.querySelector('#task-description').textContent = task.description;
    document.querySelectorAll('[data-task]').forEach(a => {
      a.classList.toggle('active', a.dataset.task === selected);
      if (a.dataset.task === selected) a.setAttribute('aria-current','true'); else a.removeAttribute('aria-current');
    });
    document.querySelectorAll('[data-mode]').forEach(b => b.setAttribute('aria-pressed', String(b.dataset.mode === mode)));
    let picks = task.picks.filter(p => mode === 'all' || p.qualified);
    const order = document.querySelector('#sort').value;
    if (order === 'score') picks.sort((a,b) => b.score-a.score || b.stars-a.stars);
    if (order === 'stars') picks.sort((a,b) => b.stars-a.stars || b.score-a.score);
    const count = picks.length;
    picks = picks.slice(0,3);
    document.querySelector('#result-meta').textContent = mode === 'quality'
      ? `当前条件：编辑评分 ≥ ${data.score_min} · 来源仓库 ≥ ${number(data.stars_min)} Star · 来源已核验的推荐项。匹配 ${count} 项。`
      : `这个场景共 ${count} 项候选；热度不足、试用及需适配项也会显示，均不代表已实机通过。`;
    const target = document.querySelector('#recommendations');
    target.innerHTML = count ? picks.map(card).join('') : '<div class="empty"><h3>这个需求暂时没有符合门槛的推荐</h3><p>现有候选可能热度不足，或仍需适配、试用。你可以查看它们的具体边界再决定。</p><button id="show-candidates">查看该需求的全部候选</button></div>';
    document.querySelector('#show-candidates')?.addEventListener('click', () => {mode='all'; updateUrl(); render();});
    target.querySelectorAll('[data-copy]').forEach(button => button.addEventListener('click', async () => {
      const notice = button.nextElementSibling;
      try {await navigator.clipboard.writeText(button.dataset.copy); notice.textContent='已复制';}
      catch {notice.textContent='浏览器未允许剪贴板访问，请复制上方命令。';}
    }));
  }

  function updateUrl(replace=false) {
    const url = new URL(location.href);
    url.searchParams.set('task', selected);
    if (mode === 'all') url.searchParams.set('mode','all'); else url.searchParams.delete('mode');
    url.hash = 'results';
    history[replace ? 'replaceState' : 'pushState']({}, '', url);
  }
  function restore() {
    const params = new URLSearchParams(location.search);
    selected = group.tasks.some(t => t.id === params.get('task')) ? params.get('task') : group.tasks[0].id;
    mode = params.get('mode') === 'all' ? 'all' : 'quality';
    render();
  }
  if (group) {
    document.querySelectorAll('[data-task]').forEach(a => a.addEventListener('click', event => {
      event.preventDefault(); selected=a.dataset.task; updateUrl(); render(); document.querySelector('.scenario-switcher').open=false; document.querySelector('#results').scrollIntoView({behavior:'smooth'});
    }));
    document.querySelectorAll('[data-mode]').forEach(b => b.addEventListener('click', () => {mode=b.dataset.mode; updateUrl(); render();}));
    document.querySelector('#sort').addEventListener('change', render);
    window.addEventListener('popstate', restore);
    restore();
  }
})();
