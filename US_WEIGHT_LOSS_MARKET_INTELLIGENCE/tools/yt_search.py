#!/usr/bin/env python3
"""YouTube public search scraper (US, English). Reads the public results page and parses ytInitialData.
Usage: python3 -I yt_search.py "query" [filter] [max]
filter: any | week | month | year | views_week | views_month | views_year | date (newest) | views
Outputs JSON lines: videoId,title,channel,views,views_num,published,length,url,badges,snippet
"""
import sys, re, json, urllib.request, urllib.parse, time
FILTERS={"any":"", "week":"EgIIAw%253D%253D","month":"EgIIBA%253D%253D","year":"EgIIBQ%253D%253D",
 "views_week":"CAMSBAgDEAE%253D","views_month":"CAMSBAgEEAE%253D","views_year":"CAMSBAgFEAE%253D","date":"CAI%253D","views":"CAM%253D"}
q=sys.argv[1]; f=sys.argv[2] if len(sys.argv)>2 else "any"; mx=int(sys.argv[3]) if len(sys.argv)>3 else 20
sp=FILTERS.get(f,f)
url="https://www.youtube.com/results?search_query="+urllib.parse.quote_plus(q)+("&sp="+sp if sp else "")+"&hl=en&gl=US"
req=urllib.request.Request(url,headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64)","Accept-Language":"en-US,en;q=0.9","Cookie":"CONSENT=YES+1"})
h=urllib.request.urlopen(req,timeout=40).read().decode("utf-8","ignore")
m=re.search(r'var ytInitialData = (\{.*?\});</script>',h,re.S)
if not m: print(json.dumps({"error":"no ytInitialData","url":url})); sys.exit(1)
d=json.loads(m.group(1))
def walk(o):
    if isinstance(o,dict):
        if 'videoRenderer' in o: yield o['videoRenderer']
        for v in o.values(): yield from walk(v)
    elif isinstance(o,list):
        for v in o: yield from walk(v)
def num(s):
    if not s: return None
    s=s.replace(',','').lower(); m=re.search(r'([\d\.]+)\s*([km]?)',s)
    if not m: return None
    v=float(m.group(1)); return int(v*{'k':1e3,'m':1e6}.get(m.group(2),1))
seen=set(); out=0
for v in walk(d):
    vid=v.get('videoId')
    if not vid or vid in seen: continue
    seen.add(vid)
    t=''.join(r.get('text','') for r in v.get('title',{}).get('runs',[]))
    views=v.get('viewCountText',{}).get('simpleText') or ''.join(r.get('text','') for r in v.get('viewCountText',{}).get('runs',[]))
    snip=''.join(r.get('text','') for s in v.get('detailedMetadataSnippets',[]) for r in s.get('snippetText',{}).get('runs',[]))
    badges=[b.get('metadataBadgeRenderer',{}).get('label') for b in v.get('badges',[])]
    rec={"videoId":vid,"title":t,"channel":v.get('ownerText',{}).get('runs',[{}])[0].get('text'),
         "views":views,"views_num":num(views),"published":v.get('publishedTimeText',{}).get('simpleText'),
         "length":v.get('lengthText',{}).get('simpleText'),"url":"https://www.youtube.com/watch?v="+vid,
         "badges":[b for b in badges if b],"snippet":snip[:300],"query":q,"filter":f,"collected":time.strftime("%Y-%m-%d")}
    print(json.dumps(rec,ensure_ascii=False)); out+=1
    if out>=mx: break
