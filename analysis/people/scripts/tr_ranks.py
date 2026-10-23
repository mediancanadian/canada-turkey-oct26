import sys,json,openpyxl; sys.path.insert(0,'../people/scripts')
from ircc_xlsx import annual
O='../people/'
def ye(path):
    ws=openpyxl.load_workbook(path,read_only=True).worksheets[0]
    rows=[list(r) for r in ws.iter_rows(values_only=True)]
    hdr=rows[2]; yc={str(c):j for j,c in enumerate(hdr) if c and str(c).isdigit()}
    d={}
    for r in rows[3:]:
        if not r or not isinstance(r[0],str) or r[0].startswith('Note'): continue
        d[r[0].strip()]={y:(None if str(r[j])=='--' else float(str(r[j]).replace(',',''))) for y,j in yc.items() if j<len(r) and r[j] not in (None,'')}
    return d
res={}
for name,f,kind in [('study_dec31','study_citz_dec31.xlsx','ye'),('imp_dec31','imp_citz_dec31_all.xlsx','ye'),('tfwp_dec31','tfwp_citz_dec31.xlsx','ye'),('study_effective','study_citz_effective.xlsx','an'),('imp_effective','imp_citz_effective.xlsx','an'),('tfwp_effective','tfwp_citz_effective.xlsx','an'),('new_citizens_cob','new_citizens_cob.xlsx','an')]:
    d=ye(O+'raw/ircc/'+f) if kind=='ye' else annual(O+'raw/ircc/'+f)[3]
    totk=[k for k in d if k.startswith('Total')][0]
    out={}
    for y in sorted(d['Turkey']):
        if int(y)<2015: continue
        s=sorted([(v.get(y) or 0,k) for k,v in d.items() if not k.startswith('Total') and k!='Not stated'],reverse=True)
        out[y]={'turkey':d['Turkey'][y],'rank':[k for _,k in s].index('Turkey')+1,'total':d[totk].get(y)}
    res[name]=out; print(name,{y:(v['turkey'],v['rank']) for y,v in out.items()})
json.dump(res,open(O+'outputs/temp_residents_turkey.json','w'),indent=1)
