# Parse "Table 6" (exports by destination, non-US) from an extracted report text; print Türkiye value and rank.
import re,sys,json
out={}
for f in sys.argv[1:]:
    t=open(f).read()
    idx=[m.start() for m in re.finditer(r'Table 6:',t)]
    i=idx[-1]; j=t.find('Table 7',i)
    seg=t[i:j]
    rows=[]
    for line in seg.split('\n'):
        m=re.match(r'\s*(.+?)\s+\$\s?([\d,\.]+)\s*$',line)
        if m:
            name=m.group(1).strip(); v=m.group(2).replace(',','')
            v=re.sub(r'\.(?=.*\.)','',v)  # fix stray separators
            try: rows.append((name,float(v.rstrip('.'))))
            except: pass
    rows=[r for r in rows if not r[0].lower().startswith('total')]
    rows.sort(key=lambda r:-r[1])
    tk=[k for k,r in enumerate(rows) if 'rkiye' in r[0] or 'Turkey' in r[0]]
    res={'n_destinations':len(rows),'total':sum(r[1] for r in rows)}
    if tk: res.update(turkiye_value=rows[tk[0]][1],turkiye_rank=tk[0]+1)
    out[f]=res; print(f,res)
json.dump(out,open(sys.argv[1].rsplit('/',3)[0]+'/../outputs/table6_ranks.json' if False else '../defence/outputs/table6_ranks.json','w'),indent=1)
