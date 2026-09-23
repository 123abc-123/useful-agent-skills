// Local browser regression for task routing, quality gates and install interactions.
const {chromium} = require(process.env.PLAYWRIGHT_MODULE || 'playwright');
const fs = require('node:fs');
const path = require('node:path');
const os = require('node:os');
const http = require('node:http');
const assert = require('node:assert/strict');
const root = path.resolve(__dirname, '../..');
const out = fs.mkdtempSync(path.join(os.tmpdir(), 'skill-discovery-'));
fs.cpSync(path.join(root,'site'), out, {recursive:true});
fs.copyFileSync(path.join(root,'content/data/recommended-skills.json'),path.join(out,'skills.json'));
fs.copyFileSync(path.join(root,'content/data/prompts.json'),path.join(out,'prompts.json'));
fs.cpSync(path.join(root,'content/data/tools'),path.join(out,'data/tools'),{recursive:true});
fs.cpSync(path.join(root,'content/prompts'),path.join(out,'prompts'),{recursive:true});
const types={'.html':'text/html; charset=utf-8','.js':'text/javascript; charset=utf-8','.css':'text/css; charset=utf-8','.json':'application/json; charset=utf-8','.md':'text/plain; charset=utf-8'};
const server=http.createServer((req,res)=>{
  const pathname=decodeURIComponent(new URL(req.url,'http://localhost').pathname);
  let file=path.resolve(out, '.'+pathname);
  if(!file.startsWith(out+path.sep)&&file!==out){res.writeHead(403);return res.end();}
  if(fs.existsSync(file)&&fs.statSync(file).isDirectory())file=path.join(file,'index.html');
  if(!fs.existsSync(file)){res.writeHead(404);return res.end();}
  res.setHeader('Content-Type',types[path.extname(file)]||'application/octet-stream');
  res.end(fs.readFileSync(file));
});
(async()=>{
  await new Promise(resolve=>server.listen(0,'127.0.0.1',resolve));
  const base=`http://127.0.0.1:${server.address().port}`;
  const browser=await chromium.launch({channel:'msedge',headless:true});
  try{
    const context=await browser.newContext({viewport:{width:1440,height:1000},permissions:['clipboard-read','clipboard-write']});
    const page=await context.newPage();
    const errors=[];
    page.on('pageerror',e=>errors.push(e.message));
    page.on('response',r=>{if(r.url().startsWith(base)&&r.status()>=400)errors.push(`${r.status()} ${r.url()}`);});
    await page.goto(base);
    await page.waitForSelector('.group-card');
    assert.equal(await page.locator('.must-banner').count(),1);
    assert.equal(await page.locator('.group-card').count(),6);
    assert.equal(await page.locator('.shortcut').count(),20);
    await page.screenshot({path:path.join(out,'home-desktop.png'),fullPage:true});
    const search=page.locator('#need-search');
    for(const [query,expected] of [['修 Bug','debug'],['RAG 回答不好','rag'],['生成 HTML 报告','report'],['上下文','understand'],['systematic-debugging','debug']]){
      await search.fill(query);
      assert.ok((await page.locator('.search-result').first().getAttribute('href')).includes(`task=${expected}`),query);
    }
    await search.fill('zzzx-no-match');
    assert.ok((await page.locator('#search-results').innerText()).includes('暂时没有'));
    await search.fill('修 Bug');
    await page.locator('.search-result').first().click();
    await page.waitForSelector('.recommendation');
    assert.ok(page.url().includes('task=debug'));
    const config=JSON.parse(await page.locator('#discovery-data').textContent());
    let tasks=0;
    for(const group of config.groups){
      for(const task of group.tasks){
        await page.goto(`${base}/${group.page}?task=${task.id}`);
        await page.waitForFunction(()=>document.querySelector('#task-title').textContent.length>0);
        assert.equal(await page.locator('#task-title').textContent(),task.title);
        const qualified=task.picks.filter(x=>x.qualified);
        assert.equal(await page.locator('.recommendation').count(),Math.min(3,qualified.length));
        for(const p of qualified){assert.ok(p.score>=85&&p.stars>=1000&&p.status==='recommended'&&!p.archived);}
        await page.locator('[data-mode="all"]').click();
        assert.equal(await page.locator('.recommendation').count(),Math.min(3,task.picks.length));
        await page.locator('#sort').selectOption('stars');
        const sorted=[...task.picks].sort((a,b)=>b.stars-a.stars||b.score-a.score);
        assert.equal(await page.locator('.recommendation h3').first().textContent(),sorted[0].name);
        tasks++;
      }
    }
    await page.goto(`${base}/tools/coding-agent-upgrades/?task=debug`);
    await page.waitForSelector('.recommendation');
    assert.equal(await page.locator('.scenario-switcher').getAttribute('open'),null);
    const firstPickBox=await page.locator('.recommendation').first().boundingBox();
    const switcherBox=await page.locator('.scenario-switcher').boundingBox();
    assert.ok(firstPickBox.y<switcherBox.y,'first recommendation must appear before scenario switcher');
    assert.ok((await page.locator('.recommendation.primary .rec-tag').textContent()).includes('先试这个'));
    await page.locator('.install summary').first().click();
    const command=await page.locator('.copy').first().getAttribute('data-copy');
    await page.locator('.copy').first().click();
    await page.waitForFunction(()=>document.querySelector('.copy-status').textContent==='已复制');
    assert.equal(await page.evaluate(()=>navigator.clipboard.readText()),command);
    await page.locator('.scenario-switcher summary').click();
    await page.locator('[data-task="review"]').click();
    assert.ok(page.url().includes('task=review'));
    await page.goBack();
    assert.equal(await page.locator('#task-title').textContent(),'修 Bug，总在反复猜');
    await page.screenshot({path:path.join(out,'coding-desktop.png'),fullPage:true});
    await page.setViewportSize({width:390,height:844});
    for(const route of ['/', '/tools/', '/must-have-skills/', '/prompts.html',...config.groups.map(g=>'/'+g.page)]){
      await page.goto(base+route);
      await page.waitForTimeout(80);
      assert.ok(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth),`mobile overflow: ${route}`);
    }
    await page.goto(`${base}/tools/coding-agent-upgrades/?task=debug`);
    await page.waitForSelector('.recommendation');
    await page.screenshot({path:path.join(out,'coding-mobile.png'),fullPage:true});
    await page.goto(`${base}/tools/html-reports/?task=report`);
    await page.waitForSelector('.empty');
    await page.locator('#show-candidates').click();
    assert.ok(await page.locator('.recommendation').count()>0);
    await page.locator('.install summary').first().click();
    await page.evaluate(()=>{Object.defineProperty(navigator,'clipboard',{value:{writeText:async()=>{throw new Error('denied');}},configurable:true});});
    await page.locator('.copy').first().click();
    await page.waitForFunction(()=>document.querySelector('.copy-status').textContent.includes('请复制上方命令'));
    await page.goto(`${base}/must-have-skills/`);
    await page.waitForSelector('.must-card');
    assert.equal(await page.locator('#core .must-card').count(),5);
    assert.equal(await page.locator('#role .must-card').count(),4);
    assert.equal(await page.locator('.signal-card').count(),3);
    await page.locator('[data-static-copy]').first().click();
    await page.waitForFunction(()=>document.querySelector('.must-card .copy-status').textContent==='已复制');
    await page.screenshot({path:path.join(out,'must-have-mobile.png'),fullPage:true});
    await page.goto(`${base}/prompts.html`);
    await page.waitForSelector('[data-path]');
    await page.locator('[data-path]').first().click();
    await page.waitForFunction(()=>document.querySelector('[data-path]').textContent==='已复制');
    assert.ok((await page.evaluate(()=>navigator.clipboard.readText())).includes('---'));
    assert.deepEqual(errors,[]);
    console.log(JSON.stringify({result:'passed',tasks,checks:'desktop, 390px, search routing, deep links, history, quality gates, star sorting, clipboard success/failure, Prompt copy, zero page errors',screenshots:out},null,2));
  }finally{await browser.close();}
})().catch(e=>{console.error(e);process.exitCode=1;}).finally(()=>server.close());
