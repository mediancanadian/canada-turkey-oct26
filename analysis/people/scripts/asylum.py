import sys,json; sys.path.insert(0,'../people/scripts')
from ircc_xlsx import annual
O='../people/'
rows,hr,yc,d=annual(O+'raw/ircc/asylum_top25_lastyear.xlsx')
tk=[k for k in d if 'Turkey' in k][0]
# office rows follow the country row
idx=[i for i,r in enumerate(rows) if r and r[0]==tk][0]
off={}
for r in rows[idx+1:idx+5]:
    if r and r[0] in ('Airport','Border','Inland','Other offices'):
        off[r[0]]={y:(None if str(r[j])=='--' else float(str(r[j]).replace(',',''))) for y,j in yc.items() if j<len(r) and r[j] not in (None,'')}
countries={k:v for k,v in d.items() if k.startswith('(')}
ranks={}
for y in yc:
    s=sorted([(v.get(y) or 0,k) for k,v in countries.items()],reverse=True)
    ranks[y]=[k for _,k in s].index(tk)+1
out={'turkey':d[tk],'total_all_countries':d['Total'],'turkey_by_office':off,'rank_among_2025_top25':ranks,'label':tk}
print(json.dumps(out,indent=1))
json.dump(out,open(O+'outputs/asylum_turkey.json','w'),indent=1)
