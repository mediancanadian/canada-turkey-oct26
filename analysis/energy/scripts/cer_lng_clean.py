"""Summarise CER LNG export shipment detail, excluding records > 200,000 10^3 m3 (single cargo physically ~100,000)."""
import csv,collections,sys
rows=list(csv.DictReader(open(sys.argv[1],encoding='latin-1')))
ex=[r for r in rows if r['Activity']=='Exports' and r['TransportName']=='Marine']
bad=[r for r in ex if float(r['Volume'])>200000]
print('EXCLUDED anomalous records:',[(r['Period'],r['Vessel'],r['ToCountryName'],r['Volume']) for r in bad])
ex=[r for r in ex if float(r['Volume'])<=200000]
for label,f in [('2025 all',lambda r:r['Year']=='2025'),('2026 Jan-Jul',lambda r:r['Year']=='2026' and int(r['Period'][:2])<=7),('2026 Jan-Aug (clean)',lambda r:r['Year']=='2026'),('Jun 2025-Aug 2026 (clean)',lambda r:(r['Year']=='2025' and int(r['Period'][:2])>=6) or r['Year']=='2026')]:
    sel=[r for r in ex if f(r)]
    vol=collections.defaultdict(float); n=collections.Counter()
    for r in sel: vol[r['ToCountryName']]+=float(r['Volume']); n[r['ToCountryName']]+=1
    tot=sum(vol.values())
    print(f'== {label}: records {len(sel)}, {tot:,.0f} thousand m3 gas equiv = {tot/1e6:,.2f} bcm = {tot*35.3147/1e6:,.1f} Bcf; approx {tot/1e6/1.36:,.1f} Mt LNG (1 Mt LNG ~ 1.36 bcm)')
    for k,v in sorted(vol.items(),key=lambda x:-x[1]): print(f'   {k:28s} {v:13,.0f} {100*v/tot:5.1f}%  cargoes/records {n[k]}')
kit=[r for r in ex if 'Kitimat' in r['Terminal']]
print('first Kitimat export record period:',min(r['Period'][6:]+r['Period'][:2] for r in kit))
print('Kitimat records by period:',sorted(collections.Counter(r['Period'][6:]+'-'+r['Period'][:2] for r in kit).items()))
