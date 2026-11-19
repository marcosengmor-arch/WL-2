#!/usr/bin/env python3
"""Google Trends collector (US) via pytrends, paced to avoid 429s.
Usage: python3 -I trends_collect.py terms.txt out_prefix
terms.txt: one term per line; groups of up to 5 are compared together (first term of file is the anchor and is included in every group for normalization).
Outputs: <out_prefix>_iot_3m.csv, <out_prefix>_iot_12m.csv (interest over time, anchored), <out_prefix>_related.jsonl (rising/top related queries per term), <out_prefix>_log.txt
"""
import sys, time, json, csv, random
from pytrends.request import TrendReq
terms=[l.strip() for l in open(sys.argv[1]) if l.strip() and not l.startswith('#')]
out=sys.argv[2]; anchor=terms[0]; rest=terms[1:]
log=open(out+'_log.txt','a')
def L(*a):
    s=' '.join(str(x) for x in a); print(s); log.write(s+'\n'); log.flush()
pt=TrendReq(hl='en-US', tz=300, timeout=(10,40), retries=0)
def call(fn, *a, **k):
    for attempt in range(5):
        try: return fn(*a, **k)
        except Exception as e:
            wait=20*(attempt+1)+random.uniform(0,10); L('  retry',attempt,type(e).__name__,str(e)[:80],'wait',int(wait)); time.sleep(wait)
    return None
def groups(lst,n=4):
    for i in range(0,len(lst),n): yield lst[i:i+n]
for tf,tag in [('today 3-m','3m'),('today 12-m','12m')]:
    rows={}; cols=[]
    for g in groups(rest):
        kw=[anchor]+g; L(tf,'payload',kw)
        if call(pt.build_payload, kw, geo='US', timeframe=tf) is None: continue
        df=call(pt.interest_over_time)
        if df is None or df.empty: L('  empty'); time.sleep(8); continue
        for c in kw:
            if c in df.columns and c not in cols: cols.append(c)
        for d,r in df.iterrows():
            rows.setdefault(str(d.date()),{}).update({c:int(r[c]) for c in kw if c in df.columns})
        time.sleep(random.uniform(7,12))
    with open(f'{out}_iot_{tag}.csv','w',newline='') as f:
        w=csv.writer(f); w.writerow(['date']+cols)
        for d in sorted(rows): w.writerow([d]+[rows[d].get(c,'') for c in cols])
    L('wrote',f'{out}_iot_{tag}.csv',len(rows),'rows',len(cols),'cols')
# related queries per term (3-m)
with open(out+'_related.jsonl','a') as f:
    for t in terms:
        L('related',t)
        if call(pt.build_payload, [t], geo='US', timeframe='today 3-m') is None: continue
        rq=call(pt.related_queries)
        if rq and t in rq:
            rec={'term':t,'timeframe':'today 3-m','geo':'US'}
            for k in ('rising','top'):
                d=rq[t].get(k)
                rec[k]=d.head(15).to_dict('records') if d is not None else []
            f.write(json.dumps(rec,ensure_ascii=False)+'\n'); f.flush()
        time.sleep(random.uniform(8,14))
L('done')
