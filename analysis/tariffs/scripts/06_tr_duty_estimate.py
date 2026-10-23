"""Estimate Turkish customs duties on Canada's 2025 domestic exports to Türkiye.
Trade: StatCan CIMT 2025 domestic exports to TR (HS8 Canadian export codes, CAD, FOB-type export value).
Rates: Türkiye 2026 Import Regime (Karar 3350 consolidated, Ministry of Trade Excel, 'Diğer Ülkeler'/col 7 = rate for Canada)
       plus Additional Customs Duty (IGV, Karar 3351 consolidated Ek-1/2/3, 'Diğer Ülkeler'/col 7).
Matching at HS6: if all Turkish 12-digit lines in the HS6 share a rate, use it; otherwise use explicit picks below,
else the simple average of lines (flagged). Specific duties (EMY per tonne) not included. End-use 0% for civil aircraft applied where noted."""
import pandas as pd, numpy as np
B='../tariffs/'
ex=pd.read_csv(B+'outputs/domexports_to_TR_2025_hs8.csv',dtype={'hs8':str})
desc={}
for l in open(B+'raw/statcan/CIMT-CICM_Dom_Exp_2025/ODPF_2_HS8Desc.TXT',encoding='latin1'): desc[l[:8]]=l[8:].strip()[23:110]
r=pd.read_csv(B+'outputs/tr_2026_rates_DU_all.csv',dtype={'gtip':str})
r['hs6']=r.gtip.str[:6]
gv=r[r.src.str.startswith('GV')].copy(); igv=r[r.src.str.startswith('IGV')].copy()
gv['du']=pd.to_numeric(gv.du,errors='coerce'); igv['du']=pd.to_numeric(igv.du,errors='coerce')
# explicit picks (Canadian HS8 -> Turkish 12-digit line), from 2026 TGTC (Karar 10781) descriptions
pick={'07134095':'071340000013',  # red lentils
      '07134094':'071340000012',  # green lentils
      '07134010':'071340000011',  # lentil seed
      '07132091':'071320000019',  # chickpeas other than seed
      '07132010':'071320000011',  # chickpea seed
      }
civil_air_zero={'8802','8807','8411'}  # end-use footnotes (1)/(b)/(a): 0% if civil aircraft / for civil aircraft
rows=[]
for _,x in ex.iterrows():
    h6=x.hs8[:6]; flag=''
    if x.hs8 in pick:
        g=gv[gv.gtip==pick[x.hs8]].du.mean(); note='line '+pick[x.hs8]
    else:
        s=gv[gv.hs6==h6].du.dropna()
        if len(s)==0: g=np.nan; note='no GV line'
        elif s.nunique()==1: g=s.iloc[0]; note='uniform'
        else: g=s.mean(); note=f'avg of {len(s)} lines {s.min()}-{s.max()}'; flag='mixed'
    if h6[:4] in civil_air_zero:
        note+='; civil-aircraft end-use 0% assumed'; g0=g; g=0.0
    s2=igv[igv.hs6==h6].du.dropna()
    n6=(gv.hs6==h6).sum()
    ig=0.0 if len(s2)==0 else s2.sum()/max(n6,1)  # lines without IGV entry have 0
    if len(s2) and h6[:4] in civil_air_zero: ig=0.0
    rows.append(dict(hs8=x.hs8,desc=desc.get(x.hs8,''),value_cad=x.val,tr_gv_pct=g,tr_igv_pct=ig,note=note,flag=flag))
o=pd.DataFrame(rows)
o['total_pct']=o.tr_gv_pct.fillna(0)+o.tr_igv_pct
o['est_duty_cad']=o.value_cad*o.total_pct/100
o=o.sort_values('value_cad',ascending=False)
o.to_csv(B+'outputs/ca_exports_to_TR_2025_est_tr_duty.csv',index=False)
tot=o.value_cad.sum()
print('total',tot,'est duty',o.est_duty_cad.sum(),'avg',o.est_duty_cad.sum()/tot)
print('duty-free share',o[o.total_pct==0].value_cad.sum()/tot)
print('no rate value',o[o.tr_gv_pct.isna()].value_cad.sum())
print('mixed value share',o[o.flag=='mixed'].value_cad.sum()/tot)
print(o.head(30)[['hs8','desc','value_cad','tr_gv_pct','tr_igv_pct','est_duty_cad','note']].to_string())
print(o.sort_values('est_duty_cad',ascending=False).head(15)[['hs8','desc','value_cad','total_pct','est_duty_cad']].to_string())
