"""Parse Table 2 (exports by destination, two year columns) from SIPRI-hosted copies of GAC 2010-2011 and 2012-2013 reports."""
import re,json
D='../defence/raw/reports/'
out={}
for p,yrs in [('2010_2011',('2010','2011')),('2012_2013',('2012','2013'))]:
    t=open(D+f'sipri_canada_{p}.txt').read()
    i=t.find('Table 2'); i=t.find('Table 2',i+10) if t.find('Table 2',i+10)>0 and t.find('Table 2',i+10)<t.find('Table 3',i+10) else i
    # locate table 2 body: from first 'Table 2:' heading followed by rows, to 'Table 3'
    starts=[m.start() for m in re.finditer(r'Table 2',t)]
    best=[]
    for s in starts:
        e=t.find('Table 3',s+10); seg=t[s:e if e>0 else s+40000]
        rows=[]
        for line in seg.split('\n'):
            m=re.match(r'\s*([A-Z][A-Za-z\'’,\.\(\)\- &]+?)\s{2,}(\$?[\d,]+|-)\s+(\$?[\d,]+|-)\s*$',line)
            if m and not re.search(r'(?i)total|destination|HDI|NATO|AFCCL|countries|^(Africa|Americas|Asia|Europe|Middle East|Oceania)',m.group(1).strip()):
                f=lambda x:0.0 if x=='-' else float(x.replace('$','').replace(',',''))
                rows.append((m.group(1).strip(),f(m.group(2)),f(m.group(3))))
        dd={}
        for r in rows: dd.setdefault(r[0],r)
        rows=list(dd.values())
        if len(rows)>len(best): best=rows
    for k,y in enumerate(yrs):
        r=sorted([(n,v[k]) for n,*v in [(a,b,c) for a,b,c in best]],key=lambda x:-x[1])
        r=[x for x in r if x[1]>0]
        tk=[j for j,x in enumerate(r) if x[0]=='Turkey']
        out[y]={'n_destinations_parsed':len(r),'sum_parsed':sum(x[1] for x in r),'turkiye_value':r[tk[0]][1] if tk else None,'turkiye_rank':tk[0]+1 if tk else None,'top5':r[:5]}
        print(y,out[y])
json.dump(out,open('../defence/outputs/exports_2010_2013_parsed.json','w'),indent=1)
