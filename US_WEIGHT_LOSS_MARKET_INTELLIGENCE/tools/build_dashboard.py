#!/usr/bin/env python3
"""Builds EXECUTIVE_DASHBOARD.html from the CSVs in data/. Run from the project folder: python3 -I tools/build_dashboard.py"""
import csv, json, os, html
D='data'
def load(name):
    p=os.path.join(D,name)
    if not os.path.exists(p): return []
    with open(p,newline='',encoding='utf-8') as f: return list(csv.DictReader(f))
data={
 'sources':load('SOURCES_DATABASE.csv'),'language':load('CUSTOMER_LANGUAGE.csv'),'videos':load('VIDEO_FORMATS.csv'),
 'ingredients':load('INGREDIENT_TRENDS.csv'),'hosts':load('HOSTS_EXPERTS.csv'),'competitors':load('COMPETITORS.csv'),'ranking':load('OPPORTUNITY_RANKING.csv')}
counts={k:len(v) for k,v in data.items()}
page=f"""<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Weight Loss Intel Dashboard</title>
<style>
:root{{--bg:#0f1115;--card:#171a21;--ink:#e8eaf0;--mut:#9aa3b2;--acc:#f2b705;--acc2:#4fc3f7;--line:#262b36}}
*{{box-sizing:border-box}}body{{margin:0;font:14px/1.45 system-ui,Segoe UI,Roboto,sans-serif;background:var(--bg);color:var(--ink);padding:16px}}
h1{{font-size:20px;margin:0 0 4px}}h2{{font-size:16px;margin:18px 0 8px;color:var(--acc)}}.sub{{color:var(--mut);margin-bottom:12px}}
.tabs{{display:flex;flex-wrap:wrap;gap:6px;margin:12px 0}}.tabs button{{background:var(--card);color:var(--ink);border:1px solid var(--line);padding:8px 12px;border-radius:8px;cursor:pointer}}.tabs button.on{{border-color:var(--acc);color:var(--acc)}}
.bar{{display:flex;flex-wrap:wrap;gap:8px;margin:8px 0}}input,select{{background:var(--card);color:var(--ink);border:1px solid var(--line);padding:7px 9px;border-radius:6px;min-width:160px}}
table{{width:100%;border-collapse:collapse;font-size:13px}}th,td{{border-bottom:1px solid var(--line);padding:6px 8px;text-align:left;vertical-align:top}}th{{color:var(--mut);cursor:pointer;position:sticky;top:0;background:var(--bg)}}
td{{max-width:420px;overflow-wrap:anywhere}}a{{color:var(--acc2)}}.kpi{{display:flex;flex-wrap:wrap;gap:8px}}.kpi div{{background:var(--card);border:1px solid var(--line);border-radius:8px;padding:10px 14px}}.kpi b{{font-size:20px;display:block;color:var(--acc)}}
.wrap{{overflow:auto;max-height:70vh;border:1px solid var(--line);border-radius:8px}}.n{{color:var(--mut)}}
.scorebar{{height:6px;background:var(--line);border-radius:3px}}.scorebar i{{display:block;height:6px;background:var(--acc);border-radius:3px}}
@media(max-width:600px){{td{{max-width:220px}}input,select{{min-width:120px}}}}
</style></head><body>
<h1>US Weight Loss Market Intelligence — Dashboard</h1>
<div class="sub">Mulheres americanas 40–75 · coleta 19/11/2026 · fontes com link original · filtros por aba. Os relatórios .md são a fonte completa; este painel é navegação.</div>
<div class="kpi">{''.join(f'<div><b>{v}</b>{k}</div>' for k,v in counts.items())}</div>
<div class="tabs" id="tabs"></div>
<div class="bar"><input id="q" placeholder="buscar texto…"><select id="f1"></select><select id="f2"></select><span class="n" id="cnt"></span></div>
<div class="wrap"><table id="t"><thead></thead><tbody></tbody></table></div>
<script>
const DATA={json.dumps(data,ensure_ascii=False)};
const TABS=[['ranking','Ranking de oportunidades',['type','status']],['ingredients','Ingredientes',['trend_status','saturation']],['videos','Vídeos & formatos',['format_type','platform']],['hosts','Hosts & experts',['category','archetype']],['competitors','Concorrência',['format','validation_level']],['language','Customer language',['category','platform']],['sources','Fontes',['frente','platform']]];
let cur='ranking',sortK=null,sortD=1;
const $=s=>document.querySelector(s);
function fill(sel,rows,key,label){{const vals=[...new Set(rows.map(r=>r[key]||'').filter(Boolean))].sort();sel.innerHTML=`<option value="">${{label}}: todos</option>`+vals.map(v=>`<option>${{v}}</option>`).join('');sel.dataset.key=key}}
function render(){{const rows0=DATA[cur]||[];const tab=TABS.find(t=>t[0]==cur);
 const q=$('#q').value.toLowerCase(),a=$('#f1'),b=$('#f2');
 let rows=rows0.filter(r=>(!q||Object.values(r).join(' ').toLowerCase().includes(q))&&(!a.value||r[a.dataset.key]==a.value)&&(!b.value||r[b.dataset.key]==b.value));
 if(sortK)rows=rows.slice().sort((x,y)=>{{const u=parseFloat(x[sortK]),v=parseFloat(y[sortK]);if(!isNaN(u)&&!isNaN(v))return (u-v)*sortD;return String(x[sortK]||'').localeCompare(String(y[sortK]||''))*sortD}});
 const cols=rows0.length?Object.keys(rows0[0]):[];
 $('#t thead').innerHTML='<tr>'+cols.map(c=>`<th data-k="${{c}}">${{c}}</th>`).join('')+'</tr>';
 $('#t tbody').innerHTML=rows.map(r=>'<tr>'+cols.map(c=>{{let v=r[c]||'';if(/^https?:\\/\\//.test(v))v=v.split(/[;\\s]+/).filter(Boolean).map(u=>`<a href="${{u}}" target="_blank" rel="noopener">${{u.replace(/^https?:\\/\\/(www\\.)?/,'').slice(0,40)}}</a>`).join('<br>');else v=v.replace(/[&<>]/g,m=>({{'&':'&amp;','<':'&lt;','>':'&gt;'}}[m]));if(/score/.test(c)&&!isNaN(parseFloat(r[c]))&&parseFloat(r[c])<=100)v+=`<div class="scorebar"><i style="width:${{r[c]}}%"></i></div>`;return `<td>${{v}}</td>`}}).join('')+'</tr>').join('');
 $('#cnt').textContent=rows.length+' / '+rows0.length+' linhas';
 document.querySelectorAll('#t th').forEach(th=>th.onclick=()=>{{sortD=sortK==th.dataset.k?-sortD:1;sortK=th.dataset.k;render()}})}}
function go(k){{cur=k;sortK=null;const tab=TABS.find(t=>t[0]==k);document.querySelectorAll('#tabs button').forEach(b=>b.classList.toggle('on',b.dataset.k==k));fill($('#f1'),DATA[k]||[],tab[2][0],tab[2][0]);fill($('#f2'),DATA[k]||[],tab[2][1],tab[2][1]);$('#q').value='';render()}}
$('#tabs').innerHTML=TABS.map(t=>`<button data-k="${{t[0]}}">${{t[1]}} (${{(DATA[t[0]]||[]).length}})</button>`).join('');
document.querySelectorAll('#tabs button').forEach(b=>b.onclick=()=>go(b.dataset.k));['#q','#f1','#f2'].forEach(s=>$(s).oninput=render);go('ranking');
</script></body></html>"""
open('EXECUTIVE_DASHBOARD.html','w',encoding='utf-8').write(page)
print('dashboard written', counts)
