import json,glob,collections,sys
d=sys.argv[1]
rows=[]
for f in glob.glob(d+'/reactors_*.json'):
    rows+=json.load(open(f))['items']
print('total units',len(rows))
for x in rows:
    if x['countryCode']=='TR':
        print({k:x[k] for k in ('unitName','statusName','model','netElectricalCapacity','constructionDate','criticalityDate','gridDate','ownerName','operatorName','reactorSupplierName')})
op=[x for x in rows if x['statusName']=='Operational']
print('operational',len(op),'net MW',sum(x['netElectricalCapacity'] or 0 for x in op))
phwr=[x for x in op if x['typeCode']=='PHWR']
print('operational PHWR',len(phwr),collections.Counter(x['countryCode'] for x in phwr))
candu=[x for x in op if x['typeCode']=='PHWR' and ('CANDU' in (x['model'] or '').upper() or 'AECL' in (x['reactorSupplierName'] or '').upper() or 'CANDU' in (x['reactorSupplierName'] or '').upper())]
print('operational CANDU-labelled',len(candu),collections.Counter(x['countryCode'] for x in candu))
for x in phwr:
    if x not in candu: pass
print('non-CANDU-labelled PHWR by country/model', collections.Counter((x['countryCode'],x['model'],x['reactorSupplierName']) for x in phwr if x not in candu).most_common(40))
uc=[x for x in rows if x['statusName']=='Under Construction' and x['typeCode']=='PHWR']
print('PHWR under construction',collections.Counter((x['countryCode'],x['model']) for x in uc))
