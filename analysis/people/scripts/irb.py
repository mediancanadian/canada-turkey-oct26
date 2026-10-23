import pandas as pd,io,json,re
O='../people/'
out={}
for y in range(2015,2027):
    html=open(O+f'raw/irb/rpd_{y}.html',encoding='utf-8',errors='ignore').read()
    try: tabs=pd.read_html(io.StringIO(html))
    except Exception as e: print(y,'ERR',e); continue
    for t in tabs:
        t.columns=[' '.join(map(str,c)) if isinstance(c,tuple) else str(c) for c in t.columns]
        m=t[t.iloc[:,0].astype(str).str.contains('Turk|Türk',regex=True)]
        if len(m):
            out[y]={'columns':list(t.columns),'row':m.astype(str).values.tolist()}
            tot=t[t.iloc[:,0].astype(str).str.contains('Total',case=False)]
            out[y]['total']=tot.astype(str).values.tolist()
            break
    title=re.search(r'<title>(.*?)</title>',html,re.S)
    print(y, out.get(y,{}).get('columns'), out.get(y,{}).get('row'), out.get(y,{}).get('total'))
json.dump(out,open(O+'outputs/irb_turkiye.json','w'),indent=1,ensure_ascii=False)
