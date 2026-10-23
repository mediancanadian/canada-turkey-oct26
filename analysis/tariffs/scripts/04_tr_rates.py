"""Parse Türkiye 2026 consolidated Import Regime (Karar 3350) lists and Additional Customs Duty (IGV, Karar 3351) tables
from Ministry of Trade Excel files. Output the rate applying to Canada = 'Diğer Ülkeler' (DÜ / column 7) column."""
import openpyxl, re, pandas as pd, glob, sys
X='../tariffs/raw/tr/xl/'
OUT='../tariffs/outputs/'
def norm(c):
    if c is None: return None
    s=re.sub(r'\D','',str(c).strip())
    if len(s)==11: s='0'+s
    return s if len(s)==12 else None
def num(v):
    if v is None or v=='': return None
    s=str(v).strip().replace(',','.')
    m=re.match(r'^-?\d+(\.\d+)?',s)
    return float(m.group()) if m else s
recs=[]
def parse(f, src, du_col_finder):
    wb=openpyxl.load_workbook(X+f,read_only=True,data_only=True)
    for ws in wb.worksheets:
        rows=list(ws.iter_rows(values_only=True))
        # find header row containing DÜ/D.Ü./Diğer or numeric 7
        ci=du_col_finder(rows)
        if ci is None: 
            print('no DU col',f,ws.title,file=sys.stderr); continue
        for r in rows:
            if not r or len(r)<=ci: continue
            c=norm(r[0])
            if c: recs.append(dict(gtip=c,src=src,sheet=ws.title,foot=r[1],du=num(r[ci]),raw=r[ci]))
def by_label(rows):
    for r in rows[:8]:
        for i,v in enumerate(r):
            if v is not None and re.sub(r'[\s.]','',str(v)) in ('DÜ','D.Ü','DÜ.'.replace('.','')): return i
    for r in rows[:8]:
        for i,v in enumerate(r):
            if v is not None and str(v).strip() in ('7','7.0') or v==7: return i
    return None
for f in glob.glob(X+'rej_*.xlsx'):
    f=f.split('/')[-1]
    if any(k in f for k in ['_V_','_VI_','_VII_','EK-1']): continue
    parse(f,'GV_'+f,by_label)
parse('igv_EK-1.xlsx','IGV_Ek1',by_label)
parse('igv_EK_2_-3.xlsx','IGV_Ek2_3',by_label)
d=pd.DataFrame(recs)
d.to_csv(OUT+'tr_2026_rates_DU_all.csv',index=False)
print(d.groupby('src').size())
