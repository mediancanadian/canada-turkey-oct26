"""Combine parsed outputs into exports_turkiye_2010_2025.csv."""
import json,csv
O='../defence/outputs/'
a=json.load(open(O+'exports_2010_2013_parsed.json')); b=json.load(open(O+'exports_by_year_parsed.json'))
official_total={'2010':408513736,'2011':634542198,'2012':1042277613,'2013':681366082,'2014':796613343,'2015':676431004,'2016':717700000,'2017':1031000000,'2018':2069000000,'2019':3757000000,'2020':1966000000,'2021':2730664660.84,'2022':2122000000,'2023':2143000000,'2024':2504000000,'2025':2045095824.74}
rows=[]
for y in sorted(set(a)|set(b)):
    r=a.get(y) or b.get(y)
    ecl=b.get(y,{}).get('ecl',{})
    rows.append({'year':y,'turkiye_value_cad':r['turkiye_value'],'turkiye_rank_non_us':r['turkiye_rank'],
      'destinations_with_exports':r['n_destinations_parsed'],'official_total_non_us_cad':official_total[y],
      'turkiye_share_pct':round(100*r['turkiye_value']/official_total[y],2),
      'ecl_2_5':ecl.get('2-5',''),'ecl_2_15':ecl.get('2-15',''),'ecl_all':json.dumps(ecl)})
with open(O+'exports_turkiye_2010_2025.csv','w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
for r in rows: print(r['year'],r['turkiye_value_cad'],r['turkiye_rank_non_us'],r['turkiye_share_pct'])
