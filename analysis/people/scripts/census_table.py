import json,csv
O='../people/'
r=json.load(open(O+'outputs/census_results.json'))
order=['Canada','Newfoundland and Labrador','Prince Edward Island','Nova Scotia','New Brunswick','Quebec','Ontario','Manitoba','Saskatchewan','Alberta','British Columbia','Yukon','Northwest Territories','Nunavut','Toronto (CMA), Ont.','Montréal (CMA), Que.','Vancouver (CMA), B.C.','Ottawa - Gatineau (CMA), Ont./Que.','Edmonton (CMA), Alta.','Calgary (CMA), Alta.','Kitchener - Cambridge - Waterloo (CMA), Ont.','Hamilton (CMA), Ont.','Winnipeg (CMA), Man.','Halifax (CMA), N.S.','Québec (CMA), Que.']
def g(p,geo,x):
    for row in r[p]:
        if row['geo']==geo and row['x']==x: return row['value']
    return None
cols=[('eth_total','98100356',1),('eth_single','98100356',2),('eth_multi','98100356',3),('pob_total','98100302',1),('pob_immigrants','98100302',3),('pob_nonPR','98100302',11),('pob_2016_21','98100302',10),('mt_total','98100181',1),('mt_single','98100181',2),('home_any','98100201',1)]
w=csv.writer(open(O+'outputs/census_turkish_by_geo.csv','w'))
w.writerow(['geography']+[c[0] for c in cols])
for geo in order:
    row=[geo]+[g(p,geo,x) for _,p,x in cols]; w.writerow(row); print(row)
print('periods Canada',[(x,g('98100302','Canada',x)) for x in range(1,12)])
print('periods Toronto',[(x,g('98100302','Toronto (CMA), Ont.',x)) for x in range(1,12)])
