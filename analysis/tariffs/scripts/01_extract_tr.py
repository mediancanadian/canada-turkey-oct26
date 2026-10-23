import pandas as pd, sys
base='../tariffs/raw/statcan/'
out='../tariffs/outputs/'
imp=pd.read_csv(base+'CIMT-CICM_Imp_2025/ODPFN014_202512N.csv',dtype={0:str,1:str},usecols=[0,1,2,5])
imp.columns=['ym','hs10','cty','val']
t=imp[imp.cty=='TR']
t.groupby('hs10').val.sum().reset_index().to_csv(out+'imports_from_TR_2025_hs10.csv',index=False)
print('imports TR total',t.val.sum(),'all',imp.val.sum())
ex=pd.read_csv(base+'CIMT-CICM_Dom_Exp_2025/ODPFN016_202512N.csv',dtype={0:str,1:str},usecols=[0,1,2,5])
ex.columns=['ym','hs8','cty','val']
e=ex[ex.cty=='TR']
e.groupby('hs8').val.sum().reset_index().to_csv(out+'domexports_to_TR_2025_hs8.csv',index=False)
print('domexp TR total',e.val.sum())
