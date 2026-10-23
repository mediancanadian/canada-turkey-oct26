"""Recompute CER LNG exports by destination and check scale claims."""
import csv, collections
R='../energy/raw/cer/liquefied-natural-gas-exports-detail.csv'
agg=collections.defaultdict(float); big=[]
for r in csv.DictReader(open(R,encoding='latin-1')):
    if r['Activity']!='Exports': continue
    v=float(r['Volume'] or 0); y=r['Year']; m=int(r['Period'][:2])
    if v>5e6: big.append((r['Period'],r['Vessel'],r['ToCountryName'],v)); continue
    if y=='2025': agg[('2025',r['ToCountryName'])]+=v
    if y=='2026' and m<=8: agg[('2026',r['ToCountryName'])]+=v
print('excluded',big)
for y in ['2025','2026']:
    t=sum(v for (yy,c),v in agg.items() if yy==y)
    print(y,'total bcm %.2f'%(t/1e6),'Bcf %.1f'%(t/1e6*35.3147))
    for (yy,c),v in sorted(agg.items(),key=lambda x:-x[1]):
        if yy==y: print('   ',c,'%.2f'%(v/1e6),'%.0f%%'%(100*v/t))
print('2025 LNG vs TR imports 58.337: %.1f%%'%(100*3.114/58.337))
print('Ankara EPDK LNG share 17090.59/58336.57 = %.2f%%'%(100*17090.59/58336.57))
print('per cap ratio 16.6/6.83=%.2f ; 17/6.8=%.2f'%(16.6/6.83,17/6.8))
print('Canada per cap 685e6/41262329 = %.2f; TR 584.5e6/85518661=%.2f'%(685e6/41262329,584.5e6/85518661))
print('NDC 643 vs 584.5: +%.1f%% ; vs net 517.4: +%.1f%%'%(100*(643/584.5-1),100*(643/517.4-1)))
print('U3O8 14327*1.1792=%.0f'%(14327*842.08/714.09))
print('Energy share 62.47/365.5=%.1f%%'%(100*62.47/365.5))
print('Net imports (128437-12304)/165214=%.1f%%'%(100*(128437-12304)/165214))
