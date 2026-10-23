import csv,collections,sys
rows=list(csv.DictReader(open(sys.argv[1],encoding='latin-1')))
ex=[r for r in rows if r['Activity']=='Exports' and r['TransportName']=='Marine']
print('latest period', max((r['Year'],r['Period']) for r in rows))
for yr in ('2025','2026'):
    sel=[r for r in ex if r['Year']==yr]
    vol=collections.defaultdict(float); n=collections.Counter()
    for r in sel:
        vol[r['ToCountryName']]+=float(r['Volume']); n[r['ToCountryName']]+=1
    tot=sum(vol.values())
    print(f'== {yr} marine LNG exports: cargo records {len(sel)}, volume {tot:,.0f} 10^3 m3 gas equivalent ({tot*35.3147/1e6:,.1f} Bcf)')
    for k,v in sorted(vol.items(),key=lambda x:-x[1]):
        print(f'   {k:30s} {v:14,.0f}  {100*v/tot:5.1f}%  records {n[k]}')
    print('  terminals',collections.Counter(r['Terminal'] for r in sel))
    print('  months',sorted(set(r['Period'] for r in sel))[:1],sorted(set(r['Period'] for r in sel))[-1:])
print('any Turkiye rows:',[r for r in rows if 'urk' in r['ToCountryName'] or 'ürk' in r['ToCountryName']][:3])
print('first LNG Canada marine export:',min((r['Period'],r['Vessel'],r['ToCountryName']) for r in ex if 'Kitimat' in r['Terminal'] or 'LNG Canada' in r['CompanyName']) if any('Kitimat' in r['Terminal'] or 'LNG Canada' in r['CompanyName'] for r in ex) else None)
print('non-marine export transport', collections.Counter(r['TransportName'] for r in rows if r['Activity']=='Exports'))
