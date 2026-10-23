import sys,json,csv
sys.path.insert(0,'../people/scripts')
from ircc_xlsx import annual
O='../people/'
rows,hr,yc,data=annual(O+'raw/ircc/EN_ODP-PR-Citz.xlsx')
out=[]
for y in yc:
    vals=sorted([(v.get(y) or 0,k) for k,v in data.items() if k!='Total' and 'Not stated' not in k],reverse=True)
    rank=[k for _,k in vals].index('Turkey')+1
    t=data['Turkey'][y]; tot=data['Total'][y]
    out.append({'year':y,'turkey_pr':t,'rank':rank,'n_countries':len(vals),'total_pr':tot,'share_pct':round(100*t/tot,2)})
    print(out[-1])
# monthly 2026
r=[x for x in rows if x and x[0]=='Turkey'][0]
print('header months',rows[hr+1][187:200]); print('2026 vals',r[187:200])
print('2025 vals',r[170:187])
json.dump(out,open(O+'outputs/pr_turkey_by_year.json','w'),indent=1)
csv.DictWriter(open(O+'outputs/pr_turkey_by_year.csv','w'),fieldnames=out[0].keys()).writerows([dict(zip(out[0].keys(),out[0].keys()))]+out)
