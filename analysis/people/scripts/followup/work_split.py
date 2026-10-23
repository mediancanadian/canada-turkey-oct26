import openpyxl,json
B='../people/raw/'
def row(f,name='Turkey',hdr_rows=None):
    rows=list(openpyxl.load_workbook(B+f,read_only=True).worksheets[0].iter_rows(values_only=True))
    return rows
def n(v):
    try: return int(str(v).replace(',',''))
    except: return None
out={}
# Dec 31 holders
for key,f in [('imp_all_dec31','ircc/imp_citz_dec31_all.xlsx'),('imp_workonly_dec31','followup/ircc/imp_citz_dec31_workonly.xlsx'),('tfwp_dec31','ircc/tfwp_citz_dec31.xlsx')]:
    rows=row(f); hdr=next(r for r in rows if r and r[0]=='Country of Citizenship')
    tr=next(r for r in rows if r and r[0]=='Turkey'); tot=next(r for r in rows if r and str(r[0]).startswith('Total'))
    out[key]={str(h):{'turkey':n(a),'all':n(b)} for h,a,b in zip(hdr[1:],tr[1:],tot[1:]) if h and str(h)>='2015'}
# effective-year files with quarterly layout: pick columns whose header row-2 says 'Total' for the year
for key,f in [('hc_effective','followup/ircc/hc_citz_effective.xlsx'),('imp_workonly_effective','ircc/imp_citz_effective.xlsx'),('tfwp_effective','ircc/tfwp_citz_effective.xlsx')]:
    rows=row(f); i=next(k for k,r in enumerate(rows) if r and r[0]=='Country of Citizenship')
    years=rows[i]; q=rows[i+1]; m=rows[i+2]
    tr=next(r for r in rows if r and r[0]=='Turkey'); tot=next(r for r in rows if r and str(r[0]).startswith('Total'))
    cur=None; res={}
    for j in range(1,len(years)):
        if years[j]: cur=str(years[j])
        lab=(m[j] or q[j] or '')
        if lab and 'Total' in str(lab) and not str(lab).startswith('Q'):
            res[cur]={'turkey':n(tr[j]),'all':n(tot[j])}
    out[key]=res
json.dump(out,open('../people/outputs/work_permit_split_turkey.json','w'),indent=1)
for k,v in out.items(): print(k,{y:v[y]['turkey'] for y in sorted(v) if y>='2019'})
# monthly IMP work-only and H&C, Türkiye, 2022-2025 (from xlsx)
mon={}
for key,f in [('hc','followup/ircc/hc_citz_effective.xlsx'),('imp_workonly','ircc/imp_citz_effective.xlsx')]:
    rows=row(f); i=next(k for k,r in enumerate(rows) if r and r[0]=='Country of Citizenship')
    years=rows[i]; m=rows[i+2]; tr=next(r for r in rows if r and r[0]=='Turkey'); cur=None; d={}
    for j in range(1,len(years)):
        if years[j]: cur=str(years[j])
        if m[j] and len(str(m[j]))==3 and 'Tot' not in str(m[j]) and cur in ('2022','2023','2024','2025'): d[f'{cur}-{m[j]}']=n(tr[j])
    mon[key]=d
out['monthly']=mon
json.dump(out,open('../people/outputs/work_permit_split_turkey.json','w'),indent=1)
for k,d in mon.items(): print(k,{x:v for x,v in d.items() if x[:4] in('2023','2024')})
