"""2025 imports from Türkiye (StatCan HS10) falling in (a) Schedule 1 steel TRQ classes of SOR/2025-148 as amended (current to 2026-09-30)
and (b) tariff classification numbers listed for SIMA measures in force naming Türkiye (CBSA MIF pages, accessed 2026-10-23).
2025 trade is used as a proxy for the coverage in 2026; class/line lists are the 2026 versions."""
import re, pandas as pd
B='../tariffs/'
L=[re.sub(r'[\u2009\u00a0\u202f]',' ',l).strip() for l in open(B+'raw/official/sor2025-148.txt')]
s=[i for i,l in enumerate(L) if l.startswith('SCHEDULE 1')][-1]; e=[i for i,l in enumerate(L) if l.startswith('SCHEDULE 2')][-1]
cls=None; m={}
for l in L[s:e]:
    a=re.match(r'^(\d+)\s+([A-Za-z][A-Za-z ,\-]*[A-Za-z])\s+[\d ]+(?:\.\d+)?\s+\d+%',l)
    if a: cls=a.group(2).strip()
    for c in re.findall(r'\d{4}\.\d{2}\.\d{2}\.\d{2}',l):
        m[c.replace('.','')]=cls
imp=pd.read_csv(B+'outputs/imports_from_TR_2025_hs10.csv',dtype={'hs10':str})
imp['trq_class']=imp.hs10.map(m)
t=imp[imp.trq_class.notna()]
print('TRQ classes parsed',len(set(m.values())),'lines',len(m))
g=t.groupby('trq_class').val.sum().sort_values(ascending=False); print(g); print('TOTAL TRQ-covered 2025 imports from TR',t.val.sum())
g.to_csv(B+'outputs/tr_imports_2025_in_steel_trq_classes.csv')
# SIMA
sima={}
for code in ['cswp3','rb1','cor2','dwp','hss','octg2','octg5','ss','sw']:
    txt=open(B+f'raw/official/sima/{code}.txt').read()
    for c in re.findall(r'\d{4}\.\d{2}\.\d{2}\.\d{2}',txt): sima.setdefault(c.replace('.',''),set()).add(code.upper())
imp['sima']=imp.hs10.map(lambda x: ','.join(sorted(sima[x])) if x in sima else None)
u=imp[imp.sima.notna()]
print(u.groupby('sima').val.sum().sort_values(ascending=False)); print('TOTAL in SIMA-listed lines',u.val.sum())
u.groupby('sima').val.sum().to_csv(B+'outputs/tr_imports_2025_in_sima_listed_lines.csv')
