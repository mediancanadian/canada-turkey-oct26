import json,sys,glob,os
d=sys.argv[1]
for y in (2022,2023,2024,2025):
    for pref,lab in (('ca_to_tr','Canada-reported exports to Turkiye'),('tr_from_ca','Turkiye-reported imports from Canada')):
        f=f'{d}/{pref}_{y}_sel.json'
        rows=json.load(open(f)).get('data') or []
        out=', '.join(f"{r['cmdCode']}: {r['primaryValue']/1e6:.2f}M USD ({(r.get('netWgt') or 0)/1000:,.0f} t)" for r in sorted(rows,key=lambda r:r['cmdCode']) if r.get('customsCode') in (None,'C00') and r.get('motCode') in (None,0) and r.get('partner2Code') in (None,0))
        print(y,lab,'|',out)
    t=json.load(open(f'{d}/ca_to_tr_{y}_total.json')).get('data') or []
    print(y,'Canada total & ch27 exports to TR:',[(r['cmdCode'],round(r['primaryValue']/1e6,1)) for r in t])
