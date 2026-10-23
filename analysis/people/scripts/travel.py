import json,subprocess,collections
O='../people/'
URL='https://www150.statcan.gc.ca/t1/wds/rest/getDataFromCubePidCoordAndLatestNPeriods'
def fetch(p,coords,n):
    body=json.dumps([{"productId":p,"coordinate":c,"latestN":n} for c in coords])
    r=subprocess.run(['curl','-sS','-m','180','-X','POST','-H','Content-Type: application/json','-d',body,URL],capture_output=True,text=True)
    return json.loads(r.stdout)
m=json.load(open(O+'raw/meta_24100050.json'))[0]['object']['dimension'][1]['member']
print('dim2 first',m[0])
a=fetch(24100050,['1.139.0.0.0.0.0.0.0.0','1.1.0.0.0.0.0.0.0.0'],140)
json.dump(a,open(O+'raw/wds_24100050_turkiye.json','w'))
res={}
for o in a:
    ob=o['object']; pts=ob['vectorDataPoint']
    ann=collections.defaultdict(float); cnt=collections.Counter()
    for p in pts:
        y=p['refPer'][:4]; ann[y]+=p['value'] or 0; cnt[y]+=1
    res[ob['coordinate']]={'vector':ob['vectorId'],'annual':dict(ann),'months':dict(cnt),'last':pts[-1]['refPer'],'monthly_2025_2026':{p['refPer'][:7]:p['value'] for p in pts if p['refPer']>='2025'}}
    print(ob['coordinate'],ob['vectorId'],dict(ann),dict(cnt))
b=fetch(24100080,['40.1.1.0.0.0.0.0.0.0','40.1.3.0.0.0.0.0.0.0','40.1.5.0.0.0.0.0.0.0','40.4.1.0.0.0.0.0.0.0','20.1.1.0.0.0.0.0.0.0'],40)
json.dump(b,open(O+'raw/wds_24100080_turkiye.json','w'))
for o in b:
    ob=o['object']
    if o['status']!='SUCCESS': print('FAIL',ob); continue
    pts=ob['vectorDataPoint']
    ann=collections.defaultdict(float); cnt=collections.Counter()
    for p in pts: ann[p['refPer'][:4]]+=p['value'] or 0; cnt[p['refPer'][:4]]+=1
    print(ob['coordinate'],ob['vectorId'],[(p['refPer'],p['value'],p['scalarFactorCode'],p.get('statusCode'),p.get('symbolCode')) for p in pts][-6:])
    print('  annual',dict(ann),dict(cnt))
    res[ob['coordinate']]={'vector':ob['vectorId'],'annual':dict(ann),'quarters':dict(cnt),'points':[(p['refPer'],p['value'],p['scalarFactorCode']) for p in pts]}
json.dump(res,open(O+'outputs/travel_results.json','w'),indent=1)
