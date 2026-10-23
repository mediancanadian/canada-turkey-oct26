"""Estimate Canadian customs duties on 2025 imports from Türkiye:
StatCan CIMT 2025 imports (HS10, customs basis, CAD) x CBSA Customs Tariff T2026-2 MFN rate for the 8-digit tariff item.
Ad valorem part applied to value; specific parts in cents/kg or $/kg applied to quantity when the StatCan UOM is KGM.
Does NOT include SIMA (AD/CVD) duties, steel surtaxes, duty relief, drawback, Chapter 98/99 concessions or remissions."""
import pandas as pd, re
B='../tariffs/'
imp=pd.read_csv(B+'raw/statcan/CIMT-CICM_Imp_2025/ODPFN014_202512N.csv',dtype=str,usecols=[0,1,2,5,6,7])
imp.columns=['ym','hs10','cty','val','qty','uom']
t=imp[imp.cty=='TR'].copy(); t['val']=t.val.astype(float); t['qty']=pd.to_numeric(t.qty,errors='coerce').fillna(0)
t=t.groupby(['hs10','uom'],dropna=False).agg(val=('val','sum'),qty=('qty','sum')).reset_index()
tar=pd.read_csv(B+'raw/cbsa/tphs_2026-2.csv',dtype=str)
tar=tar[tar.TARIFF.str.match(r'^\d{4}\.\d{2}\.\d{2}$')].drop_duplicates('TARIFF')
tar['ti']=tar.TARIFF.str.replace('.','',regex=False)
mfn=dict(zip(tar.ti,tar.MFN.fillna('').str.strip()))
desc=dict(zip(tar.ti,tar.DESC1.fillna('')))
def parse(rate,val,qty,uom):
    r=rate.replace('¢','c')
    if r=='' : return None,'no rate found'
    if r=='Free': return 0.0,''
    adv=re.findall(r'([\d.]+)\s*%',r); spec_c=re.findall(r'([\d.]+)\s*c/kg',r); spec_d=re.findall(r'\$([\d.]+)/kg',r)
    flag=''
    if 'not less than' in r or 'not more than' in r: flag='min/max ignored'
    duty=0.0
    if adv: duty+=float(adv[0])/100*val
    sp=[float(x)/100 for x in spec_c]+[float(x) for x in spec_d]
    if sp and not ('not less than' in r and adv and r.find('%')<r.find('not less than')):
        if uom=='KGM': duty+=sp[0]*qty
        else: flag=(flag+'; ' if flag else '')+'specific rate not applied (UOM '+str(uom)+')'
    if not adv and not sp: return None,'unparsed: '+r
    return duty,flag
rows=[]
for _,x in t.iterrows():
    ti=x.hs10[:8]; rate=mfn.get(ti,'')
    d,f=parse(rate,x.val,x.qty,x.uom)
    rows.append(dict(hs10=x.hs10,tariff_item=ti,desc=desc.get(ti,'')[:80],uom=x.uom,value_cad=x.val,qty=x.qty,mfn_rate=rate,est_duty_cad=d,flag=f))
o=pd.DataFrame(rows).sort_values('value_cad',ascending=False)
o.to_csv(B+'outputs/ca_imports_from_TR_2025_est_mfn_duty.csv',index=False)
tot=o.value_cad.sum(); free=o[o.mfn_rate=='Free'].value_cad.sum()
print('total imports',tot,'dutiable-free share',free/tot)
print('est duty',o.est_duty_cad.sum(),'avg',o.est_duty_cad.sum()/tot)
print('unmatched value',o[o.est_duty_cad.isna()].value_cad.sum())
print(o[o.est_duty_cad.isna()].head(10)[['hs10','value_cad','mfn_rate','flag']])
print(o[o.flag!=''].value_cad.sum(),'value with flags')
o['hs2']=o.hs10.str[:2]
g=o.groupby('hs2').agg(val=('value_cad','sum'),duty=('est_duty_cad','sum')).sort_values('duty',ascending=False)
g['rate']=g.duty/g.val; print(g.head(15))
print(o.sort_values('est_duty_cad',ascending=False).head(20)[['hs10','desc','value_cad','mfn_rate','est_duty_cad']].to_string())
