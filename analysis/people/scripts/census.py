import json,subprocess,sys
OUT='../people/'
URL='https://www150.statcan.gc.ca/t1/wds/rest/getDataFromCubePidCoordAndLatestNPeriods'
def meta(p):
    d=json.load(open(OUT+f'raw/meta_{p}.json'))[0]['object']
    return {m['memberId']:m['memberNameEn'] for m in d['dimension'][0]['member']}
def geos(p):
    g=meta(p); keep=[]
    for k,v in g.items():
        if '(' not in v or any(c in v for c in ['Toronto (CMA)','Montréal (CMA)','Vancouver (CMA)','Ottawa - Gatineau (CMA), Ont./Que.','Calgary (CMA)','Edmonton (CMA)','Kitchener','Hamilton (CMA)','Winnipeg (CMA)','Halifax (CMA)','Québec (CMA)']):
            if 'part' not in v: keep.append(k)
    return keep,g
def fetch(p,coords):
    body=json.dumps([{"productId":int(p),"coordinate":c,"latestN":1} for c in coords])
    r=subprocess.run(['curl','-sS','-m','180','-X','POST','-H','Content-Type: application/json','-d',body,URL],capture_output=True,text=True)
    return json.loads(r.stdout)
specs={
 '98100356':('ethnic_turkish',lambda g,x:f"{g}.1.1.1.437.{x}.0.0.0.0",[1,2,3]),
 '98100302':('pob_turkey',lambda g,x:f"{g}.1.1.1.1.220.{x}.0.0.0",list(range(1,12))),
 '98100181':('mt_turkish',lambda g,x:f"{g}.1.1.528.{x}.0.0.0.0.0",[1,2,3]),
 '98100201':('home_turkish',lambda g,x:f"{g}.1.1.528.{x}.0.0.0.0.0",[1,2,3]),
}
res={}
for p,(name,f,xs) in specs.items():
    keep,g=geos(p)
    coords=[f(k,x) for k in keep for x in xs]
    out=[]
    for i in range(0,len(coords),100):
        out+=fetch(p,coords[i:i+100])
    json.dump(out,open(OUT+f'raw/wds_{p}_{name}.json','w'))
    rows=[]
    for o in out:
        if o.get('status')!='SUCCESS': print('FAIL',p,o); continue
        ob=o['object']; c=ob['coordinate'].split('.')
        v=ob['vectorDataPoint'][0]['value'] if ob['vectorDataPoint'] else None
        rows.append({'geo':g[int(c[0])],'x':int({'98100356':c[5],'98100302':c[6],'98100181':c[4],'98100201':c[4]}[p]),'value':v,'vector':ob['vectorId']})
    res[p]=rows
json.dump(res,open(OUT+'outputs/census_results.json','w'),indent=1,ensure_ascii=False)
for p,rows in res.items():
    print(p,specs[p][0])
    for r in rows: print('  ',r)
