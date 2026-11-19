#!/usr/bin/env python3
"""Merge data/F*_sources.csv into data/SOURCES_DATABASE.csv, dedupe by URL (keep first), validate schema."""
import csv, glob, os, re
COLS="id,url,platform,title,author,date_published,date_collected,metrics,excerpt,category,audience_segment,confidence,limitations,frente".split(',')
rows=[]; seen=set(); bad=0; per={}
for f in sorted(glob.glob('data/F*_sources.csv')):
    with open(f,newline='',encoding='utf-8') as fh:
        r=csv.DictReader(fh)
        for row in r:
            if set(COLS)-set(row.keys()): bad+=1; continue
            u=(row.get('url') or '').strip().rstrip('/')
            key=re.sub(r'^https?://(www\.)?','',u).lower()
            if not key or key in seen: continue
            seen.add(key); rows.append({c:(row.get(c) or '').replace('\n',' ').strip() for c in COLS}); per[row['frente']]=per.get(row['frente'],0)+1
with open('data/SOURCES_DATABASE.csv','w',newline='',encoding='utf-8') as fh:
    w=csv.DictWriter(fh,fieldnames=COLS); w.writeheader(); w.writerows(rows)
print('unique sources:',len(rows),'per frente:',per,'schema-bad rows:',bad)
