"""HS2 chapter check and doubling math."""
import json, collections, math
R='../trade/raw/wds/'
for f in ['hs2_exports_tur.json','hs2_imports_tur.json']:
    d=json.load(open(R+f)); a=collections.defaultdict(float)
    for k,s in d.items():
        p=k.split('.')
        if p[0]!='1': continue
        for ym,v in s:
            if v is not None: a[(ym[:4],int(p[4]))]+=v/1e3
    t25=sum(v for (y,c),v in a.items() if y=='2025')
    top=sorted([(c,v) for (y,c),v in a.items() if y=='2025'],key=lambda x:-x[1])[:10]
    print(f,[(c,round(v,1),'%.1f%%'%(100*v/t25),round(a[('2024',c)],1)) for c,v in top])
base=4334.663; fx=1.3978
print('US$ base %.1f'%(base/fx))
for name,tgt in [('2x',2*base),('C10B',10000),('US10B',10000*fx),('US5B',5000*fx)]:
    m=tgt/base; print(name,round(tgt,0),'%.2fx'%m,'5y %.1f%%'%(100*(m**0.2-1)),'10y %.1f%%'%(100*(m**0.1-1)))
print('doubling years at 6.0%%: %.1f'%(math.log(2)/math.log(1.0598)))
print('Reuters C$4.34B in USD at 1.3978: %.2f'%(4.3347/fx))
