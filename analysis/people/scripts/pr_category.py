import csv,collections,json
O='../people/'
r=csv.DictReader(open(O+'raw/ircc/ODP-PR-Citz_immcat.csv',encoding='utf-8-sig'),delimiter='\t')
agg=collections.defaultdict(lambda:collections.defaultdict(int)); sup=collections.defaultdict(int)
for row in r:
    if row['EN_COUNTRY_OF_CITIZENSHIP']!='Turkey': continue
    v=row['TOTAL'].replace(',','')
    if v=='--': sup[row['EN_YEAR']]+=1; v=0
    agg[(row['EN_IMMIGRATION_CATEGORY-MAIN_CATEGORY'],row['EN_IMMIGRATION_CATEGORY-GROUP'])][row['EN_YEAR']]+=int(v or 0)
res={f'{a} | {b}':dict(sorted(d.items())) for (a,b),d in sorted(agg.items())}
for k,d in res.items(): print(k,d)
print('suppressed cells per year',dict(sup))
json.dump({'by_category_sum_of_rounded_monthly':res,'suppressed_cells':sup},open(O+'outputs/pr_turkey_by_category.json','w'),indent=1)
